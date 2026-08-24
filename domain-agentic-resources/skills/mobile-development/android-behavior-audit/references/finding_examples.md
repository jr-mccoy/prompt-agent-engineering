# Behavior Audit Finding Examples

Calibration examples for each finding category. Use these to develop consistent, well-calibrated finding classifications.

## Likely Bug Examples

### Example LB-1: Silent Data Loss on Save Error

**Behavior traced:**
When user taps "Save Note", `NoteViewModel.saveNote()` calls `repository.save(note)` which calls `noteDao.insert(note)`. The DAO uses `OnConflictStrategy.REPLACE`. If the insert fails due to a database error, the exception is caught in the ViewModel with:
```kotlin
catch (e: Exception) {
    Log.e(TAG, "Failed to save note", e)
}
```
No UI state is updated. No error is shown to the user.

**Why this is a Likely Bug (95% confidence):**
The user taps "Save", sees no error, and assumes the note was saved. The data is silently lost. This is not a case where logging-only is acceptable — it's a user-initiated save operation. Every user-initiated data operation should confirm success or report failure to the user.

**What a fix would look like:**
Update the catch block to set an error state that the UI observes, showing a snackbar or error message.

---

### Example LB-2: Firebase Listener Never Detached

**Behavior traced:**
In `ChatRepository`, a ValueEventListener is attached to the messages path in `observeMessages()`:
```kotlin
fun observeMessages(chatId: String) {
    val ref = database.child("chats").child(chatId).child("messages")
    ref.addValueEventListener(messageListener)
}
```
There is no corresponding `removeEventListener` call. The ViewModel calls `observeMessages()` in `init {}` but never calls a cleanup function.

**Why this is a Likely Bug (90% confidence):**
Firebase listeners that are never removed continue to consume bandwidth, battery, and memory. They also continue to fire callbacks after the ViewModel is cleared, potentially causing crashes or unexpected behavior. The listener should be removed when the ViewModel is cleared or when the Flow/LiveData collector stops.

---

### Example LB-3: Navigation Dead End After Deep Link

**Behavior traced:**
When a notification deep link opens `ItemDetailScreen` directly (bypassing `HomeScreen`), the back button calls `navController.popBackStack()`. Since `HomeScreen` was never on the back stack, `popBackStack()` returns `false` and the user is stuck on a screen with no way to navigate anywhere.

**Why this is a Likely Bug (85% confidence):**
Deep links that bypass the normal navigation flow must handle the empty back stack case. The standard solution is to rebuild the back stack or navigate to Home when popBackStack returns false.

## Suspicious Pattern Examples

### Example SP-1: Timing-Dependent Initialization

**Behavior traced:**
In `SyncManager.init()`, there is a `delay(2000)` before starting the initial sync:
```kotlin
fun init() {
    scope.launch {
        delay(2000) // Wait for Firebase Auth to initialize
        startSync()
    }
}
```

**Why this is Suspicious (70% confidence):**
This assumes Firebase Auth will be ready within 2 seconds, which is a timing assumption that may not hold on slow devices or slow networks. However, it's possible this was tested and 2 seconds is sufficient for the target devices. The proper approach would be to observe Firebase Auth state rather than using a fixed delay.

**Question for developer:** Is this delay intentional? Would it be better to listen for Firebase Auth ready state instead?

---

### Example SP-2: Catch-All Error Handler

**Behavior traced:**
The `ApiRepository` wraps all API calls in:
```kotlin
suspend fun <T> safeApiCall(call: suspend () -> T): Result<T> {
    return try {
        Result.success(call())
    } catch (e: Exception) {
        Result.failure(e)
    }
}
```
This catches ALL exceptions including `CancellationException`, which should never be caught in coroutines (it prevents cancellation from working correctly).

**Why this is Suspicious (75% confidence):**
Catching `CancellationException` is a well-known coroutine anti-pattern. However, the developer may not be aware of this issue, and in many cases it might not cause visible problems. It becomes a real issue when the user navigates away and the cancelled coroutine keeps running.

**Question for developer:** Are you aware that this catches CancellationException? Should we add `if (e is CancellationException) throw e` at the start of the catch block?

---

### Example SP-3: Partial Feature Implementation

**Behavior traced:**
`SettingsScreen` has a "Export Data" button that calls `viewModel.exportData()`. The ViewModel function:
```kotlin
fun exportData() {
    // TODO: Implement export
    _uiState.update { it.copy(message = "Export coming soon") }
}
```

**Why this is Suspicious (60% confidence):**
The button is visible and tappable in the UI but does nothing useful. This could be intentional (deferred feature shown as coming soon) or it could be a forgotten TODO. For a pre-production release, visible non-functional features could confuse testers.

**Question for developer:** Is "Export Data" intentionally deferred, or should we implement it before the closed test? If deferred, should the button be hidden or disabled?

## Design Question Examples

### Example DQ-1: Auto-Save Frequency

**Behavior traced:**
`NoteEditorViewModel` auto-saves the note every 30 seconds via:
```kotlin
init {
    viewModelScope.launch {
        noteContent.debounce(30_000).collect { content ->
            repository.save(content)
        }
    }
}
```

**Why this is a Design Question (30% confidence):**
30 seconds could be a deliberate choice based on user research (frequent enough to prevent data loss, infrequent enough to not cause performance issues) or it could be an arbitrary number. Both 5 seconds and 60 seconds would be equally reasonable without context.

**Question for developer:** Is the 30-second auto-save interval a deliberate choice? Should it be configurable? Would users expect more frequent saving?

---

### Example DQ-2: No Confirmation Before Delete

**Behavior traced:**
`ItemListScreen` has a swipe-to-delete gesture that calls `viewModel.deleteItem(id)` directly. There is no confirmation dialog. The delete calls `dao.delete(item)` and `firebaseRef.removeValue()`.

**Why this is a Design Question (35% confidence):**
Some apps intentionally skip delete confirmation for speed (with undo snackbar as safety net). Others require confirmation to prevent accidents. Without knowing the product design philosophy, either approach is valid. However, there is no undo mechanism visible in the code.

**Question for developer:** Is the lack of delete confirmation intentional? If so, should there be an undo mechanism? Without either, accidental deletes are permanent.

---

### Example DQ-3: Error Message Specificity

**Behavior traced:**
When Firebase Auth sign-in fails, the error is mapped:
```kotlin
catch (e: FirebaseAuthException) {
    _uiState.update { it.copy(error = e.message ?: "Authentication failed") }
}
```
This shows the raw Firebase error message to the user (e.g., "The email address is badly formatted", "There is no user record corresponding to this identifier").

**Why this is a Design Question (25% confidence):**
Firebase error messages are somewhat user-readable but technical. Some apps prefer to show custom, friendlier messages. Others prefer to show the actual error for clarity. Both are valid approaches.

**Question for developer:** Are the raw Firebase error messages intentional, or would you prefer custom user-facing messages?

## Confirmed Correct Examples

### Example CC-1: Optimistic UI Update with Rollback

**Behavior traced:**
When user toggles a favorite, the UI updates immediately (optimistic), then syncs to Firebase. If the sync fails, the UI reverts:
```kotlin
fun toggleFavorite(itemId: String) {
    val previous = _uiState.value
    _uiState.update { it.copy(isFavorite = !it.isFavorite) } // optimistic
    viewModelScope.launch {
        try {
            repository.setFavorite(itemId, !previous.isFavorite)
        } catch (e: Exception) {
            _uiState.update { previous } // rollback on failure
            _events.emit(ShowError("Failed to update favorite"))
        }
    }
}
```

**Why this is Confirmed Correct:**
This is a standard optimistic UI pattern. The UI responds instantly for a snappy feel, the actual operation runs in the background, and the UI reverts with an error message if it fails. All three paths (success, failure with rollback, error messaging) are handled.

### Example CC-2: Debounced Search

**Behavior traced:**
Search input is debounced before making API calls:
```kotlin
searchQuery
    .debounce(300)
    .distinctUntilChanged()
    .filter { it.length >= 2 }
    .flatMapLatest { query -> repository.search(query) }
    .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), emptyList())
```

**Why this is Confirmed Correct:**
300ms debounce prevents excessive API calls while typing. `distinctUntilChanged` avoids duplicate queries. Minimum 2 characters prevents overly broad searches. `flatMapLatest` cancels previous in-flight searches when a new query arrives. `WhileSubscribed(5000)` keeps the upstream active for 5 seconds after the collector disappears (handles rotation without re-fetching).
