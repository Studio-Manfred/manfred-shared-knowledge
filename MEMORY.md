# MEMORY.md

A self-learning log for `manfred-shared-knowledge`. Each session appends what was decided, what was learned, and where work was left. Read this before starting a new session — it answers "what's the state of the world here?" without rereading the whole transcript.

**Format rules:**
- New sessions append at the top (newest first).
- Each entry: date, scope, what changed, what was learned, what's open.
- "Lessons" promote to the **Standing lessons** section once they recur or feel durable.
- Don't delete old entries — they're the audit trail.

---

## Standing lessons (apply across sessions)

Promoted from session entries when they prove durable. Read these first.

### On building skills with TDD (per `superpowers:writing-skills`)

- **Baseline pressure scenarios are non-negotiable.** Three RED-phase agents without the skill surfaced rationalizations I'd never have predicted ("the snapshot is just a label change", "Linear MCP isn't available so I'll do it manually", "I'll glance at the dashboard while doing the next thing"). Those exact strings became the rationalization table in the skill. Skipping RED produces a skill that misses the actual failure modes.
- **REFACTOR-phase subagents catch ambiguity humans miss.** The typo-fix agent flagged that the cosmetic fast path didn't say what to do about Vercel-wait or step 8. Both real holes. A second pass after writing is cheap and high-value.
- **Reference docs only load on demand.** Putting Linear/Vercel call patterns in `references/*.md` instead of inline kept SKILL.md at ~280 lines. Future skill: keep heavy reference out of the body.

### On Linear MCP at Manfred

- Server name: `linear-server`. **Confirmed connected** at Manfred — don't assume it's unavailable.
- **Body strings must contain literal newlines, not `\n`.** The server explicitly says so. Easy to forget when programmatically constructing comments.
- **Linear "Project" ≠ "Milestone".** What people call a "milestone the work belongs to" is almost always a Linear *Project* (referenced via `issue.project`). Project milestones are separate sub-objects. The `release` skill operates on Projects.
- Identifiers like `STU-204` work directly in tool args (no need to resolve to UUIDs first).
- Workflow: comment first (`save_comment`), transition second (`save_issue` with `state`), then optionally append to project description (`save_project`). Comment-before-transition matters: if the transition errors, the comment is still on the ticket as audit trail.

### On Vercel-GitHub deploys

- `git push origin main` IS the production deploy at Manfred — the push is the trigger, not a separate "deploy" step.
- The tag should be pushed **after** Vercel reports `READY`, not before. A tag pointing at a broken commit is worse than a delayed tag.
- Linear updates run last — local checks passing ≠ Vercel building successfully. Don't claim "shipped" on Linear before Vercel confirms.
- Studio Manfred Vercel team slug: `studio-manfred`. `teamId` resolvable via `list_teams` or read from `.vercel/project.json`.

### On repo conventions

- Conventional commits (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`).
- CHANGELOG follows Keep a Changelog. `[Unreleased]` section gets promoted on each release.
- Skills live under `skills/<name>/SKILL.md`. Heavy references under `skills/<name>/references/`.
- Both `install.sh` and `uninstall.sh` have a `SKILLS=( … )` array that **must be updated together** when adding/removing a skill — easy to miss the second one.
- Production GitHub remote: `https://github.com/Studio-Manfred/manfred-shared-knowledge.git`. The repo was rehomed from `jens-wedin` to `Studio-Manfred` in v0.3.3/0.3.4 — repo name itself was kept, only the org changed. The separate `manfred-design_system` (with underscore) is a different repo.

---

## Sessions

### 2026-04-29 — Built `skills/release` (full TDD loop)

**Where we ended:**
- New skill `skills/release/SKILL.md` (~280 lines) + `references/linear-actions.md` + `references/vercel-wait.md` written.
- `install.sh`, `uninstall.sh`, `README.md` (12-skill table), `CHANGELOG.md` (`[Unreleased]`) all updated to include `release`.
- **Not yet committed or released.** Working tree dirty. Next step is `/deploy` (or rather, the new `release` skill — but the repo itself has no Vercel/Linear so `deploy` is fine here).
- Plan file: `/Users/jens.wedin/.claude/plans/i-want-to-create-linked-stearns.md`.

**What was built:**
- 12-step release workflow: pre-flight → 4 quality gates (lint+format, type+build, unit tests, a11y audit) → version bump → CHANGELOG → README → commit+push → wait Vercel `READY` → tag + GitHub Release → Linear updates (comment → transition → project note).
- Cosmetic-only fast path for docs/config-only changes (skips gates 3/4/5, still runs lint, still waits Vercel).
- Rationalization table built from three baseline pressure-test agents (just-ship-it, Linear-stale, typo-fix). Verbatim quotes from baselines became the table entries.

**What was learned this session:**
- The Linear MCP tool surface differs from my initial mental model. `save_comment` takes `issueId`, not `id`. `save_issue` for state changes uses the `state` parameter and accepts the identifier (`STU-204`). See standing lesson on Linear above.
- The cosmetic fast path in the first SKILL.md draft didn't address Vercel-wait or step 8 (README) — REFACTOR agent caught both. Patched.
- Pressure-test agents were generally more disciplined than I expected — they fixed the failing snapshot, smoke-tested prod, didn't auto-close milestones. The actual failure modes were silent skips (a11y, full test re-run after fix) and ordering errors (tag before Vercel green). The skill targets those specifically.

**Open / next:**
- Real-world dry-run on a Manfred Vite/React project with an open `STU-` ticket to verify the Linear/Vercel flow end to end. Until that's done, the skill is theoretically validated only.
- Cut a release of `manfred-shared-knowledge` itself to ship the new skill (likely v0.4.0 — minor bump, "Added" entry).
- Consider adding an E2E gate option for projects that maintain Playwright suites (currently in "out of scope"). Worth revisiting after the dry-run.

### 2026-04-29 — Repo rehomed to Studio-Manfred org (v0.3.4)

**Where we ended:** v0.3.4 tagged + pushed. Remote moved from `jens-wedin/manfred-shared-knowledge` to `Studio-Manfred/manfred-shared-knowledge`. All install/uninstall URLs, marketplace command, and cross-references updated. v0.3.3 tag had been pre-burned by abandoned local work — bumped to v0.3.4 instead of force-deleting.

**What was learned:**
- Repo *name* didn't change; only the *org* did. Initial pass over-corrected to `manfred-design-system`. Always verify repo name vs. org name separately when handling a transfer.
- A locally-tagged commit pointing at orphan work blocks tag reuse. Bumping past the conflict (v0.3.3 → v0.3.4) is safer than deleting the orphan tag.

---

## How to update this file

When closing a session:
1. Add a new dated entry under "Sessions" at the top.
2. Note: where work was left, what was decided, what's still open.
3. If a learning recurs across sessions or feels generally true, promote it to "Standing lessons".
4. Keep entries terse — bullets, not paragraphs. The point is fast re-orientation.
