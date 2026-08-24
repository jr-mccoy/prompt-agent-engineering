---
title: "Firebase Cost Monitoring Setup"
category: mobile-development
description: "Set up comprehensive Firebase cost monitoring with GCP budget alerts, anomaly detection, and emergency cost-circuit-breaker patterns to prevent surprise bills"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - android
  - firebase
  - cost-management
  - gcp
  - mobile-development
  - solo-developer
updated: "2026-02-11"
---

# Firebase Cost Monitoring Setup

**Objective:** Set up comprehensive Firebase cost monitoring and alerting for an Android app, including GCP budget alerts at multiple thresholds, per-service usage dashboards, anomaly detection, and emergency cost-circuit-breaker patterns to prevent catastrophic surprise bills.

**When to Use:** Use this prompt when setting up a new Firebase project, when migrating from Spark (free) to Blaze (pay-as-you-go) plan, after experiencing unexpected charges, or as a periodic cost governance review. Critical for any solo developer or small team where a $70K surprise bill could end the business. Apply this before any production launch on the Blaze plan.

---

## Context Gathering

Before setting up cost monitoring, gather essential context:

1. **Firebase Project Details:**
   - "What Firebase services are you using (Firestore, Realtime Database, Cloud Functions, Storage, Hosting, Auth, Analytics, Crashlytics)?"
   - "Are you on the Spark (free) or Blaze (pay-as-you-go) plan?"
   - "Do you have multiple Firebase projects (dev/staging/prod)?"

2. **Current Usage:**
   - "What is your current monthly Firebase spend?"
   - "Which service is your largest cost driver?"
   - "Do you know your current read/write volumes?"

3. **Budget Constraints:**
   - "What is your maximum acceptable monthly Firebase cost?"
   - "At what dollar amount would you consider the spend an emergency?"
   - "Do you have GCP billing export set up already?"

4. **Architecture:**
   - "Do you use real-time listeners or one-time reads primarily?"
   - "Do you have Cloud Functions that trigger other Cloud Functions?"
   - "Do you use Firebase Extensions?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending ANY monitoring configuration, you MUST:**

1. **Understand the actual billing model** - Firebase billing is complex. Firestore charges per read/write/delete operation AND storage. Cloud Functions charge per invocation, compute time, AND networking. Don't conflate these.
2. **Check free tier limits** - Many Firebase services have generous free tiers on the Blaze plan. Don't alarm the user about costs that fall within free usage.
3. **Verify the service is actually in use** - Don't set up monitoring for services the project doesn't use.
4. **Consider the billing plan** - Spark plan has hard limits (no overage possible). Blaze plan has free tier + pay-as-you-go. Recommendations differ.
5. **Provide specific GCP console paths** - Every setup step must include the exact console navigation path or gcloud CLI command.

**Finding that costs are well-controlled is an acceptable outcome.** If existing monitoring is adequate, say so.

### False-Positive Prevention

- ❌ Do NOT create panic about costs when usage is within free tier limits
- ❌ Do NOT recommend overly aggressive alerts that cause notification fatigue
- ❌ Do NOT suggest disabling services as a "cost control" when the service is essential
- ❌ Do NOT assume all real-time listeners are wasteful — some are core to the product
- ✅ DO calculate whether current usage actually exceeds free tier
- ✅ DO provide specific dollar amounts, not vague warnings
- ✅ DO explain the billing model for each service before recommending monitoring
- ✅ DO distinguish between expected growth costs and anomalous spikes

---

### Phase 1: Firebase Billing Fundamentals Review

Establish baseline understanding of the project's cost structure.

#### 1.1 Service-by-Service Cost Model

For each Firebase service in use, document:

```
Service: [Name]
Billing Dimensions:
  - [Dimension 1]: [Unit] at [Rate]
  - [Dimension 2]: [Unit] at [Rate]
Free Tier Allowance:
  - [Dimension 1]: [Amount]/month
  - [Dimension 2]: [Amount]/month
Current Usage Estimate:
  - [Dimension 1]: [Amount]/month → $[Cost]
  - [Dimension 2]: [Amount]/month → $[Cost]
Risk Level: [Low/Medium/High/Critical]
```

**Key Firebase pricing to review:**

| Service | Primary Cost Drivers | Common Surprise Bill Causes |
|---------|--------------------|-----------------------------|
| **Firestore** | Reads, writes, deletes, storage, network egress | Unoptimized queries, missing indexes causing full scans, real-time listeners on large collections |
| **Realtime Database** | Connections, storage, downloads | Too many concurrent connections, large data downloads on app start |
| **Cloud Functions** | Invocations, compute time (GB-seconds), networking | Infinite loops (Function A triggers B triggers A), cold starts, unoptimized execution |
| **Cloud Storage** | Storage volume, operations, network egress | Uncompressed uploads, no lifecycle policies, public bucket abuse |
| **Hosting** | Storage, data transfer | CDN egress spikes from viral traffic |
| **Authentication** | Phone auth (SMS costs), SAML/OIDC | Phone verification abuse without rate limiting |

#### 1.2 Free Tier Baseline

Document what's covered at no cost:

```
Firestore Free Tier (Blaze plan):
- 50,000 reads/day
- 20,000 writes/day
- 20,000 deletes/day
- 1 GiB storage
- 10 GiB/month network egress

Cloud Functions Free Tier:
- 2,000,000 invocations/month
- 400,000 GB-seconds/month
- 200,000 GHz-seconds/month
- 5 GB network egress/month

Cloud Storage Free Tier:
- 5 GB storage
- 50,000 downloads/day
- 20,000 uploads/day
```

**Note:** Free tier limits are subject to change. Always verify against current Firebase pricing documentation.

---

### Phase 2: GCP Budget Alerts Configuration

Set up tiered budget alerts in Google Cloud Console.

#### 2.1 Budget Creation

**Navigate to:** GCP Console → Billing → Budgets & Alerts → Create Budget

**Recommended budget alert thresholds for a solo developer:**

| Threshold | Amount | Alert Channel | Purpose |
|-----------|--------|---------------|---------|
| **1%** | ~$0.50 on $50 budget | Email | "You've left free tier" early warning |
| **25%** | ~$12.50 on $50 budget | Email | Normal growth checkpoint |
| **50%** | ~$25 on $50 budget | Email + Slack/Discord | Mid-month review trigger |
| **75%** | ~$37.50 on $50 budget | Email + Slack/Discord | Approaching limit warning |
| **100%** | $50 | Email + Slack/Discord + SMS | Budget reached — investigate immediately |
| **150%** | $75 | Email + SMS + PagerDuty | Anomaly — possible runaway process |
| **300%** | $150 | All channels + auto-disable trigger | Emergency — activate circuit breaker |

**gcloud CLI setup:**

```bash
# Create a budget with alerts
gcloud billing budgets create \
  --billing-account=BILLING_ACCOUNT_ID \
  --display-name="Firebase Production Budget" \
  --budget-amount=50.00USD \
  --threshold-rule=percent=0.01,basis=current-spend \
  --threshold-rule=percent=0.25,basis=current-spend \
  --threshold-rule=percent=0.50,basis=current-spend \
  --threshold-rule=percent=0.75,basis=current-spend \
  --threshold-rule=percent=1.0,basis=current-spend \
  --threshold-rule=percent=1.5,basis=current-spend \
  --threshold-rule=percent=3.0,basis=current-spend \
  --all-updates-rule-pubsub-topic=projects/PROJECT_ID/topics/billing-alerts
```

#### 2.2 Notification Channel Setup

**Email alerts (automatic):** Budget alerts go to billing admins by default.

**Pub/Sub integration for programmatic response:**

```bash
# Create a Pub/Sub topic for billing alerts
gcloud pubsub topics create billing-alerts --project=PROJECT_ID

# Create a subscription for processing
gcloud pubsub subscriptions create billing-alerts-sub \
  --topic=billing-alerts \
  --project=PROJECT_ID
```

**Cloud Function to forward alerts to Slack/Discord:**

```typescript
// functions/src/billing-alert.ts
import * as functions from "firebase-functions";

export const billingAlert = functions.pubsub
  .topic("billing-alerts")
  .onPublish(async (message) => {
    const data = message.json;
    const costAmount = data.costAmount;
    const budgetAmount = data.budgetAmount;
    const percentUsed = (costAmount / budgetAmount * 100).toFixed(1);

    const alertMessage = {
      text: `Firebase Cost Alert: $${costAmount.toFixed(2)} / $${budgetAmount.toFixed(2)} (${percentUsed}%)`,
    };

    // Send to Slack webhook
    await fetch(process.env.SLACK_WEBHOOK_URL!, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(alertMessage),
    });
  });
```

---

### Phase 3: Per-Service Monitoring Dashboards

Set up Cloud Monitoring dashboards for granular visibility.

#### 3.1 Firestore Monitoring

**Key metrics to track:**

| Metric | Dashboard Widget | Alert Threshold |
|--------|-----------------|-----------------|
| `firestore.googleapis.com/document/read_count` | Time series graph | > 2x daily average |
| `firestore.googleapis.com/document/write_count` | Time series graph | > 2x daily average |
| `firestore.googleapis.com/document/delete_count` | Time series graph | > 5x daily average |
| Active connections | Gauge | > expected concurrent users |

#### 3.2 Cloud Functions Monitoring

**Key metrics to track:**

| Metric | Dashboard Widget | Alert Threshold |
|--------|-----------------|-----------------|
| `cloudfunctions.googleapis.com/function/execution_count` | Time series per function | > 3x hourly average |
| `cloudfunctions.googleapis.com/function/execution_times` | Heatmap | p95 > 10s (cost driver) |
| Active instances | Gauge | > maxInstances setting |
| Error rate | Time series | > 5% of invocations |

#### 3.3 Cloud Storage Monitoring

**Key metrics to track:**

| Metric | Dashboard Widget | Alert Threshold |
|--------|-----------------|-----------------|
| Total storage bytes | Gauge | Approaching lifecycle policy threshold |
| `storage.googleapis.com/network/sent_bytes_count` | Time series | > 2x daily average |
| Object count | Gauge | Unexpected growth |

---

### Phase 4: Anomaly Detection and Circuit Breakers

Protect against runaway costs with automated responses.

#### 4.1 Cloud Functions Infinite Loop Prevention

**The most dangerous cost scenario:** Function A writes to Firestore → triggers Function B → which writes to Firestore → triggers Function A → infinite loop.

**Prevention patterns:**

```typescript
// Pattern 1: Idempotency check with processed flag
export const onDocumentUpdate = functions.firestore
  .document("items/{itemId}")
  .onWrite(async (change, context) => {
    const data = change.after.data();

    // Prevent re-trigger: check if this function already processed this change
    if (data?.lastProcessedBy === "onDocumentUpdate") {
      console.log("Already processed, skipping to prevent loop");
      return null;
    }

    // Do work...
    await change.after.ref.update({
      lastProcessedBy: "onDocumentUpdate",
      lastProcessedAt: admin.firestore.FieldValue.serverTimestamp(),
    });
  });

// Pattern 2: Max invocation counter
export const processItem = functions.firestore
  .document("items/{itemId}")
  .onWrite(async (change, context) => {
    const data = change.after.data();
    const processCount = data?.processCount || 0;

    if (processCount > 3) {
      console.error("Max process count exceeded, possible loop detected");
      return null;
    }

    // Do work...
  });
```

**Set maxInstances to limit blast radius:**

```typescript
export const expensiveFunction = functions
  .runWith({
    maxInstances: 10,    // Hard cap on concurrent executions
    timeoutSeconds: 60,  // Don't let functions run forever
    memory: "256MB",     // Don't over-provision memory
  })
  .firestore.document("path/{id}")
  .onWrite(async (change, context) => {
    // ...
  });
```

#### 4.2 Emergency Cost Circuit Breaker

**A Cloud Function that can disable billing when costs exceed emergency threshold:**

```typescript
// WARNING: Disabling billing will stop ALL Firebase services
// Only use as absolute last resort
// This is the "break glass" option

import { CloudBillingClient } from "@google-cloud/billing";

export const emergencyCostBreaker = functions.pubsub
  .topic("billing-alerts")
  .onPublish(async (message) => {
    const data = message.json;
    const costAmount = data.costAmount;
    const budgetAmount = data.budgetAmount;

    // Only trigger at 300% of budget (emergency threshold)
    if (costAmount <= budgetAmount * 3) {
      return;
    }

    console.error(`EMERGENCY: Cost $${costAmount} exceeds 3x budget $${budgetAmount}`);

    // Option A: Disable billing (NUCLEAR OPTION - stops everything)
    // const billing = new CloudBillingClient();
    // await billing.updateProjectBillingInfo({
    //   name: `projects/${PROJECT_ID}`,
    //   projectBillingInfo: { billingEnabled: false },
    // });

    // Option B: Disable specific expensive functions (SAFER)
    // Use Cloud Functions API to disable specific functions

    // Option C: Alert aggressively and let human decide
    await sendEmergencyAlert(costAmount, budgetAmount);
  });
```

**Important:** Disabling billing will make your app non-functional. For most solo developers, aggressive alerting (Option C) is better than automated shutdown. Discuss with yourself what threshold truly justifies killing the app vs. eating the cost.

#### 4.3 Firestore Read Spike Protection

For apps where a bug or viral traffic could cause millions of reads:

```typescript
// Rate-limit client reads using a Cloud Function proxy
// instead of direct Firestore access for expensive collections
export const getExpensiveData = functions.https.onCall(async (data, context) => {
  if (!context.auth) throw new functions.https.HttpsError("unauthenticated", "");

  // Check rate limit (using a simple counter in Firestore)
  const rateLimitRef = admin.firestore()
    .doc(`rateLimits/${context.auth.uid}`);
  const rateLimit = await rateLimitRef.get();
  const requestCount = rateLimit.data()?.count || 0;
  const lastReset = rateLimit.data()?.lastReset?.toMillis() || 0;

  // Reset counter every hour
  if (Date.now() - lastReset > 3600000) {
    await rateLimitRef.set({ count: 1, lastReset: admin.firestore.FieldValue.serverTimestamp() });
  } else if (requestCount > 100) {
    throw new functions.https.HttpsError("resource-exhausted", "Rate limit exceeded");
  } else {
    await rateLimitRef.update({ count: admin.firestore.FieldValue.increment(1) });
  }

  // Proceed with the expensive query
  return await fetchExpensiveData(data);
});
```

---

### Phase 5: Ongoing Cost Review Process

Establish a sustainable cost review cadence.

#### 5.1 Weekly Cost Check (5 minutes)

```
Every Monday morning:
1. Open GCP Console → Billing → Reports
2. Check: Is this week's spend on track with budget?
3. Check: Any single service spiking unexpectedly?
4. Check: Are Cloud Functions invocation counts normal?
5. Action: If anything unusual, investigate before it compounds
```

#### 5.2 Monthly Cost Review (30 minutes)

```
First of each month:
1. Review total spend vs. budget
2. Compare to previous month (>20% increase needs investigation)
3. Check per-service breakdown:
   - Firestore: reads, writes, storage
   - Functions: invocations, compute time
   - Storage: volume, egress
4. Review: Are any services approaching paid tier from free tier?
5. Optimize: Convert any real-time listeners that could be one-time reads
6. Optimize: Check Cloud Functions execution times — any > 5s that could be faster?
7. Plan: Project next month's costs based on user growth
```

#### 5.3 Cost Optimization Quick Wins

| Optimization | Potential Savings | Effort |
|-------------|-------------------|--------|
| Replace real-time listeners with polling for non-critical data | 30-70% read reduction | Medium |
| Add client-side caching with TTL | 40-60% read reduction | Low |
| Batch Firestore writes | 20-30% write cost reduction | Low |
| Optimize Cloud Functions cold starts (smaller packages) | 15-25% compute reduction | Medium |
| Set Cloud Functions maxInstances | Caps worst-case cost | Low |
| Use Firestore bundle for common queries | 50-80% read reduction for cached data | Medium |
| Delete unused indexes | Reduces storage costs | Low |
| Set Storage lifecycle policies | Automatic old data cleanup | Low |

---

## Expected Output

### Firebase Cost Monitoring Report

```markdown
# Firebase Cost Monitoring Setup Report

## Project Overview
- **Project:** [Project name]
- **Plan:** Blaze (pay-as-you-go)
- **Services in use:** [List]
- **Current monthly spend:** $[Amount]
- **Budget set:** $[Amount]/month

## Cost Baseline

| Service | Monthly Usage | Free Tier | Overage | Monthly Cost |
|---------|-------------|-----------|---------|--------------|
| Firestore | [X] reads/day | 50K/day | [Y] reads | $[Amount] |
| Cloud Functions | [X] invocations | 2M/month | [Y] invocations | $[Amount] |
| Storage | [X] GB | 5 GB | [Y] GB | $[Amount] |
| **Total** | | | | **$[Amount]** |

## Monitoring Configuration

### Budget Alerts
| Threshold | Amount | Channel | Status |
|-----------|--------|---------|--------|
| 1% | $[X] | Email | ✅ Configured |
| 25% | $[X] | Email | ✅ Configured |
| 50% | $[X] | Email + Slack | ✅ Configured |
| 100% | $[X] | Email + Slack + SMS | ✅ Configured |
| 150% | $[X] | All channels | ✅ Configured |
| 300% | $[X] | Emergency alert | ✅ Configured |

### Dashboard Metrics
- [X] Firestore read/write tracking
- [X] Cloud Functions invocation monitoring
- [X] Storage egress tracking
- [X] Error rate alerting

### Circuit Breakers
- [X] Cloud Functions maxInstances set
- [X] Infinite loop prevention patterns applied
- [X] Emergency cost breaker configured at [X]x budget
- [X] Rate limiting on expensive operations

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Cloud Functions infinite loop | Low | Critical ($1000s/hour) | maxInstances + loop detection |
| Firestore read spike from bug | Medium | High ($100s/day) | Client caching + rate limits |
| Storage egress from viral traffic | Low | Medium ($10s/day) | CDN + lifecycle policies |

## Optimization Recommendations

1. [Recommendation with estimated savings]
2. [Recommendation with estimated savings]
3. [Recommendation with estimated savings]

## Review Schedule
- **Weekly:** 5-minute spend check every Monday
- **Monthly:** 30-minute cost review on the 1st
- **Quarterly:** Full cost optimization audit
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Cost monitoring focus
- **ST-02** (Structured Sequential Instructions) - Phased setup process
- **RT-02** (Multi-Dimensional Analysis) - Per-service cost analysis
- **CM-01** (Explicit Context Framing) - Firebase billing model context
- **DS-06** (Prioritization Guidance) - Alert threshold prioritization
- **QA-01** (Chain-of-Verification) - Cost calculation verification

---

## Related Prompts

- `android_firebase_security_rules_audit.md` - Security rules review (often interacts with cost)
- `cloud_cost_optimization.md` - General cloud cost optimization
- `mobile_cicd_pipeline_optimization.md` - CI/CD cost optimization
- `firebase_health_check.md` - Periodic Firebase health review (planned)

---

## Customization Guide

- **For apps still on Spark plan:** Focus on understanding when you'll need Blaze, and set up monitoring before switching
- **For apps with high read volumes:** Emphasize Firestore read monitoring and caching strategies
- **For apps with many Cloud Functions:** Emphasize invocation tracking, cold start optimization, and loop prevention
- **For multi-project setups (dev/staging/prod):** Set up per-project budgets; development projects often have looser budgets but still need monitoring
- **For apps approaching scale:** Consider BigQuery billing export for detailed cost attribution analysis
