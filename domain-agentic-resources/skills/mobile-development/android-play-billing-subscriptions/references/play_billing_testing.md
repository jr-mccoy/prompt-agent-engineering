# Play Billing Testing Guide

## Testing Levels

| Level | What | How | Billing Charged? |
|-------|------|-----|-----------------|
| Static responses | Basic flow validation | Reserved product IDs | No |
| License testers | Full flow with Play | Add emails in Play Console | No (free purchases) |
| Internal testing | Real builds, small group | Internal test track (100 users) | No (for license testers) |
| Closed testing | Targeted beta group | Closed test track | Yes (real charges) |
| Open testing | Public beta | Open test track | Yes (real charges) |

## Level 1: Static Response Testing (Debug Builds)

Use reserved product IDs that always return specific responses without Play Console setup:

| Product ID | Behavior |
|------------|----------|
| `android.test.purchased` | Purchase succeeds |
| `android.test.canceled` | Purchase cancelled by user |
| `android.test.item_unavailable` | Product not found |

```kotlin
// Use static IDs in debug builds
val productId = if (BuildConfig.DEBUG) {
    "android.test.purchased"
} else {
    "premium_monthly"
}
```

**Limitations:** No subscription state testing, no server verification, no renewal.

## Level 2: License Tester Testing

### Setup
1. Go to **Play Console → Settings → License testing**
2. Add test account emails (must be Google accounts)
3. Set license response to "RESPOND_NORMALLY"

### Behavior with License Testers
- Purchases are free (no real charges)
- Subscription renewals happen on accelerated schedule:

| Real Duration | Test Duration |
|---------------|---------------|
| 1 week | 5 minutes |
| 1 month | 5 minutes |
| 3 months | 10 minutes |
| 6 months | 15 minutes |
| 1 year | 30 minutes |

- Grace period: 5 minutes
- Account hold: 10 minutes
- Subscriptions renew up to 6 times, then auto-cancel

### Testing Subscription States

```
1. Purchase subscription → verify ACTIVE state
2. Wait 5 min → verify RENEWED (check server logs)
3. Cancel subscription → verify CANCELLED (still active)
4. Wait until expiry → verify EXPIRED
5. Resubscribe → verify re-ACTIVE
```

**To test grace period:**
1. Purchase subscription with license tester
2. Remove payment method from Google account
3. Wait for renewal attempt → enters GRACE PERIOD
4. Re-add payment method → should recover

**To test on-hold:**
1. Follow grace period steps above
2. Don't re-add payment method
3. Wait past grace period → enters ON HOLD

## Level 3: Internal Testing Track

### Setup
1. Upload signed AAB to Play Console → Internal testing
2. Add up to 100 testers by email
3. Testers install via Play Store opt-in link
4. License testers get free purchases; non-license testers pay real money

### What to Test
- [ ] Fresh install purchase flow
- [ ] Subscription purchase and acknowledgment
- [ ] Subscription renewal (wait for test period)
- [ ] Subscription cancellation
- [ ] Subscription restoration on new device
- [ ] Grace period entry and recovery
- [ ] On-hold entry and recovery
- [ ] Upgrade from monthly to annual
- [ ] Downgrade from annual to monthly
- [ ] "Restore Purchases" button
- [ ] Offline purchase → reconnect → verification
- [ ] Pending purchase flow (if applicable)
- [ ] Server-side verification logs (Cloud Functions)
- [ ] RTDN notifications received (Cloud Pub/Sub)

## Level 4: Closed/Open Testing

Real charges apply (except for license testers). Use for:
- Testing real payment flows with actual transactions
- Validating receipt verification with real purchase tokens
- Testing refund handling via Play Console manual refunds
- Load testing server-side verification

## Automated Testing

### Unit Testing BillingClient (Mocked)

```kotlin
@Test
fun `successful purchase triggers server verification`() = runTest {
    // Arrange
    val mockBillingClient = mockk<BillingClient>()
    val mockVerification = mockk<PurchaseVerificationRepository>()
    val purchase = Purchase("""{"productId":"premium_monthly","purchaseToken":"test_token","purchaseState":1}""", "sig")

    coEvery { mockVerification.verifyPurchase(any(), any()) } returns true

    // Act
    purchaseHandler.processPurchase(purchase)

    // Assert
    coVerify { mockVerification.verifyPurchase("test_token", "premium_monthly") }
    coVerify { entitlementManager.grantEntitlement("premium_monthly") }
}

@Test
fun `failed verification does not grant entitlement`() = runTest {
    coEvery { mockVerification.verifyPurchase(any(), any()) } returns false

    purchaseHandler.processPurchase(purchase)

    coVerify(exactly = 0) { entitlementManager.grantEntitlement(any()) }
}
```

### Integration Testing with Billing Testing Library

```kotlin
// Use Google's BillingClient testing library for integration tests
testImplementation("com.android.billingclient:billing-testing:7.0.0")
```

## Debugging

### Common Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| "Item already owned" | Unacknowledged purchase | Query and acknowledge existing purchases |
| "Item unavailable" | Product not configured in Play Console | Create product in Play Console, wait 24h |
| Purchase succeeds but no entitlement | Server verification failing | Check Cloud Functions logs |
| Subscription doesn't renew in test | Not a license tester | Add email to license testing |
| RTDN not received | Pub/Sub not configured | Set up Real-time developer notifications in Play Console |

### Logging

```kotlin
// Enable verbose billing logging in debug
if (BuildConfig.DEBUG) {
    BillingClient.newBuilder(context)
        .enablePendingPurchases()
        .setListener(listener)
        .build()
    // Check logcat with tag: BillingClient
}
```
