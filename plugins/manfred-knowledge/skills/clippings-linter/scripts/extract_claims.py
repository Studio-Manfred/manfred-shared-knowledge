#!/usr/bin/env python3
"""
v2 pre-processor: extract claim candidates and cluster them by dominant tag.

This is the deterministic half of the v2 lint pipeline. It reads the Clippings
folder, finds sentences in each file's body that look like factual claims (with
numbers, dates, percentages, or absolute language), groups the files by their
primary tag, and writes a worklist JSON for downstream LLM-based processing.

The LLM work (finding contradictions within a cluster, checking staleness
against the web) is orchestrated by Claude via the SKILL.md instructions —
this script does not call any LLM or network itself.

Python 3 stdlib only.
"""

import argparse
import collections
import json
import os
import re
import sys
from datetime import datetime

# --- Claim extraction heuristics --------------------------------------------

# Any digit run, percentage, year
NUMERIC_RE = re.compile(r"\b(\d{1,3}(?:[.,]\d+)?%?|\d{4})\b")

# Absolute / universal language that tends to disagree across sources
ABSOLUTE_WORDS = {
    "always", "never", "only", "best", "worst", "most", "least",
    "all", "none", "every", "no one", "must", "cannot", "impossible",
    "the first", "the last", "the biggest", "the smallest",
}
ABSOLUTE_RE = re.compile(
    r"\b(" + "|".join(re.escape(w) for w in sorted(ABSOLUTE_WORDS, key=len, reverse=True)) + r")\b",
    re.IGNORECASE,
)

# Temporal markers that suggest a claim is making a "now" statement.
# These are PHRASE markers only — avoid matching "in 1871" / "since 1959" which
# are historical anchors, not stale claims.
STALE_MARKERS = [
    r"\b(currently|recently|right now|today|this year|last year|nowadays)\b",
    r"\b(the (new|latest|modern)|emerging|upcoming)\b",
    r"\b(state of the art|cutting edge|just released|brand new)\b",
]
STALE_RE = re.compile("|".join(STALE_MARKERS), re.IGNORECASE)
YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")

MAX_CLAIMS_PER_FILE = 5
MAX_FILES_PER_CLUSTER = 100
MAX_CLUSTERS = 5
MAX_STALE_CANDIDATES = 50
MIN_BODY_CHARS = 500  # skip stub files below this (noise filter)
STALE_RECENT_WINDOW_YEARS = 5  # years older than this are not interesting unless marker-flagged
CURRENT_YEAR = datetime.now().year


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end < 0:
        return None, text
    return text[3:end], text[end + 4:]


def extract_tags(fm):
    m = re.search(r'^tags:\s*\n((?:  - [^\n]*\n)*)', fm, re.M)
    if not m:
        return []
    return [t.strip() for t in re.findall(r'  - (\S[^\n]*)', m.group(1)) if t.strip()]


def clean_body(body):
    """Strip markdown noise so sentence splitting works on prose."""
    s = body
    s = re.sub(r"```.*?```", "", s, flags=re.S)       # code blocks
    s = re.sub(r"`[^`]*`", "", s)                     # inline code
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)        # images
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)    # links
    # Strip wiki-links ENTIRELY (including alias/title) — their contents often
    # include years like "(2026)" that would otherwise pollute year extraction.
    s = re.sub(r"\[\[[^\]]*\]\]", "", s)
    s = re.sub(r"^\s*#{1,6}\s+.*$", "", s, flags=re.M)  # headings
    s = re.sub(r"^\s*[-*]\s+", "", s, flags=re.M)     # bullets
    s = re.sub(r"^\s*>\s?", "", s, flags=re.M)        # blockquotes
    return s


def split_sentences(text):
    """Simple sentence splitter. Good enough for claim-level heuristics."""
    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()
    # Split on sentence terminators followed by space + capital or digit
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", text)
    return [p.strip() for p in parts if len(p.strip()) > 20]


def score_claim(sentence):
    """Return (score, reasons) — higher score = more claim-like."""
    score = 0
    reasons = []
    if NUMERIC_RE.search(sentence):
        score += 2
        reasons.append("numeric")
    if ABSOLUTE_RE.search(sentence):
        score += 2
        reasons.append("absolute")
    if YEAR_RE.search(sentence):
        score += 1
        reasons.append("year")
    if STALE_RE.search(sentence):
        score += 1
        reasons.append("temporal")
    return score, reasons


def pick_claims(body):
    """Return up to MAX_CLAIMS_PER_FILE ranked claims from the body."""
    cleaned = clean_body(body)
    scored = []
    for sent in split_sentences(cleaned):
        if len(sent) > 300:  # too long, probably joined paragraphs
            continue
        s, reasons = score_claim(sent)
        if s == 0:
            continue
        scored.append((s, sent, reasons))
    scored.sort(key=lambda x: -x[0])
    return [{"text": s[1], "reasons": s[2]} for s in scored[:MAX_CLAIMS_PER_FILE]]


def file_is_stale_candidate(claim_text):
    """Does this claim look like it might have gone stale?

    A claim is stale-suspect if EITHER:
      (a) it uses a temporal marker like "currently / recent / new / latest", OR
      (b) it references a year within the last few years AND the sentence
          reads like a current statement.
    Historical anchors (e.g. "founded in 1871") get dropped — they're fact,
    not staleness.
    """
    has_marker = bool(STALE_RE.search(claim_text))
    years = [int(y) for y in re.findall(r"\b(19\d{2}|20\d{2})\b", claim_text)]
    recent_year = (
        years
        and max(years) >= CURRENT_YEAR - STALE_RECENT_WINDOW_YEARS
    )
    return has_marker or recent_year


def build_worklist(root):
    files = sorted(f for f in os.listdir(root) if f.endswith(".md"))
    claims_by_file = {}
    tags_by_file = {}

    for f in files:
        try:
            text = open(os.path.join(root, f), errors="ignore").read()
        except Exception:
            continue
        fm, body = parse_frontmatter(text)
        if fm is None:
            continue
        tags = extract_tags(fm)
        if not tags:
            continue
        if len(body.strip()) < MIN_BODY_CHARS:
            continue  # skip stubs — boilerplate placeholders contaminate claim extraction
        claims = pick_claims(body)
        if not claims:
            continue
        claims_by_file[f] = claims
        tags_by_file[f] = tags

    # Cluster by primary tag (the first tag in the file's tag list)
    by_tag = collections.defaultdict(list)
    for f, tags in tags_by_file.items():
        by_tag[tags[0]].append(f)

    # Take the N biggest clusters
    top_clusters = sorted(by_tag.items(), key=lambda kv: -len(kv[1]))[:MAX_CLUSTERS]

    clusters_out = {}
    for tag, tag_files in top_clusters:
        picked = tag_files[:MAX_FILES_PER_CLUSTER]
        clusters_out[tag] = [
            {"file": f, "claims": claims_by_file[f]}
            for f in picked
        ]

    # Build stale-candidate list across ALL files, ranked by year (oldest first)
    stale = []
    for f, claims in claims_by_file.items():
        for c in claims:
            if file_is_stale_candidate(c["text"]):
                years = [int(y) for y in re.findall(r"\b(19\d{2}|20\d{2})\b", c["text"])]
                # Display the NEWEST year mentioned — that's what made the claim
                # suspect ("...in 2023"), not the oldest historical reference.
                year = max(years) if years else 0
                stale.append({
                    "file": f,
                    "claim": c["text"],
                    "year": year,
                    "reasons": c["reasons"],
                })
    # Sort oldest-first so the most-likely-stale surface at the top.
    stale.sort(key=lambda s: (s["year"], s["file"]))
    stale = stale[:MAX_STALE_CANDIDATES]

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "files_scanned": len(files),
        "files_with_claims": len(claims_by_file),
        "clusters": clusters_out,
        "stale_candidates": stale,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", required=True, help="Clippings folder to scan")
    ap.add_argument("--out", required=True, help="Path to write worklist JSON")
    args = ap.parse_args()

    if not os.path.isdir(args.path):
        print(f"error: not a directory: {args.path}", file=sys.stderr)
        return 2

    result = build_worklist(args.path)
    with open(args.out, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"files scanned:       {result['files_scanned']}")
    print(f"files with claims:   {result['files_with_claims']}")
    print(f"clusters (top {MAX_CLUSTERS}):")
    for tag, items in result["clusters"].items():
        total_claims = sum(len(i["claims"]) for i in items)
        print(f"  {tag:30s}  files={len(items):3d}  claims={total_claims}")
    print(f"stale candidates:    {len(result['stale_candidates'])}")
    print(f"worklist:            {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
