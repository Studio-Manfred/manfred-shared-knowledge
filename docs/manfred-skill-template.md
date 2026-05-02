# Manfred SKILL.md template

Conventions every skill in a `manfred-*` plugin follows. Use this as a checklist when writing or reviewing a new SKILL.md.

> Adapted skills (forks of MIT-licensed third-party content like `Owl-Listener/designer-skills`) must also clear this checklist — they're not exempt because they're forks.

## 1. Voice

Manfred's voice — pulled from `~/.claude/shared/manfred-brand.md`:

- **Warm + precise.** Conversational fragments are full sentences. ("Yep." "Of course." "Just when you need it.")
- **Direct second person.** Talk *to* the reader.
- **Concrete over abstract.** "Messy scale-ups, suit-heavy orgs" not "mid-sized to enterprise clients."
- **Self-deprecating where most brands posture.** "Winging it with a whiteboard" is a legitimate mode.
- **Q&A beat OK.** "Is this scope creep? Yep. Push back."
- **Serious-serious-wink triplet OK.** "Smart work, sharp thinking, and a bit of fun."

### Anti-patterns (never)

- Marketing verbs: *transform, empower, leverage, unlock, supercharge, drive, deliver value*
- Corporate adjectives: *cutting-edge, world-class, innovative, best-in-class, passionate*
- "We're passionate about…"
- Forced levity (emoji clutter, exclamation stacking, "haha we're quirky" energy)
- Hedging ("we might be able to…")
- Feature-list structure where a conversation would do

### The quick test

Before shipping a SKILL.md, ask:

1. Could I read this out loud without cringing?
2. Would I say "yep" in response to any of the headlines?
3. Is there at least one fragment, one concrete noun, and zero marketing verbs?
4. Does it trust the reader to be an adult? (No over-explaining, no hedging, no performative enthusiasm.)

If any answer is no — rewrite.

## 2. Cagan + Torres lens

Where the topic touches **discovery, strategy, validation, or assumption-testing**, the skill must explicitly map output to:

- One of **Cagan's 4 product risks** — value, usability, feasibility, viability
- And/or a node on a **Torres opportunity-solution tree** — outcome / opportunity / solution / assumption-test

Skip this lens for skills where it doesn't apply (e.g. `typography-scale`, `color-palette`, `markitdown-convert`). For those, the lens is just dead weight.

When in doubt: if a skill's output could change a build/no-build decision, the lens applies. If it's about how something looks or feels in execution, it usually doesn't.

## 3. Manfred outputs

Skills that produce artifacts route them through Manfred's tooling where possible:

- **Linear**: tickets are linked from branch names (`feat/STU-123-…`). When a skill produces a report or summary tied to a ticket, post it as a Linear comment via `mcp__linear-server__save_comment` after resolving the issue with `mcp__linear-server__get_issue`. Pattern reference: `plugins/manfred-dev/skills/test-my-code/SKILL.md` (Linear update section).
- **Vercel**: deploy hooks via the existing `manfred-dev/skills/release` pattern when relevant.
- **Design system**: when producing CSS/Tailwind/component output, use semantic tokens from `~/.claude/shared/DESIGN.md` (e.g. `bg-background`, `text-foreground`, `bg-primary`) — never hardcoded hex. Use named brand utilities (`bg-business-blue`, `bg-human-pink`) only for explicit literal-brand surfaces.
- **File outputs**: reports go under a topic-specific directory (`qa-reports/`, `discovery-reports/`, etc.) named `<TICKET-or-slug>-<YYYY-MM-DD>.md`.

## 4. Frontmatter

```yaml
---
name: skill-name-with-hyphens
description: Use when [specific triggering phrases and symptoms]. Stack/context if applicable. Do NOT summarise the workflow.
---
```

- `description` starts with "Use when…"
- Lists trigger phrases the user is likely to say
- Specifies stack/context only when narrow (e.g. "Vite/React, vitest + Playwright")
- Does **not** summarise the skill's process or workflow — that goes in the body. (Per `superpowers:writing-skills` — descriptions that summarise workflow cause Claude to follow the description instead of reading the body.)

## 5. Body structure

Recommended sections, in order:

1. **Overview** — 1–2 sentences. What this skill does, core principle.
2. **When to Use** — bullet list of triggers + a "Skip when" carve-out.
3. **Pre-flight** (if the skill needs context-gathering) — branch parsing, ticket lookup, file scope, etc.
4. **The actual work** — steps, tables, gates, rules. Use tables for parallel structure.
5. **Manfred lens callout** (if applicable) — explicit map to Cagan risks / OST nodes.
6. **Output format** — exact template if the skill produces an artifact.
7. **Common rationalizations** — table of "Excuse | Reality" pairs (for discipline-shaped skills).
8. **Red flags — STOP** — specific moments that should halt execution.
9. **Tools used** — list of Bash commands, MCP tools, other skills called.

Scale to the task. Not every skill needs all 9.

## 6. Cross-skill references

When a skill calls into another skill, reference it by full plugin-qualified name:

- ✅ `mcp__linear-server__get_issue`
- ✅ `superpowers:verification-before-completion`
- ✅ `manfred-discovery:opportunity-solution-tree`
- ❌ `the OST skill` (ambiguous — multiple plugins might have one)

## 7. TDD-for-skills

Every fresh skill goes through `superpowers:writing-skills`'s RED → GREEN → REFACTOR loop:

1. **RED** — dispatch a baseline subagent without the skill loaded. Document the gaps.
2. **GREEN** — write the SKILL.md addressing those gaps.
3. **REFACTOR** — dispatch a second subagent with the skill loaded; pressure-test for compliance and find rationalizations.

Adapted skills (forks) skip RED but must still pass REFACTOR.

## 8. Attribution

If the skill is adapted from `Owl-Listener/designer-skills` (MIT) or another open-source source, add a footer:

```markdown
---
*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
```

Keep it short. The work to make it Manfred is in the body, not the credit.

## 9. README per plugin

Each `plugins/manfred-*/README.md` lists:

- One-paragraph plugin description in Manfred voice
- Skills table (name → trigger phrase)
- Commands table (if any)
- `Install` block with `/plugin install <name>@manfred`
- Cross-plugin dependencies (if a skill calls into another plugin's skill)
