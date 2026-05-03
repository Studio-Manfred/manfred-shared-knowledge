# manfred-dev

Engineering workflow for Vite/React projects: pre-merge QA, lightweight deploy, and full production release.

## Skills

| Skill | When it triggers |
|-------|-----------------|
| `test-my-code` | "test my code", "run QA", "is this ready to ship" — runs typecheck → lint → vitest → build → Playwright → axe gate, saves report, posts to Linear |
| `deploy` | "deploy", "ship it", "version bump", "cut a release" — lightweight release path: changelog + tag + push |
| `release` | "release", "ship to production", "ship STU-###" — production-grade with Vercel build verification + Linear ticket update |

## Cross-plugin dependencies

`test-my-code` and `release` both call into the `manfred-design-systems` plugin's `a11y-qa` skill for the runtime accessibility scan. Install both plugins for the full gate:

```
/plugin install manfred-design-systems@manfred
/plugin install manfred-dev@manfred
```

If `manfred-design-systems` is not installed, the a11y gate falls back to a soft warning. (Pre-v0.15: `a11y-qa` lived in `manfred-a11y`; that plugin is deprecated and will be removed in v1.0.0.)

## Install

```
/plugin marketplace add Studio-Manfred/manfred-shared-knowledge
/plugin install manfred-dev@manfred
```
