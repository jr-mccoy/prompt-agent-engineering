---
title: "Entity Framework Core Optimization"
category: software-engineering/dotnet
description: "Analyze Entity Framework Core usage for N+1 queries, tracking overhead, migration issues, and performance optimization opportunities"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - csharp
  - dotnet
  - entity-framework
  - ef-core
  - database
  - performance
  - orm
  - sql
updated: "2026-03-19"
---

# Entity Framework Core Optimization

**Objective:** Analyze an application's Entity Framework Core usage to identify performance anti-patterns, query inefficiencies, configuration issues, and migration problems, then provide specific optimization recommendations.

---

## Inputs / Context

**Required:**
- EF Core `DbContext` configuration and entity classes
- Repository or data access layer code
- EF Core version (6, 7, 8, or 9)

**Optional:**
- Database provider (SQL Server, PostgreSQL, SQLite, MySQL, Cosmos DB)
- Current performance symptoms (slow queries, high memory, timeouts)
- EF Core query logs or SQL profiler output
- Migration history and current migration files
- Database size and expected query volumes

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Distinguish between EF Core version-specific features and recommendations
- Provide the actual SQL that EF Core would generate for flagged LINQ queries when possible
- Account for the specific database provider's capabilities and limitations

**Must Not:**
- Recommend replacing EF Core with Dapper/raw SQL for every performance issue (only for genuinely inappropriate ORM scenarios)
- Assume all lazy loading is bad — evaluate in context
- Flag projections as "incomplete" when only needed columns are selected intentionally

---

## Steps

1. **Review DbContext configuration:**
   - Connection string management (no hardcoded strings, `IDbContextFactory` for background services)
   - DbContext lifetime (scoped for web requests, factory-created for background work)
   - Change tracker configuration (`QueryTrackingBehavior.NoTracking` as default where appropriate)
   - Connection resiliency (`EnableRetryOnFailure` for transient fault handling)
   - Logging and diagnostics configuration
   - Interceptors and `SaveChanges` hooks
   - Database provider-specific optimizations (e.g., `UseQuerySplittingBehavior` for SQL Server)

2. **Analyze query patterns for performance anti-patterns:**
   For each query pattern found, evaluate:
   a. **N+1 queries:** Navigation property access in loops without eager loading (`Include`) or explicit loading
   b. **Over-fetching:** `SELECT *` equivalent — loading full entities when only a few columns are needed (use projections with `Select`)
   c. **Client-side evaluation:** LINQ expressions that can't translate to SQL and execute in memory (flagged as warnings in EF Core 3+)
   d. **Cartesian explosion:** Multiple `Include` calls on collection navigations creating massive result sets (use `AsSplitQuery()`)
   e. **Missing pagination:** `ToList()` on unbounded queries without `Skip`/`Take`
   f. **Unnecessary tracking:** Tracked queries for read-only operations

3. **Review entity model and relationship configuration:**
   - Fluent API vs. data annotation consistency
   - Relationship configuration (one-to-many, many-to-many, owned entities)
   - Index definitions (missing indexes on frequently queried/filtered columns)
   - Value conversions and custom column mappings
   - Inheritance strategy (TPH, TPT, TPC) and its performance implications
   - Shadow properties and backing fields
   - Concurrency tokens (`[ConcurrencyCheck]`, `[Timestamp]`, or `IsRowVersion()`)

4. **Evaluate bulk operations and write patterns:**
   - Batch size configuration for `SaveChanges`
   - Bulk insert/update strategies (EF Core 7+ `ExecuteUpdate`/`ExecuteDelete`, or third-party libraries)
   - Transaction management (implicit vs. explicit transactions, isolation levels)
   - Concurrency conflict handling (`DbUpdateConcurrencyException`)
   - Disconnected entity update patterns (attach, update, or merge strategies)

5. **Review migrations and schema management:**
   - Migration naming conventions and organization
   - Data migrations mixed with schema migrations (anti-pattern — should be separate)
   - Migration idempotency (can migrations be re-run safely?)
   - Seed data approach (`HasData` vs. custom migration vs. startup seeding)
   - Production migration strategy (automated vs. manual, rollback plan)
   - Missing migration for model changes (model snapshot drift)

6. **Identify optimization opportunities with specific fixes.**

---

## Output Format

### Data Access Health Summary
Overall assessment (Optimized / Adequate / Needs Optimization) with the most impactful finding highlighted.

### Query Performance Findings

For each finding:
```
File: [file path]
Line(s): [line numbers]
Pattern: [N+1 | Over-fetching | Client Evaluation | Cartesian Explosion | Missing Pagination | Tracking Overhead]
Severity: [Critical | High | Medium | Low]
Current Code:
  [The problematic LINQ query]
Generated SQL (approximate):
  [The SQL this produces]
Issue: [Why this is a problem]
Optimized Code:
  [The fixed LINQ query]
Expected Impact: [e.g., "Reduces from N+1 queries to 1 query with JOIN"]
```

### Entity Model Findings
Issues with entity configuration, missing indexes, relationship problems.

### Write Pattern Findings
Issues with SaveChanges usage, bulk operations, transaction handling.

### Migration Review
Assessment of migration health and schema management practices.

### Performance Optimization Summary

| Optimization | Category | Impact | Effort | Priority |
|-------------|----------|--------|--------|----------|
| Add `AsNoTracking()` to read endpoints | Tracking | ~15-30% read perf gain | Small | 1 |
| Fix N+1 in `OrderService.GetAll()` | Query | Eliminates N queries | Small | 2 |
| Add index on `Orders.CustomerId` | Schema | Query time reduction | Small | 3 |

---

## Verification

**Quick self-check:**
- [ ] N+1 query patterns are identified with specific code locations
- [ ] Recommendations include both the problematic and fixed LINQ code
- [ ] EF Core version-specific features are correctly referenced
- [ ] Index recommendations are backed by query pattern analysis
- [ ] Migration review checks for data/schema separation

**False-Positive Prevention:**
- Do NOT flag eager loading (`Include`) as "over-fetching" when the related data IS needed
- Do NOT flag tracked queries as wasteful when the entities will be modified and saved
- Do NOT flag `ToList()` as "missing pagination" on queries that legitimately need all results (e.g., dropdown population with bounded data)
- Do NOT flag lazy loading as automatically bad — it may be acceptable for rarely-accessed navigation properties
- Do NOT recommend `AsNoTracking()` on queries where tracked entities are subsequently modified
- DO verify that "N+1" patterns actually execute in a loop context (a single `Include` miss in a non-loop context is just over-fetching)
- DO check if flagged client-side evaluation is on a small, bounded result set where it's acceptable

---

**Techniques Used:**
- ST-01 (Clear Objective Statement) — Focused on EF Core optimization
- ST-02 (Structured Sequential Instructions) — 6-step analysis from config through migrations
- RT-02 (Multi-Dimensional Analysis Framework) — Queries, model, writes, migrations analyzed separately
- RT-05 (Evidence-Based Reasoning) — Actual LINQ and generated SQL required
- DS-06 (Prioritization Guidance) — Impact/effort matrix for prioritization
