---
title: "Android Accessibility & Localization Plan"
category: mobile-development
description: "Plan accessibility-by-design and localization/internationalization for an Android app before UI is built — WCAG 2.2 AA mapped to Android, TalkBack/Compose semantics, touch targets, font scaling, RTL, string externalization, plurals, ICU formatting, per-app language, and a combined per-locale + a11y QA matrix."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - CM-01
difficulty: intermediate
tags:
  - android
  - mobile-development
  - accessibility
  - localization
  - i18n
  - talkback
  - compose-semantics
  - rtl
updated: "2026-06-06"
related_prompts:
  - ../analysis/android_accessibility_audit.md
  - ../improvement/android_accessibility_improvement.md
  - ../analysis/android_localization_i18n_readiness_audit.md
  - android_compose_ui_design_studio.md
---

# Android Accessibility & Localization Plan

**Objective:** Produce a concrete accessibility-by-design and localization/internationalization plan for an Android app **before** the UI is implemented, so that screen-reader support, touch targets, font scaling, color contrast, right-to-left layout, string externalization, plurals, locale-aware formatting, and a per-app language picker are designed in from the first screen rather than retrofitted under pressure later. The plan ends with a single combined per-locale + accessibility QA matrix that the team can execute against every screen.

**When to Use:** Use this prompt at planning time, after you know your feature set and target markets but before you write production Composables or screens. Use it whenever you are starting a new Android app, adding a new market/locale, or about to commit to a design system. Do **not** wait for an audit prompt — audits find what you forgot; this plan prevents the forgetting.

**Sequence Map:** Use after `android_mvp_scope_and_release_roadmap.md` and concept/UI-direction decisions; use before `android_compose_ui_design_studio.md` and any sustained UI implementation. The audit/improvement prompts (`../analysis/android_accessibility_audit.md`, `../analysis/android_localization_i18n_readiness_audit.md`, `../improvement/android_accessibility_improvement.md`) come **later**, against built screens.

**Important context:** Accessibility and localization are cheap as decisions and expensive as repairs. The two are deliberately planned together because they share the same root discipline — *never bake meaning into layout, pixels, or hardcoded English*. A11y bakes meaning into semantics instead of visuals; i18n bakes meaning into resources instead of literals. On Android specifically: TalkBack drives screen-reader UX, Compose `semantics {}` is the modern lever (not legacy `contentDescription`-only thinking), per-app language (Android 13+/`AppCompatDelegate.setApplicationLocales` and `LocaleManager`) is now the expected pattern, and RTL is a per-string and per-modifier decision (`start`/`end`, never `left`/`right`). The goal of this prompt is a plan, not code — but every plan item must be specific enough to become a code-review checklist line.

---

## Context Gathering

Ask these before producing the plan. Do not assume answers.

1. **Product & UI surface:**
   - "Which screens/flows are in MVP, and which contain media (audio/video), maps, charts, or custom-drawn views?"
   - "Compose-only, Views-only, or hybrid? What design-system / theming approach (Material 3)?"
   - "Any custom interactive components (sliders, drag-and-drop, canvas gestures, carousels)?"

2. **Accessibility commitments:**
   - "Is there a legal/contractual conformance target (e.g., EN 301 549, ADA, Section 508, a customer's RFP)? Default target if unspecified: **WCAG 2.2 Level AA**."
   - "Who are the expected assistive-tech users (TalkBack, Switch Access, external keyboard/d-pad, large font, magnification, reduced motion)?"
   - "Will the app ship to Android TV / large-screen / foldables (changes focus-order and d-pad requirements)?"

3. **Localization commitments:**
   - "Which locales at launch, and which are planned next? What is the *reason* for each (market size, contract, existing user base)?"
   - "Are any target locales RTL (Arabic, Hebrew, Farsi, Urdu)?"
   - "Who translates — in-house, vendor (e.g., TMS), or community? What is the source language?"
   - "Any locale-specific assets (legal text, currency, imagery, units, regulated copy)?"

---

## Instructions

Work in two phases (Accessibility, then Localization), then produce the combined QA matrix. Stop at each **CHECKPOINT** and present before continuing.

---

### Phase 1 — Accessibility Plan (WCAG 2.2 AA → Android)

#### Step 1.1: Map the conformance target to Android mechanisms

Produce this table, marked per screen where relevant:

| WCAG 2.2 AA criterion | Android mechanism | Plan decision |
|---|---|---|
| 1.1.1 Non-text content | `semantics { contentDescription = … }`; `null` for decorative images | Every meaningful image gets a description; decorative gets explicit `null` |
| 1.3.1 Info & relationships | Semantics roles, `heading()`, grouping with `mergeDescendants` | Headings declared; related controls merged |
| 1.4.3 Contrast (text) | Color tokens audited ≥ 4.5:1 (≥ 3:1 large text) | Theme tokens chosen to pass before design lock |
| 1.4.4 Resize text | `sp` units (never `dp`) for text; layouts reflow | No fixed-height text containers; test at 200% |
| 1.4.11 Non-text contrast | Icon/control/focus-indicator contrast ≥ 3:1 | Verify icon + state colors |
| 2.1.1 Keyboard | d-pad/keyboard focus reachable for all interactive elements | Focus order defined per screen |
| 2.4.3 Focus order | `Modifier.focusProperties`/traversal order | Logical reading + focus order documented |
| 2.4.7 Focus visible | Visible focus indicator in theme | Focus ring/highlight designed |
| 2.5.5 / 2.5.8 Target size | Minimum touch target **48dp × 48dp** (Material) | Enforced via `sizeIn`/`minimumInteractiveComponentSize` |
| 2.3.3 Animation from interactions | Respect reduced-motion / disable non-essential animation | Motion plan (see Step 1.4) |
| 1.2.x Time-based media | Captions/transcripts for audio/video | Captions plan (see Step 1.5) |
| 4.1.2 Name, role, value | Semantics: role + state (`toggleable`, `selectable`, `stateDescription`) | State announced, not just visual |

#### Step 1.2: Compose semantics plan (per interactive component type)

For each component type used (button, toggle, list item, tab, slider, custom), specify:

```
Component: Favorite toggle (heart icon)
  Role:               Toggleable
  contentDescription: "Add to favorites" / "Remove from favorites" (state-dependent)
  stateDescription:   "On" / "Off"
  mergeDescendants:   true (icon + label announced as one)
  Touch target:       48dp via Modifier.minimumInteractiveComponentSize()
  Custom action(s):   none
  Notes:              Do NOT rely on color alone to show selected state
```

Rules to enforce in the plan:
- Use `semantics(mergeDescendants = true)` to collapse a labeled control into one announcement; do **not** leave a label and its icon as two separate TalkBack stops.
- Declare `heading()` on section titles so TalkBack users can navigate by heading.
- Express state via `stateDescription` / `toggleableState` / `selectableGroup`, never via color or position alone.
- Decorative imagery: `contentDescription = null`. Never use a filename or placeholder text.
- Live/changing content: plan `liveRegion` for snackbars, validation errors, and async status.

#### Step 1.3: Touch targets, contrast, and font scaling

- **Touch target:** every interactive element ≥ 48dp × 48dp. List the components that need padding/expanded hit area to reach it.
- **Color contrast:** list every text/background and icon/background token pair with its computed ratio and pass/fail (4.5:1 text, 3:1 large text/non-text). Choose tokens that pass *before* design lock.
- **Font scaling / large text:** all text in `sp`; no fixed-pixel text heights; verify layouts at 130%, 150%, and 200% font scale and with the system "largest" display size. Flag any screen that truncates or overlaps.

#### Step 1.4: Input modalities & motion

- **Switch Access / keyboard / d-pad:** document the focus traversal order per screen; ensure no interactive element is unreachable; ensure focus does not trap. For TV/large-screen, confirm directional navigation.
- **Motion/animation reduction:** identify non-essential animations (parallax, autoplay, large transitions). Plan to read the system *Remove animations* setting (`Settings.Global.ANIMATOR_DURATION_SCALE` / transition scale) and reduce or disable accordingly. No content may *require* motion to be understood.

#### Step 1.5: Media & a11y acceptance checklist

- **Captions/transcripts:** every audio/video asset needs captions or a transcript; plan the format and source.
- Produce an **a11y acceptance checklist** (per screen): TalkBack swipe-through reads everything in logical order; all controls have name+role+state; targets ≥ 48dp; contrast passes; works at 200% font; keyboard/d-pad reachable; reduced motion honored; no info conveyed by color alone.

**CHECKPOINT 1:** Present the WCAG→Android mapping, the per-component semantics plan, and the a11y acceptance checklist. Confirm conformance target and component coverage before moving to localization.

---

### Phase 2 — Localization & Internationalization Plan

#### Step 2.1: Locale list & selection rationale

| Locale (BCP-47) | Direction | Reason to support | Launch / Next | Translator |
|---|---|---|---|---|
| `en-US` (source) | LTR | Source language | Launch | — |
| `es-419` | LTR | Largest secondary market | Launch | Vendor |
| `ar` | **RTL** | Contractual / region X | Next | Vendor |
| `de-DE` | LTR | High-ARPU market | Next | Vendor |

#### Step 2.2: RTL decision

Decide explicitly: **RTL supported at launch / supported later / out of scope** (with reason).
If supported now or later, the plan must require from day one:
- All directional modifiers use `start`/`end`, never `left`/`right` (padding, alignment, `Arrangement`).
- `android:supportsRtl="true"` in the manifest.
- Mirror directional icons (back arrows, chevrons, progress) via `autoMirrored` / RTL-aware assets; do **not** mirror logos, media controls that are direction-neutral, or numerals.
- Test with *Force RTL* (developer options) and a pseudo-RTL locale.

#### Step 2.3: String externalization conventions

- **No hardcoded user-facing strings** anywhere in code or Compose — all in `strings.xml` (or per-locale resource files).
- **Naming:** `screen_component_purpose` (e.g., `login_button_submit`, `cart_label_empty`). Document the convention so all contributors follow it.
- **No string concatenation** to build sentences. Forbidden: `"$count " + getString(R.string.items)`. Word order and grammar differ per language.
- Mark non-translatable strings `translatable="false"` (keys, debug, brand names).

#### Step 2.4: Plurals & parameterized formatting

- **Plurals:** use quantity strings (`<plurals>` / `getQuantityString`); never `if (n == 1)`. Many locales have more than two plural categories (zero/one/two/few/many/other). Plan to provide all categories the locale requires.
- **Parameterized formatting:** use positional placeholders (`%1$s`, `%2$d`) so translators can reorder. For numbers/dates/currency/units, format via locale-aware APIs (ICU `MessageFormat`/`NumberFormatter`, `java.time` formatters with the active `Locale`, CLDR data) — never manual formatting or hardcoded symbols/separators.

```xml
<!-- Good: positional + plural + locale-formatted via ICU at call site -->
<plurals name="cart_items_count">
    <item quantity="one">%1$d item in your cart</item>
    <item quantity="other">%1$d items in your cart</item>
</plurals>
```

#### Step 2.5: Pseudolocalization, locale-specific assets, in-app language picker, workflow

- **Pseudolocalization in QA:** enable the `en-XA`/`ar-XB` pseudolocales (or build-config pseudo) to catch hardcoded strings, truncation, and concatenation *before* real translations arrive. Plan it as a standing QA step.
- **Locale-specific assets:** list any per-locale images, legal/regulated copy, currency, or units; store in locale-qualified resource folders.
- **In-app language picker (per-app language):** plan a picker that sets the app locale via `AppCompatDelegate.setApplicationLocales(...)` / `LocaleManager` (per-app language, Android 13+ with AppCompat back-compat), plus a `locales_config.xml` declared in the manifest. Document fallback behavior when a string is missing for the chosen locale.
- **Translation workflow & string freeze:** define source-of-truth (TMS/spreadsheet), export/import cadence, a **string freeze** date before each release, and how new keys are flagged for translation. No release ships with untranslated user-facing strings in a launch locale.

**CHECKPOINT 2:** Present the locale list + rationale, the RTL decision, the externalization conventions, and the translation workflow. Confirm before producing the combined matrix.

---

### Step 3: Combined per-locale + a11y QA matrix

Produce one matrix the team runs against every screen. Rows = screens; columns = checks. Each cell: ✅ / ⚠️ / ❌ / N/A.

| Screen | TalkBack order OK | Name+role+state | 48dp targets | Contrast AA | 200% font OK | Keyboard/d-pad | Reduced motion | No hardcoded strings | Plurals OK | RTL layout OK | Date/number/currency localized | Picker switches locale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Login | | | | | | | | | | | | |
| Home/List | | | | | | | | | | | | |
| Detail | | | | | | | | | | | | |
| Settings | | | | | | | | | | | | |
| Media/Player | | | | | | | | | | | | |

For each locale in scope, the matrix is run at least once (with that locale active, plus pseudolocale and Force-RTL passes for RTL locales).

---

## Expected Output

1. **Accessibility conformance mapping** — WCAG 2.2 AA → Android mechanisms with per-screen decisions.
2. **Compose semantics plan** — per-component role/description/state/merge/touch-target spec.
3. **A11y acceptance checklist** — per-screen pass criteria.
4. **Locale list & rationale** — with direction, launch timing, and translator.
5. **RTL decision** — explicit scope and the rules it triggers.
6. **String & formatting conventions** — externalization naming, no-concatenation, plurals, ICU/CLDR formatting, per-app language picker, translation workflow + string freeze.
7. **Combined per-locale + a11y QA matrix** — the executable test grid.

---

## CRITICAL: Verification Requirements

- [ ] A conformance target is stated explicitly (default WCAG 2.2 AA) and mapped to concrete Android mechanisms, not generic advice.
- [ ] Every interactive component type has a semantics plan including role **and** state (not just `contentDescription`).
- [ ] Minimum touch target of 48dp × 48dp is required for all interactive elements.
- [ ] All text uses `sp`; layouts are verified at 200% font scale; no fixed-height text containers.
- [ ] Color contrast pairs are listed with computed ratios and pass/fail against 4.5:1 / 3:1.
- [ ] Keyboard/d-pad/Switch Access focus order is documented per screen and proven reachable.
- [ ] Reduced-motion behavior is planned and no content requires motion to be understood.
- [ ] Captions/transcripts are planned for every audio/video asset.
- [ ] No hardcoded user-facing strings; naming convention defined; concatenation banned.
- [ ] Plurals use quantity strings and cover all categories the locale requires.
- [ ] Numbers/dates/currency/units are formatted via locale-aware ICU/CLDR APIs with positional placeholders.
- [ ] RTL decision is explicit; if in scope, `start`/`end`, `supportsRtl`, and icon mirroring are required.
- [ ] Pseudolocalization is a standing QA step; an in-app per-app-language picker and `locales_config.xml` are planned.
- [ ] A translation workflow with a string-freeze date is defined.
- [ ] The combined per-locale + a11y QA matrix exists and covers every MVP screen.

## False-Positive Prevention

- ❌ Do NOT claim a screen is "accessible" because it has `contentDescription` — role and **state** must also be announced, and TalkBack order must be logical.
- ❌ Do NOT treat color as a sufficient signal for state (selected, error, on/off) — it fails for low-vision and color-blind users.
- ❌ Do NOT mark localization "done" because `strings.xml` exists — check for concatenation, missing plural categories, and hardcoded number/date/currency formatting.
- ❌ Do NOT assume two plural forms — many locales need zero/one/two/few/many/other.
- ❌ Do NOT use `left`/`right` modifiers and assume RTL "probably works."
- ❌ Do NOT defer a11y/i18n to "after MVP" and call this plan satisfied — the point is to plan before UI exists.
- ✅ DO require name + role + state for every interactive element and a logical TalkBack/focus order.
- ✅ DO verify contrast ratios numerically and font scaling at 200% before design lock.
- ✅ DO externalize strings with a naming convention, positional placeholders, plurals, and ICU/CLDR formatting.
- ✅ DO run pseudolocalization and Force-RTL passes before real translations land.
- ✅ DO produce the combined QA matrix and run it per locale per screen.

## Techniques Used

- **ST-01** (Clear Objective Statement): Singular goal — plan a11y + i18n before UI is built.
- **ST-02** (Sequential Instructions): Accessibility phase → localization phase → combined matrix.
- **RT-02** (Multi-Dimensional Analysis): Evaluates each screen across screen-reader, motor, vision, and locale dimensions simultaneously.
- **RT-05** (Best-Practice Review): Maps decisions to WCAG 2.2 AA and Android/CLDR/ICU conventions.
- **DS-06** (Prioritized Findings/Output): Conformance mapping and QA matrix order checks by user-impact and risk.
- **CM-01** (Explicit Context Framing): Context-gathering establishes locales, conformance target, and UI surface before planning.

## Related Prompts

- [../analysis/android_accessibility_audit.md](../analysis/android_accessibility_audit.md) — Audit built screens against this plan.
- [../improvement/android_accessibility_improvement.md](../improvement/android_accessibility_improvement.md) — Remediate a11y gaps found in audit.
- [../analysis/android_localization_i18n_readiness_audit.md](../analysis/android_localization_i18n_readiness_audit.md) — Audit localization readiness of existing code.
- [android_compose_ui_design_studio.md](android_compose_ui_design_studio.md) — Design the UI with these a11y/i18n constraints baked in.
