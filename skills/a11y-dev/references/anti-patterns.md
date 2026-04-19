# Accessibility Anti-Patterns

Common mistakes and their fixes.

## Anti-Pattern Table

| Anti-pattern | Problem | Fix |
|---|---|---|
| `<div onClick>` | No keyboard access, no role | Use `<button>` |
| `<img>` without `alt` | Screen readers read the file name | Add `alt` text or `alt=""` for decorative |
| Icon without `aria-label` | Announced as unlabelled button | Add `aria-label` to the button |
| Redundant `aria-label` on text button | Confusing double announcement | Remove `aria-label`, rely on text |
| `outline: none` without replacement | Keyboard users lose position | Use `focus-visible` styles |
| `tabIndex={1}` or higher | Breaks natural focus order | Only use `0` and `-1` |
| `aria-hidden="true"` on focusable element | Element unreachable from keyboard | Remove from tab order first |
| Placeholder as only label | Disappears on input | Always pair with `<label>` |
| Missing `lang` on `<html>` | Screen readers use wrong voice | `<html lang="en">` |

---

## Color and Contrast

| Text type | Minimum contrast ratio (WCAG AA) |
|-----------|----------------------------------|
| Normal text (< 18pt / < 14pt bold) | 4.5:1 |
| Large text (≥ 18pt or ≥ 14pt bold) | 3:1 |
| UI components and focus indicators | 3:1 |

```tsx
// Use semantic tokens with built-in contrast
<p className="text-foreground">Primary — high contrast</p>
<p className="text-muted-foreground">Secondary — still WCAG AA</p>
<p className="text-destructive">Error text</p>

// Color must never be the ONLY state indicator — combine with icon + text
<span className="text-destructive flex items-center gap-2">
  <AlertCircle size={16} aria-hidden="true" />
  Required field
</span>
```

**Tools:** axe DevTools browser extension, Colour Contrast Analyser, Figma A11y plugin.
