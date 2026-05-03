---
description: Audit a project for Manfred design system compliance — token usage, a11y, naming consistency, dark mode coverage. Produces a markdown report with prioritised fixes.
argument-hint: [path or scope to audit, e.g. "src/components/billing"]
---

You're auditing a project for Manfred design system compliance. The user mentioned: $ARGUMENTS

## Step 1 — Scope the audit

Ask:

- What's the audit scope? (Whole `src/`, one feature, one component, recent PR diff?)
- Is there a Linear ticket this audit serves? (For posting results.)
- Pre- or post-merge? (Pre = block; post = backlog.)

If scope isn't clear, default to `src/components/` and the most recently changed files.

## Step 2 — Survey the project's token surface

Before scanning for violations, confirm what's available:

```bash
test -f ~/.claude/shared/DESIGN.md && head -200 ~/.claude/shared/DESIGN.md
test -f src/tokens/tokens.css && cat src/tokens/tokens.css
test -f tailwind.config.* && grep -A 50 "theme:" tailwind.config.*
```

This is the baseline. Violations are measured against what's actually defined, not what should exist.

## Step 3 — Run the four scans

For each scan, list files + line numbers + the specific violation. No vague "needs improvement" — concrete evidence.

### Scan 1 — Token compliance (`manfred-design-systems:design-token`)

Look for:

- Raw hex literals in component files: `grep -rn "#[0-9a-fA-F]\{3,6\}" src/components/`
- Default Tailwind palette colours that bypass tokens: `grep -rn "bg-\(red\|green\|blue\|amber\|slate\|gray\|zinc\)-[0-9]" src/`
- `var(--token-name)` references for tokens that don't exist in `tokens.css`
- Brand utilities (`bg-business-blue`) used where semantic would be correct (consumer text doesn't account for both modes)

### Scan 2 — Accessibility (`manfred-design-systems:a11y-qa`)

Defer to the skill. Run runtime axe scan on a built/preview URL if available; fall back to static jsx-a11y lint otherwise.

### Scan 3 — Naming consistency (`manfred-design-systems:naming-convention`)

Look for:

- Components named for appearance not purpose (`BlueButton`, `BigCard`, `FancyHeader`)
- Mixed casing for the same concept (`Listbox`/`ListBox`/`List_Box` all in one project)
- Numeric-versioned names (`Button2`, `ButtonNew`)
- Token names not matching the `--<category>-<purpose>-<variant>-<state>` pattern

### Scan 4 — Dark mode coverage (`manfred-design-systems:theming-system`)

Look for:

- Components hardcoding light-only colours that won't flip in dark mode
- Components with explicit `if (theme === 'dark')` logic (token failure — should be in tokens, not components)
- Storybook stories without dark-mode coverage

## Step 4 — Prioritise

Group findings into three buckets:

| Bucket | Threshold | Action |
|---|---|---|
| **Block-merge** | Hex literals, missing focus indicators, broken keyboard nav, axe critical/serious | Fix before merge |
| **High-priority backlog** | Default Tailwind palette colours, naming inconsistencies in shipped components, missing dark-mode coverage on visible surfaces | Open tickets, fix this sprint |
| **Cleanup** | Internal naming nits, deprecated patterns still in use, low-priority a11y moderate findings | Backlog, address opportunistically |

## Step 5 — Write the report

Save to `design-system-audits/<scope-slug>-<YYYY-MM-DD>.md`:

```markdown
# Design system audit: <scope>

**Date**: YYYY-MM-DD
**Scope**: [files / feature / branch]
**Linear ticket**: [STU-XXX or n/a]
**Auditor**: [name]

## Summary
- N block-merge findings
- N high-priority backlog findings
- N cleanup findings

## Block-merge
[file:line — finding — recommended fix — link to relevant skill]

## High-priority backlog
[file:line — finding — recommended fix]

## Cleanup
[file:line — finding — recommended fix]

## Tokens used vs available
[Brief — what semantic tokens were heavily used, what brand utilities, what was bypassed]

## Recommended next step
[Concrete — usually "fix block-merge before merge", or "open N tickets for backlog"]
```

## Step 6 — Linear update (if ticket linked)

If a Linear ticket is in scope, post the summary as a comment via `mcp__linear-server__save_comment`. Include the report path, finding counts, and the next-step recommendation.

## Wrap-up

Tell the user:

- Where the report lives
- The block-merge count (if any — this is the gate)
- The next-step recommendation
- Offer: "Want me to open Linear tickets for the high-priority backlog items?"

If the project has zero block-merge findings: say so plainly. Don't manufacture issues to look thorough.
