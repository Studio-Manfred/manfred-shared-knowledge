---
name: north-star-vision
description: Use when articulating a product vision that aligns a team and guides strategic design decisions — anyone says "north star", "product vision", "vision statement", "where are we going", "design vision", "5-year vision", "what does this product become", "vision for the team", "north star metric". Manfred-flavoured: concrete over abstract, customer-driven, ethics non-negotiable.
---

# north-star-vision

A north-star vision is the picture the team can point at when "should we build this?" stops being obvious. Not a slogan, not a tagline, not a wall poster of inspirational verbs — a description of the future product that the team can use to make a hundred trade-offs without re-arguing the fundamentals.

Manfred's north stars are concrete. "Make the product world more customer driven" is the studio's own — it tells you what to bet on (research-led work) and what to refuse (feature factories). That's a north star: directional and unambiguous.

## Overview

A north-star vision has four parts:

1. **Vision statement** — one sentence. Who, what experience, why it matters.
2. **Design pillars** — 3–5 strategic focus areas that *differentiate*. Not "be high quality" (everyone says that) — what specifically does this product bet on?
3. **Vision scenarios** — concrete narrative stories of the future experience. Day-in-the-life, not abstractions.
4. **Success criteria** — qualitative signals + quantitative metrics + milestones. How we know the vision landed.

The vision lives across three time horizons: near-term (1 yr — tangible), mid-term (2–3 yr — major shifts), long-term (5+ yr — aspirational). All three can change; the long-term changes least.

## When to use

- A team is starting a new product or major direction shift
- The current vision feels stale, contested, or missing
- A team keeps re-arguing the same trade-offs ("should we build feature X?") because no shared direction is anchoring the decision
- A leader needs a frame to communicate strategy externally (clients, board, hiring)
- Workshopping vision in a quarterly off-site

**Skip when:**

- The user wants design principles (use `manfred-ux-strategy:design-principles`)
- The user wants a design brief for a specific project (use `manfred-ux-strategy:design-brief`)
- The user wants competitive analysis (use `manfred-ux-strategy:competitive-analysis`)
- The user wants the *team's* values rather than the *product's* future (different artifact — values doc, not north star)

## Pre-flight

Before drafting:

```bash
test -f ~/.claude/shared/design-principles.md && head -30 ~/.claude/shared/design-principles.md
test -f ~/.claude/shared/manfred-brand.md && head -60 ~/.claude/shared/manfred-brand.md
```

Find:

1. **Manfred's voice** — vision text uses warm + precise, not McKinsey
2. **Manfred's principles** — the vision can't violate principle 1 (customer-driven), principle 6 (critical & ethical), or principle 4 (warm + precise)

## The hard rules

| Rule | What it means |
|---|---|
| **Concrete over abstract** | "Make the product world more customer driven" beats "transform how teams work". Specific verbs, specific subjects, specific changes. |
| **Customer-driven floor** | The vision starts from a real human need, named. Not "users want better experiences" — *which* users, *what* moment, *what* changes for them. |
| **Pillars must differentiate** | "High quality" is not a pillar (every team says this). "Every research output is reusable across the studio" is — it tells you what to invest in. |
| **Scenarios are narratives, not bullet points** | "Lina, a customer success manager at a 50-person SaaS, opens the dashboard at 8:47am after a stand-up…" beats "users will be able to view dashboards efficiently". |
| **Trade-offs stated explicitly** | The vision says what it gives up, not just what it pursues. "We will be slower to ship features than competitors because every release is research-validated." |
| **Ethics test (principle 6)** | What does this vision *do in the world*? If the answer is "captures more attention" or "extracts more time", revise. The Manfred filter — would we be proud to ship this if our names were on the front? |
| **Manfred voice** | No "transform", "empower", "leverage", "supercharge", "unlock", "drive value". Read aloud — would you cringe? Rewrite. |

## The flow

### Step 1 — Confirm the vision serves a real decision

Ask:

- What decision is missing because the vision is missing? (If the user can't name one, the vision is decoration — don't write it yet.)
- Who is the audience? (Internal team only? External — clients, board, market?)
- Time horizon? (Vision is meaningless without one.)
- How will success be measured? (Qualitative narrative + quantitative metric + observable milestone.)

If the user says "we just feel like we should have a vision" without a decision in mind, push back: "Vision is a forcing function for trade-offs. If there's no trade-off you're trying to anchor, you're producing a slogan, not a vision."

### Step 2 — Gather inputs

A real vision pulls from:

- **Customer evidence** — what's the user need this serves? (Cite specific research, not "we believe users want…")
- **Studio / company values** — what do we genuinely care about? (`~/.claude/shared/design-principles.md` for Manfred — what's the parallel for this product?)
- **Market reality** — what are competitors doing? Where's the gap? (See `manfred-ux-strategy:competitive-analysis`.)
- **Team aspiration** — what does this team want to be in 3–5 years? (Quiet input — surface in workshop, not as a shopping list.)

If any of the four is missing, name the gap. Don't fill it with confidence.

### Step 3 — Workshop format (when working with a team)

```markdown
# Vision workshop — 90 min

**0–10 min** — Frame: vision serves trade-off decisions, not posters. Read 2–3 example visions (Manfred's "make the product world more customer driven", one good external example, one cautionary slogan-y one).

**10–30 min** — Customer story round. Each participant tells a 2-min story about a real user moment they observed in the last 90 days. Scribe the moments.

**30–55 min** — Pillar pair sketch. Each pair drafts 3 candidate pillars: <pillar title> / <what it bets on> / <what it gives up>. No pillar without a stated trade-off.

**55–75 min** — Vision sentence drafting. Single sentence: who / what experience / why it matters. Walk top 3, vote.

**75–85 min** — Scenarios. Pick the winning vision sentence + 2 pillars. Write a 3-paragraph day-in-the-life narrative for one user.

**85–90 min** — Trial frame: "we'll use this for one quarter, then revisit." Set a date.
```

### Step 4 — Draft (when working solo or after the workshop)

```markdown
# <Product / company> north-star vision

## Vision statement
[One sentence. Who. What experience. Why it matters.]

## Design pillars (3–5)

### Pillar 1 — <name>
**What we bet on.** [Concrete commitment.]
**What we give up.** [The trade-off we've already accepted.]
**How we know it's working.** [Observable signal.]

[Repeat for each pillar.]

## Vision scenarios (1–3)

### Scenario 1: <user / moment>
[3-paragraph narrative. Specific user, specific time, specific actions, specific feelings. Show the future, don't claim it.]

[Repeat for additional scenarios if needed.]

## Time horizons

### Near-term (1 year)
[Tangible improvements consistent with vision.]

### Mid-term (2–3 years)
[Major experience shifts.]

### Long-term (5+ years)
[Aspirational state — what does this product become if the vision lands?]

## Success criteria

| Type | What | Owner | Cadence |
|---|---|---|---|
| Qualitative | Customer narrative — "users say [X]" | … | quarterly |
| Quantitative | North-star metric — [single number that captures vision impact] | … | weekly |
| Milestone | Observable event — "we shipped [X] / we stopped [Y]" | … | per release |

## What this vision gives up

[Plain text. The competitors / approaches / opportunities we're explicitly choosing not to pursue. If empty, the vision isn't doing its job.]

## Trial frame

This vision is in trial through [date]. We will revisit at [event] and decide: keep, refine, retire.
```

### Step 5 — Voice pass

Read the draft aloud. For every sentence, ask:

- Would I cringe? Rewrite.
- Could this come from any company's annual report? Make it specific to this team and product.
- Does it say what we *give up*, not just what we pursue? If only the latter, add the trade-off.
- Marketing verb count: 0 is the only acceptable number.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "We need a vision because every team has one" | Every team has a slogan. A vision serves trade-offs. If there's no trade-off it anchors, you're writing decoration. |
| "Aspirational language inspires the team" | Aspirational language produces confident-sounding slides and ambiguous decisions. Specific, testable scenarios inspire and anchor. |
| "We can't say what we give up — that's negative messaging" | Visions without trade-offs are wish lists. Naming the trade-off is what makes the vision a decision. |
| "5 years is too short — let's do a 10-year vision" | 10-year visions are unfalsifiable. 3–5 years lets the team check whether the bet was right. |
| "The vision is just for internal alignment, no need for ethics" | Internal alignment around an unethical product is still building an unethical product. Principle 6 doesn't have a target audience. |
| "We'll write the metric later" | A vision without a measurable signal is a feeling. Pick a metric now, even if it's imperfect. |
| "Marketing will rewrite this for external use anyway" | Marketing rewrites lose the trade-off and the specificity. Push back — let marketing translate, not invent. |

## Red flags — STOP

- About to use "transform", "empower", "leverage", "supercharge", "unlock", "drive value", "best-in-class"
- Vision sentence that could fit any product in any industry
- Pillars that are just rephrased company values
- Scenarios written as bullet points instead of narrative
- No stated trade-off (no "what this vision gives up" section, or it's empty)
- No measurable success criterion
- Wrote the vision in <30 minutes without team input or customer evidence

## Manfred lens

Vision is **strategy** — Cagan's value risk lives here directly. A vision that doesn't anchor "is this thing worth building?" is just a brand exercise.

Cross-references:

- `manfred-ux-strategy:design-principles` — pillars derive from principles; check the canonical 15 first
- `manfred-discovery:product-brief` — Section 02 (Strategic Alignment) cites the vision
- `manfred-discovery:opportunity-solution-tree` — outcomes ladder up to the vision; the OST root *is* the near-term vision metric
- `manfred-design-research:user-archetype` — scenarios use real archetypes, not invented personas
- `manfred-ux-strategy:metrics-definition` — the success criteria need this skill to be operational

## Output format

Markdown vision document, save to `discovery/vision/<engagement-slug>-<YYYY-MM-DD>.md`.

When working with a team in a workshop, the output is the workshop kit (Step 3) first, then the draft (Step 4) after the workshop runs.

## Tools used

- `Read` — `~/.claude/shared/design-principles.md`, `~/.claude/shared/manfred-brand.md`, prior research
- `Write` — vision document or workshop kit
- `manfred-ux-strategy:design-principles` — for pillar derivation
- `manfred-ux-strategy:competitive-analysis` — for market input
- `manfred-design-research:user-archetype` — for scenario subjects
- `manfred-discovery:opportunity-solution-tree` — for vision-to-outcome anchoring
