---
name: android_ship_check
description: Pre-release verification command that runs the full test suite, checks for regressions, validates ProGuard rules, verifies Play Store policy compliance, checks Firebase security rules, and produces a go/no-go report
version: "1.0.0"
category: mobile-development
tags: [android, release, verification, play-store, firebase, testing, solo-developer]
agents_used: [android-release-manager, firebase-security-auditor, compliance-scanner, mobile-developer, test-automator]
---

Pre-release verification command for Android apps. Runs a comprehensive ship-readiness check across code quality, testing, security, performance, Play Store compliance, and Firebase configuration to produce a data-driven go/no-go release decision:

[Extended thinking: This is the "pre-flight checklist" for shipping an Android app update. Solo developers often skip verification steps under shipping pressure, leading to post-release crashes, policy violations, or security issues. This workflow enforces systematic verification by running all checks in parallel where possible, then synthesizing results into a clear go/no-go decision. Phase 1 runs build and test verification. Phase 2 runs security, compliance, and Firebase checks in parallel. Phase 3 synthesizes all results into a release decision. The key value is that a solo developer cannot hold all verification requirements in their head — this command does it for them.]

## Configuration

### Parameters
- `$ARGUMENTS` — Path to the Android project root
- `--track=internal|beta|production` — Release track (affects strictness of checks)
- `--skip-firebase` — Skip Firebase checks if not using Firebase

### Strictness Levels
- **Internal track:** Relaxed — warnings OK, focus on blockers only
- **Beta track:** Moderate — warnings should be addressed, known issues documented
- **Production track:** Strict — all checks must pass, no known critical issues

## Phase 1: Build and Test Verification

### 1. Clean Release Build
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Build the release variant of the Android app at $ARGUMENTS. Execute: (a) `./gradlew clean`, (b) `./gradlew assembleRelease` or `./gradlew bundleRelease`, (c) Capture and report: build warnings count, build errors, APK/AAB size, build duration. If the build fails, report the full error. Check that `isDebuggable` is false for release and `isMinifyEnabled` is true."
- Expected output: Build result with pass/fail, size, and warnings
- GATE: Build must succeed before proceeding

### 2. Test Suite
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Run the full test suite for the Android app at $ARGUMENTS. Execute: (a) `./gradlew test` for unit tests, (b) `./gradlew lintRelease` for lint checks. Report: total tests, passed, failed, skipped, and lint error/warning count. For any failures, include the test name and error message. Check if test coverage is configured and report the percentage."
- Expected output: Test results with pass/fail details and coverage

### 3. Version Verification
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Verify the release version configuration for the Android app at $ARGUMENTS. Check: (a) `versionCode` in build.gradle.kts — is it incremented from the previous release? (b) `versionName` follows semantic versioning, (c) Version is tagged in git, (d) No TODO or FIXME comments in production code paths (search for these), (e) No debug-only code paths active in release (check for `BuildConfig.DEBUG` usage that might leave features disabled)."
- Expected output: Version verification report

## Phase 2: Quality Audits (Run All In Parallel)

### 4. Security Check
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Perform a pre-release security check on the Android app at $ARGUMENTS. Scan for: (a) Hardcoded API keys, passwords, or tokens in source files (search patterns: API_KEY, SECRET, PASSWORD, Bearer, firebase.*apiKey outside google-services.json), (b) `android:debuggable=true` in release manifest, (c) Exported components without permission protection, (d) Cleartext traffic enabled in network_security_config.xml, (e) Sensitive data logged (Log.d with user data), (f) WebView with JavaScript enabled without proper validation. Classify findings as CRITICAL/HIGH/MEDIUM."
- Expected output: Security findings with severity

### 5. Play Store Compliance
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Review Play Store compliance for the Android app at $ARGUMENTS. Check: (a) targetSdkVersion meets current Play Store minimum, (b) Permissions declared in AndroidManifest — are all justified and used in code?, (c) Account deletion capability exists (if app has accounts), (d) Privacy policy URL is accessible, (e) ProGuard/R8 mapping file will be generated (for crash reporting), (f) Baseline Profiles are included (if configured). Report each check as PASS/FAIL."
- Expected output: Compliance checklist with pass/fail

### 6. Firebase Verification
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Verify Firebase configuration for the Android app at $ARGUMENTS (skip if no Firebase). Check: (a) google-services.json is for the correct project (prod, not dev/staging), (b) Firestore security rules don't have open access (`allow read, write: if true`), (c) App Check is referenced in the codebase, (d) Crashlytics is configured (mapping file upload in build.gradle), (e) No Firebase emulator references in production code. Report each check as PASS/FAIL/N/A."
- Expected output: Firebase verification report

### 7. ProGuard/R8 Validation
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Validate ProGuard/R8 configuration for the Android app at $ARGUMENTS. Check: (a) ProGuard rules file exists and is referenced in build.gradle, (b) Keep rules exist for: serialization classes (Kotlin Serialization, Moshi, Gson models), Room entities, Hilt components, Firebase models, Parcelable classes, (c) No warnings in R8 output from the release build, (d) Release APK/AAB size is reasonable (compare with previous release if available). Report any missing keep rules that could cause runtime crashes."
- Expected output: ProGuard validation report

### CONVERGENCE: Steps 4-7 must all complete before Phase 3

## Phase 3: Ship Decision

### 8. Go/No-Go Assessment
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Synthesize all pre-release check results for the Android app at $ARGUMENTS and make a release recommendation.

Evaluation thresholds for [$TRACK] track:
- Build: Must pass (blocker if fails)
- Tests: All pass for production, >95% for beta, >80% for internal
- Security: 0 CRITICAL (blocker), ≤2 HIGH for production
- Compliance: All PASS for production
- Firebase: All PASS for production, PASS or N/A for beta
- ProGuard: No missing critical keep rules

Produce this report:

## Ship Check Report — [Date]

### Summary
| Check | Status | Details |
|-------|--------|---------|
| Build | ✅/❌ | [size, warnings] |
| Tests | ✅/❌ | [passed/total, coverage] |
| Security | ✅/⚠️/❌ | [findings count by severity] |
| Compliance | ✅/❌ | [pass/fail items] |
| Firebase | ✅/❌/N/A | [status] |
| ProGuard | ✅/⚠️ | [status] |

### Decision: **GO** / **CONDITIONAL GO** / **NO GO**

### Blockers (must fix before shipping)
- [list if any]

### Warnings (should fix, not blocking)
- [list if any]

### Release Notes Draft
- [summary of changes for this release]

### Recommended Rollout
- [percentage and monitoring plan]
"
- Expected output: Formatted ship-check report with decision
- Context: Include all findings from Steps 1-7

## Success Criteria

### Technical Criteria
- ✅ Release build compiles successfully
- ✅ All unit tests pass
- ✅ No critical security findings
- ✅ Play Store policy compliance verified
- ✅ ProGuard rules validated

### Process Criteria
- ✅ Go/No-Go decision is data-driven
- ✅ Blockers are clearly identified
- ✅ Rollout strategy is recommended

### Operational Criteria
- ✅ Firebase configuration verified for production
- ✅ Version numbers are correct and incremented
- ✅ Mapping file will be available for crash reporting

## Rollback Procedures

If issues are found after shipping:
1. **Immediate:** Halt staged rollout in Play Console
2. **Assessment:** Review crash reports and user feedback
3. **Decision:** Fix-forward (hotfix) or rollback (unpublish and revert)
4. **Rollback:** Increment versionCode, build with previous code, deploy

## Coordination Notes

- Run this command before every production release
- For beta releases, `--track=beta` uses relaxed thresholds
- Save the ship-check report as a release artifact (documentation)
- Pair with `android-release-pipeline` skill for the actual deployment steps

Target: $ARGUMENTS
