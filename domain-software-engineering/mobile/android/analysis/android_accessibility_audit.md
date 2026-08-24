---
title: "Android Accessibility Audit"
category: mobile-development
description: "Audits an Android app's accessibility across TalkBack/semantics, touch targets, color contrast, content descriptions, dynamic type, focus order, and RTL, producing WCAG-referenced findings with file:line locations and fixes."
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
  - accessibility
  - a11y
  - jetpack-compose
  - wcag
  - talkback
  - analysis
  - mobile-development
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/improvement/android_accessibility_improvement.md
  - domain-software-engineering/mobile/android/analysis/android_compose_ui_analysis.md
  - domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md
---

# Android Accessibility Audit

**Objective:** Audit an Android codebase for accessibility defects across screen-reader support (TalkBack), touch-target sizing, color contrast, content descriptions, dynamic type scaling, focus order, and right-to-left (RTL) layout — and report findings with `file:line` locations, WCAG references, severity, and concrete fixes. This is an **analysis-phase audit** that surfaces and prioritizes issues; remediation belongs to `improvement/android_accessibility_improvement.md`.

**When to Use:** Use this prompt before a release, when preparing for a Play Store accessibility review, when onboarding accessibility requirements to an existing app, after a major UI rewrite, or when users report screen-reader or low-vision difficulties. Works for Jetpack Compose, View/XML, and hybrid codebases.

---

## Context Gathering

1. **Surface & tech:** "Is the UI Compose, XML, or hybrid? Roughly how many screens/components?"
2. **Audience & obligations:** "Any specific compliance target (WCAG 2.1 AA, Section 508, EN 301 549, internal standard)?"
3. **Known pain points:** "Are there already reported accessibility complaints or known weak screens?"
4. **Languages:** "Does the app ship any RTL locales (Arabic, Hebrew, Farsi, Urdu)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace actual code** — confirm the defect in the real composable/view/resource, not from a guess. Cite `file:line`.
2. **Check for an existing accommodation** — a missing `contentDescription` on an icon may be correct if the icon is decorative and marked so, or if an adjacent text label already conveys the meaning.
3. **Confirm real user impact** — tie each finding to a concrete assistive-technology consequence (e.g., "TalkBack announces nothing for the primary CTA").
4. **Reference the standard** — map each finding to a WCAG success criterion or Android guideline where one applies.

**Finding the app accessible is an acceptable outcome.** If a screen meets the bar, say so. Do not manufacture issues.

### False-Positive Prevention

- ❌ Do NOT flag decorative images that correctly set `contentDescription = null`.
- ❌ Do NOT demand a `contentDescription` when a visible, associated text label already names the control.
- ❌ Do NOT flag contrast on disabled controls held to a lower bar by design, or on purely decorative surfaces.
- ❌ Do NOT report touch-target size for elements that are part of a larger clickable row meeting the minimum.
- ✅ DO flag interactive controls that are silent or mislabeled to a screen reader.
- ✅ DO flag layouts that break, clip, or overlap at large font scales.
- ✅ DO distinguish "fails WCAG" from "could be improved."

---

### Phase 1: Accessibility Surface Discovery

Inventory the assistive-technology surface before judging it.

| Item | What to Locate |
|------|----------------|
| Interactive controls | Buttons, icon buttons, switches, checkboxes, custom clickables (`Modifier.clickable`, `setOnClickListener`) |
| Images & icons | `Image`, `Icon`, `ImageView`, vector assets — note decorative vs informative |
| Text inputs | `TextField`, `EditText` — label association, error announcement |
| Custom components | Canvas-drawn UI, custom views without built-in semantics |
| Dynamic content | Snackbars, dialogs, loading states, live regions |
| Locale config | RTL support (`supportsRtl`), `start`/`end` vs `left`/`right` usage |

---

### Phase 2: Screen-Reader & Semantics Audit

| Check | Severity if Violated | What to Look For |
|-------|---------------------|-----------------|
| Silent interactive controls | HIGH | Icon-only buttons/clickables with no `contentDescription` or `semantics { }` |
| Mislabeled controls | HIGH | Description doesn't match action ("image" for a Send button) |
| Decorative noise | MEDIUM | Decorative images NOT marked `null`, adding clutter to TalkBack |
| Merged semantics | MEDIUM | Rows/cards not using `Modifier.semantics(mergeDescendants = true)` where a single focus target is expected |
| State announcement | HIGH | Toggles/selection state not exposed (`stateDescription`, `toggleableState`, `role`) |
| Headings & structure | LOW | No `semantics { heading() }` for section titles, hurting navigation |
| Live regions | MEDIUM | Async results/errors not announced (`liveRegion`) |
| Custom views | HIGH | Canvas/custom UI without `AccessibilityNodeInfo` / `semantics` |

---

### Phase 3: Visual Accessibility Audit

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Color contrast | HIGH | Text < WCAG AA (4.5:1 normal, 3:1 large/icons) — check theme color pairs |
| Color-only meaning | MEDIUM | Status/validity conveyed by color alone (no icon/text) |
| Touch targets | MEDIUM | Interactive elements < 48dp × 48dp effective size |
| Dynamic type | HIGH | Hardcoded `sp` ignoring user font scale; layouts that clip/overlap at 200% |
| Density/scaling | MEDIUM | Fixed `dp` containers that can't grow with content |

---

### Phase 4: Navigation, Focus & RTL Audit

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Focus order | MEDIUM | Illogical traversal order; `traversalIndex` needed but absent |
| Focus on dialogs/sheets | HIGH | Focus not moved into dialogs; back/dismiss not reachable |
| Keyboard/D-pad | MEDIUM | Non-touch navigation traps or unreachable controls |
| RTL mirroring | MEDIUM | `left`/`right` instead of `start`/`end`; non-mirrored directional icons |
| Text expansion | LOW | Layouts that break with longer translated strings |

---

## Output Format

```markdown
## Android Accessibility Audit Report

### Summary
| Dimension | Rating (Pass / Needs Work / Fails) | Critical Findings |
|-----------|-----------------------------------|-------------------|
| Screen reader / semantics | | |
| Visual (contrast, type, targets) | | |
| Navigation / focus / RTL | | |

### Findings (severity-ordered)
**[SEVERITY] Dimension: short title**
- Location: `path/to/File.kt:line`
- Issue: what AT users experience and which WCAG SC it implicates
- Fix: specific code change

### Prioritized Remediation
- **P1 (blocks AT users):** …
- **P2 (significant friction):** …
- **P3 (polish):** …

### What's Already Good
- (Honest list of areas that pass.)
```

---

## Expected Output

1. **Surface inventory** — what was audited.
2. **Findings** — severity-rated, `file:line`, WCAG-referenced, with fixes.
3. **Prioritized remediation** list.
4. **Affirmation of passing areas.**

---

## Techniques Used

- **ST-01** (Clear Objective): Accessibility-only scope.
- **ST-02** (Structured Sequential Instructions): Surface → semantics → visual → navigation.
- **RT-02** (Multi-Dimensional Analysis): Multiple AT angles per screen.
- **RT-05** (Evidence-Based Reasoning): `file:line` + WCAG references.
- **DS-06** (Prioritization Guidance): P1/P2/P3 severity.
- **QA-02** (Edge Case Coverage): Large font scale, RTL, custom views.

---

## Related Prompts

- [android_accessibility_improvement.md](../improvement/android_accessibility_improvement.md) - Remediate the findings from this audit
- [android_compose_ui_analysis.md](android_compose_ui_analysis.md) - Broader UI quality and appeal
- [../../../domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md](../../../../domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md) - WCAG criteria reference
