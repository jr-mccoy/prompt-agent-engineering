---
name: android_beta_launch
description: Orchestrate comprehensive Android beta launch preparation across security, performance, Firebase validation, test coverage, and Play Store compliance with go/no-go release decision
version: "1.0.0"
category: mobile-development
tags: [android, beta, firebase, kotlin, launch, play-store, release, testing]
agents_used: [android-release-manager, security-auditor, performance-engineer, tdd-orchestrator, test-automator, mobile-developer]
---

Orchestrate the complete Android beta launch workflow, coordinating specialized agents across 4 phases to assess release readiness and produce a go/no-go decision:

[Extended thinking: This workflow prepares an Android app for beta distribution by running parallel quality assessments and synthesizing results into a release decision. Phase 1 establishes the baseline codebase health and Firebase infrastructure status. Phase 2 runs security, performance, and testing audits in parallel for efficiency. Phase 3 validates build configuration and Play Store compliance. Phase 4 synthesizes all findings into a data-driven go/no-go recommendation. The workflow is designed for feature-rich apps using Kotlin, Jetpack Compose, Room, Firebase RTDB/Firestore, and Cloud Functions.]

## Phase 1: Pre-Flight Assessment

### 1. Codebase Health Scan
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Analyze the Android codebase at $ARGUMENTS for beta readiness. Assess: (a) TODO/FIXME/HACK comment density in production code, (b) build warnings count (run `./gradlew assembleRelease 2>&1 | grep -c 'warning'`), (c) Kotlin compiler warnings and deprecation notices, (d) dependency freshness — identify major version gaps for critical libraries (Compose, Room, Firebase, Hilt), (e) ProGuard/R8 configuration completeness. Report blocking issues vs acceptable issues."
- Expected output: Codebase health summary with blocking vs non-blocking issues
- Context: Focus on release-readiness indicators, not code style

### 2. Firebase Infrastructure Validation
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Validate Firebase infrastructure for the Android app at $ARGUMENTS. Check: (a) Firebase RTDB security rules — ensure no open read/write access, all paths require authentication, (b) Firestore security rules — verify collection-level rules exist for all collections used in code, (c) Cloud Functions — list all deployed functions and verify they have appropriate IAM roles, (d) Firebase App Check — verify it's configured to prevent API abuse, (e) Crashlytics — verify integration is active and mapping files are uploaded. Use the android-firebase-sync-validator skill guidance."
- Expected output: Firebase validation report with pass/fail per service
- GATE: No CRITICAL issues in Firebase security rules before proceeding

## Phase 2: Quality Audits (Run All In Parallel)

### 3. Security Audit
- Use Task tool with subagent_type="security-auditor"
- Prompt: "Perform an Android-specific security audit for the app at $ARGUMENTS. Check: (a) OWASP MASVS compliance for the app's risk profile, (b) hardcoded API keys, secrets, or credentials in source files (search for patterns: API_KEY, SECRET, PASSWORD, Bearer, firebase.*apiKey), (c) exported Activities/Services without proper permissions, (d) WebView security (JavaScript enabled, file access, mixed content), (e) intent filter vulnerabilities (deep link validation), (f) certificate pinning implementation, (g) Room database encryption status, (h) SharedPreferences vs EncryptedSharedPreferences for sensitive data, (i) network_security_config.xml — verify cleartext traffic is disabled. Classify findings as CRITICAL/HIGH/MEDIUM/LOW."
- Expected output: Security findings with severity, file location, and remediation steps
- Context: App uses Firebase Auth, Room, RTDB, Firestore, Cloud Functions, location services

### 4. Performance Audit
- Use Task tool with subagent_type="performance-engineer"
- Prompt: "Assess performance characteristics of the Android app at $ARGUMENTS. Analyze: (a) cold start time indicators — Application.onCreate() complexity, ContentProvider count, eager initialization in Hilt modules, (b) Compose recomposition hotspots — @Stable/@Immutable annotations, remember usage, LazyColumn key strategy, (c) Room query complexity — identify N+1 queries, missing indexes, large result sets without pagination, (d) Firebase listener lifecycle — snapshot listeners not scoped to lifecycle, (e) background work impact — WorkManager constraints, battery optimization compliance, (f) image loading — Coil/Glide configuration, memory cache settings, (g) APK/AAB size analysis. Report against thresholds: cold start <2s, no UI jank >16ms frames, APK <50MB."
- Expected output: Performance metrics with threshold comparison and optimization recommendations
- Context: App uses Jetpack Compose, Room, Firebase RTDB + Firestore, WorkManager, location services

### 5. Test Coverage Assessment
- Use Task tool with subagent_type="test-automator"
- Prompt: "Assess test suite health for the Android app at $ARGUMENTS. Evaluate: (a) test coverage percentage (if JaCoCo configured, run coverage report), (b) unit test count and distribution across modules, (c) instrumented test count (UI tests, integration tests), (d) critical paths with test coverage: authentication, data sync (Room ↔ Firebase), notification handling, location reminders, purchase flows (if implemented), (e) test quality — look for tests with no assertions, flaky indicators (Thread.sleep, timing-dependent), mocking depth, (f) Compose UI tests — verify key screens have @Preview and UI tests. Report coverage gaps ranked by risk."
- Expected output: Coverage metrics, gap analysis with risk ranking, test quality assessment
- Context: Prioritize coverage gaps in auth, sync, billing, and notification paths

### CONVERGENCE: Steps 3-5 must all complete before Phase 3

## Phase 3: Release Preparation

### 6. Build Configuration Verification
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Verify the release build configuration for the Android app at $ARGUMENTS. Check: (a) signing configuration — release keystore configured, key alias set, (b) ProGuard/R8 — minifyEnabled true for release, shrinkResources true, rules file exists and covers Firebase/Room/Hilt, (c) buildConfigField values — no debug URLs, test API keys, or localhost references in release variant, (d) versionCode is incremented from last release, versionName follows semver, (e) debuggable is false for release, (f) target SDK meets current Play Store requirement (API 34+), (g) compileSdk is latest stable, (h) Kotlin compiler options — no -Xdebug flags in release. Report each check as PASS/FAIL."
- Expected output: Build configuration checklist with pass/fail per item
- Context: Results from Phase 2 may inform additional build config checks

### 7. Play Store Compliance Review
- Use Task tool with subagent_type="android-release-manager"
- Prompt: "Review Play Store compliance for beta release of the Android app at $ARGUMENTS. Verify: (a) Data Safety Declaration accuracy — cross-reference with actual data collection (Firebase Analytics, Crashlytics, FCM tokens, location data, user-generated content), (b) permissions justification — every permission in AndroidManifest has clear user-facing purpose, (c) ACCESS_BACKGROUND_LOCATION — if declared, verify prominent in-app disclosure before requesting, (d) target API level compliance (API 34+), (e) content rating questionnaire accuracy, (f) privacy policy URL is accessible and covers all data practices, (g) if billing is implemented: auto-renewal disclosures, cancellation flow accessibility. Report each compliance area as PASS/NEEDS_ATTENTION/FAIL."
- Expected output: Compliance review with pass/fail and remediation for failures
- Context: App collects location data, uses Firebase services, may include billing

## Phase 4: Go/No-Go Decision

### 8. Release Readiness Assessment
- Use Task tool with subagent_type="android-release-manager"
- Prompt: "Synthesize all audit results from Phases 1-3 and make a beta launch recommendation for the Android app at $ARGUMENTS.

  Evaluate against these thresholds:
  - Security: 0 CRITICAL, ≤2 HIGH (with mitigation plan)
  - Performance: Cold start <2s, no blocking UI jank
  - Test coverage: ≥60% on critical paths (auth, sync, billing)
  - Build config: All checks PASS
  - Play Store compliance: All PASS or NEEDS_ATTENTION with timeline
  - Firebase: 0 CRITICAL rule issues

  Provide:
  1. **GO** / **CONDITIONAL GO** / **NO GO** recommendation
  2. Explicit rationale citing specific findings
  3. If CONDITIONAL: list conditions that must be met before distribution
  4. Recommended beta track (internal → closed → open) with justification
  5. Staged rollout plan for the chosen track
  6. Monitoring plan for beta period (metrics to watch, alert thresholds)
  7. Timeline for addressing non-blocking findings"
- Expected output: Release decision with rationale, conditions, rollout plan, and monitoring strategy
- Context: ALL outputs from Phases 1-3

## Configuration Options

- `--track [internal|closed|open]`: Override recommended beta track
- `--skip-performance`: Skip performance audit (if recently done)
- `--skip-security`: Skip security audit (if recently done)
- `--quick`: Reduced scope — only check blocking issues
- `--verbose`: Include all findings, not just blocking ones

## Success Criteria

- All 4 phases complete with actionable findings
- Every CRITICAL/HIGH finding has a remediation recommendation
- Go/no-go decision is data-driven with explicit threshold evaluation
- Rollout plan includes monitoring metrics and halt criteria
- Non-blocking findings have a prioritized remediation timeline
- Report is shareable with the team

## Coordination Notes

- Phase 2 tasks are independent and should run in parallel
- Phase 3 depends on Phase 2 findings (security issues may affect build config)
- Phase 4 requires ALL previous outputs
- If the security audit reveals CRITICAL issues, Phase 3 compliance review should flag them
- The go/no-go decision should be conservative for first beta (err on the side of fixing)

Target app: $ARGUMENTS
