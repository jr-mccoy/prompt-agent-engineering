---
title: "ML Synthetic Data Strategy"
category: AI-ML/data-for-ml
description: "Decide when and how to use synthetic data — weighing fidelity, privacy guarantees, and distribution-shift risk — and how to validate that it helps rather than quietly degrades the model."
techniques:
  - ST-02
  - RT-02
  - DT-04
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - synthetic-data
  - data-fidelity
  - privacy
  - distribution-shift
  - generative-models
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_data_augmentation_plan.md
  - domain-AI-ML/data-for-ml/mldata_class_imbalance_strategy.md
  - domain-AI-ML/data-for-ml/mldata_datasheet_authoring.md
---

# ML Synthetic Data Strategy

**Objective:** Decide whether synthetic data should be used for a given purpose (privacy, rare-case coverage, augmentation, cold-start) and, if so, specify the generation approach, the fidelity and privacy guarantees it must meet, and the validation protocol that proves it improves the model without introducing distribution shift or leaking private information.

**When to Use:**
- Real data is restricted by privacy/regulation and you need a shareable or trainable substitute.
- Rare/critical cases are too scarce to collect and you're considering generating them.
- You must decide between collecting more real data, augmenting, or synthesizing.

**When NOT to Use:**
- You only need label-preserving transforms of existing records (use `mldata_data_augmentation_plan.md`).
- The issue is purely class balance solvable by weighting (use `mldata_class_imbalance_strategy.md`).

## Inputs / Context

Provide what you can; the strategy degrades gracefully if some are missing:
- **Purpose** — privacy substitution, rare-case coverage, augmentation, or bootstrapping a cold-start model.
- **Modality & schema** — tabular/text/image/time-series; fields, types, key relationships and constraints.
- **Real data available** — how much, how representative, and its sensitivity/regulatory status.
- **Privacy requirement** — the standard to meet (e.g., differential privacy budget, re-identification risk tolerance).
- **Fidelity needs** — which statistical properties and correlations must be preserved for the downstream task.
- **Deployment distribution** — what the model must perform on in production.

## Constraints

**Must:**
- Justify synthetic data against alternatives (collect more real, augment, reweight) before recommending it.
- Specify the fidelity criteria (marginals, joint correlations, constraint satisfaction) and the privacy guarantee with how each will be measured.
- Validate utility by the "train-on-synthetic, test-on-real" (TSTR) principle — synthetic data is judged by real-world downstream performance, never by how realistic it looks.

**Must Not:**
- Claim a privacy guarantee (e.g., "anonymous," "DP") as fact without a stated mechanism and budget — privacy is not free from generation.
- Assume synthetic data matches the real distribution; treat distribution shift and mode collapse as default risks to test for.
- Recommend training and evaluating on synthetic data and reporting those metrics as production estimates.

**Instructions:**

1. **Clarify the purpose and the bar it sets.** Different purposes (privacy vs rare-case coverage vs cold-start) demand different fidelity/privacy tradeoffs; state which dominates.

2. **Compare to alternatives.** Weigh synthetic generation against collecting more real data, augmentation, and reweighting on cost, fidelity, privacy, and time — recommend synthetic only where it wins.

3. **Choose the generation approach.** Map the modality and fidelity needs to an approach (rule/simulation-based, statistical/copula, or learned generative model), noting constraint handling and data-volume requirements.

4. **Define fidelity criteria.** Specify the statistics that must be preserved (per-field marginals, cross-field correlations, business-rule constraints, conditional distributions for rare cases) and how each is checked.

5. **Define the privacy guarantee.** State the mechanism (e.g., DP training, k-anonymity, hold-out membership tests) and how re-identification / membership-inference risk will be measured — never assert privacy by virtue of being "synthetic."

6. **Specify the real/synthetic blend and placement.** Decide the mix ratio and whether synthetic is used for pretraining, augmentation, or full substitution; keep the *test* set real and untouched by synthetic data.

7. **Validate with TSTR and shift checks.** Require train-on-synthetic/test-on-real (and TRTR/TSTR comparison), plus distribution-shift and mode-coverage diagnostics on real holdouts and per slice.

8. **State residual risks and governance.** Flag distribution shift, amplified bias from the generator, privacy leakage, and document the synthetic process for the dataset's datasheet.

**Output Format:**

A markdown strategy:
- **Purpose & Dominant Tradeoff** — why synthetic, what bar it sets.
- **Alternatives Comparison** — table: Option | Fidelity | Privacy | Cost/time | Verdict.
- **Generation Approach** — method + constraint handling + data needs.
- **Fidelity Criteria** — statistics preserved + checks.
- **Privacy Guarantee** — mechanism + measurement.
- **Blend & Placement** — mix ratio; real test set untouched.
- **Validation (TSTR)** — protocol + shift/mode-coverage checks.
- **Risks & Governance** — shift, bias amplification, privacy; datasheet note.

## Verification

- [ ] Synthetic data is justified against real-collection/augmentation/reweighting alternatives.
- [ ] Fidelity criteria are explicit (marginals, correlations, constraints) with measurement methods.
- [ ] The privacy guarantee names a mechanism and a measurement, not a bare "it's synthetic so it's private."
- [ ] Utility is validated by train-on-synthetic/test-on-real on a real holdout, per slice.
- [ ] The real test set is kept free of synthetic data; distribution-shift risk is tested, not assumed away.

## False-Positive Prevention

❌ **DON'T:**
- Assume synthetic data is automatically private — generators can memorize and leak real records.
- Judge synthetic data by how realistic samples look; visual/spot realism doesn't imply downstream utility.
- Train and evaluate on synthetic data and report those numbers as production performance.
- Generate rare cases from a model fit on almost no rare data — it will hallucinate an unrepresentative tail.

✅ **DO:**
- State the privacy mechanism (DP budget, membership-inference test) and measure re-identification risk.
- Validate with train-on-synthetic/test-on-real against a real baseline, per slice, and check distribution shift + mode coverage.
- Keep the test set real and untouched; use synthetic only for train/pretrain/augment.
- Compare against simply collecting/augmenting real data, and recommend synthetic only where it demonstrably wins.

## Example Output

```markdown
## Synthetic Data Strategy: Shareable Clinical Tabular Dataset

### Purpose & Dominant Tradeoff
- Purpose: privacy-preserving substitute to share with an external research partner. Privacy dominates fidelity.

### Alternatives Comparison
| Option | Fidelity | Privacy | Cost/time | Verdict |
|---|---|---|---|---|
| Share real (de-id) | High | Weak (re-id risk) | Low | Rejected (regulatory) |
| DP-synthetic (learned) | Medium | Strong (DP budget) | Medium | Chosen |
| Augmentation | N/A (not shareable) | N/A | Low | Not applicable |

### Generation Approach
- DP-trained generative model for tabular; enforce schema constraints (age 0–120, valid ICD codes) post-hoc.
- Needs ≥ ~20k real rows for stable estimates; below that, fidelity degrades.

### Fidelity Criteria
- Preserve per-field marginals (KS distance < 0.1), top-20 cross-field correlations (Δ corr < 0.1),
  and the comorbidity conditional structure used by the downstream model.

### Privacy Guarantee
- (ε, δ)-DP at a stated budget; run membership-inference attack — require AUC ≈ 0.5 (no advantage).

### Blend & Placement
- Partner trains fully on synthetic; OUR internal test set stays 100% real for the production estimate.

### Validation (TSTR)
- Train downstream model on synthetic, test on real holdout; compare to train-on-real/test-on-real.
  Accept if TSTR within 3pp AUC and per-subgroup gaps don't widen.

### Risks & Governance
- Distribution shift on rare comorbidities (test per slice); generator may amplify majority bias.
- Document generator, ε, and validation in the dataset datasheet.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** purpose → alternatives → method → fidelity → privacy → validation.
- **RT-02 (Multi-Dimensional Analysis Framework):** options weighed on fidelity, privacy, cost jointly.
- **DT-04 (Decision Criteria Specification):** explicit accept/reject criteria for synthetic vs alternatives.
- **CM-02 (Constraint Specification):** fidelity and privacy guarantees are governing constraints.
- **QA-12 (False Positives Identification):** preempts the "synthetic = private/useful" and shift fallacies.

**Related Prompts:**
- `mldata_data_augmentation_plan.md` — the lighter-weight alternative when transforms suffice.
- `mldata_class_imbalance_strategy.md` — decide if synthesis is the right minority-class lever at all.
- `mldata_datasheet_authoring.md` — document the synthetic generation process for the dataset.
