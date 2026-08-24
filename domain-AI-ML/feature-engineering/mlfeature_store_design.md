---
title: "Feature Store Design"
category: AI-ML/feature-engineering
description: "Design a feature store with offline/online consistency so the same feature values are used for training and serving — eliminating train/serve skew at the source."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-02
  - QA-12
difficulty: advanced
tags:
  - feature-store
  - train-serve-skew
  - point-in-time
  - online-offline-consistency
  - mlops
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/feature-engineering/mlfeature_leakage_safe_pipeline.md
  - domain-AI-ML/feature-engineering/mlfeature_drift_audit.md
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
---

# Feature Store Design

**Objective:** Design a feature store (or a lightweight equivalent) that guarantees offline training features and online serving features are computed from the same definitions and respect point-in-time correctness — so train/serve skew and temporal leakage are prevented structurally rather than caught after deployment.

**When to Use:**
- Multiple models or teams will reuse features and need a shared, consistent source.
- Train/serve skew has bitten you and you want an architectural fix.
- Online inference must read precomputed features with low latency and point-in-time correctness.

**When NOT to Use:**
- A single model's pipeline is the scope (use `mlfeature_leakage_safe_pipeline.md`).
- You only need to monitor feature drift (use `mlfeature_drift_audit.md`).

## Inputs / Context

Provide what you can (ask for framework + version if a specific store is targeted):
- **Feature set** — entities, features, freshness needs, and whether each is batch or streaming.
- **Serving needs** — online (latency, QPS) vs batch; read patterns.
- **Sources** — warehouses, streams, and their update cadences.
- **Point-in-time requirements** — label timing and the prediction-time boundary.
- **Scale & team** — number of models/consumers; MLOps maturity.

## Constraints

**Must:**
- Define features once and serve them to both training (offline) and inference (online) from the same definitions.
- Enforce point-in-time correctness for training data generation (no future values relative to the event time).
- Specify freshness, materialization cadence, and the online/offline store responsibilities.

**Must Not:**
- Allow separate offline and online feature computation logic that can diverge (the skew root cause).
- Invent latency/QPS/storage figures — mark them as requirements to confirm.
- Treat the store as a leakage cure-all without point-in-time joins (a store can still leak the future).

**Instructions:**

1. **Model entities and feature views.** Define entities (user, merchant, device) and group features into views with owners, source, and freshness, so reuse and lineage are explicit.

2. **Enforce point-in-time correctness.** Specify point-in-time joins for training-set generation so each training row gets only feature values as of its event time — preventing temporal leakage at the store level.

3. **Split online vs offline responsibilities.** Offline store backs training/batch (history, point-in-time); online store backs low-latency inference (latest materialized values). State how the same definition populates both.

4. **Define materialization and freshness.** Set how/when features are computed and pushed online (batch cadence, streaming), and the staleness tolerance per feature.

5. **Guarantee definition parity.** Mandate a single feature definition (transformation logic) reused for both paths, with versioning — the structural defense against train/serve skew.

6. **Plan consistency checks.** Specify automated checks comparing online-served values to offline-recomputed values for the same entity/time, and alerting on divergence.

7. **Address governance and reuse.** Cover access, ownership, deprecation, and how new consumers discover and trust features (lineage, documentation).

**Output Format:**

A markdown design:
- **Entities & Feature Views** — table: View | Entity | Features | Source | Freshness | Owner.
- **Point-in-Time Strategy** — how training rows avoid future leakage.
- **Online vs Offline Store Roles** — responsibilities and the shared definition.
- **Materialization & Freshness** — cadence and staleness tolerance.
- **Skew-Prevention Mechanism** — single-definition + versioning.
- **Consistency Checks** — online/offline parity monitoring.
- **Open Requirements** — latency/QPS/scale numbers to confirm.

## Verification

- [ ] Features are defined once and serve both training and inference.
- [ ] Point-in-time correctness is enforced for training-set generation.
- [ ] Online and offline store roles and the shared definition are specified.
- [ ] Materialization cadence and per-feature freshness are defined.
- [ ] An online/offline parity check is included.
- [ ] No latency/QPS/storage figure is fabricated; requirements are flagged.

## False-Positive Prevention

❌ **DON'T:**
- Compute training features with a SQL job and serving features with separate app code — they will diverge and create skew that offline metrics never reveal.
- Generate training labels/features with a naive join that pulls the latest value — that leaks the future; use point-in-time joins.
- Assume an online store with fresh values is automatically consistent with how training features were built.
- Quote latency/QPS targets as facts when they are unconfirmed requirements.

✅ **DO:**
- Enforce a single feature definition reused by both offline and online paths, versioned.
- Use point-in-time (as-of-event) joins so each training row sees only past feature values.
- Add automated online-vs-offline value parity checks with alerting.
- Track freshness/staleness per feature and surface it to consumers.

## Example Output

```markdown
## Feature Store Design: Shared Risk Features (online inference, p99 < 50ms)

### Entities & Feature Views
| View | Entity | Features | Source | Freshness | Owner |
|---|---|---|---|---|---|
| user_activity | user | logins_14d, days_since_login | events stream | 5 min | Growth ML |
| merchant_stats | merchant | txn_rate_30d, chargeback_rate_30d | warehouse batch | daily | Risk ML |

### Point-in-Time Strategy
Training sets built via as-of-event joins: a transaction at time t gets feature values valid ≤ t.
No "latest value" joins — prevents temporal leakage.

### Online vs Offline Store Roles
Offline (warehouse/parquet): full history + point-in-time for training. Online (KV store): latest
materialized values for inference. Both populated from the SAME transformation definition.

### Materialization & Freshness
Streaming features materialized every 5 min; batch features nightly. Staleness tolerance noted
per feature; risk features must be < 1 day stale.

### Skew-Prevention Mechanism
One versioned feature definition per view, reused offline and online. Changing a definition bumps
its version; models pin a version.

### Consistency Checks
Hourly job recomputes offline values for sampled live requests and compares to online-served
values; alert if mismatch > threshold.

### Open Requirements
Confirm QPS, p99 latency budget, online store sizing.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** entities → point-in-time → roles → parity checks.
- **RT-02 (Multi-Dimensional Analysis Framework):** balances freshness, latency, reuse, and consistency.
- **CM-02 (Constraint Specification):** point-in-time correctness and single-definition are hard constraints.
- **DS-02 (Metric Specification):** parity checks are defined with divergence thresholds.
- **QA-12 (False Positives Identification):** targets the train/serve skew and future-join failure modes.

**Related Prompts:**
- `mlfeature_leakage_safe_pipeline.md` — per-model parity that this generalizes across models.
- `mlfeature_drift_audit.md` — monitor the served features for drift over time.
- `mldata_data_leakage_detector.md` — point-in-time errors are a temporal-leakage source.
