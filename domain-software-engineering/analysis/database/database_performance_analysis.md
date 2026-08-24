---
title: "Database Performance Analysis"
category: code-analysis/database
description: "Comprehensive analysis of database performance including query execution, resource utilization, and bottleneck identification"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-02
  - DS-06
  - ST-03
difficulty: advanced
tags:
  - database
  - performance
  - monitoring
  - bottleneck
  - tuning
  - diagnostics
updated: "2026-01-15"
---

# Database Performance Analysis

**Objective:** Conduct a comprehensive analysis of database performance to identify bottlenecks, resource constraints, and optimization opportunities, then provide actionable recommendations with expected performance improvements and implementation priorities.

---

## Instructions

### Phase 1: Performance Baseline Establishment

1. **Collect current performance metrics:**

   **Query Performance:**
   - Average query execution time
   - 95th/99th percentile query times
   - Slow query log analysis
   - Most frequent queries
   - Most expensive queries (by total time)

   **Resource Utilization:**
   - CPU utilization (user, system, iowait)
   - Memory usage (buffer pool, cache hit ratio)
   - Disk I/O (reads, writes, IOPS, latency)
   - Network I/O (if distributed/replicated)

   **Connection Metrics:**
   - Active connections
   - Connection pool utilization
   - Connection wait times
   - Max connections vs. typical usage

   **Lock and Contention:**
   - Lock wait times
   - Deadlock frequency
   - Row/table lock statistics
   - Blocking queries

2. **Identify performance targets:**
   - What response times are acceptable?
   - What throughput is required?
   - What are the SLA requirements?
   - Peak vs. average load expectations

3. **Document workload characteristics:**
   - Read/write ratio
   - Transaction volume
   - Concurrent user count
   - Data growth rate

---

### Phase 2: Query Performance Analysis

1. **Slow Query Investigation:**
   ```sql
   -- PostgreSQL: Find slow queries
   SELECT query, calls, total_time, mean_time, rows
   FROM pg_stat_statements
   ORDER BY total_time DESC
   LIMIT 20;

   -- MySQL: Review slow query log
   -- Or query performance_schema
   SELECT DIGEST_TEXT, COUNT_STAR, SUM_TIMER_WAIT/1000000000 as total_ms
   FROM performance_schema.events_statements_summary_by_digest
   ORDER BY SUM_TIMER_WAIT DESC
   LIMIT 20;
   ```

2. **Query pattern analysis:**
   - Identify N+1 query patterns
   - Find queries with high execution counts
   - Locate queries with high row examination ratios
   - Detect queries causing full table scans

3. **Execution plan analysis:**
   - Analyze top 10 slowest queries
   - Identify missing indexes
   - Find suboptimal join strategies
   - Detect plan regressions

---

### Phase 3: Index Analysis

1. **Index utilization review:**
   ```sql
   -- PostgreSQL: Unused indexes
   SELECT schemaname, relname, indexrelname, idx_scan, idx_tup_read, idx_tup_fetch
   FROM pg_stat_user_indexes
   WHERE idx_scan = 0
   ORDER BY pg_relation_size(indexrelid) DESC;

   -- MySQL: Index usage
   SELECT * FROM sys.schema_unused_indexes;
   ```

2. **Missing index identification:**
   ```sql
   -- PostgreSQL: Sequential scans on large tables
   SELECT relname, seq_scan, seq_tup_read, idx_scan, idx_tup_fetch
   FROM pg_stat_user_tables
   WHERE seq_scan > 0
   ORDER BY seq_tup_read DESC;
   ```

3. **Index efficiency metrics:**
   - Index size vs. table size ratio
   - Index bloat estimation
   - Covering index opportunities
   - Composite index optimization

---

### Phase 4: Resource Utilization Analysis

1. **Memory Analysis:**

   **Buffer Pool/Cache:**
   ```sql
   -- PostgreSQL: Cache hit ratio
   SELECT
     sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)) as cache_hit_ratio
   FROM pg_statio_user_tables;

   -- MySQL: Buffer pool hit ratio
   SHOW STATUS LIKE 'Innodb_buffer_pool%';
   ```

   **Target:** Cache hit ratio should be >99% for OLTP workloads

   **Memory pressure indicators:**
   - Page faults
   - Swap usage
   - OOM killer activations

2. **CPU Analysis:**
   - User CPU (query processing)
   - System CPU (I/O operations)
   - CPU wait time (I/O bound)
   - Query parallelism utilization

3. **Disk I/O Analysis:**
   ```sql
   -- PostgreSQL: I/O statistics
   SELECT * FROM pg_statio_user_tables ORDER BY heap_blks_read DESC;

   -- Check for I/O wait
   -- System level: iostat -x 1
   ```

   **Key metrics:**
   - Read/write IOPS
   - I/O latency (should be <10ms for SSD)
   - I/O queue depth
   - Disk utilization percentage

4. **Connection Analysis:**
   ```sql
   -- PostgreSQL: Connection states
   SELECT state, count(*) FROM pg_stat_activity GROUP BY state;

   -- MySQL: Connection status
   SHOW STATUS LIKE 'Threads%';
   ```

---

### Phase 5: Lock and Contention Analysis

1. **Lock wait analysis:**
   ```sql
   -- PostgreSQL: Current locks
   SELECT blocked.pid, blocked.query, blocking.pid, blocking.query
   FROM pg_stat_activity blocked
   JOIN pg_stat_activity blocking ON blocking.pid = ANY(pg_blocking_pids(blocked.pid));

   -- MySQL: Lock waits
   SELECT * FROM sys.innodb_lock_waits;
   ```

2. **Deadlock investigation:**
   - Review deadlock logs
   - Identify deadlock-prone transactions
   - Analyze lock ordering issues

3. **Contention hotspots:**
   - Tables with high lock wait times
   - Frequently updated rows
   - Auto-increment contention
   - Index maintenance contention

---

### Phase 6: Database Configuration Analysis

1. **Memory configuration:**
   ```
   PostgreSQL:
   - shared_buffers (25% of RAM typical)
   - effective_cache_size (75% of RAM)
   - work_mem (for sorts/hashes)
   - maintenance_work_mem (for VACUUM, CREATE INDEX)

   MySQL:
   - innodb_buffer_pool_size (70-80% of RAM)
   - innodb_log_file_size
   - query_cache_size (often disabled in MySQL 8+)
   ```

2. **Connection configuration:**
   - max_connections vs. typical usage
   - Connection pooler configuration
   - Timeout settings

3. **I/O configuration:**
   - WAL/redo log settings
   - Checkpoint frequency
   - fsync settings
   - Parallel I/O workers

4. **Query optimizer settings:**
   - Cost estimation parameters
   - Join method preferences
   - Parallelism settings

---

### Phase 7: Replication and High Availability Analysis

1. **Replication lag:**
   ```sql
   -- PostgreSQL: Replication status
   SELECT client_addr, state, sent_lsn, write_lsn, flush_lsn, replay_lsn
   FROM pg_stat_replication;

   -- MySQL: Replica lag
   SHOW SLAVE STATUS\G
   ```

2. **Replication performance:**
   - Network bandwidth between primary and replicas
   - Apply lag during peak load
   - Replication thread contention

3. **Failover readiness:**
   - Synchronous vs. asynchronous replication
   - Data loss potential in failover
   - Failover time estimation

---

### Phase 8: Workload-Specific Analysis

1. **OLTP Workloads:**
   - Transaction throughput (TPS)
   - Commit latency
   - Lock contention
   - Connection efficiency

2. **OLAP Workloads:**
   - Query parallelism
   - Scan efficiency
   - Aggregation performance
   - Memory for complex queries

3. **Mixed Workloads:**
   - Resource contention between OLTP and OLAP
   - Read replica utilization
   - Query routing effectiveness

---

### Phase 9: CRITICAL - Evidence-Based Recommendations

**Before making recommendations:**

1. **Verify bottleneck with data:**
   - Is this actually the bottleneck?
   - What's the expected improvement?
   - What's the implementation cost?

2. **Prioritize by impact:**
   - Focus on queries consuming most total time
   - Address resource constraints before micro-optimizations
   - Consider effort-to-impact ratio

3. **Consider side effects:**
   - Will index help queries but hurt writes?
   - Will configuration change affect other workloads?
   - Is there enough headroom for the change?

**Do NOT recommend:**
- Optimizations without baseline measurements
- Configuration changes without understanding current settings
- Index additions without query analysis
- Hardware upgrades when software optimization suffices

---

## Expected Output: Performance Analysis Report

### Executive Summary
- Overall database health: [Good/Needs Attention/Critical]
- Primary bottleneck: [CPU/Memory/I/O/Locks/Queries]
- Estimated improvement potential: [X%]
- Quick wins available: [Yes/No]

### Performance Baseline

| Metric | Current | Target | Gap |
|--------|---------|--------|-----|
| Avg query time | 45ms | <20ms | 25ms |
| 99th percentile | 500ms | <200ms | 300ms |
| Cache hit ratio | 94% | >99% | 5% |
| CPU utilization | 75% | <60% | 15% |
| Lock wait time | 120ms/s | <10ms/s | 110ms/s |

### Top Performance Issues

#### Issue #[N]: [Title]

**Category:** [Query/Index/Configuration/Resource/Contention]
**Severity:** [Critical/High/Medium/Low]
**Impact:** [X% of total database time]

**Evidence:**
```sql
[Query or metric showing the issue]
```

**Current Behavior:**
[Description of current state]

**Root Cause:**
[Why this is happening]

**Recommendation:**
[Specific fix with implementation details]

**Expected Improvement:**
- Query time: [Before] -> [After]
- Resource usage: [Before] -> [After]

**Implementation Effort:** [Low/Medium/High]

### Resource Utilization Analysis

#### CPU
- Current: [X%] average, [Y%] peak
- Breakdown: User [A%], System [B%], Wait [C%]
- Bottleneck: [Yes/No]
- Recommendation: [If applicable]

#### Memory
- Buffer pool size: [X GB]
- Cache hit ratio: [Y%]
- Memory pressure: [None/Low/High]
- Recommendation: [If applicable]

#### Disk I/O
- Read IOPS: [X], Write IOPS: [Y]
- Latency: [Z ms]
- I/O wait: [W%]
- Recommendation: [If applicable]

### Index Recommendations

| Table | Recommended Index | Queries Improved | Priority |
|-------|-------------------|------------------|----------|
| orders | (user_id, created_at) | Q1, Q5, Q12 | High |
| products | (category_id, price) | Q3, Q8 | Medium |

### Unused Indexes (Consider Removal)

| Table | Index Name | Size | Last Used |
|-------|------------|------|-----------|
| users | idx_old_email | 50MB | Never |

### Configuration Recommendations

| Parameter | Current | Recommended | Rationale |
|-----------|---------|-------------|-----------|
| shared_buffers | 1GB | 4GB | Only 25% of available RAM |
| work_mem | 4MB | 64MB | Complex sorts spilling to disk |

### Query Optimization Priorities

| Priority | Query | Current | Target | Fix |
|----------|-------|---------|--------|-----|
| 1 | Order listing | 450ms | 50ms | Add composite index |
| 2 | Product search | 200ms | 30ms | Rewrite with JOIN |
| 3 | User dashboard | 180ms | 40ms | Add caching layer |

### Monitoring Recommendations

Set up alerts for:
- [ ] Query latency > [threshold]
- [ ] Cache hit ratio < 99%
- [ ] Lock wait time > [threshold]
- [ ] Replication lag > [threshold]
- [ ] Connection pool exhaustion

### Implementation Roadmap

**Week 1: Quick Wins**
- [ ] Add missing indexes
- [ ] Tune buffer pool size
- [ ] Fix N+1 query patterns

**Week 2-3: Query Optimization**
- [ ] Rewrite top 5 slow queries
- [ ] Implement query caching
- [ ] Add composite indexes

**Week 4+: Architecture Improvements**
- [ ] Implement read replicas
- [ ] Add connection pooling
- [ ] Schema denormalization for hot paths

---

## Example Analysis: Buffer Pool Too Small

### Finding
Buffer pool cache hit ratio is 94%, causing excessive disk reads.

### Evidence
```sql
-- PostgreSQL
SELECT
  sum(heap_blks_hit) as hits,
  sum(heap_blks_read) as reads,
  sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)) as ratio
FROM pg_statio_user_tables;

-- Result: ratio = 0.94 (should be > 0.99)
```

### Root Cause
`shared_buffers` set to 1GB on server with 16GB RAM. Hot data doesn't fit in cache.

### Recommendation
```
# postgresql.conf
shared_buffers = 4GB  # 25% of RAM
effective_cache_size = 12GB  # 75% of RAM
```

### Expected Improvement
- Cache hit ratio: 94% -> 99%+
- Average query time: -30% (fewer disk reads)
- I/O wait: Significant reduction

---

**Related Prompts:**
- database_query_optimization.md - Detailed query optimization
- database_index_optimization.md - Index strategy analysis
- database_scaling_patterns.md - Scaling architecture review
- performance_bottleneck_identification.md - General performance analysis

**When to Use:**
Use this prompt for regular database health checks, before scaling decisions, when response times degrade, during capacity planning, or as part of production readiness reviews.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Performance optimization objective
- ST-02 (Structured Sequential Instructions) - Systematic analysis phases
- RT-02 (Multi-Dimensional Analysis Framework) - Multiple performance dimensions
- DS-02 (Metric Specification) - Specific performance metrics
- DS-06 (Prioritization and Severity Guidance) - Impact-based prioritization
- ST-03 (Output Format Templates) - Structured report with metrics
