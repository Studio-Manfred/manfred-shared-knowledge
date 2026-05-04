---
name: responsive-design
description: Use when designing or auditing responsive behaviour — anyone says "responsive", "mobile design", "make this work on mobile", "breakpoint behaviour", "tablet layout", "responsive audit", "mobile first", "screen size", "viewport". Manfred-flavoured: mobile-first (principle 12); designed for content not devices; tested at 320/768/1024/1440 minimum.
---

# responsive-design

Responsive isn't an afterthought layer on top of desktop design — it's the starting position. Manfred designs for the smallest screen first, then expands. Every interactive surface gets tested at 320px before any larger breakpoint is considered.

For the static grid system (columns, gutters, container widths), use `manfred-ui-design:layout-grid`. This skill is the dynamic-behaviour layer on top.

## Overview

Four responsive strategies — pick by what the content needs:

| Strategy | When | Example |
|---|---|---|
| **Fluid** | Content scales smoothly; layout doesn't change shape | `max-w-7xl mx-auto` with content reflowing |
| **Adaptive** | Distinct layouts at specific breakpoints | Sidebar appears at `lg:` and not before |
| **Mobile-first** | Build smallest first, enhance upward | Tailwind defaults are mobile; `md:` / `lg:` enhance |
| **Content-first** | Let content needs drive breakpoints, not device assumptions | Custom breakpoint where the line-length gets uncomfortable |

Manfred default is **mobile-first** + **content-first**: design the smallest version first, add complexity at the breakpoints where the content actually needs more room.

## When to use

- Designing a new feature or page across breakpoints
- Auditing an existing surface for responsive issues
- Picking a responsive strategy for a specific component
- Adapting a desktop-first design to be mobile-first
- Reviewing whether a "responsive" design actually works on real devices

**Skip when:**

- The work is the static grid (use `manfred-ui-design:layout-grid`)
- The work is component-internal (use `manfred-design-systems:component-spec`)
- The work is dark-mode behaviour (use `manfred-ui-design:dark-mode-design`)
- The work is touch vs pointer interaction (use `manfred-interaction-design` when shipped)

## Pre-flight

Identify:

- **What's the smallest viewport?** Manfred default: 320px. Some products need 360px. Check the product.
- **What devices are in scope?** iOS / Android phones, tablets, laptops, desktops, large displays.
- **What input methods?** Touch, mouse, keyboard, voice, screen reader.
- **What network?** Some users on slow connections — performance matters as much as layout.
- **Existing breakpoints in the project?** Tailwind defaults vs project overrides.

## The hard rules

| Rule | What it means |
|---|---|
| **Mobile-first** (principle 12) | Design and implement smallest first, enhance upward. Tailwind utilities are mobile by default; `md:`/`lg:` add. |
| **Test at every breakpoint, not the extremes** | 320, 768, 1024, 1440 minimum. Issues hide in the middle (e.g. ugly at 980px even if both 320 and 1280 work). |
| **Touch targets ≥ 44px on mobile** | Per principle 12 + WCAG 2.5.8. Tap targets smaller than this fail on mobile. |
| **Test on real devices** | Browser resize is approximate. Touch behaviour, gesture support, viewport quirks (iOS Safari, Android Chrome) reveal issues only on devices. |
| **Account for slow connections** | Mobile users are often on bad networks. Performance budgets matter at every breakpoint (principle 13). |
| **Both orientations** | Portrait and landscape on phones + tablets. Don't assume orientation. |
| **Content-first breakpoints** | Add a breakpoint when the content needs it, not when a device size says so. |
| **Accessibility per breakpoint** | Run `manfred-design-systems:a11y-qa` at every breakpoint. Issues appear at one size and not others. |

## Manfred breakpoints

| Breakpoint | Range | Devices | Columns |
|---|---|---|---|
| Mobile | 320–639px | Phones | 4 |
| Tablet | 640–1023px | Tablets, small laptops | 8 |
| Desktop | 1024–1439px | Laptops | 12 |
| Wide | 1440px+ | Large displays, desktops | 12 (capped at `max-w-7xl`) |

(Tailwind: `sm 640px`, `md 768px`, `lg 1024px`, `xl 1280px`, `2xl 1536px` — adjust to fit project conventions.)

## Responsive patterns

### Column drop
Reduce columns at smaller sizes. 12 → 8 → 4.

```tsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  {items.map(item => <Card key={item.id} {...item} />)}
</div>
```

### Reflow
Stack horizontal elements vertically.

```tsx
<div className="flex flex-col md:flex-row gap-4">
  <Sidebar />
  <Main />
</div>
```

### Off-canvas
Hide secondary content behind a toggle on small screens.

```tsx
<>
  <button className="md:hidden" onClick={() => setNavOpen(true)}>Menu</button>
  <Sheet open={navOpen} onOpenChange={setNavOpen} className="md:hidden">
    <Nav />
  </Sheet>
  <Nav className="hidden md:block" />
</>
```

### Priority+
Show most important; overflow the rest behind a "more" affordance.

```tsx
<nav className="flex gap-4">
  {visible.map(item => <NavLink key={item.id} {...item} />)}
  {overflow.length > 0 && <MoreMenu items={overflow} />}
</nav>
```

## Input method adaptation

| Input | What to design for |
|---|---|
| Touch | 44px minimum targets (WCAG 2.5.8); gesture support; no hover-only |
| Mouse | Hover states; precise targeting (24px minimum per WCAG 2.5.5) |
| Keyboard | Focus indicators visible; logical tab order; no keyboard traps |
| Voice | Clear labels; logical structure; accessible names |

Touch + mouse coexist on hybrid devices (laptop with touchscreen). Don't assume one or the other.

## Responsive typography + images

- **Fluid type scaling** — type sizes scale between breakpoints, not just at them. Use Tailwind's `text-base lg:text-lg` or CSS `clamp()` for true fluid scaling.
- **Responsive images** — `srcset` + `sizes` for resolution; `<picture>` for art direction (different crops per breakpoint).
- **Don't ship desktop-sized images to mobile** — bandwidth + render performance both suffer.

## Responsive audit checklist

When auditing a design:

- [ ] Renders at 320px without horizontal scroll
- [ ] Renders at 360px (common Android)
- [ ] Renders at 768px (tablet portrait)
- [ ] Renders at 1024px (tablet landscape / small laptop)
- [ ] Renders at 1440px (desktop)
- [ ] Text remains readable at every breakpoint (16px minimum body)
- [ ] Touch targets ≥ 44px on mobile
- [ ] Focus indicators visible at every breakpoint
- [ ] Off-canvas / collapsed nav works on mobile
- [ ] Images scale appropriately per breakpoint
- [ ] No hover-only interactions
- [ ] Both orientations work (portrait + landscape)
- [ ] Tested on at least one real iOS + one real Android device
- [ ] `manfred-design-systems:a11y-qa` passes at every breakpoint

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Desktop-first is faster — most users are desktop" | Manfred users are increasingly mobile. Mobile-first means designing for the harder constraint first; desktop is an enhancement. |
| "Browser resize is good enough for testing" | It catches layout but misses touch behaviour, gesture quirks, viewport metadata, performance. Test on real devices. |
| "We'll add mobile after launch" | Mobile is the launch. Adding mobile after means reskinning every component. |
| "Tablet's the same as desktop with smaller text" | Tablet (768–1023) needs its own thinking — usually 8 cols, not 4 or 12. Touch + larger screen + portrait/landscape. |
| "Hover for mobile is fine — we'll just trigger on tap" | Tap-to-trigger-hover is confusing. Design for the touch model directly. |
| "44px touch targets are too big — looks sloppy" | They aren't sloppy when designed in. WCAG 2.5.8 floor is 24px; recommended 44px. The thumb doesn't shrink. |

## Red flags — STOP

- About to design a feature without confirming the smallest viewport
- About to ship without testing 320 / 768 / 1024 / 1440px
- About to use hover-only interactions
- About to use touch targets <44px on mobile
- About to ship without testing on a real device
- About to design tablet as "small desktop" without an 8-col step
- About to skip the responsive a11y audit (issues hide at specific breakpoints)

## Manfred lens

Responsive design touches **usability** at every breakpoint. It also touches **accessibility** (touch targets, focus visibility), **performance** (mobile networks), and **principle 12 (mobile first, responsive always)** — the explicit Manfred commitment.

Critical & ethical (principle 6): designs that work poorly on mobile exclude users who only have phones. In some markets that's the majority. Mobile-first isn't aesthetic preference; it's accessibility.

## Cross-references

- `~/.claude/shared/DESIGN.md` Section 5 (Layout Principles)
- `~/.claude/shared/design-principles.md` principles 12, 13, 5
- `manfred-ui-design:layout-grid` — static grid; this skill is the dynamic behaviour
- `manfred-ui-design:dark-mode-design` — runs across breakpoints too
- `manfred-design-systems:a11y-qa` — runtime gate per breakpoint
- `manfred-design-systems:a11y-design` — design-stage annotation per breakpoint

## Tools used

- `Read` — `~/.claude/shared/DESIGN.md`, project's `tailwind.config`
- `Bash` — browser dev tools for responsive testing
- `manfred-design-systems:a11y-qa` — runtime audit per breakpoint
- `manfred-ui-design:layout-grid` — static grid foundation

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
