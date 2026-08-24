---
title: "Android Geofence and Location Services Review"
category: mobile/android/targeted-reviews
description: "Android Geofence and Location Services Review."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - geofence
  - location
  - mobile
  - review
  - reviews
updated: "2026-03-19"
related_prompts: []
---

# Android Geofence and Location Services Review

**Objective:** Conduct a targeted review of geofencing and location services implementation in Android applications, analyzing permission handling, geofence registration reliability, battery optimization, privacy compliance, and background location access patterns.

**When to Use:** Use this prompt when debugging missed geofence triggers, optimizing location-based features for battery, before adding new location-aware functionality, during privacy audits, or when preparing for Google Play policy reviews regarding background location access.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the actual permission and location flow** - Don't flag based on pattern matching alone. Verify that the suspected issue actually causes permission problems or location failures.
2. **Check for existing permission handling** - Search for permission request dialogs, rationale screens, or settings navigation that may already address concerns.
3. **Understand the context** - Consider WHY certain location accuracy or background access is needed. App use cases dictate requirements.
4. **Confirm actual policy compliance** - Test against Google Play's Background Location policy requirements with real scenarios.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `LocationService.kt:92`).

**Finding NO issues is an acceptable outcome.** If location handling follows best practices and policy requirements, say so with confidence. Don't manufacture compliance concerns.

### False-Positive Prevention

- ❌ Do NOT flag background location access as wrong if app legitimately requires it (e.g., fitness tracking, navigation)
- ❌ Do NOT flag based solely on manifest permissions without checking actual usage
- ❌ Do NOT assume missing permission handling without searching the codebase
- ❌ Do NOT report battery drain concerns without evidence from actual profiling
- ✅ DO understand Google Play's Background Location policy and legitimate exceptions
- ✅ DO check for Foreground Service usage for continuous location
- ✅ DO verify geofence radius choices match the use case requirements
- ✅ DO consider device-specific behavior (OEM battery optimizations)

---

### 1. Permission Handling

Analyze location permission implementation:

* **Permission Request Flow:**
  - Review foreground location permission request (ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION)
  - Check background location permission request (ACCESS_BACKGROUND_LOCATION)
  - Assess incremental permission request pattern (foreground first, then background)
  - Verify permission rationale dialogs

* **Permission State Handling:**
  - Review permission check before location operations
  - Check for graceful degradation without permission
  - Assess "Don't ask again" state handling
  - Verify settings navigation for denied permissions

* **Runtime Permission Best Practices:**
  - Check for in-context permission requests (when user needs feature)
  - Review permission request timing (not on app launch)
  - Assess permission request result handling
  - Verify no functionality blocked without explanation

### 2. Geofence Registration

Evaluate geofence setup and management:

* **Geofence Configuration:**
  - Review geofence radius selection (minimum 100m recommended)
  - Check transition types (ENTER, EXIT, DWELL) appropriateness
  - Assess expiration duration settings
  - Verify notification responsiveness settings

* **Registration Reliability:**
  - Check for geofence limit handling (100 per app maximum)
  - Review re-registration after boot (BOOT_COMPLETED receiver)
  - Assess re-registration after location settings change
  - Verify handling of registration failures

* **Geofence Lifecycle:**
  - Review geofence removal when no longer needed
  - Check for orphaned geofences on data deletion
  - Assess geofence update patterns (remove + add vs. update)
  - Verify proper cleanup on user logout

### 3. Geofence Triggering

Analyze trigger reliability:

* **Trigger Reception:**
  - Review GeofenceBroadcastReceiver implementation
  - Check for proper PendingIntent configuration (FLAG_MUTABLE/IMMUTABLE)
  - Assess trigger handling in various app states (foreground, background, killed)
  - Verify WakeLock handling for processing

* **Trigger Processing:**
  - Check geofence transition event parsing
  - Review triggering geofence identification
  - Assess multiple simultaneous trigger handling
  - Verify error event handling (GEOFENCE_NOT_AVAILABLE, TOO_MANY_GEOFENCES)

* **Edge Cases:**
  - Check behavior when device location is stale
  - Review handling of location accuracy fluctuations
  - Assess behavior at geofence boundaries
  - Verify handling of rapid enter/exit sequences

### 4. Battery Optimization

Evaluate power consumption:

* **Location Request Configuration:**
  - Review location accuracy settings (PRIORITY_BALANCED_POWER_ACCURACY for geofences)
  - Check location update interval appropriateness
  - Assess fastest update interval settings
  - Verify location request removed when not needed

* **Doze Mode Compatibility:**
  - Check geofence behavior during Doze mode
  - Review high-priority FCM for location updates if needed
  - Assess WorkManager integration for location tasks
  - Verify no excessive wake-ups

* **Battery Optimization Exemptions:**
  - Review REQUEST_IGNORE_BATTERY_OPTIMIZATIONS usage
  - Check for proper user education about battery settings
  - Assess impact of battery saver mode
  - Verify graceful degradation under power restrictions

### 5. Background Location Access

Analyze background location patterns:

* **Play Store Compliance:**
  - Review background location access justification
  - Check for prominent disclosure of background location use
  - Assess core functionality requirement for background location
  - Verify privacy policy coverage

* **Background Access Minimization:**
  - Check if foreground location could suffice
  - Review alternatives to continuous background location
  - Assess geofence-only vs. continuous location needs
  - Verify location access stops when not needed

* **User Control:**
  - Review user ability to disable location features
  - Check for location usage transparency in app
  - Assess granular location permissions (per-feature)
  - Verify location access indicators

### 6. Location Provider Strategy

Evaluate location sourcing:

* **Fused Location Provider:**
  - Review FusedLocationProviderClient usage
  - Check for proper client connection/disconnection
  - Assess location settings resolution
  - Verify Play Services availability checks

* **Location Request Parameters:**
  - Review priority settings for different use cases
  - Check interval vs. fastest interval configuration
  - Assess maximum wait time settings
  - Verify displacement threshold usage

* **Fallback Strategies:**
  - Check handling of location unavailable scenarios
  - Review fallback to last known location
  - Assess timeout handling for location requests
  - Verify behavior when GPS/network location disabled

### 7. Privacy and Security

Analyze privacy implementation:

* **Location Data Handling:**
  - Review local storage of location data (encryption?)
  - Check location data transmission security
  - Assess location data retention policy
  - Verify location data deletion on request

* **User Privacy Features:**
  - Review location accuracy reduction options
  - Check for approximate vs. precise location support
  - Assess location sharing visibility
  - Verify no unnecessary location collection

* **Sensitive Location Protection:**
  - Check for geofence around sensitive locations (home, work)
  - Review location data anonymization
  - Assess location history purging
  - Verify no location data in crash reports/logs

### 8. Testing and Debugging

Evaluate testability:

* **Location Mocking:**
  - Review mock location handling for testing
  - Check for ADB location simulation support
  - Assess emulator location testing
  - Verify production detection of mock locations

* **Geofence Testing:**
  - Review geofence testing approach
  - Check for geofence simulation capabilities
  - Assess testing of edge cases (boundary, rapid movement)
  - Verify automated testing strategies

### 9. Error Handling and Recovery

Analyze failure scenarios:

* **Common Error Handling:**
  - Check GEOFENCE_NOT_AVAILABLE error handling
  - Review TOO_MANY_GEOFENCES error recovery
  - Assess GEOFENCE_TOO_MANY_PENDING_INTENTS handling
  - Verify proper user feedback on errors

* **Recovery Strategies:**
  - Review automatic retry for transient failures
  - Check for exponential backoff on errors
  - Assess user intervention prompts when needed
  - Verify error logging for debugging

---

## Expected Output

Provide a comprehensive geofence and location review report including:

### 1. Executive Summary
- Overall location implementation health rating
- Permission handling assessment
- Geofence reliability rating
- Battery impact assessment
- Play Store compliance status

### 2. Permission Flow Assessment

| Permission | Request Timing | Rationale | Fallback | Status |
|------------|----------------|-----------|----------|--------|
| [Permission] | [When] | [Shown?] | [Behavior] | [OK/Issue] |

### 3. Geofence Inventory

| Geofence Type | Count | Radius | Transitions | Expiration | Issues |
|---------------|-------|--------|-------------|------------|--------|
| [Type] | [#] | [meters] | [Types] | [Duration] | [Count] |

### 4. Detailed Findings

For each issue:
- **Location:** File and method
- **Issue:** Description
- **Impact:** Reliability/battery/privacy effect
- **Severity:** Critical/High/Medium/Low
- **Current Code:** Problematic pattern
- **Recommended Fix:** Corrected implementation
- **Verification:** How to test the fix

### 5. Battery Impact Analysis

| Component | Power Impact | Optimization | Status |
|-----------|--------------|--------------|--------|
| [Component] | [High/Med/Low] | [Action] | [OK/Issue] |

### 6. Compliance Checklist

| Requirement | Status | Evidence | Action |
|-------------|--------|----------|--------|
| [Requirement] | [Met/Not Met] | [Where] | [If needed] |

### 7. Prioritized Recommendations

Ordered by reliability and compliance impact.

---

## Example Output

```markdown
# Geofence and Location Services Review Report

## Executive Summary
- **Overall Health:** Needs Attention
- **Permission Handling:** Good with minor improvements
- **Geofence Reliability:** Issues with re-registration
- **Battery Impact:** Medium - optimization opportunities exist
- **Play Store Compliance:** At risk - background location justification needed

## Critical Findings

### CRITICAL-1: Geofences Lost After Device Reboot
**Severity:** Critical
**Impact:** Location reminders fail until app is opened

**Location:** GeofenceManager.kt

**Current Implementation:**
```kotlin
// Geofences registered but not persisted
class GeofenceManager @Inject constructor(
    private val geofencingClient: GeofencingClient
) {
    fun registerGeofence(location: Location, todoId: String) {
        val geofence = Geofence.Builder()
            .setRequestId(todoId)
            .setCircularRegion(location.lat, location.lng, 150f)
            .setTransitionTypes(Geofence.GEOFENCE_TRANSITION_ENTER)
            .setExpirationDuration(Geofence.NEVER_EXPIRE)
            .build()

        val request = GeofencingRequest.Builder()
            .addGeofence(geofence)
            .setInitialTrigger(GeofencingRequest.INITIAL_TRIGGER_ENTER)
            .build()

        geofencingClient.addGeofences(request, pendingIntent)
        // PROBLEM: No persistence! Lost on reboot.
    }
}

// MISSING: Boot receiver to re-register geofences
```

**Problem:**
1. User creates todo with location reminder
2. Geofence registered successfully
3. Device reboots (or location settings toggled)
4. All geofences cleared by system
5. User never gets location reminder

**Recommended Fix:**
```kotlin
// 1. Persist geofence data in Room
@Entity(tableName = "geofence_state")
data class GeofenceStateEntity(
    @PrimaryKey val requestId: String,
    val latitude: Double,
    val longitude: Double,
    val radius: Float,
    val transitionTypes: Int,
    val associatedTodoId: String,
    val registeredAt: Long
)

// 2. Add boot receiver
class BootReceiver : BroadcastReceiver() {
    @Inject lateinit var geofenceRestorer: GeofenceRestorer

    override fun onReceive(context: Context, intent: Intent) {
        if (intent.action == Intent.ACTION_BOOT_COMPLETED ||
            intent.action == Intent.ACTION_MY_PACKAGE_REPLACED ||
            intent.action == LocationManager.PROVIDERS_CHANGED_ACTION) {

            // Restore geofences from database
            goAsync().let { result ->
                CoroutineScope(Dispatchers.IO).launch {
                    geofenceRestorer.restoreAllGeofences()
                    result.finish()
                }
            }
        }
    }
}

// 3. Register receiver in manifest
<receiver
    android:name=".todo.BootReceiver"
    android:exported="false">
    <intent-filter>
        <action android:name="android.intent.action.BOOT_COMPLETED"/>
        <action android:name="android.intent.action.MY_PACKAGE_REPLACED"/>
        <action android:name="android.location.PROVIDERS_CHANGED"/>
    </intent-filter>
</receiver>

// 4. WorkManager for reliable restoration
class ReregisterGeofencesWorker : CoroutineWorker {
    override suspend fun doWork(): Result {
        val savedGeofences = geofenceDao.getAllActive()

        savedGeofences.chunked(50).forEach { batch ->
            val geofences = batch.map { entity ->
                Geofence.Builder()
                    .setRequestId(entity.requestId)
                    .setCircularRegion(entity.latitude, entity.longitude, entity.radius)
                    .setTransitionTypes(entity.transitionTypes)
                    .setExpirationDuration(Geofence.NEVER_EXPIRE)
                    .build()
            }

            val result = geofencingClient.addGeofences(
                GeofencingRequest.Builder().addGeofences(geofences).build(),
                pendingIntent
            ).await()
        }

        return Result.success()
    }
}
```

---

### HIGH-1: Background Location Permission Request on First Launch
**Severity:** High
**Impact:** Poor UX, likely permission denial, Play Store policy violation

**Location:** OnboardingActivity.kt

**Current Implementation:**
```kotlin
// PROBLEM: Asking for background location immediately
class OnboardingActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Bad: Requesting all permissions upfront
        ActivityCompat.requestPermissions(
            this,
            arrayOf(
                Manifest.permission.ACCESS_FINE_LOCATION,
                Manifest.permission.ACCESS_BACKGROUND_LOCATION  // Too early!
            ),
            PERMISSION_REQUEST_CODE
        )
    }
}
```

**Problems:**
1. Users don't understand why background location is needed
2. Higher chance of denial
3. Violates Play Store policy (must explain need first)
4. No in-context request

**Recommended Fix:**
```kotlin
// 1. Request foreground permission when user first uses location feature
class TodoEditorScreen {
    fun onAddLocationReminder() {
        when {
            hasForegroundLocationPermission() -> {
                showLocationPicker()
            }
            shouldShowRationale() -> {
                showForegroundLocationRationale {
                    requestForegroundLocationPermission()
                }
            }
            else -> {
                requestForegroundLocationPermission()
            }
        }
    }
}

// 2. Request background permission only when actually needed
class LocationReminderSetupScreen {
    fun onConfirmLocationReminder() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            if (!hasBackgroundLocationPermission()) {
                // Show education dialog first
                showBackgroundLocationEducation(
                    onAccept = { requestBackgroundLocationPermission() },
                    onDecline = { offerForegroundOnlyAlternative() }
                )
            }
        }
        // Proceed with geofence setup
    }
}

// 3. Background location education dialog
@Composable
fun BackgroundLocationEducationDialog(
    onAccept: () -> Unit,
    onDecline: () -> Unit
) {
    AlertDialog(
        title = { Text("Location Reminders Need Background Access") },
        text = {
            Column {
                Text("To remind you when you arrive at or leave a location, " +
                     "the app needs to check your location in the background.")
                Spacer(modifier = Modifier.height(8.dp))
                Text("On the next screen, please select 'Allow all the time'.")
                Spacer(modifier = Modifier.height(8.dp))
                Text("Your location is only used for reminders you create " +
                     "and is never shared.", style = MaterialTheme.typography.bodySmall)
            }
        },
        confirmButton = {
            Button(onClick = onAccept) { Text("Continue") }
        },
        dismissButton = {
            TextButton(onClick = onDecline) { Text("Not Now") }
        }
    )
}
```

---

### HIGH-2: Geofence Radius Too Small
**Severity:** High
**Impact:** Unreliable triggers, user frustration

**Location:** GeofenceManager.kt

**Current Implementation:**
```kotlin
fun registerGeofence(location: Location) {
    val geofence = Geofence.Builder()
        .setRequestId(location.id)
        .setCircularRegion(location.lat, location.lng, 50f)  // 50 meters!
        .setTransitionTypes(Geofence.GEOFENCE_TRANSITION_ENTER)
        .build()
}
```

**Problem:**
- 50m radius is too small for reliable GPS accuracy
- Urban areas with tall buildings cause GPS drift
- User might be "inside" geofence but GPS shows outside
- Triggers are inconsistent

**Recommended Fix:**
```kotlin
fun registerGeofence(location: Location) {
    // Use minimum 100m, or allow user to choose
    val radius = maxOf(location.customRadius ?: DEFAULT_RADIUS, MIN_RELIABLE_RADIUS)

    val geofence = Geofence.Builder()
        .setRequestId(location.id)
        .setCircularRegion(location.lat, location.lng, radius)
        .setTransitionTypes(Geofence.GEOFENCE_TRANSITION_ENTER)
        // Add dwell for more reliable triggers
        .setLoiteringDelay(30_000)  // 30 seconds dwell
        .build()

    companion object {
        const val MIN_RELIABLE_RADIUS = 100f  // meters
        const val DEFAULT_RADIUS = 150f  // meters
    }
}

// Let user understand radius implications
@Composable
fun RadiusSelector(
    currentRadius: Float,
    onRadiusChange: (Float) -> Unit
) {
    Column {
        Text("Trigger Distance: ${currentRadius.toInt()}m")
        Slider(
            value = currentRadius,
            onValueChange = onRadiusChange,
            valueRange = 100f..500f,
            steps = 7
        )
        Text(
            when {
                currentRadius < 150 -> "Precise but may miss triggers in buildings"
                currentRadius < 300 -> "Balanced - recommended for most locations"
                else -> "Reliable but triggers from further away"
            },
            style = MaterialTheme.typography.bodySmall
        )
    }
}
```

---

### MEDIUM-1: Missing PendingIntent Mutability Flag
**Severity:** Medium
**Impact:** Crash on Android 12+ devices

**Location:** GeofencePendingIntentFactory.kt

**Current Implementation:**
```kotlin
// PROBLEM: Missing mutability flag for Android 12+
private fun createPendingIntent(): PendingIntent {
    val intent = Intent(context, GeofenceBroadcastReceiver::class.java)
    return PendingIntent.getBroadcast(
        context,
        0,
        intent,
        PendingIntent.FLAG_UPDATE_CURRENT  // Missing FLAG_MUTABLE or FLAG_IMMUTABLE
    )
}
```

**Recommended Fix:**
```kotlin
private fun createPendingIntent(): PendingIntent {
    val intent = Intent(context, GeofenceBroadcastReceiver::class.java)
    val flags = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
        PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_MUTABLE
    } else {
        PendingIntent.FLAG_UPDATE_CURRENT
    }
    return PendingIntent.getBroadcast(context, 0, intent, flags)
}
```

---

## Permission Flow Assessment

| Permission | Request Timing | Rationale | Fallback | Status |
|------------|----------------|-----------|----------|--------|
| ACCESS_FINE_LOCATION | Onboarding ❌ | None shown ❌ | None ❌ | Needs Work |
| ACCESS_COARSE_LOCATION | Onboarding ❌ | None shown ❌ | None ❌ | Needs Work |
| ACCESS_BACKGROUND_LOCATION | Onboarding ❌ | None shown ❌ | None ❌ | Critical |

## Geofence Configuration Summary

| Type | Count | Radius | Transitions | Reliable | Issues |
|------|-------|--------|-------------|----------|--------|
| Todo Location | Dynamic | 50m ❌ | ENTER | No | 2 |
| Favorite Place | 5 max | 100m | ENTER, EXIT | Partial | 1 |
| Home/Work | 2 | 150m | DWELL | Yes | 0 |

## Battery Impact Assessment

| Component | Impact | Current State | Optimization |
|-----------|--------|---------------|--------------|
| Geofencing | Low ✓ | Using FLP | OK |
| Location Updates | Medium | Continuous in some cases | Reduce frequency |
| Boot Re-registration | Low ✓ | WorkManager | OK |
| Background Service | High ❌ | Long-running service found | Convert to WorkManager |

## Play Store Compliance

| Requirement | Status | Evidence | Action Needed |
|-------------|--------|----------|---------------|
| Prominent Disclosure | ❌ | None found | Add in-app disclosure |
| Background Location Justification | ⚠️ | Minimal | Strengthen justification |
| Privacy Policy | ✓ | Covers location | None |
| In-Context Permission | ❌ | Asked at launch | Move to feature use |
| Foreground-First | ❌ | Both at once | Request sequentially |

## Remediation Priority

### Critical (Immediate)
1. Add geofence persistence and re-registration after boot
2. Fix permission request flow (in-context, foreground-first)

### High Priority (This Sprint)
1. Increase minimum geofence radius to 100m
2. Add background location education dialog
3. Fix PendingIntent mutability flags

### Medium Priority (Next Sprint)
1. Add prominent disclosure for background location
2. Implement graceful degradation without background permission
3. Add location usage transparency UI

### Low Priority (Backlog)
1. Add geofence testing utilities
2. Implement location accuracy monitoring
3. Add battery impact monitoring
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Focused geofence/location review
- **ST-02** (Structured Sequential Instructions) - Systematic review areas
- **RT-02** (Multi-Dimensional Analysis) - Permission, reliability, battery, privacy
- **RT-05** (Evidence-Based Reasoning) - Specific code examples
- **ST-03** (Output Format Templates) - Compliance checklists
- **DS-06** (Prioritization Guidance) - Reliability and compliance focus
- **QA-02** (Adversarial Stress-Test) - Edge case analysis

---

## Related Prompts

- `android_workmanager_background_review.md` - For background task integration
- `mobile_app_security_review.md` - For location privacy security
- `android_kotlin_best_practices.md` - General patterns
- `android_battery_drain_investigation.md` - For power optimization
- `android_notification_channel_review.md` - For location notifications

---

## Customization Guide

- **For Fleet/Logistics Apps:** Add continuous location tracking review, route optimization
- **For Social Apps:** Add location sharing privacy, approximate location support
- **For Fitness Apps:** Add activity recognition integration, workout tracking
- **For Safety Apps:** Add emergency location access, always-on location justification
- **For Child Tracking:** Add COPPA compliance, parental consent review
