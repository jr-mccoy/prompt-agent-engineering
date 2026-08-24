---
title: "Android Architectural Coarse-Graining Review"
category: mobile/android/targeted-reviews
description: "Android Architectural Coarse-Graining Review."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - architectural
  - coarse
  - graining
  - mobile
  - reviews
updated: "2026-03-19"
related_prompts: []
---

# Android Architectural Coarse-Graining Review

---
title: "Android Architectural Coarse-Graining Review"
category: mobile/android/performance
description: "Detect architectural patterns where small user actions trigger disproportionately large state rebuilds, causing the app to feel behind without freezing"
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
  - architecture
  - mvi
  - state-management
  - performance
  - ui-responsiveness
  - monolithic-state
  - screen-state
updated: "2026-03-09"
---

**Objective:** Analyze the Android codebase to identify architectural coarse-graining — patterns where a small user action (toggling a checkbox, expanding a section, typing a character) triggers a disproportionately large chain reaction: full screen-state rebuild → full list rebuild → broad recomposition or rebinding. Nothing freezes, but the whole app feels a beat behind because every tiny change cascades through a monolithic state pipeline.

**When to Use:** Use when the app has a clean architecture (MVI, MVVM, UDF) but still feels sluggish. Common in MVI implementations where the state object is too monolithic, in apps where every ViewModel action produces a full new state, or when small user gestures (checkbox, expand/collapse, swipe) produce a visible beat of delay. This is especially prevalent in well-architected apps that accidentally over-unified their state management.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace from user action to final UI update** — Map the full cascade: Action → Reducer/ViewModel → State emission → UI consumption.
2. **Confirm the state rebuild is disproportionate** — A checkbox toggle should not rebuild an entire screen state object with 15 fields.
3. **Verify the coarse-graining causes visible delay** — If the rebuild is fast enough (<8ms total), it's not a real problem regardless of architecture.
4. **Provide exact file:line locations.**

**Finding NO issues is an acceptable outcome.** A monolithic state pattern that is fast enough is fine.

### False-Positive Prevention

- ❌ Do NOT flag monolithic state that reconstructs in <5ms — it's architecturally impure but not a performance issue
- ❌ Do NOT flag MVI reducers as inherently problematic — the pattern is fine when state is appropriately scoped
- ❌ Do NOT flag `copy()` on data classes as expensive — it's O(1) for flat data classes
- ❌ Do NOT flag unified state for simple screens with <5 fields
- ❌ Do NOT recommend splitting state purely for architectural purity — only for measurable performance improvement
- ✅ DO measure or estimate the cascade cost: state rebuild + list rebuild + recomposition/rebind
- ✅ DO check if Compose's skip optimization already handles the coarse state efficiently
- ✅ DO verify that list items actually recompose/rebind due to the state change
- ✅ DO consider the action frequency — coarse state for rare actions (settings toggle) is fine; for frequent actions (typing, scrolling) it's not

---

### 1. Monolithic Screen State Objects

Identify state objects that bundle unrelated concerns:

* **Too many fields with different update frequencies:**
  - A single `data class ScreenState` with 10-20 fields ranging from "changes every keystroke" to "changes once per session"
  - Every emission creates a new state object even though most fields are unchanged

* **Heterogeneous concerns in one class:**
  - User profile + feed items + notification count + search query + filter settings all in one state
  - A change to any field triggers observation of the entire bundle

* **Nested state objects that rebuild entirely:**
  - `ScreenState(header = Header(...), content = Content(...), footer = Footer(...))`
  - A footer change forces re-emission of the entire tree

**Best Practices:**
```kotlin
// ❌ BAD: Monolithic state — checkbox toggle rebuilds everything
data class DashboardState(
    // User section (changes rarely)
    val userName: String = "",
    val userAvatar: String = "",

    // Feed section (changes on refresh)
    val feedItems: List<FeedItem> = emptyList(),
    val isRefreshing: Boolean = false,

    // Filters (changes on user interaction)
    val selectedCategory: Category = Category.ALL,
    val searchQuery: String = "",           // changes every keystroke!

    // Notifications (changes on push)
    val unreadCount: Int = 0,

    // Settings (changes rarely)
    val isDarkMode: Boolean = false,
    val isCompactLayout: Boolean = false,

    // Selection (changes on every tap)
    val selectedItemIds: Set<String> = emptySet()  // changes frequently!
)

// Every state emission rebuilds ALL of this, observed by ALL UI sections

// ✅ GOOD: Split by concern and update frequency
@HiltViewModel
class DashboardViewModel : ViewModel() {
    // Slow-changing user data
    val userProfile: StateFlow<UserProfile> = ...

    // Feed with its own refresh state
    val feedState: StateFlow<FeedState> = ...

    // Fast-changing search/filter
    val searchQuery: StateFlow<String> = MutableStateFlow("")
    val selectedCategory: StateFlow<Category> = MutableStateFlow(Category.ALL)

    // Fast-changing selection
    val selectedItemIds: StateFlow<Set<String>> = MutableStateFlow(emptySet())

    // Derived: filtered feed (only recalculates when inputs change)
    val filteredFeed: StateFlow<List<FeedItem>> = combine(
        feedState.map { it.items },
        searchQuery.debounce(300),
        selectedCategory
    ) { items, query, category ->
        items.filter { matchesQuery(it, query) && matchesCategory(it, category) }
    }.stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), emptyList())
}
```

**Suggested Fixes:**
- Split state by update frequency: rarely-changing, user-action-driven, high-frequency
- Expose separate `StateFlow`s for independent UI sections
- Use `combine` only for flows that genuinely need to be combined
- Keep the total field count per state class to ≤5-7 for high-frequency states
- For MVI purists: use multiple "sub-states" composed in the UI layer, not in one reducer

---

### 2. Over-Unified Reducers

Identify MVI/Redux-style reducers where every action passes through one function:

* **Single reducer for all screen actions:**
  - One `reduce(state, action)` function handling 20+ action types
  - Every action produces a full new `ScreenState` even for tiny changes

* **Action → State → Side Effect coupling:**
  - Actions that only trigger side effects still produce a new state emission
  - Navigation events, analytics events mixed with state updates

* **State machine transitions that are too broad:**
  - `Loading → Content → Error` transitions that reset unrelated state
  - Tab switching that rebuilds the entire screen state

**Best Practices:**
```kotlin
// ❌ BAD: One reducer, every action rebuilds full state
fun reduce(state: ScreenState, action: Action): ScreenState = when (action) {
    is Action.ToggleItem -> state.copy(
        selectedIds = state.selectedIds.toggle(action.id)
        // This also re-emits userName, feedItems, searchQuery, etc.!
    )
    is Action.UpdateSearch -> state.copy(
        searchQuery = action.query
        // This also re-emits selectedIds, feedItems, etc.!
    )
    is Action.RefreshFeed -> state.copy(
        isRefreshing = true
        // This also re-emits searchQuery, selectedIds, etc.!
    )
    // 15 more actions...
}

// ✅ GOOD: Scoped state updates
class DashboardViewModel : ViewModel() {
    fun toggleItem(id: String) {
        _selectedIds.update { it.toggle(id) }
        // ONLY selectedIds observers are notified
    }

    fun updateSearch(query: String) {
        _searchQuery.value = query
        // ONLY search-related observers are notified
    }

    fun refreshFeed() {
        _feedState.update { it.copy(isRefreshing = true) }
        viewModelScope.launch { /* fetch */ }
    }
}
```

**Suggested Fixes:**
- Break one mega-reducer into scoped state updaters
- Separate commands (side effects) from state updates — use `Channel` or `SharedFlow` for one-shot events
- If using a state machine, ensure transitions only modify relevant fields
- Consider the "multiple state holders" pattern: one per independent UI section

---

### 3. Full List Rebuild on Non-List State Changes

Identify patterns where changing non-list state triggers list reconstruction:

* **List derived from screen state:**
  - `screenState.map { it.toListItems() }` — re-maps entire list on ANY state field change
  - Even toggling a toolbar option reconstructs the list model

* **List items include screen-level state:**
  - Each `ListItemModel` includes `isEditMode`, `selectedCategory`, or other screen-level flags
  - Changing any flag forces re-creation of ALL list items

**Best Practices:**
```kotlin
// ❌ BAD: List model includes screen-level state
data class ItemUiModel(
    val id: String,
    val title: String,
    val isSelected: Boolean,      // from screen selection state
    val isEditMode: Boolean,      // from screen edit mode
    val showCategory: Boolean,    // from screen display settings
)

// Every time edit mode or display settings change, ALL items are rebuilt

// ✅ GOOD: Separate item data from screen-level display state
data class ItemUiModel(
    val id: String,
    val title: String,
)

@Composable
fun ItemRow(
    item: ItemUiModel,
    isSelected: Boolean,   // passed as separate parameter
    isEditMode: Boolean,   // passed as separate parameter
) {
    // ...
}

// In LazyColumn:
items(items, key = { it.id }) { item ->
    // These derivations don't cause item list rebuild
    val isSelected = remember(selectedIds, item.id) { item.id in selectedIds }
    ItemRow(item = item, isSelected = isSelected, isEditMode = isEditMode)
}
```

**Suggested Fixes:**
- Keep list item models containing only item-specific data
- Pass screen-level state (edit mode, selection, display options) as separate parameters
- In Compose, derive per-item booleans inside the `items {}` lambda
- In RecyclerView, use `payloads` in DiffUtil to handle selection/mode changes without full rebind
- Use `distinctUntilChanged` on the list flow to prevent re-emission when only non-list state changes

---

### 4. Cascade Amplification

Identify where a small state change amplifies through multiple layers:

* **Action → Reducer → Repository → Database → Flow → Transform → UI:**
  - A checkbox toggle traverses the entire persistence layer before reflecting in UI
  - Each layer adds its own processing overhead

* **Event propagation through multiple ViewModels:**
  - Shared state updated in one ViewModel, observed by others, each producing new state
  - N ViewModels each rebuilding state for one change

* **State normalization overhead:**
  - Flat/normalized state store requiring denormalization on every change
  - Join operations run on every mutation, not just when join inputs change

**Best Practices:**
```kotlin
// ❌ BAD: Toggle propagates through entire stack
// UI: onClick → ViewModel: toggleFavorite() → Repository: updateFavorite()
//   → DAO: update() → Room invalidation → DAO: query() → Repository: transform()
//   → ViewModel: map() → UI: recompose/rebind
// Total: 6 layer crossings for a single toggle

// ✅ GOOD: Optimistic update with background sync
// UI: onClick → ViewModel: toggleFavorite() → _uiState.update { toggle } → UI: recompose
// Background: → Repository: updateFavorite() → DAO: update()
// Total: 2 layer crossings for immediate feedback; 4 for persistence (non-blocking)
```

**Suggested Fixes:**
- Implement optimistic updates for interactive state (see `android_async_boundaries_review.md`)
- Use local state for UI-only concerns (expanded/collapsed, selection, hover)
- Don't persist ephemeral UI state (selection, scroll position) unless required
- For shared state, use a dedicated state holder rather than propagating through multiple ViewModels
- Batch multiple rapid changes (e.g., multi-select) into single state emissions

---

### 5. Screen-Level Recomposition/Rebind From Coarse State

Identify where the architectural state granularity directly causes broad UI updates:

* **Compose: Screen reads one state, all sections recompose:**
  - `val state by viewModel.state.collectAsStateWithLifecycle()` at screen level
  - All child composables receive state-derived parameters, none can skip

* **Views: Single observer, full rebind:**
  - One `LiveData<ScreenState>` observer that calls `bindScreen(state)`
  - `bindScreen` touches every view, even unchanged ones

**Best Practices:**
```kotlin
// ❌ BAD (Views): One observer rebinds everything
viewModel.screenState.observe(viewLifecycleOwner) { state ->
    binding.userName.text = state.userName
    binding.feedRecyclerView.adapter.submitList(state.feedItems)
    binding.searchBar.setText(state.searchQuery)
    binding.notificationBadge.text = "${state.unreadCount}"
    // ALL views updated on EVERY emission
}

// ✅ GOOD (Views): Scoped observers
viewModel.userProfile.observe(viewLifecycleOwner) { profile ->
    binding.userName.text = profile.name
}
viewModel.feedItems.observe(viewLifecycleOwner) { items ->
    feedAdapter.submitList(items)
}
viewModel.unreadCount.observe(viewLifecycleOwner) { count ->
    binding.notificationBadge.text = "$count"
}

// ❌ BAD (Compose): One state read at top
@Composable
fun DashboardScreen(viewModel: DashboardViewModel) {
    val state by viewModel.state.collectAsStateWithLifecycle()
    Column {
        UserHeader(state.userName, state.avatar)
        FeedList(state.feedItems)
        SearchBar(state.searchQuery)
    }
}

// ✅ GOOD (Compose): Granular collection
@Composable
fun DashboardScreen(viewModel: DashboardViewModel) {
    Column {
        val profile by viewModel.userProfile.collectAsStateWithLifecycle()
        UserHeader(profile)

        val feedItems by viewModel.feedItems.collectAsStateWithLifecycle()
        FeedList(feedItems)

        val query by viewModel.searchQuery.collectAsStateWithLifecycle()
        SearchBar(query, onQueryChange = viewModel::updateSearch)
    }
}
```

**Suggested Fixes:**
- Split state observation to match UI section boundaries
- Each UI section should observe only what it needs
- In Compose, collect separate flows in or near the composables that use them
- In Views, use multiple observers on scoped `LiveData`/`StateFlow`
- For MVI architectures, use state selectors or `distinctUntilChangedBy` to scope observations

---

## Expected Output

Provide an architectural coarse-graining analysis report including:

### 1. Executive Summary
- Architectural efficiency rating
- State granularity assessment
- Cascade depth for common user actions

### 2. Action-to-UI Cascade Map

| User Action | State Fields Changed | State Fields Re-Emitted | UI Sections Notified | UI Sections Actually Changed | Priority |
|-------------|---------------------|------------------------|---------------------|------------------------------|----------|
| [Toggle checkbox] | [1 field] | [15 fields] | [All] | [1 section] | [Level] |

### 3. State Object Analysis

| State Class | Field Count | Update Frequencies | Observation Points | Recommendation |
|-------------|-------------|-------------------|-------------------|----------------|
| [ScreenState] | [N] | [mixed/uniform] | [N observers] | [Split/Keep] |

### 4. Detailed Findings

For each issue:
- **Location:** file:line
- **Category:** Monolithic State / Over-Unified Reducer / Full List Rebuild / Cascade Amplification / Broad Observation
- **User action:** What triggers the cascade
- **Cascade path:** Action → State → UI with annotations
- **Wasted work:** What recomputes/redraws unnecessarily
- **Confidence:** High / Medium / Low
- **Current Architecture:** State flow diagram
- **Recommended Architecture:** Scoped state flow diagram
- **Migration Strategy:** How to incrementally refactor

### 5. Prioritized Remediation Plan

Ordered by cascade reduction × action frequency.

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on architectural cascade analysis
- **ST-02** (Structured Sequential Instructions) — Layer-by-layer analysis
- **RT-02** (Multi-Dimensional Analysis) — State objects, reducers, lists, cascades, observation
- **RT-05** (Evidence-Based Reasoning) — Field count × change frequency analysis
- **DS-06** (Prioritization Guidance) — Ranked by wasted work × action frequency
- **QA-01** (Chain-of-Verification) — Verify cascade cost before recommending refactor

---

## Related Prompts

- `android_state_propagation_review.md` — For state delivery issues within the cascade
- `android_overbroad_ui_updates_review.md` — For the UI side of the cascade
- `android_compose_recomposition_problems_review.md` — For Compose-specific cascade effects
- `android_async_boundaries_review.md` — For optimistic update patterns to short-circuit cascades
- `android_per_update_expensive_work_review.md` — For transformation costs within the cascade
