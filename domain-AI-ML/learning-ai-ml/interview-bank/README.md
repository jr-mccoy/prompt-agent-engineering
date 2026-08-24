# ML Interview Bank

Graded system-design question banks organized by problem class, plus a universal scoring rubric. Distinct from the interactive [`mllearn_ml_system_design_interview.md`](../mllearn_ml_system_design_interview.md): these are banks to work through, not a simulated interview.

**5 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- Preparing for ML system-design interviews and wanting breadth by problem class.
- Calibrating what separates a junior answer from a staff one.
- Interviewing others and needing a consistent bar.

**Not here:**
- You want a live simulated interview — [`../mllearn_ml_system_design_interview.md`](../mllearn_ml_system_design_interview.md).
- You want general ML interview preparation — [`../mllearn_ml_interview_prep.md`](../mllearn_ml_interview_prep.md).

## Prompts

| Prompt | Use it to |
|---|---|
| [`mllearn_interview_bank_recommendation_ranking.md`](mllearn_interview_bank_recommendation_ranking.md) | A bank of recommendation and ranking ML-system-design interview questions, each paired with a junior→staff leveled rubric covering candidate generation, ranking, cold start, feedback-loop bias, and online/offline evaluation. |
| [`mllearn_interview_bank_search_systems.md`](mllearn_interview_bank_search_systems.md) | A bank of search and retrieval ML-system-design interview questions, each paired with a junior→staff leveled rubric covering query understanding, retrieval vs ranking, relevance evaluation, latency budgets, and lexical/embedding hybrids. |
| [`mllearn_interview_bank_nlp_llm_applications.md`](mllearn_interview_bank_nlp_llm_applications.md) | A bank of NLP/LLM-application ML-system-design interview questions, each paired with a junior→staff leveled rubric covering RAG-vs-fine-tune decisions, LLM evaluation and guardrails, hallucination control, latency/cost, and online quality monitoring. |
| [`mllearn_interview_bank_realtime_fraud_detection.md`](mllearn_interview_bank_realtime_fraud_detection.md) | A bank of real-time/streaming and fraud-detection ML-system-design interview questions, each paired with a junior→staff leveled rubric covering latency, train/serve skew, label delay, class imbalance, adversarial drift, and human-review loops. |
| [`mllearn_interview_scoring_rubric.md`](mllearn_interview_scoring_rubric.md) | A reusable, dimension-by-dimension scoring rubric for ML system-design interview answers — requirements, data, modeling, evaluation, serving, monitoring, tradeoff articulation, and scale — with explicit junior/mid/senior/staff bars, usable to grade answers from any topical question bank. |

## Conventions

- **Prefix:** `mllearn_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/learning-ai-ml/interview-bank`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.
- **Rubrics bake in the ML failure-mode catalog.** Leakage, train/serve skew, baseline-first, drift-with-a-baseline, label delay, imbalance metrics, and Goodhart appear as the senior and staff discriminators — the things that separate a fluent answer from a correct one.
- **No invented questions from named companies, and no invented scores.** These are constructed banks, not leaked material.

## What lives elsewhere

- The practitioner prompts behind the answers → the lifecycle subdirectories of [`domain-AI-ML/`](../../README.md).
- Non-ML interview and career preparation → `domain-personal-development/prompts/career/`.
