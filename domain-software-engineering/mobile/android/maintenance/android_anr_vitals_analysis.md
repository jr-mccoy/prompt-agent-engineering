---
title: "Android ANR and Vitals Analysis"
category: mobile-development
description: "Diagnoses Application Not Responding (ANR) events from Android Vitals and Crashlytics — classifying ANR type, tracing main-thread blocking, and producing prioritized fixes against Play's Bad Behavior thresholds."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - android
  - maintenance
  - anr
  - performance
  - vitals
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/maintenance/android_crash_analysis.md
  - domain-software-engineering/mobile/android/maintenance/android_performance_regression_detective.md
  - domain-software-engineering/mobile/android/maintenance/android_reliability_slo_error_budget_review.md
  - domain-software-engineering/mobile/android/analysis/android_performance_audit.md
---

# Android ANR and Vitals Analysis

**Objective:** Diagnose Application Not Responding (ANR) events surfaced by Google Play Android Vitals, Firebase Crashlytics, or ANR traces — classify the ANR type, trace the main-thread blocking source, assess impact against Play's Bad Behavior thresholds, and produce prioritized, verifiable fixes.

**When to Use:** Use when the user-perceived ANR rate is elevated or approaching Play's quality bar, when Android Vitals flags an ANR cluster, or when investigating `ANR in <process>` traces. ANRs are distinct from exception crashes (use `android_crash_analysis.md` for those) — they stem from the main thread being unresponsive, not from an uncaught throwable.

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

1. **ANR source & shape:**
   - "Where is the ANR data from — Android Vitals, Crashlytics ANR section, or a raw `/data/anr/traces.txt`?"
   - "Paste the ANR trace, especially the `main` thread stack and the 'Reason' line."
   - "Is this a single cluster or several distinct ANR signatures?"

2. **Impact metrics:**
   - "What is the user-perceived ANR rate, and the overall vs. per-device-tier breakdown?"
   - "Which app version introduced or increased it? Is the trend rising, stable, or falling?"
   - "Which devices/OS versions/regions dominate? (low-RAM devices and slow storage skew ANRs)"

3. **Code & runtime context:**
   - "What was the foreground component (Activity/Service/BroadcastReceiver) at ANR time?"
   - "Are there recent changes to startup, main-thread I/O, or broadcast/service handling?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before diagnosing any ANR, you MUST:**

1. **Read the `main` thread stack first** — the ANR is defined by what the main thread was doing when it failed to respond. Identify the exact blocking frame.
2. **Classify the ANR reason** — input dispatch timeout, broadcast timeout, service (start/executing) timeout, or `ContentProvider` not responding. The reason line drives the fix.
3. **Distinguish "blocked" from "deadlocked" from "slow"** — a held lock, a binder call to a slow system service, and genuinely slow main-thread work need different fixes. Inspect other threads' states for lock owners.
4. **Quantify against the Play threshold** — state the user-perceived ANR rate and whether it exceeds Play's Bad Behavior bar (the quality bar that can suppress discoverability).
5. **Provide file:line for the app-owned blocking frame** — skip framework frames; find the first frame in app code.

### False-Positive Prevention

- ❌ Do NOT treat every ANR as "main-thread did heavy work" — many are lock contention or slow binder/IPC calls
- ❌ Do NOT recommend moving work off-main without identifying *which* work and *why* it blocks
- ❌ Do NOT ignore the device tier — ANRs concentrated on low-RAM/slow-storage devices may need adaptive behavior, not a universal rewrite
- ❌ Do NOT conflate startup ANRs with steady-state ANRs — root causes and fixes differ
- ✅ DO check for `synchronized`/lock waits held by a background thread (deadlock or contention)
- ✅ DO consider `BroadcastReceiver.onReceive` and `Service` lifecycle doing synchronous work
- ✅ DO verify a fix with on-device measurement, not just code review

---

### Phase 1: ANR Classification

Identify the ANR reason and the responsible component.

| ANR Reason | Trigger | Typical Window | Common Cause |
|------------|---------|----------------|--------------|
| Input dispatching timeout | UI unresponsive to touch/key | ~5s | Main-thread work / lock wait / slow frame |
| Broadcast timeout | `onReceive` too slow | ~10s (fg) | Sync work in receiver |
| Service timeout | `startForeground`/exec too slow | ~10-20s | Blocking service start |
| ContentProvider not responding | Slow provider | — | Heavy query on main |

**Record:**
- [ ] Reason line (verbatim)
- [ ] Foreground component + lifecycle state
- [ ] App version, device tier, OS distribution
- [ ] User-perceived ANR rate vs. Play threshold

---

### Phase 2: Main-Thread Trace Triage

Walk the `main` thread stack top-down and find the first app-owned frame.

```text
Triage questions per frame:
1. Is this frame in app code or framework code?  (find first app frame)
2. Is the thread RUNNABLE (doing work) or BLOCKED/WAITING (on a lock/IPC)?
3. If WAITING on a monitor — which thread holds it? (scan other threads)
4. Is this a binder call into a system service (e.g., PackageManager, storage)?
5. Is this I/O on main (disk, SharedPreferences.commit, DB, network)?
```

**Thread-state interpretation:**

| Main thread state | Likely category | Next step |
|-------------------|-----------------|-----------|
| RUNNABLE in app code | Slow main-thread work | Move to background / optimize algorithm |
| BLOCKED on monitor | Lock contention/deadlock | Find lock owner thread; reduce critical section |
| Native/binder wait | Slow IPC to system service | Cache result; call off-main; add timeout/fallback |
| WAITING on latch/future | Sync-over-async | Remove blocking `.get()`/`runBlocking` on main |

---

### Phase 3: Root-Cause Pattern Matching

```kotlin
// Pattern A: Synchronous I/O on main
// Symptom: main RUNNABLE in SharedPreferences/File/Room/Cursor on main
// Fix: use apply() not commit(); move DB/file reads to Dispatchers.IO

// Pattern B: Sync-over-async (the silent ANR factory)
// Symptom: runBlocking { } or future.get() on main
val data = runBlocking { repository.load() }   // blocks main → ANR on slow path
// Fix: lift to a coroutine scoped to lifecycle; render loading state

// Pattern C: Lock contention / deadlock
// Symptom: main BLOCKED on monitor held by a background thread
// Fix: shrink critical sections; avoid holding locks across I/O; prefer immutable state/StateFlow

// Pattern D: Heavy work in BroadcastReceiver.onReceive
// Symptom: ANR reason = broadcast timeout
// Fix: goAsync() + WorkManager / JobIntentService equivalent; never block onReceive

// Pattern E: Startup ANR
// Symptom: ANR within first frames; Application.onCreate / content providers
// Fix: defer init (App Startup lib / lazy), move SDK init off critical path

// Pattern F: Slow binder / system-service call
// Symptom: main in native binder transact
// Fix: cache, batch, call off-main, add fallback when service is slow
```

---

### Phase 4: Findings Presentation

**CHECKPOINT 1:** Present before implementing fixes.

```markdown
## ANR Analysis Report

### Cluster Summary
| Field | Value |
|-------|-------|
| ANR reason | [Input/Broadcast/Service/Provider] |
| Blocking frame | [file:line] |
| Main thread state | [RUNNABLE/BLOCKED/WAITING] |
| Lock owner (if any) | [thread + frame] |
| User-perceived ANR rate | [X%] (Play bar: exceeded? Y/N) |
| Dominant devices/OS | [list] |
| Introduced in | [version] · Trend: [↑/→/↓] |

### Root Cause
[Plain explanation tied to the trace]

### Pattern
[A–F from Phase 3] + evidence

**Proceed with fix, or investigate further?**
```

---

### Phase 5: Fix Implementation

**Move blocking work off the main thread (the most common fix):**

```kotlin
// Before: blocking the main thread during a lifecycle callback
override fun onResume() {
    super.onResume()
    val prefs = getSharedPreferences("p", MODE_PRIVATE)
    prefs.edit().putLong("seen", now()).commit()   // commit() = sync disk I/O
    val items = db.dao().getAllBlocking()           // sync DB query on main
    render(items)
}

// After: async + lifecycle-scoped
override fun onResume() {
    super.onResume()
    getSharedPreferences("p", MODE_PRIVATE)
        .edit().putLong("seen", now()).apply()      // async write
    viewLifecycleOwner.lifecycleScope.launch {
        val items = withContext(Dispatchers.IO) { db.dao().getAll() }
        render(items)
    }
}
```

**BroadcastReceiver doing work synchronously:**

```kotlin
// After: hand off, do not block onReceive
override fun onReceive(context: Context, intent: Intent) {
    val work = OneTimeWorkRequestBuilder<SyncWorker>().build()
    WorkManager.getInstance(context).enqueue(work)   // returns immediately
}
```

**Patterns to apply:**
- [ ] Replace `commit()` with `apply()`; move DB/file/network off main
- [ ] Remove `runBlocking`/`Future.get()` on the main thread
- [ ] Shrink or eliminate locks held across I/O; prefer `StateFlow`/immutable snapshots
- [ ] Defer non-critical startup init (App Startup / lazy)
- [ ] Cache or background slow system-service/binder calls; add timeouts/fallbacks

---

### Phase 6: Verification & Prevention

**Verify the fix actually removed the block:**
- [ ] Reproduce the prior scenario on a low-tier device; confirm no ANR
- [ ] Enable `StrictMode` (disk/network on main → penaltyLog) in debug to catch regressions
- [ ] Add a Macrobenchmark or frame-timing check on the affected flow
- [ ] Watch Android Vitals user-perceived ANR rate for the rollout window

```kotlin
// StrictMode guard in debug builds
if (BuildConfig.DEBUG) {
    StrictMode.setThreadPolicy(
        StrictMode.ThreadPolicy.Builder()
            .detectDiskReads().detectDiskWrites().detectNetwork()
            .penaltyLog().build()
    )
}
```

**Prevention checklist:**
- [ ] StrictMode in debug; CI fails on new main-thread I/O where feasible
- [ ] Lint/ban list for `commit()`, `runBlocking` on main, `.get()` on futures in UI
- [ ] ANR rate added to the reliability SLO + release gate

---

## Expected Output

1. **ANR classification** (reason + responsible component)
2. **Main-thread trace triage** (first app frame, thread state, lock owner)
3. **Root-cause pattern** (A–F) with file:line evidence
4. **Impact statement** vs. Play's user-perceived ANR threshold
5. **Prioritized fixes** with before/after code
6. **Verification plan** (device repro, StrictMode, Vitals monitoring) + prevention guardrails

---

## Techniques Used

- **ST-01** (Clear Objective): ANR-specific diagnosis scope
- **ST-02** (Sequential Instructions): Classify → trace → match → fix → verify
- **RT-02** (Multi-Dimensional Analysis): Reason, thread state, device tier, version
- **RT-05** (Evidence-Based Reasoning): Every diagnosis tied to a trace frame + metric
- **DS-02** (Structured Decision Support): Thread-state → fix-category mapping
- **QA-01** (Verification/Self-Check): Device repro + StrictMode + Vitals confirmation

---

## Related Prompts

- [android_crash_analysis.md](android_crash_analysis.md) - For exception crashes (non-ANR)
- [android_performance_regression_detective.md](android_performance_regression_detective.md) - When ANR rate rose after a release
- [android_reliability_slo_error_budget_review.md](android_reliability_slo_error_budget_review.md) - Set ANR-rate SLO + release gates
- [android_performance_audit.md](../analysis/android_performance_audit.md) - Broader main-thread/jank investigation
- [../targeted-reviews/android_workmanager_background_review.md](../targeted-reviews/android_workmanager_background_review.md) - Correct background-work offloading
- [../targeted-reviews/android_coroutine_scope_review.md](../targeted-reviews/android_coroutine_scope_review.md) - Coroutine scoping to avoid sync-over-async
