---
title: "Database Schema Design and Normalization Analysis"
category: code-analysis/database
description: "Analyze database schema design for normalization issues, redundancy, and structural best practices"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - ST-03
difficulty: intermediate
tags:
  - database
  - schema
  - normalization
  - data-modeling
  - relational
  - design
updated: "2026-01-15"
---

# Database Schema Design and Normalization Analysis

**Objective:** Analyze database schema design to identify normalization violations, redundancy issues, and structural problems, then provide recommendations for optimal schema organization that balances data integrity with query performance.

---

## Instructions

### Phase 1: Schema Discovery and Documentation

1. **Identify and document all database objects:**
   - Tables/collections with their purpose
   - Columns/fields with data types and constraints
   - Primary keys and unique constraints
   - Foreign key relationships
   - Indexes and their configurations
   - Views, stored procedures, and triggers

2. **Create relationship inventory:**
   - One-to-one relationships
   - One-to-many relationships
   - Many-to-many relationships (including junction tables)
   - Self-referencing relationships
   - Polymorphic associations

3. **Document current constraints:**
   - NOT NULL constraints
   - DEFAULT values
   - CHECK constraints
   - UNIQUE constraints
   - Cascading rules (ON DELETE, ON UPDATE)

---

### Phase 2: Normalization Analysis

1. **First Normal Form (1NF) Analysis:**
   - Check for atomic values (no repeating groups)
   - Identify comma-separated values in single columns
   - Find arrays stored as strings (e.g., "tag1,tag2,tag3")
   - Locate JSON/XML blobs storing multiple values
   - Check for numbered columns (item1, item2, item3)

   **Violations to look for:**
   ```sql
   -- BAD: Repeating groups
   CREATE TABLE orders (
     order_id INT PRIMARY KEY,
     item1 VARCHAR(100), item1_qty INT, item1_price DECIMAL,
     item2 VARCHAR(100), item2_qty INT, item2_price DECIMAL
   );

   -- BAD: Comma-separated values
   CREATE TABLE users (
     user_id INT PRIMARY KEY,
     roles VARCHAR(255)  -- Contains "admin,editor,viewer"
   );
   ```

2. **Second Normal Form (2NF) Analysis:**
   - Verify all non-key attributes depend on the entire primary key
   - Identify partial dependencies (especially in composite keys)
   - Check for attributes that depend on only part of a composite key

   **Violations to look for:**
   ```sql
   -- BAD: Partial dependency
   CREATE TABLE order_items (
     order_id INT,
     product_id INT,
     product_name VARCHAR(100),  -- Depends only on product_id
     product_price DECIMAL,       -- Depends only on product_id
     quantity INT,
     PRIMARY KEY (order_id, product_id)
   );
   ```

3. **Third Normal Form (3NF) Analysis:**
   - Identify transitive dependencies
   - Find non-key attributes that depend on other non-key attributes
   - Check for derived or calculated values stored redundantly

   **Violations to look for:**
   ```sql
   -- BAD: Transitive dependency
   CREATE TABLE employees (
     employee_id INT PRIMARY KEY,
     department_id INT,
     department_name VARCHAR(100),  -- Depends on department_id, not employee_id
     department_location VARCHAR(100)  -- Also transitive
   );
   ```

4. **Boyce-Codd Normal Form (BCNF) Analysis:**
   - Check if every determinant is a candidate key
   - Identify functional dependencies where determinant is not a superkey
   - Particularly important for tables with multiple candidate keys

5. **Higher Normal Forms (if applicable):**
   - Fourth Normal Form (4NF): Multi-valued dependencies
   - Fifth Normal Form (5NF): Join dependencies
   - Note: Only analyze if specific anomalies suggest these issues

---

### Phase 3: Redundancy and Anomaly Analysis

1. **Identify update anomalies:**
   - Data that must be updated in multiple places
   - Denormalized values that can become inconsistent
   - Calculated totals stored alongside source data

2. **Identify insertion anomalies:**
   - Data that cannot be inserted without unrelated data
   - Missing information required by over-coupled tables
   - Required fields that force NULL placeholder values

3. **Identify deletion anomalies:**
   - Useful data lost when other data is deleted
   - Information stored in only one place unnecessarily
   - Cascade delete risks

4. **Calculate redundancy metrics:**
   - Estimate storage overhead from duplication
   - Identify most frequently duplicated data
   - Assess update frequency vs. duplication cost

---

### Phase 4: Denormalization Assessment

**Not all denormalization is bad.** Evaluate intentional denormalization:

1. **Identify justified denormalization:**
   - Read-heavy tables with expensive joins
   - Materialized aggregates for reporting
   - Caching frequently accessed derived data
   - Partitioned data for performance

2. **Assess denormalization strategy:**
   - Is the denormalization documented?
   - Are there triggers/procedures to maintain consistency?
   - Is the update frequency low enough to justify duplication?
   - Are there clear performance benefits?

3. **Identify unjustified denormalization:**
   - Copy-paste data without clear performance benefit
   - Inconsistent redundancy (some duplicated, some not)
   - No mechanism to maintain data consistency

---

### Phase 5: Schema Quality Assessment

1. **Naming conventions:**
   - Consistent table naming (singular vs. plural)
   - Column naming patterns (snake_case, camelCase)
   - Foreign key naming conventions
   - Index naming conventions

2. **Data type appropriateness:**
   - Correct types for data (VARCHAR vs TEXT, INT vs BIGINT)
   - Appropriate precision for numeric types
   - Date/time type selection (DATE, DATETIME, TIMESTAMP)
   - Boolean representation consistency

3. **Constraint completeness:**
   - Missing NOT NULL where data is always required
   - Missing foreign keys for logical relationships
   - Absent CHECK constraints for business rules
   - Insufficient unique constraints

4. **Default value strategy:**
   - Sensible defaults for non-nullable columns
   - Timestamp defaults (CURRENT_TIMESTAMP)
   - Boolean defaults

---

### Phase 6: CRITICAL - Context-Aware Analysis

**Before flagging violations, consider:**

1. **Performance trade-offs:**
   - Would normalization require expensive joins?
   - Is the table read-heavy or write-heavy?
   - What's the data volume and growth rate?

2. **Application requirements:**
   - Does the application layer enforce consistency?
   - Are atomic updates handled at application level?
   - Is eventual consistency acceptable?

3. **Database engine capabilities:**
   - Does the engine support efficient joins?
   - Are materialized views available?
   - What indexing options exist?

**Do NOT flag:**
- Intentional denormalization with clear documentation
- OLAP/reporting schemas optimized for reads
- NoSQL schemas following document model best practices
- Staging/ETL tables with temporary structures

---

## Expected Output: Schema Analysis Report

### Executive Summary
- Overall schema health score (1-10)
- Number of tables analyzed
- Normalization level achieved (1NF, 2NF, 3NF, BCNF)
- Critical issues requiring immediate attention
- Strategic recommendations

### Schema Overview

| Table Name | Columns | Primary Key | Foreign Keys | Normalization Level |
|------------|---------|-------------|--------------|---------------------|
| users | 12 | user_id | 0 | 3NF |
| orders | 15 | order_id | 2 | 2NF (violation found) |

### Detailed Findings

For each issue found:

#### Issue #[N]: [Normalization Level] Violation in [Table Name]

**Type:** [1NF/2NF/3NF/BCNF Violation | Redundancy | Anomaly Risk]
**Severity:** [Critical/High/Medium/Low]
**Table:** [table_name]

**Current Schema:**
```sql
[Current problematic schema definition]
```

**Problem:**
[Clear explanation of the normalization violation and its consequences]

**Anomaly Risks:**
- Update: [description]
- Insert: [description]
- Delete: [description]

**Recommended Schema:**
```sql
[Normalized schema definition with proper structure]
```

**Migration Considerations:**
- Data transformation required
- Foreign key updates needed
- Application code changes
- Query modifications

**Trade-off Analysis:**
- Storage: [impact]
- Read performance: [impact]
- Write performance: [impact]
- Maintenance: [impact]

### Positive Patterns Observed

Document well-designed aspects of the schema:
- Proper relationship modeling
- Good constraint usage
- Appropriate denormalization decisions

### Recommendations Summary

| Priority | Issue | Table | Effort | Impact |
|----------|-------|-------|--------|--------|
| High | 3NF violation | employees | Medium | Eliminates update anomalies |
| Medium | Missing FK | orders | Low | Enforces referential integrity |

### Schema Evolution Roadmap

1. **Immediate (Critical Issues)**
   - [List of changes]

2. **Short-term (High Priority)**
   - [List of changes]

3. **Long-term (Optimization)**
   - [List of changes]

---

## Example Analysis

### Example 1NF Violation

**Table:** products

**Current Schema:**
```sql
CREATE TABLE products (
  product_id INT PRIMARY KEY,
  name VARCHAR(100),
  categories VARCHAR(500),  -- "electronics,phones,smartphones"
  tags VARCHAR(500)         -- "new,featured,sale"
);
```

**Problem:** Categories and tags stored as comma-separated strings violate 1NF (no atomic values).

**Recommended Schema:**
```sql
CREATE TABLE products (
  product_id INT PRIMARY KEY,
  name VARCHAR(100)
);

CREATE TABLE categories (
  category_id INT PRIMARY KEY,
  name VARCHAR(100)
);

CREATE TABLE product_categories (
  product_id INT REFERENCES products(product_id),
  category_id INT REFERENCES categories(category_id),
  PRIMARY KEY (product_id, category_id)
);

CREATE TABLE tags (
  tag_id INT PRIMARY KEY,
  name VARCHAR(50)
);

CREATE TABLE product_tags (
  product_id INT REFERENCES products(product_id),
  tag_id INT REFERENCES tags(tag_id),
  PRIMARY KEY (product_id, tag_id)
);
```

**Benefits:**
- Query categories/tags independently
- Add metadata to categories (description, parent_category)
- Prevent typos ("elecrtonics" vs "electronics")
- Enable category/tag analytics

---

**Related Prompts:**
- database_data_modeling_review.md - Entity relationship and data modeling analysis
- database_query_optimization.md - Query optimization and performance
- database_migration_strategy.md - Schema migration planning
- architecture_database_schema_review.md - Architecture-level schema review

**When to Use:**
Use this prompt when designing new database schemas, reviewing existing schemas for data quality issues, planning database refactoring, or conducting database audits. Particularly valuable before major application changes that affect data structures.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with specific analysis objective
- ST-02 (Structured Sequential Instructions) - Phased approach to analysis
- RT-02 (Multi-Dimensional Analysis Framework) - Multiple normalization levels
- RT-05 (Trade-off Analysis) - Denormalization cost-benefit assessment
- DS-06 (Prioritization and Severity Guidance) - Issue severity classification
- ST-03 (Output Format Templates) - Structured report format with examples
