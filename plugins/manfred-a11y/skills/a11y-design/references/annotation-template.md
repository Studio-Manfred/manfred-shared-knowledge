# Accessibility Annotation Template

Use this template to document the a11y requirements for a screen or component
before developer handoff. Fill in every section — leave nothing as "TBD".

---

## Screen / Component: [Name]

**Designer:** [Name]
**Date:** [Date]
**Design file:** [Link]

---

## 1. Landmark Regions

Map each major area to a semantic HTML landmark:

| Visual area | HTML element | `aria-label` (if needed) |
|-------------|-------------|--------------------------|
| Top bar / logo | `<header>` | — |
| Primary navigation | `<nav>` | `"Main navigation"` |
| Main content | `<main>` | — |
| Sidebar | `<aside>` | `"Related content"` |
| Bottom bar | `<footer>` | — |

---

## 2. Heading Hierarchy

List every text element that serves as a heading, regardless of its visual size:

| Visual text | Heading level | Notes |
|-------------|--------------|-------|
| [Page title] | `h1` | One per page |
| [Section title] | `h2` | |
| [Card title] | `h3` | |

> Do not skip levels (e.g., h1 → h3). Use CSS to style headings visually.

---

## 3. Focus Order

Number the interactive elements in the order keyboard focus should move through them
(left-to-right, top-to-bottom unless there is a logical reason to deviate):

1. Skip to main content link (visually hidden, first in DOM)
2. Logo / home link
3. Navigation items (left to right)
4. [Continue numbering all interactive elements...]

---

## 4. Text Alternatives

| Element | Type | Alt text / aria-label |
|---------|------|----------------------|
| [Company logo] | Informative image | `"[Company name] — home"` |
| [Decorative divider] | Decorative image | `alt=""` |
| [Close icon button] | Icon-only button | `aria-label="Close dialog"` |
| [Search icon button] | Icon-only button | `aria-label="Search"` |

---

## 5. Interactive Component States

For each custom interactive component, document all required states:

### [Component name, e.g. "Primary Button"]

| State | Visual description | Notes for developer |
|-------|--------------------|---------------------|
| Default | [describe] | |
| Hover | [describe] | |
| Focus | 2px solid #[color], offset 2px | Must contrast 3:1 against adjacent background |
| Active / pressed | [describe] | |
| Disabled | [describe] | Use `disabled` attr or `aria-disabled="true"` |
| Loading | Spinner + sr-only "Loading..." | `aria-busy="true"` on container |

---

## 6. ARIA Roles for Custom Widgets

| Component | ARIA role | Expected keyboard behaviour |
|-----------|-----------|----------------------------|
| [Tabs] | `tablist` / `tab` / `tabpanel` | Arrow keys to switch tabs |
| [Accordion] | `button` + `aria-expanded` | Enter/Space to toggle |
| [Modal] | `dialog` + `aria-modal="true"` | Tab trapped, Escape closes |
| [Autocomplete] | `combobox` + `listbox` | Arrow keys to navigate options |

---

## 7. Error & Validation Messages

| Field | Error message text | How announced |
|-------|-------------------|---------------|
| [Email] | "Enter a valid email address" | `role="alert"` on error paragraph |
| [Password] | "Password must be at least 8 characters" | `aria-describedby` pointing to error |

---

## 8. Motion & Animation

| Animation | Trigger | `prefers-reduced-motion` alternative |
|-----------|---------|--------------------------------------|
| [Page transition] | Route change | Instant swap, no fade |
| [Toast slide-in] | Action complete | Static appearance, no slide |

---

## Open Questions

- [ ] [Any unresolved design decisions that affect accessibility]
