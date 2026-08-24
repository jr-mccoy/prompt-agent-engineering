---
title: "Android Build & Gradle Health Analysis"
category: mobile-development
description: "Analyzes an Android project's Gradle build for configuration health and build performance: version catalogs, convention plugins, configuration cache, KSP vs kapt, variants/flavors, and redundant or risky configuration."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - android
  - gradle
  - build-performance
  - version-catalog
  - convention-plugins
  - analysis
  - mobile-development
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_dependency_audit.md
  - domain-software-engineering/mobile/android/analysis/android_module_graph_analysis.md
  - domain-software-engineering/mobile/android/maintenance/android_proguard_r8_optimization.md
---

# Android Build & Gradle Health Analysis

**Objective:** Analyze an Android project's Gradle build for configuration health and build performance — dependency declaration strategy (version catalogs), build-logic reuse (convention plugins vs copy-paste), configuration cache and parallelization readiness, annotation-processing strategy (KSP vs kapt), variant/flavor sprawl, and redundant or risky settings — reporting issues with file locations and prioritized fixes.

**When to Use:** Use this when builds are slow, when build scripts have drifted into copy-paste across modules, before scaling the number of modules, when migrating to version catalogs / KSP, or as part of a codebase health review. Covers Groovy and Kotlin DSL build scripts.

---

## Context Gathering

1. **Build setup:** "Can you share `settings.gradle(.kts)`, root and module `build.gradle(.kts)`, `gradle.properties`, `libs.versions.toml`, and `buildSrc`/`build-logic` if present?"
2. **Scale:** "How many modules? AGP/Gradle/Kotlin versions?"
3. **Symptoms:** "Slow clean/incremental builds? Flaky cache? Duplicated config across modules?"
4. **CI:** "What does CI run, and is build time a pain point there?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Read the actual build files** — cite the file and block. Don't assume conventions.
2. **Confirm the cost** — flag a slow-down only when the setting plausibly affects build time or correctness (e.g., kapt on a hot module, configuration cache disabled).
3. **Respect intentional choices** — a flavor dimension or a pinned version may exist for a real reason; ask or note the assumption.
4. **Separate health from style** — distinguish settings that cause real problems from mere preference.

**A clean, fast build is an acceptable outcome.** Don't invent problems.

### False-Positive Prevention

- ❌ Do NOT flag kapt where the processor has no KSP equivalent yet.
- ❌ Do NOT flag a pinned dependency version without checking for an intentional compatibility constraint.
- ❌ Do NOT recommend configuration cache if a known incompatible plugin is required.
- ❌ Do NOT flag multiple flavors that map to real product/build needs.
- ✅ DO flag versions scattered across modules instead of a catalog.
- ✅ DO flag duplicated build logic that a convention plugin would consolidate.
- ✅ DO flag `kapt` on modules where KSP is available and would speed builds.

---

### Phase 1: Build Topology Inventory

| Item | What to Locate |
|------|----------------|
| Dependency declarations | Hardcoded coordinates vs `libs.versions.toml` catalog |
| Build logic | `buildSrc` / `build-logic` convention plugins vs repeated `android { }` blocks |
| Plugins | Plugin application style, `plugins {}` vs legacy `apply`, plugin versions alignment |
| Annotation processing | `kapt` vs `ksp`; which modules |
| Variants | Build types, product flavors, dimensions; count and combinatorics |
| Properties | `gradle.properties`: JVM args, parallel, caching, configuration cache, AndroidX |

---

### Phase 2: Configuration Health

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| No version catalog | MEDIUM | Versions/coordinates duplicated across modules; drift risk |
| Copy-paste build logic | MEDIUM | Same `compileSdk`/`kotlinOptions`/`testOptions` repeated per module |
| Plugin version drift | MEDIUM | Same plugin applied at different versions across modules |
| Dynamic/`+` versions | HIGH | Version ranges causing non-reproducible builds |
| Misused configurations | MEDIUM | `api` where `implementation` suffices (leaks deps, slows builds) |
| Hardcoded secrets/signing | HIGH | Keystore passwords/API keys in committed build files |
| Variant sprawl | LOW | Flavor combinatorics producing many unused variants |

---

### Phase 3: Build Performance

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Configuration cache off | MEDIUM | `org.gradle.configuration-cache` not enabled / blocked by a plugin |
| Parallel/caching off | MEDIUM | `org.gradle.parallel`/`caching` disabled; low daemon heap |
| kapt on hot modules | MEDIUM | `kapt` where KSP is supported (Room, Hilt, Moshi codegen) |
| Over-broad `api` graph | MEDIUM | Excessive `api` deps forcing wide recompilation |
| Non-incremental tasks | LOW | Custom tasks without inputs/outputs declared |
| Heavy `buildSrc` | LOW | `buildSrc` changes invalidating the whole build (vs `build-logic` included build) |

---

### Phase 4: Reproducibility & Risk

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Lockfile/repro | MEDIUM | No dependency locking; dynamic versions |
| Repository safety | MEDIUM | Untrusted/insecure (`http`) repositories; missing `dependencyResolutionManagement` |
| AGP/Gradle/Kotlin alignment | MEDIUM | Incompatible or far-behind toolchain versions |
| Debug-only flags in release | HIGH | `minifyEnabled false`/test-only config leaking to release |

---

## Output Format

```markdown
## Android Build & Gradle Health Report

### Build Topology
| Aspect | Current | Assessment |
|--------|---------|------------|
| Dependency declaration | | |
| Build logic reuse | | |
| Annotation processing | | |
| Variants | | |

### Findings (severity-ordered)
**[SEVERITY] Area: title** — Location `file` · Issue · Fix

### Build-Performance Opportunities
| Change | Est. effort | Expected benefit |
|--------|-------------|------------------|

### Prioritized Remediation (P1/P2/P3)
```

---

## Expected Output

1. **Build topology** summary.
2. **Severity-rated findings** with file locations and fixes.
3. **Build-performance opportunities** with effort/benefit.
4. **Prioritized remediation.**

---

## Techniques Used

- **ST-01** (Clear Objective): Build/Gradle scope.
- **ST-02** (Structured Sequential Instructions): Topology → health → performance → risk.
- **RT-02** (Multi-Dimensional Analysis): Correctness + performance + reproducibility.
- **RT-05** (Evidence-Based Reasoning): Cite build files and blocks.
- **DS-06** (Prioritization Guidance): Severity + effort/benefit.

---

## Related Prompts

- [android_dependency_audit.md](android_dependency_audit.md) - Dependency freshness and vulnerabilities
- [android_module_graph_analysis.md](android_module_graph_analysis.md) - How module structure drives build time
- [android_proguard_r8_optimization.md](../maintenance/android_proguard_r8_optimization.md) - Release shrinking/optimization config
