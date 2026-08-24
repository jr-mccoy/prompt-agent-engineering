---
title: "Data Schema Draft from Requirements"
category: engineering-workflows/workflows
description: "Translate product requirements and user stories into a normalized database schema — entities, columns, typed relationships, constraints, and indexes — output as structured JSON with a coverage audit."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - database
  - schema-design
  - data-modeling
  - normalization
  - postgresql
updated: "2026-06-07"
related_prompts:
  - domain-engineering-workflows/tasks/task_sorting_algorithm_designer.md
  - domain-engineering-workflows/workflows/coding_problems_catalog.md
  - domain-engineering-workflows/improvement/improvement_best_practice_analysis.md
---

# Data Schema Draft from Requirements

**Objective:** Translate product requirements, user stories, or a feature brief into a properly normalized database schema — tables, columns, typed relationships, constraints, and indexes — returned as structured JSON with a coverage audit against the stated requirements.

**When to use:**
- Starting a new project or feature that needs data persistence.
- Converting a product brief into a concrete data model.
- Reviewing or refactoring an existing schema.
- Documenting data architecture for team alignment.

**When NOT to use:**
- Deep query/index performance tuning on a live DB — use a database performance prompt.
- API contract design (use an API design prompt) — though this pairs well with it.
- When requirements are too vague to identify entities (gather them first).

**Audience:** Backend engineers, data modelers, and tech leads designing a schema.

---

## Inputs / Context

The user supplies:
1. **Product brief / user stories** — wrap pasted requirements in a `<requirements>` tag.
2. **Known entities** (optional) — entities already identified.
3. **Business rules** — cardinality and integrity rules (e.g. "users can have multiple addresses").
4. **Scale & access pattern** (optional) — volumes, read/write ratio.
5. **Technical constraints** — target DB engine, soft deletes, multi-tenant, etc.

If a requirement is ambiguous about cardinality or ownership, state the assumption in the schema notes rather than guessing silently.

---

## Constraints

### Must
- Cover every entity implied by the requirements; flag any you inferred.
- Type every relationship (1:1, 1:N, M:N) and specify ON DELETE behavior for each FK.
- Choose appropriate data types (e.g. money as integer cents or DECIMAL, not FLOAT).
- Recommend indexes for FKs, unique keys, and stated query patterns — each with a reason.
- Output valid JSON matching the schema below, plus a coverage audit.

### Must Not
- Invent business rules, entities, or volumes the user didn't state — mark inferences as inferred.
- Store money as FLOAT, dates as strings, or arrays in violation of 1NF.
- Leave FKs without ON DELETE semantics.
- Claim a normalization form (e.g. 3NF) the schema doesn't actually satisfy.

---

## Your Input

**Product Brief:**
```markdown
[Paste your user stories, feature requirements, or product description here]
```

**Known Entities:** [Optional: List main data entities you've already identified]

**Business Rules:**
- [Rule 1: e.g., "Users can have multiple addresses"]
- [Rule 2: e.g., "Orders must have at least one line item"]
- [Rule 3: e.g., "Products belong to exactly one category"]

**Expected Scale:**
- Users: [estimated count]
- Records per day: [estimated volume]
- Read/Write ratio: [e.g., "80% reads, 20% writes"]

**Technical Constraints:** [e.g., "PostgreSQL", "must support soft deletes", "multi-tenant"]


**Instructions**

Design a database schema following these steps:

**Step 1: Entity Extraction**
Identify all entities from the product brief:
- Core entities (users, products, orders, etc.)
- Supporting entities (addresses, tags, categories)
- Junction/bridge entities for many-to-many relationships

**Step 2: Attribute Mapping**
For each entity, define:
- Primary key strategy (auto-increment, UUID, composite)
- Required vs optional fields
- Data types appropriate for the content
- Default values where applicable

**Step 3: Relationship Modeling**
Map relationships between entities:
- One-to-one (1:1)
- One-to-many (1:N)
- Many-to-many (M:N) with junction tables

**Step 4: Normalization Review**
Ensure schema follows normalization best practices:
- No repeating groups (1NF)
- No partial dependencies (2NF)
- No transitive dependencies (3NF)

**Step 5: Performance Optimization**
Recommend indexes based on:
- Primary key lookups
- Foreign key joins
- Frequent query patterns
- Unique constraints

**Step 6: Audit Verification**
Verify completeness:
- All entities from requirements are represented
- All relationships are typed and documented
- Critical business rules are enforceable


**Output Format**

Structure your response as JSON:

```json
{
  "schema_summary": {
    "total_tables": 0,
    "database": "postgresql|mysql|sqlite|etc",
    "normalization_form": "3NF"
  },
  "tables": [
    {
      "name": "table_name",
      "description": "What this table stores",
      "primary_key": "id",
      "columns": [
        {
          "field": "column_name",
          "type": "data_type",
          "nullable": false,
          "description": "What this column stores",
          "default": null,
          "constraints": ["UNIQUE", "CHECK (value > 0)"]
        }
      ],
      "relationships": [
        {
          "with_table": "other_table",
          "type": "1-many|many-1|many-many",
          "fk_field": "foreign_key_column",
          "on_delete": "CASCADE|SET NULL|RESTRICT"
        }
      ],
      "indexes": [
        {
          "columns": ["column1", "column2"],
          "type": "btree|hash|gin",
          "unique": false,
          "reason": "Why this index helps"
        }
      ]
    }
  ],
  "audit": {
    "all_entities_covered": true,
    "all_relationships_typed": true,
    "business_rules_enforced": ["rule1", "rule2"]
  }
}
```


## Example Output

```json
{
  "schema_summary": {
    "total_tables": 5,
    "database": "postgresql",
    "normalization_form": "3NF"
  },
  "tables": [
    {
      "name": "users",
      "description": "Application users who can place orders",
      "primary_key": "id",
      "columns": [
        {
          "field": "id",
          "type": "UUID",
          "nullable": false,
          "description": "Unique user identifier",
          "default": "gen_random_uuid()"
        },
        {
          "field": "email",
          "type": "VARCHAR(255)",
          "nullable": false,
          "description": "User's email address, used for login",
          "constraints": ["UNIQUE"]
        },
        {
          "field": "password_hash",
          "type": "VARCHAR(255)",
          "nullable": false,
          "description": "Bcrypt hashed password"
        },
        {
          "field": "full_name",
          "type": "VARCHAR(100)",
          "nullable": true,
          "description": "User's display name"
        },
        {
          "field": "created_at",
          "type": "TIMESTAMP WITH TIME ZONE",
          "nullable": false,
          "description": "Account creation timestamp",
          "default": "NOW()"
        },
        {
          "field": "deleted_at",
          "type": "TIMESTAMP WITH TIME ZONE",
          "nullable": true,
          "description": "Soft delete timestamp, NULL if active"
        }
      ],
      "relationships": [
        {
          "with_table": "orders",
          "type": "1-many",
          "fk_field": "user_id",
          "on_delete": "RESTRICT"
        },
        {
          "with_table": "addresses",
          "type": "1-many",
          "fk_field": "user_id",
          "on_delete": "CASCADE"
        }
      ],
      "indexes": [
        {
          "columns": ["email"],
          "type": "btree",
          "unique": true,
          "reason": "Fast lookup for authentication"
        },
        {
          "columns": ["deleted_at"],
          "type": "btree",
          "unique": false,
          "reason": "Filter active users efficiently"
        }
      ]
    },
    {
      "name": "products",
      "description": "Items available for purchase",
      "primary_key": "id",
      "columns": [
        {
          "field": "id",
          "type": "UUID",
          "nullable": false,
          "description": "Unique product identifier",
          "default": "gen_random_uuid()"
        },
        {
          "field": "sku",
          "type": "VARCHAR(50)",
          "nullable": false,
          "description": "Stock keeping unit",
          "constraints": ["UNIQUE"]
        },
        {
          "field": "name",
          "type": "VARCHAR(255)",
          "nullable": false,
          "description": "Product display name"
        },
        {
          "field": "description",
          "type": "TEXT",
          "nullable": true,
          "description": "Detailed product description"
        },
        {
          "field": "price_cents",
          "type": "INTEGER",
          "nullable": false,
          "description": "Price in cents to avoid floating point issues",
          "constraints": ["CHECK (price_cents >= 0)"]
        },
        {
          "field": "category_id",
          "type": "UUID",
          "nullable": false,
          "description": "Reference to product category"
        },
        {
          "field": "stock_quantity",
          "type": "INTEGER",
          "nullable": false,
          "description": "Current inventory count",
          "default": 0,
          "constraints": ["CHECK (stock_quantity >= 0)"]
        }
      ],
      "relationships": [
        {
          "with_table": "categories",
          "type": "many-1",
          "fk_field": "category_id",
          "on_delete": "RESTRICT"
        },
        {
          "with_table": "order_items",
          "type": "1-many",
          "fk_field": "product_id",
          "on_delete": "RESTRICT"
        }
      ],
      "indexes": [
        {
          "columns": ["sku"],
          "type": "btree",
          "unique": true,
          "reason": "Fast inventory lookups"
        },
        {
          "columns": ["category_id"],
          "type": "btree",
          "unique": false,
          "reason": "Filter products by category"
        }
      ]
    },
    {
      "name": "orders",
      "description": "Customer purchase orders",
      "primary_key": "id",
      "columns": [
        {
          "field": "id",
          "type": "UUID",
          "nullable": false,
          "description": "Unique order identifier"
        },
        {
          "field": "user_id",
          "type": "UUID",
          "nullable": false,
          "description": "Customer who placed the order"
        },
        {
          "field": "status",
          "type": "VARCHAR(20)",
          "nullable": false,
          "description": "Order status",
          "default": "'pending'",
          "constraints": ["CHECK (status IN ('pending', 'confirmed', 'shipped', 'delivered', 'cancelled'))"]
        },
        {
          "field": "total_cents",
          "type": "INTEGER",
          "nullable": false,
          "description": "Order total in cents"
        },
        {
          "field": "shipping_address_id",
          "type": "UUID",
          "nullable": false,
          "description": "Delivery address"
        },
        {
          "field": "created_at",
          "type": "TIMESTAMP WITH TIME ZONE",
          "nullable": false,
          "default": "NOW()"
        }
      ],
      "relationships": [
        {
          "with_table": "users",
          "type": "many-1",
          "fk_field": "user_id",
          "on_delete": "RESTRICT"
        },
        {
          "with_table": "order_items",
          "type": "1-many",
          "fk_field": "order_id",
          "on_delete": "CASCADE"
        },
        {
          "with_table": "addresses",
          "type": "many-1",
          "fk_field": "shipping_address_id",
          "on_delete": "RESTRICT"
        }
      ],
      "indexes": [
        {
          "columns": ["user_id", "created_at"],
          "type": "btree",
          "unique": false,
          "reason": "User order history queries"
        },
        {
          "columns": ["status"],
          "type": "btree",
          "unique": false,
          "reason": "Filter orders by status for fulfillment"
        }
      ]
    },
    {
      "name": "order_items",
      "description": "Line items within an order",
      "primary_key": "id",
      "columns": [
        {
          "field": "id",
          "type": "UUID",
          "nullable": false
        },
        {
          "field": "order_id",
          "type": "UUID",
          "nullable": false
        },
        {
          "field": "product_id",
          "type": "UUID",
          "nullable": false
        },
        {
          "field": "quantity",
          "type": "INTEGER",
          "nullable": false,
          "constraints": ["CHECK (quantity > 0)"]
        },
        {
          "field": "unit_price_cents",
          "type": "INTEGER",
          "nullable": false,
          "description": "Price at time of purchase (snapshot)"
        }
      ],
      "relationships": [
        {
          "with_table": "orders",
          "type": "many-1",
          "fk_field": "order_id",
          "on_delete": "CASCADE"
        },
        {
          "with_table": "products",
          "type": "many-1",
          "fk_field": "product_id",
          "on_delete": "RESTRICT"
        }
      ],
      "indexes": [
        {
          "columns": ["order_id"],
          "type": "btree",
          "unique": false,
          "reason": "Fetch all items for an order"
        }
      ]
    },
    {
      "name": "categories",
      "description": "Product categories for organization",
      "primary_key": "id",
      "columns": [
        {
          "field": "id",
          "type": "UUID",
          "nullable": false
        },
        {
          "field": "name",
          "type": "VARCHAR(100)",
          "nullable": false,
          "constraints": ["UNIQUE"]
        },
        {
          "field": "slug",
          "type": "VARCHAR(100)",
          "nullable": false,
          "constraints": ["UNIQUE"]
        },
        {
          "field": "parent_id",
          "type": "UUID",
          "nullable": true,
          "description": "Self-reference for category hierarchy"
        }
      ],
      "relationships": [
        {
          "with_table": "products",
          "type": "1-many",
          "fk_field": "category_id",
          "on_delete": "RESTRICT"
        },
        {
          "with_table": "categories",
          "type": "1-many",
          "fk_field": "parent_id",
          "on_delete": "SET NULL"
        }
      ],
      "indexes": [
        {
          "columns": ["slug"],
          "type": "btree",
          "unique": true,
          "reason": "URL-friendly category lookups"
        }
      ]
    }
  ],
  "audit": {
    "all_entities_covered": true,
    "all_relationships_typed": true,
    "business_rules_enforced": [
      "Users can have multiple addresses (1:N relationship)",
      "Orders must have at least one line item (application-level enforcement)",
      "Products belong to exactly one category (NOT NULL FK)"
    ]
  }
}
```


**Self-Audit Checklist:**
- [ ] At least 3 tables defined
- [ ] Every relationship has a type (1:1, 1:N, M:N)
- [ ] All foreign keys have ON DELETE behavior specified
- [ ] Primary keys defined for all tables
- [ ] Indexes recommended for foreign keys and frequent queries
- [ ] Business rules mapped to constraints where possible


**Common Schema Design Pitfalls:**

| Pitfall | Problem | Solution |
|---------|---------|----------|
| Storing money as FLOAT | Floating point errors | Use INTEGER cents or DECIMAL |
| No soft deletes | Can't recover deleted data | Add deleted_at timestamp |
| Missing timestamps | No audit trail | Include created_at, updated_at |
| Storing arrays | Violates 1NF | Create junction tables |
| VARCHAR without limit | Unbounded storage | Always specify max length |

---

## False-Positive Prevention

❌ **DON'T:**
- Don't invent entities, business rules, or data volumes the brief doesn't mention — mark anything you inferred as inferred.
- Don't store money as FLOAT, dates as strings, or arrays inline (1NF violation).
- Don't leave a foreign key without ON DELETE behavior.
- Don't label the schema "3NF" unless it actually has no transitive dependencies.

✅ **DO:**
- Map each table back to a requirement; flag inferred entities.
- Type every relationship and specify ON DELETE.
- Justify every index with a query/lookup reason.
- State assumptions for any ambiguous cardinality or ownership.

---

## Verification

- [ ] Every entity from the requirements is represented; inferences flagged.
- [ ] All relationships typed (1:1, 1:N, M:N) with ON DELETE behavior.
- [ ] Primary keys on all tables; data types appropriate (money/date handling correct).
- [ ] Indexes recommended for FKs and stated query patterns, each with a reason.
- [ ] Business rules mapped to constraints where enforceable.
- [ ] Output is valid JSON; coverage audit included.
- [ ] No fabricated rules/entities/volumes; normalization claim is accurate.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the requirements-to-schema goal.
- **ST-02 (Structured Sequential Instructions):** Entities → attributes → relationships → normalization → indexes → audit.
- **RT-02 (Multi-Dimensional Analysis):** Balances correctness, normalization, integrity, and performance.
- **DS-02 (Structured Output Schema):** Locks the JSON schema for tables, relationships, and indexes.
- **QA-01 (Self-Verification):** Coverage audit and pre-report check guard against gaps and fabrication.

---

## Related Prompts

- `domain-engineering-workflows/tasks/task_sorting_algorithm_designer.md` — Design algorithms over the entities you model.
- `domain-engineering-workflows/workflows/coding_problems_catalog.md` — Reference database/architecture defect taxonomy.
- `domain-engineering-workflows/improvement/improvement_best_practice_analysis.md` — Audit the implementation built on this schema.
