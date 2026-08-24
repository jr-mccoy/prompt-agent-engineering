---
title: "Android Repository Pattern Review"
category: mobile/android/targeted-reviews
description: "Android Repository Pattern Review."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - mobile
  - pattern
  - repository
  - review
  - reviews
updated: "2026-03-19"
related_prompts: []
---

# Android Repository Pattern Review

**Objective:** Conduct a targeted review of repository pattern implementation in Android applications, analyzing data source abstraction, reactive data patterns, caching strategies, error handling, and proper separation of concerns between data and domain layers.

**When to Use:** Use this prompt when reviewing data layer architecture, debugging data flow issues, optimizing data access patterns, ensuring proper separation of concerns, or during architecture refactoring. Essential for apps transitioning to clean architecture or implementing offline-first patterns.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the actual data flow** - Don't flag based on pattern matching alone. Verify that the suspected architectural issue actually causes problems.
2. **Check for existing abstractions** - Search for interfaces, mappers, or adapters that may already address the concern.
3. **Understand the context** - Consider WHY the repository is designed this way. Project constraints and team preferences are valid factors.
4. **Confirm actual maintainability impact** - Can this actually cause confusion, bugs, or testability issues?
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `UserRepository.kt:45`).

**Finding NO issues is an acceptable outcome.** If the repository pattern implementation is clean and functional, say so with confidence. Don't manufacture architectural concerns.

### False-Positive Prevention

- ❌ Do NOT flag all deviations from "pure" clean architecture as problems
- ❌ Do NOT flag pragmatic shortcuts that work well for the project size
- ❌ Do NOT assume missing abstraction without understanding the team's architecture decisions
- ❌ Do NOT report theoretical issues that don't affect real-world maintainability
- ✅ DO consider the project's size and complexity when evaluating architecture
- ✅ DO understand that not every app needs full clean architecture
- ✅ DO check if repositories are testable as-is before flagging concerns
- ✅ DO consider the trade-off between abstraction and simplicity

---

### 1. Repository Interface Design

Analyze repository contracts:

* **Interface Definition:**
  - Review repository interfaces in domain layer
  - Check for proper abstraction (no implementation details leak)
  - Assess method signatures (suspend functions, Flows)
  - Verify interface segregation (focused interfaces)

* **Method Naming:**
  - Review naming conventions (get, fetch, observe, save)
  - Check for consistent terminology across repositories
  - Assess clarity of method purpose
  - Verify CRUD operations coverage

* **Return Types:**
  - Review Flow vs. suspend function usage
  - Check for proper reactive data exposure
  - Assess Result/Either wrapper usage for errors
  - Verify nullable vs. non-nullable returns

### 2. Data Source Management

Evaluate data source handling:

* **Local Data Source:**
  - Review Room DAO integration
  - Check for proper data mapping (Entity to Domain)
  - Assess caching implementation
  - Verify data source independence

* **Remote Data Source:**
  - Review API service integration
  - Check for proper DTO handling
  - Assess network error handling
  - Verify response mapping to domain models

* **Source Coordination:**
  - Review local-first vs. remote-first strategies
  - Check for proper cache invalidation
  - Assess data freshness policies
  - Verify conflict handling between sources

### 3. Reactive Data Patterns

Analyze Flow usage:

* **Observable Data:**
  - Review Flow emission patterns
  - Check for proper Flow operators
  - Assess distinctUntilChanged usage
  - Verify Flow transformation efficiency

* **Single-Shot Operations:**
  - Review suspend function usage
  - Check for proper coroutine scope
  - Assess timeout handling
  - Verify cancellation support

* **Combined Flows:**
  - Review combine, zip, merge usage
  - Check for efficient Flow composition
  - Assess hot vs. cold Flow understanding
  - Verify proper error propagation

### 4. Caching Strategy

Evaluate caching implementation:

* **Cache Policies:**
  - Review cache-first vs. network-first strategies
  - Check for cache expiration policies
  - Assess cache size management
  - Verify cache invalidation triggers

* **Stale-While-Revalidate:**
  - Review background refresh patterns
  - Check for proper stale data handling
  - Assess user experience during refresh
  - Verify no duplicate network calls

* **Cache Consistency:**
  - Review cache update after write operations
  - Check for optimistic updates
  - Assess rollback on server failure
  - Verify cross-repository cache consistency

### 5. Error Handling

Analyze error management:

* **Error Types:**
  - Review error classification (network, validation, business)
  - Check for typed error handling (sealed classes)
  - Assess error mapping from data to domain
  - Verify user-friendly error messages

* **Error Propagation:**
  - Review how errors flow to UI layer
  - Check for proper try-catch placement
  - Assess error recovery strategies
  - Verify no swallowed exceptions

* **Retry Mechanisms:**
  - Review retry policies for transient errors
  - Check for exponential backoff
  - Assess retry limits
  - Verify circuit breaker patterns

### 6. Data Mapping

Evaluate model transformations:

* **Mapper Implementation:**
  - Review Entity to Domain model mapping
  - Check for DTO to Domain mapping
  - Assess mapper testing
  - Verify bidirectional mapping where needed

* **Mapping Location:**
  - Check mappers are in appropriate layer
  - Review mapping consistency
  - Assess extension function vs. mapper class
  - Verify no domain logic in mappers

### 7. Dependency Injection

Analyze DI patterns:

* **Repository Binding:**
  - Review interface-to-implementation binding
  - Check for proper scope (@Singleton appropriate?)
  - Assess repository dependencies
  - Verify testability through DI

* **Data Source Injection:**
  - Review DAO and API service injection
  - Check for proper abstraction
  - Assess dispatcher injection
  - Verify no hidden dependencies

### 8. Testing Considerations

Evaluate testability:

* **Mock-Friendly Design:**
  - Review interface-based design
  - Check for injectable dependencies
  - Assess fake implementation feasibility
  - Verify no static dependencies

* **Test Coverage:**
  - Review repository unit tests
  - Check for data source mocking
  - Assess Flow testing patterns
  - Verify error scenario coverage

---

## Expected Output

Provide a comprehensive repository pattern review report including:

### 1. Executive Summary
- Overall data layer health rating
- Repository count and scope
- Pattern compliance assessment
- Critical issues count

### 2. Repository Inventory

| Repository | Interface | Sources | Caching | Issues |
|------------|-----------|---------|---------|--------|
| [Name] | [Yes/No] | [List] | [Strategy] | [Count] |

### 3. Data Flow Analysis

For each repository:
- Data source diagram
- Caching strategy
- Error handling approach
- Reactive patterns

### 4. Detailed Findings

For each issue:
- **Location:** Repository and method
- **Issue:** Description
- **Impact:** Data integrity/performance effect
- **Severity:** Critical/High/Medium/Low
- **Current Code:** Problematic pattern
- **Recommended Fix:** Corrected implementation

### 5. Prioritized Recommendations

Ordered by data integrity and architecture impact.

---

## Example Output

```markdown
# Repository Pattern Review Report

## Executive Summary
- **Overall Health:** Needs Improvement
- **Repositories Reviewed:** 8
- **Interface Compliance:** 75% (2 missing interfaces)
- **Critical Issues:** 2 | High: 4 | Medium: 6 | Low: 5

## Critical Findings

### CRITICAL-1: Repository Exposes Room Entity to UI
**Severity:** Critical
**Impact:** Layer boundary violation, tight coupling to database schema

**Location:** TodoRepository.kt

**Current Implementation:**
```kotlin
// PROBLEM: Interface exposes database entity
interface ITodoRepository {
    fun getTodos(): Flow<List<TodoEntity>>  // Entity exposed!
    suspend fun saveTodo(entity: TodoEntity)  // Entity in signature!
}

class TodoRepository @Inject constructor(
    private val todoDao: TodoDao
) : ITodoRepository {

    override fun getTodos(): Flow<List<TodoEntity>> {
        return todoDao.getAllTodos()  // Direct entity exposure
    }
}

// In ViewModel - direct entity usage
class TodoViewModel : ViewModel() {
    val todos = repository.getTodos()
        .map { entities ->
            entities.map { entity ->
                // ViewModel knows about database schema!
                TodoUiModel(
                    id = entity.id,
                    title = entity.title,
                    dbCreatedAt = entity.createdAt  // DB field names leak!
                )
            }
        }
}
```

**Problems:**
1. UI layer knows about database schema
2. Schema changes require UI changes
3. Domain logic mixed with data concerns
4. Testing requires Room dependencies

**Recommended Fix:**
```kotlin
// 1. Define domain model (in domain layer)
data class Todo(
    val id: String,
    val title: String,
    val isCompleted: Boolean,
    val dueDate: LocalDateTime?,
    val createdAt: Instant
)

// 2. Repository interface uses domain model
interface ITodoRepository {
    fun observeTodos(): Flow<List<Todo>>
    suspend fun saveTodo(todo: Todo)
    suspend fun getTodoById(id: String): Todo?
}

// 3. Mapper in data layer
object TodoMapper {
    fun TodoEntity.toDomain(): Todo = Todo(
        id = this.id,
        title = this.title,
        isCompleted = this.status == "COMPLETED",
        dueDate = this.dueDate?.let { LocalDateTime.ofEpochSecond(it, 0, ZoneOffset.UTC) },
        createdAt = Instant.ofEpochMilli(this.createdAt)
    )

    fun Todo.toEntity(): TodoEntity = TodoEntity(
        id = this.id,
        title = this.title,
        status = if (this.isCompleted) "COMPLETED" else "PENDING",
        dueDate = this.dueDate?.toEpochSecond(ZoneOffset.UTC),
        createdAt = this.createdAt.toEpochMilli()
    )
}

// 4. Repository implementation with mapping
class TodoRepository @Inject constructor(
    private val todoDao: TodoDao,
    private val dispatcher: CoroutineDispatcher
) : ITodoRepository {

    override fun observeTodos(): Flow<List<Todo>> {
        return todoDao.getAllTodos()
            .map { entities -> entities.map { it.toDomain() } }
            .flowOn(dispatcher)
    }

    override suspend fun saveTodo(todo: Todo) {
        withContext(dispatcher) {
            todoDao.insert(todo.toEntity())
        }
    }
}

// 5. ViewModel uses domain model (no entity knowledge)
class TodoViewModel : ViewModel() {
    val todos = repository.observeTodos()  // Clean domain objects!
}
```

---

### CRITICAL-2: No Error Handling in Repository
**Severity:** Critical
**Impact:** Unhandled exceptions crash the app

**Location:** ShoppingRepository.kt

**Current Implementation:**
```kotlin
class ShoppingRepository @Inject constructor(
    private val api: ShoppingApi,
    private val dao: ShoppingItemDao
) : IShoppingRepository {

    override suspend fun syncItems() {
        // PROBLEM: No error handling - crashes on network error!
        val items = api.fetchItems()
        dao.insertAll(items.map { it.toEntity() })
    }

    override suspend fun addItem(item: ShoppingItem) {
        // PROBLEM: If remote fails, local is not updated
        api.addItem(item.toDto())  // Crash if network fails
        dao.insert(item.toEntity())  // Never reached
    }
}
```

**Recommended Fix:**
```kotlin
// 1. Define Result wrapper
sealed class DataResult<out T> {
    data class Success<T>(val data: T) : DataResult<T>()
    data class Error(val exception: Throwable) : DataResult<Nothing>()
}

// 2. Repository with proper error handling
class ShoppingRepository @Inject constructor(
    private val api: ShoppingApi,
    private val dao: ShoppingItemDao,
    private val errorHandler: ErrorHandler
) : IShoppingRepository {

    override suspend fun syncItems(): DataResult<Unit> {
        return try {
            val items = api.fetchItems()
            dao.insertAll(items.map { it.toEntity() })
            DataResult.Success(Unit)
        } catch (e: IOException) {
            // Network error - use cached data
            DataResult.Error(NetworkException("Failed to sync", e))
        } catch (e: HttpException) {
            DataResult.Error(ApiException(e.code(), e.message()))
        } catch (e: Exception) {
            DataResult.Error(UnknownException(e))
        }
    }

    override suspend fun addItem(item: ShoppingItem): DataResult<ShoppingItem> {
        return try {
            // Local-first: save locally, then sync
            dao.insert(item.toEntity())

            try {
                api.addItem(item.toDto())
            } catch (e: IOException) {
                // Queue for later sync, don't fail the operation
                syncQueue.enqueue(SyncOperation.Add(item))
            }

            DataResult.Success(item)
        } catch (e: Exception) {
            DataResult.Error(e)
        }
    }
}

// 3. ViewModel handles Result
class ShoppingViewModel : ViewModel() {
    fun addItem(item: ShoppingItem) {
        viewModelScope.launch {
            when (val result = repository.addItem(item)) {
                is DataResult.Success -> _uiState.update { it.copy(itemAdded = true) }
                is DataResult.Error -> _uiState.update {
                    it.copy(error = result.exception.toUserMessage())
                }
            }
        }
    }
}
```

---

### HIGH-1: Missing distinctUntilChanged on Flows
**Severity:** High
**Impact:** Unnecessary UI updates, wasted recomposition

**Location:** Multiple repositories

**Current Implementation:**
```kotlin
class NoteRepository @Inject constructor(
    private val noteDao: NoteDao
) : INoteRepository {

    override fun observeNotes(): Flow<List<Note>> {
        // PROBLEM: Emits on any table change, even if notes unchanged
        return noteDao.getAllNotes()
            .map { it.map { entity -> entity.toDomain() } }
    }
}

// Room emits on ANY write to notes table, even if data is same
```

**Recommended Fix:**
```kotlin
class NoteRepository @Inject constructor(
    private val noteDao: NoteDao
) : INoteRepository {

    override fun observeNotes(): Flow<List<Note>> {
        return noteDao.getAllNotes()
            .map { it.map { entity -> entity.toDomain() } }
            .distinctUntilChanged()  // Only emit when data actually changes
    }

    // For more complex cases, custom equality
    override fun observeNoteById(id: String): Flow<Note?> {
        return noteDao.getNoteById(id)
            .map { it?.toDomain() }
            .distinctUntilChanged { old, new ->
                old?.id == new?.id &&
                old?.content == new?.content &&
                old?.updatedAt == new?.updatedAt
            }
    }
}
```

---

### HIGH-2: Repository Does Too Much (SRP Violation)
**Severity:** High
**Impact:** Hard to test, maintain, and understand

**Location:** CalendarRepository.kt

**Current Implementation:**
```kotlin
class CalendarRepository @Inject constructor(
    private val eventDao: CalendarEventDao,
    private val api: CalendarApi,
    private val googleCalendarSync: GoogleCalendarSyncManager,
    private val notificationScheduler: NotificationScheduler,
    private val syncQueue: SyncQueueManager,
    private val analytics: AnalyticsManager
) : ICalendarRepository {

    override suspend fun addEvent(event: CalendarEvent) {
        // Repository does too much!
        eventDao.insert(event.toEntity())
        analytics.track("event_created")  // Analytics in repository?
        notificationScheduler.scheduleReminder(event)  // Side effects?
        syncQueue.enqueue(SyncOperation.Add(event))  // Sync management?

        if (event.syncToGoogle) {
            googleCalendarSync.pushEvent(event)  // External service sync?
        }
    }
}
```

**Recommended Fix:**
```kotlin
// 1. Repository focuses on data access only
class CalendarRepository @Inject constructor(
    private val eventDao: CalendarEventDao
) : ICalendarRepository {

    override suspend fun saveEvent(event: CalendarEvent) {
        eventDao.insert(event.toEntity())
    }

    override fun observeEvents(range: DateRange): Flow<List<CalendarEvent>> {
        return eventDao.getEventsInRange(range.start, range.end)
            .map { it.map { entity -> entity.toDomain() } }
            .distinctUntilChanged()
    }
}

// 2. Use case/interactor handles orchestration
class AddCalendarEventUseCase @Inject constructor(
    private val repository: ICalendarRepository,
    private val syncManager: ISyncManager,
    private val reminderService: IReminderService
) {
    suspend operator fun invoke(event: CalendarEvent): Result<CalendarEvent> {
        // Save to repository
        repository.saveEvent(event)

        // Schedule reminder (separate concern)
        event.reminder?.let { reminderService.schedule(event.id, it) }

        // Queue for sync (separate concern)
        syncManager.queueForSync(event)

        return Result.success(event)
    }
}

// 3. Analytics handled at ViewModel/UI layer
class CalendarViewModel : ViewModel() {
    fun addEvent(event: CalendarEvent) {
        viewModelScope.launch {
            val result = addCalendarEventUseCase(event)
            if (result.isSuccess) {
                analytics.track("event_created")  // Analytics at presentation layer
            }
        }
    }
}
```

---

### MEDIUM-1: Inconsistent Suspend vs Flow Usage
**Severity:** Medium
**Impact:** Inconsistent API, confusion about data freshness

**Location:** Multiple repositories

**Current Pattern:**
```kotlin
interface IMessageRepository {
    suspend fun getMessages(): List<Message>  // One-shot, gets stale
    fun observeConversations(): Flow<List<Conversation>>  // Reactive
    suspend fun getLatestMessage(): Message?  // One-shot again
}
```

**Recommended Pattern:**
```kotlin
interface IMessageRepository {
    // Observable data - use Flow for anything the UI displays
    fun observeMessages(conversationId: String): Flow<List<Message>>
    fun observeConversations(): Flow<List<Conversation>>
    fun observeLatestMessage(conversationId: String): Flow<Message?>

    // Commands - use suspend for write operations
    suspend fun sendMessage(message: Message)
    suspend fun deleteMessage(messageId: String)
    suspend fun markAsRead(conversationId: String)
}

// If one-shot read is truly needed, make it explicit
interface IMessageRepository {
    // Snapshot (explicitly not reactive)
    suspend fun getMessageSnapshot(conversationId: String): List<Message>
}
```

---

## Repository Inventory

| Repository | Interface | Local | Remote | Cache | Issues |
|------------|-----------|-------|--------|-------|--------|
| TodoRepository | Yes (leaky) | Room | Firebase | Write-through | 2 |
| ShoppingRepository | Yes | Room | REST API | Stale-while-revalidate | 2 |
| NoteRepository | Yes | Room | Firebase | Local-first | 1 |
| MessageRepository | Yes | Room | Firebase | Real-time | 0 |
| CalendarRepository | Yes | Room | REST + Google | Complex | 2 |
| SettingsRepository | No ❌ | DataStore | None | N/A | 1 |
| ProfileRepository | Yes | Room | Firebase | Cache-first | 0 |
| WeatherRepository | Yes | Room | REST | TTL-based | 0 |

## Data Flow Patterns

### TodoRepository
```
UI → ViewModel → Repository → DAO ↔ Room DB
                           ↘ Firebase Sync (background)
```
Issues: Entity exposure, no error handling

### CalendarRepository
```
UI → ViewModel → Repository → DAO ↔ Room DB
                           ↘ API
                           ↘ GoogleCalendarSync
                           ↘ NotificationScheduler
                           ↘ SyncQueue
```
Issues: Too many responsibilities, not single-purpose

## Remediation Priority

### Critical (Immediate)
1. Add domain models, stop exposing entities
2. Add error handling to all repositories

### High Priority (This Sprint)
1. Add distinctUntilChanged to all Flows
2. Extract non-data concerns from CalendarRepository
3. Create consistent suspend vs Flow patterns

### Medium Priority (Next Sprint)
1. Add interface for SettingsRepository
2. Improve mapper organization
3. Add repository unit tests

### Low Priority (Backlog)
1. Document caching strategies
2. Add metrics for cache hit rates
3. Consider repository caching layer
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Focused repository review
- **ST-02** (Structured Sequential Instructions) - Systematic analysis areas
- **RT-02** (Multi-Dimensional Analysis) - Interface, data source, caching aspects
- **RT-05** (Evidence-Based Reasoning) - Code examples and diagrams
- **ST-03** (Output Format Templates) - Repository inventory tables
- **DS-06** (Prioritization Guidance) - Architecture impact priority
- **OC-03** (Tabular Output) - Data flow analysis

---

## Related Prompts

- `android_room_database_query_review.md` - For DAO integration
- `android_sync_architecture_review.md` - For sync repository patterns
- `android_hilt_di_scope_review.md` - For repository DI
- `android_coroutine_scope_review.md` - For async patterns
- `architecture_design_pattern_identification.md` - For pattern compliance

---

## Customization Guide

- **For Clean Architecture:** Focus on use case layer, domain model purity
- **For MVVM:** Ensure repository is only data access, no business logic
- **For Offline-First:** Expand caching and sync sections
- **For Testing Focus:** Expand fake implementation patterns
- **For Multi-Module:** Add repository module boundary review
