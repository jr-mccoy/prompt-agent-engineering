---
title: "Android Performance Regression Detective"
category: mobile-development
description: "Investigate performance regressions in Android apps — analyze Android Vitals data, correlate with releases, identify root causes through profiling and bisection, and verify fixes with benchmarks."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
difficulty: intermediate
tags:
  - android
  - maintenance
  - performance
  - profiling
  - android-vitals
  - macrobenchmark
  - solo-developer
updated: "2026-02-11"
---

# Android Performance Regression Detective

**Objective:** Systematically investigate performance regressions in an Android app — analyzing Android Vitals and internal metrics to detect degradation, correlating regressions with specific releases or code changes, using profiling tools and bisection strategies to identify root causes, and verifying that fixes actually resolve the regression through Macrobenchmark and real-device testing.

**When to Use:** Use this when Android Vitals shows degraded metrics (startup time, slow rendering, ANR rate), when users report the app "feels slower," after a release where performance wasn't benchmarked, or as a quarterly performance health check. Also use proactively before major launches to establish baselines and catch regressions before users do.

**Important context:** Performance regressions are sneaky. They rarely come from one dramatic change — they accumulate from many small ones. A new analytics SDK here, an extra database query there, a layout that's slightly deeper. This prompt treats regression investigation as detective work: gather evidence, form hypotheses, test them, and verify the fix.

---

## Context Gathering

Before investigating, gather:

1. **Symptoms:**
   - "What specific performance metric degraded? (startup time, frame rate, ANR rate, memory, battery)"
   - "When did you first notice the issue? (specific date, release version, user reports)"
   - "Does it affect all devices or specific ones? (low-end vs. flagship, specific OS versions)"

2. **Data Sources:**
   - "Do you have access to Android Vitals in Play Console?"
   - "Do you have any internal performance monitoring (Firebase Performance, custom metrics)?"
   - "Do you have existing Macrobenchmark or Microbenchmark tests?"

3. **Release History:**
   - "What changed in recent releases? (features, libraries, SDK updates)"
   - "Do you have tagged release commits in version control?"
   - "Can you build and run any previous version for comparison?"

4. **Environment:**
   - "What is your current minSdk and targetSdk?"
   - "Do you use Jetpack Compose, Views, or both?"
   - "What is your approximate APK size?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before attributing ANY regression to a specific cause, you MUST:**

1. **Reproduce the regression** — Measure the degraded metric yourself on a controlled device, not just from aggregate Vitals data. Vitals data can be noisy.
2. **Establish a baseline** — Compare against a known-good build (previous release APK or git tag), not against assumptions about what "should" be fast.
3. **Isolate the variable** — Change one thing at a time when testing hypotheses. If you update a library AND refactor code, you can't attribute the regression.
4. **Measure multiple times** — A single profiling run is not evidence. Run benchmarks at least 5 times and look at medians, not averages.
5. **Verify on representative hardware** — Profiling on a Pixel 8 Pro won't catch regressions that only appear on budget devices with 3GB RAM.

**Finding no regression on your test device does not mean there is no regression.** Low-end devices and specific OS versions may be disproportionately affected.

### False-Positive Prevention

- ❌ Do NOT blame the most recent change by default — regressions can be latent (triggered by data growth, not code change)
- ❌ Do NOT rely solely on Android Vitals percentiles — they include diverse hardware and network conditions that may not reflect your change
- ❌ Do NOT assume a slow trace profile means a problem — some operations are intentionally slow (encryption, large data sync)
- ❌ Do NOT optimize before confirming the regression exists — premature optimization wastes time
- ❌ Do NOT treat Vitals "bad behavior threshold" as a binary pass/fail — trends matter more than thresholds
- ✅ DO compare like-for-like (same device, same data set, same network conditions)
- ✅ DO check if "regression" correlates with user growth (more diverse devices = different percentiles)
- ✅ DO look at multiple metrics together (startup regression + increased APK size = likely new dependency bloat)
- ✅ DO check for data-dependent regressions (app gets slower as local database grows)
- ✅ DO verify the regression persists after clearing app data (eliminates state-related causes)

---

### Phase 1: Evidence Collection

#### 1.1 Android Vitals Dashboard Review

Pull current metrics from Play Console:

```markdown
## Android Vitals Snapshot — [App Name] [Date]

### Core Vitals
| Metric | Current | 30d Ago | 90d Ago | Threshold | Status |
|--------|---------|---------|---------|-----------|--------|
| Startup time (cold) | XXXms | XXXms | XXXms | < 1000ms | ⚠️/✅ |
| Startup time (warm) | XXXms | XXXms | XXXms | < 500ms | ⚠️/✅ |
| Slow rendering (16ms) | XX% | XX% | XX% | < 5% | ⚠️/✅ |
| Frozen frames (700ms) | XX% | XX% | XX% | < 0.5% | ⚠️/✅ |
| ANR rate | XX% | XX% | XX% | < 0.47% | ⚠️/✅ |
| Crash rate | XX% | XX% | XX% | < 1.09% | ⚠️/✅ |

### Trend Direction
| Metric | Trend | Correlation with Release? |
|--------|-------|--------------------------|
| Cold startup | ↗️ increasing since vX.Y | Yes — matches release date |
| ANR rate | → stable | No |
| Slow rendering | ↗️ gradual increase | Unclear — gradual over 3 releases |
```

#### 1.2 Release Timeline Correlation

```markdown
## Release Timeline
| Version | Release Date | Key Changes | Performance Impact Suspected |
|---------|-------------|-------------|------------------------------|
| 2.4.0 | 2026-01-15 | New onboarding flow, Firebase Analytics | Cold start +150ms |
| 2.3.2 | 2025-12-20 | Bug fixes only | None observed |
| 2.3.0 | 2025-12-01 | Room migration, new image lib | Slow rendering +2% |
| 2.2.0 | 2025-11-01 | Compose migration started | Baseline (last known good) |
```

#### 1.3 Local Baseline Measurement

Establish a controlled baseline on your test device:

```bash
# Build current version
./gradlew assembleRelease

# Build a known-good version (checkout previous tag)
git stash && git checkout v2.2.0
./gradlew assembleRelease
# Rename APK to baseline_v2.2.0.apk
git checkout main && git stash pop
```

**Manual timing (if no benchmarks exist yet):**

```bash
# Cold start timing via ADB
adb shell am force-stop com.example.app
adb shell am start-activity -W -n com.example.app/.MainActivity

# Output includes:
# TotalTime: XXXms   ← This is your cold start time
# WaitTime: XXXms

# Run 5 times each for baseline and current, record medians
```

---

### Phase 2: Regression Triage

#### 2.1 Regression Classification

Classify the regression to focus the investigation:

| Regression Type | Symptoms | Likely Causes | Investigation Path |
|----------------|----------|---------------|-------------------|
| **Startup regression** | Cold/warm start time increased | New SDKs initializing, ContentProvider overhead, heavy Application.onCreate | Profile startup trace |
| **Rendering regression** | Janky scrolling, dropped frames | Deep view hierarchies, recomposition storms, main thread work | GPU profiling, systrace |
| **ANR regression** | App Not Responding dialogs | Main thread blocked (disk I/O, network, lock contention) | ANR traces, StrictMode |
| **Memory regression** | OOM crashes, background kills | Leaks, bitmap caching, retained fragments | Heap dump, LeakCanary |
| **Battery regression** | Excessive battery use warnings | Wake locks, excessive location, background work | Battery Historian |
| **Size regression** | APK grew significantly | New dependencies, unoptimized assets, missing R8 | APK Analyzer |

#### 2.2 Quick Diagnostic Commands

```bash
# APK size comparison
ls -la app/build/outputs/apk/release/
# Compare against previous release APK size

# Method count (dex complexity)
# Use Android Studio APK Analyzer or:
unzip -l app-release.apk | grep "\.dex"

# Startup trace capture
adb shell am start -W -S --ez trace true com.example.app/.MainActivity
# Pull trace from device:
adb pull /data/local/tmp/startup_trace.perfetto-trace

# Allocation tracking during startup
adb shell setprop debug.alloctracker.enable 1
adb shell am start -W -S com.example.app/.MainActivity
```

#### 2.3 Binary Search (Bisection) Strategy

When the regression spans multiple releases:

```bash
# Use git bisect to find the exact commit
git bisect start
git bisect bad HEAD                    # Current version (slow)
git bisect good v2.2.0                 # Last known good version

# At each step:
# 1. Build: ./gradlew assembleRelease
# 2. Install: adb install -r app/build/outputs/apk/release/app-release.apk
# 3. Measure: adb shell am start-activity -W -S com.example.app/.MainActivity
# 4. Compare against threshold
# 5. Mark: git bisect good  OR  git bisect bad

# Git will narrow to the exact commit in O(log n) steps
```

**Shortcut for large histories:** If you have 200+ commits, first bisect by release tags (v2.2.0 → v2.3.0 → v2.3.2 → v2.4.0) to identify the release window, then bisect within that window.

---

### Phase 3: Root Cause Analysis

#### 3.1 Startup Profiling

```kotlin
// Add startup timing instrumentation temporarily
class MyApplication : Application() {
    override fun onCreate() {
        val startTime = SystemClock.elapsedRealtime()
        super.onCreate()

        // Log each initialization phase
        val afterSuper = SystemClock.elapsedRealtime()
        Log.d("PERF", "Application.super.onCreate: ${afterSuper - startTime}ms")

        initializeDI()
        val afterDI = SystemClock.elapsedRealtime()
        Log.d("PERF", "DI initialization: ${afterDI - afterSuper}ms")

        initializeFirebase()
        val afterFirebase = SystemClock.elapsedRealtime()
        Log.d("PERF", "Firebase init: ${afterFirebase - afterDI}ms")

        initializeAnalytics()
        val afterAnalytics = SystemClock.elapsedRealtime()
        Log.d("PERF", "Analytics init: ${afterAnalytics - afterFirebase}ms")

        val total = SystemClock.elapsedRealtime() - startTime
        Log.d("PERF", "Total Application.onCreate: ${total}ms")
    }
}
```

**Check for ContentProvider initialization overhead:**

```bash
# List all ContentProviders — each one runs before Application.onCreate
adb shell dumpsys package com.example.app | grep "Provider{"
# Many Firebase/analytics SDKs add ContentProviders for auto-init
```

```kotlin
// Defer SDK initialization to reduce startup time
// In AndroidManifest.xml — disable auto-init:
// <provider
//     android:name="com.google.firebase.provider.FirebaseInitProvider"
//     android:authorities="${applicationId}.firebaseinitprovider"
//     tools:node="remove" />

// Then initialize manually when actually needed:
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        // Don't initialize Firebase here — defer to first use
    }
}
```

#### 3.2 Rendering Profiling

```kotlin
// For Compose: detect recomposition storms
@Composable
fun MyScreen(viewModel: MyViewModel) {
    // Add recomposition counter (debug only)
    val recomposeCount = remember { mutableIntStateOf(0) }
    SideEffect {
        recomposeCount.intValue++
        Log.d("RECOMPOSE", "MyScreen recomposed: ${recomposeCount.intValue} times")
    }

    // If this logs many times per frame → unstable parameters or
    // reading frequently-changing state at too high a level
}
```

```bash
# Enable GPU rendering profiling
adb shell setprop debug.hwui.profile true
# Then navigate to the janky screen and look at the bar chart overlay

# Capture a systrace for frame analysis
python3 $ANDROID_HOME/platform-tools/systrace/systrace.py \
    --time=5 -o trace.html \
    gfx view res dalvik sched freq idle
```

#### 3.3 ANR Investigation

```bash
# Pull ANR traces from device
adb bugreport bugreport.zip
# Unzip and check:
# FS/data/anr/traces.txt — thread dumps at time of ANR

# Or check Play Console ANR clusters for patterns:
# Common causes:
# - SharedPreferences.apply() blocking main thread
# - Room queries on main thread
# - ContentProvider operations during startup
# - Binder IPC deadlocks
```

#### 3.4 Memory Investigation

```bash
# Capture heap dump
adb shell am dumpheap com.example.app /data/local/tmp/heap.hprof
adb pull /data/local/tmp/heap.hprof

# Open in Android Studio Memory Profiler or MAT
# Look for:
# - Duplicate bitmap instances (missing caching)
# - Retained Activity/Fragment references (leaks)
# - Large collections that grow unbounded
# - Context held by singletons
```

---

### Phase 4: Fix Verification

#### 4.1 Macrobenchmark Setup

Set up repeatable benchmarks to verify fixes and prevent future regressions:

```kotlin
// benchmark/build.gradle.kts
plugins {
    id("com.android.test")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.example.app.benchmark"
    compileSdk = 35
    targetProjectPath = ":app"

    defaultConfig {
        minSdk = 24
        testInstrumentationRunner = "androidx.benchmark.junit4.AndroidBenchmarkRunner"
    }

    buildTypes {
        create("benchmark") {
            isDebuggable = true
            signingConfig = signingConfigs.getByName("debug")
            matchingFallbacks += listOf("release")
        }
    }
}

dependencies {
    implementation("androidx.benchmark:benchmark-macro-junit4:1.3.3")
    implementation("androidx.test.ext:junit:1.2.1")
    implementation("androidx.test.espresso:espresso-core:3.6.1")
}
```

```kotlin
// benchmark/src/main/java/com/example/app/benchmark/StartupBenchmark.kt
@RunWith(AndroidJUnit4::class)
class StartupBenchmark {

    @get:Rule
    val benchmarkRule = MacrobenchmarkRule()

    @Test
    fun startupCold() = benchmarkRule.measureRepeated(
        packageName = "com.example.app",
        metrics = listOf(StartupTimingMetric()),
        iterations = 10,
        startupMode = StartupMode.COLD,
    ) {
        pressHome()
        startActivityAndWait()
    }

    @Test
    fun startupWarm() = benchmarkRule.measureRepeated(
        packageName = "com.example.app",
        metrics = listOf(StartupTimingMetric()),
        iterations = 10,
        startupMode = StartupMode.WARM,
    ) {
        pressHome()
        startActivityAndWait()
    }

    @Test
    fun scrollPerformance() = benchmarkRule.measureRepeated(
        packageName = "com.example.app",
        metrics = listOf(FrameTimingMetric()),
        iterations = 5,
        startupMode = StartupMode.WARM,
    ) {
        startActivityAndWait()
        // Navigate to the list screen
        device.findObject(By.text("Items")).click()
        device.waitForIdle()
        // Scroll the list
        val list = device.findObject(By.scrollable(true))
        list.setGestureMargin(device.displayWidth / 5)
        list.fling(Direction.DOWN)
        device.waitForIdle()
    }
}
```

#### 4.2 Before/After Comparison Protocol

```markdown
## Fix Verification Protocol

### Before Fix (reproduce regression)
1. Checkout the commit with the regression
2. Build release APK
3. Run benchmark suite 3 times
4. Record median values

### Apply Fix
1. Apply the fix on a branch
2. Build release APK
3. Run benchmark suite 3 times
4. Record median values

### Comparison
| Metric | Before Fix | After Fix | Improvement | Target |
|--------|-----------|-----------|-------------|--------|
| Cold start (ms) | XXX | XXX | -XX% | < 1000ms |
| Warm start (ms) | XXX | XXX | -XX% | < 500ms |
| P95 frame time (ms) | XXX | XXX | -XX% | < 16ms |
| P99 frame time (ms) | XXX | XXX | -XX% | < 32ms |

### Verification
- [ ] Regression confirmed to exist before fix
- [ ] Fix resolves the regression (median improves)
- [ ] No other metrics regressed as a side effect
- [ ] Fix tested on low-end device (not just flagship)
- [ ] Benchmark added to CI to prevent recurrence
```

#### 4.3 Regression Prevention

```yaml
# .github/workflows/benchmark.yml (GitHub Actions example)
name: Performance Benchmark
on:
  pull_request:
    branches: [main]

jobs:
  benchmark:
    runs-on: macos-latest  # macOS for hardware acceleration
    steps:
      - uses: actions/checkout@v4
      - uses: reactivecircus/android-emulator-runner@v2
        with:
          api-level: 34
          script: ./gradlew :benchmark:connectedBenchmarkAndroidTest
      - name: Compare results
        run: |
          # Compare against stored baselines
          python scripts/compare_benchmarks.py \
            --baseline benchmarks/baseline.json \
            --current benchmark/build/outputs/connected_android_test_additional_output/
```

---

## Expected Output

```markdown
# Performance Regression Report — [App Name]
**Date:** YYYY-MM-DD
**Trigger:** [Android Vitals alert / User report / Quarterly check]

## Executive Summary
[1-2 sentences: what regressed, by how much, identified cause, recommended fix]

## Regression Evidence
| Metric | Baseline (vX.Y) | Current (vX.Z) | Delta | Severity |
|--------|-----------------|-----------------|-------|----------|
| [metric] | [value] | [value] | [+/-XX%] | [P0-P3] |

## Root Cause
**Commit:** [hash] "[commit message]"
**Mechanism:** [How this change causes the regression]
**Evidence:** [Profiling data, traces, benchmarks supporting this conclusion]

## Recommended Fix
[Specific code changes with file paths and line numbers]

## Verification Plan
[Benchmark commands, expected improvement, devices to test on]

## Prevention
[CI benchmark addition, monitoring threshold, code review checklist item]
```

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **ST-01: Structured Taxonomy** | Regressions classified by type (startup, rendering, ANR, memory, battery, size) with distinct investigation paths |
| **ST-02: Decision Matrices** | Priority and severity matrices drive investigation order and fix urgency |
| **RT-02: Verification Gates** | Every hypothesis must be verified with measurement before and after, not just assumed |
| **CM-01: Context Mapping** | Regression correlated with release timeline, code changes, and device distribution |
| **DS-06: Output Templates** | Standardized regression report format for consistent documentation |

---

## Related Prompts

- **[android_dependency_audit.md](android_dependency_audit.md)** — New dependencies are a common source of performance regression; audit may reveal the culprit
- **[android_tech_debt_triage.md](android_tech_debt_triage.md)** — Recurring performance regressions indicate architectural tech debt that should be triaged
- **[android_proguard_r8_optimization.md](android_proguard_r8_optimization.md)** — R8 optimization directly affects APK size and startup time regressions
- **[../../analysis/performance/performance_bottleneck_identification.md](../../../analysis/performance/performance_bottleneck_identification.md)** — General performance bottleneck analysis for deeper investigation
- **../../testing/testing_performance_benchmarks.md** — Establishing ongoing performance test suites to prevent future regressions

---

## Customization Guide

1. **Compose-heavy app variant:** Add specific sections for recomposition profiling using Layout Inspector's recomposition counts, stability analysis with the Compose compiler reports, and `remember`/`derivedStateOf` optimization patterns.

2. **Startup-focused variant:** Expand Phase 3.1 into its own deep-dive with App Startup library analysis, tracing each ContentProvider, Dagger/Hilt initialization time, and baseline profile generation.

3. **Low-end device variant:** Add a device tier matrix (budget/mid/flagship), memory pressure simulation, and specific thresholds for low-RAM devices (< 4GB). Include `isLowRamDevice` check patterns.

4. **CI integration variant:** Focus Phase 4.3 on continuous benchmarking in CI/CD, including baseline management, statistical significance testing, and automatic PR commenting with benchmark results.

5. **Battery regression variant:** Expand with Battery Historian analysis, wake lock auditing, WorkManager scheduling review, and location request frequency analysis.
