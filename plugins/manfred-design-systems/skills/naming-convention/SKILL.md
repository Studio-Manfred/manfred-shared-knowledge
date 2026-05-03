---
name: naming-convention
description: Use when naming components, tokens, files, CSS classes, or design assets in a Manfred codebase or design file — anyone says "what should I call this", "naming convention", "rename this token", "file naming", "PascalCase or kebab-case", "BEM", "token naming", "Figma layer naming", "component naming". Stack: React + Tailwind + CSS custom properties + Figma.
---

# naming-convention

A name that reads predictably is a name that doesn't need a comment. Manfred's naming is boring on purpose — predictable beats clever.

## Overview

Five principles, five contexts. The principles tell you how to think; the contexts tell you what to type.

**Principles:**

1. **Predictable** — given a category and a purpose, a competent reader can guess the name
2. **Consistent** — the same separator, the same casing, the same order, every time
3. **Scalable** — adding a sibling doesn't break the pattern
4. **Scannable** — sorts well in a list, reads in <1 second
5. **Unambiguous** — one name = one thing; one thing = one name

## When to use

- Naming a new component, token, file, or asset
- Renaming an existing one
- Reviewing a PR for naming consistency
- Setting up naming rules for a new project or design file
- Migrating a codebase to a new naming convention

**Skip when:**

- Naming a one-off internal variable in a function (use plain English, move on)
- Naming a Linear ticket (different system, different rules)

## Context-specific patterns

### Components (React / Vue)

**PascalCase**, named for purpose, not appearance.

```
✅ Button, Dialog, FormField, EmptyState, NavigationRail
❌ BlueButton, BigCard, FancyHeader, Wrapper, Container
```

Variants live in props, not names. `<Button variant="primary">`, not `<PrimaryButton>`.

### CSS classes

**kebab-case**, scoped where possible (CSS Modules, Tailwind).

```
✅ .form-field, .empty-state, .nav-rail
❌ .formField, .emptyState, .NavRail, .formfield
```

If the project uses Tailwind utilities, this section barely applies — utilities carry the naming.

### Tokens (CSS custom properties)

**kebab-case**, layered (`primitive` → `semantic` → `shadcn`). Pattern from `~/.claude/shared/DESIGN.md`:

```
Primitives:    --color-business-blue, --color-almost-black, --spacing-4
Semantic:      --color-text-primary, --color-interactive-brand-bg
shadcn:        --background, --foreground, --primary, --accent, --muted
```

Categories: `color` · `spacing` · `font` · `radius` · `shadow` · `motion` · `z`.

Pattern: `--<category>-<purpose>-<variant?>-<state?>`

```
✅ --color-text-primary, --color-interactive-brand-bg-hover, --spacing-4, --radius-md
❌ --textPrimary, --color-blue-thing, --my-custom-spacing, --pad
```

### Files

Lowercase, kebab-case, type prefix for grouping where helpful.

```
✅ button.tsx, dialog.tsx, use-toast.ts, form-field.test.tsx
✅ icon-trash.svg, illust-empty-cart.png  (assets benefit from prefix)
❌ Button.tsx (PascalCase file collides on case-insensitive filesystems), useToast.ts
```

Test files: `<name>.test.ts(x)`. Story files: `<name>.stories.tsx`. MDX docs: `<name>.mdx`.

(Note: convention varies — Manfred default is kebab-case for filenames, but some React projects use PascalCase. Match the project. Don't mix in one project.)

### Props (React)

**camelCase**, boolean props prefixed with `is` / `has` / `should` / `can`.

```
✅ variant, size, isLoading, hasError, asChild, onSelect
❌ Variant, IsLoading, has_error, on_select, fancy
```

Event handlers: `on<Event>` (`onClick`, `onChange`, `onSelect`).
Render props / slots: noun (`icon`, `leftSlot`, `trigger`).

### Figma layers and pages

- Pages: numbered + descriptive (`01 Cover`, `02 Foundations`, `03 Components`).
- Components: PascalCase, mirror the React component name (`Button`, `FormField`).
- Variants: prop-shaped (`Button/primary/md/default`, `Button/outline/lg/loading`).
- Frames inside a component: descriptive (`States/hover`, `Anatomy/with-icon`).

## Common pitfalls

| Pitfall | Why it bites |
|---|---|
| Abbreviations only the author understands (`btn-spcl-v2`) | Future-you doesn't remember. Spell it out. |
| Inconsistent separators (`form_field`, `formField`, `form-field` in same project) | Reading taxes break consistency. Pick one per context, document it. |
| Names based on visual properties (`BigBlueButton`, `RedBanner`) | Visuals change. Purpose doesn't. Name for the role, not the look. |
| Numeric versioning in names (`Button2`, `ButtonNew`) | Becomes `Button2New` becomes `Button2NewFinal`. Use git, not file names. |
| Plurals where unclear (`UserList` vs `Users`) | Pick singular for the component (`User`), plural for collections (`UserList`, `UserGrid`). Consistent. |
| Mixed casing for the same concept (`Listbox` vs `ListBox` vs `List_Box`) | One project, one casing. |

## Common rationalisations

| Excuse | Reality |
|---|---|
| "It's just a quick prototype, naming doesn't matter" | Prototypes ship more often than they don't. Name well from the start, save the rename. |
| "The name explains the implementation" (`UserListSortedByDate`) | Names describe purpose, not implementation. The component sorts users by date — that's a prop, not a name. |
| "I'll prefix everything with the project name to avoid collisions" (`AcmeButton`, `AcmeDialog`) | If you're collision-worried, use a barrel file or a namespace. Prefixes pollute every read. |
| "The new name is better but it'd be a huge rename" | LSP renames are reliable. Run them. The cost of a rename is once; the cost of a bad name is forever. |

## The hard rules

| Rule | What it means |
|---|---|
| **One pattern per context, documented** | The project has a NAMING.md (or a section in CLAUDE.md) that says "components are PascalCase, tokens are kebab-case", etc. Disputes get resolved by reading the doc, not by argument. |
| **Purpose, not appearance** | `EmptyState` not `BigCard`. `text-muted` not `text-grey`. |
| **Predictable separators** | Component path: `Category/Component/variant/state`. Token path: `category-purpose-variant-state`. Once chosen, never broken. |
| **Lint where possible** | Stylelint for CSS, ESLint for JS, custom token-name validators where it pays off. Convention enforced by tooling beats convention enforced by review. |

## Manfred lens

Naming is infrastructure — Cagan/Torres lens doesn't apply. But naming choices are sticky and hard to roll back. When in doubt, ask: "if a new hire reads this name in three months, can they guess what it is?"

## Tools used

- `Bash` / `Grep` — survey existing naming patterns across a codebase
- `Read` — `~/.claude/shared/DESIGN.md` for token patterns; existing `tailwind.config` / `tokens.css` for token surface
- `manfred-design-systems:design-token` — for token-specific naming
- `manfred-design-systems:component-spec` — for component-name decisions in spec context

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
