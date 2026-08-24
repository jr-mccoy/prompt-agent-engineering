---
title: "Android Hilt Dependency Injection Scope Review"
category: mobile/android/targeted-reviews
description: "Android Hilt Dependency Injection Scope Review."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - hilt
  - mobile
  - reviews
  - scope
  - targeted
updated: "2026-03-19"
related_prompts: []
---

# Android Hilt Dependency Injection Scope Review

**Objective:** Conduct a targeted review of Hilt dependency injection implementation in Android applications, analyzing scope definitions, module organization, injection patterns, and potential memory leaks or misconfigurations.

**When to Use:** Use this prompt when debugging DI-related crashes, adding new dependencies to the graph, refactoring module organization, investigating memory leaks suspected to be scope-related, or during architecture audits of Hilt setup.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the actual dependency graph** - Don't flag based on pattern matching alone. Verify that the suspected scope issue actually causes problems.
2. **Check for existing scope management** - Hilt handles most lifecycle concerns automatically. Verify issues aren't already addressed by framework.
3. **Understand the context** - Consider WHY dependencies are scoped certain ways. Business requirements often dictate scope choices.
4. **Confirm actual impact** - Can this actually cause leaks, crashes, or incorrect behavior? Test with actual runtime scenarios.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `AppModule.kt:35`).

**Finding NO issues is an acceptable outcome.** If Hilt configuration follows best practices, say so with confidence. Don't manufacture DI concerns.

### False-Positive Prevention

- ❌ Do NOT flag @Singleton as problematic without verifying actual memory impact
- ❌ Do NOT flag based solely on scope annotations without understanding usage patterns
- ❌ Do NOT assume scope mismatches without tracing actual injection sites
- ❌ Do NOT report issues that Hilt's compile-time checks would already catch
- ✅ DO verify that suspected leaks actually hold references improperly
- ✅ DO understand Hilt's component hierarchy and automatic scope management
- ✅ DO check for @ViewModelScoped when reviewing ViewModel dependencies
- ✅ DO consider whether objects genuinely need different scoping

---

### 1. Scope Definition Analysis

Evaluate scope usage across the application:

* **Singleton Scope (@Singleton):**
  - Review what's marked as Singleton and whether it should be
  - Check for expensive objects that should be Singleton but aren't
  - Assess memory impact of Singleton instances
  - Verify Singleton objects are truly stateless or properly synchronized

* **Activity/Fragment Scopes:**
  - Review @ActivityScoped and @FragmentScoped usage
  - Check for scope mismatches (injecting shorter-lived scope into longer-lived)
  - Assess whether scopes match object lifecycle requirements
  - Verify proper cleanup when scope is destroyed

* **ViewModel Scope (@ViewModelScoped):**
  - Review dependencies injected into ViewModels
  - Check for appropriate ViewModelScoped bindings
  - Assess SavedStateHandle integration
  - Verify ViewModel dependencies survive configuration changes

* **Custom Scopes:**
  - Review any custom scope definitions
  - Check for proper component hierarchy
  - Assess custom scope lifecycle management
  - Verify scope boundaries are clear

### 2. Module Organization

Analyze module structure and bindings:

* **Module Categorization:**
  - Review module organization (by layer, feature, or mixed)
  - Check for single responsibility in modules
  - Assess module reusability across features
  - Verify no circular module dependencies

* **Installation Points:**
  - Review @InstallIn annotations for correctness
  - Check that bindings are installed in appropriate components
  - Assess SingletonComponent vs ActivityComponent vs ViewModelComponent usage
  - Verify bindings are available when needed

* **Binding Types:**
  - Review @Binds vs @Provides usage (prefer @Binds for interfaces)
  - Check for unnecessary @Provides when @Binds would work
  - Assess binding lifecycle (is it recomputed unnecessarily?)
  - Verify proper qualifier usage for multiple implementations

### 3. Injection Patterns

Evaluate how dependencies are injected:

* **Constructor Injection:**
  - Review @Inject constructor patterns
  - Check for proper @HiltViewModel annotation
  - Assess constructor parameter ordering (required vs optional)
  - Verify no missing @Inject annotations

* **Field Injection:**
  - Review @Inject field usage (discouraged but sometimes necessary)
  - Check for field injection in Activities/Fragments
  - Assess lateinit safety for injected fields
  - Verify no field injection in ViewModels (use constructor)

* **Assisted Injection:**
  - Review @AssistedFactory usage for runtime parameters
  - Check for proper @Assisted parameter handling
  - Assess AssistedInject with SavedStateHandle
  - Verify factory usage patterns

### 4. Scope Mismatch Detection

Identify potential scope conflicts:

* **Lifetime Mismatches:**
  - Check for Activity-scoped injected into Singleton
  - Review ViewModel-scoped dependencies of Singleton objects
  - Assess any shorter-lived scope in longer-lived container
  - Verify no references that outlive their scope

* **Context Leaks:**
  - Check for Activity/Fragment Context in Singletons
  - Review @ApplicationContext vs @ActivityContext usage
  - Assess Context storage patterns
  - Verify no Context leaks through scope hierarchy

* **Memory Retention:**
  - Check for objects retaining references beyond their scope
  - Review callback/listener retention across scopes
  - Assess closure captures in injected lambdas
  - Verify proper cleanup mechanisms

### 5. Testing Configuration

Analyze test DI setup:

* **Test Modules:**
  - Review @TestInstallIn for test replacements
  - Check for @UninstallModules usage
  - Assess test double bindings (fakes, mocks)
  - Verify test isolation

* **Test Patterns:**
  - Review HiltAndroidRule usage
  - Check for proper test component setup
  - Assess ViewModel testing patterns
  - Verify instrumentation test DI setup

### 6. Performance Considerations

Evaluate DI performance impact:

* **Initialization Cost:**
  - Review heavy objects initialized at app startup
  - Check for lazy vs eager initialization
  - Assess @Provides method complexity
  - Verify no blocking calls in bindings

* **Graph Complexity:**
  - Review dependency graph depth
  - Check for unnecessary intermediate dependencies
  - Assess module compilation impact
  - Verify incremental compilation support

### 7. Common Anti-Patterns

Check for problematic patterns:

* **Service Locator Pattern:**
  - Check for EntryPointAccessors overuse
  - Review manual DI bypassing Hilt
  - Assess static getInstance patterns alongside Hilt
  - Verify no mixed DI approaches

* **Overly Complex Graphs:**
  - Check for deep dependency chains
  - Review circular dependency workarounds
  - Assess binding complexity
  - Verify graph is understandable

---

## Expected Output

Provide a comprehensive Hilt DI review report including:

### 1. Executive Summary
- Overall DI health rating
- Scope usage assessment
- Module organization quality
- Critical issues count

### 2. Scope Inventory

| Scope | Count | Purpose | Issues |
|-------|-------|---------|--------|
| @Singleton | [#] | [Description] | [Count] |
| @ActivityScoped | [#] | [Description] | [Count] |
| @ViewModelScoped | [#] | [Description] | [Count] |

### 3. Module Analysis

| Module | InstallIn | Bindings | Type | Issues |
|--------|-----------|----------|------|--------|
| [Name] | [Component] | [Count] | [Binds/Provides] | [Count] |

### 4. Detailed Findings

For each issue:
- **Location:** Module/class
- **Issue:** Description
- **Impact:** Memory leak/crash/performance
- **Severity:** Critical/High/Medium/Low
- **Current Code:** Problematic pattern
- **Recommended Fix:** Correct implementation

### 5. Scope Hierarchy Diagram

Visual representation of scope relationships and potential conflicts.

### 6. Prioritized Recommendations

Ordered by severity and impact.

---

## Example Output

```markdown
# Hilt DI Scope Review Report

## Executive Summary
- **Overall Health:** Needs Attention
- **Scope Usage:** 3 scope mismatches found
- **Module Organization:** Good with minor improvements
- **Critical Issues:** 1 | High: 3 | Medium: 5 | Low: 4

## Critical Findings

### CRITICAL-1: Activity Context Leaked in Singleton
**Severity:** Critical
**Impact:** Memory leak, potential crash on configuration change

**Location:** NetworkModule.kt

**Current Implementation:**
```kotlin
@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {

    @Provides
    @Singleton
    fun provideNetworkMonitor(
        @ActivityContext context: Context  // CRITICAL: Activity context in Singleton!
    ): NetworkMonitor {
        return NetworkMonitorImpl(context)
    }
}
```

**Problem:**
1. NetworkMonitor is Singleton (lives forever)
2. It holds reference to Activity Context
3. Activity is destroyed on rotation
4. Old Activity cannot be garbage collected
5. Memory leak grows with each rotation

**Recommended Fix:**
```kotlin
@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {

    @Provides
    @Singleton
    fun provideNetworkMonitor(
        @ApplicationContext context: Context  // Use Application context for Singletons
    ): NetworkMonitor {
        return NetworkMonitorImpl(context)
    }
}
```

**Alternative - Scope to Activity if Activity Context is Required:**
```kotlin
@Module
@InstallIn(ActivityComponent::class)  // Change scope
object NetworkModule {

    @Provides
    @ActivityScoped  // Now properly scoped
    fun provideNetworkMonitor(
        @ActivityContext context: Context
    ): NetworkMonitor {
        return NetworkMonitorImpl(context)
    }
}
```

---

### HIGH-1: Scope Mismatch - ViewModelScoped in Singleton
**Severity:** High
**Impact:** Incorrect object sharing, potential data leakage between users

**Location:** SettingsRepository.kt

**Current Implementation:**
```kotlin
// SettingsRepository is Singleton
@Singleton
class SettingsRepository @Inject constructor(
    private val userPreferences: UserPreferences  // This is ViewModelScoped!
) {
    fun getUserSettings(): Settings {
        return userPreferences.getSettings()  // Wrong user's settings!
    }
}

// UserPreferences is ViewModelScoped
@ViewModelScoped
class UserPreferences @Inject constructor(
    private val savedStateHandle: SavedStateHandle
) {
    // ...
}
```

**Problem:**
- SettingsRepository is Singleton (one instance for app)
- UserPreferences is ViewModelScoped (one per ViewModel)
- Singleton is created once at first injection
- It captures the UserPreferences from the first ViewModel
- All subsequent ViewModels share the first user's preferences

**Recommended Fix:**
```kotlin
// Option 1: Make SettingsRepository also ViewModelScoped
@ViewModelScoped
class SettingsRepository @Inject constructor(
    private val userPreferences: UserPreferences
)

// Option 2: Use Provider for lazy/scoped access
@Singleton
class SettingsRepository @Inject constructor(
    private val userPreferencesProvider: Provider<UserPreferences>
) {
    fun getUserSettings(): Settings {
        return userPreferencesProvider.get().getSettings()
    }
}

// Option 3: Restructure to remove the scope mismatch
@Singleton
class SettingsRepository @Inject constructor(
    private val settingsDao: SettingsDao  // Use Singleton dependency instead
) {
    fun getUserSettings(userId: String): Settings {
        return settingsDao.getSettingsForUser(userId)
    }
}
```

---

### HIGH-2: Missing @Binds - Using @Provides Unnecessarily
**Severity:** High
**Impact:** Increased compile time, more generated code

**Location:** RepositoryModule.kt

**Current Implementation:**
```kotlin
@Module
@InstallIn(SingletonComponent::class)
object RepositoryModule {

    // INEFFICIENT: Using @Provides for simple interface binding
    @Provides
    @Singleton
    fun provideTodoRepository(impl: TodoRepositoryImpl): ITodoRepository {
        return impl  // Just returning the injected implementation
    }

    @Provides
    @Singleton
    fun provideNoteRepository(impl: NoteRepositoryImpl): INoteRepository {
        return impl
    }

    // ... 10 more similar bindings
}
```

**Recommended Fix:**
```kotlin
@Module
@InstallIn(SingletonComponent::class)
abstract class RepositoryModule {

    // EFFICIENT: Use @Binds for interface-to-implementation bindings
    @Binds
    @Singleton
    abstract fun bindTodoRepository(impl: TodoRepositoryImpl): ITodoRepository

    @Binds
    @Singleton
    abstract fun bindNoteRepository(impl: NoteRepositoryImpl): INoteRepository
}
```

**Benefits:**
- No method body generated (just metadata)
- Faster compile time
- Smaller generated code
- Clearer intent

---

### HIGH-3: Assisted Injection Without Factory
**Severity:** High
**Impact:** Runtime crash when attempting to inject

**Location:** ConversationChatViewModel.kt

**Current Implementation:**
```kotlin
// PROBLEM: Using @AssistedInject but no factory
@HiltViewModel  // Cannot use with @AssistedInject
class ConversationChatViewModel @AssistedInject constructor(
    private val repository: IMessageRepository,
    @Assisted private val conversationId: String  // Runtime parameter
) : ViewModel()

// Trying to inject normally - will crash!
@Composable
fun ConversationScreen(
    conversationId: String,
    viewModel: ConversationChatViewModel = hiltViewModel()  // Crash!
)
```

**Recommended Fix:**
```kotlin
// 1. Remove @HiltViewModel, use proper assisted injection
class ConversationChatViewModel @AssistedInject constructor(
    private val repository: IMessageRepository,
    @Assisted private val conversationId: String
) : ViewModel() {

    @AssistedFactory
    interface Factory {
        fun create(conversationId: String): ConversationChatViewModel
    }
}

// 2. Provide entry point for factory access
@EntryPoint
@InstallIn(ActivityComponent::class)
interface ViewModelFactoryProvider {
    fun conversationChatViewModelFactory(): ConversationChatViewModel.Factory
}

// 3. Create ViewModel with factory
@Composable
fun ConversationScreen(
    conversationId: String
) {
    val factory = EntryPointAccessors.fromActivity(
        LocalContext.current as Activity,
        ViewModelFactoryProvider::class.java
    ).conversationChatViewModelFactory()

    val viewModel: ConversationChatViewModel = viewModel {
        factory.create(conversationId)
    }
}
```

**Alternative - Use SavedStateHandle (Preferred):**
```kotlin
// Simpler approach using SavedStateHandle for navigation arguments
@HiltViewModel
class ConversationChatViewModel @Inject constructor(
    private val repository: IMessageRepository,
    savedStateHandle: SavedStateHandle
) : ViewModel() {
    private val conversationId: String = savedStateHandle["conversationId"]
        ?: throw IllegalArgumentException("conversationId required")
}

// Works with standard hiltViewModel()
@Composable
fun ConversationScreen(
    viewModel: ConversationChatViewModel = hiltViewModel()
)
```

---

### MEDIUM-1: Duplicate Bindings in Multiple Modules
**Severity:** Medium
**Impact:** Confusion, potential binding conflicts

**Location:** AppBindingsModule.kt, ServiceBindingsModule.kt

**Current Implementation:**
```kotlin
// In AppBindingsModule.kt
@Module
@InstallIn(SingletonComponent::class)
abstract class AppBindingsModule {
    @Binds
    abstract fun bindLogger(impl: AnalyticsLogger): ILogger
}

// In ServiceBindingsModule.kt - DUPLICATE!
@Module
@InstallIn(SingletonComponent::class)
abstract class ServiceBindingsModule {
    @Binds
    abstract fun bindLogger(impl: AnalyticsLogger): ILogger  // Same binding!
}
```

**Recommended Fix:**
```kotlin
// Consolidate bindings into appropriate module
@Module
@InstallIn(SingletonComponent::class)
abstract class CoreBindingsModule {
    @Binds
    abstract fun bindLogger(impl: AnalyticsLogger): ILogger
}

// Remove duplicate from ServiceBindingsModule
```

---

## Scope Inventory

| Scope | Count | Purpose | Issues |
|-------|-------|---------|--------|
| @Singleton | 24 | App-wide singletons | 2 (Context leak, scope mismatch) |
| @ActivityScoped | 3 | Activity-bound services | 0 |
| @ViewModelScoped | 8 | ViewModel dependencies | 1 (mismatch) |
| @FragmentScoped | 0 | Not used | N/A |

## Module Analysis

| Module | InstallIn | Bindings | Type | Issues |
|--------|-----------|----------|------|--------|
| AppBindingsModule | Singleton | 8 | Mixed | 1 (duplicate) |
| RepositoryModule | Singleton | 12 | @Provides ❌ | 1 (should use @Binds) |
| NetworkModule | Singleton | 5 | @Provides | 1 (Context leak) |
| ServiceBindingsModule | Singleton | 6 | @Binds | 1 (duplicate) |
| SyncModule | Singleton | 4 | Mixed | 0 |
| ViewModelEntryPoints | Activity | 2 | Entry points | 0 |

## Scope Hierarchy

```
SingletonComponent (App lifetime)
├── NetworkMonitor ❌ (holds ActivityContext)
├── SettingsRepository ❌ (holds ViewModelScoped dependency)
├── TodoRepository ✓
└── ...

ActivityComponent (Activity lifetime)
├── ActivityContext ✓
└── ...

ViewModelComponent (ViewModel lifetime)
├── UserPreferences ✓
├── SavedStateHandle ✓
└── ...
```

## Remediation Priority

### Critical (Immediate)
1. Fix Activity Context leak in NetworkModule

### High Priority (This Sprint)
1. Fix scope mismatch in SettingsRepository
2. Convert @Provides to @Binds in RepositoryModule
3. Fix Assisted Injection pattern in ConversationChatViewModel

### Medium Priority (Next Sprint)
1. Remove duplicate bindings
2. Add @Qualifier for multiple implementations
3. Document module responsibilities

### Low Priority (Backlog)
1. Reorganize modules by feature
2. Add DI graph visualization to docs
3. Add lint checks for scope mismatches
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Focused DI review
- **ST-02** (Structured Sequential Instructions) - Systematic scope analysis
- **RT-02** (Multi-Dimensional Analysis) - Scope, module, injection patterns
- **RT-05** (Evidence-Based Reasoning) - Code examples and diagrams
- **ST-03** (Output Format Templates) - Scope inventory tables
- **DS-06** (Prioritization Guidance) - Impact-based priority
- **OC-03** (Tabular Output) - Module analysis matrix

---

## Related Prompts

- `android_viewmodel_state_management_review.md` - For ViewModel DI patterns
- `android_coroutine_scope_review.md` - For scope-related coroutine issues
- `android_kotlin_best_practices.md` - General patterns
- `code_quality_code_complexity_analysis.md` - For module complexity
- `architecture_design_pattern_identification.md` - For DI patterns

---

## Customization Guide

- **For Multi-Module Apps:** Add inter-module DI review, component dependencies
- **For Feature Modules:** Focus on feature-scoped components, entry points
- **For Testing Focus:** Expand test module and mocking sections
- **For Compose Navigation:** Add navigation-scoped ViewModel DI patterns
- **For Legacy Migration:** Add comparison with Dagger, migration patterns
