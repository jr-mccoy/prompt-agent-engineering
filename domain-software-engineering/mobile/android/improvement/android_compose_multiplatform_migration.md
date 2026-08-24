---
title: "Android Compose Multiplatform Migration"
category: mobile-development
description: "Guide for evaluating and planning migration from Android-only Compose to Compose Multiplatform (CMP), covering shared UI decisions, platform-specific boundaries, and incremental adoption strategy"
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
  - compose-multiplatform
  - kmp
  - migration
  - kotlin
  - cross-platform
  - mobile-development
updated: "2026-02-12"
---

# Android Compose Multiplatform Migration

**Objective:** Evaluate and plan an incremental migration from an Android-only Jetpack Compose application to Compose Multiplatform (CMP) — assessing feasibility, identifying what UI can be shared vs. must remain platform-specific, designing the module boundary architecture, and producing a phased migration plan with effort estimates and risk mitigations.

**When to Use:** Use this prompt when you have a working Android app in Jetpack Compose and want to explore expanding to iOS (or Desktop/Web) via Compose Multiplatform. Also useful when evaluating CMP vs. other cross-platform options (Flutter, React Native, KMM-only) for an existing Kotlin codebase.

**Important context:** Compose Multiplatform (by JetBrains) shares the Compose UI framework across Android, iOS, Desktop, and Web. As of 2025-2026 it is production-ready for Android and iOS with stable API status. Migration from Android-only Compose is incremental — you do not need to rewrite your app. The key decision is what to share (UI components, ViewModels, business logic) vs. what stays platform-specific (platform APIs, navigation, system integrations).

---

## Context Gathering

Before planning the migration, gather information about the current app:

1. **Current Architecture:**
   - "Describe your current module structure (single module or multi-module). List modules and their responsibilities."
   - "What architecture pattern do you use (MVVM, MVI, Clean Architecture)? How are layers separated?"
   - "What DI framework (Hilt, Koin, manual)? Note: Hilt is Android-only; Koin works cross-platform."
   - "What navigation approach (Navigation Component, Compose Navigation with type-safe routes, custom)?"

2. **Platform API Usage:**
   - "List all Android-specific APIs your UI layer uses directly (e.g., Context, Activity, FragmentManager, Android Permissions, system intents)."
   - "Do your Composables reference Android types directly (e.g., android.graphics.Bitmap, android.net.Uri)?"
   - "What platform services do you use (camera, location, biometrics, notifications, file system)?"

3. **Dependencies:**
   - "List your key dependencies. Flag which are Android-only vs. have multiplatform versions."
   - "Networking: Retrofit (Android-only) or Ktor (multiplatform)?"
   - "Serialization: Gson (Android-only) or kotlinx.serialization (multiplatform)?"
   - "Image loading: Coil (Android) — Coil 3+ has multiplatform support."
   - "Database: Room (Android) or SQLDelight (multiplatform)?"

4. **Business Goals:**
   - "What target platforms (iOS, Desktop, Web)? What is the priority order?"
   - "What is the acceptable timeline for the first platform addition?"
   - "How much UI do you ideally want to share (just components? full screens? entire navigation?)?"
   - "Do you have iOS development resources (Swift/Xcode experience) for platform-specific work?"

---

## Instructions

### Phase 1: Feasibility Assessment

Analyze the current codebase and produce a feasibility report:

1. **Dependency Audit:**
   - Categorize every dependency as: (a) Already multiplatform, (b) Has a multiplatform alternative, (c) Android-only with no alternative (must wrap with `expect`/`actual`)
   - Flag blocking dependencies that have no multiplatform path
   - Estimate migration effort per dependency (drop-in replacement vs. API change)

2. **Platform API Surface Scan:**
   - Scan all `@Composable` functions for direct Android API references
   - Categorize: (a) Easy to abstract (string resources, context), (b) Moderate (permissions, intents), (c) Hard (camera, custom views, deep OS integration)
   - Calculate the percentage of UI code that is already platform-agnostic

3. **Architecture Compatibility Score:**
   Rate 1-5 on each dimension:
   - UI layer purity (no Android types in Composables) → 5 = perfect, 1 = Android types everywhere
   - Business logic separation (ViewModels don't import Android) → 5 = clean, 1 = tightly coupled
   - Data layer abstraction (repository interfaces, not implementations) → 5 = interface-driven, 1 = concrete
   - Navigation decoupling (navigation logic independent of Android Navigation) → 5 = agnostic, 1 = tightly bound
   - DI framework portability (Koin/manual = 5, Hilt = 2)

4. **Feasibility Verdict:**
   - Score 20-25: **Ready** — migration is straightforward
   - Score 14-19: **Feasible with prep work** — refactoring needed before migration
   - Score 8-13: **Significant effort** — major refactoring required
   - Score 5-7: **Rewrite may be more practical** — consider alternatives

### Phase 2: Migration Architecture Design

Design the target module structure:

```
project/
├── shared/                        # Kotlin Multiplatform shared code
│   ├── commonMain/
│   │   ├── domain/                # Business logic, use cases, models
│   │   ├── data/                  # Repository interfaces, DTOs
│   │   ├── presentation/          # ViewModels (with kotlinx-coroutines)
│   │   └── ui/                    # Shared Compose UI components
│   ├── androidMain/               # Android-specific implementations
│   │   ├── data/                  # Android data sources (Room, Android APIs)
│   │   └── platform/             # expect/actual Android implementations
│   └── iosMain/                   # iOS-specific implementations
│       ├── data/                  # iOS data sources
│       └── platform/             # expect/actual iOS implementations
├── androidApp/                    # Android application module
│   ├── navigation/                # Android-specific navigation (if needed)
│   └── di/                        # Hilt modules (Android-only DI)
└── iosApp/                        # iOS application (Xcode project)
    └── ContentView.swift          # SwiftUI host for Compose views
```

For each module, define:
- What moves to `commonMain` (shared)
- What stays in `androidMain` (platform-specific)
- What new `expect`/`actual` declarations are needed
- What interfaces need to be created for platform abstraction

### Phase 3: Incremental Migration Plan

Produce a phased migration plan ordered by risk and dependency:

**Step 1 — Foundation (Week 1-2):**
- Set up KMP project structure with Gradle conventions
- Configure `libs.versions.toml` for multiplatform dependencies
- Add `shared` module with empty `commonMain`, `androidMain`, `iosMain`
- Verify Android app still builds and runs identically

**Step 2 — Domain Layer (Week 3-4):**
- Move pure Kotlin domain models to `commonMain`
- Move business logic (use cases, mappers) to `commonMain`
- Replace Android-specific types with Kotlin equivalents (e.g., `java.time` → `kotlinx-datetime`)
- Create `expect`/`actual` for any platform-specific domain needs

**Step 3 — Data Layer (Week 5-7):**
- Define repository interfaces in `commonMain`
- Move networking to Ktor (if currently Retrofit) in `commonMain`
- Move serialization to kotlinx.serialization (if currently Gson)
- Keep Room in `androidMain`, create SQLDelight alternative for `commonMain` (or defer)
- Implement `actual` data sources per platform

**Step 4 — Presentation Layer (Week 8-10):**
- Move ViewModels to `commonMain` using `kotlinx-coroutines` (no Android ViewModel dependency)
- Replace `androidx.lifecycle.ViewModel` with a multiplatform ViewModel base class
- Move state management (StateFlow, SharedFlow) — already cross-platform
- Create `expect`/`actual` for platform-specific presentation needs

**Step 5 — UI Layer (Week 11-14):**
- Move shared Composable components to `commonMain/ui/`
- Start with leaf components (buttons, cards, list items) — lowest risk
- Progress to screen-level Composables
- Abstract platform-specific UI (permissions dialogs, system bars) behind `expect`/`actual`
- Set up Compose Multiplatform resources (images, strings)

**Step 6 — iOS Integration (Week 15-18):**
- Set up Xcode project with Kotlin framework integration
- Implement all `actual` declarations for `iosMain`
- Create SwiftUI host view for Compose screens
- Test on iOS simulator and devices
- Handle iOS-specific concerns (safe area, gestures, navigation patterns)

### Phase 4: Risk Assessment

For each migration step, identify:
- **What could go wrong:** Specific technical risks (dependency incompatibility, performance differences, platform behavior differences)
- **Mitigation:** How to reduce the risk (keep Android app working at every step, feature flags, A/B comparison)
- **Rollback plan:** How to undo the step if it causes problems
- **Verification:** How to confirm the step succeeded (tests, manual QA, performance benchmarks)

---

## Expected Output

Produce a migration assessment document containing:

1. **Feasibility Score** with per-dimension breakdown and overall verdict
2. **Dependency Compatibility Matrix** — every dependency with its multiplatform status and migration effort
3. **Platform API Surface Analysis** — categorized list of Android APIs used in UI
4. **Target Module Architecture** — diagram and description of the CMP module structure
5. **Phased Migration Plan** — ordered steps with effort estimates, dependencies, and risks
6. **Decision Recommendation** — clear GO / GO WITH PREP / CONSIDER ALTERNATIVES verdict with rationale
7. **Cost-Benefit Analysis** — estimated total migration effort vs. long-term benefit of code sharing

---

## CRITICAL: Verification Requirements

Before finalizing the migration plan:
- [ ] Android app builds and runs identically at every migration step (no regression)
- [ ] No Android-specific types leak into `commonMain`
- [ ] All `expect` declarations have corresponding `actual` implementations
- [ ] Gradle build times are measured at each step (multi-module can slow builds)
- [ ] iOS compilation is verified (not just Android) if iOS is the target
- [ ] Every dependency replacement is tested for behavioral equivalence
- [ ] The migration can be paused at any step without leaving the app in a broken state
