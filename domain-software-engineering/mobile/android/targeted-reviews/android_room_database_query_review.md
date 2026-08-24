---
title: "Android Room Database Query Review"
category: mobile/android/targeted-reviews
description: "Android Room Database Query Review."
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
  - query
  - reviews
  - room
updated: "2026-03-19"
related_prompts: []
---

# Android Room Database Query Review

**Objective:** Conduct a targeted review of Room database implementation, analyzing DAO query efficiency, schema design, index usage, migration safety, and reactive data patterns for optimal performance and data integrity.

**When to Use:** Use this prompt when reviewing database layer performance, before adding new queries or entities, after identifying slow screens tied to database operations, during migration planning, or when optimizing app startup time affected by database access.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the actual query execution** - Don't flag based on pattern matching alone. Verify that the suspected query actually causes performance problems.
2. **Check for existing optimizations** - Search for indexes, query optimizations, or caching that may already address the concern.
3. **Understand the context** - Consider WHY queries are structured this way. Data access patterns and business requirements dictate query design.
4. **Confirm actual performance impact** - Use EXPLAIN QUERY PLAN or Room's query logging to verify slow queries.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `UserDao.kt:34`).

**Finding NO issues is an acceptable outcome.** If queries are well-optimized for the use case, say so with confidence. Don't manufacture performance concerns.

### False-Positive Prevention

- ❌ Do NOT flag all JOIN operations as problematic without measuring actual performance
- ❌ Do NOT flag missing indexes without confirming the query is actually slow
- ❌ Do NOT assume N+1 patterns without tracing actual query execution
- ❌ Do NOT report micro-optimizations for queries that run rarely or on small datasets
- ✅ DO use EXPLAIN QUERY PLAN to verify query efficiency
- ✅ DO consider the actual dataset size when evaluating performance
- ✅ DO check for @Transaction usage where appropriate
- ✅ DO understand Room's automatic query optimization capabilities

---

### 1. Query Efficiency Analysis

Evaluate DAO query performance:

* **Query Complexity:**
  - Review complex JOIN operations for efficiency
  - Check for N+1 query patterns (fetching related entities in loops)
  - Assess subquery usage and alternatives
  - Evaluate query result set sizes

* **Index Utilization:**
  - Verify indexes exist for WHERE clause columns
  - Check for composite index usage in multi-column queries
  - Assess covering index opportunities
  - Review index impact on write performance

* **Projection Optimization:**
  - Check for SELECT * usage (should select only needed columns)
  - Review entity projections for list queries
  - Assess use of @ColumnInfo for specific fields
  - Evaluate return type appropriateness (Entity vs. POJO)

* **Pagination:**
  - Review Paging 3 integration for large datasets
  - Check for LIMIT/OFFSET usage in manual pagination
  - Assess keyset pagination for better performance
  - Verify page size appropriateness

### 2. Schema Design Review

Analyze entity and relationship modeling:

* **Entity Structure:**
  - Review primary key design (auto-generate vs. natural keys)
  - Check for appropriate column types and nullability
  - Assess embedded objects vs. separate entities
  - Verify @ColumnInfo naming conventions

* **Relationships:**
  - Review @Relation annotations for correctness
  - Check for appropriate cascade behaviors
  - Assess @ForeignKey constraint definitions
  - Verify referential integrity enforcement

* **Normalization:**
  - Check for appropriate normalization level
  - Assess denormalization for read performance
  - Review redundant data storage
  - Verify data consistency mechanisms

### 3. Reactive Query Patterns

Evaluate Flow and LiveData usage:

* **Flow Queries:**
  - Review Flow return types in DAOs
  - Check for proper distinctUntilChanged usage
  - Assess Flow operators applied before collection
  - Verify Flow cancellation on query changes

* **Query Invalidation:**
  - Understand Room's automatic invalidation
  - Check for over-invalidation (unnecessary re-queries)
  - Assess multi-table query invalidation scope
  - Review @RawQuery invalidation handling

* **Performance Impact:**
  - Check for expensive Flows collected on main thread
  - Review Flow transformation efficiency
  - Assess conflation for rapid updates
  - Verify lifecycle-aware collection

### 4. Transaction Management

Review transaction usage:

* **Transaction Boundaries:**
  - Review @Transaction annotation usage
  - Check for multi-operation atomicity requirements
  - Assess transaction scope (too large/too small)
  - Verify rollback behavior on failure

* **Batch Operations:**
  - Check for batch insert/update patterns
  - Review @Insert(onConflict) strategies
  - Assess bulk delete efficiency
  - Verify large batch chunking

* **Deadlock Prevention:**
  - Review transaction nesting patterns
  - Check for consistent lock ordering
  - Assess long-running transaction risks
  - Verify no blocking operations in transactions

### 5. Migration Safety

Analyze migration implementation:

* **Migration Coverage:**
  - Verify migration exists for each schema version jump
  - Check for destructive migration fallback (should be disabled)
  - Review auto-migration suitability
  - Assess migration testing approach

* **Migration Safety:**
  - Review ALTER TABLE statements for data preservation
  - Check default value assignments for new columns
  - Assess foreign key migration handling
  - Verify index recreation after schema changes

* **Migration Testing:**
  - Check for migration test coverage
  - Review schema export configuration
  - Assess production database testing approach
  - Verify rollback capabilities

### 6. Performance Optimization

Evaluate database performance:

* **Query Performance:**
  - Review EXPLAIN QUERY PLAN for complex queries
  - Check for full table scans on large tables
  - Assess query cache utilization
  - Verify appropriate use of @RawQuery for optimization

* **Write Performance:**
  - Review write-ahead logging (WAL) configuration
  - Check for batch write optimizations
  - Assess index impact on insert performance
  - Verify no unnecessary write operations

* **Memory Efficiency:**
  - Check for large entity loading (prefer projections)
  - Review cursor window size for large queries
  - Assess in-memory caching strategies
  - Verify proper cleanup of database references

### 7. Full-Text Search

If using FTS, review implementation:

* **FTS Configuration:**
  - Review FTS table setup (@Fts4 annotation)
  - Check tokenizer configuration
  - Assess content sync with source table
  - Verify FTS index maintenance

* **Search Queries:**
  - Review MATCH query syntax
  - Check for proper escaping of search terms
  - Assess search result ranking
  - Verify search performance on large datasets

### 8. Database Security

Analyze security considerations:

* **Encryption:**
  - Review SQLCipher integration if used
  - Check for encryption key management
  - Assess performance impact of encryption
  - Verify encryption covers all sensitive data

* **Query Injection:**
  - Check for SQL injection vulnerabilities in @RawQuery
  - Review dynamic query construction
  - Assess parameterized query usage
  - Verify input sanitization

---

## Expected Output

Provide a comprehensive Room database review report including:

### 1. Executive Summary
- Overall database health rating
- Query performance assessment
- Schema design quality
- Migration safety status
- Critical findings count

### 2. Query Inventory

| DAO | Query | Type | Indexed | Performance | Issues |
|-----|-------|------|---------|-------------|--------|
| [DAO] | [Method] | [SELECT/INSERT/...] | [Yes/No] | [Fast/Slow] | [Count] |

### 3. Index Analysis

| Table | Column(s) | Index Present | Query Usage | Recommendation |
|-------|-----------|---------------|-------------|----------------|
| [Table] | [Columns] | [Yes/No] | [Queries using it] | [Action] |

### 4. Detailed Findings

For each issue:
- **Location:** DAO and query method
- **Issue:** Description
- **Impact:** Performance/correctness effect
- **Severity:** Critical/High/Medium/Low
- **Current Query:** SQL showing problem
- **Optimized Query:** Improved version
- **Expected Improvement:** Performance gain estimate

### 5. Migration Assessment

| From | To | Migration | Tested | Data Safe | Issues |
|------|-----|-----------|--------|-----------|--------|
| [Version] | [Version] | [Present/Missing] | [Yes/No] | [Yes/Risk] | [Description] |

### 6. Prioritized Recommendations

Ordered by impact and effort.

---

## Example Output

```markdown
# Room Database Query Review Report

## Executive Summary
- **Overall Health:** Needs Optimization - 3 slow queries identified
- **Query Performance:** 85% optimal, 3 queries need attention
- **Schema Design:** Good with minor improvements possible
- **Migration Safety:** 2 gaps identified
- **Critical Issues:** 1 | High: 3 | Medium: 7 | Low: 4

## Critical Findings

### CRITICAL-1: N+1 Query Pattern in TodoDao
**Severity:** Critical
**Impact:** O(n) database calls for list screen, causes visible lag

**Location:** TodoDao.kt - getTodosWithAssignees()

**Current Pattern:**
```kotlin
// In TodoDao - fetches todos
@Query("SELECT * FROM todos WHERE familyId = :familyId")
fun getTodosForFamily(familyId: String): Flow<List<TodoEntity>>

// In Repository - N+1 pattern!
fun getTodosWithAssignees(familyId: String): Flow<List<TodoWithAssignee>> {
    return todoDao.getTodosForFamily(familyId).map { todos ->
        todos.map { todo ->
            // PROBLEM: One query per todo!
            val assignee = memberDao.getMemberById(todo.assigneeId)
            TodoWithAssignee(todo, assignee)
        }
    }
}
```

**Performance Impact:**
- 50 todos = 51 database queries
- Each query: ~5ms
- Total: ~250ms delay (noticeable lag)

**Optimized Solution:**
```kotlin
// SOLUTION 1: Use @Relation (preferred)
data class TodoWithAssignee(
    @Embedded val todo: TodoEntity,
    @Relation(
        parentColumn = "assigneeId",
        entityColumn = "id"
    )
    val assignee: FamilyMemberProfileEntity?
)

@Transaction
@Query("SELECT * FROM todos WHERE familyId = :familyId")
fun getTodosWithAssignees(familyId: String): Flow<List<TodoWithAssignee>>

// SOLUTION 2: JOIN query (for specific fields)
@Query("""
    SELECT t.*, m.displayName as assigneeName, m.avatarUrl as assigneeAvatar
    FROM todos t
    LEFT JOIN family_member_profiles m ON t.assigneeId = m.id
    WHERE t.familyId = :familyId
""")
fun getTodosWithAssigneeInfo(familyId: String): Flow<List<TodoWithAssigneeInfo>>
```

**Expected Improvement:** 51 queries → 1-2 queries (~95% reduction)

---

### HIGH-1: Missing Index on Frequently Filtered Column
**Severity:** High
**Impact:** Full table scan on every filter operation

**Location:** TodoEntity - status column

**Current Schema:**
```kotlin
@Entity(tableName = "todos")
data class TodoEntity(
    @PrimaryKey val id: String,
    val familyId: String,
    val status: String,  // No index!
    val dueDate: Long?,
    // ...
)
```

**Slow Query:**
```kotlin
@Query("SELECT * FROM todos WHERE status = :status AND familyId = :familyId")
fun getTodosByStatus(status: String, familyId: String): Flow<List<TodoEntity>>

// EXPLAIN QUERY PLAN shows: SCAN TABLE todos
// Should show: SEARCH TABLE todos USING INDEX
```

**Solution:**
```kotlin
@Entity(
    tableName = "todos",
    indices = [
        Index(value = ["familyId", "status"]),  // Composite index
        Index(value = ["dueDate"]),
        Index(value = ["assigneeId"])
    ]
)
data class TodoEntity(
    // ... fields
)
```

**Migration Required:**
```kotlin
val MIGRATION_65_66 = object : Migration(65, 66) {
    override fun migrate(database: SupportSQLiteDatabase) {
        database.execSQL(
            "CREATE INDEX IF NOT EXISTS index_todos_familyId_status ON todos(familyId, status)"
        )
    }
}
```

---

### HIGH-2: SELECT * in List Query
**Severity:** High
**Impact:** Loading unnecessary data, increased memory usage

**Location:** NoteDao.kt

**Current Query:**
```kotlin
// Loads entire note content for list display
@Query("SELECT * FROM notes WHERE familyId = :familyId ORDER BY updatedAt DESC")
fun getNotesForFamily(familyId: String): Flow<List<NoteEntity>>

// NoteEntity has:
// - id, title, content (potentially 100KB+), createdAt, updatedAt, isPinned, ...
```

**Problem:**
- Note content can be very large
- List only shows title, date, preview
- Loading 50 notes = 50 × 100KB = 5MB unnecessary data

**Optimized Solution:**
```kotlin
// Create a projection for list display
data class NoteListItem(
    val id: String,
    val title: String,
    val contentPreview: String,  // First 200 chars
    val updatedAt: Long,
    val isPinned: Boolean
)

@Query("""
    SELECT id, title, SUBSTR(content, 1, 200) as contentPreview, updatedAt, isPinned
    FROM notes
    WHERE familyId = :familyId
    ORDER BY isPinned DESC, updatedAt DESC
""")
fun getNoteListItems(familyId: String): Flow<List<NoteListItem>>

// Full entity only when opening note
@Query("SELECT * FROM notes WHERE id = :id")
suspend fun getNoteById(id: String): NoteEntity?
```

**Expected Improvement:** ~90% reduction in memory for list screens

---

### MEDIUM-1: Flow Without distinctUntilChanged
**Severity:** Medium
**Impact:** Unnecessary recompositions when data hasn't changed

**Location:** Multiple DAOs

**Current Pattern:**
```kotlin
@Query("SELECT * FROM todos WHERE id = :id")
fun getTodoById(id: String): Flow<TodoEntity?>

// In ViewModel - no distinctUntilChanged
val todo = todoDao.getTodoById(todoId)
    .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), null)
```

**Recommended Pattern:**
```kotlin
// In Repository or ViewModel
val todo = todoDao.getTodoById(todoId)
    .distinctUntilChanged()  // Prevent duplicate emissions
    .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), null)
```

---

## Query Inventory

| DAO | Method | Type | Indexed | Perf | Issues |
|-----|--------|------|---------|------|--------|
| TodoDao | getTodosForFamily | SELECT | Yes | Fast | 0 |
| TodoDao | getTodosByStatus | SELECT | No | Slow | 1 |
| TodoDao | getTodosWithAssignees | SELECT+N | N/A | Slow | 1 |
| NoteDao | getNotesForFamily | SELECT | Yes | Slow | 1 |
| NoteDao | searchNotes | FTS | Yes | Fast | 0 |
| ShoppingItemDao | getItemsByCategory | SELECT | Yes | Fast | 0 |
| MessageDao | getMessagesForConversation | SELECT | Yes | Fast | 0 |
| CalendarEventDao | getEventsInRange | SELECT | Partial | Medium | 1 |

## Index Recommendations

| Table | Columns | Action | Priority |
|-------|---------|--------|----------|
| todos | (familyId, status) | Add composite index | High |
| todos | (dueDate) | Add single index | Medium |
| todos | (assigneeId) | Add single index | Medium |
| calendar_events | (startDate, endDate) | Add composite index | High |
| shopping_items | (familyId, isPurchased) | Add composite index | Medium |

## Migration Assessment

| From → To | Status | Data Safe | Issue |
|-----------|--------|-----------|-------|
| 64 → 65 | Present | Yes | None |
| 63 → 64 | Present | Risk | No default for new NOT NULL column |
| 62 → 63 | Present | Yes | None |
| 61 → 62 | Missing | N/A | Auto-migration used, verify |

## Remediation Priority

### Critical (Fix Immediately)
1. Fix N+1 pattern in TodoDao

### High Priority (This Sprint)
1. Add missing indexes
2. Create list projections for Note and Message

### Medium Priority (Next Sprint)
1. Add distinctUntilChanged to all Flows
2. Review and optimize CalendarEventDao range query
3. Add migration tests for all versions
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Focused database review
- **ST-02** (Structured Sequential Instructions) - Systematic review areas
- **RT-02** (Multi-Dimensional Analysis) - Query, schema, and migration aspects
- **RT-05** (Evidence-Based Reasoning) - EXPLAIN QUERY PLAN evidence
- **ST-03** (Output Format Templates) - Query inventory tables
- **DS-06** (Prioritization Guidance) - Performance-based priority
- **OC-03** (Tabular Output) - Index and migration matrices

---

## Related Prompts

- `android_room_migration_safety_audit.md` - Deep dive on migrations
- `android_sync_architecture_review.md` - For sync queue storage
- `android_sqlcipher_key_management_review.md` - For encrypted databases
- `android_kotlin_best_practices.md` - General patterns
- `performance_bottleneck_identification.md` - Performance profiling

---

## Customization Guide

- **For SQLCipher databases:** Add encryption key management review, performance overhead assessment
- **For Paging 3:** Add PagingSource implementation review, RemoteMediator analysis
- **For FTS-heavy apps:** Expand FTS section with tokenizer tuning, relevance ranking
- **For multi-module apps:** Add database module boundary review, shared schema access
- **For high-write apps:** Focus on WAL mode, write batching, index write overhead
