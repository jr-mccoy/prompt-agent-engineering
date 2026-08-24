---
title: "iOS App Review Guidelines Check"
category: mobile-development
description: "Comprehensive pre-submission audit against Apple's App Review Guidelines covering metadata, content policies, design compliance, privacy, in-app purchases, and common rejection reasons."
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
  - app-review
  - guidelines
  - rejection
  - compliance
  - metadata
updated: "2026-03-19"
---

# iOS App Review Guidelines Check

**Objective:** Perform a comprehensive pre-submission audit of an iOS app against Apple's App Review Guidelines to prevent rejection. This prompt covers the five main guideline sections (Safety, Performance, Business, Design, Legal), common rejection reasons, and metadata compliance. The goal is to identify and resolve issues before submission, saving days of review cycle time.

**When to Use:** Before every App Store submission, after significant feature changes, when adding new monetization, when expanding content categories, or after receiving a rejection to systematically address all potential issues before resubmission.

**Prompt Type:** Comprehensive (approximately 380 lines)

## Context Gathering

1. What type of app is this (utility, social, game, health, finance, education)?
2. Does the app include in-app purchases or subscriptions?
3. Does the app display user-generated content?
4. Does the app target children or include content that could be restricted?
5. Does the app use any web views or redirect to external web experiences?
6. Has the app been rejected before? If so, what was the rejection reason?
7. Does the app include account creation and sign-in?
8. Does the app access health, financial, or other sensitive data?

## Instructions

### CRITICAL: Verification Requirements

- [ ] All five guideline sections audited with no unresolved issues
- [ ] Metadata (screenshots, description, keywords) accurately represents app functionality
- [ ] All in-app purchase flows comply with Section 3 (Business)
- [ ] Privacy requirements from Section 5 (Legal) are fully addressed
- [ ] Common rejection reasons checklist completed with no flags
- [ ] App functions as described in metadata on all supported devices

### False-Positive Prevention

- ❌ DO NOT assume guideline compliance from previous approvals; guidelines change and reviewers vary
- ❌ DO NOT include placeholder content ("lorem ipsum", test data, "coming soon" features)
- ❌ DO NOT link to external payment methods for digital content (Guideline 3.1.1)
- ❌ DO NOT use private APIs or undocumented entitlements
- ❌ DO NOT reference other platforms ("also available on Android") in screenshots or descriptions
- ❌ DO NOT include hidden features or switches that change app behavior post-review
- ✅ DO test every feature path a reviewer would follow
- ✅ DO provide demo credentials in the App Review Notes field
- ✅ DO explain non-obvious features in the reviewer notes
- ✅ DO ensure the app works fully without a network connection if it claims offline support
- ✅ DO test on the oldest supported device and iOS version

## Section 1: Safety (Guideline 1.x)

```
SAFETY AUDIT:

1.1 Objectionable Content:
[ ] No pornographic, excessively violent, or discriminatory content
[ ] User-generated content has moderation (reporting, blocking, filtering)
[ ] Content ratings in App Store Connect accurately reflect app content
[ ] If app includes mature themes, age rating is set appropriately

1.2 User-Generated Content:
[ ] Content filtering or moderation system in place
[ ] Mechanism to report offensive content and users
[ ] Ability to block abusive users
[ ] Developer contact info accessible for reporting concerns
[ ] Terms of service clearly state content rules

1.3 Kids Category:
[ ] If targeting children: No third-party analytics, advertising, or tracking
[ ] COPPA compliance verified
[ ] No links to external websites or apps without parental gate
[ ] Age-appropriate content only
[ ] Parental gate for any in-app purchases

1.4 Physical Harm:
[ ] Medical apps include appropriate disclaimers
[ ] No encouragement of dangerous activities
[ ] Emergency service features function correctly
[ ] Health data handling follows HealthKit guidelines

1.5 Developer Information:
[ ] Support URL is valid and accessible
[ ] Privacy policy URL is valid and accessible
[ ] Developer name matches the legal entity
```

## Section 2: Performance (Guideline 2.x)

```
PERFORMANCE AUDIT:

2.1 App Completeness:
[ ] No placeholder content or "coming soon" sections
[ ] All features described in metadata are functional
[ ] No broken links or empty screens
[ ] Error states are handled gracefully (no raw error messages or crashes)
[ ] App does not appear to be a demo, trial, or test version

2.2 Beta Testing:
[ ] App is not labeled as "beta" in title, description, or UI
[ ] No TestFlight references in production build

2.3 Accurate Metadata:
[ ] Screenshots show actual app UI on the devices depicted
[ ] Description accurately reflects current functionality
[ ] Category is correct for the app's primary function
[ ] What's New accurately describes changes in this version
[ ] Keywords do not include competitor names or misleading terms
[ ] App name does not include price information

2.4 Hardware Compatibility:
[ ] App runs correctly on all devices listed as supported
[ ] iPad version works properly if listed as universal
[ ] Multitasking (Split View, Slide Over) supported or properly opted out on iPad
[ ] Dynamic Island / notification island handled if relevant
[ ] Camera-required features degrade gracefully on devices without camera

2.5 Software Requirements:
[ ] No use of private APIs (run against Apple's API scanner)
[ ] No deprecated APIs that cause crashes on latest iOS
[ ] No use of non-public URL schemes
[ ] App does not download or execute code (except JavaScript in WebKit)
```

Verify no private API usage:

```bash
# Check for private framework references
grep -rn "UIKit.framework/PrivateHeaders\|_UIApplication\|_NS" --include="*.swift" --include="*.m" YourProject/

# Use Apple's app validation
xcrun altool --validate-app -f YourApp.ipa -t ios -u "email" -p "@keychain:AC_PASSWORD"
```

## Section 3: Business (Guideline 3.x)

```
BUSINESS AUDIT:

3.1 Payments:
[ ] All digital content/services purchased through In-App Purchase (not external links)
[ ] Physical goods/services can use external payment (Stripe, etc.)
[ ] No buttons, links, or calls to action directing to external purchase pages for digital content
[ ] Reader apps (Kindle-like): No in-app purchase button required, but no external links either
[ ] Subscription terms clearly displayed before purchase
[ ] Free tier functionality is meaningful, not just a paywall shell

3.1.1 In-App Purchase:
[ ] All IAP products configured in App Store Connect
[ ] StoreKit 2 or StoreKit 1 implementation handles all purchase states
[ ] Restore Purchases button is present and functional
[ ] Subscription management accessible from within the app
[ ] Introductory offers and promotional offers configured correctly
[ ] Family Sharing enabled where applicable
[ ] Price displayed matches App Store Connect configuration

3.1.2 Subscriptions:
[ ] Clear description of what the subscription provides
[ ] Subscription duration and price visible before purchase
[ ] Auto-renewal clearly disclosed
[ ] Cancellation instructions available or linked
[ ] Free trial duration clearly stated if offered
[ ] What happens when subscription expires is explained
[ ] No dark patterns in subscription UI (pre-selected expensive tier, etc.)

3.2 Other Business Model Issues:
[ ] No bait-and-switch (app doesn't fundamentally change after purchase)
[ ] No manipulative pricing (fake discounts, urgency timers for subscriptions)
[ ] Advertisements clearly distinguishable from app content
[ ] No forced ratings or review prompts (use SKStoreReviewController)
```

## Section 4: Design (Guideline 4.x)

```
DESIGN AUDIT:

4.0 Design Principles:
[ ] App provides value beyond a repackaged website
[ ] App is not a simple RSS feed reader disguised as an app
[ ] App has sufficient functionality to justify being in the App Store

4.1 Copycat Apps:
[ ] App has unique value and is not a clone of an existing app
[ ] UI is not designed to be confused with another well-known app
[ ] App name is not confusingly similar to a popular existing app

4.2 Minimum Functionality:
[ ] App does more than a single web page could accomplish
[ ] App provides a native experience, not just a web view wrapper
[ ] If a web view is core to the app, additional native functionality justifies it

4.3 Spam:
[ ] Not a duplicate of developer's own existing app
[ ] Not a template app with minimal customization

4.5 Apple Sites and Services:
[ ] Proper use of Apple icons and trademarks (uses SF Symbols or official assets)
[ ] Sign in with Apple offered if any third-party social login is available (Guideline 4.8)
[ ] Sign in with Apple button follows Apple's Human Interface Guidelines
[ ] "Sign in with Apple" and other login options given equal visual treatment

4.7 HTML5 Games and Apps:
[ ] HTML5 content (if any) is bundled in the binary, not downloaded
[ ] No remote code execution beyond standard WebKit JavaScript
```

## Section 5: Legal (Guideline 5.x)

```
LEGAL AUDIT:

5.1 Privacy:
[ ] Privacy policy URL provided and accessible
[ ] Privacy nutrition labels completed in App Store Connect
[ ] Data collection matches privacy labels
[ ] PrivacyInfo.xcprivacy manifest included and accurate
[ ] Required reason APIs declared with approved reasons
[ ] Location, camera, contacts, and other permissions have usage descriptions
[ ] Minimum data collected necessary for stated functionality
[ ] Account deletion available if account creation is offered

5.2 Intellectual Property:
[ ] All content is original or properly licensed
[ ] No copyrighted material used without permission
[ ] Third-party content has documented licensing
[ ] Music, images, and fonts are properly licensed

5.3 Gaming, Gambling, and Lotteries:
[ ] If applicable: Complies with local gambling laws
[ ] In-app currency cannot be converted to real currency
[ ] Odds are disclosed for randomized reward mechanisms

5.4 VPN Apps:
[ ] If VPN: Uses NEVPNManager or NetworkExtension
[ ] No data collection beyond what's needed for VPN functionality
[ ] Clear disclosure of VPN functionality

5.6 Developer Code of Conduct:
[ ] No hidden features or kill switches
[ ] No misleading behavior post-review
[ ] App behaves the same in review and production
```

## Common Rejection Reasons Quick Check

```
TOP 10 REJECTION REASONS CHECKLIST:

1. Guideline 2.1 - App Completeness:
   [ ] No crashes, bugs, or broken features
   [ ] All links work, no placeholder content

2. Guideline 2.3.3 - Screenshots:
   [ ] Screenshots show actual app, not mockups
   [ ] No misleading imagery

3. Guideline 4.0 - Design:
   [ ] App provides genuine utility
   [ ] Not a thin wrapper around a website

4. Guideline 2.3.1 - Hidden Features:
   [ ] No undisclosed features
   [ ] All features accessible to reviewer

5. Guideline 3.1.1 - In-App Purchase:
   [ ] Digital content uses IAP
   [ ] No external payment links for digital goods

6. Guideline 5.1.1 - Data Collection:
   [ ] Privacy labels accurate
   [ ] Purpose strings for all permissions

7. Guideline 4.8 - Sign in with Apple:
   [ ] Offered if third-party social login exists

8. Guideline 5.1.2 - Data Use and Sharing:
   [ ] No unauthorized data sharing
   [ ] User consent for data collection

9. Guideline 2.5.1 - Software Requirements:
   [ ] No private API usage
   [ ] Only approved APIs and frameworks

10. Guideline 1.2 - User Generated Content:
    [ ] Moderation system in place
    [ ] Reporting mechanism available
```

## App Store Connect Metadata Checklist

```
METADATA VALIDATION:
[ ] App name: 30 characters max, no keyword stuffing
[ ] Subtitle: 30 characters max, unique from title
[ ] Description: Accurate, no competitor mentions, no prices
[ ] Keywords: 100 characters, no duplicates with title/subtitle
[ ] What's New: Updated for this version
[ ] Promotional Text: Optional, can be updated without new build
[ ] Support URL: Valid and accessible
[ ] Marketing URL: Valid if provided
[ ] Privacy Policy URL: Valid, accessible, comprehensive
[ ] Category: Primary and secondary correctly set
[ ] Age Rating: Questionnaire answered accurately
[ ] Screenshots: Correct device sizes, actual app UI
[ ] App Preview: Under 30 seconds, actual app footage
[ ] Copyright: Current year, correct entity
[ ] Contact Information: Valid for review team communication
[ ] Review Notes: Demo credentials, special instructions
```

## Expected Output

After completing this prompt, you will have:

1. A complete audit across all five App Review Guideline sections
2. A metadata validation confirming App Store Connect is correctly configured
3. A list of any compliance issues found with remediation steps
4. Confidence that common rejection reasons have been proactively addressed

## Example Interaction

**User:** My social fitness app has subscriptions, user-generated workout posts, and Sign in with Apple alongside Google Sign-In. We got rejected last time for Guideline 2.1.

**Assistant:** Given your previous 2.1 rejection (App Completeness), let me prioritize that section first, then audit the areas specific to your app:

**Priority 1 - Guideline 2.1 (previous rejection):**
- Walk through every screen and feature. Document any that crash, show errors, or are incomplete.
- Verify the reviewer can access all features with the demo credentials you provide.
- Test on the oldest supported device at the minimum iOS version.

**Priority 2 - Guideline 1.2 (UGC):**
- Your workout posts need: content reporting, user blocking, and content moderation.
- Terms of service must define acceptable content.

**Priority 3 - Guideline 3.1 (Subscriptions):**
- Subscription terms visible before purchase, auto-renewal disclosure, restore button present.

**Priority 4 - Guideline 4.8 (Sign in with Apple):**
- Since you offer Google Sign-In, Sign in with Apple must be offered with equal prominence.

## Techniques Used

| Technique | Application |
|-----------|-------------|
| ST-01 (Structured Task Decomposition) | Five guideline sections audited systematically |
| RT-02 (Checklist Verification) | Actionable checklists for each guideline section |
| RT-05 (Constraint Specification) | Apple's specific constraints and requirements |
| DS-02 (Domain-Specific Terminology) | Apple guideline numbers, review terminology |
| QA-01 (Quality Assurance Gates) | Each section is a gate before submission |

## Related Prompts

- [ios_pre_submission_checklist.md](ios_pre_submission_checklist.md) - Technical checklist complementing this guideline audit
- [ios_privacy_compliance.md](ios_privacy_compliance.md) - Deep dive into Section 5.1 privacy requirements
- [ios_release_preparation.md](ios_release_preparation.md) - Technical preparation for submission
- [ios_app_store_review_response.md](ios_app_store_review_response.md) - Handling user reviews after approval

## Customization Guide

- **For game apps:** Expand Section 3 for virtual currency, loot boxes (must disclose odds), and gambling-adjacent mechanics
- **For health apps:** Expand Section 1.4 with medical disclaimer requirements and HealthKit compliance
- **For financial apps:** Add Section 5 financial data protections and regulatory compliance
- **For kids apps:** Replace standard audit with Kids Category-specific checklist (COPPA, no tracking, parental gates)
- **For apps with external web views:** Expand Section 4.2 to address web view vs. native functionality requirements
- **For resubmission after rejection:** Start with the specific rejection guideline, resolve it, then audit adjacent guidelines that reviewers commonly check together
