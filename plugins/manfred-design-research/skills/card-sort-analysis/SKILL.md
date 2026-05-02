---
name: card-sort-analysis
description: Use when analysing the results of a card sort study (open or closed) to inform information architecture and navigation. Triggers on "card sort", "card sort analysis", "open card sort", "closed card sort", "IA from card sort", "tree test plan", "navigation grouping", "what categories did users create".
---

# card-sort-analysis

Turns card sort raw data into a recommended IA structure, with the ambiguities flagged.

## Overview

A card sort tells you how users *would* group concepts — not how the team thinks the concepts should be grouped. The two often disagree, and the disagreement is the finding.

This skill processes open or closed card sort results into:

- A similarity matrix (how often pairs of cards ended up grouped together)
- Recommended top-level categories (named in user language, not internal jargon)
- Flagged ambiguous cards (the ones that didn't cluster cleanly — the most useful signal)
- A recommended next test (almost always a tree test to validate the proposed IA)

## When to use

- Card sort study results are in (open or closed)
- Considering navigation / IA changes for a product
- Need to validate that the team's mental model matches the user's

**Skip when:**

- Working on micro-IA (within a single page or component) — usability test instead
- Sample size is under 15 — too thin for clustering inference; treat as exploratory only

## Two principles drive everything

1. **Use user language.** Whatever labels users created in an open sort, those are the candidate category names. Don't sanitise to internal jargon. If users called it "Inbox," it's "Inbox" — not "Communication Center."
2. **The cards that didn't cluster are the most useful signal.** Ambiguous cards (the ones split across multiple groups in similar proportions) are where the IA needs the most thought. They flag concepts users don't have a stable mental model for — which usually means *the team doesn't either*.

## Phase 1 — Pre-flight

Confirm:

- **Sort type:** Open (users created their own categories) or Closed (users sorted into pre-defined categories)
- **Sample size:** N participants. Below 15 → exploratory only; recommend running again with a larger sample before acting.
- **Tooling:** Optimal Workshop, UserTesting, Maze, custom — what export format is the data in?
- **Source data:** raw export file path. Confirm it loads cleanly.
- **Output path:** `discovery/card-sorts/<study-slug>-<YYYY-MM-DD>.md`
- **Linked outcome:** which IA decision does this serve?

## Phase 2 — Build the similarity matrix

For each pair of cards, calculate the percentage of participants who placed them in the same group. The matrix is the foundation for the rest of the analysis.

For 30 cards, that's 435 pairs — typically tooling produces this directly. If tooling didn't, generate it from the raw data.

Read the matrix for:

- **Strong pairs** (80%+ co-occurrence) — these cards almost always belong together
- **Weak pairs** (under 30% co-occurrence) — these cards are clearly separate concepts
- **Ambiguous pairs** (30–60% co-occurrence) — these are the cards that don't have a stable mental model

## Phase 3 — Identify candidate categories

For **closed sorts**: count how often each card landed in each pre-defined category. The dominant category for each card is its placement; cards with no clear dominant category are flagged ambiguous.

For **open sorts**: cluster the user-created category labels. Common labels (used by 30%+ of participants) become candidate top-level categories. Use **user phrasing** for the labels.

Aim for 5–9 top-level categories. Below 5 → too coarse, hides distinctions. Above 9 → too fine, navigation will sprawl.

## Phase 4 — Place each card

For each card:

- Place it in its dominant category if confidence is high (clear majority placed it there)
- Flag it `[ambiguous]` if no clear dominant category — note where else it commonly went
- For closed sorts where no category fits well, flag `[needs new category]` and recommend revising the closed set

## Phase 5 — Flag the ambiguities (the actual deliverable)

The ambiguous cards are usually the most valuable output. For each:

- **Why ambiguous?** Concept overlaps two categories (legitimate cross-category), or concept is unclear to users (label problem), or concept is unfamiliar (education problem).
- **Recommendation:** rename the card, place in two categories (cross-listing), or remove from the IA entirely if users don't have a mental model for it.

## Phase 6 — Recommend the next test

Almost always a **tree test** to validate the proposed IA. The card sort told you how users *would* group; the tree test tells you whether users can *find* things in your proposed structure. They're not the same question.

Sample size for the tree test: 30+ participants for a directional answer. Pre-write the tasks before recommending the test — usually 5–8 findability tasks covering high-frequency user journeys.

## Phase 7 — Output

Save to `discovery/card-sorts/<study-slug>-<YYYY-MM-DD>.md`:

```markdown
# Card sort analysis — [Study name]

**Study type:** Open / Closed
**Sample size:** N participants
**Tool:** [Optimal Workshop / Maze / etc.]
**Date analysed:** [YYYY-MM-DD]
**Linked outcome:** [from the OST]

## Summary

[2–3 sentences on what the sort tells you about users' mental model — top finding.]

## Recommended IA (top-level categories)

| Category (user-named) | Cards placed here |
|-----------------------|-------------------|
| [User-language label 1] | [card-a, card-b, card-c] |
| [User-language label 2] | [card-d, card-e] |
| [...] | |

## Ambiguous cards (the actually-useful section)

| Card | Why ambiguous | Recommendation |
|------|---------------|----------------|
| [card-x] | Split between [cat-1] and [cat-2] in roughly equal proportions; users seem unsure whether this is about A or B | Rename to "[clearer label]" / cross-list / remove |
| [...] | | |

## Strong pairs (cards that almost always grouped together)

- [card-a] + [card-b] (87% co-occurrence)
- [card-c] + [card-d] (82%)
- [...]

## Weak pairs (cards that are clearly separate concepts)

- [card-x] vs [card-y] (12%)
- [...]

## Notes on the sample

- [Any segment skews — e.g. "70% of participants were power users; the IA may not work for first-time users — recommend a balanced re-test"]
- [Any tool / data quality caveats]

## Recommended next test

**Tree test** to validate findability:

- **Tasks (5–8 high-frequency user journeys):**
  - [Task 1: "Find where you'd manage your saved invoices" → expected path]
  - [Task 2: ...]
- **Sample size:** 30+ participants
- **Success criteria:** 70%+ first-click correct on each task
```

If a Linear ticket is linked, post the recommended IA as a comment via `mcp__linear-server__save_comment`.

## Manfred lens

- **Customer-driven always** (principle 1) — IA categories use user language, not internal jargon
- **Research isn't a phase** (principle 2) — card sort recommendations include a follow-up test, not a one-shot answer
- **Simple by default** (principle 7) — 5–9 top-level categories; resist the urge to add more
- **Inclusive language** (principle 15) — category labels follow Manfred plain-language rules

## Cross-plugin handoffs

- **Output to `manfred-design-research:usability-test-plan`** — the recommended tree test
- **Output to `manfred-design-systems:naming-convention`** — when category names need to be codified
- **Output to `manfred-discovery:opportunity-solution-tree`** — IA decisions that affect the outcome

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "Sanitise the user labels into proper navigation copy" | No. The user label IS the navigation copy until you have evidence it confuses other users. |
| "Skip the tree test, the card sort is enough" | They answer different questions. Card sort = how users would group. Tree test = can users find. Both. |
| "Sample of 8 is fine for an exploratory read" | For exploratory directional sense, OK — but say so explicitly. Don't act on it as if it were N=30+. |
| "Ambiguous cards mean the study failed" | The opposite. They're the most useful finding. Surface them. |
| "The IA we already designed is close — just confirm it" | Then this isn't a card sort, it's seeking validation. Different exercise; rename and own it. |

## Red flags — STOP

- About to use sanitised "proper" category labels instead of user-created ones → Stop. User language wins.
- About to skip the ambiguous cards section → Stop. That's the deliverable.
- About to recommend acting on N<15 sample → Stop. Run again with more participants first, OR mark as exploratory only.
- About to skip the tree test recommendation → Stop. Card sort doesn't validate findability.
- About to propose >9 top-level categories → Stop. Force the prioritisation.

## Tools used

- **Read**: card sort raw data export
- **Write**: `discovery/card-sorts/<slug>-<date>.md`
- **MCP** (when ticket linked): `mcp__linear-server__get_issue`, `mcp__linear-server__save_comment`
- **Skills called**:
  - `manfred-design-research:usability-test-plan` — design the follow-up tree test
  - `manfred-design-systems:naming-convention` — codify the chosen labels
  - `manfred-discovery:opportunity-solution-tree` — record IA changes
- **Reference**: Donna Spencer, *Card Sorting: Designing Usable Categories*

---

*Adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) (MIT). Ambiguity-as-finding emphasis, user-language enforcement, and Manfred follow-up test pattern are original.*
