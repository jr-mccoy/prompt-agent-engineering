---
title: "Data Contract Enforcement in CI & Runtime"
category: AI-ML/data-for-ml
description: "Operationalize a data contract: validate on producer change in CI, check records at ingestion runtime, block merges on breaking-change detection, quarantine violating records, and route alerts to owners — without silent acceptance or over-strict pipelines that halt on benign changes."
techniques:
  - ST-02
  - ST-03
  - DS-06
  - QA-01
  - CM-02
difficulty: advanced
tags:
  - contract-enforcement
  - ci
  - runtime-validation
  - quarantine
  - alerting
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_data_contract_design.md
  - domain-AI-ML/data-for-ml/mldata_schema_evolution_strategy.md
  - domain-AI-ML/mlops-infrastructure/mlops_ml_cicd_pipeline_design.md
---

# Data Contract Enforcement in CI & Runtime

**Objective:** Turn a written data contract into enforced gates — CI checks on producer changes, runtime validation at ingestion, breaking-change detection that blocks merges, quarantine/dead-letter handling, and ownership-routed alerts — calibrated to catch real violations without halting on benign ones.

**When to Use:**
- A data contract exists and you need it to actually fail builds and catch bad records, not just sit in a doc.
- Bad upstream data has reached training/serving because nothing validated it at the boundary.
- You need a quarantine + alerting path for records that violate the contract.

**When NOT to Use:**
- The contract itself (fields, SLAs, ownership, breaking-change policy) isn't written yet — use `mldata_data_contract_design.md`.
- You're deciding how the schema is *allowed* to change over time — use `mldata_schema_evolution_strategy.md`.

## Inputs / Context

- **The contract** — schema, quality expectations, SLAs, and breaking-change policy to enforce.
- **Producer change surface** — repo/PR where schema or producing logic changes (the CI hook point).
- **Ingestion path** — stream/batch entry point where records arrive (the runtime hook point).
- **Severity tiers** — which violations should block a merge, quarantine a record, or only warn.
- **Ownership routing** — who is paged for which violation class.
- **Tolerance** — acceptable false-block / false-pass rates; how strict the pipeline can be without harming availability.

## Constraints

**Must:**
- Place enforcement at two layers: CI (producer-side, pre-merge) and runtime (ingestion-side, per-record/per-batch).
- Detect breaking changes against the contract and block the merge that introduces them.
- Define a quarantine / dead-letter path for violating records — never drop them silently and never let them pass into training/serving.
- Route every violation to a named owner via a defined channel.
- Tier severities so benign/non-breaking changes warn rather than halt.

**Must Not:**
- Invent error-rate thresholds, alert SLAs, or pipeline-throughput numbers — derive from stated tolerance and mark unknowns as `UNKNOWN — confirm`.
- Design an all-or-nothing gate that halts the pipeline on any deviation; over-strictness is its own outage.

**Instructions:**

1. **Map enforcement points.** Identify the producer PR (CI) and the ingestion boundary (runtime); decide what each layer is responsible for catching.
2. **Encode contract assertions.** Translate schema + quality expectations into executable checks (schema diff, type/nullability, range/enum, freshness, volume bounds).
3. **Build breaking-change detection.** Compare the proposed schema against the contract; classify the diff; block the merge only for breaking classes.
4. **Define the runtime decision.** Per record/batch: pass, quarantine (dead-letter + alert), or fail-fast — by severity tier, not uniformly.
5. **Wire quarantine & replay.** Send violating records to a dead-letter store with the failed assertion attached; define how they're reviewed and replayed.
6. **Route alerts.** Map each violation class to an owner and channel; set noise controls (dedupe, rate-limit) so the signal survives.
7. **Tune for false-block/false-pass.** State the calibration goal and how thresholds are adjusted from observed enforcement outcomes.

**Output Format:**

A markdown enforcement plan: Enforcement Points (CI vs runtime) · Contract Assertions (table) · Breaking-Change Gate · Runtime Severity & Quarantine Matrix · Alert Routing · Calibration Notes. Unknowns marked.

## Verification

- [ ] Both a CI layer and a runtime layer are defined with distinct responsibilities.
- [ ] Each contract expectation maps to a concrete executable assertion.
- [ ] Breaking-change detection blocks merges only for breaking classes; benign changes pass.
- [ ] A quarantine/dead-letter path exists; no violating record is dropped or silently passed.
- [ ] Every violation class routes to a named owner via a defined channel.
- [ ] Severity tiers prevent uniform fail-fast; false-block/false-pass calibration is addressed.
- [ ] No threshold or SLA number was fabricated; gaps are UNKNOWN.

## False-Positive Prevention

❌ **DON'T:**
- Validate only in CI and trust runtime — a schema can pass CI yet still receive out-of-range *values* (null spike, currency drift) at runtime that no static check catches.
- Make every assertion fail-fast — halting the whole pipeline because one record has an unexpected enum turns a single bad row into a full outage, which teams then disable entirely.
- Drop violating records to "keep the pipeline green" — silent drops hide a data outage and bias training data without any signal.
- Treat the CI green check as proof the data is correct — CI verifies the *schema/producer code*, not that today's actual records satisfy ranges and freshness; conflating the two is a false sense of safety.

✅ **DO:**
- Enforce at both layers: CI catches schema/producer-code regressions; runtime catches value-level and freshness violations on live records.
- Tier severities so non-breaking deviations warn and quarantine while only contract-breaking changes hard-fail.
- Dead-letter violating records with the failed assertion attached, and define a review + replay path.
- Calibrate thresholds against observed false-block/false-pass outcomes rather than guessing a number.

## Example Output

```markdown
## Contract Enforcement: orders_events → fraud-scoring-model

### Enforcement Points
- CI (producer repo): schema diff vs contract on every PR touching the event schema.
- Runtime (ingestion): per-batch validation of values, freshness, volume before write to feature store.

### Contract Assertions
| assertion | layer | severity |
|---|---|---|
| schema matches contract field set/types | CI | block merge if breaking |
| amount_minor non-null, 0 ≤ x ≤ 10_000_000 | runtime | quarantine + alert |
| currency in {USD,EUR,GBP} | runtime | quarantine + alert |
| P95 lag < 5 min | runtime | warn → page if sustained UNKNOWN window — confirm |
| daily volume ≥ 99.5% of baseline | runtime | page; baseline UNKNOWN — confirm |

### Breaking-Change Gate
- PR adds nullable field → pass (warn). PR renames/drops/narrows → BLOCK with link to contract policy.

### Runtime Severity & Quarantine Matrix
- Range/enum violation → dead-letter topic `orders.dlq` + assertion tag; replay after producer fix.
- Freshness breach → warn first occurrence, page if sustained beyond window.

### Alert Routing
- Schema/breaking → #checkout-oncall (producer). Value/freshness → #fraud-ml-oncall (consumer). Dedupe 5m.

### Calibration Notes
- Goal: minimize false-block on benign additive changes; review DLQ weekly to retune ranges. Target false-pass rate: UNKNOWN — confirm tolerance.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** Sequences enforcement from map → assert → gate → quarantine → route → tune.
- **ST-03 (Output Format Specification):** Fixes the plan's tables (assertions, severity/quarantine matrix).
- **DS-06 (Prioritization & Severity):** Tiers violations so only breaking ones halt, the rest quarantine or warn.
- **QA-01 (Self-Verification):** Calibration loop checks false-block/false-pass against observed outcomes.
- **CM-02 (Constraint Specification):** Encodes the no-silent-drop / no-over-strict / no-fabrication rules.

**Related Prompts:**
- `mldata_data_contract_design.md` — the contract whose assertions this plan enforces.
- `mldata_schema_evolution_strategy.md` — the change classes the breaking-change gate keys off.
- `mlops_ml_cicd_pipeline_design.md` — the CI/CD pipeline these gates plug into.
