# Paper Reproductions — Landmark ML Papers

A series of scoped, rigor-first guides for reproducing landmark ML papers as a way to *deeply* learn them. Part of the `domain-AI-ML/learning-ai-ml/` learner track (Wave 5). Each guide instantiates the general method in `../mllearn_reproduce_a_paper_plan.md` for one specific paper.

## Load-bearing convention: never assert the paper's specifics from memory

This is the highest-fabrication-risk content in the domain, so the convention is strict and non-negotiable:

- **No paper-specific numbers, hyperparameters, dataset statistics, or scores are stated in these guides.** Every such value appears as a `[extract from paper §X / Table Y]` placeholder. The learner must read them out of the actual paper.
- **"Reproduced" is defined as the paper's *relative claim*** (e.g., residual ≥ plain; Transformer ≥ attention-free baseline) at a **tolerance band over multiple seeds** — not an exact match to the reported number, which is rarely realistic on scaled-down compute.
- **A reimplemented baseline is mandatory.** The claims are relative; a number you can't recompute is not a comparison.
- **Under-specified details are catalogued as named risks** with a resolution strategy (released code, convention, small sweep) — never assumed known.
- **Each guide carries a divergence protocol** that distinguishes a bug/instability from a genuine non-reproduction.

If a guide ever tempts you to "just use the known value," stop — extract it from the paper instead.

## Recommended reading order

1. `../mllearn_paper_reading_guide.md` — read the target paper critically first; surface its ambiguities.
2. `../mllearn_reproduce_a_paper_plan.md` — the general reproduction method (scope, success criterion, divergence protocol).
3. The specific guide below for your paper.

## The series

| Guide | Paper | Modality | Compute scope note |
|---|---|---|---|
| `mllearn_reproduce_word2vec_embeddings.md` | word2vec (skip-gram/CBOW) | NLP | Lightest; trainable on a modest corpus + CPU/one GPU. |
| `mllearn_reproduce_resnet_image_classifier.md` | Deep Residual Learning (ResNet) | Computer vision | Scale to a CIFAR-scale dataset on one GPU; most learners scale down from ImageNet. |
| `mllearn_reproduce_dqn_atari.md` | Deep Q-Networks (DQN) | Reinforcement learning | Start on a simpler control env or one cheap game; full Atari suite is expensive. |
| `mllearn_reproduce_transformer_attention.md` | "Attention Is All You Need" (Transformer) | NLP / seq-to-seq | Scale to a small seq-to-seq task; full translation setup is out of reach for most. |

Rough difficulty/compute ordering: **word2vec ≤ ResNet ≤ DQN ≤ Transformer (at full scale)** — which is why every guide is explicitly scoped down and judged on the relative claim.

## Related

- `../study-tracks/mllearn_study_track_nlp_llm.md`, `../study-tracks/mllearn_study_track_computer_vision.md`, `../study-tracks/mllearn_study_track_reinforcement_learning.md` — the curricula these reproductions slot into.
- `../mllearn_paper_digest_generator.md` — structurally summarize a paper before reproducing it.
- `../mllearn_portfolio_project_designer.md` — turn a completed reproduction into a portfolio piece.
