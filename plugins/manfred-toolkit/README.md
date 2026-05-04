# manfred-toolkit

Manfred-flavoured designer toolkit: UX writing (Manfred voice baked in), case studies, design rationale, design-system adoption + token audit, presentation decks, meeting summaries (bilingual SV/EN), and the LinkedIn (Swedish) post trio.

Voice rules from `~/.claude/shared/manfred-brand.md` enforced throughout. Errors explain, don't blame. Quick test before any output ships: could I read this aloud without cringing?

## Skills

| Skill | When it triggers |
|-------|-----------------|
| `ux-writing` | "write microcopy", "write error messages", "write button labels", "write empty state copy", "write CTAs" — **foundational TDD'd skill**: refuses generic-SaaS-friendly tics ("Oops!", "Hmm,", "Welcome aboard!"); demands real failure-mode context for errors; CTAs are specific verbs with outcomes |
| `case-study` | "case study", "write up this project", "portfolio piece", "client showcase" — customer-driven framing, evidence over polish, honest trade-offs, voice from `manfred-brand.md` |
| `design-rationale` | "design rationale", "why did we choose this", "design decision doc", "ADR for design" — connects to canonical 15 design principles + customer evidence; alternatives + trade-offs named honestly |
| `design-system-adoption` | "design system adoption", "get teams to use the DS", "system rollout", "DS not being used" — treat the system as a product with users; barriers surfaced honestly; metrics + qualitative pairing |
| `design-token-audit` | "design token audit", "token coverage", "are we using tokens", "find hex literals" — three-layer audit (primitives → semantic → shadcn contract); flags + recommends, doesn't auto-fix |
| `meeting-summary` | "summarize meeting", "meeting summary", "meeting notes", "mötessammanfattning", "sammanfatta möte" — bilingual structure (Swedish + English headers); language follows transcript dominance, not team origin; decisions ≠ discussions; Jens's actions separated from others' |
| `presentation-deck` | "presentation", "deck", "slides", "stakeholder slides", "showcase deck" — hook → context → journey → solution → evidence → ask; one idea per slide |
| `linkedin-teach` | LinkedIn post (Swedish) that teaches a concept, process, or tool through personal experience |
| `linkedin-show-and-tell` | LinkedIn post (Swedish) that demonstrates something concrete — a tool, output, demo, or result |
| `linkedin-reflect` | LinkedIn post (Swedish) that looks back on an experience, celebrates people, or makes sense of something |

## Commands

| Command | What it does |
|---------|--------------|
| `/manfred-toolkit:build-presentation` | Build a presentation end-to-end. Scope + audience + structure + outline + voice pass + production-ready deck. |
| `/manfred-toolkit:write-case-study` | Write a portfolio-ready case study end-to-end. Outcome hook + structured narrative + evidence + voice pass. |
| `/manfred-toolkit:write-rationale` | Write a design rationale for a major decision. Decision + context + alternatives + evidence + reasoning + trade-offs + validation plan. |

## Manfred opinions baked in

- **Voice rules from `manfred-brand.md`** — anti-marketing-verb list (transform, empower, leverage, unlock, supercharge, drive, deliver value), anti-corporate-adjective list (cutting-edge, world-class, innovative, best-in-class, passionate), fragments OK, direct second person, concrete over abstract
- **Errors explain, don't blame** — `ux-writing` enforces error-message structure (what happened / what to do / one clear action); user is never the subject of the failure
- **CTAs are specific verbs with outcomes** — "Get in touch" not "Submit"; "Save changes" not "Save"; "Send invite" not "OK"
- **Quick test** before any output ships — could I read this aloud without cringing? If yes, rewrite.
- **Customer evidence floor** — case studies, rationales, presentations all cite specifically (research session date + n, analytics event, customer verbatim) — generic claims get pushed back
- **Trade-offs named** — case studies, rationales, presentations all surface what was given up; cases without trade-offs are propaganda
- **Bilingual where it matters** — `meeting-summary` headers are always Swedish + English; language follows the transcript text, not the team origin

## Cross-plugin handoffs

- **Pulls from `manfred-design-research`** — customer quotes (`summarize-interview`), affinity findings, archetype-based case-study subjects
- **Pulls from `manfred-discovery`** — discovery readouts feed case studies + presentations
- **Pulls from `manfred-ux-strategy`** — design briefs, metrics-definition, principles all feed rationales + cases
- **Pulls from `manfred-design-systems`** — token audits run against the system; design rationales reference component-spec decisions
- **Pulls from `manfred-design-ops`** — handoff specs reference rationales for non-obvious decisions; design reviews feed rationale-writing moments
- **Receives from `manfred-interaction-design`** — `error-handling-ux` hands off structured copy requests to `ux-writing`
- **Cross-references `~/.claude/shared/manfred-brand.md`** — non-optional voice doc for every skill in this plugin
- **Cross-references `~/.claude/shared/DESIGN.md`** — for token-audit work + presentation-deck visual style

## Install

```
/plugin marketplace add Studio-Manfred/manfred-shared-knowledge
/plugin install manfred-toolkit@manfred
```
