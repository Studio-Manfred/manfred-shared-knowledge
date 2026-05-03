# manfred-design-ops

Manfred-flavoured design ops: handoff specs (Linear-integrated, token-anchored), design critiques, QA checklists, review process gates, design sprints, team workflows, version control strategy.

Trio attendance (PM + designer + tech lead). Design system as source of truth. Handoffs go to Linear, not screenshots. Async-first with sync moments earned.

## Skills

| Skill | When it triggers |
|-------|-----------------|
| `handoff-spec` | "write a handoff spec", "engineering handoff", "spec for the dev team", "redline this for engineers", "ship to dev" — **foundational TDD'd skill**: posts to Linear via MCP, hard 300-word cap, refuses hex literals, refuses kitchen-sink dumps, requires walk-through scheduling |
| `design-critique` | "design crit", "feedback on this design", "team critique", "desk critique" — Trio attends; structured "I notice / I wonder / What if / I think because" feedback format; action items captured + owned |
| `design-qa-checklist` | "design QA", "spec compliance check", "does this match the design", "designer review of the PR" — token-anchored; 6 categories; runtime a11y gate via `manfred-design-systems:a11y-qa` |
| `design-review-process` | "design review process", "review gates", "approval workflow", "set up design reviews" — 4 gates scaled to project size; accessibility hard gate |
| `design-sprint-plan` | "design sprint", "5-day sprint", "GV sprint", "challenge to prototype" — Classic / Mini / Discovery / Remote shapes; Day-0 checklist; Day 5 test plan via `manfred-design-research:usability-test-plan` |
| `team-workflow` | "team workflow", "design team rituals", "design ops setup", "task management for designers" — 5 components, async-first, Linear-anchored, scaled to team size |
| `version-control-strategy` | "design system versioning", "Figma versioning", "design changelog", "component library semver" — SemVer for code/tokens, Figma named versions, breaking changes flagged loudly |

## Commands

| Command | What it does |
|---------|--------------|
| `/manfred-design-ops:handoff` | Hand off a finished design to engineering. Pre-handoff review + token check + spec drafted + Linear post + walk-through scheduled. |
| `/manfred-design-ops:plan-sprint` | Plan a design sprint end-to-end. Challenge framing + Day-0 checklist + 5-day schedule + recruit + test plan + follow-up commitment. |
| `/manfred-design-ops:setup-workflow` | Set up a design team's workflow. Task management + rituals + comms norms + tooling + design↔eng seams + version control. Documented and revisitable. |

## Manfred opinions baked in

- **Trio attends cross-functional rituals** (PM + designer + tech lead — not designer-solo)
- **Design system is the source of truth** — handoffs reference tokens, not screenshots; QA verifies token compliance, not memory
- **Linear is the delivery channel** — handoffs, design reviews, QA findings, sprint summaries all post via `mcp__linear-server__save_comment`
- **Async-first, sync earned** — most "quick syncs" should be Linear comments + Loom; sync for tension resolution, not coordination
- **Accessibility is a hard gate at every review** (Manfred design principle 5; WCAG 2.2 AA non-negotiable)
- **Handoff specs are tight** (~300-word cap on intent + decisions + open questions; Figma is the measurement source, not the spec doc)
- **Kitchen-sink specs refused** — completeness theatre is worse than a tight spec engineering reads end-to-end

## Cross-plugin handoffs

- **`manfred-dev:test-my-code` and `manfred-dev:release`** are downstream of `handoff-spec` — they verify the build against the spec and run `manfred-design-systems:a11y-qa`
- **`manfred-design-systems:component-spec`** is what `handoff-spec` builds on for new components
- **`manfred-design-systems:design-token`** enforces the token-first rule used by `handoff-spec` and `design-qa-checklist`
- **`manfred-design-systems:a11y-design`** + **`a11y-qa`** are the a11y gates run inside `design-review-process` and `design-qa-checklist`
- **`manfred-design-research:usability-test-plan`** is run for sprint Day 5 + post-handoff usability validation
- **`manfred-discovery:discovery-rituals`** sits next to `team-workflow` — discovery cadence + design cadence

## Install

```
/plugin marketplace add Studio-Manfred/manfred-shared-knowledge
/plugin install manfred-design-ops@manfred
```
