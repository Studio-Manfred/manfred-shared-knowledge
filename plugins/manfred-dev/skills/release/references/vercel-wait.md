# Vercel MCP — waiting for the deploy to go green

These are the Vercel actions the `release` skill performs in step 10. Loaded only when actually waiting for a Vercel deploy.

The MCP server tools are namespaced `mcp__claude_ai_Vercel__*`. At Manfred, the team slug is `studio-manfred` (dashboard: https://vercel.com/studio-manfred).

## 1. Resolve `teamId` and `projectId` once

Both arguments are required for `list_deployments` and `get_deployment`. Resolve them in this order:

1. Read `.vercel/project.json` if the project has been linked locally — it contains `orgId` (= teamId) and `projectId`.
2. Else: `mcp__claude_ai_Vercel__list_teams` and find the entry with slug `studio-manfred` → `id` is the `teamId`.
3. Then `mcp__claude_ai_Vercel__list_projects` (with that `teamId`) and match by repo name → `id` is the `projectId`.

Cache the values in local working memory for the rest of the release. Don't re-resolve on every poll.

## 2. Find the deployment for the just-pushed commit

Right after `git push`, capture the `HEAD` SHA of the local branch. Then:

```
mcp__claude_ai_Vercel__list_deployments({
  teamId: "<teamId>",
  projectId: "<projectId>",
  since: <unix-ms-30s-before-push>
})
```

Match by the commit SHA. The deployment's `meta.githubCommitSha` (or equivalent) should equal the local `HEAD` SHA. If multiple deployments match the same SHA (re-deploys, build retries), take the most recent.

If no deployment shows up within ~30 seconds of the push, the GitHub-Vercel integration may be misconfigured. Surface this to the user — don't silently spin.

## 3. Poll until terminal state

```
mcp__claude_ai_Vercel__get_deployment({
  teamId: "<teamId>",
  idOrUrl: "<deployment-id-or-hostname>"
})
```

Poll every 10 seconds. Default ceiling: 10 minutes (60 polls). Tunable via the `VERCEL_WAIT_TIMEOUT_SEC` env var if the project has slow builds.

States to handle:

| State | Action |
|---|---|
| `QUEUED` | Continue polling. |
| `BUILDING` | Continue polling. |
| `INITIALIZING` | Continue polling. |
| `READY` | **Pass.** Capture `url` (preview URL) and `aliasAssigned`/`alias` (production URL) for the Linear comment. |
| `ERROR` | **Fail.** Fetch build logs (see below). Surface to user. Stop the release workflow. |
| `CANCELED` | Ask the user. Likely superseded by a newer push. Ask whether to point at the new deployment or stop. |

On timeout (no terminal state in 10 minutes): tell the user the deploy is taking longer than expected. Offer: continue waiting, switch to manual ("I'll watch the dashboard, tell me when it's green"), or abort.

## 4. On `ERROR` — fetch and surface logs

```
mcp__claude_ai_Vercel__get_deployment_build_logs({
  teamId: "<teamId>",
  idOrUrl: "<deployment-id>",
  limit: 200
})
```

Surface the last ~50 lines (or whatever shows the actual failure — search for `ERROR`, `Failed`, `error TS`, `npm ERR!`). Don't dump 200 lines into the conversation.

Then **stop**. Do not proceed to step 11 (tag) or step 12 (Linear). The commit is on `main`, but the release is not done. The user decides whether to:

- Fix-forward (push another commit, wait for that deploy)
- Revert (`git revert <sha>; git push origin main`)
- Override (push the tag anyway with explicit "I know Vercel failed" — the skill should require typing the literal phrase to be sure)

## 5. Handing off the production URL

When the deploy reaches `READY`, capture the production URL — the one users will see, not the unique deployment URL.

Vercel's deployment object surfaces this in `aliasAssigned` (boolean) and `alias` (array of hostnames). Pick the production alias (typically the bare domain or the `*.vercel.app` matching the project name without the deployment hash).

If only the unique deployment URL is available (alias not yet assigned, e.g., very fresh project), use that — but note it in the Linear comment so the human can verify.

## 6. When to skip step 10 entirely

- The repo isn't a Vercel project (no `vercel.json`, not registered in the studio-manfred team).
- The pushed branch isn't the production branch (push went to a preview).
- The user explicitly says `--skip-vercel-wait`.

In all three cases, the skill notes the skip in the final summary and tells Linear "production URL unverified" instead of including a URL.

## Failure modes

- **`list_teams` empty / auth error:** `mcp__claude_ai_Vercel__authenticate` (if exists) or fall back to manual ("watch the dashboard, tell me when ready").
- **Project not found in `studio-manfred` team:** the project might be under a different team or a personal account. Ask the user.
- **Deployment found but stuck `BUILDING` past timeout:** could be a long build (e.g., heavy Next.js project). Ask user to extend timeout vs. abort. Don't auto-extend silently.
