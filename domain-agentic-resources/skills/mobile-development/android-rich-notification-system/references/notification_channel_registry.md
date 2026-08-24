# Notification Channel Registry

## Channel Design Principles

1. **One channel per user-controllable category** — Users should be able to disable "Shopping Alerts" without losing "Calendar Reminders"
2. **Group related channels** — Use NotificationChannelGroup to organize Settings UI
3. **Set appropriate importance** — HIGH for time-sensitive (messages, alarms), DEFAULT for actionable (tasks), LOW for informational (achievements)
4. **Never change existing channel IDs** — Once created, the channel ID is permanent. To change defaults, create a new channel

## Channel Groups

| Group ID | Group Name | Contains |
|----------|------------|----------|
| `communication` | Communication | Messages |
| `reminders` | Reminders & Alerts | Calendar, Tasks, Shopping, Weather, Location |
| `activity` | Activity | Gamification |
| (ungrouped) | — | System |

## Channel Definitions

### messages
- **ID:** `messages`
- **Name:** Messages
- **Importance:** HIGH (heads-up, sound, vibration)
- **Group:** communication
- **Description:** New messages from contacts
- **Badge:** Yes
- **Vibration:** Yes
- **Sound:** Default message tone
- **Use for:** Direct messages, group chat messages, message reactions
- **Style:** MessagingStyle with Person

### calendar_reminders
- **ID:** `calendar_reminders`
- **Name:** Calendar Reminders
- **Importance:** HIGH (heads-up, sound, vibration)
- **Group:** reminders
- **Description:** Upcoming event reminders
- **Badge:** No
- **Vibration:** Yes
- **Sound:** Default notification
- **Use for:** Event reminders (15min/1hr/1day before), event updates, invitation responses
- **Style:** BigTextStyle with event details, Snooze + Dismiss actions

### task_reminders
- **ID:** `task_reminders`
- **Name:** Task Reminders
- **Importance:** DEFAULT (sound, no heads-up)
- **Group:** reminders
- **Description:** Task due date reminders
- **Badge:** No
- **Vibration:** No
- **Sound:** Default notification
- **Use for:** Task due reminders, overdue alerts, recurring task prompts
- **Style:** BigTextStyle, Mark Complete action

### shopping_alerts
- **ID:** `shopping_alerts`
- **Name:** Shopping Alerts
- **Importance:** DEFAULT (sound, no heads-up)
- **Group:** reminders
- **Description:** Shopping list reminders and shared list updates
- **Badge:** No
- **Vibration:** No
- **Sound:** Default notification
- **Use for:** Shared list updates, store proximity alerts, item added by collaborator
- **Style:** InboxStyle for multiple items

### weather_alerts
- **ID:** `weather_alerts`
- **Name:** Weather Alerts
- **Importance:** HIGH (heads-up for severe weather)
- **Group:** reminders
- **Description:** Severe weather warnings
- **Badge:** No
- **Vibration:** Yes
- **Sound:** Default alarm
- **Use for:** Severe weather warnings, daily forecast summary, rain alerts
- **Style:** BigTextStyle with alert details

### location_reminders
- **ID:** `location_reminders`
- **Name:** Location Reminders
- **Importance:** HIGH (heads-up, user requested this alert)
- **Group:** reminders
- **Description:** Reminders triggered by arriving at or leaving a location
- **Badge:** No
- **Vibration:** Yes
- **Sound:** Default notification
- **Use for:** Geofence-triggered reminders, store arrival shopping lists
- **Style:** BigTextStyle with location name and reminder content

### gamification
- **ID:** `gamification`
- **Name:** Achievements
- **Importance:** LOW (no sound, silent)
- **Group:** activity
- **Description:** Achievement unlocks, level ups, and score milestones
- **Badge:** No
- **Vibration:** No
- **Sound:** None
- **Use for:** Achievement unlocks, streak milestones, leaderboard changes
- **Style:** BigPictureStyle with achievement badge image

### system
- **ID:** `system`
- **Name:** System
- **Importance:** LOW (no sound, silent)
- **Group:** (ungrouped)
- **Description:** App updates and system notifications
- **Badge:** No
- **Vibration:** No
- **Sound:** None
- **Use for:** App update available, sync status, background task completion
- **Style:** Standard

## Notification ID Strategy

Use deterministic IDs to enable notification updates and prevent duplicates:

```kotlin
object NotificationIds {
    // Deterministic: same notification replaces itself
    fun forMessage(chatId: String) = "msg_$chatId".hashCode()
    fun forCalendarEvent(eventId: String) = "cal_$eventId".hashCode()
    fun forTask(taskId: String) = "task_$taskId".hashCode()
    fun forWeather(alertId: String) = "weather_$alertId".hashCode()
    fun forLocation(reminderId: String) = "loc_$reminderId".hashCode()
    fun forAchievement(achievementId: String) = "ach_$achievementId".hashCode()

    // Group summary IDs
    const val MESSAGE_GROUP_SUMMARY = 10001
    const val TASK_GROUP_SUMMARY = 10002
}
```
