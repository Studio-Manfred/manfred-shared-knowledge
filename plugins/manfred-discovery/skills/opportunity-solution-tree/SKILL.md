---
name: opportunity-solution-tree
description: Use when building or maintaining a Teresa Torres opportunity-solution tree (OST) — connecting a desired outcome to opportunities, solutions, and assumption tests. Triggers on "OST", "opportunity solution tree", "Torres tree", "tree this out", "map outcomes to opportunities", "what opportunities serve this outcome", "where does this solution attach". Produces a markdown OST that lives in the repo and gets updated weekly.
---

# opportunity-solution-tree

Teresa Torres's opportunity-solution tree, in markdown. The thing that makes continuous discovery actually continuous.

## Overview

An OST is a living tree:

```
Outcome (the business or customer outcome we're driving)
└── Opportunity (a customer need / pain / desire that, if addressed, moves the outcome)
    └── Solution (a candidate way to address the opportunity)
        └── Assumption test (the cheapest experiment that retires the riskiest assumption about that solution)
```

It's a *thinking* tool, not a Gantt. It captures every plausible opportunity and solution under consideration, even ones we won't act on, so the team sees the alternatives that didn't get picked. Updated weekly. Lives in the repo as markdown so it travels with the team.

Source: Teresa Torres, *Continuous Discovery Habits*. The OST is the central artifact of her method.

## When to use

- Standing up a new product area / squad / outcome — first OST
- Weekly discovery ritual — pruning, adding, re-prioritising the tree
- "We have an idea — where does it attach?" / "What problem is this solving?"
- After a `manfred-discovery:product-brief` is approved with discovery as the next step
- After a `manfred-discovery:cagan-risks` profile names a High risk that turns into an assumption to test

**Skip when:**

- One-off feature that doesn't tie to a stable outcome (rare, but it happens)
- The team has no shared outcome — fix that first with `manfred-discovery:product-brief` (section 02, Strategic Alignment)

## Two principles drive everything

1. **The outcome anchors everything.** No opportunities float — every one connects up to the outcome. If you can't draw the line from a customer pain to the outcome, the pain is interesting but doesn't belong on this tree.
2. **Opportunities are customer-stated, solutions are team-generated.** Opportunities come from customer interviews, support tickets, NPS verbatims — phrased the way customers actually describe the pain. Solutions are what the team invents to address them. Don't blur the layers — that's the most common failure mode.

## Phase 1 — Establish (or surface) the outcome

If you don't have an explicit outcome, stop and find one. Ask:

- "What's the one outcome this team is accountable for this quarter? In numbers if possible — e.g. 'increase 30-day activation rate from 22% to 30%' or 'reduce time-to-first-value from 4 days to under 1 day'."
- If the answer is a feature ("ship the new dashboard"), that's not an outcome — keep digging: "What does shipping the dashboard achieve for the customer or business?"
- If the answer is multiple outcomes ("activation, retention, monetisation"), pick one for this tree. Other outcomes get other trees.

A good outcome is:

- **Customer or business measurable** (a number, not "improve X")
- **Stable for at least a quarter** (not "ship the dashboard")
- **Influence-able by the team** (not "increase market share by 20%" if the team can't move it directly)

## Phase 2 — Add opportunities

Opportunities are customer needs, pains, or desires that — if addressed — move the outcome. Pull them from real customer evidence: interview themes, support ticket clusters, NPS verbatims, behavioural drop-offs, churn-call notes.

Phrasing rules:

- **Customer-stated.** "I can't tell which of my projects need attention right now." Not "Lack of project prioritisation feature."
- **Specific.** "I'm afraid of losing the work I just did." Not "Trust issues."
- **Job-shaped, not feature-shaped.** "I want to share this with my team without them needing an account" — not "Anonymous shareable link."

Group similar opportunities. Reject vague ones — turn them into specific ones or drop them.

For each opportunity, capture:

- **The pain** (one sentence, customer's voice)
- **Evidence** (where this came from — interview ID, ticket cluster, analytics signal)
- **Outcome impact estimate** (how much this opportunity, if fully addressed, would move the outcome — Low/Med/High with one-line reason)

## Phase 3 — Add solutions under the chosen opportunities

Don't add solutions to every opportunity. Pick the 1–3 highest-impact opportunities and brainstorm 3–5 solutions each. (Torres's "compare and contrast" — multiple solutions per opportunity force better thinking than picking the first idea.)

For each solution:

- **One-sentence description** of what it is
- **Riskiest assumption** — the single thing that, if false, kills this solution
- **Initial cheapest test** — pointer to `manfred-discovery:assumption-test` for the experiment design

Solutions that don't get picked stay on the tree, marked `[parked]` with a one-line reason. Future-you will be glad to see them.

## Phase 4 — Assumption tests under each solution being pursued

Every active solution gets at least one assumption test attached. Status is one of:

- `[planned]` — designed, not yet run
- `[running]` — in flight, dates noted
- `[done — supported]` — assumption confirmed
- `[done — refuted]` — assumption killed; solution dies or pivots
- `[done — inconclusive]` — re-design the test or accept the uncertainty

Use `manfred-discovery:assumption-test` for the actual test design. The OST tracks the result, not the design.

## Phase 5 — Save the tree

Save to `discovery/<outcome-slug>-ost.md` (created if missing). Use this format:

```markdown
# OST — [Outcome name]

**Outcome:** [stable, measurable]
**Owner:** [PM / squad lead]
**Last updated:** [YYYY-MM-DD]
**Cadence:** weekly

## Opportunity 1: [customer pain in their voice]

- **Evidence:** [interview-12, support cluster #4, NPS verbatim 'X']
- **Outcome impact:** Med — [one line on why]

### Solution 1.1: [one-sentence description]
- **Riskiest assumption:** [the thing that kills this if false]
- **Tests:**
  - 2026-04-30 [running] Wizard-of-Oz with 5 customers — [link to test design]
  - 2026-04-15 [done — supported] Fake-door CTR test on signup — 8% click vs 1.2% baseline → assumption supported

### Solution 1.2: [parked]
- **Why parked:** [one line — usually "tested, refuted" or "lower impact than 1.1" or "viability blocker"]

## Opportunity 2: [...]

[...]

## Pruned (history)

- 2026-03-12 Removed opportunity "Users want a dashboard" — too feature-shaped, replaced by 3 specific pains (#5, #6, #7)
- 2026-02-28 Killed solution 2.3 (auto-categorisation) — value risk refuted by interviews
```

Pruning matters. Don't keep dead branches without context — note when and why they died.

## Manfred lens

The OST sits at the centre of the discovery workflow:

- **`manfred-discovery:product-brief`** — section 02 (Strategic Alignment) names the outcome. The OST is the ongoing tracker for everything below it.
- **`manfred-discovery:cagan-risks`** — when a risk profile names a High risk on a solution, that risk usually translates into an assumption to add under that solution.
- **`manfred-discovery:assumption-test`** — for designing each test that hangs off the tree.
- **`manfred-discovery:weekly`** — the command that runs through the OST update + plans the next customer touchpoints.
- **`manfred-discovery:discovery-rituals`** — the weekly OST review meeting is one of the rituals.

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "We don't need an OST, the team knows what we're doing" | Then writing one takes 30 minutes and confirms it. If it takes longer, you didn't all know the same thing. |
| "Let me just put solutions directly under the outcome" | That's a feature list, not an OST. The opportunity layer is what makes it discovery. Skipping it = skipping continuous discovery. |
| "Opportunity = 'lack of feature X'" | No. That's a feature in disguise. Phrase it as the customer pain that the missing feature would address. |
| "We'll only put solutions we're committed to" | Then you lose the ability to see alternatives. Park them visibly so future-you can see what you considered. |
| "Update it monthly is fine" | Then it's not continuous discovery — it's quarterly planning with a tree icon. Weekly minimum. |
| "The OST should match what's in the roadmap" | OST is what we're learning. Roadmap is what we're committing to ship. They diverge — that's the whole point. |
| "Outcome is 'ship the new feature'" | That's an output, not an outcome. What does shipping it achieve? Ask twice if needed. |

## Red flags — STOP

- About to add a solution directly under an outcome with no opportunity layer → Stop. Find the customer pain first.
- About to phrase an opportunity in feature-shaped language → Stop. Restate in the customer's voice.
- About to delete a parked solution without recording why → Stop. Note the reason in the Pruned section.
- About to call something an outcome that's actually an output → Stop. Keep asking "what does this achieve?" until you reach a customer or business measure.
- About to skip the assumption test for a solution because it "feels obviously right" → Stop. The riskiest assumption is most often the one that feels obvious.
- OST hasn't been updated in 4+ weeks and is being treated as current → Stop. Either update it now or mark it stale at the top.

## Tools used

- **Read / Write / Edit**: `discovery/<outcome-slug>-ost.md`
- **Skills called**:
  - `manfred-discovery:assumption-test` — for each solution's experiment design
  - `manfred-discovery:cagan-risks` — when a solution surfaces a High risk
  - `manfred-discovery:product-brief` — to revisit the outcome / strategic alignment
- **Reference**: Teresa Torres, *Continuous Discovery Habits* (chapters on opportunity solution trees and assumption mapping)
