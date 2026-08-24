---
title: "Play Store Pre-Launch Checklist"
category: mobile-development
description: "Comprehensive pre-launch checklist for a new Android app covering store listing assets, developer account setup, testing requirements, app signing, content rating, pricing, and data safety"
techniques:
  - ST-01
  - ST-02
  - DT-01
  - CM-01
  - QA-01
difficulty: beginner
tags:
  - android
  - play-store
  - launch
  - checklist
  - publishing
  - mobile-development
  - solo-developer
updated: "2026-02-11"
---

# Play Store Pre-Launch Checklist

**Objective:** Provide a comprehensive pre-launch checklist for submitting a new Android app to the Google Play Store — covering developer account setup, store listing assets, testing track requirements, app signing configuration, content rating questionnaire, pricing and distribution setup, data safety section, and policy compliance — ensuring nothing is missed that could delay or prevent launch.

**When to Use:** Use this prompt 2-4 weeks before your planned launch date. The Play Store has requirements that take time to fulfill (e.g., 20 testers for 14 continuous days on the closed testing track before production access, developer identity verification). Starting this checklist early prevents launch day surprises. Also useful as a review before submitting major updates.

**Important context:** Google Play has tightened requirements significantly in 2024-2026. New developer accounts must complete identity verification, apps must meet testing track requirements before production access, and the Data Safety section must accurately reflect all data collection. This checklist reflects current requirements — but verify against the latest Play Console documentation as policies change frequently.

---

## Context Gathering

Before working through the checklist, gather essential context:

1. **Account Status:**
   - "Do you already have a Google Play Developer account?"
   - "Is your developer identity verification complete?"
   - "Is this your first app submission or have you published before?"

2. **App Details:**
   - "What is your app's name, package name, and version?"
   - "Is it free or paid? Does it have in-app purchases or subscriptions?"
   - "What is the target audience age range?"
   - "What category best fits your app?"

3. **Assets Readiness:**
   - "Do you have screenshots for your store listing?"
   - "Do you have a feature graphic (1024x500)?"
   - "Do you have a privacy policy URL?"
   - "Do you have a short description (80 chars) and full description (4000 chars)?"

4. **Technical Readiness:**
   - "Is your app built as an Android App Bundle (.aab)?"
   - "Have you configured Play App Signing?"
   - "Have you tested on multiple devices and API levels?"
   - "Is Crashlytics or equivalent crash reporting integrated?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before marking ANY checklist item as complete, you MUST:**

1. **Verify the requirement is current** — Google Play requirements change. Check the Play Console help documentation for the latest requirements.
2. **Distinguish between required and recommended** — Some items are hard requirements (will block submission), others are best practices (recommended but won't block).
3. **Account for new developer account restrictions** — New accounts have additional requirements compared to established accounts.
4. **Check for category-specific requirements** — Some app categories (health, finance, children) have additional requirements.

### False-Positive Prevention

- ❌ Do NOT skip the testing track requirements — they are mandatory for new apps and cause the most common launch delays
- ❌ Do NOT assume the Data Safety section is optional — it's required and inaccurate declarations can cause removal
- ❌ Do NOT submit without a privacy policy — required for all apps that access personal or sensitive data
- ❌ Do NOT rush the content rating questionnaire — inaccurate ratings can result in app removal
- ✅ DO start the 14-day closed testing period early — it's the most common blocker
- ✅ DO verify identity early — verification can take days to weeks
- ✅ DO test the app on the minimum supported API level
- ✅ DO proofread all store listing text — you can't quickly fix typos after approval

---

### Pre-Launch Timeline

**Recommended timeline for a first-time app submission:**

```
Week -4: Developer account + identity verification
Week -3: Testing track setup + recruit testers
Week -2: Store listing assets + Data Safety section
Week -1: Final testing + submission
Day 0:   Review approval + staged rollout
```

---

### Section 1: Developer Account (Start 4+ weeks before launch)

#### 1.1 Account Setup

- [ ] **Google Play Developer account created** ($25 one-time fee)
  - URL: https://play.google.com/console/signup
  - Use a dedicated Google account (not personal) if possible

- [ ] **Developer identity verification completed**
  - Required for all new accounts (since 2023)
  - Individual: Government ID verification
  - Organization: D-U-N-S number + business documents
  - Processing time: 2-7 business days (can take longer)
  - **Cannot publish until verification is complete**

- [ ] **Contact information configured**
  - Developer name (public — choose carefully, hard to change)
  - Contact email (public — use a professional address)
  - Contact phone (required but not public)
  - Website (recommended)

- [ ] **Payment profile linked** (if selling paid apps or IAPs)
  - Google Payments merchant account
  - Tax information (W-9 for US, W-8BEN for non-US)
  - Payout bank account configured

#### 1.2 Developer Program Policies

- [ ] **Read and acknowledged Developer Program Policies**
- [ ] **Read and acknowledged Developer Distribution Agreement**
- [ ] **Reviewed recent policy update announcements**

---

### Section 2: Testing Track Requirements (Start 3+ weeks before launch)

**This is the most common cause of launch delays for new apps.**

#### 2.1 Closed Testing Track (REQUIRED before production)

Google requires new apps to complete closed testing before production access:

- [ ] **Closed testing track created in Play Console**
  - Play Console → Testing → Closed testing → Create track

- [ ] **Minimum 20 testers enrolled**
  - Testers must opt in via the testing link
  - They must actually install and use the app
  - Can use Google Groups or email lists for tester management

- [ ] **App available on closed testing for 14+ continuous days**
  - The 14-day clock starts when the first build is published to the track
  - Upload a near-final build — don't waste this time on broken builds

- [ ] **Testers have been active** (some testing activity required)
  - Not just enrolled — they need to have actually used the app

- [ ] **Core app functionality working** during testing period
  - Critical crashes or ANRs during testing can delay production access

#### 2.2 Testing Track Build Requirements

- [ ] **Signed Android App Bundle (.aab)** uploaded
  - Not APK — Google Play requires AAB for new apps
  - Must be signed with your upload key (Play App Signing handles the rest)

- [ ] **Minimum API level requirements met**
  - New apps must target the latest required `targetSdkVersion` (check current deadline)
  - As of 2025: `targetSdkVersion` must be at least 34 for new apps

- [ ] **64-bit support included**
  - All native code must include 64-bit libraries (arm64-v8a, x86_64)

---

### Section 3: App Signing (Before first upload)

- [ ] **Play App Signing enrolled**
  - Required for all new apps
  - Google manages your app signing key
  - You upload with an upload key
  - **BACK UP YOUR UPLOAD KEY** — losing it requires contacting Google support

- [ ] **Upload key generated and stored securely**
  - Store the keystore file in a secure location (NOT in your repository)
  - Document the keystore password, key alias, and key password
  - Consider storing in a password manager

- [ ] **Signing configuration verified in build.gradle**
  ```kotlin
  android {
      signingConfigs {
          release {
              storeFile = file("path/to/keystore.jks")
              storePassword = System.getenv("KEYSTORE_PASSWORD")
              keyAlias = System.getenv("KEY_ALIAS")
              keyPassword = System.getenv("KEY_PASSWORD")
          }
      }
  }
  ```

---

### Section 4: Store Listing Assets

#### 4.1 Required Assets

| Asset | Specification | Status |
|-------|--------------|--------|
| **App name** | Max 30 characters | [ ] |
| **Short description** | Max 80 characters | [ ] |
| **Full description** | Max 4,000 characters | [ ] |
| **App icon** | 512x512 PNG, 32-bit, no alpha | [ ] |
| **Feature graphic** | 1024x500 PNG or JPEG | [ ] |
| **Screenshots (phone)** | Min 2, max 8, JPEG or PNG, 16:9 or 9:16 | [ ] |
| **Screenshots (tablet)** | Recommended if tablet-optimized, same specs | [ ] |
| **App category** | Select primary and secondary | [ ] |
| **Default language** | Set primary language | [ ] |
| **Privacy policy URL** | Public URL, must be accessible | [ ] |

#### 4.2 Recommended Assets

| Asset | Specification | Status |
|-------|--------------|--------|
| **Promo video** | YouTube URL, 30s-2min | [ ] |
| **Tablet screenshots** | 7" and 10" if relevant | [ ] |
| **Localized listings** | Translations for key markets | [ ] |

#### 4.3 Store Listing Quality Checks

- [ ] **App name is not misleading** (no "free", "best", "top" unless accurate)
- [ ] **Description focuses on benefits, not just features**
- [ ] **Screenshots show actual app UI** (not mockups that differ from the app)
- [ ] **Feature graphic is compelling and readable at small sizes**
- [ ] **No trademarked terms used without authorization**
- [ ] **No keyword stuffing in title or description**
- [ ] **All text proofread for typos and grammar**

---

### Section 5: Content Rating

- [ ] **Content rating questionnaire completed**
  - Play Console → Content rating → Start questionnaire
  - Answer honestly — misrepresentation can cause removal

- [ ] **Questionnaire answers reviewed for accuracy:**
  - [ ] Violence level correctly reported
  - [ ] Sexual content level correctly reported
  - [ ] Language/profanity level correctly reported
  - [ ] Controlled substances references accurately reported
  - [ ] User-generated content flagged if present
  - [ ] Location sharing flagged if applicable
  - [ ] Gambling elements flagged if present

- [ ] **Rating applied to app** (ESRB, PEGI, etc. — automatically assigned based on answers)

---

### Section 6: Data Safety Section

- [ ] **Data collection inventory completed** (document all data your app collects):

  **App collects directly:**
  - [ ] Name, email, phone, address
  - [ ] Photos, videos, files
  - [ ] Location (precise or approximate)
  - [ ] Financial/payment information
  - [ ] Health/fitness data
  - [ ] Messages, contacts, calendar
  - [ ] App activity, browsing history
  - [ ] Device identifiers

  **SDKs collect on your behalf:**
  - [ ] Firebase Analytics — device info, app interactions
  - [ ] Firebase Crashlytics — crash data, device info
  - [ ] AdMob — advertising ID, device info, app interactions
  - [ ] Other SDKs — document each one

- [ ] **Data sharing accurately declared**
  - If using ad SDKs: data IS shared with third parties
  - If using analytics: data is shared with Google

- [ ] **Data handling practices documented:**
  - [ ] Encryption in transit (HTTPS) — likely yes
  - [ ] Data deletion mechanism — can users request deletion?
  - [ ] Data retention period defined

- [ ] **Privacy policy URL set** and accessible
- [ ] **Data Safety section matches actual app behavior** (cross-reference with code)

---

### Section 7: Pricing and Distribution

- [ ] **Pricing model configured**
  - Free, paid, or free with in-app purchases
  - **Note:** Cannot change from paid to free and back to paid

- [ ] **Country distribution selected**
  - Select countries where app will be available
  - Consider starting with fewer countries and expanding

- [ ] **In-app products configured** (if applicable)
  - Subscription products created with pricing
  - One-time purchase products created
  - Product descriptions written
  - Grace period configured for subscriptions

- [ ] **Tax settings reviewed** (auto-handled by Google in most countries)

---

### Section 8: Technical Readiness

#### 8.1 Build Quality

- [ ] **No critical crashes** on test devices
  - Test on minimum supported API level
  - Test on latest API level
  - Test on small screens and large screens
  - Test on low-memory devices (if targeting)

- [ ] **ANR rate acceptable** (< 0.47% target)
  - No long operations on main thread
  - Network calls on background threads
  - Database operations on background threads

- [ ] **App size reasonable**
  - AAB format reduces download size
  - Check for large unused assets
  - Consider dynamic feature modules for large apps

- [ ] **ProGuard/R8 configured and tested**
  - Shrinking enabled for release builds
  - Obfuscation enabled
  - Keep rules verified (app works after minification)
  - Mapping file uploading configured for crash reports

#### 8.2 Monitoring and Crash Reporting

- [ ] **Firebase Crashlytics integrated**
  - Crash reporting active
  - Mapping file upload configured
  - Crash alerts enabled (email or Slack)

- [ ] **Firebase Analytics integrated** (if using)
  - Core events implemented
  - DebugView verified during testing

- [ ] **Firebase Performance Monitoring** (optional but recommended)
  - App startup time tracked
  - Network request monitoring active

#### 8.3 Security

- [ ] **No API keys or secrets in client code**
  - Check strings.xml, BuildConfig, and source files
  - Use Firebase Remote Config or server-side for secrets

- [ ] **Network security config** properly configured
  - HTTPS enforced for all connections
  - No cleartext traffic allowed in production

- [ ] **App Check configured** (recommended)
  - Play Integrity attestation provider
  - Debug provider for testing

---

### Section 9: Policy Compliance Final Check

- [ ] **Play Store policy compliance audit passed**
  - Use `play_store_policy_compliance_check.md` for full audit
  - All critical violations resolved

- [ ] **Permissions are justified** — no unnecessary permissions
- [ ] **Ads policy compliant** (if showing ads)
- [ ] **Billing policy compliant** (if selling digital goods)
- [ ] **Content appropriate for declared rating**
- [ ] **Target audience accurately declared**

---

### Section 10: Launch Day Preparation

- [ ] **Staged rollout planned**
  - Start at 1-5% of users
  - Monitor crash rate and ANR rate for 24-48 hours
  - Gradually increase to 20%, 50%, 100%

- [ ] **Monitoring active**
  - Crashlytics alerts configured
  - Play Console alerts enabled
  - Firebase cost monitoring active (see `firebase_cost_monitor_setup.md`)

- [ ] **Rollback plan defined**
  - Know how to halt a staged rollout
  - Previous stable version available if needed
  - Communication plan for users if rollback needed

- [ ] **Marketing ready** (if applicable)
  - Store listing optimized (see `android_play_store_optimization.md`)
  - Launch plan prepared (see `marketing_zero_budget_launch_plan.md`)
  - Social media posts drafted

- [ ] **Support ready**
  - Contact email monitored
  - FAQ or help section in app
  - Review response templates prepared

---

## Expected Output

### Pre-Launch Readiness Report

```markdown
# Pre-Launch Readiness: [App Name]

## Status: [READY / NOT READY — [N] blockers remaining]

## Blockers (Must resolve before launch)
1. [Blocker with remediation steps]
2. [Blocker with remediation steps]

## Warnings (Should resolve but won't block)
1. [Warning with recommendation]

## Section Status

| Section | Status | Blockers | Notes |
|---------|--------|----------|-------|
| Developer Account | [Ready/Not Ready] | [Count] | [Notes] |
| Testing Track | [Ready/Not Ready] | [Count] | [14-day countdown status] |
| App Signing | [Ready/Not Ready] | [Count] | |
| Store Listing | [Ready/Not Ready] | [Count] | |
| Content Rating | [Ready/Not Ready] | [Count] | |
| Data Safety | [Ready/Not Ready] | [Count] | |
| Pricing | [Ready/Not Ready] | [Count] | |
| Technical | [Ready/Not Ready] | [Count] | |
| Policy | [Ready/Not Ready] | [Count] | |
| Launch Day | [Ready/Not Ready] | [Count] | |

## Timeline
- Earliest possible launch: [Date — accounting for testing track requirement]
- Recommended launch: [Date — with buffer for review]

## Post-Launch Plan
- Staged rollout: [Percentage schedule]
- Monitoring: [What to watch]
- First update planned: [When and what]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Pre-launch verification focus
- **ST-02** (Structured Sequential Instructions) - Systematic checklist process
- **DT-01** (Hierarchical Task Breakdown) - Sections broken into actionable items
- **CM-01** (Explicit Context Framing) - Current Play Store requirements
- **QA-01** (Chain-of-Verification) - Cross-checking requirements against actual readiness

---

## Testing Planning Inputs

Before final go/no-go, import outputs from:

- `../testing/android_device_api_test_matrix_design.md` for API/device coverage exit criteria
- `../testing/android_ci_test_pipeline_optimization.md` for CI gate definitions and reliability metrics
- `../testing/android_test_flakiness_triage_quarantine.md` for quarantine status and deflake SLA
- `../analysis/android_test_coverage_analysis.md` for critical-path coverage and unresolved test gaps

Use these artifacts to confirm closed testing results are representative and release-ready.

## Related Prompts

- `play_store_policy_compliance_check.md` - Deep policy compliance audit
- `android_play_store_optimization.md` - Store listing optimization (ASO)
- `privacy_policy_generator.md` - Generate required privacy policy
- `marketing_zero_budget_launch_plan.md` - Launch marketing plan
- `firebase_cost_monitor_setup.md` - Cost monitoring before launch
- `android_target_sdk_migration.md` - Target SDK requirements

---

## Customization Guide

- **For apps targeting children:** Add Families Policy requirements, COPPA compliance checks, and certified ad SDK verification
- **For subscription apps:** Expand the in-app products section with subscription lifecycle requirements, trial terms disclosure, and cancellation accessibility
- **For apps with user-generated content:** Add content moderation requirements, reporting mechanisms, and Terms of Service verification
- **For games:** Add content rating specifics for violence/gambling, in-app purchase disclosure requirements, and loot box regulations (varies by country)
- **For enterprise/B2B apps:** Consider managed Google Play distribution, private track instead of production, and MDM compatibility testing
