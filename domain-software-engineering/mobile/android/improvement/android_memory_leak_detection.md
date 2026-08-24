---
title: "Android Memory Leak Detection"
category: mobile-development
description: "Identifies potential memory leaks through static analysis patterns with specific fixes for each leak type"
techniques:
  - ST-01
  - ST-02
  - RT-04
  - RT-05
  - OC-05
difficulty: intermediate
tags:
  - android
  - mobile-development
  - memory
  - performance
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_performance_audit.md
  - domain-software-engineering/mobile/android/analysis/android_codebase_health_assessment.md
  - domain-software-engineering/mobile/android/targeted-reviews/android_coroutine_scope_review.md
---

# Android Memory Leak Detection

**Objective:** Identify potential memory leaks in an Android codebase through static analysis patterns, providing specific fixes for each leak type.

**When to Use:** Use this prompt when users report out-of-memory crashes, app slowdowns over time, or when profiling shows growing memory usage. Also useful during code reviews, before releases, or as part of regular quality audits.

**Prompt Type:** Comprehensive (300-350 lines)

---

## Context Gathering

1. **Symptoms:**
   - "Have you observed OOM crashes or memory-related ANRs?"
   - "Does the app slow down the longer it's used?"
   - "Are there specific flows where memory issues occur?"

2. **Profiling Data (if available):**
   - "Have you captured heap dumps or memory profiles?"
   - "Is LeakCanary or similar tooling already integrated?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace actual memory retention** - Don't flag based on pattern matching alone. Verify that the suspected leak actually holds references improperly.
2. **Check for existing leak prevention** - Search for WeakReferences, proper lifecycle handling, or LeakCanary integration that may already address concerns.
3. **Understand the context** - Consider WHY certain patterns exist. Some "leak patterns" are actually correct for the use case.
4. **Confirm actual memory impact** - Use heap dumps or LeakCanary to verify suspected leaks, not just code inspection.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `MainActivity.kt:45`).

**Finding NO leaks is an acceptable outcome.** If the code handles memory correctly, say so with confidence. Don't manufacture leak concerns.

### False-Positive Prevention

- ❌ Do NOT flag all static references as leaks without checking what they hold
- ❌ Do NOT flag ViewModel references from lifecycle-aware components (they're correct)
- ❌ Do NOT assume missing cleanup without checking onDestroy/onCleared
- ❌ Do NOT report theoretical leaks without demonstrating actual retention
- ✅ DO use LeakCanary or heap analysis to verify suspected leaks
- ✅ DO understand Android lifecycle and proper reference handling
- ✅ DO check for WeakReference usage before flagging
- ✅ DO consider the difference between temporary and persistent references

---

### Phase 1: Leak Pattern Detection

#### 1.1 Context Leaks (Most Common)

**Static Context References:**

```kotlin
// LEAK: Singleton holding Activity context
object UserManager {
    lateinit var context: Context // If Activity context stored here = LEAK

    fun init(context: Context) {
        this.context = context // Leaks if Activity passed
    }
}

// LEAK: Companion object with context
class MyFragment : Fragment() {
    companion object {
        var context: Context? = null // Lives forever, leaks Activity
    }
}

// FIX: Use Application context
object UserManager {
    private lateinit var appContext: Context

    fun init(context: Context) {
        appContext = context.applicationContext // Safe: Application lives as long as process
    }
}
```

**Search patterns:**
```kotlin
// Find potential leaks:
object.*Context
companion object.*context
static.*Context
lateinit var context
```

#### 1.2 Handler and Runnable Leaks

**Inner Class Handler:**

```kotlin
// LEAK: Non-static inner class holds implicit reference to outer Activity
class MyActivity : AppCompatActivity() {

    private val handler = object : Handler(Looper.getMainLooper()) {
        override fun handleMessage(msg: Message) {
            updateUI() // Implicit reference to MyActivity
        }
    }

    // If handler has pending messages when Activity destroyed = LEAK
}

// FIX: WeakReference pattern
class MyActivity : AppCompatActivity() {

    private class SafeHandler(activity: MyActivity) : Handler(Looper.getMainLooper()) {
        private val activityRef = WeakReference(activity)

        override fun handleMessage(msg: Message) {
            activityRef.get()?.updateUI()
        }
    }

    private val handler = SafeHandler(this)

    override fun onDestroy() {
        super.onDestroy()
        handler.removeCallbacksAndMessages(null) // Clear pending messages
    }
}
```

**Runnable Leaks:**

```kotlin
// LEAK: Anonymous Runnable captures Activity
class MyActivity : AppCompatActivity() {

    fun startDelayedWork() {
        handler.postDelayed({
            updateUI() // Captures Activity reference
        }, 10000) // If Activity destroyed before 10s = LEAK
    }
}

// FIX: Remove callbacks or use lifecycle-aware approach
override fun onDestroy() {
    super.onDestroy()
    handler.removeCallbacksAndMessages(null)
}

// BETTER: Use coroutines with lifecycle scope
lifecycleScope.launch {
    delay(10000)
    updateUI() // Automatically cancelled when lifecycle destroyed
}
```

#### 1.3 Listener and Callback Leaks

**Unregistered Listeners:**

```kotlin
// LEAK: Listener registered but never unregistered
class MyActivity : AppCompatActivity() {

    override fun onStart() {
        super.onStart()
        EventBus.register(this) // Registers
    }

    // Missing onStop() with EventBus.unregister(this) = LEAK
}

// LEAK: Observer not removed
class MyActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        ContentResolver.registerContentObserver(uri, true, observer)
        // If not unregistered = LEAK
    }
}

// FIX: Always pair register with unregister
override fun onStart() {
    super.onStart()
    EventBus.register(this)
}

override fun onStop() {
    super.onStop()
    EventBus.unregister(this)
}
```

#### 1.4 ViewModel and LiveData Leaks

**Passing Activity to ViewModel:**

```kotlin
// LEAK: ViewModel holds Activity reference
class MyViewModel(private val activity: Activity) : ViewModel() {
    // ViewModel outlives Activity = LEAK
}

// LEAK: Storing View in ViewModel
class MyViewModel : ViewModel() {
    var textView: TextView? = null // Views hold Context = LEAK
}

// FIX: Never pass Activity/View to ViewModel
class MyViewModel(application: Application) : AndroidViewModel(application) {
    // Use application context if needed
}
```

**LiveData Observer Leaks:**

```kotlin
// LEAK: Observing with wrong lifecycle owner
class MyFragment : Fragment() {

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        // WRONG: Using fragment as owner in onViewCreated
        // viewModel.data.observe(this) { } // Can leak on config change

        // CORRECT: Use viewLifecycleOwner
        viewModel.data.observe(viewLifecycleOwner) { data ->
            updateUI(data)
        }
    }
}
```

#### 1.5 Coroutine Scope Leaks

**GlobalScope Misuse:**

```kotlin
// LEAK: GlobalScope lives forever
class MyActivity : AppCompatActivity() {

    fun loadData() {
        GlobalScope.launch {
            val data = repository.getData()
            withContext(Dispatchers.Main) {
                updateUI(data) // Activity may be destroyed
            }
        }
    }
}

// FIX: Use lifecycle-aware scope
class MyActivity : AppCompatActivity() {

    fun loadData() {
        lifecycleScope.launch {
            val data = repository.getData()
            updateUI(data) // Automatically cancelled when lifecycle destroyed
        }
    }
}

// In ViewModel
class MyViewModel : ViewModel() {
    fun loadData() {
        viewModelScope.launch {
            // Automatically cancelled when ViewModel cleared
        }
    }
}
```

#### 1.6 Bitmap and Resource Leaks

**Large Bitmap References:**

```kotlin
// LEAK: Holding onto large bitmaps
class ImageCache {
    private val cache = mutableMapOf<String, Bitmap>() // Can grow unbounded
}

// FIX: Use LruCache or weak references
class ImageCache(maxSize: Int) {
    private val cache = object : LruCache<String, Bitmap>(maxSize) {
        override fun sizeOf(key: String, bitmap: Bitmap): Int {
            return bitmap.byteCount / 1024
        }
    }
}

// Or use image loading library (Coil, Glide)
```

**Unclosed Resources:**

```kotlin
// LEAK: Stream not closed
fun readFile(path: String): String {
    val stream = FileInputStream(path)
    return stream.readText() // Stream never closed
}

// FIX: Use use() extension
fun readFile(path: String): String {
    return FileInputStream(path).use { stream ->
        stream.readText()
    }
}

// Or: bufferedReader()
fun readFile(path: String): String {
    return File(path).bufferedReader().use { it.readText() }
}
```

---

### Phase 2: Leak Findings Report

**CHECKPOINT:** Present leak analysis findings.

```markdown
## Memory Leak Analysis Results

### Summary

| Leak Type | Instances Found | Severity |
|-----------|-----------------|----------|
| Context Leaks | [X] | High |
| Handler/Runnable Leaks | [X] | High |
| Listener Leaks | [X] | Medium |
| ViewModel Leaks | [X] | Medium |
| Coroutine Scope Leaks | [X] | Medium |
| Resource Leaks | [X] | Low |

### High Priority Fixes

| Issue | Location | Impact | Fix Effort |
|-------|----------|--------|------------|
| [Issue] | [file:line] | [Memory impact] | [Low/Med] |

### Detailed Findings

#### Context Leaks

| Location | Pattern | Fix |
|----------|---------|-----|
| [file:line] | [Description] | [Solution] |

**Shall I provide fixes for these leaks?**
```

---

### Phase 3: Implementation Fixes

For each identified leak, provide specific fixes:

```markdown
## Leak Fix: [Location]

### Current Code (Leaking)
```kotlin
[Current code that leaks]
```

### Fixed Code
```kotlin
[Corrected code]
```

### Explanation
[Why this fixes the leak]

### Verification
- [ ] Build passes
- [ ] Leak no longer detected by LeakCanary
- [ ] Memory profile shows stable usage
```

---

## Expected Output

1. **Leak Inventory** - All potential leaks identified by type
2. **Severity Assessment** - Prioritized by impact
3. **Fix Recommendations** - Specific code changes for each leak
4. **Verification Guide** - How to confirm leaks are fixed

---

## Techniques Used

- **ST-01** (Clear Objective): Focused leak detection
- **ST-02** (Sequential Instructions): Pattern-based detection
- **RT-04** (Best Practice Review): Memory management patterns
- **RT-05** (Evidence-Based Reasoning): Specific code locations
- **OC-05** (Severity Classification): Leak prioritization

---

## Related Prompts

- [android_performance_audit.md](../analysis/android_performance_audit.md) - Broader performance review
- [android_codebase_health_assessment.md](../analysis/android_codebase_health_assessment.md) - Overall health check

---

## Customization Guide

### For Compose Apps
- Focus on remember{} with context
- Check CompositionLocal usage
- Analyze LaunchedEffect scopes

### For Heavy Image Apps
- Focus on bitmap handling
- Check image loading library usage
- Analyze cache configurations

### For Real-time Apps
- Focus on listener/callback patterns
- Check WebSocket/streaming connections
- Analyze background processing
