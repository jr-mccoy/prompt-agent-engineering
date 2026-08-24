---
name: android_monetization_setup
description: Orchestrate complete Android monetization implementation including Google Play Billing, subscriptions, AdMob, paywalls, server-side verification, and policy compliance
version: "1.0.0"
category: mobile-development
tags: [admob, android, billing, compose, firebase, kotlin, monetization, subscriptions]
agents_used: [android-monetization-architect, android-release-manager, mobile-developer, security-auditor, test-automator]
---

Orchestrate the implementation of a complete Android monetization layer including billing, subscriptions, ads, and paywalls. Coordinates specialized agents across 4 phases to deliver a production-ready monetization system:

[Extended thinking: Monetization implementation touches multiple architectural layers simultaneously: the billing layer (Google Play Billing Library), the ad layer (AdMob), the verification layer (Cloud Functions), the entitlement layer (Firestore + Room), and the UI layer (Compose paywalls, ad placements). This workflow sequences these dependencies correctly: architecture first, then parallel implementation of billing + ads + backend, then integration (paywall UI, ad suppression), and finally testing + compliance. The key insight is that billing and ads must share an entitlement system — subscribers don't see ads.]

## Phase 1: Architecture and Planning

### 1. Monetization Architecture Design
- Use Task tool with subagent_type="android-monetization-architect"
- Prompt: "Design the monetization architecture for the Android app at $ARGUMENTS. The app needs:
  - Subscription tiers (free, premium monthly, premium annual)
  - AdMob ads for free users (banner, interstitial at natural break points, rewarded for bonus features)
  - Ad suppression for premium subscribers
  - Server-side purchase verification via Firebase Cloud Functions
  - Entitlement system shared between billing and ad layers

  Deliver:
  1. Entitlement data model (what's stored in Firestore vs Room)
  2. BillingClient integration architecture (Hilt modules, repository pattern)
  3. AdMob initialization flow with consent management
  4. Ad suppression architecture (how entitlements gate ad display)
  5. Cloud Functions needed (receipt verification, RTDN handler, subscription status check)
  6. Data flow diagram showing: User → BillingClient → Cloud Function → Firestore → Room → UI
  7. Product configuration plan for Play Console (product IDs, pricing, offer structure)"
- Expected output: Architecture document with data models, component diagram, and Cloud Functions spec
- Context: App uses Kotlin, Jetpack Compose, Hilt, Room, Firebase (RTDB + Firestore + Cloud Functions)

## Phase 2: Parallel Implementation

### 2. Google Play Billing Implementation
- Use Task tool with subagent_type="mobile-developer"
- Prompt: "Implement Google Play Billing for the Android app at $ARGUMENTS using the architecture from Phase 1. Build:

  **Hilt Modules:**
  - BillingModule providing singleton BillingClient
  - BillingClient connection manager with retry logic

  **Repository Layer:**
  - BillingRepository with: queryProducts(), launchPurchaseFlow(), queryExistingPurchases(), acknowledgePurchase()
  - PurchasesUpdatedListener implementation
  - Pending purchase handling

  **Entitlement Manager:**
  - EntitlementManager observing Firestore subscription document
  - Local Room cache for offline entitlement access
  - isPremium Flow for UI observation

  Use the android-play-billing-subscriptions skill for implementation patterns. Follow the subscription state machine for handling all states (active, grace period, on-hold, paused, cancelled, expired)."
- Expected output: Kotlin implementation files for billing layer
- Context: Architecture from step 1, existing Hilt/Room/Firebase setup

### 3. AdMob Integration
- Use Task tool with subagent_type="mobile-developer"
- Prompt: "Implement AdMob for the Android app at $ARGUMENTS using the architecture from Phase 1. Build:

  **Consent Management:**
  - ConsentManager using UMP SDK
  - Consent flow before any ad loading
  - Debug geography settings for testing

  **Ad Manager:**
  - AdManager singleton coordinating consent + entitlement checks
  - shouldShowAds Flow combining subscription state and consent status
  - Banner ad Compose wrapper component
  - Interstitial ad preloader with frequency capping
  - Rewarded ad manager for gamification bonus features

  **Ad Placement:**
  - Configure ad placements per screen (see android-admob-mediation skill ad format decision tree)
  - Implement frequency capping (max 1 interstitial per 5 min)

  Use the android-admob-mediation skill for implementation patterns. Use TEST ad unit IDs in all code (production IDs via BuildConfig)."
- Expected output: Kotlin implementation files for ad layer
- Context: Architecture from step 1, existing Compose UI, gamification features

### 4. Server-Side Verification (Cloud Functions)
- Use Task tool with subagent_type="mobile-developer"
- Prompt: "Implement Firebase Cloud Functions for purchase verification and subscription management for the app at $ARGUMENTS. Build:

  **verifyPurchase (HTTPS Callable):**
  - Accepts purchaseToken, productId, productType from client
  - Validates with Google Play Developer API
  - Stores subscription state in Firestore `subscriptions/{userId}`
  - Returns verification result to client

  **handleSubscriptionNotification (Pub/Sub):**
  - Receives Real-time Developer Notifications from Play Billing
  - Fetches latest subscription state from Play Developer API
  - Updates Firestore subscription document
  - Handles all notification types (renewed, cancelled, grace_period, on_hold, expired, revoked)

  **getSubscriptionStatus (HTTPS Callable):**
  - Returns current subscription status from Firestore
  - Refreshes from Play API if stale (>1 hour)

  All functions must verify `context.auth` before processing. Use TypeScript with proper error handling."
- Expected output: Cloud Functions TypeScript implementation
- Context: Existing Firebase project with Cloud Functions deployment

### CONVERGENCE: Steps 2-4 must complete before Phase 3

## Phase 3: Integration and UI

### 5. Paywall UI Implementation
- Use Task tool with subagent_type="mobile-developer"
- Prompt: "Build the paywall and subscription management UI in Jetpack Compose for the app at $ARGUMENTS. Implement:

  **Paywall Screen:**
  - Feature comparison between free and premium tiers
  - Subscription option cards (monthly, annual with savings badge)
  - Trial offer display (if available from ProductDetails)
  - 'Restore Purchases' button
  - Legal disclosure text (auto-renewal terms — required by Play Store)
  - Loading and error states

  **Subscription Management:**
  - Current subscription status display
  - Link to Play Store subscription management
  - Upgrade/downgrade flow between tiers

  **Premium Feature Gates:**
  - Composable wrapper that checks entitlement and shows paywall
  - Premium badge on gated features
  - Upgrade CTA on free tier

  **Ad Integration Points:**
  - Conditional banner placement (hidden for premium)
  - Interstitial trigger points at natural breaks
  - Rewarded ad entry points in gamification

  Follow Material Design 3 patterns. Reference the billing and ad implementations from Phase 2."
- Expected output: Compose UI implementation for paywall and monetization touchpoints
- Context: Existing Compose navigation, Material 3 theme, billing + ad managers from Phase 2

### 6. Entitlement Integration Testing
- Use Task tool with subagent_type="test-automator"
- Prompt: "Create comprehensive tests for the monetization layer of the Android app at $ARGUMENTS. Cover:

  **Unit Tests:**
  - EntitlementManager: isPremium returns correct state for each subscription state
  - PurchaseUpdateHandler: processes purchases correctly, handles errors
  - AdManager: shouldShowAds returns false for premium, true for free with consent
  - Frequency capping: interstitials respect timing limits

  **Integration Tests:**
  - BillingClient → Cloud Function → Firestore → Room → UI entitlement flow
  - Ad suppression activates immediately on subscription purchase
  - Subscription expiry removes premium access and shows ads
  - Restore purchases recovers entitlement from Firestore
  - Offline entitlement works from Room cache

  **Edge Cases:**
  - Purchase succeeds but verification fails → no entitlement granted
  - Network loss during purchase → pending purchase handled
  - Grace period → premium access maintained, update payment shown
  - Concurrent purchase from multiple devices → idempotent processing

  Use MockK for mocking, JUnit5 for test framework, Turbine for Flow testing."
- Expected output: Test suite covering monetization layer
- Context: Billing, ad, and entitlement implementations from Phases 2-3

## Phase 4: Compliance and Verification

### 7. Security Review of Monetization
- Use Task tool with subagent_type="security-auditor"
- Prompt: "Review the monetization implementation security for the Android app at $ARGUMENTS. Verify:
  - All purchases validated server-side (no client-only entitlement granting)
  - Cloud Functions verify auth context before processing
  - No way to bypass paywall by modifying Room database
  - Purchase tokens cannot be replayed
  - Ad unit IDs not hardcoded (use BuildConfig)
  - Consent data handled per GDPR requirements
  - No PII logged in billing or ad event tracking
  Report any path where a user could gain premium access without payment."
- Expected output: Monetization security assessment

### 8. Play Store Monetization Policy Compliance
- Use Task tool with subagent_type="android-release-manager"
- Prompt: "Review monetization implementation for Play Store policy compliance at $ARGUMENTS. Verify:
  - Auto-renewal disclosure appears before purchase
  - Subscription terms clearly stated (price, period, renewal terms)
  - Cancellation instructions easily discoverable
  - Free trial duration and post-trial pricing clearly communicated
  - No misleading pricing (e.g., showing monthly price for annual plan)
  - Refund policy linked in the app
  - Data Safety Declaration updated with billing data collection
  - Ad implementation follows Play ad policy (no accidental clicks, no deceptive ads)
  Provide pass/fail for each policy requirement with specific fixes for failures."
- Expected output: Policy compliance checklist with pass/fail
- Context: Full monetization implementation from Phases 2-3

## Configuration Options

- `--skip-ads`: Implement billing only, no AdMob
- `--skip-billing`: Implement AdMob only, no billing
- `--tiers [free,premium|free,basic,premium]`: Specify subscription tier structure
- `--trial-days [N]`: Include free trial in subscription offers
- `--existing-billing`: Skip billing implementation, only add AdMob integration

## Success Criteria

- BillingClient connects, queries products, and processes purchases
- Server-side verification validates every purchase before granting entitlement
- RTDN handler processes all subscription state change types
- Paywall displays products with correct pricing from Play Console
- Ads display for free users and suppress for premium users
- Consent form shows in applicable regions before ad loading
- All monetization tests pass
- Play Store monetization policies met
- No security vulnerabilities in payment flow

## Coordination Notes

- Phase 2 tasks are independent and should run in parallel
- Phase 3 depends on all Phase 2 implementations
- Phase 4 reviews the complete integrated system
- Play Console product configuration must happen manually (not automatable)
- RTDN setup requires manual Pub/Sub topic configuration in Play Console
- Use test ad unit IDs throughout development — switch to production only for release builds

Target app: $ARGUMENTS
