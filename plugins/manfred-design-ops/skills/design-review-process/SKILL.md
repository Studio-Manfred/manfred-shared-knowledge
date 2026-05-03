---
name: design-review-process
description: Use when establishing review gates and approval workflows for design work — anyone says "design review process", "review gates", "design approval workflow", "set up design reviews", "review checklist", "what's our review process", "when do we review designs", "approval criteria". Manfred-flavoured: Trio attendance, gates scaled to project size, accessibility as a hard gate.
---

# design-review-process

Design reviews are gates. The point isn't to slow work down — it's to catch the things that get expensive late. A good review process catches problems at the cheapest moment to fix them; a bad one becomes ceremonial drag.

Manfred runs reviews with the Trio (PM + designer + tech lead). Gates scale to project size. Accessibility is a hard gate at every stage.

## Overview

Four gates, scaled to project. Not every project needs every gate.

| Gate | When | Decides | Who |
|---|---|---|---|
| **Concept review** | After research, before design | Is this the right problem to solve? | Trio + decision maker |
| **Design review** | Mid-design, multiple options on table | Which direction? | Trio + 1-2 designers |
| **Pre-handoff review** | Design "done", before engineering pickup | Ship-ready? | Trio + accessibility check |
| **Implementation QA** | Build complete, before merge | Does the build match the spec? | Designer + `manfred-design-ops:design-qa-checklist` |

A small project (1-week feature) might collapse to one combined review. A large project (multi-month redesign) runs all four.

## When to use

- Setting up a review process for a new project / engagement
- Refreshing a stale review process that's become rubber-stamping
- Reviewing whether a current process is right-sized (too heavy? too light?)
- Onboarding a new team member to project's review rhythm
- Documenting the review process for client or stakeholder context

**Skip when:**

- Solo work with no stakeholders (rare)
- The team already has a review process that works (don't manufacture)
- The user wants critique facilitation (use `manfred-design-ops:design-critique`)
- The user wants pre-merge QA (use `manfred-design-ops:design-qa-checklist`)

## Pre-flight

Ask:

- What's the project size? (1 week → 1 review. 1 month → 2-3. Multi-month → all four.)
- Who's the decision maker? (Per RACI from `manfred-ux-strategy:stakeholder-alignment`.)
- What's the team's prior review history? (Skipping reviews entirely? Doing them but ignoring them? Doing them well but slowly?)
- Where do reviews happen? (Sync meeting? Async Figma comments? Mix?)
- What's the accessibility gate setup? (`manfred-design-systems:a11y-qa` runtime gate confirmed?)

## The hard rules

| Rule | What it means |
|---|---|
| **Right-size to project** | A 4-gate process on a 1-week feature kills velocity. A 1-gate process on a multi-month redesign skips quality. Match. |
| **Trio attends every gate** | PM + designer + tech lead. Not designer-solo. The Trio is the cross-functional check. |
| **Accessibility is a hard gate** | Every gate includes an a11y check. Pre-handoff gate includes `manfred-design-systems:a11y-design`. Implementation QA gate runs `manfred-design-systems:a11y-qa`. WCAG 2.2 AA is the floor. |
| **Time-boxed reviews** | A review that runs forever is a review that loses authority. Time-box; capture decisions; move on. |
| **Decisions captured + reasoning** | Every gate review produces: decision (proceed / iterate / stop) + reasoning + action items + owner. Without this, the gate doesn't actually gate. |
| **Block-merge severity bar** | Block-merge findings are accessibility, brand violation, broken state, scope creep. Other findings are backlog. Don't burn block-merge credibility on minor issues. |
| **Asynchronous-first where possible** | A 30-min review pre-read + 30-min sync beats a 60-min sync. Async surfaces individual perspectives; sync resolves tensions. |

## The four gates

### Gate 1: Concept review

**When**: after research, before design starts.

**Decides**: is this the right problem to solve, and is the team ready to design?

**Inputs**:
- Research synthesis (`manfred-design-research:affinity-diagram`)
- Opportunity-solution tree (`manfred-discovery:opportunity-solution-tree`)
- Design brief (`manfred-ux-strategy:design-brief`)
- 4-risk check (`manfred-discovery:cagan-risks`)

**Criteria**:
- Problem clearly defined with user evidence
- Multiple concept directions explored (not pre-decided)
- Strategic alignment confirmed (per `manfred-ux-strategy:design-principles`)
- Stakeholder input gathered

**Output**: proceed to design / iterate research / kill the project.

### Gate 2: Design review

**When**: mid-design, multiple options on the table.

**Decides**: which design direction is the team committing to?

**Inputs**:
- 2-3 design directions (sketches → mid-fi → hi-fi)
- Token + component compliance check (per `manfred-design-systems:design-token`, `manfred-design-systems:component-spec`)
- Initial accessibility annotation (per `manfred-design-systems:a11y-design`)

**Criteria**:
- Visual design uses Manfred design system (no hex literals, references existing components)
- Interaction patterns consistent with Manfred design principles
- Responsive behaviour defined
- Content strategy applied
- Initial a11y check (focus order, target sizes, contrast)

**Output**: commit to direction X / iterate top two / explore further.

### Gate 3: Pre-handoff review

**When**: design "done", before engineering pickup.

**Decides**: is this ship-ready for handoff?

**Inputs**:
- Final design + Figma source
- All states designed (default · hover · focus · active · disabled · loading · error · empty)
- A11y annotation (per `manfred-design-systems:a11y-design`)
- Handoff spec drafted (per `manfred-design-ops:handoff-spec`)
- Component spec(s) (per `manfred-design-systems:component-spec`) where new components introduced

**Criteria**:
- All states designed (not just happy path)
- Edge cases addressed
- Accessibility requirements met (focus order, keyboard, SR labels per spec)
- Handoff spec complete and tight (per the ~300-word cap)
- Engineering walk-through scheduled or async-equivalent recorded
- Tokens used; no hex literals or default Tailwind palette

**Output**: handoff to engineering / iterate states / iterate a11y.

### Gate 4: Implementation QA

**When**: build complete, before merge to main.

**Decides**: does the built thing match the design intent and pass the a11y floor?

**Inputs**:
- Built thing (Storybook URL, dev server, PR preview)
- Spec source (Figma + handoff spec)
- `manfred-dev:test-my-code` runs (covers engineering-side gates including `manfred-design-systems:a11y-qa`)
- Designer QA pass (per `manfred-design-ops:design-qa-checklist`)

**Criteria**:
- Implementation matches spec (visual + interaction + content)
- All states render correctly
- Responsive behaviour verified
- A11y runtime gate passed (0 critical/serious findings)
- Cross-browser/device covered

**Output**: merge / fix block-merge findings / fix high-priority + merge.

## Sizing the process

### Small project (1-week feature, single component)
- Combined gate: pre-handoff + implementation QA in one pass
- Designer-led, async Figma comments + 30-min Trio sync
- Total review overhead: ~2 hours

### Medium project (1-month feature, multi-screen flow)
- Gate 1 (concept) + Gate 3 (pre-handoff) + Gate 4 (QA)
- Skip Gate 2 (design review) if direction is clear early
- Total review overhead: ~5 hours across the month

### Large project (multi-month redesign, ecosystem-level)
- All four gates
- Gate 2 may run multiple times across explorations
- Total review overhead: ~15-20 hours across the engagement

## Common rationalisations

| Excuse | Reality |
|---|---|
| "We're moving fast, skip the gates" | Skipping the cheap gate (concept) creates the expensive bug (post-launch fix). Gates exist to catch problems early. |
| "Designer-solo review is fine, the Trio's busy" | The Trio is busy because they aren't reviewing. The gate is the cross-functional check; designer-solo loses it. |
| "Accessibility is gate 4 work, not gate 3" | A11y at gate 3 is annotation; at gate 4 is runtime. Both run. Skipping gate 3 a11y means engineering rework. |
| "Reviews are taking too long" | Time-box. Async-first. Capture decisions. If reviews still drag, the team isn't deciding — that's a decision-rights problem (use `manfred-ux-strategy:stakeholder-alignment`), not a review-process problem. |
| "We'll capture decisions in our heads" | Decisions in heads = decisions re-litigated next week. Write them down. |
| "Implementation QA is engineering's job" | Engineering's QA (`manfred-dev:test-my-code`) covers engineering tests. Design QA is the design-side pass — it's the designer's job and it complements engineering QA. |

## Red flags — STOP

- About to set up a 4-gate process on a 1-week project
- Reviews running designer-solo at scale
- A11y gate missing from any of the four gates
- No decision captured at gate close
- Block-merge findings being argued away
- Reviews running 2x their time-box without changing format
- Concept review skipped because "we know what to build" (= you're starting from your assumptions, not user evidence)

## Manfred lens

Design reviews touch all four **Cagan risks**:

- **Value** (concept review) — does this serve a real need?
- **Usability** (design + pre-handoff reviews) — can users actually use it?
- **Feasibility** (pre-handoff review) — can engineering build it?
- **Viability** (implementation QA) — does it ship and work?

Skipping a gate skips its risk check. Don't.

Critical & ethical (principle 6): every gate includes "what does this design do in the world?" — concept review is the cheapest moment to surface ethics issues; implementation QA is the most expensive. Surface early.

## Cross-references

- `manfred-design-ops:design-critique` — the format for the team-crit conversation inside Gate 2
- `manfred-design-ops:handoff-spec` — the artifact gate 3 produces
- `manfred-design-ops:design-qa-checklist` — the checklist gate 4 runs
- `manfred-design-systems:a11y-design` — gate 3 a11y check
- `manfred-design-systems:a11y-qa` — gate 4 runtime a11y check
- `manfred-design-systems:component-spec` — input for gate 3
- `manfred-design-systems:design-token` — input for gate 3
- `manfred-discovery:cagan-risks` — input for gate 1
- `manfred-ux-strategy:design-brief` — input for gate 1
- `manfred-ux-strategy:stakeholder-alignment` — for decision rights inside the gates

## Tools used

- `Read` — design artifacts at each gate
- `Write` — capture decisions + action items
- `mcp__linear-server__save_comment` — post gate decisions to the ticket
- `manfred-design-ops:design-critique` — for the team-crit format
- `manfred-design-systems:a11y-qa` — for gate 4

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
