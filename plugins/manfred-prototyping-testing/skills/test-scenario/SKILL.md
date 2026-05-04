---
name: test-scenario
description: Use when writing tasks for usability testing — anyone says "write test tasks", "test scenarios", "usability test script", "what should I ask the participant", "facilitator guide", "moderator script", "task wording for the test". Manfred-flavoured: tasks are goal-oriented, never UI-oriented; participant language not product jargon; one goal per task; pair with `manfred-toolkit:ux-writing` for the wording rules.
---

# test-scenario

Test scenarios are the bridge between "we want to learn X" and what the participant actually sees / hears in the session. Bad task wording reveals the answer ("Click the settings icon"); good task wording elicits genuine behaviour ("Where would you go to change your email address?").

Manfred defaults:

- **Goal-oriented, not UI-oriented.** The task names what the user is trying to accomplish, not the path through the UI.
- **Participant's language, not product jargon.** "Cancel my plan" not "Modify subscription tier".
- **One goal per task.** Multi-goal tasks confound success measurement.
- **Don't reveal the path.** If task wording names a UI element, you've answered your own question.
- **Realistic context.** Brief backstory that gives the participant a reason to act, without pushing them.

## When to use

- Writing tasks for a moderated usability test (route the *plan* through `manfred-design-research:usability-test-plan`)
- Writing tasks for an unmoderated click test (route through `manfred-prototyping-testing:click-test-plan`)
- Writing facilitator guides for diary studies, contextual inquiries, journey-mapping sessions
- Reviewing existing tasks for hint-leakage / jargon / multi-goal structure

**Skip when:**

- The whole test plan is needed (recruit, logistics, analysis) — that's `manfred-design-research:usability-test-plan`
- Interview question design (open-ended exploratory) — that's `manfred-design-research:interview-script`
- Card-sort or tree-test design (no scenarios needed) — different methods

## The hard rules

| Rule | What it means |
|---|---|
| **Goal-oriented** | "What are you trying to accomplish" not "How do you click the button" |
| **Real context, no leading** | Brief backstory ("you bought a pair of shoes that don't fit") gives motivation without instruction |
| **Participant's language** | Use the words a real customer would use — not internal product jargon |
| **One goal per task** | Multi-step is fine; multi-goal is not |
| **Don't name UI elements** | If the task names "the settings icon" or "the menu", you've revealed the answer |
| **Pre-define success** | What does "completed" look like? Decide before the test runs. |

## The flow

### Step 1 — Confirm what you're testing

Map every task to:

- **Question being answered** ("Can users find X?", "Can users complete Y under time pressure?", "Where do users get stuck on Z?")
- **Decision the answer informs** (ship as-is / redesign / further investigation)

If a task doesn't trace to a question + decision — cut it.

### Step 2 — Write the backstory

A short, realistic frame that gives the participant motivation without nudging behaviour.

| Bad backstory | Why | Better |
|---|---|---|
| "Try to add a product to your cart." | Pure instruction, no motivation | "You're shopping for a birthday gift for a friend who likes hiking gear. Find something they'd like and prepare to buy it." |
| "You're a Manfred customer." | Generic, no real context | "You signed up for our service last week and haven't used it yet. You sit down with a coffee to get started." |
| "Imagine you're frustrated with your current bank." | Emotion-loaded, primes negative response | "You moved cities and need a bank that has better mobile features than your current one." |

### Step 3 — Write the task

Templates:

| Pattern | When | Example |
|---|---|---|
| **"Find / locate / show me…"** | Findability questions | "Where would you go to change your email address?" |
| **"How would you…"** | Open-path tasks (multiple valid paths OK) | "How would you cancel your subscription?" |
| **"You want to do X. Where do you start?"** | First-click / wayfinding | "You want to know how this app handles your data. Where would you click first?" |
| **"You realised Y. What do you do?"** | Recovery tasks | "You realised you sent the form to the wrong address. What do you do?" |
| **Comparative**: "If you wanted X, would you…?" | Choice between paths | "If you wanted to download your data, would you go to settings or your profile?" |

Bad patterns:

- ❌ "Click on the X button." — instructional, not behavioural
- ❌ "Initiate the return-merchandise authorisation flow." — jargon
- ❌ "Find the returns link and tell us what you think of it." — two tasks
- ❌ "Try to figure out how to delete your account." — leading ("try to" implies it'll be hard)

### Step 4 — Define success

For each task, before the test runs:

```markdown
## Task: <name>

**Question answered**: <findability / completability / comprehension / behaviour>

**Backstory**: <realistic frame>

**Task wording (verbatim)**: <exact words the moderator says or the unmoderated tool displays>

**Success criteria**:
  - **Completed**: <what counts as done — specific UI state or user statement>
  - **Time threshold**: <if relevant — e.g. "should complete within 60s in production">
  - **Path criteria**: <any path / specific path required — list acceptable alternatives>
  - **Errors**: <what counts as an error — wrong path taken, asking for help, abandoning>

**Observation watch-outs**: <what to look for during the task — hesitation, frustration markers, verbal confusion, recovery behaviour>

**Follow-up questions**: <after-task probes, e.g. "Was that easier or harder than you expected?", "What would you have wanted to see different?">

**Self-reported difficulty**: <e.g. "On a scale of 1–5, how easy was that?">
```

### Step 5 — Order the tasks

- **Warm-up first** — easy, unrelated to the test focus, to calibrate the participant on the interface conventions
- **Easy → hard** — build confidence; complex tasks come after the participant is acclimated
- **Don't cluster sensitive tasks** — distribute privacy-related, money-related, or destructive-action tasks across the session
- **End on something positive** — the participant leaves with a sense of competence

### Step 6 — Pilot the tasks

Always — no exceptions:

- Run the task script with 1–2 colleagues / friends *before* real participants
- Watch for: misinterpreted wording, missing context, tasks that take 3x longer than expected
- Revise based on the pilot

A test that ships with un-piloted tasks burns participant time and produces noisy data.

### Step 7 — Document

Save to:

```
research/test-scenarios/<test-name>-<YYYY-MM-DD>.md
```

Format:

```markdown
# Test scenarios — <test name>

**Date**: YYYY-MM-DD
**Linear**: STU-XXX
**Test type**: <moderated / unmoderated / diary / etc>
**Linked plan**: <path to manfred-design-research:usability-test-plan output>

## Pilot notes
[What you learned from the pilot; what changed]

## Tasks (in order)

### Warm-up
[Per format from Step 4]

### Task 1
...

### Task 2
...

## Closing
[Wrap-up questions; participant thanks; consent re-confirm; payment]
```

### Step 8 — Linear comment

Post via `mcp__linear-server__save_comment` with summary + path to scenarios.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Just tell them what to click — saves time." | Then you're testing whether they can read instructions, not whether the design works. Throw out the test or rewrite. |
| "Use product names — they'll get used to them." | Participants reach for *their* mental model, not yours. Use their words; map to yours in analysis. |
| "Two goals in one task is efficient." | Two goals = compound success rate; can't tell which step failed. Split. |
| "Pilots take time — we'll wing it." | Bad task wording costs more in re-runs than pilot would cost. Always pilot. |
| "Same script for moderated and unmoderated." | Moderated allows clarification; unmoderated can't. Unmoderated needs more context, no probes mid-task. |

## Red flags — STOP

- Task names a UI element ("the settings icon", "the menu", "the breadcrumb")
- Two goals in one task
- No success criteria pre-defined
- No pilot run before launch
- Backstory missing or generic ("you're a user")
- Order is random or hardest-first
- Jargon from the product appears in the task wording

## Manfred lens

**Cagan's 4 risks** — test scenarios are *plumbing* for tests retiring usability risk. Doesn't usually need its own Cagan call-out. Exception: when a test's task wording reveals the team's own assumption about the user (e.g. assumes user knows technical terms), surface as **value risk** (we may be wrong about who the user is) and route to `manfred-discovery:cagan-risks`.

## Cross-references

- `manfred-design-research:usability-test-plan` — the test plan; this skill writes the tasks inside it
- `manfred-design-research:interview-script` — for open-ended exploratory questions (different shape)
- `manfred-prototyping-testing:click-test-plan` — for unmoderated tasks
- `manfred-toolkit:ux-writing` — for the wording craft (Manfred voice rules apply to test wording too)
- `manfred-discovery:assumption-test` — frames the assumption the test retires

## Tools used

- `Read` — to inspect existing test artifacts
- `mcp__linear-server__get_issue` / `save_comment` — for ticket linkage

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, no-UI-naming rule, pilot-required rule, and Manfred-specific guidance are original.*
