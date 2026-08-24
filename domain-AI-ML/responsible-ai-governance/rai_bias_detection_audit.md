---
title: "Model Bias Detection Audit"
category: AI-ML/responsible-ai-governance
description: "Audit a model for disparate performance and outcomes across protected and relevant groups using slice-level and intersectional evidence tied to a stated fairness definition."
techniques:
  - ST-02
  - RT-05
  - QA-12
  - QA-17
  - DS-06
difficulty: advanced
tags:
  - fairness
  - bias-audit
  - slice-analysis
  - intersectionality
  - responsible-ai
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_fairness_metric_selection.md
  - domain-AI-ML/responsible-ai-governance/rai_fairness_mitigation_strategy.md
  - domain-AI-ML/responsible-ai-governance/rai_model_card_authoring.md
---

# Model Bias Detection Audit

**Objective:** Audit a model for bias by measuring performance and outcomes across protected and relevant groups — including intersectional subgroups — against an explicitly stated fairness definition, and produce a ranked, evidence-backed report that distinguishes measured disparities from confirmed harm and from causal claims.

**When to Use:**
- Before deploying a model that affects people (lending, hiring, healthcare, content moderation, pricing).
- After a complaint, incident, or regulator inquiry about discriminatory outcomes.
- Periodically, as a monitoring control on a deployed model.
- When inheriting a model whose group-level behavior has never been measured.

**When NOT to Use:**
- To *choose* which fairness metric applies (use `rai_fairness_metric_selection.md` first — this audit assumes a definition is chosen).
- To *fix* a disparity once found (use `rai_fairness_mitigation_strategy.md`).
- When no group labels exist and none can be ethically/legally obtained — note the gap rather than inferring protected attributes.

## Inputs / Context

Provide what you can; the audit degrades gracefully if some are missing:
- **Decision context** — what the model decides, the stakes for the affected person, and the applicable jurisdiction/regulatory frame (ask the user; do not assume).
- **Stated fairness definition** — the chosen criterion (e.g., demographic parity, equal opportunity, equalized odds, calibration). If absent, stop and route to metric selection.
- **Group attributes** — protected and relevant grouping variables available (or proxies, clearly labeled as proxies), and their source/quality.
- **Predictions + ground truth** — scores, thresholds, labels, per-row group membership; or aggregated confusion matrices per group.
- **Base rates** — outcome prevalence per group, and whether label quality itself differs by group.

## Constraints

**Must:**
- State the fairness definition being measured *before* reporting any number; report metrics consistent with that definition.
- Report per-group AND intersectional (e.g., group A × group B) slices, with sample size per slice.
- Attach a confidence/uncertainty indicator (sample size, confidence interval) to every disparity.
- Separate a measured disparity from a claim of unfairness, and both from a causal claim about *why* the disparity exists.

**Must Not:**
- Declare the model "fair" or "biased" from aggregate metrics alone — require slice-level evidence and a stated definition.
- Fabricate or invent regulatory citations, statute text, or article numbers; if the legal standard is unknown, say so and ask the user to confirm.
- Infer protected attributes for individuals where doing so is prohibited or unreliable, then treat the inference as ground truth.
- Read a disparity as proof of causation (the model *causing* harm) without ruling out label bias, base-rate differences, and sampling.

**Instructions:**

1. **Confirm the fairness definition and stakes.** Restate the chosen definition and why it fits the decision's harm profile. Note that several definitions conflict mathematically — you are measuring against *this* one, not all of them.

2. **Inventory groups and slice sizes.** List protected/relevant attributes, define the slices (including intersections), and record sample size per slice. Flag slices too small for reliable estimates.

3. **Compute per-group performance and outcomes.** For each slice, report the metrics tied to the definition (e.g., TPR/FPR for equalized odds; selection rate for demographic parity; calibration for calibration) plus a shared accuracy/error metric for context.

4. **Compute intersectional slices.** Repeat for combinations; surface subgroups where a disparity appears only at the intersection (hidden by marginal views).

5. **Quantify disparities with uncertainty.** Express gaps as ratios/differences with confidence intervals or sample-size caveats. Distinguish statistically and practically significant gaps from noise.

6. **Interrogate the source of each disparity.** For the largest gaps, ask whether the driver is the model, label bias, base-rate differences, feature availability, or sampling — and what evidence would discriminate among these.

7. **Rank findings by (harm severity × disparity magnitude × confidence).** Order remediation attention; do not equate a large gap on a low-stakes slice with a small gap on a high-stakes one.

8. **State the limits of the audit.** Note groups not measured, proxy usage, label-quality concerns, and what a fix would (and would not) resolve.

**Output Format:**

A markdown report:
- **Audit Frame** — stated fairness definition, decision stakes, jurisdiction (or "to be confirmed by user")
- **Slice Coverage** — table of groups/intersections with sample sizes; flagged small slices
- **Disparity Findings** — table: Slice | Metric (per definition) | Value | Reference | Gap (with CI) | Confidence
- **Ranked Concerns** — top disparities by severity × magnitude × confidence, each with a source hypothesis (model vs label vs base rate)
- **Causation Caveats** — what is correlation vs what would establish causation
- **Limits & Open Questions** — unmeasured groups, proxy risks, label-quality gaps
- **INSUFFICIENT EVIDENCE** — an enumerated value in the Confidence column, for slices below the sample size the chosen metric needs and for groups with no available labels. A gap computed on a handful of examples is noise that will be read as a finding; state the count that would support the metric, or the group-label source that would make the slice measurable at all.

## Verification

- [ ] A single fairness definition is stated before any metric is reported.
- [ ] Every reported disparity has a sample size and uncertainty indicator.
- [ ] Intersectional slices were computed, not just marginal groups.
- [ ] No "fair"/"biased" verdict appears without slice evidence + the stated definition.
- [ ] Each top finding separates measured gap from unfairness claim from causal claim.
- [ ] No regulatory text or article number is invented; legal standard is user-confirmed or flagged unknown.
- [ ] Slices too small for the chosen metric, and groups with no labels, are reported as INSUFFICIENT EVIDENCE with the required count or label source named — never as "no disparity found."

## False-Positive Prevention

❌ **DON'T:**
- Call a model "fair because overall accuracy is equal" — aggregate parity can hide large intersectional gaps.
- Report a disparity on a 19-row slice as if it were stable.
- Treat a higher false-positive rate for a group as proof the *model* is the cause when group base rates and label quality differ.
- Switch fairness definitions mid-report to make the model look better (or worse).

✅ **DO:**
- Fix one fairness definition up front and measure against it consistently.
- Always pair a disparity with its slice size and a confidence interval.
- Compute intersectional slices and surface gaps invisible in marginal views.
- Label each finding: measured gap (data), fairness concern (vs definition), or causal hypothesis (needs further design) — and keep them distinct.

## Example Output

```markdown
## Bias Audit: Resume-Screening Classifier v4

### Audit Frame
- Fairness definition: **Equal opportunity** (equal TPR across groups for qualified candidates).
- Stakes: gate to a human interview; false negatives deny opportunity.
- Jurisdiction/standard: **to be confirmed by user** — anti-discrimination obligations not assumed.

### Slice Coverage
| Slice | N | Reliable? |
|---|---|---|
| Group A | 12,400 | Yes |
| Group B | 3,110 | Yes |
| Group A × Age 50+ | 410 | Borderline |
| Group B × Age 50+ | 88 | No — too small |

### Disparity Findings
| Slice | TPR | Reference (Group A) | Gap (95% CI) | Confidence |
|---|---|---|---|---|
| Group B | 0.71 | 0.83 | -0.12 (-0.16, -0.08) | High |
| Group A × Age 50+ | 0.74 | 0.83 | -0.09 (-0.18, 0.00) | Medium |
| Group B × Age 50+ | 0.66 | 0.83 | -0.17 (wide) | Low (N=88) |

### Ranked Concerns
1. **Group B TPR gap (-0.12, High).** Qualified Group-B candidates are advanced at a lower rate. Source hypothesis: model and/or training-label bias — label quality by group is unverified (open question). Not yet established as model-caused.

### Causation Caveats
- The TPR gap is a measured disparity, not proof the model causes it; historical labels may encode prior screening bias.

### Limits & Open Questions
- Group B × Age 50+ is unmeasurable at N=88; collect more data before any verdict.
- No attribute available for disability status; that dimension is unaudited.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** definition → slices → metrics → intersections → ranking.
- **RT-05 (Evidence-Based Reasoning):** every disparity anchored to a slice with size and CI.
- **QA-12 (False Positives Identification):** separates measured gap from unfairness from causation.
- **QA-17 (Named Scores for Multi-Dimensional Metrics):** per-group, per-definition scorecard.
- **DS-06 (Prioritization & Severity Guidance):** ranks by severity × magnitude × confidence.

**Related Prompts:**
- `rai_fairness_metric_selection.md` — choose the definition this audit measures against.
- `rai_fairness_mitigation_strategy.md` — act on confirmed disparities.
- `rai_model_card_authoring.md` — document per-group performance for release.
