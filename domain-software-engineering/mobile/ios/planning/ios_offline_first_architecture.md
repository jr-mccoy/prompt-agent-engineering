---
title: "iOS Offline-First Architecture"
category: mobile-development
description: "Design offline-first iOS architecture with local persistence, CloudKit sync, conflict resolution, background refresh, and network-aware UI patterns."
techniques:
  - ST-01
  - ST-02
  - RT-02
difficulty: advanced
tags:
  - ios
  - swift
  - offline-first
  - cloudkit
  - sync
updated: "2026-03-20"
---

# iOS Offline-First Architecture

**Objective:** Design a complete offline-first iOS architecture where local persistence is the source of truth, cloud sync is transparent and conflict-resilient, and the UI gracefully handles all connectivity states, using SwiftData/Core Data with CloudKit or custom backend sync.

**When to Use:** Use when building an app that must function fully without network connectivity, requires data sync across devices, or serves users in low-connectivity environments. Essential for productivity apps, field service tools, health tracking, note-taking, and any app where data loss is unacceptable.

**Prompt Type:** Comprehensive (400+ lines)

---

## Context Gathering

Before designing the architecture, gather essential context:

1. **Data Characteristics:**
   - "What types of data need offline support (text, images, files, structured records)?"
   - "How large is the dataset per user (KBs, MBs, GBs)?"
   - "How frequently does data change?"
   - "Are there shared/collaborative data scenarios?"

2. **Sync Requirements:**
   - "Is CloudKit acceptable or is a custom backend required?"
   - "How many devices per user need sync?"
   - "What is the acceptable sync latency (real-time, minutes, hours)?"
   - "How should conflicts be resolved (last-write-wins, merge, user-choice)?"

3. **Connectivity Context:**
   - "What connectivity scenarios are common (airplane, rural, subway, hospital)?"
   - "Should the app indicate sync status to the user?"
   - "Are there data operations that REQUIRE network (e.g., payments)?"

4. **Platform:**
   - "Minimum iOS version? (Determines SwiftData vs Core Data availability)"
   - "Apple Watch companion app? (Limited connectivity model)"
   - "Is iCloud account required or optional?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before designing ANY offline architecture, you MUST:**

1. **Define the source of truth** - Local database is ALWAYS the source of truth in offline-first.
2. **Design conflict resolution BEFORE sync** - Never assume conflicts won't happen.
3. **Handle all connectivity states** - Offline, online, transitioning, limited connectivity.
4. **Plan data migration** - Schema changes must work with unsynchronized local data.
5. **Test offline-first** - The app must be tested with network disabled from first launch.

### False-Positive Prevention

- ❌ Do NOT treat the server as the source of truth (that's online-first, not offline-first)
- ❌ Do NOT assume CloudKit sync "just works" without conflict handling
- ❌ Do NOT queue unlimited operations for sync (memory and storage limits exist)
- ❌ Do NOT block UI on network operations -- all reads come from local store
- ❌ Do NOT ignore the iCloud account sign-out scenario (data must remain accessible)
- ✅ DO write to local store first, sync to cloud asynchronously
- ✅ DO design idempotent sync operations (safe to retry)
- ✅ DO provide clear sync status indicators in UI
- ✅ DO handle CloudKit quota limits and errors gracefully
- ✅ DO test with NSPersistentCloudKitContainer debug logging enabled

---

### Phase 1: Data Layer Architecture

#### 1.1 Core Principle: Local-First

```
User Action → Local Write → UI Update → Background Sync → Cloud
                    ↑                            ↓
                    └──── Conflict Resolution ────┘
```

All reads come from the local store. All writes go to the local store first. Sync is a background concern that never blocks the user.

#### 1.2 Persistence Stack (SwiftData + CloudKit)

```swift
// File: Core/Persistence/PersistenceController.swift

import SwiftUI
import SwiftData

@MainActor
final class PersistenceController {
    static let shared = PersistenceController()

    let container: ModelContainer

    init(inMemory: Bool = false) {
        let schema = Schema([
            Note.self,
            Folder.self,
            Attachment.self,
        ])

        let configuration: ModelConfiguration
        if inMemory {
            configuration = ModelConfiguration(
                schema: schema,
                isStoredInMemoryOnly: true
            )
        } else {
            configuration = ModelConfiguration(
                schema: schema,
                isStoredInMemoryOnly: false,
                cloudKitDatabase: .automatic  // Enables CloudKit sync
            )
        }

        do {
            container = try ModelContainer(
                for: schema,
                configurations: [configuration]
            )
        } catch {
            fatalError("Failed to create ModelContainer: \(error)")
        }
    }

    /// Preview/testing container with no CloudKit
    static var preview: PersistenceController {
        PersistenceController(inMemory: true)
    }
}
```

#### 1.3 Model Design for Sync

```swift
// File: Core/Models/Note.swift

import SwiftData
import Foundation

@Model
final class Note {
    // Stable identifier for cross-device sync
    @Attribute(.unique)
    var id: UUID

    var title: String
    var content: String
    var createdAt: Date
    var modifiedAt: Date

    // Soft delete for sync (never hard-delete synced records)
    var isDeleted: Bool

    // Sync metadata
    var lastSyncedAt: Date?
    var needsSync: Bool

    // Relationships
    @Relationship(deleteRule: .cascade)
    var attachments: [Attachment]

    @Relationship(inverse: \Folder.notes)
    var folder: Folder?

    init(
        title: String = "",
        content: String = "",
        folder: Folder? = nil
    ) {
        self.id = UUID()
        self.title = title
        self.content = content
        self.createdAt = .now
        self.modifiedAt = .now
        self.isDeleted = false
        self.needsSync = true
        self.lastSyncedAt = nil
        self.attachments = []
        self.folder = folder
    }

    func markModified() {
        modifiedAt = .now
        needsSync = true
    }
}
```

---

### Phase 2: Sync Engine

**CHECKPOINT 1:** Confirm data models and persistence stack design.

```markdown
## Data Layer Summary
- Models defined: _
- Persistence: SwiftData / Core Data
- CloudKit enabled: Yes / No / Custom backend
- Soft deletes: Yes

**Proceed with sync engine design?**
```

#### 2.1 Sync Architecture

```swift
// File: Core/Sync/SyncEngine.swift

import Foundation
import Observation
import Network

@Observable
final class SyncEngine {
    enum SyncState: Equatable {
        case idle
        case syncing
        case error(String)
        case offline
    }

    private(set) var state: SyncState = .idle
    private(set) var lastSyncDate: Date?
    private(set) var pendingChanges: Int = 0

    private let networkMonitor = NWPathMonitor()
    private let monitorQueue = DispatchQueue(label: "sync.network")
    private var isConnected = false

    init() {
        startNetworkMonitoring()
    }

    private func startNetworkMonitoring() {
        networkMonitor.pathUpdateHandler = { [weak self] path in
            let wasOffline = self?.isConnected == false
            self?.isConnected = path.status == .satisfied

            if wasOffline && path.status == .satisfied {
                Task { await self?.syncPendingChanges() }
            }

            Task { @MainActor in
                if path.status != .satisfied {
                    self?.state = .offline
                }
            }
        }
        networkMonitor.start(queue: monitorQueue)
    }

    func syncPendingChanges() async {
        guard isConnected else {
            state = .offline
            return
        }

        state = .syncing

        do {
            // 1. Push local changes to cloud
            try await pushLocalChanges()

            // 2. Pull remote changes
            try await pullRemoteChanges()

            // 3. Resolve conflicts
            try await resolveConflicts()

            state = .idle
            lastSyncDate = .now
            pendingChanges = 0
        } catch {
            state = .error(error.localizedDescription)
        }
    }

    private func pushLocalChanges() async throws {
        // Fetch records where needsSync == true
        // Push to CloudKit/backend
        // Mark as synced on success
    }

    private func pullRemoteChanges() async throws {
        // Fetch changes since lastSyncDate
        // Merge into local store
    }

    private func resolveConflicts() async throws {
        // Apply conflict resolution strategy
    }
}
```

#### 2.2 Conflict Resolution Strategies

```swift
// File: Core/Sync/ConflictResolver.swift

enum ConflictResolutionStrategy {
    /// Most recent modification wins (simplest, good for single-user)
    case lastWriteWins

    /// Merge field-by-field (complex but preserves more data)
    case fieldLevelMerge

    /// Present both versions to user (safest, worst UX)
    case userChoice

    /// Custom per-model resolution logic
    case custom((Any, Any) -> Any)
}

struct ConflictResolver {
    let strategy: ConflictResolutionStrategy

    func resolve<T: Syncable>(local: T, remote: T) -> T {
        switch strategy {
        case .lastWriteWins:
            return local.modifiedAt > remote.modifiedAt ? local : remote

        case .fieldLevelMerge:
            // Merge non-conflicting fields, use latest for conflicts
            return mergeFields(local: local, remote: remote)

        case .userChoice:
            // Store both, flag for user resolution
            return local // Placeholder -- UI handles this

        case .custom(let resolver):
            return resolver(local, remote) as! T
        }
    }

    private func mergeFields<T: Syncable>(local: T, remote: T) -> T {
        // Implementation depends on model
        // General approach: compare each field's timestamp
        return local.modifiedAt > remote.modifiedAt ? local : remote
    }
}

protocol Syncable {
    var modifiedAt: Date { get }
    var needsSync: Bool { get set }
    var lastSyncedAt: Date? { get set }
}
```

---

### Phase 3: Network-Aware UI

#### 3.1 Sync Status Indicator

```swift
// File: Shared/Components/SyncStatusView.swift

import SwiftUI

struct SyncStatusView: View {
    let syncEngine: SyncEngine

    var body: some View {
        HStack(spacing: 6) {
            switch syncEngine.state {
            case .idle:
                Image(systemName: "checkmark.circle.fill")
                    .foregroundStyle(.green)
                Text("Synced")
            case .syncing:
                ProgressView()
                    .controlSize(.small)
                Text("Syncing...")
            case .offline:
                Image(systemName: "wifi.slash")
                    .foregroundStyle(.orange)
                Text("Offline")
                if syncEngine.pendingChanges > 0 {
                    Text("(\(syncEngine.pendingChanges) pending)")
                }
            case .error(let message):
                Image(systemName: "exclamationmark.triangle.fill")
                    .foregroundStyle(.red)
                Text(message)
                    .lineLimit(1)
            }
        }
        .font(.caption)
        .foregroundStyle(.secondary)
        .accessibilityElement(children: .combine)
        .accessibilityLabel(syncAccessibilityLabel)
    }

    private var syncAccessibilityLabel: String {
        switch syncEngine.state {
        case .idle: "All changes synced"
        case .syncing: "Syncing changes"
        case .offline: "Offline, \(syncEngine.pendingChanges) changes pending"
        case .error(let msg): "Sync error: \(msg)"
        }
    }
}
```

#### 3.2 Optimistic UI Pattern

```swift
// File: Features/Notes/NoteEditorViewModel.swift

@Observable
final class NoteEditorViewModel {
    private let context: ModelContext
    private let syncEngine: SyncEngine

    func saveNote(_ note: Note) {
        // 1. Save locally IMMEDIATELY (optimistic)
        note.markModified()
        try? context.save()
        // UI reflects change instantly

        // 2. Trigger background sync (non-blocking)
        Task.detached(priority: .utility) { [syncEngine] in
            await syncEngine.syncPendingChanges()
        }
    }

    func deleteNote(_ note: Note) {
        // Soft delete for sync
        note.isDeleted = true
        note.markModified()
        try? context.save()

        // Sync deletion
        Task.detached(priority: .utility) { [syncEngine] in
            await syncEngine.syncPendingChanges()
        }
    }
}
```

---

### Phase 4: Background Sync

#### 4.1 Background App Refresh

```swift
// File: Core/Sync/BackgroundSyncScheduler.swift

import BackgroundTasks

enum BackgroundSyncScheduler {
    static let syncTaskIdentifier = "com.app.sync"

    static func register() {
        BGTaskScheduler.shared.register(
            forTaskWithIdentifier: syncTaskIdentifier,
            using: nil
        ) { task in
            handleSync(task: task as! BGAppRefreshTask)
        }
    }

    static func scheduleSync() {
        let request = BGAppRefreshTaskRequest(identifier: syncTaskIdentifier)
        request.earliestBeginDate = Date(timeIntervalSinceNow: 15 * 60) // 15 min
        try? BGTaskScheduler.shared.submit(request)
    }

    private static func handleSync(task: BGAppRefreshTask) {
        // Schedule next sync
        scheduleSync()

        let syncTask = Task {
            await SyncEngine.shared.syncPendingChanges()
        }

        task.expirationHandler = {
            syncTask.cancel()
        }

        Task {
            await syncTask.value
            task.setTaskCompleted(success: true)
        }
    }
}
```

#### 4.2 Push Notification Triggered Sync

```swift
// File: App/AppDelegate.swift

import UIKit
import CloudKit

class AppDelegate: NSObject, UIApplicationDelegate {
    func application(
        _ application: UIApplication,
        didReceiveRemoteNotification userInfo: [AnyHashable: Any]
    ) async -> UIBackgroundFetchResult {

        // CloudKit sends silent push when data changes
        if let notification = CKNotification(fromRemoteNotificationDictionary: userInfo) {
            await SyncEngine.shared.syncPendingChanges()
            return .newData
        }
        return .noData
    }
}
```

---

### Phase 5: Edge Cases and Resilience

**CHECKPOINT 2:** Review sync architecture before addressing edge cases.

```markdown
## Sync Architecture Summary
- Sync engine: Custom / CloudKit automatic
- Conflict strategy: Last-write-wins / Field-merge / User-choice
- Background sync: BGAppRefreshTask + silent push
- Optimistic UI: Yes

**Proceed with edge case handling?**
```

#### 5.1 Edge Case Matrix

| Scenario | Handling |
|----------|---------|
| First launch, no network | App works with empty local store. Sync when connected. |
| iCloud account signed out | Data remains in local store. Sync pauses. No data loss. |
| iCloud account changed | Reset sync anchors. Re-sync from new account. Offer to keep local data. |
| Quota exceeded | Pause sync, notify user, prioritize recent data. |
| Schema migration with unsynced data | Migrate local schema first, then sync. Never lose unsynced changes. |
| Conflicting deletes | If A deletes item that B edited, deletion wins (configurable). |
| Large file sync (photos, attachments) | Sync metadata immediately, download assets on demand. |
| Airplane mode toggle rapid | Debounce network state changes (2-second delay). |

#### 5.2 Data Integrity Guards

```swift
// File: Core/Sync/SyncGuards.swift

enum SyncGuard {
    /// Verify local data integrity before sync
    static func preSyncCheck(context: ModelContext) throws {
        // Check for orphaned records
        let orphanedAttachments = try context.fetch(
            FetchDescriptor<Attachment>(
                predicate: #Predicate { $0.note == nil && !$0.isDeleted }
            )
        )
        for attachment in orphanedAttachments {
            attachment.isDeleted = true
        }

        // Check for duplicate IDs (sync corruption indicator)
        // Log but don't crash -- resolve on next sync
    }

    /// Verify sync didn't corrupt data
    static func postSyncCheck(context: ModelContext) throws {
        // Verify relationship integrity
        // Check for records stuck in needsSync state
        // Log metrics for monitoring
    }
}
```

---

## Expected Output

```
Offline-First Architecture Document
├── Data Layer
│   ├── Persistence stack configuration
│   ├── Model design with sync metadata
│   └── Soft delete strategy
├── Sync Engine
│   ├── Push/pull sync flow
│   ├── Conflict resolution strategy
│   └── Network monitoring
├── UI Layer
│   ├── Sync status indicators
│   ├── Optimistic UI patterns
│   └── Offline-aware components
├── Background Sync
│   ├── BGAppRefreshTask configuration
│   └── Silent push notification handling
└── Edge Cases
    ├── iCloud account scenarios
    ├── Schema migration with pending sync
    └── Data integrity guards
```

---

## Example Interaction

**User:** "Building a note-taking app. Needs to work fully offline, sync across iPhone and iPad via iCloud. iOS 17+."

**Assistant:**

**Recommended Stack:** SwiftData with `cloudKitDatabase: .automatic`

This gives you CloudKit sync with minimal custom code. SwiftData handles:
- Automatic push/pull sync via NSPersistentCloudKitContainer under the hood
- Conflict resolution (last-write-wins by default)
- Silent push notifications for near-real-time sync

**What you still need to build:**
1. Sync status UI (SwiftData doesn't expose sync state -- use `NSPersistentCloudKitContainer.eventChangedNotification`)
2. Soft delete pattern (CloudKit doesn't truly delete, so your model should match)
3. Network-aware UI showing pending changes count
4. Large attachment handling (store images as `@Attribute(.externalStorage)` for CloudKit compatibility)

---

## Techniques Used

- **ST-01** (Clear Objective): Design complete offline-first architecture
- **ST-02** (Sequential Instructions): Five-phase design from data layer to edge cases
- **RT-02** (Multi-Dimensional Analysis): Covers persistence, sync, UI, background, and resilience

---

## Related Prompts

- [ios_architecture_selection.md](ios_architecture_selection.md) - Architecture impacts offline-first design
- [ios_data_retention_policy_design.md](ios_data_retention_policy_design.md) - Data lifecycle management
- [ios_tech_stack_selection.md](ios_tech_stack_selection.md) - Persistence technology selection

---

## Customization Guide

### For Custom Backend Sync (Not CloudKit)
Replace CloudKit layer with custom sync protocol. Implement operational transform or CRDTs for collaborative editing. Use WebSocket for real-time sync, HTTP for batch sync.

### For Apple Watch Companion
Use Watch Connectivity framework (`WCSession`) for direct iPhone-Watch sync. Watch uses its own local store, syncing via the phone rather than directly to CloudKit.

### For Healthcare/Regulated Data
Add encryption at rest (Core Data + NSFileProtection), audit logging for all sync operations, and ensure no PHI leaves the device without explicit consent. Consider on-device-only mode as a fallback.
