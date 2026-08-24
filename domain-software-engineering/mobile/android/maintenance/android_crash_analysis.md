---
title: "Android Crash Analysis"
category: mobile-development
description: "Analyzes crash reports and stack traces to identify root causes and provides prioritized fixes for stability issues"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-01
difficulty: advanced
tags:
  - analysis
  - android
  - mobile-development
  - crash
  - maintenance
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/maintenance/android_anr_vitals_analysis.md
  - domain-software-engineering/mobile/android/improvement/android_memory_leak_detection.md
  - domain-software-engineering/mobile/android/maintenance/android_incident_triage_and_severity_classification.md
  - domain-software-engineering/mobile/android/maintenance/android_performance_regression_detective.md
---

# Android Crash Analysis

**Objective:** Analyze crash reports from Firebase Crashlytics, Play Console, or other crash reporting tools to identify root causes, prioritize fixes, and implement solutions for production stability issues.

**When to Use:** Use this prompt when you have crash reports to investigate, whether from Crashlytics dashboards, ANR reports, Play Console crash clusters, or user-reported issues. Ideal for triaging production crashes, debugging intermittent issues, or conducting post-incident analysis. Prerequisites include access to crash reports or stack traces and the relevant source code.

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

Before beginning crash analysis, gather essential context:

1. **Crash Source:**
   - "Where are the crash reports from? (Firebase Crashlytics, Play Console, custom analytics, user reports)"
   - "Can you share the crash report, stack trace, or crash cluster details?"

2. **Crash Characteristics:**
   - "Is this a single crash or a pattern of similar crashes?"
   - "What is the crash frequency and user impact? (% of users affected)"
   - "When did this crash first appear? (specific version, date)"

3. **Environment Details:**
   - "Which Android versions and devices are affected?"
   - "Is this crash specific to certain configurations? (language, region, screen size)"
   - "Are there any common user actions preceding the crash?"

4. **Codebase Context:**
   - "Which app version(s) contain this crash?"
   - "Have there been recent changes to the affected area?"
   - "Is there any relevant logging or breadcrumb data?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before diagnosing ANY crash, you MUST:**

1. **Trace the actual stack trace** - Don't guess root causes without analyzing the complete stack trace.
2. **Check for existing fixes** - Search the codebase for recent changes that might have already addressed the issue.
3. **Understand the context** - Consider device, Android version, and user action patterns from crash reports.
4. **Confirm reproduction** - Can this crash be reproduced, or is it a one-off flake?
5. **Provide specific file:line locations** - Every diagnosis must reference exact code locations (e.g., `HomeFragment.kt:156`).

**Finding the crash is NOT reproducible is an acceptable outcome.** Some crashes are device-specific or one-time issues.

### False-Positive Prevention

- ❌ Do NOT guess root causes without stack trace analysis
- ❌ Do NOT assume all crashes need code fixes (some are OEM/device issues)
- ❌ Do NOT ignore context (device, OS version, recent changes)
- ❌ Do NOT recommend changes without verifying they address the actual crash
- ✅ DO correlate crashes with recent code changes
- ✅ DO check if crashes are device/version specific
- ✅ DO verify proposed fixes against the actual stack trace
- ✅ DO consider crash frequency when prioritizing fixes

---

### Phase 1: Crash Report Analysis

Systematically analyze the crash report to understand the failure.

#### 1.1 Stack Trace Parsing

**Decode and analyze the stack trace:**

```kotlin
// Stack trace analysis checklist:

// 1. Identify the exception type
// Common Android crashes:
// - NullPointerException: Null reference access
// - IllegalStateException: Invalid state transition
// - IllegalArgumentException: Bad parameter
// - SecurityException: Permission denied
// - OutOfMemoryError: Memory exhaustion
// - ANR (Application Not Responding): Main thread blocked

// 2. Locate the crash origin
// - Find YOUR code in the stack trace (not framework code)
// - Identify the exact file:line where crash originated
// - Trace the call path leading to the crash

// 3. Identify the context
// - What lifecycle state was the component in?
// - What user action triggered this path?
// - What data was being processed?
```

**Extract key information:**
- [ ] Exception type and message
- [ ] Originating file and line number
- [ ] Call stack leading to crash
- [ ] Thread that crashed (main, background, coroutine)
- [ ] Any obfuscation that needs deobfuscation

#### 1.2 Crash Metadata Analysis

**Analyze accompanying metadata:**

```
Metadata to examine:
├── Device Information
│   ├── Device model and manufacturer
│   ├── Android version (API level)
│   ├── RAM and storage availability
│   └── Screen configuration
├── App State
│   ├── App version code and name
│   ├── Build type (release/debug)
│   ├── Time since app start
│   └── Foreground/background state
├── User Context
│   ├── Breadcrumbs (last actions)
│   ├── Custom keys/values logged
│   └── User identifier (if available)
└── System State
    ├── Memory pressure
    ├── Battery state
    └── Network connectivity
```

**Evaluate:**
- [ ] Device distribution (isolated vs. widespread)
- [ ] Android version correlation
- [ ] Memory availability at crash time
- [ ] App version introduction point
- [ ] User action patterns

#### 1.3 Crash Pattern Recognition

**Identify common crash patterns:**

```kotlin
// Pattern 1: Null Safety Violations
// Symptoms: NullPointerException in Kotlin code
// Common causes:
// - Platform types from Java interop (String! treated as String)
// - Late-initialized properties accessed too early
// - Unsafe casts or assertions (!!)
// - Nullable returns from Android framework

// Pattern 2: Lifecycle Timing Issues
// Symptoms: IllegalStateException, "Fragment not attached"
// Common causes:
// - Accessing view after onDestroyView
// - Starting transactions after onSaveInstanceState
// - Callback firing after component destruction
// - Coroutine continuing after lifecycle end

// Pattern 3: Concurrency Issues
// Symptoms: ConcurrentModificationException, inconsistent state
// Common causes:
// - Shared mutable state without synchronization
// - Race conditions in coroutines
// - UI updates from wrong thread

// Pattern 4: Resource Exhaustion
// Symptoms: OutOfMemoryError, ANR
// Common causes:
// - Memory leaks
// - Large bitmap allocations
// - Unbounded caches
// - Main thread blocking

// Pattern 5: Configuration Change Crashes
// Symptoms: Crashes after rotation, locale change
// Common causes:
// - View references held across config change
// - Non-parcelable data in savedInstanceState
// - Resource ID changes
```

---

### Phase 2: Root Cause Investigation

Deep dive into the codebase to identify the root cause.

#### 2.1 Code Path Analysis

**Trace the execution path:**

```kotlin
// For each method in the stack trace:

// 1. Read the source code at the crash location
// 2. Identify all possible paths to this code
// 3. Determine what conditions cause the crash
// 4. Map data flow to the crash point

// Questions to answer:
// - What value caused the crash? (null, invalid state, etc.)
// - Where did that value come from?
// - Why was the value unexpected?
// - What should the value have been?
```

**Examine:**
- [ ] The crashing method and its callers
- [ ] Data models involved in the crash
- [ ] State management for the affected component
- [ ] Error handling (or lack thereof) in the path
- [ ] Recent changes to the affected code

#### 2.2 Reproduce the Scenario

**Identify reproduction conditions:**

```kotlin
// Build a reproduction hypothesis:

// 1. User Journey
// What sequence of actions leads to the crash?
// Example: "Open app → Navigate to Profile → Edit Photo → Rotate device"

// 2. Data State
// What specific data triggers the crash?
// Example: "User with no profile photo, account created before v2.0"

// 3. Timing Conditions
// What timing is required?
// Example: "Rapid navigation before previous screen finishes loading"

// 4. Device/OS Conditions
// What environment triggers the crash?
// Example: "Android 11+ with restricted background activity"
```

**Document:**
- [ ] Minimum steps to reproduce
- [ ] Required data state
- [ ] Timing dependencies
- [ ] Device/OS requirements

#### 2.3 Impact Assessment

**Evaluate crash impact:**

```markdown
## Crash Impact Assessment

### Severity Score: [Critical/High/Medium/Low]

### User Impact
- Affected Users: [X%] of DAU
- Crash-Free Rate Impact: [X.XX%] → [X.XX%]
- User Journey Blocked: [Description of blocked functionality]

### Business Impact
- Revenue Impact: [If applicable - e.g., checkout flow affected]
- User Retention Risk: [High/Medium/Low]
- App Store Rating Risk: [High/Medium/Low]

### Stability Metrics
- Crash Occurrences: [X] in last [timeframe]
- Trend: [Increasing/Stable/Decreasing]
- First Seen: [Version/Date]
```

---

### Phase 3: Findings Presentation

**CHECKPOINT 1:** Present the crash analysis findings.

```markdown
## Crash Analysis Report

### Crash Summary
| Field | Value |
|-------|-------|
| Exception | [Type]: [Message] |
| Location | [file:line] |
| First Seen | [Version/Date] |
| Occurrences | [Count] in [Timeframe] |
| Users Affected | [X%] |
| Severity | [Critical/High/Medium/Low] |

### Root Cause
[Clear explanation of why the crash occurs]

### Crash Flow
```
[User Action] → [Code Path] → [Failure Point]
Example: "Photo selection → ImageProcessor.compress() → Bitmap.createScaledBitmap() → OOM"
```

### Contributing Factors
1. [Primary cause with evidence]
2. [Secondary factor if applicable]
3. [Environmental condition if relevant]

### Affected Code
```kotlin
// Snippet showing the problematic code
[File: path/to/file.kt:123]
```

### Reproduction Steps
1. [Step 1]
2. [Step 2]
3. [Crash occurs]

**Would you like me to proceed with the fix implementation, or do you need more investigation?**
```

---

### Phase 4: Fix Implementation

Implement robust fixes for identified crashes.

#### 4.1 Null Safety Fixes

**For NullPointerException crashes:**

```kotlin
// Before: Unsafe code
fun processUser(user: User?) {
    val name = user!!.name  // Crash when user is null
    displayName(name)
}

// After: Safe code with proper handling
fun processUser(user: User?) {
    val name = user?.name ?: run {
        logWarning("processUser called with null user")
        return  // or provide default behavior
    }
    displayName(name)
}

// Alternative: Require non-null at API boundary
fun processUser(user: User) {
    // Crash is now caller's responsibility
    displayName(user.name)
}
```

**Patterns to apply:**
- [ ] Replace `!!` with safe alternatives
- [ ] Add null checks at API boundaries
- [ ] Use `requireNotNull()` with clear messages
- [ ] Implement proper default/fallback behavior

#### 4.2 Lifecycle Safety Fixes

**For lifecycle-related crashes:**

```kotlin
// Before: Unsafe fragment access
class MyFragment : Fragment() {
    private val viewModel: MyViewModel by viewModels()

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        viewModel.data.observe(viewLifecycleOwner) { data ->
            // Potentially crashes if view is destroyed during update
            binding.textView.text = data.title
        }

        lifecycleScope.launch {
            val result = api.fetchData()
            // Crash: Fragment may not be attached
            binding.textView.text = result.title
        }
    }
}

// After: Lifecycle-safe code
class MyFragment : Fragment() {
    private val viewModel: MyViewModel by viewModels()
    private var _binding: FragmentMyBinding? = null
    private val binding get() = _binding!!

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        _binding = FragmentMyBinding.bind(view)

        // Safe: Uses viewLifecycleOwner
        viewModel.data.observe(viewLifecycleOwner) { data ->
            binding.textView.text = data.title
        }

        // Safe: Uses viewLifecycleOwner.lifecycleScope
        viewLifecycleOwner.lifecycleScope.launch {
            val result = api.fetchData()
            // Only runs if view is still alive
            binding.textView.text = result.title
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null  // Prevent leaks
    }
}
```

**Patterns to apply:**
- [ ] Use `viewLifecycleOwner` for view-related observations
- [ ] Scope coroutines to appropriate lifecycle
- [ ] Clear view references in `onDestroyView`
- [ ] Check `isAdded`/`isResumed` before fragment transactions

#### 4.3 Concurrency Fixes

**For race condition crashes:**

```kotlin
// Before: Unsafe shared state
class DataRepository {
    private val cache = mutableListOf<Item>()

    suspend fun loadItems(): List<Item> {
        val items = api.fetchItems()
        cache.clear()  // Race condition with other threads
        cache.addAll(items)
        return cache.toList()
    }
}

// After: Thread-safe implementation
class DataRepository {
    private val cache = ConcurrentHashMap<String, Item>()
    private val mutex = Mutex()

    suspend fun loadItems(): List<Item> = mutex.withLock {
        val items = api.fetchItems()
        cache.clear()
        items.forEach { cache[it.id] = it }
        cache.values.toList()
    }

    // Alternative: Use StateFlow for reactive updates
    private val _items = MutableStateFlow<List<Item>>(emptyList())
    val items: StateFlow<List<Item>> = _items.asStateFlow()

    suspend fun refreshItems() {
        val items = api.fetchItems()
        _items.value = items  // Atomic update
    }
}
```

#### 4.4 Memory Crash Fixes

**For OutOfMemoryError crashes:**

```kotlin
// Before: Unbounded memory usage
class ImageProcessor {
    fun loadLargeImage(uri: Uri): Bitmap {
        return BitmapFactory.decodeStream(
            contentResolver.openInputStream(uri)
        )  // Can crash with large images
    }
}

// After: Memory-conscious implementation
class ImageProcessor {
    fun loadLargeImage(uri: Uri, maxWidth: Int, maxHeight: Int): Bitmap? {
        return try {
            // First, decode bounds only
            val options = BitmapFactory.Options().apply {
                inJustDecodeBounds = true
            }
            contentResolver.openInputStream(uri)?.use { stream ->
                BitmapFactory.decodeStream(stream, null, options)
            }

            // Calculate sample size
            options.apply {
                inSampleSize = calculateInSampleSize(
                    outWidth, outHeight, maxWidth, maxHeight
                )
                inJustDecodeBounds = false
            }

            // Decode with subsampling
            contentResolver.openInputStream(uri)?.use { stream ->
                BitmapFactory.decodeStream(stream, null, options)
            }
        } catch (e: OutOfMemoryError) {
            Log.e(TAG, "OOM while loading image", e)
            null
        }
    }

    private fun calculateInSampleSize(
        width: Int, height: Int,
        reqWidth: Int, reqHeight: Int
    ): Int {
        var inSampleSize = 1
        if (height > reqHeight || width > reqWidth) {
            val halfHeight = height / 2
            val halfWidth = width / 2
            while (halfHeight / inSampleSize >= reqHeight &&
                   halfWidth / inSampleSize >= reqWidth) {
                inSampleSize *= 2
            }
        }
        return inSampleSize
    }
}
```

#### 4.5 ANR Fixes

**For Application Not Responding issues:**

```kotlin
// Before: Main thread blocking
class SearchActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val results = database.searchItems(query)  // Blocks main thread
        displayResults(results)
    }
}

// After: Proper async handling
class SearchActivity : AppCompatActivity() {
    private val viewModel: SearchViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Show loading immediately
        showLoading()

        // Observe results reactively
        lifecycleScope.launch {
            viewModel.searchResults.collect { state ->
                when (state) {
                    is SearchState.Loading -> showLoading()
                    is SearchState.Success -> displayResults(state.results)
                    is SearchState.Error -> showError(state.message)
                }
            }
        }

        // Trigger search
        viewModel.search(query)
    }
}

class SearchViewModel(
    private val repository: SearchRepository
) : ViewModel() {
    private val _searchResults = MutableStateFlow<SearchState>(SearchState.Loading)
    val searchResults: StateFlow<SearchState> = _searchResults.asStateFlow()

    fun search(query: String) {
        viewModelScope.launch {
            _searchResults.value = SearchState.Loading
            try {
                val results = withContext(Dispatchers.IO) {
                    repository.search(query)  // Off main thread
                }
                _searchResults.value = SearchState.Success(results)
            } catch (e: Exception) {
                _searchResults.value = SearchState.Error(e.message ?: "Search failed")
            }
        }
    }
}
```

---

### Phase 5: Verification & Prevention

Ensure the fix works and prevent regression.

#### 5.1 Fix Verification

**Verify the crash is resolved:**

```kotlin
// 1. Write a unit test for the fix
@Test
fun `processUser handles null user gracefully`() {
    val processor = UserProcessor()

    // Should not throw
    val result = processor.processUser(null)

    assertThat(result).isNull()  // or expected default
}

// 2. Write a regression test
@Test
fun `fragment survives configuration change without crash`() {
    val scenario = launchFragmentInContainer<MyFragment>()

    // Trigger the previously crashing scenario
    scenario.onFragment { fragment ->
        fragment.loadData()
    }

    // Simulate rotation
    scenario.recreate()

    // Should not crash
    scenario.onFragment { fragment ->
        assertThat(fragment.isAdded).isTrue()
    }
}
```

**Verification checklist:**
- [ ] Unit test covers the crash scenario
- [ ] Manual reproduction no longer crashes
- [ ] Edge cases are handled
- [ ] Fix doesn't introduce new issues

#### 5.2 Crash Monitoring Setup

**Enhance crash monitoring:**

```kotlin
// Add breadcrumbs for better debugging
class MyFragment : Fragment() {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        FirebaseCrashlytics.getInstance().log("MyFragment: onViewCreated")

        binding.button.setOnClickListener {
            FirebaseCrashlytics.getInstance().log("MyFragment: button clicked")
            performAction()
        }
    }
}

// Add custom keys for context
FirebaseCrashlytics.getInstance().apply {
    setCustomKey("user_type", user.accountType)
    setCustomKey("feature_enabled", isFeatureEnabled)
    setCustomKey("data_count", items.size)
}

// Add non-fatal error logging
try {
    riskyOperation()
} catch (e: Exception) {
    FirebaseCrashlytics.getInstance().recordException(e)
    // Handle gracefully
}
```

#### 5.3 Prevention Measures

**Implement preventive measures:**

```kotlin
// 1. Add lint rules for common issues
// custom-lint-rules/NullSafetyChecks.kt

// 2. Add static analysis
// build.gradle.kts
android {
    lint {
        warningsAsErrors = true
        abortOnError = true
        checkDependencies = true
    }
}

// 3. Add pre-commit hooks for crash-prone patterns
// .pre-commit-config.yaml
- repo: local
  hooks:
    - id: check-double-bang
      name: Check for !! operators
      entry: grep -r "!!" --include="*.kt"
      language: system
      types: [kotlin]
```

---

## Expected Output

### Crash Analysis Report Format

```markdown
# Crash Analysis Report

## Executive Summary
- **Crash:** [Exception type and brief description]
- **Root Cause:** [One sentence explanation]
- **Severity:** [Critical/High/Medium/Low]
- **Fix Status:** [Identified/In Progress/Fixed/Verified]

## Crash Details
### Stack Trace (Deobfuscated)
```
[Full stack trace with your code highlighted]
```

### Occurrence Data
| Metric | Value |
|--------|-------|
| First Seen | [Date/Version] |
| Total Occurrences | [Count] |
| Affected Users | [Count/Percentage] |
| Affected Versions | [List] |
| Top Devices | [List] |
| Top OS Versions | [List] |

## Root Cause Analysis
[Detailed explanation of why the crash occurs, with code references]

## Fix Implementation
### Changes Made
| File | Change Description |
|------|-------------------|
| [path/file.kt:line] | [Description of change] |

### Code Changes
```kotlin
// Before
[problematic code]

// After
[fixed code]
```

## Verification
- [ ] Unit tests added
- [ ] Manual testing passed
- [ ] Fix deployed to [environment]
- [ ] Crash rate monitored for [duration]

## Prevention
- [Actions taken to prevent similar crashes]
```

---

## Example Interaction

**User:** We're seeing a spike in crashes in our latest release. Here's the crash from Crashlytics:

```
java.lang.NullPointerException: Attempt to invoke virtual method 'void android.widget.TextView.setText(java.lang.CharSequence)' on a null object reference
    at com.myapp.ui.profile.ProfileFragment.updateUI(ProfileFragment.kt:87)
    at com.myapp.ui.profile.ProfileFragment.access$updateUI(ProfileFragment.kt:23)
    at com.myapp.ui.profile.ProfileFragment$loadProfile$1.invokeSuspend(ProfileFragment.kt:56)
```

**Agent:** I'll analyze this crash. Let me start by examining the crash details and then investigate the code.

*[Agent examines ProfileFragment.kt and related files]*

## Crash Analysis

### Stack Trace Analysis
- **Exception:** NullPointerException - TextView.setText() called on null reference
- **Location:** `ProfileFragment.kt:87` in `updateUI()` method
- **Trigger:** Coroutine callback from `loadProfile()` at line 56

### Root Cause Identified

The crash occurs because `updateUI()` is called from a coroutine that outlives the Fragment's view:

```kotlin
// ProfileFragment.kt:52-60
fun loadProfile() {
    lifecycleScope.launch {  // Problem: Uses fragment's lifecycleScope
        val profile = repository.getProfile()
        updateUI(profile)  // Called after view destruction
    }
}

// ProfileFragment.kt:85-90
private fun updateUI(profile: Profile) {
    binding.nameTextView.text = profile.name  // Line 87 - binding is null
}
```

**The issue:** `lifecycleScope` is tied to the Fragment's lifecycle, not the view's lifecycle. If the user navigates away while `getProfile()` is in progress, the coroutine continues and calls `updateUI()` after `onDestroyView()`, when `binding` is null.

### Device Distribution
Looking at the metadata, this affects all Android versions equally, with higher occurrence on slower devices (where the API call takes longer, increasing the timing window).

### Impact Assessment
- **Severity:** High
- **Affected Users:** ~3% of DAU
- **Crash-Free Rate:** Dropped from 99.8% to 99.2%

**Would you like me to implement the fix? The solution involves using `viewLifecycleOwner.lifecycleScope` instead of `lifecycleScope`.**

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective defining crash analysis scope
- **ST-02** (Sequential Instructions): Phased approach from analysis to fix to prevention
- **RT-02** (Multi-Dimensional Analysis): Examines code, metadata, patterns, and impact
- **RT-05** (Evidence-Based Reasoning): All findings include file:line references and data
- **ST-03** (Output Format Templates): Structured crash report and fix documentation
- **OC-05** (Severity Classification): Critical/High/Medium/Low crash severity
- **AG-02** (Skeptical Default Stance): Thorough root cause investigation
- **NE-02** (Phased Workflow): Clear checkpoints between analysis and implementation
- **NE-07** (Discussion Before Action): User approval before implementing fixes

---

## Related Prompts

- [android_memory_leak_detection.md](../improvement/android_memory_leak_detection.md) - Deep dive on memory-related crashes
- [android_error_handling_improvement.md](../improvement/android_error_handling_improvement.md) - Improve error handling to prevent crashes
- [android_test_strategy_design.md](../testing/android_test_strategy_design.md) - Add tests to prevent regressions
- [android_performance_audit.md](../analysis/android_performance_audit.md) - Investigate ANR-related issues
- [android_release_preparation.md](../publishing/android_release_preparation.md) - Pre-release crash prevention

---

## Customization Guide

### For Different Crash Reporting Tools

**Firebase Crashlytics:**
- Rich metadata and breadcrumbs
- Velocity alerts for crash spikes
- Integration with BigQuery for custom analysis

**Play Console:**
- Pre-launch reports from automated testing
- ANR clustering
- Device catalog insights

**Sentry/Bugsnag:**
- Custom tags and context
- Release tracking
- Performance monitoring integration

### For Different Crash Categories

**Native Crashes (NDK):**
- Require symbolication with .so files
- Check for memory corruption, buffer overflows
- Use Address Sanitizer for debugging

**ANR Issues:**
- Focus on main thread analysis
- Check for deadlocks and blocking calls
- Use StrictMode in development

**Multi-Process Crashes:**
- Check IPC communication
- Verify process lifecycle handling
- Examine ContentProvider implementations

### For Team Workflows

**On-Call Triage:**
- Focus on severity assessment and quick mitigation
- Document for handoff to feature team

**Sprint Planning:**
- Prioritize crashes by user impact
- Group related crashes for efficient fixing
- Include regression tests in acceptance criteria

**Post-Mortems:**
- Document timeline and impact
- Identify systemic issues
- Propose process improvements
