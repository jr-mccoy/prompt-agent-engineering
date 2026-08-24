---
title: "Android/Kotlin Best Practices Review"
category: mobile-development
description: "Analyzes Android applications for adherence to modern architecture patterns, Jetpack libraries, and optimal Kotlin language feature usage"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - mobile-development
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/ai_code_review_android.md
  - domain-software-engineering/mobile/android/analysis/android_architecture_review.md
  - domain-software-engineering/mobile/android/improvement/android_kotlin_refactoring.md
---


# Android/Kotlin Best Practices Review

**Objective:** Analyze Android applications built with Kotlin to ensure adherence to Android best practices, modern architecture patterns, and optimal use of Jetpack libraries and Kotlin language features.

**When to Use:** Use this prompt when reviewing Android codebases for code quality, modernization opportunities, or compliance with Google's recommended Android development practices. Ideal for architecture reviews, migration planning (Java to Kotlin, legacy to Jetpack), and onboarding.

**Instructions:**

### CRITICAL: Verification Requirements

**Before flagging ANY best practice violation, you MUST:**

1. **Trace the actual code path** - Don't flag based on pattern matching alone. Verify the code actually exhibits the anti-pattern you're identifying.
2. **Check for intentional decisions** - Search for evidence that the pattern is deliberate (comments, architectural decisions, project constraints).
3. **Understand the context** - Consider WHY the code was written this way. Legacy requirements, team expertise, or specific use cases may justify the approach.
4. **Confirm actual impact** - Will following the "best practice" genuinely improve the codebase, or is the current approach acceptable for this context?
5. **Provide specific file:line locations** - Every finding MUST include exact code locations with line numbers.

**Finding code that ALREADY FOLLOWS best practices is an acceptable outcome.** If the codebase is well-structured for its requirements, say so with confidence. Don't manufacture violations to fill a report.

### False-Positive Prevention

- ❌ Do NOT flag code as violating best practices without verifying the actual pattern
- ❌ Do NOT recommend changes that would break working, tested code
- ❌ Do NOT flag acceptable alternatives as "wrong" (e.g., LiveData vs StateFlow when both are appropriate)
- ❌ Do NOT assume missing patterns without searching for them first
- ✅ DO trace complete code flows before flagging anti-patterns
- ✅ DO understand Android platform-specific patterns that may differ from general best practices
- ✅ DO consider the project's target API level and backward compatibility requirements
- ✅ DO acknowledge when code follows best practices, even if different from your preference

---

1. **Architecture Pattern Assessment:**
   * Identify the architecture pattern in use (MVC, MVP, MVVM, MVI, Clean Architecture)
   * Evaluate adherence to Android Architecture Components
   * Check for proper separation of concerns across layers
   * Review implementation of recommended app architecture (UI layer, Domain layer, Data layer)
   * Assess use of single activity vs. multiple activities pattern

2. **Kotlin Language Features Usage:**
   * Review proper use of Kotlin idioms and best practices
   * Check for null safety patterns (proper use of `?`, `!!`, `?.let`, `?:`)
   * Evaluate use of data classes, sealed classes, and object declarations
   * Assess coroutines usage for asynchronous operations
   * Check for extension functions and higher-order functions
   * Review use of destructuring, scope functions (let, run, with, apply, also)
   * Evaluate delegation patterns and property delegates
   * Check for proper use of companion objects vs. top-level functions

3. **Jetpack Libraries Integration:**
   * **ViewModel:** Check for proper ViewModel usage, no Context references, lifecycle awareness
   * **LiveData/Flow:** Evaluate observable data pattern implementation
   * **Room Database:** Review database schema, DAOs, type converters, migrations
   * **Navigation Component:** Assess navigation graph usage and deep linking
   * **WorkManager:** Check for proper background work scheduling
   * **Paging 3:** Evaluate large dataset handling
   * **Hilt/Dagger:** Review dependency injection setup
   * **Compose:** Check for modern UI development with Jetpack Compose
   * **DataStore:** Assess SharedPreferences replacement
   * **Lifecycle:** Review lifecycle-aware components

4. **UI Layer Analysis:**
   * **XML-based UI:** Review layouts, ViewBinding/DataBinding usage, custom views
   * **Jetpack Compose:** Analyze composable functions, state management, recomposition optimization
   * Check for proper theme and style implementation
   * Evaluate accessibility features (content descriptions, touch targets)
   * Review responsive design and multi-screen support
   * Assess animation implementations
   * Check for proper handling of configuration changes

5. **Data Layer and Repository Pattern:**
   * Review repository implementations and data source abstraction
   * Check for proper separation between local and remote data sources
   * Evaluate caching strategies and data synchronization
   * Assess use of Kotlin Flow or LiveData for reactive data streams
   * Review data mapping between layers (DTO to Domain to UI models)

6. **Networking:**
   * Review networking library usage (Retrofit, OkHttp, Ktor)
   * Check for proper API interface definitions
   * Evaluate request/response serialization (Gson, Moshi, kotlinx.serialization)
   * Review error handling and retry mechanisms
   * Assess authentication and token management
   * Check for proper timeout configurations
   * Evaluate SSL pinning and network security config

7. **Concurrency and Coroutines:**
   * Review coroutine scope usage (viewModelScope, lifecycleScope, GlobalScope usage)
   * Check for proper dispatcher usage (Main, IO, Default)
   * Evaluate structured concurrency implementation
   * Assess error handling in coroutines (try-catch, CoroutineExceptionHandler)
   * Check for potential leaks with GlobalScope
   * Review use of suspend functions vs. callback-based APIs
   * Evaluate Flow operators and collection

8. **Dependency Injection:**
   * Review DI framework usage (Hilt, Dagger, Koin, manual DI)
   * Check for proper module organization
   * Evaluate scope definitions (Singleton, ActivityScoped, ViewModelScoped)
   * Assess constructor injection vs. field injection
   * Check for circular dependencies
   * Review provision of interfaces vs. implementations

9. **Testing:**
   * Review unit test coverage and organization
   * Check for proper use of test doubles (mocks, fakes, stubs)
   * Evaluate UI tests (Espresso, Compose UI Testing)
   * Assess integration test coverage
   * Review test-driven development practices
   * Check for proper use of testing libraries (JUnit, Mockito, MockK, Truth)
   * Evaluate test maintainability and readability

10. **Performance Optimization:**
    * Check for memory leaks (Context leaks, static references)
    * Review RecyclerView implementations (ViewHolder pattern, DiffUtil)
    * Evaluate image loading and caching (Glide, Coil, Picasso)
    * Check for unnecessary object allocations in hot paths
    * Review ANR prevention (no blocking operations on main thread)
    * Assess app startup time optimization
    * Check for proper Compose performance (remember, derivedStateOf, LaunchedEffect)
    * Review ProGuard/R8 configuration

11. **Security Best Practices:**
    * Review data storage security (encryption, KeyStore usage)
    * Check for hardcoded secrets or credentials
    * Evaluate network security (HTTPS enforcement, certificate pinning)
    * Review authentication implementation
    * Check for proper permissions handling and runtime permissions
    * Assess WebView security if used
    * Review code obfuscation setup

12. **Resource Management:**
    * Review proper resource cleanup (closeable resources, cancel coroutines)
    * Check for proper use of resource qualifiers (language, screen size, density)
    * Evaluate string externalization and localization
    * Review drawable optimization and vector graphics usage
    * Check for proper handling of landscape/portrait modes

13. **Build Configuration:**
    * Review Gradle build files organization
    * Check for proper build variant configuration (debug, release, staging)
    * Evaluate dependency management (version catalogs, buildSrc)
    * Review build performance optimizations
    * Check for proper signing configuration
    * Assess modularization strategy

14. **Android Lint and Code Quality:**
    * Review Android Lint warnings and suppressions
    * Check for deprecated API usage
    * Evaluate code style consistency (ktlint, detekt)
    * Review TODO and FIXME comments
    * Check for suppressed warnings and their justification

**Expected Output:** A comprehensive best practices review report including:

1. **Executive Summary:**
   - Overall code quality assessment (Excellent/Good/Moderate/Needs Improvement)
   - Architecture pattern identified
   - Key technology stack (Jetpack libraries, Kotlin version, etc.)
   - Critical issues count by severity

2. **Detailed Analysis by Category:**
   - For each section above:
     - Current implementation description
     - Code examples showing patterns
     - Compliance with best practices (Compliant/Partially Compliant/Non-Compliant)
     - Issues identified with severity levels
     - Specific recommendations

3. **Critical Findings:**
   - Security vulnerabilities
   - Performance issues
   - Memory leaks
   - Crash risks
   - Deprecated API usage

4. **Modernization Opportunities:**
   - Migration to Jetpack Compose (if using XML)
   - Coroutines migration (if using callbacks/RxJava)
   - Hilt migration (if using Dagger or no DI)
   - ViewBinding/DataBinding improvements
   - Room database modernization

5. **Code Examples:**
   - Before/after comparisons for recommendations
   - Reference to specific files and line numbers
   - Best practice implementations to adopt

6. **Prioritized Action Items:**
   - Critical fixes (security, crashes)
   - High-priority improvements (performance, memory)
   - Medium-priority enhancements (modernization, refactoring)
   - Low-priority optimizations (code style, minor improvements)

**Example Output:**

```
# Android/Kotlin Best Practices Review Report

## Executive Summary
- **Overall Assessment:** Good with modernization opportunities
- **Architecture:** MVVM with Repository pattern
- **Technology Stack:** Kotlin 1.9, Jetpack Compose + XML hybrid, Hilt, Retrofit, Room
- **Critical Issues:** 2 | High Priority: 5 | Medium: 12 | Low: 8

## Detailed Findings

### 1. Architecture Pattern (Status: Good)
**Compliance:** Compliant

**Strengths:**
- Clean MVVM implementation with clear separation
- Proper use of Repository pattern
- ViewModels correctly scoped and lifecycle-aware

**Code Example:**
File: `features/dashboard/DashboardViewModel.kt`
```kotlin
class DashboardViewModel @Inject constructor(
    private val repository: DashboardRepository
) : ViewModel() {

    private val _uiState = MutableStateFlow<DashboardUiState>(DashboardUiState.Loading)
    val uiState: StateFlow<DashboardUiState> = _uiState.asStateFlow()

    init {
        loadDashboard()
    }

    private fun loadDashboard() {
        viewModelScope.launch {
            repository.getDashboardData()
                .collect { result ->
                    _uiState.value = when(result) {
                        is Result.Success -> DashboardUiState.Success(result.data)
                        is Result.Error -> DashboardUiState.Error(result.exception)
                    }
                }
        }
    }
}
```

### 2. Kotlin Language Features (Status: Moderate)
**Compliance:** Partially Compliant

**Issues Found:**
- **Critical:** Force unwrapping (!!) used in 15 locations without null checks
- **High:** Inconsistent null safety patterns

**Code Example - Issue:**
File: `utils/UserHelper.kt:42`
```kotlin
// Current - Dangerous force unwrapping
fun getUserName(): String {
    return PreferenceManager.getUser()!!.name  // Can crash if null
}
```

**Recommended Fix:**
```kotlin
// Better approach with elvis operator and default
fun getUserName(): String {
    return PreferenceManager.getUser()?.name ?: "Guest"
}

// Or handle null explicitly
fun getUserName(): String? {
    return PreferenceManager.getUser()?.name
}
```

[... more detailed sections ...]

## Prioritized Action Items

### Critical (Fix Immediately)
1. **Replace force unwrapping (!!!) with safe calls** - 15 instances in `utils/` and `data/`
   - Risk: App crashes on null values
   - Effort: 2-4 hours

2. **Fix Context leak in Singleton** - `NetworkManager` holds Activity context
   - Risk: Memory leak
   - File: `network/NetworkManager.kt:25`
   - Effort: 30 minutes

### High Priority (This Sprint)
1. **Migrate deprecated LiveData to StateFlow** - 12 ViewModels still using LiveData
   - Benefits: Better coroutine integration, type safety
   - Effort: 1-2 days

[... more action items ...]
```

**Techniques Used:**
- ST-01 (Clear Objective)
- ST-02 (Sequential Instructions)
- RT-02 (Multi-Dimensional Analysis)
- RT-04 (Best Practice Review)
- ST-03 (Structured Output Templates)
- OC-05 (Severity Classification)

**Related Prompts:**
- `ios_swift_architecture_review.md` - For comparing iOS/Android architectural patterns
- `mobile_app_security_review.md` - For deeper security analysis
- `cross_platform_architecture_design.md` - For apps with cross-platform considerations
- `code_quality_code_style_consistency.md` - For Kotlin style guide analysis

**Customization Guide:**
- For pure Compose apps: Focus on Compose-specific sections, skip XML UI analysis
- For XML-heavy apps: Emphasize View/ViewBinding sections, minimize Compose coverage
- For Java to Kotlin migrations: Add section comparing remaining Java code and migration opportunities
- For specific domains: Add domain-specific checks (e.g., payment processing security for fintech apps)
- For modularized apps: Add multi-module dependency analysis and modularization best practices
- Specify frameworks in use: "This app uses RxJava" or "This app uses Ktor instead of Retrofit" for targeted analysis
