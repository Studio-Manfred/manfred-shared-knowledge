---
name: user-archetype
description: Use when synthesising research into behavioural user archetypes. Chosen over "user persona" because archetypes are role-and-behaviour-based — no invented names, stock photos, or biographical fiction. Triggers on "user archetype", "behavioural archetype", "user types", "research-grounded archetypes", "cluster users by behaviour", "who are our users". Refuses to invent details not in the research data.
---

# user-archetype

A research-grounded behavioural archetype. Not a persona — no name, no stock photo, no biographical fiction. The unit of synthesis is *patterns of behaviour* the team has actual evidence for.

## Overview

User personas are useful when grounded; harmful when invented. The harmful pattern: a team brainstorms "Sarah, 34, marketing manager, likes yoga" — and then makes design decisions on Sarah's imagined preferences. The fiction creeps into the decisions.

**Archetypes** sidestep this by staying behavioural and role-based:

- ❌ "Sarah, 34, marketing manager at a mid-sized SaaS company, has 2 kids, drinks oat milk, likes Slack notifications."
- ✅ "The experienced solo freelancer — issues 5–15 invoices a month, has used 3+ tools before, treats invoicing as 5 minutes of necessary admin, resents anything that adds steps."

Same data; different framing. The archetype focuses the team on the behavioural cluster (which decisions actually need to serve), not the person (which the team will project their own assumptions onto).

This skill produces 2–4 behavioural archetypes from research data, with the patterns that define each, the design implications, and the gaps where the data is thin.

## When to use

- Multiple interview summaries (5+) from a coherent product / service area
- Affinity-diagram themes show distinct behavioural clusters
- The team needs a shared mental model for design decisions
- After `manfred-design-research:summarize-interview` and `affinity-diagram`

**Skip when:**

- You have <5 interviews — too thin for clustering
- Single coherent user type — one archetype isn't worth the artifact
- The team needs personas for marketing or sales — those are different artifacts (and OK to invent biographical detail for; just don't confuse them with research-grounded synthesis)

## Two principles drive everything

1. **No invented detail.** No name, no stock photo, no fictional bio. Every attribute of the archetype must trace to research evidence. If you don't know whether they have kids — don't say. If you don't know their education — don't say. The discipline is the point.
2. **Behavioural over demographic.** Demographic ("women 30–50") doesn't predict behaviour and creates fairness problems. Behavioural ("issues 5+ invoices a month, has tried 3+ tools, resents friction") predicts behaviour and stays research-grounded.

## Phase 1 — Pre-flight

- **Source data:** at least 5 interview summaries + (ideally) supporting affinity diagram for the segment
- **Output path:** `discovery/archetypes/<product-area-slug>-<YYYY-MM-DD>.md`
- **Linked OST outcome:** archetypes serve a specific outcome — name it

## Phase 2 — Identify behavioural clusters

From the affinity diagram themes (or directly from summaries), look for clusters in:

- **Volume / frequency** of the activity ("issues 5+ invoices/month" vs "issues 1/quarter")
- **Tools / context** ("has used multiple tools before" vs "this is their first")
- **Attitude toward the activity** ("treats it as core craft" vs "treats it as necessary admin")
- **Skill / experience** ("can debug their own setup" vs "calls support immediately")
- **Decision authority** ("can choose tools alone" vs "needs sign-off")
- **Constraint sensitivity** ("optimises for cheapest" vs "optimises for least friction")

Aim for 2–4 distinct archetypes. Below 2: not worth the artifact. Above 4: clusters too fine, consolidate.

## Phase 3 — For each archetype, define

| Field | What goes here |
|-------|----------------|
| **Name** | Behavioural label, not a person's name. e.g. "Experienced solo freelancer", "First-time founder", "Skeptical evaluator" |
| **Defining behaviours** | 3–5 observable patterns from the data — with source citations |
| **Goal** | What they're trying to get done in the relevant area (link to `manfred-design-research:jobs-to-be-done`) |
| **Frustrations** | Concrete pains, source-cited |
| **Decision drivers** | What makes them say yes / no to a tool or feature |
| **Success indicators for the team** | How would the team know this archetype is well-served? |
| **Anti-patterns to avoid** | Designs that would alienate this archetype |
| **Accessibility / inclusion notes** | Specific known accessibility characteristics from research, OR explicit "no data — needs research" |
| **Sample size** | How many of the source participants fit this archetype (e.g. "5 of 8 interview participants") |
| **Confidence** | How well does the data support this archetype as a distinct cluster? (H/M/L with reason) |

## Phase 4 — Cross-archetype dynamics

Two questions worth answering:

- **Where do archetypes overlap?** Some users may straddle archetypes; note where the same person could be in two.
- **Where do archetypes conflict?** Sometimes serving Archetype A makes life worse for Archetype B. The team needs to see these tensions explicitly.

## Phase 5 — What's missing (the gaps)

Honest research surfaces what the archetypes *don't* cover:

- Segments not represented in the recruit
- Behavioural patterns that appeared once but didn't cluster
- Accessibility / disability dimensions where data is thin

These become input for the next research cycle (`manfred-discovery:customer-touchpoint-plan`).

## Phase 6 — Output

Save to `discovery/archetypes/<product-area-slug>-<YYYY-MM-DD>.md`:

```markdown
# User archetypes — [Product area]

**Date:** [YYYY-MM-DD]
**Linked outcome:** [from the OST]
**Sources:** [N interview summaries, affinity diagram path]
**Synthesised by:** [Trio names]

## Archetype 1 — [Behavioural label]

**Sample size:** [N of N source participants fit this]
**Confidence:** H / M / L ([reason])

### Defining behaviours
- [Observable pattern 1] — [source citation]
- [Observable pattern 2] — [source citation]
- [Observable pattern 3] — [source citation]

### Goal
[What they're trying to get done — links to jobs-to-be-done if mapped]

### Frustrations
- [Concrete pain] — [verbatim quote with source]
- [...]

### Decision drivers
- [What makes them say yes] — [source]
- [What makes them say no] — [source]

### Success indicators for the team
- [Observable behaviour that would indicate the archetype is well-served]
- [...]

### Anti-patterns to avoid
- [Design pattern that would alienate this archetype] — [reason]

### Accessibility / inclusion notes
- [Specific known characteristics from research]
- _OR: "No data — recruit needs to include AT/disabled users in next cycle for this archetype."_

## Archetype 2 — [...]
[...]

## Cross-archetype dynamics

### Overlaps
- [Archetype A and Archetype B both share behaviour X — note the user could fit both]

### Conflicts
- [Serving Archetype A's preference for X may worsen Archetype B's experience of Y]

## What's missing (gaps)

- [Behavioural patterns observed but didn't cluster cleanly]
- [Segments / experiences not represented in the recruit]
- [Accessibility dimensions thin in current data]

## Linked artifacts

- Source summaries: [paths]
- Source affinity: [path]
- Linked journey maps: [paths — one per archetype as they're created]
- Linked empathy maps: [paths]
- Linked OST opportunities: [links]
```

If a Linear ticket is linked, post the archetype names + sample size + confidence as a Linear comment.

## Manfred lens

- **Customer-driven always** (principle 1) — archetypes are research-grounded, not invented
- **Critical & ethical design** (principle 6) — behavioural focus avoids demographic stereotyping
- **Accessible first** (principle 5) — explicit accessibility section per archetype, not afterthought
- **Craft seriously** (principle 3) — confidence ratings + sample sizes; no fake precision
- **Consistent, not uniform** (principle 11) — surfaces archetype conflicts so the team designs intentionally

## Cross-plugin handoffs

- **Input from `manfred-design-research:summarize-interview`** — the source patterns
- **Input from `manfred-design-research:affinity-diagram`** — themes inform the behavioural clusters
- **Output to `manfred-design-research:journey-map`** — one journey map per archetype
- **Output to `manfred-design-research:empathy-map`** — one empathy map per archetype
- **Output to `manfred-design-research:jobs-to-be-done`** — archetype goal links to JTBD
- **Output to `manfred-discovery:opportunity-solution-tree`** — anti-patterns + frustrations become opportunities

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "Personas are easier to remember — give them names" | Names create projection. The team will start saying "Sarah wouldn't…" — that's the failure mode. Names are the bug, not the feature. |
| "Add a stock photo so the team feels connected to the user" | Stock photos invite projection AND racial / age / gender bias. No photos. |
| "Fill in age / income / family status from typical-segment data" | That's marketing-segment data, not research. Don't fabricate it into a research artifact. |
| "Skip 'sample size' — looks weak" | It is weak when N=2. Better to surface that than fake confidence. |
| "Cross-archetype conflicts are too negative for the deliverable" | Conflicts are the most useful insight. Show them. The team needs to see what trade-offs the design makes. |
| "Accessibility section can be 'TBD' across all archetypes" | Then say "no data" explicitly and surface the recruit gap. Don't leave it blank. |
| "Skip the 'what's missing' section — focuses on negatives" | Honest research surfaces gaps. Hiding them creates false confidence. |

## Red flags — STOP

- About to give an archetype a person's name → Stop. Behavioural label only.
- About to attach a stock photo → Stop. No photos.
- About to fill demographic detail not in the research → Stop. Behavioural attributes only.
- About to claim an archetype is High confidence with N=1–2 source participants → Stop. Re-rate.
- About to skip the cross-archetype conflicts section → Stop. They're the most useful output.
- About to skip the accessibility section → Stop. Either name what you found or surface the gap.
- About to define an archetype primarily by demographics ("Women 25–35 in tech") → Stop. Behavioural attributes only.

## Tools used

- **Read**: source summaries, affinity diagram
- **Write**: `discovery/archetypes/<slug>-<date>.md`
- **MCP** (when ticket linked): `mcp__linear-server__get_issue`, `mcp__linear-server__save_comment`
- **Skills called**:
  - `manfred-design-research:journey-map` — one per archetype
  - `manfred-design-research:empathy-map` — one per archetype
  - `manfred-design-research:jobs-to-be-done` — link to the archetype's goal
  - `manfred-discovery:opportunity-solution-tree` — frustrations become opportunities
- **Reference**: Indi Young (thinking styles); Alan Cooper (behavioural personas / archetypes); Lene Nielsen on persona pitfalls; the broader case for archetypes-over-personas in inclusive design literature

---

*Manfred-original skill. Chosen over "user persona" specifically to sidestep the projection / bias / fabrication failure modes common in persona work. Structurally inspired by [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills)'s `user-persona` skill (MIT) — but the framing, anti-fabrication discipline, cross-archetype conflicts, and explicit gaps section are Manfred-original.*
