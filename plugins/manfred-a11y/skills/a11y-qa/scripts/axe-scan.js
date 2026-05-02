// axe-core browser injection script
// Run via browser automation (Playwright, Puppeteer) on each page.
// After execution, retrieve window.__axeResults for the scan data.
//
// Check https://github.com/dequelabs/axe-core/releases for the latest version.
// Or use 'https://unpkg.com/axe-core/axe.min.js' (always latest, no version pin).

(async () => {
  if (!window.axe) {
    const script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.2/axe.min.js';
    document.head.appendChild(script);
    await new Promise(resolve => { script.onload = resolve; });
  }
  const results = await axe.run(document, {
    runOnly: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa', 'best-practice']
  });
  window.__axeResults = {
    page: window.location.pathname,
    violations: results.violations.length,
    passes: results.passes.length,
    incomplete: results.incomplete.length,
    details: results.violations.map(v => ({
      id: v.id,
      impact: v.impact,
      description: v.description,
      helpUrl: v.helpUrl,
      nodes: v.nodes.length,
      elements: v.nodes.slice(0, 5).map(n => ({
        html: n.html.substring(0, 200),
        target: n.target,
        failureSummary: n.failureSummary
      }))
    }))
  };
})().then(() => console.log('AXE_SCAN_DONE'));
