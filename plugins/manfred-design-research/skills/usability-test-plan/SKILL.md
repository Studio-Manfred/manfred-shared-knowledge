---
name: usability-test-plan
description: Use when designing a moderated or unmoderated usability test — research questions, tasks, success metrics, participant criteria, facilitation guide. Triggers on "usability test", "usability study", "moderated test", "unmoderated test", "task-based test", "usability test plan", "test plan for the prototype".
---

# usability-test-plan

A usability test designed to answer specific research questions, with task scenarios written in user language, accessibility-inclusive recruit, and a synthesis path that connects findings to the OST.

## Overview

Usability tests fail two common ways: tasks are written as feature checks ("click the dashboard"), or the test answers a question the team didn't actually have. This skill gates on the research question first, then builds tasks as realistic scenarios in user language, recruits inclusively, and ships with a facilitation guide that prevents the common moderator mistakes (leading the participant, explaining the design, helping them through stuck moments).

Pairs with `manfred-design-research:interview-script` for the actual moderator script.

## When to use

- Have a prototype, design, or live product to test
- Need to validate that users can complete specific tasks
- Need to surface where users get stuck and why
- Comparing design alternatives (within-subject or between-subject)
- Pre-launch readiness check

**Skip when:**

- Question is "do users want this" — value risk, use `manfred-discovery:cagan-risks` + `assumption-test` instead
- Question is "what should the IA be" — use `manfred-design-research:card-sort-analysis` first
- Need quantitative behaviour at scale — A/B test instead

## Two principles drive everything

1. **Research questions before tasks.** What specifically do you want to know after this test? "Can users complete the new signup flow without help?" — answerable. "Is the new design good?" — not. Tasks come from research questions, not from the design.
2. **Tasks are scenarios, not instructions.** ✅ "You want to send an invoice to a new client. Show me how you'd do it." ❌ "Click the 'New Invoice' button in the top right." Scenarios let you observe behaviour; instructions test reading comprehension.

## Phase 1 — Pre-flight

Ask:

- **Research questions:** 3–5, max. Specific. Answerable from observation.
- **What's being tested:** prototype (Figma / coded), staging product, live production, paper sketch
- **Moderated or unmoderated:** Moderated = richer signal, smaller N (5–8). Unmoderated = larger N (15–30+), shallower signal.
- **Success criteria per question:** what would "passing" look like? Be concrete.
- **Recruit:** segment, sample size, accessibility inclusion (see Phase 2)
- **Output path:** `discovery/usability/<study-slug>-<YYYY-MM-DD>.md`

## Phase 2 — Recruit (inclusion is non-optional)

Recruit must include:

- The primary segment for the feature being tested
- **Accessibility recruitment minimum:** at least 1 in 5 participants should be a disabled / AT-using / neurodivergent user, *unless* the feature genuinely has no accessibility surface (rare). This is per Manfred design principle 5 — accessibility is not a follow-up test phase.
- Segment-balanced (don't accidentally test only power users)
- Recruited at 1.5× target to handle no-shows

Pay participants. Standard rate for 30–60 min: equivalent of one hour's professional rate.

## Phase 3 — Write the tasks

For each research question, design 1–3 task scenarios that would answer it through observation.

Task scenario format:

```
**Scenario:** You want to [realistic outcome the user would actually want].
**Task:** Show me how you would [verb that doesn't reveal the answer].
**Success criteria:** [observable behaviour that means it worked]
**Failure modes to watch for:** [predicted points of confusion]
**Probing questions** (after task): "Tell me what you were thinking when [moment X]." (Story-based; no leading.)
```

Don't give more than 5–7 tasks total — fatigue degrades the data.

## Phase 4 — Facilitation guide

Standard moderator rules, written into the script:

- **Don't help.** When the participant gets stuck, observe. Note the time. Only intervene if they're about to give up entirely.
- **Don't explain the design.** "Why is the button there?" → "What would you expect?" Then observe.
- **Embrace silence.** 4 seconds usually pulls more than the next question.
- **Story-based probes only** (per `manfred-design-research:interview-script`)
- **Don't sell.** Resist the urge to pitch upcoming features when they ask.

For unmoderated: write all instructions and probe questions into the test platform (Maze, UserTesting, etc.). Pre-test with one internal volunteer to catch ambiguous instructions.

## Phase 5 — Pilot the test

Before running with real participants, pilot with 1 internal volunteer (not the designer, not someone who's seen the design). Catches:

- Ambiguous task scenarios
- Tools / tech setup issues (screen share, recording, etc.)
- Time mis-estimates

If the pilot exposes 3+ issues, fix and pilot again before going live.

## Phase 6 — Synthesis plan

Plan the synthesis before running the test. Decide:

- **What gets coded:** task completion (yes/no/with help), time-on-task (if relevant), severity of friction (Low/Med/High), specific issue category
- **Who synthesises:** Trio (per Manfred discovery rituals)
- **Output format:** issues list with severity, recommended changes, link to OST

## Phase 7 — Output

Save to `discovery/usability/<study-slug>-<YYYY-MM-DD>.md`:

```markdown
# Usability test plan — [Study name]

**Date:** [YYYY-MM-DD]
**What's tested:** [prototype / staging / live]
**Type:** Moderated / Unmoderated
**Sample size (target / recruit):** [N / N×1.5]
**Linked outcome:** [from the OST]
**Linked Linear ticket:** [STU-XXX or "n/a"]

## Research questions

1. [Specific, answerable question]
2. [...]
3. [...]

## Recruit

- **Segment:** [specific behavioural definition]
- **Accessibility inclusion:** [1 in 5 minimum — define which AT/disability included]
- **Channel + screener:** [recruit source + screening questions]
- **Incentive:** [amount + format + payment timing]
- **Owner:** [Name]

## Tasks

### Task 1 — [name]

- **Research question this answers:** [link to RQ above]
- **Scenario:** [Realistic outcome.]
- **Task instruction:** [Verb that doesn't reveal the answer.]
- **Success criteria:** [observable behaviour]
- **Failure modes to watch for:** [predicted confusion points]
- **Post-task probe:** [story-based question]

### Task 2 — [name]
[...]

## Facilitation guide

- [Standard rules — don't help, don't explain, embrace silence]
- [Trio roles — moderator / note-taker / observer]
- [Recording + consent script]

## Pilot

- [ ] Internal pilot with 1 volunteer — date: [YYYY-MM-DD]
- [ ] Issues surfaced + fixed before live test

## Synthesis plan

- **Coding dimensions:** [task completion, time, severity, issue category]
- **Trio synthesis session:** [date]
- **Output:** issues list with severity → recommended changes → OST update

## Risk / readiness check

- [ ] Research questions are specific and answerable
- [ ] Tasks are scenarios, not instructions
- [ ] Recruit includes 1+ disabled / AT user
- [ ] Pilot scheduled before live test
- [ ] Trio committed to synthesis
```

If a Linear ticket is linked, post the research questions + sample size + dates as a Linear comment.

## Manfred lens

- **Customer-driven always** (principle 1) — research questions before tasks
- **Accessible first** (principle 5) — recruit inclusion is mandatory, not optional
- **Critical & ethical design** (principle 6) — observation includes "where could this design coerce or exclude?"
- **Research isn't a phase** (principle 2) — tests feed the OST continuously, not just project-end

## Cross-plugin handoffs

- **Input from `manfred-design-research:card-sort-analysis`** — recommended tree tests use this skill's structure
- **Input from `manfred-discovery:assumption-test`** — usability-risk tests come here for design
- **Output to `manfred-design-research:summarize-interview`** — for moderated test debriefs
- **Output to `manfred-discovery:opportunity-solution-tree`** — issues become opportunities or assumption test results
- **Output to `manfred-design-systems:a11y-qa`** — accessibility findings cross over

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "Skip the research questions, just have users 'try the design'" | Test will produce a stack of unsorted observations with no decision power. RQs first. |
| "Tasks like 'click the new dashboard' are clearer" | They test reading comprehension, not usability. Scenarios in user language only. |
| "Accessibility recruit can wait for a follow-up test" | Then it's not Manfred work. AT/disabled users in every test, period. |
| "5 users isn't enough — bump to 20" | 5 surfaces 80% of usability issues for moderated qualitative. 20 is for quantitative — different tool. |
| "Skip the pilot — we don't have time" | The pilot saves more time than it costs. Always pilot. |

## Red flags — STOP

- About to write tasks that are click-instructions instead of scenarios → Stop. Reframe in user language.
- About to recruit only able-bodied users → Stop. Add 1 in 5 minimum.
- About to skip the pilot → Stop. Always pilot.
- About to design a test without clear research questions → Stop. RQs first.
- About to recommend N=20 for moderated qualitative → Stop. 5–8 is the right range.

## Tools used

- **Write**: `discovery/usability/<slug>-<date>.md`
- **MCP** (when ticket linked): `mcp__linear-server__get_issue`, `mcp__linear-server__save_comment`
- **Skills called**:
  - `manfred-design-research:interview-script` — for the moderator script
  - `manfred-design-research:summarize-interview` — for debriefs
  - `manfred-discovery:opportunity-solution-tree` — issues become opportunities
  - `manfred-design-systems:a11y-qa` — accessibility issues cross over
- **Reference**: Steve Krug, *Rocket Surgery Made Easy*; Jakob Nielsen on the 5-user discovery rule; Erika Hall, *Just Enough Research*

---

*Adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) (MIT). Research-questions-first gate, scenario-not-instruction discipline, mandatory accessibility recruit, mandatory pilot, and Manfred OST integration are original.*
