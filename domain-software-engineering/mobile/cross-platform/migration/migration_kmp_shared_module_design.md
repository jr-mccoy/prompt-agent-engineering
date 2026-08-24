---
title: "KMP Shared Module Design"
category: mobile-development
description: "Design Kotlin Multiplatform shared modules with clear expect/actual boundaries, SKIE configuration, and Gradle/SPM integration for Android and iOS"
techniques:
  - ST-01
  - RT-02
  - RT-04
  - DS-02
difficulty: advanced
tags:
  - ios
  - android
  - migration
  - kmp
  - kotlin-multiplatform
  - shared-module
  - gradle
  - spm
updated: "2026-03-19"
---

# KMP Shared Module Design

**Objective:** Design a Kotlin Multiplatform (KMP) shared module architecture that maximizes code reuse between Android and iOS while maintaining clean platform boundaries. The output includes module structure, expect/actual declarations, SKIE configuration for Swift-friendly APIs, and build system integration via Gradle and Swift Package Manager.

**When to Use:** When a team has decided to use KMP to share business logic between Android and iOS. This prompt is most valuable during the initial architecture phase when determining what to share, how to define platform boundaries, and how to integrate the shared module into both platform projects.

**Prompt Type:** Comprehensive (~320 lines)

## Context Gathering

1. What business logic do you want to share? (e.g., networking, data models, validation, use cases)
2. What platform-specific features need expect/actual declarations? (e.g., file I/O, secure storage, analytics)
3. What is the current Android project structure? (e.g., single module, multi-module)
4. What iOS dependency management is in use? (CocoaPods, SPM, or direct framework embedding)
5. Are you using any serialization libraries? (e.g., kotlinx.serialization, Moshi)
6. What networking library is used on Android? (e.g., Ktor, Retrofit)
7. Do you need to expose Coroutines/Flow to iOS? (SKIE vs. manual wrapping)
8. What is the minimum iOS deployment target?
9. What Kotlin version and KMP plugin version are you targeting?
10. Are there any existing shared modules or KMP experiments in the project?

## Instructions

### CRITICAL: Verification Requirements

- Module boundaries MUST be validated by confirming each shared type compiles on both targets
- expect/actual declarations MUST have matching signatures verified by the Kotlin compiler
- SKIE configuration MUST be tested with actual Swift consumer code
- SPM integration MUST be verified with a clean build from Xcode

### False-Positive Prevention

- ❌ DO NOT share UI code through KMP (Compose Multiplatform is a separate concern)
- ✅ DO share business logic, data models, networking, and validation
- ❌ DO NOT expose raw Kotlin Coroutines to Swift without SKIE or wrapper layer
- ✅ DO use SKIE to generate Swift-friendly async/await wrappers for suspend functions and Flow
- ❌ DO NOT assume all Kotlin stdlib types map cleanly to Swift (e.g., Kotlin `Map` → `NSDictionary` without SKIE)
- ✅ DO verify type mapping in the generated Objective-C/Swift headers
- ❌ DO NOT put platform-specific imports in shared code without expect/actual
- ✅ DO use expect/actual for every platform-divergent implementation

### Step 1: Define Module Boundaries

Determine what belongs in the shared module vs. platform-specific modules:

```
shared/
├── commonMain/          # Pure Kotlin — runs on all platforms
│   ├── models/          # Data classes, sealed classes, enums
│   ├── domain/          # Use cases, business rules
│   ├── repository/      # Repository interfaces
│   ├── network/         # Ktor client, API definitions
│   └── util/            # Validation, formatting, extensions
├── androidMain/         # Android-specific implementations
│   ├── platform/        # Android actual declarations
│   └── di/              # Koin/Hilt module bindings
├── iosMain/             # iOS-specific implementations
│   ├── platform/        # iOS actual declarations
│   └── di/              # Koin module bindings for iOS
├── commonTest/          # Shared tests
├── androidUnitTest/     # Android-specific tests
└── iosTest/             # iOS-specific tests
```

### Step 2: Implement expect/actual Declarations

**Kotlin (commonMain — expect declaration):**
```kotlin
// shared/src/commonMain/kotlin/com/app/platform/Platform.kt
expect class PlatformContext

expect class SecureStorage(context: PlatformContext) {
    fun getString(key: String): String?
    fun putString(key: String, value: String)
    fun remove(key: String)
    fun clear()
}

expect fun createPlatformLogger(tag: String): PlatformLogger

interface PlatformLogger {
    fun debug(message: String)
    fun info(message: String)
    fun error(message: String, throwable: Throwable? = null)
}
```

**Kotlin (androidMain — actual declaration):**
```kotlin
// shared/src/androidMain/kotlin/com/app/platform/Platform.android.kt
actual typealias PlatformContext = android.content.Context

actual class SecureStorage actual constructor(
    private val context: PlatformContext
) {
    private val prefs = EncryptedSharedPreferences.create(
        context,
        "secure_prefs",
        MasterKey.Builder(context).setKeyScheme(
            MasterKey.KeyScheme.AES256_GCM
        ).build(),
        EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
        EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
    )

    actual fun getString(key: String): String? = prefs.getString(key, null)
    actual fun putString(key: String, value: String) {
        prefs.edit().putString(key, value).apply()
    }
    actual fun remove(key: String) { prefs.edit().remove(key).apply() }
    actual fun clear() { prefs.edit().clear().apply() }
}
```

**Kotlin (iosMain — actual declaration):**
```kotlin
// shared/src/iosMain/kotlin/com/app/platform/Platform.ios.kt
import platform.Foundation.NSBundle
import platform.Security.*
import kotlinx.cinterop.*

actual class PlatformContext

actual class SecureStorage actual constructor(
    private val context: PlatformContext
) {
    private val serviceName = NSBundle.mainBundle.bundleIdentifier ?: "com.app"

    actual fun getString(key: String): String? {
        val query = keychainQuery(key) + mapOf(
            kSecReturnData to true,
            kSecMatchLimit to kSecMatchLimitOne
        )
        // Keychain query implementation
        return keychainGet(query)
    }

    actual fun putString(key: String, value: String) {
        keychainSet(key, value)
    }

    actual fun remove(key: String) { keychainDelete(key) }
    actual fun clear() { keychainDeleteAll() }
}
```

### Step 3: Configure SKIE for Swift-Friendly APIs

**Gradle (SKIE configuration):**
```kotlin
// shared/build.gradle.kts
plugins {
    kotlin("multiplatform")
    kotlin("plugin.serialization")
    id("co.touchlab.skie") version "0.9.3"
}

kotlin {
    androidTarget {
        compilations.all {
            kotlinOptions { jvmTarget = "17" }
        }
    }

    listOf(iosX64(), iosArm64(), iosSimulatorArm64()).forEach {
        it.binaries.framework {
            baseName = "Shared"
            isStatic = true
        }
    }

    sourceSets {
        commonMain.dependencies {
            implementation("io.ktor:ktor-client-core:2.3.12")
            implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.9.0")
            implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.3")
        }
        androidMain.dependencies {
            implementation("io.ktor:ktor-client-okhttp:2.3.12")
        }
        iosMain.dependencies {
            implementation("io.ktor:ktor-client-darwin:2.3.12")
        }
    }
}

skie {
    features {
        enableSwiftUIObservingPreview = true
        coroutinesInterop.set(true)
    }
    analytics { enabled.set(false) }
}
```

**Kotlin (shared suspend function):**
```kotlin
// shared/src/commonMain/kotlin/com/app/domain/GetUserUseCase.kt
class GetUserUseCase(private val repository: UserRepository) {
    suspend fun invoke(userId: String): Result<User> {
        return repository.getUser(userId)
    }
}
```

**Swift (consuming SKIE-generated async wrapper):**
```swift
// iOS project — SKIE automatically generates Swift async/await
import Shared

class UserViewModel: ObservableObject {
    @Published var user: User?
    @Published var error: String?

    private let getUserUseCase: GetUserUseCase

    init(getUserUseCase: GetUserUseCase) {
        self.getUserUseCase = getUserUseCase
    }

    func loadUser(id: String) async {
        // SKIE converts `suspend fun` → Swift `async` automatically
        let result = try? await getUserUseCase.invoke(userId: id)
        if let user = result?.getOrNull() {
            self.user = user
        }
    }
}
```

### Step 4: SPM Integration

**Package.swift (consuming KMP framework via SPM):**
```swift
// Package.swift at the repo root or a local package
// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "SharedKMP",
    platforms: [.iOS(.v16)],
    products: [
        .library(name: "Shared", targets: ["Shared"])
    ],
    targets: [
        .binaryTarget(
            name: "Shared",
            path: "shared/build/XCFrameworks/release/Shared.xcframework"
        )
    ]
)
```

**Gradle task to build XCFramework:**
```kotlin
// shared/build.gradle.kts
tasks.register("buildXCFramework") {
    dependsOn("assembleSharedReleaseXCFramework")
    description = "Builds XCFramework for SPM consumption"
}
```

### Step 5: Shared Testing Strategy

**Kotlin (commonTest):**
```kotlin
// shared/src/commonTest/kotlin/com/app/domain/GetUserUseCaseTest.kt
class GetUserUseCaseTest {
    private val fakeRepository = FakeUserRepository()
    private val useCase = GetUserUseCase(fakeRepository)

    @Test
    fun `returns user when repository succeeds`() = runTest {
        fakeRepository.setUser(User(id = "1", name = "Alice"))
        val result = useCase.invoke("1")
        assertTrue(result.isSuccess)
        assertEquals("Alice", result.getOrNull()?.name)
    }

    @Test
    fun `returns failure when user not found`() = runTest {
        val result = useCase.invoke("unknown")
        assertTrue(result.isFailure)
    }
}
```

## Expected Output

1. **Module structure diagram** showing shared/commonMain, androidMain, iosMain boundaries
2. **expect/actual declaration inventory** for all platform-divergent features
3. **SKIE configuration** with verified Swift interop for suspend functions and Flow
4. **Build configuration** for Gradle (Android + KMP) and SPM/CocoaPods (iOS)
5. **Test plan** covering commonTest, androidUnitTest, and iosTest

## Example Interaction

**User:** We want to share our networking layer (Ktor), data models, and business logic use cases. We use SPM on iOS and Gradle on Android.

**Assistant:**

### Shared Module Architecture

```
shared/
├── commonMain/
│   ├── models/          # @Serializable data classes
│   ├── network/         # Ktor HttpClient, API service interfaces
│   ├── domain/          # Use cases consuming repository interfaces
│   ├── repository/      # Repository interfaces (expect for platform storage)
│   └── di/              # Koin common modules
├── androidMain/
│   ├── network/         # OkHttp engine configuration
│   └── platform/        # EncryptedSharedPreferences, Android logging
├── iosMain/
│   ├── network/         # Darwin engine configuration
│   └── platform/        # Keychain, os_log
```

### Key expect/actual Boundaries

| Feature | commonMain (expect) | androidMain (actual) | iosMain (actual) |
|---------|-------------------|---------------------|-----------------|
| HTTP Engine | `expect fun createHttpEngine()` | `OkHttp` | `Darwin` |
| Secure Storage | `expect class SecureStorage` | `EncryptedSharedPreferences` | `Keychain` |
| Logging | `expect fun platformLog()` | `android.util.Log` | `os_log` |
| UUID | `expect fun randomUUID()` | `java.util.UUID` | `NSUUID` |

## Techniques Used

| Technique | Application |
|-----------|-------------|
| **ST-01: Structured Task Decomposition** | Breaking module design into boundaries, expect/actual, SKIE, and build steps |
| **RT-02: Contextual Reference Integration** | KMP documentation, SKIE documentation, SPM specification |
| **RT-04: Comparative Analysis Framework** | Android vs. iOS actual implementations side by side |
| **DS-02: Output Specification Framework** | Module structure, configuration files, test plan deliverables |

## Related Prompts

- `migration_android_to_ios_strategy.md` — Overall migration strategy (KMP is one approach)
- `migration_coroutines_to_swift_concurrency.md` — Deep dive on async interop
- `migration_gradle_to_spm_xcode.md` — Build system details for SPM integration
- `migration_hilt_to_swift_di.md` — DI patterns for shared module consumers

## Customization Guide

- **CocoaPods Instead of SPM:** Replace the SPM binary target with `cocoapods {}` block in `build.gradle.kts` and use `pod install` on iOS side.
- **Compose Multiplatform:** If sharing UI as well, add `org.jetbrains.compose` plugin and create `composeApp` module separate from `shared` business logic.
- **No SKIE:** If SKIE is not an option, manually create wrapper classes with `@ObjCName` annotations and callback-based async patterns for iOS consumption.
- **Mono-repo vs. Multi-repo:** If KMP shared module is in a separate repo, publish to Maven (Android) and a binary SPM registry (iOS) instead of local path references.
