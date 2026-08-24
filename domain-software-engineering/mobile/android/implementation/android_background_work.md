---
title: "Android Background Work"
category: mobile-development
description: ""
tags:
  - android
  - mobile-development
updated: "2026-03-19"
---

# Android Background Work

**Objective:** Implement reliable background processing using WorkManager with proper constraints, retry policies, and progress tracking following Android background execution best practices.

**When to Use:** Use this prompt when implementing background tasks that need to survive app restarts, such as data sync, file uploads, periodic updates, or long-running operations. Best for tasks that don't require immediate execution or need guaranteed completion.

**Prompt Type:** Modular (120-150 lines)

---

## Context Gathering

Before implementing background work, gather essential context:

1. **Task Requirements:**
   - "What task needs to run in the background?"
   - "Does it need to run periodically or just once?"
   - "What constraints are required (network, charging, idle)?"

2. **Reliability:**
   - "Should the task retry on failure? How many times?"
   - "Does the task need to survive device reboots?"
   - "Is task ordering important (chains)?"

3. **User Feedback:**
   - "Should users see progress or notifications?"
   - "Can users cancel the background task?"

---

## Instructions

### CRITICAL: Implementation Requirements

**Before implementing ANY code, you MUST:**

1. **Understand existing background work patterns** - Check for existing WorkManager setup, workers, or services in the codebase.
2. **Verify work requirements** - Confirm timing, constraints, retry behavior, and success criteria before implementing.
3. **Follow project conventions** - Match existing worker organization and scheduling patterns.
4. **Provide specific, working code** - All code samples MUST include file paths (e.g., `work/SyncWorker.kt`) and be copy-paste ready.
5. **Include proper error handling** - Handle all failure scenarios with appropriate Result values.

**Adapting to existing background patterns is preferred over introducing new approaches.**

### Quality Requirements

- ❌ Do NOT use deprecated background APIs (IntentService, AlarmManager for deferrable work)
- ❌ Do NOT generate workers without proper idempotency considerations
- ❌ Do NOT schedule work without appropriate constraints
- ❌ Do NOT ignore WorkManager's execution guarantees and limitations
- ✅ DO follow existing worker patterns in the project
- ✅ DO provide proper CoroutineWorker implementation for async work
- ✅ DO include exponential backoff for retryable failures
- ✅ DO specify exact file paths for all code changes

---

### Phase 1: WorkManager Setup

#### 1.1 Dependencies

```kotlin
// build.gradle.kts
dependencies {
    implementation("androidx.work:work-runtime-ktx:2.9.0")

    // For Hilt integration
    implementation("androidx.hilt:hilt-work:1.2.0")
    ksp("androidx.hilt:hilt-compiler:1.2.0")
}
```

#### 1.2 Basic Worker Implementation

```kotlin
@HiltWorker
class SyncWorker @AssistedInject constructor(
    @Assisted appContext: Context,
    @Assisted workerParams: WorkerParameters,
    private val repository: DataRepository
) : CoroutineWorker(appContext, workerParams) {

    override suspend fun doWork(): Result {
        return try {
            // Get input data
            val syncType = inputData.getString(KEY_SYNC_TYPE) ?: return Result.failure()

            // Perform work
            setProgress(workDataOf(KEY_PROGRESS to 0))

            repository.syncData(syncType) { progress ->
                setProgress(workDataOf(KEY_PROGRESS to progress))
            }

            setProgress(workDataOf(KEY_PROGRESS to 100))

            // Return result with output data
            Result.success(workDataOf(KEY_ITEMS_SYNCED to itemCount))
        } catch (e: Exception) {
            if (runAttemptCount < MAX_RETRIES) {
                Result.retry()
            } else {
                Result.failure(workDataOf(KEY_ERROR to e.message))
            }
        }
    }

    companion object {
        const val KEY_SYNC_TYPE = "sync_type"
        const val KEY_PROGRESS = "progress"
        const val KEY_ITEMS_SYNCED = "items_synced"
        const val KEY_ERROR = "error"
        private const val MAX_RETRIES = 3
    }
}
```

---

### Phase 2: Work Scheduling

#### 2.1 One-Time Work

```kotlin
class WorkScheduler @Inject constructor(
    private val workManager: WorkManager
) {
    fun scheduleSyncWork(syncType: String): UUID {
        val constraints = Constraints.Builder()
            .setRequiredNetworkType(NetworkType.CONNECTED)
            .setRequiresBatteryNotLow(true)
            .build()

        val inputData = workDataOf(
            SyncWorker.KEY_SYNC_TYPE to syncType
        )

        val workRequest = OneTimeWorkRequestBuilder<SyncWorker>()
            .setConstraints(constraints)
            .setInputData(inputData)
            .setBackoffCriteria(
                BackoffPolicy.EXPONENTIAL,
                WorkRequest.MIN_BACKOFF_MILLIS,
                TimeUnit.MILLISECONDS
            )
            .addTag(TAG_SYNC)
            .build()

        workManager.enqueueUniqueWork(
            "sync_$syncType",
            ExistingWorkPolicy.KEEP,
            workRequest
        )

        return workRequest.id
    }

    companion object {
        const val TAG_SYNC = "sync_work"
    }
}
```

#### 2.2 Periodic Work

```kotlin
fun schedulePeriodicSync() {
    val constraints = Constraints.Builder()
        .setRequiredNetworkType(NetworkType.UNMETERED)
        .setRequiresCharging(true)
        .build()

    val periodicWork = PeriodicWorkRequestBuilder<SyncWorker>(
        repeatInterval = 6,
        repeatIntervalTimeUnit = TimeUnit.HOURS,
        flexTimeInterval = 30,
        flexTimeIntervalUnit = TimeUnit.MINUTES
    )
        .setConstraints(constraints)
        .addTag(TAG_PERIODIC_SYNC)
        .build()

    workManager.enqueueUniquePeriodicWork(
        WORK_NAME_PERIODIC_SYNC,
        ExistingPeriodicWorkPolicy.KEEP,
        periodicWork
    )
}
```

#### 2.3 Chained Work

```kotlin
fun scheduleChainedWork() {
    val downloadWork = OneTimeWorkRequestBuilder<DownloadWorker>()
        .addTag("download")
        .build()

    val processWork = OneTimeWorkRequestBuilder<ProcessWorker>()
        .addTag("process")
        .build()

    val uploadWork = OneTimeWorkRequestBuilder<UploadWorker>()
        .addTag("upload")
        .build()

    workManager
        .beginWith(downloadWork)
        .then(processWork)
        .then(uploadWork)
        .enqueue()
}
```

---

### Phase 3: Progress & Cancellation

#### 3.1 Observing Work Status

```kotlin
@HiltViewModel
class SyncViewModel @Inject constructor(
    private val workScheduler: WorkScheduler,
    private val workManager: WorkManager
) : ViewModel() {

    private val _syncState = MutableStateFlow<SyncState>(SyncState.Idle)
    val syncState: StateFlow<SyncState> = _syncState.asStateFlow()

    private var currentWorkId: UUID? = null

    fun startSync(syncType: String) {
        currentWorkId = workScheduler.scheduleSyncWork(syncType)

        viewModelScope.launch {
            workManager.getWorkInfoByIdFlow(currentWorkId!!)
                .collect { workInfo ->
                    _syncState.value = when (workInfo?.state) {
                        WorkInfo.State.ENQUEUED -> SyncState.Pending
                        WorkInfo.State.RUNNING -> {
                            val progress = workInfo.progress.getInt(SyncWorker.KEY_PROGRESS, 0)
                            SyncState.InProgress(progress)
                        }
                        WorkInfo.State.SUCCEEDED -> {
                            val count = workInfo.outputData.getInt(SyncWorker.KEY_ITEMS_SYNCED, 0)
                            SyncState.Success(count)
                        }
                        WorkInfo.State.FAILED -> {
                            val error = workInfo.outputData.getString(SyncWorker.KEY_ERROR)
                            SyncState.Failed(error ?: "Unknown error")
                        }
                        WorkInfo.State.CANCELLED -> SyncState.Cancelled
                        else -> SyncState.Idle
                    }
                }
        }
    }

    fun cancelSync() {
        currentWorkId?.let { workManager.cancelWorkById(it) }
    }
}

sealed interface SyncState {
    data object Idle : SyncState
    data object Pending : SyncState
    data class InProgress(val progress: Int) : SyncState
    data class Success(val itemsSynced: Int) : SyncState
    data class Failed(val error: String) : SyncState
    data object Cancelled : SyncState
}
```

#### 3.2 Foreground Service for Long Tasks

```kotlin
@HiltWorker
class LongRunningWorker @AssistedInject constructor(
    @Assisted appContext: Context,
    @Assisted workerParams: WorkerParameters
) : CoroutineWorker(appContext, workerParams) {

    override suspend fun doWork(): Result {
        setForeground(createForegroundInfo())

        // Perform long-running work...

        return Result.success()
    }

    private fun createForegroundInfo(): ForegroundInfo {
        val notification = NotificationCompat.Builder(applicationContext, CHANNEL_ID)
            .setContentTitle("Processing")
            .setContentText("Working in background...")
            .setSmallIcon(R.drawable.ic_sync)
            .setProgress(100, 0, true)
            .build()

        return ForegroundInfo(NOTIFICATION_ID, notification)
    }

    companion object {
        private const val CHANNEL_ID = "background_work"
        private const val NOTIFICATION_ID = 1001
    }
}
```

---

## Expected Output

### File Structure

```
work/
├── SyncWorker.kt
├── WorkScheduler.kt
└── di/
    └── WorkModule.kt
```

### Implementation Checklist

- [ ] Worker implementation with input/output data
- [ ] Constraints configuration (network, battery, charging)
- [ ] Retry policy with exponential backoff
- [ ] Work scheduling (one-time and/or periodic)
- [ ] Unique work handling (KEEP, REPLACE, APPEND)
- [ ] Progress reporting
- [ ] Work status observation in ViewModel
- [ ] Cancellation support
- [ ] Foreground service for long operations

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective for background work
- **ST-02** (Sequential Instructions): Phased approach from setup to monitoring
- **RT-04** (Best Practice Review): WorkManager best practices
- **ST-03** (Output Format Templates): Worker and scheduler templates

---

## Related Prompts

- [android_offline_first_sync.md](android_offline_first_sync.md) - Offline sync with WorkManager
- [android_data_layer_implementation.md](android_data_layer_implementation.md) - Repository for background sync
- [android_dependency_injection.md](android_dependency_injection.md) - Inject into Workers
- [android_state_management.md](android_state_management.md) - Observe work state in UI

---

## Customization Guide

### For File Uploads

Add progress tracking:
```kotlin
setProgress(workDataOf(
    "bytes_uploaded" to bytesUploaded,
    "total_bytes" to totalBytes
))
```

### For Periodic Cleanup

Use minimum interval:
```kotlin
PeriodicWorkRequestBuilder<CleanupWorker>(
    repeatInterval = 15, // Minimum is 15 minutes
    repeatIntervalTimeUnit = TimeUnit.MINUTES
)
```

### For Expedited Work

Request expedited execution:
```kotlin
OneTimeWorkRequestBuilder<UrgentWorker>()
    .setExpedited(OutOfQuotaPolicy.RUN_AS_NON_EXPEDITED_WORK_REQUEST)
    .build()
```
