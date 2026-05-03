---
description: Build a design presentation end-to-end — scope + audience + structure + outline + voice pass + production-ready deck.
argument-hint: [audience + topic, e.g. "client showcase deck for the Settings page redesign, 30 min talk"]
---

You're building a presentation. The user mentioned: $ARGUMENTS

## Step 1 — Confirm scope + audience

Ask:

- **Audience?** Stakeholders, peers, executives, clients, mixed?
- **Goal?** Inform / align / approve / persuade / demonstrate? Be specific — "they should sign off on direction X by Friday" beats "they should be impressed".
- **Length?** Stakeholder updates: 10-15 min. Design reviews: 30-45 min. Showcases: 20-30 min. Conference talks: per CFP.
- **Format?** Live or self-presented (Loom)?
- **Deck type?** Stakeholder update, design review, final showcase, or portfolio talk?

If "outcome" is "they'll be impressed" — push back. Decks aiming for impression produce bullet-point posters; decks aiming for a specific outcome produce decisions.

## Step 2 — Outline the deck (`manfred-toolkit:presentation-deck`)

Run the `presentation-deck` skill to produce the outline:

- Hook (slide 1 — why should the audience care?)
- Context (background, constraints — what they need to know)
- Journey (process — 2-3 moments, not every step)
- Solution (the design with rationale)
- Evidence (research, testing, data — cite specifically)
- Ask (the specific outcome you need from them)

Save outline to `presentations/<engagement-slug>-<YYYY-MM-DD>-outline.md`.

## Step 3 — Source content from existing artifacts

The deck pulls from:

- `manfred-toolkit:case-study` — if this engagement has one, it's most of the content
- `manfred-toolkit:design-rationale` — for the rationale slides
- `manfred-design-research:summarize-interview` — for customer quotes
- `manfred-discovery:discovery-readout` — for stakeholder-update decks
- `manfred-ux-strategy:metrics-definition` — for the evidence section

Don't re-write content that exists elsewhere. Reference and condense.

## Step 4 — Voice pass

Read every slide title + body aloud. Apply `~/.claude/shared/manfred-brand.md` rules:

- No marketing verbs (transform, empower, leverage, unlock, supercharge, drive, deliver value)
- No corporate adjectives (cutting-edge, world-class, innovative, best-in-class, passionate)
- No "Thank you" or "Q&A" as final slide — replace with the ask
- No title slide as first slide — replace with the hook

Rewrite anything that fails.

## Step 5 — Visual production

If using Figma slides, FigJam, Keynote, Google Slides, or similar:

- One idea per slide
- Visuals over text
- 24pt body minimum
- High contrast
- Speaker notes for every slide (notes carry the spoken layer; deck shared async should still work)
- Reference `~/.claude/shared/DESIGN.md` for typography + color tokens

If Figma is the tool, optionally use `mcp__figma-console__*` for slide creation.

## Step 6 — Rehearse + adjust

Before the live presentation:

- Time the rehearsal — over time-box = cut, not "talk faster"
- Read every slide aloud — anything that makes you cringe gets rewritten
- Identify the 1-2 slides most likely to draw questions; prepare backup slides
- Confirm the ask slide is the close

## Step 7 — Linear update

If a Linear ticket / project is in scope, post a comment via `mcp__linear-server__save_comment` with:

- Path to deck outline + final deck
- Audience + format + duration
- The ask (what you need from the audience)
- Date of presentation

## Wrap-up

Confirm the deck covers:

- [ ] Hook (slide 1) — not title slide
- [ ] Context calibrated to audience
- [ ] Journey shows 2-3 key moments, not every step
- [ ] Solution walks the design with rationale
- [ ] Evidence cited specifically (research, data, customer quotes)
- [ ] Ask (final slide) — specific outcome needed
- [ ] One idea per slide
- [ ] Visuals over text
- [ ] Speaker notes for every slide
- [ ] No marketing verbs / corporate adjectives
- [ ] Voice passes the read-aloud test

Then offer:

> "Run the rehearsal, time-box, cut what runs over. After the presentation, capture decisions in `manfred-toolkit:design-rationale` if direction was set, or `manfred-discovery:discovery-readout` if it was a discovery summary."
