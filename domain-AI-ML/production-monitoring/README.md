# Production Monitoring

What happens after deployment — drift, degradation, retraining triggers, safe rollout and rollback, incident response, and the two fleet-level prompts for organizations running more models than anyone can name.

**16 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- A deployed model is degrading, or you want to know before it does.
- Designing rollout, rollback, or SLOs for a model.
- An ML incident has happened and needs a postmortem.

**Not here:**
- Offline evaluation is the concern — [`../model-evaluation-validation/`](../model-evaluation-validation/README.md).
- The degradation is caused by a feature-pipeline difference — that is train/serve skew; start with the degradation triage prompt, which separates the causes.
- The model is an agent — [`../agentic-ai-systems/aiagent_observability_telemetry_design.md`](../agentic-ai-systems/aiagent_observability_telemetry_design.md).

## Prompts


**Detect**

| Prompt | Use it to |
|---|---|
| [`mlmonitor_drift_detection_design.md`](mlmonitor_drift_detection_design.md) | Design data, concept, and prediction drift detection with explicit reference windows, statistical tests, and alert thresholds — so drift claims are evidenced, not eyeballed. |
| [`mlmonitor_monitoring_dashboard_design.md`](mlmonitor_monitoring_dashboard_design.md) | Design an ML monitoring dashboard: which signals to surface, at what cadence, against which baselines, and with what alert tiers — so operators can tell healthy from degrading at a glance. |
| [`mlmonitor_slo_design_for_ml.md`](mlmonitor_slo_design_for_ml.md) | Define SLIs and SLOs for an ML service across quality, latency, and availability, with error budgets — accounting for delayed labels and the difference between operational health and model correctness. |
| [`mlmonitor_data_pipeline_health_audit.md`](mlmonitor_data_pipeline_health_audit.md) | Audit the production data pipeline feeding a model for silent failures and train-serve skew — nulls, schema drift, stale joins, default-substitution, and timing mismatches that degrade quality without raising errors. |
| [`mlmonitor_feedback_loop_detection.md`](mlmonitor_feedback_loop_detection.md) | Detect and break harmful feedback loops where a model's own outputs contaminate the data it later trains on — runaway bias, popularity collapse, and self-fulfilling labels — with evidence and counterfactual checks. |

**Diagnose and respond**

| Prompt | Use it to |
|---|---|
| [`mlmonitor_performance_degradation_triage.md`](mlmonitor_performance_degradation_triage.md) | Triage a production model whose quality dropped using a decision tree that separates data shift, pipeline/serving bugs, label delay/quality, and genuine concept drift before recommending a fix. |
| [`mlmonitor_ml_incident_response.md`](mlmonitor_ml_incident_response.md) | A decision-tree incident runbook for ML production failures — detect, classify severity, diagnose the ML-specific cause, mitigate or roll back, and run an ML-aware postmortem. |
| [`mlmonitor_incident_postmortem_template.md`](mlmonitor_incident_postmortem_template.md) | A blameless postmortem framework for a resolved ML production incident — reconstructed timeline, quantified impact, ML-specific root cause split across model/data/pipeline/serving, contributing factors, and owned, dated corrective + preventive actions. |
| [`mlmonitor_incident_runbook_library.md`](mlmonitor_incident_runbook_library.md) | Build an indexed library of ML incident runbooks organized by failure-mode class — drift, pipeline failure/skew, feedback-loop contamination, training-pipeline failure, serving/latency bug, label-delay masking — each with detection signals, triage, ML diagnosis decision points, mitigation, and escalation. |
| [`mlmonitor_genai_incident_patterns.md`](mlmonitor_genai_incident_patterns.md) | A catalog of GenAI/LLM-specific production incident patterns with detection + response runbooks — hallucination/factuality spike, prompt-injection/jailbreak, RAG retrieval failure, output-safety violation, latency/timeout, and cost/token runaway — each with signals, immediate containment, diagnosis, and durable fix. |
| [`mlmonitor_cv_incident_patterns.md`](mlmonitor_cv_incident_patterns.md) | A catalog of computer-vision-specific production incident patterns with detection + response — camera/sensor config shift, domain/lighting shift, class/label distribution drift, corrupted or out-of-distribution input, adversarial perturbation, and confidence/calibration collapse — each with signals, containment, diagnosis, and durable fix. |

**Roll out and roll back**

| Prompt | Use it to |
|---|---|
| [`mlmonitor_canary_shadow_deployment.md`](mlmonitor_canary_shadow_deployment.md) | Design canary and shadow deployments to de-risk model releases — what to compare, against which baseline, with what promotion and abort criteria — before a new model takes full traffic. |
| [`mlmonitor_rollback_strategy.md`](mlmonitor_rollback_strategy.md) | Design safe model rollback — version pinning, rollback criteria, automation, and data/feature consistency — so reverting to a prior model is fast, deterministic, and does not reintroduce a worse state. |
| [`mlmonitor_retraining_trigger_strategy.md`](mlmonitor_retraining_trigger_strategy.md) | Decide when to retrain a production model — scheduled vs triggered — and design the triggers, data-readiness gates, and guardrails that prevent retraining on corrupted or under-labeled data. |

**Manage the fleet**

| Prompt | Use it to |
|---|---|
| [`mlmonitor_champion_challenger_design.md`](mlmonitor_champion_challenger_design.md) | Run challenger models against a production champion continuously — deciding what challengers see and whether they act, defining promotion criteria before results arrive, and preventing the multiple-comparisons problem that continuous challenging creates. |
| [`mlmonitor_model_portfolio_health_review.md`](mlmonitor_model_portfolio_health_review.md) | Review every model an organization runs as a portfolio — finding the unowned, unmonitored, and quietly degrading ones, ranking by consequence rather than by attention received, and producing retirement decisions alongside remediation. |

## Conventions

- **Prefix:** `mlmonitor_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/production-monitoring`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.

## What lives elsewhere

- Continuous updating from production feedback → [`../mlops-infrastructure/mlops_online_learning_pipeline_design.md`](../mlops-infrastructure/mlops_online_learning_pipeline_design.md).
- Documentation going stale relative to the deployed model → [`../responsible-ai-governance/rai_documentation_freshness_audit.md`](../responsible-ai-governance/rai_documentation_freshness_audit.md).
