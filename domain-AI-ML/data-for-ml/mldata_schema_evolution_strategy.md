---
title: "Schema Evolution Strategy for ML Inputs"
category: AI-ML/data-for-ml
description: "Define how an ML pipeline's input/feature schema may change over time — backward vs forward compatibility, additive vs breaking changes, version negotiation, migration/backfill, deprecation windows — while protecting train/serve consistency and historical reproducibility."
techniques:
  - ST-02
  - DS-01
  - DS-06
  - RT-10
  - CM-02
difficulty: advanced
tags:
  - schema-evolution
  - compatibility
  - migration
  - deprecation
  - reproducibility
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_data_contract_design.md
  - domain-AI-ML/production-monitoring/mlmonitor_data_pipeline_health_audit.md
  - domain-AI-ML/data-for-ml/mldata_data_versioning_lineage.md
---

# Schema Evolution Strategy for ML Inputs

**Objective:** Produce a schema-evolution policy for an ML pipeline's inputs/features that classifies every change by compatibility, prescribes the version-negotiation and migration path, and protects both train/serve consistency and the reproducibility of historical training runs.

**When to Use:**
- An ML input or feature schema needs to change and you must decide how to roll it out without breaking serving or retraining.
- You are establishing standing rules so future changes are routine rather than incidents.
- Historical training reproducibility must survive ongoing schema change.

**When NOT to Use:**
- You are defining the *initial* contract and field semantics from scratch — use `mldata_data_contract_design.md`.
- You need to *enforce* changes via CI/runtime gates — use `mldata_data_contract_enforcement_ci.md`.

## Inputs / Context

- **Current schema** — fields, types, nullability, and which are consumed by which model versions.
- **Proposed change(s)** — what fields are added, removed, renamed, retyped, or re-semantic.
- **Consumers** — training jobs, batch scoring, online serving, and the schema version each expects.
- **Reproducibility requirement** — whether/how past training runs must remain re-runnable.
- **Backfill feasibility** — whether historical data can be recomputed for new/changed fields.
- **Coordination latency** — how quickly producers and consumers can deploy in lockstep (usually they can't).

## Constraints

**Must:**
- Classify each proposed change by compatibility: backward-compatible (old readers OK), forward-compatible (old writers OK), full, or breaking.
- Map each compatibility class to a rollout path (additive + default, dual-read/dual-write, versioned namespace, hard migration).
- Address train/serve skew explicitly: a feature available at training time must be available, with identical computation, at serving time.
- Specify a deprecation window and a migration/backfill plan for removed or retyped fields.
- Preserve historical reproducibility: state how a run from version N can be reproduced after the schema advances.

**Must Not:**
- Invent backfill costs, storage figures, coordination timelines, or SLA numbers — reason from stated inputs and mark unknowns as `UNKNOWN — confirm`.
- Recommend a synchronized "big bang" producer+consumer deploy as the default; assume independent deploy as the realistic case.

**Instructions:**

1. **Classify the change.** For each proposed change, assign a compatibility class using the decision tree (add nullable → backward; add required → breaking for old writers; rename → breaking unless aliased; type-narrow → breaking; type-widen → often backward).
2. **Choose the rollout pattern.** Additive-with-default, dual-read/dual-write, versioned schema namespace, or hard migration — match the pattern to the class and to whether producer/consumer can deploy independently.
3. **Audit train/serve skew.** Confirm any new/changed feature is computed identically and is available in both training and serving paths before it can be used.
4. **Plan migration & backfill.** State whether historical data is recomputed, defaulted, or left null; define the order of operations so no consumer reads a partial state.
5. **Set the deprecation window.** Time-box dual-running of old + new, with a removal date and a consumer cutover checkpoint.
6. **Protect reproducibility.** Pin each training run to a schema version + data snapshot so version-N runs remain re-runnable after the schema advances.

**Output Format:**

A markdown strategy with: Change Inventory (table: change → class → rollout pattern) · Train/Serve Skew Audit · Migration & Backfill Plan · Deprecation Window & Cutover · Reproducibility Guarantee. Unknowns marked explicitly.

## Verification

- [ ] Every proposed change has an assigned compatibility class with a stated reason.
- [ ] Each change maps to a concrete rollout pattern compatible with independent deploys.
- [ ] Train/serve availability and identical computation are confirmed for each new/changed feature.
- [ ] A deprecation window with a removal date and cutover checkpoint exists for removed fields.
- [ ] The reproducibility guarantee names what is pinned (schema version + data snapshot).
- [ ] No cost/timeline/SLA figure was fabricated; gaps are UNKNOWN.

## False-Positive Prevention

❌ **DON'T:**
- Call adding a column "always safe" — adding a *required* (non-null, no-default) field is breaking for every old writer, and adding a feature the *serving* path can't compute creates train/serve skew even though the *training* table looks fine.
- Assume a type widen is harmless — int→float can silently change downstream feature binning or hash bucketing, shifting the model's input distribution.
- Plan a migration that flips producer and consumer at the same instant — independent deploys mean there is always a window where one side is on the old schema and one on the new.
- Recompute a feature with *today's* logic and backfill it onto *historical* rows as if it were original — that fabricates history and corrupts reproducibility of past runs.

✅ **DO:**
- Run each change through the compatibility decision tree and write down why it lands in that class.
- For any new feature, verify identical computation and availability in both training and serving before allowing its use.
- Use dual-read/dual-write or a versioned namespace so old and new consumers coexist during the deprecation window.
- Pin every training run to its schema version and data snapshot so historical runs reproduce without backfill rewriting the past.

## Example Output

```markdown
## Schema Evolution Strategy: user_features v3 → v4

### Change Inventory
| change | from → to | class | rollout pattern |
|---|---|---|---|
| add `session_count_7d` (nullable int) | — → int64? | backward-compatible | additive + null default; backfill via recompute |
| add `region` (required) | — → string (req) | BREAKING (old writers) | dual-write; version namespace v4; 30d deprecation |
| `tenure_days` int → float | int64 → float64 | BREAKING (binning shift) | new field `tenure_days_f64`; deprecate int field |
| drop `legacy_flag` | bool → removed | BREAKING (readers) | mark deprecated; remove after cutover date |

### Train/Serve Skew Audit
- session_count_7d: computed in feature store, available online — OK.
- region: derived from geo-IP at request time online vs ETL offline — VERIFY identical logic before use.

### Migration & Backfill Plan
1. Producer writes both v3 and v4 (dual-write).
2. Backfill session_count_7d for history (recompute window: UNKNOWN — confirm cost).
3. Consumers migrate reads v3 → v4 individually.
4. Stop v3 writes only after all consumers confirmed on v4.

### Deprecation Window & Cutover
- Dual-run 30 days. Cutover checkpoint at day 21; removal of v3 + legacy_flag at day 30.

### Reproducibility Guarantee
- Each training run pins {schema_version, data_snapshot_id}. v3 runs reproduce against the v3 snapshot — no backfill rewrites historical inputs.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** Ordered flow from classify → roll out → skew audit → migrate → deprecate → reproduce.
- **DS-01 (Framework Application):** Applies the backward/forward/full/breaking compatibility framework.
- **DS-06 (Prioritization & Severity):** Ranks changes by breaking severity to drive the rollout choice.
- **RT-10 (Troubleshooting Decision Tree):** Encodes the change-class decision tree (add/rename/retype/drop).
- **CM-02 (Constraint Specification):** Pins must/must-not rules and the no-fabrication clause.

**Related Prompts:**
- `mldata_data_contract_design.md` — define the baseline schema and breaking-change policy a change evolves from.
- `mlmonitor_data_pipeline_health_audit.md` — detect skew and silent schema drift in the live pipeline.
- `mldata_data_versioning_lineage.md` — pin schema version + snapshot for reproducible historical runs.
