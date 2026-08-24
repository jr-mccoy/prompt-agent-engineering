# Cache Invalidation Patterns

## Overview

Room serves as the primary read source for UI. This document covers when and how to invalidate Room data to keep it consistent with Firebase backends and external APIs.

## Pattern 1: Listener-Driven Invalidation (Firebase Data)

**Use for:** Any data backed by Firestore or RTDB

Firebase snapshot listeners automatically push updates. Room is invalidated by upsert:

```kotlin
// Firestore listener → Room upsert → Flow auto-emits
firestore.collection("tasks")
    .whereEqualTo("userId", userId)
    .addSnapshotListener { snapshot, _ ->
        snapshot?.documentChanges?.forEach { change ->
            when (change.type) {
                ADDED, MODIFIED -> taskDao.upsert(change.document.toTask())
                REMOVED -> taskDao.deleteById(change.document.id)
            }
        }
    }
```

**No manual invalidation needed.** The listener keeps Room current as long as the app is connected.

**On reconnection:** Firestore resends all changes since the last sync. Room automatically catches up.

## Pattern 2: TTL-Based Invalidation (External API Data)

**Use for:** Weather data, exchange rates, any data from external APIs

```kotlin
@Entity
data class WeatherCache(
    @PrimaryKey val locationKey: String,
    val weatherJson: String,
    val fetchedAt: Long,
    val ttlMillis: Long = 30 * 60 * 1000, // 30 minutes default
) {
    fun isExpired(): Boolean =
        System.currentTimeMillis() - fetchedAt > ttlMillis
}

// Repository checks TTL before returning cached data
class WeatherRepository @Inject constructor(
    private val weatherDao: WeatherDao,
    private val weatherApi: WeatherApi,
) {
    fun getWeather(location: Location): Flow<Weather> = flow {
        val cached = weatherDao.getByLocation(location.key)

        if (cached != null && !cached.isExpired()) {
            emit(cached.toWeather())
        }

        // Always try to refresh (stale-while-revalidate)
        try {
            val fresh = weatherApi.getForecast(location.lat, location.lng)
            weatherDao.upsert(fresh.toCache(location.key))
            emit(fresh)
        } catch (e: Exception) {
            // Network error — use cached even if stale
            if (cached != null) emit(cached.toWeather())
            else throw e
        }
    }
}
```

## Pattern 3: Version-Based Invalidation

**Use for:** Data that changes infrequently but must be exactly correct when it does

```kotlin
// Check server version before using cache
suspend fun getConfig(): AppConfig {
    val localVersion = configDao.getVersion()
    val remoteVersion = firestore.collection("config")
        .document("app")
        .get().await()
        .getLong("version") ?: 0

    return if (remoteVersion > localVersion) {
        // Fetch and cache new config
        val config = fetchRemoteConfig()
        configDao.upsert(config)
        config
    } else {
        configDao.getConfig()
    }
}
```

## Pattern 4: Event-Driven Invalidation

**Use for:** Invalidating related caches when a write occurs

```kotlin
// When a task is completed, invalidate related caches
suspend fun completeTask(taskId: String) {
    taskDao.markCompleted(taskId)

    // Invalidate related caches
    gamificationDao.invalidateScoreCache()  // Score might change
    statisticsDao.invalidateWeeklyStats()   // Stats need recalculation

    // Sync to Firestore
    syncQueue.enqueue(SyncOperation.Update("tasks", taskId))
}
```

## Pattern 5: Periodic Background Refresh

**Use for:** Data that drifts over time (leaderboards, shared lists when app is backgrounded)

```kotlin
class PeriodicSyncWorker(
    context: Context,
    params: WorkerParameters,
) : CoroutineWorker(context, params) {

    override suspend fun doWork(): Result {
        // Refresh stale caches
        refreshIfStale("tasks", taskDao.getLastSyncTime(), 5.minutes)
        refreshIfStale("calendar", calendarDao.getLastSyncTime(), 15.minutes)
        refreshIfStale("shopping", shoppingDao.getLastSyncTime(), 5.minutes)
        return Result.success()
    }
}

// Schedule periodic sync
val periodicSync = PeriodicWorkRequestBuilder<PeriodicSyncWorker>(
    repeatInterval = 15,
    repeatIntervalTimeUnit = TimeUnit.MINUTES,
).setConstraints(
    Constraints.Builder()
        .setRequiredNetworkType(NetworkType.CONNECTED)
        .setRequiresBatteryNotLow(true)
        .build()
).build()
```

## Cache Cleanup

Prevent unbounded Room growth:

```kotlin
@Dao
interface CleanupDao {
    // Delete messages older than 30 days
    @Query("DELETE FROM messages WHERE timestamp < :cutoff")
    suspend fun deleteOldMessages(cutoff: Long)

    // Delete expired weather caches
    @Query("DELETE FROM weather_cache WHERE fetched_at + ttl_millis < :now")
    suspend fun deleteExpiredWeather(now: Long)

    // Keep only last 1000 notification history entries
    @Query("""
        DELETE FROM notifications
        WHERE id NOT IN (
            SELECT id FROM notifications ORDER BY created_at DESC LIMIT 1000
        )
    """)
    suspend fun trimNotifications()
}
```

Schedule cleanup with WorkManager on a daily cadence.

## Summary Table

| Pattern | Trigger | Best For | Freshness |
|---------|---------|----------|-----------|
| Listener-Driven | Firebase push | Firestore/RTDB data | Real-time |
| TTL-Based | Time expiry | External API caches | Minutes |
| Version-Based | Version mismatch | Infrequent config changes | On-demand |
| Event-Driven | Related write | Dependent caches | Immediate |
| Periodic Refresh | WorkManager timer | Background catch-up | Configurable |
