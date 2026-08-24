---
title: "iOS Data Layer Implementation"
category: mobile-development
description: "Build a robust data layer with Core Data or SwiftData, repository pattern, background contexts, fetch request optimization, and migration strategies."
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
  - core-data
  - swiftdata
  - repository-pattern
  - persistence
  - mobile-development
updated: "2026-03-19"
---

# iOS Data Layer Implementation

**Objective:** Build a production-ready data persistence layer using Core Data or SwiftData with the repository pattern, background context management, fetch request optimization, and safe migration strategies for iOS applications.

**When to Use:** Use this prompt when implementing local data persistence in an iOS app. Ideal for apps that need structured storage, offline capability, or complex data relationships. Best used after data models and API contracts are defined.

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

Before building the data layer, gather essential context:

1. **Persistence Framework:**
   - "Is the project using Core Data, SwiftData, or no persistence yet?"
   - "What is the minimum deployment target (iOS 17+ for SwiftData)?"
   - "Are there existing model files (.xcdatamodeld) or @Model classes?"

2. **Data Requirements:**
   - "What entities/models need to be persisted?"
   - "What are the relationships between entities (one-to-many, many-to-many)?"
   - "Are there large binary fields (images, files) that need external storage?"

3. **Performance:**
   - "How many records are expected per entity (hundreds, thousands, millions)?"
   - "What are the most frequent read queries?"
   - "Does the app need background imports (e.g., syncing API data)?"

4. **Migration:**
   - "Is there an existing schema that needs migration?"
   - "How often do schema changes occur?"
   - "Is lightweight migration sufficient or do you need custom mapping?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before implementing ANY code, you MUST:**

1. **Understand existing data patterns** - Check for existing persistence code, model files, and data access patterns in the codebase.
2. **Verify data requirements** - Confirm entity relationships, indexing needs, and query patterns before writing models.
3. **Follow project conventions** - Match existing naming, module organization, and error handling patterns.
4. **Provide specific, working code** - All code samples MUST include file paths and be copy-paste ready.
5. **Include migration strategy** - Every schema change must have an explicit migration path.

### False-Positive Prevention

- ❌ Do NOT mix Core Data and SwiftData in the same model layer without explicit bridging
- ❌ Do NOT perform heavy fetches on the main thread
- ❌ Do NOT access managed objects across context boundaries
- ❌ Do NOT skip indexing on frequently queried attributes
- ❌ Do NOT ignore merge conflicts in multi-context setups
- ✅ DO use background contexts for imports and batch operations
- ✅ DO define fetch limits and batch sizes for large datasets
- ✅ DO provide proper error handling for persistence failures
- ✅ DO test migration paths before shipping schema changes

---

### Phase 1: SwiftData Stack Setup

#### 1.1 Model Container Configuration

```swift
// File: Data/Persistence/PersistenceController.swift

import SwiftData
import SwiftUI

struct PersistenceController {
    static let shared = PersistenceController()

    let modelContainer: ModelContainer

    init(inMemory: Bool = false) {
        let schema = Schema([
            Item.self,
            Category.self,
            Tag.self,
        ])

        let configuration = ModelConfiguration(
            schema: schema,
            isStoredInMemoryOnly: inMemory,
            allowsSave: true
        )

        do {
            modelContainer = try ModelContainer(
                for: schema,
                configurations: [configuration]
            )
        } catch {
            fatalError("Failed to create ModelContainer: \(error)")
        }
    }

    /// Preview container with sample data
    @MainActor
    static var preview: PersistenceController = {
        let controller = PersistenceController(inMemory: true)
        let context = controller.modelContainer.mainContext

        // Insert sample data
        let category = Category(name: "Work", colorHex: "#007AFF")
        context.insert(category)

        for i in 1...10 {
            let item = Item(
                title: "Item \(i)",
                body: "Description for item \(i)",
                createdAt: Date().addingTimeInterval(Double(-i) * 3600),
                category: category
            )
            context.insert(item)
        }

        return controller
    }()
}

// App entry point integration
@main
struct MyApp: App {
    let persistence = PersistenceController.shared

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(persistence.modelContainer)
    }
}
```

#### 1.2 SwiftData Models

```swift
// File: Data/Models/Item.swift

import SwiftData
import Foundation

@Model
final class Item {
    var title: String
    var body: String
    var createdAt: Date
    var updatedAt: Date
    var isPinned: Bool
    var sortOrder: Int

    // Relationships
    var category: Category?
    var tags: [Tag]

    // External storage for large data
    @Attribute(.externalStorage)
    var imageData: Data?

    init(
        title: String,
        body: String = "",
        createdAt: Date = .now,
        category: Category? = nil,
        tags: [Tag] = []
    ) {
        self.title = title
        self.body = body
        self.createdAt = createdAt
        self.updatedAt = createdAt
        self.isPinned = false
        self.sortOrder = 0
        self.category = category
        self.tags = tags
    }
}

// File: Data/Models/Category.swift

@Model
final class Category {
    @Attribute(.unique)
    var name: String
    var colorHex: String

    @Relationship(deleteRule: .nullify, inverse: \Item.category)
    var items: [Item]

    init(name: String, colorHex: String = "#007AFF") {
        self.name = name
        self.colorHex = colorHex
        self.items = []
    }
}

// File: Data/Models/Tag.swift

@Model
final class Tag {
    @Attribute(.unique)
    var name: String

    @Relationship(inverse: \Item.tags)
    var items: [Item]

    init(name: String) {
        self.name = name
        self.items = []
    }
}
```

---

### Phase 2: Repository Pattern

**CHECKPOINT 1:** Confirm models and container before implementing repositories.

#### 2.1 Repository Protocol

```swift
// File: Data/Repositories/ItemRepositoryProtocol.swift

import Foundation

protocol ItemRepositoryProtocol: Sendable {
    func fetchAll(sortedBy: ItemSortOrder, filter: ItemFilter?) async throws -> [Item]
    func fetch(id: PersistentIdentifier) async throws -> Item?
    func search(query: String) async throws -> [Item]
    func create(_ draft: ItemDraft) async throws -> Item
    func update(_ id: PersistentIdentifier, with draft: ItemDraft) async throws
    func delete(_ id: PersistentIdentifier) async throws
    func batchImport(_ drafts: [ItemDraft]) async throws -> Int
}

enum ItemSortOrder {
    case createdAtDescending
    case createdAtAscending
    case titleAscending
    case pinnedFirst
}

struct ItemFilter {
    var categoryName: String?
    var isPinned: Bool?
    var dateRange: ClosedRange<Date>?
}

struct ItemDraft {
    var title: String
    var body: String
    var categoryName: String?
    var tagNames: [String]
}
```

#### 2.2 SwiftData Repository Implementation

```swift
// File: Data/Repositories/ItemRepository.swift

import SwiftData
import Foundation

@ModelActor
actor ItemRepository: ItemRepositoryProtocol {

    func fetchAll(
        sortedBy sortOrder: ItemSortOrder,
        filter: ItemFilter? = nil
    ) async throws -> [Item] {
        var descriptor = FetchDescriptor<Item>()

        // Apply sorting
        switch sortOrder {
        case .createdAtDescending:
            descriptor.sortBy = [SortDescriptor(\.createdAt, order: .reverse)]
        case .createdAtAscending:
            descriptor.sortBy = [SortDescriptor(\.createdAt)]
        case .titleAscending:
            descriptor.sortBy = [SortDescriptor(\.title)]
        case .pinnedFirst:
            descriptor.sortBy = [
                SortDescriptor(\.isPinned, order: .reverse),
                SortDescriptor(\.createdAt, order: .reverse)
            ]
        }

        // Apply filters
        if let filter {
            var predicates: [Predicate<Item>] = []

            if let categoryName = filter.categoryName {
                predicates.append(#Predicate { $0.category?.name == categoryName })
            }
            if let isPinned = filter.isPinned {
                predicates.append(#Predicate { $0.isPinned == isPinned })
            }

            if !predicates.isEmpty {
                // Combine predicates manually
                if let categoryName = filter.categoryName, let isPinned = filter.isPinned {
                    descriptor.predicate = #Predicate {
                        $0.category?.name == categoryName && $0.isPinned == isPinned
                    }
                } else if let categoryName = filter.categoryName {
                    descriptor.predicate = #Predicate {
                        $0.category?.name == categoryName
                    }
                } else if let isPinned = filter.isPinned {
                    descriptor.predicate = #Predicate {
                        $0.isPinned == isPinned
                    }
                }
            }
        }

        // Batch size for performance
        descriptor.fetchLimit = 100

        return try modelContext.fetch(descriptor)
    }

    func fetch(id: PersistentIdentifier) async throws -> Item? {
        return modelContext.model(for: id) as? Item
    }

    func search(query: String) async throws -> [Item] {
        let descriptor = FetchDescriptor<Item>(
            predicate: #Predicate {
                $0.title.localizedStandardContains(query) ||
                $0.body.localizedStandardContains(query)
            },
            sortBy: [SortDescriptor(\.createdAt, order: .reverse)]
        )
        return try modelContext.fetch(descriptor)
    }

    func create(_ draft: ItemDraft) async throws -> Item {
        let item = Item(title: draft.title, body: draft.body)

        if let categoryName = draft.categoryName {
            item.category = try findOrCreateCategory(name: categoryName)
        }

        item.tags = try draft.tagNames.map { try findOrCreateTag(name: $0) }

        modelContext.insert(item)
        try modelContext.save()
        return item
    }

    func update(_ id: PersistentIdentifier, with draft: ItemDraft) async throws {
        guard let item = modelContext.model(for: id) as? Item else {
            throw RepositoryError.notFound
        }

        item.title = draft.title
        item.body = draft.body
        item.updatedAt = .now

        if let categoryName = draft.categoryName {
            item.category = try findOrCreateCategory(name: categoryName)
        }

        item.tags = try draft.tagNames.map { try findOrCreateTag(name: $0) }

        try modelContext.save()
    }

    func delete(_ id: PersistentIdentifier) async throws {
        guard let item = modelContext.model(for: id) as? Item else {
            throw RepositoryError.notFound
        }
        modelContext.delete(item)
        try modelContext.save()
    }

    func batchImport(_ drafts: [ItemDraft]) async throws -> Int {
        var count = 0
        for draft in drafts {
            let item = Item(title: draft.title, body: draft.body)
            modelContext.insert(item)
            count += 1

            // Save in batches of 100 for memory efficiency
            if count % 100 == 0 {
                try modelContext.save()
            }
        }
        try modelContext.save()
        return count
    }

    // MARK: - Helpers

    private func findOrCreateCategory(name: String) throws -> Category {
        let descriptor = FetchDescriptor<Category>(
            predicate: #Predicate { $0.name == name }
        )
        if let existing = try modelContext.fetch(descriptor).first {
            return existing
        }
        let category = Category(name: name)
        modelContext.insert(category)
        return category
    }

    private func findOrCreateTag(name: String) throws -> Tag {
        let descriptor = FetchDescriptor<Tag>(
            predicate: #Predicate { $0.name == name }
        )
        if let existing = try modelContext.fetch(descriptor).first {
            return existing
        }
        let tag = Tag(name: name)
        modelContext.insert(tag)
        return tag
    }
}

enum RepositoryError: LocalizedError {
    case notFound
    case saveFailed(Error)

    var errorDescription: String? {
        switch self {
        case .notFound: return "Record not found"
        case .saveFailed(let error): return "Save failed: \(error.localizedDescription)"
        }
    }
}
```

---

### Phase 3: Core Data Alternative

For projects targeting iOS 16 or requiring Core Data:

#### 3.1 Core Data Stack

```swift
// File: Data/Persistence/CoreDataStack.swift

import CoreData

final class CoreDataStack {
    static let shared = CoreDataStack()

    let persistentContainer: NSPersistentContainer

    var viewContext: NSManagedObjectContext {
        persistentContainer.viewContext
    }

    init(inMemory: Bool = false) {
        persistentContainer = NSPersistentContainer(name: "DataModel")

        if inMemory {
            persistentContainer.persistentStoreDescriptions.first?.url =
                URL(fileURLWithPath: "/dev/null")
        }

        // Enable persistent history tracking for background sync
        let description = persistentContainer.persistentStoreDescriptions.first
        description?.setOption(true as NSNumber,
            forKey: NSPersistentHistoryTrackingKey)
        description?.setOption(true as NSNumber,
            forKey: NSPersistentStoreRemoteChangeNotificationPostOptionKey)

        persistentContainer.loadPersistentStores { _, error in
            if let error {
                fatalError("Core Data failed to load: \(error)")
            }
        }

        viewContext.automaticallyMergesChangesFromParent = true
        viewContext.mergePolicy = NSMergeByPropertyObjectTrumpMergePolicy
    }

    /// Background context for imports and heavy operations
    func newBackgroundContext() -> NSManagedObjectContext {
        let context = persistentContainer.newBackgroundContext()
        context.mergePolicy = NSMergeByPropertyObjectTrumpMergePolicy
        return context
    }

    /// Perform work on a background context
    func performBackground<T>(
        _ block: @escaping (NSManagedObjectContext) throws -> T
    ) async throws -> T {
        try await persistentContainer.performBackgroundTask { context in
            context.mergePolicy = NSMergeByPropertyObjectTrumpMergePolicy
            return try block(context)
        }
    }
}
```

#### 3.2 Core Data Batch Operations

```swift
// File: Data/Repositories/CoreDataBatchOperations.swift

import CoreData

extension CoreDataStack {

    /// Batch insert for large datasets (iOS 14+)
    func batchInsertItems(_ records: [[String: Any]]) async throws {
        try await performBackground { context in
            let batchInsert = NSBatchInsertRequest(
                entity: CDItem.entity(),
                objects: records
            )
            batchInsert.resultType = .objectIDs

            let result = try context.execute(batchInsert) as? NSBatchInsertResult
            let objectIDs = result?.result as? [NSManagedObjectID] ?? []

            // Merge changes into view context
            NSManagedObjectContext.mergeChanges(
                fromRemoteContextSave: [NSInsertedObjectsKey: objectIDs],
                into: [self.viewContext]
            )
        }
    }

    /// Batch delete with merge
    func batchDeleteItems(predicate: NSPredicate) async throws {
        try await performBackground { context in
            let fetchRequest = NSFetchRequest<NSFetchRequestResult>(entityName: "CDItem")
            fetchRequest.predicate = predicate

            let batchDelete = NSBatchDeleteRequest(fetchRequest: fetchRequest)
            batchDelete.resultType = .resultTypeObjectIDs

            let result = try context.execute(batchDelete) as? NSBatchDeleteResult
            let objectIDs = result?.result as? [NSManagedObjectID] ?? []

            NSManagedObjectContext.mergeChanges(
                fromRemoteContextSave: [NSDeletedObjectsKey: objectIDs],
                into: [self.viewContext]
            )
        }
    }
}
```

---

### Phase 4: Migration Strategy

**CHECKPOINT 2:** Review data layer before implementing migrations.

#### 4.1 SwiftData Migration

```swift
// File: Data/Migrations/ItemMigrationPlan.swift

import SwiftData

enum ItemSchemaV1: VersionedSchema {
    static var versionIdentifier = Schema.Version(1, 0, 0)
    static var models: [any PersistentModel.Type] {
        [ItemV1.self]
    }

    @Model
    final class ItemV1 {
        var title: String
        var body: String
        var createdAt: Date
        init(title: String, body: String, createdAt: Date) {
            self.title = title
            self.body = body
            self.createdAt = createdAt
        }
    }
}

enum ItemSchemaV2: VersionedSchema {
    static var versionIdentifier = Schema.Version(2, 0, 0)
    static var models: [any PersistentModel.Type] {
        [Item.self, Category.self, Tag.self]
    }
}

enum ItemMigrationPlan: SchemaMigrationPlan {
    static var schemas: [any VersionedSchema.Type] {
        [ItemSchemaV1.self, ItemSchemaV2.self]
    }

    static var stages: [MigrationStage] {
        [migrateV1toV2]
    }

    static let migrateV1toV2 = MigrationStage.custom(
        fromVersion: ItemSchemaV1.self,
        toVersion: ItemSchemaV2.self
    ) { context in
        // Pre-migration: data cleanup
    } didMigrate: { context in
        // Post-migration: set defaults for new fields
        let items = try context.fetch(FetchDescriptor<Item>())
        for item in items {
            item.isPinned = false
            item.sortOrder = 0
            item.updatedAt = item.createdAt
        }
        try context.save()
    }
}
```

---

## Expected Output

### File Structure

```
Data/
├── Models/
│   ├── Item.swift              # @Model entity
│   ├── Category.swift          # @Model entity
│   └── Tag.swift               # @Model entity
├── Persistence/
│   ├── PersistenceController.swift  # Container setup
│   └── CoreDataStack.swift          # Core Data alternative
├── Repositories/
│   ├── ItemRepositoryProtocol.swift # Protocol definition
│   └── ItemRepository.swift         # @ModelActor implementation
└── Migrations/
    └── ItemMigrationPlan.swift      # Versioned schema migration
```

### Implementation Checklist

- [ ] Model container configured with proper schema
- [ ] @Model classes with relationships and indexes
- [ ] Repository protocol with async interface
- [ ] @ModelActor repository for thread-safe background access
- [ ] Batch operations for large imports
- [ ] Fetch descriptors with predicates and sort
- [ ] Migration plan with versioned schemas
- [ ] Preview container with sample data
- [ ] Error handling for all persistence operations

---

## Example Interaction

**User:** "I need to store user tasks with tags and due dates, with search and filter by tag."

**Assistant:**
```swift
@Model
final class UserTask {
    @Attribute(.spotlight)
    var title: String
    var notes: String
    var dueDate: Date?
    var isCompleted: Bool
    var tags: [TaskTag]

    init(title: String, notes: String = "", dueDate: Date? = nil) {
        self.title = title
        self.notes = notes
        self.dueDate = dueDate
        self.isCompleted = false
        self.tags = []
    }
}

@ModelActor
actor TaskRepository {
    func fetchByTag(name: String) throws -> [UserTask] {
        let descriptor = FetchDescriptor<UserTask>(
            predicate: #Predicate { task in
                task.tags.contains { $0.name == name }
            },
            sortBy: [SortDescriptor(\.dueDate)]
        )
        return try modelContext.fetch(descriptor)
    }

    func searchTasks(query: String) throws -> [UserTask] {
        let descriptor = FetchDescriptor<UserTask>(
            predicate: #Predicate {
                $0.title.localizedStandardContains(query) ||
                $0.notes.localizedStandardContains(query)
            }
        )
        return try modelContext.fetch(descriptor)
    }
}
```

---

## Techniques Used

- **ST-01** (Clear Objective): Focused objective on data layer construction
- **ST-02** (Sequential Instructions): Phased approach from models to migration
- **RT-02** (Multi-Dimensional Analysis): Covers SwiftData, Core Data, repositories, migration
- **RT-05** (Edge Case Identification): Merge conflicts, batch operations, migration failures
- **DS-02** (Progressive Disclosure): From simple models to advanced migration
- **NE-02** (Phased Workflow): Clear phases with checkpoints

---

## Related Prompts

- [ios_offline_first_sync.md](ios_offline_first_sync.md) - Add CloudKit sync to data layer
- [ios_api_integration.md](ios_api_integration.md) - Network layer that feeds repository
- [ios_cloudkit_integration.md](ios_cloudkit_integration.md) - CloudKit database operations
- [ios_state_management.md](ios_state_management.md) - Connect data layer to UI state

---

## Customization Guide

### For Encrypted Storage

Add encrypted store:
```swift
let description = NSPersistentStoreDescription()
description.url = storeURL
description.setOption(
    FileProtectionType.complete as NSObject,
    forKey: NSPersistentStoreFileProtectionKey
)
```

### For Sectioned Fetch Results

Use `@Query` with `SectionedFetchResults`:
```swift
@Query(sort: \Item.category?.name)
var items: [Item]

// Group in view
var grouped: [String: [Item]] {
    Dictionary(grouping: items) { $0.category?.name ?? "Uncategorized" }
}
```

### For Unit Testing

Inject in-memory container:
```swift
func testCreateItem() async throws {
    let container = try ModelContainer(
        for: Item.self,
        configurations: ModelConfiguration(isStoredInMemoryOnly: true)
    )
    let repo = ItemRepository(modelContainer: container)
    let draft = ItemDraft(title: "Test", body: "Body")
    let item = try await repo.create(draft)
    XCTAssertEqual(item.title, "Test")
}
```
