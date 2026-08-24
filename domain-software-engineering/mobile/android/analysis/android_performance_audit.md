---
title: "Android Performance Audit"
category: mobile-development
description: "Identifies performance bottlenecks and inefficiencies in Android apps through static analysis with prioritized optimization recommendations"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - android
  - mobile-development
  - performance
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_battery_drain_investigation.md
  - domain-software-engineering/mobile/android/analysis/android_concurrency_threading_analysis.md
  - domain-software-engineering/mobile/android/improvement/android_startup_optimization.md
---


# Android Performance Audit

**Objective:** Identify performance bottlenecks, inefficiencies, and optimization opportunities in an Android codebase through static code analysis, providing prioritized recommendations with estimated impact.

**When to Use:** Use this prompt when users report the app feels slow, battery drains quickly, or startup takes too long. Also ideal for pre-launch performance reviews, quarterly performance audits, or when planning optimization sprints. Best used after a codebase health assessment identifies performance concerns.

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

Before beginning the audit, gather performance context:

1. **Symptoms:**
   - "What performance issues have been reported or observed?"
   - "Which screens or flows feel slow?"
   - "Is battery drain a concern?"

2. **Metrics (if available):**
   - "Do you have any performance metrics (startup time, frame rates, ANR rates)?"
   - "Are there Firebase Performance or other monitoring dashboards?"

3. **Device Targets:**
   - "What's the lowest-end device you need to support well?"
   - "What's your minimum SDK level?"

4. **Constraints:**
   - "Are there features that cannot be changed for performance reasons?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace actual performance impact** - Don't flag based on pattern matching alone. Verify that the suspected issue actually causes measurable performance problems.
2. **Check for existing optimizations** - Search for caching, lazy loading, or other optimizations that may already address the concern.
3. **Understand the context** - Consider WHY the code is structured this way. Some performance trade-offs are intentional for readability or correctness.
4. **Confirm actual impact** - Profile and measure before flagging. Is the "slow" code actually on a hot path?
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `HomeActivity.kt:56`).

**Finding NO significant issues is an acceptable outcome.** If the app performs well, say so with confidence. Don't manufacture performance concerns.

### False-Positive Prevention

- ❌ Do NOT flag all main thread operations as problematic without measuring duration
- ❌ Do NOT flag patterns without profiler evidence of actual impact
- ❌ Do NOT assume performance issues without measuring real-world scenarios
- ❌ Do NOT report micro-optimizations for code that runs rarely
- ✅ DO use Systrace, Perfetto, or Android Profiler to verify claims
- ✅ DO consider the actual frequency and criticality of code paths
- ✅ DO understand Android's optimization capabilities (R8, ART)
- ✅ DO test on representative devices, not just emulators

---

### Phase 1: Performance Discovery

#### 1.1 Startup Performance Analysis

**Application Initialization:**

```kotlin
// Check Application class
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        // AUDIT: What happens here?
        // - Heavy initialization?
        // - Blocking calls?
        // - Third-party SDK init?
    }
}

// ContentProvider initialization (often hidden)
// Check AndroidManifest.xml for ContentProviders
<provider
    android:name=".MyContentProvider"
    android:authorities="..."
    android:initOrder="100" /> // Higher = initialized earlier
```

**Startup Anti-patterns to Find:**

| Anti-pattern | Detection Method | Impact |
|--------------|-----------------|--------|
| Blocking I/O in Application.onCreate | Search for file/network ops | High |
| Heavy DI initialization | Check Dagger/Hilt modules | Medium-High |
| Synchronous analytics init | Check Firebase/analytics init | Medium |
| Large SharedPreferences read | Search for getSharedPreferences in onCreate | Medium |
| Excessive ContentProviders | Count in manifest | Medium |
| Theme/resource inflation | Check for custom themes loading | Low-Medium |

**Search Patterns:**

```kotlin
// Find blocking operations in Application
Application.onCreate() containing:
- Database.getInstance()
- File operations
- SharedPreferences.getX() with MODE_PRIVATE
- Synchronous network calls
- Thread.sleep or blocking waits
```

#### 1.2 UI Performance Analysis

**RecyclerView Performance:**

```kotlin
// ANTI-PATTERN: No ViewHolder optimization
class BadAdapter : RecyclerView.Adapter<ViewHolder>() {
    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        // Creating new objects in bind - BAD
        holder.textView.text = items[position].name
        holder.imageView.setImageBitmap(BitmapFactory.decodeFile(path)) // SLOW!
    }
}

// PATTERN CHECK: DiffUtil usage
class GoodAdapter : ListAdapter<Item, ViewHolder>(ItemDiffCallback())

// Check for setHasFixedSize
recyclerView.setHasFixedSize(true) // Present?

// Check for nested RecyclerViews
// Nested scrolling impacts performance
```

**Compose Performance:**

```kotlin
// ANTI-PATTERN: Unstable lambda in composable
@Composable
fun MyScreen(viewModel: MyViewModel) {
    Button(onClick = { viewModel.onClick() }) // Creates new lambda each recomposition
}

// CHECK: Proper remember usage
val derivedValue = remember(key) { expensiveCalculation() }

// ANTI-PATTERN: Reading state during composition that changes frequently
@Composable
fun BadComposable(scrollState: ScrollState) {
    // Reading scroll position causes recomposition every frame!
    Text("Position: ${scrollState.value}")
}

// CHECK: LaunchedEffect usage for side effects
LaunchedEffect(key) {
    // Side effect here
}
```

**Layout Performance:**

```xml
<!-- ANTI-PATTERN: Deep nesting -->
<LinearLayout>
    <LinearLayout>
        <LinearLayout>
            <LinearLayout> <!-- 4+ levels = performance concern -->
            </LinearLayout>
        </LinearLayout>
    </LinearLayout>
</LinearLayout>

<!-- ANTI-PATTERN: layout_weight in nested LinearLayouts -->
<LinearLayout android:orientation="horizontal">
    <View android:layout_weight="1"/>
    <LinearLayout android:orientation="vertical">
        <View android:layout_weight="1"/> <!-- Triggers multiple measure passes -->
    </LinearLayout>
</LinearLayout>
```

#### 1.3 Memory Performance Analysis

**Potential Memory Leaks:**

```kotlin
// LEAK: Static reference to Context
object Singleton {
    lateinit var context: Context // NEVER store Activity context here
}

// LEAK: Inner class holding Activity reference
class MyActivity : Activity() {
    inner class MyHandler : Handler() { // Implicit reference to Activity
        override fun handleMessage(msg: Message) { }
    }
}

// LEAK: Unregistered listeners
override fun onStart() {
    eventBus.register(this)
}
// Missing: override fun onStop() { eventBus.unregister(this) }

// LEAK: Anonymous class in long-lived scope
class MyViewModel : ViewModel() {
    init {
        api.addListener(object : Listener { // Lives as long as API
            override fun onEvent() {
                // If this references Activity, leak!
            }
        })
    }
}
```

**Large Object Allocations:**

```kotlin
// Find in hot paths:
- Bitmap creation without proper recycling
- Large list/array allocations in loops
- String concatenation in loops (instead of StringBuilder)
- Frequent object creation in onDraw() or bind()
```

#### 1.4 Network Performance Analysis

**Inefficient Network Patterns:**

```kotlin
// ANTI-PATTERN: No caching
@GET("users")
suspend fun getUsers(): List<User> // Called every screen visit?

// ANTI-PATTERN: Sequential calls that could be parallel
suspend fun loadData() {
    val users = api.getUsers()
    val posts = api.getPosts() // Waits for users to complete
    val comments = api.getComments() // Waits for posts to complete
}

// BETTER: Parallel calls
suspend fun loadData() = coroutineScope {
    val users = async { api.getUsers() }
    val posts = async { api.getPosts() }
    val comments = async { api.getComments() }
    Triple(users.await(), posts.await(), comments.await())
}

// ANTI-PATTERN: Large payloads without pagination
@GET("all-items")
suspend fun getAllItems(): List<Item> // Returns thousands of items?
```

#### 1.5 Database Performance Analysis

**Room Performance Issues:**

```kotlin
// ANTI-PATTERN: Query without index
@Query("SELECT * FROM users WHERE email = :email")
suspend fun getUserByEmail(email: String): User?
// Is email column indexed?

// ANTI-PATTERN: N+1 query pattern
fun loadUsersWithPosts() {
    val users = userDao.getAllUsers()
    users.forEach { user ->
        val posts = postDao.getPostsByUser(user.id) // N additional queries!
    }
}

// BETTER: JOIN or @Relation
@Transaction
@Query("SELECT * FROM users")
suspend fun getUsersWithPosts(): List<UserWithPosts>

// ANTI-PATTERN: Main thread database access
val user = userDao.getUserSync() // Blocking on main thread
```

#### 1.6 Background Work Analysis

**WorkManager Issues:**

```kotlin
// CHECK: Proper constraints
val workRequest = OneTimeWorkRequestBuilder<MyWorker>()
    .setConstraints(
        Constraints.Builder()
            .setRequiredNetworkType(NetworkType.CONNECTED) // Present?
            .setRequiresBatteryNotLow(true) // Considered?
            .build()
    )
    .build()

// ANTI-PATTERN: Too frequent periodic work
PeriodicWorkRequestBuilder<SyncWorker>(15, TimeUnit.MINUTES) // Minimum is 15 min
```

---

### Phase 2: Findings Compilation

**CHECKPOINT 1:** Present performance findings summary.

```markdown
## Performance Audit - Initial Findings

### Performance Risk Score: [1-10]

| Category | Issues Found | Severity | Impact |
|----------|-------------|----------|--------|
| Startup | [X] | [Critical/High/Med/Low] | [Estimated ms/s] |
| UI/Rendering | [X] | [Severity] | [Frame impact] |
| Memory | [X] | [Severity] | [MB estimate] |
| Network | [X] | [Severity] | [Data/time impact] |
| Database | [X] | [Severity] | [Query time impact] |
| Background | [X] | [Severity] | [Battery impact] |

### Critical Issues (Immediate Attention)

1. **[Issue]** - [Location] - [Impact]
2. **[Issue]** - [Location] - [Impact]

### High-Impact Quick Wins

1. **[Fix]** - [Estimated improvement] - [Effort: Low]
2. **[Fix]** - [Estimated improvement] - [Effort: Low]

### Questions

1. Are there specific areas you'd like me to deep-dive?
2. Do the identified issues match the symptoms you've observed?

**Shall I proceed with detailed recommendations?**
```

---

### Phase 3: Detailed Performance Report

```markdown
# Performance Audit Report: [App Name]

## Executive Summary

### Overall Performance Grade: [A-F]

| Metric | Assessment | Benchmark |
|--------|------------|-----------|
| Startup Time | [Good/Slow/Critical] | <2s cold start |
| UI Smoothness | [60fps/Jank/Severe] | 60fps target |
| Memory Usage | [Optimal/High/Leak Risk] | <150MB typical |
| Battery Impact | [Low/Medium/High] | Background battery |
| Network Efficiency | [Efficient/Wasteful] | Data usage |

### Critical Findings Summary
1. [Most critical issue with impact]
2. [Second critical issue with impact]
3. [Third critical issue with impact]

---

## Detailed Findings

### 1. Startup Performance

#### Current State
- **Estimated Cold Start:** [X ms/s]
- **Application.onCreate Duration:** [Heavy/Moderate/Light]
- **ContentProviders:** [Count]

#### Issues Found

| Issue | Location | Impact | Priority |
|-------|----------|--------|----------|
| [Issue] | [file:line] | [+X ms] | [Critical/High/Med] |

#### Specific Findings

**Application Initialization:**
```kotlin
// File: MyApplication.kt
// Issue: Synchronous heavy initialization
override fun onCreate() {
    Analytics.init(this) // Blocks for ~200ms
    Database.getInstance(this) // Blocks for ~150ms
}
```

**Recommendations:**
```kotlin
// Lazy initialization
val analytics by lazy { Analytics.init(this) }

// Background initialization
lifecycleScope.launch(Dispatchers.IO) {
    Database.getInstance(this@MyApplication)
}

// Use App Startup library
class AnalyticsInitializer : Initializer<Analytics> {
    override fun create(context: Context): Analytics {
        return Analytics.init(context)
    }
}
```

---

### 2. UI Performance

#### RecyclerView Analysis

| Adapter | DiffUtil | ViewHolder | Issues |
|---------|----------|------------|--------|
| [Adapter] | [Yes/No] | [Optimized/Issues] | [List] |

#### Compose Analysis

| Composable | Stability | Remember Usage | Issues |
|------------|-----------|----------------|--------|
| [Composable] | [Stable/Unstable] | [Proper/Missing] | [List] |

#### Layout Analysis

| Layout | Depth | Weight Usage | Issues |
|--------|-------|--------------|--------|
| [layout.xml] | [X levels] | [Yes/No] | [Specific issues] |

#### Recommendations

**RecyclerView:**
```kotlin
// Add DiffUtil
class MyDiffCallback : DiffUtil.ItemCallback<Item>() {
    override fun areItemsTheSame(old: Item, new: Item) = old.id == new.id
    override fun areContentsTheSame(old: Item, new: Item) = old == new
}

// Use ListAdapter
class MyAdapter : ListAdapter<Item, ViewHolder>(MyDiffCallback())
```

**Compose:**
```kotlin
// Stabilize lambdas
val onClick = remember(viewModel) { { viewModel.onClick() } }

// Use derivedStateOf for computed values
val isValid by remember {
    derivedStateOf { name.isNotBlank() && email.contains("@") }
}
```

---

### 3. Memory Performance

#### Leak Risk Assessment

| Pattern | Instances | Risk Level | Location |
|---------|-----------|------------|----------|
| Static Context | [X] | [High] | [files] |
| Handler leak | [X] | [High] | [files] |
| Listener not unregistered | [X] | [Medium] | [files] |
| Large bitmap | [X] | [Medium] | [files] |

#### Recommendations

```kotlin
// Fix static Context leak
// BEFORE
object UserManager {
    lateinit var context: Context
}

// AFTER
object UserManager {
    private lateinit var appContext: Context

    fun init(context: Context) {
        appContext = context.applicationContext // Only store app context
    }
}

// Fix Handler leak
// BEFORE
inner class MyHandler : Handler(Looper.getMainLooper())

// AFTER
class MyHandler(activity: MyActivity) : Handler(Looper.getMainLooper()) {
    private val activityRef = WeakReference(activity)

    override fun handleMessage(msg: Message) {
        activityRef.get()?.handleMessage(msg)
    }
}
```

---

### 4. Network Performance

#### Network Call Analysis

| Endpoint | Caching | Size | Frequency | Issues |
|----------|---------|------|-----------|--------|
| [endpoint] | [Yes/No] | [KB] | [calls/session] | [Issues] |

#### Recommendations

```kotlin
// Add caching
@GET("users")
@Headers("Cache-Control: max-age=300") // 5 minute cache
suspend fun getUsers(): List<User>

// Parallel loading
suspend fun loadDashboard(): DashboardData = coroutineScope {
    val users = async { api.getUsers() }
    val stats = async { api.getStats() }
    val notifications = async { api.getNotifications() }

    DashboardData(
        users = users.await(),
        stats = stats.await(),
        notifications = notifications.await()
    )
}
```

---

### 5. Database Performance

#### Query Analysis

| Query | Index Used | Execution | Issues |
|-------|------------|-----------|--------|
| [Query] | [Yes/No] | [ms] | [Issues] |

#### Recommendations

```kotlin
// Add missing index
@Entity(
    tableName = "users",
    indices = [Index(value = ["email"], unique = true)]
)
data class User(...)

// Fix N+1 query
@Dao
interface UserDao {
    @Transaction
    @Query("SELECT * FROM users")
    suspend fun getUsersWithPosts(): List<UserWithPosts>
}

data class UserWithPosts(
    @Embedded val user: User,
    @Relation(parentColumn = "id", entityColumn = "userId")
    val posts: List<Post>
)
```

---

## Optimization Roadmap

### Phase 1: Critical Fixes (Immediate)

| Fix | Impact | Effort | Files |
|-----|--------|--------|-------|
| [Fix] | [High] | [Low] | [files] |

### Phase 2: Quick Wins (This Week)

| Optimization | Impact | Effort | Files |
|--------------|--------|--------|-------|
| [Optimization] | [Medium-High] | [Low-Medium] | [files] |

### Phase 3: Strategic Improvements (This Month)

| Improvement | Impact | Effort | Scope |
|-------------|--------|--------|-------|
| [Improvement] | [High] | [High] | [description] |

---

## Profiling Recommendations

### Tools to Use

| Tool | Purpose | When to Use |
|------|---------|-------------|
| Android Studio Profiler | CPU, Memory, Network | General profiling |
| Systrace | UI rendering | Jank investigation |
| LeakCanary | Memory leaks | Development builds |
| Firebase Performance | Production monitoring | Ongoing tracking |

### Suggested Profiling Tasks

1. **Startup Trace:** Record app startup, identify blocking operations
2. **Memory Heap Dump:** After heavy usage, look for leaks
3. **Frame Profiling:** On complex screens, identify jank sources
```

---

## Expected Output

1. **Performance Score** - Overall and per-category ratings
2. **Issue Catalog** - All performance issues with locations and impact
3. **Quick Wins** - Low-effort, high-impact fixes
4. **Optimization Roadmap** - Phased improvement plan
5. **Profiling Guide** - Recommended tools and approaches

---

## Techniques Used

- **ST-01** (Clear Objective): Focused performance analysis
- **ST-02** (Sequential Instructions): Phased discovery and reporting
- **RT-02** (Multi-Dimensional Analysis): Six performance categories
- **RT-05** (Evidence-Based Reasoning): Specific code locations and metrics
- **ST-03** (Output Format Templates): Structured audit report
- **OC-05** (Severity Classification): Impact-based prioritization
- **AG-12** (Quantitative Metrics): Performance scores and estimates
- **NE-02** (Phased Workflow): Clear checkpoints

---

## Related Prompts

- [android_codebase_health_assessment.md](android_codebase_health_assessment.md) - Overall health check
- [android_memory_leak_detection.md](../improvement/android_memory_leak_detection.md) - Deep memory analysis
- [android_startup_optimization.md](../improvement/android_startup_optimization.md) - Startup improvements
- [android_battery_drain_investigation.md](android_battery_drain_investigation.md) - Battery focus

---

## Customization Guide

### For Compose-Heavy Apps
- Emphasize recomposition analysis
- Check remember/derivedStateOf usage
- Analyze state stability
- Review side effect patterns

### For Data-Heavy Apps
- Focus on database queries
- Analyze pagination patterns
- Check caching strategies
- Review data sync efficiency

### For Offline-First Apps
- Analyze sync efficiency
- Check conflict resolution
- Review local storage patterns
- Assess background work efficiency
