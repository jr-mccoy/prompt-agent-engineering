# Code Analysis Prompts

Comprehensive prompts for analyzing codebases across security, quality, performance, architecture, evolution, and database dimensions.

**Total Prompts:** 44

---

## Subcategories

| Subcategory | Prompts | Purpose |
|-------------|---------|---------|
| [Security](security/) | 14 | Vulnerability detection, compliance, threat modeling |
| [Architecture](architecture/) | 9 | Design patterns, layers, coupling analysis |
| [Quality](quality/) | 7 | Code complexity, duplication, documentation |
| [Performance](performance/) | 7 | Bottlenecks, optimization, scalability |
| [Evolution](evolution/) | 6 | Technical debt, refactoring, code churn |
| [Database](database/) | 1 | Schema and query analysis |

---

## Security (14 prompts)

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
| `security_stride_threat_modeling.md` | STRIDE threat modeling exercise |

---

## Architecture (9 prompts)

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

---

## Quality (7 prompts)

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

---

## Performance (7 prompts)

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

## Database (1 prompt)

Analyze database design and queries.

| Prompt | When to Use |
|--------|-------------|
| `database_comprehensive_analysis.md` | Full database analysis (schema, queries, performance) |

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
