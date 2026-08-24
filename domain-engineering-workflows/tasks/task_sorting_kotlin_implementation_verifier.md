---
title: "Task Sorting Algorithm - Kotlin Implementation Verifier"
category: engineering-workflows/tasks
description: "Verify a Kotlin/Android implementation of a task-sorting algorithm against its specification, checking algorithmic correctness, Kotlin idioms, Android architecture, performance, edge cases, and tests with file:line evidence."
techniques:
  - ST-01
  - RT-02
  - QA-01
  - DS-06
  - QA-02
difficulty: advanced
tags:
  - kotlin
  - android
  - code-review
  - implementation-verification
  - task-prioritization
updated: "2026-06-07"
related_prompts:
  - domain-engineering-workflows/tasks/task_sorting_algorithm_designer.md
  - domain-engineering-workflows/tasks/task_sorting_algorithm_reviewer.md
  - domain-engineering-workflows/improvement/improvement_best_practice_analysis.md
---

# Task Sorting Algorithm - Kotlin Implementation Verifier

**Objective:** Verify that a task-sorting algorithm is correctly implemented in Kotlin for Android — confirming alignment with its specification, algorithmic correctness, Kotlin idioms, Android architecture integration, performance, edge-case handling, and test coverage, with file:line evidence for every finding.

**When to use:**
- Reviewing a Kotlin implementation of a task-sorting algorithm before release.
- Debugging unexpected sorting behavior in an Android app.
- Code-review or production-readiness gate for the sorting feature.
- Confirming an implementation matches a design from `task_sorting_algorithm_designer.md`.

**When NOT to use:**
- Designing the algorithm — use `task_sorting_algorithm_designer.md`.
- Reviewing the algorithm's logic/UX independent of code — use `task_sorting_algorithm_reviewer.md`.
- Non-Kotlin implementations (the Kotlin/Android idiom checks won't apply).

**Audience:** Android engineers and reviewers validating a Kotlin task-sorting implementation.

---

## Inputs / Context

The user supplies:
1. **The implementation** — wrap pasted Kotlin in a `<code>` tag (note file paths and the class/function under review); or a repo path.
2. **The algorithm specification** — design doc or expected behavior to verify against.
3. **Implementation context** — architecture layer (ViewModel/UseCase/Repository), min/target SDK, DI framework, key dependencies.
4. **Performance budget** (optional) — e.g. "sort 100 tasks within one 60fps frame."

If the spec is unavailable, verify internal consistency and idioms, and flag correctness checks as "spec-dependent."

---

## Constraints

### Must
- Cite **file:line** for every finding.
- Check correctness against the spec (sort order, tie-breaking, null handling, overflow, timezone).
- Review Kotlin idioms (null safety, collection ops, `when`, immutability) and Android integration (lifecycle, coroutines/dispatchers, DI).
- Assess performance from the actual code (derive complexity; benchmarks only if provided/run).
- Give every issue a severity and a concrete before/after fix.

### Must Not
- Invent benchmark timings or test-coverage percentages — derive complexity from the code; label any runtime as an estimate unless measured.
- Flag idiomatic-but-unfamiliar Kotlin as a defect without a principle or rule behind it.
- Assert a correctness bug without tracing the input → output path that triggers it.
- Claim spec misalignment when no spec was provided — mark as spec-dependent.

---

## Instructions

### 1. Implementation Overview and Context

First, gather essential information about the implementation:

**Algorithm Specification:**
```
Algorithm Name: [Name from design spec]
Design Document: [Link or reference to algorithm spec]
Expected Behavior: [High-level description of what algorithm should do]

Key Algorithm Features:
- [Feature 1: e.g., weighted scoring based on due date and priority]
- [Feature 2: e.g., context-aware reordering based on location]
- [Feature 3: e.g., adaptive learning from user behavior]
```

**Implementation Context:**
```
File Location: [e.g., app/src/main/java/com/example/tasks/sorting/TaskSorter.kt]
Related Files: [List related classes, interfaces, data models]
Architecture Layer: [Domain/UseCase/ViewModel/Repository]
Android Version Target: [Minimum SDK, Target SDK]
Dependencies: [Libraries used, if any]
```

**Code Structure:**
```kotlin
// Primary classes/functions
class TaskSorter {
    fun sortTasks(tasks: List<Task>, context: SortingContext): List<Task>
}

// Data models
data class Task(...)
data class SortingContext(...)
```

### 2. Algorithmic Correctness Verification

**Specification Alignment Check:**

For each requirement in the algorithm specification:

| Requirement | Implementation Location | Status | Notes |
|-------------|------------------------|--------|-------|
| [Req 1: Sort by due date] | [File:Line] | ✓ / ✗ / ⚠ | [Any discrepancies] |
| [Req 2: Weight by priority] | [File:Line] | ✓ / ✗ / ⚠ | [Any discrepancies] |
| [Req 3: Handle null due dates] | [File:Line] | ✓ / ✗ / ⚠ | [Any discrepancies] |

**Logic Flow Analysis:**

Trace through the implementation step-by-step:

```kotlin
// Example analysis
fun sortTasks(tasks: List<Task>, context: SortingContext): List<Task> {
    // Step 1: Filter completed tasks [Line X]
    // ✓ Correct: Filters as expected
    // ⚠ Issue: No null check on tasks list

    // Step 2: Calculate scores [Line Y]
    // ✓ Correct: Scoring formula matches spec
    // ✗ Issue: Integer overflow possible with large scores

    // Step 3: Sort by score descending [Line Z]
    // ✓ Correct: Proper sort order

    return sortedTasks
}
```

**For Each Implementation Block:**
- **Matches Spec:** Does code implement what was designed?
- **Correctness:** Is the logic mathematically/algorithmically correct?
- **Edge Cases:** Are boundary conditions handled?
- **Assumptions:** Are any implicit assumptions made?

**Common Algorithm Implementation Errors:**

Check for these specific issues:

- [ ] **Off-by-one errors** in date comparisons or array indexing
- [ ] **Integer overflow** in score calculations
- [ ] **Floating-point precision issues** in weight calculations
- [ ] **Incorrect comparison operators** (< vs <=, > vs >=)
- [ ] **Reversed sort order** (ascending vs descending)
- [ ] **Timezone handling** for date/time comparisons
- [ ] **Null handling** in optional fields
- [ ] **Empty collection handling**
- [ ] **Tie-breaking logic** when scores are equal
- [ ] **Missing fallback** when insufficient data for sorting

### 3. Kotlin Language Best Practices Review

**Null Safety:**

Review all nullable types and null handling:

```kotlin
// ✗ BAD: Force unwrapping without safety
fun calculateScore(task: Task): Int {
    return task.dueDate!!.toEpochDay() // Can crash if null
}

// ✓ GOOD: Safe null handling with elvis operator
fun calculateScore(task: Task): Int {
    return task.dueDate?.toEpochDay() ?: Int.MAX_VALUE // Safe default
}

// ✓ GOOD: Early return for null case
fun calculateScore(task: Task): Int {
    val dueDate = task.dueDate ?: return Int.MAX_VALUE
    return dueDate.toEpochDay()
}
```

**Audit Checklist:**
- [ ] No force unwrapping (!!) without null checks
- [ ] Nullable types properly declared with `?`
- [ ] Safe calls (`?.`) or elvis operators (`?:`) used appropriately
- [ ] Smart casts leveraged where possible
- [ ] Let/run/apply used for null-safe chaining where appropriate

**Idiomatic Kotlin:**

Check for proper use of Kotlin features:

```kotlin
// ✗ BAD: Java-style loops and mutability
fun filterActiveTasks(tasks: List<Task>): List<Task> {
    val result = ArrayList<Task>()
    for (i in 0 until tasks.size) {
        if (!tasks[i].completed) {
            result.add(tasks[i])
        }
    }
    return result
}

// ✓ GOOD: Functional style with filter
fun filterActiveTasks(tasks: List<Task>): List<Task> {
    return tasks.filter { !it.completed }
}

// ✗ BAD: Verbose conditional
fun getPriorityWeight(priority: Priority): Int {
    if (priority == Priority.HIGH) {
        return 10
    } else if (priority == Priority.MEDIUM) {
        return 5
    } else {
        return 1
    }
}

// ✓ GOOD: When expression
fun getPriorityWeight(priority: Priority): Int = when (priority) {
    Priority.HIGH -> 10
    Priority.MEDIUM -> 5
    Priority.LOW -> 1
}
```

**Idiomatic Kotlin Checklist:**
- [ ] Collection operations (filter, map, sortedBy, etc.) used over loops
- [ ] `when` expressions used instead of if-else chains
- [ ] Data classes used for simple data holders
- [ ] Extension functions used for utility operations
- [ ] Destructuring used where appropriate
- [ ] Sealed classes used for state representation
- [ ] Companion objects vs top-level functions used appropriately
- [ ] Scope functions (let, run, with, apply, also) used correctly

**Immutability and Functional Style:**

```kotlin
// ✗ BAD: Mutable state
class TaskSorter {
    private var cachedScores = mutableMapOf<String, Int>()

    fun sortTasks(tasks: List<Task>): List<Task> {
        cachedScores.clear() // Side effect, not thread-safe
        tasks.forEach { task ->
            cachedScores[task.id] = calculateScore(task)
        }
        return tasks.sortedBy { cachedScores[it.id] }
    }
}

// ✓ GOOD: Immutable, pure function
class TaskSorter {
    fun sortTasks(tasks: List<Task>): List<Task> {
        val scores = tasks.associateWith { calculateScore(it) }
        return tasks.sortedByDescending { scores[it] }
    }
}
```

**Immutability Checklist:**
- [ ] Prefer `val` over `var`
- [ ] Use immutable collections (List, Set, Map) over mutable variants
- [ ] Avoid side effects in pure functions
- [ ] State mutations clearly isolated and justified
- [ ] Thread-safety considered for mutable state

### 4. Android-Specific Best Practices

**Architecture Component Integration:**

If integrated with Android Architecture Components:

**ViewModel Usage:**
```kotlin
// ✓ GOOD: Sorting in ViewModel, exposing as StateFlow
class TaskListViewModel @Inject constructor(
    private val taskRepository: TaskRepository,
    private val taskSorter: TaskSorter
) : ViewModel() {

    private val _sortedTasks = MutableStateFlow<List<Task>>(emptyList())
    val sortedTasks: StateFlow<List<Task>> = _sortedTasks.asStateFlow()

    fun loadAndSortTasks(context: SortingContext) {
        viewModelScope.launch {
            taskRepository.getTasks()
                .map { tasks -> taskSorter.sortTasks(tasks, context) }
                .collect { sorted -> _sortedTasks.value = sorted }
        }
    }
}
```

**Checklist:**
- [ ] No Context references held in ViewModel
- [ ] Sorting happens in appropriate layer (Domain/UseCase)
- [ ] Results exposed via StateFlow or LiveData
- [ ] Lifecycle-aware collection in UI layer
- [ ] No direct ViewModel-to-View coupling

**Dependency Injection:**

```kotlin
// ✓ GOOD: Hilt/Dagger integration
@Module
@InstallIn(SingletonComponent::class)
object TaskSortingModule {

    @Provides
    @Singleton
    fun provideTaskSorter(
        timeProvider: TimeProvider,
        userPreferences: UserPreferences
    ): TaskSorter {
        return TaskSorterImpl(timeProvider, userPreferences)
    }
}

class TaskSorterImpl @Inject constructor(
    private val timeProvider: TimeProvider,
    private val userPreferences: UserPreferences
) : TaskSorter {
    // Implementation
}
```

**Checklist:**
- [ ] Dependencies injected via constructor
- [ ] No direct instantiation with `new`
- [ ] Proper scope annotations (@Singleton, @ViewModelScoped, etc.)
- [ ] Interfaces used for testability
- [ ] No circular dependencies

**Threading and Coroutines:**

```kotlin
// ✗ BAD: Blocking main thread
class TaskSorter {
    fun sortTasks(tasks: List<Task>): List<Task> {
        Thread.sleep(100) // Simulate work - BLOCKS MAIN THREAD
        return tasks.sortedBy { calculateExpensiveScore(it) }
    }
}

// ✓ GOOD: Suspending function with proper dispatcher
class TaskSorter(
    private val ioDispatcher: CoroutineDispatcher = Dispatchers.Default
) {
    suspend fun sortTasks(tasks: List<Task>): List<Task> = withContext(ioDispatcher) {
        tasks.sortedBy { calculateExpensiveScore(it) }
    }
}

// ✓ GOOD: Non-suspending for quick operations
class TaskSorter {
    fun sortTasks(tasks: List<Task>): List<Task> {
        // Quick, CPU-bound operation under 16ms - safe on main thread
        return tasks.sortedBy { it.priority.ordinal }
    }
}
```

**Coroutine Checklist:**
- [ ] Long-running operations use suspend functions
- [ ] Appropriate dispatcher used (Main, IO, Default)
- [ ] Structured concurrency maintained
- [ ] No blocking calls on Main dispatcher
- [ ] viewModelScope or lifecycleScope used in UI components
- [ ] GlobalScope avoided (or justified if used)
- [ ] Exception handling with try-catch or CoroutineExceptionHandler

### 5. Performance Analysis

**Computational Complexity:**

Analyze actual time and space complexity:

```kotlin
fun sortTasks(tasks: List<Task>): List<Task> {
    // Line 1: Filter - O(n)
    val activeTasks = tasks.filter { !it.completed }

    // Line 2: Map to scores - O(n)
    val scores = activeTasks.associateWith { calculateScore(it) }

    // Line 3: Sort - O(n log n)
    return activeTasks.sortedByDescending { scores[it] }
}

// Overall: O(n log n) time, O(n) space
```

**Performance Assessment:**

| Operation | Actual Complexity | Expected Complexity | Status |
|-----------|------------------|---------------------|--------|
| Filtering | O(n) | O(n) | ✓ Optimal |
| Score calculation | O(n) | O(n) | ✓ Optimal |
| Sorting | O(n log n) | O(n log n) | ✓ Optimal |
| **Overall** | **O(n log n)** | **O(n log n)** | **✓ Optimal** |

**Benchmark Requirements:**

Based on typical app usage:

```kotlin
// Performance test example
@Test
fun `sorting 100 tasks completes under 16ms`() {
    val tasks = generateRandomTasks(100)
    val startTime = System.nanoTime()

    taskSorter.sortTasks(tasks, defaultContext)

    val duration = (System.nanoTime() - startTime) / 1_000_000 // Convert to ms
    assertThat(duration).isLessThan(16) // One frame at 60fps
}
```

**Performance Checklist:**
- [ ] Sorting 100 tasks: < 16ms (one frame)
- [ ] Sorting 1000 tasks: < 100ms (acceptable for background)
- [ ] No unnecessary allocations in hot path
- [ ] Efficient data structures used (no nested loops where avoidable)
- [ ] Caching implemented where beneficial
- [ ] Incremental updates possible for large lists

**Memory Efficiency:**

```kotlin
// ✗ BAD: Unnecessary copies and allocations
fun sortTasks(tasks: List<Task>): List<Task> {
    val copy1 = ArrayList(tasks) // Unnecessary copy
    val copy2 = copy1.map { it.copy() } // Another unnecessary copy
    val scores = mutableMapOf<String, Int>()
    copy2.forEach { task ->
        scores[task.id] = calculateScore(task)
    }
    return copy2.sortedBy { scores[it.id] }
}

// ✓ GOOD: Minimal allocations
fun sortTasks(tasks: List<Task>): List<Task> {
    return tasks.sortedByDescending { calculateScore(it) }
}
```

**Memory Checklist:**
- [ ] No unnecessary object allocations
- [ ] No memory leaks (Context leaks, listener leaks)
- [ ] Large collections handled efficiently
- [ ] Caches have size limits and eviction policies
- [ ] No holding references to Activities or Views

### 6. Edge Case and Error Handling

**Boundary Conditions:**

Test implementation with edge cases:

```kotlin
// Test each edge case
@Test fun `empty task list returns empty`()
@Test fun `single task returns single task`()
@Test fun `all tasks with same score maintains stable sort`()
@Test fun `all tasks overdue sorts by most overdue first`()
@Test fun `tasks with null due dates sorted to end`()
@Test fun `handles maximum integer values without overflow`()
@Test fun `handles date range limits (year 1970, 2100, etc)`()
```

**For Each Edge Case:**

| Edge Case | Code Location | Handling Status | Issue (if any) |
|-----------|---------------|----------------|----------------|
| Empty list | Line X | ✓ Returns empty | None |
| Single item | Line X | ✓ Returns item | None |
| All null due dates | Line Y | ⚠ Returns original order | Should be sorted by priority |
| Integer overflow | Line Z | ✗ Crashes | Need to use Long or clamp values |

**Error Handling:**

```kotlin
// ✗ BAD: Silently fails or crashes
fun sortTasks(tasks: List<Task>): List<Task> {
    return tasks.sortedBy {
        calculateScore(it) // Can throw exception, crashes app
    }
}

// ✓ GOOD: Graceful degradation
fun sortTasks(tasks: List<Task>): List<Task> {
    return try {
        tasks.sortedByDescending { task ->
            runCatching { calculateScore(task) }
                .getOrDefault(0) // Fallback score on error
        }
    } catch (e: Exception) {
        Timber.e(e, "Error sorting tasks, returning unsorted")
        tasks // Fallback to original order
    }
}
```

**Error Handling Checklist:**
- [ ] Exceptions caught and handled gracefully
- [ ] User never sees crash from sorting failure
- [ ] Fallback behavior is reasonable (unsorted list, default order)
- [ ] Errors logged for debugging
- [ ] Invalid data doesn't break sorting (NaN, null, extremes)

### 7. Testing Coverage Analysis

**Unit Test Review:**

Required test categories:

**Basic Functionality:**
```kotlin
@Test fun `sorts by due date ascending`()
@Test fun `sorts by priority when due dates equal`()
@Test fun `combines multiple sorting factors correctly`()
```

**Edge Cases:**
```kotlin
@Test fun `handles empty list`()
@Test fun `handles single item`()
@Test fun `handles null due dates`()
@Test fun `handles missing priorities`()
@Test fun `handles all tasks identical`()
```

**Algorithm Correctness:**
```kotlin
@Test fun `urgent important task ranks first`()
@Test fun `overdue tasks ranked by severity`()
@Test fun `future tasks ranked appropriately`()
@Test fun `score calculation matches specification`()
```

**Test Quality Assessment:**

| Test Category | Tests Present | Coverage | Quality | Issues |
|--------------|---------------|----------|---------|--------|
| Basic sorting | 5/5 | ✓ Complete | Good | None |
| Edge cases | 3/8 | ⚠ Partial | Medium | Missing null handling tests |
| Algorithm correctness | 2/6 | ✗ Insufficient | Poor | No tests for scoring formula |
| Performance | 0/3 | ✗ None | N/A | Add benchmark tests |

**Test Code Review:**

```kotlin
// ✗ BAD: Unclear test, hardcoded values
@Test
fun testSort() {
    val result = taskSorter.sortTasks(getTasks())
    assertEquals(3, result.size)
    assertEquals("Task A", result[0].name)
}

// ✓ GOOD: Clear test name, explicit setup, clear assertions
@Test
fun `overdue tasks are sorted before future tasks`() {
    // Given
    val overdueTask = Task(name = "Overdue", dueDate = yesterday)
    val futureTask = Task(name = "Future", dueDate = tomorrow)
    val tasks = listOf(futureTask, overdueTask)

    // When
    val sorted = taskSorter.sortTasks(tasks)

    // Then
    assertThat(sorted.first()).isEqualTo(overdueTask)
    assertThat(sorted.last()).isEqualTo(futureTask)
}
```

**Testing Checklist:**
- [ ] All requirements have corresponding tests
- [ ] Edge cases covered with explicit tests
- [ ] Test names clearly describe what is being tested
- [ ] Tests use clear Given-When-Then structure
- [ ] No hardcoded magic values in tests
- [ ] Test data is realistic and representative
- [ ] Mocking used appropriately for dependencies
- [ ] Tests are deterministic (no flakiness)

### 8. Code Quality and Maintainability

**Readability:**

```kotlin
// ✗ BAD: Unclear variable names, magic numbers
fun sortTasks(t: List<Task>): List<Task> {
    return t.sortedBy {
        val x = it.dueDate?.toEpochDay() ?: 99999
        val y = it.priority.ordinal * 1000
        x - y // What does this formula mean?
    }
}

// ✓ GOOD: Clear names, documented formula
fun sortTasks(tasks: List<Task>): List<Task> {
    return tasks.sortedBy { task ->
        calculateCompositeScore(task)
    }
}

private fun calculateCompositeScore(task: Task): Long {
    // Score = (days until due) - (priority weight)
    // Lower score = higher priority in sorted list
    val daysUntilDue = task.dueDate?.toEpochDay() ?: Long.MAX_VALUE
    val priorityWeight = task.priority.weight * DAYS_PER_PRIORITY_LEVEL
    return daysUntilDue - priorityWeight
}

private companion object {
    const val DAYS_PER_PRIORITY_LEVEL = 1000L // High priority = 1000 days earlier
}
```

**Documentation:**

```kotlin
/**
 * Sorts tasks by composite priority score.
 *
 * Algorithm combines multiple factors:
 * 1. Due date proximity (closer = higher priority)
 * 2. User-assigned priority (High/Medium/Low)
 * 3. Task category weights
 *
 * Tasks without due dates are sorted to the end.
 * When scores are equal, original order is preserved (stable sort).
 *
 * @param tasks List of tasks to sort
 * @param context Current sorting context (time, location, user preferences)
 * @return Sorted list with highest priority tasks first
 *
 * @see TaskSortingSpec for full algorithm specification
 */
fun sortTasks(tasks: List<Task>, context: SortingContext): List<Task>
```

**Code Organization:**

```kotlin
// ✓ GOOD: Well-organized class structure
class TaskSorter(
    private val timeProvider: TimeProvider,
    private val scoreCalculator: TaskScoreCalculator
) {
    // Public API
    fun sortTasks(tasks: List<Task>, context: SortingContext): List<Task> {
        return tasks
            .filter { isActive(it) }
            .sortedByDescending { calculateScore(it, context) }
    }

    // Private helpers - logically grouped
    private fun isActive(task: Task): Boolean = !task.completed

    private fun calculateScore(task: Task, context: SortingContext): Int {
        return scoreCalculator.calculate(task, context, timeProvider.now())
    }
}

// Separate class for complex scoring logic
class TaskScoreCalculator {
    fun calculate(task: Task, context: SortingContext, currentTime: Instant): Int {
        // Complex scoring logic isolated in dedicated class
    }
}
```

**Code Quality Checklist:**
- [ ] Variable and function names are descriptive
- [ ] Magic numbers extracted to named constants
- [ ] Complex logic extracted to named functions
- [ ] Public API documented with KDoc
- [ ] Algorithm assumptions and limitations documented
- [ ] Code follows project/team style guide
- [ ] No commented-out code
- [ ] No TODO or FIXME comments in production code

### 9. Integration and Compatibility

**API Compatibility:**

```kotlin
// ✓ GOOD: Stable public API
interface TaskSorter {
    fun sortTasks(tasks: List<Task>, context: SortingContext): List<Task>
}

// Implementation can change without breaking clients
class WeightedTaskSorter : TaskSorter {
    override fun sortTasks(tasks: List<Task>, context: SortingContext): List<Task> {
        // Implementation details
    }
}
```

**Data Model Compatibility:**

```kotlin
// ✓ GOOD: Backward compatible data model changes
@Parcelize
data class Task(
    val id: String,
    val name: String,
    val dueDate: LocalDate?,
    val priority: Priority,

    // New field with default value - backward compatible
    val estimatedDuration: Duration? = null,

    // New field with default - backward compatible
    @Since("2.0") val energyLevel: EnergyLevel = EnergyLevel.MEDIUM
) : Parcelable
```

**Android Version Compatibility:**

```kotlin
// ✓ GOOD: SDK version checks for new APIs
fun sortWithLocale(tasks: List<Task>): List<Task> {
    return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
        // Use newer LocaleList API
        tasks.sortedWith(compareBy(LocaleList.getDefault().get(0)) { it.name })
    } else {
        // Fallback for older versions
        tasks.sortedBy { it.name }
    }
}
```

**Integration Checklist:**
- [ ] Public API is stable and documented
- [ ] Breaking changes are avoided or properly versioned
- [ ] Data model changes are backward compatible
- [ ] SDK version requirements documented
- [ ] Proper compatibility checks for new Android APIs
- [ ] Migration path provided for breaking changes

### 10. Security and Privacy

**Data Handling:**

```kotlin
// ✓ GOOD: No logging of sensitive data
fun sortTasks(tasks: List<Task>): List<Task> {
    Timber.d("Sorting ${tasks.size} tasks") // ✓ Count is fine

    // ✗ DON'T: Timber.d("Sorting tasks: ${tasks.map { it.name }}")
    // Task names could contain PII

    return tasks.sortedBy { calculateScore(it) }
}
```

**Security Checklist:**
- [ ] No sensitive data in logs
- [ ] No hardcoded secrets or keys
- [ ] User data handled securely
- [ ] Proper permission checks if accessing device resources
- [ ] No SQL injection if using raw queries (should use Room)

## Expected Output

Your comprehensive Kotlin implementation verification should include:

### 1. Executive Summary
- **Overall Implementation Quality:** [Excellent/Good/Fair/Poor]
- **Algorithm Correctness:** [Matches spec / Has discrepancies]
- **Code Quality:** [Production-ready / Needs improvements / Requires rework]
- **Recommendation:** [Ship / Fix critical issues first / Major refactoring needed]

### 2. Algorithmic Correctness Report
- Specification alignment table (requirement vs implementation)
- Logic flow analysis with line-by-line verification
- Identified correctness issues with severity ratings
- Edge case handling assessment

### 3. Kotlin Best Practices Evaluation
- Null safety score: [X/10]
- Idiomatic Kotlin score: [X/10]
- Issues found: [list with file:line references]
- Code examples of issues with suggested fixes

### 4. Android Integration Review
- Architecture component usage: [compliant/issues found]
- Threading and coroutines: [compliant/issues found]
- Performance analysis: [time/space complexity, benchmarks]
- Memory efficiency: [score and issues]

### 5. Test Coverage Analysis
- Current coverage: [X%]
- Missing test categories: [list]
- Test quality assessment: [rating]
- Required additional tests: [list]

### 6. Prioritized Issue List

**Critical Issues (Must Fix Before Release):**
1. [Issue with file:line, description, fix]
2. [Issue with file:line, description, fix]

**High Priority (Fix This Sprint):**
1. [Issue with file:line, description, fix]
2. [Issue with file:line, description, fix]

**Medium Priority (Technical Debt):**
1. [Issue with file:line, description, fix]

**Low Priority (Nice to Have):**
1. [Issue with file:line, description, fix]

### 7. Code Quality Score Card

| Category | Score | Status |
|----------|-------|--------|
| Algorithm Correctness | X/10 | ✓ / ⚠ / ✗ |
| Null Safety | X/10 | ✓ / ⚠ / ✗ |
| Idiomatic Kotlin | X/10 | ✓ / ⚠ / ✗ |
| Performance | X/10 | ✓ / ⚠ / ✗ |
| Test Coverage | X/10 | ✓ / ⚠ / ✗ |
| Documentation | X/10 | ✓ / ⚠ / ✗ |
| Maintainability | X/10 | ✓ / ⚠ / ✗ |
| **Overall** | **X/10** | **✓ / ⚠ / ✗** |

### 8. Recommended Improvements

For each significant issue, provide:
```kotlin
// BEFORE (Current Implementation)
[problematic code]

// AFTER (Recommended Fix)
[improved code]

// Explanation
[Why this is better, what it fixes]
```

### 9. Verification Test Suite

Provide test code for validating fixes:
```kotlin
@Test
fun `specific edge case is now handled correctly`() {
    // Test code that would have failed before, passes after fix
}
```

## False-Positive Prevention

❌ **DON'T:**
- Don't report a benchmark time ("100 tasks in 8ms") or coverage % you didn't actually measure — derive complexity from the code and label runtime as an estimate.
- Don't flag idiomatic Kotlin (scope functions, `associateWith`, sealed classes) as a defect just because it's unfamiliar; cite a principle or rule.
- Don't assert a correctness bug (overflow, wrong tie-break) without tracing the input that triggers it.
- Don't claim the implementation "doesn't match spec" when no spec was provided — mark spec-dependent findings.

✅ **DO:**
- Cite file:line for every finding and give a concrete before/after fix.
- Derive time/space complexity from the actual code; mark wall-clock numbers as estimates unless measured.
- Trace the triggering input for each correctness bug.
- Distinguish confirmed issues from spec-dependent or context-dependent ones.

---

## Verification

- [ ] Correctness verified against the spec (order, tie-breaking, nulls, overflow, timezone) — or marked spec-dependent.
- [ ] Kotlin idioms (null safety, collections, `when`, immutability) reviewed.
- [ ] Android integration (lifecycle, coroutines/dispatchers, DI) reviewed.
- [ ] Performance assessed from code; benchmarks only if measured.
- [ ] Edge cases documented; tests assessed for gaps.
- [ ] Every issue has file:line, severity, and a before/after fix.
- [ ] No fabricated benchmark or coverage numbers.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the spec-aligned verification goal.
- **RT-02 (Multi-Dimensional Analysis):** Reviews correctness, idioms, architecture, performance, edge cases, and tests.
- **QA-01 (Self-Verification):** Final checklist confirms evidence and blocks fabricated metrics.
- **DS-06 (Prioritization and Severity Guidance):** Severity ranking orders the issue list (Critical → Low).
- **QA-02 (Adversarial Self-Critique):** Edge-case and overflow probing surfaces latent defects.

---

## Related Prompts

- `domain-engineering-workflows/tasks/task_sorting_algorithm_designer.md` — Source design spec to verify against.
- `domain-engineering-workflows/tasks/task_sorting_algorithm_reviewer.md` — Review the algorithm's logic and UX.
- `domain-engineering-workflows/improvement/improvement_best_practice_analysis.md` — Broader codebase quality audit.

## Customization Guide

**For New Implementations:**
- Focus on correctness and test coverage
- Emphasize clear documentation
- Validate against specification thoroughly
- Lighter on optimization (premature optimization)

**For Legacy Code:**
- Add section on refactoring opportunities
- Assess migration path to modern patterns
- Identify deprecation risks
- Consider backward compatibility carefully

**For Performance-Critical Paths:**
- Add detailed profiling section
- Include memory allocation analysis
- Benchmark against targets
- Consider algorithmic optimizations

**For Team Onboarding:**
- Add rationale for architectural decisions
- Explain non-obvious patterns
- Document common pitfalls
- Provide learning resources
