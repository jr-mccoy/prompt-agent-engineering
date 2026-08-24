# Fix Pattern Library for Android Behavioral Issues

Concrete implementation patterns for the most common behavioral fixes in Android apps. Each pattern includes the before/after code and testing approach.

## Error Notification Fixes

### Fix: Silent Exception to User-Visible Error

**Before (silent failure):**
```kotlin
fun saveItem(item: Item) {
    viewModelScope.launch {
        try {
            repository.save(item)
        } catch (e: Exception) {
            Log.e(TAG, "Save failed", e)
        }
    }
}
```

**After (user notified):**
```kotlin
fun saveItem(item: Item) {
    viewModelScope.launch {
        try {
            repository.save(item)
            _uiState.update { it.copy(saveSuccess = true) }
        } catch (e: Exception) {
            Log.e(TAG, "Save failed", e)
            _uiState.update { it.copy(error = "Failed to save. Please try again.") }
        }
    }
}
```

**Test approach:**
```kotlin
@Test
fun `saveItem failure shows error in UI state`() = runTest {
    repository.setShouldFail(true)
    viewModel.saveItem(testItem)
    assertNotNull(viewModel.uiState.value.error)
}
```

---

### Fix: Differentiated Error Messages

**Before (generic error):**
```kotlin
catch (e: Exception) {
    _uiState.update { it.copy(error = "Something went wrong") }
}
```

**After (specific errors):**
```kotlin
catch (e: IOException) {
    _uiState.update { it.copy(error = "No internet connection. Please check your network.") }
} catch (e: HttpException) {
    _uiState.update { it.copy(error = "Server error. Please try again later.") }
} catch (e: Exception) {
    if (e is CancellationException) throw e
    _uiState.update { it.copy(error = "Unexpected error. Please try again.") }
}
```

## Lifecycle Fixes

### Fix: Firebase Listener Cleanup

**Before (leaked listener):**
```kotlin
class ChatViewModel @Inject constructor(
    private val database: FirebaseDatabase
) : ViewModel() {
    private val messagesRef = database.child("messages")

    init {
        messagesRef.addValueEventListener(object : ValueEventListener {
            override fun onDataChange(snapshot: DataSnapshot) {
                _messages.value = snapshot.toMessages()
            }
            override fun onCancelled(error: DatabaseError) {
                Log.e(TAG, "Listener cancelled", error.toException())
            }
        })
    }
}
```

**After (proper lifecycle management):**
```kotlin
class ChatViewModel @Inject constructor(
    private val database: FirebaseDatabase
) : ViewModel() {
    private val messagesRef = database.child("messages")
    private var messageListener: ValueEventListener? = null

    init {
        messageListener = object : ValueEventListener {
            override fun onDataChange(snapshot: DataSnapshot) {
                _messages.value = snapshot.toMessages()
            }
            override fun onCancelled(error: DatabaseError) {
                Log.e(TAG, "Listener cancelled", error.toException())
            }
        }
        messagesRef.addValueEventListener(messageListener!!)
    }

    override fun onCleared() {
        super.onCleared()
        messageListener?.let { messagesRef.removeEventListener(it) }
    }
}
```

**Alternative (callbackFlow approach — preferred):**
```kotlin
private fun observeMessages(): Flow<List<Message>> = callbackFlow {
    val listener = object : ValueEventListener {
        override fun onDataChange(snapshot: DataSnapshot) {
            trySend(snapshot.toMessages())
        }
        override fun onCancelled(error: DatabaseError) {
            close(error.toException())
        }
    }
    messagesRef.addValueEventListener(listener)
    awaitClose { messagesRef.removeEventListener(listener) }
}
```

### Fix: Process Death State Preservation

**Before (state lost on process death):**
```kotlin
class EditViewModel @Inject constructor() : ViewModel() {
    private val _draftTitle = MutableStateFlow("")
    val draftTitle: StateFlow<String> = _draftTitle.asStateFlow()

    fun updateTitle(title: String) {
        _draftTitle.value = title
    }
}
```

**After (state preserved with SavedStateHandle):**
```kotlin
class EditViewModel @Inject constructor(
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {
    val draftTitle: StateFlow<String> = savedStateHandle.getStateFlow("draftTitle", "")

    fun updateTitle(title: String) {
        savedStateHandle["draftTitle"] = title
    }
}
```

## Navigation Fixes

### Fix: Deep Link Back Stack Reconstruction

**Before (dead end after deep link):**
```kotlin
composable("item/{itemId}",
    deepLinks = listOf(navDeepLink { uriPattern = "app://item/{itemId}" })
) {
    ItemDetailScreen(
        onBack = { navController.popBackStack() }  // Fails if back stack is empty
    )
}
```

**After (back stack reconstructed):**
```kotlin
composable("item/{itemId}",
    deepLinks = listOf(navDeepLink { uriPattern = "app://item/{itemId}" })
) {
    ItemDetailScreen(
        onBack = {
            if (!navController.popBackStack()) {
                navController.navigate("home") {
                    popUpTo(navController.graph.startDestinationId) { inclusive = true }
                }
            }
        }
    )
}
```

### Fix: Auth Gate on Protected Screens

**Before (unprotected screen):**
```kotlin
composable("profile") {
    ProfileScreen(viewModel = hiltViewModel())
}
```

**After (auth-gated):**
```kotlin
composable("profile") {
    val authState by authViewModel.authState.collectAsStateWithLifecycle()
    when (authState) {
        is AuthState.Authenticated -> ProfileScreen(viewModel = hiltViewModel())
        is AuthState.Unauthenticated -> {
            LaunchedEffect(Unit) {
                navController.navigate("login") {
                    popUpTo("profile") { inclusive = true }
                }
            }
        }
        is AuthState.Loading -> LoadingIndicator()
    }
}
```

### Fix: Back Stack Duplication Prevention

**Before (duplicate screens on back stack):**
```kotlin
navController.navigate("home")
```

**After (single top, clean back stack):**
```kotlin
navController.navigate("home") {
    popUpTo(navController.graph.startDestinationId) { saveState = true }
    launchSingleTop = true
    restoreState = true
}
```

## Coroutine Fixes

### Fix: CancellationException Rethrow

**Before (cancellation swallowed):**
```kotlin
suspend fun <T> safeCall(block: suspend () -> T): Result<T> {
    return try {
        Result.success(block())
    } catch (e: Exception) {
        Result.failure(e)
    }
}
```

**After (cancellation respected):**
```kotlin
suspend fun <T> safeCall(block: suspend () -> T): Result<T> {
    return try {
        Result.success(block())
    } catch (e: CancellationException) {
        throw e
    } catch (e: Exception) {
        Result.failure(e)
    }
}
```

### Fix: Double-Tap Protection

**Before (no protection against rapid taps):**
```kotlin
fun onSubmitClicked() {
    viewModelScope.launch {
        repository.submit(data)  // Called twice on double-tap
    }
}
```

**After (debounced submission):**
```kotlin
private var submitJob: Job? = null

fun onSubmitClicked() {
    if (submitJob?.isActive == true) return
    submitJob = viewModelScope.launch {
        _uiState.update { it.copy(isSubmitting = true) }
        try {
            repository.submit(data)
        } finally {
            _uiState.update { it.copy(isSubmitting = false) }
        }
    }
}
```

## Data Integrity Fixes

### Fix: Transaction for Related Writes

**Before (non-atomic writes):**
```kotlin
@Dao
interface ItemDao {
    @Insert
    suspend fun insertItem(item: ItemEntity)

    @Insert
    suspend fun insertTags(tags: List<TagEntity>)
}

// Usage: two separate operations, could fail between them
dao.insertItem(item)
dao.insertTags(tags)
```

**After (atomic transaction):**
```kotlin
@Dao
abstract class ItemDao {
    @Insert
    abstract suspend fun insertItem(item: ItemEntity)

    @Insert
    abstract suspend fun insertTags(tags: List<TagEntity>)

    @Transaction
    open suspend fun insertItemWithTags(item: ItemEntity, tags: List<TagEntity>) {
        insertItem(item)
        insertTags(tags)
    }
}
```

### Fix: Conflict Strategy Correction

**Before (REPLACE overwrites all fields):**
```kotlin
@Insert(onConflict = OnConflictStrategy.REPLACE)
suspend fun upsertItem(item: ItemEntity)
```

**After (explicit upsert preserving fields):**
```kotlin
@Insert(onConflict = OnConflictStrategy.IGNORE)
suspend fun insertItem(item: ItemEntity): Long

@Update
suspend fun updateItem(item: ItemEntity)

@Transaction
open suspend fun upsertItem(item: ItemEntity) {
    val id = insertItem(item)
    if (id == -1L) {
        updateItem(item)
    }
}
```

## State Machine Fixes

### Fix: Add Error State Recovery

**Before (no recovery from error state):**
```kotlin
sealed class UiState {
    object Loading : UiState()
    data class Success(val data: List<Item>) : UiState()
    data class Error(val message: String) : UiState()
}

// Error state has no way out — no retry, no dismiss
```

**After (recoverable error state):**
```kotlin
sealed class UiState {
    object Loading : UiState()
    data class Success(val data: List<Item>) : UiState()
    data class Error(val message: String) : UiState()
}

// In ViewModel:
fun retry() {
    _uiState.value = UiState.Loading
    loadData()
}

fun dismissError() {
    _uiState.value = UiState.Success(emptyList())  // or previous data
}
```

**In UI:**
```kotlin
is UiState.Error -> {
    ErrorView(
        message = state.message,
        onRetry = { viewModel.retry() },
        onDismiss = { viewModel.dismissError() }
    )
}
```

## WorkManager Fixes

### Fix: Add Network Constraint

**Before (runs immediately, fails without network):**
```kotlin
val syncRequest = OneTimeWorkRequestBuilder<SyncWorker>().build()
WorkManager.getInstance(context).enqueue(syncRequest)
```

**After (waits for network):**
```kotlin
val constraints = Constraints.Builder()
    .setRequiredNetworkType(NetworkType.CONNECTED)
    .build()

val syncRequest = OneTimeWorkRequestBuilder<SyncWorker>()
    .setConstraints(constraints)
    .setBackoffCriteria(BackoffPolicy.EXPONENTIAL, 30, TimeUnit.SECONDS)
    .build()

WorkManager.getInstance(context)
    .enqueueUniqueWork("sync", ExistingWorkPolicy.KEEP, syncRequest)
```

### Fix: Make Worker Idempotent

**Before (duplicate execution causes duplicates):**
```kotlin
override suspend fun doWork(): Result {
    val items = localDao.getUnsyncedItems()
    items.forEach { item ->
        firebaseRef.child(item.id).setValue(item)
    }
    return Result.success()
}
```

**After (idempotent — safe for re-execution):**
```kotlin
override suspend fun doWork(): Result {
    val items = localDao.getUnsyncedItems()
    items.forEach { item ->
        try {
            firebaseRef.child(item.id).setValue(item).await()
            localDao.markSynced(item.id)  // Mark each item as synced individually
        } catch (e: Exception) {
            // Items already marked as synced won't be re-sent on retry
            return Result.retry()
        }
    }
    return Result.success()
}
```
