---
title: "Accessibility Testing (WCAG Compliance)"
category: testing
description: "Design accessibility testing for WCAG compliance and inclusive design"
techniques:
  - ST-01
  - ST-02
  - DS-01
  - RT-02
difficulty: intermediate
tags:
  - testing
  - accessibility
  - wcag
  - a11y
  - compliance
  - inclusive-design
updated: "2026-03-19"
---

# Accessibility Testing (WCAG Compliance)

**Objective:** Design and implement comprehensive accessibility testing to ensure your application meets WCAG (Web Content Accessibility Guidelines) standards and is usable by people with disabilities.

**When to Use:** Use this prompt when building public-facing websites, enterprise applications, government systems, or any product that must be accessible to users with disabilities. Essential for legal compliance (ADA, Section 508), inclusive design, and reaching wider audiences.

**Instructions:**

1. **Understand WCAG Conformance Levels**
   - **Level A**: Minimum accessibility (basic support for assistive technologies)
   - **Level AA**: Mid-range accessibility (recommended standard, legally required in many jurisdictions)
   - **Level AAA**: Highest accessibility (enhanced support, difficult to achieve for all content)
   - **Target**: WCAG 2.1 Level AA or WCAG 2.2 Level AA (latest)

2. **Identify Key Accessibility Requirements**
   Review WCAG 2.1/2.2 principles (POUR):
   - **Perceivable**: Information must be presentable to users in ways they can perceive
     - Text alternatives, captions, adaptable content, distinguishable elements
   - **Operable**: UI components and navigation must be operable
     - Keyboard accessible, enough time, navigable, input modalities
   - **Understandable**: Information and UI operation must be understandable
     - Readable, predictable, input assistance
   - **Robust**: Content must be robust enough for assistive technologies
     - Compatible with current and future tools

3. **Select Accessibility Testing Tools**
   - **Automated Testing**:
     - **axe-core**: Industry standard, comprehensive rules (Deque Systems)
     - **Pa11y**: Command-line tool, CI/CD friendly
     - **Lighthouse**: Chrome DevTools, accessibility audit included
     - **WAVE**: Browser extension, visual feedback
     - **jest-axe**: Jest integration for component testing
   - **Manual Testing**:
     - Screen readers (NVDA, JAWS, VoiceOver)
     - Keyboard navigation testing
     - Color contrast analyzers
     - Browser zoom testing (200%, 400%)

4. **Design Automated Accessibility Tests**
   - Test all pages and critical user flows
   - Test interactive components (forms, modals, dropdowns)
   - Test dynamic content updates
   - Test keyboard navigation paths
   - Test ARIA attributes and landmark regions
   - Test color contrast ratios
   - Test form labels and error messages

5. **Plan Manual Accessibility Testing**
   Automated tools catch only 30-40% of issues. Manual testing required for:
   - **Screen Reader Testing**: Navigate entire app with eyes closed
   - **Keyboard-Only Navigation**: Complete all tasks without mouse
   - **Focus Management**: Verify logical focus order and visible focus indicators
   - **Content Understanding**: Ensure content makes sense when linearized
   - **Zoom Testing**: Test at 200% and 400% zoom levels

6. **Create Accessibility Test Scenarios**
   - **User Persona-Based**: Blind user, low vision, motor disability, cognitive disability
   - **Assistive Technology-Based**: Screen reader, screen magnifier, voice control
   - **Scenario-Based**: Complete purchase, fill form, navigate site, consume content

7. **Establish Accessibility Standards and Gates**
   - Define acceptance criteria (zero critical violations, < 5 moderate)
   - Set up automated testing in CI/CD pipeline
   - Create accessibility checklist for code reviews
   - Plan accessibility audit schedule

8. **CRITICAL: Validate Accessibility Issues Before Reporting**
   - Confirm each issue with both automated tools AND manual verification
   - Test with actual assistive technology, not just automated scanners
   - Verify issues are reproducible across multiple browsers/assistive tech
   - **Confidence level** for each issue:
     - **High Confidence:** Confirmed by automated tool + manual testing + assistive technology
     - **Medium Confidence:** Flagged by automated tool, manually verified but not tested with assistive tech
     - **Low Confidence:** Flagged by automated tool only, may be false positive

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Report automated tool findings without manual verification (tools have ~30-50% false positive rate)
- Flag issues in third-party embedded content you don't control (iframes, widgets)
- Report ARIA violations without understanding the component's actual behavior
- Assume color contrast issues without checking actual rendered colors (CSS variables, overlays)
- Flag missing alt text on decorative images that should be hidden from screen readers
- Report keyboard navigation issues in components meant to be mouse-only (drag-and-drop with alternative)
- Assume hidden content needs accessibility (visually-hidden != screen-reader-hidden)

✅ **DO:**
- Test every flagged issue manually with keyboard navigation
- Verify critical issues using at least one screen reader (NVDA, VoiceOver)
- Check if reported contrast issues account for focus states, hover states
- Confirm form label associations by clicking labels and verifying input focus
- Test with browser zoom at 200% and 400% before reporting reflow issues
- Consider user context (is this a power-user app where some complexity is acceptable?)
- Document workarounds when complete compliance isn't feasible
- Prioritize issues by actual user impact, not just WCAG severity

**Expected Output:** A comprehensive accessibility testing strategy including:
- WCAG conformance level target (A, AA, or AAA)
- Selected testing tools and integration approach
- Automated accessibility test suite with examples
- Manual testing procedures and checklists
- User persona-based test scenarios
- Accessibility defect tracking and remediation plan
- CI/CD integration for automated checks
- Team training and awareness plan

**Example Output:**

```markdown
## Accessibility Testing Strategy

**Target**: WCAG 2.1 Level AA Compliance
**Application**: E-commerce Website
**Priority**: High (legal requirement + inclusive design)

---

### Accessibility Requirements (WCAG 2.1 AA)

#### Perceivable (P)
- ✅ **1.1.1 Non-text Content**: All images have alt text
- ✅ **1.3.1 Info and Relationships**: Semantic HTML, proper heading hierarchy
- ✅ **1.4.3 Contrast (Minimum)**: 4.5:1 for normal text, 3:1 for large text
- ✅ **1.4.4 Resize Text**: Text can be resized up to 200% without loss of content
- ✅ **1.4.5 Images of Text**: Use actual text instead of images of text

#### Operable (O)
- ✅ **2.1.1 Keyboard**: All functionality available via keyboard
- ✅ **2.1.2 No Keyboard Trap**: Focus can move away from all components
- ✅ **2.4.3 Focus Order**: Focus order is logical and intuitive
- ✅ **2.4.7 Focus Visible**: Keyboard focus indicator is visible
- ✅ **2.5.3 Label in Name**: Accessible name contains visible label text

#### Understandable (U)
- ✅ **3.1.1 Language of Page**: HTML lang attribute set
- ✅ **3.2.1 On Focus**: No unexpected context changes on focus
- ✅ **3.3.1 Error Identification**: Form errors clearly identified
- ✅ **3.3.2 Labels or Instructions**: Form inputs have clear labels
- ✅ **3.3.3 Error Suggestion**: Error messages provide suggestions

#### Robust (R)
- ✅ **4.1.1 Parsing**: Valid HTML (no duplicate IDs)
- ✅ **4.1.2 Name, Role, Value**: All UI components have accessible names and roles
- ✅ **4.1.3 Status Messages**: Status messages announced to screen readers

---

### Automated Testing Setup

**Tool**: axe-core + jest-axe + Playwright

**Installation**:
```bash
npm install --save-dev jest-axe @axe-core/playwright
```

#### Component-Level Accessibility Tests

```javascript
// src/components/Button/Button.test.tsx
import React from 'react';
import { render } from '@testing-library/react';
import { axe, toHaveNoViolations } from 'jest-axe';
import { Button } from './Button';

expect.extend(toHaveNoViolations);

describe('Button Accessibility', () => {
  it('should not have accessibility violations', async () => {
    const { container } = render(<Button>Click me</Button>);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });

  it('should have accessible name from children', async () => {
    const { getByRole } = render(<Button>Submit Form</Button>);
    expect(getByRole('button', { name: 'Submit Form' })).toBeInTheDocument();
  });

  it('should be keyboard accessible', () => {
    const handleClick = jest.fn();
    const { getByRole } = render(<Button onClick={handleClick}>Click</Button>);

    const button = getByRole('button');
    button.focus();
    button.click();

    expect(handleClick).toHaveBeenCalled();
  });

  it('disabled button should not be keyboard accessible', () => {
    const { getByRole } = render(<Button disabled>Disabled</Button>);
    const button = getByRole('button');

    expect(button).toHaveAttribute('aria-disabled', 'true');
    expect(button).toHaveAttribute('tabindex', '-1');
  });
});
```

#### Page-Level Accessibility Tests

```javascript
// tests/accessibility/pages.spec.ts
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test.describe('Page Accessibility Tests', () => {
  test('homepage should not have accessibility violations', async ({ page }) => {
    await page.goto('/');

    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21aa'])
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);
  });

  test('product listing page should not have violations', async ({ page }) => {
    await page.goto('/products');

    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa'])
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);
  });

  test('checkout page with form validation', async ({ page }) => {
    await page.goto('/checkout');

    // Trigger form validation errors
    await page.click('[data-testid="submit-checkout"]');

    // Wait for error messages to appear
    await page.waitForSelector('[role="alert"]');

    // Run accessibility scan including error states
    const results = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa'])
      .analyze();

    expect(results.violations).toEqual([]);

    // Verify error messages are properly announced
    const errorMessages = await page.locator('[role="alert"]').all();
    expect(errorMessages.length).toBeGreaterThan(0);

    for (const error of errorMessages) {
      const ariaLive = await error.getAttribute('aria-live');
      expect(['polite', 'assertive']).toContain(ariaLive);
    }
  });
});
```

---

### Keyboard Navigation Tests

```javascript
test.describe('Keyboard Navigation', () => {
  test('should navigate entire site with keyboard only', async ({ page }) => {
    await page.goto('/');

    // Tab through all interactive elements
    const interactiveElements = await page.locator(
      'a, button, input, select, textarea, [tabindex]:not([tabindex="-1"])'
    ).all();

    for (let i = 0; i < interactiveElements.length; i++) {
      await page.keyboard.press('Tab');

      // Verify focus is visible
      const focusedElement = await page.locator(':focus');
      expect(await focusedElement.count()).toBe(1);

      // Verify focus indicator is visible (not default browser outline)
      const outline = await focusedElement.evaluate((el) =>
        window.getComputedStyle(el).outline
      );
      expect(outline).not.toBe('none');
    }
  });

  test('should activate button with Enter and Space', async ({ page }) => {
    await page.goto('/products');

    const button = page.locator('[data-testid="filter-button"]');
    await button.focus();

    // Test Enter key
    await page.keyboard.press('Enter');
    await expect(page.locator('[data-testid="filter-panel"]')).toBeVisible();

    // Close panel
    await page.keyboard.press('Escape');

    // Test Space key
    await button.focus();
    await page.keyboard.press('Space');
    await expect(page.locator('[data-testid="filter-panel"]')).toBeVisible();
  });

  test('modal should trap focus', async ({ page }) => {
    await page.goto('/');

    // Open modal
    await page.click('[data-testid="open-modal"]');
    await page.waitForSelector('[role="dialog"]');

    const modalElements = await page.locator(
      '[role="dialog"] button, [role="dialog"] input'
    ).all();

    // Tab through all elements in modal
    for (let i = 0; i < modalElements.length + 1; i++) {
      await page.keyboard.press('Tab');
    }

    // Focus should still be within modal
    const focusedElement = await page.locator(':focus');
    const isInsideModal = await focusedElement.evaluate((el) => {
      return !!el.closest('[role="dialog"]');
    });

    expect(isInsideModal).toBe(true);
  });
});
```

---

### Color Contrast Testing

```javascript
test.describe('Color Contrast', () => {
  test('all text should meet WCAG AA contrast requirements', async ({ page }) => {
    await page.goto('/');

    const results = await new AxeBuilder({ page })
      .withRules(['color-contrast'])
      .analyze();

    expect(results.violations).toEqual([]);
  });

  test('verify specific component contrast ratios', async ({ page }) => {
    await page.goto('/');

    // Get computed styles for critical elements
    const buttonContrast = await page.locator('[data-testid="cta-button"]').evaluate((el) => {
      const styles = window.getComputedStyle(el);
      const color = styles.color;
      const backgroundColor = styles.backgroundColor;

      // Use color contrast library to calculate ratio
      // (implementation depends on library)
      return { color, backgroundColor };
    });

    // Verify contrast ratio meets 4.5:1 for normal text
    // or 3:1 for large text (18pt+ or 14pt+ bold)
  });
});
```

---

### Screen Reader Testing Checklist

**Tool**: NVDA (Windows), VoiceOver (macOS), TalkBack (Android)

#### Homepage Screen Reader Test
- [ ] Page title is announced on load
- [ ] Main landmark regions identified (header, nav, main, footer)
- [ ] Navigation menu is navigable with arrow keys
- [ ] Images have descriptive alt text
- [ ] Links have meaningful text (not "click here")
- [ ] Headings create logical document outline (h1 → h2 → h3)

#### Product Listing Screen Reader Test
- [ ] Product count announced ("Showing 24 of 100 products")
- [ ] Filters are labeled and associated with controls
- [ ] Price information announced correctly
- [ ] "Add to cart" buttons have product name in accessible name
- [ ] Sort dropdown announces current selection and options

#### Checkout Form Screen Reader Test
- [ ] Form fields have associated labels
- [ ] Required fields are announced as required
- [ ] Error messages are announced immediately (aria-live)
- [ ] Error messages are associated with fields (aria-describedby)
- [ ] Field instructions provided before user input
- [ ] Success confirmation announced after submission

**Sample Screen Reader Script**:
```
1. Navigate to homepage
2. Verify page title: "E-commerce Store - Shop Electronics"
3. Navigate by headings (H key): Verify heading hierarchy
4. Navigate by landmarks (D key): Verify main regions
5. Tab through navigation: Verify link announcements
6. Search for product: Verify search results announced
7. Add product to cart: Verify confirmation announced
8. Complete checkout: Verify all form fields labeled
9. Submit form: Verify success/error messages announced
```

---

### Manual Accessibility Testing Procedures

#### Keyboard-Only Testing Procedure
1. **Disconnect mouse** or don't use it at all
2. **Navigate**: Use Tab (forward), Shift+Tab (backward)
3. **Activate**: Use Enter (links/buttons), Space (buttons/checkboxes)
4. **Select**: Use arrow keys (dropdowns/radio groups)
5. **Close**: Use Escape (modals/dropdowns)
6. **Verify**: Can you complete all tasks without mouse?

#### Zoom Testing Procedure
1. **Zoom to 200%**: Verify all content visible and usable
2. **Zoom to 400%**: Verify content remains accessible (WCAG 2.1 AA)
3. **Check horizontal scrolling**: Should be minimal or none
4. **Check text reflow**: Text should wrap, not overflow
5. **Check interactive elements**: Buttons and links still clickable

#### Focus Management Testing
1. **Visible focus indicator**: Always visible, distinct from hover
2. **Logical focus order**: Top to bottom, left to right
3. **No focus traps**: Can always escape with keyboard
4. **Modal focus**: Trapped in modal when open
5. **Skip links**: Present for keyboard users to skip navigation

---

### CI/CD Integration

```yaml
# .github/workflows/accessibility.yml
name: Accessibility Tests

on:
  pull_request:
  push:
    branches: [main]

jobs:
  accessibility:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm ci

      - name: Run accessibility tests
        run: npm run test:a11y

      - name: Run Pa11y on critical pages
        run: |
          npm start &
          npx wait-on http://localhost:3000
          npx pa11y-ci --config .pa11yci.json

      - name: Upload accessibility report
        if: failure()
        uses: actions/upload-artifact@v3
        with:
          name: accessibility-violations
          path: pa11y-report.json

      - name: Comment PR with violations
        if: failure() && github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            // Parse violations and comment on PR
```

**Pa11y Configuration** (`.pa11yci.json`):
```json
{
  "defaults": {
    "standard": "WCAG2AA",
    "runners": ["axe", "htmlcs"],
    "timeout": 10000,
    "wait": 1000,
    "chromeLaunchConfig": {
      "args": ["--no-sandbox"]
    }
  },
  "urls": [
    "http://localhost:3000/",
    "http://localhost:3000/products",
    "http://localhost:3000/products/1",
    "http://localhost:3000/cart",
    "http://localhost:3000/checkout"
  ],
  "threshold": 0
}
```

---

### Common Accessibility Issues and Fixes

#### Issue 1: Missing Form Labels
```html
<!-- ❌ Bad: No label -->
<input type="text" placeholder="Enter your name" />

<!-- ✅ Good: Visible label -->
<label for="name">Name</label>
<input id="name" type="text" />

<!-- ✅ Good: aria-label for icon-only buttons -->
<button aria-label="Close dialog">
  <XIcon />
</button>
```

#### Issue 2: Poor Color Contrast
```css
/* ❌ Bad: 2.5:1 contrast ratio */
.text {
  color: #999; /* Light gray */
  background: #fff; /* White */
}

/* ✅ Good: 4.6:1 contrast ratio */
.text {
  color: #666; /* Darker gray */
  background: #fff;
}
```

#### Issue 3: Non-Semantic HTML
```html
<!-- ❌ Bad: div soup -->
<div class="button" onclick="submit()">Submit</div>

<!-- ✅ Good: semantic HTML -->
<button type="submit">Submit</button>
```

#### Issue 4: Missing Skip Link
```html
<!-- ✅ Good: skip to main content -->
<body>
  <a href="#main-content" class="skip-link">Skip to main content</a>
  <header><!-- navigation --></header>
  <main id="main-content"><!-- content --></main>
</body>
```

---

### Accessibility Defect Tracking

| Issue ID | WCAG | Severity | Page | Description | Confidence | Verification Method |
|----------|------|----------|------|-------------|------------|---------------------|
| A11Y-001 | 1.4.3 | Critical | Checkout | Button contrast 2.1:1 | High | axe + manual + contrast analyzer |
| A11Y-002 | 2.4.7 | High | All | No visible focus indicator | High | Manual keyboard test |
| A11Y-003 | 3.3.2 | High | Contact | Form fields missing labels | High | axe + NVDA verification |
| A11Y-004 | 1.1.1 | Medium | Products | Product images missing alt | Medium | axe flag, not tested with SR |
| A11Y-005 | 4.1.2 | Medium | Nav | Mobile menu not keyboard accessible | High | Keyboard-only navigation test |

### False Positives Dismissed

| Tool Finding | Reason Dismissed | Verification |
|--------------|------------------|--------------|
| "Link has no discernible text" on icon buttons | aria-label present, axe config issue | Manual inspection confirmed |
| "Contrast ratio insufficient" on hover state | Only applies during interaction, not resting state | WCAG allows this |
| "Missing form label" on search | Uses aria-label, not visible label | NVDA announces correctly |
| "Duplicate ID" on React portal | IDs in different DOM trees, no conflict | Browser console clean |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- ST-07 (Prioritization and Ranking)
- RT-01 (Requirement Analysis)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- OC-04 (Comprehensive Example Outputs)
- TC-03 (Framework-Based Analysis - WCAG)

**Related Prompts:**
- testing_e2e_test_scenario_creation.md - For including accessibility in E2E tests
- testing_visual_regression.md - For visual accessibility testing
- code-analysis/frontend/frontend_component_architecture.md - For accessible component design
- quality_code_review_checklist.md - To include accessibility checks

**Customization Guide:**
- **For Government Sites**: Target WCAG 2.1 Level AA + Section 508 compliance, extensive documentation required
- **For SaaS Products**: Focus on keyboard navigation and screen reader support for power users
- **For Content Sites**: Emphasize semantic HTML, heading hierarchy, alt text for all images
- **For E-commerce**: Ensure checkout process is fully keyboard accessible, test with assistive technologies
- **For Mobile Apps**: Use platform-specific accessibility APIs (iOS VoiceOver, Android TalkBack)
