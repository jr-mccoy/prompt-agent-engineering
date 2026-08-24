---
title: "Android Compose Recomposition Problems Review"
category: mobile/android/targeted-reviews
description: "Android Compose Recomposition Problems Review."
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
  - problems
  - recomposition
  - reviews
updated: "2026-03-19"
related_prompts: []
---

# Android Compose Recomposition Problems Review

---
title: "Android Compose Recomposition Problems Review"
category: mobile/android/performance
description: "Detect Compose-specific recomposition problems that make the UI feel less immediate than it should"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - QA-01
difficulty: advanced
tags:
  - android
  - jetpack-compose
  - recomposition
  - stability
  - state
  - performance
  - side-effects
updated: "2026-03-09"
---

**Objective:** Analyze a Jetpack Compose codebase to identify recomposition problems — patterns where the rendering is smooth enough overall but the UI feels less immediate, responsive, or crisp than it should due to unnecessary, excessive, or poorly scoped recomposition.

**When to Use:** Use when a Compose app feels "not quite right" — not frozen, but not snappy either. When interactions have a subtle beat of delay, when typing feels slightly behind, when toggling a switch takes a moment to reflect, or when Compose compiler reports show high recomposition counts. This is one of the highest-probability performance buckets for Compose apps.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Verify with Compose compiler metrics or Layout Inspector** — Don't flag based on code patterns alone. Confirm that the composable actually recomposes more than expected.
2. **Check Compose's skip optimization** — Compose automatically skips recomposition for composables with stable, unchanged parameters. Verify the skip isn't already happening.
3. **Confirm user-visible impact** — Recomposition of cheap composables is fine. Focus on cases with measurable visual delay.
4. **Provide exact file:line locations.**

**Finding NO issues is an acceptable outcome.** Well-structured Compose code can be efficient.

### False-Positive Prevention

- ❌ Do NOT flag composables that recompose but are cheap (single `Text`, `Icon`, `Spacer`)
- ❌ Do NOT flag recomposition caused by actual state changes (that's correct behavior)
- ❌ Do NOT assume instability without checking the Compose compiler report
- ❌ Do NOT flag `remember {}` absence for trivially cheap operations
- ❌ Do NOT flag all lambdas as unstable — Compose handles non-capturing and composable lambdas well
- ✅ DO check the Compose compiler stability report for actual stability classifications
- ✅ DO verify recomposition count using Layout Inspector or `RecompositionHighlighter`
- ✅ DO distinguish "recomposes often" from "recomposes expensively"
- ✅ DO consider the recomposition frequency (per-frame vs per-user-action)

---

### 1. Rapidly Changing State Read Too High

Identify state that changes frequently being read at a high level in the tree:

* **Timer/counter/progress in screen-level state:**
  - A `currentTime`, `scrollProgress`, or `animationProgress` field in the main `UiState` class
  - Read at the screen composable level, causing all children to recompose

* **Text field state at screen level:**
  - `TextField` value in a monolithic screen state
  - Each keystroke triggers full-screen recomposition

**Best Practices:**
```kotlin
// ❌ BAD: Text input in screen-level state
data class FormScreenState(
    val name: String = "",          // changes on every keystroke
    val email: String = "",         // changes on every keystroke
    val items: List<Item> = ...,    // expensive list
    val isLoading: Boolean = false
)

@Composable
fun FormScreen(viewModel: FormViewModel) {
    val state by viewModel.state.collectAsStateWithLifecycle()
    // ENTIRE screen recomposes on every keystroke!
    Column {
        TextField(value = state.name, onValueChange = viewModel::updateName)
        TextField(value = state.email, onValueChange = viewModel::updateEmail)
        ExpensiveItemList(state.items) // recomposes on keystroke!
        SubmitButton(state.isLoading)  // recomposes on keystroke!
    }
}

// ✅ GOOD: Separate high-frequency state
@Composable
fun FormScreen(viewModel: FormViewModel) {
    val name by viewModel.name.collectAsStateWithLifecycle()
    val email by viewModel.email.collectAsStateWithLifecycle()
    val items by viewModel.items.collectAsStateWithLifecycle()
    val isLoading by viewModel.isLoading.collectAsStateWithLifecycle()

    Column {
        TextField(value = name, onValueChange = viewModel::updateName)
        TextField(value = email, onValueChange = viewModel::updateEmail)
        ExpensiveItemList(items) // only recomposes when items change
        SubmitButton(isLoading)  // only recomposes when loading changes
    }
}

// ✅ ALSO GOOD: Use lambda-based state reading for animations
Box(
    modifier = Modifier.offset {
        // Read in layout phase, doesn't trigger recomposition
        IntOffset(0, scrollState.value)
    }
)
```

**Suggested Fixes:**
- Split monolithic state into separate flows by change frequency
- Move `TextField` value to local `remember` state with ViewModel sync, or separate flow
- Use lambda-based modifiers (`Modifier.offset { }`, `Modifier.graphicsLayer { }`) for animation state — reads happen in layout/draw phase, not composition
- Use `derivedStateOf` to reduce change frequency of derived values

---

### 2. Mutable Collections as Parameters

Identify mutable collection types causing instability:

* **`List<T>`, `Map<K,V>`, `Set<T>` parameters:**
  - Compose compiler treats these as unstable — composable always recomposes when parent does
  - Even `emptyList()` creates a new reference each time

* **Mutable state collections:**
  - `mutableStateListOf` exposed as `List` — still considered unstable by compiler
  - `SnapshotStateList` casts

**Best Practices:**
```kotlin
// ❌ BAD: List is unstable
@Composable
fun TagList(tags: List<String>) { // Compose cannot skip this!
    tags.forEach { tag -> TagChip(tag) }
}

// ✅ GOOD: ImmutableList is stable
@Composable
fun TagList(tags: ImmutableList<String>) { // Compose can skip if unchanged
    tags.forEach { tag -> TagChip(tag) }
}

// In ViewModel:
_uiState.update { it.copy(tags = newTags.toImmutableList()) }

// Gradle dependency:
// implementation("org.jetbrains.kotlinx:kotlinx-collections-immutable:0.3.7")
```

**Suggested Fixes:**
- Use `kotlinx-collections-immutable` (`ImmutableList`, `ImmutableMap`, `ImmutableSet`)
- Add `@Immutable` annotation to data classes that genuinely are immutable
- Configure Compose compiler stability config file to declare external library types as stable
- Convert at the ViewModel boundary: `items.toImmutableList()`

---

### 3. Recreated Callbacks and Models

Identify objects recreated on every recomposition:

* **Lambda recreation:**
  - `onClick = { viewModel.doThing(item.id) }` — new lambda instance every composition
  - Callbacks with captured mutable state

* **Object recreation:**
  - `val style = TextStyle(fontSize = 16.sp)` created inline every composition
  - Data class instances built inline as parameters

* **Modifier recreation:**
  - Complex modifier chains without `remember`

**Best Practices:**
```kotlin
// ❌ BAD: New TextStyle every recomposition
@Composable
fun StyledText(text: String) {
    Text(text = text, style = TextStyle(fontSize = 16.sp, fontWeight = FontWeight.Bold))
}

// ✅ GOOD: Defined outside composition or remembered
private val headerStyle = TextStyle(fontSize = 16.sp, fontWeight = FontWeight.Bold)

@Composable
fun StyledText(text: String) {
    Text(text = text, style = headerStyle)
}

// ❌ BAD: Complex modifier recreated every time
@Composable
fun Card(onClick: () -> Unit) {
    Box(
        modifier = Modifier
            .shadow(4.dp, RoundedCornerShape(8.dp)) // new Shape instance!
            .clip(RoundedCornerShape(8.dp))           // another new Shape!
            .background(Color.White)
            .clickable(onClick = onClick)
    )
}

// ✅ GOOD: Cache shape, use MaterialTheme
private val cardShape = RoundedCornerShape(8.dp)

@Composable
fun Card(onClick: () -> Unit) {
    Box(
        modifier = Modifier
            .shadow(4.dp, cardShape)
            .clip(cardShape)
            .background(MaterialTheme.colorScheme.surface)
            .clickable(onClick = onClick)
    )
}
```

**Suggested Fixes:**
- Define styles, shapes, and other reusable objects as top-level constants or companion objects
- Use `remember` for objects that depend on composition parameters
- Use method references (`viewModel::doThing`) instead of lambdas when signature matches
- For lambdas with parameters, use `remember<(T) -> Unit> { { param -> ... } }`

---

### 4. Side Effects Launched Too Often

Identify side effects with incorrect keys:

* **`LaunchedEffect` with unstable keys:**
  - `LaunchedEffect(uiState)` where `uiState` changes frequently — relaunches effect on every change
  - `LaunchedEffect(Unit)` when the effect should respond to specific triggers

* **`DisposableEffect` churning:**
  - Effect disposes and re-registers on every recomposition due to unstable key
  - Listener registration/deregistration on every state change

* **Side effect in wrong scope:**
  - Work that should happen in ViewModel done in `LaunchedEffect`
  - Network calls triggered from composition

**Best Practices:**
```kotlin
// ❌ BAD: Relaunches on every state change
@Composable
fun Screen(viewModel: ScreenViewModel) {
    val state by viewModel.state.collectAsStateWithLifecycle()

    LaunchedEffect(state) { // cancels and restarts on EVERY state emission!
        analytics.trackScreenView(state.screenName)
    }
}

// ✅ GOOD: Launch only on specific trigger
@Composable
fun Screen(viewModel: ScreenViewModel) {
    val state by viewModel.state.collectAsStateWithLifecycle()

    LaunchedEffect(state.screenName) { // only relaunches when screen name changes
        analytics.trackScreenView(state.screenName)
    }
}

// ✅ BETTER: Move to ViewModel
class ScreenViewModel : ViewModel() {
    init {
        viewModelScope.launch {
            state.map { it.screenName }
                .distinctUntilChanged()
                .collect { analytics.trackScreenView(it) }
        }
    }
}
```

**Suggested Fixes:**
- Use the most specific, stable key possible for `LaunchedEffect` and `DisposableEffect`
- Move business logic side effects to ViewModel — only keep UI-specific effects in composables
- Use `rememberUpdatedState` for callbacks inside long-running effects
- Audit all `LaunchedEffect(Unit)` — these run once, which may or may not be correct

---

### 5. Coarse-Grained State Holders

Identify state holder patterns that expose too much at once:

* **Monolithic screen state:**
  - Single `data class ScreenState` with 10+ fields of varying update frequencies
  - Every field change triggers observation of the entire state

* **Screen-level `MutableState` for everything:**
  - All UI state in a single `mutableStateOf(ScreenState())`
  - No field-level granularity for skip optimization

**Best Practices:**
```kotlin
// ❌ BAD: Monolithic state
@HiltViewModel
class DashboardViewModel : ViewModel() {
    private val _state = MutableStateFlow(DashboardState())
    val state = _state.asStateFlow()
}

data class DashboardState(
    val userName: String = "",
    val notifications: List<Notification> = emptyList(),
    val balance: Double = 0.0,
    val recentTransactions: List<Transaction> = emptyList(),
    val isRefreshing: Boolean = false,
    val lastUpdated: Long = 0L // changes every refresh!
)

// ✅ GOOD: Granular state exposure
@HiltViewModel
class DashboardViewModel : ViewModel() {
    val userName: StateFlow<String> = ...
    val notifications: StateFlow<ImmutableList<Notification>> = ...
    val balance: StateFlow<Double> = ...
    val recentTransactions: StateFlow<ImmutableList<Transaction>> = ...
    val isRefreshing: StateFlow<Boolean> = ...
    // lastUpdated only exposed if UI actually needs it
}
```

**Suggested Fixes:**
- Split state by update frequency: fast-changing vs. slow-changing
- Expose individual `StateFlow`s for independent UI sections
- If monolithic state is architecturally required, use Compose's state selection: `snapshotFlow { state.value.specificField }.collectAsState()`
- Use `derivedStateOf` in composables to extract specific fields from coarse state

---

### 6. Large Composables That Recompose for Tiny Changes

Identify composables that are too large for their recomposition scope:

* **Entire screen in one function:**
  - 200+ line composable function that recomposes for any state change
  - No extraction of independent sections into child composables

* **Missing composable boundaries:**
  - Sections that could be independent but are inlined
  - UI elements that don't share state combined in one recomposition scope

**Suggested Fixes:**
- Extract independent UI sections into separate composable functions
- Each composable should have a clear, minimal set of parameters
- Use `key {}` to create distinct composition scopes within a single composable
- Profile with Layout Inspector to identify which sections actually need to recompose together

---

## Expected Output

Provide a Compose recomposition analysis report including:

### 1. Executive Summary
- Recomposition health rating
- Screens analyzed
- Compose compiler metrics summary (stable/unstable class counts)

### 2. Recomposition Hotspot Map

| Composable | Recomp Count | Trigger | Cost | Necessary? | Priority |
|------------|-------------|---------|------|------------|----------|
| [Name] | [per-sec or per-action] | [State change] | [cheap/moderate/expensive] | [Yes/No] | [Level] |

### 3. Stability Report

| Class/Type | Stable? | Reason | Composables Affected | Fix |
|------------|---------|--------|---------------------|-----|
| [Type] | [Yes/No] | [Why] | [List] | [Action] |

### 4. Detailed Findings

For each issue:
- **Location:** file:line
- **Category:** High State Read / Mutable Collections / Recreated Objects / Side Effects / Coarse State / Large Composable
- **Recomposition Impact:** Count and cost
- **Confidence:** High / Medium / Low
- **Current Code:** Pattern causing excess recomposition
- **Recommended Fix:** Optimized pattern
- **Verification:** How to confirm improvement

### 5. Prioritized Remediation Plan

Ordered by recomposition reduction impact.

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on Compose recomposition
- **ST-02** (Structured Sequential Instructions) — Systematic pattern-by-pattern analysis
- **RT-02** (Multi-Dimensional Analysis) — State, stability, callbacks, effects, granularity
- **RT-05** (Evidence-Based Reasoning) — Recomposition counts and compiler reports
- **DS-06** (Prioritization Guidance) — Ranked by recomposition cost reduction
- **QA-01** (Chain-of-Verification) — Verify with compiler metrics before reporting

---

## Related Prompts

- `android_compose_recomposition_review.md` — Comprehensive Compose performance review
- `android_state_propagation_review.md` — For upstream state issues feeding into recomposition
- `android_overbroad_ui_updates_review.md` — For broader update scope including Views
- `android_architectural_coarse_graining_review.md` — For architectural patterns causing broad recomposition
