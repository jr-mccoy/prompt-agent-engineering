---
title: "Database Migration Strategy Analysis"
category: code-analysis/database
description: "Plan and review database migration strategies for schema changes, data transformations, and version upgrades"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - ST-03
  - QA-02
difficulty: advanced
tags:
  - database
  - migration
  - schema-changes
  - data-transformation
  - versioning
  - deployment
updated: "2026-01-15"
---

# Database Migration Strategy Analysis

**Objective:** Analyze proposed or existing database migrations for safety, reversibility, and data integrity, then provide a comprehensive migration strategy that minimizes downtime and risk while ensuring successful schema evolution.

---

## Instructions

### Phase 1: Migration Context Assessment

1. **Document current state:**
   - Current database schema version
   - Database engine and version (PostgreSQL 14, MySQL 8, etc.)
   - Total data volume per table
   - Active connections and peak usage patterns
   - Existing migration framework (Flyway, Liquibase, Rails migrations, etc.)

2. **Document target state:**
   - Desired schema changes
   - New tables, columns, or constraints
   - Removed or renamed objects
   - Data transformations required
   - Expected data volume post-migration

3. **Identify constraints:**
   - Maximum acceptable downtime
   - Maintenance window availability
   - Rollback requirements
   - Compliance and audit requirements
   - Application deployment dependencies

---

### Phase 2: Migration Type Classification

Classify each proposed change:

1. **Additive (Low Risk):**
   - Adding nullable columns
   - Adding new tables
   - Adding new indexes (may need monitoring)
   - Creating new views

2. **Transformative (Medium Risk):**
   - Adding columns with default values
   - Renaming columns or tables
   - Changing column data types
   - Splitting or merging tables
   - Adding NOT NULL constraints

3. **Destructive (High Risk):**
   - Dropping columns or tables
   - Removing constraints
   - Truncating data
   - Changing primary keys
   - Breaking foreign key relationships

4. **Data Migration (Variable Risk):**
   - Bulk data transformations
   - Data backfills
   - Cross-table data movement
   - Data format conversions

---

### Phase 3: Risk Analysis

For each migration step, analyze:

1. **Data Loss Risk:**
   - Can data be lost during migration?
   - Is the data recoverable?
   - Are there foreign key cascades?

2. **Downtime Risk:**
   - Does this require table locks?
   - How long will locks be held?
   - Can it be done online?

3. **Application Compatibility:**
   - Will old application code work during migration?
   - Is there a breaking change?
   - Can old and new app versions coexist?

4. **Performance Risk:**
   - Will migration cause resource contention?
   - How long will the migration take?
   - Impact on concurrent operations?

5. **Reversibility:**
   - Can this migration be rolled back?
   - Is data transformation reversible?
   - What's the rollback complexity?

---

### Phase 4: Migration Strategy Design

1. **Zero-Downtime Patterns:**

   **Expand-Contract Pattern:**
   ```
   Phase 1: EXPAND
   - Add new column (nullable)
   - Deploy app that writes to both columns
   - Backfill new column from old

   Phase 2: MIGRATE
   - Deploy app that reads from new column
   - Verify data consistency

   Phase 3: CONTRACT
   - Make new column NOT NULL
   - Deploy app that only uses new column
   - Drop old column
   ```

   **Blue-Green Database Pattern:**
   - Maintain two schema versions
   - Switch traffic between versions
   - Requires application version awareness

2. **Column Rename Strategy:**
   ```sql
   -- Step 1: Add new column
   ALTER TABLE users ADD COLUMN full_name VARCHAR(200);

   -- Step 2: Backfill data
   UPDATE users SET full_name = name WHERE full_name IS NULL;

   -- Step 3: App reads from both, writes to both
   -- Step 4: App reads from new only, writes to both
   -- Step 5: App uses new column only

   -- Step 6: Drop old column (after verification)
   ALTER TABLE users DROP COLUMN name;
   ```

3. **Table Split Strategy:**
   ```sql
   -- Original: users table with profile data

   -- Step 1: Create new table
   CREATE TABLE user_profiles (
     user_id INT PRIMARY KEY REFERENCES users(id),
     bio TEXT,
     avatar_url VARCHAR(500)
   );

   -- Step 2: Migrate data
   INSERT INTO user_profiles (user_id, bio, avatar_url)
   SELECT id, bio, avatar_url FROM users;

   -- Step 3: Update application
   -- Step 4: Verify data consistency
   -- Step 5: Remove columns from original table
   ```

4. **Large Table Migrations:**
   - Batch processing to avoid long locks
   - Off-peak execution windows
   - Progress tracking and resumability
   - Parallel processing where possible

---

### Phase 5: Rollback Planning

1. **For each migration, define rollback:**
   ```sql
   -- Forward migration
   ALTER TABLE orders ADD COLUMN discount_amount DECIMAL(10,2) DEFAULT 0;

   -- Rollback migration
   ALTER TABLE orders DROP COLUMN discount_amount;
   ```

2. **Data-preserving rollbacks:**
   ```sql
   -- If column was renamed, keep data accessible
   -- Forward: rename name -> full_name
   -- Rollback: rename full_name -> name (data preserved)
   ```

3. **Point-in-time recovery planning:**
   - Backup before migration
   - Transaction log position for PITR
   - Tested restore procedure

4. **Rollback triggers:**
   - Define conditions that trigger rollback
   - Error thresholds
   - Performance degradation limits
   - Data consistency check failures

---

### Phase 6: Testing Strategy

1. **Pre-migration testing:**
   - Test on production-like data volume
   - Verify migration time estimates
   - Test rollback procedure
   - Validate application compatibility

2. **Test data considerations:**
   ```sql
   -- Test with representative data:
   -- - Boundary values
   -- - NULL values
   -- - Maximum length strings
   -- - Unicode characters
   -- - Edge case dates (leap years, timezone boundaries)
   ```

3. **Dry run validation:**
   - Execute migration in staging
   - Compare schema pre/post
   - Verify data integrity
   - Measure execution time

4. **Application testing:**
   - Test with old app version + new schema
   - Test with new app version + old schema (if applicable)
   - Load testing post-migration

---

### Phase 7: Execution Checklist

**Before Migration:**
- [ ] Full database backup completed
- [ ] Backup verified (test restore)
- [ ] Maintenance window communicated
- [ ] Rollback scripts prepared and tested
- [ ] Monitoring dashboards ready
- [ ] On-call team notified

**During Migration:**
- [ ] Monitor lock waits and blocking
- [ ] Track migration progress
- [ ] Watch for replication lag
- [ ] Monitor disk space usage
- [ ] Check application errors

**After Migration:**
- [ ] Verify schema changes applied
- [ ] Run data consistency checks
- [ ] Monitor application performance
- [ ] Verify replication caught up
- [ ] Update documentation

---

### Phase 8: CRITICAL - Safety Checks

**Before recommending any migration:**

1. **Verify backup strategy:**
   - When was the last backup?
   - How long does restore take?
   - Is point-in-time recovery available?

2. **Assess lock impact:**
   - DDL statements acquire locks
   - Large tables may lock for minutes/hours
   - Consider online DDL options

3. **Check for blocking operations:**
   ```sql
   -- PostgreSQL: Check for blocking
   SELECT blocked.pid, blocked.query, blocking.pid, blocking.query
   FROM pg_stat_activity blocked
   JOIN pg_stat_activity blocking ON blocking.pid = ANY(pg_blocking_pids(blocked.pid));
   ```

4. **Validate migration framework:**
   - Is the migration idempotent?
   - Does it handle partial failures?
   - Is there transaction wrapping?

**Do NOT recommend:**
- Migrations without tested rollback
- Large table DDL during peak hours
- Data deletion without backup verification
- Breaking changes without application coordination

---

## Expected Output: Migration Strategy Report

### Executive Summary
- Number of migration steps: [N]
- Risk level: [Low/Medium/High]
- Estimated downtime: [X minutes/zero]
- Rollback complexity: [Simple/Moderate/Complex]
- Recommended approach: [Approach name]

### Migration Inventory

| Step | Type | Risk | Downtime | Reversible |
|------|------|------|----------|------------|
| 1. Add status column | Additive | Low | 0 | Yes |
| 2. Backfill status | Data | Medium | 0 | N/A |
| 3. Add NOT NULL | Transformative | Medium | <1min | Yes |

### Detailed Migration Plan

#### Step [N]: [Description]

**Change Type:** [Additive/Transformative/Destructive/Data]
**Risk Level:** [Low/Medium/High]
**Estimated Duration:** [X minutes]
**Downtime Required:** [Yes/No]

**Forward Migration:**
```sql
[SQL statements]
```

**Rollback Migration:**
```sql
[SQL statements for rollback]
```

**Prerequisites:**
- [ ] [Prerequisite 1]
- [ ] [Prerequisite 2]

**Verification:**
```sql
-- Verify migration succeeded
[Verification queries]
```

**Risks and Mitigations:**
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Lock timeout | Medium | High | Execute during low traffic |

**Application Changes Required:**
- [ ] [Application change 1]
- [ ] [Application change 2]

### Execution Timeline

```
T-24h: Announce maintenance window
T-4h:  Final backup
T-1h:  Verify backup, notify team
T-0:   Begin migration
T+Xm:  Migration complete, begin verification
T+Ym:  Verification complete, resume normal operations
T+24h: Monitor for issues, keep rollback ready
T+7d:  Remove rollback scripts, close maintenance ticket
```

### Rollback Plan

**Trigger Conditions:**
- Application error rate exceeds X%
- Query latency exceeds Xms
- Data consistency check fails
- Migration exceeds time limit

**Rollback Procedure:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Estimated Rollback Time:** [X minutes]

### Monitoring Checklist

During migration, monitor:
- [ ] Database CPU utilization
- [ ] Lock wait times
- [ ] Replication lag
- [ ] Application error rates
- [ ] Query latency percentiles

### Post-Migration Validation

```sql
-- Data integrity checks
[Validation queries]

-- Expected results
[Expected output]
```

---

## Example: Column Rename Migration

### Scenario
Rename `users.name` to `users.full_name` with zero downtime.

### Migration Strategy: Expand-Contract

**Step 1: Add new column (Safe - Additive)**
```sql
-- Migration V001
ALTER TABLE users ADD COLUMN full_name VARCHAR(200);
```

**Step 2: Backfill data (Safe - Batch)**
```sql
-- Migration V002 (run in batches)
UPDATE users
SET full_name = name
WHERE full_name IS NULL
  AND id BETWEEN ? AND ?;
```

**Step 3: Deploy dual-write application**
```
-- Application writes to BOTH columns
-- Application reads from 'name' (old)
```

**Step 4: Switch reads**
```
-- Application writes to BOTH columns
-- Application reads from 'full_name' (new)
```

**Step 5: Deploy single-write application**
```
-- Application writes to 'full_name' only
-- Application reads from 'full_name' only
```

**Step 6: Drop old column (Contract)**
```sql
-- Migration V003 (after verification period)
ALTER TABLE users DROP COLUMN name;
```

**Total downtime: 0**
**Rollback possible until Step 6**

---

**Related Prompts:**
- database_schema_design_normalization.md - Schema design best practices
- database_performance_analysis.md - Performance impact assessment
- devops_database_deployment.md - Deployment automation
- engineering_delivery_sprint_planner.md - Sprint planning for migrations

**When to Use:**
Use this prompt when planning schema changes, reviewing migration scripts before execution, designing zero-downtime deployment strategies, or recovering from failed migrations. Essential for production database changes.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Migration safety objective
- ST-02 (Structured Sequential Instructions) - Phased migration approach
- RT-02 (Multi-Dimensional Analysis Framework) - Risk analysis dimensions
- RT-05 (Trade-off Analysis) - Downtime vs. complexity trade-offs
- DS-06 (Prioritization and Severity Guidance) - Risk classification
- ST-03 (Output Format Templates) - Structured migration plan format
- QA-02 (Safety Check Requirements) - Pre-migration verification
