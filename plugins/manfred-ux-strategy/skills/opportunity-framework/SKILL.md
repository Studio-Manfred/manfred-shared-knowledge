---
name: opportunity-framework
description: Use when identifying, evaluating, and prioritising design opportunities — anyone says "prioritise these ideas", "what should we work on", "RICE scoring", "impact-effort matrix", "Kano model", "build a roadmap", "rank these opportunities", "pick the next 3 things". Manfred-flavoured: outcomes over outputs, multiple frameworks for triangulation, customer evidence first.
---

# opportunity-framework

A pile of ideas isn't a roadmap. The opportunity framework turns possible improvements into a ranked, defensible list — with reasoning the team can re-litigate later when something changes.

Manfred runs opportunities through more than one framework (impact-effort + RICE + sometimes Kano). Triangulation surfaces disagreements between frameworks; those disagreements are usually where the most interesting bets live.

## Overview

Three frameworks, used together:

1. **Impact-effort matrix (2×2)** — fast, intuitive, good for first pass
2. **RICE** — quantitative, comparable across opportunities, slower
3. **Kano model** — captures user emotional response (must-be vs delighter)

Plus **value-vs-complexity** for engineering-shaped trade-offs.

The output is a ranked list with theme groupings, dependencies, confidence levels, and the reasoning behind every ranking. The reasoning is the thing — without it, the list rots the moment context changes.

## When to use

- Quarterly / annual planning across many candidate opportunities
- Picking the next 2–3 things to work on after a discovery cycle
- Prioritising backlog items where intuition isn't producing agreement
- Defending a roadmap to stakeholders ("why is X above Y?")
- Re-prioritising mid-quarter after new evidence

**Skip when:**

- The user has 1–3 opportunities and a clear winner (don't manufacture process — just pick)
- The user wants opportunity *generation* (use `manfred-discovery:opportunity-solution-tree`)
- The user wants assumption testing (use `manfred-discovery:assumption-test`)

## Pre-flight

Ask:

- How many opportunities are in the pile? (3 → no framework needed; 10–30 → impact-effort + RICE; 30+ → narrow first.)
- What's the source of these opportunities? (User research? Stakeholder asks? Analytics? Support tickets? Competitive analysis?)
- What's the time horizon for the prioritised list? (Sprint? Quarter? Year?)
- Are they all the same shape? (E.g. "all features for product X" vs "mix of features, debt, research, hiring" — frameworks work better on like-with-like.)
- Who will use the prioritised list to make decisions, and what decisions specifically?

If the pile is 50+ opportunities, narrow first — drop anything with no user evidence, anything off-strategy, anything the team has explicitly rejected before. Frameworks on 50 noisy items take all day and produce nothing trustworthy.

## The hard rules

| Rule | What it means |
|---|---|
| **Customer evidence floor** | Every opportunity has at least one source citation (research, ticket, analytics, competitive). Opportunities without evidence get marked "needs validation" and don't compete with evidenced ones. |
| **Multiple frameworks** | Single-framework rankings produce false confidence. Run impact-effort + RICE; flag disagreements; investigate disagreements. |
| **Reasoning, not just scores** | Every ranking comes with a 1–2 sentence "why this is here". Scores rot; reasoning stays useful. |
| **Confidence levels stated** | Some opportunities are well-evidenced (high confidence); some are guesses (low confidence). Score and rank reflect both. High-impact / low-confidence opportunities go to assumption testing, not directly to build. |
| **Theme groupings** | After ranking, group by theme — onboarding, retention, support, infrastructure. Helps the team see if the top 5 all land in one area (often a sign of bias). |
| **Revisit cadence stated** | Rankings without a revisit date become permanent. Ship a date — "we revisit this list at end of quarter / after the next research cycle". |
| **Outcomes, not outputs** | Opportunities phrased as outcomes ("reduce KYC abandonment from 38% to 15%"), not outputs ("build a progress indicator"). The how comes later. |

## The flow

### Step 1 — Inventory the opportunities

For each opportunity, capture:

```markdown
| ID | Opportunity (outcome-shaped) | Source | Evidence | Confidence (H/M/L) |
|---|---|---|---|---|
| 01 | Reduce KYC abandonment from 38% to 15% | Research (n=8, 2026-04) + analytics | "users abandon during the wait when they don't know how long" | H |
| 02 | Increase joint account adoption | Stakeholder ask (CEO) | none | L |
| 03 | Launch dark mode for the dashboard | Support tickets (n=42 in 90 days) | "tickets requesting dark mode" | M |
```

Anything with confidence L gets flagged for assumption testing before competing for engineering effort.

### Step 2 — Impact-effort first pass

Plot every opportunity on a 2×2:

```
                        EFFORT
                        Low    High
                        ─────  ─────
        High      ┌──────────┬──────────┐
                  │  Quick   │ Strategic│
        IMPACT    │   wins   │   bets   │
                  ├──────────┼──────────┤
        Low       │ Fill-ins │Deprioritise│
                  └──────────┴──────────┘
```

- **Quick wins** — high impact, low effort. Do these now.
- **Strategic bets** — high impact, high effort. Plan, validate, commit.
- **Fill-ins** — low impact, low effort. Pick up between bigger work.
- **Deprioritise** — low impact, high effort. Defer or kill.

This is the cheap pass. Useful for cutting the list, surfacing the obvious-go and obvious-no-go.

### Step 3 — RICE for the contested middle

For opportunities that didn't sort cleanly via impact-effort (or for the top 10–15 the team is debating), run RICE:

| Factor | Definition | Scale |
|---|---|---|
| **Reach** | How many users / customers affected per time period | Number (e.g. "users per month") |
| **Impact** | How much does it move the needle for those users | 1 (low) – 3 (high), allow 0.5 increments |
| **Confidence** | How sure are we about the estimates | 0%–100% |
| **Effort** | Person-weeks to build | Number |

**RICE score = (Reach × Impact × Confidence) ÷ Effort**

Higher score = higher priority.

```markdown
| ID | Opp | Reach (users/mo) | Impact (1–3) | Confidence (%) | Effort (person-wks) | RICE |
|---|---|---|---|---|---|---|
| 01 | Reduce KYC abandonment | 12,000 | 3 | 80% | 6 | 4,800 |
| 02 | Joint account adoption | 800 | 2 | 30% | 8 | 60 |
| 03 | Dark mode | 45,000 | 1 | 90% | 4 | 10,125 |
```

RICE is approximate. It's useful for *comparing*, not for absolute confidence. A RICE of 4,800 vs 60 is a real signal; 4,800 vs 4,500 is noise.

### Step 4 — Disagreement check

Compare impact-effort vs RICE rankings. Where do they disagree?

- An opportunity ranked "quick win" in impact-effort but middle-of-the-pack in RICE — usually means it affects a small audience (low Reach) or is less impactful than gut suggests
- An opportunity ranked "deprioritise" in impact-effort but high RICE — usually means Reach is much larger than gut suggests
- An opportunity in "strategic bets" that has low Confidence — must go through assumption testing first

The disagreements are the most interesting outputs. Investigate, refine, re-rank.

### Step 5 — Optional: Kano for emotional shape

For opportunities competing for primacy in the user's perception, Kano helps decide what's worth the polish budget:

| Category | What it means | Example |
|---|---|---|
| **Must-be** | Users expect it; absence kills satisfaction; presence is invisible | Sign-up doesn't break |
| **One-dimensional** | More is better; investment scales linearly | Speed of dashboard |
| **Attractive (delighter)** | Users don't expect it; presence delights; absence is not missed | Surprise-and-delight transaction confirmation |
| **Indifferent** | Users don't care either way | Theme variants for power-user UI |
| **Reverse** | Users prefer LESS; "feature" is a negative | More frequent re-auth prompts |

Use Kano sparingly — it's slow, often debated. Worth it when the team is investing heavily in polish and needs to know what's earning value vs what's invisible.

### Step 6 — Ranked list with reasoning

Final output:

```markdown
## Ranked opportunities (Q3 2026)

| Rank | ID | Opportunity | RICE | Confidence | Theme | Why this rank |
|---|---|---|---|---|---|---|
| 1 | 01 | Reduce KYC abandonment | 4,800 | H | Onboarding | Strong evidence, large reach, clear hypothesis. Owns Q3. |
| 2 | 03 | Dark mode | 10,125 | M | Polish | High RICE driven by reach; impact is moderate. Pair with Q3 dashboard work. |
| 3 | 02 | Joint accounts | 60 | L | Expansion | Stakeholder priority but no user evidence. Goes to assumption test before competing for build. |

## Theme groupings
- Onboarding (3 opportunities) — biggest concentration; reflects current research focus
- Polish (2 opportunities)
- Expansion (1 opportunity, low confidence)
- Infrastructure (0 opportunities — gap; team should discuss)

## Dependencies
- Opp 01 (KYC) depends on compliance team capacity in May
- Opp 03 (dark mode) depends on `manfred-design-systems:theming-system` rollout

## Revisit
This list will be revisited [date] after the next discovery cycle's findings.
```

## Output format

Save to `discovery/opportunities/<scope-slug>-<YYYY-MM-DD>.md`.

Include:
- The inventory (all opportunities, evidenced)
- Impact-effort 2×2 (table or ASCII grid)
- RICE table for the contested middle
- Disagreement notes
- Kano (if used)
- Final ranked list with reasoning
- Theme groupings
- Dependencies
- Revisit date

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Impact-effort is enough, RICE is over-engineering" | Single-framework ranking is over-confident. Triangulation surfaces the disagreements that matter. |
| "Stakeholder priorities should override the framework" | Fine — but capture them as low-confidence opportunities and run them through assumption testing. Don't pretend they're top of the list because someone said so. |
| "Confidence is hard to estimate, just leave it out" | Confidence is the most important number in RICE. Hard to estimate = important to estimate. Ranges are OK. |
| "We'll just pick the top 5 and start, the reasoning isn't important" | Reasoning is what survives when context changes. Without it, every revisit re-litigates from scratch. |
| "No need to revisit, the list is good for the year" | Lists go stale within weeks of new research. Set a revisit date or accept that the list will be ignored. |
| "Outputs are more concrete than outcomes — easier to rank" | True, but ranking outputs locks in the *how* before the team has earned it. Rank outcomes; pick how during the build. |

## Manfred lens

Opportunity prioritisation touches all four **Cagan risks**:

- **Value** — does this actually serve a user need? (covered by Confidence + customer evidence)
- **Usability** — can users actually use it? (often unknown at prioritisation; surfaces during assumption testing)
- **Feasibility** — can we build it? (covered by Effort)
- **Viability** — does the business want it? (covered by Reach + business metric link)

A complete prioritisation considers all four. Pure RICE captures Reach + Effort well, Value moderately, Usability poorly. Pair with `manfred-discovery:cagan-risks` for the gaps.

Critical & ethical (principle 6): some opportunities have negative externalities even when RICE looks good. Always include a "harm check" — "if this opportunity ships and works as intended, who could be hurt? Mitigation?" Skip the check, ship the harm.

## Cross-references

- `manfred-discovery:opportunity-solution-tree` — opportunities live on the OST; this skill prioritises among them
- `manfred-discovery:assumption-test` — low-confidence opportunities go here before competing for build
- `manfred-discovery:cagan-risks` — fills the framework gaps (Value, Usability)
- `manfred-ux-strategy:metrics-definition` — every opportunity should map to an outcome metric
- `manfred-ux-strategy:competitive-analysis` — competitive gaps feed opportunities
- `manfred-design-research:affinity-diagram` — research themes feed opportunities

## Tools used

- `Read` — existing roadmap, OST, research outputs
- `Write` — produce the ranked list
- `manfred-discovery:opportunity-solution-tree` — opportunity source
- `manfred-discovery:assumption-test` — for low-confidence opportunities
- `manfred-discovery:cagan-risks` — to fill framework gaps

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
