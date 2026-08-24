---
title: "Database Data Modeling Review"
category: code-analysis/database
description: "Review data models for correctness, completeness, and alignment with business requirements"
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
  - data-modeling
  - entity-relationship
  - schema-design
  - domain-modeling
updated: "2026-01-15"
---

# Database Data Modeling Review

**Objective:** Review database data models (entity-relationship diagrams, schema definitions, or domain models) to verify they accurately represent business requirements, follow modeling best practices, and support intended use cases without unnecessary complexity or missing elements.

---

## Instructions

### Phase 1: Requirements Alignment Analysis

1. **Document business requirements:**
   - What business domain does this model represent?
   - What are the key business entities?
   - What relationships exist between entities?
   - What business rules must be enforced?
   - What queries and reports are needed?

2. **Identify key use cases:**
   - CRUD operations for each entity
   - Complex queries and aggregations
   - Reporting requirements
   - Integration points with other systems
   - Historical/audit requirements

3. **Map requirements to model elements:**
   - Does each business entity have a corresponding table?
   - Are all required attributes captured?
   - Are relationships correctly represented?
   - Are business rules enforceable at the database level?

---

### Phase 2: Entity Analysis

For each entity (table) in the model:

1. **Entity identification correctness:**
   - Does this represent a distinct business concept?
   - Is the entity appropriately scoped (not too broad/narrow)?
   - Is the naming clear and consistent?

2. **Primary key analysis:**
   ```
   Good primary keys:
   ✓ Immutable (never changes)
   ✓ Unique (guaranteed)
   ✓ Not null
   ✓ Simple (single column preferred)
   ✓ Meaningless (no business meaning)

   Problematic primary keys:
   ✗ Natural keys that may change (email, SSN)
   ✗ Composite keys when simple surrogate works
   ✗ Business identifiers that may be reused
   ```

3. **Attribute analysis:**
   - Are all required attributes present?
   - Are data types appropriate?
   - Are there missing constraints (NOT NULL, CHECK)?
   - Are there redundant/derived attributes?
   - Is sensitive data identified?

4. **Entity completeness:**
   - Missing common attributes:
     - Created timestamp
     - Updated timestamp
     - Soft delete flag (if applicable)
     - Version/revision number (if optimistic locking)
     - Created by / Updated by (if auditing)

---

### Phase 3: Relationship Analysis

1. **Relationship identification:**
   - Are all business relationships represented?
   - Is the cardinality correct (1:1, 1:N, M:N)?
   - Is optionality correct (required vs. optional)?

2. **One-to-One relationships:**
   ```
   Questions to ask:
   - Should these be merged into one table?
   - Is there a valid reason for separation?
     (Different access patterns, security, optional data)
   - Which side should have the foreign key?
   ```

3. **One-to-Many relationships:**
   ```
   Verify:
   - Foreign key is on the "many" side
   - Appropriate ON DELETE behavior
   - Index on foreign key column
   - Correct nullability
   ```

4. **Many-to-Many relationships:**
   ```
   Verify:
   - Junction table exists
   - Junction table has appropriate primary key
   - Additional attributes on the relationship (if needed)
   - Indexes for both foreign keys
   ```

5. **Self-referencing relationships:**
   ```
   Examples:
   - Employee → Manager (same table)
   - Category → Parent Category
   - Comment → Reply To Comment

   Verify:
   - Cycle prevention (if needed)
   - Appropriate handling of root elements
   - Query patterns for hierarchical data
   ```

---

### Phase 4: Business Rule Representation

1. **Constraint analysis:**
   - Are business rules enforceable at database level?
   - Are there missing unique constraints?
   - Are there missing check constraints?
   - Are foreign keys properly defined?

2. **Example business rules to check:**
   ```sql
   -- Price must be positive
   CONSTRAINT chk_positive_price CHECK (price > 0)

   -- End date must be after start date
   CONSTRAINT chk_date_order CHECK (end_date > start_date)

   -- Status must be from allowed values
   CONSTRAINT chk_valid_status CHECK (status IN ('pending', 'active', 'completed'))

   -- Email must be unique per organization
   CONSTRAINT uq_org_email UNIQUE (organization_id, email)
   ```

3. **Rules that may need application enforcement:**
   - Cross-table validations
   - Complex conditional logic
   - Time-dependent rules
   - Rules requiring external data

---

### Phase 5: Data Type Review

1. **String types:**
   ```
   Considerations:
   - VARCHAR vs TEXT vs CHAR
   - Maximum length requirements
   - Character set (UTF-8 for international)
   - Collation for sorting/comparison
   ```

2. **Numeric types:**
   ```
   Considerations:
   - INTEGER vs BIGINT (growth projection)
   - DECIMAL vs FLOAT (precision requirements)
   - Appropriate precision/scale for money
   - Unsigned when negative values impossible
   ```

3. **Date/Time types:**
   ```
   Considerations:
   - DATE vs DATETIME vs TIMESTAMP
   - Timezone handling (store in UTC?)
   - Precision needed (seconds vs milliseconds)
   - TIMESTAMP WITH TIME ZONE for user-facing dates
   ```

4. **Other types:**
   ```
   Consider specialized types:
   - UUID for distributed IDs
   - JSONB for flexible attributes
   - ENUM for fixed value sets
   - ARRAY for simple lists (PostgreSQL)
   - Spatial types for geographic data
   ```

---

### Phase 6: Naming Convention Review

1. **Table naming:**
   ```
   Consistent pattern:
   - Singular vs plural (users vs user)
   - snake_case vs PascalCase
   - Prefix conventions (tbl_, none)

   Good: orders, order_items, user_preferences
   Bad: tblOrder, OrderItems, user_prefs
   ```

2. **Column naming:**
   ```
   Consistent pattern:
   - snake_case preferred for SQL
   - Clear, descriptive names
   - Consistent suffixes (_id, _at, _count)

   Good: created_at, user_id, order_total
   Bad: createdAt, UserId, tot
   ```

3. **Foreign key naming:**
   ```
   Pattern: {referenced_table}_id

   Good: user_id, order_id, category_id
   Bad: user, fk_user, user_fk
   ```

4. **Index naming:**
   ```
   Pattern: idx_{table}_{columns}

   Good: idx_orders_user_id, idx_products_category_price
   Bad: index1, orders_idx
   ```

5. **Constraint naming:**
   ```
   Patterns:
   - pk_{table} for primary keys
   - fk_{table}_{referenced_table} for foreign keys
   - uq_{table}_{columns} for unique constraints
   - chk_{table}_{description} for check constraints
   ```

---

### Phase 7: Query Support Analysis

1. **Common query patterns:**
   - Can key queries be executed efficiently?
   - Are necessary indexes suggested?
   - Are joins straightforward?

2. **Reporting requirements:**
   - Are aggregations possible without complex queries?
   - Is denormalization needed for reporting?
   - Should a separate reporting model exist?

3. **Search requirements:**
   - Full-text search needed?
   - Faceted search support?
   - Geographic search support?

---

### Phase 8: Special Considerations

1. **Audit and history:**
   ```
   Options:
   - Timestamp columns (created_at, updated_at)
   - Soft deletes (deleted_at)
   - History tables (entity_history)
   - Change data capture (CDC)
   - Event sourcing
   ```

2. **Multi-tenancy:**
   ```
   Options:
   - Shared schema with tenant_id column
   - Schema per tenant
   - Database per tenant

   Verify tenant isolation in model if applicable
   ```

3. **Internationalization:**
   ```
   Considerations:
   - Translation tables for localized content
   - Character encoding
   - Date/time/currency formatting (application concern)
   ```

4. **Soft deletes vs hard deletes:**
   ```
   Soft delete pattern:
   - deleted_at TIMESTAMP NULL
   - Filter in queries: WHERE deleted_at IS NULL
   - Consider impact on unique constraints
   ```

---

### Phase 9: CRITICAL - Context-Aware Review

**Before flagging issues:**

1. **Consider the application context:**
   - Is this an OLTP or OLAP system?
   - What's the expected data volume?
   - What's the team's experience level?
   - Are there framework constraints (ORM requirements)?

2. **Validate against actual requirements:**
   - Is the "missing" element actually needed?
   - Is the "redundancy" intentional for performance?
   - Are there external constraints driving decisions?

3. **Avoid over-modeling:**
   - Is every entity necessary?
   - Are there premature abstractions?
   - Is flexibility justified by requirements?

**Do NOT flag:**
- Intentional denormalization with clear purpose
- ORM-required patterns (e.g., single-table inheritance)
- Domain-specific modeling conventions
- Appropriate trade-offs for the use case

---

## Expected Output: Data Model Review Report

### Executive Summary
- Overall model quality: [Good/Needs Improvement/Significant Issues]
- Requirements coverage: [Complete/Partial/Incomplete]
- Number of issues found: [N]
- Critical issues: [N]

### Model Overview

| Entity | Attributes | Relationships | Purpose |
|--------|------------|---------------|---------|
| users | 12 | 3 | User account management |
| orders | 15 | 4 | Purchase transactions |

### Requirements Mapping

| Requirement | Model Element | Status |
|-------------|---------------|--------|
| Store customer data | users table | ✓ Complete |
| Track order history | orders, order_items | ✓ Complete |
| Support discount codes | - | ✗ Missing |

### Entity Review

#### Entity: [name]

**Purpose:** [Description]

**Attributes:**
| Column | Type | Constraints | Assessment |
|--------|------|-------------|------------|
| id | BIGINT | PK | ✓ Good |
| email | VARCHAR(255) | NOT NULL, UNIQUE | ✓ Good |
| status | VARCHAR(50) | | ⚠ Add CHECK constraint |

**Issues:**
1. [Issue description]
2. [Issue description]

**Recommendations:**
1. [Recommendation]
2. [Recommendation]

### Relationship Review

| Relationship | Type | Assessment |
|--------------|------|------------|
| users → orders | 1:N | ✓ Correct |
| orders ↔ products | M:N | ⚠ Missing junction attributes |

### Missing Elements

| Element | Impact | Recommendation |
|---------|--------|----------------|
| Audit timestamps | Medium | Add created_at, updated_at |
| Discount codes | High | Create discount_codes table |

### Naming Issues

| Current | Recommended | Reason |
|---------|-------------|--------|
| tblUser | users | Remove prefix, use plural |
| createdDate | created_at | Use snake_case and _at suffix |

### Business Rules Representation

| Rule | Enforced | How |
|------|----------|-----|
| Price > 0 | No | Add CHECK constraint |
| Unique email | Yes | UNIQUE constraint |

### Suggested Schema Changes

```sql
-- Add missing audit columns
ALTER TABLE orders
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

-- Add missing constraint
ALTER TABLE products
ADD CONSTRAINT chk_positive_price CHECK (price > 0);

-- Create missing table
CREATE TABLE discount_codes (
  code_id SERIAL PRIMARY KEY,
  code VARCHAR(50) UNIQUE NOT NULL,
  discount_percent DECIMAL(5,2) CHECK (discount_percent BETWEEN 0 AND 100),
  valid_from DATE NOT NULL,
  valid_until DATE NOT NULL,
  CHECK (valid_until > valid_from)
);
```

### Entity-Relationship Diagram (if generating)

```
[ASCII ER diagram or description]

┌──────────────┐       ┌──────────────┐
│    users     │       │   orders     │
├──────────────┤       ├──────────────┤
│ id (PK)      │───1:N─│ id (PK)      │
│ email        │       │ user_id (FK) │
│ name         │       │ total        │
│ created_at   │       │ status       │
└──────────────┘       └──────────────┘
```

---

## Example: E-commerce Data Model Review Finding

### Finding: Missing Order Status Audit Trail

**Entity:** orders
**Issue:** Status changes are overwritten without history

**Current Model:**
```sql
CREATE TABLE orders (
  order_id SERIAL PRIMARY KEY,
  status VARCHAR(20) NOT NULL  -- Only current status stored
);
```

**Problem:**
- Cannot track when status changed
- Cannot see previous statuses
- Compliance and debugging difficulty

**Recommended Model:**
```sql
CREATE TABLE orders (
  order_id SERIAL PRIMARY KEY,
  current_status VARCHAR(20) NOT NULL
);

CREATE TABLE order_status_history (
  history_id SERIAL PRIMARY KEY,
  order_id INT REFERENCES orders(order_id),
  status VARCHAR(20) NOT NULL,
  changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  changed_by INT REFERENCES users(user_id),
  notes TEXT
);

-- Index for efficient queries
CREATE INDEX idx_order_status_history_order
ON order_status_history(order_id, changed_at DESC);
```

**Trade-off:**
- Additional table and writes
- More complex queries for current status
- Full audit capability

---

**Related Prompts:**
- database_schema_design_normalization.md - Normalization analysis
- database_query_optimization.md - Query efficiency considerations
- architecture_database_schema_review.md - Architecture-level review
- business_model_canvas_analysis.md - Business requirements context

**When to Use:**
Use this prompt when reviewing data models before implementation, during design reviews, when onboarding to existing systems, or when planning schema refactoring. Essential for greenfield projects and major feature additions.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Model review objective
- ST-02 (Structured Sequential Instructions) - Systematic review phases
- RT-02 (Multi-Dimensional Analysis Framework) - Multiple review dimensions
- RT-05 (Trade-off Analysis) - Design decision evaluation
- DS-06 (Prioritization and Severity Guidance) - Issue classification
- ST-03 (Output Format Templates) - Structured review report
