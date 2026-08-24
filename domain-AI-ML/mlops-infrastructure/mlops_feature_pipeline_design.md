---
title: "MLOps Feature Pipeline Design"
category: AI-ML/mlops-infrastructure
description: "Design offline and online feature pipelines that share definitions and timing so the same feature is computed identically for training and serving — eliminating train/serve skew."
techniques:
  - ST-02
  - CM-02
  - QA-04
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - feature-pipeline
  - feature-store
  - train-serve-skew
  - point-in-time
  - data-engineering
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_model_serving_architecture.md
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
  - domain-AI-ML/mlops-infrastructure/mlops_training_pipeline_orchestration.md
---

# MLOps Feature Pipeline Design

**Objective:** Design the offline (training) and online (serving) feature pipelines so that each feature has a single definition, a single timing rule, and a verifiable equivalence between the two paths — so the value a model sees at training time matches the value it sees at inference, eliminating train/serve skew.

**When to Use:**
- A model scores well offline but degrades online, and feature differences are suspected.
- Standing up a feature store or formalizing how features are computed for both training and serving.
- Features are currently computed by separate offline and online code that can drift apart.

**When NOT to Use:**
- Diagnosing leakage in a single (training) dataset (use `mldata_data_leakage_detector.md`).
- Choosing the serving runtime pattern (use `mlops_model_serving_architecture.md` — this feeds it).

## Inputs / Context

Provide what you can; the design degrades gracefully:
- **Feature list** — names, source data, and the transformation each needs.
- **Prediction time** — the exact instant inference happens in production and what data is available then.
- **Freshness needs** — per feature: can it be precomputed daily, or must it reflect the last few seconds?
- **Serving pattern** — online real-time / batch / streaming, and expected latency for feature lookup.
- **Current implementation** — how features are computed today offline vs online (if at all).
- **Platform** — feature store / engine in use or considered (Feast / Tecton / SageMaker Feature Store / Vertex / Databricks). Ask if unspecified.

## Constraints

**Must:**
- Define each feature once, with a single transformation, consumed by both offline and online paths (shared definition, not parallel code).
- Enforce point-in-time correctness offline: training features must use only data available at each example's prediction time.
- Specify a skew-detection check that compares offline-computed and online-computed values for the same entity.

**Must Not:**
- Allow the offline and online paths to use different code/logic for the same feature without a verified equivalence.
- Use future-relative windows in offline feature computation (that is leakage, not just skew).
- Assume a feature store guarantees consistency; the timing and definitions still have to be correct.

**Instructions:**

1. **Anchor the prediction-time boundary.** For each feature, state when it is observed/computed relative to inference. Offline computation must respect this exact boundary (point-in-time joins), or training data is leaked.

2. **Classify each feature by freshness and source.** Group features into precomputable (batch, slowly changing) vs near-real-time (must be fresh at request). This drives where each is computed.

3. **Define each feature once.** For every feature, write the single canonical transformation and its inputs. Both pipelines reference this definition; neither reimplements it.

4. **Design the offline path.** Specify how training features are materialized with point-in-time-correct joins to produce a training table where each row's features reflect only past data.

5. **Design the online path.** Specify how serving retrieves each feature — precomputed values from the online store, on-request computation, or a hybrid — within the serving latency budget.

6. **Guarantee equivalence.** Specify the mechanism that keeps offline and online consistent: shared transformation code, a feature store that materializes one definition to both, and the timing alignment between them.

7. **Design skew detection.** Define a check that, for sampled entities, compares the feature value computed offline against the value served online, and alerts when they diverge beyond tolerance.

8. **Handle backfills and freshness SLAs.** Specify how the online store is kept fresh, what happens on a stale/missing feature at serving time, and how historical features are backfilled consistently.

**Output Format:**

A markdown design doc:
- **Prediction-Time Boundary** — when inference occurs, what is available.
- **Feature Catalog** — table: Feature | Source | Transformation | Freshness class | Offline path | Online path.
- **Point-in-Time Strategy** — how offline joins avoid future data.
- **Equivalence Mechanism** — how offline ≡ online is guaranteed.
- **Skew Detection Plan** — sampling, comparison, tolerance, alert.
- **Freshness, Backfill & Fallback** — SLAs, missing-value handling.

## Verification

- [ ] Each feature has one canonical definition consumed by both paths.
- [ ] Offline features are point-in-time correct (no future data per row).
- [ ] Online retrieval for each feature fits the serving latency budget.
- [ ] A concrete skew-detection check (offline vs online value) is specified with a tolerance.
- [ ] Missing/stale-feature behavior at serving time is defined.

## False-Positive Prevention

❌ **DON'T:**
- Assume a feature store eliminates skew on its own — duplicated definitions in two places still drift.
- Treat matching feature *names* offline and online as proof they compute the same value.
- Use a window like "average over the last 30 days including today" offline if "today" isn't fully available at prediction time.
- Declare parity without ever comparing an actual offline value to the served value for the same entity.

✅ **DO:**
- Materialize one definition to both paths, or share the exact transformation code.
- Verify point-in-time correctness per row, anchored to that example's prediction timestamp.
- Run a periodic skew check on sampled entities and alert on divergence beyond tolerance.
- Define what serving does when a feature is missing/stale, so a gap degrades gracefully instead of silently skewing.

## Example Output

```markdown
## Feature Pipeline Design — Ride ETA Model (platform: Feast)

### Prediction-Time Boundary
- Inference fires when a rider requests a quote. Available: rider/driver state, recent trip stats, live traffic.

### Feature Catalog
| Feature | Source | Transformation | Freshness | Offline | Online |
|---|---|---|---|---|---|
| driver_trips_7d | trips table | count over [t-7d, t) | daily | PIT join on request_ts | precomputed → online store |
| zone_demand_now | event stream | count over [t-5m, t) | real-time | PIT window join | computed on-request from stream |
| rider_avg_rating | ratings | mean to t | daily | PIT join | online store lookup |

### Point-in-Time Strategy
- Training built via as-of joins on `request_ts`; every window is half-open `[start, request_ts)`. No "including today."

### Equivalence Mechanism
- One Feast FeatureView per feature; batch source materializes to the online store; on-demand features share a single Python transformation imported by both paths.

### Skew Detection Plan
- Hourly: sample 500 served requests, recompute features offline for the same entity+timestamp, compare. Alert if > 1% of features differ beyond ε.

### Freshness, Backfill & Fallback
- Online store refreshed every 5 min for real-time features; daily features at 03:00. Missing feature → last-known value flagged; if absent, region median + skew alert.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** boundary → catalog → offline → online → equivalence → skew.
- **CM-02 (Constraint Specification):** point-in-time correctness and shared definition are the binding constraints.
- **QA-04 (Consistency Checking):** the skew-detection check is the core consistency mechanism.
- **RT-05 (Evidence-Based Reasoning):** equivalence is proven by value comparison, not assumed.
- **DS-02 (Metric Specification):** features bound to explicit windows and freshness classes.

**Related Prompts:**
- `mlops_model_serving_architecture.md` — the serving path this feeds, with its latency budget.
- `mldata_data_leakage_detector.md` — point-in-time errors here are temporal leakage.
- `mlops_training_pipeline_orchestration.md` — orchestrates the offline materialization step.
