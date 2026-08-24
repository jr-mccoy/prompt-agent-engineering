---
name: training-loop-scaffolding
description: Scaffold a production-grade PyTorch or JAX training loop with checkpointing, mixed precision, gradient accumulation, deterministic seeding, structured logging, and resumability. Use when starting a new model project or replacing a notebook-grown training script with something CI can run.
metadata:
  tags:
    - ml
    - training
    - pytorch
    - jax
    - mlops
    - checkpointing
  updated: "2026-05-05"
---

# Training Loop Scaffolding

Most training loops grow out of a notebook and never recover. They lose checkpoints, can't resume, leak GPU memory, and produce one-off results. This skill gives you a scaffold that survives interrupted training, hardware changes, and team handoffs.

## When to Use This Skill

- Starting a new training project
- Replacing a notebook-based training script with something runnable from CI
- A training run crashed at hour 14 and there's no checkpoint
- Multiple engineers need to reproduce a run from a config alone
- You're moving from single-GPU to multi-GPU or accelerator-agnostic code

## Core Principles

1. **Config in, artifacts out.** A training run is fully described by its config file plus the data version.
2. **Resume from any checkpoint.** Crashes, preemptions, and OOMs happen — loss of work shouldn't.
3. **Determinism within a seed.** Same config + same seed + same data = same result.
4. **Logging is structured, not printed.** Metrics, gradients, and hyperparameters go to a tracker.
5. **The scaffold is framework-agnostic in shape.** PyTorch and JAX differ in implementation, not in structure.

## Standard Loop Structure

```
project/
├── configs/
│   └── base.yaml              # Hydra/OmegaConf config
├── train.py                   # Entry point — parses config, launches
├── trainer/
│   ├── __init__.py
│   ├── trainer.py             # Trainer class (loop, optim, sched)
│   ├── checkpoint.py          # Save/load atomic checkpoints
│   ├── data.py                # Dataset, sampler, collate
│   ├── callbacks.py           # EvalCallback, EarlyStopping, LRMonitor
│   └── distributed.py         # DDP/FSDP/multi-host helpers
├── models/
│   └── my_model.py
└── eval/                      # See: model-evaluation-harness skill
```

## Config Schema (Hydra/OmegaConf)

```yaml
# configs/base.yaml
seed: 42
project: ranker
run_name: ${now:%Y-%m-%d_%H-%M-%S}_${model.name}

data:
  train_path: s3://datasets/ranker/train_v3.parquet
  val_path: s3://datasets/ranker/val_v3.parquet
  batch_size: 256
  num_workers: 8

model:
  name: ranker-mlp-v2
  hidden_dim: 512
  dropout: 0.1

optim:
  name: adamw
  lr: 1.0e-3
  weight_decay: 1.0e-2
  betas: [0.9, 0.95]

schedule:
  name: cosine_warmup
  warmup_steps: 1000
  total_steps: 50000

train:
  max_steps: 50000
  eval_every: 1000
  ckpt_every: 5000
  log_every: 100
  grad_accum_steps: 4
  mixed_precision: bf16
  gradient_clip_norm: 1.0
  resume_from: null  # path to checkpoint or null

logging:
  backend: wandb  # or mlflow, tensorboard
  watch_grads: true
  watch_params: false  # expensive
```

## Trainer Skeleton (PyTorch)

```python
# trainer/trainer.py
class Trainer:
    def __init__(self, model, optim, sched, train_loader, val_loader, cfg):
        self.model = model
        self.optim = optim
        self.sched = sched
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.cfg = cfg
        self.scaler = torch.amp.GradScaler() if cfg.train.mixed_precision == "fp16" else None
        self.step = 0
        self.epoch = 0
        self.best_metric = -float("inf")

    def fit(self):
        if self.cfg.train.resume_from:
            self.load_checkpoint(self.cfg.train.resume_from)

        self.model.train()
        accum_count = 0

        while self.step < self.cfg.train.max_steps:
            for batch in self.train_loader:
                with torch.amp.autocast(dtype=self._amp_dtype()):
                    loss = self.model(batch) / self.cfg.train.grad_accum_steps

                if self.scaler:
                    self.scaler.scale(loss).backward()
                else:
                    loss.backward()

                accum_count += 1
                if accum_count == self.cfg.train.grad_accum_steps:
                    self._optimizer_step()
                    accum_count = 0
                    self.step += 1

                    if self.step % self.cfg.train.log_every == 0:
                        self._log_train_metrics(loss)
                    if self.step % self.cfg.train.eval_every == 0:
                        self._run_eval()
                    if self.step % self.cfg.train.ckpt_every == 0:
                        self.save_checkpoint(f"step_{self.step}")
                    if self.step >= self.cfg.train.max_steps:
                        break
            self.epoch += 1

        self.save_checkpoint("final")

    def _optimizer_step(self):
        if self.scaler:
            self.scaler.unscale_(self.optim)
        if self.cfg.train.gradient_clip_norm:
            torch.nn.utils.clip_grad_norm_(
                self.model.parameters(),
                self.cfg.train.gradient_clip_norm,
            )
        if self.scaler:
            self.scaler.step(self.optim)
            self.scaler.update()
        else:
            self.optim.step()
        self.sched.step()
        self.optim.zero_grad(set_to_none=True)
```

## Checkpoint Format

```python
# trainer/checkpoint.py — atomic save, full resumability
def save_checkpoint(trainer, name):
    payload = {
        "step": trainer.step,
        "epoch": trainer.epoch,
        "best_metric": trainer.best_metric,
        "model_state": trainer.model.state_dict(),
        "optim_state": trainer.optim.state_dict(),
        "sched_state": trainer.sched.state_dict(),
        "scaler_state": trainer.scaler.state_dict() if trainer.scaler else None,
        "rng_state": {
            "torch": torch.get_rng_state(),
            "torch_cuda": torch.cuda.get_rng_state_all(),
            "numpy": np.random.get_state(),
            "python": random.getstate(),
        },
        "config": OmegaConf.to_container(trainer.cfg, resolve=True),
        "git_sha": git_sha(),
    }
    tmp = f"{path}.tmp"
    torch.save(payload, tmp)
    os.replace(tmp, path)  # atomic
```

A checkpoint that doesn't restore the optimizer state, scheduler state, scaler state, and RNG state is not a checkpoint. It's a model snapshot.

## Determinism Setup

```python
def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    # Set environment for fully deterministic CUBLAS
    os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
    torch.use_deterministic_algorithms(True, warn_only=True)
```

Document tradeoffs: full determinism may cost 10-30% throughput. For large-scale training, fix seeds + document non-determinism rather than enforce it.

## Distributed Training

- **DDP** for model fits in a single GPU's memory, scale by data parallelism
- **FSDP** for large models with sharded parameters and optimizer states
- **DeepSpeed/Megatron** for trillion-parameter scale
- Make the trainer accept a `is_main_process` flag — only rank 0 logs and checkpoints
- Wrap model after `.to(device)`, before optimizer construction

## Implementation Checklist

- [ ] Single config file fully describes the run
- [ ] All randomness is seeded
- [ ] Checkpoints save model + optim + sched + scaler + RNG state + config
- [ ] Checkpoint save is atomic (write to tmp, rename)
- [ ] Resume from any checkpoint produces identical continuation (test this)
- [ ] Mixed precision is configurable (fp32, bf16, fp16)
- [ ] Gradient accumulation is supported
- [ ] Gradient clipping is configurable
- [ ] Eval runs at fixed intervals and uses the eval harness
- [ ] Metrics go to a structured tracker (W&B, MLflow, TensorBoard)
- [ ] Distributed training works on N=1 and N>1 with the same code path
- [ ] OOM, preemption, and crash all leave a recoverable checkpoint

## Anti-Patterns to Avoid

- **Saving only the model weights** — you can't resume optimization
- **Non-atomic checkpoint writes** — a crash mid-save corrupts everything
- **Hardcoded hyperparameters** — config-driven runs are reproducible; hardcoded ones aren't
- **Logging with print()** — unstructured, not searchable, not aggregable
- **Determinism flags but unseeded data shuffling** — partial determinism is worse than none
- **CudaOutOfMemory caught and ignored** — the training is now in a bad state; crash and resume cleanly
- **Per-script training loops** — every project re-invents the trainer; extract it once

## Companion Skills

- `model-evaluation-harness` — run during eval callbacks
- `dataset-validation` — fail fast on bad inputs before wasting GPU hours
- `hyperparameter-sweep-templates` — fan out trainer runs across a search space

## Related Resources

- PyTorch: torch.distributed, torch.amp, torch.compile docs
- Hydra: https://hydra.cc/
- W&B: https://docs.wandb.ai/guides/track
