---
name: android-rich-notification-system
description: Comprehensive Android notification system covering FCM integration, notification channels per feature, rich notifications with actions and media, geofence-triggered location reminders, in-app messaging, and Android 13+ runtime permission handling. Activates when implementing push notifications, local notifications, notification channels, geofence reminders, or handling POST_NOTIFICATIONS permission for apps with messaging, calendars, reminders, and alerts.
metadata:
  tags:
    - android
    - mobile
    - notification
    - rich
    - system
  updated: "2026-04-11"
---
# Android Rich Notification System

Complete notification architecture for feature-rich Android apps. Covers FCM cloud messaging, local notifications, channel organization, rich notification layouts, geofence-based location reminders, and the Android 13+ notification permission model.

## Purpose

Apps with multiple notification-producing features (messaging, calendars, tasks, shopping, weather, reminders) need a unified notification architecture. This skill provides patterns for organizing notification channels, building rich notification layouts, integrating FCM for cloud-triggered notifications, implementing geofence-based reminders, and handling the Android 13+ POST_NOTIFICATIONS runtime permission.

## When to Use This Skill

Use this skill when you need to:
- Set up notification channels for a multi-feature Android app
- Implement FCM for push notifications with data and notification messages
- Build rich notifications with actions, images, progress bars, or custom layouts
- Implement location-based reminders using geofencing
- Handle POST_NOTIFICATIONS permission for Android 13+ (API 33+)
- Coordinate notifications from multiple features into a coherent user experience
- Implement in-app messaging alongside push notifications

## When NOT to Use This Skill

Do NOT use this skill when:
- App has only one type of notification (use standard NotificationCompat)
- Need Firebase configuration validation (use android-firebase-sync-validator)
- Building notification UI in Compose (use jetpack-compose-patterns)
- Need backend Cloud Functions for notifications (use Cloud Functions documentation)

## Quick Start

1. **Define channels** — One per feature category (see channel registry)
2. **Request permission** — POST_NOTIFICATIONS for Android 13+
3. **Set up FCM** — FirebaseMessagingService for cloud push
4. **Build notifications** — NotificationCompat with appropriate style
5. **Add geofencing** — GeofencingClient for location reminders

## Step 1: Define Notification Channel Registry

Create all channels at app startup. See `references/notification_channel_registry.md` for the complete registry.

```kotlin
object NotificationChannels {
    // Channel IDs — one per notification category
    const val MESSAGES = "messages"
    const val CALENDAR_REMINDERS = "calendar_reminders"
    const val TASK_REMINDERS = "task_reminders"
    const val SHOPPING_ALERTS = "shopping_alerts"
    const val WEATHER_ALERTS = "weather_alerts"
    const val LOCATION_REMINDERS = "location_reminders"
    const val GAMIFICATION = "gamification"
    const val SYSTEM = "system"

    fun createAll(context: Context) {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.O) return

        val manager = context.getSystemService(NotificationManager::class.java)

        // Group channels for Settings UI
        manager.createNotificationChannelGroup(
            NotificationChannelGroup("communication", "Communication")
        )
        manager.createNotificationChannelGroup(
            NotificationChannelGroup("reminders", "Reminders & Alerts")
        )
        manager.createNotificationChannelGroup(
            NotificationChannelGroup("activity", "Activity")
        )

        manager.createNotificationChannels(listOf(
            NotificationChannel(MESSAGES, "Messages", IMPORTANCE_HIGH).apply {
                group = "communication"
                description = "New messages from contacts"
                enableVibration(true)
                setShowBadge(true)
            },
            NotificationChannel(CALENDAR_REMINDERS, "Calendar Reminders", IMPORTANCE_HIGH).apply {
                group = "reminders"
                description = "Upcoming event reminders"
                enableVibration(true)
            },
            NotificationChannel(TASK_REMINDERS, "Task Reminders", IMPORTANCE_DEFAULT).apply {
                group = "reminders"
                description = "Task due date reminders"
            },
            NotificationChannel(SHOPPING_ALERTS, "Shopping Alerts", IMPORTANCE_DEFAULT).apply {
                group = "reminders"
                description = "Shopping list reminders and deals"
            },
            NotificationChannel(WEATHER_ALERTS, "Weather Alerts", IMPORTANCE_HIGH).apply {
                group = "reminders"
                description = "Severe weather warnings"
            },
            NotificationChannel(LOCATION_REMINDERS, "Location Reminders", IMPORTANCE_HIGH).apply {
                group = "reminders"
                description = "Reminders triggered by arriving at a location"
                enableVibration(true)
            },
            NotificationChannel(GAMIFICATION, "Achievements", IMPORTANCE_LOW).apply {
                group = "activity"
                description = "Achievement unlocks and score updates"
            },
            NotificationChannel(SYSTEM, "System", IMPORTANCE_LOW).apply {
                description = "App updates and system notifications"
            },
        ))
    }
}
```

Call `NotificationChannels.createAll(this)` in `Application.onCreate()`.

## Step 2: Handle POST_NOTIFICATIONS Permission (Android 13+)

```kotlin
class NotificationPermissionHandler @Inject constructor(
    private val preferences: DataStore<Preferences>,
) {
    private val PERMISSION = Manifest.permission.POST_NOTIFICATIONS
    private val ASKED_KEY = booleanPreferencesKey("notification_permission_asked")

    fun shouldRequestPermission(context: Context): Boolean {
        if (Build.VERSION.SDK_INT < 33) return false
        return ContextCompat.checkSelfPermission(context, PERMISSION) !=
            PackageManager.PERMISSION_GRANTED
    }

    /**
     * Request at a contextually appropriate moment:
     * - After user sends first message (for messaging notifications)
     * - After user creates first calendar event (for reminders)
     * - After onboarding explains notification value
     *
     * Do NOT request on first app launch with no context.
     */
    suspend fun requestPermission(
        activity: ComponentActivity,
        launcher: ActivityResultLauncher<String>,
    ) {
        if (!shouldRequestPermission(activity)) return

        val hasAsked = preferences.data.first()[ASKED_KEY] ?: false
        if (hasAsked && !activity.shouldShowRequestPermissionRationale(PERMISSION)) {
            // User denied permanently — show settings redirect
            return
        }

        launcher.launch(PERMISSION)
        preferences.edit { it[ASKED_KEY] = true }
    }
}
```

## Step 3: Set Up FCM

See `references/fcm_message_patterns.md` for data vs notification message patterns.

```kotlin
class AppFirebaseMessagingService : FirebaseMessagingService() {

    override fun onNewToken(token: String) {
        // Send token to your server for targeted push
        CoroutineScope(Dispatchers.IO).launch {
            uploadTokenToFirestore(token)
        }
    }

    override fun onMessageReceived(message: RemoteMessage) {
        val data = message.data

        when (data["type"]) {
            "message" -> showMessageNotification(data)
            "calendar_reminder" -> showCalendarNotification(data)
            "task_reminder" -> showTaskNotification(data)
            "weather_alert" -> showWeatherNotification(data)
            "achievement" -> showAchievementNotification(data)
            else -> {
                // Fallback: show notification message payload if present
                message.notification?.let { showGenericNotification(it) }
            }
        }
    }

    private fun showMessageNotification(data: Map<String, String>) {
        val senderName = data["senderName"] ?: return
        val messageText = data["messageText"] ?: return
        val chatId = data["chatId"] ?: return

        val notification = NotificationCompat.Builder(this, NotificationChannels.MESSAGES)
            .setSmallIcon(R.drawable.ic_message)
            .setContentTitle(senderName)
            .setContentText(messageText)
            .setStyle(NotificationCompat.MessagingStyle(selfPerson)
                .addMessage(messageText, System.currentTimeMillis(), Person.Builder()
                    .setName(senderName)
                    .build()))
            .setContentIntent(createChatPendingIntent(chatId))
            .addAction(createReplyAction(chatId))
            .setAutoCancel(true)
            .setCategory(NotificationCompat.CATEGORY_MESSAGE)
            .build()

        NotificationManagerCompat.from(this).notify(chatId.hashCode(), notification)
    }
}
```

## Step 4: Build Rich Notifications

### Message Notification with Direct Reply

```kotlin
private fun createReplyAction(chatId: String): NotificationCompat.Action {
    val remoteInput = RemoteInput.Builder("reply_text")
        .setLabel("Reply")
        .build()

    val replyIntent = PendingIntent.getBroadcast(
        this, chatId.hashCode(),
        Intent(this, ReplyReceiver::class.java).putExtra("chatId", chatId),
        PendingIntent.FLAG_MUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
    )

    return NotificationCompat.Action.Builder(
        R.drawable.ic_reply, "Reply", replyIntent
    ).addRemoteInput(remoteInput).build()
}
```

### Calendar Notification with Actions

```kotlin
fun showCalendarNotification(event: CalendarEvent) {
    val notification = NotificationCompat.Builder(this, NotificationChannels.CALENDAR_REMINDERS)
        .setSmallIcon(R.drawable.ic_calendar)
        .setContentTitle(event.title)
        .setContentText("In ${event.minutesUntil} minutes")
        .setWhen(event.startTime)
        .setShowWhen(true)
        .addAction(R.drawable.ic_snooze, "Snooze 10min", createSnoozePendingIntent(event.id))
        .addAction(R.drawable.ic_dismiss, "Dismiss", createDismissPendingIntent(event.id))
        .setContentIntent(createEventDetailPendingIntent(event.id))
        .setAutoCancel(true)
        .setCategory(NotificationCompat.CATEGORY_REMINDER)
        .build()

    NotificationManagerCompat.from(this).notify(event.id.hashCode(), notification)
}
```

### Weather Alert with Big Text

```kotlin
fun showWeatherAlert(alert: WeatherAlert) {
    val notification = NotificationCompat.Builder(this, NotificationChannels.WEATHER_ALERTS)
        .setSmallIcon(R.drawable.ic_weather_alert)
        .setContentTitle("${alert.severity}: ${alert.headline}")
        .setContentText(alert.description)
        .setStyle(NotificationCompat.BigTextStyle()
            .bigText(alert.description)
            .setSummaryText(alert.area))
        .setPriority(NotificationCompat.PRIORITY_HIGH)
        .setCategory(NotificationCompat.CATEGORY_ALARM)
        .build()

    NotificationManagerCompat.from(this).notify(alert.id.hashCode(), notification)
}
```

## Step 5: Implement Geofence Location Reminders

```kotlin
class GeofenceReminderManager @Inject constructor(
    private val context: Context,
    private val geofencingClient: GeofencingClient,
) {
    fun addLocationReminder(reminder: LocationReminder) {
        val geofence = Geofence.Builder()
            .setRequestId(reminder.id)
            .setCircularRegion(reminder.latitude, reminder.longitude, reminder.radiusMeters)
            .setExpirationDuration(Geofence.NEVER_EXPIRE)
            .setTransitionTypes(
                when (reminder.trigger) {
                    TriggerType.ON_ARRIVAL -> Geofence.GEOFENCE_TRANSITION_ENTER
                    TriggerType.ON_DEPARTURE -> Geofence.GEOFENCE_TRANSITION_EXIT
                    TriggerType.BOTH -> Geofence.GEOFENCE_TRANSITION_ENTER or
                        Geofence.GEOFENCE_TRANSITION_EXIT
                }
            )
            .build()

        val request = GeofencingRequest.Builder()
            .setInitialTrigger(GeofencingRequest.INITIAL_TRIGGER_ENTER)
            .addGeofence(geofence)
            .build()

        val pendingIntent = PendingIntent.getBroadcast(
            context, reminder.id.hashCode(),
            Intent(context, GeofenceBroadcastReceiver::class.java),
            PendingIntent.FLAG_MUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
        )

        geofencingClient.addGeofences(request, pendingIntent)
    }
}

class GeofenceBroadcastReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        val event = GeofencingEvent.fromIntent(intent) ?: return
        if (event.hasError()) return

        val reminderId = event.triggeringGeofences?.firstOrNull()?.requestId ?: return

        // Look up reminder details from Room and show notification
        CoroutineScope(Dispatchers.IO).launch {
            val reminder = reminderDao.getById(reminderId) ?: return@launch
            showLocationReminderNotification(context, reminder)
        }
    }
}
```

**Required permissions:**
```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

Request `ACCESS_BACKGROUND_LOCATION` separately after `ACCESS_FINE_LOCATION` is granted. Show rationale explaining why background location is needed for geofence reminders.

## Step 6: Notification Grouping

For apps that may produce many notifications, group them:

```kotlin
// Group messages by conversation
val GROUP_MESSAGES = "group_messages"

fun showGroupedMessageNotification(messages: List<MessageNotification>) {
    messages.forEach { msg ->
        val notification = NotificationCompat.Builder(this, NotificationChannels.MESSAGES)
            .setSmallIcon(R.drawable.ic_message)
            .setContentTitle(msg.senderName)
            .setContentText(msg.text)
            .setGroup(GROUP_MESSAGES)
            .build()
        NotificationManagerCompat.from(this).notify(msg.id.hashCode(), notification)
    }

    // Summary notification
    val summary = NotificationCompat.Builder(this, NotificationChannels.MESSAGES)
        .setSmallIcon(R.drawable.ic_message)
        .setContentTitle("${messages.size} new messages")
        .setStyle(NotificationCompat.InboxStyle()
            .also { style -> messages.forEach { style.addLine("${it.senderName}: ${it.text}") } }
            .setSummaryText("${messages.size} new messages"))
        .setGroup(GROUP_MESSAGES)
        .setGroupSummary(true)
        .build()
    NotificationManagerCompat.from(this).notify(GROUP_MESSAGES.hashCode(), summary)
}
```

## Common Issues

### Notifications Not Showing on Android 13+
POST_NOTIFICATIONS permission must be granted. The app must target API 33+ and request the permission at runtime. Notifications sent before permission is granted are silently dropped.

### Geofences Lost After Reboot
Geofences are cleared on device reboot. Register a `BOOT_COMPLETED` receiver to re-register all active geofences from Room on startup.

### FCM Data Messages Not Received in Background
Use data messages (not notification messages) to ensure `onMessageReceived()` is always called. Notification messages are handled by the system tray when the app is backgrounded.

### Channel Importance Cannot Be Changed After Creation
Once a channel is created, the user controls its importance. If you need to change default importance, create a new channel with a new ID and delete the old one.

## Resources

### references/notification_channel_registry.md
Complete channel definitions with IDs, importance levels, grouping, and behavioral configuration.

### references/fcm_message_patterns.md
Data vs notification messages, topic subscriptions, conditional delivery, and message payload patterns.

### references/android13_permission_handling.md
Complete guide to POST_NOTIFICATIONS runtime permission handling with contextual request strategies.

## Related Skills

- `android-firebase-sync-validator` — Validates FCM and Cloud Functions configuration
- `android-multi-source-data-layer` — Data layer patterns that support notification triggers
- `jetpack-compose-patterns` — Building notification permission request UI in Compose
