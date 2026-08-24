---
title: "Android Data Integrity Audit"
category: mobile/android/targeted-reviews
description: "Android Data Integrity Audit."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - audit
  - data
  - integrity
  - mobile
  - reviews
updated: "2026-03-19"
related_prompts: []
---

# Android Data Integrity Audit

**Objective:** Conduct a comprehensive audit of all data handling workflows in an Android application, tracing every user data operation (create, read, update, delete) through the complete lifecycle — from UI action through ViewModel, Repository, local database, sync queue, and cloud — to identify any path where data can be lost, corrupted, silently dropped, or left in an inconsistent state.

**When to Use:** Use this prompt when users report data inconsistencies (e.g., deleted items reappearing, edits not persisting, data not syncing to cloud), before launching multi-device support, after refactoring data or sync layers, when adding new entity types, or as a periodic health check on data reliability. This is the "big picture" audit — use the more targeted `android_crud_sync_verification.md` or `android_silent_data_loss_detection.md` for focused investigations.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the actual data flow end-to-end** — Don't flag based on pattern matching or code structure alone. Follow the data from the UI action through every layer to the cloud (or from cloud back to UI) and confirm the issue causes real data loss, corruption, or inconsistency.
2. **Check for existing safeguards** — Search for retry logic, error recovery, conflict resolution, data validation, or compensating transactions that may already address the concern.
3. **Understand the business context** — Not all data requires the same integrity guarantees. A cached preference and a financial transaction have different requirements. Consider the data's criticality.
4. **Confirm with concrete scenarios** — Describe the exact sequence of events that triggers the issue (user action → what happens → what goes wrong).
5. **Provide specific file:line locations** — Every finding MUST include exact code locations (e.g., `TaskRepository.kt:142`).

**Finding NO issues is an acceptable outcome.** If data handling is correct and robust, say so with confidence. Don't manufacture data integrity concerns.

### False-Positive Prevention

- ❌ Do NOT flag eventual consistency as a bug (it's a valid architectural choice for many data types)
- ❌ Do NOT flag optimistic UI updates as data loss (the UI showing changes before sync confirmation is intentional)
- ❌ Do NOT assume missing error handling without tracing complete flows including base classes and interceptors
- ❌ Do NOT flag soft-delete patterns as "data not really deleted" without understanding the sync strategy
- ❌ Do NOT report theoretical issues without demonstrating a concrete scenario that triggers them
- ✅ DO trace each operation through ALL layers (UI → ViewModel → UseCase → Repository → DAO/API → Sync)
- ✅ DO check what happens when operations are interrupted at each layer boundary
- ✅ DO verify that error states are surfaced to the user, not silently swallowed
- ✅ DO test data flows under adverse conditions (process death, no network, low memory, concurrent access)

---

### Phase 1: Data Architecture Mapping

Map the complete data architecture before analyzing individual flows:

#### 1.1 Entity Inventory

For every entity/data type in the app, document:

* **Entity name and location** (Room entity, data class, DTO)
* **Storage mechanism** (Room, DataStore, SharedPreferences, file system)
* **Cloud counterpart** (Firestore collection, RTDB node, REST endpoint)
* **Sync strategy** (real-time listener, periodic sync, on-demand, write-through)
* **Sync metadata fields** (syncStatus, lastModifiedAt, serverTimestamp, isDeleted, version)
* **Criticality level** (Critical: user-created content, High: settings/preferences, Medium: cached data, Low: derived/computed data)

#### 1.2 Data Flow Architecture

Map the layered architecture:

* **UI Layer** — Compose screens, Fragment/Activity, UI state holders
* **ViewModel Layer** — StateFlow/LiveData, UI state management, user action handlers
* **Domain Layer** (if present) — UseCases/Interactors
* **Repository Layer** — Data source coordination, cache strategy, offline-first logic
* **Local Data Source** — Room DAOs, DataStore, file operations
* **Remote Data Source** — API clients, Firebase references, cloud SDK calls
* **Sync Layer** — Sync engine, queue, WorkManager workers, conflict resolution
* **Error Handling** — Global error handlers, interceptors, retry policies

#### 1.3 Dependency Injection Scope Verification

Check that data layer components have appropriate DI scopes:

* Are Repositories scoped as singletons (not recreated per screen)?
* Are DAOs provided correctly (not creating multiple database instances)?
* Are sync workers using the same data source instances as the rest of the app?
* Could scope mismatches cause operations to target different database instances or stale caches?

---

### Phase 2: CRUD Operation Integrity Analysis

For EACH entity type identified in Phase 1, trace all four CRUD operations:

#### 2.1 CREATE Flow Audit

Trace the complete creation path:

* **UI → ViewModel:** Is user input validated before dispatching? Can double-taps create duplicates?
* **ViewModel → Repository:** Is the create call wrapped in proper error handling? What happens if it throws?
* **Repository → Local DB:** Is the item persisted with correct sync metadata (PENDING_CREATE)? Is the insert inside a transaction if multiple tables are involved?
* **Local DB → Sync:** Is the new item queued for sync? What triggers the sync (immediate, periodic, connectivity change)?
* **Sync → Cloud:** Does the cloud create succeed? Is the local item updated with server-assigned IDs/timestamps? What happens on 409 Conflict (item already exists on server)?
* **Failure recovery:** If ANY step fails, is the user notified? Is the operation retryable? Is partial state cleaned up?

#### 2.2 READ Flow Audit

Trace data retrieval paths:

* **Single source of truth:** Does the UI always read from local DB (Room Flow/LiveData), or does it sometimes read directly from cloud?
* **Stale data:** Can the UI show stale data indefinitely? Is there a cache invalidation or refresh mechanism?
* **Deleted item visibility:** Can soft-deleted items leak into UI queries? Are all queries filtered by `is_deleted = 0` (or equivalent)?
* **Empty states:** What happens when cloud data hasn't been pulled yet? Is there a loading/empty state distinction?
* **Referential integrity in reads:** If displaying a task with its category, what happens if the category was deleted but the task still references it?

#### 2.3 UPDATE Flow Audit

Trace modification paths:

* **Optimistic updates:** Does the UI reflect changes immediately? If sync later fails, is the optimistic update rolled back or does the user see stale state?
* **Field-level tracking:** Are individual field modifications tracked (for field-level merge), or is the entire entity marked as modified?
* **Concurrent local edits:** What happens if the user rapidly edits the same item? Are intermediate states preserved or coalesced?
* **ViewModel → Repository:** Is the update call idempotent? What happens if the same update is dispatched twice?
* **Sync status transition:** Does update correctly transition sync status (SYNCED → PENDING_UPDATE)? What about PENDING_CREATE → still PENDING_CREATE (edit before first sync)?
* **Version/timestamp management:** Is `localUpdatedAt` set correctly? Could clock manipulation or timezone changes corrupt timestamps?

#### 2.4 DELETE Flow Audit

Trace deletion paths (most common source of sync issues):

* **Soft delete implementation:** Is deletion a soft delete (setting `isDeleted = true` + `syncStatus = PENDING_DELETE`) or hard delete?
* **UI removal:** Is the deleted item immediately hidden from UI queries? Are ALL queries filtered correctly?
* **Sync queue:** Is the delete operation queued for cloud sync? Is the queue item distinguishable from update operations?
* **Cloud deletion:** What API call performs the cloud delete? Does it handle "already deleted" (404) gracefully?
* **Post-sync cleanup:** After cloud confirms deletion, is the local record hard-deleted? Or does it linger as a soft-deleted ghost?
* **Cascade behavior:** When a parent entity is deleted, what happens to children? Are child deletions also synced?
* **Undo support:** If the app supports undo-delete, how does this interact with the sync queue? Can an undo race with a sync that already pushed the delete to cloud?
* **Delete during offline:** If the user deletes while offline, is the delete preserved across app restarts and process death? Is it synced when connectivity returns?

---

### Phase 3: Sync Pipeline Integrity

#### 3.1 Sync Queue Analysis

* **Queue persistence:** Is the sync queue persisted (Room table) or in-memory only? Does it survive process death?
* **Queue ordering:** Are operations processed in the correct order? (Create before Update, Update before Delete for the same entity)
* **Queue deduplication:** If the user creates then immediately updates an item, are redundant sync operations coalesced?
* **Queue overflow:** Is there a maximum queue size? What happens when it's exceeded?
* **Queue item metadata:** Does each queue item contain enough information to execute the operation (entity type, operation type, entity ID, payload, retry count, created timestamp)?

#### 3.2 Push Sync Verification

For each entity type, verify the push flow:

* **PENDING_CREATE items:** Are they pushed with the correct API call? Is the response (server ID, timestamp) written back to the local entity?
* **PENDING_UPDATE items:** Are they pushed with the correct API call? Is version/timestamp conflict detection happening?
* **PENDING_DELETE items:** Are they pushed? Is the cloud deletion confirmed before local hard-delete?
* **Error handling per status code:**
  - 200/201: Mark synced — is `syncStatus` updated atomically with server metadata?
  - 400: Validation error — is the user notified? Is the queue item removed or kept for retry?
  - 401/403: Auth error — is sync paused until re-authentication?
  - 404: Entity not found on server — handle gracefully (already deleted?) vs. unexpected
  - 409: Conflict — is conflict resolution triggered?
  - 429: Rate limited — is backoff applied?
  - 5xx: Server error — retry with exponential backoff?

#### 3.3 Pull Sync Verification

* **Incremental sync:** Is the app pulling only changes since last sync, or doing full pulls?
* **New remote items:** Are they inserted locally with `SYNCED` status?
* **Updated remote items:** If the local item is `SYNCED`, is it updated? If the local item is `PENDING_UPDATE`, is conflict resolution triggered?
* **Deleted remote items:** Are remotely deleted items removed locally? Is the deletion propagated through related entities?
* **Pagination:** For large datasets, is pull sync paginated? Can partial page failures leave the sync in an inconsistent state?

#### 3.4 Sync Timing and Triggers

* **When does sync fire?** On connectivity change? Periodic? On each write? App foreground?
* **Sync debouncing:** Are rapid changes debounced to avoid excessive sync operations?
* **Sync during background:** Does WorkManager (or equivalent) handle background sync? Are constraints (network, battery) set correctly?
* **Sync on fresh install:** What happens when the app is installed on a new device? Is initial pull handled correctly?

---

### Phase 4: Data Integrity Under Adverse Conditions

#### 4.1 Process Death Recovery

* **Mid-write process death:** If the app is killed while writing to Room, is the transaction atomic?
* **Mid-sync process death:** If the app is killed during sync, are queue items left in a recoverable state? (Not stuck in "processing" limbo)
* **SavedStateHandle:** Is critical in-progress user input saved to survive process death?
* **ViewModel recreation:** After process death, does the ViewModel correctly restore state from Room, not from a stale in-memory cache?

#### 4.2 Concurrent Access

* **Multi-screen access:** If two screens can modify the same entity, are there race conditions?
* **Background sync vs. user edit:** If a sync pull updates an entity while the user is editing it in the UI, what happens?
* **Database thread safety:** Is Room accessed from appropriate dispatchers? Are there raw SQLite calls that bypass Room's thread safety?

#### 4.3 Network Edge Cases

* **Flaky connectivity:** Rapid online/offline toggling — does the sync queue get corrupted?
* **Slow network:** Timeout during sync — is the partial response handled?
* **Airplane mode with WiFi:** Does the connectivity check accurately detect internet availability (not just WiFi connection)?
* **Server maintenance/downtime:** Extended 503 responses — does the app handle gracefully without data loss?

#### 4.4 Storage Edge Cases

* **Low storage:** What happens when Room insert fails due to disk full? Is the user notified?
* **Database migration:** If a Room migration fails, is data preserved? Is there a fallback?
* **Corrupted database:** If Room database becomes corrupted, what recovery mechanisms exist? Is cloud data used to rebuild?

---

### Phase 5: Cross-Cutting Concerns

#### 5.1 Transaction Boundaries

* **Multi-entity operations:** When a user action affects multiple entities (e.g., moving a task to a different category), are all changes in a single Room transaction?
* **Sync atomicity:** Are related entity changes synced atomically to the cloud, or can partial sync leave cloud data inconsistent?
* **Rollback behavior:** If a multi-entity operation partially fails, is the entire operation rolled back or are some changes persisted?

#### 5.2 Referential Integrity

* **Foreign key enforcement:** Are Room foreign keys defined and enforced?
* **Cascade deletes:** When a parent is deleted, are children handled (cascade delete, set null, or restrict)?
* **Orphan detection:** Is there logic to detect and clean up orphaned records (children whose parent was deleted)?
* **Cross-entity sync order:** When syncing related entities, is the parent synced before the child? What happens if the child syncs first and the parent doesn't exist on the server yet?

#### 5.3 Data Validation

* **Input validation:** Is user input validated before persistence (not just at the UI level)?
* **Schema validation:** Are data types, lengths, and constraints enforced at the database level?
* **Cloud data validation:** Is data pulled from the cloud validated before inserting into Room? Could corrupted or malicious cloud data crash the app?
* **Migration validation:** After database migrations, is data integrity verified?

---

## Expected Output

Provide a comprehensive data integrity audit report:

### 1. Executive Summary

- Overall data integrity health rating (Healthy / Needs Attention / Critical Issues)
- Total entity types audited
- Total findings by severity (Critical / High / Medium / Low)
- Top 3 highest-risk issues with one-sentence descriptions

### 2. Entity Inventory Matrix

| Entity | Storage | Cloud Target | Sync Strategy | Sync Metadata | Criticality | Issues |
|--------|---------|-------------|---------------|---------------|-------------|--------|
| [Name] | [Room/DataStore] | [Firestore/RTDB/API] | [Strategy] | [Fields] | [Level] | [Count] |

### 3. CRUD Flow Audit Results

For each entity:

| Operation | UI→VM | VM→Repo | Repo→Local | Local→Sync | Sync→Cloud | Status |
|-----------|-------|---------|------------|------------|------------|--------|
| Create | ✅/⚠️/❌ | ✅/⚠️/❌ | ✅/⚠️/❌ | ✅/⚠️/❌ | ✅/⚠️/❌ | [Summary] |
| Read | ✅/⚠️/❌ | ✅/⚠️/❌ | ✅/⚠️/❌ | N/A | N/A | [Summary] |
| Update | ✅/⚠️/❌ | ✅/⚠️/❌ | ✅/⚠️/❌ | ✅/⚠️/❌ | ✅/⚠️/❌ | [Summary] |
| Delete | ✅/⚠️/❌ | ✅/⚠️/❌ | ✅/⚠️/❌ | ✅/⚠️/❌ | ✅/⚠️/❌ | [Summary] |

### 4. Detailed Findings

For each issue found:

- **ID:** DATA-INTEGRITY-[N]
- **Severity:** Critical / High / Medium / Low
- **Category:** CREATE / READ / UPDATE / DELETE / SYNC / TRANSACTION / REFERENTIAL
- **Location:** File:line(s)
- **Scenario:** Step-by-step description of how the issue is triggered
- **Current Behavior:** What actually happens (with code excerpt)
- **Expected Behavior:** What should happen
- **Data Impact:** What data is lost, corrupted, or left inconsistent
- **Recommended Fix:** Specific code changes with rationale
- **Test Case:** How to verify the fix

### 5. Data Flow Diagram

Visual representation showing:
- Data path for each CRUD operation
- Layer boundaries and handoff points
- Identified failure points marked with severity

### 6. Adverse Condition Analysis

| Condition | Impact | Current Handling | Recommendation |
|-----------|--------|-----------------|----------------|
| Process death during sync | [Impact] | [Current] | [Fix] |
| Network loss during write | [Impact] | [Current] | [Fix] |
| Concurrent access | [Impact] | [Current] | [Fix] |
| Low storage | [Impact] | [Current] | [Fix] |

### 7. Prioritized Remediation Plan

- **Critical (Immediate):** Data loss or corruption that users can trigger through normal usage
- **High (This Sprint):** Data inconsistencies that occur under common adverse conditions
- **Medium (Next Sprint):** Edge cases that are unlikely but have significant impact
- **Low (Backlog):** Minor inconsistencies or improvements to data handling robustness

---

## Example Output

```markdown
# Data Integrity Audit Report — TaskMaster App

## Executive Summary
- **Overall Health:** Critical Issues — 3 Critical, 7 High Priority
- **Entities Audited:** 5 (Task, Category, Tag, Attachment, UserSettings)
- **Most Critical:** Deleted tasks are not synced to cloud (Task DELETE flow broken at Sync→Cloud)

## CRUD Flow Audit: Task Entity

| Operation | UI→VM | VM→Repo | Repo→Local | Local→Sync | Sync→Cloud | Status |
|-----------|-------|---------|------------|------------|------------|--------|
| Create | ✅ | ✅ | ✅ | ✅ | ✅ | Healthy |
| Read | ✅ | ✅ | ✅ | N/A | N/A | Healthy |
| Update | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Optimistic update not rolled back on sync failure |
| Delete | ✅ | ✅ | ✅ | ❌ | ❌ | **Delete not queued for sync** |

## Critical Finding: DATA-INTEGRITY-1

**Severity:** Critical
**Category:** DELETE / SYNC
**Location:** TaskRepository.kt:142, SyncEngine.kt:87

**Scenario:**
1. User deletes a task
2. TaskRepository.softDelete() sets `isDeleted = true`
3. UI correctly hides the task
4. SyncEngine.pushLocalChanges() queries for `syncStatus != SYNCED`
5. But softDelete() does NOT update syncStatus to PENDING_DELETE
6. The deleted task is never picked up by the sync queue
7. Cloud still has the task; other devices still show it

**Current Behavior:**
```kotlin
// TaskRepository.kt:142
suspend fun delete(taskId: String) {
    taskDao.softDelete(taskId)  // Sets isDeleted = true ONLY
    // Missing: syncStatus not set to PENDING_DELETE
}
```

**Expected Behavior:**
```kotlin
suspend fun delete(taskId: String) {
    taskDao.softDeleteAndMarkPending(taskId)
    // This should atomically set isDeleted = true AND syncStatus = PENDING_DELETE
    if (connectivityObserver.isOnline()) {
        syncEngine.syncItem(taskId)
    }
}
```

**Data Impact:** Deleted tasks remain on cloud and reappear on other devices or after reinstall.

**Test Case:**
1. Create a task and verify it syncs to cloud
2. Delete the task locally
3. Trigger sync
4. Verify the task is deleted from cloud
5. Install on new device and verify task does not appear
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on end-to-end data integrity
- **ST-02** (Structured Sequential Instructions) — Phased audit approach
- **RT-02** (Multi-Dimensional Analysis) — Every CRUD operation × every entity × every layer
- **RT-05** (Evidence-Based Reasoning) — Require file:line locations and concrete scenarios
- **DT-01** (Hierarchical Task Breakdown) — Architecture → CRUD flows → sync pipeline → edge cases
- **ST-03** (Output Format Templates) — Structured matrices and finding format
- **DS-06** (Prioritization Guidance) — Severity-based remediation
- **QA-02** (Adversarial Stress-Test) — Adverse condition analysis

---

## Related Prompts

- `android_crud_sync_verification.md` — Focused verification that each CRUD op syncs correctly
- `android_silent_data_loss_detection.md` — Finds subtle/hidden data loss patterns
- `android_sync_architecture_review.md` — Overall sync design review
- `android_offline_conflict_resolution_review.md` — Deep dive on conflict handling
- `android_room_database_query_review.md` — Room query correctness and performance
- `android_local_data_security_audit.md` — Local data storage security
- `android_process_death_recovery_review.md` — Process death resilience

---

## Customization Guide

- **For Firebase RTDB apps:** Focus on listener-based sync, `.info/connected` handling, transaction patterns, and fan-out write consistency
- **For Firestore apps:** Emphasize offline persistence settings, snapshot listener behavior, batch write atomicity, and subcollection cascade deletion
- **For REST API backends:** Add HTTP status code handling per operation, ETag/If-Match header verification, and API versioning impact on sync
- **For multi-user/collaborative apps:** Add concurrent user edit analysis, real-time listener conflict detection, and shared entity permission changes
- **For apps with file attachments:** Add file upload/download integrity, partial upload recovery, and attachment-entity relationship consistency
- **For encrypted data:** Add encryption/decryption at sync boundaries, key rotation impact on synced data, and encrypted field searchability
