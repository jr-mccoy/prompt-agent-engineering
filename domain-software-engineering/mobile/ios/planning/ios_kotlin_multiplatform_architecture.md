---
title: "iOS Kotlin Multiplatform Architecture"
category: mobile-development
description: "Design iOS-side architecture for Kotlin Multiplatform (KMP) projects with shared business logic, native SwiftUI UI, and seamless Swift-Kotlin interop."
techniques:
  - ST-01
  - ST-02
  - RT-02
difficulty: advanced
tags:
  - ios
  - swift
  - kmp
  - kotlin
  - cross-platform
updated: "2026-03-20"
---

# iOS Kotlin Multiplatform Architecture

**Objective:** Design the iOS-side architecture for a Kotlin Multiplatform (KMP) project where business logic is shared in Kotlin, the UI is native SwiftUI, and the integration layer provides type-safe, ergonomic Swift APIs over the shared Kotlin module, with proper error handling, concurrency bridging, and dependency injection.

**When to Use:** Use when adopting KMP for an iOS project, migrating an existing iOS app to share code with Android, or designing the Swift integration layer for a KMP shared module. Essential when the team wants shared business logic but native platform UI.

**Prompt Type:** Comprehensive (400+ lines)

---

## Context Gathering

Before designing the architecture, gather essential context:

1. **Shared Code Scope:**
   - "What will be shared via KMP (networking, business logic, models, persistence)?"
   - "What stays platform-native (UI, platform APIs, navigation)?"
   - "Are there existing Kotlin shared modules or is this greenfield?"

2. **Team Structure:**
   - "Are there dedicated iOS and Android developers, or full-stack mobile?"
   - "Who owns the shared Kotlin module?"
   - "What is the team's Kotlin proficiency on the iOS side?"

3. **Technical Context:**
   - "What KMP framework version and tooling (SKIE, KMP-NativeCoroutines)?"
   - "What iOS minimum deployment target?"
   - "Is the shared module distributed as XCFramework or built from source?"
   - "What build system (Gradle KMP plugin, CocoaPods, SPM)?"

4. **Integration Requirements:**
   - "How should Kotlin coroutines be exposed to Swift (SKIE, KMP-NativeCoroutines, manual)?"
   - "Are Kotlin sealed classes used? How should they map to Swift?"
   - "What error handling pattern (Kotlin exceptions → Swift errors)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before designing ANY KMP integration, you MUST:**

1. **Define the shared/native boundary precisely** - Every type crossing the boundary must have a clear mapping.
2. **Choose a coroutine bridging strategy** - Kotlin coroutines do not natively map to Swift async/await without tooling.
3. **Plan the XCFramework distribution** - Local build vs. CI-built binary vs. SPM package.
4. **Handle nullability carefully** - Kotlin nullable types map to Swift optionals, but generics get complex.
5. **Test the interop layer** - Swift tests must cover the Kotlin-to-Swift boundary.

### False-Positive Prevention

- ❌ Do NOT assume Kotlin sealed classes map cleanly to Swift enums (they don't without SKIE)
- ❌ Do NOT call Kotlin suspend functions directly from Swift without bridging (will crash)
- ❌ Do NOT use Kotlin Flow directly in SwiftUI (needs AsyncSequence bridge)
- ❌ Do NOT ignore the Kotlin/Native memory model implications
- ❌ Do NOT distribute shared module as source to iOS developers unfamiliar with Gradle
- ✅ DO use SKIE or KMP-NativeCoroutines for idiomatic Swift interop
- ✅ DO create Swift wrapper types for complex Kotlin types
- ✅ DO keep the shared module API surface minimal and Swift-friendly
- ✅ DO test the interop boundary with Swift-side unit tests
- ✅ DO provide pre-built XCFramework for iOS developers who don't have Kotlin tooling

---

### Phase 1: Architecture Overview

#### 1.1 Layer Diagram

```
┌─────────────────────────────────────────────────────┐
│                 SwiftUI Views                        │
│            (100% native, platform-specific)           │
├─────────────────────────────────────────────────────┤
│              Swift ViewModels                         │
│        (@Observable, consume shared use cases)        │
├─────────────────────────────────────────────────────┤
│           Swift Integration Layer                     │
│    (Wraps Kotlin types, bridges coroutines/flows)     │
├─────────────────────────────────────────────────────┤
│          KMP Shared Module (XCFramework)              │
│   (Use cases, repositories, models, networking)       │
│              Written in Kotlin                        │
└─────────────────────────────────────────────────────┘
```

#### 1.2 What Goes Where

| Layer | Language | Contains | Example |
|-------|----------|----------|---------|
| **UI** | Swift/SwiftUI | Views, navigation, animations | `RecipeListScreen.swift` |
| **ViewModel** | Swift | State management, UI logic | `RecipeListViewModel.swift` |
| **Integration** | Swift | Kotlin type wrappers, async bridges | `RecipeUseCaseWrapper.swift` |
| **Shared** | Kotlin | Business logic, networking, models | `GetRecipesUseCase.kt` |

---

### Phase 2: Kotlin-to-Swift Interop

**CHECKPOINT 1:** Confirm shared module scope and distribution strategy.

```markdown
## KMP Configuration
- Shared module scope: [networking, models, business logic]
- Distribution: [Source / XCFramework / CocoaPods / SPM]
- Coroutine bridging: [SKIE / KMP-NativeCoroutines / Manual]
- Kotlin version: _
- KMP plugin version: _

**Proceed with interop design?**
```

#### 2.1 Coroutine Bridging with SKIE

```kotlin
// Shared Kotlin module: shared/src/commonMain/kotlin/com/app/shared/
// GetRecipesUseCase.kt

class GetRecipesUseCase(
    private val repository: RecipeRepository
) {
    // SKIE automatically converts this to Swift async function
    suspend fun execute(): List<Recipe> {
        return repository.getRecipes()
    }
}

// Kotlin Flow exposed as Swift AsyncSequence via SKIE
class ObserveRecipesUseCase(
    private val repository: RecipeRepository
) {
    fun execute(): Flow<List<Recipe>> {
        return repository.observeRecipes()
    }
}
```

```swift
// iOS-side: Swift ViewModel consuming SKIE-bridged shared code
// File: Features/Recipes/RecipeListViewModel.swift

import SharedModule
import SwiftUI

@Observable
final class RecipeListViewModel {
    enum State: Equatable {
        case idle, loading, loaded([Recipe]), error(String)
    }

    private(set) var state: State = .idle

    private let getRecipes: GetRecipesUseCase
    private let observeRecipes: ObserveRecipesUseCase

    init(
        getRecipes: GetRecipesUseCase = .init(repository: KoinHelper.shared.recipeRepository),
        observeRecipes: ObserveRecipesUseCase = .init(repository: KoinHelper.shared.recipeRepository)
    ) {
        self.getRecipes = getRecipes
        self.observeRecipes = observeRecipes
    }

    func load() async {
        state = .loading
        do {
            // SKIE makes this a native Swift async call
            let recipes = try await getRecipes.execute()
            state = recipes.isEmpty ? .loaded([]) : .loaded(recipes)
        } catch {
            state = .error(error.localizedDescription)
        }
    }

    func observe() async {
        // SKIE converts Kotlin Flow to Swift AsyncSequence
        for await recipes in observeRecipes.execute() {
            state = .loaded(recipes)
        }
    }
}
```

#### 2.2 Sealed Class Mapping

```kotlin
// Kotlin sealed class
sealed class NetworkResult<out T> {
    data class Success<T>(val data: T) : NetworkResult<T>()
    data class Error(val message: String) : NetworkResult<Nothing>()
    object Loading : NetworkResult<Nothing>()
}
```

```swift
// Without SKIE: Kotlin sealed classes become awkward in Swift
// The generated Swift code requires instanceof checks:
if let success = result as? NetworkResultSuccess<NSArray> {
    // Awkward, untyped
}

// With SKIE: Sealed classes become Swift enums automatically
// SKIE generates:
switch result {
case .success(let data):
    // Typed, idiomatic Swift
case .error(let message):
    // Clean pattern matching
case .loading:
    break
}
```

#### 2.3 Dependency Injection Bridge

```kotlin
// Shared module: Koin DI setup
// shared/src/commonMain/kotlin/com/app/shared/di/SharedModule.kt

val sharedModule = module {
    single<RecipeRepository> { RecipeRepositoryImpl(get()) }
    factory { GetRecipesUseCase(get()) }
    factory { ObserveRecipesUseCase(get()) }
}

// iOS-specific Koin helper
// shared/src/iosMain/kotlin/com/app/shared/di/KoinHelper.kt

class KoinHelper {
    companion object {
        val shared = KoinHelper()
    }

    val recipeRepository: RecipeRepository
        get() = getKoin().get()

    fun getRecipesUseCase(): GetRecipesUseCase = getKoin().get()
}
```

```swift
// iOS-side: Bridge Koin to Swift DI
// File: Core/DI/SharedDependencies.swift

import SharedModule

enum SharedDependencies {
    static func setup() {
        // Initialize Koin from Swift
        KoinHelperKt.doInitKoin()
    }

    static var recipeRepository: RecipeRepository {
        KoinHelper.shared.recipeRepository
    }

    static func getRecipesUseCase() -> GetRecipesUseCase {
        KoinHelper.shared.getRecipesUseCase()
    }
}
```

---

### Phase 3: XCFramework Distribution

#### 3.1 Build Configuration

```kotlin
// shared/build.gradle.kts

kotlin {
    listOf(
        iosX64(),
        iosArm64(),
        iosSimulatorArm64()
    ).forEach { iosTarget ->
        iosTarget.binaries.framework {
            baseName = "SharedModule"
            isStatic = true // Static framework for better app startup
        }
    }
}
```

#### 3.2 Distribution Options

| Method | Pros | Cons | Best For |
|--------|------|------|---------|
| **Local build** | Always latest, debuggable | Requires JDK + Gradle on iOS dev machine | Small team, co-located |
| **CI-built XCFramework** | No Kotlin tooling on iOS | Version lag, larger artifacts | Separate iOS/Android teams |
| **SPM package** | Standard iOS integration | Complex CI setup | Open source distribution |
| **CocoaPods** | KMP plugin support | Legacy tool | Existing CocoaPods project |

#### 3.3 CI Pipeline for XCFramework

```yaml
# .github/workflows/build-xcframework.yml
name: Build XCFramework

on:
  push:
    paths: ['shared/**']
    branches: [main]

jobs:
  build:
    runs-on: macos-14
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'temurin'

      - name: Build XCFramework
        run: ./gradlew :shared:assembleXCFramework

      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: SharedModule.xcframework
          path: shared/build/XCFrameworks/release/
```

---

### Phase 4: Testing the Boundary

**CHECKPOINT 2:** Review interop layer before testing strategy.

```markdown
## Interop Summary
- Coroutine bridging: SKIE / KMP-NativeCoroutines
- Sealed class mapping: SKIE enums / Manual wrappers
- DI bridge: Koin → Swift helper
- Distribution: [Method]

**Proceed with testing strategy?**
```

#### 4.1 Interop Test Strategy

```swift
// File: Tests/Integration/SharedModuleInteropTests.swift

import XCTest
import SharedModule

final class SharedModuleInteropTests: XCTestCase {

    func testRecipeModelMapsCorrectly() {
        // Verify Kotlin data class properties are accessible from Swift
        let recipe = Recipe(
            id: "1",
            title: "Pasta",
            ingredients: ["flour", "eggs"],
            cookTime: 30
        )

        XCTAssertEqual(recipe.id, "1")
        XCTAssertEqual(recipe.title, "Pasta")
        XCTAssertEqual(recipe.ingredients.count, 2)
        XCTAssertEqual(recipe.cookTime, 30)
    }

    func testSuspendFunctionBridge() async throws {
        // Verify Kotlin suspend function works as Swift async
        let useCase = GetRecipesUseCase(
            repository: FakeRecipeRepository()
        )
        let recipes = try await useCase.execute()
        XCTAssertFalse(recipes.isEmpty)
    }

    func testFlowBridge() async {
        // Verify Kotlin Flow works as Swift AsyncSequence
        let useCase = ObserveRecipesUseCase(
            repository: FakeRecipeRepository()
        )

        var collected: [[Recipe]] = []
        for await recipes in useCase.execute().prefix(2) {
            collected.append(recipes)
        }

        XCTAssertEqual(collected.count, 2)
    }

    func testErrorBridge() async {
        // Verify Kotlin exceptions map to Swift errors
        let useCase = GetRecipesUseCase(
            repository: FailingRecipeRepository()
        )

        do {
            _ = try await useCase.execute()
            XCTFail("Expected error")
        } catch {
            // Verify error is meaningful, not just KotlinException
            XCTAssertFalse(error.localizedDescription.isEmpty)
        }
    }
}
```

---

### Phase 5: Common Pitfalls

#### 5.1 Known Issues and Solutions

| Issue | Cause | Solution |
|-------|-------|---------|
| `KotlinException` with no message | Unhandled Kotlin exception | Use `@Throws` annotation on Kotlin functions |
| Frozen object mutation crash | Kotlin/Native old memory model | Ensure new memory model is enabled |
| Generic type erasure | Kotlin generics in ObjC interop | Use concrete types or SKIE |
| Slow build times | Full Kotlin compilation on each build | Use pre-built XCFramework |
| Missing nullability | Kotlin platform types | Explicitly annotate nullability in shared API |
| Swift `any` protocol issues | Kotlin interfaces in Swift 6 | Use SKIE's protocol mapping |

#### 5.2 Performance Considerations

```markdown
| Concern | Mitigation |
|---------|-----------|
| Kotlin/Native startup overhead | Use static framework, preload in AppDelegate |
| Object conversion at boundary | Minimize boundary crossings, pass primitives/lists |
| Memory: Kotlin objects in Swift | Use Kotlin's new memory manager (default since 1.7.20) |
| Binary size from shared module | Strip unused code with `-Xbinary=stripDebugSymbols` |
```

---

## Expected Output

```
KMP iOS Architecture Document
├── Layer Diagram (UI → ViewModel → Integration → Shared)
├── Interop Patterns
│   ├── Coroutine → async/await bridging
│   ├── Sealed class → Swift enum mapping
│   └── DI bridge (Koin → Swift)
├── XCFramework Distribution Strategy
├── Testing Plan (boundary tests)
└── Common Pitfalls Reference
```

---

## Example Interaction

**User:** "We have an Android app with business logic in Kotlin. We want to reuse it for iOS with SwiftUI. Team of 3 Android devs and 2 iOS devs."

**Assistant:**

**Recommended approach:**

1. **Extract shared module** from Android app into `shared/` KMP module containing: repositories, use cases, models, networking (Ktor)
2. **Use SKIE** for seamless Swift interop (suspend → async, sealed → enum, Flow → AsyncSequence)
3. **Distribute as CI-built XCFramework** so iOS devs don't need Kotlin/Gradle tooling
4. **iOS devs own:** SwiftUI views, ViewModels, navigation, platform APIs (HealthKit, etc.)
5. **Android devs own:** shared module, Kotlin API surface design

**Key rule:** The shared module API should be designed for Swift consumption. If it feels awkward in Swift, redesign the Kotlin API. The iOS team should review shared module PRs.

---

## Techniques Used

- **ST-01** (Clear Objective): Design iOS-side KMP architecture with clear boundaries
- **ST-02** (Sequential Instructions): Five-phase design from overview to pitfalls
- **RT-02** (Multi-Dimensional Analysis): Covers interop, distribution, testing, and performance

---

## Related Prompts

- [ios_architecture_selection.md](ios_architecture_selection.md) - iOS-side architecture within KMP context
- [ios_module_design.md](ios_module_design.md) - Module structure for iOS-native code alongside shared module
- [ios_tech_stack_selection.md](ios_tech_stack_selection.md) - Technology choices for the native iOS layer

---

## Customization Guide

### For Compose Multiplatform (Shared UI)
If sharing UI via Compose Multiplatform, the iOS layer becomes thinner. Replace the SwiftUI layer with Compose views, keeping only platform-specific screens (App Store review, HealthKit) in SwiftUI.

### For Gradual KMP Adoption
Start by sharing only models and networking. Keep business logic native initially. Migrate use cases to shared module one at a time, validating interop quality at each step.

### For Large Teams
Add a dedicated "platform interface" layer in the shared module that iOS and Android teams agree on. Use Kotlin `expect/actual` sparingly -- prefer dependency injection for platform differences.
