---
title: "iOS Privacy Compliance"
category: mobile-development
description: "Comprehensive guide for ensuring iOS app privacy compliance including privacy nutrition labels, App Tracking Transparency, GDPR/CCPA requirements, and PrivacyInfo.xcprivacy manifest configuration."
techniques:
  - ST-01 (Structured Task Decomposition)
  - RT-02 (Checklist Verification)
  - RT-05 (Constraint Specification)
  - DS-02 (Domain-Specific Terminology)
  - QA-01 (Quality Assurance Gates)
  - FP-01 (False-Positive Prevention)
difficulty: advanced
tags:
  - ios
  - swift
  - app-store
  - privacy
  - gdpr
  - ccpa
  - att
  - privacy-manifest
  - tracking-transparency
updated: "2026-03-19"
---

# iOS Privacy Compliance

**Objective:** Ensure comprehensive privacy compliance for an iOS application by auditing data collection practices, configuring privacy nutrition labels in App Store Connect, implementing App Tracking Transparency (ATT), addressing GDPR and CCPA requirements, and building a complete PrivacyInfo.xcprivacy privacy manifest. This prompt covers the full spectrum of Apple's privacy requirements as well as major regulatory frameworks.

**When to Use:** During initial app submission, when adding new SDKs or data collection features, during annual privacy audits, when expanding to EU or California markets, or whenever Apple updates its privacy requirements. Required before every App Store submission since Apple enforces privacy manifests for all apps and SDKs.

**Prompt Type:** Comprehensive (approximately 420 lines)

## Context Gathering

1. What data does your app collect directly from users (name, email, location, photos, health data, etc.)?
2. What third-party SDKs are integrated (analytics, advertising, crash reporting, social login)?
3. Does the app track users across other companies' apps or websites for advertising purposes?
4. Does the app use any of the required reason APIs (UserDefaults, file timestamp, disk space, system boot time, active keyboard)?
5. What is the app's target market (US only, EU, global)?
6. Does the app handle data from children under 13 (COPPA considerations)?
7. Does the app offer account creation? If so, does it support account deletion?
8. What server-side data storage and processing does the backend perform?

## Instructions

### CRITICAL: Verification Requirements

- [ ] PrivacyInfo.xcprivacy is included in ALL app targets and framework targets
- [ ] Every required reason API usage has a declared reason in the privacy manifest
- [ ] Privacy nutrition labels in App Store Connect accurately reflect ALL data collection
- [ ] ATT prompt is shown BEFORE any tracking occurs
- [ ] GDPR consent is collected BEFORE processing EU user data
- [ ] Account deletion functionality is implemented and accessible
- [ ] All third-party SDK privacy manifests are present and accurate
- [ ] Privacy policy URL is valid and accessible from App Store listing

### False-Positive Prevention

- ❌ DO NOT declare data as "not linked to user" if you have any mechanism to associate it (even indirectly via device ID)
- ❌ DO NOT assume crash reporting data is exempt from privacy labels; stack traces can contain user data
- ❌ DO NOT skip ATT because you "only use first-party analytics"; if any SDK performs cross-app tracking, ATT is required
- ❌ DO NOT list purposes as "App Functionality" when the actual purpose is analytics or advertising
- ❌ DO NOT assume third-party SDKs handle their own privacy compliance; you are responsible for all data your app collects
- ❌ DO NOT confuse Apple's privacy nutrition labels with GDPR consent; both are independently required
- ✅ DO audit every SDK's documentation for data collection disclosures
- ✅ DO use Apple's required reason API categories exactly as specified
- ✅ DO test ATT flow on a real device (simulator always returns .notDetermined)
- ✅ DO provide granular GDPR consent options, not just a single "accept all" button
- ✅ DO verify privacy labels match between your app and any embedded frameworks

## Step 1: Privacy Manifest (PrivacyInfo.xcprivacy)

Create the privacy manifest file required by Apple since Spring 2024:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <!-- Privacy Tracking Enabled -->
    <key>NSPrivacyTracking</key>
    <false/>

    <!-- Tracking Domains (if NSPrivacyTracking is true) -->
    <key>NSPrivacyTrackingDomains</key>
    <array>
        <!-- <string>analytics.example.com</string> -->
    </array>

    <!-- Collected Data Types -->
    <key>NSPrivacyCollectedDataTypes</key>
    <array>
        <dict>
            <key>NSPrivacyCollectedDataType</key>
            <string>NSPrivacyCollectedDataTypeEmailAddress</string>
            <key>NSPrivacyCollectedDataTypeLinked</key>
            <true/>
            <key>NSPrivacyCollectedDataTypeTracking</key>
            <false/>
            <key>NSPrivacyCollectedDataTypePurposes</key>
            <array>
                <string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>
            </array>
        </dict>
    </array>

    <!-- Required Reason APIs -->
    <key>NSPrivacyAccessedAPITypes</key>
    <array>
        <dict>
            <key>NSPrivacyAccessedAPIType</key>
            <string>NSPrivacyAccessedAPICategoryUserDefaults</string>
            <key>NSPrivacyAccessedAPITypeReasons</key>
            <array>
                <string>CA92.1</string>
            </array>
        </dict>
        <dict>
            <key>NSPrivacyAccessedAPIType</key>
            <string>NSPrivacyAccessedAPICategoryFileTimestamp</string>
            <key>NSPrivacyAccessedAPITypeReasons</key>
            <array>
                <string>C617.1</string>
            </array>
        </dict>
        <dict>
            <key>NSPrivacyAccessedAPIType</key>
            <string>NSPrivacyAccessedAPICategoryDiskSpace</string>
            <key>NSPrivacyAccessedAPITypeReasons</key>
            <array>
                <string>E174.1</string>
            </array>
        </dict>
        <dict>
            <key>NSPrivacyAccessedAPIType</key>
            <string>NSPrivacyAccessedAPICategorySystemBootTime</string>
            <key>NSPrivacyAccessedAPITypeReasons</key>
            <array>
                <string>35F9.1</string>
            </array>
        </dict>
    </array>
</dict>
</plist>
```

```
CHECKLIST - Privacy Manifest:
[ ] PrivacyInfo.xcprivacy added to the app target's Copy Bundle Resources
[ ] NSPrivacyTracking matches actual tracking behavior
[ ] All tracking domains listed if tracking is enabled
[ ] Every collected data type is declared with correct linkage and purpose
[ ] All required reason API usages have approved reason codes
[ ] Third-party framework targets each include their own PrivacyInfo.xcprivacy
[ ] Privacy manifest passes Xcode's Generate Privacy Report validation
```

Generate the privacy report in Xcode:

```
Xcode → Product → Archive → Distribute App → Generate Privacy Report
```

### Required Reason API Categories Reference

| API Category | Example APIs | Common Reason Codes |
|-------------|-------------|-------------------|
| File Timestamp | `NSFileCreationDate`, `NSFileModificationDate` | C617.1, 3B52.1, 0A2A.1 |
| System Boot Time | `systemUptime`, `ProcessInfo.processInfo.systemUptime` | 35F9.1 |
| Disk Space | `volumeAvailableCapacity`, `FileManager.attributesOfFileSystem` | E174.1, 85F4.1 |
| User Defaults | `UserDefaults.standard` | CA92.1, 1C8F.1 |
| Active Keyboards | `UITextInputMode.activeInputModes` | 54BD.1, 3EC4.1 |

## Step 2: Privacy Nutrition Labels (App Store Connect)

Map your data collection to App Store Connect categories:

```
DATA COLLECTION AUDIT TEMPLATE:

First-Party Data Collection:
┌─────────────────────────┬──────────┬───────────┬──────────────┬────────────────┐
│ Data Type               │ Collected│ Linked to │ Used for     │ Tracking?      │
│                         │          │ Identity? │ Tracking?    │                │
├─────────────────────────┼──────────┼───────────┼──────────────┼────────────────┤
│ Name                    │ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ Email Address           │ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ Phone Number            │ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ Physical Address        │ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ Precise Location        │ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ Coarse Location         │ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ Health & Fitness        │ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ Payment Info            │ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ Photos or Videos        │ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ Contacts                │ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ User Content            │ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ Search History          │ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ Browsing History        │ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ Identifiers (User ID)  │ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ Identifiers (Device ID)│ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ Purchase History        │ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ Usage Data              │ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ Diagnostics (Crash Data)│ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ Performance Data        │ [ ]      │ [ ]       │ [ ]          │ [ ]            │
│ Other Diagnostic Data   │ [ ]      │ [ ]       │ [ ]          │ [ ]            │
└─────────────────────────┴──────────┴───────────┴──────────────┴────────────────┘

Third-Party SDK Data Collection:
┌─────────────────────────┬──────────────────────┬─────────────────────────────┐
│ SDK Name                │ Data Types Collected  │ Purposes                    │
├─────────────────────────┼──────────────────────┼─────────────────────────────┤
│ Firebase Analytics      │ Usage Data, Device ID│ Analytics                   │
│ Firebase Crashlytics    │ Crash Data, Device ID│ App Functionality           │
│ Google AdMob            │ Device ID, Usage Data│ Third-Party Advertising     │
│ Facebook SDK            │ Device ID, Usage Data│ Third-Party Advertising     │
│ Mixpanel                │ Usage Data, Device ID│ Analytics                   │
│ Stripe                  │ Payment Info         │ App Functionality           │
│ (Add your SDKs here)    │                      │                             │
└─────────────────────────┴──────────────────────┴─────────────────────────────┘
```

## Step 3: App Tracking Transparency (ATT)

Implement ATT when any form of cross-app tracking occurs:

```swift
import AppTrackingTransparency
import AdSupport

final class TrackingManager {
    static func requestTrackingPermission() {
        // CRITICAL: Only request after app is fully loaded and user has context
        // Do NOT request on first launch immediately
        guard #available(iOS 14, *) else { return }

        ATTrackingManager.requestTrackingAuthorization { status in
            DispatchQueue.main.async {
                switch status {
                case .authorized:
                    // Enable tracking SDKs
                    let idfa = ASIdentifierManager.shared().advertisingIdentifier
                    Analytics.shared.enableTracking(idfa: idfa)
                case .denied, .restricted:
                    // Disable all tracking, use only non-tracking analytics
                    Analytics.shared.disableTracking()
                case .notDetermined:
                    // Should not happen after request, but handle gracefully
                    Analytics.shared.disableTracking()
                @unknown default:
                    Analytics.shared.disableTracking()
                }
            }
        }
    }
}
```

```
CHECKLIST - App Tracking Transparency:
[ ] NSUserTrackingUsageDescription is set in Info.plist with clear, specific language
[ ] ATT prompt appears BEFORE any tracking begins
[ ] ATT is NOT requested on first app launch splash screen (Apple rejects this)
[ ] App functions correctly when tracking is denied
[ ] IDFA is only accessed after authorization is granted
[ ] All advertising SDKs respect the ATT status
[ ] SKAdNetwork is configured as fallback for denied tracking
```

## Step 4: GDPR Compliance

```
CHECKLIST - GDPR Requirements:
[ ] Lawful basis identified for each data processing activity
[ ] Explicit consent collected before processing (not pre-checked boxes)
[ ] Users can withdraw consent at any time, as easily as they gave it
[ ] Privacy policy explains data processing in plain language
[ ] Data processing agreement (DPA) signed with all third-party processors
[ ] Right to access: users can export their data
[ ] Right to deletion: users can delete their account and all data
[ ] Right to rectification: users can correct their data
[ ] Right to portability: data export in machine-readable format
[ ] Data breach notification process documented (72-hour requirement)
[ ] Data Protection Impact Assessment (DPIA) completed if high-risk processing
[ ] Records of processing activities maintained
[ ] EU representative appointed if company is outside EU
```

## Step 5: CCPA Compliance

```
CHECKLIST - CCPA Requirements:
[ ] "Do Not Sell or Share My Personal Information" link accessible
[ ] Users can opt out of sale of personal information
[ ] Financial incentives for data collection are clearly disclosed
[ ] Privacy policy updated with CCPA-specific disclosures
[ ] Consumers can request disclosure of collected personal information
[ ] Respond to verifiable consumer requests within 45 days
[ ] Do not discriminate against consumers who exercise CCPA rights
[ ] Service provider agreements include CCPA-required provisions
```

## Step 6: Account Deletion Requirement

Apple requires all apps that offer account creation to also offer account deletion:

```
CHECKLIST - Account Deletion:
[ ] Account deletion option is discoverable in app settings
[ ] Deletion process is not unreasonably difficult
[ ] Users are informed what data will be deleted
[ ] Server-side data is actually deleted (not just deactivated) within 14 days
[ ] Associated data in third-party services is also deleted
[ ] Subscriptions are addressed during deletion flow
[ ] Confirmation is required before irreversible deletion
[ ] Apple's Sign in with Apple token revocation API is called if SIWA is used
```

```swift
// Sign in with Apple token revocation on account deletion
func revokeAppleSignInToken(authorizationCode: String) async throws {
    let url = URL(string: "https://appleid.apple.com/auth/revoke")!
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")

    let body = "client_id=\(bundleId)&client_secret=\(clientSecret)&token=\(authorizationCode)&token_type_hint=access_token"
    request.httpBody = body.data(using: .utf8)

    let (_, response) = try await URLSession.shared.data(for: request)
    guard let httpResponse = response as? HTTPURLResponse,
          httpResponse.statusCode == 200 else {
        throw AccountDeletionError.tokenRevocationFailed
    }
}
```

## Expected Output

After completing this prompt, you will have:

1. A complete PrivacyInfo.xcprivacy manifest with all required reason APIs and collected data types
2. Accurate privacy nutrition labels ready for App Store Connect submission
3. ATT implementation that complies with Apple's guidelines
4. GDPR compliance checklist verified for EU users
5. CCPA compliance checklist verified for California users
6. Account deletion flow that meets Apple's requirements
7. A privacy audit trail documenting all data collection and processing

## Example Interaction

**User:** My social media app collects email, photos, location, and uses Firebase Analytics, Facebook SDK for ads, and Crashlytics. We serve users in the US and EU.

**Assistant:** Given your SDK stack and EU presence, here is your privacy compliance plan:

**Privacy Manifest (PrivacyInfo.xcprivacy):**
- `NSPrivacyTracking`: `true` (Facebook SDK performs cross-app tracking)
- Tracking Domains: `graph.facebook.com`, `facebook.com`
- Collected Data Types: Email (linked, app functionality), Photos (linked, app functionality), Location (linked, app functionality), Device ID (linked, tracking + analytics), Usage Data (not linked, analytics), Crash Data (not linked, app functionality)

**ATT Required:** Yes, Facebook SDK requires ATT authorization before initialization.

**GDPR:** Required. You need explicit consent for: analytics (Firebase), advertising (Facebook), location, and photo processing. Implement a granular consent screen before any SDK initialization.

**Nutrition Labels:** You must declare 6 data types across 3 purposes...

## Techniques Used

| Technique | Application |
|-----------|-------------|
| ST-01 (Structured Task Decomposition) | Six-step privacy compliance workflow |
| RT-02 (Checklist Verification) | Detailed checklists for each regulatory framework |
| RT-05 (Constraint Specification) | Apple's exact API reason codes and data type identifiers |
| DS-02 (Domain-Specific Terminology) | Privacy-specific terms: IDFA, ATT, DPA, DPIA, required reason APIs |
| QA-01 (Quality Assurance Gates) | Each step validates before proceeding |
| FP-01 (False-Positive Prevention) | Prevents common misclassifications in privacy labels |

## Related Prompts

- [ios_privacy_labels_generator.md](ios_privacy_labels_generator.md) - Focused tool for generating privacy nutrition labels from SDK audit
- [ios_privacy_policy_generator.md](ios_privacy_policy_generator.md) - Generate a privacy policy tailored to your app
- [ios_gdpr_compliance_audit.md](ios_gdpr_compliance_audit.md) - Deep GDPR audit with data mapping and consent flows
- [ios_release_preparation.md](ios_release_preparation.md) - Overall release preparation including Info.plist audit
- [ios_app_review_guidelines_check.md](ios_app_review_guidelines_check.md) - Full guideline compliance audit

## Customization Guide

- **For apps without advertising:** Remove ATT section and Facebook SDK references; focus on analytics and crash reporting privacy labels
- **For health/fitness apps:** Add HealthKit-specific privacy considerations and heightened GDPR protections for health data (special category data under GDPR Article 9)
- **For children's apps (COPPA):** Add COPPA compliance section, disable all tracking, require parental consent, limit data collection
- **For apps with subscription billing:** Add payment data handling, Stripe/RevenueCat privacy considerations
- **For apps targeting Brazil:** Add LGPD compliance requirements alongside GDPR
- **For apps using CloudKit:** Address iCloud data residency and Apple's role as data processor
