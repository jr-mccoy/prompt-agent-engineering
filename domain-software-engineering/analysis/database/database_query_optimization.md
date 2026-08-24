---
title: "Database Query Optimization Analysis"
category: code-analysis/database
description: "Analyze SQL queries for performance issues and provide optimization recommendations"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-02
  - DS-06
  - ST-03
  - AG-05
difficulty: advanced
tags:
  - database
  - query
  - optimization
  - performance
  - sql
  - explain-plan
updated: "2026-01-15"
---

# Database Query Optimization Analysis

**Objective:** Analyze database queries to identify performance bottlenecks, inefficient patterns, and optimization opportunities, then provide specific recommendations with before/after comparisons and expected performance improvements.

---

## Instructions

### Phase 1: Query Discovery and Inventory

1. **Locate all database queries in the codebase:**
   - SQL statements (SELECT, INSERT, UPDATE, DELETE)
   - ORM-generated queries (examine query logs or ORM debug output)
   - Stored procedures and functions
   - Dynamic SQL generation
   - Query builder patterns

2. **Categorize queries by:**
   - Frequency (hot paths vs. occasional)
   - Complexity (simple vs. multi-join vs. subqueries)
   - Data volume affected
   - Response time requirements
   - Transaction context

3. **Document query context:**
   - Where is the query called from?
   - What triggers the query execution?
   - What is the expected result size?
   - Is it user-facing (latency-sensitive)?

---

### Phase 2: Query Pattern Analysis

1. **Identify N+1 Query Problems:**
   ```sql
   -- BAD: N+1 pattern (executed in a loop)
   SELECT * FROM orders WHERE user_id = ?
   -- Then for each order:
   SELECT * FROM order_items WHERE order_id = ?

   -- GOOD: Single query with JOIN
   SELECT o.*, oi.*
   FROM orders o
   JOIN order_items oi ON o.order_id = oi.order_id
   WHERE o.user_id = ?
   ```

2. **Identify SELECT * Anti-patterns:**
   ```sql
   -- BAD: Selecting all columns
   SELECT * FROM users WHERE active = true

   -- GOOD: Select only needed columns
   SELECT user_id, username, email FROM users WHERE active = true
   ```

3. **Identify Missing WHERE Clauses:**
   - Full table scans without filters
   - Unbounded result sets
   - Queries that grow with data volume

4. **Identify Subquery Inefficiencies:**
   ```sql
   -- BAD: Correlated subquery
   SELECT *
   FROM orders o
   WHERE total > (SELECT AVG(total) FROM orders WHERE user_id = o.user_id)

   -- GOOD: JOIN with derived table
   SELECT o.*
   FROM orders o
   JOIN (
     SELECT user_id, AVG(total) as avg_total
     FROM orders GROUP BY user_id
   ) avg_orders ON o.user_id = avg_orders.user_id
   WHERE o.total > avg_orders.avg_total
   ```

5. **Identify Function Usage on Indexed Columns:**
   ```sql
   -- BAD: Function prevents index usage
   SELECT * FROM orders WHERE YEAR(created_at) = 2024

   -- GOOD: Range query uses index
   SELECT * FROM orders
   WHERE created_at >= '2024-01-01' AND created_at < '2025-01-01'
   ```

6. **Identify LIKE Pattern Issues:**
   ```sql
   -- BAD: Leading wildcard (no index)
   SELECT * FROM products WHERE name LIKE '%phone%'

   -- BETTER: Trailing wildcard (can use index)
   SELECT * FROM products WHERE name LIKE 'phone%'

   -- BEST: Full-text search for text searching
   SELECT * FROM products WHERE MATCH(name) AGAINST('phone')
   ```

7. **Identify OR Clause Inefficiencies:**
   ```sql
   -- BAD: OR can prevent index usage
   SELECT * FROM users WHERE email = ? OR phone = ?

   -- GOOD: UNION allows index usage on both
   SELECT * FROM users WHERE email = ?
   UNION
   SELECT * FROM users WHERE phone = ?
   ```

---

### Phase 3: Execution Plan Analysis

For each significant query, analyze the execution plan:

1. **Request or simulate EXPLAIN output:**
   ```sql
   EXPLAIN ANALYZE SELECT ...
   -- or
   EXPLAIN (FORMAT JSON, ANALYZE, BUFFERS) SELECT ...
   ```

2. **Identify warning signs in execution plans:**
   - **Full Table Scan** (type: ALL) on large tables
   - **Filesort** operations on large result sets
   - **Using temporary** for GROUP BY or ORDER BY
   - **Nested Loop** with large outer table
   - **High rows examined** vs rows returned ratio
   - **Missing index** warnings

3. **Analyze join strategies:**
   - Nested Loop: Efficient for small result sets
   - Hash Join: Better for large unsorted joins
   - Merge Join: Efficient for sorted data

4. **Check index utilization:**
   - Is the optimal index being used?
   - Are covering indexes available?
   - Is the index selectivity sufficient?

---

### Phase 4: Index Opportunity Analysis

1. **Identify missing indexes:**
   - Columns frequently in WHERE clauses
   - JOIN columns without indexes
   - ORDER BY columns causing filesort
   - Columns with high selectivity

2. **Identify composite index opportunities:**
   ```sql
   -- Query pattern:
   SELECT * FROM orders
   WHERE user_id = ? AND status = 'pending'
   ORDER BY created_at DESC

   -- Optimal composite index:
   CREATE INDEX idx_orders_user_status_created
   ON orders(user_id, status, created_at DESC)
   ```

3. **Identify covering index opportunities:**
   ```sql
   -- Query only needs these columns:
   SELECT order_id, total, created_at FROM orders WHERE user_id = ?

   -- Covering index (no table lookup needed):
   CREATE INDEX idx_orders_covering
   ON orders(user_id) INCLUDE (order_id, total, created_at)
   ```

4. **Identify unused or redundant indexes:**
   - Indexes never used in query plans
   - Duplicate indexes (subset of another index)
   - Indexes on low-selectivity columns

---

### Phase 5: Query Rewriting Analysis

1. **JOIN optimization opportunities:**
   - Reorder JOINs to reduce intermediate result sizes
   - Convert implicit joins to explicit
   - Use appropriate join types (INNER vs LEFT)

2. **Aggregation optimization:**
   ```sql
   -- BAD: Counting after filtering
   SELECT COUNT(*) FROM (
     SELECT * FROM orders WHERE status = 'completed'
   ) subquery

   -- GOOD: Direct count with filter
   SELECT COUNT(*) FROM orders WHERE status = 'completed'
   ```

3. **Pagination optimization:**
   ```sql
   -- BAD: OFFSET for deep pagination
   SELECT * FROM products ORDER BY created_at LIMIT 20 OFFSET 10000

   -- GOOD: Keyset pagination
   SELECT * FROM products
   WHERE created_at < ?last_seen_created_at
   ORDER BY created_at DESC
   LIMIT 20
   ```

4. **EXISTS vs IN optimization:**
   ```sql
   -- Consider for large subquery results:
   -- IN materializes full subquery
   SELECT * FROM users WHERE user_id IN (SELECT user_id FROM orders)

   -- EXISTS can short-circuit
   SELECT * FROM users u
   WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.user_id)
   ```

---

### Phase 6: Database-Specific Optimizations

**PostgreSQL:**
- Partial indexes for filtered queries
- Expression indexes for computed columns
- BRIN indexes for time-series data
- Parallel query utilization

**MySQL:**
- Index hints when optimizer chooses poorly
- Query cache considerations
- InnoDB buffer pool utilization
- Covering index optimization

**SQL Server:**
- Columnstore indexes for analytics
- Filtered indexes
- Query store analysis
- Parameter sniffing issues

**SQLite:**
- WAL mode considerations
- Index-only queries
- Temp table optimization

---

### Phase 7: CRITICAL - Verification Before Recommending

**Before recommending optimizations:**

1. **Verify the query is actually slow:**
   - Is execution time a problem? (>100ms for user-facing)
   - How often is it called?
   - What's the data volume?

2. **Test optimization impact:**
   - Will the index help this specific query?
   - Does the index hurt write performance?
   - Is the selectivity high enough?

3. **Consider trade-offs:**
   - Index maintenance cost vs. query benefit
   - Storage overhead vs. speed improvement
   - Query complexity vs. maintainability

**Do NOT recommend:**
- Indexes on tables with very few rows (<1000)
- Optimizations for queries called once per day
- Complex rewrites for minimal improvement
- Denormalization without clear benchmarks

---

## Expected Output: Query Optimization Report

### Executive Summary
- Total queries analyzed: [N]
- Queries requiring optimization: [N]
- Estimated total improvement: [X%]
- Critical issues: [N]

### Query Performance Inventory

| Query ID | Location | Avg Time | Calls/Hour | Priority |
|----------|----------|----------|------------|----------|
| Q1 | orders.repository:45 | 450ms | 1200 | Critical |
| Q2 | users.service:102 | 120ms | 500 | High |

### Detailed Findings

#### Issue #[N]: [Query Description]

**Location:**
```
File: [file_path]
Function: [function_name]
Line: [line_number]
```

**Current Query:**
```sql
[Current slow query]
```

**Execution Plan Analysis:**
```
[EXPLAIN output or description]
```

**Problems Identified:**
1. [Problem 1 - e.g., Full table scan]
2. [Problem 2 - e.g., Missing index]
3. [Problem 3 - e.g., N+1 pattern]

**Severity:** [Critical/High/Medium/Low]
**Performance Impact:** [Current: Xms, Expected: Yms]

**Optimized Query:**
```sql
[Optimized query]
```

**Required Index:**
```sql
CREATE INDEX [index_name] ON [table]([columns]);
```

**Explanation:**
[Why this optimization works and expected improvement]

**Testing Recommendations:**
- [ ] Benchmark before/after on representative data
- [ ] Verify index is used in EXPLAIN
- [ ] Test with production-like data volume
- [ ] Monitor write performance impact

### Index Recommendations Summary

| Table | Index Name | Columns | Queries Helped | Priority |
|-------|------------|---------|----------------|----------|
| orders | idx_user_status | user_id, status | Q1, Q5 | High |
| products | idx_category_price | category_id, price | Q3 | Medium |

### Indexes to Remove

| Table | Index Name | Reason | Storage Saved |
|-------|------------|--------|---------------|
| users | idx_old_unused | No queries use this | 50MB |

### Application Code Changes

| File | Change Description | Queries Affected |
|------|-------------------|------------------|
| OrderRepository.java | Replace loop with JOIN | Q1 |
| ProductService.js | Add pagination | Q4 |

### Quick Wins (High Impact, Low Effort)

1. **Add index on orders.user_id** - Improves Q1 by 80%
2. **Select specific columns in UserQuery** - Reduces data transfer 60%
3. **Add LIMIT to admin dashboard query** - Prevents timeout

### Implementation Roadmap

**Phase 1: Index Creation (No Code Changes)**
- [ ] Create idx_orders_user_status
- [ ] Create idx_products_category_price
- [ ] Analyze index usage after 1 week

**Phase 2: Query Rewrites (Code Changes Required)**
- [ ] Refactor N+1 in OrderRepository
- [ ] Implement keyset pagination
- [ ] Add query result caching

**Phase 3: Schema Optimizations (Data Migration)**
- [ ] Denormalize order totals
- [ ] Add summary tables for reporting

---

## Example Optimization

### Before: N+1 Query Problem

**Location:** `src/services/OrderService.js:45`

**Current Code:**
```javascript
async function getOrdersWithItems(userId) {
  const orders = await db.query(
    'SELECT * FROM orders WHERE user_id = ?', [userId]
  );

  // N+1: One query per order
  for (const order of orders) {
    order.items = await db.query(
      'SELECT * FROM order_items WHERE order_id = ?', [order.id]
    );
  }

  return orders;
}
```

**Problem:** If user has 100 orders, this executes 101 queries.

**Optimized Code:**
```javascript
async function getOrdersWithItems(userId) {
  const rows = await db.query(`
    SELECT
      o.id as order_id, o.total, o.status, o.created_at,
      oi.id as item_id, oi.product_id, oi.quantity, oi.price
    FROM orders o
    LEFT JOIN order_items oi ON o.id = oi.order_id
    WHERE o.user_id = ?
    ORDER BY o.created_at DESC, oi.id
  `, [userId]);

  // Transform flat results to nested structure
  return groupOrdersWithItems(rows);
}
```

**Index Required:**
```sql
CREATE INDEX idx_orders_user_created ON orders(user_id, created_at DESC);
CREATE INDEX idx_order_items_order ON order_items(order_id);
```

**Improvement:** 101 queries -> 1 query, ~95% faster

---

**Related Prompts:**
- database_index_optimization.md - Detailed index strategy analysis
- database_performance_analysis.md - Comprehensive database performance review
- performance_bottleneck_identification.md - General performance analysis
- database_schema_design_normalization.md - Schema optimization

**When to Use:**
Use this prompt when queries are slow, during performance optimization sprints, before scaling to handle more traffic, when database CPU is high, or during code review of data access layers.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Specific optimization objective
- ST-02 (Structured Sequential Instructions) - Phased analysis approach
- RT-02 (Multi-Dimensional Analysis Framework) - Multiple optimization dimensions
- DS-02 (Metric Specification) - Performance measurement guidance
- DS-06 (Prioritization and Severity Guidance) - Impact-based prioritization
- ST-03 (Output Format Templates) - Structured report with examples
- AG-05 (Concrete Deliverable Templates) - Before/after code examples
