# manfred-dev

Engineering workflow for Vite/React projects: pre-merge QA, lightweight deploy, full production release, and project bootstrap.

## Skills

| Skill | When it triggers |
|-------|-----------------|
| `test-my-code` | "test my code", "run QA", "is this ready to ship" — runs typecheck → lint → vitest → build → Playwright → axe gate, saves report, posts to Linear |
| `deploy` | "deploy", "ship it", "version bump", "cut a release" — lightweight release path: changelog + tag + push |
| `release` | "release", "ship to production", "ship STU-###" — production-grade with Vercel build verification + Linear ticket update |
| `bootstrap-manfred-project` | "start a new Manfred project", "add manfred-bootstrap to this project", "overlay Manfred bootstrap", "download the latest bootstrap" — scaffolds a new project, overlays WoW onto existing, or clones the template |
| `install-manfred-claude-skills` | "install manfred Claude skills", "set up manfred Claude" — registers the marketplace, picks plugins, optional home-level install |

## Cross-plugin dependencies

`test-my-code` and `release` both call into the `manfred-design-systems` plugin's `a11y-qa` skill for the runtime accessibility scan. Install both plugins for the full gate:

```
/plugin install manfred-design-systems@manfred
/plugin install manfred-dev@manfred
```

If `manfred-design-systems` is not installed, the a11y gate falls back to a soft warning.

## Install

```
/plugin marketplace add Studio-Manfred/manfred-shared-knowledge
/plugin install manfred-dev@manfred
```
