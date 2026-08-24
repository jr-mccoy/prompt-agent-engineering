---
title: "iOS Push Notifications Implementation"
category: mobile-development
description: "Implement production-ready APNs push notifications with permission handling, UNUserNotificationCenter, remote/local notifications, notification service extensions, rich notifications, notification actions, and silent push."
techniques:
  - ST-01
  - ST-02
  - ST-03
difficulty: intermediate
tags:
  - ios
  - swift
  - push-notifications
  - apns
  - mobile-development
updated: "2026-03-20"
---

# iOS Push Notifications Implementation

**Objective:** Implement a complete push notification system for an iOS app covering APNs registration, permission handling, UNUserNotificationCenter delegation, remote and local notifications, notification service extensions for rich content, notification actions, and silent push for background data sync.

**When to Use:** Use this prompt when adding push notification support to an iOS app, upgrading from legacy notification handling, or implementing advanced notification features like rich media, grouped notifications, or silent background updates. Best used after the app's data layer and authentication are in place.

**Prompt Type:** Modular (150-400 lines)

---

## Context Gathering

Before implementing notifications, gather essential context:

1. **Notification Requirements:**
   - "What types of notifications does the app send (marketing, transactional, real-time alerts)?"
   - "Do you need rich notifications (images, video, custom UI)?"
   - "Are notification actions required (reply, approve, dismiss)?"

2. **Backend Integration:**
   - "What push notification service is used (APNs directly, Firebase Cloud Messaging, OneSignal, Amazon SNS)?"
   - "Is the device token registration endpoint already defined?"
   - "Do you need topic-based or token-based APNs authentication?"

3. **Existing Setup:**
   - "Is the Push Notification capability already added in Xcode?"
   - "Are there existing UNUserNotificationCenterDelegate implementations?"
   - "What iOS deployment target is set (affects API availability)?"

4. **Silent Push & Background:**
   - "Do you need silent push for background data refresh?"
   - "Is the Background Modes capability enabled for remote notifications?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before implementing ANY code, you MUST:**

1. **Verify entitlements** - Confirm the Push Notifications capability is added in the Xcode project and the provisioning profile includes the `aps-environment` entitlement.
2. **Check existing notification code** - Search for existing `UNUserNotificationCenterDelegate`, `didRegisterForRemoteNotificationsWithDeviceToken`, and notification registration logic.
3. **Confirm backend contract** - Understand the expected device token format (hex string vs raw Data) and registration API.
4. **Follow project conventions** - Match existing error handling, logging, and dependency injection patterns.
5. **Provide specific, working code** - All code samples MUST include file paths and be copy-paste ready.

### False-Positive Prevention

- Do NOT request notification permissions at app launch without user context; use a pre-permission screen
- Do NOT ignore the `notDetermined` authorization status; always handle all cases
- Do NOT store device tokens as raw Data; convert to hex string for backend transmission
- Do NOT assume APNs registration succeeds; handle `didFailToRegisterForRemoteNotificationsWithError`
- Do NOT process notification payloads without validating expected keys
- DO set `UNUserNotificationCenter.current().delegate` before `application(_:didFinishLaunchingWithOptions:)` returns
- DO handle both foreground and background notification delivery
- DO support notification grouping with `threadIdentifier`
- DO implement proper token refresh handling

---

### Phase 1: APNs Registration & Permission Handling

#### 1.1 Notification Permission Manager

```swift
// File: Services/Notifications/NotificationPermissionManager.swift

import UserNotifications
import UIKit

@Observable
final class NotificationPermissionManager {
    enum PermissionState: Equatable {
        case notDetermined
        case authorized
        case denied
        case provisional
        case ephemeral
    }

    private(set) var permissionState: PermissionState = .notDetermined

    func checkCurrentStatus() async {
        let settings = await UNUserNotificationCenter.current().notificationSettings()
        await MainActor.run {
            permissionState = mapAuthorizationStatus(settings.authorizationStatus)
        }
    }

    func requestPermission(options: UNAuthorizationOptions = [.alert, .badge, .sound]) async throws -> Bool {
        let granted = try await UNUserNotificationCenter.current().requestAuthorization(options: options)
        await checkCurrentStatus()

        if granted {
            await MainActor.run {
                UIApplication.shared.registerForRemoteNotifications()
            }
        }
        return granted
    }

    func requestProvisionalPermission() async throws -> Bool {
        let granted = try await UNUserNotificationCenter.current()
            .requestAuthorization(options: [.alert, .badge, .sound, .provisional])
        await checkCurrentStatus()

        if granted {
            await MainActor.run {
                UIApplication.shared.registerForRemoteNotifications()
            }
        }
        return granted
    }

    private func mapAuthorizationStatus(_ status: UNAuthorizationStatus) -> PermissionState {
        switch status {
        case .notDetermined: return .notDetermined
        case .denied: return .denied
        case .authorized: return .authorized
        case .provisional: return .provisional
        case .ephemeral: return .ephemeral
        @unknown default: return .notDetermined
        }
    }
}
```

#### 1.2 Device Token Registration

```swift
// File: Services/Notifications/DeviceTokenManager.swift

import Foundation

final class DeviceTokenManager {
    private let apiClient: APIClientProtocol
    private let tokenStorage: UserDefaults

    init(apiClient: APIClientProtocol, tokenStorage: UserDefaults = .standard) {
        self.apiClient = apiClient
        self.tokenStorage = tokenStorage
    }

    func registerToken(_ deviceToken: Data) async throws {
        let tokenString = deviceToken.map { String(format: "%02.2hhx", $0) }.joined()

        // Avoid redundant registration
        guard tokenString != tokenStorage.string(forKey: "apns_device_token") else { return }

        try await apiClient.registerDeviceToken(tokenString)
        tokenStorage.set(tokenString, forKey: "apns_device_token")
    }

    func clearToken() async throws {
        guard let token = tokenStorage.string(forKey: "apns_device_token") else { return }
        try await apiClient.unregisterDeviceToken(token)
        tokenStorage.removeObject(forKey: "apns_device_token")
    }
}
```

---

### Phase 2: UNUserNotificationCenter Delegate

**CHECKPOINT 1:** Confirm APNs registration and permission flow before proceeding.

```markdown
## Registration Summary

| Component | Status |
|-----------|--------|
| Push Notification capability | Added to Xcode |
| Permission manager | Handles all UNAuthorizationStatus cases |
| Device token conversion | Data -> hex string |
| Token registration | Deduplicated, backend synced |

**Proceed with notification handling?**
```

#### 2.1 Notification Handler

```swift
// File: Services/Notifications/NotificationHandler.swift

import UserNotifications
import UIKit

final class NotificationHandler: NSObject, UNUserNotificationCenterDelegate {
    private let router: NotificationRouterProtocol
    private let analyticsTracker: AnalyticsTrackerProtocol

    init(router: NotificationRouterProtocol, analyticsTracker: AnalyticsTrackerProtocol) {
        self.router = router
        self.analyticsTracker = analyticsTracker
    }

    // MARK: - Foreground Delivery
    func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        willPresent notification: UNNotification
    ) async -> UNNotificationPresentationOptions {
        let userInfo = notification.request.content.userInfo
        analyticsTracker.trackNotificationReceived(userInfo: userInfo, state: .foreground)

        // Show banner even when app is in foreground
        return [.banner, .badge, .sound]
    }

    // MARK: - Notification Tapped
    func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        didReceive response: UNNotificationResponse
    ) async {
        let userInfo = response.notification.request.content.userInfo
        let actionIdentifier = response.actionIdentifier

        analyticsTracker.trackNotificationTapped(userInfo: userInfo, action: actionIdentifier)

        switch actionIdentifier {
        case UNNotificationDefaultActionIdentifier:
            await router.routeToContent(from: userInfo)
        case UNNotificationDismissActionIdentifier:
            break
        default:
            await router.handleAction(actionIdentifier, userInfo: userInfo, response: response)
        }
    }
}
```

#### 2.2 App Delegate Integration

```swift
// File: App/AppDelegate.swift (relevant notification methods)

import UIKit

class AppDelegate: NSObject, UIApplicationDelegate {
    let notificationHandler: NotificationHandler
    let deviceTokenManager: DeviceTokenManager

    // Set delegate BEFORE didFinishLaunching returns
    func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        UNUserNotificationCenter.current().delegate = notificationHandler
        registerNotificationCategories()
        return true
    }

    func application(
        _ application: UIApplication,
        didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
    ) {
        Task {
            try? await deviceTokenManager.registerToken(deviceToken)
        }
    }

    func application(
        _ application: UIApplication,
        didFailToRegisterForRemoteNotificationsWithError error: Error
    ) {
        // Log but don't crash - notifications are optional functionality
        print("APNs registration failed: \(error.localizedDescription)")
    }

    // MARK: - Silent Push
    func application(
        _ application: UIApplication,
        didReceiveRemoteNotification userInfo: [AnyHashable: Any]
    ) async -> UIBackgroundFetchResult {
        guard let contentType = userInfo["content-type"] as? String else {
            return .noData
        }

        do {
            switch contentType {
            case "data-sync":
                try await DataSyncService.shared.performSync()
                return .newData
            case "badge-update":
                let count = userInfo["badge-count"] as? Int ?? 0
                await MainActor.run {
                    application.applicationIconBadgeNumber = count
                }
                return .newData
            default:
                return .noData
            }
        } catch {
            return .failed
        }
    }
}
```

---

### Phase 3: Notification Actions & Categories

#### 3.1 Category Registration

```swift
// File: Services/Notifications/NotificationCategories.swift

import UserNotifications

enum NotificationCategory {
    static func registerAll() {
        let center = UNUserNotificationCenter.current()

        let messageCategory = UNNotificationCategory(
            identifier: "MESSAGE",
            actions: [
                UNNotificationAction(
                    identifier: "REPLY_ACTION",
                    title: "Reply",
                    options: [],
                    icon: UNNotificationActionIcon(systemImageName: "arrowshape.turn.up.left")
                ),
                UNTextInputNotificationAction(
                    identifier: "INLINE_REPLY",
                    title: "Quick Reply",
                    options: [],
                    icon: UNNotificationActionIcon(systemImageName: "text.bubble"),
                    textInputButtonTitle: "Send",
                    textInputPlaceholder: "Type a reply..."
                ),
                UNNotificationAction(
                    identifier: "MARK_READ_ACTION",
                    title: "Mark as Read",
                    options: .authenticationRequired
                )
            ],
            intentIdentifiers: [],
            options: [.customDismissAction]
        )

        let approvalCategory = UNNotificationCategory(
            identifier: "APPROVAL_REQUEST",
            actions: [
                UNNotificationAction(
                    identifier: "APPROVE_ACTION",
                    title: "Approve",
                    options: .authenticationRequired,
                    icon: UNNotificationActionIcon(systemImageName: "checkmark.circle")
                ),
                UNNotificationAction(
                    identifier: "REJECT_ACTION",
                    title: "Reject",
                    options: [.authenticationRequired, .destructive],
                    icon: UNNotificationActionIcon(systemImageName: "xmark.circle")
                )
            ],
            intentIdentifiers: [],
            options: []
        )

        center.setNotificationCategories([messageCategory, approvalCategory])
    }
}
```

---

### Phase 4: Rich Notifications & Service Extension

**CHECKPOINT 2:** Review notification handling before adding rich content.

```markdown
## Notification Handling Summary

| Feature | Implementation |
|---------|---------------|
| Foreground delivery | Banner + badge + sound |
| Tap routing | Deep link via NotificationRouter |
| Action handling | Category-specific actions |
| Silent push | Background fetch with content type routing |
| Categories | MESSAGE (reply, mark read), APPROVAL (approve, reject) |

**Ready for rich notification and service extension setup?**
```

#### 4.1 Notification Service Extension

```swift
// File: NotificationServiceExtension/NotificationService.swift
// Target: NotificationServiceExtension (new app extension target)

import UserNotifications

class NotificationService: UNNotificationServiceExtension {
    private var contentHandler: ((UNNotificationContent) -> Void)?
    private var bestAttemptContent: UNMutableNotificationContent?

    override func didReceive(
        _ request: UNNotificationRequest,
        withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void
    ) {
        self.contentHandler = contentHandler
        bestAttemptContent = (request.content.mutableCopy() as? UNMutableNotificationContent)

        guard let bestAttemptContent else {
            contentHandler(request.content)
            return
        }

        Task {
            // Download and attach media
            if let mediaURLString = bestAttemptContent.userInfo["media-url"] as? String,
               let mediaURL = URL(string: mediaURLString) {
                do {
                    let attachment = try await downloadAttachment(from: mediaURL)
                    bestAttemptContent.attachments = [attachment]
                } catch {
                    // Deliver without attachment rather than failing
                }
            }

            // Decrypt end-to-end encrypted content if needed
            if let encrypted = bestAttemptContent.userInfo["encrypted-body"] as? String {
                bestAttemptContent.body = CryptoHelper.decrypt(encrypted) ?? bestAttemptContent.body
            }

            contentHandler(bestAttemptContent)
        }
    }

    override func serviceExtensionTimeWillExpire() {
        // Deliver best attempt before 30-second deadline
        if let contentHandler, let bestAttemptContent {
            contentHandler(bestAttemptContent)
        }
    }

    private func downloadAttachment(from url: URL) async throws -> UNNotificationAttachment {
        let (data, response) = try await URLSession.shared.data(from: url)
        let mimeType = (response as? HTTPURLResponse)?.mimeType ?? "image/jpeg"
        let ext = mimeType.contains("png") ? "png" : "jpg"

        let tempURL = FileManager.default.temporaryDirectory
            .appendingPathComponent(UUID().uuidString)
            .appendingPathExtension(ext)
        try data.write(to: tempURL)
        return try UNNotificationAttachment(identifier: UUID().uuidString, url: tempURL)
    }
}
```

#### 4.2 Local Notification Scheduling

```swift
// File: Services/Notifications/LocalNotificationScheduler.swift

import UserNotifications

struct LocalNotificationScheduler {
    static func scheduleReminder(
        id: String,
        title: String,
        body: String,
        triggerDate: Date,
        repeats: Bool = false,
        categoryIdentifier: String? = nil
    ) async throws {
        let content = UNMutableNotificationContent()
        content.title = title
        content.body = body
        content.sound = .default
        content.threadIdentifier = "reminders"
        if let category = categoryIdentifier {
            content.categoryIdentifier = category
        }

        let components = Calendar.current.dateComponents(
            [.year, .month, .day, .hour, .minute],
            from: triggerDate
        )
        let trigger = UNCalendarNotificationTrigger(dateMatching: components, repeats: repeats)

        let request = UNNotificationRequest(identifier: id, content: content, trigger: trigger)
        try await UNUserNotificationCenter.current().add(request)
    }

    static func cancelNotification(id: String) {
        UNUserNotificationCenter.current().removePendingNotificationRequests(withIdentifiers: [id])
    }

    static func cancelAllNotifications() {
        UNUserNotificationCenter.current().removeAllPendingNotificationRequests()
    }
}
```

---

## Expected Output

### File Structure

```
Services/Notifications/
├── NotificationPermissionManager.swift  # Permission state and requests
├── DeviceTokenManager.swift             # APNs token registration
├── NotificationHandler.swift            # UNUserNotificationCenterDelegate
├── NotificationCategories.swift         # Action categories
└── LocalNotificationScheduler.swift     # Local notification helpers

NotificationServiceExtension/
└── NotificationService.swift            # Rich notification processing

App/
└── AppDelegate.swift                    # Token callbacks, silent push
```

### Implementation Checklist

- [ ] Push Notification capability added in Xcode
- [ ] Background Modes > Remote notifications enabled
- [ ] `UNUserNotificationCenter.delegate` set before `didFinishLaunching` returns
- [ ] Permission request with pre-permission screen
- [ ] Device token converted to hex string
- [ ] Token registered with backend (deduplicated)
- [ ] Foreground notification presentation configured
- [ ] Notification tap routing implemented
- [ ] Notification actions and categories registered
- [ ] Notification Service Extension target created
- [ ] Rich media download with timeout handling
- [ ] Silent push with `content-available: 1` handling
- [ ] Local notification scheduling support
- [ ] Notification grouping via `threadIdentifier`

---

## Techniques Used

- **ST-01** (Clear Objective): Focused objective for complete push notification implementation
- **ST-02** (Sequential Instructions): Phased approach from registration through rich notifications
- **ST-03** (Output Format Templates): Code templates for each notification component

---

## Related Prompts

- [ios_background_tasks.md](../implementation/ios_background_tasks.md) - Background processing for silent push data sync
- [ios_state_management.md](../implementation/ios_state_management.md) - State management for notification-driven UI updates
- [ios_privacy_compliance.md](../publishing/ios_privacy_compliance.md) - Privacy compliance for notification data
- [ios_api_integration.md](../implementation/ios_api_integration.md) - Backend integration for device token registration
