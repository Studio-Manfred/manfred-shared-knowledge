# manfred-design-research

User research, the way Manfred runs it. Continuous over project-shaped, Trio-attended, story-based, grounded in real evidence.

## Skills

| Skill | Triggers when you say… |
|-------|-----------------------|
| `interview-script` | "interview script", "user interview prep", "discovery interview", "customer conversation guide" |
| `summarize-interview` | "summarise the interview", "interview notes", "what did the customer say", "transcript synthesis" |
| `affinity-diagram` | "affinity diagram", "synthesise the research", "cluster these notes", "find the themes" |
| `card-sort-analysis` | "card sort results", "card sort analysis", "open card sort", "closed card sort", "tree test plan" |
| `diary-study-plan` | "diary study", "longitudinal study", "behaviour over time", "in-context study" |
| `empathy-map` | "empathy map", "Says/Thinks/Does/Feels", "build empathy", "synthesise the user" |
| `jobs-to-be-done` | "JTBD", "jobs to be done", "what job is the customer hiring this for", "functional / emotional / social job" |
| `usability-test-plan` | "usability test", "moderated test", "unmoderated test", "usability study plan" |
| `journey-map` | "journey map", "experience map", "stages and touchpoints", "moments of truth" |
| `user-archetype` | "user archetype", "behavioural archetype", "user types", "research-grounded archetypes" |
| `transcript-anonymizer` | "anonymise transcript", "PII removal", "GDPR compliance", "scrub personal data", "de-identify" |

## Commands

| Command | What it does |
|---------|--------------|
| `/manfred-design-research:discover` | Run a discovery cycle: interviews → summaries → affinity → archetypes |
| `/manfred-design-research:interview` | Plan + script + summarise a single interview round |
| `/manfred-design-research:synthesize` | Take raw notes/transcripts and produce affinity + insights + journey/empathy artifacts |
| `/manfred-design-research:test-plan` | Design a moderated or unmoderated usability test |

## Manfred posture

- **Research isn't a phase** (Manfred design principle 2). Continuous over big-bang. Every skill ties back to the cadence in `manfred-discovery:discovery-rituals`.
- **The Trio attends** (PM + designer + tech lead). Async transcript-reading is a fallback, not the default. Interview and usability skills enforce Trio scheduling.
- **Story-based interviewing** (Torres). Past behaviour beats hypothetical future. Skills refuse leading and hypothetical questions.
- **Pay people for their time.** Recruit guidance includes incentive.
- **Customer-driven always** (principle 1). Research grounds product decisions; not the other way round.
- **Accessible first** (principle 5). Recruit + test design include disabled and neurodiverse participants; testing covers assistive tech.

## Cross-plugin handoffs

- **Outputs feed `manfred-discovery`** — synthesis updates the OST (`manfred-discovery:opportunity-solution-tree`), recruit goes through `manfred-discovery:customer-touchpoint-plan`, qualitative signal feeds `manfred-discovery:assumption-test`, cycles wrap with `manfred-discovery:discovery-readout`.
- **Inputs from `manfred-ux-strategy`** (when research is strategy-led, not discovery-led) — landing in v1.0.0.
- **Outputs feed `manfred-toolkit`** — `case-study`, `design-rationale`, `presentation-deck` consume the research summaries this plugin produces.

## Install

```
/plugin marketplace add Studio-Manfred/manfred-shared-knowledge
/plugin install manfred-design-research@manfred
```

## Background

Adapted from [Owl-Listener/designer-skills/design-research](https://github.com/Owl-Listener/designer-skills/tree/main/design-research) (MIT) for the structural skills (affinity-diagram, card-sort-analysis, diary-study-plan, empathy-map, interview-script, jobs-to-be-done, journey-map, summarize-interview, usability-test-plan). Each adapted skill carries an attribution footer.

`user-archetype` is Manfred-original — chosen over the more common "user persona" because archetypes (behavioural, role-based) sidestep the marketing-persona trap and stay grounded in actual research patterns rather than demographic invention.

`transcript-anonymizer` is Manfred-original, relocated from `manfred-writing` (where it lived in v0.13.x).
