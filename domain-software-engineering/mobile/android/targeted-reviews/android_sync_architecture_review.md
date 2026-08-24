---
title: "Android Sync Architecture Review"
category: mobile/android/targeted-reviews
description: "Android Sync Architecture Review."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - architecture
  - mobile
  - review
  - reviews
  - sync
updated: "2026-03-19"
related_prompts: []
---

# Android Sync Architecture Review

**Objective:** Conduct a targeted review of offline-first sync architecture in Android applications, analyzing conflict detection, resolution strategies, queue processing, data consistency, and failure recovery patterns.

**When to Use:** Use this prompt when reviewing apps with offline-first data synchronization, particularly those syncing with Firebase Realtime Database, Firestore, or custom backend APIs. Essential before major sync system changes, after sync-related bugs, when adding new entity types to sync, or during architecture audits of apps with multi-device data consistency requirements.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the actual sync flow** - Don't flag based on pattern matching alone. Verify that the suspected issue actually causes data loss, corruption, or sync failures.
2. **Check for existing safeguards** - Search for retry logic, conflict resolution, or recovery mechanisms that may already address the concern.
3. **Understand the context** - Consider WHY specific sync strategies are chosen. Business requirements and backend constraints affect design.
4. **Confirm actual impact** - Test with real offline/online scenarios before flagging sync issues.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `SyncWorker.kt:87`).

**Finding NO issues is an acceptable outcome.** If the sync architecture handles edge cases correctly, say so with confidence. Don't manufacture sync reliability concerns.

### False-Positive Prevention

- ❌ Do NOT flag all eventual consistency as problematic (it's appropriate for many use cases)
- ❌ Do NOT flag sync design without understanding backend capabilities and constraints
- ❌ Do NOT assume missing error handling without tracing complete sync flows
- ❌ Do NOT report theoretical sync failures without demonstrating actual scenarios
- ✅ DO test with airplane mode, poor connectivity, and server errors
- ✅ DO understand the difference between optimistic and pessimistic sync strategies
- ✅ DO check for proper conflict resolution matching business requirements
- ✅ DO consider the probability and impact of actual sync failures

---

### 1. Sync Queue Architecture Analysis

Review the sync queue implementation for correctness and reliability:

* **Queue Data Structure:**
  - Examine how pending changes are stored locally (Room table, file-based, memory)
  - Verify queue items contain sufficient metadata (timestamp, entity type, operation type, retry count)
  - Check for proper serialization of complex objects in queue items
  - Assess queue ordering guarantees (FIFO, priority-based, dependency-aware)

* **Queue Persistence:**
  - Verify queue survives app restart and process death
  - Check for queue corruption recovery mechanisms
  - Assess maximum queue size handling and overflow strategies
  - Review queue cleanup after successful sync

* **Queue Processing:**
  - Analyze worker/job that processes the queue (WorkManager, custom service)
  - Check for proper batch processing vs. individual item processing
  - Review exponential backoff and retry strategies
  - Assess network condition awareness before processing

### 2. Conflict Detection Mechanisms

Analyze how the app detects data conflicts:

* **Conflict Detection Strategy:**
  - Identify the detection method used (timestamp comparison, version vectors, hash-based, server-side detection)
  - Evaluate clock skew handling for timestamp-based detection
  - Check if all entity types have conflict detection coverage
  - Review detection granularity (field-level vs. record-level)

* **Concurrent Edit Scenarios:**
  - How are simultaneous edits from multiple devices detected?
  - What happens when Device A edits while Device B deletes?
  - How are create-create conflicts handled (same logical identity)?
  - Are rapid successive edits from the same user handled correctly?

* **Timestamp/Version Management:**
  - Review how modification timestamps are assigned (client vs. server)
  - Check for server timestamp enforcement to prevent manipulation
  - Assess version increment strategies for optimistic locking
  - Verify timestamp precision is sufficient for conflict detection

### 3. Conflict Resolution Strategies

Evaluate the resolution logic for each entity type:

* **Resolution Policies by Entity:**
  - Document the resolution strategy for each synced entity type
  - Verify strategies are appropriate for the data semantics:
    - **Last-Write-Wins (LWW):** Appropriate for independent fields
    - **Merge:** Appropriate for additive changes (lists, counters)
    - **Manual Resolution:** Required for critical business data
    - **Server-Authoritative:** When server state is source of truth

* **Merge Logic:**
  - Review field-level merge implementations for complex entities
  - Check for data loss scenarios during automatic merging
  - Assess handling of partially conflicting updates
  - Verify merge produces valid entity state (constraints satisfied)

* **User-Facing Conflict Resolution:**
  - Check if conflicts are surfaced to users when automatic resolution is inappropriate
  - Review conflict resolution UI accessibility and usability
  - Verify users can view conflict history and reverse automatic resolutions
  - Assess notification strategy for unresolved conflicts

### 4. Data Consistency Guarantees

Review mechanisms ensuring data integrity across sync operations:

* **Local-Remote Consistency:**
  - How does the app ensure local Room database matches remote state?
  - Are there periodic full-sync reconciliation mechanisms?
  - How are orphaned records detected and cleaned up?
  - What happens if remote data is corrupted or rolled back?

* **Referential Integrity:**
  - How are parent-child relationships maintained during sync?
  - What happens when a parent entity is deleted while child is being synced?
  - Are foreign key constraints enforced across sync boundaries?
  - How are circular dependencies handled in sync order?

* **Transaction Boundaries:**
  - Are related entity changes synced atomically?
  - What happens if sync is interrupted mid-transaction?
  - How are partial sync failures rolled back or recovered?
  - Are there distributed transaction patterns (saga, two-phase commit)?

### 5. Network and Connection Handling

Analyze network state management:

* **Connection State Management:**
  - How is network connectivity monitored?
  - Are different network types handled appropriately (WiFi, cellular, metered)?
  - Is there a debounce/throttle on connection state changes?
  - How quickly does sync resume after connectivity restored?

* **Offline Behavior:**
  - What is the user experience during offline operation?
  - Are pending changes clearly indicated in the UI?
  - Is there a queue size limit before blocking new changes?
  - How are conflicts that occur during offline period surfaced?

* **Bandwidth Optimization:**
  - Are sync payloads delta-compressed or full replacements?
  - Is there batching of multiple changes to reduce requests?
  - Are large payloads (media, attachments) synced separately?
  - Is sync prioritized (critical data first, media later)?

### 6. Error Handling and Recovery

Assess failure scenarios and recovery:

* **Transient Error Handling:**
  - Review retry strategies for network timeouts and 5xx errors
  - Check exponential backoff implementation (base, max, jitter)
  - Verify retry limits prevent infinite retry loops
  - Assess circuit breaker patterns for persistent failures

* **Permanent Error Handling:**
  - How are validation errors (400) handled differently from transient errors?
  - What happens to queue items that repeatedly fail?
  - Is there a dead letter queue for failed items?
  - Are users notified of items that couldn't sync?

* **Corruption Recovery:**
  - What happens if local database becomes corrupted?
  - Can the app recover from inconsistent sync state?
  - Is there a "reset sync" capability for severe issues?
  - Are sync checkpoints or snapshots maintained for recovery?

### 7. Security and Privacy in Sync

Review security aspects of the sync system:

* **Data in Transit:**
  - Is all sync traffic encrypted (HTTPS/TLS)?
  - Is certificate pinning implemented for sync endpoints?
  - Are sensitive fields encrypted before sync (E2E encryption)?

* **Authentication and Authorization:**
  - Is every sync request authenticated?
  - Are authorization checks performed server-side?
  - What happens if auth token expires during sync?
  - Can users sync data they don't have permission to access?

* **Audit and Logging:**
  - Are sync operations logged for debugging?
  - Is sensitive data excluded from sync logs?
  - Are conflict resolutions audited for accountability?
  - Can sync history be exported for compliance?

### 8. Performance and Scalability

Evaluate sync system performance:

* **Sync Latency:**
  - What is the typical latency from local change to server?
  - Are there real-time sync capabilities (WebSocket, Firebase listeners)?
  - How is sync prioritized for user-visible changes?

* **Battery and Resource Impact:**
  - Are sync operations batched to reduce wakeups?
  - Is sync scheduled during optimal conditions (charging, WiFi)?
  - How does sync impact battery during heavy usage?
  - Are there resource limits on sync workers?

* **Scalability:**
  - How does sync performance degrade with data volume?
  - Is there pagination for initial sync of large datasets?
  - Are there indexes optimized for sync queries?
  - What is the sync behavior during first-time setup with existing data?

---

## Expected Output

Provide a comprehensive sync architecture review report including:

### 1. Executive Summary
- Overall sync architecture health rating (Healthy/Needs Attention/Critical Issues)
- Sync technology stack identified (Firebase, custom, hybrid)
- Entity types covered by sync
- Critical findings count by severity

### 2. Sync Flow Diagram
- Visual representation of data flow (local → queue → remote → conflict resolution)
- Key components and their interactions
- Decision points for conflict handling

### 3. Entity Sync Matrix

| Entity Type | Conflict Detection | Resolution Strategy | Sync Priority | Issues |
|-------------|-------------------|---------------------|---------------|--------|
| [Entity]    | [Method]          | [Strategy]          | [Priority]    | [Count]|

### 4. Detailed Findings by Category

For each review area above:
- **Current Implementation:** Description of how it works
- **Compliance:** Compliant / Partially Compliant / Non-Compliant
- **Issues Found:** List with severity (Critical/High/Medium/Low)
- **Code Examples:** Showing problematic patterns
- **Recommendations:** Specific fixes with rationale

### 5. Conflict Scenario Analysis

| Scenario | Current Behavior | Expected Behavior | Risk Level |
|----------|-----------------|-------------------|------------|
| Edit-Edit conflict | [Behavior] | [Expected] | [Risk] |
| Edit-Delete conflict | [Behavior] | [Expected] | [Risk] |
| Create-Create conflict | [Behavior] | [Expected] | [Risk] |
| Offline period conflicts | [Behavior] | [Expected] | [Risk] |

### 6. Data Loss Risk Assessment
- Scenarios where data could be lost
- Probability and impact ratings
- Mitigation recommendations

### 7. Prioritized Remediation Plan
- **Critical (Immediate):** Data loss or corruption risks
- **High (This Sprint):** Reliability and consistency issues
- **Medium (Next Sprint):** Performance and UX improvements
- **Low (Backlog):** Optimizations and enhancements

---

## Example Output

```markdown
# Sync Architecture Review Report

## Executive Summary
- **Overall Health:** Needs Attention - 2 Critical, 5 High Priority Issues
- **Sync Stack:** Firebase Realtime Database + Room + WorkManager
- **Synced Entities:** Todo, ShoppingItem, Note, CalendarEvent, Message
- **Architecture Pattern:** Offline-first with sync queue

## Critical Findings

### CRITICAL-1: Race Condition in Conflict Resolution
**Severity:** Critical
**Risk:** Data loss when two devices edit simultaneously

**Location:** FamilySyncCoordinator.kt - resolveConflict()

**Current Behavior:**
```kotlin
// PROBLEM: No locking, race condition possible
suspend fun resolveConflict(local: TodoEntity, remote: TodoEntity): TodoEntity {
    // If both are in flight simultaneously, last write wins without merge
    return if (local.modifiedAt > remote.modifiedAt) local else remote
}
```

**Issue:**
When Device A and Device B both edit the same todo offline and come online simultaneously:
1. Both detect the conflict
2. Both run resolveConflict() concurrently
3. Race condition determines which "wins" - unpredictable behavior
4. One device's changes are silently lost

**Evidence:**
- User reports of "disappearing" todo changes
- Crash analytics showing concurrent sync operations

**Recommended Fix:**
```kotlin
// SOLUTION: Use mutex and server timestamp arbitration
private val conflictMutex = Mutex()

suspend fun resolveConflict(local: TodoEntity, remote: TodoEntity): TodoEntity {
    return conflictMutex.withLock {
        // Use server timestamp for authoritative ordering
        val serverTime = firebaseDatabase.getServerTime()

        when {
            // If changes are within 5 seconds, merge fields
            abs(local.modifiedAt - remote.modifiedAt) < 5000 -> {
                mergeEntities(local, remote)
            }
            // Otherwise, use server-verified timestamp
            local.serverModifiedAt > remote.serverModifiedAt -> local
            else -> remote
        }
    }
}

private fun mergeEntities(local: TodoEntity, remote: TodoEntity): TodoEntity {
    return local.copy(
        title = if (local.titleModifiedAt > remote.titleModifiedAt)
                    local.title else remote.title,
        description = if (local.descriptionModifiedAt > remote.descriptionModifiedAt)
                    local.description else remote.description,
        // ... merge each field independently
    )
}
```

**Testing Required:**
- Concurrent sync integration test
- Multi-device conflict simulation

---

### CRITICAL-2: Queue Items Lost on Process Death
**Severity:** Critical
**Risk:** Unsaved changes lost if app killed during sync

**Location:** SyncQueueWorker.kt

**Current Behavior:**
Queue items marked as "processing" in memory, not persisted. If process killed:
- Items marked as processing are orphaned
- User changes never sync to server

**Recommended Fix:**
- Add `processingStartedAt` timestamp to queue items in Room
- On worker start, reset any items stuck in processing state > 5 minutes
- Use database transaction to mark complete only after server confirms

---

## Entity Sync Matrix

| Entity | Detection | Resolution | Priority | Issues |
|--------|-----------|------------|----------|--------|
| TodoEntity | Timestamp | LWW | High | 2 Critical |
| ShoppingItem | Timestamp | LWW | Medium | 1 High |
| NoteEntity | Timestamp | LWW + Content merge | High | 1 Medium |
| CalendarEvent | Version vector | Manual | High | None |
| Message | Server-assigned ID | Append-only | Critical | None |

## Conflict Scenario Analysis

| Scenario | Current | Expected | Risk |
|----------|---------|----------|------|
| Both edit title | Last timestamp wins | Merge or prompt user | HIGH - silent data loss |
| Edit while other deletes | Undefined | Restore with edit | CRITICAL - data loss |
| Same item created offline | Duplicate created | Detect and merge | MEDIUM - duplicates |
| Large offline period | All conflicts auto-resolved | Surface for review | HIGH - unexpected changes |

## Remediation Roadmap

### Phase 1: Critical (This Week)
1. Fix race condition in conflict resolution
2. Persist queue processing state
3. Add edit-delete conflict handling

### Phase 2: High Priority (Sprint)
1. Implement field-level merge for todos
2. Add conflict notification UI
3. Implement queue item dead-letter handling

### Phase 3: Medium Priority (Next Sprint)
1. Add conflict history/audit log
2. Implement manual resolution UI
3. Add periodic full-sync reconciliation
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Focused sync architecture analysis
- **ST-02** (Structured Sequential Instructions) - Systematic review areas
- **RT-02** (Multi-Dimensional Analysis) - Multiple sync aspects covered
- **RT-05** (Evidence-Based Reasoning) - Specific code examples required
- **ST-03** (Output Format Templates) - Structured report format
- **DS-06** (Prioritization Guidance) - Severity-based findings
- **QA-02** (Adversarial Stress-Test) - Conflict scenario analysis

---

## Related Prompts

- `android_room_database_query_review.md` - For sync queue storage optimization
- `android_offline_conflict_resolution_review.md` - Deep dive on conflict handling
- `android_firebase_security_rules_audit.md` - Security rules for synced data
- `android_workmanager_background_review.md` - Sync worker implementation
- `mobile_app_security_review.md` - Data-in-transit security

---

## Customization Guide

- **For Firebase Realtime Database:** Focus on listener-based sync, .info/connected handling, transaction patterns
- **For Firestore:** Emphasize offline persistence settings, snapshot listeners, batch writes
- **For custom REST APIs:** Add API versioning, ETag/If-Match headers, optimistic locking review
- **For multi-tenant apps:** Add tenant isolation verification in sync
- **For encrypted sync:** Add E2E encryption layer analysis
- **For large media sync:** Add chunked upload, resume capability, CDN integration review
