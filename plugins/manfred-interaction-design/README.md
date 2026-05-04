# manfred-interaction-design

Manfred-flavoured interaction design: animation, feedback, gestures, loading, micro-interactions, state machines, error-handling UX. Errors explain don't blame; motion respects `prefers-reduced-motion`; sustainability in the small (animation has a cost). Defers copy generation to `manfred-toolkit:ux-writing`.

## Skills

| Skill | When it triggers |
|-------|-----------------|
| `animation-principles` | "add an animation", "what easing", "how long should this transition", "page transition", "stagger", "feels janky", "respect reduced motion" — purposeful motion, sub-400ms default, reduced-motion fallback non-negotiable, tokens before raw values |
| `error-handling-ux` | "design the error flow", "API timeout UX", "what error do we show", "retry behaviour", "explain don't blame", "just generate the error copy", "Oops!", "Something went wrong", "we can iterate later" — **foundational TDD'd skill**: refuses copy without four pre-flight answers (failure mode + surface + recovery + user state); routes copy to `manfred-toolkit:ux-writing`; (a)/(b)/(c) menu when context missing; (c) requires Linear ticket + code TODO + worst-case design |
| `feedback-patterns` | "design a toast", "success message", "what kind of notification", "inline validation", "snackbar", "feedback after submit" — closer-to-action wins; undo > "Are you sure?"; copy via `manfred-toolkit:ux-writing` |
| `gesture-patterns` | "swipe to dismiss", "drag-to-reorder", "long-press menu", "pull to refresh", "pinch to zoom", "iOS / Android gesture parity" — every gesture has a non-gesture alternative (a11y non-negotiable); platform conventions first; visible affordances |
| `loading-states` | "loading state", "skeleton", "spinner", "blank screen", "feels slow", "optimistic UI", "perceived performance", "shimmer" — never a blank screen; skeleton matches real layout; reduced-motion fallback for shimmer; copy via `manfred-toolkit:ux-writing` |
| `micro-interaction-spec` | "spec the toggle behaviour", "design the like animation", "trigger / rules / feedback / loops", "button press feedback" — Saffer's frame; every interaction has stated purpose; tokens for durations |
| `state-machine` | "model the states", "state diagram", "finite state machine", "XState", "impossible states", "wizard flow", "form state model" — discriminated unions over boolean soup; every state has a way out; entry/exit actions explicit |

## Commands

| Command | What it does |
|---------|--------------|
| `/manfred-interaction-design:design-interaction` | Design a complete interaction flow end-to-end. Chains state-machine → micro-interactions → animation → gestures → feedback → error → loading. |
| `/manfred-interaction-design:error-flow` | Design the full error UX for a feature. Inventory failure modes → prevention → state model → recovery → copy handoff to `manfred-toolkit:ux-writing`. |
| `/manfred-interaction-design:map-states` | Model the states + transitions for a complex component or flow. Verifies impossible states; chains loading + error + feedback + animation per state. |

## Manfred opinions baked in

- **Errors explain, don't blame** — `error-handling-ux` enforces the brand error rule (`shared/manfred-brand.md`); refuses generic-SaaS-friendly copy; routes to `manfred-toolkit:ux-writing`
- **Reduced motion is non-negotiable** — every animated skill mandates a `prefers-reduced-motion: reduce` fallback (WCAG 2.3.3)
- **Sustainability in the small (principle 13)** — motion / loading skills note CPU / battery / bundle cost
- **Tokens, not raw values** — durations / easings reference `manfred-design-systems:design-token`; flag inline values as token leaks
- **Undo > confirmation** — `feedback-patterns` defaults to undo; confirmation reserved for genuinely-irreversible actions
- **Platform conventions first** — `gesture-patterns` follows iOS / Android HIG; custom gestures need a stated reason
- **State preservation is non-negotiable** — `error-handling-ux` requires form values, multi-step progress, scroll position to survive errors
- **Copy lives in `manfred-toolkit:ux-writing`** — interaction skills design *flow*; words live in the toolkit. Generic "Something went wrong" is the failure mode this plugin exists to prevent.

## Cross-plugin handoffs

- **Routes copy to `manfred-toolkit:ux-writing`** — error messages, loading copy, toast text, button labels — the words are always written there with structured context from here
- **Built on `manfred-design-systems:design-token`** — duration / easing / motion tokens
- **Pairs with `manfred-design-systems:a11y-design` + `manfred-design-systems:a11y-qa`** — ARIA patterns, focus management, reduced-motion, keyboard equivalents
- **Built on `manfred-ui-design`** — visual surface for the interaction lives there
- **Feeds `manfred-design-ops:handoff-spec`** — interaction specs become engineering handoffs
- **Surfaces `manfred-discovery:cagan-risks`** — when error UX or interaction friction is on a critical revenue / retention path

## Install

```
/plugin marketplace add Studio-Manfred/manfred-shared-knowledge
/plugin install manfred-interaction-design@manfred
```
