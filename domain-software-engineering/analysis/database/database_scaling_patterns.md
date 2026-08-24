---
title: "Database Scaling Patterns Analysis"
category: code-analysis/database
description: "Analyze database architecture for scalability and recommend appropriate scaling patterns"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - ST-03
difficulty: advanced
tags:
  - database
  - scaling
  - sharding
  - replication
  - partitioning
  - distributed
updated: "2026-01-15"
---

# Database Scaling Patterns Analysis

**Objective:** Analyze current database architecture and workload characteristics to recommend appropriate scaling patterns (vertical, horizontal, read replicas, sharding, partitioning) that meet growth projections while balancing complexity, cost, and operational requirements.

---

## Instructions

### Phase 1: Current State Assessment

1. **Document current architecture:**
   - Database engine and version
   - Server specifications (CPU, RAM, storage)
   - Current data volume per table
   - Number of databases/schemas
   - Replication topology (if any)
   - Connection pooling setup

2. **Measure current utilization:**
   - CPU utilization (average, peak)
   - Memory usage and buffer pool efficiency
   - Storage usage and growth rate
   - IOPS and throughput
   - Connection count (average, peak)
   - Query throughput (QPS/TPS)

3. **Characterize workload:**
   - Read/write ratio
   - Transaction patterns (short/long, simple/complex)
   - Data access patterns (uniform vs. hot spots)
   - Time-based patterns (peak hours, batch jobs)
   - Geographic distribution of users

---

### Phase 2: Growth Projection Analysis

1. **Historical growth analysis:**
   - Data growth rate (GB/month)
   - Transaction growth rate
   - User growth rate
   - Query complexity trends

2. **Future projections:**
   - 6-month projection
   - 1-year projection
   - 3-year projection

3. **Identify scaling triggers:**
   - At what point will current setup become insufficient?
   - Which resource will hit limits first?
   - What's the timeline to action?

---

### Phase 3: Scaling Pattern Evaluation

Evaluate each scaling pattern against your requirements:

#### 1. Vertical Scaling (Scale Up)

**Description:** Increase server resources (CPU, RAM, storage, IOPS)

**When to Use:**
- Current server is underprovisioned
- Workload is not easily partitionable
- Simplicity is paramount
- Headroom still available on larger instances

**Limitations:**
- Hardware limits (max instance size)
- Single point of failure
- Diminishing returns at high end
- Downtime for upgrades (usually)

**Analysis Questions:**
- What's the largest available instance?
- Is current bottleneck addressable by more resources?
- What's the cost curve for larger instances?

```
Example Assessment:
Current: db.r5.xlarge (4 vCPU, 32GB RAM)
Headroom: db.r5.16xlarge (64 vCPU, 512GB RAM) = 16x current
Timeline: Vertical scaling viable for ~18 months
```

#### 2. Read Replicas (Scale Reads)

**Description:** Route read queries to replica databases

**When to Use:**
- Read-heavy workload (>70% reads)
- Can tolerate slight replication lag
- Read queries don't need latest data
- Single-writer bottleneck not an issue

**Limitations:**
- Replication lag (eventual consistency)
- Doesn't help write-heavy workloads
- Added complexity in application
- Cost of replica instances

**Implementation Patterns:**
```
Primary (writes) ─── Replication ──► Replica 1 (reads)
                                 ├──► Replica 2 (reads)
                                 └──► Replica 3 (analytics)
```

**Analysis Questions:**
- What's current read/write ratio?
- Which queries can use replicas?
- What replication lag is acceptable?
- How will application route queries?

#### 3. Database Sharding (Horizontal Partitioning)

**Description:** Distribute data across multiple database instances

**When to Use:**
- Data volume exceeds single-server capacity
- Write throughput exceeds single-server limits
- Clear partitioning key exists
- Geographic distribution needed

**Sharding Strategies:**

**Range-Based Sharding:**
```
Shard 1: user_id 1-1,000,000
Shard 2: user_id 1,000,001-2,000,000
Shard 3: user_id 2,000,001-3,000,000
```
- Pro: Simple, range queries efficient
- Con: Hot spots, rebalancing difficult

**Hash-Based Sharding:**
```
Shard = hash(user_id) % num_shards
```
- Pro: Even distribution
- Con: Range queries require all shards

**Directory-Based Sharding:**
```
Lookup table maps key → shard
```
- Pro: Flexible, easy rebalancing
- Con: Lookup table is single point of failure

**Geographic Sharding:**
```
US users → US shard
EU users → EU shard
Asia users → Asia shard
```
- Pro: Low latency, data residency compliance
- Con: Cross-region queries complex

**Analysis Questions:**
- What's the natural partition key?
- Are cross-shard queries needed?
- How will you handle shard key changes?
- What's the rebalancing strategy?

#### 4. Table Partitioning (Within Single Database)

**Description:** Split large tables into smaller partitions

**When to Use:**
- Large tables (>100M rows)
- Time-series data
- Clear partition key exists
- Queries filter by partition key

**Partition Types:**
```sql
-- Range Partitioning (by date)
CREATE TABLE orders (
  order_id BIGINT,
  created_at TIMESTAMP,
  ...
) PARTITION BY RANGE (created_at);

CREATE TABLE orders_2024_q1 PARTITION OF orders
  FOR VALUES FROM ('2024-01-01') TO ('2024-04-01');

-- List Partitioning (by category)
CREATE TABLE products (...)
PARTITION BY LIST (category);

-- Hash Partitioning (for even distribution)
CREATE TABLE logs (...)
PARTITION BY HASH (id);
```

**Benefits:**
- Partition pruning improves query performance
- Easier data lifecycle management (drop old partitions)
- Parallel query execution across partitions
- Maintenance operations on single partitions

**Analysis Questions:**
- Which tables would benefit from partitioning?
- What's the partition key and granularity?
- How will old partitions be archived/dropped?

#### 5. Caching Layer

**Description:** Cache frequently accessed data in memory

**When to Use:**
- High read frequency on same data
- Data changes infrequently
- Can tolerate cache staleness
- Want to reduce database load

**Caching Patterns:**
```
Application → Cache (Redis/Memcached) → Database

Cache-Aside:
  1. Check cache
  2. If miss, query database
  3. Store in cache
  4. Return result

Write-Through:
  1. Write to cache
  2. Cache writes to database
  3. Return result

Write-Behind:
  1. Write to cache
  2. Return immediately
  3. Async write to database
```

**Analysis Questions:**
- What data is frequently read?
- What's acceptable staleness?
- How will cache invalidation work?
- What's the cache hit ratio target?

#### 6. CQRS (Command Query Responsibility Segregation)

**Description:** Separate read and write models

**When to Use:**
- Read and write patterns are very different
- Complex read queries (aggregations, joins)
- Need optimized read models
- Event-driven architecture

**Pattern:**
```
Commands (Writes) → Write Database (normalized)
                        ↓ (events/CDC)
Queries (Reads)  ← Read Database (denormalized)
```

**Analysis Questions:**
- How different are read/write patterns?
- Can you tolerate eventual consistency?
- How will you synchronize read/write stores?

---

### Phase 4: Trade-off Analysis

For each viable pattern, analyze:

| Factor | Vertical | Read Replicas | Sharding | Partitioning |
|--------|----------|---------------|----------|--------------|
| Complexity | Low | Medium | High | Medium |
| Cost | Medium | Medium | High | Low |
| Consistency | Strong | Eventual | Varies | Strong |
| Query flexibility | High | High | Limited | High |
| Operational burden | Low | Medium | High | Medium |
| Scaling ceiling | Limited | Read-only | High | Limited |

---

### Phase 5: Implementation Considerations

1. **Application changes required:**
   - Connection routing logic
   - Query modification for sharding
   - Cache integration
   - Error handling for distributed systems

2. **Operational requirements:**
   - Monitoring for distributed systems
   - Backup and recovery procedures
   - Failover automation
   - Data rebalancing procedures

3. **Migration path:**
   - How to implement without downtime
   - Data migration strategy
   - Rollback plan
   - Testing approach

---

### Phase 6: CRITICAL - Right-Sizing Recommendations

**Before recommending complex solutions:**

1. **Exhaust simpler options first:**
   - Have you optimized queries?
   - Have you added proper indexes?
   - Have you tuned configuration?
   - Have you tried vertical scaling?

2. **Validate assumptions:**
   - Is the projected growth realistic?
   - Are there alternative approaches to reduce load?
   - Can the application be optimized instead?

3. **Consider operational maturity:**
   - Does the team have distributed systems experience?
   - Is there 24/7 operational support?
   - What's the acceptable complexity level?

**Do NOT recommend:**
- Sharding when vertical scaling has headroom
- Complex distributed architectures for small-scale needs
- Patterns that require capabilities the team lacks
- Over-engineering based on speculative growth

---

## Expected Output: Scaling Strategy Report

### Executive Summary
- Current capacity utilization: [X%]
- Time to capacity exhaustion: [N months]
- Recommended scaling pattern: [Pattern name]
- Implementation complexity: [Low/Medium/High]
- Estimated cost impact: [X% increase/decrease]

### Current State Analysis

| Resource | Current | Capacity | Utilization |
|----------|---------|----------|-------------|
| CPU | X cores | Y cores | Z% |
| Memory | X GB | Y GB | Z% |
| Storage | X TB | Y TB | Z% |
| IOPS | X | Y | Z% |
| Connections | X | Y max | Z% |

### Workload Characteristics

- Read/Write ratio: [X:Y]
- Average QPS: [N]
- Peak QPS: [N]
- Data growth rate: [X GB/month]
- Hot data size: [X GB]

### Growth Projections

| Timeframe | Data Size | QPS | Connections |
|-----------|-----------|-----|-------------|
| Current | X TB | Y | Z |
| 6 months | X TB | Y | Z |
| 1 year | X TB | Y | Z |
| 3 years | X TB | Y | Z |

### Scaling Options Evaluated

#### Option 1: [Pattern Name]

**Viability:** [Recommended/Viable/Not Recommended]
**Complexity:** [Low/Medium/High]
**Cost:** [$ range/month]

**Pros:**
- [Pro 1]
- [Pro 2]

**Cons:**
- [Con 1]
- [Con 2]

**Implementation Requirements:**
- [Requirement 1]
- [Requirement 2]

[Repeat for each option evaluated]

### Recommended Strategy

**Primary Pattern:** [Pattern name]
**Rationale:** [Why this pattern fits]

**Implementation Phases:**

**Phase 1: [Timeframe]**
- [ ] [Task 1]
- [ ] [Task 2]
- Expected outcome: [Description]

**Phase 2: [Timeframe]**
- [ ] [Task 1]
- [ ] [Task 2]
- Expected outcome: [Description]

### Architecture Diagram

```
[ASCII diagram of recommended architecture]
```

### Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk 1] | [H/M/L] | [H/M/L] | [Mitigation] |

### Cost Analysis

| Component | Current Cost | Projected Cost | Change |
|-----------|-------------|----------------|--------|
| Database instances | $X | $Y | +Z% |
| Storage | $X | $Y | +Z% |
| Network | $X | $Y | +Z% |
| Total | $X | $Y | +Z% |

### Success Metrics

Post-implementation, measure:
- [ ] Query latency at [N] QPS
- [ ] Write throughput at [N] TPS
- [ ] Replication lag < [N] seconds
- [ ] Cost per transaction

---

## Example: Read Replica Recommendation

### Scenario
E-commerce application with 80% reads, experiencing database CPU saturation at peak hours.

### Analysis
- Current: Single PostgreSQL instance (8 vCPU, 64GB RAM)
- CPU utilization: 85% peak, 60% average
- Read/write ratio: 80/20
- Replication lag tolerance: 1 second acceptable for product catalog

### Recommendation: Add Read Replicas

**Architecture:**
```
                    ┌─────────────────┐
                    │   Load Balancer │
                    │   (Application) │
                    └────────┬────────┘
                             │
           ┌─────────────────┼─────────────────┐
           │                 │                 │
           ▼                 ▼                 ▼
    ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
    │   Primary   │   │  Replica 1  │   │  Replica 2  │
    │  (Writes)   │──►│  (Reads)    │   │  (Reads)    │
    └─────────────┘   └─────────────┘   └─────────────┘
```

**Implementation:**
1. Set up streaming replication
2. Configure connection pooler (PgBouncer) with read/write splitting
3. Update application to route read queries
4. Add monitoring for replication lag

**Expected Outcome:**
- Primary CPU: 85% → 45%
- Read capacity: 3x current
- Cost increase: ~60% (2 additional instances)

---

**Related Prompts:**
- database_performance_analysis.md - Performance baseline assessment
- database_query_optimization.md - Query optimization before scaling
- architecture_layer_identification.md - System architecture review
- cloud_cost_optimization.md - Cost analysis for scaling decisions

**When to Use:**
Use this prompt when approaching database capacity limits, planning for significant growth, experiencing performance degradation under load, or evaluating architecture for a new high-scale application.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Scaling analysis objective
- ST-02 (Structured Sequential Instructions) - Systematic evaluation approach
- RT-02 (Multi-Dimensional Analysis Framework) - Multiple scaling dimensions
- RT-05 (Trade-off Analysis) - Pattern comparison matrix
- DS-06 (Prioritization and Severity Guidance) - Complexity/cost classification
- ST-03 (Output Format Templates) - Structured strategy report
