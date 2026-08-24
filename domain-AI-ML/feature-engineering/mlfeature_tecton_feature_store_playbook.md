---
title: "Tecton Feature Platform Playbook"
category: AI-ML/feature-engineering
description: "Design an ML feature workflow on Tecton — feature views/services, batch/stream/on-demand feature types, offline training retrieval and online serving, freshness SLAs, and train/serve consistency — without inventing version-specific API behavior or pricing."
techniques:
  - ST-02
  - CM-02
  - RT-10
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - tecton
  - feature-store
  - streaming-features
  - train-serve-skew
  - mlops
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/feature-engineering/mlfeature_store_design.md
  - domain-AI-ML/feature-engineering/mlfeature_feast_feature_store_playbook.md
  - domain-AI-ML/mlops-infrastructure/mlops_feature_pipeline_design.md
---

# Tecton Feature Platform Playbook

**Objective:** Turn a managed-feature-platform decision into a concrete Tecton workflow — feature views (batch, stream, on-demand) and feature services, offline training retrieval and low-latency online serving, freshness SLAs, and train/serve consistency — so models share governed, point-in-time-correct features across training and production.

**When to Use:**
- You have chosen Tecton (managed feature platform) and need an opinionated setup walkthrough.
- You need streaming and on-demand (request-time) features alongside batch, with managed online serving and freshness SLAs.
- Multiple production models must share governed, consistent features.

**When NOT to Use:**
- You haven't decided whether you need a feature platform — start with `mlfeature_store_design.md`.
- You want the open-source path — see `mlfeature_feast_feature_store_playbook.md`.
- You need the upstream feature-computation pipeline design — use `mlops_feature_pipeline_design.md`.

## Inputs / Context

Provide what you can:
- **Tecton version/SDK** and the underlying compute/streaming + online-store configuration in your account.
- **Data sources** — batch (warehouse/lake), streaming sources, and any request-time inputs.
- **Entities & timestamps** — join keys and event-time columns.
- **Feature types needed** — batch, streaming, and on-demand (transform at request time).
- **Serving latency SLO and freshness SLA** per feature.

## Constraints

**Must:**
- Ask which feature types (batch/stream/on-demand) are needed and the freshness SLA before defining feature views.
- Use point-in-time-correct offline retrieval for training datasets (as-of join on event time).
- Ensure the same feature definitions and transformations power offline training and online serving (no skew), including on-demand transforms.

**Must Not:**
- Invent Tecton API signatures, decorators, config keys, or pricing — mark "verify against current Tecton docs and your account."
- Treat on-demand (request-time) features as if they can be backfilled from history without the request inputs.
- Recommend a freshness/serving configuration that can't meet the stated SLO/SLA.

**Instructions:**

1. **Map sources, entities, and timestamps.** Catalog batch, streaming, and request-time sources; define entities (join keys) and event-timestamp columns. Confirm timestamps before anything else — point-in-time correctness depends on them.

2. **Choose feature types per signal.** For each feature, decide batch vs. streaming vs. on-demand based on freshness needs and whether it depends on request-time inputs. Justify each choice against the freshness SLA.

3. **Define feature views.** Specify feature views for each type with their transformations, entities, timestamps, and TTL/freshness. Keep definitions in version-controlled code (the feature repo).

4. **Compose feature services.** Group the feature views a model consumes into a feature service — the contract the model trains and serves against. One service = one model's feature contract.

5. **Design training retrieval (point-in-time).** Build training datasets via as-of joins against an entity/spine dataframe so each label gets feature values as-of its event time, including correct handling of streaming and on-demand features.

6. **Design online serving.** Specify how the feature service is queried online within the latency SLO, how streaming features stay fresh, and how on-demand transforms run at request time identically to training.

7. **Guarantee consistency & governance.** Ensure offline and online paths share the same transformation code (the platform's main value); set up access governance, freshness monitoring, and cost controls on the online store/compute.

8. **Define validation.** Provide a smoke test: generate a training set from the feature service (point-in-time), then request the same entities online and confirm values match as-of values (no skew), including an on-demand feature computed from request inputs.

**Output Format:**

A markdown setup playbook:
- **Sources, Entities & Timestamps** — catalog
- **Feature-Type Decisions** — table: Feature | Type (batch/stream/on-demand) | Freshness SLA | Why
- **Feature Views** — transforms, entities, TTL
- **Feature Services** — per-model contracts
- **Training Retrieval** — point-in-time design
- **Online Serving** — latency, streaming freshness, on-demand at request time
- **Consistency, Governance & Cost** — shared transforms, monitoring
- **Smoke Test** — skew-check validation
- **Verify-in-Docs** — version/pricing items flagged

## Verification

- [ ] Each feature's type (batch/stream/on-demand) is justified against its freshness SLA.
- [ ] Training retrieval is point-in-time-correct across batch, streaming, and on-demand features.
- [ ] Offline and online paths share the same transformation code (no skew), including on-demand.
- [ ] Online serving design meets the latency SLO; streaming freshness meets the SLA.
- [ ] A feature service defines each model's feature contract explicitly.
- [ ] Tecton API/config/pricing specifics are flagged "verify," not asserted.

## False-Positive Prevention

❌ **DON'T:**
- Treat an on-demand, request-time feature as backfillable from history alone — without the original request inputs the training value is wrong.
- Assume offline and online produce the same feature because the name matches, while a transform differs — that is skew.
- Promise a freshness SLA the streaming/materialization configuration can't actually meet.
- Quote Tecton decorators, API calls, or pricing from memory as version-stable.

✅ **DO:**
- Use point-in-time retrieval and reconstruct on-demand features from the request inputs as they existed at event time.
- Verify online-served values equal as-of training values for the same entity, including an on-demand case.
- Set freshness/serving configs to demonstrably meet the SLA/SLO, or revise the SLA.
- Mark all Tecton API/config/pricing specifics as "verify against current docs and your account."

## Example Output

```markdown
## Tecton Playbook: Fraud Features (batch + stream + on-demand)

### Sources, Entities & Timestamps
- Batch: account warehouse table. Stream: transaction events. Request-time: current transaction amount/geo.
- Entities: account_id. Event-time columns confirmed on each source.

### Feature-Type Decisions
| Feature | Type | Freshness SLA | Why |
|---|---|---|---|
| account_age_days | batch | daily | slow-changing |
| txn_count_5m | stream | seconds | velocity signal |
| amount_vs_avg | on-demand | request-time | needs current txn input |

### Feature Views
Batch/stream views with transforms + TTL; on-demand view transforms request input vs. stored avg.

### Feature Services
fraud_model_v3_service = {account_age_days, txn_count_5m, amount_vs_avg}.

### Training Retrieval (point-in-time)
Spine (account_id, txn_event_time, label) → as-of join; on-demand feature recomputed from the historical request inputs at txn_event_time.

### Online Serving
Query fraud_model_v3_service online within p99 SLO; stream keeps txn_count_5m fresh; amount_vs_avg computed at request from live input via same transform code.

### Consistency, Governance & Cost
Offline + online share transform code; freshness monitoring on stream features; access governance on the service; online-store cost watched.

### Smoke Test
Generate PIT training set → request same accounts online → assert values match as-of (incl. amount_vs_avg recomputed from request).

### Verify-in-Docs
- Feature-view/service definitions + decorators for your Tecton version.
- Streaming/online config and pricing.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** sources → feature types → views → services → training → serving → validation.
- **CM-02 (Constraint Specification):** no-fabrication, point-in-time-correctness, and offline/online-parity constraints govern the design.
- **RT-10 (Troubleshooting / Operational Reasoning):** organized around the platform's core value — eliminating skew across batch, stream, and on-demand features.
- **DS-02 (Metric Specification):** freshness SLAs, latency SLO, and the skew-check are concrete gates.
- **QA-01 (Self-Verification):** the smoke test proves no skew, including the hardest case (on-demand features).

**Related Prompts:**
- `mlfeature_store_design.md` — decide whether/what feature platform before this playbook.
- `mlfeature_feast_feature_store_playbook.md` — the open-source alternative.
- `mlops_feature_pipeline_design.md` — the upstream pipeline computing the features Tecton governs.
