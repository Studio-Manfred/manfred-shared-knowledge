# Manual Test Checklist

Automated tools find ~30–40% of accessibility issues. Complete this checklist
for the pages under test after running axe-core and/or ESLint scans.

## Keyboard-Only Navigation

- [ ] Tab from the top of the page to the bottom — every interactive element receives focus
- [ ] Focus indicator is always visible (never disappears)
- [ ] Tab order matches visual reading order
- [ ] Skip link appears and works (keyboard users bypass navigation)
- [ ] Modal / dialog: Tab stays trapped inside while open; Escape closes it and returns focus to the trigger
- [ ] Custom widgets (sliders, date pickers, tabs): arrow keys work as expected

## Screen Reader Testing

Test with at least one of: NVDA + Chrome (Windows), VoiceOver + Safari (macOS/iOS),
TalkBack (Android).

- [ ] Page `<title>` is descriptive and unique per page
- [ ] `<html lang="…">` is set correctly
- [ ] Heading structure makes sense when read in sequence (h1 → h2 → h3)
- [ ] All images are announced with meaningful alt text (decorative images are skipped)
- [ ] All form fields announce their label and any error messages
- [ ] Error messages are announced immediately on validation (not only visually highlighted)
- [ ] Dynamic content changes (loaded data, toasts, status) are announced via live regions
- [ ] Link text is descriptive out of context (no "click here" or "read more" alone)
- [ ] Buttons announce their purpose

## Visual / Cognitive Checks

- [ ] Zoom to 200% — no content is clipped, truncated, or overlaps
- [ ] Zoom to 400% — page is still usable (scrolls, no horizontal scroll for text)
- [ ] Color is never the only way to convey information (errors also have icons or text)
- [ ] All text meets contrast ratio: 4.5:1 normal, 3:1 large text
- [ ] Animated content can be paused, stopped, or hidden (WCAG 2.2.2)
- [ ] Session timeouts warn the user with enough time to extend

## Touch / Mobile

- [ ] All interactive targets are at least 24×24 px (WCAG 2.5.8 minimum) / 44×44 px recommended
- [ ] No functionality relies on hover only
- [ ] Pinch-zoom is not disabled (`user-scalable=no` is absent)
