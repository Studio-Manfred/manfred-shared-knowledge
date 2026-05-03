---
name: design-rationale
description: Use when documenting the reasoning behind a design decision — anyone says "design rationale", "why did we choose this", "design decision doc", "ADR for design", "decision record", "rationale document", "explain this design choice". Manfred-flavoured: connects to `~/.claude/shared/design-principles.md` + customer evidence; alternatives + trade-offs named honestly.
---

# design-rationale

A design rationale is the answer to "why did we choose this?" written down at the moment of choosing. Done well, it survives team turnover, defends decisions in review, and prevents the same arguments six months later. Done badly, it's after-the-fact justification nobody trusts.

Manfred rationales are short, evidence-led, and honest about what was given up. They tie to the canonical design principles (`~/.claude/shared/design-principles.md`) and to customer evidence — not to designer preference.

## Overview

A rationale has seven sections, each scaled to the decision's weight. Trivial decisions don't need rationales (use them for the decisions that get questioned). Major decisions get all seven; minor decisions can collapse to 3-4.

1. **Decision** — what was chosen, specifically
2. **Context** — what problem prompted it, what constraints
3. **Options considered** — alternatives with brief description
4. **Evidence** — research, data, principles cited
5. **Reasoning** — why this option won
6. **Trade-offs** — what was given up; what was deprioritised
7. **Validation plan** — how we'll know if the decision was right

## When to use

- Major direction decisions (information architecture, primary navigation, core flow)
- Departures from established patterns (Manfred design system, shadcn defaults, project conventions)
- Controversial or debated choices (where the team disagreed)
- Decisions that will be questioned later (by stakeholders, by future teammates, by the team itself in 6 months)
- Changes from previous approaches (what we used to do, what we're doing now, why)

**Skip when:**

- The decision is obvious / consensus (don't manufacture rationales)
- The "decision" is following a pattern (use the pattern; don't re-justify)
- The decision is a trivial visual tweak (use a comment in Figma)
- The user wants a case study (use `manfred-toolkit:case-study`)
- The user wants a brief (use `manfred-ux-strategy:design-brief`)

## Pre-flight

Ask:

- **What's the decision?** Specific. "Use bottom-sheet for mobile filters" — not "improve mobile filtering".
- **Has it been made, or are you deciding now?** Rationales written *during* the decision are more honest than ones written after.
- **Who will read this?** Future teammates? Stakeholders for sign-off? Reviewers in a critique? Adapt depth to the audience.
- **Where will it live?** Project docs? Linear ticket? Storybook? Repo CLAUDE.md? README per component?
- **Voice doc loaded?** (`~/.claude/shared/manfred-brand.md` and `~/.claude/shared/design-principles.md` for the principle anchors.)

If the decision hasn't been made yet — push back. The rationale skill is for *capturing* a decision, not for making one. If the team is still deciding, run `manfred-design-ops:design-critique` or `manfred-design-ops:design-review-process` first.

## The hard rules

| Rule | What it means |
|---|---|
| **Connects to user need or design principle** | Not just "I prefer X". Cite a Manfred design principle (per `~/.claude/shared/design-principles.md`) or a customer evidence point. |
| **Alternatives named, briefly** | List 2-3 options that were considered. Reasoning lands harder when the alternatives are visible. |
| **Trade-offs honest** | "We chose X, we gave up Y." A rationale without trade-offs is propaganda. |
| **Specific enough to defend later** | Future-you reads this in 6 months. Will it be enough to remember why? Add the specific evidence, the specific user moment. |
| **Written at decision time** | Rationales written 6 months later are reconstructions. Write during; refine after. |
| **Stored alongside the design** | Lives next to the design files (Figma description, repo `decisions/` dir, Linear ticket). Not in someone's email. |
| **Voice from `shared/manfred-brand.md`** | Direct, fragments OK, no marketing verbs, no hedging. Read aloud — would you cringe? |

## Rationale structure

```markdown
# <Decision name — short, specific>

**Date**: YYYY-MM-DD
**Decided by**: <names — Trio + accountable per RACI>
**Status**: proposed | decided | superseded by [link]

## Decision

[1-3 sentences. What was chosen, specifically. Avoid "we chose to use X to enable Y" — say "We chose X."]

## Context

[2-3 sentences. What problem this resolves. What constraints exist. What changed that prompted the decision now.]

## Options considered

### Option A — [name]
[Brief description. 2-3 sentences.]
**Pros**: [strongest argument for]
**Cons**: [strongest argument against]

### Option B — [name]
[Brief description.]
**Pros**: …
**Cons**: …

### Option C — [name]
[Brief description.]
**Pros**: …
**Cons**: …

## Evidence

[Cite specifically — research session date + n, analytics event, support ticket pattern, Manfred design principle, prior rationale that informed this one.]

- [Evidence point 1]
- [Evidence point 2]
- [Evidence point 3]

## Reasoning

[1-2 paragraphs. Why this option won, given the evidence. Connect to user need (cite specific need). Connect to design principle (cite by number from canonical 15). Connect to technical or business constraint where relevant.]

## Trade-offs

[Plain text. What we explicitly gave up. What we deprioritised.]

- **We chose**: [the decision's strength]
- **We gave up**: [the cost of the choice]
- **Deprioritised**: [feature / approach we noted but didn't pursue]

## Validation plan

[How we'll know if this decision was right. What metrics or signals will confirm? When will we revisit?]

- **Quantitative signal**: [metric + baseline + expected movement + when measured — `manfred-ux-strategy:metrics-definition`]
- **Qualitative signal**: [what we'll hear from customers if it's working]
- **Revisit date**: [when we'll re-examine this decision]
- **Reversal cost**: [if the decision proves wrong, how hard is it to reverse?]
```

## Sizing

- **Major decision** (architecture, navigation, primary flow): all 7 sections, ~600-800 words
- **Significant decision** (component variant, pattern choice): 4-5 sections, ~300-400 words
- **Minor decision** (visual tweak with rationale needed): decision + 1-line context + 1-line reasoning, can fit in a Figma comment

Don't over-document. The goal is *defensible*, not *exhaustive*.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "We don't need a rationale, the team agrees" | Agreement now ≠ agreement in 6 months when team has changed. Rationales are for the future, not the present. |
| "I'll write it after the design ships" | After-shipping rationales are reconstructions. Write at decision time; the evidence is fresh, the alternatives are remembered, the trade-offs are honest. |
| "Trade-offs section is too negative" | Trade-offs section is what makes the rationale credible. Without it, the doc reads as propaganda. |
| "The reasoning is obvious; everyone knows" | "Obvious" today is "wait, why?" in 6 months. Write it down. |
| "I'll skip the alternatives — we never seriously considered them" | If you didn't consider alternatives, the decision was a default, not a choice. Surface that in the rationale ("we defaulted to X because…") rather than pretending there was a deliberation. |
| "Validation plan is engineering's problem" | Without a validation plan, the decision can't be evaluated. The plan is part of the decision, not separate from it. |

## Red flags — STOP

- About to write reasoning that reduces to "I prefer X" without principle or evidence cited
- About to skip the trade-offs section
- About to write a rationale for a decision that hasn't been made yet (run a critique / review instead)
- About to use marketing verbs (transform, empower, leverage)
- About to claim "everyone agrees" as the reasoning
- About to write a 2,000-word rationale for a 1-component decision
- No validation plan — decision can't be evaluated

## Manfred lens

Design rationales touch all four **Cagan risks** indirectly:

- **Value** (does this solve a user need?) — the evidence section
- **Usability** (can users actually use this?) — the validation plan
- **Feasibility** (can engineering build it?) — the trade-offs section often surfaces this
- **Viability** (does the business want it?) — the context section

Rationales also enforce **design principle 14 (design with data)** — by requiring evidence over preference and a validation plan to measure outcome.

Critical & ethical (principle 6): every rationale should include a thought on what this decision *does in the world*. If the decision optimises for engagement at user expense, the rationale should surface that — and a justified rationale should defend it (or it shouldn't be the decision).

## Cross-references

- `~/.claude/shared/design-principles.md` — the canonical 15 principles cited in rationales
- `~/.claude/shared/manfred-brand.md` — voice rules
- `manfred-design-ops:design-critique` — the format that produces the decision the rationale captures
- `manfred-design-ops:design-review-process` — gates where rationales get reviewed
- `manfred-design-ops:handoff-spec` — handoffs reference rationales for non-obvious decisions
- `manfred-toolkit:case-study` — case studies reference rationales for the "key decisions" section
- `manfred-discovery:opportunity-solution-tree` — opportunities + solutions on the OST often have rationales

## Output format

Markdown rationale, save to `decisions/<slug>-<YYYY-MM-DD>.md` (or wherever the project keeps them — Storybook MDX, Notion, Linear ticket comment).

If the decision is in scope of a Linear ticket, post the rationale (or a link to it) as a comment via `mcp__linear-server__save_comment`.

## Tools used

- `Read` — `~/.claude/shared/design-principles.md`, `~/.claude/shared/manfred-brand.md`, prior rationales, project artefacts
- `Write` — produce rationale doc
- `mcp__linear-server__save_comment` — post link to Linear if ticket scoped
- `manfred-design-ops:design-critique` — input source
- `manfred-toolkit:case-study` — for the case-study cross-reference

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
