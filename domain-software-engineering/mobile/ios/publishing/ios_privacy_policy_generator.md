---
title: "iOS Privacy Policy Generator"
category: mobile-development
description: "Generate a comprehensive privacy policy for App Store submission covering data collection inventory, third-party SDK data usage, GDPR/CCPA requirements, and Apple's privacy requirements."
techniques:
  - ST-01
  - ST-03
difficulty: beginner
tags:
  - ios
  - privacy
  - app-store
  - legal
  - mobile-development
updated: "2026-03-20"
---

# iOS Privacy Policy Generator

**Objective:** Generate a comprehensive, legally structured privacy policy for an iOS app that satisfies App Store Review Guidelines, covers all data collection and usage practices, documents third-party SDK data sharing, and addresses GDPR and CCPA regulatory requirements with clear user-facing language.

**When to Use:** Use this prompt before initial App Store submission, when adding new data collection features, when integrating new third-party SDKs, or during annual privacy policy reviews. Must be completed before configuring App Store Privacy Labels.

**Prompt Type:** Modular (150-300 lines)

---

## Context Gathering

Before generating the privacy policy, gather essential context:

1. **App Information:**
   - "What is the app name, company name, and company jurisdiction (country/state)?"
   - "What is the primary contact email for privacy inquiries?"
   - "Does the company have a Data Protection Officer (DPO)?"

2. **Data Collection:**
   - "What personal data does the app collect (name, email, phone, location, photos, health data)?"
   - "Is data collected directly from the user or automatically (device ID, IP, usage analytics)?"
   - "Is any data collected from children under 13 (COPPA implications)?"

3. **Third-Party SDKs:**
   - "Which analytics SDKs are integrated (Firebase Analytics, Mixpanel, Amplitude)?"
   - "Which advertising SDKs are integrated (AdMob, Meta Ads, AppLovin)?"
   - "Which crash reporting SDKs are integrated (Crashlytics, Sentry, Datadog)?"

4. **Data Usage:**
   - "How is collected data used (personalization, analytics, advertising, authentication)?"
   - "Is data shared with or sold to third parties?"
   - "How long is data retained before deletion?"

5. **User Rights:**
   - "Can users request data export (GDPR portability)?"
   - "Can users request data deletion?"
   - "Is there a self-service data management interface in the app?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before generating ANY privacy policy, you MUST:**

1. **Audit all data collection** - Review every network request, SDK, and local storage to identify all data collected.
2. **Review third-party SDK privacy manifests** - Check each SDK's `PrivacyInfo.xcprivacy` file for declared data usage.
3. **Confirm jurisdictional requirements** - Identify which regulations apply (GDPR for EU users, CCPA for California, etc.).
4. **Match App Store Privacy Labels** - Ensure the policy is consistent with what is declared in App Store Connect privacy nutrition labels.
5. **Legal review disclaimer** - Note that AI-generated policies should be reviewed by legal counsel.

### False-Positive Prevention

- Do NOT claim "we do not collect any data" if any SDK collects device identifiers or analytics
- Do NOT omit third-party SDK data practices; the developer is responsible for all code in the app
- Do NOT use vague language like "we may collect" -- be specific about what IS collected
- Do NOT forget to address Apple's required reasons API usage (iOS 17+ Privacy Manifests)
- Do NOT claim GDPR compliance without implementing actual data subject rights
- DO list every category of data collected, with purpose for each
- DO include specific third-party SDK names and links to their privacy policies
- DO provide clear instructions for data deletion requests
- DO include the effective date and update history
- DO add a disclaimer that this is a template requiring legal review

---

### Phase 1: Data Collection Inventory

#### 1.1 Data Inventory Template

Before generating the policy, complete this inventory:

```markdown
## Data Collection Inventory

### Data Collected Directly from Users
| Data Type | Collection Point | Purpose | Required? | Stored Where |
|-----------|-----------------|---------|-----------|-------------|
| Email address | Registration | Account authentication | Yes | Backend server |
| Full name | Profile setup | Personalization | No | Backend server |
| Profile photo | Profile setup | Display | No | Cloud storage |
| Payment info | Checkout | Process purchases | Yes | Stripe (3rd party) |
| Location | Map feature | Show nearby items | No | Device only |

### Data Collected Automatically
| Data Type | Source | Purpose | Stored Where |
|-----------|--------|---------|-------------|
| Device model | UIDevice | Analytics, crash reports | Analytics provider |
| OS version | UIDevice | Compatibility analytics | Analytics provider |
| IP address | Network requests | Security, geolocation | Backend logs (30 days) |
| App usage events | Analytics SDK | Product improvement | Analytics provider |
| Crash logs | Crash SDK | Bug fixing | Crash reporting provider |
| IDFA | ATTrackingManager | Advertising attribution | Ad network |

### Third-Party SDK Data Practices
| SDK | Data Collected | Purpose | Privacy Policy URL |
|-----|---------------|---------|-------------------|
| Firebase Analytics | Events, device info | Analytics | https://firebase.google.com/support/privacy |
| Crashlytics | Crash logs, device info | Stability | https://firebase.google.com/support/privacy |
| Stripe | Payment tokens | Payments | https://stripe.com/privacy |
| RevenueCat | Purchase history | Subscriptions | https://www.revenuecat.com/privacy |
```

---

### Phase 2: Privacy Policy Generation

**CHECKPOINT 1:** Confirm data inventory is complete before generating the policy.

```markdown
## Data Inventory Review

| Category | Count | All Documented? |
|----------|-------|----------------|
| User-provided data | — | Yes/No |
| Automatically collected data | — | Yes/No |
| Third-party SDKs | — | Yes/No |

**Proceed with policy generation?**
```

#### 2.1 Privacy Policy Template

```markdown
# Privacy Policy for [App Name]

**Effective Date:** [Date]
**Last Updated:** [Date]

[Company Name] ("we," "our," or "us") operates the [App Name] mobile application
(the "App"). This Privacy Policy describes how we collect, use, store, and share
your information when you use our App.

**IMPORTANT:** This privacy policy template was generated with AI assistance and
should be reviewed by qualified legal counsel before publication.

---

## 1. Information We Collect

### 1.1 Information You Provide
We collect information you voluntarily provide when using the App:

- **Account Information:** [email address, name, etc.] when you create an account
- **Profile Information:** [profile photo, bio, etc.] when you customize your profile
- **Payment Information:** [payment method details] processed securely by [Stripe/payment provider]
- **User Content:** [photos, messages, reviews, etc.] that you submit through the App
- **Communications:** When you contact our support team

### 1.2 Information Collected Automatically
When you use the App, we automatically collect:

- **Device Information:** Device model, operating system version, unique device identifiers
- **Usage Data:** Features used, screens viewed, actions taken, timestamps
- **Log Data:** IP address, access times, app crashes, and system activity
- **Location Data:** [Precise/approximate] location when you [grant permission for specific feature]

### 1.3 Information from Third-Party Services
We use the following third-party services that may collect information:

| Service | Purpose | Data Collected | Privacy Policy |
|---------|---------|---------------|----------------|
| [Firebase Analytics] | [Analytics] | [Usage events, device info] | [Link] |
| [Crashlytics] | [Crash reporting] | [Crash logs, device info] | [Link] |
| [Stripe] | [Payment processing] | [Payment tokens] | [Link] |

---

## 2. How We Use Your Information

We use collected information to:

- **Provide the Service:** Operate and maintain the App's core functionality
- **Improve the App:** Analyze usage patterns to improve features and fix bugs
- **Communicate:** Send you service-related notifications and respond to inquiries
- **Security:** Detect and prevent fraud, abuse, and security incidents
- **Legal Compliance:** Comply with applicable laws and regulations
- [**Advertising:** Display relevant advertisements (if applicable)]
- [**Personalization:** Customize your experience based on preferences]

---

## 3. How We Share Your Information

We do not sell your personal information. We may share information with:

- **Service Providers:** Third-party services listed in Section 1.3 that help us
  operate the App, subject to their privacy policies
- **Legal Requirements:** When required by law, subpoena, or court order
- **Business Transfers:** In connection with a merger, acquisition, or sale of assets
- **With Your Consent:** When you explicitly agree to share information

---

## 4. Data Retention

We retain your personal information for as long as your account is active or as
needed to provide services. Specific retention periods:

| Data Type | Retention Period | Basis |
|-----------|-----------------|-------|
| Account data | Until account deletion | Service provision |
| Usage analytics | [24 months] | Legitimate interest |
| Crash logs | [90 days] | Bug resolution |
| Server logs (IP) | [30 days] | Security |
| Payment records | [7 years] | Legal requirement |

---

## 5. Your Rights and Choices

### 5.1 All Users
- **Account Deletion:** You can delete your account [in Settings > Delete Account / by contacting us]
- **Notification Preferences:** Manage push notifications in iOS Settings
- **Location Permission:** Control location access in iOS Settings > Privacy > Location Services
- **Tracking Permission:** Control ad tracking via iOS Settings > Privacy > Tracking

### 5.2 European Economic Area (EEA) Residents - GDPR
If you are in the EEA, you have the right to:
- **Access** your personal data
- **Rectify** inaccurate personal data
- **Erase** your personal data ("right to be forgotten")
- **Restrict** processing of your personal data
- **Data Portability** - receive your data in a structured, machine-readable format
- **Object** to processing based on legitimate interests
- **Withdraw Consent** at any time

To exercise these rights, contact us at [privacy@company.com].
We will respond within 30 days.

### 5.3 California Residents - CCPA/CPRA
If you are a California resident, you have the right to:
- **Know** what personal information is collected, used, and shared
- **Delete** your personal information
- **Opt-Out** of the sale or sharing of personal information
- **Non-Discrimination** for exercising your privacy rights

We do not sell personal information as defined by the CCPA.
To exercise these rights, contact us at [privacy@company.com].

---

## 6. Data Security

We implement appropriate technical and organizational measures to protect your
information, including:
- Encryption in transit (TLS 1.2+) and at rest
- Access controls and authentication for internal systems
- Regular security assessments and monitoring
- Secure coding practices following OWASP guidelines

No method of transmission over the internet is 100% secure. We cannot guarantee
absolute security of your data.

---

## 7. Children's Privacy

[Our App is not intended for children under 13 / Our App includes features
for children and complies with COPPA]. We do not knowingly collect personal
information from children under 13. If you believe we have collected information
from a child under 13, please contact us at [privacy@company.com].

---

## 8. International Data Transfers

Your information may be transferred to and processed in countries other than your
own. We ensure appropriate safeguards are in place, including [Standard
Contractual Clauses / Privacy Shield certification / adequacy decisions].

---

## 9. Changes to This Policy

We may update this Privacy Policy from time to time. We will notify you of
material changes by [updating the "Last Updated" date / sending a notification
through the App / email notification].

---

## 10. Contact Us

If you have questions about this Privacy Policy or your personal data:

- **Email:** [privacy@company.com]
- **Address:** [Company Address]
- **Data Protection Officer:** [DPO Name, dpo@company.com] (if applicable)

For EEA residents: You have the right to lodge a complaint with your local
supervisory authority.
```

---

### Phase 3: App Store Privacy Labels Alignment

**CHECKPOINT 2:** Review generated policy before aligning with App Store privacy labels.

```markdown
## Policy Review

| Section | Complete? | Matches Data Inventory? |
|---------|-----------|----------------------|
| Information collected | — | — |
| Third-party SDKs listed | — | — |
| User rights (GDPR/CCPA) | — | — |
| Data retention periods | — | — |
| Contact information | — | — |

**Proceed with App Store Privacy Label alignment?**
```

#### 3.1 Privacy Label Mapping

```markdown
## App Store Privacy Label Alignment

Map each data type from your policy to App Store Connect categories:

### Data Used to Track You
(Data linked to your identity used for advertising across other companies' apps/websites)
- [ ] IDFA / Advertising identifier
- [ ] Third-party advertising SDKs

### Data Linked to You
(Data connected to your identity)
- [ ] Contact Info (name, email, phone)
- [ ] User Content (photos, posts)
- [ ] Identifiers (user ID)
- [ ] Usage Data (product interaction)
- [ ] Purchases (purchase history)

### Data Not Linked to You
(Data not connected to your identity)
- [ ] Diagnostics (crash data, performance data)
- [ ] Usage Data (aggregated analytics)

### Purpose for Each Data Type
For each data type, select applicable purposes:
- [ ] App Functionality
- [ ] Analytics
- [ ] Product Personalization
- [ ] Advertising / Marketing
- [ ] Third-Party Advertising
- [ ] Developer's Advertising
- [ ] Other Purposes
```

---

## Expected Output

### Deliverables

```
privacy/
├── PRIVACY_POLICY.md              # Complete privacy policy document
├── DATA_INVENTORY.md              # Data collection inventory spreadsheet
├── PRIVACY_LABEL_MAPPING.md       # App Store Connect privacy label mapping
└── THIRD_PARTY_SDK_AUDIT.md       # SDK data usage documentation
```

### Implementation Checklist

- [ ] Data collection inventory completed for all user-provided data
- [ ] Automatic data collection documented (device info, analytics, logs)
- [ ] All third-party SDKs documented with their privacy policies
- [ ] Privacy policy generated with all required sections
- [ ] GDPR user rights section included (if serving EU users)
- [ ] CCPA rights section included (if serving California users)
- [ ] Data retention periods specified for each data type
- [ ] Contact information and DPO details included
- [ ] Privacy policy URL hosted and accessible
- [ ] App Store Privacy Labels match the policy content
- [ ] Legal counsel review disclaimer included
- [ ] Policy effective date set

---

## Techniques Used

- **ST-01** (Clear Objective): Focused on generating a complete, App Store-compliant privacy policy
- **ST-03** (Output Format Templates): Structured policy template with fill-in sections

---

## Related Prompts

- [ios_gdpr_compliance_audit.md](../publishing/ios_gdpr_compliance_audit.md) - Comprehensive GDPR compliance audit
- [ios_privacy_compliance.md](../publishing/ios_privacy_compliance.md) - Apple privacy framework compliance
- [ios_privacy_labels_generator.md](../publishing/ios_privacy_labels_generator.md) - App Store privacy nutrition labels
- [ios_terms_of_service_generator.md](../publishing/ios_terms_of_service_generator.md) - Terms of service generation
- [ios_pre_submission_checklist.md](../publishing/ios_pre_submission_checklist.md) - Pre-submission requirements
