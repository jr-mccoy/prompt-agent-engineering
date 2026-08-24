---
title: "Android Version Upgrade (targetSdk Execution Runbook)"
category: mobile-development
description: "Executes a targetSdk version upgrade — applying behavior changes, permission updates, and API migrations from a migration plan, then verifying and rolling out safely"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - android
  - mobile-development
  - targetSdk
  - sdk-migration
  - maintenance
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/maintenance/android_target_sdk_migration.md
  - domain-software-engineering/mobile/android/maintenance/android_sdk_migration.md
  - domain-software-engineering/mobile/android/maintenance/android_build_toolchain_upgrade.md
  - domain-software-engineering/mobile/android/publishing/android_staged_rollout.md
---

# Android Version Upgrade

**Objective:** Upgrade an Android app's targetSdk version to meet Google Play Store requirements, implementing required behavior changes, permission updates, and API migrations while maintaining backward compatibility.

**When to Use:** Use this prompt when you need to increase your app's targetSdk to comply with Play Store requirements, access new Android features, or modernize your app for newer Android versions. Ideal when Google announces new targetSdk deadlines, when preparing major releases, or when users report issues on newer Android versions. Prerequisites include understanding your current SDK configuration and having test devices or emulators for target Android versions.

> **Role — Execution runbook.** This prompt **executes** a targetSdk upgrade: apply changes, fix, test, and roll out. For the upstream **planning** step — systematically mapping every behavior change between your current and target API level, scoping effort, and tracking the Play deadline — run [`android_target_sdk_migration.md`](android_target_sdk_migration.md) first, then bring its plan here. The two prompts chain: **planner → executor**.

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

Before beginning the version upgrade, gather essential context:

1. **Current Configuration:**
   - "What is your current targetSdk version?"
   - "What is your minSdk version?"
   - "What Android versions do your users primarily use?"

2. **Upgrade Target:**
   - "What targetSdk are you upgrading to? (e.g., 34 for Android 14)"
   - "Is this driven by Play Store deadline or feature requirements?"

3. **App Characteristics:**
   - "Does your app use any special permissions? (location, camera, storage, etc.)"
   - "Does your app have background services or work?"
   - "Does your app use foreground services?"

4. **Risk Assessment:**
   - "Are there any known issues with your app on newer Android versions?"
   - "Do you have comprehensive test coverage for affected areas?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending ANY change, you MUST:**

1. **Trace actual requirements** - Don't recommend changes without understanding specific behavior changes for the target SDK.
2. **Check for existing handling** - Search for existing permission handling, foreground service configurations, or compatibility code.
3. **Understand the context** - Consider the app's actual usage patterns and what permissions/features it needs.
4. **Confirm actual impact** - Will this behavior change actually affect this app's functionality?
5. **Provide specific file:line locations** - Every change must include exact code locations (e.g., `AndroidManifest.xml:45`).

**Finding MINIMAL required changes is an acceptable outcome.** Not every app uses every feature affected by SDK changes.

### False-Positive Prevention

- ❌ Do NOT recommend changes for features the app doesn't use
- ❌ Do NOT assume the app needs every permission-related update
- ❌ Do NOT ignore existing compatibility handling
- ❌ Do NOT recommend unnecessary permission additions
- ✅ DO check what features the app actually uses before recommending changes
- ✅ DO reference official Android documentation for behavior changes
- ✅ DO test on actual target SDK version devices/emulators
- ✅ DO consider gradual migration paths for complex changes

---

### Phase 1: SDK Configuration Analysis

Analyze current SDK configuration and identify upgrade requirements.

#### 1.1 Current SDK Audit

**Examine build configuration:**

```kotlin
// app/build.gradle.kts
android {
    compileSdk = 33  // Current compile SDK

    defaultConfig {
        minSdk = 24      // Minimum supported version
        targetSdk = 33   // Current target SDK
    }
}
```

**Document current configuration:**

| Setting | Current Value | Target Value | Gap |
|---------|--------------|--------------|-----|
| compileSdk | 33 | 35 | +2 |
| targetSdk | 33 | 35 | +2 |
| minSdk | 24 | 24 | 0 |
| AGP | 8.1.0 | 8.5.0+ | Required |
| Kotlin | 1.9.0 | 2.0.0+ | Recommended |

#### 1.2 Behavior Changes Inventory

**Identify required behavior changes for each SDK level:**

```markdown
## SDK 34 (Android 14) Behavior Changes

### All Apps (regardless of targetSdk)
- [ ] Non-dismissible foreground notifications require user action
- [ ] Runtime-registered broadcasts must specify export behavior
- [ ] Minimum installable targetSdk is 23

### Apps Targeting SDK 34+
- [ ] Foreground service types must be declared
- [ ] SCHEDULE_EXACT_ALARM requires user permission
- [ ] Photo/Video partial access for media permissions
- [ ] Must handle new back gesture behavior
- [ ] Restrictions on implicit intents
- [ ] BLUETOOTH_CONNECT required for Bluetooth APIs

## SDK 35 (Android 15) Behavior Changes

### All Apps
- [ ] Edge-to-edge enforcement
- [ ] 16KB page size support (NDK)

### Apps Targeting SDK 35+
- [ ] Private space support
- [ ] Foreground service restrictions
- [ ] Must declare foreground service types in manifest
```

#### 1.3 Permission Changes Analysis

**Audit permission requirements:**

```kotlin
// Permissions that changed between SDK versions:

// SDK 33 (Android 13) Introduced:
// - POST_NOTIFICATIONS (for push notifications)
// - READ_MEDIA_IMAGES, READ_MEDIA_VIDEO, READ_MEDIA_AUDIO
//   (replaced READ_EXTERNAL_STORAGE for media)

// SDK 34 (Android 14) Changes:
// - SCHEDULE_EXACT_ALARM now requires explicit grant
// - Foreground service types required for FGS
// - USE_FULL_SCREEN_INTENT restricted to specific apps

// SDK 35 (Android 15) Changes:
// - Additional foreground service restrictions
```

**Create permission migration checklist:**

| Permission | Current Usage | SDK 34+ Requirement | Action Needed |
|------------|---------------|---------------------|---------------|
| READ_EXTERNAL_STORAGE | Media access | Split into READ_MEDIA_* | Migrate |
| SCHEDULE_EXACT_ALARM | Alarms | User grant required | Add flow |
| POST_NOTIFICATIONS | Push | Runtime request | Add request |
| FOREGROUND_SERVICE | Background work | Declare FGS type | Update manifest |

---

### Phase 2: Impact Assessment

Evaluate the scope of changes required.

#### 2.1 Codebase Impact Analysis

**Search for affected patterns:**

```kotlin
// Patterns to search for SDK 34 migration:

// 1. Foreground Services without type
// Search: "startForegroundService" or "startForeground("
// Action: Add foreground service type declaration

// 2. Broadcast receivers
// Search: "registerReceiver(" without RECEIVER_EXPORTED/NOT_EXPORTED
// Action: Add export flag

// 3. Exact alarms
// Search: "setExact(", "setExactAndAllowWhileIdle("
// Action: Check SCHEDULE_EXACT_ALARM permission

// 4. PendingIntent without mutability
// Search: "PendingIntent." without FLAG_MUTABLE/FLAG_IMMUTABLE
// Action: Add mutability flag

// 5. Media access
// Search: "READ_EXTERNAL_STORAGE", "WRITE_EXTERNAL_STORAGE"
// Action: Migrate to scoped storage / photo picker

// 6. Implicit intents
// Search: "intent.setPackage", intent without explicit package
// Action: Make intents explicit where required
```

#### 2.2 Feature-Specific Impact

**Analyze major features:**

```markdown
## Feature Impact Assessment

### Background Work
| Component | Impact | Changes Required |
|-----------|--------|------------------|
| WorkManager | Low | Verify expedited work |
| Foreground Services | High | Add FGS types |
| AlarmManager | Medium | Handle SCHEDULE_EXACT_ALARM |
| JobScheduler | Low | Verify constraints |

### Notifications
| Component | Impact | Changes Required |
|-----------|--------|------------------|
| Push notifications | Medium | POST_NOTIFICATIONS permission |
| Foreground service notifications | High | Non-dismissible changes |
| Custom notifications | Low | Style compatibility |

### Storage & Media
| Component | Impact | Changes Required |
|-----------|--------|------------------|
| Photo/video access | High | Photo picker or partial access |
| File downloads | Medium | Download manager or MediaStore |
| App-specific files | None | Already scoped |

### UI & Navigation
| Component | Impact | Changes Required |
|-----------|--------|------------------|
| Predictive back | Medium | Implement back handler |
| Edge-to-edge | High (SDK 35) | Handle insets |
| Large screens | Low | Verify layouts |
```

---

### Phase 3: Findings Presentation

**CHECKPOINT 1:** Present the upgrade analysis and impact assessment.

```markdown
## SDK Upgrade Analysis Report

### Upgrade Path
- **Current:** targetSdk 33 (Android 13)
- **Target:** targetSdk 35 (Android 15)
- **Behavior Change Levels:** 2 (SDK 34 + SDK 35)

### Impact Summary
| Category | High Impact | Medium Impact | Low Impact |
|----------|-------------|---------------|------------|
| Permissions | 2 | 1 | 0 |
| Services | 3 | 1 | 0 |
| UI/UX | 1 | 2 | 1 |
| Storage | 1 | 1 | 0 |

### Required Changes

#### Must Fix (Breaking)
1. **Foreground Service Types** - 4 services need FGS type declaration
2. **Broadcast Receiver Export** - 6 receivers need export flag
3. **POST_NOTIFICATIONS Permission** - Push notifications require runtime permission

#### Should Fix (Warnings/Deprecations)
1. **Photo Picker Migration** - Replace media permission with photo picker
2. **PendingIntent Mutability** - 12 intents need FLAG_IMMUTABLE

#### Nice to Have (Modernization)
1. **Predictive Back Gesture** - Improve navigation UX
2. **Edge-to-Edge** - Modern visual design (required in SDK 35)

### Estimated Effort
- **Total Changes:** 28 code locations
- **Estimated Time:** [X] hours
- **Risk Level:** Medium

**Would you like me to proceed with the implementation, starting with the most critical changes?**
```

---

### Phase 4: Implementation

Implement SDK upgrade changes systematically.

#### 4.1 Build Configuration Update

**Update SDK versions:**

```kotlin
// app/build.gradle.kts
android {
    compileSdk = 35  // Update to latest

    defaultConfig {
        targetSdk = 35  // Update to target
        // minSdk remains unchanged for compatibility
    }
}

// Also update:
// - Android Gradle Plugin to 8.5.0+
// - Kotlin to 2.0.0+
// - AndroidX libraries to latest stable
```

#### 4.2 Foreground Service Migration (SDK 34+)

**Add foreground service types:**

```xml
<!-- AndroidManifest.xml -->

<!-- Before: No type declared -->
<service android:name=".LocationService" />

<!-- After: Type declared -->
<service
    android:name=".LocationService"
    android:foregroundServiceType="location"
    android:exported="false" />

<!-- Common foreground service types: -->
<!-- location, camera, microphone, mediaPlayback, -->
<!-- phoneCall, connectedDevice, mediaProjection, -->
<!-- dataSync, health, remoteMessaging, shortService -->

<!-- Multiple types if needed: -->
<service
    android:name=".MediaService"
    android:foregroundServiceType="mediaPlayback|camera" />
```

**Update service start code:**

```kotlin
// Before: SDK 33
class LocationService : Service() {
    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val notification = createNotification()
        startForeground(NOTIFICATION_ID, notification)
        return START_STICKY
    }
}

// After: SDK 34+
class LocationService : Service() {
    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val notification = createNotification()

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.UPSIDE_DOWN_CAKE) {
            startForeground(
                NOTIFICATION_ID,
                notification,
                ServiceInfo.FOREGROUND_SERVICE_TYPE_LOCATION
            )
        } else {
            startForeground(NOTIFICATION_ID, notification)
        }
        return START_STICKY
    }
}
```

#### 4.3 Broadcast Receiver Export Flag (SDK 34+)

**Update dynamic receiver registration:**

```kotlin
// Before: No export flag
context.registerReceiver(receiver, IntentFilter(ACTION_CUSTOM))

// After: With export flag
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.UPSIDE_DOWN_CAKE) {
    context.registerReceiver(
        receiver,
        IntentFilter(ACTION_CUSTOM),
        Context.RECEIVER_NOT_EXPORTED  // or RECEIVER_EXPORTED if needed
    )
} else {
    context.registerReceiver(receiver, IntentFilter(ACTION_CUSTOM))
}

// For exported receivers that receive broadcasts from other apps:
context.registerReceiver(
    receiver,
    IntentFilter(ACTION_CUSTOM),
    Context.RECEIVER_EXPORTED
)
```

**Update manifest receivers:**

```xml
<!-- AndroidManifest.xml -->

<!-- Explicitly set exported for all receivers -->
<receiver
    android:name=".MyReceiver"
    android:exported="false">
    <intent-filter>
        <action android:name="com.myapp.CUSTOM_ACTION" />
    </intent-filter>
</receiver>

<!-- System broadcast receivers must be exported -->
<receiver
    android:name=".BootReceiver"
    android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.BOOT_COMPLETED" />
    </intent-filter>
</receiver>
```

#### 4.4 Notification Permission (SDK 33+)

**Request POST_NOTIFICATIONS permission:**

```kotlin
// Add to manifest
// <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />

class NotificationPermissionHandler(
    private val activity: ComponentActivity
) {
    private val requestPermissionLauncher = activity.registerForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { isGranted: Boolean ->
        if (isGranted) {
            // Permission granted, notifications will work
        } else {
            // Permission denied, show explanation or disable feature
        }
    }

    fun requestNotificationPermission() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
            when {
                ContextCompat.checkSelfPermission(
                    activity,
                    Manifest.permission.POST_NOTIFICATIONS
                ) == PackageManager.PERMISSION_GRANTED -> {
                    // Already granted
                }
                activity.shouldShowRequestPermissionRationale(
                    Manifest.permission.POST_NOTIFICATIONS
                ) -> {
                    // Show rationale then request
                    showRationaleDialog()
                }
                else -> {
                    requestPermissionLauncher.launch(
                        Manifest.permission.POST_NOTIFICATIONS
                    )
                }
            }
        }
    }
}
```

#### 4.5 Exact Alarm Permission (SDK 34+)

**Handle SCHEDULE_EXACT_ALARM:**

```kotlin
// Check and request exact alarm permission
class AlarmPermissionHandler(private val context: Context) {

    private val alarmManager = context.getSystemService<AlarmManager>()

    fun canScheduleExactAlarms(): Boolean {
        return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
            alarmManager?.canScheduleExactAlarms() == true
        } else {
            true
        }
    }

    fun requestExactAlarmPermission(activity: Activity) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
            if (!canScheduleExactAlarms()) {
                // Direct user to settings
                Intent(Settings.ACTION_REQUEST_SCHEDULE_EXACT_ALARM).also { intent ->
                    intent.data = Uri.parse("package:${context.packageName}")
                    activity.startActivity(intent)
                }
            }
        }
    }

    fun scheduleAlarm(triggerTime: Long, pendingIntent: PendingIntent) {
        if (canScheduleExactAlarms()) {
            alarmManager?.setExactAndAllowWhileIdle(
                AlarmManager.RTC_WAKEUP,
                triggerTime,
                pendingIntent
            )
        } else {
            // Fallback to inexact alarm
            alarmManager?.setAndAllowWhileIdle(
                AlarmManager.RTC_WAKEUP,
                triggerTime,
                pendingIntent
            )
        }
    }
}
```

#### 4.6 Photo Picker Migration (SDK 33+)

**Migrate from storage permission to photo picker:**

```kotlin
// Before: Storage permission approach
private val legacyLauncher = registerForActivityResult(
    ActivityResultContracts.GetContent()
) { uri: Uri? ->
    uri?.let { processImage(it) }
}

fun selectImageLegacy() {
    if (checkPermission(READ_EXTERNAL_STORAGE)) {
        legacyLauncher.launch("image/*")
    } else {
        requestPermission(READ_EXTERNAL_STORAGE)
    }
}

// After: Photo Picker approach (no permission needed!)
private val photoPickerLauncher = registerForActivityResult(
    ActivityResultContracts.PickVisualMedia()
) { uri: Uri? ->
    uri?.let { processImage(it) }
}

fun selectImage() {
    photoPickerLauncher.launch(
        PickVisualMediaRequest(
            ActivityResultContracts.PickVisualMedia.ImageOnly
        )
    )
}

// For multiple selection:
private val multiplePhotoPickerLauncher = registerForActivityResult(
    ActivityResultContracts.PickMultipleVisualMedia(maxItems = 5)
) { uris: List<Uri> ->
    uris.forEach { processImage(it) }
}
```

#### 4.7 PendingIntent Mutability (SDK 31+)

**Add mutability flags:**

```kotlin
// Before: No mutability flag
val pendingIntent = PendingIntent.getActivity(
    context,
    requestCode,
    intent,
    PendingIntent.FLAG_UPDATE_CURRENT
)

// After: With mutability flag
val pendingIntent = PendingIntent.getActivity(
    context,
    requestCode,
    intent,
    PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
)

// Use FLAG_MUTABLE only when required:
// - When using inline reply actions
// - When PendingIntent needs to be modified
val mutablePendingIntent = PendingIntent.getActivity(
    context,
    requestCode,
    intent,
    PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_MUTABLE
)
```

#### 4.8 Predictive Back Gesture (SDK 34+)

**Implement predictive back support:**

```kotlin
// Enable in manifest
// android:enableOnBackInvokedCallback="true"

// In Activity/Fragment - using OnBackPressedCallback
class MyFragment : Fragment() {

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val callback = object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                if (hasUnsavedChanges()) {
                    showDiscardDialog()
                } else {
                    isEnabled = false
                    requireActivity().onBackPressedDispatcher.onBackPressed()
                }
            }
        }

        requireActivity().onBackPressedDispatcher.addCallback(
            viewLifecycleOwner,
            callback
        )
    }
}

// In Compose - using BackHandler
@Composable
fun MyScreen(onNavigateBack: () -> Unit) {
    var hasUnsavedChanges by remember { mutableStateOf(false) }

    BackHandler(enabled = hasUnsavedChanges) {
        // Show confirmation dialog
    }
}
```

#### 4.9 Edge-to-Edge (SDK 35+)

**Implement edge-to-edge display:**

```kotlin
class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Enable edge-to-edge
        WindowCompat.setDecorFitsSystemWindows(window, false)

        setContent {
            MyAppTheme {
                Scaffold(
                    modifier = Modifier
                        .fillMaxSize()
                        .windowInsetsPadding(WindowInsets.systemBars)
                ) { paddingValues ->
                    // Content with proper insets
                    Content(
                        modifier = Modifier.padding(paddingValues)
                    )
                }
            }
        }
    }
}

// Handle insets in Compose
@Composable
fun MyScreen() {
    val insets = WindowInsets.systemBars

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(insets.asPaddingValues())
    ) {
        // Content
    }
}

// For Views - handle insets
ViewCompat.setOnApplyWindowInsetsListener(view) { v, windowInsets ->
    val insets = windowInsets.getInsets(WindowInsetsCompat.Type.systemBars())
    v.setPadding(insets.left, insets.top, insets.right, insets.bottom)
    WindowInsetsCompat.CONSUMED
}
```

---

### Phase 5: Testing & Verification

Comprehensive testing for the SDK upgrade.

#### 5.1 Build Verification

**Verify successful build:**

```bash
# Clean build with new SDK
./gradlew clean build

# Check for API compatibility warnings
./gradlew lint

# Verify no new StrictMode violations
./gradlew connectedAndroidTest
```

#### 5.2 API Level Testing Matrix

**Test across SDK versions:**

| Test Area | API 24 (Min) | API 33 | API 34 | API 35 |
|-----------|--------------|--------|--------|--------|
| App launch | [ ] | [ ] | [ ] | [ ] |
| Permissions | [ ] | [ ] | [ ] | [ ] |
| Background work | [ ] | [ ] | [ ] | [ ] |
| Notifications | [ ] | [ ] | [ ] | [ ] |
| Storage access | [ ] | [ ] | [ ] | [ ] |
| Navigation | [ ] | [ ] | [ ] | [ ] |

#### 5.3 Behavior Change Testing

**Test specific behavior changes:**

```markdown
## SDK 34 Testing Checklist

### Foreground Services
- [ ] All FGS start without SecurityException
- [ ] FGS show correct notification type icon
- [ ] FGS work after app backgrounded

### Broadcasts
- [ ] All receivers receive expected broadcasts
- [ ] No "Background execution not allowed" errors
- [ ] System broadcasts still received

### Notifications
- [ ] POST_NOTIFICATIONS request shown
- [ ] Notifications appear when permission granted
- [ ] Graceful degradation when denied

### Alarms
- [ ] Exact alarms work when permitted
- [ ] Inexact fallback works when not permitted
- [ ] User directed to settings correctly

## SDK 35 Testing Checklist

### Edge-to-Edge
- [ ] Status bar area handled correctly
- [ ] Navigation bar area handled correctly
- [ ] Keyboard insets handled correctly
- [ ] No content cut off by system UI
```

---

## Expected Output

### SDK Upgrade Report

```markdown
# SDK Upgrade Report

## Summary
| Metric | Value |
|--------|-------|
| Previous targetSdk | 33 |
| New targetSdk | 35 |
| Code Changes | 28 files |
| New Permissions | 1 (POST_NOTIFICATIONS) |
| Manifest Changes | 12 components |

## Changes Implemented

### Manifest Updates
- Added foreground service types to 4 services
- Added exported flags to 6 broadcast receivers
- Added POST_NOTIFICATIONS permission

### Code Changes
| Change Type | Files | Description |
|-------------|-------|-------------|
| FGS Types | 4 | Added ServiceInfo.FOREGROUND_SERVICE_TYPE_* |
| Receiver Export | 6 | Added RECEIVER_NOT_EXPORTED flags |
| Notification Permission | 3 | Added runtime permission request |
| Photo Picker | 2 | Migrated from storage permission |
| PendingIntent | 12 | Added FLAG_IMMUTABLE |
| Edge-to-Edge | 5 | Added inset handling |

## Testing Results
| API Level | Status | Notes |
|-----------|--------|-------|
| 24 (Min) | Pass | Full compatibility |
| 33 | Pass | All features work |
| 34 | Pass | New behaviors verified |
| 35 | Pass | Edge-to-edge working |

## Known Issues
- [ ] [Any remaining issues]

## Recommendations
- Monitor crash reports after release
- Consider targeting SDK 35 in next release
```

---

## Example Interaction

**User:** We need to update our app to targetSdk 34 before the Play Store deadline. Our current targetSdk is 31.

**Agent:** I'll help you upgrade from targetSdk 31 to 34. This involves behavior changes from SDK 32, 33, and 34. Let me analyze your codebase.

*[Agent examines manifest, services, and permissions]*

## SDK Upgrade Analysis

### Current Configuration
- compileSdk: 31
- targetSdk: 31
- minSdk: 24

### Behavior Changes to Address

**SDK 32 (Android 12L):**
- No significant changes for your app

**SDK 33 (Android 13):**
- **POST_NOTIFICATIONS permission** - Your app uses FCM, needs runtime permission
- **Granular media permissions** - You use READ_EXTERNAL_STORAGE for images

**SDK 34 (Android 14):**
- **Foreground service types** - Found 2 services: `LocationTrackingService`, `MusicPlaybackService`
- **Broadcast receiver export** - Found 5 dynamically registered receivers
- **PendingIntent mutability** - Found 8 PendingIntents without flags

### Required Changes

| Category | Count | Effort |
|----------|-------|--------|
| Foreground Services | 2 | Medium |
| Broadcast Receivers | 5 | Low |
| Notification Permission | 1 | Medium |
| Media Permission Migration | 1 | Medium |
| PendingIntent Flags | 8 | Low |

### Recommended Approach

1. **Phase 1:** Update build config and fix PendingIntent flags (low risk)
2. **Phase 2:** Add POST_NOTIFICATIONS runtime permission
3. **Phase 3:** Add foreground service types
4. **Phase 4:** Update broadcast receiver registration
5. **Phase 5:** Migrate to photo picker

Shall I start with Phase 1?

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective for SDK upgrades
- **ST-02** (Sequential Instructions): Phased approach through SDK levels
- **RT-02** (Multi-Dimensional Analysis): Permissions, services, UI, storage impacts
- **RT-04** (Best Practice Review): Follows Android upgrade best practices
- **RT-05** (Evidence-Based Reasoning): Specific API references and migration guides
- **ST-03** (Output Format Templates): Structured checklists and matrices
- **OC-05** (Severity Classification): Breaking vs. warning vs. enhancement
- **AG-02** (Skeptical Default Stance): Thorough compatibility verification
- **AG-12** (Quantitative Metrics): SDK levels, change counts, test coverage
- **NE-02** (Phased Workflow): Clear phases with checkpoints
- **NE-07** (Discussion Before Action): User approval before major changes

---

## Related Prompts

- [android_dependency_update.md](android_dependency_update.md) - Update accompanying library dependencies
- [android_sdk_migration.md](android_sdk_migration.md) - Major SDK/platform migrations
- [android_privacy_compliance.md](../publishing/android_privacy_compliance.md) - Permission and privacy requirements
- [android_release_preparation.md](../publishing/android_release_preparation.md) - Pre-release checklist
- [android_code_modernization.md](../improvement/android_code_modernization.md) - Broader modernization

---

## Customization Guide

### For Different SDK Jump Sizes

**Small Jump (1-2 versions):**
- Focus on breaking behavior changes
- Usually quick migration
- Minimal testing matrix

**Large Jump (3+ versions):**
- Address each SDK level systematically
- More comprehensive testing required
- Consider intermediate releases

### For Different App Types

**Background-Heavy Apps:**
- Focus on foreground service types
- Review battery optimization changes
- Test all background processing paths

**Media Apps:**
- Prioritize storage permission migration
- Implement photo/video picker
- Review media codec changes

**Communication Apps:**
- Focus on notification changes
- Review call/SMS permission changes
- Test real-time communication

### For Different Risk Tolerances

**Conservative (Production Critical):**
- Extensive testing on each SDK level
- Beta testing period
- Staged rollout

**Balanced:**
- Core path testing
- Standard release cycle
- Monitor crash rates

**Aggressive (Quick Compliance):**
- Focus on breaking changes only
- Quick verification
- Hotfix plan ready

### By Play Store Deadline

**Months Before Deadline:**
- Full migration with modernization
- Time for thorough testing
- Opportunity for beta feedback

**Weeks Before Deadline:**
- Focus on required changes only
- Prioritize breaking changes
- Plan for quick follow-up release

**At Deadline:**
- Minimum viable changes
- Critical testing only
- Immediate monitoring post-release
