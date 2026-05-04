---
name: gesture-patterns
description: Use when designing touch / pointer interactions — anyone says "swipe to dismiss", "drag-to-reorder", "long-press menu", "pull to refresh", "pinch to zoom", "gesture-based navigation", "iOS / Android gesture parity". Manfred-flavoured: every gesture has a non-gesture alternative (a11y non-negotiable); follow platform conventions; gestures need visible affordances.
---

# gesture-patterns

Gestures are powerful when they match user expectations and visible when they're new. They're hostile when they're hidden, custom for the sake of being custom, or the only way to do something.

Manfred's defaults:

- **Every gesture has a non-gesture alternative.** Button, menu, keyboard shortcut — pick one. Without it the gesture is an accessibility wall.
- **Follow platform conventions.** iOS users know iOS gestures. Android users know Android gestures. Custom gestures need a very good reason.
- **Affordances make gestures discoverable.** A draggable handle, a swipe hint on first use, a "drag" cursor — without these, the gesture is a puzzle.

## When to use

- Specifying a single gesture (swipe, drag, long-press, pull-to-refresh)
- Resolving conflicts between gestures (scroll vs swipe; tap vs long-press)
- Reviewing a gesture-heavy interaction for discoverability + accessibility
- Pairing with `manfred-interaction-design:micro-interaction-spec` for the full spec

**Skip when:**

- You're designing for desktop-only with mouse + keyboard — gestures are touch-first; for desktop, see `manfred-interaction-design:micro-interaction-spec`
- You're specifying VoiceOver / TalkBack rotors — that's `manfred-design-systems:a11y-design` territory
- The product doesn't ship a touch target (admin tool, B2B desktop dashboard) — defer

## The hard rules

| Rule | What it means |
|---|---|
| **Non-gesture alternative mandatory** | Every gesture must have a button / menu / keyboard equivalent. WCAG 2.5.1 (pointer gestures). |
| **Platform conventions first** | If iOS / Android already has a gesture for this, use it. Custom gestures need a stated reason. |
| **Visible affordance** | Drag handles, swipe hints, peek-reveal animations on first use. Hidden gestures are bugs disguised as features. |
| **System gestures take priority** | Don't intercept iOS back-swipe, Android edge-swipe, browser back-swipe, OS notification pull. |
| **Cancellable** | Returning to start position aborts the gesture. The user can change their mind. |
| **No precision-timing required** | Gestures that need 250ms-precise input fail for users with motor impairments. Generous thresholds. |

## Core gestures + intended meaning

| Gesture | Default meaning | Notes |
|---|---|---|
| Tap | Select, activate, toggle | The default. Always works. |
| Double-tap | Zoom (maps, images), like (social) | Slow-tap users miss this — pair with single-tap alternative |
| Long-press | Context menu, reorder mode, preview | 500ms threshold; visual feedback at 200ms so users know it's working |
| Swipe | Navigate (page change), dismiss (item from list), reveal (action drawer) | Direction-locks after first 10–15px |
| Pinch / spread | Zoom | Only on zoomable surfaces (image viewer, map). Don't intercept on scrollable lists. |
| Drag | Move, reorder, adjust value (slider) | Always with a visible handle |
| Pull-to-refresh | Reload list content | Only on lists where reload makes sense. Show a non-pull refresh button too. |

## Conflict resolution

| Conflict | Resolution |
|---|---|
| Scroll vs swipe-to-action | Direction-lock after 10–15px in the dominant axis. If horizontal first, it's a swipe; if vertical first, it's a scroll. |
| Tap vs long-press | 500ms threshold. Tap fires on `pointerup` if duration < 500ms; long-press fires on duration ≥ 500ms with no movement > 8px. |
| Pinch vs drag | Number of pointers — 1 is drag, 2 is pinch. |
| Browser back-swipe vs in-app swipe | Don't intercept system gestures within 20px of edges. |

## Thresholds (defaults to start with — measure on real users)

- **Activation distance**: 10–15px before a swipe is recognised
- **Velocity threshold**: 0.3 px/ms for a "flick" (vs slow drag)
- **Long-press duration**: 500ms
- **Cancel zone**: returning within 20px of start aborts
- **Touch target size**: 44 × 44px minimum (iOS HIG / WCAG 2.5.5)

## Discoverability

Hidden gestures get used by 5% of users. Visible gestures get used by 80%. Make them visible:

- **First-use coachmark** — a one-time hint ("swipe down for filters") that dismisses on first use.
- **Persistent affordance** — drag handles, swipe arrows, peek-reveal on the first item of a list.
- **Animation hint** — a subtle bounce / shimmer on first load to suggest "this can be swiped".
- **Inline help** — discoverable via a (?) icon, not a popup.

If the gesture has no affordance and no coachmark, it doesn't exist for most of your users.

## Accessibility

- Switch control + voice control must be able to trigger every gesture's alternative.
- VoiceOver / TalkBack: announce the gesture availability ("Long-press for options").
- `prefers-reduced-motion`: gesture animations (rubber-band, snap-back) honour the preference.
- Gesture cancel zone must be large enough for users with tremor or low motor control.

Verify with `manfred-design-systems:a11y-qa`.

## Specifying a gesture

Use this template:

```markdown
## Gesture: <name>

**Trigger**: <swipe / long-press / drag / pull / etc>
**Direction**: <horizontal / vertical / radial / n/a>
**Activation threshold**: <distance / time / velocity>
**Affordance**: <what the user sees that suggests this gesture exists>
**Non-gesture alternative**: <button / menu / keyboard shortcut>
**Conflict with**: <scroll? other gestures? system gestures?>
**Cancel behaviour**: <how the user aborts mid-gesture>
**Reduced-motion fallback**: <what changes for `prefers-reduced-motion: reduce`>
**Accessibility announcement**: <VoiceOver / TalkBack hint>
```

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Power users will discover it." | Power users represent 5% of your audience. The other 95% will hit the wall and bounce. |
| "It's intuitive." | "Intuitive" means "matches a convention you already know". Verify it matches the platform convention or explicitly teach it. |
| "We don't need a button — the gesture is enough." | The gesture-only path fails switch users, voice users, motor-impaired users, and the WCAG audit. |
| "Custom gesture is on-brand." | Brand lives in copy, layout, motion timing — not in custom gestures. Custom gestures cost users the muscle memory they brought from other apps. |

## Red flags — STOP

- Gesture with no non-gesture alternative.
- Gesture that intercepts a system gesture (browser back-swipe, OS notification pull).
- Custom gesture replacing a platform-conventional one with no stated reason.
- Long-press as the *only* way to access a destructive action.
- Touch target < 44 × 44px.

## Manfred lens

Usually skip — gesture design is execution craft. Exception: if a gesture-heavy flow risks adoption (especially on platforms where users don't expect that gesture), surface as **usability risk** and route to `manfred-discovery:cagan-risks`.

## Cross-references

- `manfred-interaction-design:micro-interaction-spec` — fold the gesture into a full trigger / rules / feedback spec
- `manfred-interaction-design:animation-principles` — for rubber-band, snap-back, and gesture-feedback animations
- `manfred-design-systems:a11y-design` + `manfred-design-systems:a11y-qa` — for switch / voice / VoiceOver verification
- `manfred-toolkit:ux-writing` — for the coachmark / affordance copy

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, accessibility-first framing, and Manfred-specific guidance are original.*
