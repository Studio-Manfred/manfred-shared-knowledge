# Pre-Commit / PR Accessibility Checklist

Run through this before merging any PR that touches interactive UI components.

## Required checks

- [ ] All images have `alt` text (`alt=""` for purely decorative images)
- [ ] All form inputs have an associated `<label>` (via `htmlFor` or wrapping)
- [ ] Icon-only buttons have `aria-label` or `aria-labelledby`
- [ ] Focus styles are never removed without a visible replacement (use `focus-visible`)
- [ ] New interactive elements are reachable and operable by keyboard alone
- [ ] No heading levels are skipped (h1 → h2 → h3, not h1 → h3)
- [ ] Color is not the only way to convey information (errors use icon + text, not just red)
- [ ] Dynamic content changes are announced via `aria-live` or `role="alert"`
- [ ] Modals trap focus while open and restore focus to the trigger on close
- [ ] Tab order from top to bottom makes logical sense

## Quick screen reader spot-check

- macOS VoiceOver: `Cmd+F5` to toggle
- Windows NVDA: free download from nvaccess.org
- iOS VoiceOver: triple-click side button
- Android TalkBack: Settings → Accessibility → TalkBack

Navigate the changed area with the screen reader and verify:
- [ ] All labels and roles are announced correctly
- [ ] State changes (expanded, selected, checked) are announced
- [ ] No element is announced as "unlabelled" or reads out a file name/class name
