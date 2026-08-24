# Classical NLP (non-LLM)

Text analysis without a language model — classification, extraction, tokenization, topic modelling, and preprocessing. This directory exists because high-volume, low-latency, stable-label text tasks are frequently served better and far more cheaply by a trained classifier than by an LLM.

**6 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- A text task with high volume, tight latency, stable labels, or an explainability requirement.
- Labelled data already exists and the categories rarely change.
- Start with task framing; it makes the LLM-versus-trained-model decision explicit rather than assumed.

**Not here:**
- The task is generative, conversational, or open-ended — [`../../genai-llm-engineering/`](../../genai-llm-engineering/README.md).
- The label set changes constantly and no labelled data exists — an LLM is likely the right instrument.

## Prompts

| Prompt | Use it to |
|---|---|
| [`nlp_task_framing.md`](nlp_task_framing.md) | Frame a text task before choosing a method — deciding what the unit of prediction is, whether the label set is closed, and whether an LLM or a trained classical model is the right instrument for this volume, latency, and stability profile. |
| [`nlp_text_classification_design.md`](nlp_text_classification_design.md) | Design a non-LLM text classification pipeline — representation, model, evaluation, and class-imbalance handling — with leakage-safe preprocessing and metrics that survive imbalanced, multi-label, or skewed-cost settings. |
| [`nlp_ner_extraction_design.md`](nlp_ner_extraction_design.md) | Design a named-entity / span extraction system — entity schema, annotation and tagging scheme (BIO/BILOU), boundary rules, and span-level evaluation that does not mistake token accuracy for extraction quality. |
| [`nlp_topic_modeling_approach.md`](nlp_topic_modeling_approach.md) | Approach unsupervised text structure discovery — LDA vs embeddings+clustering — and validate it with coherence, stability, and human interpretability rather than trusting auto-discovered topics at face value. |
| [`nlp_tokenization_representation_strategy.md`](nlp_tokenization_representation_strategy.md) | Choose a tokenization scheme and text representation — bag-of-words, TF-IDF, word, or subword embeddings — matched to the task, language, vocabulary behavior, and out-of-vocabulary risk, with a leakage-safe fitting boundary. |
| [`nlp_text_preprocessing_pipeline.md`](nlp_text_preprocessing_pipeline.md) | Design a text preprocessing pipeline — normalization, language handling, noise removal — that is reproducible, identical offline and at serving, and free of the silent leakage and information-destruction that quietly degrade NLP models. |

## Conventions

- **Prefix:** `nlp_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/specialized-ml/nlp-classical`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.

## What lives elsewhere

- LLM-based extraction and classification at scale → [`../../genai-llm-engineering/genai_structured_extraction_at_scale.md`](../../genai-llm-engineering/genai_structured_extraction_at_scale.md).
- Multilingual system design → [`../../genai-llm-engineering/genai_multilingual_design.md`](../../genai-llm-engineering/genai_multilingual_design.md).
