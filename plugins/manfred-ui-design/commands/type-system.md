---
description: Define a type system for a project — apply Manfred's Host Grotesk scale per `~/.claude/shared/DESIGN.md` Section 3, with role-based mapping + responsive scaling + line-length guidance.
argument-hint: [scope, e.g. "type system for the new client app, English + Swedish parity"]
---

You're defining a type system. The user mentioned: $ARGUMENTS

## Step 1 — Confirm scope

Ask:

- **What's the scope?** Whole product, single feature, marketing surface?
- **Languages?** English / Swedish parity? Other locales?
- **Project's font setup confirmed?** (Host Grotesk shipped via design system; Guttery only for logotype)
- **Existing type tokens defined?** Tailwind `@theme` config, or rolling per-project?
- **Linear ticket?**

## Step 2 — Map roles to the scale (`manfred-ui-design:typography-scale`)

Walk Manfred's role table and confirm what's needed for this project:

| Role | Default | Project decision |
|---|---|---|
| Display / hero | `text-5xl` (56px) at 600 weight | … |
| Section heading | `text-2xl`–`text-3xl` (24–32px) at 600 | … |
| Subheading | `text-lg`–`text-xl` (18–20px) at 500 | … |
| Body | `text-base` (16px) at 400, line-height 1.5 | non-negotiable |
| UI / buttons | `text-sm`–`text-base` (14–16px) at 500 | … |
| Captions / metadata | `text-xs`–`text-sm` (12–14px) at 400 | … |

If the project needs sizes Manfred's scale doesn't ship — flag as a token gap; route via `manfred-design-systems:design-token`.

## Step 3 — Responsive scaling

For each role, decide:

- **Stays consistent** — body always 16px regardless of breakpoint
- **Scales down on mobile** — display from `text-5xl` (56px) to `text-3xl` (32px)
- **Fluid scales** — `clamp()` between breakpoints for smooth transitions

Example default scaling:
- `text-3xl md:text-4xl lg:text-5xl` for hero
- `text-2xl md:text-3xl` for section headings
- `text-base` for body (no responsive change)

## Step 4 — Line-height + letter-spacing

| Role | Line-height | Letter-spacing |
|---|---|---|
| Display | 1.1–1.2 (`leading-tight`) | -0.02em (`tracking-tight`) |
| Headings | 1.2–1.3 | normal |
| Body | 1.5 (`leading-normal`) | normal |
| UI labels | 1.2–1.4 | normal or slight (`tracking-wide` for uppercase) |
| Long-form reading | 1.6–1.75 (`leading-relaxed`) | normal |

## Step 5 — Line-length

Body content: line-length 45–75 characters per line. Use `max-w-prose` (Tailwind: `max-w-[65ch]`) for body containers.

Long lines fatigue; short lines fragment. Test at every breakpoint with real content (Swedish runs longer than English; account for it).

## Step 6 — Performance budget (`~/.claude/shared/design-principles.md` principle 13)

For each weight loaded:

- Font file size (KB)
- Whether it's actually used (grep usage in the codebase)
- Whether it's worth the perf cost

Manfred ships Host Grotesk in 6 weights (300, 400, 500, 600, 700, 800). Most projects use 4 max. If your project doesn't use 300 or 800, drop them from the bundle.

## Step 7 — Document the system

Save to `discovery/type-systems/<project-slug>-<YYYY-MM-DD>.md`:

```markdown
# Type system — <project>

**Date**: YYYY-MM-DD
**Languages**: <list>
**Linear**: STU-XXX

## Scale (per role)
[Role table from Step 2 with project-specific decisions]

## Responsive scaling
[Per role: how it scales across breakpoints]

## Line-height + letter-spacing
[Per role]

## Line-length
[Body container max-width; note language considerations if Swedish parity needed]

## Performance
[Weights loaded; weights used; bundle impact]

## Tokens used
[Tailwind type classes referenced]

## Token additions needed
[None — used existing | Need <token name>; queued via manfred-design-systems:design-token]
```

## Step 8 — Linear update

Post via `mcp__linear-server__save_comment` with:

- Path to the system doc
- Roles defined + responsive scaling decisions
- Performance impact (weights kept / dropped)
- Token additions queued (if any)

## Wrap-up

Confirm the system covers:

- [ ] All roles mapped to existing scale or flagged for addition
- [ ] Responsive scaling per role
- [ ] Line-height + letter-spacing per role
- [ ] Line-length capped (45–75ch for body)
- [ ] Body 16px minimum
- [ ] 4–5 sizes max per view
- [ ] Host Grotesk for UI; Guttery for logotype only
- [ ] Performance budget documented (weights used)
- [ ] Language parity tested with real content (Swedish + English where applicable)

Then offer:

> "Apply this to a specific screen via `/manfred-ui-design:design-screen`. Cross-check against the design system via `manfred-toolkit:design-token-audit` to verify type compliance across the project."
