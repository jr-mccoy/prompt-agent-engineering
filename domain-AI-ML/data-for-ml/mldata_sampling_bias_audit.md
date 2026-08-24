---
title: "ML Sampling Bias Audit"
category: AI-ML/data-for-ml
description: "Detect sampling and selection bias between the training sample and the deployment population — per-segment coverage gaps, selection mechanisms, and shift — with evidence-backed, severity-ranked findings."
techniques:
  - ST-02
  - RT-05
  - QA-12
  - DS-06
  - DS-02
difficulty: advanced
tags:
  - sampling-bias
  - selection-bias
  - representativeness
  - distribution-shift
  - coverage
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_dataset_curation_plan.md
  - domain-AI-ML/data-for-ml/mldata_data_quality_audit.md
  - domain-AI-ML/data-for-ml/mldata_datasheet_authoring.md
---

# ML Sampling Bias Audit

**Objective:** Determine whether the training sample faithfully represents the population the model will score in deployment — identifying segment-level coverage gaps, the selection mechanisms that skewed the sample, and where train/deployment distributions diverge — and produce severity-ranked, evidence-backed findings with mitigations, before the model is trusted to generalize.

**When to Use:**
- A model performs well in aggregate but you suspect it underserves certain segments.
- The training data came from a convenient or historical source that may not match who/what the model now scores.
- Before deployment, to check that the sample reflects the live population.

**When NOT to Use:**
- The concern is dirty values rather than representativeness (use `mldata_data_quality_audit.md`).
- The concern is train/test contamination or target leakage (use `mldata_data_leakage_detector.md`).
- You are deciding fairness mitigations on model outputs (this prompt audits the *data*, upstream of that).

## Inputs / Context

Provide what you can; the audit degrades gracefully if some are missing:
- **Deployment population definition** — who/what the model scores in production, and over what window.
- **Training sample profile** — segment counts/proportions (geography, demographics, device, time, channel, class).
- **Reference distribution** — known or estimated deployment proportions, census/market figures, or live traffic stats.
- **Selection mechanism** — how rows entered the sample (opt-in, historical decisions, instrument availability, survivorship).
- **Outcome by segment** — base rates or label availability per segment, if known.
- **Performance by slice** — any existing per-segment metrics.

## Constraints

**Must:**
- Compare the sample to an explicit reference (deployment) distribution; never call a sample "representative" without a stated reference.
- Require per-segment / per-slice evidence for any bias claim — aggregate numbers alone are insufficient.
- Identify the *selection mechanism* behind each gap (why it's skewed), not just the gap.

**Must Not:**
- Declare bias from a single aggregate statistic, or assert representativeness because the dataset is large.
- Invent reference proportions or segment figures the user did not provide — mark them "to be sourced."
- Conflate a difference in segment proportions with proven harm; flag where impact is unconfirmed and needs a slice-performance check.

**Instructions:**

1. **Define the deployment population and reference.** State precisely who/what the model scores and the reference proportions to compare against; if unavailable, identify how to source them and proceed with that caveat.

2. **Profile the sample by segment.** Break the training sample down across the segments that matter for the task (geography, demographics, device, time, channel, class) and tabulate proportions.

3. **Compare sample vs reference.** For each segment, quantify the divergence between sample and deployment proportions; flag under- and over-represented segments and segments with too few rows to even measure.

4. **Diagnose the selection mechanism.** For each significant gap, identify why it arose (opt-in/self-selection, historical-decision bias, survivorship, instrument/coverage limits, time-window mismatch) — this drives the right fix.

5. **Check coverage sufficiency.** Identify segments below the count needed for reliable training and per-slice evaluation, distinct from proportional skew.

6. **Tie gaps to likely impact.** Where slice performance exists, link coverage gaps to measured underperformance; where it doesn't, mark impact as suspected and specify the per-slice check to run.

7. **Rank and mitigate.** Order findings by (impact × confidence). For each, propose a mitigation (targeted collection, reweighting, stratified resampling, scope restriction, or documenting the limitation).

8. **State residual limits.** Note where the audit is bounded by missing reference data and what must be obtained to close the question.

**Output Format:**

A markdown report:
- **Population & Reference** — deployment definition + reference source (or gap).
- **Segment Coverage Table** — Segment | Sample % | Reference % | Divergence | Count | Sufficient?
- **Selection-Mechanism Diagnosis** — per gap: mechanism + why.
- **Findings (ranked)** — Finding | Severity | Evidence | Suspected/Confirmed impact | Mitigation.
- **Coverage Sufficiency Notes** — segments too small to train/measure.
- **Residual Limits** — reference data still needed.
- **INSUFFICIENT EVIDENCE** — the honest verdict when no reference distribution exists for the deployment population. Divergence is undefined without one, so state that and name the unblocking datum: a reference source (census, registry, upstream funnel counts) with its own coverage caveats, rather than treating the training sample's own distribution as the reference.

## Verification

- [ ] An explicit deployment reference distribution is named (or its absence flagged as a limit).
- [ ] Every bias claim has per-segment evidence, not an aggregate statistic.
- [ ] Each significant gap has an identified selection mechanism.
- [ ] Coverage sufficiency (absolute counts) is assessed separately from proportional skew.
- [ ] Impact is labeled confirmed (slice metric) vs suspected (needs a check); no invented reference figures.
- [ ] Where no reference distribution is available, the verdict is INSUFFICIENT EVIDENCE with the reference source named — the sample is not compared against itself.

## False-Positive Prevention

❌ **DON'T:**
- Call a dataset representative because it is large — size does not fix a skewed selection mechanism.
- Declare bias from an aggregate gap without showing which segments diverge and by how much.
- Treat a proportion mismatch as proven harm without a per-slice performance check.
- Assume the deployment distribution equals the historical training distribution when the population has shifted.

✅ **DO:**
- Compare the sample to an explicit, sourced reference distribution per segment.
- Name the selection mechanism (self-selection, survivorship, historical decisions) behind each gap so the fix targets the cause.
- Separate proportional skew from absolute under-coverage; both can break a segment but need different fixes.
- Label impact as confirmed vs suspected and specify the slice metric to confirm it.

## Example Output

```markdown
## Sampling Bias Audit: Credit Risk Model (deployment = all US applicants, 2026)

### Population & Reference
- Deployment: all incoming US applicants. Reference: prior-year applicant mix (sourced from intake logs).

### Segment Coverage Table
| Segment | Sample % | Reference % | Divergence | Count | Sufficient? |
|---|---|---|---|---|---|
| Urban | 71% | 58% | +13pp | 210k | Yes |
| Rural | 9% | 22% | −13pp | 12k | Borderline |
| Age <25 | 6% | 17% | −11pp | 8k | No (too few positives) |
| Thin-file applicants | 4% | 15% | −11pp | 5k | No |

### Selection-Mechanism Diagnosis
- Rural/under-25/thin-file under-represented: historical sample drawn from a branch-only channel; online
  applicants (younger, more rural, thin-file) entered only recently → time-window + channel selection bias.

### Findings (ranked)
| Finding | Severity | Evidence | Impact | Mitigation |
|---|---|---|---|---|
| Thin-file under-coverage | Critical | 4% vs 15%, <500 positives | Suspected (no slice metric yet) | Targeted collection; restrict scope until covered |
| Under-25 under-coverage | High | 6% vs 17% | Suspected | Stratified collection + reweighting |
| Urban over-representation | Medium | +13pp | Confirmed (urban recall 0.81 vs rural 0.69) | Reweight; monitor rural slice |

### Coverage Sufficiency Notes
- Thin-file and under-25 lack enough positives to estimate recall reliably — collect before claiming any slice metric.

### Residual Limits
- Reference proportions assume next-year mix ≈ prior-year; confirm against current live traffic before final sign-off.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** population → profile → compare → diagnose → rank.
- **RT-05 (Evidence-Based Reasoning):** every bias claim is anchored to per-segment figures.
- **QA-12 (False Positives Identification):** separates proportional skew, under-coverage, and proven harm.
- **DS-06 (Prioritization & Severity Guidance):** findings ranked by impact × confidence.
- **DS-02 (Metric Specification):** divergence quantified against a reference; slice metrics confirm impact.

**Related Prompts:**
- `mldata_dataset_curation_plan.md` — fix coverage gaps at the source via targeted sampling.
- `mldata_data_quality_audit.md` — a parallel, distinct concern (clean vs representative).
- `mldata_datasheet_authoring.md` — record the representativeness findings in the dataset's limitations.
