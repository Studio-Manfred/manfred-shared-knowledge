---
name: micro-interaction-spec
description: Use when specifying a single micro-interaction — anyone says "spec the toggle behaviour", "design the like animation", "what happens when the user taps the heart", "trigger / rules / feedback / loops", "micro-interaction", "button press feedback", "swipe-to-action spec". Manfred-flavoured: every micro-interaction has a stated purpose; reduced-motion fallback non-negotiable; durations from tokens.
---

# micro-interaction-spec

A micro-interaction is one moment: one trigger, one piece of feedback, one outcome. The toggle that flips. The heart that fills. The button that depresses. They're tiny — but they're where the interface either feels alive or feels dead.

This skill specifies *one* micro-interaction at a time using Dan Saffer's frame: **trigger → rules → feedback → loops/modes**. It's the unit of execution; bigger flows live in `/manfred-interaction-design:design-interaction`.

Manfred defaults:

- **Stated purpose.** Every micro-interaction answers: what does this signal? If the answer is "looks nice", it doesn't ship.
- **Tokens for durations + easings.** Inline values are token leaks.
- **Reduced-motion fallback.** Mandatory.
- **One purpose per interaction.** A button press is *not* the place to also play a sound, animate a colour change, *and* trigger a confetti burst.

## When to use

- Specifying a single, isolated interaction (toggle, button, like, swipe-to-archive, pull-to-refresh)
- Documenting an existing interaction so engineering can build it
- Reviewing an interaction that "feels off"
- Pairing with `manfred-interaction-design:animation-principles` for the motion spec inside this frame

**Skip when:**

- The user wants the *whole flow* (e.g. checkout) — that's `/manfred-interaction-design:design-interaction`
- The user wants the underlying state model — that's `manfred-interaction-design:state-machine`
- The user wants gesture conflict resolution at the screen level — that's `manfred-interaction-design:gesture-patterns`

## The frame (Saffer's four parts)

| Part | What it answers |
|---|---|
| **Trigger** | What initiates the interaction. User action, system event, or condition. |
| **Rules** | What happens once triggered. The logic, sequence, branching. |
| **Feedback** | How the user perceives the result. Visual, motion, audio, haptic. |
| **Loops + modes** | Does it repeat? Does it change with frequency? First-use vs repeat behaviour. |

Use the template below — fill every field.

## The template

```markdown
## Micro-interaction: <name>

### 1. Purpose
<One sentence: what does this signal to the user? If you can't write one, cut the interaction.>

### 2. Trigger
- **What**: <user click / hover / swipe / system event / condition>
- **Where**: <which element, which surface>
- **Active when**: <enabled state — what blocks this trigger>

### 3. Rules
- **Sequence**: <what happens, in order>
- **Branching**: <conditions that change the outcome>
- **Timing**: <delays, debounces, thresholds>
- **State change**: <what state transition this represents — see `manfred-interaction-design:state-machine`>

### 4. Feedback
- **Visual**: <colour, scale, position change — durations + easings from tokens>
- **Motion**: <animation type, duration, easing — see `manfred-interaction-design:animation-principles`>
- **Audio**: <if any — almost never in web>
- **Haptic**: <if any — native mobile only>
- **Surface for system feedback**: <inline / toast / banner — see `manfred-interaction-design:feedback-patterns`>
- **Copy** (if any): <route via `manfred-toolkit:ux-writing` — name the surface, don't write the words here>

### 5. Loops + modes
- **First-use**: <coachmark, peek, hint?>
- **Repeat behaviour**: <does it change after first use? become silent?>
- **Rate / debounce**: <can the user fire it 10x/sec? what limits exist?>
- **Termination**: <when does the interaction end?>

### 6. Accessibility
- **Keyboard equivalent**: <required>
- **Screen-reader announcement**: <`aria-live`, `aria-pressed`, etc>
- **Reduced-motion fallback**: <required for any animation; describe>
- **Touch target**: <≥ 44 × 44px>

### 7. Performance
- **Animated properties**: <should be transform / opacity; flag layout properties>
- **Repeats / loops**: <CPU / battery cost if continuous>

### 8. Failure mode
- **What if the action fails?**: <route to `manfred-interaction-design:error-handling-ux`>
- **What if the user cancels mid-interaction?**: <return to start state cleanly>
```

## Common micro-interactions + key decisions

| Interaction | Trigger | Key feedback | Common pitfall |
|---|---|---|---|
| **Toggle** | Tap | Position + colour change, 100–150ms | Animating colour but not position — confusing |
| **Like / favourite** | Tap | Fill + brief scale pulse | Confetti burst — overkill outside social-app context |
| **Swipe to archive** | Horizontal swipe | Reveal action background; threshold snap | No visual hint that swipe is available |
| **Pull-to-refresh** | Vertical pull on list top | Resistance, snap, spinner | Activation distance too short; fires accidentally |
| **Long-press for menu** | 500ms press, no movement | Subtle visual at 200ms (so user knows it's working), menu at 500ms | No 200ms "I see your press" feedback |
| **Button press** | Click / tap | Scale or depth response, 50–100ms | No visible response — feels broken |
| **Form validation (inline)** | Blur or input change | Inline icon + text below field | Validation that fires on every keystroke; too noisy |

## What NOT to do

- **Don't combine four feedback channels.** A button press doesn't need scale + colour + sound + haptic. Pick one or two.
- **Don't put the copy in this spec.** Reference the surface and route to `manfred-toolkit:ux-writing`. Don't decide the words here.
- **Don't skip the reduced-motion fallback.** Ship-blocker.
- **Don't lock input during the animation.** Interruptible by default.

## Red flags — STOP

- No stated purpose for the interaction.
- No reduced-motion fallback.
- Inline duration / easing values instead of tokens.
- Copy written into the spec instead of routed to ux-writing.
- Multiple competing feedback channels for one trigger (visual + audio + haptic + colour pulse).
- No keyboard / screen-reader equivalent.

## Manfred lens

Skip Cagan / Torres — micro-interactions are execution craft. Exception: if the interaction is the *primary* affordance for a critical action (e.g. swipe-to-pay) and isn't discoverable, that's a **usability risk** — flag and route to `manfred-discovery:cagan-risks`.

## Cross-references

- `manfred-interaction-design:animation-principles` — for the motion spec inside the feedback frame
- `manfred-interaction-design:state-machine` — for the state transition this interaction represents
- `manfred-interaction-design:feedback-patterns` — for system-level feedback channel choice
- `manfred-interaction-design:error-handling-ux` — for the failure-mode path
- `manfred-interaction-design:gesture-patterns` — when the trigger is a gesture
- `manfred-toolkit:ux-writing` — for any visible copy
- `manfred-design-systems:design-token` — for duration + easing tokens
- `manfred-design-systems:a11y-qa` — for keyboard + screen-reader + reduced-motion verification

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, copy-routing rule, and Manfred-specific guidance are original.*
