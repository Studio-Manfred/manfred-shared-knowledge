# Design System: Manfred

> **Context:** This document specifies the Manfred design system — the shared component library and token set used by Manfred and its clients. For the studio itself (mission, services, team, voice), see `manfred-brand.md`. For the decision framework, see `design-principles.md`.

## 1. Visual Theme & Atmosphere

Manfred's visual language sits at the intersection of **business capability and human warmth**. The system carries two colors by name — `business-blue` and `human-pink` — and that pairing is not decorative: it encodes the studio's mission (building better product companies, making the product world more customer-driven) into the visual layer. Products built with this system should feel professional enough to earn trust in enterprise contexts, and warm enough that the people using them feel seen, not processed.

The visual direction favors **restraint and warmth over ornament**. Warm neutrals replace the cold grays of generic tech UI. Type is a single humanist sans-serif used at generous sizes with comfortable line-height. Color is reserved for action and meaning — the blue leads, the warm tones hold the room, and accents appear only when they signal intent.

**Core identity:** Business-ready, human-warm, accessible. A design system for teams that want their software to feel like it was made by people, for people — a visual expression of Manfred's mission to make the product world more customer-driven.

**Stack note:** The implementation ships as `@jens-wedin/design-system` — Tailwind CSS v4 + Radix UI + shadcn-shaped component APIs. The token layer is what keeps the brand coherent; the component layer is thin glue over proven primitives.

**Key adjectives:** Warm, confident, human, accessible, unflashy, precise.

## 2. Color Palette & Roles

Tokens are defined in `src/tokens/tokens.css` as a three-layer architecture (primitives → semantic → shadcn contract). The brand-level palette below is layer 1:

| Descriptive Name | Token | Hex | Functional Role |
|---|---|---|---|
| Almost Black | `--color-almost-black` | `#1e1e24` | Primary text. Dark surfaces. Never pure black — a touch of warmth keeps it from feeling clinical. |
| Business Blue | `--color-business-blue` | `#2c28ec` | Brand primary. CTAs, focus rings, links, interactive surfaces. |
| Human Pink | `--color-human-pink` | `#efd6d3` | Warm accent surface. Callouts, highlight panels, moments of care. |
| Beige | `--color-beige` | `#e6dcc8` | Neutral warm surface. Cards, sections, secondary backgrounds. |
| Light Beige | `--color-light-beige` | `#f4f3e8` | Default warm background. The page canvas in light mode. |
| White | `--color-white` | `#ffffff` | Default surface, inverse text on dark/brand backgrounds. |

**Color philosophy:** Blue drives action, warm neutrals hold the room, pink is for moments of human emphasis. Avoid saturated competition — the palette recedes so content leads. Named-utility classes (`bg-business-blue`, `bg-human-pink`, etc.) are **literal brand primitives and do not flip between light and dark mode** — use semantic tokens (`bg-background`, `bg-primary`, etc.) when the intent is theme-aware.

**Semantic layer:** Brand-aware aliases like `--color-text-primary`, `--color-interactive-brand-bg`, and the shadcn contract tokens (`--background`, `--foreground`, `--primary`, `--accent`, `--muted`, `--destructive`, `--border`, `--ring`) sit on top of primitives and are what components consume. This keeps components portable across theme changes without touching their CSS.

## 3. Typography Rules

**Font family:** Host Grotesk (licensed TTFs bundled with the library).

Host Grotesk is a contemporary humanist sans-serif with a confident geometric backbone and warm, open apertures. It scales well from UI microcopy to display headings and carries personality without drawing attention to itself.

**Scale:** `xs` (12px) → `5xl` (56px). **Weights available:** 300 · 400 · 500 · 600 · 700 · 800.

| Role | Weight | Size | Character |
|---|---|---|---|
| Display / hero headings | Semi-Bold–Bold (600–700) | 40–56px (`4xl`–`5xl`) | Used sparingly. One per view. |
| Section headings | Semi-Bold (600) | 24–32px (`2xl`–`3xl`) | Clear wayfinding; establishes information hierarchy. |
| Subheadings | Medium (500) | 18–20px (`lg`–`xl`) | Supports without competing. |
| Body | Regular (400) | 16px (`base`) | Line-height 1.5. Comfortable reading. |
| UI / buttons | Medium (500) | 14–16px (`sm`–`base`) | Slight tracking for button labels. |
| Captions & metadata | Regular (400) | 12–14px (`xs`–`sm`) | Secondary info; muted color. |

**Loading:** Fonts are declared in `src/styles/fonts.css` via `@font-face` and are included when the consumer imports the stylesheet: `import '@jens-wedin/design-system/styles'`.

## 4. Component Library

Manfred ships the following components (see `src/components/`):

Alert · Badge · Breadcrumb · Button · Checkbox · Dialog · FormField · Icon · Logo · ProgressBar · Radio (RadioGroup) · SearchBar · Spinner · TextInput · Toast (Toaster + `toast()` from sonner) · Tooltip · Typography.

Component APIs follow **stock shadcn shapes** where they exist (Dialog, Tooltip, RadioGroup, Toast). This is deliberate: it keeps the component surface familiar, cuts documentation overhead, and lets shadcn-savvy teams be productive immediately.

### Button

```tsx
import { Button } from '@jens-wedin/design-system';

<Button variant="primary">Get started</Button>
<Button variant="brand" size="lg">Primary CTA</Button>
<Button variant="outline" isLoading>Saving…</Button>
<Button asChild><a href="/signup">As link</a></Button>
```

**Variants:** `primary` · `brand` · `outline` · `ghost` · `inverse` · **Sizes:** `sm` · `md` · `lg`.

### Dialog · Tooltip · Toast · RadioGroup

Use the composed Radix-style shapes:

```tsx
<Dialog open onOpenChange={…}>
  <DialogTrigger asChild><Button>Open</Button></DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>…</DialogTitle>
      <DialogDescription>…</DialogDescription>
    </DialogHeader>
    <DialogFooter>…</DialogFooter>
  </DialogContent>
</Dialog>
```

Checkbox forwards `onCheckedChange(state)` (Radix idiom) instead of native `onChange(event)`. RadioGroup wraps items as `<RadioGroupItem value="a" label="A" />`.

### Logo

Uses the Guttery typeface — reserved for the Manfred logotype only. Not a UI font.

## 5. Layout Principles

- **Generous whitespace.** Sections breathe. Vertical padding of 64–96px between major sections is typical.
- **Content width.** Body content sits on a ~1120–1200px max-width container, centered. Prose columns cap around 65–75 characters.
- **Warm background rhythm.** Alternate `bg-light-beige` (canvas) and `bg-white` or `bg-beige` (cards) rather than layering grays. This is how the brand feels warm without being loud.
- **Scale expresses hierarchy.** Headings step down clearly; supporting content tightens. Avoid mid-range sizes that could read as either heading or body.
- **Minimum touch target:** 44×44px (WCAG 2.2 AA). Every interactive element.

## 6. Depth & Elevation

- **Flat-first.** Elements sit on the same plane by default. Depth is earned, not decorative.
- **Subtle card lift:** a soft `box-shadow` (roughly `0 1px 3px rgba(0,0,0,0.08)`) is enough — just enough to separate from surface, never enough to call attention.
- **Overlays:** Dialogs and menus use a dimmed backdrop (~40% opacity) behind the content. The Radix primitives handle focus trapping and scroll locking; don't reinvent this.
- **No heavy gradients, no neumorphism, no glass.** Warmth comes from color, not effects.

## 7. Iconography & Imagery

- **Icons** are line-based, consistent in stroke width, drawn on a 24px grid. They inherit `currentColor` so they travel through dark mode untouched.
- **Imagery** favors honest photography over rendered or illustrated hero art when depicting people. When illustration is used, it should share the warm palette and avoid trend-chasing stylization.
- **Logotype** is the Guttery-based mark — a single text treatment used at consistent sizes. Do not reflow, reposition, or re-color it.

## 8. Accessibility & Inclusive Design

Accessibility is a baseline commitment, not a feature.

- **WCAG 2.2 AA minimum** across all components. AAA where practical.
- **Color contrast.** All text meets 4.5:1 on its background (3:1 for large text). Verify every token pair before shipping a new combination.
- **Focus indicators.** Every interactive element has a visible focus ring tied to `--ring`. Never remove without an equivalent.
- **Semantic HTML.** Use the right element first; reach for ARIA only when HTML alone is insufficient.
- **Keyboard navigation.** All flows completable keyboard-only. Tab order follows reading order.
- **Screen readers.** Meaningful `alt` text on informative images; `alt=""` on decorative ones; labels bound to inputs; live regions for async updates.
- **Motion.** Honor `prefers-reduced-motion` — any transform/transition above 200ms should have a reduced variant or be disabled.

## 9. Dark Mode

Every component adapts. Activation is explicit:

- **System preference** — with no class on `<html>`, `prefers-color-scheme: dark` flips the semantic tokens.
- **Forced light:** `<html class="light">`.
- **Forced dark:** `<html class="dark">`.

Only **layer-2 semantic tokens** rebind in dark. Brand blue shifts from `--blue-500` (light) to `--blue-400` (dark) for legibility. Warm surfaces collapse toward neutral dark backgrounds. Feedback colors pair a darker bg with a lighter fg. Primitives never change; the shadcn contract flips automatically through `var()` indirection, so `bg-background`, `text-foreground`, `bg-primary` etc. keep working without component-level changes.

Importing the stylesheet installs a zero-specificity baseline on `<body>` that sets `background-color` and `color` from the active theme, so icons and controls relying on `currentColor` inherit correctly.

**Named brand utilities do NOT flip.** `bg-business-blue`, `bg-almost-black`, `bg-human-pink`, `bg-beige`, `bg-light-beige` point at layer-1 primitives — they remain their literal value in both themes. Reach for semantic tokens when the intent is theme-aware.

## 10. Brand Voice in UI

- **Tone:** Clear, warm, direct. Not corporate, not overly casual. Confident without being cocky.
- **Microcopy:** Say what the thing does. "Save changes" not "Submit." "You're signed in as …" not "Current user identity." Strip marketing from UI copy entirely.
- **CTAs:** Short, verb-led. "Get started," "Save," "Continue," "Send."
- **Errors:** Explain what happened, what to do next. Never blame the user. Never leak stack traces.
- **Empty states:** Treat as onboarding — suggest one next action, show what this view will look like when populated.

## 11. Do's and Don'ts

### Do

- Use semantic tokens (`bg-background`, `text-foreground`, `bg-primary`) for anything that should adapt to the theme
- Reach for shadcn-shaped component compositions (`<Dialog><DialogTrigger/><DialogContent/></Dialog>`) — they're the documented API
- Keep contrast high, touch targets at 44px+, and focus rings visible
- Alternate warm neutrals (`light-beige`, `beige`, `white`) to create rhythm without adding ornament
- Ship components with keyboard and screen-reader testing done, not "planned"

### Don't

- Don't use `bg-business-blue` or other named brand utilities and expect them to flip in dark mode — they're intentionally literal
- Don't reintroduce `<Modal isOpen>` or `<Tooltip content="…">` shapes — those were pre-0.2.0 and have been replaced with Radix-style composition
- Don't add a fourth color layer or invent tokens outside `tokens.css` — the three-layer architecture is how the system stays maintainable
- Don't use the Guttery logotype font for anything other than the logotype
- Don't use heavy shadows, gradients, or neumorphic effects — Manfred is flat and warm
- Don't add features to components without a clear a11y story — ship it accessible or don't ship it

## 12. Using Tokens in CSS

When working outside Tailwind utilities (custom stylesheets, inline styles in edge cases), reference tokens via CSS variables:

```css
.my-callout {
  background-color: var(--color-human-pink);
  color: var(--color-almost-black);
  padding: var(--spacing-4);
}
```

Prefer the Tailwind v4 `@theme` utilities wherever possible — they're generated from the same tokens and keep the dark-mode flip automatic.

## 13. Reference Material

- Source: `github.com/jens-wedin/manfred-design_system`
- Storybook: `npm run storybook` → `http://localhost:6006`
- Brand assets (fonts, logotype files, brand guidelines PDF): `References/` in the design-system repo — not modified by the library
- Companion short-form: `~/.claude/shared/manfred-brand.md` (brand voice + core values)
- Principles: `~/.claude/shared/design-principles.md` (decision framework)
