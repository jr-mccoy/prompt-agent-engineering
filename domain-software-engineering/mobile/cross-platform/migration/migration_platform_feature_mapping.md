---
title: "Platform Feature API Mapping"
category: mobile-development
description: "Feature-by-feature API mapping between Android and iOS covering permissions, background processing, notifications, storage, and system services"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-02
difficulty: intermediate
tags:
  - ios
  - android
  - migration
  - api-mapping
  - platform-services
  - permissions
  - notifications
updated: "2026-03-19"
---

# Platform Feature API Mapping

**Objective:** Provide a comprehensive, API-level mapping between Android and iOS platform features. For each feature area — permissions, background processing, notifications, storage, and system services — document the Android API, its iOS equivalent, behavioral differences, and migration code patterns.

**When to Use:** During the implementation phase of an Android-to-iOS migration when developers need concrete API mappings to translate Android features to their iOS counterparts. This prompt bridges the gap between high-level strategy and line-by-line code conversion.

**Prompt Type:** Comprehensive (~380 lines)

## Context Gathering

1. Which platform features does your Android app use? (permissions, background tasks, notifications, storage, sensors, camera, location, etc.)
2. What is the minimum Android API level and target iOS version?
3. Are there any Google-specific services (GMS) that need Apple equivalents?
4. Does the app use any hardware features (Bluetooth, NFC, biometrics)?
5. What notification patterns are used? (foreground, background, silent, rich)
6. What storage mechanisms are used? (SharedPreferences, DataStore, Room, file system)
7. Are there any custom ContentProviders or BroadcastReceivers?
8. Does the app use any Accessibility services?

## Instructions

### CRITICAL: Verification Requirements

- Every API mapping MUST reference specific framework and class names on both platforms
- Behavioral differences MUST be explicitly called out, especially where Android is more permissive
- iOS-specific restrictions (e.g., background execution limits) MUST be documented
- Code examples MUST compile on their respective platforms

### False-Positive Prevention

- ❌ DO NOT assume Android runtime permissions map 1:1 to iOS permission prompts
- ✅ DO document that iOS permissions cannot be re-requested after denial (must direct to Settings)
- ❌ DO NOT assume Android background services have iOS equivalents
- ✅ DO explain iOS background execution modes and their strict limitations
- ❌ DO NOT assume notification channels map to iOS notification categories
- ✅ DO clarify the different grouping and customization models
- ❌ DO NOT assume file system access patterns are identical
- ✅ DO document sandboxing differences and App Group containers

### Step 1: Permissions Mapping

**Kotlin (Android runtime permissions):**
```kotlin
// Android: Request camera permission
class CameraFragment : Fragment() {
    private val permissionLauncher = registerForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { isGranted ->
        if (isGranted) {
            openCamera()
        } else {
            showPermissionDeniedMessage()
        }
    }

    fun requestCamera() {
        when {
            ContextCompat.checkSelfPermission(
                requireContext(), Manifest.permission.CAMERA
            ) == PackageManager.PERMISSION_GRANTED -> openCamera()

            shouldShowRequestPermissionRationale(
                Manifest.permission.CAMERA
            ) -> showRationale()

            else -> permissionLauncher.launch(Manifest.permission.CAMERA)
        }
    }
}
```

**Swift (iOS permission request):**
```swift
// iOS: Request camera permission
import AVFoundation

class CameraManager {
    func requestCameraAccess() async -> Bool {
        let status = AVCaptureDevice.authorizationStatus(for: .video)

        switch status {
        case .authorized:
            return true
        case .notDetermined:
            return await AVCaptureDevice.requestAccess(for: .video)
        case .denied, .restricted:
            // iOS cannot re-prompt — must direct user to Settings
            await openAppSettings()
            return false
        @unknown default:
            return false
        }
    }

    private func openAppSettings() async {
        guard let url = URL(string: UIApplication.openSettingsURLString) else { return }
        await UIApplication.shared.open(url)
    }
}
```

> **Key Difference:** Android allows re-requesting permissions; iOS shows the system prompt only once. After denial, iOS requires the user to manually enable in Settings.

### Step 2: Background Processing Mapping

| Android API | iOS Equivalent | Behavioral Difference |
|-------------|---------------|----------------------|
| `WorkManager` (periodic) | `BGAppRefreshTask` | iOS timing is advisory, not guaranteed |
| `WorkManager` (one-time) | `BGProcessingTask` | iOS grants ~30s for refresh, minutes for processing |
| `ForegroundService` | `beginBackgroundTask` | iOS gives ~30s after backgrounding |
| `AlarmManager` (exact) | No direct equivalent | Use `UNNotificationRequest` for time-based triggers |
| `JobScheduler` | `BGTaskScheduler` | Similar concept, stricter iOS limits |
| Bound Service | No equivalent | Use app extensions or shared containers |

**Kotlin (Android foreground service):**
```kotlin
class LocationTrackingService : Service() {
    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val notification = createNotification()
        startForeground(NOTIFICATION_ID, notification)
        startLocationUpdates()
        return START_STICKY
    }
}
```

**Swift (iOS continuous location — background mode):**
```swift
// iOS: Continuous location requires Background Modes capability
import CoreLocation

class LocationTracker: NSObject, CLLocationManagerDelegate {
    private let manager = CLLocationManager()

    func startTracking() {
        manager.delegate = self
        manager.allowsBackgroundLocationUpdates = true
        manager.showsBackgroundLocationIndicator = true
        manager.requestAlwaysAuthorization()
        manager.startUpdatingLocation()
    }

    func locationManager(
        _ manager: CLLocationManager,
        didUpdateLocations locations: [CLLocation]
    ) {
        guard let location = locations.last else { return }
        processLocation(location)
    }
}
```

> **Key Difference:** Android foreground services can run indefinitely with a notification. iOS background location requires specific entitlement and shows a blue indicator bar.

### Step 3: Notifications Mapping

**Kotlin (Android notification with channel):**
```kotlin
// Android: Create channel + send notification
val channel = NotificationChannel(
    "messages", "Messages", NotificationManager.IMPORTANCE_HIGH
).apply {
    description = "New message notifications"
    enableLights(true)
    lightColor = Color.BLUE
}
notificationManager.createNotificationChannel(channel)

val notification = NotificationCompat.Builder(context, "messages")
    .setSmallIcon(R.drawable.ic_message)
    .setContentTitle("New Message")
    .setContentText("Alice: Hey, are you free?")
    .setCategory(NotificationCompat.CATEGORY_MESSAGE)
    .addAction(R.drawable.ic_reply, "Reply", replyPendingIntent)
    .setStyle(NotificationCompat.MessagingStyle(person)
        .addMessage("Hey, are you free?", timestamp, alice))
    .build()
```

**Swift (iOS notification with category):**
```swift
// iOS: Register category + schedule notification
import UserNotifications

func setupNotifications() {
    let replyAction = UNNotificationAction(
        identifier: "REPLY",
        title: "Reply",
        options: [.authenticationRequired]
    )
    let category = UNNotificationCategory(
        identifier: "MESSAGES",
        actions: [replyAction],
        intentIdentifiers: [],
        options: [.customDismissAction]
    )
    UNUserNotificationCenter.current()
        .setNotificationCategories([category])

    let content = UNMutableNotificationContent()
    content.title = "New Message"
    content.body = "Alice: Hey, are you free?"
    content.categoryIdentifier = "MESSAGES"
    content.sound = .default

    let request = UNNotificationRequest(
        identifier: UUID().uuidString,
        content: content,
        trigger: nil // Deliver immediately
    )
    UNUserNotificationCenter.current().add(request)
}
```

### Step 4: Storage Mapping

| Android Storage | iOS Equivalent | Notes |
|----------------|----------------|-------|
| `SharedPreferences` | `UserDefaults` | Similar key-value API |
| `DataStore` (preferences) | `UserDefaults` + property wrappers | See `migration_datastore_to_userdefaults.md` |
| `DataStore` (proto) | `Codable` + file storage | Custom serialization |
| `Room` | `Core Data` / `SwiftData` | See `migration_room_to_core_data.md` |
| `EncryptedSharedPreferences` | `Keychain Services` | Different API surface |
| Internal storage (`filesDir`) | `FileManager` documents directory | Both sandboxed |
| External storage | No equivalent | iOS has no shared file system |
| `ContentProvider` | App Groups + shared container | For inter-app data sharing |

**Kotlin (Android internal file storage):**
```kotlin
// Android: Write to internal storage
val file = File(context.filesDir, "data.json")
file.writeText(json)

// Read
val content = File(context.filesDir, "data.json").readText()
```

**Swift (iOS file storage):**
```swift
// iOS: Write to documents directory
let documentsURL = FileManager.default.urls(
    for: .documentDirectory, in: .userDomainMask
).first!
let fileURL = documentsURL.appendingPathComponent("data.json")

try json.write(to: fileURL, atomically: true, encoding: .utf8)

// Read
let content = try String(contentsOf: fileURL, encoding: .utf8)
```

### Step 5: System Services Mapping

| Android Service | iOS Equivalent | API Mapping |
|----------------|----------------|-------------|
| `ConnectivityManager` | `NWPathMonitor` | Network state monitoring |
| `LocationManager` | `CLLocationManager` | Similar delegate pattern |
| `SensorManager` | `CMMotionManager` | Accelerometer, gyroscope |
| `BiometricPrompt` | `LAContext` | Face ID / Touch ID |
| `ClipboardManager` | `UIPasteboard` | Copy/paste |
| `PackageManager` | `UIApplication.canOpenURL` | App availability check |
| `AlarmManager` | `UNUserNotificationCenter` | Scheduled triggers |
| `DownloadManager` | `URLSessionDownloadTask` | Background downloads |

**Kotlin (Android biometric authentication):**
```kotlin
val biometricPrompt = BiometricPrompt(
    this,
    ContextCompat.getMainExecutor(this),
    object : BiometricPrompt.AuthenticationCallback() {
        override fun onAuthenticationSucceeded(result: AuthenticationResult) {
            unlockContent()
        }
        override fun onAuthenticationError(errorCode: Int, errString: CharSequence) {
            showError(errString.toString())
        }
    }
)
val promptInfo = BiometricPrompt.PromptInfo.Builder()
    .setTitle("Authenticate")
    .setSubtitle("Use biometrics to access your account")
    .setNegativeBButtonText("Use Password")
    .build()
biometricPrompt.authenticate(promptInfo)
```

**Swift (iOS biometric authentication):**
```swift
import LocalAuthentication

func authenticateWithBiometrics() async throws -> Bool {
    let context = LAContext()
    var error: NSError?

    guard context.canEvaluatePolicy(
        .deviceOwnerAuthenticationWithBiometrics,
        error: &error
    ) else {
        throw AuthError.biometricsUnavailable
    }

    return try await context.evaluatePolicy(
        .deviceOwnerAuthenticationWithBiometrics,
        localizedReason: "Use biometrics to access your account"
    )
}
```

## Expected Output

1. **Complete API mapping table** for all platform features used by the Android app
2. **Side-by-side code examples** for each critical feature migration
3. **Behavioral difference documentation** highlighting where iOS is more restrictive
4. **Migration checklist** with verification steps for each feature area

## Example Interaction

**User:** Our Android app uses runtime permissions (camera, location, contacts), WorkManager for background sync, FCM notifications, Room for offline storage, and BiometricPrompt.

**Assistant:**

### Migration Map

| Feature | Android | iOS | Effort | Risk |
|---------|---------|-----|--------|------|
| Camera permission | `ActivityResultContracts` | `AVCaptureDevice.requestAccess` | S | Low |
| Location permission | `FusedLocationProvider` | `CLLocationManager` | M | Medium — always vs. when-in-use |
| Contacts permission | `ContentResolver` | `CNContactStore` | M | Medium — different data model |
| Background sync | `WorkManager` | `BGAppRefreshTask` | L | High — iOS timing not guaranteed |
| Push notifications | FCM | APNs (or FCM on iOS) | M | Low |
| Offline storage | Room | SwiftData | XL | Medium — see migration guide |
| Biometrics | `BiometricPrompt` | `LAContext` | S | Low |

## Techniques Used

| Technique | Application |
|-----------|-------------|
| **ST-01: Structured Task Decomposition** | Organizing mapping by feature area |
| **ST-02: Systematic Analysis Framework** | Exhaustive API comparison tables |
| **RT-02: Contextual Reference Integration** | Platform-specific API documentation references |
| **DS-02: Output Specification Framework** | Mapping tables, code examples, checklist deliverables |

## Related Prompts

- `migration_android_to_ios_strategy.md` — High-level migration strategy
- `migration_room_to_core_data.md` — Deep dive on database migration
- `migration_firebase_to_apple_services.md` — Firebase service equivalents
- `migration_coroutines_to_swift_concurrency.md` — Async pattern mapping

## Customization Guide

- **Subset Mapping:** If only migrating specific features, filter the mapping tables to relevant areas.
- **Hybrid Approach:** For KMP-shared features (networking, models), the mapping applies only to platform-specific layers.
- **Older iOS Targets:** If targeting iOS 15 or earlier, substitute SwiftData references with Core Data.
- **Wear OS / watchOS:** Extend the mapping to include wearable platform equivalents if the app has a companion watch app.
