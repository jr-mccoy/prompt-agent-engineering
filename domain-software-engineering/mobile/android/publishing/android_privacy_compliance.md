---
title: "Android Privacy Compliance"
category: mobile-development
description: "Android Privacy Compliance"
tags:
  - android
  - mobile-development
updated: "2026-03-19"
---

# Android Privacy Compliance

> Part of the end-to-end flow: see [`android_release_governance_runbook.md`](android_release_governance_runbook.md).

**Objective:** Audit an Android application for privacy compliance with GDPR, CCPA, Google Play Store policies, and other major privacy regulations, providing a remediation plan for any violations found.

**When to Use:** Use this prompt before releasing an app to the Play Store, when expanding to new markets (especially EU/California), when integrating new SDKs that collect user data, or during periodic privacy audits. Essential for apps that collect personal data, use analytics, display ads, or have user accounts. This audit helps avoid Play Store rejection and legal compliance issues.

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

Before beginning the compliance audit, gather essential context:

1. **App Category:**
   - "What category of app is this (social, fintech, health, children, etc.)?"
   - "Does the app target children under 13 (COPPA) or under 16 (GDPR)?"

2. **Data Collection:**
   - "What types of user data does the app collect (email, location, health, financial)?"
   - "Do you use any third-party analytics, advertising, or crash reporting SDKs?"

3. **Target Markets:**
   - "Where will this app be available (US, EU, California, global)?"
   - "Are there specific compliance requirements you're already aware of?"

4. **Current State:**
   - "Do you have an existing privacy policy? Is it published online?"
   - "Have you implemented any consent mechanisms already?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before flagging ANY compliance issue, you MUST:**

1. **Trace actual data collection** - Don't flag compliance issues without confirming what data is actually collected.
2. **Check for existing compliance** - Search for privacy policies, consent mechanisms, or Data Safety Section entries that may already exist.
3. **Understand the context** - Consider the app's target markets, user base, and actual data flows.
4. **Confirm actual requirements** - Does this regulation actually apply to this app and its markets?
5. **Provide specific locations** - Every finding must reference exact code, SDKs, or configurations.

**Finding the app is ALREADY COMPLIANT is an acceptable outcome.** If privacy practices meet requirements, say so with confidence.

### False-Positive Prevention

- ❌ Do NOT flag all data collection as problematic without understanding purpose
- ❌ Do NOT assume GDPR applies to apps not available in EU
- ❌ Do NOT report SDK data collection without checking if it's actually enabled
- ❌ Do NOT recommend consent for data collection that doesn't require it
- ✅ DO verify which regulations actually apply to the app
- ✅ DO check SDK configurations for data collection settings
- ✅ DO understand the difference between necessary and optional data collection
- ✅ DO consider Play Console Data Safety Section requirements

---

### Phase 1: Data Collection Inventory

Create a comprehensive inventory of all data collection in the app.

#### 1.1 First-Party Data Collection

**Search for data collection patterns:**

```kotlin
// Patterns to search for:
- User registration/login (email, name, phone)
- Profile information storage
- Location access (GPS, network)
- Camera/microphone access
- Contact access
- Storage access
- Biometric data
- Health/fitness data
- Financial information
- Device identifiers
```

**Document for each data type:**
| Data Type | Collection Point | Storage Location | Purpose | Retention |
|-----------|-----------------|------------------|---------|-----------|
| [Type] | [file:line] | [local/remote] | [purpose] | [duration] |

#### 1.2 Third-Party SDK Data Collection

**Audit all third-party SDKs:**

```
Common data-collecting SDKs:
├── Analytics (Firebase, Amplitude, Mixpanel)
├── Crash Reporting (Crashlytics, Sentry, Bugsnag)
├── Advertising (AdMob, Facebook Ads, AppLovin)
├── Social (Facebook Login, Google Sign-In)
├── Attribution (AppsFlyer, Adjust, Branch)
├── Push Notifications (Firebase, OneSignal)
└── Customer Support (Intercom, Zendesk)
```

**Document for each SDK:**
| SDK | Data Collected | Data Shared With | Privacy Policy | GDPR Compliant |
|-----|---------------|------------------|----------------|----------------|
| [SDK] | [types] | [parties] | [URL] | [Yes/No/Partial] |

#### 1.3 Automatic Data Collection

**Check for automatic collection:**

```kotlin
// Items that may collect data automatically:
- Advertising ID (AAID)
- Device information (model, OS version)
- IP address logging
- App usage analytics
- Crash/error logs with user context
- Network request logging
```

---

### Phase 2: GDPR Compliance Audit (EU)

Verify compliance with General Data Protection Regulation requirements.

#### 2.1 Lawful Basis for Processing

**For each data type, verify lawful basis:**

```
GDPR Lawful Bases:
1. Consent - User explicitly agreed
2. Contract - Necessary for service delivery
3. Legal Obligation - Required by law
4. Vital Interests - Protect someone's life
5. Public Task - Official function
6. Legitimate Interests - Business need (with balance test)
```

**Evaluate:**
- [ ] Each data collection has identified lawful basis
- [ ] Consent is not bundled (separate consents for different purposes)
- [ ] Consent is freely given (not a condition of service unless necessary)
- [ ] Consent can be withdrawn as easily as it was given

#### 2.2 Consent Implementation

**Verify consent mechanisms:**

```kotlin
// Required consent UI elements:
- Clear explanation of what data is collected
- Purpose of collection explained
- Third parties receiving data listed
- Accept and Reject buttons equally prominent
- Granular consent options (analytics, ads, etc.)
- No pre-checked boxes
- Consent timestamp recording
```

**Code patterns to verify:**

```kotlin
// Good: Explicit consent before data collection
if (consentManager.hasConsent(ConsentType.ANALYTICS)) {
    FirebaseAnalytics.getInstance(context).setAnalyticsCollectionEnabled(true)
}

// Bad: Collecting before consent
FirebaseAnalytics.getInstance(context).setAnalyticsCollectionEnabled(true)
// ... later asking for consent
```

**Evaluate:**
- [ ] Consent is obtained before data collection begins
- [ ] Consent UI clearly explains data usage
- [ ] Users can decline without losing core functionality
- [ ] Consent preferences are persisted
- [ ] Consent can be changed in app settings

#### 2.3 User Rights Implementation

**Verify support for GDPR rights:**

```
Required rights:
1. Right to Access - Export user data
2. Right to Rectification - Edit personal data
3. Right to Erasure - Delete account and data
4. Right to Portability - Download data in standard format
5. Right to Object - Opt out of processing
6. Right to Restrict Processing - Limit data use
```

**Evaluate:**
- [ ] Data export functionality exists or is documented
- [ ] Account deletion is available in-app or via clear process
- [ ] Users can update their personal information
- [ ] Opt-out mechanisms exist for non-essential processing
- [ ] Process for handling rights requests is documented

#### 2.4 Data Protection Measures

**Verify technical measures:**

```kotlin
// Required measures:
- Encryption at rest (EncryptedSharedPreferences, encrypted databases)
- Encryption in transit (HTTPS only, certificate pinning for sensitive data)
- Access controls (authentication before accessing personal data)
- Data minimization (only collect what's needed)
- Storage limitation (automatic deletion of old data)
```

**Evaluate:**
- [ ] Personal data is encrypted at rest
- [ ] All network traffic uses HTTPS
- [ ] Sensitive data has additional protection
- [ ] Data is automatically purged after retention period
- [ ] Pseudonymization used where possible

---

### Phase 3: CCPA Compliance Audit (California)

Verify compliance with California Consumer Privacy Act.

#### 3.1 Notice Requirements

**Verify notice at collection:**

```
CCPA requires disclosure of:
1. Categories of personal information collected
2. Purposes for collection
3. Categories shared with third parties
4. Whether information is sold (and to whom)
```

**Evaluate:**
- [ ] Privacy policy lists all categories of PI collected
- [ ] Purpose for each category is explained
- [ ] Third-party sharing is disclosed
- [ ] "Sale" of information is disclosed (if applicable)
- [ ] Notice is provided at or before collection

#### 3.2 Consumer Rights

**Verify CCPA rights implementation:**

```
Required rights:
1. Right to Know - What PI is collected
2. Right to Delete - Request deletion
3. Right to Opt-Out - No sale of PI
4. Right to Non-Discrimination - Same service regardless of rights exercise
```

**Evaluate:**
- [ ] Users can request their data
- [ ] Users can request deletion
- [ ] "Do Not Sell My Personal Information" option exists (if selling)
- [ ] Service is not degraded for users who exercise rights

#### 3.3 Do Not Sell Implementation

**If applicable, verify opt-out:**

```kotlin
// "Sale" under CCPA includes sharing data with third parties
// for monetary or other valuable consideration

// Required implementation:
- Prominent "Do Not Sell My Personal Information" link
- Functional opt-out mechanism
- Respect Global Privacy Control (GPC) signal
- Annual reminder for opted-out users
```

---

### Phase 4: Google Play Store Policy Compliance

Verify compliance with Play Store privacy requirements.

#### 4.1 Data Safety Section Requirements

**Prepare Data Safety section responses:**

```
Play Console requires disclosure of:
├── Data types collected
│   ├── Location (approximate, precise)
│   ├── Personal info (name, email, phone, address)
│   ├── Financial info (payment info, purchase history)
│   ├── Health and fitness
│   ├── Messages (emails, texts)
│   ├── Photos/videos
│   ├── Audio files
│   ├── Files and docs
│   ├── Calendar
│   ├── Contacts
│   ├── App activity (interactions, search history)
│   ├── Web browsing
│   ├── App info and performance (crash logs, diagnostics)
│   └── Device or other IDs
├── Data usage purposes
│   ├── App functionality
│   ├── Analytics
│   ├── Developer communications
│   ├── Advertising/marketing
│   ├── Fraud prevention/security
│   ├── Personalization
│   └── Account management
├── Data sharing
│   ├── Shared with third parties
│   └── Third party names/categories
├── Data handling practices
│   ├── Data encrypted in transit
│   ├── Data deletion available
│   └── Data encrypted at rest
```

**Generate Data Safety declaration:**

| Data Type | Collected | Shared | Purpose | Optional |
|-----------|-----------|--------|---------|----------|
| [Type] | Yes/No | Yes/No | [Purpose] | Yes/No |

#### 4.2 Privacy Policy Requirements

**Verify privacy policy compliance:**

```
Privacy policy must:
- Be publicly accessible (valid URL)
- Clearly identify the app/developer
- Describe data collection comprehensively
- Explain data usage purposes
- Disclose third-party sharing
- Explain user rights and how to exercise them
- Include contact information
- Specify data retention practices
- Be updated when practices change
```

**Evaluate:**
- [ ] Privacy policy URL is valid and accessible
- [ ] Policy is linked in Play Store listing
- [ ] Policy is accessible within the app
- [ ] Policy matches actual app behavior
- [ ] Policy is written in understandable language
- [ ] Policy has been updated for current app version

#### 4.3 Families Policy (if applicable)

**If targeting children:**

```
Requirements for apps in Families program:
- No behavioral advertising
- No personally identifiable info collection without consent
- Comply with COPPA
- Use appropriate ad SDKs (family-safe certified)
- Limited data collection
- Parental consent for certain features
```

**Evaluate:**
- [ ] App correctly declares target audience
- [ ] Age screening is implemented if needed
- [ ] Parental consent implemented for children
- [ ] Only family-safe SDKs are used
- [ ] No behavioral advertising to children

#### 4.4 Permissions Policy

**Verify permissions comply with policy:**

```
Play Store permission requirements:
- Only request permissions needed for declared functionality
- Provide runtime permission rationale
- Handle permission denial gracefully
- Don't request permissions at install time only for later use
- Special scrutiny for sensitive permissions (SMS, Call Log, Location)
```

**Evaluate:**
- [ ] All permissions are justified by app functionality
- [ ] No permissions requested "just in case"
- [ ] Sensitive permission use is declared in Play Console
- [ ] Runtime permission flow is user-friendly

---

### Phase 5: Consent Management Implementation

Provide guidance for implementing proper consent management.

#### 5.1 Consent Architecture

**Recommended implementation:**

```kotlin
// ConsentManager.kt
class ConsentManager @Inject constructor(
    private val preferences: EncryptedSharedPreferences
) {
    enum class ConsentType {
        ESSENTIAL,      // Required for app function, no consent needed
        ANALYTICS,      // Usage analytics
        ADVERTISING,    // Personalized ads
        THIRD_PARTY     // Third-party data sharing
    }

    data class ConsentRecord(
        val type: ConsentType,
        val granted: Boolean,
        val timestamp: Long,
        val version: String  // Consent UI version for audit
    )

    fun hasConsent(type: ConsentType): Boolean
    fun setConsent(type: ConsentType, granted: Boolean)
    fun getConsentRecords(): List<ConsentRecord>
    fun withdrawAllConsent()
}
```

#### 5.2 Consent UI Requirements

**UI checklist:**

- [ ] Clear header explaining consent request
- [ ] Purpose for each consent type explained
- [ ] List of third parties that will receive data
- [ ] Accept and Reject buttons equally visible
- [ ] Link to full privacy policy
- [ ] "Manage preferences" for granular control
- [ ] Accessible (proper contrast, screen reader support)
- [ ] Available in all supported languages

#### 5.3 Consent Integration Points

**Where to check consent:**

```kotlin
// Before initializing SDKs
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Essential SDKs - no consent needed
        initializeCrashReporting() // anonymized crashes

        // Consent-gated SDKs
        if (consentManager.hasConsent(ConsentType.ANALYTICS)) {
            initializeAnalytics()
        }
        if (consentManager.hasConsent(ConsentType.ADVERTISING)) {
            initializeAds()
        }
    }
}
```

---

### Phase 6: Findings Presentation

**CHECKPOINT 1:** Present the privacy compliance assessment.

```markdown
## Privacy Compliance Assessment

### Overall Compliance Status: [Compliant/Needs Work/Non-Compliant]

### Regulation Summary
| Regulation | Status | Critical Issues | Warnings |
|------------|--------|-----------------|----------|
| GDPR | [Status] | [Count] | [Count] |
| CCPA | [Status] | [Count] | [Count] |
| Play Store | [Status] | [Count] | [Count] |
| COPPA | [N/A or Status] | [Count] | [Count] |

### Data Collection Inventory
[Summary table of all data collection]

### Critical Compliance Issues
1. **[Issue]** - [Regulation violated] - [Location] - [Remediation]
2. **[Issue]** - [Regulation violated] - [Location] - [Remediation]

### Warnings
1. **[Issue]** - [Recommendation]
2. **[Issue]** - [Recommendation]

### Remediation Priority
1. [Highest priority fix]
2. [Second priority]
3. [Third priority]

**Would you like me to help implement the compliance fixes?**
```

---

### Phase 7: Remediation Implementation

After presenting findings, help implement fixes.

#### 7.1 Privacy Policy Updates

**Generate required policy sections:**

```markdown
## Data We Collect

### Information You Provide
- Account information (email, name) - used for authentication
- Profile information - used to personalize your experience
- [Additional items based on audit]

### Information Collected Automatically
- Device information (model, OS version) - used for compatibility
- Usage analytics - used to improve the app
- Crash reports - used to fix bugs
- [Additional items based on audit]

### Information from Third Parties
- [List any third-party data sources]

## How We Use Your Information
[Generated based on actual app usage]

## How We Share Your Information
[Generated based on SDK audit]

## Your Rights and Choices
[Generated based on applicable regulations]

## Contact Us
[Developer contact information]
```

#### 7.2 Consent Implementation

**Provide implementation code:**

```kotlin
// Implement consent check before SDK initialization
// Implement consent UI flow
// Implement preference management
// Implement consent withdrawal
```

#### 7.3 Data Safety Declaration

**Generate Play Console responses:**

```
Data Safety Section Responses:
[Generated based on data collection audit]
```

---

## Expected Output

### Privacy Compliance Report

```markdown
# Privacy Compliance Report: [App Name]

## Executive Summary
- **Overall Status:** [Compliant/Needs Work]
- **Primary Regulation:** [GDPR/CCPA/Both]
- **Risk Level:** [Low/Medium/High]

## Data Collection Inventory

### First-Party Data
| Data Type | Purpose | Legal Basis | Retention |
|-----------|---------|-------------|-----------|
| [Type] | [Purpose] | [Basis] | [Period] |

### Third-Party SDKs
| SDK | Data Types | Shared With | Compliant |
|-----|------------|-------------|-----------|
| [SDK] | [Types] | [Parties] | [Yes/No] |

## Compliance Status

### GDPR (EU)
- Lawful Basis: [Documented/Missing]
- Consent: [Implemented/Missing/Partial]
- User Rights: [Implemented/Missing/Partial]
- Data Protection: [Adequate/Needs Work]

### CCPA (California)
- Notice: [Adequate/Missing]
- Rights: [Implemented/Missing]
- Opt-Out: [N/A/Implemented/Missing]

### Play Store
- Data Safety: [Ready/Needs Update]
- Privacy Policy: [Adequate/Needs Update]
- Permissions: [Justified/Issues]

## Required Actions
1. [Action with priority and location]
2. [Action with priority and location]

## Generated Artifacts
- [ ] Privacy Policy sections
- [ ] Data Safety declaration
- [ ] Consent implementation code
```

---

## Example Interaction

**User:** Please audit my social fitness app for privacy compliance. We're launching in the US and EU, and we use Firebase Analytics and AdMob.

**Agent:** I'll conduct a comprehensive privacy compliance audit. Let me start by inventorying your data collection.

*[Agent searches codebase for data collection patterns]*

**Agent:**

## Privacy Compliance Assessment

### Data Collection Found

**First-Party:**
- Email, name, profile photo (registration)
- Fitness activities and metrics (core feature)
- Location data (workout tracking)
- Friend connections (social feature)

**Third-Party SDKs:**
| SDK | Data Collected | Concern Level |
|-----|---------------|---------------|
| Firebase Analytics | Device ID, app usage, user properties | Medium |
| AdMob | Advertising ID, usage for targeting | High |
| Firebase Auth | Email, auth tokens | Low |
| Crashlytics | Device info, crash context | Low |

### Critical Issues Found

**1. No Consent Before SDK Initialization** - `MyApplication.kt:23`
- Firebase Analytics and AdMob initialize before any consent is obtained
- **GDPR Violation:** Processing without lawful basis
- **Fix:** Delay SDK init until consent is obtained

**2. Location Tracking Without Adequate Consent** - `WorkoutTracker.kt:45`
- Precise location collected for workouts
- Privacy policy doesn't mention location tracking
- **GDPR Violation:** Transparency requirement
- **Fix:** Update privacy policy, add location-specific consent

**3. No Data Deletion Mechanism**
- No way for users to delete their account and data
- **GDPR Violation:** Right to erasure
- **CCPA Violation:** Right to delete
- **Fix:** Implement account deletion flow

### Warnings

1. **Health data collection** - Fitness metrics may be considered health data under GDPR, requiring explicit consent
2. **AdMob in EU** - Ensure TCF 2.0 consent is implemented for EU users
3. **Privacy policy outdated** - Last updated 2022, doesn't reflect current data practices

### Remediation Priority
1. Implement consent management (blocks release)
2. Add account deletion (blocks EU release)
3. Update privacy policy
4. Prepare Data Safety declaration

**Would you like me to help implement the consent management system first?**

---

## Techniques Used

- **ST-01** (Clear Objective): Specific objective defining privacy compliance scope
- **ST-02** (Sequential Instructions): Phased audit through each regulation
- **RT-02** (Multi-Dimensional Analysis): Coverage of GDPR, CCPA, Play Store, COPPA
- **RT-04** (Best Practice Review): Privacy best practices evaluation
- **RT-05** (Evidence-Based Reasoning): File:line references for violations
- **ST-03** (Output Format Templates): Compliance report structure
- **OC-05** (Severity Classification): Critical/Warning categorization
- **AG-02** (Skeptical Default Stance): Thorough violation identification
- **AG-12** (Quantitative Metrics): Compliance status scoring
- **NE-02** (Phased Workflow): Checkpoints for user input
- **NE-07** (Discussion Before Action): Remediation guidance based on findings

---

## Related Prompts

- [android_release_preparation.md](android_release_preparation.md) - Complete release checklist
- [android_play_store_optimization.md](android_play_store_optimization.md) - Store listing optimization
- android_security_audit.md - Security assessment
- [android_data_layer_implementation.md](../implementation/android_data_layer_implementation.md) - Secure data handling

---

## Customization Guide

### For Different Regulations

**GDPR Focus (EU Market):**
- Emphasize consent mechanisms
- Verify all user rights are implementable
- Check Data Protection Officer requirement
- Verify international data transfer compliance

**CCPA Focus (California Market):**
- Focus on "sale" of information disclosure
- Implement Do Not Sell mechanism
- Verify non-discrimination provisions
- Check financial incentive disclosures

**COPPA Focus (Children's Apps):**
- Stricter consent requirements (parental)
- Limit data collection
- No behavioral advertising
- Verify safe harbor compliance

### For Different App Categories

**Health/Fitness Apps:**
- Health data requires explicit consent (GDPR special category)
- HIPAA may apply in healthcare contexts
- Apple Health/Google Fit integration considerations

**Fintech Apps:**
- PCI-DSS for payment data
- Strong customer authentication requirements
- Financial regulation compliance (varies by region)

**Social Apps:**
- User-generated content considerations
- Minor user protections
- Content moderation data practices

### For Different SDK Profiles

**Heavy Analytics:**
- Ensure anonymization options are enabled
- Implement sampling for privacy
- Provide analytics opt-out

**Ad-Supported:**
- Implement consent management platform (CMP)
- Support TCF 2.0 for EU
- Implement ATT for iOS cross-platform apps

**Minimal Data Collection:**
- Consider privacy-first positioning
- Highlight in store listing
- Simpler compliance requirements
