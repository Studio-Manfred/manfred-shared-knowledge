# Screen Reader Only Content

Visually hidden text that provides context obvious to sighted users but missing from the DOM.

## Tailwind

```tsx
<span className="sr-only">Opens in new tab</span>
```

## Plain CSS equivalent

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

## Common uses

- Clarify link destinations: `<a href="/reports">Download <span className="sr-only">annual report PDF</span></a>`
- Supplement icon button purpose
- Provide table captions
- Announce loading states: `<span className="sr-only">Loading, please wait</span>`
