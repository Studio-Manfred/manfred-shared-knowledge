---
name: transcript-anonymizer
description: Use when the user wants to anonymize transcripts, remove PII from text files, comply with GDPR/CCPA for research data, de-identify interviews, scrub personal data from .txt/.md files, or clean research notes for privacy. Triggers on "anonymize", "PII removal", "GDPR compliance", "scrub personal data", "de-identify".
---

# Transcript Anonymizer

Anonymize research transcripts and text files for GDPR/CCPA compliance by detecting personal information and replacing it with consistent, readable placeholders.

## When to Use

- User wants to anonymize interview transcripts or research notes
- User mentions GDPR, CCPA, PII removal, or de-identification
- User points at a folder of text files and asks to "clean" or "scrub" personal data

**When NOT to use:**
- Structured data (JSON, CSV, databases) — different tools needed
- Redacting documents for legal discovery (different process and requirements)
- Anonymizing code or configuration files

## Quick Reference

| Step | Action | Output |
|------|--------|--------|
| 1 | Confirm target folder | File list |
| 2 | Read files, build PII registry | Consistent placeholder mapping |
| 3 | Create `anonymized/` subfolder | Output structure |
| 4 | Write anonymized copies | `{name}_anonymized.{ext}` |
| 5 | Write anonymization log | `anonymization_log.md` |
| 6 | Present results | Summary + review offer |

## Why this matters

Research transcripts contain real conversations with real people. Regulations like GDPR and CCPA require that personal information is protected. Simply deleting PII destroys context — placeholders preserve the readability and research value of the transcript while keeping individuals unidentifiable.

## Workflow

### Step 1: Confirm the target folder

Ask the user which folder contains the transcripts if they haven't already specified one. Verify the folder exists and list the `.txt` and `.md` files found.

### Step 2: First pass — read and identify PII

Read each file and identify all instances of personal information. Build a **PII registry** — a mapping that ensures consistency across all files in the batch.

**PII categories to detect and their placeholder format:**

| Category | Example | Placeholder format |
|---|---|---|
| Person names | "Anna Svensson" | `[PERSON_1]`, `[PERSON_2]`, ... |
| Email addresses | "anna@example.com" | `[EMAIL_1]`, `[EMAIL_2]`, ... |
| Phone numbers | "+46 70 123 4567" | `[PHONE_1]`, `[PHONE_2]`, ... |
| Physical addresses | "Storgatan 12, Stockholm" | `[ADDRESS_1]`, `[ADDRESS_2]`, ... |
| Company names | "Acme Corp" | `[COMPANY_1]`, `[COMPANY_2]`, ... |
| Job titles | "Senior UX Designer" | `[JOBTITLE_1]`, `[JOBTITLE_2]`, ... |
| Ages | "34 years old" | `[AGE_1]`, `[AGE_2]`, ... |
| Cities/Locations | "Gothenburg" | `[LOCATION_1]`, `[LOCATION_2]`, ... |
| Dates of birth | "1989-03-15" | `[DOB_1]`, `[DOB_2]`, ... |
| IP addresses | "192.168.1.1" | `[IP_1]`, `[IP_2]`, ... |

**Consistency rule:** The same real value gets the same placeholder everywhere. If "Anna Svensson" appears in three different files, she is `[PERSON_1]` in all three. This preserves cross-reference ability without exposing identity.

### Step 3: Create output structure

Inside the folder containing the original files, create:

```
anonymized/
├── file1_anonymized.md
├── file2_anonymized.txt
├── ...
└── anonymization_log.md
```

The originals are never modified.

### Step 4: Write anonymized copies

For each file, create an anonymized copy with all PII replaced by placeholders. Keep all other content, formatting, and structure identical.

Name the output files: `{original_name}_anonymized.{ext}`

### Step 5: Write the anonymization log

Create `anonymization_log.md` in the `anonymized/` folder with:

```markdown
# Anonymization Log

**Date:** YYYY-MM-DD
**Files processed:** N
**Tool:** Claude Code transcript-anonymizer

## Summary

Total PII instances found: X
Categories detected: [list]

## Per-file details

### filename.md
- [PERSON_1] — 3 occurrences (person name)
- [EMAIL_1] — 1 occurrence (email address)
- [COMPANY_1] — 2 occurrences (company name)

### filename2.txt
- [PERSON_1] — 1 occurrence (person name)
- [PERSON_2] — 4 occurrences (person name)
- [LOCATION_1] — 2 occurrences (city/location)

## Placeholder Registry

| Placeholder | Category | Occurrences | Files |
|---|---|---|---|
| [PERSON_1] | Person name | 4 | file1.md, file2.txt |
| [EMAIL_1] | Email | 1 | file1.md |
| [COMPANY_1] | Company | 2 | file1.md |
```

The log does NOT contain the original PII values — that would defeat the purpose. It documents what was changed, how many times, and where, so the researcher can verify completeness.

### Step 6: Present results

After processing, show the user:
- How many files were processed
- How many PII instances were found per category
- The path to the anonymized folder
- Ask if they want to review any specific file to verify quality

## Detection guidance

PII detection in free-form text is nuanced. Here's how to approach tricky cases:

**Names:** Look for capitalized words in contexts that suggest they're names — introductions, speaker labels ("Interviewer: Hi, I'm talking to Anna today"), signatures, references to people. Be cautious with common words that could be names (e.g., "Grace" as a concept vs. a name). Use surrounding context to decide.

**Locations vs. general geography:** "Stockholm" in "I live in Stockholm" is PII. "Stockholm" in "Stockholm is the capital of Sweden" is general knowledge, not PII. Anonymize when the location is tied to an individual's identity.

**Job titles:** "I'm a senior designer at Spotify" — both the title and company are PII because together they could identify someone. "Designers often use Figma" is a general statement, not PII.

**Ages:** "I'm 34" or "she's in her mid-thirties" — anonymize specific ages. "Adults aged 25-40" as a demographic range in analysis is not PII.

**Ambiguous cases:** When unsure, err on the side of anonymizing. It's better to over-protect than to miss something. Flag ambiguous decisions in the log.

## Edge cases

- **Speaker labels:** If transcripts use real names as speaker labels (e.g., "Anna: I think..."), replace consistently with the placeholder: `[PERSON_1]: I think...`
- **Possessive forms:** "Anna's opinion" → `[PERSON_1]'s opinion`
- **Partial references:** If "Anna" and "Anna Svensson" both appear, treat them as the same person and use the same placeholder
- **Interviewer names:** The researcher's own name may appear — anonymize it too unless the user says otherwise
- **Non-Latin characters:** Handle names and addresses in any script
- **Multiple languages:** Transcripts may mix languages — detect PII regardless of language
- **Names in UI/system text:** If a transcript mentions a name appearing in software UI (e.g., "Welcome, Grace" on a screen), still anonymize it — it could be a real user's name displayed by the system. When in doubt, anonymize.

## Common Mistakes

- **Modifying originals**: Never edit the source files. Always write to the `anonymized/` subfolder.
- **Inconsistent placeholders**: "Anna" in file 1 and "Anna" in file 3 must both be `[PERSON_1]`. Build the registry across ALL files before writing.
- **Putting real PII in the log**: The anonymization log documents what was changed, NOT what the original values were.
- **Skipping the log under pressure**: The log is the audit trail for compliance — it's not optional.
- **Under-detecting PII**: When unsure, anonymize. Over-protection is better than a privacy breach. Flag ambiguous decisions in the log.
