---
title: "Accessible Form Design & UX Audit"
category: frontend-development/forms
description: "Audit and design forms for accessibility: programmatic label association, error announcement, fieldset/legend grouping, required/invalid state semantics, keyboard operability, and well-timed inline validation."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - forms
  - accessibility
  - aria
  - labels
  - error-announcement
  - keyboard
  - screen-reader
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/forms/frontend_forms_validation_design.md
  - domain-frontend-development/accessibility/frontend_accessibility_aria_patterns.md
  - domain-frontend-development/accessibility/frontend_accessibility_screen_reader.md
  - domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md
---

# Accessible Form Design & UX Audit

**Objective:** Ensure a form is fully operable and understandable with a keyboard and screen reader — every control labeled, every error announced, required/invalid states conveyed programmatically, and validation timed so it helps rather than interrupts.

**When to Use:**
- Use when: Building or reviewing any form that collects user input (sign-up, checkout, settings, search, surveys).
- Use when: Errors are styled visually (red text/border) but not announced to assistive tech.
- Use when: Custom controls (comboboxes, date pickers, toggles) replace native inputs.
- Use when: Preparing for a WCAG audit and need the forms-specific slice.
- Don't use when: There is no user input on the page — this prompt is about form controls specifically.

## Instructions

1. **Audit Label Association**
   - Confirm every input has a programmatic label via `<label for>`/wrapping `<label>`, or `aria-label`/`aria-labelledby` for controls without visible text.
   - Flag placeholder-as-label (placeholders disappear on input and are not a reliable label).
   - For grouped controls (radios, checkbox sets), confirm `<fieldset>` + `<legend>` provide the group label.

2. **Audit Required and Invalid State Semantics**
   - Required fields: convey with `required`/`aria-required="true"`, not color or an asterisk alone; the asterisk needs a text legend.
   - Invalid fields: set `aria-invalid="true"` when in error and remove it when corrected.
   - Confirm error text is associated to the field via `aria-describedby` so the screen reader reads the input, its state, and its error together.

3. **Audit Error Announcement**
   - Inline errors that appear after submit/blur must be announced. Verify a live region (`role="alert"` or `aria-live="assertive"` for the summary; `aria-live="polite"` for incremental hints) or programmatic focus move.
   - On submit failure, confirm focus moves to the first invalid field or to an error summary that links to each field.
   - Confirm success/confirmation messages are also announced, not just shown.

4. **Audit Grouping and Structure**
   - Related fields grouped with `fieldset`/`legend`; multi-step forms expose step context (e.g., `aria-current`, headings, or a labeled progress indicator).
   - Confirm reading order and DOM order match the visual order so screen-reader and tab order are coherent.

5. **Audit Keyboard Operability**
   - Every control reachable and operable by keyboard; no keyboard traps.
   - Visible focus indicator on all interactive elements (do not remove `:focus` outlines without a replacement).
   - Custom widgets follow the expected key interactions (e.g., arrow keys in radio groups, Esc to close pickers) — cross-reference ARIA Authoring Practices.

6. **Audit Inline Validation Timing**
   - Validation should not fire on every keystroke before a field is touched; prefer on-blur or on-submit, then re-validate on change once errored.
   - Ensure errors are not announced repeatedly on each keystroke (debounce/avoid re-triggering the live region needlessly).
   - Confirm error messages are specific and actionable ("Enter a date in MM/DD/YYYY"), not generic ("Invalid").

7. **CRITICAL: Verify findings before reporting**
   - Verify announcements with an actual screen reader (or by inspecting the accessibility tree and live-region wiring), not by assuming `aria-*` attributes work.
   - Distinguish "attribute present" from "behaves correctly" — a misused `aria-live` can be silent.
   - **Confidence level** for each finding:
     - **High Confidence:** Reproduced with a screen reader or confirmed in the accessibility tree.
     - **Medium Confidence:** Markup strongly implies correct behavior but not AT-verified.
     - **Low Confidence:** Inferred from code; flagged for manual AT testing.

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Treat a placeholder as a label — it fails when the field has a value and has poor contrast.
- Convey required/error state with color or an asterisk alone (color is not programmatic; WCAG 1.4.1).
- Add `aria-live` regions and assume they announce — wrong politeness or a hidden region stays silent.
- Announce errors on every keystroke; it floods the screen reader and annoys users.
- Use `aria-label` where a visible label exists (creates a mismatch for voice-control users).
- Remove focus outlines without providing a clearly visible replacement.
- Assume custom widgets are accessible because they look right; verify keyboard and AT behavior.

✅ **DO:**
- Pair every input with a programmatic label and associate errors via `aria-describedby`.
- Convey required/invalid with `required`/`aria-required` and `aria-invalid`, plus visible text.
- Move focus to the first invalid field (or a linked error summary) on submit failure.
- Use `polite` for incremental hints and `assertive`/`role="alert"` for blocking errors.
- Group related controls in `fieldset`/`legend`.
- Keep DOM order aligned with visual order and maintain visible focus.
- Verify announcements with a real screen reader before signing off.

## Expected Output

An accessibility audit/design report for the form covering:
- Label association and grouping findings.
- Required/invalid state semantics.
- Error-announcement mechanism and submit focus behavior.
- Keyboard operability findings.
- Inline validation timing assessment.
- Prioritized, WCAG-referenced remediations.

### Output Format

```markdown
## Form Accessibility Audit: [Form Name]

### Summary
[Overall state, WCAG level targeted]

### Findings

| ID | Issue | WCAG SC | Severity | Confidence | Location | Evidence | Recommendation |
|----|-------|---------|----------|------------|----------|----------|----------------|

### Label & Grouping
[Details]

### State Semantics (required/invalid)
[Details]

### Error Announcement & Focus
[Details]

### Keyboard
[Details]

### Validation Timing
[Details]

### Prioritized Remediations
1. ...
```

## Example Output

```markdown
## Form Accessibility Audit: Checkout — Shipping Details

### Summary
Form is visually clear but fails screen-reader users on three counts: errors are not announced, required state is color-only, and the city/state group lacks a programmatic label. Target: WCAG 2.2 AA.

### Findings

| ID | Issue | WCAG SC | Severity | Confidence | Location | Evidence | Recommendation |
|----|-------|---------|----------|------------|----------|----------|----------------|
| A1 | Inline errors shown but not announced | 4.1.3, 3.3.1 | High | High | `ShippingForm.tsx` error spans | Errors render in a `<span class="error">` with no live region or `aria-describedby` | Wire `aria-describedby` to each input and add `role="alert"` to the error container |
| A2 | Required conveyed by red asterisk only | 1.4.1, 3.3.2 | High | High | label markup | `<span class="req">*</span>`, no `aria-required`, no legend | Add `aria-required="true"` and a "* indicates required" legend |
| A3 | Placeholder used as label on "Apt/Unit" | 1.3.1, 3.3.2 | Medium | High | input `placeholder="Apt/Unit"` | No `<label>`; placeholder vanishes on input | Add a visible `<label>` |
| A4 | City/State/ZIP not grouped | 1.3.1 | Medium | Medium | address fieldset | Three inputs with no `fieldset`/`legend` for "Address" | Wrap in `<fieldset><legend>Address</legend>` |
| A5 | Focus not moved to first error on submit | 3.3.1, 2.4.3 | Medium | High | submit handler | Submit reveals errors but leaves focus on button | Move focus to first invalid field |
| A6 | Error validates on every keystroke from empty | 3.3.1 | Low | Medium | `onChange` validation | ZIP announces "Invalid ZIP" while typing | Validate on blur, then on change after first error |

### Label & Grouping
Most inputs have associated `<label>`s. Exceptions: A3 (placeholder-as-label) and A4 (ungrouped address block). Recommend `fieldset`/`legend` for the address group and a real label for Apt/Unit.

### State Semantics (required/invalid)
No `aria-invalid` is toggled when fields error (screen reader announces the field as valid). Required state is color-only (A2). Add `aria-invalid="true"` on error and clear it on correction.

### Error Announcement & Focus
No live region exists, so error appearance is silent to AT users (A1). On submit, add an error summary at the top with `role="alert"` linking to each field, and move focus to the first invalid field (A5).

### Keyboard
All native inputs are reachable; tab order matches visual order. Focus outline is intact. No keyboard traps found. (No findings.)

### Validation Timing
ZIP validates on every keystroke from empty, announcing errors mid-typing (A6). Switch to blur-first, change-after-error to reduce noise.

### Prioritized Remediations
1. **A1 — Announce errors (live region + `aria-describedby`).** Without it, AT users cannot perceive errors at all.
2. **A2 — Programmatic required state + legend.** Color-only required state excludes color-blind and AT users.
3. **A5 — Move focus to first invalid field on submit.** Users land where the problem is.
4. **A3/A4 — Real label and address grouping.** Restores field context.
5. **A6 — Re-time inline validation.** Stops mid-typing error floods.
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Defines the goal — keyboard- and screen-reader-operable forms with announced errors.
- **ST-02 (Structured Sequential Instructions):** Sequences labels → state → announcement → grouping → keyboard → timing.
- **RT-02 (Multi-Dimensional Analysis Framework):** Assesses each control across label, state, announcement, keyboard, and timing dimensions.
- **RT-05 (Evidence-Based Reasoning):** Each finding cites WCAG success criteria, location, and concrete evidence.
- **DS-06 (Prioritization Guidance):** Orders remediations by user impact (perception-blocking first).

## Related Prompts

- [frontend_forms_validation_design.md](frontend_forms_validation_design.md) - The validation logic whose errors this prompt makes accessible
- [../accessibility/frontend_accessibility_aria_patterns.md](../accessibility/frontend_accessibility_aria_patterns.md) - ARIA patterns for custom form widgets
- [../accessibility/frontend_accessibility_screen_reader.md](../accessibility/frontend_accessibility_screen_reader.md) - Verifying announcements with real screen readers
- [../accessibility/frontend_accessibility_wcag_audit.md](../accessibility/frontend_accessibility_wcag_audit.md) - Full-page WCAG audit that this forms slice feeds into
