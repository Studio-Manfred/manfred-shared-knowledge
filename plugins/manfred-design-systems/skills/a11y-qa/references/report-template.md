# Accessibility Audit Report Template

Present findings in this structure:

```markdown
## Accessibility Audit Results

**Scan mode:** [runtime / static / full]
**Standards:** WCAG 2.2 Level AA + Best Practices
**Date:** [date]
**Pages / files scanned:** [count]

### Summary

| Page / File | Violations | Passes | Worst impact |
|-------------|-----------|--------|--------------|
| /           | 3         | 42     | serious      |
| /about      | 1         | 39     | moderate     |

**Total violations:** [n]
Critical: [n] | Serious: [n] | Moderate: [n] | Minor: [n]

---

### Violations

#### 1. [rule-id] — [impact]

**Description:** [what the rule checks]
**WCAG criterion:** [e.g. 1.1.1 Non-text Content (Level A)]
**Pages / files affected:** [list]
**Instances:** [count]

**Example element:**
```html
<element that failed>
```

**Fix:** [specific recommendation from auto-fix table]
**Reference:** [axe-core help URL]

---

### Recommended Next Steps

1. [Highest-priority fix]
2. [Second priority]
3. [etc.]
```
