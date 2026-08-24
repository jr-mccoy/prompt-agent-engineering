---
title: "Privacy Policy Generator for Android Apps"
category: mobile-development
description: "Generate a comprehensive privacy policy for an Android app covering data collection inventory, GDPR, CCPA, COPPA, and Google Play Store requirements"
techniques:
  - ST-01
  - ST-02
  - CM-01
  - CM-02
  - RT-02
  - QA-01
difficulty: beginner
tags:
  - android
  - privacy
  - legal
  - compliance
  - play-store
  - solo-developer
updated: "2026-02-11"
---

# Privacy Policy Generator for Android Apps

**Objective:** Generate a comprehensive, legally-informed privacy policy for an Android app that accurately inventories all data collection (including third-party SDKs like Firebase, AdMob, and Crashlytics), addresses GDPR (EU), CCPA (California), COPPA (children under 13) requirements as applicable, and satisfies Google Play Store privacy policy requirements.

**When to Use:** Use this prompt when launching a new Android app, when adding new SDKs or data collection features, when expanding to new markets (EU, California), when your existing privacy policy is outdated, or when you've received a Play Store policy warning about your privacy policy. Every app on the Play Store needs a privacy policy — this generates one that's accurate, comprehensive, and compliant.

**Important disclaimer:** This prompt generates a privacy policy document based on your app's data practices. It is NOT a substitute for legal counsel. For apps handling sensitive data (health, financial, children's data) or operating in heavily regulated industries, have an attorney review the generated policy.

---

## Context Gathering

Before generating the privacy policy, gather ALL of the following:

1. **Business Information:**
   - "What is your business name or developer name?"
   - "What is your business entity type (sole proprietor, LLC, corporation)?"
   - "What is your contact email for privacy inquiries?"
   - "What country/state is your business registered in?"

2. **App Information:**
   - "What is the app name?"
   - "What does the app do (brief description)?"
   - "What platforms is the app on (Android only, or also iOS/web)?"

3. **Data Collection — Explicit:**
   - "What data do you directly ask users to provide?"
     - Account information (name, email, phone, password)
     - Profile information (photo, bio, preferences)
     - Content (photos, videos, documents, messages)
     - Payment information (handled via Play Billing or direct)
     - Location data (precise GPS, approximate, or none)
     - Health/fitness data
     - Financial data
     - Other

4. **Data Collection — Third-Party SDKs:**
   - "Which of these SDKs does your app include?"
     - Firebase Analytics
     - Firebase Crashlytics
     - Firebase Cloud Messaging (push notifications)
     - Firebase Remote Config
     - Google AdMob
     - Google Sign-In
     - Facebook SDK
     - Adjust / AppsFlyer / Branch (attribution)
     - Sentry / Bugsnag (error tracking)
     - Mixpanel / Amplitude (analytics)
     - Stripe / other payment processors
     - Other

5. **Data Sharing:**
   - "Do you share user data with any third parties beyond SDK providers?"
   - "Do you sell user data? (This must be disclosed under CCPA)"
   - "Do you use data for advertising personalization?"

6. **Target Audience:**
   - "Is this app directed at children under 13?"
   - "Could children reasonably use this app even if not targeted at them?"

7. **Data Retention and Deletion:**
   - "How long do you keep user data?"
   - "Can users request deletion of their data?"
   - "What happens to user data when they delete the app or their account?"

8. **Security Measures:**
   - "Is data encrypted in transit (HTTPS)?"
   - "Is data encrypted at rest?"
   - "Where is data stored (Firebase, your own servers, etc.)?"

---

## Instructions

### CRITICAL: Accuracy Requirements

**Before generating the privacy policy, you MUST:**

1. **Inventory ALL data collection** - The biggest legal risk is failing to disclose data you actually collect. Under-reporting is worse than over-reporting.
2. **Include SDK-implicit data collection** - Even if you never call an analytics API explicitly, Firebase Analytics collects device info, app events, and crash data automatically once included.
3. **Distinguish between collection and sharing** - Collecting data for your own use vs. sharing with third parties have different disclosure requirements.
4. **Match the Play Store Data Safety section** - The privacy policy and Data Safety declarations must be consistent. Mismatches trigger policy reviews.
5. **Use plain language** - Privacy policies must be understandable by normal users, not just lawyers.

### False-Positive Prevention

- ❌ Do NOT include data types the app doesn't actually collect (over-reporting creates confusion)
- ❌ Do NOT use boilerplate language that doesn't match the actual app
- ❌ Do NOT claim data practices that aren't implemented (e.g., "we encrypt all data" if you don't)
- ❌ Do NOT include COPPA sections if the app has no relation to children
- ✅ DO include all SDK-collected data even if the developer isn't aware of it
- ✅ DO specify the actual data retention period (not "reasonable period")
- ✅ DO provide actual contact information (not placeholder)
- ✅ DO specify the effective date and how updates are communicated

---

### Policy Structure

Generate the privacy policy with the following sections:

#### Section 1: Introduction
- App name and developer/business name
- What this policy covers
- Effective date
- How to contact about privacy concerns

#### Section 2: Information We Collect

**2a. Information you provide directly:**
For each data type collected, state:
- What data
- Why it's collected
- Whether it's required or optional

**2b. Information collected automatically:**
For each SDK or automatic collection:
- What data is collected
- What SDK/service collects it
- Why it's collected
- How it's used

**2c. Information from third parties:**
If applicable:
- What data
- From whom
- Why

#### Section 3: How We Use Your Information
List all purposes:
- Providing and maintaining the service
- Improving the app
- Analytics and performance monitoring
- Advertising (if applicable)
- Communications (push notifications, email)
- Security and fraud prevention

#### Section 4: How We Share Your Information
For each third party:
- Who the data is shared with
- What data is shared
- Why it's shared
- Link to their privacy policy

**Common third parties to disclose:**
| Service | Data Shared | Purpose | Privacy Policy |
|---------|------------|---------|----------------|
| Google (Firebase Analytics) | App usage, device info | Analytics | [Google Privacy Policy] |
| Google (Crashlytics) | Crash data, device info | Stability | [Google Privacy Policy] |
| Google (AdMob) | Ad interactions, device ID | Advertising | [Google Privacy Policy] |
| [Other] | [Data] | [Purpose] | [Link] |

#### Section 5: Data Retention
- How long data is kept
- Criteria for retention period
- What happens when data is no longer needed
- Account deletion data handling

#### Section 6: Your Rights

**For all users:**
- Right to access your data
- Right to correct inaccurate data
- Right to delete your data
- How to exercise these rights

**For EU/EEA users (GDPR):**
- Legal basis for processing (consent, legitimate interest, contract)
- Right to data portability
- Right to restrict processing
- Right to object to processing
- Right to withdraw consent
- Right to lodge complaint with supervisory authority
- Data Protection Officer contact (if applicable)

**For California users (CCPA/CPRA):**
- Right to know what data is collected
- Right to delete personal information
- Right to opt-out of sale of personal information
- Right to non-discrimination for exercising rights
- "Do Not Sell or Share My Personal Information" instructions
- Authorized agent provisions

#### Section 7: Children's Privacy
- Whether the app is directed at children under 13
- If yes: COPPA compliance details, parental consent mechanism
- If no: Statement that app is not intended for children under 13, and what happens if children's data is inadvertently collected

#### Section 8: Data Security
- Encryption in transit (TLS/SSL)
- Encryption at rest (if applicable)
- Access controls
- Acknowledgment that no method is 100% secure

#### Section 9: International Data Transfers
- Where data is stored/processed
- Transfer mechanisms (for GDPR: Standard Contractual Clauses, adequacy decisions)
- Firebase/GCP data processing locations

#### Section 10: Changes to This Policy
- How users will be notified of changes
- When changes take effect
- Where to find the latest version

#### Section 11: Contact Information
- Email address for privacy inquiries
- Business name and address (required by GDPR)
- Response timeframe commitment

---

### Formatting Requirements

The generated policy should:
- Use plain language (8th grade reading level)
- Include a "Last Updated" date
- Use clear section headings for easy navigation
- Bold key terms and rights
- Provide a brief summary/TL;DR at the top for key points
- Include links to third-party privacy policies
- Be formatted as web-publishable HTML or Markdown

---

## Expected Output

```markdown
# Privacy Policy for [App Name]

**Last Updated:** [Date]
**Effective Date:** [Date]

## Summary

[App Name] collects [brief description of data types] to [brief purpose]. We use third-party services including [list]. We do not sell your personal information. You can request deletion of your data by [method].

---

## 1. Introduction

[App Name] ("we," "us," or "our") operates the [App Name] mobile application (the "App"). This Privacy Policy describes how we collect, use, disclose, and protect your information when you use our App.

**Developer:** [Business Name]
**Contact:** [Email]

---

## 2. Information We Collect

### Information You Provide
- **Account Information:** [What and why]
- **[Other Category]:** [What and why]

### Information Collected Automatically
- **Usage Data:** We collect information about how you use the App, including [specifics].
- **Device Information:** [What device data is collected]
- **Crash Data:** We use [Crashlytics/Sentry] to collect crash reports including [specifics].

### Third-Party SDK Data Collection
| Service | Data Collected | Purpose |
|---------|---------------|---------|
| [Service] | [Data] | [Purpose] |

---

## 3. How We Use Your Information

We use your information to:
- [Purpose 1]
- [Purpose 2]
- [Purpose 3]

---

## 4. How We Share Your Information

We share your information with:
- **[Service Provider]:** [What data, why, link to their policy]

We do not sell your personal information.

---

## 5. Data Retention

We retain your information for [period]. When you delete your account, we [action] within [timeframe].

---

## 6. Your Rights

### All Users
You have the right to:
- **Access** your personal data
- **Correct** inaccurate data
- **Delete** your data

To exercise these rights, contact us at [email].

### European Economic Area (GDPR)
[GDPR-specific rights if applicable]

### California (CCPA)
[CCPA-specific rights if applicable]

---

## 7. Children's Privacy

[Children's privacy statement]

---

## 8. Security

We implement [specific measures] to protect your information. However, no method of electronic transmission or storage is 100% secure.

---

## 9. International Data Transfers

Your information may be transferred to and processed in [countries/regions] where [service providers] operate.

---

## 10. Changes to This Policy

We will notify you of changes by [method]. The updated policy will be effective [when].

---

## 11. Contact Us

For questions about this Privacy Policy:
- **Email:** [Email]
- **Developer:** [Business Name]
- **Address:** [If applicable]

We will respond to your inquiry within [timeframe].
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Privacy policy generation focus
- **ST-02** (Structured Sequential Instructions) - Section-by-section policy structure
- **CM-01** (Explicit Context Framing) - App-specific data practices context
- **CM-02** (Constraint Specification) - Legal compliance requirements
- **RT-02** (Multi-Dimensional Analysis) - Multiple regulation dimensions (GDPR, CCPA, COPPA)
- **QA-01** (Chain-of-Verification) - Data collection accuracy verification

---

## Related Prompts

- `android_privacy_compliance.md` - Audit existing privacy compliance
- `play_store_policy_compliance_check.md` - Broader Play Store policy review
- `play_store_data_safety_generator.md` - Generate matching Data Safety section (planned)
- `gdpr_compliance_audit.md` - Deep GDPR audit (planned)

---

## Customization Guide

- **For apps with no user accounts:** Simplify Section 2 (no account data), but still include SDK data collection
- **For children's apps:** Expand Section 7 with full COPPA compliance, parental consent mechanism, and verifiable parental consent (VPC) requirements
- **For health/fitness apps:** Add HIPAA considerations (if applicable), health data specific disclosures, and user consent for health data processing
- **For EU-only apps:** Expand GDPR section with Data Protection Officer details, data processing agreements, and detailed legal basis for each processing activity
- **For ad-supported apps:** Expand Section 4 with detailed ad network disclosures, tracking consent mechanisms, and IDFA/GAID usage details
- **For apps with social features:** Add content moderation disclosures, community guidelines reference, and user-to-user data sharing practices
