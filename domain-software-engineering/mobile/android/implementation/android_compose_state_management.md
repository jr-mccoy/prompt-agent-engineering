---
title: "Android Compose State Management"
category: mobile-development
description: "Deep dive into Compose state management patterns — when to use remember, rememberSaveable, ViewModels, collectAsStateWithLifecycle, and state hoisting for complex UIs"
techniques:
  - ST-01
  - ST-02
  - RT-01
  - RT-02
  - ED-05
difficulty: intermediate
tags:
  - android
  - jetpack-compose
  - state-management
  - viewmodel
  - mobile-development
updated: "2026-02-12"
---

# Android Compose State Management

**Objective:** Provide a comprehensive guide to Compose state management patterns — clarifying when to use `remember`, `rememberSaveable`, ViewModels with `StateFlow`, `collectAsStateWithLifecycle`, state hoisting, and derived state — with decision trees, code examples, and common anti-patterns to avoid, enabling correct state management in complex production UIs.

**When to Use:** Use this prompt when building complex Compose UIs that need to handle state correctly through configuration changes, process death, and recomposition. Essential when your team is adopting Compose and needs clear state management guidelines, when debugging state-related bugs (state loss, stale data, unnecessary recomposition), or when reviewing Compose code for state management correctness.

**Important context:** State management is the most common source of bugs in Compose applications. The framework provides multiple tools (`remember`, `rememberSaveable`, `ViewModel`, `StateFlow`) and the right choice depends on the state's lifecycle, scope, and persistence needs. Getting this wrong leads to state loss on rotation, stale UI after process death, unnecessary recomposition, and subtle race conditions.

---

## State Management Decision Tree

```
What kind of state is it?
│
├── UI-only state (animation, scroll position, expanded/collapsed)?
│   ├── Survives recomposition only? → remember { }
│   └── Survives configuration change? → rememberSaveable { }
│
├── Screen-level state (form data, selected tab, filter state)?
│   ├── Simple value (String, Int, Boolean)? → rememberSaveable { }
│   └── Complex object (list, custom class)?
│       ├── Serializable/Parcelable? → rememberSaveable { } with Saver
│       └── Not serializable? → ViewModel + StateFlow
│
├── Business logic state (user data, API responses, computed data)?
│   └── Always → ViewModel + StateFlow + collectAsStateWithLifecycle()
│
└── Shared state (used across multiple screens)?
    └── Always → ViewModel (scoped to NavGraph or Activity) + StateFlow
```

---

## Instructions

### Pattern 1: `remember` — Recomposition-Scoped State

**Use when:** State is purely UI-local and can be recreated after configuration change.

```kotlin
@Composable
fun AnimatedCard() {
    // Lost on configuration change — OK for transient animation state
    val expanded = remember { mutableStateOf(false) }
    val rotation by animateFloatAsState(if (expanded.value) 180f else 0f)

    Card(
        modifier = Modifier.clickable { expanded.value = !expanded.value }
    ) {
        Icon(
            imageVector = Icons.Default.ExpandMore,
            modifier = Modifier.rotate(rotation)
        )
    }
}
```

**Correct uses:** Animation state, derived values from parameters, memoized calculations.

**Anti-pattern — don't use for form data:**
```kotlin
// BAD: User types in a form, rotates device, text is gone
val name = remember { mutableStateOf("") }

// GOOD: Survives configuration change
val name = rememberSaveable { mutableStateOf("") }
```

### Pattern 2: `rememberSaveable` — Configuration-Change-Surviving State

**Use when:** State should survive configuration changes (rotation, dark mode toggle) and process death.

```kotlin
@Composable
fun FilterBar() {
    // Survives rotation and process death
    var selectedCategory by rememberSaveable { mutableStateOf("All") }
    var sortOrder by rememberSaveable { mutableStateOf("Recent") }

    Row {
        CategoryChip(selectedCategory) { selectedCategory = it }
        SortChip(sortOrder) { sortOrder = it }
    }
}
```

**For complex objects, use a custom Saver:**

```kotlin
data class FilterState(
    val category: String,
    val sortOrder: String,
    val priceRange: IntRange
)

val FilterStateSaver = run {
    val categoryKey = "category"
    val sortKey = "sort"
    val minKey = "min"
    val maxKey = "max"
    mapSaver(
        save = { mapOf(categoryKey to it.category, sortKey to it.sortOrder, minKey to it.priceRange.first, maxKey to it.priceRange.last) },
        restore = { FilterState(it[categoryKey] as String, it[sortKey] as String, (it[minKey] as Int)..(it[maxKey] as Int)) }
    )
}

@Composable
fun FilterScreen() {
    var filterState by rememberSaveable(stateSaver = FilterStateSaver) {
        mutableStateOf(FilterState("All", "Recent", 0..100))
    }
}
```

### Pattern 3: ViewModel + StateFlow — Business Logic State

**Use when:** State involves business logic, API calls, database queries, or is shared across Composables.

```kotlin
// ViewModel
@HiltViewModel
class HomeViewModel @Inject constructor(
    private val getItemsUseCase: GetItemsUseCase,
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {

    // UI state as a single sealed/data class
    private val _uiState = MutableStateFlow<HomeUiState>(HomeUiState.Loading)
    val uiState: StateFlow<HomeUiState> = _uiState.asStateFlow()

    // Search query survives process death via SavedStateHandle
    val searchQuery = savedStateHandle.getStateFlow("search", "")

    init {
        loadItems()
    }

    fun onSearchQueryChanged(query: String) {
        savedStateHandle["search"] = query
        loadItems(query)
    }

    private fun loadItems(query: String = searchQuery.value) {
        viewModelScope.launch {
            _uiState.value = HomeUiState.Loading
            getItemsUseCase(query)
                .onSuccess { items -> _uiState.value = HomeUiState.Success(items) }
                .onFailure { error -> _uiState.value = HomeUiState.Error(error.message) }
        }
    }
}

sealed interface HomeUiState {
    data object Loading : HomeUiState
    data class Success(val items: List<Item>) : HomeUiState
    data class Error(val message: String?) : HomeUiState
}
```

**In the Composable:**

```kotlin
@Composable
fun HomeScreen(
    viewModel: HomeViewModel = hiltViewModel()
) {
    // CRITICAL: Use collectAsStateWithLifecycle, NOT collectAsState
    // This respects the lifecycle — stops collecting when the app is backgrounded
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    val searchQuery by viewModel.searchQuery.collectAsStateWithLifecycle()

    HomeContent(
        uiState = uiState,
        searchQuery = searchQuery,
        onSearchQueryChanged = viewModel::onSearchQueryChanged
    )
}
```

### Pattern 4: State Hoisting

**Rule:** Composables that display state should not own state. Hoist state to the caller.

```kotlin
// BAD: TextField owns its state — can't be controlled externally
@Composable
fun SearchBar() {
    var text by remember { mutableStateOf("") }
    TextField(value = text, onValueChange = { text = it })
}

// GOOD: State is hoisted — caller controls the state
@Composable
fun SearchBar(
    query: String,
    onQueryChanged: (String) -> Unit,
    modifier: Modifier = Modifier
) {
    TextField(
        value = query,
        onValueChange = onQueryChanged,
        modifier = modifier
    )
}

// Usage
@Composable
fun HomeScreen(viewModel: HomeViewModel = hiltViewModel()) {
    val query by viewModel.searchQuery.collectAsStateWithLifecycle()
    SearchBar(
        query = query,
        onQueryChanged = viewModel::onSearchQueryChanged
    )
}
```

### Pattern 5: Derived State

**Use `derivedStateOf` when:** A value is computed from other state and should only trigger recomposition when the derived value changes (not every time the source changes).

```kotlin
@Composable
fun ItemList(items: List<Item>) {
    val listState = rememberLazyListState()

    // Only recomposes when the boolean value changes, not on every scroll pixel
    val showScrollToTop by remember {
        derivedStateOf { listState.firstVisibleItemIndex > 5 }
    }

    Box {
        LazyColumn(state = listState) {
            items(items) { item -> ItemRow(item) }
        }
        if (showScrollToTop) {
            ScrollToTopButton(onClick = { /* scroll to top */ })
        }
    }
}
```

### Pattern 6: State Holder Classes

**Use when:** A screen has complex state logic that doesn't need ViewModel's lifecycle awareness.

```kotlin
// State holder — plain class, not a ViewModel
class DrawerState(
    initialOpen: Boolean = false
) {
    var isOpen by mutableStateOf(initialOpen)
        private set

    fun open() { isOpen = true }
    fun close() { isOpen = false }
    fun toggle() { isOpen = !isOpen }
}

@Composable
fun rememberDrawerState(initialOpen: Boolean = false): DrawerState {
    return remember { DrawerState(initialOpen) }
}

// Usage
@Composable
fun MainScreen() {
    val drawerState = rememberDrawerState()
    // ...
}
```

---

## Common Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| `collectAsState()` instead of `collectAsStateWithLifecycle()` | Keeps collecting when app is backgrounded — wastes resources, can crash | Always use `collectAsStateWithLifecycle()` |
| Storing list data in `rememberSaveable` | Large lists exceed `Bundle` size limit (1MB) — causes `TransactionTooLargeException` | Use ViewModel + StateFlow for list data |
| ViewModel in nested Composables | Creates new ViewModel instance per recomposition | Hoist ViewModel access to screen-level Composable |
| Mutable state in ViewModel exposed directly | Allows UI to modify state directly, bypassing business logic | Expose `StateFlow` (immutable), keep `MutableStateFlow` private |
| `remember { mutableStateListOf() }` for API data | Lost on configuration change, no process death survival | Use ViewModel + StateFlow for API data |
| `LaunchedEffect(Unit)` to load data | Runs on every recomposition if not careful, no lifecycle awareness | Load data in ViewModel `init` or explicit trigger |

---

## Expected Output

When reviewing or implementing state management:

1. **State Audit** — classify every piece of state in the screen by lifecycle (recomposition, config change, process death, permanent)
2. **State Holder Selection** — for each state, determine the correct mechanism (`remember`, `rememberSaveable`, ViewModel, etc.)
3. **Hoisting Plan** — identify which Composables should own vs. receive state
4. **Anti-Pattern Check** — flag any state management anti-patterns found in existing code
5. **Migration Steps** — if fixing existing code, ordered steps to migrate state management correctly

---

## CRITICAL: Verification Requirements

- [ ] No `collectAsState()` — always `collectAsStateWithLifecycle()`
- [ ] Form data survives rotation (use `rememberSaveable` or ViewModel + SavedStateHandle)
- [ ] Business data survives process death (use ViewModel + SavedStateHandle or repository)
- [ ] No mutable state exposed from ViewModel (only `StateFlow`, never `MutableStateFlow`)
- [ ] State hoisting applied — stateless Composables receive state as parameters
- [ ] `derivedStateOf` used where computed state could cause excessive recomposition
- [ ] LazyColumn items use stable keys (not index) to prevent unnecessary recomposition
