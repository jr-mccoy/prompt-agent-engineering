---
title: "Android Compose Performance Optimization"
category: mobile-development
description: "Diagnose and fix Jetpack Compose runtime performance problems — excess recomposition, unstable parameters, and read-too-high state — using compiler metrics, stability fixes, strong skipping, deferred reads, and Macrobenchmark verification."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - QA-01
difficulty: advanced
tags:
  - android
  - mobile-development
  - compose
  - performance
  - recomposition
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/targeted-reviews/android_compose_recomposition_review.md
  - domain-software-engineering/mobile/android/targeted-reviews/android_compose_recomposition_problems_review.md
  - domain-software-engineering/mobile/android/improvement/android_baseline_profiles_optimization.md
  - domain-software-engineering/mobile/android/analysis/android_performance_audit.md
---

# Android Compose Performance Optimization

**Objective:** Diagnose and fix runtime performance problems in a Jetpack Compose UI — excess recomposition, unstable parameters, reading state too high in the tree, allocation churn, and lazy-list inefficiency — then verify the improvement with measured evidence (Layout Inspector recomposition counts and/or a Macrobenchmark `FrameTimingMetric`).

## When to Use

- Use when: Scrolling or animations jank, the Layout Inspector shows high recomposition counts, or `FrameTimingMetric` shows frames over budget.
- Use when: A screen feels sluggish on mid-tier devices even though the logic is cheap.
- Use when: You want to enable Compose stability tooling (compiler metrics, strong skipping, a stability config) and act on the results.
- **Don't use when:** The problem is a slow *cold start* — use `android_startup_optimization.md` and `android_baseline_profiles_optimization.md`.
- **Don't use when:** You only want a read-only review without changes — use `../targeted-reviews/android_compose_recomposition_review.md`.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Measure, don't guess.** Confirm a real recomposition or frame problem with Layout Inspector recomposition counts, composition tracing, or a Macrobenchmark — not by reading code alone. A composable that recomposes is not a bug; a composable that recomposes *unnecessarily and frequently on a hot path* is.
2. **Confirm the parameter is actually unstable.** Run the Compose compiler stability report and cite the class/parameter it marks unstable. Do not assume `List` is unstable in *this* module without checking (strong skipping changes the calculus).
3. **Trace where state is read.** A `State` read inside a composable's body triggers recomposition of that scope; the same read inside a deferred lambda (`Modifier.offset { }`, `graphicsLayer { }`, `drawBehind { }`) does not. Identify the exact read site.
4. **Provide `File:line` evidence** for every finding.
5. **Quantify expected impact.** Tie each fix to a measurable target (recomposition count → N, P90 frame time → X ms).

**Finding the UI is ALREADY performant is an acceptable outcome.** If recomposition counts are reasonable and frames are within budget, say so. Do not micro-optimize cold paths.

### False-Positive Prevention

- ❌ Do NOT wrap everything in `remember`/`derivedStateOf` reflexively — unnecessary `derivedStateOf` adds overhead.
- ❌ Do NOT add `@Stable`/`@Immutable` to a class that is actually mutated — this is a correctness lie that causes stale UI.
- ❌ Do NOT flag `List`/`Map` params as unstable if strong skipping is enabled and the instance is stable in practice — confirm with the report.
- ❌ Do NOT optimize a composable that recomposes once per user action — that is correct behavior.
- ✅ DO measure before and after every change.
- ✅ DO prefer making types genuinely stable (immutable data, `ImmutableList`) over annotations.
- ✅ DO check whether the screen is gated by a missing Baseline Profile before blaming recomposition.

---

### Phase 1: Establish a Measurement Baseline

Set up the tooling that produces evidence before changing anything.

1. **Enable Compose compiler metrics + stability reports:**
   ```kotlin
   // build.gradle.kts (app or module) — Compose Compiler Gradle plugin (Kotlin 2.0+)
   composeCompiler {
       reportsDestination = layout.buildDirectory.dir("compose_compiler")
       metricsDestination = layout.buildDirectory.dir("compose_compiler")
       // Optional: stabilityConfigurationFile = rootProject.layout.projectDirectory.file("compose_stability.conf")
   }
   ```
   Build a release variant, then read `*-classes.txt` (stability of classes), `*-composables.txt` (restartable/skippable status), and `*-module.json` (counts).

2. **Capture recomposition counts:** Run the app with Android Studio's Layout Inspector → "Recomposition counts" enabled. Record counts for the janky screen during the problem interaction.

3. **(Preferred) Add a Macrobenchmark** with `FrameTimingMetric` for the scroll/animation path (see `android_baseline_profiles_optimization.md` for module setup). Record P50/P90/P99 frame durations.

Record the baseline in a table:

| Screen / interaction | Recompositions (worst composable) | P90 frame (ms) | Notes |
|----------------------|-----------------------------------|----------------|-------|
| [Screen] | [count] | [ms] | [device] |

---

### Phase 2: Diagnose

Apply these checks, citing evidence for each confirmed issue.

#### 2.1 Stability (from the compiler report)
- **Unstable parameters** on a hot composable make it non-skippable. Confirm via `*-composables.txt` (`restartable scheme(...) fun X` without `skippable`).
- Common causes: classes with `var` fields, classes from modules without the Compose compiler, `List`/`Map`/`Set` interfaces holding potentially-mutable impls, lambdas capturing unstable values.

#### 2.2 Strong skipping
- Strong skipping (default with the modern Compose compiler) makes composables with unstable parameters skippable when arguments are referentially equal, and auto-remembers lambdas. **Confirm it is enabled** for the module before recommending manual lambda `remember`. If disabled or on an old compiler, that is itself the highest-leverage fix.

#### 2.3 Read-too-high / wrong read site
- State read in a parent that only a child uses → hoist the read down or pass a lambda.
- Frequently-changing state (scroll offset, animation progress) read in the composition phase instead of a deferred lambda → defer it.

#### 2.4 Lazy list inefficiency
- Missing `key =` on `items()` → identity churn on insert/move.
- Missing `contentType` for heterogeneous lists → poor item reuse.
- Unstable item models causing every visible item to recompose on any change.

#### 2.5 Allocation / derived work in composition
- New collections, sorts, or filters computed in the composable body every recomposition → move to `remember(key)` or the ViewModel.
- `derivedStateOf` missing where a frequently-changing state is mapped to a rarely-changing one (e.g., `scrollOffset > 0` → "show elevation").

---

### Phase 3: Fix (in priority order)

Present a prioritized plan; apply after confirmation.

| Priority | Fix | Technique |
|----------|-----|-----------|
| 1 | Enable strong skipping / upgrade Compose compiler if off | Build config |
| 2 | Make hot models genuinely stable (immutable `data class`, `ImmutableList`) | Type design |
| 3 | Defer frequently-changing reads into lambda modifiers | `Modifier.offset { }`, `graphicsLayer { }` |
| 4 | Add `key` + `contentType` to lazy lists | Lazy list |
| 5 | Hoist expensive computation out of composition (`remember`/ViewModel) | State |
| 6 | Add `derivedStateOf` for high→low frequency mappings | State |
| 7 | Last resort: `stabilityConfigurationFile` for third-party types you cannot annotate | Build config |

Representative fixes:

```kotlin
// Stability: prefer real immutability over annotations
data class Filters(val query: String, val tags: ImmutableList<Tag>)   // kotlinx.collections.immutable

// Deferred read: scroll offset read in a lambda, not in composition
Modifier.graphicsLayer { translationY = scrollState.value.toFloat() } // not Modifier.offset(y = scrollState.value.dp)

// derivedStateOf: recompose only when the boolean flips, not every pixel
val showElevation by remember { derivedStateOf { listState.firstVisibleItemScrollOffset > 0 } }

// Lazy list: stable identity + reuse
LazyColumn {
    items(items, key = { it.id }, contentType = { it.type }) { item -> Row(item) }
}
```

---

### Phase 4: Verify

Re-run the exact same measurement from Phase 1 and present a before/after table. A fix that does not move the metric should be reverted.

| Screen / interaction | Recompositions before → after | P90 frame before → after | Verdict |
|----------------------|------------------------------|--------------------------|---------|
| [Screen] | [N → M] | [X → Y ms] | [Improved / No change / Regressed] |

---

## Expected Output

1. **Measurement baseline** — recomposition counts and/or frame timings with device/variant noted.
2. **Stability report findings** — specific unstable classes/composables with `File:line`.
3. **Prioritized fix plan** — each fix tied to evidence and an expected metric delta.
4. **Applied changes** — before/after code for each fix.
5. **Verification table** — measured before/after proving (or disproving) each fix.

---

## CRITICAL: Verification Checklist (self-audit before reporting)

- [ ] Every finding has a measurement, not just a code smell
- [ ] Strong-skipping status was confirmed before recommending manual lambda remembering
- [ ] No `@Stable`/`@Immutable` was added to a type that is actually mutated
- [ ] Each applied fix shows a measured before/after delta
- [ ] Fixes that did not move the metric were reverted, not kept "for cleanliness"
- [ ] Considered whether a missing Baseline Profile, not recomposition, was the real cause

---

## Related Prompts

- [android_compose_recomposition_review.md](../targeted-reviews/android_compose_recomposition_review.md) - Read-only recomposition review
- [android_compose_recomposition_problems_review.md](../targeted-reviews/android_compose_recomposition_problems_review.md) - Specific recomposition anti-patterns
- [android_baseline_profiles_optimization.md](android_baseline_profiles_optimization.md) - Launch/scroll AOT profiling + Macrobenchmark setup
- [android_performance_audit.md](../analysis/android_performance_audit.md) - Broader performance analysis
