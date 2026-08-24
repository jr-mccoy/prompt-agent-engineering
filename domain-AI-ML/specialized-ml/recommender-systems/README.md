# Recommender Systems

Architecture, candidate generation and ranking, cold start, offline evaluation, and the two problems that define the field in production: multi-objective tradeoffs and the feedback loop a recommender creates in its own training data.

**9 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- Designing or debugging a recommendation or ranking system.
- Offline metrics improve and online engagement does not.
- The system is narrowing — recommending less and less variety over time.

**Not here:**
- The ranking problem is document retrieval for a RAG system — [`../../genai-llm-engineering/genai_reranking_strategy.md`](../../genai-llm-engineering/genai_reranking_strategy.md).
- The concern is the production feedback loop generally → [`../../production-monitoring/mlmonitor_feedback_loop_detection.md`](../../production-monitoring/mlmonitor_feedback_loop_detection.md).

## Prompts

| Prompt | Use it to |
|---|---|
| [`recsys_objective_business_alignment.md`](recsys_objective_business_alignment.md) | Align a recommender's training objective with the actual business objective — exposing proxy-metric risk where optimizing the trainable label (clicks, watch-time) quietly degrades the goal it's supposed to serve (retention, revenue, satisfaction). |
| [`recsys_architecture_design.md`](recsys_architecture_design.md) | Design an end-to-end recommender (retrieval + ranking, content/collaborative/hybrid) matched to the use case, data, scale, and latency budget. |
| [`recsys_candidate_ranking_design.md`](recsys_candidate_ranking_design.md) | Design the two-stage retrieval (candidate generation) + ranking pipeline for a recommender — the recall mechanisms, the ranking features and objective, and the handoff between stages — sized to catalog scale and latency. |
| [`recsys_cold_start_strategy.md`](recsys_cold_start_strategy.md) | Design strategies for user, item, and system cold start using content features, popularity priors, onboarding, and exploration — without starving discovery or overfitting to early signal. |
| [`recsys_sequential_session_based_design.md`](recsys_sequential_session_based_design.md) | Model user behavior as an ordered sequence — choose between session-based RNN/transformer/next-item architectures, define session boundaries, balance short- vs long-term intent, handle cold sessions, and design leak-free temporal evaluation. |
| [`recsys_multi_objective_ranking.md`](recsys_multi_objective_ranking.md) | Balance relevance against diversity, revenue, freshness, and fairness in a single ranker — choose between scalarization (weighted sum), constrained optimization, and Pareto methods, select and validate objective weights, and install guardrail metrics that catch silent degradation. |
| [`recsys_bandits_exploration.md`](recsys_bandits_exploration.md) | Decide when and how to use bandits for recommendation — epsilon-greedy / UCB / Thompson sampling, contextual vs non-contextual, off-policy evaluation (IPS / doubly-robust), exploration budget and safety guardrails, and propensity logging that makes future evaluation possible. |
| [`recsys_offline_evaluation.md`](recsys_offline_evaluation.md) | Evaluate a recommender offline with appropriate ranking metrics and beyond-accuracy measures, and reason rigorously about why offline gains may not translate to online lift due to logged-data bias. |
| [`recsys_feedback_loop_bias_audit.md`](recsys_feedback_loop_bias_audit.md) | Audit a recommender for popularity bias, position bias, and self-reinforcing feedback loops — where the system trains on data it generated, entrenching the head and starving discovery — with evidence-backed findings and mitigations. |

## Conventions

- **Prefix:** `recsys_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/specialized-ml/recommender-systems`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.

## What lives elsewhere

- Online learning from engagement feedback → [`../../mlops-infrastructure/mlops_online_learning_pipeline_design.md`](../../mlops-infrastructure/mlops_online_learning_pipeline_design.md).
- Graph-structured recommendation → [`../graph-ml/`](../graph-ml/README.md).
