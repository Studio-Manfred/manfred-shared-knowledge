---
name: spacing-system
description: Use when defining or applying spacing — anyone says "spacing system", "padding", "margin", "gap", "spacing scale", "vertical rhythm", "what spacing should I use", "compact mode", "spacious mode". Manfred-flavoured: 4px base unit (Tailwind default); always use the scale; no arbitrary px.
---

# spacing-system

Spacing is the silent design system. Most users don't notice spacing when it's right; everyone notices when it's wrong (cramped, drifting, inconsistent). Manfred uses Tailwind's default 4px base unit, which gives a clean scale up through `4xl` and beyond.

For component-internal spacing (padding inside a Card, gaps between FormField elements), this skill is the source. For the page-level grid (columns + gutters), use `manfred-ui-design:layout-grid`.

## Overview

The scale (Tailwind defaults, multiplied by 4px):

| Token | Pixels | Tailwind | When to use |
|---|---|---|---|
| `0.5` | 2px | `p-0.5`, `gap-0.5` | Hairline gaps (rare) |
| `1` | 4px | `p-1`, `gap-1` | Tightest meaningful spacing — between icon + label |
| `2` | 8px | `p-2`, `gap-2` | Tight grouping — within a button, inside a small chip |
| `3` | 12px | `p-3`, `gap-3` | Compact grouping — between form-field label + input |
| `4` | 16px | `p-4`, `gap-4` | Default — most padding inside cards, default vertical rhythm |
| `5` | 20px | `p-5`, `gap-5` | Less common — bridge between 4 and 6 |
| `6` | 24px | `p-6`, `gap-6` | Comfortable — between fields in a form, between cards in a grid |
| `8` | 32px | `p-8`, `gap-8` | Spacious — between sections in a page |
| `10` | 40px | `p-10`, `gap-10` | Hero spacing — above/below hero sections |
| `12` | 48px | `p-12`, `gap-12` | Large hero / page-margin equivalent |
| `16` | 64px | `p-16`, `gap-16` | Page-section break |
| `20` | 80px | `p-20`, `gap-20` | Major section break (marketing pages) |
| `24` | 96px | `p-24`, `gap-24` | Hero / landing-page top spacing |

## When to use

- Picking spacing values for a new component
- Reviewing a design that has off-scale spacing
- Defining density variants (compact / comfortable / spacious)
- Auditing a project for spacing consistency
- Deciding between similar values (when 4 vs 6 vs 8)

**Skip when:**

- The work is page-level grid (use `manfred-ui-design:layout-grid`)
- The work is component spec (use `manfred-design-systems:component-spec`)
- The work is naming the tokens themselves (use `manfred-design-systems:naming-convention`)

## Spacing types

| Type | Definition | Example |
|---|---|---|
| **Inset** | Padding inside a container | `<Card className="p-6">` |
| **Stack** | Vertical space between stacked elements | `<div className="space-y-4">` |
| **Inline** | Horizontal space between inline elements | `<div className="flex gap-4">` |
| **Grid gap** | Space between grid / flex items | `<div className="grid gap-6">` |

## The hard rules

| Rule | What it means |
|---|---|
| **Always use the scale** | Never `p-[19px]`, never `gap-[7px]`. Tailwind's primitive scale covers every multiple of 4px (and a few halves). If your value isn't on the scale, round to the nearest scale step. |
| **Related items: smaller spacing** | Within a group (button + icon, label + input): `gap-1`/`gap-2`/`gap-3`. |
| **Distinct sections: larger spacing** | Between groups (form fields, cards): `gap-6`/`gap-8`. Between page sections: `gap-12`/`gap-16`. |
| **Consistent within a component** | A Card uses one inset value for all sides — `p-6`, not `pt-4 pb-6 px-5`. Asymmetric padding is intentional, documented, and rare. |
| **Larger gap between unrelated > smaller gap within related** | The hierarchy of spacing reinforces the hierarchy of grouping. If unrelated items have less space than related items, perception breaks. |
| **Document spacing intent** | When a component spec calls out spacing, name *why*: "16px above CTA to give it room from the form" — not just "16px above CTA". |
| **Test at viewport sizes** | Spacing that works at 1440px can feel cramped at 320px. Audit per breakpoint. |

## Density modes

For data-heavy or reading-heavy contexts:

- **Compact** — reduce by one step (e.g. `p-3` instead of `p-4`); for tables, dense lists
- **Comfortable** — default
- **Spacious** — increase by one step; for reading-focused content, marketing surfaces

Density is a project-level decision, not per-component. If the project ships density modes, use them everywhere consistently (`manfred-design-systems:theming-system` describes the architecture).

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Just `p-[19px]` to match Figma" | Either Figma is on the scale and you misread, or Figma's wrong. Round to `p-5` (20px) or `p-4` (16px). |
| "Asymmetric padding looks more dynamic" | Asymmetric is OK when intentional. Default is symmetric — drift to asymmetric is design-system rot. |
| "We need an in-between value" | Tailwind ships 0.5-step values (`p-0.5`, `p-1.5`, `p-2.5`, `p-3.5`) for genuine half-step needs. Use them; don't invent. |
| "Spacing within a button doesn't matter" | It does. Tight spacing makes buttons feel cheap; spacious spacing makes them feel important. Both are valid; both are deliberate. |
| "Compact mode just shrinks everything" | Compact mode shrinks *spacing*, not text. Text smaller than 16px is a readability regression, not density. |

## Red flags — STOP

- About to use `p-[arbitrary]` value
- About to use a non-scale gap value
- About to ship asymmetric padding without a documented reason
- About to use larger spacing within a group than between groups
- About to ship density variants that include text-size changes (different concern)

## Manfred lens

Spacing is **infrastructure** — Cagan/Torres lens doesn't apply. But: spacing carries **principle 7 (simple by default)** — generous spacing is part of how Manfred surfaces feel calm. It also carries **principle 11 (consistent, not uniform)** — spacing consistency reinforces the rest of the system.

Performance (principle 13): not a direct concern of spacing, but excessive padding pushes content below the fold and increases scroll cost. Calibrate.

## Cross-references

- `~/.claude/shared/DESIGN.md` Section 5 (Layout Principles)
- `~/.claude/shared/design-principles.md` principles 7, 11
- `manfred-ui-design:layout-grid` — page-level grid; uses spacing for gutters and margins
- `manfred-design-systems:design-token` — for component-level spacing decisions
- `manfred-design-systems:naming-convention` — for token naming
- `manfred-design-systems:theming-system` — for density-mode architecture

## Tools used

- `Read` — `~/.claude/shared/DESIGN.md`, project's `tailwind.config`
- `manfred-design-systems:design-token` — for component-level token decisions

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
