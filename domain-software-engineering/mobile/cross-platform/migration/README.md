# Cross-Platform Migration Prompts

> **18 migration prompts** for Android-to-iOS transitions and KMP shared architecture design.

---

## Overview

This collection provides structured prompts for teams migrating Android applications to iOS, whether through full native rewrite or Kotlin Multiplatform (KMP) shared architecture. Each prompt covers a specific migration concern -- from high-level strategy down to build system adaptation -- and produces actionable migration plans, mapping tables, and implementation guides.

These prompts are designed to be used sequentially following the recommended migration workflow, or individually when addressing a specific migration challenge.

---

## Recommended Migration Workflow

Migrations should proceed in dependency order. Each phase builds on the decisions and outputs of the previous one.

```
Phase 1: Architecture & Strategy
    Define overall approach (KMP vs native), map features, adapt architecture
    │
    ▼
Phase 2: Data Layer
    Migrate persistence, networking, and preferences layers
    │
    ▼
Phase 3: DI & Concurrency
    Adapt dependency injection and async patterns
    │
    ▼
Phase 4: UI Layer
    Map Compose to SwiftUI, Material to HIG, navigation patterns
    │
    ▼
Phase 5: Platform Services
    Replace Firebase, billing, and store publishing
    │
    ▼
Phase 6: Build System & Tooling
    Adapt Gradle to SPM/Xcode, CI/CD pipelines, and testing strategy
```

**Why this order?**
- Architecture decisions constrain everything downstream
- Data and concurrency layers are dependencies for UI
- UI migration requires stable data and DI layers
- Platform services can be swapped once core app works
- Build and tooling come last since they wrap the finished product

---

## Decision Tree: KMP vs Full Native Rewrite

```
Should you use KMP shared modules?
│
├─ How much business logic exists?
│  ├─ Heavy (>40% of codebase) ──────────────► Strong KMP candidate
│  └─ Light (<20% of codebase) ──────────────► Native rewrite likely simpler
│
├─ Does the team know Kotlin?
│  ├─ iOS team comfortable with Kotlin ──────► KMP viable
│  └─ iOS team Kotlin-averse ────────────────► Native rewrite preferred
│
├─ How platform-specific is the app?
│  ├─ Heavy platform API usage ──────────────► Native rewrite preferred
│  │  (camera, ARKit, HealthKit, widgets)
│  └─ Mostly networking/data/logic ──────────► Strong KMP candidate
│
├─ What is the timeline?
│  ├─ Need both platforms maintained long-term ► KMP reduces duplication
│  └─ One-time migration, separate teams ─────► Native rewrite cleaner
│
└─ What is the risk tolerance?
   ├─ Low (enterprise, regulated) ────────────► Native rewrite (mature tooling)
   └─ Moderate (startup, greenfield) ─────────► KMP (shared code advantage)
```

**Hybrid approach:** Many teams use KMP for data/domain layers while keeping UI fully native (SwiftUI on iOS, Compose on Android). This captures most code-sharing benefits while preserving platform-native UX.

---

## Prompt Categories

### Architecture & Strategy (4 prompts)

Start here. These prompts define the migration approach and set constraints for all downstream decisions.

| Prompt | Description |
|--------|-------------|
| `migration_android_to_ios_strategy.md` | Comprehensive Android-to-iOS migration strategy covering timeline, team structure, risk assessment, and phased rollout planning |
| `migration_kmp_shared_module_design.md` | KMP shared module layer design including expect/actual boundaries, module structure, and Kotlin/Native interop patterns |
| `migration_platform_feature_mapping.md` | Feature-by-feature platform API mapping producing a complete matrix of Android APIs to iOS equivalents with gap analysis |
| `migration_architecture_adaptation.md` | Adapt Android architecture patterns (MVVM, Clean Architecture, MVI) to idiomatic iOS equivalents (MVVM+Coordinator, TCA, etc.) |

### UI Layer Migration (3 prompts)

Map Android UI patterns to iOS equivalents. Use after architecture and data layers are defined.

| Prompt | Description |
|--------|-------------|
| `migration_compose_to_swiftui.md` | Jetpack Compose to SwiftUI component mapping covering layouts, modifiers, state management, animations, and lifecycle |
| `migration_material_to_hig.md` | Material Design 3 to Apple Human Interface Guidelines adaptation including color systems, typography, spacing, and component replacements |
| `migration_navigation_patterns.md` | Navigation pattern mapping from Jetpack Navigation/Compose Navigation to NavigationStack, NavigationSplitView, and Coordinator patterns |

### Data Layer Migration (3 prompts)

Migrate persistence, networking, and local storage. These are typically the most mechanical translations.

| Prompt | Description |
|--------|-------------|
| `migration_room_to_core_data.md` | Room database to Core Data or SwiftData mapping including entity modeling, relationships, migrations, queries, and threading |
| `migration_retrofit_to_urlsession.md` | Retrofit/OkHttp to URLSession/async-await mapping covering interceptors, serialization, error handling, and caching strategies |
| `migration_datastore_to_userdefaults.md` | Jetpack DataStore to UserDefaults and Keychain mapping for preferences, encrypted storage, and proto-based structured data |

### DI & Concurrency (2 prompts)

Adapt dependency injection and asynchronous programming patterns.

| Prompt | Description |
|--------|-------------|
| `migration_hilt_to_swift_di.md` | Hilt/Dagger to Swift DI mapping covering property wrappers, Environment, factory patterns, and third-party options (Swinject, needle) |
| `migration_coroutines_to_swift_concurrency.md` | Kotlin Coroutines to Swift structured concurrency mapping including Flow to AsyncSequence, suspend to async/await, dispatchers to actors |

### Platform Services (3 prompts)

Replace Android platform services with Apple equivalents. These often require the most re-engineering.

| Prompt | Description |
|--------|-------------|
| `migration_firebase_to_apple_services.md` | Firebase to Apple platform equivalents: FCM to APNs, Crashlytics to MetricKit, Remote Config to CloudKit, Analytics to App Analytics |
| `migration_play_billing_to_storekit.md` | Google Play Billing Library to StoreKit 2 mapping covering products, subscriptions, receipt validation, and server-side verification |
| `migration_play_store_to_app_store.md` | Play Store to App Store publishing covering App Review guidelines, metadata requirements, screenshots, TestFlight, and phased rollout |

### Build System & Tooling (3 prompts)

Adapt build infrastructure last, once the application code is migrated.

| Prompt | Description |
|--------|-------------|
| `migration_gradle_to_spm_xcode.md` | Gradle build system to Swift Package Manager and Xcode project mapping including dependency management, build configurations, and flavors/schemes |
| `migration_ci_cd_adaptation.md` | CI/CD pipeline adaptation from Android (Gradle-based) to iOS (Xcode/xcodebuild) covering signing, provisioning, Fastlane, and distribution |
| `migration_testing_strategy_adaptation.md` | Testing strategy adaptation mapping JUnit/Espresso/Robolectric to XCTest/XCUITest/Swift Testing with coverage parity planning |

---

## Usage Patterns

### Full Migration
Run prompts in phase order (Architecture, Data, DI/Concurrency, UI, Platform, Build). Feed outputs from earlier phases as context into later prompts.

### Targeted Migration
Use individual prompts when migrating a specific layer. For example, if only the networking layer needs migration, use `migration_retrofit_to_urlsession.md` directly.

### KMP Assessment
Start with `migration_kmp_shared_module_design.md` and `migration_platform_feature_mapping.md` to evaluate whether KMP is viable before committing to a strategy.

### Estimation & Planning
Use `migration_android_to_ios_strategy.md` and `migration_platform_feature_mapping.md` together to produce effort estimates and migration timelines for stakeholders.

---

## Related Resources

- **Android prompts:** `domain-software-engineering/mobile/android/`
- **iOS prompts:** `domain-software-engineering/mobile/ios/`
- **Cross-platform architecture:** `domain-software-engineering/mobile/cross_platform_architecture_design.md`
- **Mobile CI/CD:** `domain-software-engineering/mobile/mobile_cicd_pipeline_optimization.md`
- **Mobile security:** `domain-software-engineering/mobile/mobile_app_security_review.md`
