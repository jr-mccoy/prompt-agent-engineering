---
title: "Genomics QC Protocol"
category: science/computational
description: "Builds a per-stage genomics quality-control protocol — read-level, alignment, variant, and sample-level — with each metric tied to a user-supplied or standard-cited threshold, an action-if-violated, and a remediation path."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-02
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - genomics
  - quality-control
  - sequencing-qc
  - variant-calling
  - sample-qc
  - thresholds
  - remediation
  - reproducibility
updated: "2026-06-26"
related_prompts:
  - domain-science/computational/science_bioinformatics_pipeline_designer.md
  - domain-science/disciplines/biology/bio_genomics_study_design.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
  - domain-science/statistics/science_multiple_comparisons_strategy.md
---

# Genomics QC Protocol

**Objective:** Produce a structured, per-stage genomics QC protocol covering raw reads, alignment, variant calls, and sample-level checks. For each metric it specifies a threshold (placeholder / `[user-supplied]` / cited standard — never invented), the action if the threshold is violated, and a remediation path. The artifact distinguishes hard-exclusion criteria from inspect-then-decide criteria and aligns with established best-practice *structure* (e.g., GATK / ENCODE-style organization) without asserting specific numeric cutoffs.

**When to use:** After a pipeline is designed (or while designing one) and before trusting downstream results — to define, in advance, what "good enough" means at each genomics processing stage. Pair with `science_bioinformatics_pipeline_designer.md`, which consumes these gates.

**Required inputs:**
- **Discipline.** Genomics subfield (whole-genome, whole-exome, targeted panel, RNA-seq, etc.).
- **Study type.** Observational / experimental / clinical / population / method-development.
- **Sequencing platform and library type.** Read length, paired/single-end, capture/amplicon if relevant.
- **Reference build and analysis goal.** Reference/annotation versions ([user-supplied]); germline vs somatic; cohort vs single-sample.

**Optional inputs:**
- Existing project QC thresholds or a standard to inherit them from.
- Sample metadata (expected sex, known relatedness, population structure).
- Sequencing depth target and coverage design.

**Constraints — Must:**
- Organize QC by stage: raw reads, alignment, variant, sample-level — each with metric → threshold → action-if-violated → remediation.
- For every metric, set the threshold as a `PLACEHOLDER`, `[user-supplied]` value, or a value cited to a named standard. Require the user/standard to anchor the number.
- Explicitly classify each criterion as hard-exclusion vs inspect-then-decide.
- Cover, at minimum: reads (per-base quality, adapter content, duplication, GC distribution, overrepresented k-mers); alignment (mapping rate, insert-size distribution, coverage uniformity/depth, duplication rate); variant (Ti/Tv ratio, het/hom ratio, depth, strand bias, filtering structure such as VQSR or hard-filter logic); sample-level (sex/genetic-sex check, contamination estimate, relatedness, PCA/ancestry outliers).
- State reporting-standard alignment explicitly and keep QC decisions auditable/provenance-tracked.

**Constraints — Must Not:**
- Do not invent citations, DOIs, dataset accessions, tool version numbers, or numeric QC thresholds. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not present a numeric cutoff as a community standard without a named, verifiable source.
- Do not collapse hard-exclusion and inspect-then-decide criteria into a single undifferentiated pass/fail.
- Do not describe any drafted output as "novel", "groundbreaking", "first-ever", or "gold standard".
- Do not retrofit thresholds to make borderline samples pass (post-hoc threshold tuning is a flagged risk).

**Instructions:**

1. **Restate context.** Confirm discipline, study type, platform/library, reference build, and germline-vs-somatic / cohort-vs-single goal. Flag missing required inputs.
2. **Define read-level QC.** Specify metrics (per-base quality, adapter, duplication, GC, overrepresented k-mers), each with threshold (`[user-supplied]`/standard), violation action, and remediation (e.g., trimming, re-sequencing decision).
3. **Define alignment QC.** Specify mapping rate, insert-size distribution, coverage depth and uniformity, and duplication; set thresholds, actions, and remediation (e.g., realignment, re-prep).
4. **Define variant-level QC.** Specify Ti/Tv, het/hom ratio, depth, strand bias, and the filtering structure (VQSR vs hard filters), each with threshold/action/remediation. Keep filter logic explicit and pre-specified.
5. **Define sample-level QC.** Specify sex check, contamination, relatedness, and PCA/ancestry-outlier detection; set thresholds/actions/remediation, including cohort-level exclusion logic.
6. **Classify criteria.** Mark each metric hard-exclusion vs inspect-then-decide, and state who/what makes the call for the latter.
7. **Specify provenance and reporting.** State how QC metrics, decisions, and exclusions are logged (e.g., an aggregated multi-sample report) for auditability.
8. **Run an adversarial pass (QA-02).** Stress-test the protocol: which metric could pass while the data are still bad? Add a guardrail. Confirm no invented numbers remain.

**Output format (locked):**

```
## QC Context
[discipline, study type, platform, reference build, germline/somatic, cohort/single]

## Read-Level QC
| Metric | Threshold (source) | Action if violated | Remediation | Hard-exclusion / Inspect |
|---|---|---|---|---|

## Alignment QC
| Metric | Threshold (source) | Action if violated | Remediation | Hard-exclusion / Inspect |
|---|---|---|---|---|

## Variant-Level QC
| Metric | Threshold (source) | Action if violated | Remediation | Hard-exclusion / Inspect |
|---|---|---|---|---|
[filtering structure: VQSR vs hard-filter logic, pre-specified]

## Sample-Level QC
| Metric | Threshold (source) | Action if violated | Remediation | Hard-exclusion / Inspect |
|---|---|---|---|---|

## Provenance & Reporting
[how metrics/decisions/exclusions are logged and aggregated]

## Open Questions / [user-supplied] Thresholds
[every unanchored number listed for resolution]
```

**Reporting-standard alignment:** GATK best-practice and ENCODE-style QC *structure* (organization, not asserted numeric cutoffs); FAIR / The Turing Way for auditable, provenance-tracked QC decisions.

**Verification checklist (before delivering):**
- [ ] Discipline and study type captured as the first inputs.
- [ ] All four stages present (reads, alignment, variant, sample-level) with required metrics each.
- [ ] Every threshold is `PLACEHOLDER`/`[user-supplied]`/cited — no invented numbers.
- [ ] Each metric has an action-if-violated and a remediation path.
- [ ] Hard-exclusion vs inspect-then-decide classified for every criterion.
- [ ] Variant filter structure stated and pre-specified (no post-hoc tuning).
- [ ] Provenance/reporting of QC decisions specified.
- [ ] No banned promotional language in drafted text.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Invented thresholds | Confident-looking cutoffs with no source | Every number `[user-supplied]` or cited; unanchored numbers listed in Open Questions |
| Passing-but-bad sample | All gates green yet sample is contaminated/swapped | Adversarial QA-02 pass; require contamination + sex + relatedness cross-checks |
| Post-hoc threshold tuning | Cutoffs nudged so borderline samples survive | Pre-specify thresholds; flag any change as a deviation needing justification |
| Filter logic ambiguity | "Filtered variants" without stating the filter | Require explicit VQSR/hard-filter structure pre-specified |
| Hard/soft conflation | One undifferentiated pass/fail hides judgment calls | Mandatory hard-exclusion vs inspect-then-decide tag per metric |
