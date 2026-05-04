---
description: Audit a screen, feature, or project for responsive coverage — every breakpoint tested, touch targets ≥ 44px, no hover-only, accessibility per breakpoint.
argument-hint: [scope, e.g. "audit the Settings page across all breakpoints"]
---

You're auditing a design or build for responsive coverage. The user mentioned: $ARGUMENTS

## Step 1 — Scope

Ask:

- **What's being audited?** A specific screen? A feature? A whole project's routes?
- **Design or build?** Figma file (design-stage) or deployed URL / Storybook (build-stage)?
- **Breakpoints in scope?** Default: 320 / 360 / 768 / 1024 / 1440px.
- **Real devices to test on?** At minimum one iOS + one Android phone.
- **Linear ticket?** (For posting findings.)

## Step 2 — Run the responsive-design skill (`manfred-ui-design:responsive-design`)

Walk the audit checklist:

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
- [ ] Layout grid (`manfred-ui-design:layout-grid`) snapped at every breakpoint

## Step 3 — A11y per breakpoint (`manfred-design-systems:a11y-qa`)

Run the runtime a11y gate at each breakpoint. Issues hide at specific sizes — focus that's visible on desktop may disappear inside a small mobile container; touch targets that pass on desktop may fail on mobile.

## Step 4 — Categorise findings

| Severity | Threshold | Examples |
|---|---|---|
| **Block-merge** | Breaks at a key breakpoint; a11y critical/serious; missing mobile entirely | Horizontal scroll at 320px; touch target <44px; nav unreachable on mobile |
| **High-priority** | Works but degrades; a11y moderate; awkward at one breakpoint | Visible 1px overflow at 360px; tap target 36px; hover-only interaction |
| **Cleanup** | Polish; minor density issues; scaling cosmetics | Slight padding inconsistency at 1440px; minor type-size jump |

## Step 5 — Write the audit report

Save to `audits/responsive-<scope-slug>-<YYYY-MM-DD>.md`:

```markdown
# Responsive audit: <scope>

**Date**: YYYY-MM-DD
**Audited**: design | build
**Breakpoints**: 320, 360, 768, 1024, 1440
**Real devices**: iPhone X (iOS X), Pixel X (Android X)
**Linear**: STU-XXX

## Summary
- N block-merge findings
- N high-priority findings
- N cleanup findings

## Block-merge
[file:line | breakpoint | finding | screenshot | recommended fix]

## High-priority
[same format]

## Cleanup
[same format]

## A11y per breakpoint (manfred-design-systems:a11y-qa results)
[Per breakpoint: pass/fail count]

## Recommended next steps
[Concrete: fix block-merge before merge | open N tickets for backlog]
```

## Step 6 — Linear update

Post via `mcp__linear-server__save_comment` with:

- Path to the audit report
- Block-merge count (the gate)
- A11y per-breakpoint summary
- Recommended next steps

## Wrap-up

Tell the user:

- Where the report lives
- The block-merge count
- Recommended next step

If zero block-merge findings: say so plainly. Don't manufacture issues to look thorough.

Then offer:

> "Open Linear tickets for the high-priority backlog items? Or kick off the fixes via `/manfred-design-ops:handoff` for any that need engineering pickup."
