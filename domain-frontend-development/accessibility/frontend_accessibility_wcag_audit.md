---
title: "WCAG Accessibility Compliance Audit"
category: frontend-development/accessibility
description: "Conduct comprehensive WCAG 2.1/2.2 compliance audits identifying accessibility barriers with remediation priorities and implementation guidance"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - accessibility
  - wcag
  - a11y
  - compliance
  - audit
  - inclusive-design
updated: "2026-01-29"
related_prompts:
  - domain-frontend-development/accessibility/frontend_accessibility_aria_patterns.md
  - domain-frontend-development/accessibility/frontend_accessibility_screen_reader.md
  - domain-software-engineering/testing/testing_accessibility_wcag.md
---

# WCAG Accessibility Compliance Audit

**Objective:** Conduct a comprehensive accessibility audit of a web application against WCAG 2.1/2.2 guidelines, identifying barriers that prevent users with disabilities from accessing content and functionality.

**When to Use:**
- Use when: Assessing accessibility compliance before launch
- Use when: Responding to accessibility complaints or legal requirements
- Use when: Establishing baseline accessibility for improvement planning
- Use when: Validating accessibility after major redesigns
- Don't use when: Quick spot-check only (use automated tools directly)

## Instructions

1. **Define Audit Scope**
   - Target conformance level (A, AA, or AAA)
   - Pages/flows to be audited
   - Assistive technologies to test with
   - Applicable legal requirements (ADA, Section 508, EN 301 549)

2. **Conduct Automated Testing**
   - Run axe-core, WAVE, or Lighthouse accessibility audits
   - Document all automated findings
   - Note: Automated tools catch only 30-40% of issues

3. **Conduct Manual Testing**
   - Keyboard-only navigation (Tab, Enter, Space, Arrow keys, Escape)
   - Screen reader testing (NVDA, VoiceOver, JAWS)
   - Zoom testing (200%, 400%)
   - Color and contrast verification
   - Content structure and reading order

4. **Evaluate Against WCAG Criteria**
   For each applicable success criterion:
   - Perceivable: Can users perceive the content?
   - Operable: Can users operate the interface?
   - Understandable: Is the interface understandable?
   - Robust: Is content robust for assistive technologies?

5. **CRITICAL: Validate Findings**
   - Confirm each issue with multiple testing methods
   - Test with actual assistive technology, not just automated tools
   - Verify the user impact of each barrier
   - **Confidence level** for each finding:
     - **High Confidence**: Confirmed by automated + manual + AT testing
     - **Medium Confidence**: Confirmed by 2 of 3 methods
     - **Low Confidence**: Single method detection only

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Report automated tool findings without manual verification
- Flag decorative images for missing alt text (they should have alt="")
- Report ARIA issues without understanding component behavior
- Assume color contrast failure without checking actual rendered values
- Flag third-party embedded content you don't control
- Report issues in content that's intentionally hidden from all users
- Flag mobile-specific patterns as keyboard accessibility failures

✅ **DO:**
- Verify every critical/high finding with screen reader testing
- Check if seemingly missing labels have programmatic associations
- Test color contrast in actual context (overlays, backgrounds)
- Consider responsive behavior when testing keyboard navigation
- Distinguish between actual barriers and minor improvements
- Document browser/AT combinations used for testing
- Prioritize by actual user impact, not just WCAG level

## Expected Output

A comprehensive accessibility audit report including:
- Executive summary with compliance status
- Detailed findings by WCAG principle
- Prioritized remediation plan
- Testing methodology documentation
- Pass/fail status for each criterion

### Output Format

```markdown
## Accessibility Audit Report

### Executive Summary
[Compliance status, critical issues, key recommendations]

### Audit Methodology
[Scope, tools, assistive technologies used]

### Findings by WCAG Principle
[Detailed issues organized by POUR principles]

### Remediation Roadmap
[Prioritized action plan]

### Appendix
[Testing details, browser/AT matrix]
```

## Example Output

```markdown
## Accessibility Audit Report

### Executive Summary

**Audit Date:** 2026-01-29
**Target Level:** WCAG 2.1 Level AA
**Scope:** E-commerce website (12 key pages)
**Overall Compliance:** 68% Pass Rate (Partial Compliance)

**Critical Barriers Found:** 4
- Checkout form completely inaccessible to screen readers
- No keyboard access to product filters
- Videos lack captions
- Focus trapping in modal dialogs broken

**High Priority Issues:** 12
**Medium Priority Issues:** 23
**Low Priority Issues:** 15

**Recommendation:** Address 4 critical barriers immediately. Implement phased remediation plan over 8 weeks to achieve AA compliance.

---

### Audit Methodology

**Tools Used:**
- axe-core v4.8 (automated scanning)
- WAVE browser extension
- Colour Contrast Analyser
- Manual keyboard testing
- Screen readers: NVDA 2024.1, VoiceOver (macOS 14)

**Browsers Tested:**
- Chrome 120, Firefox 121, Safari 17

**Pages Audited:**
1. Homepage
2. Product listing
3. Product detail
4. Shopping cart
5. Checkout (4 steps)
6. Order confirmation
7. Account login/register
8. Account profile
9. Search results
10. Contact form

---

### Findings by WCAG Principle

## Perceivable

### 1.1 Text Alternatives

#### 1.1.1 Non-text Content (Level A) - FAIL

**Issue P-001: Product Images Missing Alt Text**
- **Severity:** High
- **Confidence:** High (automated + manual + NVDA)
- **Location:** Product listing page, 47 product images
- **Evidence:**
  ```html
  <!-- Current -->
  <img src="product-123.jpg">

  <!-- Screen reader announces: "product-123.jpg, image" -->
  ```
- **User Impact:** Blind users cannot identify products, cannot shop independently
- **Remediation:**
  ```html
  <img src="product-123.jpg" alt="Blue cotton t-shirt with round neck, front view">
  ```
- **Effort:** Low (content update)
- **WCAG Reference:** 1.1.1 Non-text Content

**Issue P-002: Decorative Icons Announced by Screen Readers**
- **Severity:** Medium
- **Confidence:** High
- **Location:** Navigation, buttons throughout site
- **Evidence:**
  ```html
  <!-- Current: Icon announced as "shopping cart graphic" -->
  <button>
    <svg>...</svg>
    Cart
  </button>
  ```
- **Remediation:**
  ```html
  <button>
    <svg aria-hidden="true">...</svg>
    Cart
  </button>
  ```
- **Effort:** Low

### 1.2 Time-based Media

#### 1.2.2 Captions (Prerecorded) (Level A) - FAIL

**Issue P-003: Product Videos Lack Captions**
- **Severity:** Critical
- **Confidence:** High
- **Location:** 23 product pages with demo videos
- **User Impact:** Deaf/hard-of-hearing users miss product information
- **Remediation:** Add synchronized captions to all videos
- **Effort:** High (need caption files for 23 videos)

### 1.3 Adaptable

#### 1.3.1 Info and Relationships (Level A) - PARTIAL FAIL

**Issue P-004: Form Labels Not Programmatically Associated**
- **Severity:** Critical
- **Confidence:** High
- **Location:** Checkout form, all input fields
- **Evidence:**
  ```html
  <!-- Current: No association -->
  <span>Email Address</span>
  <input type="email" name="email">

  <!-- NVDA announces: "edit blank" - no label! -->
  ```
- **User Impact:** Screen reader users cannot identify form fields, cannot complete checkout
- **Remediation:**
  ```html
  <label for="email">Email Address</label>
  <input type="email" id="email" name="email">
  ```
- **Effort:** Medium

#### 1.3.2 Meaningful Sequence (Level A) - PASS
✅ Content follows logical reading order when CSS is disabled.

### 1.4 Distinguishable

#### 1.4.3 Contrast (Minimum) (Level AA) - FAIL

**Issue P-005: Insufficient Text Contrast**
- **Severity:** High
- **Confidence:** High (verified with Colour Contrast Analyser)
- **Location:** Footer links, placeholder text, disabled buttons
- **Evidence:**

  | Element | Foreground | Background | Ratio | Required |
  |---------|------------|------------|-------|----------|
  | Footer links | #888 | #333 | 2.8:1 | 4.5:1 |
  | Placeholder | #aaa | #fff | 2.3:1 | 4.5:1 |
  | Sale badge | #fff | #ff6b6b | 3.2:1 | 4.5:1 |

- **Remediation:**
  ```css
  /* Footer links */
  .footer-link { color: #b3b3b3; } /* 5.1:1 */

  /* Placeholders - use visible labels instead */

  /* Sale badge */
  .sale-badge { background: #d32f2f; } /* 5.5:1 */
  ```
- **Effort:** Low

#### 1.4.4 Resize Text (Level AA) - PASS
✅ Content remains usable at 200% zoom. No horizontal scrolling required.

#### 1.4.10 Reflow (Level AA) - FAIL

**Issue P-006: Horizontal Scroll at 400% Zoom**
- **Severity:** Medium
- **Confidence:** Medium (tested on Chrome only)
- **Location:** Product grid, data tables
- **User Impact:** Low vision users must scroll horizontally
- **Remediation:** Implement responsive breakpoints that reflow to single column at 320px viewport
- **Effort:** Medium

---

## Operable

### 2.1 Keyboard Accessible

#### 2.1.1 Keyboard (Level A) - FAIL

**Issue O-001: Filter Panel Not Keyboard Accessible**
- **Severity:** Critical
- **Confidence:** High
- **Location:** Product listing page filters
- **Evidence:** Tab key skips filter controls entirely. Filters only respond to mouse clicks.
- **User Impact:** Keyboard users cannot filter products, major feature inaccessible
- **Remediation:**
  - Add tabindex="0" to filter container
  - Implement arrow key navigation within filter groups
  - Add Enter/Space activation for filter options
- **Effort:** High

**Issue O-002: Custom Dropdown Not Keyboard Operable**
- **Severity:** High
- **Confidence:** High
- **Location:** Sort by dropdown, quantity selector
- **Evidence:**
  ```html
  <!-- Current: div-based dropdown -->
  <div class="dropdown" onclick="toggleDropdown()">
    <div class="selected">Sort by: Price</div>
    <div class="options">...</div>
  </div>
  ```
- **Remediation:** Use native `<select>` or implement full ARIA combobox pattern
- **Effort:** Medium

#### 2.1.2 No Keyboard Trap (Level A) - FAIL

**Issue O-003: Modal Dialog Traps Focus Incorrectly**
- **Severity:** Critical
- **Confidence:** High
- **Location:** Quick view modal, size guide modal
- **Evidence:** Focus escapes modal to background content when tabbing. Escape key doesn't close modal.
- **Remediation:**
  ```javascript
  // Implement proper focus trap
  const focusableElements = modal.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  // Cycle focus within modal
  // Close on Escape
  ```
- **Effort:** Medium

### 2.4 Navigable

#### 2.4.1 Bypass Blocks (Level A) - FAIL

**Issue O-004: No Skip Navigation Link**
- **Severity:** High
- **Confidence:** High
- **Location:** All pages
- **User Impact:** Keyboard/screen reader users must tab through 47 navigation items on every page
- **Remediation:**
  ```html
  <body>
    <a href="#main-content" class="skip-link">Skip to main content</a>
    <header>...</header>
    <main id="main-content">...</main>
  </body>
  ```
- **Effort:** Low

#### 2.4.7 Focus Visible (Level AA) - FAIL

**Issue O-005: Focus Indicator Removed**
- **Severity:** High
- **Confidence:** High
- **Location:** Global CSS
- **Evidence:**
  ```css
  /* Found in global.css */
  *:focus { outline: none; }
  ```
- **User Impact:** Keyboard users cannot see where they are on the page
- **Remediation:**
  ```css
  *:focus-visible {
    outline: 2px solid #005fcc;
    outline-offset: 2px;
  }
  ```
- **Effort:** Low

### 2.5 Input Modalities

#### 2.5.3 Label in Name (Level A) - PASS
✅ Visible labels match accessible names.

---

## Understandable

### 3.1 Readable

#### 3.1.1 Language of Page (Level A) - PASS
✅ `<html lang="en">` present on all pages.

### 3.2 Predictable

#### 3.2.2 On Input (Level A) - FAIL

**Issue U-001: Form Auto-Submits on Dropdown Change**
- **Severity:** Medium
- **Confidence:** High
- **Location:** Sort dropdown on product listing
- **Evidence:** Changing sort order immediately submits form without user confirmation
- **User Impact:** Screen reader users exploring options may trigger unintended actions
- **Remediation:** Add explicit "Apply" button or delay auto-submit with announcement
- **Effort:** Low

### 3.3 Input Assistance

#### 3.3.1 Error Identification (Level A) - PARTIAL FAIL

**Issue U-002: Form Errors Not Programmatically Associated**
- **Severity:** High
- **Confidence:** High
- **Location:** Checkout form
- **Evidence:**
  ```html
  <!-- Error message not linked to input -->
  <input type="email" id="email" class="error">
  <span class="error-msg">Please enter a valid email</span>
  ```
- **Remediation:**
  ```html
  <input type="email" id="email"
         aria-invalid="true"
         aria-describedby="email-error">
  <span id="email-error" class="error-msg">Please enter a valid email</span>
  ```
- **Effort:** Low

#### 3.3.2 Labels or Instructions (Level A) - FAIL
See Issue P-004 above (form labels not associated)

---

## Robust

### 4.1 Compatible

#### 4.1.2 Name, Role, Value (Level A) - FAIL

**Issue R-001: Custom Components Missing ARIA**
- **Severity:** High
- **Confidence:** High
- **Location:** Tabs, accordions, carousels throughout site
- **Evidence:**
  ```html
  <!-- Current: No ARIA roles -->
  <div class="tabs">
    <div class="tab active">Description</div>
    <div class="tab">Specifications</div>
  </div>
  <div class="panel">...</div>
  ```
- **Remediation:**
  ```html
  <div role="tablist">
    <button role="tab" aria-selected="true" aria-controls="panel-1">
      Description
    </button>
    <button role="tab" aria-selected="false" aria-controls="panel-2">
      Specifications
    </button>
  </div>
  <div role="tabpanel" id="panel-1">...</div>
  ```
- **Effort:** High

---

### Remediation Roadmap

#### Phase 1: Critical Barriers (Week 1-2)
| Issue | Action | Owner | Status |
|-------|--------|-------|--------|
| P-004 | Associate form labels | Dev | To Do |
| O-001 | Make filters keyboard accessible | Dev | To Do |
| O-003 | Fix modal focus trapping | Dev | To Do |
| O-005 | Restore focus indicators | Dev | To Do |

#### Phase 2: High Priority (Week 3-4)
| Issue | Action | Owner | Status |
|-------|--------|-------|--------|
| P-001 | Add alt text to product images | Content | To Do |
| P-005 | Fix color contrast issues | Design | To Do |
| O-002 | Fix custom dropdowns | Dev | To Do |
| O-004 | Add skip navigation link | Dev | To Do |
| R-001 | Add ARIA to custom components | Dev | To Do |

#### Phase 3: Medium Priority (Week 5-6)
| Issue | Action | Owner | Status |
|-------|--------|-------|--------|
| P-002 | Hide decorative icons | Dev | To Do |
| P-006 | Fix reflow issues at 400% | Dev | To Do |
| U-001 | Fix auto-submit behavior | Dev | To Do |
| U-002 | Associate error messages | Dev | To Do |

#### Phase 4: Content & Captions (Week 7-8)
| Issue | Action | Owner | Status |
|-------|--------|-------|--------|
| P-003 | Add video captions | Content | To Do |

---

### Appendix: Testing Matrix

| Browser | Screen Reader | Tested By | Date |
|---------|---------------|-----------|------|
| Chrome 120 | NVDA 2024.1 | Tester A | 2026-01-29 |
| Firefox 121 | NVDA 2024.1 | Tester A | 2026-01-29 |
| Safari 17 | VoiceOver | Tester B | 2026-01-29 |
| Edge 120 | Narrator | Tester B | 2026-01-29 |

### Success Criteria Checklist

| Criterion | Level | Status | Issues |
|-----------|-------|--------|--------|
| 1.1.1 Non-text Content | A | FAIL | P-001, P-002 |
| 1.2.2 Captions | A | FAIL | P-003 |
| 1.3.1 Info and Relationships | A | FAIL | P-004 |
| 1.3.2 Meaningful Sequence | A | PASS | - |
| 1.4.3 Contrast | AA | FAIL | P-005 |
| 1.4.4 Resize Text | AA | PASS | - |
| 1.4.10 Reflow | AA | FAIL | P-006 |
| 2.1.1 Keyboard | A | FAIL | O-001, O-002 |
| 2.1.2 No Keyboard Trap | A | FAIL | O-003 |
| 2.4.1 Bypass Blocks | A | FAIL | O-004 |
| 2.4.7 Focus Visible | AA | FAIL | O-005 |
| 3.1.1 Language of Page | A | PASS | - |
| 3.2.2 On Input | A | FAIL | U-001 |
| 3.3.1 Error Identification | A | FAIL | U-002 |
| 4.1.2 Name, Role, Value | A | FAIL | R-001 |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focused on WCAG compliance
- **ST-02 (Structured Sequential Instructions):** Systematic audit methodology
- **RT-02 (Multi-Dimensional Analysis):** POUR principles framework
- **RT-05 (Evidence-Based Reasoning):** Code evidence for each finding
- **DS-06 (Prioritization Guidance):** Phased remediation plan

## Related Prompts

- [frontend_accessibility_aria_patterns.md](frontend_accessibility_aria_patterns.md) - ARIA implementation
- [frontend_accessibility_screen_reader.md](frontend_accessibility_screen_reader.md) - Screen reader testing
- [testing_accessibility_wcag.md](../../domain-software-engineering/testing/testing_accessibility_wcag.md) - Testing strategy

## Customization Guide

- **For Legal Compliance**: Add specific ADA/Section 508/EN 301 549 mapping
- **For Mobile Apps**: Include WCAG 2.1 mobile-specific criteria (2.5.x)
- **For WCAG 2.2**: Add new criteria (2.4.11, 3.2.6, 3.3.7, etc.)
- **For AAA Target**: Extend checklist to include Level AAA criteria
