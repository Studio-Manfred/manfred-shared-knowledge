---
name: cagan-risks
description: Use when assessing a feature idea or initiative against Marty Cagan's four product risks (value, usability, feasibility, viability). Triggers on "Cagan risks", "four risks", "value/usability/feasibility/viability", "risk profile this idea", "is this ready for build", "what should we test first", "smallest test for X risk", "discovery vs build". Produces a risk profile and a named cheapest-test for the highest risks. Refuses to rate without evidence.
---

# cagan-risks

Marty Cagan's four product risks, applied honestly. Refuses to rate vibes — asks for evidence first.

## Overview

Every feature idea has to retire four risks before build is the right answer:

- **Value** — will customers actually want this?
- **Usability** — can they figure out how to use it?
- **Feasibility** — can we build it with current tech, in the time we have?
- **Viability** — does it work for the wider business (legal, brand, commercial, ops)?

This skill rates each risk Low / Med / High and recommends the **cheapest specific test** that retires the highest-rated ones. It refuses to rate without evidence — vibes ratings are worse than no rating.

Source: Marty Cagan, *Inspired* and *Empowered* (SVPG). Continuous Discovery Habits (Teresa Torres) is the operational layer — see `manfred-discovery:opportunity-solution-tree` and `manfred-discovery:assumption-test` for what to do with the highest risks.

## When to use

- Someone says "we're thinking of building X — should we?"
- A `manfred-discovery:product-brief` reaches section 05 (Cagan risks) and needs deeper assessment
- An in-flight feature is going sideways and the team wants to pressure-test whether to keep going
- "What should we test first?" / "Which risk is highest?"

**Skip when:**

- The feature is already shipped — use `manfred-discovery:discovery-readout` to learn from it instead
- The risks are obviously all Low and stakes are tiny (a button colour change)
- Pure technical refactor with no customer-facing change

## Two principles drive everything

1. **Evidence before rating.** Don't put numbers on hunches. If you don't know the value-risk evidence, the answer is "we need to retire this risk first" — not "Medium probably".
2. **Test the riskiest assumption cheapest.** Each risk has a menu of specific tests, ordered by cost. Reach for the cheapest one that genuinely retires the risk. "Do user research" is not a test.

## Phase 1 — Pre-flight: gather evidence

Before rating anything, ask the user for evidence in each risk dimension. If they don't have it, that risk is High by default — and the test design becomes "get this evidence."

| Risk | What evidence are you looking for? |
|------|-----------------------------------|
| Value | Quantitative signal (drop-off rates, search volume, churn reasons), qualitative (interview themes, support ticket clusters, NPS verbatims), willingness-to-pay or willingness-to-switch data |
| Usability | Existing pattern (well-trodden) vs. novel interaction, prior usability test data, comparable products' patterns, complexity of the user's mental model |
| Feasibility | Tech stack fit, API/data dependencies, prior spike outcomes, engineering team's confidence (ask explicitly, don't assume) |
| Viability | Legal/GDPR review, brand fit, commercial model fit, ops impact, sales/CRM compatibility, support team load |

Example pre-flight questions:

- "What evidence do we have that customers want this? Drop-off data? Interview quotes? Or is this hypothesis-stage?"
- "What's the closest existing pattern? Have we usability-tested anything similar?"
- "Has engineering done a spike on this, or is feasibility a guess?"
- "Has legal/CRM/ops weighed in? Or are we assuming they'll be fine with it?"

If the answer to any of these is "no" or "haven't asked," the corresponding risk goes to High — and the cheapest test is "go ask."

**Red flag:** if the user pushes you to rate without evidence ("just give me your best guess"), refuse politely. Output the risk as **High — no evidence** and recommend the evidence-gathering test below.

## Phase 2 — Rate each risk

Only after Phase 1. For each risk, produce a single line:

```
[Risk name] — [Low/Med/High] — [one-sentence reason grounded in evidence from Phase 1]
```

Examples:

- **Value — Med** — Drop-off at signup is 38%, but we don't know if friction or value prop is the cause. (See test below.)
- **Usability — Low** — OAuth-style sign-in is a well-trodden pattern; users recognise it. Confirmed in three prior usability sessions.
- **Feasibility — High** — No spike done on Apple's private relay email handling for our loyalty model. Engineering rated confidence at 4/10.
- **Viability — High** — Legal hasn't reviewed; loyalty programme depends on attributable email which Apple hides. CRM ops has not signed off.

If the rating is Low with no specific evidence — reject your own answer and re-rate as Med or High with "no evidence" as the note.

## Phase 3 — Pick the cheapest test that retires each high-rated risk

For each High (and ideally each Med) risk, name a **specific cheapest test** from this menu. Cost ascending.

### Value risk — cheapest tests first

1. **Customer interview cluster (5–8)** — talk to recent users in the relevant segment about the underlying problem. Listen for whether the problem itself shows up unprompted. Cost: 1 week.
2. **Fake-door / Smoke test** — add the proposed entry point (button, link) to the existing surface; on click, capture intent and fall through. Compare CTR to baseline. Cost: 2–5 days build + 1 week run.
3. **Wizard-of-Oz** — manually deliver the value behind the curtain for a small cohort (e.g. send the personalised recommendation by email instead of building the algorithm). Cost: 1–2 weeks.
4. **Concierge MVP** — do the work by hand for one customer end-to-end. Cost: a few hours per customer; high signal.
5. **Landing page test** — sign-up rate against a paid traffic source. Cost: ad spend + a few days.

### Usability risk — cheapest tests first

1. **Pattern audit** — find 3 comparable products doing the same thing; compare their solutions. Cost: 2 hours.
2. **Click-test on a static prototype** — Maze, Useberry, or similar. Cost: 1–2 days build + 24h run.
3. **Moderated 5-user usability test** on a low-fi prototype. Cost: 1 week incl. recruit.
4. **Tree test** for IA/navigation questions. Cost: 1–2 days.

### Feasibility risk — cheapest tests first

1. **Direct conversation with engineering tech lead** (30 min) — what's their confidence? What would they need to spike? Cost: 30 min. Often resolves the rating.
2. **Engineering spike** — timeboxed (1–5 days) prototype to confirm the unknown. Define a success criterion before starting.
3. **Architecture review** — bring 2–3 engineers and walk the integration path. Cost: 2 hours.

### Viability risk — cheapest tests first

1. **Stakeholder working session** (60–90 min) — get legal / CRM / ops / brand in a room, walk the proposal, ask "does this work for you? What would you need to say yes?" Cost: 90 min.
2. **Specific written question to the stakeholder** — sometimes faster than scheduling. Cost: 1 day for the answer.
3. **Compliance review request** (formal) — when the risk is actually a compliance question. Cost: 1–4 weeks depending on the org.

If the cheapest test for a risk doesn't retire it, escalate to the next one. Don't run two tests when one would do.

## Phase 4 — Output the risk profile

Save the output as `discovery-reports/cagan-risks-<initiative-slug>-<YYYY-MM-DD>.md` **when the assessment is part of a cycle** — running discovery, kicking off a brief, doing a risk-check command. For one-off advisory consultations (someone asks you a quick risk question in passing) **offer the file save**, don't presume it. Format:

```markdown
# Cagan risk profile — [Initiative name]

**Date:** [YYYY-MM-DD]
**Assessed by:** [Name(s)]
**Status:** Pre-build assessment

## Evidence summary

| Risk | Evidence available |
|------|-------------------|
| Value | [what we have / what we don't] |
| Usability | [...] |
| Feasibility | [...] |
| Viability | [...] |

## Risk ratings

| Risk | Rating | Reason |
|------|--------|--------|
| Value | [Low/Med/High] | [one-line, evidence-grounded] |
| Usability | [Low/Med/High] | [one-line] |
| Feasibility | [Low/Med/High] | [one-line] |
| Viability | [Low/Med/High] | [one-line] |

## Cheapest tests recommended

For each High (and Med worth retiring):

### [Risk name] — [Test name]
- **What:** [one-line description]
- **Why this test:** [what it specifically retires]
- **Cost:** [time + people]
- **Owner:** [who runs it]
- **Definition of done:** [the answer that retires the risk]

## Recommendation

[One paragraph. Build / discovery / park, with one-line reason. If any risk is High and the recommendation is build, name the contradiction explicitly.]
```

If the initiative is linked to a Linear ticket (branch matches `[A-Z]+-\d+`), post a summary as a comment on the ticket using `mcp__linear-server__save_comment` after resolving the issue id with `mcp__linear-server__get_issue`. Pattern reference: `manfred-dev:test-my-code` Linear update section.

## Manfred lens

This skill maps directly into the product brief and Torres OST:

- **`manfred-discovery:product-brief`** — section 05 (Product Risk Assessment) is exactly this output. When facilitating a brief, run this skill for each risk that comes up "High" with a vague reason.
- **`manfred-discovery:assumption-test`** — once a High risk's cheapest-test is named here, hand off to `assumption-test` for the experiment design (hypothesis, success criteria, timebox).
- **`manfred-discovery:opportunity-solution-tree`** — each High risk usually maps to an assumption that lives below an opportunity in the OST. The OST is where you track what's been retired vs. still open.

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "Just give me your gut on the ratings" | Vibes ratings are worse than no rating — they create false confidence. Refuse and ask for evidence. |
| "I'm in a hurry — meeting in 10 / sprint planning starts now" | A wrong rating in 10 minutes is worse than no rating. Counter-offer: 2 minutes of pre-flight questions. The team brings back evidence after the meeting; you produce the profile then. |
| "But Apple/Stripe/this-platform-thing is a known fact, can't you rate viability on that?" | Yes — platform-property facts (e.g. Apple's private relay hides email, Stripe doesn't accept PayPal) ARE evidence. Single-risk ratings are OK when the evidence is structural and public. Don't extend to "but everyone knows our customers want X" — that's not evidence. |
| "Value risk is Low because we know our customers" | "We know our customers" isn't evidence. What's the data? If none — Value is High by default. |
| "Feasibility is Low, the engineers will figure it out" | Have the engineers said so? In what timebox? With what spike done? If not — Feasibility is Med or High. |
| "Viability is Low, legal will be fine" | If you haven't asked legal — Viability is High. The cheapest test is the one-hour conversation. |
| "We can run all four tests in parallel" | Maybe — if cost allows. But often one test outcome (e.g. viability dies) makes the others moot. Sequence by cost AND by how much each retires the others. |
| "The team has decided to build, so let's just frame the risks" | Then this isn't a brief, it's PR. Push back: name the riskiest assumption, name the test, give the team the chance to course-correct. |
| "Do more user research" is the recommendation | "User research" isn't a test. Name the technique — interview cluster, fake-door, click-test, concierge MVP. |
| "Low risk" with no note | Reject your own answer. Re-rate or add the evidence note. |

## Red flags — STOP

- About to rate a risk without asking for evidence first → Stop. Pre-flight first.
- About to recommend "do more research" without naming a specific technique → Stop. Pick from the menu.
- About to rate a risk Low with no note → Stop. Either find the evidence or rate Med/High with "no evidence."
- About to recommend "build" with one or more risks at High → Stop. Name the contradiction. Recommend retiring the High first.
- About to skip the viability risk because "the team isn't worried" → Stop. Viability is the most-skipped risk and the most likely to kill projects late. Force the conversation.
- About to dump all four ratings without ranking which to retire first → Stop. Sequence by cost-of-test and dependency.

## Tools used

- **Write**: `discovery-reports/cagan-risks-<slug>-<date>.md`
- **MCP** (when ticket linked): `mcp__linear-server__get_issue`, `mcp__linear-server__save_comment`
- **Skills called next**:
  - `manfred-discovery:assumption-test` for each High risk's cheapest test
  - `manfred-discovery:opportunity-solution-tree` to track what's been retired
  - `manfred-discovery:product-brief` (section 05 round-trip)
- **Reference**: Marty Cagan, *Inspired* (chapters on product risk and discovery techniques), *Empowered* (chapters on product teams and continuous discovery)
