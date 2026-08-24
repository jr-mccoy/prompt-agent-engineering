# Notebook → Production

A sequenced four-step arc, each step linking its neighbours: refactor a notebook into a tested package, make training reproducible, package and serve with train/serve parity, then deploy with monitoring, CI/CD, and a tested rollback. Train/serve skew gets a dedicated callout in the serving and deploy steps because it is where this journey most often fails.

**4 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- You have a working notebook and no path to production.
- Learning the engineering half of ML rather than the modelling half.
- Onboarding someone who models well and ships rarely.

**Not here:**
- You are building an organization's ML platform rather than learning the path — [`../../mlops-infrastructure/`](../../mlops-infrastructure/README.md).
- The model is not yet good enough to ship — that is a modelling problem first.

## Prompts

| Prompt | Use it to |
|---|---|
| [`mllearn_n2p_01_refactor_notebook_to_package.md`](mllearn_n2p_01_refactor_notebook_to_package.md) | Step 1 of the notebook-to-production arc — guide a learner to refactor a working notebook into a tested, importable Python package, separating config/data/model/eval, removing hidden state and out-of-order-cell bugs, and adding tests. |
| [`mllearn_n2p_02_reproducible_training_pipeline.md`](mllearn_n2p_02_reproducible_training_pipeline.md) | Step 2 of the notebook-to-production arc — turn the refactored package into a reproducible training pipeline with a pinned environment, seeds, data versioning, deterministic splits, and experiment tracking, so a run is re-runnable and comparable. |
| [`mllearn_n2p_03_package_and_serve_model.md`](mllearn_n2p_03_package_and_serve_model.md) | Step 3 of the notebook-to-production arc — package the trained model and serve it behind an API/container with input validation, a versioned artifact, train/serve parity, latency/throughput basics, and a smoke test. |
| [`mllearn_n2p_04_deploy_monitor_cicd.md`](mllearn_n2p_04_deploy_monitor_cicd.md) | Step 4 (final) of the notebook-to-production arc — deploy the served model with monitoring (drift, performance, data quality) and a CI/CD path (automated tests, build, rollout/rollback), closing the loop from notebook to a maintainable production service. |

## Conventions

- **Prefix:** `mllearn_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/learning-ai-ml/notebook-to-production`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.
- **Run them in order.** Each step assumes the previous one's output; step 3 in particular depends on the reproducible pipeline from step 2.
- **Train/serve parity is the through-line** — the arc is designed around the failure where a model works in a notebook and behaves differently in production.

## What lives elsewhere

- Production-grade versions of each step → [`../../mlops-infrastructure/`](../../mlops-infrastructure/README.md) and [`../../production-monitoring/`](../../production-monitoring/README.md).
- Software engineering practice generally → `domain-software-engineering/`.
