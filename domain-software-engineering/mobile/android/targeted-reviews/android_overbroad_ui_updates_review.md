---
title: "Android Over-Broad UI Updates Review"
category: mobile/android/targeted-reviews
description: "Android Over-Broad UI Updates Review."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - mobile
  - overbroad
  - reviews
  - targeted
  - updates
updated: "2026-03-19"
related_prompts: []
---

# Android Over-Broad UI Updates Review

---
title: "Android Over-Broad UI Updates Review"
category: mobile/android/performance
description: "Detect UI updates that recompute or redraw far more than necessary, causing sluggishness without freezing"
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
  - compose
  - recomposition
  - recyclerview
  - performance
  - ui-responsiveness
  - rendering
updated: "2026-03-09"
---

**Objective:** Analyze the Android codebase to identify places where the UI framework recomputes or redraws far more than the actual data change warrants — causing sluggishness, visual lag, or "mushiness" without outright freezing.

**When to Use:** Use when the app feels sluggish or laggy (but never ANRs), when small state changes cause visible full-screen redraws, when scrolling feels rough but not frozen, or when profiling shows high recomposition counts or excessive `onBindViewHolder` calls. This is the #2 most common cause of perceived slowness without freezing.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Confirm the scope of the redraw** — Don't guess. Trace from the state change to every composable/view that actually re-executes.
2. **Check for existing mitigations** — Look for `remember`, `derivedStateOf`, `DiffUtil`, `key {}`, `@Stable`, etc.
3. **Verify actual user impact** — A composable recomposing 3 times during a gesture is fine if it's cheap. Focus on cases that produce visible lag.
4. **Provide exact file:line locations.**

**Finding NO issues is an acceptable outcome.**

### False-Positive Prevention

- ❌ Do NOT flag recomposition of small/cheap composables — recomposing a `Text()` is nearly free
- ❌ Do NOT flag `notifyDataSetChanged()` on lists of <20 items — the cost is negligible at small scale
- ❌ Do NOT flag broad recomposition that completes within a single frame (<16ms total)
- ❌ Do NOT flag intentional full-screen transitions (navigation, theme changes)
- ❌ Do NOT assume `notifyDataSetChanged` is wrong without checking if `DiffUtil` is impractical for the data type
- ✅ DO measure or estimate the actual cost of the over-broad update
- ✅ DO check Compose compiler stability reports before claiming instability
- ✅ DO verify RecyclerView bind cost before flagging rebinding patterns
- ✅ DO distinguish between "recomposes often" and "recomposes expensively"

---

### 1. Compose: State Read Placement

Identify state reads that are too high in the composition tree:

* **Screen-level state reads:**
  - A single `val uiState by viewModel.uiState.collectAsStateWithLifecycle()` at the top of a screen composable forces recomposition of the entire screen on any field change
  - Rapidly changing fields (timers, counters, progress) in a monolithic state object

* **Shared state across unrelated subtrees:**
  - Multiple unrelated sections reading the same state object
  - A change to one field causes all sections to recompose

**Best Practices:**
```kotlin
// ❌ BAD: One state read controls entire screen
@Composable
fun ProfileScreen(viewModel: ProfileViewModel) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    Column {
        ProfileHeader(uiState.name, uiState.avatar)  // recomposes on unrelated changes
        StatsSection(uiState.stats)                    // recomposes on unrelated changes
        ActivityFeed(uiState.activities)               // recomposes on unrelated changes
        OnlineIndicator(uiState.isOnline)              // changes frequently!
    }
}

// ✅ GOOD: Granular state reads
@Composable
fun ProfileScreen(viewModel: ProfileViewModel) {
    Column {
        // Each section reads only what it needs
        val headerState by viewModel.headerState.collectAsStateWithLifecycle()
        ProfileHeader(headerState)

        val stats by viewModel.stats.collectAsStateWithLifecycle()
        StatsSection(stats)

        val activities by viewModel.activities.collectAsStateWithLifecycle()
        ActivityFeed(activities)

        val isOnline by viewModel.isOnline.collectAsStateWithLifecycle()
        OnlineIndicator(isOnline)
    }
}

// ✅ ALSO GOOD: Defer reads into child composables
@Composable
fun ProfileScreen(viewModel: ProfileViewModel) {
    Column {
        ProfileHeader(viewModel) // reads state internally
        StatsSection(viewModel)
        ActivityFeed(viewModel)
        OnlineIndicator(viewModel)
    }
}
```

**Suggested Fixes:**
- Split monolithic `UiState` into separate flows by update frequency
- Use `derivedStateOf` for computed values to reduce propagation scope
- Move state reads as deep into the tree as possible
- Use lambda-based state reading: `Modifier.offset { IntOffset(scrollState.value, 0) }` defers read to layout phase

---

### 2. Compose: Unstable Parameters

Identify parameters that prevent Compose from skipping recomposition:

* **Mutable collection types:**
  - `List<T>`, `Map<K,V>`, `Set<T>` — Compose treats these as unstable
  - Every call passes a "new" list even if content is identical

* **Recreated objects and lambdas:**
  - Data class instances created inline every composition
  - Lambdas that capture mutable references
  - `Modifier` chains built inline without `remember`

* **Non-data-class parameters:**
  - Classes without structural equality — Compose cannot determine skip-ability

**Best Practices:**
```kotlin
// ❌ BAD: Recreated list every recomposition
@Composable
fun TagBar(tags: List<String>) { ... } // List is unstable

// ✅ GOOD: Use immutable collections
@Composable
fun TagBar(tags: ImmutableList<String>) { ... } // Stable, skippable

// ❌ BAD: Recreated lambda captures
@Composable
fun Screen(viewModel: ScreenViewModel) {
    ItemList(
        onItemClick = { id -> viewModel.select(id) } // new lambda each time
    )
}

// ✅ GOOD: Stable lambda
@Composable
fun Screen(viewModel: ScreenViewModel) {
    val onItemClick = remember<(String) -> Unit> { { id -> viewModel.select(id) } }
    ItemList(onItemClick = onItemClick)
}
// OR use method reference if applicable:
ItemList(onItemClick = viewModel::select)
```

**Suggested Fixes:**
- Use `kotlinx-collections-immutable` (`ImmutableList`, `ImmutableMap`)
- Add `@Immutable` or `@Stable` annotations to state classes that qualify
- Remember lambdas that capture ViewModel or stable references
- Run Compose compiler metrics to identify unstable classes: `-P plugin:androidx.compose.compiler.plugins.kotlin:metricsDestination=...`

---

### 3. Compose: Missing `remember` / `derivedStateOf`

Identify expensive recomputations that repeat unnecessarily:

* **Unremembered computations:**
  - Sorting, filtering, or mapping collections on every recomposition
  - Formatting dates/numbers on every recomposition
  - Building `Modifier` chains with dynamic values without `remember`

* **Missing `derivedStateOf`:**
  - Computed values that change less often than their inputs
  - Boolean conditions derived from frequently changing numeric state

**Best Practices:**
```kotlin
// ❌ BAD: Filters on every recomposition
@Composable
fun SearchResults(items: List<Item>, query: String) {
    val filtered = items.filter { it.name.contains(query, ignoreCase = true) }
    // ...
}

// ✅ GOOD: Remembered with correct keys
@Composable
fun SearchResults(items: List<Item>, query: String) {
    val filtered = remember(items, query) {
        items.filter { it.name.contains(query, ignoreCase = true) }
    }
    // ...
}

// ❌ BAD: Boolean derived from scroll position recomposes on every pixel
@Composable
fun ScreenWithFab(scrollState: LazyListState) {
    val showFab = scrollState.firstVisibleItemIndex > 0 // reads scroll state directly
    AnimatedVisibility(visible = showFab) { Fab() }
}

// ✅ GOOD: derivedStateOf reduces recomposition to value changes
@Composable
fun ScreenWithFab(scrollState: LazyListState) {
    val showFab by remember {
        derivedStateOf { scrollState.firstVisibleItemIndex > 0 }
    }
    AnimatedVisibility(visible = showFab) { Fab() }
}
```

**Suggested Fixes:**
- Wrap any O(n) or expensive computation in `remember(keys)`
- Use `derivedStateOf` when derived value changes less frequently than source
- Move expensive transformations to ViewModel as `StateFlow` chains

---

### 4. Views: RecyclerView Over-Binding

Identify RecyclerView patterns that rebind more than necessary:

* **`notifyDataSetChanged()` on large lists:**
  - Used instead of `DiffUtil` / `ListAdapter` — forces rebind of all visible items
  - Especially problematic when only 1-2 items changed

* **Expensive `onBindViewHolder`:**
  - Image loading, date formatting, layout inflation inside bind
  - Complex view manipulation on every bind call

* **Missing stable IDs:**
  - Without `setHasStableIds(true)` + unique `getItemId()`, RecyclerView cannot optimize rebinding

* **Invalidating parent containers:**
  - Calling `requestLayout()` or `invalidate()` on a parent that contains the RecyclerView
  - Wrapping RecyclerView in `NestedScrollView` causing full measurement passes

**Best Practices:**
```kotlin
// ❌ BAD: Nuclear option
fun updateItems(newItems: List<Item>) {
    items = newItems
    notifyDataSetChanged() // rebinds ALL visible items
}

// ✅ GOOD: Targeted updates with DiffUtil
class ItemAdapter : ListAdapter<Item, ItemViewHolder>(ItemDiffCallback()) {
    // submitList() handles diffing automatically
}

class ItemDiffCallback : DiffUtil.ItemCallback<Item>() {
    override fun areItemsTheSame(old: Item, new: Item) = old.id == new.id
    override fun areContentsTheSame(old: Item, new: Item) = old == new
}

// ❌ BAD: Expensive work in bind
override fun onBindViewHolder(holder: ViewHolder, position: Int) {
    val item = items[position]
    holder.dateText.text = SimpleDateFormat("MMM dd, yyyy", Locale.US).format(item.date)
    Glide.with(holder.itemView).load(item.imageUrl).into(holder.image) // on EVERY bind
}

// ✅ GOOD: Cache formatters, use payload-based partial bind
private val dateFormatter = SimpleDateFormat("MMM dd, yyyy", Locale.US)

override fun onBindViewHolder(holder: ViewHolder, position: Int, payloads: List<Any>) {
    if (payloads.isNotEmpty()) {
        // Partial bind — only update changed fields
        holder.bindPartial(items[position], payloads)
        return
    }
    holder.bindFull(items[position])
}
```

**Suggested Fixes:**
- Replace `notifyDataSetChanged()` with `ListAdapter` + `DiffUtil.ItemCallback`
- Implement `areContentsTheSame` with fine-grained field comparison
- Use payload-based partial binding for expensive items
- Enable stable IDs for animator optimizations
- Pre-compute formatted strings in ViewModel, not in `onBindViewHolder`
- Avoid nesting RecyclerViews; use `ConcatAdapter` for mixed-type lists

---

### 5. Views: Container-Level Invalidation

Identify cases where small changes trigger large view hierarchy updates:

* **`requestLayout()` propagation:**
  - Changing a `TextView` content that triggers parent `ConstraintLayout` re-measurement
  - Toggling visibility of a view inside deeply nested layouts

* **`invalidate()` on large containers:**
  - Custom views calling `invalidate()` on parent views unnecessarily
  - Background/drawable changes on container-level views

**Suggested Fixes:**
- Use `ConstraintLayout` barriers/guidelines to isolate measurement changes
- Prefer `View.INVISIBLE` over `View.GONE` when layout stability matters
- Use `ViewStub` for rarely-shown content
- Flatten view hierarchy to reduce measurement propagation

---

## Expected Output

Provide an over-broad UI updates review report including:

### 1. Executive Summary
- UI update efficiency rating
- Framework: Compose / Views / Hybrid
- Critical over-broad update count

### 2. Update Scope Analysis

| Trigger | Actual Scope | Necessary Scope | Excess Cost | Priority |
|---------|-------------|-----------------|-------------|----------|
| [State change] | [Full screen] | [One widget] | [estimate] | [Level] |

### 3. Detailed Findings

For each issue:
- **Location:** file:line
- **Category:** State Read Placement / Unstable Params / Missing Remember / RecyclerView Over-Bind / Container Invalidation
- **Trigger → Scope:** What changes, what redraws
- **Impact:** Estimated cost of over-broad update
- **Confidence:** High / Medium / Low
- **Current Code:** With explanation of the blast radius
- **Recommended Fix:** Narrowed update scope with code
- **Verification:** How to confirm improvement (Layout Inspector, recomposition counts, profiler)

### 4. Prioritized Remediation Plan

Ordered by reduction in unnecessary work.

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on update scope analysis
- **ST-02** (Structured Sequential Instructions) — Compose then Views systematic review
- **RT-02** (Multi-Dimensional Analysis) — State reads, params, caching, binding, invalidation
- **RT-05** (Evidence-Based Reasoning) — Verify scope with profiling evidence
- **DS-06** (Prioritization Guidance) — Ranked by wasted recomputation cost
- **QA-01** (Chain-of-Verification) — Confirm scope before flagging

---

## Related Prompts

- `android_compose_recomposition_review.md` — Deep dive into Compose recomposition
- `android_state_propagation_review.md` — For upstream state delivery issues
- `android_list_rendering_inefficiency_review.md` — For list-specific performance
- `performance_bottleneck_identification.md` — For general performance analysis
