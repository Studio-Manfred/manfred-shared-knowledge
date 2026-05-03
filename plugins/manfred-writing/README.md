# manfred-writing

Writing helpers for meeting summaries and (transitionally) LinkedIn posts + transcript handling.

## Status — partially deprecated in v0.18

| Skill | Status | Where it lives |
|-------|--------|----------------|
| `meeting-summary` | **Active** — only skill currently rooted here | `manfred-writing:meeting-summary` |
| `linkedin-reflect` | **Deprecated** — moved to `manfred-toolkit:linkedin-reflect` | Identical content lives at the new home |
| `linkedin-show-and-tell` | **Deprecated** — moved to `manfred-toolkit:linkedin-show-and-tell` | Identical content lives at the new home |
| `linkedin-teach` | **Deprecated** — moved to `manfred-toolkit:linkedin-teach` | Identical content lives at the new home |
| `transcript-anonymizer` | **Deprecated** (since v0.14) — moved to `manfred-design-research:transcript-anonymizer` | Identical content lives at the new home |

## Migrate

```
/plugin install manfred-toolkit@manfred         # for the linkedin trio
/plugin install manfred-design-research@manfred # for transcript-anonymizer
```

The skill names are unchanged at their new homes — references like `manfred-toolkit:linkedin-reflect` and `manfred-design-research:transcript-anonymizer` work the same way as the old `manfred-writing:` versions did.

## Why the partial deprecation

`manfred-toolkit` is the v1.0.0 home for content + writing skills (case studies, design rationale, presentation decks, UX writing, LinkedIn). The linkedin trio belongs there. `transcript-anonymizer` belongs in `manfred-design-research` (where it serves the user-research workflow).

`meeting-summary` stays here for now — its eventual v1.0.0 home is unresolved (could go to `manfred-toolkit`, `manfred-design-ops`, or stay general). Will be relocated before v1.0.0.

## Skills (legacy — install replacements above where deprecated)

| Skill | When it triggers |
|-------|-----------------|
| `meeting-summary` | Summarising a meeting, notes, or transcript (English or Swedish) |
| `linkedin-teach` *(deprecated)* | LinkedIn post (Swedish) that teaches a concept, process, or tool through personal experience |
| `linkedin-show-and-tell` *(deprecated)* | LinkedIn post (Swedish) that demonstrates something concrete — a tool, output, demo, or result |
| `linkedin-reflect` *(deprecated)* | LinkedIn post (Swedish) that looks back on an experience, celebrates people, or makes sense of something |
| `transcript-anonymizer` *(deprecated)* | Removing PII from interview transcripts or research notes for GDPR/CCPA compliance |

## Install

```
/plugin marketplace add Studio-Manfred/manfred-shared-knowledge
/plugin install manfred-writing@manfred
```
