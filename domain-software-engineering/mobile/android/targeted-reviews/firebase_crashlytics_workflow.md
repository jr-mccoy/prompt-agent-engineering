---
title: "Firebase Crashlytics Workflow"
category: mobile-development
description: "Set up a Crashlytics-driven crash response workflow for solo developers — severity classification, crash-free rate targets, alert thresholds, on-call procedures, regression detection, crash grouping optimization, and custom keys/logs"
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
  - crashlytics
  - crash-reporting
  - stability
  - solo-developer
updated: "2026-02-11"
---

# Firebase Crashlytics Workflow

**Objective:** Set up a Crashlytics-driven crash response workflow for a solo Android developer — covering severity classification (P0 through P4), crash-free rate targets (99.5%+ for top apps), alert threshold configuration, on-call procedures designed for one person, regression detection after releases, crash grouping optimization, and custom keys and logs for faster debugging — producing a complete crash response system that turns raw crash data into prioritized, actionable work without burning out a solo developer.

**When to Use:** Use this prompt when launching an app and need crash monitoring from day one, when your crash-free rate has dropped below 99% and you need a systematic response, when you are releasing frequently and need regression detection, or when you are drowning in crash reports and need a triage system that respects your time as a solo developer. Critical because crashes are the fastest way to lose users — 53% of users uninstall an app after experiencing 3 crashes, and the Play Store algorithm penalizes apps with low stability scores.

**Important context:** The biggest mistake solo developers make with Crashlytics is treating every crash as equally urgent. If you wake up to 47 crash reports, you need a system that tells you which 2 require immediate attention, which 10 can wait until the next release, and which 35 are edge cases you may never fix. Without severity classification and alert thresholds, crash monitoring becomes a source of anxiety instead of a tool. This prompt builds a workflow sized for one person — not a team with on-call rotations and SRE practices.

---

## Context Gathering

Before setting up the Crashlytics workflow, gather essential context:

1. **App Stability Baseline:**
   - "Is Crashlytics already integrated? If so, what is your current crash-free rate?"
   - "How many daily active users does your app have?"
   - "What is your current release cadence?"
   - "What are the top 3 crashes you see most frequently?"

2. **Development Context:**
   - "Are you using Kotlin or Java (or mixed)?"
   - "Are you using coroutines, and if so, do you have a global exception handler?"
   - "Do you use any crash-prone libraries (WebView, camera, media playback)?"
   - "Are you using ProGuard/R8 obfuscation?"

3. **Response Capacity:**
   - "How many hours per week can you dedicate to crash investigation?"
   - "Do you have automated tests that catch regressions?"
   - "How quickly can you push a hotfix to the Play Store?"
   - "Do you use staged rollouts on Google Play?"

4. **Notification Preferences:**
   - "What is your preferred notification channel (email, Slack, push)?"
   - "Do you want to be notified outside business hours for critical crashes?"
   - "Are there times you should NOT be disturbed (vacation, weekends)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before classifying ANY crash as a severity level, you MUST:**

1. **Check the crash-free rate impact** — A crash that affects 0.01% of sessions is not the same as one affecting 5% of sessions. Severity is determined by impact, not by how scary the stack trace looks.
2. **Verify it is a real crash** — Some "crashes" are ANRs (Application Not Responding), which have different root causes and different fix strategies. Crashlytics distinguishes between crashes and ANRs — treat them separately.
3. **Check the affected versions** — A crash only in version 2.3.1 that has been superseded by 2.4.0 may not need a hotfix. Check if the fix is already shipped.
4. **Verify reproduction** — Before spending hours debugging, confirm the crash is reproducible. Some crashes are caused by OS bugs, OEM modifications, or corrupted device state that you cannot fix.
5. **Check custom keys first** — Well-placed custom keys tell you the app state at crash time. Read them before diving into the stack trace.

### False-Positive Prevention

- Do NOT treat every crash as P0 — most crashes are P3/P4 and can wait for the next release
- Do NOT chase crashes on obscure devices with < 0.1% market share unless they reveal a real code bug
- Do NOT ignore ANRs — they hurt Play Store ranking as much as crashes but are harder to find
- Do NOT assume a crash is your code — check if it originates in a third-party SDK, OS, or OEM layer
- Do NOT set up alerts for every crash — alert fatigue is worse than no alerts
- DO focus on crash-free SESSIONS rate (not users) for accurate impact assessment
- DO check if a crash is already fixed in a newer version before investigating
- DO set severity based on user impact, not stack trace complexity
- DO invest in custom keys and logs — 5 minutes of logging setup saves hours of debugging
- DO treat regression crashes (new crashes after a release) as higher priority than chronic crashes

---

### Phase 1: Setup and Configuration

#### 1.1 Crashlytics SDK Integration

```kotlin
// build.gradle.kts (project level)
plugins {
    id("com.google.firebase.crashlytics") version "3.0.3" apply false
}

// build.gradle.kts (app level)
plugins {
    id("com.google.firebase.crashlytics")
}

dependencies {
    implementation(platform("com.google.firebase:firebase-bom:33.8.0"))
    implementation("com.google.firebase:firebase-crashlytics")
    implementation("com.google.firebase:firebase-analytics")
}
```

#### 1.2 ProGuard/R8 Mapping File Upload

If you use code obfuscation (and you should in release builds), Crashlytics needs the mapping file to deobfuscate stack traces:

```kotlin
// build.gradle.kts (app level)
android {
    buildTypes {
        release {
            isMinifyEnabled = true
            isShrinkResources = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
            // Crashlytics mapping file upload happens automatically
            // via the com.google.firebase.crashlytics plugin
        }
    }
}

// The Crashlytics Gradle plugin automatically uploads mapping files
// during the build process. Verify in build output:
// "Crashlytics mapping file upload successful"
```

#### 1.3 NDK Crash Reporting (if applicable)

```kotlin
// Only needed if your app uses native code (JNI, NDK)
dependencies {
    implementation("com.google.firebase:firebase-crashlytics-ndk")
}

// build.gradle.kts (app level)
android {
    buildFeatures {
        // Enable native symbol upload for NDK crash deobfuscation
    }
}

firebaseCrashlytics {
    nativeSymbolUploadEnabled = true
}
```

#### 1.4 Opt-Out Support

```kotlin
// Respect user privacy — allow crash reporting opt-out
class CrashlyticsManager {

    fun setCrashReportingEnabled(enabled: Boolean) {
        Firebase.crashlytics.setCrashlyticsCollectionEnabled(enabled)
    }

    // Call during onboarding or from settings screen
    fun initializeWithConsent(userConsented: Boolean) {
        Firebase.crashlytics.setCrashlyticsCollectionEnabled(userConsented)
    }
}
```

---

### Phase 2: Severity Framework

#### 2.1 Severity Classification System

| Severity | Name | Crash-Free Rate Impact | User Impact | Response Time | Example |
|----------|------|----------------------|-------------|---------------|---------|
| **P0** | Critical | Drops below 99.0% | App unusable for many users | < 4 hours | Crash on app startup, crash on main feature |
| **P1** | High | Drops below 99.5% | Major feature broken for subset | < 24 hours | Crash in payment flow, crash in core action |
| **P2** | Medium | Drops below 99.7% | Non-critical feature affected | Next release (< 2 weeks) | Crash in settings, crash in edge-case flow |
| **P3** | Low | Minimal impact (< 0.1%) | Rare edge case | Backlog (fix when convenient) | Crash on specific device/OS combo |
| **P4** | Noise | No measurable impact | Isolated incident | Won't fix (or monitor) | One-time crash, OEM-specific, corrupted state |

#### 2.2 Severity Decision Tree

```markdown
New crash report arrives
│
├─→ Does it affect app startup or the main feature?
│   YES → P0 (Critical) — Fix immediately
│
├─→ Does it affect > 1% of sessions in the last 24 hours?
│   YES → P1 (High) — Fix within 24 hours
│
├─→ Does it affect > 0.3% of sessions?
│   YES → P2 (Medium) — Fix in next release
│
├─→ Is it reproducible on common devices?
│   YES → P3 (Low) — Backlog
│   NO → Is it in your code or a third-party SDK?
│       YOUR CODE → P3 (Low) — Backlog
│       THIRD-PARTY → P4 (Noise) — Monitor, report to SDK vendor
│
└─→ Is it a single occurrence on one device?
    YES → P4 (Noise) — Close unless pattern emerges
```

#### 2.3 Crash-Free Rate Targets

```markdown
## Crash-Free Rate Benchmarks

| Category | Target | Top 25% Apps | Median Apps | Action Threshold |
|----------|--------|-------------|-------------|-----------------|
| **Crash-free sessions** | 99.5%+ | 99.8%+ | 99.2% | Below 99.0% = P0 |
| **Crash-free users** | 99.0%+ | 99.5%+ | 98.5% | Below 98.0% = P0 |
| **ANR-free sessions** | 99.7%+ | 99.9%+ | 99.5% | Below 99.0% = P1 |

## How to Read These Numbers

- 99.5% crash-free sessions means 5 out of 1000 sessions experience a crash
- For an app with 1000 DAU averaging 3 sessions each:
  - 3000 sessions/day
  - 99.5% = 15 crash sessions/day
  - 99.0% = 30 crash sessions/day
  - 98.0% = 60 crash sessions/day (unacceptable)

## Google Play Console Impact

- Crash rate is a factor in Play Store search ranking
- Apps with crash rates > 1.09% receive a warning badge
- Apps with ANR rates > 0.47% receive a warning badge
- Both thresholds are per-device-model for Play Console's Android Vitals
```

---

### Phase 3: Alert Strategy

#### 3.1 Alert Configuration

Configure Crashlytics alerts to match your severity framework — not every crash deserves a notification.

```markdown
## Alert Rules

### Alert 1: New Fatal Issue (Velocity Alert)
- **Trigger:** A NEW crash issue affects 0.5% of sessions within 1 hour
- **Channel:** Push notification + email
- **Why:** New crashes after a release are likely regressions — catch them fast
- **Action:** Triage immediately, consider rollback

### Alert 2: Regressed Issue
- **Trigger:** A previously closed crash issue reappears in a new version
- **Channel:** Email
- **Why:** Your fix didn't hold or the regression was reintroduced
- **Action:** Investigate within 24 hours

### Alert 3: Trending Issue
- **Trigger:** An existing crash issue increases by 3x in the last 24 hours
- **Channel:** Email
- **Why:** Something changed — new OS version, backend change, etc.
- **Action:** Investigate within 48 hours

### DO NOT Alert On:
- Individual crash occurrences (noise)
- Crashes on a single device model (usually OEM issue)
- Crashes in third-party SDKs you don't control
- Crashes in versions more than 2 releases behind current
```

#### 3.2 Firebase Console Alert Setup

```markdown
## Setting Up Alerts in Firebase Console

1. Go to Firebase Console → Crashlytics
2. Click the bell icon (Alerts) in the top right
3. Configure velocity alerts:
   - "Alert me when an issue causes X% of sessions to crash"
   - Set to 0.5% for P1 threshold
4. Enable regression alerts:
   - "Alert me when a closed issue regresses"
5. Set up email forwarding or Slack integration:
   - Firebase Console → Project Settings → Integrations
   - Connect Slack or PagerDuty (or use email rules)

## For Solo Developers — Notification Strategy:
- Business hours (9am-6pm): All alerts via push + email
- Evenings (6pm-10pm): P0/P1 only via email
- Night/weekends: P0 only via email (check in morning)
- Vacation: Disable all alerts, check crash-free rate on return
```

#### 3.3 Programmatic Alert Enhancement

```kotlin
// Add context to crash reports so alerts are more actionable
class CrashContextProvider {

    fun setUserContext(userId: String, tier: String) {
        Firebase.crashlytics.setUserId(userId)
        Firebase.crashlytics.setCustomKey("user_tier", tier)
    }

    fun setSessionContext(
        screenName: String,
        featureFlag: String? = null
    ) {
        Firebase.crashlytics.setCustomKey("current_screen", screenName)
        featureFlag?.let {
            Firebase.crashlytics.setCustomKey("active_feature_flag", it)
        }
    }

    fun setAppStateContext(
        isOnline: Boolean,
        syncStatus: String,
        dataCount: Int
    ) {
        Firebase.crashlytics.setCustomKey("is_online", isOnline)
        Firebase.crashlytics.setCustomKey("sync_status", syncStatus)
        Firebase.crashlytics.setCustomKey("local_data_count", dataCount)
    }
}
```

---

### Phase 4: Response Procedures

#### 4.1 Solo Developer On-Call Procedure

```markdown
## Daily Crash Review (10 minutes, every morning)

### Quick Check (2 minutes)
1. Open Firebase Console → Crashlytics
2. Check crash-free rate for last 24 hours
   - Green (> 99.5%): No immediate action needed
   - Yellow (99.0-99.5%): Check top new issues
   - Red (< 99.0%): Investigate top crash immediately

### Triage New Issues (5 minutes)
3. Sort by "Events" (descending) to see most impactful crashes
4. For each new issue:
   - Read the stack trace
   - Check custom keys for context
   - Assign severity (P0-P4) using the decision tree
   - Add a note with your assessment

### Plan (3 minutes)
5. Any P0/P1? → Block current work, fix now
6. Any P2? → Add to current sprint/release
7. P3/P4? → Backlog or close with note

## Weekly Stability Review (15 minutes, Monday)

1. Check crash-free rate trend (7-day, 30-day)
2. Compare crash-free rate to last week
3. Review top 5 unresolved issues — any changes in frequency?
4. Check if any closed issues regressed
5. Review crash-free rate by app version — is the latest version better or worse?
```

#### 4.2 Crash Investigation Workflow

```markdown
## When Investigating a Crash

### Step 1: Read the Crash Report (2 minutes)
- Exception type and message
- Stack trace — where in YOUR code does it originate?
- Custom keys — what was the app state?
- Device and OS distribution — is it device-specific?
- App version distribution — is it version-specific?

### Step 2: Classify the Crash (1 minute)
- Is it a NullPointerException? → Missing null check or uninitialized state
- Is it an IllegalStateException? → Lifecycle or state machine issue
- Is it an IndexOutOfBoundsException? → Collection/array boundary issue
- Is it an OOM (OutOfMemoryError)? → Memory leak or large allocation
- Is it in native code? → NDK issue, check native stack trace
- Is it in a third-party SDK? → Check SDK issue tracker, update SDK

### Step 3: Reproduce (5-15 minutes)
- Use custom keys to reconstruct user flow
- Try on the most affected device/OS combination
- If not reproducible, add more custom logging and wait

### Step 4: Fix and Verify (varies)
- Write the fix
- Write a regression test if possible
- Test on the affected device/OS combination
- Deploy via staged rollout (10% → monitor → 100%)

### Step 5: Close the Loop (2 minutes)
- Mark issue as resolved in Crashlytics
- Add a note with the fix and affected versions
- If fix is in version X.Y.Z, note that in the issue
```

#### 4.3 Custom Keys and Logs for Faster Debugging

```kotlin
/**
 * Strategic custom key placement.
 *
 * Custom keys appear in every crash report, telling you the
 * app state at the moment of the crash. Place them at key
 * state transitions — not on every function call.
 *
 * Limit: 64 custom key-value pairs per crash report
 * Key max length: 1024 characters
 * Value max length: 1024 characters
 */
object CrashKeys {

    // Set once at startup
    fun setStartupContext() {
        val crashlytics = Firebase.crashlytics
        crashlytics.setCustomKey("app_start_time", System.currentTimeMillis())
        crashlytics.setCustomKey("build_type", BuildConfig.BUILD_TYPE)
        crashlytics.setCustomKey("flavor", BuildConfig.FLAVOR.ifEmpty { "default" })
    }

    // Set on authentication state change
    fun setAuthContext(isLoggedIn: Boolean, authMethod: String?) {
        val crashlytics = Firebase.crashlytics
        crashlytics.setCustomKey("is_logged_in", isLoggedIn)
        authMethod?.let { crashlytics.setCustomKey("auth_method", it) }
    }

    // Set on screen navigation
    fun setScreenContext(screenName: String) {
        Firebase.crashlytics.setCustomKey("current_screen", screenName)
    }

    // Set on network state change
    fun setNetworkContext(isOnline: Boolean, connectionType: String) {
        val crashlytics = Firebase.crashlytics
        crashlytics.setCustomKey("is_online", isOnline)
        crashlytics.setCustomKey("connection_type", connectionType)
    }

    // Set on data operation
    fun setDataContext(operation: String, collection: String, documentId: String?) {
        val crashlytics = Firebase.crashlytics
        crashlytics.setCustomKey("last_data_operation", operation)
        crashlytics.setCustomKey("last_data_collection", collection)
        documentId?.let { crashlytics.setCustomKey("last_data_doc_id", it) }
    }
}

/**
 * Custom log messages for crash breadcrumbs.
 *
 * These appear in chronological order in the crash report,
 * showing what happened leading up to the crash.
 *
 * Limit: 64KB of log data per crash report
 */
object CrashLog {

    fun userAction(action: String) {
        Firebase.crashlytics.log("USER: $action")
    }

    fun navigation(from: String, to: String) {
        Firebase.crashlytics.log("NAV: $from → $to")
    }

    fun dataOperation(operation: String, result: String) {
        Firebase.crashlytics.log("DATA: $operation → $result")
    }

    fun networkCall(endpoint: String, statusCode: Int) {
        Firebase.crashlytics.log("NET: $endpoint → $statusCode")
    }

    fun stateChange(component: String, oldState: String, newState: String) {
        Firebase.crashlytics.log("STATE: $component: $oldState → $newState")
    }
}

// Usage example in a ViewModel
class TaskViewModel(
    private val repository: TaskRepository
) : ViewModel() {

    fun createTask(title: String, dueDate: LocalDate?) {
        CrashLog.userAction("create_task")
        CrashKeys.setDataContext("create", "tasks", null)

        viewModelScope.launch {
            try {
                val task = repository.createTask(title, dueDate)
                CrashLog.dataOperation("create_task", "success:${task.id}")
                CrashKeys.setDataContext("create", "tasks", task.id)
            } catch (e: Exception) {
                CrashLog.dataOperation("create_task", "error:${e.message}")
                // Record non-fatal for tracking without crashing
                Firebase.crashlytics.recordException(e)
                // Handle error in UI...
            }
        }
    }
}
```

---

### Phase 5: Release Integration

#### 5.1 Pre-Release Crash Checklist

```markdown
## Before Every Release

### Code Review for Crash Risk
- [ ] No force-unwrapping (`!!`) on nullable types from external sources (API, DB, Intent extras)
- [ ] All coroutine scopes have exception handlers
- [ ] WebView has a WebViewClient that handles errors
- [ ] All file/network operations are in try-catch blocks
- [ ] No new deprecated API usage that could NPE on newer Android versions
- [ ] ProGuard/R8 rules updated for any new libraries

### Crashlytics Configuration
- [ ] Mapping file upload enabled in build.gradle
- [ ] Version name and version code correctly set
- [ ] Custom keys updated for any new screens or features
- [ ] Non-fatal exception recording added for new error paths

### Staged Rollout Plan
- [ ] Release to 5% initially
- [ ] Monitor crash-free rate for 24 hours
- [ ] If crash-free > 99.5% → increase to 25%
- [ ] Monitor for 24 hours
- [ ] If crash-free > 99.5% → increase to 100%
- [ ] If crash-free < 99.0% at any stage → HALT ROLLOUT
```

#### 5.2 Post-Release Regression Detection

```markdown
## After Every Release (First 72 Hours)

### Hour 1-4: Immediate Check
- [ ] Open Crashlytics filtered to new version
- [ ] Any new crash issues? (issues not seen in previous version)
- [ ] Crash-free rate for new version vs previous version
- [ ] If new crashes found → classify severity immediately

### Hour 4-24: Early Detection
- [ ] Compare crash-free rate: new version vs previous version
- [ ] Check for regressed issues (previously fixed crashes returning)
- [ ] Monitor velocity alerts for the new version
- [ ] Check ANR rate for the new version

### Day 1-3: Trend Analysis
- [ ] Crash-free rate stabilized?
- [ ] Any device-specific crashes emerging?
- [ ] Any version-specific crashes (only on certain Android versions)?
- [ ] Top 5 crashes in new version — are they known or new?

### Regression Response
If a regression is detected:
1. Assess severity using the decision tree
2. If P0/P1:
   - Halt staged rollout immediately (Play Console)
   - Start hotfix development
   - Consider rolling back to previous version
3. If P2/P3:
   - Continue rollout but prioritize fix for next release
   - Add monitoring for the specific issue
```

#### 5.3 Coroutine Exception Handling

The most common source of Android crashes in modern Kotlin apps is unhandled coroutine exceptions:

```kotlin
// Global coroutine exception handler — catches unhandled exceptions
// that would otherwise crash the app
class AppCoroutineExceptionHandler : Thread.UncaughtExceptionHandler {

    private val defaultHandler = Thread.getDefaultUncaughtExceptionHandler()

    override fun uncaughtException(thread: Thread, throwable: Throwable) {
        // Crashlytics will capture this, but add extra context
        Firebase.crashlytics.setCustomKey("crash_thread", thread.name)
        Firebase.crashlytics.setCustomKey("unhandled_exception_type",
            throwable::class.java.simpleName)

        // Let the default handler (Crashlytics) process the crash
        defaultHandler?.uncaughtException(thread, throwable)
    }
}

// Install in Application.onCreate()
// Thread.setDefaultUncaughtExceptionHandler(AppCoroutineExceptionHandler())

// ViewModel-level coroutine exception handling
class SafeViewModel : ViewModel() {

    // This handler prevents ViewModel coroutines from crashing the app
    private val exceptionHandler = CoroutineExceptionHandler { _, throwable ->
        Firebase.crashlytics.recordException(throwable)
        CrashLog.stateChange("ViewModel", "running", "error:${throwable.message}")
        // Update UI state to show error
        _errorState.value = throwable.toUserMessage()
    }

    // All coroutine launches should use this handler
    fun safeAction(block: suspend () -> Unit) {
        viewModelScope.launch(exceptionHandler) {
            block()
        }
    }
}
```

---

## Expected Output

### Crashlytics Workflow Document

```markdown
# Crashlytics Workflow: [App Name]

## Current Stability
- **Crash-free sessions (7-day):** [%]
- **Crash-free sessions (30-day):** [%]
- **ANR-free sessions (7-day):** [%]
- **Top crash issues (unresolved):** [count]

## Severity Framework
| Severity | Threshold | Response Time | Current Count |
|----------|-----------|---------------|--------------|
| P0 | < 99.0% sessions | 4 hours | [N] |
| P1 | < 99.5% sessions | 24 hours | [N] |
| P2 | < 99.7% sessions | Next release | [N] |
| P3 | < 0.1% impact | Backlog | [N] |
| P4 | Isolated | Won't fix | [N] |

## Alert Configuration
| Alert Type | Trigger | Channel | Hours |
|-----------|---------|---------|-------|
| Velocity | 0.5% sessions | Push + Email | Business hours |
| Regression | Closed issue returns | Email | Business hours |
| Trending | 3x increase | Email | Business hours |

## Daily Review Procedure
[10-minute morning checklist from Phase 4.1]

## Release Integration
- Staged rollout: 5% → 25% → 100%
- Regression window: 72 hours of monitoring per release
- Halt threshold: crash-free < 99.0%

## Custom Keys Active
| Key | Set When | Debug Value |
|-----|----------|------------|
| current_screen | Navigation | Screen name |
| is_online | Connectivity change | true/false |
| last_data_operation | Data operations | operation name |
| user_tier | Auth state change | free/premium |
| auth_method | Login | google/email |

## Known Issues (Accepted Risk)
| Issue | Severity | Reason Not Fixing | Monitoring |
|-------|----------|------------------|-----------|
| [description] | P4 | [reason] | [how tracked] |
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Crash response workflow with explicit solo-developer scope
- **ST-02** (Structured Sequential Instructions) - Phased setup from configuration through release integration
- **RT-02** (Multi-Dimensional Analysis) - Severity classification, crash-free rate targets, alert strategy, and response procedures as distinct workflow dimensions
- **CM-01** (Explicit Context Framing) - Crashlytics capabilities, Play Store stability requirements, and solo developer constraints
- **DS-06** (Prioritization Guidance) - P0-P4 severity framework, response time targets, and alert configuration priorities

---

## Related Prompts

- `firebase_remote_config_strategy.md` - Kill switches to disable features causing crashes
- `firebase_analytics_strategy.md` - Analytics correlation with crash events
- `firebase_health_check.md` - Periodic stability review including crash trends
- `android_compose_recomposition_review.md` - UI crashes related to Compose recomposition
- `android_coroutine_scope_review.md` - Coroutine exception handling that prevents crashes

---

## Customization Guide

- **For apps with < 100 DAU:** Crash-free rate percentages are unreliable with small user bases (one crash can swing the rate by several percent). Focus on absolute crash counts instead: "zero new crash types per release" is a better target than "99.5% crash-free."
- **For apps with native code (NDK):** Add the `firebase-crashlytics-ndk` dependency and enable native symbol upload. Native crashes produce different stack traces that require symbol files for deobfuscation. Prioritize native crashes higher — they often indicate memory corruption that can cause data loss.
- **For apps with WebView-heavy features:** WebView crashes are notoriously hard to debug because the stack trace often points to Chromium internals. Add custom keys for the URL being loaded and the WebView state. Consider wrapping WebView in a try-catch that records a non-fatal and shows a fallback UI.
- **For apps releasing daily or more frequently:** Shorten the regression detection window from 72 hours to 24 hours. Use automated crash-free rate checks in your CI/CD pipeline — fail the next deploy if crash-free rate dropped below threshold after the previous deploy.
- **For apps preparing for Play Store featuring:** Google reviews crash-free rate and ANR rate when considering apps for featuring. Target 99.8%+ crash-free and 99.9%+ ANR-free. Clean up all P2 and P3 issues, not just P0/P1, before submitting for featuring consideration.
