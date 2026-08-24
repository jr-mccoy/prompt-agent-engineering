---
title: "Firebase Cost Optimization"
category: mobile-development
description: "Analyze and optimize Firebase costs — identify expensive read patterns, convert real-time listeners to one-time reads, implement caching strategies, optimize Cloud Functions cold starts, and plan index optimization"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
difficulty: intermediate
tags:
  - android
  - firebase
  - cost-optimization
  - firestore
  - cloud-functions
  - performance
  - solo-developer
updated: "2026-02-11"
---

# Firebase Cost Optimization

**Objective:** Analyze and optimize Firebase costs across all services — identifying expensive Firestore read patterns, converting unnecessary real-time listeners to one-time reads, implementing client-side and server-side caching strategies, reducing Cloud Functions cold starts and execution time, optimizing indexes, and controlling Storage egress — producing a prioritized optimization plan with estimated savings for each change.

**When to Use:** Use this prompt when your Firebase bill is higher than expected, when preparing to scale an app beyond the free tier, when doing a pre-launch cost audit, or when you notice sudden cost spikes in the Firebase Console. Critical because Firebase costs can grow exponentially with users — a pattern that costs $0.50/month at 100 users can cost $500/month at 100,000 users. Finding these patterns early saves real money.

**Important context:** Firebase pricing is usage-based, which means cost grows with success. The most common cost surprise is Firestore reads — a single screen that reads 20 documents, shown to 10,000 daily active users, generates 6 million reads/month ($2.16 just for that one screen). This prompt helps you find these patterns before they become expensive.

---

## Context Gathering

Before analyzing Firebase costs, gather essential context:

1. **Current Costs:**
   - "What is your current monthly Firebase bill?"
   - "Which services are the top cost drivers (Firestore, Functions, Storage, Hosting)?"
   - "Have you experienced any cost spikes? When and what triggered them?"
   - "What is your Firebase billing plan (Spark/free, Blaze/pay-as-you-go)?"

2. **Usage Patterns:**
   - "How many daily active users (DAU) does your app have?"
   - "How many Firestore reads/writes does your app generate daily?"
   - "How many Cloud Functions invocations per day?"
   - "How much data is in Firebase Storage and how often is it downloaded?"

3. **Architecture:**
   - "Which screens use real-time listeners vs one-time reads?"
   - "How many Cloud Functions do you have and what triggers them?"
   - "Do you use offline persistence (Firestore local cache)?"
   - "Are you using composite indexes? How many?"

4. **Growth Projections:**
   - "What is your expected user growth over the next 6 months?"
   - "Are you planning features that would significantly increase reads/writes?"
   - "What is your target monthly Firebase budget?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending ANY cost optimization, you MUST:**

1. **Identify the actual cost drivers** — Don't guess. Check the Firebase Console billing breakdown. A $50/month bill where $48 is Firestore reads and $2 is everything else means you optimize reads, not functions.
2. **Calculate the actual savings** — Every recommendation must include estimated monthly savings. "This will reduce reads" is not helpful. "This will reduce reads by ~500K/month, saving ~$1.80" is.
3. **Consider the tradeoff** — Cheaper is not always better. Converting a real-time listener to a one-time read saves money but degrades the user experience. Document the tradeoff.
4. **Verify the optimization is correct** — An aggressive caching strategy that serves stale data to users is worse than paying more for reads. Correctness comes before cost.
5. **Prioritize by impact** — Fix the $20/month problem before the $0.20 problem. Time is the solo developer's scarcest resource.

**Finding that your costs are reasonable for your usage level is an acceptable outcome.**

### False-Positive Prevention

- ❌ Do NOT recommend removing real-time listeners from features where real-time updates are the core value
- ❌ Do NOT recommend aggressive caching without a cache invalidation strategy
- ❌ Do NOT optimize costs that are within the free tier — save effort for things that actually cost money
- ❌ Do NOT assume all Cloud Functions are expensive — many stay within the free tier forever
- ❌ Do NOT recommend Firebase alternatives for cost reasons alone without considering migration cost
- ✅ DO calculate actual dollar amounts for each optimization
- ✅ DO prioritize by savings-per-effort ratio
- ✅ DO consider the user experience impact of each optimization
- ✅ DO check if the free tier covers the current usage before optimizing
- ✅ DO include a "do nothing" option with projected costs at current growth rate

---

### Phase 1: Firebase Pricing Reference

#### 1.1 Current Firebase Pricing (Blaze Plan, 2025)

| Service | Unit | Price | Free Tier (Monthly) |
|---------|------|-------|---------------------|
| **Firestore reads** | per 100K docs | $0.036 | 50K/day (~1.5M/month) |
| **Firestore writes** | per 100K docs | $0.108 | 20K/day (~600K/month) |
| **Firestore deletes** | per 100K docs | $0.012 | 20K/day (~600K/month) |
| **Firestore storage** | per GiB/month | $0.108 | 1 GiB |
| **Cloud Functions invocations** | per million | $0.40 | 2M/month |
| **Cloud Functions compute** | per 100ms (256MB) | $0.000000463 | 400K GB-seconds |
| **Cloud Functions networking** | per GiB egress | $0.12 | 5 GiB |
| **Cloud Storage** | per GiB/month | $0.026 | 5 GiB |
| **Cloud Storage downloads** | per GiB egress | $0.12 | 1 GiB/day |
| **Cloud Storage operations** | per 10K | $0.05 (upload) / $0.004 (download) | 50K uploads, 50K downloads/day |
| **Authentication** | per SMS verification | $0.01-0.06 (by country) | 10 SMS/day (US) |
| **Hosting** | per GiB stored | $0.026 | 10 GiB |
| **Hosting transfer** | per GiB | $0.15 | 360 MB/day |

**Key insight:** For most apps, Firestore reads are 60-80% of the bill. Optimize reads first.

#### 1.2 Quick Cost Calculator

```markdown
## Cost Estimation Worksheet

### Firestore
Daily Active Users (DAU): ___
Avg reads per session: ___
Sessions per user per day: ___

Daily reads = DAU × reads/session × sessions/day = ___
Monthly reads = daily × 30 = ___
Free tier monthly = ~1,500,000
Billable reads = monthly - 1,500,000 = ___
Monthly cost = billable × $0.036 / 100,000 = $___

### Cloud Functions
Daily invocations: ___
Avg execution time (ms): ___
Memory allocation (MB): ___

Monthly invocations = daily × 30 = ___
Free tier = 2,000,000
Billable invocations = monthly - 2,000,000 = ___
Invocation cost = billable × $0.40 / 1,000,000 = $___
Compute cost = (billable × avg_time_ms / 100) × $0.000000463 × (memory / 256) = $___

### Storage
Total stored (GiB): ___
Monthly downloads (GiB): ___

Storage cost = max(0, stored - 5) × $0.026 = $___
Egress cost = max(0, downloads - 30) × $0.12 = $___
```

---

### Phase 2: Firestore Read Optimization

#### 2.1 Read Audit: Find Your Expensive Screens

For each screen in your app, calculate the read cost:

```markdown
| Screen | Data Loaded | Reads/Visit | Visits/Day (per user) | Real-time? | Monthly Reads (1K DAU) |
|--------|------------|-------------|----------------------|------------|----------------------|
| Home | Feed (20 posts) | 20 | 5 | Yes (listener) | 3,000,000 |
| Profile | User doc + posts | 11 | 2 | No (one-time) | 660,000 |
| Settings | User settings | 1 | 0.5 | No | 15,000 |
| Search | Query results (10) | 10 | 3 | No | 900,000 |
| **Total** | | | | | **4,575,000** |
```

#### 2.2 Optimization Patterns

**Pattern 1: Convert unnecessary real-time listeners to one-time reads**

```kotlin
// EXPENSIVE: Real-time listener on data that rarely changes
// Every time any post changes, ALL 20 documents re-read and re-billed
val listener = db.collection("posts")
    .orderBy("createdAt", Query.Direction.DESCENDING)
    .limit(20)
    .addSnapshotListener { snapshot, error ->
        // This fires on every change, re-reading all 20 docs
        updateUI(snapshot)
    }

// CHEAPER: One-time read with pull-to-refresh
suspend fun loadPosts(): List<Post> {
    return db.collection("posts")
        .orderBy("createdAt", Query.Direction.DESCENDING)
        .limit(20)
        .get()
        .await()
        .toObjects(Post::class.java)
}

// Savings: If listener fires 5x/hour × 8 hours = 40 re-reads/day
// 40 × 20 docs × 1K users = 800K reads/day saved
// Monthly savings: 24M reads × $0.036/100K = $8.64/month at 1K DAU
```

**Pattern 2: Reduce document count per query**

```kotlin
// EXPENSIVE: Loading full user profiles for a member list
// Each profile: displayName, email, photoUrl, bio, settings, preferences...
val members = db.collection("users")
    .whereIn(FieldPath.documentId(), memberIds) // 50 full user docs
    .get()

// CHEAPER: Use a denormalized "memberSummary" with only display fields
// Each summary: displayName, photoUrl (2 fields vs 20)
val members = db.collection("groups/${groupId}/memberSummaries")
    .get() // Same 50 docs but much smaller, and in one subcollection

// Savings: Same read count, but faster load times
// Better approach: embed member summaries in the group document itself
val group = db.document("groups/$groupId").get()
// group.data.memberSummaries = [{ uid, displayName, photoUrl }, ...]
// 1 read instead of 50
// Monthly savings at 1K DAU, 3 views/day: 50 × 3 × 1K × 30 - 1 × 3 × 1K × 30 = 4,410K reads
```

**Pattern 3: Client-side caching**

```kotlin
class PostRepository(
    private val db: FirebaseFirestore,
    private val cache: PostCache // Room database or in-memory
) {
    // Cache-first strategy
    suspend fun getPosts(forceRefresh: Boolean = false): List<Post> {
        // Check cache age
        if (!forceRefresh && cache.isValid(maxAgeMinutes = 5)) {
            return cache.getPosts()
        }

        // Fetch from Firestore
        val posts = db.collection("posts")
            .orderBy("createdAt", Query.Direction.DESCENDING)
            .limit(20)
            .get(Source.SERVER) // Explicitly hit server
            .await()
            .toObjects(Post::class.java)

        // Update cache
        cache.savePosts(posts)
        return posts
    }

    // For pull-to-refresh
    suspend fun refreshPosts() = getPosts(forceRefresh = true)
}

// Savings: If user opens the app 5x/day but posts only refresh 2x
// 60% fewer Firestore reads for this screen
```

**Pattern 4: Pagination instead of loading all**

```kotlin
// EXPENSIVE: Load all user's items at once
val allItems = db.collection("users/${uid}/items")
    .orderBy("createdAt", Query.Direction.DESCENDING)
    .get() // Could be 500+ documents!

// CHEAPER: Paginate with cursor
class PaginatedItemsSource(
    private val db: FirebaseFirestore,
    private val uid: String
) {
    private var lastDocument: DocumentSnapshot? = null
    private val pageSize = 20

    suspend fun loadNextPage(): List<Item> {
        var query = db.collection("users/$uid/items")
            .orderBy("createdAt", Query.Direction.DESCENDING)
            .limit(pageSize.toLong())

        lastDocument?.let { query = query.startAfter(it) }

        val snapshot = query.get().await()
        lastDocument = snapshot.documents.lastOrNull()
        return snapshot.toObjects(Item::class.java)
    }
}

// Savings: User with 200 items loads 20 instead of 200 on screen open
// 90% fewer reads on initial load
```

#### 2.3 Read Optimization Decision Matrix

| Current Pattern | Optimization | Savings | UX Impact | Effort | Recommendation |
|----------------|-------------|---------|-----------|--------|----------------|
| Real-time listener on static data | One-time read + pull-to-refresh | High | Minor (manual refresh) | Low | Do first |
| Loading N docs for a list | Denormalize into parent doc | High | None (faster) | Medium | Do if N > 10 |
| Loading full docs for summaries | Create summary subcollection | Medium | None | Medium | Do if doc size > 5KB |
| No pagination | Add cursor-based pagination | High | Better (faster initial load) | Medium | Do if list > 20 items |
| No client cache | Add Room/memory cache | High | Better (instant subsequent loads) | High | Do for frequently visited screens |
| Multiple queries per screen | Batch/combine into one query | Medium | None | Low | Do always |

---

### Phase 3: Cloud Functions Cost Optimization

#### 3.1 Function Cost Audit

For each Cloud Function, calculate the actual cost:

```markdown
| Function | Trigger | Invocations/Day | Avg Duration | Memory | Daily Cost | Monthly Cost |
|----------|---------|----------------|-------------|--------|------------|-------------|
| onUserCreated | Auth | 50 | 800ms | 256MB | $0.0004 | $0.01 |
| onPostCreated | Firestore | 200 | 500ms | 256MB | $0.001 | $0.03 |
| sendNotification | Callable | 1,000 | 300ms | 128MB | $0.003 | $0.09 |
| dailyCleanup | Scheduled | 1 | 30s | 256MB | $0.0001 | $0.003 |
| imageProcessor | Storage | 100 | 5s | 1GB | $0.01 | $0.30 |
| **Total** | | **1,351** | | | **$0.014** | **$0.43** |
```

**Key insight:** Most solo-developer apps have Cloud Functions costs well within the free tier (2M invocations + 400K GB-seconds/month). Don't optimize functions unless they're actually costing money.

#### 3.2 Functions That Might Not Need to Be Functions

| Current Function | Alternative | When to Switch |
|-----------------|------------|----------------|
| Validate data on write | Firestore security rules | If validation is simple (type checks, ranges, enums) |
| Set default fields on create | Client-side defaults | If no security concern with client setting defaults |
| Aggregate counts | Client-side increment in transaction | If count doesn't need to be perfectly accurate |
| Format data before display | Client-side formatting | Always — never pay for server compute for display logic |
| Send welcome email | Firebase Extensions (Trigger Email) | If using standard templates |

#### 3.3 Cold Start Optimization

```typescript
// EXPENSIVE: Large bundle with unused dependencies
import { BigQuery } from "@google-cloud/bigquery";
import { Storage } from "@google-cloud/storage";
import Stripe from "stripe";
import SendGrid from "@sendgrid/mail";
// All imported even if this function only uses Firestore

export const simpleUpdate = onDocumentCreated("items/{id}", async (event) => {
  // Does not use BigQuery, Storage, Stripe, or SendGrid
  await event.data?.ref.update({ processed: true });
});

// CHEAP: Only import what this function needs
export const simpleUpdate = onDocumentCreated("items/{id}", async (event) => {
  await event.data?.ref.update({ processed: true });
});

// SEPARATE FILE: Heavy functions in their own module
// functions/src/billing/stripe.ts — only loaded when stripe functions run
// functions/src/email/sendgrid.ts — only loaded when email functions run
// functions/src/index.ts — imports selectively
```

#### 3.4 Execution Time Reduction

```typescript
// SLOW: Sequential external calls
export const processOrder = onDocumentCreated("orders/{id}", async (event) => {
  const data = event.data?.data();
  await sendConfirmationEmail(data);    // 500ms
  await updateInventory(data);           // 300ms
  await notifyAdmin(data);               // 200ms
  // Total: 1000ms of compute time
});

// FAST: Parallel where possible
export const processOrder = onDocumentCreated("orders/{id}", async (event) => {
  const data = event.data?.data();
  await Promise.all([
    sendConfirmationEmail(data),    // 500ms
    updateInventory(data),           // 300ms  } Runs in parallel
    notifyAdmin(data),               // 200ms  } Total: 500ms
  ]);
  // Total: 500ms — half the compute cost
});
```

---

### Phase 4: Storage Cost Optimization

#### 4.1 Storage Cost Analysis

| Content Type | Total Size | Downloads/Month | Storage Cost | Egress Cost | Total |
|-------------|-----------|-----------------|-------------|-------------|-------|
| User avatars | 2 GiB | 50 GiB | $0.05 | $5.40 | $5.45 |
| Uploaded photos | 10 GiB | 20 GiB | $0.26 | $1.80 | $2.06 |
| App assets | 0.5 GiB | 5 GiB | $0.01 | $0.00 | $0.01 |
| **Total** | **12.5 GiB** | **75 GiB** | **$0.32** | **$7.20** | **$7.52** |

**Key insight:** Storage costs are mostly egress (downloads), not storage itself. Reduce download size and frequency.

#### 4.2 Storage Optimization Patterns

```kotlin
// EXPENSIVE: Serving full-resolution images every time
Glide.with(context)
    .load(storageRef.downloadUrl) // 2MB original image for a 48dp avatar
    .into(avatarImageView)

// CHEAPER: Use Firebase Extensions "Resize Images" to auto-generate thumbnails
// Configure: 100x100 for avatars, 400x400 for previews, original for detail view
Glide.with(context)
    .load(thumbnailStorageRef.downloadUrl) // 15KB thumbnail
    .into(avatarImageView)

// Savings: 2MB → 15KB per avatar load = 99.25% reduction
// At 50K avatar loads/month: 100 GiB → 0.75 GiB egress
```

**Image optimization checklist:**
- [ ] Compress images on upload (max 1MB for photos, 100KB for avatars)
- [ ] Generate thumbnails using Resize Images extension
- [ ] Use CDN-cached download URLs (Firebase Storage URLs are already CDN-backed)
- [ ] Implement client-side image caching (Glide/Coil handle this automatically)
- [ ] Set Cache-Control headers on uploaded files

```kotlin
// Set cache headers when uploading
val metadata = StorageMetadata.Builder()
    .setCacheControl("public, max-age=86400") // 24-hour cache
    .setContentType("image/jpeg")
    .build()

storageRef.putFile(imageUri, metadata)
```

---

### Phase 5: Quick Wins vs Deep Optimization

#### 5.1 Optimization Priority Matrix

| Optimization | Savings/Month | Effort | Risk | Priority |
|-------------|--------------|--------|------|----------|
| Convert static listeners to one-time reads | $5-50 | Low (1-2 hours) | Low | **Do first** |
| Add pagination to long lists | $2-20 | Low (2-3 hours) | Low | **Do first** |
| Enable Firestore offline persistence | $1-10 | Minimal (1 line) | Low | **Do first** |
| Compress images before upload | $1-5 | Low (1-2 hours) | Low | **Do first** |
| Denormalize frequently-joined data | $5-30 | Medium (4-8 hours) | Medium | **Do second** |
| Add client-side caching (Room) | $5-20 | High (8-16 hours) | Low | **Do second** |
| Optimize Cloud Functions cold starts | $0.50-5 | Medium (2-4 hours) | Low | **Do third** |
| Split Cloud Functions into separate files | $0.10-1 | Medium (2-4 hours) | Low | **Do third** |
| Remove unused composite indexes | $0.01-0.10 | Low (30 min) | Low | **Do when convenient** |

#### 5.2 One-Line Wins

```kotlin
// WIN 1: Enable offline persistence (on by default, but verify)
// This serves cached data instead of hitting Firestore for repeated reads
val settings = FirebaseFirestoreSettings.Builder()
    .setPersistenceEnabled(true) // Default is true, but explicit is good
    .setCacheSizeBytes(FirebaseFirestoreSettings.CACHE_SIZE_UNLIMITED)
    .build()
Firebase.firestore.firestoreSettings = settings

// WIN 2: Use Source.CACHE for data that doesn't need to be fresh
val cachedUser = db.document("users/$uid")
    .get(Source.CACHE) // Zero Firestore reads — free!
    .await()

// WIN 3: Limit query results
// BAD: No limit (reads ALL documents in collection)
db.collection("posts").get()

// GOOD: Always limit
db.collection("posts")
    .orderBy("createdAt", Query.Direction.DESCENDING)
    .limit(20)
    .get()
```

#### 5.3 Cost Monitoring Setup

```kotlin
// Set budget alerts in Firebase Console:
// Firebase Console → Usage and billing → Manage billing → Budgets and alerts
// Set alerts at: $5, $10, $25 (adjust to your scale)

// For programmatic monitoring, use Cloud Functions:
// This function runs daily and checks costs
export const checkDailyCosts = onSchedule("every day 09:00", async () => {
  // Query Cloud Billing API for current spending
  // Send alert if spending exceeds threshold
  // Log daily cost breakdown to Firestore for tracking
});
```

---

### Phase 6: Growth Cost Projection

#### 6.1 Cost Scaling Model

```markdown
| DAU | Monthly Reads | Monthly Writes | Functions | Storage | **Total/Month** |
|-----|-------------|---------------|-----------|---------|----------------|
| 100 | 450K (free) | 30K (free) | 5K (free) | 0.5 GiB (free) | **$0** |
| 500 | 2.25M | 150K | 25K (free) | 2 GiB (free) | **$0.27** |
| 1,000 | 4.5M | 300K | 50K (free) | 4 GiB (free) | **$1.08** |
| 5,000 | 22.5M | 1.5M | 250K (free) | 15 GiB | **$8.75** |
| 10,000 | 45M | 3M | 500K (free) | 30 GiB | **$18.40** |
| 50,000 | 225M | 15M | 2.5M | 100 GiB | **$96.00** |

Note: These are estimates based on a typical content-browsing app with
20 reads/session, 2 sessions/user/day, 2 writes/session.
Your actual costs will vary based on usage patterns.
```

#### 6.2 Cost Breakeven Points

| Service | Free Tier | Cost When Exceeded | Usage to Hit |
|---------|-----------|-------------------|-------------|
| Firestore reads | ~1.5M/month | $0.036/100K | ~750 DAU at 20 reads/session, 2x/day |
| Firestore writes | ~600K/month | $0.108/100K | ~5,000 DAU at 2 writes/session, 2x/day |
| Cloud Functions | 2M invocations | $0.40/1M | Rarely exceeded by solo-dev apps |
| Storage | 5 GiB stored | $0.026/GiB | ~5K users with avatars |
| Storage egress | ~30 GiB/month | $0.12/GiB | ~2K DAU loading images frequently |

---

## Expected Output

### Firebase Cost Optimization Report

```markdown
# Firebase Cost Optimization: [App Name]

## Current Cost Breakdown
| Service | Monthly Cost | % of Total |
|---------|-------------|-----------|
| Firestore reads | $[X] | [Y]% |
| Firestore writes | $[X] | [Y]% |
| Cloud Functions | $[X] | [Y]% |
| Storage | $[X] | [Y]% |
| **Total** | **$[X]** | **100%** |

## Top Cost Driver Analysis
1. **[Service]** — [Why it's expensive] — [Specific screens/features causing it]

## Optimization Plan (Prioritized)

### Quick Wins (< 2 hours each)
| # | Change | Estimated Savings | UX Impact |
|---|--------|------------------|-----------|
| 1 | [Change] | $[X]/month | [None/Minor/Moderate] |

### Medium Effort (2-8 hours each)
| # | Change | Estimated Savings | UX Impact |
|---|--------|------------------|-----------|
| 1 | [Change] | $[X]/month | [None/Minor/Moderate] |

### Long-term (8+ hours each)
| # | Change | Estimated Savings | UX Impact |
|---|--------|------------------|-----------|
| 1 | [Change] | $[X]/month | [None/Minor/Moderate] |

## Total Projected Savings: $[X]/month

## 6-Month Cost Projection
| Month | Current Path | Optimized Path | Savings |
|-------|-------------|---------------|---------|
| Month 1 | $[X] | $[Y] | $[Z] |
| Month 6 | $[X] | $[Y] | $[Z] |

## Do-Nothing Costs (Current Growth Rate)
At [growth rate], monthly costs will reach $[X] by [date].
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Cost optimization with measurable savings targets
- **ST-02** (Structured Sequential Instructions) - Phased optimization from audit to implementation
- **RT-02** (Multi-Dimensional Analysis) - Cost, performance, UX, and effort dimensions
- **CM-01** (Explicit Context Framing) - Firebase pricing model and billing constraints
- **DS-06** (Prioritization Guidance) - Quick wins first, savings-per-effort ranking

---

## Related Prompts

- `firebase_cost_monitor_setup.md` - Ongoing cost monitoring and alerts
- `firestore_data_model_design.md` - Data model decisions that affect cost
- `firestore_query_optimization.md` - Detailed query optimization patterns
- `firebase_cloud_functions_design.md` - Functions architecture affecting cost
- `firebase_health_check.md` - Periodic health review including cost trends

---

## Customization Guide

- **For apps within the free tier:** Focus on the growth projection section to understand when you'll start paying and which optimization to implement before that point.
- **For apps with heavy image/file usage:** Expand the Storage section with CDN strategies, progressive image loading, and consider moving large files to a dedicated CDN like Cloudflare R2.
- **For apps with many Cloud Functions:** Add a function-by-function audit, identify functions that can be replaced by security rules or client logic, and implement the function splitting pattern.
- **For apps with real-time features (chat, collaboration):** Don't convert those listeners to one-time reads. Instead focus on listener scope (don't listen to entire collections) and pagination within listeners.
- **For apps approaching $100+/month:** Consider architectural changes like moving heavy read patterns to a read-through cache (Redis via Cloud Run) or pre-computed views updated by Cloud Functions.
