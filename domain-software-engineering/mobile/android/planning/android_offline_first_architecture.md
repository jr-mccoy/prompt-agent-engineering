---
title: "Android Offline-First Architecture"
category: mobile-development
description: "Design an offline-first architecture using Room + WorkManager + DataStore, with conflict resolution strategies, sync queue patterns, and network-aware operations"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
difficulty: advanced
tags:
  - android
  - offline-first
  - room
  - workmanager
  - sync
  - architecture
  - mobile-development
updated: "2026-02-12"
---

# Android Offline-First Architecture

**Objective:** Design a complete offline-first architecture for an Android application — using Room as the single source of truth, WorkManager for reliable background sync, DataStore for preferences and sync metadata, with conflict resolution strategies, optimistic UI updates, sync queue management, and network-aware operations — producing an architecture that works seamlessly with or without internet connectivity.

**When to Use:** Use this prompt when building apps that must work in low-connectivity environments (field work, travel, emerging markets), when users expect zero-latency interactions (writes succeed immediately), when your app stores user-generated content that must not be lost, or when sync reliability is a critical requirement (medical records, financial data, task management).

**Sequence Map:** Use after core architecture selection; use before data-layer implementation.

**Important context:** Offline-first means the app's primary data source is local (Room database), and the remote server is a sync target, not the source of truth. The UI always reads from Room. Writes go to Room first, then sync to the server asynchronously. This inverts the typical pattern where the server is the source of truth and the local DB is a cache. The tradeoff is complexity in conflict resolution, but the user experience is dramatically better.

---

## Context Gathering

1. **Data Characteristics:**
   - "What types of data need offline support (user content, settings, media, references)?"
   - "What is the data volume (hundreds of items? millions?)?"
   - "How frequently does data change (real-time collaboration? daily updates?)?"
   - "Can multiple users edit the same data (single-user vs. collaborative)?"

2. **Sync Requirements:**
   - "What is the acceptable sync latency (seconds? minutes? next app open?)?"
   - "What backend are you syncing with (Firebase Firestore, REST API, GraphQL)?"
   - "Do you need real-time updates from the server (push) or is pull-based sufficient?"
   - "What happens if a conflict occurs (last-write-wins? user resolves? merge?)?"

3. **Connectivity Context:**
   - "What are the target usage environments (urban, rural, airplane, underground)?"
   - "Should the app work entirely offline for extended periods (days/weeks)?"
   - "Are there large files (images, documents) that need offline support?"

---

## Instructions

### Step 1: Architecture Overview

```
┌─────────────────────────────────────────────────┐
│                   UI Layer                       │
│  Composables observe Room via Flow/StateFlow     │
│  Writes go to Repository (local-first)           │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│               Repository Layer                   │
│  - Read: Room (always local)                     │
│  - Write: Room + enqueue sync                    │
│  - Provides Flow<List<T>> from Room DAO          │
└──────────┬──────────────────────┬───────────────┘
           │                      │
┌──────────▼──────────┐  ┌───────▼────────────────┐
│    Room Database     │  │    Sync Engine          │
│  (Source of Truth)   │  │  - SyncQueue table      │
│  - Entity tables     │  │  - WorkManager jobs     │
│  - Sync metadata     │  │  - Conflict resolution  │
│  - Pending changes   │  │  - Retry with backoff   │
└─────────────────────┘  └───────┬────────────────┘
                                  │
                         ┌────────▼────────────────┐
                         │    Remote API / Firebase │
                         │  - REST/GraphQL/Firestore│
                         │  - Server timestamps     │
                         │  - Conflict detection    │
                         └─────────────────────────┘
```

### Step 2: Room Database Design

```kotlin
// Entity with sync metadata
@Entity(tableName = "items")
data class ItemEntity(
    @PrimaryKey val id: String,                    // UUID generated locally
    val title: String,
    val content: String,
    val createdAt: Long,                           // Local creation timestamp
    val updatedAt: Long,                           // Local update timestamp
    val serverUpdatedAt: Long? = null,             // Server's last known timestamp
    val syncStatus: SyncStatus = SyncStatus.PENDING_CREATE,
    val isDeleted: Boolean = false                 // Soft delete for sync
)

enum class SyncStatus {
    SYNCED,             // In sync with server
    PENDING_CREATE,     // Created locally, not yet on server
    PENDING_UPDATE,     // Modified locally, not yet synced
    PENDING_DELETE,     // Deleted locally, not yet removed from server
    CONFLICT            // Server and local versions diverged
}

// Sync queue for outbound changes
@Entity(tableName = "sync_queue")
data class SyncQueueEntry(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val entityType: String,          // "item", "comment", etc.
    val entityId: String,            // The entity's primary key
    val operation: SyncOperation,    // CREATE, UPDATE, DELETE
    val payload: String,             // JSON of the change
    val createdAt: Long,             // When the change was made
    val retryCount: Int = 0,         // Number of failed sync attempts
    val lastError: String? = null    // Last error message
)

enum class SyncOperation { CREATE, UPDATE, DELETE }
```

**DAO with offline-first patterns:**

```kotlin
@Dao
interface ItemDao {
    // UI reads — always from local, excludes soft-deleted items
    @Query("SELECT * FROM items WHERE isDeleted = 0 ORDER BY updatedAt DESC")
    fun observeItems(): Flow<List<ItemEntity>>

    @Query("SELECT * FROM items WHERE id = :id AND isDeleted = 0")
    fun observeItem(id: String): Flow<ItemEntity?>

    // Write operations — mark as pending sync
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsert(item: ItemEntity)

    // Sync reads — pending changes to push
    @Query("SELECT * FROM items WHERE syncStatus != 'SYNCED' ORDER BY updatedAt ASC")
    suspend fun getPendingChanges(): List<ItemEntity>

    // Sync writes — mark as synced after successful push
    @Query("UPDATE items SET syncStatus = 'SYNCED', serverUpdatedAt = :serverTimestamp WHERE id = :id")
    suspend fun markSynced(id: String, serverTimestamp: Long)
}
```

### Step 3: Repository Pattern (Local-First)

```kotlin
class ItemRepository @Inject constructor(
    private val itemDao: ItemDao,
    private val syncQueueDao: SyncQueueDao,
    private val syncScheduler: SyncScheduler
) {
    // READ: Always from Room
    fun observeItems(): Flow<List<Item>> =
        itemDao.observeItems().map { entities -> entities.map { it.toDomain() } }

    // WRITE: Local first, then schedule sync
    suspend fun createItem(title: String, content: String): Item {
        val item = ItemEntity(
            id = UUID.randomUUID().toString(),
            title = title,
            content = content,
            createdAt = System.currentTimeMillis(),
            updatedAt = System.currentTimeMillis(),
            syncStatus = SyncStatus.PENDING_CREATE
        )
        itemDao.upsert(item)
        syncQueueDao.enqueue(SyncQueueEntry(
            entityType = "item",
            entityId = item.id,
            operation = SyncOperation.CREATE,
            payload = Json.encodeToString(item),
            createdAt = System.currentTimeMillis()
        ))
        syncScheduler.scheduleSync()  // Trigger WorkManager
        return item.toDomain()
    }

    // DELETE: Soft delete locally, schedule sync
    suspend fun deleteItem(id: String) {
        itemDao.upsert(itemDao.getItem(id).copy(
            isDeleted = true,
            syncStatus = SyncStatus.PENDING_DELETE,
            updatedAt = System.currentTimeMillis()
        ))
        syncScheduler.scheduleSync()
    }
}
```

### Step 4: WorkManager Sync Engine

```kotlin
class SyncWorker @AssistedInject constructor(
    @Assisted context: Context,
    @Assisted params: WorkerParameters,
    private val syncQueueDao: SyncQueueDao,
    private val remoteApi: RemoteApi,
    private val itemDao: ItemDao,
    private val conflictResolver: ConflictResolver
) : CoroutineWorker(context, params) {

    override suspend fun doWork(): Result {
        val pendingEntries = syncQueueDao.getPendingEntries()
        if (pendingEntries.isEmpty()) return Result.success()

        var hasFailures = false
        for (entry in pendingEntries) {
            try {
                when (entry.operation) {
                    SyncOperation.CREATE -> remoteApi.createItem(entry.payload)
                    SyncOperation.UPDATE -> {
                        val serverVersion = remoteApi.getItem(entry.entityId)
                        if (serverVersion != null && serverVersion.updatedAt > entry.createdAt) {
                            // Conflict detected
                            conflictResolver.resolve(entry, serverVersion)
                        } else {
                            remoteApi.updateItem(entry.entityId, entry.payload)
                        }
                    }
                    SyncOperation.DELETE -> remoteApi.deleteItem(entry.entityId)
                }
                itemDao.markSynced(entry.entityId, System.currentTimeMillis())
                syncQueueDao.remove(entry.id)
            } catch (e: Exception) {
                hasFailures = true
                syncQueueDao.incrementRetry(entry.id, e.message)
            }
        }

        return if (hasFailures) Result.retry() else Result.success()
    }
}

// Sync scheduler
class SyncScheduler @Inject constructor(
    private val workManager: WorkManager
) {
    fun scheduleSync() {
        val request = OneTimeWorkRequestBuilder<SyncWorker>()
            .setConstraints(
                Constraints.Builder()
                    .setRequiredNetworkType(NetworkType.CONNECTED)
                    .build()
            )
            .setBackoffCriteria(BackoffPolicy.EXPONENTIAL, 30, TimeUnit.SECONDS)
            .build()

        workManager.enqueueUniqueWork(
            "sync",
            ExistingWorkPolicy.KEEP,  // Don't duplicate if already queued
            request
        )
    }

    fun schedulePeriodicSync() {
        val request = PeriodicWorkRequestBuilder<SyncWorker>(15, TimeUnit.MINUTES)
            .setConstraints(
                Constraints.Builder()
                    .setRequiredNetworkType(NetworkType.CONNECTED)
                    .build()
            )
            .build()

        workManager.enqueueUniquePeriodicWork(
            "periodic-sync",
            ExistingPeriodicWorkPolicy.KEEP,
            request
        )
    }
}
```

### Step 5: Conflict Resolution Strategies

Choose and implement a conflict resolution strategy:

| Strategy | When to Use | Complexity |
|----------|-------------|------------|
| **Last-Write-Wins** | Single-user apps, low-stakes data | Low |
| **Server-Wins** | Reference data, admin-controlled content | Low |
| **Client-Wins** | User-generated content, offline-heavy | Low |
| **Field-Level Merge** | Collaborative editing, forms | Medium |
| **User-Prompted Resolution** | High-stakes data, medical/financial | High |

```kotlin
class ConflictResolver @Inject constructor(
    private val itemDao: ItemDao,
    private val conflictDao: ConflictDao
) {
    suspend fun resolve(localEntry: SyncQueueEntry, serverVersion: ServerItem) {
        val localVersion = itemDao.getItem(localEntry.entityId)

        // Strategy: Field-level merge with conflict flagging
        val merged = merge(localVersion, serverVersion)
        if (merged.hasConflicts) {
            // Store conflict for user resolution
            itemDao.upsert(localVersion.copy(syncStatus = SyncStatus.CONFLICT))
            conflictDao.insert(ConflictRecord(
                entityId = localEntry.entityId,
                localVersion = Json.encodeToString(localVersion),
                serverVersion = Json.encodeToString(serverVersion),
                conflictFields = merged.conflictFields
            ))
        } else {
            itemDao.upsert(merged.result)
        }
    }
}
```

### Step 6: Network-Aware UI

```kotlin
@Composable
fun ItemListScreen(viewModel: ItemListViewModel = hiltViewModel()) {
    val items by viewModel.items.collectAsStateWithLifecycle()
    val isOnline by viewModel.isOnline.collectAsStateWithLifecycle()
    val pendingSyncCount by viewModel.pendingSyncCount.collectAsStateWithLifecycle()

    Column {
        // Connectivity banner
        if (!isOnline) {
            Surface(color = MaterialTheme.colorScheme.tertiaryContainer) {
                Text(
                    "Offline — changes will sync when connected",
                    modifier = Modifier.padding(8.dp)
                )
            }
        }

        // Pending sync indicator
        if (pendingSyncCount > 0) {
            LinearProgressIndicator(modifier = Modifier.fillMaxWidth())
            Text("$pendingSyncCount changes pending sync")
        }

        // Items — always available, online or offline
        LazyColumn {
            items(items, key = { it.id }) { item ->
                ItemRow(
                    item = item,
                    isPending = item.syncStatus != SyncStatus.SYNCED
                )
            }
        }
    }
}
```

---

## Expected Output

1. **Architecture Diagram** — showing data flow between UI, Repository, Room, Sync Engine, and Remote API
2. **Room Schema** — entities with sync metadata, sync queue table, conflict records
3. **Repository Implementation** — local-first read/write operations with sync scheduling
4. **WorkManager Configuration** — sync worker with conflict detection, retry logic, and constraints
5. **Conflict Resolution Strategy** — chosen strategy with implementation
6. **Network-Aware UI Patterns** — connectivity indicators, pending sync counts, conflict resolution UI
7. **Testing Strategy** — how to test offline scenarios, sync logic, and conflict resolution

---

## CRITICAL: Verification Requirements

- [ ] UI reads exclusively from Room (never directly from network)
- [ ] Writes complete instantly (no loading spinner for local writes)
- [ ] App works fully offline (all CRUD operations available)
- [ ] Pending changes sync automatically when connectivity returns
- [ ] Conflicts are detected and resolved (not silently dropped)
- [ ] Soft-deleted items are not shown in UI but remain in DB until synced
- [ ] WorkManager constraints ensure sync only runs with network connectivity
- [ ] Sync queue is processed in order (FIFO) to prevent data inconsistency
- [ ] Process death does not lose pending changes (Room + WorkManager persist)
