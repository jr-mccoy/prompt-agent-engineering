---
title: "Android Resource & Asset Analysis"
category: mobile-development
description: "Analyzes an Android app's resources and assets for hygiene and bloat: unused resources, density-bucket and vector/raster choices, duplicate or oversized drawables, string/dimen organization, and resource-driven APK size."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - android
  - resources
  - assets
  - drawables
  - apk-size
  - analysis
  - mobile-development
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_localization_i18n_readiness_audit.md
  - domain-software-engineering/mobile/android/analysis/android_theme_investigation.md
  - domain-software-engineering/mobile/android/publishing/android_app_bundle_optimization.md
---

# Android Resource & Asset Analysis

**Objective:** Analyze an Android app's `res/` and `assets/` for hygiene and size — unused/duplicate resources, density-bucket coverage, vector-vs-raster choices, oversized images, string/dimen/color organization, resource-qualifier correctness, and resource-driven APK/AAB bloat — and report findings with locations, size impact, and prioritized cleanup.

**When to Use:** Use this when download/install size is a concern, when resources have accumulated cruft over time, before an App Bundle size pass, or when consolidating a design system's resources. Complements `publishing/android_app_bundle_optimization.md` (which focuses on delivery/packaging) by auditing the resource *source*.

---

## Context Gathering

1. **Surface:** "Roughly how many drawables/strings/layouts? Any large image-heavy features?"
2. **Tooling:** "Do you run `lint` (unused resources), `shrinkResources`, or an APK-size analyzer today?"
3. **Concern:** "Is the priority size reduction, maintainability, or both?"
4. **Design system:** "Is there a token/design-system source these resources should align to?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Confirm a resource is actually unused** — check code, XML, data binding, reflection (`getIdentifier`), and library references before flagging. Resource shrinking and `getIdentifier` make naive "unused" calls risky.
2. **Quantify size where it matters** — note approximate file sizes for image findings; small files aren't bloat.
3. **Respect density/qualifier intent** — a drawable that exists only in `xxxhdpi` may be intentional; missing buckets aren't always wrong if a vector or single density is used deliberately.
4. **Separate hygiene from size** — organization issues and size issues are different findings.

**A clean, lean resource set is an acceptable outcome.** Don't over-flag.

### False-Positive Prevention

- ❌ Do NOT flag resources referenced only via `resources.getIdentifier(...)` / dynamic names as unused.
- ❌ Do NOT flag library-provided resources the app can't remove.
- ❌ Do NOT demand all density buckets when a vector drawable is used.
- ❌ Do NOT flag intentionally large hero/splash images without weighing the size/benefit.
- ✅ DO flag genuinely orphaned drawables/layouts/strings confirmed unreferenced.
- ✅ DO flag raster images that should be vectors (simple icons shipped as multi-density PNGs).
- ✅ DO flag uncompressed/oversized images and duplicates.

---

### Phase 1: Resource Inventory

| Item | What to Capture |
|------|-----------------|
| Drawables | Count by type (vector, PNG, WebP, 9-patch); density buckets present |
| Images & assets | Large files in `res/drawable*`, `mipmap`, `assets/`, `raw/` |
| Values | `strings.xml`, `dimens.xml`, `colors.xml`, `styles/themes` — size and duplication |
| Layouts | Count; obvious duplicates / near-duplicates |
| Qualifiers | Locale, density, orientation, night — coverage and correctness |

---

### Phase 2: Hygiene & Organization

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Unused resources | MEDIUM | Orphaned drawables/layouts/strings (verified, not `getIdentifier`-dynamic) |
| Duplicate resources | MEDIUM | Identical images under different names; copy-paste layouts |
| Hardcoded values | LOW | Inline colors/dimens that should be tokens/`@dimen`/`@color` |
| Naming/structure | LOW | Inconsistent naming; values files that should be split |
| Stale qualifiers | LOW | Leftover `values-xx` / density folders no longer needed |

---

### Phase 3: Size & Format Optimization

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Raster-where-vector | MEDIUM | Simple icons as multi-density PNGs instead of `VectorDrawable` |
| PNG-where-WebP | MEDIUM | Photographic PNGs that should be WebP/lossy |
| Oversized images | MEDIUM | Images far larger than their display size; full-res in small views |
| Missing density strategy | LOW | Multiple raster densities where one vector would do |
| Uncompressed assets | LOW | Large uncompressed files in `assets/`/`raw/` |
| Resource shrinking off | MEDIUM | `shrinkResources`/`minifyEnabled` disabled in release |

---

### Phase 4: APK/AAB Size Attribution

| Dimension | What to Assess |
|-----------|----------------|
| Top size contributors | Largest resources/assets and their share of the package |
| Per-feature weight | Which features carry the heaviest resource cost |
| Delivery readiness | Whether large/optional assets could move to dynamic delivery |
| Quick wins | Highest size reduction for least effort/risk |

---

## Output Format

```markdown
## Android Resource & Asset Analysis Report

### Inventory Summary
| Category | Count | Notable sizes |
|----------|-------|---------------|

### Findings (severity-ordered)
**[SEVERITY] Area: title** — Location `res/...` · Issue (incl. ~size) · Fix

### Size Reduction Opportunities
| Change | Approx. savings | Effort | Risk |
|--------|-----------------|--------|------|

### Prioritized Cleanup (P1/P2/P3)
```

---

## Expected Output

1. **Resource inventory** summary.
2. **Severity-rated findings** with locations and size notes.
3. **Size-reduction opportunities** with savings/effort/risk.
4. **Prioritized cleanup** plan.

---

## Techniques Used

- **ST-01** (Clear Objective): Resource/asset scope.
- **ST-02** (Structured Sequential Instructions): Inventory → hygiene → size → attribution.
- **RT-02** (Multi-Dimensional Analysis): Maintainability + size lenses.
- **RT-05** (Evidence-Based Reasoning): Cite resource paths and sizes.
- **DS-06** (Prioritization Guidance): Savings/effort/risk ranking.

---

## Related Prompts

- [android_localization_i18n_readiness_audit.md](android_localization_i18n_readiness_audit.md) - String/locale resource correctness
- [android_theme_investigation.md](android_theme_investigation.md) - Theme/style resource architecture
- [android_app_bundle_optimization.md](../publishing/android_app_bundle_optimization.md) - Delivery/packaging size optimization
