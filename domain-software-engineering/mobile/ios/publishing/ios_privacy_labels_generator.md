---
title: "iOS Privacy Labels Generator"
category: mobile-development
description: "Modular guide for generating accurate App Store privacy nutrition labels by auditing first-party data collection and third-party SDK data practices."
techniques:
  - ST-01 (Structured Task Decomposition)
  - RT-02 (Checklist Verification)
  - DS-02 (Domain-Specific Terminology)
  - AN-01 (Analysis Framework)
difficulty: intermediate
tags:
  - ios
  - swift
  - app-store
  - privacy
  - privacy-labels
  - nutrition-labels
  - sdk-audit
  - data-collection
updated: "2026-03-19"
---

# iOS Privacy Labels Generator

**Objective:** Generate accurate App Store privacy nutrition labels by systematically auditing all data collection across first-party code and third-party SDKs. This prompt produces a complete data collection map ready for entry into App Store Connect, ensuring no data type is overlooked and all purposes and linkage are correctly classified.

**When to Use:** Before initial App Store submission, when adding new SDKs, when updating privacy labels for a new version, during annual privacy audits, or when Apple flags privacy label inaccuracies during review.

**Prompt Type:** Modular (approximately 260 lines)

## Context Gathering

1. What third-party SDKs and frameworks does the app integrate?
2. Does the app require user account creation with profile information?
3. Does the app access device sensors or system APIs (location, camera, contacts)?
4. Does the app include advertising or cross-app tracking?
5. Does the app process payments directly or through a third-party?
6. Does the app include social features (messaging, sharing, user content)?

## Instructions

### CRITICAL: Verification Requirements

- [ ] Every data type collected by first-party code is documented
- [ ] Every third-party SDK's data collection is verified against its privacy documentation
- [ ] Data linkage (linked to identity vs not) is accurately determined
- [ ] Data used for tracking is flagged and ATT compliance verified
- [ ] All purposes are correctly mapped using Apple's defined categories
- [ ] Privacy labels match the PrivacyInfo.xcprivacy manifest declarations

### False-Positive Prevention

- ❌ DO NOT mark data as "not collected" if any SDK collects it on your behalf
- ❌ DO NOT assume analytics SDKs only collect "anonymous" data; device IDs are identifiers
- ❌ DO NOT classify crash report data as "not linked" if it includes user IDs in logs
- ❌ DO NOT omit server-side data collection from privacy labels; they must reflect total data practices
- ❌ DO NOT list "App Functionality" as the purpose for advertising-related data collection
- ✅ DO review each SDK's privacy manifest (PrivacyInfo.xcprivacy) if available
- ✅ DO check SDK documentation and privacy pages for data collection disclosures
- ✅ DO consider data collected by your backend server, not just the client app
- ✅ DO ask SDK vendors for their data disclosure if documentation is unclear

## Module 1: First-Party Data Audit

Scan your codebase for data collection:

```bash
# Search for common data collection patterns in Swift code
echo "=== User Input Collection ==="
grep -rn "UITextField\|UITextView\|.text =\|textField.text" --include="*.swift" YourProject/

echo "=== Location Services ==="
grep -rn "CLLocationManager\|requestLocation\|startUpdatingLocation\|CLGeocoder" --include="*.swift" YourProject/

echo "=== Camera/Photos ==="
grep -rn "AVCaptureSession\|UIImagePickerController\|PHPhotoLibrary\|PHAsset" --include="*.swift" YourProject/

echo "=== Contacts ==="
grep -rn "CNContactStore\|CNContact\|ABAddressBook" --include="*.swift" YourProject/

echo "=== Health Data ==="
grep -rn "HKHealthStore\|HKQuantityType\|HKWorkout" --include="*.swift" YourProject/

echo "=== Keychain/Credentials ==="
grep -rn "SecItemAdd\|SecItemCopyMatching\|KeychainWrapper" --include="*.swift" YourProject/

echo "=== Network Requests (API calls sending data) ==="
grep -rn "URLSession\|Alamofire\|URLRequest" --include="*.swift" YourProject/

echo "=== UserDefaults Storage ==="
grep -rn "UserDefaults\|NSUserDefaults" --include="*.swift" YourProject/

echo "=== CoreData/Database ==="
grep -rn "NSManagedObject\|NSPersistentContainer\|RealmSwift\|GRDB" --include="*.swift" YourProject/
```

```
FIRST-PARTY DATA AUDIT TEMPLATE:

User-Provided Data:
┌──────────────────────┬───────────┬───────────────┬──────────────────────────┐
│ Data Point           │ Collected?│ Where in Code │ Sent to Server?          │
├──────────────────────┼───────────┼───────────────┼──────────────────────────┤
│ Name                 │ [ ]       │               │ [ ] Yes  [ ] No          │
│ Email                │ [ ]       │               │ [ ] Yes  [ ] No          │
│ Phone Number         │ [ ]       │               │ [ ] Yes  [ ] No          │
│ Physical Address     │ [ ]       │               │ [ ] Yes  [ ] No          │
│ Date of Birth        │ [ ]       │               │ [ ] Yes  [ ] No          │
│ Username/Handle      │ [ ]       │               │ [ ] Yes  [ ] No          │
│ Password             │ [ ]       │               │ [ ] Yes  [ ] No          │
│ Payment Card Info    │ [ ]       │               │ [ ] Yes  [ ] No          │
│ Profile Photo        │ [ ]       │               │ [ ] Yes  [ ] No          │
│ User-Generated Content│ [ ]      │               │ [ ] Yes  [ ] No          │
└──────────────────────┴───────────┴───────────────┴──────────────────────────┘

Device/Sensor Data:
┌──────────────────────┬───────────┬───────────────┬──────────────────────────┐
│ Data Point           │ Collected?│ Precision     │ Purpose                  │
├──────────────────────┼───────────┼───────────────┼──────────────────────────┤
│ Precise Location     │ [ ]       │ GPS-level     │                          │
│ Coarse Location      │ [ ]       │ City-level    │                          │
│ Photos/Videos        │ [ ]       │               │                          │
│ Camera (live)        │ [ ]       │               │                          │
│ Microphone           │ [ ]       │               │                          │
│ Contacts             │ [ ]       │               │                          │
│ Calendar Events      │ [ ]       │               │                          │
│ Motion/Fitness       │ [ ]       │               │                          │
│ Health Data          │ [ ]       │               │                          │
│ Bluetooth Devices    │ [ ]       │               │                          │
└──────────────────────┴───────────┴───────────────┴──────────────────────────┘
```

## Module 2: Third-Party SDK Audit

```
SDK DATA COLLECTION REFERENCE:

Common SDKs and Their Known Data Collection:

Firebase Analytics:
  - Device ID (linked, analytics)
  - Usage Data (not linked, analytics)
  - Diagnostics (not linked, analytics)
  Privacy manifest: Included in Firebase 10.22.0+

Firebase Crashlytics:
  - Crash Data (not linked, app functionality)
  - Device ID (not linked, app functionality)
  - Performance Data (not linked, app functionality)

Google AdMob:
  - Device ID (linked, third-party advertising)
  - Usage Data (linked, third-party advertising)
  - Coarse Location (not linked, third-party advertising)
  - Diagnostics (not linked, developer advertising)
  TRACKING: YES - Requires ATT

Facebook SDK (Meta):
  - Device ID (linked, third-party advertising + analytics)
  - Usage Data (linked, third-party advertising)
  - Purchase History (linked, third-party advertising)
  TRACKING: YES - Requires ATT

Adjust / AppsFlyer / Branch (Attribution):
  - Device ID (linked, third-party advertising)
  - Usage Data (linked, third-party advertising)
  - Purchase History (linked, third-party advertising)
  TRACKING: YES - Requires ATT

Stripe:
  - Payment Info (linked, app functionality)
  - Contact Info used for fraud prevention (linked, app functionality)
  NOT tracking

RevenueCat:
  - Purchase History (linked, app functionality)
  - Device ID (linked, analytics)
  NOT tracking

Mixpanel / Amplitude:
  - Usage Data (linked or not linked, analytics)
  - Device ID (linked or not linked, analytics)
  Check configuration: anonymous mode vs identified mode

Sentry:
  - Crash Data (not linked, app functionality)
  - Performance Data (not linked, app functionality)
  Check if user context is attached to events

OneSignal / Braze (Push):
  - Device ID (linked, app functionality)
  - Usage Data (linked if segmented, analytics)
```

```
YOUR SDK AUDIT TEMPLATE:
┌─────────────────────┬──────────────────────┬───────────┬──────────────┐
│ SDK Name + Version  │ Data Types Collected  │ Tracking? │ Has Privacy  │
│                     │                       │           │ Manifest?    │
├─────────────────────┼──────────────────────┼───────────┼──────────────┤
│                     │                       │ [ ]       │ [ ]          │
│                     │                       │ [ ]       │ [ ]          │
│                     │                       │ [ ]       │ [ ]          │
│                     │                       │ [ ]       │ [ ]          │
│                     │                       │ [ ]       │ [ ]          │
└─────────────────────┴──────────────────────┴───────────┴──────────────┘
```

## Module 3: Privacy Label Generation

Map all collected data to Apple's privacy label categories:

```
APP STORE CONNECT PRIVACY LABELS:

For each data type, determine:
1. COLLECTED: Is this data type collected? (Yes/No)
2. LINKED: Is the data linked to the user's identity? (Yes/No)
3. TRACKING: Is the data used for tracking? (Yes/No)
4. PURPOSE: One or more of Apple's defined purposes

Apple's Defined Purposes:
- Third-Party Advertising
- Developer's Advertising or Marketing
- Analytics
- Product Personalization
- App Functionality
- Other Purposes

GENERATED PRIVACY LABELS:
┌─────────────────────────┬──────────┬────────┬──────────┬──────────────────────┐
│ Data Type               │ Collected│ Linked │ Tracking │ Purpose(s)           │
├─────────────────────────┼──────────┼────────┼──────────┼──────────────────────┤
│ Contact Info            │          │        │          │                      │
│   Name                  │ [ ]      │ [ ]    │ [ ]      │                      │
│   Email Address         │ [ ]      │ [ ]    │ [ ]      │                      │
│   Phone Number          │ [ ]      │ [ ]    │ [ ]      │                      │
│   Physical Address      │ [ ]      │ [ ]    │ [ ]      │                      │
│ Health & Fitness        │          │        │          │                      │
│   Health                │ [ ]      │ [ ]    │ [ ]      │                      │
│   Fitness               │ [ ]      │ [ ]    │ [ ]      │                      │
│ Financial Info          │          │        │          │                      │
│   Payment Info          │ [ ]      │ [ ]    │ [ ]      │                      │
│   Credit Info           │ [ ]      │ [ ]    │ [ ]      │                      │
│ Location                │          │        │          │                      │
│   Precise Location      │ [ ]      │ [ ]    │ [ ]      │                      │
│   Coarse Location       │ [ ]      │ [ ]    │ [ ]      │                      │
│ Sensitive Info          │ [ ]      │ [ ]    │ [ ]      │                      │
│ Contacts                │ [ ]      │ [ ]    │ [ ]      │                      │
│ User Content            │          │        │          │                      │
│   Emails or Messages    │ [ ]      │ [ ]    │ [ ]      │                      │
│   Photos or Videos      │ [ ]      │ [ ]    │ [ ]      │                      │
│   Audio Data            │ [ ]      │ [ ]    │ [ ]      │                      │
│   Gameplay Content      │ [ ]      │ [ ]    │ [ ]      │                      │
│   Customer Support      │ [ ]      │ [ ]    │ [ ]      │                      │
│   Other User Content    │ [ ]      │ [ ]    │ [ ]      │                      │
│ Browsing History        │ [ ]      │ [ ]    │ [ ]      │                      │
│ Search History          │ [ ]      │ [ ]    │ [ ]      │                      │
│ Identifiers             │          │        │          │                      │
│   User ID               │ [ ]      │ [ ]    │ [ ]      │                      │
│   Device ID             │ [ ]      │ [ ]    │ [ ]      │                      │
│ Purchases               │ [ ]      │ [ ]    │ [ ]      │                      │
│ Usage Data              │          │        │          │                      │
│   Product Interaction   │ [ ]      │ [ ]    │ [ ]      │                      │
│   Advertising Data      │ [ ]      │ [ ]    │ [ ]      │                      │
│   Other Usage Data      │ [ ]      │ [ ]    │ [ ]      │                      │
│ Diagnostics             │          │        │          │                      │
│   Crash Data            │ [ ]      │ [ ]    │ [ ]      │                      │
│   Performance Data      │ [ ]      │ [ ]    │ [ ]      │                      │
│   Other Diagnostic Data │ [ ]      │ [ ]    │ [ ]      │                      │
└─────────────────────────┴──────────┴────────┴──────────┴──────────────────────┘
```

## Module 4: Validation

```
VALIDATION CHECKLIST:
[ ] Every SDK in Podfile/Package.swift has been audited
[ ] First-party API calls are mapped to data types
[ ] No data type is marked "not collected" when any source collects it
[ ] "Linked to identity" is true if ANY mechanism can associate data with a user
[ ] "Tracking" is true if data is shared with data brokers or used for cross-app advertising
[ ] Privacy labels are consistent with PrivacyInfo.xcprivacy manifest
[ ] Labels match the privacy policy hosted at the App Store Connect URL
[ ] Labels cover both client-side and server-side data handling
```

## Expected Output

After completing this prompt, you will have:

1. A complete first-party data collection audit with code references
2. A third-party SDK data collection inventory
3. Filled-out privacy label table ready for App Store Connect entry
4. Validation confirming consistency between labels, manifest, and privacy policy

## Example Interaction

**User:** My recipe app uses Firebase Analytics, Crashlytics, and RevenueCat. Users create accounts with email and can upload recipe photos. No ads.

**Assistant:** Here are your privacy labels:

| Data Type | Collected | Linked | Tracking | Purpose |
|-----------|-----------|--------|----------|---------|
| Email Address | Yes | Yes | No | App Functionality |
| Photos | Yes | Yes | No | App Functionality |
| User ID | Yes | Yes | No | App Functionality, Analytics |
| Device ID | Yes | No | No | Analytics |
| Purchase History | Yes | Yes | No | App Functionality |
| Product Interaction | Yes | No | No | Analytics |
| Crash Data | Yes | No | No | App Functionality |
| Performance Data | Yes | No | No | App Functionality |

**Tracking: No** -- None of your SDKs perform cross-app tracking, so ATT is not required.

## Techniques Used

| Technique | Application |
|-----------|-------------|
| ST-01 (Structured Task Decomposition) | Four-module audit workflow |
| RT-02 (Checklist Verification) | Data collection and validation checklists |
| DS-02 (Domain-Specific Terminology) | Apple's privacy label categories and SDK terms |
| AN-01 (Analysis Framework) | Systematic code and SDK analysis |

## Related Prompts

- [ios_privacy_compliance.md](ios_privacy_compliance.md) - Full privacy compliance including GDPR, CCPA, and ATT
- [ios_privacy_policy_generator.md](ios_privacy_policy_generator.md) - Generate privacy policy matching these labels
- [ios_gdpr_compliance_audit.md](ios_gdpr_compliance_audit.md) - GDPR-specific data mapping audit
- [ios_app_review_guidelines_check.md](ios_app_review_guidelines_check.md) - Full compliance check including privacy

## Customization Guide

- **For apps with no third-party SDKs:** Skip Module 2 and focus on first-party code audit only
- **For apps with 10+ SDKs:** Create a spreadsheet version of the SDK audit template and assign SDK review to individual team members
- **For apps using server-side analytics (Plausible, Matomo):** Include server-side collection in the audit even though it is not in the client binary
- **For apps with multiple targets (app + extensions):** Audit each target separately and combine results
- **For apps migrating from UIKit to SwiftUI:** Re-audit data flows as architecture changes may introduce new collection points
