---
title: "iOS CloudKit Integration"
category: mobile-development
description: "Implement CloudKit with container setup, record types, CKQuery operations, subscriptions, share participants, and public/private/shared database management."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - ST-03
  - NE-02
difficulty: intermediate
tags:
  - ios
  - swift
  - cloudkit
  - icloud
  - sync
  - sharing
  - mobile-development
updated: "2026-03-19"
---

# iOS CloudKit Integration

**Objective:** Implement CloudKit integration including container setup, record type definitions, CKQuery operations, subscriptions for real-time updates, share participants for collaboration, and proper management of public, private, and shared databases.

**When to Use:** Use this prompt when building CloudKit-powered features such as user data sync, public content feeds, or collaborative document sharing. Ideal for apps that need iCloud-backed storage without managing a custom backend. Best used after data model design is complete.

**Prompt Type:** Comprehensive (400-450 lines)

---

## Context Gathering

Before implementing CloudKit, gather essential context:

1. **Data Model:**
   - "What record types need to be stored in CloudKit?"
   - "What fields and relationships exist between records?"
   - "Should data be private (per-user), public (all users), or shared?"

2. **Capabilities:**
   - "Is the iCloud entitlement configured in the project?"
   - "Has the CloudKit container been created in Apple Developer portal?"
   - "Do you need CloudKit Dashboard schema deployment?"

3. **Features:**
   - "Do users need to share records with other users?"
   - "Should the app receive push notifications for record changes?"
   - "Is there a web or Android counterpart that needs CloudKit JS?"

4. **Scale:**
   - "How many records per user are expected?"
   - "What is the expected query frequency?"
   - "Are there large assets (images, files) to store?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before implementing ANY code, you MUST:**

1. **Enable iCloud capability** with CloudKit checked in Xcode capabilities.
2. **Create CloudKit container** in Apple Developer portal matching the container identifier.
3. **Define schema in CloudKit Dashboard** (development environment) before coding.
4. **Deploy schema to production** before App Store release.
5. **Handle CKError exhaustively** - CloudKit has many error types requiring different handling.

### False-Positive Prevention

- ❌ Do NOT assume CloudKit operations always succeed - network errors are common
- ❌ Do NOT fetch all records without cursor-based pagination
- ❌ Do NOT store large files as CKRecord fields (use CKAsset)
- ❌ Do NOT ignore CKError.serverRecordChanged for conflict resolution
- ❌ Do NOT hardcode record type names as strings without constants
- ✅ DO use CKModifyRecordsOperation for batch saves
- ✅ DO implement cursor-based pagination for large result sets
- ✅ DO handle partial failures in batch operations
- ✅ DO use CKFetchRecordZoneChangesOperation for incremental sync

---

### Phase 1: Container & Schema Setup

#### 1.1 CloudKit Manager

```swift
// File: CloudKit/CloudKitManager.swift

import CloudKit
import OSLog

actor CloudKitManager {
    static let shared = CloudKitManager()

    private let container: CKContainer
    private let privateDB: CKDatabase
    private let publicDB: CKDatabase
    private let sharedDB: CKDatabase
    private let logger = Logger(subsystem: "com.example.app", category: "CloudKit")

    // Record type constants
    enum RecordType {
        static let note = "Note"
        static let folder = "Folder"
        static let attachment = "Attachment"
    }

    // Custom zone for private database
    static let appZone = CKRecordZone(zoneName: "AppZone")

    init(containerID: String = "iCloud.com.example.app") {
        self.container = CKContainer(identifier: containerID)
        self.privateDB = container.privateCloudDatabase
        self.publicDB = container.publicCloudDatabase
        self.sharedDB = container.sharedCloudDatabase
    }

    /// One-time setup: create custom zone
    func setup() async throws {
        do {
            _ = try await privateDB.modifyRecordZones(
                saving: [Self.appZone],
                deleting: []
            )
            logger.info("Custom zone created")
        } catch let error as CKError where error.code == .serverRejectedRequest {
            // Zone already exists - that's fine
            logger.info("Custom zone already exists")
        }
    }

    /// Check iCloud account status
    func checkAccountStatus() async throws -> CKAccountStatus {
        try await container.accountStatus()
    }
}
```

#### 1.2 Record Type Definitions

```swift
// File: CloudKit/Models/NoteRecord.swift

import CloudKit

struct NoteRecord {
    static let recordType = CloudKitManager.RecordType.note

    // Field keys
    enum Field: String {
        case title
        case body
        case folderRef = "folder"
        case isPinned
        case modifiedAt
        case tags
        case coverImage
    }

    let record: CKRecord

    var id: CKRecord.ID { record.recordID }
    var title: String { record[Field.title.rawValue] as? String ?? "" }
    var body: String { record[Field.body.rawValue] as? String ?? "" }
    var isPinned: Bool { record[Field.isPinned.rawValue] as? Bool ?? false }
    var modifiedAt: Date { record[Field.modifiedAt.rawValue] as? Date ?? record.modificationDate ?? .now }
    var tags: [String] { record[Field.tags.rawValue] as? [String] ?? [] }
    var folderReference: CKRecord.Reference? { record[Field.folderRef.rawValue] as? CKRecord.Reference }

    var coverImageAsset: CKAsset? { record[Field.coverImage.rawValue] as? CKAsset }
    var coverImageURL: URL? { coverImageAsset?.fileURL }

    init(record: CKRecord) {
        self.record = record
    }

    init(
        title: String,
        body: String,
        folderID: CKRecord.ID? = nil,
        zone: CKRecordZone.ID = CloudKitManager.appZone.zoneID
    ) {
        let recordID = CKRecord.ID(zoneID: zone)
        self.record = CKRecord(recordType: Self.recordType, recordID: recordID)
        record[Field.title.rawValue] = title
        record[Field.body.rawValue] = body
        record[Field.modifiedAt.rawValue] = Date.now
        record[Field.isPinned.rawValue] = false

        if let folderID {
            record[Field.folderRef.rawValue] = CKRecord.Reference(
                recordID: folderID,
                action: .none
            )
        }
    }

    mutating func update(title: String? = nil, body: String? = nil, isPinned: Bool? = nil) {
        if let title { record[Field.title.rawValue] = title }
        if let body { record[Field.body.rawValue] = body }
        if let isPinned { record[Field.isPinned.rawValue] = isPinned }
        record[Field.modifiedAt.rawValue] = Date.now
    }

    mutating func setCoverImage(fileURL: URL) {
        record[Field.coverImage.rawValue] = CKAsset(fileURL: fileURL)
    }
}
```

---

### Phase 2: CRUD Operations

**CHECKPOINT 1:** Confirm container and zone setup before CRUD.

#### 2.1 Save & Fetch

```swift
// File: CloudKit/CloudKitManager+CRUD.swift

import CloudKit

extension CloudKitManager {

    // MARK: - Save

    func save(_ record: CKRecord, to database: DatabaseScope = .private) async throws -> CKRecord {
        let db = self.database(for: database)
        do {
            let saved = try await db.save(record)
            logger.info("Saved record: \(saved.recordID.recordName)")
            return saved
        } catch let error as CKError {
            throw mapError(error)
        }
    }

    func batchSave(_ records: [CKRecord], to database: DatabaseScope = .private) async throws -> [CKRecord] {
        let db = self.database(for: database)
        let (saved, _) = try await db.modifyRecords(
            saving: records,
            deleting: [],
            savePolicy: .changedKeys,
            atomically: false
        )
        logger.info("Batch saved \(saved.count) records")
        return saved.map(\.value).compactMap { try? $0.get() }
    }

    // MARK: - Fetch

    func fetch(recordID: CKRecord.ID, from database: DatabaseScope = .private) async throws -> CKRecord {
        let db = self.database(for: database)
        return try await db.record(for: recordID)
    }

    func fetchAll(
        recordType: String,
        predicate: NSPredicate = NSPredicate(value: true),
        sortDescriptors: [NSSortDescriptor] = [],
        limit: Int = 100,
        from database: DatabaseScope = .private
    ) async throws -> [CKRecord] {
        let db = self.database(for: database)
        let query = CKQuery(recordType: recordType, predicate: predicate)
        query.sortDescriptors = sortDescriptors

        var allRecords: [CKRecord] = []
        var cursor: CKQueryOperation.Cursor?

        // First page
        let (results, nextCursor) = try await db.records(
            matching: query,
            inZoneWith: database == .private ? Self.appZone.zoneID : nil,
            desiredKeys: nil,
            resultsLimit: limit
        )

        allRecords.append(contentsOf: results.compactMap { try? $0.1.get() })
        cursor = nextCursor

        // Paginate
        while let currentCursor = cursor {
            let (moreResults, nextCursor) = try await db.records(
                continuingMatchFrom: currentCursor,
                resultsLimit: limit
            )
            allRecords.append(contentsOf: moreResults.compactMap { try? $0.1.get() })
            cursor = nextCursor
        }

        logger.info("Fetched \(allRecords.count) \(recordType) records")
        return allRecords
    }

    // MARK: - Delete

    func delete(recordID: CKRecord.ID, from database: DatabaseScope = .private) async throws {
        let db = self.database(for: database)
        try await db.deleteRecord(withID: recordID)
        logger.info("Deleted record: \(recordID.recordName)")
    }

    // MARK: - Query

    func queryNotes(
        inFolder folderID: CKRecord.ID? = nil,
        searchText: String? = nil
    ) async throws -> [NoteRecord] {
        var predicateComponents: [NSPredicate] = []

        if let folderID {
            let ref = CKRecord.Reference(recordID: folderID, action: .none)
            predicateComponents.append(
                NSPredicate(format: "folder == %@", ref)
            )
        }

        if let searchText, !searchText.isEmpty {
            predicateComponents.append(
                NSPredicate(format: "self contains %@", searchText)
            )
        }

        let predicate: NSPredicate
        if predicateComponents.isEmpty {
            predicate = NSPredicate(value: true)
        } else {
            predicate = NSCompoundPredicate(andPredicateWithSubpredicates: predicateComponents)
        }

        let records = try await fetchAll(
            recordType: NoteRecord.recordType,
            predicate: predicate,
            sortDescriptors: [NSSortDescriptor(key: "modifiedAt", ascending: false)]
        )

        return records.map { NoteRecord(record: $0) }
    }

    // MARK: - Helpers

    enum DatabaseScope { case `private`, `public`, shared }

    private func database(for scope: DatabaseScope) -> CKDatabase {
        switch scope {
        case .private: return privateDB
        case .public: return publicDB
        case .shared: return sharedDB
        }
    }

    private func mapError(_ error: CKError) -> CloudKitError {
        switch error.code {
        case .networkFailure, .networkUnavailable:
            return .networkUnavailable
        case .notAuthenticated:
            return .notAuthenticated
        case .quotaExceeded:
            return .quotaExceeded
        case .serverRecordChanged:
            return .conflict(serverRecord: error.serverRecord)
        case .unknownItem:
            return .recordNotFound
        case .limitExceeded:
            return .batchTooLarge
        default:
            return .unknown(error.localizedDescription)
        }
    }
}

enum CloudKitError: LocalizedError {
    case networkUnavailable
    case notAuthenticated
    case quotaExceeded
    case conflict(serverRecord: CKRecord?)
    case recordNotFound
    case batchTooLarge
    case unknown(String)

    var errorDescription: String? {
        switch self {
        case .networkUnavailable: return "No network connection"
        case .notAuthenticated: return "Please sign in to iCloud"
        case .quotaExceeded: return "iCloud storage is full"
        case .conflict: return "Record was modified by another device"
        case .recordNotFound: return "Record not found"
        case .batchTooLarge: return "Too many records in one operation"
        case .unknown(let msg): return msg
        }
    }
}
```

---

### Phase 3: Subscriptions

#### 3.1 Subscribe to Changes

```swift
// File: CloudKit/CloudKitManager+Subscriptions.swift

import CloudKit

extension CloudKitManager {

    func setupSubscriptions() async throws {
        // Subscribe to Note changes in private DB
        let noteSubscription = CKQuerySubscription(
            recordType: RecordType.note,
            predicate: NSPredicate(value: true),
            subscriptionID: "note-changes",
            options: [.firesOnRecordCreation, .firesOnRecordUpdate, .firesOnRecordDeletion]
        )

        let notificationInfo = CKSubscription.NotificationInfo()
        notificationInfo.shouldSendContentAvailable = true // Silent push
        noteSubscription.notificationInfo = notificationInfo
        noteSubscription.zoneID = Self.appZone.zoneID

        try await privateDB.modifySubscriptions(
            saving: [noteSubscription],
            deleting: []
        )
        logger.info("Subscriptions configured")
    }

    /// Incremental fetch using change tokens
    func fetchChanges(since token: CKServerChangeToken?) async throws -> ChangeSet {
        let zoneID = Self.appZone.zoneID
        var changedRecords: [CKRecord] = []
        var deletedRecordIDs: [CKRecord.ID] = []
        var newToken: CKServerChangeToken?

        let changes = privateDB.recordZoneChanges(
            inZoneWith: zoneID,
            since: token
        )

        for try await change in changes {
            switch change {
            case .changed(let record):
                changedRecords.append(record)
            case .deleted(let recordID, _):
                deletedRecordIDs.append(recordID)
            @unknown default:
                break
            }
        }

        // Get the new token for next fetch
        let zoneChanges = privateDB.recordZoneChanges(inZoneWith: zoneID, since: token)
        // Token is returned via the async sequence completion

        logger.info("Changes: \(changedRecords.count) modified, \(deletedRecordIDs.count) deleted")

        return ChangeSet(
            changed: changedRecords,
            deleted: deletedRecordIDs,
            newToken: newToken
        )
    }
}

struct ChangeSet {
    let changed: [CKRecord]
    let deleted: [CKRecord.ID]
    let newToken: CKServerChangeToken?
}
```

---

### Phase 4: Sharing

#### 4.1 Share Records

```swift
// File: CloudKit/CloudKitManager+Sharing.swift

import CloudKit
import UIKit

extension CloudKitManager {

    /// Create a share for a record
    func share(
        record: CKRecord,
        title: String? = nil,
        permission: CKShare.ParticipantPermission = .readWrite
    ) async throws -> CKShare {
        let share = CKShare(rootRecord: record)
        share[CKShare.SystemFieldKey.title] = (title ?? "Shared Item") as CKRecordValue
        share.publicPermission = .none // Require invitation

        let (savedResults, _) = try await privateDB.modifyRecords(
            saving: [record, share],
            deleting: []
        )

        guard let savedShare = try savedResults[share.recordID]?.get() as? CKShare else {
            throw CloudKitError.unknown("Failed to create share")
        }

        logger.info("Share created: \(savedShare.url?.absoluteString ?? "no URL")")
        return savedShare
    }

    /// Accept a share from a URL
    func acceptShare(metadata: CKShare.Metadata) async throws {
        try await container.accept(metadata)
        logger.info("Share accepted")
    }

    /// Fetch shared records
    func fetchSharedRecords(recordType: String) async throws -> [CKRecord] {
        let zones = try await sharedDB.allRecordZones()

        var allRecords: [CKRecord] = []
        for zone in zones {
            let query = CKQuery(recordType: recordType, predicate: NSPredicate(value: true))
            let (results, _) = try await sharedDB.records(
                matching: query,
                inZoneWith: zone.zoneID
            )
            allRecords.append(contentsOf: results.compactMap { try? $0.1.get() })
        }

        return allRecords
    }
}
```

---

## Expected Output

### File Structure

```
CloudKit/
├── CloudKitManager.swift              # Container + zone setup
├── CloudKitManager+CRUD.swift         # Save, fetch, delete, query
├── CloudKitManager+Subscriptions.swift # Subscriptions + change tokens
├── CloudKitManager+Sharing.swift      # CKShare management
└── Models/
    └── NoteRecord.swift               # Record wrapper types
```

### Implementation Checklist

- [ ] CKContainer initialized with correct identifier
- [ ] Custom CKRecordZone created in private database
- [ ] Record type wrappers with field constants
- [ ] CRUD operations with proper error mapping
- [ ] Cursor-based pagination for large queries
- [ ] CKQuerySubscription for real-time notifications
- [ ] Incremental sync with CKServerChangeToken
- [ ] CKShare creation and acceptance
- [ ] CKAsset for large file storage
- [ ] Exhaustive CKError handling

---

## Example Interaction

**User:** "I need to store user notes in CloudKit with search and folder organization."

**Assistant:**
```swift
// Query notes in a specific folder
let folderRef = CKRecord.Reference(recordID: folderID, action: .none)
let notes = try await CloudKitManager.shared.queryNotes(inFolder: folderID)

// Full-text search using CloudKit's CONTAINS operator
let results = try await CloudKitManager.shared.queryNotes(searchText: "meeting")

// Save a new note
var note = NoteRecord(title: "Meeting Notes", body: "Discussion points...", folderID: folderID)
let saved = try await CloudKitManager.shared.save(note.record)
```

---

## Techniques Used

- **ST-01** (Clear Objective): CloudKit integration across all database scopes
- **ST-02** (Sequential Instructions): Phased from setup to sharing
- **RT-02** (Multi-Dimensional Analysis): CRUD, subscriptions, sharing, errors
- **RT-05** (Edge Case Identification): Quota, conflicts, network, account status
- **ST-03** (Output Format Templates): Code templates per CloudKit feature
- **NE-02** (Phased Workflow): Progressive build from container to sharing

---

## Related Prompts

- [ios_offline_first_sync.md](ios_offline_first_sync.md) - Offline-first with CloudKit sync
- [ios_data_layer_implementation.md](ios_data_layer_implementation.md) - Local persistence paired with CloudKit
- [ios_push_notifications.md](ios_push_notifications.md) - Handle CloudKit subscription notifications
- [ios_background_tasks.md](ios_background_tasks.md) - Background CloudKit sync

---

## Customization Guide

### For Public Database (Social Feed)

Use public database for shared content:
```swift
let posts = try await CloudKitManager.shared.fetchAll(
    recordType: "Post",
    sortDescriptors: [NSSortDescriptor(key: "createdAt", ascending: false)],
    limit: 50,
    from: .public
)
```

### For CloudKit Dashboard Schema

Deploy schema programmatically:
```swift
// In DEBUG: use development environment
// Before App Store: deploy via CloudKit Dashboard
// Production schemas cannot be modified, only extended
```

### For Large Asset Storage

Use CKAsset for files over 1MB:
```swift
let tempURL = FileManager.default.temporaryDirectory.appendingPathComponent("photo.jpg")
try imageData.write(to: tempURL)
record["photo"] = CKAsset(fileURL: tempURL)
```
