---
name: markitdown-convert
description: Use when the user wants to batch-convert documents in a folder to Markdown using markitdown — PDFs, Word docs, PowerPoints, Excel files, HTML, images, audio, EPub, CSV/JSON/XML, and more. Triggers on "convert these PDFs to markdown", "run markitdown on this folder", "turn these docs into .md files", "markitdown the clippings folder", or any phrasing about batch-converting documents to markdown. Use even when the user only names one format (e.g., "convert all the PDFs") — the skill handles mixed batches too.
---

# markitdown-convert

Batch-converts files in a folder to Markdown using the `markitdown` CLI, writing each `.md` next to its source. Designed for folders of clippings, downloads, research material, meeting exports — anywhere you have a pile of mixed document formats you want as plain markdown.

## When to use

Trigger when the user wants to convert one or more documents in a folder to `.md`. Common phrasings:

- "convert these PDFs to markdown"
- "run markitdown on this folder"
- "turn my downloads into .md files"
- "markitdown the clippings"

If the user points at a single file, this skill is overkill — just run `markitdown <file> -o <file>.md` directly. Use the skill when there are multiple files or when the folder contents are mixed/unknown.

## Prerequisites

Check once at the start:

```bash
markitdown --version
```

If it's missing, tell the user and suggest `pip install markitdown[all]` or `pipx install 'markitdown[all]'`. Don't try to install it silently.

## Supported formats

markitdown converts (non-exhaustive): `.pdf`, `.docx`, `.pptx`, `.xlsx`, `.xls`, `.html`, `.htm`, `.csv`, `.json`, `.xml`, `.epub`, `.zip`, `.txt`, `.md`, and many image/audio formats. When scanning a folder, match on extension (case-insensitive) and skip anything that isn't recognizably convertible.

## Workflow

### 1. Resolve the target folder

The user usually names the folder loosely ("the State of Design folder", "my downloads"). Before doing anything:

- If the path they gave resolves cleanly, use it.
- Otherwise, search likely roots (`~/Sandbox/Obsidian`, `~/Downloads`, `~/Documents`, cwd) with `find <root> -type d -iname "*<hint>*"` to locate it.
- If multiple candidates match, list them and ask which one. Don't guess on ambiguous matches — converting the wrong folder wastes the user's time.

### 2. Inventory the files

List convertible files in the folder (non-recursive by default — recurse only if the user asks or the folder is clearly organized into subfolders of documents). Show the count and a few example names before running anything substantial:

> "Found 18 PDFs and 3 DOCX files in `<folder>`. I'll convert each to `.md` saved alongside the source. Proceed?"

For small batches (say, under ~5 files) you can skip the confirmation and just run it. Use judgment — the point is to avoid surprising the user with a big operation, not to slow down small ones.

### 3. Determine the output filename

For each source file `foo.pdf`, the default output is `foo.md` in the same folder. **Never overwrite an existing file.** If `foo.md` already exists, use `foo-1.md`; if that exists, `foo-2.md`; and so on. This matters because the user may have hand-written notes in an existing `.md` with the same stem — silently clobbering them would be a serious loss.

### 4. Convert

Run markitdown per-file. A simple shell loop is fine:

```bash
cd "<folder>"
for f in *.pdf *.docx *.pptx *.xlsx *.html *.epub; do
  [ -f "$f" ] || continue
  out="${f%.*}.md"
  # collision check: bump suffix until free
  i=1
  while [ -e "$out" ]; do
    out="${f%.*}-$i.md"
    i=$((i+1))
  done
  markitdown "$f" -o "$out" 2>&1 | tail -3
done
```

Adjust the glob list to match what you actually found in step 2 — don't run globs for extensions that aren't present, it'll just produce noise.

**About warnings:** pdfminer often prints things like `Could not get FontBBox from font descriptor` to stderr. These are cosmetic and don't affect text extraction. Mention them only if a conversion actually fails (empty output, non-zero exit code).

**About large batches:** If there are many files (20+) or big PDFs, the loop can take a while. Use a long Bash timeout (e.g. 10 min) rather than splitting into chunks — markitdown runs are independent and failures don't cascade, so a single pass is simplest.

### 5. Verify and report

After the loop, confirm each source got an output:

```bash
cd "<folder>" && for f in *.pdf *.docx *.pptx *.xlsx *.html *.epub; do
  [ -f "$f" ] || continue
  stem="${f%.*}"
  ls "$stem".md "$stem"-*.md 2>/dev/null | head -1 > /dev/null || echo "MISSING: $f"
done
```

Report briefly: how many converted, where they are, and any skipped/failed files with the reason. Don't dump the full file list unless the user asks — they can see the folder themselves.

## Why these choices

- **Same folder as source**: keeps the markdown paired with the original. Obsidian, git, and the user's own mental model all benefit from co-location.
- **New name on collision, never overwrite**: the user's existing notes are sacred. A stale `.md` from a previous run is easy to delete; lost hand-written content is not.
- **Non-recursive default**: recursion surprises people. "Convert this folder" usually means the files they can see, not a whole tree. Recurse only when asked.
- **Per-file loop, not one big call**: markitdown's CLI takes one file at a time. A loop is the honest primitive; don't pretend otherwise with a wrapper script.
- **Confirm before big batches, not small ones**: the confirmation exists to prevent surprise, not ceremony. Match the friction to the stakes.

## Edge cases

- **Password-protected PDFs**: markitdown will fail. Note the file, continue the batch, report at the end.
- **Scanned/image-only PDFs**: markitdown returns empty or near-empty markdown. Don't silently produce empty files — check output size; if a result is under ~100 bytes, flag it so the user knows OCR would be needed.
- **Files with unusual characters in names** (`·`, `—`, spaces): always quote paths. The shell loop above handles this with `"$f"`.
- **ZIPs and EPubs**: markitdown handles these natively — just treat them like any other format. Don't extract first.
- **`.md` sources**: markitdown can "convert" these (passthrough-ish). Skip them by default — no point rewriting existing markdown, and it risks collisions with the source itself.
