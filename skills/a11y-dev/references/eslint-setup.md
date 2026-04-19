# ESLint Static Analysis Setup

Catch accessibility issues at development time with `eslint-plugin-jsx-a11y`.
This runs without a browser and is ideal for CI and PR checks.

## Install

```bash
pnpm add -D eslint-plugin-jsx-a11y   # or npm install -D / yarn add -D
```

## Standalone config (ESLint 9 flat config)

Create this file at project root, run the scan, then delete it.

```javascript
// eslint.a11y.mjs
import jsxA11y from "eslint-plugin-jsx-a11y";
import tseslint from "typescript-eslint";

export default [
  {
    files: ["src/**/*.tsx", "src/**/*.jsx"],
    plugins: { "jsx-a11y": jsxA11y },
    languageOptions: {
      parser: tseslint.parser,
      parserOptions: { ecmaFeatures: { jsx: true } },
    },
    rules: { ...jsxA11y.flatConfigs.recommended.rules },
  },
];
```

## Run

```bash
npx eslint --config eslint.a11y.mjs src/
```

Delete `eslint.a11y.mjs` after the scan. Keep `eslint-plugin-jsx-a11y` installed.

## Known false positives to suppress

- Custom component props named `role` that are not the HTML `role` attribute
- Components that forward ARIA props to an underlying element

Suppress with `// eslint-disable-next-line jsx-a11y/<rule>` and a comment explaining why.

## Integrating into CI

Add as a separate lint job so it doesn't block the main lint pipeline:

```yaml
# .github/workflows/a11y.yml
- name: Accessibility lint
  run: |
    cp .github/eslint.a11y.mjs .
    npx eslint --config eslint.a11y.mjs src/ --format json > a11y-report.json
    rm eslint.a11y.mjs
```
