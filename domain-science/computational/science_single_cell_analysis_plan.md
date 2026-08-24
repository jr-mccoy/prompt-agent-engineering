---
title: "Single-Cell RNA-seq Analysis Plan"
category: science/computational
description: "Builds a pre-specified scRNA-seq analysis plan — ambient-RNA/doublet handling, data-driven cell QC, normalization, integration, clustering with resolution-robustness, marker- and reference-based annotation, and pseudobulk-aware differential testing."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - RT-03
  - QA-01
  - CM-02
difficulty: advanced
tags:
  - single-cell
  - scrna-seq
  - quality-control
  - batch-correction
  - clustering
  - cell-annotation
  - pseudobulk
  - reproducibility
updated: "2026-06-26"
related_prompts:
  - domain-science/computational/science_genomics_qc_protocol.md
  - domain-science/computational/science_bioinformatics_pipeline_designer.md
  - domain-science/disciplines/biology/bio_genomics_study_design.md
  - domain-science/statistics/science_multiple_comparisons_strategy.md
---

# Single-Cell RNA-seq Analysis Plan

**Objective:** Produce a pre-specified scRNA-seq analysis plan covering ambient-RNA and doublet handling, data-driven cell QC, normalization, feature selection, integration/batch correction, dimensionality reduction, clustering (with resolution treated as a researcher degree of freedom and tested for robustness), marker- and reference-based annotation with validation, and differential-expression/abundance testing that respects replicate structure (pseudobulk/aggregation to avoid pseudoreplication). The plan separates pre-specified from exploratory steps and aligns with scRNA-seq community practice and MINSEQE-style reporting.

**When to use:** Before running a single-cell analysis — to lock decisions that are otherwise tuned post-hoc (QC cutoffs, integration choice, clustering resolution, annotation, DE strategy). Use upstream-pipeline and QC siblings for read/alignment QC; this plan begins at the count matrix.

**Required inputs:**
- **Discipline.** Tissue/system and assay (e.g., 10x 3′ scRNA-seq, snRNA-seq, multiome).
- **Study type.** Observational / experimental; cross-condition comparison or atlas/descriptive.
- **Experimental design.** Conditions, biological replicates per condition, samples per batch, capture/sequencing batches.
- **Goal.** Cell-type discovery, cross-condition DE, compositional change, trajectory, or reference mapping.

**Optional inputs:**
- Reference atlas or marker sets for annotation.
- Known batch axes (donor, lane, chemistry, timepoint).
- Expected/known cell types and prior QC distributions.
- Pre-registration status (registered vs exploratory).

**Constraints — Must:**
- Begin from the count matrix; specify ambient-RNA correction and doublet detection/removal before cell QC.
- Set cell-QC cutoffs (counts, genes, percent-mitochondrial, percent-ribosomal) data-drivenly (e.g., MAD-based) rather than fixed magic numbers; thresholds are `[user-supplied]` or derived, never invented.
- State the normalization and feature-selection choice and its rationale.
- Enumerate the batch axes present and the integration/batch-correction approach (conceptually, e.g., Harmony / scVI), with how its success is assessed (mixing vs biology preservation).
- Treat clustering resolution as a researcher degree of freedom: report robustness across a range of resolutions, not a single tuned value.
- Annotate with both marker-based and reference-based evidence and a validation step.
- For cross-condition DE/abundance, aggregate to biological-sample level (pseudobulk) to avoid pseudoreplication; pre-specify the contrast and multiple-comparison handling.
- Flag clustering and annotation as exploratory unless pre-registered; align with MINSEQE-style / community reporting and FAIR deposit.

**Constraints — Must Not:**
- Do not invent citations, DOIs, dataset accessions, tool version numbers, or numeric QC thresholds. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not apply fixed "standard" QC cutoffs (e.g., a single percent-mito number) as if universal.
- Do not run cross-condition DE on individual cells as independent replicates (pseudoreplication).
- Do not present a single clustering resolution as ground truth, nor annotation as confirmed without validation.
- Do not describe any drafted output as "novel", "groundbreaking", "first-ever", or "gold standard".

**Instructions:**

1. **Restate design.** Confirm discipline, study type, replicates/batches, and goal. Flag if biological replication is insufficient for the stated DE/abundance goal.
2. **Specify pre-QC cleanup.** Ambient-RNA correction and doublet detection/removal, with the chosen approach and parameters (`[user-supplied]` where needed).
3. **Specify data-driven cell QC.** Counts, genes, percent-mito, percent-ribo via MAD/distribution-based cutoffs; state direction (low and/or high) and exclusion logic.
4. **Specify normalization + feature selection.** Choose and justify; note assumptions and alternatives (RT-03: compare candidate options where the choice is consequential).
5. **Specify integration/batch correction.** List batch axes; choose an approach; define success criteria (batch mixing without erasing biological signal) and how over-correction is detected.
6. **Specify dimensionality reduction + clustering.** Method and parameters; treat resolution as a degree of freedom — define the resolution sweep and the robustness/stability assessment.
7. **Specify annotation + validation.** Marker-based and reference-based annotation; a validation step (independent markers, held-out reference, or orthogonal signal). Label confidence per cluster.
8. **Specify DE/abundance testing.** Aggregate to sample-level pseudobulk for cross-condition contrasts; pre-specify the contrast, model, and multiple-comparison control; state compositional-analysis approach for abundance shifts.
9. **Mark pre-specified vs exploratory + deposit.** Tag each step; default to FAIR deposit (public accession, code in VCS with release tag/archive, container/lock). Run QA-01 self-check against the checklist.

**Output format (locked):**

```
## Design & Goal
[discipline, study type, replicates/batches, analysis goal; replication adequacy note]

## Pre-QC Cleanup
[ambient-RNA correction; doublet detection/removal]

## Cell QC (data-driven)
| Metric | Cutoff method (MAD/distribution, source) | Direction | Exclusion logic |
|---|---|---|---|

## Normalization & Feature Selection
[choice + rationale + alternatives considered]

## Integration / Batch Correction
[batch axes; approach; success criteria; over-correction check]

## Dimensionality Reduction & Clustering
[method/params; resolution sweep; robustness/stability assessment]

## Annotation & Validation
[marker-based + reference-based; validation step; per-cluster confidence]

## Differential Expression / Abundance Testing
[pseudobulk aggregation; pre-specified contrast/model; multiple-comparison control; compositional method]

## Pre-specified vs Exploratory
[per-step tag]

## Deposit & Reproducibility
[FAIR accession, VCS release tag, container/lock; [user-supplied] items]
```

**Reporting-standard alignment:** scRNA-seq community practice (QC on counts/genes/percent-mito, normalization, integration, Leiden/Louvain clustering, marker-based annotation); MINSEQE-style reporting; FAIR / The Turing Way deposit and provenance.

**Verification checklist (before delivering):**
- [ ] Discipline and study type captured as the first inputs.
- [ ] Biological replication assessed against the DE/abundance goal.
- [ ] Ambient-RNA and doublet handling specified before cell QC.
- [ ] Cell-QC cutoffs data-driven (MAD/distribution) or `[user-supplied]`, not fixed magic numbers.
- [ ] Batch axes enumerated; integration success/over-correction criteria defined.
- [ ] Clustering resolution treated as a degree of freedom with a robustness check.
- [ ] Annotation uses marker + reference evidence and a validation step.
- [ ] Cross-condition DE uses pseudobulk; contrast and multiple-comparison control pre-specified.
- [ ] Pre-specified vs exploratory tagged; no banned promotional language.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Pseudoreplication | Per-cell DE yielding tiny p-values across two samples | Aggregate to sample-level pseudobulk; pre-specify the model |
| Magic-number QC | A single percent-mito cutoff applied as universal | Require MAD/distribution-based, data-driven cutoffs |
| Resolution shopping | One clustering resolution chosen because it "looks right" | Resolution sweep + stability assessment; flag as exploratory |
| Over-integration | Batch "fixed" but real biology erased | Define success as mixing without biology loss; over-correction check |
| Unvalidated annotation | Cluster labels asserted from a single marker | Marker + reference evidence + validation; per-cluster confidence |
| Exploratory-as-confirmatory | Discovered clusters reported as pre-planned findings | Tag each step pre-specified vs exploratory |
