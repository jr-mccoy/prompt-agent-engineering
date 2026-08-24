# FCM Message Patterns

## Data Messages vs Notification Messages

| Feature | Data Message | Notification Message |
|---------|-------------|---------------------|
| `onMessageReceived()` called | Always (foreground + background) | Only in foreground |
| Background behavior | Your code handles display | System tray auto-displays |
| Customization | Full control | Limited |
| Max payload | 4KB | 4KB |

**Recommendation:** Always use **data messages** for full control. This ensures your notification channel, style, actions, and grouping logic always runs.

## Sending Data Messages from Cloud Functions

```typescript
// Cloud Function — send data message (NOT notification message)
import { getMessaging } from "firebase-admin/messaging";

export const sendMessageNotification = functions.firestore
  .document("chats/{chatId}/messages/{messageId}")
  .onCreate(async (snapshot, context) => {
    const message = snapshot.data();
    const chatId = context.params.chatId;

    // Get recipient FCM tokens
    const tokens = await getRecipientTokens(chatId, message.senderId);

    // Send data-only message (no "notification" field)
    await getMessaging().sendEachForMulticast({
      tokens,
      data: {
        type: "message",
        chatId: chatId,
        senderName: message.senderName,
        messageText: message.text,
        senderId: message.senderId,
        timestamp: String(message.timestamp),
      },
      android: {
        priority: "high",
        ttl: 86400000, // 24 hours
      },
    });
  });
```

## Topic Subscriptions

Use topics for broadcast notifications (weather, system updates):

```kotlin
// Subscribe to weather alerts for user's location
FirebaseMessaging.getInstance().subscribeToTopic("weather_${cityId}")

// Subscribe to system announcements
FirebaseMessaging.getInstance().subscribeToTopic("system_announcements")

// Unsubscribe
FirebaseMessaging.getInstance().unsubscribeFromTopic("weather_${oldCityId}")
```

**Topic naming convention:**
- `weather_{cityId}` — Weather alerts per city
- `system_announcements` — App-wide announcements
- `gamification_leaderboard_{boardId}` — Leaderboard updates

## Conditional Delivery

Send to devices matching specific conditions:

```typescript
// Send weather alert to users in a specific region
await getMessaging().send({
  condition: "'weather_nyc' in topics || 'weather_nj' in topics",
  data: {
    type: "weather_alert",
    severity: "WARNING",
    headline: "Winter Storm Watch",
    description: "Heavy snow expected...",
  },
});
```

## Message Payload Templates

### Chat Message
```json
{
  "data": {
    "type": "message",
    "chatId": "chat_abc123",
    "senderName": "Alice",
    "senderId": "user_123",
    "messageText": "Hey, are you coming to the meeting?",
    "timestamp": "1706900400000"
  }
}
```

### Calendar Reminder
```json
{
  "data": {
    "type": "calendar_reminder",
    "eventId": "event_xyz",
    "eventTitle": "Team Standup",
    "startTime": "1706904000000",
    "minutesBefore": "15",
    "location": "Conference Room B"
  }
}
```

### Task Reminder
```json
{
  "data": {
    "type": "task_reminder",
    "taskId": "task_456",
    "taskTitle": "Submit expense report",
    "dueDate": "1706990400000",
    "priority": "high"
  }
}
```

### Achievement Unlock
```json
{
  "data": {
    "type": "achievement",
    "achievementId": "ach_streak_7",
    "title": "Week Warrior",
    "description": "7-day activity streak!",
    "imageUrl": "https://example.com/badges/streak_7.png"
  }
}
```

## High Priority vs Normal Priority

| Priority | Wake device? | Battery impact | Use for |
|----------|-------------|----------------|---------|
| **high** | Yes | Higher | Messages, calendar reminders, weather alerts |
| **normal** | No (batched) | Lower | Achievements, shopping updates, system |

Set priority per message type:
```typescript
android: {
  priority: isTimeSensitive ? "high" : "normal",
}
```

## Token Management

```kotlin
class FcmTokenManager @Inject constructor(
    private val firestore: FirebaseFirestore,
    private val auth: FirebaseAuth,
) {
    suspend fun refreshToken() {
        val token = FirebaseMessaging.getInstance().token.await()
        val userId = auth.currentUser?.uid ?: return

        firestore.collection("users").document(userId)
            .update("fcmTokens", FieldValue.arrayUnion(token))
    }

    suspend fun removeToken() {
        val token = FirebaseMessaging.getInstance().token.await()
        val userId = auth.currentUser?.uid ?: return

        firestore.collection("users").document(userId)
            .update("fcmTokens", FieldValue.arrayRemove(token))
    }
}
```
