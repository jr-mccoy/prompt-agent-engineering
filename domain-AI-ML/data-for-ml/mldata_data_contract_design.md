---
title: "Data Contract Design for ML Pipelines"
category: AI-ML/data-for-ml
description: "Design an explicit data contract between upstream producers and downstream ML consumers — schema, semantics/units, freshness/SLA, ownership, quality expectations, and a versioned breaking-change policy — reasoning only from stated inputs."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - data-contract
  - schema
  - sla
  - ownership
  - data-quality
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_data_versioning_lineage.md
  - domain-AI-ML/data-for-ml/mldata_data_quality_audit.md
  - domain-AI-ML/mlops-infrastructure/mlops_feature_pipeline_design.md
---

# Data Contract Design for ML Pipelines

**Objective:** Produce a complete, signable data contract that captures the producer's promise to the ML consumer — schema, semantics, freshness, ownership, quality expectations, and a versioned breaking-change policy — so downstream training and serving never silently inherit upstream changes.

**When to Use:**
- A producing team (events, CDC stream, batch export, third-party feed) supplies data that an ML pipeline trains or serves on.
- You are formalizing an informal "just read the table" dependency into an accountable interface.
- Repeated incidents trace back to undocumented upstream schema or semantic drift.

**When NOT to Use:**
- You need to manage how the schema *changes over time* (compatibility classes, migration, deprecation) — use `mldata_schema_evolution_strategy.md`.
- You need to *enforce* a contract in CI/runtime (validation gates, quarantine, alerting) — use `mldata_data_contract_enforcement_ci.md`.

## Inputs / Context

- **Producer & consumer identity** — owning teams, on-call/escalation, who signs.
- **Dataset interface** — table/topic/file, delivery mechanism (batch, stream, API), partitioning.
- **Field inventory** — each field's name, type, nullability, allowed values, units, semantic meaning.
- **Freshness requirements** — how stale the consumer can tolerate (latency, update cadence).
- **Volume & shape** — expected row/event counts, cardinalities, known seasonality.
- **Criticality** — whether the consuming model serves live traffic or trains offline.

## Constraints

**Must:**
- Specify, per field: name, type, nullability, units/semantics, and allowed/expected range.
- Define freshness and availability as measurable SLAs (e.g., "P95 lag < 30 min", "≥ 99.5% daily delivery").
- Name an accountable owner and escalation path on both producer and consumer sides.
- Include a breaking-change policy: what counts as breaking, required notice window, and version bump rule.
- Distinguish the *contract version* (semantic) from the *data version/snapshot* it governs.

**Must Not:**
- Invent SLA numbers, schema fields, volumes, or freshness figures the user did not provide — reason from stated inputs and mark every gap as `UNKNOWN — confirm with producer` rather than guessing.
- Treat the contract as documentation only; it is an enforceable promise with consequences when violated.

**Instructions:**

1. **Fix the parties and interface.** Record producer, consumer, delivery mechanism, and the single source-of-truth artifact the contract governs.
2. **Build the field table.** For every field capture type, nullability, unit/semantic, allowed range. Flag any field whose meaning the producer cannot confirm.
3. **Set quality expectations.** Define per-field and dataset-level checks (completeness, uniqueness, referential integrity, distribution bounds) as testable assertions.
4. **Define freshness & availability SLAs.** State them as measurable thresholds with the window over which they are evaluated.
5. **Assign ownership.** Producer owner, consumer owner, escalation contacts, review cadence.
6. **Write the breaking-change policy.** Enumerate breaking vs non-breaking change classes, notice window, version-bump rule, and consumer-notification channel.
7. **Version and sign.** Assign contract semantic version; record effective date and both signatories.

**Output Format:**

A markdown contract with sections: Parties & Interface · Field Schema (table) · Quality Expectations · Freshness & Availability SLA · Ownership & Escalation · Breaking-Change Policy · Versioning & Signatures. Every unconfirmed value carries an explicit `UNKNOWN` marker.

## Verification

- [ ] Every field has type, nullability, unit/semantic, and allowed range (or an explicit UNKNOWN).
- [ ] All SLAs are measurable thresholds with an evaluation window, not adjectives.
- [ ] A named accountable owner exists on both producer and consumer sides.
- [ ] The breaking-change policy enumerates change classes and a notice window.
- [ ] Contract version is distinct from the data snapshot version.
- [ ] No number in the document was invented; gaps are marked UNKNOWN.

## False-Positive Prevention

❌ **DON'T:**
- Copy field *types* from a sample row and assume *semantics* — a column typed `int` could be cents, dollars, or a status enum; an unconfirmed unit is a future train/serve skew bug, not a documented fact.
- Write "data is fresh and high quality" as the SLA; vague adjectives pass review but enforce nothing and silently degrade.
- Treat additive nullable fields and column renames as equally breaking — miscategorizing change severity either blocks benign updates or lets breaking ones through.
- Backfill an SLA number ("99.9% is standard") because the producer didn't give one — fabricating an availability target the producer never agreed to makes the contract unsignable.

✅ **DO:**
- Confirm each field's *unit and meaning* with the producer and mark anything unconfirmed as `UNKNOWN — confirm`.
- Express every quality and freshness expectation as a testable threshold with a window.
- Classify each change type (add nullable, add required, rename, type-narrow, drop) explicitly as breaking or non-breaking.
- Derive SLA targets from the consumer's stated tolerance, and leave them UNKNOWN when no input exists.

## Example Output

```markdown
## Data Contract: orders_events → fraud-scoring-model
Contract version: 2.1.0 · Effective: 2026-06-19

### Parties & Interface
- Producer: Checkout Platform (owner: a.lee, on-call: #checkout-oncall)
- Consumer: Fraud ML (owner: r.patel, on-call: #fraud-ml-oncall)
- Delivery: Kafka topic `orders.events.v2`, partitioned by order_id

### Field Schema
| field | type | nullable | unit / semantic | allowed range |
|---|---|---|---|---|
| order_id | string (UUID) | no | unique order key | UUID v4 |
| amount_minor | int64 | no | order total, MINOR units (cents) | 0 – 10_000_000 |
| currency | string | no | ISO-4217 code | enum: USD, EUR, GBP |
| created_at | timestamp (UTC) | no | event creation time | within 24h of ingest |
| coupon_code | string | yes | applied coupon, null = none | UNKNOWN — confirm casing |

### Quality Expectations
- order_id: 100% non-null, 100% unique per day.
- amount_minor: 0 null tolerance; P99 ≤ 10_000_000 (alert on breach).
- currency: 100% within enum; any value outside → quarantine.

### Freshness & Availability SLA
- Lag: P95 event-to-topic < 5 min (window: rolling 1h).
- Availability: ≥ 99.5% of expected daily volume delivered (window: calendar day).
- Expected volume: UNKNOWN — confirm baseline with producer.

### Breaking-Change Policy
- Non-breaking (minor bump): add nullable field; widen numeric range.
- Breaking (major bump): rename/drop field; narrow type; change unit (e.g. minor→major).
- Notice: 14 calendar days before any breaking change, posted to #fraud-ml-oncall.

### Versioning & Signatures
- Producer: a.lee (2026-06-19) · Consumer: r.patel (2026-06-19)
```

**Techniques Used:**
- **ST-01 (Clear Objective):** Anchors the artifact as a signable producer-promise, not loose docs.
- **ST-02 (Structured Sequential Instructions):** Ordered build from parties → fields → SLAs → policy → signature.
- **ST-03 (Output Format Specification):** Fixes the contract's section layout and field-table shape.
- **CM-02 (Constraint Specification):** Encodes must/must-not rules including the no-fabrication clause.
- **DS-02 (Metric Specification):** Forces SLAs and quality checks to be measurable thresholds with windows.

**Related Prompts:**
- `mldata_data_versioning_lineage.md` — version and trace the data snapshots a contract governs.
- `mldata_data_quality_audit.md` — assess actual data against the contract's quality expectations.
- `mlops_feature_pipeline_design.md` — design the downstream pipeline that consumes the contracted data.
