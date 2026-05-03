---
description: Develop a UX strategy end-to-end — design principles + north-star vision + opportunity prioritisation + metric set, ending in a defensible direction the team can plan against.
argument-hint: [scope, e.g. "UX strategy for our 2026 fintech roadmap"]
---

You're developing a UX strategy. The user mentioned: $ARGUMENTS

## Step 1 — Confirm strategy is what's needed

Ask:

- What decision does this strategy serve? (If "we just want a strategy doc" — push for the decision. Strategy is a forcing function for trade-offs; without a trade-off, you're producing decoration.)
- What time horizon? (12 months? 3 years? 5 years? The strategy shape changes per horizon.)
- Who's the audience? (Internal team alignment? Client direction? Board pitch? Hiring narrative?)
- Is this a fresh strategy or a refresh of an existing one?

If "we just want to look strategic" — stop. Run `manfred-ux-strategy:design-brief` instead — that's framing a project, not setting strategy.

## Step 2 — Anchor in principles (`manfred-ux-strategy:design-principles`)

Strategy without principles is opportunism. Run the principles skill:

- Read Manfred's canonical 15 in `~/.claude/shared/design-principles.md`
- Walk the 15 with the team — keep, adapt, drop, extend for this engagement
- If new principles are needed, follow the testable + trade-off-stated + Manfred-voice rules
- Don't invent 5 new principles in 30 seconds — the skill refuses that and offers (a) adapt, (b) workshop kit, (c) starter set with workshop date

The principles set anchors every later strategic decision. Without it, the strategy can't tell the team what to refuse.

## Step 3 — Frame the north star (`manfred-ux-strategy:north-star-vision`)

A vision serves trade-offs. Run the north-star-vision skill:

- Vision statement (one sentence — who, what experience, why it matters)
- 3–5 design pillars with explicit trade-offs ("what we bet on / what we give up")
- Vision scenarios (narrative day-in-the-life, not bullet points)
- Time horizons (near / mid / long)
- Success criteria (qualitative + quantitative + observable milestone)
- "What this vision gives up" section — non-negotiable

The vision pulls from the principles (Step 2) and from any prior research (`manfred-design-research:summarize-interview`, `manfred-design-research:user-archetype`).

## Step 4 — Map the competitive context (`manfred-ux-strategy:competitive-analysis`)

Vision and principles need market grounding. Run competitive analysis:

- Direct + indirect + aspirational lenses
- Opportunity map (table-stakes / gaps / aspirational lifts / what NOT to do)
- Tie back to the strategic question

The output identifies where the vision can credibly differ from the market.

## Step 5 — Prioritise opportunities (`manfred-ux-strategy:opportunity-framework`)

Strategy translates into a roadmap. Run the opportunity framework:

- Inventory opportunities from research, competitive analysis, OST, stakeholder asks
- Impact-effort first pass
- RICE for the contested middle
- Disagreement check (where impact-effort and RICE disagree — investigate)
- Theme groupings, dependencies, confidence levels
- Revisit cadence

Low-confidence opportunities → `manfred-discovery:assumption-test` before competing for build.

## Step 6 — Define the metric set (`manfred-ux-strategy:metrics-definition`)

A strategy without measurement is a wish. Run the metrics skill:

- Pick 3–5 primary metrics across behavioural / attitudinal / business
- Baselines + targets + action thresholds
- HEART coverage check
- Qualitative companion plan (verbatims + spot interviews)
- Owner + cadence per metric

The metric set operationalises the success criteria from the vision (Step 3).

## Step 7 — Stakeholder alignment (`manfred-ux-strategy:stakeholder-alignment`)

Strategy that the team can't agree on isn't strategy — it's a draft. Run alignment:

- Stakeholder map for strategy decisions
- RACI for the major calls (vision approval, metric set approval, opportunity ranking)
- Communication plan for the strategy rollout
- Feedback protocol for incoming critique

Decision rights for "what does this strategy mean for X" decided **at the strategy phase**, not when the first conflict arrives.

## Step 8 — Compile the strategy doc

Combine the outputs into a single strategy document:

```markdown
# <Engagement> — UX strategy 2026–2028

**Date**: YYYY-MM-DD
**Time horizon**: [near / mid / long]
**Audience**: [internal | client | board]
**Owners**: <names>
**Sign-off**: <name>, <date>

## 1. The decision this strategy serves
[The one-line decision the strategy anchors]

## 2. Principles
[Adapted set from Step 2 — 5–8 principles, testable, trade-off-stated]

## 3. North-star vision
[Vision statement, pillars, scenarios, time horizons, success criteria, what we give up]

## 4. Competitive landscape
[Top 3 patterns to mirror, top 3 to break, top 3 to avoid; gap analysis]

## 5. Ranked opportunities
[Top 5–10 from the opportunity framework, with theme groupings and dependencies]

## 6. Success metrics
[3–5 primary, with baselines and targets]

## 7. Stakeholder alignment
[Map summary, RACI for strategy decisions, comms plan, feedback protocol]

## 8. Ethics check (Manfred principle 6)
[What does this strategy do in the world? Who could it harm? Mitigation?]

## 9. Trial frame
[This strategy is in trial through <date>. We will revisit at <event> and decide: keep, refine, retire.]
```

Save to `discovery/strategy/<engagement-slug>-<YYYY-MM-DD>.md`.

## Step 9 — Linear update

If a Linear ticket / project is in scope, post a comment via `mcp__linear-server__save_comment` with:

- Path to the strategy doc
- Top 3 strategic bets
- Top 3 assumption tests for week 1
- Sign-off status

## Wrap-up

Confirm the strategy covers:

- [ ] A specific decision the strategy anchors (not "we want a strategy doc")
- [ ] Principles set (adapted from canonical 15, not invented)
- [ ] Vision with explicit trade-offs ("what we give up" non-empty)
- [ ] Competitive grounding
- [ ] Ranked opportunities with reasoning
- [ ] Measurable success criteria
- [ ] Stakeholder alignment with sign-off
- [ ] Ethics check
- [ ] Trial frame with revisit date

Then offer:

> "Run `/manfred-discovery:kickoff` to operationalise this strategy into a discovery cycle, or `/manfred-ux-strategy:frame-problem` for the first project under this strategy. Strategies are living docs — set a quarterly revisit and treat it like a contract, not a poster."
