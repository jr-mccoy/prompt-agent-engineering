---
title: "Database Index Optimization Analysis"
category: code-analysis/database
description: "Analyze database indexes for effectiveness and recommend optimal indexing strategy"
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
  - index
  - optimization
  - performance
  - query-tuning
updated: "2026-01-15"
---

# Database Index Optimization Analysis

**Objective:** Analyze existing database indexes for effectiveness and coverage, identify missing indexes that would improve query performance, and recommend an optimal indexing strategy that balances read performance with write overhead and storage costs.

---

## Instructions

### Phase 1: Current Index Inventory

1. **Document all existing indexes:**
   ```sql
   -- PostgreSQL: List all indexes
   SELECT
     schemaname,
     tablename,
     indexname,
     indexdef
   FROM pg_indexes
   WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
   ORDER BY tablename, indexname;

   -- MySQL: List all indexes
   SELECT
     TABLE_NAME,
     INDEX_NAME,
     COLUMN_NAME,
     SEQ_IN_INDEX,
     NON_UNIQUE
   FROM INFORMATION_SCHEMA.STATISTICS
   WHERE TABLE_SCHEMA = DATABASE()
   ORDER BY TABLE_NAME, INDEX_NAME, SEQ_IN_INDEX;
   ```

2. **For each index, document:**
   - Table name
   - Index name
   - Column(s) included
   - Index type (B-tree, Hash, GIN, GiST, etc.)
   - Unique or non-unique
   - Partial index condition (if applicable)
   - Include columns (if covering index)

3. **Calculate index statistics:**
   - Total index size per table
   - Index-to-table size ratio
   - Number of indexes per table

---

### Phase 2: Index Usage Analysis

1. **Identify unused indexes:**
   ```sql
   -- PostgreSQL: Unused indexes
   SELECT
     schemaname || '.' || relname AS table,
     indexrelname AS index,
     pg_size_pretty(pg_relation_size(indexrelid)) AS size,
     idx_scan AS scans
   FROM pg_stat_user_indexes
   WHERE idx_scan = 0
   ORDER BY pg_relation_size(indexrelid) DESC;

   -- MySQL: Unused indexes (requires performance_schema)
   SELECT * FROM sys.schema_unused_indexes;
   ```

2. **Analyze index scan frequency:**
   ```sql
   -- PostgreSQL: Index usage stats
   SELECT
     relname AS table,
     indexrelname AS index,
     idx_scan AS scans,
     idx_tup_read AS tuples_read,
     idx_tup_fetch AS tuples_fetched
   FROM pg_stat_user_indexes
   ORDER BY idx_scan DESC;
   ```

3. **Identify over-indexed tables:**
   - Tables with many indexes but few writes
   - Redundant indexes (subset of another index)
   - Duplicate indexes

---

### Phase 3: Missing Index Identification

1. **Analyze query workload for missing indexes:**
   ```sql
   -- PostgreSQL: Tables with sequential scans
   SELECT
     relname AS table,
     seq_scan,
     seq_tup_read,
     idx_scan,
     seq_tup_read / NULLIF(seq_scan, 0) AS avg_seq_tuples
   FROM pg_stat_user_tables
   WHERE seq_scan > 0
   ORDER BY seq_tup_read DESC;

   -- MySQL: Missing index suggestions
   SELECT * FROM sys.schema_tables_with_full_table_scans;
   ```

2. **Review slow query log for patterns:**
   - Queries with full table scans
   - Queries with filesort operations
   - Queries with temporary tables
   - Queries with high rows_examined/rows_sent ratio

3. **Common patterns requiring indexes:**
   ```sql
   -- WHERE clause columns
   SELECT * FROM orders WHERE user_id = ?
   -- Index: CREATE INDEX idx_orders_user ON orders(user_id);

   -- JOIN columns
   SELECT * FROM orders o JOIN users u ON o.user_id = u.id
   -- Index: CREATE INDEX idx_orders_user ON orders(user_id);

   -- ORDER BY columns
   SELECT * FROM products ORDER BY created_at DESC
   -- Index: CREATE INDEX idx_products_created ON products(created_at DESC);

   -- GROUP BY columns
   SELECT category_id, COUNT(*) FROM products GROUP BY category_id
   -- Index: CREATE INDEX idx_products_category ON products(category_id);
   ```

---

### Phase 4: Index Type Selection

1. **B-tree indexes (default, most common):**
   ```
   Best for:
   - Equality comparisons (=)
   - Range queries (<, >, BETWEEN)
   - Sorting (ORDER BY)
   - Pattern matching with prefix (LIKE 'abc%')

   Not suitable for:
   - Full-text search
   - Spatial queries
   - Array contains operations
   ```

2. **Hash indexes:**
   ```
   Best for:
   - Equality comparisons only (=)

   Limitations:
   - No range queries
   - Not crash-safe in some databases (older PostgreSQL)
   - Rarely used in practice
   ```

3. **GIN indexes (PostgreSQL):**
   ```sql
   -- Full-text search
   CREATE INDEX idx_docs_content ON documents USING gin(to_tsvector('english', content));

   -- JSONB queries
   CREATE INDEX idx_data_jsonb ON events USING gin(metadata);

   -- Array contains
   CREATE INDEX idx_tags ON articles USING gin(tags);
   ```

4. **GiST indexes (PostgreSQL):**
   ```sql
   -- Geometric/spatial data
   CREATE INDEX idx_locations ON places USING gist(location);

   -- Range types
   CREATE INDEX idx_reservations ON bookings USING gist(duration);
   ```

5. **BRIN indexes (PostgreSQL):**
   ```sql
   -- Very large tables with natural ordering
   CREATE INDEX idx_logs_time ON logs USING brin(created_at);

   -- Best for: Time-series data, append-only tables
   -- Very small index size, but less precise
   ```

---

### Phase 5: Composite Index Design

1. **Column ordering in composite indexes:**
   ```
   Rule: Most selective column first, OR
   Rule: Equality columns before range columns

   Query: WHERE category_id = ? AND price > ? ORDER BY created_at

   Best: CREATE INDEX idx ON products(category_id, price, created_at);
   - category_id: equality (most restrictive position)
   - price: range
   - created_at: ORDER BY
   ```

2. **The "leftmost prefix" rule:**
   ```
   Index: (a, b, c)

   Can efficiently support:
   ✓ WHERE a = ?
   ✓ WHERE a = ? AND b = ?
   ✓ WHERE a = ? AND b = ? AND c = ?
   ✓ WHERE a = ? ORDER BY b
   ✓ ORDER BY a, b, c

   Cannot efficiently support:
   ✗ WHERE b = ?
   ✗ WHERE c = ?
   ✗ WHERE b = ? AND c = ?
   ✗ ORDER BY b, c
   ```

3. **Covering indexes (Index-Only Scans):**
   ```sql
   -- Query only needs these columns:
   SELECT order_id, total, status FROM orders WHERE user_id = ?

   -- Covering index (includes all needed columns):
   -- PostgreSQL
   CREATE INDEX idx_orders_covering ON orders(user_id)
   INCLUDE (order_id, total, status);

   -- MySQL
   CREATE INDEX idx_orders_covering ON orders(user_id, order_id, total, status);

   -- Benefit: No table lookup needed (index-only scan)
   ```

---

### Phase 6: Partial and Filtered Indexes

1. **Partial indexes (PostgreSQL):**
   ```sql
   -- Only index active users (most queries filter by active)
   CREATE INDEX idx_users_email_active ON users(email)
   WHERE active = true;

   -- Only index recent orders
   CREATE INDEX idx_orders_recent ON orders(created_at)
   WHERE created_at > '2024-01-01';

   -- Only index non-null values
   CREATE INDEX idx_products_sku ON products(sku)
   WHERE sku IS NOT NULL;
   ```

2. **Filtered indexes (SQL Server):**
   ```sql
   CREATE INDEX idx_orders_pending ON orders(order_date)
   WHERE status = 'pending';
   ```

3. **Benefits of partial indexes:**
   - Smaller index size
   - Faster index maintenance
   - More relevant index statistics
   - Better cache utilization

---

### Phase 7: Index Maintenance Analysis

1. **Index bloat assessment:**
   ```sql
   -- PostgreSQL: Estimate index bloat
   SELECT
     schemaname || '.' || relname AS table,
     indexrelname AS index,
     pg_size_pretty(pg_relation_size(indexrelid)) AS size,
     round(100 * pg_relation_size(indexrelid) /
           NULLIF(pg_relation_size(relid), 0)) AS index_to_table_pct
   FROM pg_stat_user_indexes
   ORDER BY pg_relation_size(indexrelid) DESC;
   ```

2. **Reindex requirements:**
   - When to REINDEX (bloat > 50%, corruption)
   - REINDEX CONCURRENTLY (PostgreSQL 12+)
   - Online index rebuild (MySQL, SQL Server)

3. **Index maintenance impact:**
   - Write amplification from many indexes
   - Lock contention during index updates
   - Transaction log overhead

---

### Phase 8: CRITICAL - Index Trade-off Analysis

**Before recommending new indexes:**

1. **Verify the benefit:**
   - Will the query actually use this index?
   - Test with EXPLAIN before and after
   - Is the selectivity high enough?

2. **Consider the cost:**
   - Every INSERT must update all indexes
   - Every UPDATE on indexed columns updates indexes
   - Storage overhead for index data
   - Index maintenance operations

3. **Rule of thumb:**
   ```
   Good candidates for indexing:
   - Columns in WHERE with high selectivity
   - Foreign key columns
   - Columns used in JOINs
   - Columns in ORDER BY (if sorting is slow)

   Poor candidates for indexing:
   - Low selectivity columns (boolean, status with few values)
   - Frequently updated columns
   - Columns rarely used in queries
   - Small tables (full scan is fast enough)
   ```

**Do NOT recommend:**
- Indexes on tables with <1000 rows
- Indexes on every column
- Duplicate or redundant indexes
- Indexes without verifying query patterns

---

## Expected Output: Index Optimization Report

### Executive Summary
- Total indexes analyzed: [N]
- Unused indexes found: [N] (potential [X GB] savings)
- Missing indexes identified: [N]
- Redundant indexes found: [N]
- Estimated performance improvement: [X%]

### Current Index Overview

| Table | Indexes | Table Size | Index Size | Index Ratio |
|-------|---------|------------|------------|-------------|
| orders | 5 | 2.3 GB | 1.8 GB | 78% |
| users | 3 | 500 MB | 200 MB | 40% |

### Unused Indexes (Recommend Removal)

| Table | Index Name | Size | Last Used | Removal Impact |
|-------|------------|------|-----------|----------------|
| users | idx_old_phone | 45 MB | Never | None (verify) |
| orders | idx_temp_status | 120 MB | Never | None |

**Verification Query:**
```sql
-- Before removing, verify no recent usage
SELECT idx_scan FROM pg_stat_user_indexes WHERE indexrelname = 'idx_name';
```

**Removal Script:**
```sql
DROP INDEX CONCURRENTLY idx_old_phone;
DROP INDEX CONCURRENTLY idx_temp_status;
```

### Redundant Indexes (Recommend Consolidation)

| Table | Redundant Index | Covered By | Action |
|-------|-----------------|------------|--------|
| orders | idx_orders_user | idx_orders_user_date | Remove |
| products | idx_cat | idx_cat_price | Remove |

**Explanation:**
```
idx_orders_user(user_id) is redundant because
idx_orders_user_date(user_id, created_at) covers all queries
that idx_orders_user would serve.
```

### Missing Indexes (Recommend Addition)

#### Index #[N]: [Description]

**Table:** [table_name]
**Reason:** [Why this index is needed]

**Query Pattern:**
```sql
[Query that would benefit]
```

**Current Execution (without index):**
```
Seq Scan on orders  (cost=0.00..15420.00 rows=100 width=50)
  Filter: (user_id = 12345)
  Rows Removed by Filter: 499900
  Execution Time: 450ms
```

**Recommended Index:**
```sql
CREATE INDEX CONCURRENTLY idx_orders_user_id
ON orders(user_id);
```

**Expected Execution (with index):**
```
Index Scan using idx_orders_user_id  (cost=0.42..8.44 rows=100 width=50)
  Index Cond: (user_id = 12345)
  Execution Time: 2ms
```

**Improvement:** 450ms → 2ms (99.5% faster)

### Index Optimization Recommendations

| Priority | Action | Table | Impact | Effort |
|----------|--------|-------|--------|--------|
| High | Add index | orders(user_id, status) | -80% query time | Low |
| High | Remove unused | users.idx_old | +45MB space | Low |
| Medium | Add covering | products | -60% query time | Low |
| Low | Rebuild bloated | orders.idx_date | -20% size | Medium |

### Implementation Plan

**Phase 1: Safe Removals (No Risk)**
```sql
-- Verify these have 0 scans in pg_stat_user_indexes
DROP INDEX CONCURRENTLY IF EXISTS idx_old_phone;
DROP INDEX CONCURRENTLY IF EXISTS idx_temp_status;
```

**Phase 2: Add Missing Indexes**
```sql
-- Add during low-traffic period
CREATE INDEX CONCURRENTLY idx_orders_user_status
ON orders(user_id, status);

CREATE INDEX CONCURRENTLY idx_products_category_price
ON products(category_id, price);
```

**Phase 3: Optimize Existing**
```sql
-- Rebuild bloated indexes
REINDEX CONCURRENTLY idx_orders_created_at;
```

### Monitoring After Changes

After implementing changes, monitor:
- [ ] Query execution times (should decrease)
- [ ] Index scan usage (new indexes should be used)
- [ ] Write performance (should not significantly degrade)
- [ ] Storage usage (should reflect removals/additions)

---

## Example: Composite Index Design

### Scenario
Slow query: Get pending orders for a user, sorted by date

### Query
```sql
SELECT * FROM orders
WHERE user_id = 12345
  AND status = 'pending'
ORDER BY created_at DESC
LIMIT 20;
```

### Current Execution
```
Sort  (cost=15000.00..15001.00)
  ->  Seq Scan on orders  (cost=0.00..14900.00)
        Filter: (user_id = 12345 AND status = 'pending')
Execution Time: 850ms
```

### Analysis
- Full table scan (no useful index)
- In-memory sort required
- All three columns should be in index

### Recommended Index
```sql
CREATE INDEX idx_orders_user_status_created
ON orders(user_id, status, created_at DESC);
```

### Improved Execution
```
Index Scan using idx_orders_user_status_created  (cost=0.42..45.00)
  Index Cond: (user_id = 12345 AND status = 'pending')
Execution Time: 3ms
```

### Improvement
- 850ms → 3ms (99.6% faster)
- No sort needed (index already ordered)
- Index-only scan possible if we add INCLUDE columns

---

**Related Prompts:**
- database_query_optimization.md - Query-level optimization
- database_performance_analysis.md - Overall performance review
- database_schema_design_normalization.md - Schema design impact on indexing
- performance_bottleneck_identification.md - General performance analysis

**When to Use:**
Use this prompt during regular database maintenance, when queries become slow, before and after major data growth, when storage costs increase significantly, or as part of performance optimization initiatives.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Index optimization objective
- ST-02 (Structured Sequential Instructions) - Systematic analysis phases
- RT-02 (Multi-Dimensional Analysis Framework) - Multiple index dimensions
- DS-02 (Metric Specification) - Index usage metrics
- DS-06 (Prioritization and Severity Guidance) - Impact-based prioritization
- ST-03 (Output Format Templates) - Structured report format
- AG-05 (Concrete Deliverable Templates) - SQL examples throughout
