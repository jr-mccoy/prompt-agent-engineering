---
title: "Mass-Spectrometry Proteomics Analysis Plan"
category: science/computational
description: "Builds a pre-specified MS proteomics analysis plan — DDA vs DIA choice, search strategy, target-decoy FDR at the correct level with protein inference, missing-value mechanism handling, normalization, PTM site-localization and PTM FDR, and replicate-aware statistical testing with public deposit."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - RT-03
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - proteomics
  - mass-spectrometry
  - fdr-control
  - missing-data
  - post-translational-modification
  - dda-dia
  - statistical-testing
  - reproducibility
updated: "2026-06-26"
related_prompts:
  - domain-science/computational/science_bioinformatics_pipeline_designer.md
  - domain-science/computational/science_genomics_qc_protocol.md
  - domain-science/statistics/science_multiple_comparisons_strategy.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Mass-Spectrometry Proteomics Analysis Plan

**Objective:** Produce a pre-specified MS proteomics analysis plan: acquisition strategy (DDA vs DIA), database-search strategy, target-decoy FDR control applied at the correct level (PSM vs peptide vs protein, with the protein-inference problem made explicit), match-between-runs caveats, missing-value mechanism handling (MNAR vs MCAR; left-censored imputation), normalization, PTM site-localization scoring and PTM FDR, and replicate-aware statistical testing. The plan pre-specifies the contrast and FDR threshold and aligns with MIAPE reporting and public deposit (PRIDE/ProteomeXchange, PXD).

**When to use:** Before analyzing quantitative MS proteomics data — to fix decisions that strongly bias results if tuned post-hoc (FDR level, imputation, normalization, PTM localization, test contrast). For acquisition-method design upstream, supply that as a required input; this plan covers identification through statistics and deposit.

**Required inputs:**
- **Discipline.** Proteomics subfield (e.g., expression proteomics, phosphoproteomics, interactomics).
- **Study type.** Observational / experimental; quantitative comparison or descriptive catalog.
- **Acquisition mode.** DDA or DIA (and label-free vs labeled, e.g., TMT/SILAC), instrument if relevant.
- **Design and goal.** Conditions, biological replicates, the contrast(s) of interest, and search database/version ([user-supplied]).

**Optional inputs:**
- Spectral library (for DIA) provenance and version.
- Known PTMs of interest and localization-scoring expectation.
- Existing FDR thresholds or a community standard to inherit.
- Pre-registration status.

**Constraints — Must:**
- State and justify the DDA-vs-DIA workflow choice and its implications for quantification and missingness (RT-03: compare the options where consequential).
- Specify the search strategy (database, enzyme, modifications, decoy construction) with versions `[user-supplied]` where unknown.
- Control FDR with target-decoy at the explicitly named level (PSM / peptide / protein) and address the protein-inference problem (shared peptides, protein grouping). Pre-specify the FDR threshold.
- State match-between-runs use and its transfer-error caveats.
- Identify the missing-value mechanism (MNAR vs MCAR), and choose an imputation/handling strategy consistent with left-censored MNAR where applicable; state the assumption.
- Specify normalization and the replicate-aware statistical model (e.g., MSstats-style handling of technical vs biological replication); pre-specify the contrast and multiple-comparison control.
- For PTM studies, specify site-localization scoring and PTM-level FDR distinct from peptide/protein FDR.
- Default to public deposit (PRIDE/ProteomeXchange, PXD accession) with complete MIAPE metadata; code in VCS with a release tag/archive.

**Constraints — Must Not:**
- Do not invent citations, DOIs, dataset accessions, tool version numbers, or numeric QC thresholds (including FDR cutoffs). If needed and not supplied, mark `[user-supplied]` and ask.
- Do not report a single FDR without naming the level it applies to (PSM/peptide/protein).
- Do not impute missing values without stating the assumed mechanism (treating MNAR as MCAR is a flagged error).
- Do not claim PTM sites without localization scoring, nor conflate PTM FDR with peptide/protein FDR.
- Do not describe any drafted output as "novel", "groundbreaking", "first-ever", or "gold standard".

**Instructions:**

1. **Restate design.** Confirm discipline, study type, acquisition mode, replicates, contrast, and database/version. Flag missing required inputs and replication adequacy.
2. **Choose acquisition workflow.** Justify DDA vs DIA (and labeling), noting consequences for quantification completeness and missing-data structure.
3. **Specify the search strategy.** Database (and version), enzyme, fixed/variable modifications, decoy approach; spectral-library provenance for DIA.
4. **Specify FDR control.** Name the level(s) — PSM, peptide, protein — and the pre-specified threshold(s); address protein inference (shared peptides, grouping, razor/unique handling).
5. **Address match-between-runs.** State whether used and its transfer-error and false-transfer caveats.
6. **Handle missing values.** Diagnose MNAR vs MCAR; choose handling (left-censored imputation, filtering, or model-based) consistent with the mechanism; state the assumption explicitly.
7. **Specify normalization + statistics.** Normalization method; replicate-aware model (technical vs biological); pre-specified contrast; multiple-comparison control across proteins.
8. **Handle PTMs (if applicable).** Site-localization scoring and a PTM-level FDR distinct from peptide/protein FDR; report localized vs ambiguous sites.
9. **Specify deposit + reproducibility.** PRIDE/ProteomeXchange (PXD) deposit with MIAPE metadata; VCS release tag/archive; container/lock. Self-check against the verification checklist.

**Output format (locked):**

```
## Design & Goal
[discipline, study type, acquisition mode, replicates, contrast, database/version; replication note]

## Acquisition Workflow Choice
[DDA vs DIA + labeling; quantification & missingness implications]

## Search Strategy
[database/version, enzyme, modifications, decoy; DIA library provenance]

## FDR Control
| Level (PSM/peptide/protein) | Threshold (source) | Protein-inference handling |
|---|---|---|

## Match-Between-Runs
[used? transfer-error / false-transfer caveats]

## Missing-Value Handling
[mechanism: MNAR/MCAR; strategy; stated assumption]

## Normalization & Statistical Testing
[normalization; replicate-aware model; pre-specified contrast; multiple-comparison control]

## PTM Handling (if applicable)
[site-localization scoring; PTM-level FDR; localized vs ambiguous]

## Deposit & Reproducibility
[PXD/PRIDE deposit + MIAPE metadata; VCS release tag/archive; container/lock; [user-supplied] items]
```

**Reporting-standard alignment:** MIAPE (proteomics reporting); ProteomeXchange / PRIDE (PXD) public deposit; target-decoy FDR and MSstats-style statistical handling as community practice.

**Verification checklist (before delivering):**
- [ ] Discipline and study type captured as the first inputs.
- [ ] DDA-vs-DIA choice justified with missingness/quantification implications.
- [ ] Search strategy specified with `[user-supplied]` versions where unknown.
- [ ] FDR level named (PSM/peptide/protein) with pre-specified threshold; protein inference addressed.
- [ ] Match-between-runs caveats stated if used.
- [ ] Missing-value mechanism (MNAR/MCAR) diagnosed and handling justified.
- [ ] Replicate-aware model, pre-specified contrast, and multiple-comparison control present.
- [ ] PTM site-localization and distinct PTM FDR specified where applicable.
- [ ] Public deposit (PXD/PRIDE) + MIAPE metadata; no banned promotional language.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Wrong-level FDR | "1% FDR" reported but applied at PSM level while protein claims inflate | Name FDR level explicitly; control at the level of the claim |
| Protein-inference glossed | Counts proteins as if peptides map uniquely | Require shared-peptide/grouping/razor handling statement |
| MNAR treated as MCAR | Mean/random imputation of left-censored absences | Diagnose mechanism; use left-censored-appropriate handling; state assumption |
| MBR over-trust | Match-between-runs fills gaps with false transfers | State MBR caveats; pre-specify when transfers are accepted |
| PTM over-claim | Modification sites asserted without localization | Require site-localization scoring + distinct PTM FDR |
| Replicate conflation | Technical replicates inflate significance | Replicate-aware model separating technical vs biological |
