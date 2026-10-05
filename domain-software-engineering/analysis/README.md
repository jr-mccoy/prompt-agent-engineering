# Code Analysis Prompts

Comprehensive prompts for analyzing codebases across security, quality, performance, architecture, evolution, and database dimensions.

**Total Prompts:** 115

---

## Subcategories

| Subcategory | Prompts | Purpose |
|-------------|---------|---------|
| [Security](security/) | 29 | Vulnerability detection, compliance, threat modeling |
| [Architecture](architecture/) | 27 | Design patterns, layers, coupling analysis |
| [Quality](quality/) | 10 | Code complexity, duplication, documentation |
| [Performance](performance/) | 8 | Bottlenecks, optimization, scalability |
| [Evolution](evolution/) | 6 | Technical debt, refactoring, code churn |
| [Database](database/) | 8 | Schema and query analysis |
| [Business](business/) | 20 | Strategic business analysis frameworks (SWOT, PESTEL, Porter's, canvases) applied to a codebase |
| [Feature Design](feature-design/) | 4 | Task-sorting algorithm design, review, and Kotlin implementation verification |
| [Integration](integration/) | 1 | Cross-system integration validation (Firebase accounts, groups, invites) |
| Top level (`ml_model_evaluation.md`, `repository_analysis_for_improvements.md`) | 2 | ML model evaluation; adaptive-depth repository improvement audit |

---

## Security (29 prompts)

Identify vulnerabilities and ensure security compliance.

| Prompt | When to Use |
|--------|-------------|
| `security_vulnerability_analysis.md` | General security audit of codebase |
| `security_sql_injection_analysis.md` | Database query security review |
| `security_xss_vulnerability_analysis.md` | Frontend/template XSS detection |
| `security_owasp_top_10_analysis.md` | Comprehensive OWASP vulnerability check |
| `security_authentication_authorization_review.md` | Auth system security audit |
| `security_api_testing.md` | API endpoint security testing |
| `security_container_review.md` | Docker/container security audit |
| `security_compliance_analysis.md` | Regulatory compliance (GDPR, HIPAA, SOC2) |
| `security_code_review_checklist.md` | Security-focused code review |
| `security_cryptography_encryption_review.md` | Encryption implementation review |
| `security_dependency_vulnerability_analysis.md` | Third-party dependency CVE check |
| `security_infrastructure_analysis.md` | Infrastructure security posture |
| `security_secret_credential_detection.md` | Hardcoded secrets/credentials scan |
| `security_detection_engineering_review.md` | Detection quality, ATT&CK coverage, alert tuning |
| `security_threat_hunting_plan.md` | Hypothesis-driven threat hunt plan |
| `security_vulnerability_management_program.md` | Risk-based vulnerability management program |
| `security_soc_alert_triage_runbook.md` | Security on-call triage runbook design |
| `security_stride_threat_modeling.md` | STRIDE threat modeling exercise |
| `security_ai_misuse_detection_playbook.md` | Defensive detection playbook for AI-enabled threats and misuse |
| `security_audit_trail_design.md` | Audit trail architecture: event design, tamper-evidence, retention, compliance evidence |
| `security_fedramp_authorization.md` | FedRAMP authorization: controls, SSP, continuous monitoring, ATO preparation |
| `security_gdpr_implementation_guide.md` | GDPR implementation: DSRs, DPIAs, consent management, data mapping, breach response |
| `security_hipaa_software_compliance.md` | Technical HIPAA compliance: PHI handling, ePHI safeguards, audit logging, BAAs |
| `security_industry_regulatory_compliance.md` | Industry regulatory compliance (FINRA, PSD2/SCA, CCPA/CPRA, ADA/Section 508) |
| `security_iso27001_implementation.md` | ISO 27001 ISMS: Annex A controls, risk treatment, SoA, certification preparation |
| `security_llm_application_review.md` | LLM application security: prompt injection, tool-use authorization, RAG poisoning |
| `security_privacy_by_design_architecture.md` | Privacy-by-design architecture: data minimization, purpose limitation, pseudonymization |
| `security_sbom_supply_chain_review.md` | Supply chain posture: SBOM, provenance, signing, SLSA level, dependency confusion |
| `security_soc2_type2_preparation.md` | SOC 2 Type II audit preparation: Trust Service Criteria, evidence, auditor readiness |

---

## Architecture (27 prompts)

Analyze and improve system design.

| Prompt | When to Use |
|--------|-------------|
| `architecture_layer_identification.md` | Map codebase layers and boundaries |
| `architecture_design_pattern_identification.md` | Identify existing design patterns |
| `architecture_coupling_cohesion_analysis.md` | Module dependency analysis |
| `architecture_diagram_generation.md` | Generate architecture diagrams |
| `architecture_database_schema_review.md` | Database design review |
| `architecture_database_schema_documentation.md` | Document existing schema |
| `architecture_api_conformance_check.md` | API contract validation |
| `architecture_api_client_code_generation.md` | Generate API client code |
| `architecture_refactoring_for_design_patterns.md` | Refactor toward patterns |
| `architecture_ai_workflow_architect.md` | Redesign an existing job into an AI-native workflow without changing roles |
| `architecture_config_driven_domain_modeling.md` | Review the config-vs-code boundary in config-driven systems |
| `architecture_context_architecture_ceiling.md` | Bitter Lesson check: would the agentic system scale with a more capable model? |
| `architecture_context_attention_budget.md` | Sort agent information into four tiers to minimize context window size |
| `architecture_context_cache_stability.md` | Audit agentic prompt structure for KV cache reuse |
| `architecture_context_demystifying_memory.md` | Plain-language explainer of how AI agents remember and forget |
| `architecture_context_external_memory.md` | Decide what belongs in the context window versus external storage |
| `architecture_context_failure_reflection.md` | Design a structured failure reflection system for an agent |
| `architecture_context_multi_agent_scope.md` | Decide whether and how to split an agentic system into multiple agents |
| `architecture_context_observability.md` | Design observability for what an agent knows right now, and why |
| `architecture_context_retrieval_trigger.md` | Design explicit signals that cause an agent to load context from memory |
| `architecture_context_state_persistence.md` | Classify agent information by persistence tier and design storage accordingly |
| `architecture_context_summarization_schema.md` | Design a safe summarization schema that preserves agent-critical information |
| `architecture_context_view_compilation.md` | Design the view compilation layer that produces minimal per-step context |
| `architecture_gui_background_computation.md` | Review threading, progress, and cancellation in desktop GUI apps running long computations |
| `architecture_plugin_constraint_system.md` | Review a plugin-based constraint system for extensibility, isolation, and fault tolerance |
| `repo_analysis_improvement_recommendations.md` | Example output of a full repository audit (reference artifact) |
| `system_design_case_studies_comprehensive_guide.md` | Reference compilation of 19 system design case studies |

---

## Quality (10 prompts)

Assess and improve code quality.

| Prompt | When to Use |
|--------|-------------|
| `quality_code_complexity_analysis.md` | Identify complex/hard-to-maintain code |
| `quality_code_duplication_analysis.md` | Find duplicate/similar code blocks |
| `quality_code_style_consistency_analysis.md` | Style and convention audit |
| `quality_code_documentation_coverage_analysis.md` | Documentation gap analysis |
| `quality_documentation_generation.md` | Generate missing documentation |
| `quality_error_analysis.md` | Error handling review |
| `quality_risk_assessment.md` | Code risk evaluation |
| `quality_concurrency_race_condition_audit.md` | Audit code for concurrency correctness defects (races, deadlocks, TOCTOU) |
| `quality_pull_request_diff_review.md` | Review a single PR/diff the way a thoughtful senior engineer would |
| `quality_yaml_configuration_schema_validation.md` | Audit YAML configuration schema validation in config-driven systems |

---

## Performance (8 prompts)

Optimize application performance.

| Prompt | When to Use |
|--------|-------------|
| `performance_bottleneck_identification.md` | Find performance bottlenecks |
| `performance_code_optimization_suggestions.md` | Get optimization recommendations |
| `performance_scalability_analysis.md` | Evaluate scalability limits |
| `performance_concurrency_synchronization_analysis.md` | Thread safety and concurrency review |
| `performance_resource_usage_profiling.md` | Memory/CPU usage analysis |
| `performance_configuration_tuning.md` | Config optimization suggestions |
| `performance_test_scenario_generation.md` | Generate performance test cases |
| `performance_scheduling_algorithm_optimization.md` | Profile and optimize schedule generation performance |

---

## Evolution (6 prompts)

Manage codebase evolution and technical debt.

| Prompt | When to Use |
|--------|-------------|
| `evolution_technical_debt_estimation.md` | Quantify technical debt |
| `evolution_code_churn_hotspot_analysis.md` | Find frequently-changed code |
| `evolution_refactoring_recommendation_generation.md` | Get refactoring suggestions |
| `evolution_impact_analysis_of_code_changes.md` | Assess change impact |
| `evolution_code_evolution_report_generation.md` | Generate evolution report |
| `evolution_codebase_evolution_visualization.md` | Visualize codebase history |

---

## Database (8 prompts)

Analyze database design and queries.

| Prompt | When to Use |
|--------|-------------|
| `database_comprehensive_analysis.md` | Full database analysis (schema, queries, performance) |
| `database_data_modeling_review.md` | Review data models for correctness, completeness, and business alignment |
| `database_index_optimization.md` | Analyze indexes and recommend an optimal indexing strategy |
| `database_migration_strategy.md` | Plan and review database migration strategies |
| `database_performance_analysis.md` | Database performance: query execution, resource utilization, bottlenecks |
| `database_query_optimization.md` | Analyze SQL queries for performance issues |
| `database_scaling_patterns.md` | Analyze database architecture for scalability and scaling patterns |
| `database_schema_design_normalization.md` | Analyze schema design for normalization issues and redundancy |

---

## Related Categories

- **[Testing](../testing/)** - Test generation and coverage analysis
- **[DevOps](../devops/)** - Infrastructure and deployment review
- **[Improvement](../mobile/android/improvement/)** - Refactoring and enhancement prompts
- **[Engineering](../../domain-agentic-resources/personas/engineering/)** - Development workflow and debugging

---

## Quick Selection Guide

**"My app is slow"** → `performance/performance_bottleneck_identification.md`

**"Is my code secure?"** → `security/security_owasp_top_10_analysis.md`

**"Code is hard to maintain"** → `quality/quality_code_complexity_analysis.md`

**"Need to understand the architecture"** → `architecture/architecture_layer_identification.md`

**"Where's the tech debt?"** → `evolution/evolution_technical_debt_estimation.md`

**"Review database design"** → `architecture/architecture_database_schema_review.md`
