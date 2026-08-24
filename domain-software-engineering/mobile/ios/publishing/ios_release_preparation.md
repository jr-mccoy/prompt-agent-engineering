---
title: "iOS Release Preparation"
category: mobile-development
description: "Comprehensive guide for preparing an iOS app for App Store submission including archive configuration, code signing validation, entitlements review, Info.plist audit, and pre-submission checklist."
techniques:
  - ST-01 (Structured Task Decomposition)
  - RT-02 (Checklist Verification)
  - RT-05 (Constraint Specification)
  - DS-02 (Domain-Specific Terminology)
  - QA-01 (Quality Assurance Gates)
difficulty: intermediate
tags:
  - ios
  - swift
  - app-store
  - release
  - code-signing
  - entitlements
  - info-plist
  - xcode
updated: "2026-03-19"
---

# iOS Release Preparation

**Objective:** Systematically prepare an iOS application for App Store submission by validating archive configuration, code signing identity and provisioning profiles, entitlements, Info.plist keys, and completing a comprehensive pre-submission checklist. This prompt ensures no critical step is missed before uploading a build to App Store Connect.

**When to Use:** Before every App Store submission, after feature freeze and QA sign-off, when the build is ready to move from development to distribution. Use this prompt each release cycle to catch configuration drift, expired certificates, or missing entitlements before Apple's automated and manual review.

**Prompt Type:** Comprehensive (approximately 350 lines)

## Context Gathering

1. What is the app's Bundle Identifier (e.g., `com.company.appname`)?
2. What Xcode version and minimum deployment target are you using?
3. Does the app use any special capabilities (Push Notifications, Sign in with Apple, HealthKit, App Groups, iCloud, etc.)?
4. What distribution method are you targeting (App Store, Ad Hoc, Enterprise)?
5. Does the app include app extensions (widgets, share extensions, notification service extensions)?
6. Are you using manual or automatic code signing in Xcode?
7. What CI/CD system, if any, is used for building the archive?
8. Does the app use any third-party SDKs that require specific entitlements or Info.plist keys?

## Instructions

### CRITICAL: Verification Requirements

Every release preparation must satisfy ALL of the following before upload:

- [ ] Archive builds successfully with zero errors and zero warnings in Release configuration
- [ ] Code signing identity is a valid Apple Distribution certificate (not expired, not revoked)
- [ ] Provisioning profile matches Bundle ID, includes all required entitlements, and is not expired
- [ ] All entitlements in the built binary match the provisioning profile exactly
- [ ] Info.plist contains all required keys with valid values for the target iOS version
- [ ] No debug-only keys, test API endpoints, or development flags remain in the Release build
- [ ] App version and build number are correctly incremented and unique in App Store Connect

### False-Positive Prevention

- ❌ DO NOT assume automatic signing resolves all issues; manual verification is still required for entitlement mismatches
- ❌ DO NOT skip entitlements review because "it worked last time"; profile regeneration can silently drop entitlements
- ❌ DO NOT rely solely on Xcode's built-in validation; it does not catch all App Store rejection reasons
- ❌ DO NOT leave `NSAllowsArbitraryLoads` set to `YES` in production builds without explicit exception domains
- ❌ DO NOT forget to remove `get-task-allow` entitlement in distribution builds
- ✅ DO verify entitlements by inspecting the actual .app bundle, not just the Xcode project
- ✅ DO cross-reference your provisioning profile's entitlements list with the Entitlements.plist
- ✅ DO test the archive on a physical device via Ad Hoc distribution before uploading
- ✅ DO check that all URL schemes, associated domains, and background modes are intentional

## Step-by-Step Release Preparation

### Step 1: Archive Configuration Validation

Verify the Xcode project's Release build configuration:

```
CHECKLIST - Archive Configuration:
[ ] Scheme is set to Release configuration for Archive action
[ ] Build Settings → Code Signing Identity = "Apple Distribution"
[ ] Build Settings → Code Signing Style = Manual (recommended) or Automatic
[ ] Optimization Level = -Os (Fastest, Smallest) for Release
[ ] DEBUG_INFORMATION_FORMAT = dwarf-with-dsym
[ ] SWIFT_OPTIMIZATION_LEVEL = -O (Optimize for Speed) or -Osize
[ ] GCC_PREPROCESSOR_DEFINITIONS does NOT include DEBUG=1 for Release
[ ] SWIFT_ACTIVE_COMPILATION_CONDITIONS does NOT include DEBUG for Release
[ ] ENABLE_TESTABILITY = NO for Release
[ ] Any environment-switching logic points to production endpoints
[ ] Strip Debug Symbols During Copy = YES
[ ] Strip Swift Symbols = YES
```

Template for verifying via command line:

```bash
# Extract build settings for Release configuration
xcodebuild -showBuildSettings -configuration Release -scheme "YourScheme" | grep -E "(CODE_SIGN|PROVISIONING|PRODUCT_BUNDLE_IDENTIFIER|SWIFT_OPTIMIZATION|DEBUG)"
```

### Step 2: Code Signing Validation

```
CHECKLIST - Code Signing:
[ ] Apple Distribution certificate is installed in Keychain Access
[ ] Certificate is not expired (check expiration date)
[ ] Certificate is not revoked (verify in Apple Developer Portal)
[ ] Private key is present alongside the certificate in Keychain
[ ] Provisioning profile is valid and not expired
[ ] Provisioning profile includes the correct App ID
[ ] Provisioning profile includes the Apple Distribution certificate
[ ] For CI/CD: p12/certificate and provisioning profile are correctly installed on build machine
```

Verify signing with codesign:

```bash
# After archiving, verify the .app is signed correctly
codesign -dv --verbose=4 /path/to/YourApp.app

# Verify the provisioning profile embedded in the archive
security cms -D -i /path/to/YourApp.app/embedded.mobileprovision

# Check certificate expiration
security find-identity -v -p codesigning
```

### Step 3: Entitlements Review

Extract and validate entitlements from the built binary:

```bash
# Extract entitlements from the archived .app
codesign -d --entitlements - /path/to/YourApp.app

# Compare with your Entitlements.plist in the project
diff <(codesign -d --entitlements - /path/to/YourApp.app 2>/dev/null) YourApp.entitlements
```

```
CHECKLIST - Entitlements:
[ ] aps-environment = "production" (not "development") for push notifications
[ ] com.apple.developer.associated-domains lists correct production domains
[ ] com.apple.security.application-groups matches across app and extensions
[ ] get-task-allow = false (must be false for distribution)
[ ] No development-only entitlements remain
[ ] Keychain access groups are correctly configured
[ ] HealthKit entitlements present only if HealthKit is used
[ ] Sign in with Apple entitlement present if feature is used
[ ] iCloud entitlements match iCloud container identifiers
[ ] All extension entitlements are consistent with the main app
```

### Step 4: Info.plist Audit

```
CHECKLIST - Required Info.plist Keys:
[ ] CFBundleDisplayName - User-facing app name
[ ] CFBundleIdentifier - Matches App Store Connect
[ ] CFBundleShortVersionString - Marketing version (e.g., "2.1.0")
[ ] CFBundleVersion - Build number, unique per upload (e.g., "42")
[ ] UILaunchStoryboardName - Launch screen configured
[ ] UISupportedInterfaceOrientations - Correct orientations for device
[ ] MinimumOSVersion - Matches deployment target
[ ] UIRequiredDeviceCapabilities - Only capabilities the app truly requires
[ ] LSApplicationQueriesSchemes - All URL schemes the app queries
[ ] ITSAppUsesNonExemptEncryption - Set correctly to avoid export compliance hold
```

```
CHECKLIST - Privacy Usage Description Keys (include ONLY those your app uses):
[ ] NSCameraUsageDescription - Camera access justification
[ ] NSPhotoLibraryUsageDescription - Photo library access
[ ] NSPhotoLibraryAddUsageDescription - Save to photo library
[ ] NSLocationWhenInUseUsageDescription - Location while in use
[ ] NSLocationAlwaysAndWhenInUseUsageDescription - Always location
[ ] NSMicrophoneUsageDescription - Microphone access
[ ] NSContactsUsageDescription - Contacts access
[ ] NSCalendarsUsageDescription - Calendar access
[ ] NSFaceIDUsageDescription - Face ID usage
[ ] NSHealthShareUsageDescription - HealthKit read
[ ] NSHealthUpdateUsageDescription - HealthKit write
[ ] NSUserTrackingUsageDescription - App Tracking Transparency
[ ] NSBluetoothAlwaysUsageDescription - Bluetooth usage
```

Verify no missing usage descriptions:

```bash
# Search for framework usage that requires Info.plist keys
grep -rn "AVCaptureSession\|CLLocationManager\|CNContactStore\|PHPhotoLibrary\|HKHealthStore\|ATTrackingManager" --include="*.swift" YourProject/
```

### Step 5: Pre-Submission Checklist

```
FINAL PRE-UPLOAD CHECKLIST:
[ ] App version number is incremented from last approved version
[ ] Build number is unique (never used before for this version)
[ ] All test/debug code is removed or gated behind compiler flags
[ ] No placeholder content (lorem ipsum, test images, sample data)
[ ] Crashlytics/analytics point to production configuration
[ ] API base URLs point to production servers
[ ] Feature flags are set to production values
[ ] App icon is present for all required sizes
[ ] Launch screen displays correctly on all supported devices
[ ] Archive validates successfully in Xcode Organizer
[ ] App runs correctly when installed from the archive (Ad Hoc test)
[ ] dSYM files are generated and ready for upload to crash reporting service
[ ] Export compliance information is accurate
[ ] Content rights declarations are correct
```

Upload verification:

```bash
# Validate the archive before upload
xcrun altool --validate-app -f YourApp.ipa -t ios -u "apple-id@example.com" -p "@keychain:AC_PASSWORD"

# Or using the newer notarytool / Transporter approach
xcrun notarytool submit YourApp.ipa --apple-id "apple-id@example.com" --team-id "TEAMID" --password "@keychain:AC_PASSWORD"
```

## Expected Output

After completing this prompt, you will have:

1. A fully validated Xcode archive in Release configuration
2. Confirmed code signing with a valid Apple Distribution identity
3. Entitlements verified against the provisioning profile with no mismatches
4. Info.plist audited for all required and privacy-related keys
5. A completed pre-submission checklist with all items verified
6. An IPA ready for upload to App Store Connect via Xcode Organizer, Transporter, or `xcrun altool`

## Example Interaction

**User:** I need to prepare my fitness app for App Store submission. It uses HealthKit, Push Notifications, and Sign in with Apple. We're on Xcode 16, targeting iOS 17+.

**Assistant:** I'll walk through the full release preparation for your fitness app. Let me start with your specific entitlements requirements:

**Entitlements needed:**
- `com.apple.developer.healthkit` (HealthKit)
- `com.apple.developer.healthkit.access` with appropriate health data types
- `aps-environment` = `production` (Push Notifications)
- `com.apple.developer.applesignin` = `["Default"]` (Sign in with Apple)

**Info.plist keys required:**
- `NSHealthShareUsageDescription` - "AppName reads your workout and activity data to track fitness goals."
- `NSHealthUpdateUsageDescription` - "AppName saves your completed workouts to Apple Health."

Let me now run through each checklist step for your specific configuration...

## Techniques Used

| Technique | Application |
|-----------|-------------|
| ST-01 (Structured Task Decomposition) | Breaking release preparation into five discrete validation phases |
| RT-02 (Checklist Verification) | Actionable checklists for each phase ensuring nothing is missed |
| RT-05 (Constraint Specification) | Explicit constraints on signing, entitlements, and configuration values |
| DS-02 (Domain-Specific Terminology) | Apple-specific terms: provisioning profiles, entitlements, codesign, dSYM |
| QA-01 (Quality Assurance Gates) | Each step serves as a quality gate before proceeding to the next |

## Related Prompts

- [ios_pre_submission_checklist.md](ios_pre_submission_checklist.md) - Expanded final checklist with metadata and App Store Connect configuration
- [ios_privacy_compliance.md](ios_privacy_compliance.md) - Deep dive into privacy nutrition labels and PrivacyInfo.xcprivacy
- [ios_app_review_guidelines_check.md](ios_app_review_guidelines_check.md) - Audit against Apple's App Review Guidelines
- [ios_testflight_rollout.md](ios_testflight_rollout.md) - Beta testing before production release
- [ios_release_management.md](ios_release_management.md) - Version numbering and phased release strategy

## Customization Guide

- **For CI/CD pipelines:** Add steps for Fastlane `match` or manual certificate installation, and replace Xcode Organizer steps with `xcodebuild -exportArchive` commands
- **For apps with extensions:** Duplicate the entitlements and signing checklists for each extension target, ensuring App Group entitlements are consistent
- **For enterprise distribution:** Replace "Apple Distribution" with "Apple Distribution (Enterprise)" and adjust provisioning profile type
- **For apps using CloudKit:** Add entitlements check for `com.apple.developer.icloud-services` and verify CloudKit container identifiers
- **For watchOS companion apps:** Include separate signing and entitlements validation for the WatchKit extension and Watch app targets
