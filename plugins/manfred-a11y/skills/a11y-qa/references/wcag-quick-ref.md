# WCAG 2.2 AA Quick Reference

Key success criteria for QA testers to verify. Use this alongside the automated
scan results — axe-core maps violations to these criterion IDs.

| Criterion | Level | What to check |
|-----------|-------|---------------|
| 1.1.1 Non-text Content | A | All images, icons, charts have text alternatives |
| 1.3.1 Info and Relationships | A | Structure (headings, lists, tables) conveyed in markup |
| 1.3.2 Meaningful Sequence | A | Reading order in DOM matches visual order |
| 1.4.1 Use of Color | A | Color is not the sole visual indicator |
| 1.4.3 Contrast (Minimum) | AA | 4.5:1 normal text, 3:1 large text |
| 1.4.4 Resize Text | AA | Text scales to 200% without loss of content |
| 1.4.10 Reflow | AA | Content reflows at 400% zoom, no horizontal scroll |
| 1.4.11 Non-text Contrast | AA | UI components and focus indicators meet 3:1 |
| 1.4.12 Text Spacing | AA | No loss of content when letter/word/line spacing increased |
| 2.1.1 Keyboard | A | All functionality operable by keyboard |
| 2.1.2 No Keyboard Trap | A | Focus can always be moved away with keyboard |
| 2.4.3 Focus Order | A | Focus order preserves meaning and operability |
| 2.4.4 Link Purpose | A | Link purpose clear from text or context |
| 2.4.7 Focus Visible | AA | Keyboard focus indicator is visible |
| 2.4.11 Focus Appearance | AA (2.2) | Focus indicator meets minimum size and contrast |
| 2.5.3 Label in Name | A | Visible label text is included in accessible name |
| 2.5.8 Target Size (Minimum) | AA (2.2) | Interactive targets at least 24×24 px |
| 3.1.1 Language of Page | A | `<html lang="…">` is set |
| 3.3.1 Error Identification | A | Errors identified in text, not just color |
| 3.3.2 Labels or Instructions | A | All form fields have labels |
| 4.1.2 Name, Role, Value | A | All UI components have name, role, and state in markup |
| 4.1.3 Status Messages | AA | Status messages announced without focus (live regions) |

## Reference

- [WCAG 2.2 Understanding Docs](https://www.w3.org/WAI/WCAG22/Understanding/)
- [WCAG 2.1 Full Guidelines](https://www.w3.org/TR/WCAG21/)
