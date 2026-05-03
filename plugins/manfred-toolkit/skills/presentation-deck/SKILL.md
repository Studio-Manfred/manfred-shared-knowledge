---
name: presentation-deck
description: Use when structuring a design presentation for stakeholders, reviews, showcases, or talks — anyone says "presentation", "deck", "slides", "design review presentation", "stakeholder slides", "showcase deck", "talk", "conference talk", "pitch deck", "client presentation". Manfred-flavoured: hook → context → journey → solution → evidence → ask; one idea per slide; voice from `shared/manfred-brand.md`.
---

# presentation-deck

A presentation is a document the audience can't pause to re-read. Every slide has to land or it's lost. Done well, the deck moves the audience from where they are to where you need them. Done badly, it's a wall of bullet points that produces neither understanding nor decisions.

Manfred decks lead with the hook (why should the audience care?), structure around audience-need, and end with a specific ask. No "thank you" slide, no "any questions?" filler.

## Overview

Four common deck types — pick the right structure for the goal:

| Type | Goal | Universal arc |
|---|---|---|
| **Stakeholder update** | Inform + align | context recap → progress → key decisions → next steps → asks |
| **Design review** | Get feedback | objectives → walkthrough → rationale → open questions → feedback request |
| **Final showcase** | Gain approval | problem → process → solution → evidence → impact → next steps |
| **Portfolio / case study talk** | Demonstrate capability | challenge → approach → key decisions → outcome → learnings |

All four share a structure: **hook → context → journey → solution → evidence → ask**. The deck type determines weight per section.

## When to use

- Stakeholder update (project milestone, quarterly readout)
- Design review presentation (Gate 2 or 3 per `manfred-design-ops:design-review-process`)
- Final showcase to client / leadership (project sign-off)
- Conference talk (industry event, internal show-and-tell)
- Pitch (sales, fundraising, board)

**Skip when:**

- The audience is one person (use a doc — `manfred-toolkit:design-rationale` or `manfred-toolkit:case-study`)
- The content is a reference (use Notion / Storybook / a doc — decks aren't reference material)
- The decision can be made async (Linear thread + Figma comments + Loom — no need for a meeting + slides)

## Pre-flight

Ask, before drafting:

- **Audience?** Stakeholders, peers, executives, clients, mixed?
- **Goal?** Inform / align / approve / persuade / demonstrate?
- **Length?** Stakeholder updates: 10-15 min. Design reviews: 30-45 min. Showcases: 20-30 min. Conference talks: per CFP rules.
- **Format?** Live (in-person / video call) or self-presented (Loom / shared deck)?
- **What outcome do you need from the audience?** A decision? Feedback? Awareness? Sign-off? Be specific.
- **Voice doc loaded?** (`~/.claude/shared/manfred-brand.md` — the deck voice is the same as everything else)

If "outcome" is "they'll be impressed" — push back. Decks that aim for impression produce bullet-point posters. Decks that aim for a specific outcome produce decisions.

## The hard rules

| Rule | What it means |
|---|---|
| **One idea per slide** | If a slide has two ideas, split it. The audience can read or listen, not both — pick one mode per slide. |
| **Show, don't tell** | Visuals over text. A screen + 3 words beats 3 bullets. |
| **Lead with the hook** | First slide is "why should you care?" — not project name + author + date. Save the title slide; lead with stakes. |
| **Progressive disclosure** | Reveal complexity gradually. A complex diagram is built up across 3 slides, not crammed into 1. |
| **Design for the back of the room** | 24pt body minimum. Text high contrast against background. Don't ship slides only readable on a 15-inch laptop. |
| **End with the ask, not "Q&A"** | The final slide is "Here's what I need from you." Q&A happens regardless; the slide is the take-away. |
| **Speaker notes for context** | Slides are visual; notes are the spoken layer. Decks shared async should still work without you. |
| **Voice from `shared/manfred-brand.md`** | Direct, fragments OK, no marketing verbs, no corporate adjectives. Read aloud — would you cringe? |

## The universal arc

Six sections. Scale each to deck length.

### 1. Hook
Why should the audience care? Open with a problem, a number, a story — not a title slide.

**Bad opening**: "Settings page redesign — Q3 update — Lina Designer"

**Better opening**: A slide with one sentence: "Customers were calling support every Tuesday because they couldn't find last week's invoices."

### 2. Context
What does the audience need to know? Background, constraints, where the project sits.

Don't recap the company history. Recap only what's relevant to the decision the audience needs to make.

### 3. Journey
How did you get here? Process, key moments — not every step.

Pick 2-3 moments that mattered: research insight, pivot, breakthrough. Let the rest live in the case study.

### 4. Solution
What are you proposing? The design (with rationale).

Walk the design. Highlight 2-3 key features and why each addresses a specific user problem.

### 5. Evidence
Why is this right? Research, testing data.

Cite specifically. "We tested with 8 users; 6 completed the new flow without help" beats "users responded positively".

### 6. Ask
What do you need from them? Approval, feedback, resources, a decision.

Be specific. "Sign off on direction X by Friday so engineering can start Monday" — not "looking forward to your thoughts".

## Audience adaptation

Same structure, different emphasis per audience.

| Audience | Lead with | Emphasise | De-emphasise |
|---|---|---|---|
| **Executives** | Business impact | Business framing, decisions needed, asks | Process detail, technical implementation |
| **Engineers** | Technical context | Interaction specs, edge cases, dependencies | Brand polish, market positioning |
| **Designers** | Design challenge | Process, rationale, design system alignment | Business framing |
| **Clients** | Their user / business need | Outcomes, evidence, how this addresses their problem | Internal team process |
| **Mixed** | Lead with the user / problem | Layer detail progressively | Pick one focus; signal the rest is in appendix |

## Slide design principles

- **One idea per slide.** Two ideas = two slides.
- **Visual over text.** A screenshot + 3 words beats 5 bullet points.
- **Title that's a sentence.** "Customers stopped asking why verification took so long" beats "Verification UX".
- **Progressive disclosure.** Complex diagrams build up across 3 slides.
- **24pt body minimum** at the back of the room.
- **High contrast.** Don't trust your monitor — assume the projector is dim.
- **Speaker notes for everything.** The notes carry the spoken layer.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "I'll just put bullet points on each slide; people can read along" | Bullet-point slides + a presenter reading them is the worst of both. Pick: read or listen. |
| "I need a title slide with my name and date" | Save it for the last slide. The first slide is the hook. |
| "End with a 'Thank you' slide" | Last slide should be the ask. Thank you is for verbal close, not screen real estate. |
| "I'll cram more on each slide so there are fewer slides" | Slide count isn't the budget; audience attention is. More dense slides = less retention. |
| "Visuals are nice-to-have; I'll add them if there's time" | Visuals are the deck. Text-only slides are docs in disguise — send the doc. |
| "I'll just talk through it; the slides don't need to stand alone" | Decks shared async / archived / forwarded should work without you. Notes carry the spoken layer. |

## Red flags — STOP

- Title slide is the first slide (move to last; lead with hook)
- "Thank you" or "Q&A" as the last slide (replace with the ask)
- Slides with >5 bullet points (split into multiple slides)
- A slide trying to make 2+ points (split)
- 14pt body font (back of the room can't read it)
- No speaker notes (deck won't work async)
- Marketing verbs / corporate adjectives in slide text
- The closing slide has no specific ask

## Manfred lens

Presentations are **infrastructure** — Cagan/Torres lens doesn't apply directly. But they're a **brand surface** — a deck that violates Manfred's voice rules undermines every other Manfred surface that respects them.

Critical & ethical (principle 6): decks shouldn't manipulate. False urgency ("Only this week!"), shame-prompts ("Don't fall behind!"), dishonest data visualisation (truncated y-axes, cherry-picked time windows) — refuse. Decks that manipulate produce decisions that should have been refused.

## Cross-references

- `~/.claude/shared/manfred-brand.md` — voice rules
- `~/.claude/shared/DESIGN.md` — visual style for decks (typography, colours, spacing)
- `manfred-toolkit:case-study` — same content, different shape; case studies often source the deck
- `manfred-toolkit:design-rationale` — rationale slides reference these
- `manfred-design-ops:design-review-process` — Gate 2 / Gate 3 reviews use design-review decks
- `manfred-discovery:discovery-readout` — discovery readouts often use stakeholder-update deck shape

## Output format

Two artifacts:

1. **Deck outline** — markdown structure with 1-2 sentences per slide + speaker notes. Saved to `presentations/<engagement-slug>-<YYYY-MM-DD>-outline.md`.
2. **Slide-by-slide build** — actual deck (Figma slides, Keynote, Google Slides) — built from the outline.

The outline is the thinking; the build is the production. Get the outline right first; building from a wrong outline is wasted time.

## Tools used

- `Read` — `~/.claude/shared/manfred-brand.md`, project artefacts (case study, design files)
- `Write` — produce the deck outline
- `manfred-toolkit:case-study` — for content source
- `manfred-toolkit:design-rationale` — for the rationale slides
- `mcp__figma-console__*` — for slide production in Figma slides (when used)

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
