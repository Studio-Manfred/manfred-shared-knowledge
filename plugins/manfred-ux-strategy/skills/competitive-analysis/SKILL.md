---
name: competitive-analysis
description: Use when comparing UX patterns, features, strengths, and gaps across rival products — anyone says "competitive analysis", "competitor audit", "benchmark our competitors", "what are X and Y doing", "competitive landscape", "feature comparison", "UX teardown of competitors", "find market gaps". Manfred-flavoured: structured, evidence-based, pattern-focused; not feature-counting.
---

# competitive-analysis

A competitive analysis tells the team what's already solved, what's still broken across the category, and where this product can credibly differ. It's not a feature checklist — it's UX evidence that informs strategy.

Done well, it surfaces opportunities the team can't see from inside their own product. Done badly, it produces a 40-row spreadsheet that nobody opens twice.

## Overview

Three lenses, one output. The lenses are:

1. **Direct competitors** — same problem, same audience
2. **Indirect competitors** — same problem, different audience (often the most useful)
3. **Aspirational benchmarks** — best-in-class from adjacent domains

The output is a structured report saved under `discovery/competitive/`. The report ties findings to **strategic opportunities** the team can act on — not just observations.

## When to use

- Starting a new product or feature where similar things already exist
- Refreshing strategy mid-project ("are we still credibly different?")
- Pre-discovery for a new client engagement (understand the category before talking to users)
- Identifying patterns to mirror (so the product is learnable) vs patterns to break (so it's distinctive)
- Briefing a design review or workshop with category context

**Skip when:**

- The user wants to copy a competitor feature (don't help with that — instead, ask why; if the feature serves a real user need, the answer comes from research, not from a competitor screenshot)
- The product genuinely has no competitors (rare; if true, the user usually means "no direct competitors" — go indirect or aspirational)
- The user wants a sales-style comparison ("we're better than X because…") — different artifact, different skill (marketing, not UX)

## Pre-flight

Ask, before scoping:

- Who's the audience for this analysis? (Internal strategy? Client briefing? Designer onboarding?)
- What strategic question does it answer? (If "we just want to look around" — push for a question first.)
- How will it be used? (One-shot reference doc → comprehensive. Recurring tracking → narrow + repeatable.)
- What's the budget? (One day → 3 competitors, 2 lenses. One week → 8 competitors, full structure.)

If the user can't name the strategic question, don't run a generic audit. Ask them to name 2–3 trade-offs they're trying to anchor with this work — then scope around those.

## The flow

### Step 1 — Pick competitors

For each lens, name 2–4 candidates. Total: usually 6–10 products.

| Lens | What to pick | Examples (in a fictional fintech context) |
|---|---|---|
| **Direct** | Same problem, same audience — the products users mention when comparing | Revolut, N26, Klarna |
| **Indirect** | Same problem, different audience — often where the most interesting solutions live | Stripe Atlas, Wise Business |
| **Aspirational** | Best-in-class from adjacent categories — sets the bar for craft | Linear (B2B SaaS UX), Apple Wallet (consumer trust UX) |

Don't include 12 direct competitors. The marginal one teaches nothing. Width across lenses beats depth in one lens.

### Step 2 — Define evaluation dimensions

Pick 4–6 dimensions relevant to the strategic question. Common ones:

- Information architecture (navigation, content structure, terminology)
- Interaction patterns (forms, lists, transitions, gestures)
- Visual design (hierarchy, density, brand expression)
- Content / copy (tone, microcopy, error language)
- Onboarding / first-run
- Performance (perceived speed, loading, responsiveness)
- Accessibility (axe scan, keyboard nav, screen reader spot-check)
- Mobile experience (touch targets, gestures, orientation)
- Trust signals (especially in regulated / financial / health contexts)

Skip dimensions that don't serve the question. A nav audit when the question is "what's the trust pattern in onboarding" wastes attention.

### Step 3 — Run the comparison matrix

For each key user task (3–5 tasks max — the ones tied to the strategic question), score every competitor:

| Task | Competitor | Support level | Steps | UX quality (1–5) | Unique approach |
|---|---|---|---|---|---|
| Open an account | Revolut | full | 6 | 4 | BankID-first, defaults to EU residency |
| Open an account | N26 | full | 9 | 3 | Document upload heavy, slow KYC |
| Open an account | Klarna | partial | — | — | Doesn't actually open accounts (different product) |

Quality scoring is subjective — that's fine. Justify each score with one observation. ("4 — BankID flow takes 90 seconds, no document upload, clear progress indicator.")

### Step 4 — Per-competitor profile

Short profile per competitor (200–400 words):

```markdown
### <Competitor> — [direct | indirect | aspirational]

**One-line take.** What this competitor is, in one sentence.

**Strengths (2–3).** What they do well. Be specific — "fast onboarding (90s)" not "good UX".

**Weaknesses (2–3).** Where they break down. Specific moments — "post-signup empty state has no clear next action".

**Unique pattern.** One thing they do that nobody else does. (May or may not be good — note both.)

**What we should learn from them.** Concrete pattern to mirror or break.
```

### Step 5 — Synthesise to opportunity map

This is where most analyses fail. A list of competitor strengths and weaknesses isn't strategy. The synthesis turns observations into actionable opportunities:

```markdown
## Opportunity map

### Table-stakes (do these or lose)
[Patterns 80%+ of competitors ship — skipping them is a tax]
- BankID-first sign-up
- Real-time transaction notifications
- In-app chat support

### Gaps in the category (real opportunities)
[Problems no competitor solves well]
- Multi-currency mental model — every product makes this confusing; clear frame would differentiate
- Dispute / chargeback UX — universally bad, often the moment trust breaks
- Joint accounts — only 2 of 6 competitors support; weak UX on both

### Aspirational lifts
[Patterns from outside the category to import]
- Linear's keyboard-first interaction — applies to power-user workflows
- Apple Wallet's tactile transaction confirmation — could anchor trust moments

### What we should NOT do
[Patterns common in the category but actively bad — explicit choice not to copy]
- Gamified onboarding (rings, streaks, confetti) — common but breaks trust in financial context
- Aggressive cross-sell in receipts — universally tolerated, universally hated
```

### Step 6 — Tie back to the strategic question

The report's last section answers the original strategic question. If the question was "where can we credibly differentiate?", the answer is 2–3 specific bets backed by the opportunity map.

If the analysis can't answer the original question, say so — and name what additional input is needed (more research, narrower scope, different competitors).

## Output format

Save to `discovery/competitive/<scope-slug>-<YYYY-MM-DD>.md`:

```markdown
# Competitive analysis: <scope>

**Date**: YYYY-MM-DD
**Strategic question**: [the one-line question this analysis serves]
**Scope**: [N competitors across direct / indirect / aspirational]

## Summary
[3–5 sentences. Top finding, top opportunity, top "do not do".]

## Comparison matrix
[The table from Step 3]

## Per-competitor profiles
[The profiles from Step 4]

## Opportunity map
[The synthesis from Step 5]

## Answer to the strategic question
[2–3 bets, backed by the opportunity map]

## Limitations
[What this analysis didn't cover; what additional input would sharpen it]
```

## Common rationalisations

| Excuse | Reality |
|---|---|
| "We just need to know what features competitors have" | Feature lists don't make strategy. Patterns and trade-offs do. Compare experiences, not feature checkboxes. |
| "Let's analyse 20 competitors to be thorough" | The 20th teaches less than the 5th. Width across lenses (direct / indirect / aspirational) beats depth in one lens. |
| "We don't have time for indirect competitors" | The indirect lens is where the interesting solutions usually live. Direct-only analysis confirms the category; indirect reframes it. |
| "Quality scoring is subjective" | Yes. That's fine. Score with a one-sentence justification per number. Subjective + justified > pretending objectivity. |
| "Let's just collect screenshots, we'll analyse later" | "Later" doesn't happen. Synthesise as you go — the opportunity map should be drafted before the report is final. |
| "The findings are just observations, the team will figure out what to do" | They won't. Observations without recommended bets are decoration. Tie every finding to a specific opportunity or "do not do". |

## Manfred lens

Competitive analysis touches **value risk** (Cagan) — what does the market already get right, where's the credible space to differ? It also feeds **opportunity-solution tree** work (`manfred-discovery:opportunity-solution-tree`) — competitive gaps become opportunities to validate via research.

But: competitive analysis is *not* user research. A pattern that 5 competitors ship may still be wrong for users. The output of this skill *informs* discovery; it does not replace it. Cite competitors as evidence of what's been tried, not as evidence that users want it.

## Tools used

- `Bash` / `Read` — for any locally-cached competitor screenshots, reports, or notes
- `Write` — produce the report
- `manfred-design-research:user-archetype` — to confirm the audience matches across "direct" competitors
- `manfred-discovery:opportunity-solution-tree` — competitive gaps feed opportunities
- `manfred-discovery:assumption-test` — every "credibly different" bet from this analysis becomes an assumption to test

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
