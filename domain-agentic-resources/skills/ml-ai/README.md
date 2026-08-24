# ML/AI Skills

Reusable knowledge bundles for ML engineering workflows — evaluation, training, data validation, and tuning. Designed to be invoked by ML/AI agents in `agents/ml-ai/` (data-engineer, ai-engineer, mlops-engineer, prompt-engineer, etc.).

## Skills

| Skill | Use For |
|-------|---------|
| [`model-evaluation-harness`](model-evaluation-harness/SKILL.md) | Frozen test sets, slice metrics, regression gates, CI integration |
| [`training-loop-scaffolding`](training-loop-scaffolding/SKILL.md) | Production training loops with checkpointing, mixed precision, resumability |
| [`dataset-validation`](dataset-validation/SKILL.md) | Schema, distribution, leakage, label quality, drift detection |
| [`hyperparameter-sweep-templates`](hyperparameter-sweep-templates/SKILL.md) | Bayesian search, ASHA pruning, multi-objective tuning with Optuna/Ray Tune/W&B |

## Typical Pipeline

```
dataset-validation → training-loop-scaffolding → model-evaluation-harness → hyperparameter-sweep-templates
       │                       │                          │                            │
       ↓                       ↓                          ↓                            ↓
   Block training          Single trial              Compare to baseline        Search across configs
   on bad data             reproducibility           Block regression            using above 3 skills
```

Each skill is independently usable; together they form a reproducible ML pipeline.

## Companion Skills

- `skills/llm-application-dev/` — for LLM-specific workflows (RAG, fine-tuning, prompt eval)
- `skills/data-engineering/` — for upstream data pipelines feeding training

## Companion Agents

- `agents/ml-ai/data-engineer.md`
- `agents/ml-ai/ai-engineer.md`
- `agents/ml-ai/mlops-engineer.md`
