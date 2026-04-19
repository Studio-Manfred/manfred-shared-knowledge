# Manfred Brand Guidelines

## Brand Thesis

**Business and human, at the same time.**

The two headline tokens — `business-blue` (`#2c28ec`) and `human-pink` (`#efd6d3`) — are not a color scheme. They are the brand's argument: that software can be serious enough to trust with real work and warm enough that the people using it feel seen. Manfred is built by and for people who don't want to choose between those two things.

## Brand Values

### Warmth

- Warm defaults over clinical ones. Soft off-black (`#1e1e24`) over pure black. Warm beige canvas over cold gray.
- UI copy reads like a person wrote it for a person.
- Empty states welcome rather than scold.

### Precision

- Language is exact. Tokens are explicit. Spacing is on a scale.
- Nothing lands in a component "because it looks right" — it lands because a token says so.
- Every variant earns its place. If it isn't being used, it doesn't ship.

### Accessibility as Baseline

- Not a compliance line item. A core brand value.
- WCAG 2.2 AA minimum, AAA where practical. Tested with keyboard and screen readers, not just axe.
- Contrast, focus, motion preferences, keyboard navigation — non-negotiable.

### Honesty

- Say what the software does. Don't dress it up.
- "Save changes" beats "Submit." "You're signed in as …" beats "Current user identity."
- Error messages explain and help. They never blame.

### Sustainability in the Small

- Light pages, small bundles, considered font loading.
- One typeface (Host Grotesk), bundled and subset where appropriate.
- Design for longevity — avoid trendy patterns that age in a year.

## Brand Voice

### Tone

- **Clear** — say what you mean.
- **Warm** — address the reader as a person, not a user record.
- **Confident** — no apology or hedging in routine copy.
- **Direct** — short sentences, active voice, verb-led.
- **Unflashy** — the product is the hero. Copy is the quiet shoulder-tap.

### Writing Principles

- Lead with the benefit to the reader.
- Plain language over jargon. Every time.
- Specific and actionable: "Save changes" not "Submit form data."
- Short sentences, short paragraphs.
- Inclusive language always — no gendered terms, no ableist metaphors, no cultural assumptions.
- Parity between Swedish and English where the product supports both.

### CTAs

- Action-oriented, short: "Get started," "Save," "Continue," "Send," "Try it."
- Never "Click here." Never "Submit."

### Errors

- What happened, what to do next, one clear action. In that order.
- "We couldn't save your changes — try again, or refresh the page if it keeps failing." Not "Error 500."

## Color Palette

Full token specification is in `~/.claude/shared/DESIGN.md`. Quick reference:

| Name | Token | Hex | Role |
|---|---|---|---|
| Almost Black | `--color-almost-black` | `#1e1e24` | Primary text, dark surfaces |
| Business Blue | `--color-business-blue` | `#2c28ec` | Brand primary, CTAs, links |
| Human Pink | `--color-human-pink` | `#efd6d3` | Warm accent surface |
| Beige | `--color-beige` | `#e6dcc8` | Neutral warm surface |
| Light Beige | `--color-light-beige` | `#f4f3e8` | Default warm background |
| White | `--color-white` | `#ffffff` | Default surface, inverse text |

### Color Philosophy

Blue leads, warm neutrals hold the room, pink is for moments of human emphasis. The palette is restrained so that content — not decoration — carries the weight. Named brand utilities (`bg-business-blue`, `bg-human-pink`, etc.) are literal primitives and **do not flip in dark mode**. Use semantic tokens (`bg-background`, `bg-primary`, etc.) for theme-aware styling.

## Typography

**Font:** Host Grotesk. **Logotype only:** Guttery (reserved for the Manfred mark; never used in UI).

Host Grotesk is a humanist sans-serif with geometric precision and warm apertures — the typographic version of the brand thesis. Scale runs from `xs` (12px) to `5xl` (56px). Weights: 300 / 400 / 500 / 600 / 700 / 800.

Full typographic scale and role mapping is in `DESIGN.md`.

## Layout & Atmosphere

- **Generous whitespace.** Sections breathe. The Nordic love of room applies.
- **Warm background rhythm.** Alternate `light-beige` canvas with `white` or `beige` cards. Avoid gray-on-gray layering — that's not Manfred's tonal range.
- **Flat first.** Depth is earned; heavy shadows and gradients don't belong here.

## Brand Strategy Context

Manfred is the design practice of Jens Wedin. The design system exists to codify how Manfred-made software looks and behaves so that everything shipped under the name is recognizable, consistent, and accessible — without every new project reinventing basics.

### Audiences

- **Teams adopting the system** — other engineers, other studios, products that want the Manfred look without rebuilding it. They get: tokens, components, and a short path from `npm install` to shipping.
- **People using the software** — the actual end users of products built on this system. They get: fast, legible, accessible, warm interfaces.

Both audiences get equal weight. A system that's lovely to build with but poor for end users is a failure. So is one that's great for end users but impossible for teams to adopt.

### Research & Evolution

The brand is young and will evolve as it gets used in more contexts. Versioned, additive changes through the design system repo. Breaking changes announced in the CHANGELOG with migration notes (see the `v0.1.x → v0.2.0` shadcn-shapes migration as the template).

## Quick Reference

- **Full design system spec:** `~/.claude/shared/DESIGN.md`
- **Decision framework:** `~/.claude/shared/design-principles.md`
- **Source of truth (code + Storybook):** `github.com/jens-wedin/manfred-design_system`
- **Distributed package:** `@jens-wedin/design-system`
