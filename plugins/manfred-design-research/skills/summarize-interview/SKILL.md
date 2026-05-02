---
name: summarize-interview
description: Use when synthesising a recorded interview or transcript into structured findings — themes, verbatim quotes, jobs surfaced, pain points, action items. Triggers on "summarise the interview", "interview summary", "transcript synthesis", "what came out of the interview", "extract themes from this transcript", "interview readout".
---

# summarize-interview

Turns a raw interview transcript into structured findings the team can act on. Verbatim quotes stay verbatim. Inferences are labeled inferences. Confidence is named.

## Overview

Most interview summaries blur three things: what the participant said, what the synthesizer inferred, and what the team should do. This skill keeps those layers separate so the next person reading the summary can see the seams — and challenge them if needed.

A good summary makes the source recording optional for most readers, but findable for any reader who wants to verify.

## When to use

- A recorded interview / transcript exists and the synthesis hasn't happened yet
- Friday synthesis ritual under `manfred-discovery:discovery-rituals` — multiple interviews to summarise
- After an `interview-script` session is run

**Skip when:**

- The recording is from a sales / support / stakeholder call — different format
- You're synthesising 5+ interviews together — use `manfred-design-research:affinity-diagram` instead

## Two principles drive everything

1. **Verbatim beats paraphrase.** When the participant said something memorable, capture it word-for-word. Paraphrase loses signal and can shift meaning by accident. Quotes carry timestamp + line of context.
2. **Stated vs inferred is a hard line.** What they actually said is a finding. What you concluded from what they said is an inference. Both are useful; conflating them is dangerous.

## Phase 1 — Pre-flight

- **Source path:** transcript file (`.md`, `.txt`, `.vtt`, etc.) — confirm it exists before processing
- **Linked artifacts:** which `interview-script` was used, which OST opportunity / assumption it served, ticket id if any
- **Output path:** `discovery/summaries/<participant-slug>-<YYYY-MM-DD>.md` (create `discovery/summaries/` if missing)

## Phase 2 — Read the transcript end-to-end before extracting

Read the whole thing first. Don't extract on first pass. Patterns that matter often only become visible after the participant has said the same thing in three different ways.

## Phase 3 — Extract along five dimensions

For each dimension, capture both **what was said** (verbatim, with timestamp) and **what it suggests** (inference, labelled).

| Dimension | What to look for |
|-----------|-----------------|
| **Jobs / motivations** | What was the participant trying to get done? Functional, emotional, social. (Bridge to `manfred-design-research:jobs-to-be-done`.) |
| **Current behaviour** | What do they actually do today? Tools, workflows, workarounds. Past behaviour. |
| **Pain points** | Where it breaks, where they pay a tax, where they've given up. Concrete instances, not generalisations. |
| **Surprises** | What didn't fit your hypothesis going in. These are usually the most valuable. |
| **Open questions** | What you wish you'd asked. Feeds the next interview brief. |

Don't force every dimension to fill — if jobs didn't come up clearly, say so.

## Phase 4 — Confidence-rate every inference

For each inference (not for verbatim quotes — those are findings):

- **High** — multiple statements support it, participant emphasised it, no contradicting signal in the transcript
- **Med** — some support, but you're connecting dots
- **Low** — speculative; you're naming a possibility for the next interview to probe

If most inferences come out Low, that's fine — write it. The team needs to see the uncertainty.

## Phase 5 — Output

Save to `discovery/summaries/<participant-slug>-<YYYY-MM-DD>.md`:

```markdown
# Interview summary — [Participant first name, segment]

**Session date:** [YYYY-MM-DD]
**Method:** Discovery / Usability
**Recording:** [path or tool link]
**Transcript:** [path]
**Linked script:** [path to interview-script file]
**Outcome / assumption probed:** [one line]
**Linked Linear ticket:** [STU-XXX or "n/a"]
**Trio attended:** [Moderator] · [Note-taker] · [Observer]

## Top 3 takeaways

1. [Most important finding — one sentence] (Confidence: High / Med / Low)
2. [...]
3. [...]

## Findings (verbatim)

- [Verbatim quote] — [timestamp] — _re: [topic]_
- [Another quote] — [timestamp] — _re: [topic]_
- [...]

## Jobs surfaced

- **Functional:** [what they're trying to get done] (Confidence: H/M/L)
- **Emotional:** [how they want to feel doing it]
- **Social:** [how they want to be perceived]

## Current behaviour

- [Specific action they take today, with quote support if available]
- [...]

## Pain points

- [Pain — concrete, not generic] — [verbatim quote if available] (Confidence: H/M/L)
- [...]

## Surprises

- [Something that didn't fit the going-in hypothesis] (Confidence: H/M/L)
- [...]

## Open questions for next interview

- [...]
- [...]

## Action items

- [What changes in the OST as a result — link to opportunity / solution / assumption test]
- [Follow-up needed — recruit, follow-up interview, internal stakeholder]
```

If a Linear ticket is linked, post a 5-line summary as a comment via `mcp__linear-server__save_comment` (resolve issue with `mcp__linear-server__get_issue`). Pattern reference: `manfred-dev:test-my-code` Linear update section.

## Manfred lens

- **Research isn't a phase** (principle 2) — every summary updates the OST, not just a folder
- **Customer-driven always** (principle 1) — verbatim quotes preserve the customer's actual voice, not the team's interpretation of it
- **Craft seriously** (principle 3) — confidence ratings are precision; vague summaries are sloppy

## Cross-plugin handoffs

- **Input from `manfred-design-research:interview-script`** — the script + recording produces the transcript
- **Output to `manfred-design-research:affinity-diagram`** — when synthesising 3+ summaries together
- **Output to `manfred-design-research:user-archetype`** — when patterns across summaries form behavioural archetypes
- **Output to `manfred-design-research:journey-map`** — when summaries map to journey stages
- **Output to `manfred-discovery:opportunity-solution-tree`** — action items update the tree
- **Output to `manfred-discovery:discovery-readout`** — Friday synthesis aggregates summaries into a cycle readout

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "Just give me the top-line, skip the verbatim" | Verbatim is the audit trail. Without it, future-you can't challenge the inference. Keep them. |
| "Confidence ratings are subjective — skip them" | Yes, subjective — but the explicit reason for the rating is the value. Skip the letter, keep the reason. |
| "Inference is more useful than what they said" | Both are useful. Separate them. The team needs to see the seam. |
| "Top 3 takeaways is too restrictive — I have 8" | If you have 8 top-line findings, none of them are top-line. Force the prioritisation. |
| "Disconfirmation isn't a finding worth writing up" | It's the most valuable finding, especially on a hypothesis-driven cycle. Surprises and refutations get top billing. |

## Red flags — STOP

- About to skip verbatim quotes because "the inferences are good enough" → Stop. Verbatim is the audit trail.
- About to claim High confidence on a single statement → Stop. High needs multiple supporting statements.
- About to omit "Open questions" → Stop. The next interview's brief comes from here.
- About to summarise without reading the transcript end-to-end first → Stop. Patterns appear on second read.
- About to write findings the participant didn't actually say or behave → Stop. That's not a finding, it's a hypothesis. Move to "Open questions."

## Tools used

- **Read**: the transcript file
- **Write**: `discovery/summaries/<participant-slug>-<date>.md`
- **MCP** (when ticket linked): `mcp__linear-server__get_issue`, `mcp__linear-server__save_comment`
- **Skills called**:
  - `manfred-design-research:affinity-diagram` — multi-summary synthesis
  - `manfred-discovery:opportunity-solution-tree` — OST updates
- **Reference**: Steve Portigal, *Interviewing Users* (synthesis chapter); Erika Hall, *Just Enough Research*

---

*Adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) (MIT). Verbatim/inference discipline, confidence labelling, and Manfred OST integration are original.*
