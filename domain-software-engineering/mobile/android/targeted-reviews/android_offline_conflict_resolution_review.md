---
title: "Android Offline Conflict Resolution Review"
category: mobile/android/targeted-reviews
description: "Android Offline Conflict Resolution Review."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - conflict
  - mobile
  - offline
  - resolution
  - reviews
updated: "2026-03-19"
related_prompts: []
---

# Android Offline Conflict Resolution Review

**Objective:** Conduct a targeted review of conflict detection and resolution logic in offline-first Android applications, analyzing conflict identification algorithms, resolution strategies per entity type, user experience patterns, and data integrity guarantees.

**When to Use:** Use this prompt when debugging data inconsistencies after sync, before adding new entity types to offline sync, when users report "lost" data, during architecture review of sync systems, or when planning multi-device support enhancements.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the actual sync and conflict flow** - Don't flag based on pattern matching alone. Verify that the suspected issue actually causes data loss or corruption.
2. **Check for existing conflict handling** - Search for merge strategies, conflict UI, or resolution logic that may already address the concern.
3. **Understand the context** - Consider WHY specific resolution strategies are chosen. Business requirements often dictate conflict behavior.
4. **Confirm actual data integrity impact** - Test with real conflict scenarios, not just code patterns.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `SyncEngine.kt:234`).

**Finding NO issues is an acceptable outcome.** If conflict resolution handles edge cases correctly, say so with confidence. Don't manufacture data integrity concerns.

### False-Positive Prevention

- ❌ Do NOT flag "last write wins" as always wrong (it's valid for many use cases)
- ❌ Do NOT flag based solely on algorithm choice without understanding data model
- ❌ Do NOT assume missing conflict handling without searching the codebase
- ❌ Do NOT report theoretical data loss without demonstrating actual scenarios
- ✅ DO test with actual multi-device conflict scenarios
- ✅ DO understand the trade-offs between consistency and availability
- ✅ DO check for user-facing conflict resolution UI where appropriate
- ✅ DO consider the probability and impact of actual conflicts

---

### 1. Conflict Detection Strategy

Analyze how conflicts are identified:

* **Detection Method:**
  - Identify detection approach (timestamp, version vectors, hash comparison)
  - Assess accuracy of conflict detection
  - Check for false positives (detected but not real conflict)
  - Check for false negatives (real conflict missed)

* **Timestamp-Based Detection:**
  - Review client vs. server timestamp usage
  - Check for clock skew handling
  - Assess timestamp precision (seconds vs. milliseconds)
  - Verify timezone handling

* **Version Vector Detection:**
  - Review version increment logic
  - Check for vector merging on sync
  - Assess concurrent edit detection
  - Verify version persistence

* **Field-Level Detection:**
  - Check if detection is record-level or field-level
  - Review granularity of conflict detection
  - Assess partial update conflict handling
  - Verify field modification tracking

### 2. Resolution Strategy Analysis

Evaluate resolution approaches per entity type:

* **Resolution Policies:**
  - Document strategy for each entity type
  - Assess appropriateness for data semantics:
    - Last-Write-Wins (LWW)
    - First-Write-Wins
    - Merge (combine changes)
    - Manual (user decides)
    - Server-Authoritative

* **Automatic Resolution:**
  - Review when automatic resolution is applied
  - Check for data loss in automatic resolution
  - Assess merge algorithm correctness
  - Verify resolution is deterministic

* **Manual Resolution:**
  - Check when users are prompted for resolution
  - Review conflict presentation UI
  - Assess user decision persistence
  - Verify resolution history

### 3. Merge Logic Review

Analyze merging of concurrent changes:

* **Field-Level Merge:**
  - Review field-by-field comparison
  - Check for field type-specific merge (text, numbers, lists)
  - Assess conflict in same field handling
  - Verify merge produces valid entity

* **List/Collection Merge:**
  - Review add/remove conflict handling
  - Check for duplicate detection
  - Assess ordering conflicts
  - Verify list integrity after merge

* **Nested Object Merge:**
  - Review parent-child conflict handling
  - Check for orphan prevention
  - Assess deep merge logic
  - Verify referential integrity

### 4. Edge Case Handling

Evaluate boundary scenarios:

* **Edit-Delete Conflicts:**
  - What happens when A edits while B deletes?
  - Check for resurrection of deleted items
  - Assess user preference enforcement
  - Verify audit trail

* **Create-Create Conflicts:**
  - How are duplicate creations handled?
  - Check for deduplication logic
  - Assess identity collision prevention
  - Verify unique constraint handling

* **Rapid Succession Edits:**
  - What happens with quick successive changes?
  - Check for edit coalescing
  - Assess last change priority
  - Verify no lost intermediate states

* **Long Offline Periods:**
  - How are conflicts from days of offline use handled?
  - Check for batch conflict resolution
  - Assess user notification for many conflicts
  - Verify resolution doesn't overwhelm system

### 5. User Experience

Analyze conflict UX:

* **Conflict Visibility:**
  - Are conflicts surfaced to users appropriately?
  - Check for conflict indicators in UI
  - Assess notification strategy for conflicts
  - Verify non-disruptive conflict handling

* **Resolution Interface:**
  - Review conflict resolution UI
  - Check for clear presentation of options
  - Assess preview of resolution outcomes
  - Verify undo capability

* **Transparency:**
  - Can users see conflict history?
  - Check for explanation of what happened
  - Assess automatic resolution communication
  - Verify no silent data changes

### 6. Data Integrity Guarantees

Evaluate consistency:

* **Post-Resolution Integrity:**
  - Check that resolved state is valid
  - Review constraint enforcement after resolution
  - Assess foreign key integrity
  - Verify no orphaned records

* **Consistency Across Devices:**
  - Check that resolution is consistent everywhere
  - Review resolution propagation
  - Assess eventual consistency guarantees
  - Verify no permanent divergence

* **Audit and Recovery:**
  - Check for conflict audit logging
  - Review recovery from bad resolution
  - Assess rollback capability
  - Verify data recovery options

### 7. Performance Considerations

Analyze efficiency:

* **Detection Performance:**
  - Check conflict detection speed
  - Review batch conflict detection
  - Assess index usage for comparison
  - Verify no full table scans

* **Resolution Performance:**
  - Check resolution processing time
  - Review large conflict set handling
  - Assess UI responsiveness during resolution
  - Verify no ANR risk

### 8. Testing Coverage

Evaluate conflict testing:

* **Test Scenarios:**
  - Check for conflict simulation in tests
  - Review multi-device test setup
  - Assess edge case test coverage
  - Verify resolution correctness tests

---

## Expected Output

Provide a comprehensive conflict resolution review report including:

### 1. Executive Summary
- Overall conflict handling health rating
- Entity types with conflict support
- Critical issues count
- Data loss risk assessment

### 2. Entity Conflict Matrix

| Entity | Detection | Resolution | Merge | User Choice | Issues |
|--------|-----------|------------|-------|-------------|--------|
| [Entity] | [Method] | [Strategy] | [Fields] | [When] | [Count] |

### 3. Conflict Scenario Analysis

| Scenario | Current Behavior | Expected | Risk Level |
|----------|------------------|----------|------------|
| [Scenario] | [Behavior] | [Expected] | [Risk] |

### 4. Detailed Findings

For each issue:
- **Location:** File and method
- **Issue:** Description
- **Impact:** Data integrity effect
- **Severity:** Critical/High/Medium/Low
- **Current Logic:** Problematic code
- **Recommended Fix:** Corrected approach
- **Test Case:** Verification scenario

### 5. Data Loss Risk Assessment

| Scenario | Probability | Impact | Mitigation |
|----------|-------------|--------|------------|
| [Scenario] | [Low/Med/High] | [Description] | [Action] |

### 6. Prioritized Recommendations

Ordered by data integrity impact.

---

## Example Output

```markdown
# Offline Conflict Resolution Review Report

## Executive Summary
- **Overall Health:** Needs Attention - Significant data loss risks
- **Entities with Conflict Handling:** 5 of 8 entity types
- **Detection Method:** Timestamp-based (prone to clock skew)
- **Critical Issues:** 2 | High: 3 | Medium: 4 | Low: 5

## Critical Findings

### CRITICAL-1: Edit-Delete Conflict Causes Silent Data Loss
**Severity:** Critical
**Impact:** User changes permanently lost without notification

**Location:** ConflictResolver.kt

**Scenario:**
1. Device A and B both have Todo "Buy milk"
2. Device A goes offline, edits title to "Buy oat milk"
3. Device B deletes "Buy milk"
4. Device B syncs (delete propagates)
5. Device A comes online and syncs

**Current Behavior:**
```kotlin
class ConflictResolver {
    fun resolve(local: TodoEntity?, remote: TodoEntity?): ResolvedTodo {
        return when {
            // If remote is null (deleted), accept deletion
            remote == null -> {
                ResolvedTodo.Deleted  // Local edits LOST!
            }
            local == null -> {
                ResolvedTodo.Created(remote)
            }
            else -> {
                resolveEditConflict(local, remote)
            }
        }
    }
}
```

**Problem:**
- User A's edit to "Buy oat milk" is silently discarded
- No notification that edit was lost
- No option to restore edited version

**Recommended Fix:**
```kotlin
class ConflictResolver @Inject constructor(
    private val conflictStore: ConflictStore,
    private val notificationService: ConflictNotificationService
) {
    suspend fun resolve(
        local: TodoEntity?,
        remote: TodoEntity?,
        lastSyncedState: TodoEntity?
    ): ResolvedTodo {
        return when {
            remote == null && local != null -> {
                // Remote deleted, but local exists
                val localWasEdited = local.modifiedAt > (lastSyncedState?.modifiedAt ?: 0)

                if (localWasEdited) {
                    // User edited after sync - DON'T silently delete!
                    conflictStore.saveEditDeleteConflict(
                        EditDeleteConflict(
                            entityType = "Todo",
                            entityId = local.id,
                            editedVersion = local,
                            deletedBy = remote.deletedBy,
                            deletedAt = remote.deletedAt
                        )
                    )

                    // Notify user of conflict
                    notificationService.notifyEditDeleteConflict(local)

                    // Keep local version until user decides
                    ResolvedTodo.Conflicted(local)
                } else {
                    // Local wasn't edited since sync, safe to delete
                    ResolvedTodo.Deleted
                }
            }
            // ... other cases
        }
    }
}

// UI for edit-delete conflict
@Composable
fun EditDeleteConflictDialog(
    conflict: EditDeleteConflict,
    onKeepEdited: () -> Unit,
    onAcceptDelete: () -> Unit
) {
    AlertDialog(
        title = { Text("Sync Conflict") },
        text = {
            Column {
                Text("You edited '${conflict.editedVersion.title}' while another device deleted it.")
                Spacer(Modifier.height(8.dp))
                Text("What would you like to do?")
            }
        },
        confirmButton = {
            Button(onClick = onKeepEdited) {
                Text("Keep My Changes")
            }
        },
        dismissButton = {
            TextButton(onClick = onAcceptDelete) {
                Text("Accept Deletion")
            }
        }
    )
}
```

---

### CRITICAL-2: No Detection of Concurrent Edits to Same Field
**Severity:** Critical
**Impact:** Last write wins silently, losing user's changes

**Location:** TodoConflictDetector.kt

**Scenario:**
1. Device A and B both have Todo "Buy groceries" with description "eggs, milk"
2. Device A edits description to "eggs, milk, bread"
3. Device B (offline) edits description to "eggs, milk, cheese"
4. Device B comes online
5. Last timestamp wins - one user's edit lost

**Current Implementation:**
```kotlin
fun resolveConflict(local: TodoEntity, remote: TodoEntity): TodoEntity {
    // Simple timestamp comparison - no field awareness
    return if (local.modifiedAt > remote.modifiedAt) {
        local  // Remote user's changes LOST
    } else {
        remote  // Local user's changes LOST
    }
}
```

**Recommended Fix - Field-Level Merge:**
```kotlin
data class FieldModification(
    val fieldName: String,
    val modifiedAt: Long,
    val value: Any?
)

class FieldLevelConflictResolver {
    fun merge(
        local: TodoEntity,
        remote: TodoEntity,
        base: TodoEntity  // Last synced state
    ): MergeResult {
        val conflicts = mutableListOf<FieldConflict>()
        val merged = local.copy()

        // Compare each field
        val fieldsToMerge = listOf(
            Triple("title", local.title to local.titleModifiedAt, remote.title to remote.titleModifiedAt),
            Triple("description", local.description to local.descriptionModifiedAt, remote.description to remote.descriptionModifiedAt),
            Triple("dueDate", local.dueDate to local.dueDateModifiedAt, remote.dueDate to remote.dueDateModifiedAt)
        )

        for ((fieldName, localField, remoteField) in fieldsToMerge) {
            val (localValue, localModified) = localField
            val (remoteValue, remoteModified) = remoteField
            val baseValue = getBaseValue(base, fieldName)

            when {
                // Only local changed
                localValue != baseValue && remoteValue == baseValue -> {
                    merged.setField(fieldName, localValue)
                }
                // Only remote changed
                remoteValue != baseValue && localValue == baseValue -> {
                    merged.setField(fieldName, remoteValue)
                }
                // Both changed to same value - no conflict
                localValue == remoteValue -> {
                    merged.setField(fieldName, localValue)
                }
                // Both changed to different values - CONFLICT
                localValue != remoteValue -> {
                    conflicts.add(FieldConflict(
                        fieldName = fieldName,
                        localValue = localValue,
                        remoteValue = remoteValue,
                        localModifiedAt = localModified,
                        remoteModifiedAt = remoteModified
                    ))
                }
            }
        }

        return if (conflicts.isEmpty()) {
            MergeResult.AutoMerged(merged)
        } else {
            MergeResult.RequiresResolution(merged, conflicts)
        }
    }
}

// For text fields, try intelligent merge
fun mergeTextFields(
    local: String,
    remote: String,
    base: String
): TextMergeResult {
    // If both added to the end, combine
    if (local.startsWith(base) && remote.startsWith(base)) {
        val localAddition = local.removePrefix(base)
        val remoteAddition = remote.removePrefix(base)
        return TextMergeResult.Merged("$base$localAddition$remoteAddition")
    }

    // Otherwise, needs manual resolution
    return TextMergeResult.Conflict(local, remote)
}
```

---

### HIGH-1: Clock Skew Not Handled
**Severity:** High
**Impact:** Wrong winner selected in conflicts

**Location:** ConflictDetector.kt

**Scenario:**
- Device A's clock is 5 minutes ahead
- Device A edits at "10:05" (actually 10:00)
- Device B edits at "10:02" (correct time)
- Device A wins even though B edited later

**Current Implementation:**
```kotlin
// Uses client timestamps directly
fun detectConflict(local: Entity, remote: Entity): Boolean {
    return local.modifiedAt != remote.modifiedAt
}

fun resolveByTimestamp(local: Entity, remote: Entity): Entity {
    return if (local.modifiedAt > remote.modifiedAt) local else remote
}
```

**Recommended Fix:**
```kotlin
class ClockSkewAwareConflictResolver {
    companion object {
        const val SKEW_TOLERANCE_MS = 5000L  // 5 seconds
    }

    fun resolve(
        local: TodoEntity,
        remote: TodoEntity,
        serverTimestamp: Long
    ): ConflictResolution {
        // Use server timestamp for authoritative ordering when close
        val timeDiff = abs(local.modifiedAt - remote.modifiedAt)

        return when {
            // Clearly different times - use timestamps
            timeDiff > SKEW_TOLERANCE_MS -> {
                if (local.modifiedAt > remote.modifiedAt) {
                    ConflictResolution.UseLocal(local)
                } else {
                    ConflictResolution.UseRemote(remote)
                }
            }
            // Close in time - can't trust timestamps, use server order
            else -> {
                // Server determines order based on which sync arrived first
                // Or: merge fields and flag for review
                ConflictResolution.MergeAndFlag(
                    mergeFields(local, remote),
                    reason = "Edits too close in time to determine order"
                )
            }
        }
    }
}

// Alternative: Use logical clocks (Lamport/Vector)
data class VectorClock(
    val deviceId: String,
    val counter: Long
)

class VectorClockConflictResolver {
    fun compare(local: VectorClock, remote: VectorClock): ClockComparison {
        return when {
            local.counter > remote.counter && local.deviceId == remote.deviceId -> AFTER
            local.counter < remote.counter && local.deviceId == remote.deviceId -> BEFORE
            else -> CONCURRENT  // True conflict - needs resolution
        }
    }
}
```

---

### HIGH-2: Conflict Resolution Not Persisted Correctly
**Severity:** High
**Impact:** Resolved conflicts reappear on next sync

**Location:** SyncCoordinator.kt

**Current Implementation:**
```kotlin
suspend fun handleConflict(local: TodoEntity, remote: TodoEntity) {
    val resolved = conflictResolver.resolve(local, remote)

    // PROBLEM: Only updates local database
    todoDao.update(resolved)

    // Next sync: Remote still has old version, conflict reappears!
}
```

**Recommended Fix:**
```kotlin
suspend fun handleConflict(local: TodoEntity, remote: TodoEntity) {
    val resolved = conflictResolver.resolve(local, remote)

    // 1. Update local with resolution
    todoDao.update(resolved)

    // 2. Mark as resolved with resolution timestamp
    val resolvedVersion = resolved.copy(
        syncVersion = maxOf(local.syncVersion, remote.syncVersion) + 1,
        resolvedAt = System.currentTimeMillis(),
        conflictResolutionId = UUID.randomUUID().toString()
    )
    todoDao.update(resolvedVersion)

    // 3. Push resolution to server
    syncQueue.enqueue(
        SyncOperation.ConflictResolution(
            entityType = "Todo",
            entityId = resolved.id,
            resolvedVersion = resolvedVersion,
            supersedes = listOf(local.syncVersion, remote.syncVersion)
        )
    )

    // 4. Record in conflict history for audit
    conflictHistoryDao.insert(
        ConflictHistoryEntry(
            entityType = "Todo",
            entityId = resolved.id,
            localVersion = local,
            remoteVersion = remote,
            resolution = resolved,
            resolvedAt = System.currentTimeMillis(),
            resolutionMethod = "automatic_timestamp"
        )
    )
}
```

---

## Entity Conflict Matrix

| Entity | Detection | Resolution | Field-Level | User Choice | Issues |
|--------|-----------|------------|-------------|-------------|--------|
| TodoEntity | Timestamp | LWW | No ❌ | Never | 3 |
| ShoppingItem | Timestamp | LWW | No ❌ | Never | 2 |
| NoteEntity | Timestamp | LWW | No ❌ | Never | 2 |
| CalendarEvent | Version | Merge | Partial | Edit conflicts | 1 |
| Message | Server ID | Append-only | N/A | Never | 0 |
| FamilyMember | Timestamp | Server-wins | No | N/A | 0 |

## Conflict Scenario Matrix

| Scenario | Current | Expected | Risk |
|----------|---------|----------|------|
| Edit-Edit same field | Last timestamp wins | Field-level merge or prompt | HIGH |
| Edit-Delete | Delete wins silently | Prompt user, preserve edit option | CRITICAL |
| Create-Create same ID | Undefined/crash | Detect and assign new ID | HIGH |
| Long offline divergence | Mass LWW | Batch review for user | MEDIUM |
| Rapid successive edits | All tracked | Coalesce within window | LOW |

## Data Loss Risk Assessment

| Scenario | Probability | Impact | Mitigation |
|----------|-------------|--------|------------|
| Edit lost to delete | Medium | High - permanent | Conflict UI |
| Field edit overwritten | High | Medium - lost edits | Field-level merge |
| Clock skew wrong winner | Medium | Medium - wrong version | Logical clocks |
| Conflict reappears | Low | Medium - UX annoyance | Resolution persistence |

## Remediation Priority

### Critical (Immediate)
1. Implement edit-delete conflict detection and UI
2. Add field-level conflict detection for todos/notes

### High Priority (This Sprint)
1. Add clock skew tolerance or logical clocks
2. Fix conflict resolution persistence
3. Add conflict history for audit

### Medium Priority (Next Sprint)
1. Implement intelligent text merging
2. Add batch conflict resolution UI
3. Improve conflict notification

### Low Priority (Backlog)
1. Add conflict prevention (edit locking)
2. Implement real-time conflict awareness
3. Add conflict analytics
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Conflict resolution focus
- **ST-02** (Structured Sequential Instructions) - Systematic analysis
- **RT-02** (Multi-Dimensional Analysis) - Detection, resolution, UX
- **RT-05** (Evidence-Based Reasoning) - Scenario-based examples
- **ST-03** (Output Format Templates) - Entity conflict matrix
- **DS-06** (Prioritization Guidance) - Data integrity priority
- **QA-02** (Adversarial Stress-Test) - Edge case analysis

---

## Related Prompts

- `android_sync_architecture_review.md` - For overall sync design
- `android_room_database_query_review.md` - For conflict storage
- `android_firebase_security_rules_audit.md` - For server-side conflict handling
- `android_viewmodel_state_management_review.md` - For conflict UI state
- `mobile_app_security_review.md` - For data integrity security

---

## Customization Guide

- **For Collaborative Apps:** Focus on real-time conflict awareness, operational transforms
- **For Note Apps:** Add rich text merge, paragraph-level conflict detection
- **For Calendar Apps:** Focus on time-based conflicts, recurring event handling
- **For E-commerce:** Add inventory conflict handling, order consistency
- **For Social Apps:** Focus on post/comment threading, reaction conflicts
