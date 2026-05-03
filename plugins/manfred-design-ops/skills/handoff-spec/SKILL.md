---
name: handoff-spec
description: Use when handing off a design to engineering — anyone says "write a handoff spec", "engineering handoff", "spec for the dev team", "design-to-dev document", "redline the design", "annotate this for engineers", "send this to engineering", "ship to dev", "developer handoff". Manfred-specific: token-anchored, posts to Linear via MCP, references existing components, pushes back on kitchen-sink dumps.
---

# handoff-spec

A handoff spec is the smallest document that produces shared understanding between designer and engineer. Not a kitchen-sink dump of every measurement — a tight intent + decisions + open-questions doc plus a Figma link, posted as a Linear comment where engineering actually lives.

If the brief is "engineering hates having to come back asking", more words don't fix it. A 15-min walk-through fixes it.

## Overview

A Manfred handoff has three layers:

1. **Intent** — what this design is trying to do, in 2–3 sentences. Engineering needs context, not just spec.
2. **Decisions + tokens** — the visual + interaction decisions, anchored to existing tokens (`~/.claude/shared/DESIGN.md`) and existing components, not raw values.
3. **Open questions + states** — what's NOT yet decided and needs discussion; what edge cases are in scope; what's deferred.

The spec posts as a Linear comment via `mcp__linear-server__save_comment` when a ticket exists. The doc lives where engineering already works.

## When to use

- Handing off a finished or near-finished design to engineering
- Writing the spec section of a Linear ticket for a UI change
- Documenting a component or pattern that engineering will implement
- Annotating a Figma file for developer pickup
- Producing a redline document for a complex layout

**Skip when:**

- The change is so small that a Slack message + Figma link suffices (don't manufacture process)
- The design isn't done — handoff before completion produces churn (use `manfred-design-systems:component-spec` for spec'ing during design)
- The user wants a complete component definition (use `manfred-design-systems:component-spec` — that's the engineering-facing API spec; this is the per-instance handoff)

## Pre-flight (do this every time)

Three reads, one MCP check, before drafting:

```bash
# 1. Token surface
test -f ~/.claude/shared/DESIGN.md && head -200 ~/.claude/shared/DESIGN.md

# 2. Existing components
grep -A 2 "## 4. Component Library" ~/.claude/shared/DESIGN.md

# 3. Linear ticket (if mentioned)
git rev-parse --abbrev-ref HEAD  # extract ticket key from branch name like feat/STU-123-foo
```

```
# 4. If a ticket key is found, fetch the ticket via MCP
mcp__linear-server__get_issue(id: "STU-XXX")
```

If `~/.claude/shared/DESIGN.md` is unreadable, ask the user to install `manfred-shared-knowledge` or point at the project's `tokens.css`. **Do not draft a handoff with hex literals because the token file isn't readable.**

If a Linear ticket key is in the brief or branch name, hold the spec for posting via `mcp__linear-server__save_comment` — don't just return inline markdown.

## The hard rules

| Rule | What it means |
|---|---|
| **Tokens, not literals** | Every colour/spacing/radius value resolves through `manfred-design-systems:design-token`. No hex, no raw px, no `bg-green-500`. If a token doesn't exist, surface that as a design-system gap. |
| **Reference existing components** | Manfred ships Alert, Badge, Breadcrumb, Button, Checkbox, Dialog, FormField, Icon, Logo, ProgressBar, Radio, SearchBar, Spinner, TextInput, Toast, Tooltip, Typography. If the spec calls for a "modal" — say `<Dialog>`. If it calls for a "switch" — flag that Manfred doesn't ship one and decide (build new, or use `<Checkbox>`). |
| **Refuse "dump everything"** | A complete-looking spec engineering scans for the relevant 20% is worse than a tight spec they read all of. **Hard gate: if intent + decisions + open questions exceed 300 words, stop drafting and audit — every section past the cap means something belongs in Figma instead.** Link to Figma for measurements; the spec is intent and decisions, not a measurement dump. |
| **Walk-through over document** | If the brief is "engineering keeps asking" or "dev keeps getting it wrong", that's a process problem (no walk-through ritual, no synchronous moment). Recommend a 15-min sync, schedule it; the spec is the prep, not the substitute. |
| **Linear is the delivery channel** | When a ticket is linked, post via `mcp__linear-server__save_comment`. Don't return inline markdown and call it done. Engineering lives in Linear. |
| **A11y as first-class section, not footnote** | Per-component: focus indicator, keyboard order, SR labels, reduced-motion alternative for any animation. WCAG 2.2 AA non-negotiable (Manfred design principle 5). |
| **Open questions explicit** | If something isn't decided, name it in the "Open questions" section. Don't pretend the spec is more complete than it is — that's where engineering surprises come from. |

## The flow

### Step 1 — Confirm scope

Ask if not stated:

- Linear ticket? (Or branch name to extract from?)
- Figma link? (URL to the source of truth — the spec references it, doesn't replace it)
- Walk-through scheduled? (If not — recommend one, schedule it, capture the time in the spec)
- What's the dev's prior context? (First time on this surface vs. has built similar — adjust depth)

### Step 2 — Pre-flight reads

Per the Pre-flight section above. Don't skip — every spec written without reading DESIGN.md first leaks raw values into the codebase.

### Step 3 — Draft the spec (the ~300-word frame)

```markdown
## Handoff: <surface name> — <Linear key>

**Figma**: <link>
**Walk-through**: <scheduled time> with <names>
**Designer**: <name>
**Status**: ready for pickup | needs walk-through first | blocking on [decision]

### Intent
[2–3 sentences. What this design does, why it changed from current, what user need it serves. Engineering needs context to make 100 small decisions correctly.]

### Decisions
- **Layout**: <component or container choice + token reference> — e.g. "Two-column with `Card` containers, `gap-6` between"
- **Surfaces**: <semantic tokens> — e.g. "Page: `bg-background`. Cards: `bg-card border-border`."
- **Type**: <typography role from Section 3> — e.g. "Page title: section-heading (24px / 32px / 600). Field labels: medium (14/20/500)."
- **Components**: <existing Manfred components used> — e.g. "Form fields use `<FormField>`. Save action uses `<Button variant='primary'>`. Confirmation uses `<Dialog>`."
- **Spacing rhythm**: <Tailwind primitives or token refs> — e.g. "Sections: `gap-8`. Within section: `gap-4`. Within field: `gap-2`."
- **States covered in Figma**: default · hover · focus · disabled · loading · error · empty
- **Responsive**: <breakpoints with token refs> — e.g. "Single-column at `sm`, two-column at `lg+`."
- **Motion**: <reduced-motion alternative stated> — e.g. "Toast: `slide-in-from-bottom-2 duration-200`. With `prefers-reduced-motion`: fade only, no slide."

### Accessibility (WCAG 2.2 AA — non-negotiable)
- **Focus order**: <document the tab sequence — number per Figma annotation if needed>
- **Keyboard**: <shortcuts, escape behaviour, enter behaviour per surface>
- **SR labels**: <icon-only actions get `aria-label` — list them>
- **Live regions**: <toasts get `role="status"` or `role="alert"`; loading states get `aria-busy`>
- **Reduced motion**: <which animations have a reduced-motion alternative>
- **Contrast**: <verified at design stage; runtime gate is `manfred-design-systems:a11y-qa`>

### Edge cases in scope
- [Specific edge case + how it should behave]
- [Specific edge case + how it should behave]

### Out of scope (this handoff)
- [Adjacent work that's NOT this engagement — name explicitly so it doesn't get scope-crept in]

### Open questions
- [Decision the designer needs from engineering or product before this can ship]
- [Constraint the designer hasn't validated yet]

### Tokens used (cross-check)
[List every token name referenced. If any aren't in `~/.claude/shared/DESIGN.md`, flag — needs design-system PR.]
```

### Step 4 — Post to Linear

If a ticket key was found:

```
mcp__linear-server__save_comment(
  issueId: "STU-XXX",
  body: <the spec from Step 3>
)
```

Confirm the comment was created. If posting fails (auth issue, ticket missing), surface to the user — don't pretend it succeeded.

If no ticket: pause and ask. A handoff without a ticket usually means one of three things:

- **Engineering pickup is intended but a ticket hasn't been created yet** — push for a ticket first. The spec without a ticket is a doc nobody owns. Offer to draft the ticket title + description from the spec intent.
- **Internal exploration only, no engineering pickup intended** — confirm explicitly, then save to `discovery/handoffs/<surface-slug>-<YYYY-MM-DD>.md` with header `**Status**: internal exploration — no engineering pickup intended`.
- **Spec is being drafted ahead of the ticket** (sprint planning use) — save locally with header `**Status**: draft — to be posted to <ticket key> on creation`.

Don't silently fall through to a markdown file. The Linear post is where engineering reads; a markdown file at `discovery/handoffs/...` is documentation only — easy to miss, easy to skip.

### Step 5 — Recommend / schedule the walk-through

The spec is prep, not substitute. Recommend a 15-min sync between designer + engineer to walk the spec. Capture the time in the spec header.

If the user pushes back ("we don't need a sync, the spec is enough"): hold the line. The most efficient handoff is async-prep + sync-walk + async-build. Skipping the sync trades one 15-min meeting for many small misunderstandings later.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Just dump everything you know about the screen" | A 2,000-word spec engineering scans for 200 words is worse than a 300-word spec they read all of. Cap the spec; link Figma for the rest. |
| "I'll spec it in pixels because Tailwind sometimes doesn't have the exact value" | Tailwind has every multiple of 4 (`p-1` = 4px, `p-2` = 8px, etc.). If you genuinely need a value Tailwind doesn't have, that's a design system gap — flag it, don't bypass. |
| "Engineering keeps asking — I need a more complete spec" | They're asking because there's no walk-through. Schedule the walk-through. The spec is prep, not substitute. |
| "I'll use hex codes, the dev will translate to tokens" | They won't. Hex codes leak into PRs. Token references force the right value at write-time. |
| "I don't need to post to Linear, I can just paste this in Slack" | Linear is where engineering tracks work. Slack pastes get lost. Post via MCP — `mcp__linear-server__save_comment` — even if you also Slack the link. |
| "Accessibility section can be a footnote — the engineer knows" | Accessibility specified at handoff is accessibility built-in. Accessibility as footnote is accessibility as afterthought. WCAG 2.2 AA is the floor, not a stretch. |
| "I'll skip 'open questions' — the spec is complete" | Every spec has open questions. Hiding them produces engineering surprises. Naming them produces conversations before commit. |

## Red flags — STOP

- About to write a hex literal in the spec
- About to write a raw px value (use `p-4`, `var(--spacing-4)`, etc.)
- About to spec a custom component when an existing Manfred one fits
- About to ship a spec without checking `~/.claude/shared/DESIGN.md`
- About to return inline markdown when a Linear ticket is linked (use `mcp__linear-server__save_comment`)
- About to write more than ~300 words of decisions (you're producing a kitchen-sink dump)
- About to skip the walk-through because the user said "the spec is enough"
- About to bury accessibility in a footnote

## Manfred lens

A handoff is a contract between teams. A bad contract creates rework, missed accessibility floors, and design drift. The skill exists to make the contract small enough to honour and clear enough to verify.

## Output format

Markdown spec, posted as Linear comment via `mcp__linear-server__save_comment` if ticket linked. Otherwise saved to `discovery/handoffs/<surface-slug>-<YYYY-MM-DD>.md`.

Final user-facing message: confirm the spec was posted (with Linear comment URL if available), confirm or recommend the walk-through time, list any open questions that need resolution before engineering starts.

## Tools used

- `Read` — `~/.claude/shared/DESIGN.md` for tokens + existing components
- `Bash` — `git rev-parse --abbrev-ref HEAD` to extract Linear ticket key from branch
- `mcp__linear-server__get_issue` — fetch ticket context
- `mcp__linear-server__save_comment` — post the spec
- `Write` — fallback when no ticket linked
- `manfred-design-systems:design-token` — for every visual value
- `manfred-design-systems:component-spec` — when the handoff calls out a new component definition (not just a per-instance use)
- `manfred-design-systems:a11y-design` — for the a11y annotation pass at design stage
- `manfred-design-systems:a11y-dev` — for the implementation gate post-handoff
- `manfred-design-systems:a11y-qa` — for the runtime gate (called by `manfred-dev:test-my-code`)
