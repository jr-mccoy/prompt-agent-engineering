---
name: android-behavior-trace
description: "Deep code path tracing methodology for Android applications that follows user actions through all architectural layers (UI → ViewModel → Repository → Data → Network/Background) and produces a factual behavior catalog. Use this skill when tracing feature behavior across code layers, creating a behavior audit list, documenting what code actually does, or when users mention 'trace the code', 'what does this feature actually do', 'behavior catalog', or 'follow the code path'."
metadata:
  tags:
    - android
    - tracing
    - behavior-analysis
    - code-path
    - audit
  updated: "2026-02-17"
---

# Android Behavior Trace

Deep code path tracing methodology that follows user actions through every layer of an Android application and produces a structured behavior catalog. The output is purely factual — it documents what the code **actually does**, with no judgments about whether the behavior is correct.

## Purpose

After surveying an app and selecting areas to audit, you need to trace exactly what happens when a user interacts with each feature. This skill provides a systematic, layer-by-layer tracing methodology that ensures no code path is missed — including error paths, edge cases, and background operations. The output is a behavior catalog that becomes the input for behavioral scrutiny.

This is distinct from code review (which evaluates quality) and architecture review (which evaluates structure). Behavior tracing answers one question: "When the user does X, what does the code actually do?"

## When to Use This Skill

- Tracing code behavior for selected feature areas during a behavior audit
- Need to understand exactly what happens when a user performs an action
- Creating documentation of actual code behavior (not intended behavior)
- Building a behavior catalog for audit, testing, or knowledge transfer
- Pre-release verification that all code paths are accounted for

## When NOT to Use This Skill

- You need to survey the app first (use `android-app-survey` instead — survey before trace)
- You want to evaluate whether behavior is correct (use `android-behavior-audit` after tracing)
- You need to fix issues (use `android-behavior-fix-planning` after audit)
- You only need a high-level overview (survey is sufficient)
- The feature has no code yet (nothing to trace)

## Prerequisites

- A completed feature map from the survey phase (know what to trace)
- User's selection of which feature areas to trace
- Access to the full source code of the Android application

## Tracing Methodology: Layer-by-Layer

For each user action in the selected feature area, trace through every layer systematically.

### Layer 1: UI Layer

**What to trace:**
- User input handling (clicks, swipes, text input, gestures)
- UI state observation (how does the screen react to state changes?)
- Navigation triggers (what causes navigation to another screen?)
- Loading states (what does the user see while waiting?)
- Error states (what does the user see on error?)
- Empty states (what does the user see with no data?)

**Where to look:**
- Screen composables (`*Screen.kt`)
- Click handlers, `onClick`, `onValueChange` lambdas
- State collection: `collectAsStateWithLifecycle()`, `observeAsState()`
- Conditional rendering: `when(state)`, `if(isLoading)`, `AnimatedVisibility`

**Document format:**
```
UI: [Screen] → User taps [Button]
  → Calls viewModel.[function]()
  → Shows loading indicator via state.isLoading = true
  → On success: navigates to [Screen] / displays [data]
  → On error: shows [specific error UI]
```

### Layer 2: ViewModel Layer

**What to trace:**
- State management (how is UI state created and updated?)
- Business logic (validation, transformation, decisions)
- Side effects (what else happens besides updating state?)
- Error handling (how are errors caught and converted to UI state?)
- Coroutine scoping (which scope? what happens on cancellation?)

**Where to look:**
- ViewModel classes
- StateFlow/MutableStateFlow definitions
- `viewModelScope.launch` blocks
- `try/catch` blocks within coroutines
- `init {}` blocks (what loads on ViewModel creation?)

**Document format:**
```
ViewModel: [ClassName].[function]()
  → Validates input: [what validation]
  → Sets state to Loading
  → Calls repository.[function]()
  → On success: Updates state with [data], triggers [side effect]
  → On error: Catches [ExceptionType], sets state to Error([message])
  → Cancellation behavior: [what happens if scope is cancelled]
```

### Layer 3: Repository Layer

**What to trace:**
- Data source selection (local vs remote? which source wins?)
- Caching strategy (cache-first? network-first? cache-then-network?)
- Data transformation (does data change shape between layers?)
- Conflict resolution (what happens when local and remote disagree?)
- Offline behavior (what happens with no network?)

**Where to look:**
- Repository classes (usually in `data/repository/`)
- `@Inject constructor` parameters (which data sources are injected?)
- Flow operators (`.map`, `.flatMapLatest`, `.combine`, `.catch`)
- Network checks (`NetworkManager`, `ConnectivityManager`)

**Document format:**
```
Repository: [ClassName].[function]()
  → Checks [condition] to select data source
  → Local path: Queries Room DAO [function]
  → Remote path: Calls [API/Firebase] for [data]
  → Combines/transforms: [how data is merged or transformed]
  → Caches result: [where and how]
  → Error handling: [what happens on failure at this layer]
```

### Layer 4: Data Layer

**What to trace for Room:**
- Query logic (what SQL runs? any joins? any filtering?)
- Write operations (insert strategy: REPLACE, ABORT, IGNORE?)
- Transaction boundaries (are related writes in a transaction?)
- Migration handling (how are schema changes managed?)
- Data consistency (are related entities updated together?)

**What to trace for Firebase:**
- Read operations (single-value vs listener? query filters?)
- Write operations (set vs update? merge behavior?)
- Security rules dependency (does code assume rules allow this?)
- Offline persistence (is offline mode enabled? cache size?)
- Listener lifecycle (when are listeners attached/detached?)

**What to trace for API calls:**
- Request construction (headers, auth tokens, parameters)
- Response handling (deserialization, error response parsing)
- Retry logic (does it retry? how many times? backoff?)
- Timeout configuration (how long before timeout?)

**Document format:**
```
Data: Room DAO [ClassName].[function]()
  → SQL: [actual query or insert/update/delete]
  → Conflict strategy: [REPLACE/ABORT/IGNORE]
  → Returns: [type and structure]
  → Transaction: [yes/no, with what other operations]

Data: Firebase [service] at path [path]
  → Operation: [get/set/update/listen]
  → Filters: [query constraints]
  → Listener lifecycle: [attached in X, detached in Y]
  → Offline behavior: [cached/not cached]
```

### Layer 5: Background & System Layer

**What to trace:**
- WorkManager tasks (constraints, retry policy, chain dependencies)
- Services (foreground service lifecycle, binding behavior)
- Broadcast receivers (what intents are handled?)
- Notifications (when created, what actions, channel configuration)
- Sync operations (how sync is triggered, conflict resolution)

**Where to look:**
- Classes extending `CoroutineWorker` or `Worker`
- Work requests created with `OneTimeWorkRequestBuilder` or `PeriodicWorkRequestBuilder`
- `Service` subclasses, `ForegroundService` usage
- `BroadcastReceiver` subclasses
- Notification creation and channel setup

**Document format:**
```
Background: WorkManager [WorkerName]
  → Trigger: [what schedules this worker]
  → Constraints: [network, battery, charging requirements]
  → Operation: [what work is performed]
  → Success path: [what happens on completion]
  → Failure path: [retry policy, max attempts, backoff]
  → Data passing: [input data, output data]
```

## Behavior Cataloging Template

Compile all traced behaviors into this structured format:

```markdown
# Behavior Catalog: [Feature Area]

## Summary
- **Feature area:** [name]
- **Screens involved:** [list]
- **ViewModels:** [list]
- **Repositories:** [list]
- **Data sources:** [list]
- **Background workers:** [list]
- **Total behaviors cataloged:** [count]

## Behaviors

### [Feature Area] — [Sub-feature]

| # | User Action | Code Behavior | Code Location | Edge Cases |
|---|-------------|---------------|---------------|------------|
| 1 | User taps "Save" button | Validates fields (name non-empty, email format), calls repository.save(), shows loading, navigates to list on success, shows snackbar on error | `SaveScreen.kt:45`, `SaveViewModel.kt:78`, `ItemRepository.kt:92` | Empty name: shows inline error. No network: queues for sync. Process death during save: state lost |
| 2 | ... | ... | ... | ... |
```

## Code Path Analysis Patterns

### Following a User Action End-to-End

For each user action, trace the complete chain:

```
User Input (UI)
  → Event Handler (UI/ViewModel boundary)
    → ViewModel Function
      → Business Logic / Validation
        → Repository Call
          → Data Source Operation (Room/Firebase/API)
            → Response/Result
          ← Data flows back up
        ← Repository returns result
      ← ViewModel updates state
    ← UI observes state change
  ← User sees result
```

At each step, document:
1. **What function is called** (with file:line)
2. **What parameters are passed**
3. **What the function does with those parameters**
4. **What it returns or emits**
5. **What happens on error at this step**

### Tracing Reactive Chains

For Flow/StateFlow chains, trace the full pipeline:

```
Source Flow (e.g., Room DAO query)
  → .map { transform }
  → .flatMapLatest { nested operation }
  → .catch { error handling }
  → .stateIn(scope, started, initial)
  → Collected in UI via collectAsStateWithLifecycle()
```

Document each operator's purpose and what happens if data is null, empty, or error.

### Tracing Initialization Sequences

For features that load data on screen entry:

```
Navigation to Screen
  → Screen Composable created
    → ViewModel created (by Hilt)
      → init {} block runs
        → Loads initial data
        → Sets up observers/listeners
      → State initialized with default/loading values
    → UI renders initial state
  → Data arrives asynchronously
    → State updated
    → UI recomposes with data
```

## Edge Case Enumeration Checklist

For each behavior traced, check these edge cases:

### Lifecycle Edge Cases
- [ ] What happens on configuration change (rotation)?
- [ ] What happens on process death and restoration?
- [ ] What happens if the user navigates away mid-operation?
- [ ] What happens if the ViewModel is cleared during an async operation?

### Data Edge Cases
- [ ] What happens with empty/null data?
- [ ] What happens with malformed/unexpected data?
- [ ] What happens with very large datasets?
- [ ] What happens when data conflicts between local and remote?

### Network Edge Cases
- [ ] What happens with no network connectivity?
- [ ] What happens on network timeout?
- [ ] What happens on server error (4xx, 5xx)?
- [ ] What happens if the request succeeds but the response is unexpected?

### Concurrency Edge Cases
- [ ] What happens if the user triggers the action twice rapidly?
- [ ] What happens if two operations modify the same data simultaneously?
- [ ] What happens if a background sync runs while the user is editing?

### Permission Edge Cases
- [ ] What happens if a required permission is denied?
- [ ] What happens if a permission is revoked while the app is running?

## Output Requirements

The behavior catalog must be:
1. **Factual** — Only document what the code does, not what it should do
2. **Complete** — Every code path traced, including error and edge cases
3. **Referenced** — Every behavior tied to specific `file:line` locations
4. **Structured** — Uses the cataloging template consistently
5. **Non-judgmental** — No evaluations of whether behavior is correct or incorrect

The audit phase (next step) will evaluate the catalog for correctness. The trace phase only observes and records.

## Related Skills

- `android-app-survey` — Must complete survey before tracing (need feature map first)
- `android-behavior-audit` — Use after tracing to evaluate behavior for correctness

## Cross-References: Existing Review Prompts

When tracing specific Android subsystems, reference these existing targeted review prompts for subsystem-specific guidance:

| Subsystem | Existing Prompt |
|-----------|----------------|
| ViewModel state | `android_viewmodel_state_management_review.md` |
| Compose recomposition | `android_compose_recomposition_review.md` |
| Room database | `android_room_database_query_review.md` |
| Process death | `android_process_death_recovery_review.md` |
| Coroutine scopes | `android_coroutine_scope_review.md` |
| Sync architecture | `android_sync_architecture_review.md` |
| Offline conflicts | `android_offline_conflict_resolution_review.md` |
| WorkManager | `android_workmanager_background_review.md` |
| Data integrity | `android_data_integrity_audit.md` |
| Hilt DI scopes | `android_hilt_di_scope_review.md` |
| Room migrations | `android_room_migration_safety_audit.md` |
| Repository pattern | `android_repository_pattern_review.md` |
