---
title: "Android Coroutine Scope & Memory Leak Review"
category: mobile/android/targeted-reviews
description: "Android Coroutine Scope & Memory Leak Review."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - coroutine
  - mobile
  - review
  - reviews
  - scope
updated: "2026-03-19"
related_prompts: []
---

# Android Coroutine Scope & Memory Leak Review

**Objective:** Conduct a targeted review of coroutine usage in Android applications, analyzing scope management, lifecycle awareness, structured concurrency, cancellation handling, and potential memory leaks from improper coroutine usage.

**When to Use:** Use this prompt when investigating memory leaks, before releasing features with heavy async work, when users report battery drain or slow performance, during architecture review of ViewModel/Repository layers, or when refactoring from RxJava to coroutines.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the actual scope lifecycle** - Don't flag based on pattern matching alone. Verify that the suspected scope issue actually causes leaks or improper behavior.
2. **Check for existing lifecycle handling** - Search for `onCleared()`, `onDestroy()`, cancellation calls, or DisposableEffect that may handle cleanup.
3. **Understand the context** - Consider WHY the code uses specific scope patterns. Some use cases legitimately require GlobalScope or custom scopes.
4. **Confirm actual memory leak** - Use LeakCanary or heap dumps to verify suspected leaks, not just code patterns.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `UserRepository.kt:78`).

**Finding NO issues is an acceptable outcome.** If coroutine scopes are properly managed, say so with confidence. Don't manufacture leak warnings.

### False-Positive Prevention

- ❌ Do NOT flag `viewModelScope` as a leak risk (it's lifecycle-aware by design)
- ❌ Do NOT flag all `GlobalScope` usage as wrong without checking if it's appropriate (e.g., application-level operations)
- ❌ Do NOT assume missing cancellation without searching the codebase
- ❌ Do NOT report scope issues without verifying actual impact
- ✅ DO verify that suspected leaks actually hold references to Activity/Fragment
- ✅ DO understand that `repeatOnLifecycle` handles Flow collection correctly
- ✅ DO check for SupervisorJob patterns in error handling scenarios
- ✅ DO consider whether the operation genuinely needs to outlive the component

---

### 1. Scope Definition Analysis

Analyze how coroutine scopes are defined:

* **ViewModel Scopes:**
  - Review viewModelScope usage patterns
  - Check for custom scope creation in ViewModels
  - Assess SupervisorJob usage for failure isolation
  - Verify scope cancellation on ViewModel clearing

* **Lifecycle Scopes:**
  - Review lifecycleScope usage in Activities/Fragments
  - Check repeatOnLifecycle patterns
  - Assess Lifecycle.State usage (STARTED vs RESUMED)
  - Verify flowWithLifecycle usage

* **Custom Scopes:**
  - Review manually created CoroutineScope instances
  - Check for proper Job hierarchy
  - Assess scope lifetime management
  - Verify cancellation on component destruction

* **Global Scopes (Anti-pattern):**
  - Check for GlobalScope usage (critical issue)
  - Review MainScope without proper management
  - Assess unscoped coroutine launches
  - Identify fire-and-forget patterns

### 2. Structured Concurrency

Evaluate structured concurrency compliance:

* **Parent-Child Relationships:**
  - Review coroutine hierarchy
  - Check for detached coroutines
  - Assess exception propagation
  - Verify cancellation propagation

* **Coroutine Builders:**
  - Review launch vs async usage
  - Check for proper await() calls
  - Assess runBlocking usage (should be rare)
  - Verify withContext for thread switching

* **Supervisor Patterns:**
  - Review SupervisorJob usage
  - Check supervisorScope for independent children
  - Assess failure isolation needs
  - Verify one child failure doesn't cancel siblings

### 3. Cancellation Handling

Analyze cancellation behavior:

* **Cancellation Cooperation:**
  - Check for isActive checks in loops
  - Review ensureActive() usage
  - Assess yield() for cooperative cancellation
  - Verify long-running operations are cancellable

* **Cancellation Exceptions:**
  - Review CancellationException handling
  - Check for swallowed cancellation
  - Assess cleanup in finally blocks
  - Verify NonCancellable for cleanup operations

* **Timeout Handling:**
  - Review withTimeout/withTimeoutOrNull usage
  - Check for proper timeout exception handling
  - Assess retry logic with timeouts
  - Verify timeout values are appropriate

### 4. Memory Leak Patterns

Identify common memory leak sources:

* **Captured References:**
  - Check for Activity/Fragment captures in lambdas
  - Review View references in coroutines
  - Assess Context references (prefer applicationContext)
  - Verify no implicit this captures

* **Long-Running Operations:**
  - Review operations that outlive components
  - Check for proper scope association
  - Assess fire-and-forget patterns
  - Verify cleanup on configuration changes

* **Callback Leaks:**
  - Check for listener registration without deregistration
  - Review callback-to-coroutine bridges
  - Assess suspendCancellableCoroutine usage
  - Verify invokeOnCancellation cleanup

* **Flow Collection Leaks:**
  - Review Flow collection lifecycle
  - Check for terminal operators without lifecycle
  - Assess shareIn/stateIn scope usage
  - Verify launchIn scope selection

### 5. Dispatcher Usage

Evaluate dispatcher selection:

* **Main Dispatcher:**
  - Check UI operations on Main
  - Review Main.immediate usage
  - Assess unnecessary dispatcher switches
  - Verify short operations on Main

* **IO Dispatcher:**
  - Review blocking I/O operations
  - Check for proper IO dispatcher usage
  - Assess thread pool exhaustion risks
  - Verify database operations on IO

* **Default Dispatcher:**
  - Review CPU-intensive operations
  - Check for proper Default usage
  - Assess parallel processing needs
  - Verify no blocking on Default

* **Custom Dispatchers:**
  - Review limitedParallelism usage
  - Check for custom executor-based dispatchers
  - Assess single-threaded dispatcher needs
  - Verify dispatcher lifecycle management

### 6. Flow Lifecycle Management

Analyze Flow collection patterns:

* **Collection in UI:**
  - Review collectAsStateWithLifecycle usage
  - Check for proper Compose collection
  - Assess View-based collection patterns
  - Verify no leaking collectors

* **SharedFlow/StateFlow:**
  - Review sharing scope selection
  - Check SharingStarted strategy
  - Assess replay configuration
  - Verify WhileSubscribed timeout

* **Hot Flow Lifecycle:**
  - Check for proper hot flow cancellation
  - Review channel-based flows
  - Assess callbackFlow lifecycle
  - Verify awaitClose cleanup

### 7. Exception Handling

Evaluate error handling patterns:

* **CoroutineExceptionHandler:**
  - Review global exception handlers
  - Check for proper handler installation
  - Assess crash reporting integration
  - Verify uncaught exception behavior

* **try-catch Patterns:**
  - Review exception handling in coroutines
  - Check for proper exception propagation
  - Assess Result type usage
  - Verify no silent failures

* **Supervisor Exception Isolation:**
  - Review exception isolation needs
  - Check SupervisorJob for UI coroutines
  - Assess one-failure-shouldn't-crash-all scenarios
  - Verify proper error UI display

### 8. Testing Considerations

Evaluate testability:

* **Dispatcher Injection:**
  - Check for injectable dispatchers
  - Review TestDispatcher usage
  - Assess runTest integration
  - Verify deterministic testing

* **Scope Injection:**
  - Review injectable scope patterns
  - Check for test scope replacement
  - Assess TestScope usage
  - Verify proper test cleanup

---

## Expected Output

Provide a comprehensive coroutine scope and memory leak review including:

### 1. Executive Summary
- Overall coroutine health rating
- Critical memory leak risks
- Structured concurrency compliance
- Test coverage for async code

### 2. Scope Analysis Matrix

| Component | Scope Used | Lifecycle Aware | Leak Risk | Issues |
|-----------|------------|-----------------|-----------|--------|
| [ViewModel] | [viewModelScope] | [Yes/No] | [Low/Medium/High] | [Count] |

### 3. Detailed Findings

For each issue:
- **Location:** Class/Function
- **Issue:** Description of problem
- **Impact:** Memory leak, crash risk, battery drain
- **Severity:** Critical/High/Medium/Low
- **Current Code:** Problematic pattern
- **Recommended Fix:** Correct implementation

### 4. Memory Leak Checklist

List of verified leak-free patterns vs. identified leak risks.

### 5. Prioritized Remediation

Ordered by severity and impact.

---

## Example Output

```markdown
# Coroutine Scope & Memory Leak Review

## Executive Summary
- **Overall Health:** Poor - Multiple memory leak patterns detected
- **GlobalScope Usage:** 3 instances (Critical)
- **Lifecycle Issues:** 8 collectors not lifecycle-aware
- **Cancellation:** 5 operations don't cooperate with cancellation
- **Test Coverage:** No TestDispatcher injection found

## Critical Findings

### CRITICAL-1: GlobalScope Usage Causes Memory Leaks
**Severity:** Critical
**Impact:** Activity/Fragment leaks, battery drain, crashes

**Location:** MessageRepository.kt

**Scenario:**
1. User opens chat screen
2. Message sync starts with GlobalScope
3. User navigates away
4. Sync continues holding Activity reference
5. Activity cannot be garbage collected

**Current Implementation:**
```kotlin
class MessageRepository @Inject constructor(
    private val messageDao: MessageDao,
    private val api: MessageApi,
    private val context: Context  // PROBLEM: Holds Activity context
) {
    // CRITICAL: GlobalScope never cancels!
    fun syncMessages(conversationId: String) {
        GlobalScope.launch {
            try {
                val messages = api.getMessages(conversationId)
                messageDao.insertAll(messages)

                // PROBLEM: Shows toast with leaked context
                withContext(Dispatchers.Main) {
                    Toast.makeText(context, "Synced", Toast.LENGTH_SHORT).show()
                }
            } catch (e: Exception) {
                Log.e("Sync", "Failed", e)
            }
        }
    }
}
```

**Recommended Fix:**
```kotlin
class MessageRepository @Inject constructor(
    private val messageDao: MessageDao,
    private val api: MessageApi,
    @ApplicationContext private val appContext: Context,  // Application context
    private val externalScope: CoroutineScope  // Injected scope
) {
    // Use injected scope with proper lifecycle
    fun syncMessages(conversationId: String): Job {
        return externalScope.launch {
            try {
                val messages = api.getMessages(conversationId)
                messageDao.insertAll(messages)
                // Toast via application context (no leak)
            } catch (e: CancellationException) {
                throw e  // Don't swallow cancellation!
            } catch (e: Exception) {
                Log.e("Sync", "Failed", e)
            }
        }
    }
}

// Provide application-scoped coroutine scope
@Module
@InstallIn(SingletonComponent::class)
object CoroutineScopeModule {

    @Provides
    @Singleton
    fun provideApplicationScope(): CoroutineScope {
        return CoroutineScope(
            SupervisorJob() + Dispatchers.Default +
            CoroutineExceptionHandler { _, throwable ->
                Log.e("AppScope", "Uncaught exception", throwable)
            }
        )
    }
}
```

---

### CRITICAL-2: Flow Collection Without Lifecycle
**Severity:** Critical
**Impact:** Updates after Fragment destroyed, crashes

**Location:** TodoListFragment.kt

**Current Implementation:**
```kotlin
class TodoListFragment : Fragment() {

    private val viewModel: TodoViewModel by viewModels()

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // PROBLEM: Collects forever, even after Fragment destroyed
        lifecycleScope.launch {
            viewModel.todos.collect { todos ->
                // Will crash if Fragment view is gone
                binding.recyclerView.adapter = TodoAdapter(todos)
            }
        }

        // PROBLEM: Also collects forever
        lifecycleScope.launch {
            viewModel.errors.collect { error ->
                Snackbar.make(binding.root, error, Snackbar.LENGTH_LONG).show()
            }
        }
    }
}
```

**Recommended Fix:**
```kotlin
class TodoListFragment : Fragment() {

    private val viewModel: TodoViewModel by viewModels()

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // CORRECT: repeatOnLifecycle respects Fragment lifecycle
        viewLifecycleOwner.lifecycleScope.launch {
            viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
                // Launch all collections in parallel
                launch {
                    viewModel.todos.collect { todos ->
                        binding.recyclerView.adapter = TodoAdapter(todos)
                    }
                }

                launch {
                    viewModel.errors.collect { error ->
                        Snackbar.make(binding.root, error, Snackbar.LENGTH_LONG).show()
                    }
                }
            }
        }
    }
}

// Alternative using flowWithLifecycle extension
viewLifecycleOwner.lifecycleScope.launch {
    viewModel.todos
        .flowWithLifecycle(viewLifecycleOwner.lifecycle, Lifecycle.State.STARTED)
        .collect { todos ->
            binding.recyclerView.adapter = TodoAdapter(todos)
        }
}
```

---

### HIGH-1: ViewModel Creates Detached Coroutines
**Severity:** High
**Impact:** Operations continue after ViewModel cleared

**Location:** SyncViewModel.kt

**Current Implementation:**
```kotlin
@HiltViewModel
class SyncViewModel @Inject constructor(
    private val syncRepository: SyncRepository
) : ViewModel() {

    // PROBLEM: Creates new scope, not tied to viewModelScope
    private val syncScope = CoroutineScope(Dispatchers.IO)

    fun startSync() {
        // PROBLEM: This scope is never cancelled!
        syncScope.launch {
            while (true) {
                syncRepository.performSync()
                delay(30.seconds)
            }
        }
    }

    override fun onCleared() {
        super.onCleared()
        // PROBLEM: syncScope not cancelled here
    }
}
```

**Recommended Fix:**
```kotlin
@HiltViewModel
class SyncViewModel @Inject constructor(
    private val syncRepository: SyncRepository
) : ViewModel() {

    private var syncJob: Job? = null

    fun startSync() {
        // Cancel previous sync if running
        syncJob?.cancel()

        // CORRECT: Use viewModelScope - automatically cancelled
        syncJob = viewModelScope.launch {
            while (isActive) {  // Check for cancellation
                try {
                    syncRepository.performSync()
                    delay(30.seconds)
                } catch (e: CancellationException) {
                    throw e  // Propagate cancellation
                } catch (e: Exception) {
                    // Handle error, maybe retry
                    delay(5.seconds)
                }
            }
        }
    }

    fun stopSync() {
        syncJob?.cancel()
        syncJob = null
    }

    // viewModelScope automatically cancelled in onCleared()
}
```

---

### HIGH-2: Captured Activity Reference in Lambda
**Severity:** High
**Impact:** Activity memory leak

**Location:** PhotoUploadService.kt

**Current Implementation:**
```kotlin
class PhotoUploadActivity : AppCompatActivity() {

    private val viewModel: PhotoUploadViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding.uploadButton.setOnClickListener {
            val uri = selectedPhotoUri ?: return@setOnClickListener

            // PROBLEM: Lambda captures 'this' (Activity)
            viewModel.uploadPhoto(uri) { progress ->
                // 'this' reference keeps Activity alive
                binding.progressBar.progress = progress
            }
        }
    }
}

@HiltViewModel
class PhotoUploadViewModel @Inject constructor(
    private val uploadRepository: UploadRepository
) : ViewModel() {

    // PROBLEM: Callback holds reference to Activity
    fun uploadPhoto(uri: Uri, onProgress: (Int) -> Unit) {
        viewModelScope.launch {
            uploadRepository.upload(uri).collect { progress ->
                withContext(Dispatchers.Main) {
                    onProgress(progress)  // Activity leaked!
                }
            }
        }
    }
}
```

**Recommended Fix:**
```kotlin
class PhotoUploadActivity : AppCompatActivity() {

    private val viewModel: PhotoUploadViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding.uploadButton.setOnClickListener {
            val uri = selectedPhotoUri ?: return@setOnClickListener
            viewModel.uploadPhoto(uri)
        }

        // CORRECT: Observe StateFlow with lifecycle awareness
        lifecycleScope.launch {
            repeatOnLifecycle(Lifecycle.State.STARTED) {
                viewModel.uploadProgress.collect { progress ->
                    binding.progressBar.progress = progress
                }
            }
        }
    }
}

@HiltViewModel
class PhotoUploadViewModel @Inject constructor(
    private val uploadRepository: UploadRepository
) : ViewModel() {

    // CORRECT: Expose state, don't accept callbacks
    private val _uploadProgress = MutableStateFlow(0)
    val uploadProgress: StateFlow<Int> = _uploadProgress.asStateFlow()

    fun uploadPhoto(uri: Uri) {
        viewModelScope.launch {
            uploadRepository.upload(uri).collect { progress ->
                _uploadProgress.value = progress
            }
        }
    }
}
```

---

### HIGH-3: callbackFlow Without Proper Cleanup
**Severity:** High
**Impact:** Listener leak, continued callbacks after cancellation

**Location:** LocationRepository.kt

**Current Implementation:**
```kotlin
class LocationRepository @Inject constructor(
    private val fusedLocationClient: FusedLocationProviderClient
) {
    // PROBLEM: No cleanup when flow is cancelled
    fun observeLocation(): Flow<Location> = callbackFlow {
        val callback = object : LocationCallback() {
            override fun onLocationResult(result: LocationResult) {
                result.lastLocation?.let { trySend(it) }
            }
        }

        val request = LocationRequest.Builder(
            Priority.PRIORITY_HIGH_ACCURACY, 10_000
        ).build()

        fusedLocationClient.requestLocationUpdates(
            request, callback, Looper.getMainLooper()
        )

        // PROBLEM: Missing awaitClose!
        // Callback is never removed when Flow is cancelled
    }
}
```

**Recommended Fix:**
```kotlin
class LocationRepository @Inject constructor(
    private val fusedLocationClient: FusedLocationProviderClient
) {
    @RequiresPermission(anyOf = [
        Manifest.permission.ACCESS_FINE_LOCATION,
        Manifest.permission.ACCESS_COARSE_LOCATION
    ])
    fun observeLocation(): Flow<Location> = callbackFlow {
        val callback = object : LocationCallback() {
            override fun onLocationResult(result: LocationResult) {
                result.lastLocation?.let { location ->
                    trySend(location).isSuccess  // Handle backpressure
                }
            }
        }

        val request = LocationRequest.Builder(
            Priority.PRIORITY_HIGH_ACCURACY, 10_000
        ).build()

        fusedLocationClient.requestLocationUpdates(
            request, callback, Looper.getMainLooper()
        )

        // CRITICAL: Clean up when Flow is cancelled
        awaitClose {
            fusedLocationClient.removeLocationUpdates(callback)
        }
    }.shareIn(
        scope = externalScope,
        started = SharingStarted.WhileSubscribed(5000),
        replay = 1
    )
}
```

---

### MEDIUM-1: Non-Cooperative Long Operation
**Severity:** Medium
**Impact:** Delayed cancellation, resource waste

**Location:** ImageProcessingUseCase.kt

**Current Implementation:**
```kotlin
class ImageProcessingUseCase @Inject constructor() {

    suspend fun processImages(images: List<Uri>): List<ProcessedImage> {
        return images.map { uri ->
            // PROBLEM: No cancellation check in long loop
            processImage(uri)
        }
    }

    private suspend fun processImage(uri: Uri): ProcessedImage {
        // Long-running operation without cancellation cooperation
        val bitmap = loadBitmap(uri)  // Blocking
        val resized = resizeBitmap(bitmap)  // CPU intensive
        val compressed = compressBitmap(resized)  // CPU intensive
        return ProcessedImage(compressed)
    }
}
```

**Recommended Fix:**
```kotlin
class ImageProcessingUseCase @Inject constructor() {

    suspend fun processImages(images: List<Uri>): List<ProcessedImage> {
        return withContext(Dispatchers.Default) {
            images.map { uri ->
                // CORRECT: Check for cancellation between items
                ensureActive()
                processImage(uri)
            }
        }
    }

    private suspend fun processImage(uri: Uri): ProcessedImage {
        return withContext(Dispatchers.Default) {
            // Check cancellation between expensive operations
            ensureActive()
            val bitmap = loadBitmap(uri)

            ensureActive()
            val resized = resizeBitmap(bitmap)

            ensureActive()
            val compressed = compressBitmap(resized)

            ProcessedImage(compressed)
        }
    }

    // Alternative: Use yield() for cooperative multitasking
    private suspend fun processManyImages(images: List<Uri>): List<ProcessedImage> {
        return images.map { uri ->
            yield()  // Allow cancellation and other coroutines to run
            processImage(uri)
        }
    }
}
```

---

### MEDIUM-2: Swallowed CancellationException
**Severity:** Medium
**Impact:** Coroutine doesn't cancel properly, resource leaks

**Location:** DataSyncUseCase.kt

**Current Implementation:**
```kotlin
class DataSyncUseCase @Inject constructor(
    private val api: DataApi,
    private val database: AppDatabase
) {
    suspend fun sync(): Result<Unit> {
        return try {
            val data = api.fetchData()
            database.save(data)
            Result.success(Unit)
        } catch (e: Exception) {
            // PROBLEM: Catches ALL exceptions including CancellationException!
            Log.e("Sync", "Sync failed", e)
            Result.failure(e)
        }
    }
}
```

**Recommended Fix:**
```kotlin
class DataSyncUseCase @Inject constructor(
    private val api: DataApi,
    private val database: AppDatabase
) {
    suspend fun sync(): Result<Unit> {
        return try {
            val data = api.fetchData()
            database.save(data)
            Result.success(Unit)
        } catch (e: CancellationException) {
            // CRITICAL: Always rethrow CancellationException!
            throw e
        } catch (e: Exception) {
            Log.e("Sync", "Sync failed", e)
            Result.failure(e)
        }
    }

    // Alternative: Use runCatching with proper handling
    suspend fun syncSafe(): Result<Unit> = runCatching {
        val data = api.fetchData()
        database.save(data)
    }.onFailure { e ->
        if (e is CancellationException) throw e
        Log.e("Sync", "Sync failed", e)
    }
}
```

---

### MEDIUM-3: SharedFlow Without Proper Scope
**Severity:** Medium
**Impact:** Hot flow lives forever, memory not reclaimed

**Location:** EventBus.kt

**Current Implementation:**
```kotlin
// PROBLEM: Global object with never-cancelled SharedFlow
object EventBus {
    // Lives forever, all subscribers hold references
    private val _events = MutableSharedFlow<Event>(
        replay = 10,
        extraBufferCapacity = 100
    )
    val events: SharedFlow<Event> = _events.asSharedFlow()

    suspend fun emit(event: Event) {
        _events.emit(event)
    }
}
```

**Recommended Fix:**
```kotlin
// CORRECT: Inject scoped event bus
@Singleton
class EventBus @Inject constructor(
    @ApplicationScope private val scope: CoroutineScope
) {
    private val _events = MutableSharedFlow<Event>(
        replay = 0,  // Don't replay by default
        extraBufferCapacity = 64,
        onBufferOverflow = BufferOverflow.DROP_OLDEST
    )

    val events: SharedFlow<Event> = _events
        .shareIn(
            scope = scope,
            started = SharingStarted.WhileSubscribed(5000),
            replay = 0
        )

    fun emit(event: Event) {
        scope.launch {
            _events.emit(event)
        }
    }
}

// Or for truly global events, use proper lifecycle
@Module
@InstallIn(SingletonComponent::class)
object EventModule {

    @Provides
    @Singleton
    fun provideEventBus(
        @ApplicationScope scope: CoroutineScope
    ): EventBus = EventBus(scope)
}
```

---

## Scope Usage Matrix

| Component | Scope | Lifecycle Tied | Cancellation | Status |
|-----------|-------|----------------|--------------|--------|
| MessageRepository | GlobalScope | ❌ No | ❌ Never | Critical |
| TodoListFragment | lifecycleScope | ⚠️ Partial | ⚠️ Wrong | Critical |
| SyncViewModel | Custom scope | ❌ No | ❌ Manual | High |
| PhotoUploadViewModel | viewModelScope | ✅ Yes | ✅ Auto | OK |
| LocationRepository | callbackFlow | ❌ No cleanup | ❌ Leak | High |
| ImageProcessingUseCase | (caller) | N/A | ⚠️ Non-coop | Medium |
| EventBus | None (object) | ❌ Forever | ❌ Never | Medium |
| DatabaseRepository | viewModelScope | ✅ Yes | ✅ Auto | OK |

## Test Coverage Issues

### Missing Test Infrastructure
```kotlin
// PROBLEM: No dispatcher injection for testing
class MyViewModel(
    private val repository: Repository
) : ViewModel() {
    fun load() {
        viewModelScope.launch {
            // Uses Dispatchers.Main - can't test!
            _state.value = repository.getData()
        }
    }
}

// CORRECT: Injectable dispatchers
class MyViewModel(
    private val repository: Repository,
    private val dispatcher: CoroutineDispatcher = Dispatchers.Main
) : ViewModel() {
    fun load() {
        viewModelScope.launch(dispatcher) {
            _state.value = repository.getData()
        }
    }
}

// Test
@Test
fun `load updates state`() = runTest {
    val viewModel = MyViewModel(
        repository = fakeRepository,
        dispatcher = UnconfinedTestDispatcher(testScheduler)
    )

    viewModel.load()

    assertEquals(expected, viewModel.state.value)
}
```

## Remediation Priority

### Critical (Immediate)
1. Replace all GlobalScope with injected CoroutineScope
2. Add repeatOnLifecycle to all Fragment/Activity Flow collectors
3. Cancel custom scopes in onCleared/onDestroy

### High Priority (This Sprint)
1. Add awaitClose to all callbackFlow implementations
2. Remove captured Activity/Fragment references from lambdas
3. Expose StateFlow instead of accepting callbacks

### Medium Priority (Next Sprint)
1. Add ensureActive() checks in long loops
2. Properly handle CancellationException (don't swallow)
3. Inject dispatchers for testability
4. Review SharedFlow scopes and lifetimes

### Low Priority (Backlog)
1. Add CoroutineExceptionHandler for crash reporting
2. Document coroutine patterns in architecture docs
3. Add lint rules for GlobalScope usage
4. Create testing utilities for coroutine code
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Coroutine and memory focus
- **ST-02** (Structured Sequential Instructions) - Systematic analysis
- **RT-02** (Multi-Dimensional Analysis) - Scope, lifecycle, cancellation
- **RT-05** (Evidence-Based Reasoning) - Code examples
- **ST-03** (Output Format Templates) - Scope matrix
- **DS-06** (Prioritization Guidance) - Severity-based ordering
- **QA-02** (Edge Case Coverage) - Various leak scenarios

---

## Related Prompts

- `android_viewmodel_state_management_review.md` - For ViewModel patterns
- `android_compose_recomposition_review.md` - For Compose state
- `android_hilt_di_scope_review.md` - For DI scope patterns
- `android_workmanager_background_review.md` - For background work
- `testing_unit_test_generation.md` - For coroutine testing

---

## Customization Guide

- **For Retrofit/Network Heavy Apps:** Focus on API cancellation, timeout handling
- **For Realtime Apps:** Focus on WebSocket lifecycle, connection management
- **For Media Apps:** Focus on ExoPlayer scope, playback lifecycle
- **For Background Processing:** Focus on WorkManager coroutine integration
- **For Multi-Module Apps:** Focus on shared scope patterns, module boundaries
