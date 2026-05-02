---
name: diary-study-plan
description: Use when designing a longitudinal diary study to understand user behaviour over time in natural contexts. Triggers on "diary study", "longitudinal study", "behaviour over time", "in-context study", "self-reported behaviour", "naturalistic research", "extended observation".
---

# diary-study-plan

A longitudinal diary study, designed to actually finish — with realistic duration, attrition planning, prompt structure, and a synthesis path.

## Overview

Diary studies are the right tool when a question is about *behaviour over time in a natural context* — something that doesn't surface in a 45-minute interview. They're also the wrong tool 80% of the time, because the team thinks they want a diary study when they really want 5 well-designed interviews.

This skill gates on that question first ("are you sure this isn't an interview study?"), then designs the study to actually finish: realistic duration, attrition-aware sample size, prompt structure that doesn't burn out participants, and a coding framework for the data when it comes back.

## When to use

- The question is genuinely about behaviour-over-time or in-context behaviour ("how do people use this across a typical week", "how does sentiment shift over the first month of onboarding")
- Sentiment / context shifts that interviews can't surface
- High-stakes hypothesis about repeated behaviour (vs one-off)

**Skip when:**

- The question is "how do people feel about X" — interview instead
- The question is "can people complete this task" — usability test instead
- You don't have 4+ weeks of project time — diary studies need at least 1 week of study + 2 weeks of synthesis

## Two principles drive everything

1. **Duration honesty.** Diary studies fail when too long (attrition) or too short (no behaviour pattern). 5–14 days for behaviour patterns; 21–30 days for sentiment / habit formation. Anything over 30 days needs strong reason.
2. **Light prompts beat heavy ones.** Daily 2-minute prompts beat weekly 20-minute ones. Participants drop out of long-form requirements; they keep up with short-form. The trade-off is depth — accept it and structure prompts accordingly.

## Phase 1 — Gate: are you sure?

Ask:

- "What specifically can you not learn from a 45-min interview that you'd learn from this study?" If the answer is "richer context" — push back, that's still interview territory.
- "What does the data look like at the end?" If the user can't describe the synthesis output, they don't know what they're studying.
- "How many weeks do you have, total?" Below 4 weeks total, recommend interviews + a follow-up.

If the gate clears, proceed.

## Phase 2 — Design the study

| Decision | Default | When to deviate |
|----------|---------|-----------------|
| **Duration** | 7–10 days | Habit / sentiment work: 21–30 days. Single-event capture: 1–3 days. |
| **Sample size** | 8–12 (with attrition padding to 15) | Down to 5 for highly-targeted segments; up to 20+ if statistical inference needed |
| **Recruit segment** | Specific behavioural criteria, not demographic | Default — segment by what they do, not who they are |
| **Prompt cadence** | 1× daily, 2 minutes | Heavier weekly prompts only if depth is the question |
| **Prompt format** | Mixed: short text + photo upload + 1-question scale | Vary; participants disengage from format monotony |
| **Incentive** | Significant (€100–€300 for 1–2 weeks; more for longer) | Must reflect the time + cognitive load — diary studies are real work |

## Phase 3 — Write the prompt set

Two kinds of prompts:

**Recurring (daily / every-time-X-happens):**

- "Did [behaviour X] happen today? If yes — when, where, how did it go?"
- "What was your sentiment at end of day around [topic]?" (1–5 scale + one sentence why)
- "Photo: take a picture of [in-context artifact]"

**One-off (start, mid, end):**

- **Day 0:** baseline / expectations
- **Mid:** check-in (catches attrition; surfaces emerging patterns)
- **Final:** retrospective interview (15 min, optional)

Avoid:

- Long-form essay prompts daily — burns participants out
- Solution-validation prompts ("would you use this feature?") — diary captures what's actually happening, not opinions
- Open-ended prompts with no anchor ("anything to share?") — too vague to engage with

## Phase 4 — Plan attrition

Attrition is normal. Plan for 30–50% dropout over 14 days. To handle it:

- Recruit 1.5x the target sample (target 8 → recruit 12; target 12 → recruit 18)
- Day 1 onboarding session (group call or 1:1) — the participants who attend Day 1 stick at 2x the rate of those who don't
- Day 3 check-in — flag silent participants and re-engage
- Day 7 mid-cycle prompt re-anchors the study purpose
- Pay incrementally — half at Day 0, half at completion — better retention than lump-sum-end

## Phase 5 — Design the synthesis framework

Diary data is messy. Plan the coding before the data arrives.

**Coding dimensions to plan:**

- **Behavioural events** (what happened) — codable into a few discrete categories
- **Context** (when, where, with what tools)
- **Sentiment** (numeric rating + qualitative reason)
- **Surprises** (anything not in the codebook — these become emerging themes)

**Synthesis output:**

- Affinity diagram (`manfred-design-research:affinity-diagram`) of the surprises
- Behavioural-event frequency table (quant from the qual)
- Per-participant sentiment trajectory (a chart per participant showing sentiment over the study)
- Cross-cutting themes that show up in 30%+ of participants

## Phase 6 — Output the study plan

Save to `discovery/diary-studies/<study-slug>-<YYYY-MM-DD>.md`:

```markdown
# Diary study plan — [Study name]

**Date drafted:** [YYYY-MM-DD]
**Outcome / question this serves:** [from the OST]
**Linked Linear ticket:** [STU-XXX or "n/a"]

## Why this is a diary study (not interviews)

[2–3 sentences answering the gate question. If you can't write this, do interviews instead.]

## Design

| Field | Value |
|-------|-------|
| Duration | [X days] |
| Sample size (target / recruit) | [target / target × 1.5] |
| Recruit segment | [behavioural criteria] |
| Prompt cadence | [daily / every-time-X / weekly] |
| Format mix | [text / photo / scale / video] |
| Incentive | [amount + format + payment schedule] |

## Recruit

- **Channel:** [in-product, support history, panel-as-fallback]
- **Owner:** [PM name]
- **Screener questions:** [3–5 questions to confirm fit]

## Prompts

### Day 0 — Onboarding session (group call, 30 min)
- Walk participants through the study
- Set expectations: cadence, total time, payment schedule
- Practice prompt: have everyone post once before leaving the call

### Recurring prompts (daily for [N] days)
- "[Recurring prompt 1]"
- "[Recurring prompt 2]"

### Day [N/2] — Mid-cycle check-in
- "[Check-in prompt]"

### Final day — Retrospective
- 15-minute optional interview, story-based questions about the study period

## Attrition plan

- Day 0 onboarding session attendance is the main retention lever
- Day 3 silent-participant re-engage list owner: [Name]
- Half-payment at Day 0, half on completion
- Replacement recruit window: Days 1–3 only

## Synthesis framework

- **Coding dimensions:** [list]
- **Synthesis cadence:** weekly during study + 1-week intensive after
- **Output:** affinity diagram + frequency table + sentiment trajectory + cross-cutting themes
- **Trio attendance for synthesis:** weekly during, intensive at end

## Risk / readiness check

- [ ] We have ≥4 weeks total project time (study + synthesis + decision)
- [ ] Recruit pipeline can deliver target × 1.5 in target segment
- [ ] Trio committed to weekly synthesis
- [ ] Tool chosen + tested ([Indeemo / Dscout / Slack / paper-equivalent])
- [ ] Incentive budget approved
```

If a Linear ticket is linked, post the gate-question answer + design summary as a Linear comment.

## Manfred lens

- **Research isn't a phase** (principle 2) — diary studies feed continuous OST updates, not just an end-of-study report
- **Customer-driven always** (principle 1) — natural-context observation captures what customers actually do, not what they say
- **Pay people for their time** — diary studies are real work; honour it

## Cross-plugin handoffs

- **Output to `manfred-design-research:affinity-diagram`** — synthesise surprises across participants
- **Output to `manfred-design-research:journey-map`** — map behaviours across time / stages
- **Output to `manfred-discovery:opportunity-solution-tree`** — themes update the tree
- **Input from `manfred-design-research:interview-script`** — Day 0 + retrospective interviews use the script template

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "Let's run a 30-day diary study to be thorough" | 30 days = high attrition. Pick the shortest duration that captures the behaviour pattern. Default 7–10. |
| "Sample of 5 is fine, costs less" | After attrition, you'll have 2–3. The study fails. Recruit 1.5× target minimum. |
| "Daily 15-minute prompts get richer data" | They get richer data from the 30% who don't drop out. Lighter prompts get usable data from 70%+. The trade is worth it. |
| "We can synthesise at the end — no weekly cadence needed" | Then surprises in week 1 get forgotten by week 4. Weekly synthesis is the discipline. |
| "Diary study is the right tool because we want 'rich qualitative insight'" | Maybe. Probably interviews. Run the gate question first. |

## Red flags — STOP

- About to recommend a diary study without running the Phase 1 gate → Stop. Most "diary study" requests are interview studies in disguise.
- About to set duration over 14 days without sentiment / habit reason → Stop. Drop to 7–10.
- About to recruit at sample size = target (no padding) → Stop. 1.5× minimum.
- About to plan daily prompts of 15+ minutes → Stop. Light prompts only.
- About to skip the synthesis framework → Stop. Code dimensions before data arrives, not after.

## Tools used

- **Write**: `discovery/diary-studies/<slug>-<date>.md`
- **MCP** (when ticket linked): `mcp__linear-server__get_issue`, `mcp__linear-server__save_comment`
- **Skills called**:
  - `manfred-design-research:interview-script` — Day 0 + retrospective interviews
  - `manfred-design-research:affinity-diagram` — synthesis
  - `manfred-discovery:opportunity-solution-tree` — outcome updates

---

*Adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) (MIT). Phase 1 gate, attrition-aware sample sizing, light-prompt principle, and Manfred OST integration are original.*
