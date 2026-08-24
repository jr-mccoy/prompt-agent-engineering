---
title: "Infrastructure as Code Review and Analysis"
category: devops
description: "Analyze IaC configurations for security, cost optimization, and cloud-native best practices"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-03
  - DS-06
difficulty: intermediate
tags:
  - infrastructure-as-code
  - iac
  - terraform
  - pulumi
  - cloudformation
  - cloud
updated: "2026-03-19"
---

# Infrastructure as Code Review and Analysis

**Objective:** Analyze Infrastructure as Code (IaC) configurations for security vulnerabilities, cost optimization, reliability patterns, and adherence to cloud-native best practices across Terraform, Pulumi, CloudFormation, and other IaC tools.

**When to Use:** Use this prompt when reviewing IaC pull requests, auditing cloud infrastructure configurations, optimizing cloud costs, preparing for production deployments, or establishing infrastructure standards for your organization.

**Instructions:**

1. **Security Configuration Analysis**
   - Check for overly permissive IAM policies
   - Review network security configurations (security groups, NACLs)
   - Analyze encryption settings (at rest and in transit)
   - Check for public exposure of resources
   - Review secrets management practices
   - Analyze compliance with security frameworks (CIS, SOC2)

2. **State Management Review**
   - Check state backend configuration (remote state, locking)
   - Review state file security and access controls
   - Analyze workspace/environment organization
   - Check for sensitive data in state files
   - Review state migration practices

3. **Module and Code Organization**
   - Analyze module structure and reusability
   - Check for DRY principle adherence
   - Review variable and output organization
   - Analyze naming conventions consistency
   - Check documentation completeness
   - Review versioning practices

4. **Resource Configuration**
   - Check for hardcoded values vs. variables
   - Review resource tagging strategy
   - Analyze resource dependencies and ordering
   - Check for resource lifecycle configurations
   - Review count/for_each usage patterns

5. **Cost Optimization**
   - Identify over-provisioned resources
   - Check for reserved capacity opportunities
   - Review storage tier selections
   - Analyze network egress patterns
   - Check for idle or unused resources
   - Review auto-scaling configurations

6. **Reliability and High Availability**
   - Check for multi-AZ/region deployments
   - Review backup and disaster recovery configurations
   - Analyze fault tolerance patterns
   - Check for proper health checks
   - Review scaling policies

7. **Operational Excellence**
   - Check for monitoring and logging integration
   - Review alerting configurations
   - Analyze CI/CD integration patterns
   - Check for drift detection setup
   - Review change management practices

**Expected Output:** A comprehensive IaC analysis report including:
- Security vulnerability assessment with severity ratings
- Cost optimization recommendations with estimated savings
- Reliability improvement suggestions
- Code quality and maintainability analysis
- Corrected configuration examples
- Architecture recommendations

**Example Output:**

```markdown
## Infrastructure as Code Review Report

### Project: E-commerce Platform Infrastructure

#### Summary
- **Security Score**: 5/10 (Critical issues found)
- **Cost Optimization**: $2,400/month savings identified
- **Reliability Score**: 7/10 (Single AZ deployments)
- **Code Quality**: 6/10 (Inconsistent patterns)

---

### Critical Security Issues

#### Issue 1: Overly Permissive S3 Bucket Policy (CRITICAL)
**File**: modules/storage/main.tf, Line 45
**Problem**: S3 bucket allows public read access

**Current**:
```hcl
resource "aws_s3_bucket_public_access_block" "data" {
  bucket = aws_s3_bucket.data.id

  block_public_acls       = false  # DANGEROUS
  block_public_policy     = false  # DANGEROUS
  ignore_public_acls      = false
  restrict_public_buckets = false
}
```

**Recommended**:
```hcl
resource "aws_s3_bucket_public_access_block" "data" {
  bucket = aws_s3_bucket.data.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "data" {
  bucket = aws_s3_bucket.data.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.s3.arn
    }
    bucket_key_enabled = true
  }
}
```

#### Issue 2: IAM Policy with Wildcard Actions (HIGH)
**File**: modules/iam/main.tf, Line 23
**Problem**: IAM policy grants `*` actions on resources

**Current**:
```hcl
data "aws_iam_policy_document" "lambda_policy" {
  statement {
    effect = "Allow"
    actions = ["*"]  # DANGEROUS
    resources = ["*"]  # DANGEROUS
  }
}
```

**Recommended**:
```hcl
data "aws_iam_policy_document" "lambda_policy" {
  statement {
    effect = "Allow"
    actions = [
      "dynamodb:GetItem",
      "dynamodb:PutItem",
      "dynamodb:UpdateItem",
      "dynamodb:Query"
    ]
    resources = [
      aws_dynamodb_table.orders.arn,
      "${aws_dynamodb_table.orders.arn}/index/*"
    ]
  }

  statement {
    effect = "Allow"
    actions = [
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ]
    resources = [
      "${aws_cloudwatch_log_group.lambda.arn}:*"
    ]
  }
}
```

#### Issue 3: Security Group Allows All Inbound Traffic (HIGH)
**File**: modules/networking/main.tf, Line 67

**Current**:
```hcl
resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Web server security group"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]  # DANGEROUS
  }
}
```

**Recommended**:
```hcl
resource "aws_security_group" "web" {
  name        = "${var.project}-web-sg"
  description = "Web server security group - HTTPS only"
  vpc_id      = aws_vpc.main.id

  tags = local.common_tags
}

resource "aws_security_group_rule" "web_https_ingress" {
  type              = "ingress"
  from_port         = 443
  to_port           = 443
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.web.id
  description       = "HTTPS from internet"
}

resource "aws_security_group_rule" "web_egress" {
  type              = "egress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.web.id
  description       = "Allow all outbound"
}
```

---

### Cost Optimization Recommendations

#### Recommendation 1: Right-Size RDS Instance
**Current**: db.r5.2xlarge ($580/month)
**Recommended**: db.r5.large ($145/month)
**Analysis**: CPU utilization averages 15%, memory 40%
**Savings**: $435/month

```hcl
resource "aws_db_instance" "main" {
  identifier           = "${var.project}-db"
  instance_class       = "db.r5.large"  # Down from db.r5.2xlarge

  # Enable auto-scaling storage
  allocated_storage     = 100
  max_allocated_storage = 500

  # Enable Performance Insights for monitoring
  performance_insights_enabled = true
  performance_insights_retention_period = 7
}
```

#### Recommendation 2: Use Spot Instances for Non-Critical Workloads
**Current**: On-demand instances for batch processing ($800/month)
**Recommended**: Spot instances with fallback ($200/month)
**Savings**: $600/month

```hcl
resource "aws_autoscaling_group" "batch" {
  name                = "${var.project}-batch-asg"
  min_size            = 0
  max_size            = 10
  desired_capacity    = 0
  vpc_zone_identifier = var.private_subnet_ids

  mixed_instances_policy {
    instances_distribution {
      on_demand_base_capacity                  = 0
      on_demand_percentage_above_base_capacity = 0
      spot_allocation_strategy                 = "capacity-optimized"
    }

    launch_template {
      launch_template_specification {
        launch_template_id = aws_launch_template.batch.id
        version            = "$Latest"
      }

      override {
        instance_type = "c5.xlarge"
      }
      override {
        instance_type = "c5a.xlarge"
      }
      override {
        instance_type = "c6i.xlarge"
      }
    }
  }
}
```

#### Recommendation 3: Enable S3 Intelligent Tiering
**Savings**: ~$300/month based on access patterns

```hcl
resource "aws_s3_bucket_intelligent_tiering_configuration" "data" {
  bucket = aws_s3_bucket.data.id
  name   = "EntireBucket"

  tiering {
    access_tier = "DEEP_ARCHIVE_ACCESS"
    days        = 180
  }

  tiering {
    access_tier = "ARCHIVE_ACCESS"
    days        = 90
  }
}
```

---

### Security Checklist

| Check | Status | Severity |
|-------|--------|----------|
| S3 public access blocked | FAIL | Critical |
| IAM least privilege | FAIL | High |
| Security groups restricted | FAIL | High |
| Encryption at rest | WARN | Medium |
| Encryption in transit | PASS | - |
| VPC flow logs enabled | FAIL | Medium |
| CloudTrail enabled | PASS | - |
| Secrets in Secrets Manager | WARN | Medium |
| State file encrypted | PASS | - |
| Remote state locking | PASS | - |

---

### Code Quality Improvements

#### Add Consistent Tagging Strategy
```hcl
# variables.tf
variable "project" {
  description = "Project name for resource naming and tagging"
  type        = string
}

variable "environment" {
  description = "Environment (dev, staging, prod)"
  type        = string
}

variable "owner" {
  description = "Team or individual responsible"
  type        = string
}

# locals.tf
locals {
  common_tags = {
    Project     = var.project
    Environment = var.environment
    Owner       = var.owner
    ManagedBy   = "terraform"
    Repository  = "github.com/org/infra"
  }
}

# Usage in resources
resource "aws_instance" "web" {
  # ... other config

  tags = merge(local.common_tags, {
    Name = "${var.project}-${var.environment}-web"
    Role = "webserver"
  })
}
```

#### Implement Module Structure
```
infrastructure/
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── terraform.tfvars
│   ├── staging/
│   └── prod/
├── modules/
│   ├── networking/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   └── README.md
│   ├── compute/
│   ├── database/
│   └── security/
└── shared/
    └── backend.tf
```

---

### Reliability Improvements

#### Enable Multi-AZ for Database
```hcl
resource "aws_db_instance" "main" {
  identifier     = "${var.project}-db"
  multi_az       = true  # Enable Multi-AZ

  # Enable automated backups
  backup_retention_period = 7
  backup_window          = "03:00-04:00"

  # Enable deletion protection
  deletion_protection = var.environment == "prod"

  # Enable enhanced monitoring
  monitoring_interval = 60
  monitoring_role_arn = aws_iam_role.rds_monitoring.arn
}
```

#### Add Auto Scaling
```hcl
resource "aws_appautoscaling_target" "ecs" {
  max_capacity       = 10
  min_capacity       = 2
  resource_id        = "service/${aws_ecs_cluster.main.name}/${aws_ecs_service.web.name}"
  scalable_dimension = "ecs:service:DesiredCount"
  service_namespace  = "ecs"
}

resource "aws_appautoscaling_policy" "ecs_cpu" {
  name               = "${var.project}-cpu-autoscaling"
  policy_type        = "TargetTrackingScaling"
  resource_id        = aws_appautoscaling_target.ecs.resource_id
  scalable_dimension = aws_appautoscaling_target.ecs.scalable_dimension
  service_namespace  = aws_appautoscaling_target.ecs.service_namespace

  target_tracking_scaling_policy_configuration {
    predefined_metric_specification {
      predefined_metric_type = "ECSServiceAverageCPUUtilization"
    }
    target_value       = 70.0
    scale_in_cooldown  = 300
    scale_out_cooldown = 60
  }
}
```

---

### Total Cost Impact

| Category | Current | Optimized | Monthly Savings |
|----------|---------|-----------|-----------------|
| RDS | $580 | $145 | $435 |
| EC2 Batch | $800 | $200 | $600 |
| S3 Storage | $400 | $100 | $300 |
| NAT Gateway | $300 | $150 | $150 |
| **Total** | **$2,080** | **$595** | **$1,485** |

**Annual Savings: ~$17,820**
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- OC-03 (Markdown Table Specification)
- DS-06 (Prioritization and Severity Guidance)
- DS-02 (Metric Specification)
- RT-05 (Evidence-Based Reasoning)

**Related Prompts:**
- devops_terraform_best_practices.md - For Terraform-specific patterns
- devops_kubernetes_manifest_review.md - For K8s infrastructure
- devops_cicd_pipeline_analysis.md - For IaC deployment automation
- code-analysis/security/security_cloud_infrastructure_analysis.md - For cloud security

**Customization Guide:**
- **For AWS**: Focus on IAM, VPC, and AWS-specific services and best practices
- **For Azure**: Emphasize ARM templates, RBAC, and Azure Policy integration
- **For GCP**: Highlight organization policies, IAM conditions, and GCP-specific patterns
- **For Multi-Cloud**: Add guidance on abstraction layers, provider-agnostic modules
- **For Compliance**: Include CIS benchmarks, SOC2 controls, and audit requirements
