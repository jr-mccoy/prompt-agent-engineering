---
title: "Notebook → Production 1: Refactor a Notebook into a Package"
category: AI-ML/learning-ai-ml/notebook-to-production
description: "Step 1 of the notebook-to-production arc — guide a learner to refactor a working notebook into a tested, importable Python package, separating config/data/model/eval, removing hidden state and out-of-order-cell bugs, and adding tests."
techniques:
  - ST-02
  - ED-01
  - CM-02
  - QA-01
  - RP-01
difficulty: intermediate
tags:
  - notebook-to-production
  - refactoring
  - packaging
  - testing
  - reproducibility
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/learning-ai-ml/mllearn_portfolio_project_designer.md
  - domain-AI-ML/learning-ai-ml/notebook-to-production/mllearn_n2p_02_reproducible_training_pipeline.md
  - domain-AI-ML/mlops-infrastructure/mlops_reproducibility_audit.md
---

# Notebook → Production 1: Refactor a Notebook into a Package

**Objective:** Guide a learner through the first step of taking an ML project to production — turning a working-but-fragile notebook into a tested, importable Python package with clear module boundaries (config, data, model, evaluation) — so the project becomes reproducible, testable, and ready for a real training pipeline, eliminating the hidden-state and out-of-order-execution bugs that make notebooks untrustworthy.

**When to Use:**
- A learner has a model working in a notebook and wants to make it production-grade.
- First step before building a training pipeline, serving, or CI/CD (the rest of this arc).
- A notebook "works" but can't be re-run top-to-bottom or reused outside the notebook.

**When NOT to Use:**
- There's no working notebook yet — build and validate the model first.
- The learner needs a project designed, not refactored (use `mllearn_portfolio_project_designer.md`).
- The notebook is genuinely exploratory and not headed to production (keep it a notebook).

## Inputs / Context

- **The notebook** — the working notebook (or its structure: cells, what each does).
- **The model/task** — what it does, its inputs and outputs.
- **Target use** — what the package must support next (a training pipeline, then serving).
- **Learner level** — software-engineering comfort (testing, modules, packaging).

## Constraints

**Must:**
- Separate concerns into modules — configuration, data loading/processing, model definition/training, and evaluation — with no business logic trapped in notebook cells.
- Eliminate hidden state and execution-order dependence: the package must produce the same result run start-to-finish, every time, from a clean state.
- Add tests that lock current behavior before and after refactoring (at minimum: data-shape/contract tests and a training/eval smoke test).

**Must Not:**
- Change model behavior while refactoring — refactor and behavior-change are separate steps; verify parity with the notebook's results first.
- Leave hard-coded paths, magic constants, or notebook-only globals in the package.
- Call it done without a way to run the whole thing from the command line / an entry point.

**Instructions:**

1. **Inventory the notebook.** List what each cell/section does and classify it: config, data, model, training, evaluation, or throwaway exploration (which does not move to the package).

2. **Capture current behavior as a baseline.** Record the notebook's key outputs (metrics, shapes) so you can verify the refactor preserves them — refactoring must not silently change results.

3. **Design the module layout.** Propose a minimal package structure (e.g., `config`, `data`, `model`, `train`, `evaluate`, plus an entry point) and where each notebook piece moves.

4. **Extract config first.** Pull paths, hyperparameters, and constants into a single config (file or object) — no magic numbers scattered through code.

5. **Move logic into functions/modules with tests.** Refactor each concern into importable functions; add tests as you go (data contracts, a smoke test that trains a tiny run and evaluates).

6. **Add an entry point.** Provide a CLI/`main` that runs train→evaluate end-to-end from a clean state, driven by config.

7. **Verify parity and clean state.** Confirm the package reproduces the notebook's baseline outputs and runs identically from a fresh interpreter — no hidden state, no cell-order dependence.

**Output Format:**

A markdown refactor guide:
- **Notebook Inventory** — cell/section → concern classification.
- **Behavior Baseline** — the outputs the refactor must preserve.
- **Module Layout** — the proposed package structure + what moves where.
- **Refactor Steps** — config → modules → tests → entry point.
- **Test Plan** — the data-contract and smoke tests added.
- **Parity & Clean-State Check** — how parity with the notebook was verified.

## Verification

- [ ] Logic is split into config/data/model/train/evaluate modules; no logic stuck in cells.
- [ ] The package runs end-to-end from a clean state with no execution-order dependence.
- [ ] Behavior parity with the notebook baseline is verified (no silent result change).
- [ ] Tests exist (data contracts + a training/eval smoke test).
- [ ] An entry point runs the pipeline from config; no hard-coded paths or magic constants.

## False-Positive Prevention

❌ **DON'T:**
- "Refactor" and change model behavior in the same pass, then not notice the metric moved.
- Leave notebook globals, hard-coded paths, or magic numbers in the package.
- Declare success without running it from a fresh interpreter top to bottom.
- Skip tests because "it worked in the notebook."

✅ **DO:**
- Capture the notebook's outputs first and verify parity after refactoring.
- Centralize config; remove hidden state and cell-order dependence.
- Add data-contract and smoke tests as you extract each module.
- Provide a clean-state entry point and confirm it reproduces the baseline.

## Example Output

```markdown
## Notebook → Package — tabular classifier

### Notebook Inventory
Cells 1–3 data load/clean → data. Cell 4 EDA plots → throwaway. Cells 5–7 features → data.
Cells 8–10 train → model/train. Cell 11 metrics → evaluate.

### Behavior Baseline
Test macro-F1 0.81; feature matrix shape (N, 42); 3-fold CV mean recorded.

### Module Layout
pkg/{config.py, data.py, model.py, train.py, evaluate.py}, entry point `python -m pkg.train`.

### Refactor Steps
Config: paths, seed, hyperparams → config.py. Data/feature logic → data.py (drop EDA). Training →
train.py; eval → evaluate.py.

### Test Plan
test_data_contract (column set + dtypes + no NaN leakage), test_smoke (tiny train run produces a
model + a finite metric).

### Parity & Clean-State Check
`python -m pkg.train` from a fresh venv reproduces macro-F1 0.81 ± seed noise; runs identically twice.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** inventory → baseline → layout → refactor → verify.
- **ED-01 (Iterative Scaffolding):** refactor concern-by-concern, adding tests as you go.
- **CM-02 (Constraint Specification):** clean-state reproducibility and behavior parity as hard constraints.
- **QA-01 (Self-Verification):** parity and clean-state checks verify the refactor preserved behavior.
- **RP-01 (Audience/Level Adaptation):** depth tuned to the learner's software-engineering comfort.

**Related Prompts:**
- `mllearn_portfolio_project_designer.md` — the project this arc productionizes.
- `notebook-to-production/mllearn_n2p_02_reproducible_training_pipeline.md` — next step: a reproducible training pipeline.
- `mlops_reproducibility_audit.md` — deeper reference on reproducibility practices.
