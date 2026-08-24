---
title: "Android Privacy & Data-Flow Audit"
category: mobile-development
description: "Maps an Android app's personal-data inventory and end-to-end data flows, audits third-party SDK/tracker data sharing, and reconciles actual behavior against the Play Data Safety declaration and privacy policy."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - QA-02
difficulty: advanced
tags:
  - android
  - privacy
  - data-flow
  - pii
  - third-party-sdk
  - data-safety
  - analysis
  - mobile-development
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_manifest_permissions_audit.md
  - domain-software-engineering/mobile/android/analysis/android_networking_layer_analysis.md
  - domain-software-engineering/mobile/android/publishing/play_store_data_safety_generator.md
---

# Android Privacy & Data-Flow Audit

**Objective:** Build a personal-data inventory for an Android app, map how each data type flows from collection to storage to transmission to third parties, audit the data-sharing behavior of bundled SDKs/trackers, and reconcile the *actual* behavior with the app's **Play Data Safety** declaration and privacy policy — reporting gaps, undisclosed sharing, and excessive collection with `file:line` evidence.

**When to Use:** Use this before a release or store submission, when completing/refreshing the Play Data Safety form, after adding an analytics/ads/attribution SDK, during a GDPR/CCPA readiness review, or when a privacy complaint or policy rejection needs investigation. This audit is about **data handling and disclosure** — distinct from the vulnerability-focused security audits and the legal/policy-text prompts in `publishing/`.

---

## Context Gathering

1. **Data types:** "What personal/sensitive data does the app intend to collect (account info, location, contacts, health, financial, photos, identifiers)?"
2. **Third parties:** "Which analytics, ads, crash, attribution, or backend SDKs are integrated?"
3. **Existing disclosures:** "Can you share the current Play Data Safety answers and the privacy policy?"
4. **Regulatory scope:** "Which regimes apply (GDPR, CCPA/CPRA, COPPA/children, HIPAA)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace each data type end-to-end** — from the collection point (UI/sensor/permission) through storage and into every network egress. Cite `file:line` at collection and transmission.
2. **Identify the real recipient** — distinguish first-party backend from third-party SDK endpoints; a value sent to an analytics SDK is *shared/collected by a third party*.
3. **Separate "collected" from "shared"** — Play distinguishes data processed on the app's behalf vs transferred to another company. Classify each accordingly.
4. **Reconcile against disclosures** — compare observed behavior to the Data Safety form and policy; flag both under-disclosure (undisclosed) and over-disclosure (declared but not collected).

**Finding the app's disclosures accurate is an acceptable outcome.** Don't fabricate sharing.

### False-Positive Prevention

- ❌ Do NOT label on-device-only data (never transmitted) as "shared."
- ❌ Do NOT count ephemeral, non-persisted diagnostic values toward "collected" without evidence of transmission/retention.
- ❌ Do NOT assume an SDK shares data without identifying the egress or citing its documented behavior.
- ❌ Do NOT flag data the user explicitly exports/sends as part of the core feature (e.g., a message they author).
- ✅ DO flag identifiers (Advertising ID, Android ID, IMEI-equivalents) sent to third parties.
- ✅ DO flag location/contacts/photos leaving the device undisclosed.
- ✅ DO flag mismatches between behavior and the Data Safety form.

---

### Phase 1: Personal-Data Inventory

| Data Type | Collection Point (file:line) | Sensitivity | Permission-gated? |
|-----------|------------------------------|-------------|-------------------|
| (Account, location, contacts, photos, identifiers, health, financial, usage…) | | | |

Categorize each against the Play Data Safety taxonomy (Personal info, Financial, Location, Messages, Photos/Videos, Files, App activity, Device/IDs, etc.).

---

### Phase 2: Data-Flow Mapping

For each data type, trace the path and classify the destination.

| Data Type | Stored Where | Transmitted To (endpoint/SDK) | First- or Third-Party | Encrypted in transit | Retention |
|-----------|--------------|-------------------------------|-----------------------|----------------------|-----------|

Look for egress points: Retrofit/OkHttp/Ktor calls, Firebase writes, analytics `logEvent`, ad requests, crash uploads, WebView, deep-link parameter leakage, log statements, and clipboard.

---

### Phase 3: Third-Party SDK & Tracker Audit

| SDK / Tracker | Purpose | Data Accessed | Shares Off-Device? | Collection vs Sharing | Configurable/Opt-out? |
|---------------|---------|---------------|--------------------|-----------------------|-----------------------|

- Identify SDKs from Gradle dependencies and initialization code.
- Note auto-initializing SDKs (manifest providers/`Initializer`) that collect before consent.
- Flag SDKs known to collect identifiers or behavioral data by default.

---

### Phase 4: Disclosure Reconciliation

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Undisclosed collection | CRITICAL | Data transmitted but absent from Data Safety form/policy |
| Undisclosed sharing | CRITICAL | Third-party transfer not declared as "shared" |
| Pre-consent collection | HIGH | Data/identifiers sent before consent in GDPR regions |
| Excessive collection | MEDIUM | Data collected with no feature using it |
| Over-disclosure | LOW | Declared data types not actually collected |
| Children's data | CRITICAL | Identifiers/behavioral data with a child-directed audience (COPPA/Families policy) |
| Account deletion path | MEDIUM | No in-app/web account & data deletion route (Play requirement) |

---

## Output Format

```markdown
## Android Privacy & Data-Flow Audit Report

### Data Inventory & Flow
| Data Type | Collected (file:line) | Destination | 1st/3rd party | Disclosed? |
|-----------|----------------------|-------------|---------------|------------|

### Third-Party SDK Sharing
| SDK | Data | Shares off-device | Disclosed as shared |
|-----|------|-------------------|---------------------|

### Findings (severity-ordered)
**[SEVERITY] title** — Location · Risk (privacy/regulatory/policy) · Fix

### Data Safety Form Reconciliation
- Should be marked Collected: …
- Should be marked Shared: …
- Remove (over-declared): …

### Prioritized Remediation (P1/P2/P3)
```

---

## Expected Output

1. **Data inventory** mapped to the Play taxonomy.
2. **End-to-end data-flow table** with destinations.
3. **Third-party sharing audit.**
4. **Disclosure reconciliation** + corrected Data Safety answers.
5. **Prioritized remediation.**

---

## Techniques Used

- **ST-01** (Clear Objective): Privacy/data-handling scope.
- **ST-02** (Structured Sequential Instructions): Inventory → flow → SDKs → reconciliation.
- **RT-02** (Multi-Dimensional Analysis): Engineering + regulatory + policy lenses.
- **RT-05** (Evidence-Based Reasoning): `file:line` at collection and egress.
- **DS-06** (Prioritization Guidance): Severity ordering.
- **QA-02** (Edge Case Coverage): Pre-consent init, children's data, deletion path.

---

## Related Prompts

- [android_manifest_permissions_audit.md](android_manifest_permissions_audit.md) - Permissions that gate data collection
- [android_networking_layer_analysis.md](android_networking_layer_analysis.md) - The transport carrying the data
- [play_store_data_safety_generator.md](../publishing/play_store_data_safety_generator.md) - Produce the corrected declaration
