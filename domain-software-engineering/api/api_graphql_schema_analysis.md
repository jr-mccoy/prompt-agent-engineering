---
title: "GraphQL Schema Analysis"
category: api-design
description: "type Query {"
tags:
  - analysis
  - api-design
updated: "2026-03-19"
---

# GraphQL Schema Analysis

**Objective:** Analyze GraphQL schemas for design quality, performance implications, security vulnerabilities, and adherence to best practices to produce efficient, secure, and maintainable GraphQL APIs.

**When to Use:** Use this prompt when designing new GraphQL schemas, reviewing existing schemas before release, optimizing query performance, auditing for security issues, or standardizing schema conventions across teams.

**Instructions:**

1. **Analyze Schema Structure**
   - Evaluate type naming conventions (PascalCase for types, camelCase for fields)
   - Check for proper nullability definitions
   - Assess interface and union type usage
   - Review enum definitions and naming
   - Identify circular reference patterns
   - Evaluate custom scalar usage

2. **Review Query Design**
   - Analyze root query field organization
   - Check for N+1 query vulnerabilities
   - Assess connection/pagination patterns (Relay-style cursors)
   - Review filtering and sorting argument design
   - Evaluate query complexity and depth
   - Check for appropriate use of fragments

3. **Evaluate Mutation Design**
   - Check input type patterns (Input suffix convention)
   - Analyze mutation payload design
   - Review error handling patterns
   - Assess optimistic update support
   - Evaluate bulk operation mutations
   - Check for idempotency patterns

4. **Subscription Analysis**
   - Review subscription event naming
   - Assess real-time data patterns
   - Check for subscription payload efficiency
   - Evaluate connection management considerations
   - Review authorization in subscriptions

5. **Performance Assessment**
   - Identify potential N+1 query patterns
   - Check for DataLoader opportunities
   - Analyze field resolver complexity
   - Review query depth and complexity limits
   - Assess batching and caching strategies
   - Evaluate persisted queries usage

6. **Security Review**
   - Check for introspection exposure in production
   - Review field-level authorization
   - Assess query depth limiting
   - Evaluate rate limiting by complexity
   - Check for sensitive data exposure
   - Review input validation completeness

7. **Schema Evolution**
   - Assess deprecation usage and communication
   - Review breaking change risks
   - Check for additive-only changes
   - Evaluate versioning strategy (if any)
   - Review schema stitching/federation patterns

**Expected Output:** A comprehensive GraphQL schema analysis report including:
- Schema quality score (1-10)
- Type diagram or summary
- Performance vulnerability assessment
- Security audit results
- Specific recommendations with code examples
- Schema evolution readiness evaluation

**Example Output:**

```markdown
## GraphQL Schema Analysis Report

### Summary
- **Schema Name**: E-Commerce Product API
- **Types Analyzed**: 47 (23 Object, 12 Input, 8 Enum, 4 Interface)
- **Schema Quality Score**: 7.5/10
- **Critical Issues**: 3
- **Performance Risks**: 5
- **Security Issues**: 2

### Type Structure Overview

```graphql
# Core Types Identified
type Query {
  products(filter: ProductFilter, pagination: PaginationInput): ProductConnection!
  product(id: ID!): Product
  categories: [Category!]!  # Issue: Unbounded list
  # ... 12 more root queries
}

type Mutation {
  createProduct(input: CreateProductInput!): CreateProductPayload!
  updateProduct(id: ID!, input: UpdateProductInput!): UpdateProductPayload!
  # ... 8 more mutations
}

type Subscription {
  productUpdated(productId: ID!): Product!
  inventoryChanged: InventoryEvent!
}
```

### Critical Issues

#### Issue 1: N+1 Query Vulnerability (HIGH)
**Location**: `Product.reviews` field
**Problem**: Reviews resolved individually per product without batching

**Current Schema**:
```graphql
type Product {
  id: ID!
  name: String!
  reviews: [Review!]!  # Resolves N queries for N products
}
```

**Current Resolver** (problematic):
```javascript
Product: {
  reviews: (product) => db.reviews.findByProductId(product.id)
}
```

**Recommended Solution**:
```javascript
// Use DataLoader for batching
const reviewLoader = new DataLoader(async (productIds) => {
  const reviews = await db.reviews.findByProductIds(productIds);
  return productIds.map(id => reviews.filter(r => r.productId === id));
});

Product: {
  reviews: (product, _, { loaders }) => loaders.review.load(product.id)
}
```

**Impact**: Without fix, querying 100 products = 101 database queries. With DataLoader = 2 queries.

#### Issue 2: Missing Query Depth Limiting (HIGH)
**Problem**: No protection against deeply nested queries

**Malicious Query Example**:
```graphql
query DeepNest {
  products {
    edges {
      node {
        category {
          products {
            edges {
              node {
                category {
                  products {  # Continues infinitely
                    ...
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

**Recommended Solution**:
```javascript
import depthLimit from 'graphql-depth-limit';

const server = new ApolloServer({
  schema,
  validationRules: [depthLimit(7)],
  plugins: [
    ApolloServerPluginLandingPageDisabled(),  // Disable introspection in prod
  ],
});
```

#### Issue 3: Unbounded List Returns (HIGH)
**Location**: `Query.categories`, `Product.variants`
**Problem**: Lists without pagination can return unlimited data

**Current**:
```graphql
type Query {
  categories: [Category!]!  # Could return 10,000 categories
}

type Product {
  variants: [ProductVariant!]!  # Unbounded
}
```

**Recommended**:
```graphql
type Query {
  categories(first: Int = 20, after: String): CategoryConnection!
}

type Product {
  variants(first: Int = 10): [ProductVariant!]!  # Limited with default
}
```

### Performance Analysis

| Pattern | Status | Impact | Recommendation |
|---------|--------|--------|----------------|
| DataLoader Usage | MISSING | High | Implement for all list relations |
| Query Complexity | MISSING | High | Add complexity analysis (max: 1000) |
| Persisted Queries | MISSING | Medium | Implement for production |
| Response Caching | PARTIAL | Medium | Add cache hints to stable fields |
| Batch Mutations | MISSING | Low | Add bulk create/update mutations |

### Query Complexity Analysis

**Most Complex Queries Identified**:
```
1. products + reviews + author + products → Complexity: ~2,500 (HIGH)
2. orders + items + product + category → Complexity: ~1,800 (MEDIUM)
3. user + orders + items → Complexity: ~900 (OK)
```

**Recommended Complexity Limits**:
```javascript
const complexityPlugin = createComplexityPlugin({
  schema,
  maximumComplexity: 1000,
  estimators: [
    fieldExtensionsEstimator(),
    simpleEstimator({ defaultComplexity: 1 }),
  ],
  onComplete: (complexity) => {
    console.log('Query Complexity:', complexity);
  },
});
```

### Security Audit

| Check | Status | Finding |
|-------|--------|---------|
| Introspection Disabled (Prod) | FAIL | Introspection enabled in all environments |
| Query Depth Limit | FAIL | No depth limiting configured |
| Complexity Limit | FAIL | No complexity analysis |
| Field Authorization | WARN | 5 fields missing auth checks |
| Input Validation | PASS | All inputs properly validated |
| Rate Limiting | PASS | Implemented at gateway level |

**Field Authorization Issues**:
```graphql
type User {
  email: String!        # OK - has @auth directive
  orders: [Order!]!     # OK - filtered by user context
  internalNotes: String # MISSING - no auth, sensitive data
  adminFlags: [String!] # MISSING - admin-only field exposed
}
```

### Schema Design Best Practices

#### Naming Convention Compliance
| Convention | Status | Examples |
|------------|--------|----------|
| PascalCase Types | PASS | `Product`, `OrderItem` |
| camelCase Fields | PASS | `createdAt`, `totalPrice` |
| Input Type Suffix | WARN | `ProductInput` should be `CreateProductInput` |
| Payload Type Suffix | PASS | `CreateProductPayload` |
| SCREAMING_SNAKE Enums | FAIL | Using `pending` instead of `PENDING` |

#### Nullability Assessment
```graphql
# Good: Explicit nullability
type Product {
  id: ID!                    # Never null
  name: String!              # Required
  description: String        # Optional (nullable)
  price: Money!              # Required complex type
}

# Issue Found: Inconsistent nullability
type Order {
  items: [OrderItem!]!       # Good: Non-null list of non-null items
  notes: [String]            # Issue: Nullable list AND nullable items
  # Should be: notes: [String!]! or notes: [String!] depending on intent
}
```

### Mutation Design Review

**Good Patterns Found**:
```graphql
# Proper Input/Payload pattern
mutation CreateProduct($input: CreateProductInput!) {
  createProduct(input: $input) {
    product {
      id
      name
    }
    errors {
      field
      message
    }
  }
}
```

**Issues Found**:
```graphql
# Issue: Multiple arguments instead of input type
mutation UpdateProduct($id: ID!, $name: String, $price: Int, $description: String) {
  updateProduct(id: $id, name: $name, price: $price, description: $description) {
    ...
  }
}

# Should be:
mutation UpdateProduct($id: ID!, $input: UpdateProductInput!) {
  updateProduct(id: $id, input: $input) {
    ...
  }
}
```

### Relay Compliance (Connection Specification)

| Requirement | Status | Notes |
|-------------|--------|-------|
| Node Interface | PASS | All entities implement Node |
| Connection Types | PARTIAL | 3 lists missing connection pattern |
| Edge Types | PASS | Proper edge implementation |
| PageInfo | PASS | Complete pageInfo fields |
| Cursor-based | PASS | Using opaque cursors |

### Action Plan

| Priority | Action | Effort | Impact |
|----------|--------|--------|--------|
| 1 | Implement DataLoader for all relations | Medium | High |
| 2 | Add query depth limit (max: 7) | Small | High |
| 3 | Add query complexity analysis | Medium | High |
| 4 | Disable introspection in production | Small | High |
| 5 | Add field-level authorization | Medium | High |
| 6 | Convert unbounded lists to connections | Medium | Medium |
| 7 | Standardize enum naming (SCREAMING_SNAKE) | Small | Low |
| 8 | Add persisted queries | Medium | Medium |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- DS-06 (Prioritization and Severity Guidance)
- RT-05 (Evidence-Based Reasoning)
- DS-03 (Technology-Specific Guidance)

**Related Prompts:**
- api_rest_design_review.md - For REST API design review
- api_versioning_strategy.md - For API versioning decisions
- api_openapi_documentation.md - For API documentation generation
- code-analysis/performance/performance_bottleneck_identification.md - For resolver performance
- code-analysis/security/security_api_security_testing.md - For API security testing

**Customization Guide:**
- **For Relay-Compliant Schemas**: Emphasize connection specification compliance, Node interface
- **For Apollo Federation**: Add federation directive review, entity resolution analysis
- **For Schema Stitching**: Focus on type conflicts, schema composition patterns
- **For Real-Time Heavy Apps**: Increase emphasis on subscription design, connection management
- **For Mobile Clients**: Focus on query complexity, field selection, offline support patterns


---

## Must / Must Not

**Must:**
- Cite the exact type, field, or directive in every finding (e.g., `type User.friends: [User!]!`).
- Classify findings by axis: **Design** (schema shape), **Performance** (N+1, complexity), **Security** (auth/AuthZ at field level), **Evolution** (breaking-change risk).
- Differentiate **federated / Apollo Federation** schemas from **monolithic** schemas — the analysis rules differ.
- Use severity: **Critical** (breaks clients or exposes data), **Major** (perf/maint issue), **Minor**, **Nit**.

**Must Not:**
- Recommend breaking changes to a production schema without a deprecation path (`@deprecated` directive).
- Flag nullability as wrong without considering whether the field represents "absent", "unknown", or "error" — all legitimate distinctions.
- Apply REST anti-patterns as GraphQL rules (e.g., "no nested mutations" — GraphQL allows them).
- Recommend complexity caps / depth limits without examining actual client query patterns first.
- Rewrite a Relay-compliant schema unless told the team is leaving the Relay spec.

## Verification (Self-Check)

Before emitting findings:

1. **Federation vs monolith identified** — State which, and scope recommendations accordingly.
2. **Resolver impact traced** — For every performance finding, trace to the resolver and any DataLoader / N+1 risk.
3. **Backward-compatibility check** — Every schema change is classified as **Breaking**, **Non-Breaking**, or **Additive**.
4. **Subscription-lifecycle issues flagged separately** — they have different semantics from queries/mutations.
5. **Confidence marked** per finding (High / Medium / Low).

## False-Positive Prevention

Rule out:

- **"Over-fetching"** — GraphQL's selling point is client-chosen shape; this is a CLIENT concern, not a schema one. Only flag if schema FORCES over-fetching.
- **"Should be non-null"** — Non-null on output type means errors bubble up and can cascade; nullable is often safer for schema evolution.
- **"Missing @deprecated"** — Only needed when replacing a field, not for every optional field.
- **"Complexity too high"** — Need actual query complexity examples; a theoretical 100-depth query may never happen in practice.
- **"Should be an interface"** — Interfaces add resolution cost; only recommend when 2+ concrete types actually share the shape.

If you did not inspect resolver code, mark all performance findings as **Medium** confidence maximum.
