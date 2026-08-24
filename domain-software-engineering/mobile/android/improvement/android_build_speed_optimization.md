---
title: "Android Build Speed Optimization"
category: mobile-development
description: "Profile and reduce Gradle build times for an Android project — configuration cache, build cache, parallelization, KSP-over-KAPT, AGP/feature flags, and modularization — verified with measured before/after build profiles."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - android
  - mobile-development
  - gradle
  - build-system
  - performance
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/improvement/android_version_catalog_migration.md
  - domain-software-engineering/mobile/android/maintenance/android_proguard_r8_optimization.md
  - domain-software-engineering/mobile/android/planning/android_modularization_strategy.md
  - domain-software-engineering/mobile/android/analysis/android_dependency_audit.md
---

# Android Build Speed Optimization

**Objective:** Measure and reduce Gradle build times for an Android project — distinguishing clean, incremental, and configuration-only builds — by enabling Gradle's caching/parallelism features, migrating KAPT to KSP, tuning AGP feature flags, and removing build-graph bottlenecks, then proving the gain with before/after build profiles.

## When to Use

- Use when: Incremental builds take long enough to break flow, CI build minutes are costly, or `./gradlew --profile` shows specific slow phases.
- Use when: The project uses KAPT, lacks the configuration cache, or has a single monolithic `:app` module.
- **Don't use when:** The problem is *app runtime* performance — use `android_compose_performance_optimization.md` or `android_startup_optimization.md`.
- **Don't use when:** You only need release-binary size/obfuscation tuning — use `../maintenance/android_proguard_r8_optimization.md`.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Profile first.** Capture a build profile (`--profile` or a Build Scan) and identify which build type is slow (clean vs. incremental vs. configuration). Do not recommend fixes for a phase that is not the bottleneck.
2. **Measure each build type separately.** Configuration cache helps configuration time; the build cache helps task execution; parallelism helps multi-module. They solve different problems — match the fix to the measured bottleneck.
3. **Confirm a flag is not already set** before recommending it (check `gradle.properties`, `settings.gradle.kts`, module build files).
4. **Check compatibility before enabling the configuration cache** — some plugins/tasks are incompatible and will fail or warn. Report incompatibilities found in the report rather than blindly enabling.
5. **Provide `File:line` / file evidence** for every change.

**Finding the build is ALREADY well-tuned is an acceptable outcome.** If the major flags are on and builds are within a reasonable range for the project size, say so.

### False-Positive Prevention

- ❌ Do NOT enable the configuration cache without checking plugin compatibility — it can break the build.
- ❌ Do NOT crank `org.gradle.jvmargs` heap beyond available RAM — it causes swapping and slower builds.
- ❌ Do NOT blame "Gradle" when the cost is an annotation processor (KAPT) or a custom task.
- ❌ Do NOT recommend modularization as a quick win — it is an architecture change; scope it separately.
- ✅ DO measure clean, incremental, and config-only builds independently.
- ✅ DO verify each flag's effect with a re-profile.
- ✅ DO prefer KSP over KAPT where the library supports it.

---

### Phase 1: Profile

Capture evidence for three build scenarios on the same machine:

```bash
# Configuration time only (no task work)
./gradlew help --profile

# Incremental build (make a one-line change in :app first, then:)
./gradlew :app:assembleDebug --profile

# Clean build
./gradlew clean :app:assembleDebug --profile

# Richer, shareable analysis:
./gradlew :app:assembleDebug --scan
```

Read the generated `build/reports/profile/*.html` (or the Build Scan). Record:

| Scenario | Total | Configuration | Task execution | Slowest tasks |
|----------|-------|---------------|----------------|---------------|
| Config only | [s] | [s] | — | — |
| Incremental | [s] | [s] | [s] | [task: s] |
| Clean | [s] | [s] | [s] | [task: s] |

Identify the dominant phase. Everything below is prioritized by what the profile shows.

---

### Phase 2: Gradle-level wins (gradle.properties)

Check current values; enable what's missing and compatible:

```properties
# gradle.properties
org.gradle.caching=true                  # Build cache — reuse task outputs
org.gradle.configuration-cache=true      # Skip configuration on subsequent builds (verify compatibility)
org.gradle.parallel=true                 # Parallel module execution
org.gradle.jvmargs=-Xmx4g -XX:+UseParallelGC -Dfile.encoding=UTF-8   # Size to the machine, not blindly large
android.nonTransitiveRClass=true         # Smaller R classes, less recompilation
android.nonFinalResIds=true              # Faster resource recompilation
```

For the configuration cache, run `./gradlew :app:assembleDebug --configuration-cache` and triage any reported incompatibilities (often a plugin or a `Task.project` access at execution time). List incompatible plugins in the report.

---

### Phase 3: Annotation processing & compiler

- **KAPT → KSP:** KAPT runs the Java stub-generating compiler; KSP is multiples faster. Migrate processors that support KSP (Room, Hilt, Moshi, Glide all do):
  ```kotlin
  // Before:  kapt(libs.room.compiler)
  // After:   ksp(libs.room.compiler)   // plus: id("com.google.devtools.ksp")
  ```
  Remove the `kotlin-kapt` plugin once no KAPT processors remain — its presence alone adds cost.
- **K2 / current Kotlin compiler:** Confirm a current Kotlin version; older compilers are slower.
- **AGP version:** Upgrade to a current AGP — newer versions ship build-speed improvements and better incremental support.

---

### Phase 4: AGP feature flags & module hygiene

- Disable build features you don't use, per module:
  ```kotlin
  android.buildFeatures {
      buildConfig = false   // unless you read BuildConfig
      resValues = false
      aidl = false
      renderScript = false
      shaders = false
  }
  ```
- Debug builds: disable minification/PNG crunching (`isCrunchPngs = false`) and avoid running R8 on debug.
- Avoid dynamic dependency versions (`1.2.+`) — they defeat caching and force resolution. Pair with `android_version_catalog_migration.md`.
- **Remote build cache** (CI + team): point `buildCache { remote(...) }` at a shared node so CI and developers reuse outputs.
- **Modularization** (larger lever, separate effort): a monolithic `:app` recompiles everything on any change. If the profile shows one huge compile task dominating, scope a modularization effort via `../planning/android_modularization_strategy.md`.

---

### Phase 5: Verify

Re-run the Phase 1 profiling after each batch of changes and present before/after:

| Scenario | Before | After | Delta |
|----------|--------|-------|-------|
| Config only | [s] | [s] | [−%] |
| Incremental | [s] | [s] | [−%] |
| Clean | [s] | [s] | [−%] |

Revert any flag that did not help or that introduced instability.

---

## Expected Output

1. **Build profile baseline** — config/incremental/clean with the dominant phase identified.
2. **Prioritized change list** — each tied to the measured bottleneck, with compatibility notes.
3. **Applied `gradle.properties` / build-file changes** — before/after.
4. **KAPT→KSP migration list** — processors migrated and the `kotlin-kapt` removal.
5. **Verification table** — re-profiled before/after with deltas.

---

## CRITICAL: Verification Checklist (self-audit before reporting)

- [ ] All three build scenarios were profiled, not just one
- [ ] Configuration-cache compatibility was tested, and incompatibilities are listed
- [ ] No flag was recommended that was already enabled
- [ ] `jvmargs` heap is sized to the machine's RAM
- [ ] Each change shows a measured before/after delta
- [ ] Modularization was scoped as a separate effort, not presented as a quick flag

---

## Related Prompts

- [android_version_catalog_migration.md](android_version_catalog_migration.md) - Centralize/pin dependency versions
- [android_proguard_r8_optimization.md](../maintenance/android_proguard_r8_optimization.md) - Release-binary shrinking/obfuscation
- [android_modularization_strategy.md](../planning/android_modularization_strategy.md) - Split a monolithic app for parallel builds
- [android_dependency_audit.md](../analysis/android_dependency_audit.md) - Find and prune dependencies
