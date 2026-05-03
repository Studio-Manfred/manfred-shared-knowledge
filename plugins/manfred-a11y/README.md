# manfred-a11y

> **DEPRECATED in v0.15.** All three skills (`a11y-design`, `a11y-dev`, `a11y-qa`) have moved to `manfred-design-systems`. This plugin is removed in v1.0.0.

## Migrate

```
/plugin install manfred-design-systems@manfred
/plugin uninstall manfred-a11y@manfred
```

The skill names are unchanged — references like `manfred-design-systems:a11y-qa` work the same way as the old `manfred-a11y:a11y-qa` did. Cross-plugin callers (`manfred-dev:test-my-code`, `manfred-dev:release`) already point at the new home in v0.15.

## Why the move

`manfred-design-systems` is the v1.0.0 home for everything systems-shaped — tokens, components, theming, accessibility. The a11y trio belongs there alongside `design-token`, `component-spec`, and the rest. The split into a separate `manfred-a11y` plugin was a v0.12 expedience; v1.0.0 fixes it.

## Skills (legacy — install manfred-design-systems instead)

| Skill | New home |
|-------|----------|
| `a11y-design` | `manfred-design-systems:a11y-design` |
| `a11y-dev` | `manfred-design-systems:a11y-dev` |
| `a11y-qa` | `manfred-design-systems:a11y-qa` |
