---
title: "Genomics Study Design"
category: science/disciplines/biology
description: "Design a genomics or genome-association study with sample-size justification, multiple-testing strategy, batch and ancestry control, and pre-specified analysis plan"
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-02
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - genomics
  - gwas
  - rna-seq
  - power-analysis
  - batch-effects
  - ancestry
  - multiple-testing
updated: "2026-05-19"
related_prompts:
  - domain-science/methods-foundations/science_experimental_design_advisor.md
  - domain-science/methods-foundations/science_hypothesis_generator.md
  - domain-science/disciplines/biology/bio_omics_study_metadata_planner.md
---

# Genomics Study Design

**Objective:** Produce a defensible study design for a genomics experiment (GWAS, bulk RNA-seq, single-cell, WGS / WES, ChIP-seq, ATAC-seq, methylation, or similar) including sample-size justification appropriate to the assay, batch and ancestry confound control, multiple-testing strategy, and a pre-specified analysis plan that a reviewer could lock against the data.

**When to use:** Before any samples are collected or sequenced, when the user has a biological question that requires a genome-scale measurement and needs to demonstrate that the chosen scale, controls, and analysis plan can actually answer it.

**Required inputs:**
- **Biological question.** Phrased as a testable claim, not a topic.
- **Assay type.** GWAS, bulk RNA-seq, scRNA-seq, snRNA-seq, WGS, WES, ChIP-seq, ATAC-seq, bisulfite, Hi-C, etc.
- **Organism, tissue / cell type, and disease or condition** (if applicable).
- **Sample source.** New collection, biobank, public repository (specify which), or mixed.
- **Available sample size and projected cost per sample.**
- **Computational and storage capacity** (or a constraint on what is realistically available).
- **Existing comparable studies** the user knows of (titles or DOIs supplied by the user — do not invent).

**Optional inputs:**
- Effect size estimates from prior work (if known).
- Sub-question or interaction terms (e.g., sex-by-treatment).
- Anticipated ancestry / population structure.
- Replicate strategy (technical, biological, or both).

**Constraints — Must:**
- Distinguish biological replicates from technical replicates throughout. Sample-size justification is in biological-replicate units.
- Treat batch (run, lane, library prep day, reagent lot, instrument, technician) as a first-class confound, not an afterthought.
- For human studies, treat ancestry and relatedness as first-class confounds (PCA, kinship matrix, mixed model) and surface the population-stratification risk explicitly.
- Pre-specify the primary contrast, the primary statistical model, and the multiple-testing strategy before data are seen.
- Pre-specify QC thresholds (read depth, call rate, MAF cutoff, percent mitochondrial reads, doublet rate — whichever apply to the assay).
- Align reporting to community standards: MIAME / MINSEQE for transcriptomics; MIATA for adaptive immune; MIRAGE for glycomics; GWAS-CC reporting for GWAS; STORMS for microbiome; broader MIBBI family otherwise. Name the standard explicitly in the output.

**Constraints — Must Not:**
- Do not propose any sample size without naming the assumption set (effect size, allele frequency, dropout rate, dispersion, baseline mean) it depends on.
- Do not invent published effect sizes, allele frequencies, or QC thresholds. If a literature anchor is needed and not supplied, mark `[user-supplied]` and ask.
- Do not propose multiple-testing-naive p-value reporting (no "p < 0.05" interpreted at genome scale).
- Do not pool batches across the experimental contrast in a way that confounds batch with biology (e.g., all controls on day 1, all cases on day 2).
- Do not recommend a specific commercial kit, vendor, or catalog number unless the user supplies one to react to.

**Instructions:**

1. **Restate the biological question as a measurement-level hypothesis.** Identify the unit of biological replication, the contrast(s), and the effect to be estimated (mean difference, fold change, odds ratio, beta, peak height, etc.). If the question cannot be expressed this way, stop and ask the user to refine it.

2. **Match assay to question.** Build a short matched-list of assay options and explain in 2–3 lines per option why the user's chosen assay does or does not match. If a better-matched assay exists at comparable cost, surface it and let the user accept or override.

3. **Sample-size and power.** Build a table of three sample-size scenarios (pessimistic / central / optimistic) with the assumption set fully written out (effect size, variance / dispersion, dropout, MAF, dispersion parameter, etc.). Cite the calculation method by name (e.g., PROPER for RNA-seq, scPower for scRNA-seq, GAS-power for GWAS) but do not invent numerical defaults — ask the user for the prior-study anchor or mark `[user-supplied]`.

4. **Batch and confounder plan.** Build a sample-by-batch crosstab schematic showing how cases, controls, conditions, sexes, and ancestries will be balanced across processing batches. Name every batch axis (collection day, RNA extraction day, library prep day, sequencing run, lane, instrument, operator, reagent lot). Recommend randomization within batch and identify any axis that cannot be balanced.

5. **Population structure / relatedness plan (human or outbred organism).** Specify PCA on a pruned variant set, ancestry inference method, exclusion thresholds for related individuals (e.g., kinship coefficient > 0.0884 ≈ 2nd-degree), and the mixed-model / covariate strategy used downstream.

6. **QC thresholds, pre-specified.** Output a numeric QC table with per-step thresholds and the rationale for each. Distinguish hard exclusion thresholds from soft ones requiring inspection.

7. **Analysis plan, pre-specified.** Specify primary model, primary contrast(s), covariate set, multiple-testing correction (FDR vs. genome-wide-significant threshold), sensitivity analyses, and exploratory analyses (clearly labeled exploratory).

8. **Sharing and reporting commitments.** Identify the deposit target (dbGaP / GEO / ArrayExpress / SRA / EGA / European Nucleotide Archive), the metadata standard, the licensing posture, and whether consent supports controlled vs. open access.

9. **Pitfalls and what would invalidate the study.** Enumerate the 4–6 most likely failure modes (batch confound, low yield, ancestry stratification, dropout, doublet rate, contamination, allele dropout, etc.) and how each would be detected.

**Output format (locked):**

```
## Question and measurement model
[restated as testable claim with replication unit named]

## Assay match
| Option | Matches question? | Trade-off vs. selected |

## Sample size scenarios
| Scenario | Per-group N | Assumption set | Power | Calculation method |

## Batch design
[crosstab showing balanced allocation across every batch axis]

## Population structure plan (if applicable)
[PCA, kinship, mixed-model spec]

## Pre-specified QC thresholds
| Stage | Metric | Threshold | Action if violated | Rationale |

## Pre-specified analysis plan
- Primary model:
- Primary contrast:
- Covariates:
- Multiple-testing correction:
- Sensitivity analyses:
- Exploratory analyses:

## Reporting standard alignment
[name standard; one line per checklist item the design satisfies]

## Pitfalls and detection
| Failure mode | Detection | Mitigation |

## Open questions for the user
[gaps marked [user-supplied] above, collected here]
```

**Reporting-standard alignment:** Name the applicable standard explicitly (MIAME, MINSEQE, GWAS-CC, STORMS, etc.) and trace each section above back to a checklist item. If no single standard fits, compose from MIBBI components and list the components.

**Verification checklist (before delivering):**
- [ ] Replication unit named and biological-vs-technical distinction enforced.
- [ ] Every sample-size scenario has an assumption set written out.
- [ ] No invented effect sizes, allele frequencies, or QC thresholds — all marked `[user-supplied]` if missing.
- [ ] Batch design balances the primary contrast across every named batch axis.
- [ ] Multiple-testing correction is named.
- [ ] Primary analysis pre-specified; exploratory labeled exploratory.
- [ ] Reporting standard named.
- [ ] At least four failure modes and their detection are listed.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Power overstatement | Single optimistic scenario reported as "the" sample size | Three scenarios always |
| Hidden batch confound | Apparent biology that mirrors batch axis | Crosstab printed and inspected |
| Ancestry stratification masquerading as signal | Top hits track PC1 / PC2 rather than phenotype | PC-controlled model, λ_GC, LD-score regression |
| QC-threshold hacking | Adjusting thresholds after seeing results | Thresholds pre-specified in this document |
| Multiple-testing softening | Switching from FWER to FDR after the fact | Correction method pre-specified |
| Invented citations or kit numbers | Plausible-looking DOI / catalog reference | All citations user-supplied or marked missing |
