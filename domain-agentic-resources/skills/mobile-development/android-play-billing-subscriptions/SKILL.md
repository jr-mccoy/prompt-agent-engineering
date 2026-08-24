---
name: android-play-billing-subscriptions
description: Implements Google Play Billing Library 7+ for in-app purchases and subscriptions. Covers BillingClient lifecycle, purchase flows, subscription state machine (active/grace period/on-hold/paused/cancelled/expired), server-side receipt validation via Cloud Functions, paywall UI in Compose, and testing with Play Console test tracks. Activates when implementing billing, subscriptions, paywalls, or in-app purchases for Android apps.
metadata:
  tags:
    - android
    - billing
    - mobile
    - play
    - subscriptions
    - testing
  updated: "2026-04-11"
---
# Android Play Billing & Subscriptions

Complete implementation guide for Google Play Billing Library 7+ covering one-time purchases, auto-renewing subscriptions, server-side verification, paywall design, and testing.

## Purpose

Implementing billing correctly requires handling a complex state machine, server-side verification, edge cases (pending purchases, network failures, upgrade/downgrade), and Play Store policy compliance. This skill provides production-ready patterns for the entire billing lifecycle.

## When to Use This Skill

Use this skill when you need to:
- Implement Google Play Billing Library in an Android app
- Handle subscription lifecycle (auto-renew, grace period, cancellation, etc.)
- Build server-side receipt validation with Firebase Cloud Functions
- Design paywall screens in Jetpack Compose
- Test purchases with Play Console test tracks and license testers
- Implement subscription upgrades, downgrades, and plan changes
- Handle purchase acknowledgment and consumption

## When NOT to Use This Skill

Do NOT use this skill when:
- Building for iOS (use StoreKit)
- Implementing third-party payment processors (Stripe, etc.)
- Only need AdMob ads without purchases (use android-admob-mediation)
- Need general monetization strategy (use android-monetization-architect agent)

## Step 1: Add Dependencies and Configure BillingClient

```kotlin
// build.gradle.kts (app module)
dependencies {
    implementation("com.android.billingclient:billing-ktx:7.0.0")
}
```

### Hilt Module for BillingClient

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object BillingModule {

    @Provides
    @Singleton
    fun provideBillingClient(
        @ApplicationContext context: Context,
        purchaseListener: PurchasesUpdatedListener,
    ): BillingClient {
        return BillingClient.newBuilder(context)
            .setListener(purchaseListener)
            .enablePendingPurchases()
            .build()
    }
}
```

## Step 2: Implement BillingClient Connection Management

```kotlin
@Singleton
class BillingClientManager @Inject constructor(
    private val billingClient: BillingClient,
) {
    private val _connectionState = MutableStateFlow(false)
    val isConnected: StateFlow<Boolean> = _connectionState.asStateFlow()

    private var retryCount = 0
    private val maxRetries = 3

    suspend fun ensureConnected(): Boolean {
        if (billingClient.isReady) return true

        return suspendCancellableCoroutine { continuation ->
            billingClient.startConnection(object : BillingClientStateListener {
                override fun onBillingSetupFinished(result: BillingResult) {
                    if (result.responseCode == BillingClient.BillingResponseCode.OK) {
                        _connectionState.value = true
                        retryCount = 0
                        continuation.resume(true)
                    } else {
                        _connectionState.value = false
                        continuation.resume(false)
                    }
                }

                override fun onBillingServiceDisconnected() {
                    _connectionState.value = false
                    if (retryCount < maxRetries) {
                        retryCount++
                        // Reconnection handled by next ensureConnected() call
                    }
                }
            })
        }
    }
}
```

## Step 3: Query Products and Launch Purchase Flow

```kotlin
@Singleton
class PurchaseManager @Inject constructor(
    private val billingClientManager: BillingClientManager,
    private val billingClient: BillingClient,
    private val verificationRepository: PurchaseVerificationRepository,
) {
    suspend fun querySubscriptionProducts(): List<ProductDetails> {
        billingClientManager.ensureConnected()

        val params = QueryProductDetailsParams.newBuilder()
            .setProductList(listOf(
                QueryProductDetailsParams.Product.newBuilder()
                    .setProductId("premium_monthly")
                    .setProductType(BillingClient.ProductType.SUBS)
                    .build(),
                QueryProductDetailsParams.Product.newBuilder()
                    .setProductId("premium_annual")
                    .setProductType(BillingClient.ProductType.SUBS)
                    .build(),
            ))
            .build()

        val (result, productDetails) = billingClient.queryProductDetails(params)
        return if (result.responseCode == BillingClient.BillingResponseCode.OK) {
            productDetails ?: emptyList()
        } else {
            emptyList()
        }
    }

    fun launchPurchaseFlow(
        activity: Activity,
        productDetails: ProductDetails,
        offerToken: String,
    ): BillingResult {
        val flowParams = BillingFlowParams.newBuilder()
            .setProductDetailsParamsList(listOf(
                BillingFlowParams.ProductDetailsParams.newBuilder()
                    .setProductDetails(productDetails)
                    .setOfferToken(offerToken)
                    .build()
            ))
            .build()

        return billingClient.launchBillingFlow(activity, flowParams)
    }
}
```

## Step 4: Handle Purchase Updates

```kotlin
@Singleton
class PurchaseUpdateHandler @Inject constructor(
    private val billingClient: BillingClient,
    private val verificationRepository: PurchaseVerificationRepository,
    private val entitlementManager: EntitlementManager,
) : PurchasesUpdatedListener {

    override fun onPurchasesUpdated(result: BillingResult, purchases: List<Purchase>?) {
        when (result.responseCode) {
            BillingClient.BillingResponseCode.OK -> {
                purchases?.forEach { purchase -> processPurchase(purchase) }
            }
            BillingClient.BillingResponseCode.USER_CANCELED -> {
                // User cancelled — no action needed
            }
            BillingClient.BillingResponseCode.ITEM_ALREADY_OWNED -> {
                // Restore existing purchase
                restorePurchases()
            }
            else -> {
                // Log error for debugging
            }
        }
    }

    private fun processPurchase(purchase: Purchase) {
        CoroutineScope(Dispatchers.IO).launch {
            if (purchase.purchaseState == Purchase.PurchaseState.PURCHASED) {
                // 1. Verify server-side FIRST
                val verified = verificationRepository.verifyPurchase(
                    purchaseToken = purchase.purchaseToken,
                    productId = purchase.products.first(),
                )

                if (verified) {
                    // 2. Acknowledge the purchase (required within 3 days)
                    if (!purchase.isAcknowledged) {
                        val ackResult = billingClient.acknowledgePurchase(
                            AcknowledgePurchaseParams.newBuilder()
                                .setPurchaseToken(purchase.purchaseToken)
                                .build()
                        )
                    }

                    // 3. Grant entitlement
                    entitlementManager.grantEntitlement(purchase.products.first())
                }
            } else if (purchase.purchaseState == Purchase.PurchaseState.PENDING) {
                // Pending purchase (e.g., cash payment) — don't grant yet
                entitlementManager.markPending(purchase.products.first())
            }
        }
    }
}
```

## Step 5: Server-Side Receipt Validation

See `references/subscription_state_machine.md` for the complete state machine.

```typescript
// Cloud Function — verify purchase with Google Play Developer API
import * as functions from "firebase-functions";
import { google } from "googleapis";

const play = google.androidpublisher("v3");

export const verifyPurchase = functions.https.onCall(async (data, context) => {
  if (!context.auth) {
    throw new functions.https.HttpsError("unauthenticated", "Must be signed in");
  }

  const { purchaseToken, productId, productType } = data;

  const auth = new google.auth.GoogleAuth({
    scopes: ["https://www.googleapis.com/auth/androidpublisher"],
  });
  const authClient = await auth.getClient();

  try {
    if (productType === "subs") {
      const response = await play.purchases.subscriptions.get({
        auth: authClient,
        packageName: "com.example.app",
        subscriptionId: productId,
        token: purchaseToken,
      });

      const subscription = response.data;
      const isValid = !subscription.cancelReason &&
        subscription.paymentState === 1; // 1 = received

      // Store subscription state in Firestore
      await admin.firestore()
        .collection("subscriptions")
        .doc(context.auth.uid)
        .set({
          productId,
          purchaseToken,
          state: subscription.cancelReason ? "cancelled" : "active",
          expiryTime: subscription.expiryTimeMillis,
          autoRenewing: subscription.autoRenewing,
          updatedAt: admin.firestore.FieldValue.serverTimestamp(),
        });

      return { valid: isValid, expiryTime: subscription.expiryTimeMillis };
    } else {
      // One-time purchase verification
      const response = await play.purchases.products.get({
        auth: authClient,
        packageName: "com.example.app",
        productId,
        token: purchaseToken,
      });

      return { valid: response.data.purchaseState === 0 }; // 0 = purchased
    }
  } catch (error) {
    throw new functions.https.HttpsError("internal", "Verification failed");
  }
});
```

## Step 6: Entitlement Management

```kotlin
@Singleton
class EntitlementManager @Inject constructor(
    private val entitlementDao: EntitlementDao,
    private val firestore: FirebaseFirestore,
    private val auth: FirebaseAuth,
) {
    // Flow that UI observes for feature gating
    val isPremium: Flow<Boolean> = entitlementDao.observeEntitlement("premium")
        .map { it?.isActive == true }

    suspend fun checkEntitlements() {
        val userId = auth.currentUser?.uid ?: return

        // Fetch from server (source of truth)
        val doc = firestore.collection("subscriptions")
            .document(userId)
            .get().await()

        val isActive = doc.getString("state") == "active" &&
            (doc.getLong("expiryTime") ?: 0) > System.currentTimeMillis()

        // Cache locally in Room
        entitlementDao.upsert(Entitlement(
            id = "premium",
            isActive = isActive,
            expiresAt = doc.getLong("expiryTime"),
            checkedAt = System.currentTimeMillis(),
        ))
    }

    suspend fun grantEntitlement(productId: String) {
        entitlementDao.upsert(Entitlement(
            id = "premium",
            isActive = true,
            checkedAt = System.currentTimeMillis(),
        ))
    }
}
```

## Step 7: Build Paywall UI in Compose

```kotlin
@Composable
fun PaywallScreen(
    products: List<ProductDetails>,
    onSubscribe: (ProductDetails, String) -> Unit,
    onRestorePurchases: () -> Unit,
) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState())
            .padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
    ) {
        // Value proposition
        Text("Unlock Premium", style = MaterialTheme.typography.headlineMedium)
        Spacer(Modifier.height(8.dp))
        Text("Get the most out of your experience", color = MaterialTheme.colorScheme.onSurfaceVariant)

        Spacer(Modifier.height(24.dp))

        // Feature list
        PremiumFeatureList()

        Spacer(Modifier.height(24.dp))

        // Subscription options
        products.forEach { product ->
            product.subscriptionOfferDetails?.firstOrNull()?.let { offer ->
                SubscriptionCard(
                    product = product,
                    offer = offer,
                    onSelect = { onSubscribe(product, offer.offerToken) },
                )
            }
        }

        Spacer(Modifier.height(16.dp))

        // Restore purchases
        TextButton(onClick = onRestorePurchases) {
            Text("Restore Purchases")
        }

        // Legal text (required by Play Store policy)
        Spacer(Modifier.height(8.dp))
        Text(
            "Subscription auto-renews unless cancelled at least 24 hours before " +
            "the end of the current period. Manage subscriptions in Google Play settings.",
            style = MaterialTheme.typography.bodySmall,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
            textAlign = TextAlign.Center,
        )
    }
}
```

## Step 8: Testing

See `references/play_billing_testing.md` for the complete testing guide.

**Quick testing checklist:**
1. Add license test accounts in Play Console (Settings > License testing)
2. Upload a signed AAB to internal testing track
3. Test with license testers — purchases are free and can be cancelled
4. Test all states: purchase, cancel, renew, grace period, refund
5. Test offline purchase → reconnect → verification flow
6. Test `ITEM_ALREADY_OWNED` recovery
7. Verify server-side verification with Cloud Functions logs

## Common Issues

### "Item already owned" Error
Call `billingClient.queryPurchasesAsync()` on app start to recover unacknowledged purchases. Acknowledge them to resolve.

### Purchase Not Acknowledged Within 3 Days
Google automatically refunds unacknowledged purchases after 3 days. Always acknowledge immediately after server verification.

### Pending Purchases
Some regions support delayed payment methods. Don't grant entitlements for pending purchases — wait for `PURCHASED` state.

### Testing with Static Responses
Use reserved product IDs for testing without Play Console setup:
- `android.test.purchased` — Always succeeds
- `android.test.canceled` — Always cancels
- `android.test.item_unavailable` — Item not found

## Resources

### references/subscription_state_machine.md
Complete state machine diagram for subscription lifecycle with all transitions and recommended handling.

### references/play_billing_testing.md
Testing guide covering license testers, test tracks, static responses, and automated testing strategies.

## Related Skills

- `android-admob-mediation` — AdMob integration with subscriber ad suppression
- `android-multi-source-data-layer` — Entitlement caching with Room + Firestore
- `android-firebase-sync-validator` — Cloud Functions validation for receipt verification
