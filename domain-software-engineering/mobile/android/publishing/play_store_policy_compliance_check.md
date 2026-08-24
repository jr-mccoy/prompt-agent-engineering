---
title: "Play Store Policy Compliance Check"
category: mobile-development
description: "Comprehensive audit of an Android app against Google Play Store policies covering data safety, permissions, content rating, ads, billing, and target audience requirements"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-01
  - DS-06
  - CM-01
difficulty: intermediate
tags:
  - android
  - play-store
  - compliance
  - policy
  - mobile-development
  - solo-developer
updated: "2026-02-11"
---

# Play Store Policy Compliance Check

**Objective:** Audit an Android app for comprehensive Google Play Store policy compliance, covering Data Safety section accuracy, permissions justification, content rating accuracy, ads policy, billing policy, target audience settings, and recent policy updates — producing a compliance report with remediation steps for any violations found.

**When to Use:** Use this prompt before initial app submission, before major updates, after receiving a policy violation warning, when adding new SDKs or data collection, or as a quarterly compliance review. Critical because policy violations can result in app suspension or removal — which for a solo developer means losing your entire business overnight. Google Play policy updates happen frequently, and ignorance is not a defense.

---

## Context Gathering

Before beginning the compliance audit, gather essential context:

1. **App Details:**
   - "What is your app's category and target audience?"
   - "Does your app target children under 13, or is it a 'Teacher Approved' app?"
   - "What is your app's content rating and how was it determined?"

2. **Data & SDKs:**
   - "List all third-party SDKs integrated (Firebase Analytics, Crashlytics, AdMob, Facebook SDK, etc.)"
   - "What data does your app collect from users (explicitly and implicitly)?"
   - "Do you share any data with third parties?"

3. **Monetization:**
   - "How does your app monetize (subscriptions, one-time purchases, ads, free)?"
   - "Do you offer any digital goods or subscriptions that must use Google Play Billing?"
   - "Do you display ads? If so, which ad networks?"

4. **Current Compliance State:**
   - "Have you received any policy violation warnings previously?"
   - "When was your Data Safety section last updated?"
   - "Do you have a published privacy policy linked in the Play Console?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before flagging ANY compliance issue, you MUST:**

1. **Check the actual current policy** - Google Play policies change frequently. Verify the specific policy version you're referencing.
2. **Understand the app's specific situation** - Some policies apply only to certain app categories, target audiences, or monetization models.
3. **Distinguish warnings from violations** - Some issues are policy suggestions (warnings) vs. actual violations that can cause removal.
4. **Consider regional policy differences** - Some policies vary by country or region.
5. **Provide specific policy references** - Every finding must cite the specific Google Play policy section.

**Finding the app is FULLY COMPLIANT is an acceptable outcome.** Don't manufacture violations. If the app meets all current policies, confirm this with confidence.

### False-Positive Prevention

- ❌ Do NOT flag issues based on outdated policy versions
- ❌ Do NOT apply children's policy requirements to apps that don't target children
- ❌ Do NOT flag standard analytics/crashlytics as privacy violations without checking Data Safety accuracy
- ❌ Do NOT assume all in-app transactions require Play Billing (physical goods/services are exempt)
- ✅ DO verify which policies apply to the specific app category
- ✅ DO distinguish between must-fix violations and best-practice recommendations
- ✅ DO check whether flagged SDKs are declared in the Data Safety section
- ✅ DO consider the most recent Google Play policy update dates

---

### 1. Data Safety Section Audit

The Data Safety section is one of the most common compliance failure points.

#### 1.1 Data Collection Inventory

Map ALL data your app collects, both directly and via SDKs:

**Direct data collection:**

| Data Type | Collected? | Purpose | Optional? | User Control |
|-----------|-----------|---------|-----------|--------------|
| Name | [Yes/No] | [Purpose] | [Yes/No] | [Delete/Export] |
| Email | [Yes/No] | [Purpose] | [Yes/No] | [Delete/Export] |
| Phone number | [Yes/No] | [Purpose] | [Yes/No] | [Delete/Export] |
| Address | [Yes/No] | [Purpose] | [Yes/No] | [Delete/Export] |
| Photos/Videos | [Yes/No] | [Purpose] | [Yes/No] | [Delete/Export] |
| Location (precise) | [Yes/No] | [Purpose] | [Yes/No] | [Delete/Export] |
| Location (approximate) | [Yes/No] | [Purpose] | [Yes/No] | [Delete/Export] |
| Financial/Payment info | [Yes/No] | [Purpose] | [Yes/No] | [Delete/Export] |
| Health/Fitness data | [Yes/No] | [Purpose] | [Yes/No] | [Delete/Export] |

**SDK-implicated data collection:**

| SDK | Data Collected | Shared With | Purpose |
|-----|---------------|-------------|---------|
| Firebase Analytics | App events, device info, advertising ID | Google | Analytics |
| Firebase Crashlytics | Crash data, device info, app state | Google | Stability |
| AdMob | Advertising ID, device info, location | Google + ad networks | Advertising |
| Facebook SDK | Device info, app events | Meta | Analytics/Ads |
| [Other SDK] | [Data] | [Third party] | [Purpose] |

#### 1.2 Data Safety Declaration Accuracy

**For each data type, verify:**

- [ ] Collection is accurately declared (not under-reporting)
- [ ] Sharing is accurately declared (including SDK data sharing)
- [ ] Purpose categories are correct (functionality, analytics, advertising, etc.)
- [ ] "Required" vs "optional" is correctly marked
- [ ] Data deletion mechanism exists and is described
- [ ] Encryption in transit is correctly reported

**Common Data Safety mistakes to check:**

1. **Not declaring Firebase Analytics data** — Even if you don't explicitly collect data, Analytics collects device info and app events automatically
2. **Not declaring Crashlytics data** — Crash reports contain device info, OS version, app state
3. **Not declaring advertising ID collection** — If you use AdMob or any ad SDK, the advertising ID is collected
4. **Declaring "no data shared" when using ad SDKs** — Ad SDKs share data with third parties by definition
5. **Missing "approximate location"** — IP-based location is approximate location data

---

### 2. Permissions Audit

#### 2.1 Declared Permissions Review

For each permission in AndroidManifest.xml:

| Permission | Declared | Actually Used | Justification | Policy Compliant |
|-----------|----------|--------------|---------------|-----------------|
| `INTERNET` | [Yes/No] | [Yes/No] | [Required for...] | [Yes/No] |
| `CAMERA` | [Yes/No] | [Yes/No] | [Required for...] | [Yes/No] |
| `ACCESS_FINE_LOCATION` | [Yes/No] | [Yes/No] | [Required for...] | [Yes/No] |
| `READ_CONTACTS` | [Yes/No] | [Yes/No] | [Required for...] | [Yes/No] |
| `RECORD_AUDIO` | [Yes/No] | [Yes/No] | [Required for...] | [Yes/No] |
| `READ_PHONE_STATE` | [Yes/No] | [Yes/No] | [Required for...] | [Yes/No] |

#### 2.2 High-Risk Permission Checks

**Sensitive permissions requiring specific policy justification:**

- **SMS/Call Log permissions** — Restricted. Must be declared as default handler or have approved use case
- **Background Location** — Requires separate disclosure and approval form in Play Console
- **All Files Access (MANAGE_EXTERNAL_STORAGE)** — Restricted. Must demonstrate necessity
- **Accessibility Service** — Restricted. Must be for accessibility purpose only
- **VPN Service** — Restricted. Must be core functionality
- **Device Admin** — Restricted. Must be for enterprise management

**For each high-risk permission, verify:**
- [ ] Permission is actually necessary for core app functionality
- [ ] Permission usage is disclosed to the user before request
- [ ] Play Console declaration form is submitted (if required)
- [ ] Permission is not used for undisclosed purposes

---

### 3. Content Rating Accuracy

#### 3.1 Rating Questionnaire Review

Verify the content rating questionnaire answers match the app:

- [ ] Violence content level accurately reported
- [ ] Sexual content level accurately reported
- [ ] Language/profanity level accurately reported
- [ ] Controlled substances references accurately reported
- [ ] User-generated content flagged if present
- [ ] Gambling elements flagged if present
- [ ] Content rating is appropriate for actual app content

#### 3.2 Rating Changes After Updates

- [ ] Have new features changed the appropriate content rating?
- [ ] Has user-generated content been added since last rating?
- [ ] Have ads been added that might contain mature content?

**Common mistake:** Adding user-generated content features (chat, image upload, profiles) without updating the content rating questionnaire.

---

### 4. Ads Policy Compliance

If the app displays ads:

#### 4.1 General Ads Requirements

- [ ] Ads are clearly distinguishable from app content
- [ ] Ads do not interfere with app functionality
- [ ] No deceptive ads (fake close buttons, misleading content)
- [ ] No accidental click patterns (ads too close to interactive elements)
- [ ] Interstitial ad frequency is reasonable (not every screen transition)
- [ ] Users can close interstitial ads after a reasonable time

#### 4.2 Children's Ads Policy (if applicable)

If the app targets children or is in the "Family" category:

- [ ] Only certified ad SDKs are used (Google's Families Self-Certified Ads SDK Program)
- [ ] No interest-based advertising
- [ ] No remarketing
- [ ] Ad content is appropriate for children
- [ ] No data collection for advertising purposes from children

#### 4.3 Ad SDK Compliance

- [ ] All ad SDKs are declared in the Data Safety section
- [ ] Ad mediation partners are listed
- [ ] GDPR consent mechanisms are implemented for EU users (TCF 2.0)
- [ ] CCPA opt-out is available for California users

---

### 5. Billing Policy Compliance

#### 5.1 Google Play Billing Requirement

**Must use Google Play Billing for:**
- [ ] In-app purchases of digital goods (coins, gems, premium features)
- [ ] Subscriptions to digital content or services
- [ ] Any digital product consumed within the app

**Exempt from Google Play Billing:**
- [ ] Physical goods and services (Uber rides, food delivery, physical merchandise)
- [ ] Peer-to-peer payments
- [ ] Online gambling (where legally permitted)
- [ ] Products purchased for use outside the app

#### 5.2 Subscription Requirements

If app offers subscriptions:

- [ ] Subscription terms are clearly disclosed before purchase
- [ ] Free trial terms are explicit (duration, what happens after)
- [ ] Price is clearly displayed in local currency
- [ ] Cancellation instructions are accessible within the app
- [ ] Grace period is implemented for billing failures
- [ ] Account hold is handled properly
- [ ] Users are notified before free trial converts to paid
- [ ] Annual subscription savings (vs monthly) are not misleading

#### 5.3 Refund and Cancellation

- [ ] Refund policy is documented
- [ ] Google Play's refund flow is not obstructed
- [ ] Subscription cancellation doesn't require contacting support
- [ ] Pro-rated refunds are handled per Google policy

---

### 6. Target Audience and Content

#### 6.1 Target Audience Declaration

- [ ] Target age group is accurately set in Play Console
- [ ] If targeting "Everyone" — content is suitable for all ages
- [ ] If targeting children — Families Policy requirements are met
- [ ] App does not appeal to children while containing adult content

#### 6.2 Families Policy (if targeting children under 13)

- [ ] App is enrolled in the Designed for Families program
- [ ] All ads are from certified family-safe ad networks
- [ ] No collection of personal data from children without parental consent
- [ ] Content is appropriate for the declared age range
- [ ] No links to content outside the app that is inappropriate for children
- [ ] Login is not required (or parental gate is implemented)
- [ ] In-app purchases have parental gate

#### 6.3 User-Generated Content

If the app allows user-generated content:

- [ ] Content moderation system is in place
- [ ] Reporting mechanism for inappropriate content
- [ ] Terms of use prohibit inappropriate content
- [ ] Mechanism to remove reported content
- [ ] Age-appropriate content filtering if targeting mixed audiences

---

### 7. Recent Policy Updates Check

**Review the most recent Google Play policy updates:**

Check these areas for recent changes:

- [ ] Data Safety requirements updates
- [ ] SDK requirements (minimum target SDK version)
- [ ] Photo/Video permissions policy updates
- [ ] Health data handling requirements
- [ ] Financial data handling requirements
- [ ] AI-generated content disclosure requirements
- [ ] Developer verification requirements

**Google Play deadline awareness:**
- Target SDK requirement deadline (annual, typically August 31)
- New policy enforcement dates from recent policy announcements
- Existing policy violation remediation deadlines

---

### 8. App Metadata Compliance

#### 8.1 Store Listing Content

- [ ] Title does not contain misleading claims or excessive keywords
- [ ] Description does not reference other apps/platforms for promotion
- [ ] Screenshots accurately represent the app (not deceptive)
- [ ] App icon follows guidelines (no badges, no misleading elements)
- [ ] No use of "free" in the title if app has in-app purchases
- [ ] No claim of awards or ratings not independently verified

#### 8.2 APK/Bundle Requirements

- [ ] App targets required minimum SDK version
- [ ] 64-bit support is included
- [ ] App Bundle format is used (not just APK)
- [ ] Deobfuscation file is uploaded for crash reporting
- [ ] App signing by Google Play is configured

---

## Expected Output

### Play Store Policy Compliance Report

```markdown
# Play Store Policy Compliance Report

## App Overview
- **App name:** [Name]
- **Package:** [com.example.app]
- **Category:** [Category]
- **Target audience:** [Age range]
- **Monetization:** [Model]
- **Last policy review:** [Date]

## Compliance Status: [PASS / PASS WITH WARNINGS / FAIL]

## Critical Violations (Must Fix Before Release)

### VIOLATION-1: [Title]
**Policy:** [Specific Google Play policy section]
**Issue:** [Description]
**Risk:** App removal / suspension
**Remediation:** [Specific steps to fix]
**Deadline:** [If applicable]

## Warnings (Should Fix)

### WARNING-1: [Title]
**Policy:** [Specific policy section]
**Issue:** [Description]
**Risk:** Future enforcement / user trust
**Remediation:** [Steps to fix]

## Section-by-Section Results

| Section | Status | Issues | Priority |
|---------|--------|--------|----------|
| Data Safety | [Pass/Fail] | [Count] | [P0/P1/P2] |
| Permissions | [Pass/Fail] | [Count] | [P0/P1/P2] |
| Content Rating | [Pass/Fail] | [Count] | [P0/P1/P2] |
| Ads Policy | [Pass/Fail/N/A] | [Count] | [P0/P1/P2] |
| Billing Policy | [Pass/Fail/N/A] | [Count] | [P0/P1/P2] |
| Target Audience | [Pass/Fail] | [Count] | [P0/P1/P2] |
| Metadata | [Pass/Fail] | [Count] | [P0/P1/P2] |
| Recent Policies | [Pass/Fail] | [Count] | [P0/P1/P2] |

## Data Safety Accuracy Matrix

| Data Type | Actually Collected | Declared | Accurate |
|-----------|-------------------|----------|----------|
| [Type] | [Yes/No] | [Yes/No] | [Match/Mismatch] |

## Remediation Plan

### Immediate (Before Next Release)
1. [Action with specific steps]

### Short-term (Within 30 Days)
1. [Action with specific steps]

### Ongoing
1. [Recurring review action]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Policy compliance audit focus
- **ST-02** (Structured Sequential Instructions) - Systematic policy review
- **RT-02** (Multi-Dimensional Analysis) - Multiple policy dimensions
- **RT-05** (Evidence-Based Reasoning) - Specific policy citations
- **QA-01** (Chain-of-Verification) - Cross-check declarations vs. reality
- **DS-06** (Prioritization Guidance) - Severity-based issue ordering
- **CM-01** (Explicit Context Framing) - App-specific policy applicability

---

## Related Prompts

- `android_privacy_compliance.md` - Deep dive into privacy-specific compliance (GDPR, CCPA)
- `android_play_store_optimization.md` - Store listing optimization (ASO)
- `play_store_data_safety_generator.md` - Generate accurate Data Safety section (planned)
- `android_release_preparation.md` - Release readiness checklist
- `mobile_app_security_review.md` - Security review

---

## Customization Guide

- **For children's apps:** Expand Section 6 (Families Policy) significantly; add COPPA compliance depth
- **For subscription apps:** Expand Section 5 (Billing) with detailed subscription lifecycle compliance
- **For ad-supported apps:** Expand Section 4 (Ads) with mediation compliance and consent framework details
- **For health/fitness apps:** Add health data handling requirements and FDA/regulatory considerations
- **For financial apps:** Add PCI-DSS considerations and financial data handling requirements
- **For apps with user-generated content:** Expand content moderation requirements and reporting mechanisms
