---
title: "Android Battery Drain Investigation & Remediation"
category: mobile-development
description: "Analyzes Android Kotlin/Compose apps to identify implementation errors and inefficiencies causing excessive battery consumption"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - mobile-development
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_performance_audit.md
  - domain-software-engineering/mobile/android/analysis/android_concurrency_threading_analysis.md
  - domain-software-engineering/mobile/android/targeted-reviews/android_workmanager_background_review.md
---


# Android Battery Drain Investigation & Remediation

**Objective:** Analyze Android applications built with Kotlin and Jetpack Compose to identify implementation errors, inefficiencies, and optimization opportunities that cause excessive battery consumption, then propose specific remediation strategies.

**When to Use:** Use this prompt when users report battery drain issues, when preparing for app store submission, during performance optimization sprints, or as part of regular code quality reviews. This prompt focuses on *how* features are implemented rather than *what* features exist—the goal is to optimize implementations, not eliminate functionality.

**Important Note:** This analysis does not blame features for battery usage. GPS, networking, and background processing are legitimate app capabilities. The focus is on identifying implementation mistakes, missed optimizations, and inefficient patterns that cause *unnecessary* battery drain beyond what the feature actually requires.

---

## Instructions

### CRITICAL: Verification Requirements

**Before flagging ANY battery issue, you MUST:**

1. **Trace actual code behavior** - Don't flag based on pattern matching alone. Verify that the suspected pattern actually causes unnecessary drain.
2. **Check for existing optimizations** - Search for lifecycle-aware scopes, proper cancellation, or battery-conscious implementations.
3. **Understand the context** - Consider WHY certain patterns exist. Legitimate features need background processing.
4. **Confirm actual impact** - Profile or measure to verify the issue causes meaningful battery drain.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `SyncWorker.kt:45`).

**Finding NO significant issues is an acceptable outcome.** If the app handles battery efficiently for its feature set, say so with confidence. Don't manufacture drain concerns.

### False-Positive Prevention

- ❌ Do NOT flag legitimate background features as drain issues
- ❌ Do NOT assume all GlobalScope usage is wrong without checking context
- ❌ Do NOT report theoretical issues without evidence of actual drain
- ❌ Do NOT blame features for existing—focus on implementation quality
- ✅ DO understand that some features legitimately need background processing
- ✅ DO check for proper lifecycle management before flagging
- ✅ DO profile or measure to verify actual battery impact
- ✅ DO consider the trade-off between functionality and battery

---

### 1. Coroutine & Concurrency Analysis

Investigate coroutine usage for battery-draining anti-patterns:

* **Scope Leaks:**
  - Identify coroutines launched in `GlobalScope` that continue running after the user leaves a screen
  - Check for missing `viewModelScope` or `lifecycleScope` usage where appropriate
  - Look for coroutines not cancelled when their associated lifecycle ends
  - Find `Job` references that are never cancelled

* **Dispatcher Misuse:**
  - Identify CPU-intensive work running on `Dispatchers.Main` (keeps main thread active)
  - Find I/O operations not using `Dispatchers.IO` (inefficient thread usage)
  - Check for `Dispatchers.Default` used for blocking operations
  - Look for unnecessary dispatcher switches causing overhead

* **Polling & Loops:**
  - Find `while(true)` loops or recursive delays in coroutines
  - Identify fixed-interval polling that could use exponential backoff
  - Check for missing `delay()` in retry loops
  - Look for tight loops without yield points

* **Flow Collection Issues:**
  - Identify `Flow` collections not using `repeatOnLifecycle` or `flowWithLifecycle`
  - Check for multiple redundant collectors of the same flow
  - Find hot flows (`StateFlow`/`SharedFlow`) emitting when no collectors exist
  - Look for `collect` calls that never complete blocking the coroutine

**Code Patterns to Search:**
```kotlin
// Problematic patterns to find:
GlobalScope.launch { }
while (true) { delay(...) }
while (isActive) { /* no delay */ }
flow.collect { } // without lifecycle awareness
launch { } // in Activity/Fragment without proper scope
```

---

### 2. Jetpack Compose Recomposition Analysis

Identify Compose patterns that cause excessive CPU usage:

* **Unstable Parameters:**
  - Find composables receiving lambda parameters that aren't remembered
  - Identify data classes missing `@Stable` or `@Immutable` annotations where needed
  - Check for `List`, `Map`, or `Set` parameters that should be wrapped in stable types
  - Look for composables with frequently-changing parameters causing cascading recompositions

* **State Management Issues:**
  - Identify `mutableStateOf` called outside of `remember`
  - Find state reads in composables that should use `derivedStateOf`
  - Check for state hoisting violations causing unnecessary recompositions
  - Look for `remember` with keys that change too frequently

* **Side Effect Misuse:**
  - Find `LaunchedEffect` with `Unit` key running expensive operations repeatedly
  - Identify missing `DisposableEffect` for cleanup of resources
  - Check for `SideEffect` used where `LaunchedEffect` is appropriate
  - Look for effects not properly keyed to their dependencies

* **Layout Performance:**
  - Identify `Modifier.graphicsLayer` operations that could use `drawBehind`
  - Find intrinsic measurement usage that could be avoided
  - Check for deep nesting causing measurement passes
  - Look for `SubcomposeLayout` used unnecessarily

**Code Patterns to Search:**
```kotlin
// Problematic patterns to find:
val state = mutableStateOf(...) // outside remember
LaunchedEffect(Unit) { expensiveOperation() }
@Composable fun Item(onClick: () -> Unit) // unstable lambda
items(list) { /* list not stable */ }
```

---

### 3. Network Operations Analysis

Examine networking code for battery-inefficient patterns:

* **Request Frequency:**
  - Identify APIs polled more frequently than data changes
  - Check for missing caching of responses that rarely change
  - Find requests triggered on every recomposition
  - Look for duplicate requests for the same data

* **Connection Management:**
  - Check for connections held open longer than necessary
  - Identify missing connection pooling in OkHttp configuration
  - Find WebSocket connections that don't properly close
  - Look for missing timeout configurations causing hung connections

* **Payload Efficiency:**
  - Identify requests fetching more data than displayed
  - Check for missing pagination in list fetches
  - Find uncompressed request/response bodies
  - Look for image downloads without size optimization

* **Batching Opportunities:**
  - Find multiple sequential requests that could be batched
  - Identify requests that could be deferred to Wi-Fi
  - Check for missing request deduplication
  - Look for sync operations that could use WorkManager batching

**Code Patterns to Search:**
```kotlin
// Problematic patterns to find:
delay(1000); fetchData() // frequent polling
LaunchedEffect(Unit) { while(true) { api.poll() } }
retrofit.create(...) // created per-request
client.newCall(...) // without connection reuse
```

---

### 4. Location Services Analysis

Review location implementation for power efficiency:

* **Request Configuration:**
  - Check if location accuracy is higher than needed (e.g., GPS when network is sufficient)
  - Identify missing `setPriority()` calls defaulting to high accuracy
  - Find location requests without proper interval configuration
  - Look for missing `setSmallestDisplacement()` causing updates for minor movements

* **Update Management:**
  - Identify location listeners not removed when activity/fragment stops
  - Check for `requestLocationUpdates` without corresponding removal
  - Find background location requests that could use geofencing instead
  - Look for missing fastest interval limits

* **Lifecycle Issues:**
  - Check for location requests continuing when app is backgrounded
  - Identify missing foreground service for legitimate background location
  - Find location callbacks holding references to destroyed contexts
  - Look for LocationManager used instead of Fused Location Provider

**Code Patterns to Search:**
```kotlin
// Problematic patterns to find:
PRIORITY_HIGH_ACCURACY // when BALANCED_POWER_ACCURACY would suffice
setInterval(1000) // very frequent updates
requestLocationUpdates(...) // without removeLocationUpdates
LocationManager.requestLocationUpdates // instead of FusedLocationProviderClient
```

---

### 5. Wake Lock & Alarm Analysis

Examine wake management for battery impact:

* **Wake Lock Issues:**
  - Identify wake locks acquired but never released
  - Check for wake locks held longer than the work they protect
  - Find partial wake locks where job scheduling would work
  - Look for wake locks without timeout fallbacks

* **Alarm Scheduling:**
  - Identify `setExact()` or `setExactAndAllowWhileIdle()` used for non-critical tasks
  - Check for alarms scheduled more frequently than necessary
  - Find repeating alarms that could use `setInexactRepeating()`
  - Look for AlarmManager used where WorkManager is more appropriate

* **Work Scheduling:**
  - Check for work not using `WorkManager` constraints (e.g., `requiresCharging`, `requiresNetworkType`)
  - Identify work scheduled as expedited when it doesn't need to be
  - Find periodic work with intervals shorter than necessary
  - Look for missing backoff policies on retryable work

**Code Patterns to Search:**
```kotlin
// Problematic patterns to find:
powerManager.newWakeLock(...) // without release in finally
setExactAndAllowWhileIdle(...) // for non-time-critical work
PeriodicWorkRequestBuilder<...>(15, TimeUnit.MINUTES) // minimum is 15, but is it needed?
.setExpedited(OutOfQuotaPolicy.RUN_AS_NON_EXPEDITED_WORK_REQUEST) // unnecessary expedited
```

---

### 6. Sensor & Hardware Access Analysis

Review sensor usage for unnecessary drain:

* **Sensor Registration:**
  - Identify sensors registered with `SENSOR_DELAY_FASTEST` when slower rates suffice
  - Check for sensor listeners not unregistered in `onPause()` or `onStop()`
  - Find continuous sensor reading when event-based would work
  - Look for multiple registrations for the same sensor

* **Camera & Media:**
  - Check for camera sessions not properly closed
  - Identify media players not released when finished
  - Find audio focus held longer than playback
  - Look for camera preview running when not visible

* **Bluetooth & NFC:**
  - Identify continuous BLE scanning without scan filters
  - Check for scan callbacks not unregistered
  - Find high duty cycle scanning when low duty cycle works
  - Look for missing scan result batching

**Code Patterns to Search:**
```kotlin
// Problematic patterns to find:
registerListener(..., SENSOR_DELAY_FASTEST) // when SENSOR_DELAY_NORMAL works
startScan() // without stopScan in onPause
cameraProvider.bindToLifecycle(...) // without checking lifecycle state
mediaPlayer.start() // without corresponding release
```

---

### 7. Background Processing Analysis

Examine background behavior for optimization opportunities:

* **Service Lifecycle:**
  - Identify services that run longer than their work requires
  - Check for `START_STICKY` services that don't need to restart
  - Find foreground services running without active user-facing work
  - Look for services that could be replaced with WorkManager

* **Broadcast Receivers:**
  - Identify manifest-registered receivers for implicit broadcasts that could be context-registered
  - Check for receivers processing broadcasts they should ignore
  - Find receivers triggering expensive work synchronously
  - Look for missing `goAsync()` for long-running receiver work

* **Content Providers & Observers:**
  - Identify ContentObservers not unregistered
  - Check for observers with `notifyForDescendants=true` when not needed
  - Find observers triggering work on every minor change
  - Look for missing debouncing of rapid observer callbacks

**Code Patterns to Search:**
```kotlin
// Problematic patterns to find:
START_STICKY // when START_NOT_STICKY would work
startForegroundService(...) // without timely stopSelf
registerReceiver(broadcastReceiver, intentFilter) // without unregister
contentResolver.registerContentObserver(...) // without unregister
```

---

### 8. Memory & Resource Leaks Analysis

Find leaks that cause increased GC and CPU usage:

* **Context Leaks:**
  - Identify Activity context stored in singletons or companion objects
  - Check for anonymous inner classes holding Activity references
  - Find static handlers or runnables with Activity callbacks
  - Look for ViewModels storing View or Context references

* **Bitmap & Drawable Leaks:**
  - Identify large bitmaps not recycled when no longer displayed
  - Check for Glide/Coil requests not tied to lifecycle
  - Find drawable callbacks holding references after view destruction
  - Look for image loading without proper sizing

* **Listener & Callback Leaks:**
  - Identify listeners registered but never unregistered
  - Check for callbacks holding strong references to destroyed objects
  - Find observers not removed in `onCleared()` or `onDestroy()`
  - Look for event bus subscriptions not unsubscribed

**Code Patterns to Search:**
```kotlin
// Problematic patterns to find:
companion object { var context: Context? = null } // context leak
object Singleton { lateinit var activity: Activity } // activity leak
inner class MyCallback : SomeCallback // holds implicit reference
Handler(Looper.getMainLooper()) // in Activity without weak reference
```

---

### 9. Animation & Rendering Analysis

Review graphics operations for power efficiency:

* **Animation Efficiency:**
  - Identify animations running when view is not visible
  - Check for `ValueAnimator` or `ObjectAnimator` not cancelled in `onPause()`
  - Find animations with unnecessarily high frame rates
  - Look for `repeatCount = INFINITE` without proper lifecycle management

* **Compose Animation Issues:**
  - Identify `animate*AsState` with targets that never stabilize
  - Check for `rememberInfiniteTransition` animations not stopped when off-screen
  - Find expensive calculations inside animation lambdas
  - Look for animations triggering full recomposition

* **Rendering Overhead:**
  - Identify overdraw from overlapping opaque elements
  - Check for hardware layers not removed after animations
  - Find canvas operations that could be cached
  - Look for unnecessary alpha compositing

**Code Patterns to Search:**
```kotlin
// Problematic patterns to find:
infiniteTransition.animateFloat(...) // without lifecycle consideration
animator.repeatCount = ValueAnimator.INFINITE // without cancel
Modifier.graphicsLayer { } // with changing content every frame
Canvas operations in onDraw without caching
```

---

### 10. Data Storage & Sync Analysis

Examine persistence operations for efficiency:

* **Database Operations:**
  - Identify frequent small writes that could be batched
  - Check for Room queries running on main thread
  - Find transactions not used for multiple operations
  - Look for missing indices on frequently queried columns

* **SharedPreferences/DataStore:**
  - Identify `commit()` used where `apply()` would work
  - Check for DataStore collected without lifecycle awareness
  - Find frequent preference updates that could be debounced
  - Look for large objects serialized to preferences

* **File Operations:**
  - Identify file I/O on main thread
  - Check for files opened but not closed in finally blocks
  - Find redundant file reads that could be cached
  - Look for sync operations that could be deferred

**Code Patterns to Search:**
```kotlin
// Problematic patterns to find:
sharedPreferences.edit().putString(...).commit() // blocking commit
room.query(...) // on main thread without suspend
File(...).readText() // without Dispatchers.IO
dataStore.data.collect { } // without repeatOnLifecycle
```

---

## Expected Output

Provide a comprehensive battery drain analysis report with the following structure:

### 1. Executive Summary

```
## Battery Drain Analysis Summary

**Application:** [App name/package]
**Analysis Date:** [Date]
**Overall Battery Health Score:** [A/B/C/D/F with explanation]

### Key Findings
- **Critical Issues:** [Count] issues requiring immediate attention
- **High Priority:** [Count] optimizations with significant impact
- **Medium Priority:** [Count] improvements for better efficiency
- **Low Priority:** [Count] minor optimizations

### Estimated Impact
- **Current State:** [Description of battery behavior]
- **After Remediation:** [Expected improvement]

### Top 3 Quick Wins
1. [Highest impact, lowest effort fix]
2. [Second highest impact fix]
3. [Third fix]
```

### 2. Detailed Findings

For each issue found, provide:

```
## [Category]: [Issue Title]

**Severity:** Critical / High / Medium / Low
**Battery Impact:** [Estimated drain: e.g., "Prevents device sleep", "Continuous CPU usage", "Excessive radio activation"]
**Location:** [File path and line numbers]

### Problem
[Clear description of what's wrong with the implementation]

### Evidence
```kotlin
// Current problematic code
[Actual code snippet from the codebase]
```

### Why This Drains Battery
[Technical explanation of how this implementation causes drain, without blaming the feature itself]

### Remediation
```kotlin
// Recommended fix
[Corrected code with proper implementation]
```

### Implementation Notes
- [Step-by-step fix instructions]
- [Any migration considerations]
- [Testing recommendations]
```

### 3. Remediation Priority Matrix

```
## Prioritized Action Plan

| Priority | Issue | Impact | Effort | Category |
|----------|-------|--------|--------|----------|
| P0 | [Issue name] | Critical | [Low/Med/High] | [Category] |
| P1 | [Issue name] | High | [Low/Med/High] | [Category] |
| P2 | [Issue name] | Medium | [Low/Med/High] | [Category] |
| P3 | [Issue name] | Low | [Low/Med/High] | [Category] |

### Sprint Recommendations
- **Immediate (This Week):** [P0 items]
- **Short Term (This Sprint):** [P1 items]
- **Medium Term (Next Sprint):** [P2 items]
- **Backlog:** [P3 items]
```

### 4. Verification Checklist

```
## Post-Remediation Verification

### Profiling Steps
- [ ] Run Battery Historian analysis before and after
- [ ] Check CPU profiler for idle state behavior
- [ ] Verify wake lock acquisition in `adb shell dumpsys power`
- [ ] Monitor network activity with Network Profiler
- [ ] Test location drain with Location toggle

### Automated Checks
- [ ] Add StrictMode for main thread violations
- [ ] Enable LeakCanary for memory leak detection
- [ ] Configure Layout Inspector for recomposition counts
- [ ] Set up Firebase Performance for production monitoring

### Test Scenarios
- [ ] App backgrounded for 1 hour - verify minimal battery use
- [ ] Screen off behavior - verify no wake locks held
- [ ] Airplane mode - verify no unnecessary retry loops
- [ ] Poor connectivity - verify exponential backoff
```

### 5. Prevention Guidelines

```
## Prevention Recommendations

### Code Review Checklist
- [ ] All coroutines use appropriate scoped lifecycle
- [ ] Location requests specify minimum accuracy needed
- [ ] Wake locks have timeout and are released in finally blocks
- [ ] Compose state is stable or properly remembered
- [ ] Network requests are cached when appropriate
- [ ] Sensors are unregistered in onPause/onStop

### CI/CD Integration
- Lint rules to add: [Specific lint checks]
- Static analysis: [Detekt/ktlint rules for battery patterns]
- Automated tests: [Battery-aware test recommendations]
```

---

## Example Output

```markdown
## Battery Drain Analysis Summary

**Application:** MyApp (com.example.myapp)
**Analysis Date:** 2024-01-15
**Overall Battery Health Score:** C - Significant optimization opportunities

### Key Findings
- **Critical Issues:** 2 issues requiring immediate attention
- **High Priority:** 4 optimizations with significant impact
- **Medium Priority:** 7 improvements for better efficiency
- **Low Priority:** 3 minor optimizations

---

## Coroutines: Unscoped Location Polling

**Severity:** Critical
**Battery Impact:** Prevents Doze mode, continuous GPS activation, blocks device sleep
**Location:** `app/src/main/java/com/example/location/LocationTracker.kt:45-67`

### Problem
Location updates are requested in a GlobalScope coroutine with high accuracy and frequent intervals. The coroutine continues running after the user leaves the screen, and the location listener is never removed.

### Evidence
```kotlin
// LocationTracker.kt:45-67
class LocationTracker(private val context: Context) {

    fun startTracking() {
        GlobalScope.launch {  // Never cancelled
            val locationRequest = LocationRequest.create().apply {
                priority = LocationRequest.PRIORITY_HIGH_ACCURACY  // Always GPS
                interval = 5000  // Every 5 seconds
            }

            fusedLocationClient.requestLocationUpdates(
                locationRequest,
                locationCallback,
                Looper.getMainLooper()
            )  // Never removed
        }
    }
}
```

### Why This Drains Battery
1. `GlobalScope` means this coroutine outlives any UI lifecycle - it runs until the app process is killed
2. `PRIORITY_HIGH_ACCURACY` forces GPS hardware active, one of the highest power consumers
3. 5-second interval means constant radio activation without allowing the chip to sleep
4. No `removeLocationUpdates()` call means location hardware stays active indefinitely
5. This prevents Android's Doze mode from activating, causing overnight drain

### Remediation
```kotlin
// LocationTracker.kt - Fixed implementation
class LocationTracker @Inject constructor(
    private val fusedLocationClient: FusedLocationProviderClient
) {
    private var locationCallback: LocationCallback? = null

    fun startTracking(
        scope: CoroutineScope,  // Caller provides scoped lifecycle
        onLocation: (Location) -> Unit
    ) {
        val locationRequest = LocationRequest.create().apply {
            // Use balanced power - network location when possible, GPS when needed
            priority = LocationRequest.PRIORITY_BALANCED_POWER_ACCURACY
            // Longer interval with fastest interval for bursts
            interval = 60_000  // 1 minute normal
            fastestInterval = 30_000  // 30 second minimum
            // Don't update for minor movements
            smallestDisplacement = 50f  // 50 meters
        }

        locationCallback = object : LocationCallback() {
            override fun onLocationResult(result: LocationResult) {
                result.lastLocation?.let(onLocation)
            }
        }

        scope.launch {
            try {
                fusedLocationClient.requestLocationUpdates(
                    locationRequest,
                    locationCallback!!,
                    Looper.getMainLooper()
                )
                // Suspend until scope is cancelled
                awaitCancellation()
            } finally {
                // Always clean up when scope ends
                stopTracking()
            }
        }
    }

    fun stopTracking() {
        locationCallback?.let { callback ->
            fusedLocationClient.removeLocationUpdates(callback)
            locationCallback = null
        }
    }
}

// Usage in ViewModel
class MapViewModel @Inject constructor(
    private val locationTracker: LocationTracker
) : ViewModel() {

    init {
        locationTracker.startTracking(viewModelScope) { location ->
            // Handle location - automatically stops when ViewModel clears
        }
    }
}
```

### Implementation Notes
1. Replace `GlobalScope` with caller-provided `CoroutineScope` (e.g., `viewModelScope`)
2. Use `PRIORITY_BALANCED_POWER_ACCURACY` unless GPS precision is genuinely required
3. Add `smallestDisplacement` to avoid updates for minor movements
4. Use `awaitCancellation()` with finally block to guarantee cleanup
5. Test by backgrounding app and verifying location icon disappears from status bar

---

## Prioritized Action Plan

| Priority | Issue | Impact | Effort | Category |
|----------|-------|--------|--------|----------|
| P0 | Unscoped location polling | Critical | Medium | Coroutines |
| P0 | Wake lock never released in SyncService | Critical | Low | Wake Locks |
| P1 | StateFlow collected without lifecycle | High | Low | Compose |
| P1 | Polling API every 10 seconds | High | Medium | Network |
| P1 | Sensor listener active when backgrounded | High | Low | Sensors |
| P1 | Infinite animation on hidden tab | High | Low | Animation |
```

---

## Techniques Used

- **ST-01** (Clear Objective): Focus on implementation issues, not feature criticism
- **ST-02** (Sequential Instructions): Organized by subsystem for systematic review
- **RT-02** (Multi-Dimensional Analysis): 10 distinct analysis dimensions
- **RT-05** (Evidence-Based Reasoning): Code patterns and specific examples required
- **ST-03** (Structured Output Templates): Consistent issue reporting format
- **OC-05** (Severity Classification): Priority matrix for remediation planning
- **DS-06** (Prioritization Guidance): Action plan with effort/impact analysis

---

## Related Prompts

- `android_kotlin_best_practices.md` - General code quality review including performance
- `mobile_app_security_review.md` - Security aspects that may overlap with battery (e.g., background service permissions)
- `android_compose_ui_improvement.md` - UI-specific optimizations including recomposition
- `performance_bottleneck_identification.md` - General performance analysis techniques
- `performance_resource_usage_profiling.md` - Memory and CPU profiling guidance

---

## Customization Guide

- **For Compose-only apps:** Emphasize Section 2 (Recomposition) and Section 9 (Animation), reduce focus on XML-related patterns
- **For apps with heavy location features:** Expand Section 4 with geofencing patterns and significant location change APIs
- **For media/streaming apps:** Add dedicated section for ExoPlayer/MediaSession optimization
- **For IoT/Bluetooth apps:** Expand Section 6 with BLE connection parameter optimization
- **For apps targeting Wear OS:** Add Wear-specific considerations (ambient mode, complications)
- **For enterprise apps with sync:** Expand Section 7 and 10 with SyncAdapter and AccountManager patterns
- **Specify API level:** "Target API 34+" enables analysis of Android 14 specific optimizations like foreground service types
