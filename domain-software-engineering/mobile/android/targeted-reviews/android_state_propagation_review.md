---
title: "Android State Propagation Review"
category: mobile/android/targeted-reviews
description: "Android State Propagation Review."
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
  - propagation
  - review
  - reviews
  - state
updated: "2026-03-19"
related_prompts: []
---

# Android State Propagation Review

---
title: "Android State Propagation Review"
category: mobile/android/performance
description: "Detect wrong or delayed state propagation causing UI updates that lag behind user actions without freezing"
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
  - state-management
  - livedata
  - stateflow
  - compose-state
  - reactivity
  - performance
  - ui-responsiveness
updated: "2026-03-09"
---

**Android State Propagation Review

Objective: Analyze the Android codebase to identify state propagation issues — places where UI state changes are delayed, dropped, suppressed, or rendered inconsistently because of incorrect reactive wiring. Focus on structural problems in the path from state mutation to UI consumption that make the UI feel behind user actions, stale after lifecycle changes, or inconsistent across surfaces.

When to Use: Use when the UI feels behind user actions, when changes take too long to appear, when state seems stale after navigation or configuration change, when updates vanish unless another action happens later, or when different parts of the same screen show conflicting data. This is for propagation and wiring failures, not ANRs or hard freezes.


---

Instructions

CRITICAL: Static Review Constraints

This is a static code review. You do NOT have runtime traces, profiler data, device measurements, or real-world telemetry.

Before reporting any finding, you MUST:

1. Trace the full propagation chain

Follow the path from the point of mutation to the point of rendered UI consumption.

Include the full chain of relevant file:line locations across data source, repository, ViewModel, adapters/mappers, lifecycle collection, and UI rendering.

Do NOT flag patterns in isolation.



2. Identify the state type and source of truth

Specify whether the affected value is:

durable UI state

derived UI state

one-shot event

cached data

lifecycle-restored state


Identify the source of truth:

local UI state

ViewModel state

repository state

Room/DB Flow

network response

SavedStateHandle

derived/combined state




3. Classify the user-visible failure mode

Delayed propagation: the UI updates later than the architecture requires

Dropped propagation: a legitimate state change may never reach the UI

Inconsistent propagation: different UI surfaces or lifecycles observe different values

Stale replay / stale restoration: an old value is rendered after recreation/navigation when a newer one should be shown



4. Confirm the issue is structurally user-visible

Explain why the current chain can plausibly produce a visible delay, lost update, stale render, or inconsistent UI.

Do NOT report findings based only on suspicious-looking operators or patterns.

Do NOT invent milliseconds or claim measured latency.



5. Check for intentional design

Some delayed propagation is correct:

debounce on search query

throttle/conflate on high-frequency sensor streams

lifecycle-gated collection for expensive or privacy-sensitive sources


If the pattern is intentional, explain why it should not be flagged.



6. Classify evidence correctly

High-confidence structural issue: the code clearly allows or forces a visible propagation problem

Plausible structural issue: the code strongly suggests a propagation problem, but some wiring is inferred

Needs runtime verification: the structure looks risky, but rendered behavior cannot be determined confidently from code



7. Deduplicate findings

Report each user-visible propagation failure once under the primary category.

Mention contributing factors inside the same finding rather than creating duplicates.




Finding NO issues is an acceptable outcome. If propagation is correctly wired, say so.


---

False-Positive Prevention

❌ Do NOT flag debounce / throttle on search input or intentionally rate-limited streams when scoped correctly

❌ Do NOT flag distinctUntilChanged just because it suppresses redundant emissions

❌ Do NOT flag conflate on high-frequency streams where latest-only semantics are correct

❌ Do NOT flag SharingStarted.WhileSubscribed(5000) as inherently delayed

❌ Do NOT assume in-place mutation without tracing actual mutation sites and emission behavior

❌ Do NOT flag a combined ViewModel state as “multiple sources of truth” unless multiple owners can diverge

❌ Do NOT treat one-shot event delivery problems and durable state propagation problems as interchangeable

❌ Do NOT invent timing numbers such as “200ms lag” in a static review

✅ DO verify whether assignment style (value, postValue, update) matches threading and emission semantics

✅ DO check whether equality semantics suppress legitimate UI updates

✅ DO trace lifecycle-aware collection and replay behavior across stop/start, navigation, and recreation

✅ DO verify that combine, merge, zip, flatMapLatest, mapLatest, and stateIn/shareIn produce the intended delivery behavior

✅ DO identify whether the issue affects immediate feedback, lifecycle restoration, or cross-surface consistency



---

Review Categories

1. In-Place Mutation and Emission Suppression

Identify state containers that may not emit because the held object is mutated in place or replaced with an effectively unchanged value.

Look for:

Mutable collections stored in state

MutableStateFlow<MutableList<T>>, MutableStateFlow<MutableMap<K, V>>

MutableLiveData<MutableList<T>>

Compose state holding mutable containers whose reference does not change


In-place mutation of nested objects

mutating a child object without creating a new parent state reference

mutating fields on objects stored inside a state container without re-emitting a structurally new state


Equality-based suppression

StateFlow suppressing emission because newValue == oldValue

custom state objects with broken or misleading equals()/hashCode()

recomposition/state observation relying on reference or structural equality that is not actually invalidated



Best Practices:

// ❌ BAD: In-place mutation — StateFlow may not emit meaningful change
_uiState.value.items.add(newItem)
_uiState.value = _uiState.value

// ✅ GOOD: New state reference
_uiState.update { state ->
    state.copy(items = state.items + newItem)
}

// ❌ BAD: Mutating LiveData-held object
val current = _liveData.value!!
current.name = "Updated"
_liveData.value = current

// ✅ GOOD: New object
_liveData.value = current.copy(name = "Updated")

Suggested Fixes:

Store immutable collections in state (List, Map, persistent collections)

Use copy() for data-class-based state updates

Prefer MutableStateFlow.update {} for atomic read-modify-write

Audit nested state for mutable children that bypass parent invalidation

Verify equals()/hashCode() on state objects used with StateFlow, distinctUntilChanged, or Compose state



---

2. Multiple Sources of Truth and Divergent Ownership

Identify where the same logical UI state is owned or mutated in multiple places, allowing divergence.

Look for:

Duplicate mutable copies

same data kept in both UI layer and ViewModel

repository cache plus ViewModel copy plus local composable remember

Fragment/Activity maintaining a mutable mirror of ViewModel state


Competing write paths

UI mutates local state while ViewModel mutates a separate copy

multiple ViewModels writing to the same shared concept independently

SavedStateHandle and ViewModel state updated through different paths


Stale references after recreation

adapters, delegates, or remembered state holding onto old references

restored state diverging from current source of truth after navigation/process death



Best Practices:

// ❌ BAD: Fragment keeps its own mutable copy
class MyFragment : Fragment() {
    private var localItems = mutableListOf<Item>()

    override fun onViewCreated(...) {
        viewModel.items.observe(viewLifecycleOwner) { items ->
            localItems = items.toMutableList()
            adapter.submitList(localItems)
        }
    }

    fun onItemDeleted(id: String) {
        localItems.removeIf { it.id == id }
        adapter.submitList(localItems.toList())
        viewModel.deleteItem(id)
    }
}

// ✅ GOOD: Single owner of mutable state
class MyFragment : Fragment() {
    override fun onViewCreated(...) {
        viewLifecycleOwner.lifecycleScope.launch {
            viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
                viewModel.items.collectLatest { items ->
                    adapter.submitList(items)
                }
            }
        }
    }

    fun onItemDeleted(id: String) {
        viewModel.deleteItem(id)
    }
}

Suggested Fixes:

Establish one mutable owner per logical state value

Keep UI as a renderer/dispatcher, not a second mutable store

If local UI-only state is necessary, define clear ownership boundaries

Keep optimistic state inside the official owner, not in parallel UI copies

Reconcile SavedStateHandle, ViewModel state, and repository-backed state explicitly



---

3. Collection and Observation Wiring

Verify that state is actually being observed correctly at the UI boundary.

Look for:

Wrong lifecycle owner or scope

Fragment using lifecycleScope instead of viewLifecycleOwner.lifecycleScope

LiveData observed with this instead of viewLifecycleOwner

collectors outliving the view or missing the recreated view


Missing or incorrect collection

ViewModel exposes state that the UI never collects

Compose using collectAsState() where lifecycle-aware collection is required

wrong LifecycleOwner preventing expected replay/update delivery


Wrong primitive for the job

durable screen state modeled as SharedFlow(replay = 0)

one-shot events modeled as state and re-fired unintentionally

event streams collected in a way that loses delivery during lifecycle transitions



Best Practices:

// ❌ BAD: Collector tied to Fragment lifecycle, not view lifecycle
lifecycleScope.launch {
    viewModel.uiState.collect { ... }
}

// ✅ GOOD: View-lifecycle-aware collection
viewLifecycleOwner.lifecycleScope.launch {
    viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.uiState.collect { state ->
            updateUi(state)
        }
    }
}

// ✅ GOOD (Compose)
val uiState by viewModel.uiState.collectAsStateWithLifecycle()

// ❌ BAD (Compose)
val uiState by viewModel.uiState.collectAsState()

Suggested Fixes:

Use viewLifecycleOwner in Fragments for rendered UI collection

Use repeatOnLifecycle / flowWithLifecycle where appropriate

Use collectAsStateWithLifecycle() in Compose

Model durable UI state with StateFlow or replaying state holder

Model one-shot events with a primitive and collection strategy appropriate to lifecycle semantics



---

4. Lifecycle and Replay Semantics

Check whether lifecycle-aware collection, replay, or restart behavior causes stale, missing, or late state.

Look for:

Replay mismatch

SharedFlow(replay = 0) used where re-delivery after recreation is required

StateFlow used where transient one-time delivery was intended

stateIn/shareIn configured such that late subscribers miss necessary current state


Lifecycle stop/start gaps

collection restarts correctly, but upstream does not replay the latest needed value

updates emitted while UI is stopped are silently lost when the user expects continuity


WhileSubscribed behavior

too-short stop timeout causing unnecessary upstream cancellation/restart

restart sequences that refetch or recompute, making state appear stale or delayed after quick navigation/config change


Restoration divergence

SavedStateHandle, repository state, and current in-memory state restoring in the wrong order

old state replayed briefly before newer state replaces it



Suggested Fixes:

Match replay semantics to the value type: durable state vs transient event

Use StateFlow or replaying shared state for screen state that must survive re-collection

Use sensible WhileSubscribed timeouts to avoid churn on quick recreation

Audit restoration ordering across SavedStateHandle, repository, and ViewModel initialization

Make replay/restart behavior explicit rather than incidental



---

5. Debounce / Throttle / Conflation Audit

Check whether rate-limiting or backpressure operators hide legitimate updates or delay the wrong state.

Look for:

Over-broad debounce

debounce applied to whole screen state instead of just the noisy input field

non-search actions delayed because they share a debounced aggregate stream


Conflation dropping meaningful intermediates

conflate() on progress, step transitions, staged loading, or multi-step visual state where intermediates matter

buffer(CONFLATED) dropping states the UI should actually render


Backpressure and queueing mismatch

buffering that causes visible stale delivery under a slow collector

rate limiting attached downstream near the UI instead of upstream near the noisy source



Best Practices:

// ❌ BAD: Debounce applied to full UI state
viewModel.uiState
    .debounce(300)
    .collect { ... }

// ✅ GOOD: Debounce only the noisy query stream
combine(
    viewModel.searchQuery.debounce(300),
    viewModel.filterState,
    viewModel.items
) { query, filter, items -> ... }

Suggested Fixes:

Apply debounce/throttle only to the specific noisy stream

Keep primary screen state immediate unless delayed delivery is intentional

Use conflation only where latest-only semantics are correct

Avoid buffering patterns that make UI delivery observably stale



---

6. Reactive Transformation Chain Audit

Check whether intermediate operators or composition choices suppress, restart, delay, or distort propagation.

Look for:

Unnecessary restart behavior

flatMapLatest used where frequent source emissions repeatedly cancel/restart expensive inner work

restart patterns that cause visible state churn, stale fallback state, or delayed steady-state render


Transformation bottlenecks

heavy synchronous work in map, combine, or collectors

large aggregate combines where one slow source or transform delays a useful visible update


Equality / distinct misuse

distinctUntilChanged with objects whose equality does not match rendering semantics

state objects always looking “new” due to missing equality, causing churn

state objects incorrectly looking “unchanged,” suppressing required UI invalidation


Operator semantics mismatch

zip used where latest-combination semantics were intended

merge used where ordering/coherence matters

derived state rebuilt in a way that delays or masks a simpler direct update path



Suggested Fixes:

Prefer mapLatest over flatMapLatest when a new flow is not required

Move truly expensive transforms off the main-sensitive path

Break apart oversized aggregate state chains where a smaller direct emission would improve responsiveness

Audit operator choice against desired semantics: latest, ordered, replayed, restartable, conflated, or lossless

Verify equality semantics for every state object used in suppression-sensitive operators



---

Expected Output

Provide a state propagation review report with the following sections.

1. Executive Summary

Include:

Overall state propagation health: Excellent / Good / Fair / Poor

Propagation chains traced: count

High-confidence structural issues: count

Plausible issues needing runtime verification: count

Dominant failure mode(s): delayed / dropped / inconsistent / stale-restored

Overall assessment: brief summary of the main propagation risks



---

2. Propagation Chain Map

Chain	Source → UI Path	Failure Risk	Primary Issue	Priority

[Name]	[Mutation/DataSource → Repo → VM → Lifecycle Collection → UI]	[Delayed / Dropped / Inconsistent / Stale]	[Description]	[High / Medium / Low]


Notes:

Do NOT invent milliseconds

Describe the chain and the structural failure mode

Prioritize by user-visible impact and breadth of effect



---

3. Detailed Findings

For each issue, provide:

Location: full file:line chain from mutation to rendered UI consumption

Category: In-Place Mutation / Multiple Sources / Collection Wiring / Lifecycle-Replay / Rate-Limiting / Transformation Chain

Failure mode: Delayed / Dropped / Inconsistent / Stale-restored

Affected state: what value or UI model is involved

Source of truth: Local UI / ViewModel / Repository / DB Flow / Network / SavedStateHandle / Derived

User-visible impact: how the problem would appear

Confidence: High / Medium / Low

Evidence type: High-confidence structural issue / Plausible structural issue / Needs runtime verification

Current Code Path: annotated propagation chain

Why propagation fails: exact structural reason updates are delayed, dropped, or diverge

Recommended Fix: corrected wiring or state model

Verification: how to confirm the fix with code inspection, targeted logging, or test coverage


Use this structure:

#### [Finding Title]

- **Location:** `TaskRepository.kt:67` → `TaskViewModel.kt:42` → `TaskScreen.kt:30`
- **Category:** In-Place Mutation
- **Failure mode:** Dropped
- **Affected state:** task list
- **Source of truth:** ViewModel `MutableStateFlow`
- **User-visible impact:** newly added task may not appear until an unrelated later emission
- **Confidence:** High
- **Evidence type:** High-confidence structural issue

**Current Code Path**
```kotlin
addTask(task)
  -> _tasks.value.add(task)
  -> _tasks.value = _tasks.value
  -> UI collector sees no new emitted list

Why propagation fails The state holder contains a mutable list that is mutated in place and then reassigned without producing a structurally new value. The collector may not receive a meaningful emission, so the rendered list stays stale until a different update path emits later.

Recommended Fix Store List<Task> instead of MutableList<Task> and update via _tasks.update { it + task }.

Verification Add a unit test asserting that addTask() produces a new emitted list immediately. Add targeted logging around the flow emission path if needed.

---

### 4. Prioritized Remediation Plan

Order recommendations by:

1. **Severity of user-visible failure**
2. **Breadth of impact across screens or flows**
3. **Ease of correcting the underlying state model or wiring**
4. **Risk of recurrence elsewhere in the codebase**

For each remediation item include:

- **Target chain(s)**
- **Why it matters**
- **Best fix strategy**
- **Expected improvement**
- **Implementation scope:** Small / Medium / Large

Prefer this order:

1. Dropped or inconsistent updates caused by broken state ownership or in-place mutation
2. Collection/lifecycle wiring bugs that affect recreated or navigated screens
3. Replay/restoration problems causing stale state after rotation/process death
4. Over-broad debounce/conflation or transformation-chain issues
5. Plausible findings that need runtime verification before refactor

---

## Review Rules

- Prefer one fully traced user-visible propagation failure over multiple speculative code-smell findings
- Report the **propagation failure**, not just the suspicious API usage
- Distinguish clearly between:
  - **durable state**
  - **derived state**
  - **one-shot events**
  - **restored state**
- Distinguish clearly between:
  - **delayed propagation**
  - **dropped propagation**
  - **inconsistent propagation**
  - **stale replay/restoration**
- If a pattern is intentional and semantically correct, do **not** force a finding
- If the rendered UI consumption point cannot be identified, mark the case **Needs runtime verification** or omit it

---

## Final Deliverable Standard

The report must answer this question for every finding:

**“What exact structural problem in the propagation chain prevents the intended state from reaching the rendered UI correctly, promptly, and consistently?”**

If that cannot be answered concretely from static code analysis, mark the case as **Needs runtime verification** or omit it.

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on state propagation delay
- **ST-02** (Structured Sequential Instructions) — Systematic category-by-category analysis
- **RT-02** (Multi-Dimensional Analysis) — Mutation, collection, lifecycle, operators
- **RT-05** (Evidence-Based Reasoning) — Trace actual chains, verify observable impact
- **DS-06** (Prioritization Guidance) — Ranked by user-perceived delay
- **QA-01** (Chain-of-Verification) — Verify before reporting

---

## Related Prompts

- `android_compose_recomposition_review.md` — For Compose-specific recomposition issues
- `android_viewmodel_state_management_review.md` — For ViewModel state patterns
- `android_coroutine_scope_review.md` — For coroutine lifecycle and scope issues
- `android_room_database_query_review.md` — For database observation issues
- `performance_bottleneck_identification.md` — For general performance analysis

