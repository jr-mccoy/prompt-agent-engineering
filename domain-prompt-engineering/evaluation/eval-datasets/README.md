# Evaluation — Eval Datasets

**Purpose:** Build, curate, and structure evaluation datasets — from production log mining to synthetic generation, difficulty stratification, and holdout split design.

Use these prompts to produce the raw material that regression tests, rubric evaluations, and adversarial audits run against. Good eval datasets are diverse, well-labeled, difficulty-stratified, and leakage-free.

---

## Prompt Catalog

| File | What it does |
|------|--------------|
| `dataset_case_inventory_from_logs.md` | Mine production logs into a structured test set with extraction filters, deduplication, behavior labeling, and anonymization |
| `dataset_synthetic_case_generator.md` | Generate synthetic cases using axis-based coverage grids with quality validation and mode-collapse detection |
| `dataset_difficulty_stratifier.md` | Score and stratify eval cases across difficulty axes, producing a balanced easy/medium/hard distribution |
| `dataset_holdout_split_designer.md` | Design train/dev/test splits with leakage prevention, stratification verification, and a test-set lockdown protocol |

---

## How to Use These Together

**Building an eval dataset from scratch (no logs):**
1. `dataset_synthetic_case_generator.md` — generate cases across coverage axes
2. `dataset_difficulty_stratifier.md` — score and balance difficulty distribution
3. `dataset_holdout_split_designer.md` — split into dev and locked test sets

**Building from production logs:**
1. `dataset_case_inventory_from_logs.md` — extract, deduplicate, label, anonymize
2. `dataset_difficulty_stratifier.md` — stratify by difficulty
3. `dataset_synthetic_case_generator.md` — fill coverage gaps found in the log-derived set
4. `dataset_holdout_split_designer.md` — design the split

**Diagnosing a flawed dataset:**
- Model always scores >90% → `dataset_difficulty_stratifier.md` (dataset is too easy)
- Coverage gaps → `dataset_synthetic_case_generator.md` (fill missing axis combinations)
- Test results leak into prompt development → `dataset_holdout_split_designer.md`

---

## Relationship to Other Eval Infrastructure

| What you need | Go to |
|---------------|-------|
| Score the cases once you have them | `../rubrics/` |
| Run regression tests on the cases | `../regression/` |
| Add adversarial cases to the dataset | `../adversarial/` |
| Monitor production for drift | `../correctness_production_monitoring_setup.md` |
