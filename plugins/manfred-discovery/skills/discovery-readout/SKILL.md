---
name: discovery-readout
description: Use when summarising what was learned in a discovery cycle (a week, sprint, or focused investigation). Triggers on "discovery readout", "summarise what we learned", "what came out of the research", "post the discovery summary", "wrap up this discovery cycle", "share the findings with the team". Produces a markdown readout, saves it under discovery-reports/, and posts a summary as a Linear comment if a ticket is linked.
---

# discovery-readout

Wraps a discovery cycle. What we set out to learn, what we actually learned, what changes as a result. Posts to Linear when there's a ticket on the line.

## Overview

A discovery cycle (a week of touchpoints, an assumption test, a focused investigation) only counts if its findings re-enter the team's decision-making. This skill produces the readout — a one-page markdown that any teammate can read in 5 minutes and act on.

The readout has three jobs:

1. Document what was learned, with evidence (so the team can audit the conclusions later)
2. Name what changes as a result (OST updates, decisions, next tests)
3. Surface what's still open (so the next cycle has direction)

If the cycle didn't change anything — that's a finding too. Document the disconfirmation honestly.

## When to use

- End of a week of customer touchpoints (Friday afternoon synthesis)
- An `manfred-discovery:assumption-test` finishes — write the readout for that single test
- A focused investigation (e.g. "do we have a churn problem in segment X?") wraps
- The team needs to share with stakeholders / leadership what discovery is producing

**Skip when:**

- The cycle is still in flight — wait until the test / week is actually done
- A single customer interview wraps (note in the per-customer brief, but readout is for cycles, not individual conversations)

## Phase 1 — Pre-flight

Before writing, gather:

1. **Branch → Linear ticket** — `git rev-parse --abbrev-ref HEAD` and extract `[A-Z]+-\d+`. If found, the readout posts as a comment on the ticket. Pattern reference: `manfred-dev:test-my-code` Linear update section.
2. **Cycle scope** — what bracketed this work? A week? A sprint? An assumption test? Get it in one sentence.
3. **Source artifacts** — paths to: touchpoint plan(s), assumption test file(s), OST file(s) updated, any meeting notes from synthesis. The readout links back, doesn't replace them.
4. **Report path** — `discovery-reports/<TICKET-or-cycle-slug>-<YYYY-MM-DD>.md`. Create `discovery-reports/` if missing.

## Phase 2 — Walk the readout structure

Five sections. None of them get skipped.

### 1. What we set out to learn

One paragraph. What was the question this cycle was designed to answer? Pull from the touchpoint plan's "Mode" + "Outcome focus" or the assumption-test file's stated assumption.

If you can't say what the question was — the cycle was unfocused. Note it as a finding for the rituals to address.

### 2. What we actually learned

Bullet list of findings. Each finding has:

- **The finding itself** (one line, plain language)
- **Evidence** (interview IDs, test data, specific quotes — concrete sources, not "the team felt that")
- **Confidence** — High / Med / Low, with a reason

Push back on findings without evidence. "We learned customers want X" with no source isn't a finding, it's an opinion. Either find the evidence or drop it.

### 3. What changes as a result

The action layer. For each item:

- **OST updates** — opportunities added/refined/parked, solutions added/parked, assumption tests now `done — supported / refuted / inconclusive`
- **Decisions taken** — e.g. "park solution 2.3", "advance solution 1.1 to build", "open new opportunity X"
- **Next tests / actions** — what's the next assumption to test, who runs it, by when

Be specific. "We'll do more research" is not a change. "We'll run a 5-customer click-test on the new flow next week — Selma owns" is.

### 4. What's still open

Things we wanted to learn but didn't get clean signal on. Things that surfaced as new questions. These feed the next cycle's plan.

### 5. Cost & metadata

- **Cycle dates:** start → end
- **People:** who participated (Trio, plus extended)
- **Customers spoken to:** [N], with segment summary
- **Tests run:** [N], with linked test files
- **Time invested:** rough estimate (helps the team learn the cost of discovery vs. the value)

## Phase 3 — Save the file and post to Linear

Save to `discovery-reports/<TICKET-or-cycle-slug>-<YYYY-MM-DD>.md`. Use this template:

```markdown
# Discovery readout — [Cycle name or ticket id]

**Cycle dates:** [YYYY-MM-DD] → [YYYY-MM-DD]
**Trio:** [PM] · [Designer] · [Tech lead]
**Linked ticket:** [STU-XXX] (or "n/a")
**Linked artifacts:**
- [path to touchpoint plan]
- [path to assumption test(s)]
- [path to OST]

## 1. What we set out to learn

[One paragraph — the question this cycle answered.]

## 2. What we learned

- **[Finding 1]** — [evidence: interview-3 / interview-7, support cluster X] — Confidence: High / Med / Low ([reason])
- **[Finding 2]** — [...]
- **[Finding 3]** — [...]

## 3. What changes as a result

### OST updates
- [opportunity / solution / test status changes — link to the OST entries]

### Decisions taken
- [e.g. "Park solution 2.3 — value risk refuted (see test file)."]

### Next tests / actions
- [test / action — owner — by when]

## 4. What's still open

- [open question — feeds next cycle]

## 5. Cost & metadata

- **Customers spoken to:** [N] ([segment summary])
- **Tests run:** [N]
- **Time invested:** [rough estimate]

---

*Linked back to: [OST file], [assumption test files], [touchpoint plan]*
```

After saving, if a Linear ticket is linked, post a summary comment via `mcp__linear-server__save_comment` (resolve the issue first with `mcp__linear-server__get_issue`). Comment body:

```
Discovery readout — [YYYY-MM-DD]

We set out to: [one-line restatement of section 1]

Top findings:
- [finding 1] — High confidence
- [finding 2] — Med confidence
- [finding 3] — Low confidence

Decisions:
- [decision 1]
- [decision 2]

Next: [the single most important next action]

Full readout: discovery-reports/<TICKET-or-slug>-<YYYY-MM-DD>.md
```

If the ticket id can't be resolved or the comment fails, surface to the user — do NOT silently skip.

## Manfred lens

- **`manfred-discovery:opportunity-solution-tree`** — the OST is the single source of truth; the readout describes changes to it
- **`manfred-discovery:customer-touchpoint-plan`** — the readout closes the cycle that the touchpoint plan opened
- **`manfred-discovery:assumption-test`** — single-test readouts focus on the test result; multi-test cycles aggregate
- **`manfred-discovery:cagan-risks`** — re-rate any risk that's now informed by the cycle's findings
- **`manfred-discovery:discovery-rituals`** — the readout is part of the weekly ritual cadence

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "We learned a lot — too much to write up" | Then the readout is even more important. Bullet the top 3–5; link to evidence for the rest. |
| "We didn't really learn anything — no readout needed" | Disconfirmation IS a finding. Write that. The team needs to know what didn't move. |
| "I'll dump it in chat instead of a file" | The team won't find it again in 4 weeks. File. Link from chat if you must. |
| "We can skip the Linear comment, the ticket is closed" | If the ticket is closed and there's still discovery happening on it, the ticket might be wrong. Reopen or open a new one. |
| "Confidence ratings are subjective" | They are. Note your reason. The reason is the value, not the rating. |
| "Findings without evidence are still useful" | They're hypotheses, not findings. Move them to the OST as new opportunities to validate, not as findings here. |
| "Cost / time-invested is awkward to share" | The team needs to learn the unit cost of discovery to budget for it. Awkward is the point. |

## Red flags — STOP

- About to skip evidence on any finding → Stop. Either find the evidence or move the bullet to "open questions."
- About to claim High confidence without naming the data source → Stop. High needs a specific source.
- About to dump output to chat without saving the file → Stop. File first, then summary.
- About to post to Linear without saving the file → Stop. The Linear comment links to the file.
- About to skip section 3 ("what changes") because "we'll figure it out next week" → Stop. The whole point of the readout is the change.
- About to write a readout for a cycle that's still in flight → Stop. Wait until it's actually done.

## Tools used

- **Bash**: `git rev-parse --abbrev-ref HEAD` for ticket detection
- **Write**: `discovery-reports/<TICKET-or-slug>-<date>.md`
- **MCP**: `mcp__linear-server__get_issue`, `mcp__linear-server__save_comment`
- **Skills called**:
  - `manfred-discovery:opportunity-solution-tree` — to record the OST changes the readout names
  - `manfred-discovery:cagan-risks` — to re-rate risks informed by findings
- **Reference**: Teresa Torres, *Continuous Discovery Habits* (chapters on the weekly cadence and synthesis)
- **Pattern reference**: `manfred-dev:test-my-code` SKILL.md — Linear MCP integration pattern (resolve issue, post comment, surface failures)
