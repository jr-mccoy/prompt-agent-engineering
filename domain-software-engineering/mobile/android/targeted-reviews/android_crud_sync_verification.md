---
title: "Android CRUD Sync Verification"
category: mobile/android/targeted-reviews
description: "Android CRUD Sync Verification."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - crud
  - mobile
  - reviews
  - sync
  - targeted
updated: "2026-03-19"
related_prompts: []
---

# Android CRUD Sync Verification

**Objective:** Systematically verify that every CRUD operation (Create, Read, Update, Delete) for every synced entity in an Android application correctly propagates from local storage to the cloud backend and vice versa, with specific focus on identifying operations that silently fail to sync.

**When to Use:** Use this prompt when a specific sync issue has been reported (e.g., "deleted tasks don't sync to cloud," "edits revert after app restart"), when adding a new entity type to sync, when changing sync infrastructure, or when validating sync correctness after a refactor. This is a focused, operation-by-operation verification — for a broader audit, use `android_data_integrity_audit.md`.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the exact code path** — Follow the specific operation from the point of user action to the cloud write (or cloud event to local write). Name every function, class, and method in the chain.
2. **Verify the sync trigger** — Confirm that the operation actually enqueues or triggers a sync. Don't assume — find the code that transitions the sync status or adds to the queue.
3. **Check the sync worker/engine** — Confirm that the sync worker queries for this specific sync status and handles this specific operation type.
4. **Test the cloud API call** — Verify the correct API endpoint/Firebase method is called with the correct payload.
5. **Provide specific file:line locations** — Every finding MUST include exact code locations.

**Finding NO issues is an acceptable outcome.** If all CRUD operations sync correctly, document the verified paths and say so with confidence.

### False-Positive Prevention

- ❌ Do NOT flag delayed sync as broken sync (periodic/batched sync is valid)
- ❌ Do NOT flag optimistic UI updates as sync failures
- ❌ Do NOT assume sync is broken without tracing the complete path from local write to cloud write
- ❌ Do NOT report issues based on naming conventions alone (e.g., "this method doesn't mention sync" — the sync trigger may be elsewhere)
- ✅ DO check every branch and early return in the sync path — missed enum cases and unhandled status values are the #1 cause of sync gaps
- ✅ DO verify that sync status transitions form a complete state machine with no dead-end states
- ✅ DO check that the sync query matches all pending states, not just some
- ✅ DO verify that post-sync cleanup (status update, hard delete) actually executes

---

### Step 1: Identify All Synced Entities

Inventory every entity that should sync between local and cloud:

* List each entity class (Room @Entity or equivalent)
* Identify its cloud counterpart (Firestore document, RTDB node, REST resource)
* Note the sync direction: Local→Cloud only, Cloud→Local only, or Bidirectional
* Identify the sync status field and its possible values
* Note the sync trigger mechanism (immediate, queued, periodic, listener-based)

**Produce Entity Sync Inventory Table** (see Output Format).

---

### Step 2: Verify CREATE Sync Path

For each entity, trace the Create operation:

#### 2.1 Local Creation
* Find the function that creates the entity (usually in Repository or UseCase)
* Verify the entity is saved to Room with `syncStatus = PENDING_CREATE` (or equivalent)
* Verify a unique ID is generated (UUID, or placeholder for server-assigned ID)
* Check: Is the sync status set in the SAME transaction as the insert, or separately?

#### 2.2 Sync Trigger
* Find what triggers the sync after creation (immediate call? connectivity observer? WorkManager?)
* Verify the sync engine/worker queries include `PENDING_CREATE` items
* Check: Is there a code path where the item is created but sync is never triggered?

#### 2.3 Cloud Write
* Find the API/Firebase call that creates the entity on the cloud
* Verify the payload includes all required fields
* Check: Does the response contain a server-assigned ID or timestamp? Is it written back to the local entity?

#### 2.4 Post-Sync Update
* Verify `syncStatus` is updated to `SYNCED` after successful cloud creation
* Verify `serverTimestamp` or equivalent is saved locally
* Check: If the cloud returns a different ID than the local UUID, is the local ID updated? Are foreign key references updated?

#### 2.5 Failure Handling
* What happens if the cloud create returns 400 (validation error)?
* What happens if it returns 409 (already exists)?
* What happens if it returns 5xx (server error)?
* Is the item left as `PENDING_CREATE` for retry, or is it stuck in a broken state?

---

### Step 3: Verify UPDATE Sync Path

For each entity, trace the Update operation:

#### 3.1 Local Update
* Find the function that updates the entity
* Verify `syncStatus` transitions correctly:
  - `SYNCED` → `PENDING_UPDATE` ✓
  - `PENDING_CREATE` → stays `PENDING_CREATE` ✓ (first sync should create, not update)
  - `PENDING_UPDATE` → stays `PENDING_UPDATE` ✓ (coalesce pending updates)
  - `PENDING_DELETE` → what happens? (User undeleted then edited? Or bug?)
  - `CONFLICT` → what happens? (User edited a conflicted item?)
* Verify `localUpdatedAt` is set to current time

#### 3.2 Sync Trigger
* Verify the sync engine queries include `PENDING_UPDATE` items
* Check: Is the UPDATE sync path separate from CREATE, or does the same code handle both?

#### 3.3 Cloud Write
* Verify the correct API call (PUT/PATCH, Firestore set/update, RTDB update)
* For PATCH: Are only changed fields sent, or the entire entity?
* Check: Is there conflict detection (version check, ETag, server timestamp comparison)?

#### 3.4 Post-Sync Update
* Verify `syncStatus` → `SYNCED` after success
* Verify `serverUpdatedAt` is saved
* Check: If the server modified additional fields (computed fields, server timestamps), are those reflected locally?

#### 3.5 Conflict Detection
* What happens when the server returns 409 or the server version is newer?
* Is the conflict stored and surfaced to the user, or silently resolved?

---

### Step 4: Verify DELETE Sync Path

**This is the most commonly broken sync operation.** Examine with extra scrutiny:

#### 4.1 Local Deletion
* Find the function that deletes the entity
* **CRITICAL CHECK:** Is it a soft delete (set flag) or hard delete (remove from DB)?
* If soft delete:
  - Is `isDeleted` set to `true`?
  - Is `syncStatus` set to `PENDING_DELETE`?
  - Are BOTH set in the SAME operation/transaction?
  - Is `localUpdatedAt` updated?
* If hard delete:
  - Is the item removed from Room BEFORE or AFTER the cloud sync?
  - If before: How does the sync engine know what to delete on the cloud? Is there a separate delete queue?

#### 4.2 UI Filtering
* Are all UI queries filtered to exclude deleted items (`WHERE is_deleted = 0`)?
* Check ALL queries — list queries, detail queries, search queries, count queries
* Are Flow/LiveData observers re-emitting after the soft delete to update the UI?

#### 4.3 Sync Trigger for Deletes
* **CRITICAL CHECK:** Does the sync engine query INCLUDE `PENDING_DELETE` status?
  ```
  Common Bug: Query is "WHERE syncStatus = 'PENDING_CREATE' OR syncStatus = 'PENDING_UPDATE'"
  Missing: PENDING_DELETE never queried → deletes never sync!
  ```
* Does the sync engine have a handler for `PENDING_DELETE` items?
* Is the delete handler calling the correct cloud API (DELETE endpoint, not update)?

#### 4.4 Cloud Deletion
* What API call deletes the entity from the cloud?
* For Firebase: Is `.removeValue()` or `.delete()` called? On the correct path/reference?
* For REST: Is HTTP DELETE sent to the correct endpoint with the correct ID?
* Check: Is the cloud deletion calling delete, or just updating a `deleted` flag on the server too?

#### 4.5 Post-Delete Cleanup
* After the cloud confirms deletion:
  - Is the local soft-deleted item hard-deleted (removed from Room)?
  - Or does it linger indefinitely as a deleted ghost row?
* If hard-deleted locally: Could a subsequent pull sync re-create the item from the cloud if the cloud delete hasn't propagated to all listeners?

#### 4.6 Cascade Deletion
* When a parent entity is deleted, are child entities also:
  - Soft-deleted locally?
  - Marked as `PENDING_DELETE`?
  - Synced to cloud as deletions?
* What happens if the parent delete syncs but child deletes fail?

#### 4.7 Edge Cases for Delete
* **Delete while offline:** Is the soft-deleted + PENDING_DELETE state persisted in Room? Does it survive app restart? Does it sync when connectivity returns?
* **Delete then undo:** If undo is supported, does it correctly revert `isDeleted` AND `syncStatus`? Can the undo race with an in-progress sync?
* **Delete already-pending-create item:** If the user creates an item offline then deletes it before it syncs, what happens? Is the item simply removed (since the cloud never knew about it)?
* **Remote delete arrives during local edit:** If the server pushes a delete for an item the user is currently editing, what happens?

---

### Step 5: Verify Pull Sync (Cloud→Local) Path

#### 5.1 New Remote Items
* When the cloud has items that don't exist locally, are they created in Room with `SYNCED` status?

#### 5.2 Updated Remote Items
* When a cloud item is newer than the local `SYNCED` version, is the local version updated?
* When a cloud item conflicts with a local `PENDING_UPDATE`, is conflict resolution triggered?

#### 5.3 Deleted Remote Items
* When an item exists locally but has been deleted from the cloud:
  - How is this detected? (Absence from full sync? Explicit deletion event? Tombstone?)
  - Is the local item deleted?
  - What if the local item has pending changes (`PENDING_UPDATE`)?

---

### Step 6: Sync Status State Machine Verification

Map the complete state machine and verify there are no dead-end states:

```
INITIAL → PENDING_CREATE → SYNCED → PENDING_UPDATE → SYNCED
                                   → PENDING_DELETE → [hard deleted]
                                   → CONFLICT → [resolved] → SYNCED
          PENDING_CREATE → [delete before sync] → [hard deleted, no cloud action needed]
```

Check for:
* **Dead-end states:** Can an entity get stuck in a status that no sync query picks up?
* **Invalid transitions:** Can an entity transition to a state that makes no sense (e.g., PENDING_DELETE → PENDING_CREATE)?
* **Missing transitions:** Is there a user action that doesn't set the sync status correctly?
* **Concurrent transition safety:** If a sync and a user action happen simultaneously, can the status be overwritten incorrectly?

---

## Expected Output

### 1. Entity Sync Inventory

| Entity | Cloud Target | Direction | Sync Status Field | Sync Trigger | Verified |
|--------|-------------|-----------|-------------------|-------------|----------|
| [Name] | [Target] | [Dir] | [Field] | [Trigger] | ✅/❌ |

### 2. CRUD Sync Verification Matrix

For each entity:

| Operation | Local Write | Status Set | Sync Queried | Cloud Call | Post-Sync | Result |
|-----------|------------|------------|-------------|------------|-----------|--------|
| CREATE | ✅/❌ [loc] | ✅/❌ [loc] | ✅/❌ [loc] | ✅/❌ [loc] | ✅/❌ [loc] | PASS/FAIL |
| UPDATE | ✅/❌ [loc] | ✅/❌ [loc] | ✅/❌ [loc] | ✅/❌ [loc] | ✅/❌ [loc] | PASS/FAIL |
| DELETE | ✅/❌ [loc] | ✅/❌ [loc] | ✅/❌ [loc] | ✅/❌ [loc] | ✅/❌ [loc] | PASS/FAIL |

`[loc]` = file:line reference for the verified code

### 3. Sync Status State Machine

```
[Visual diagram of actual state transitions found in code]
Highlight any dead-end states or missing transitions
```

### 4. Detailed Findings

For each broken or at-risk sync path:

- **ID:** SYNC-[CRUD_OP]-[N]
- **Severity:** Critical / High / Medium / Low
- **Entity:** Which entity is affected
- **Operation:** CREATE / UPDATE / DELETE / PULL
- **Broken Link:** Which step in the sync chain fails (e.g., "Status not set" / "Query doesn't include status" / "Cloud API not called")
- **Location:** File:line for the broken code
- **Root Cause:** Why this link is broken (code excerpt)
- **Impact:** What the user experiences (e.g., "deleted tasks reappear on other devices")
- **Fix:** Specific code change to repair the sync path
- **Verification Test:** How to confirm the fix works

### 5. Sync Path Trace Per Entity

For the most critical entities, provide the complete code path trace:

```
CREATE: UserTapsAdd → TaskViewModel.createTask() [TaskViewModel.kt:45]
  → TaskRepository.create() [TaskRepository.kt:72]
  → TaskDao.insert(entity.copy(syncStatus=PENDING_CREATE)) [TaskDao.kt:18]
  → SyncEngine.syncItem(id) [SyncEngine.kt:95]
  → SyncEngine.pushLocalChanges() queries PENDING_CREATE ✅ [SyncEngine.kt:112]
  → RemoteDataSource.createTask(dto) [TaskRemoteDataSource.kt:34]
  → TaskDao.markSynced(id, serverTimestamp) [TaskDao.kt:45]
  ✅ VERIFIED: Complete sync path
```

```
DELETE: UserSwipesDelete → TaskViewModel.deleteTask() [TaskViewModel.kt:78]
  → TaskRepository.delete() [TaskRepository.kt:142]
  → TaskDao.softDelete(id) [TaskDao.kt:62] — sets isDeleted=true
  ❌ BROKEN: syncStatus NOT set to PENDING_DELETE
  → SyncEngine.pushLocalChanges() queries PENDING_* [SyncEngine.kt:112]
  → PENDING_DELETE never queried — delete never reaches cloud
  ❌ BROKEN: Cloud delete never fires
```

### 6. Prioritized Fix List

Ordered by data integrity impact:
1. **[Critical]** [Entity] [Operation] — [One-sentence description of break and fix]
2. **[High]** ...
3. ...

---

## Example Output

```markdown
# CRUD Sync Verification Report — TaskMaster App

## Entity Sync Inventory

| Entity | Cloud Target | Direction | Status Field | Trigger | Verified |
|--------|-------------|-----------|-------------|---------|----------|
| Task | Firestore tasks/{id} | Bidirectional | syncStatus | Immediate + periodic | ❌ DELETE broken |
| Category | Firestore categories/{id} | Bidirectional | syncStatus | Immediate | ✅ All ops verified |
| Tag | Firestore tags/{id} | Bidirectional | syncStatus | Periodic only | ⚠️ Slow sync |

## CRUD Sync Matrix: Task

| Op | Local Write | Status Set | Queried | Cloud Call | Post-Sync | Result |
|----|------------|-----------|---------|-----------|-----------|--------|
| CREATE | ✅ Repo:72 | ✅ Repo:74 | ✅ Sync:112 | ✅ Remote:34 | ✅ Dao:45 | PASS |
| UPDATE | ✅ Repo:98 | ✅ Repo:101 | ✅ Sync:112 | ✅ Remote:52 | ✅ Dao:45 | PASS |
| DELETE | ✅ Repo:142 | ❌ Repo:142 | ❌ Sync:112 | ❌ N/A | ❌ N/A | **FAIL** |

## SYNC-DELETE-1: Task Deletion Not Synced to Cloud

**Severity:** Critical
**Entity:** Task
**Operation:** DELETE
**Broken Link:** syncStatus never set to PENDING_DELETE

**Location:** TaskRepository.kt:142

**Root Cause:**
```kotlin
// TaskRepository.kt:142
suspend fun delete(taskId: String) {
    taskDao.softDelete(taskId)
    // softDelete() only sets isDeleted = true
    // syncStatus is NOT changed — stays as SYNCED
}
```

Meanwhile, the DAO's softDelete only touches isDeleted:
```kotlin
// TaskDao.kt:62
@Query("UPDATE tasks SET is_deleted = 1 WHERE id = :id")
suspend fun softDelete(id: String)
```

And the sync engine queries:
```kotlin
// SyncEngine.kt:112
@Query("SELECT * FROM tasks WHERE sync_status IN ('PENDING_CREATE', 'PENDING_UPDATE')")
suspend fun getPendingSync(): List<TaskEntity>
// PENDING_DELETE is not in the query!
```

**Impact:** Deleted tasks remain in Firestore. Other devices still show them. Fresh installs pull them back.

**Fix:**
```kotlin
// TaskDao.kt — add combined operation
@Query("""
    UPDATE tasks
    SET is_deleted = 1,
        sync_status = 'PENDING_DELETE',
        local_updated_at = :timestamp
    WHERE id = :id
""")
suspend fun softDeleteAndMarkPending(id: String, timestamp: Long = System.currentTimeMillis())

// TaskRepository.kt:142 — use new DAO method
suspend fun delete(taskId: String) {
    taskDao.softDeleteAndMarkPending(taskId)
    if (connectivityObserver.isOnline()) {
        syncEngine.syncItem(taskId)
    }
}

// SyncEngine.kt:112 — include PENDING_DELETE in query
@Query("SELECT * FROM tasks WHERE sync_status IN ('PENDING_CREATE', 'PENDING_UPDATE', 'PENDING_DELETE')")
suspend fun getPendingSync(): List<TaskEntity>

// SyncEngine.kt — add delete handler in syncItem()
SyncStatus.PENDING_DELETE -> {
    remoteDataSource.deleteTask(item.id)
    taskDao.hardDelete(item.id)
}
```

**Verification Test:**
1. Create task → verify in Firestore
2. Delete task locally
3. Query Room: confirm syncStatus = PENDING_DELETE
4. Trigger sync (or wait for periodic)
5. Query Firestore: confirm task document deleted
6. Install on new device: confirm task does not appear
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on CRUD sync verification
- **ST-02** (Structured Sequential Instructions) — Operation-by-operation trace
- **RT-05** (Evidence-Based Reasoning) — Require exact code path traces with file:line
- **RT-01** (Chain-of-Thought) — Step-by-step sync path reasoning
- **DT-02** (Specific Focus Areas) — Each CRUD operation as a distinct focus area
- **ST-03** (Output Format Templates) — Structured verification matrices
- **DS-06** (Prioritization Guidance) — Severity-based ordering
- **QA-01** (Chain-of-Verification) — State machine completeness check

---

## Related Prompts

- `android_data_integrity_audit.md` — Broader data integrity audit across all workflows
- `android_silent_data_loss_detection.md` — Finds subtle data loss patterns beyond sync
- `android_sync_architecture_review.md` — Overall sync design and architecture
- `android_offline_conflict_resolution_review.md` — Conflict handling deep dive
- `android_room_database_query_review.md` — Room query correctness
- `android_workmanager_background_review.md` — Background sync worker review

---

## Customization Guide

- **For Firebase Realtime Database:** Replace Firestore references with RTDB paths. Check `.setValue()`, `.updateChildren()`, `.removeValue()` calls. Verify `.info/connected` listener for online/offline detection.
- **For Firestore:** Check `set()`, `update()`, `delete()` calls. Verify `WriteBatch` usage for multi-entity operations. Check offline persistence settings (`FirebaseFirestoreSettings`).
- **For REST APIs:** Verify HTTP methods (POST for create, PUT/PATCH for update, DELETE for delete). Check response status code handling. Verify request payload serialization.
- **For apps with server-assigned IDs:** Pay extra attention to the CREATE path — local UUID must be replaced with server ID, and all foreign key references must be updated.
- **For apps with real-time listeners:** Verify that listener-based pull sync doesn't conflict with push sync (e.g., local delete triggers push, but listener receives the "old" state before delete propagates).
