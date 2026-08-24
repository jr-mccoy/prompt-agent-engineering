# Responsible AI & Governance

Fairness, explainability, documentation, privacy engineering, and regulatory assessment. The regulatory prompts share one load-bearing convention: they map a system onto a framework's *structure*, the user confirms the classification, and no article text, threshold, or citation is asserted from memory.

**25 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- A fairness, privacy, or explainability question needs an evidenced answer.
- A regulatory framework applies and you need a structured pre-assessment for legal review.
- Model documentation exists but nobody knows whether it still describes the deployed model.

**Not here:**
- The attack surface rather than the obligation is the concern — [`../model-security/`](../model-security/README.md).
- You need statutory interpretation, article text, or a legal opinion → `domain-legal/`; these prompts prepare material for that review and never substitute for it.
- The question is regulated-finance model validation and capital treatment → `domain-finance/`.

## Prompts


**Fairness**

| Prompt | Use it to |
|---|---|
| [`rai_bias_detection_audit.md`](rai_bias_detection_audit.md) | Audit a model for disparate performance and outcomes across protected and relevant groups using slice-level and intersectional evidence tied to a stated fairness definition. |
| [`rai_fairness_metric_selection.md`](rai_fairness_metric_selection.md) | Choose a defensible fairness definition and metric for a specific decision context, surfacing the mathematical impossibility tradeoffs between competing criteria. |
| [`rai_fairness_mitigation_strategy.md`](rai_fairness_mitigation_strategy.md) | Choose a pre-, in-, or post-processing bias mitigation under a stated fairness definition, and measure its accuracy-fairness tradeoff with slice-level evidence rather than asserting it worked. |

**Explainability**

| Prompt | Use it to |
|---|---|
| [`rai_explainability_plan.md`](rai_explainability_plan.md) | Plan model explanations matched to audience and decision stakes — choosing among SHAP, LIME, counterfactuals, and surrogate models — while respecting the known limits and instability of post-hoc methods. |
| [`rai_interpretability_analysis.md`](rai_interpretability_analysis.md) | Analyze and validate a model's internal and global behavior — what it has actually learned — while distinguishing genuine interpretability from unstable post-hoc artifacts and predictive-vs-causal claims. |

**Documentation**

| Prompt | Use it to |
|---|---|
| [`rai_model_card_authoring.md`](rai_model_card_authoring.md) | Author a complete, honest Model Card — intended use, training data, per-group performance, limitations, and ethical considerations — without inflating metrics or inventing evaluation results. |
| [`rai_documentation_suite_orchestrator.md`](rai_documentation_suite_orchestrator.md) | Orchestrate the full model documentation bundle — model card, dataset datasheet, risk register, and evaluation report — into one coherent, cross-referenced suite with a single source of truth so shared facts never diverge across documents. |
| [`rai_documentation_freshness_audit.md`](rai_documentation_freshness_audit.md) | Audit an existing documentation suite for staleness and drift against the currently deployed model and data — detecting stale metrics, superseded versions, changed data composition, expired reviews, and claims monitoring now contradicts — and emit a per-claim freshness verdict and refresh work-queue. |

**Governance and risk**

| Prompt | Use it to |
|---|---|
| [`rai_governance_framework_design.md`](rai_governance_framework_design.md) | Design an AI governance framework — risk tiers, roles, review gates, and required documentation — proportionate to harm, without inventing regulatory obligations or adopting checkbox theater. |
| [`rai_ethics_review_protocol.md`](rai_ethics_review_protocol.md) | Design an ethics review protocol for an AI project — stakeholder impact, consent, recourse, and oversight — that produces accountable decisions rather than a values-statement rubber stamp. |
| [`rai_model_risk_assessment.md`](rai_model_risk_assessment.md) | Assess an AI model's risk by enumerating failure modes, scoring harm severity × likelihood, identifying affected populations, and mapping controls — grounded in evidence rather than speculative or aggregate reassurance. |
| [`rai_model_risk_register.md`](rai_model_risk_register.md) | Author and maintain a living model risk register — structured risk entries with severity, likelihood, controls, residual risk, owner, and review cadence — kept current across model and data changes rather than produced once and abandoned. |
| [`rai_red_teaming_plan.md`](rai_red_teaming_plan.md) | Design a red-teaming plan for an AI system — threat model, attack categories, coverage, and reporting — that measures real failure modes rather than producing anecdotes, and pairs findings with severity and reproducibility. |

**Privacy engineering**

| Prompt | Use it to |
|---|---|
| [`rai_privacy_technique_selection.md`](rai_privacy_technique_selection.md) | Choose among anonymization, synthetic data, differential privacy, federated learning, and access control by first naming the specific disclosure each is meant to prevent, then matching techniques to threats rather than assembling a portfolio of privacy-sounding controls. |
| [`rai_privacy_pii_assessment.md`](rai_privacy_pii_assessment.md) | Assess an ML system's privacy risk — PII exposure, membership inference, and memorization — and select proportionate mitigations (minimization, differential privacy) measured against utility, without overclaiming protection. |
| [`rai_differential_privacy_design.md`](rai_differential_privacy_design.md) | Design a differentially private training or release pipeline — fixing the unit of privacy before the budget, accounting composition across every release, pricing the utility cost, and stating what the guarantee does and does not cover. |
| [`rai_federated_learning_governance.md`](rai_federated_learning_governance.md) | Govern a federated learning deployment — settling what federation does and does not protect, who is accountable when no one holds the data, how participant heterogeneity and dropout are handled, and what a malicious or careless participant can do to the shared model. |
| [`rai_machine_unlearning_deletion.md`](rai_machine_unlearning_deletion.md) | Design how a deletion request propagates into trained models — separating deleting the record from removing its influence, choosing between retraining, approximate unlearning, and containment, and stating precisely what was and was not achieved. |

**Regulatory assessment**

| Prompt | Use it to |
|---|---|
| [`rai_eu_ai_act_compliance_assessment.md`](rai_eu_ai_act_compliance_assessment.md) | Assess an AI system against the EU AI Act's risk-based structure and obligations, with the user confirming the classification and without inventing article text or specific legal thresholds. |
| [`rai_nist_ai_rmf_assessment.md`](rai_nist_ai_rmf_assessment.md) | Assess an AI system against the NIST AI Risk Management Framework's four functions — GOVERN, MAP, MEASURE, MANAGE — producing a function-by-function maturity gap assessment with evidence, gaps, and prioritized actions, without inventing category identifiers or normative thresholds. |
| [`rai_fda_samd_compliance_assessment.md`](rai_fda_samd_compliance_assessment.md) | Assess an AI/ML-based Software-as-a-Medical-Device against FDA framework concepts — intended use/indications, risk categorization, Good Machine Learning Practice principles, and a Predetermined Change Control Plan for adaptive models — producing a readiness assessment and documentation gaps without inventing guidance numbers, clearance pathways, or thresholds. |
| [`rai_fair_lending_ecoa_assessment.md`](rai_fair_lending_ecoa_assessment.md) | Assess a credit/lending model for fair-lending risk under ECOA / Regulation B concepts — prohibited-basis disparate treatment vs disparate impact, adverse-action reason generation, and a less-discriminatory-alternative search — without inventing statutory cites, dollar thresholds, or enforcement figures. |
| [`rai_gdpr_automated_decisioning_assessment.md`](rai_gdpr_automated_decisioning_assessment.md) | Assess an automated decision-making/profiling system against GDPR Article 22 concepts — whether a decision is solely automated with legal/significant effect, lawful basis, safeguards, meaningful-information/explanation obligations, and data-subject rights — without inventing article numbers beyond Art. 22, fine amounts, or recital text. |
| [`rai_model_risk_management_sr1107.md`](rai_model_risk_management_sr1107.md) | Assess a model's governance against banking Model Risk Management principles — robust development/implementation/use, effective validation with independent effective challenge, and sound governance/policies/controls, plus model inventory and ongoing monitoring — without inventing regulatory citations, capital figures, or deadlines. |

**Sustainability**

| Prompt | Use it to |
|---|---|
| [`rai_sustainability_carbon_assessment.md`](rai_sustainability_carbon_assessment.md) | Estimate and reduce the compute and carbon footprint of training and serving an ML system using measured inputs and stated assumptions, never invented energy or emissions figures. |

## Conventions

- **Prefix:** `rai_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/responsible-ai-governance`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.
- **Regulatory anti-fabrication is load-bearing:** no article number, statutory text, date, or numeric threshold is asserted from memory. The user confirms classification and version; specifics are flagged "verify against the current official source". These are structured pre-assessments, not legal opinions.
- **Privacy claims state their unit** — record, user, group, or organization — because a guarantee at the wrong unit protects nobody.

## What lives elsewhere

- Model-side attacks and defenses → [`../model-security/`](../model-security/README.md).
- Agent privacy and data governance → [`../agentic-ai-systems/aiagent_privacy_data_governance.md`](../agentic-ai-systems/aiagent_privacy_data_governance.md).
- Fleet-level ownership and monitoring coverage → [`../production-monitoring/mlmonitor_model_portfolio_health_review.md`](../production-monitoring/mlmonitor_model_portfolio_health_review.md).
