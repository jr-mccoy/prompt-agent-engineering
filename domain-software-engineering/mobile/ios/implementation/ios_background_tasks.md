---
title: "iOS Background Tasks"
category: mobile-development
description: "Implement BGTaskScheduler with BGAppRefreshTask and BGProcessingTask, URLSession background transfers, and silent push triggers for background execution."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - ST-03
difficulty: advanced
tags:
  - ios
  - swift
  - background-tasks
  - bgtaskscheduler
  - urlsession
  - silent-push
  - mobile-development
updated: "2026-03-19"
---

# iOS Background Tasks

**Objective:** Implement background execution using BGTaskScheduler (BGAppRefreshTask, BGProcessingTask), URLSession background transfers, and silent push notification triggers for reliable background data processing in iOS applications.

**When to Use:** Use this prompt when implementing background data sync, periodic content refresh, large file uploads/downloads, or background database maintenance. Best used after the app's data sync and networking patterns are established.

**Prompt Type:** Modular (350-400 lines)

---

## Context Gathering

Before implementing background tasks, gather essential context:

1. **Background Requirements:**
   - "What work needs to happen in the background (sync, upload, cleanup)?"
   - "How frequently should background refresh occur?"
   - "Are there large file transfers that need background URLSession?"

2. **Existing Setup:**
   - "Is BGTaskScheduler already registered in Info.plist?"
   - "Are there existing background URLSession configurations?"
   - "Does the app receive silent push notifications?"

3. **Constraints:**
   - "What is the maximum acceptable staleness for data?"
   - "Are there power-sensitive operations (ML, image processing)?"
   - "Does the task need network connectivity?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before implementing ANY code, you MUST:**

1. **Register task identifiers in Info.plist** - BGTaskScheduler tasks MUST be listed under `BGTaskSchedulerPermittedIdentifiers`.
2. **Register handlers before app launch completes** - BGTaskScheduler.shared.register() must be called in application(_:didFinishLaunchingWithOptions:) or App init.
3. **Test with Xcode debugger** - Background tasks can be triggered via `e -l objc -- (void)[[BGTaskScheduler sharedScheduler] _simulateLaunchForTaskWithIdentifier:@"TASK_ID"]`.
4. **Handle task expiration** - Every BGTask MUST set an expirationHandler.

### False-Positive Prevention

- ❌ Do NOT assume background tasks will run at the exact scheduled time
- ❌ Do NOT perform unlimited work - respect the time budget (30s for refresh, minutes for processing)
- ❌ Do NOT forget to call task.setTaskCompleted(success:) - the system will penalize your app
- ❌ Do NOT schedule tasks without registering them in Info.plist first
- ❌ Do NOT use BGProcessingTask for time-sensitive work (may be deferred significantly)
- ✅ DO set expirationHandler on every BGTask
- ✅ DO test background tasks using Xcode simulator commands
- ✅ DO use BGProcessingTask for power-intensive work (requires charging + Wi-Fi)
- ✅ DO handle the case where background tasks are never granted by the system

---

### Module 1: BGTaskScheduler Setup

```swift
// File: Background/BackgroundTaskManager.swift

import BackgroundTasks
import OSLog

final class BackgroundTaskManager {
    static let shared = BackgroundTaskManager()

    // Task identifiers - MUST match Info.plist BGTaskSchedulerPermittedIdentifiers
    static let appRefreshTaskID = "com.example.app.refresh"
    static let dataProcessingTaskID = "com.example.app.processing"
    static let dbMaintenanceTaskID = "com.example.app.db-maintenance"

    private let logger = Logger(subsystem: "com.example.app", category: "BackgroundTask")
    private let syncService: SyncServiceProtocol
    private let maintenanceService: MaintenanceServiceProtocol

    init(
        syncService: SyncServiceProtocol = SyncService(),
        maintenanceService: MaintenanceServiceProtocol = MaintenanceService()
    ) {
        self.syncService = syncService
        self.maintenanceService = maintenanceService
    }

    /// Call in App.init() or application(_:didFinishLaunchingWithOptions:)
    func registerTasks() {
        BGTaskScheduler.shared.register(
            forTaskWithIdentifier: Self.appRefreshTaskID,
            using: nil
        ) { [weak self] task in
            self?.handleAppRefresh(task as! BGAppRefreshTask)
        }

        BGTaskScheduler.shared.register(
            forTaskWithIdentifier: Self.dataProcessingTaskID,
            using: nil
        ) { [weak self] task in
            self?.handleDataProcessing(task as! BGProcessingTask)
        }

        BGTaskScheduler.shared.register(
            forTaskWithIdentifier: Self.dbMaintenanceTaskID,
            using: nil
        ) { [weak self] task in
            self?.handleDBMaintenance(task as! BGProcessingTask)
        }

        logger.info("Background tasks registered")
    }

    /// Schedule all background tasks (call when app enters background)
    func scheduleAllTasks() {
        scheduleAppRefresh()
        scheduleDataProcessing()
    }

    // MARK: - App Refresh (lightweight, ~30 seconds)

    private func scheduleAppRefresh() {
        let request = BGAppRefreshTaskRequest(identifier: Self.appRefreshTaskID)
        request.earliestBeginDate = Date(timeIntervalSinceNow: 15 * 60) // 15 min minimum

        do {
            try BGTaskScheduler.shared.submit(request)
            logger.info("App refresh scheduled")
        } catch {
            logger.error("Failed to schedule app refresh: \(error)")
        }
    }

    private func handleAppRefresh(_ task: BGAppRefreshTask) {
        logger.info("App refresh started")

        // Schedule the next refresh immediately
        scheduleAppRefresh()

        let syncTask = Task {
            do {
                try await syncService.performQuickSync()
                task.setTaskCompleted(success: true)
                logger.info("App refresh completed successfully")
            } catch {
                task.setTaskCompleted(success: false)
                logger.error("App refresh failed: \(error)")
            }
        }

        // CRITICAL: Handle expiration
        task.expirationHandler = {
            self.logger.warning("App refresh expired, cancelling")
            syncTask.cancel()
            task.setTaskCompleted(success: false)
        }
    }

    // MARK: - Data Processing (longer, power-aware)

    private func scheduleDataProcessing() {
        let request = BGProcessingTaskRequest(identifier: Self.dataProcessingTaskID)
        request.requiresNetworkConnectivity = true
        request.requiresExternalPower = false // Set true for heavy tasks
        request.earliestBeginDate = Date(timeIntervalSinceNow: 60 * 60) // 1 hour

        do {
            try BGTaskScheduler.shared.submit(request)
            logger.info("Data processing scheduled")
        } catch {
            logger.error("Failed to schedule processing: \(error)")
        }
    }

    private func handleDataProcessing(_ task: BGProcessingTask) {
        logger.info("Data processing started")

        let processingTask = Task {
            do {
                try await syncService.performFullSync()
                task.setTaskCompleted(success: true)
                logger.info("Data processing completed")
            } catch {
                task.setTaskCompleted(success: false)
                logger.error("Data processing failed: \(error)")
            }
        }

        task.expirationHandler = {
            self.logger.warning("Data processing expired")
            processingTask.cancel()
            task.setTaskCompleted(success: false)
        }
    }

    // MARK: - DB Maintenance

    private func handleDBMaintenance(_ task: BGProcessingTask) {
        let maintenanceTask = Task {
            do {
                try await maintenanceService.performMaintenance()
                task.setTaskCompleted(success: true)
            } catch {
                task.setTaskCompleted(success: false)
            }
        }

        task.expirationHandler = {
            maintenanceTask.cancel()
            task.setTaskCompleted(success: false)
        }
    }
}
```

### Module 2: App Integration

```swift
// File: App/MyApp.swift

import SwiftUI
import BackgroundTasks

@main
struct MyApp: App {
    @Environment(\.scenePhase) private var scenePhase

    init() {
        BackgroundTaskManager.shared.registerTasks()
    }

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: scenePhase) { _, newPhase in
            if newPhase == .background {
                BackgroundTaskManager.shared.scheduleAllTasks()
            }
        }
    }
}
```

```xml
<!-- Info.plist addition -->
<!-- File: Info.plist -->
<key>BGTaskSchedulerPermittedIdentifiers</key>
<array>
    <string>com.example.app.refresh</string>
    <string>com.example.app.processing</string>
    <string>com.example.app.db-maintenance</string>
</array>
```

### Module 3: Background URLSession Transfers

```swift
// File: Background/BackgroundTransferManager.swift

import Foundation
import OSLog

final class BackgroundTransferManager: NSObject, @unchecked Sendable {
    static let shared = BackgroundTransferManager()

    private let logger = Logger(subsystem: "com.example.app", category: "BackgroundTransfer")
    private var completionHandlers: [String: () -> Void] = [:]
    private var uploadContinuations: [String: CheckedContinuation<URL, Error>] = [:]

    lazy var backgroundSession: URLSession = {
        let config = URLSessionConfiguration.background(
            withIdentifier: "com.example.app.background-transfer"
        )
        config.isDiscretionary = false // Set true for non-urgent transfers
        config.sessionSendsLaunchEvents = true
        config.allowsCellularAccess = true

        return URLSession(configuration: config, delegate: self, delegateQueue: nil)
    }()

    /// Start a background download
    func downloadFile(from url: URL) -> URLSessionDownloadTask {
        let task = backgroundSession.downloadTask(with: url)
        task.earliestBeginDate = Date() // Start immediately
        task.countOfBytesClientExpectsToSend = 0
        task.countOfBytesClientExpectsToReceive = 10 * 1024 * 1024 // Estimate 10MB
        task.resume()
        logger.info("Background download started: \(url.lastPathComponent)")
        return task
    }

    /// Start a background upload
    func uploadFile(fileURL: URL, to endpoint: URL) -> URLSessionUploadTask {
        var request = URLRequest(url: endpoint)
        request.httpMethod = "PUT"
        request.setValue("application/octet-stream", forHTTPHeaderField: "Content-Type")

        let task = backgroundSession.uploadTask(with: request, fromFile: fileURL)
        task.resume()
        logger.info("Background upload started: \(fileURL.lastPathComponent)")
        return task
    }

    /// Store completion handler from AppDelegate
    func setCompletionHandler(_ handler: @escaping () -> Void, for identifier: String) {
        completionHandlers[identifier] = handler
    }
}

// MARK: - URLSession Delegate

extension BackgroundTransferManager: URLSessionDelegate, URLSessionDownloadDelegate {

    func urlSession(
        _ session: URLSession,
        downloadTask: URLSessionDownloadTask,
        didFinishDownloadingTo location: URL
    ) {
        // Move file from temporary location to permanent storage
        let documentsURL = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
        let fileName = downloadTask.originalRequest?.url?.lastPathComponent ?? "download"
        let destinationURL = documentsURL.appendingPathComponent(fileName)

        do {
            if FileManager.default.fileExists(atPath: destinationURL.path) {
                try FileManager.default.removeItem(at: destinationURL)
            }
            try FileManager.default.moveItem(at: location, to: destinationURL)
            logger.info("Download completed: \(fileName)")
        } catch {
            logger.error("Failed to save download: \(error)")
        }
    }

    func urlSession(
        _ session: URLSession,
        task: URLSessionTask,
        didCompleteWithError error: Error?
    ) {
        if let error {
            logger.error("Transfer failed: \(error)")
        }
    }

    func urlSessionDidFinishEvents(
        forBackgroundURLSession session: URLSession
    ) {
        DispatchQueue.main.async { [weak self] in
            let handler = self?.completionHandlers.removeValue(forKey: session.configuration.identifier ?? "")
            handler?()
            self?.logger.info("Background session events finished")
        }
    }
}
```

### Module 4: Silent Push Triggers

```swift
// File: Background/SilentPushHandler.swift

import UIKit
import UserNotifications
import OSLog

final class SilentPushHandler {
    private let logger = Logger(subsystem: "com.example.app", category: "SilentPush")
    private let syncService: SyncServiceProtocol

    init(syncService: SyncServiceProtocol = SyncService()) {
        self.syncService = syncService
    }

    /// Handle silent push notification
    /// Called from application(_:didReceiveRemoteNotification:fetchCompletionHandler:)
    func handleSilentPush(
        userInfo: [AnyHashable: Any],
        completionHandler: @escaping (UIBackgroundFetchResult) -> Void
    ) {
        // Verify it's a content-available push
        guard let aps = userInfo["aps"] as? [String: Any],
              aps["content-available"] as? Int == 1 else {
            completionHandler(.noData)
            return
        }

        let pushType = userInfo["type"] as? String ?? "unknown"
        logger.info("Silent push received: \(pushType)")

        Task {
            do {
                switch pushType {
                case "sync":
                    try await syncService.performQuickSync()
                    completionHandler(.newData)

                case "invalidate-cache":
                    let keys = userInfo["cache_keys"] as? [String] ?? []
                    await CacheManager.shared.invalidate(keys: keys)
                    completionHandler(.newData)

                case "content-update":
                    let contentId = userInfo["content_id"] as? String
                    if let contentId {
                        try await syncService.syncSingleItem(id: contentId)
                        completionHandler(.newData)
                    } else {
                        completionHandler(.noData)
                    }

                default:
                    logger.warning("Unknown push type: \(pushType)")
                    completionHandler(.noData)
                }
            } catch {
                logger.error("Silent push handling failed: \(error)")
                completionHandler(.failed)
            }
        }
    }
}

// AppDelegate integration
class AppDelegate: NSObject, UIApplicationDelegate {
    let silentPushHandler = SilentPushHandler()

    func application(
        _ application: UIApplication,
        didReceiveRemoteNotification userInfo: [AnyHashable: Any],
        fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void
    ) {
        silentPushHandler.handleSilentPush(
            userInfo: userInfo,
            completionHandler: completionHandler
        )
    }

    // Store background URLSession completion handler
    func application(
        _ application: UIApplication,
        handleEventsForBackgroundURLSession identifier: String,
        completionHandler: @escaping () -> Void
    ) {
        BackgroundTransferManager.shared.setCompletionHandler(
            completionHandler, for: identifier
        )
    }
}
```

---

## Expected Output

### File Structure

```
Background/
├── BackgroundTaskManager.swift       # BGTaskScheduler setup
├── BackgroundTransferManager.swift   # Background URLSession
└── SilentPushHandler.swift           # Silent push processing

App/
├── MyApp.swift                       # Task registration + scheduling
└── AppDelegate.swift                 # Background session + push handler
```

### Implementation Checklist

- [ ] BGTaskScheduler task identifiers in Info.plist
- [ ] Task registration in App.init()
- [ ] BGAppRefreshTask with 15-minute schedule
- [ ] BGProcessingTask for heavy work
- [ ] Expiration handlers on all BGTasks
- [ ] Background URLSession for downloads/uploads
- [ ] Silent push notification handling
- [ ] Proper completion handler calls
- [ ] OSLog-based debugging

---

## Example Interaction

**User:** "I need to sync new content every 30 minutes in the background."

**Assistant:**
```swift
// In BackgroundTaskManager:
private func scheduleAppRefresh() {
    let request = BGAppRefreshTaskRequest(identifier: Self.appRefreshTaskID)
    request.earliestBeginDate = Date(timeIntervalSinceNow: 30 * 60)
    try? BGTaskScheduler.shared.submit(request)
}

// Also add silent push as a complement (more reliable):
// Server sends: {"aps": {"content-available": 1}, "type": "sync"}
// This triggers immediate sync without waiting for BGTaskScheduler
```

---

## Techniques Used

- **ST-01** (Clear Objective): Focused on background execution strategies
- **ST-02** (Sequential Instructions): Modular approach per background mechanism
- **RT-02** (Multi-Dimensional Analysis): BGTask, URLSession, silent push
- **RT-05** (Edge Case Identification): Expiration, system throttling, cold start
- **ST-03** (Output Format Templates): Code templates per module

---

## Related Prompts

- [ios_offline_first_sync.md](ios_offline_first_sync.md) - Sync data that background tasks fetch
- [ios_push_notifications.md](ios_push_notifications.md) - Configure silent push notifications
- [ios_api_integration.md](ios_api_integration.md) - Network layer for background requests
- [ios_data_layer_implementation.md](ios_data_layer_implementation.md) - Persistence for background data

---

## Customization Guide

### For Testing Background Tasks

Use Xcode debugger commands:
```
// Pause app, then in LLDB:
e -l objc -- (void)[[BGTaskScheduler sharedScheduler] _simulateLaunchForTaskWithIdentifier:@"com.example.app.refresh"]

// Force early expiration:
e -l objc -- (void)[[BGTaskScheduler sharedScheduler] _simulateExpirationForTaskWithIdentifier:@"com.example.app.refresh"]
```

### For Task Chaining

Run processing after refresh:
```swift
private func handleAppRefresh(_ task: BGAppRefreshTask) {
    let work = Task {
        try await syncService.performQuickSync()
        // If significant changes, schedule processing
        if await syncService.hasPendingProcessing {
            scheduleDataProcessing()
        }
        task.setTaskCompleted(success: true)
    }
    task.expirationHandler = { work.cancel() }
}
```
