---
title: "iOS GDPR Compliance Audit"
category: mobile-development
description: "Comprehensive GDPR compliance audit for iOS apps covering data processing inventory, consent management, data subject rights implementation, data breach procedures, DPA requirements, and SDK data sharing audit."
techniques:
  - ST-01
  - ST-02
  - RT-02
difficulty: advanced
tags:
  - ios
  - privacy
  - gdpr
  - compliance
  - data-protection
  - mobile-development
updated: "2026-03-20"
---

# iOS GDPR Compliance Audit

**Objective:** Conduct a comprehensive GDPR (General Data Protection Regulation) compliance audit for an iOS application covering data processing inventory, lawful basis for processing, consent management implementation, data subject rights (access, rectification, erasure, portability, restriction, objection), data breach notification procedures, Data Processing Agreement requirements for third-party SDKs, and a technical audit of all data flows.

**When to Use:** Use this prompt before launching an iOS app in the EU/EEA, during annual compliance reviews, when integrating new third-party SDKs, when responding to a data protection authority inquiry, or after a data breach. Should be performed by apps processing personal data of EU/EEA residents regardless of where the developer is based.

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

Before conducting the audit, gather essential context:

1. **Business Context:**
   - "Is the company established in the EU, or does it process data of EU residents?"
   - "Has a Data Protection Officer (DPO) been appointed? Is one required?"
   - "Has a Data Protection Impact Assessment (DPIA) been conducted?"

2. **Data Processing:**
   - "What categories of personal data are processed (identifiers, location, health, biometric)?"
   - "What is the lawful basis for each processing activity (consent, contract, legitimate interest)?"
   - "Are special categories of data processed (health, biometric, racial/ethnic origin)?"

3. **Technical Infrastructure:**
   - "Where is data stored (AWS region, Google Cloud, on-device)?"
   - "Is data transferred outside the EU/EEA? If so, what safeguards are in place?"
   - "What encryption is used for data at rest and in transit?"

4. **Third-Party SDKs:**
   - "Which SDKs process personal data (analytics, advertising, crash reporting, payment)?"
   - "Are Data Processing Agreements (DPAs) in place with all processors?"
   - "Have SDK privacy manifests been reviewed (iOS 17+ PrivacyInfo.xcprivacy)?"

5. **Current State:**
   - "Has the app been audited for GDPR compliance before?"
   - "Have any data subject requests been received? How were they handled?"
   - "Is there a consent management platform in use?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before conducting ANY compliance assessment, you MUST:**

1. **Map all data flows** - Trace every piece of personal data from collection through storage, processing, sharing, and deletion.
2. **Identify all processors** - Every third-party SDK or service that processes personal data on your behalf must be documented.
3. **Verify lawful basis** - Each processing activity must have a documented lawful basis under GDPR Article 6.
4. **Check data transfer mechanisms** - Any transfer outside the EU/EEA requires documented safeguards (SCCs, adequacy decision).
5. **Review technical measures** - Encryption, access controls, and data minimization must be verified, not assumed.

### False-Positive Prevention

- Do NOT mark consent as "obtained" if it is bundled with Terms acceptance; GDPR requires separate, granular consent
- Do NOT assume legitimate interest applies without documenting the balancing test
- Do NOT claim compliance with data deletion rights if soft-delete is used without eventual hard deletion
- Do NOT ignore third-party SDK data processing; the app developer is the data controller
- Do NOT assume on-device-only data is exempt; GDPR applies to automated processing of personal data
- DO document every lawful basis with specific justification
- DO implement granular consent for each processing purpose
- DO provide actual data export functionality (not just a description in the privacy policy)
- DO maintain records of processing activities (ROPA) as required by Article 30
- DO test data deletion to ensure it removes data from backups within a reasonable timeframe

---

### Phase 1: Data Processing Inventory

#### 1.1 Record of Processing Activities (ROPA)

```markdown
## Record of Processing Activities (Article 30)

### Controller Information
| Field | Value |
|-------|-------|
| Controller Name | [Company Legal Name] |
| Controller Address | [Registered Address] |
| Controller Contact | [privacy@company.com] |
| DPO Name & Contact | [Name, dpo@company.com] or "Not appointed - justify below" |
| EU Representative | [Name, Address] (required if not established in EU) |

### Processing Activity Register

#### Activity 1: User Account Management
| Field | Detail |
|-------|--------|
| **Purpose** | Create and manage user accounts |
| **Lawful Basis** | Article 6(1)(b) - Performance of contract |
| **Categories of Data Subjects** | App users |
| **Categories of Personal Data** | Email, name, profile photo |
| **Categories of Recipients** | Backend hosting provider ([AWS/GCP]) |
| **International Transfers** | [Yes/No - if yes, specify destination and safeguard] |
| **Retention Period** | Until account deletion + 30 days backup retention |
| **Technical Measures** | TLS 1.2+, AES-256 at rest, access control |

#### Activity 2: Analytics
| Field | Detail |
|-------|--------|
| **Purpose** | Understand app usage to improve features |
| **Lawful Basis** | Article 6(1)(a) - Consent OR Article 6(1)(f) - Legitimate interest |
| **Categories of Data Subjects** | App users |
| **Categories of Personal Data** | Device ID, usage events, app version, OS version |
| **Categories of Recipients** | [Analytics provider name] |
| **International Transfers** | [Yes - US, Standard Contractual Clauses] |
| **Retention Period** | [24 months from collection] |
| **Technical Measures** | Anonymized device IDs, aggregation after 90 days |

#### Activity 3: Crash Reporting
| Field | Detail |
|-------|--------|
| **Purpose** | Identify and fix app crashes |
| **Lawful Basis** | Article 6(1)(f) - Legitimate interest |
| **Balancing Test** | User expectation of stable app outweighs minimal data impact |
| **Categories of Personal Data** | Device model, OS version, crash stack trace |
| **Categories of Recipients** | [Crashlytics/Sentry] |
| **Retention Period** | [90 days] |

[Continue for ALL processing activities]
```

#### 1.2 Lawful Basis Assessment

```markdown
## Lawful Basis Decision Tree

For each processing activity, select ONE lawful basis:

### Article 6(1)(a) - Consent
Use when:
- Processing is for marketing/advertising
- Tracking across apps (ATT consent required AND GDPR consent)
- Special category data (health, biometric) - also need Article 9 basis
- Non-essential analytics

Requirements:
- [ ] Consent is freely given (not bundled with service access)
- [ ] Consent is specific (separate consent per purpose)
- [ ] Consent is informed (clear description before consent)
- [ ] Consent is unambiguous (affirmative action, no pre-ticked boxes)
- [ ] Consent is withdrawable (easy as giving it)
- [ ] Consent records are maintained

### Article 6(1)(b) - Performance of Contract
Use when:
- Processing is necessary to provide the service the user signed up for
- Account creation, authentication, core feature delivery

Requirements:
- [ ] Processing is objectively necessary (not just useful)
- [ ] Service cannot be provided without this processing
- [ ] Terms of service describe the service requiring this data

### Article 6(1)(f) - Legitimate Interest
Use when:
- Security monitoring, fraud prevention
- Essential crash reporting
- Basic analytics for service improvement (with proper balancing test)

Requirements:
- [ ] Legitimate interest identified and documented
- [ ] Processing is necessary for the interest (no less invasive alternative)
- [ ] Balancing test documented (interest vs data subject rights)
- [ ] Data subjects can reasonably expect this processing
```

---

### Phase 2: Consent Management Implementation

**CHECKPOINT 1:** Complete data inventory before implementing consent.

```markdown
## Data Inventory Summary

| Processing Activity | Lawful Basis | Consent Required? |
|--------------------|--------------|--------------------|
| [Activity 1] | [Basis] | [Yes/No] |
| [Activity 2] | [Basis] | [Yes/No] |

**Total activities requiring consent: [N]. Proceed with consent implementation?**
```

#### 2.1 Consent Management Architecture

```swift
// File: Services/Privacy/ConsentManager.swift

import Foundation

@Observable
final class ConsentManager {
    enum ConsentPurpose: String, CaseIterable, Codable {
        case analytics = "analytics"
        case crashReporting = "crash_reporting"
        case advertising = "advertising"
        case personalization = "personalization"
    }

    struct ConsentRecord: Codable {
        let purpose: ConsentPurpose
        let granted: Bool
        let timestamp: Date
        let version: String  // Privacy policy version at time of consent
    }

    private(set) var consents: [ConsentPurpose: ConsentRecord] = [:]
    private let storage: UserDefaults
    private let serverSync: ConsentSyncProtocol

    init(storage: UserDefaults = .standard, serverSync: ConsentSyncProtocol) {
        self.storage = storage
        self.serverSync = serverSync
        loadConsents()
    }

    /// Check if a specific purpose has active consent
    func hasConsent(for purpose: ConsentPurpose) -> Bool {
        consents[purpose]?.granted ?? false
    }

    /// Record consent decision (must be called AFTER showing consent UI)
    func updateConsent(for purpose: ConsentPurpose, granted: Bool, policyVersion: String) async {
        let record = ConsentRecord(
            purpose: purpose,
            granted: granted,
            timestamp: .now,
            version: policyVersion
        )
        consents[purpose] = record
        saveConsents()

        // Sync to server for auditability
        try? await serverSync.syncConsent(record)

        // Enable/disable SDKs based on consent
        applyConsent(purpose: purpose, granted: granted)
    }

    /// Withdraw all consents (GDPR right to withdraw)
    func withdrawAllConsents() async {
        for purpose in ConsentPurpose.allCases {
            await updateConsent(for: purpose, granted: false, policyVersion: currentPolicyVersion)
        }
    }

    private func applyConsent(purpose: ConsentPurpose, granted: Bool) {
        switch purpose {
        case .analytics:
            AnalyticsService.shared.setEnabled(granted)
        case .crashReporting:
            CrashReporter.shared.setEnabled(granted)
        case .advertising:
            AdService.shared.setEnabled(granted)
        case .personalization:
            PersonalizationEngine.shared.setEnabled(granted)
        }
    }

    private var currentPolicyVersion: String { "2026-03-20-v1" }

    private func loadConsents() {
        guard let data = storage.data(forKey: "gdpr_consents"),
              let decoded = try? JSONDecoder().decode([ConsentPurpose: ConsentRecord].self, from: data)
        else { return }
        consents = decoded
    }

    private func saveConsents() {
        let data = try? JSONEncoder().encode(consents)
        storage.set(data, forKey: "gdpr_consents")
    }
}
```

#### 2.2 Consent UI Requirements

```swift
// File: Features/Privacy/ConsentView.swift

import SwiftUI

struct ConsentView: View {
    @Environment(ConsentManager.self) private var consentManager
    @State private var analyticsConsent = false
    @State private var crashConsent = false
    @State private var adConsent = false
    let policyVersion: String
    let onComplete: () -> Void

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 24) {
                    Text("Your Privacy Choices")
                        .font(.title)
                        .fontWeight(.bold)

                    Text("We respect your privacy. Please choose which data processing activities you consent to. You can change these choices at any time in Settings.")
                        .font(.body)
                        .foregroundStyle(.secondary)

                    // GDPR requires separate, granular consent per purpose
                    consentToggle(
                        title: "Analytics",
                        description: "Help us improve the app by sharing anonymous usage data. We use [Provider] to analyze feature usage and app performance.",
                        isOn: $analyticsConsent
                    )

                    consentToggle(
                        title: "Crash Reporting",
                        description: "Share crash reports to help us fix bugs. Reports include device model, OS version, and crash stack traces.",
                        isOn: $crashConsent
                    )

                    consentToggle(
                        title: "Personalized Advertising",
                        description: "Allow us to show relevant ads based on your interests. Your data is shared with [Ad Network] for this purpose.",
                        isOn: $adConsent
                    )

                    // Links must be accessible BEFORE consent
                    Link("Read our Privacy Policy", destination: URL(string: "https://yourapp.com/privacy")!)
                        .font(.footnote)

                    Button("Save Preferences") {
                        Task {
                            await saveConsents()
                            onComplete()
                        }
                    }
                    .buttonStyle(.borderedProminent)
                    .frame(maxWidth: .infinity)

                    Button("Reject All") {
                        analyticsConsent = false
                        crashConsent = false
                        adConsent = false
                        Task {
                            await saveConsents()
                            onComplete()
                        }
                    }
                    .frame(maxWidth: .infinity)
                    .font(.footnote)
                }
                .padding()
            }
        }
    }

    private func consentToggle(title: String, description: String, isOn: Binding<Bool>) -> some View {
        VStack(alignment: .leading, spacing: 8) {
            Toggle(title, isOn: isOn)
                .font(.headline)
            Text(description)
                .font(.caption)
                .foregroundStyle(.secondary)
        }
        .padding()
        .background(Color(.systemGray6))
        .clipShape(RoundedRectangle(cornerRadius: 12))
    }

    private func saveConsents() async {
        await consentManager.updateConsent(for: .analytics, granted: analyticsConsent, policyVersion: policyVersion)
        await consentManager.updateConsent(for: .crashReporting, granted: crashConsent, policyVersion: policyVersion)
        await consentManager.updateConsent(for: .advertising, granted: adConsent, policyVersion: policyVersion)
    }
}
```

---

### Phase 3: Data Subject Rights Implementation

#### 3.1 Rights Implementation Matrix

```markdown
## Data Subject Rights (Articles 15-22)

| Right | Article | Implementation | Response Time |
|-------|---------|---------------|---------------|
| Access | Art. 15 | Export user's data as JSON/CSV | 30 days |
| Rectification | Art. 16 | In-app profile editing | Without undue delay |
| Erasure | Art. 17 | Account deletion + data purge | 30 days |
| Restriction | Art. 18 | Suspend processing, retain data | Without undue delay |
| Portability | Art. 20 | Machine-readable export (JSON) | 30 days |
| Objection | Art. 21 | Opt-out of legitimate interest processing | Without undue delay |
| Automated decisions | Art. 22 | Human review option for automated decisions | Without undue delay |
```

#### 3.2 Data Export (Right of Access & Portability)

```swift
// File: Services/Privacy/DataExportService.swift

import Foundation

struct DataExportService {
    struct UserDataExport: Codable {
        let exportDate: Date
        let userData: UserData
        let activityData: [ActivityRecord]
        let consentHistory: [ConsentManager.ConsentRecord]

        struct UserData: Codable {
            let id: String
            let email: String
            let name: String
            let createdAt: Date
            let profilePhotoURL: String?
        }

        struct ActivityRecord: Codable {
            let type: String
            let timestamp: Date
            let metadata: [String: String]
        }
    }

    static func exportUserData(userId: String) async throws -> Data {
        // Gather ALL personal data from ALL storage locations
        let userData = try await APIClient.shared.get("/users/\(userId)/data-export")

        // Include on-device data
        let consentHistory = ConsentManager.shared.allConsentRecords()

        let export = UserDataExport(
            exportDate: .now,
            userData: userData,
            activityData: try await fetchActivityData(userId: userId),
            consentHistory: consentHistory
        )

        // Return as JSON (machine-readable format for portability)
        let encoder = JSONEncoder()
        encoder.dateEncodingStrategy = .iso8601
        encoder.outputFormatting = [.prettyPrinted, .sortedKeys]
        return try encoder.encode(export)
    }

    private static func fetchActivityData(userId: String) async throws -> [UserDataExport.ActivityRecord] {
        try await APIClient.shared.get("/users/\(userId)/activity")
    }
}
```

#### 3.3 Account Deletion (Right to Erasure)

```swift
// File: Services/Privacy/AccountDeletionService.swift

import Foundation

final class AccountDeletionService {
    enum DeletionStatus: String, Codable {
        case requested
        case processing
        case completed
        case failed
    }

    /// Initiate account deletion with grace period
    func requestDeletion(userId: String) async throws -> DeletionConfirmation {
        // Step 1: Mark account for deletion (grace period for user to change mind)
        let confirmation = try await APIClient.shared.post(
            "/users/\(userId)/deletion-request",
            body: DeletionRequest(
                userId: userId,
                requestedAt: .now,
                scheduledDeletionDate: Calendar.current.date(byAdding: .day, value: 30, to: .now)!
            )
        )

        // Step 2: Revoke all active sessions
        try await APIClient.shared.post("/users/\(userId)/revoke-sessions", body: EmptyBody())

        // Step 3: Withdraw all consents immediately
        await ConsentManager.shared.withdrawAllConsents()

        // Step 4: Clear on-device data
        clearLocalData(userId: userId)

        // Step 5: Notify third-party processors to delete data
        try await notifyProcessors(userId: userId)

        return confirmation
    }

    private func clearLocalData(userId: String) {
        // Clear UserDefaults
        let domain = Bundle.main.bundleIdentifier!
        UserDefaults.standard.removePersistentDomain(forName: domain)

        // Clear Keychain items
        KeychainHelper.deleteAll()

        // Clear Core Data / SwiftData
        PersistenceController.shared.deleteUserData(userId: userId)

        // Clear cached files
        let cacheDir = FileManager.default.urls(for: .cachesDirectory, in: .userDomainMask).first!
        try? FileManager.default.removeItem(at: cacheDir)

        // Clear cookies
        HTTPCookieStorage.shared.removeCookies(since: .distantPast)
    }

    private func notifyProcessors(userId: String) async throws {
        // Notify each data processor to delete user data
        // This should be automated where APIs exist
        async let analyticsDelete = AnalyticsService.shared.deleteUserData(userId: userId)
        async let crashDelete = CrashReporter.shared.deleteUserData(userId: userId)

        _ = try await (analyticsDelete, crashDelete)
    }
}
```

---

### Phase 4: Data Breach & SDK Audit

**CHECKPOINT 2:** Review data subject rights implementation before breach procedures.

```markdown
## Rights Implementation Summary

| Right | In-App UI | Backend API | Tested? |
|-------|-----------|-------------|---------|
| Access / Export | Settings > Export Data | GET /data-export | — |
| Rectification | Profile edit screen | PUT /users/:id | — |
| Erasure | Settings > Delete Account | POST /deletion-request | — |
| Consent withdrawal | Settings > Privacy | POST /consent | — |
| Portability | JSON export | GET /data-export | — |

**Proceed with breach procedures and SDK audit?**
```

#### 4.1 Data Breach Response Plan

```markdown
## Data Breach Notification Procedure (Article 33 & 34)

### Timeline
| Action | Deadline | Responsible |
|--------|----------|-------------|
| Internal detection & assessment | Immediately | Engineering/Security |
| Notify supervisory authority | 72 hours from awareness | DPO / Legal |
| Notify affected users (if high risk) | Without undue delay | DPO / Legal |
| Document the breach | Ongoing | DPO |

### Breach Assessment Template
1. **Nature of breach:** [confidentiality / integrity / availability]
2. **Categories of data affected:** [names, emails, financial, health]
3. **Approximate number of data subjects affected:** [N]
4. **Likely consequences:** [identity theft, financial loss, discrimination]
5. **Risk level:** [Low / Medium / High]
6. **Measures taken to address:** [containment, mitigation, prevention]

### Notification to Supervisory Authority (Article 33)
Required if breach is likely to result in risk to rights and freedoms.
Include: nature, categories, approximate numbers, DPO contact, consequences, measures taken.

### Notification to Data Subjects (Article 34)
Required if breach is likely to result in HIGH risk to rights and freedoms.
Must be in clear, plain language. Include: nature, DPO contact, consequences, measures taken.
```

#### 4.2 Third-Party SDK GDPR Audit

```markdown
## SDK Data Processing Audit

For EACH third-party SDK, complete this assessment:

### SDK: [Name, e.g., Firebase Analytics]
| Field | Detail |
|-------|--------|
| **Processor or Controller** | [Processor / Joint Controller / Independent Controller] |
| **DPA in place** | [Yes, link / No - REQUIRED before use] |
| **SCCs for international transfer** | [Yes / No / N/A (EU data center)] |
| **Data collected** | [List specific data points] |
| **Privacy Manifest (PrivacyInfo.xcprivacy)** | [Present / Missing - required iOS 17+] |
| **Required Reasons APIs used** | [List any, e.g., UserDefaults, disk space] |
| **Data minimization** | [Is SDK configured to collect minimum needed?] |
| **Consent gating** | [Is SDK initialized only after consent?] |
| **User deletion API** | [Does SDK provide user data deletion?] |
| **Sub-processors** | [List known sub-processors] |
```

```swift
// Consent-gated SDK initialization pattern
// File: App/SDKInitializer.swift

final class SDKInitializer {
    static func initializeSDKs(consents: [ConsentManager.ConsentPurpose: Bool]) {
        // ONLY initialize SDKs the user has consented to

        if consents[.analytics] == true {
            // Initialize analytics ONLY with consent
            AnalyticsSDK.configure(options: .init(
                anonymizeIP: true,  // Data minimization
                sessionTimeout: 1800
            ))
        }

        if consents[.crashReporting] == true {
            CrashReportingSDK.configure()
        }

        if consents[.advertising] == true {
            AdSDK.configure(options: .init(
                requestNonPersonalizedAdsOnly: false
            ))
        } else {
            // Show only non-personalized ads or no ads
            AdSDK.configure(options: .init(
                requestNonPersonalizedAdsOnly: true
            ))
        }
    }
}
```

---

## Expected Output

### GDPR Compliance Report

```markdown
## GDPR Compliance Audit Report

### App: [App Name]
### Audit Date: [Date]
### Auditor: [Name/AI-Assisted]

### Executive Summary
| Area | Status | Critical Issues |
|------|--------|----------------|
| Data Processing Inventory | [Complete/Incomplete] | [N issues] |
| Lawful Basis Documentation | [Complete/Incomplete] | [N issues] |
| Consent Management | [Implemented/Partial/Missing] | [N issues] |
| Data Subject Rights | [Implemented/Partial/Missing] | [N issues] |
| Data Breach Procedures | [Documented/Missing] | [N issues] |
| Third-Party DPAs | [All in place/N missing] | [N issues] |
| International Transfers | [Safeguarded/Unsafeguarded] | [N issues] |
| **Overall Compliance** | **[Compliant/Partially/Non-Compliant]** | **[Total issues]** |

### Critical Findings
1. [Finding with severity and remediation]
2. [Finding with severity and remediation]

### Recommendations
1. [Recommendation with priority and effort]
2. [Recommendation with priority and effort]
```

### Implementation Checklist

- [ ] Record of Processing Activities (ROPA) completed
- [ ] Lawful basis documented for each processing activity
- [ ] Consent management UI implemented with granular, separate consents
- [ ] Consent records stored and server-synced
- [ ] SDKs initialized only after consent (consent-gated)
- [ ] Data export (access/portability) functional and tested
- [ ] Account deletion process implemented end-to-end
- [ ] Data deletion propagated to all third-party processors
- [ ] On-device data cleared on deletion
- [ ] Data breach response plan documented
- [ ] DPAs in place with all third-party processors
- [ ] International transfer safeguards documented (SCCs)
- [ ] Privacy Manifests (PrivacyInfo.xcprivacy) reviewed for all SDKs
- [ ] Privacy policy aligned with actual data practices
- [ ] Legal counsel review completed

---

## Techniques Used

- **ST-01** (Clear Objective): Focused on comprehensive GDPR compliance assessment
- **ST-02** (Sequential Instructions): Phased from inventory through implementation to audit
- **RT-02** (Multi-Dimensional Analysis): Covers legal, technical, and organizational measures

---

## Related Prompts

- [ios_privacy_policy_generator.md](../publishing/ios_privacy_policy_generator.md) - Generate privacy policy aligned with audit findings
- [ios_privacy_compliance.md](../publishing/ios_privacy_compliance.md) - Apple-specific privacy framework compliance
- [ios_privacy_labels_generator.md](../publishing/ios_privacy_labels_generator.md) - App Store privacy nutrition labels
- [ios_terms_of_service_generator.md](../publishing/ios_terms_of_service_generator.md) - Terms of service with GDPR considerations
