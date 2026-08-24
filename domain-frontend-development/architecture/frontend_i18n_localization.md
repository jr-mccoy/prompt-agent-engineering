---
title: "Internationalization & Localization Architecture"
category: frontend-development/architecture
description: "Design and audit frontend i18n/l10n: message extraction, ICU plural/gender handling, RTL support, locale-aware formatting, lazy-loaded locale bundles, and pseudo-localization testing."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - i18n
  - localization
  - icu-messageformat
  - rtl
  - locale-formatting
  - pseudo-localization
  - architecture
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/architecture/frontend_state_management_selection.md
  - domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md
  - domain-frontend-development/performance/frontend_performance_bundle_optimization.md
  - domain-frontend-development/forms/frontend_forms_accessibility_ux.md
---

# Internationalization & Localization Architecture

**Objective:** Make the frontend translatable and locale-correct — strings externalized and extractable, plurals/gender handled via ICU, layouts that survive RTL and text expansion, locale-aware number/date/currency formatting, and locale bundles that load efficiently.

**When to Use:**
- Use when: Adding a second language/locale to an app that was built English-only.
- Use when: Auditing an i18n setup for hardcoded strings, broken plurals, or RTL breakage.
- Use when: Designing the message catalog, extraction pipeline, and locale-loading strategy.
- Use when: Formatting dates/numbers/currency that currently use hardcoded or US-only formats.
- Don't use when: The product is permanently single-locale with no formatting concerns — i18n machinery would be overhead.

## Instructions

1. **Audit for Hardcoded and Concatenated Strings**
   - Scan for user-facing text embedded directly in markup/JS instead of referenced from a message catalog.
   - Flag string concatenation that assembles sentences from fragments (word order differs across languages) — these must become single parameterized messages.
   - Confirm a stable message ID/key scheme so extraction is deterministic.

2. **Audit Plurals, Gender, and Interpolation (ICU)**
   - Confirm plural-sensitive messages use ICU `plural` (not `count === 1 ? "item" : "items"`), since languages have more than two plural categories.
   - Confirm gendered/select cases use ICU `select`.
   - Verify interpolated values (names, counts, dates) are passed as arguments, not concatenated, and are themselves formatted per locale.

3. **Audit Locale-Aware Formatting**
   - Numbers, currency, dates, times, relative times, and lists must use locale-aware formatting (e.g., `Intl.*` APIs) rather than hardcoded patterns.
   - Confirm currency includes the correct symbol/placement and that time zones are handled for dates.
   - Flag manual `toLocaleString` calls that omit an explicit locale (rely on environment default).

4. **Audit RTL and Layout Resilience**
   - Confirm the app can render right-to-left (e.g., `dir="rtl"`, logical CSS properties like `margin-inline-start` instead of `margin-left`, mirrored icons where directional).
   - Verify layouts tolerate text expansion (many languages run 30–40%+ longer than English) without truncation or overflow.
   - Check that bidirectional content (mixed LTR/RTL) is handled.

5. **Audit the Extraction & Catalog Pipeline**
   - Confirm there's an extraction step that pulls keys from source into catalogs, and a way to detect missing/orphaned keys.
   - Confirm a fallback-locale strategy for untranslated keys (and whether missing keys are surfaced in dev).
   - Verify translator context (descriptions/placeholders) accompanies keys.

6. **Audit Locale Bundle Loading**
   - Confirm locale message bundles are code-split/lazy-loaded so users download only their active locale, not all languages.
   - Verify the active locale's data (and any `Intl` polyfill/locale-data, if used) loads before first paint of translated content to avoid flashes of keys/English.
   - Account for bundle-size budget across locales.

7. **Audit Testing (Pseudo-Localization)**
   - Confirm a pseudo-localization mode exists (accented/expanded text, bracketed strings) to surface hardcoded strings, truncation, and concatenation before real translation.
   - Confirm an RTL smoke test and a longest-string layout check.

8. **CRITICAL: Verify findings before reporting**
   - Confirm hardcoded strings by grepping rendered text, not by assuming all text is externalized.
   - Verify plural/format behavior against actual locale rules rather than English intuition; note where locale data must be verified against current docs.
   - **Confidence level** for each finding:
     - **High Confidence:** Confirmed in source (hardcoded string located, ICU missing, RTL break reproduced).
     - **Medium Confidence:** Strong indicator but not exhaustively traced.
     - **Low Confidence:** Inferred; flagged for locale/QA verification.

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Assemble sentences by concatenating translated fragments — word order varies by language.
- Use `count === 1` two-form plural logic — many languages have more than two plural categories; use ICU `plural`.
- Hardcode date/number/currency formats or call `toLocaleString` without an explicit locale.
- Use physical CSS (`margin-left`, `text-align: left`) where logical properties are needed for RTL.
- Ship all locale bundles to every user; that bloats the bundle.
- Assume layouts that fit English fit every language — text expansion overflows.
- Treat translation as done without translator context/descriptions for keys.

✅ **DO:**
- Externalize every user-facing string with a stable key and a single parameterized message per sentence.
- Use ICU `plural`/`select` for counts and gender.
- Format numbers/dates/currency/lists with locale-aware `Intl.*` APIs and explicit locales.
- Use `dir` and logical CSS properties; test RTL and bidi content.
- Lazy-load only the active locale's bundle; budget across locales.
- Run pseudo-localization to catch hardcoded strings, truncation, and concatenation early.
- Verify hardcoded strings and plural rules in source rather than assuming.

## Expected Output

An i18n/l10n architecture or audit report including:
- Hardcoded/concatenated string findings.
- Plural/gender/interpolation (ICU) assessment.
- Locale-aware formatting assessment.
- RTL and text-expansion resilience.
- Extraction/catalog and lazy-loading strategy.
- Pseudo-localization testing coverage.
- Prioritized remediations.

### Output Format

```markdown
## i18n/l10n Audit: [App/Feature]

### Findings

| ID | Issue | Category | Severity | Confidence | Location | Evidence | Recommendation |
|----|-------|----------|----------|------------|----------|----------|----------------|

### Strings & Extraction
[Assessment]

### Plurals / Gender / Interpolation (ICU)
[Assessment]

### Locale-Aware Formatting
[Assessment]

### RTL & Text Expansion
[Assessment]

### Bundle Loading
[Assessment]

### Pseudo-Localization Testing
[Assessment]

### Prioritized Remediations
1. ...
```

## Example Output

```markdown
## i18n/l10n Audit: E-Commerce Storefront (adding Arabic + German)

### Findings

| ID | Issue | Category | Severity | Confidence | Location | Evidence | Recommendation |
|----|-------|----------|----------|------------|----------|----------|----------------|
| I1 | Hardcoded English strings in product cards | Strings | High | High | `ProductCard.tsx` | `<span>Add to cart</span>` literal | Externalize to catalog with key `product.addToCart` |
| I2 | Cart count uses `count === 1 ? 'item' : 'items'` | Plurals | High | High | `CartBadge.tsx` | Two-form logic breaks for Arabic (6 forms) | Use ICU `plural` message |
| I3 | Sentence built by concatenation | Strings | High | High | `Greeting.tsx` | `"Hi " + name + ", you have " + n + " orders"` | Single ICU message with `{name}` and `{n, plural, ...}` |
| I4 | Prices formatted as `"$" + value.toFixed(2)` | Formatting | High | High | `Price.tsx` | Hardcoded `$`, no locale | `Intl.NumberFormat(locale, { style: 'currency', currency })` |
| I5 | Layout uses `margin-left`/`text-align: left` | RTL | High | Medium | global styles | Breaks under `dir="rtl"` (Arabic) | Switch to logical properties; add RTL smoke test |
| I6 | All 3 locale bundles shipped to every user | Bundle | Medium | High | i18n init | German + Arabic loaded for English users | Lazy-load active locale bundle |
| I7 | German labels overflow buttons | Expansion | Medium | Medium | nav/buttons | Longer German text truncates | Allow wrapping / flexible widths; test with longest strings |
| I8 | No pseudo-localization mode | Testing | Medium | High | build config | No way to catch hardcoded strings pre-translation | Add pseudo-locale (accented + expanded + bracketed) |
| I9 | Dates shown as `MM/DD/YYYY` for all locales | Formatting | Medium | High | `OrderDate.tsx` | US format for German users | `Intl.DateTimeFormat(locale)` |

### Strings & Extraction
Multiple hardcoded strings (I1) and a concatenated sentence (I3). Stand up an extraction step that pulls keys into per-locale catalogs and flags missing keys; attach translator descriptions.

### Plurals / Gender / Interpolation (ICU)
Replace two-form plural logic with ICU `plural` (I2) — Arabic requires up to six categories. Convert concatenated greeting to one ICU message (I3).

### Locale-Aware Formatting
Currency (I4) and dates (I9) are US-hardcoded. Use `Intl.NumberFormat`/`Intl.DateTimeFormat` with the active locale and correct currency; verify currency placement per locale against current docs.

### RTL & Text Expansion
Physical CSS breaks RTL (I5); migrate to logical properties and add a `dir="rtl"` smoke test. German expansion overflows (I7); make widths flexible and test with longest strings.

### Bundle Loading
All locales are bundled for everyone (I6); code-split so users fetch only their active locale, and load it before rendering translated content to avoid a flash of keys.

### Pseudo-Localization Testing
No pseudo-locale (I8). Add one to surface hardcoded strings, truncation, and concatenation before real translation work begins.

### Prioritized Remediations
1. **I1 & I3 — Externalize strings; eliminate concatenation.** Foundation for any translation.
2. **I2 — ICU plurals.** Prevents grammatically broken counts in target locales.
3. **I4 & I9 — Locale-aware currency/date formatting.** Core correctness for German/Arabic users.
4. **I5 — RTL via logical properties.** Required for Arabic.
5. **I6 — Lazy-load locale bundles.** Removes cross-locale bundle bloat.
6. **I8 & I7 — Pseudo-localization + expansion testing.** Catches the rest before translators are involved.
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Sets the goal — translatable, locale-correct, RTL-safe UI.
- **ST-02 (Structured Sequential Instructions):** Sequences strings → ICU → formatting → RTL → pipeline → loading → testing.
- **RT-02 (Multi-Dimensional Analysis Framework):** Assesses each area across correctness, layout, performance, and testability.
- **RT-05 (Evidence-Based Reasoning):** Every finding cites the offending source and the locale rule it violates.
- **DS-06 (Prioritization Guidance):** Orders fixes from foundational (externalization) to refinement (pseudo-loc testing).

## Related Prompts

- [frontend_state_management_selection.md](frontend_state_management_selection.md) - Where active-locale state lives in the app
- [../accessibility/frontend_accessibility_wcag_audit.md](../accessibility/frontend_accessibility_wcag_audit.md) - `lang`/`dir` attributes and language-of-parts as WCAG concerns
- [../performance/frontend_performance_bundle_optimization.md](../performance/frontend_performance_bundle_optimization.md) - Code-splitting locale bundles
- [../forms/frontend_forms_accessibility_ux.md](../forms/frontend_forms_accessibility_ux.md) - Localizing form labels and error messages
