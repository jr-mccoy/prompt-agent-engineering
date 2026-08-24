---
title: "Eval Result Skepticism Audit"
category: AI-ML/model-evaluation-validation
description: "When results look too good to be true, audit the EVALUATION itself — not just the data — for metric mis-specification, contamination, harness bugs, and accidental cheating."
techniques:
  - ST-02
  - RT-05
  - RT-09
  - QA-12
  - DS-06
difficulty: advanced
tags:
  - eval-bugs
  - too-good-to-be-true
  - contamination
  - metric-misspecification
  - skepticism
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
  - domain-AI-ML/model-evaluation-validation/mleval_baseline_comparison_protocol.md
  - domain-AI-ML/model-evaluation-validation/mleval_evaluation_harness_design.md
---

# Eval Result Skepticism Audit

**Objective:** When a result looks too good to be true, systematically interrogate the *evaluation pipeline itself* — the metric definition, the harness code, contamination paths, and accidental cheating — to find the bug that's inflating the number, distinguishing a genuine win from an evaluation artifact before anyone acts on it.

**When to Use:**
- A metric jumps implausibly (near-perfect on a hard task, a giant leap over a strong baseline).
- A new pipeline/refactor coincides with a sudden score improvement.
- Before promoting any surprisingly strong result, as a standing gate.

**When NOT to Use:**
- The suspect is specifically train/test/temporal leakage in the *data* (start with `mldata_data_leakage_detector.md`).
- The result is plausible and just needs a significance test (use `mleval_statistical_significance_testing.md`).

## Inputs / Context

Provide what you can:
- **The surprising result** — metric, value, the baseline/prior it beats, and why it's suspicious.
- **The evaluation code/pipeline** — how the metric is computed, how predictions and labels are joined.
- **What changed recently** — code, data version, metric definition, splits, libraries.
- **The metric definition** — averaging, operating point, label encoding, edge-case handling.
- **The eval data** — provenance and whether it could overlap with training or be derivable.

## Constraints

**Must:**
- Treat the evaluation as the prime suspect — audit metric, code, join logic, and contamination before crediting the model.
- For each candidate cause, state the *signature* it would produce and the *check* that confirms or rules it out.
- Compare the result to baselines and domain plausibility; an implausible margin is the trigger, not the proof.

**Must Not:**
- Conclude the result is genuine merely because you can't immediately find the bug — distinguish "audited and clean" from "not yet explained."
- Fabricate causes or evidence; if the eval code isn't available, list the targeted questions needed to audit it.
- Accept a fix without re-running and confirming the score moves toward a plausible range.

**Instructions:**

1. **Quantify the implausibility.** State the result against the strongest baseline and domain expectation. How big is the surprise? This frames how hard to dig.

2. **Audit the metric definition.** Check averaging (micro/macro), operating point, label/class encoding, positive-class definition, and edge-case handling. A flipped label, wrong average, or mismatched threshold can manufacture a great-looking number.

3. **Audit the harness join and indexing.** Verify predictions are aligned to the *correct* labels (no index/order misalignment, no off-by-one, no joining predictions to training labels). Confirm the eval set is the intended held-out set.

4. **Hunt accidental cheating in code.** Look for the target (or a function of it) used as a feature, evaluation on training rows, the same examples in fit and score, or the metric reading from a cached/stale file.

5. **Check contamination and overlap.** Confirm eval items aren't present in or trivially derivable from training (especially for pretrained/LLM systems); check for duplicate items spanning train and eval.

6. **Run the predicted-signature checks.** For each hypothesis, run its specific test (e.g., shuffle labels → metric should collapse to chance; if it doesn't, the harness is reading labels somewhere it shouldn't).

7. **Re-run after each fix and rank findings.** Apply the most likely fix, re-measure, and see if the score lands in a plausible range. Rank findings by impact and confidence; declare clean only after the signature checks pass.

**Output Format:**

A markdown audit:
- **Implausibility Statement** — result vs. baseline/expectation; size of surprise.
- **Suspect Table** — Suspect | Signature | Check | Status (confirmed/ruled-out/open).
- **Confirmed Eval Bugs** — mechanism + evidence + fix, ranked.
- **Signature-Test Results** — e.g., label-shuffle / index-check outcomes.
- **Post-Fix Result** — re-measured score and whether it's now plausible.
- **Residual Open Questions** — what remains unexplained (not "clean by default").
- **INSUFFICIENT EVIDENCE** — the correct closing state when every suspect was checked, none confirmed, and the result remains implausible. That is an unresolved audit, not a clean bill of health, and the distinction is the whole point of the prompt. Name the unblocking datum: the discriminating test still outstanding, or the independent re-implementation that would settle it.

## Verification

- [ ] The implausibility is quantified against the strongest baseline, not just stated.
- [ ] Metric definition, harness join/indexing, and contamination are each audited.
- [ ] A label-shuffle (or equivalent) signature test is run to detect harness label leakage.
- [ ] Each suspect has a signature and a confirming/ruling-out check, with a status.
- [ ] "Clean" is only declared after signature checks pass — not from failure to find a bug.
- [ ] Any fix is re-run and the score confirmed to land in a plausible range.
- [ ] An implausible result with no confirmed suspect closes as INSUFFICIENT EVIDENCE with the outstanding test named — never as validated by exhaustion of the suspect list.

## False-Positive Prevention

❌ **DON'T:**
- Accept a near-perfect score as a breakthrough because the team is excited and the bug isn't obvious.
- Assume the metric code is correct; a swapped positive class or micro-vs-macro slip can fake a great number.
- Stop at the data-leakage check and ignore harness bugs (index misalignment, scoring training rows).
- Call the eval "verified clean" when you simply didn't find the cause yet.

✅ **DO:**
- Anchor the audit in how implausible the margin is versus strong baselines.
- Run a label-shuffle test: a correct harness should collapse to chance — if it stays high, the eval is leaking labels.
- Audit join/indexing and the metric definition as first-class suspects, not just the data.
- Re-measure after fixes and report the plausible post-fix number; flag anything still unexplained.

## Example Output

```markdown
## Skepticism Audit: NER Model Reports F1 = 0.997

### Implausibility Statement
Prior best on this dataset ≈ 0.91; human ceiling ≈ 0.96. F1 = 0.997 exceeds the human ceiling → strong red flag.

### Suspect Table
| Suspect | Signature | Check | Status |
|---|---|---|---|
| Eval on training rows | near-perfect, collapses on true holdout | re-run on held-out only | CONFIRMED |
| Metric reads gold as pred | label-shuffle keeps F1 high | shuffle predictions, recompute | ruled out |
| Span-matching too lenient | inflated partial matches | switch to exact-span match | open |
| Train/eval overlap | duplicates across splits | dedup check on doc IDs | CONFIRMED (3% overlap) |

### Confirmed Eval Bugs (ranked)
1. **Evaluation ran on a dataframe that still included training documents** (the holdout filter was dropped
   in a refactor). Evidence: 78% of "eval" doc IDs are in the training set. Fix: restore the holdout filter.
2. **3% duplicate documents span train and eval.** Fix: dedup by document hash before splitting.

### Signature-Test Results
Label-shuffle: F1 drops to ~0.02 → harness is NOT reading gold as predictions (good). Confirms the inflation
came from train rows in the eval set, not from a metric-side label leak.

### Post-Fix Result
After restoring the holdout filter and deduping: F1 = 0.905 — back in the plausible range near prior best.

### Residual Open Questions
Confirm span-matching strictness (exact vs. partial) — minor, but verify before final reporting.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** implausibility → metric → harness → cheating → contamination → signature tests → re-run.
- **RT-05 (Evidence-Based Reasoning):** each suspect is tied to a concrete signature and check.
- **RT-09 (Root Cause Explanation):** the goal is the mechanism inflating the score, not a symptom.
- **QA-12 (False Positives Identification):** the entire prompt is built around distrusting a too-good result.
- **DS-06 (Prioritization & Severity Guidance):** confirmed bugs are ranked by impact.

**Related Prompts:**
- `mldata_data_leakage_detector.md` — when the suspect is leakage in the data rather than the harness.
- `mleval_baseline_comparison_protocol.md` — the baseline comparison that flags implausible margins.
- `mleval_evaluation_harness_design.md` — build a harness whose preconditions catch these bugs automatically.
