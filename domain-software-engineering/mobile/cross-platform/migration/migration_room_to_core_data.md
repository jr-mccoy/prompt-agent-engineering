---
title: "Room to Core Data/SwiftData Migration"
category: mobile-development
description: "Migrate Room database layer to Core Data or SwiftData including entities, DAOs to fetch requests, migrations, relationships, and Flow to NSFetchedResultsController"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-02
difficulty: advanced
tags:
  - ios
  - android
  - migration
  - room
  - core-data
  - swiftdata
  - database
  - persistence
updated: "2026-03-19"
---

# Room to Core Data/SwiftData Migration

**Objective:** Translate Android's Room persistence layer to iOS equivalents (Core Data or SwiftData), covering entity definitions, DAO patterns, database migrations, relationships, reactive queries (Flow to observation), and offline-first data strategies.

**When to Use:** When migrating an Android app's local database from Room to iOS. Choose SwiftData for iOS 17+ projects with simpler schemas, or Core Data for iOS 16 compatibility and complex migration needs.

**Prompt Type:** Comprehensive (~350 lines)

## Context Gathering

1. How many Room entities does the app define?
2. What relationships exist between entities? (one-to-many, many-to-many, embedded)
3. Are there complex Room queries (JOINs, aggregations, FTS)?
4. How many database migrations exist? What do they involve?
5. Does the app use Room's Flow/LiveData observation for reactive UI?
6. Is there a caching strategy? (network-first, cache-first, stale-while-revalidate)
7. What is the target iOS version? (iOS 17+ enables SwiftData)
8. What is the approximate database size and record count?

## Instructions

### CRITICAL: Verification Requirements

- Entity mappings MUST preserve all data fields and their types
- Relationship cardinality MUST match between Room and Core Data/SwiftData
- Migration strategies MUST be tested with production-like data
- Reactive observation MUST update the UI at the same granularity as Room Flow

### False-Positive Prevention

- ❌ DO NOT assume Room's auto-generated migration maps to Core Data lightweight migration
- ✅ DO verify each schema change qualifies for lightweight migration or write custom mapping models
- ❌ DO NOT assume Room's `@Embedded` has a direct Core Data equivalent
- ✅ DO flatten embedded objects into the entity or use Transformable attributes
- ❌ DO NOT ignore threading — Core Data has strict concurrency rules
- ✅ DO use `@ModelActor` (SwiftData) or `performBackgroundTask` (Core Data) for writes
- ❌ DO NOT observe SwiftData queries from a background context
- ✅ DO use `@Query` macro on the main actor for SwiftUI observation

### Step 1: Entity Mapping

**Kotlin (Room entity):**
```kotlin
@Entity(
    tableName = "tasks",
    indices = [Index(value = ["project_id"])],
    foreignKeys = [ForeignKey(
        entity = ProjectEntity::class,
        parentColumns = ["id"],
        childColumns = ["project_id"],
        onDelete = ForeignKey.CASCADE
    )]
)
data class TaskEntity(
    @PrimaryKey
    val id: String,
    @ColumnInfo(name = "title")
    val title: String,
    @ColumnInfo(name = "description")
    val description: String?,
    @ColumnInfo(name = "is_completed")
    val isCompleted: Boolean = false,
    @ColumnInfo(name = "project_id")
    val projectId: String,
    @ColumnInfo(name = "due_date")
    val dueDate: Long?, // Epoch millis
    @ColumnInfo(name = "priority")
    val priority: Int = 0,
    @ColumnInfo(name = "created_at")
    val createdAt: Long = System.currentTimeMillis()
)

@Entity(tableName = "projects")
data class ProjectEntity(
    @PrimaryKey
    val id: String,
    val name: String,
    val color: String
)
```

**Swift (SwiftData model — iOS 17+):**
```swift
import SwiftData

@Model
final class TaskItem {
    @Attribute(.unique) var id: String
    var title: String
    var taskDescription: String?
    var isCompleted: Bool = false
    var dueDate: Date?
    var priority: Int = 0
    var createdAt: Date = Date()

    @Relationship(inverse: \Project.tasks)
    var project: Project?

    init(id: String, title: String, project: Project) {
        self.id = id
        self.title = title
        self.project = project
    }
}

@Model
final class Project {
    @Attribute(.unique) var id: String
    var name: String
    var color: String

    @Relationship(deleteRule: .cascade)
    var tasks: [TaskItem] = []

    init(id: String, name: String, color: String) {
        self.id = id
        self.name = name
        self.color = color
    }
}
```

**Swift (Core Data model — iOS 16 compatible):**
```swift
// Defined in .xcdatamodeld visual editor, accessed via generated classes:
// TaskItem+CoreDataClass.swift (auto-generated)
extension TaskItem {
    @nonobjc public class func fetchRequest() -> NSFetchRequest<TaskItem> {
        return NSFetchRequest<TaskItem>(entityName: "TaskItem")
    }

    @NSManaged public var id: String
    @NSManaged public var title: String
    @NSManaged public var taskDescription: String?
    @NSManaged public var isCompleted: Bool
    @NSManaged public var dueDate: Date?
    @NSManaged public var priority: Int16
    @NSManaged public var createdAt: Date
    @NSManaged public var project: Project?
}
```

### Step 2: DAO to Fetch Request / Query Macro

**Kotlin (Room DAO):**
```kotlin
@Dao
interface TaskDao {
    @Query("SELECT * FROM tasks WHERE project_id = :projectId ORDER BY priority DESC")
    fun observeTasksByProject(projectId: String): Flow<List<TaskEntity>>

    @Query("SELECT * FROM tasks WHERE is_completed = 0 ORDER BY due_date ASC")
    fun observeIncompleteTasks(): Flow<List<TaskEntity>>

    @Query("SELECT * FROM tasks WHERE id = :id")
    suspend fun getTaskById(id: String): TaskEntity?

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsert(task: TaskEntity)

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsertAll(tasks: List<TaskEntity>)

    @Delete
    suspend fun delete(task: TaskEntity)

    @Query("SELECT COUNT(*) FROM tasks WHERE project_id = :projectId AND is_completed = 0")
    fun observeIncompleteCount(projectId: String): Flow<Int>
}
```

**Swift (SwiftData @Query — iOS 17+):**
```swift
// In SwiftUI View — reactive observation via @Query
struct ProjectTasksView: View {
    let projectId: String

    @Query private var tasks: [TaskItem]

    init(projectId: String) {
        self.projectId = projectId
        _tasks = Query(
            filter: #Predicate<TaskItem> { task in
                task.project?.id == projectId
            },
            sort: [SortDescriptor(\.priority, order: .reverse)]
        )
    }

    var body: some View {
        List(tasks) { task in
            TaskRow(task: task)
        }
    }
}

// Repository for non-view operations
@ModelActor
actor TaskRepository {
    func getTaskById(_ id: String) throws -> TaskItem? {
        let descriptor = FetchDescriptor<TaskItem>(
            predicate: #Predicate { $0.id == id }
        )
        return try modelContext.fetch(descriptor).first
    }

    func upsert(_ task: TaskItem) throws {
        modelContext.insert(task)
        try modelContext.save()
    }

    func delete(_ task: TaskItem) throws {
        modelContext.delete(task)
        try modelContext.save()
    }
}
```

**Swift (Core Data — iOS 16 compatible):**
```swift
// NSFetchedResultsController for reactive observation
class TaskListViewModel: NSObject, ObservableObject {
    @Published var tasks: [TaskItem] = []

    private let fetchedResultsController: NSFetchedResultsController<TaskItem>

    init(projectId: String, context: NSManagedObjectContext) {
        let request: NSFetchRequest<TaskItem> = TaskItem.fetchRequest()
        request.predicate = NSPredicate(format: "project.id == %@", projectId)
        request.sortDescriptors = [
            NSSortDescriptor(key: "priority", ascending: false)
        ]

        fetchedResultsController = NSFetchedResultsController(
            fetchRequest: request,
            managedObjectContext: context,
            sectionNameKeyPath: nil,
            cacheName: nil
        )

        super.init()
        fetchedResultsController.delegate = self
        try? fetchedResultsController.performFetch()
        tasks = fetchedResultsController.fetchedObjects ?? []
    }
}

extension TaskListViewModel: NSFetchedResultsControllerDelegate {
    func controllerDidChangeContent(
        _ controller: NSFetchedResultsController<any NSFetchRequestResult>
    ) {
        tasks = fetchedResultsController.fetchedObjects ?? []
    }
}
```

### Step 3: Migration Strategy

| Room Migration | Core Data / SwiftData Equivalent |
|---------------|--------------------------------|
| Auto-migration (Room 2.4+) | Lightweight migration (automatic) |
| Manual Migration (`Migration(1,2)`) | Mapping Model (`.xcmappingmodel`) |
| Destructive migration | Delete and recreate store |
| Schema export (JSON) | `.xcdatamodeld` versioned models |

**Kotlin (Room migration):**
```kotlin
val MIGRATION_1_2 = object : Migration(1, 2) {
    override fun migrate(db: SupportSQLiteDatabase) {
        db.execSQL("ALTER TABLE tasks ADD COLUMN priority INTEGER NOT NULL DEFAULT 0")
    }
}

Room.databaseBuilder(context, AppDatabase::class.java, "app.db")
    .addMigrations(MIGRATION_1_2)
    .build()
```

**Swift (SwiftData schema versioning):**
```swift
enum SchemaV1: VersionedSchema {
    static var versionIdentifier = Schema.Version(1, 0, 0)
    static var models: [any PersistentModel.Type] { [TaskItemV1.self] }

    @Model final class TaskItemV1 { /* v1 fields */ }
}

enum SchemaV2: VersionedSchema {
    static var versionIdentifier = Schema.Version(2, 0, 0)
    static var models: [any PersistentModel.Type] { [TaskItem.self] }
}

enum TaskMigrationPlan: SchemaMigrationPlan {
    static var schemas: [any VersionedSchema.Type] {
        [SchemaV1.self, SchemaV2.self]
    }

    static var stages: [MigrationStage] {
        [migrateV1toV2]
    }

    static let migrateV1toV2 = MigrationStage.custom(
        fromVersion: SchemaV1.self,
        toVersion: SchemaV2.self
    ) { context in
        // Custom migration logic
        let tasks = try context.fetch(FetchDescriptor<SchemaV2.TaskItem>())
        for task in tasks {
            task.priority = 0 // Set default for new field
        }
        try context.save()
    }
}
```

### Step 4: Relationship Mapping

| Room Pattern | SwiftData / Core Data Equivalent |
|-------------|--------------------------------|
| `@ForeignKey` + `@Relation` | `@Relationship` (SwiftData) / Relationship in model editor |
| `@Embedded` | Flatten into entity or use Transformable |
| Junction table (many-to-many) | `@Relationship` with inverse on both sides |
| `@Relation(associateBy = Junction(...))` | Implicit junction table in SwiftData |

## Expected Output

1. **Entity/model definitions** for SwiftData or Core Data
2. **Repository/DAO equivalent** with all query methods translated
3. **Migration plan** for initial schema and future versioning
4. **Observation pattern** connecting database to SwiftUI views

## Example Interaction

**User:** Our Room database has 6 entities, 3 one-to-many relationships, uses Flow for all queries, and has 4 migrations. Target is iOS 17+.

**Assistant:** SwiftData is recommended for iOS 17+. Here is the mapping approach:

| Room Component | SwiftData Equivalent |
|---------------|---------------------|
| 6 `@Entity` classes | 6 `@Model` classes |
| `@ForeignKey` + `@Relation` | `@Relationship` with inverse |
| `@Dao` with `Flow<List<T>>` | `@Query` in SwiftUI views + `@ModelActor` for repositories |
| 4 `Migration` objects | `SchemaMigrationPlan` with `VersionedSchema` |

## Techniques Used

| Technique | Application |
|-----------|-------------|
| **ST-01: Structured Task Decomposition** | Entity, DAO, migration, observation steps |
| **ST-02: Systematic Analysis Framework** | Comprehensive mapping tables for all patterns |
| **RT-02: Contextual Reference Integration** | Room, Core Data, and SwiftData documentation |
| **DS-02: Output Specification Framework** | Model definitions, repository code, migration plan |

## Related Prompts

- `migration_datastore_to_userdefaults.md` — Key-value storage migration
- `migration_coroutines_to_swift_concurrency.md` — Flow observation patterns
- `migration_architecture_adaptation.md` — Repository layer architecture

## Customization Guide

- **Core Data (iOS 16):** Replace `@Model` with `.xcdatamodeld`, `@Query` with `NSFetchedResultsController`, and `@ModelActor` with `performBackgroundTask`.
- **GRDB/SQLite:** If preferring a SQL-based approach on iOS, use GRDB.swift which has a more similar API to Room.
- **Realm:** If the Android app uses Realm instead of Room, the migration is simpler since Realm is cross-platform.
- **Large Databases:** For databases over 100MB, implement batch migration and test performance on the oldest supported iOS device.
