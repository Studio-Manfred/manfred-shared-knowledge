---
description: Define a colour palette for a feature, page, or surface. Routes through the existing token surface; refuses hex generation; surfaces semantic gaps as design-system decisions.
argument-hint: [scope, e.g. "Smart Insights tab — needs cards in three states"]
---

You're defining a colour palette. The user mentioned: $ARGUMENTS

## Step 1 — Confirm what's actually needed

Ask:

- **What surfaces?** Page background, cards, callouts, CTAs, status states, data viz?
- **What's the user trying to do on this surface?** ("Modern and trustworthy" gets pushed back; specific moments get colour decisions.)
- **Theme-aware or literal-brand?** (Most surfaces want semantic / theme-aware; literal-brand for explicit moments only.)
- **Linear ticket?** (For posting decisions.)
- **Does this need new tokens, or does the existing surface cover it?**

If the brief is generic ("modern, trustworthy, fintech vibes") — push back. Manfred isn't generic-fintech.

## Step 2 — Run the color-system skill (`manfred-ui-design:color-system`)

The skill maps each requested surface to the right token:

- Page → `bg-background` (semantic)
- Cards → `bg-card` (semantic) or `bg-beige` / `bg-human-pink` (brand utilities for warm-emphasis)
- CTAs → `bg-primary` (semantic, business-blue) or `bg-business-blue` (literal)
- Text → `text-foreground` / `text-muted-foreground` (semantic)
- Destructive → `bg-destructive` (semantic)
- Status states (success/warning/info) → **(a)/(b)/(c) menu** — refuses to invent

If the user picks (a) — add tokens to the design system — queue the work via `manfred-design-systems:design-token` *before* the feature ships.

## Step 3 — Verify dark mode

For every token in the palette:

- Semantic tokens: confirm they flip automatically (`bg-background`, `bg-card`, `text-foreground`, etc.)
- Brand utilities: confirm they stay literal — and that the surrounding text/contrast works in both modes
- Custom additions (path (a)): contrast verified at 4.5:1 (body) / 3:1 (large + UI) on every surface they sit on

## Step 4 — Run a11y check (`manfred-design-systems:a11y-design`)

Annotate the palette for accessibility:

- Contrast ratios per text/background pairing
- Focus-ring colour (semantic `ring-ring`)
- Status colours don't carry meaning alone — pair with shape, label, or icon

## Step 5 — Output the palette

Save to `discovery/palettes/<surface-slug>-<YYYY-MM-DD>.md`:

```markdown
# Palette — <surface>

**Date**: YYYY-MM-DD
**Linear**: STU-XXX
**Designer**: <name>

## Tokens used
[Per surface, with brand-utility-vs-semantic distinction]

## Dark mode
[Per token: flips automatically | stays literal | requires absolute pair]

## A11y
[Contrast ratios verified; status states not colour-alone]

## Token additions needed
[None — used existing | Need <token name>; queued via manfred-design-systems:design-token]
```

## Step 6 — Linear update

Post a comment via `mcp__linear-server__save_comment` with:

- Path to the palette file
- Surfaces covered
- Token additions queued (if any)
- Dark mode + a11y verification result

## Wrap-up

Confirm the palette covers:

- [ ] Every surface mapped to an existing token (or flagged for path-(a) addition)
- [ ] No hex literals
- [ ] Brand utilities vs semantic tokens distinguished
- [ ] Dark mode behaviour stated per token
- [ ] A11y contrast verified
- [ ] Status states use icon + copy + neutral surface (path c) or named semantic addition (path a) — never invented

Then offer:

> "Hand off to engineering with `/manfred-design-ops:handoff`. The handoff spec will reference these tokens (no hex). If new tokens were queued, the design-system PR ships before the feature PR."
