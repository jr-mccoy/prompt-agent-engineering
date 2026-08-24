# Android 13+ POST_NOTIFICATIONS Permission Handling

## Overview

Starting with Android 13 (API 33), apps must request the `POST_NOTIFICATIONS` runtime permission before showing notifications. Without this permission, all notifications are silently dropped.

## Key Rules

1. **Apps targeting API 33+** must declare and request the permission
2. **Apps targeting API 32 or below** on Android 13 devices get an automatic permission prompt on first notification channel creation
3. **Permission cannot be auto-granted** — the user must explicitly allow it
4. **Once denied permanently**, the user must enable it in Settings

## Manifest Declaration

```xml
<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
```

## When to Request

**Do NOT request on first app launch.** The user has no context for why notifications matter.

**DO request at contextually relevant moments:**

| Trigger | Rationale | Example |
|---------|-----------|---------|
| User sends first message | "Allow notifications to know when you get replies" |
| User creates calendar event with reminder | "Allow notifications for event reminders" |
| User creates location reminder | "Allow notifications for location-based reminders" |
| User enables weather alerts | "Allow notifications for weather warnings" |
| During onboarding (with explanation) | "Stay on top of messages, reminders, and alerts" |

## Implementation

```kotlin
@Composable
fun NotificationPermissionRequest(
    onPermissionResult: (Boolean) -> Unit,
) {
    val context = LocalContext.current

    // Only needed on Android 13+
    if (Build.VERSION.SDK_INT < 33) {
        onPermissionResult(true)
        return
    }

    // Check if already granted
    if (ContextCompat.checkSelfPermission(
            context, Manifest.permission.POST_NOTIFICATIONS
        ) == PackageManager.PERMISSION_GRANTED
    ) {
        onPermissionResult(true)
        return
    }

    val launcher = rememberLauncherForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { granted ->
        onPermissionResult(granted)
    }

    // Show rationale before requesting
    var showRationale by remember { mutableStateOf(true) }

    if (showRationale) {
        NotificationRationaleDialog(
            onConfirm = {
                showRationale = false
                launcher.launch(Manifest.permission.POST_NOTIFICATIONS)
            },
            onDismiss = {
                showRationale = false
                onPermissionResult(false)
            }
        )
    }
}

@Composable
private fun NotificationRationaleDialog(
    onConfirm: () -> Unit,
    onDismiss: () -> Unit,
) {
    AlertDialog(
        onDismissRequest = onDismiss,
        title = { Text("Enable Notifications") },
        text = {
            Text("Get notified about new messages, event reminders, " +
                 "and location-based alerts. You can customize which " +
                 "notifications you receive in Settings.")
        },
        confirmButton = {
            TextButton(onClick = onConfirm) { Text("Enable") }
        },
        dismissButton = {
            TextButton(onClick = onDismiss) { Text("Not Now") }
        }
    )
}
```

## Handling Denial

```kotlin
fun handlePermissionDenied(activity: Activity) {
    if (!activity.shouldShowRequestPermissionRationale(
            Manifest.permission.POST_NOTIFICATIONS
        )
    ) {
        // User selected "Don't ask again" — redirect to Settings
        showSettingsRedirectSnackbar(activity)
    } else {
        // User denied but can be asked again later
        // Show a subtle banner explaining what they'll miss
        showPermissionDeniedBanner()
    }
}

fun showSettingsRedirectSnackbar(activity: Activity) {
    Snackbar.make(
        activity.findViewById(android.R.id.content),
        "Enable notifications in Settings to receive reminders",
        Snackbar.LENGTH_LONG
    ).setAction("Settings") {
        val intent = Intent(Settings.ACTION_APP_NOTIFICATION_SETTINGS).apply {
            putExtra(Settings.EXTRA_APP_PACKAGE, activity.packageName)
        }
        activity.startActivity(intent)
    }.show()
}
```

## Graceful Degradation

When notification permission is denied, the app should still function:

```kotlin
class NotificationService @Inject constructor(
    private val context: Context,
) {
    fun canShowNotifications(): Boolean {
        return if (Build.VERSION.SDK_INT >= 33) {
            ContextCompat.checkSelfPermission(
                context, Manifest.permission.POST_NOTIFICATIONS
            ) == PackageManager.PERMISSION_GRANTED
        } else {
            NotificationManagerCompat.from(context).areNotificationsEnabled()
        }
    }

    fun showNotification(notification: Notification, id: Int) {
        if (!canShowNotifications()) {
            // Fall back to in-app notification (banner, badge, etc.)
            showInAppNotification(notification)
            return
        }
        NotificationManagerCompat.from(context).notify(id, notification)
    }
}
```

## Testing

```kotlin
@Test
fun `notification permission denied - shows in-app fallback`() {
    // Mock permission as denied
    every {
        ContextCompat.checkSelfPermission(any(), POST_NOTIFICATIONS)
    } returns PackageManager.PERMISSION_DENIED

    notificationService.showNotification(testNotification, 1)

    // Verify in-app notification shown instead
    verify { inAppNotificationManager.show(any()) }
    // Verify system notification NOT shown
    verify(exactly = 0) { notificationManager.notify(any(), any()) }
}
```
