---
name: layout-grid
description: Use when defining or applying a layout grid — anyone says "layout grid", "column grid", "12-column", "page layout", "container width", "grid system", "page margins", "gutters", "baseline grid". Manfred-flavoured: 12-column on desktop dropping to 4 on mobile; consistent gutters from spacing tokens; mobile-first responsive.
---

# layout-grid

A layout grid is the contract between layout decisions and the rest of the system. Done right, every page sits on the same rhythm and developers can build to spec without measuring screenshots. Done badly, every page invents its own widths and the codebase gets full of `max-w-[1234px]` magic values.

Manfred uses a 12-column grid on desktop dropping to 8 on tablet and 4 on mobile, with gutters and margins drawn from the spacing token scale. Mobile-first per principle 12.

## Overview

Grid anatomy:

- **Columns** — the vertical divisions content snaps to. 12 (desktop), 8 (tablet), 4 (mobile).
- **Gutters** — space between columns. From the spacing token scale (`gap-4`, `gap-6`, `gap-8` typically).
- **Margins** — outer page padding. Smaller on mobile (`px-4`), larger on desktop (`px-8`/`px-12`).
- **Container** — max-width constraint. Manfred default: `max-w-7xl` (1280px) for content; `max-w-screen-2xl` (1536px) for full-width marketing.
- **Baseline grid** — vertical rhythm on a 4px or 8px base; aligns with `manfred-ui-design:spacing-system`.

## When to use

- Setting up a new page or template
- Reviewing a design that doesn't snap to the grid
- Defining the responsive grid behaviour for a feature
- Documenting layout rules for a project
- Auditing existing layouts for grid inconsistency

**Skip when:**

- The work is component-internal layout (use `manfred-design-systems:component-spec`)
- The work is responsive behaviour specifically (use `manfred-ui-design:responsive-design`)
- The work is spacing decisions inside a component (use `manfred-ui-design:spacing-system`)

## Pre-flight

Check:

- Project's `tailwind.config` for breakpoint definitions (default Tailwind: `sm 640px`, `md 768px`, `lg 1024px`, `xl 1280px`, `2xl 1536px`)
- Existing layout components — are there shared `Container` / `PageLayout` primitives to use?
- `~/.claude/shared/DESIGN.md` Section 5 (Layout Principles) for Manfred defaults

## Manfred grid defaults

| Breakpoint | Columns | Gutter | Page margin | Container max |
|---|---|---|---|---|
| Mobile (<640px) | 4 | `gap-4` (16px) | `px-4` (16px) | n/a (full-bleed within margins) |
| Tablet (640–1023px) | 8 | `gap-6` (24px) | `px-6` (24px) | n/a |
| Desktop (1024–1279px) | 12 | `gap-6` (24px) | `px-8` (32px) | `max-w-7xl` (1280px) |
| Wide (1280px+) | 12 | `gap-8` (32px) | `px-12` (48px) | `max-w-7xl` (1280px) for content; `max-w-screen-2xl` for full-width marketing |

## The hard rules

| Rule | What it means |
|---|---|
| **Consistent gutters from tokens** | Gutter values come from the spacing scale — never `gap-[19px]`. |
| **Mobile-first** | Design and implement mobile (4-col) first, expand to tablet/desktop. Default Tailwind classes are mobile; breakpoint prefixes (`md:`, `lg:`) layer on. |
| **Snap to columns** | Content widths express in column counts (`col-span-4`, `col-span-8`), not arbitrary pixels. |
| **Max-width container** | Content has a max width. Without one, line-lengths get unreadable on wide screens. Default `max-w-7xl`. |
| **Responsive at every breakpoint** | Test 320, 768, 1024, 1440px minimum (per principle 12). Not just the extremes. |
| **Baseline grid alignment** | Vertical rhythm on a 4 or 8px base. Tailwind primitives are already on this base. |
| **Intentional grid-breaking** | A design that breaks the grid does so for emphasis. Document the reason. |

## Grid types

### Column grid (default)
Equal columns separated by gutters. Content spans 1 or more columns. The default Manfred grid.

```tsx
<div className="grid grid-cols-4 md:grid-cols-8 lg:grid-cols-12 gap-4 md:gap-6 lg:gap-8">
  <div className="col-span-4 md:col-span-6 lg:col-span-8">Main content</div>
  <div className="col-span-4 md:col-span-2 lg:col-span-4">Sidebar</div>
</div>
```

### Asymmetric grid
Sidebar + main content. Common for app shells.

```tsx
<div className="grid grid-cols-1 lg:grid-cols-[240px_1fr] gap-6">
  <Nav />
  <Main />
</div>
```

### Full-bleed
Content spans full viewport (hero sections, image galleries). Sit outside the container.

```tsx
<section className="w-full bg-business-blue text-white py-16">
  <div className="max-w-7xl mx-auto px-4 md:px-8">
    {/* content with normal margins */}
  </div>
</section>
```

### Card grid
Auto-fill responsive cards. Falls back to single column on mobile.

```tsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  {cards.map(card => <Card key={card.id} {...card} />)}
</div>
```

## Common rationalisations

| Excuse | Reality |
|---|---|
| "I'll just use `max-w-[1234px]` for this one" | Magic values pollute the codebase. Use the container scale. If the system needs a new container width, add it to `tailwind.config`, don't bypass. |
| "12 columns on tablet too" | Tablet (~768px) is too narrow for 12 readable columns. 8 is the right step. |
| "Gutter just needs to be 19px to match Figma" | Either Figma is on the spacing scale and you misread, or Figma is wrong. Tailwind primitives are on a 4px base; 19px isn't. Round to the scale. |
| "We'll add the responsive breakpoints later" | "Later" is "never". Mobile-first means mobile-first, not desktop-first-with-mobile-tweaks. |
| "Centre the content vertically and horizontally on every page" | Vertical centering on long pages breaks scrolling expectations. Horizontal yes; vertical only when content fits without scroll. |
| "Drop the max-width — let it stretch" | Without max-width, text becomes unreadable past 1440px. Lines get too long for the eye to track. Always cap. |

## Red flags — STOP

- About to use `max-w-[arbitrary-px]` instead of the container scale
- About to use a gap value not on the spacing scale
- About to design tablet without an 8-column step
- About to ship without a mobile (320px) layout
- About to break the grid without documenting why
- About to centre content vertically when it could scroll

## Manfred lens

Layout grids are **infrastructure** — Cagan/Torres lens doesn't apply. But: bad grid systems make every page a snowflake; good ones make pages cheap and consistent. Layout drift is design-system rot in slow motion.

Mobile-first (principle 12) and responsive-always are floors here, not ceilings.

## Cross-references

- `~/.claude/shared/DESIGN.md` Section 5 (Layout Principles)
- `~/.claude/shared/design-principles.md` principle 12 (Mobile First, Responsive Always)
- `manfred-ui-design:responsive-design` — for the responsive behaviour layer (this skill is the static grid; that's the dynamic behaviour)
- `manfred-ui-design:spacing-system` — for the spacing scale gutters draw from
- `manfred-ui-design:visual-hierarchy` — grid is the structural floor for hierarchy
- `manfred-design-systems:component-spec` — components live within the grid

## Tools used

- `Read` — `~/.claude/shared/DESIGN.md`, `tailwind.config`
- `manfred-ui-design:spacing-system` — for gutter values
- `manfred-ui-design:responsive-design` — for breakpoint behaviour

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
