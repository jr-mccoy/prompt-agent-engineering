---
name: "android-quarterly-maintenance"
description: "Comprehensive quarterly maintenance workflow covering dependencies, security, performance, Play Store compliance, Firebase costs, and technical debt. Use this skill when performing quarterly maintenance reviews, preparing for major releases, conducting end-of-quarter health checks, or when a solo Android developer mentions 'quarterly review', 'maintenance cycle', 'dependency updates', 'Play Store compliance check', 'Firebase cost review', or 'tech debt assessment'."
metadata:
  type: skill
  category: mobile-development
  tags:
    - android
    - maintenance
    - quarterly
    - solo-developer
  updated: "2026-02-11"
  title: "Android Quarterly Maintenance"
---

# Android Quarterly Maintenance

Comprehensive quarterly maintenance workflow for Android applications. Guides a solo developer through a structured 6-section review covering dependency health, security posture, performance benchmarks, Play Store policy compliance, Firebase cost efficiency, and technical debt -- producing a Quarterly Health Report with actionable findings.

## Purpose

This skill prevents the accumulation of invisible maintenance debt that degrades app quality over time. Solo developers often skip routine maintenance because there is no team process enforcing it. This workflow provides that structure, ensuring that every quarter you systematically review the six areas most likely to cause production incidents, Play Store rejections, or unexpected costs.

The output is a Quarterly Health Report that serves as both a maintenance record and a planning input for the next quarter.

## When to Use This Skill

Use this skill when you need to:
- Perform a scheduled quarterly maintenance review on an Android app
- Prepare an app for a major release (pre-release health check)
- Onboard to a new Android project and assess its maintenance state
- Justify maintenance time to stakeholders with evidence
- Create a maintenance baseline for a newly launched app
- Respond to "when did we last check [dependencies/security/performance]?"

## When NOT to Use This Skill

Do NOT use this skill when:
- You need to fix a specific production issue (use incident response runbooks instead)
- You are doing a single-area deep dive (use the dedicated prompt for that area)
- The app is pre-launch and has not shipped yet (use pre-launch checklists instead)
- You need to set up monitoring from scratch (use monitoring/alerting setup guides first)

## Prerequisites

- Android project with at least one production release
- Access to: Firebase Console, Google Play Console, project source code
- Tools installed: Android Studio, `gcloud` CLI, `firebase` CLI
- Approximately 4-8 hours of dedicated maintenance time
- Previous quarter's health report (if this is not the first quarter)

## Workflow Overview

```
Section 1: Dependency Updates ──────────── ~1 hour
Section 2: Security Audit ─────────────── ~1 hour
Section 3: Performance Benchmark ──────── ~1 hour
Section 4: Play Store Policy Review ───── ~30 minutes
Section 5: Firebase Cost Review ───────── ~30 minutes
Section 6: Tech Debt Assessment ────────── ~1-2 hours
                                           ──────────
                                 Total: ~5-7 hours
```

Each section produces findings that feed into the Quarterly Health Report.

---

## Section 1: Dependency Updates

**Purpose:** Ensure all dependencies are current, secure, and actively maintained.

**Time budget:** ~1 hour

### Step 1.1: Generate Dependency Report

```bash
# Run dependency update check
./gradlew dependencyUpdates -Drevision=release

# Generate dependency tree for analysis
./gradlew app:dependencies --configuration releaseRuntimeClasspath > dependency_tree.txt

# If using version catalog, review it directly
cat gradle/libs.versions.toml
```

### Step 1.2: Classify Updates

For each outdated dependency, classify:

| Classification | Action | Example |
|---------------|--------|---------|
| **Security patch** (any version) | Update immediately | OkHttp patch fixing CVE |
| **Minor version** (x.Y.z) | Update this quarter | Retrofit 2.9 to 2.11 |
| **Major version** (X.y.z) | Evaluate migration effort | Compose 1.x to 2.x |
| **Abandoned** (no updates 18+ months) | Find replacement | Deprecated library |

### Step 1.3: Execute Updates

1. Update one dependency group at a time (e.g., all Compose libraries together)
2. Run full test suite after each group update
3. Build and test release configuration (R8 may behave differently)
4. Document any breaking changes encountered

### Step 1.4: Record Findings

```markdown
### Dependency Update Summary
- Total dependencies: [N]
- Up to date: [N] ([%])
- Updated this quarter: [N]
- Major updates deferred: [N] (with justification)
- Abandoned dependencies identified: [N]
- Security patches applied: [N]
```

---

## Section 2: Security Audit

**Purpose:** Identify security vulnerabilities in code, configuration, and dependencies.

**Time budget:** ~1 hour

### Step 2.1: Dependency Vulnerability Scan

```bash
# Run OWASP dependency check (if configured)
./gradlew dependencyCheckAnalyze

# Or check National Vulnerability Database manually for key dependencies
# Focus on: networking (OkHttp, Retrofit), serialization (Gson, Moshi),
# image loading (Coil, Glide), and any library handling user input
```

### Step 2.2: Firebase Security Rules Review

```bash
# Export current rules
firebase firestore:rules:get --project=YOUR_PROJECT > firestore.rules
firebase database:rules:get --project=YOUR_PROJECT > rtdb.rules.json

# Check for overly permissive rules
# RED FLAGS:
# - allow read, write: if true;
# - ".read": true / ".write": true
# - Missing authentication checks on sensitive collections
# - Missing validation rules on write operations
```

### Step 2.3: Local Data Security Check

Review local storage for sensitive data exposure:

- SharedPreferences: Check for unencrypted tokens, passwords, PII
- Room database: Verify encryption if storing sensitive data
- File storage: Check for sensitive data in app-specific or external storage
- Logs: Ensure production builds do not log sensitive information
- WebView: Check for JavaScript interface exposure

### Step 2.4: Authentication Review

- Review authentication flows for weaknesses
- Check token refresh mechanisms
- Verify session timeout policies
- Review biometric authentication implementation
- Check for proper logout/session invalidation

### Step 2.5: Record Findings

```markdown
### Security Audit Summary
- Known CVEs in dependencies: [N] ([N] critical, [N] high, [N] medium)
- Firebase Security Rules issues: [N]
- Local data exposure risks: [N]
- Authentication weaknesses: [N]
- Overall security posture: [GREEN / YELLOW / RED]
```

---

## Section 3: Performance Benchmark

**Purpose:** Measure current performance against baselines and identify regressions.

**Time budget:** ~1 hour

### Step 3.1: Startup Performance

```bash
# Measure cold start time
adb shell am start-activity -W -n com.yourapp/.MainActivity \
  | grep "TotalTime"

# Compare with last quarter's measurement
# Target: Cold start < 2 seconds on mid-range device
```

### Step 3.2: Runtime Performance

Measure on a mid-range reference device (not your development phone):

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Cold start time | < 2000ms | `adb shell am start-activity -W` |
| Warm start time | < 1000ms | `adb shell am start-activity -W` (app in background) |
| Frame rate (scrolling) | > 55 FPS | Android Studio Profiler |
| Memory usage (idle) | < 150MB | `adb shell dumpsys meminfo com.yourapp` |
| Network data per session | Track trend | Firebase Performance Monitoring |
| ANR rate | < 0.1% | Play Console > Android Vitals |
| Crash-free rate | > 99.5% | Firebase Crashlytics |

### Step 3.3: APK/AAB Size

```bash
# Measure release APK size
ls -lh app/build/outputs/apk/release/app-release.apk

# Use APK Analyzer for detailed breakdown
# Android Studio > Build > Analyze APK
# Track: DEX size, resource size, native lib size, asset size
```

### Step 3.4: Battery and Network

- Review Firebase Performance Monitoring for network request patterns
- Check for unnecessary background work
- Review WorkManager task efficiency
- Check for wake lock usage

### Step 3.5: Record Findings

```markdown
### Performance Benchmark Summary
| Metric | Last Quarter | This Quarter | Target | Status |
|--------|-------------|-------------|--------|--------|
| Cold start | [X]ms | [Y]ms | <2000ms | [OK/WARN/FAIL] |
| Crash-free rate | [X]% | [Y]% | >99.5% | [OK/WARN/FAIL] |
| ANR rate | [X]% | [Y]% | <0.1% | [OK/WARN/FAIL] |
| APK size | [X]MB | [Y]MB | <[Z]MB | [OK/WARN/FAIL] |
| Memory (idle) | [X]MB | [Y]MB | <150MB | [OK/WARN/FAIL] |

Regressions identified: [N]
Improvements observed: [N]
```

---

## Section 4: Play Store Policy Review

**Purpose:** Verify continued compliance with Google Play Store policies, which change quarterly.

**Time budget:** ~30 minutes

### Step 4.1: Check Policy Updates

```markdown
### Play Store Policy Review Checklist

1. Visit: https://play.google.com/about/developer-content-policy/
2. Check "What's new" or "Policy updates" section
3. Review any emails from Google Play about policy changes

### Common Policy Areas to Verify:
- [ ] Target SDK version meets current requirement (check Play Console deadlines)
- [ ] Privacy policy is accessible and up to date
- [ ] Data Safety section in Play Console matches actual data collection
- [ ] Permissions declared match actual app usage
- [ ] Ad SDK compliance (if using ads)
- [ ] User data deletion capability (if collecting data)
- [ ] Subscription billing compliance (if using subscriptions)
- [ ] Content rating is accurate
- [ ] App accessibility declarations (if applicable)
```

### Step 4.2: Target SDK Compliance

```groovy
// Check current target SDK in build.gradle.kts
android {
    compileSdk = 35  // Should match latest stable
    defaultConfig {
        targetSdk = 35  // Must meet Play Store minimum
        minSdk = 24     // Review if this can be raised
    }
}

// Google typically requires targetSdk >= (current year's API level - 1)
// Check: https://developer.android.com/google/play/requirements/target-sdk
```

### Step 4.3: Record Findings

```markdown
### Play Store Compliance Summary
- Current target SDK: [N] (requirement: [N])
- Policy violations found: [N]
- Data Safety section accurate: [YES/NO]
- Privacy policy current: [YES/NO]
- Target SDK deadline: [date]
- Actions required before next quarter: [list]
```

---

## Section 5: Firebase Cost Review

**Purpose:** Analyze Firebase spending trends and identify optimization opportunities.

**Time budget:** ~30 minutes

### Step 5.1: Billing Analysis

```bash
# Check Firebase usage and billing
# Go to: Firebase Console > Usage and billing > Details

# Check Google Cloud billing for the project
gcloud billing accounts describe $(gcloud billing accounts list --format="value(name)" --limit=1)
```

### Step 5.2: Cost Breakdown

```markdown
### Firebase Cost Analysis Template

| Service | Last Quarter | This Quarter | Change | Budget |
|---------|-------------|-------------|--------|--------|
| Firestore reads | [N] / $[X] | [N] / $[Y] | [+/-]% | $[Z] |
| Firestore writes | [N] / $[X] | [N] / $[Y] | [+/-]% | $[Z] |
| Cloud Functions | [N] / $[X] | [N] / $[Y] | [+/-]% | $[Z] |
| Storage | [N]GB / $[X] | [N]GB / $[Y] | [+/-]% | $[Z] |
| Authentication | [N] / $[X] | [N] / $[Y] | [+/-]% | $[Z] |
| **Total** | **$[X]** | **$[Y]** | **[+/-]%** | **$[Z]** |
```

### Step 5.3: Cost Optimization Check

- Are there Firestore queries that could be cached client-side?
- Are Cloud Functions cold starts adding unnecessary compute time?
- Is Storage being used efficiently (old exports cleaned up)?
- Are budget alerts configured and at appropriate thresholds?
- Is the billing plan still appropriate for current usage?

### Step 5.4: Record Findings

```markdown
### Firebase Cost Summary
- Total monthly cost: $[X] (budget: $[Y])
- Quarter-over-quarter change: [+/-]%
- Largest cost driver: [service]
- Optimization opportunities identified: [N]
- Projected next quarter cost: $[X]
- Budget alerts configured: [YES/NO] at $[threshold]
```

---

## Section 6: Tech Debt Assessment

**Purpose:** Inventory and prioritize technical debt for the upcoming quarter's paydown plan.

**Time budget:** ~1-2 hours

### Step 6.1: Quick Debt Scan

```bash
# Count TODOs, FIXMEs, and HACKs in codebase
grep -r "TODO\|FIXME\|HACK\|XXX" --include="*.kt" --include="*.java" app/src/ | wc -l

# Check for deprecated API usage
./gradlew lint --check Deprecation

# Check Kotlin compiler warnings
./gradlew compileReleaseKotlin 2>&1 | grep -c "warning"
```

### Step 6.2: Debt Categories

Review each category and note items:

| Category | What to Look For |
|----------|-----------------|
| **Architecture** | God classes, missing layers, circular dependencies |
| **Testing** | Missing tests for critical paths, flaky tests |
| **Dependencies** | Outdated, abandoned, or duplicated libraries |
| **UI** | Hardcoded values, accessibility gaps, inconsistent patterns |
| **Build** | Slow builds, deprecated Gradle features, missing caching |

### Step 6.3: Prioritize for Next Quarter

Using severity scoring (impact x frequency x fix difficulty, each 1-5):

```markdown
### Top 5 Tech Debt Items for Q[N+1]

| Rank | Item | Category | Score | Est. Hours | Sprint |
|------|------|----------|-------|------------|--------|
| 1 | [Item] | [Cat] | [Score] | [Hours] | Sprint 1 |
| 2 | [Item] | [Cat] | [Score] | [Hours] | Sprint 1 |
| 3 | [Item] | [Cat] | [Score] | [Hours] | Sprint 2 |
| 4 | [Item] | [Cat] | [Score] | [Hours] | Sprint 3 |
| 5 | [Item] | [Cat] | [Score] | [Hours] | Sprint 3 |
```

### Step 6.4: Record Findings

```markdown
### Tech Debt Summary
- Total debt items identified: [N]
- New items since last quarter: [N]
- Items retired since last quarter: [N]
- Top priority for next quarter: [item]
- Estimated debt paydown budget: [N] hours (20% of dev time)
```

---

## Quarterly Health Report Template

The full Quarterly Health Report Template (Executive Summary table with G/Y/R status per section, Critical Actions, Section Reports paste-in blocks, Quarter-Over-Quarter Trends table, and Next Quarter Plan) is in the reference file.

See [references/quarterly-health-report-template.md](references/quarterly-health-report-template.md)

---

## Validation Checklist

Before marking the quarterly maintenance as complete, verify:

- [ ] All six sections have been reviewed (not skipped)
- [ ] Dependency updates have been tested in release configuration
- [ ] Security findings have severity ratings
- [ ] Performance measurements used a consistent reference device
- [ ] Play Store policy review checked the latest policy updates
- [ ] Firebase cost review includes quarter-over-quarter comparison
- [ ] Tech debt items are scored and prioritized for next quarter
- [ ] Quarterly Health Report has been generated and stored
- [ ] Critical action items have owners and deadlines
- [ ] Next quarterly review date is scheduled

---

## Related Skills

- `android-firebase-sync-validator` - Deep dive on Firebase sync configuration (use during Section 2)
- `android-room-database` - Database-specific maintenance patterns
- `android-testing-patterns` - Test gap analysis for Section 2 security and Section 6 testing debt
- `android-hilt-di` - Dependency injection review during Section 6 architecture debt
- `android-play-billing-subscriptions` - Billing compliance for Section 4 Play Store review

## Related Prompts

- `domain-software-engineering/mobile/android/maintenance/android_tech_debt_triage.md` - Deep tech debt analysis for Section 6
- `domain-software-engineering/mobile/android/maintenance/android_proguard_r8_optimization.md` - R8 optimization during dependency updates
- `domain-software-engineering/mobile/android/maintenance/android_dependency_audit.md` - Detailed dependency audit for Section 1
- `domain-software-engineering/mobile/android/targeted-reviews/firebase_incident_response.md` - Incident procedures to review alongside this maintenance
- `domain-software-engineering/devops/monitoring_solo_dev_alerting.md` - Alerting review to complement this maintenance cycle

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/quarterly-health-report-template.md` | Full Quarterly Health Report Template: Executive Summary (G/Y/R table), Critical Actions, Section Reports, Quarter-Over-Quarter Trends table (7 metrics), Next Quarter Plan, Upcoming Deadlines |
