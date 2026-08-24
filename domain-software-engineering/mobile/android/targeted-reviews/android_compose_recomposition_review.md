---
title: "Android Jetpack Compose Recomposition Review"
category: mobile/android/targeted-reviews
description: "Android Jetpack Compose Recomposition Review."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - compose
  - mobile
  - recomposition
  - review
  - reviews
updated: "2026-03-19"
related_prompts: []
---

# Android Jetpack Compose Recomposition Review

**Objective:** Conduct a targeted performance review of Jetpack Compose UI implementation, analyzing recomposition efficiency, state management patterns, remember usage, stability annotations, and rendering performance optimizations.

**When to Use:** Use this prompt when screens feel sluggish, after profiling shows excessive recompositions, before releasing performance-critical UI, when migrating from XML to Compose, or during code review of new Compose features. Essential for apps with complex dynamic UIs, large lists, or real-time updates.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the actual recomposition path** - Don't flag based on pattern matching alone. Verify that the suspected issue actually causes unnecessary recompositions.
2. **Check for existing optimizations** - Search for `remember`, `derivedStateOf`, `@Stable`, `@Immutable` annotations that may already address the concern.
3. **Understand the context** - Consider WHY the code is written this way. Some recompositions are intentional and necessary for correct behavior.
4. **Confirm actual performance impact** - Use Layout Inspector or composition tracing to verify the issue causes measurable performance problems.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `HomeScreen.kt:45`).

**Finding NO issues is an acceptable outcome.** If the Compose implementation is well-optimized, say so with confidence. Don't manufacture performance issues.

### False-Positive Prevention

- ❌ Do NOT flag intentional recompositions as problems (e.g., UI responding to state changes)
- ❌ Do NOT flag based solely on patterns (e.g., seeing a lambda without checking if it's remembered)
- ❌ Do NOT assume instability without checking Compose compiler reports or actual recomposition counts
- ❌ Do NOT report micro-optimizations that have negligible real-world impact
- ✅ DO verify recomposition counts using Layout Inspector or `RecompositionHighlighter`
- ✅ DO understand Compose's skip optimization and when it applies
- ✅ DO check if reported instability actually affects the specific composable
- ✅ DO consider the update frequency - occasional recomposition is fine

---

### 1. Recomposition Frequency Analysis

Identify unnecessary recompositions:

* **Recomposition Triggers:**
  - Review state changes that trigger recompositions
  - Check for state reads in parent composables that force child recomposition
  - Assess lambda stability in event handlers
  - Identify mutable objects causing recomposition

* **Recomposition Scope:**
  - Analyze composable function boundaries
  - Check for too-large composables (entire screen in one function)
  - Assess recomposition scope of each state read
  - Verify proper composable extraction for isolation

* **Profiling:**
  - Review Layout Inspector recomposition counts
  - Check for composables with high recomposition numbers
  - Assess recomposition patterns during user interaction
  - Identify "hot" composables that recompose too often

### 2. State Management Efficiency

Evaluate state handling patterns:

* **State Hoisting:**
  - Review proper state hoisting to appropriate level
  - Check for state stored too high (unnecessary recompositions)
  - Assess state stored too low (duplication, sync issues)
  - Verify single source of truth for each piece of state

* **State Type Selection:**
  - Review mutableStateOf vs. mutableStateListOf vs. mutableStateMapOf
  - Check for proper use of derivedStateOf for computed values
  - Assess snapshotFlow usage for side effects
  - Verify produceState for async state loading

* **State Updates:**
  - Check for atomic state updates
  - Assess state update frequency (debouncing needed?)
  - Review batch updates vs. individual updates
  - Verify state updates happen on correct thread

### 3. Remember and Caching

Analyze caching patterns:

* **Remember Usage:**
  - Review remember {} for expensive calculations
  - Check for missing remember on object creation
  - Assess key parameter usage for cache invalidation
  - Verify rememberSaveable for process death

* **Remember Key Selection:**
  - Check for appropriate key parameters
  - Assess false cache invalidation from unstable keys
  - Review key stability (String, Int vs. objects)
  - Verify cache size doesn't grow unbounded

* **Derived State:**
  - Review derivedStateOf usage for expensive derivations
  - Check for computations that should be derived
  - Assess derivation efficiency (O(n) computations?)
  - Verify no side effects in derivation

### 4. Lambda Stability

Evaluate callback patterns:

* **Lambda Capturing:**
  - Check for lambdas capturing ViewModel or mutable state
  - Review remember { } wrapping for unstable lambdas
  - Assess method reference usage where appropriate
  - Verify lambda parameter stability

* **Event Handler Patterns:**
  - Review onClick, onValueChange handler stability
  - Check for inline lambda recreation on each composition
  - Assess callback interface patterns
  - Verify trailing lambda stability

* **Composable Lambda Stability:**
  - Check for composable lambdas in parameters
  - Review movableContentOf for complex composable content
  - Assess slot API stability
  - Verify content lambda caching

### 5. List Performance

Analyze LazyColumn/LazyRow efficiency:

* **Item Keys:**
  - Review key parameter usage in items {}
  - Check for stable, unique keys for each item
  - Assess key stability during list updates
  - Verify no key collisions

* **Item Composables:**
  - Review individual item composable efficiency
  - Check for expensive operations in item scope
  - Assess item state reading patterns
  - Verify proper item recomposition scope

* **Content Types:**
  - Review contentType parameter for heterogeneous lists
  - Check for proper type grouping
  - Assess RecyclerView-style view holder reuse
  - Verify minimal item composable complexity

* **Prefetching and Scrolling:**
  - Review LazyListState usage
  - Check for prefetch strategies
  - Assess scroll performance metrics
  - Verify smooth 60fps scrolling

### 6. Stability Annotations

Evaluate class stability:

* **@Immutable Annotation:**
  - Review data classes for @Immutable applicability
  - Check for mutable properties preventing stability
  - Assess nested object stability
  - Verify collections are immutable (kotlinx.collections.immutable)

* **@Stable Annotation:**
  - Review classes with stable public API
  - Check for observable properties using @Stable
  - Assess stability contract adherence
  - Verify proper equality implementation

* **Stability Report:**
  - Review Compose compiler stability reports
  - Check for unexpectedly unstable classes
  - Assess impact of external library types
  - Verify stability improvements over time

### 7. Side Effects

Analyze effect handlers:

* **LaunchedEffect:**
  - Review key parameter selection
  - Check for unnecessary effect restarts
  - Assess coroutine scope and cancellation
  - Verify no blocking operations

* **DisposableEffect:**
  - Review cleanup implementation
  - Check for resource leaks
  - Assess lifecycle awareness
  - Verify proper subscription cleanup

* **SideEffect:**
  - Review for non-composable side effects only
  - Check for composition-scoped operations
  - Assess logging and analytics usage
  - Verify no state modifications

* **rememberCoroutineScope:**
  - Review scope usage patterns
  - Check for launches outside composition
  - Assess scope cancellation on disposal
  - Verify no leaked coroutines

### 8. Layout Performance

Evaluate layout efficiency:

* **Layout Phases:**
  - Review Modifier ordering for layout efficiency
  - Check for unnecessary layout passes
  - Assess SubcomposeLayout usage and cost
  - Verify intrinsic measurement minimization

* **Custom Layouts:**
  - Review Layout composable implementations
  - Check for efficient measure/place operations
  - Assess Modifier.layout usage
  - Verify no unnecessary state in layout

* **Constraint Layout:**
  - Review ConstraintLayout usage and alternatives
  - Check for simpler layout solutions
  - Assess constraint solving overhead
  - Verify proper constraint definitions

### 9. Image Loading

Analyze image efficiency:

* **Image Libraries:**
  - Review Coil/Glide/Picasso Compose integration
  - Check for proper painter caching
  - Assess placeholder and error handling
  - Verify memory-efficient loading

* **Image Sizing:**
  - Review contentScale usage
  - Check for proper size constraints
  - Assess bitmap memory consumption
  - Verify no oversized image loading

---

## Expected Output

Provide a comprehensive Compose recomposition review report including:

### 1. Executive Summary
- Overall performance health rating
- Screens reviewed
- Critical issues count
- Recomposition efficiency score

### 2. Recomposition Hotspots

| Composable | Recomp/Frame | Cause | Impact | Priority |
|------------|--------------|-------|--------|----------|
| [Name] | [Count] | [Reason] | [Effect] | [Level] |

### 3. Stability Analysis

| Class | Stable | Reason | Recommendation |
|-------|--------|--------|----------------|
| [UiState] | [Yes/No] | [Why] | [Action] |

### 4. Detailed Findings

For each issue:
- **Location:** Composable function
- **Issue:** Description of the problem
- **Impact:** Performance effect
- **Severity:** Critical/High/Medium/Low
- **Current Code:** Problematic pattern
- **Optimized Code:** Improved version
- **Verification:** How to confirm fix

### 5. Performance Metrics

| Screen | Composition | Recomposition | Frame | Status |
|--------|-------------|---------------|-------|--------|
| [Screen] | [ms] | [count] | [ms] | [OK/Slow] |

### 6. Prioritized Recommendations

Ordered by performance impact.

---

## Example Output

```markdown
# Compose Recomposition Performance Review

## Executive Summary
- **Overall Health:** Needs Optimization
- **Screens Reviewed:** 5
- **Critical Issues:** 2 | High: 4 | Medium: 8 | Low: 6
- **Recomposition Efficiency:** 65% (target: 90%+)

## Critical Findings

### CRITICAL-1: Entire Screen Recomposes on Timer Tick
**Severity:** Critical
**Impact:** 60 recompositions/second, severe jank

**Location:** HomeScreen.kt

**Current Implementation:**
```kotlin
@Composable
fun HomeScreen(viewModel: HomeViewModel = hiltViewModel()) {
    // PROBLEM: currentTime causes entire screen to recompose every second
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    Column {
        // All of these recompose every second!
        HeaderSection(uiState.userName)
        TodoListSection(uiState.todos)  // Expensive list!
        WeatherWidget(uiState.weather)
        CurrentTimeDisplay(uiState.currentTime)  // Updates every second
    }
}

// In ViewModel
data class HomeUiState(
    val userName: String = "",
    val todos: List<Todo> = emptyList(),
    val weather: Weather? = null,
    val currentTime: Long = System.currentTimeMillis()  // Updates constantly
)
```

**Problem Analysis:**
1. currentTime updates every second
2. Entire UiState is replaced
3. Every child composable receives "new" data
4. All children recompose (even though their data unchanged)

**Recommended Fix:**
```kotlin
@Composable
fun HomeScreen(viewModel: HomeViewModel = hiltViewModel()) {
    // SOLUTION 1: Separate StateFlows for different update frequencies
    val contentState by viewModel.contentState.collectAsStateWithLifecycle()
    val currentTime by viewModel.currentTime.collectAsStateWithLifecycle()

    Column {
        // These only recompose when their data changes
        HeaderSection(contentState.userName)
        TodoListSection(contentState.todos)
        WeatherWidget(contentState.weather)

        // Only this recomposes every second
        CurrentTimeDisplay(currentTime)
    }
}

// In ViewModel - separate flows by update frequency
@HiltViewModel
class HomeViewModel : ViewModel() {
    // Slow-changing content
    private val _contentState = MutableStateFlow(ContentState())
    val contentState: StateFlow<ContentState> = _contentState.asStateFlow()

    // Fast-changing time
    val currentTime: StateFlow<Long> = flow {
        while (true) {
            emit(System.currentTimeMillis())
            delay(1000)
        }
    }.stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), 0L)
}

// SOLUTION 2: Use derivedStateOf for computed values
@Composable
fun CurrentTimeDisplay(timeMillis: Long) {
    // Only recomposes when formatted string changes
    val formattedTime by remember(timeMillis) {
        derivedStateOf {
            SimpleDateFormat("HH:mm", Locale.getDefault()).format(Date(timeMillis))
        }
    }
    Text(text = formattedTime)
}
```

**Expected Improvement:** 60 recompositions/sec → 1 recomposition/sec for time display only

---

### CRITICAL-2: Unstable Lambda in LazyColumn Items
**Severity:** Critical
**Impact:** Every item recomposes on any list change

**Location:** TodoListSection.kt

**Current Implementation:**
```kotlin
@Composable
fun TodoListSection(
    todos: List<Todo>,
    viewModel: TodoViewModel = hiltViewModel()  // PROBLEM!
) {
    LazyColumn {
        items(
            items = todos,
            key = { it.id }
        ) { todo ->
            TodoItem(
                todo = todo,
                // PROBLEM: Lambda captures viewModel, unstable on every composition
                onComplete = { viewModel.completeTodo(todo.id) },
                onDelete = { viewModel.deleteTodo(todo.id) }
            )
        }
    }
}
```

**Problem Analysis:**
1. viewModel is injected inside the composable
2. Lambdas capture viewModel reference
3. Each recomposition creates new lambda instances
4. Even with stable Todo, TodoItem recomposes due to unstable lambdas

**Recommended Fix:**
```kotlin
@Composable
fun TodoListSection(
    todos: List<Todo>,
    onComplete: (String) -> Unit,  // Hoist callbacks to parent
    onDelete: (String) -> Unit
) {
    LazyColumn {
        items(
            items = todos,
            key = { it.id }
        ) { todo ->
            // Use remember to stabilize lambdas per item
            val onCompleteCallback = remember(todo.id) { { onComplete(todo.id) } }
            val onDeleteCallback = remember(todo.id) { { onDelete(todo.id) } }

            TodoItem(
                todo = todo,
                onComplete = onCompleteCallback,
                onDelete = onDeleteCallback
            )
        }
    }
}

// Parent screen provides stable callbacks
@Composable
fun HomeScreen(viewModel: HomeViewModel = hiltViewModel()) {
    val onComplete = remember<(String) -> Unit> { { id -> viewModel.completeTodo(id) } }
    val onDelete = remember<(String) -> Unit> { { id -> viewModel.deleteTodo(id) } }

    TodoListSection(
        todos = uiState.todos,
        onComplete = onComplete,
        onDelete = onDelete
    )
}
```

**Alternative - Function References:**
```kotlin
// If ViewModel methods don't capture, use method references
@Composable
fun HomeScreen(viewModel: HomeViewModel = hiltViewModel()) {
    TodoListSection(
        todos = uiState.todos,
        onComplete = viewModel::completeTodo,  // Stable reference
        onDelete = viewModel::deleteTodo
    )
}
```

---

### HIGH-1: Missing @Immutable on UI State Class
**Severity:** High
**Impact:** State class treated as unstable, excessive recomposition

**Location:** TodoUiState.kt

**Current Implementation:**
```kotlin
// PROBLEM: List<Todo> is mutable interface, class considered unstable
data class TodoUiState(
    val isLoading: Boolean = false,
    val todos: List<Todo> = emptyList(),  // Mutable List interface!
    val error: String? = null
)

data class Todo(
    val id: String,
    val title: String,
    val isComplete: Boolean,
    val tags: List<String> = emptyList()  // Also mutable!
)
```

**Compose Stability Report:**
```
unstable class TodoUiState {
  stable val isLoading: Boolean
  unstable val todos: List<Todo>  // <- Problem
  stable val error: String?
}
```

**Recommended Fix:**
```kotlin
import kotlinx.collections.immutable.ImmutableList
import kotlinx.collections.immutable.persistentListOf

@Immutable
data class TodoUiState(
    val isLoading: Boolean = false,
    val todos: ImmutableList<Todo> = persistentListOf(),
    val error: String? = null
)

@Immutable
data class Todo(
    val id: String,
    val title: String,
    val isComplete: Boolean,
    val tags: ImmutableList<String> = persistentListOf()
)

// In ViewModel, convert to immutable
_uiState.update { state ->
    state.copy(todos = newTodos.toImmutableList())
}
```

**Gradle Dependency:**
```kotlin
implementation("org.jetbrains.kotlinx:kotlinx-collections-immutable:0.3.7")
```

---

### HIGH-2: LazyColumn Missing contentType
**Severity:** High
**Impact:** Suboptimal composition reuse for mixed lists

**Location:** ShoppingListScreen.kt

**Current Implementation:**
```kotlin
@Composable
fun ShoppingList(items: List<ShoppingItem>) {
    LazyColumn {
        items(items, key = { it.id }) { item ->
            // PROBLEM: Different item types use same composition slot
            when (item.type) {
                ItemType.HEADER -> CategoryHeader(item.name)
                ItemType.PRODUCT -> ProductRow(item)
                ItemType.DIVIDER -> Divider()
            }
        }
    }
}
```

**Recommended Fix:**
```kotlin
@Composable
fun ShoppingList(items: List<ShoppingItem>) {
    LazyColumn {
        items(
            items = items,
            key = { it.id },
            contentType = { it.type }  // Enable proper recycling
        ) { item ->
            when (item.type) {
                ItemType.HEADER -> CategoryHeader(item.name)
                ItemType.PRODUCT -> ProductRow(item)
                ItemType.DIVIDER -> Divider()
            }
        }
    }
}
```

---

### MEDIUM-1: Missing remember for Expensive Calculation
**Severity:** Medium
**Impact:** Repeated calculation on each recomposition

**Location:** CalendarScreen.kt

**Current Implementation:**
```kotlin
@Composable
fun MonthView(events: List<CalendarEvent>, month: YearMonth) {
    // PROBLEM: Expensive grouping recalculated on every recomposition
    val eventsByDay = events.groupBy { it.date }  // O(n) operation!

    val days = (1..month.lengthOfMonth()).map { day ->
        val date = month.atDay(day)
        DayCell(
            date = date,
            events = eventsByDay[date] ?: emptyList()
        )
    }

    // Grid layout...
}
```

**Recommended Fix:**
```kotlin
@Composable
fun MonthView(events: List<CalendarEvent>, month: YearMonth) {
    // CORRECT: Remember expensive calculation with proper keys
    val eventsByDay = remember(events) {
        events.groupBy { it.date }
    }

    // Even better: Move to ViewModel as derived state
    val days = remember(month, eventsByDay) {
        (1..month.lengthOfMonth()).map { day ->
            val date = month.atDay(day)
            DayData(date, eventsByDay[date] ?: emptyList())
        }
    }

    LazyVerticalGrid(columns = GridCells.Fixed(7)) {
        items(days, key = { it.date }) { dayData ->
            DayCell(dayData)
        }
    }
}
```

---

## Recomposition Hotspots

| Composable | Recomp/Frame | Cause | Impact | Priority |
|------------|--------------|-------|--------|----------|
| HomeScreen | 60/sec | Timer in state | Critical jank | Critical |
| TodoItem | 20+ on scroll | Unstable lambdas | List stuttering | Critical |
| ShoppingList | Variable | Missing contentType | Slow recycling | High |
| CalendarMonth | 5+/gesture | Missing remember | Computation lag | High |
| ChatBubble | 3-4/message | Unstable props | Visible lag | Medium |
| WeatherWidget | 1/min | Expected | None | OK |

## Stability Report Summary

| Class | Stable | Issue | Fix |
|-------|--------|-------|-----|
| TodoUiState | ❌ | List<> | Use ImmutableList |
| Todo | ❌ | List<> | Use ImmutableList |
| ShoppingItem | ✓ | None | OK |
| CalendarEvent | ❌ | LocalDateTime | Add @Immutable |
| ChatMessage | ❌ | MutableMap | Use ImmutableMap |
| Weather | ✓ | None | OK |

## Performance Metrics

| Screen | Initial Comp | Recomposition | Frame Time | Status |
|--------|-------------|---------------|------------|--------|
| Home | 45ms | 60/sec | 28ms | ❌ Jank |
| TodoList | 30ms | 20/scroll | 22ms | ⚠️ Marginal |
| Shopping | 25ms | 5/scroll | 14ms | ✓ OK |
| Calendar | 80ms | 5/gesture | 18ms | ⚠️ Initial slow |
| Chat | 35ms | 3/msg | 12ms | ✓ OK |

## Remediation Priority

### Critical (Immediate)
1. Separate timer state from content state in HomeScreen
2. Stabilize lambdas in TodoListSection

### High Priority (This Sprint)
1. Add @Immutable to all UI state classes
2. Add contentType to LazyColumn/LazyRow
3. Add remember for expensive calculations

### Medium Priority (Next Sprint)
1. Extract smaller composables for better recomposition scope
2. Review and optimize ChatBubble recomposition
3. Add stability annotations to domain models

### Low Priority (Backlog)
1. Profile and optimize initial composition time
2. Implement movableContentOf for animated content
3. Add Compose metrics to CI pipeline
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Focused performance review
- **ST-02** (Structured Sequential Instructions) - Systematic optimization areas
- **RT-02** (Multi-Dimensional Analysis) - State, lambda, layout, list aspects
- **RT-05** (Evidence-Based Reasoning) - Recomposition counts and metrics
- **ST-03** (Output Format Templates) - Performance report structure
- **DS-06** (Prioritization Guidance) - Performance-based priority
- **OC-03** (Tabular Output) - Hotspot and metric matrices

---

## Related Prompts

- `android_viewmodel_state_management_review.md` - For ViewModel state patterns
- `android_kotlin_best_practices.md` - General Kotlin optimization
- `performance_bottleneck_identification.md` - General performance analysis
- `android_room_database_query_review.md` - For data layer optimization
- `code_quality_code_complexity_analysis.md` - For composable complexity

---

## Customization Guide

- **For Animation-Heavy UIs:** Add animation performance, derivedStateOf for animations
- **For Real-Time Apps:** Focus on high-frequency state updates, debouncing
- **For Large Lists:** Expand LazyColumn section, add paging considerations
- **For Complex Forms:** Add form state management, validation recomposition
- **For Accessibility:** Add content description impact, semantic properties
