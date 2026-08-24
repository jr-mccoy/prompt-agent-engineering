---
title: "Firebase Cloud Functions Cost Guard"
category: mobile-development
description: "Audit Cloud Functions for cost risks — infinite loop detection, excessive invocations, functions replaceable by security rules, unoptimized execution times, cold start costs, and cost calculation with monitoring setup"
techniques: [ST-01, ST-02, RT-02, CM-01, DS-06]
difficulty: intermediate
tags: [android, firebase, cloud-functions, cost-optimization, serverless, solo-developer]
updated: "2026-02-11"
---

# Firebase Cloud Functions Cost Guard

**Objective:** Audit all Cloud Functions in a Firebase project for cost risks and runaway spending potential — covering infinite loop detection (Function A triggers B triggers A), excessive invocation patterns, functions that could be replaced by security rules or client logic, unoptimized execution times, cold start overhead costs, and missing resource limits — producing a risk-ranked report with cost calculations, safe alternatives, and a monitoring plan to prevent bill surprises.

**When to Use:** Use this prompt before deploying Cloud Functions to production, after receiving a higher-than-expected Firebase bill, when adding new functions to an existing project, when a function appears to run more often than expected, or as a periodic (monthly) cost review. This is a defensive audit — its purpose is to find the function that will cost you $500 overnight before it does.

**Important context:** Cloud Functions are the #1 source of unexpected Firebase costs for solo developers and small teams. A single infinite loop between two Firestore-triggered functions can generate millions of invocations in minutes. Unlike Firestore reads (which have a free tier and predictable per-document pricing), Cloud Functions costs combine invocation count, compute time, memory allocation, and networking — making runaway costs harder to predict and faster to accumulate. The Firebase console does not alert you by default when costs spike.

---

## Context Gathering

Before auditing Cloud Functions, gather essential context:

1. **Function Inventory:**
   - "How many Cloud Functions do you have deployed?"
   - "Are you using 1st gen, 2nd gen, or a mix?"
   - "What trigger types are in use (Firestore, Auth, HTTP, Scheduled, Storage, Pub/Sub)?"
   - "Do you have `maxInstances` set on all functions?"

2. **Cost History:**
   - "What is your current monthly Cloud Functions spend?"
   - "Have you had any cost spikes or surprises?"
   - "Have you set a Firebase budget alert?"
   - "Are you within the free tier or exceeding it?"

3. **Trigger Chains:**
   - "Do any of your functions write to Firestore collections that other functions listen to?"
   - "Do any functions call other functions via HTTP or Pub/Sub?"
   - "Have you observed functions executing more than expected?"
   - "Do any functions trigger on `onWrite` or `onUpdate` (which fire on any change, including changes made by other functions)?"

4. **Development Practices:**
   - "Do you test functions locally with the Firebase Emulator Suite before deploying?"
   - "Do you have separate Firebase projects for dev and production?"
   - "How do you monitor function execution counts and errors?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before flagging ANY function as a cost risk, you MUST:**

1. **Map the complete trigger chain** — For every function that writes to Firestore, trace what other functions listen to that collection. Draw the chain. Look for cycles.
2. **Count actual invocations** — Check the Cloud Functions dashboard or Cloud Logging for real invocation counts. Do not assume based on expected traffic alone.
3. **Verify the function is actually unnecessary** — Before recommending removal, confirm the function's purpose cannot be served by security rules alone. Some validation logic genuinely requires server-side execution.
4. **Calculate real costs, not theoretical** — Use actual execution duration from Cloud Logging, not guesses. A function that runs for 100ms costs very differently from one that runs for 10 seconds.
5. **Check existing safeguards** — Before flagging missing `maxInstances`, check if it is already set. Before flagging loop risk, check if the function already has loop prevention logic.

### False-Positive Prevention

- Do NOT flag a Firestore-triggered function as a loop risk if it only writes to a DIFFERENT collection than it listens to and no other function listens to that target collection
- Do NOT recommend replacing a function with security rules if the function performs operations that security rules cannot do (external API calls, complex aggregations, sending notifications)
- Do NOT flag cold start costs as a problem for scheduled functions that run once a day — the cold start is irrelevant at that frequency
- Do NOT flag `maxInstances` as missing if the function is an HTTP/Callable function behind a rate limiter or API gateway
- Do NOT assume high invocation count means a problem — a function triggered 10,000 times per day is normal for an app with 10,000 DAU if it runs once per user session
- DO trace the complete write chain for every function that modifies Firestore
- DO compare invocation counts against expected user-driven events
- DO calculate the actual monthly cost before and after proposed changes
- DO check Cloud Logging for error rates that cause retries (failed functions retry automatically, doubling invocations)
- DO verify that `timeoutSeconds` is set appropriately — a function that finishes in 200ms but has a 540s timeout wastes resources if it hangs

---

### Phase 1: Function Inventory

#### 1.1 Catalog All Deployed Functions

For each deployed function, document:

```
Function: [name]
Generation: [1st gen / 2nd gen]
Trigger: [Type + path/topic/schedule]
Runtime: [Node.js version]
Memory: [128MB / 256MB / 512MB / 1GB / default?]
Timeout: [seconds / default?]
maxInstances: [number / NOT SET]
minInstances: [number / 0]
Region: [region]
Last deployed: [date]
Purpose: [What this function does]
Writes to: [Collections/services this function modifies]
```

#### 1.2 Risk Classification

| Risk Level | Criteria | Action |
|-----------|----------|--------|
| **CRITICAL** | Function has loop potential, no maxInstances, or writes to its own trigger collection | Fix immediately before next deploy |
| **HIGH** | Function has no timeout set, excessive memory allocation, or replaces a security-rule-solvable task | Fix within the week |
| **MEDIUM** | Function has suboptimal execution time, unnecessary dependencies, or cold start impact on UX | Fix when convenient |
| **LOW** | Minor optimization opportunities, documentation gaps | Track for next review |

---

### Phase 2: Loop Risk Analysis

This is the most critical phase. Infinite loops are the single largest cost risk in Cloud Functions.

#### 2.1 Trigger Chain Mapping

For every function, draw the trigger-to-write chain:

```
TRIGGER CHAIN MAP
=================

onOrderCreated (listens: orders/{orderId} onCreate)
  └─ Writes to: orders/{orderId} (updates status)
     └─ TRIGGERS: onOrderUpdated? ← Check if this function exists!

onOrderUpdated (listens: orders/{orderId} onUpdate)
  └─ Writes to: orders/{orderId} (updates total)
     └─ TRIGGERS: onOrderUpdated AGAIN ← INFINITE LOOP!

onUserCreated (listens: users/{userId} onCreate)
  └─ Writes to: users/{userId} (sets default fields)
     └─ TRIGGERS: Does NOT trigger (onCreate only fires on creation, not update) ← SAFE
```

#### 2.2 Dangerous Loop Patterns

**DANGER: Function A triggers Function B triggers Function A:**

```typescript
// DANGEROUS: Function A writes to collection B, Function B writes to collection A

// Function A: listens to "orders", writes to "inventory"
export const onOrderCreated = onDocumentCreated("orders/{orderId}", async (event) => {
  const items = event.data?.data()?.items;
  for (const item of items) {
    // Writes to inventory — triggers Function B
    await db.doc(`inventory/${item.productId}`).update({
      stock: FieldValue.increment(-item.quantity),
      lastOrderId: event.params.orderId,
    });
  }
});

// Function B: listens to "inventory", writes to "orders"
export const onInventoryUpdated = onDocumentUpdated("inventory/{productId}", async (event) => {
  const after = event.data?.after.data();
  if (after?.stock <= 0) {
    // Writes to orders — triggers Function A? No, only if it CREATES a new order.
    // But what if it does...
    await db.collection("orders").add({
      type: "restock",
      productId: event.params.productId,
      // THIS CREATES A NEW ORDER → TRIGGERS Function A → TRIGGERS Function B → LOOP!
    });
  }
});

// RESULT: If stock hits 0, Function B creates a restock order,
// which triggers Function A, which updates inventory,
// which triggers Function B, which creates another restock order...
// INFINITE LOOP — thousands of invocations per minute.
```

**SAFE: Rewritten with loop prevention:**

```typescript
// SAFE: Function B writes to a DIFFERENT collection that no function listens to

export const onInventoryUpdated = onDocumentUpdated("inventory/{productId}", async (event) => {
  const after = event.data?.after.data();
  const before = event.data?.before.data();

  // Guard 1: Only process if stock actually changed
  if (before?.stock === after?.stock) return;

  // Guard 2: Only process if stock dropped to or below reorder threshold
  if (after?.stock > after?.reorderThreshold) return;

  // Guard 3: Check if restock already requested (idempotency)
  if (after?.restockRequested === true) return;

  // Write to a separate collection that NO function listens to
  await db.collection("restockRequests").add({
    productId: event.params.productId,
    currentStock: after?.stock,
    requestedAt: FieldValue.serverTimestamp(),
  });

  // Mark as handled to prevent duplicate requests
  await event.data?.after.ref.update({ restockRequested: true });
});
// SAFE: restockRequests is not listened to by any function
// SAFE: The flag prevents re-triggering on the same document
```

**DANGER: Function triggers itself via onUpdate:**

```typescript
// DANGEROUS: Function listens to onUpdate, then updates the same document

export const calculateOrderTotal = onDocumentUpdated("orders/{orderId}", async (event) => {
  const after = event.data?.after.data();
  const items = after?.items || [];

  const total = items.reduce((sum: number, item: any) => sum + item.price * item.quantity, 0);

  // This UPDATE triggers THIS SAME FUNCTION again!
  await event.data?.after.ref.update({ total });
  // Loop: update total → triggers calculateOrderTotal → recalculates total → update total → ...
});
```

**SAFE: Self-trigger prevention:**

```typescript
// SAFE: Check if the field we care about actually changed

export const calculateOrderTotal = onDocumentUpdated("orders/{orderId}", async (event) => {
  const before = event.data?.before.data();
  const after = event.data?.after.data();

  // Guard: Only recalculate if items changed (not if total changed)
  if (JSON.stringify(before?.items) === JSON.stringify(after?.items)) {
    return; // Items didn't change — this was triggered by our own total update
  }

  const items = after?.items || [];
  const total = items.reduce((sum: number, item: any) => sum + item.price * item.quantity, 0);

  // Safe to update: this changes "total", not "items", so the guard above will prevent re-trigger
  await event.data?.after.ref.update({ total });
});
```

#### 2.3 Loop Risk Scoring

For each function, calculate a loop risk score:

| Factor | Score |
|--------|-------|
| Function uses `onUpdate` or `onWrite` trigger | +3 |
| Function writes to the SAME collection it listens to | +5 |
| Function writes to a collection another function listens to | +3 |
| No change detection guard (before vs after comparison) | +4 |
| No idempotency flag check | +2 |
| No `maxInstances` set | +3 |
| **Total risk score** | **[sum]** |

| Score | Risk Level | Action |
|-------|-----------|--------|
| 0-3 | Low | Acceptable |
| 4-7 | Medium | Add guards |
| 8-12 | High | Redesign before deploying |
| 13+ | Critical | DO NOT DEPLOY — fix immediately |

---

### Phase 3: Cost Calculation

#### 3.1 Cloud Functions Pricing Model

Cloud Functions pricing (verify at cloud.google.com/functions/pricing):

| Component | Free Tier (monthly) | Price Beyond Free |
|-----------|-------------------|-------------------|
| Invocations | 2,000,000 | $0.40 per million |
| Compute (GB-second) | 400,000 GB-s | $0.0000025 per GB-s |
| Compute (GHz-second) | 200,000 GHz-s | $0.0000100 per GHz-s |
| Networking (outbound) | 5 GB | $0.12 per GB |

#### 3.2 Per-Function Cost Formula

```
Monthly cost per function:

Invocation cost:
  = (monthly_invocations - free_tier_share) x $0.40 / 1,000,000

Compute cost (memory):
  GB_allocated = memory_MB / 1024
  GB_seconds = GB_allocated x avg_duration_seconds x monthly_invocations
  = (GB_seconds - free_tier_share) x $0.0000025

Compute cost (CPU):
  GHz_allocated = [based on memory tier, see docs]
  GHz_seconds = GHz_allocated x avg_duration_seconds x monthly_invocations
  = (GHz_seconds - free_tier_share) x $0.0000100

Total = invocation_cost + memory_cost + cpu_cost + networking_cost
```

#### 3.3 Cost Calculation Example

```
Function: sendNotificationOnComment
Memory: 256MB (0.25 GB → 0.4 GHz CPU)
Average duration: 300ms (0.3 seconds)
Monthly invocations: 50,000

Invocation cost:
  50,000 well within free tier (2M) → $0.00

Memory compute:
  0.25 GB x 0.3s x 50,000 = 3,750 GB-seconds
  Well within free tier (400,000 GB-s) → $0.00

CPU compute:
  0.4 GHz x 0.3s x 50,000 = 6,000 GHz-seconds
  Well within free tier (200,000 GHz-s) → $0.00

Total: $0.00 (within free tier)

──────────────────────────────

Function: processImageUpload
Memory: 1GB (1 GB → 1.4 GHz CPU)
Average duration: 8 seconds
Monthly invocations: 100,000

Invocation cost:
  100,000 within free tier → $0.00

Memory compute:
  1 GB x 8s x 100,000 = 800,000 GB-seconds
  Exceeds free tier: (800,000 - 400,000) x $0.0000025 = $1.00

CPU compute:
  1.4 GHz x 8s x 100,000 = 1,120,000 GHz-seconds
  Exceeds free tier: (1,120,000 - 200,000) x $0.0000100 = $9.20

Total: $10.20/month
```

#### 3.4 Worst-Case Scenario Calculation

For each function with loop risk, calculate the cost of a 1-hour runaway loop:

```
Function: [name]
Memory: [X] GB
Duration per invocation: [Y] seconds
Max instances: [N] (or UNLIMITED if not set)
Invocations per second (at max concurrency): [Z]

1-hour runaway cost:
  Invocations: Z x 3600 = [total]
  GB-seconds: X x Y x [total] = [gb_s]
  GHz-seconds: [cpu_ghz] x Y x [total] = [ghz_s]

  Invocation cost: [total] x $0.40 / 1,000,000 = $[A]
  Memory cost: [gb_s] x $0.0000025 = $[B]
  CPU cost: [ghz_s] x $0.0000100 = $[C]

  TOTAL 1-HOUR RUNAWAY COST: $[A + B + C]

With maxInstances=5:
  Invocations capped at: 5 x (3600 / Y) = [capped_total]
  CAPPED 1-HOUR COST: $[capped_cost]

  Savings from maxInstances: $[uncapped - capped]
```

---

### Phase 4: Optimization Plan

#### 4.1 Functions Replaceable by Security Rules

| Function | What It Does | Can Security Rules Do It? | Recommendation |
|----------|-------------|--------------------------|----------------|
| validateOrderData | Validates order fields on write | YES — rules can validate field types, ranges, required fields | **Remove function, use security rules** |
| checkUserOwnership | Verifies user owns the document | YES — `request.auth.uid == resource.data.userId` | **Remove function, use security rules** |
| enforceMaxDocSize | Rejects documents over a size | YES — `request.resource.data.text.size() < 10000` | **Remove function, use security rules** |
| sendWelcomeEmail | Sends email to new users | NO — security rules cannot make external API calls | **Keep function** |
| aggregateStats | Computes counters from subcollection | NO — security rules cannot read other documents for aggregation | **Keep function** |

**Security rules replacement example:**

```typescript
// BEFORE: Cloud Function for validation (costs per invocation)
export const validateOrder = onDocumentCreated("orders/{orderId}", async (event) => {
  const data = event.data?.data();
  if (!data?.items || data.items.length === 0) {
    await event.data?.ref.delete(); // Roll back invalid order
    return;
  }
  if (data.items.length > 50) {
    await event.data?.ref.delete();
    return;
  }
});
```

```javascript
// AFTER: Security rules (free, no cold start, no invocation cost)
match /orders/{orderId} {
  allow create: if request.auth != null
    && request.resource.data.items is list
    && request.resource.data.items.size() > 0
    && request.resource.data.items.size() <= 50
    && request.resource.data.userId == request.auth.uid;
}
```

#### 4.2 Execution Time Optimization

```typescript
// SLOW: Sequential external API calls
export const processOrder = onDocumentCreated("orders/{orderId}", async (event) => {
  const data = event.data?.data();

  // Sequential — each awaits before starting the next
  await sendConfirmationEmail(data);        // 500ms
  await updateInventory(data);              // 300ms
  await notifyWarehouse(data);              // 400ms
  await logAnalytics(data);                 // 200ms
  // Total: ~1400ms
});

// FAST: Parallel execution where possible
export const processOrderOptimized = onDocumentCreated("orders/{orderId}", async (event) => {
  const data = event.data?.data();

  // Parallel — all start at the same time
  await Promise.all([
    sendConfirmationEmail(data),        // 500ms ─┐
    updateInventory(data),              // 300ms  ├─ All run concurrently
    notifyWarehouse(data),              // 400ms  │
    logAnalytics(data),                 // 200ms ─┘
  ]);
  // Total: ~500ms (time of longest operation)
  // Cost reduction: ~64% less compute time
});
```

#### 4.3 Dependency Optimization

```typescript
// SLOW: Heavy imports increase cold start time
import * as admin from "firebase-admin";    // Imports EVERYTHING
import { BigQuery } from "@google-cloud/bigquery";  // Heavy SDK
import Stripe from "stripe";                         // Always loaded
import nodemailer from "nodemailer";                 // Always loaded

// FAST: Lazy imports — only load what you need, when you need it
import { getFirestore } from "firebase-admin/firestore";  // Specific import

// Lazy-loaded dependencies
let stripe: any = null;
function getStripe() {
  if (!stripe) {
    const Stripe = require("stripe");
    stripe = new Stripe(process.env.STRIPE_SECRET_KEY);
  }
  return stripe;
}

let mailer: any = null;
function getMailer() {
  if (!mailer) {
    const nodemailer = require("nodemailer");
    mailer = nodemailer.createTransport({ /* config */ });
  }
  return mailer;
}
```

#### 4.4 Resource Limit Enforcement

Every function MUST have explicit resource limits:

```typescript
// REQUIRED: Set limits on every function
export const myFunction = onDocumentCreated(
  {
    document: "collection/{docId}",
    maxInstances: 10,          // Prevent runaway scaling
    timeoutSeconds: 60,        // Kill hung functions
    memory: "256MiB",          // Don't over-allocate
    // minInstances: 0,        // Default, no always-on cost
    // cpu: 1,                 // For 2nd gen, explicit CPU
  },
  async (event) => {
    // Function logic
  }
);

// For HTTP/Callable functions facing users:
export const userFacingFunction = onCall(
  {
    maxInstances: 20,          // Allow more concurrency for user requests
    timeoutSeconds: 30,        // User-facing should be fast
    memory: "256MiB",
    // minInstances: 1,        // Consider for latency-critical endpoints
  },
  async (request) => {
    // Function logic
  }
);
```

---

### Phase 5: Monitoring Setup

#### 5.1 Firebase Budget Alerts

Configure budget alerts in Google Cloud Console:

```
Budget 1: Warning threshold
  Amount: $25/month (or your expected monthly spend x 2)
  Alert at: 50%, 90%, 100%
  Notify: Email to project owner

Budget 2: Emergency threshold
  Amount: $100/month (or your absolute maximum acceptable spend)
  Alert at: 100%
  Notify: Email + Pub/Sub topic (to trigger automatic shutdown function)
```

#### 5.2 Automatic Cost Circuit Breaker

```typescript
// Cloud Function that disables other functions when budget is exceeded
// Triggered by Pub/Sub from budget alert
import { onMessagePublished } from "firebase-functions/v2/pubsub";

export const budgetGuard = onMessagePublished(
  { topic: "budget-alerts", maxInstances: 1 },
  async (event) => {
    const data = event.data.message.json;

    const costAmount = data.costAmount;
    const budgetAmount = data.budgetAmount;

    if (costAmount > budgetAmount) {
      console.error(`BUDGET EXCEEDED: $${costAmount} > $${budgetAmount}`);

      // Option 1: Log and alert (least disruptive)
      await sendEmergencyAlert(costAmount, budgetAmount);

      // Option 2: Disable expensive functions (more aggressive)
      // This requires using the Cloud Functions API to disable functions
      // Use with caution — this can break app functionality
    }
  }
);
```

#### 5.3 Invocation Monitoring Dashboard

Set up Cloud Monitoring alerts for:

| Metric | Threshold | Alert |
|--------|-----------|-------|
| `cloudfunctions.googleapis.com/function/execution_count` | > 2x normal daily rate | Email warning |
| `cloudfunctions.googleapis.com/function/execution_times` | > 2x average duration | Email warning |
| `cloudfunctions.googleapis.com/function/active_instances` | = maxInstances | Email warning (at capacity) |
| Error rate | > 10% of invocations | Email + SMS |

#### 5.4 Logging Best Practices

```typescript
// Structured logging for cost tracking
export const trackedFunction = onDocumentCreated("items/{itemId}", async (event) => {
  const startTime = Date.now();

  try {
    // Function logic...
    await doWork(event.data?.data());

    // Log execution metrics
    console.log(JSON.stringify({
      function: "trackedFunction",
      trigger: `items/${event.params.itemId}`,
      duration_ms: Date.now() - startTime,
      status: "success",
    }));
  } catch (error) {
    console.error(JSON.stringify({
      function: "trackedFunction",
      trigger: `items/${event.params.itemId}`,
      duration_ms: Date.now() - startTime,
      status: "error",
      error: error instanceof Error ? error.message : "Unknown error",
    }));
    throw error; // Re-throw for retry if appropriate
  }
});
```

---

## Verification Requirements

After completing the audit, verify your findings:

1. **Loop verification** — For every function flagged as a loop risk, manually trace the trigger chain in code. Confirm the loop is real and not prevented by existing guards.
2. **Cost verification** — Cross-check your cost calculations against the Cloud Functions dashboard in Google Cloud Console. Ensure your invocation counts and durations match reality.
3. **Replacement verification** — For every function you recommend replacing with security rules, write the equivalent security rule and verify it handles all the cases the function handles. Security rules cannot make external calls, read documents outside the request, or perform complex computations.
4. **maxInstances verification** — Check that your recommended `maxInstances` values are high enough to handle legitimate traffic peaks. Setting it too low causes dropped events.
5. **Budget alert verification** — After setting up budget alerts, trigger a test alert to confirm notifications are received.

---

## Expected Output

### Cloud Functions Cost Guard Report

```markdown
# Cloud Functions Cost Guard Report: [App Name]

## Executive Summary
- **Functions audited:** [N]
- **Critical risks found:** [N]
- **Estimated current monthly spend:** $[X]
- **Estimated spend after optimization:** $[X]
- **Projected monthly savings:** $[X]
- **Worst-case runaway cost (1 hour, current):** $[X]
- **Worst-case runaway cost (1 hour, after fixes):** $[X]

## Function Inventory
| # | Function | Trigger | Memory | Timeout | maxInstances | Monthly Cost | Risk |
|---|----------|---------|--------|---------|-------------|-------------|------|
| 1 | [name] | [type] | [MB] | [s] | [N/NOT SET] | $[X] | Critical |
| 2 | [name] | [type] | [MB] | [s] | [N] | $[X] | Low |

## Trigger Chain Map
[ASCII diagram of all trigger chains with loop risks marked]

## Risk Findings

### CRITICAL: [Finding Name]
- **Function:** [name]
- **Risk:** [Infinite loop / No maxInstances / Self-trigger]
- **Severity:** Critical
- **Confidence:** High | Medium
- **Estimated runaway cost (1 hour):** $[X]
- **Before code:** [snippet showing dangerous pattern]
- **After code:** [snippet showing safe alternative]
- **Action required:** [specific fix]

### HIGH: [Finding Name]
[Same structure]

## Functions to Replace with Security Rules
| Function | Current Cost | Replacement | Savings |
|----------|-------------|-------------|---------|
| [name] | $[X]/month | Security rule | $[X]/month |

## Resource Limit Recommendations
| Function | Current maxInstances | Recommended | Current Timeout | Recommended |
|----------|---------------------|-------------|-----------------|-------------|
| [name] | NOT SET | [N] | default | [N]s |

## Cost Projection
| Scenario | Current | Optimized | Savings |
|----------|---------|-----------|---------|
| Normal month | $[X] | $[X] | $[X] |
| High traffic month | $[X] | $[X] | $[X] |
| 1-hour runaway | $[X] | $[X] | $[X] |

## Monitoring Checklist
- [ ] Budget alerts configured at 50%, 90%, 100% of expected spend
- [ ] Emergency budget alert with Pub/Sub notification
- [ ] Cloud Monitoring alerts for invocation spikes
- [ ] Error rate alerts configured
- [ ] maxInstances set on all functions
- [ ] Structured logging on all functions

## Prioritized Action Plan
| # | Action | Risk Reduced | Effort | Savings |
|---|--------|-------------|--------|---------|
| 1 | [Fix loop in Function X] | Critical → Low | Low | $[X] risk eliminated |
| 2 | [Set maxInstances on all functions] | High → Low | Low | $[X] risk cap |
| 3 | [Replace Function Y with security rule] | Medium → None | Medium | $[X]/month |
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused specifically on Cloud Functions cost risks and runaway spending, not general function design
- **ST-02** (Structured Sequential Instructions) — Phased approach: Inventory, Loop Risk Analysis, Cost Calculation, Optimization Plan, Monitoring Setup
- **RT-02** (Multi-Dimensional Analysis) — Each function analyzed across loop risk, cost, necessity, performance, and monitoring dimensions
- **CM-01** (Explicit Context Framing) — Cloud Functions pricing model and billing mechanics established upfront so cost calculations are grounded in reality
- **DS-06** (Prioritization Guidance) — Findings ranked by risk severity and cost impact, ensuring the highest-danger items are addressed first

---

## Related Prompts

- `firebase_cloud_functions_design.md` — Design new functions with safety patterns from the start
- `firebase_cost_optimization.md` — Broader Firebase cost optimization beyond just Cloud Functions
- `firebase_cost_monitor_setup.md` — Detailed monitoring setup for all Firebase services
- `firebase_health_check.md` — Periodic review that includes function cost and performance audit
- `firestore_data_model_design.md` — Data model changes that can eliminate the need for some functions
- `firebase_security_rules_generator.md` — Generate security rules to replace validation functions

---

## Customization Guide

- **For apps with many Firestore triggers:** Focus heavily on Phase 2 (Loop Risk Analysis). Map every trigger chain and verify every function that uses `onUpdate` or `onWrite`. These are the most dangerous trigger types because they fire on any change, including changes made by other functions.
- **For apps with image/file processing:** Cloud Storage triggers with image processing are the most expensive per-invocation functions due to high memory and long duration. Consider using Firebase Extensions (Resize Images) instead of custom functions, or offload to Cloud Run for better cost control.
- **For apps with scheduled functions:** Scheduled functions rarely cause cost surprises (they run at known intervals). Focus audit effort on event-triggered functions instead. But verify that scheduled cleanup functions have appropriate timeouts — a nightly cleanup that processes millions of documents can time out and retry indefinitely.
- **For apps calling external APIs:** External API calls add networking costs and increase execution time. Batch external calls where possible. Implement circuit breakers for external services that may be slow or down — a function waiting for a timeout on a dead API wastes compute time and money.
- **For apps migrating from 1st gen to 2nd gen:** 2nd gen functions have different concurrency behavior (multiple requests per instance). This changes the cost model significantly. A function that spawns 100 instances in 1st gen may only need 10 in 2nd gen with concurrency=10, reducing cold start costs dramatically.
