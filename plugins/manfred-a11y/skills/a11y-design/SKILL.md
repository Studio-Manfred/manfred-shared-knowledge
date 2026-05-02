---
name: a11y-design
description: >
  Use when asked to "review my design for accessibility", "annotate my Figma",
  "check my mockup", "create a11y specs", "accessibility handoff", "inclusive design
  review", "design audit", "a11y-design", "accessibility before handoff", "contrast
  check", "focus order", "target size", or "designer accessibility checklist". Also
  activate when the user shares a design file, mockup screenshot, or discusses UI
  specs for developer handoff, even without explicitly mentioning accessibility.
---

# Accessibility for Designers

Move accessibility left in the lifecycle — catch issues before code is written.

---

## When to Use

- Reviewing designs, mockups, or Figma files for accessibility before handoff
- Creating accessibility annotations or specs for developers
- User shares a design screenshot and asks about accessibility

**When NOT to use:**
- Writing or fixing accessible code → use `a11y-dev`
- Running automated audits on live code → use `a11y-qa`
- Writing accessibility policy documents (no skill for this)

## 1. Annotations (Documentation & Specs)

Convert designs into clear a11y requirements for developers. Full annotation template → `references/annotation-template.md`

Key annotations to generate:
- **Focus Order:** Numbered `tab` sequence for interactive elements
- **Landmarks:** `<header>`, `<nav>`, `<main>`, `<footer>`, `<aside>` with any required `aria-label`
- **Text Alternatives:** Specific `alt` text for images, `aria-label` for icon-only buttons
- **Heading Hierarchy:** Assign `h1`–`h6` by document structure, not visual size
- **State Indicators:** Focus, hover, disabled, loading, error for every interactive component
- **ARIA Roles:** Suggest roles (`tablist`, `combobox`, `dialog`) for custom widgets, including expected keyboard behaviour

---

## 2. Assessment

### Visual & Cognitive Audit
- **Color Contrast:** 4.5:1 (normal text), 3:1 (large text)
- **Font Scaling:** Readable and unbroken at 200% zoom
- **Color Independence:** Information not conveyed only through color
- **Target Size:** Interactive targets at least 24×24 px (WCAG 2.2 AA), 44×44 px recommended

### Storybook / Live Code Check
- Inspect rendered DOM for semantic elements in custom components
- Verify hidden elements use `aria-hidden="true"` or `display: none`

---

## 3. Tool Integration

### With Figma MCP connected
Use MCP tools to list layers, inspect properties, read accessibility comments, export design tokens, and identify components missing focus/disabled states.

### Without Figma MCP
Work from screenshots or exported screens. Produce annotation documents, contrast assessments from visible hex values, and lists of missing states.

### Design System Alignment
- Flag colours used in code that don't exist in the approved palette
- Identify one-off colours that may fail contrast
- Check interactive component variants (default, focus, hover, disabled, error) are all defined

---

## 4. Thinking About Accessibility

Challenge assumptions during design:
- **"What if I couldn't use a mouse?"** — Keyboard navigation, focus indicators
- **"What if I couldn't see the screen?"** — Screen reader semantics, logical order
- **"What if I were in bright sunlight?"** — Contrast, brightness

---

## 5. Pre-Handoff Checklist

Before handing off to developers:
- [ ] **Contrast:** All text and UI components meet WCAG AA
- [ ] **Hierarchy:** Headings identified and logically ordered
- [ ] **Labels:** All icon-only actions have intended accessible names
- [ ] **Targets:** No interactive element smaller than 24×24 px
- [ ] **Focus:** Focus states designed and clearly visible
- [ ] **Motion:** Animations respect `prefers-reduced-motion`

---

## Examples

**Example 1 — Annotating a Figma screen**
Input: "annotate my design for accessibility"
Output: Map focus order, identify landmarks, provide alt text, assign heading levels, define state variants. Deliver as annotation document for the Figma file.

**Example 2 — Pre-handoff review**
Input: "is my design ready for accessibility handoff?"
Output: Walk through Section 5 checklist item by item, flag missing items with specific guidance, confirm ARIA roles documented for custom widgets.

---

## Troubleshooting

**No Figma MCP connected** — Work from screenshots. Ask the user to export screens and describe the component hierarchy.

**Contrast ratio is borderline** — Use exact hex values. Between 3:1 and 4.5:1 qualifies only for large text (18pt+ or 14pt bold). When in doubt, recommend adjusting.

**Focus states not designed** — Flag as handoff blocker. Required under WCAG 2.4.7 and 2.4.11. Suggest a 2px solid ring with 3:1 contrast against adjacent background.

**Custom widget with no ARIA role** — Use the closest role and document expected keyboard behaviour explicitly in annotations.

---

## Common Mistakes

- **Skipping focus state design** — Focus states are a WCAG requirement (2.4.7, 2.4.11), not optional. Flag missing focus states as a handoff blocker.
- **Only checking color contrast for text** — UI components and graphical objects also need 3:1 contrast against adjacent colors.
- **Choosing heading levels by visual size** — Assign h1-h6 by document structure, then style with CSS. A small heading can be h2.
- **Not annotating keyboard behavior for custom widgets** — Developers need to know expected keyboard interactions (arrow keys, Enter, Escape) for non-native components.
- **Assuming Figma MCP is required** — The skill works from screenshots or exported screens too. Produce annotations, contrast assessments, and state checklists without Figma access.

## Standards Reference

- [WCAG 2.2 Understanding Docs](https://www.w3.org/WAI/WCAG22/Understanding/)
- [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [A11Y Project Checklist](https://www.a11yproject.com/checklist/)
- Annotation template → `references/annotation-template.md`
