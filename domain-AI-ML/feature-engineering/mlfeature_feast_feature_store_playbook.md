---
title: "Feast Feature Store Playbook"
category: AI-ML/feature-engineering
description: "Stand up Feast for ML feature serving — entities, feature views, offline/online stores, point-in-time-correct training retrieval, and materialization — so training and serving share consistent features without train/serve skew, and without inventing version-specific API behavior."
techniques:
  - ST-02
  - CM-02
  - RT-10
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - feast
  - feature-store
  - point-in-time-correctness
  - train-serve-skew
  - mlops
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/feature-engineering/mlfeature_store_design.md
  - domain-AI-ML/feature-engineering/mlfeature_leakage_safe_pipeline.md
  - domain-AI-ML/mlops-infrastructure/mlops_feature_pipeline_design.md
---

# Feast Feature Store Playbook

**Objective:** Turn a feature-consistency goal into a concrete Feast setup — entity and feature-view definitions, offline and online store choices, point-in-time-correct training retrieval, and materialization to the online store — so the same feature definitions serve both training and online inference without train/serve skew.

**When to Use:**
- You have chosen Feast (open-source feature store) and need an opinionated setup walkthrough.
- Multiple models/teams need to share consistent, reusable features across training and serving.
- You are seeing (or want to prevent) train/serve skew or point-in-time leakage in feature retrieval.

**When NOT to Use:**
- You haven't decided *whether* you need a feature store at all — start with `mlfeature_store_design.md`.
- The core problem is leakage in feature logic itself — use `mlfeature_leakage_safe_pipeline.md`.
- You need the upstream pipeline that computes features — use `mlops_feature_pipeline_design.md`.

## Inputs / Context

Provide what you can:
- **Feast version** and deployment (local, containerized, or managed); the registry backend.
- **Offline store** — warehouse/lake (e.g., BigQuery, Snowflake, file/Parquet) holding historical features.
- **Online store** — low-latency store (e.g., Redis, DynamoDB, other) for serving.
- **Entities & keys** — the join keys (e.g., user_id, item_id) and event-timestamp columns.
- **Latency SLO** for online retrieval and the freshness requirement for features.

## Constraints

**Must:**
- Ask for offline/online store choices, entity keys, and event-timestamp columns before defining feature views.
- Use point-in-time-correct retrieval (`get_historical_features` semantics) for training so labels never see future feature values.
- Define materialization cadence so online features meet the freshness requirement, and ensure training/serving use the same definitions.

**Must Not:**
- Invent Feast API signatures, config keys, or store-specific options — mark "verify against your Feast version's docs."
- Generate training data with a naive join that ignores event timestamps (causes leakage / skew).
- Recommend an online store whose latency can't meet the serving SLO.

**Instructions:**

1. **Model entities and event timestamps.** Define entities (join keys) and identify the event-timestamp column for each source. Point-in-time correctness depends on accurate timestamps — confirm them first.

2. **Choose offline and online stores.** Select the offline store (historical, batch retrieval) and online store (low-latency serving) from the inputs; justify the online store against the latency SLO.

3. **Define feature views and sources.** Author feature views over the data sources, each tied to entities and a timestamp, with TTLs where features expire. Keep definitions in version-controlled code (the feature repo).

4. **Design training retrieval (point-in-time).** Specify how training datasets are built with point-in-time joins against an entity dataframe so each label row gets feature values as-of its event time — no future leakage. This is the anti-skew/anti-leakage core.

5. **Design materialization to online.** Define the materialization cadence (batch/stream) that pushes features to the online store to meet freshness, and how serving calls `get_online_features` with the same view definitions used in training.

6. **Guarantee train/serve consistency.** Establish that training and serving import the exact same feature-view definitions; flag any transformation done outside Feast that could diverge between paths.

7. **Add governance & monitoring.** Cover the registry (shared definitions), access, feature freshness monitoring, and online-store cost/TTL. Cross-link production-monitoring for drift.

8. **Define validation.** Provide a smoke test: build a training set via point-in-time retrieval, materialize, fetch the same entity online, and confirm the online feature values match the as-of training values (no skew).

**Output Format:**

A markdown setup playbook:
- **Entities & Timestamps** — keys + event-time columns
- **Store Choices** — offline + online + rationale vs. SLO
- **Feature Views** — views, sources, TTLs (table)
- **Training Retrieval** — point-in-time join design
- **Materialization** — cadence + freshness
- **Train/Serve Consistency** — shared definitions + skew risks
- **Governance & Monitoring** — registry, freshness, cost
- **Smoke Test** — skew-check validation steps
- **Verify-in-Docs** — version-sensitive items flagged

## Verification

- [ ] Every feature source has a correct event-timestamp column for point-in-time joins.
- [ ] Training retrieval is point-in-time-correct (no future feature values for a label).
- [ ] The online store choice is justified against the serving latency SLO.
- [ ] Materialization cadence meets the stated freshness requirement.
- [ ] Training and serving use identical feature-view definitions (no divergent transforms).
- [ ] Feast API/config specifics are flagged "verify," not asserted.

## False-Positive Prevention

❌ **DON'T:**
- Build training data with a plain join on entity key while ignoring event time — it leaks future feature values and inflates offline metrics.
- Assume online and offline features match because they share a name, while a transformation differs between paths (train/serve skew).
- Pick an online store for convenience without checking it meets the serving latency SLO.
- Quote Feast API calls, config keys, or store options from memory as version-stable.

✅ **DO:**
- Use point-in-time retrieval so each label sees only as-of feature values.
- Verify online-served values equal the as-of training values for the same entity (explicit skew check).
- Justify the online store against the measured/target latency SLO.
- Mark all Feast API/config specifics as "verify against your Feast version's docs."

## Example Output

```markdown
## Feast Playbook: Real-Time Recommendation Features

### Entities & Timestamps
- Entities: user_id, item_id. Event-timestamp column on each source.

### Store Choices
- Offline: warehouse (historical features, batch retrieval).
- Online: low-latency KV store — meets p99 < 20ms serving SLO. Verify store option support.

### Feature Views
| View | Source | Entities | TTL |
|---|---|---|---|
| user_activity_7d | events table | user_id | 7d |
| item_popularity_1d | item agg | item_id | 1d |

### Training Retrieval (point-in-time)
Entity dataframe (user_id, item_id, label_event_time) → get_historical_features → each row gets features as-of label_event_time. No future leakage.

### Materialization
Batch materialize hourly to online store (meets 1h freshness for item_popularity; user_activity streamed if tighter freshness needed).

### Train/Serve Consistency
Serving calls get_online_features with the SAME feature-view definitions imported from the feature repo. No out-of-store transforms.

### Governance & Monitoring
Shared registry; monitor feature freshness + online hit rate; TTL controls online-store size/cost.

### Smoke Test
Build training set (PIT) for sample entities → materialize → get_online_features for same entities/time → assert online values == as-of training values.

### Verify-in-Docs
- get_historical_features / get_online_features signatures, store config keys for your Feast version.
- Materialization (batch/stream) options.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** entities → stores → views → training retrieval → materialization → consistency → validation.
- **CM-02 (Constraint Specification):** no-fabrication, point-in-time-correctness, and train/serve-consistency constraints govern the setup.
- **RT-10 (Troubleshooting / Operational Reasoning):** organized around eliminating the real failure mode — train/serve skew and point-in-time leakage.
- **DS-02 (Metric Specification):** freshness, latency SLO, and the skew-check are concrete, measurable gates.
- **QA-01 (Self-Verification):** the smoke test asserts online == as-of training values to prove no skew.

**Related Prompts:**
- `mlfeature_store_design.md` — decide whether/what feature store before this playbook.
- `mlfeature_leakage_safe_pipeline.md` — ensure the feature logic itself is leakage-free.
- `mlops_feature_pipeline_design.md` — the upstream pipeline that computes the features Feast serves.
