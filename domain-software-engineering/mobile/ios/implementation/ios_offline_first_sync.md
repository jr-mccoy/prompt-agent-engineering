---
title: "iOS Offline-First Sync"
category: mobile-development
description: "Build offline-first architecture with Core Data or SwiftData plus CloudKit sync, conflict resolution, CKSubscription for real-time updates, and network reachability monitoring."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-02
  - NE-02
difficulty: advanced
tags:
  - ios
  - swift
  - offline-first
  - cloudkit
  - core-data
  - swiftdata
  - sync
  - mobile-development
updated: "2026-03-19"
---

# iOS Offline-First Sync

**Objective:** Build an offline-first architecture using Core Data or SwiftData with CloudKit synchronization, robust conflict resolution strategies, CKSubscription for real-time push updates, and network reachability monitoring for seamless online/offline transitions.

**When to Use:** Use this prompt when building apps that must work fully offline and sync data when connectivity is available. Ideal for note-taking apps, task managers, field data collection, or any app where users operate in unreliable network conditions.

**Prompt Type:** Comprehensive (450-500 lines)

---

## Context Gathering

Before implementing offline-first sync, gather essential context:

1. **Data Model:**
   - "What entities need to sync across devices?"
   - "Are there relationships between synced entities?"
   - "What is the expected data volume per user?"

2. **Sync Requirements:**
   - "Should sync be real-time, periodic, or on-demand?"
   - "Is CloudKit acceptable or do you need a custom backend?"
   - "How should conflicts be resolved (last-writer-wins, merge, user choice)?"

3. **User Experience:**
   - "Should users see sync status indicators?"
   - "How should merge conflicts be presented?"
   - "What happens when quota is exceeded?"

4. **Existing Infrastructure:**
   - "Is iCloud entitlement already configured?"
   - "Is there an existing Core Data or SwiftData stack?"
   - "Are there background task registrations for sync?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before implementing ANY code, you MUST:**

1. **Enable iCloud capability** - CloudKit requires the iCloud entitlement with CloudKit checked.
2. **Configure the CloudKit container** - Set up the container identifier in Apple Developer portal.
3. **Test with multiple devices** - Offline-first must be validated across device and account scenarios.
4. **Handle iCloud account changes** - Users can sign out of iCloud or switch accounts.
5. **Respect storage quotas** - CloudKit has per-user storage limits.

### False-Positive Prevention

- ❌ Do NOT assume network is always available - design for offline-first
- ❌ Do NOT silently drop data on sync conflicts - always have a resolution strategy
- ❌ Do NOT sync sensitive data without encryption consideration
- ❌ Do NOT ignore CKError cases (quotaExceeded, userDeletedZone, changeTokenExpired)
- ❌ Do NOT poll for changes when CKSubscription can push updates
- ✅ DO queue mutations locally first, then sync
- ✅ DO implement exponential backoff for sync retries
- ✅ DO monitor network reachability to trigger sync opportunistically
- ✅ DO handle iCloud account unavailable gracefully (app still works locally)

---

### Phase 1: NSPersistentCloudKitContainer Setup

#### 1.1 CloudKit-Enabled Core Data Stack

```swift
// File: Data/Persistence/CloudKitSyncStack.swift

import CoreData
import CloudKit
import OSLog

final class CloudKitSyncStack {
    static let shared = CloudKitSyncStack()

    let persistentContainer: NSPersistentCloudKitContainer
    private let logger = Logger(subsystem: "com.example.app", category: "CloudKitSync")

    var viewContext: NSManagedObjectContext {
        persistentContainer.viewContext
    }

    init(inMemory: Bool = false) {
        persistentContainer = NSPersistentCloudKitContainer(name: "DataModel")

        // Configure CloudKit sync
        guard let description = persistentContainer.persistentStoreDescriptions.first else {
            fatalError("No persistent store descriptions found")
        }

        if inMemory {
            description.url = URL(fileURLWithPath: "/dev/null")
            description.cloudKitContainerOptions = nil
        } else {
            let cloudKitOptions = NSPersistentCloudKitContainerOptions(
                containerIdentifier: "iCloud.com.example.app"
            )
            cloudKitOptions.databaseScope = .private
            description.cloudKitContainerOptions = cloudKitOptions
        }

        // Enable history tracking (required for CloudKit sync)
        description.setOption(true as NSNumber,
            forKey: NSPersistentHistoryTrackingKey)
        description.setOption(true as NSNumber,
            forKey: NSPersistentStoreRemoteChangeNotificationPostOptionKey)

        persistentContainer.loadPersistentStores { [weak self] description, error in
            if let error {
                self?.logger.error("Store failed to load: \(error)")
                fatalError("Core Data store failed: \(error)")
            }
            self?.logger.info("Store loaded: \(description.url?.absoluteString ?? "unknown")")
        }

        // Auto-merge remote changes into view context
        viewContext.automaticallyMergesChangesFromParent = true
        viewContext.mergePolicy = NSMergeByPropertyObjectTrumpMergePolicy
        viewContext.name = "viewContext"

        // Listen for remote changes
        NotificationCenter.default.addObserver(
            self,
            selector: #selector(handleRemoteChange),
            name: .NSPersistentStoreRemoteChange,
            object: persistentContainer.persistentStoreCoordinator
        )
    }

    @objc private func handleRemoteChange(_ notification: Notification) {
        logger.info("Remote change received from CloudKit")
        // Process persistent history to determine what changed
        Task { @MainActor in
            NotificationCenter.default.post(name: .didReceiveRemoteChanges, object: nil)
        }
    }

    func newBackgroundContext() -> NSManagedObjectContext {
        let context = persistentContainer.newBackgroundContext()
        context.mergePolicy = NSMergeByPropertyObjectTrumpMergePolicy
        context.transactionAuthor = "backgroundSync"
        return context
    }
}

extension Notification.Name {
    static let didReceiveRemoteChanges = Notification.Name("didReceiveRemoteChanges")
}
```

---

### Phase 2: Conflict Resolution

**CHECKPOINT 1:** Confirm CloudKit container setup before implementing conflict resolution.

#### 2.1 Conflict Resolution Strategies

```swift
// File: Data/Sync/ConflictResolver.swift

import CoreData
import OSLog

enum ConflictStrategy {
    case serverWins      // Remote changes take priority
    case clientWins      // Local changes take priority
    case latestWins      // Most recent timestamp wins
    case merge           // Field-level merge
    case askUser         // Present conflict to user
}

final class ConflictResolver {
    private let logger = Logger(subsystem: "com.example.app", category: "Conflict")
    private let defaultStrategy: ConflictStrategy

    init(strategy: ConflictStrategy = .latestWins) {
        self.defaultStrategy = strategy
    }

    func resolve<T: SyncableEntity>(
        local: T,
        remote: T,
        strategy: ConflictStrategy? = nil
    ) -> T {
        let resolveStrategy = strategy ?? defaultStrategy

        switch resolveStrategy {
        case .serverWins:
            logger.info("Conflict resolved: server wins for \(T.entityName) \(local.syncID)")
            return remote

        case .clientWins:
            logger.info("Conflict resolved: client wins for \(T.entityName) \(local.syncID)")
            return local

        case .latestWins:
            if local.modifiedAt > remote.modifiedAt {
                logger.info("Conflict resolved: local is newer for \(T.entityName)")
                return local
            } else {
                logger.info("Conflict resolved: remote is newer for \(T.entityName)")
                return remote
            }

        case .merge:
            logger.info("Conflict resolved: merging fields for \(T.entityName)")
            return mergeFields(local: local, remote: remote)

        case .askUser:
            // Return local for now; UI will present the conflict
            logger.info("Conflict queued for user resolution: \(T.entityName)")
            return local
        }
    }

    private func mergeFields<T: SyncableEntity>(local: T, remote: T) -> T {
        // Field-level merge: take the most recently modified field
        var merged = local
        for field in T.mergeableFields {
            if remote.fieldModifiedAt(field) > local.fieldModifiedAt(field) {
                merged.setField(field, from: remote)
            }
        }
        return merged
    }
}

// Protocol for syncable entities
protocol SyncableEntity {
    static var entityName: String { get }
    static var mergeableFields: [String] { get }
    var syncID: String { get }
    var modifiedAt: Date { get }
    func fieldModifiedAt(_ field: String) -> Date
    mutating func setField(_ field: String, from other: Self)
}
```

#### 2.2 Sync Queue for Offline Mutations

```swift
// File: Data/Sync/SyncQueue.swift

import SwiftData
import Foundation
import OSLog

@Model
final class PendingSyncOperation {
    var id: UUID
    var entityType: String
    var entityID: String
    var operationType: String // "create", "update", "delete"
    var payload: Data? // JSON-encoded changes
    var createdAt: Date
    var retryCount: Int
    var lastError: String?

    init(entityType: String, entityID: String, operation: String, payload: Data? = nil) {
        self.id = UUID()
        self.entityType = entityType
        self.entityID = entityID
        self.operationType = operation
        self.payload = payload
        self.createdAt = .now
        self.retryCount = 0
    }
}

actor SyncQueue {
    private let logger = Logger(subsystem: "com.example.app", category: "SyncQueue")
    private let modelContext: ModelContext
    private let maxRetries = 5

    init(modelContainer: ModelContainer) {
        self.modelContext = ModelContext(modelContainer)
    }

    func enqueue(entityType: String, entityID: String, operation: String, payload: Data? = nil) throws {
        let op = PendingSyncOperation(
            entityType: entityType,
            entityID: entityID,
            operation: operation,
            payload: payload
        )
        modelContext.insert(op)
        try modelContext.save()
        logger.info("Queued \(operation) for \(entityType):\(entityID)")
    }

    func pendingOperations() throws -> [PendingSyncOperation] {
        let descriptor = FetchDescriptor<PendingSyncOperation>(
            predicate: #Predicate { $0.retryCount < 5 },
            sortBy: [SortDescriptor(\.createdAt)]
        )
        return try modelContext.fetch(descriptor)
    }

    func markCompleted(_ operation: PendingSyncOperation) throws {
        modelContext.delete(operation)
        try modelContext.save()
    }

    func markFailed(_ operation: PendingSyncOperation, error: String) throws {
        operation.retryCount += 1
        operation.lastError = error
        try modelContext.save()
        logger.warning("Sync operation failed (attempt \(operation.retryCount)): \(error)")
    }
}
```

---

### Phase 3: Network Reachability

#### 3.1 Network Monitor

```swift
// File: Data/Sync/NetworkMonitor.swift

import Network
import OSLog

@Observable
final class NetworkMonitor {
    static let shared = NetworkMonitor()

    private(set) var isConnected = false
    private(set) var connectionType: ConnectionType = .unknown

    private let monitor = NWPathMonitor()
    private let queue = DispatchQueue(label: "NetworkMonitor")
    private let logger = Logger(subsystem: "com.example.app", category: "Network")

    enum ConnectionType {
        case wifi, cellular, wiredEthernet, unknown
    }

    func start() {
        monitor.pathUpdateHandler = { [weak self] path in
            let wasConnected = self?.isConnected ?? false
            self?.isConnected = path.status == .satisfied

            if path.usesInterfaceType(.wifi) {
                self?.connectionType = .wifi
            } else if path.usesInterfaceType(.cellular) {
                self?.connectionType = .cellular
            } else if path.usesInterfaceType(.wiredEthernet) {
                self?.connectionType = .wiredEthernet
            } else {
                self?.connectionType = .unknown
            }

            // Trigger sync when connectivity is restored
            if !wasConnected && path.status == .satisfied {
                self?.logger.info("Network restored, triggering sync")
                Task {
                    await SyncCoordinator.shared.syncNow()
                }
            }
        }
        monitor.start(queue: queue)
    }

    func stop() {
        monitor.cancel()
    }
}
```

---

### Phase 4: Sync Coordinator

```swift
// File: Data/Sync/SyncCoordinator.swift

import Foundation
import OSLog

actor SyncCoordinator {
    static let shared = SyncCoordinator()

    enum SyncState: Equatable {
        case idle
        case syncing
        case error(String)
        case completed(Date)
    }

    private(set) var state: SyncState = .idle
    private let logger = Logger(subsystem: "com.example.app", category: "Sync")
    private var isSyncing = false

    func syncNow() async {
        guard !isSyncing else {
            logger.info("Sync already in progress, skipping")
            return
        }

        guard NetworkMonitor.shared.isConnected else {
            logger.info("No network, deferring sync")
            return
        }

        isSyncing = true
        state = .syncing

        do {
            // Step 1: Push local changes
            try await pushPendingChanges()

            // Step 2: Pull remote changes
            try await pullRemoteChanges()

            state = .completed(.now)
            logger.info("Sync completed successfully")
        } catch {
            state = .error(error.localizedDescription)
            logger.error("Sync failed: \(error)")
        }

        isSyncing = false
    }

    private func pushPendingChanges() async throws {
        // Process sync queue
        logger.info("Pushing pending changes...")
    }

    private func pullRemoteChanges() async throws {
        // Fetch from CloudKit / API
        logger.info("Pulling remote changes...")
    }
}
```

---

### Phase 5: Sync Status UI

```swift
// File: Features/Shared/SyncStatusView.swift

import SwiftUI

struct SyncStatusView: View {
    let state: SyncCoordinator.SyncState
    @Environment(NetworkMonitor.self) private var networkMonitor

    var body: some View {
        HStack(spacing: 6) {
            statusIcon
            statusText
        }
        .font(.caption)
        .foregroundStyle(.secondary)
        .padding(.horizontal, 12)
        .padding(.vertical, 6)
        .background(.ultraThinMaterial, in: Capsule())
    }

    @ViewBuilder
    private var statusIcon: some View {
        switch state {
        case .idle:
            if networkMonitor.isConnected {
                Image(systemName: "checkmark.icloud")
                    .foregroundStyle(.green)
            } else {
                Image(systemName: "icloud.slash")
                    .foregroundStyle(.orange)
            }
        case .syncing:
            ProgressView()
                .controlSize(.mini)
        case .error:
            Image(systemName: "exclamationmark.icloud")
                .foregroundStyle(.red)
        case .completed:
            Image(systemName: "checkmark.icloud")
                .foregroundStyle(.green)
        }
    }

    private var statusText: some View {
        Group {
            switch state {
            case .idle:
                Text(networkMonitor.isConnected ? "Up to date" : "Offline")
            case .syncing:
                Text("Syncing...")
            case .error(let message):
                Text(message)
            case .completed(let date):
                Text("Synced \(date.formatted(.relative(presentation: .named)))")
            }
        }
    }
}
```

---

## Expected Output

### File Structure

```
Data/
├── Persistence/
│   └── CloudKitSyncStack.swift       # NSPersistentCloudKitContainer
└── Sync/
    ├── ConflictResolver.swift         # Conflict resolution strategies
    ├── SyncQueue.swift                # Offline mutation queue
    ├── NetworkMonitor.swift           # NWPathMonitor wrapper
    └── SyncCoordinator.swift          # Orchestrates push/pull

Features/Shared/
└── SyncStatusView.swift              # UI sync indicator
```

### Implementation Checklist

- [ ] NSPersistentCloudKitContainer with history tracking
- [ ] Automatic merge from remote changes
- [ ] Conflict resolution with configurable strategies
- [ ] Offline mutation queue (enqueue, retry, dequeue)
- [ ] NWPathMonitor network reachability
- [ ] Auto-sync on connectivity restoration
- [ ] Sync coordinator with state tracking
- [ ] Sync status UI component
- [ ] iCloud entitlement configured
- [ ] Background task for periodic sync

---

## Example Interaction

**User:** "My note-taking app needs to sync notes across devices with offline support."

**Assistant:**
```swift
// 1. Use NSPersistentCloudKitContainer for automatic sync
let container = NSPersistentCloudKitContainer(name: "Notes")
// CloudKit handles push/pull automatically

// 2. For offline edits, the local Core Data store works without network
// Changes queue automatically and sync when connectivity returns

// 3. Add conflict resolution for simultaneous edits:
let resolver = ConflictResolver(strategy: .latestWins)
// For notes, field-level merge is often better:
let resolver = ConflictResolver(strategy: .merge)
// Title uses latest timestamp, body uses operational transform or last-writer-wins
```

---

## Techniques Used

- **ST-01** (Clear Objective): Focused on offline-first architecture
- **ST-02** (Sequential Instructions): Phased from persistence to UI
- **RT-02** (Multi-Dimensional Analysis): CloudKit, conflicts, queue, network
- **RT-05** (Edge Case Identification): Offline, conflicts, quota, account changes
- **DS-02** (Progressive Disclosure): From basic sync to advanced conflict resolution
- **NE-02** (Phased Workflow): Clear build phases with checkpoints

---

## Related Prompts

- [ios_cloudkit_integration.md](ios_cloudkit_integration.md) - Direct CloudKit API usage
- [ios_data_layer_implementation.md](ios_data_layer_implementation.md) - Local persistence layer
- [ios_background_tasks.md](ios_background_tasks.md) - Background sync scheduling
- [ios_api_integration.md](ios_api_integration.md) - Custom backend sync alternative

---

## Customization Guide

### For Custom Backend Sync

Replace CloudKit with REST API:
```swift
actor CustomSyncEngine {
    func push(changes: [SyncChange]) async throws {
        let response = try await apiClient.request(
            SyncEndpoints.push(changes: changes),
            responseType: SyncResponse.self
        )
        // Apply server-resolved conflicts
    }

    func pull(since token: String?) async throws -> SyncResponse {
        try await apiClient.request(
            SyncEndpoints.pull(sinceToken: token),
            responseType: SyncResponse.self
        )
    }
}
```

### For Shared Database Sync

Use CKDatabaseScope.shared for collaborative data:
```swift
let options = NSPersistentCloudKitContainerOptions(
    containerIdentifier: "iCloud.com.example.app"
)
options.databaseScope = .shared // Enable sharing
```
