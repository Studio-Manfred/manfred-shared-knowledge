---
description: Create a prototyping + testing plan for a design initiative — chains assumption-test framing + fidelity selection (LEARN vs SHOW) + flow + wireframes + test scenarios + a11y + timeline.
argument-hint: [feature or initiative to prototype + test, e.g. "new onboarding flow" or "checkout review step"]
---

You're creating a prototyping + testing plan. The user mentioned: $ARGUMENTS

This is the orchestrator — it runs the full prototype-to-test pipeline, starting from the assumption (not the fidelity) and producing a plan that retires the right risk at the cheapest cost.

## Step 1 — Frame the assumption (`manfred-discovery:assumption-test`)

Before anything else: what assumption is this prototyping + testing exercise retiring?

- **Risk type**: value / usability / feasibility / viability
- **Assumption**: explicit, testable
- **Decision**: what changes based on the result (build / kill / pivot / iterate)
- **Audience**: users (LEARN) or stakeholders (SHOW)?

If the user can't state these — refuse and route to `manfred-discovery:assumption-test` first. **Do not skip this step**. The most common failure mode is producing a competent-sounding plan that retires no assumption.

## Step 2 — Pick fidelity + method (`manfred-prototyping-testing:prototype-strategy`)

Run the prototype-strategy skill. Critically:

- **Cheapest fidelity that retires the assumption** wins
- **Separate LEARN and SHOW artifacts** if audiences differ
- **Push back on stakeholder polish + deadline as fidelity drivers** — they're not
- **Build to throw away** — if the answer is "no", you're building product

Output: fidelity recommendation + tool + cost/time estimate + cross-plugin handoffs.

## Step 3 — Map user flows (`manfred-prototyping-testing:user-flow-diagram`)

For the prototyped artifact:

- **Goal of the flow** — single user goal
- **Happy path first**, then branches, then error paths
- **Decision criteria** explicit at every diamond
- **Error paths** mapped (pair with `manfred-interaction-design:error-handling-ux`)
- **AT-equivalent paths** for accessibility

Output: flow diagram + walkthrough + decision table + error/recovery table.

## Step 4 — Spec wireframes (`manfred-prototyping-testing:wireframe-spec`)

For each screen in the prototype:

- **All five states** — empty / loading / populated / error / partial
- **Greyscale only** (defer colour to visual phase via `manfred-ui-design:design-screen`)
- **Content priority numbered**
- **Responsive variants** (mobile-first per principle 12)
- **Spacing in tokens** via `manfred-design-systems:design-token`
- **a11y annotations** — heading hierarchy, landmarks, focus order

For hi-fi prototypes: chain to `manfred-ui-design:design-screen` for the visual layer after wireframes are stable.

## Step 5 — Write test scenarios (`manfred-prototyping-testing:test-scenario`)

For each task the participant will perform:

- **Goal-oriented, not UI-oriented** — name what they're trying to accomplish, not the path
- **Participant's language**, not product jargon
- **One goal per task**
- **Don't reveal the UI path**
- **Pre-define success criteria** (what counts as completed, time threshold, acceptable paths, errors)
- **Pilot the tasks** before real participants

Output: facilitator guide with backstory + task wording + success + observation watch-outs + follow-up probes.

## Step 6 — Plan accessibility testing (`manfred-prototyping-testing:accessibility-test-plan`)

Even for a prototype:

- **Layer 1 (axe)** in the prototype tool if available
- **Layer 2 (manual)** keyboard + zoom + reduced-motion walkthrough
- **Layer 3 (AT)** at minimum VoiceOver + Safari for hi-fi prototypes
- **Layer 4 (users with disabilities)** if the prototype is going to user testing

Plan the four layers, not just the first.

## Step 7 — Pick the test method per question

Match question shape to test method:

| Question | Method | Skill |
|---|---|---|
| "Can users find X?" | First-click / unmoderated click test | `manfred-prototyping-testing:click-test-plan` |
| "Why do users get stuck?" | Moderated 5-user usability test | `manfred-design-research:usability-test-plan` |
| "By how much does X improve Y at scale?" | A/B test | `manfred-prototyping-testing:a-b-test-design` |
| "Is the IA structured right?" | Tree test / card sort | `manfred-design-research:card-sort-analysis` |
| "Is this accessible?" | Per `manfred-prototyping-testing:accessibility-test-plan` |

Cheapest test that retires the assumption.

## Step 8 — Timeline

Realistic, with iteration room:

- Prototype build (per fidelity + method)
- Pilot the test scenarios (1–2 colleagues, half a day)
- Recruit participants (1–2 weeks for moderated; 24–48 hours for unmoderated)
- Run the test
- Analyse + write up
- Decision meeting + share learnings

If the timeline doesn't include iteration room, the test is theatre.

## Step 9 — Document

Save to:

```
docs/prototype-plans/<initiative-slug>-<YYYY-MM-DD>.md
```

Include:

- Brief (assumption + risk + decision + audience from Step 1)
- Fidelity recommendation (LEARN + SHOW separately if applicable, from Step 2)
- User flows (Step 3)
- Wireframe specs per screen (Step 4)
- Test scenarios (Step 5)
- a11y plan (Step 6)
- Method per question (Step 7)
- Timeline (Step 8)
- Cross-plugin handoffs:
  - Visual design after wireframes stabilise: `manfred-ui-design:design-screen`
  - Components in the prototype: `manfred-design-systems:component-spec`
  - Interaction details: `manfred-interaction-design:design-interaction`
  - Copy: `manfred-toolkit:ux-writing`
  - a11y verification: `manfred-design-systems:a11y-qa`

## Step 10 — Linear comment

Post via `mcp__linear-server__save_comment`:

- Path to plan
- Assumption + risk + cheapest test selected
- Fidelity + tool + timeline
- Cross-plugin handoffs queued

## Wrap-up checklist

- [ ] Assumption + risk + decision + audience explicit
- [ ] Fidelity is the cheapest that retires the risk
- [ ] LEARN vs SHOW separated if needed
- [ ] User flows mapped with error paths
- [ ] Wireframes spec'd in greyscale, all 5 states
- [ ] Test scenarios goal-oriented, no UI hints, pilot done
- [ ] a11y plan covers all 4 layers
- [ ] Timeline includes iteration room
- [ ] Linear comment posted

Then offer:

> "For the test execution: `/manfred-prototyping-testing:test-plan` for the full usability test plan. For visual design after wireframes stabilise: `/manfred-ui-design:design-screen`. For the interaction details: `/manfred-interaction-design:design-interaction`."
