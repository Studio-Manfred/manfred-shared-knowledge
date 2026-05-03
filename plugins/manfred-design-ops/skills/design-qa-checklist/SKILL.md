---
name: design-qa-checklist
description: Use when verifying that an implementation matches the design spec — anyone says "design QA", "spec compliance check", "does this match the design", "design review of the build", "QA against design", "implementation matches Figma", "design-side QA pass", "designer review of the PR". Manfred-flavoured: token-anchored, references existing components, runs through `manfred-design-systems:a11y-qa` for runtime gate.
---

# design-qa-checklist

Design QA is the designer's pass over the built thing. Not "did engineering follow my Figma exactly" — that's not the question. The question is: does the built thing meet the design intent, the token system, the accessibility floor, and the user need it was built to serve?

A good design QA catches drift before launch. A bad one becomes a list of pixel nits engineering ignores.

## Overview

Six categories. Run them in order — visual / layout first (catches the obvious), then interaction / content / accessibility / cross-platform (catches the subtle).

| Category | What it covers |
|---|---|
| **Visual accuracy** | Tokens used? Type scale right? Icons correct? |
| **Layout** | Grid alignment, responsive breakpoints, no overflow |
| **Interaction** | All states render; transitions match; focus visible |
| **Content** | Real content fits; truncation works; empty/loading/error states |
| **Accessibility** | WCAG 2.2 AA — keyboard, SR, contrast, focus, reduced motion |
| **Cross-platform** | Required browsers, devices, OS text-size settings |

The runtime accessibility gate runs through `manfred-design-systems:a11y-qa` — this skill produces the design-side checklist that complements it.

## When to use

- Pre-merge QA on a UI change (the design's own pass, separate from the engineering test gate)
- Pre-release QA on a feature that's design-led
- Auditing existing surfaces for design-system compliance
- Setting up a recurring QA ritual on a project

**Skip when:**

- The change has no UI surface (CLI, worker, API)
- The change is so small (one-line copy fix) that QA is overkill
- The user wants engineering test gates (use `manfred-dev:test-my-code`)
- The user wants accessibility audits specifically (use `manfred-design-systems:a11y-qa` directly)

## Pre-flight

Before running the QA:

- **Spec source.** What's the design source of truth? Figma? `manfred-design-systems:component-spec` output? Both — Figma for the visual, spec doc for the API.
- **Build location.** Where's the built thing? Storybook URL, dev server, staging, PR preview?
- **Scope.** One component? One screen? A whole flow?
- **Linear ticket.** For posting findings as a comment.

If the spec source is "in my head" — push back. QA against memory is QA against drift.

## The hard rules

| Rule | What it means |
|---|---|
| **QA against the spec, not memory** | Open the Figma. Open the spec doc. Compare. Don't QA from "I remember it being…" |
| **Use real content + data** | Lorem ipsum hides truncation, alignment, density issues. Test with the longest realistic name, the longest possible amount, the most-data and least-data states. |
| **Tokens, not pixels** | When checking colour / spacing, verify it resolves to the right token (browser dev tools → computed style → CSS variable). "Looks right" isn't enough — different tokens can produce visually similar values. |
| **All states, not happy path** | Default + hover + focus + active + disabled + loading + error + empty. Skipping a state at QA = shipping a state untested. |
| **A11y is its own pass** | Don't roll a11y into "it looks fine". Run `manfred-design-systems:a11y-qa` for the runtime gate. This skill captures design-side a11y findings (keyboard order, SR labels per the spec, focus indicators visible). |
| **Bugs filed with screenshots + spec ref** | "Looks wrong" is unactionable. "Spacing here is `gap-2` per Figma; build renders `gap-3`. Screenshot attached." is actionable. |
| **Block-merge severity bar is high** | Block-merge findings are accessibility, brand violation, broken state. Pixel nits are backlog. Don't burn block-merge credibility on minor issues. |

## The checklist (run top to bottom)

### 1. Visual accuracy

- [ ] **Colours** match design tokens (verify via dev tools → computed style → CSS variable resolves to the expected token)
- [ ] **Typography** matches the role from `~/.claude/shared/DESIGN.md` Section 3 (size / weight / line-height; no off-scale values)
- [ ] **Spacing** matches Tailwind primitives (no random `8.5px` paddings; uses `p-2` / `gap-4` / etc.)
- [ ] **Border radius** matches token (`rounded-md`, `rounded-lg`, `rounded-full`)
- [ ] **Shadows** match token (no custom blur values)
- [ ] **Opacity** values match spec (no surprise `opacity-50` on text that should be muted token)
- [ ] **Icons** correct size + colour + library (Lucide unless project decided otherwise — see `manfred-design-systems:icon-system`)
- [ ] **Images** correct aspect ratio + format (no jagged scaling, no surprise PNGs where SVG would work)

### 2. Layout

- [ ] **Grid alignment** matches spec at default breakpoint
- [ ] **Responsive** behaviour matches at each tested breakpoint (320, 768, 1024, 1440 minimum per design principle 12)
- [ ] **Content reflows** properly — no horizontal scroll, no clipping
- [ ] **Min/max widths** respected (long text doesn't break the layout; short text doesn't collapse it)
- [ ] **Container queries** working as designed (if used)

### 3. Interaction

- [ ] **All states** render correctly: default · hover · focus · focus-visible · active · disabled · loading · error
- [ ] **Transitions** match spec (duration, easing, properties)
- [ ] **Animations** respect `prefers-reduced-motion`
- [ ] **Touch targets** at least 24×24 px (44×44 px for primary actions per design principle 12)
- [ ] **Keyboard navigation** in correct order; no keyboard traps
- [ ] **Focus indicators** visible against every adjacent surface (light and dark modes)

### 4. Content

- [ ] **Real content** fits the layout (not lorem ipsum)
- [ ] **Truncation** works as specified (where and how — ellipsis, fade, "show more"?)
- [ ] **Empty states** display correctly
- [ ] **Error messages** are correct + helpful (no "Error 4xx" — actual user-readable text)
- [ ] **Loading states** appear as designed (skeleton vs spinner — chose deliberately?)
- [ ] **Long-text edge cases** handled (long names, long emails, long amounts)

### 5. Accessibility

- [ ] **Screen reader** announces correctly (test with VoiceOver / NVDA — at least one device)
- [ ] **Colour contrast** meets WCAG 2.2 AA (4.5:1 body, 3:1 large text and UI components — verify with `manfred-design-systems:a11y-qa`)
- [ ] **Focus management** works (focus moves logically; focus returns after dialog close; etc.)
- [ ] **ARIA labels + roles** correct (icon-only actions have `aria-label`; live regions have `role="status"` or `role="alert"`)
- [ ] **Reduced motion** respected (animations have a non-animated alternative)
- [ ] **Forms** have labels, error associations, helper-text associations

### 6. Cross-platform

- [ ] **Browsers** in scope (project's required matrix — usually Chrome / Safari / Firefox latest)
- [ ] **Devices** in scope (iOS / Android / desktop)
- [ ] **OS text size** settings handled (large text shouldn't break layout)
- [ ] **Screen densities** handled (icons + images crisp at 2x / 3x)
- [ ] **Dark mode** matches spec (per design principle 9 — Manfred ships dark day-one)

## QA process

1. **Self-review** by developer against this checklist before opening PR
2. **Designer pass** runs the checklist against the deployed branch / Storybook
3. **Bugs filed** with screenshots: design vs implementation, plus spec ref
4. **Severity tagged**: block-merge / high-priority / cleanup
5. **Verify fixes** before close

Findings posted as Linear comment on the ticket via `mcp__linear-server__save_comment`. Pattern reference: `manfred-dev:test-my-code` Linear update section.

## Output format

Save to `qa-reports/<surface-slug>-<YYYY-MM-DD>-design-qa.md`:

```markdown
# Design QA: <surface> (STU-XXX)

**Date**: YYYY-MM-DD
**Build**: <Storybook URL / branch / staging>
**Design source**: <Figma link>
**Reviewer**: <name>

## Summary
- N block-merge findings
- N high-priority findings
- N cleanup findings

## Block-merge
[file:line | screenshot | finding | spec ref | recommended fix]

## High-priority
[file:line | screenshot | finding | spec ref | recommended fix]

## Cleanup
[file:line | screenshot | finding | spec ref | recommended fix]

## Tokens / components used vs spec
[Brief — cross-reference what was built against what was spec'd]

## A11y gate result
Ran `manfred-design-systems:a11y-qa` — [pass/fail with finding count]

## Recommended next step
[Concrete — usually "fix block-merge before merge", or "open N tickets for backlog"]
```

## Common rationalisations

| Excuse | Reality |
|---|---|
| "I'll QA against memory, I designed it" | Memory drifts. Open the spec; compare. |
| "Lorem ipsum is fine for the QA pass" | Lorem hides the truncation, alignment, and content-density issues that ship. Use real content. |
| "Hover states are obvious, I'll skip them" | Hover, focus, active, disabled, loading, error are all distinct states with distinct a11y. Don't skip. |
| "We'll do accessibility QA after launch" | "After launch" doesn't happen. The runtime gate (`manfred-design-systems:a11y-qa`) runs pre-merge. |
| "I'll just file 'looks wrong' bugs" | Engineering can't act on that. Screenshot + spec ref + severity = actionable. |
| "Block-merge for this 1px nit" | Don't burn block-merge credibility. Reserve for accessibility, brand violation, broken state. Pixel nits are cleanup. |

## Red flags — STOP

- About to QA without opening the spec source
- Skipping a state because "it's obvious"
- Filing bugs without screenshots or spec references
- Calling something "block-merge" when it's a pixel preference
- Skipping the a11y pass because "the build looks fine"
- Running QA against lorem-ipsum content

## Manfred lens

Design QA is **infrastructure** — Cagan/Torres lens doesn't apply directly. But: it's the moment design discipline gets enforced or quietly abandoned. Skipping the QA pass is how shipped products drift from their spec.

A11y findings carry the most weight here — Manfred design principle 5 says accessibility is non-negotiable. Block-merge severity for any WCAG 2.2 AA failure isn't optional.

## Cross-references

- `manfred-design-ops:handoff-spec` — the spec this QA verifies against
- `manfred-design-ops:design-review-process` — the gate this QA is part of
- `manfred-design-systems:design-token` — for verifying token compliance
- `manfred-design-systems:a11y-qa` — runtime a11y gate (called from this skill)
- `manfred-design-systems:component-spec` — the component-side spec this QA cross-references
- `manfred-dev:test-my-code` — engineering-side test gate (sibling artifact)

## Tools used

- `Bash` — `grep -rn` for token / component compliance, browser dev tools for computed styles
- `Read` — Figma exports, spec docs
- `Write` — produce the QA report
- `mcp__linear-server__save_comment` — post findings to the ticket
- `manfred-design-systems:a11y-qa` — runtime a11y gate

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
