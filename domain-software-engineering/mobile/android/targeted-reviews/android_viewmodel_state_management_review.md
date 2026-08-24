---
title: "Android ViewModel State Management Review"
category: mobile/android/targeted-reviews
description: "Android ViewModel State Management Review."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - management
  - mobile
  - reviews
  - state
  - targeted
updated: "2026-03-19"
related_prompts: []
---

# Android ViewModel State Management Review

**Objective:** Conduct a targeted review of ViewModel state management patterns in Android applications using Jetpack Compose, analyzing StateFlow usage, UI state modeling, side effect handling, state restoration, and lifecycle awareness.

**When to Use:** Use this prompt when reviewing ViewModels for new features, debugging state-related bugs, refactoring from LiveData to StateFlow, auditing for memory leaks, or ensuring proper handling of configuration changes and process death. Essential for apps with complex UI state requirements.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the actual state flow** - Don't flag based on pattern matching alone. Verify that the suspected state management issue actually causes bugs or poor UX.
2. **Check for existing state handling** - Search for state restoration, proper collectors, or ViewModel factory that may already address the concern.
3. **Understand the context** - Consider WHY state is modeled a specific way. UI requirements and data complexity affect state design.
4. **Confirm actual impact** - Test with configuration changes and process death before flagging.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `HomeViewModel.kt:45`).

**Finding NO issues is an acceptable outcome.** If state management is clean and correct, say so with confidence. Don't manufacture state handling concerns.

### False-Positive Prevention

- ❌ Do NOT flag LiveData usage as outdated if it works correctly for the use case
- ❌ Do NOT flag state granularity without understanding recomposition implications
- ❌ Do NOT assume missing state restoration without checking SavedStateHandle
- ❌ Do NOT report architectural preferences as bugs (e.g., single vs. multiple StateFlows)
- ✅ DO verify state collection uses lifecycle-aware patterns
- ✅ DO check for proper MutableStateFlow encapsulation
- ✅ DO test with configuration changes (rotation) and process death
- ✅ DO understand the trade-offs between different state modeling approaches

---

### 1. UI State Modeling

Analyze how UI state is structured and exposed:

* **State Class Design:**
  - Review UI state class structure (sealed class, data class, or multiple properties)
  - Check for `@Immutable` or `@Stable` annotations on state classes
  - Evaluate state granularity (single monolithic state vs. multiple state flows)
  - Assess default state values and initialization

* **State Properties:**
  - Verify all UI-relevant data is captured in state
  - Check for derived/computed state using `derivedStateOf`
  - Review loading, error, and success state representations
  - Assess nullable vs. sealed class approaches for optional data

* **State Exposure:**
  - Verify `MutableStateFlow` is private and exposed as `StateFlow`
  - Check for accidental exposure of mutable state
  - Review state flow operators applied before exposure
  - Assess whether state changes are atomic

### 2. StateFlow and Flow Usage

Evaluate reactive state patterns:

* **StateFlow Configuration:**
  - Review `MutableStateFlow` initialization and default values
  - Check `stateIn` operator usage for cold flows (scope, started, initial value)
  - Assess replay and buffer configurations
  - Verify proper use of `asStateFlow()` for immutable exposure

* **Flow Collection:**
  - Review flow collection in ViewModels (avoid collecting in init block without lifecycle awareness)
  - Check for proper scope usage (`viewModelScope`)
  - Assess cancellation handling and cleanup
  - Review `combine`, `flatMapLatest`, `distinctUntilChanged` usage

* **SharedFlow for Events:**
  - Evaluate one-time event handling (navigation, snackbars, toasts)
  - Check for `SharedFlow` vs. `Channel` for events
  - Review replay configuration for events (should typically be 0)
  - Assess event consumption guarantees

### 3. Side Effect Handling

Analyze how ViewModels handle side effects:

* **One-Time Events:**
  - Review pattern for navigation events
  - Check handling of toast/snackbar triggers
  - Assess dialog show/dismiss events
  - Verify events are not re-emitted on configuration change

* **Event Consumption:**
  - Check if events are consumed exactly once
  - Review handling of events when UI is not active
  - Assess event queuing during background
  - Verify no event loss during rapid navigation

* **Side Effect Isolation:**
  - Review separation of state changes from side effects
  - Check for mixing state updates with external calls
  - Assess transaction boundaries for complex operations
  - Verify side effects don't block state updates

### 4. Lifecycle Awareness

Evaluate ViewModel lifecycle handling:

* **Scope Management:**
  - Review `viewModelScope` usage for coroutines
  - Check for any use of `GlobalScope` (should be avoided)
  - Assess custom scope creation and cleanup
  - Verify no work continues after ViewModel cleared

* **Collection Lifecycle:**
  - Check Compose usage of `collectAsStateWithLifecycle()` vs. `collectAsState()`
  - Review lifecycle awareness of flow collection
  - Assess behavior during Activity/Fragment lifecycle changes
  - Verify no redundant resubscription patterns

* **Resource Cleanup:**
  - Review `onCleared()` implementation if present
  - Check for proper cancellation of long-running operations
  - Assess cleanup of external subscriptions (Firebase listeners, etc.)
  - Verify no references held after ViewModel cleared

### 5. Process Death and State Restoration

Analyze SavedStateHandle usage:

* **SavedStateHandle Integration:**
  - Check if critical state is persisted via SavedStateHandle
  - Review what state needs restoration vs. re-fetch
  - Assess SavedStateHandle injection pattern
  - Verify navigation arguments are properly handled

* **State Selection for Persistence:**
  - Review which state properties are saved (user input, scroll position, selected items)
  - Check that transient state is not persisted (loading states, errors)
  - Assess parcelization of complex objects
  - Verify size limits for saved state (< 1MB recommended)

* **Restoration Testing:**
  - Is process death tested as part of QA?
  - Are there automated tests for state restoration?
  - How is partial state restoration handled?

### 6. State Updates and Mutations

Review how state is modified:

* **Update Patterns:**
  - Review use of `update {}` vs. direct assignment
  - Check for thread safety of state updates
  - Assess atomicity of multi-property updates
  - Verify copy() is used for data class updates

* **Update Sources:**
  - Map all sources that can trigger state updates
  - Check for race conditions between update sources
  - Assess ordering guarantees for sequential updates
  - Review debouncing/throttling for rapid updates

* **Validation:**
  - Review input validation before state updates
  - Check for state invariant enforcement
  - Assess error state handling on invalid input
  - Verify state consistency after partial failures

### 7. ViewModel Dependencies and DI

Analyze dependency patterns:

* **Constructor Injection:**
  - Review `@HiltViewModel` and `@Inject` usage
  - Check for proper repository/use case injection
  - Assess dependency scope compatibility
  - Verify no Android Context in ViewModel (use `@ApplicationContext` if needed)

* **Assisted Injection:**
  - Review `@AssistedFactory` for runtime parameters
  - Check for navigation argument handling
  - Assess pattern for ViewModel factories
  - Verify SavedStateHandle injection

* **Dependency Usage:**
  - Check for blocking calls to injected dependencies
  - Review suspend function usage with repositories
  - Assess timeout handling for external dependencies
  - Verify error propagation from dependencies

### 8. Testing Considerations

Evaluate testability of state management:

* **State Testability:**
  - Can state transitions be tested in isolation?
  - Are there test helpers for state assertion?
  - Is state observable without Compose dependencies?

* **Mocking and Fakes:**
  - Are dependencies injectable for testing?
  - Are there fakes for complex dependencies?
  - Can events be captured for assertion?

* **Test Coverage:**
  - Are all state transitions tested?
  - Are edge cases (empty, error, loading) covered?
  - Is process death restoration tested?

---

## Expected Output

Provide a comprehensive ViewModel state management review report including:

### 1. Executive Summary
- Overall state management health rating
- Number of ViewModels reviewed
- Critical findings count by severity
- Architecture pattern assessment (MVI, MVVM, hybrid)

### 2. ViewModel Inventory

| ViewModel | State Class | StateFlow | Events | SavedState | Issues |
|-----------|-------------|-----------|--------|------------|--------|
| [Name]    | [Type]      | [Count]   | [Pattern] | [Yes/No] | [Count] |

### 3. State Modeling Assessment

For each ViewModel:
- State class design evaluation
- Immutability compliance
- State granularity assessment
- Recommendations

### 4. Detailed Findings

For each issue found:
- **Location:** ViewModel and property/method
- **Issue:** Description of the problem
- **Impact:** Effect on app behavior
- **Severity:** Critical/High/Medium/Low
- **Current Code:** Problematic pattern
- **Recommended Fix:** Corrected pattern
- **Testing:** How to verify the fix

### 5. Pattern Violations Matrix

| Pattern | Expected | Actual | ViewModels Affected |
|---------|----------|--------|---------------------|
| Private MutableStateFlow | Required | [Status] | [List] |
| StateFlow exposure | Required | [Status] | [List] |
| No GlobalScope | Required | [Status] | [List] |
| SavedStateHandle for input | Recommended | [Status] | [List] |

### 6. Prioritized Recommendations

- **Critical:** Issues causing crashes or data loss
- **High:** State bugs affecting UX
- **Medium:** Best practice violations
- **Low:** Style and optimization opportunities

---

## Example Output

```markdown
# ViewModel State Management Review Report

## Executive Summary
- **Overall Health:** Moderate - Needs attention on event handling
- **ViewModels Reviewed:** 12
- **Critical Issues:** 1 | High: 4 | Medium: 8 | Low: 5
- **Pattern:** MVVM with StateFlow, partial MVI adoption

## Critical Findings

### CRITICAL-1: MutableStateFlow Exposed Publicly
**Severity:** Critical
**Impact:** External code can modify ViewModel state, breaking unidirectional data flow

**Location:** TodoViewModel.kt

**Current Code:**
```kotlin
@HiltViewModel
class TodoViewModel @Inject constructor(
    private val repository: ITodoRepository
) : ViewModel() {

    // PROBLEM: Mutable state exposed publicly
    val uiState = MutableStateFlow(TodoUiState())

    // Anyone can do: viewModel.uiState.value = maliciousState
}
```

**Recommended Fix:**
```kotlin
@HiltViewModel
class TodoViewModel @Inject constructor(
    private val repository: ITodoRepository
) : ViewModel() {

    // CORRECT: Private mutable, public immutable
    private val _uiState = MutableStateFlow(TodoUiState())
    val uiState: StateFlow<TodoUiState> = _uiState.asStateFlow()

    fun updateTitle(title: String) {
        _uiState.update { it.copy(title = title) }
    }
}
```

---

### HIGH-1: Events Lost on Configuration Change
**Severity:** High
**Impact:** Navigation events replayed or lost during rotation

**Location:** ShoppingViewModel.kt

**Current Code:**
```kotlin
// PROBLEM: Using StateFlow for one-time events
private val _navigateToDetail = MutableStateFlow<String?>(null)
val navigateToDetail: StateFlow<String?> = _navigateToDetail.asStateFlow()

fun onItemClick(id: String) {
    _navigateToDetail.value = id  // Will replay on rotation!
}

// In Composable
LaunchedEffect(navigateToDetail) {
    navigateToDetail.collect { id ->
        id?.let { navController.navigate("detail/$it") }
        // Navigation happens again after rotation
    }
}
```

**Recommended Fix:**
```kotlin
// SOLUTION: Use Channel/SharedFlow for one-time events
private val _navigateToDetail = Channel<String>(Channel.BUFFERED)
val navigateToDetail = _navigateToDetail.receiveAsFlow()

fun onItemClick(id: String) {
    viewModelScope.launch {
        _navigateToDetail.send(id)  // Consumed once
    }
}

// In Composable - with lifecycle awareness
LaunchedEffect(Unit) {
    viewModel.navigateToDetail.collect { id ->
        navController.navigate("detail/$id")
    }
}
```

**Alternative Pattern (Preferred):**
```kotlin
// Even better: Event wrapper with consumption tracking
sealed interface TodoEvent {
    data class NavigateToDetail(val id: String) : TodoEvent
    data class ShowSnackbar(val message: String) : TodoEvent
}

private val _events = Channel<TodoEvent>(Channel.BUFFERED)
val events = _events.receiveAsFlow()
```

---

### HIGH-2: No Process Death Handling
**Severity:** High
**Impact:** User loses form input if app killed in background

**Location:** TodoEditorViewModel.kt

**Current Code:**
```kotlin
@HiltViewModel
class TodoEditorViewModel @Inject constructor(
    private val repository: ITodoRepository
) : ViewModel() {

    // User types a long description, switches to another app
    // Android kills the app for memory
    // User returns - all input is gone!
    private val _title = MutableStateFlow("")
    private val _description = MutableStateFlow("")
}
```

**Recommended Fix:**
```kotlin
@HiltViewModel
class TodoEditorViewModel @Inject constructor(
    private val repository: ITodoRepository,
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {

    // CORRECT: Persist user input to SavedStateHandle
    val title = savedStateHandle.getStateFlow("title", "")
    val description = savedStateHandle.getStateFlow("description", "")

    fun updateTitle(value: String) {
        savedStateHandle["title"] = value
    }

    fun updateDescription(value: String) {
        savedStateHandle["description"] = value
    }
}
```

---

### MEDIUM-1: Using collectAsState Instead of collectAsStateWithLifecycle
**Severity:** Medium
**Impact:** Flow collection continues during background, wasting resources

**Location:** Multiple screens

**Current Code:**
```kotlin
@Composable
fun TodoScreen(viewModel: TodoViewModel = hiltViewModel()) {
    // PROBLEM: Collects even when app is in background
    val uiState by viewModel.uiState.collectAsState()
}
```

**Recommended Fix:**
```kotlin
@Composable
fun TodoScreen(viewModel: TodoViewModel = hiltViewModel()) {
    // CORRECT: Stops collection when lifecycle is below STARTED
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
}
```

**Files Affected:**
- TodoScreen.kt
- ShoppingScreen.kt
- NotesScreen.kt
- CalendarScreen.kt
- (8 more screens)

---

## ViewModel Inventory

| ViewModel | State Class | Flows | Events | SavedState | Issues |
|-----------|-------------|-------|--------|------------|--------|
| TodoViewModel | TodoUiState | 1 | Channel | No | 2 |
| TodoEditorViewModel | Separate props | 4 | None | No | 3 |
| ShoppingViewModel | ShoppingUiState | 1 | StateFlow (wrong) | No | 2 |
| CalendarViewModel | CalendarUiState | 2 | Channel | Yes | 1 |
| ChatViewModel | ChatUiState | 1 | SharedFlow | No | 1 |
| SettingsViewModel | SettingsState | 3 | None | Yes | 0 |

## Pattern Violations Summary

| Pattern | Status | Affected |
|---------|--------|----------|
| Private MutableStateFlow | 1 violation | TodoViewModel |
| Proper event handling | 3 violations | Shopping, Notes, Profile |
| SavedStateHandle usage | 8 missing | Todo, Editor, Shopping, Chat... |
| collectAsStateWithLifecycle | 10 missing | All screens |
| No GlobalScope | Compliant | None |
| Proper onCleared | 2 missing | Chat, Sync |

## Remediation Priority

### Critical (Fix Immediately)
1. Make MutableStateFlow private in TodoViewModel

### High Priority (This Sprint)
1. Migrate event handling to Channel pattern
2. Add SavedStateHandle to form ViewModels
3. Fix Firebase listener cleanup in ChatViewModel

### Medium Priority (Next Sprint)
1. Migrate all collectAsState to collectAsStateWithLifecycle
2. Add @Immutable annotations to state classes
3. Consolidate state into sealed class UiState pattern
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Focused state management review
- **ST-02** (Structured Sequential Instructions) - Systematic review areas
- **RT-02** (Multi-Dimensional Analysis) - Multiple state aspects covered
- **RT-05** (Evidence-Based Reasoning) - Specific code examples required
- **ST-03** (Output Format Templates) - Structured report with tables
- **DS-06** (Prioritization Guidance) - Severity-based findings
- **QA-01** (Self-Verification) - Pattern violation matrix

---

## Related Prompts

- `android_compose_recomposition_review.md` - For Compose-specific state optimizations
- `android_process_death_recovery_review.md` - Deep dive on SavedStateHandle
- `android_coroutine_scope_review.md` - For coroutine lifecycle issues
- `android_hilt_di_scope_review.md` - For ViewModel dependency injection
- `android_kotlin_best_practices.md` - General Kotlin patterns

---

## Customization Guide

- **For MVI Architecture:** Add intent/action handling review, reducer pattern analysis
- **For Compose Multiplatform:** Include platform-specific state considerations
- **For Large Teams:** Add state documentation and naming convention review
- **For Legacy Migration:** Include LiveData to StateFlow migration assessment
- **For Testing Focus:** Expand testing considerations with specific test patterns
