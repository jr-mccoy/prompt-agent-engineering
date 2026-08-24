# Android Layer Tracing Guide

Detailed guide for tracing code execution through each architectural layer of a modern Android application. Use this when you need to follow a user action from touch event to data persistence and back.

## The Android Layer Stack

```
┌─────────────────────────────────────────────┐
│  UI Layer (Compose / Views)                 │
│  Screen composables, click handlers, state  │
│  observation, navigation triggers           │
├─────────────────────────────────────────────┤
│  ViewModel Layer                            │
│  State management, business logic,          │
│  coroutine launching, error mapping         │
├─────────────────────────────────────────────┤
│  Domain Layer (optional)                    │
│  Use cases, business rules, transformations │
├─────────────────────────────────────────────┤
│  Repository Layer                           │
│  Data source coordination, caching,         │
│  offline strategy, conflict resolution      │
├─────────────────────────────────────────────┤
│  Data Source Layer                           │
│  Room DAOs, Firebase references, API calls, │
│  DataStore, SharedPreferences               │
├─────────────────────────────────────────────┤
│  Background Layer                           │
│  WorkManager, Services, BroadcastReceivers, │
│  sync operations, notification handling     │
└─────────────────────────────────────────────┘
```

## Layer 1: UI → ViewModel Boundary

### What Crosses This Boundary

**Downward (UI → ViewModel):**
- User action events (tap, swipe, text input)
- Lifecycle events (screen appeared, resumed)
- Navigation arguments
- System events forwarded from UI (permissions result, activity result)

**Upward (ViewModel → UI):**
- UI state (via StateFlow, typically a sealed class or data class)
- One-time events (via SharedFlow or Channel — navigation, snackbar, toast)
- Loading indicators (usually part of UI state)

### Tracing Patterns

**Direct function call:**
```kotlin
// UI calls ViewModel directly
Button(onClick = { viewModel.onSaveClicked() })
```
Trace: `onSaveClicked()` → what happens inside

**Event-based:**
```kotlin
// UI sends event, ViewModel processes
viewModel.onEvent(MyEvent.SaveClicked)
```
Trace: `onEvent()` → `when(event)` dispatch → handler function

**State observation:**
```kotlin
val state by viewModel.uiState.collectAsStateWithLifecycle()
```
Trace: What mutations to `_uiState` cause recomposition? Follow every `.update {}` or `.value = ` assignment.

### Common Pitfalls to Document

- ViewModel functions launched in `viewModelScope` — what happens if scope is cancelled?
- Multiple rapid calls — is there debouncing or protection against double-tap?
- State race conditions — can two state updates conflict?

## Layer 2: ViewModel → Repository Boundary

### What Crosses This Boundary

**Downward:**
- Data requests (get, query, search)
- Data mutations (create, update, delete)
- Parameters for the operation

**Upward:**
- Data results (usually via `Flow<T>` or `suspend` return)
- Errors (via exceptions or Result type)

### Tracing Patterns

**Suspend function call:**
```kotlin
viewModelScope.launch {
    val result = repository.saveItem(item)
    // handle result
}
```
Trace: What does `saveItem` do? Does it throw on error or return Result?

**Flow collection:**
```kotlin
repository.getItems()
    .map { items -> items.toUiModel() }
    .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), emptyList())
```
Trace: What does `getItems()` return? Is it Room Flow (auto-updates) or one-shot? What does `WhileSubscribed(5000)` mean for the upstream?

### Common Pitfalls to Document

- Repository returns Flow but ViewModel collects with wrong sharing strategy
- Error handling mismatch: Repository throws, ViewModel doesn't catch
- Repository returns cached data while network call runs — is this intentional?

## Layer 3: Repository → Data Source Boundary

### What Crosses This Boundary

**Downward:**
- Queries to Room DAO
- Calls to Firebase SDK
- HTTP requests to API

**Upward:**
- Raw data (entities, documents, API responses)
- Errors (IO exceptions, Firebase exceptions, HTTP errors)

### Data Source Coordination Patterns

**Cache-first (offline-first):**
```kotlin
fun getItems(): Flow<List<Item>> {
    return dao.getAll()  // Returns Room Flow (auto-updates)
}

suspend fun refreshItems() {
    val remote = api.fetchItems()
    dao.insertAll(remote.map { it.toEntity() })
    // Room Flow auto-emits new data
}
```
Trace: When is `refreshItems()` called? What if it fails? Does the user see stale data?

**Network-first:**
```kotlin
suspend fun getItems(): List<Item> {
    return try {
        val remote = api.fetchItems()
        dao.insertAll(remote)  // cache
        remote
    } catch (e: Exception) {
        dao.getAll()  // fallback to cache
    }
}
```
Trace: What if both network and cache fail? Is the error surfaced to the user?

**Firebase listener:**
```kotlin
fun observeItems(): Flow<List<Item>> = callbackFlow {
    val listener = ref.addValueEventListener(object : ValueEventListener {
        override fun onDataChange(snapshot: DataSnapshot) {
            trySend(snapshot.toItems())
        }
        override fun onCancelled(error: DatabaseError) {
            close(error.toException())
        }
    })
    awaitClose { ref.removeEventListener(listener) }
}
```
Trace: When is the listener detached? What happens if `close()` is called with an error? Does the collecting coroutine handle it?

## Layer 4: Room Database Operations

### What to Trace in Detail

**Insert operations:**
- Conflict strategy: `OnConflictStrategy.REPLACE` silently overwrites, `ABORT` throws, `IGNORE` silently drops
- Are related entities inserted in the same transaction?
- Are auto-generated IDs handled correctly?

**Query operations:**
- Does the query return `Flow<List<T>>` (reactive) or `suspend fun` (one-shot)?
- Are there any N+1 query patterns (querying in a loop)?
- Are queries filtered/sorted at the SQL level or in Kotlin?
- Are there any missing indexes on frequently queried columns?

**Update/Delete operations:**
- Is the correct entity matched (by primary key)?
- Are cascading effects handled? (`@Relation`, `ForeignKey`)
- Is the operation within a transaction when it should be?

**Migrations:**
- Is there an auto-migration or manual migration for each schema change?
- Does the migration preserve existing data?
- What happens if migration fails?

## Layer 5: Firebase Operations

### What to Trace in Detail

**Authentication:**
- Sign-in method (email/password, Google, anonymous)
- Token refresh behavior
- Auth state listener placement and lifecycle
- What happens when auth expires mid-session?

**Realtime Database / Firestore:**
- Read: Single read vs persistent listener? Query constraints?
- Write: Set (overwrite) vs Update (merge)? What fields are written?
- Rules dependency: Does the code assume the security rules allow this operation?
- Offline: Is persistence enabled? What's the cache size limit?

**Cloud Functions:**
- What data is sent to the function?
- What does the function return?
- Timeout configuration?
- Error handling for function failures?

## Layer 6: Background Operations

### WorkManager Tracing

For each Worker class, trace:

```
Worker: [ClassName]
├── Scheduled by: [what code creates the work request]
├── Constraints: [NetworkType, BatteryNotLow, etc.]
├── Input data: [what data is passed in]
├── doWork() execution:
│   ├── Step 1: [operation]
│   ├── Step 2: [operation]
│   ├── Error handling: [what happens on exception]
│   └── Return: Result.success() / Result.retry() / Result.failure()
├── Retry policy: [LINEAR/EXPONENTIAL, max attempts]
├── Output data: [what data is returned]
└── Chain dependencies: [chained with other workers?]
```

### Service Tracing

For each Service, trace:
- Lifecycle: `onCreate` → `onStartCommand`/`onBind` → `onDestroy`
- Is it a foreground service? What notification does it show?
- What work does it perform?
- How is it started and stopped?
- What happens on system-initiated kill?

## Completeness Checklist

Before moving to the audit phase, verify the behavior catalog covers:

- [ ] Every user-facing action in the selected feature area
- [ ] The complete code path for each action (UI through data layer)
- [ ] Both success and error paths for each operation
- [ ] Edge cases: process death, config change, no network, concurrent access
- [ ] Background operations related to the feature
- [ ] Data flow in both directions (user action → data store → UI update)
- [ ] All state transitions (loading, success, error, empty)
- [ ] Navigation triggers and their conditions
- [ ] Side effects (analytics events, notifications, sync triggers)
