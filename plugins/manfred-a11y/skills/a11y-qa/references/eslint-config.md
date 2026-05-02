# Standalone ESLint a11y Config

Temporary config for accessibility-only scans. Create at project root, delete after scan.

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

## Usage

```bash
pnpm add -D eslint-plugin-jsx-a11y   # if not already installed
npx eslint --config eslint.a11y.mjs src/
```

Delete `eslint.a11y.mjs` after the scan. Keep the plugin installed.

## Known false positives

Do not report these as real violations:
- Custom component props named `role` (not the HTML `role` attribute)
- Components that forward ARIA props to underlying elements
- Dynamic content loaded after initial render (use runtime scan for those)
