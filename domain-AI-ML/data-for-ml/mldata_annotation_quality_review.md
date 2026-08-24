---
title: "ML Annotation Quality Review"
category: AI-ML/data-for-ml
description: "Assess label quality with the right agreement metric (Cohen's/Fleiss' kappa, Krippendorff's alpha), gold-set accuracy, and a disagreement-adjudication plan — separating noisy annotators from ambiguous guidelines."
techniques:
  - ST-02
  - RT-05
  - DS-02
  - QA-12
  - DS-06
difficulty: advanced
tags:
  - annotation-quality
  - inter-annotator-agreement
  - kappa
  - krippendorff-alpha
  - adjudication
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_labeling_guideline_designer.md
  - domain-AI-ML/data-for-ml/mldata_data_quality_audit.md
  - domain-AI-ML/data-for-ml/mldata_dataset_curation_plan.md
---

# ML Annotation Quality Review

**Objective:** Evaluate the quality of a labeled dataset by selecting and computing the appropriate inter-annotator agreement metric, checking annotators against a trusted gold set, diagnosing whether disagreement stems from noisy annotators or ambiguous guidelines, and producing an adjudication plan to resolve disputed labels before the data trains a model.

**When to Use:**
- After a labeling round, to decide whether the labels are trustworthy enough to train on.
- When two pipelines/annotators disagree and you need to know which (if either) is right.
- To monitor an ongoing annotation operation for drift in quality.

**When NOT to Use:**
- You are writing the rules before labeling (use `mldata_labeling_guideline_designer.md`).
- The concern is feature/value quality rather than label correctness (use `mldata_data_quality_audit.md`).

## Inputs / Context

Provide what you can; the review degrades gracefully if some are missing:
- **Label schema** — categorical (nominal/ordinal), spans, or continuous; single- vs multi-label.
- **Annotation structure** — how many annotators, how much overlap (items labeled by ≥2), and which items.
- **Raw annotations** — per-item, per-annotator labels (or a confusion/agreement summary).
- **Gold/expert labels** — any trusted subset, and how it was produced.
- **Guideline version** — the rulebook annotators used.
- **Intended use** — how the labels feed the model, which sets the agreement bar.

## Constraints

**Must:**
- Choose the agreement metric that matches the schema (e.g., Cohen's κ for 2 nominal raters, Fleiss' κ for many, Krippendorff's α for missing data/ordinal/interval, weighted κ for ordinal) and justify the choice.
- Report agreement with its interpretation and, where possible, an uncertainty range — never a bare number with no context.
- Separate "annotators are inconsistent" from "the guideline is ambiguous" using the pattern of disagreement.

**Must Not:**
- Report an agreement statistic, kappa value, or gold accuracy as fact if it was not supplied or computable from the provided annotations — mark it "to compute."
- Treat raw percent agreement as sufficient for skewed class distributions (it ignores chance).
- Recommend discarding an annotator on one metric without checking gold accuracy and per-class patterns.

**Instructions:**

1. **Confirm schema and agreement design.** Establish label type, number of annotators, and the overlap structure, since these determine which metric is valid.

2. **Select and justify the metric.** Pick the correct agreement coefficient for the schema and design; explain why percent-agreement alone is insufficient (chance, class skew) and what the chosen metric corrects for.

3. **Compute or specify agreement.** Report overall and per-class agreement; flag classes with much lower agreement. Where data to compute is missing, specify exactly what to calculate.

4. **Check against gold.** Score each annotator's accuracy on the gold subset; distinguish low agreement caused by one weak annotator from systematic confusion shared by all.

5. **Diagnose the source of disagreement.** Inspect the confusion structure: if specific label *pairs* drive disagreement across annotators, suspect the guideline; if one annotator diverges everywhere, suspect that annotator.

6. **Design adjudication.** Specify how disputed items are resolved (majority, expert tie-break, discussion-to-consensus) and which items must be re-labeled vs accepted.

7. **Recommend guideline/annotator actions.** For guideline-driven confusion, propose the specific definition/edge-case fix; for annotator-driven noise, propose retraining, re-labeling, or removal — with the evidence for each.

8. **Set the acceptance bar.** State the agreement/gold threshold the labels must meet for the intended use, and whether the dataset passes, with caveats per class.

**Output Format:**

A markdown report:
- **Agreement Summary** — chosen metric + value + interpretation + per-class table.
- **Gold-Set Performance** — per-annotator accuracy on gold.
- **Disagreement Diagnosis** — guideline-driven vs annotator-driven, with the confusion evidence.
- **Adjudication Plan** — resolution rule + which items to re-label.
- **Recommended Actions** — ranked: guideline fixes, annotator actions.
- **Acceptance Decision** — pass/fail vs the stated bar, per-class caveats.
- **INSUFFICIENT EVIDENCE** — the correct acceptance decision when no items were labelled independently by more than one annotator, or when the doubly-labelled subset is too small for the chosen agreement statistic. State the unblocking datum: the number of items needing independent double-labelling, and for which classes.

## Verification

- [ ] The agreement metric matches the schema and design, with the choice justified.
- [ ] Agreement is reported with interpretation (and uncertainty where possible), not as a bare number.
- [ ] Per-class agreement is reported and low-agreement classes are isolated.
- [ ] Disagreement is attributed to guideline vs annotator using the confusion pattern, not assumed.
- [ ] Values not computable from the input are marked "to compute," not invented.
- [ ] If no doubly-labelled subset (or no gold set) exists, the acceptance decision is INSUFFICIENT EVIDENCE with the double-labelling volume named — not a pass inferred from throughput or annotator seniority.

## False-Positive Prevention

❌ **DON'T:**
- Report raw percent agreement as the headline on a skewed dataset — high agreement can be pure chance when one class dominates.
- Use Cohen's κ for more than two annotators or for ordinal labels where weighting matters.
- Blame an annotator for low agreement that is actually a confusable label pair affecting everyone.
- Treat a single kappa cutoff (e.g., "0.6 is good") as universal across tasks and class skews.

✅ **DO:**
- Choose a chance-corrected metric appropriate to raters/scale/missingness and report per-class breakdowns.
- Cross-check agreement against gold accuracy to separate "consistently wrong together" from "inconsistent."
- Read the confusion structure: pair-specific disagreement → fix the guideline; person-specific → address the annotator.
- Set the acceptance threshold from the downstream cost of label noise for *this* task, not a generic rule of thumb.

## Example Output

```markdown
## Annotation Quality Review: Toxicity Labeling Round 3

### Agreement Summary
- Schema: 4 annotators, nominal {none, mild, severe}, ordinal-ish → weighted Fleiss' κ.
- Overall κ_w = 0.61 (substantial), 95% bootstrap ≈ [0.57, 0.65].
| Class | κ_w | Note |
|---|---|---|
| none | 0.78 | strong |
| mild | 0.41 | weak — drives overall down |
| severe | 0.69 | acceptable |

### Gold-Set Performance (n=300 gold)
| Annotator | Gold acc | Note |
|---|---|---|
| A1 | 0.91 | strong |
| A2 | 0.89 | strong |
| A3 | 0.72 | low on `mild` |
| A4 | 0.63 | low across classes — retrain/remove |

### Disagreement Diagnosis
- `none↔mild` confusion appears across ALL annotators → guideline-driven (the mild threshold is under-defined).
- A4 diverges on every class → annotator-driven noise (separate from the guideline issue).

### Adjudication Plan
- Items with ≥2-way split on `mild`: expert tie-break (n≈420).
- A4's solo labels: re-labeled by A1/A2.

### Recommended Actions
1. Guideline fix: add explicit `none` vs `mild` threshold + 3 near-miss examples.
2. A4: retrain; if next-round gold < 0.80, remove and re-label A4's data.

### Acceptance Decision
- FAIL for `mild` (κ_w 0.41 < 0.60 bar). PASS for none/severe. Re-label `mild` after guideline fix before training.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** schema → metric → compute → gold → diagnose → adjudicate.
- **RT-05 (Evidence-Based Reasoning):** every diagnosis is tied to the confusion pattern and gold accuracy.
- **DS-02 (Metric Specification):** selects the chance-corrected agreement metric matched to the schema.
- **QA-12 (False Positives Identification):** separates annotator noise from guideline ambiguity.
- **DS-06 (Prioritization & Severity Guidance):** actions ranked; per-class acceptance decision.

**Related Prompts:**
- `mldata_labeling_guideline_designer.md` — fix the guideline ambiguities this review surfaces.
- `mldata_data_quality_audit.md` — a parallel review of feature/value quality (not labels).
- `mldata_dataset_curation_plan.md` — plan the gold and overlap structure that makes this review possible.
