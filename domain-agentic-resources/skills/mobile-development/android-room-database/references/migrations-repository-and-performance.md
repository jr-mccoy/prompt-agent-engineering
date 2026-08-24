# Android Room Database — Migrations, Repository Pattern & Performance

## Migrations

### Basic Migration

```kotlin
val MIGRATION_1_2 = object : Migration(1, 2) {
    override fun migrate(database: SupportSQLiteDatabase) {
        // Add new column
        database.execSQL(
            "ALTER TABLE users ADD COLUMN profile_picture TEXT"
        )
    }
}
```

### Complex Migration with Data Transformation

```kotlin
val MIGRATION_2_3 = object : Migration(2, 3) {
    override fun migrate(database: SupportSQLiteDatabase) {
        // Create new table with updated schema
        database.execSQL("""
            CREATE TABLE users_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                user_name TEXT NOT NULL,
                email TEXT NOT NULL,
                created_at INTEGER NOT NULL DEFAULT 0,
                is_active INTEGER NOT NULL DEFAULT 1,
                profile_picture TEXT
            )
        """)

        // Copy data from old table
        database.execSQL("""
            INSERT INTO users_new (id, user_name, email, created_at, is_active, profile_picture)
            SELECT id, name, email, created_at, 1, profile_picture
            FROM users
        """)

        // Remove old table
        database.execSQL("DROP TABLE users")

        // Rename new table
        database.execSQL("ALTER TABLE users_new RENAME TO users")

        // Recreate indices
        database.execSQL("CREATE INDEX index_users_email ON users (email)")
    }
}
```

### Auto Migration (Room 2.4+)

```kotlin
@Database(
    entities = [User::class],
    version = 3,
    autoMigrations = [
        AutoMigration(from = 1, to = 2),
        AutoMigration(from = 2, to = 3, spec = Migration2To3::class)
    ]
)
abstract class AppDatabase : RoomDatabase()

@DeleteColumn(tableName = "users", columnName = "old_field")
@RenameColumn(tableName = "users", fromColumnName = "name", toColumnName = "user_name")
class Migration2To3 : AutoMigrationSpec
```

### Migration Testing

```kotlin
@RunWith(AndroidJUnit4::class)
class MigrationTest {
    private val testDb = "migration-test"

    @get:Rule
    val helper = MigrationTestHelper(
        InstrumentationRegistry.getInstrumentation(),
        AppDatabase::class.java
    )

    @Test
    fun migrate1To2() {
        // Create database with version 1
        helper.createDatabase(testDb, 1).apply {
            execSQL("""
                INSERT INTO users (id, name, email)
                VALUES (1, 'John', 'john@email.com')
            """)
            close()
        }

        // Run migration
        helper.runMigrationsAndValidate(testDb, 2, true, MIGRATION_1_2)

        // Verify data
        val db = helper.openDatabase(testDb, 2)
        val cursor = db.query("SELECT * FROM users WHERE id = 1")
        assertTrue(cursor.moveToFirst())
        assertEquals("John", cursor.getString(cursor.getColumnIndex("name")))
        assertNull(cursor.getString(cursor.getColumnIndex("profile_picture")))
        cursor.close()
    }
}
```

---

## Repository Pattern

### Repository Implementation

```kotlin
class TaskRepository @Inject constructor(
    private val taskDao: TaskDao,
    private val ioDispatcher: CoroutineDispatcher = Dispatchers.IO
) {
    fun observeAllTasks(): Flow<List<Task>> =
        taskDao.observeAll()
            .flowOn(ioDispatcher)

    fun observeTaskById(taskId: Long): Flow<Task?> =
        taskDao.observeById(taskId)
            .flowOn(ioDispatcher)

    suspend fun getTaskById(taskId: Long): Task? =
        withContext(ioDispatcher) {
            taskDao.getById(taskId)
        }

    suspend fun insertTask(task: Task): Result<Long> =
        withContext(ioDispatcher) {
            try {
                Result.success(taskDao.insert(task))
            } catch (e: Exception) {
                Result.failure(e)
            }
        }

    suspend fun updateTask(task: Task): Result<Unit> =
        withContext(ioDispatcher) {
            try {
                taskDao.update(task)
                Result.success(Unit)
            } catch (e: Exception) {
                Result.failure(e)
            }
        }

    suspend fun deleteTask(task: Task): Result<Unit> =
        withContext(ioDispatcher) {
            try {
                taskDao.delete(task)
                Result.success(Unit)
            } catch (e: Exception) {
                Result.failure(e)
            }
        }
}
```

---

## Performance Optimization

### Index Optimization

```kotlin
@Entity(
    tableName = "messages",
    indices = [
        Index(value = ["conversation_id", "timestamp"]),  // Composite index
        Index(value = ["sender_id"]),
        Index(value = ["is_read"])  // Good for boolean filters
    ]
)
data class Message(...)
```

### Pagination with Paging 3

```kotlin
@Dao
interface TaskDao {
    @Query("SELECT * FROM tasks ORDER BY created_at DESC")
    fun pagingSource(): PagingSource<Int, Task>
}

// In Repository
fun getPagedTasks(): Flow<PagingData<Task>> {
    return Pager(
        config = PagingConfig(
            pageSize = 20,
            enablePlaceholders = false,
            maxSize = 100
        ),
        pagingSourceFactory = { taskDao.pagingSource() }
    ).flow
}

// In ViewModel
val pagedTasks: Flow<PagingData<Task>> = repository.getPagedTasks()
    .cachedIn(viewModelScope)
```

### Write-Ahead Logging (WAL)

```kotlin
Room.databaseBuilder(context, AppDatabase::class.java, "app.db")
    .setJournalMode(RoomDatabase.JournalMode.WRITE_AHEAD_LOGGING)
    .build()
```

---

## Common Issues

### Issue: Migration Failed

**Quick Diagnosis:**
```kotlin
// Enable logging
Room.databaseBuilder(...)
    .setQueryCallback({ sqlQuery, bindArgs ->
        Log.d("Room", "Query: $sqlQuery Args: $bindArgs")
    }, Executors.newSingleThreadExecutor())
```

**Resolution:**
1. Ensure schema exports are enabled
2. Compare expected vs actual schema
3. Fix migration SQL to match schema exactly
4. Test migrations with MigrationTestHelper

### Issue: Query Performance Slow

**Quick Diagnosis:**
```sql
EXPLAIN QUERY PLAN SELECT * FROM tasks WHERE user_id = ?
```

**Resolution:**
1. Add appropriate indices
2. Use LIMIT for large result sets
3. Avoid SELECT * when possible
4. Use `@RawQuery` for dynamic complex queries

### Issue: Conflicting Entity Updates

**Resolution:**
```kotlin
// Use proper conflict strategy
@Insert(onConflict = OnConflictStrategy.REPLACE)
suspend fun upsert(entity: Entity)

// Or handle manually
@Transaction
open suspend fun upsertTask(task: Task) {
    val existing = getById(task.id)
    if (existing != null) {
        update(task)
    } else {
        insert(task)
    }
}
```

### Issue: Type Converter Not Found

**Resolution:**
```kotlin
// Register at Database level
@Database(...)
@TypeConverters(Converters::class)
abstract class AppDatabase

// Or at DAO level for specific DAOs
@Dao
@TypeConverters(SpecificConverters::class)
interface SpecificDao
```

---

## Best Practices Summary

1. **Export Schemas:** Always set `exportSchema = true` for migration testing
2. **Use Flow:** Prefer Flow over LiveData for reactive queries
3. **Suspend Functions:** Use suspend for one-shot operations
4. **Indices:** Add indices for frequently queried columns
5. **Foreign Keys:** Define relationships explicitly with foreign keys
6. **Transactions:** Wrap related operations in @Transaction
7. **Testing:** Write migration tests for all schema changes
8. **Type Converters:** Keep them simple; complex objects should be normalized
9. **Repository:** Wrap DAO access in Repository for abstraction
10. **Error Handling:** Handle database exceptions in Repository layer

## Related Skills

- `android-hilt-di` - Dependency injection for database modules
- `android-testing-patterns` - Testing Room databases
- `jetpack-compose-patterns` - Displaying Room data in Compose
