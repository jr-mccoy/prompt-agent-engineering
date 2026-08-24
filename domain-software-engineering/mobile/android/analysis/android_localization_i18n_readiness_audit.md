---
title: "Android Localization & i18n Readiness Audit"
category: mobile-development
description: "Audits an Android app's readiness for localization and internationalization: hardcoded strings, plurals, locale-aware formatting, RTL support, text expansion, and string-resource hygiene, with prioritized fixes."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - QA-02
difficulty: intermediate
tags:
  - android
  - localization
  - i18n
  - l10n
  - rtl
  - strings
  - analysis
  - mobile-development
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_resource_asset_analysis.md
  - domain-software-engineering/mobile/android/analysis/android_accessibility_audit.md
  - domain-software-engineering/mobile/android/analysis/android_compose_ui_consistency_audit.md
---

# Android Localization & i18n Readiness Audit

**Objective:** Audit an Android codebase for internationalization (i18n) readiness and localization (l10n) correctness — hardcoded user-facing strings, plural/quantity handling, locale-aware date/number/currency formatting, right-to-left (RTL) support, text-expansion resilience, and string-resource hygiene — reporting issues with `file:line` evidence and concrete fixes.

**When to Use:** Use this before adding new locales, when planning international launch, after a UI rewrite, or when translators report context/format problems. Even single-locale apps benefit (accessibility, future-proofing, format correctness). Covers Compose and View/XML UIs.

---

## Context Gathering

1. **Target locales:** "Which languages/regions are planned, current, or required? Any RTL locales?"
2. **Current state:** "Are there `values-xx/` resource folders today? Any translation pipeline (TMS, Weblate, Crowdin)?"
3. **Formats:** "Does the app show dates, times, numbers, currencies, or measurements?"
4. **Constraints:** "Any fixed-width UI elements or design constraints that limit text expansion?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Confirm the string is user-facing** — log messages, exception text, analytics keys, and internal tags do not need translation. Cite `file:line`.
2. **Check for an existing resource** — a literal may be a fallback already mirrored in `strings.xml`; verify before flagging.
3. **Verify format-correctness impact** — `String.format`/concatenation is a problem when it affects locale-sensitive output or word order, not for non-linguistic assembly.
4. **Distinguish readiness from translation** — the audit assesses whether the app *can* be localized correctly, not whether translations exist.

**A localization-ready codebase is an acceptable outcome.** Don't over-flag.

### False-Positive Prevention

- ❌ Do NOT flag debug logs, exception messages, test data, or analytics/event names.
- ❌ Do NOT flag technical literals (URLs, MIME types, keys, format patterns) as untranslated.
- ❌ Do NOT flag English-only apps for *missing translations* — flag i18n-*readiness* defects instead.
- ❌ Do NOT demand `start`/`end` where `left`/`right` is genuinely intended (rare, e.g., a fixed compass UI).
- ✅ DO flag user-visible literals in Kotlin/Compose/XML.
- ✅ DO flag manual pluralization (`if (n==1) "item" else "items"`).
- ✅ DO flag concatenation that breaks word order across languages.

---

### Phase 1: Localization Surface Inventory

| Item | What to Locate |
|------|----------------|
| String resources | `strings.xml` and `values-*/` locale folders present |
| Hardcoded strings | Literals in Compose (`Text("…")`), XML (`android:text="…"`), and Kotlin |
| Plurals | `<plurals>` usage vs manual count branching |
| Formatting | `SimpleDateFormat`, `DecimalFormat`, `String.format`, manual concatenation |
| RTL config | `android:supportsRtl`, `start`/`end` vs `left`/`right`, directional drawables |
| Locale handling | `Locale.getDefault()` usage, per-app language (`AppCompatDelegate`/`LocaleManager`) |

---

### Phase 2: String Externalization & Resource Hygiene

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Hardcoded user-facing strings | HIGH | Literals in UI that should be `stringResource`/`@string` |
| Manual pluralization | HIGH | Count-based string branching instead of `<plurals>`/`pluralStringResource` |
| Concatenation word order | HIGH | `"$count " + label` or `getString(a) + getString(b)` breaking grammar |
| Missing placeholders | MEDIUM | Positional args without indices (`%1$s`) for reorderable text |
| Untranslatable marking | LOW | Constant strings not marked `translatable="false"` (noise for translators) |
| Missing context | LOW | No comments for ambiguous strings translators will misread |

---

### Phase 3: Formatting & Locale Correctness

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Hardcoded date/time format | HIGH | `SimpleDateFormat("MM/dd/yyyy")` instead of locale-aware `DateFormat`/`DateTimeFormatter` |
| Number/currency format | HIGH | Manual decimal/currency formatting ignoring locale separators/symbols |
| Forced `Locale.US`/ROOT misuse | MEDIUM | Locale.ROOT for display text, or default locale for machine formats (inconsistent) |
| Measurement units | LOW | Imperial/metric not adapted by region |

---

### Phase 4: RTL & Text-Expansion Resilience

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| RTL layout | HIGH | `left`/`right` constraints/padding instead of `start`/`end`; `supportsRtl` off |
| Directional assets | MEDIUM | Back/forward/chevron icons not auto-mirrored (`autoMirrored`) |
| Text expansion | MEDIUM | Fixed-width/`maxLines=1` containers that clip longer translations |
| Bidi handling | LOW | User content mixing LTR/RTL without isolation |

---

## Output Format

```markdown
## Android Localization & i18n Readiness Audit Report

### Readiness Summary
| Dimension | Rating (Ready / Partial / Not Ready) | Notes |
|-----------|--------------------------------------|-------|
| String externalization | | |
| Plurals & grammar | | |
| Locale-aware formatting | | |
| RTL & text expansion | | |

### Findings (severity-ordered)
**[SEVERITY] Dimension: title** — Location `file:line` · Issue · Fix

### Hardcoded String Hotspots
| File | Approx. count | Example |
|------|---------------|---------|

### Prioritized Remediation (P1/P2/P3)
```

---

## Expected Output

1. **Readiness summary** across four dimensions.
2. **Severity-rated findings** with locations and fixes.
3. **Hardcoded-string hotspot** map.
4. **Prioritized remediation.**

---

## Techniques Used

- **ST-01** (Clear Objective): i18n/l10n readiness scope.
- **ST-02** (Structured Sequential Instructions): Inventory → strings → formatting → RTL.
- **RT-02** (Multi-Dimensional Analysis): Grammar + format + layout angles.
- **RT-05** (Evidence-Based Reasoning): `file:line` citations.
- **DS-06** (Prioritization Guidance): Severity ordering.
- **QA-02** (Edge Case Coverage): RTL, plurals, text expansion, bidi.

---

## Related Prompts

- [android_resource_asset_analysis.md](android_resource_asset_analysis.md) - Resource folder/qualifier hygiene
- [android_accessibility_audit.md](android_accessibility_audit.md) - Text scaling and screen-reader overlap
- [android_compose_ui_consistency_audit.md](android_compose_ui_consistency_audit.md) - Layout invariance under longer text
