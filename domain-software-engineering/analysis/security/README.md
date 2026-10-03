# Security Analysis Prompts

> Prompts for identifying security vulnerabilities, reviewing authentication systems, analyzing cryptographic implementations, and ensuring compliance with security standards.

## Prompts in This Category

| Prompt | Description |
|--------|-------------|
| [security_api_testing](security_api_testing.md) | Comprehensive REST and GraphQL API security testing |
| [security_authentication_authorization_review](security_authentication_authorization_review.md) | Review authentication and authorization mechanisms |
| [security_code_review_checklist](security_code_review_checklist.md) | Systematic security-focused code review checklist |
| [security_compliance_analysis](security_compliance_analysis.md) | Analyze compliance with GDPR, SOC2, HIPAA, PCI-DSS |
| [security_container_review](security_container_review.md) | Docker and container security configuration review |
| [security_cryptography_encryption_review](security_cryptography_encryption_review.md) | Review cryptographic implementations and key management |
| [security_dependency_vulnerability_analysis](security_dependency_vulnerability_analysis.md) | Identify CVEs and supply chain risks in dependencies |
| [security_infrastructure_analysis](security_infrastructure_analysis.md) | Analyze Infrastructure as Code and cloud security |
| [security_owasp_top_10_analysis](security_owasp_top_10_analysis.md) | Systematic analysis against OWASP Top 10 vulnerabilities |
| [security_secret_credential_detection](security_secret_credential_detection.md) | Detect hardcoded secrets, API keys, and credentials |
| [security_sql_injection_analysis](security_sql_injection_analysis.md) | Identify SQL injection vulnerabilities and remediation |
| [security_stride_threat_modeling](security_stride_threat_modeling.md) | Apply STRIDE framework for threat modeling |
| [security_vulnerability_analysis](security_vulnerability_analysis.md) | Identify common vulnerabilities (SQLi, XSS, CSRF, auth bypasses) |
| [security_xss_vulnerability_analysis](security_xss_vulnerability_analysis.md) | Identify Cross-Site Scripting (XSS) vulnerabilities |
| [security_llm_application_review](security_llm_application_review.md) | Review LLM-backed apps: prompt injection, jailbreak, tool-use, OWASP LLM Top 10 |
| [security_sbom_supply_chain_review](security_sbom_supply_chain_review.md) | Audit SBOM, supply-chain provenance, SLSA level, dependency confusion |
| [security_detection_engineering_review](security_detection_engineering_review.md) | Review SIEM/EDR detections as code: ATT&CK mapping graded honestly, precision and alert load, replay tests, FP tuning |
| [security_threat_hunting_plan](security_threat_hunting_plan.md) | Plan a bounded, hypothesis-driven hunt: data readiness, queries, stop rule, searched-and-cleared log, hunt → detection |
| [security_vulnerability_management_program](security_vulnerability_management_program.md) | Run vuln management as a program: inventory/ownership, prioritisation by exploitation evidence + exposure, SLAs, exceptions, ungameable metrics |
| [security_soc_alert_triage_runbook](security_soc_alert_triage_runbook.md) | Design triage for an engineering-run security on-call: per-detection runbooks, dispositions, clocks, escalation, queue health |

## Security Operations Boundaries

The four security-operations prompts above are for teams with security engineers. A small organisation without a SOC or security staff should use `../../../domain-risk/risk_security_alert_triage_runbook.md` and `../../../domain-risk/risk_security_incident_response_playbook.md`; model-assisted or autonomous SOC triage is `../../../domain-AI-ML/agentic-ai-systems/aiagent_secops_autonomous_defense.md`.

## Usage

These prompts help analyze codebases for security vulnerabilities, compliance gaps, and best practice violations. Use them during security audits, before deployments, when reviewing third-party code, or as part of secure development lifecycle processes.

## Related Resources

- [Analysis Overview](../README.md) - All analysis categories
- [Software Engineering Domain](../../README.md) - Full domain index
- [DevOps Security](../../devops/README.md) - CI/CD and infrastructure security
