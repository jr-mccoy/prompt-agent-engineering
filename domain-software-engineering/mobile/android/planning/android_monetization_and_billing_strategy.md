---
title: "Android Monetization and Billing Strategy"
category: mobile-development
description: "Choose a monetization model and design the Google Play Billing product catalog, entitlement model, and paywall strategy at planning time — before any billing code is written."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - AG-02
  - CM-01
  - NE-02
difficulty: intermediate
tags:
  - android
  - mobile-development
  - monetization
  - play-billing
  - subscriptions
  - paywall
  - entitlements
updated: "2026-06-06"
related_prompts:
  - android_app_concept_validation.md
  - ../implementation/android_in_app_billing.md
  - ../publishing/android_play_store_optimization.md
---

# Android Monetization and Billing Strategy

**Objective:** Decide *how* an Android app will make money and design the complete commercial plan — monetization model, Google Play Billing product catalog (subscriptions with base plans and offers, free trials/intro pricing, prepaid plans, one-time products), the entitlement model that maps each tier to unlocked features, paywall placement and trigger strategy, pricing/regional pricing, and a server-side purchase-verification and entitlement source-of-truth plan — so that when billing is actually implemented, every product, price, gate, and verification path is already specified.

**When to Use:** Use this prompt after the concept is validated and the feature set is roughly known, but *before* writing any Play Billing code. Use it when you must choose between subscriptions, one-time purchases, IAP, ads, freemium, or a hybrid; when you need to draft the product catalog you'll create in Play Console; when you need to draw the free/paid feature cut line; or when you need to design where and when the paywall appears. This is a planning artifact, not an implementation — it produces the spec that `android_in_app_billing.md` consumes.

**Sequence Map:** Use after `android_app_concept_validation.md`; use before `../implementation/android_in_app_billing.md`.

**Important context:** Google Play policy requires that **digital goods and services consumed inside the app must use Google Play Billing** — you cannot route in-app digital purchases to your own payment processor (physical goods/services and real-world purchases are the carve-out). External-offer and alternative-billing programs exist in limited form and vary by region and ongoing regulatory/litigation changes, so treat "Play Billing is the default" as the planning assumption and flag any external-billing ambition as a policy-review item, not a default. The current Play Billing Library is a major version that uses the `BillingClient` + `ProductDetails` API surface (one-time products and subscriptions are queried via `queryProductDetailsAsync`, subscriptions are modeled as a base plan with optional offers). The single most important architectural decision made here is the **entitlement source of truth**: never trust the client to decide what a user owns. The plan must designate a server (or at minimum Play's verification APIs) as the authority, fed by the Play Developer API and Real-Time Developer Notifications (RTDN).

---

## Context Gathering

Before recommending a model, gather:

1. **App type & value delivery:**
   - "What does the app do, and is the value delivered once (a tool/unlock) or continuously (content, sync, a service)?"
   - "Is there an ongoing server cost per active user (storage, compute, third-party APIs)?"
   - "Does the app produce digital goods consumed in-app, or facilitate real-world goods/services?"

2. **Audience & willingness to pay:**
   - "Who is the audience (consumer, prosumer, B2B), and what is their price sensitivity?"
   - "What do comparable apps charge, and via what model?"
   - "Is the audience large/ad-tolerant, or small/high-intent (better for paid)?"

3. **Business goals & constraints:**
   - "Are you optimizing for predictable recurring revenue, total downloads, or one-time cash?"
   - "Do you have a backend already, or is this client-only today?"
   - "What jurisdictions/regions matter (affects regional pricing, tax, consent)?"

4. **Catalog inputs:**
   - "What is the full feature list, and which features could plausibly be premium?"
   - "Do you want a free trial? Introductory pricing? Multiple tiers?"

---

## Instructions

### Phase 1: Monetization Model Selection

Score each model against this app. Rate Fit 1–5 (5 = strong fit). Recommend the highest-fit model (or a deliberate hybrid).

| Model | Best for | Pros | Cons / risks | Play Billing object | Fit (1–5) |
|-------|----------|------|--------------|---------------------|-----------|
| **One-time purchase (paid app / unlock)** | Tools, utilities, "buy once" value | Simple; no churn; no recurring infra | No recurring revenue; hard to fund ongoing cost | One-time product (non-consumable) | _ |
| **IAP — consumables** | Games, credits, coins, packs | Repeat revenue; flexible pricing | Needs consumption tracking; balance fraud risk | One-time product (consumable) | _ |
| **Subscriptions** | Content, sync, services with ongoing cost | Predictable MRR; trials; tiers | Churn management; refund/grace handling; policy scrutiny | Subscription (base plan + offers) | _ |
| **Freemium (free core + paid upgrade)** | Broad funnel apps | Low friction install; large top of funnel | Conversion often low; must protect premium value | Subscription or non-consumable | _ |
| **Ads (banner/interstitial/rewarded)** | High-volume, ad-tolerant audiences | No purchase friction; monetizes free users | Low ARPU; UX cost; needs consent + Ad ID handling | Not Play Billing (ad SDK) | _ |
| **Hybrid (e.g., free + ads + remove-ads IAP + subscription)** | Apps spanning casual + committed users | Captures multiple willingness-to-pay segments | Complexity; conflicting incentives | Mix of the above | _ |

> **CHECKPOINT 1 — Model lock.** Present the scored matrix and a single recommended model (or hybrid) with rationale tied to *this* app's value-delivery shape and audience. Do not design the catalog until the user confirms the model.

### Phase 2: Entitlement Model & Free/Paid Cut Line

Define what each tier unlocks. The entitlement model is the contract between "what the user paid for" and "what the app enforces."

```
Tier definition table:

| Entitlement key      | Free | Premium (monthly/annual) | Pro / one-time |
|----------------------|------|--------------------------|----------------|
| core_feature_a       |  ✅  |           ✅             |       ✅       |
| unlimited_items      |  ❌ (cap 10) |    ✅             |       ✅       |
| cloud_sync           |  ❌  |           ✅             |       ❌       |
| advanced_export      |  ❌  |           ✅             |       ✅       |
| no_ads               |  ❌  |           ✅             |       ✅       |
```

Cut-line rules to apply:
- **Free tier must be genuinely useful** (drives installs, retention, word of mouth) but must leave a clear reason to upgrade.
- **Premium must protect a real value moment** — the thing users hit *after* they're invested.
- Map every entitlement to a single named key (e.g., `cloud_sync`) — these keys, not product IDs, are what the app checks. Products grant entitlements; the app never checks product IDs directly in feature code.

### Phase 3: Play Billing Product Catalog Design

Design the exact catalog you will create in Play Console. Use stable, namespaced product IDs (lowercase, dot/underscore separated; **IDs are permanent and cannot be reused after deletion**).

**Subscriptions** (each subscription has one or more **base plans**; each base plan can have **offers**):

| Subscription ID | Base plan(s) | Billing period | Offer(s) | Grants entitlements |
|-----------------|--------------|----------------|----------|---------------------|
| `premium` | `monthly` | P1M | none | `unlimited_items`, `cloud_sync`, `advanced_export`, `no_ads` |
| `premium` | `annual` | P1Y | `freetrial` (7-day free trial), `intro` (intro price first year) | same as above |

Offer types to specify per base plan:

| Offer type | Use | Eligibility |
|------------|-----|-------------|
| **Free trial** | Let new users try premium (e.g., 7 days) | New subscribers only (set eligibility to prevent re-trialing) |
| **Introductory price** | Discounted first N periods | New subscribers |
| **Developer-determined / win-back** | Re-acquire churned users | Lapsed subscribers |

**Prepaid plans** (no auto-renew; user "tops up" access for a fixed window — good for regions/audiences that prefer no recurring charge):

| Subscription ID | Prepaid base plan | Access window | Grants |
|-----------------|-------------------|---------------|--------|
| `premium` | `prepaid_30d` | 30 days | premium entitlements for the window |

**One-time products:**

| Product ID | Type | Grants | Notes |
|------------|------|--------|-------|
| `pro_unlock` | Non-consumable | `unlimited_items`, `advanced_export`, `no_ads` | Restored on reinstall via `queryPurchasesAsync` |
| `coins_500` | Consumable | +500 coins | Must be *consumed* server-side after credit, else not repurchasable |

> **CHECKPOINT 2 — Catalog lock.** Present the full catalog (IDs, base plans, offers, prepaid, one-time) and the entitlement mapping. Confirm IDs are final before proceeding — IDs are permanent.

### Phase 4: Paywall Placement & Trigger Strategy

Decide *where* and *when* the upgrade prompt appears. Different placements suit different models.

| Placement | Trigger | Best for | Risk |
|-----------|---------|----------|------|
| **Onboarding paywall** | Right after sign-up / first launch | Subscription apps with obvious value | Can suppress installs/retention if too early |
| **Value-moment / contextual** | When user hits a premium feature or the free cap (e.g., "you've reached 10 items") | Freemium, most apps | Requires good event instrumentation to find the moment |
| **Hard gate** | Feature is fully locked until purchase | Pro tools, B2B | Highest friction; only when value is pre-established |
| **Soft/dismissible** | Banner or modal user can skip | Ad-supported + upgrade | Lower conversion, preserves goodwill |

Specify, for this app:
- Primary paywall placement + 1–2 secondary triggers (tie each to a measurable event — coordinate with the analytics measurement plan).
- What the paywall screen shows: tier comparison, trial framing, restore-purchases entry point (required UX), and a clear price + renewal disclosure.
- Trial framing and **cancellation transparency** (Play policy and user trust both require clear "renews at X / cancel anytime" copy).

### Phase 5: Pricing & Regional Pricing

| Decision | Plan |
|----------|------|
| Anchor price (primary market) | e.g., `premium/monthly` = $X.99; `premium/annual` = $Y (≈ N months free) |
| Annual discount | Annual should beat 12× monthly to incentivize commitment |
| Regional pricing | Use Play Console's localized pricing; let Play suggest purchasing-power-adjusted prices per country rather than a flat FX conversion |
| Price-ending convention | Keep consistent charm pricing across locales where Play allows |
| Tax & display | Play handles tax collection/remittance for digital goods in supported regions; plan displayed-price expectations accordingly |
| Price changes | Plan how existing subscribers are treated on price change (Play has opt-in/notice rules) |

### Phase 6: Server-Side Verification & Entitlement Source of Truth

**Never trust the client to decide entitlements.** Specify the authority chain:

```
Purchase flow (planning view):

[Client] BillingClient.launchBillingFlow → user pays
   → onPurchasesUpdated returns Purchase + purchaseToken
   → Client sends purchaseToken to YOUR backend (do NOT grant locally)
        → Backend verifies token via Google Play Developer API
          (purchases.subscriptionsv2.get / purchases.products.get)
        → Backend records entitlement in source-of-truth DB
        → Backend ACKNOWLEDGES the purchase within the required window
          (un-acknowledged purchases are auto-refunded)
   → Client reads entitlements from backend (or signed claim), gates features

Ongoing state (the part most apps get wrong):
[Google] Real-Time Developer Notifications (RTDN) via Pub/Sub
   → renewals, cancellations, grace period, account hold, refunds, revocations
   → Backend updates entitlement state from RTDN (NOT from the client)
```

Specify in the plan:

| Concern | Decision |
|---------|----------|
| **Source of truth** | Backend DB keyed by user + entitlement (preferred). If no backend yet, document that client-only verification is a *temporary* state and a known risk. |
| **Verification API** | Google Play Developer API (`subscriptionsv2`, `products`) for token validation |
| **Acknowledgement** | Every purchase must be acknowledged within the required window or it is refunded — assign an owner for this in the design |
| **Consumables** | Consume server-side only after crediting the user, to prevent double-credit/lost-purchase |
| **RTDN** | Subscribe to Real-Time Developer Notifications via Cloud Pub/Sub for renewal/cancel/refund/hold events |
| **Restore purchases** | On reinstall/new device, reconcile via `queryPurchasesAsync` + backend, not local cache |

### Phase 7: Lifecycle — Grace Period, Account Hold, Refunds

Plan the unhappy paths now:

| State | What it means | Plan |
|-------|---------------|------|
| **Grace period** | Payment failed but Play is retrying; user *keeps* access | Keep entitlement active; prompt user to fix payment (driven by RTDN) |
| **Account hold** | Retry window expired; access should be *revoked* until fixed | Revoke entitlement; show recovery UI; restore on resolution |
| **Pause** | User paused subscription (where enabled) | Suspend entitlement for the pause window |
| **Refund / chargeback / revoke** | Play or you refunded | Revoke entitlement on RTDN revocation event; never leave access granted after refund |
| **Upgrade/downgrade/proration** | User switches base plan | Specify proration mode and which entitlements change when |

> **CHECKPOINT 3 — Verification & lifecycle review.** Confirm the source of truth, acknowledgement owner, RTDN handling, and grace/hold behavior are all specified before declaring the plan complete.

---

## Expected Output

1. **Monetization Model Decision** — scored matrix + chosen model/hybrid with rationale.
2. **Entitlement Model** — named entitlement keys + free/paid cut-line table.
3. **Play Billing Product Catalog** — subscriptions (base plans + offers), prepaid plans, one-time products, with final product IDs and entitlement mapping.
4. **Paywall Strategy** — placement(s), triggers tied to events, and required UX (restore, disclosure, trial framing).
5. **Pricing Plan** — anchor prices, annual discount, regional-pricing approach.
6. **Verification & Source-of-Truth Plan** — backend authority, Play Developer API usage, acknowledgement owner, RTDN subscription, consumable handling.
7. **Lifecycle Plan** — grace period, account hold, pause, refund/revoke, proration behavior.
8. **Policy Notes** — confirmation that digital goods use Play Billing; any external-billing ambitions flagged for policy review.

---

## CRITICAL: Verification Requirements

- [ ] A single monetization model (or deliberate hybrid) is chosen with a documented rationale, not left open
- [ ] Every premium feature maps to a named entitlement key; feature code checks entitlements, never raw product IDs
- [ ] The product catalog uses final, stable, namespaced product IDs (acknowledged as permanent)
- [ ] Subscriptions are modeled correctly as base plan(s) + offer(s); trials/intro pricing have eligibility rules
- [ ] Prepaid and/or one-time products are specified where the audience/model warrants them
- [ ] The paywall has a defined primary placement plus event-tied triggers, and includes a restore-purchases path
- [ ] Regional pricing uses Play's purchasing-power-adjusted pricing, not flat FX conversion
- [ ] The entitlement source of truth is a server/backend (or client-only is explicitly flagged as temporary risk)
- [ ] Purchase verification uses the Google Play Developer API; acknowledgement-within-window has a named owner
- [ ] RTDN (Real-Time Developer Notifications) is part of the plan for renewal/cancel/refund/hold state
- [ ] Grace period, account hold, refund/revoke, and proration behavior are all specified
- [ ] The plan confirms Play Billing is used for digital goods; any external-billing path is flagged for policy review

## False-Positive Prevention

- ❌ Do NOT grant entitlements on the client based on `onPurchasesUpdated` alone — that is spoofable
- ✅ DO treat the backend (verified via Play Developer API + RTDN) as the source of truth
- ❌ Do NOT assume "subscription" is always right — a one-time unlock may fit a tool with no ongoing cost better
- ✅ DO match the model to whether value/cost is one-time or continuous
- ❌ Do NOT forget to acknowledge purchases — un-acknowledged purchases are auto-refunded and the user loses access
- ✅ DO assign an explicit owner and window for purchase acknowledgement
- ❌ Do NOT check raw product IDs inside feature code — catalogs change and IDs multiply
- ✅ DO gate features on stable entitlement keys that products grant
- ❌ Do NOT plan to route in-app digital purchases through a non-Play processor "to save fees" without a policy review
- ✅ DO assume Play Billing for digital goods and flag external-billing ambitions as a separate policy item
- ❌ Do NOT ignore grace period vs. account hold — silently revoking on first failed payment angers paying users
- ✅ DO keep access during grace period and revoke only on account hold/refund per RTDN
- ❌ Do NOT write full billing implementation code here — this is the plan that the implementation prompt consumes
- ✅ DO produce a catalog + verification spec precise enough to implement directly afterward

## Techniques Used

- **ST-01** (Clear Objective): Focused on producing a monetization + billing plan, not implementation
- **ST-02** (Structured Sequential Instructions): Model → entitlements → catalog → paywall → pricing → verification → lifecycle
- **RT-02** (Multi-Dimensional Analysis): Scores models across fit, pros, cons, and Play Billing objects
- **AG-02** (Skeptical Default Stance): Treats the client as untrusted; requires server-side verification
- **CM-01** (Explicit Context Framing): Gathers app type, audience, and goals before recommending
- **NE-02** (Phased Workflow Architecture): Checkpoint gates at model, catalog, and verification

## Related Prompts

- [android_app_concept_validation.md](android_app_concept_validation.md) — Validate the concept and rough business model before designing the catalog
- [../implementation/android_in_app_billing.md](../implementation/android_in_app_billing.md) — Implement the billing flow against this catalog and verification plan
- [../publishing/android_play_store_optimization.md](../publishing/android_play_store_optimization.md) — Optimize the store listing and conversion once the monetization model is set
