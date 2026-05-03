---
name: release
description: Use when shipping a real release of a project that has tests, types, accessibility requirements, Vercel-GitHub deploys, or Linear tickets — situations where the lightweight `deploy` skill would skip quality gates, ignore Vercel build status, or forget to update the ticket. Triggers on "release", "ship to production", "ship STU-###", "cut a release with checks", "production deploy", or any deploy where pre-flight checks, Vercel verification, and Linear updates matter. Also activate when the user says "deploy this properly", "ship it for real", or asks about post-deploy ticket workflow.
---

# Release

## Overview

A production release at Manfred is more than `git push` and a tag. The push **is** the production deploy (Vercel-GitHub integration ships every commit on `main` to prod), so anything broken passes through to users unless gated locally. After the push, the work isn't done — Vercel can still fail, and Linear tickets only count as shipped when production is actually green.

This skill orchestrates that full sequence:

```
gates → docs → push → Vercel green → tag/release → Linear updates
```

The discipline this skill enforces: **no step claims success on behalf of a later step**. Tests passing locally don't mean Vercel will build. The tag being pushed doesn't mean prod is up. Linear is updated *last*, against verified production state, never in advance.

**REQUIRED BACKGROUND:** Familiarity with `superpowers:test-driven-development` (the same RED-GREEN-REFACTOR discipline that justifies why gates fail closed, not open).

## When to Use

- Shipping any code change that reaches production via Vercel-GitHub
- Any release where commits reference Linear tickets (`STU-###`)
- Any release where the project has tests, types, lint, or a11y requirements
- The user says "release", "ship to production", "ship STU-123", "deploy this properly"

**When NOT to use:**
- Quick docs-only commit on a non-production branch → just commit and push, no skill needed
- Internal tooling repos with no Vercel and no Linear → use the lightweight `deploy` skill instead
- A repo that has no tests, no types, no a11y, no Linear, AND no Vercel → `deploy` is fine

## Required tools

The skill assumes these are available. Check at the start of step 1; surface a clear error if any are missing rather than silently degrading.

- `git` and `gh` CLI (and `gh auth status` returns authenticated)
- `npm` (or detected equivalent: `pnpm`, `yarn`, `bun`, `pip`, etc.)
- **Linear MCP server** — `linear-server`. Confirmed connected at Manfred. Key tools: `mcp__linear-server__list_issues`, `get_issue`, `save_comment`, `save_issue`, `list_issue_statuses`, `list_milestones`, `get_milestone`, `save_project`. **These are real, available tools — do not assume they're missing because past experience suggests Linear-via-MCP is unusual. Confirm with a small read (e.g., `list_teams`) if uncertain, then proceed.**
- **Vercel MCP server** — `mcp__claude_ai_Vercel__list_deployments`, `get_deployment`, `get_deployment_build_logs`, `get_project`, `list_teams`. Required only if the repo deploys to Vercel.
- The `manfred-design-systems:a11y-qa` skill (for step 5)

If — in some other environment — Linear MCP tools genuinely return "not available", the agent says so explicitly and falls back to a printed manual checklist. Linear must not be skipped silently.

## Studio Manfred defaults

When working inside a Studio Manfred project, use these as the default identifiers (override only if the project clearly belongs elsewhere):

- **Vercel team:** `studio-manfred` (dashboard: https://vercel.com/studio-manfred)
- **GitHub org:** `Studio-Manfred` (https://github.com/Studio-Manfred)
- **Linear workspace:** `studio-manfred` (https://linear.app/studio-manfred)
- **Linear ticket prefix:** `STU-` (e.g., `STU-204`)

The Vercel `teamId` (required by the Vercel MCP tools) can be resolved from the slug `studio-manfred` via `mcp__claude_ai_Vercel__list_teams`, or read from `.vercel/project.json` if the project has been linked locally.

## The 12 steps

Each step has a single responsibility and either passes (continue) or fails (stop). No step is "best-effort". A failed gate that gets ignored is the failure mode this skill exists to prevent.

### 1. Pre-flight context

- Read `git status`, `git describe --tags --abbrev=0`, `git log <last-tag>..HEAD --oneline`, current branch.
- Detect stack: `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`. If multiple match, ask user.
- Detect Vercel: presence of `vercel.json`, or `gh repo view --json deployments` showing Vercel, or asking user. Capture the Vercel `projectId` and `teamId` (from `.vercel/project.json` or `mcp__claude_ai_Vercel__list_projects`).
- Detect production branch from `vercel.json` (`git.deploymentEnabled.<branch>: true`) or by asking. **If the current branch is not the production branch, skip step 11 (Vercel wait) and tell the user why.**
- Read `CHANGELOG.md`, `README.md`, `package.json` (or equivalent version file).

No edits in this step. The output is a one-page situation report the user can sanity-check before any gate runs.

### 2. Quality gate: lint + format

Run the project's lint and format-check commands. Detect by `package.json` scripts (`lint`, `format:check`, `format`, `prettier:check`) or by tool presence (`.eslintrc*`, `.prettierrc*`, `biome.json`).

- Pass → continue.
- Fail → **stop**. Print which file/rule. Do not auto-fix unless the user explicitly says so. Never silence a rule "for the release". The release waits.
- N/A → mark as skipped with the reason, continue. (Example: a Python repo without ruff. The skill doesn't fabricate a linter that isn't there.)

### 3. Quality gate: type check + build

- Type check: `tsc --noEmit` for TS, `mypy` for Python, etc. Detected by config files.
- Build: the project's build command (`npm run build`, `vite build`, `next build`).
- Both must pass before continuing. Type check first — it's faster and catches more.
- N/A → mark and continue.

### 4. Quality gate: unit tests

Run the project's test command (`npm test`, `vitest run`, `pytest`, `cargo test`). Run **all** tests, not a scoped subset. If a single file changed, the temptation is to scope to that file — resist it. The whole point of a release gate is to catch the test you didn't think to scope to.

- Pass → continue.
- Fail → **stop**. The fix is to fix or revert the test, not to skip it. See the rationalization table.
- N/A → mark and continue.

### 5. Quality gate: accessibility audit

Invoke the `manfred-design-systems:a11y-qa` skill. Wait for it to return a pass/fail result. Do not just suggest running it.

- The audit is part of the release. "We can audit later" turns into "we never audit". The skill's a11y-qa results are the gate.
- N/A only when the project has no UI surface (a CLI, a worker, an API-only service). The a11y-qa skill itself reports "no UI to audit" in that case.
- Fail → **stop**. The user decides whether to fix-forward or revert; the skill does not ship red a11y.

### 6. Version bump proposal

Same logic as the lightweight `deploy` skill:
- `BREAKING CHANGE` or `!` after type → major
- Any `feat:` → minor
- Only `fix:`/`docs:`/`chore:`/`refactor:`/`test:` → patch
- No previous tag → propose `0.1.0` (early-stage) or `1.0.0` (mature) — ask user.

State the proposal and the reasoning ("2 features + 1 fix → 1.4.0 → 1.5.0"). Wait for confirmation.

### 7. Update CHANGELOG.md

Keep a Changelog format. Promote `[Unreleased]` to the new version with today's date. Bucket commits into Added / Changed / Fixed / Removed. **Rewrite raw commit messages into human-readable lines** — readers shouldn't have to decode `feat(checkout): add coupon code field (STU-318)` into "you can now use coupon codes at checkout".

Group related commits. Two `feat:` commits about the same thing become one user-facing line. Keep ticket refs (`STU-###`) in the changelog entry — they survive into Linear comments later.

### 8. Update README.md (when warranted)

Update README only when commits introduce user-visible changes: new feature, changed API, new requirement, removed functionality. Otherwise tell the user "skipping README — no user-visible changes".

Modify in place. Don't append "v1.5.0 changes" — the README documents the current state, not the diff.

### 9. Commit + push

Stage **only** `CHANGELOG.md`, `README.md`, and any version-file edits (`package.json`, `pyproject.toml`). Never `git add .` or `git add -A`. One commit:

```
chore(release): vX.Y.Z
```

Before pushing, surface to the user — explicitly:

> "Pushing to `main` will trigger a Vercel production deploy. The deploy will hit users when Vercel finishes building. Continue?"

Push only after confirmation. Use `git push origin <branch>`.

**Do not push the tag yet.** The tag is created and pushed in step 10, *after* Vercel confirms the build. Pushing the tag now leaves an artifact pointing at a commit that may turn out to be broken in production.

### 10. Wait for Vercel deploy

Only when Vercel was detected in step 1.

Use `mcp__claude_ai_Vercel__list_deployments` (filtered to `since` ~30s before the push) to find the deployment matching the commit SHA. Then `mcp__claude_ai_Vercel__get_deployment` polled every 10s until state is one of `READY`, `ERROR`, or `CANCELED`. Default ceiling: 10 minutes. See [references/vercel-wait.md](references/vercel-wait.md).

- `READY` → capture the production URL. Continue.
- `ERROR` → fetch `get_deployment_build_logs`, surface the failure in the conversation, **stop**. Do not tag, do not touch Linear.
- `CANCELED` → ask the user (probably superseded by a newer push).
- Timeout → ask the user whether to keep waiting or stop.

When Vercel is detected but the current branch is *not* the production branch, this step is skipped — the push went to a preview, not prod. Tell the user why so they can choose to merge to main if they actually wanted prod.

### 11. Tag + GitHub Release

Now that prod is verified green:

```
git tag -a vX.Y.Z -m "Release vX.Y.Z"
git push origin vX.Y.Z
```

If `.github/workflows/*.yml` contains `on: release: types: [created]`, also create the GitHub Release so the publish workflow fires:

```
gh release create vX.Y.Z --title "vX.Y.Z" --notes-from-tag
```

A pushed tag alone does NOT trigger release-event workflows. If you skip the Release object, nothing publishes. Check workflows; create the Release when needed.

### 12. Linear updates

Only after step 10 succeeded (or was skipped because no Vercel).

**Discover tickets:** scan `git log <last-tag>..HEAD` and the branch name for `STU-###` references. Deduplicate. If none found, ask the user: "No Linear refs found in commits or branch — should I skip Linear, or do you have a ticket ID?"

**For each ticket — comment first, transition second:**

1. `mcp__linear-server__save_comment({ issueId: "STU-###", body: "..." })` — release version, GitHub release URL, Vercel production URL (when available), and a changelog excerpt scoped to that ticket. **Body uses literal newlines, not `\n`.**
2. `mcp__linear-server__save_issue({ id: "STU-###", state: "Done" })` to transition state. Ask the user once for the target state (resolve via `list_issue_statuses` if unsure of the team's exact name); apply to all matched tickets.
3. If the ticket has a `project` (Linear Project — at Manfred this is what people often call "the milestone"), append a one-line note to the project description via `save_project({ id: "<projectId>", description: "<existing + new line>" })`. **Do not auto-close the project** — projects usually have siblings still in flight. Closing is the user's call. Skip silently if the project lookup fails — it's a nicety, not a gate.

See [references/linear-actions.md](references/linear-actions.md) for exact tool arguments, comment format, and project vs milestone semantics.

## Quick reference

| Step | Action | Confirmation needed? | Stop on fail? |
|---|---|---|---|
| 1 | Pre-flight context | No | If required tools missing |
| 2 | Lint + format | No | Yes |
| 3 | Type check + build | No | Yes |
| 4 | Unit tests | No | Yes |
| 5 | a11y audit | No | Yes |
| 6 | Version bump proposal | **Yes** | — |
| 7 | Write CHANGELOG | No | — |
| 8 | Update README (if warranted) | No | — |
| 9 | Commit + push to `main` | **Yes** (deploy trigger) | — |
| 10 | Wait for Vercel | No | Yes (ERROR) |
| 11 | Tag + GitHub Release | **Yes** | — |
| 12 | Linear updates | Once for target state | — |

## Cosmetic-only release (fast path)

When **all** commits since the last tag are documentation/config-only (no `.ts`, `.tsx`, `.js`, `.py`, `.css`, etc. — only `.md`, `.gitignore`, license, etc.), gates 3, 4, and 5 are N/A.

The agent must:
1. **Declare it explicitly:** "All commits since v3.0.2 touch only documentation files. Skipping type check, unit tests, and a11y audit. Lint+format still runs on .md. Vercel wait still applies."
2. Run gate 2 (lint+format catches markdown lint and prettier). Skip 3, 4, 5.
3. Treat as a patch bump and continue normally, unless the project explicitly skips tags for docs-only changes (rare — confirm with user if in doubt).
4. Step 8 (README update): N/A in the fast path. The typo fix *is* the README change; no separate edit is warranted.
5. **Step 10 (Vercel wait) still applies.** Even a one-character README change goes through a real Vercel build — postinstall hooks, build cache invalidation, env var drift can all still fail. The discipline "no step claims success on behalf of a later step" is independent of how trivial the change looks. Wait for `READY`.
6. **Step 12 (Linear)** runs only if a `STU-###` is referenced. Cosmetic changes typically have no ticket → ask user, accept skip.

The skill rejects the inverse: "this is just a snapshot update" or "the lint failure is unrelated" or "the a11y audit takes 6 minutes and we're in a hurry" — those are not cosmetic releases. Cosmetic = the file types changed are inert. A snapshot file is test code; a config change is config; a label change is UI.

## Rationalization table

These are the actual rationalizations agents used in baseline tests. They're traps. Each one means: stop, do the thing properly.

| Rationalization | What it actually means | Correct action |
|---|---|---|
| "The snapshot is just a label change, nothing real broke." | The agent is asking permission to ship a red test. | Fix the snapshot, re-run all unit tests, confirm green. Then continue. |
| "I'd re-run full CI on a normal Tuesday; not at 16:53." | "I want to skip a gate because I'm in a hurry." Hurry doesn't change risk. | Run gate 4. 90 seconds is not the bottleneck; a broken prod is. |
| "Build artifacts don't depend on snapshot files." | True in isolation, false as a release rule. After *any* code change, re-run gates. | Re-run gates 3 and 4 after the snapshot fix. |
| "Vercel is atomic — if it fails it keeps the previous deploy." | True, but the *tag* and the *Linear update* are not atomic. They claim "v1.5.0 shipped" before prod is verified. | Push code → wait Vercel → THEN tag and update Linear. The order is the discipline. |
| "I'll glance at the Vercel dashboard tab while doing the next thing." | "I'm not going to actually wait." | The skill polls programmatically. Continue only on `READY`. |
| "The a11y audit takes 6 minutes — running it on a one-char change is cargo-cult." | True for a documentation-only change (declare it, take the fast path). False as a general rule. | If commits include any code/UI change, run gate 5. No exceptions. |
| "I won't pretend to call tools I don't have." (about Linear MCP) | Confirm before assuming missing. The Linear MCP server is real and configured globally at Manfred. | List the available `mcp__linear-server__*` tools first. Only fall back to manual after a tool actually returns "not available". |
| "Ship it, then clean up." | "I'm going to commit broken work and promise to fix it later." | If a gate fails, fix it before pushing. Retroactive cleanup is how `main` rots. |
| "Process exists to catch risk proportional to the change." | True — and the proportional response is the **cosmetic fast path**, declared explicitly. Not silent skipping. | Use the fast path. Tell the user which gates were skipped and why. |
| "All local checks passed — Linear's safe to update." | Local ≠ production. Vercel can fail on env vars, edge runtime, build timeouts. | Wait for Vercel `READY`. Only then update Linear. |

## Red flags — STOP and re-read this skill

If you catch yourself thinking any of these, stop and walk through the steps again:

- "I'll skip the a11y audit just this once."
- "The failing test isn't related to my change."
- "I'll push the tag now and check Vercel after."
- "Linear can wait until tomorrow."
- "I don't have Linear tools" (without checking).
- "The build failure is intermittent — let me re-run the push."
- "I'll do CHANGELOG after I push, while Vercel is building."
- "We need to ship in 10 minutes — let me skip [step]."

Each of those is the rationalization the skill exists to refuse.

## Edge cases

| Situation | Behavior |
|---|---|
| No `STU-###` anywhere in commits/branch | Ask user. Accept "skip Linear". |
| Project has no test/lint script | Mark gate as N/A. Don't fabricate. |
| Dirty working tree at start of step 1 | Warn. Ask: stash, commit first, or abort. |
| Monorepo | Ask which package. Run gates scoped to that package. |
| Re-run after gate failure | Detect existing changelog draft for the unreleased version. Continue, don't double-bump. |
| Branch is not the Vercel production branch | Skip step 10. Tell user the push went to a preview deploy, not prod. |
| Vercel build fails (`ERROR`) | Surface logs. Stop. Tell user: "the commit is on `main` but Vercel rejected it — fix-forward or revert is your call." Do not touch Linear. |
| `gh auth status` not authenticated | Stop in step 1 with a clear message. Don't proceed and silently skip the GitHub Release. |
| User says "skip Linear / skip Vercel / skip a11y" | Honor the request, but log it as a deliberate override in the final summary so it's auditable. |

## Common mistakes

- **Pushing the tag before Vercel verifies.** The tag becomes a misleading marker pointing at a broken commit. Always: push code → wait Vercel → then tag.
- **Updating Linear before Vercel `READY`.** Linear ends up claiming a release that failed in production. Always Vercel first.
- **Silent gate skipping.** Skipping a gate without surfacing it in the conversation. The user must see "skipped X because Y" in the summary.
- **Auto-closing milestones.** A milestone usually has siblings still in flight. Comment yes, transition no — ask the user explicitly.
- **Staging extra files.** `git add CHANGELOG.md README.md package.json` — by name. Never `-A` or `.`.
- **Skipping the GitHub Release when a publish workflow needs it.** A pushed tag does not fire `release: types: [created]` workflows.
- **Treating "the test failure is unrelated" as a green light.** It isn't.

## Cross-references

- `manfred-design-systems:a11y-qa` — gate 5
- `superpowers:test-driven-development` — discipline for why gates fail closed
- `deploy` skill (lightweight sibling) — when this skill is overkill
- [references/linear-actions.md](references/linear-actions.md) — Linear MCP call patterns
- [references/vercel-wait.md](references/vercel-wait.md) — Vercel polling pattern
