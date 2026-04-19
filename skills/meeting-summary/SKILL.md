---
name: meeting-summary
description: Use when the user asks to summarize a meeting, meeting notes, or meeting transcript. Triggers on "summarize meeting", "meeting summary", "meeting notes", "mötessammanfattning", "sammanfatta möte".
---

# Meeting Summary

Summarize meeting transcripts into a structured, actionable format. Output only the summary — never create files or directories unless asked.

## When to Use

- User provides a meeting transcript or recording notes to summarize
- User asks to "summarize this meeting" or "write meeting notes"

**When NOT to use:**
- Workshop facilitation notes (different structure needed)
- Lecture or presentation notes (no decisions/actions pattern)

## Language Rule

**Write the summary in the language that dominates the transcript text.** Count the actual words spoken — not who the speakers are or what company they work for. If the transcript is 70% Swedish with some English terms, write in Swedish. If the transcript is mostly English, write in English — even if the team is Swedish. Technical terms can stay in their original language regardless.

## Output Structure

Use exactly this structure. Every section is required. Use Obsidian-compatible markdown.

```markdown
## [Datum och möte / Date and meeting]

[Exactly three sentences: (1) who attended, (2) what the meeting covered, (3) the key outcome. Not four. Not two.]

## Beslut / Decisions

- [Only concrete decisions. Not things discussed — things concluded.]
- [Be specific: names, numbers, feature names, deadlines.]

## Mina uppgifter / My action items

- [Only tasks belonging to Jens. Start each with a verb.]
- [Be direct and actionable.]

## Andras uppgifter / Others' action items

- **[Name]:** [Task with deadline if mentioned]

## Öppna frågor / Open questions

- [Unresolved things, dependencies, or follow-up decisions needed.]

## Kontext att minnas / Context worth keeping

- [Maximum 5 bullets.]
- [Only include if it explains a decision or will matter in a future meeting.]
- [Skip generic discussion.]
```

## Rules

1. **Decisions are not discussions.** If nobody concluded anything, it's not a decision. "We talked about X" is not a decision. "We chose X" is.
2. **Jens's tasks are separate.** Any action item for Jens goes under "Mina uppgifter", everyone else goes under "Andras uppgifter".
3. **Context is filtered.** The "Kontext att minnas" section has a hard cap of 5 bullets. Each bullet must pass the test: "Will this matter in a future meeting?" If no, cut it.
4. **No file creation.** Return the summary as text in the conversation. Do not create files or directories unless the user explicitly asks.
5. **No tables.** Use bullet lists for everything. Tables add visual noise without value in meeting notes.
6. **No rationale or discussion sections.** The summary captures outcomes, not process.
7. **Section headers are bilingual.** Always use the Swedish / English format shown above, regardless of transcript language.

## Common Mistakes

- **Writing in English when the meeting was in Swedish** — match the dominant transcript language
- **Adding a "Discussion points" section** — not part of this format, cut it
- **Lumping all action items together** — always separate Jens's items from others'
- **Including more than 5 context bullets** — hard cap, prioritize ruthlessly
- **Using tables for decisions or actions** — use bullet lists only
- **Creating files unprompted** — output text in conversation unless asked otherwise
- **Writing four sentences in the overview** — the limit is exactly three, compress if needed
- **Listing implementation fixes as decisions** — "we'll fix X by doing Y" is an action item, not a decision. A decision is a choice between alternatives
- **Writing in Swedish because the team is Swedish** — language is determined by the transcript text, not the company or participants
