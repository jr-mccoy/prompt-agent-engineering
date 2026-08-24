---
title: "iOS Crash Analysis"
category: mobile-development
description: "Analyze crash reports from Xcode Organizer with symbolication, stack trace analysis, crash clustering, root cause identification, and fix verification for production iOS applications."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - AG-02
difficulty: advanced
tags:
  - ios
  - swift
  - crashes
  - debugging
  - xcode-organizer
updated: "2026-03-20"
---

# iOS Crash Analysis

**Objective:** Analyze crash reports from Xcode Organizer, symbolicate stack traces, cluster related crashes, identify root causes, and verify fixes to reduce crash-free user rates in production iOS applications.

**When to Use:** Use this prompt when investigating production crashes from Xcode Organizer, TestFlight, or third-party crash reporting tools (Firebase Crashlytics, Sentry). Ideal after a release shows increased crash rates or when triaging top crashers for a stability sprint.

**Prompt Type:** Comprehensive (400+ lines)

---

## Context Gathering

Before analyzing crashes, gather essential context:

1. **Crash Source:**
   - "Where are crash reports coming from (Xcode Organizer, Crashlytics, Sentry, TestFlight)?"
   - "What is the current crash-free user rate?"
   - "Which app version(s) are affected?"

2. **Environment:**
   - "What iOS versions are your users on (check Xcode Organizer > Metrics)?"
   - "What device types show the highest crash rates?"
   - "Is the crash reproducible in development or only in production?"

3. **Recent Changes:**
   - "What changed in the most recent release?"
   - "Were there dependency updates, new features, or infrastructure changes?"
   - "Are crashes concentrated in new code or existing code paths?"

4. **Existing Diagnostics:**
   - "Are dSYMs uploaded for the affected build?"
   - "Is MetricKit integrated for additional diagnostic data?"
   - "Are there related logs from os_log or your logging framework?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before analyzing ANY crash report, you MUST:**

1. **Confirm symbolication status** - Unsymbolicated crash logs are nearly useless. Verify dSYMs are available for the exact build UUID.
2. **Identify the crash type** - Distinguish between Mach exceptions, Swift runtime errors, watchdog terminations, and memory pressure kills.
3. **Check crash frequency** - A crash affecting 0.01% of sessions requires different urgency than one affecting 5%.
4. **Correlate with release timeline** - Determine if the crash is new, regressed, or longstanding.
5. **Provide actionable fixes** - Every root cause identification MUST include a concrete code-level fix with file paths.

**Accurate diagnosis requires complete symbolication. Never guess at function names from addresses.**

### False-Positive Prevention

- ❌ Do NOT assume a crash is a regression without checking previous version crash data
- ❌ Do NOT blame third-party SDKs without evidence in the stack trace
- ❌ Do NOT recommend fixes that only suppress symptoms (e.g., wrapping everything in try/catch)
- ❌ Do NOT ignore the crashed thread - focus analysis on thread 0 or the thread marked as crashed
- ❌ Do NOT conflate correlation with causation in crash clustering
- ✅ DO verify the crash log is fully symbolicated before analysis
- ✅ DO check for multiple crash signatures that share a root cause
- ✅ DO consider device-specific and OS-specific factors
- ✅ DO provide severity ratings based on frequency and user impact
- ✅ DO include regression test recommendations with every fix

---

### Phase 1: Crash Report Reading & Symbolication

#### 1.1 Understanding the Crash Log Structure

A crash report has these critical sections:

```
Header:
  Incident Identifier:  B3A2F1C4-...
  Hardware Model:       iPhone14,5
  Process:              MyApp [1234]
  OS Version:           iPhone OS 17.2 (21C62)
  Exception Type:       EXC_BAD_ACCESS (SIGSEGV)    <-- Crash type
  Exception Subtype:    KERN_INVALID_ADDRESS at 0x0  <-- Null pointer
  Triggered by Thread:  0                            <-- Which thread crashed

Thread 0 Crashed:
  0  MyApp        0x0000000104a2f3c8 ViewModel.loadData() + 124  (ViewModel.swift:47)
  1  MyApp        0x0000000104a2e1a0 HomeScreen.body.getter + 88  (HomeScreen.swift:23)
  2  SwiftUI      0x00000001a4f2c340 ...
```

Key fields to examine:
- **Exception Type**: `EXC_BAD_ACCESS`, `EXC_CRASH (SIGABRT)`, `EXC_BREAKPOINT (SIGTRAP)`
- **Exception Subtype**: `KERN_INVALID_ADDRESS`, `KERN_PROTECTION_FAILURE`
- **Termination Reason**: Namespace and code for watchdog/memory kills
- **Crashed Thread**: The thread where the crash occurred

#### 1.2 Symbolication Verification

```bash
# Verify dSYM matches the binary UUID
dwarfdump --uuid MyApp.app.dSYM
dwarfdump --uuid MyApp.app/MyApp

# Manually symbolicate an address
atos -arch arm64 -o MyApp.app.dSYM/Contents/Resources/DWARF/MyApp -l 0x104a20000 0x104a2f3c8

# Check Xcode Organizer for automatic symbolication
# Xcode > Window > Organizer > Crashes
```

#### 1.3 Common Crash Types & Their Meanings

| Exception Type | Meaning | Common Causes |
|---|---|---|
| `EXC_BAD_ACCESS (SIGSEGV)` | Invalid memory access | Force-unwrapped nil, dangling pointer, use-after-free |
| `EXC_BAD_ACCESS (SIGBUS)` | Misaligned memory access | Corrupt data, alignment issues |
| `EXC_CRASH (SIGABRT)` | Deliberate abort | `fatalError()`, assertion failure, uncaught exception |
| `EXC_BREAKPOINT (SIGTRAP)` | Trace/breakpoint trap | Swift runtime error, implicitly unwrapped nil |
| `EXC_RESOURCE` | Resource limit exceeded | CPU/memory/disk limits |
| `EXC_GUARD` | Guarded resource violation | Using invalidated file descriptor |
| Watchdog termination | App took too long | Main thread blocked, slow launch, background timeout |

---

### Phase 2: Common Crash Patterns

**CHECKPOINT 1:** Confirm crash report is symbolicated and crash type is identified before proceeding.

```markdown
## Crash Report Triage

| Field | Value |
|-------|-------|
| Exception Type | [e.g., EXC_BREAKPOINT] |
| Crashed Thread | [e.g., Thread 0] |
| Symbolicated | [Yes/No] |
| Affected Version(s) | [e.g., 3.2.1] |
| Frequency | [e.g., 1,200 occurrences / 50K users] |

**Proceed with root cause analysis?**
```

#### 2.1 Nil Force-Unwrap Crashes

**Signature:** `EXC_BREAKPOINT (SIGTRAP)` + Swift runtime in stack

```swift
// CRASH: Force unwrapping nil optional
let user = userDict["current"] as! User  // Crashes if key missing or wrong type

// FIX: Safe unwrapping with fallback
guard let user = userDict["current"] as? User else {
    Logger.error("Missing current user in userDict")
    return
}
```

**Detection pattern in codebase:**
```bash
# Find force unwraps in Swift files
grep -rn '!\.' --include="*.swift" Sources/
grep -rn 'as!' --include="*.swift" Sources/
grep -rn '\.first!' --include="*.swift" Sources/
```

#### 2.2 Index Out of Range

**Signature:** `EXC_BREAKPOINT (SIGTRAP)` + `Swift runtime error: Index out of range`

```swift
// CRASH: Direct array subscript without bounds check
let item = items[selectedIndex]  // Crashes if selectedIndex >= items.count

// FIX: Safe subscript or bounds check
extension Collection {
    subscript(safe index: Index) -> Element? {
        indices.contains(index) ? self[index] : nil
    }
}

guard let item = items[safe: selectedIndex] else {
    Logger.warning("Index \(selectedIndex) out of range for items (count: \(items.count))")
    return
}
```

#### 2.3 Main Thread Violations

**Signature:** Watchdog termination or `EXC_CRASH` with UI framework in stack from background thread

```swift
// CRASH: Updating UI from background thread
DispatchQueue.global().async {
    let data = self.processData()
    self.tableView.reloadData()  // Main thread violation
}

// FIX: Dispatch to main or use @MainActor
@MainActor
func updateUI(with data: ProcessedData) {
    self.tableView.reloadData()
}

// Or with structured concurrency
Task { @MainActor in
    self.viewModel.state = .loaded(data)
}
```

#### 2.4 Deadlock / Main Thread Hang

**Signature:** Watchdog termination, `0x8badf00d` in termination reason

```swift
// CRASH: Synchronous work on main thread triggering watchdog
func application(_ application: UIApplication, didFinishLaunchingWithOptions...) -> Bool {
    let data = try! Data(contentsOf: largeFileURL)  // Blocks main thread
    self.database.migrateSync()  // Blocks main thread
    return true
}

// FIX: Defer heavy work
func application(_ application: UIApplication, didFinishLaunchingWithOptions...) -> Bool {
    Task {
        await database.migrate()
        let data = try await loadLargeFile()
    }
    return true
}
```

#### 2.5 Memory Pressure Termination

**Signature:** `Termination Reason: Namespace JETSAM` or `EXC_RESOURCE (RESOURCE_TYPE_MEMORY)`

```swift
// CRASH: Unbounded memory growth
func loadAllImages() {
    for url in imageURLs {  // 10,000+ URLs
        let image = UIImage(contentsOfFile: url.path)
        imageCache[url] = image  // Grows without bound
    }
}

// FIX: Use NSCache with limits and load on demand
let imageCache = NSCache<NSURL, UIImage>()
imageCache.countLimit = 100
imageCache.totalCostLimit = 50 * 1024 * 1024  // 50 MB
```

---

### Phase 3: Crash Clustering & Prioritization

#### 3.1 Clustering Strategy

Group crashes by shared root cause, not just stack trace similarity:

```markdown
## Crash Cluster Analysis

### Cluster 1: Nil Unwrap in User Session
- **Signatures:** 3 distinct stack traces
- **Shared Root Cause:** UserSession.currentUser force-unwrapped after logout race condition
- **Frequency:** 2,400 crashes / 7 days
- **Affected Users:** ~800 unique users
- **Impact:** HIGH - data loss possible

### Cluster 2: Collection Index Out of Range in Feed
- **Signatures:** 2 distinct stack traces
- **Shared Root Cause:** Feed array mutated during enumeration from background refresh
- **Frequency:** 890 crashes / 7 days
- **Affected Users:** ~450 unique users
- **Impact:** MEDIUM - recoverable, user retries
```

#### 3.2 Prioritization Matrix

| Severity | Frequency | User Impact | Priority |
|----------|-----------|-------------|----------|
| Data loss/corruption | >1000/week | Core flow blocked | P0 - Hotfix |
| Core flow crash | 100-1000/week | Feature unusable | P1 - This sprint |
| Secondary flow crash | 10-100/week | Workaround exists | P2 - Next sprint |
| Edge case crash | <10/week | Minimal disruption | P3 - Backlog |

---

### Phase 4: Fix Verification

**CHECKPOINT 2:** Confirm root causes identified and fixes proposed before verification.

```markdown
## Root Cause Summary

| Crash Cluster | Root Cause | Proposed Fix | Priority |
|---|---|---|---|
| [Cluster 1] | [Race condition in UserSession] | [Add actor isolation] | P0 |
| [Cluster 2] | [Array mutation during enumeration] | [Copy-on-write snapshot] | P1 |

**Proceed with fix verification strategy?**
```

#### 4.1 Fix Verification Checklist

For each crash fix, verify:

```markdown
### Fix Verification: [Crash Cluster Name]

- [ ] **Reproduces locally** - Can trigger the crash in development
- [ ] **Unit test added** - Test covers the exact crash condition
- [ ] **Fix applied** - Code change addresses root cause (not just symptoms)
- [ ] **No regression** - Existing tests pass
- [ ] **Edge cases covered** - Fix handles related edge cases
- [ ] **Crash-free in TestFlight** - Monitor TestFlight crash reports for 48 hours
- [ ] **Production verified** - Crash signature absent in next release crash data
```

#### 4.2 Regression Test Pattern

```swift
// File: Tests/CrashRegressionTests.swift

import XCTest
@testable import MyApp

final class CrashRegressionTests: XCTestCase {

    /// Regression test for crash cluster: Nil unwrap in UserSession
    /// Crash report: INC-2024-0847
    /// Root cause: currentUser force-unwrapped after logout race condition
    func testUserSessionAccessAfterLogout() async {
        let session = UserSession()
        await session.login(user: .mock)

        // Simulate race: logout while accessing user
        async let logoutTask: Void = session.logout()
        async let accessTask = session.currentUser

        _ = await (logoutTask, accessTask)

        // Should not crash - returns nil after logout
        let user = await session.currentUser
        XCTAssertNil(user, "currentUser should be nil after logout")
    }

    /// Regression test for crash cluster: Index out of range in Feed
    /// Crash report: INC-2024-0851
    func testFeedAccessDuringBackgroundRefresh() async {
        let feed = FeedViewModel()
        feed.items = [.mock, .mock, .mock]

        // Simulate: access item at index while refresh clears array
        async let refreshTask: Void = feed.refresh()
        let item = feed.item(at: 2)  // Should not crash

        await refreshTask
        // item may be nil if refresh completed first, but must not crash
    }
}
```

---

## Expected Output

### Crash Analysis Report

```markdown
# Crash Analysis Report - [App Name] v[X.Y.Z]

## Executive Summary
- Crash-free user rate: [X.X%] (target: 99.5%)
- Top crashers analyzed: [N]
- Root causes identified: [N]
- Estimated fix impact: +[X.X%] crash-free rate

## Top Crash Clusters (by frequency)

### 1. [Crash Name]
- **Exception:** [EXC_BREAKPOINT (SIGTRAP)]
- **Location:** [File.swift:LineNumber]
- **Frequency:** [N] crashes / [N] users / [period]
- **Root Cause:** [Detailed explanation]
- **Fix:** [Code-level solution with file path]
- **Regression Test:** [Test name and approach]
- **Priority:** [P0/P1/P2/P3]

### 2. [Next Crash...]

## Implementation Plan
| Priority | Crash | Fix Effort | Expected Impact |
|----------|-------|-----------|-----------------|
| P0 | [name] | [hours] | -[N] crashes/day |
| P1 | [name] | [hours] | -[N] crashes/day |

## Monitoring Plan
- [ ] Add crash-free rate alert threshold
- [ ] Monitor fixed crash signatures post-release
- [ ] Schedule follow-up review in [N] days
```

### Implementation Checklist

- [ ] All crash logs fully symbolicated
- [ ] Crash type correctly identified for each report
- [ ] Crashes clustered by shared root cause
- [ ] Prioritization based on frequency and user impact
- [ ] Root cause identified (not just symptoms)
- [ ] Code-level fix provided with file paths
- [ ] Regression tests written for each fix
- [ ] Fix verification plan includes TestFlight monitoring
- [ ] Production monitoring configured for post-release

---

## Techniques Used

- **ST-01** (Clear Objective): Focused objective on crash analysis and resolution
- **ST-02** (Sequential Instructions): Phased approach from reading crash logs to fix verification
- **RT-02** (Multi-Dimensional Analysis): Covers symbolication, pattern matching, clustering, and verification
- **AG-02** (Self-Verification): Checkpoint-based verification at each analysis phase

---

## Related Prompts

- [ios_performance_regression_detective.md](ios_performance_regression_detective.md) - Investigate performance regressions
- [ios_tech_debt_triage.md](ios_tech_debt_triage.md) - Prioritize tech debt including crash-prone code
- [ios_xcode_build_optimization.md](ios_xcode_build_optimization.md) - Optimize build and debug workflows
- [ios_deprecation_audit.md](ios_deprecation_audit.md) - Find deprecated APIs that may cause crashes
