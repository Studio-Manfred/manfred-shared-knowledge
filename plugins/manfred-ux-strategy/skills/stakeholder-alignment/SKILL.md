---
name: stakeholder-alignment
description: Use when navigating stakeholder landscapes and creating alignment around design decisions — anyone says "stakeholder map", "RACI", "decision framework", "communication plan", "feedback protocol", "who decides what", "how do we handle conflicting feedback", "stakeholder management", "kickoff with stakeholders". Manfred-flavoured: decision rights before conflict, proactive communication, document the why.
---

# stakeholder-alignment

Stakeholder alignment is the part of a project that's invisible when it works and unrecoverable when it doesn't. Done right, the team knows who decides what before the disagreement happens. Done wrong, every design review re-litigates the same questions and decisions take three rounds longer than they should.

Manfred treats stakeholder alignment as **infrastructure**: decided early, documented, revisited explicitly when context changes.

## Overview

Five artifacts. Pick what the engagement needs — not every project needs all five.

1. **Stakeholder map** — who's in scope, what's their influence and interest
2. **RACI matrix** — who's Responsible, Accountable, Consulted, Informed per decision
3. **Decision framework** — what kinds of decisions need what kinds of input
4. **Communication plan** — who hears what, when, through which channel
5. **Feedback protocol** — how feedback is collected, prioritised, and resolved

Plus the most important rule: **decision rights are decided before conflict, not during.** A team that figures out "who decides" in the moment of disagreement decides poorly.

## When to use

- Kickoff of a new design engagement — before work starts
- Mid-project when stakeholder dynamics are creating friction
- After a decision went badly because the wrong person made it (or the right person wasn't asked)
- Onboarding a new stakeholder mid-engagement
- Setting up alignment for a recurring program (quarterly planning, design reviews)

**Skip when:**

- Solo work with no stakeholders (rare; usually there's at least one)
- The team already has clear decision rights and the project is on track (don't manufacture process)
- The user wants leadership / executive coaching (different skill, different domain)

## Pre-flight

Ask:

- Who's the convening team? (PM, designer, tech lead — the Manfred Trio.)
- Who else has influence over decisions in this project? (Be specific — names, not "leadership".)
- What's gone wrong in past projects? (Past failure surfaces real risks better than abstract planning.)
- Are there stakeholders who *should* be involved but currently aren't? (Often the most useful question.)
- What's the project size? (Small projects need a 1-page alignment doc, not five artifacts.)

If past failure was "stakeholder X kept changing their mind" or "design got overruled by Y at the last minute", those are the patterns the alignment work needs to prevent. Design the artifacts around them.

## The hard rules

| Rule | What it means |
|---|---|
| **Decision rights before conflict** | Decide who decides at kickoff, not during the disagreement. The decision-rights doc gets agreed and signed before work starts. |
| **Document the why** | Every significant decision gets recorded with reasoning. Reasoning beats minutes — minutes go stale, reasoning answers "why did we choose this?" months later. |
| **Communicate proactively** | Stakeholders surprised by progress become stakeholders blocking progress. Cadence + content + channel decided up front. |
| **Map at kickoff, revisit at milestones** | Stakeholder maps go stale in weeks. Revisit at every milestone — who joined, who left, who shifted influence. |
| **Surface missing stakeholders** | The stakeholder you didn't invite is the stakeholder who derails the work in week 6. Ask "who else should be in this conversation?" early. |
| **Feedback has a format** | Free-form Slack feedback is unactionable. Define the format ("specific, with screenshot, with proposed alternative") so feedback can be processed. |
| **Conflicts get a decider** | Every decision has someone who breaks ties. Without a named decider, conflict cycles forever. |

## The five artifacts

### 1. Stakeholder map

Plot stakeholders on **influence × interest**:

```
                       INTEREST
                       Low      High
                       ─────    ─────
        High    ┌──────────┬──────────┐
                │  Keep    │  Manage  │
        INFLUENCE  satisfied│  closely │
                ├──────────┼──────────┤
        Low     │ Monitor  │   Keep   │
                │          │ informed │
                └──────────┴──────────┘
```

For each stakeholder:

```markdown
| Name / role | Influence (H/M/L) | Interest (H/M/L) | Quadrant | Engagement strategy |
|---|---|---|---|---|
| Anna (CEO) | H | M | Keep satisfied | Monthly summary, escalation point |
| David (PM) | H | H | Manage closely | Weekly working session |
| Compliance lead | M | H | Keep informed | Bi-weekly briefing, sign-off on KYC flow |
| Engineering manager | H | L | Keep satisfied | Bi-weekly status, deep dive on technical decisions |
| Customer support lead | L | H | Keep informed | Monthly research share, surface support patterns |
```

### 2. RACI matrix

For each significant decision in the project, assign:

- **R**esponsible — does the work
- **A**ccountable — owns the outcome (one person only)
- **C**onsulted — input gathered before decision
- **I**nformed — told after the decision

```markdown
| Decision | PM (David) | Designer (Lina) | Tech lead (Mo) | CEO (Anna) | Compliance | Support |
|---|---|---|---|---|---|---|
| Visual direction (mood, palette use) | A | R | I | C | — | — |
| Information architecture | A | R | C | I | C | C |
| Component API decisions | I | C | A R | — | — | — |
| KYC flow specifics | C | R | C | — | A | C |
| Launch date | A R | C | C | C | C | I |
| Pricing changes | I | I | I | A R | — | C |
```

One **A** per row. Multiple **A**s = no Accountable = decision drift.

### 3. Decision framework

Different decisions need different process:

```markdown
| Decision type | Process | Time | Decider | Examples |
|---|---|---|---|---|
| **Reversible / low-stakes** | One person decides, informs after | Hours | Designer (or owner) | Microcopy choices, minor visual tweaks |
| **Reversible / high-stakes** | Trio agrees | Days | Trio (PM + Designer + Tech) | Component API, navigation pattern |
| **Irreversible / low-stakes** | Trio + relevant stakeholder | Days | Trio | Naming a feature publicly |
| **Irreversible / high-stakes** | Trio + Accountable per RACI | Weeks | Per RACI | Launch timing, pricing, scope changes |
| **Strategic** | Workshop with full stakeholder set | Weeks | CEO | Vision, positioning, market entry |
```

### 4. Communication plan

```markdown
| Audience | What | When | Channel | Owner |
|---|---|---|---|---|
| Trio (PM + Designer + Tech) | Daily working updates | Daily | Slack thread | Self-organising |
| Compliance lead | KYC milestone updates | Bi-weekly | 30-min call | PM |
| CEO + leadership | Project summary | Monthly | Email + 30-min call | PM |
| Customer support | Research findings, design changes | Monthly | Async write-up + optional Q&A | Designer |
| Engineering team (broader) | Technical decisions, dependencies | Per release | Internal blog post | Tech lead |
| Whole company | Launch | Launch + 1 wk after | All-hands + email | PM + leadership |
```

### 5. Feedback protocol

How feedback gets given, processed, and resolved:

```markdown
## Feedback format

Specific, evidenced, with proposed alternative where possible.

Bad: "I don't like this colour"
Good: "The yellow CTA against the beige background fails contrast (2.8:1). Suggest using the brand-blue CTA per the design system."

## Feedback channels

| Type | Channel | Cadence | Response time |
|---|---|---|---|
| In-flight design feedback | Figma comments | Continuous | 1 working day |
| Async written critique | Slack design-review channel | Per milestone | 2 working days |
| Live design review | Bi-weekly 60-min call | Bi-weekly | n/a |
| Escalations / urgent | Direct DM to PM | As needed | Same day |

## Feedback prioritisation

- **Block-merge** — accessibility, brand violation, legal risk → fix before next milestone
- **High** — usability concern, divergence from spec → discuss in next design review
- **Medium** — preference, alternative approach → backlog, address opportunistically
- **Low** — taste, micro-polish → evaluate at end of project

## Feedback resolution

- Resolved in Figma comments → mark resolved, link to commit / change
- Discussed in design review → minutes posted within 1 day, decisions noted
- Escalated → decision and rationale documented in project log

## When feedback conflicts

When two stakeholders give conflicting feedback:
1. Designer + PM surface the conflict
2. Reference RACI to identify the Accountable for that decision
3. Schedule a 30-min decision call with the Accountable + relevant Cs
4. Decision recorded with rationale; non-winning stakeholder informed of why
```

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Our team's small, we don't need a RACI" | Even 3 people on a decision benefit from named accountability. RACI for small teams is one paragraph, not a spreadsheet. |
| "Decision rights will sort themselves out" | They sort themselves out by whoever pushes hardest. Decide upfront or watch the loudest voice win. |
| "Stakeholders don't want to read these docs" | Stakeholders want to be informed at the right moment in the right way. The doc protects them from being surprised. |
| "We can't control what stakeholders feed back" | Format isn't control — it's a request. Most stakeholders will use the format if you make it easy. The ones who won't are signal. |
| "Communication plan feels corporate for our team" | A 1-page communication plan beats six "wait, why didn't I know about this" Slack threads. Light is fine; absent is not. |
| "We'll add the missing stakeholder if it comes up" | By "comes up" you mean "they block the project in week 6". Map at kickoff. |

## Manfred lens

Stakeholder alignment touches **viability risk** (Cagan) — the project doesn't ship if internal stakeholders can't agree on what shipped means. It also gates the **discovery rituals** (`manfred-discovery:discovery-rituals`) — research insights die when the team doesn't have a shared frame for who acts on them.

Critical & ethical (principle 6): stakeholder dynamics are a vector for design ethics. A stakeholder asking for an attention-capturing pattern, a dark feature flag, a pricing change that targets the vulnerable — these get pushed through by stakeholder power, not by user evidence. Decision rights and feedback protocols should explicitly include "ethics check" as a stop. If the Trio surfaces an ethics concern, it goes to the Accountable; if the Accountable overrules, it gets documented, not silently shipped.

## Cross-references

- `manfred-discovery:discovery-rituals` — research findings need a stakeholder map to land
- `manfred-discovery:product-brief` — Section 02 (Strategic Alignment) cites the stakeholder map
- `manfred-ux-strategy:design-brief` — Section 1 (Project Overview) names stakeholders
- `manfred-design-research:summarize-interview` — research outputs need to reach the right stakeholders per the comms plan
- `manfred-discovery:discovery-readout` — the readout uses the comms plan to land insights

## Output format

Save the alignment doc to `discovery/alignment/<engagement-slug>-<YYYY-MM-DD>.md`.

Include the artifacts the engagement needs — for a small project, often just stakeholder map + RACI + light comms plan (1–2 pages). For a large project, all five artifacts (4–6 pages).

Sign-off line at the bottom: "Agreed by [PM / Designer / Tech / Accountable per RACI rows]". Without sign-off, the doc isn't an alignment doc — it's a draft.

## Tools used

- `Read` — prior alignment docs, project briefs
- `Write` — produce the artifact(s)
- `manfred-ux-strategy:design-brief` — for the brief that the alignment doc supports
- `manfred-discovery:discovery-rituals` — for ongoing comms cadence

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
