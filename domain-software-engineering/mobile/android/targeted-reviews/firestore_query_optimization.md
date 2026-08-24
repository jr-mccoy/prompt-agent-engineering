---
title: "Firestore Query Optimization"
category: mobile-development
description: "Audit and optimize Firestore queries — detect N+1 patterns, unnecessary real-time listeners, missing indexes, client-side joins, pagination strategy, composite index planning, and cost-per-query calculations"
techniques: [ST-01, ST-02, RT-02, CM-01, DS-06]
difficulty: intermediate
tags: [android, firebase, firestore, query-optimization, performance, solo-developer]
updated: "2026-02-11"
---

# Firestore Query Optimization

**Objective:** Audit an Android app's Firestore query layer to identify performance anti-patterns, unnecessary costs, and missing optimizations — covering N+1 query detection, real-time listener audit, missing composite indexes, client-side joins that should be server-side denormalization, pagination strategy (cursor-based vs offset), and per-query cost calculations — producing a prioritized optimization plan with before/after code examples and projected cost savings.

**When to Use:** Use this prompt when your Firebase bill is higher than expected, when screens load slowly due to multiple sequential Firestore reads, when the Firestore console shows missing index warnings, when you suspect your app is reading far more documents than necessary, or when preparing for scale and wanting to ensure your query layer is cost-efficient. This is one of the highest-ROI audits for Firebase apps because query inefficiency is the primary driver of both latency and cost.

**Important context:** Firestore charges per document read, not per query. A single poorly written query that reads 100 documents where 1 would suffice costs 100x more. Unlike SQL where you can join tables efficiently on the server, Firestore has no joins — every "join" you do on the client means additional document reads and additional cost. Optimizing queries often requires changing the data model, so this prompt works best alongside `firestore_data_model_design.md`.

---

## Context Gathering

Before auditing queries, gather essential context:

1. **Current Query Landscape:**
   - "How many distinct Firestore queries does your app make? Which screens make the most queries?"
   - "Are you using real-time listeners (snapshots) or one-time reads (get)? On which queries?"
   - "Have you seen any 'missing index' errors in the Firestore console or logcat?"
   - "What is your current monthly Firestore read count and cost?"

2. **Data Model:**
   - "What are your main collections and their approximate document counts?"
   - "Are you using subcollections? Collection group queries?"
   - "Do any queries require fetching data from multiple collections to display a single screen?"
   - "What fields are you filtering and sorting on?"

3. **Performance Observations:**
   - "Which screens feel slow? How long do they take to load?"
   - "Do you notice lag when scrolling through lists?"
   - "Are there screens that flash or re-render frequently?"
   - "Do you have offline persistence enabled?"

4. **Pagination:**
   - "Do any of your lists show all items at once or do you paginate?"
   - "If paginating, what method are you using (limit, offset, cursor)?"
   - "How many items per page? What is the maximum list size?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before flagging ANY query as problematic, you MUST:**

1. **Count the actual document reads** — Do not guess. Trace the code path and count every `.get()`, `.addSnapshotListener()`, and `.collection().get()` call that executes for a given user action.
2. **Check if a composite index exists** — A query that filters on two fields may already have an index. Check `firestore.indexes.json` and the Firebase console before flagging.
3. **Verify the listener lifecycle** — A snapshot listener that is properly scoped to a screen's lifecycle is not wasteful. Only flag listeners that outlive their usefulness.
4. **Measure, don't assume** — A query reading 10 documents for an admin screen used once a week is not a priority. Focus on high-frequency, high-volume queries.
5. **Consider the data model** — Some query patterns cannot be optimized at the query level and require data model changes. Note when this is the case.

### False-Positive Prevention

- Do NOT flag a real-time listener as wasteful if the data genuinely changes frequently and the UI must reflect changes immediately
- Do NOT flag a multi-document read as an N+1 if the documents are fetched in a single batch via `in` query or `getAll()`
- Do NOT recommend denormalization without calculating the write-cost increase and comparing it to the read-cost savings
- Do NOT assume every list needs cursor-based pagination — small bounded lists (under 50 items) are fine to fetch entirely
- Do NOT flag collection group queries as expensive without checking if they have the required composite indexes
- DO count document reads per user action, not per function call
- DO verify that a listener is actually removed when the composable/fragment/activity is destroyed
- DO check `firestore.indexes.json` for existing composite indexes before recommending new ones
- DO compare the cost of the current approach vs the proposed optimization with real numbers
- DO consider that offline cache reads are free — a query that hits cache is not a cost concern

---

### Phase 1: Query Inventory

#### 1.1 Catalog All Firestore Queries

For each screen or feature, document every Firestore operation:

```
Screen: [Name]
Load Frequency: [Every app open / Navigation / User action]
─────────────────────────────────────────────────────
Query 1:
  Collection: [path]
  Operation: [get / addSnapshotListener / onSnapshot]
  Filters: [where clauses]
  OrderBy: [field, direction]
  Limit: [number or none]
  Estimated docs read: [N]
  Real-time needed: [Yes/No — justify]

Query 2:
  Collection: [path]
  ...

Total document reads per screen load: [sum]
```

#### 1.2 Read Volume Classification

| Volume Class | Reads per Action | Frequency | Priority |
|-------------|-----------------|-----------|----------|
| **Critical** | > 50 docs | Every app open | Optimize immediately |
| **High** | 10-50 docs | Multiple times per session | Optimize soon |
| **Medium** | 3-10 docs | Once per session | Review for improvements |
| **Low** | 1-2 docs | Occasional | Acceptable |

---

### Phase 2: Anti-Pattern Detection

#### 2.1 N+1 Query Pattern

The most expensive and most common Firestore anti-pattern. Fetching a list, then fetching related data for each item individually.

**BAD: N+1 pattern (reads 1 + N documents):**

```kotlin
// BAD: Fetches all posts, then fetches author for EACH post
suspend fun getPostsWithAuthors(): List<PostWithAuthor> {
    val posts = firestore.collection("posts")
        .orderBy("createdAt", Query.Direction.DESCENDING)
        .limit(20)
        .get()
        .await()
        .toObjects(Post::class.java)

    // N+1: This fires 20 ADDITIONAL reads
    return posts.map { post ->
        val author = firestore.document("users/${post.authorId}")
            .get()
            .await()
            .toObject(User::class.java)
        PostWithAuthor(post, author)
    }
}
// Total reads: 1 (posts query) + 20 (author lookups) = 21 reads
```

**GOOD: Denormalized data (reads 1 document per post):**

```kotlin
// GOOD: Author name and avatar are embedded in the post document
suspend fun getPostsWithAuthors(): List<Post> {
    return firestore.collection("posts")
        .orderBy("createdAt", Query.Direction.DESCENDING)
        .limit(20)
        .get()
        .await()
        .toObjects(Post::class.java)
    // Each post already contains authorName and authorAvatarUrl
    // Total reads: 1 query reading 20 documents = 20 reads
}

// Data class with denormalized author info
data class Post(
    val id: String = "",
    val content: String = "",
    val authorId: String = "",
    val authorName: String = "",       // Denormalized from users collection
    val authorAvatarUrl: String = "",  // Denormalized from users collection
    val createdAt: Timestamp? = null
)
```

**GOOD: Batch get when denormalization is not appropriate:**

```kotlin
// GOOD: Batch lookup for unique author IDs
suspend fun getPostsWithAuthors(): List<PostWithAuthor> {
    val posts = firestore.collection("posts")
        .orderBy("createdAt", Query.Direction.DESCENDING)
        .limit(20)
        .get()
        .await()
        .toObjects(Post::class.java)

    // Deduplicate author IDs — often 20 posts have only 5-8 unique authors
    val uniqueAuthorIds = posts.map { it.authorId }.distinct()

    // Batch fetch with whereIn (max 30 per query)
    val authors = if (uniqueAuthorIds.size <= 30) {
        firestore.collection("users")
            .whereIn(FieldPath.documentId(), uniqueAuthorIds)
            .get()
            .await()
            .toObjects(User::class.java)
            .associateBy { it.id }
    } else {
        // Chunk into groups of 30 for the whereIn limit
        uniqueAuthorIds.chunked(30).flatMap { chunk ->
            firestore.collection("users")
                .whereIn(FieldPath.documentId(), chunk)
                .get()
                .await()
                .toObjects(User::class.java)
        }.associateBy { it.id }
    }

    return posts.map { post ->
        PostWithAuthor(post, authors[post.authorId])
    }
}
// Total reads: 20 (posts) + 8 (unique authors) = 28 reads
// vs N+1: 20 (posts) + 20 (per-post author) = 40 reads
```

#### 2.2 Unnecessary Real-Time Listeners

**BAD: Listener on data that rarely changes:**

```kotlin
// BAD: User profile rarely changes, no need for real-time listener
class ProfileViewModel : ViewModel() {
    val profile = firestore.document("users/${auth.uid}")
        .snapshots()             // Real-time listener — fires on every field change
        .map { it.toObject(UserProfile::class.java) }
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), null)
}
// Cost: Continuous reads every time any field on the document changes
```

**GOOD: One-time read for rarely-changing data:**

```kotlin
// GOOD: Fetch once, cache locally, re-fetch on pull-to-refresh
class ProfileViewModel : ViewModel() {
    private val _profile = MutableStateFlow<UserProfile?>(null)
    val profile: StateFlow<UserProfile?> = _profile.asStateFlow()

    init {
        loadProfile()
    }

    fun loadProfile() {
        viewModelScope.launch {
            val doc = firestore.document("users/${auth.uid}")
                .get(Source.CACHE)   // Try cache first
                .await()
            _profile.value = doc.toObject(UserProfile::class.java)
                ?: firestore.document("users/${auth.uid}")
                    .get(Source.SERVER)  // Fall back to server
                    .await()
                    .toObject(UserProfile::class.java)
        }
    }
}
// Cost: 1 read on first load, 0 reads from cache on subsequent loads
```

**Listener Decision Matrix:**

| Data Type | Changes Frequency | Users See It | Recommendation |
|-----------|------------------|-------------|----------------|
| Chat messages | Real-time | Immediately | Listener |
| Feed/timeline | Minutes | On refresh | One-time + pull-to-refresh |
| User profile | Rarely | On navigation | One-time + cache |
| App settings | Very rarely | On restart | One-time + local storage |
| Notifications | Real-time | Badge count | Listener (scoped) |
| Analytics data | Never (historical) | On demand | One-time |

#### 2.3 Client-Side Joins

Detect patterns where the app fetches from multiple collections and merges results in Kotlin code.

**BAD: Client-side join across collections:**

```kotlin
// BAD: Fetch orders, then fetch product details for each line item
suspend fun getOrderDetails(orderId: String): OrderDetails {
    val order = firestore.document("orders/$orderId").get().await()
    val lineItems = order.get("lineItems") as List<Map<String, Any>>

    // Client-side join: fetching each product individually
    val products = lineItems.map { item ->
        val productId = item["productId"] as String
        firestore.document("products/$productId").get().await()
            .toObject(Product::class.java)
    }
    return OrderDetails(order.toObject(Order::class.java)!!, products)
}
// Reads: 1 (order) + N (products per line item)
```

**GOOD: Denormalized order document with embedded product snapshot:**

```kotlin
// GOOD: Product name, price, and image are embedded in the order at creation time
data class OrderLineItem(
    val productId: String = "",
    val productName: String = "",      // Snapshot at order time
    val productImageUrl: String = "",  // Snapshot at order time
    val priceAtPurchase: Double = 0.0, // Frozen price
    val quantity: Int = 0
)

suspend fun getOrderDetails(orderId: String): Order {
    return firestore.document("orders/$orderId")
        .get()
        .await()
        .toObject(Order::class.java)!!
}
// Reads: 1 (order with everything embedded)
```

#### 2.4 Missing Composite Indexes

Check for queries that combine multiple conditions without a composite index:

```kotlin
// This query REQUIRES a composite index on (category ASC, createdAt DESC)
firestore.collection("posts")
    .whereEqualTo("category", "tech")
    .orderBy("createdAt", Query.Direction.DESCENDING)
    .limit(20)
    .get()

// Without the composite index, this query will FAIL at runtime
// Check firestore.indexes.json:
```

```json
{
  "indexes": [
    {
      "collectionGroup": "posts",
      "queryScope": "COLLECTION",
      "fields": [
        { "fieldPath": "category", "order": "ASCENDING" },
        { "fieldPath": "createdAt", "order": "DESCENDING" }
      ]
    }
  ]
}
```

---

### Phase 3: Index Optimization

#### 3.1 Index Audit Checklist

For each composite index in `firestore.indexes.json`:

| Index | Collection | Fields | Query That Uses It | Still Needed? |
|-------|-----------|--------|-------------------|---------------|
| [1] | [collection] | [fields] | [query or UNKNOWN] | [Yes/No/Verify] |

**Common index waste patterns:**
- Indexes for queries that were removed in code refactoring
- Duplicate indexes with different field orders that serve the same query
- Indexes on fields that are no longer filtered or sorted

#### 3.2 Missing Index Detection

Run through every query in the codebase and verify index coverage:

```
Query: posts where category == X, orderBy createdAt DESC
Index needed: (category ASC, createdAt DESC)
Index exists: [Yes/No]
Action: [None / Create / Verify in console]

Query: orders where userId == X, where status == "active", orderBy createdAt DESC
Index needed: (userId ASC, status ASC, createdAt DESC)
Index exists: [Yes/No]
Action: [None / Create / Verify in console]
```

#### 3.3 Index Limit Planning

Firestore allows 200 composite indexes per database. For complex apps, plan index usage:

```
Current composite indexes: [N] / 200
Indexes needed for new features: [M]
Buffer for future growth: [200 - N - M]
Risk: [Low (>100 remaining) / Medium (50-100) / High (<50)]
```

---

### Phase 4: Pagination Strategy

#### 4.1 Pagination Method Comparison

| Method | How It Works | Pros | Cons | Best For |
|--------|-------------|------|------|----------|
| **Cursor-based** | `startAfter(lastDoc)` | Consistent, efficient, works with real-time | Cannot jump to page N | Infinite scroll, feeds |
| **Offset-based** | `offset(N)` | Can jump to any page | Reads and charges for skipped docs | Admin panels (small datasets) |
| **No pagination** | Fetch all | Simple | Expensive, slow for large collections | Lists < 50 items |

#### 4.2 Cursor-Based Pagination Implementation

**GOOD: Proper cursor-based pagination:**

```kotlin
class FeedViewModel : ViewModel() {
    private var lastDocument: DocumentSnapshot? = null
    private val _posts = MutableStateFlow<List<Post>>(emptyList())
    val posts: StateFlow<List<Post>> = _posts.asStateFlow()

    private val _hasMore = MutableStateFlow(true)
    val hasMore: StateFlow<Boolean> = _hasMore.asStateFlow()

    private val pageSize = 20

    fun loadNextPage() {
        viewModelScope.launch {
            var query = firestore.collection("posts")
                .orderBy("createdAt", Query.Direction.DESCENDING)
                .limit(pageSize.toLong())

            // Cursor: start after the last document from previous page
            lastDocument?.let { query = query.startAfter(it) }

            val snapshot = query.get().await()

            if (snapshot.documents.size < pageSize) {
                _hasMore.value = false
            }

            lastDocument = snapshot.documents.lastOrNull()

            val newPosts = snapshot.toObjects(Post::class.java)
            _posts.value = _posts.value + newPosts
        }
    }
}
// Cost per page: exactly [pageSize] document reads
// No wasted reads on skipped documents
```

**BAD: Offset-based pagination (wastes reads):**

```kotlin
// BAD: offset(40) means Firestore reads and CHARGES for 40 skipped docs
suspend fun getPage(pageNumber: Int): List<Post> {
    val offset = pageNumber * 20
    return firestore.collection("posts")
        .orderBy("createdAt", Query.Direction.DESCENDING)
        .offset(offset)  // Reads AND charges for all skipped documents!
        .limit(20)
        .get()
        .await()
        .toObjects(Post::class.java)
}
// Page 3 costs: 60 (skipped) + 20 (returned) = 80 document reads
// But you only display 20 items!
```

#### 4.3 Real-Time Pagination

When combining real-time listeners with pagination:

```kotlin
// Paginated real-time listener — listen only to the current page window
fun listenToPage(lastDoc: DocumentSnapshot?): Flow<List<Post>> {
    var query = firestore.collection("posts")
        .orderBy("createdAt", Query.Direction.DESCENDING)
        .limit(20)

    lastDoc?.let { query = query.startAfter(it) }

    return query.snapshots().map { snapshot ->
        snapshot.toObjects(Post::class.java)
    }
}
// Only pays for changes within the current page window
```

---

### Phase 5: Cost Analysis

#### 5.1 Per-Query Cost Calculation

Firestore pricing (verify current rates at cloud.google.com/firestore/pricing):

| Operation | Cost per 100,000 | Free Tier (daily) |
|-----------|------------------|-------------------|
| Document reads | $0.036 | 50,000 |
| Document writes | $0.108 | 20,000 |
| Document deletes | $0.012 | 20,000 |

**Cost calculation template for each query:**

```
Query: [Description]
Documents read per execution: [N]
Executions per user per day: [M]
Daily Active Users: [DAU]
────────────────────────────────
Daily reads from this query: N x M x DAU = [total]
Monthly reads: [daily total] x 30 = [monthly]
Monthly cost: ([monthly] - free_tier_allocation) x $0.036 / 100,000 = $[cost]
```

#### 5.2 Before/After Cost Comparison

For each optimization, calculate the savings:

| Query | Before (reads/exec) | After (reads/exec) | Daily Execs | Monthly Savings |
|-------|--------------------|--------------------|-------------|----------------|
| Feed load | 41 (N+1) | 20 (denormalized) | 5,000 | $[X] |
| Profile view | 5 (joins) | 1 (embedded) | 10,000 | $[X] |
| Search results | 100 (no limit) | 20 (paginated) | 2,000 | $[X] |
| **Total monthly savings** | | | | **$[X]** |

#### 5.3 Cost Projection at Scale

| DAU | Monthly Reads (Before) | Monthly Reads (After) | Before Cost | After Cost | Savings |
|-----|----------------------|---------------------|-------------|------------|---------|
| 100 | [X] | [X] | $[X] | $[X] | $[X] |
| 1,000 | [X] | [X] | $[X] | $[X] | $[X] |
| 10,000 | [X] | [X] | $[X] | $[X] | $[X] |
| 100,000 | [X] | [X] | $[X] | $[X] | $[X] |

---

## Verification Requirements

After completing the audit, verify your findings:

1. **Read count verification** — For each flagged query, manually trace the code path and count document reads. Confirm the number matches your estimate.
2. **Index verification** — For each recommended index, confirm it does not already exist in `firestore.indexes.json` or the Firebase console.
3. **Cost verification** — Double-check arithmetic in cost calculations. Ensure free tier is correctly subtracted.
4. **Feasibility check** — For each recommended denormalization, confirm the write-cost increase is less than the read-cost decrease.
5. **Regression check** — Ensure that recommended changes do not break real-time update requirements or offline cache behavior.

---

## Expected Output

### Firestore Query Optimization Report

```markdown
# Firestore Query Optimization Report: [App Name]

## Executive Summary
- **Total queries audited:** [N]
- **Anti-patterns found:** [N]
- **Estimated current monthly read cost:** $[X]
- **Estimated monthly cost after optimization:** $[X]
- **Projected monthly savings:** $[X] ([Y]% reduction)

## Query Inventory
| # | Screen | Query | Reads/Exec | Frequency | Monthly Reads | Priority |
|---|--------|-------|-----------|-----------|---------------|----------|
| 1 | [Screen] | [Description] | [N] | [freq] | [total] | Critical |
| 2 | [Screen] | [Description] | [N] | [freq] | [total] | High |

## Anti-Patterns Found

### Finding 1: [Anti-Pattern Name]
- **Location:** [File:line or screen name]
- **Pattern:** [N+1 / Unnecessary listener / Client-side join / Missing index / No pagination]
- **Severity:** High | Medium | Low
- **Confidence:** High | Medium | Low
- **Current cost:** [reads per execution]
- **Optimized cost:** [reads per execution]
- **Before code:** [snippet]
- **After code:** [snippet]
- **Data model changes required:** [Yes/No — details]

### Finding 2: [Anti-Pattern Name]
[Same structure]

## Index Recommendations
| Action | Collection | Fields | Query Served |
|--------|-----------|--------|-------------|
| Create | [collection] | [fields] | [query] |
| Remove | [collection] | [fields] | No longer used |

## Pagination Recommendations
| List | Current Method | Recommended | Reason |
|------|---------------|-------------|--------|
| [List] | [None/Offset] | Cursor-based | [reason] |

## Cost Projection
[Cost table at various DAU levels]

## Prioritized Action Plan
| # | Action | Effort | Impact | Monthly Savings |
|---|--------|--------|--------|----------------|
| 1 | [Action] | Low | High | $[X] |
| 2 | [Action] | Medium | High | $[X] |
| 3 | [Action] | High | Medium | $[X] |

## Data Model Changes Required
[List any denormalization or restructuring needed, with migration notes]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused specifically on Firestore query performance and cost, not general app performance
- **ST-02** (Structured Sequential Instructions) — Phased approach: Inventory, Anti-Pattern Detection, Index Optimization, Pagination, Cost Analysis
- **RT-02** (Multi-Dimensional Analysis) — Each query analyzed across performance, cost, complexity, and maintainability dimensions
- **CM-01** (Explicit Context Framing) — Firestore-specific billing model and limitations established upfront
- **DS-06** (Prioritization Guidance) — Findings ranked by cost impact and frequency, enabling highest-ROI optimizations first

---

## Related Prompts

- `firestore_data_model_design.md` — Data model changes often required to fix query anti-patterns
- `firebase_cost_optimization.md` — Broader cost optimization beyond just queries
- `firebase_cost_monitor_setup.md` — Set up monitoring to track improvements after optimization
- `firebase_security_rules_generator.md` — Security rules that complement optimized query patterns
- `firebase_health_check.md` — Periodic review that includes query efficiency checks
- `android_room_database_query_review.md` — Similar optimization for local Room database queries

---

## Customization Guide

- **For chat/messaging apps:** Focus on real-time listener scoping for message threads, fan-in patterns for conversation lists, and presence queries. Chat apps legitimately need many listeners but should scope them to active conversations only.
- **For e-commerce apps:** Emphasize product catalog pagination, order history cursor-based loading, and cart operations. Product searches often benefit from Algolia or Typesense integration rather than Firestore queries.
- **For social media/feed apps:** Focus on feed denormalization (fan-out on write), timeline pagination, and avoiding N+1 on post metadata. Consider precomputed feed documents for high-traffic users.
- **For IoT/dashboard apps:** Time-series queries are expensive in Firestore. Consider BigQuery for historical data and Firestore only for the latest N readings. Avoid unbounded listeners on sensor data collections.
- **For apps with complex search:** Firestore is not a search engine. If users need full-text search, autocomplete, or faceted filtering, integrate a dedicated search service and use Firestore only for document storage.
