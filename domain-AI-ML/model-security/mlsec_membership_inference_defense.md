---
title: "Membership Inference Defense"
category: AI-ML/model-security
description: "Assess and reduce what a model leaks about who was in its training set — measuring the attack against a correctly matched non-member baseline, treating the generalization gap as the underlying cause, and stating what each mitigation does and does not protect."
techniques:
  - RT-02
  - DS-02
  - QA-12
  - CM-02
  - RT-05
difficulty: advanced
tags:
  - membership-inference
  - privacy-attack
  - generalization-gap
  - differential-privacy
  - model-security
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/model-security/mlsec_model_inversion_leakage_audit.md
  - domain-AI-ML/responsible-ai-governance/rai_differential_privacy_design.md
  - domain-AI-ML/responsible-ai-governance/rai_privacy_pii_assessment.md
  - domain-AI-ML/model-security/mlsec_ml_threat_model.md
---

# Membership Inference Defense

**Objective:** Determine whether a model reveals that a specific record was in its training set, measure that leakage against a properly matched non-member baseline, and reduce it — while being explicit that the underlying cause is usually the generalization gap and that each mitigation protects against some inference and not others.

**When to Use:**
- Training data is sensitive enough that *membership itself* is disclosive — patients in a condition-specific cohort, users of a service, people in an enforcement dataset.
- Before exposing scores, probabilities, or explanations to callers who could hold candidate records.
- When a privacy assessment or regulator question asks what the model reveals about individuals, and an evidenced answer is needed.

**When NOT to Use:**
- The training data is public or non-sensitive, and membership carries no consequence — say so and stop; the attack has no victim.
- The concern is reconstructing attribute values or inputs rather than membership — use `mlsec_model_inversion_leakage_audit.md`.
- You need a compliance mapping rather than a measurement — use `../responsible-ai-governance/rai_privacy_pii_assessment.md`.

## Inputs / Context

- **Why membership is sensitive** — the concrete harm if it were known that a given record was in the training set. This governs everything; without it the work has no target.
- **Model outputs exposed** — hard label, score, full distribution, loss, or explanations, and to whom.
- **Generalization gap** — train vs held-out performance, which is the strongest single predictor of leakage.
- **Training-set composition** — duplicates, near-duplicates, outliers, and small subgroups, which leak disproportionately.
- **Attacker's prior** — what a candidate record looks like to them, and whether they already suspect membership.
- **Existing privacy controls** — any DP training, regularization, or output restriction already applied.

## Constraints

**Must:**
- Measure attack success against a **matched non-member baseline** drawn from the same distribution — an attack evaluated against dissimilar non-members measures distribution discrimination, not membership.
- Report attack performance in terms that reflect the attacker's real position, and prioritize the **low false-positive-rate regime**: an attack that identifies a few members with high confidence is often more harmful than one with better average accuracy.
- Report per-subgroup leakage, since outliers, small subgroups, and duplicated records leak far more than the average.
- Treat the generalization gap as the primary lever and check it before reaching for privacy machinery.
- State for every mitigation what it protects against and what it leaves exposed.

**Must Not:**
- Report attack accuracy near 50% as "no leakage" without examining the low-FPR regime, where a usable attack can hide behind chance-level average accuracy.
- Assert privacy-budget values, attack-accuracy figures, or published leakage results from memory; mark any needed figure `[verify against a primary source]`.
- Describe differential privacy as protecting privacy without stating the budget, what it is defined over (record, user, group), and what it does not cover.
- Treat removing direct identifiers as membership protection — membership inference operates on the model's behaviour, not on stored fields.
- Generate a working attack implementation; describe the evaluation design instead.

**Instructions:**

1. **Establish why membership matters.** Write the concrete harm from a confirmed membership disclosure, and for whom. If no harm can be articulated, stop and record that.

2. **Measure the generalization gap first.** Train vs held-out performance, overall and per subgroup. A large gap is both the leading indicator of leakage and usually the cheapest thing to fix, and fixing it is independently valuable.

3. **Build a matched non-member set.** Draw non-members from the same population, matched on the attributes that drive model behaviour. State the matching explicitly — this is the step that most often invalidates a membership-inference evaluation.

4. **Evaluate the attack in the exposure you actually have.** Score-based, loss-based, or label-only depending on what callers receive. Do not evaluate a logits-based attack against an endpoint that returns a hard label; the result would not describe your exposure.

5. **Report in the low-FPR regime.** Give true-positive rate at low false-positive rates alongside any average measure, and lead with it. Say how many members an attacker could identify confidently, because that is the disclosure that happens.

6. **Break results out by subgroup.** Report leakage for outliers, small subgroups, duplicated and near-duplicated records separately. The average hides exactly the individuals most at risk, and they are frequently the individuals the sensitivity concern was about.

7. **Choose mitigations in cost order.**
   - **Close the generalization gap** — regularization, early stopping, more data, less capacity. Cheapest, and improves the model.
   - **Deduplicate and handle outliers** — remove near-duplicates; consider whether extreme outliers belong in training at all.
   - **Reduce output granularity** — coarsen or withhold scores, distributions, and explanations. Directly removes attack signal, at a stated cost to legitimate consumers.
   - **Differentially private training** — a formal guarantee, at a stated utility cost. Only here, and only with the budget and its unit written down.

8. **State each mitigation's coverage boundary.** For each: what it protects against and what it does not. DP at a record level does not bound what is learned about a user with many records; closing the generalization gap reduces average leakage while outliers may remain identifiable.

9. **Re-measure and state the residual.** Re-run the evaluation after mitigation, in the low-FPR regime and per subgroup, and state which individuals remain identifiable and what that means against the harm from step 1.

**Output Format:**

A markdown assessment:
- **Sensitivity Rationale** — the harm from a membership disclosure, and to whom.
- **Generalization Gap** — train vs held-out, overall and per subgroup.
- **Evaluation Setup** — matched non-member construction, exposure assumed, attack class.
- **Results** — table: Subgroup | TPR @ low FPR | Average attack accuracy | Members confidently identifiable.
- **Mitigation Plan** — table: Mitigation | Leakage reduction | Utility cost | Protects against | Does NOT protect against.
- **Post-Mitigation Residual** — re-measured, per subgroup, with the individuals still exposed.
- **Statement for a Privacy Reviewer** — what can honestly be said, with its conditions.
- **INSUFFICIENT EVIDENCE** — the correct result whenever the non-member set was not matched to the member set on distribution and collection period. An unmatched baseline makes the attack a distribution classifier, so both a high and a low score are uninterpretable. Name the unblocking datum: a matched non-member set, and the per-subgroup counts needed for TPR at the chosen low FPR.

## Verification

- [ ] The concrete harm from membership disclosure is stated before any measurement.
- [ ] Non-members are matched to members on the attributes that drive model behaviour, and the matching is described.
- [ ] The attack class matches the exposure actually offered to callers.
- [ ] TPR at low FPR is reported and led with, not only average accuracy.
- [ ] Per-subgroup results are reported, including outliers and duplicated records.
- [ ] The generalization gap is measured and addressed before privacy machinery is proposed.
- [ ] Every mitigation states both what it protects against and what it does not.
- [ ] Any DP recommendation names the budget and the unit it is defined over.
- [ ] No privacy budgets or attack figures are asserted from memory.
- [ ] No working attack implementation appears.
- [ ] Results built on an unmatched non-member set, or on subgroups too small for TPR at the chosen FPR, are reported as INSUFFICIENT EVIDENCE rather than as low leakage.

## False-Positive Prevention

❌ **DON'T:**
- Conclude "no membership leakage" from ~50% average attack accuracy — a strong attack in the low-FPR regime can sit underneath a chance-level average and is the one that causes disclosure.
- Evaluate against non-members drawn from a different distribution; you will measure how well the attack tells the two populations apart and report it as membership leakage.
- Report only an aggregate figure when the sensitivity concern was about a small subgroup — that subgroup is where leakage concentrates and where the average conceals it.
- Reach for differential privacy while a large generalization gap remains; the cheaper fix improves the model and removes most of the signal.
- Say "we apply differential privacy" without the budget and the unit — record-level DP says little about a user contributing many records.
- Treat identifier removal as a defense; the leak is in the model's behaviour, not in a stored column.

✅ **DO:**
- Anchor the whole assessment in the specific harm a confirmed membership would cause.
- Match non-members carefully and describe the matching, so the measurement means what it claims.
- Lead with TPR at low FPR and translate it into how many members are confidently identifiable.
- Report outliers, near-duplicates, and small subgroups separately and lead with the worst.
- Fix the generalization gap first and re-measure before considering formal privacy machinery.
- Write each mitigation's coverage boundary next to it, so a reviewer sees what remains uncovered.

## Example Output

```markdown
## Membership Inference: Readmission-Risk Model (specialty cardiology cohort)
Membership implies the person was a cardiology inpatient at this hospital in the study window.
That inference alone is disclosive regardless of the prediction, which is what makes this
model different from an ordinary tabular classifier.

### Sensitivity Rationale
A confirmed membership reveals a specific individual's care episode at a named institution to
anyone holding a candidate record — an insurer, an employer, or a family member. Harm does not
require the prediction; the fact of inclusion is the disclosure.

### Generalization Gap
| Slice | Train AUC | Held-out AUC | Gap |
|---|---|---|---|
| Overall | 0.913 | 0.847 | **0.066** |
| Age <40 (n=412) | 0.968 | 0.782 | **0.186** |
| Age 40–75 | 0.905 | 0.851 | 0.054 |
| Rare comorbidity set (n=190) | 0.981 | 0.744 | **0.237** |

The two small subgroups are heavily memorized. That is the leak, visible before any attack.

### Evaluation Setup
Non-members drawn from the **same hospital, same window, cardiology inpatients excluded from
training** — matched on age band, sex, primary diagnosis category, and length of stay. Without
this matching the attack would separate cardiology from non-cardiology patients and we would
misreport that as membership leakage. Exposure evaluated: **score-based**, since the model
returns a calibrated risk score to clinicians.

### Results
| Subgroup | TPR @ 0.1% FPR | TPR @ 1% FPR | Avg attack acc | Confidently identifiable |
|---|---|---|---|---|
| Overall | 3.1% | 9.4% | 0.561 | ~2,100 of 68k |
| Age <40 | **19.7%** | 34.2% | 0.643 | **~81 of 412** |
| Rare comorbidity set | **28.4%** | 41.1% | 0.688 | **~54 of 190** |
| Age 40–75 | 1.9% | 6.8% | 0.539 | ~1,900 of 64k |

Average accuracy of 0.561 overall reads as weak. It is not the number that matters: in the
rare-comorbidity subgroup an attacker holding a candidate record confirms membership for more
than a quarter of them at a 0.1% false-positive rate. Those are exactly the individuals whose
membership is most disclosive.

### Mitigation Plan
| Mitigation | Leakage reduction | Utility cost | Protects against | Does NOT protect against |
|---|---|---|---|---|
| Early stopping + stronger L2 | large in the memorized subgroups | held-out AUC −0.004 | memorization-driven leakage | an attacker with auxiliary data |
| Merge rare comorbidity set into a coarser category | large for n=190 group | small loss of clinical granularity | small-subgroup identifiability | leakage from other outliers |
| Return risk **band** instead of continuous score | moderate–large | clinicians lose fine ordering | score-based attacks | label-only attacks |
| DP-SGD, record-level budget | formal bound | AUC −0.03 to −0.06 `[verify on your data]` | bounded per-record influence | a patient with **many** episodes — record-level ≠ patient-level |

### Post-Mitigation Residual
After early stopping, category merging, and banded output, re-measured:
| Subgroup | TPR @ 0.1% FPR (before → after) |
|---|---|
| Age <40 | 19.7% → **4.2%** |
| Rare comorbidity (now merged) | 28.4% → **5.1%** |
| Overall | 3.1% → 1.8% |

Still exposed: patients with multiple episodes in the window. Record-level controls do not
bound what accumulates across a patient's several records, and no mitigation above is defined
at the patient level. If patient-level protection is required, the DP unit must change and the
utility cost must be re-estimated.

### Statement for a Privacy Reviewer
"Under a matched-baseline score-based evaluation, no subgroup exceeds a 5.1% true-positive
rate at a 0.1% false-positive rate after mitigation, down from 28.4%. This holds for
record-level membership. Patients contributing multiple episodes are not covered by these
controls and remain the open item. The measurement assumes the attacker sees banded scores;
restoring continuous scores invalidates it."
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** exposure × subgroup × attack regime is the measurement grid.
- **DS-02 (Metric Specification):** TPR at low FPR is specified as the reportable metric precisely because average accuracy misleads here.
- **QA-12 (False Positives Identification):** the matched-baseline requirement rejects results that measure distribution discrimination instead of membership.
- **CM-02 (Constraint Specification):** coverage-boundary and DP-unit disclosure rules bound what may be claimed.
- **RT-05 (Evidence-Based Reasoning):** the privacy statement is tied to measured quantities and their conditions.

**Related Prompts:**
- `mlsec_model_inversion_leakage_audit.md` — when the concern is reconstructing attributes or inputs, not membership.
- `../responsible-ai-governance/rai_differential_privacy_design.md` — if a formal guarantee is required, including choosing the unit.
- `../responsible-ai-governance/rai_privacy_pii_assessment.md` — the compliance-facing counterpart.
- `mlsec_ml_threat_model.md` — establishes whether this attack class applies to your exposure.
