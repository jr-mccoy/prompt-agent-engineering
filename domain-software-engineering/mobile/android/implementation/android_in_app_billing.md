---
title: "Android In-App Billing"
category: mobile-development
description: ""
tags:
  - android
  - mobile-development
updated: "2026-03-19"
---

# Android In-App Billing

**Objective:** Implement Google Play Billing for in-app purchases and subscriptions with proper purchase verification, entitlement management, and subscription lifecycle handling.

**When to Use:** Use this prompt when monetizing an Android app through one-time purchases, consumables, or subscriptions. Best used when setting up billing for the first time or migrating to the latest Billing Library version.

**Prompt Type:** Modular (120-150 lines)

---

## Context Gathering

Before implementing billing, gather essential context:

1. **Product Types:**
   - "What types of purchases do you need (one-time, consumables, subscriptions)?"
   - "What are your product IDs configured in Google Play Console?"
   - "Do subscriptions have different tiers or billing periods?"

2. **Verification:**
   - "Do you have a backend for purchase verification?"
   - "Should entitlements be stored locally or server-side?"

3. **User Experience:**
   - "How should purchase state be shown in UI?"
   - "Do you need to handle subscription upgrades/downgrades?"

---

## Instructions

### CRITICAL: Implementation Requirements

**Before implementing ANY code, you MUST:**

1. **Understand existing billing setup** - Check for existing BillingClient, purchase flows, or subscription handling in the codebase.
2. **Verify product configuration** - Confirm product IDs, pricing tiers, and subscription plans are configured in Play Console.
3. **Follow security best practices** - Never trust client-side purchase verification alone; implement server-side validation.
4. **Provide specific, working code** - All code samples MUST include file paths (e.g., `billing/BillingManager.kt`) and be copy-paste ready.
5. **Include proper error handling** - Handle all BillingResponseCodes appropriately with user feedback.

**Security is critical for billing.** Always implement server-side receipt validation for real money transactions.

### Quality Requirements

- ❌ Do NOT trust client-side purchase verification for unlocking features
- ❌ Do NOT generate billing code without proper error handling for all response codes
- ❌ Do NOT skip acknowledgement of purchases (will result in refunds)
- ❌ Do NOT ignore subscription grace periods and account holds
- ✅ DO implement server-side receipt validation
- ✅ DO provide clear UI feedback during purchase flows
- ✅ DO handle purchase restoration properly
- ✅ DO specify exact file paths for all code changes

---

### Phase 1: Billing Setup

#### 1.1 Dependencies

```kotlin
// build.gradle.kts
dependencies {
    implementation("com.android.billingclient:billing-ktx:6.1.0")
}
```

#### 1.2 Billing Client Setup

```kotlin
@Singleton
class BillingManager @Inject constructor(
    @ApplicationContext private val context: Context,
    private val purchaseVerifier: PurchaseVerifier
) {
    private var billingClient: BillingClient? = null
    private val _purchaseState = MutableStateFlow<PurchaseState>(PurchaseState.Idle)
    val purchaseState: StateFlow<PurchaseState> = _purchaseState.asStateFlow()

    private val _products = MutableStateFlow<List<ProductDetails>>(emptyList())
    val products: StateFlow<List<ProductDetails>> = _products.asStateFlow()

    private val purchasesUpdatedListener = PurchasesUpdatedListener { billingResult, purchases ->
        when (billingResult.responseCode) {
            BillingClient.BillingResponseCode.OK -> {
                purchases?.forEach { purchase ->
                    handlePurchase(purchase)
                }
            }
            BillingClient.BillingResponseCode.USER_CANCELED -> {
                _purchaseState.value = PurchaseState.Cancelled
            }
            else -> {
                _purchaseState.value = PurchaseState.Error(
                    billingResult.debugMessage
                )
            }
        }
    }

    fun initialize() {
        billingClient = BillingClient.newBuilder(context)
            .setListener(purchasesUpdatedListener)
            .enablePendingPurchases()
            .build()

        startConnection()
    }

    private fun startConnection() {
        billingClient?.startConnection(object : BillingClientStateListener {
            override fun onBillingSetupFinished(billingResult: BillingResult) {
                if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
                    queryProducts()
                    queryPurchases()
                }
            }

            override fun onBillingServiceDisconnected() {
                // Retry connection
                startConnection()
            }
        })
    }
}
```

---

### Phase 2: Product Queries

#### 2.1 Query Available Products

```kotlin
private fun queryProducts() {
    val productList = listOf(
        QueryProductDetailsParams.Product.newBuilder()
            .setProductId("premium_monthly")
            .setProductType(BillingClient.ProductType.SUBS)
            .build(),
        QueryProductDetailsParams.Product.newBuilder()
            .setProductId("premium_yearly")
            .setProductType(BillingClient.ProductType.SUBS)
            .build(),
        QueryProductDetailsParams.Product.newBuilder()
            .setProductId("remove_ads")
            .setProductType(BillingClient.ProductType.INAPP)
            .build()
    )

    val params = QueryProductDetailsParams.newBuilder()
        .setProductList(productList)
        .build()

    billingClient?.queryProductDetailsAsync(params) { billingResult, productDetailsList ->
        if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
            _products.value = productDetailsList
        }
    }
}
```

#### 2.2 Query Existing Purchases

```kotlin
private fun queryPurchases() {
    billingClient?.queryPurchasesAsync(
        QueryPurchasesParams.newBuilder()
            .setProductType(BillingClient.ProductType.SUBS)
            .build()
    ) { billingResult, purchasesList ->
        if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
            purchasesList.forEach { purchase ->
                if (purchase.purchaseState == Purchase.PurchaseState.PURCHASED) {
                    handlePurchase(purchase)
                }
            }
        }
    }

    // Also query in-app purchases
    billingClient?.queryPurchasesAsync(
        QueryPurchasesParams.newBuilder()
            .setProductType(BillingClient.ProductType.INAPP)
            .build()
    ) { billingResult, purchasesList ->
        if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
            purchasesList.forEach { purchase ->
                if (purchase.purchaseState == Purchase.PurchaseState.PURCHASED) {
                    handlePurchase(purchase)
                }
            }
        }
    }
}
```

---

### Phase 3: Purchase Flow

#### 3.1 Launch Purchase Flow

```kotlin
fun launchPurchaseFlow(activity: Activity, productDetails: ProductDetails) {
    val offerToken = productDetails.subscriptionOfferDetails
        ?.firstOrNull()?.offerToken

    val productDetailsParamsList = listOf(
        BillingFlowParams.ProductDetailsParams.newBuilder()
            .setProductDetails(productDetails)
            .apply {
                offerToken?.let { setOfferToken(it) }
            }
            .build()
    )

    val billingFlowParams = BillingFlowParams.newBuilder()
        .setProductDetailsParamsList(productDetailsParamsList)
        .build()

    _purchaseState.value = PurchaseState.Purchasing

    billingClient?.launchBillingFlow(activity, billingFlowParams)
}
```

#### 3.2 Handle Purchase

```kotlin
private fun handlePurchase(purchase: Purchase) {
    if (purchase.purchaseState == Purchase.PurchaseState.PURCHASED) {
        if (!purchase.isAcknowledged) {
            acknowledgePurchase(purchase)
        }

        // Verify with backend (recommended)
        CoroutineScope(Dispatchers.IO).launch {
            val isValid = purchaseVerifier.verify(purchase)
            if (isValid) {
                grantEntitlement(purchase)
                _purchaseState.value = PurchaseState.Success(purchase.products)
            } else {
                _purchaseState.value = PurchaseState.Error("Verification failed")
            }
        }
    } else if (purchase.purchaseState == Purchase.PurchaseState.PENDING) {
        _purchaseState.value = PurchaseState.Pending
    }
}

private fun acknowledgePurchase(purchase: Purchase) {
    val params = AcknowledgePurchaseParams.newBuilder()
        .setPurchaseToken(purchase.purchaseToken)
        .build()

    billingClient?.acknowledgePurchase(params) { billingResult ->
        if (billingResult.responseCode != BillingClient.BillingResponseCode.OK) {
            Timber.e("Acknowledge failed: ${billingResult.debugMessage}")
        }
    }
}

private fun grantEntitlement(purchase: Purchase) {
    purchase.products.forEach { productId ->
        // Update local entitlements
        entitlementManager.grant(productId)
    }
}
```

---

### Phase 4: Entitlement Management

#### 4.1 Entitlement Manager

```kotlin
@Singleton
class EntitlementManager @Inject constructor(
    private val dataStore: DataStore<Preferences>
) {
    private val _isPremium = MutableStateFlow(false)
    val isPremium: StateFlow<Boolean> = _isPremium.asStateFlow()

    private val _hasRemovedAds = MutableStateFlow(false)
    val hasRemovedAds: StateFlow<Boolean> = _hasRemovedAds.asStateFlow()

    suspend fun grant(productId: String) {
        when (productId) {
            "premium_monthly", "premium_yearly" -> {
                dataStore.edit { it[PREMIUM_KEY] = true }
                _isPremium.value = true
            }
            "remove_ads" -> {
                dataStore.edit { it[ADS_REMOVED_KEY] = true }
                _hasRemovedAds.value = true
            }
        }
    }

    suspend fun revoke(productId: String) {
        when (productId) {
            "premium_monthly", "premium_yearly" -> {
                dataStore.edit { it[PREMIUM_KEY] = false }
                _isPremium.value = false
            }
        }
    }

    suspend fun loadEntitlements() {
        dataStore.data.collect { prefs ->
            _isPremium.value = prefs[PREMIUM_KEY] ?: false
            _hasRemovedAds.value = prefs[ADS_REMOVED_KEY] ?: false
        }
    }

    companion object {
        private val PREMIUM_KEY = booleanPreferencesKey("is_premium")
        private val ADS_REMOVED_KEY = booleanPreferencesKey("ads_removed")
    }
}

sealed interface PurchaseState {
    data object Idle : PurchaseState
    data object Purchasing : PurchaseState
    data object Pending : PurchaseState
    data class Success(val productIds: List<String>) : PurchaseState
    data object Cancelled : PurchaseState
    data class Error(val message: String) : PurchaseState
}
```

---

## Expected Output

### File Structure

```
billing/
├── BillingManager.kt
├── EntitlementManager.kt
├── PurchaseVerifier.kt
├── PurchaseState.kt
└── di/
    └── BillingModule.kt
```

### Implementation Checklist

- [ ] BillingClient initialization and connection
- [ ] Product queries for subscriptions and one-time purchases
- [ ] Purchase flow launch
- [ ] Purchase acknowledgment
- [ ] Backend verification (recommended)
- [ ] Entitlement management
- [ ] Purchase state observation
- [ ] Subscription lifecycle handling
- [ ] Reconnection on service disconnect

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective for billing
- **ST-02** (Sequential Instructions): Setup to entitlement flow
- **RT-04** (Best Practice Review): Google Play Billing best practices
- **ST-03** (Output Format Templates): Billing manager template

---

## Related Prompts

- [android_state_management.md](android_state_management.md) - Purchase state in UI
- [android_api_integration.md](android_api_integration.md) - Backend verification
- [android_dependency_injection.md](android_dependency_injection.md) - DI for billing

---

## Customization Guide

### For Consumables

Handle consumable purchases:
```kotlin
private fun consumePurchase(purchase: Purchase) {
    val params = ConsumeParams.newBuilder()
        .setPurchaseToken(purchase.purchaseToken)
        .build()

    billingClient?.consumeAsync(params) { billingResult, purchaseToken ->
        if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
            // Grant consumable (coins, gems, etc.)
        }
    }
}
```

### For Subscription Upgrades

Handle plan changes:
```kotlin
fun upgradeSubscription(
    activity: Activity,
    oldPurchase: Purchase,
    newProductDetails: ProductDetails
) {
    val params = BillingFlowParams.newBuilder()
        .setProductDetailsParamsList(listOf(
            BillingFlowParams.ProductDetailsParams.newBuilder()
                .setProductDetails(newProductDetails)
                .setOfferToken(newProductDetails.subscriptionOfferDetails?.firstOrNull()?.offerToken!!)
                .build()
        ))
        .setSubscriptionUpdateParams(
            BillingFlowParams.SubscriptionUpdateParams.newBuilder()
                .setOldPurchaseToken(oldPurchase.purchaseToken)
                .setSubscriptionReplacementMode(
                    BillingFlowParams.SubscriptionUpdateParams.ReplacementMode.WITH_TIME_PRORATION
                )
                .build()
        )
        .build()

    billingClient?.launchBillingFlow(activity, params)
}
```

### For Backend Verification

Verify purchases server-side:
```kotlin
interface PurchaseVerifier {
    suspend fun verify(purchase: Purchase): Boolean
}

class ServerPurchaseVerifier @Inject constructor(
    private val api: PurchaseApi
) : PurchaseVerifier {
    override suspend fun verify(purchase: Purchase): Boolean {
        return try {
            val response = api.verifyPurchase(
                VerifyPurchaseRequest(
                    purchaseToken = purchase.purchaseToken,
                    productId = purchase.products.first(),
                    packageName = BuildConfig.APPLICATION_ID
                )
            )
            response.isValid
        } catch (e: Exception) {
            false
        }
    }
}
```
