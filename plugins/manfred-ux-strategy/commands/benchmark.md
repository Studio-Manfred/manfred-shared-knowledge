---
description: Benchmark a product against competitors and adjacent best-in-class — competitive analysis + experience-map gap-finding + opportunity prioritisation, ending in a defensible "where we should differ" recommendation.
argument-hint: [scope or product, e.g. "our fintech onboarding vs Revolut, N26, Wise"]
---

You're benchmarking a product against the competitive landscape. The user mentioned: $ARGUMENTS

## Step 1 — Scope the benchmark

Ask:

- What's the strategic question this serves? (If "we just want to look at competitors" — push for a question first. Examples: "where can we credibly differentiate on onboarding?", "what should we copy and what should we ignore?", "is our X pattern still defensible?")
- Which 6–10 competitors / references? (Direct, indirect, aspirational — see `manfred-ux-strategy:competitive-analysis` for the lens model.)
- What's the audience? (Internal strategy doc, client briefing, designer onboarding?)
- Linear ticket? (For posting results.)

If the strategic question isn't clear, name 2–3 trade-offs the team is trying to anchor — benchmark scope follows from those.

## Step 2 — Run competitive analysis (`manfred-ux-strategy:competitive-analysis`)

Run the full analysis:

- Pick competitors across direct / indirect / aspirational lenses
- Define 4–6 evaluation dimensions tied to the strategic question
- Score each competitor on key tasks (UX quality 1–5, with one-sentence justification)
- Per-competitor profile (strengths, weaknesses, unique pattern, what to learn)
- **Opportunity map** — table-stakes / gaps / aspirational lifts / what NOT to do
- Tie back to the strategic question with 2–3 specific bets

Save to `discovery/competitive/<scope-slug>-<YYYY-MM-DD>.md`.

## Step 3 — Map the ecosystem (optional, for cross-channel benchmarks)

If the benchmark spans multiple touchpoints / channels, use `manfred-ux-strategy:experience-map`:

- Map the user journey across competitors at each phase
- Compare ecosystem completeness — who does what well, who has gaps
- Identify cross-team handoffs that competitors handle differently

Skip this step for narrow single-touchpoint benchmarks (e.g. just "compare onboarding screens").

## Step 4 — Translate to opportunities (`manfred-ux-strategy:opportunity-framework`)

Take the gaps and aspirational lifts surfaced in Step 2/3 and run them through the opportunity framework:

- Inventory each as an opportunity with evidence (the competitive observation)
- Mark confidence (competitive evidence is M at best — "competitor X does this" doesn't mean "users want this")
- Impact-effort first pass
- RICE for the contested middle
- Disagreement check
- Ranked list with reasoning

Save to `discovery/opportunities/<scope-slug>-benchmark-<YYYY-MM-DD>.md`.

## Step 5 — Validate via discovery, not via competitive copy

For every "credibly different" bet from the benchmark, the path is **assumption test, not direct build**:

- The competitive analysis says "no competitor does X well"
- That's a candidate opportunity, not a confirmed user need
- Run `manfred-discovery:assumption-test` for each bet — design a quick test (research session, prototype, landing-page test) before committing engineering effort

This is the most important step. Benchmarks that go straight to build are how teams copy competitor mistakes.

## Step 6 — Linear update

If a Linear ticket is in scope, post a comment via `mcp__linear-server__save_comment` with:

- Path to the competitive analysis report
- Path to the opportunity ranking
- Top 3 bets the benchmark surfaced
- Recommended assumption tests for each bet

## Wrap-up

Tell the user:

- The strategic question and the answer (3–5 sentences)
- Top 3 bets with short reasoning
- "Do not do" list (specific patterns common in the category but actively bad)
- Recommended next assumption tests

Then offer:

> "Run `/manfred-discovery:risk-check` on each bet before committing engineering effort, or `/manfred-design-research:test-plan` if a usability test is the right way to validate. Don't ship a competitor-copy without testing — the gap might be there for a reason."
