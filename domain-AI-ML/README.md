# AI / ML: Practitioner, Leadership & Learner Prompt Library

The canonical home in this repository for **doing AI/ML work** — building, training, evaluating, shipping, governing, and learning machine-learning and AI systems. This domain serves three audiences:

- **ML/AI practitioners** — data scientists, ML engineers, applied scientists, AI engineers, researchers.
- **AI product & leadership** — ML PMs, eng leads, and decision-makers scoping, funding, and governing AI work.
- **Learners & AI literacy** — people building skills, reading papers, prepping for interviews, or making sense of the field.

## Scope

This domain covers the practitioner lifecycle: problem framing, data for ML, feature engineering, classical modeling, deep learning, evaluation & validation, MLOps & infrastructure, production monitoring, model optimization, GenAI/LLM engineering, agentic systems, specialized verticals (CV, NLP, recsys, time-series, RL, multimodal), responsible AI & governance, AI product leadership, and learning paths.

Prompts are written for users who already know roughly what they need. They omit generic "consult an expert" boilerplate. Substantive guardrails — no fabricated benchmarks, reproducibility discipline, leakage-before-celebration, evidence-before-bias-claims — are encoded as testable constraints inside each prompt.

## Directory Map

**326 prompts across 16 subdirectories.** Counts are per-directory totals.

```
domain-AI-ML/
├── problem-framing-scoping/   (10)   Domain triage router (the front door), is-this-ML, use-case canvas,
│                                     success metrics, baseline-first, build/buy/finetune, data readiness,
│                                     feasibility, cost-of-wrong
├── data-for-ml/               (19)   Curation, quality audit, labeling, leakage detection, splits,
│                                     imbalance, augmentation, synthetic data, versioning, datasheets,
│                                     data contracts + schema evolution + CI enforcement,
│                                     active learning, weak supervision, DVC & lakeFS playbooks
├── feature-engineering/        (9)   Ideation, selection, encoding, leak-safe pipelines, importance,
│                                     feature stores, feature drift, Feast & Tecton playbooks
├── classical-ml-modeling/     (10)   Algorithm selection, baselines, HPO, cross-validation, imbalance,
│                                     regularization, ensembling, calibration, fit diagnosis
├── deep-learning/             (15)   Architecture, training debugging, overfitting, LR/optimizer,
│                                     transfer/fine-tuning, distributed, mixed precision, gradients,
│                                     self-supervised pretraining, continual learning, mixture-of-experts
├── model-evaluation-validation/(16)  Metric selection, eval harness, error slicing, significance,
│                                     offline/online alignment, benchmarks, robustness, model A/B,
│                                     calibration, eval-result skepticism; uncertainty quantification,
│                                     conformal prediction, OOD detection, selective prediction
├── mlops-infrastructure/      (22)   Experiment tracking, registry, ML CI/CD, reproducibility, serving,
│                                     feature pipelines, packaging, maturity, cost attribution/showback,
│                                     budget & forecast, carbon accounting; MLflow, W&B, SageMaker,
│                                     Vertex AI & Databricks playbooks; GPU capacity planning,
│                                     batch-vs-streaming inference, online learning
├── production-monitoring/     (16)   Drift, dashboards, degradation triage, retraining triggers,
│                                     incident response, canary/shadow, rollback, SLOs, feedback loops,
│                                     postmortem template, runbook library, GenAI & CV incident patterns,
│                                     champion-challenger, model portfolio health review
├── model-optimization-efficiency/(11) Quantization (PTQ + QAT), pruning, distillation,
│                                     latency/throughput, hardware selection, edge deployment,
│                                     compression tradeoffs, LLM inference serving, model routing/cascades
├── genai-llm-engineering/     (30)   RAG design & eval, fine-tuning workflows, LLM eval, LLM-as-judge,
│                                     guardrails, observability, embeddings, chunking, function calling,
│                                     multilingual, long-context, RAFT, structured extraction at scale;
│                                     pgvector, Pinecone, Weaviate & Milvus playbooks; query rewriting,
│                                     reranking, vector-index tuning, citation grounding, GraphRAG,
│                                     model-facing tool interfaces (MCP)
├── agentic-ai-systems/        (42)   The domain's largest subdirectory, organized as a build pipeline:
│                                     Gate 0 justify-the-agent → design (architecture, tools, memory, eval,
│                                     cost, HITL, failure modes) → coordinate a fleet (planning, topology,
│                                     protocol, routing) → run it durably (observability, durable execution,
│                                     deployment, context at scale, long-running continuity & recovery,
│                                     project memory) → secure it (threat model, trust boundaries,
│                                     least agency, zero trust, supply chain, injection & memory-poisoning
│                                     defense, enforced gates) → improve it.
│                                     See agentic-ai-systems/README.md for the sequencing.
├── model-security/            (10)   ML threat model, adversarial robustness & defense, data poisoning
│                                     & backdoors, model extraction, membership inference, model
│                                     inversion, ML supply chain, watermarking/provenance, secure
│                                     inference endpoints
├── specialized-ml/            (50)   Seven verticals. Each keeps its framing prompt in its own directory.
│   ├── computer-vision/       (10)   Task framing, annotation, augmentation, detection/segmentation eval,
│   │                                 video understanding, 3D/point-cloud, OCR, medical imaging
│   ├── recommender-systems/    (9)   Architecture, cold start, candidate/ranking, offline eval,
│   │                                 feedback bias, sequential/session, multi-objective ranking, bandits
│   ├── time-series/            (9)   Forecasting selection, TS features, backtesting, anomaly, seasonality,
│   │                                 leakage audit, hierarchical, probabilistic, intermittent demand
│   ├── reinforcement-learning/ (8)   Problem framing, reward design, environment, algo selection,
│   │                                 eval/safety, offline RL, RLHF/RLAIF, multi-agent RL
│   ├── nlp-classical/          (6)   Task framing; non-LLM text: classification, NER, tokenization,
│   │                                 topic modeling, preprocessing
│   ├── other-modalities/       (4)   Multimodal, speech (ASR/TTS), non-speech audio, anomaly/outlier
│   └── graph-ml/               (4)   Task framing, link prediction, fraud-graph patterns, GNN scalability
├── responsible-ai-governance/ (25)   Bias audit, fairness metrics & mitigation, model cards,
│                                     explainability, interpretability, governance framework, red-team,
│                                     privacy/PII, sustainability; model risk assessment + register +
│                                     doc-suite orchestrator + freshness audit; regulatory assessments
│                                     (EU AI Act, NIST AI RMF, FDA SaMD, fair-lending/ECOA,
│                                     GDPR Art. 22, SR 11-7 MRM); privacy-technique selection,
│                                     differential privacy, federated-learning governance, machine unlearning
├── ai-product-leadership/     (12)   Use-case prioritization, scoping, build/buy/partner, exec risk briefs,
│                                     ROI business case, team/hiring, roadmap, vendor selection,
│                                     MLOps maturity for leaders, AI policy authoring, failed-project postmortem
└── learning-ai-ml/            (29)   12 flat generators — concept & math explainers, paper reading/digest,
                                      reproduce-a-paper, interview prep, ML system design, study paths,
                                      portfolios, Kaggle, glossary, understanding debugger — plus four
                                      sequenced series:
    ├── study-tracks/           (4)   Instantiated CV / NLP-LLM / RL / MLOps specialization curricula
    ├── paper-reproductions/    (4)   ResNet, Transformer, word2vec, DQN — strict no-fabrication convention
    ├── interview-bank/         (5)   System-design question banks by problem class + a universal rubric
    └── notebook-to-production/ (4)   Sequenced arc: refactor → pipeline → serve → deploy/monitor/CI-CD
```

Wave history and the committed Wave 9 build list live in [`EXPANSION_ROADMAP.md`](EXPANSION_ROADMAP.md).

## How These Prompts Are Built

Every prompt includes:
- **Required context inputs** — task, data shape, framework + version, and metrics where relevant. Outputs degrade gracefully when some are missing, but the prompt asks rather than assumes.
- **No-fabrication clause** — the model must not invent benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. It reasons from the user's actual data and says when something is unknowable.
- **Reproducibility discipline** — seeds, environment, and data versioning surfaced wherever they affect a claim.
- **Locked output format** — tables, report skeletons, decision matrices that drop straight into a notebook, design doc, or model card.
- **Verification block** — a self-check covering evidence discipline, baseline comparison, and the domain's specific failure modes.
- **False-Positive Prevention (❌/✅)** — adapted to ML: don't declare bias without slice evidence; don't declare drift without a baseline window; don't celebrate metrics before ruling out leakage; distinguish correlation from causation.

## Conventions

- **File naming:** `{prefix}_{specific_function}.md` per subdirectory (`mlframe_`, `mldata_`, `mlfeature_`, `mlmodel_`, `dl_`, `mleval_`, `mlops_`, `mlmonitor_`, `mlopt_`, `genai_`, `aiagent_`, `cv_`/`nlp_`/`recsys_`/`ts_`/`rl_`/`graphml_`/`mlmodal_`, `rai_`, `aipm_`, `mllearn_`).
- **Frontmatter:** `title`, `category` (`AI-ML/<subdir>`), `description`, `techniques` (valid IDs from `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Framework-neutral by default:** the user supplies framework + version (PyTorch, TensorFlow/Keras, JAX, scikit-learn, XGBoost, etc.); prompts avoid hardcoding APIs that drift.

## What These Prompts Are Not

- Not a substitute for running the experiment. They produce design, diagnosis, and decision scaffolding — not measured results.
- Not bound to a specific MLOps platform (MLflow, W&B, SageMaker, Vertex, Databricks). Outputs are platform-neutral; the user names their stack.
- Not a replacement for the existing prompt-engineering and LLM-ops content in this repo — they **cross-link** it (see below).

## Boundary with adjacent domains

**This table is authoritative.** Several neighbouring domains touch AI/ML; a prompt that would sit on one of these seams belongs where the table says, and is cross-linked from here rather than duplicated. The same table appears as [Explicitly not gaps](EXPANSION_ROADMAP.md#explicitly-not-gaps) in the roadmap, where it governs what may be proposed for a future wave.

**Tie-break rule.** ML/AI engineering judgment about *the model itself* — its data, training, evaluation, serving, security, and governance — lives here. The surrounding discipline's judgment lives in that discipline's domain. When a prompt's conclusion would need a lawyer, a clinician, a statistician, or a board to sign off, it belongs to their domain and cross-links back here.

| Topic | Lives here when… | Lives elsewhere when… | Where |
|---|---|---|---|
| **Statistical inference** | You are choosing an evaluation metric, designing a model A/B test, or judging whether a metric delta is real | You are designing a study, estimating a causal effect, or running survival/time-to-event analysis | `domain-science/statistics/` |
| **Model risk** | You are assessing a model's own failure modes, documentation, and governance controls | The question is regulated-finance model validation and capital treatment | `domain-finance/` |
| **Regulation** | You are mapping a system onto a framework's *structure* and finding evidence gaps | You need statutory interpretation, article text, or a legal opinion | `domain-legal/` |
| **Clinical AI** | You are designing CV/tabular modelling and evaluation for medical data | The question is clinical validity, care pathways, or device practice | `domain-healthcare-clinical/` |
| **Prompt craft** | You are engineering an LLM *system* — retrieval, evaluation, guardrails, cost | You want prompt patterns, RAG prompt templates, or hallucination control at the prompt level | `domain-prompt-engineering/{rag-prompts,hallucination-control,instruction-design}/` |
| **Agent control flow** | You are making an architecture decision (topology, protocol, memory, gates) | You want a reusable control-flow or tool-use prompt template | `domain-prompt-engineering/{agent-workflows,tool-use}/` |
| **Agentic system authoring** | You are deciding one thing about one agent | You want a whole production-ready system produced from a use case | `agentic-system-factory/`, `authoring/system-patterns/` |
| **Executable capability** | You want design, diagnosis, or decision scaffolding | You want a runnable skill or scaffold | `domain-agentic-resources/skills/{llm-application-dev,ml-ai}/` |
| **Strategy** | You are scoping, prioritizing, or building the business case for an ML project | The question is board-level or enterprise AI strategy | `domain-business-strategy/ai-strategy/` |
| **Platform engineering** | You are designing model serving, ML CI/CD, or training orchestration | The question is general containers, infra, or DevOps practice | `domain-software-engineering/devops/` |
| **Security** | The attack surface is the *model* — adversarial inputs, poisoning, extraction, inversion — or the *agent* — trust boundaries, agency scope, memory poisoning | The attack surface is the surrounding *application* — injection at the app layer, output handling, authn/z | `domain-software-engineering/analysis/security/security_llm_application_review.md` |
| **Agent lifecycle patterns** | You are designing the agent | You want auto-improving triplets, task delegation specs, or work-loop patterns | `domain-engineering-workflows/ai-patterns/` |

`genai-llm-engineering/` covers the *engineering workflow* — RAG system design, fine-tuning workflow, LLM eval harness, guardrails, observability — and cross-links the ops, security, and prompt files above rather than re-implementing them.

> **Note.** `domain-software-engineering/analysis/ml_model_evaluation.md` predates this domain and is superseded by the 12 `mleval_*` prompts in `model-evaluation-validation/`. It is retained where it sits but should not be treated as the model-evaluation entry point.

## Routing (for Claude)

Organized by **lifecycle stage**, not by the wave that shipped a prompt. Match the user's request to a stage, then to a file. Filenames are descriptive `{prefix}_{function}`, so the Directory Map above doubles as the exhaustive index; the rows below are the high-traffic entries.

### 1. Frame — before any modelling

| User says | Use |
|---|---|
| **"I don't know where to start / the model isn't working"** | `problem-framing-scoping/mlframe_domain_triage_router.md` — **the front door**; classifies the situation and emits an ordered prompt sequence |
| "Is this even an ML problem?" | `problem-framing-scoping/mlframe_is_this_an_ml_problem.md` |
| "Turn my business problem into an ML task" | `problem-framing-scoping/mlframe_problem_to_ml_task_translator.md` |
| "Scope the use case end to end" | `problem-framing-scoping/mlframe_ml_use_case_canvas.md` |
| "What should success look like?" | `problem-framing-scoping/mlframe_success_metric_selection.md` |
| "Do we even have the data for this?" | `problem-framing-scoping/mlframe_data_readiness_assessment.md` |
| "Is this feasible, and what could go wrong?" | `problem-framing-scoping/mlframe_feasibility_risk_assessment.md` |
| "What does a wrong prediction actually cost?" | `problem-framing-scoping/mlframe_cost_of_being_wrong_analysis.md` |
| "Start with a baseline, not a model" | `problem-framing-scoping/mlframe_baseline_first_design.md` |
| "Should we build, buy, or fine-tune?" | `problem-framing-scoping/mlframe_build_buy_finetune_decision.md`, `ai-product-leadership/aipm_build_buy_partner_decision.md` |

### 2. Data

| User says | Use |
|---|---|
| "Curate / audit the dataset" | `data-for-ml/mldata_dataset_curation_plan.md`, `mldata_data_quality_audit.md` |
| "My results look too good to be true" | `data-for-ml/mldata_data_leakage_detector.md` + `model-evaluation-validation/mleval_eval_result_skepticism_audit.md` |
| "How should I split train/test?" | `data-for-ml/mldata_train_test_split_strategy.md` |
| "Write labeling guidelines / review annotation quality" | `data-for-ml/mldata_labeling_guideline_designer.md`, `mldata_annotation_quality_review.md` |
| "My classes are badly imbalanced" | `data-for-ml/mldata_class_imbalance_strategy.md`, `classical-ml-modeling/mlmodel_imbalanced_classification_approach.md` |
| "Augment / synthesize training data" | `data-for-ml/mldata_data_augmentation_plan.md`, `mldata_synthetic_data_strategy.md` |
| "Is my sample biased?" | `data-for-ml/mldata_sampling_bias_audit.md` |
| "Version my data / track lineage" | `data-for-ml/mldata_data_versioning_lineage.md`; with a tool: `mldata_dvc_data_versioning_playbook.md`, `mldata_lakefs_data_versioning_playbook.md` |
| "Design a data contract / handle schema evolution / enforce it in CI" | `data-for-ml/mldata_data_contract_design.md`, `mldata_schema_evolution_strategy.md`, `mldata_data_contract_enforcement_ci.md` |
| "Document the dataset" | `data-for-ml/mldata_datasheet_authoring.md` |
| "Where should I spend my labelling budget?" | `data-for-ml/mldata_active_learning_strategy.md` |
| "Can I derive labels instead of buying them?" | `data-for-ml/mldata_weak_supervision_strategy.md` |

### 3. Features

| User says | Use |
|---|---|
| "What features should I build?" | `feature-engineering/mlfeature_ideation_workshop.md` |
| "Which features actually matter?" | `feature-engineering/mlfeature_selection_strategy.md`, `mlfeature_importance_analysis.md` |
| "How do I encode these variables?" | `feature-engineering/mlfeature_encoding_strategy.md` |
| "Keep leakage out of my feature pipeline" | `feature-engineering/mlfeature_leakage_safe_pipeline.md` |
| "My features drifted" | `feature-engineering/mlfeature_drift_audit.md` |
| "Do I need a feature store?" | `feature-engineering/mlfeature_store_design.md`; with a tool: `mlfeature_feast_feature_store_playbook.md`, `mlfeature_tecton_feature_store_playbook.md` |

### 4. Model — classical and deep

| User says | Use |
|---|---|
| "Which algorithm should I use?" | `classical-ml-modeling/mlmodel_algorithm_selection_matrix.md` |
| "Give me a baseline plan" | `classical-ml-modeling/mlmodel_baseline_modeling_plan.md` |
| "Design cross-validation / tune hyperparameters" | `classical-ml-modeling/mlmodel_cross_validation_design.md`, `mlmodel_hyperparameter_tuning_strategy.md` |
| "Am I overfitting or underfitting?" | `classical-ml-modeling/mlmodel_overfitting_underfitting_diagnosis.md` |
| "Regularize / ensemble / calibrate" | `classical-ml-modeling/mlmodel_regularization_strategy.md`, `mlmodel_ensembling_strategy.md`, `mlmodel_probability_calibration.md` |
| "I need a model people can interpret" | `classical-ml-modeling/mlmodel_interpretability_first_modeling.md` |
| "Pick a neural architecture" | `deep-learning/dl_architecture_selection.md` |
| "My training loss won't go down" | `deep-learning/dl_training_not_converging_debug.md` |
| "Exploding / vanishing gradients" | `deep-learning/dl_gradient_issue_debug.md` |
| "Choose a learning rate and optimizer" | `deep-learning/dl_learning_rate_optimizer_selection.md` |
| "Fine-tune / transfer-learn from a pretrained model" | `deep-learning/dl_fine_tuning_strategy.md`, `dl_transfer_learning_plan.md` |
| "Train across multiple GPUs / use mixed precision" | `deep-learning/dl_distributed_training_plan.md`, `dl_mixed_precision_setup.md` |
| "My data loader is the bottleneck" | `deep-learning/dl_data_loading_bottleneck_audit.md` |
| "Make training reproducible" | `deep-learning/dl_reproducibility_setup.md` |
| "Pretrain on unlabelled domain data" | `deep-learning/dl_self_supervised_pretraining.md` |
| "Add new classes/tasks without forgetting the old ones" | `deep-learning/dl_continual_learning_strategy.md` |
| "Is mixture-of-experts worth it?" | `deep-learning/dl_mixture_of_experts_design.md` |

### 5. Evaluate

| User says | Use |
|---|---|
| "What metric should I optimize?" | `model-evaluation-validation/mleval_metric_selection_guide.md` |
| "Build an evaluation harness" | `model-evaluation-validation/mleval_evaluation_harness_design.md` |
| "Where exactly is my model failing?" | `model-evaluation-validation/mleval_error_analysis_slicing.md` |
| "Is this improvement real?" | `model-evaluation-validation/mleval_statistical_significance_testing.md`, `mleval_baseline_comparison_protocol.md` |
| "My eval results look too good" | `model-evaluation-validation/mleval_eval_result_skepticism_audit.md` |
| "Offline metrics don't match production" | `model-evaluation-validation/mleval_offline_online_alignment.md` |
| "A/B test two models" | `model-evaluation-validation/mleval_ab_test_design_for_models.md` |
| "Stress-test robustness / design a benchmark" | `model-evaluation-validation/mleval_robustness_stress_testing.md`, `mleval_benchmark_design.md` |
| "Are my probabilities calibrated?" | `model-evaluation-validation/mleval_calibration_assessment.md` |
| "Read this confusion matrix" | `model-evaluation-validation/mleval_confusion_matrix_interpretation.md` |
| "How sure is the model, and can I act on that?" | `model-evaluation-validation/mleval_uncertainty_quantification_design.md` |
| "I need a coverage guarantee, not a score" | `model-evaluation-validation/mleval_conformal_prediction_design.md` |
| "Flag inputs the model shouldn't be trusted on" | `model-evaluation-validation/mleval_ood_detection_design.md` |
| "When should the model decline to answer?" | `model-evaluation-validation/mleval_selective_prediction_abstention.md` |

### 6. Optimize — make it small, fast, cheap

| User says | Use |
|---|---|
| "Inference is too slow" | `model-optimization-efficiency/mlopt_inference_latency_optimization.md` |
| "Quantize / prune / distill the model" | `model-optimization-efficiency/mlopt_quantization_plan.md`, `mlopt_pruning_strategy.md`, `mlopt_knowledge_distillation_plan.md` |
| "What am I giving up by compressing?" | `model-optimization-efficiency/mlopt_compression_tradeoff_analysis.md` |
| "Run it on-device / at the edge" | `model-optimization-efficiency/mlopt_edge_deployment_optimization.md` |
| "Which accelerator should we buy?" | `model-optimization-efficiency/mlopt_hardware_accelerator_selection.md` |
| "Raise throughput / tune batching" | `model-optimization-efficiency/mlopt_throughput_batching_optimization.md` |
| "LLM serving is slow or expensive (KV cache, speculative decoding, continuous batching)" | `model-optimization-efficiency/mlopt_llm_inference_serving_optimization.md` |
| "Post-training quantization lost too much accuracy" | `model-optimization-efficiency/mlopt_quantization_aware_training.md` |
| "Route easy requests to a cheaper model" | `model-optimization-efficiency/mlopt_model_routing_cascade_design.md` |

### 7. Ship — MLOps & infrastructure

| User says | Use |
|---|---|
| "Set up experiment tracking" | `mlops-infrastructure/mlops_experiment_tracking_setup.md`; with a tool: `mlops_mlflow_experiment_tracking_playbook.md`, `mlops_wandb_experiment_tracking_playbook.md` |
| "Design a model registry / packaging strategy" | `mlops-infrastructure/mlops_model_registry_design.md`, `mlops_model_packaging_strategy.md` |
| "Build ML CI/CD" | `mlops-infrastructure/mlops_ml_cicd_pipeline_design.md` |
| "Orchestrate the training pipeline" | `mlops-infrastructure/mlops_training_pipeline_orchestration.md`, `mlops_feature_pipeline_design.md` |
| "Design model serving" | `mlops-infrastructure/mlops_model_serving_architecture.md` |
| "Nobody can reproduce this run" | `mlops-infrastructure/mlops_reproducibility_audit.md`, `mlops_environment_dependency_management.md` |
| "Deploy on SageMaker / Vertex AI / Databricks" | `mlops-infrastructure/mlops_sagemaker_deployment_playbook.md`, `mlops_vertex_ai_deployment_playbook.md`, `mlops_databricks_mlops_playbook.md` |
| "Our ML bill is out of control" | `mlops-infrastructure/mlops_infra_cost_optimization.md`, `mlops_cost_attribution_showback.md`, `mlops_cost_budget_forecasting.md` |
| "Account for the carbon cost" | `mlops-infrastructure/mlops_carbon_accounting_deep_dive.md`, `responsible-ai-governance/rai_sustainability_carbon_assessment.md` |
| "How mature is our MLOps?" | `mlops-infrastructure/mlops_maturity_assessment.md`, `ai-product-leadership/aipm_mlops_maturity_for_leaders.md` |
| "How many GPUs do we actually need?" | `mlops-infrastructure/mlops_gpu_capacity_planning.md` |
| "Batch, streaming, or on-demand inference?" | `mlops-infrastructure/mlops_batch_vs_streaming_inference.md` |
| "Update the model continuously from production feedback" | `mlops-infrastructure/mlops_online_learning_pipeline_design.md` |
| "Take my notebook to production, step by step" | `learning-ai-ml/notebook-to-production/mllearn_n2p_0*.md` |

### 8. Monitor — production

| User says | Use |
|---|---|
| "Detect drift" | `production-monitoring/mlmonitor_drift_detection_design.md` |
| "My model degraded in prod" | `production-monitoring/mlmonitor_performance_degradation_triage.md` |
| "When should we retrain?" | `production-monitoring/mlmonitor_retraining_trigger_strategy.md` |
| "Design monitoring dashboards / SLOs" | `production-monitoring/mlmonitor_monitoring_dashboard_design.md`, `mlmonitor_slo_design_for_ml.md` |
| "Roll out safely / roll back" | `production-monitoring/mlmonitor_canary_shadow_deployment.md`, `mlmonitor_rollback_strategy.md` |
| "Run an ML incident / write the postmortem" | `production-monitoring/mlmonitor_ml_incident_response.md`, `mlmonitor_incident_postmortem_template.md`, `mlmonitor_incident_runbook_library.md` |
| "GenAI or CV incident patterns" | `production-monitoring/mlmonitor_genai_incident_patterns.md`, `mlmonitor_cv_incident_patterns.md` |
| "Is the model influencing its own training data?" | `production-monitoring/mlmonitor_feedback_loop_detection.md` |
| "Audit data-pipeline health" | `production-monitoring/mlmonitor_data_pipeline_health_audit.md` |
| "Run challengers against the production model continuously" | `production-monitoring/mlmonitor_champion_challenger_design.md` |
| "How many models are we running, and who owns them?" | `production-monitoring/mlmonitor_model_portfolio_health_review.md` |

### 9. Govern — responsible AI & regulation

| User says | Use |
|---|---|
| "Is my model biased?" | `responsible-ai-governance/rai_bias_detection_audit.md` |
| "Which fairness metric, and how do we mitigate?" | `responsible-ai-governance/rai_fairness_metric_selection.md`, `rai_fairness_mitigation_strategy.md` |
| "Explain / interpret the model" | `responsible-ai-governance/rai_explainability_plan.md`, `rai_interpretability_analysis.md` |
| "Write a model card / assemble the doc suite" | `responsible-ai-governance/rai_model_card_authoring.md`, `rai_documentation_suite_orchestrator.md`, `rai_documentation_freshness_audit.md` |
| "Stand up AI governance / an ethics review" | `responsible-ai-governance/rai_governance_framework_design.md`, `rai_ethics_review_protocol.md` |
| "Assess and track model risk" | `responsible-ai-governance/rai_model_risk_assessment.md`, `rai_model_risk_register.md` |
| "Assess against EU AI Act / NIST AI RMF / FDA SaMD / ECOA / GDPR Art. 22 / SR 11-7" | `responsible-ai-governance/rai_eu_ai_act_compliance_assessment.md`, `rai_nist_ai_rmf_assessment.md`, `rai_fda_samd_compliance_assessment.md`, `rai_fair_lending_ecoa_assessment.md`, `rai_gdpr_automated_decisioning_assessment.md`, `rai_model_risk_management_sr1107.md` |
| "Red-team the model / check PII exposure" | `responsible-ai-governance/rai_red_teaming_plan.md`, `rai_privacy_pii_assessment.md` |
| "Which privacy technique do we actually need?" | `responsible-ai-governance/rai_privacy_technique_selection.md` |
| "Design differential privacy / federated learning" | `responsible-ai-governance/rai_differential_privacy_design.md`, `rai_federated_learning_governance.md` |
| "A deletion request has to reach our models" | `responsible-ai-governance/rai_machine_unlearning_deletion.md` |

### 10. GenAI & LLM engineering

| User says | Use |
|---|---|
| "Design a RAG system" | `genai-llm-engineering/genai_rag_system_design.md` |
| "My RAG retrieves the wrong things" | `genai-llm-engineering/genai_rag_retrieval_quality_debug.md`, `genai_chunking_strategy.md`, `genai_embedding_model_selection.md` |
| "Evaluate my RAG / LLM / judge" | `genai-llm-engineering/genai_rag_evaluation_harness.md`, `genai_llm_evaluation_design.md`, `genai_llm_as_judge_design.md` |
| "Fine-tune, RAG, or just prompt?" | `genai-llm-engineering/genai_finetune_vs_rag_vs_prompt_decision.md`, `genai_fine_tuning_workflow.md`, `genai_retrieval_augmented_finetuning.md` |
| "Guardrails / injection defense" | `genai-llm-engineering/genai_guardrails_design.md`, `genai_prompt_injection_defense.md` |
| "Trace and observe my LLM app" | `genai-llm-engineering/genai_llm_observability_tracing.md` |
| "Cut LLM cost and latency" | `genai-llm-engineering/genai_llm_cost_latency_optimization.md` |
| "Get structured output / function calls" | `genai-llm-engineering/genai_structured_output_function_calling.md`, `genai_structured_extraction_at_scale.md` |
| "Manage the context window / go long-context" | `genai-llm-engineering/genai_context_window_strategy.md`, `genai_long_context_strategy.md` |
| "Multilingual LLM system" | `genai-llm-engineering/genai_multilingual_design.md` |
| "Generate synthetic data with an LLM" | `genai-llm-engineering/genai_synthetic_data_with_llms.md` |
| "Retrieval misses what a human would find" | `genai-llm-engineering/genai_query_rewriting_expansion.md` |
| "The right passage is retrieved but ranked too low" | `genai-llm-engineering/genai_reranking_strategy.md` |
| "Tune the ANN index (recall vs latency vs memory)" | `genai-llm-engineering/genai_vector_index_tuning.md` |
| "Make answers verifiably traceable to sources" | `genai-llm-engineering/genai_citation_grounding_attribution.md` |
| "Queries need facts linked across documents (GraphRAG)" | `genai-llm-engineering/genai_graphrag_knowledge_graph_design.md` |
| "Design tools/an MCP server a model can use correctly" | `genai-llm-engineering/genai_mcp_tool_interface_design.md` |
| "Stand up a vector DB (pgvector / Pinecone / Weaviate / Milvus)" | `genai-llm-engineering/genai_pgvector_vector_db_playbook.md` and siblings |

### 11. Agentic systems

Full pipeline sequencing lives in [`agentic-ai-systems/README.md`](agentic-ai-systems/README.md).

| User says | Use |
|---|---|
| "Does this need an agent at all?" (**start here**) | `agentic-ai-systems/aiagent_complexity_ladder_gate.md` |
| "Design the agent" | `agentic-ai-systems/aiagent_architecture_design.md`, `aiagent_tool_design.md`, `aiagent_memory_design.md` |
| "Budget its cost / put a human in the loop" | `agentic-ai-systems/aiagent_cost_token_budget_design.md`, `aiagent_human_in_the_loop_design.md` |
| "Evaluate the agent" | `agentic-ai-systems/aiagent_evaluation_design.md`, `aiagent_agentic_safety_eval_layer.md` |
| "Coordinate a fleet" | `agentic-ai-systems/aiagent_multi_agent_orchestration.md`, `aiagent_orchestration_topology_selection.md`, `aiagent_inter_agent_communication_protocol.md`, `aiagent_task_routing_load_balancing.md` |
| "Make it survive crashes and long runs" | `agentic-ai-systems/aiagent_durable_execution_state_persistence.md`, `aiagent_long_running_task_setup.md`, `aiagent_failure_recovery_rescope.md`, `aiagent_cross_agent_handoff_recovery.md` |
| "Give it memory across sessions" | `agentic-ai-systems/aiagent_project_continuity_memory_design.md`, `aiagent_project_memory_capture_protocol.md`, `aiagent_project_memory_guard_before_action.md` |
| "Secure it" | `agentic-ai-systems/aiagent_agentic_threat_model.md`, `aiagent_trust_boundary_design.md`, `aiagent_least_agency_scoping.md`, `aiagent_prompt_injection_untrusted_content_defense.md`, `aiagent_memory_poisoning_defense.md` |
| "Enforce gates rather than trust instructions" | `agentic-ai-systems/aiagent_hard_gates_designer.md`, `aiagent_runtime_guardrails_policy.md` |
| "Zero-trust maturity / supply-chain attestation" | `agentic-ai-systems/aiagent_zero_trust_maturity_assessment.md`, `aiagent_supply_chain_aibom.md` |
| "Observe, deploy, and improve it" | `agentic-ai-systems/aiagent_observability_telemetry_design.md`, `aiagent_deployment_serving_architecture.md`, `aiagent_self_improvement_online_adaptation.md`, `aiagent_fleet_cost_attribution_optimization.md` |
| "Emit a master orchestrator for a multi-stage system" | `agentic-ai-systems/aiagent_orchestrator_generator.md` |

### 12. Secure the model

Security in this domain is deep on both sides: `model-security/` covers the model itself, `agentic-ai-systems/` covers the agent around it. Application-layer security lives in `domain-software-engineering/analysis/security/` — see the boundary table.

| User says | Use |
|---|---|
| "Threat-model our deployed model" (**start here**) | `model-security/mlsec_ml_threat_model.md` |
| "Can our model be fooled by crafted inputs?" | `model-security/mlsec_adversarial_robustness_assessment.md`, then `mlsec_adversarial_defense_strategy.md` |
| "Could our training data be poisoned / backdoored?" | `model-security/mlsec_data_poisoning_backdoor_defense.md` |
| "Can someone steal our model through the API?" | `model-security/mlsec_model_extraction_defense.md` |
| "Does the model reveal who was in its training set?" | `model-security/mlsec_membership_inference_defense.md` |
| "Does the model regurgitate its training data?" | `model-security/mlsec_model_inversion_leakage_audit.md` |
| "Where did these weights and datasets come from?" | `model-security/mlsec_ml_supply_chain_audit.md` |
| "Prove a model or its output is ours" | `model-security/mlsec_model_watermarking_provenance.md` |
| "Harden the inference endpoint" | `model-security/mlsec_secure_inference_endpoint_design.md` |

### 13. Specialized verticals

| User says | Use |
|---|---|
| "Frame a CV task / annotate / augment" | `specialized-ml/computer-vision/cv_task_framing.md`, `cv_annotation_strategy.md`, `cv_augmentation_strategy.md` |
| "Detection or segmentation, and how do I evaluate it?" | `specialized-ml/computer-vision/cv_object_detection_eval.md`, `cv_segmentation_approach.md` |
| "Video / 3D point cloud / OCR / medical imaging" | `specialized-ml/computer-vision/cv_video_understanding_design.md`, `cv_3d_point_cloud_design.md`, `cv_ocr_pipeline_design.md`, `cv_medical_imaging_considerations.md` |
| "Text classification / NER / topic modeling **without** an LLM" | `specialized-ml/nlp-classical/nlp_text_classification_design.md`, `nlp_ner_extraction_design.md`, `nlp_topic_modeling_approach.md` |
| "Tokenization and text representation / preprocessing" | `specialized-ml/nlp-classical/nlp_tokenization_representation_strategy.md`, `nlp_text_preprocessing_pipeline.md` |
| "Design a recommender / handle cold start" | `specialized-ml/recommender-systems/recsys_architecture_design.md`, `recsys_cold_start_strategy.md`, `recsys_candidate_ranking_design.md` |
| "Recsys evaluation, feedback bias, objectives, bandits" | `specialized-ml/recommender-systems/recsys_offline_evaluation.md`, `recsys_feedback_loop_bias_audit.md`, `recsys_objective_business_alignment.md`, `recsys_bandits_exploration.md` |
| "Pick a forecasting model / backtest it" | `specialized-ml/time-series/ts_forecasting_model_selection.md`, `ts_backtesting_design.md`, `ts_feature_engineering.md` |
| "Time-series leakage, seasonality, anomalies" | `specialized-ml/time-series/ts_data_leakage_audit.md`, `ts_seasonality_decomposition.md`, `ts_anomaly_detection_design.md` |
| "Hierarchical / probabilistic / intermittent-demand forecasting" | `specialized-ml/time-series/ts_hierarchical_forecasting.md`, `ts_probabilistic_forecasting.md`, `ts_intermittent_demand_forecasting.md` |
| "Frame an RL problem / design the reward" | `specialized-ml/reinforcement-learning/rl_problem_framing.md`, `rl_reward_function_design.md`, `rl_environment_design.md` |
| "RL algorithm choice, evaluation & safety" | `specialized-ml/reinforcement-learning/rl_algorithm_selection.md`, `rl_evaluation_safety.md` |
| "Offline RL / RLHF-RLAIF / multi-agent RL" | `specialized-ml/reinforcement-learning/rl_offline_rl_design.md`, `rl_rlhf_rlaif_pipeline_design.md`, `rl_multi_agent_rl_design.md` |
| "Frame a graph-ML task" | `specialized-ml/graph-ml/graphml_task_framing.md` |
| "Graph ML: link prediction, fraud graphs, GNN scale" | `specialized-ml/graph-ml/graphml_link_prediction_design.md`, `graphml_fraud_graph_patterns.md`, `graphml_gnn_scalability.md` |
| "Frame a non-LLM text task" | `specialized-ml/nlp-classical/nlp_task_framing.md` |
| "Multimodal / speech / anomaly detection" | `specialized-ml/other-modalities/mlmodal_multimodal_architecture.md`, `mlmodal_speech_asr_tts_framing.md`, `mlmodal_anomaly_outlier_detection.md` |
| "Non-speech audio: sound events, machine or wildlife acoustics" | `specialized-ml/other-modalities/mlmodal_audio_ml_design.md` |

### 14. Lead — AI product & leadership

| User says | Use |
|---|---|
| "Which AI use cases should we do first?" | `ai-product-leadership/aipm_use_case_prioritization.md`, `aipm_ml_project_scoping.md` |
| "Build the ROI case / brief the execs on risk" | `ai-product-leadership/aipm_roi_business_case.md`, `aipm_model_risk_brief_for_execs.md` |
| "Build, buy, or partner? Which vendor?" | `ai-product-leadership/aipm_build_buy_partner_decision.md`, `aipm_vendor_model_selection.md` |
| "Structure and hire the ML team" | `ai-product-leadership/aipm_ml_team_structure_hiring.md` |
| "Write the AI roadmap / AI policy" | `ai-product-leadership/aipm_ai_roadmap_design.md`, `aipm_ai_policy_authoring.md` |
| "Translate the jargon for stakeholders" | `ai-product-leadership/aipm_jargon_translator_for_stakeholders.md` |
| "Our ML project failed — what happened?" | `ai-product-leadership/aipm_failed_ml_project_postmortem.md` |
| "How mature is our MLOps, for a leadership audience?" | `ai-product-leadership/aipm_mlops_maturity_for_leaders.md` |

### 15. Learn

| User says | Use |
|---|---|
| "Explain this ML concept / the math behind it" | `learning-ai-ml/mllearn_concept_explainer.md`, `mllearn_math_for_ml_explainer.md`, `mllearn_glossary_builder.md` |
| "I don't actually understand this — find the hole" | `learning-ai-ml/mllearn_understanding_debugger.md` |
| "Help me read / digest this paper" | `learning-ai-ml/mllearn_paper_reading_guide.md`, `mllearn_paper_digest_generator.md` |
| "Plan how I learn ML" | `learning-ai-ml/mllearn_study_path_designer.md` |
| "Give me a full CV / NLP-LLM / RL / MLOps curriculum" | `learning-ai-ml/study-tracks/mllearn_study_track_*.md` |
| "Reproduce ResNet / the Transformer / word2vec / DQN" | `learning-ai-ml/paper-reproductions/mllearn_reproduce_*.md`; to plan your own: `domain-AI-ML/learning-ai-ml/mllearn_reproduce_paper_plan.md` |
| "Prep me for an ML interview" | `learning-ai-ml/mllearn_ml_interview_prep.md`, `mllearn_ml_system_design_interview.md` |
| "Graded system-design question bank + rubric" | `learning-ai-ml/interview-bank/mllearn_interview_bank_*.md`, `mllearn_interview_scoring_rubric.md` |
| "Design a portfolio project / compete on Kaggle" | `learning-ai-ml/mllearn_portfolio_project_designer.md`, `mllearn_kaggle_competition_strategy.md` |

---

Every subdirectory's file list in the Directory Map above is itself a complete index — filenames are descriptive `{prefix}_{function}`, so a prompt absent from the routing tables is still reachable by name. Each subdirectory also carries its own `README.md` with the full local index and conventions.
