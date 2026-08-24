---
title: "Kotlin & Jetpack Compose Debugging Audit "
category: mobile-development
description: "Audits Kotlin and Jetpack Compose code for the crash and defect patterns behind common runtime failures — null-safety, recomposition loops, LazyColumn keys, state handling, coroutines, side effects, and unsafe casts — producing file:line findings with fixes."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - debugging
  - mobile-development
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/ai_code_review_android.md
  - domain-software-engineering/mobile/android/analysis/android_performance_audit.md
  - domain-software-engineering/mobile/android/targeted-reviews/android_compose_recomposition_review.md
---


# Kotlin & Jetpack Compose Debugging Audit

**Objective:** Analyze a Kotlin/Jetpack Compose codebase to identify common crashes, bugs, and pitfalls based on known Android development issues, including null safety violations, recomposition problems, state management errors, coroutine race conditions, and side effect misuse.

---

## Context

This prompt systematically checks for **7 critical categories** of issues commonly found in Kotlin and Jetpack Compose applications:

1. Null Safety & Smart Casting Issues (KT-22158 and related)
2. Compose Recomposition Problems
3. LazyColumn/LazyRow Crashes
4. State Management Pitfalls
5. Coroutines & Flow Issues
6. Side Effects Misuse
7. Type Casting Crashes

These issues are based on documented crash patterns, JetBrains YouTrack issues, and Android development best practices.

---

## Instructions

### Step 1: Review Codebase Structure

First, scan the codebase to identify:
- All `@Composable` functions
- ViewModel implementations
- Repository/data layer files
- Coroutine usage patterns
- State management approaches

Document the general architecture and tech stack (Compose version, coroutine libraries, state management patterns).

### Step 2: Analyze for Category 1 - Null Safety & Smart Casting Issues

**Search for these specific patterns:**

#### 2.1 `isNullOrBlank()` / `isNullOrEmpty()` Smart Cast Failure

Look for code where nullable properties (`String?`, `Int?`, etc.) are used directly after `isNullOrBlank()` or `isNullOrEmpty()` checks without assignment to a local variable:

```kotlin
// CRASH-PRONE PATTERN:
if (!item.locationLabel.isNullOrBlank()) {
    Text(text = item.locationLabel)  // Still String?, may crash
}
```

**Detection criteria:**
- Nullable property accessed after `isNullOrBlank()` check
- No local variable assignment between check and usage
- Commonly found in Composable functions with data class parameters

#### 2.2 Mutable Property Smart Cast Failure

Look for `var` properties that are null-checked and then used without copying to a local `val`:

```kotlin
// CRASH-PRONE PATTERN:
var name: String? = "John"
if (name != null) {
    println(name.length)  // Error: Smart cast impossible
}
```

#### 2.3 Properties from External Modules

Identify properties from external modules or data classes used without local variable assignment after null checks.

**For each issue found, document:**
- **File:** `path/to/file.kt`
- **Line(s):** Line number(s)
- **Issue:** Description of the smart cast failure pattern
- **Current Code:** Exact code snippet
- **Risk:** Why this can crash (smart cast doesn't work, race condition, etc.)
- **Severity:** High (crashes), Medium (unreliable), Low (edge case)
- **Fix:** Specific code change with safe pattern:
  ```kotlin
  // SAFE: Assign to local variable first
  val locationLabel = item.locationLabel
  if (!locationLabel.isNullOrBlank()) {
      Text(text = locationLabel)  // Smart casted to String
  }
  ```

### Step 3: Analyze for Category 2 - Compose Recomposition Problems

**Search for these specific patterns:**

#### 3.1 Infinite Recomposition Loop

Look for state updates in Composable body (outside of `LaunchedEffect` or other side effect handlers):

```kotlin
// CRASH-PRONE PATTERN:
@Composable
fun BadExample() {
    var count by remember { mutableStateOf(0) }
    count++  // Updates on every recomposition!
    Text("Count: $count")
}
```

**Detection criteria:**
- State mutation directly in Composable body
- State setters called outside side effect APIs
- Conditional logic that updates state based on other state

#### 3.2 Unstable Types Causing Excessive Recomposition

Look for Composable parameters using unstable types (regular `List`, `Set`, `Map`, custom classes without `@Stable` or `@Immutable`):

```kotlin
// BAD PATTERN:
@Composable
fun ItemList(items: List<String>) {  // List is unstable!
    items.forEach { Text(it) }
}
```

#### 3.3 Expensive Operations During Recomposition

Look for expensive operations (sorting, filtering, mapping, complex calculations) in Composable body without `remember`:

```kotlin
// BAD PATTERN:
@Composable
fun SortedList(items: List<Item>) {
    val sorted = items.sortedBy { it.name }  // Runs every recomposition!
    LazyColumn { items(sorted) { ... } }
}
```

#### 3.4 Reading State in Wrong Compose Phase

Look for scroll state, list state, or other frequently-changing state read directly without `derivedStateOf`:

```kotlin
// BAD PATTERN:
@Composable
fun BadScrollButton(scrollState: LazyListState) {
    val showButton = scrollState.firstVisibleItemIndex > 0  // Triggers full recomposition
    if (showButton) { FloatingActionButton(...) }
}
```

**For each issue, document the same format as Category 1.**

### Step 4: Analyze for Category 3 - LazyColumn/LazyRow Crashes

**Search for these specific patterns:**

#### 4.1 Duplicate Keys Crash

Look for `LazyColumn`/`LazyRow` with `key` parameter that might have duplicates:

```kotlin
// CRASH-PRONE PATTERN:
LazyColumn {
    items(listWithDuplicates, key = { it.id }) { item ->  // Crash if IDs aren't unique!
        ItemRow(item)
    }
}
```

#### 4.2 Missing Keys Causing State Loss

Look for `LazyColumn`/`LazyRow` items with local state (`remember`) but no `key` parameter:

```kotlin
// BAD PATTERN:
LazyColumn {
    items(items) { item ->  // No key!
        var expanded by remember { mutableStateOf(false) }  // Resets on scroll!
        ExpandableItem(item, expanded)
    }
}
```

#### 4.3 Nested Scrollable Crash

Look for nested scrollables with the same direction:

```kotlin
// CRASH PATTERN:
LazyColumn {
    item {
        Column(Modifier.verticalScroll(rememberScrollState())) {  // CRASH!
            // Content
        }
    }
}
```

#### 4.4 `remember` Inside LazyColumn Resets

Look for expensive state created with `remember` (not `rememberSaveable`) inside LazyColumn items without hoisting:

**For each issue, document the same format as above.**

### Step 5: Analyze for Category 4 - State Management Pitfalls

**Search for these specific patterns:**

#### 5.1 `remember` vs `rememberSaveable`

Look for UI state (text input, selections, expansions) using `remember` that should survive configuration changes:

```kotlin
// ISSUE: State lost on configuration change (rotation)
var text by remember { mutableStateOf("") }  // Lost on rotation!
```

#### 5.2 Stale State in Lambdas

Look for `LaunchedEffect` with wrong keys that capture stale state:

```kotlin
// BUG PATTERN:
LaunchedEffect(Unit) {
    while (true) {
        delay(1000)
        count++  // Always uses initial value!
    }
}
```

#### 5.3 One-Time Events Triggering Multiple Times

Look for snackbars, navigation, or other one-time events triggered with wrong keys:

```kotlin
// BUG PATTERN:
if (showSnackbar) {
    LaunchedEffect(Unit) {  // Triggers every recomposition!
        snackbarHostState.showSnackbar("Message")
    }
}
```

**For each issue, document the same format as above.**

### Step 6: Analyze for Category 5 - Coroutines & Flow Issues

**Search for these specific patterns:**

#### 6.1 Race Conditions with Shared Mutable State

Look for mutable variables accessed by multiple coroutines without synchronization:

```kotlin
// BUG PATTERN:
var counter = 0
coroutineScope.launch { repeat(1000) { counter++ } }
coroutineScope.launch { repeat(1000) { counter++ } }
// counter may not be 2000!
```

**Detection criteria:**
- Shared `var` modified in multiple `launch` blocks
- No `Mutex`, `synchronized`, or atomic types
- State not using `StateFlow` or `MutableStateFlow`

#### 6.2 StateFlow Not Emitting Initial Value

Identify where collectors might miss initial StateFlow value due to timing.

#### 6.3 Cold vs Hot Flow Confusion

Look for cold flows (`flow {}`) collected multiple times causing duplicate operations:

```kotlin
// ISSUE PATTERN:
val coldFlow = flow {
    println("Fetching...")  // Runs for each collector!
    emit(fetchData())
}

// Multiple collectors
val data1 by coldFlow.collectAsState(null)
val data2 by coldFlow.collectAsState(null)  // Fetches twice!
```

#### 6.4 Unconfined Dispatcher Deadlock Risk

Look for `Dispatchers.Unconfined` used with `Mutex` or blocking operations.

**For each issue, document the same format as above.**

### Step 7: Analyze for Category 6 - Side Effects Misuse

**Search for these specific patterns:**

#### 7.1 Using `SideEffect` for Business Logic

Look for `SideEffect` used for analytics, logging, or business operations (should use `LaunchedEffect`):

```kotlin
// BAD PATTERN:
SideEffect {
    analytics.logScreen("Profile")  // Runs every recomposition!
}
```

#### 7.2 DisposableEffect Not Cleaning Up

Look for `DisposableEffect` that adds listeners/observers but doesn't remove them in `onDispose`:

```kotlin
// BUG PATTERN:
DisposableEffect(Unit) {
    source.addListener(listener)
    onDispose { }  // Forgot to remove!
}
```

#### 7.3 Wrong Key for LaunchedEffect

Look for `LaunchedEffect(Unit)` that should re-run when specific values change:

```kotlin
// BUG PATTERN:
LaunchedEffect(Unit) {
    loadData(userId)  // Only runs once, even if userId changes!
}
```

**For each issue, document the same format as above.**

### Step 8: Analyze for Category 7 - Type Casting Crashes

**Search for these specific patterns:**

#### 8.1 Unsafe Cast Crash

Look for unsafe casts (`as`) instead of safe casts (`as?`):

```kotlin
// CRASH PATTERN:
val text = obj as String  // ClassCastException if obj is not String
```

#### 8.2 Generic Type Erasure

Look for runtime type checks on generic types:

```kotlin
// CRASH PATTERN:
if (list is List<String>) {  // Warning: unchecked cast
    // This check doesn't work as expected!
}
```

**For each issue, document the same format as above.**

### Step 9: Identify Patterns and Trends

After analyzing all categories:

1. **Identify systemic issues:**
   - Which categories have the most issues?
   - Are there architectural patterns causing repeated problems?
   - Is there inconsistent use of state management?

2. **Calculate risk score:**
   - Count High/Medium/Low severity issues
   - Identify files with multiple critical issues
   - Highlight areas of highest risk

3. **Detect missing best practices:**
   - No use of `@Immutable`/`@Stable` annotations
   - Inconsistent coroutine scope usage
   - Missing key parameters in LazyColumn/LazyRow

### Step 10: Prioritize Findings

Rank all identified issues by:

**Priority 1 (Fix Immediately):**
- Null safety issues causing crashes (Category 1)
- Infinite recomposition loops (Category 2.1)
- Duplicate keys in LazyColumn (Category 3.1)
- Race conditions with critical data (Category 5.1)
- Unsafe casts (Category 7.1)

**Priority 2 (Fix Soon):**
- State lost on configuration changes (Category 4.1)
- DisposableEffect memory leaks (Category 6.2)
- Excessive recomposition from unstable types (Category 2.2)
- Missing keys causing state loss (Category 3.2)

**Priority 3 (Optimize):**
- Expensive operations without remember (Category 2.3)
- Cold flows collected multiple times (Category 5.3)
- SideEffect misuse (Category 6.1)

**Priority 4 (Refactor When Time Permits):**
- Generic type erasure issues (Category 7.2)
- StateFlow timing issues (Category 5.2)
- Reading state in wrong phase (Category 2.4)

### Step 11: Generate Summary Report

If no issues are found in a category, explicitly state: "**No significant issues detected in [Category Name].**"

If issues ARE found, provide:
- Total issue count by category
- Total issue count by severity (High/Medium/Low)
- Total issue count by priority (P1/P2/P3/P4)
- Top 5 riskiest files
- Top 3 recommended actions

---

## Expected Output

Provide a comprehensive debugging audit report with the following structure:

### Part 1: Executive Summary

```
# Kotlin & Jetpack Compose Debugging Audit Report

**Codebase:** [Project name]
**Compose Version:** [Version from build files]
**Analysis Date:** [Date]
**Total Issues Found:** [Number]

## Overview
- Total files analyzed: [X]
- Total Composable functions analyzed: [X]
- Total issues identified: [X]
  - Priority 1 (Critical): [X]
  - Priority 2 (Important): [X]
  - Priority 3 (Optimization): [X]
  - Priority 4 (Refactor): [X]

## Risk Assessment
[Brief paragraph on overall code health and highest risk areas]

## Top 3 Recommended Actions
1. [Most critical fix]
2. [Second most critical fix]
3. [Third most critical fix]
```

### Part 2: Detailed Findings by Category

For each category (1-7), provide:

```
## Category [N]: [Category Name]

### Issues Found: [X]

---

#### Issue [N.1]: [Brief Description]

**File:** `path/to/file.kt`
**Line(s):** [Line numbers]
**Severity:** [High/Medium/Low]
**Priority:** [P1/P2/P3/P4]

**Current Code:**
```kotlin
[Exact problematic code snippet]
```

**Problem:**
[Clear explanation of why this is an issue, what can go wrong, and under what conditions]

**Recommended Fix:**
```kotlin
[Corrected code snippet with safe pattern]
```

**Why This Works:**
[Explanation of how the fix addresses the root cause]

**References:**
- [Link to relevant documentation or YouTrack issue if applicable]

---

[Repeat for each issue in category]

---

**Category Summary:** [Paragraph summarizing patterns in this category]
```

### Part 3: Pattern Analysis

```
## Systemic Patterns Observed

### Most Common Issue Types
1. [Issue type]: [X] occurrences
2. [Issue type]: [X] occurrences
3. [Issue type]: [X] occurrences

### Architectural Concerns
[Analysis of whether issues stem from architectural decisions]

### Code Quality Observations
[Observations about code consistency, best practice adherence, etc.]
```

### Part 4: Prioritized Action Plan

```
## Recommended Fix Order

### Priority 1: Critical Fixes (Fix This Week)
1. **[File:Line]** - [Issue description] - [Estimated effort: X mins]
2. **[File:Line]** - [Issue description] - [Estimated effort: X mins]
[Continue...]

### Priority 2: Important Fixes (Fix This Sprint)
[Same format]

### Priority 3: Optimizations (Next Sprint)
[Same format]

### Priority 4: Refactoring (Backlog)
[Same format]
```

### Part 5: Preventive Recommendations

```
## Preventive Measures for Future Development

### Recommended Lint Rules
- Enable Kotlin smart cast warnings
- Add custom Compose lint checks for recomposition
- Configure detekt rules for coroutine safety

### Architecture Improvements
- [Suggestion 1]
- [Suggestion 2]
- [Suggestion 3]

### Team Best Practices
- [Practice 1]
- [Practice 2]
- [Practice 3]

### Testing Additions
- Add recomposition counting tests
- Add state restoration tests (configuration changes)
- Add coroutine race condition tests
```

### Part 6: Quick Reference Checklist

Provide the debugging checklist from the source document for future use:

```
## Quick Debugging Checklist for Future Development

### Null Safety
- [ ] Are nullable properties used after `isNullOrBlank()`/`isNullOrEmpty()` without local variable assignment?
- [ ] Are mutable (`var`) properties being smart-casted?
- [ ] Are properties from external modules used without local assignment after null checks?

### Compose Recomposition
- [ ] Is state being updated unconditionally in a Composable body?
- [ ] Are expensive operations (sort, filter, map) running without `remember`?
- [ ] Are unstable types being passed to Composables?
- [ ] Is `derivedStateOf` needed to defer state reads?

### LazyColumn/LazyRow
- [ ] Are item keys unique?
- [ ] Are item keys stable (not based on position)?
- [ ] Is there nested scrolling with the same direction?
- [ ] Is `remember` inside items losing state on scroll?

### State Management
- [ ] Should `rememberSaveable` be used instead of `remember`?
- [ ] Are one-time events (navigation, snackbar) re-triggering?
- [ ] Is state in lambdas stale (captured by value)?

### Side Effects
- [ ] Is `LaunchedEffect`/`DisposableEffect` using the correct key?
- [ ] Is `DisposableEffect` properly cleaning up resources?
- [ ] Is business logic incorrectly placed in `SideEffect`?

### Coroutines
- [ ] Is there shared mutable state without synchronization?
- [ ] Is a cold flow being collected multiple times?
- [ ] Are there potential deadlocks with Mutex?

### Type Casting
- [ ] Are unsafe casts (`as`) used instead of safe casts (`as?`)?
- [ ] Are generic types checked at runtime without reified parameters?
```

---

## Verification

After completing your initial analysis:

1. **Review for completeness:**
   - Did you check all 7 categories thoroughly?
   - Did you provide specific file paths and line numbers for every issue?
   - Did you include both the problematic code AND the fix for every issue?

2. **Verify prioritization:**
   - Are crash-causing issues marked Priority 1?
   - Are performance issues appropriately prioritized?
   - Is the recommended fix order logical and achievable?

3. **Check for false positives:**
   - List any potential false positives you identified
   - Explain why they might not be actual issues
   - Provide context for borderline cases

4. **Assess confidence:**
   - For each issue, rate your confidence: High/Medium/Low
   - If confidence is Medium or Low, explain what additional information would help
   - Flag any areas where static analysis alone is insufficient

---

## Important Notes

1. **Line Numbers Required:** Always provide specific file paths and line numbers for each issue. Never give general advice without concrete locations.

2. **Code Snippets Required:** Always show both the problematic code AND the fixed version for each issue.

3. **Evidence-Based:** Every issue must cite specific code from the codebase, not hypothetical examples.

4. **No Issues = Say So:** If a category has no issues, explicitly state it. Don't skip categories.

5. **Prioritize by Impact:** A crash-causing issue in rarely-used code may be lower priority than a performance issue in critical UI.

6. **Consider Context:** Not every pattern is wrong in every context. Explain when exceptions might be acceptable.

7. **Known Issues:** Reference JetBrains YouTrack issues (like KT-22158) when applicable to provide context.

---

## References

This debugging audit is based on documented issues and best practices from:

- [JetBrains YouTrack: KT-22158 - isNullOrBlank Smart Cast](https://youtrack.jetbrains.com/issue/KT-22158)
- [Android Developers: Compose Best Practices](https://developer.android.com/develop/ui/compose/performance/bestpractices)
- [Baeldung: Fixing Smart Cast Impossible](https://www.baeldung.com/kotlin/smart-cast-to-type-is-impossible)
- [Medium: Pitfalls of Jetpack Compose Recomposition](https://medium.com/@rzmeneghelo/the-pitfalls-of-jetpack-compose-recomposition-how-to-avoid-breaking-your-app-8569589d095f)
- [Medium: 10 Critical Jetpack Compose Mistakes](https://medium.com/@sharmapraveen91/10-critical-jetpack-compose-mistakes-youre-probably-making-and-how-to-fix-them-04064e950b2f)
- [ProAndroidDev: Common Performance Pitfalls in Compose](https://proandroiddev.com/overcoming-common-performance-pitfalls-in-jetpack-compose-98e6b155fbb4)
- [Medium: Solving Race Conditions in Kotlin Coroutines](https://medium.com/@1mailanton/solving-problem-of-race-condition-in-kotlin-coroutines-958abfceab37)
- [Dave Leeds: Preventing Race Conditions in Coroutines](https://typealias.com/articles/prevent-race-conditions-in-coroutines/)
- [droidcon: Stop Recomposition Errors](https://www.droidcon.com/2025/12/15/stop-recomposition-errors-how-to-correctly-handle-one-time-events-in-jetpack-compose/)

---

**Last Updated:** December 2024
**Based on:** KOTLIN_COMPOSE_DEBUGGING_GUIDE.md.txt (crash investigation findings for KT-22158 and related issues)
