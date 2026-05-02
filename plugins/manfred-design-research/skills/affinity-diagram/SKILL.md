---
name: affinity-diagram
description: Use when synthesising qualitative research data into themed clusters with insight statements. Triggers on "affinity diagram", "synthesise the research", "cluster these notes", "find the themes", "thematic analysis", "what patterns are in this research", "group the findings".
---

# affinity-diagram

Bottom-up clustering that turns a pile of research notes into named themes and the insight statements that come out of them.

## Overview

The affinity diagram (KJ method, after Jiro Kawakita) works because it forces you to start at the bottom — individual observations — and build up to themes, rather than top-down imposing a framework on the data. Done honestly, it surfaces patterns the team didn't expect; done lazily, it just confirms what the team already thought.

This skill walks the bottom-up clustering process and produces a markdown affinity diagram + a short insight statement per theme. Insight statements are the actionable layer — they're what the team decides off, not the clusters themselves.

## When to use

- 5+ interview summaries (`manfred-design-research:summarize-interview`) need synthesising
- Any qualitative dataset (interview notes, support tickets, NPS verbatims, observation field notes) needs structure
- Friday synthesis ritual — the cycle's summaries become themes
- Before populating an `manfred-design-research:empathy-map`, `journey-map`, or `user-archetype`

**Skip when:**

- You only have one or two data points — too thin for clustering, just summarise
- You're working from quantitative data — wrong tool, use a stats workflow

## Two principles drive everything

1. **Bottom-up, not top-down.** Don't decide the themes before reading the data. Read everything, write each observation on its own (one card per observation), then look for what wants to cluster. Theming first kills the surprise.
2. **Insight statements > theme labels.** "Trust" as a theme label means nothing on its own. "Customers don't trust the recommendation engine because it surfaces things they've already bought" is an insight statement — actionable. Themes name the cluster; insight statements name what the cluster *means*.

## Phase 1 — Pre-flight

- **Source paths:** the summaries, transcripts, notes that go in. Confirm they exist.
- **Scope:** one outcome / one product area at a time. Mixing scopes muddies the clusters.
- **Output path:** `discovery/affinity/<topic-slug>-<YYYY-MM-DD>.md`
- **Linked OST outcome:** the affinity diagram should serve a specific outcome from `manfred-discovery:opportunity-solution-tree`. If it doesn't — why are you doing this?

## Phase 2 — Extract individual observations

Read every source. For each distinct observation, write one card:

- One observation per card. If you can split it into two, split.
- Use the participant's voice where possible. Verbatim beats paraphrase.
- Tag the source: `[interview-3]`, `[ticket-cluster-X]`, `[NPS-verbatim-Y]`. Future-you will want to find the original.

A "card" here is a markdown bullet. Aim for 30–80 observation cards from a typical 5-interview cycle. If you have under 20, you're paraphrasing too aggressively. If you have over 150, you're slicing too fine.

## Phase 3 — Cluster bottom-up (silently first)

Group observations that feel like they belong together. Don't name the clusters yet. Let the groups form.

Do this in **two passes**:

- **First pass:** group on first instinct. Move quickly. Don't over-think.
- **Second pass:** look at each group. Does it actually hold together? Split groups that have multiple themes hiding inside. Merge groups that are saying the same thing in different words.

If you're synthesising as a Trio (per Manfred's discovery rituals), do the silent clustering individually first, then compare. The differences tell you where the team's mental models diverge — which is itself a finding.

## Phase 4 — Name each cluster (descriptively, not aspirationally)

Theme labels should describe what's in the cluster, not what you wish were there.

- ✅ "Customers can't tell when their data has finished syncing"
- ❌ "Trust"
- ❌ "Sync experience"

Aim for one sentence, in the customer's voice or close to it.

## Phase 5 — Write the insight statement per theme

For each theme, write one insight statement: **what does this theme mean for the team?**

Format: *"[Customer or behaviour], because [underlying reason], so [implication for the team]."*

Examples:

- "Small business users abandon multi-step setup, because they expect SaaS tools to be useful within 5 minutes, so any onboarding path over 3 steps needs to demo value before asking for setup commitment."
- "Power users resist the new dashboard, because they had memorised exact pixel positions in the old one, so layout changes for power-user surfaces need explicit migration, not just announcements."

If you can't write the insight statement, the theme isn't sharp enough — go back to clustering.

## Phase 6 — Prioritise

Not every theme deserves equal action. Rate each by:

- **Outcome impact** (Low / Med / High) — how much does this theme, if addressed, move the linked outcome?
- **Confidence** (Low / Med / High) — how strongly does the data support the theme? (Single-interview themes are Low; cross-cutting themes from multiple participants are High.)

Recommend the team focus on themes that are **High impact + High confidence** first. **High impact + Low confidence** themes go to the next research cycle as questions to probe.

## Phase 7 — Output

Save to `discovery/affinity/<topic-slug>-<YYYY-MM-DD>.md`:

```markdown
# Affinity diagram — [Topic / outcome]

**Date:** [YYYY-MM-DD]
**Outcome:** [from the OST]
**Sources:** [N summaries / interviews / data points]
**Synthesised by:** [Trio names]

## Themes (prioritised by impact × confidence)

### Theme 1 — [Descriptive label, in customer voice if possible]

**Insight statement:** [Customer/behaviour, because reason, so implication.]

**Impact:** High / Med / Low (— [reason])
**Confidence:** High / Med / Low (— [reason — multiple sources, single source, etc.])

**Observations in this theme:**
- "[Verbatim quote]" — [interview-3, 14:22]
- "[Verbatim quote]" — [interview-5, 27:10]
- [Observation paraphrase] — [support cluster #4]

### Theme 2 — [...]

[...]

## Recommended next actions

- **High impact + High confidence themes** → update the OST (`manfred-discovery:opportunity-solution-tree`) — add these as opportunities under the outcome
- **High impact + Low confidence themes** → next interview cycle should probe these specifically — add to `manfred-discovery:customer-touchpoint-plan`
- **Low impact themes** → log for visibility, don't act

## Cards that didn't cluster

[Observations that didn't fit any theme. Don't force them into clusters — they may be next cycle's seeds.]

- [Quote / observation] — [source]
- [...]
```

If a Linear ticket is linked, post a 5-line summary of top themes via `mcp__linear-server__save_comment`.

## Manfred lens

- **Research isn't a phase** (principle 2) — affinity diagrams happen weekly during synthesis ritual, not just at engagement-end
- **Customer-driven always** (principle 1) — themes phrased in customer voice, not team jargon
- **Craft seriously** (principle 3) — insight statements are precise, not generic; themes are descriptive, not aspirational

## Cross-plugin handoffs

- **Input from `manfred-design-research:summarize-interview`** — the summaries become the source observations
- **Input from `manfred-design-research:transcript-anonymizer`** — when raw transcripts are the source and PII needs removing first
- **Output to `manfred-design-research:user-archetype`** — themes about behaviour become archetype dimensions
- **Output to `manfred-design-research:journey-map`** — themes about specific journey stages populate the map
- **Output to `manfred-discovery:opportunity-solution-tree`** — High impact + High confidence themes become opportunities
- **Output to `manfred-discovery:assumption-test`** — High impact + Low confidence themes become assumption-test candidates

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "I'll start with the themes I already see, then place observations under them" | That's not affinity, that's confirmation. Bottom-up only. |
| "Theme labels can be one word — easier to remember" | One-word labels lose the meaning. "Trust" can mean five different things; the cluster is one of them. Sentence-length labels are the discipline. |
| "Insight statements are wordy — just list themes" | Themes without insight statements are vibes. Insight statements are what the team decides off. |
| "Single-interview themes are still High confidence if the participant felt strongly" | No. Confidence ≠ intensity. Single-source = Low confidence even if the participant cried. The test is "did multiple people independently surface this?" |
| "I can synthesise alone — the Trio reads my output" | They can, but they'll trust your themes more than they should and miss where you went wrong. Solo synthesis loses the divergence-as-finding. |

## Red flags — STOP

- About to write theme labels before clustering observations → Stop. Bottom-up.
- About to write themes as one-word labels → Stop. Sentence form.
- About to claim High confidence on single-source themes → Stop. Re-rate to Med or Low.
- About to skip the "cards that didn't cluster" section → Stop. They're often next cycle's seeds.
- About to action all themes equally → Stop. Prioritise by impact × confidence.

## Tools used

- **Read**: source files (interview summaries, transcripts, ticket exports)
- **Write**: `discovery/affinity/<slug>-<date>.md`
- **MCP** (when ticket linked): `mcp__linear-server__get_issue`, `mcp__linear-server__save_comment`
- **Skills called**:
  - `manfred-discovery:opportunity-solution-tree` — themes become opportunities
  - `manfred-discovery:assumption-test` — Low-confidence themes become tests
  - `manfred-design-research:user-archetype` / `journey-map` — themes populate downstream synthesis
- **Reference**: Jiro Kawakita (KJ method); Erika Hall, *Just Enough Research*

---

*Adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) (MIT). Insight-statement format, confidence × impact prioritisation, and Manfred OST integration are original.*
