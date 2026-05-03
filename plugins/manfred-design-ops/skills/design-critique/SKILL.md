---
name: design-critique
description: Use when running or facilitating a design critique — anyone says "design crit", "design review feedback", "let's critique this", "feedback on my design", "give me feedback", "design feedback session", "desk critique", "team critique". Manfred-flavoured: Trio attendance, structured feedback formats, separates exploration from refinement.
---

# design-critique

A design critique is feedback on the work, not on the person, with action items the designer leaves with. Done well, it sharpens thinking; done badly, it produces "design by committee" or hurt feelings — neither helps the user.

Manfred runs critiques as a ritual, not an event. Trio attends (PM + designer + tech lead). Feedback is structured. Action items are captured.

## Overview

Four critique modes — pick the right one for the work's stage:

| Mode | When | Format | Time |
|---|---|---|---|
| **Desk crit** | Mid-flow, quick check | 1-on-1, informal, async OK | 10 min |
| **Team crit** | Milestone moment | Trio + 1-2 peers, structured | 60 min |
| **Cross-team crit** | Need fresh eyes | Designers from outside the project | 60 min |
| **Stakeholder review** | Decision-focused | Approver + Trio | 60–90 min |

The mode shapes the format. A team crit run as a stakeholder review (everyone deferring to one decider) loses the value of the team. A stakeholder review run as a team crit (open feedback round, no decider) loses the decision.

## When to use

- A designer is stuck and needs another pair of eyes
- A milestone moment (concept, mid-design, pre-handoff) needs structured feedback
- The team's design quality is drifting — critique as a recurring ritual catches drift
- A stakeholder needs to approve / reject a direction
- Cross-team work needs alignment

**Skip when:**

- The designer wants validation, not feedback (different conversation — and pushy "this is great!" critiques produce drift)
- The work is too early to critique productively (exploring 12 directions — give it time, then critique the top 2)
- The work is about to ship and feedback can't be acted on (critique earlier, or accept the timing constraint)

## Pre-flight (designer's prep)

Before walking into a critique:

- **What's the goal?** What problem is this design solving?
- **What stage?** Exploration, refinement, polishing — different feedback for each
- **What feedback do I want?** Layout? Flow? Copy? Everything? Naming this saves 30 minutes of misaligned input
- **What's already decided?** Out-of-scope topics get parked, not relitigated
- **Who's in the room?** The Trio? Plus stakeholders? Designers from outside?

If the designer hasn't done this prep, the critique drifts. Send the questions before the meeting.

## The hard rules

| Rule | What it means |
|---|---|
| **Critique the work, not the person** | "This layout pushes the CTA below the fold" not "you should have made the CTA more prominent". The first invites discussion; the second invites defensiveness. |
| **Tie feedback to user need or goal** | "This violates the user's mental model" beats "I would do it differently". Personal preference is not feedback. |
| **Separate exploration from refinement** | Exploration crit asks "are these the right directions?" Refinement crit asks "is this direction landing?". Mixing them confuses both. |
| **Trio attends** | PM + designer + tech lead. Not designer-solo, not designer + designer. Critique without the Trio loses the cross-functional input that's most useful. |
| **Action items captured + owned** | Every critique ends with: list of changes, owner per change, due date. No owner = no change. |
| **Time-boxed** | A 60-min critique that runs 90 min is a 60-min critique with 30 min of friction. Hold the time. |
| **Designer leads, doesn't defend** | Designer presents, asks for the feedback they want, captures responses. Defending every choice signals "I don't actually want feedback" and shuts the room down. |

## The flow (60-min team crit)

### 0–5 min — Frame
Designer states: goal, stage, what feedback is wanted. Explicitly: "Today I want feedback on [X]. I'm not looking for feedback on [Y] — those are decided."

### 5–10 min — Present
Designer walks the work. No questions, no commentary — just the walkthrough.

### 10–15 min — Clarify
Audience asks questions to understand, not judge. ("How does this respond on mobile?" "What's the empty state here?") Designer answers briefly.

### 15–35 min — Feedback rounds (structured)

Use the four-frame format — every comment fits one:

- **"I notice…"** — observation, not judgment ("I notice the primary CTA is below the fold on mobile")
- **"I wonder…"** — question or exploration ("I wonder if users would scroll past it")
- **"What if…"** — suggestion or alternative ("What if we sticky the CTA on mobile?")
- **"I think… because…"** — opinion with rationale ("I think this needs a sticky CTA because mobile users typically scroll-and-decide")

Forbid: "I just don't like it." "It feels wrong." "I would do it differently." Without rationale, these aren't feedback — they're noise.

### 35–50 min — Discuss
Open conversation on key tensions. Disagreements get aired, not resolved on the spot — the designer takes the input and decides later.

### 50–60 min — Capture + close

- Designer summarises top 3 takeaways
- Action items list with owners + due dates
- Decisions parked for later (with deadline for resolution)
- Follow-up critique scheduled if needed

## Common rationalisations

| Excuse | Reality |
|---|---|
| "We don't need a structured format, the team gets along" | Liking each other isn't critique. Structure isn't formality — it's what makes feedback usable. |
| "Designer should defend every choice — shows confidence" | Defending shuts the room down. Confidence is asking for feedback you don't want to hear. |
| "We'll capture action items in our heads" | "In our heads" = nobody owns it. Write them down. Owners + dates. |
| "Cross-team crit is overkill, our team knows the work best" | Knowing the work too well is the problem — fresh eyes catch the assumptions you've stopped seeing. |
| "Stakeholder review and team crit are the same thing" | They're not. Stakeholder review needs a decider. Team crit needs the team. Mixing them produces design-by-committee. |
| "Critique should be positive — don't crush morale" | Vague positivity drifts to bad work. Specific, work-focused critique builds craft. |

## Red flags — STOP

- About to critique without the designer naming what feedback they want
- About to use "I just don't like it" or "it feels wrong" without rationale
- Critique going past time-box
- Designer defending every choice instead of capturing input
- No action items captured
- Personal preference being argued as if it's user need
- The Trio isn't in the room (and the work is past the desk-crit stage)

## Manfred lens

Critiques touch **usability risk** (Cagan) — they're the team's structured check that the design serves the user. They also gate the **discovery rituals** (`manfred-discovery:discovery-rituals`) — research findings need a critique moment to land in design decisions.

Critical & ethical (principle 6): critique includes the "what does this design do in the world?" question. If the design optimises for the team's metric at the user's expense, critique is the moment to surface it — before the design goes to handoff.

## Cross-references

- `manfred-design-ops:design-review-process` — for the broader review gates that critiques fit into
- `manfred-design-ops:design-qa-checklist` — for pre-handoff checklist (different artifact, related purpose)
- `manfred-design-research:user-archetype` — for grounding "user need" arguments in real evidence
- `manfred-discovery:discovery-rituals` — critique is a discovery ritual

## Tools used

- `Read` — designer's prior work, Figma context
- `Write` — capture action items, save to project log
- `manfred-design-ops:design-review-process` — for the gate this critique serves
- `manfred-design-systems:a11y-design` — for accessibility-specific critique input

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
