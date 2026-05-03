---
description: Convert hardcoded values (hex literals, default Tailwind palette colours, var() refs to non-existent tokens) into Manfred design tokens. Surfaces missing tokens; refuses to invent.
argument-hint: [path or scope, e.g. "src/components/billing" or "the EmptyState component"]
---

You're tokenising hardcoded values in a Manfred app. The user mentioned: $ARGUMENTS

## Step 1 — Scope

Ask:

- What's the scope? (One file, one feature directory, the whole project?)
- Is this part of a larger refactor or a one-off cleanup?
- Linear ticket? (For posting results.)

If unclear, default to the file the user has open or most recently edited.

## Step 2 — Survey the token surface

Before changing anything, confirm what tokens are available:

```bash
test -f ~/.claude/shared/DESIGN.md && head -200 ~/.claude/shared/DESIGN.md
test -f src/tokens/tokens.css && cat src/tokens/tokens.css
```

This is the constraint — every replacement must resolve to an existing token (or be flagged as needing a new one).

## Step 3 — Find violations

Run three scans across the scope:

### Hex literals

```bash
grep -rn "#[0-9a-fA-F]\{3,6\}" <scope>
```

Filter out: SVG `fill`/`stroke` in icon files (those have their own tokenisation pattern), comment-only lines, generated files.

### Default Tailwind palette

```bash
grep -rn "\(bg\|text\|border\|ring\|fill\|stroke\)-\(red\|green\|blue\|amber\|yellow\|orange\|slate\|gray\|zinc\|stone\|neutral\)-[0-9]" <scope>
```

These bypass Manfred's token layer even though they look like utilities.

### Phantom tokens

```bash
# Find var() refs, then check each name against tokens.css
grep -rn "var(--[a-z-]\+)" <scope> | awk -F'var(' '{print $2}' | awk -F')' '{print $1}' | sort -u
```

For each name found, verify it exists in `tokens.css`. Anything that doesn't exist is rendering as the browser fallback (often `unset` or `inherit`) — silently broken.

## Step 4 — Map each violation to a fix

For each finding, decide:

| Violation | Fix |
|---|---|
| Hex literal that maps to an existing semantic | Replace with the semantic Tailwind utility or `hsl(var(--token))` |
| Hex literal that's actually brand-literal (logo plate, hero) | Replace with the brand utility (`bg-business-blue`) |
| Default Tailwind palette where a semantic exists | Replace with the semantic (`bg-card`, `text-foreground`, etc.) |
| Default Tailwind palette where no semantic exists (e.g. `bg-green-50` for a success state) | **Stop.** Run `manfred-design-systems:design-token` decision: (a) add semantic token, (b) reuse existing semantic like `--accent`, (c) neutral surface + icon. Don't auto-replace. |
| Phantom token (`var(--color-success)` that doesn't exist) | Same as above — the reference is just as broken as a hex. Resolve via `manfred-design-systems:design-token`. |

The skill (`manfred-design-systems:design-token`) handles the (a)/(b)/(c) menu. Surface the choice to the user — don't pick for them.

## Step 5 — Apply the fixes

For each clear-cut replacement (hex → existing semantic), make the edit. For each ambiguous case (no existing semantic), batch them into a list and present to the user before touching code.

Show the user:

```markdown
## Auto-replaceable (N findings)
[file:line] `#1e1e24` → `text-foreground` (semantic)
[file:line] `#ffffff` → `bg-background` (semantic)
[file:line] `bg-business-blue` → kept (brand-literal, intentional)

## Needs decision (N findings)
[file:line] `bg-green-50` for success state — pick:
  (a) Add `--color-success` to tokens.css
  (b) Reuse `bg-accent`
  (c) Use `bg-muted` + check icon
[file:line] `var(--color-warning)` — phantom token, same options as above
```

Wait for the user's pick on the "needs decision" items before applying. Don't invent.

## Step 6 — Verify dark mode

Once replacements are in: build (or run dev), toggle `.dark`, walk the changed surfaces. Confirm:

- Replaced colours flip correctly (semantic tokens) or stay literal (brand utilities) as intended
- No contrast regressions
- No "white text on white" or "black on black" breakages

If dark mode breaks: a brand utility was used where semantic was needed. Revisit those calls.

## Step 7 — Run the a11y gate

```
manfred-design-systems:a11y-qa
```

Tokenisation can change colour contrast — verify no new violations.

## Step 8 — Commit + Linear update

Conventional commit:

```
refactor(tokens): replace hardcoded values in <scope> with semantic tokens

- N hex literals replaced
- N default Tailwind palette colours replaced
- N phantom tokens resolved (added to semantic layer | reused existing | swapped to neutral+icon)
- Dark mode verified
- a11y-qa: 0 new findings
```

If a Linear ticket is in scope, post the summary as a comment.

## Wrap-up

Tell the user:

- Total replacements made
- Any "needs decision" items still open (and what the resolution was)
- Whether new tokens were added (and to which file)
- Dark-mode + a11y verification result

If new semantic tokens were added: remind the user that the design system itself (`Studio-Manfred/manfred-design_system`) probably wants them upstream too — open a follow-up issue.

If zero violations were found in the scope: say so plainly. Tokenisation often surfaces gnarly inherited code; sometimes the gnarl isn't there.
