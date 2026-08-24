---
title: "Android Database Observation Review"
category: mobile/android/targeted-reviews
description: "Android Database Observation Review."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - database
  - mobile
  - observation
  - review
  - reviews
updated: "2026-03-19"
related_prompts: []
---

# Android Database Observation Review

---
title: "Android Database Observation Review"
category: mobile/android/performance
description: "Detect coarse or slow database observation patterns that add visible lag between user actions and UI updates"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - QA-01
difficulty: advanced
tags:
  - android
  - room
  - database
  - sqlite
  - observation
  - flow
  - livedata
  - performance
  - queries
updated: "2026-03-09"
---

**Objective:** Analyze the Android codebase to identify database observation patterns — Room or other local store queries and their reactive observation — that add visible lag between user actions and UI state updates, without freezing. This includes overly broad table observation, expensive query re-execution, missing indexes, heavy post-query transformation, and write-then-read patterns.

**When to Use:** Use when UI updates depend on local database state and there's a noticeable delay between user actions and visible changes. Common in apps with offline-first architecture, complex data models, or dashboard/list screens backed by Room. The app never freezes, but actions feel sluggish because the database observation pipeline is too slow.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Confirm the query is on the critical UI path** — Background sync queries that don't affect immediate UI are fine to be slow.
2. **Check actual table size** — A full table scan on 50 rows is fine. On 50,000 rows, it's a problem.
3. **Verify the query runs on every relevant mutation** — Room re-runs observed queries on any write to the observed table(s), not just relevant writes.
4. **Provide exact file:line locations and SQL queries.**

**Finding NO issues is an acceptable outcome.**

### False-Positive Prevention

- ❌ Do NOT flag queries on small tables (<1,000 rows) unless they join multiple tables
- ❌ Do NOT flag background sync/prefetch queries that don't affect immediate UI
- ❌ Do NOT flag Room's automatic invalidation as a bug — it's by design; flag only when the re-execution is expensive
- ❌ Do NOT flag missing indexes without verifying the query is frequently executed and the table is large
- ❌ Do NOT flag write-then-read if the write-to-emission latency is <50ms
- ✅ DO check `EXPLAIN QUERY PLAN` output (or infer from query structure) for full table scans
- ✅ DO estimate table size × query frequency to gauge actual impact
- ✅ DO verify whether the query result is transformed after retrieval (additional cost)
- ✅ DO check if Room's invalidation tracker fires this query unnecessarily often

---

### 1. Overly Broad Table Observation

Identify queries that observe more data than the UI needs:

* **Full-table observation for partial display:**
  - `SELECT * FROM items` when the UI only shows items for a specific category
  - Observing an entire table when only a count or single field is needed

* **Room invalidation over-triggering:**
  - Any write to the observed table causes the query to re-run, even if the write doesn't affect the query result
  - Multi-table JOINs where a write to ANY joined table re-triggers the query

* **Missing WHERE clauses:**
  - Observing all rows when a subset would suffice
  - Not parameterizing queries to narrow the observation scope

**Best Practices:**
```kotlin
// ❌ BAD: Observes entire table, re-runs on ANY write to 'items'
@Query("SELECT * FROM items ORDER BY created_at DESC")
fun observeAllItems(): Flow<List<ItemEntity>>

// UI only shows one category, but query fetches everything
val categoryItems = dao.observeAllItems()
    .map { items -> items.filter { it.categoryId == selectedCategory } } // filters in memory!

// ✅ GOOD: Narrow observation to what UI needs
@Query("SELECT * FROM items WHERE category_id = :categoryId ORDER BY created_at DESC")
fun observeItemsByCategory(categoryId: String): Flow<List<ItemEntity>>

// Only re-runs when items in this category are modified
val categoryItems = dao.observeItemsByCategory(selectedCategory)

// ❌ BAD: Full table observation for a count
@Query("SELECT * FROM notifications")
fun observeAll(): Flow<List<NotificationEntity>>

val unreadCount = dao.observeAll().map { it.count { n -> !n.isRead } }

// ✅ GOOD: Targeted count query
@Query("SELECT COUNT(*) FROM notifications WHERE is_read = 0")
fun observeUnreadCount(): Flow<Int>
```

**Suggested Fixes:**
- Add WHERE clauses that match what the UI actually displays
- Use targeted aggregate queries (`COUNT`, `SUM`, `MAX`) instead of fetching all rows
- Split broad queries into narrower, parameterized ones
- Consider `@RewriteQueriesToDropUnusedColumns` to avoid fetching unused columns

---

### 2. Expensive Query Re-Execution

Identify queries that are expensive to re-run:

* **Complex JOINs re-executing on every write:**
  - Multi-table JOINs with large tables
  - Subqueries that scan large datasets
  - Room re-runs the entire query on any write to any involved table

* **Full-text search on every mutation:**
  - FTS queries re-executing when the search term hasn't changed
  - Missing FTS indexes on searched columns

* **Sorting without indexes:**
  - `ORDER BY` on non-indexed columns requiring full sort on every query

**Best Practices:**
```kotlin
// ❌ BAD: Complex JOIN re-runs on ANY write to items, users, or categories
@Query("""
    SELECT i.*, u.name as userName, c.name as categoryName
    FROM items i
    JOIN users u ON i.user_id = u.id
    JOIN categories c ON i.category_id = c.id
    ORDER BY i.created_at DESC
    LIMIT 100
""")
fun observeItemsWithDetails(): Flow<List<ItemWithDetails>>

// ✅ GOOD: Use @Relation for lazy loading, or cache with intermediary
@Query("SELECT * FROM items ORDER BY created_at DESC LIMIT 100")
fun observeRecentItems(): Flow<List<ItemEntity>>

// Resolve relations in a separate step, cached per item
@Transaction
@Query("SELECT * FROM items WHERE id IN (:ids)")
fun getItemsWithRelations(ids: List<String>): List<ItemWithRelations>
```

**Suggested Fixes:**
- Avoid multi-table JOINs in observed queries when possible — they re-trigger on writes to ANY involved table
- Use `@Relation` with `@Transaction` for data that doesn't change on every mutation
- Cache resolved relations in a ViewModel-level map; only re-resolve changed items
- Consider denormalized views or materialized aggregates for frequently-read dashboards

---

### 3. Missing Indexes

Identify queries that scan without index support:

* **WHERE clause on non-indexed columns:**
  - `WHERE status = 'active'` without an index on `status`
  - `WHERE user_id = :userId AND created_at > :since` without a composite index

* **ORDER BY without index:**
  - Sorting large result sets on unindexed columns
  - Combined filter + sort requiring index coverage

* **JOIN conditions without indexes:**
  - Foreign keys used in JOINs without indexes (Room doesn't auto-index foreign keys unless you specify)

**Best Practices:**
```kotlin
// ❌ BAD: No index on frequently queried columns
@Entity(tableName = "messages")
data class MessageEntity(
    @PrimaryKey val id: String,
    val conversationId: String, // queried frequently, no index!
    val senderId: String,
    val content: String,
    val createdAt: Long,        // sorted by, no index!
    val isRead: Boolean         // filtered by, no index!
)

// ✅ GOOD: Indexes on query patterns
@Entity(
    tableName = "messages",
    indices = [
        Index("conversation_id", "created_at"),  // covers conversation list queries
        Index("sender_id"),                        // covers sender lookups
        Index("is_read")                           // covers unread count queries
    ]
)
data class MessageEntity(
    @PrimaryKey val id: String,
    @ColumnInfo(name = "conversation_id") val conversationId: String,
    @ColumnInfo(name = "sender_id") val senderId: String,
    val content: String,
    @ColumnInfo(name = "created_at") val createdAt: Long,
    @ColumnInfo(name = "is_read") val isRead: Boolean
)
```

**Suggested Fixes:**
- Add indexes for all columns used in WHERE, ORDER BY, and JOIN conditions
- Use composite indexes matching the most common query patterns (filter + sort)
- Add `@Index` annotations on `@Entity` classes or use `CREATE INDEX` in migrations
- Profile with `EXPLAIN QUERY PLAN` (via `SupportSQLiteDatabase.query`) to verify index usage
- Remember: indexes cost write performance — only index columns that are queried more than they're written

---

### 4. Heavy Post-Query Transformations

Identify expensive work done to query results before they reach the UI:

* **Full list mapping after every query emission:**
  - `dao.observeAll().map { list -> list.map { it.toDomainModel() } }` — maps entire list on every emission
  - Domain model construction involving formatting, calculation, or lookup

* **Redundant re-transformation:**
  - Same transformation applied in repository AND ViewModel
  - No caching of mapped results between emissions

**Best Practices:**
```kotlin
// ❌ BAD: Full list transformation on every emission
val items: StateFlow<List<ItemUiModel>> = dao.observeAllItems()
    .map { entities ->
        entities.map { entity ->
            ItemUiModel(
                id = entity.id,
                title = entity.title,
                formattedDate = formatDate(entity.createdAt), // expensive per item
                distanceLabel = calculateDistance(entity.lat, entity.lng), // expensive
                thumbnail = resolveThumbnail(entity.imageId) // may involve I/O
            )
        }
    }
    .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), emptyList())

// ✅ GOOD: Incremental mapping with cache
private val uiModelCache = mutableMapOf<String, ItemUiModel>()

val items: StateFlow<List<ItemUiModel>> = dao.observeAllItems()
    .map { entities ->
        entities.map { entity ->
            uiModelCache.getOrPut(entity.id) { entity.toUiModel() }
                .let { cached ->
                    if (cached.sourceVersion == entity.updatedAt) cached
                    else entity.toUiModel().also { uiModelCache[entity.id] = it }
                }
        }
    }
    .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), emptyList())
```

**Suggested Fixes:**
- Cache mapped UI models by ID; only re-map items that actually changed
- Pre-compute formatted strings in the entity or during write (denormalization)
- Use Room's `@ColumnInfo` defaults and computed columns where possible
- Move expensive per-item transforms to write-time rather than read-time
- Use `distinctUntilChanged()` before expensive transformations to skip no-op emissions

---

### 5. Write-Then-Read Latency

Identify patterns where the UI waits for a full DB round-trip:

* **Insert → observe → UI cycle:**
  - Writing to Room, then waiting for the Room observation Flow to re-emit
  - The invalidation → query → emission cycle adds 10-50ms+ latency

* **No optimistic local state:**
  - UI doesn't update until Room's invalidation tracker fires, query re-runs, and Flow emits
  - User perceives delay between action and visual feedback

**Best Practices:**
```kotlin
// ❌ BAD: UI waits for full Room round-trip
fun completeTask(taskId: String) {
    viewModelScope.launch {
        dao.updateTaskStatus(taskId, "completed")
        // UI updates only when dao.observeTasks() re-emits after invalidation
        // This adds 10-50ms+ perceived delay
    }
}

// ✅ GOOD: Optimistic update + Room observation for consistency
fun completeTask(taskId: String) {
    // 1. Instant UI update
    _uiState.update { state ->
        state.copy(
            tasks = state.tasks.map { task ->
                if (task.id == taskId) task.copy(status = "completed") else task
            }
        )
    }

    // 2. Persist (Room observation will eventually align)
    viewModelScope.launch {
        dao.updateTaskStatus(taskId, "completed")
    }
}
```

**Suggested Fixes:**
- Implement optimistic UI updates for user-initiated mutations
- Let Room observation serve as the "source of truth sync" — not the immediate feedback mechanism
- For complex state, maintain a ViewModel-level overlay that merges optimistic changes with DB observations
- Consider whether the Room observation Flow is even needed if the ViewModel is the primary state owner

---

## Expected Output

Provide a database observation analysis report including:

### 1. Executive Summary
- Database observation efficiency rating
- Number of observed queries analyzed
- Critical query cost issues

### 2. Query Cost Matrix

| Query | DAO Method | Table(s) | Est. Rows | Indexed? | Re-trigger Rate | Post-Transform Cost | Priority |
|-------|-----------|----------|-----------|----------|-----------------|---------------------|----------|
| [SQL] | [method] | [tables] | [N] | [Y/N] | [per mutation type] | [ms estimate] | [Level] |

### 3. Detailed Findings

For each issue:
- **Location:** file:line and SQL query
- **Category:** Broad Observation / Expensive Re-Execution / Missing Index / Post-Query Transform / Write-Then-Read
- **Impact:** Estimated latency per occurrence
- **Confidence:** High / Medium / Low
- **Current Code:** Query and observation pattern
- **Recommended Fix:** Optimized query/observation
- **Verification:** `EXPLAIN QUERY PLAN` or timing measurements

### 4. Prioritized Remediation Plan

Ordered by query latency × frequency impact.

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on database observation latency
- **ST-02** (Structured Sequential Instructions) — Query-by-query analysis
- **RT-02** (Multi-Dimensional Analysis) — Scope, indexes, transforms, write-read cycle
- **RT-05** (Evidence-Based Reasoning) — Row count × query cost estimates
- **DS-06** (Prioritization Guidance) — Ranked by latency × frequency
- **QA-01** (Chain-of-Verification) — Verify table size and query path before flagging

---

## Related Prompts

- `android_room_database_query_review.md` — For Room query optimization
- `android_async_boundaries_review.md` — For async pipeline latency
- `android_state_propagation_review.md` — For state delivery issues
- `performance_bottleneck_identification.md` — For general performance analysis
