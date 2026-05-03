---
name: icon-system
description: Use when adding, organising, or auditing icons in a Manfred app — anyone says "add an icon", "icon library", "what icon should I use", "Lucide / Phosphor / Heroicons", "icon size", "icon naming", "SVG sprite", "icon component", "swap an icon", "icon accessibility". Stack: React + Lucide (Manfred's default) or project-chosen icon library, exposed via the `Icon` component.
---

# icon-system

Manfred ships an `Icon` component that wraps Lucide. The icon system isn't a place to be creative — it's a place to be consistent. Same grid, same stroke, same sizes, same naming, every time.

## Overview

Icons are tiny, repeated, semantic. They live next to text labels (or stand alone as actions), and they get scanned, not read. The system has four parts:

1. **Library** — a single source. Manfred defaults to Lucide (currently shipped). Don't mix libraries.
2. **Sizes** — fixed scale (`xs`/`sm`/`md`/`lg`/`xl`), always tied to the surrounding type and target size.
3. **Naming** — predictable, category-prefixed (`navigation-arrow-right`, not `arr-r-fancy`).
4. **Accessibility** — every icon has a label or `aria-hidden`. No exceptions.

## When to use

- Adding a new icon to a project
- Picking which icon to use for a specific UI moment
- Auditing existing icon usage (mixed libraries, inconsistent sizes, missing labels)
- Replacing an icon library across a codebase
- Documenting the icon system for a team

**Skip when:**

- Designing a new bespoke icon (different skill — needs a designer with grid/stroke/keyline knowledge, not this)
- Adding a logo or illustration (logos use the `Logo` component; illustrations are not icons)

## Pre-flight

Before adding an icon:

```bash
grep -rn "from 'lucide-react'" src/ | head
test -f src/components/Icon.tsx && cat src/components/Icon.tsx | head -30
```

Find:

1. Which library the project uses (Lucide is Manfred default — confirm before assuming)
2. Whether there's a wrapper `Icon` component (Manfred ships one — re-use it)
3. Existing icon sizes used in the project (don't introduce a new one without reason)

## The grid + size scale

Icons sit on a fixed grid. Manfred's `Icon` component handles this — pass a `size` prop, get the right pixel dimensions and surrounding box.

| Size | Pixels | When |
|---|---|---|
| `xs` | 12 px | Captions, metadata, tag chips |
| `sm` | 16 px | Inline with body text, dense lists |
| `md` | 20 px (default) | Buttons, inputs, most UI surfaces |
| `lg` | 24 px | Section headers, primary nav |
| `xl` | 32 px+ | Empty states, hero moments |

**Touch targets:** the icon's *visual* size and the icon's *target* size are different. A 20 px icon in a button still needs a 24×24 px (min) or 44×44 px (recommended) hit area — handled by the button's padding, not the icon's.

## Naming

Format: `<category>-<name>-<variant>`

Categories: `action` · `navigation` · `content` · `communication` · `social` · `status` · `file` · `device`

Examples:

- `action-trash` (delete)
- `action-share`
- `navigation-arrow-right`
- `navigation-chevron-down`
- `status-check-circle`
- `status-alert-triangle`
- `file-image`
- `device-mobile`

Lucide's own names (camelCase) map cleanly — `Trash2` → `action-trash`, `ChevronDown` → `navigation-chevron-down`. Use Lucide's name in code (`<TrashIcon />`), use the categorised name in docs and design files (Figma).

## Accessibility — non-negotiable

Every icon makes one of two choices:

| Use | Markup | Example |
|---|---|---|
| **Decorative** (icon repeats text label) | `aria-hidden="true"` | `<button><CheckIcon aria-hidden="true" /> Save</button>` |
| **Meaningful** (icon stands alone) | `aria-label="…"` | `<button aria-label="Close"><XIcon aria-hidden="true" /></button>` (label on the button, icon hidden — same effect) |

Rules:

- Icon-only buttons: label goes on the **button**, icon stays `aria-hidden`. Don't double up.
- Icon next to text: icon is `aria-hidden`. Text carries the meaning.
- Icon as the only thing in a link: link needs `aria-label` describing the destination.
- **Never** use `title` as the only label — it's tooltip-only, doesn't reach all assistive tech.
- **Never** rely on colour to distinguish two icons (status colour + icon shape — both, always).

Pair `manfred-design-systems:a11y-dev` for the implementation pass.

## The hard rules

| Rule | What it means |
|---|---|
| **One library per project** | Lucide unless the project decided otherwise. Mixing Lucide + Phosphor + Heroicons in the same codebase = visual inconsistency + bundle bloat. |
| **Use the `Icon` component, not raw library imports** | Wrapping centralises sizing, colour (token-driven), and a11y defaults. Raw imports leak inconsistency. |
| **Tokens drive icon colour** | `text-foreground` / `text-primary` / `text-muted-foreground` — never hex. See `manfred-design-systems:design-token`. |
| **Pair icon + text for critical actions** | Icon-only is OK for universally recognised symbols (close, search, menu) — anything else gets a text label. Recognition over recall. |
| **24×24 px target minimum** | WCAG 2.5.8. Bigger if the action is primary. |

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Lucide doesn't have this exact icon, I'll grab one from Heroicons" | Pick the closest Lucide. If nothing fits, request an addition or commission a custom SVG that matches Lucide's stroke + grid. Mixing libraries is permanent inconsistency. |
| "It's icon-only but everyone knows what a trash can means" | Trash, close, search, menu — yes. Most others — no. Add a text label or a tooltip + `aria-label`. Don't assume. |
| "I'll just colour this icon red for danger" | Status colour + icon shape, always. Colour-blind users see no red. Pair with `status-alert-triangle` or similar. |
| "I'll use the title attribute as the label" | `title` is tooltip-only and unreliable on touch devices and some screen readers. Use `aria-label`. |

## Manfred lens

Icon decisions are infrastructure — Cagan/Torres lens doesn't apply. But icons are a **usability** surface and an **accessibility** surface. When in doubt about whether an icon-only action is recognisable, run a mini usability check (`manfred-design-research:usability-test-plan`) — recognition is testable.

## Tools used

- `Bash` / `Grep` — survey current icon usage across a project
- `Read` — `~/.claude/shared/DESIGN.md` Section 7 (Iconography & Imagery)
- `manfred-design-systems:design-token` — for icon colour decisions
- `manfred-design-systems:a11y-dev` — for the implementation pass on icon a11y
- Lucide — `https://lucide.dev` for icon search

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
