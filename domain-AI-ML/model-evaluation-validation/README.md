# Model Evaluation & Validation

Deciding what to measure, measuring it honestly, and knowing when a result is real. The skepticism audit and the offline/online alignment prompt exist because the most common evaluation failure is not a wrong number but a right number that means something other than what the team believes.

**16 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- Choosing the metric before the modelling starts.
- A result looks too good, or offline and production disagree.
- You need a coverage guarantee, an uncertainty estimate, or an abstention rule rather than a point prediction.

**Not here:**
- The suspicion is leakage in the data — [`../data-for-ml/mldata_data_leakage_detector.md`](../data-for-ml/mldata_data_leakage_detector.md) first.
- The question is fairness across groups — [`../responsible-ai-governance/`](../responsible-ai-governance/README.md).
- The evaluation target is an LLM or an agent — [`../genai-llm-engineering/genai_llm_evaluation_design.md`](../genai-llm-engineering/genai_llm_evaluation_design.md) or [`../agentic-ai-systems/aiagent_evaluation_design.md`](../agentic-ai-systems/aiagent_evaluation_design.md).

## Prompts


**Decide what to measure**

| Prompt | Use it to |
|---|---|
| [`mleval_metric_selection_guide.md`](mleval_metric_selection_guide.md) | Choose a primary metric and guardrail metrics that align to the business objective and the real cost of each error type, instead of defaulting to accuracy. |
| [`mleval_evaluation_harness_design.md`](mleval_evaluation_harness_design.md) | Design a reusable, leak-safe evaluation harness — fixed datasets, slices, baselines, metrics, and reporting — so every model is judged the same honest way. |
| [`mleval_benchmark_design.md`](mleval_benchmark_design.md) | Design a fair, contamination-free benchmark for a task — representative data, leak-proof splits, baselines, and protocols that resist teaching-to-the-test and gaming. |
| [`mleval_baseline_comparison_protocol.md`](mleval_baseline_comparison_protocol.md) | Define the baselines every model must beat — trivial, heuristic, prior-model, and human — and a protocol for comparing honestly with intervals, so 'improvement' is never measured against nothing. |

**Test whether it is real**

| Prompt | Use it to |
|---|---|
| [`mleval_eval_result_skepticism_audit.md`](mleval_eval_result_skepticism_audit.md) | When results look too good to be true, audit the EVALUATION itself — not just the data — for metric mis-specification, contamination, harness bugs, and accidental cheating. |
| [`mleval_statistical_significance_testing.md`](mleval_statistical_significance_testing.md) | Choose and apply the right significance test (McNemar, paired t, bootstrap CIs) to decide whether one model truly beats another, with proper care for paired data and multiple comparisons. |
| [`mleval_offline_online_alignment.md`](mleval_offline_online_alignment.md) | Diagnose and close the gap between offline evaluation metrics and online/business outcomes — finding why the model that wins on the holdout fails to move the real KPI. |
| [`mleval_ab_test_design_for_models.md`](mleval_ab_test_design_for_models.md) | Design an online A/B test to compare models — randomization unit, power and duration, guardrail metrics, and handling of novelty and network effects — so the winner is real and safe. |

**Find where it fails**

| Prompt | Use it to |
|---|---|
| [`mleval_error_analysis_slicing.md`](mleval_error_analysis_slicing.md) | Systematically dissect model errors by slice and subgroup to find where it fails, how badly, and why — turning an aggregate number into an actionable failure map. |
| [`mleval_confusion_matrix_interpretation.md`](mleval_confusion_matrix_interpretation.md) | Read a confusion matrix and per-class metrics correctly — separating which errors are frequent, which are costly, and which are threshold artifacts — then decide next actions. |
| [`mleval_robustness_stress_testing.md`](mleval_robustness_stress_testing.md) | Stress-test a model against input perturbations, distribution shift, edge cases, and seed variance to find where it is fragile before production does it for you. |

**Quantify and act on uncertainty**

| Prompt | Use it to |
|---|---|
| [`mleval_calibration_assessment.md`](mleval_calibration_assessment.md) | Assess whether a model's predicted probabilities mean what they say (calibration), measure miscalibration, and decide whether and how to recalibrate before downstream use. |
| [`mleval_uncertainty_quantification_design.md`](mleval_uncertainty_quantification_design.md) | Design uncertainty estimates a downstream decision can actually use — separating aleatoric from epistemic uncertainty, choosing a method against the decision rather than the literature, and validating that the estimates are honest before anyone acts on them. |
| [`mleval_conformal_prediction_design.md`](mleval_conformal_prediction_design.md) | Design conformal prediction sets or intervals with a coverage guarantee that survives deployment — checking the exchangeability assumption the guarantee rests on, choosing a score function that produces useful set sizes, and reporting conditional coverage rather than marginal alone. |
| [`mleval_ood_detection_design.md`](mleval_ood_detection_design.md) | Design detection for inputs the model should not be trusted on — defining what counts as out-of-distribution for this deployment, evaluating against near-OOD rather than only obvious cases, and setting the threshold from the cost of an undetected input rather than from an AUROC. |
| [`mleval_selective_prediction_abstention.md`](mleval_selective_prediction_abstention.md) | Design when a model should decline to predict — deriving the abstention threshold from the cost of a wrong answer versus the cost of the fallback, sizing the deferral load against real capacity, and measuring whether the humans receiving deferrals do better than the model would have. |

## Conventions

- **Prefix:** `mleval_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/model-evaluation-validation`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.

## What lives elsewhere

- Adversarial rather than distributional robustness → [`../model-security/mlsec_adversarial_robustness_assessment.md`](../model-security/mlsec_adversarial_robustness_assessment.md).
- Continuous production comparison of candidate models → [`../production-monitoring/mlmonitor_champion_challenger_design.md`](../production-monitoring/mlmonitor_champion_challenger_design.md).
- Experimental design, power analysis, and causal identification → `domain-science/statistics/`.
