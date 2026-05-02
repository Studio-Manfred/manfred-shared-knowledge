---
name: customer-touchpoint-plan
description: Use when planning weekly customer conversations for continuous discovery (Teresa Torres). Triggers on "weekly customer touchpoint", "plan customer interviews this week", "continuous discovery interviews", "set up discovery cadence", "customer conversation plan", "interview recruit", "discovery sprint plan". Produces a one-week plan: who you're talking to, when, what you're trying to learn, and where the answers update the OST.
---

# customer-touchpoint-plan

A week of customer conversations, planned. The continuous part of continuous discovery only stays continuous if it's scheduled.

## Overview

Torres's continuous discovery hinges on talking to customers every week. Not "when we have a project" — every week. This skill produces a one-week plan: who, when, what topics, what assumptions are being probed, what gets updated as a result.

A good week of touchpoints does one of:

- Surfaces new opportunities (when the team is in expansion mode)
- Refines existing opportunities (when the OST has gaps)
- Probes specific assumptions (when assumption tests need qualitative signal)

You don't have to do all three in one week. Pick one mode per week.

Source: Teresa Torres, *Continuous Discovery Habits* — chapter on continuous interviewing and the Trio (PM + designer + tech lead) attending together.

## When to use

- Start of a sprint / week — planning the discovery activity
- After an `manfred-discovery:opportunity-solution-tree` update reveals gaps to probe
- After an `manfred-discovery:assumption-test` design that needs customer recruit
- A team that wants to start continuous discovery — the first plan

**Skip when:**

- The team is doing one-off project research (use `design-research:interview-script` from the design-research plugin instead, when it ships)
- Heavy quantitative testing where customer voice isn't the bottleneck

## Two principles drive everything

1. **The Trio attends together.** PM, designer, and (where possible) tech lead in every interview. Asynchronous read-back of recordings is a fallback, not the default. The team needs the same exposure to be able to make the same decisions.
2. **Recruit from your customer base, not from panels.** Real users of your product give signal that paid panels can't. Build a recruit pipeline once, reuse weekly. Pay people for their time.

## Phase 1 — Pick the mode for this week

| Mode | Use when | Output |
|------|----------|--------|
| **Expansion** | The OST feels thin or the outcome is new | New opportunities added under the outcome |
| **Refinement** | Opportunities exist but feel vague or ungrounded | Opportunities sharpened with better evidence; some merged or pruned |
| **Probe** | Specific assumptions need qualitative signal | Assumption tests get directional data; possible re-rate |

If the team picks more than one, push back: pick one. A week of focused touchpoints beats a scattered week.

## Phase 2 — Decide the recruit

Ask:

- "Who do we need to talk to? Be specific — segment, behaviour, recency. 'Recent users' is too broad — 'users who churned in the last 30 days' is usable."
- "How many? 5–8 is the sweet spot for one week. Below 5 is fragile, above 10 is hard to actually attend as a Trio."
- "Recruit channel — in-product prompt, support ticket history, CS list, paid panel as a last resort?"
- "Incentive — what are we paying? (Pay people. Always pay people.)"

Capture as:

```
Segment: [specific description]
Sample: [number] customers
Channel: [recruit source]
Incentive: [amount, format]
Recruit owner: [Name + by when]
```

If the user can't answer "who exactly," send them back to define the question this week is answering, then come back.

## Phase 3 — Schedule the conversations

For a 5-customer week:

- Block 5 × 60-minute slots (50 for conversation, 10 for buffer/notes)
- Spread across 3 days, not jammed into one (the team needs reflection time between)
- Trio attends each — calendar holds for all three
- Recording + transcript via your usual tooling (Tella, Dovetail, Otter, etc.)

If the Trio can't all attend, scope down to 3–4 customers that week. Don't run 8 interviews with only the PM in the room — the Trio symmetry matters more than the customer count.

## Phase 4 — Prep the topics & assumptions

For each conversation, write a short brief:

```
Customer: [first name only, segment]
Time slot: [day/time]
Trio attendees: [PM / Designer / Tech lead names]

What we want to learn (1–3 things, no more):
1. [open question — opportunity exploration]
2. [specific probe — tied to an OST opportunity or assumption]
3. [optional — recent product change feedback]

Assumptions being probed (link to assumption-test files if any):
- [assumption-1] — supporting / refuting evidence we'd accept
- [assumption-2] — ...

Opening prompt: [first 2–3 sentences to set context for the customer]

Backup line if conversation stalls: [a "tell me about the last time you..." question]
```

Use Torres's "story-based interview" technique: ask about specific past events, not hypothetical futures. "Tell me about the last time you tried to X" beats "Would you use Y?"

Avoid:

- Leading questions ("Do you find the dashboard helpful?")
- Solution validation ("Would you use this?" — anything they say is unreliable)
- Multi-part questions (ask one, listen, follow up)

## Phase 5 — Save the plan

Save to `discovery/touchpoints/<YYYY>-W<week-number>.md`. Format:

```markdown
# Customer touchpoints — Week [N], [YYYY]

**Mode:** Expansion / Refinement / Probe
**Outcome focus:** [outcome from the OST]
**Trio:** [PM name] · [Designer name] · [Tech lead name]
**Recruit owner:** [Name]

## Recruit summary

| Field | Value |
|-------|-------|
| Segment | [...] |
| Sample size | [N] |
| Channel | [...] |
| Incentive | [...] |
| Status | Recruiting / Confirmed / Complete |

## Schedule

| Day | Time | Customer | Trio attending | Brief link |
|-----|------|----------|----------------|------------|
| Mon | 10:00 | [first name, segment] | All | [./brief-mon-1000.md] |
| Mon | 14:00 | [...] | PM, Designer | [...] |
| Wed | 09:30 | [...] | All | [...] |
| Wed | 13:00 | [...] | All | [...] |
| Fri | 11:00 | [...] | PM, Tech lead | [...] |

## Assumptions being probed this week

- [assumption-1 from assumption-test file] — [what we'd hear that supports / refutes]
- [assumption-2] — [...]

## Open opportunities being refined

- [opportunity from OST] — [what we want sharper signal on]

## Synthesis ritual

- **When:** Friday afternoon, 60 minutes
- **Who:** Trio + (optional) extended team
- **Output:** OST update + 1–2 lines into `discovery-readout` for the cycle
```

## Phase 6 — Run the synthesis ritual at end of week

Block 60 minutes Friday afternoon. The Trio walks through what they heard:

- New opportunities → add to OST
- Existing opportunity refinements → update the relevant entry
- Assumption signal → update the assumption-test file (status / notes)
- Surprises → flag in the readout

Then run `manfred-discovery:opportunity-solution-tree` to update the tree, and start the next week's plan.

## Manfred lens

- **`manfred-discovery:opportunity-solution-tree`** — both feeds in (which opportunities to probe) and out (what gets updated as a result)
- **`manfred-discovery:assumption-test`** — touchpoints often serve as the qualitative side of a test design
- **`manfred-discovery:discovery-readout`** — synthesis from the week feeds the next readout
- **`manfred-discovery:weekly`** — the orchestrator command that runs through this skill plus assumption-test plus readout
- **`manfred-discovery:discovery-rituals`** — sets up the recurring calendar holds for these touchpoints

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "We don't have time to recruit weekly" | Build the recruit pipeline once, then it's 2 hours a week, not 2 days. The PM does this — it's the job. |
| "Just the PM does the interviews — designer and tech lead can read the transcripts" | They can, but they won't make the same decisions. Trio symmetry is the whole point. Calendar holds, no exceptions. |
| "5 customers isn't enough" | 5 is the qualitative sweet spot. If you want quantitative signal, run an `assumption-test` with proper sample sizing. |
| "Customers from panels are fine" | They're fine for early validation of unfamiliar territory. For your own product, real users are 10x the signal. |
| "We'll skip the synthesis ritual this week" | Then the touchpoints didn't happen, decisions-wise. Synthesis is when learning enters the team. |
| "Story-based interviewing is too constraining" | It's the highest-signal form of interviewing for behavioural truth. The constraint is the point. |
| "We only need to talk to customers when we're working on a feature" | That's project research, not continuous discovery. Both are valuable; this skill is for the continuous mode. |

## Red flags — STOP

- About to plan a week with no Trio attendance → Stop. Either recruit fewer customers and get the Trio, or postpone the week.
- About to recruit "general users" with no specific segment → Stop. Segment first.
- About to skip the synthesis ritual → Stop. Without synthesis, the touchpoints don't enter the team's decision-making.
- About to use leading or hypothetical questions → Stop. Story-based interviewing only.
- About to plan touchpoints with no link to an outcome on the OST → Stop. What outcome is this serving?
- Recruit is "from panels" without a stated reason → Stop. Default is your own customers; panels need a justification.

## Tools used

- **Write**: `discovery/touchpoints/<YYYY>-W<week>.md` and per-customer brief files
- **Skills called**:
  - `manfred-discovery:opportunity-solution-tree` — update tree from the synthesis
  - `manfred-discovery:assumption-test` — when a touchpoint serves as qualitative signal for a test
  - `manfred-discovery:discovery-readout` — at end of cycle
- **Reference**: Teresa Torres, *Continuous Discovery Habits* (chapters on the Trio, story-based interviewing, building a recruit pipeline)
