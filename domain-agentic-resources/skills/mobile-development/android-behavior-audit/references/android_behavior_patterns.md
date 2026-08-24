# Common Android Behavioral Anti-Patterns

Catalog of behavioral patterns in Android apps that frequently indicate bugs, incomplete implementations, or developer oversights. Use these as a reference during behavioral scrutiny to recognize known problematic patterns.

## Data Loss Patterns

### Silent Write Failure
**Pattern:** A data save operation catches exceptions but does not notify the user.
**What it looks like:**
```kotlin
try {
    dao.insert(item)
} catch (e: Exception) {
    Log.e(TAG, "Insert failed", e)
}
```
**Why it's problematic:** The user believes their data is saved. It isn't. This is the most common behavioral anti-pattern in Android apps.
**Severity:** Likely Bug (high confidence)

### Overwrite on Conflict
**Pattern:** Using `OnConflictStrategy.REPLACE` when the intent is to update specific fields.
**What it looks like:** `@Insert(onConflict = OnConflictStrategy.REPLACE)` used broadly.
**Why it's problematic:** REPLACE deletes the existing row and inserts a new one. If the entity has fields populated by other operations (timestamps, sync status, local flags), those are silently reset to defaults.
**Severity:** Likely Bug or Suspicious Pattern depending on context

### Orphaned Records
**Pattern:** Deleting a parent entity without cascading to children.
**What it looks like:** `dao.deleteFolder(folderId)` but no corresponding delete of items in that folder, and no `ForeignKey(onDelete = CASCADE)`.
**Why it's problematic:** Child records remain in the database with no parent, potentially causing crashes (null parent lookup) or stale data display.
**Severity:** Likely Bug

### Incomplete Sync
**Pattern:** Syncing data to Firebase but not handling partial failures in batch operations.
**What it looks like:** Multiple `setValue()` calls without using `updateChildren()` or transactions.
**Why it's problematic:** If the app crashes or loses connectivity between writes, the remote data is in an inconsistent state.
**Severity:** Suspicious Pattern

## State Management Patterns

### Dead-End State
**Pattern:** A UI state from which there is no user-recoverable path.
**What it looks like:** Error state with no retry button, no dismiss action, and no navigation option.
**Why it's problematic:** The user is stuck. They can only kill and restart the app.
**Severity:** Likely Bug

### State Leak Across Screens
**Pattern:** State from one screen affecting another due to shared ViewModel or singleton.
**What it looks like:** A shared ViewModel between screens where one screen's state changes bleed into another.
**Why it's problematic:** User navigates to Screen B, makes changes, returns to Screen A, and Screen A shows unexpected state.
**Severity:** Suspicious Pattern

### Process Death Data Loss
**Pattern:** Critical state stored in ViewModel but not in SavedStateHandle.
**What it looks like:** Form input, draft content, or filter selections stored in `MutableStateFlow` only.
**Why it's problematic:** Android can kill the process when the app is backgrounded. On restoration, the ViewModel is recreated and all non-persisted state is lost.
**Severity:** Suspicious Pattern (depends on criticality of the data)

### Race Condition on State Update
**Pattern:** Multiple coroutines updating the same state without synchronization.
**What it looks like:**
```kotlin
// Coroutine 1
_state.update { it.copy(items = newItems) }
// Coroutine 2 (simultaneous)
_state.update { it.copy(isLoading = false) }
```
**Why it's usually OK:** `MutableStateFlow.update` is thread-safe by default with optimistic concurrency. But if one update depends on the result of another, ordering matters.
**When it's problematic:** When updates should be atomic (both items and loading state should change together but don't).
**Severity:** Design Question or Suspicious Pattern

## Error Handling Patterns

### Swallowed CancellationException
**Pattern:** Catching `Exception` broadly in coroutines, which captures `CancellationException`.
**What it looks like:**
```kotlin
try { networkCall() } catch (e: Exception) { handleError(e) }
```
**Why it's problematic:** Catching `CancellationException` prevents structured concurrency from working. Cancelled coroutines continue running instead of stopping.
**Severity:** Suspicious Pattern (40-80% confidence depending on context)

### Error Message Mismatch
**Pattern:** Showing a generic "Something went wrong" for all error types.
**What it looks like:** All exceptions mapped to a single error string.
**Why it's problematic:** The user can't distinguish between network error (fixable by the user), server error (wait and retry), or data error (contact support). Different errors need different user actions.
**Severity:** Suspicious Pattern or Design Question

### Crash Prevention Over Correctness
**Pattern:** Wrapping entire operations in try-catch to prevent crashes, at the cost of incorrect behavior.
**What it looks like:** Global exception handler that shows a toast and continues.
**Why it's problematic:** The app doesn't crash, but it continues in an undefined state. The user sees no error but subsequent operations may fail or produce wrong results.
**Severity:** Suspicious Pattern

## Lifecycle Patterns

### Leaked Listener
**Pattern:** An event listener (Firebase, location, sensor) attached but never removed.
**What it looks like:** `addValueEventListener()` in ViewModel init without corresponding `removeEventListener()` in `onCleared()`.
**Why it's problematic:** Listeners continue firing after the ViewModel is garbage collected, causing memory leaks, unnecessary network usage, and potential crashes.
**Severity:** Likely Bug

### Activity Result Not Handled
**Pattern:** Launching an activity for result but not registering a result handler.
**What it looks like:** Calling `startActivity()` or using `ActivityResultLauncher` but never processing the result.
**Why it's problematic:** The user performs an action in another app/screen (take photo, pick file, grant permission) and returns, but the app doesn't use the result.
**Severity:** Likely Bug if the result is needed, Design Question if it's fire-and-forget

### Configuration Change State Loss
**Pattern:** State stored in the composable but not hoisted to ViewModel.
**What it looks like:** `var text by remember { mutableStateOf("") }` for a form input.
**Why it's problematic:** On rotation (or any configuration change), the composable is recreated and `remember` state is lost. For ephemeral state (animation) this is fine. For user input, it's frustrating.
**Severity:** Suspicious Pattern for user input, Confirmed Correct for ephemeral UI state

## Navigation Patterns

### Missing Auth Gate
**Pattern:** A screen that requires authentication is accessible without checking auth state.
**What it looks like:** Direct navigation to `ProfileScreen` without checking `FirebaseAuth.currentUser`.
**Why it's problematic:** Unauthenticated users reach a screen that assumes authentication, causing crashes or empty UI.
**Severity:** Likely Bug

### Back Stack Corruption
**Pattern:** Using `navigate()` without managing the back stack, causing duplicate screens.
**What it looks like:** `navController.navigate("home")` without `popUpTo` or `launchSingleTop`.
**Why it's problematic:** Pressing back multiple times visits the same screen repeatedly. The user can't exit the app naturally.
**Severity:** Suspicious Pattern

### Deep Link Back Stack
**Pattern:** Deep links that bypass normal navigation don't reconstruct the expected back stack.
**What it looks like:** Notification opens `DetailScreen` directly, but pressing back closes the app instead of going to the list screen.
**Why it's problematic:** User expectation is that back button navigates "up" in the hierarchy, even from a deep link entry.
**Severity:** Suspicious Pattern

## Background Work Patterns

### Non-Idempotent Worker
**Pattern:** A WorkManager worker that causes side effects when re-executed.
**What it looks like:** A sync worker that doesn't check for already-synced items.
**Why it's problematic:** WorkManager may re-execute workers (on retry, on constraint re-satisfaction). If the worker duplicates data, sends duplicate notifications, or makes duplicate API calls, re-execution causes visible bugs.
**Severity:** Suspicious Pattern

### Missing Worker Constraint
**Pattern:** A network-dependent worker scheduled without `NetworkType.CONNECTED` constraint.
**What it looks like:** `OneTimeWorkRequestBuilder<SyncWorker>().build()` without `setConstraints()`.
**Why it's problematic:** The worker runs immediately, fails because there's no network, retries with exponential backoff, and wastes battery. Adding the network constraint means WorkManager waits until connectivity is available.
**Severity:** Suspicious Pattern

### Foreground Service Without Notification
**Pattern:** Starting a foreground service but providing a minimal or misleading notification.
**What it looks like:** Empty notification channel, "Running..." notification text.
**Why it's problematic:** Android requires foreground services to have a visible notification. A misleading notification violates user trust and may violate Play Store policies.
**Severity:** Design Question (functional but possibly violating policy)

## Firebase-Specific Patterns

### Unvalidated Client Write
**Pattern:** Writing to Firebase without client-side validation, relying solely on security rules.
**What it looks like:** Directly writing user input to `ref.setValue()` without sanitization.
**Why it's problematic:** Security rules are the last line of defense, not the only line. Client-side validation provides immediate user feedback and reduces unnecessary write operations.
**Severity:** Design Question

### Auth State Not Observed
**Pattern:** Checking auth state once on startup but not observing changes.
**What it looks like:** `val user = FirebaseAuth.getInstance().currentUser` stored as a value.
**Why it's problematic:** If the auth token expires or the user is signed out by another session, the app continues operating as if authenticated until the next restart.
**Severity:** Suspicious Pattern

### Snapshot Listener Memory
**Pattern:** Firebase snapshot listeners attached at the repository level that live for the app's lifetime.
**What it looks like:** Listener attached in repository's `init {}` block.
**Why it's problematic:** The listener downloads data continuously even when no screen is observing it. This wastes bandwidth and battery, and the cached data might be stale when finally used.
**Severity:** Suspicious Pattern
