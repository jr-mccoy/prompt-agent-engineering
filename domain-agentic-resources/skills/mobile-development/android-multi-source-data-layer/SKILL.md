---
name: android-multi-source-data-layer
description: Architectural patterns for Android apps that coordinate data across Room (local cache/offline), Firebase Realtime Database (real-time sync), and Firestore (structured queries) through a unified repository layer. Activates when designing or troubleshooting data layer architecture for apps using multiple Firebase backends with local caching, offline-first patterns, conflict resolution, or data routing decisions.
metadata:
  tags:
    - android
    - caching
    - data
    - layer
    - mobile
    - multi
    - source
  updated: "2026-04-11"
---
# Android Multi-Source Data Layer

Architectural guidance for Android apps that must coordinate data across Room, Firebase Realtime Database, and Cloud Firestore through a single unified data layer. Covers source-of-truth decisions per data type, conflict resolution, offline queueing, and cache invalidation.

## Purpose

Apps using Room + Firebase RTDB + Firestore face a unique orchestration challenge: each database has different strengths, consistency models, and real-time capabilities. This skill provides patterns for building a unified repository abstraction that routes reads and writes to the correct backend, handles offline scenarios, resolves conflicts between sources, and maintains a coherent local cache.

## When to Use This Skill

Use this skill when you need to:
- Design the data layer for an app using Room + Firebase RTDB + Firestore
- Decide which data types should live in RTDB vs Firestore vs Room-only
- Implement offline-first architecture with Firebase backends
- Resolve conflicts when the same data is modified offline and in Firebase
- Build a unified repository pattern that abstracts multiple data sources
- Debug data inconsistencies between local cache and Firebase

## When NOT to Use This Skill

Do NOT use this skill when:
- App uses only one database (use android-room-database or android-firebase-sync-validator)
- App uses a non-Firebase backend (use general offline-first architecture patterns)
- Only need Firebase security rules validation (use android-firebase-sync-validator)
- Building a new app from scratch (start with architecture skill, then come back here)

## Core Concept: Source of Truth Per Data Type

The fundamental principle: **each data type has exactly one source of truth**, but that source differs by type.

```
┌─────────────────────────────────────────────────────────┐
│                    Unified Repository                    │
│              (Single API for all data access)            │
├──────────────┬──────────────────┬────────────────────────┤
│  Room (Local) │  Firebase RTDB   │   Cloud Firestore     │
│              │                  │                        │
│ • Offline    │ • Real-time      │ • Structured queries   │
│   cache      │   shared state   │ • Complex filtering    │
│ • Fast reads │ • Presence       │ • Transactions         │
│ • Complex    │ • Typing status  │ • Offline persistence  │
│   joins      │ • Live counters  │ • Collection groups    │
│ • Search     │ • Chat messages  │ • Pagination           │
└──────────────┴──────────────────┴────────────────────────┘
```

## Data Routing Decision Tree

See `references/data_routing_decision_tree.md` for the complete decision framework.

**Quick reference for common app features:**

| Feature | Primary Source | Cache | Rationale |
|---------|---------------|-------|-----------|
| User profile | Firestore | Room | Structured data, queried by fields, offline needed |
| Chat/messaging | RTDB | Room | Real-time delivery, low latency, fan-out |
| Presence/online status | RTDB | None | Ephemeral, real-time only |
| Calendar events | Firestore | Room | Complex queries (date ranges), offline editing |
| Task lists | Firestore | Room | Structured queries, ordering, filtering |
| Shopping lists | Firestore | Room | Shared lists, real-time listeners, offline editing |
| Weather data | API → Room | Room | External API cached locally, no Firebase needed |
| Location reminders | Room | Room | Device-local geofences, no cloud sync needed |
| Gamification scores | Firestore | Room | Leaderboards, aggregation queries |
| App settings | Room | Room | Device-local preferences, DataStore alternative |
| Notifications history | Room | Room | Local display log, no cross-device sync |

## Step 1: Define the Unified Repository Interface

Each feature gets a repository that exposes a clean API regardless of backing store:

```kotlin
interface TaskRepository {
    // Returns Flow that combines Room cache with Firestore updates
    fun observeTasks(userId: String): Flow<List<Task>>

    // Writes to Room immediately, syncs to Firestore via WorkManager
    suspend fun createTask(task: Task): Result<Task>

    // Updates Room, queues Firestore update
    suspend fun updateTask(task: Task): Result<Task>

    // Deletes from Room, queues Firestore deletion
    suspend fun deleteTask(taskId: String): Result<Unit>
}
```

**Key principle:** The caller never knows whether data came from Room or Firestore. The repository handles routing internally.

## Step 2: Implement the Cache-Then-Network Pattern

For Firestore-backed data with Room cache:

```kotlin
class TaskRepositoryImpl @Inject constructor(
    private val taskDao: TaskDao,
    private val firestore: FirebaseFirestore,
    private val syncQueue: SyncQueue,
) : TaskRepository {

    override fun observeTasks(userId: String): Flow<List<Task>> {
        // 1. Emit cached data from Room immediately
        // 2. Start Firestore listener
        // 3. Update Room when Firestore emits
        // 4. Room Flow automatically re-emits
        return taskDao.observeByUserId(userId)
            .onStart { startFirestoreSync(userId) }
    }

    private fun startFirestoreSync(userId: String) {
        firestore.collection("tasks")
            .whereEqualTo("userId", userId)
            .addSnapshotListener { snapshot, error ->
                if (error != null) return@addSnapshotListener
                snapshot?.documents?.forEach { doc ->
                    val task = doc.toObject(Task::class.java)
                    // Update Room cache — Flow will auto-emit
                    taskDao.upsert(task)
                }
            }
    }

    override suspend fun createTask(task: Task): Result<Task> {
        // Write to Room first (instant local feedback)
        val localTask = task.copy(
            syncStatus = SyncStatus.PENDING,
            localModifiedAt = System.currentTimeMillis()
        )
        taskDao.insert(localTask)

        // Queue sync to Firestore
        syncQueue.enqueue(SyncOperation.Create("tasks", localTask))

        return Result.success(localTask)
    }
}
```

## Step 3: Implement the Real-Time Pattern (RTDB)

For RTDB-backed data (messaging, presence):

```kotlin
class MessageRepositoryImpl @Inject constructor(
    private val messageDao: MessageDao,
    private val rtdb: FirebaseDatabase,
) : MessageRepository {

    override fun observeMessages(chatId: String): Flow<List<Message>> {
        return callbackFlow {
            val ref = rtdb.getReference("chats/$chatId/messages")
            val listener = ref.orderByChild("timestamp")
                .limitToLast(50)
                .addChildEventListener(object : ChildEventListener {
                    override fun onChildAdded(snapshot: DataSnapshot, prev: String?) {
                        val msg = snapshot.getValue(Message::class.java) ?: return
                        // Cache in Room for offline access
                        messageDao.upsert(msg)
                    }
                    // ... other callbacks
                })

            // Emit from Room (includes cached + new messages)
            messageDao.observeByChatId(chatId).collect { send(it) }

            awaitClose { ref.removeEventListener(listener) }
        }
    }
}
```

## Step 4: Build the Offline Sync Queue

Use WorkManager to replay failed writes when connectivity returns:

```kotlin
class SyncQueue @Inject constructor(
    private val workManager: WorkManager,
) {
    fun enqueue(operation: SyncOperation) {
        val request = OneTimeWorkRequestBuilder<SyncWorker>()
            .setInputData(operation.toWorkData())
            .setConstraints(
                Constraints.Builder()
                    .setRequiredNetworkType(NetworkType.CONNECTED)
                    .build()
            )
            .setBackoffCriteria(
                BackoffPolicy.EXPONENTIAL,
                WorkRequest.MIN_BACKOFF_MILLIS,
                TimeUnit.MILLISECONDS
            )
            .build()

        // Use APPEND_OR_REPLACE to avoid duplicate syncs
        workManager.enqueueUniqueWork(
            operation.uniqueId,
            ExistingWorkPolicy.KEEP,
            request
        )
    }
}
```

## Step 5: Handle Conflict Resolution

See `references/conflict_resolution_strategies.md` for complete strategies.

**Default strategy: Last-Write-Wins with server timestamp**

```kotlin
// In SyncWorker
suspend fun resolveConflict(local: Task, remote: Task): Task {
    return when {
        // Server version is newer — accept server
        remote.serverModifiedAt > local.localModifiedAt -> remote
        // Local version is newer — push local
        local.localModifiedAt > remote.serverModifiedAt -> local
        // Same timestamp — merge fields
        else -> mergeFields(local, remote)
    }
}
```

**When to use other strategies:**
- **Shopping lists:** Merge strategy (combine items from both sides)
- **Calendar events:** Last-write-wins (single user owns each event)
- **Task completion:** OR-merge (if completed on either side, it's completed)
- **Gamification scores:** Max-wins (keep the higher score)

## Step 6: Implement Cache Invalidation

See `references/cache_invalidation_patterns.md` for complete patterns.

**TTL-based invalidation for weather and external data:**
```kotlin
@Entity
data class WeatherCache(
    @PrimaryKey val locationId: String,
    val data: String,
    val fetchedAt: Long,
) {
    fun isStale(): Boolean =
        System.currentTimeMillis() - fetchedAt > 30.minutes.inWholeMilliseconds
}
```

**Event-driven invalidation for Firebase data:**
- Firestore snapshot listeners automatically invalidate Room cache
- RTDB child listeners update Room in real-time
- No manual invalidation needed for Firebase-backed data

## Common Issues

### Room and Firestore Model Drift
Keep Room entities and Firestore documents aligned. Use a shared data class with annotations for both:
```kotlin
@Entity(tableName = "tasks")
data class Task(
    @PrimaryKey val id: String,
    val title: String,
    val completed: Boolean,
    // Room-only fields
    @ColumnInfo(name = "sync_status") val syncStatus: SyncStatus = SyncStatus.SYNCED,
    @ColumnInfo(name = "local_modified_at") val localModifiedAt: Long = 0,
    // Firestore ignores unknown fields by default
)
```

### Snapshot Listener Memory Leaks
Always scope Firestore listeners to the appropriate lifecycle:
```kotlin
// In ViewModel — cleared when ViewModel is destroyed
private val listenerRegistration = firestore.collection("tasks")
    .addSnapshotListener { ... }

override fun onCleared() {
    listenerRegistration.remove()
}
```

### Offline Queue Ordering
WorkManager doesn't guarantee order. For operations where order matters (create then update), use chaining:
```kotlin
workManager.beginUniqueWork("task-${task.id}", REPLACE, createWork)
    .then(updateWork)
    .enqueue()
```

## Related Skills

- `android-room-database` — Deep dive into Room patterns, migrations, and testing
- `android-firebase-sync-validator` — Validates Firebase rules and sync coverage
- `android-testing-patterns` — Testing strategies for multi-source data layers
