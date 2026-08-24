# Problem Framing & Scoping

The stage before any modelling: deciding whether this is an ML problem at all, what would count as success, and whether the data and the organization can support it. Work skipped here reappears later as a model that is technically fine and answers the wrong question.

**10 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- You have a business problem and no modelling task yet.
- Someone has proposed an ML solution and nobody has asked whether it is needed.
- A project is stuck and the symptoms do not point anywhere — start with the triage router.

**Not here:**
- The task is framed and you need a method — go to the relevant modelling subdirectory.
- The question is which AI use cases to fund across a portfolio — [`../ai-product-leadership/`](../ai-product-leadership/README.md).

## Prompts


**Start here**

| Prompt | Use it to |
|---|---|
| [`mlframe_domain_triage_router.md`](mlframe_domain_triage_router.md) | Classify what an ML situation actually is — a framing question, a data problem, a training failure, an evaluation doubt, a serving constraint, a production incident, or a governance requirement — and emit an ordered prompt sequence, so the domain is consumed by route rather than exhaustively. |
| [`mlframe_is_this_an_ml_problem.md`](mlframe_is_this_an_ml_problem.md) | Decide whether a problem genuinely warrants machine learning versus rules, heuristics, or analytics — with an honest cost/benefit and the conditions under which ML is the wrong tool. |

**Frame the task**

| Prompt | Use it to |
|---|---|
| [`mlframe_problem_to_ml_task_translator.md`](mlframe_problem_to_ml_task_translator.md) | Map a fuzzy business ask to a concrete ML task type (classification, regression, ranking, clustering, detection, forecasting, etc.) with a precise target definition and unit of analysis. |
| [`mlframe_ml_use_case_canvas.md`](mlframe_ml_use_case_canvas.md) | Compress an ML initiative onto one page: the problem, the prediction, the decision it drives, the data available, the value, the risks, and the baseline — so everyone aligns before any model is built. |
| [`mlframe_success_metric_selection.md`](mlframe_success_metric_selection.md) | Translate a business objective into a single primary model metric, a set of guardrail metrics, and a concrete decision threshold — so 'success' is unambiguous before training begins. |
| [`mlframe_baseline_first_design.md`](mlframe_baseline_first_design.md) | Design the simplest viable baseline before any model is built, and define precisely what 'beating it' must mean — so model effort is justified, not assumed. |

**Assess feasibility**

| Prompt | Use it to |
|---|---|
| [`mlframe_data_readiness_assessment.md`](mlframe_data_readiness_assessment.md) | Determine whether the available data is sufficient, representative, labeled, and legally usable to attempt the problem — before any modeling effort is committed. |
| [`mlframe_feasibility_risk_assessment.md`](mlframe_feasibility_risk_assessment.md) | Pressure-test technical feasibility and surface the risks of an ML initiative — data, modeling, deployment, and harm — before resources are committed. |
| [`mlframe_cost_of_being_wrong_analysis.md`](mlframe_cost_of_being_wrong_analysis.md) | Quantify the asymmetric costs of false negatives versus false positives and let that asymmetry drive metric choice, decision threshold, and human-in-the-loop design. |
| [`mlframe_build_buy_finetune_decision.md`](mlframe_build_buy_finetune_decision.md) | Decide between building a custom model, buying a managed API, or fine-tuning an open-source model — from a practitioner and engineering view, with a weighted decision matrix and total-cost reasoning. |

## Conventions

- **Prefix:** `mlframe_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/problem-framing-scoping`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.

## What lives elsewhere

- Whether an *agent* is warranted rather than a model or workflow → [`../agentic-ai-systems/aiagent_complexity_ladder_gate.md`](../agentic-ai-systems/aiagent_complexity_ladder_gate.md).
- Study design, causal identification, and statistical power → `domain-science/statistics/`.
- Board-level AI strategy → `domain-business-strategy/ai-strategy/`.
