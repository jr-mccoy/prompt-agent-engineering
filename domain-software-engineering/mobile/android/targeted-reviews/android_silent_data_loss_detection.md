---
title: "Android Silent Data Loss Detection"
category: mobile/android/targeted-reviews
description: "Android Silent Data Loss Detection."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - data
  - loss
  - mobile
  - reviews
  - silent
updated: "2026-03-19"
related_prompts: []
---

# Android Silent Data Loss Detection

**Objective:** Systematically detect all code patterns in an Android application where user data can be silently lost — dropped without error, swallowed by exception handlers, overwritten without merge, orphaned by cascade failures, or made unreachable by state machine bugs — without the user or developer being notified.

**When to Use:** Use this prompt when users report "data disappeared" or "my changes were lost" but the app didn't show any errors, after investigating sync issues where the root cause isn't obvious, as a proactive audit before launching a data-heavy feature, or after a production incident involving data loss. This prompt finds the non-obvious losses that don't show up in crash analytics.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Construct a concrete scenario** — For every suspected data loss pattern, describe the exact sequence of user actions and system events that triggers it. If you can't construct a plausible scenario, don't report it.
2. **Verify the data is truly lost** — Confirm it's not cached elsewhere, recoverable from cloud, or restorable through undo. "Lost" means the user's data is gone and cannot be recovered through normal app behavior.
3. **Check for existing safeguards** — The app may have retry logic, recovery mechanisms, or compensating actions that prevent the loss from being permanent.
4. **Assess probability** — Some patterns are theoretically possible but practically impossible. Focus on patterns that real users can trigger through normal usage.
5. **Provide specific file:line locations** — Every finding MUST include exact code locations.

**Finding NO silent data loss is an acceptable outcome.** Well-built apps can avoid these patterns. Don't manufacture findings.

### False-Positive Prevention

- ❌ Do NOT flag intentional data deletion as "data loss" (e.g., cache clearing, TTL expiry)
- ❌ Do NOT flag eventual consistency delays as data loss
- ❌ Do NOT flag data transformation (e.g., trimming whitespace) as corruption
- ❌ Do NOT report patterns that only occur under conditions the app explicitly doesn't support
- ✅ DO focus on patterns where the user expects their data to be preserved but it isn't
- ✅ DO check what happens when the "happy path" fails — that's where silent loss hides
- ✅ DO examine every `catch` block, `onFailure`, and error callback for swallowed errors
- ✅ DO trace data through format conversions and serialization for lossy transformations

---

### Pattern 1: Swallowed Exceptions

Search for places where exceptions are caught but the failed operation is not retried, reported, or surfaced to the user:

#### 1.1 Empty Catch Blocks
* Find all `catch` blocks that do nothing or only log
* For each, ask: Did the code in the `try` block write, update, or delete user data?
* If yes: The user's action appeared to succeed, but the data wasn't persisted

**Common locations:**
```kotlin
// DANGEROUS: User thinks save worked, but it silently failed
try {
    repository.saveItem(item)
} catch (e: Exception) {
    Log.e(TAG, "Save failed", e)  // Logged but not surfaced to user
}
```

#### 1.2 Kotlin `runCatching` Without Error Handling
* Find all `runCatching { }` calls
* Check: Is `.onFailure { }` or `.getOrElse { }` handling the error?
* Find cases where only `.getOrNull()` is used and the null case is silently ignored

#### 1.3 Coroutine Exception Swallowing
* Check `CoroutineExceptionHandler` implementations — do they swallow exceptions silently?
* Check `supervisorScope` and `SupervisorJob` usage — child failures may be silently lost
* Check `launch` without exception handling — unhandled exceptions crash the app... unless caught by a global handler that swallows them
* Check `async` where `.await()` is never called — the exception is lost entirely

#### 1.4 Flow Exception Swallowing
* Find `.catch { }` operators on Flows
* Check: Do they emit a fallback value that hides the error (e.g., emitting empty list instead of error)?
* Check: Do they log but not propagate the error to the UI?

---

### Pattern 2: Fire-and-Forget Operations

Search for data write operations that are launched but never awaited or confirmed:

#### 2.1 Unawaited Coroutine Launches
```kotlin
// DANGEROUS: If this fails, nobody knows
viewModelScope.launch {
    repository.saveItem(item)
    // No result check, no error handling
}
// ViewModel immediately shows "saved" success
```

* Find all `launch { }` blocks that contain write operations
* Check: Is the result awaited? Is success/failure communicated to the UI?

#### 2.2 One-Way Firebase Writes
* Find Firebase `setValue()`, `updateChildren()`, `removeValue()` calls
* Check: Is the `addOnCompleteListener`/`addOnFailureListener` callback handling failures?
* Common bug: `.setValue(data)` without any completion listener — if it fails, nobody knows

#### 2.3 WorkManager Enqueue Without Observation
* Find `workManager.enqueue()` calls
* Check: Is the work result observed? What happens if the worker fails permanently?
* Check: Is `Result.failure()` handled, or does the failed data write silently disappear?

---

### Pattern 3: Overwrite Without Merge

Search for patterns where newer data silently overwrites user changes:

#### 3.1 Full-Entity Overwrite on Sync Pull
```kotlin
// DANGEROUS: User's pending local edits silently replaced by server version
remoteChanges.forEach { remoteItem ->
    localDao.upsert(ItemMapper.fromDto(remoteItem))  // Overwrites everything
}
```

* Find all pull sync/refresh operations
* Check: Before overwriting a local entity with a remote version, is the local `syncStatus` checked?
* If local is `PENDING_UPDATE`, overwriting with the remote version loses the user's edits

#### 3.2 InsertOrReplace Without Checking Pending State
* Find `@Insert(onConflict = OnConflictStrategy.REPLACE)` usages
* Check: Is this ever called from sync pull? It will overwrite local pending changes

#### 3.3 SharedPreferences/DataStore Race
* Find concurrent reads and writes to the same preference key
* Check: Can a background sync update a preference while the UI is about to write a user's change?
* DataStore: Check for `.updateData { }` vs `.edit { }` patterns that may not be atomic

---

### Pattern 4: Orphaned Data

Search for data that becomes unreachable or inconsistent due to incomplete cascading operations:

#### 4.1 Missing Cascade on Delete
* Find entity deletion code (soft and hard)
* For each parent entity: What happens to child entities when the parent is deleted?
* Check: Are children left pointing to a non-existent parent (orphaned)?
* Check: Are orphaned children visible in the UI, causing crashes or confusion?

#### 4.2 Missing Cascade on ID Change
* If server returns a different ID than the local UUID after CREATE sync:
  * Are all foreign key references updated?
  * Are related entities updated to point to the new ID?
  * Are sync queue items for the old ID updated?

#### 4.3 Partial Multi-Entity Operations
* Find operations that modify multiple entities (e.g., "move task to new category")
* Check: Are all modifications in a single Room `@Transaction`?
* If not: Can a crash between modifications leave data partially updated?

#### 4.4 Orphaned Sync Queue Items
* If an entity is hard-deleted from Room, are pending sync queue items for that entity cleaned up?
* Can the sync engine try to push an item that no longer exists locally?

---

### Pattern 5: State Machine Dead Ends

Search for sync status values or entity states from which data cannot escape:

#### 5.1 Unqueried Sync States
* List all possible values of the sync status field
* For each value: Is there a sync query that picks up items in this state?
* Common bug: Custom states like `CONFLICT`, `ERROR`, `RETRY_FAILED` that no query ever selects

#### 5.2 Permanent Failure States
* When a sync operation fails permanently (e.g., max retries exceeded):
  * What state does the item end up in?
  * Is the user notified?
  * Can the user retry manually?
  * Or does the item sit in `FAILED` forever, never syncing?

#### 5.3 Stuck in Processing
* If sync marks items as "processing" or "in-flight" before sending to cloud:
  * What happens if the app is killed during processing?
  * Is there recovery logic to reset "stuck" items back to pending?

#### 5.4 Boolean Flag Traps
* Find entities with boolean flags like `isDeleted`, `isArchived`, `isCompleted`
* Check: Can combinations of flags create states where the item is invisible to all queries?
  * Example: `isDeleted = true` AND `syncStatus = SYNCED` — item is hidden from UI AND not picked up by sync for cloud deletion

---

### Pattern 6: Lossy Data Transformations

Search for data conversions that silently lose information:

#### 6.1 Serialization/Deserialization Loss
* Find JSON serialization of entities (Moshi, Gson, Kotlinx.serialization)
* Check: Are all fields included in serialization? Are any excluded by annotation (`@Transient`, `@JsonIgnore`)?
* Check: When deserializing, are unknown fields silently dropped? Could this lose data added by a newer app version?

#### 6.2 DTO ↔ Entity Mapping Loss
* Find mapper functions between DTOs and Room entities
* Check: Are all fields mapped? Could a new field added to one side be missing from the mapper?
* Check: Are nullable fields on one side mapped to non-nullable on the other, with a silent default?

#### 6.3 Type Conversion Loss
* Find TypeConverters (Room `@TypeConverter`)
* Check: Is the conversion reversible? (e.g., `Date` → `Long` → `Date` — does precision survive?)
* Check: Are enum conversions handling unknown values? What happens if the server sends an enum value the app doesn't know about?

#### 6.4 String Truncation
* Check: Are there column length limits that could silently truncate user input?
* Check: Are API payloads size-limited? Could a long note be truncated by the server?

---

### Pattern 7: Race Conditions That Lose Data

Search for timing-dependent data loss:

#### 7.1 Read-Modify-Write Races
```kotlin
// DANGEROUS: If two coroutines do this simultaneously, one's changes are lost
val item = dao.getById(id)
val updated = item.copy(count = item.count + 1)
dao.update(updated)
```

* Find read-then-write patterns
* Check: Is there a transaction or mutex protecting the sequence?

#### 7.2 Sync Pull During User Edit
* If the user is editing an entity when a background sync pull arrives:
  * Does the sync overwrite the in-memory state the user is editing?
  * When the user saves, does their save overwrite the sync'd data?
  * Can the user lose either their own edits OR the remote changes?

#### 7.3 Multiple ViewModel Instances
* Can multiple screens/ViewModels modify the same entity simultaneously?
* Check: Is there coordination between them, or can one overwrite the other's changes?

#### 7.4 Process Death During User Input
* If the user has typed content but not yet saved:
  * Is the in-progress input saved to `SavedStateHandle` or a draft mechanism?
  * Or is it lost on process death?

---

### Pattern 8: Cloud-Side Silent Loss

Search for patterns where the cloud backend silently loses or rejects data:

#### 8.1 Firebase Security Rules Rejection
* If Firebase security rules reject a write, does the client handle the failure?
* Common bug: Rules deny write, client receives error in callback, but callback only logs it

#### 8.2 Cloud Function Transformation
* If Cloud Functions process data before storage, do they preserve all fields?
* Can a Cloud Function validation silently reject or modify data?

#### 8.3 Server-Side Validation Rejection
* If the server returns 400/422 (validation error), is the user notified?
* Or does the item stay as `PENDING_CREATE` forever, retrying a validation error that will never succeed?

#### 8.4 Quota/Size Limits
* If the cloud has storage quotas or document size limits:
  * What happens when the limit is hit?
  * Is the user notified, or does the write silently fail?

---

## Expected Output

### 1. Executive Summary

- Total patterns examined: [N of 8]
- Total silent data loss risks found: [N] by severity
- Overall risk level: Low / Medium / High / Critical
- Most critical finding: [One-sentence description]

### 2. Silent Data Loss Risk Matrix

| Pattern | Instances Found | Severity | Probability | User Impact |
|---------|----------------|----------|-------------|-------------|
| Swallowed Exceptions | [N] | [Level] | [Prob] | [Impact] |
| Fire-and-Forget | [N] | [Level] | [Prob] | [Impact] |
| Overwrite Without Merge | [N] | [Level] | [Prob] | [Impact] |
| Orphaned Data | [N] | [Level] | [Prob] | [Impact] |
| State Machine Dead Ends | [N] | [Level] | [Prob] | [Impact] |
| Lossy Transformations | [N] | [Level] | [Prob] | [Impact] |
| Race Conditions | [N] | [Level] | [Prob] | [Impact] |
| Cloud-Side Loss | [N] | [Level] | [Prob] | [Impact] |

### 3. Detailed Findings

For each finding:

- **ID:** SILENT-LOSS-[N]
- **Pattern:** Which of the 8 patterns
- **Severity:** Critical / High / Medium / Low
- **Probability:** How likely a real user triggers this (Daily / Weekly / Monthly / Rare)
- **Location:** File:line(s)
- **Scenario:** Step-by-step: what the user does → what the code does → what goes wrong → what data is lost
- **Evidence:** Code excerpt showing the problematic pattern
- **User Experience:** What the user sees (or doesn't see — that's the "silent" part)
- **Data Lost:** Specifically what data is gone and whether it's recoverable
- **Fix:** Specific code change with rationale
- **Detection:** How to add monitoring/alerting so this loss is no longer silent (even before fixing)

### 4. Swallowed Exception Inventory

| Location | Exception Type | Data Operation | User Notified | Severity |
|----------|---------------|----------------|---------------|----------|
| [File:line] | [Type] | [What operation failed] | Yes/No | [Level] |

### 5. Sync State Machine Audit

```
[Diagram showing all states and transitions]
Mark dead-end states with ❌
Mark states with no query coverage with ⚠️
```

### 6. Prioritized Fix List

- **Critical (Data loss in normal usage):**
  1. [Finding] — [Fix summary]
- **High (Data loss under common adverse conditions):**
  1. [Finding] — [Fix summary]
- **Medium (Data loss under unlikely conditions):**
  1. [Finding] — [Fix summary]
- **Low (Theoretical or minimal-impact loss):**
  1. [Finding] — [Fix summary]

### 7. Monitoring Recommendations

For each finding, suggest instrumentation to detect the loss in production:
- Analytics events to fire when errors are caught
- Sync health metrics to track
- Data consistency checks to run periodically
- User-facing indicators to add

---

## Example Output

```markdown
# Silent Data Loss Detection Report — TaskMaster App

## Executive Summary
- **Patterns Examined:** 8 of 8
- **Silent Loss Risks:** 2 Critical, 4 High, 3 Medium, 2 Low
- **Overall Risk:** Critical
- **Most Critical:** Sync pull overwrites user's pending local edits without merge (SILENT-LOSS-3)

## Critical Findings

### SILENT-LOSS-1: Delete Exception Swallowed in ViewModel
**Pattern:** Swallowed Exceptions
**Severity:** Critical
**Probability:** Weekly (any user who deletes while sync is running)

**Location:** TaskViewModel.kt:89

**Scenario:**
1. User swipes to delete a task
2. ViewModel calls `repository.delete(taskId)` inside `launch { }`
3. Repository calls `softDelete()` — succeeds locally
4. Repository calls `syncEngine.syncItem(taskId)` — throws because sync is already running
5. Exception caught by ViewModel's `CoroutineExceptionHandler` which only logs
6. User sees task disappear (local soft delete worked)
7. Sync engine never retries because the item's syncStatus was never set to PENDING_DELETE
8. Task reappears on next pull sync from cloud

**Evidence:**
```kotlin
// TaskViewModel.kt:89
fun deleteTask(taskId: String) {
    viewModelScope.launch {
        repository.delete(taskId)
        // If this throws, CoroutineExceptionHandler catches it
        // But local soft-delete already happened
        // syncStatus is now inconsistent
    }
}

// TaskViewModel.kt:12
private val exceptionHandler = CoroutineExceptionHandler { _, throwable ->
    Log.e(TAG, "Error in ViewModel", throwable)  // Silent! User not notified
}
```

**User Experience:** Task disappears from list, then magically reappears after next sync or app restart. User deletes again, same thing happens. Extremely frustrating.

**Data Lost:** The delete operation itself is lost. The data (task) is actually preserved when it shouldn't be.

**Fix:**
```kotlin
fun deleteTask(taskId: String) {
    viewModelScope.launch {
        repository.delete(taskId)
            .onFailure { error ->
                _uiState.update { it.copy(
                    error = UiError.DeleteFailed(taskId, error.message)
                )}
                // Also: ensure softDelete and syncStatus are atomic
                // so we never get isDeleted=true with syncStatus=SYNCED
            }
    }
}
```

**Detection:** Add analytics event `sync_status_inconsistency` that fires when an item has `isDeleted=true` but `syncStatus=SYNCED`.

---

### SILENT-LOSS-3: Sync Pull Overwrites Pending Local Edits
**Pattern:** Overwrite Without Merge
**Severity:** Critical
**Probability:** Daily (any user who edits while offline or during slow sync)

**Location:** SyncEngine.kt:145

**Scenario:**
1. User edits task title from "Buy milk" to "Buy oat milk" (offline)
2. Local entity: syncStatus = PENDING_UPDATE, title = "Buy oat milk"
3. Network returns, periodic sync fires
4. Pull sync gets server version: title = "Buy milk" (old)
5. Sync engine does `localDao.upsert(remoteItem)` without checking syncStatus
6. Local entity overwritten: syncStatus = SYNCED, title = "Buy milk"
7. User's edit is permanently lost
8. No error, no notification, no conflict indication

**Evidence:**
```kotlin
// SyncEngine.kt:145
private suspend fun pullRemoteChanges() {
    val remoteChanges = remoteDataSource.getChangesSince(lastSync)
    remoteChanges.forEach { remoteItem ->
        // BUG: No check for local pending changes!
        localDao.upsert(ItemMapper.fromDto(remoteItem))
    }
}
```

**Fix:**
```kotlin
private suspend fun pullRemoteChanges() {
    val remoteChanges = remoteDataSource.getChangesSince(lastSync)
    remoteChanges.forEach { remoteItem ->
        val localItem = localDao.getById(remoteItem.id)
        when {
            localItem == null -> localDao.upsert(ItemMapper.fromDto(remoteItem))
            localItem.syncStatus == SyncStatus.SYNCED -> localDao.upsert(ItemMapper.fromDto(remoteItem))
            else -> handleConflict(localItem, remoteItem)  // Don't overwrite pending changes!
        }
    }
}
```
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on silent data loss detection
- **ST-02** (Structured Sequential Instructions) — Pattern-by-pattern analysis
- **RT-05** (Evidence-Based Reasoning) — Concrete scenarios and code excerpts required
- **DT-02** (Specific Focus Areas) — 8 distinct loss patterns as focus areas
- **QA-02** (Adversarial Stress-Test) — Thinking about failure modes and edge cases
- **DS-06** (Prioritization Guidance) — Probability × impact ranking
- **RT-07** (Cascade Effect Analysis) — Tracing how one failure cascades through the system

---

## Related Prompts

- `android_data_integrity_audit.md` — Comprehensive end-to-end data integrity audit
- `android_crud_sync_verification.md` — Verify each CRUD operation syncs correctly
- `android_sync_architecture_review.md` — Overall sync design review
- `android_offline_conflict_resolution_review.md` — Conflict resolution deep dive
- `android_error_handling_improvement.md` — Improve error handling patterns
- `android_crash_analysis.md` — Crash analysis (for non-silent failures)
- `android_process_death_recovery_review.md` — Process death resilience

---

## Customization Guide

- **For Firebase apps:** Add Pattern 8 sub-checks for Firebase-specific silent failures: security rules silently blocking writes, Firestore offline cache hitting size limits, RTDB `.info/connected` listener missing.
- **For apps with encryption:** Add checks for silent loss during encrypt/decrypt failures, key rotation that leaves data unreadable, and encrypted field search that misses records.
- **For apps with media/attachments:** Add checks for orphaned file references, partial upload losses, storage cleanup that deletes files still referenced by entities.
- **For multi-user apps:** Add checks for permission change propagation, shared entity visibility after user removal, and silent rejection of edits to entities the user no longer has access to.
- **For apps with undo/redo:** Add checks for undo state that races with sync, undo stack that doesn't survive process death, and redo that silently fails because the entity state changed.
