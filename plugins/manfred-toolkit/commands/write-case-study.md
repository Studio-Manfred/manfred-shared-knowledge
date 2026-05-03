---
description: Write a portfolio-ready case study end-to-end — outcome hook + structured narrative + evidence + voice pass.
argument-hint: [project + audience, e.g. "case study for the Settings page redesign for the Manfred portfolio site"]
---

You're writing a case study. The user mentioned: $ARGUMENTS

## Step 1 — Confirm scope + audience

Ask:

- **Audience?** Portfolio (designers / hiring managers), client showcase (prospects), conference (peers), LinkedIn (mixed)?
- **Length?** Portfolio: 800-1200 words. Client showcase: 400-600 words. Conference: per CFP.
- **Outcome to lead with?** The hook — quant where possible ("Reduced KYC abandonment from 38% to 14%"), qual where not.
- **Evidence available?** Research sessions, analytics, customer verbatims, before/after artefacts. Cases without evidence read as advertising.
- **Linear ticket / project for posting?**

If outcome is "we shipped on time" — push back. That's a deadline, not an outcome. Ask for the user-facing change.

## Step 2 — Run the case-study skill (`manfred-toolkit:case-study`)

Run the `case-study` skill to produce the structured narrative:

- Overview (title + summary + role + outcome — the hook)
- Challenge (business context + user problem + why it mattered)
- Process (research + key decisions + iteration — show breadth, not every step)
- Solution (final design + how it addresses the challenge)
- Impact (quant + qual + what'd be different next time)
- Reflection (key learnings + skills + influence on future work)

Save to `case-studies/<engagement-slug>-<YYYY-MM-DD>.md`.

## Step 3 — Source content from existing artifacts

Pull from:

- `manfred-toolkit:design-rationale` — for the "key decisions" section
- `manfred-design-research:summarize-interview` — for the customer-quote sources
- `manfred-design-research:affinity-diagram` — for research findings
- `manfred-discovery:discovery-readout` — for the discovery-cycle summary
- `manfred-ux-strategy:metrics-definition` — for the impact metrics

If artifacts don't exist for a section, name the gap honestly — don't invent. Cases with invented evidence get spotted.

## Step 4 — Visual storytelling

Cases live or die on their visuals:

- Real product screenshots (mix in with mockups; mockups read as marketing)
- Before / after comparisons (side-by-side)
- Annotated screenshots for key decisions
- Process artefacts (research findings, OST snapshot, journey map clusters)
- Sketches / wireframes / iterations — show the journey

Plan visuals before writing — what visual lands each section?

## Step 5 — Voice pass

Read every paragraph aloud. Apply `~/.claude/shared/manfred-brand.md` rules:

- No marketing verbs (transform, empower, leverage, unlock, supercharge)
- No corporate adjectives (cutting-edge, world-class, innovative, best-in-class, passionate)
- First person for your contributions ("I led research" not "research was led")
- Specific over generic ("Reduced KYC abandonment 38% → 14%" not "improved completion")
- Trade-offs honest (cases without trade-offs are propaganda)

Edit ruthlessly. First draft is too long. Cut 30%.

## Step 6 — Cross-link

If this case study has a:

- Long-form companion → link to the design rationale doc
- Shorter LinkedIn version → cross-link to `manfred-toolkit:linkedin-show-and-tell` post
- Conference talk → link to deck (`manfred-toolkit:presentation-deck` outline)

These versions reuse content; cross-linking helps readers find the right format.

## Step 7 — Linear update

If a Linear ticket is in scope, post a comment via `mcp__linear-server__save_comment` with:

- Case study URL / path
- Top 3 outcomes the case captures
- Where it's been published / will be published

## Wrap-up

Confirm the case study covers:

- [ ] Hook (first 2 sentences) — user problem + change
- [ ] Outcome quantified (with baseline + result + time-frame)
- [ ] Challenge specific (named user, named moment, named consequence)
- [ ] Process shows 2-3 key moments (not every step)
- [ ] Solution walks the design with rationale
- [ ] Impact has both quant + qual + "what we'd do differently"
- [ ] Reflection captures learnings
- [ ] Trade-offs named honestly
- [ ] Real screenshots (not just mockups)
- [ ] First person for contributions
- [ ] No marketing verbs / corporate adjectives
- [ ] Voice passes the read-aloud test

Then offer:

> "Adapt the case for other formats — LinkedIn (`manfred-toolkit:linkedin-show-and-tell`), conference talk (`manfred-toolkit:presentation-deck` via `/manfred-toolkit:build-presentation`), or stakeholder update."
