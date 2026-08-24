---
name: android_pre_release_security_audit
description: Android-specific security audit covering OWASP MASVS, Firebase security rules, local data protection, network security, authentication, billing security, location privacy, and Play Store data safety compliance
version: "1.0.0"
category: security
tags: [android, audit, firebase, kotlin, owasp, privacy, security]
agents_used: [security-auditor, threat-modeling-expert, mobile-developer]
---

Perform a comprehensive Android-specific security audit coordinating specialized agents across 4 phases. Covers static analysis, Firebase rules, local data protection, network security, authentication, and privacy compliance:

[Extended thinking: This command goes beyond generic SAST by addressing Android-specific attack vectors. Mobile apps have unique security considerations: local storage on a potentially rooted device, exported components accessible to other apps, Firebase security rules that gate cloud data access, location data privacy, and billing receipt validation. The phased approach ensures systematic coverage without overwhelming the review. Phase 1 handles static analysis that can run automatically. Phase 2 covers data security across local storage and network. Phase 3 addresses authentication, authorization, and billing. Phase 4 synthesizes findings with privacy compliance review.]

## Phase 1: Static Analysis and Firebase Rules

### 1. Android SAST Scan
- Use Task tool with subagent_type="security-auditor"
- Prompt: "Perform static application security testing on the Android codebase at $ARGUMENTS. Scan for:

  **Secrets and Credentials:**
  - Hardcoded API keys (grep for patterns: apiKey, API_KEY, api_key, secret, password, token)
  - Firebase configuration exposed in google-services.json (expected but verify no server keys)
  - OAuth client secrets in source code
  - Test credentials left in release code

  **Exported Components:**
  - Activities with `exported=true` or intent filters without permission guards
  - Services, BroadcastReceivers, ContentProviders with open access
  - Deep link handlers without input validation
  - PendingIntent mutability risks (FLAG_MUTABLE without proper safeguards)

  **Code-Level Vulnerabilities:**
  - SQL injection in raw Room queries (`@RawQuery` without parameterization)
  - WebView with JavaScript enabled + file access
  - Insecure random number generation (java.util.Random instead of SecureRandom)
  - Logging of sensitive data (passwords, tokens, PII in Log.d/Log.i)
  - StrictMode violations in release builds
  - Debug flags or test backdoors in release variant

  Classify each finding as CRITICAL/HIGH/MEDIUM/LOW with file path and line number."
- Expected output: SAST findings with severity, location, and remediation
- Context: Kotlin codebase with Jetpack Compose, Hilt, Room, Firebase

### 2. Firebase Security Rules Audit
- Use Task tool with subagent_type="security-auditor"
- Prompt: "Audit all Firebase security rules for the Android app at $ARGUMENTS. Review:

  **Realtime Database Rules:**
  - No `.read: true` or `.write: true` at root level
  - All paths require `auth != null`
  - User data paths validate `auth.uid === $userId`
  - Rate limiting rules where applicable
  - Data validation rules (`.validate` with type and range checks)

  **Firestore Rules:**
  - No `allow read, write: if true` on any collection
  - All collections require authentication
  - Document-level ownership validation (resource.data.userId == request.auth.uid)
  - Write validation rules (field types, required fields, size limits)
  - Deny wildcards at top level

  **Cloud Functions:**
  - All HTTPS callable functions verify auth context (`context.auth`)
  - Firestore triggers have appropriate IAM roles
  - No admin SDK usage with default credentials in production
  - Rate limiting on public-facing functions

  **Firebase App Check:**
  - Verify App Check is enforced for RTDB, Firestore, Cloud Functions, and Storage
  - Verify attestation provider is configured (Play Integrity for Android)

  Report each rule file with pass/fail per check."
- Expected output: Firebase rules audit with specific rule violations and fixes
- Context: App uses RTDB for messaging/presence, Firestore for structured data, Cloud Functions for server logic

## Phase 2: Data Security (Run In Parallel)

### 3. Local Data Protection
- Use Task tool with subagent_type="security-auditor"
- Prompt: "Audit local data protection for the Android app at $ARGUMENTS. Review:

  **Room Database:**
  - Is SQLCipher or similar encryption used? If not, assess data sensitivity stored in Room
  - Review all @Entity classes for PII or sensitive data stored unencrypted
  - Check database export settings (allowExportImportAuthority)

  **SharedPreferences / DataStore:**
  - Is EncryptedSharedPreferences used for sensitive values (tokens, keys)?
  - Check for PII in plain SharedPreferences
  - Verify DataStore files are in app-private storage

  **File Storage:**
  - FileProvider configuration — verify no overly broad path declarations
  - Temporary files in cache cleaned up appropriately
  - No sensitive data written to external storage

  **Android Keystore:**
  - Cryptographic keys stored in Android Keystore (not hardcoded)
  - Key generation with appropriate algorithm and key size
  - Key access requires user authentication where appropriate

  Classify data exposure risks by sensitivity of the data."
- Expected output: Local data protection audit with specific files/entities flagged

### 4. Network Security
- Use Task tool with subagent_type="security-auditor"
- Prompt: "Audit network security configuration for the Android app at $ARGUMENTS. Review:

  **network_security_config.xml:**
  - Cleartext traffic disabled (`cleartextTrafficPermitted=\"false\"`)
  - No overly permissive domain exceptions
  - Certificate pinning configured for critical API endpoints
  - Debug overrides removed from release configuration

  **API Communication:**
  - All API calls use HTTPS
  - No hardcoded HTTP URLs in source code
  - OkHttp/Retrofit configured with certificate pinning
  - Timeout settings appropriate (prevent hanging connections)

  **Firebase Network:**
  - Firebase SDK handles TLS automatically — verify no custom SSLSocketFactory overrides
  - Verify Firebase URLs not hardcoded (should use SDK methods)

  **WebView:**
  - Mixed content mode set to MIXED_CONTENT_NEVER_ALLOW
  - WebView JavaScript interface methods annotated with @JavascriptInterface and sanitized
  - loadUrl() inputs validated (no user-controlled URLs without allowlist)

  Report each check as PASS/FAIL with evidence."
- Expected output: Network security audit with configuration issues and fixes

### CONVERGENCE: Steps 3-4 must complete before Phase 3

## Phase 3: Authentication, Authorization, and Billing

### 5. Authentication and Session Security
- Use Task tool with subagent_type="security-auditor"
- Prompt: "Audit authentication and session security for the Android app at $ARGUMENTS. Review:

  **Firebase Authentication:**
  - Sign-in methods configured appropriately (email/password, Google, etc.)
  - Email verification enforced before accessing sensitive features
  - Password requirements meet minimum standards (8+ chars, complexity)
  - Account deletion flow implemented (Play Store requirement)

  **Session Management:**
  - Firebase Auth token refresh handled correctly
  - Token storage uses secure mechanisms (not plain SharedPreferences)
  - Session timeout for inactive users
  - Re-authentication required for sensitive operations (delete account, change email)

  **Authorization:**
  - Feature access tied to Firebase Auth state (not local flags)
  - Admin/premium features properly gated server-side
  - Firestore/RTDB rules enforce authorization (not just client-side checks)

  Report gaps with severity based on exploitability."
- Expected output: Auth/session security assessment

### 6. Billing and Purchase Security (If Applicable)
- Use Task tool with subagent_type="security-auditor"
- Prompt: "If billing is implemented in the Android app at $ARGUMENTS, audit purchase security. If no billing exists, skip and report 'N/A — billing not implemented.' Review:

  **Receipt Validation:**
  - ALL purchases verified server-side (never trust client-side BillingResult alone)
  - Cloud Function validates purchase tokens with Google Play Developer API
  - Validated purchases stored in Firestore (server as source of truth)

  **Entitlement Security:**
  - Premium features gated by server-side entitlement, not local Room cache alone
  - Local entitlement cache has expiry and is refreshed from server
  - No way to grant entitlements by modifying local storage

  **Replay Attack Prevention:**
  - Purchase tokens validated only once (idempotency)
  - Token reuse detected and rejected

  Report any finding where a user could gain premium access without paying."
- Expected output: Billing security assessment or N/A

## Phase 4: Privacy and Compliance

### 7. Privacy and Data Safety Review
- Use Task tool with subagent_type="android-release-manager"
- Prompt: "Review privacy practices and Play Store Data Safety compliance for the Android app at $ARGUMENTS. Cross-reference actual data collection against Play Store declarations:

  **Data Collection Inventory:**
  - List ALL data collected: Firebase Analytics events, Crashlytics data, FCM tokens, location data, user-generated content, purchase history, device identifiers
  - For each: Is it disclosed in the Data Safety Declaration?

  **Location Data:**
  - Purpose of location collection documented for user
  - Background location usage has prominent in-app disclosure
  - Location data minimization (only collect precision needed)
  - Location data not shared with third parties without disclosure

  **Notification Data:**
  - FCM token storage and retention policy
  - Notification content not logged in plaintext

  **Third-Party SDKs:**
  - List all SDKs that collect data (Firebase, AdMob, analytics)
  - Verify Data Safety Declaration covers third-party data collection

  **User Rights:**
  - Account deletion implemented and discoverable
  - Data export capability (if required by jurisdiction)
  - Consent withdrawal mechanism

  Report discrepancies between actual practices and declarations."
- Expected output: Privacy compliance report with discrepancies and required updates

### 8. Consolidated Security Report
- Use Task tool with subagent_type="security-auditor"
- Prompt: "Synthesize all security findings from Phases 1-4 into a consolidated Android Security Audit Report for $ARGUMENTS.

  Format:
  ```
  # Android Pre-Release Security Audit Report
  **App:** [name]
  **Date:** [date]

  ## Executive Summary
  [1-2 paragraph overview of security posture]

  ## Findings by Severity
  ### CRITICAL (Fix Before Release)
  [Each finding with: description, location, impact, remediation]

  ### HIGH (Fix Before Production)
  [Same format]

  ### MEDIUM (Schedule Fix)
  [Same format]

  ### LOW (Track)
  [Same format]

  ## Firebase Rules Status
  [Pass/fail summary for RTDB, Firestore, Cloud Functions, App Check]

  ## Data Safety Declaration Accuracy
  [Discrepancies found, required updates]

  ## Recommendations
  [Prioritized action list with effort estimates]

  ## Sign-Off Criteria
  [What must be true before security sign-off for beta]
  ```"
- Expected output: Consolidated security report ready for team review

## Configuration Options

- `--scope [full|critical-only]`: Full audit or only critical checks
- `--include-billing`: Force billing audit even if billing code not detected
- `--skip-firebase`: Skip Firebase rules audit (if recently audited)
- `--output [markdown|json]`: Report format

## Success Criteria

- All 4 phases complete with specific, actionable findings
- Every CRITICAL finding has a clear remediation with code example
- Firebase rules audit covers all rule files with pass/fail per rule
- Privacy review cross-references actual data collection vs declarations
- Consolidated report is self-contained and shareable
- No false positives in CRITICAL/HIGH findings (verified by cross-reference)

## Coordination Notes

- Phase 2 tasks are independent and should run in parallel
- Phase 3 may depend on Phase 2 findings (local data issues affect auth assessment)
- Phase 4 requires ALL previous outputs for synthesis
- This command is read-only — it does not modify the codebase
- For remediation, use findings from this audit with the security-auditor agent

Target app: $ARGUMENTS
