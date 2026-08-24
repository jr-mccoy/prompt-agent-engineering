---
title: "Android Build Toolchain Upgrade (AGP / Gradle / Kotlin / JDK / KSP)"
category: mobile-development
description: "Plans and executes a coordinated upgrade of the Android build toolchain — Android Gradle Plugin, Gradle, Kotlin, JDK, and KSP/KAPT — mapping compatibility constraints, breaking changes, and a staged, verifiable rollout."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - android
  - maintenance
  - build
  - gradle
  - kotlin
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/maintenance/android_dependency_update.md
  - domain-software-engineering/mobile/android/improvement/android_version_catalog_migration.md
  - domain-software-engineering/mobile/android/improvement/android_build_speed_optimization.md
  - domain-software-engineering/mobile/android/maintenance/android_target_sdk_migration.md
---

# Android Build Toolchain Upgrade (AGP / Gradle / Kotlin / JDK / KSP)

**Objective:** Plan and execute a coordinated upgrade of the Android build toolchain — Android Gradle Plugin (AGP), Gradle wrapper, Kotlin, the JDK used to build, and the annotation-processing pipeline (KSP/KAPT) — by mapping the locked compatibility matrix, surfacing breaking changes between current and target versions, and producing a staged rollout that is verifiable at each step.

**When to Use:** Use when bumping AGP/Gradle/Kotlin (e.g., AGP 8.2 → 8.7, Kotlin 1.9 → 2.0, Gradle 8.4 → 8.x), migrating KAPT → KSP, adopting a new JDK for the build, or when a needed library requires a newer Kotlin/AGP than the project currently runs. This is the **toolchain** layer — distinct from upgrading application libraries (use `android_dependency_update.md`) and from restructuring dependency declarations (use `android_version_catalog_migration.md`).

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

Before planning the upgrade, gather:

1. **Current toolchain state:**
   - "What are the current and target versions for AGP, Gradle wrapper, Kotlin, JDK, and KSP (or KAPT)?"
   - "Paste `gradle/libs.versions.toml` (or buildscript versions) and `gradle/wrapper/gradle-wrapper.properties`."
   - "Which Kotlin compiler features are in use (K2 compiler, KSP plugins, Compose compiler, kapt processors, serialization)?"

2. **Build surface:**
   - "How many modules, and which use `kapt` vs `ksp`? Any custom Gradle plugins or convention plugins (`build-logic`)?"
   - "Which annotation processors run (Hilt/Dagger, Room, Moshi, Glide)? What versions?"
   - "Is the Compose compiler pinned, and is it the standalone Compose Compiler Gradle plugin (Kotlin 2.0+) or the old `composeOptions` mapping?"

3. **Constraints & safety net:**
   - "What is the CI build environment's JDK and Gradle distribution?"
   - "Do you have a green build baseline and a way to compare build output (APK/AAB diff, baseline benchmarks)?"
   - "What is the rollback path if the upgrade destabilizes the build?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending any version bump, you MUST:**

1. **Respect the compatibility matrix** — AGP requires a minimum Gradle; Kotlin requires a compatible KSP build (KSP version is `<kotlinVersion>-<kspVersion>`); the Compose compiler is tied to the Kotlin version; AGP requires a minimum JDK. Never bump one in isolation without confirming the others.
2. **Bump one axis at a time where possible** — order matters (see Phase 2). Coupled bumps (Kotlin + KSP + Compose compiler) move together by necessity; everything else is sequential.
3. **Read the breaking-change notes** — cite the specific AGP/Gradle/Kotlin release-note item for each required code or config change. Do not assume.
4. **Verify each step builds green** — every intermediate state must compile, assemble a release build, and pass tests before the next bump.
5. **Confirm reproducibility on CI** — the upgrade is not done until CI (not just a local machine) builds with the new toolchain.

### False-Positive Prevention

- ❌ Do NOT bump AGP and Gradle and Kotlin simultaneously in a single commit — failures become unbisectable
- ❌ Do NOT assume KAPT processors "just work" on a new Kotlin major — verify each, and prefer KSP migration where available
- ❌ Do NOT ignore the JDK: a newer AGP often requires JDK 17/21 for the build, independent of the app's `targetCompatibility`
- ❌ Do NOT mix a Compose-compiler version that is not mapped to the chosen Kotlin version
- ❌ Do NOT treat deprecation warnings as cosmetic — Gradle removes deprecated APIs on major versions
- ✅ DO pin every toolchain version explicitly (no dynamic `+` versions)
- ✅ DO keep the configuration cache and build cache in mind — re-validate they still work after the bump
- ✅ DO capture before/after build scan or `--profile` output to detect regressions

---

### Phase 1: Compatibility Matrix Lock

Build the matrix before changing anything. Fill current → target and the binding constraint for each pair.

| Component | Current | Target | Binding Constraint | Source (release note) |
|-----------|---------|--------|--------------------|------------------------|
| JDK (build) | [e.g. 17] | [e.g. 21] | AGP min JDK; Gradle JDK support | [link] |
| Gradle wrapper | [8.4] | [8.x] | AGP requires Gradle ≥ X | [link] |
| AGP | [8.2.x] | [8.7.x] | Requires Gradle ≥ X, JDK ≥ Y | [link] |
| Kotlin | [1.9.x] | [2.0.x] | K2 compiler; affects KSP + Compose | [link] |
| KSP | [matched] | [`<kotlin>-<ksp>`] | Must match Kotlin version exactly | [link] |
| Compose compiler | [mapped] | [plugin / mapped] | Tied to Kotlin version | [link] |
| KAPT processors | [list] | [KSP where avail.] | Per-processor Kotlin support | [per lib] |

**Output a single "target lock" block** the team can paste into `libs.versions.toml`.

---

### Phase 2: Upgrade Ordering Plan

Recommended safe order (each step = its own commit + green build):

```text
1) JDK for the build environment (local + CI aligned)         → build green
2) Gradle wrapper bump (./gradlew wrapper --gradle-version)   → build green, address deprecations
3) AGP bump                                                   → build green, apply AGP migration items
4) Kotlin + KSP + Compose compiler (coupled)                 → build green, fix K2/source changes
5) KAPT → KSP migration per processor (optional, incremental)→ build green per processor
6) Re-enable/verify configuration cache + build cache         → build green
```

For each step, document: the change, the expected breaking items, the verification command, and the rollback.

| Step | Change | Expected Breakage | Verify Command | Rollback |
|------|--------|-------------------|----------------|----------|
| 1 | [JDK X→Y] | [toolchain/source-target] | `./gradlew assembleRelease` | [revert wrapper/CI image] |
| 2 | [Gradle X→Y] | [deprecated APIs in plugins] | `./gradlew help --warning-mode=all` | [revert wrapper] |
| 3 | [AGP X→Y] | [DSL/namespace/variant API] | `./gradlew assembleRelease testDebugUnitTest` | [revert AGP] |
| 4 | [Kotlin/KSP/Compose] | [K2 strictness, stdlib] | `./gradlew assembleRelease test` | [revert coupled trio] |
| 5 | [kapt→ksp: lib] | [generated code differences] | `./gradlew :app:kspReleaseKotlin` | [restore kapt for lib] |

---

### Phase 3: Breaking-Change Surface Analysis

For each component, enumerate the concrete changes that hit this codebase.

**Gradle:**
- [ ] Removed/deprecated APIs used by custom or convention plugins (`build-logic`)
- [ ] `--warning-mode=all` output triaged; each deprecation has a fix or accepted-risk note
- [ ] Configuration cache compatibility (tasks that read at config time, project access at execution)

**AGP:**
- [ ] `namespace` migration (out of manifest) confirmed
- [ ] Variant API / `onVariants` changes if custom build logic manipulates variants
- [ ] BuildConfig generation flags, `buildFeatures` defaults that changed
- [ ] Lint behavior/baseline changes

**Kotlin (esp. 1.9 → 2.0 / K2):**
- [ ] K2 compiler enabled; stricter nullability/smart-cast/overload-resolution errors triaged
- [ ] Compose compiler moved to standalone Gradle plugin (Kotlin 2.0+); `composeOptions.kotlinCompilerExtensionVersion` removed
- [ ] `kotlinx-serialization`, `kotlin-parcelize`, other Kotlin plugins re-pinned
- [ ] Language/API version flags reviewed (`-language-version`)

**KSP / KAPT:**
- [ ] KSP version string matches Kotlin exactly
- [ ] Per-processor support confirmed (Hilt, Room, Moshi, Glide) on target Kotlin
- [ ] Where KSP is available and KAPT is the bottleneck, migration drafted (Phase 2 step 5)

---

### Phase 4: Findings Presentation

**CHECKPOINT 1:** Present the matrix + ordered plan before any change.

```markdown
## Toolchain Upgrade Plan

### Target Lock
[paste-ready versions block]

### Upgrade Order
1. … 2. … 3. …

### Highest-Risk Changes
1. [Change] — [why risky] — [mitigation]

### Effort & Sequencing
- Estimated steps: [N]; each independently verifiable
- Highest-risk step: [step] (recommend isolated PR)

**Proceed step-by-step, or adjust ordering/scope first?**
```

---

### Phase 5: Execution & Verification (per step)

Apply one step, then verify before the next.

**Standard verification gate (run after every step):**

```bash
./gradlew --stop                        # clear daemons holding old toolchain
./gradlew clean
./gradlew assembleRelease               # release build path (R8 active)
./gradlew testDebugUnitTest             # unit tests
./gradlew lintRelease                   # lint on the shipping variant
./gradlew help --warning-mode=all       # surface new deprecations
```

**Per-step verification checklist:**
- [ ] Clean release build succeeds
- [ ] Unit + instrumentation smoke tests pass
- [ ] No new unaddressed deprecation warnings
- [ ] APK/AAB size delta within expectation (use APK Analyzer)
- [ ] Configuration cache + build cache still function (`--configuration-cache`)
- [ ] CI reproduces the green build on the new toolchain

**Build health comparison (before/after full upgrade):**

| Metric | Before | After | Notes |
|--------|--------|-------|-------|
| Clean build time | [s] | [s] | use `--profile` |
| Incremental build time | [s] | [s] | |
| AAB size | [MB] | [MB] | APK Analyzer |
| KAPT vs KSP processing | [s] | [s] | if migrated |

---

## Expected Output

1. **Compatibility matrix** (current → target with binding constraints + sources)
2. **Paste-ready target lock** block for `libs.versions.toml` / wrapper
3. **Ordered upgrade plan** (one verifiable step per commit, with rollback per step)
4. **Breaking-change surface** mapped to this codebase (Gradle/AGP/Kotlin/KSP)
5. **Per-step verification gate** and a before/after build-health comparison
6. **CI alignment note** confirming the new toolchain builds in CI

---

## Techniques Used

- **ST-01** (Clear Objective): Single coordinated-upgrade objective
- **ST-02** (Sequential Instructions): Strict one-axis-at-a-time ordering
- **RT-02** (Multi-Dimensional Analysis): Matrix across five toolchain axes
- **DS-02** (Structured Decision Support): Ordered plan with rollback per step
- **QA-01** (Verification/Self-Check): Mandatory green-build gate at every step

---

## Related Prompts

- [android_dependency_update.md](android_dependency_update.md) - Application-library updates (distinct from toolchain)
- [android_version_catalog_migration.md](../improvement/android_version_catalog_migration.md) - Restructure dependency declarations into a version catalog
- [android_build_speed_optimization.md](../improvement/android_build_speed_optimization.md) - Tune build performance after the upgrade
- [android_target_sdk_migration.md](android_target_sdk_migration.md) - SDK/behavior-change planning (often paired with toolchain bumps)
- [android_proguard_r8_optimization.md](android_proguard_r8_optimization.md) - R8 behavior can change across AGP versions
