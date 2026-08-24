---
title: "Terraform Best Practices and Code Review"
category: devops
description: "Analyze Terraform configurations for best practices, security, and maintainability"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-03
  - QA-01
difficulty: intermediate
tags:
  - terraform
  - infrastructure-as-code
  - iac
  - aws
  - cloud
  - automation
updated: "2026-03-19"
---

# Terraform Best Practices and Code Review

**Objective:** Analyze Terraform configurations for adherence to best practices, code quality, security, scalability, and maintainability to build robust and manageable infrastructure.

**When to Use:** Use this prompt when writing new Terraform configurations, reviewing Terraform pull requests, refactoring existing infrastructure code, establishing Terraform standards for teams, or preparing Terraform modules for reuse.

**Instructions:**

1. **Code Organization and Structure**
   - Review file organization (main.tf, variables.tf, outputs.tf, locals.tf)
   - Check module structure and composition
   - Analyze workspace vs. directory-based environment separation
   - Review naming conventions consistency
   - Check for proper use of data sources vs. resources

2. **State Management**
   - Check remote backend configuration
   - Review state locking implementation
   - Analyze state file organization (workspaces, separate states)
   - Check for sensitive data exposure in state
   - Review state migration and import practices

3. **Variable and Output Design**
   - Check variable definitions (types, descriptions, defaults, validation)
   - Review output definitions and sensitivity marking
   - Analyze local value usage for computed values
   - Check for proper variable organization
   - Review tfvars file structure

4. **Resource Configuration Patterns**
   - Review use of count vs. for_each
   - Check lifecycle block usage (prevent_destroy, ignore_changes)
   - Analyze depends_on usage (explicit vs. implicit dependencies)
   - Review resource naming patterns
   - Check for proper provider configuration

5. **Module Design**
   - Analyze module input/output interface design
   - Check module versioning practices
   - Review module documentation
   - Analyze module composition patterns
   - Check for circular dependencies

6. **Security Best Practices**
   - Check for hardcoded secrets or sensitive values
   - Review provider credential management
   - Analyze state file access controls
   - Check sensitive output marking
   - Review infrastructure security configurations

7. **Testing and Validation**
   - Check for input validation rules
   - Review precondition and postcondition blocks
   - Analyze check blocks for assertions
   - Review testing strategy (terratest, etc.)
   - Check plan and apply workflows

**Expected Output:** A comprehensive Terraform code review including:
- Code organization recommendations
- Best practice violations with corrections
- Security issues and remediations
- Module design improvements
- Refactored code examples
- Testing recommendations

**Example Output:**

```markdown
## Terraform Code Review Report

### Project: Production Infrastructure

#### Summary
- **Code Quality Score**: 6/10
- **Security Score**: 7/10
- **Maintainability**: 5/10
- **Best Practice Compliance**: 60%

---

### Code Organization Issues

#### Issue 1: All Resources in Single File (HIGH)
**Current Structure**:
```
infrastructure/
└── main.tf (800+ lines)
```

**Recommended Structure**:
```
infrastructure/
├── main.tf           # Provider config, data sources
├── variables.tf      # Input variables
├── outputs.tf        # Output definitions
├── locals.tf         # Local values
├── versions.tf       # Required providers and versions
├── networking.tf     # VPC, subnets, routing
├── compute.tf        # EC2, ECS, Lambda
├── database.tf       # RDS, DynamoDB
├── storage.tf        # S3, EFS
├── security.tf       # IAM, security groups
├── monitoring.tf     # CloudWatch, alarms
└── terraform.tfvars  # Variable values
```

#### Issue 2: Missing Provider Version Constraints (MEDIUM)
**Current**:
```hcl
provider "aws" {
  region = "us-west-2"
}
```

**Recommended** (versions.tf):
```hcl
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.5"
    }
  }

  backend "s3" {
    bucket         = "company-terraform-state"
    key            = "prod/infrastructure.tfstate"
    region         = "us-west-2"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Environment = var.environment
      Project     = var.project
      ManagedBy   = "terraform"
    }
  }
}
```

---

### Variable Design Improvements

#### Issue 3: Missing Variable Validation (MEDIUM)
**Current**:
```hcl
variable "environment" {
  type = string
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}
```

**Recommended**:
```hcl
variable "environment" {
  description = "Deployment environment (dev, staging, prod)"
  type        = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "instance_type" {
  description = "EC2 instance type for web servers"
  type        = string
  default     = "t3.micro"

  validation {
    condition     = can(regex("^t3\\.", var.instance_type))
    error_message = "Instance type must be from the t3 family."
  }
}

variable "allowed_cidr_blocks" {
  description = "CIDR blocks allowed to access the application"
  type        = list(string)
  default     = []

  validation {
    condition = alltrue([
      for cidr in var.allowed_cidr_blocks : can(cidrhost(cidr, 0))
    ])
    error_message = "All values must be valid CIDR blocks."
  }
}
```

---

### Resource Pattern Improvements

#### Issue 4: Using count Instead of for_each (MEDIUM)
**Problem**: count creates resources by index, making additions/removals disruptive

**Current**:
```hcl
variable "subnet_cidrs" {
  default = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
}

resource "aws_subnet" "private" {
  count             = length(var.subnet_cidrs)
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.subnet_cidrs[count.index]
  availability_zone = data.aws_availability_zones.available.names[count.index]
}

# Problem: Removing middle CIDR shifts all subsequent indices
```

**Recommended**:
```hcl
variable "subnets" {
  description = "Map of subnet configurations"
  type = map(object({
    cidr_block        = string
    availability_zone = string
    public            = optional(bool, false)
  }))
  default = {
    "private-a" = {
      cidr_block        = "10.0.1.0/24"
      availability_zone = "us-west-2a"
    }
    "private-b" = {
      cidr_block        = "10.0.2.0/24"
      availability_zone = "us-west-2b"
    }
    "private-c" = {
      cidr_block        = "10.0.3.0/24"
      availability_zone = "us-west-2c"
    }
  }
}

resource "aws_subnet" "private" {
  for_each = var.subnets

  vpc_id            = aws_vpc.main.id
  cidr_block        = each.value.cidr_block
  availability_zone = each.value.availability_zone

  tags = {
    Name = "${var.project}-${each.key}"
  }
}

# Now you can add/remove subnets without affecting others
```

#### Issue 5: Hardcoded Values (MEDIUM)
**Current**:
```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"  # Hardcoded!
  instance_type = "t3.medium"

  tags = {
    Name = "web-server"  # Hardcoded!
  }
}
```

**Recommended**:
```hcl
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = var.instance_type

  tags = {
    Name = "${var.project}-${var.environment}-web"
  }
}
```

---

### Module Design Best Practices

#### Issue 6: Module Interface Design (HIGH)
**Current** (poor encapsulation):
```hcl
# modules/vpc/main.tf
resource "aws_vpc" "main" {
  cidr_block = var.cidr_block
}

# Parent module directly references internal resources
output "vpc" {
  value = aws_vpc.main  # Exposes entire resource!
}
```

**Recommended** (clean interface):
```hcl
# modules/vpc/outputs.tf
output "vpc_id" {
  description = "The ID of the VPC"
  value       = aws_vpc.main.id
}

output "vpc_cidr" {
  description = "The CIDR block of the VPC"
  value       = aws_vpc.main.cidr_block
}

output "private_subnet_ids" {
  description = "List of private subnet IDs"
  value       = [for subnet in aws_subnet.private : subnet.id]
}

output "public_subnet_ids" {
  description = "List of public subnet IDs"
  value       = [for subnet in aws_subnet.public : subnet.id]
}

# Module README.md example
```

```markdown
# VPC Module

Creates a VPC with public and private subnets across multiple AZs.

## Usage

```hcl
module "vpc" {
  source = "./modules/vpc"

  project     = "myapp"
  environment = "prod"
  vpc_cidr    = "10.0.0.0/16"

  availability_zones = ["us-west-2a", "us-west-2b", "us-west-2c"]

  private_subnet_cidrs = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnet_cidrs  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
}
```

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| project | Project name | string | - | yes |
| environment | Environment name | string | - | yes |
| vpc_cidr | CIDR block for VPC | string | - | yes |

## Outputs

| Name | Description |
|------|-------------|
| vpc_id | The ID of the VPC |
| private_subnet_ids | List of private subnet IDs |
```

---

### Security Improvements

#### Issue 7: Sensitive Values Not Marked (HIGH)
**Current**:
```hcl
output "database_password" {
  value = random_password.db.result  # Exposed in console!
}
```

**Recommended**:
```hcl
output "database_password" {
  description = "Generated database password"
  value       = random_password.db.result
  sensitive   = true
}

# Better: Don't output at all, use AWS Secrets Manager
resource "aws_secretsmanager_secret" "db_password" {
  name = "${var.project}-${var.environment}-db-password"
}

resource "aws_secretsmanager_secret_version" "db_password" {
  secret_id     = aws_secretsmanager_secret.db_password.id
  secret_string = random_password.db.result
}

output "database_password_secret_arn" {
  description = "ARN of the secret containing database password"
  value       = aws_secretsmanager_secret.db_password.arn
}
```

---

### Lifecycle and Maintenance

#### Issue 8: Missing Lifecycle Rules (MEDIUM)
**Recommended patterns**:
```hcl
# Prevent accidental deletion of critical resources
resource "aws_db_instance" "main" {
  identifier = "${var.project}-db"
  # ... other config

  lifecycle {
    prevent_destroy = true
  }
}

# Ignore changes managed outside Terraform
resource "aws_autoscaling_group" "web" {
  name = "${var.project}-web-asg"
  # ... other config

  lifecycle {
    ignore_changes = [
      desired_capacity,  # Managed by autoscaling
    ]
  }
}

# Create before destroy for zero-downtime updates
resource "aws_instance" "web" {
  ami = data.aws_ami.amazon_linux.id
  # ... other config

  lifecycle {
    create_before_destroy = true
  }
}
```

---

### Terraform 1.5+ Features to Adopt

#### Check Blocks for Assertions
```hcl
check "health_check" {
  data "http" "api_health" {
    url = "https://${aws_lb.main.dns_name}/health"
  }

  assert {
    condition     = data.http.api_health.status_code == 200
    error_message = "API health check failed after deployment"
  }
}
```

#### Import Blocks (Terraform 1.5+)
```hcl
import {
  to = aws_instance.legacy
  id = "i-1234567890abcdef0"
}

resource "aws_instance" "legacy" {
  ami           = "ami-12345678"
  instance_type = "t3.medium"
  # ... config to match existing
}
```

#### Moved Blocks for Refactoring
```hcl
# When renaming resources
moved {
  from = aws_instance.web
  to   = aws_instance.web_server
}

# When moving to modules
moved {
  from = aws_vpc.main
  to   = module.networking.aws_vpc.main
}
```

---

### Best Practices Checklist

| Practice | Status | Notes |
|----------|--------|-------|
| Remote state backend | PASS | S3 + DynamoDB |
| Provider version constraints | FAIL | Add to versions.tf |
| Variable validation | FAIL | Add validation blocks |
| Sensitive output marking | FAIL | Mark passwords sensitive |
| for_each over count | WARN | Partial adoption |
| Module versioning | FAIL | Use version constraints |
| Consistent naming | WARN | Inconsistent patterns |
| Documentation | FAIL | Missing README files |
| Pre-commit hooks | FAIL | Add terraform fmt/validate |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- OC-03 (Markdown Table Specification)
- RT-05 (Evidence-Based Reasoning)
- DS-03 (Tool and Methodology Suggestions)

**Related Prompts:**
- devops_infrastructure_as_code_review.md - For general IaC patterns
- devops_cicd_pipeline_analysis.md - For Terraform in CI/CD
- devops_kubernetes_manifest_review.md - For K8s integration
- code-analysis/quality/code_quality_analysis.md - For code quality patterns

**Customization Guide:**
- **For AWS**: Include AWS provider features, assume roles, default tags
- **For Azure**: Focus on azurerm provider patterns, service principals
- **For GCP**: Highlight google provider, project/region configurations
- **For OpenTofu**: Note OpenTofu-specific features and compatibility
- **For Enterprise**: Add Terraform Cloud/Enterprise workspace patterns, policy as code
