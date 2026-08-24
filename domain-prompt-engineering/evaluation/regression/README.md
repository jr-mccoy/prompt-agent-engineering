# Evaluation — Regression

**Purpose:** Test infrastructure for detecting regressions when a prompt changes — golden sets, canary runners, change impact estimation, and A/B experiment design.

Use these prompts to build the infrastructure that tells you whether a prompt change broke something, and how to measure whether it improved something.

---

## Prompt Catalog

| File | What it does |
|------|--------------|
| `regression_golden_set_curator.md` | Build and maintain a versioned golden test set with provenance, freeze protocol, and update criteria |
| `regression_change_impact_estimator.md` | Predict which test cases a specific prompt diff is likely to affect before running them, to prioritize execution order |
| `regression_ab_test_runner_prompt.md` | Design a rigorous A/B experiment over two prompt variants with hypothesis, sample size, blinding, rubric, and pre-committed decision rule |
| `regression_canary_set_designer.md` | Design a 5–15-case canary set that runs in <60 seconds and catches major regressions before the full suite |

---

## How to Use These Together

**Setting up regression infrastructure from scratch:**
1. `regression_golden_set_curator.md` — build the stable reference set
2. `regression_canary_set_designer.md` — extract a fast-running subset for CI gates
3. `regression_change_impact_estimator.md` — use before each change to prioritize run order

**Evaluating a specific prompt change:**
1. `regression_change_impact_estimator.md` — predict affected cases
2. `regression_canary_set_designer.md` — run canary first for fast signal
3. `regression_ab_test_runner_prompt.md` — formal measurement if change is significant

**After a regression incident:**
1. `regression_golden_set_curator.md` — add the failure case as a new frozen anchor
2. `regression_canary_set_designer.md` — check whether canary covers the failure; add if not

---

## Related Folders

- `../adversarial/` — adversarial test cases for security/robustness evaluation
- `../rubrics/` — scoring rubrics used to evaluate pass/fail in A/B tests
- `../eval-datasets/` — dataset construction upstream of regression set curation
