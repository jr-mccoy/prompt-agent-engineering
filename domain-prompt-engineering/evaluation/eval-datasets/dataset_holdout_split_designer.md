---
title: "Holdout Split Designer"
category: prompt-engineering/evaluation/eval-datasets
description: "Design train/dev/test splits that prevent data leakage, with split ratios, stratification criteria, leakage audit, and a documented rationale for each design decision."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - holdout_split
  - train_test_split
  - data_leakage
  - eval_methodology
  - dataset_design
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/evaluation/eval-datasets/dataset_difficulty_stratifier.md
  - domain-prompt-engineering/evaluation/regression/regression_golden_set_curator.md
  - domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
---

## Objective

Design a principled train/dev/test split for an eval dataset that prevents data leakage across splits, maintains class balance per split, and is documented well enough to be reproduced. Output includes split ratios with rationale, stratification criteria, a leakage audit, and split assignment instructions.

## When to Use

- Designing an eval infrastructure for a prompt that will be iteratively improved
- When separating the dataset used for prompt development from the one used for final evaluation
- When a model or prompt change will be evaluated against held-out data that must not have influenced the design
- When multiple teams share a dataset and leakage risk is high

## Inputs

| Field | Required | Description |
|-------|----------|-------------|
| `dataset_size` | Yes | Total number of cases available |
| `use_case` | Yes | `prompt_development` / `fine_tuning` / `model_comparison` / `production_monitoring` |
| `stratification_fields` | Yes | Fields to stratify on (e.g., `behavior_label`, `difficulty_tier`, `source`) |
| `leakage_risks` | Yes | Known or suspected leakage vectors (e.g., "same user across splits", "temporal overlap") |
| `reproduction_requirement` | Yes | `random_seed` / `deterministic_by_field` / `temporal` |

## Constraints

**Must:**
- Select split ratios appropriate to `use_case` from the decision table
- Apply stratification on all fields in `stratification_fields`
- Document each known leakage vector and how it is mitigated
- Specify the split assignment method: random seed, field-based, or temporal cutoff
- Verify that class distributions in each split match the overall dataset within ±5%

**Must Not:**
- Use the test set for any decision during prompt development — document this as a hard rule
- Split at the case level when the natural unit is a session or user (group-level split required)
- Use random split when temporal leakage is a known risk (use temporal split instead)

## Instructions

**Step 1 — Use-case split ratios**

| Use case | Train | Dev | Test | Rationale |
|----------|-------|-----|------|-----------|
| `prompt_development` | 0% | 70% | 30% | No training; dev is the iteration set, test is held out |
| `fine_tuning` | 70% | 15% | 15% | Standard fine-tune split |
| `model_comparison` | 0% | 0% | 100% | No iteration; entire set used for final comparison |
| `production_monitoring` | 0% | 20% | 80% | Small dev for threshold-setting; large test for ongoing measurement |

Adjust if `dataset_size` < 100: prefer 0/30/70 (no dev) or 0/0/100 with k-fold on dev.

**Step 2 — Leakage taxonomy**

| Type | Description | Mitigation |
|------|-------------|------------|
| Temporal leakage | Test cases precede train cases in time | Temporal split: train on earlier window, test on later |
| User/session leakage | Same user's data in multiple splits | Group-level split: all cases from user assigned to one split |
| Near-duplicate leakage | Paraphrase pairs split across train/test | Deduplicate before splitting; or cluster-based split |
| Label leakage | Test labels influenced by train cases | Blind test labels until evaluation is complete |
| Benchmark contamination | Test cases appeared in model training data | Audit test cases against known public benchmarks |

For each `leakage_risk` provided, identify which type it is and state the mitigation applied.

**Step 3 — Split assignment instructions**

Choose one method and document it completely:

*Random seed (for shuffled split):*
```python
import random
random.seed(42)  # document seed
cases = sorted(all_cases, key=lambda x: x["id"])  # deterministic sort before shuffle
random.shuffle(cases)
train = cases[:int(0.7 * N)]
dev   = cases[int(0.7 * N):int(0.85 * N)]
test  = cases[int(0.85 * N):]
```

*Group-level split (when leakage unit ≠ case):*
```
1. Identify grouping field (e.g., user_id, session_id)
2. Shuffle groups (not cases) with fixed seed
3. Assign groups to splits at target ratio
4. Verify that no group spans multiple splits
```

*Temporal split:*
```
1. Sort all cases by timestamp ascending
2. Train: timestamps before cutoff_1
3. Dev: timestamps between cutoff_1 and cutoff_2
4. Test: timestamps after cutoff_2
5. Document cutoffs as ISO dates, not relative windows
```

**Step 4 — Stratification verification**

After splitting, for each `stratification_field`:

| Field value | Overall % | Train % | Dev % | Test % | Max deviation |
|-------------|-----------|---------|-------|--------|---------------|
| label_A | X% | X% | X% | X% | ≤5% ✓ |
| label_B | X% | X% | X% | X% | ≤5% ✓ |

If deviation >5% for any cell: re-run split with stratification enforced (stratified shuffle or adjustments).

**Step 5 — Test set lockdown protocol**

Document and enforce:
```
LOCKDOWN RULES:
1. Test set cases are not reviewed during prompt development
2. Test set scores are not used to make prompt changes
3. Test set is evaluated only after dev-set evaluation is complete and the prompt is locked
4. Any exception requires written justification signed by owner: [name]
5. After a test set is consumed, it moves to archive; a new test set is drawn
```

**Step 6 — Reproduction package**

Produce a reproduction card:
```
Split version: v1.0
Date: 2026-05-11
Method: [random_seed | group | temporal]
Seed / cutoff: [value]
Stratification fields: [list]
Train: N cases ([IDs or file])
Dev: N cases
Test: N cases (LOCKED)
Owner: [name]
```

## Output Format

1. **Split ratio table** — selected ratios with use-case rationale
2. **Leakage audit** — each known risk mapped to type and mitigation
3. **Split assignment instructions** — code snippet or step-by-step for the chosen method
4. **Stratification verification table** — per-field distribution across splits
5. **Test set lockdown protocol** — rules and owner
6. **Reproduction card** — version, date, method, seed/cutoff, counts

## Verification

- [ ] Split ratios match the selected `use_case` from the decision table
- [ ] Every `leakage_risk` mapped to a type and mitigation
- [ ] Stratification verification shows ≤5% deviation per field per split
- [ ] Test set lockdown protocol documented with owner name
- [ ] Reproduction card includes seed or temporal cutoff (not "random")
