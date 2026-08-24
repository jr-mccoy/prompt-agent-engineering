# domain-AI-ML — Expansion Roadmap

This domain launched with ~185 prompts across 15 topic areas covering the AI/ML practitioner lifecycle plus product-leadership and learner tracks. It now holds **326 prompts across 16 subdirectories**. This roadmap is the domain's shipping record and its boundary contract.

**Scope discipline.** This roadmap is intentionally finite. [Explicitly not gaps](#explicitly-not-gaps) is the **authoritative boundary**: a proposal to add anything listed there should be checked against it first and cross-linked rather than built. [Deliberately deferred](#deliberately-deferred) records what was considered and declined, with reasons.

---

## Shipping record

### Initial Build (shipped) — ~185 prompts

All 15 subdirectories populated (problem-framing, data, features, classical modeling, deep learning, evaluation, MLOps, monitoring, optimization, GenAI/LLM, agentic, specialized verticals, responsible AI, product leadership, learning). README, field guide, and roadmap in place; registered in `PROMPT_INDEX.json`, `PROMPT_INDEX.md`, and `CLAUDE.md`.

### Agentic systems — "larger autonomous systems" wave (shipped) — agentic 9 → 23

`agentic-ai-systems/` expanded from 9 → 23 prompts, adding the systems layer beyond single-agent design: multi-agent coordination depth (planning/decomposition, orchestration topology, inter-agent protocol, routing/load-balancing), runtime & reliability (observability/telemetry, durable execution, deployment/rollout, context engineering at scale), safety & security at scale (runtime guardrails, prompt-injection/untrusted-content defense, privacy/data governance), and quality & evolution (simulation/staging testing, self-improvement/online adaptation, fleet cost attribution). All cross-link — rather than duplicate — the prompt-level control-flow templates (`domain-prompt-engineering/agent-workflows/`, `tool-use/`), multi-agent contract templates (`domain-agentic-resources/commands/multi-agent/`), and single-agent lifecycle patterns (`domain-engineering-workflows/ai-patterns/`). See `agentic-ai-systems/README.md` for the build-pipeline sequencing.

### Wave 2 — Tooling Playbooks (platform-specific) — shipped — 13 prompts

Platform-neutral prompts remain the default; Wave 2 adds opinionated named-stack playbooks for
practitioners who have already adopted a specific tool. Each follows the domain's Tier-1 structure
(no-fabrication, reproducibility, False-Positive Prevention) and stays version-neutral *inside* the
named stack — version-specific API/pricing/quota facts are flagged "verify against current docs"
rather than asserted. 13 playbooks across four homes:

- **Experiment tracking** (`mlops-infrastructure/`): `mlops_mlflow_experiment_tracking_playbook.md`,
  `mlops_wandb_experiment_tracking_playbook.md`
- **Cloud training & deployment** (`mlops-infrastructure/`): `mlops_sagemaker_deployment_playbook.md`,
  `mlops_vertex_ai_deployment_playbook.md`, `mlops_databricks_mlops_playbook.md`
- **Data versioning** (`data-for-ml/`): `mldata_dvc_data_versioning_playbook.md`,
  `mldata_lakefs_data_versioning_playbook.md`
- **Feature stores** (`feature-engineering/`): `mlfeature_feast_feature_store_playbook.md`,
  `mlfeature_tecton_feature_store_playbook.md`
- **Vector databases** (`genai-llm-engineering/`, cross-linked to `domain-software-engineering/devops/`):
  `genai_pgvector_vector_db_playbook.md`, `genai_pinecone_vector_db_playbook.md`,
  `genai_weaviate_vector_db_playbook.md`, `genai_milvus_vector_db_playbook.md`

### Wave 3 — Deeper Verticals (shipped) — 20 prompts, index 214 → 234

Deepened the six specialized-ML verticals from breadth-first coverage with **20 new Tier-1 prompts**, one per enumerated topic. Each carries the domain signature (no-fabrication, reproducibility/leakage discipline, a vertical-specific False-Positive-Prevention failure mode, framework-neutral with empirical picks deferred to evaluation on the user's data). Graph ML graduated to its own dedicated `specialized-ml/graph-ml/` subdirectory (prefix `graphml_`). All registered in `PROMPT_INDEX.json` / `PROMPT_INDEX.md` with routing rows in the domain `README.md` and root `CLAUDE.md`.

- **Computer vision** (`specialized-ml/computer-vision/`, `cv_`): video understanding, 3D/point-cloud, OCR pipelines, medical imaging considerations — `cv_video_understanding_design.md`, `cv_3d_point_cloud_design.md`, `cv_ocr_pipeline_design.md`, `cv_medical_imaging_considerations.md`
- **NLP/GenAI** (`genai-llm-engineering/`, `genai_`): multilingual, long-context strategies, retrieval-augmented fine-tuning, structured extraction at scale — `genai_multilingual_design.md`, `genai_long_context_strategy.md`, `genai_retrieval_augmented_finetuning.md`, `genai_structured_extraction_at_scale.md`
- **Recsys** (`specialized-ml/recommender-systems/`, `recsys_`): sequential/session-based, multi-objective ranking, bandits for exploration — `recsys_sequential_session_based_design.md`, `recsys_multi_objective_ranking.md`, `recsys_bandits_exploration.md`
- **Time-series** (`specialized-ml/time-series/`, `ts_`): hierarchical forecasting, probabilistic forecasting, intermittent demand — `ts_hierarchical_forecasting.md`, `ts_probabilistic_forecasting.md`, `ts_intermittent_demand_forecasting.md`
- **RL** (`specialized-ml/reinforcement-learning/`, `rl_`): offline RL, RLHF/RLAIF pipelines (cross-linked to GenAI), multi-agent RL — `rl_offline_rl_design.md`, `rl_rlhf_rlaif_pipeline_design.md`, `rl_multi_agent_rl_design.md`
- **Graph ML** (**new** `specialized-ml/graph-ml/`, `graphml_`): link prediction, fraud-graph patterns, GNN scalability — `graphml_link_prediction_design.md`, `graphml_fraud_graph_patterns.md`, `graphml_gnn_scalability.md`

### Wave 4 — Cross-Cutting & Governance Depth (shipped) — 18 prompts, index 234 → 252

Filled the governance/cross-cutting layer with **18 new Tier-1 prompts** across four homes, all carrying the domain signature (no-fabrication, reproducibility/leakage discipline, a topic-specific False-Positive-Prevention block). For the regulatory prompts the anti-fabrication clause is load-bearing: they map a system to a framework's *structure* and obligations, the user confirms classification/version, and any specific article text, threshold, or citation is flagged "verify against the current official source" rather than asserted.

- **Data contracts & schema-evolution** (`data-for-ml/`, `mldata_`): `mldata_data_contract_design.md`, `mldata_schema_evolution_strategy.md`, `mldata_data_contract_enforcement_ci.md`
- **Cost/carbon accounting deep dives** (`mlops-infrastructure/`, `mlops_`): `mlops_cost_attribution_showback.md`, `mlops_cost_budget_forecasting.md`, `mlops_carbon_accounting_deep_dive.md`
- **Model documentation suites** (`responsible-ai-governance/`, `rai_`): `rai_model_risk_register.md`, `rai_documentation_suite_orchestrator.md`, `rai_documentation_freshness_audit.md`
- **Regulatory expansion beyond EU AI Act** (`responsible-ai-governance/`, `rai_`): `rai_nist_ai_rmf_assessment.md`, `rai_fda_samd_compliance_assessment.md`, `rai_fair_lending_ecoa_assessment.md`, `rai_gdpr_automated_decisioning_assessment.md`, `rai_model_risk_management_sr1107.md`
- **AI incident postmortem library & runbooks** (`production-monitoring/`, `mlmonitor_`): `mlmonitor_incident_postmortem_template.md`, `mlmonitor_incident_runbook_library.md`, `mlmonitor_genai_incident_patterns.md`, `mlmonitor_cv_incident_patterns.md`

### Wave 5 — Learner Depth (shipped) — 17 prompts + 1 series README, index 252 → 269

Added **17 new Tier-1 prompts + 1 series README** to the learner track, putting *instantiated depth* on top of the 12 existing `mllearn_*` generators and cross-linking — rather than duplicating — them. Organized into **four new subdirectories** inside `learning-ai-ml/` (the existing 12 standalone generators stay flat; the Wave-5 sets are cohesive, sequenced series).

- **Study tracks** (`learning-ai-ml/study-tracks/`, `mllearn_study_track_`): instantiated specialization curricula — not another generator — for computer vision, NLP/LLM, reinforcement learning, and MLOps. Each sequences phases by prerequisite, pairs every phase with a build + a demonstrable checkpoint, and describes resource *types* (never invents course/book/benchmark facts). Files: `mllearn_study_track_computer_vision.md`, `mllearn_study_track_nlp_llm.md`, `mllearn_study_track_reinforcement_learning.md`, `mllearn_study_track_mlops.md`.
- **Paper reproductions** (`learning-ai-ml/paper-reproductions/`, `mllearn_reproduce_`): scoped, landmark-paper reproduction guides — the highest-fabrication-risk content in the domain. **Load-bearing convention:** no paper-specific number, hyperparameter, dataset statistic, or score is asserted from memory — every such value is a `[extract from paper §X / Table Y]` placeholder; "reproduced" is the paper's *relative* claim over a tolerance band across seeds against a reimplemented baseline. A series `README.md` spells this out. Files: `mllearn_reproduce_resnet_image_classifier.md`, `mllearn_reproduce_transformer_attention.md`, `mllearn_reproduce_word2vec_embeddings.md`, `mllearn_reproduce_dqn_atari.md`.
- **Interview bank** (`learning-ai-ml/interview-bank/`, `mllearn_interview_`): graded question *banks* organized by problem class, each with junior/mid/senior/staff rubric bars that bake the ML failure-mode catalog into the senior/staff discriminators, plus a universal cross-topic scoring rubric. Files: `mllearn_interview_bank_recommendation_ranking.md`, `mllearn_interview_bank_search_systems.md`, `mllearn_interview_bank_nlp_llm_applications.md`, `mllearn_interview_bank_realtime_fraud_detection.md`, `mllearn_interview_scoring_rubric.md`.
- **Notebook → production** (`learning-ai-ml/notebook-to-production/`, `mllearn_n2p_0`): a sequenced 4-step guided arc (each step links its neighbors) — refactor a notebook into a tested package → reproducible training pipeline + tracking → package & serve with train/serve parity → deploy, monitor & CI/CD with a tested rollback. Files: `mllearn_n2p_01_refactor_notebook_to_package.md`, `mllearn_n2p_02_reproducible_training_pipeline.md`, `mllearn_n2p_03_package_and_serve_model.md`, `mllearn_n2p_04_deploy_monitor_cicd.md`.

### Wave 6 — Agentic Security Posture (shipped 2026-06-19) — 7 prompts

*Recorded retroactively: this wave shipped without a roadmap entry.* Moved `agentic-ai-systems/` from "secure the agent" as one design concern to a full security posture, treating an autonomous agent as an identity with privileges rather than a program with inputs. Files: `aiagent_agentic_threat_model.md`, `aiagent_trust_boundary_design.md`, `aiagent_least_agency_scoping.md`, `aiagent_zero_trust_maturity_assessment.md`, `aiagent_supply_chain_aibom.md`, `aiagent_memory_poisoning_defense.md`, `aiagent_secops_autonomous_defense.md`.

### Wave 7 — Agentic Authoring & Enforced Gates (shipped 2026-06-20) — 4 prompts

*Recorded retroactively.* The design-decision layer beneath the `agentic-system-factory/` pipeline and the `authoring/system-patterns/` manual: justify the agent before designing it, compose security/eval/governance into enforced gates rather than trusted instructions, emit a master orchestrator for a multi-stage system, and treat agentic safety evaluation as its own gate. Files: `aiagent_complexity_ladder_gate.md`, `aiagent_hard_gates_designer.md`, `aiagent_orchestrator_generator.md`, `aiagent_agentic_safety_eval_layer.md`.

### Wave 8 — Long-Running Continuity & Recovery (shipped 2026-06-21 → 06-25) — 8 prompts

*Recorded retroactively.* The problem of an agent that outlives a single session: what it must write down, what it must re-check before acting on what it wrote, how that memory decays or is poisoned, how it hands off, and how it recovers or re-scopes when a long task fails partway. Files: `aiagent_long_running_task_setup.md`, `aiagent_failure_recovery_rescope.md`, `aiagent_cross_agent_handoff_recovery.md`, `aiagent_project_continuity_memory_design.md`, `aiagent_project_memory_capture_protocol.md`, `aiagent_project_memory_guard_before_action.md`, `aiagent_project_memory_interop_adapter_design.md`, `aiagent_project_memory_security_decay_audit.md`.

**Running total before Wave 9: 286 prompts** — `agentic-ai-systems/` 42, `genai-llm-engineering/` 24, `responsible-ai-governance/` 21, `mlops-infrastructure/` 19, `data-for-ml/` 17, `production-monitoring/` 14, `ai-product-leadership/` 12, `deep-learning/` 12, `model-evaluation-validation/` 12, `learning-ai-ml/` 29 (12 flat + 17 in four series), `classical-ml-modeling/` 10, `feature-engineering/` 9, `problem-framing-scoping/` 9, `model-optimization-efficiency/` 8, `specialized-ml/` 48 across seven verticals.

---

## Wave 9 — Model Security, Uncertainty & Serving Depth (shipped 2026-08-22) — 40 prompts

The organizing observation: **security in this domain is deep on the agent side and absent on the model side.** Waves 6–8 gave `agentic-ai-systems/` a threat model, trust boundaries, least-agency scoping, supply-chain attestation and memory-poisoning defense. Meanwhile the repo has *zero* coverage of adversarial examples, model extraction, data poisoning, or model inversion — the attacks that apply to every deployed model whether or not an agent is involved. Wave 9 closes that, then fills three smaller verified gaps: prediction-time uncertainty, serving/inference economics, and retrieval depth.

### New subdirectory — `model-security/` (prefix `mlsec_`) — 10

`mlsec_ml_threat_model.md` · `mlsec_adversarial_robustness_assessment.md` · `mlsec_adversarial_defense_strategy.md` · `mlsec_data_poisoning_backdoor_defense.md` · `mlsec_model_extraction_defense.md` · `mlsec_membership_inference_defense.md` · `mlsec_model_inversion_leakage_audit.md` · `mlsec_ml_supply_chain_audit.md` · `mlsec_model_watermarking_provenance.md` · `mlsec_secure_inference_endpoint_design.md`

Cross-links rather than duplicates: `rai_red_teaming_plan.md`, `aiagent_agentic_threat_model.md`, `aiagent_supply_chain_aibom.md`, `domain-software-engineering/analysis/security/`.

**Wave-specific failure modes** for the False-Positive Prevention blocks, to be added to `field_guide.md`: attack feasibility asserted without threat-model grounding; a defense called effective without an adaptive-attacker evaluation; robustness measured against one attack and generalized to "robust"; a privacy technique named without stating what it does *not* protect against.

### Privacy-preserving ML — `responsible-ai-governance/` (`rai_`) — 4

`rai_differential_privacy_design.md` · `rai_federated_learning_governance.md` · `rai_machine_unlearning_deletion.md` · `rai_privacy_technique_selection.md`

### Prediction-time uncertainty — `model-evaluation-validation/` (`mleval_`) — 4

`mleval_uncertainty_quantification_design.md` · `mleval_conformal_prediction_design.md` · `mleval_ood_detection_design.md` · `mleval_selective_prediction_abstention.md`

### Data-efficient learning — `data-for-ml/` (`mldata_`) — 2

`mldata_active_learning_strategy.md` · `mldata_weak_supervision_strategy.md`

### Training-regime depth — `deep-learning/` (`dl_`) — 3

`dl_self_supervised_pretraining.md` · `dl_continual_learning_strategy.md` · `dl_mixture_of_experts_design.md`

### Serving & inference economics — `mlops-infrastructure/` + `model-optimization-efficiency/` — 6

`mlops_gpu_capacity_planning.md` · `mlops_batch_vs_streaming_inference.md` · `mlops_online_learning_pipeline_design.md` · `mlopt_llm_inference_serving_optimization.md` (KV cache, speculative decoding, continuous batching) · `mlopt_quantization_aware_training.md` · `mlopt_model_routing_cascade_design.md`

### Fleet-level production ops — `production-monitoring/` (`mlmonitor_`) — 2

`mlmonitor_champion_challenger_design.md` · `mlmonitor_model_portfolio_health_review.md`

### Retrieval & tool-interface depth — `genai-llm-engineering/` (`genai_`) — 6

`genai_query_rewriting_expansion.md` · `genai_reranking_strategy.md` · `genai_vector_index_tuning.md` · `genai_citation_grounding_attribution.md` · `genai_graphrag_knowledge_graph_design.md` · `genai_mcp_tool_interface_design.md`

### Thin-vertical framing — `specialized-ml/` — 2

`nlp-classical/nlp_task_framing.md` · `other-modalities/mlmodal_audio_ml_design.md`

Paired with a structural fix: `other-modalities/mlmodal_graph_ml_design.md` relocates to `graph-ml/graphml_task_framing.md`, matching `cv_task_framing.md` and `rl_problem_framing.md` — every vertical keeps its framing prompt in its own directory.

### Domain entry point — `problem-framing-scoping/` (`mlframe_`) — 1

`mlframe_domain_triage_router.md` — the front door. Modeled on `domain-negotiation/preparation/negotiation_prep_depth_triage.md`: classify the user's situation and emit an ordered prompt sequence, so the domain is consumed by route rather than exhaustively.

**Wave 9 total: 40 prompts. Domain total: 326** — `model-security/` 10, `genai-llm-engineering/` 30, `responsible-ai-governance/` 25, `mlops-infrastructure/` 22, `data-for-ml/` 19, `model-evaluation-validation/` 16, `production-monitoring/` 16, `deep-learning/` 15, `model-optimization-efficiency/` 11, `problem-framing-scoping/` 10, plus `specialized-ml/` 50 and the unchanged remainder.

**Quality gate at ship:** 326/326 carry the full 8-field frontmatter and the five canonical H2 sections; 1,048 `related_prompts` references all resolve; every technique ID validates against `techniques/MASTER_TECHNIQUE_INDEX.md`; 2,807 False-Positive Prevention bullets across the domain remain 2,796 distinct, with a maximum repeat of 4 — the pre-Wave-9 bar held.

---

## Explicitly not gaps

*This table is the authoritative boundary.* A proposal to add any of these should be checked against it first and cross-linked, never duplicated.

| Looks like a gap | Actually lives at | Why there |
|---|---|---|
| Causal inference, DAGs, IV/RDD/DiD | `domain-science/statistics/science_causal_inference_design.md` | Experimental-design judgment, not model engineering |
| Survival / time-to-event analysis | `domain-science/statistics/science_survival_analysis_design.md` | Same |
| Power analysis, multiple comparisons, pre-specified analysis plans | `domain-science/statistics/` | Same |
| Prompt patterns, RAG prompt templates, hallucination control at the prompt level | `domain-prompt-engineering/{rag-prompts,hallucination-control,instruction-design}/` | Prompt craft, not system engineering |
| Tool-use and agent-workflow prompt templates | `domain-prompt-engineering/{tool-use,agent-workflows}/` | Control-flow templates, not architecture decisions |
| Authoring a whole agentic system from a use case | `agentic-system-factory/`, `authoring/system-patterns/` | Those *orchestrate* this domain's `aiagent_*` design prompts |
| Ready-to-run LLM/ML skills and scaffolds | `domain-agentic-resources/skills/{llm-application-dev,ml-ai}/` | Executable capability, not design scaffolding |
| Board-level / enterprise AI strategy | `domain-business-strategy/ai-strategy/` | Strategy, not engineering |
| Serving infrastructure, containers, CI/CD as general practice | `domain-software-engineering/devops/` | Platform engineering the model happens to run on |
| LLM *application* security review (injection, output handling) | `domain-software-engineering/analysis/security/security_llm_application_review.md` | Application-layer review; Wave 9's `mlsec_*` covers the model itself |
| ML red-teaming exercise design | `responsible-ai-governance/rai_red_teaming_plan.md` | Already here — Wave 9 cross-links it |
| Auto-improving agent triplets, agent task delegation, work loops | `domain-engineering-workflows/ai-patterns/` | Single-agent lifecycle patterns |

**Tie-break rule.** ML/AI engineering judgment about *the model itself* — its data, training, evaluation, serving, security, and governance — lives here. The surrounding discipline's judgment lives in that discipline's domain. When a prompt would need a lawyer, a clinician, a statistician, or a board to sign off on its conclusion, it belongs to their domain and cross-links back here.

---

## Deliberately deferred

| Considered | Decision | Reason |
|---|---|---|
| Quantum ML | Not building | No practitioner demand signal; the field is not stable enough for framework-neutral guidance that will survive |
| AutoML platform playbooks | Not building | `mlmodel_algorithm_selection_matrix.md` + `mlmodel_hyperparameter_tuning_strategy.md` cover the decisions; platform playbooks would date fast |
| Per-model-family prompts (BERT, YOLO, Llama…) | Not building | Violates framework-neutrality; the vertical prompts already carry the judgment and the model choice is the user's input |
| Neural architecture search | Deferred | Narrow audience; revisit if `dl_architecture_selection.md` proves insufficient |
| Data mesh / data platform architecture | Deferred to `domain-software-engineering/` | Platform architecture, not ML judgment; `mldata_data_contract_design.md` covers the ML-facing seam |
| Model interpretability library playbooks (SHAP, LIME, Captum) | Not building | `rai_interpretability_analysis.md` and `rai_explainability_plan.md` are method-level and tool-neutral by design |

---

## Authoring Notes for Future Waves

- Keep the no-fabrication and reproducibility clauses; they are the domain's signature.
- Cross-link rather than duplicate. Check [Explicitly not gaps](#explicitly-not-gaps) before proposing anything new.
- Every new prompt needs a non-trivial, ML-specific False-Positive Prevention block — see `field_guide.md` for the catalog of ML failure modes. Reused or generic FPP bullets are the failure mode that quietly degrades this domain; across the current 286 files the most-repeated FPP bullet appears only 4 times, and that bar must hold.
- Follow the house style exactly: the five H2 sections (`Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output`), with `Objective` / `When to Use` / `When NOT to Use` / `Instructions` / `Output Format` as **bold labels**, not headings.
- Filenames must stay ≤55 characters — `scripts/validate_naming_conventions.py` enforces it.
- **Every wave must update four places**, or the domain drifts again: this roadmap, the README Directory Map, the README routing table, and the root `CLAUDE.md` routing block. Waves 6–8 shipped without any of the four and went undocumented for months.
