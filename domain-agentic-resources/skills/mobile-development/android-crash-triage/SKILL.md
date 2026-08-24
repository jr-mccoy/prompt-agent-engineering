---
name: android-crash-triage
description: "Systematic crash investigation workflow covering reproduction from stack traces, device/OS isolation, root cause analysis for ANRs, OOMs, and native crashes, and fix production with regression tests. Use this skill when triaging production crashes, investigating Crashlytics reports, diagnosing ANRs, debugging OOM errors, or when a developer mentions 'crash', 'ANR', 'stack trace', 'Crashlytics', or 'production issue'."
metadata:
  tags:
    - android
    - crash
    - debugging
    - crashlytics
    - solo-developer
  updated: "2026-02-12"
---

# Android Crash Triage

Systematic crash investigation workflow for Android applications. Guides a developer through reproducing crashes from stack traces, isolating device/OS combinations, identifying root cause patterns (ANRs, OOMs, native crashes), implementing fixes with regression tests, and preventing recurrence.

## Purpose

Production crashes are the highest-priority issues for any Android app — they directly impact crash-free rate (target: >99.5%), store rating, and user retention. This skill provides a structured investigation process that prevents the common trap of guessing at fixes without understanding root causes. For solo developers, a systematic approach is essential because there is no team to bounce ideas off.

## When to Use This Skill

Use this skill when you need to:
- Investigate a production crash reported in Firebase Crashlytics
- Diagnose an ANR (Application Not Responding) issue
- Debug an OOM (OutOfMemoryError) or native crash
- Prioritize which crashes to fix first based on impact
- Write regression tests to prevent crash recurrence
- Respond to a spike in crash-free rate drop

## When NOT to Use This Skill

Do NOT use this skill when:
- Debugging a development-time crash (use standard debugging tools)
- The crash is in a third-party SDK you don't control (file a bug with the SDK)
- You need to set up Crashlytics from scratch (use the Crashlytics workflow prompt)
- The issue is a performance problem, not a crash (use performance regression detective)

## Prerequisites

- Firebase Crashlytics configured and receiving crash reports
- ProGuard/R8 mapping file uploaded for deobfuscation
- Access to crash logs (Crashlytics, Play Console, or logcat)
- Test devices spanning Android versions your app supports

## Step 1: Crash Assessment and Prioritization

### 1.1 Gather Crash Data

From Crashlytics, collect for the target crash:
- **Crash cluster ID** and title
- **Stack trace** (deobfuscated)
- **Crash count** and **affected users count**
- **Crash-free rate impact** (what % of sessions crash?)
- **Device distribution** (is it all devices or specific models?)
- **OS version distribution** (is it all versions or specific API levels?)
- **App version** (which release introduced it?)
- **Frequency trend** (increasing, stable, decreasing?)

### 1.2 Priority Classification

| Priority | Criteria | Response Time |
|----------|----------|---------------|
| **P0 — Critical** | Crash-free rate < 99%, affects >10% of users, data loss risk | Fix immediately, hotfix release |
| **P1 — High** | Affects >1% of users, core feature, increasing trend | Fix in next release |
| **P2 — Medium** | Affects <1% of users, non-core feature, stable trend | Schedule in next sprint |
| **P3 — Low** | Affects <0.1% of users, edge case, single device model | Backlog |

### 1.3 Crash Type Classification

| Type | Indicators | Common Causes |
|------|-----------|---------------|
| **NullPointerException** | `NullPointerException` in stack trace | Missing null checks, lifecycle timing, uninitialized lateinit |
| **IllegalStateException** | `IllegalStateException` in stack trace | Fragment transaction after onSaveInstanceState, wrong lifecycle state |
| **ANR** | "Application Not Responding" | Main thread blocked, long database queries, synchronous network calls |
| **OOM** | `OutOfMemoryError` | Image loading without caching, memory leaks, large allocations |
| **Native Crash** | Signal 11 (SIGSEGV), tombstone | NDK issues, corrupted native memory, third-party native libraries |
| **SecurityException** | `SecurityException` | Missing runtime permission, wrong permission declaration |
| **TransactionTooLargeException** | `TransactionTooLargeException` | Bundle > 1MB in savedInstanceState, large Intent extras |

## Step 2: Root Cause Analysis

### 2.1 Stack Trace Analysis

```
Read the stack trace bottom-up:
1. Find YOUR code (not framework/library code) — this is the entry point
2. Identify the failing line and the operation being performed
3. Check the exception type and message for clues
4. Look at the thread name — is this the main thread? A coroutine? A background thread?
5. Check the "caused by" chain — the root cause is usually the deepest "Caused by"
```

### 2.2 Device/OS Isolation

Check if the crash correlates with:
- **Specific Android version:** May indicate API behavior change (e.g., scoped storage on Android 11+)
- **Specific manufacturer:** May indicate OEM customization issue (Samsung, Xiaomi, Huawei)
- **Specific device:** May indicate hardware limitation (low RAM, specific GPU)
- **Specific locale/region:** May indicate localization issue
- **App version:** May indicate regression from specific release

### 2.3 Reproduction Strategy

1. **Exact reproduction:** Same device model, same OS version, same app version, same steps
2. **Minimal reproduction:** Simplify to the fewest steps that trigger the crash
3. **Stress reproduction:** If intermittent, add stress (low memory, airplane mode toggle, rapid rotation)
4. **Automated reproduction:** Write an instrumented test that triggers the condition

If the crash is not reproducible:
- Check if it requires specific state (first launch, logged out, specific data)
- Check if it is timing-dependent (race condition between coroutines)
- Check if it requires specific hardware (camera, NFC, biometrics)
- Add additional logging around the crash site and ship in next release

## Step 3: Fix Implementation

### 3.1 Fix Patterns by Crash Type

**NullPointerException:**
```kotlin
// BAD: Crash if user is null
val name = user.name

// GOOD: Safe call with fallback
val name = user?.name ?: "Unknown"

// BEST: Fix the root cause — why is user null?
// Check: Is this a lifecycle issue? Is the data not loaded yet?
```

**ANR (main thread blocked):**
```kotlin
// BAD: Database query on main thread
val items = database.getItems()

// GOOD: Move to background with coroutines
viewModelScope.launch {
    val items = withContext(Dispatchers.IO) { database.getItems() }
    _uiState.value = items
}
```

**OOM (memory leak):**
```kotlin
// BAD: Activity reference in singleton
object ImageCache {
    var context: Context? = null  // Leaks Activity!
}

// GOOD: Use Application context
object ImageCache {
    lateinit var context: Context  // Application context only
    fun init(appContext: Context) {
        context = appContext.applicationContext
    }
}
```

### 3.2 Fix Verification

Before committing the fix:
- [ ] The crash is reproducible (you can trigger it on demand)
- [ ] The fix prevents the crash (verified on a test device)
- [ ] The fix does not introduce new issues (existing tests pass)
- [ ] The fix handles the root cause, not just the symptom

## Step 4: Regression Test

Write a test that would have caught this crash:

```kotlin
@Test
fun `settings screen survives rotation`() {
    // This crash was caused by accessing a destroyed ViewModel after rotation
    val scenario = launchActivity<SettingsActivity>()
    scenario.recreate()  // Simulate rotation
    scenario.onActivity { activity ->
        // Verify the screen is in a valid state
        assertNotNull(activity.findViewById<ComposeView>(R.id.compose_view))
    }
}
```

For ANRs, verify the fix with StrictMode:
```kotlin
StrictMode.setThreadPolicy(
    StrictMode.ThreadPolicy.Builder()
        .detectDiskReads()
        .detectDiskWrites()
        .detectNetwork()
        .penaltyDeath()  // Crash instead of ANR — makes it testable
        .build()
)
```

## Step 5: Post-Fix Monitoring

After deploying the fix:
- [ ] Monitor Crashlytics — the crash cluster count should stop growing
- [ ] Check crash-free rate trend — should improve within 24-48 hours
- [ ] Verify no new crash clusters appeared (fix didn't introduce regression)
- [ ] Update crash triage log with resolution details

## Crash Triage Log Template

```markdown
| Date | Crash ID | Type | Priority | Users Affected | Root Cause | Fix | Version Fixed | Regression Test |
|------|----------|------|----------|---------------|------------|-----|---------------|-----------------|
| 2026-02-12 | #1234 | NPE | P1 | 2,340 | Null user after process death | Added SavedStateHandle | v2.3.2 | SettingsViewModelTest#testProcessDeath |
```

## Related Skills

- `android-release-pipeline` - For shipping the crash fix
- `android-quarterly-maintenance` - For quarterly crash rate review
- `android-testing-patterns` - For comprehensive test coverage to prevent crashes
