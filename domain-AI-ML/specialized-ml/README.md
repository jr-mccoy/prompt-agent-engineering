# Specialized ML Verticals

Seven verticals where the modality or problem structure changes the engineering enough to need its own treatment. **50 prompts across seven subdirectories; none at this level** — this file is the routing index.

Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## Choosing a vertical

Start from what the input *is*, then from what the task does with it.

| Your data is… | And the task is… | Go to |
|---|---|---|
| Images or video | classification, detection, segmentation, OCR, or medical imagery | [`computer-vision/`](computer-vision/README.md) (10) |
| Text | classification, extraction, or topic discovery **without** an LLM | [`nlp-classical/`](nlp-classical/README.md) (6) |
| User–item interactions | recommending, ranking, or personalizing | [`recommender-systems/`](recommender-systems/README.md) (9) |
| Ordered observations over time | forecasting or temporal anomaly detection | [`time-series/`](time-series/README.md) (9) |
| A sequential decision problem | actions that change future state | [`reinforcement-learning/`](reinforcement-learning/README.md) (8) |
| A graph — entities and relationships | link prediction, node classification, fraud on a graph | [`graph-ml/`](graph-ml/README.md) (4) |
| Several types at once, or speech/audio | multimodal fusion, speech, non-speech audio, anomaly detection | [`other-modalities/`](other-modalities/README.md) (4) |

**Every vertical keeps its framing prompt in its own directory** — `cv_task_framing`, `nlp_task_framing`, `graphml_task_framing`, `rl_problem_framing`, `recsys_objective_business_alignment`, `ts_forecasting_model_selection`. If you are not sure the vertical is right, start there rather than in the domain root.

## When *not* to come here first

- **You do not yet know what you are predicting** → [`../problem-framing-scoping/`](../problem-framing-scoping/README.md), or the [triage router](../problem-framing-scoping/mlframe_domain_triage_router.md).
- **The task is building a system with a language model** — RAG, agents, generation → [`../genai-llm-engineering/`](../genai-llm-engineering/README.md) or [`../agentic-ai-systems/`](../agentic-ai-systems/README.md). `nlp-classical/` is deliberately the *non*-LLM text directory.
- **The question is generic across modalities** — metric choice, leakage, drift, deployment, governance → the lifecycle subdirectories. These verticals cover only what is genuinely modality-specific; they do not restate the lifecycle for each one.

## Boundary between the verticals

Three pairs are commonly confused, and the distinction decides which directory is correct:

| Confusion | Resolution |
|---|---|
| `nlp-classical/` vs `genai-llm-engineering/` | Volume, latency, label stability, existing labels, and explainability decide — not capability. `nlp_task_framing.md` scores all five. |
| `graph-ml/` vs `genai_graphrag_knowledge_graph_design.md` | Is the graph the *modelling target* (here) or a *retrieval structure* feeding a language model (there)? |
| `time-series/` vs `other-modalities/mlmodal_audio_ml_design.md` | Audio has its own representation and leakage failures; a non-audio sensor signal is a time series. |

## Conventions

- **Prefix per vertical:** `cv_`, `nlp_`, `recsys_`, `ts_`, `rl_`, `graphml_`, `mlmodal_` — a filename identifies its home.
- **Frontmatter:** the domain's eight fields, with `category: AI-ML/specialized-ml/<vertical>`.
- **Structure:** the five canonical H2 sections with bold-label subsections, as elsewhere in the domain.
- **Vertical-specific False-Positive Prevention:** each prompt's FPP block targets a failure mode of *that* vertical — recording-condition leakage in audio, temporal leakage in forecasting, graph-split leakage in graph ML, feedback-loop bias in recsys — rather than a generic ML caution.
- **No fabrication, framework-neutral:** as across the domain.

## What lives elsewhere

- Generative image synthesis → `domain-image-generation/`.
- Clinical validity and care pathways (as opposed to modelling on medical data) → `domain-healthcare-clinical/`.
- Causal inference and survival analysis → `domain-science/statistics/`.
- LLM-based text systems → [`../genai-llm-engineering/`](../genai-llm-engineering/README.md).
