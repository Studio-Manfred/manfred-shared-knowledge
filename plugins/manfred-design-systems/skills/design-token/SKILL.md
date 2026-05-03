---
name: design-token
description: Use when defining, extending, or consuming design tokens — anyone says "give me CSS for…", "add a color/spacing/radius/shadow", "make a callout/banner/badge/card", "what color should I use", "tokens.css", "design system colors", "Tailwind class for…", "dark mode this", "add a success/warning/error state", "extend the palette", "new semantic token", "brand color", "convert this hex to a token". Stack: Tailwind v4 + CSS custom properties + shadcn-shaped components. Manfred design system specifically.
---

# design-token

Tokens before code. Every colour, spacing, radius, shadow, and motion value in a Manfred app comes from `~/.claude/shared/DESIGN.md`'s three-layer architecture — primitives → semantic → shadcn contract. No hex literals in components. No `bg-green-500` shortcuts that bypass the layer.

This skill is the gate. If a token doesn't exist, the skill stops and asks where to add it — it doesn't invent one.

## Overview

A **design token** is a named value (`--color-business-blue`, `--spacing-4`, `--radius-md`) that components consume instead of hardcoded values. Manfred's tokens live in `src/tokens/tokens.css` of `Studio-Manfred/manfred-design_system` and are re-exported via Tailwind v4's `@theme` directive.

**Three layers, top-down:**

1. **Primitives** — raw brand values (`--color-business-blue: #2c28ec`). Defined once. Components never reach this layer directly.
2. **Semantic aliases** — purpose-bound (`--color-text-primary`, `--color-interactive-brand-bg`). Theme-aware. Flip in dark mode.
3. **shadcn contract** — `--background`, `--foreground`, `--primary`, `--accent`, `--muted`, `--destructive`, `--border`, `--ring`. What components actually consume. Stays stable so shadcn shapes work unchanged.

Two utility *families* in Tailwind:

- **Semantic utilities** (`bg-background`, `text-foreground`, `bg-primary`, `border-border`) — flip with theme. Default for components.
- **Brand utilities** (`bg-business-blue`, `bg-human-pink`, `bg-beige`) — literal, do **not** flip. Only for explicit literal-brand surfaces (logo backgrounds, hero panels, marketing moments).

## When to use

- Anyone asks for CSS, a Tailwind class, or a colour/spacing value
- A new component needs styling
- Adding a state (success, warning, error, info, loading) that may not exist yet
- Converting a Figma spec or hex value into a token
- Deciding between brand utility and semantic token
- Reviewing a PR that introduced raw hex or `bg-green-500`-style colours

**Skip when:**

- Pure markup with no styling decisions (use `manfred-design-systems:a11y-dev` for semantic HTML)
- Component composition without new tokens (use `manfred-design-systems:component-spec`)
- The user is editing the design system itself, not consuming it (different scope — they'll know)

## Pre-flight (do this every time)

Before producing any colour, spacing, or surface value:

```bash
test -f ~/.claude/shared/DESIGN.md && head -200 ~/.claude/shared/DESIGN.md
```

Find:

1. **What primitives exist** (Section 2 — the brand colour table)
2. **What semantic aliases exist** (Section 2 — semantic layer paragraph)
3. **What shadcn tokens exist** (`--background`, `--foreground`, `--primary`, etc.)
4. **What dark mode does** (Section 9)

If `~/.claude/shared/DESIGN.md` is not readable, ask the user to install it via `manfred-shared-knowledge` or point you at the project's `tokens.css`. **Do not write CSS without seeing the token surface first.**

## The hard rules

| Rule | What it means | What violates it |
|---|---|---|
| **No raw hex in components** | Every colour value comes from a token | `background: #f0fdf4`, `border-color: #22c55e`, `color: rgb(34, 197, 94)` |
| **No default Tailwind palette colours** | Tailwind's `green-500`, `amber-50`, `slate-200` etc. bypass the token layer | `bg-green-50`, `text-amber-800`, `border-slate-200` |
| **Components consume semantic, not primitives** | Components use `bg-background` / `text-foreground` / `bg-primary`, not `bg-business-blue` | `<Button className="bg-business-blue">` (unless explicitly literal-brand) |
| **Dark mode flips automatically** | Use semantic tokens so `.dark` flips them; brand utilities are literal and stay put | Hardcoding light-only colours that break in `.dark` mode |
| **Missing semantics → stop and ask** | If `--success` / `--warning` / `--info` don't exist, do not invent them | Inventing a green for `success` because the user asked |

## The flow

### 1. Map the request to a token layer

Ask: what kind of value does the user need?

- **Page background, card, surface** → semantic (`bg-background`, `bg-card`, `bg-muted`)
- **Body text, headings** → semantic (`text-foreground`, `text-muted-foreground`)
- **CTA, focus ring, link** → semantic (`bg-primary`, `text-primary`, `ring-ring`)
- **Border, divider** → semantic (`border-border`)
- **Destructive action** → semantic (`bg-destructive`, `text-destructive`)
- **Literal brand surface** (logo plate, hero panel) → brand utility (`bg-business-blue`, `bg-human-pink`)
- **State the user named** (success, warning, error, info) → check if a semantic exists (`destructive` exists; `success`, `warning`, `info` likely don't)

### 2. If the semantic doesn't exist, stop

Manfred's palette is intentionally narrow: business-blue for action, warm neutrals to hold the room, human-pink for moments of care, white/almost-black for surfaces and text. There is no canonical green-for-success or amber-for-warning.

When the user asks for a state colour you can't find:

```
You asked for a success/warning/error state, but Manfred's semantic layer doesn't ship that token.
Three options:

  (a) Add it to the semantic layer — pick a primitive (or a new one), add `--color-success`
      to tokens.css, expose it in `@theme`. Token PR first, then your component PR.
      Real cost: 15–30 min, not "blocked indefinitely."
  (b) Reuse an existing semantic — `--accent` for soft positive emphasis, `--destructive`
      for negative. Enough.
  (c) Use a neutral surface + an icon — `bg-muted` + a checkmark/warning glyph carries the
      meaning without needing colour to do the work. Most accessible.

Which way? I'm not going to invent a colour and pretend it's a token.
```

Wait for the answer. Don't ship CSS until the user picks.

### 3. Produce the CSS

Once the token layer is clear, output the component using **Tailwind utilities first, CSS variables second**:

```tsx
// preferred — Tailwind utility, theme-aware
<div className="bg-card text-card-foreground border border-border rounded-lg p-4">
```

```css
/* fallback — CSS variable, when outside Tailwind utilities */
.my-callout {
  background-color: hsl(var(--card));
  color: hsl(var(--card-foreground));
  border: 1px solid hsl(var(--border));
  padding: var(--spacing-4);
  border-radius: var(--radius-md);
}
```

Never:

```css
/* never — raw hex */
background-color: #f0fdf4;

/* never — default Tailwind palette */
.callout { @apply bg-green-50 text-green-800; }

/* never — primitive in a component (unless literal-brand) */
<div className="bg-business-blue text-white">
```

### 4. Confirm dark mode behaves

If the component uses semantic tokens (`bg-background`, `bg-card`, etc.), dark mode flips automatically — the semantic layer redefines the values under `.dark`. Verify by mentally toggling: does the contrast still work? Does the meaning still read?

If the component uses brand utilities (`bg-business-blue`), they **do not flip**. That's intentional — the brand colour is literal. But it means the surrounding text/contrast must work in both modes; usually pair with `text-white` or another absolute that doesn't flip either.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "It's just a one-off, I'll inline a hex this once" | One-offs are how token systems rot. The next dev sees `#f0fdf4` and copies it. Add it as a token or pick an existing one. |
| "The user said they're in a hurry" | A 30-second token check is faster than the rework caused by hardcoding. Token discipline is the fast path, not the slow one. |
| "Tailwind's `green-500` is fine, it's still a utility" | It's a utility outside the token system. It won't flip in dark mode, won't update when the palette changes, and signals to other devs that bypassing tokens is OK. |
| "I'll use the primitive directly, it's the same colour" | Components consuming primitives can't be re-themed. The whole point of the semantic layer is that you can swap the primitive without touching components. |
| "They asked for `success` green, I have to give them green" | No, you have to give them a token. If the token doesn't exist, asking the user to choose between (a) add it (b) reuse a sibling (c) use a neutral + icon is the right move. |
| "shadcn contract is just shadcn, I can use my own names" | Manfred's components follow stock shadcn shapes. Drifting from `--primary` / `--accent` / `--muted` etc. breaks composition with shadcn-savvy code and the design system's own components. |
| "Dark mode can wait, ship light first" | Manfred is dark-mode-on-day-one (Section 9 of DESIGN.md). Shipping light-only writes a TODO that becomes never. Use semantic tokens and dark mode is free. |
| "I'll use `var(--color-success)` and add the token later, my component file stays clean" | Worse than a hex. The reference looks legitimate in review but resolves to nothing — the component renders unstyled or with a browser fallback. Committing a reference to a token that doesn't exist is the same debt as the hex, just disguised. Add the token first, or use option (b) / (c). |

## Red flags — STOP

- About to write a hex literal in a component file
- About to use a Tailwind palette colour that's not in Manfred's `@theme`
- About to invent a `--success` / `--warning` / `--info` token without user confirmation
- The user pushed for "just give me the CSS" and you're about to comply without reading DESIGN.md
- The component uses a brand utility but the surrounding text isn't accounted for in both modes
- You're styling a component variant that should map to a shadcn slot (`primary`, `outline`, `ghost`, etc.) but you're inventing a new variant name

## Manfred lens

Tokens are infrastructure, not strategy — Cagan's 4 risks and the OST don't apply. Skip the discovery lens for this skill.

But: token decisions touch **brand consistency** and **usability** (contrast, dark mode, focus visibility). When in doubt about contrast or focus rings, hand off to `manfred-design-systems:a11y-design` (mockup stage) or `manfred-design-systems:a11y-qa` (live code).

## Output format

When the user wanted CSS for a component, return:

```markdown
## Tokens used

- `bg-card` (semantic) — surface
- `text-card-foreground` (semantic) — text
- `border-border` (semantic) — outline
- `p-4`, `rounded-lg` (spacing/radius primitives via Tailwind)

## Component

[Tailwind-first JSX, semantic tokens only]

## Dark mode

Verified: all tokens are semantic, flip automatically under `.dark`.
[OR: Uses brand utility `bg-business-blue` — does not flip; paired with `text-white` which also doesn't flip; contrast works in both modes.]

## Token additions needed

[None — used existing tokens]
[OR: Need `--color-success` added to semantic layer first; PR'd separately.]
```

When the user asked for a state colour that doesn't exist, return the (a)/(b)/(c) prompt from step 2 and **do not produce CSS** until they pick.

## Tools used

- `Bash` — `head ~/.claude/shared/DESIGN.md`, `cat src/tokens/tokens.css`
- `Read` — `~/.claude/shared/DESIGN.md` for full token surface
- `Grep` — find existing usages of a token before adding a new one
- `manfred-design-systems:a11y-design` — when contrast/focus questions come up at mockup stage
- `manfred-design-systems:a11y-qa` — when contrast/focus questions come up in live code
