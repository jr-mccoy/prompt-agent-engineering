---
title: "Android Startup Optimization"
category: mobile-development
description: "Optimizes Android app cold start time by identifying blocking operations and implementing lazy initialization strategies"
techniques:
  - ST-01
  - RT-04
  - ST-03
  - AG-12
difficulty: intermediate
tags:
  - android
  - mobile-development
  - optimization
  - startup-time
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/mobile/android/improvement/android_baseline_profiles_optimization.md
  - domain-software-engineering/mobile/android/analysis/android_performance_audit.md
  - domain-software-engineering/mobile/android/improvement/android_code_modernization.md
---

# Android Startup Optimization

**Objective:** Analyze and optimize Android app cold start time by identifying blocking operations, implementing lazy initialization, and applying startup best practices.

**When to Use:** Use this prompt when app startup feels slow (>2 seconds cold start), when users complain about launch time, before app store submissions, or during performance optimization sprints.

**Prompt Type:** Modular (120-150 lines)

---

## Context Gathering

1. **Current State:**
   - "Do you have metrics on current startup time?"
   - "Is the splash screen showing for too long?"

2. **Requirements:**
   - "What needs to be initialized before the user can interact with the app?"
   - "Are there specific SDKs that must initialize early?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace actual startup time** - Don't flag based on code patterns alone. Measure actual startup time to verify optimization is needed.
2. **Check for existing optimizations** - Search for App Startup library, lazy initialization, or background initialization that may already address concerns.
3. **Understand the context** - Consider WHY certain initializations are in onCreate. Some must be synchronous for app correctness.
4. **Confirm actual impact** - Profile to verify the suspected code actually contributes to slow startup.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `MyApplication.kt:34`).

**Finding ACCEPTABLE startup time is an acceptable outcome.** If startup is within industry standards (<1s cold start), say so with confidence. Don't manufacture optimization concerns.

### False-Positive Prevention

- ❌ Do NOT flag all onCreate code as problematic without profiling
- ❌ Do NOT assume initialization is slow without measuring
- ❌ Do NOT report micro-optimizations that won't noticeably improve startup
- ❌ Do NOT recommend moving required initializations to background
- ✅ DO use Perfetto, Systrace, or startup profiling to verify claims
- ✅ DO understand App Startup library and its guarantees
- ✅ DO consider Baseline Profiles for startup optimization
- ✅ DO test on actual devices, not just emulators

---

### Phase 1: Startup Analysis

#### 1.1 Application.onCreate Analysis

```kotlin
// Find and audit Application class
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        // AUDIT everything that happens here:
        // - Each line adds to startup time
        // - Synchronous calls block the main thread
    }
}
```

**Common Startup Bottlenecks:**

| Operation | Typical Impact | Can Defer? |
|-----------|----------------|------------|
| DI initialization (Hilt/Dagger) | 100-300ms | Partially |
| Analytics SDK init | 50-200ms | Yes |
| Crash reporting init | 50-150ms | Yes |
| Database instance creation | 100-300ms | Yes |
| SharedPreferences read | 10-100ms | Yes |
| Firebase init | 100-500ms | Partially |
| Network client setup | 50-100ms | Yes |
| Image loader init | 50-150ms | Yes |

#### 1.2 ContentProvider Analysis

```xml
<!-- Check AndroidManifest for ContentProviders -->
<!-- Each ContentProvider initializes before Application.onCreate -->
<provider
    android:name="androidx.startup.InitializationProvider"
    android:authorities="${applicationId}.androidx-startup"
    android:exported="false"
    tools:node="merge">
    <!-- Check what initializers are registered -->
</provider>
```

#### 1.3 Main Activity Analysis

```kotlin
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // AUDIT: What happens before setContentView?
        // AUDIT: What happens between setContentView and user can interact?
    }
}
```

---

### Phase 2: Optimization Strategies

#### 2.1 Lazy Initialization

```kotlin
// BEFORE: Eager initialization
class MyApplication : Application() {
    lateinit var analytics: Analytics
    lateinit var database: AppDatabase

    override fun onCreate() {
        super.onCreate()
        analytics = Analytics.init(this) // Blocks startup
        database = Room.databaseBuilder(...).build() // Blocks startup
    }
}

// AFTER: Lazy initialization
class MyApplication : Application() {
    val analytics by lazy { Analytics.init(this) }
    val database by lazy { Room.databaseBuilder(...).build() }
}
```

#### 2.2 Background Initialization

```kotlin
// BEFORE: Blocking initialization
override fun onCreate() {
    super.onCreate()
    val data = loadInitialData() // Blocks main thread
}

// AFTER: Background initialization
override fun onCreate() {
    super.onCreate()
    ProcessLifecycleOwner.get().lifecycleScope.launch(Dispatchers.IO) {
        loadInitialData()
    }
}
```

#### 2.3 App Startup Library

```kotlin
// Define initializer
class AnalyticsInitializer : Initializer<Analytics> {
    override fun create(context: Context): Analytics {
        return Analytics.init(context)
    }

    override fun dependencies(): List<Class<out Initializer<*>>> {
        return emptyList() // Or list dependencies
    }
}

// Register in manifest
<provider
    android:name="androidx.startup.InitializationProvider"
    ...>
    <meta-data
        android:name="com.example.AnalyticsInitializer"
        android:value="androidx.startup" />
</provider>
```

#### 2.4 Splash Screen Optimization

```kotlin
// Use SplashScreen API (Android 12+)
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        val splashScreen = installSplashScreen()

        // Keep splash screen while loading essential data
        splashScreen.setKeepOnScreenCondition {
            viewModel.isLoading.value
        }

        super.onCreate(savedInstanceState)
    }
}
```

---

### Phase 3: Optimization Report

```markdown
## Startup Optimization Report

### Current Startup Analysis

| Phase | Operations | Estimated Time |
|-------|-----------|----------------|
| ContentProviders | [List] | [X ms] |
| Application.onCreate | [List] | [X ms] |
| MainActivity.onCreate | [List] | [X ms] |
| **Total Estimated** | | **[X ms]** |

### Optimization Opportunities

| Operation | Current | Optimization | Savings |
|-----------|---------|--------------|---------|
| [Operation] | Blocking | Lazy | [X ms] |
| [Operation] | Eager | Background | [X ms] |

### Implementation Plan

1. **Quick Wins (Immediate)**
   - [Change with minimal risk]

2. **Medium Effort**
   - [Change requiring testing]

3. **Architectural Changes**
   - [Larger refactoring]

### Expected Results
- **Before:** ~[X] seconds cold start
- **After:** ~[Y] seconds cold start
- **Improvement:** [Z]%
```

---

## Expected Output

1. **Startup Timeline** - Breakdown of what happens during startup
2. **Bottleneck Identification** - Specific operations slowing startup
3. **Optimization Recommendations** - Prioritized improvements
4. **Implementation Guide** - How to apply each optimization

---

## Techniques Used

- **ST-01** (Clear Objective): Startup time focus
- **RT-04** (Best Practice Review): Startup optimization patterns
- **ST-03** (Output Format Templates): Structured report
- **AG-12** (Quantitative Metrics): Time estimates

---

## Related Prompts

- [android_performance_audit.md](../analysis/android_performance_audit.md) - Broader performance review
- [android_code_modernization.md](android_code_modernization.md) - Overall modernization
