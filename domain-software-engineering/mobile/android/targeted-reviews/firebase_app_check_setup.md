---
title: "Firebase App Check Setup"
category: mobile-development
description: "Implement Firebase App Check with Play Integrity — attestation provider setup, debug tokens, enforcement rollout strategy, monitoring verified vs unverified traffic, and production hardening"
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
  - app-check
  - play-integrity
  - security
  - solo-developer
updated: "2026-02-11"
---

# Firebase App Check Setup

**Objective:** Implement Firebase App Check with Play Integrity for an Android app — covering attestation provider setup, debug token configuration for development, a phased enforcement rollout strategy (monitor, warn, enforce), monitoring verified vs unverified traffic ratios, Play Integrity vs SafetyNet comparison, Cloud Functions enforcement, and production hardening — producing a fully configured App Check implementation that protects your Firebase backend from unauthorized access without breaking legitimate users.

**When to Use:** Use this prompt when your Firebase project is exposed to the internet and you want to ensure only your genuine app can access your backend, when you notice suspicious traffic or unauthorized API calls to your Firestore or Cloud Functions, when preparing for production launch and need to harden your security posture, or when migrating from the deprecated SafetyNet attestation provider to Play Integrity. Critical because without App Check, anyone with your Firebase config (which is public in your APK) can call your Firestore, Cloud Functions, and Storage directly from curl or a modified app.

**Important context:** App Check is NOT a replacement for Firestore security rules or Cloud Functions authentication. It is an additional layer that verifies the REQUEST is coming from your genuine, unmodified app — not from a script, emulator, or tampered APK. Think of it as a bouncer checking IDs at the door: security rules decide what each person can do inside, but App Check decides who gets through the door at all. The biggest mistake is enforcing App Check before monitoring — if you flip enforcement on immediately, you will lock out users on older app versions, rooted devices, and some emulators.

---

## Context Gathering

Before implementing App Check, gather essential context:

1. **Current Security Posture:**
   - "What Firebase services does your app use (Firestore, Cloud Functions, Storage, RTDB)?"
   - "Do you have Firestore security rules in place?"
   - "Have you noticed any suspicious or unauthorized traffic to your Firebase backend?"
   - "Are you currently using any attestation or device verification?"

2. **App Distribution:**
   - "What is your minimum supported Android API level?"
   - "Do you distribute your app through Google Play only, or also via sideloading, Samsung Galaxy Store, etc.?"
   - "Approximately how many active app versions are in the wild?"
   - "Do any of your users run on rooted devices or custom ROMs?"

3. **Development Workflow:**
   - "Do you test on physical devices, emulators, or both?"
   - "How many developers work on this project?"
   - "Do you have CI/CD that runs automated tests against Firebase?"
   - "Do you have separate Firebase projects for dev/staging/prod?"

4. **Migration Context (if applicable):**
   - "Are you currently using SafetyNet for attestation?"
   - "Have you already registered your app with the Play Integrity API?"
   - "Are you using any other Google Play services that require integrity checks?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before enabling ANY App Check enforcement, you MUST:**

1. **Monitor first, enforce later** — Enable App Check in monitoring mode for at least 2 weeks before enforcing. This lets you see how much traffic is verified vs unverified without blocking anyone.
2. **Set up debug tokens** — Development builds, emulators, and CI environments cannot pass real attestation. You MUST configure debug tokens before enforcement or your development workflow breaks.
3. **Update all app versions** — App Check only works in app versions that include the App Check SDK. Any older versions in the wild will be blocked when enforcement is turned on. Communicate the update requirement.
4. **Test enforcement on staging first** — Never enable enforcement on production Firebase without testing on a staging project first.
5. **Have a rollback plan** — Know how to disable enforcement instantly if legitimate users are blocked. This is a Firebase Console toggle — ensure you know where it is.

### False-Positive Prevention

- Do NOT enable enforcement before monitoring for at least 2 weeks — you will lock out legitimate users
- Do NOT assume all legitimate traffic will be verified — rooted devices, sideloaded installs, and older versions will fail attestation
- Do NOT forget debug tokens for development — your local builds will stop working
- Do NOT treat App Check as a replacement for security rules — it protects the channel, not the data model
- Do NOT hardcode debug tokens in source control — use environment variables or local properties
- DO monitor the verified/unverified traffic ratio before making enforcement decisions
- DO set up debug tokens for every developer and CI environment
- DO plan a minimum app version requirement before enforcement
- DO test enforcement in a staging Firebase project before production
- DO have a one-click rollback plan documented

---

### Phase 1: Provider Setup

#### 1.1 Play Integrity vs SafetyNet Comparison

| Feature | Play Integrity API | SafetyNet Attestation |
|---------|-------------------|----------------------|
| **Status** | Active, recommended | Deprecated (removed Jan 2025) |
| **API level** | Android 5.0+ (API 21+) | Android 5.0+ (API 21+) |
| **Distribution** | Google Play required | Google Play required |
| **Verdict types** | Device integrity, account, app licensing | Basic integrity, CTS profile match |
| **Daily quota** | 10,000 free/day (standard), more with Play Console | 10,000 free/day |
| **Latency** | ~200-500ms (warm), ~1-3s (cold) | ~200-800ms |
| **Rooted devices** | Fails MEETS_DEVICE_INTEGRITY | Fails CTS profile match |
| **Emulators** | Fails (use debug tokens) | Fails (use debug tokens) |
| **Cost above quota** | $0.00 for standard tier, paid for classic | N/A (deprecated) |

**Recommendation:** Always use Play Integrity. SafetyNet is deprecated and no longer receives updates. If you are still on SafetyNet, migrate immediately.

#### 1.2 Firebase Console Configuration

```markdown
## Setup Steps in Firebase Console

1. Go to Firebase Console → App Check
2. Click on your Android app
3. Select "Play Integrity" as the attestation provider
4. Register your app:
   - SHA-256 certificate fingerprint is required
   - Get it with: `./gradlew signingReport`
5. Note: Play Integrity registration happens automatically when
   you add the App Check SDK — no separate Google Cloud Console
   setup is required for the standard (non-classic) API tier
```

#### 1.3 Android SDK Integration

Add dependencies to your app-level `build.gradle.kts`:

```kotlin
// build.gradle.kts (app level)
dependencies {
    // Firebase BoM — manages all Firebase library versions
    implementation(platform("com.google.firebase:firebase-bom:33.8.0"))

    // App Check with Play Integrity provider
    implementation("com.google.firebase:firebase-appcheck-playintegrity")

    // Debug provider for development builds
    implementation("com.google.firebase:firebase-appcheck-debug")
}
```

#### 1.4 App Check Initialization

```kotlin
class MyApplication : Application() {

    override fun onCreate() {
        super.onCreate()

        // Initialize App Check BEFORE any other Firebase calls
        val appCheckFactory = if (BuildConfig.DEBUG) {
            // Debug provider for development/testing
            DebugAppCheckProviderFactory.getInstance()
        } else {
            // Play Integrity for production
            PlayIntegrityAppCheckProviderFactory.getInstance()
        }

        FirebaseAppCheck.getInstance().installAppCheckProviderFactory(appCheckFactory)
    }
}
```

**Key implementation notes:**
- App Check must be initialized BEFORE `FirebaseFirestore.getInstance()`, `FirebaseStorage.getInstance()`, etc.
- The initialization should happen in your `Application.onCreate()`, not in an Activity
- The `BuildConfig.DEBUG` check ensures debug provider is only used in debug builds — never in production

---

### Phase 2: Debug Configuration

#### 2.1 Debug Token Setup for Local Development

When you run your app in debug mode, the debug provider will print a token to logcat:

```
D/DebugAppCheckProvider: Enter this debug token in the Firebase Console:
   YOUR-DEBUG-TOKEN-HERE
```

Register this token in Firebase Console:

```markdown
## Registering Debug Tokens

1. Run your debug build on a device or emulator
2. Check logcat for the debug token (filter by "DebugAppCheckProvider")
3. Go to Firebase Console → App Check → Apps → Manage debug tokens
4. Click "Add debug token"
5. Paste the token and give it a descriptive name:
   - "[Your Name] - Pixel 8 Emulator"
   - "[Your Name] - Physical Device"
   - "CI/CD - GitHub Actions"
6. Click "Save"
```

#### 2.2 Debug Tokens for CI/CD

For CI environments, you cannot read logcat. Instead, set a predetermined debug token via environment variable:

```kotlin
// For CI/CD: Set a known debug token via environment variable
// In your Application class:
class MyApplication : Application() {

    override fun onCreate() {
        super.onCreate()

        val appCheckFactory = if (BuildConfig.DEBUG) {
            // Check if we're in CI with a predetermined token
            val ciToken = System.getenv("FIREBASE_APP_CHECK_DEBUG_TOKEN")
            if (ciToken != null) {
                // Set the debug token programmatically for CI
                DebugAppCheckProviderFactory.getInstance().apply {
                    // The CI token must also be registered in Firebase Console
                }
            } else {
                DebugAppCheckProviderFactory.getInstance()
            }
        } else {
            PlayIntegrityAppCheckProviderFactory.getInstance()
        }

        FirebaseAppCheck.getInstance().installAppCheckProviderFactory(appCheckFactory)
    }
}
```

For GitHub Actions, store the debug token as a repository secret:

```yaml
# .github/workflows/test.yml
env:
  FIREBASE_APP_CHECK_DEBUG_TOKEN: ${{ secrets.FIREBASE_APP_CHECK_DEBUG_TOKEN }}
```

#### 2.3 Debug Token Security

```markdown
## Debug Token Security Rules

1. NEVER commit debug tokens to source control
2. Store CI tokens as encrypted secrets (GitHub Secrets, etc.)
3. Use different debug tokens for each developer and CI environment
4. Periodically rotate debug tokens (quarterly)
5. Remove debug tokens for developers who leave the project
6. Name tokens descriptively so you know what to revoke:
   - "john-macbook-emulator" — John's development machine
   - "github-actions-main" — CI pipeline
   - "staging-test-device" — Shared staging test device

## Token Inventory (keep this updated):
| Token Name | Owner | Purpose | Created | Last Rotated |
|-----------|-------|---------|---------|-------------|
| [name] | [person] | [dev/CI] | [date] | [date] |
```

---

### Phase 3: Monitoring Phase

#### 3.1 Enable Monitoring (No Enforcement)

Before enforcing, monitor the ratio of verified to unverified requests:

```markdown
## Monitoring Setup Steps

1. Go to Firebase Console → App Check
2. For each service (Firestore, Cloud Functions, Storage):
   - The default state is "Not enforced" — this is monitoring mode
   - App Check will track which requests include valid tokens
   - NO requests are blocked in this state
3. Wait at least 2 weeks to collect representative data
4. Check the metrics dashboard regularly
```

#### 3.2 Monitoring Metrics to Track

```markdown
## Key Metrics During Monitoring Phase

| Metric | What to Look For | Action If Concerning |
|--------|-----------------|---------------------|
| **Verified %** | Should be 80-95% if most users are on recent versions | If < 80%, too many old versions in the wild — delay enforcement |
| **Unverified requests** | Should decrease over time as users update | If steady or increasing, investigate source |
| **Request volume** | Baseline for normal traffic | Spikes in unverified traffic may indicate abuse |
| **Geographic distribution** | Matches your user base | Unexpected regions may indicate scraping |
| **Error rate** | App Check SDK errors | High error rate means SDK integration issues |
```

#### 3.3 Interpreting Monitoring Data

```markdown
## Monitoring Decision Framework

### Scenario 1: Verified > 95%
- Ready for enforcement
- Proceed to Phase 4 with confidence
- The 5% unverified is likely old app versions and will decrease

### Scenario 2: Verified 80-95%
- Mostly ready but some unverified traffic
- Check: What percentage is from old app versions vs suspicious?
- Action: Push an update prompt to users on old versions
- Wait until verified > 90% before enforcing

### Scenario 3: Verified 50-80%
- Too many unverified requests to enforce safely
- Likely causes:
  - Many users on pre-App-Check app versions
  - Sideloaded installs (no Play Integrity)
  - Rooted/custom ROM users
- Action: Require app update via in-app messaging, wait 4-6 weeks

### Scenario 4: Verified < 50%
- Do NOT enforce — you will lock out most users
- Likely cause: App Check SDK not properly integrated or very old user base
- Action: Verify SDK integration, check that initialization runs before Firebase calls

### Scenario 5: Spike in unverified requests
- Possible abuse or scraping detected
- Action: Consider enforcing on the specific service being targeted
- Even partial enforcement (e.g., just Cloud Functions) helps
```

---

### Phase 4: Gradual Enforcement

#### 4.1 Enforcement Rollout Strategy

```markdown
## Enforcement Rollout Plan

### Pre-Enforcement Checklist
- [ ] Monitored for 2+ weeks
- [ ] Verified traffic ratio > 90%
- [ ] All debug tokens registered and tested
- [ ] CI/CD pipeline has debug token configured
- [ ] Minimum app version with App Check SDK communicated to users
- [ ] Rollback procedure documented and tested
- [ ] Staging project enforcement tested successfully

### Stage 1: Enforce on Cloud Functions Only (Week 1-2)
Why: Cloud Functions are the most commonly abused endpoint and the
     easiest to test. If enforcement breaks something, the impact
     is limited to server-side operations.
- [ ] Enable enforcement for Cloud Functions in Firebase Console
- [ ] Monitor for 1 week:
  - [ ] No increase in client-side errors
  - [ ] Cloud Functions still accessible from your app
  - [ ] Debug builds still work
  - [ ] CI/CD pipeline still passes

### Stage 2: Enforce on Cloud Storage (Week 3-4)
Why: Storage is the second most common abuse vector (unauthorized
     uploads consuming your quota).
- [ ] Enable enforcement for Cloud Storage
- [ ] Monitor for 1 week:
  - [ ] File uploads and downloads still work
  - [ ] No increase in storage errors in Crashlytics

### Stage 3: Enforce on Firestore (Week 5-6)
Why: Firestore enforcement has the broadest impact — every read
     and write is checked. Save this for last.
- [ ] Enable enforcement for Firestore
- [ ] Monitor for 2 weeks:
  - [ ] All CRUD operations still work
  - [ ] No increase in Firestore errors
  - [ ] Query performance unchanged
  - [ ] Offline/sync still works correctly

### Stage 4: Enforce on Realtime Database (if used)
- [ ] Enable enforcement for RTDB
- [ ] Monitor for 1 week
```

#### 4.2 Enforcement in Firebase Console

```markdown
## How to Enable/Disable Enforcement

### Enable:
1. Firebase Console → App Check
2. Select the service (Firestore, Functions, Storage)
3. Click "Enforce"
4. Confirm in the dialog

### Disable (Rollback):
1. Firebase Console → App Check
2. Select the service
3. Click "Unenforce"
4. Effect is immediate — all requests are allowed again

IMPORTANT: Unenforcement is instant. If you see problems after
enabling enforcement, you can roll back in under 30 seconds.
```

#### 4.3 Cloud Functions Enforcement Code

App Check is enforced at the service level in Firebase Console, but you can also verify App Check tokens explicitly in Cloud Functions for fine-grained control:

```typescript
// functions/src/middleware/appCheck.ts
import { onCall, HttpsError } from "firebase-functions/v2/https";

// Option 1: Automatic enforcement via Firebase Console
// When you enable enforcement in the Console, ALL callable/HTTP
// functions automatically reject requests without valid App Check tokens.
// No code changes needed.

// Option 2: Manual verification in specific functions
// Use this for gradual per-function enforcement
export const sensitiveOperation = onCall(
  {
    // Enforce App Check for this specific function
    enforceAppCheck: true,
  },
  async (request) => {
    // If we get here, App Check token was valid
    // (invalid tokens are rejected automatically)

    if (!request.auth) {
      throw new HttpsError("unauthenticated", "Must be logged in");
    }

    // Proceed with sensitive operation
    return await processSecureAction(request.data);
  }
);

// Option 3: Conditional enforcement (monitor then enforce)
export const gradualEnforcement = onCall(async (request) => {
  // Log App Check status for monitoring
  const appCheckToken = request.app;

  if (!appCheckToken) {
    // Request has no App Check token
    console.warn("Request without App Check token", {
      uid: request.auth?.uid,
      ip: request.rawRequest.ip,
    });

    // During monitoring phase: allow but log
    // During enforcement phase: uncomment the throw below
    // throw new HttpsError("permission-denied", "App Check required");
  }

  return await processAction(request.data);
});
```

#### 4.4 firebase.json App Check Configuration

```json
{
  "firestore": {
    "rules": "firestore.rules",
    "indexes": "firestore.indexes.json"
  },
  "functions": [
    {
      "source": "functions",
      "codebase": "default",
      "ignore": [
        "node_modules",
        ".git",
        "firebase-debug.log",
        "firebase-debug.*.log",
        "*.local"
      ],
      "predeploy": [
        "npm --prefix \"$RESOURCE_DIR\" run lint",
        "npm --prefix \"$RESOURCE_DIR\" run build"
      ]
    }
  ],
  "emulators": {
    "auth": {
      "port": 9099
    },
    "functions": {
      "port": 5001
    },
    "firestore": {
      "port": 8080
    },
    "storage": {
      "port": 9199
    },
    "ui": {
      "enabled": true,
      "port": 4000
    }
  },
  "appCheck": {
    "enforcement": {
      "firestore": false,
      "storage": false,
      "functions": false
    }
  }
}
```

**Note:** The `firebase.json` `appCheck` section configures enforcement for emulators and local testing. Production enforcement is controlled via the Firebase Console, not this file.

---

### Phase 5: Production Hardening

#### 5.1 Token Refresh Strategy

App Check tokens have a limited TTL (time-to-live). The SDK handles refresh automatically, but you should understand the lifecycle:

```kotlin
// App Check token lifecycle:
// 1. SDK requests token from Play Integrity (cold: 1-3s, warm: 200-500ms)
// 2. Token is cached locally (default TTL: 1 hour)
// 3. SDK auto-refreshes before expiry
// 4. If refresh fails, cached token is used until expiry
// 5. After expiry with no refresh, requests fail (if enforcement is on)

// You can listen to token changes for monitoring:
FirebaseAppCheck.getInstance().addAppCheckListener { token ->
    Log.d("AppCheck", "New token received, expires: ${token.expireTimeMillis}")
}
```

#### 5.2 Handling Attestation Failures Gracefully

```kotlin
/**
 * Not all legitimate users will pass attestation:
 * - Rooted devices fail Play Integrity
 * - Sideloaded installs may fail
 * - Very old Android versions may have issues
 *
 * Design your UX for these cases.
 */
class AppCheckStatusMonitor {

    fun checkAttestationStatus(
        onVerified: () -> Unit,
        onFailed: (Exception) -> Unit
    ) {
        FirebaseAppCheck.getInstance()
            .getAppCheckToken(false) // false = don't force refresh
            .addOnSuccessListener { token ->
                onVerified()
            }
            .addOnFailureListener { exception ->
                // Log but don't crash — handle gracefully
                Log.w("AppCheck", "Attestation failed", exception)
                onFailed(exception)
            }
    }
}

// In your UI, show a helpful message instead of a cryptic error
@Composable
fun AppCheckFailureScreen() {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(32.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Text(
            text = "Verification Required",
            style = MaterialTheme.typography.headlineMedium
        )
        Spacer(modifier = Modifier.height(16.dp))
        Text(
            text = "This app requires verification through Google Play. " +
                   "Please ensure you installed this app from the Google Play Store " +
                   "and that your device software is up to date.",
            style = MaterialTheme.typography.bodyLarge,
            textAlign = TextAlign.Center
        )
        Spacer(modifier = Modifier.height(24.dp))
        Button(onClick = { /* Open Play Store listing */ }) {
            Text("Open Play Store")
        }
    }
}
```

#### 5.3 Monitoring After Enforcement

```markdown
## Post-Enforcement Monitoring Checklist (Weekly)

| Check | Where | Expected | Action If Abnormal |
|-------|-------|----------|-------------------|
| Verified request % | App Check dashboard | > 95% | Investigate unverified source |
| Blocked request count | App Check dashboard | Low and decreasing | Check if legitimate users are blocked |
| Client error rate | Crashlytics | No increase | Check for App Check SDK errors |
| Cloud Functions success | Functions dashboard | No decrease | Check enforcement config |
| User complaints | Play Store reviews | No App Check mentions | Review enforcement scope |
| Debug token usage | Token audit log | Only known tokens | Revoke unknown tokens |
```

#### 5.4 Security Hardening Checklist

```markdown
## Production Security Checklist

### App Check Layer
- [ ] Play Integrity provider configured for production
- [ ] Debug provider ONLY in debug builds (check BuildConfig.DEBUG)
- [ ] All services enforced (Firestore, Functions, Storage)
- [ ] Debug tokens inventoried and rotated quarterly
- [ ] CI/CD tokens stored as encrypted secrets

### Complementary Security (App Check alone is not enough)
- [ ] Firestore security rules enforce user-level access control
- [ ] Cloud Functions verify auth tokens (request.auth)
- [ ] Storage rules restrict paths and file types
- [ ] API keys restricted in Google Cloud Console
- [ ] Firebase config not exposing sensitive project details
- [ ] ProGuard/R8 enabled for release builds (code obfuscation)

### Operational Security
- [ ] Monitoring alerts set for unusual traffic patterns
- [ ] Rollback procedure documented and tested
- [ ] Incident response plan includes App Check disable as option
- [ ] Team access to Firebase Console reviewed quarterly
```

---

## Expected Output

### App Check Implementation Document

```markdown
# App Check Implementation: [App Name]

## Provider Configuration
- **Attestation provider:** Play Integrity (standard tier)
- **Min Android API:** [level]
- **App distribution:** Google Play only / Also sideloaded

## Debug Token Inventory
| Token Name | Owner | Environment | Created | Rotate By |
|-----------|-------|-------------|---------|-----------|
| [name] | [person/CI] | [dev/CI/staging] | [date] | [date] |

## Enforcement Status
| Service | Status | Enforced Since | Verified % |
|---------|--------|---------------|-----------|
| Cloud Functions | Enforced | [date] | [%] |
| Cloud Storage | Enforced | [date] | [%] |
| Firestore | Monitoring | — | [%] |

## Monitoring Results (from 2-week monitoring phase)
- Verified requests: [%]
- Unverified sources identified: [list]
- Decision: [Ready/Not ready for enforcement]

## Rollback Procedure
1. Go to Firebase Console → App Check
2. Select affected service
3. Click "Unenforce"
4. Effect is immediate

## Enforcement Rollout Timeline
- Week 1-2: Monitor only (no enforcement)
- Week 3-4: Enforce Cloud Functions
- Week 5-6: Enforce Cloud Storage
- Week 7-8: Enforce Firestore
- Week 9+: Full enforcement, ongoing monitoring

## Known Limitations
- Rooted devices: [How handled — blocked or allowed with warning]
- Sideloaded installs: [How handled]
- Emulators: [Debug tokens configured]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - App Check implementation with explicit security scope
- **ST-02** (Structured Sequential Instructions) - Phased rollout from provider setup through production hardening
- **RT-02** (Multi-Dimensional Analysis) - Provider comparison, enforcement by service type, verified vs unverified traffic analysis
- **CM-01** (Explicit Context Framing) - App Check capabilities, Play Integrity mechanics, and enforcement implications
- **DS-06** (Prioritization Guidance) - Enforcement order by service risk level, monitoring before enforcing

---

## Related Prompts

- `firebase_security_rules_generator.md` - Security rules that complement App Check at the data level
- `firebase_security_rules_audit.md` - Audit existing rules alongside App Check enforcement
- `firebase_cloud_functions_design.md` - Functions enforcement and per-function App Check
- `firebase_health_check.md` - Periodic health check including App Check status
- `android_ci_cd_pipeline_design.md` - CI/CD integration with debug tokens

---

## Customization Guide

- **For apps distributed outside Google Play:** Play Integrity requires Google Play Services. If you distribute via sideloading, F-Droid, or other stores, consider using a custom attestation provider or accept that those installs cannot be verified. You may need to implement your own server-side device verification.
- **For apps with a large rooted-device user base:** Consider a tiered enforcement approach — enforce on Cloud Functions (server-side security) but not on Firestore reads (so rooted users can still browse). Log rooted-device usage to understand the population size before deciding.
- **For apps with multiple Firebase projects (dev/staging/prod):** Each project needs its own debug tokens. Create a token naming convention that includes the environment: `ci-github-actions-prod`, `john-dev-emulator-staging`. Never share tokens across environments.
- **For apps migrating from SafetyNet:** Replace `SafetyNetAppCheckProviderFactory` with `PlayIntegrityAppCheckProviderFactory`. The API is identical — only the factory class changes. Test thoroughly because Play Integrity and SafetyNet have different device verdicts.
- **For apps with very low traffic (< 100 DAU):** The monitoring phase may not produce statistically meaningful data. Run monitoring for 4 weeks instead of 2, or use manual testing across device types to supplement the data.
