---
name: android-room-database
description: Master Room persistence library for Android including entity design, DAO patterns, migrations, type converters, and Flow/coroutines integration. Use this skill when working with local databases in Android, implementing data persistence, creating database migrations, or when users mention "Room database", "Room migration", "DAO", "Entity", "@Database", "type converter", or "database schema".
metadata:
  tags:
    - android
    - database
    - migration
    - mobile
    - room
  updated: "2026-04-11"
---
# Android Room Database

Comprehensive guidance for implementing local data persistence with Room, covering entity design, DAO patterns, migrations, type converters, and reactive data access with Flow and coroutines.

## Purpose

This skill provides patterns and best practices for Room database development, helping developers:
- Design efficient database schemas with proper entity relationships
- Implement type-safe DAOs with coroutines and Flow support
- Create and manage database migrations safely
- Use type converters for complex data types
- Integrate Room with ViewModel and Repository patterns

## When to Use This Skill

Use this skill when you need to:
- Set up Room database in an Android app
- Design database entities and relationships
- Create DAOs for data access
- Implement database migrations
- Add type converters for custom types
- Query data reactively with Flow
- Optimize database performance
- Debug Room-related issues

## When NOT to Use This Skill

Do NOT use this skill when:
- Working with remote databases only (use Retrofit/Firebase skills)
- Need simple key-value storage (use DataStore)
- Working with iOS or cross-platform (use platform-specific skills)
- Need encrypted database (combine with SQLCipher patterns)
- Building non-Android applications

## Core Patterns

### Database Setup

#### Basic Database Configuration

```kotlin
@Database(
    entities = [User::class, Task::class, Tag::class],
    version = 1,
    exportSchema = true  // Always export for migration testing
)
@TypeConverters(Converters::class)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
    abstract fun taskDao(): TaskDao
    abstract fun tagDao(): TagDao
}
```

#### Database Provider with Hilt

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object DatabaseModule {

    @Provides
    @Singleton
    fun provideDatabase(
        @ApplicationContext context: Context
    ): AppDatabase {
        return Room.databaseBuilder(
            context,
            AppDatabase::class.java,
            "app_database"
        )
            .addMigrations(MIGRATION_1_2, MIGRATION_2_3)
            .fallbackToDestructiveMigration()  // Only for debug builds!
            .build()
    }

    @Provides
    fun provideUserDao(database: AppDatabase): UserDao {
        return database.userDao()
    }

    @Provides
    fun provideTaskDao(database: AppDatabase): TaskDao {
        return database.taskDao()
    }
}
```

### Entity Design

#### Basic Entity

```kotlin
@Entity(tableName = "users")
data class User(
    @PrimaryKey(autoGenerate = true)
    val id: Long = 0,

    @ColumnInfo(name = "user_name")
    val userName: String,

    @ColumnInfo(name = "email")
    val email: String,

    @ColumnInfo(name = "created_at")
    val createdAt: Long = System.currentTimeMillis(),

    @ColumnInfo(name = "is_active", defaultValue = "1")
    val isActive: Boolean = true
)
```

#### Entity with Indices

```kotlin
@Entity(
    tableName = "tasks",
    indices = [
        Index(value = ["user_id"]),
        Index(value = ["due_date"]),
        Index(value = ["title"], unique = false)
    ],
    foreignKeys = [
        ForeignKey(
            entity = User::class,
            parentColumns = ["id"],
            childColumns = ["user_id"],
            onDelete = ForeignKey.CASCADE
        )
    ]
)
data class Task(
    @PrimaryKey(autoGenerate = true)
    val id: Long = 0,

    @ColumnInfo(name = "user_id")
    val userId: Long,

    val title: String,

    val description: String?,

    @ColumnInfo(name = "due_date")
    val dueDate: Long?,

    @ColumnInfo(name = "is_completed")
    val isCompleted: Boolean = false,

    val priority: Priority = Priority.MEDIUM
)

enum class Priority {
    LOW, MEDIUM, HIGH, URGENT
}
```

#### Embedded Objects

```kotlin
data class Address(
    val street: String,
    val city: String,
    val state: String,
    @ColumnInfo(name = "zip_code")
    val zipCode: String
)

@Entity(tableName = "users")
data class User(
    @PrimaryKey(autoGenerate = true)
    val id: Long = 0,
    val name: String,
    @Embedded(prefix = "home_")
    val homeAddress: Address?,
    @Embedded(prefix = "work_")
    val workAddress: Address?
)
```

#### Many-to-Many Relationship

```kotlin
@Entity(tableName = "tasks")
data class Task(
    @PrimaryKey(autoGenerate = true)
    val taskId: Long = 0,
    val title: String
)

@Entity(tableName = "tags")
data class Tag(
    @PrimaryKey(autoGenerate = true)
    val tagId: Long = 0,
    val name: String,
    val color: String
)

@Entity(
    tableName = "task_tag_cross_ref",
    primaryKeys = ["taskId", "tagId"],
    foreignKeys = [
        ForeignKey(
            entity = Task::class,
            parentColumns = ["taskId"],
            childColumns = ["taskId"],
            onDelete = ForeignKey.CASCADE
        ),
        ForeignKey(
            entity = Tag::class,
            parentColumns = ["tagId"],
            childColumns = ["tagId"],
            onDelete = ForeignKey.CASCADE
        )
    ]
)
data class TaskTagCrossRef(
    val taskId: Long,
    val tagId: Long
)

data class TaskWithTags(
    @Embedded val task: Task,
    @Relation(
        parentColumn = "taskId",
        entityColumn = "tagId",
        associateBy = Junction(TaskTagCrossRef::class)
    )
    val tags: List<Tag>
)
```

### DAO Patterns

#### Basic CRUD Operations

```kotlin
@Dao
interface UserDao {
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(user: User): Long

    @Insert(onConflict = OnConflictStrategy.IGNORE)
    suspend fun insertAll(users: List<User>): List<Long>

    @Update
    suspend fun update(user: User)

    @Delete
    suspend fun delete(user: User)

    @Query("DELETE FROM users WHERE id = :userId")
    suspend fun deleteById(userId: Long)

    @Query("DELETE FROM users")
    suspend fun deleteAll()
}
```

#### Flow-Based Queries

```kotlin
@Dao
interface TaskDao {
    // Observe all tasks reactively
    @Query("SELECT * FROM tasks ORDER BY due_date ASC")
    fun observeAll(): Flow<List<Task>>

    // Observe single task
    @Query("SELECT * FROM tasks WHERE id = :taskId")
    fun observeById(taskId: Long): Flow<Task?>

    // Observe with filter
    @Query("SELECT * FROM tasks WHERE is_completed = :isCompleted")
    fun observeByStatus(isCompleted: Boolean): Flow<List<Task>>

    // One-shot query (suspend)
    @Query("SELECT * FROM tasks WHERE id = :taskId")
    suspend fun getById(taskId: Long): Task?

    // Count query
    @Query("SELECT COUNT(*) FROM tasks WHERE is_completed = 0")
    fun observePendingCount(): Flow<Int>
}
```

#### Complex Queries

```kotlin
@Dao
interface TaskDao {
    // Query with multiple parameters
    @Query("""
        SELECT * FROM tasks
        WHERE user_id = :userId
        AND is_completed = :isCompleted
        AND (due_date IS NULL OR due_date >= :fromDate)
        ORDER BY priority DESC, due_date ASC
    """)
    fun getTasksFiltered(
        userId: Long,
        isCompleted: Boolean,
        fromDate: Long
    ): Flow<List<Task>>

    // Full-text search (requires FTS entity)
    @Query("""
        SELECT * FROM tasks
        WHERE title LIKE '%' || :query || '%'
        OR description LIKE '%' || :query || '%'
    """)
    fun search(query: String): Flow<List<Task>>

    // Aggregation
    @Query("""
        SELECT priority, COUNT(*) as count
        FROM tasks
        WHERE user_id = :userId
        GROUP BY priority
    """)
    fun getTaskCountByPriority(userId: Long): Flow<List<PriorityCount>>
}

data class PriorityCount(
    val priority: Priority,
    val count: Int
)
```

#### Transaction Operations

```kotlin
@Dao
abstract class TaskDao {
    @Insert
    abstract suspend fun insertTask(task: Task): Long

    @Insert
    abstract suspend fun insertTags(tags: List<Tag>): List<Long>

    @Insert
    abstract suspend fun insertTaskTagRefs(refs: List<TaskTagCrossRef>)

    @Transaction
    open suspend fun insertTaskWithTags(task: Task, tags: List<Tag>) {
        val taskId = insertTask(task)
        val tagIds = insertTags(tags)
        val refs = tagIds.map { tagId ->
            TaskTagCrossRef(taskId = taskId, tagId = tagId)
        }
        insertTaskTagRefs(refs)
    }

    @Transaction
    @Query("SELECT * FROM tasks WHERE id = :taskId")
    abstract fun getTaskWithTags(taskId: Long): Flow<TaskWithTags?>
}
```

### Type Converters

#### Standard Converters

```kotlin
class Converters {
    // Date conversion
    @TypeConverter
    fun fromTimestamp(value: Long?): Date? {
        return value?.let { Date(it) }
    }

    @TypeConverter
    fun dateToTimestamp(date: Date?): Long? {
        return date?.time
    }

    // Enum conversion
    @TypeConverter
    fun fromPriority(priority: Priority): String {
        return priority.name
    }

    @TypeConverter
    fun toPriority(value: String): Priority {
        return Priority.valueOf(value)
    }

    // List conversion (use with caution - consider normalization)
    @TypeConverter
    fun fromStringList(list: List<String>): String {
        return list.joinToString(",")
    }

    @TypeConverter
    fun toStringList(value: String): List<String> {
        return if (value.isEmpty()) emptyList() else value.split(",")
    }

    // JSON conversion for complex objects
    @TypeConverter
    fun fromJson(json: String): Map<String, Any> {
        return Json.decodeFromString(json)
    }

    @TypeConverter
    fun toJson(map: Map<String, Any>): String {
        return Json.encodeToString(map)
    }
}
```

## Migrations, Repository Pattern, Performance & Common Issues

Basic migration (MIGRATION_1_2 ALTER TABLE ADD COLUMN), complex migration (MIGRATION_2_3 with CREATE TABLE + INSERT + DROP + RENAME + CREATE INDEX), Auto Migration (Room 2.4+ with @DeleteColumn/@RenameColumn/AutoMigrationSpec), MigrationTestHelper instrumented test, Repository Pattern (TaskRepository @Inject constructor with Result<T> wrapper for all operations), Performance Optimization (composite index, Paging 3 with PagingSource/Pager/cachedIn, WRITE_AHEAD_LOGGING), Common Issues (Migration Failed/Slow Query/Conflicting Entity Updates/Type Converter Not Found), Best Practices (10 points), Related Skills.

See [references/migrations-repository-and-performance.md](references/migrations-repository-and-performance.md)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/migrations-repository-and-performance.md` | Migrations, repository pattern, performance optimization, common issues, best practices |
