---
title: "Android Integration Testing"
category: mobile-development
description: "Implements integration tests verifying database operations, API interactions, and repository-level data flows work correctly"
tags:
  - android
  - mobile-development
  - testing
updated: "2026-03-19"
---

# Android Integration Testing

**Objective:** Implement integration tests that verify multiple components work together correctly, including database operations, API interactions, and repository-level data flows.

**When to Use:** Use this prompt when validating that Room database operations work correctly, when testing API service implementations with MockWebServer, when verifying repository logic that coordinates local and remote data sources, or when ensuring data layer components integrate properly.

**Prompt Type:** Modular (120-150 lines)

---

## Context Gathering

1. **Integration Targets:**
   - "What components need integration testing? (Database, API, Repository)"
   - "Are you using Room, Retrofit, or other specific libraries?"

2. **Data Layer Structure:**
   - "Do you have separate local/remote data sources?"
   - "Is there caching or offline-first logic to test?"

3. **Test Environment:**
   - "Is Hilt/Dagger used for dependency injection?"
   - "Are there existing integration tests to reference?"

---

## Instructions

### CRITICAL: Implementation Requirements

**Before generating ANY test, you MUST:**

1. **Understand the integration points** - Read the actual implementation to understand how components interact.
2. **Check for existing integration tests** - Search for existing test patterns, in-memory databases, or mock servers.
3. **Follow project conventions** - Match existing test naming, setup, and assertion patterns.
4. **Provide specific, working tests** - All tests MUST include file paths and be immediately runnable.
5. **Include proper test isolation** - Each test should clean up state and not affect other tests.

**Adapting to existing test patterns is required.** Match the project's testing style.

### Quality Requirements

- ❌ Do NOT use production databases or real APIs in integration tests
- ❌ Do NOT generate tests that depend on external network availability
- ❌ Do NOT skip cleanup that could cause test interdependence
- ❌ Do NOT generate overly broad tests that are hard to debug
- ✅ DO use in-memory databases for Room testing
- ✅ DO use MockWebServer for API testing
- ✅ DO test actual data transformations, not just mock passthrough
- ✅ DO specify exact file paths for all test files

---

### Phase 1: Test Setup

#### 1.1 Dependencies

```kotlin
// build.gradle.kts
dependencies {
    // AndroidX Test
    androidTestImplementation("androidx.test:core:1.5.0")
    androidTestImplementation("androidx.test:runner:1.5.2")
    androidTestImplementation("androidx.test:rules:1.5.0")
    androidTestImplementation("androidx.test.ext:junit:1.1.5")

    // Room Testing
    androidTestImplementation("androidx.room:room-testing:2.6.1")

    // Coroutines Test
    androidTestImplementation("org.jetbrains.kotlinx:kotlinx-coroutines-test:1.7.3")

    // MockWebServer for API testing
    androidTestImplementation("com.squareup.okhttp3:mockwebserver:4.12.0")

    // Hilt Testing
    androidTestImplementation("com.google.dagger:hilt-android-testing:2.48.1")
    kspAndroidTest("com.google.dagger:hilt-compiler:2.48.1")

    // Truth for assertions
    androidTestImplementation("com.google.truth:truth:1.1.5")
}
```

---

### Phase 2: Database Integration Tests

#### 2.1 Room DAO Tests

```kotlin
@RunWith(AndroidJUnit4::class)
class ItemDaoTest {

    private lateinit var database: AppDatabase
    private lateinit var itemDao: ItemDao

    @Before
    fun setup() {
        val context = ApplicationProvider.getApplicationContext<Context>()
        database = Room.inMemoryDatabaseBuilder(context, AppDatabase::class.java)
            .allowMainThreadQueries() // Only for testing
            .build()
        itemDao = database.itemDao()
    }

    @After
    fun teardown() {
        database.close()
    }

    // Insert and retrieve tests
    @Test
    fun insertItem_retrievesCorrectItem() = runTest {
        val item = ItemEntity(id = "1", name = "Test Item", createdAt = System.currentTimeMillis())

        itemDao.insert(item)
        val retrieved = itemDao.getById("1")

        assertThat(retrieved).isEqualTo(item)
    }

    @Test
    fun insertAll_retrievesAllItems() = runTest {
        val items = listOf(
            ItemEntity(id = "1", name = "Item 1", createdAt = 1000L),
            ItemEntity(id = "2", name = "Item 2", createdAt = 2000L)
        )

        itemDao.insertAll(items)
        val retrieved = itemDao.getAll().first()

        assertThat(retrieved).hasSize(2)
    }

    // Update tests
    @Test
    fun updateItem_updatesCorrectly() = runTest {
        val item = ItemEntity(id = "1", name = "Original", createdAt = 1000L)
        itemDao.insert(item)

        val updated = item.copy(name = "Updated")
        itemDao.update(updated)

        val retrieved = itemDao.getById("1")
        assertThat(retrieved?.name).isEqualTo("Updated")
    }

    // Delete tests
    @Test
    fun deleteItem_removesFromDatabase() = runTest {
        val item = ItemEntity(id = "1", name = "Test", createdAt = 1000L)
        itemDao.insert(item)

        itemDao.delete(item)

        val retrieved = itemDao.getById("1")
        assertThat(retrieved).isNull()
    }

    // Query tests
    @Test
    fun getItemsByCategory_returnsFilteredResults() = runTest {
        val items = listOf(
            ItemEntity(id = "1", name = "Item 1", category = "A", createdAt = 1000L),
            ItemEntity(id = "2", name = "Item 2", category = "B", createdAt = 2000L),
            ItemEntity(id = "3", name = "Item 3", category = "A", createdAt = 3000L)
        )
        itemDao.insertAll(items)

        val categoryA = itemDao.getByCategory("A").first()

        assertThat(categoryA).hasSize(2)
        assertThat(categoryA.map { it.id }).containsExactly("1", "3")
    }

    // Flow emission tests
    @Test
    fun getAllFlow_emitsOnChanges() = runTest {
        val emissions = mutableListOf<List<ItemEntity>>()

        val job = launch {
            itemDao.getAll().take(3).toList(emissions)
        }

        itemDao.insert(ItemEntity(id = "1", name = "First", createdAt = 1000L))
        itemDao.insert(ItemEntity(id = "2", name = "Second", createdAt = 2000L))

        job.join()

        assertThat(emissions).hasSize(3)
        assertThat(emissions[0]).isEmpty()
        assertThat(emissions[1]).hasSize(1)
        assertThat(emissions[2]).hasSize(2)
    }
}
```

#### 2.2 Database Migration Tests

```kotlin
@RunWith(AndroidJUnit4::class)
class MigrationTest {

    @get:Rule
    val migrationTestHelper = MigrationTestHelper(
        InstrumentationRegistry.getInstrumentation(),
        AppDatabase::class.java
    )

    @Test
    fun migrate1To2_preservesData() {
        // Create database with version 1
        migrationTestHelper.createDatabase(TEST_DB_NAME, 1).apply {
            execSQL("INSERT INTO items (id, name) VALUES ('1', 'Test Item')")
            close()
        }

        // Run migration
        val db = migrationTestHelper.runMigrationsAndValidate(
            TEST_DB_NAME, 2, true, MIGRATION_1_2
        )

        // Verify data preserved and new column exists
        val cursor = db.query("SELECT * FROM items WHERE id = '1'")
        assertThat(cursor.moveToFirst()).isTrue()
        assertThat(cursor.getString(cursor.getColumnIndex("name"))).isEqualTo("Test Item")

        // New column should have default value
        val newColumnIndex = cursor.getColumnIndex("created_at")
        assertThat(newColumnIndex).isNotEqualTo(-1)
    }

    companion object {
        private const val TEST_DB_NAME = "test_database"
    }
}
```

---

### Phase 3: API Integration Tests

#### 3.1 MockWebServer Setup

```kotlin
@RunWith(AndroidJUnit4::class)
class ApiServiceTest {

    private lateinit var mockWebServer: MockWebServer
    private lateinit var apiService: ApiService

    @Before
    fun setup() {
        mockWebServer = MockWebServer()
        mockWebServer.start()

        val retrofit = Retrofit.Builder()
            .baseUrl(mockWebServer.url("/"))
            .addConverterFactory(Json.asConverterFactory("application/json".toMediaType()))
            .build()

        apiService = retrofit.create(ApiService::class.java)
    }

    @After
    fun teardown() {
        mockWebServer.shutdown()
    }

    @Test
    fun getItems_success_parsesResponse() = runTest {
        val responseJson = """
            {
                "items": [
                    {"id": "1", "name": "Item 1"},
                    {"id": "2", "name": "Item 2"}
                ]
            }
        """.trimIndent()

        mockWebServer.enqueue(
            MockResponse()
                .setResponseCode(200)
                .setBody(responseJson)
        )

        val response = apiService.getItems()

        assertThat(response.items).hasSize(2)
        assertThat(response.items[0].name).isEqualTo("Item 1")
    }

    @Test
    fun getItems_serverError_throwsException() = runTest {
        mockWebServer.enqueue(
            MockResponse().setResponseCode(500)
        )

        assertThrows<HttpException> {
            apiService.getItems()
        }
    }

    @Test
    fun createItem_sendsCorrectRequest() = runTest {
        mockWebServer.enqueue(
            MockResponse()
                .setResponseCode(201)
                .setBody("""{"id": "new-id", "name": "New Item"}""")
        )

        apiService.createItem(CreateItemRequest(name = "New Item"))

        val request = mockWebServer.takeRequest()
        assertThat(request.method).isEqualTo("POST")
        assertThat(request.path).isEqualTo("/items")
        assertThat(request.body.readUtf8()).contains("New Item")
    }

    @Test
    fun getItems_networkError_throwsIOException() = runTest {
        mockWebServer.shutdown() // Simulate network unavailable

        assertThrows<IOException> {
            apiService.getItems()
        }
    }
}
```

---

### Phase 4: Repository Integration Tests

#### 4.1 Full Repository Tests

```kotlin
@HiltAndroidTest
@RunWith(AndroidJUnit4::class)
class ItemRepositoryIntegrationTest {

    @get:Rule
    val hiltRule = HiltAndroidRule(this)

    @Inject
    lateinit var database: AppDatabase

    @Inject
    lateinit var repository: ItemRepository

    private lateinit var mockWebServer: MockWebServer

    @Before
    fun setup() {
        hiltRule.inject()
        mockWebServer = MockWebServer()
        mockWebServer.start()
    }

    @After
    fun teardown() {
        database.close()
        mockWebServer.shutdown()
    }

    @Test
    fun getData_cacheEmpty_fetchesFromRemote() = runTest {
        mockWebServer.enqueue(successResponse())

        val result = repository.getData()

        assertThat(result.isSuccess).isTrue()
        assertThat(result.getOrNull()).isNotEmpty()

        // Verify cached
        val cached = database.itemDao().getAll().first()
        assertThat(cached).isNotEmpty()
    }

    @Test
    fun getData_cacheAvailable_returnsCache() = runTest {
        // Pre-populate cache
        database.itemDao().insert(testEntity())

        val result = repository.getData()

        assertThat(result.isSuccess).isTrue()
        // No network request should be made
        assertThat(mockWebServer.requestCount).isEqualTo(0)
    }

    @Test
    fun refresh_updatesCache() = runTest {
        // Initial cache
        database.itemDao().insert(testEntity(name = "Old"))

        mockWebServer.enqueue(successResponse(name = "New"))

        repository.refresh()

        val cached = database.itemDao().getAll().first()
        assertThat(cached[0].name).isEqualTo("New")
    }

    private fun successResponse(name: String = "Test") = MockResponse()
        .setResponseCode(200)
        .setBody("""{"items": [{"id": "1", "name": "$name"}]}""")

    private fun testEntity(name: String = "Test") = ItemEntity(
        id = "1",
        name = name,
        createdAt = System.currentTimeMillis()
    )
}
```

---

## Expected Output

```markdown
## Integration Tests for [Component]

### Test Coverage
| Component | Test Count | Scenarios |
|-----------|------------|-----------|
| Database (DAO) | [X] | CRUD, Queries, Flows |
| API Service | [X] | Success, Errors, Request validation |
| Repository | [X] | Cache logic, Sync, Error handling |

### Generated Tests
[Complete test classes organized by component]
```

---

## Techniques Used

- **ST-01** (Clear Objective): Integration test implementation
- **RT-04** (Best Practice Review): Android testing patterns
- **ST-03** (Output Format Templates): Organized test structure

---

## Related Prompts

- [android_test_strategy_design.md](android_test_strategy_design.md) - Overall test strategy
- [android_unit_test_generation.md](android_unit_test_generation.md) - Unit tests for business logic
- [android_data_layer_implementation.md](../implementation/android_data_layer_implementation.md) - Data layer patterns
