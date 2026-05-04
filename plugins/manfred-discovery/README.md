# manfred-discovery

Manfred-flavoured product discovery. Cagan's four risks, Torres's continuous discovery and opportunity-solution trees, Manfred's product brief — pulled into one plugin. Built to make customer-driven decisions, not feature lists.

## Skills

| Skill | Triggers when you say… |
|-------|-----------------------|
| `cagan-risks` | "what are the Cagan risks", "assess the four risks", "value/usability/feasibility/viability", "risk profile this idea", "is this ready for build?" |
| `opportunity-solution-tree` | "build an OST", "opportunity solution tree", "Torres tree", "map outcomes to opportunities", "tree this out" |
| `assumption-test` | "test this assumption", "design an assumption test", "what's the riskiest assumption", "assumption mapping", "smallest test we can run" |
| `customer-touchpoint-plan` | "plan customer interviews this week", "weekly customer touchpoint", "continuous discovery interviews", "set up discovery cadence" |
| `product-brief` | "write a product brief", "PRD", "feature spec", "shape this opportunity", "kick off a feature" |
| `discovery-readout` | "summarise what we learned", "discovery readout", "what came out of the research", "post the discovery summary" |
| `discovery-rituals` | "set up discovery rituals", "team discovery cadence", "OST review meeting", "weekly assumption test review" |

## Commands

| Command | What it does |
|---------|--------------|
| `/manfred-discovery:kickoff` | Frame a new opportunity end-to-end. Chains `product-brief` → `cagan-risks` → `opportunity-solution-tree`. |
| `/manfred-discovery:weekly` | Run one week of continuous discovery. Chains `customer-touchpoint-plan` → `assumption-test` → `discovery-readout`. |
| `/manfred-discovery:risk-check` | Quick risk pass on an in-flight feature. `cagan-risks` deep dive, branches to the relevant assumption test. |

## When to reach for this plugin

You're shaping something — an opportunity, a feature, a problem area — and you need to figure out what's true before committing build effort. Or you're already in the middle of something and want to pressure-test whether it deserves more time. Either way, this plugin is the room where customer evidence wins over hunches.

If you want the lighter shape — just write the brief, no ceremony — use `product-brief` directly.

## Cross-plugin dependencies

- **`discovery-readout`** uses the Linear MCP integration pattern from `manfred-dev:test-my-code`. If a branch maps to a Linear ticket (`STU-\d+`), the readout posts as a comment on the ticket.
- **`product-brief`** replaces the older `manfred-product:brief-prd` (the `manfred-product` plugin was removed in v1.0.0).

## Install

```
/plugin marketplace add Studio-Manfred/manfred-shared-knowledge
/plugin install manfred-discovery@manfred
```

## Background

- **Marty Cagan**'s four product risks — value, usability, feasibility, viability — from *Inspired* and the SVPG essays. The `cagan-risks` skill maps an idea to these explicitly and recommends the cheapest test to retire each one.
- **Teresa Torres**'s continuous discovery — opportunity-solution trees, weekly customer touchpoints, assumption mapping — from *Continuous Discovery Habits*. The `opportunity-solution-tree`, `customer-touchpoint-plan`, and `assumption-test` skills are direct applications.
- **Manfred's product brief** is the studio's 8-section template (Opportunity → Strategic Alignment → Hypothesis → Success Metrics → Cagan Risks → Scope → Dependencies → Recommended Next Step). Originally shaped during Scandic engagements, generalised here.
