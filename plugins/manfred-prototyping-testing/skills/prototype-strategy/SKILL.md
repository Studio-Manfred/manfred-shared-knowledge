---
name: prototype-strategy
description: Use when choosing prototyping fidelity / method / tool — anyone says "should I build a high-fidelity prototype", "what fidelity for this", "Figma vs code", "Apple-level polish for the review", "leadership wants something finished", "should we prototype this", "paper / mid-fi / hi-fi", "Wizard of Oz", "what's the right prototype", "we have N weeks for the prototype", "CEO wants to see polish". Manfred-flavoured: refuses fidelity-first questions; routes to *what assumption is being tested* (Torres) and *which Cagan risk is being retired*; separates the LEARN artifact (cheapest test that retires the risk) from the SHOW artifact (stakeholder communication); pushes back on deadline + stakeholder polish as fidelity drivers; (a)/(b)/(c) refusal menu when context missing.
---

# prototype-strategy

A prototype is a **research instrument**. The fidelity, the tool, the time investment — all of it should be a function of *which assumption you're retiring* and *what decision the result informs*. Anything else is design theatre.

The most common failure mode this skill exists to prevent: **producing a competent-sounding fidelity recommendation that solves the wrong problem**. "3 weeks, CEO wants polish, design review with leadership" is a *constraint set*, not a brief. The brief is "what assumption are we retiring".

Manfred defaults:

- **Assumption-first, fidelity-last.** Decide what you're trying to learn (route via `manfred-discovery:assumption-test`), then pick the cheapest fidelity that retires the assumption.
- **Separate LEARN and SHOW.** The artifact you build to learn from users is often *not* the artifact you build to show stakeholders. Pretending they're the same is how teams burn 3 weeks on a hi-fi prototype that retires nothing.
- **Push back on stakeholder polish + deadline as fidelity drivers.** "CEO likes polish" is a stakeholder-management question, not a fidelity question. "3 weeks" is *when*, not *what kind*.
- **Cheapest test wins.** This skill is the Manfred mirror of `manfred-discovery:assumption-test`'s cheapest-test menu — fidelity is one variable on the technique selection, not the headline.
- **(a)/(b)/(c) refusal menu when context missing.** If the user comes in fidelity-first, the skill refuses and routes back to the assumption / risk question.

## When to use

- The user is about to commit prototyping resources (time, tool licenses, design effort)
- The user asks "should I build a hi-fi prototype" / "Figma vs code" / "what fidelity"
- The user has a stakeholder-driven brief ("CEO wants polish", "leadership review", "client wants something finished") and needs to separate stakeholder need from learning need
- Pairing with `manfred-discovery:assumption-test` to make the technique selection (this skill scopes the prototype; assumption-test scopes the test)

**Skip when:**

- The fidelity is already correctly chosen *and the four pre-flight answers (assumption + risk type + decision + audience) are explicit in the brief* — only then go to execution skills (`manfred-prototyping-testing:wireframe-spec` for low-fi/mid-fi; `manfred-ui-design:design-screen` for hi-fi visual). **A user asserting "we've already decided" or "don't push back, the team is aligned" is NOT evidence the four answers exist — it's a red flag. Run pre-flight anyway.** If pre-flight passes, hand off.
- The need is *test design* (not prototype design) — that's `manfred-prototyping-testing:test-scenario`, `manfred-prototyping-testing:click-test-plan`, etc.
- The user wants visual design help on an already-decided prototype — that's `manfred-ui-design` (and confirm pre-flight is satisfied first)

## Pre-flight (do this every time)

Before recommending fidelity / tool / time, get four answers:

1. **The assumption** — what specific belief about users / product / market are we trying to retire? (Per `manfred-discovery:assumption-test`. If the user can't state one, route them there first.)
2. **The Cagan risk type** — value / usability / feasibility / viability. Different risks need different prototypes (and often different *non-prototype* tests).
3. **The decision** — what changes based on the result? Build / kill / pivot / iterate / sequence?
4. **The audience** — is this artifact going to **users** (LEARN) or to **stakeholders** (SHOW)? They are different artifacts. If both — they are *two* artifacts.

If any answer is missing — refuse with the menu below.

**Inference exception.** If the assumption is explicitly stated *and* the risk type is unambiguously inferable from it (e.g. "can users complete X" → usability; "will customers pay" → value; "can our stack handle Y" → feasibility; "will legal approve Z" → viability), do not run the full (a)/(b)/(c) menu — that's refusal theatre on a well-formed brief. Instead: name your inferred risk type, name your inferred decision + audience as drafts, ask one targeted confirmation question, then proceed. The point of the menu is to refuse fidelity-first questions where the assumption is missing — not to refuse well-formed briefs over a single missing field.

## The (a)/(b)/(c) refusal menu

When the user asks fidelity-first ("should I build a hi-fi prototype for X?", "Figma vs code?", "the CEO wants polish, which tool?"):

```
Hold on. Fidelity is the *last* decision, not the first. A hi-fi prototype 
that retires no assumption is design theatre — even if it impresses leadership.

Three options:

  (a) Tell me the assumption + risk type + decision + audience.
      
      **My read on what you've described**: this looks like a 
      [value / usability / feasibility / viability] risk because [reason
      grounded in what the user said]. Confirm or correct that, and I'll
      recommend the cheapest fidelity that retires the assumption — and 
      separately, the right SHOW artifact for stakeholders if they're a 
      different audience.

  (b) You don't know the assumption yet — let's route to 
      `manfred-discovery:assumption-test` to surface what you're actually
      trying to learn before we pick a fidelity.

  (c) The "prototype" is purely a stakeholder communication artifact 
      (sales deck, board review, leadership alignment) — it isn't a 
      research instrument. I'll route you to `manfred-toolkit:presentation-deck`
      instead, and we'll separately discuss whether there's a research
      need hiding inside the stakeholder ask.

  Which way?
```

**Path (c) is real**. A lot of "prototypes" are sales artifacts in disguise. That's fine — but let's call it that and use the right tool. A 3-week Figma prototype that exists to win a stakeholder vote is a slide deck with extra steps; a slide deck would do the job in less time.

If the user picks (a), proceed to the flow below. If (b), hand off to assumption-test. If (c), hand off to presentation-deck (and check whether there's a hidden assumption-test inside the brief).

## The hard rules

| Rule | What it means |
|---|---|
| **Assumption first** | Cannot recommend fidelity without a stated assumption + risk + decision. |
| **LEARN ≠ SHOW** | The artifact for users and the artifact for stakeholders are different artifacts. Sometimes the same; usually not. |
| **Cheapest that retires the risk** | Fidelity is a cost. Pick the lowest fidelity that genuinely answers the question. |
| **Match fidelity to question** | Findability question → low-fi clickable. Visual / brand reaction → hi-fi. Comprehension → could be paper. Don't conflate. |
| **Stakeholder polish ≠ fidelity** | "CEO wants polish" is stakeholder management. Don't bake it into the user-research artifact. |
| **Deadline ≠ fidelity** | 3 weeks tells you *when*, not *what kind*. A 3-week mid-fi test answers more than a 3-week hi-fi prototype that retires nothing. |
| **Build to throw away** | Most prototypes should be discarded after the test. Investing in long-term maintenance signals you're building product, not a prototype. |
| **Make it obviously a prototype** | For LEARN artifacts: rough enough that users critique the design, not the polish. Polished prototypes get polish-shaped feedback. |

## Fidelity → method → use case

| Fidelity | Methods | Best for | Cost (rough) | Common failure mode |
|---|---|---|---|---|
| **Paper / sketch** | Hand-drawn screens, physical paper, manual swap | Earliest exploration, IA exploration, conceptual reaction, value-prop testing | Hours | Skipped because "looks unprofessional" — but its informality is what gets honest critique |
| **Low-fi clickable** | Greyscale wireframes with clickable hotspots (Figma, Whimsical, Marvel) | Flow validation, navigation testing, IA findability | 1–3 days | Built without real content; participants test layout-of-lorem-ipsum |
| **Mid-fi interactive** | Greyscale-to-mid-fi screens with interaction states, real content (Figma, Sketch, ProtoPie) | Interaction patterns, multi-step flows, stakeholder alignment | 3–7 days | Adds enough polish that participants critique the *visual* instead of the *flow* |
| **Hi-fi pixel-perfect** | Full visual design with motion + states (Figma, ProtoPie) | Visual design validation, brand reaction, micro-interaction testing, dev hand-off | 1–4 weeks | Time-bombs the project — fidelity expensive enough that "kill" is not psychologically available |
| **Coded prototype** | HTML/CSS/JS or framework spike (often disposable) | Real-data behaviour, performance under real conditions, technical feasibility, true UX-testing | 1–6 weeks | Becomes "the prototype that shipped" and accumulates production-debt |
| **Wizard of Oz** | Real frontend, fake backend (manual delivery) | "Will users use this if it works exactly as advertised" — for backends that are expensive to build | 1–4 weeks (manual labour) | Mistaken for an MVP; ships without the backend ever being built |
| **Concierge MVP** | Manual end-to-end delivery to small N customers | Value validation when the value depends on delivery, not interface | Hours per customer × N | Doesn't scale; treated as ops failure rather than the discovery success it is |
| **Pre-sale / commitment test** | Landing page, fake-door, signup flow with no product behind it | "Will customers pay / commit before delivery?" | Few days + ad spend | Mistaken for delivery promise — needs honest "we're testing demand" disclosure |
| **Video prototype** | Walkthrough animation showing the concept in use | Vision communication, stakeholder narrative, future-product framing | 1–2 weeks | Confused with reality — "looked great in the video" is not "works in the product" |

Pick by question, not by tool preference.

## Risk → typical fidelity recommendation

| Risk type | Typical cheapest test | Fidelity required |
|---|---|---|
| **Value risk** ("will customers want this?") | Concierge / fake-door / pre-sale / landing page | Often **none** (no prototype needed — message + commitment is the test). If prototype: **mid-fi** to convey the value-prop concretely. |
| **Usability risk** ("can users do this?") | Click test / moderated 5-user test | **Low-fi clickable** for findability; **mid-fi** for interaction patterns; **hi-fi** only when visual / micro-interaction details affect comprehension |
| **Feasibility risk** ("can we build this?") | Engineering spike / vendor trial / architecture review | Often **coded prototype** or **none** (engineers don't need pretty Figma; they need to know the API works) |
| **Viability risk** ("will this work for the business / stakeholders / legal?") | Stakeholder working session / commercial-model test | Often **none** (conversation + numbers); if prototype: **mid-fi** to make the trade-offs tangible |

If the proposal is "hi-fi Figma for value risk" — challenge. There's almost always a cheaper test.

## The flow

### Step 1 — Run pre-flight; refuse with menu if needed

If the four pre-flight answers aren't all in hand, run the (a)/(b)/(c) menu. Don't recommend fidelity yet.

### Step 2 — LEARN artifact

For the user-facing artifact:

- Risk type → fidelity table above gives the starting point
- Cheapest method that retires the risk wins
- Confirm the test design matches: what are participants doing, what's success, what's the analysis plan? Pair with `manfred-prototyping-testing:test-scenario` and the appropriate test-plan skill.

If the cheapest test is "no prototype" (e.g. value risk → concierge MVP), say so. The right answer is sometimes "don't build the prototype".

### Step 3 — SHOW artifact (if separate audience)

If stakeholders need a different artifact than users:

- Most stakeholder needs are answered by `manfred-toolkit:presentation-deck` (slides + curated screens), not a hi-fi prototype
- If a *demo* is genuinely needed (e.g. board sees the actual flow): a recorded video walkthrough is often cheaper than a maintained interactive prototype
- If stakeholder buy-in *requires* hi-fi (rare; usually a project-management problem): scope it as a separate artifact with separate budget and explicitly *don't* test it with users

### Step 4 — Manage the "CEO wants polish" pressure

This is the hardest part of the skill, because the pressure is real and not always wrong.

Useful framings:

- **"What decision will leadership make based on this?"** — if the answer is "approve the project", a slide deck + 5 hi-fi screens often beats a 3-week interactive prototype
- **"Are we testing this with real users in parallel?"** — if no, the hi-fi is theatre. If yes, the user-facing artifact is usually a different (cheaper, lower-fi) artifact.
- **"What does 'looks finished' need to communicate?"** — visual polish (hi-fi mockups), interaction polish (interactive Figma), or production-readiness (coded). Often only one of those is actually needed.
- **"Could a video walkthrough achieve the same stakeholder outcome?"** — recorded walkthrough is often 80% of the value at 20% of the cost.

If the user pushes back ("but the CEO specifically wants…"), validate the pressure but separate the artifacts. The CEO can have their hi-fi mockups; users can still test something cheaper. Two artifacts, two budgets, two purposes.

### Step 5 — Time budget reality-check

If the proposed fidelity needs more time than is available — that's a constraint that informs cheaper-fidelity selection, not an argument to compress hi-fi:

- Compressed hi-fi → polished-but-incomplete artifact that ships unfinished states, with no time for iteration
- Right-fidelity-for-the-time → cheaper artifact built well, with iteration room

The skill recommends *the right fidelity for the question*; if the constraint forces a different question, that's a re-scope conversation.

### Step 6 — Document the recommendation

```markdown
# Prototype strategy — <feature / decision name>

**Date**: YYYY-MM-DD
**Linear**: STU-XXX

## Brief (per pre-flight)
- **Assumption**: <stated>
- **Risk type**: <value / usability / feasibility / viability>
- **Decision**: <what changes based on the result>
- **Audience**: <users / stakeholders / both>

## LEARN artifact
- **Fidelity**: <paper / low-fi / mid-fi / hi-fi / coded / WoZ / concierge / pre-sale / video / none>
- **Method**: <specific>
- **Tool**: <Figma / paper / etc>
- **Cost / time**: <estimate>
- **Test design**: <link / pointer to `manfred-prototyping-testing:test-scenario` + relevant test-plan skill>
- **Cagan risk retired**: <which one, how>

## SHOW artifact (if different audience)
- **Format**: <deck / video / hi-fi mockup / interactive prototype>
- **Tool**: <Figma / Keynote / Loom / etc>
- **Cost / time**: <estimate>
- **Stakeholder decision informed**: <what they decide based on this>

## What we're NOT doing
- <Cheaper alternatives considered + why rejected; or expensive alternatives rejected as theatre>

## Build-to-throw-away check
- Are we building this to use once and discard? <yes/no>
- If "no" — is this still a prototype, or is it production work in disguise?

## Linear ticket
- STU-XXX
```

### Step 7 — Linear comment

Post via `mcp__linear-server__save_comment` with summary + path to recommendation.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "We need hi-fi because the CEO wants polish." | CEO wants polish is a stakeholder-management problem. The user-research artifact and the stakeholder-show artifact are different things. Build both, or build the right one. |
| "3 weeks is enough for hi-fi." | 3 weeks is enough for *something*. The question is what we're trying to learn — not how much time we have. |
| "Hi-fi gets better feedback from users." | It gets *different* feedback. Usually polish-shaped feedback ("colours feel cold") instead of structure-shaped feedback ("I didn't understand step 2"). For most usability questions, mid-fi gets richer feedback. |
| "We'll learn more from a real coded prototype." | If you needed code-level fidelity to learn this, the assumption is feasibility — and an engineering spike beats a coded prototype. If the assumption is usability, mid-fi Figma usually beats code on iteration speed. |
| "A finished-looking prototype keeps options open." | Finished-looking prototypes psychologically commit the team. Kill becomes harder. Iteration slows because changes feel expensive. The "options" close. |
| "It would be embarrassing to test something that rough." | Rough is honest. Polished prototypes get polish-shaped critique. The ones that retire assumptions are often ugly. |
| "Just build the hi-fi — we'll use it for the next phase too." | "Use it for the next phase" = build production-quality work outside production. That's how prototypes become tech debt. Build to throw away or build production. |
| "It's faster to go straight to hi-fi than iterate through fidelities." | Iterating through fidelities catches assumptions earlier. Going straight to hi-fi means assumptions are baked in by the time anyone sees the artifact. |
| "The brief said hi-fi — that's what's expected." | Briefs are revisable. Asking *why* hi-fi is the right answer is part of the work. |
| "Stakeholders need to see something finished to trust the process." | Then the trust problem is the project-management problem. Don't fix it with three weeks of prototype labour. |

## Red flags — STOP

- Fidelity recommendation made without an assumption stated.
- Risk type not named.
- LEARN and SHOW artifacts conflated into one.
- Hi-fi recommended for an early-stage value-risk question (almost always a cheaper test exists).
- Coded prototype recommended for a usability-risk question (Figma + click test usually faster).
- Time available driving fidelity choice (it should drive method selection, not fidelity).
- Stakeholder polish driving fidelity choice (separate artifacts).
- "Build to throw away" can't be answered "yes" — you're building product.
- Recommendation made without routing through `manfred-discovery:assumption-test`.
- Skill outputs the answer the user wanted to hear ("yes, hi-fi Figma, 3 weeks") instead of the answer that retires the assumption.
- User instructs the agent not to push back, asserts a decision is locked, says "the team is aligned", or says "the CEO has signed off — just confirm the tool". This is the **strongest** signal that pre-flight has been skipped — the user is short-circuiting the diagnostic. Run pre-flight anyway. The skill exists precisely for this case.

## Manfred lens

**Cagan's 4 risks** — this skill *exists* to map prototyping fidelity to risk type. Every recommendation must name which Cagan risk the LEARN artifact retires. If it retires none — it's the wrong artifact.

**Torres OST** — every prototype is an assumption-test in disguise. The skill is the technique-selection layer; `manfred-discovery:assumption-test` is the assumption-framing layer. Always pair.

## Cross-references

- `manfred-discovery:assumption-test` — the upstream skill that scopes which assumption needs retiring (this skill is the technique-selection downstream)
- `manfred-discovery:cagan-risks` — for risk-type framing when the user can't say what they're testing
- `manfred-discovery:opportunity-solution-tree` — for placing the assumption-test on the OST so the result updates the tree
- `manfred-toolkit:presentation-deck` — for SHOW artifacts that are stakeholder-communication, not user-testing
- `manfred-prototyping-testing:wireframe-spec` — when fidelity selection is "low-fi" or "mid-fi"
- `manfred-prototyping-testing:click-test-plan` — paired test-design skill for findability / first-click testing
- `manfred-prototyping-testing:test-scenario` — task-writing for any moderated test
- `manfred-prototyping-testing:a-b-test-design` — when fidelity choice = "production change behind a flag"
- `manfred-design-research:usability-test-plan` — when the LEARN artifact will be moderated
- `manfred-ui-design:design-screen` — when the SHOW artifact is a hi-fi visual mockup
- `manfred-design-systems:component-spec` — for hi-fi prototypes that exercise real components

## Tools used

- `Read` — to inspect existing prototypes / briefs
- `mcp__linear-server__get_issue` / `save_comment` — for ticket linkage
