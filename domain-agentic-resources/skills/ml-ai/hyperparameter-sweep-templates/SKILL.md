---
name: hyperparameter-sweep-templates
description: Design hyperparameter searches that don't waste compute — Bayesian search, ASHA early stopping, multi-fidelity, and proper search space design. Use when planning a sweep, when grid search has gone out of control, or when you need to defend "we tuned this" in a paper or PR.
metadata:
  tags:
    - ml
    - hyperparameter
    - optuna
    - ray-tune
    - wandb-sweeps
  updated: "2026-05-05"
---

# Hyperparameter Sweep Templates

Grid search is dead. Random search is the floor. Anything serious uses Bayesian optimization with early stopping. This skill gives you templates for the common cases — single-model tuning, multi-fidelity, neural architecture search lite — and the rules that prevent burning a month of GPU time on a poorly-defined search.

## When to Use This Skill

- Planning a hyperparameter search for a new model
- Replacing a grid search that's gotten unmanageable
- Justifying a chosen hyperparameter configuration in a paper or design doc
- Tuning under a fixed compute budget
- Multi-objective tuning (accuracy vs. latency vs. cost)

## Core Principles

1. **Define the search space carefully.** Most "tuning" gains come from the right space, not the right algorithm.
2. **Log scale for learning rates and weight decay.** Linear scale wastes 90% of trials in irrelevant ranges.
3. **Use multi-fidelity early stopping.** ASHA/Hyperband kills bad trials fast.
4. **Tune one thing at a time when introducing new components.** Joint search of 8 dimensions with 50 trials is undersampled.
5. **Hold out a final test set.** Tuning is on validation; final reporting is on held-out test.

## Search Space Design

### Standard Optimizer Hyperparameters

| Parameter | Type | Range | Scale |
|---|---|---|---|
| learning_rate | float | 1e-5 to 1e-2 | log |
| weight_decay | float | 1e-6 to 1e-1 | log |
| batch_size | int (powers of 2) | 16 to 512 | log |
| warmup_steps | int | 0 to 10% of total | linear |
| dropout | float | 0.0 to 0.5 | linear |
| label_smoothing | float | 0.0 to 0.2 | linear |
| grad_clip_norm | float | 0.1 to 10.0 | log |

### Architecture Hyperparameters (model-specific)

| Parameter | Type | Notes |
|---|---|---|
| hidden_dim | int (powers of 2) | log scale |
| num_layers | int | small range, integer |
| num_heads | int | divisor of hidden_dim |
| ffn_multiplier | float | 2.0 to 8.0 |

## Optuna Template (Bayesian + ASHA)

```python
# sweep/optuna_sweep.py
import optuna
from optuna.pruners import HyperbandPruner
from optuna.samplers import TPESampler

def objective(trial: optuna.Trial) -> float:
    cfg = {
        "lr": trial.suggest_float("lr", 1e-5, 1e-2, log=True),
        "weight_decay": trial.suggest_float("weight_decay", 1e-6, 1e-1, log=True),
        "batch_size": trial.suggest_categorical("batch_size", [32, 64, 128, 256]),
        "dropout": trial.suggest_float("dropout", 0.0, 0.5),
        "warmup_steps": trial.suggest_int("warmup_steps", 0, 5000),
        "hidden_dim": trial.suggest_categorical("hidden_dim", [256, 512, 1024]),
        "num_layers": trial.suggest_int("num_layers", 2, 8),
    }

    trainer = build_trainer(cfg)
    for step, val_metric in trainer.fit_yielding(eval_every=1000):
        trial.report(val_metric, step)
        if trial.should_prune():
            raise optuna.TrialPruned()
    return val_metric

study = optuna.create_study(
    direction="maximize",
    sampler=TPESampler(seed=42, n_startup_trials=10),
    pruner=HyperbandPruner(min_resource=1000, max_resource=50000, reduction_factor=3),
    storage="postgresql://optuna@host/sweeps",
    study_name="ranker-v0.5-tune",
    load_if_exists=True,
)
study.optimize(objective, n_trials=200, n_jobs=8)
```

### Why these choices

- **TPESampler** with `n_startup_trials=10` — random for the first 10, Bayesian afterward
- **HyperbandPruner** — kills underperforming trials at increasing budgets
- **PostgreSQL storage** — multiple workers can pull from one study
- **load_if_exists=True** — interrupted sweeps resume cleanly
- **Seed the sampler** — reproducible ordering

## Ray Tune Template (ASHA, Distributed)

```python
from ray import tune
from ray.tune.schedulers import ASHAScheduler
from ray.tune.search.optuna import OptunaSearch

config = {
    "lr": tune.loguniform(1e-5, 1e-2),
    "weight_decay": tune.loguniform(1e-6, 1e-1),
    "batch_size": tune.choice([32, 64, 128, 256]),
    "dropout": tune.uniform(0.0, 0.5),
}

scheduler = ASHAScheduler(
    metric="val_metric",
    mode="max",
    max_t=50000,         # max training steps
    grace_period=2000,   # min steps before considering pruning
    reduction_factor=3,
)

tuner = tune.Tuner(
    train_fn,
    param_space=config,
    tune_config=tune.TuneConfig(
        num_samples=200,
        scheduler=scheduler,
        search_alg=OptunaSearch(metric="val_metric", mode="max", seed=42),
    ),
)
results = tuner.fit()
```

## W&B Sweeps Template (YAML)

```yaml
# sweep.yaml
program: train.py
method: bayes
metric:
  name: val_metric
  goal: maximize
parameters:
  lr:
    distribution: log_uniform_values
    min: 1e-5
    max: 1e-2
  weight_decay:
    distribution: log_uniform_values
    min: 1e-6
    max: 1e-1
  batch_size:
    values: [32, 64, 128, 256]
  dropout:
    distribution: uniform
    min: 0.0
    max: 0.5
early_terminate:
  type: hyperband
  min_iter: 5
  eta: 3
```

## Multi-Objective Tuning

When optimizing accuracy and latency simultaneously:

```python
def objective(trial):
    cfg = sample_config(trial)
    trainer = build_trainer(cfg)
    val_acc, p95_latency_ms = trainer.fit_and_eval()
    return val_acc, p95_latency_ms  # tuple

study = optuna.create_study(directions=["maximize", "minimize"])
# Inspect Pareto front: study.best_trials
```

Pick from the Pareto front based on deployment constraints, not a single scalar.

## Compute Budgeting

Before launching a sweep:

| Total budget | Recommended approach |
|---|---|
| < 30 trials | Random search (TPE needs warmup) |
| 30-200 trials | Bayesian (TPE/GP) + Hyperband pruning |
| 200-1000 trials | Bayesian + ASHA + multi-fidelity |
| > 1000 trials | Population-based training, BOHB, or split into nested studies |

Estimate: `total_GPU_hours = num_trials × avg_trial_steps × cost_per_step / pruning_savings`

If the estimate exceeds the team's monthly budget, narrow the search space.

## Implementation Checklist

- [ ] Search space is justified (each parameter has a reason to be there)
- [ ] Log scales for lr, weight_decay, batch_size
- [ ] Pruner/early-stopping configured (Hyperband or ASHA)
- [ ] Sampler is seeded for reproducibility
- [ ] Storage backend allows multiple workers and resumption
- [ ] Each trial uses the same eval harness as production training
- [ ] Final selection is validated on a held-out test set, not the tuning val set
- [ ] Compute budget is estimated before launch
- [ ] Sweep config is committed to the repo
- [ ] Best config is documented with sweep ID and trial number for traceability

## Anti-Patterns to Avoid

- **Grid search across 5+ dimensions** — combinatorial explosion, undersamples
- **Linear-scale learning rate range** — wastes trials in 1e-3 to 1e-2 that all behave similarly
- **Tuning on the test set** — final reported metric is now optimistic
- **No pruner** — every trial runs to completion, including obvious losers
- **Joint NAS + HP search with a small budget** — you can't disentangle the contributions
- **Ignoring the random seed in objective()** — within-trial variance gets confused with cross-trial differences
- **Reporting "best of N" without confidence intervals** — best is often noise

## Companion Skills

- `training-loop-scaffolding` — provides the `trainer.fit_yielding` interface used in objectives
- `model-evaluation-harness` — produces the metric the sweep optimizes
- `dataset-validation` — runs once before the sweep starts, not per trial

## Related Resources

- Optuna docs: https://optuna.readthedocs.io
- Ray Tune: https://docs.ray.io/en/latest/tune/
- ASHA paper: Li et al., "A System for Massively Parallel Hyperparameter Tuning" (2018)
