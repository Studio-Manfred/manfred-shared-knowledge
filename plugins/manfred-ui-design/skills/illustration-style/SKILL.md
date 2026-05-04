---
name: illustration-style
description: Use when defining or applying an illustration style — anyone says "illustration style", "illustration system", "design illustrations for X", "empty state illustration", "spot illustration", "hero illustration", "what should our illustrations look like", "character design". Manfred-flavoured: subset of the brand palette; warm, geometric-leaning, never decorative-only; dark variants planned.
---

# illustration-style

Illustrations carry meaning when they earn it; clutter when they don't. A good illustration system makes consistent visual storytelling cheap; a bad one becomes a graveyard of one-off images that don't match.

Manfred illustrations sit in the brand: warm, slightly geometric, never decorative-only. The palette is a subset of the six brand colours plus white and almost-black — no extra hex.

## Overview

An illustration system has six components:

1. **Style definition** — geometric vs organic, flat vs dimensional, detailed vs minimal, line treatment
2. **Colour usage** — subset of brand palette, gradient/shadow rules, dark variants
3. **Character design** (if applicable) — proportions, faces, diversity, poses
4. **Illustration types** — spot / hero / empty state / onboarding / error
5. **Application rules** — when to use, sizes per context, alignment with grid
6. **Production rules** — file format, asset library, contribution workflow

## When to use

- Defining an illustration style for a project or product
- Specifying an empty state, onboarding scene, or hero illustration
- Reviewing existing illustrations for system consistency
- Documenting illustration rules for new contributors
- Adding dark-mode variants to existing illustrations

**Skip when:**

- The work is iconography (use `manfred-design-systems:icon-system` — different system, different rules)
- The work is photography or stock imagery (different artifact)
- The work is data viz (use `manfred-ui-design:data-visualization`)
- The work is logo design (out of scope; consult `~/.claude/shared/manfred-brand.md`)

## Pre-flight

```bash
test -f ~/.claude/shared/DESIGN.md && sed -n '/^## 7/,/^## /p' ~/.claude/shared/DESIGN.md
test -f ~/.claude/shared/manfred-brand.md && head -200 ~/.claude/shared/manfred-brand.md
```

DESIGN.md Section 7 (Iconography & Imagery) and the brand-doc visual-language section are the source of truth.

## Manfred's illustration style — defaults

Until a specific project / brand sets otherwise, Manfred illustrations follow:

- **Geometric-leaning**: angular forms, 4px / 8px-grid friendly, structured rather than organic
- **Flat-first**: 2D flat by default. 2.5D isometric for diagrams; 3D only when functionally required (rare).
- **Minimal detail**: communicate the moment, don't decorate. If a shape isn't earning meaning, drop it.
- **Stroke + fill mix**: thin-to-medium strokes (2px on a 24px grid), filled shapes for emphasis.
- **Warm palette**: subset of the six brand colours. Default trio for a single illustration: one warm neutral (`beige` / `light-beige` / `human-pink`), one accent (`business-blue` for action, `human-pink` for warmth), one anchor (`almost-black` for line / `white` for negative space).

## The hard rules

| Rule | What it means |
|---|---|
| **Subset of the brand palette** | Use 2–4 of the six brand colours per illustration. No extra hex; if a colour isn't in `~/.claude/shared/DESIGN.md` it doesn't go in a Manfred illustration. |
| **Earn detail** | Every shape, line, gradient earns meaning. If it's there for "polish" alone, drop it. Manfred is craft + warmth, not decoration. |
| **Flat first; depth is earned** | Default is 2D flat. No drop shadows, gradients, or pseudo-3D unless they communicate something specific. |
| **Dark variants from day one** | Provide a dark variant or design within a neutral container that works on `bg-background` in both modes. Dark is not "after". |
| **Don't carry meaning by colour alone** | Status / category / role differentiation needs shape, label, or position too — colour is one signal among many (principle 5 + 15). |
| **Aligned with grid + spacing system** | Illustrations sit on the same 4px / 8px grid as everything else. Sized to spacing tokens (`w-32`, `w-64`, etc.), not arbitrary. |
| **Inclusive representation** | Characters reflect real diversity — body types, ages, abilities, ethnicities. Default to abstract / non-character where the audience is unclear. |
| **Don't replace text** | Illustrations support text, not replace it. Empty-state illustrations always pair with copy + CTA. |

## Illustration types

### Spot illustrations
Small, inline, supporting UI elements. 24–96px typically. Single colour + accent at most. Used in cards, navigation, status indicators.

### Hero illustrations
Large, featured, storytelling. 320px+ wide. Multi-colour from the brand palette. Used on landing pages, marketing surfaces, onboarding hero moments.

### Empty states
Guide users when no content exists. Always pair: illustration + heading + body copy + CTA. Tone: matter-of-fact, not chirpy.

Example structure:
```
[Illustration — 200px]
[Heading: "No reports yet"]
[Body: "Reports show up here once you've added your first."]
[CTA: "Add a report"]
```

### Onboarding illustrations
Explain features and concepts. One concept per illustration; keep the action focal. Allow skipping.

### Error states
Soften error messages — but don't dilute them. Pair with `manfred-toolkit:ux-writing` rules: errors explain, don't blame. Illustration is supporting; copy is primary.

## Application rules

| Context | Size | Use |
|---|---|---|
| Card empty state | 96–128px | Spot |
| Page-level empty state | 200–320px | Spot or small hero |
| Hero / marketing | 400px+ | Hero |
| Inline feature explainer | 64–96px | Spot |
| Error state | 96–200px | Spot |
| Onboarding step | 240–320px | Spot or small hero |

Within a layout: aligned to the grid, sized to spacing tokens, never arbitrary pixels.

## Production rules

- **Format**: SVG (scalable, accessible, theme-flippable). Raster (PNG/WebP) only for photographic / textured illustrations.
- **Naming**: `illust-<scene>-<variant>.svg` per `manfred-design-systems:naming-convention`
- **Size**: optimised — run through SVGO; remove unused attributes
- **Library**: Figma component library + repo `assets/illustrations/`
- **Contribution**: documented (style guide, file template, review process); reviewed by the design system owner before merge

## Common rationalisations

| Excuse | Reality |
|---|---|
| "We need a unique colour for this illustration" | "Need" is rarely true. Pick from the six brand colours. If you genuinely need more, that's a system-level decision, not a one-off. |
| "Add a gradient — it'll look modern" | Manfred is flat-first. Gradients are decoration; they don't carry meaning. Drop unless functional. |
| "Skip dark variant — most users are light mode" | Manfred ships dark day-one. No-dark-variant is a TODO that becomes never. |
| "The illustration replaces the empty-state copy" | Illustrations support text, not replace. Always pair with a heading + body + CTA. |
| "Stock illustrations are faster" | Stock breaks the system. Stock characters / scenes mismatch the brand. Use Manfred illustrations or commission new ones. |
| "Add detail — it'll feel premium" | Manfred is craft + warmth, not detail. Earn every shape. |

## Red flags — STOP

- About to use a hex value not in the six brand colours
- About to design without a dark variant in mind
- About to ship an empty state without copy + CTA
- About to use heavy drop shadows / 3D / gradients without functional reason
- About to use stock illustrations in a Manfred-branded surface
- About to rely on illustration colour alone for status / category meaning
- Illustrations not aligned to the 4/8px grid

## Manfred lens

Illustration is a **brand surface** — it carries Manfred's visual identity into product moments. Inconsistency erodes the brand argument; consistency reinforces it. It's also a **usability surface** (empty states, onboarding) and **accessibility surface** (alt text, colour-not-alone, dark variants).

Critical & ethical (principle 6): inclusive representation isn't decorative — it shapes who feels seen using the product. Default to inclusive; don't tokenize.

## Cross-references

- `~/.claude/shared/DESIGN.md` Section 7 (Iconography & Imagery)
- `~/.claude/shared/manfred-brand.md` — visual language defaults
- `manfred-ui-design:color-system` — palette decisions for illustrations
- `manfred-ui-design:dark-mode-design` — for dark-variant design
- `manfred-design-systems:icon-system` — sibling skill for icons (different rules)
- `manfred-design-systems:naming-convention` — for asset naming
- `manfred-toolkit:ux-writing` — for empty-state and error copy that pairs with illustrations

## Tools used

- `Read` — `~/.claude/shared/DESIGN.md`, `~/.claude/shared/manfred-brand.md`
- `manfred-ui-design:color-system` — for palette decisions
- `manfred-toolkit:ux-writing` — for empty-state copy
- `mcp__figma-console__*` — for illustration production in Figma (when used)

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
