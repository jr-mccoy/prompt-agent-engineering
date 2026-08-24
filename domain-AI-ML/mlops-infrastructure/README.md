# MLOps & Infrastructure

The machinery around a model: tracking, registry, CI/CD, orchestration, serving, reproducibility, capacity, and cost. Platform-neutral by default, with named-stack playbooks for teams that have already chosen a tool.

**22 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- Standing up or hardening the pipeline that trains, packages, and serves models.
- Nobody can reproduce a run.
- Accelerator capacity or ML spend needs a defensible number.

**Not here:**
- The question is what to monitor once it is live — [`../production-monitoring/`](../production-monitoring/README.md).
- The concern is making the model itself smaller or faster — [`../model-optimization-efficiency/`](../model-optimization-efficiency/README.md).
- The question is general container, infra, or DevOps practice → `domain-software-engineering/devops/`.

## Prompts


**Track and register**

| Prompt | Use it to |
|---|---|
| [`mlops_experiment_tracking_setup.md`](mlops_experiment_tracking_setup.md) | Design an experiment-tracking system (params, metrics, artifacts, lineage) and the logging discipline that makes every run reproducible and comparable. |
| [`mlops_model_registry_design.md`](mlops_model_registry_design.md) | Design a model registry with lifecycle stages, approval gates, required metadata, and promotion criteria so only governed, traceable models reach production. |
| [`mlops_model_packaging_strategy.md`](mlops_model_packaging_strategy.md) | Package a trained model for deployment — containerization, pinned dependencies, and an explicit input/output contract — so the artifact runs identically wherever it is served. |

**Build the pipeline**

| Prompt | Use it to |
|---|---|
| [`mlops_ml_cicd_pipeline_design.md`](mlops_ml_cicd_pipeline_design.md) | Design CI/CD for ML — code, data, and model tests, training-pipeline triggers, and deployment gates — so changes ship automatically only when quality is proven. |
| [`mlops_training_pipeline_orchestration.md`](mlops_training_pipeline_orchestration.md) | Orchestrate a multi-step training pipeline as a DAG with idempotent steps, retries, and caching so runs are reliable, resumable, and reproducible. |
| [`mlops_feature_pipeline_design.md`](mlops_feature_pipeline_design.md) | Design offline and online feature pipelines that share definitions and timing so the same feature is computed identically for training and serving — eliminating train/serve skew. |
| [`mlops_online_learning_pipeline_design.md`](mlops_online_learning_pipeline_design.md) | Design continuous model updating from streaming feedback — establishing that label latency permits it, guarding the feedback loop that lets a model teach itself its own errors, and building the rollback path that a continuously updating model needs most. |

**Serve**

| Prompt | Use it to |
|---|---|
| [`mlops_model_serving_architecture.md`](mlops_model_serving_architecture.md) | Choose and design a model serving pattern — online/batch/streaming, real-time vs async — driven by latency, throughput, freshness, and cost requirements, not defaults. |
| [`mlops_batch_vs_streaming_inference.md`](mlops_batch_vs_streaming_inference.md) | Choose between batch, micro-batch, streaming, and on-demand inference by working backwards from when the prediction is actually consumed — exposing prediction staleness as the real cost, and pricing train/serve skew risk per serving shape. |

**Reproduce**

| Prompt | Use it to |
|---|---|
| [`mlops_reproducibility_audit.md`](mlops_reproducibility_audit.md) | Audit an ML project for reproducibility gaps across code, data, environment, seeds, and config — then produce ranked, concrete remediations to make any result re-runnable. |
| [`mlops_environment_dependency_management.md`](mlops_environment_dependency_management.md) | Manage Python, CUDA, and library environments so training and serving are reproducible and consistent — pinned, locked, and verified across dev, CI, and production. |

**Capacity and cost**

| Prompt | Use it to |
|---|---|
| [`mlops_gpu_capacity_planning.md`](mlops_gpu_capacity_planning.md) | Plan accelerator capacity across training and serving — sizing from measured utilization rather than device count, separating memory-bound from compute-bound workloads, and deciding the reserved/on-demand/spot mix against interruption tolerance. |
| [`mlops_infra_cost_optimization.md`](mlops_infra_cost_optimization.md) | Reduce training and serving infrastructure cost without unacceptable loss of model quality or latency — by measuring spend, ranking levers, and gating each cut on a quality/SLA check. |
| [`mlops_cost_attribution_showback.md`](mlops_cost_attribution_showback.md) | Attribute shared ML training, serving, storage, and data-pipeline spend back to teams, models, and products in a multi-tenant environment — tagging strategy, allocation of un-taggable shared cost, showback vs chargeback, and a per-model cost view built only from observed billing data. |
| [`mlops_cost_budget_forecasting.md`](mlops_cost_budget_forecasting.md) | Build a forward-looking ML cost model — unit economics ($/prediction, $/training run, $/1k tokens), volume drivers, budget envelopes, scenario forecasts under growth and retraining, and spend guardrails (budget alerts, anomaly detection, cost-per-unit regression gates) — using only stated unit costs and volumes. |
| [`mlops_carbon_accounting_deep_dive.md`](mlops_carbon_accounting_deep_dive.md) | Operational carbon accounting for ML training and serving — measured energy (kWh) × PUE × region grid carbon intensity, embodied vs operational emissions, Scope 2 (location- vs market-based) and Scope 3 framing — reporting only from measured inputs and stated assumptions, never invented energy or emissions figures. |

**Assess**

| Prompt | Use it to |
|---|---|
| [`mlops_maturity_assessment.md`](mlops_maturity_assessment.md) | Assess a team or org's MLOps maturity across the lifecycle, score each dimension against evidence, and produce a prioritized, sequenced improvement roadmap. |

**Tool playbooks**

| Prompt | Use it to |
|---|---|
| [`mlops_mlflow_experiment_tracking_playbook.md`](mlops_mlflow_experiment_tracking_playbook.md) | Stand up MLflow for experiment tracking and model-registry promotion on a real stack — tracking server, run/artifact conventions, autologging, registry stages, and reproducibility hooks — without fabricating version-specific API behavior. |
| [`mlops_wandb_experiment_tracking_playbook.md`](mlops_wandb_experiment_tracking_playbook.md) | Stand up Weights & Biases for experiment tracking, sweeps, and artifact lineage on a real stack — project/entity structure, run conventions, what to log, sweep configuration, and reproducibility hooks — without inventing version-specific API behavior. |
| [`mlops_sagemaker_deployment_playbook.md`](mlops_sagemaker_deployment_playbook.md) | Design a training-to-serving workflow on Amazon SageMaker — training jobs, model registry, real-time vs. batch vs. async endpoints, CI/CD wiring, cost controls, and rollback — without inventing instance pricing or version-specific API behavior. |
| [`mlops_vertex_ai_deployment_playbook.md`](mlops_vertex_ai_deployment_playbook.md) | Design a training-to-serving workflow on Google Vertex AI — custom/AutoML training, Model Registry, online vs. batch prediction endpoints, Vertex Pipelines CI/CD, cost controls, and rollback — without inventing pricing or version-specific API behavior. |
| [`mlops_databricks_mlops_playbook.md`](mlops_databricks_mlops_playbook.md) | Design an end-to-end MLOps workflow on Databricks — managed MLflow tracking, Unity Catalog model registry, Model Serving endpoints, Workflows/Jobs CI/CD, and the deploy-code promotion pattern across dev/staging/prod — without inventing pricing or version-specific API behavior. |

## Conventions

- **Prefix:** `mlops_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/mlops-infrastructure`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.
- **Tool playbooks** stay version-neutral *inside* the named stack; version-specific API, pricing, and quota facts are flagged "verify against current docs" rather than asserted. Route to the platform-neutral sibling first when the user has not chosen a tool.

## What lives elsewhere

- MLOps maturity framed for a leadership audience → [`../ai-product-leadership/aipm_mlops_maturity_for_leaders.md`](../ai-product-leadership/aipm_mlops_maturity_for_leaders.md).
- The notebook-to-production learning arc → [`../learning-ai-ml/notebook-to-production/`](../learning-ai-ml/notebook-to-production/README.md).
