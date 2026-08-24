---
title: "Android Compose UI Consistency Audit (Typography, Size, Spacing, Cross-Theme Invariance)"
category: mobile-development
description: "Audit a Kotlin + Jetpack Compose Android app for UI consistency in typography, element/component sizes, and spacing — with explicit cross-theme invariance checks so layout never drifts between themes (only color/elevation should vary)."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - RT-05
  - DS-06
  - AG-01
difficulty: intermediate
tags:
  - android
  - kotlin
  - jetpack-compose
  - ui-consistency
  - typography
  - spacing
  - design-system
  - themes
  - analysis
updated: "2026-05-19"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_theme_investigation.md
  - domain-software-engineering/mobile/android/analysis/android_compose_ui_analysis.md
  - domain-software-engineering/mobile/android/targeted-reviews/android_overbroad_ui_updates_review.md
  - domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md
---

# Android Compose UI Consistency Audit

## Objective

Audit a Kotlin + Jetpack Compose Android app for **UI consistency** across three orthogonal dimensions — **typography**, **element/component sizing**, and **spacing** — and verify that these dimensions remain **invariant across themes** (light, dark, dynamic/Material You, and any custom themes). Color, elevation surface tint, and state colors are *expected* to vary by theme; font sizes, line heights, component heights, icon sizes, paddings, margins, and corner radii must **not**.

Output is an evidence-based report: every finding cites `file:line`, every recommendation references a specific token or component. The audit does not modify code.

---

## When to Use

- The app has been built incrementally and you suspect drift in typography scale, paddings, or component sizes between screens.
- You're shipping new themes (or Material You / dynamic color) and want to confirm layout doesn't shift when the theme changes.
- You're consolidating ad-hoc `dp`/`sp` literals into a design-system token layer (typography, spacing, shape, dimension).
- You're preparing for an accessibility audit and need to confirm font scaling and minimum touch targets behave consistently.
- You're onboarding a new design system / Material 3 migration and need a baseline of current inconsistencies.

**Not for:** debugging stubborn color bugs (use `android_theme_investigation.md`), or full Compose architecture review (use `android_compose_ui_analysis.md`).

---

## Inputs / Context

Ask the user, then proceed:

1. **App scope:** "Path to the repo root? Is the app Compose-only or hybrid (Compose + XML Views)?"
2. **Design system:** "Do you have a documented design system, type scale, or spacing token set? If yes, where is it defined (Compose `Typography`, custom `Tokens.kt`, Figma reference, etc.)?"
3. **Themes in scope:** "Which themes should I treat as 'must be layout-invariant'? (Examples: light, dark, dynamic color, brand A, brand B, high-contrast.)"
4. **Font scaling:** "Should I check behavior under user font-scale changes (1.0×, 1.3×, 2.0×)?"
5. **Modules:** "Single-module or multi-module? If multi-module, which modules are in scope?"
6. **Known pain points:** "Are there screens or components you already suspect are inconsistent?"

If the user cannot answer a question, mark that section of the audit as **assumption-based** and proceed.

---

## Constraints

### Must
- Cite **exact `file:line`** for every finding, hardcoded value, and recommendation.
- Distinguish **intentional variation** (e.g., a marketing splash with deliberately oversized type) from **drift** (e.g., body text using 14sp in one screen and 15sp in another).
- Treat **theme-invariance** as a first-class check: explicitly verify that typography, spacing, sizing, and shape tokens resolve to the **same numeric value** under every in-scope theme. Color, container tint, elevation overlays, and state colors are out of scope here.
- Distinguish **`sp` (typography, scales with user font size)** from **`dp` (everything else)**. Flag misuse (e.g., `sp` on padding, `dp` on text size).
- Report **counts and exemplars**, not exhaustive grep dumps — e.g., "37 hardcoded paddings; representative offenders: `HomeScreen.kt:88`, `SettingsRow.kt:42`."
- Group findings by **severity** (Critical / High / Medium / Low) and **fix complexity** (Mechanical / Localized refactor / Cross-cutting refactor).
- Produce the report in the exact structure given in **Output Format** below.

### Must Not
- Do **not** modify code. This prompt is read-only.
- Do **not** flag color, elevation, or state-color differences between themes as inconsistencies — those belong in a theme audit.
- Do **not** invent design-system tokens that don't exist. If there's no token layer, recommend creating one and proceed without pretending one exists.
- Do **not** assume the Material 3 default typography/shape scales are in use — verify by reading the actual `Typography` and `Shapes` definitions.
- Do **not** flag a single-screen deviation as systemic without at least one peer screen showing the canonical pattern.
- Do **not** report theoretical issues without an observable artifact (a file, a literal, a screenshot description, or a token mismatch).
- Do **not** count `Modifier.padding(MaterialTheme...)` token references as hardcoded literals — only flag bare `dp`/`sp` numbers and `Color(0x...)`-style literals where applicable.

---

## Instructions

Execute in phases. Do not proceed to the next phase until the current one is complete.

### Phase 1 — Token & Scale Discovery

Locate the **source of truth** for each dimension. For each, capture: file path, defined values, and whether it's used consistently.

**Typography**
- Find the Compose `Typography` definition (commonly `ui/theme/Type.kt` or similar). Enumerate every `TextStyle`: name, `fontSize`, `lineHeight`, `letterSpacing`, `fontWeight`, `fontFamily`.
- Find any custom typography tokens (e.g., `AppTypography`, `BrandType`).
- Find any non-Material `FontFamily` declarations and where they're applied.

**Dimensions (spacing & sizing)**
- Find Compose dimension tokens (e.g., `Spacing.kt`, `Dimens.kt`, `object Sizes { val ... }`).
- If hybrid app, find `res/values/dimens.xml` and any qualifier variants (`values-sw600dp`, `values-night`, etc.).
- Document the scale (e.g., 4/8/12/16/24/32) or note its absence.

**Shapes**
- Find `Shapes.kt` / `MaterialTheme.shapes` overrides. Document corner sizes per role (small/medium/large/extra-large).

**Theme entry points**
- Find every `MaterialTheme { ... }` call and every custom `AppTheme { ... }` wrapper. Note which themes they switch between (light/dark/dynamic/brand).

Output of Phase 1: **Token Inventory** table.

---

### Phase 2 — Typography Consistency Audit

For typography, check:

1. **Scale coverage.** Are there `TextStyle`s defined but never used? Used but not defined (i.e., constructed inline)?
2. **Inline `TextStyle(...)` constructions.** Find every `Text(... style = TextStyle(...))` and every `MaterialTheme.typography.bodyLarge.copy(fontSize = ...)`. Each is a potential drift source.
3. **Hardcoded `sp` values.** `grep` for `\.sp` literals in `*.kt` outside the typography definition file. Group by value (e.g., "14.sp appears in 22 files; 15.sp in 4; 16.sp in 31").
4. **Font weight inconsistency.** Same logical role (e.g., "section header") rendered with different weights across screens.
5. **Font family inconsistency.** Multiple `FontFamily` instances used for the same role, or system default leaking in where a brand font is expected.
6. **Line-height & letter-spacing drift.** Inline overrides of `lineHeight` or `letterSpacing` that bypass the scale.
7. **`Text` without a `style`.** Calls that rely on `LocalTextStyle.current` — verify the parent context is the intended style.
8. **Role-to-style mapping.** For each repeated UI role (screen title, list item primary text, list item secondary text, button label, caption, error text), list the styles actually used and flag any role with >1 style.

Output: **Typography Consistency** section with role-to-style table and offender list.

---

### Phase 3 — Element & Component Size Consistency Audit

Check that components that should be the same size **are** the same size, across screens:

1. **Touch target / control heights.** Buttons, icon buttons, list rows, app bar height, bottom-nav height, FAB sizes, switches, checkboxes. Compare across screens. Flag anything below 48dp touch target as accessibility-critical.
2. **Icon sizes.** `Icon(... modifier = Modifier.size(...))` calls — group by site (toolbar leading, toolbar trailing, list row leading, inline emphasis). Flag inconsistent sizes within the same site.
3. **Image / thumbnail / avatar sizes.** Group by semantic role; flag drift.
4. **Card / surface / container widths and heights.** Especially flag fixed widths/heights set with `.size(...)` or `.height(...)` that should be intrinsic.
5. **Divider thickness, indicator widths, progress bar heights.**
6. **Corner radii used on the same component class.** Two card components with different `RoundedCornerShape(8.dp)` vs `RoundedCornerShape(12.dp)` for the same semantic role.
7. **Inline `.dp` for sizing.** Count hardcoded `dp` literals used for sizing (height, width, size, minSize) outside the dimensions token file.

Output: **Element Size Consistency** section with role-to-size table and offender list.

---

### Phase 4 — Spacing Consistency Audit

Check padding/margin/arrangement values:

1. **`Modifier.padding(...)`, `Modifier.padding(horizontal = ..., vertical = ...)`, `PaddingValues(...)`** — count literals and group by value. Identify the de-facto spacing scale in use; compare to the documented scale (or absence thereof).
2. **`Arrangement.spacedBy(...)` and `Spacer(Modifier.height/width(...))`** — same drill.
3. **Edge insets / screen gutters.** Top-level screen padding should be consistent. Flag screens that diverge from the dominant value.
4. **Section spacing.** Distance between a section header and its content; between list items; between cards. Group by semantic role and flag drift.
5. **Off-scale values.** Any `dp` value not on the documented (or inferred) scale of 4 — e.g., `5.dp`, `7.dp`, `13.dp` — flag as anomaly.
6. **WindowInsets handling.** Note whether screens consistently use `Modifier.windowInsetsPadding(...)` / `safeContentPadding` or mix approaches; mismatch causes visible top/bottom inset drift between screens.

Output: **Spacing Consistency** section with scale histogram and offender list.

---

### Phase 5 — Cross-Theme Invariance Check (the core ask)

For each theme in scope (light, dark, dynamic, brand A, brand B, high-contrast), verify that **layout-affecting tokens resolve to the same value**.

1. **Typography invariance.** Does any code path conditionally pick a different `fontSize`, `fontWeight`, `lineHeight`, or `fontFamily` based on theme, dark mode (`isSystemInDarkTheme()`), or dynamic color? Grep for `isSystemInDarkTheme`, `LocalConfiguration`, and theme-conditional branches — flag every place a typography property forks on theme.
2. **Dimension invariance.** Same for spacing/sizing tokens. A `dp` value must not depend on theme.
3. **Shape invariance.** Corner radii should not change between themes (unless explicitly part of the brand difference and documented).
4. **Density / FontScale handling.** Confirm components don't hardcode `dp` that should be `sp` (text-sized backgrounds, icon-with-text rows). Test reasoning under `fontScale = 1.3` and `2.0` — note components that will visibly clip or overflow.
5. **Layout-invariance smoke test.** Recommend a `@Preview` matrix (per screen × per theme) the team can adopt for regression. Sketch one as an example.

Output: **Cross-Theme Invariance** section. For each token category, state: **invariant / forks under condition X / unverified**. Every fork must cite `file:line`.

---

### Phase 6 — Component-Level Synthesis

For each high-traffic component class (Button, ListItem, Card, AppBar, BottomNav, FAB, TextField, Dialog), produce a one-row summary:

| Component | Variants found | Canonical (most used) | Outliers (file:line) | Recommendation |
| --- | --- | --- | --- | --- |
| Button | 3 (filled, tonal, custom-inline) | filled (M3 default) | `OnboardingScreen.kt:142` custom-inline | Adopt M3 filled; remove custom |

---

### Phase 7 — False-Positive Prevention Sweep

Before finalizing, re-check each finding against this filter:

- Is the deviation **intentional** (designed marketing surface, hero screen, splash)? → Move to "Intentional Variations" appendix, not the offender list.
- Is the file **third-party / generated**? → Exclude.
- Is the file in `androidTest` / `test` / sample / demo code? → Exclude unless the user said otherwise.
- Is the value off-scale because it's an inset compensation (e.g., `1.dp` hairline divider)? → Keep as a known-correct outlier.
- Does the "inconsistency" actually represent two different semantic roles that happen to look similar? → Re-classify, don't merge.

---

## Output Format

Produce a single Markdown report with this exact structure:

```markdown
# Android Compose UI Consistency Audit — <App Name>

## 0. Audit Scope
- Repo path, modules in scope, themes in scope, font-scale range checked.
- Assumptions made and where (call out unanswered inputs).

## 1. Executive Summary
| Dimension | Health | Critical findings | Hardcoded literals |
| --- | --- | --- | --- |
| Typography | Clean / Mixed / Fragmented | N | N `sp` outside Type.kt |
| Element sizes | ... | ... | ... |
| Spacing | ... | ... | ... |
| Cross-theme invariance | Invariant / Forks present | ... | ... |

Top 3 findings (one sentence each, with `file:line`).

## 2. Token Inventory
- Typography: list of defined TextStyles with values.
- Dimensions: token set or "absent".
- Shapes: corner radii by role.
- Theme entry points: list with `file:line`.

## 3. Typography Consistency
- Role → style mapping table.
- Hardcoded `.sp` histogram.
- Inline `TextStyle(...)` / `.copy(fontSize=...)` offenders.
- Font weight / family drift offenders.

## 4. Element Size Consistency
- Role → size mapping table.
- Touch-target violations (<48dp).
- Icon size site-by-site comparison.
- Hardcoded sizing `.dp` literals (count + top offenders).

## 5. Spacing Consistency
- Inferred or documented scale.
- Histogram of `.dp` values used as spacing.
- Off-scale anomalies.
- Screen gutter / inset handling consistency.

## 6. Cross-Theme Invariance
For each token category, one row:
| Category | Status (Invariant / Forks / Unverified) | Forks observed (file:line) |
| --- | --- | --- |

Include the recommended `@Preview` matrix sketch.

## 7. Component-Level Synthesis
The table from Phase 6.

## 8. Findings & Recommendations (prioritized)
For each finding:
- **ID:** F-001
- **Severity:** Critical / High / Medium / Low
- **Fix complexity:** Mechanical / Localized / Cross-cutting
- **Evidence:** `file:line` × N
- **Why it matters:** one or two sentences
- **Recommendation:** concrete change (token to introduce, file to consolidate)

Group findings by severity, then by fix complexity.

## 9. Intentional Variations (Appendix)
Cases that look like drift but are deliberate, with the rationale captured.

## 10. Suggested Next Steps
- Token layer to introduce (if absent).
- Refactor order (start with highest-traffic role).
- Preview/regression harness (cross-theme + font-scale).
```

---

## Verification (Self-Check Before Returning the Report)

Before delivering, confirm:

- [ ] Every finding includes at least one `file:line` citation.
- [ ] No finding flags a color, elevation, or state-color difference between themes.
- [ ] Every "fork on theme" claim in Section 6 cites the conditional code path (`isSystemInDarkTheme()`, theme parameter branch, etc.) with `file:line`.
- [ ] Hardcoded-literal counts are presented as **count + top offenders**, not raw grep dumps.
- [ ] The Token Inventory reflects what the codebase actually defines, not Material 3 defaults assumed to be present.
- [ ] No code changes were made.
- [ ] The "Intentional Variations" appendix is non-empty *or* explicitly states "none observed."
- [ ] Each recommendation maps to a specific file or token, not generic advice.
- [ ] Findings are deduplicated (the same `sp` literal across many files appears once as a histogram entry, not N times as separate findings).

If any check fails, fix the report before returning it.

---

## False-Positive Matrix

| If the prompt would flag... | Suppress when... |
| --- | --- |
| `sp` literal outside `Type.kt` | It's inside a `@Preview` function or a `*Sample.kt` demo. |
| `dp` literal outside `Dimens` | It's a 1dp/0.5dp hairline divider, or a compensation for a known platform inset. |
| Different button heights | One is a Material 3 `Button`, the other an `IconButton` — different semantic roles. |
| Different icon sizes | The sites are different (24dp toolbar icon vs 40dp list leading icon is correct). |
| Different paddings on two screens | One is a content surface, the other a chrome surface (e.g., bottom sheet handle area). |
| Typography "fork" on theme | The fork is a documented brand requirement, captured in the design-system doc. |
| Off-scale `dp` value | It's an animated/interpolated value (`animateDpAsState`) — only the endpoints matter. |

---

## Techniques Used

- **ST-01** Clear Objective — single, narrow audit goal.
- **ST-02** Structured Sequential Instructions — seven enforced phases.
- **ST-03** Output Format Templates — exact report shape.
- **RT-02** Multi-Dimensional Analysis — typography × sizing × spacing × cross-theme invariance.
- **RT-05** Evidence-Based Reasoning — `file:line` required on every finding.
- **DS-06** Prioritization Guidance — Critical/High/Medium/Low + fix complexity.
- **AG-01** Skeptical Default Stance — false-positive matrix + intentional-variation appendix.

---

## Customization Guide

- **Compose-only apps:** Skip `dimens.xml` / `styles.xml` discovery in Phase 1.
- **Hybrid (Compose + Views):** Add a sub-step in Phase 1 to also enumerate `styles.xml` text appearances and compare them to the Compose `Typography` to catch divergence at the bridge.
- **Material You / dynamic color:** Add a Phase 5 sub-check that confirms only `colorScheme` is sourced from dynamic color — typography/shape/dimension tokens must come from app code, not the dynamic provider.
- **Multi-module apps:** In Phase 1, list which module owns the token layer and flag every other module that defines its own tokens (this is almost always drift).
- **Brand-themed apps (multiple brands as themes):** Treat the brand axis as a theme dimension in Phase 5; only document, brand-approved deviations are allowed.
- **Pre-accessibility-audit use:** Tighten Phase 3 touch-target threshold to 48dp strict and Phase 5 to test `fontScale = 2.0` explicitly.
