---
title: "DevOps Prompts Workflow Guide"
category: devops
description: "DevOps Prompts Workflow Guide."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: beginner
tags:
  - devops
  - guide
  - workflow
updated: "2026-04-03"
related_prompts: []
artifact_type: "reference"
---

# DevOps Prompts Workflow Guide

**Purpose:** This guide helps you navigate the DevOps category prompts to effectively use AI assistance throughout your infrastructure and deployment workflows.

---

## Quick Reference

| Prompt | Use When |
|--------|----------|
| [devops_dockerfile_optimization.md](devops_dockerfile_optimization.md) | Building or optimizing container images |
| [devops_kubernetes_manifest_review.md](devops_kubernetes_manifest_review.md) | Deploying to Kubernetes, reviewing K8s configs |
| [devops_cicd_pipeline_analysis.md](devops_cicd_pipeline_analysis.md) | Setting up or optimizing CI/CD workflows |
| [devops_infrastructure_as_code_review.md](devops_infrastructure_as_code_review.md) | Reviewing Terraform, CloudFormation, Pulumi |
| [devops_terraform_best_practices.md](devops_terraform_best_practices.md) | Terraform-specific code quality and patterns |
| [devops_helm_chart_review.md](devops_helm_chart_review.md) | Creating or reviewing Helm charts |
| [devops_container_security.md](devops_container_security.md) | Security audits of container environments |
| [devops_monitoring_observability.md](devops_monitoring_observability.md) | Setting up metrics, logging, tracing |
| [devops_gitops_workflow.md](devops_gitops_workflow.md) | Implementing GitOps with ArgoCD/Flux |

---

## Workflow Scenarios

### Scenario 1: New Application Deployment

**Goal:** Deploy a new application to Kubernetes

**Recommended Prompt Order:**

1. **Start with Dockerfile optimization**
   - Use `devops_dockerfile_optimization.md` to create a secure, efficient container image
   - Focus on: multi-stage builds, non-root user, minimal base image

2. **Create Kubernetes manifests**
   - Use `devops_kubernetes_manifest_review.md` to design production-ready K8s configs
   - Focus on: security context, resource limits, probes, PDB

3. **Set up CI/CD pipeline**
   - Use `devops_cicd_pipeline_analysis.md` to create automated build/deploy workflows
   - Focus on: caching, parallel jobs, security scanning

4. **Configure monitoring**
   - Use `devops_monitoring_observability.md` to set up observability
   - Focus on: SLIs/SLOs, dashboards, alerting

### Scenario 2: Infrastructure as Code Project

**Goal:** Set up cloud infrastructure with Terraform

**Recommended Prompt Order:**

1. **Start with IaC review**
   - Use `devops_infrastructure_as_code_review.md` for architecture and security
   - Focus on: IAM policies, network security, encryption

2. **Apply Terraform best practices**
   - Use `devops_terraform_best_practices.md` for code quality
   - Focus on: module structure, state management, variables

3. **Set up CI/CD for infrastructure**
   - Use `devops_cicd_pipeline_analysis.md` for Terraform pipelines
   - Focus on: plan/apply workflows, state locking, drift detection

### Scenario 3: Security Hardening

**Goal:** Improve container and Kubernetes security posture

**Recommended Prompt Order:**

1. **Audit container security**
   - Use `devops_container_security.md` for comprehensive assessment
   - Focus on: CVE scanning, runtime security, compliance

2. **Review Kubernetes configurations**
   - Use `devops_kubernetes_manifest_review.md` for K8s security
   - Focus on: Pod Security Standards, RBAC, network policies

3. **Scan CI/CD for vulnerabilities**
   - Use `devops_cicd_pipeline_analysis.md` for pipeline security
   - Focus on: secret management, dependency scanning, SAST/DAST

### Scenario 4: GitOps Implementation

**Goal:** Implement GitOps for continuous deployment

**Recommended Prompt Order:**

1. **Design GitOps workflow**
   - Use `devops_gitops_workflow.md` for architecture
   - Focus on: repository structure, promotion strategy

2. **Prepare Kubernetes configs**
   - Use `devops_kubernetes_manifest_review.md` for manifest quality
   - Focus on: Kustomize overlays, health checks

3. **Or create Helm charts**
   - Use `devops_helm_chart_review.md` for Helm-based GitOps
   - Focus on: values flexibility, documentation

4. **Set up monitoring**
   - Use `devops_monitoring_observability.md` for deployment observability
   - Focus on: sync status monitoring, deployment metrics

---

## Integration with Other Categories

### DevOps + Code Analysis

| DevOps Prompt | Code Analysis Complement |
|---------------|-------------------------|
| Container Security | `security_owasp_top_10_analysis.md` |
| CI/CD Pipeline | `testing_integration_test_design.md` |
| Monitoring | `performance_analysis.md` |

### DevOps + Testing

| DevOps Prompt | Testing Complement |
|---------------|-------------------|
| CI/CD Pipeline | `testing_e2e_test_scenario_creation.md` |
| Kubernetes Review | `testing_performance_load_test_planning.md` |
| Container Security | `testing_security_testing.md` |

---

## Prompt Selection Decision Tree

```
What are you working on?
│
├─▶ Container Images
│   └─▶ devops_dockerfile_optimization.md
│
├─▶ Kubernetes Deployment
│   ├─▶ Raw manifests? → devops_kubernetes_manifest_review.md
│   └─▶ Helm charts? → devops_helm_chart_review.md
│
├─▶ CI/CD Pipelines
│   └─▶ devops_cicd_pipeline_analysis.md
│
├─▶ Infrastructure
│   ├─▶ General IaC? → devops_infrastructure_as_code_review.md
│   └─▶ Terraform specific? → devops_terraform_best_practices.md
│
├─▶ Security Audit
│   └─▶ devops_container_security.md
│
├─▶ Monitoring/Observability
│   └─▶ devops_monitoring_observability.md
│
└─▶ GitOps Setup
    └─▶ devops_gitops_workflow.md
```

---

## Common Techniques Used

All DevOps prompts leverage these core techniques:

| Technique | Code | Purpose |
|-----------|------|---------|
| Clear Objective Statement | ST-01 | Defines the analysis goal |
| Sequential Instructions | ST-02 | Step-by-step review process |
| Multi-Dimensional Analysis | RT-02 | Security, performance, reliability perspectives |
| Output Templates | ST-03 | Structured, actionable reports |
| Evidence-Based Reasoning | RT-05 | Specific code examples and fixes |
| Prioritization Guidance | DS-06 | Severity ratings for issues |
| Tool Suggestions | DS-03 | Recommended tools and frameworks |

---

## Best Practices for Using DevOps Prompts

### 1. Provide Context

Include relevant details:
- Current technology stack
- Deployment environment (cloud provider, Kubernetes version)
- Existing constraints or requirements
- Security/compliance requirements

### 2. Share Actual Configuration

Paste your actual:
- Dockerfiles
- Kubernetes manifests
- Terraform files
- CI/CD pipeline definitions

### 3. Specify Focus Areas

If you have specific concerns, mention them:
- "Focus on security vulnerabilities"
- "Optimize for build time"
- "Check cost optimization"

### 4. Iterate on Results

Use follow-up prompts to:
- Deep dive into specific findings
- Get implementation help for recommendations
- Validate fixes

---

## Example Usage

### Example 1: Dockerfile Review

```
Please review this Dockerfile for optimization and security issues:

```dockerfile
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "app.py"]
```

Use the Dockerfile optimization prompt to analyze.
```

### Example 2: Kubernetes Security Audit

```
Review these Kubernetes manifests for production readiness:

[Paste deployment.yaml, service.yaml, etc.]

Focus on:
1. Security context configuration
2. Resource management
3. High availability setup
```

### Example 3: CI/CD Optimization

```
Analyze this GitHub Actions workflow for efficiency and security:

[Paste .github/workflows/main.yml]

Current pain points:
- Builds take 15+ minutes
- Occasional flaky tests
- No security scanning
```

---

## Related Resources

- **Testing Category**: For test automation in CI/CD
- **Code Analysis Category**: For code quality gates
- **Security Category**: For application security scanning
- **Performance Category**: For performance testing integration

---

*This guide is part of the DevOps category added on 2025-12-14 to address Finding 4.2 in the Repository Improvement Recommendations.*


## AI Agent Execution Guardrails

These DevOps documents are prompts. For AI coding agents, add operational guardrails to avoid unsafe infra changes:

- Require `plan` output before any manifest/pipeline rewrite.
- Require environment separation (`dev/stage/prod`) in all recommendations.
- Require dry-run commands first (`terraform plan`, `helm template`, `kubectl diff`).
- Require rollback notes with every proposed deployment change.

High-value clause to add to DevOps prompt runs:

```
Do not assume production permissions.
Generate changes for review-only mode first, with dry-run commands and rollback steps.
Flag any recommendation that could cause downtime or secret exposure.
```
