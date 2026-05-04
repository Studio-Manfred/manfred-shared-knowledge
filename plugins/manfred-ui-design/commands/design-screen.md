---
description: Design a screen end-to-end — layout grid + responsive behaviour + colour palette + typography + visual hierarchy + dark-mode pass.
argument-hint: [screen + scope, e.g. "Smart Insights tab — desktop + mobile, dark mode included"]
---

You're designing a screen. The user mentioned: $ARGUMENTS

## Step 1 — Confirm the brief

Ask:

- **What's the user trying to do on this screen?** (Specific intent — not "browse insights" but "see if their spending is on track")
- **Primary action?** One. (If you can't name one, the hierarchy will be broken before you start.)
- **Breakpoints in scope?** Mobile (320), tablet (768), desktop (1024), wide (1440)? Default: all four.
- **Linear ticket?** (For posting decisions.)
- **Existing components / patterns to reuse?** (Default to existing — see `manfred-design-systems:component-spec`.)

If the brief is "make it look good" — push back. Specific user intent + primary action drive the design.

## Step 2 — Set the layout (`manfred-ui-design:layout-grid`)

Pick the grid for each breakpoint:

- Mobile (4 col, `gap-4`, `px-4`)
- Tablet (8 col, `gap-6`, `px-6`)
- Desktop (12 col, `gap-6`/`gap-8`, `px-8`/`px-12`, `max-w-7xl`)

Pick the layout pattern (column drop, reflow, off-canvas, sidebar) per the screen's content.

## Step 3 — Set the responsive behaviour (`manfred-ui-design:responsive-design`)

For each breakpoint:

- What changes? (Column count, sidebar visibility, nav collapse)
- Touch target sizes ≥ 44px on mobile
- No hover-only interactions
- Off-canvas pattern for nav if mobile real estate is tight

## Step 4 — Define the palette (`manfred-ui-design:color-system`)

Map every surface to existing tokens:

- Page background, cards, callouts, CTAs, status states, text
- Refuse hex generation; route through (a)/(b)/(c) for status
- Verify dark-mode behaviour per token (semantic flips, brand utilities don't)

## Step 5 — Set the type scale (`manfred-ui-design:typography-scale`)

For each text role on the screen:

- Display, section heading, subheading, body, UI labels, captions
- Host Grotesk (UI default); never Guttery outside the logotype
- Body 16px minimum; 4–5 sizes max per view
- Responsive scaling: smaller display sizes on mobile

## Step 6 — Establish hierarchy (`manfred-ui-design:visual-hierarchy`)

For each section:

- Primary action (one); secondary CTAs subordinated
- Squint test: blur eyes — hierarchy still clear?
- Above the fold: primary action surfaced or anchored
- Hierarchy holds in dark mode

## Step 7 — Dark-mode pass (`manfred-ui-design:dark-mode-design`)

Walk the design in `.dark`:

- Semantic tokens flip; brand utilities stay literal
- Contrast verified at 4.5:1 (body) / 3:1 (UI components) in both modes
- Image / illustration variants planned where needed

## Step 8 — Accessibility annotation (`manfred-design-systems:a11y-design`)

For each interactive element:

- Focus indicator (2px ring, `ring-ring`, 3:1 contrast)
- Keyboard order (Tab sequence makes sense)
- Screen-reader labels (aria-label for icon-only actions)
- Target size ≥ 24px (44px for primary)
- Reduced motion alternative for any animation

## Step 9 — Components check (`manfred-design-systems:component-spec`)

For each new component:

- Spec'd via `manfred-design-systems:component-spec`
- Mirrors shadcn shape where one exists
- All states designed (default, hover, focus, active, disabled, loading, error, empty)

For components reused from the design system: confirm they're used per spec, not customised inline.

## Step 10 — Linear update

Post via `mcp__linear-server__save_comment` with:

- Figma link
- Tokens used (cross-checked)
- Components used (existing) and components added (queued via `manfred-design-systems:component-spec`)
- A11y annotation summary
- Dark-mode verification result
- Recommended walk-through time with engineering

## Wrap-up

Confirm the design covers:

- [ ] Single primary action per view
- [ ] Layout grid per breakpoint (mobile-first)
- [ ] Responsive behaviour at 320/768/1024/1440
- [ ] Palette from existing tokens (no hex)
- [ ] Type scale (Host Grotesk, 16px body, 4–5 sizes)
- [ ] Hierarchy passes squint test
- [ ] Dark mode verified (tokens + contrast)
- [ ] A11y annotated (focus, keyboard, SR, targets, reduced motion)
- [ ] Components from design system (or new spec queued)
- [ ] Token gaps (if any) queued via `manfred-design-systems:design-token`

Then offer:

> "Pre-handoff review with `/manfred-design-ops:handoff` once design is signed off. Or run `manfred-design-research:test-plan` if a usability test should validate before engineering picks up."
