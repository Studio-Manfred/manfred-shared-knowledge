---
name: case-study
description: Use when writing a portfolio case study or client write-up — anyone says "case study", "write up this project", "portfolio piece", "client showcase", "project narrative", "tell the story of this design", "what should I write about this project". Manfred-flavoured: customer-driven framing, evidence over polish, honest about trade-offs, voice from `shared/manfred-brand.md`.
---

# case-study

A case study tells the story of a design project so someone unfamiliar can understand: what problem, what was tried, what shipped, what it changed. Done well, it's evidence of how you think; done badly, it's a polished poster nobody trusts.

Manfred case studies lead with the user problem, name the trade-offs honestly, and quote real customers when possible. Process is shown but not over-documented. Voice is direct and concrete.

## Overview

Six sections. Scale to the audience: a portfolio case study is 800-1200 words; a client showcase is 400-600 words. Each section earns its space.

1. **Overview** — title + one-line summary + role + outcome (the hook)
2. **Challenge** — business context + user problem + why it mattered
3. **Process** — research + key decisions + iteration (show breadth, not every step)
4. **Solution** — final design + how it addresses the challenge
5. **Impact** — quant + qual results + what'd be different next time
6. **Reflection** — key learnings + skills developed + influence on future work

## When to use

- Portfolio case study (Manfred site, personal portfolio, job application)
- Client showcase (case study for `studiomanfred.com` post-engagement)
- Internal write-up for the team's reference
- Conference / publication submission requiring a case study format
- LinkedIn long-form post (different shape — see `manfred-toolkit:linkedin-*` for short-form)

**Skip when:**

- The user wants a presentation (use `manfred-toolkit:presentation-deck`)
- The user wants a design rationale doc (use `manfred-toolkit:design-rationale`)
- The work isn't done yet (case studies are post-engagement; mid-project showcases are different — usually a presentation)
- The user wants a process doc (different audience — internal-team-facing, not story-shaped)

## Pre-flight

Ask, before drafting:

- **Audience?** Portfolio (designers / hiring managers), client showcase (other clients / prospects), conference (peers), LinkedIn (mixed).
- **Length?** Portfolio: 800-1200 words. Client showcase: 400-600 words. Conference: per submission rules.
- **What outcome can I lead with?** The hook — quant if possible ("Reduced KYC abandonment from 38% to 14%"), qual if not ("Customers stopped asking why the verification took so long").
- **What evidence is available?** Research sessions, analytics, customer verbatims, before/after artefacts. Cases without evidence read like advertising.
- **Voice doc loaded?** (`~/.claude/shared/manfred-brand.md` — the case study voice is the same as everything else Manfred ships.)

If outcome is "we shipped on time" — push back. That's not an outcome, that's a deadline. Ask for the user-facing change.

## The hard rules

| Rule | What it means |
|---|---|
| **Lead with the user problem** | Not the company history, not the stack, not the team's "passion for great design". The user problem is the hook. |
| **Quantify where possible** | "Reduced abandonment 38% → 14%" beats "improved completion". If you can't quantify, qualify with a customer quote. |
| **Honest about trade-offs** | "We chose X. We gave up Y." Cases that present every decision as obvious are propaganda. |
| **Process shown, not over-documented** | Show 2-3 key moments (research insight, pivot, breakthrough). Don't recap every Figma version. |
| **Real screenshots, not just mockups** | Mockups read as marketing. Real product screens read as evidence. Mix where possible. |
| **Voice from `shared/manfred-brand.md`** | Direct, fragment-friendly, no marketing verbs, no corporate adjectives. Read aloud — would you cringe? Rewrite. |
| **First person for your contributions** | "I led research" not "research was led by". Be specific about your role vs the team's. |
| **Edit ruthlessly** | First draft is too long. Cut 30%. Cases get scanned, not read. |

## Case study structure

```markdown
# <Project name>

> <One-line summary that sets the stakes. Avoid jargon.>

**Role:** <your specific contribution>
**Team:** <the others involved — designers, PM, engineers, research>
**Timeline:** <e.g. "8 weeks, Q3 2025">
**Outcome:** <the hook — quant where possible, qual where not>

---

## The challenge

[2-3 paragraphs. The business context. The user problem. Why it mattered now.]

[Concrete: who was struggling, with what, in what moment. "Customers in the EU couldn't open accounts in under 24 hours because…" beats "onboarding was inefficient".]

## The process

[3-5 paragraphs. Show breadth (we explored multiple directions) and depth (we went deep on these specific decisions). Pick 2-3 moments to highlight:]

- **Research insight** — what we learned that changed our approach
- **Key pivot** — where we changed direction and why
- **Breakthrough** — the moment something clicked

[Don't recap every Figma version. Don't list every meeting. Choose what serves the story.]

## The solution

[2-3 paragraphs + screenshots. Walk through the final design. Highlight 2-3 key features and why each addresses a specific user problem.]

[Reference the design system if applicable (`~/.claude/shared/DESIGN.md`). Note what's reused vs custom.]

[Trade-offs: what we chose to do, what we explicitly chose not to do.]

## The impact

[1-2 paragraphs.]

**Quantitative**
- [Specific metric movement, with baseline + outcome + time-frame]
- [Specific metric movement]

**Qualitative**
- [Customer quote — anonymised if needed]
- [Team / stakeholder reaction]

**What we'd do differently**
- [1-2 honest reflections — what we'd revisit if we did this again]

## Reflection

[1 paragraph.]

[What this taught me / us. How it influences future work. What I'm still figuring out.]
```

## Writing the hook

The opening 2 sentences make or break the case study. They have to make the reader want to know more.

**Bad hook**: "We worked with [Client] to redesign their dashboard. The result was a more modern, user-friendly interface."

**Better hook**: "Customers were calling support every Tuesday because they couldn't figure out where last week's invoices had gone. Eight weeks later, support tickets dropped 73% — without anyone touching the support team."

The good hook tells you the user problem, the change, and the angle (we didn't fix support, we fixed the design that *caused* the support load).

## Visual storytelling

Cases live or die on their visuals:

- **Show the journey**, not just the final product. Sketches, wireframes, iterations.
- **Before / after** comparisons where possible. Side-by-side.
- **Annotated screenshots** for key design decisions. Highlight the choices that took time to land.
- **Real product**, not just mockups. Mix in real screenshots / Loom recordings of the live thing where you can.
- **Process artefacts**: research findings, OST snapshot, journey map, affinity diagram clusters — these *are* the case for the design.

## Voice

Manfred case studies sound like Manfred — warm + precise, fragments allowed, no marketing verbs. The trap with case studies is they want to slide into "we transformed the customer experience by leveraging design thinking…" — every word of that is anti-Manfred.

**Anti-pattern (generic-agency case study)**:
> "We partnered with [Client] to transform their digital experience. Through a holistic design process leveraging user research and rapid prototyping, we delivered a best-in-class solution that empowers customers to seamlessly manage their accounts."

**Manfred version**:
> "Customers couldn't find last week's invoices. Six weeks of research, three rounds of testing, one rebuilt dashboard later — they could. Support tickets dropped 73%."

The first sentence does in 8 words what the agency version does in 40. And the Manfred version *means something*.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "I'll use a generic template; it's faster" | Generic templates produce generic case studies. The structure isn't the work — the specificity is. |
| "I'll write it after the client signs off; the polish phase" | Cases written 6 months later lose the specificity. Write the rough version during the engagement; polish after sign-off. |
| "We didn't test, so I'll just describe the design" | A case study without evidence reads as advertising. If there's no testing data, surface it honestly: "Launched recently; results pending; here's what we expect to see." |
| "I'll skip the trade-offs section — looks negative" | Trade-offs are what make the case credible. Skipping them produces propaganda. |
| "I'll add a 'wow' adjective so it lands" | "World-class", "best-in-class", "innovative" make the case unbelievable, not impressive. Specific outcomes do the work. |
| "Process should show every iteration" | Process should show the 2-3 moments that mattered. Every iteration is a slog to read. |

## Red flags — STOP

- About to use a marketing verb (transform, empower, leverage, unlock, supercharge, drive, deliver value)
- About to use a corporate adjective (cutting-edge, world-class, innovative, best-in-class, passionate)
- Hook is generic ("We worked with X to improve Y")
- Outcome is a deadline ("Shipped on time"), not a user-facing change
- Process recaps every Figma version
- No trade-offs named
- No evidence cited (research, analytics, customer quote)
- No specific numbers when numbers exist

## Manfred lens

Case studies are a **brand surface** — they show how Manfred thinks. A case study that violates the voice rules undermines every other Manfred surface that respects them. The case is also a **value claim** — it asserts that Manfred made something better. That assertion needs evidence (Cagan's value risk, retroactively).

Critical & ethical (principle 6): the case study includes "what does this design do in the world?" implicitly via the impact section. If the impact is "we increased engagement by 12%" but the engagement was at the user's expense (manipulative copy, dark-pattern flows, attention-extraction), name it. Honest case studies surface the trade-off; dishonest ones bury it.

## Cross-references

- `~/.claude/shared/manfred-brand.md` — voice rules
- `manfred-toolkit:design-rationale` — for the deeper "why this decision" doc that case studies reference
- `manfred-toolkit:presentation-deck` — for the talk version of the same content
- `manfred-toolkit:linkedin-show-and-tell` — for the LinkedIn-shaped version (Swedish, post-shaped)
- `manfred-design-research:summarize-interview` — for the customer-quote source
- `manfred-discovery:discovery-readout` — for the discovery-cycle write-up that often becomes case-study material

## Tools used

- `Read` — `~/.claude/shared/manfred-brand.md`, project artefacts (Figma, research, analytics)
- `Write` — case study markdown
- `manfred-toolkit:design-rationale` — for decisions referenced in the case
- `manfred-design-research:summarize-interview` — for customer quotes

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
