---
name: a11y-dev
description: >
  Use when writing or reviewing front-end components, forms, modals, or interactive
  widgets, or when asked to "make this accessible", "add ARIA", "fix accessibility",
  "a11y-dev", "write accessible code", "WCAG", "screen reader support", "keyboard
  navigation", "focus management", "semantic HTML", "skip link", or "aria-label".
  Activate proactively when implementing any interactive UI element — including when
  the user creates a new React, Vue, or Svelte component with interactive elements,
  even if they don't mention accessibility.
---

# Accessibility for Developers

Build accessible code from the start: **native HTML first, ARIA second, custom solutions last**.

---

## When to Use

- Writing or reviewing front-end component code for accessibility
- User asks to make something accessible, add ARIA, fix keyboard navigation
- Implementing any interactive UI element (forms, modals, menus, tabs)

**When NOT to use:**
- Running a formal accessibility audit with reports → use `a11y-qa`
- Reviewing designs/mockups before handoff → use `a11y-design`
- Writing accessibility policy documents (no skill for this)

## 1. Semantic HTML First

Native elements provide keyboard support, focus management, and screen reader semantics for free.

```tsx
<button onClick={handleClick}>Submit</button>
<nav aria-label="Main navigation">...</nav>
<main id="main-content">...</main>
<article>...</article>
<aside>...</aside>
```

If a native element exists for the purpose, use it — a `<div onClick>` requires manual ARIA and keyboard handling that `<button>` gives you automatically.

---

## 2. ARIA Patterns

Use ARIA only when native semantics are insufficient. Wrong ARIA is worse than no ARIA because screen readers trust ARIA over the underlying element.

### Icon-Only Buttons

```tsx
<Button variant="ghost" size="icon" aria-label="Close dialog">
  <X size={16} aria-hidden="true" />
</Button>
```

Mark decorative icons `aria-hidden="true"` so screen readers skip them.

### Form Fields

Associate every input with a label. Use `aria-describedby` for helper text and errors.

```tsx
<Label htmlFor="email">Email</Label>
<Input
  id="email"
  type="email"
  aria-describedby="email-hint email-error"
  aria-invalid={!!error}
  aria-required="true"
/>
<p id="email-hint" className="text-sm text-muted-foreground">We'll never share your email.</p>
{error && <p id="email-error" role="alert">{error}</p>}
```

### Loading States

Use `aria-live` so screen readers announce dynamic changes without requiring focus.

```tsx
<div aria-live="polite" aria-busy={isLoading}>
  {isLoading ? <Skeleton /> : <Content />}
</div>
```

### Accordion / Disclosure

```tsx
<button aria-expanded={isOpen} aria-controls={contentId} onClick={onToggle}>
  {title}
</button>
<div id={contentId} hidden={!isOpen}>{children}</div>
```

### Tabs, Modal Focus Trap, ARIA Roles Reference

Full implementations and role lookup table → `references/aria-patterns.md`

---

## 3. Keyboard Navigation

All interactive elements must be reachable and operable by keyboard alone.

### Custom Interactive Elements

Only use this when no native element fits — native `<button>` handles Enter, Space, and focus automatically.

```tsx
<div
  role="button"
  tabIndex={0}
  onClick={handleClick}
  onKeyDown={(e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      handleClick();
    }
  }}
>
  Custom interactive element
</div>
```

---

## 4. Focus Management

### Visible Focus Styles

Removing focus outlines leaves keyboard users unable to track their position. Use `:focus-visible` so only keyboard users see the ring.

```tsx
// Tailwind
<Button className="focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2">
```

### Skip Link

Add as the first element in `<body>` so keyboard users can bypass repeated navigation.

```tsx
<a href="#main-content" className="sr-only focus:not-sr-only focus:absolute focus:z-50 focus:px-4 focus:py-2">
  Skip to main content
</a>
<main id="main-content" tabIndex={-1}>...</main>
```

---

## 5. Screen Reader Only Content

Visually hidden text for context that is obvious visually but absent from the DOM.
Full CSS pattern and common uses → `references/sr-only.md`

Quick usage: `<span className="sr-only">Opens in new tab</span>`

---

## 6. Color and Contrast

Contrast ratios, code examples, and tool recommendations → `references/anti-patterns.md`

Key thresholds: **4.5:1** normal text, **3:1** large text and UI components.

---

## 7. Heading Hierarchy

Headings create document structure that screen reader users navigate by shortcut. Style with CSS, not by picking a heading level.

```tsx
// Correct: logical hierarchy, styled visually with CSS
<h1>Page Title</h1>
  <h2 className="text-sm font-medium">Styled small but correct level</h2>
```

---

## 8. Descriptive Links and Buttons

Every link and button must make sense out of context — screen reader users navigate by link lists.

```tsx
// BAD: "Click here"
// GOOD:
<a href="/report.pdf">Download 2024 Annual Report <span className="sr-only">(PDF, 2.4 MB)</span></a>
```

---

## 9. Anti-Patterns

Common mistakes with fixes → `references/anti-patterns.md`

---

## 10. ESLint Static Analysis

Catch issues at dev time with `eslint-plugin-jsx-a11y`.
Full setup, CI integration, and false-positive guidance → `references/eslint-setup.md`

```bash
pnpm add -D eslint-plugin-jsx-a11y
npx eslint --config eslint.a11y.mjs src/
```

---

## 11. Pre-Commit Checklist

Full checklist with screen reader spot-check → `references/pr-checklist.md`

Key checks before merging interactive UI changes:
- All images have `alt`; icon-only buttons have `aria-label`
- All form inputs have an associated `<label>`
- Focus styles visible; keyboard navigation works end-to-end
- Dynamic changes announced via `aria-live` or `role="alert"`

---

## Examples

**Example 1 — Accessible dropdown menu**
Input: "write an accessible dropdown menu"
Output: `role="menu"` / `role="menuitem"` with arrow-key roving tabindex, `aria-expanded` on trigger, focus trapped when open, returned on Escape.

**Example 2 — Form accessibility review**
Input: "make this form accessible"
Output: Every input paired with `<label htmlFor>`, `aria-describedby` for hints/errors, `aria-invalid` + `role="alert"` on error messages, contrast verified.

---

## Troubleshooting

**Screen reader announces unexpected content** — Check for `aria-hidden="true"` on still-focusable elements; remove from tab order with `tabIndex={-1}` first.

**Focus trap not working** — Ensure the focusable selector covers all interactive types including `[tabindex]:not([tabindex="-1"])`. Re-query after dynamic content changes.

**`aria-live` not announcing** — The element must exist in the DOM before content is injected; don't mount it conditionally.

**Custom element fails keyboard test** — Needs `role="button"`, `tabIndex={0}`, and `onKeyDown` for Enter + Space. Prefer native `<button>` instead.

---

## Common Mistakes

- **Using `<div onClick>` instead of `<button>`** — Native elements give you keyboard support and semantics for free. Custom elements require manual ARIA, tabIndex, and keyDown handlers.
- **Adding ARIA to elements that don't need it** — Wrong ARIA is worse than no ARIA. Screen readers trust ARIA over the underlying element.
- **Removing focus outlines without replacement** — Use `:focus-visible` to show focus rings only for keyboard users, never remove them entirely.
- **Forgetting `aria-live` for dynamic content** — Screen readers won't announce content changes unless the live region exists in the DOM before content is injected.
- **Heading levels chosen by visual size** — Headings create document structure for screen reader navigation. Style with CSS, structure with hierarchy.

## Standards Reference

- [WCAG 2.2 Guidelines](https://www.w3.org/TR/WCAG22/)
- [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [axe-core Rules](https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md)
- [jsx-a11y Rules](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y#supported-rules)
