---
name: design-principles
description: Use when defining, refining, or applying design principles for a team or product — anyone says "give me design principles", "principles for this project", "design principles for the wall", "we need principles", "draft principles for the design review", "what are our principles", "let's workshop principles", "team manifesto". Manfred-specific: every output references the canonical 15 in `~/.claude/shared/design-principles.md`.
---

# design-principles

Manfred has 15 canonical principles. This skill does not invent new ones from a cold start — it shows what already exists, helps the team adapt or extend for a specific engagement, and refuses to ship a "wall poster" before the team has done the work to earn it.

Principles are an *outcome of a process*, not a deliverable from a prompt.

## Overview

A design principle is a stated stance that resolves real trade-offs. "Be user-centered" is not a principle — it's a wish. "When research contradicts the brief, bring it to the brief — don't hide it" is a principle (it tells you what to do at a specific moment).

Manfred's 15 principles live in `~/.claude/shared/design-principles.md`. They cover customer-driven research, craft, voice, accessibility, ethics, simplicity, tokens, dark mode, shadcn shapes, consistency, mobile, performance, data, and inclusive language. Most engagements need a subset — not a fresh invention.

## When to use

- A team says "we need design principles for this project"
- Reviewing or refining an existing principle set
- Workshopping principles in a kickoff
- Applying principles to a specific design decision (the "this screen breaks principle 3 because…" exercise)
- Drafting principles for a client engagement
- Producing a meeting prep kit *before* a principles workshop

**Skip when:**

- The user already has principles and just wants design feedback (use the right design skill — component, pattern, etc.)
- The user wants Manfred's principles directly (just point them at `~/.claude/shared/design-principles.md`)
- The user wants brand or voice guidelines (different artifact — see `~/.claude/shared/manfred-brand.md`)

## Pre-flight (do this every time)

Before drafting anything:

```bash
test -f ~/.claude/shared/design-principles.md && cat ~/.claude/shared/design-principles.md
test -f ~/.claude/shared/manfred-brand.md && head -60 ~/.claude/shared/manfred-brand.md
```

If the canonical principles aren't readable, ask the user to install `manfred-shared-knowledge` or point you at the file. **Do not draft principles without seeing the canonical 15 first.**

## The hard rules

| Rule | What it means |
|---|---|
| **Show the 15 first** | Every output starts by referencing the Manfred 15. Adapt, don't invent. If the engagement needs something the 15 don't cover, say so explicitly and write the new one as an *extension* — not a replacement. |
| **No cold-start posters** | The user wants 5 principles for tomorrow's meeting? They get a meeting prep kit (questions for the team, workshop format, 1-week trial frame), not a finished poster. Principles emerge from the team. |
| **Testable, not aspirational** | Every principle includes a concrete violation example ("this screen breaks principle 3 because the fee total has no breakdown"). If you can't write the violation, the principle is a wish, not a rule. |
| **Trade-off partner stated** | Every principle names what it loses to. "Show the math" trades against "Respect the user's time" — when they conflict, which wins? Decide upfront, not in the moment. |
| **Manfred voice** | Warm + precise, no marketing verbs (transform, empower, leverage), no aspirational mush ("delight the user"). Read aloud — would you cringe? Rewrite. See `~/.claude/shared/manfred-brand.md`. |
| **Customer-driven first** | Principle 1 of the canonical 15 is non-negotiable. Any principle set that doesn't make customer evidence the floor isn't Manfred. |
| **Critical & ethical** | Principle 6 of the canonical 15 — "what does this design do in the world?" — is non-negotiable. Strategy without ethics is just confidence. |

## The flow

### Scenario A — User asks for principles cold ("give me 5 design principles for X")

**Stop.** Don't produce 5 principles. Respond:

```
Manfred ships 15 canonical principles in ~/.claude/shared/design-principles.md.
Drafting 5 new ones in 30 seconds, before the team has done the work, will produce
a poster that gets quietly ignored.

Better path:

(a) Show me the engagement. Which of the 15 already apply? Which need adapting
    for this product / team / context? What's missing that this engagement needs?

(b) If you're meeting the client tomorrow and need *something*, I can produce
    a meeting prep kit — questions to surface the real principles in a 60-min
    workshop, not the finished poster. The poster comes after the workshop.

(c) If the client genuinely needs an interim "starter set" by tomorrow, we can
    pull the 5 most relevant of the canonical 15 with adapted wording for this
    context — explicitly framed as "starter, will be revised after workshop."

Which way do you want to go?
```

Wait for the user's pick. Don't ship a cold poster.

### Scenario B — User picks (a): adapt the canonical 15

1. Read `~/.claude/shared/design-principles.md`.
2. Walk the 15 with the user. For each: keeps as-is / adapts / drops / extends.
3. Produce the adapted set with: same numbering or renumbered, same structure (title + body + rationale), and a section at the end called "What's different from canonical Manfred" listing the adaptations.

### Scenario C — User picks (b): meeting prep kit

Output a markdown kit:

```markdown
# Principles workshop — prep kit

## Workshop format (60 min)

**0–10 min** — Show the canonical Manfred 15 (5 min walkthrough). Frame: "these are our defaults; what does this engagement need on top?"

**10–25 min** — Pre-mortem: imagine this product launches and is a UX disaster.
What 3 trade-offs did we make wrong? (Surface the real tensions.)

**25–40 min** — Pair sketch: each pair drafts 3 principles in <principle title> /
<violation example> / <trade-off partner> form. No abstract aspirations.

**40–55 min** — Cluster + vote. 5–8 principles max. Rank order for conflict
resolution.

**55–60 min** — Trial frame: "we'll use these for 1 week, then revisit."

## Pre-workshop questions to send the team

- Which of the canonical Manfred 15 do you think doesn't apply to this product?
- What's a recent design decision where we couldn't agree?
- What did the last team here do that you don't want to repeat?
- What's one principle you'd defend even at the cost of velocity?

## What to bring to the workshop

- The canonical 15 (printed)
- 3 recent screens from the project (for testing principles against real work)
- 1 anti-example from a competitor (what we don't want to be)
```

### Scenario D — User picks (c): starter set from canonical 15

Pull 5–8 of the canonical 15 most relevant to the engagement. **Reword for the specific product context** — keep the principle but adapt the body. Add a header:

> "Starter set, drawn from the canonical Manfred 15. Will be revised by the team after the principles workshop on [date]."

This is a stop-gap, not a finished poster. Frame it that way.

**Required side-by-side check.** Output a two-column table with `Canonical wording` on the left and `Adapted wording for <product>` on the right, for every principle in the starter set. The trade-off partner and violation example carry across unchanged unless the user explicitly says "this trade-off doesn't apply to this product, here's why." This stops "adapting" from becoming "quietly inventing."

**Workshop date is not optional.** If the user can't name a date for the workshop that will revise this set, the starter set isn't being treated as a stop-gap — it's being treated as the deliverable. Push back: "When is the workshop? If there isn't one planned, this set will become the wall poster, which is exactly what (a) and (b) exist to prevent."

### Scenario E — User wants to apply principles to a specific design decision

The "this screen breaks principle 3 because…" exercise.

1. Read the canonical 15 (or the team's adapted set if they have one).
2. Look at the design decision (screen, component, flow).
3. Walk principles top-down. For each, pass / fail / N/A + 1 sentence why.
4. If multiple principles conflict, name the conflict and apply the priority order. If no priority is set, surface that gap to the user — "you have no rank order; this is the conflict; what's the call?"
5. Produce a punch list of changes the principles imply.

## Principle template (when writing or refining a single principle)

```markdown
## <Number>. <Title — 3-6 words, opinionated>

<Statement — 1-2 sentences, plain language, no marketing verbs.>

**Violation example.** [Concrete moment when this is broken — a specific screen, decision, or pattern.]

**Trade-off partner.** [What this principle loses to, and which wins when they collide.]

**How to test it.** [How does a designer or reviewer check whether a design follows this? Pointable evidence.]
```

## Common rationalisations

| Excuse | Reality |
|---|---|
| "We just need 5 quick ones for the wall" | Wall posters that the team didn't earn become decoration. Run the workshop. |
| "The team will revise them later" | They won't. The first draft anchors the conversation; if it's bad, the revision is harder than starting fresh. |
| "Generic principles are fine, every team needs 'be user-centered'" | "Be user-centered" doesn't resolve trade-offs. It's a wish. Specific principles tell you what to do when "user-centered" and "ship by Friday" collide. |
| "Manfred's 15 are too many, let's start fresh" | Start with the 15 and trim, don't start fresh. The 15 are the studio's accumulated answers — throwing them out costs more than adapting. |
| "Aspirational principles inspire the team" | Aspirational principles produce confident-sounding posters and ambiguous design reviews. Inspiration doesn't beat unambiguous direction. |
| "We'll figure out priority later" | Priority decided in the moment is priority decided by whoever spoke loudest. Decide priority *before* the conflict, not during. |
| "I'll skip the violation example, the principle is obvious" | If it's so obvious, the example takes 30 seconds to write. If you can't write it, the principle isn't testable. |
| "I'll just route every cold ask through Scenario D (starter set)" | Scenario D is the emergency stop-gap, not the default. If the user can't name a workshop date that revises the set, the "starter" framing is decoration — the set becomes the deliverable. Default is (a) or (b); (c) requires both an explicit user choice *and* a named workshop date. |

## Red flags — STOP

- About to produce 5+ principles without reading `~/.claude/shared/design-principles.md`
- Writing principles that include "transform", "empower", "leverage", "passionate" or any marketing verb
- Writing principles without a violation example
- Producing a "final" set in a single shot (no workshop, no team input, no trial week)
- Ignoring the user's actual context (regulatory, market, user segment) and writing generic UX principles
- Treating principles as a creative writing exercise vs. a decision-making framework

## Manfred lens

Strategy work touches **value risk** (Cagan) directly — principles are the team's stated answer to "what does the user actually need from us, and what trade-offs are we willing to make?". Bad principles let bad value bets slide through.

Cross-references:

- `manfred-discovery:product-brief` — Section 02 (Strategic Alignment) cites the principles set
- `manfred-discovery:opportunity-solution-tree` — opportunities filter through principles ("does pursuing this opportunity violate principle 6?")
- `manfred-design-research:user-archetype` — principles must be testable against real user behaviour, not assumed

## Output format

For Scenario A (cold ask): the (a)/(b)/(c) menu above.

For Scenarios B/C/D: the markdown kit / adapted set / starter set as described.

For Scenario E (apply to a design): a markdown punch list with principle # → pass/fail/N/A → 1-line evidence → recommended change.

Save outputs to `discovery/principles/<engagement-slug>-<YYYY-MM-DD>.md`.

## Tools used

- `Read` — `~/.claude/shared/design-principles.md`, `~/.claude/shared/manfred-brand.md`
- `Write` — produce the principles set or workshop kit
- `manfred-discovery:product-brief` — when principles feed the brief
- `manfred-design-research:user-archetype` — when applying principles requires user evidence
- `superpowers:writing-clearly-and-concisely` — for the voice pass on principle wording
