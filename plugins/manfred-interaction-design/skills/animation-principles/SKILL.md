---
name: animation-principles
description: Use when designing UI motion — anyone says "add an animation", "what easing", "how long should this transition be", "page transition", "hover animation", "stagger this list", "feels janky", "respect reduced motion", "motion design". Manfred-flavoured: motion has a cost (sustainability principle); `prefers-reduced-motion` is non-negotiable; tokens before raw values.
---

# animation-principles

Motion in Manfred work is functional. It signals state, guides attention, smooths a transition that would otherwise jar. It is not decoration, and it is not how confidence is shown — confidence is shown by the words and the layout, not by a 600ms bounce.

Two non-negotiables:

1. **`prefers-reduced-motion: reduce` is honoured.** Every animation has a reduced-motion fallback. Not an opacity tween "instead of" a spring — a real fallback that achieves the same communicative purpose without the motion.
2. **Motion has a cost.** Frames, JS, battery, attention. Sustainability principle (`shared/design-principles.md` principle 13) says don't ship motion you can't justify.

## When to use

- Specifying a single animation (entrance, exit, emphasis, transition)
- Choosing duration / easing / stagger for a sequence
- Reviewing an existing animation that "feels off"
- Pairing with `manfred-interaction-design:micro-interaction-spec` for the full trigger → rules → feedback spec
- Pairing with `manfred-interaction-design:state-machine` for transition animations between states

**Skip when:**

- The user wants a brand identity motion system — that's brand work, not interaction work
- The user wants a marketing-site hero animation that's pure decoration — the answer is usually "don't"
- The user wants Lottie / After Effects illustration animation — refer to `manfred-ui-design:illustration-style`

## The hard rules

| Rule | What it means |
|---|---|
| **Reduced motion fallback** | Every animation block ships with a `@media (prefers-reduced-motion: reduce)` rule. Fallback achieves the same purpose (signal state change, draw attention) without the motion. Default is "transition: none" only when motion was decorative. |
| **Tokens before raw values** | If the design system defines duration / easing tokens (`--duration-fast`, `--ease-out-quart`), use them. Inline `300ms cubic-bezier(0.4, 0, 0.2, 1)` is a token leak. |
| **Sub-400ms by default** | UI animations under 400ms feel responsive. Over 400ms feels deliberate (good for choreographed sequences) or sluggish (bad for everything else). |
| **Purposeful** | Every animation answers: what state change does this signal? If the answer is "it looks nice", cut it. |
| **Interruptible** | The user can cancel mid-flight. Animations that lock input are bugs. |
| **Performance budget** | Animate `transform` and `opacity`. Animating `width` / `height` / `top` / `left` triggers layout — refuse unless functionally required (and then test on a low-powered device). |

## The flow

### Step 1 — Name the purpose

Before picking a duration, answer:

- **What state changed?** (Idle → loading; closed → open; absent → present.)
- **Where should attention land after the change?** (The new state, the next action, nothing.)
- **What would happen if there were no animation?** (If "nothing", the animation is decorative — cut.)

### Step 2 — Pick duration + easing

| Purpose | Duration | Easing |
|---|---|---|
| Button / toggle state | 50–150ms | ease-out |
| Tooltip, small fade | 150–250ms | ease-out |
| Modal, drawer, page transition | 250–400ms | ease-in-out |
| Emphasis (pulse, attention pull) | 200–300ms (× 1–2 cycles max) | ease-in-out |
| Choreographed sequence | up to 700ms total | varies; lead element ease-out, followers ease-in-out |
| Continuous (progress bar, loader) | n/a | linear |

If the design system has tokens for these — use them. If not, flag for `manfred-design-systems:design-token` to add motion tokens.

### Step 3 — Stagger / choreography (if multiple elements)

- Stagger 30–50ms between related items.
- Lead with the most important element (the one whose appearance signals the state change).
- Cap total sequence at 700ms — anything longer is a slideshow, not a transition.
- Use consistent direction (everything slides up, or everything fades — don't mix).

### Step 4 — Reduced-motion fallback

Mandatory. For every animation:

```css
.modal-enter {
  animation: slide-up 250ms ease-out;
}

@media (prefers-reduced-motion: reduce) {
  .modal-enter {
    animation: fade-in 100ms linear;
    /* or: animation: none; if the appearance itself is sufficient */
  }
}
```

The fallback's job is to preserve the *signal*, not the motion. If the modal needs to communicate "this is new", a fast fade does that without the slide.

### Step 5 — Performance check

- Are you animating `transform` / `opacity`? Good.
- Are you animating layout properties (`width`, `height`, `top`, `left`, `margin`)? Refuse unless functionally required. Test on a throttled CPU before shipping.
- Does the sequence fire on an event the user can repeat fast (scroll, hover)? Add a debounce or ensure idempotency.

### Step 6 — Sustainability check

Manfred design principle 13 (performance is a feature). Ask:

- Does this animation play on every page load? What's the JS / CSS cost?
- Does it run continuously (loop)? What's the CPU / battery cost?
- Is it a Lottie / animated SVG > 50KB? Justify, or simplify.

If you can't justify the cost in design-review, cut it.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "It feels more polished with the animation." | Polish is a layout / typography / copy problem first. Motion-as-polish is usually motion-as-distraction. |
| "Reduced-motion users are < 1%." | They're disproportionately people who'll bounce off a vestibular trigger. Also legally relevant (WCAG 2.3.3). |
| "Just use the default browser easing." | The default linear easing is wrong for almost every UI animation. Pick one. |
| "I'll add the reduced-motion fallback later." | Later doesn't happen. Fallback ships with the animation or the animation doesn't ship. |
| "It's only 600ms — that's not slow." | It's 600ms × every transition × every user. Tighten by default. |

## Red flags — STOP

- Animating layout properties (width / height / top / left) without a performance test.
- No reduced-motion fallback in the spec.
- Duration > 400ms for a non-choreographed animation.
- Stagger longer than 700ms total.
- Animation purpose is "looks nice" with no state-change justification.

## Manfred lens

Where does this skill fit Cagan / Torres? It usually doesn't — animation is execution-craft, not discovery. Skip the lens. The exception: if a motion choice changes feasibility (e.g., 60fps animation that won't run on the target device), flag the **feasibility risk** and route to `manfred-discovery:cagan-risks`.

## Cross-references

- `manfred-interaction-design:micro-interaction-spec` — fold animation into the fuller trigger/rules/feedback spec
- `manfred-interaction-design:state-machine` — animations attach to transitions, not states
- `manfred-interaction-design:loading-states` — loading shimmer / skeleton animations live there
- `manfred-design-systems:design-token` — duration / easing tokens
- `manfred-design-systems:a11y-design` + `manfred-design-systems:a11y-qa` — reduced-motion verification
- `manfred-ui-design:illustration-style` — for Lottie / animated illustration

## Tools used

- `Read` — to inspect existing token definitions
- `Bash` (`grep`) — to find existing animation patterns in the codebase

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, Manfred-specific guidance, and reduced-motion / sustainability rules are original.*
