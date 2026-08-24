# Conflict Resolution Strategies

## When Conflicts Happen

Conflicts occur when:
1. User edits data offline, and another user/device modified the same data in Firebase
2. Multiple Firestore listeners update Room simultaneously
3. Network reconnection triggers sync of queued offline writes against changed server state

## Strategy 1: Last-Write-Wins (LWW)

**Best for:** User profiles, calendar events, individual task edits, settings

**How it works:** Compare timestamps. The most recent write wins.

```kotlin
data class Timestamped<T>(
    val data: T,
    val clientTimestamp: Long,    // System.currentTimeMillis() at write time
    val serverTimestamp: Any?,    // FieldValue.serverTimestamp() for Firestore
)

fun <T> resolveLastWriteWins(local: Timestamped<T>, remote: Timestamped<T>): T {
    return if (local.clientTimestamp > remote.clientTimestamp) {
        local.data  // Push local to server
    } else {
        remote.data  // Accept server version, update Room
    }
}
```

**Caveats:**
- Relies on clock accuracy — use `FieldValue.serverTimestamp()` for Firestore writes
- May lose valid edits if clocks are skewed
- Simple but can surprise users ("my change disappeared")

## Strategy 2: Field-Level Merge

**Best for:** Shopping lists, shared documents, collaborative editing

**How it works:** Merge non-conflicting field changes. Only flag true conflicts.

```kotlin
fun mergeTask(local: Task, remote: Task, base: Task): Task {
    return Task(
        id = local.id,
        // Each field resolves independently
        title = pickChanged(local.title, remote.title, base.title),
        completed = pickChanged(local.completed, remote.completed, base.completed),
        dueDate = pickChanged(local.dueDate, remote.dueDate, base.dueDate),
        // For lists, union items
        tags = (local.tags + remote.tags).distinct(),
    )
}

fun <T> pickChanged(local: T, remote: T, base: T): T {
    return when {
        local == base -> remote   // Only remote changed
        remote == base -> local   // Only local changed
        local == remote -> local  // Both changed to same value
        else -> remote            // True conflict — server wins (or prompt user)
    }
}
```

**Requires:** Storing the "base" version before offline edits to detect which fields changed.

## Strategy 3: Set Union (Additive Merge)

**Best for:** Shopping list items, tag collections, achievement lists

**How it works:** Combine items from both sides. Deletions are explicit (tombstoned).

```kotlin
fun mergeShoppingList(local: List<ShoppingItem>, remote: List<ShoppingItem>): List<ShoppingItem> {
    val allItems = mutableMapOf<String, ShoppingItem>()

    // Add all remote items
    remote.forEach { allItems[it.id] = it }

    // Merge local items (local takes precedence for checked state)
    local.forEach { localItem ->
        val existing = allItems[localItem.id]
        if (existing != null) {
            // Item exists in both — merge checked state with OR
            allItems[localItem.id] = localItem.copy(
                checked = localItem.checked || existing.checked
            )
        } else if (!localItem.isDeleted) {
            // New local item — add
            allItems[localItem.id] = localItem
        }
    }

    return allItems.values.filter { !it.isDeleted }.toList()
}
```

## Strategy 4: Max-Wins (Monotonic)

**Best for:** Gamification scores, achievement progress, counters that only go up

**How it works:** Always keep the higher value.

```kotlin
fun resolveScore(local: Int, remote: Int): Int = maxOf(local, remote)

fun resolveAchievement(local: Achievement, remote: Achievement): Achievement {
    return local.copy(
        unlocked = local.unlocked || remote.unlocked,  // Once unlocked, stays unlocked
        progress = maxOf(local.progress, remote.progress),
        unlockedAt = minOf(
            local.unlockedAt ?: Long.MAX_VALUE,
            remote.unlockedAt ?: Long.MAX_VALUE
        ).takeIf { it != Long.MAX_VALUE }
    )
}
```

## Strategy 5: Queue-Based (Operational Transform)

**Best for:** Chat messages, event logs, ordered sequences

**How it works:** Don't merge — append operations in order. Server determines final order.

```kotlin
// Messages are never "conflicted" — they're always appended
// RTDB handles ordering via push keys or server timestamps
fun sendMessage(message: Message) {
    val ref = rtdb.getReference("chats/${message.chatId}/messages")
    val key = ref.push().key ?: return
    ref.child(key).setValue(message.copy(
        id = key,
        timestamp = ServerValue.TIMESTAMP
    ))
}
```

## Choosing a Strategy

| Data Type | Recommended Strategy | Rationale |
|-----------|---------------------|-----------|
| User profile | Last-Write-Wins | Single owner, low conflict probability |
| Calendar events | Last-Write-Wins | Owner-based editing, rare true conflicts |
| Task items | Field-Level Merge | Multiple fields edited independently |
| Shopping lists | Set Union | Items are additive, checked state is OR-merged |
| Chat messages | Queue-Based | Append-only, server-ordered |
| Scores/progress | Max-Wins | Monotonic values, only increase |
| Settings | Last-Write-Wins | Device-local, conflicts indicate different devices |
| Weather cache | Replace | External data, always use freshest |

## Implementing Conflict Detection in Room

Add sync metadata to your Room entities:

```kotlin
@Entity
data class Task(
    @PrimaryKey val id: String,
    val title: String,
    val completed: Boolean,

    // Sync metadata
    @ColumnInfo(name = "sync_status")
    val syncStatus: SyncStatus = SyncStatus.SYNCED,

    @ColumnInfo(name = "local_version")
    val localVersion: Int = 0,

    @ColumnInfo(name = "server_version")
    val serverVersion: Int = 0,

    @ColumnInfo(name = "local_modified_at")
    val localModifiedAt: Long = 0,

    @ColumnInfo(name = "base_snapshot")
    val baseSnapshot: String? = null,  // JSON of last synced state for field-level merge
)

enum class SyncStatus {
    SYNCED,      // Room matches server
    PENDING,     // Local change not yet pushed
    CONFLICTED,  // Server changed while local was pending
    ERROR,       // Sync failed, needs retry
}
```
