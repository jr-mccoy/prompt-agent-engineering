# WCAG Audit Patterns — Automated Testing and Remediation

## Automated Testing

```javascript
// axe-core integration
const axe = require('axe-core');

async function runAccessibilityAudit(page) {
  await page.addScriptTag({ path: require.resolve('axe-core') });

  const results = await page.evaluate(async () => {
    return await axe.run(document, {
      runOnly: {
        type: 'tag',
        values: ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa']
      }
    });
  });

  return {
    violations: results.violations,
    passes: results.passes,
    incomplete: results.incomplete
  };
}

// Playwright test example
test('should have no accessibility violations', async ({ page }) => {
  await page.goto('/');
  const results = await runAccessibilityAudit(page);

  expect(results.violations).toHaveLength(0);
});
```

```bash
# CLI tools
npx @axe-core/cli https://example.com
npx pa11y https://example.com
lighthouse https://example.com --only-categories=accessibility
```

---

## Remediation Patterns

### Fix: Missing Form Labels

```html
<!-- Before -->
<input type="email" placeholder="Email">

<!-- After: Option 1 - Visible label -->
<label for="email">Email address</label>
<input id="email" type="email">

<!-- After: Option 2 - aria-label -->
<input type="email" aria-label="Email address">

<!-- After: Option 3 - aria-labelledby -->
<span id="email-label">Email</span>
<input type="email" aria-labelledby="email-label">
```

### Fix: Insufficient Color Contrast

```css
/* Before: 2.5:1 contrast */
.text { color: #767676; }

/* After: 4.5:1 contrast */
.text { color: #595959; }

/* Or add background */
.text {
  color: #767676;
  background: #000;
}
```

### Fix: Keyboard Navigation

```javascript
// Make custom element keyboard accessible
class AccessibleDropdown extends HTMLElement {
  connectedCallback() {
    this.setAttribute('tabindex', '0');
    this.setAttribute('role', 'combobox');
    this.setAttribute('aria-expanded', 'false');

    this.addEventListener('keydown', (e) => {
      switch (e.key) {
        case 'Enter':
        case ' ':
          this.toggle();
          e.preventDefault();
          break;
        case 'Escape':
          this.close();
          break;
        case 'ArrowDown':
          this.focusNext();
          e.preventDefault();
          break;
        case 'ArrowUp':
          this.focusPrevious();
          e.preventDefault();
          break;
      }
    });
  }
}
```
