---
name: component-spec
description: Use when speccing a new component for the Manfred design system or any Manfred app — anyone says "spec a component", "what should the API for X look like", "design a Button/Modal/Card variant", "component requirements", "props for…", "states for…", "design + dev handoff for a component". Stack: Vite/React + Tailwind v4 + shadcn-shaped components + Storybook.
---

# component-spec

Spec a component before anyone codes it. Manfred ships shadcn-shaped components — `Button`, `Dialog`, `Tooltip`, `RadioGroup`, etc. — so the spec stays close to the shadcn contract and consumes existing tokens. No invented API surfaces, no hardcoded values, no "we'll figure out a11y later."

## Overview

A complete component spec covers anatomy, variants, states, props, accessibility, and tokens. The Manfred difference: every spec ties back to existing tokens (`manfred-design-systems:design-token`), follows the shadcn shape where one exists, and treats WCAG 2.2 AA as a hard floor — not a "nice-to-have".

## When to use

- Adding a new component to `Studio-Manfred/manfred-design_system`
- Adding a project-local component that follows Manfred conventions
- Spec'ing a variant of an existing component (e.g. a new Button variant)
- Designer-dev handoff for any UI surface that has interactivity

**Skip when:**

- Pure layout/markup with no API surface (just write the JSX)
- Editing an existing spec to tweak copy or props (just edit it)
- The user wants tokens, not a component (use `manfred-design-systems:design-token`)

## Pre-flight

Before speccing:

1. **Check the shadcn shape.** Does shadcn ship something close? (`Dialog`, `Tooltip`, `RadioGroup`, `Toast`, `Popover`, etc.) If yes, the API mirrors the stock shadcn shape — same prop names, same composition. Manfred's existing components (Section 4 of `~/.claude/shared/DESIGN.md`) follow this rule deliberately.
2. **Check existing components.** `Alert · Badge · Breadcrumb · Button · Checkbox · Dialog · FormField · Icon · Logo · ProgressBar · Radio · SearchBar · Spinner · TextInput · Toast · Tooltip · Typography` already ship. If you're about to recreate one, stop.
3. **Check the tokens.** Read `~/.claude/shared/DESIGN.md` Section 2 (colours), Section 3 (typography), Section 5 (layout/spacing). The spec consumes these — it doesn't invent new ones.

## Spec structure

```markdown
# <ComponentName>

## What it is
One sentence. The job this component does.

## When to use / when not to
- Use when …
- Use [other component] when …
- Skip when …

## Anatomy
[ASCII or bullet breakdown — required vs optional slots]

## Props / API
| Prop | Type | Default | Required | Description |
|---|---|---|---|---|
| variant | "primary" \| "outline" \| "ghost" | "primary" | no | Visual emphasis |
| size | "sm" \| "md" \| "lg" | "md" | no | Density |
| isLoading | boolean | false | no | Shows spinner, disables interaction |
| asChild | boolean | false | no | Render as Slot for composition |

(Mirror shadcn shapes where one exists. `asChild` wherever composition matters.)

## States
- Default · Hover · Focus · Focus-visible · Active · Disabled · Loading · Error
- Each state has a token-driven visual treatment (no hex literals)

## Tokens consumed
- Surface: `bg-background` / `bg-card` / `bg-primary` (which?)
- Text: `text-foreground` / `text-primary-foreground` / `text-muted-foreground` (which?)
- Border: `border-border` (or none)
- Spacing: `p-2` / `p-4` / `gap-3` (Tailwind primitives)
- Radius: `rounded-md` / `rounded-lg`
- Motion: `transition-colors duration-150` (or none)

## Accessibility (WCAG 2.2 AA — non-negotiable)
- Role: [native element or ARIA role]
- Keyboard: Tab to focus, Enter/Space to activate, Esc to dismiss (if applicable)
- Focus indicator: 2px ring, `ring-ring` token, 3:1 contrast against adjacent surface
- Target size: 24×24 px minimum (44×44 px recommended for primary actions)
- Screen reader: [accessible name source — children, aria-label, aria-labelledby]
- Reduced motion: respects `prefers-reduced-motion`

## Composition
[How this component combines with others — e.g. "Use inside FormField for labels + errors"]

## Examples
```tsx
<ComponentName variant="primary">Default</ComponentName>
<ComponentName variant="outline" size="lg">Large outline</ComponentName>
<ComponentName isLoading>Saving…</ComponentName>
<ComponentName asChild><a href="/x">As link</a></ComponentName>
```

## Anti-patterns
- Don't [thing] — [why]
- Don't [thing] — [why]
```

## The hard rules

| Rule | What it means |
|---|---|
| **shadcn shape if one exists** | Mirror prop names and composition (`asChild`, `<Trigger>`, `<Content>` slots). Drift breaks shadcn-savvy code and the design system's own components. |
| **Tokens, not literals** | Every visual value resolves through `manfred-design-systems:design-token`. No hex, no `bg-green-500`. |
| **Every interactive state has a focus indicator** | Manfred design principle 5 — accessibility as baseline. WCAG 2.2 AA. |
| **`asChild` for composition over wrapping** | Manfred design principle 10 — composition over wrapping. Use Radix `Slot` (or shadcn equivalent) so consumers can render the component as their preferred element. |
| **No invented variant names** | Variants map to existing shadcn slots (`primary`, `outline`, `ghost`, `destructive`) where possible. New names need a reason. |

## Common rationalisations

| Excuse | Reality |
|---|---|
| "shadcn doesn't have this exact thing, I'll invent the API" | Check Radix primitives first (Popover, Listbox, Combobox, Slider). Manfred's components are Radix + shadcn shapes. New API needs justification. |
| "Hover and focus are the same state, one prop is fine" | They're not. Focus is keyboard-only, hover is pointer-only. Both need distinct visual treatment. WCAG 2.4.7 requires focus visible. |
| "Loading is just disabled with a spinner" | Loading needs `aria-busy`, the button stays focusable, click is a no-op. Disabled removes from tab order — different a11y semantics. |
| "We'll add dark mode later" | Use semantic tokens from the start and dark mode is free. Adding it later means rewriting every component. |

## Manfred lens

Component specs are infrastructure — the Cagan/Torres lens doesn't apply directly. But: a new component is a small commitment. If it's only used once, ask if it should be a component at all (vs inline JSX).

## Tools used

- `Read` — `~/.claude/shared/DESIGN.md` for token surface and existing components
- `manfred-design-systems:design-token` — for every colour/spacing/radius decision
- `manfred-design-systems:a11y-design` — for the a11y annotation pass on the spec
- `manfred-design-systems:a11y-dev` — for the implementation gate

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
