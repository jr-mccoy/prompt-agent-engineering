---
title: "Android Per-Update Expensive Work Review"
category: mobile/android/targeted-reviews
description: "Android Per-Update Expensive Work Review."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - expensive
  - mobile
  - per
  - reviews
  - targeted
updated: "2026-03-19"
related_prompts: []
---

# Android Per-Update Expensive Work Review

---
title: "Android Per-Update Expensive Work Review"
category: mobile/android/performance
description: "Detect expensive per-update transformations that make every state change take longer than it should"
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
  - performance
  - transformations
  - mapping
  - formatting
  - diffing
  - ui-responsiveness
updated: "2026-03-09"
---

**Objective:** Analyze the Android codebase to identify places where each UI state update triggers work that is individually non-blocking but cumulatively expensive — sorting, filtering, formatting, model mapping, or diffing that runs on every emission and adds perceivable latency to every state change.

**When to Use:** Use when individual UI updates feel slightly delayed (not frozen), when scrolling through data feels "heavy," when typing or toggling produces a noticeable beat before the UI responds, or when profiling shows >5ms of transformation work per state emission. This is distinct from freezing — the app remains responsive but every action feels a beat too slow.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Confirm the work runs per-update** — Don't flag one-time setup or infrequent operations.
2. **Estimate actual cost** — A `.map { }` on 10 items is negligible. On 10,000 items, it matters.
3. **Check for existing caching** — Look for `remember`, `distinctUntilChanged`, memoization, or upstream deduplication.
4. **Verify it's on the critical path** — Background transformations that complete before the UI needs them are fine.
5. **Provide exact file:line locations.**

**Finding NO issues is an acceptable outcome.**

### False-Positive Prevention

- ❌ Do NOT flag transformations on small collections (<50 items) unless they involve I/O or heavy computation per item
- ❌ Do NOT flag one-time transformations (initialization, configuration loading)
- ❌ Do NOT flag transformations that run on background dispatchers and complete well before UI consumption
- ❌ Do NOT flag `DiffUtil` computation itself — it's necessary work; flag only if the input is unnecessarily large
- ❌ Do NOT flag simple property access or trivial mapping (e.g., `item.name` extraction)
- ✅ DO estimate collection size × per-item cost to gauge actual impact
- ✅ DO check whether the transformation result could be cached
- ✅ DO verify the transformation runs on the main thread (or blocks main thread waiting for result)
- ✅ DO distinguish between "runs every emission" and "runs every frame"

---

### 1. Sorting and Filtering on Every Emission

Identify lists being sorted or filtered on each state update:

* **Sort in reactive chain:**
  - `flow.map { items -> items.sortedBy { it.date } }` — re-sorts on every emission even if sort order hasn't changed
  - Sorting inside `onBindViewHolder` or composable function

* **Filter without caching:**
  - `items.filter { it.isActive }` on every recomposition/bind
  - Chained filter+sort+map on large lists per update

**Best Practices:**
```kotlin
// ❌ BAD: Sorts 5000 items on every emission
val sortedItems: StateFlow<List<Item>> = itemsFlow
    .map { items -> items.sortedByDescending { it.createdAt } }
    .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), emptyList())

// ✅ GOOD: Only re-sort when items or sort order actually change
private val _sortOrder = MutableStateFlow(SortOrder.DATE_DESC)

val sortedItems: StateFlow<List<Item>> = combine(
    itemsFlow.distinctUntilChanged(),
    _sortOrder
) { items, order ->
    items.sortedWith(order.comparator)
}.stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), emptyList())

// ✅ BETTER: Pre-sort in repository/data layer
class ItemRepository {
    fun getItems(sortOrder: SortOrder): Flow<List<Item>> =
        dao.getItemsSorted(sortOrder.toSqlOrderBy()) // DB does the sorting
}
```

**Suggested Fixes:**
- Push sorting to the database query (SQL `ORDER BY`) when possible
- Use `distinctUntilChanged()` before expensive transformations
- Only re-sort when sort criteria or item content changes, not on every emission
- For in-memory sorting, cache the sorted result and invalidate only on actual data change

---

### 2. UI Model Mapping on Every Emission

Identify domain-to-presentation model mapping that runs too frequently:

* **Full list re-mapping:**
  - `items.map { it.toUiModel() }` on every flow emission
  - `toUiModel()` involves formatting, calculation, or resource lookup

* **Nested mapping:**
  - Mapping parent objects that recursively map child collections
  - Re-creating entire UI model trees for single-field changes

**Best Practices:**
```kotlin
// ❌ BAD: Maps entire list on every emission
val uiItems: StateFlow<List<ItemUiModel>> = itemsFlow
    .map { items ->
        items.map { item ->
            ItemUiModel(
                id = item.id,
                title = item.title,
                subtitle = formatDate(item.date), // expensive!
                priceLabel = formatCurrency(item.price), // expensive!
                distanceLabel = calculateDistance(item.location, userLocation), // expensive!
                thumbnail = resolveThumbnailUrl(item.images) // I/O-ish
            )
        }
    }
    .stateIn(...)

// ✅ GOOD: Incremental mapping — only map changed items
val uiItems: StateFlow<List<ItemUiModel>> = itemsFlow
    .scan(emptyMap<String, ItemUiModel>()) { cache, items ->
        items.associate { item ->
            item.id to (cache[item.id]?.takeIf { it.sourceHash == item.hashCode() }
                ?: item.toUiModel())
        }
    }
    .map { it.values.toList() }
    .stateIn(...)

// ✅ ALSO GOOD: Map only when individual item changes
// Use DiffUtil / key-based caching so unchanged items keep their UI model
```

**Suggested Fixes:**
- Cache mapped UI models by item ID; only re-map items that actually changed
- Move expensive formatting to the data layer or a background transform
- Use `scan` operator to maintain incremental state
- For Compose: `remember(item)` inside `LazyColumn` items to cache per-item derived state

---

### 3. Repeated Date/Number/String Formatting

Identify formatting operations that recur on every update:

* **Formatter allocation per call:**
  - Creating `SimpleDateFormat`, `NumberFormat`, `DecimalFormat` instances inside bind/recompose
  - Locale-aware formatting on every frame

* **Repeated formatting of unchanged values:**
  - Same date formatted every recomposition because the composable recomposes for unrelated reasons
  - Price formatting on every list scroll

**Best Practices:**
```kotlin
// ❌ BAD: Allocates formatter every bind
override fun onBindViewHolder(holder: ViewHolder, position: Int) {
    val item = items[position]
    holder.date.text = SimpleDateFormat("MMM dd, yyyy", Locale.US).format(item.date)
    holder.price.text = NumberFormat.getCurrencyInstance(Locale.US).format(item.price)
}

// ✅ GOOD: Shared formatter instances
companion object {
    private val dateFormatter = SimpleDateFormat("MMM dd, yyyy", Locale.US)
    private val currencyFormatter = NumberFormat.getCurrencyInstance(Locale.US)
}

// ✅ BETTER: Pre-format in UI model
data class ItemUiModel(
    val id: String,
    val formattedDate: String,   // formatted once at mapping time
    val formattedPrice: String   // formatted once at mapping time
)

// ✅ BEST (Compose): Remember formatted values
@Composable
fun ItemCard(item: Item) {
    val formattedDate = remember(item.date) {
        dateFormatter.format(item.date)
    }
    val formattedPrice = remember(item.price) {
        currencyFormatter.format(item.price)
    }
    // ...
}
```

**Suggested Fixes:**
- Reuse formatter instances (store as companion object or inject)
- Pre-format strings during domain → UI model mapping
- In Compose, use `remember(key)` for formatted values
- In Views, format in the UI model or use `onBindViewHolder` with payloads to avoid re-formatting unchanged fields

---

### 4. Repeated Collection Diffing

Identify cases where large collections are diffed more often than necessary:

* **DiffUtil on every emission:**
  - `submitList()` called on every flow emission even when the list hasn't changed
  - Large lists diffed for single-item changes when insert/remove position is known

* **Custom diffing in reactive chains:**
  - Manual diff computation in `map` or `combine` operators
  - Rebuilding entire adapter data on every state emission

**Best Practices:**
```kotlin
// ❌ BAD: Submits full list on every emission even when nothing changed
viewModel.items.collect { items ->
    adapter.submitList(items) // DiffUtil runs even if list is identical
}

// ✅ GOOD: Only submit when list actually changes
viewModel.items
    .distinctUntilChanged() // reference equality check first
    .collect { items ->
        adapter.submitList(items)
    }

// ✅ BETTER: If you know the change type, use targeted updates
sealed class ListUpdate {
    data class FullList(val items: List<Item>) : ListUpdate()
    data class ItemInserted(val item: Item, val position: Int) : ListUpdate()
    data class ItemRemoved(val position: Int) : ListUpdate()
    data class ItemChanged(val item: Item, val position: Int) : ListUpdate()
}
```

**Suggested Fixes:**
- Use `distinctUntilChanged()` before `submitList` to skip no-op diffs
- For known single-item changes, use `notifyItemInserted/Removed/Changed` directly
- Ensure `DiffUtil.ItemCallback.areContentsTheSame` is efficient (no deep object comparison)
- Consider `AsyncListDiffer` for background diffing on large lists

---

### 5. Heavy ViewModel Transformations

Identify ViewModels performing expensive work on every state composition:

* **`combine` with expensive transforms:**
  - Multiple flows combined with an expensive mapping function
  - The transform runs every time ANY input flow emits

* **Redundant re-computation:**
  - Derived state recomputed even when the relevant inputs haven't changed
  - Missing `distinctUntilChanged` between expensive stages

**Best Practices:**
```kotlin
// ❌ BAD: Expensive combine runs on every emission from ANY source
val screenState = combine(
    userFlow,
    itemsFlow,
    settingsFlow,
    analyticsFlow
) { user, items, settings, analytics ->
    // ALL of this runs when analytics emits (every 5 seconds!)
    val filtered = items.filter { matchesSettings(it, settings) }
    val sorted = filtered.sortedWith(settings.sortComparator)
    val mapped = sorted.map { it.toUiModel(user) }
    ScreenState(user.toHeader(), mapped, analytics.toSummary())
}

// ✅ GOOD: Isolate expensive transforms to their actual dependencies
private val filteredItems = combine(itemsFlow, settingsFlow) { items, settings ->
    items.filter { matchesSettings(it, settings) }
        .sortedWith(settings.sortComparator)
}.distinctUntilChanged()

private val uiItems = combine(filteredItems, userFlow) { items, user ->
    items.map { it.toUiModel(user) }
}.distinctUntilChanged()

val screenState = combine(uiItems, analyticsFlow) { items, analytics ->
    ScreenState(items = items, analytics = analytics.toSummary())
}
```

**Suggested Fixes:**
- Break `combine` chains into stages, each with `distinctUntilChanged`
- Isolate expensive transforms so they only re-run when their specific inputs change
- Use `stateIn` with appropriate sharing to avoid redundant upstream computation
- Profile `combine` lambdas to identify which part is actually expensive

---

## Expected Output

Provide a per-update cost analysis report including:

### 1. Executive Summary
- Per-update efficiency rating
- Total estimated per-emission overhead (ms)
- Critical expensive operations count

### 2. Cost Hotspots

| Operation | Location | Runs Per | Collection Size | Est. Cost | Priority |
|-----------|----------|----------|-----------------|-----------|----------|
| [Sort/Filter/Map] | [file:line] | [emission/recomp] | [N items] | [ms] | [Level] |

### 3. Detailed Findings

For each issue:
- **Location:** file:line
- **Category:** Sort/Filter / Model Mapping / Formatting / Diffing / ViewModel Transform
- **Frequency:** How often this runs
- **Cost Estimate:** Approximate time per execution
- **Confidence:** High / Medium / Low
- **Current Code:** Expensive pattern with explanation
- **Recommended Fix:** Optimized approach with code
- **Verification:** How to measure improvement

### 4. Prioritized Remediation Plan

Ordered by per-update time savings.

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on per-update cost
- **ST-02** (Structured Sequential Instructions) — Category-by-category analysis
- **RT-02** (Multi-Dimensional Analysis) — Sort, map, format, diff, transform
- **RT-05** (Evidence-Based Reasoning) — Cost estimates with collection sizes
- **DS-06** (Prioritization Guidance) — Ranked by time saved per update
- **QA-01** (Chain-of-Verification) — Verify cost before flagging

---

## Related Prompts

- `android_state_propagation_review.md` — For upstream state delivery issues
- `android_overbroad_ui_updates_review.md` — For update scope issues
- `android_list_rendering_inefficiency_review.md` — For list-specific costs
- `performance_code_optimization_suggestions.md` — For general optimization strategies
