---
name: assumption-test
description: Use when designing the cheapest test that retires a single assumption — Teresa Torres / Marty Cagan style. Triggers on "assumption test", "test this assumption", "what's the riskiest assumption", "smallest test we can run", "experiment design", "fake-door test", "wizard of oz", "concierge test", "validate this idea", "discovery experiment". Produces a one-page test design — hypothesis, method, success criteria, timebox, owner.
---

# assumption-test

The smallest test that genuinely retires one assumption. Not "do user research" — a specific, named technique with a definition of done.

## Overview

Assumption testing is the operational layer of continuous discovery. Each High-rated risk (`manfred-discovery:cagan-risks`) and each pursued solution on the OST (`manfred-discovery:opportunity-solution-tree`) carries one or more assumptions that must be true for it to work. This skill designs the cheapest test that retires the riskiest assumption — and only that one assumption.

A good assumption test answers a yes/no question. It doesn't "explore" — it kills or confirms. If your test can come back inconclusive, redesign it.

Source: Teresa Torres (*Continuous Discovery Habits*) on assumption mapping; Marty Cagan (*Inspired*) on discovery techniques. Lean Startup-adjacent but more disciplined about scope: one assumption per test.

## When to use

- A `manfred-discovery:cagan-risks` profile names a High risk and a "cheapest test" candidate
- A solution on the OST has a riskiest assumption flagged — you need to design the experiment
- "What's the smallest thing we can do this week to find out X?"
- A team is about to commit to a build — you want to retire one risk first

**Skip when:**

- The assumption is already retired (don't re-test for comfort)
- You're picking between many possible assumptions to test — use `manfred-discovery:opportunity-solution-tree` to pick first, then come back here
- The question is "is this worth doing at all" — use `manfred-discovery:cagan-risks` first to identify the right assumption to test

## Two principles drive everything

1. **One assumption per test.** Tests that try to validate "the whole solution" answer nothing clearly. Pick one assumption — usually value, usability, feasibility, or viability flavored — and design the test around just that.
2. **Define the answer that retires the risk.** Before you run anything, write down: "If we see X, the assumption is supported. If we see Y, it's refuted." If you can't write that line, the test is wrong.

## Phase 1 — Surface the assumption

Ask:

- "What's the single assumption we're testing?" If the answer is a sentence with multiple clauses ("customers will want this AND will pay for it AND will renew"), pull out the *riskiest* clause — usually the first thing that, if false, kills the rest.
- "Which Cagan risk does this assumption sit under — value, usability, feasibility, or viability?" Knowing this picks the technique menu.
- "What evidence do we already have on this?" If there's prior data, the test should target the gap, not redo what's known.

State the assumption in this exact form:

> "We assume that [target audience] will [behaviour] when we [proposed thing], because [reason]."

If you can't fill all four blanks, the assumption isn't sharp enough. Send the user back to `manfred-discovery:opportunity-solution-tree` to refine it.

## Phase 2 — Pick the technique

By risk type. Cost ascending. Pick the **cheapest** that genuinely retires the assumption.

### Value-risk techniques

| Technique | Cost | What it answers | Best for |
|-----------|------|-----------------|----------|
| **Customer interview cluster (5–8)** | 1 week | "Do customers actually have this pain unprompted?" | Validating the *problem* before any solution |
| **Fake-door / Smoke test** | 2–5 days build + 1 week run | "Will customers click on this offering at meaningful rates?" | Validating that an entry point captures real intent |
| **Landing page test** | Few days + ad spend | "Will customers sign up / register interest?" | New offerings, new positioning |
| **Wizard-of-Oz** | 1–2 weeks (manual delivery) | "Will customers use this if it works exactly as advertised?" | Complex behaviour where the front-end matters |
| **Concierge MVP** | Few hours per customer | "Does the value actually land when we deliver it by hand?" | High-touch / low-volume products |
| **Pre-sale / commitment test** | Days | "Will customers pay / commit before delivery?" | Hard value signal — money on the table |

### Usability-risk techniques

| Technique | Cost | What it answers |
|-----------|------|-----------------|
| **Pattern audit (3 comparable products)** | 2 hours | "Is there a well-trodden pattern we should match?" |
| **Click-test on static prototype (Maze / Useberry)** | 1–2 days build + 24h run | "Can users find / complete the primary action?" |
| **Moderated 5-user usability test** | 1 week incl. recruit | "Where do users get stuck and why?" |
| **Tree test** | 1–2 days | "Does the IA / navigation match user mental models?" |
| **Card sort** (open or closed) | 2–3 days | "How do users group these concepts?" |

### Feasibility-risk techniques

| Technique | Cost | What it answers |
|-----------|------|-----------------|
| **Engineering tech-lead conversation (30 min)** | 30 min | "What's the team's confidence and what do they need to spike?" |
| **Architecture review (2 engineers, 2 hours)** | 2 hours | "Does the integration path hold up under scrutiny?" |
| **Engineering spike (timeboxed 1–5 days)** | 1–5 days | "Does this actually work end-to-end with our stack and data?" |
| **Vendor / API trial** | Days | "Do the third-party limits / rate limits / data shapes work for us?" |

### Viability-risk techniques

| Technique | Cost | What it answers |
|-----------|------|-----------------|
| **Stakeholder working session (60–90 min)** | 90 min | "Will legal / CRM / brand / ops support this? What would they need?" |
| **Specific written question to one stakeholder** | 1 day for response | "Does X department block this and on what grounds?" |
| **Compliance review (formal request)** | 1–4 weeks | "Does this clear GDPR / accessibility / legal review?" |
| **Commercial model test** (e.g. quote a price to a small cohort) | Days | "Does the price/business model work for the customer segment?" |

If none of the menu fits, design a custom test — but the same rules apply: one assumption, defined answer, timebox.

## Phase 3 — Write the test design

Save to `discovery/tests/<assumption-slug>-<YYYY-MM-DD>.md`. Use this template:

```markdown
# Assumption test: [short name]

**Assumption tested:** We assume that [audience] will [behaviour] when we [thing], because [reason].

**Risk type:** Value / Usability / Feasibility / Viability
**Technique:** [from the menu, or custom]
**Owner:** [Name]
**Timebox:** [start date → end date]
**Status:** Planned / Running / Done — supported / Done — refuted / Done — inconclusive

## Hypothesis

If [we run this test], we expect [observable signal].

## Method

[5–10 lines describing exactly what happens, what's built, who's involved, what data gets captured.]

## Success / failure criteria

- **Supported (assumption survives):** [specific number / threshold / observation]
- **Refuted (assumption dies):** [specific number / threshold / observation]
- **Inconclusive (need to redesign):** [conditions that mean the test didn't run cleanly]

## What we'll do based on the result

- **If supported →** [next action — usually advance the solution on the OST]
- **If refuted →** [next action — usually park or pivot the solution]
- **If inconclusive →** [next action — usually redesign the test, not the solution]

## Recruit / setup

[Customer recruit criteria if applicable — segment, sample size, channel. Tools / prototypes / surfaces needed.]

## Notes / risks for the test itself

[E.g. "Holiday week may suppress traffic — extend run by 5 days." "Need to brief support team in case customers ask about the fake button."]

---

**Linked OST:** [path to OST file or solution name]
**Linked Cagan-risks profile:** [path or "n/a"]
**Linked Linear ticket:** [ticket id or "n/a"]
```

If a Linear ticket is linked, post the test design link as a comment via `mcp__linear-server__save_comment` after resolving the issue with `mcp__linear-server__get_issue`. Pattern reference: `manfred-dev:test-my-code` Linear update section.

## Phase 4 — When the test finishes

Update the file with results. Status moves from `Running` → one of the three `Done` states. Fill in:

- **Result observed:** [actual data / quotes / observation]
- **Decision taken:** [what the team decided as a result]
- **Date closed:** [YYYY-MM-DD]

Then update the OST (`manfred-discovery:opportunity-solution-tree`) — change the test entry under the relevant solution to reflect the new status. If refuted, mark the solution `[parked]` with a one-line reason and consider what other solution(s) under the same opportunity to pursue next.

## Manfred lens

- **`manfred-discovery:cagan-risks`** — names the High risks; this skill designs the test that retires each
- **`manfred-discovery:opportunity-solution-tree`** — tracks the open assumption tests under each solution
- **`manfred-discovery:customer-touchpoint-plan`** — when the test technique requires customer recruit, the touchpoint plan includes the recruit
- **`manfred-discovery:discovery-readout`** — the readout cycle summarises what the tests in this period found
- **`manfred-discovery:weekly`** — the weekly command runs touchpoints + assumption tests + readout

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "Let's run a test that validates the whole solution" | Tests that validate everything answer nothing clearly. One assumption per test. Sequence them. |
| "Inconclusive is a fine outcome" | If your test can come back inconclusive, the test is wrong. Redesign so the answer is binary. |
| "We don't have time for a test, just ship it" | A 30-minute tech-lead conversation or a 90-minute stakeholder session is rarely "no time." If those don't fit, ask why. |
| "5 customers isn't statistically significant" | For qualitative usability, 5 surfaces 80% of issues. For quantitative value-risk tests (fake-door, landing page), pick a sample sized to detect a meaningful effect — not statistical significance theatre. |
| "Fake-door is dishonest — we can't deceive customers" | Fake-doors that capture intent and hand off honestly to existing flow are standard practice. The deception risk is real but manageable — write the hand-off copy carefully ("Coming soon — we'll let you know when it's ready"). |
| "Concierge / Wizard-of-Oz are too manual" | They're manual on purpose — you're testing whether the value lands, not the automation. Building automation before knowing the value lands is the expensive mistake. |
| "We tested usability, so the value risk is also retired" | No. Different risks need different tests. Don't conflate. |

## Red flags — STOP

- About to write a test design with no specific success criteria → Stop. Write the binary outcome first.
- About to test multiple assumptions at once → Stop. Pick the riskiest one and design just for it.
- About to recommend "do user research" with no named technique → Stop. Pick from the menu.
- About to skip the timebox → Stop. Open-ended tests don't end. Define the date you stop and decide.
- About to run a test that doesn't connect to a current OST solution → Stop. If it doesn't, why are you running it? Either map it back or don't run it.
- About to call something an assumption when it's actually an opinion → Stop. An assumption is testable. An opinion is not. Reframe.

## Tools used

- **Read / Write**: `discovery/tests/<assumption-slug>-<date>.md`
- **MCP** (when ticket linked): `mcp__linear-server__get_issue`, `mcp__linear-server__save_comment`
- **Skills called next** (depending on result):
  - `manfred-discovery:opportunity-solution-tree` — update solution status
  - `manfred-discovery:cagan-risks` — re-rate the relevant risk
  - `manfred-discovery:discovery-readout` — when wrapping a discovery cycle
- **Reference**: Teresa Torres, *Continuous Discovery Habits* (assumption mapping chapter); Marty Cagan, *Inspired* (discovery techniques chapter)
