---
name: test-my-code
description: Use when a user finishes a Vite/React feature (vitest + Playwright stack) and asks for QA, code testing, production-readiness check, or pre-merge verification — phrases like "test my code", "run QA", "is this ready to ship", "check before prod", "before I deploy".
---

# test-my-code

## Overview

QA gate for Vite/React features after implementation. Runs a sequence of automated checks, saves a report file, and posts a summary to the linked Linear ticket. Built for non-developer users — be opinionated, run the full gate without asking permission between steps.

## When to Use

- User says: "test my code", "run QA", "is this ready to ship", "check before prod", "before I merge"
- User just finished a feature and manually verified it in the browser
- Stack is Vite + React + vitest + Playwright

**Skip when:** user is mid-implementation (use `superpowers:test-driven-development`), wants only one specific check (run it directly), or project has no test setup (offer to scaffold first).

## Pre-flight

Run these in parallel before the gate sequence:

1. **Branch → ticket**: `git rev-parse --abbrev-ref HEAD`, extract `[A-Z]+-\d+` (e.g. `STU-123`). If none found, ask user for ticket id; if user has none, fall back to branch slug for the report filename and skip the Linear step at the end.
2. **Diff scope**: `git diff --name-only main...HEAD` to know what changed.
3. **Toolchain check**: `package.json` must have `vitest` and `@playwright/test`. If Playwright missing, halt and offer:
   ```
   npm init playwright@latest
   ```
   Wait for user confirmation. Do not proceed without E2E.
4. **Lint config sanity**: confirm `eslint-plugin-jsx-a11y` is in devDependencies or extended in eslint config. If missing, note as a soft warning in the report — gate 2 still runs but a11y lint coverage is reduced.
5. **Report path**: `qa-reports/<TICKET-or-branch-slug>-<YYYY-MM-DD>.md`. Create `qa-reports/` if missing.

## Gate sequence

Run in order. **Stop on first HARD fail.** Fix and rerun, do not proceed past failures.

| # | Gate | Command | Hard fail? |
|---|------|---------|------------|
| 1 | Type check | `npx tsc --noEmit` | yes |
| 2 | Lint + jsx-a11y | `npm run lint` | yes (errors); soft (warnings) |
| 3 | Diff hygiene | grep diff for `console.log`, `TODO`, `FIXME`, `.only(`, `xit(`, `debugger` | soft |
| 4 | Unit tests | `npx vitest run` | yes |
| 5 | Build | `npm run build` | yes |
| 6 | E2E | `npx playwright test` | yes |
| 7 | Runtime a11y | start `npx vite preview` in background, delegate to `manfred-design-systems:a11y-qa` skill (axe-core scan against the preview URL); inline-aggregate findings into this skill's report | hard for `serious`/`critical`; soft for `moderate`/`minor` |
| 8 | Audit | `npm audit --omit=dev` | soft (warn high+) |

**Hard fail** → halt, write report-so-far, do NOT post to Linear, tell user what to fix.
**Soft fail** → note in report, continue.

Use `superpowers:verification-before-completion` discipline: do not claim a gate passed without seeing the actual output.

## Report format

Write to `qa-reports/<TICKET>-<YYYY-MM-DD>.md`:

```markdown
# QA Report — <TICKET>
Date: <YYYY-MM-DD>
Branch: <branch>
Files changed: <count> (<top 5>)

## Summary
- Status: PASS / FAIL
- Hard failures: <count>
- Soft warnings: <count>

## Gates
| Gate | Result | Notes |
|------|--------|-------|
| Typecheck | ✓ | |
| Lint | ✓ | 2 jsx-a11y warnings (see below) |
| ... | | |

## Details
[truncated logs per failing/warning gate, max 30 lines each]

## Recommendation
<GO / NO-GO + 1-line reason>
```

## Linear update

After the report file is saved, post a comment via `mcp__linear-server__save_comment`. Resolve the issue id first via `mcp__linear-server__get_issue` using the ticket key from branch.

Comment body:

```
QA gate <PASS/FAIL> — <YYYY-MM-DD>

✓ Passed: typecheck, unit, build, e2e, a11y
⚠ Warnings: <n> (<types>)
✗ Failed: <n> (<types>)

Full report: qa-reports/<TICKET>-<YYYY-MM-DD>.md
```

If the ticket can't be resolved or the comment fails, surface to the user — do NOT silently skip.

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "User manually tested, skip E2E" | Manual ≠ repeatable. Run E2E. |
| "Vitest passed, build will too" | Vite dev hides build-time errors (env vars, tree-shaking). Build. |
| "Lint warnings aren't blocking" | jsx-a11y errors are hard fails in this skill. |
| "Linear update is the user's job" | No. This skill closes the loop. Post the comment. |
| "Dump output to chat, skip the file" | Linear needs a stable link. Save the file. |
| "No Playwright config, skip E2E silently" | Halt and offer to install. Don't ship without E2E. |
| "axe found one minor issue, no big deal" | Note in report. Continue. Don't suppress. |
| "I'll ask the user between gates" | No. They invoked you to run the full gate. |

## Red flags — STOP

- About to post to Linear without saving the report file → write file first.
- About to claim PASS without running all gates → run remaining gates.
- About to skip Playwright because not installed → offer to install.
- About to ask user permission between gates → just run them.
- About to summarize results only in chat → also write the report file.

## Tools used

- **Bash**: git, npx, npm
- **Write**: report file
- **MCP**: `mcp__linear-server__get_issue`, `mcp__linear-server__save_comment`
- **Skills called**: `manfred-design-systems:a11y-qa` (runtime a11y scan), `superpowers:verification-before-completion` (evidence discipline)
