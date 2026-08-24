---
title: "Android Modularization Strategy"
category: mobile-development
description: "Analyze a monolithic Android app and produce a modularization plan — feature modules, library modules, build time impact analysis, and dependency graphs"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - CM-01
difficulty: advanced
tags:
  - android
  - modularization
  - architecture
  - gradle
  - build-performance
  - mobile-development
updated: "2026-02-12"
---

# Android Modularization Strategy

**Objective:** Analyze a monolithic or poorly-modularized Android app and produce a comprehensive modularization plan — identifying module boundaries based on feature domains and architectural layers, defining module types (feature, library, core), mapping the dependency graph, estimating build time improvements, and providing a phased extraction plan that keeps the app shippable at every step.

**When to Use:** Use this prompt when your Android app's build times are growing (>2 minutes for incremental builds), when multiple features are tightly coupled making independent development difficult, when you want to enable dynamic feature delivery, or when preparing for Kotlin Multiplatform adoption (modularization is a prerequisite).

**Sequence Map:** Use after architecture selection or monolith assessment; use before large-scale module extraction work.

**Important context:** Modularization is not about having the most modules — it is about having the right boundaries. Over-modularization creates maintenance overhead (more Gradle configs, more module boilerplate). Under-modularization causes slow builds and tight coupling. The goal is modules that are cohesive internally and loosely coupled externally.

---

## Context Gathering

1. **Current State:**
   - "How many modules does the project currently have? What are they?"
   - "What is the current clean build time? Incremental build time?"
   - "How many developers work on the project?"
   - "Are there any dynamic feature delivery requirements?"

2. **Architecture:**
   - "What architecture pattern (MVVM, MVI, Clean Architecture)?"
   - "What DI framework (Hilt, Koin)? How are DI modules organized?"
   - "What navigation approach? Does navigation cross feature boundaries?"
   - "Are there shared UI components used across features?"

3. **Pain Points:**
   - "What triggers full rebuilds (changes to which files/packages)?"
   - "Which features are most commonly modified together?"
   - "Are there circular dependencies between packages?"
   - "What code is duplicated across features?"

---

## Instructions

### Step 1: Codebase Analysis

Analyze the current codebase to understand the natural boundaries:

1. **Package Structure Map:**
   - List all top-level packages and their approximate size (file count, line count)
   - Identify which packages depend on which (import analysis)
   - Flag packages with high fan-out (depend on many others) and high fan-in (many depend on them)

2. **Feature Domain Identification:**
   - Group code by user-facing feature (auth, home, profile, settings, chat, payments, etc.)
   - For each feature, list: UI (Activities/Fragments/Composables), ViewModels, Repositories, Data Sources, Models
   - Identify shared code used by multiple features

3. **Dependency Graph:**
   - Map current inter-package dependencies
   - Identify circular dependencies (A → B → C → A)
   - Flag "god packages" that everything depends on
   - Use `./gradlew app:dependencies --configuration releaseRuntimeClasspath` for library dependencies

4. **Build Impact Analysis:**
   - Identify which source changes trigger the most recompilation
   - Measure current build times: `./gradlew assembleDebug --scan`
   - Identify the critical path in the build (longest chain of dependent tasks)

### Step 2: Module Type Definitions

Define the module types for your project:

| Module Type | Purpose | Example | Android Plugin |
|-------------|---------|---------|----------------|
| **`:app`** | Application entry point, navigation host, DI root | The main app module | `com.android.application` |
| **`:feature:*`** | Self-contained user-facing features | `:feature:auth`, `:feature:home` | `com.android.library` |
| **`:core:*`** | Shared infrastructure and utilities | `:core:network`, `:core:database` | `com.android.library` |
| **`:core:ui`** | Shared UI components, theme, design system | Common Composables | `com.android.library` |
| **`:core:model`** | Domain models shared across features | Data classes | Pure Kotlin (`kotlin("jvm")`) |
| **`:core:common`** | Extensions, utilities, base classes | Result wrappers | Pure Kotlin or Android library |
| **`:core:testing`** | Shared test utilities, fakes, fixtures | Test helpers | `com.android.library` |

**Rules:**
- `:feature:*` modules NEVER depend on other `:feature:*` modules
- `:feature:*` modules depend on `:core:*` modules
- `:core:*` modules NEVER depend on `:feature:*` modules
- `:core:*` modules may depend on other `:core:*` modules (no circular)
- `:app` depends on all `:feature:*` modules and wires DI + navigation

### Step 3: Modularization Plan

For each proposed module, define:

```
Module: :feature:auth
Contents:
  - LoginScreen.kt, SignUpScreen.kt (UI)
  - AuthViewModel.kt (presentation)
  - AuthRepository.kt (interface in :core:data, implementation here)
  - TokenManager.kt (move to :core:auth-api)
Dependencies:
  - :core:ui (shared Composables, theme)
  - :core:network (Ktor/Retrofit client)
  - :core:model (User, AuthToken data classes)
  - :core:common (Result type, extensions)
Extraction Difficulty: Medium
Reason: TokenManager is currently used by 3 other features — need to extract interface first
```

### Step 4: Dependency Inversion Plan

For cross-feature communication (Feature A needs data from Feature B):

1. **Define API modules:** `:feature:auth:api` contains interfaces and models, no implementation
2. **Depend on API, not implementation:** `:feature:profile` depends on `:feature:auth:api`, not `:feature:auth`
3. **Wire at app level:** `:app` module connects API interfaces to implementations via DI
4. **Navigation:** Use navigation routes (strings/sealed classes) defined in a shared navigation module — features don't know about each other's screens

### Step 5: Phased Extraction Order

Order extraction by dependency depth (extract leaves first):

**Phase 1 — Core modules (lowest risk):**
1. `:core:model` — extract all shared data classes (zero implementation logic)
2. `:core:common` — extract utilities, extensions, Result types
3. `:core:ui` — extract design system, shared Composables, theme

**Phase 2 — Infrastructure modules:**
4. `:core:network` — extract networking client, interceptors, API interfaces
5. `:core:database` — extract Room database, DAOs, migrations
6. `:core:datastore` — extract DataStore/preferences wrappers

**Phase 3 — Feature modules (one at a time):**
7. Extract the most independent feature first (fewest dependencies on other features)
8. For each feature: extract UI → ViewModel → repository implementation
9. Verify the app builds and all tests pass after each extraction
10. Continue until all features are extracted

**At each step:**
- [ ] App compiles
- [ ] All tests pass
- [ ] Incremental build time measured (should improve)
- [ ] No new circular dependencies introduced

### Step 6: Build Performance Estimation

After modularization, estimate improvements:
- **Incremental build:** Changes to `:feature:auth` only recompile `:feature:auth` and `:app`, not `:feature:home` → estimated 30-60% faster incremental builds
- **Parallel compilation:** Independent modules compile in parallel → improvement depends on module count and CPU cores
- **Cache hit rate:** More granular modules = better Gradle build cache hits = faster CI

Measure with: `./gradlew assembleDebug --scan` before and after

---

## Expected Output

1. **Current State Analysis** — package map, dependency graph, build profile
2. **Proposed Module Architecture** — module list with types, contents, and dependencies
3. **Dependency Graph** — visual representation of module dependencies (text-based or Mermaid)
4. **Phased Extraction Plan** — ordered steps with effort estimates per module
5. **Build Performance Estimate** — projected build time improvements
6. **Risk Register** — what could go wrong and how to mitigate
7. **Gradle Configuration Templates** — `build.gradle.kts` snippets for each module type

---

## CRITICAL: Verification Requirements

- [ ] No circular dependencies between modules
- [ ] Feature modules do not depend on other feature modules
- [ ] The app builds and all tests pass at every extraction step
- [ ] Build times are measured before and after (quantified improvement)
- [ ] Hilt/Koin DI still wires correctly across module boundaries
- [ ] Navigation between features works through the app module
- [ ] ProGuard/R8 rules work correctly with the multi-module setup
