---
title: "Android Kotlin Multiplatform Architecture"
category: mobile-development
description: "Design a KMP shared module architecture — what to share (networking, data, business logic) vs. keep platform-specific (UI, platform APIs), with Gradle configuration patterns"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
difficulty: advanced
tags:
  - android
  - kotlin-multiplatform
  - kmp
  - architecture
  - mobile-development
  - cross-platform
updated: "2026-02-12"
---

# Android Kotlin Multiplatform Architecture

**Objective:** Design a Kotlin Multiplatform (KMP) shared module architecture for an Android project — determining what to share across platforms (networking, data layer, business logic, ViewModels) vs. what to keep platform-specific (UI, system APIs, platform integrations), with complete Gradle configuration patterns, `expect`/`actual` strategy, and dependency management approach.

**When to Use:** Use this prompt when starting a new KMP project, when designing the shared module structure for an existing Android app expanding to other platforms, or when reviewing and improving an existing KMP architecture. This is the foundational architecture decision — get it right and cross-platform development is clean; get it wrong and you fight the framework.

**Sequence Map:** Use after concept validation; use before module design and shared-code scaffolding.

**Important context:** KMP (Kotlin Multiplatform) lets you share Kotlin code across Android, iOS, Desktop, and Web while keeping platform-specific code native. The key architectural insight is that KMP is not "write once, run everywhere" — it is "share what makes sense, go native where it matters." The sharing boundary is the most important design decision.

---

## Context Gathering

1. **Target Platforms:**
   - "Which platforms do you need to support (Android, iOS, Desktop JVM, Web/WASM)?"
   - "What is the priority order? Which platform ships first?"
   - "Are there platform-specific features that only exist on one platform?"

2. **App Architecture:**
   - "Describe the current architecture (MVVM, MVI, Clean Architecture layers)."
   - "How is state managed (StateFlow, LiveData, Redux-like)?"
   - "What networking library (Ktor recommended for KMP, Retrofit is Android-only)?"
   - "What database (SQLDelight for KMP, Room is Android-only)?"
   - "What DI approach (Koin for KMP, Hilt is Android-only)?"

3. **Team Context:**
   - "Does the team have iOS/Swift experience for implementing `actual` declarations?"
   - "How many developers will work on shared code vs. platform code?"
   - "What is the testing strategy per platform?"

---

## Instructions

### Step 1: Define the Sharing Boundary

Classify every architectural layer by sharing suitability:

| Layer | Share? | Rationale |
|-------|--------|-----------|
| **Domain Models** | YES — always | Pure Kotlin data classes, no platform dependencies |
| **Business Logic / Use Cases** | YES — always | Pure Kotlin functions, testable, platform-agnostic |
| **Repository Interfaces** | YES | Define contracts in common, implement per platform |
| **Networking** | YES (with Ktor) | Ktor is fully multiplatform, JSON via kotlinx.serialization |
| **Local Storage** | YES (with SQLDelight) | SQLDelight generates platform-specific drivers |
| **Settings/Preferences** | YES (with multiplatform-settings) | Wraps SharedPreferences/NSUserDefaults |
| **ViewModels / State Holders** | CONDITIONAL | Share if using kotlinx-coroutines StateFlow; don't share if using Android ViewModel features (SavedStateHandle) |
| **UI Components** | NO (or CMP) | Keep native unless using Compose Multiplatform |
| **Navigation** | NO (usually) | Platform navigation patterns differ significantly |
| **Platform APIs** | NO — abstract | Camera, biometrics, notifications → `expect`/`actual` |
| **DI Configuration** | PARTIAL | Koin modules can be shared; Hilt is Android-only |

### Step 2: Design Module Structure

```
project/
├── build-logic/                       # Convention plugins
│   └── convention/
│       ├── KmpLibraryConventionPlugin.kt
│       └── KmpApplicationConventionPlugin.kt
│
├── core/                              # Shared foundation modules
│   ├── core-model/                    # Domain models (commonMain only)
│   ├── core-network/                  # Ktor networking (commonMain + platform)
│   ├── core-database/                 # SQLDelight (commonMain + platform drivers)
│   ├── core-datastore/                # Settings/preferences (multiplatform-settings)
│   └── core-common/                   # Shared utilities, extensions, Result types
│
├── data/                              # Data layer modules
│   ├── data-repository/               # Repository implementations (commonMain)
│   └── data-sync/                     # Sync logic if needed (commonMain)
│
├── domain/                            # Business logic modules
│   ├── domain-usecase/                # Use cases (commonMain only, pure Kotlin)
│   └── domain-model/                  # Domain model extensions
│
├── feature/                           # Feature modules (per-screen or per-flow)
│   ├── feature-auth/
│   │   ├── commonMain/                # Shared ViewModel, state, events
│   │   ├── androidMain/               # Android-specific (if any)
│   │   └── iosMain/                   # iOS-specific (if any)
│   ├── feature-home/
│   └── feature-settings/
│
├── androidApp/                        # Android application
│   ├── src/main/
│   │   ├── ui/                        # Compose UI (Android Jetpack Compose)
│   │   ├── navigation/                # Navigation (Compose Navigation)
│   │   └── di/                        # Hilt modules (Android DI)
│   └── build.gradle.kts
│
└── iosApp/                            # iOS application (Xcode)
    ├── Sources/
    │   ├── UI/                        # SwiftUI views
    │   ├── Navigation/                # iOS navigation
    │   └── DI/                        # iOS DI setup
    └── iosApp.xcodeproj
```

### Step 3: Gradle Configuration Patterns

**Version Catalog (`gradle/libs.versions.toml`):**

```toml
[versions]
kotlin = "2.1.0"
ktor = "3.0.0"
sqldelight = "2.0.2"
coroutines = "1.9.0"
koin = "4.0.0"
multiplatformSettings = "1.2.0"

[libraries]
# Multiplatform
ktor-client-core = { group = "io.ktor", name = "ktor-client-core", version.ref = "ktor" }
ktor-client-android = { group = "io.ktor", name = "ktor-client-android", version.ref = "ktor" }
ktor-client-darwin = { group = "io.ktor", name = "ktor-client-darwin", version.ref = "ktor" }
ktor-serialization-json = { group = "io.ktor", name = "ktor-serialization-kotlinx-json", version.ref = "ktor" }
sqldelight-runtime = { group = "app.cash.sqldelight", name = "runtime", version.ref = "sqldelight" }
sqldelight-android = { group = "app.cash.sqldelight", name = "android-driver", version.ref = "sqldelight" }
sqldelight-native = { group = "app.cash.sqldelight", name = "native-driver", version.ref = "sqldelight" }
coroutines-core = { group = "org.jetbrains.kotlinx", name = "kotlinx-coroutines-core", version.ref = "coroutines" }
koin-core = { group = "io.insert-koin", name = "koin-core", version.ref = "koin" }
```

**Convention Plugin (KMP library module):**

```kotlin
// build-logic/convention/src/main/kotlin/KmpLibraryConventionPlugin.kt
class KmpLibraryConventionPlugin : Plugin<Project> {
    override fun apply(target: Project) = with(target) {
        with(pluginManager) {
            apply("org.jetbrains.kotlin.multiplatform")
        }
        extensions.configure<KotlinMultiplatformExtension> {
            androidTarget()
            listOf(iosX64(), iosArm64(), iosSimulatorArm64()).forEach {
                it.binaries.framework { baseName = project.name }
            }
            sourceSets {
                commonMain.dependencies {
                    implementation(libs.findLibrary("coroutines-core").get())
                }
                commonTest.dependencies {
                    implementation(kotlin("test"))
                }
            }
        }
    }
}
```

### Step 4: `expect`/`actual` Strategy

Define the rules for when to use `expect`/`actual`:

**Use `expect`/`actual` when:**
- A platform API has no multiplatform wrapper library
- Platform behavior genuinely differs (e.g., UUID generation, date formatting)
- You need platform-optimized implementations (e.g., image compression)

**Do NOT use `expect`/`actual` when:**
- A multiplatform library exists (Ktor, SQLDelight, kotlinx-datetime)
- You can use an interface + DI instead (more flexible, easier to test)
- The implementation is identical on all platforms

**Common `expect`/`actual` declarations:**

```kotlin
// commonMain
expect class PlatformContext  // Wraps Android Context / iOS nothing
expect fun getPlatformName(): String
expect fun createUUID(): String
expect class ImageCompressor {
    fun compress(data: ByteArray, quality: Int): ByteArray
}

// androidMain
actual class PlatformContext(val context: Context)
actual fun getPlatformName(): String = "Android ${Build.VERSION.SDK_INT}"
actual fun createUUID(): String = java.util.UUID.randomUUID().toString()

// iosMain
actual class PlatformContext  // No-op on iOS
actual fun getPlatformName(): String = UIDevice.currentDevice.systemName()
actual fun createUUID(): String = NSUUID().UUIDString
```

### Step 5: Testing Strategy

- **`commonTest`**: Test all shared business logic, repository logic, use cases. These tests run on all platforms.
- **`androidTest`**: Test Android-specific `actual` implementations, Android integrations.
- **`iosTest`**: Test iOS-specific `actual` implementations. Run via Xcode or KMP test tasks.
- **Mocking:** Use `kotlinx-coroutines-test` for coroutine testing. Use interfaces for testability (avoid `expect`/`actual` mocking complexity).

### Step 6: Common Pitfalls

1. **Over-sharing:** Don't force everything into `commonMain`. If it causes awkward abstractions, keep it platform-specific.
2. **Hilt in shared code:** Hilt is Android-only. Use Koin for shared DI, or keep DI in platform modules.
3. **Android ViewModel in shared code:** `androidx.lifecycle.ViewModel` is Android-only. Use a plain class with StateFlow for shared state holders.
4. **LiveData in shared code:** LiveData is Android-only. Use StateFlow (multiplatform).
5. **Gradle build time:** Each platform target adds compilation time. Use `--no-parallel` flag for debugging build issues. Consider limiting targets during development.
6. **iOS framework size:** The Kotlin/Native framework for iOS can be large. Use `-opt-in=kotlin.experimental.ExperimentalObjCRefinement` and `@HiddenFromObjC` to reduce API surface.

---

## Expected Output

1. **Sharing Boundary Document** — clear table of what is shared vs. platform-specific, with rationale for each decision
2. **Module Architecture Diagram** — visual representation of module dependencies
3. **Gradle Configuration** — complete `build.gradle.kts` files for the key modules
4. **`expect`/`actual` Inventory** — list of all declarations needed with implementation notes
5. **Dependency Migration Map** — current Android-only deps mapped to multiplatform alternatives
6. **Testing Strategy** — what is tested where (common vs. platform-specific)
7. **Build Verification** — confirm the project compiles for all target platforms

---

## CRITICAL: Verification Requirements

- [ ] All `commonMain` code compiles without Android SDK imports
- [ ] Every `expect` declaration has matching `actual` on all target platforms
- [ ] Android app builds and runs identically after KMP restructuring
- [ ] iOS framework compiles and links (even if iOS app is incomplete)
- [ ] Unit tests pass on all platforms (`./gradlew allTests`)
- [ ] Build time is measured and compared to pre-KMP baseline
- [ ] No circular module dependencies exist
