---
title: "Android Data Layer Implementation"
category: mobile-development
description: ""
tags:
  - android
  - mobile-development
updated: "2026-03-19"
---

# Android Data Layer Implementation

**Objective:** Build a robust, testable data layer following Android architecture best practices with Room database, Repository pattern, and proper data source abstractions.

**When to Use:** Use this prompt when implementing the data layer for a new feature or refactoring an existing data layer. Ideal when you need local persistence with Room, remote data fetching, or both with proper caching strategies. Best used after feature specification and architecture decisions are finalized.

**Prompt Type:** Comprehensive (350-450 lines)

---

## Context Gathering

Before implementing the data layer, gather essential context:

1. **Data Requirements:**
   - "What data entities need to be persisted locally?"
   - "What data comes from remote APIs?"
   - "What are the relationships between entities (one-to-one, one-to-many, many-to-many)?"

2. **Existing Architecture:**
   - "Is there an existing Room database in the project?"
   - "What dependency injection framework is used (Hilt, Koin, manual)?"
   - "Are there existing repository patterns to follow?"

3. **Caching Strategy:**
   - "Should data be cached locally for offline access?"
   - "What is the cache invalidation strategy (time-based, on-demand, never)?"
   - "How should stale data be handled?"

4. **Performance Considerations:**
   - "Are there large datasets that need pagination?"
   - "Are there frequent writes that need batching?"
   - "What queries will be most common?"

---

## Instructions

### CRITICAL: Implementation Requirements

**Before implementing ANY code, you MUST:**

1. **Understand existing data layer** - Check for existing Room setup, repositories, or data sources in the codebase. Extend rather than replace.
2. **Verify data requirements** - Confirm entity relationships, caching needs, and sync requirements before designing.
3. **Follow project conventions** - Match existing repository patterns, DAO organization, and error handling approaches.
4. **Provide specific, working code** - All code samples MUST include file paths (e.g., `data/local/UserDao.kt`) and be copy-paste ready.
5. **Include migration handling** - For schema changes, provide proper Room migrations.

**Adapting to existing data patterns is preferred over introducing new approaches.** Extend existing repositories and DAOs.

### Quality Requirements

- ❌ Do NOT introduce new ORM if Room is already used (and vice versa)
- ❌ Do NOT generate entities without proper type converters for complex types
- ❌ Do NOT skip database versioning and migrations
- ❌ Do NOT use blocking queries on the main thread
- ✅ DO follow existing entity naming and relationship patterns
- ✅ DO provide proper indices for frequently queried columns
- ✅ DO include proper error handling for database operations
- ✅ DO specify exact file paths for all code changes

---

### Phase 1: Data Model Design

#### 1.1 Domain Model Definition

Start by defining clean domain models that represent the business entities:

```kotlin
// Domain model - used throughout the app
data class [EntityName](
    val id: String,
    val name: String,
    val description: String?,
    val createdAt: Instant,
    val updatedAt: Instant,
    // Business logic methods
) {
    val isValid: Boolean
        get() = name.isNotBlank()

    fun toDisplayName(): String = name.take(50)
}
```

**Design Principles:**
- Domain models should be immutable (use `val` not `var`)
- Include validation logic and computed properties
- Keep free of framework-specific annotations
- Use Kotlin types (`Instant` over `Date`, nullable types where appropriate)

#### 1.2 Database Entity Design

Create Room entities that map to database tables:

```kotlin
@Entity(
    tableName = "entities",
    indices = [
        Index(value = ["name"]),
        Index(value = ["created_at"])
    ]
)
data class EntityDb(
    @PrimaryKey
    val id: String,

    @ColumnInfo(name = "name")
    val name: String,

    @ColumnInfo(name = "description")
    val description: String?,

    @ColumnInfo(name = "created_at")
    val createdAt: Long,

    @ColumnInfo(name = "updated_at")
    val updatedAt: Long,

    @ColumnInfo(name = "is_synced")
    val isSynced: Boolean = false
)
```

**Entity Design Guidelines:**
- Use consistent naming conventions (`snake_case` for columns)
- Add indices for frequently queried columns
- Include sync status fields for offline-first patterns
- Use primitive types for storage (Long for timestamps, not Instant)

#### 1.3 Relationship Mapping

For entities with relationships:

```kotlin
// Parent entity
@Entity(tableName = "categories")
data class CategoryDb(
    @PrimaryKey val id: String,
    val name: String
)

// Child entity with foreign key
@Entity(
    tableName = "items",
    foreignKeys = [
        ForeignKey(
            entity = CategoryDb::class,
            parentColumns = ["id"],
            childColumns = ["category_id"],
            onDelete = ForeignKey.CASCADE
        )
    ],
    indices = [Index(value = ["category_id"])]
)
data class ItemDb(
    @PrimaryKey val id: String,
    @ColumnInfo(name = "category_id") val categoryId: String,
    val name: String
)

// Relationship query result
data class CategoryWithItems(
    @Embedded val category: CategoryDb,
    @Relation(
        parentColumn = "id",
        entityColumn = "category_id"
    )
    val items: List<ItemDb>
)
```

---

### Phase 2: DAO Implementation

**CHECKPOINT 1:** Present the entity design for review.

```markdown
## Data Model Design Summary

### Entities Designed
| Entity | Table Name | Key Fields | Relationships |
|--------|------------|------------|---------------|
| [Entity] | [table] | [fields] | [relations] |

### Indices Created
| Table | Index | Columns | Purpose |
|-------|-------|---------|---------|
| [table] | [idx_name] | [columns] | [why] |

### Design Decisions
1. [Decision] - [Rationale]

**Does this entity design look correct? Any fields to add or modify?**
```

#### 2.1 DAO Interface Design

Create Data Access Objects with comprehensive query methods:

```kotlin
@Dao
interface EntityDao {
    // Insert operations
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(entity: EntityDb)

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertAll(entities: List<EntityDb>)

    // Update operations
    @Update
    suspend fun update(entity: EntityDb)

    @Query("UPDATE entities SET is_synced = :synced WHERE id = :id")
    suspend fun updateSyncStatus(id: String, synced: Boolean)

    // Delete operations
    @Delete
    suspend fun delete(entity: EntityDb)

    @Query("DELETE FROM entities WHERE id = :id")
    suspend fun deleteById(id: String)

    @Query("DELETE FROM entities")
    suspend fun deleteAll()

    // Query operations - Single item
    @Query("SELECT * FROM entities WHERE id = :id")
    suspend fun getById(id: String): EntityDb?

    @Query("SELECT * FROM entities WHERE id = :id")
    fun observeById(id: String): Flow<EntityDb?>

    // Query operations - Lists
    @Query("SELECT * FROM entities ORDER BY created_at DESC")
    fun observeAll(): Flow<List<EntityDb>>

    @Query("SELECT * FROM entities WHERE name LIKE '%' || :query || '%'")
    fun search(query: String): Flow<List<EntityDb>>

    // Pagination support
    @Query("SELECT * FROM entities ORDER BY created_at DESC LIMIT :limit OFFSET :offset")
    suspend fun getPage(limit: Int, offset: Int): List<EntityDb>

    // Aggregation queries
    @Query("SELECT COUNT(*) FROM entities")
    fun observeCount(): Flow<Int>

    @Query("SELECT COUNT(*) FROM entities WHERE is_synced = 0")
    suspend fun getUnsyncedCount(): Int
}
```

**DAO Best Practices:**
- Use `suspend` for one-shot operations
- Use `Flow` for observable queries
- Provide both suspend and Flow variants where useful
- Include pagination support for large datasets
- Add utility queries for counts and aggregations

#### 2.2 Database Configuration

Configure the Room database:

```kotlin
@Database(
    entities = [
        EntityDb::class,
        CategoryDb::class,
        ItemDb::class
    ],
    version = 1,
    exportSchema = true
)
@TypeConverters(Converters::class)
abstract class AppDatabase : RoomDatabase() {
    abstract fun entityDao(): EntityDao
    abstract fun categoryDao(): CategoryDao

    companion object {
        const val DATABASE_NAME = "app_database"
    }
}

// Type converters for complex types
class Converters {
    @TypeConverter
    fun fromTimestamp(value: Long?): Instant? =
        value?.let { Instant.fromEpochMilliseconds(it) }

    @TypeConverter
    fun toTimestamp(instant: Instant?): Long? =
        instant?.toEpochMilliseconds()

    @TypeConverter
    fun fromStringList(value: List<String>): String =
        value.joinToString(",")

    @TypeConverter
    fun toStringList(value: String): List<String> =
        if (value.isEmpty()) emptyList() else value.split(",")
}
```

---

### Phase 3: Repository Implementation

#### 3.1 Repository Interface

Define a clean repository interface:

```kotlin
interface EntityRepository {
    // Observe data
    fun observeAll(): Flow<List<Entity>>
    fun observeById(id: String): Flow<Entity?>
    fun search(query: String): Flow<List<Entity>>

    // Single fetch operations
    suspend fun getById(id: String): Entity?
    suspend fun getAll(): List<Entity>

    // Write operations
    suspend fun save(entity: Entity): Result<Entity>
    suspend fun saveAll(entities: List<Entity>): Result<Unit>
    suspend fun delete(id: String): Result<Unit>

    // Sync operations (if applicable)
    suspend fun refresh(): Result<Unit>
    suspend fun syncPending(): Result<Int>
}
```

#### 3.2 Repository Implementation

Implement the repository with proper data coordination:

```kotlin
class EntityRepositoryImpl @Inject constructor(
    private val localDataSource: EntityLocalDataSource,
    private val remoteDataSource: EntityRemoteDataSource,
    private val mapper: EntityMapper,
    private val dispatchers: DispatcherProvider
) : EntityRepository {

    override fun observeAll(): Flow<List<Entity>> =
        localDataSource.observeAll()
            .map { entities -> entities.map(mapper::toDomain) }
            .flowOn(dispatchers.io)

    override fun observeById(id: String): Flow<Entity?> =
        localDataSource.observeById(id)
            .map { entity -> entity?.let(mapper::toDomain) }
            .flowOn(dispatchers.io)

    override suspend fun getById(id: String): Entity? =
        withContext(dispatchers.io) {
            localDataSource.getById(id)?.let(mapper::toDomain)
        }

    override suspend fun save(entity: Entity): Result<Entity> =
        withContext(dispatchers.io) {
            runCatching {
                val dbEntity = mapper.toDb(entity)
                localDataSource.insert(dbEntity)
                entity
            }
        }

    override suspend fun refresh(): Result<Unit> =
        withContext(dispatchers.io) {
            runCatching {
                val remoteEntities = remoteDataSource.fetchAll()
                val dbEntities = remoteEntities.map(mapper::fromDtoToDb)
                localDataSource.replaceAll(dbEntities)
            }
        }

    override suspend fun syncPending(): Result<Int> =
        withContext(dispatchers.io) {
            runCatching {
                val pending = localDataSource.getUnsynced()
                var syncedCount = 0

                pending.forEach { entity ->
                    try {
                        remoteDataSource.create(mapper.toDto(entity))
                        localDataSource.updateSyncStatus(entity.id, true)
                        syncedCount++
                    } catch (e: Exception) {
                        // Log but continue with other items
                        Timber.e(e, "Failed to sync entity ${entity.id}")
                    }
                }

                syncedCount
            }
        }
}
```

#### 3.3 Data Source Abstractions

Create focused data source classes:

```kotlin
// Local data source wrapping Room DAO
class EntityLocalDataSource @Inject constructor(
    private val dao: EntityDao
) {
    fun observeAll(): Flow<List<EntityDb>> = dao.observeAll()

    fun observeById(id: String): Flow<EntityDb?> = dao.observeById(id)

    suspend fun getById(id: String): EntityDb? = dao.getById(id)

    suspend fun insert(entity: EntityDb) = dao.insert(entity)

    suspend fun insertAll(entities: List<EntityDb>) = dao.insertAll(entities)

    suspend fun delete(id: String) = dao.deleteById(id)

    suspend fun getUnsynced(): List<EntityDb> = dao.getUnsynced()

    suspend fun updateSyncStatus(id: String, synced: Boolean) =
        dao.updateSyncStatus(id, synced)

    @Transaction
    suspend fun replaceAll(entities: List<EntityDb>) {
        dao.deleteAll()
        dao.insertAll(entities)
    }
}

// Remote data source wrapping API
class EntityRemoteDataSource @Inject constructor(
    private val api: EntityApi
) {
    suspend fun fetchAll(): List<EntityDto> = api.getEntities()

    suspend fun fetchById(id: String): EntityDto = api.getEntity(id)

    suspend fun create(entity: EntityDto): EntityDto = api.createEntity(entity)

    suspend fun update(entity: EntityDto): EntityDto = api.updateEntity(entity.id, entity)

    suspend fun delete(id: String) = api.deleteEntity(id)
}
```

---

### Phase 4: Mapper Implementation

**CHECKPOINT 2:** Present the repository architecture for review.

```markdown
## Repository Architecture Summary

### Data Flow
```
Domain Layer (Entity)
        ↓↑ Mapper
Repository (coordinates sources)
        ↓↑
┌───────┴───────┐
LocalDataSource  RemoteDataSource
     ↓               ↓
  Room DAO        Retrofit API
```

### Components Created
| Component | Responsibility |
|-----------|---------------|
| EntityRepository | Data coordination, caching strategy |
| EntityLocalDataSource | Room database operations |
| EntityRemoteDataSource | API network calls |
| EntityMapper | Model transformations |

**Ready to implement mappers and finalize?**
```

#### 4.1 Comprehensive Mapper

Create bidirectional mappers between all model types:

```kotlin
class EntityMapper @Inject constructor() {

    // Database to Domain
    fun toDomain(db: EntityDb): Entity = Entity(
        id = db.id,
        name = db.name,
        description = db.description,
        createdAt = Instant.fromEpochMilliseconds(db.createdAt),
        updatedAt = Instant.fromEpochMilliseconds(db.updatedAt)
    )

    // Domain to Database
    fun toDb(domain: Entity): EntityDb = EntityDb(
        id = domain.id,
        name = domain.name,
        description = domain.description,
        createdAt = domain.createdAt.toEpochMilliseconds(),
        updatedAt = domain.updatedAt.toEpochMilliseconds(),
        isSynced = false
    )

    // DTO to Database (for caching API responses)
    fun fromDtoToDb(dto: EntityDto): EntityDb = EntityDb(
        id = dto.id,
        name = dto.name,
        description = dto.description,
        createdAt = parseTimestamp(dto.createdAt),
        updatedAt = parseTimestamp(dto.updatedAt),
        isSynced = true
    )

    // Database to DTO (for syncing local changes)
    fun toDto(db: EntityDb): EntityDto = EntityDto(
        id = db.id,
        name = db.name,
        description = db.description,
        createdAt = formatTimestamp(db.createdAt),
        updatedAt = formatTimestamp(db.updatedAt)
    )

    // List variants
    fun toDomainList(dbList: List<EntityDb>): List<Entity> =
        dbList.map(::toDomain)

    private fun parseTimestamp(iso8601: String): Long =
        Instant.parse(iso8601).toEpochMilliseconds()

    private fun formatTimestamp(epochMillis: Long): String =
        Instant.fromEpochMilliseconds(epochMillis).toString()
}
```

---

### Phase 5: Dependency Injection Setup

#### 5.1 Hilt Module Configuration

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object DatabaseModule {

    @Provides
    @Singleton
    fun provideDatabase(
        @ApplicationContext context: Context
    ): AppDatabase = Room.databaseBuilder(
        context,
        AppDatabase::class.java,
        AppDatabase.DATABASE_NAME
    )
        .fallbackToDestructiveMigration() // Or provide migrations
        .build()

    @Provides
    fun provideEntityDao(database: AppDatabase): EntityDao =
        database.entityDao()
}

@Module
@InstallIn(SingletonComponent::class)
object DataModule {

    @Provides
    @Singleton
    fun provideEntityLocalDataSource(dao: EntityDao): EntityLocalDataSource =
        EntityLocalDataSource(dao)

    @Provides
    @Singleton
    fun provideEntityRepository(
        localDataSource: EntityLocalDataSource,
        remoteDataSource: EntityRemoteDataSource,
        mapper: EntityMapper,
        dispatchers: DispatcherProvider
    ): EntityRepository = EntityRepositoryImpl(
        localDataSource,
        remoteDataSource,
        mapper,
        dispatchers
    )
}
```

#### 5.2 Database Migrations

For production apps, implement proper migrations:

```kotlin
val MIGRATION_1_2 = object : Migration(1, 2) {
    override fun migrate(database: SupportSQLiteDatabase) {
        database.execSQL(
            "ALTER TABLE entities ADD COLUMN priority INTEGER NOT NULL DEFAULT 0"
        )
    }
}

val MIGRATION_2_3 = object : Migration(2, 3) {
    override fun migrate(database: SupportSQLiteDatabase) {
        // Create new table
        database.execSQL("""
            CREATE TABLE IF NOT EXISTS entities_new (
                id TEXT NOT NULL PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                priority INTEGER NOT NULL DEFAULT 0,
                created_at INTEGER NOT NULL,
                updated_at INTEGER NOT NULL
            )
        """)

        // Copy data
        database.execSQL("""
            INSERT INTO entities_new (id, name, description, priority, created_at, updated_at)
            SELECT id, name, description, priority, created_at, updated_at FROM entities
        """)

        // Replace tables
        database.execSQL("DROP TABLE entities")
        database.execSQL("ALTER TABLE entities_new RENAME TO entities")
    }
}

// Apply migrations
Room.databaseBuilder(context, AppDatabase::class.java, DATABASE_NAME)
    .addMigrations(MIGRATION_1_2, MIGRATION_2_3)
    .build()
```

---

## Expected Output

### File Structure Created

```
data/
├── local/
│   ├── AppDatabase.kt
│   ├── Converters.kt
│   ├── dao/
│   │   └── EntityDao.kt
│   ├── entity/
│   │   └── EntityDb.kt
│   └── datasource/
│       └── EntityLocalDataSource.kt
├── remote/
│   ├── api/
│   │   └── EntityApi.kt
│   ├── dto/
│   │   └── EntityDto.kt
│   └── datasource/
│       └── EntityRemoteDataSource.kt
├── repository/
│   ├── EntityRepository.kt
│   └── EntityRepositoryImpl.kt
├── mapper/
│   └── EntityMapper.kt
└── di/
    ├── DatabaseModule.kt
    └── DataModule.kt
```

### Deliverables Checklist

- [ ] Domain models defined (no framework dependencies)
- [ ] Room entities with proper annotations and indices
- [ ] DAO interfaces with suspend and Flow methods
- [ ] Database configuration with type converters
- [ ] Repository interface defining data contract
- [ ] Repository implementation with error handling
- [ ] Local and remote data sources abstracted
- [ ] Mappers for all model transformations
- [ ] Hilt modules for dependency injection
- [ ] Database migrations (if updating existing schema)

---

## Example Interaction

**User:** I need to implement a data layer for a task management feature. Tasks have a title, description, due date, priority (low/medium/high), and completion status. They belong to projects.

**Agent:** I'll help you build a comprehensive data layer for tasks. Let me gather some context first.

1. Do you have an existing Room database, or is this a new database?
2. Do tasks sync with a backend API, or are they local-only?
3. How many tasks might a user have? (Affects pagination needs)

**User:** New database. Tasks sync with our REST API. Users typically have 50-200 tasks.

**Agent:**

## Data Model Design

### Domain Model

```kotlin
data class Task(
    val id: String,
    val projectId: String,
    val title: String,
    val description: String?,
    val dueDate: LocalDate?,
    val priority: Priority,
    val isCompleted: Boolean,
    val createdAt: Instant,
    val updatedAt: Instant
) {
    enum class Priority { LOW, MEDIUM, HIGH }

    val isOverdue: Boolean
        get() = dueDate?.let { it < Clock.System.todayIn(TimeZone.currentSystemDefault()) } ?: false
}
```

### Database Entity

```kotlin
@Entity(
    tableName = "tasks",
    foreignKeys = [
        ForeignKey(
            entity = ProjectDb::class,
            parentColumns = ["id"],
            childColumns = ["project_id"],
            onDelete = ForeignKey.CASCADE
        )
    ],
    indices = [
        Index("project_id"),
        Index("due_date"),
        Index("is_completed")
    ]
)
data class TaskDb(
    @PrimaryKey val id: String,
    @ColumnInfo(name = "project_id") val projectId: String,
    val title: String,
    val description: String?,
    @ColumnInfo(name = "due_date") val dueDate: Long?,
    val priority: Int, // 0=LOW, 1=MEDIUM, 2=HIGH
    @ColumnInfo(name = "is_completed") val isCompleted: Boolean,
    @ColumnInfo(name = "created_at") val createdAt: Long,
    @ColumnInfo(name = "updated_at") val updatedAt: Long,
    @ColumnInfo(name = "is_synced") val isSynced: Boolean
)
```

With 50-200 tasks, pagination isn't critical, but I've added indices on commonly filtered columns (project, due date, completion).

**Does this model structure work for your needs? Any additional fields needed?**

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective for data layer implementation
- **ST-02** (Sequential Instructions): Phased approach from models to DI
- **RT-02** (Multi-Dimensional Analysis): Covers entities, DAOs, repositories, mappers
- **RT-04** (Best Practice Review): Android architecture component patterns
- **ST-03** (Output Format Templates): Code templates for each component
- **NE-02** (Phased Workflow): Clear phases with checkpoint approvals
- **NE-07** (Discussion Before Action): Checkpoints for data model review

---

## Related Prompts

- [android_feature_specification.md](../planning/android_feature_specification.md) - Create feature spec before data layer
- [android_api_integration.md](android_api_integration.md) - Implement the remote API layer
- [android_dependency_injection.md](android_dependency_injection.md) - Configure Hilt/Dagger DI
- [android_offline_first_sync.md](android_offline_first_sync.md) - Advanced offline-first patterns
- [android_unit_test_generation.md](../testing/android_unit_test_generation.md) - Test the data layer

---

## Customization Guide

### For Local-Only Storage

If no remote sync is needed:
- Remove RemoteDataSource and API components
- Simplify repository to wrap local data source directly
- Remove sync status fields from entities

### For Read-Heavy Workloads

If data changes infrequently:
- Add more aggressive caching in repository
- Use `distinctUntilChanged()` on Flow queries
- Consider in-memory caching layer

### For Write-Heavy Workloads

If data changes frequently:
- Batch inserts using transactions
- Debounce rapid updates
- Consider WAL mode for database

### For Very Large Datasets

If handling thousands of items:
- Implement Paging 3 library integration
- Add cursor-based pagination to DAO
- Consider partial loading strategies

### For Multi-Module Projects

If in a modular architecture:
- Place database in `:core:database` module
- Repository interfaces in `:core:domain`
- Repository implementations in `:data` module
- Expose only domain models across module boundaries
