---
title: "Coroutines to Swift Concurrency Migration"
category: mobile-development
description: "Migrate Kotlin Coroutines to Swift Concurrency covering suspend to async, Flow to AsyncSequence, CoroutineScope to TaskGroup, Dispatchers to Actors, and structured concurrency"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-02
difficulty: advanced
tags:
  - ios
  - android
  - migration
  - coroutines
  - swift-concurrency
  - async-await
  - flow
  - actors
updated: "2026-03-19"
---

# Coroutines to Swift Concurrency Migration

**Objective:** Systematically translate Kotlin Coroutines patterns to Swift Concurrency equivalents, covering suspend functions, Flow, CoroutineScope, Dispatchers, structured concurrency, error handling, and cancellation. The output enables developers to write concurrent iOS code with the same safety and expressiveness as Coroutines.

**When to Use:** When migrating an Android app's async/concurrent code to iOS. This is one of the most nuanced migration areas because while both systems share the async/await concept, their cancellation, scoping, and streaming models differ significantly.

**Prompt Type:** Comprehensive (~350 lines)

## Context Gathering

1. What Coroutine patterns are used? (suspend functions, Flow, Channel, SharedFlow, StateFlow)
2. What Dispatchers are used? (Main, IO, Default, custom)
3. How is structured concurrency managed? (viewModelScope, lifecycleScope, custom CoroutineScope)
4. Are there complex Flow operators? (flatMapLatest, combine, debounce, distinctUntilChanged)
5. Is SupervisorJob used for error isolation?
6. Are there any Mutex or Semaphore patterns?
7. How is cancellation handled? (isActive checks, ensureActive, CancellationException)

## Instructions

### CRITICAL: Verification Requirements

- Every suspend function MUST have an async Swift equivalent with matching error behavior
- Flow streams MUST be translated to AsyncSequence with correct backpressure behavior
- Cancellation MUST propagate correctly through the Swift task hierarchy
- Dispatcher mapping MUST preserve threading guarantees (main thread for UI, background for IO)

### False-Positive Prevention

- ❌ DO NOT assume Flow and AsyncSequence have identical semantics
- ✅ DO note that AsyncSequence is pull-based while Flow is push-based — this affects backpressure
- ❌ DO NOT ignore Swift's actor isolation when translating Dispatcher switches
- ✅ DO use `@MainActor` for UI updates instead of `Dispatchers.Main`
- ❌ DO NOT use `DispatchQueue.global()` as a direct replacement for `Dispatchers.IO`
- ✅ DO use Swift's cooperative thread pool (default for `async` functions) which manages threads automatically
- ❌ DO NOT catch `CancellationError` for error handling — it should propagate
- ✅ DO let `CancellationError` propagate naturally and check `Task.isCancelled` when needed

### Step 1: Core Concept Mapping

| Kotlin Coroutines | Swift Concurrency | Notes |
|-------------------|-------------------|-------|
| `suspend fun` | `async func` | Direct equivalent |
| `launch { }` | `Task { }` | Unstructured task |
| `async { }` | `async let` | Concurrent child |
| `coroutineScope { }` | `withTaskGroup` | Structured concurrency |
| `supervisorScope { }` | `withThrowingTaskGroup` + error handling | Error isolation |
| `withContext(Dispatchers.Main)` | `@MainActor` | Main thread |
| `withContext(Dispatchers.IO)` | Default async context | Cooperative pool |
| `Dispatchers.Default` | Default async context | CPU-bound work |
| `delay(ms)` | `Task.sleep(for:)` | Suspending delay |
| `yield()` | `Task.yield()` | Cooperative yielding |
| `isActive` | `Task.isCancelled` | Cancellation check |
| `ensureActive()` | `try Task.checkCancellation()` | Throw if cancelled |
| `Mutex` | `actor` | Thread-safe state |
| `Channel` | `AsyncStream` | Async communication |
| `Job` | `Task` | Task handle |

### Step 2: Suspend Function Translation

**Kotlin (suspend functions):**
```kotlin
class UserService(private val api: UserApi) {

    // Simple suspend
    suspend fun getUser(id: String): User {
        return api.getUser(id).toDomain()
    }

    // Concurrent execution
    suspend fun getUserWithPosts(id: String): UserWithPosts {
        return coroutineScope {
            val user = async { api.getUser(id) }
            val posts = async { api.getUserPosts(id) }
            UserWithPosts(
                user = user.await().toDomain(),
                posts = posts.await().map { it.toDomain() }
            )
        }
    }

    // Sequential with error handling
    suspend fun syncUser(id: String): Result<User> {
        return withContext(Dispatchers.IO) {
            try {
                val remote = api.getUser(id)
                db.upsert(remote.toEntity())
                Result.success(remote.toDomain())
            } catch (e: CancellationException) {
                throw e // Always rethrow cancellation
            } catch (e: Exception) {
                Result.failure(e)
            }
        }
    }
}
```

**Swift (async functions):**
```swift
final class UserService: Sendable {
    private let api: any UserAPIService

    init(api: any UserAPIService) {
        self.api = api
    }

    // Simple async
    func getUser(id: String) async throws -> User {
        let response = try await api.getUser(id: id)
        return response.toDomain()
    }

    // Concurrent execution — async let
    func getUserWithPosts(id: String) async throws -> UserWithPosts {
        async let user = api.getUser(id: id)
        async let posts = api.getUserPosts(id: id)
        return try await UserWithPosts(
            user: user.toDomain(),
            posts: posts.map { $0.toDomain() }
        )
    }

    // Sequential with error handling
    func syncUser(id: String) async -> Result<User, Error> {
        do {
            let remote = try await api.getUser(id: id)
            try await db.upsert(remote.toEntity())
            return .success(remote.toDomain())
        } catch is CancellationError {
            return .failure(CancellationError())
        } catch {
            return .failure(error)
        }
    }
}
```

### Step 3: Flow to AsyncSequence

**Kotlin (Flow patterns):**
```kotlin
class SearchViewModel @Inject constructor(
    private val searchRepository: SearchRepository
) : ViewModel() {

    private val _query = MutableStateFlow("")

    val results: StateFlow<SearchState> = _query
        .debounce(300)
        .distinctUntilChanged()
        .flatMapLatest { query ->
            if (query.isBlank()) {
                flowOf(SearchState.Empty)
            } else {
                searchRepository.search(query)
                    .map { SearchState.Success(it) as SearchState }
                    .onStart { emit(SearchState.Loading) }
                    .catch { emit(SearchState.Error(it.message)) }
            }
        }
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), SearchState.Empty)

    fun updateQuery(query: String) {
        _query.value = query
    }
}

// Flow emission
class SearchRepository {
    fun search(query: String): Flow<List<SearchResult>> = flow {
        val results = api.search(query)
        emit(results.map { it.toDomain() })
    }
}
```

**Swift (AsyncSequence equivalent):**
```swift
@Observable
final class SearchViewModel {
    private(set) var state: SearchState = .empty
    var query: String = "" {
        didSet { searchTask?.cancel(); startSearch() }
    }

    private var searchTask: Task<Void, Never>?
    private let searchRepository: any SearchRepositoryProtocol

    init(searchRepository: any SearchRepositoryProtocol) {
        self.searchRepository = searchRepository
    }

    private func startSearch() {
        searchTask = Task { @MainActor [weak self] in
            guard let self else { return }
            let currentQuery = query

            // Debounce
            try? await Task.sleep(for: .milliseconds(300))
            guard !Task.isCancelled, query == currentQuery else { return }

            if currentQuery.isEmpty {
                state = .empty
                return
            }

            state = .loading
            do {
                let results = try await searchRepository.search(query: currentQuery)
                guard !Task.isCancelled else { return }
                state = .success(results)
            } catch is CancellationError {
                // Ignore — new search superseded this one
            } catch {
                state = .error(error.localizedDescription)
            }
        }
    }
}

// AsyncStream for continuous emission (equivalent to Flow)
class SearchRepository: SearchRepositoryProtocol {
    func observeSearchResults(query: String) -> AsyncStream<[SearchResult]> {
        AsyncStream { continuation in
            let task = Task {
                // Initial results
                let results = try? await api.search(query: query)
                continuation.yield(results?.map { $0.toDomain() } ?? [])

                // Real-time updates via WebSocket or polling
                for await update in realtimeUpdates(query: query) {
                    continuation.yield(update)
                }
                continuation.finish()
            }
            continuation.onTermination = { _ in task.cancel() }
        }
    }
}
```

### Step 4: CoroutineScope to Task Management

**Kotlin (scope management):**
```kotlin
class DataSyncManager(private val scope: CoroutineScope) {

    private var syncJob: Job? = null

    fun startPeriodicSync() {
        syncJob = scope.launch {
            while (isActive) {
                try {
                    syncAllData()
                } catch (e: CancellationException) {
                    throw e
                } catch (e: Exception) {
                    logger.error("Sync failed", e)
                }
                delay(15.minutes.inWholeMilliseconds)
            }
        }
    }

    fun stopSync() {
        syncJob?.cancel()
    }

    // Parallel sync with SupervisorJob
    private suspend fun syncAllData() = supervisorScope {
        val jobs = listOf(
            async { syncUsers() },
            async { syncPosts() },
            async { syncComments() }
        )
        jobs.forEach { it.await() } // One failure doesn't cancel others
    }
}
```

**Swift (Task management):**
```swift
actor DataSyncManager {
    private var syncTask: Task<Void, Never>?

    func startPeriodicSync() {
        syncTask = Task { [weak self] in
            while !Task.isCancelled {
                do {
                    try await self?.syncAllData()
                } catch is CancellationError {
                    break
                } catch {
                    Logger.sync.error("Sync failed: \(error)")
                }
                try? await Task.sleep(for: .seconds(900))
            }
        }
    }

    func stopSync() {
        syncTask?.cancel()
    }

    // Parallel sync with error isolation (SupervisorJob equivalent)
    private func syncAllData() async throws {
        await withTaskGroup(of: Result<Void, Error>.self) { group in
            group.addTask { await Result { try await self.syncUsers() } }
            group.addTask { await Result { try await self.syncPosts() } }
            group.addTask { await Result { try await self.syncComments() } }

            for await result in group {
                if case .failure(let error) = result {
                    Logger.sync.error("Partial sync failed: \(error)")
                }
            }
        }
    }
}
```

### Step 5: Dispatcher to Actor Mapping

| Kotlin Dispatcher | Swift Equivalent | When to Use |
|-------------------|-----------------|-------------|
| `Dispatchers.Main` | `@MainActor` | UI updates |
| `Dispatchers.Main.immediate` | `@MainActor` (already on main) | Avoid dispatch if already on main |
| `Dispatchers.IO` | Default async context | Network, file I/O |
| `Dispatchers.Default` | Default async context | CPU-bound computation |
| `Dispatchers.Unconfined` | `nonisolated` | No specific thread |
| Custom dispatcher | Custom `SerialExecutor` | Custom thread pool |

## Expected Output

1. **Concept mapping table** for all Coroutine patterns used
2. **Translated async functions** for all suspend functions
3. **Stream patterns** replacing Flow with AsyncSequence/AsyncStream
4. **Task management** patterns for scoped and unscoped work
5. **Actor definitions** for thread-safe mutable state

## Example Interaction

**User:** Our app uses `viewModelScope.launch`, `StateFlow` in 8 ViewModels, `Flow` from Room DAOs, and `supervisorScope` for parallel network requests.

**Assistant:**

| Pattern | Count | Kotlin | Swift |
|---------|-------|--------|-------|
| ViewModel scope launch | 8 | `viewModelScope.launch` | `.task` modifier in SwiftUI |
| StateFlow observation | 8 | `collectAsState()` | `@Observable` properties |
| Room Flow queries | ~15 | `Flow<List<T>>` from DAO | `@Query` macro or `AsyncStream` |
| Supervisor scope | 2 | `supervisorScope { async {} }` | `withTaskGroup` + `Result` wrapping |

## Techniques Used

| Technique | Application |
|-----------|-------------|
| **ST-01: Structured Task Decomposition** | Pattern-by-pattern migration approach |
| **ST-02: Systematic Analysis Framework** | Exhaustive concept mapping tables |
| **RT-02: Contextual Reference Integration** | Coroutines and Swift Concurrency documentation |
| **DS-02: Output Specification Framework** | Translated code, mapping tables |

## Related Prompts

- `migration_architecture_adaptation.md` — ViewModel and repository async patterns
- `migration_room_to_core_data.md` — Flow observation from database
- `migration_retrofit_to_urlsession.md` — Async networking patterns
- `migration_kmp_shared_module_design.md` — SKIE for Coroutines interop

## Customization Guide

- **Combine:** If the team prefers Combine over Swift Concurrency for reactive streams, map Flow to Combine publishers instead of AsyncSequence.
- **RxSwift:** For teams coming from RxKotlin/RxJava, RxSwift provides the most familiar reactive API.
- **Older iOS (pre-16):** For iOS 15, use `Task {}` but note some APIs (like `AsyncStream.makeStream`) require iOS 17+.
- **KMP with SKIE:** If sharing Coroutines code via KMP, SKIE generates Swift async/await wrappers automatically — reducing manual translation.
