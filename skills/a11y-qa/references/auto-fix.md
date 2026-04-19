# Auto-Fix Reference

When reporting violations, include the recommended fix from this table.

| Violation rule | Fix |
|----------------|-----|
| `region` — content not in landmark | Wrap in `<main>`, put nav in `<nav>`, footer in `<footer>` |
| `heading-order` — skipped levels | Fix heading level; use CSS to style visually, not heading number |
| `color-contrast` — insufficient contrast | Adjust colors to meet 4.5:1 (normal text) or 3:1 (large text / UI) |
| `image-alt` — missing alt text | Add descriptive `alt`; use `alt=""` for decorative images |
| `button-name` — nameless button | Add visible text, `aria-label`, or `aria-labelledby` |
| `link-name` — nameless link | Add text content or `aria-label` (avoid "click here") |
| `label` — form control without label | Add `<label htmlFor="id">` or wrap input in `<label>` |
| `aria-*` — invalid ARIA | Fix attribute name, value, or role to match ARIA spec |
| `duplicate-id` | Make all IDs unique per page |
| `focus-order-semantics` | Fix DOM order; use CSS for visual reorder, not `tabindex` |
| `keyboard` — not keyboard accessible | Ensure all interactions work with Tab, Enter, Space, Esc |
