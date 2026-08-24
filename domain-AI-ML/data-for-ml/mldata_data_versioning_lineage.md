---
title: "ML Data Versioning & Lineage Design"
category: AI-ML/data-for-ml
description: "Design data versioning and end-to-end lineage so any model's training data can be reconstructed, audited, and traced from raw source to trained artifact for reproducibility and compliance."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - data-versioning
  - lineage
  - reproducibility
  - provenance
  - auditability
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_datasheet_authoring.md
  - domain-AI-ML/data-for-ml/mldata_dataset_curation_plan.md
  - domain-AI-ML/data-for-ml/mldata_data_quality_audit.md
---

# ML Data Versioning & Lineage Design

**Objective:** Design a data versioning and lineage scheme that makes any model's training inputs fully reconstructable and traceable — capturing what data version trained which model, how each dataset was derived from its sources, and what transformations were applied — to support reproducibility, debugging, rollback, and audit/compliance.

**When to Use:**
- "Which data trained the model in production?" cannot be answered confidently.
- You need reproducible experiments or to roll back to a prior dataset state.
- Regulatory/audit requirements demand provenance from raw source to model.
- Multiple teams share/transform datasets and changes are getting lost.

**When NOT to Use:**
- You only need to document a single static dataset's contents (use `mldata_datasheet_authoring.md`).
- You only need to assess data quality once (use `mldata_data_quality_audit.md`).

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Data flow** — sources → ingestion → transforms → feature sets → training datasets → models.
- **Storage & scale** — where data lives, volumes, update frequency (batch/stream).
- **Reproducibility requirement** — must you reproduce exact bytes, or statistical equivalence?
- **Audit/compliance needs** — what must be provable and for how long (retention).
- **Existing tooling** — any data/version-control, feature store, orchestration, or metadata catalog (and versions).
- **Team workflow** — who edits data, branching needs, review process.

## Constraints

**Must:**
- Make every training run resolvable to an immutable, identified dataset version and the code/config that produced it.
- Capture lineage end-to-end: source → transform → dataset → model, with the transform logic versioned alongside.
- Specify what "reproducible" means here (exact-bytes vs statistical) and design to that bar, including retention.

**Must Not:**
- Recommend a specific tool/product as the answer without tying the design to the stated reproducibility and audit requirements (ask for tooling + versions; keep it framework-neutral).
- Assume mutable, overwritten datasets are acceptable — flag overwrite-in-place as a reproducibility hazard.
- Conflate code versioning with data versioning; both must be linked but tracked appropriately.

**Instructions:**

1. **Map the data flow.** Diagram sources → ingestion → transforms → datasets → models, marking where data is currently mutated in place or untracked.

2. **Define the versioning unit and identity.** Decide what gets versioned (raw snapshots, intermediate tables, final training sets, features) and how each version is uniquely identified (content hash, semantic version, snapshot id) and made immutable.

3. **Set the reproducibility bar.** State whether exact-byte reproduction or statistical equivalence is required, and design storage/retention to meet it (e.g., immutable snapshots vs deterministic re-derivation from versioned source + code).

4. **Design lineage capture.** Specify the metadata recorded at each step: input version(s), transform code version, parameters, timestamp, operator, and output version — so any dataset can be traced backward and forward.

5. **Link data ↔ code ↔ model.** Ensure every model artifact records the exact dataset version(s) and pipeline code/config that produced it, enabling "what trained this?" and "what models used dataset X?" queries.

6. **Define change management.** Specify how dataset changes happen (branch/PR-style review, validation gates before a new version is blessed) and how breaking schema changes are signaled to consumers.

7. **Specify retention, access, and audit.** Define how long versions are kept, who can read/modify, and how an auditor reconstructs the exact training inputs for a given model on demand.

8. **State failure modes and gaps.** Identify where lineage could break (manual edits, untracked notebooks, external feeds) and the controls that close each gap.

**Output Format:**

A markdown design:
- **Data Flow Map** — sources → datasets → models; mutation/untracked hotspots.
- **Versioning Scheme** — unit, identity mechanism, immutability.
- **Reproducibility Bar** — exact-byte vs statistical + storage/retention to match.
- **Lineage Metadata** — fields captured per step.
- **Data↔Code↔Model Linkage** — how runs resolve to versions.
- **Change Management** — review/validation gates; schema-change signaling.
- **Retention, Access & Audit** — policy + reconstruction procedure.
- **Failure Modes & Controls** — lineage-break risks and mitigations.

## Verification

- [ ] Every training run can be resolved to an immutable, identified dataset version + producing code.
- [ ] Lineage is end-to-end (source → transform → dataset → model), with transforms versioned.
- [ ] The reproducibility bar (exact-byte vs statistical) is stated and the design meets it.
- [ ] Bidirectional queries are supported: "what trained model M" and "what models used dataset D."
- [ ] Lineage-break hotspots (manual edits, untracked notebooks, external feeds) are named with controls.

## False-Positive Prevention

❌ **DON'T:**
- Treat naming files `data_v2.csv` as versioning — without immutability and lineage you still can't reproduce a run.
- Version the code but overwrite the data in place, so the same commit silently trains on different data over time.
- Assume a feature store or data-version tool gives reproducibility "for free" without linking versions to model artifacts.
- Promise exact reproducibility while relying on a live external feed that changes underneath you.

✅ **DO:**
- Make dataset versions immutable and content-identified, and bind each model run to the version(s) it used.
- Capture transform code + parameters in lineage so derivations are re-runnable, not just labeled.
- Decide exact-byte vs statistical reproducibility explicitly and design retention to support it.
- Map where lineage breaks (notebooks, manual edits, external sources) and add a control for each.

## Example Output

```markdown
## Data Versioning & Lineage Design: Recommendations Pipeline

### Data Flow Map
- Sources: event stream + catalog DB → ingestion (daily batch) → feature tables → training datasets → models.
- Hotspots: analysts currently edit a "features_final.parquet" in place (untracked); notebook-built datasets bypass the pipeline.

### Versioning Scheme
- Unit: raw daily snapshots (immutable) + each blessed training dataset.
- Identity: content hash + semantic tag (e.g., `train-recs-2026-05-29-a1b2c3`); write-once, never overwritten.

### Reproducibility Bar
- Statistical equivalence for raw streams (volume); EXACT-byte for blessed training datasets (retained 24mo).

### Lineage Metadata (per step)
- input_version(s), transform_git_sha, params, run_ts, operator, output_version, row_count, schema_hash.

### Data↔Code↔Model Linkage
- Each model artifact stores dataset_version(s) + pipeline_git_sha + config_hash → both-direction queries supported.

### Change Management
- New dataset versions require a validation gate (quality audit pass) + reviewer approval before "blessed."
- Schema changes bump a MAJOR tag and notify consumers.

### Retention, Access & Audit
- Blessed datasets + lineage retained 24mo; read-open to ML team, write via pipeline service account only.
- Auditor reconstruction: given model id → resolve dataset_version → immutable snapshot + transform sha → re-derive.

### Failure Modes & Controls
- In-place edits → block direct writes; force pipeline path. Notebook datasets → require registration before training.
- External catalog feed → snapshot daily so a live change can't alter past versions.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** flow map → versioning → lineage → linkage → governance.
- **RT-02 (Multi-Dimensional Analysis Framework):** balances reproducibility, audit, scale, and workflow.
- **CM-02 (Constraint Specification):** immutability and the reproducibility bar are governing constraints.
- **DS-01 (Framework Application):** structures provenance/lineage to support audit/compliance requirements.
- **QA-01 (Self-Verification):** the checklist gates the design against reconstructability.

**Related Prompts:**
- `mldata_datasheet_authoring.md` — document each versioned dataset's contents and provenance.
- `mldata_dataset_curation_plan.md` — establish lineage capture at collection time.
- `mldata_data_quality_audit.md` — the validation gate that blesses a new dataset version.
