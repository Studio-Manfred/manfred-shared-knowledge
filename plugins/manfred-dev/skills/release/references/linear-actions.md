# Linear MCP — call patterns for releases

These are the Linear actions the `release` skill performs in step 12. Loaded only when actually updating Linear, to keep the SKILL.md body lean.

The MCP server is `linear-server`. At Manfred, the workspace slug is `studio-manfred` (https://linear.app/studio-manfred). Tickets are prefixed `STU-`.

**Server-level rule (from server instructions):** When passing string values to any tool, send content directly. Use **literal newlines and special characters, not escape sequences** (`\n`, `\t`). Markdown bodies must contain real newlines.

## Linear data model — read this first

Linear's terminology trips agents up. The `release` skill cares about three things:

| Linear concept | What it is | Tools |
|---|---|---|
| **Issue** (e.g., `STU-204`) | A single ticket. Has `state`, `assignee`, `project`, `cycle`, `parentId`. | `get_issue`, `save_issue`, `save_comment` |
| **Project** | A collection of related issues. **At Manfred, what people often call "the milestone" is actually a Linear Project.** Has its own description, lead, target date. | `get_project`, `save_project`, `list_projects` |
| **Milestone (project milestone)** | A checkpoint within a Project (different from Project itself). Has `name`, `targetDate`, `description`. | `get_milestone`, `save_milestone`, `list_milestones` |

When an issue has a `project` field populated, that's the Linear Project — usually what users mean when they talk about the "milestone the work belongs to". The `release` skill operates on the Project here, not on a project-milestone.

## 1. Resolve ticket IDs from commit history

The skill discovers ticket IDs in this order:

1. Scan commit subjects in `git log <last-tag>..HEAD` for `STU-\d+` matches.
2. Scan the current branch name for `STU-\d+`.
3. Deduplicate. Order by first appearance.
4. If empty, ask the user. Accept "skip Linear" without follow-up grumbling.

Treat `STU-123` and `stu-123` as the same — case-insensitive match, but always emit the canonical uppercase form.

## 2. Fetch ticket details (one read per ticket)

Before writing anything, read each ticket so the comment can reference its title and so project membership is known.

```
mcp__linear-server__get_issue({ query: "STU-204" })
```

The response contains `title`, `state` (current), `assignee`, `labels`, `project` (Linear Project the ticket belongs to), `cycle`, and the `team`. Cache locally; the skill reuses these for the comment body and the project note.

If a ticket ID doesn't resolve (typo, archived team), surface it and ask the user before continuing — don't silently drop it.

## 3. Comment with release notes — first action

Always comment **before** transitioning state. Reason: if the state-change tool errors out, the comment is still on the ticket as a record. The reverse leaves the ticket transitioned with no audit trail.

```
mcp__linear-server__save_comment({
  issueId: "STU-204",
  body: <literal-newline markdown — see template below>
})
```

### Comment template

The `body` string must contain real newlines, not `\n`:

```markdown
**Shipped in v1.5.0**

- Tag: https://github.com/Studio-Manfred/<repo>/releases/tag/v1.5.0
- Production: https://<vercel-prod-url>
- Changelog excerpt:
  - Added: profile avatar upload with crop preview (STU-204)
  - Fixed: oversized avatar image rejection (STU-204)
```

Notes:

- Always include the GitHub release URL, even when no GitHub Release object exists yet (link to the tag URL — `releases/tag/v1.5.0` works for tags too).
- Include the Vercel production URL only after step 10 returned `READY` for that deployment. Never include a preview URL or speculative URL.
- Scope the changelog excerpt to lines that mention this ticket. If no line mentions it but the ticket is in the release scope (e.g., a `chore:` commit closing a refactor ticket), include a one-line summary instead.

## 4. Transition state — second action

Ask the user **once per release** which state to transition all matched tickets to. Typical answers: "Done", "Shipped", "Released". Use `list_issue_statuses` to resolve the team's exact state name if needed:

```
mcp__linear-server__list_issue_statuses({ team: "Studio Manfred" })
mcp__linear-server__save_issue({ id: "STU-204", state: "Done" })
```

`save_issue` accepts either the issue ID (the UUID returned in `get_issue`) or the identifier (`STU-204`) — prefer the identifier for readability.

Apply the same target state to every matched ticket in the release. Do not transition tickets that aren't in the matched set.

If the user says "leave the ticket alone" or "I'll move it manually", honor that — log the comment, skip the state change, note it in the final summary.

## 5. Project note — third action (when applicable)

When `get_issue` from step 2 returned a `project` field, append a release line to that project's description. Don't overwrite — read the current description, append, write back.

```
project = mcp__linear-server__get_project({ query: "<project-id-or-name>" })
new_description = project.description + "\n\nShipped in v1.5.0:\n- STU-204: profile avatar upload\n- STU-218: avatar moderation hook\n"
mcp__linear-server__save_project({ id: project.id, description: new_description })
```

(Use literal newlines in the actual call, not `\n`.)

If multiple matched tickets share the same project, batch into one note rather than one note per ticket.

**Why no auto-close on projects:** they almost always have siblings still in flight (analytics work, mobile parity, follow-up bugs). The project owner decides when it's done. The skill provides the audit trail; the human makes the call.

If `save_project` errors (permissions, project archived), skip silently. The project note is a nicety; the comment + state change on the ticket is the gate.

## 6. Final summary to the user

After all Linear actions complete, surface a one-block summary of what was touched:

```
Linear updates for v1.5.0:
- STU-204 → Done (commented, transitioned)
- STU-218 → Done (commented, transitioned)
- Project "Avatar upload" → release line appended to description (not closed; STU-225 still open)
- STU-241 (mentioned in commit but archived) → skipped, asked user
```

This is the audit trail the user will rely on three months later when someone asks "what shipped in v1.5.0?".

## Failure modes

- **`save_issue` returns an unknown-state error:** the team's workflow doesn't include the requested state name. List available states via `mcp__linear-server__list_issue_statuses({ team: "..." })`, ask the user to pick.
- **Network/auth error mid-run:** finish what you can, then surface "comment posted on STU-204 but state transition failed — please check". Do not silently retry indefinitely.
- **Linear MCP genuinely unavailable** (rare): print a manual checklist with the comment body, target state, and project line. Tell the user to paste manually. Never claim "Linear updated" without the actual tool calls.
