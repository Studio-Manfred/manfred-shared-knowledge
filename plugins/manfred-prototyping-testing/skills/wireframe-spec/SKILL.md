---
name: wireframe-spec
description: Use when specifying a wireframe / annotated layout — anyone says "wireframe spec", "low-fi", "mid-fi", "annotated wireframe", "layout spec", "what goes on this page", "content priority", "skeleton layout", "wire-flow". Manfred-flavoured: greyscale only (no color decisions at wireframe stage); content priority numbered; states (empty / loading / populated / error) all spec'd; responsive breakpoint versions included; tokens for spacing not pixel values.
---

# wireframe-spec

A wireframe is the layout argument before the visual argument. It defines what's on the page, what comes first, what behaviour each element has, and how it responds. It is *not* a colour palette, a typography decision, or a brand expression — those are downstream decisions that change without invalidating the wireframe.

Manfred defaults:

- **Greyscale only.** Wireframes that include colour decisions are visual designs in disguise. Defer colour to `manfred-ui-design:color-system` and the visual phase.
- **Content priority numbered.** What loads first / what the user sees first / what they should remember.
- **All meaningful states.** Empty, loading, populated, error. Wireframes that show only the populated state will ship with broken loading + empty + error states because nobody designed them.
- **Responsive breakpoints.** At least mobile (320–375px) and desktop. Tablet (768px) if the design changes meaningfully there.
- **Spacing in tokens, not pixels.** Reference `manfred-design-systems:design-token` units (e.g. `space-4`, `space-8`); flag if the design needs a token that doesn't exist.

## When to use

- Specifying a new screen's layout before visual design
- Annotating an existing layout for engineering hand-off
- Defining responsive behaviour across breakpoints
- Pairing with `manfred-prototyping-testing:user-flow-diagram` for wire-flow (flow + wireframe thumbnails)

**Skip when:**

- The work is already in high-fi visual design — go straight to `manfred-ui-design:design-screen`
- The work is component-level (button, card, modal in isolation) — that's `manfred-design-systems:component-spec`
- The work is the full interaction spec (motion, gestures) — that's `manfred-interaction-design:design-interaction`

## Wireframe components

### Content blocks

- Headers + navigation
- Hero / feature areas
- Content sections (text, media, cards, lists)
- Forms + input areas
- Footers + secondary navigation
- Sidebars / contextual panels

### States

| State | Why it must be spec'd |
|---|---|
| **Empty (first-load, no data)** | Often the user's first impression; wireframes that skip this ship with broken empty states |
| **Loading** | Pair with `manfred-interaction-design:loading-states` — skeleton matches real layout; never blank |
| **Populated (data present)** | The default state most wireframes only show |
| **Error** | What appears when content fails to load — see `manfred-interaction-design:error-handling-ux` |
| **Partial / degraded** | Some content present, some not (often where real users land) |

If the wireframe doesn't include all five — list what's missing and why.

### Annotations

- **Content priority numbers** — what loads / appears / the user notices first (1 = primary; 2 = secondary; 3 = tertiary)
- **Interaction notes** — what happens on click / hover / focus / swipe (route specifics to `manfred-interaction-design:micro-interaction-spec`)
- **Dynamic content indicators** — personalised, data-driven, A/B-test variant
- **Responsive behaviour** — what reflows / hides / stacks at each breakpoint
- **Accessibility notes** — heading hierarchy, landmark roles, focus order, AT-specific paths
- **Content source** — static / CMS / API / user-generated
- **Approximate text length** — character counts for headings, line counts for body
- **Image specs** — aspect ratio, sizing, alt-text guidance

## Fidelity levels

| Level | When | What's in / out |
|---|---|---|
| **Sketch** | Earliest exploration — paper, whiteboard | Hand-drawn boxes + labels; nothing pixel-perfect |
| **Low-fi** | Quick alignment on layout intent | Grey boxes, real labels, no real content; X-boxes for images |
| **Mid-fi** | Engineering preview, stakeholder review | Realistic placeholder content, real navigation labels, real headings; greyscale typography hierarchy |
| **Annotated mid-fi** | Engineering hand-off | Mid-fi + interaction / behaviour / responsive / a11y notes |

Don't skip levels. Going from sketch straight to annotated mid-fi means you're making layout decisions and visual-priority decisions and behaviour decisions all at once — and reviewing them all at once. Slow.

## Wireframe conventions

- **Greyscale only** — black, white, three or four greys. No brand colour decisions.
- **X-box for images** — rectangle with diagonal lines through corners
- **Wavy lines for placeholder body text** — but real labels for headings, navigation, buttons
- **Real navigation labels + button copy** — hand off the *content* even when the *visual* is undecided. Copy via `manfred-toolkit:ux-writing` once the wireframe stabilises.
- **Consistent component representation** — if "card" looks one way in section A, it looks the same way in section B
- **Spacing in token units** — `space-4` / `space-8` / `space-12` (referencing `manfred-design-systems:design-token`); flag missing tokens

## The flow

### Step 1 — Confirm scope + content

- **Page goal** — what's the one thing the user accomplishes here?
- **Content inventory** — what exists, what's API-driven, what's user-generated, what's static
- **Existing related screens** — does this page connect to / extend an existing pattern?
- **Linear ticket**

If content isn't ready (real copy, real data shapes), mark the wireframe as draft until it is. Wireframing on lorem ipsum is wireframing on the layout-of-lorem-ipsum.

### Step 2 — Establish layout grid

- Mobile-first (per principle 12) — start at 320–375px
- Use the project's grid (`manfred-ui-design:layout-grid`) — typically 12-col desktop / 8-col tablet / 4-col mobile
- Container widths + page margins
- Gutters from spacing tokens

### Step 3 — Place content blocks (mobile)

Mobile first — the constraints force priority. Then desktop, where real-estate is plentiful.

For each block:

- Position
- Size / proportion
- Content (real labels; placeholder body)
- Priority number (1 / 2 / 3)

### Step 4 — Annotate behaviour

For each interactive element:

- Trigger (click / hover / focus / swipe)
- Result (open modal / navigate / inline reveal / submit form)
- Disabled / loading / error state
- Routing pointer to `manfred-interaction-design:micro-interaction-spec` if motion / detailed feedback needed

### Step 5 — Responsive variants

For each meaningful breakpoint, show:

- What reflows (column count, stack direction, image aspect ratio)
- What hides (secondary content collapsed, sidebar moved to drawer)
- What changes order (mobile may put CTA above content; desktop may put it after)
- What changes size (typography scale, button size for touch)

If three breakpoints look identical, only spec one. If they diverge, spec each.

### Step 6 — All five states

Per page:

| State | Spec |
|---|---|
| Empty | What the user sees first time / when there's no data |
| Loading | Skeleton matching the populated layout (see `manfred-interaction-design:loading-states`) |
| Populated | The default — most attention here |
| Error | What appears on load failure (see `manfred-interaction-design:error-handling-ux`) |
| Partial | When some sections load and others fail / are empty |

### Step 7 — Accessibility annotations

- **Heading hierarchy** — H1 / H2 / H3 / H4 by level, no skipped levels
- **Landmark roles** — `<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>` (or ARIA equivalents)
- **Focus order** — does it match visual reading order?
- **AT-equivalent paths** — if the visual design has multiple ways to find X, do all paths exist for AT users?
- **Touch target sizes** — ≥ 44 × 44px for any interactive element

Pair with `manfred-design-systems:a11y-design` for the deeper review.

### Step 8 — Document + hand off

```markdown
# Wireframe spec — <screen name>

**Date**: YYYY-MM-DD
**Linear**: STU-XXX
**Fidelity**: <sketch / low-fi / mid-fi / annotated mid-fi>
**Page goal**: <one sentence>

## Content inventory
[List — static / CMS / API / user-generated]

## Layout
[Embedded wireframe or link]

## Content priority
[Numbered — what user notices first, second, third]

## States
[All five — wireframe per state]

## Responsive
[Per breakpoint — mobile / tablet / desktop]

## Annotations
- Behaviour
- Dynamic content
- Accessibility
- Content source

## Tokens referenced
[List spacing / type tokens used; flag missing tokens]

## Cross-plugin handoffs
- Visual design: `manfred-ui-design:design-screen`
- Components: `manfred-design-systems:component-spec`
- Interaction: `manfred-interaction-design:design-interaction`
- Copy: `manfred-toolkit:ux-writing`
- a11y: `manfred-design-systems:a11y-design`

## Open questions
[Decisions pending]
```

### Step 9 — Linear comment

Post via `mcp__linear-server__save_comment` with summary + path to spec.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Use lorem ipsum — content's not ready." | Wireframing on lorem produces layouts that don't fit real content. Use real (or close-to-real) content; mark draft. |
| "We can skip empty + error states for the spec." | Then engineering will ship them broken — nobody designed them. Spec all five states. |
| "Add some colour to make it readable." | Colour decisions belong in visual design. Greyscale forces the conversation about layout, not aesthetics. |
| "Mobile is just desktop scaled down." | Mobile-first per principle 12. Designing desktop first and shrinking produces broken mobile every time. |
| "Spacing as pixels — engineers will translate." | Use spacing tokens. Pixel values make engineering guess and produce drift. |
| "One responsive variant — engineering will figure out the rest." | Then they'll guess at the breakpoints. Spec the meaningful ones. |

## Red flags — STOP

- Wireframe with brand colours (it's a visual design in disguise)
- Lorem ipsum throughout (you're wireframing nothing)
- Only the populated state spec'd
- One breakpoint shown when design changes across breakpoints
- Spacing in pixels instead of tokens
- No interaction annotations on interactive elements
- No content priority numbers
- Heading hierarchy unclear / inconsistent

## Manfred lens

**Cagan's 4 risks** — wireframes are layout craft; usually skip the lens. Exception: when wireframing surfaces a flow / IA decision that's actually a **usability risk** (we're not sure users will scan in this order), route to `manfred-discovery:assumption-test` for a click test (`manfred-prototyping-testing:click-test-plan`).

## Cross-references

- `manfred-ui-design:design-screen` — for visual design after wireframe stabilises
- `manfred-ui-design:layout-grid` — for the underlying grid system
- `manfred-design-systems:component-spec` — for component-level detail inside the wireframe
- `manfred-design-systems:design-token` — for spacing + type tokens referenced
- `manfred-design-systems:a11y-design` — for the deeper a11y review
- `manfred-interaction-design:loading-states` — for the skeleton spec
- `manfred-interaction-design:error-handling-ux` — for the error-state spec
- `manfred-interaction-design:micro-interaction-spec` — for behaviour / motion details
- `manfred-toolkit:ux-writing` — for the copy that lands in the wireframe
- `manfred-prototyping-testing:user-flow-diagram` — for wire-flow (wireframes + flow together)

## Tools used

- Figma, Whimsical, Sketch — for the wireframes themselves
- `mcp__linear-server__get_issue` / `save_comment` — for ticket linkage

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, greyscale-only rule, all-five-states rule, mobile-first discipline, spacing-as-tokens rule, and Manfred-specific guidance are original.*
