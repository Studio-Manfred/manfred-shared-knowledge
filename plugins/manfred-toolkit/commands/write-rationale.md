---
description: Write a design rationale for a major decision — decision + context + alternatives + evidence + reasoning + trade-offs + validation plan.
argument-hint: [decision + scope, e.g. "rationale for using bottom-sheet for mobile filters in the Settings page"]
---

You're writing a design rationale. The user mentioned: $ARGUMENTS

## Step 1 — Confirm the decision is real

Ask:

- **What's the specific decision?** "Use bottom-sheet for mobile filters" — not "improve mobile filtering".
- **Has it been made?** If not — push back. The rationale skill captures decisions; it doesn't make them. Run `manfred-design-ops:design-critique` or `manfred-design-ops:design-review-process` first.
- **Who decided?** (Trio + accountable per RACI)
- **Audience?** Future teammates? Stakeholders for sign-off? Reviewers in critique?
- **Where will it live?** (project decisions/ dir, Linear ticket, Storybook MDX, repo CLAUDE.md)
- **Linear ticket?**

If the decision is "we always do X" — it's a pattern, not a decision. Use `manfred-design-systems:pattern-library` instead.

## Step 2 — Run the design-rationale skill (`manfred-toolkit:design-rationale`)

Run the `design-rationale` skill to produce the seven-section structure:

1. **Decision** — what was chosen, specifically
2. **Context** — what problem prompted it, what constraints
3. **Options considered** — alternatives with brief description
4. **Evidence** — research, data, principles cited
5. **Reasoning** — why this option won
6. **Trade-offs** — what was given up, what was deprioritised
7. **Validation plan** — how we'll know if the decision was right

Save to `decisions/<slug>-<YYYY-MM-DD>.md`.

## Step 3 — Cite evidence, not preference

For the evidence section, cite specifically:

- Research session (date + n + key finding)
- Analytics event (specific metric movement)
- Manfred design principle (cite by number from `~/.claude/shared/design-principles.md`)
- Customer verbatim
- Competitive analysis finding (`manfred-ux-strategy:competitive-analysis`)
- Prior rationale that informed this one

If the evidence is "I prefer X" — push back. Rationales without evidence are preference dressed as reason.

## Step 4 — Name the trade-offs

For the trade-offs section, force the user to name:

- **What we chose**: the decision's strength
- **What we gave up**: the cost of the choice
- **Deprioritised**: feature / approach we noted but didn't pursue

A rationale without trade-offs is propaganda. Without naming what was given up, future-you can't tell if the decision was right.

## Step 5 — Validation plan

How will we know if this decision was right?

- **Quantitative signal**: metric + baseline + expected movement + when measured (`manfred-ux-strategy:metrics-definition`)
- **Qualitative signal**: what we'll hear from customers if it's working
- **Revisit date**: when we'll re-examine this decision
- **Reversal cost**: if the decision proves wrong, how hard is it to reverse?

Decisions without validation plans can't be evaluated. The plan is part of the decision, not separate.

## Step 6 — Voice pass

Apply `~/.claude/shared/manfred-brand.md` rules:

- Direct, fragments OK
- No marketing verbs (transform, empower, leverage)
- No hedging ("perhaps", "we might be able to")
- Specific over generic ("Reduced steps from 6 to 3 for the typical user" not "simplified the flow")

## Step 7 — Linear update

If a Linear ticket is in scope, post the rationale (or a link to the saved file) as a comment via `mcp__linear-server__save_comment`.

## Wrap-up

Confirm the rationale covers:

- [ ] Decision named specifically
- [ ] Context (problem + constraints) clear
- [ ] 2-3 alternatives considered, briefly
- [ ] Evidence cited (research, principle, data — not preference)
- [ ] Reasoning connects to user need or design principle
- [ ] Trade-offs named (what was chosen, what was given up)
- [ ] Validation plan with metric + revisit date
- [ ] Voice passes the read-aloud test

Then offer:

> "Cross-link this rationale from the relevant `manfred-design-systems:component-spec` if it's about a component, or from the `manfred-toolkit:case-study` if it's part of a project narrative. Revisit on the date set."
