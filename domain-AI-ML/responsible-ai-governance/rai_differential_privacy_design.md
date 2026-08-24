---
title: "Differential Privacy Design"
category: AI-ML/responsible-ai-governance
description: "Design a differentially private training or release pipeline — fixing the unit of privacy before the budget, accounting composition across every release, pricing the utility cost, and stating what the guarantee does and does not cover."
techniques:
  - ST-02
  - DS-02
  - CM-02
  - QA-12
  - RT-05
difficulty: advanced
tags:
  - differential-privacy
  - privacy-budget
  - dp-sgd
  - composition
  - privacy-unit
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_privacy_technique_selection.md
  - domain-AI-ML/responsible-ai-governance/rai_federated_learning_governance.md
  - domain-AI-ML/model-security/mlsec_membership_inference_defense.md
  - domain-AI-ML/data-for-ml/mldata_synthetic_data_strategy.md
---

# Differential Privacy Design

**Objective:** Design a differentially private pipeline whose guarantee means what its stakeholders think it means — fixing the unit of privacy before any budget is chosen, accounting composition across every release from the same data, pricing the utility cost honestly, and writing down what the guarantee does not cover.

**When to Use:**
- `rai_privacy_technique_selection.md` selected differential privacy and you must now specify it.
- A DP claim is already being made and you need to check whether the unit, budget, and composition actually support it.
- Releasing statistics, a synthetic dataset, or a model trained on data where individual influence must be formally bounded.

**When NOT to Use:**
- The threat is data movement rather than what a release reveals — use `rai_federated_learning_governance.md`.
- No disclosure scenario has been named; DP without a scenario is a utility loss with no protection. Run the selection prompt first.
- You need to measure empirical leakage rather than bound it formally — use `../model-security/mlsec_membership_inference_defense.md`.

## Inputs / Context

- **The disclosure scenario** DP is answering, from the selection step.
- **Unit of privacy** — record, user, household, group, or organization, as the scenario requires.
- **Contribution structure** — how many records one unit can contribute, and whether that is bounded or unbounded in the raw data.
- **Everything released from this data** — models, statistics, dashboards, evaluation results, prior releases. Composition covers all of them.
- **Utility floor** — the metric and value below which the release is not worth making.
- **Release cadence** — one-off, periodic, or continuous, since repeated release is where budgets are silently exhausted.

## Constraints

**Must:**
- Fix the **unit of privacy before the budget**. A budget attached to the wrong unit is a number with no bearing on the scenario, and this is the most common way a DP deployment fails to protect anyone.
- Bound each unit's contribution explicitly — by capping records per unit before training — since a formal guarantee over a unit requires a known maximum influence.
- Account composition across **every** release derived from the same data, including evaluation runs, hyperparameter searches, and prior public statistics.
- Price utility at the chosen budget by measuring, not estimating, and compare against the floor.
- State what the guarantee does not cover: correlations between units, information already public, group-level inference, and anything released outside the accounted pipeline.

**Must Not:**
- Assert budget values, noise multipliers, or utility-loss figures from memory; every quantity is `[measure on your data]` or `[verify against a primary source]`.
- Present a budget as "strong" or "weak" without reference to the unit and the scenario — the same number means very different things at record and user level.
- Report a per-run budget as the total when multiple runs, tuning sweeps, or repeated releases occur.
- Describe DP as making data anonymous or as removing the need for access control; it bounds individual influence on a release and nothing else.
- Let hyperparameter tuning run on the sensitive data outside the accounting and then report the final run's budget as the guarantee.

**Instructions:**

1. **Restate the scenario and fix the unit.** Write the disclosure being bounded and the unit that scenario implies. If a person can appear as many records, the unit is the person, and record-level accounting will not protect them. State this before anything else.

2. **Bound contribution per unit.** Determine the maximum records one unit contributes in the raw data. If unbounded, cap it explicitly by sampling or truncation before training, and record the cap — the guarantee depends on it. State what capping costs in representativeness.

3. **Enumerate every release from this data.** Model artifacts, published statistics, evaluation results, dashboards, and prior releases. Composition accounts for all of them; anything omitted here is spent budget you are not counting.

4. **Choose the mechanism per release type.** Noisy gradient training for models, output perturbation for statistics, a DP generator for synthetic data. State which is used where, and note that a DP generator is what makes downstream synthetic data private — the synthetic data is not private by itself.

5. **Set the accounting method and the total.** Choose the composition accounting approach, state the total budget across all releases, and show how it divides. Present the total, not the per-run figure, as the guarantee.

6. **Handle tuning explicitly.** Hyperparameter search on sensitive data consumes budget. Either account for it, run it on public or synthetic proxy data, or state plainly that it was not accounted and that the reported guarantee is therefore optimistic. This is the most frequently unstated leak in a DP pipeline.

7. **Measure utility at the chosen budget.** Run the pipeline and measure against the floor, overall and per subgroup — DP costs small subgroups disproportionately, and an aggregate utility number hides that.

8. **Write the coverage boundary.** What the guarantee covers, and what it does not: correlations between units, group-level inference, public information, and any release outside the accounting.

9. **Define the operational controls.** Who can spend budget, how spend is tracked, what happens when it is exhausted, and how a request for a new release is reviewed against the remaining total.

**Output Format:**

A markdown design:
- **Scenario & Unit** — the disclosure bounded, the unit, and why.
- **Contribution Bound** — max records per unit, capping method, representativeness cost.
- **Release Inventory** — every release from this data, with its mechanism.
- **Budget Accounting** — total, division across releases, accounting method, tuning treatment.
- **Utility Measurement** — table: Metric | No DP | With DP | Floor | Pass/fail, overall and per subgroup.
- **Coverage Boundary** — covered vs not covered.
- **Operational Controls** — ownership, tracking, exhaustion behaviour.
- **Honest Statement** — what may be said publicly, with its conditions.

## Verification

- [ ] The unit of privacy is fixed before any budget is discussed, and follows from the scenario.
- [ ] Contribution per unit is bounded, with the cap and its representativeness cost stated.
- [ ] Every release from the data is inventoried, including evaluation and prior releases.
- [ ] The reported guarantee is the composed total, not a per-run figure.
- [ ] Hyperparameter tuning is accounted, moved off sensitive data, or explicitly declared unaccounted.
- [ ] Utility is measured, not estimated, and reported per subgroup as well as overall.
- [ ] The coverage boundary names correlations, group inference, and out-of-accounting releases.
- [ ] Operational controls define who spends budget and what happens at exhaustion.
- [ ] No budget values or utility figures are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Choose the budget first and the unit afterwards — the number is uninterpretable until the unit is fixed, and record-level accounting on a person with many records protects nobody.
- Report the final training run's budget as the guarantee when a tuning sweep ran over the same sensitive data.
- Leave prior public statistics out of composition because they were released before the DP project started; the data subjects' exposure composes regardless of your project boundaries.
- Describe DP output as anonymized — it bounds individual influence on a release, which is a different and narrower claim.
- Report aggregate utility only; DP degrades small subgroups hardest, and those are frequently the subjects the privacy concern was about.
- Present a budget as strong by comparison to a number you recall from a paper.

✅ **DO:**
- Derive the unit from the disclosure scenario, then cap contributions so the guarantee has something to stand on.
- Inventory every release from the data and compose across all of them.
- Move tuning to proxy data where possible, and say so plainly where it was not accounted.
- Measure utility per subgroup and lead with the worst-affected group.
- Write the coverage boundary as prominently as the budget, including correlation between units.
- Put a named owner on budget spend, with a review before any new release.

## Example Output

```markdown
## DP Design: Patient Readmission Model + Quarterly Public Statistics

### Scenario & Unit
Bounding S2/S3 from the selection memo: a model consumer or artifact holder learning that a
named person was a patient, or reconstructing their attributes. Because a patient can have
many episodes, the unit is the **patient**, not the record. Record-level accounting here would
produce a number that protects an episode and not a person — which is not the scenario.

### Contribution Bound
Raw data is unbounded per patient (max observed: 47 episodes). **Cap at 5 episodes per
patient**, sampled to preserve the admission-type mix. Cost: high-utilization patients are
under-represented, which is exactly the cohort the model is most often used on — recorded as a
known limitation, not hidden.

### Release Inventory
| Release | Mechanism | Cadence |
|---|---|---|
| Readmission model | noisy gradient training | one-off, retrained annually |
| Quarterly public statistics | output perturbation | 4×/year, ongoing |
| Internal eval report | derived from the model only | per retrain |
| Prior 2024 public statistics | **released without DP** | historical |

The 2024 release is not something we can un-release. It composes with everything after it and
is included below rather than treated as out of scope.

### Budget Accounting
Total across all releases is the guarantee; per-release figures are its division.
| Release | Share of total | Note |
|---|---|---|
| Model training | `[choose after utility measurement]` | dominant consumer |
| Quarterly statistics | `[divide across 4 releases/year]` | recurring — the budget must last |
| Internal eval | 0 additional | derived from the released model only |
| 2024 non-DP release | **unbounded for those statistics** | accounted as a known prior exposure |

**Tuning:** hyperparameter search will run on a **synthetic proxy** built from the 2024 public
statistics, not on patient data. Had it run on the sensitive data unaccounted, the reported
guarantee would have been optimistic and we would say so here instead.

All quantities `[measure on your data]` — no budget or noise value is carried in from a paper.

### Utility Measurement
| Metric | No DP | With DP | Floor | Verdict |
|---|---|---|---|---|
| Overall AUC | `[measure]` | `[measure]` | 0.78 | — |
| Age <40 AUC | `[measure]` | `[measure]` | 0.72 | **watch — small n** |
| Rare-comorbidity AUC | `[measure]` | `[measure]` | 0.70 | **watch — smallest n** |

Subgroup rows are mandatory here: the two groups DP will hurt most are the two the model is
least accurate on already.

### Coverage Boundary
**Covered:** the influence of any one patient (up to 5 capped episodes) on the model and on the
perturbed statistics.
**Not covered:** correlations between patients — a household or a disease cluster is not a unit;
group-level inference about a ward or a condition cohort; anything already public, including the
2024 statistics; any analysis run outside the accounted pipeline; a patient appearing under two
different identifiers.

### Operational Controls
Budget owned by the clinical data governance lead. Spend tracked in the release register; no
release derived from this data ships without a register entry. At exhaustion, further releases
require either a new consent basis or a longer aggregation window — not a quiet budget increase,
which is the failure mode this control exists to prevent.

### Honest Statement
"Model training and the quarterly statistics operate under a composed patient-level differential
privacy budget, with each patient's contribution capped at 5 episodes. The guarantee bounds any
single patient's influence on these releases. It does not cover correlations between patients,
group-level inference, statistics published before 2025, or a patient recorded under more than
one identifier."
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** unit before budget before composition is a strict order, because reversing it produces an uninterpretable guarantee.
- **DS-02 (Metric Specification):** budget, contribution bound, and utility floor are defined as measured quantities with units.
- **CM-02 (Constraint Specification):** the coverage-boundary and tuning-accounting rules bound what may be claimed.
- **QA-12 (False Positives Identification):** rejects per-run budgets reported as totals and DP described as anonymization.
- **RT-05 (Evidence-Based Reasoning):** the public statement is tied to measured, composed quantities.

**Related Prompts:**
- `rai_privacy_technique_selection.md` — decides whether DP is the right instrument at all.
- `rai_federated_learning_governance.md` — the common companion when data cannot be centralized.
- `../model-security/mlsec_membership_inference_defense.md` — empirical leakage measurement alongside the formal bound.
- `../data-for-ml/mldata_synthetic_data_strategy.md` — when the release is synthetic data from a DP generator.
