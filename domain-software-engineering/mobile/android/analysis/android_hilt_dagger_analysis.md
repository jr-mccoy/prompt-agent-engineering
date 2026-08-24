---
title: "Android Hilt/Dagger Dependency Injection Analysis"
category: mobile-development
description: "Comprehensive analysis of Hilt and Dagger dependency injection configurations, identifying misconfigurations, scope issues, and anti-patterns"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - mobile-development
  - android
  - dependency-injection
  - hilt
  - dagger
updated: "2025-01-18"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_architecture_review.md
  - domain-software-engineering/mobile/android/targeted-reviews/android_hilt_di_scope_review.md
  - domain-software-engineering/mobile/android/implementation/android_dependency_injection.md
---


# Android Hilt/Dagger Dependency Injection Analysis

**Objective:** Analyze Android applications using Hilt or Dagger to identify dependency injection misconfigurations, scope violations, module organization issues, and common DI anti-patterns that cause runtime crashes, memory leaks, or testability problems.

**When to Use:** Use this prompt when debugging DI-related crashes, reviewing Hilt/Dagger setup during code reviews, planning migrations from Dagger to Hilt, or auditing DI architecture for testability and maintainability issues.

**Instructions:**

### CRITICAL: Verification Requirements

**Before flagging ANY DI issue, you MUST:**

1. **Trace the actual dependency graph** - Don't flag based on annotation presence alone. Verify the component hierarchy and binding resolution path.
2. **Check for intentional scoping decisions** - Search for evidence of deliberate scope choices (comments, architecture docs, or specific use case requirements).
3. **Understand the full context** - Consider module boundaries, feature modules, and multi-module project structures.
4. **Confirm actual runtime impact** - Will the issue cause a build failure, runtime crash, memory leak, or is it merely suboptimal?
5. **Provide specific file:line locations** - Every finding MUST include exact code locations with line numbers and the affected binding/injection site.

**Finding a well-configured DI setup is an acceptable outcome.** If the dependency injection is properly configured, say so with confidence. Don't manufacture violations to fill a report.

### False-Positive Prevention

- ❌ Do NOT flag missing `@Inject` without verifying the class actually needs injection
- ❌ Do NOT recommend Hilt migration if Dagger is intentionally used for specific requirements
- ❌ Do NOT flag custom scopes as wrong without understanding their purpose
- ❌ Do NOT assume circular dependencies without tracing the full dependency graph
- ❌ Do NOT flag assisted injection as an anti-pattern when runtime parameters are genuinely required
- ✅ DO trace complete injection chains before flagging scope mismatches
- ✅ DO consider multi-module DI configurations
- ✅ DO understand that some patterns (like providing Context) have legitimate variations
- ✅ DO acknowledge when DI setup follows best practices

---

## Analysis Categories

### 1. Hilt Setup and Configuration

**Check for:**
- `@HiltAndroidApp` on Application class
- `@AndroidEntryPoint` on Activities, Fragments, Services, BroadcastReceivers, Views
- `@HiltViewModel` on ViewModels with proper `@Inject constructor`
- Gradle plugin configuration (`id 'dagger.hilt.android.plugin'`)
- Correct dependency versions and compatibility
- KSP vs KAPT configuration (prefer KSP for better performance)

**Common Issues:**
```kotlin
// ❌ Missing @AndroidEntryPoint - will crash at runtime
class MainActivity : AppCompatActivity() {
    @Inject lateinit var repository: UserRepository  // Won't be injected!
}

// ✅ Correct setup
@AndroidEntryPoint
class MainActivity : AppCompatActivity() {
    @Inject lateinit var repository: UserRepository
}
```

### 2. Dagger Component Hierarchy (Dagger-only projects)

**Check for:**
- Proper `@Component` and `@Subcomponent` relationships
- Component dependencies vs subcomponents (understand tradeoffs)
- Builder/Factory patterns for component creation
- Component provision methods match injection sites

**Common Issues:**
```kotlin
// ❌ Missing provision method - injection will fail
@Component(modules = [AppModule::class])
interface AppComponent {
    // Missing: fun inject(activity: MainActivity)
}

// ❌ Incorrect component dependency - scope violation
@Component(dependencies = [AppComponent::class])
@ActivityScope
interface ActivityComponent {
    // Parent's @Singleton bindings won't be visible without explicit exposure
}
```

### 3. Module Organization and Bindings

**Check for:**
- `@Module` classes with `@InstallIn` (Hilt) or included in component modules (Dagger)
- Proper use of `@Binds` vs `@Provides` (prefer `@Binds` for interface bindings)
- Static `@Provides` methods where possible (better performance)
- Module categorization (network, database, repository, etc.)
- Avoid placing unrelated bindings in the same module

**Common Issues:**
```kotlin
// ❌ Using @Provides when @Binds would work
@Module
@InstallIn(SingletonComponent::class)
class RepositoryModule {
    @Provides
    fun provideUserRepository(impl: UserRepositoryImpl): UserRepository = impl
}

// ✅ Use @Binds for interface-to-implementation bindings
@Module
@InstallIn(SingletonComponent::class)
abstract class RepositoryModule {
    @Binds
    abstract fun bindUserRepository(impl: UserRepositoryImpl): UserRepository
}

// ❌ Non-static @Provides (creates module instance)
@Module
@InstallIn(SingletonComponent::class)
class NetworkModule {
    @Provides
    fun provideOkHttpClient(): OkHttpClient = OkHttpClient.Builder().build()
}

// ✅ Static @Provides (better performance)
@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {
    @Provides
    fun provideOkHttpClient(): OkHttpClient = OkHttpClient.Builder().build()
}
```

### 4. Scope Violations and Mismatches

**Check for:**
- Scope annotations match component hierarchy (`@Singleton`, `@ActivityScoped`, `@ViewModelScoped`, etc.)
- Unscoped dependencies that should be scoped (creating multiple instances unexpectedly)
- Scoped dependencies injected into wrong-scoped components
- Memory leaks from over-scoping (e.g., `@Singleton` holding Activity reference)

**Common Issues:**
```kotlin
// ❌ Scope mismatch - ActivityScoped injected into Singleton
@Singleton
class UserManager @Inject constructor(
    private val activityContext: ActivityContext  // Will fail!
)

// ❌ Unscoped when it should be scoped - creates new instance every injection
class ExpensiveService @Inject constructor() {  // Missing @Singleton
    init { /* expensive initialization */ }
}

// ❌ Over-scoped - potential memory leak
@Singleton
class NavigationHelper @Inject constructor(
    private val activity: Activity  // Leaks Activity!
)

// ✅ Correct scoping
@ActivityScoped
class NavigationHelper @Inject constructor(
    private val activity: Activity
)
```

### 5. Qualifier and Named Bindings

**Check for:**
- Proper use of `@Named` or custom qualifiers for multiple bindings of same type
- Missing qualifiers causing ambiguous bindings
- Inconsistent qualifier usage between provision and injection sites
- Consider custom qualifier annotations over string-based `@Named`

**Common Issues:**
```kotlin
// ❌ Ambiguous binding - two OkHttpClient without qualifiers
@Provides fun provideAuthClient(): OkHttpClient = ...
@Provides fun provideApiClient(): OkHttpClient = ...  // Duplicate binding error!

// ✅ Use qualifiers
@Qualifier
@Retention(AnnotationRetention.BINARY)
annotation class AuthClient

@Qualifier
@Retention(AnnotationRetention.BINARY)
annotation class ApiClient

@Provides @AuthClient fun provideAuthClient(): OkHttpClient = ...
@Provides @ApiClient fun provideApiClient(): OkHttpClient = ...

// ❌ Qualifier mismatch
@Inject constructor(@Named("auth") client: OkHttpClient)  // But provided with @Named("AUTH")
```

### 6. Constructor Injection vs Field Injection

**Check for:**
- Prefer constructor injection over field injection (`@Inject lateinit var`)
- Field injection only used where constructor injection isn't possible (Activities, Fragments)
- No `@Inject` on private fields (will fail)
- Lazy injection and Provider injection used appropriately

**Common Issues:**
```kotlin
// ❌ Field injection when constructor injection is possible
class UserRepository {
    @Inject lateinit var apiService: ApiService
    @Inject lateinit var database: AppDatabase
}

// ✅ Constructor injection
class UserRepository @Inject constructor(
    private val apiService: ApiService,
    private val database: AppDatabase
)

// ❌ Private field injection - won't work
@AndroidEntryPoint
class MainActivity : AppCompatActivity() {
    @Inject private lateinit var viewModel: MainViewModel  // Will fail!
}
```

### 7. Assisted Injection (Hilt)

**Check for:**
- `@AssistedInject` constructor with `@Assisted` parameters for runtime values
- `@AssistedFactory` interface defined
- Factory injected and used to create instances
- Not overusing assisted injection when ViewModel SavedStateHandle would work

**Common Issues:**
```kotlin
// ❌ Runtime parameter in regular @Inject - won't work
class DetailViewModel @Inject constructor(
    private val itemId: String,  // Can't inject runtime value!
    private val repository: ItemRepository
)

// ✅ Assisted injection for runtime parameters
class DetailViewModel @AssistedInject constructor(
    @Assisted private val itemId: String,
    private val repository: ItemRepository
) : ViewModel() {

    @AssistedFactory
    interface Factory {
        fun create(itemId: String): DetailViewModel
    }
}

// Usage with Hilt ViewModel
@HiltViewModel
class DetailViewModel @Inject constructor(
    savedStateHandle: SavedStateHandle,  // Use for navigation args
    private val repository: ItemRepository
) : ViewModel() {
    private val itemId: String = savedStateHandle.get<String>("itemId")!!
}
```

### 8. Entry Points and Custom Components

**Check for:**
- `@EntryPoint` interfaces for injecting into classes Hilt doesn't support
- Proper `EntryPointAccessors` usage
- Custom components defined correctly when needed
- Worker injection with `@HiltWorker`

**Common Issues:**
```kotlin
// ❌ Direct component access in ContentProvider
class MyContentProvider : ContentProvider() {
    override fun onCreate(): Boolean {
        val component = (context?.applicationContext as MyApp).appComponent
        component.inject(this)  // Wrong pattern for Hilt
        return true
    }
}

// ✅ EntryPoint for ContentProvider
@EntryPoint
@InstallIn(SingletonComponent::class)
interface MyContentProviderEntryPoint {
    fun userRepository(): UserRepository
}

class MyContentProvider : ContentProvider() {
    override fun onCreate(): Boolean {
        val entryPoint = EntryPointAccessors.fromApplication(
            context!!.applicationContext,
            MyContentProviderEntryPoint::class.java
        )
        val repository = entryPoint.userRepository()
        return true
    }
}
```

### 9. Testing Configuration

**Check for:**
- `@HiltAndroidTest` on test classes
- `HiltAndroidRule` for test setup
- `@UninstallModules` for replacing production modules
- `@BindValue` for simple test replacements
- Test modules with `@TestInstallIn`
- Fake vs Mock considerations for DI testing

**Common Issues:**
```kotlin
// ❌ Missing Hilt test setup
class UserRepositoryTest {
    @Inject lateinit var repository: UserRepository  // Won't be injected!

    @Test
    fun testUser() { ... }
}

// ✅ Proper Hilt test setup
@HiltAndroidTest
@RunWith(AndroidJUnit4::class)
class UserRepositoryTest {

    @get:Rule
    var hiltRule = HiltAndroidRule(this)

    @Inject lateinit var repository: UserRepository

    @Before
    fun setup() {
        hiltRule.inject()
    }

    @Test
    fun testUser() { ... }
}

// ❌ Not replacing modules in tests
// Production network calls in unit tests!

// ✅ Replace modules for testing
@Module
@TestInstallIn(
    components = [SingletonComponent::class],
    replaces = [NetworkModule::class]
)
object FakeNetworkModule {
    @Provides
    fun provideFakeApiService(): ApiService = FakeApiService()
}
```

### 10. Multi-Module Project Configuration

**Check for:**
- Each feature module has its own `@InstallIn` modules
- Proper component dependencies across modules
- Interface bindings in API modules, implementations in impl modules
- No circular module dependencies
- Aggregating modules at app level

**Common Issues:**
```kotlin
// ❌ Feature module depending on app module
// feature/build.gradle
implementation(project(":app"))  // Circular dependency risk!

// ✅ Feature module depends on core/API modules
// feature/build.gradle
implementation(project(":core:common"))
implementation(project(":core:network-api"))

// ❌ Implementation exposed in API module
// core/network-api/NetworkModule.kt
@Provides
fun provideRetrofit(): Retrofit = Retrofit.Builder()...  // Implementation in API!

// ✅ Interface in API, implementation bound in impl module
// core/network-api/
interface ApiService { ... }

// core/network-impl/NetworkModule.kt
@Module
@InstallIn(SingletonComponent::class)
abstract class NetworkModule {
    @Binds
    abstract fun bindApiService(impl: ApiServiceImpl): ApiService
}
```

### 11. Circular Dependency Detection

**Check for:**
- Direct circular dependencies (A → B → A)
- Indirect circular dependencies (A → B → C → A)
- Lazy/Provider injection used to break cycles (but understand why cycle exists)
- Consider architectural refactoring instead of just breaking cycles with Lazy

**Common Issues:**
```kotlin
// ❌ Circular dependency
class ServiceA @Inject constructor(private val serviceB: ServiceB)
class ServiceB @Inject constructor(private val serviceA: ServiceA)  // Cycle!

// ⚠️ Breaking with Lazy (works but hides design issue)
class ServiceA @Inject constructor(private val serviceB: Lazy<ServiceB>)
class ServiceB @Inject constructor(private val serviceA: ServiceA)

// ✅ Better: Refactor to remove cycle
class ServiceA @Inject constructor(private val sharedService: SharedService)
class ServiceB @Inject constructor(private val sharedService: SharedService)
class SharedService @Inject constructor()  // Extract shared logic
```

### 12. Common Runtime Crash Patterns

**Check for:**
- Missing `@Inject` constructor on classes that need injection
- Missing `@AndroidEntryPoint` on Activities/Fragments using injection
- Injecting before `super.onCreate()` in Android components
- Accessing injected fields before injection completes
- Obfuscation issues with DI (ProGuard/R8 rules)

**Common Issues:**
```kotlin
// ❌ Accessing injected field too early
@AndroidEntryPoint
class MainActivity : AppCompatActivity() {
    @Inject lateinit var analytics: Analytics

    // CRASH: accessed before injection
    private val tracker = analytics.getTracker()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // analytics is now available
    }
}

// ✅ Access after injection
@AndroidEntryPoint
class MainActivity : AppCompatActivity() {
    @Inject lateinit var analytics: Analytics

    private lateinit var tracker: Tracker

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        tracker = analytics.getTracker()  // Safe: after super.onCreate()
    }
}
```

---

**Expected Output:** A comprehensive Hilt/Dagger analysis report including:

## 1. Executive Summary
- **DI Framework:** Hilt / Dagger / Mixed
- **Configuration Health:** Excellent / Good / Moderate / Critical Issues
- **Component Hierarchy Overview:** Visual or textual representation
- **Critical Issues Count:** By severity (Critical/High/Medium/Low)

## 2. Configuration Assessment
```
Framework: Hilt 2.x with KSP
Application Entry: ✅ @HiltAndroidApp present
Android Components: ✅ 12 Activities, 8 Fragments properly annotated
ViewModels: ⚠️ 2 of 15 missing @HiltViewModel
Modules: 8 modules across 3 feature modules
```

## 3. Detailed Findings

For each issue found:
```
**Issue:** [Descriptive title]
**Severity:** Critical | High | Medium | Low
**Location:** `path/to/File.kt:123`
**Category:** [Scope/Module/Binding/Configuration/etc.]

**Problem:**
[Explanation of what's wrong and why it matters]

**Current Code:**
```kotlin
// problematic code
```

**Recommended Fix:**
```kotlin
// corrected code
```

**Impact:** [Runtime crash / Memory leak / Build failure / Performance / Testability]
```

## 4. Dependency Graph Analysis
- Component hierarchy visualization
- Scope distribution (how many bindings per scope)
- Cross-module dependency map
- Potential circular dependency warnings

## 5. Prioritized Action Items

### Critical (Fix Immediately)
- Runtime crash risks
- Build failures
- Security issues (exposed dependencies)

### High Priority
- Memory leaks from scope violations
- Missing test configurations
- Circular dependencies

### Medium Priority
- Performance improvements (`@Binds` vs `@Provides`)
- Module organization improvements
- Qualifier consistency

### Low Priority
- Code style improvements
- Documentation for complex bindings
- Migration opportunities (Dagger to Hilt)

## 6. Best Practices Checklist
```
[✅] @HiltAndroidApp on Application
[✅] All Activities/Fragments have @AndroidEntryPoint
[⚠️] Some ViewModels missing @HiltViewModel
[✅] Using @Binds for interface bindings
[❌] Some modules using class instead of object
[✅] Proper scoping on repository layer
[⚠️] Test modules not configured
```

---

**Techniques Used:**
- ST-01 (Clear Objective)
- ST-02 (Sequential Instructions)
- RT-02 (Multi-Dimensional Analysis)
- RT-05 (Evidence-Based Reasoning)
- ST-03 (Structured Output Templates)
- OC-05 (Severity Classification)
- DT-02 (Specific Focus Areas)

**Related Prompts:**
- `android_kotlin_best_practices.md` - Broader Android best practices including DI section
- `android_kotlin_refactoring.md` - For refactoring DI-related code
- `mobile_app_security_review.md` - For security implications of DI configuration
- `code-analysis/architecture/architecture_dependency_analysis.md` - For deeper dependency analysis

**Customization Guide:**
- For **Hilt-only projects:** Skip Dagger component hierarchy section, focus on Hilt-specific annotations
- For **Dagger-only projects:** Skip Hilt setup section, focus on manual component management
- For **Migration projects:** Add section comparing current Dagger setup with Hilt equivalents
- For **Multi-module projects:** Expand section 10 with specific module dependency analysis
- For **Testing focus:** Expand section 9 with integration test configuration and test doubles strategy
- Specify Hilt/Dagger version: "This project uses Hilt 2.48 with KSP" for version-specific guidance
