---
description: Design a complete usability testing plan — chains assumption-test framing + method selection + scenarios + click tests + a11y + logistics + analysis plan.
argument-hint: [product / feature / prototype to test, e.g. "the new checkout flow" or "the onboarding step-2 redesign"]
---

You're designing a usability testing plan. The user mentioned: $ARGUMENTS

This is the orchestrator — it runs the full test design pipeline starting from the assumption (not the method) and producing a plan that retires the right risk at the cheapest cost.

## Step 1 — Frame the assumption (`manfred-discovery:assumption-test`)

Before picking method:

- **Risk type**: value / usability / feasibility / viability
- **Assumption**: explicit, testable
- **Decision**: what changes based on the result
- **Method shape required**: qualitative ("why") vs quantitative ("by how much") vs both

If the user can't state these — refuse and route to `manfred-discovery:assumption-test` first. Don't design a test plan for an unstated question.

## Step 2 — Pick the method

Match question shape to method:

| Question | Method | Skill |
|---|---|---|
| "Why do users get stuck on X?" | Moderated 5-user usability test | `manfred-design-research:usability-test-plan` (use this skill for the deep moderation craft) |
| "Can users find X / complete X?" | Unmoderated click / first-click test | `manfred-prototyping-testing:click-test-plan` |
| "Does X improve Y at scale?" | A/B test | `manfred-prototyping-testing:a-b-test-design` (use `/manfred-prototyping-testing:experiment` orchestrator) |
| "Is the IA structured right?" | Tree test / card sort | `manfred-design-research:card-sort-analysis` |
| "How does this hold up over a week of real use?" | Diary study | `manfred-design-research:diary-study-plan` |
| "Is this accessible?" | Per `manfred-prototyping-testing:accessibility-test-plan` (all four layers) |

Often: **two methods in parallel**. Moderated gives the *why* in 5 sessions; unmoderated quantifies the finding at 30+ users in 24 hours. Use both for high-stakes decisions.

## Step 3 — Confirm the test object (`manfred-prototyping-testing:prototype-strategy`)

What's being tested?

- Production code
- A prototype (low / mid / hi-fi — see prototype-strategy if undecided)
- A wireframe (`manfred-prototyping-testing:wireframe-spec`)
- A concept (paper, video, narrative)

Match the test object's fidelity to what's being learned:

- Findability → low-fi clickable usually enough
- Interaction patterns → mid-fi
- Visual / micro-interaction reaction → hi-fi
- Real-world behaviour over time → production code or hi-fi over multiple sessions

## Step 4 — Write test scenarios (`manfred-prototyping-testing:test-scenario`)

For each task:

- **Goal-oriented, not UI-oriented**
- **Participant's language**, not product jargon
- **One goal per task**
- **Don't reveal the path** ("Where would you go to change your email" not "Click the settings icon")
- **Pre-define success** (what counts as completed; time threshold; acceptable paths; errors)
- **Order easy → hard** with a warm-up
- **Pilot with 1–2 colleagues first**

Output: facilitator script with backstory + verbatim task wording + success criteria + observation watch-outs + follow-up probes per task.

## Step 5 — Pair with click tests if quant signal needed (`manfred-prototyping-testing:click-test-plan`)

If a moderated finding needs quantification:

- Same task wording (where applicable)
- 30–50 unmoderated participants
- Pre-defined click target areas
- Decision threshold pre-committed (typically 65%+ first-click success)

Quantitative confirms; qualitative explains. Pair when stakes warrant.

## Step 6 — Plan accessibility coverage (`manfred-prototyping-testing:accessibility-test-plan`)

For the test object:

- **Layer 1 (axe / Lighthouse)** — automated scan first
- **Layer 2 (manual)** — keyboard, zoom 200%, reduced-motion
- **Layer 3 (AT)** — VoiceOver + Safari, NVDA + Firefox at minimum
- **Layer 4 (real users with disabilities)** — for high-impact features; recruit via Fable / Knowbility / AccessWorks; pay fairly

If layer 4 is omitted — name the limitation explicitly.

## Step 7 — Define logistics

| Decision | Notes |
|---|---|
| **Participants (N)** | Moderated qual: 5 per primary segment (diminishing returns past). Click test: 20–50. A/B: per power calc. Diary: 10–15. |
| **Recruitment criteria** | Screen for the audience that matters — not generic crowdsource panel. Document criteria. |
| **Compensation** | Fair market rate. Same rate for AT users. |
| **Schedule** | 60–90 min sessions (moderated). Block buffer between (note-taking + reset). |
| **Equipment** | Their device + their setup wherever possible (especially for AT). Backup recording. |
| **Facilitator + observer roles** | Separate roles. Facilitator runs tasks; observer takes notes. |
| **Recording consent** | Explicit, written, what'll be used for. Allow opt-out without forfeiting compensation. |

## Step 8 — Pre-commit the analysis plan

Write down before the test runs:

- **What "completed" looks like per task**
- **What "failed" looks like per task**
- **Severity rubric for findings** (Manfred 0–4 scale per `manfred-prototyping-testing:heuristic-evaluation`)
- **What you'll do at each finding type** (ship / iterate / kill / further research)

Otherwise: post-hoc rationalisation. Findings get interpreted to support the decision the team already wanted.

## Step 9 — Document + hand off

Save to:

```
docs/test-plans/<test-slug>-<YYYY-MM-DD>.md
```

Include:

- Brief (assumption + risk + decision from Step 1)
- Method (Step 2) + rationale + cross-method pairing (Step 5)
- Test object + fidelity (Step 3)
- Scenarios (Step 4 — verbatim)
- a11y coverage (Step 6)
- Logistics (Step 7)
- Pre-committed analysis plan (Step 8)
- Cross-plugin handoffs:
  - Moderation craft: `manfred-design-research:usability-test-plan`
  - Heuristic pre-pass: `manfred-prototyping-testing:heuristic-evaluation`
  - a11y deep-dive: `manfred-design-systems:a11y-qa`
  - Findings → opportunity backlog: `manfred-discovery:opportunity-solution-tree`

## Step 10 — Linear comment

Post via `mcp__linear-server__save_comment`:

- Path to plan
- Assumption + risk + method
- Participant N + recruitment status
- Pre-committed decision rule
- Cross-plugin handoffs

## Wrap-up checklist

- [ ] Assumption + risk + decision explicit
- [ ] Method matches question shape
- [ ] Test object fidelity matches what's being learned
- [ ] Scenarios goal-oriented + piloted
- [ ] a11y coverage planned (all 4 layers or limitation named)
- [ ] Recruit for the right audience, paid fairly
- [ ] Analysis plan pre-committed in writing
- [ ] Linear comment posted

Then offer:

> "Pre-pass with `/manfred-prototyping-testing:evaluate` (heuristic eval) before user testing — saves user time on issues experts could've caught. After the test: log findings to `manfred-discovery:opportunity-solution-tree` so they update the discovery backlog."
