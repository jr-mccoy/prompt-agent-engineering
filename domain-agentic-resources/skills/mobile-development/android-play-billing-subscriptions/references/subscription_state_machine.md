# Subscription State Machine

## State Diagram

```
                    ┌──────────────────────────┐
                    │     USER PURCHASES       │
                    │   (launchBillingFlow)     │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │         ACTIVE            │
                    │  (auto-renewing or        │
                    │   prepaid with time left) │
                    └──┬────┬────┬────┬────┬───┘
                       │    │    │    │    │
          Billing ─────┘    │    │    │    └───── User cancels
          fails             │    │    │           (still active
          (card expired)    │    │    │            until period end)
                            │    │    │
                  ▼         │    │    │         ▼
    ┌─────────────────┐     │    │    │    ┌──────────────────┐
    │  GRACE PERIOD    │     │    │    │    │    CANCELLED      │
    │  (billing retry, │     │    │    │    │  (active until    │
    │   access kept)   │     │    │    │    │   expiry date)    │
    └───────┬──────────┘     │    │    │    └────────┬─────────┘
            │                │    │    │             │
   Billing  │  Billing      │    │    │    Period    │  User
   recovers │  still fails  │    │    │    ends      │  resubscribes
            │                │    │    │             │
     ▼      │         ▼     │    │    │      ▼      │      ▼
  (back to  │  ┌────────────┐│    │    │  ┌────────┐│  (back to
   ACTIVE)  │  │  ON HOLD   ││    │    │  │EXPIRED ││   ACTIVE)
            │  │  (access    ││    │    │  │        ││
            │  │  suspended) ││    │    │  └───┬────┘│
            │  └──────┬──────┘│    │    │      │     │
            │         │       │    │    │      │     │
            │  Billing│       │    │    │  Win-back  │
            │  recovers       │    │    │  offer     │
            │         │       │    │    │      │     │
            │      ▼  │       │    │    │      ▼     │
            │  (back to       │    │    │  (back to  │
            │   ACTIVE)       │    │    │   ACTIVE)  │
            │                 │    │    │            │
            │        User pauses  │    │            │
            │                 │   │    │            │
            │                 ▼   │    │            │
            │    ┌──────────────┐ │    │            │
            │    │    PAUSED     │ │    │            │
            │    │  (user chose  │ │    │            │
            │    │   to pause)   │ │    │            │
            │    └───────┬──────┘ │    │            │
            │            │        │    │            │
            │    Resume  │ Expire │    │            │
            │            │        │    │            │
            │         ▼  │   ▼    │    │            │
            │    (back to  (to    │    │            │
            │     ACTIVE) EXPIRED)│    │            │
            │                     │    │            │
            │           Renews ───┘    │            │
            │           successfully   │            │
            │                          │            │
            │              Refund ─────┘            │
            │              (voided purchase)        │
            │                     │                 │
            │                     ▼                 │
            │            ┌──────────────┐           │
            │            │   REVOKED     │           │
            │            │  (refunded,   │           │
            │            │   access off) │           │
            │            └──────────────┘           │
            │                                       │
            └───────────────────────────────────────┘
```

## State Handling Guide

### ACTIVE
- **User access:** Full premium features
- **UI:** Show premium badge, hide paywall
- **Background:** No action needed, renews automatically
- **Check:** `expiryTimeMillis > now && !cancelReason`

### GRACE PERIOD (billing retry)
- **Duration:** Typically 7 or 30 days (configurable in Play Console)
- **User access:** KEEP access (encourage payment update)
- **UI:** Show banner "Update your payment method to keep premium"
- **Action:** Deep link to Google Play subscription management
- **Check:** `paymentState == 0 (pending)` during active period

### ON HOLD (billing failed past grace period)
- **User access:** SUSPEND access
- **UI:** Show "Subscription paused due to payment issue" with recovery CTA
- **Action:** Deep link to Play subscription settings
- **Check:** `paymentState == 0 && past grace period`

### PAUSED (user-initiated)
- **User access:** SUSPEND access
- **UI:** Show "Subscription paused — resume anytime"
- **Action:** Deep link to resume in Play Store
- **Duration:** Up to 1 year, auto-expires after max pause duration

### CANCELLED (user cancelled, still in paid period)
- **User access:** KEEP access until period end
- **UI:** Show "Premium until [date]" and win-back offer
- **Action:** Offer discount to resubscribe
- **Check:** `cancelReason != null && expiryTimeMillis > now`

### EXPIRED
- **User access:** REMOVE access
- **UI:** Show paywall, offer win-back pricing
- **Action:** Allow new subscription purchase
- **Check:** `expiryTimeMillis <= now`

### REVOKED (refunded)
- **User access:** REMOVE access immediately
- **UI:** Revert to free tier
- **Action:** Log for analytics, no user action
- **Check:** Voided purchases API or RTDN notification

## Real-Time Developer Notifications (RTDN)

Set up Cloud Pub/Sub to receive subscription state changes in real-time:

### Notification Types

| Type | Meaning | Action |
|------|---------|--------|
| SUBSCRIPTION_RECOVERED | Billing recovered from grace/hold | Re-grant access |
| SUBSCRIPTION_RENEWED | Successfully renewed | Extend expiry |
| SUBSCRIPTION_CANCELED | User cancelled | Mark cancel date, keep access |
| SUBSCRIPTION_PURCHASED | New subscription | Grant access |
| SUBSCRIPTION_ON_HOLD | Entered on-hold | Suspend access |
| SUBSCRIPTION_IN_GRACE_PERIOD | Entered grace period | Show payment update prompt |
| SUBSCRIPTION_RESTARTED | Restarted after pause/cancel | Re-grant access |
| SUBSCRIPTION_PRICE_CHANGE_CONFIRMED | User accepted price change | Update stored price |
| SUBSCRIPTION_DEFERRED | Subscription extended (promo) | Extend expiry |
| SUBSCRIPTION_PAUSED | User paused | Suspend access |
| SUBSCRIPTION_PAUSE_SCHEDULE_CHANGED | Pause schedule modified | Update UI |
| SUBSCRIPTION_REVOKED | Refunded/revoked | Remove access immediately |
| SUBSCRIPTION_EXPIRED | Expired | Remove access |

### Cloud Function Handler

```typescript
export const handleSubscriptionNotification = functions.pubsub
  .topic("play-billing-notifications")
  .onPublish(async (message) => {
    const data = JSON.parse(Buffer.from(message.data, "base64").toString());
    const notification = data.subscriptionNotification;

    if (!notification) return;

    const { purchaseToken, subscriptionId, notificationType } = notification;

    // Fetch latest subscription state from Play Developer API
    const subscription = await getSubscriptionState(purchaseToken, subscriptionId);

    // Update Firestore based on notification type
    // (always fetch fresh state rather than trusting notification alone)
    await updateSubscriptionInFirestore(subscription);
  });
```
