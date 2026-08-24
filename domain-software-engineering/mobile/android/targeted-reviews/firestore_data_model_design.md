---
title: "Firestore Data Model Design"
category: mobile-development
description: "Design a Firestore NoSQL data model from requirements — denormalization strategy, subcollection vs root collection decisions, document size limits, query patterns, composite index planning, and cost-per-query estimation"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-03
  - CM-01
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - android
  - firebase
  - firestore
  - data-modeling
  - nosql
  - mobile-development
  - solo-developer
updated: "2026-02-11"
---

# Firestore Data Model Design

**Objective:** Design a production-grade Firestore NoSQL data model from application requirements — covering denormalization strategy, subcollection vs. root collection decisions, document size constraints, query pattern mapping, composite index planning, and cost-per-query estimation — producing a data model specification that balances read performance, write simplicity, and cost efficiency.

**When to Use:** Use this prompt when starting a new Firebase project, when adding major features that require new data structures, when experiencing performance or cost issues with an existing model, or when migrating from SQL to Firestore. Critical to get right early because Firestore data model decisions are expensive to change later — a bad model means high costs, slow queries, and eventual rewrites.

**Important context:** Firestore is NOT a relational database. The biggest mistake developers make is trying to normalize data like SQL. Firestore rewards denormalization, embedding, and designing your data around your queries — not around entities. This prompt teaches these principles while designing your specific model.

---

## Context Gathering

Before designing the data model, gather essential context:

1. **Application Requirements:**
   - "What are the core entities in your app (users, posts, products, orders, etc.)?"
   - "What are the relationships between entities (one-to-many, many-to-many)?"
   - "What are the 5-10 most important queries your app needs to perform?"
   - "Which queries run on app startup or on frequently visited screens?"

2. **Access Patterns:**
   - "What data is read most frequently vs. written most frequently?"
   - "Do you need real-time listeners or are one-time reads sufficient?"
   - "Do any queries need to combine data from multiple entities?"
   - "Do you need full-text search or complex filtering?"

3. **Scale Expectations:**
   - "How many users do you expect (now and in 12 months)?"
   - "How many documents per collection (orders, messages, products)?"
   - "What is the expected read-to-write ratio?"
   - "Are there any collections that could grow unbounded?"

4. **Current State:**
   - "Is this a new project or refactoring an existing data model?"
   - "If existing, what problems are you experiencing (slow queries, high costs, complex client logic)?"
   - "Are you using any Firebase services beyond Firestore (Auth, Functions, Storage)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before designing ANY data model, you MUST:**

1. **Understand the query patterns first** — In Firestore, you design data to serve queries, not the other way around. List all required queries before proposing a single collection.
2. **Know the hard limits** — Maximum document size is 1 MiB. Maximum write rate to a single document is 1 write/second. Maximum subcollection depth is 100. These are not guidelines — they are hard limits.
3. **Consider the billing impact** — Every document read costs money. A model that requires reading 10 documents where 1 would suffice costs 10x more. Always estimate cost-per-query.
4. **Check if Firestore is the right choice** — Some data patterns (complex joins, full-text search, heavy aggregations) are better served by other services. Don't force relational patterns into a document database.
5. **Validate with real query examples** — For each collection design, show the exact Firestore query code that would execute against it.

### False-Positive Prevention

- ❌ Do NOT blindly normalize data like a SQL database — this causes expensive multi-document reads
- ❌ Do NOT recommend subcollections for data that is always fetched together with the parent — embed it instead
- ❌ Do NOT assume all denormalization is good — duplicated data requires consistent updates
- ❌ Do NOT design collections without considering index requirements and costs
- ❌ Do NOT recommend collection group queries without noting they require composite indexes
- ✅ DO design around the actual query patterns the app needs
- ✅ DO calculate the document read count for each common query path
- ✅ DO consider the update complexity when recommending denormalization
- ✅ DO note when a query pattern suggests a different database might be more appropriate
- ✅ DO provide the exact Firestore query code for each collection design

---

### Phase 1: Query Pattern Analysis

Before designing any collections, catalog every query the app needs.

#### 1.1 Query Inventory

For each screen or feature, document the data queries:

```
Screen/Feature: [Name]
Frequency: [Every app open / Daily / Occasionally]
Query: "[Natural language description]"
Required Fields: [List fields needed in the result]
Filter/Sort: [Any where/orderBy conditions]
Real-time: [Yes/No — does this need a live listener?]
Expected Result Count: [1 / Few / Many / Unbounded]
```

#### 1.2 Query Priority Classification

| Priority | Criteria | Design Impact |
|----------|----------|--------------|
| **P0 — Critical Path** | Runs on app startup or main screen | Must be 1 document read if possible |
| **P1 — Frequent** | Runs multiple times per session | Minimize document reads, consider caching |
| **P2 — Occasional** | Feature-specific, user-initiated | Acceptable to read multiple documents |
| **P3 — Rare** | Admin, analytics, background | Can use Cloud Functions or BigQuery |

#### 1.3 Relationship Mapping

For each entity relationship, classify:

| Relationship | Type | Size | Query Direction | Recommendation |
|-------------|------|------|-----------------|----------------|
| User → Posts | One-to-Many | Unbounded | User's posts, Single post | Subcollection or root collection |
| Post → Comments | One-to-Many | Unbounded | Post's comments | Subcollection |
| User → Settings | One-to-One | Fixed | Always with user | Embed in user document |
| Post → Tags | Many-to-Many | Small (< 20) | Posts by tag, Tags on post | Array in document + collection group |
| User → User (followers) | Many-to-Many | Large | User's followers, Following | Separate collection with composite key |

---

### Phase 2: Collection Design

#### 2.1 Design Principles

Follow these Firestore-specific design principles:

**Principle 1: Design for reads, not writes.**
Firestore reads are frequent; writes are occasional. Optimize read patterns even if it means more complex writes.

**Principle 2: Embed data that is always fetched together.**
If you always show a user's display name with their post, store the display name IN the post document — don't fetch the user document separately.

**Principle 3: Use subcollections for unbounded one-to-many relationships.**
A user can have thousands of posts. Don't store them as an array in the user document — use a subcollection.

**Principle 4: Duplicate data to avoid joins.**
Firestore has no joins. If a query needs data from two "tables," duplicate the needed fields into one collection. Accept the update cost.

**Principle 5: Arrays for small, bounded lists; subcollections for large or growing lists.**
Tags (< 20) → Array. Comments (unbounded) → Subcollection.

#### 2.2 Collection Specification Template

For each collection, document:

```markdown
### Collection: `[name]`

**Purpose:** [What this collection stores]
**Document ID strategy:** [Auto-generated / User UID / Custom composite]
**Expected document count:** [Range]
**Write frequency:** [Per document]
**Read frequency:** [Per document]

**Document schema:**
```json
{
  "field1": "string — [description]",
  "field2": "number — [description]",
  "field3": "timestamp — [description]",
  "field4": "map — [description]",
  "embeddedData": {
    "denormalizedField": "string — [from Collection X, updated via Cloud Function]"
  },
  "tags": ["string array — max 20 items"],
  "createdAt": "timestamp",
  "updatedAt": "timestamp"
}
```

**Subcollections:**
- `[subcollection name]` — [purpose, expected size]

**Required indexes:**
- Composite: `field1 ASC, createdAt DESC` — for [query description]
- Collection group: `[if needed]` — for [query description]

**Security rules summary:**
- Read: [Who can read]
- Create: [Who can create]
- Update: [Who can update, which fields]
- Delete: [Who can delete]

**Queries served:**
| Query | Fields Used | Estimated Reads | Cost/1000 Queries |
|-------|------------|-----------------|-------------------|
| [Q1] | [fields] | [count] | $[amount] |
| [Q2] | [fields] | [count] | $[amount] |
```

#### 2.3 Denormalization Decision Framework

For each piece of data that appears in multiple places:

| Data | Source | Duplicated To | Update Frequency | Update Mechanism | Worth It? |
|------|--------|--------------|-----------------|-----------------|-----------|
| User display name | `users/{uid}` | `posts/{postId}` | Rare (profile updates) | Cloud Function on user update | Yes — avoids join on every post read |
| Comment count | `comments` subcollection | `posts/{postId}.commentCount` | On every comment | Transaction or Cloud Function | Yes — avoids counting query |
| User avatar URL | `users/{uid}` | `messages/{msgId}` | Rare | Cloud Function | Maybe — depends on message volume |

**Decision rule:** Denormalize if:
- The denormalized data is read 10x+ more frequently than it's updated
- The join would require reading additional documents on a critical path query
- The source data changes infrequently (user profiles vs. real-time counters)

**Don't denormalize if:**
- The source data changes frequently and the denormalized copies are widespread
- Consistency is critical (financial data, permissions)
- The update cascade would be complex or expensive

---

### Phase 3: Cost Estimation

#### 3.1 Per-Query Cost Calculation

Firestore pricing (as of 2025 — verify current rates):

| Operation | Price (per 100,000) | Free Tier (daily) |
|-----------|-------------------|--------------------|
| Document reads | $0.036 | 50,000 |
| Document writes | $0.108 | 20,000 |
| Document deletes | $0.012 | 20,000 |
| Storage | $0.108/GiB/month | 1 GiB |

**Calculate for each critical query:**

```
Query: [Description]
Documents read per execution: [N]
Executions per user per day: [M]
Daily active users: [DAU]

Daily reads: N × M × DAU = [total]
Monthly reads: [total] × 30 = [monthly total]
Monthly cost: ([monthly total] - free tier) × $0.036 / 100,000 = $[cost]
```

#### 3.2 Cost Comparison: Model A vs Model B

When choosing between data model approaches, compare costs:

```markdown
| Metric | Model A (Normalized) | Model B (Denormalized) |
|--------|---------------------|----------------------|
| Reads per "view post" | 3 (post + user + stats) | 1 (post with embedded data) |
| Writes per "create post" | 1 | 1 (same) |
| Writes per "update username" | 1 | 1 + N (update all posts) |
| Monthly read cost (10K DAU) | $[X] | $[Y] |
| Monthly write cost (10K DAU) | $[X] | $[Y] |
| **Total monthly cost** | **$[X]** | **$[Y]** |
```

---

### Phase 4: Index Planning

#### 4.1 Automatic vs Composite Indexes

Firestore automatically indexes every field. Composite indexes are needed for:
- Queries with multiple `where` clauses on different fields
- Queries with `where` + `orderBy` on different fields
- Collection group queries

#### 4.2 Index Specification

```markdown
| Index | Collection | Fields | Query It Serves |
|-------|-----------|--------|-----------------|
| Auto | `posts` | `authorId` | Posts by author |
| Auto | `posts` | `createdAt` | Recent posts |
| Composite | `posts` | `category ASC, createdAt DESC` | Recent posts in category |
| Composite | `posts` | `authorId ASC, status ASC, createdAt DESC` | Author's published posts |
| Collection Group | `comments` | `authorId ASC, createdAt DESC` | All comments by a user |
```

**Index limits:** 200 composite indexes per database. Plan accordingly for complex applications.

#### 4.3 Index Cost Awareness

Each composite index adds storage cost and write latency. Every indexed field increases the write cost. Remove unused indexes.

---

### Phase 5: Validation and Edge Cases

#### 5.1 Document Size Check

For each collection, estimate the maximum document size:

```
Collection: [name]
Fixed fields: ~[X] bytes
Variable fields: [field] max [X] bytes
Arrays: [field] max [N] items × [X] bytes = [total]
Maps: [field] max [X] bytes
Embedded data: ~[X] bytes
─────────────────────────────
Estimated max document size: [X] bytes / KiB
Limit: 1 MiB (1,048,576 bytes)
Safety margin: [OK / Warning / Redesign needed]
```

#### 5.2 Write Contention Check

Identify any documents that could receive concurrent writes:

| Document | Concurrent Write Risk | Mitigation |
|----------|---------------------|------------|
| User profile | Low (one user) | None needed |
| Global counter | High (all users) | Use distributed counters |
| Popular post (likes) | High | Use subcollection or sharded counter |
| Chat room message list | N/A (subcollection) | Each message is its own document |

#### 5.3 Offline Support Validation

If the app is offline-first, verify:
- [ ] All critical-path queries can be served from local cache
- [ ] Write conflicts have a resolution strategy (last-write-wins, merge, manual)
- [ ] Document sizes are reasonable for local storage
- [ ] Listeners are scoped to avoid syncing unnecessary data

---

## Expected Output

### Firestore Data Model Specification

```markdown
# Firestore Data Model: [App Name]

## Overview
- **Collections:** [Count]
- **Subcollections:** [Count]
- **Composite indexes:** [Count]
- **Estimated monthly cost at [DAU] DAU:** $[Amount]

## Query Map
| # | Query | Collection | Reads | Priority |
|---|-------|-----------|-------|----------|
| Q1 | [Description] | [Collection] | [N] | P0 |
| Q2 | [Description] | [Collection] | [N] | P1 |

## Collections

### `users`
[Full specification per template above]

### `posts`
[Full specification per template above]

[... additional collections ...]

## Denormalization Map
| Data | Source | Copies | Update Mechanism |
|------|--------|--------|-----------------|
| [Field] | [Collection] | [Where] | [How] |

## Index Plan
| Type | Collection | Fields | Purpose |
|------|-----------|--------|---------|
| Composite | [Collection] | [Fields] | [Query] |

## Cost Projection

| DAU | Monthly Reads | Monthly Writes | Storage | Total Cost |
|-----|-------------|---------------|---------|------------|
| 100 | [X] | [X] | [X] | $[X] |
| 1,000 | [X] | [X] | [X] | $[X] |
| 10,000 | [X] | [X] | [X] | $[X] |

## Migration Notes (if refactoring)
[Steps to migrate from current model to proposed model]

## Risks and Mitigations
| Risk | Impact | Mitigation |
|------|--------|------------|
| [Risk] | [Impact] | [Strategy] |
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Data model design focus
- **ST-02** (Structured Sequential Instructions) - Phased design process
- **RT-02** (Multi-Dimensional Analysis) - Query patterns, cost, performance, scalability
- **RT-03** (Tree of Thoughts) - Normalized vs denormalized model comparison
- **CM-01** (Explicit Context Framing) - Firestore-specific constraints and billing model
- **DS-06** (Prioritization Guidance) - Query priority classification
- **QA-01** (Chain-of-Verification) - Cost estimation and edge case validation

---

## Related Prompts

- `firebase_cost_monitor_setup.md` - Cost monitoring for the designed model
- `android_firebase_security_rules_audit.md` - Security rules for the collections
- `firebase_cloud_functions_design.md` - Cloud Functions that operate on this data model
- `firebase_analytics_strategy.md` - Analytics events related to data operations
- `firebase_health_check.md` - Periodic health review including data model efficiency

---

## Customization Guide

- **For chat/messaging apps:** Emphasize subcollection design for messages, fan-out patterns for group messages, and presence/typing indicators using RTDB instead of Firestore
- **For e-commerce apps:** Focus on inventory document contention, order state machines, and payment data separation (never store raw payment data in Firestore)
- **For social media apps:** Emphasize fan-out on write patterns for feeds, follower/following relationship modeling, and content moderation data structures
- **For IoT/sensor apps:** Consider RTDB for high-frequency writes, time-series data patterns, and TTL-based cleanup
- **For apps migrating from SQL:** Provide explicit mapping from normalized tables to denormalized collections, and highlight which SQL habits to unlearn
