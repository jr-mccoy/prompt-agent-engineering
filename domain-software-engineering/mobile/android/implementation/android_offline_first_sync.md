---
title: "Android Offline-First Sync"
category: mobile-development
description: ""
tags:
  - android
  - mobile-development
updated: "2026-03-19"
---

# Android Offline-First Sync

**Objective:** Implement an offline-first architecture with robust data synchronization that ensures seamless user experience regardless of network connectivity, with proper conflict resolution and sync state management.

**When to Use:** Use this prompt when building apps that must function fully offline, need to sync local changes when connectivity returns, or require optimistic UI updates. Ideal for field apps, note-taking apps, or any app where network connectivity is unreliable.

**Prompt Type:** Comprehensive (350-450 lines)

---

## Context Gathering

Before implementing offline-first sync, gather essential context:

1. **Data Requirements:**
   - "What data needs to work offline?"
   - "How frequently does data change?"
   - "What is the typical data volume per user?"

2. **Sync Strategy:**
   - "Full sync or incremental sync?"
   - "How should conflicts be resolved (last-write-wins, merge, manual)?"
   - "Do you need real-time sync or periodic?"

3. **User Experience:**
   - "Should users see sync status indicators?"
   - "How should conflicts be presented to users (if manual resolution)?"
   - "Should optimistic updates show immediately?"

4. **Backend Requirements:**
   - "Does the API support delta/incremental sync?"
   - "Are there timestamp or version fields for conflict detection?"
   - "Is there a dedicated sync endpoint?"

---

## Instructions

### CRITICAL: Implementation Requirements

**Before implementing ANY code, you MUST:**

1. **Understand existing data layer** - Check for existing Room setup, repositories, and sync mechanisms in the codebase.
2. **Verify sync requirements** - Confirm conflict resolution strategy, sync frequency, and data freshness requirements.
3. **Follow project conventions** - Match existing offline patterns, error handling, and user feedback approaches.
4. **Provide specific, working code** - All code samples MUST include file paths (e.g., `sync/SyncEngine.kt`) and be copy-paste ready.
5. **Include conflict handling** - Provide clear conflict detection and resolution logic.

**Adapting to existing data patterns is preferred over introducing new approaches.** Extend existing repositories and sync mechanisms.

### Quality Requirements

- ❌ Do NOT implement sync without proper conflict resolution strategy
- ❌ Do NOT generate sync code without considering data integrity
- ❌ Do NOT skip queue persistence for pending changes
- ❌ Do NOT ignore network state and retry requirements
- ✅ DO follow existing offline-first patterns in the project
- ✅ DO provide clear user feedback during sync operations
- ✅ DO include proper error recovery and data validation
- ✅ DO specify exact file paths for all code changes

---

### Phase 1: Data Layer Architecture

#### 1.1 Sync-Aware Entity Design

Design entities with sync metadata:

```kotlin
@Entity(tableName = "items")
data class ItemEntity(
    @PrimaryKey
    val id: String,

    val title: String,
    val content: String,

    // Timestamps
    @ColumnInfo(name = "created_at")
    val createdAt: Long,

    @ColumnInfo(name = "updated_at")
    val updatedAt: Long,

    // Sync metadata
    @ColumnInfo(name = "sync_status")
    val syncStatus: SyncStatus = SyncStatus.SYNCED,

    @ColumnInfo(name = "local_updated_at")
    val localUpdatedAt: Long = System.currentTimeMillis(),

    @ColumnInfo(name = "server_updated_at")
    val serverUpdatedAt: Long? = null,

    @ColumnInfo(name = "is_deleted")
    val isDeleted: Boolean = false,

    @ColumnInfo(name = "conflict_data")
    val conflictData: String? = null // JSON of server version if conflict
)

enum class SyncStatus {
    SYNCED,           // Matches server
    PENDING_CREATE,   // Created locally, not yet synced
    PENDING_UPDATE,   // Updated locally, not yet synced
    PENDING_DELETE,   // Deleted locally, not yet synced
    CONFLICT          // Local and server versions differ
}
```

#### 1.2 Sync-Aware DAO

```kotlin
@Dao
interface ItemDao {
    // Read operations (exclude soft-deleted)
    @Query("SELECT * FROM items WHERE is_deleted = 0 ORDER BY updated_at DESC")
    fun observeAll(): Flow<List<ItemEntity>>

    @Query("SELECT * FROM items WHERE id = :id AND is_deleted = 0")
    fun observeById(id: String): Flow<ItemEntity?>

    @Query("SELECT * FROM items WHERE id = :id")
    suspend fun getById(id: String): ItemEntity?

    // Sync queries
    @Query("SELECT * FROM items WHERE sync_status != 'SYNCED'")
    suspend fun getPendingSync(): List<ItemEntity>

    @Query("SELECT COUNT(*) FROM items WHERE sync_status != 'SYNCED'")
    fun observePendingSyncCount(): Flow<Int>

    @Query("SELECT * FROM items WHERE sync_status = 'CONFLICT'")
    fun observeConflicts(): Flow<List<ItemEntity>>

    // Write operations
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsert(item: ItemEntity)

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsertAll(items: List<ItemEntity>)

    // Sync status updates
    @Query("UPDATE items SET sync_status = :status WHERE id = :id")
    suspend fun updateSyncStatus(id: String, status: SyncStatus)

    @Query("""
        UPDATE items
        SET sync_status = 'SYNCED',
            server_updated_at = :serverUpdatedAt
        WHERE id = :id
    """)
    suspend fun markSynced(id: String, serverUpdatedAt: Long)

    // Soft delete
    @Query("""
        UPDATE items
        SET is_deleted = 1,
            sync_status = 'PENDING_DELETE',
            local_updated_at = :timestamp
        WHERE id = :id
    """)
    suspend fun softDelete(id: String, timestamp: Long = System.currentTimeMillis())

    // Hard delete after sync confirmation
    @Query("DELETE FROM items WHERE id = :id")
    suspend fun hardDelete(id: String)

    // Get last sync timestamp
    @Query("SELECT MAX(server_updated_at) FROM items WHERE sync_status = 'SYNCED'")
    suspend fun getLastSyncTimestamp(): Long?
}
```

---

### Phase 2: Repository Implementation

**CHECKPOINT 1:** Review entity design before implementing repository.

```markdown
## Entity Design Summary

### Sync Metadata Fields
| Field | Purpose |
|-------|---------|
| sync_status | Current sync state |
| local_updated_at | When locally modified |
| server_updated_at | Server timestamp |
| is_deleted | Soft delete flag |
| conflict_data | Server version for conflicts |

### Sync States
| State | Meaning |
|-------|---------|
| SYNCED | Matches server |
| PENDING_CREATE | New, awaiting upload |
| PENDING_UPDATE | Modified, awaiting upload |
| PENDING_DELETE | Deleted, awaiting confirmation |
| CONFLICT | Manual resolution needed |

**Proceed with repository implementation?**
```

#### 2.1 Offline-First Repository

```kotlin
class ItemRepositoryImpl @Inject constructor(
    private val localDataSource: ItemLocalDataSource,
    private val remoteDataSource: ItemRemoteDataSource,
    private val syncEngine: SyncEngine,
    private val connectivityObserver: ConnectivityObserver,
    private val dispatchers: DispatcherProvider
) : ItemRepository {

    override fun observeAll(): Flow<List<Item>> =
        localDataSource.observeAll()
            .map { entities -> entities.map(ItemMapper::toDomain) }
            .flowOn(dispatchers.io)

    override suspend fun getById(id: String): Item? =
        withContext(dispatchers.io) {
            localDataSource.getById(id)?.let(ItemMapper::toDomain)
        }

    // Optimistic create - immediately available locally
    override suspend fun create(item: Item): Result<Item> =
        withContext(dispatchers.io) {
            runCatching {
                val entity = ItemMapper.toEntity(item).copy(
                    syncStatus = SyncStatus.PENDING_CREATE,
                    localUpdatedAt = System.currentTimeMillis()
                )
                localDataSource.upsert(entity)

                // Trigger sync if online
                if (connectivityObserver.isOnline()) {
                    syncEngine.syncItem(item.id)
                }

                item
            }
        }

    // Optimistic update - immediately reflects locally
    override suspend fun update(item: Item): Result<Item> =
        withContext(dispatchers.io) {
            runCatching {
                val existing = localDataSource.getById(item.id)
                    ?: throw IllegalStateException("Item not found")

                val newStatus = if (existing.syncStatus == SyncStatus.PENDING_CREATE) {
                    SyncStatus.PENDING_CREATE // Keep as pending create
                } else {
                    SyncStatus.PENDING_UPDATE
                }

                val entity = ItemMapper.toEntity(item).copy(
                    syncStatus = newStatus,
                    localUpdatedAt = System.currentTimeMillis(),
                    serverUpdatedAt = existing.serverUpdatedAt
                )
                localDataSource.upsert(entity)

                if (connectivityObserver.isOnline()) {
                    syncEngine.syncItem(item.id)
                }

                item
            }
        }

    // Optimistic delete - immediately hidden locally
    override suspend fun delete(id: String): Result<Unit> =
        withContext(dispatchers.io) {
            runCatching {
                localDataSource.softDelete(id)

                if (connectivityObserver.isOnline()) {
                    syncEngine.syncItem(id)
                }
            }
        }

    // Manual sync trigger
    override suspend fun sync(): Result<SyncResult> =
        withContext(dispatchers.io) {
            syncEngine.performFullSync()
        }

    // Observe sync state
    override fun observeSyncState(): Flow<SyncState> =
        syncEngine.syncState

    override fun observePendingCount(): Flow<Int> =
        localDataSource.observePendingSyncCount()
}
```

---

### Phase 3: Sync Engine

#### 3.1 Sync Engine Implementation

```kotlin
class SyncEngine @Inject constructor(
    private val localDataSource: ItemLocalDataSource,
    private val remoteDataSource: ItemRemoteDataSource,
    private val conflictResolver: ConflictResolver,
    private val dispatchers: DispatcherProvider
) {
    private val _syncState = MutableStateFlow<SyncState>(SyncState.Idle)
    val syncState: StateFlow<SyncState> = _syncState.asStateFlow()

    private val syncMutex = Mutex()

    suspend fun performFullSync(): Result<SyncResult> = syncMutex.withLock {
        withContext(dispatchers.io) {
            runCatching {
                _syncState.value = SyncState.Syncing

                // Step 1: Push local changes
                val pushResult = pushLocalChanges()

                // Step 2: Pull remote changes
                val pullResult = pullRemoteChanges()

                // Step 3: Handle conflicts
                val conflicts = handleConflicts()

                _syncState.value = SyncState.Idle

                SyncResult(
                    itemsPushed = pushResult.count,
                    itemsPulled = pullResult.count,
                    conflicts = conflicts
                )
            }.onFailure {
                _syncState.value = SyncState.Error(it.message ?: "Sync failed")
            }
        }
    }

    suspend fun syncItem(itemId: String) {
        withContext(dispatchers.io) {
            val item = localDataSource.getById(itemId) ?: return@withContext

            try {
                when (item.syncStatus) {
                    SyncStatus.PENDING_CREATE -> {
                        val response = remoteDataSource.create(ItemMapper.toDto(item))
                        localDataSource.markSynced(itemId, response.updatedAt)
                    }
                    SyncStatus.PENDING_UPDATE -> {
                        val response = remoteDataSource.update(itemId, ItemMapper.toDto(item))
                        localDataSource.markSynced(itemId, response.updatedAt)
                    }
                    SyncStatus.PENDING_DELETE -> {
                        remoteDataSource.delete(itemId)
                        localDataSource.hardDelete(itemId)
                    }
                    else -> { /* No action needed */ }
                }
            } catch (e: HttpException) {
                if (e.code() == 409) { // Conflict
                    handleConflict(itemId)
                }
                // Other errors - leave as pending for retry
            }
        }
    }

    private suspend fun pushLocalChanges(): PushResult {
        val pendingItems = localDataSource.getPendingSync()
        var successCount = 0

        pendingItems.forEach { item ->
            try {
                syncItem(item.id)
                successCount++
            } catch (e: Exception) {
                Timber.e(e, "Failed to sync item ${item.id}")
            }
        }

        return PushResult(successCount)
    }

    private suspend fun pullRemoteChanges(): PullResult {
        val lastSync = localDataSource.getLastSyncTimestamp() ?: 0
        val remoteChanges = remoteDataSource.getChangesSince(lastSync)

        var count = 0
        remoteChanges.forEach { remoteItem ->
            val localItem = localDataSource.getById(remoteItem.id)

            when {
                localItem == null -> {
                    // New remote item
                    localDataSource.upsert(ItemMapper.fromDto(remoteItem))
                    count++
                }
                localItem.syncStatus == SyncStatus.SYNCED -> {
                    // No local changes, update from server
                    localDataSource.upsert(ItemMapper.fromDto(remoteItem))
                    count++
                }
                else -> {
                    // Local changes exist - potential conflict
                    handleConflict(remoteItem.id)
                }
            }
        }

        return PullResult(count)
    }

    private suspend fun handleConflict(itemId: String) {
        val localItem = localDataSource.getById(itemId) ?: return
        val remoteItem = runCatching { remoteDataSource.getById(itemId) }.getOrNull()

        if (remoteItem == null) {
            // Deleted on server
            localDataSource.hardDelete(itemId)
            return
        }

        val resolution = conflictResolver.resolve(localItem, remoteItem)

        when (resolution) {
            is ConflictResolution.UseLocal -> {
                remoteDataSource.update(itemId, ItemMapper.toDto(localItem))
                localDataSource.markSynced(itemId, System.currentTimeMillis())
            }
            is ConflictResolution.UseRemote -> {
                localDataSource.upsert(ItemMapper.fromDto(remoteItem))
            }
            is ConflictResolution.Merge -> {
                val merged = resolution.mergedItem
                remoteDataSource.update(itemId, ItemMapper.toDto(merged))
                localDataSource.upsert(merged.copy(syncStatus = SyncStatus.SYNCED))
            }
            is ConflictResolution.Manual -> {
                localDataSource.upsert(localItem.copy(
                    syncStatus = SyncStatus.CONFLICT,
                    conflictData = Json.encodeToString(remoteItem)
                ))
            }
        }
    }

    private suspend fun handleConflicts(): Int {
        return localDataSource.getConflicts().size
    }
}
```

#### 3.2 Conflict Resolution

```kotlin
interface ConflictResolver {
    suspend fun resolve(local: ItemEntity, remote: ItemDto): ConflictResolution
}

sealed interface ConflictResolution {
    data object UseLocal : ConflictResolution
    data object UseRemote : ConflictResolution
    data class Merge(val mergedItem: ItemEntity) : ConflictResolution
    data object Manual : ConflictResolution
}

// Last-write-wins strategy
class LastWriteWinsResolver : ConflictResolver {
    override suspend fun resolve(local: ItemEntity, remote: ItemDto): ConflictResolution {
        return if (local.localUpdatedAt > remote.updatedAt) {
            ConflictResolution.UseLocal
        } else {
            ConflictResolution.UseRemote
        }
    }
}

// Field-level merge strategy
class MergeResolver : ConflictResolver {
    override suspend fun resolve(local: ItemEntity, remote: ItemDto): ConflictResolution {
        val merged = local.copy(
            title = if (local.title != remote.title) local.title else remote.title,
            content = mergeContent(local.content, remote.content),
            updatedAt = maxOf(local.localUpdatedAt, remote.updatedAt)
        )
        return ConflictResolution.Merge(merged)
    }

    private fun mergeContent(local: String, remote: String): String {
        // Implement merge logic (diff/patch, append, etc.)
        return local // Simplified
    }
}
```

---

### Phase 4: Background Sync

**CHECKPOINT 2:** Review sync logic before implementing background sync.

```markdown
## Sync Engine Summary

### Sync Flow
1. Push local pending changes
2. Pull remote changes since last sync
3. Detect and resolve conflicts
4. Update sync timestamps

### Conflict Strategies
| Strategy | Use Case |
|----------|----------|
| Last-write-wins | Simple apps, low conflict chance |
| Field-level merge | Collaborative editing |
| Manual | User must decide |

**Proceed with background sync setup?**
```

#### 4.1 Sync Worker

```kotlin
@HiltWorker
class SyncWorker @AssistedInject constructor(
    @Assisted appContext: Context,
    @Assisted workerParams: WorkerParameters,
    private val syncEngine: SyncEngine
) : CoroutineWorker(appContext, workerParams) {

    override suspend fun doWork(): Result {
        return syncEngine.performFullSync()
            .fold(
                onSuccess = { Result.success() },
                onFailure = {
                    if (runAttemptCount < 3) {
                        Result.retry()
                    } else {
                        Result.failure()
                    }
                }
            )
    }
}

class SyncScheduler @Inject constructor(
    private val workManager: WorkManager
) {
    fun schedulePeriodicSync() {
        val constraints = Constraints.Builder()
            .setRequiredNetworkType(NetworkType.CONNECTED)
            .build()

        val syncWork = PeriodicWorkRequestBuilder<SyncWorker>(
            repeatInterval = 15,
            repeatIntervalTimeUnit = TimeUnit.MINUTES
        )
            .setConstraints(constraints)
            .build()

        workManager.enqueueUniquePeriodicWork(
            "periodic_sync",
            ExistingPeriodicWorkPolicy.KEEP,
            syncWork
        )
    }

    fun triggerImmediateSync() {
        val constraints = Constraints.Builder()
            .setRequiredNetworkType(NetworkType.CONNECTED)
            .build()

        val syncWork = OneTimeWorkRequestBuilder<SyncWorker>()
            .setConstraints(constraints)
            .build()

        workManager.enqueueUniqueWork(
            "immediate_sync",
            ExistingWorkPolicy.REPLACE,
            syncWork
        )
    }
}
```

#### 4.2 Connectivity Observer

```kotlin
interface ConnectivityObserver {
    fun observe(): Flow<Status>
    fun isOnline(): Boolean

    enum class Status { Available, Unavailable, Losing, Lost }
}

class NetworkConnectivityObserver @Inject constructor(
    @ApplicationContext private val context: Context
) : ConnectivityObserver {

    private val connectivityManager =
        context.getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager

    override fun observe(): Flow<ConnectivityObserver.Status> = callbackFlow {
        val callback = object : ConnectivityManager.NetworkCallback() {
            override fun onAvailable(network: Network) {
                trySend(ConnectivityObserver.Status.Available)
            }

            override fun onLosing(network: Network, maxMsToLive: Int) {
                trySend(ConnectivityObserver.Status.Losing)
            }

            override fun onLost(network: Network) {
                trySend(ConnectivityObserver.Status.Lost)
            }

            override fun onUnavailable() {
                trySend(ConnectivityObserver.Status.Unavailable)
            }
        }

        val request = NetworkRequest.Builder()
            .addCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
            .build()

        connectivityManager.registerNetworkCallback(request, callback)

        awaitClose {
            connectivityManager.unregisterNetworkCallback(callback)
        }
    }.distinctUntilChanged()

    override fun isOnline(): Boolean {
        val network = connectivityManager.activeNetwork ?: return false
        val capabilities = connectivityManager.getNetworkCapabilities(network) ?: return false
        return capabilities.hasCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
    }
}
```

---

## Expected Output

### File Structure

```
sync/
├── SyncEngine.kt
├── SyncWorker.kt
├── SyncScheduler.kt
├── ConflictResolver.kt
├── ConnectivityObserver.kt
└── model/
    ├── SyncStatus.kt
    ├── SyncState.kt
    └── SyncResult.kt
```

### Implementation Checklist

- [ ] Sync-aware entity with metadata fields
- [ ] DAO with sync status queries
- [ ] Offline-first repository with optimistic updates
- [ ] Sync engine with push/pull logic
- [ ] Conflict detection and resolution
- [ ] Background sync with WorkManager
- [ ] Connectivity observer for online/offline detection
- [ ] Sync state observation in UI
- [ ] Retry logic for failed syncs

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective for offline-first
- **ST-02** (Sequential Instructions): Phased data-to-sync approach
- **RT-02** (Multi-Dimensional Analysis): Entity, repository, sync, background
- **RT-04** (Best Practice Review): Offline-first architecture patterns
- **ST-03** (Output Format Templates): Code templates for sync components
- **NE-02** (Phased Workflow): Clear phases with checkpoints

---

## Related Prompts

- [android_data_layer_implementation.md](android_data_layer_implementation.md) - Base data layer
- [android_background_work.md](android_background_work.md) - WorkManager setup
- [android_api_integration.md](android_api_integration.md) - API for sync
- [android_state_management.md](android_state_management.md) - Sync state in UI

---

## Customization Guide

### For Real-Time Sync

Replace periodic sync with WebSocket:
```kotlin
class RealtimeSyncManager(private val webSocket: WebSocket) {
    fun observeChanges(): Flow<RemoteChange> = webSocket.messages()
        .map { Json.decodeFromString<RemoteChange>(it) }
}
```

### For Large Datasets

Implement pagination in sync:
```kotlin
suspend fun pullRemoteChanges() {
    var cursor: String? = null
    do {
        val page = remoteDataSource.getChangesSince(lastSync, cursor)
        processPage(page.items)
        cursor = page.nextCursor
    } while (cursor != null)
}
```

### For Multi-User Collaboration

Add user tracking:
```kotlin
@Entity
data class ItemEntity(
    // ... other fields
    val lastModifiedBy: String,
    val lockOwner: String? = null,
    val lockExpiry: Long? = null
)
```
