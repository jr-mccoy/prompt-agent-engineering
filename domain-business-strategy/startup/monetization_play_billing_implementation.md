---
title: "Google Play Billing Implementation"
category: startup/monetization
description: "Implement Google Play Billing Library 7.x in an Android app — BillingClient setup, subscription purchase flow, acknowledge and consume, grace period handling, account hold, billing retry, proration modes, server-side receipt validation, and refund handling for solo developers"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
difficulty: advanced
tags:
  - monetization
  - android
  - play-billing
  - billing-library
  - subscriptions
  - iap
  - kotlin
  - server-validation
  - solo-developer
updated: "2026-02-11"
---

# Google Play Billing Implementation

**Objective:** Implement Google Play Billing Library 7.x in an Android app — including BillingClient initialization and connection management, subscription and one-time purchase flows, purchase acknowledgment and consumption, grace period handling (3-7 days), account hold (up to 30 days), automatic billing retry, proration modes for subscription upgrades and downgrades, server-side receipt validation using the Google Play Developer API, and refund detection — so that your billing code is reliable, handles every edge case, and does not lose revenue or create bad user experiences.

**When to Use:** Use this after you have designed your subscription tiers (see `monetization_subscription_design.md`) and set your pricing (see `monetization_pricing_strategy.md`). This prompt covers the Kotlin implementation of the billing system. Do not start coding billing without reading this — the Google Play Billing Library has numerous edge cases that are poorly documented, and missing even one (like failing to acknowledge a purchase) causes automatic refunds after 3 days.

**Prerequisites:**
- Google Play Console account with your app published (at least internal testing track)
- Subscription or in-app product configured in Play Console under "Monetization > Products"
- Play Billing Library 7.x added to your project
- Minimum API level 21 (Android 5.0+)

---

## Context Gathering

Before implementing billing, gather essential context:

1. **Product Configuration:**
   - "What subscription plans have you configured in Google Play Console (product IDs, base plan IDs, offer IDs)?"
   - "What one-time in-app products have you configured (product IDs, type: consumable or non-consumable)?"
   - "Have you set up test accounts in Play Console for license testing?"
   - "Are you using test tracks (internal, closed, open) for billing testing?"

2. **Architecture:**
   - "Are you using a ViewModel/Repository pattern or a simpler architecture?"
   - "Do you have a backend server, or is this a client-only app?"
   - "Are you using Room or another local database for caching entitlements?"
   - "What dependency injection framework are you using (Hilt, Koin, manual)?"

3. **Subscription Lifecycle:**
   - "How many subscription tiers do you have (1, 2, 3)?"
   - "Do you support upgrades and downgrades between tiers?"
   - "What grace period length have you configured (3, 7, 14 days)?"
   - "Have you enabled account hold in Play Console?"

4. **Existing State:**
   - "Is this a new integration or are you migrating from an older Billing Library version?"
   - "Do you have existing subscribers whose entitlements must be preserved?"
   - "Are you using any third-party billing abstraction (RevenueCat, Qonversion)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before implementing ANY billing code, you MUST:**

1. **Verify products exist in Play Console** — BillingClient.queryProductDetails() returns empty results if products are not configured or your app version does not match the uploaded APK/AAB. Always configure products and upload at least one build to any test track before testing.
2. **Verify acknowledgment is implemented** — Google automatically refunds any purchase that is not acknowledged within 3 days. This is the single most common billing bug. Every purchase flow must end with acknowledgment.
3. **Verify you handle BillingClient disconnection** — The BillingClient connection can drop at any time (process death, network change, Google Play Services update). Your code must detect disconnection and reconnect before every billing operation.
4. **Verify you handle all purchase states** — A purchase can be in PURCHASED, PENDING, or UNSPECIFIED_STATE. Pending purchases (e.g., cash-based payments in some countries) must not grant entitlements until confirmed.
5. **Verify you test with license testers** — Real purchases in production cannot be tested without real charges. Configure license testers in Play Console (Settings > License testing) who can make test purchases for free.
6. **Acceptable null result** — If your app does not yet have a published build on any test track, billing testing is not possible. It is valid to write the billing code, prepare test accounts, and defer testing until the first build is uploaded.

### False-Positive Prevention

- Do NOT grant entitlements before acknowledging the purchase — if acknowledgment fails, the user has access but the purchase will be refunded in 3 days
- Do NOT cache entitlements only in memory — process death will lose the state. Use Room or SharedPreferences as a local cache, and always re-verify with BillingClient on app start
- Do NOT assume BillingClient is always connected — check connection state before every operation and reconnect if needed
- Do NOT ignore the PENDING purchase state — in some markets, users pay with cash at convenience stores, and the purchase is not confirmed until payment is received (hours or days later)
- Do NOT hardcode product IDs as strings throughout the codebase — use a centralized constants object
- Do NOT skip server-side validation if you have a backend — client-side billing is trivially spoofable with modified APKs
- DO acknowledge every purchase within seconds of receiving it
- DO implement retry logic for acknowledgment failures (network issues can cause transient failures)
- DO re-query purchases on every app start to catch purchases made on other devices or subscription state changes
- DO handle all BillingResponseCode values, especially SERVICE_DISCONNECTED and BILLING_UNAVAILABLE
- DO test every flow: new purchase, renewal, grace period, account hold, cancellation, refund, and upgrade/downgrade

---

### Phase 1: BillingClient Setup

#### 1.1 Dependencies

```kotlin
// build.gradle.kts (app-level)
dependencies {
    // Google Play Billing Library 7.x
    implementation("com.android.billingclient:billing-ktx:7.1.1")

    // For server-side validation (if using a backend)
    implementation("com.google.apis:google-api-services-androidpublisher:v3-rev20241203-2.0.0")
}
```

#### 1.2 Product ID Constants

```kotlin
// billing/BillingConstants.kt
object BillingConstants {
    // Subscription product IDs (must match Google Play Console exactly)
    const val PRODUCT_ID_PREMIUM = "premium_subscription"

    // Base plan IDs
    const val BASE_PLAN_MONTHLY = "monthly"
    const val BASE_PLAN_ANNUAL = "annual"

    // Offer IDs (optional — for introductory pricing, free trials)
    const val OFFER_FREE_TRIAL = "free-trial-7d"
    const val OFFER_INTRO_PRICE = "intro-50pct-off"

    // One-time purchase product IDs
    const val PRODUCT_ID_REMOVE_ADS = "remove_ads"
    const val PRODUCT_ID_COIN_PACK_100 = "coin_pack_100"

    // Product types
    val SUBSCRIPTION_PRODUCTS = listOf(PRODUCT_ID_PREMIUM)
    val INAPP_PRODUCTS = listOf(PRODUCT_ID_REMOVE_ADS, PRODUCT_ID_COIN_PACK_100)
}
```

#### 1.3 BillingClient Wrapper

```kotlin
// billing/BillingClientWrapper.kt
class BillingClientWrapper(
    private val context: Context,
    private val onPurchaseUpdated: (List<Purchase>) -> Unit
) {
    private var billingClient: BillingClient? = null
    private var isConnected = false
    private val connectionRetryPolicy = ConnectionRetryPolicy()

    // Initialize and connect
    fun initialize() {
        billingClient = BillingClient.newBuilder(context)
            .setListener { billingResult, purchases ->
                handlePurchaseUpdated(billingResult, purchases)
            }
            .enablePendingPurchases(
                PendingPurchasesParams.newBuilder()
                    .enableOneTimeProducts()
                    .enablePrepaidPlans()
                    .build()
            )
            .build()

        connect()
    }

    private fun connect() {
        billingClient?.startConnection(object : BillingClientStateListener {
            override fun onBillingSetupFinished(billingResult: BillingResult) {
                if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
                    isConnected = true
                    connectionRetryPolicy.reset()
                    Log.d("Billing", "BillingClient connected")
                } else {
                    isConnected = false
                    Log.e("Billing", "Connection failed: ${billingResult.debugMessage}")
                }
            }

            override fun onBillingServiceDisconnected() {
                isConnected = false
                Log.w("Billing", "BillingClient disconnected, retrying...")
                connectionRetryPolicy.retry { connect() }
            }
        })
    }

    // Ensure connected before any operation
    suspend fun ensureConnected(): Boolean {
        if (isConnected && billingClient?.isReady == true) return true

        return suspendCancellableCoroutine { continuation ->
            billingClient?.startConnection(object : BillingClientStateListener {
                override fun onBillingSetupFinished(billingResult: BillingResult) {
                    isConnected = billingResult.responseCode ==
                        BillingClient.BillingResponseCode.OK
                    continuation.resume(isConnected) {}
                }
                override fun onBillingServiceDisconnected() {
                    isConnected = false
                    if (continuation.isActive) continuation.resume(false) {}
                }
            })
        }
    }

    private fun handlePurchaseUpdated(
        billingResult: BillingResult,
        purchases: List<Purchase>?
    ) {
        when (billingResult.responseCode) {
            BillingClient.BillingResponseCode.OK -> {
                purchases?.let { onPurchaseUpdated(it) }
            }
            BillingClient.BillingResponseCode.USER_CANCELED -> {
                Log.d("Billing", "User canceled purchase")
            }
            BillingClient.BillingResponseCode.ITEM_ALREADY_OWNED -> {
                Log.d("Billing", "Item already owned — re-query purchases")
                // User already owns this — refresh entitlements
            }
            else -> {
                Log.e("Billing", "Purchase error: ${billingResult.responseCode} " +
                    "- ${billingResult.debugMessage}")
            }
        }
    }

    fun getClient(): BillingClient? = billingClient

    fun destroy() {
        billingClient?.endConnection()
        billingClient = null
        isConnected = false
    }
}

// Connection retry with exponential backoff
class ConnectionRetryPolicy(
    private val maxRetries: Int = 5,
    private val baseDelayMs: Long = 1000
) {
    private var retryCount = 0
    private val handler = Handler(Looper.getMainLooper())

    fun retry(action: () -> Unit) {
        if (retryCount >= maxRetries) {
            Log.e("Billing", "Max retries ($maxRetries) exceeded")
            return
        }
        val delay = baseDelayMs * (1L shl retryCount.coerceAtMost(5))
        retryCount++
        handler.postDelayed(action, delay)
    }

    fun reset() { retryCount = 0 }
}
```

---

### Phase 2: Purchase Flow

#### 2.1 Query Available Products

```kotlin
// billing/BillingRepository.kt
class BillingRepository(
    private val billingWrapper: BillingClientWrapper
) {
    // Query subscription product details
    suspend fun querySubscriptionProducts(): List<ProductDetails> {
        if (!billingWrapper.ensureConnected()) return emptyList()

        val productList = BillingConstants.SUBSCRIPTION_PRODUCTS.map { productId ->
            QueryProductDetailsParams.Product.newBuilder()
                .setProductId(productId)
                .setProductType(BillingClient.ProductType.SUBS)
                .build()
        }

        val params = QueryProductDetailsParams.newBuilder()
            .setProductList(productList)
            .build()

        val result = billingWrapper.getClient()!!.queryProductDetails(params)
        return if (result.billingResult.responseCode ==
            BillingClient.BillingResponseCode.OK) {
            result.productDetailsList ?: emptyList()
        } else {
            Log.e("Billing", "Query failed: ${result.billingResult.debugMessage}")
            emptyList()
        }
    }

    // Extract pricing information for display
    fun getSubscriptionOffers(
        productDetails: ProductDetails
    ): List<SubscriptionOffer> {
        return productDetails.subscriptionOfferDetails?.map { offerDetails ->
            val pricingPhases = offerDetails.pricingPhases.pricingPhaseList
            val basePlanPrice = pricingPhases.last() // Last phase is the recurring price
            val trialPhase = pricingPhases.firstOrNull {
                it.priceAmountMicros == 0L
            }
            val introPhase = pricingPhases.firstOrNull {
                it.priceAmountMicros > 0L && it != basePlanPrice
            }

            SubscriptionOffer(
                basePlanId = offerDetails.basePlanId,
                offerId = offerDetails.offerId,
                offerToken = offerDetails.offerToken,
                monthlyPrice = basePlanPrice.formattedPrice,
                monthlyPriceMicros = basePlanPrice.priceAmountMicros,
                billingPeriod = basePlanPrice.billingPeriod, // "P1M" or "P1Y"
                hasFreeTrial = trialPhase != null,
                trialDays = trialPhase?.billingPeriod?.let {
                    parseBillingPeriodDays(it)
                } ?: 0,
                introPrice = introPhase?.formattedPrice,
                introPeriods = introPhase?.billingCycleCount ?: 0
            )
        } ?: emptyList()
    }

    private fun parseBillingPeriodDays(period: String): Int {
        // ISO 8601 duration: P3D = 3 days, P1W = 7 days, P1M = 30 days
        return when {
            period.endsWith("D") -> period.filter { it.isDigit() }.toIntOrNull() ?: 0
            period.endsWith("W") -> (period.filter { it.isDigit() }.toIntOrNull() ?: 0) * 7
            period.endsWith("M") -> (period.filter { it.isDigit() }.toIntOrNull() ?: 0) * 30
            else -> 0
        }
    }
}

data class SubscriptionOffer(
    val basePlanId: String,
    val offerId: String?,
    val offerToken: String,
    val monthlyPrice: String,
    val monthlyPriceMicros: Long,
    val billingPeriod: String,
    val hasFreeTrial: Boolean,
    val trialDays: Int,
    val introPrice: String?,
    val introPeriods: Int
)
```

#### 2.2 Launch Purchase Flow

```kotlin
// billing/BillingRepository.kt (continued)

    // Launch subscription purchase
    fun launchSubscriptionPurchase(
        activity: Activity,
        productDetails: ProductDetails,
        offerToken: String,
        oldPurchaseToken: String? = null, // For upgrades/downgrades
        prorationMode: Int? = null        // Proration mode for changes
    ): BillingResult {
        val productDetailsParams = BillingFlowParams.ProductDetailsParams
            .newBuilder()
            .setProductDetails(productDetails)
            .setOfferToken(offerToken)
            .build()

        val billingFlowParamsBuilder = BillingFlowParams.newBuilder()
            .setProductDetailsParamsList(listOf(productDetailsParams))

        // For upgrades/downgrades
        if (oldPurchaseToken != null && prorationMode != null) {
            billingFlowParamsBuilder.setSubscriptionUpdateParams(
                BillingFlowParams.SubscriptionUpdateParams.newBuilder()
                    .setOldPurchaseToken(oldPurchaseToken)
                    .setSubscriptionReplacementMode(prorationMode)
                    .build()
            )
        }

        return billingWrapper.getClient()!!.launchBillingFlow(
            activity,
            billingFlowParamsBuilder.build()
        )
    }

    // Launch one-time product purchase
    fun launchOneTimePurchase(
        activity: Activity,
        productDetails: ProductDetails
    ): BillingResult {
        val productDetailsParams = BillingFlowParams.ProductDetailsParams
            .newBuilder()
            .setProductDetails(productDetails)
            .build()

        val billingFlowParams = BillingFlowParams.newBuilder()
            .setProductDetailsParamsList(listOf(productDetailsParams))
            .build()

        return billingWrapper.getClient()!!.launchBillingFlow(
            activity,
            billingFlowParams
        )
    }
```

#### 2.3 Handle Purchase Result and Acknowledge

```kotlin
// billing/PurchaseHandler.kt
class PurchaseHandler(
    private val billingWrapper: BillingClientWrapper,
    private val entitlementRepository: EntitlementRepository,
    private val serverValidator: ServerValidator? = null // Optional server validation
) {
    // Called from BillingClientWrapper.onPurchaseUpdated
    suspend fun handlePurchases(purchases: List<Purchase>) {
        for (purchase in purchases) {
            when (purchase.purchaseState) {
                Purchase.PurchaseState.PURCHASED -> {
                    handleCompletedPurchase(purchase)
                }
                Purchase.PurchaseState.PENDING -> {
                    handlePendingPurchase(purchase)
                }
                else -> {
                    Log.w("Billing", "Unknown purchase state: ${purchase.purchaseState}")
                }
            }
        }
    }

    private suspend fun handleCompletedPurchase(purchase: Purchase) {
        // Step 1: Validate server-side (if you have a backend)
        if (serverValidator != null) {
            val isValid = serverValidator.validatePurchase(
                purchaseToken = purchase.purchaseToken,
                productId = purchase.products.first(),
                isSubscription = purchase.products.first() in
                    BillingConstants.SUBSCRIPTION_PRODUCTS
            )
            if (!isValid) {
                Log.e("Billing", "Server validation failed for ${purchase.orderId}")
                return // Do not grant entitlement for invalid purchases
            }
        }

        // Step 2: Grant entitlement locally
        entitlementRepository.grantEntitlement(
            productId = purchase.products.first(),
            purchaseToken = purchase.purchaseToken,
            orderId = purchase.orderId ?: ""
        )

        // Step 3: Acknowledge the purchase (CRITICAL — must be done within 3 days)
        if (!purchase.isAcknowledged) {
            acknowledgePurchase(purchase)
        }
    }

    private suspend fun acknowledgePurchase(purchase: Purchase) {
        val isSubscription = purchase.products.first() in
            BillingConstants.SUBSCRIPTION_PRODUCTS

        if (isSubscription) {
            // Acknowledge subscription
            val params = AcknowledgePurchaseParams.newBuilder()
                .setPurchaseToken(purchase.purchaseToken)
                .build()

            val result = billingWrapper.getClient()!!.acknowledgePurchase(params)
            if (result.responseCode == BillingClient.BillingResponseCode.OK) {
                Log.d("Billing", "Subscription acknowledged: ${purchase.orderId}")
            } else {
                Log.e("Billing", "Acknowledge failed: ${result.debugMessage}")
                // IMPORTANT: Retry acknowledgment — failure here means auto-refund in 3 days
                scheduleAcknowledgmentRetry(purchase)
            }
        } else {
            // For consumable products, consume instead of acknowledge
            val isConsumable = purchase.products.first() ==
                BillingConstants.PRODUCT_ID_COIN_PACK_100

            if (isConsumable) {
                val params = ConsumeParams.newBuilder()
                    .setPurchaseToken(purchase.purchaseToken)
                    .build()

                val result = billingWrapper.getClient()!!.consumePurchase(params)
                if (result.billingResult.responseCode ==
                    BillingClient.BillingResponseCode.OK) {
                    Log.d("Billing", "Consumable consumed: ${purchase.orderId}")
                }
            } else {
                // Non-consumable one-time purchase — acknowledge
                val params = AcknowledgePurchaseParams.newBuilder()
                    .setPurchaseToken(purchase.purchaseToken)
                    .build()

                val result = billingWrapper.getClient()!!.acknowledgePurchase(params)
                if (result.responseCode == BillingClient.BillingResponseCode.OK) {
                    Log.d("Billing", "One-time purchase acknowledged: ${purchase.orderId}")
                }
            }
        }
    }

    private fun handlePendingPurchase(purchase: Purchase) {
        // Pending = payment not yet confirmed (e.g., cash payments in some markets)
        // Do NOT grant entitlement. Show "purchase pending" UI.
        entitlementRepository.markPending(
            productId = purchase.products.first(),
            purchaseToken = purchase.purchaseToken
        )
        Log.d("Billing", "Purchase pending: ${purchase.orderId}")
    }

    private fun scheduleAcknowledgmentRetry(purchase: Purchase) {
        // Use WorkManager for reliable retry
        // Retry 3 times with exponential backoff over 24 hours
        // If all retries fail, log critical error — you have ~2 days before auto-refund
        Log.w("Billing", "Scheduling acknowledgment retry for ${purchase.orderId}")
    }
}
```

---

### Phase 3: Subscription Lifecycle

#### 3.1 Query Current Subscriptions

```kotlin
// billing/BillingRepository.kt (continued)

    // Query all current purchases (call on app start)
    suspend fun queryCurrentPurchases(): List<Purchase> {
        if (!billingWrapper.ensureConnected()) return emptyList()

        val allPurchases = mutableListOf<Purchase>()

        // Query subscriptions
        val subsResult = billingWrapper.getClient()!!.queryPurchasesAsync(
            QueryPurchasesParams.newBuilder()
                .setProductType(BillingClient.ProductType.SUBS)
                .build()
        )
        if (subsResult.billingResult.responseCode ==
            BillingClient.BillingResponseCode.OK) {
            allPurchases.addAll(subsResult.purchasesList)
        }

        // Query one-time purchases
        val inappResult = billingWrapper.getClient()!!.queryPurchasesAsync(
            QueryPurchasesParams.newBuilder()
                .setProductType(BillingClient.ProductType.INAPP)
                .build()
        )
        if (inappResult.billingResult.responseCode ==
            BillingClient.BillingResponseCode.OK) {
            allPurchases.addAll(inappResult.purchasesList)
        }

        return allPurchases
    }

    // Refresh entitlements from Play Store (call on every app launch)
    suspend fun refreshEntitlements() {
        val purchases = queryCurrentPurchases()

        // Build set of active product IDs
        val activeProducts = purchases
            .filter { it.purchaseState == Purchase.PurchaseState.PURCHASED }
            .flatMap { it.products }
            .toSet()

        // Update local entitlement cache
        entitlementRepository.syncEntitlements(activeProducts)

        // Acknowledge any unacknowledged purchases (safety net)
        purchases
            .filter {
                it.purchaseState == Purchase.PurchaseState.PURCHASED
                    && !it.isAcknowledged
            }
            .forEach { purchase ->
                purchaseHandler.handlePurchases(listOf(purchase))
            }
    }
```

#### 3.2 Grace Period Handling (3-7 Days)

```kotlin
// billing/SubscriptionStateManager.kt
class SubscriptionStateManager(
    private val billingRepository: BillingRepository,
    private val entitlementRepository: EntitlementRepository
) {
    /**
     * Grace Period (3-7 days, configured in Play Console):
     * - Payment failed, but Google is retrying
     * - User SHOULD still have premium access (to reduce churn)
     * - Show a non-intrusive prompt to update payment method
     *
     * Detection: Check subscription purchase record.
     * During grace period, the purchase is still in PURCHASED state
     * but the auto-renewing status may indicate an issue.
     *
     * Server-side detection is more reliable (see Phase 4).
     * Client-side, the purchase continues to appear as active during grace period.
     */

    fun handleGracePeriod(purchase: Purchase) {
        // During grace period, maintain premium access
        entitlementRepository.grantEntitlement(
            productId = purchase.products.first(),
            purchaseToken = purchase.purchaseToken,
            orderId = purchase.orderId ?: "",
            isGracePeriod = true
        )

        // Show subtle notification to user
        showPaymentIssueNotification(
            message = "There's an issue with your payment. " +
                "Update your payment method to keep Premium access.",
            action = "Update Payment",
            deepLink = "https://play.google.com/store/account/subscriptions"
        )
    }

    /**
     * Account Hold (up to 30 days, configured in Play Console):
     * - Grace period expired, payment still failing
     * - User SHOULD NOT have premium access
     * - Show prominent prompt to resubscribe or update payment
     *
     * Client-side: The purchase will NOT appear in queryPurchasesAsync
     * during account hold. The user effectively has no active subscription.
     */

    fun handleAccountHold() {
        // Revoke premium access
        entitlementRepository.revokeAllEntitlements()

        // Show prominent resubscription prompt
        showResubscriptionPrompt(
            message = "Your Premium subscription is on hold due to a payment issue. " +
                "Update your payment method to restore Premium features.",
            action = "Fix Payment",
            deepLink = "https://play.google.com/store/account/subscriptions"
        )
    }

    private fun showPaymentIssueNotification(
        message: String,
        action: String,
        deepLink: String
    ) {
        // Implement as in-app banner or notification
    }

    private fun showResubscriptionPrompt(
        message: String,
        action: String,
        deepLink: String
    ) {
        // Implement as prominent in-app dialog
    }
}
```

#### 3.3 Proration Modes for Upgrades/Downgrades

```kotlin
/**
 * Proration Modes (BillingFlowParams.SubscriptionReplacementMode):
 *
 * CHARGE_PRORATED_PRICE (Recommended for upgrades):
 *   User is charged the price difference immediately.
 *   Example: Upgrading from $4.99/mo Basic to $9.99/mo Premium
 *   mid-cycle charges ~$2.50 for the remaining half-month.
 *   New billing cycle starts at the original renewal date.
 *
 * CHARGE_FULL_PRICE (Simple alternative):
 *   User is charged the full new price immediately.
 *   A new billing cycle starts immediately.
 *   Old plan's remaining value is credited to the new plan.
 *
 * WITHOUT_PRORATION (For downgrades):
 *   The new plan takes effect at the next renewal date.
 *   User keeps the old plan until then.
 *   No charge or credit is applied.
 *
 * DEFERRED (For downgrades — user keeps old plan until renewal):
 *   Same as WITHOUT_PRORATION — downgrade takes effect at renewal.
 *   Recommended for downgrades to avoid user confusion.
 */

// Upgrade example: Basic Monthly → Premium Monthly
fun upgradeSubscription(
    activity: Activity,
    premiumProductDetails: ProductDetails,
    premiumOfferToken: String,
    currentBasicPurchaseToken: String
) {
    billingRepository.launchSubscriptionPurchase(
        activity = activity,
        productDetails = premiumProductDetails,
        offerToken = premiumOfferToken,
        oldPurchaseToken = currentBasicPurchaseToken,
        prorationMode = BillingFlowParams.SubscriptionReplacementMode
            .CHARGE_PRORATED_PRICE
    )
}

// Downgrade example: Premium Monthly → Basic Monthly
fun downgradeSubscription(
    activity: Activity,
    basicProductDetails: ProductDetails,
    basicOfferToken: String,
    currentPremiumPurchaseToken: String
) {
    billingRepository.launchSubscriptionPurchase(
        activity = activity,
        productDetails = basicProductDetails,
        offerToken = basicOfferToken,
        oldPurchaseToken = currentPremiumPurchaseToken,
        prorationMode = BillingFlowParams.SubscriptionReplacementMode
            .DEFERRED
    )
}
```

#### 3.4 Subscription State Diagram

```
┌──────────────────────────────────────────────────────────────────┐
│                    SUBSCRIPTION LIFECYCLE                         │
│                                                                  │
│  ┌─────────┐    purchase     ┌──────────┐   acknowledge         │
│  │  None   │ ─────────────→ │ PURCHASED │ ─────────────→ Active │
│  └─────────┘                └──────────┘                        │
│       ↑                          │                               │
│       │                          │ pending payment               │
│       │                          ▼                               │
│       │                    ┌──────────┐                          │
│       │                    │ PENDING  │ (cash payments)          │
│       │                    └──────────┘                          │
│       │                                                          │
│  Active subscription:                                            │
│  ┌────────┐  payment   ┌───────────┐  retry    ┌────────────┐  │
│  │ Active │─ fails ──→│Grace Period│─ fails ──→│Account Hold│  │
│  │        │            │ (3-7 days) │           │ (≤30 days) │  │
│  └────────┘            └───────────┘           └────────────┘  │
│       │                     │ payment               │            │
│       │                     │ succeeds              │ payment    │
│       │                     ▼                       │ succeeds   │
│       │                ┌────────┐                   ▼            │
│       │                │ Active │ ←──────── ┌────────┐          │
│       │                └────────┘           │ Active │          │
│       │                                     └────────┘          │
│       │                                                          │
│       │  user cancels                                            │
│       ▼                                                          │
│  ┌────────────────┐  period ends  ┌──────────┐                  │
│  │ Active (cancel │ ───────────→ │ Expired  │                   │
│  │ pending)       │               └──────────┘                  │
│  └────────────────┘                    │                         │
│                                        │ user re-subscribes     │
│                                        ▼                         │
│                                   ┌────────┐                    │
│                                   │ Active │                    │
│                                   └────────┘                    │
└──────────────────────────────────────────────────────────────────┘

Key: During "Active (cancel pending)", user still has premium access
until the end of the current billing period. Do NOT revoke early.
```

---

### Phase 4: Server-Side Validation

#### 4.1 Why Server-Side Validation Matters

```
Client-side only (no server):
  ✅ Simple to implement
  ❌ Trivially bypassed by modified APKs
  ❌ Cannot detect refunds (no notification mechanism)
  ❌ Cannot verify subscription state changes in real-time
  ❌ Cannot track server-side analytics for revenue

Server-side validation:
  ✅ Tamper-proof entitlement verification
  ✅ Real-time refund detection via RTDN (Real-Time Developer Notifications)
  ✅ Accurate subscription state tracking
  ✅ Required for any app with >$1K/month revenue
  ❌ Requires a backend (Firebase Cloud Functions works for solo devs)
```

#### 4.2 Server-Side Validation Flow

```
┌──────────┐   purchase    ┌──────────┐   send token   ┌──────────┐
│ Android  │ ───────────→ │ Google   │ ──────────────→│  Your    │
│ App      │              │ Play     │                │  Server  │
└──────────┘              └──────────┘                └──────────┘
     │                                                      │
     │                                          Validate token with
     │                                          Google Play Developer API
     │                                                      │
     │                                                      ▼
     │                                              ┌──────────────┐
     │               grant entitlement              │ Verified?    │
     │ ←───────────────────────────────────────────│ Yes: grant   │
     │                                              │ No: deny     │
     │                                              └──────────────┘
```

#### 4.3 Validation with Google Play Developer API

```kotlin
// Server-side validation (Firebase Cloud Function or your backend)
// This runs on your SERVER, not in the Android app

/**
 * Validate a subscription purchase token with the Google Play Developer API.
 *
 * Endpoint: GET https://androidpublisher.googleapis.com/androidpublisher/v3/
 *   applications/{packageName}/purchases/subscriptionsv2/tokens/{token}
 *
 * Response includes:
 *   - subscriptionState: SUBSCRIPTION_STATE_ACTIVE, _EXPIRED, _PAUSED, etc.
 *   - lineItems[].expiryTime: When the subscription expires
 *   - lineItems[].autoRenewingPlan: Whether auto-renew is enabled
 *   - acknowledgementState: Whether the purchase was acknowledged
 *   - linkedPurchaseToken: For upgrades/downgrades
 */

// Simplified Kotlin server-side validation (e.g., Ktor backend)
suspend fun validateSubscription(
    packageName: String,
    purchaseToken: String
): SubscriptionValidationResult {
    val androidPublisher = AndroidPublisher.Builder(
        httpTransport,
        jsonFactory,
        credential // Service account credential
    ).build()

    val subscription = androidPublisher
        .purchases()
        .subscriptionsv2()
        .get(packageName, purchaseToken)
        .execute()

    return SubscriptionValidationResult(
        isValid = subscription.subscriptionState ==
            "SUBSCRIPTION_STATE_ACTIVE",
        state = subscription.subscriptionState,
        expiryTime = subscription.lineItems
            ?.firstOrNull()?.expiryTime,
        autoRenewing = subscription.lineItems
            ?.firstOrNull()?.autoRenewingPlan != null,
        acknowledged = subscription.acknowledgementState ==
            "ACKNOWLEDGEMENT_STATE_ACKNOWLEDGED"
    )
}

data class SubscriptionValidationResult(
    val isValid: Boolean,
    val state: String,
    val expiryTime: String?,
    val autoRenewing: Boolean,
    val acknowledged: Boolean
)
```

#### 4.4 Real-Time Developer Notifications (RTDN)

```
Setup RTDN in Google Play Console:
1. Go to Monetization setup → Real-time developer notifications
2. Enter your Cloud Pub/Sub topic: projects/{project}/topics/{topic}
3. Google sends a notification to your topic for every subscription event

Notification types you will receive:
  SUBSCRIPTION_RECOVERED:     Payment recovered during grace period
  SUBSCRIPTION_RENEWED:       Subscription renewed successfully
  SUBSCRIPTION_CANCELED:      User canceled (still active until period end)
  SUBSCRIPTION_PURCHASED:     New subscription purchased
  SUBSCRIPTION_ON_HOLD:       Entered account hold
  SUBSCRIPTION_IN_GRACE_PERIOD: Entered grace period
  SUBSCRIPTION_RESTARTED:     User resubscribed from expired
  SUBSCRIPTION_PRICE_CHANGE_CONFIRMED: User accepted price change
  SUBSCRIPTION_DEFERRED:      Subscription deferred (free extension)
  SUBSCRIPTION_PAUSED:        User paused subscription
  SUBSCRIPTION_PAUSE_SCHEDULE_CHANGED: Pause schedule updated
  SUBSCRIPTION_REVOKED:       Subscription revoked (refund or policy)
  SUBSCRIPTION_EXPIRED:       Subscription expired

For each notification:
  1. Parse the purchaseToken and notificationType
  2. Call the Play Developer API to get the full subscription state
  3. Update your server-side entitlement database
  4. Optionally, push the updated state to the client via FCM
```

---

### Phase 5: Edge Cases

#### 5.1 Refund Handling

```kotlin
/**
 * Refund detection:
 * - Client-side: Not directly detectable. queryPurchasesAsync will
 *   stop returning the refunded purchase.
 * - Server-side: RTDN sends SUBSCRIPTION_REVOKED notification.
 *
 * When a refund is detected:
 * 1. Revoke premium access
 * 2. Do NOT punish the user (they may have a legitimate reason)
 * 3. Show a neutral message: "Your subscription has ended.
 *    Resubscribe anytime to get Premium back."
 * 4. Log for analytics (track refund rate)
 */

// On app launch, detect revoked purchases
suspend fun detectRevokedPurchases() {
    val currentPurchases = billingRepository.queryCurrentPurchases()
    val activePurchaseTokens = currentPurchases
        .filter { it.purchaseState == Purchase.PurchaseState.PURCHASED }
        .map { it.purchaseToken }
        .toSet()

    val cachedEntitlements = entitlementRepository.getAllEntitlements()

    for (entitlement in cachedEntitlements) {
        if (entitlement.purchaseToken !in activePurchaseTokens) {
            // This entitlement is no longer valid (refund, expiration, etc.)
            entitlementRepository.revokeEntitlement(entitlement.productId)
            Log.d("Billing", "Revoked entitlement: ${entitlement.productId}")
        }
    }
}
```

#### 5.2 Multi-Device and Restore Purchases

```kotlin
/**
 * Users may have multiple Android devices with the same Google account.
 * Purchases made on Device A should be available on Device B.
 *
 * Solution: queryPurchasesAsync returns ALL active purchases for the
 * user's Google account, regardless of which device made the purchase.
 * Call this on every app launch.
 *
 * "Restore Purchases" button (required by Google Play policy):
 * Simply re-runs queryPurchasesAsync and updates entitlements.
 */

suspend fun restorePurchases(): RestoreResult {
    val purchases = billingRepository.queryCurrentPurchases()
    var restoredCount = 0

    for (purchase in purchases) {
        if (purchase.purchaseState == Purchase.PurchaseState.PURCHASED) {
            val wasNew = entitlementRepository.grantEntitlementIfNew(
                productId = purchase.products.first(),
                purchaseToken = purchase.purchaseToken,
                orderId = purchase.orderId ?: ""
            )
            if (wasNew) restoredCount++
        }
    }

    return RestoreResult(
        success = true,
        restoredCount = restoredCount,
        message = if (restoredCount > 0)
            "Restored $restoredCount purchase(s)!"
        else
            "No purchases found to restore."
    )
}

data class RestoreResult(
    val success: Boolean,
    val restoredCount: Int,
    val message: String
)
```

#### 5.3 Testing Checklist

**Every billing flow must be tested before release:**

| Flow | Test Steps | Expected Result |
|------|-----------|-----------------|
| **New subscription** | Tap subscribe → complete Google Play flow → verify premium access | Premium granted, purchase acknowledged |
| **Subscription renewal** | Wait for test renewal (5 min in testing) → verify access continues | Access continues, renewal logged |
| **Cancellation** | Cancel in Google Play → verify access until period end → verify revocation | Access kept until end, then revoked |
| **Grace period** | Trigger payment failure (test card) → verify access maintained | Access maintained, payment prompt shown |
| **Account hold** | Grace period expires → verify access revoked | Access revoked, resubscribe prompt shown |
| **Upgrade** | Basic → Premium → verify proration and immediate access | Premium access, prorated charge |
| **Downgrade** | Premium → Basic → verify deferred change | Premium until renewal, then Basic |
| **Restore purchases** | New device → restore → verify access | Access restored from Google account |
| **Refund** | Issue refund in Play Console → verify revocation | Access revoked, neutral message |
| **Pending purchase** | Test with slow payment method → verify pending state | No access until confirmed |
| **Process death** | Kill app during purchase flow → reopen → verify recovery | Purchase recovered, access granted |
| **No network** | Attempt purchase with no network → verify error handling | Graceful error, retry option |

**Test accounts setup:**
1. In Google Play Console: Settings > License testing > Add test email addresses
2. Test accounts can make purchases without real charges
3. Test subscriptions renew every 5 minutes (not monthly/annually)
4. Test subscriptions expire after 6 renewals

---

## Expected Output

```markdown
# Play Billing Implementation: [App Name]

## Product Configuration
| Product ID | Type | Plans | Price Points |
|-----------|------|-------|-------------|
| [product_id] | Subscription | Monthly, Annual | $[X]/mo, $[X]/yr |
| [product_id] | One-time | — | $[X] |

## Architecture
- BillingClient wrapper: [Pattern used]
- Entitlement storage: [Room / SharedPreferences / Server]
- Server validation: [Yes/No — if yes, what platform]
- RTDN: [Configured / Not needed]

## Purchase Flows Implemented
- [ ] New subscription purchase
- [ ] Subscription acknowledgment with retry
- [ ] One-time purchase (consumable and non-consumable)
- [ ] Upgrade (with proration)
- [ ] Downgrade (deferred)
- [ ] Restore purchases
- [ ] Pending purchase handling

## Lifecycle Handling
- [ ] Grace period detection and UI
- [ ] Account hold detection and UI
- [ ] Cancellation (access until period end)
- [ ] Expiration (revoke access)
- [ ] Refund detection (server-side or client-side)

## Testing
- [ ] All test flows verified with license tester accounts
- [ ] Edge cases tested (process death, no network, multi-device)
- [ ] Production testing on internal track
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on implementing a complete, production-ready billing system with all edge cases
- **ST-02** (Structured Sequential Instructions) — Five-phase process from setup through edge case handling
- **RT-02** (Multi-Dimensional Analysis) — Billing evaluated across purchase types, lifecycle states, validation methods, and failure modes
- **CM-01** (Explicit Context Framing) — Context gathering about product configuration, architecture, and existing state
- **DS-06** (Prioritization Guidance) — Critical paths identified (acknowledgment, connection management) with explicit warnings about common failures

---

## Related Prompts

- `monetization_subscription_design.md` — Design the subscription tiers before implementing billing
- `monetization_pricing_strategy.md` — Set the prices that billing will charge
- `monetization_paywall_optimization.md` — Design the paywall screen that triggers the purchase flow
- `monetization_revenue_analytics.md` — Track the revenue that billing generates
- `monetization_ad_placement_strategy.md` — Implement ads alongside billing for hybrid monetization

---

## Customization Guide

- **For apps using RevenueCat or Qonversion:** These third-party SDKs abstract away most of the BillingClient complexity. You can skip Phases 1-3 and focus on Phase 4 (server validation is handled by the SDK) and Phase 5 (edge cases still need UI handling). RevenueCat is free up to $2,500 MTR (monthly tracked revenue) — excellent for solo developers.
- **For apps with no backend server:** Skip Phase 4 entirely. Client-side billing is adequate for apps with fewer than $1,000/month revenue. The risk of fraud is low at small scale. Add server-side validation when revenue justifies the infrastructure investment.
- **For apps with consumable purchases (coins, credits):** The consume flow is critical. Unlike subscriptions, consumable purchases must be consumed (not just acknowledged) so the user can buy them again. If you forget to consume, the user will get "ITEM_ALREADY_OWNED" on their second purchase attempt.
- **For apps migrating from Billing Library 4.x/5.x/6.x:** The major changes in 7.x are the new ProductDetails API (replacing SkuDetails), the SubscriptionOfferDetails structure, and enablePendingPurchases becoming mandatory. Plan for a full rewrite of your product query and purchase flow code. Existing subscribers will not be affected by the library upgrade.
- **For apps targeting only one subscription tier (no upgrades/downgrades):** Skip the proration mode logic entirely. You only need: query products, launch purchase, acknowledge, and verify on app start. This reduces the billing code by approximately 40%.
