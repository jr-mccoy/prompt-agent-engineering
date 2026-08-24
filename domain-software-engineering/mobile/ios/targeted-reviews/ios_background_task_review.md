---
title: "iOS Background Task Review"
category: mobile-development
description: "Review BGTaskScheduler registration, URLSession background transfers, silent push handling, and system resource budget management for iOS background execution."
techniques:
  - ST-01
  - RT-02
  - AG-02
difficulty: advanced
tags:
  - ios
  - swift
  - code-review
  - background-tasks
  - bgtaskscheduler
updated: "2026-03-19"
---

# iOS Background Task Review

**Objective:** Audit background execution for correct BGTaskScheduler registration and handling, URLSession background transfer configuration, silent push notification processing, and system resource budget management to ensure reliable background operations without battery drain or system throttling.

**When to Use:** Apply when reviewing background sync, content prefetching, background processing features, or when users report missing notifications, incomplete syncs, or excessive battery usage.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. What background modes are enabled in the app's capabilities (fetch, processing, push, transfers)?
2. Are BGAppRefreshTask or BGProcessingTask registered?
3. Does the app use background URLSession for uploads/downloads?
4. Is silent push (content-available) used for triggering updates?

## Instructions

### CRITICAL: Verification Requirements

- BGTask identifiers must be registered in Info.plist AND in code before app finishes launching
- Background URLSession must use a unique identifier and implement delegate methods (not closures)
- Silent push handlers must call the completion handler within 30 seconds
- Background tasks must handle expiration handler to save state before being killed

### False-Positive Prevention

- ❌ Do NOT flag short background tasks (< 5 seconds) as needing BGTaskScheduler — beginBackgroundTask suffices
- ✅ DO flag long-running operations relying only on beginBackgroundTask (30 second limit)
- ❌ Do NOT flag missing background fetch if the app uses silent push for the same purpose
- ✅ DO flag both background fetch AND silent push updating the same data without deduplication
- ❌ Do NOT flag BGProcessingTask not running in simulator — it requires device testing
- ✅ DO flag BGProcessingTask without expiration handler — will be killed without state save

1. **BGTaskScheduler Registration**

```swift
// BAD: Registration after app launch — tasks never fire
class AppDelegate: UIResponder, UIApplicationDelegate {
    func applicationDidBecomeActive(_ application: UIApplication) {
        BGTaskScheduler.shared.register(
            forTaskWithIdentifier: "com.app.refresh",
            using: nil
        ) { task in
            self.handleRefresh(task as! BGAppRefreshTask)
        }
        // Too late — must register in didFinishLaunchingWithOptions
    }
}

// GOOD: Register before app finishes launching
class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        BGTaskScheduler.shared.register(
            forTaskWithIdentifier: "com.app.refresh",
            using: nil
        ) { task in
            self.handleRefresh(task as! BGAppRefreshTask)
        }
        return true
    }

    func handleRefresh(_ task: BGAppRefreshTask) {
        scheduleNextRefresh() // schedule next occurrence immediately

        let operation = RefreshOperation()
        task.expirationHandler = {
            operation.cancel()
        }

        operation.completionBlock = {
            task.setTaskCompleted(success: !operation.isCancelled)
        }
        OperationQueue().addOperation(operation)
    }
}
```

2. **Background URLSession**

```swift
// BAD: Foreground URLSession — transfers cancelled on app suspension
func uploadFile(_ data: Data) {
    URLSession.shared.uploadTask(with: request, from: data) { _, _, error in
        // This closure may never fire if app is suspended during upload
    }.resume()
}

// GOOD: Background URLSession with delegate
class BackgroundTransferManager: NSObject, URLSessionDelegate, URLSessionDownloadDelegate {
    static let shared = BackgroundTransferManager()

    lazy var session: URLSession = {
        let config = URLSessionConfiguration.background(
            withIdentifier: "com.app.background-transfer"
        )
        config.isDiscretionary = false
        config.sessionSendsLaunchEvents = true
        return URLSession(configuration: config, delegate: self, delegateQueue: nil)
    }()

    func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask,
                    didFinishDownloadingTo location: URL) {
        // Move file from tmp location to permanent storage
        let dest = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
            .appendingPathComponent(downloadTask.originalRequest?.url?.lastPathComponent ?? "file")
        try? FileManager.default.moveItem(at: location, to: dest)
    }

    func urlSessionDidFinishEvents(forBackgroundURLSession session: URLSession) {
        DispatchQueue.main.async {
            AppDelegate.backgroundCompletionHandler?()
        }
    }
}
```

3. **Silent Push Handling**

```swift
// BAD: No completion handler call — system penalizes app
func application(_ application: UIApplication,
                 didReceiveRemoteNotification userInfo: [AnyHashable: Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    syncManager.sync() // async operation — completionHandler never called
    // System thinks app is hung, reduces future push delivery budget
}

// GOOD: Call completion handler within 30 seconds
func application(_ application: UIApplication,
                 didReceiveRemoteNotification userInfo: [AnyHashable: Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    Task {
        do {
            let hasNewData = try await syncManager.sync()
            completionHandler(hasNewData ? .newData : .noData)
        } catch {
            completionHandler(.failed)
        }
    }
}
```

4. **Expiration Handler**

```swift
// BAD: No expiration handler — work killed without cleanup
func handleProcessing(_ task: BGProcessingTask) {
    Task {
        try await heavyMigration() // may take 5+ minutes
        task.setTaskCompleted(success: true)
    }
    // If system kills task, no state saved, no completion called
}

// GOOD: Expiration handler saves progress
func handleProcessing(_ task: BGProcessingTask) {
    let operation = MigrationOperation()

    task.expirationHandler = {
        operation.saveProgress() // persist how far we got
        operation.cancel()
    }

    Task {
        let success = await operation.run()
        task.setTaskCompleted(success: success)
    }
}
```

## Expected Output

```
## Background Task Review Report

### Summary
- **Background capabilities reviewed:** N
- **Registration issues:** N
- **Transfer configuration issues:** N
- **Completion handler gaps:** N
- **Expiration handler gaps:** N

### Findings
#### [Severity] Issue — File:Line
- **Issue:** ...
- **System impact:** Throttling / battery / data loss
- **Recommendation:** ...
```

## Example Output

```
## Background Task Review Report

### Summary
- **Background capabilities reviewed:** 4
- **Registration issues:** 1
- **Transfer configuration issues:** 0
- **Completion handler gaps:** 2
- **Expiration handler gaps:** 1

### Findings

#### [Critical] Missing Completion Handler — PushHandler.swift:L22
- **Issue:** Silent push `fetchCompletionHandler` not called after sync operation completes.
- **System impact:** iOS reduces silent push delivery budget; eventually stops delivering.
- **Recommendation:** Call `completionHandler(.newData)` or `.failed` in sync completion.

#### [Warning] No Expiration Handler — DataProcessingTask.swift:L15
- **Issue:** BGProcessingTask runs a 3-minute database cleanup without expiration handler.
- **System impact:** Process killed without saving progress; work repeated on next run.
- **Recommendation:** Add `task.expirationHandler` that saves checkpoint and cancels operation.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Separates registration, transfers, push, expiration
- **RT-02 (Role-Based Task Framing):** Reviewer acts as iOS background execution specialist
- **AG-02 (Automated Guardrails):** Prevents false flags on short tasks and valid push patterns

## Related Prompts

- `ios_push_notification_review.md` — Push notification implementation
- `ios_swift_concurrency_safety_review.md` — Async safety in background tasks
- `ios_combine_pipeline_review.md` — Reactive pipelines in background contexts

## Customization Guide

- **Health/fitness apps:** Add HealthKit background delivery and workout session checks
- **Navigation apps:** Add background location updates and significant change monitoring
- **Media apps:** Add audio session configuration and background playback checks
