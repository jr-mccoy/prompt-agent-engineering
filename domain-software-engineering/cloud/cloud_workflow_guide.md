---
title: "Cloud Infrastructure Workflow Guide"
category: cloud
description: "Cloud Infrastructure Workflow Guide."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: beginner
tags:
  - cloud
  - guide
  - workflow
updated: "2026-03-19"
related_prompts: []
artifact_type: "reference"
---

# Cloud Infrastructure Workflow Guide

This guide provides recommended workflows for using the cloud-specific prompts in this directory. It covers common scenarios and suggests the optimal sequence of prompts for comprehensive cloud infrastructure management.

---

## Overview of Available Prompts

| Prompt | Purpose | Primary Use Case |
|--------|---------|------------------|
| `cloud_aws_architecture_review.md` | AWS Well-Architected Framework analysis | AWS infrastructure review |
| `cloud_azure_best_practices.md` | Azure Well-Architected Framework analysis | Azure infrastructure review |
| `cloud_gcp_best_practices.md` | GCP best practices analysis | GCP infrastructure review |
| `cloud_cost_optimization.md` | Cross-cloud cost reduction strategies | FinOps and cost management |
| `cloud_serverless_function_analysis.md` | Serverless optimization | Lambda, Functions, Cloud Functions |
| `cloud_security_review.md` | Security and compliance assessment | Security audits, compliance |

---

## Workflow 1: New Cloud Architecture Design

**Scenario**: Starting a new cloud project or major architectural change

**Recommended Sequence**:

```
1. cloud_aws_architecture_review.md (or Azure/GCP equivalent)
   └── Understand Well-Architected Framework requirements

2. cloud_security_review.md
   └── Design security controls from the start

3. cloud_cost_optimization.md
   └── Plan for cost efficiency before deployment

4. cloud_serverless_function_analysis.md (if applicable)
   └── Optimize serverless components
```

**Key Considerations**:
- Start with architecture patterns before implementation
- Security should be designed in, not bolted on
- Consider cost implications early to avoid surprises

---

## Workflow 2: Cloud Cost Audit

**Scenario**: Monthly or quarterly cost review, budget optimization

**Recommended Sequence**:

```
1. cloud_cost_optimization.md
   └── Comprehensive cost analysis and quick wins

2. cloud_serverless_function_analysis.md
   └── Memory right-sizing and cold start optimization

3. cloud_aws_architecture_review.md (Cost Optimization Pillar)
   └── Reserved Instance and Savings Plan recommendations
```

**Quick Wins to Look For**:
- Idle resources (unattached volumes, stopped instances)
- Oversized instances (CPU/memory utilization < 30%)
- Missing commitment discounts (Reserved Instances, Savings Plans)
- Storage without lifecycle policies
- Cross-AZ/region data transfer

---

## Workflow 3: Security and Compliance Audit

**Scenario**: Preparing for SOC2, HIPAA, PCI-DSS, or security review

**Recommended Sequence**:

```
1. cloud_security_review.md
   └── Comprehensive security assessment
   └── Compliance gap analysis

2. cloud_aws_architecture_review.md (Security Pillar)
   └── AWS-specific security best practices

3. devops/devops_container_security.md
   └── Container and Kubernetes security (if applicable)
```

**Compliance Framework Coverage**:
| Framework | Primary Prompt | Supporting Prompts |
|-----------|---------------|-------------------|
| SOC2 | cloud_security_review.md | All architecture reviews |
| HIPAA | cloud_security_review.md | + data protection focus |
| PCI-DSS | cloud_security_review.md | + network segmentation |
| GDPR | cloud_security_review.md | + data residency |
| CIS Benchmarks | cloud_security_review.md | Provider-specific reviews |

---

## Workflow 4: Cloud Migration Assessment

**Scenario**: Migrating from on-premises or between cloud providers

**Recommended Sequence**:

```
1. Source Assessment
   └── Document current architecture and dependencies

2. cloud_aws_architecture_review.md (or target cloud)
   └── Understand target cloud best practices

3. cloud_cost_optimization.md
   └── Project costs and optimize for target

4. cloud_security_review.md
   └── Ensure security posture in new environment

5. cloud_serverless_function_analysis.md
   └── Modernization opportunities
```

**Migration Considerations**:
- Service mapping between clouds
- Data transfer strategies
- Compliance requirements in new region
- Training and operational readiness

---

## Workflow 5: Serverless Application Optimization

**Scenario**: Optimizing Lambda, Azure Functions, or Cloud Functions

**Recommended Sequence**:

```
1. cloud_serverless_function_analysis.md
   └── Performance and cost optimization
   └── Cold start mitigation

2. cloud_cost_optimization.md (Compute section)
   └── Compare serverless vs container vs VM costs

3. cloud_security_review.md (IAM section)
   └── Function permission review
```

**Key Metrics to Track**:
- Cold start frequency and duration
- Memory utilization vs allocation
- Invocation patterns and concurrency
- Cost per invocation

---

## Workflow 6: Reliability and Disaster Recovery

**Scenario**: Improving availability and planning DR

**Recommended Sequence**:

```
1. cloud_aws_architecture_review.md (Reliability Pillar)
   └── HA configurations and DR strategies

2. cloud_security_review.md (Data Protection)
   └── Backup security and encryption

3. cloud_cost_optimization.md
   └── Cost-effective DR strategies
```

**Reliability Checklist**:
- [ ] Multi-AZ deployment for stateful services
- [ ] Automated backups with tested restore procedures
- [ ] Health checks and auto-healing
- [ ] Documented RTO/RPO requirements
- [ ] Regular DR drills

---

## Cross-Reference with DevOps Prompts

The cloud prompts work together with DevOps prompts for comprehensive coverage:

| Cloud Prompt | Related DevOps Prompts |
|-------------|----------------------|
| All cloud reviews | `devops_terraform_best_practices.md` |
| cloud_serverless_function_analysis.md | `devops_cicd_pipeline_analysis.md` |
| cloud_security_review.md | `devops_container_security.md` |
| cloud_cost_optimization.md | `devops_monitoring_observability.md` |
| All cloud reviews | `devops_infrastructure_as_code_review.md` |

---

## Multi-Cloud Strategy

For organizations using multiple cloud providers:

**Recommended Approach**:
1. Use provider-specific prompts for detailed analysis
2. Use `cloud_cost_optimization.md` for cross-cloud comparison
3. Use `cloud_security_review.md` for consistent security baseline

**Multi-Cloud Considerations**:
- Consistent tagging and naming conventions
- Unified monitoring and alerting
- Cross-cloud networking (interconnects, VPNs)
- Workload placement optimization
- Disaster recovery across clouds

---

## Quick Reference: When to Use Each Prompt

| Situation | Start With |
|-----------|-----------|
| New AWS project | `cloud_aws_architecture_review.md` |
| Azure migration | `cloud_azure_best_practices.md` |
| GCP optimization | `cloud_gcp_best_practices.md` |
| Cost concerns | `cloud_cost_optimization.md` |
| Lambda performance | `cloud_serverless_function_analysis.md` |
| Security audit | `cloud_security_review.md` |
| Compliance prep | `cloud_security_review.md` |
| Budget planning | `cloud_cost_optimization.md` |
| DR planning | Provider-specific + security |

---

## Techniques Used Across Cloud Prompts

All prompts in this category utilize:
- **ST-01**: Clear Objective Statement
- **ST-02**: Sequential Step-by-Step Instructions
- **RT-02**: Multi-Dimensional Analysis
- **ST-03**: Structured Output Templates
- **DS-01**: Framework Application (Well-Architected, CIS)
- **DS-06**: Prioritization and Severity Guidance
- **RT-05**: Evidence-Based Reasoning

---

## Contributing

When adding new cloud prompts:
1. Follow the established format with all standard sections
2. Include provider-specific best practices
3. Add practical, copy-paste-ready code examples
4. Reference relevant compliance frameworks
5. Cross-reference with related prompts
6. Update this workflow guide

---

*Last Updated: 2026-04-17*
