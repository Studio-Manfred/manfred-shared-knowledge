#!/usr/bin/env python3
"""
Clippings linter — v1.

Scans an Obsidian Clippings folder for structural and graph-level issues,
applies safe auto-fixes, and writes a markdown report.

No external dependencies — Python 3 stdlib only.
"""

import argparse
import os
import re
import sys
import collections
from datetime import datetime


HARD_REQUIRED = ["title", "url", "source", "tags"]
SOFT_REQUIRED = ["created", "read_status"]
SMART_QUOTES = "\u201c\u201d\u2018\u2019"
STUB_BODY_CHARS = 50
FILENAME_MAX_LEN = 80

# Trailing clipping-tool artifacts seen in the vault (case-insensitive, whole-word)
FILENAME_ARTIFACT_PATTERNS = [
    r" Medium$", r" Bootcamp$", r" UX Collective$", r" Substack$",
    r" Towards Data Science$", r" Scribe$", r" LinkedIn$",
    r" YouTube$", r" Hacker News$", r" Reddit$",
    r" by [A-Z][a-zA-Z.\-]+ ?[A-Z]?[a-zA-Z.\-]*$",  # "... by Brian Solis"
]

# Words that look like sentence fragments at the end of a truncated title
TRUNCATION_ENDWORDS = {
    "through", "and", "but", "or", "for", "the", "a", "an", "to", "of",
    "in", "on", "at", "with", "from", "by", "as", "that", "which",
    "these", "those", "this", "their", "our", "your", "my", "his", "her",
    "is", "was", "are", "were", "be", "been", "being", "will", "would",
    "could", "should", "may", "might", "can",
}
DEFAULT_CANDIDATE_THRESHOLD = 5
MIN_TAGS = 2
MAX_TAGS = 4
STOPWORDS = {
    "The","A","An","And","Or","But","For","Of","In","On","At","To","From",
    "By","With","As","Is","Are","Was","Were","Be","Been","This","That",
    "These","Those","It","Its","I","You","We","They","He","She","Will",
    "Can","May","Your","My","Our","Their","His","Her","Not","No","Yes",
    "Do","Does","Did","Have","Has","Had","Get","Got","Make","Made",
    "New","Old","Good","Bad","Big","Small","Best","More","Most","Less",
    "Here","There","When","Where","What","Why","How","Who","Which",
    "If","So","Just","Only","Also","Now","Then","Still","All","Some",
    "Any","Every","Each","Many","Much","Few","One","Two","Three",
}


def parse_frontmatter(text):
    """Return (fm_str, body_str) or (None, text) if no frontmatter."""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end < 0:
        return None, text
    return text[3:end], text[end + 4:]


def strip_quotes(val):
    """Strip surrounding ASCII or smart quotes."""
    v = val.strip()
    for q in ('"', "'", "\u201c", "\u201d", "\u2018", "\u2019"):
        if v.startswith(q): v = v[1:]
        if v.endswith(q): v = v[:-1]
    return v


def parse_fm_fields(fm):
    """Parse simple YAML-ish frontmatter into a dict.

    Handles scalars and list-block fields (tags, related). Not a full YAML
    parser but robust for the Clippings schema.
    """
    fields = {}
    lines = fm.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^([a-zA-Z_][a-zA-Z0-9_]*):\s*(.*)$', line)
        if not m:
            i += 1
            continue
        key, val = m.group(1), m.group(2).rstrip()
        # list block?
        if val == "":
            items = []
            j = i + 1
            while j < len(lines) and lines[j].startswith("  - "):
                items.append(lines[j][4:].strip().strip('"').strip("'").strip("\u201c").strip("\u201d"))
                j += 1
            if items or (j > i + 1):
                fields[key] = items
                i = j
                continue
            fields[key] = ""
            i += 1
            continue
        # inline list
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            if not inner:
                fields[key] = []
            else:
                fields[key] = [x.strip().strip('"').strip("'").strip("\u201c").strip("\u201d") for x in inner.split(",")]
            i += 1
            continue
        fields[key] = val.strip().strip('"').strip("'").strip("\u201c").strip("\u201d")
        i += 1
    return fields


def count_prose_chars(body):
    """Rough estimate of body content, stripping markdown syntax and links."""
    s = body
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', s)      # images
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)  # links
    s = re.sub(r'`[^`]*`', '', s)                   # inline code
    s = re.sub(r'```.*?```', '', s, flags=re.S)     # code blocks
    s = re.sub(r'[#>*_\-]', '', s)                  # markdown markers
    s = re.sub(r'\s+', ' ', s).strip()
    return len(s)


def extract_wiki_links(text):
    """Extract [[target]] links, ignoring display aliases."""
    out = set()
    for m in re.finditer(r'\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]', text):
        out.add(m.group(1).strip())
    return out


def extract_noun_phrases(text):
    """Extract capitalised multi-word phrases as article-candidate seeds.

    Heuristic: 2-4 consecutive Title-Case words, skipping stopwords and
    phrases that are purely stopwords.
    """
    phrases = set()
    for m in re.finditer(r'\b((?:[A-Z][a-zA-Z0-9]+(?:\s+|-))+[A-Z][a-zA-Z0-9]+)\b', text):
        phrase = m.group(1).strip()
        words = re.split(r'[\s-]+', phrase)
        if not (2 <= len(words) <= 4):
            continue
        if all(w in STOPWORDS for w in words):
            continue
        phrases.add(phrase)
    return phrases


def slug(s):
    return re.sub(r'\s+', '', s.lower())


class Issue:
    __slots__ = ("severity", "kind", "file", "detail", "fix")

    def __init__(self, severity, kind, file, detail, fix=None):
        self.severity = severity
        self.kind = kind
        self.file = file
        self.detail = detail
        self.fix = fix


def auto_fix_frontmatter(path, fm, body, fields):
    """Apply safe in-place fixes. Returns list of fix descriptions applied."""
    fixes = []
    new_fm = fm
    new_body = body
    missing_defaults = {
        "read_status": "saved",
        "type": "article",
    }
    for key, default in missing_defaults.items():
        if key not in fields:
            new_fm = new_fm.rstrip() + f"\n{key}: {default}\n"
            fixes.append(f"added `{key}: {default}`")

    # fix URLs with smart quotes or needing straight quotes
    url_line_re = re.compile(r'^(url):\s*(.+)$', re.M)
    m = url_line_re.search(new_fm)
    if m:
        val = m.group(2).strip()
        has_smart = any(q in val for q in SMART_QUOTES)
        bare = val
        for q in list(SMART_QUOTES) + ['"', "'"]:
            bare = bare.replace(q, "")
        bare = bare.strip()
        needs_quotes = ('?' in bare or '&' in bare or '#' in bare)
        already_straight = val.startswith('"') and val.endswith('"') and not has_smart
        if (has_smart or needs_quotes) and not already_straight:
            new_fm = url_line_re.sub(f'url: "{bare}"', new_fm, count=1)
            fixes.append("fixed url quoting")

    # Normalise smart-quote DELIMITERS in frontmatter values (not interior chars).
    # A smart quote at the very start/end of a value is a broken YAML delimiter.
    def normalize_delim(match):
        key = match.group(1)
        val = match.group(2).rstrip()
        open_smart = val.startswith("\u201c") or val.startswith("\u2018")
        close_smart = val.endswith("\u201d") or val.endswith("\u2019")
        if not (open_smart or close_smart):
            return match.group(0)
        inner = val
        if open_smart: inner = inner[1:]
        if close_smart: inner = inner[:-1]
        return f"{key}: \"{inner}\""
    delim_re = re.compile(r'^([a-zA-Z_][\w]*):\s+(.+)$', re.M)
    before = new_fm
    new_fm = delim_re.sub(normalize_delim, new_fm)
    if new_fm != before:
        fixes.append("normalised smart-quote delimiters")

    # Ensure blank line after closing `---`. body starts with '\n' followed by content.
    if new_body.startswith("\n") and not new_body.startswith("\n\n"):
        new_body = "\n" + new_body
        fixes.append("added blank line after frontmatter")

    if new_fm != fm or new_body != body:
        new_text = "---" + new_fm + ("" if new_fm.endswith("\n") else "\n") + "---" + new_body
        with open(path, "w") as f:
            f.write(new_text)
    return fixes


def scan(path, auto_fix, candidate_threshold):
    files = sorted(f for f in os.listdir(path) if f.endswith(".md"))
    issues = []
    autofixes = collections.defaultdict(list)

    # First pass: parse everything, collect structure
    parsed = {}  # filename -> (fields, body)
    outgoing_links = collections.defaultdict(set)
    filename_index = {slug(f[:-3]): f for f in files}
    phrase_counts = collections.Counter()
    phrase_files = collections.defaultdict(set)

    for f in files:
        p = os.path.join(path, f)
        try:
            text = open(p, errors='ignore').read()
        except Exception as e:
            issues.append(Issue("error", "read_failed", f, str(e)))
            continue
        fm, body = parse_frontmatter(text)
        if fm is None:
            issues.append(Issue("error", "no_frontmatter", f, "file has no frontmatter block"))
            parsed[f] = ({}, body)
            continue
        fields = parse_fm_fields(fm)
        parsed[f] = (fields, body)

        # Content style checks (done on original text, before auto-fix)
        if not auto_fix:
            # curly-quote delimiters in frontmatter values
            if re.search(r':\s+[\u201c\u2018]', fm) or re.search(r'[\u201d\u2019]\s*$', fm, re.M):
                issues.append(Issue("warn", "curly_quote_delim", f, "frontmatter uses smart quotes as delimiters"))
            # missing blank line after `---`
            if body.startswith("\n") and not body.startswith("\n\n"):
                issues.append(Issue("info", "no_blank_after_fm", f, "body starts immediately after `---`"))

        # outgoing wiki-links
        rel = fields.get("related") or []
        if isinstance(rel, list):
            for r in rel:
                if r:
                    outgoing_links[f].add(r.lstrip("[").rstrip("]"))
        body_links = extract_wiki_links(body)
        outgoing_links[f] |= body_links

        # phrase extraction (only from body, not frontmatter)
        for phrase in extract_noun_phrases(body):
            phrase_counts[phrase] += 1
            phrase_files[phrase].add(f)

        # auto-fix pass (in-place)
        if auto_fix:
            fixes = auto_fix_frontmatter(p, fm, body, fields)
            if fixes:
                autofixes[f].extend(fixes)
                # re-parse after fix
                text = open(p, errors='ignore').read()
                fm2, body2 = parse_frontmatter(text)
                if fm2 is not None:
                    parsed[f] = (parse_fm_fields(fm2), body2)

    # Second pass: checks
    incoming_links = collections.defaultdict(set)
    for src, targets in outgoing_links.items():
        for t in targets:
            tf = filename_index.get(slug(t))
            if tf:
                incoming_links[tf].add(src)

    for f in files:
        fields, body = parsed[f]
        if not fields:
            continue

        # Schema errors (hard required)
        for field in HARD_REQUIRED:
            if field not in fields:
                issues.append(Issue("error", "missing_required", f, f"missing required field `{field}`"))
            elif fields[field] in ("", [], None):
                issues.append(Issue("error", "empty_required", f, f"required field `{field}` is empty"))
        # Schema info (soft required — historical gaps, shown as counts only)
        for field in SOFT_REQUIRED:
            if field not in fields or fields[field] in ("", [], None):
                issues.append(Issue("info", "missing_optional", f, f"missing recommended field `{field}`"))

        # Tags
        tags = fields.get("tags") or []
        if isinstance(tags, list):
            if tags == ["to-categorize"]:
                issues.append(Issue("warn", "placeholder_tags", f, "tags contain only placeholder `to-categorize`"))
            elif not tags:
                issues.append(Issue("warn", "no_tags", f, "tags block is empty"))
            elif len(tags) < MIN_TAGS:
                issues.append(Issue("warn", "too_few_tags", f, f"only {len(tags)} tag(s), expected ≥{MIN_TAGS}"))
            elif len(tags) > MAX_TAGS:
                issues.append(Issue("info", "too_many_tags", f, f"{len(tags)} tags, expected ≤{MAX_TAGS}"))

        # Empty body
        prose = count_prose_chars(body)
        if prose < STUB_BODY_CHARS:
            issues.append(Issue("warn", "stub_body", f, f"body has only {prose} chars of prose"))

        # URL malformed
        url = fields.get("url", "")
        if url and not re.match(r'^https?://', str(url).strip().strip('"')):
            issues.append(Issue("error", "bad_url", f, f"url does not start with http(s)://: {url[:60]}"))

    # Filename checks
    dupe_base = collections.defaultdict(list)
    artifact_re = re.compile("|".join(FILENAME_ARTIFACT_PATTERNS), re.IGNORECASE)
    for f in files:
        name = f[:-3]
        # " 1", " 2" suffix detection
        m = re.match(r'^(.*?) (\d+)$', name)
        if m:
            base = m.group(1)
            dupe_base[base].append(f)
        if re.match(r'^Untitled(\s\d+)?$', name):
            issues.append(Issue("warn", "generic_filename", f, "generic filename (`Untitled`)"))
        if '%' in name:
            issues.append(Issue("warn", "encoded_filename", f, "filename contains URL-encoded chars"))
        # Style: too long
        if len(name) > FILENAME_MAX_LEN:
            issues.append(Issue("info", "filename_too_long", f, f"{len(name)} chars (>{FILENAME_MAX_LEN})"))
        # Style: trailing clipping artifact
        if artifact_re.search(name):
            m2 = artifact_re.search(name)
            issues.append(Issue("warn", "filename_trailing_artifact", f, f"trailing clipping artifact: `{m2.group(0).strip()}`"))
        # Style: truncated mid-sentence (ends on a stopword/connector)
        last = name.rstrip(".… ").split()[-1].lower() if name.strip() else ""
        if last in TRUNCATION_ENDWORDS:
            issues.append(Issue("warn", "filename_truncated", f, f"ends mid-sentence: `…{last}`"))
        # Style: leading number with no context
        if re.match(r'^\d{2,}\s*[-–—:.]?\s+[A-Z]', name):
            issues.append(Issue("info", "filename_leading_number", f, "starts with opaque number prefix"))

    # Duplicate groups: base without suffix + any suffixed siblings
    for base, suffixed in dupe_base.items():
        base_file = base + ".md"
        group = []
        if base_file in parsed:
            group.append(base_file)
        group.extend(suffixed)
        if len(group) >= 2:
            for f in group:
                issues.append(Issue("warn", "duplicate", f, f"duplicate group: {', '.join(group)}"))

    # Orphan detection
    for f in files:
        fields, _ = parsed[f]
        if not fields:
            continue
        has_outgoing = bool(outgoing_links.get(f))
        has_incoming = bool(incoming_links.get(f))
        if not has_outgoing and not has_incoming:
            issues.append(Issue("info", "orphan", f, "no outgoing or incoming wiki-links"))

    # Article candidates: phrases appearing in ≥threshold files but with no matching page
    candidates = []
    for phrase, count in phrase_counts.items():
        file_count = len(phrase_files[phrase])
        if file_count < candidate_threshold:
            continue
        if slug(phrase) in filename_index:
            continue
        candidates.append((phrase, file_count))
    candidates.sort(key=lambda x: -x[1])

    return {
        "files_scanned": len(files),
        "issues": issues,
        "autofixes": dict(autofixes),
        "candidates": candidates[:50],
    }


def write_report(result, report_path):
    files_scanned = result["files_scanned"]
    issues = result["issues"]
    autofixes = result["autofixes"]
    candidates = result["candidates"]

    by_sev = collections.defaultdict(list)
    for i in issues:
        by_sev[i.severity].append(i)

    lines = []
    lines.append(f"# Clippings lint report — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append(f"**Scanned:** {files_scanned} files")
    lines.append(f"**Auto-fixes applied:** {sum(len(v) for v in autofixes.values())} across {len(autofixes)} file(s)")
    lines.append(f"**Issues requiring review:** {len(issues)}")
    lines.append("")

    lines.append("## Summary")
    lines.append("")
    lines.append("| Severity | Kind | Count |")
    lines.append("|---|---|---|")
    for sev in ("error", "warn", "info"):
        for kind in sorted(set(i.kind for i in by_sev[sev])):
            count = sum(1 for i in by_sev[sev] if i.kind == kind)
            emoji = {"error": "🔴", "warn": "🟡", "info": "🔵"}[sev]
            lines.append(f"| {emoji} {sev} | {kind} | {count} |")
    lines.append("")

    def file_link(f):
        return f"[[{f[:-3]}]]"

    for sev, emoji, title in (
        ("error", "🔴", "Errors"),
        ("warn", "🟡", "Warnings"),
        ("info", "🔵", "Suggestions"),
    ):
        if not by_sev[sev]:
            continue
        lines.append(f"## {emoji} {title}")
        lines.append("")
        # group by kind
        kinds = sorted(set(i.kind for i in by_sev[sev]))
        for kind in kinds:
            kind_issues = [i for i in by_sev[sev] if i.kind == kind]
            lines.append(f"### {kind} ({len(kind_issues)})")
            lines.append("")
            for issue in kind_issues[:200]:
                lines.append(f"- {file_link(issue.file)} — {issue.detail}")
            if len(kind_issues) > 200:
                lines.append(f"- *…and {len(kind_issues) - 200} more*")
            lines.append("")

    if candidates:
        lines.append("## 🔵 Article candidates")
        lines.append("")
        lines.append("Capitalised phrases appearing across many files with no dedicated page — potential gaps in coverage.")
        lines.append("")
        lines.append("| Phrase | Files |")
        lines.append("|---|---|")
        for phrase, count in candidates:
            lines.append(f"| {phrase} | {count} |")
        lines.append("")

    if autofixes:
        lines.append("## Auto-fixes applied")
        lines.append("")
        for f, fxs in sorted(autofixes.items()):
            lines.append(f"- {file_link(f)} — {'; '.join(fxs)}")
        lines.append("")

    with open(report_path, "w") as f:
        f.write("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", required=True)
    ap.add_argument("--auto-fix", action="store_true")
    ap.add_argument("--report", default=None)
    ap.add_argument("--candidates-threshold", type=int, default=DEFAULT_CANDIDATE_THRESHOLD)
    args = ap.parse_args()

    if not os.path.isdir(args.path):
        print(f"error: not a directory: {args.path}", file=sys.stderr)
        return 2

    report_path = args.report or os.path.join(args.path, "lint_report.md")

    result = scan(args.path, args.auto_fix, args.candidates_threshold)
    write_report(result, report_path)

    issues = result["issues"]
    by_sev = collections.Counter(i.severity for i in issues)
    by_kind = collections.Counter(i.kind for i in issues)  # noqa: used below
    print(f"scanned: {result['files_scanned']} files")
    print(f"errors:  {by_sev.get('error', 0)}")
    print(f"warns:   {by_sev.get('warn', 0)}")
    print(f"infos:   {by_sev.get('info', 0)}")
    print(f"auto-fixes: {sum(len(v) for v in result['autofixes'].values())} across {len(result['autofixes'])} file(s)")
    print(f"article candidates: {len(result['candidates'])}")
    print(f"top kinds: {', '.join(f'{k}={v}' for k, v in by_kind.most_common(6))}")
    print(f"report: {report_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
