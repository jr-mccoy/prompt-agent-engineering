---
title: "AWS Architecture Review and Best Practices Analysis"
category: cloud
description: "AWS Architecture Review and Best Practices Analysis"
tags:
  - cloud
  - review
updated: "2026-03-19"
---

# AWS Architecture Review and Best Practices Analysis

**Objective:** Analyze AWS infrastructure configurations for adherence to the AWS Well-Architected Framework, identifying opportunities for improvement across operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

**When to Use:** Use this prompt when designing new AWS architectures, reviewing existing deployments, preparing for AWS Well-Architected reviews, optimizing cloud infrastructure, or conducting cloud migration assessments.

**Instructions:**

1. **Analyze Architecture Overview**
   - Review the overall AWS architecture and service composition
   - Identify the workload type (web application, data processing, ML/AI, etc.)
   - Map out service dependencies and data flows
   - Document multi-region or multi-AZ configurations
   - Assess alignment with AWS reference architectures

2. **Operational Excellence Pillar Review**
   - Evaluate Infrastructure as Code (IaC) implementation (CloudFormation, CDK, Terraform)
   - Check for automated deployment pipelines and CI/CD integration
   - Review monitoring and observability setup (CloudWatch, X-Ray, CloudTrail)
   - Assess runbook and playbook documentation
   - Verify operational event response procedures

3. **Security Pillar Review**
   - Analyze IAM policies for least privilege principle
   - Review VPC configurations (security groups, NACLs, subnets)
   - Check encryption at rest and in transit configurations
   - Evaluate secrets management (Secrets Manager, Parameter Store)
   - Assess compliance posture (Config rules, Security Hub findings)
   - Review network security (WAF, Shield, GuardDuty)

4. **Reliability Pillar Review**
   - Evaluate high availability configurations across AZs/regions
   - Review auto-scaling policies and capacity planning
   - Assess backup and disaster recovery strategies
   - Check fault isolation and failure recovery mechanisms
   - Analyze service quotas and limit management
   - Review health checks and self-healing capabilities

5. **Performance Efficiency Pillar Review**
   - Analyze compute resource sizing and selection
   - Review database configurations and query patterns
   - Evaluate caching strategies (ElastiCache, CloudFront, DAX)
   - Assess storage tier selection and performance
   - Check network optimization (VPC endpoints, Transit Gateway)
   - Review serverless vs. container vs. EC2 decisions

6. **Cost Optimization Pillar Review**
   - Analyze resource utilization and right-sizing opportunities
   - Review Reserved Instance and Savings Plan coverage
   - Identify unused or underutilized resources
   - Evaluate data transfer costs and optimization
   - Check for cost allocation tags and tracking
   - Assess Spot Instance opportunities

7. **Sustainability Pillar Review**
   - Evaluate compute efficiency and utilization rates
   - Review storage lifecycle policies
   - Assess region selection for carbon footprint
   - Check for efficient data processing patterns
   - Identify opportunities for serverless migration

8. **AWS Service-Specific Analysis**
   - EC2: Instance types, AMI management, placement groups
   - RDS/Aurora: Multi-AZ, read replicas, parameter groups
   - S3: Bucket policies, lifecycle rules, intelligent tiering
   - Lambda: Memory/timeout optimization, cold starts, concurrency
   - ECS/EKS: Task definitions, node groups, service mesh
   - API Gateway: Caching, throttling, authorization

**Expected Output:** A comprehensive AWS architecture review report including:
- Executive summary with overall architecture health score
- Pillar-by-pillar analysis with specific findings
- Risk assessment with severity ratings (Critical/High/Medium/Low)
- Prioritized recommendations with implementation guidance
- Cost impact estimates for suggested optimizations
- Architecture diagrams showing current and recommended states

**Example Output:**

```markdown
## AWS Architecture Review Report

### Executive Summary
- **Overall Health Score**: 72/100 (Good with improvement areas)
- **Critical Issues**: 2
- **High Priority**: 5
- **Medium Priority**: 8
- **Estimated Monthly Savings**: $3,400-$4,800

### Architecture Overview
**Workload Type**: E-commerce web application
**Primary Region**: us-east-1
**Multi-AZ**: Partial (compute yes, database no)
**Services Used**: EC2, ALB, RDS MySQL, ElastiCache, S3, CloudFront

```
┌─────────────────────────────────────────────────────────┐
│                     CloudFront                          │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────┐
│                    Route 53                             │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────┐
│              Application Load Balancer                  │
│                   (us-east-1)                           │
└──────────┬─────────────────────────────┬────────────────┘
           │                             │
    ┌──────▼──────┐               ┌──────▼──────┐
    │  EC2 (AZ-a) │               │  EC2 (AZ-b) │
    │   t3.large  │               │   t3.large  │
    └──────┬──────┘               └──────┬──────┘
           │                             │
           └──────────────┬──────────────┘
                          │
           ┌──────────────▼──────────────┐
           │      RDS MySQL (AZ-a)       │
           │      ⚠️ Single-AZ only       │
           └─────────────────────────────┘
```

### Critical Issues

#### Issue 1: Single-AZ Database (CRITICAL)
**Location**: RDS MySQL instance `prod-mysql-primary`
**Risk**: Complete data tier outage if AZ-a fails
**Current Config**:
```hcl
resource "aws_db_instance" "production" {
  identifier           = "prod-mysql-primary"
  instance_class       = "db.r5.large"
  multi_az             = false  # ⚠️ CRITICAL
  storage_encrypted    = true
}
```

**Recommended**:
```hcl
resource "aws_db_instance" "production" {
  identifier           = "prod-mysql-primary"
  instance_class       = "db.r5.large"
  multi_az             = true  # ✅ Enable Multi-AZ
  storage_encrypted    = true
  backup_retention_period = 7
  deletion_protection  = true
}
```
**Impact**: ~$180/month increase, eliminates single point of failure
**Priority**: CRITICAL - Implement within 48 hours

#### Issue 2: Overly Permissive IAM Policy (CRITICAL)
**Location**: IAM Role `app-backend-role`
**Risk**: Potential for privilege escalation and data exfiltration
**Current Policy**:
```json
{
  "Effect": "Allow",
  "Action": "s3:*",
  "Resource": "*"
}
```

**Recommended**:
```json
{
  "Effect": "Allow",
  "Action": [
    "s3:GetObject",
    "s3:PutObject",
    "s3:DeleteObject"
  ],
  "Resource": [
    "arn:aws:s3:::prod-app-assets/*",
    "arn:aws:s3:::prod-user-uploads/*"
  ]
}
```
**Impact**: No cost impact, significantly improved security posture
**Priority**: CRITICAL - Implement immediately

### Pillar Analysis

#### Security Pillar: 65/100
| Check | Status | Notes |
|-------|--------|-------|
| IAM Least Privilege | ⚠️ FAIL | 3 roles with excessive permissions |
| VPC Flow Logs | ⚠️ WARN | Enabled but not analyzed |
| Encryption at Rest | ✅ PASS | All data stores encrypted |
| Encryption in Transit | ✅ PASS | TLS 1.2+ enforced |
| Security Hub | ⚠️ WARN | Not enabled |
| GuardDuty | ✅ PASS | Active with findings review |
| WAF | ⚠️ WARN | Only basic rules configured |

#### Reliability Pillar: 58/100
| Check | Status | Notes |
|-------|--------|-------|
| Multi-AZ Compute | ✅ PASS | ASG spans 2 AZs |
| Multi-AZ Database | ❌ FAIL | Single-AZ RDS |
| Automated Backups | ⚠️ WARN | 1-day retention only |
| DR Strategy | ❌ FAIL | No documented DR plan |
| Health Checks | ✅ PASS | ALB health checks active |
| Auto-Scaling | ⚠️ WARN | Reactive only, no predictive |

#### Cost Optimization Pillar: 70/100
| Check | Status | Notes |
|-------|--------|-------|
| Reserved Instances | ⚠️ WARN | 40% coverage, 60% on-demand |
| Resource Right-Sizing | ⚠️ WARN | 2 instances oversized |
| Unused Resources | ⚠️ WARN | 3 unattached EBS volumes |
| S3 Lifecycle | ❌ FAIL | No lifecycle policies |
| Data Transfer | ✅ PASS | VPC endpoints in place |

### Cost Optimization Opportunities

| Opportunity | Current Cost | Optimized Cost | Monthly Savings |
|-------------|--------------|----------------|-----------------|
| EC2 Right-sizing (t3.large → t3.medium) | $134 | $67 | $67 |
| Reserved Instance coverage (1-year) | $402 | $254 | $148 |
| Delete unattached EBS volumes | $45 | $0 | $45 |
| S3 Intelligent Tiering | $180 | $95 | $85 |
| NAT Gateway optimization | $240 | $180 | $60 |
| **Total** | | | **$405/month** |

### Prioritized Recommendations

| Priority | Recommendation | Effort | Impact | Timeline |
|----------|----------------|--------|--------|----------|
| P0 | Enable RDS Multi-AZ | Low | Critical | 48 hours |
| P0 | Fix IAM overpermissions | Medium | Critical | 1 week |
| P1 | Enable Security Hub | Low | High | 1 week |
| P1 | Implement DR plan | High | High | 2 weeks |
| P2 | Purchase Reserved Instances | Low | Medium | 1 month |
| P2 | Configure S3 lifecycle | Low | Medium | 1 week |
| P3 | Right-size EC2 instances | Medium | Medium | 2 weeks |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- DS-01 (Framework Application - AWS Well-Architected)
- DS-06 (Prioritization and Severity Guidance)
- RT-05 (Evidence-Based Reasoning)

**Related Prompts:**
- cloud_cost_optimization.md - For deeper cost analysis
- cloud_security_review.md - For comprehensive security audit
- devops_terraform_best_practices.md - For IaC improvements
- devops_infrastructure_as_code_review.md - For CloudFormation/CDK review
- code-analysis/security/security_infrastructure_analysis.md - For infrastructure security

**Customization Guide:**
- **For Startups**: Focus on cost optimization and quick wins; consider serverless-first approach
- **For Enterprises**: Emphasize compliance (SOC2, HIPAA), multi-account strategy, and governance
- **For Migration Projects**: Add source architecture comparison, TCO analysis, migration phases
- **For Serverless Architectures**: Focus on Lambda optimization, API Gateway, Step Functions patterns
- **For Data Workloads**: Emphasize S3, Redshift, EMR, Glue configurations and data pipeline patterns
