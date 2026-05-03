---
name: design-sprint-plan
description: Use when planning or facilitating a design sprint — anyone says "design sprint", "5-day sprint", "Google Ventures sprint", "GV sprint", "challenge to prototype", "sprint planning", "kick off a sprint", "design week", "rapid prototype". Manfred-flavoured: pairs with continuous discovery, prototype testing routes through `manfred-design-research:usability-test-plan`.
---

# design-sprint-plan

A design sprint compresses "frame a hard problem → ship a tested prototype" into one focused week. Done well, it produces customer-validated direction in 5 days. Done badly, it produces a slick prototype that never connects back to discovery.

Manfred treats sprints as one mode among several, not the default. Continuous discovery is the baseline (`manfred-discovery:discovery-rituals`); sprints are for moments when a hard problem needs concentrated team attention.

## Overview

Three sprint shapes:

| Shape | Length | When |
|---|---|---|
| **Classic 5-day** | 1 week | Hard, well-bounded challenge needing cross-functional concentration |
| **Mini sprint** | 2-3 days | Smaller challenge or tighter team |
| **Discovery sprint** | Days 1-2 only (no prototype) | Early-stage problem framing, no prototype warranted yet |

The Classic structure: Day 1 Understand → Day 2 Diverge → Day 3 Decide → Day 4 Prototype → Day 5 Test. Each day has a specific output that feeds the next.

## When to use

- A specific, important problem the team keeps circling without resolving
- A new product direction needing concentrated framing
- A high-stakes design decision that benefits from cross-functional input + testing
- Pre-strategy: surfacing what's known and unknown about a problem space
- Onboarding a new client engagement (modified discovery-sprint shape)

**Skip when:**

- The problem isn't well-bounded (sprint with no clear challenge produces handwaving)
- The team can't clear schedules for 5 days (sprint with half-attendance is sprint-shaped meetings)
- A regular discovery cycle (`manfred-discovery:weekly`) would suffice (don't manufacture sprint when continuous discovery already serves the work)
- The decision-maker can't be in the room (sprint without decider produces design-by-committee)

## Pre-flight (week before sprint)

These have to be locked before Day 1, or the sprint fails on Day 3:

- [ ] **Challenge statement defined** — one sentence, falsifiable, ambitious. ("In 6 months, X user can do Y in N seconds.")
- [ ] **Decision maker identified + committed** — must be in the room every day, or a delegate with explicit authority to decide on their behalf
- [ ] **Team assembled** — 5-7 people, cross-functional (designer + PM + tech + business + 1-2 domain experts)
- [ ] **Room + materials** — physical or virtual; whiteboards, sticky notes, dot-vote stickers; recording set up
- [ ] **Users recruited for Day 5** — 5 users matching the target archetype (`manfred-design-research:user-archetype`); pay them
- [ ] **Schedules cleared** — every team member's full week. Half-attendance kills the sprint.
- [ ] **Materials read in advance** — research, existing artefacts, prior attempts. Day 1 starts from a shared baseline.

If any of these is missing, push to next week. Sprints with missing pre-flight are sprints in name only.

## The hard rules

| Rule | What it means |
|---|---|
| **Decision maker in the room** | The decider attends every day, or the sprint produces direction the decider can override on Day 6. Wasted week. |
| **Follow the process even when slow** | Day 1 feels slow. Day 2 feels chaotic. Day 3 feels rushed. The structure is designed; trust it. Skipping Day 1 to "get to prototyping" produces shallow prototypes. |
| **No devices in working sessions** | Phones away, laptops closed during sketching, voting, discussion. The point is concentrated team attention. |
| **Document everything** | Photos of every whiteboard, notes from every discussion, recordings of every test. The artefacts feed the synthesis after the sprint. |
| **Test 5 users on Day 5** | Not 4, not 10. 5 catches ~85% of usability issues; more is diminishing returns. |
| **Plan the follow-up before Day 5 ends** | Sprints without follow-up produce slides nobody acts on. End the sprint with: who picks up what, by when. |
| **Pay the users** | Day 5 testers get paid. Manfred design principle 1 + research-as-posture (principle 2) — research participants are working for you, compensate them. |

## The 5-day flow

### Day 1 — Understand

**Goal**: shared understanding of the problem and the constraints.

- 9-10am — Frame: introduce the challenge, the long-term goal, sprint questions
- 10-11am — "Ask the experts" — short interviews with 3-5 internal experts (research, customer support, sales, engineering). 15 min each.
- 11-12 — Take notes via "How might we…" sticky notes. Each participant writes "HMW…" notes during interviews.
- 1-2pm — Affinity-cluster the HMW notes (`manfred-design-research:affinity-diagram`)
- 2-3pm — Map the user journey on the wall — current state, end-to-end
- 3-4pm — Ask the decider to pick a target moment in the journey to focus the rest of the sprint on
- 4-5pm — Document the day; review tomorrow's plan

**Output**: target moment + cluster of HMW notes around it.

### Day 2 — Diverge

**Goal**: maximum solution exploration.

- 9-10am — Lightning demos: 3-5 short presentations of inspiration from inside or outside the category (1-3 min each)
- 10-11am — "Notes" exercise: each participant takes 20 min to silently note ideas, then 20 min to sketch crazy 8s (8 sketches in 8 min)
- 11-12 — Solution sketch: each participant produces a 3-panel storyboard of their best solution
- 1-3pm — Quiet review: solutions go on the wall; participants silently review with dot stickers (heat map vote)
- 3-4pm — Speed critique: quick walk through each solution, name the strongest moments
- 4-5pm — Straw poll vote — each person picks 1 solution; decider has supervote

**Output**: 1-3 candidate directions to combine into the prototype.

### Day 3 — Decide

**Goal**: commit to one direction and storyboard it.

- 9-10am — Mash-up or pick-the-winner discussion (depending on Day 2 vote shape)
- 10-12 — Storyboard the prototype flow on the whiteboard — 10-15 frames
- 1-2pm — Assign roles for prototype creation: stitcher, screen designer(s), copywriter, asset wrangler, interviewer
- 2-3pm — Plan the test: which research questions does Day 5 answer? (`manfred-design-research:usability-test-plan`)
- 3-4pm — Recruit confirmation — confirm 5 testers locked in
- 4-5pm — Decompose the prototype into screens; assign

**Output**: storyboard + test plan + role assignments.

### Day 4 — Prototype

**Goal**: build a realistic facade prototype.

- 9-12 — Divide and conquer: each role works on their section
- 1-3pm — Stitch — combine sections into one continuous flow
- 3-4pm — Walkthrough — interviewer rehearses the prototype against the test script
- 4-5pm — Confirm test logistics — links work, recording works, payment ready

**Output**: realistic facade prototype + tested logistics.

### Day 5 — Test

**Goal**: 5 user interviews, observe patterns.

- 9-10am — Interview 1 — interviewer + observation room (or shared screen for remote)
- 10-12 — 2 more interviews
- 1-3pm — 2 final interviews
- 3-4pm — Debrief: each participant captures top 3 patterns
- 4-5pm — Synthesise: where did users succeed? Where did they get stuck? What's the team's confidence level on the direction?

**Output**: tested patterns + go/iterate/kill recommendation + follow-up plan.

## Variations

### Mini sprint (2-3 days)

- Day 1 = understand + diverge (combined, 8 hours)
- Day 2 = decide + prototype (combined, 8 hours)
- Day 3 = test + synthesise (combined, 8 hours)

Smaller scope; same structure compressed.

### Remote sprint

- Replace whiteboard with FigJam / Miro
- Replace dot stickers with reactions
- Replace in-room interviews with video calls + observer rooms
- Pre-record lightning demos to save time
- Add explicit "computer off" breaks (remote sprint exhaustion is real)

### Discovery sprint (days 1-2 only)

When the problem isn't yet well-bounded enough to prototype against. Run Day 1 + Day 2 only — output is a sharpened problem statement and a set of explored directions, not a prototype. Often pairs with `manfred-discovery:opportunity-solution-tree` work in the following week.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "We don't need a sprint, we already know what to build" | If you knew, you wouldn't need 5 days. The sprint surfaces what you don't know. If you genuinely know, build — don't run a sprint. |
| "Decider doesn't have time for the full week" | Then don't run a sprint. Sprint without decider is structured waste. |
| "We'll do interviews in the office on Day 5 with employees" | Employees aren't users. Recruit real users; pay them. |
| "5 users isn't statistically significant" | Sprints aren't statistical. 5 catches ~85% of usability issues; more is diminishing returns. |
| "We'll figure out follow-up after Day 5" | Sprints without follow-up produce slides nobody acts on. Plan it Day 5 morning. |
| "Async sprint — we'll spread over 2 weeks" | That's not a sprint, it's regular work. The compression is the point. |
| "We'll skip Day 1 and start prototyping Day 2" | Day 1 is the foundation. Skipping it means prototypes that don't address the actual problem. |

## Red flags — STOP

- Decider isn't committed for the full week
- Pre-flight checklist not all green by sprint Friday
- Phones / laptops in working sessions
- Day 5 testers aren't real users (employees, the team's friends, etc.)
- Day 5 testers aren't being paid
- No follow-up plan by Day 5 lunch
- "We'll skip Day 1" or "we'll skip Day 5" — that's not a sprint anymore

## Manfred lens

Sprints touch **value risk** + **usability risk** (Cagan) — they validate that the team is building something users will actually use, before committing engineering. They feed `manfred-discovery:opportunity-solution-tree` — sprint output is usually 1 confirmed direction (becomes an OST opportunity branch) + several rejected directions (become "do not pursue" notes).

Sprints are not a substitute for `manfred-discovery:discovery-rituals`. Continuous discovery is the baseline; sprints are concentrated bursts.

Critical & ethical (principle 6): include the ethics question in Day 1's problem framing and Day 5's synthesis. "What does this design do in the world?" is a Day 1 question, not a Day 6 afterthought.

## Cross-references

- `manfred-discovery:discovery-rituals` — sprints are one ritual mode among several; continuous discovery is the baseline
- `manfred-discovery:opportunity-solution-tree` — sprint output feeds OST opportunities
- `manfred-design-research:usability-test-plan` — for the Day 5 test design
- `manfred-design-research:user-archetype` — for Day 5 recruit
- `manfred-design-research:affinity-diagram` — for Day 1 HMW clustering
- `manfred-ux-strategy:design-brief` — sprints often produce or refine the brief

## Tools used

- `Read` — research, prior artefacts, existing artefacts
- `Write` — capture daily outputs, sprint debrief, follow-up plan
- `mcp__linear-server__save_comment` — post sprint summary to the ticket / project
- `manfred-design-research:usability-test-plan` — for Day 5
- `manfred-design-research:summarize-interview` — for Day 5 debrief

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
