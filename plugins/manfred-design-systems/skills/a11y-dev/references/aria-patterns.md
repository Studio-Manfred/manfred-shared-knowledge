# ARIA Patterns Reference

Full implementations for the most common complex ARIA patterns.

---

## Tabs (tablist / tab / tabpanel)

```tsx
<div role="tablist" aria-label="Settings sections">
  <button
    role="tab"
    aria-selected={activeTab === 'general'}
    aria-controls="panel-general"
    id="tab-general"
    tabIndex={activeTab === 'general' ? 0 : -1}
    onClick={() => setActiveTab('general')}
  >
    General
  </button>
  {/* more tabs... */}
</div>

<div
  role="tabpanel"
  id="panel-general"
  aria-labelledby="tab-general"
  hidden={activeTab !== 'general'}
>
  {/* panel content */}
</div>
```

**Required keyboard behaviour (roving tabindex):** Arrow Left/Right moves between tabs.
Tab moves into the active panel. Implement `onKeyDown` on the tablist that calls
`setActiveTab` and shifts focus on `ArrowLeft` / `ArrowRight`.

---

## Modal Focus Trap

When a modal opens, focus must stay inside it. When it closes, return focus to the
trigger element.

```tsx
function Modal({ isOpen, onClose, triggerRef, children }) {
  const modalRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!isOpen) return;

    // Move focus into the modal
    const focusable = modalRef.current?.querySelectorAll<HTMLElement>(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    focusable?.[0]?.focus();

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        onClose();
        triggerRef.current?.focus(); // return focus to trigger
      }
      // Trap Tab/Shift+Tab within modal
      if (e.key === 'Tab' && focusable) {
        const first = focusable[0];
        const last = focusable[focusable.length - 1];
        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault();
          last.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      }
    };

    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose, triggerRef]);

  if (!isOpen) return null;

  return (
    <div ref={modalRef} role="dialog" aria-modal="true" aria-labelledby="dialog-title">
      {children}
    </div>
  );
}
```

**Key rules:**
- Re-query focusable elements if modal content changes dynamically
- Always return focus to the trigger on close (Escape key and close button)
- Use a real dialog library (Radix, Headless UI) in production — they handle edge cases

---

## ARIA Roles Quick Reference

| Role | Use for |
|------|---------|
| `button` | Clickable non-`<button>` elements |
| `dialog` | Modal dialogs |
| `alert` | Important messages that interrupt (e.g., errors) |
| `status` | Polite status updates (e.g., "Saved") |
| `navigation` | Navigation landmark (prefer `<nav>`) |
| `tablist` / `tab` / `tabpanel` | Tab interface |
| `menu` / `menuitem` | Dropdown command menus |
| `combobox` | Autocomplete / searchable select |
| `progressbar` | Progress indicators |
| `tooltip` | Supplementary hover/focus labels |
