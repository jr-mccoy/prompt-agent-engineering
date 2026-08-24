---
title: "GDPR Compliance Audit"
category: mobile-development
description: "Audit an Android app for GDPR compliance including data processing inventory, lawful basis assessment, consent implementation, data deletion and portability capabilities, and DPA requirements for third-party services"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - CM-01
difficulty: advanced
tags:
  - android
  - gdpr
  - privacy
  - compliance
  - legal
  - mobile-development
  - solo-developer
updated: "2026-02-12"
---

# GDPR Compliance Audit

**Objective:** Conduct a comprehensive GDPR compliance audit of an Android application — inventorying all personal data processing activities, assessing the lawful basis for each, evaluating consent collection implementation, verifying data subject rights capabilities (deletion, portability, access, rectification), reviewing third-party SDK data practices, and assessing Data Processing Agreement (DPA) requirements — producing a compliance report with gaps and remediation steps.

**When to Use:** Use this prompt when your Android app has EU/EEA users, when preparing for a product launch in European markets, when you receive a data subject access request (DSAR) and need to understand your obligations, when integrating a new third-party SDK that processes personal data, or when Google Play requests a data safety section review.

**Important context:** GDPR applies to any app that processes personal data of individuals in the EU/EEA — regardless of where your business is located. Non-compliance fines can reach 4% of annual global revenue or EUR 20 million (whichever is higher). For solo developers, the realistic risk is not mega-fines but rather Google Play policy enforcement, user complaints to Data Protection Authorities, and reputational damage. **This audit is a technical assessment — for legal obligations specific to your situation, consult a qualified data protection lawyer.**

---

## Context Gathering

1. **App and Users:**
   - "Do you have users in the EU/EEA? What percentage of your user base?"
   - "Do you have a Data Protection Officer (DPO)? (Generally required if core activity involves large-scale processing)"
   - "Where is your business established? (Determines lead supervisory authority)"

2. **Data Collection:**
   - "What user data does your app collect directly (registration info, user input, files)?"
   - "What data do your third-party SDKs collect (Firebase Analytics, Crashlytics, AdMob, Facebook SDK)?"
   - "Do you collect device identifiers (Advertising ID, Android ID, IMEI)?"
   - "Do you collect location data? How precise?"
   - "Do you process special category data (health, biometric, religious, political)?"

3. **Current Compliance:**
   - "Do you have a privacy policy? Does it mention GDPR?"
   - "Do you have a consent management system (cookie banner, consent dialog)?"
   - "Can users currently delete their account and data?"
   - "Can users export their data?"

---

## Instructions

### Phase 1: Data Processing Inventory

Create a complete inventory of all personal data processing:

**For each data item, document:**

| Data Item | Source | Lawful Basis | Purpose | Retention | Third-Party Sharing | Storage Location |
|-----------|--------|-------------|---------|-----------|-------------------|-----------------|
| Email address | User registration | Contract | Account identification | Until account deletion | Firebase Auth | Firebase Auth (US) |
| Display name | User profile | Contract | Social features | Until account deletion | Firestore | Firestore (US/EU) |
| Device model | Firebase Analytics | Legitimate interest | Crash debugging | 14 months | Google Analytics | Google Cloud (US) |
| Advertising ID | AdMob SDK | Consent | Personalized ads | Session-based | AdMob, ad networks | Google Ad servers |
| Crash stack trace | Crashlytics | Legitimate interest | App stability | 90 days | Crashlytics | Google Cloud (US) |
| IP address | All network requests | Legitimate interest | Security, abuse prevention | Server logs: 30 days | Firebase, CDN | Various |
| Location (coarse) | App functionality | Consent | Location-based features | Until disabled | None | Device + Firestore |
| FCM token | Firebase Messaging | Contract | Push notifications | Until token refresh | FCM | Google Cloud |

**Common hidden data collection (often missed):**
- Firebase Analytics collects device model, OS version, app version, country, language by default
- Crashlytics collects device state, stack traces, and custom keys
- AdMob collects Advertising ID, device info, IP address, and ad interaction data
- Firebase Performance Monitoring collects network request traces
- Third-party analytics SDKs may collect more than documented

### Phase 2: Lawful Basis Assessment

For each processing activity, verify the lawful basis is correct:

| Basis | When Valid | Example | Requirements |
|-------|-----------|---------|-------------|
| **Consent (Art. 6(1)(a))** | User freely gives specific, informed consent | Ad personalization, marketing emails, location tracking | Must be withdrawable, freely given, specific, informed. Pre-ticked boxes invalid. |
| **Contract (Art. 6(1)(b))** | Processing necessary to fulfill a contract with the user | Account creation, service delivery, subscription management | Cannot be used for purposes beyond what's necessary for the service |
| **Legitimate Interest (Art. 6(1)(f))** | Processing necessary for developer's legitimate interest, balanced against user's rights | Crash reporting, security monitoring, analytics (aggregated) | Requires a Legitimate Interest Assessment (LIA). User's rights must not override. |
| **Legal Obligation (Art. 6(1)(c))** | Required by law | Tax records for in-app purchases, fraud detection | Must identify the specific legal requirement |

**Red flags:**
- Using "consent" for processing that is actually necessary for the contract (if consent is withdrawn, does the service break?)
- Using "legitimate interest" for advertising (generally requires consent)
- No documented lawful basis for a processing activity
- Consent obtained through dark patterns (pre-selected, bundled, or coerced)

### Phase 3: Consent Implementation Audit

If consent is used as a lawful basis:

**Consent collection checklist:**
- [ ] Consent is collected BEFORE processing begins (not after the fact)
- [ ] Consent is specific to each purpose (not bundled "I agree to everything")
- [ ] Consent is freely given (service works without optional consents)
- [ ] Consent can be withdrawn as easily as it was given
- [ ] Consent records are stored (who consented, when, to what, what version of privacy policy)
- [ ] Consent is re-obtained if the purpose or processing changes
- [ ] Children's consent requires parental verification (under 16 in most EU countries)

**For Android apps with ads:**
- [ ] UMP (User Messaging Platform) SDK or equivalent consent management platform is implemented
- [ ] TCF v2.2 compliance for IAB framework (if using programmatic ads)
- [ ] Non-personalized ads served when consent is denied (not no ads unless consent is required for all ads)
- [ ] Consent state is checked before loading ad SDKs

### Phase 4: Data Subject Rights

Verify the app supports all required GDPR rights:

| Right | Article | Implementation | Test |
|-------|---------|---------------|------|
| **Access (Art. 15)** | User can request a copy of all their data | Export all user data from Firestore, Storage, Analytics | Request export, verify completeness |
| **Rectification (Art. 16)** | User can correct inaccurate data | Profile editing, contact support for data corrections | Edit profile, verify changes propagate |
| **Erasure (Art. 17)** | "Right to be forgotten" — user can request deletion | Delete account + all associated data across all services | Delete account, verify data is removed from Firestore, Storage, Auth, Analytics |
| **Portability (Art. 20)** | User can receive data in machine-readable format | JSON/CSV export of user data | Export data, verify format is usable |
| **Restriction (Art. 18)** | User can request processing be restricted | Account suspension feature or processing flag | Restrict, verify data is not processed |
| **Objection (Art. 21)** | User can object to processing based on legitimate interest | Opt-out of analytics, disable specific features | Object, verify processing stops |

**Deletion implementation verification:**
- [ ] User-initiated account deletion is available in-app (Google Play requires this)
- [ ] Deletion removes data from: Firestore, Firebase Auth, Cloud Storage, Analytics (request deletion)
- [ ] Deletion propagates to third-party services (AdMob, analytics partners)
- [ ] Deletion completes within a reasonable timeframe (30 days maximum)
- [ ] Backup systems eventually purge deleted data (don't retain in backups indefinitely)
- [ ] Deletion is confirmed to the user

### Phase 5: Third-Party SDK Assessment

For each third-party SDK:

| SDK | Data Collected | DPA Required | DPA Status | GDPR Compliant | Data Transfer Mechanism |
|-----|---------------|-------------|------------|-----------------|------------------------|
| Firebase Analytics | Events, user properties, device info | Yes | Google DPA covers all Firebase | Yes (Google DPA) | Standard Contractual Clauses |
| Firebase Crashlytics | Crash data, device state | Yes | Covered by Google DPA | Yes | SCCs |
| AdMob | Ad ID, device info, interaction data | Yes | Covered by Google DPA | Requires consent (ads) | SCCs |
| Facebook SDK | User actions, device info | Yes | Meta DPA required | Requires configuration | SCCs |
| Stripe | Payment data | Yes | Stripe DPA available | Yes | SCCs |

**For each SDK, verify:**
- [ ] DPA is signed or available (Google's DPA covers all Firebase services)
- [ ] International data transfer mechanism exists (SCCs for US transfers post-Schrems II)
- [ ] SDK's data collection is documented in your privacy policy
- [ ] SDK's data collection is declared in Play Store Data Safety section
- [ ] SDK configuration respects user consent (disable before consent is given)

### Phase 6: Privacy Policy Audit

Verify your privacy policy covers GDPR requirements:

- [ ] Identity and contact details of the data controller
- [ ] Contact details of DPO (if applicable)
- [ ] Purposes of processing and lawful basis for each
- [ ] Categories of personal data collected
- [ ] Recipients or categories of recipients
- [ ] International data transfers and safeguards
- [ ] Retention periods for each data category
- [ ] Data subject rights and how to exercise them
- [ ] Right to lodge a complaint with a supervisory authority
- [ ] Whether data provision is a statutory/contractual requirement
- [ ] Automated decision-making and profiling (if applicable)
- [ ] Written in clear, plain language

---

## Expected Output

1. **Data Processing Inventory** — complete table of all personal data processing activities
2. **Lawful Basis Assessment** — verified basis for each processing activity with red flags
3. **Consent Audit Results** — consent implementation compliance status
4. **Data Subject Rights Assessment** — implementation status for each right with gaps
5. **Third-Party SDK Assessment** — DPA and compliance status for each SDK
6. **Privacy Policy Gap Analysis** — missing elements in the current privacy policy
7. **Remediation Plan** — prioritized list of compliance gaps with fixes
8. **Risk Rating** — overall GDPR compliance risk level (LOW/MEDIUM/HIGH/CRITICAL)

---

## CRITICAL: Verification Requirements

- [ ] Every data processing activity has a documented lawful basis
- [ ] Users can delete their account and data from within the app
- [ ] Consent for ads/analytics is collected before SDK initialization
- [ ] Privacy policy is accessible from within the app and from the Play Store listing
- [ ] Third-party data transfers outside EU have a legal mechanism (SCCs)
- [ ] **Disclaimer included:** This is a technical audit — consult a qualified data protection lawyer for legal compliance
