---
title: "iOS Pre-Submission Checklist"
category: mobile-development
description: "Comprehensive final checklist for App Store submission covering metadata validation, binary verification, export compliance, age ratings, App Store Connect configuration, and common last-minute issues."
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
  - submission
  - checklist
  - metadata
  - export-compliance
  - age-rating
  - app-store-connect
updated: "2026-03-19"
---

# iOS Pre-Submission Checklist

**Objective:** Complete a final, comprehensive checklist before submitting an iOS app to the App Store. This prompt covers every field and configuration in App Store Connect, binary validation, export compliance declarations, age rating questionnaire, and commonly overlooked items that cause delays or rejections. Use this as the last gate before clicking "Submit for Review."

**When to Use:** After the build is uploaded and processed in App Store Connect, after all other preparation prompts have been completed, and as the final quality gate before submission. This checklist should be the last thing completed before submitting for review.

**Prompt Type:** Comprehensive (approximately 350 lines)

## Context Gathering

1. Is this the initial submission or an update to an existing app?
2. What version number and build number are being submitted?
3. Does the app use encryption beyond standard HTTPS?
4. Does the app contain any content that could affect age rating (violence, gambling, mature themes)?
5. Are there any App Store Connect features to configure (in-app events, custom product pages)?
6. Has the app been tested on all supported devices and iOS versions?

## Instructions

### CRITICAL: Verification Requirements

- [ ] Every section of this checklist is marked complete
- [ ] Build has been validated in Xcode Organizer or via altool without errors
- [ ] App Store Connect shows the build with a green checkmark (no processing issues)
- [ ] All App Store Connect fields are filled with final, reviewed content
- [ ] Review notes include demo credentials and any special instructions
- [ ] At least one team member has reviewed the complete submission

### False-Positive Prevention

- ❌ DO NOT submit with "TODO" or placeholder content in any field
- ❌ DO NOT leave the "What to Test" or "Review Notes" empty for complex apps
- ❌ DO NOT select "No" for encryption if the app uses HTTPS (standard exemption applies)
- ❌ DO NOT submit without testing the specific build being uploaded (not a previous build)
- ❌ DO NOT forget to set the release method (manual vs automatic vs phased)
- ✅ DO provide demo credentials in the Review Notes field
- ✅ DO explain any non-obvious features in Review Notes
- ✅ DO verify the privacy policy URL is live and accessible from outside your network
- ✅ DO double-check that the correct build number is selected in App Store Connect
- ✅ DO confirm the version string matches what users will see

## Section 1: App Store Connect - App Information

```
APP INFORMATION TAB:
[ ] App Name: Final, correct, 30 characters max
    Value: "________________________________" (___/30 chars)
[ ] Subtitle: Final, correct, 30 characters max
    Value: "________________________________" (___/30 chars)
[ ] Primary Language: Correctly set
[ ] Category: Primary category selected
[ ] Secondary Category: Selected if applicable
[ ] Content Rights: "Does this app contain, show, or access third-party content?" answered correctly
[ ] Age Rating: Questionnaire completed (see Section 4 below)
```

## Section 2: App Store Connect - Pricing and Availability

```
PRICING AND AVAILABILITY:
[ ] Price: Set correctly (free, paid, or custom pricing)
[ ] Availability: All intended countries/regions selected
[ ] Pre-Order: Configured if using pre-order (otherwise disabled)
[ ] Volume Purchase Program: Enabled if targeting education/enterprise
[ ] Release Method:
    [ ] Manually release this version (you control when it goes live)
    [ ] Automatically release after App Review (goes live upon approval)
    [ ] Automatically release using phased release (1% to 100% over 7 days)
[ ] Phased Release: Enabled if gradual rollout desired (see ios_testflight_rollout.md)
```

## Section 3: App Store Connect - Version Information

```
VERSION INFORMATION:
[ ] Version: Matches CFBundleShortVersionString in Info.plist
    Value: "________"
[ ] Build: Correct build selected from uploaded builds
    Value: "________"
[ ] What's New: Updated with release notes for this version
    [ ] Written in user-facing language (not technical jargon)
    [ ] Highlights key new features and bug fixes
    [ ] Under 4,000 characters

SCREENSHOTS AND PREVIEWS:
[ ] iPhone 6.9" screenshots uploaded (required)
[ ] iPhone 6.7" screenshots uploaded (or using 6.9" fallback)
[ ] iPhone 6.5" screenshots uploaded (if supporting older devices)
[ ] iPhone 5.5" screenshots uploaded (if supporting iPhone SE/8)
[ ] iPad 13" screenshots uploaded (if universal app)
[ ] iPad 12.9" screenshots uploaded (if supporting older iPads)
[ ] App Preview videos uploaded (optional but recommended)
[ ] All screenshots show actual app UI, not mockups
[ ] All screenshots match the build being submitted

DESCRIPTION:
[ ] Description is accurate and current (max 4,000 characters)
[ ] No mentions of competing platforms ("also on Android")
[ ] No specific pricing mentioned (varies by region)
[ ] No time-sensitive claims ("new for 2025!")
[ ] Keywords embedded naturally in description

KEYWORDS:
[ ] 100-character keyword field optimized
    Value: "________________________________________..."
[ ] No words duplicated from title or subtitle
[ ] No competitor brand names
[ ] Comma-separated with no spaces after commas

SUPPORT AND MARKETING:
[ ] Support URL: Valid and accessible
    Value: "________________________________"
[ ] Marketing URL: Valid if provided
    Value: "________________________________"
[ ] Privacy Policy URL: Valid, accessible, and comprehensive
    Value: "________________________________"

PROMOTIONAL TEXT (optional, can change without new build):
[ ] Promotional text set if running a campaign
    Value: "________________________________"
```

## Section 4: Age Rating Questionnaire

```
AGE RATING - Answer each question accurately:

[ ] Cartoon or Fantasy Violence: None / Infrequent-Mild / Frequent-Intense
[ ] Realistic Violence: None / Infrequent-Mild / Frequent-Intense
[ ] Prolonged Graphic or Sadistic Violence: None / Infrequent-Mild / Frequent-Intense
[ ] Profanity or Crude Humor: None / Infrequent-Mild / Frequent-Intense
[ ] Mature/Suggestive Themes: None / Infrequent-Mild / Frequent-Intense
[ ] Horror/Fear Themes: None / Infrequent-Mild / Frequent-Intense
[ ] Medical/Treatment Information: None / Infrequent-Mild / Frequent-Intense
[ ] Alcohol, Tobacco, or Drug Use or References: None / Infrequent-Mild / Frequent-Intense
[ ] Simulated Gambling: None / Infrequent-Mild / Frequent-Intense
[ ] Sexual Content and Nudity: None / Infrequent-Mild / Frequent-Intense
[ ] Unrestricted Web Access: Yes / No
[ ] Gambling with Real Currency: Yes / No

Resulting Age Rating: _________ (4+, 9+, 12+, 17+)

VERIFY: Does the resulting age rating match your target audience?
[ ] Yes, the age rating is appropriate
[ ] If targeting children (under 13): No gambling, no unrestricted web, no tracking
```

## Section 5: Export Compliance

```
EXPORT COMPLIANCE:

Question: "Does your app use encryption?"
[ ] Yes → Complete the export compliance documentation below
[ ] No → Only if app does NOT use HTTPS, SSL/TLS, or any encryption at all

If YES, does your app qualify for an exemption?
Most apps using ONLY standard encryption (HTTPS/TLS) qualify for exemption.

[ ] App uses HTTPS/TLS for API communication only → Exempt (select "Yes" to exemption)
[ ] App uses standard iOS encryption APIs (Security.framework) → Exempt
[ ] App implements custom encryption algorithms → May require ERN/CCATS classification
[ ] App uses encryption for local data storage (Core Data encryption, CryptoKit) → Exempt

ITSAppUsesNonExemptEncryption Info.plist key:
[ ] Set to NO if exempt from export compliance documentation
[ ] Set to YES if non-exempt encryption is used (requires annual self-classification)

If non-exempt:
[ ] Self-classification report filed with BIS annually
[ ] ERN (Export Registration Number) on file if required
```

## Section 6: App Review Notes

```
APP REVIEW NOTES:

Contact Information:
[ ] First Name: ________
[ ] Last Name: ________
[ ] Phone Number: ________
[ ] Email Address: ________

Demo Account (if app requires sign-in):
[ ] Username: ________
[ ] Password: ________
[ ] Account has access to all features a reviewer needs to test
[ ] Account is not expired or rate-limited

Notes for Reviewer:
[ ] Special instructions for accessing features
[ ] Explanation of features that require specific conditions (location, time, etc.)
[ ] Any hardware requirements noted
[ ] If app uses location, provide a test location or explain how to trigger location features
[ ] If app uses push notifications, explain how to trigger them for testing
[ ] If app requires Bluetooth/external hardware, explain how to test without it

Attachment (optional):
[ ] Demo video uploaded if the app has complex features
[ ] Maximum file size: 500MB
[ ] Supported formats: .mov, .mp4, .zip (for multiple files)
```

## Section 7: In-App Purchases (if applicable)

```
IN-APP PURCHASE VERIFICATION:
[ ] All IAP products are in "Ready to Submit" or "Approved" status
[ ] Product IDs match what the app code references
[ ] Display names and descriptions are accurate and localized
[ ] Pricing is set correctly for all territories
[ ] Subscription groups are configured correctly
[ ] Introductory offers (free trial, pay-up-front, pay-as-you-go) configured
[ ] Promotional offers configured (if using)
[ ] Subscription grace period enabled (recommended)
[ ] Billing retry enabled for failed renewals (recommended)
[ ] Review screenshot uploaded for each IAP (showing the purchase flow)
[ ] Restore Purchases button is functional and visible in the app
```

## Section 8: Privacy and Legal

```
PRIVACY AND LEGAL:
[ ] Privacy Policy URL is live and publicly accessible
[ ] Privacy nutrition labels completed in App Privacy section
[ ] Privacy labels match PrivacyInfo.xcprivacy manifest
[ ] Data collection disclosures are accurate
[ ] Account deletion is available if account creation is offered
[ ] "Sign in with Apple" offered if third-party social login exists
[ ] All required usage description strings present in Info.plist
[ ] Third-party SDK privacy manifests are included
```

## Section 9: Final Binary Validation

```
BINARY VALIDATION:
[ ] Archive builds without errors or warnings in Release configuration
[ ] Xcode Organizer validation passes (Distribute App → Validate)
[ ] No missing required architectures
[ ] No unsupported architecture slices (i386/x86_64 for simulator)
[ ] Minimum deployment target matches App Store Connect configuration
[ ] App icon is present for all required sizes
[ ] Launch storyboard displays correctly on all supported devices
[ ] Binary size is acceptable (check App Thinning report)

Command-line validation:
xcrun altool --validate-app -f YourApp.ipa -t ios \
  -u "apple-id@example.com" -p "@keychain:AC_PASSWORD"
```

## Section 10: Final Smoke Test

```
SMOKE TEST (on the exact build being submitted):
[ ] App launches successfully on oldest supported device
[ ] App launches successfully on newest supported device
[ ] Core user flow #1 completes without crash: ________________
[ ] Core user flow #2 completes without crash: ________________
[ ] Core user flow #3 completes without crash: ________________
[ ] Login/signup works with the demo account provided to Apple
[ ] In-app purchase flow completes (sandbox testing)
[ ] Push notifications received and handled correctly
[ ] Deep links and universal links work
[ ] App functions in airplane mode (if applicable)
[ ] VoiceOver accessibility works on key screens
```

## Expected Output

After completing this prompt, you will have:

1. Every App Store Connect field verified and finalized
2. Export compliance accurately declared
3. Age rating correctly determined
4. Review notes with demo credentials and special instructions
5. Binary validated and smoke-tested
6. Confidence to click "Submit for Review"

## Example Interaction

**User:** I'm about to submit v2.5.0 (build 87) of my finance app. It uses HTTPS, has subscriptions, and requires Face ID. First submission since we added account deletion.

**Assistant:** Here's your pre-submission checklist focused on your specifics:

**Export Compliance:** HTTPS only means you qualify for exemption. Set `ITSAppUsesNonExemptEncryption = NO` in Info.plist.

**Subscriptions:** Verify all IAP products show "Ready to Submit" in App Store Connect. Check that the subscription management screen and Restore Purchases button are functional.

**Face ID:** Confirm `NSFaceIDUsageDescription` is in Info.plist with a clear explanation like "AppName uses Face ID to securely access your financial data."

**Account Deletion:** Since this is newly added, mention it in the Review Notes: "Account deletion is available in Settings > Account > Delete Account. This will remove all user data within 14 days."

**Age Rating:** Finance app with no gambling or mature content should result in 4+ rating.

Let me walk through each section...

## Techniques Used

| Technique | Application |
|-----------|-------------|
| ST-01 (Structured Task Decomposition) | Ten-section comprehensive checklist |
| RT-02 (Checklist Verification) | Every item is a verifiable checkbox |
| RT-05 (Constraint Specification) | Apple's exact field limits and requirements |
| DS-02 (Domain-Specific Terminology) | App Store Connect fields and Apple terminology |
| QA-01 (Quality Assurance Gates) | Each section is a gate before submission |

## Related Prompts

- [ios_release_preparation.md](ios_release_preparation.md) - Technical build preparation (signing, entitlements)
- [ios_app_review_guidelines_check.md](ios_app_review_guidelines_check.md) - Guideline compliance audit
- [ios_privacy_compliance.md](ios_privacy_compliance.md) - Privacy requirements deep dive
- [ios_screenshot_strategy.md](ios_screenshot_strategy.md) - Screenshot and preview design
- [ios_testflight_rollout.md](ios_testflight_rollout.md) - Beta testing before submission

## Customization Guide

- **For first submission:** Pay extra attention to Sections 1, 4, 5, and 6; these are where first-time submissions most often have issues
- **For update submissions:** Focus on Sections 3 (What's New), 7 (new IAPs), and 10 (smoke test of changes)
- **For apps with custom server backends:** Add a section verifying server-side readiness and backward compatibility
- **For apps with feature flags:** Add verification that feature flags are set to production values in the submitted build
- **For enterprise distribution (not App Store):** Remove App Store Connect-specific sections and focus on MDM configuration and provisioning
