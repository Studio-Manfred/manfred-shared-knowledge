---
name: experience-map
description: Use when mapping the full ecosystem of user touchpoints across phases, channels, and time — anyone says "experience map", "ecosystem map", "service blueprint", "touchpoint map", "omnichannel audit", "end-to-end experience", "where do users hit our brand", "service design map". Manfred-flavoured: research-grounded, current-state before future-state, ties findings to opportunities.
---

# experience-map

A journey map shows one user moving through one product. An experience map shows the whole ecosystem — every touchpoint, every channel, every gap between them. It's the macro view designers need when the product is one part of a bigger story (multi-channel, service-based, omnichannel).

Done well, an experience map surfaces the cross-team hand-offs nobody owns — and the moments where users fall off because the system isn't shaped around them.

## Overview

The map sits on two axes:

- **Horizontal (phases)** — awareness → evaluation → onboarding → regular use → advanced use → advocacy / departure
- **Vertical (layers)** — what the user does, what touchpoints they hit, what channels, how they feel, where it breaks, where the gaps are

Plus an "ecosystem relationships" layer showing how touchpoints connect (or don't) — data flow, human-to-automated handoffs, branded vs unbranded surfaces.

Manfred maps **current state before future state**. You can't redesign what you haven't seen.

## When to use

- New multi-channel product or service (web + mobile + email + support + in-person)
- Cross-team alignment when nobody can see the whole picture
- Identifying gaps in the ecosystem (touchpoints that should exist but don't)
- Auditing handoffs between teams (marketing → product → support, or design → engineering → ops)
- Setting up a north-star vision (`manfred-ux-strategy:north-star-vision`) that needs an honest current-state baseline

**Skip when:**

- The user wants a single-flow journey map (use `manfred-design-research:journey-map` — different scope, same toolkit)
- The product genuinely lives in one channel only (an experience map is overkill — a journey map suffices)
- The user wants a service blueprint (related but adds backstage / processes / systems — different artifact, same family)

## Pre-flight

Ask:

- What's the scope? (Whole product? One user segment? One outcome — e.g. "first 90 days"?)
- Is the audience for this map internal alignment, client briefing, or design input?
- Do we have research to ground the map, or is it analyst guesses? (If guesses — say so explicitly. Maps full of "we think users feel…" are decoration.)
- Current state, future state, or both?

If the answer is "we don't have research", strongly recommend running `manfred-design-research:summarize-interview` + `manfred-design-research:affinity-diagram` first, or pulling existing research from `manfred-design-research:user-archetype` outputs. Maps without grounding mislead more than they inform.

## The hard rules

| Rule | What it means |
|---|---|
| **Current state before future state** | Map what is, then map what could be. A future-state map without a current-state baseline is wishful thinking. |
| **Research-grounded, not assumption-padded** | Every emotion, pain point, opportunity cell cites evidence (research session, ticket, NPS verbatim). Cells with no citation get marked "assumption — to test". |
| **Ecosystem includes physical + analog** | Phone calls to support, paper invoices, in-person handoffs, third-party services — they're touchpoints too. |
| **Branded + unbranded** | The Google search that surfaces your product, the third-party review site, the support thread on Reddit — all touchpoints, all in scope. |
| **Cross-team handoffs are first-class** | Where the user moves from one team's surface to another's (marketing → product → support → CSM) — these are the highest-failure moments. Mark them, name the owner. |
| **Tied to opportunities, not just observations** | Every pain point gets paired with a candidate opportunity (or "no opportunity yet, needs research"). Observations without pairs are decoration. |

## The flow

### Step 1 — Scope the map

Define:

- **User segment(s)** — which users does this map cover? Use real archetypes (`manfred-design-research:user-archetype`).
- **Time scope** — first interaction → first month? Full lifecycle including departure?
- **Channels in scope** — web, mobile, email, SMS, support, social, in-person, third-party, physical mail.

Lock scope before mapping. Maps that try to cover "everything for everyone" become unreadable.

### Step 2 — Define phases

Standard arc for most products:

1. **Awareness** — user first hears about the product / problem
2. **Evaluation** — user assesses fit
3. **Conversion / signup** — user commits
4. **Onboarding** — first run, first value
5. **Regular use** — habit / value loop
6. **Advanced use** — power features, expansion
7. **Advocacy** — recommendation, referral
8. **Departure / churn** — paused, downgraded, left (often skipped — don't)

Adjust phases for the product. Some products have no "advanced use" (transactional). Some have multiple "regular use" patterns (B2B with multiple personas).

### Step 3 — Build the matrix

A markdown table per phase, layered vertically:

```markdown
## Phase: Onboarding (Day 1–7)

| Layer | Detail | Evidence |
|---|---|---|
| **User actions** | Downloads app, opens, hits sign-up wall | Research session 2026-04-12, n=8 |
| **Touchpoints** | App store listing, app onboarding screens, welcome email, support FAQ | Analytics: 73% open welcome email within 24h |
| **Channels** | Mobile app + email + occasionally web | — |
| **Emotions** | Curious → frustrated at KYC wait → relieved when account opens | Verbatims: "felt like applying for a mortgage" |
| **Pain points** | KYC takes 4–48 hours with no progress signal | Support ticket pattern: 230 tickets in last 30 days |
| **Opportunities** | Real-time KYC progress + estimated wait time | (testable via `manfred-discovery:assumption-test`) |
| **Cross-team handoff** | Onboarding (product) → KYC (compliance) → Support (CS) — three teams, no shared view | Owner: nobody currently |
```

Repeat per phase. Phases without a clear pain point can be tighter; phases with concentrated friction get more rows.

### Step 4 — Ecosystem relationships layer

Below the phase matrix, show **how touchpoints connect**:

```markdown
## Ecosystem relationships

### Data flow
- App → backend KYC service → Support CRM (manual sync, daily batch — lag is felt by user)
- Marketing CRM → Product analytics (one-way; product doesn't push back)

### Human-to-automated handoffs
- Support chat: bot first, escalates to human on keywords ("frustrated", "cancel", "complaint")
- KYC: fully automated for 60% of cases; 40% manual review by compliance team

### Branded ↔ unbranded
- App store listing (branded) ← organic search (unbranded) ← Reddit threads (unbranded, often negative)
- Press coverage (semi-branded) → app downloads (branded surface)

### Identified gaps
- No system view of the user spans Product + Support + Compliance — each team sees a slice
- Reddit and Trustpilot are real touchpoints with no Manfred presence; complaints there are invisible internally
```

### Step 5 — Synthesis

Three outputs from the map:

1. **Top friction moments (3–5).** The phases / handoffs where users fall off, get frustrated, or give up. Specific, evidenced.
2. **Opportunity map.** Each friction moment paired with a candidate opportunity. Feed into `manfred-discovery:opportunity-solution-tree`.
3. **Cross-team ownership gaps.** Touchpoints / handoffs with no clear owner. Surface these to leadership — they're often where the biggest wins live, and where nobody currently has a remit to act.

## Output format

Save to `discovery/experience-maps/<scope-slug>-<YYYY-MM-DD>.md`:

```markdown
# Experience map: <scope>

**Date**: YYYY-MM-DD
**Scope**: [user segment, time horizon, channels]
**Audience**: [internal alignment | client briefing | design input]
**State**: current | future
**Evidence base**: [research sources cited]

## Summary
[3–5 sentences. Top 3 friction moments. Top 3 opportunities. Top 1 ownership gap.]

## Per-phase matrix
[The phase-by-phase tables from Step 3]

## Ecosystem relationships
[The relationships layer from Step 4]

## Synthesis
- Top friction moments
- Opportunity map (paired)
- Ownership gaps

## Limitations
[What this map didn't cover; what additional research would sharpen it]
```

## Common rationalisations

| Excuse | Reality |
|---|---|
| "We don't have research, but we have analyst experience" | Analyst experience is hypothesis, not evidence. Map with what you have, mark unevidenced cells "assumption — to test", run discovery to fill gaps. |
| "We don't need to map departure, our churn is fine" | Departure is where the most honest research happens. Skipping it produces over-optimistic maps. |
| "Future state map first, current state can wait" | Future state without current state is wishful thinking. The current-state map *is* the case for change. |
| "Touchpoints we don't own (Reddit, Trustpilot) aren't relevant" | They're touchpoints. The user reads them. They shape the brand. Map them; even if you can't act, you can listen. |
| "Cross-team handoffs are HR's problem" | Cross-team handoffs are user experience problems first. The fact that no team owns the seam *is* the design issue. |
| "An experience map for one product is overkill" | If the product spans 4+ touchpoints in 3+ channels with 2+ teams, an experience map pays for itself. If it doesn't, use `manfred-design-research:journey-map` instead. |

## Manfred lens

Experience maps touch **value risk** (Cagan) — across the ecosystem, where do users get value, where do they bounce? They're the input for **opportunity-solution tree** work (`manfred-discovery:opportunity-solution-tree`) — every friction moment becomes a candidate opportunity.

Cross-references:

- `manfred-design-research:journey-map` — single-product flow; experience map zooms out
- `manfred-design-research:user-archetype` — archetypes are the subjects of the map
- `manfred-design-research:affinity-diagram` — synthesis input often comes from here
- `manfred-discovery:opportunity-solution-tree` — friction moments feed opportunities
- `manfred-discovery:assumption-test` — every "candidate opportunity" becomes an assumption to test before building

## Tools used

- `Read` — research outputs, archetypes, prior maps
- `Write` — produce the map
- `manfred-design-research:summarize-interview` — for grounding research
- `manfred-design-research:user-archetype` — for the user segment
- `manfred-discovery:opportunity-solution-tree` — for the synthesis layer

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
