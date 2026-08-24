# Technique Analysis: terraform-module-library

**Resource Type:** Skill
**Path:** `skills/cloud-infrastructure/terraform-module-library/`
**Date Analyzed:** 2025-12-22
**Category:** Cloud Infrastructure - Infrastructure-as-Code
**Bundled Resources:** 1 reference (aws-modules.md: 64 lines)
**Total Knowledge:** ~314 lines (250 in SKILL.md + 64 in reference)
**Complexity:** 3/5 (Standard IaC module patterns with testing)

---

## Resource Summary

**Purpose:** Enable Claude to build reusable, production-ready Terraform modules for AWS, Azure, and GCP following infrastructure-as-code best practices.

**Key Innovation:** Standard module pattern + input validation + module composition + infrastructure testing

**Architecture:**
- **SKILL.md (250 lines):** Module structure, AWS VPC example, best practices, composition, testing
- **references/aws-modules.md (64 lines):** 7 AWS module patterns, AWS-specific best practices

**Use Case:** When creating infrastructure modules, standardizing cloud provisioning, implementing reusable IaC components, or establishing organizational Terraform standards.

---

## Identified Techniques

### Technique 1: Standard Module Pattern
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Standardized file structure for modules with defined responsibilities per file
- **Example from resource:**
```
module-name/
├── main.tf          # Main resources
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider versions
├── README.md        # Documentation
├── examples/        # Usage examples
└── tests/           # Terratest files
```
- **Maps to existing:** NEW - **DS-68: Standard Module Pattern**
- **Effectiveness:** Consistent structure across all modules enables discoverability. Developers know where to find inputs (variables.tf), outputs (outputs.tf), examples (examples/), tests (tests/). Industry-standard Terraform module layout.

### Technique 2: Input Validation Patterns
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Terraform validation blocks with regex conditions and error messages
- **Example from resource:**
```hcl
variable "cidr_block" {
  description = "CIDR block for VPC"
  type        = string
  validation {
    condition     = can(regex("^([0-9]{1,3}\\.){3}[0-9]{1,3}/[0-9]{1,2}$", var.cidr_block))
    error_message = "CIDR block must be valid IPv4 CIDR notation."
  }
}
```
- **Maps to existing:** NEW - **DS-69: Input Validation Patterns**
- **Effectiveness:** Validates inputs at plan time, not apply time. Prevents invalid configurations. Regex validates format, custom error message provides actionable feedback. Catch errors early (plan) vs late (apply).

### Technique 3: Module Composition Pattern
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Compose modules by passing outputs from one module as inputs to another
- **Example from resource:**
```hcl
module "vpc" {
  source = "../../modules/aws/vpc"
  name   = "production"
}

module "rds" {
  source = "../../modules/aws/rds"

  vpc_id     = module.vpc.vpc_id         # Output → Input
  subnet_ids = module.vpc.private_subnet_ids  # Output → Input
}
```
- **Maps to existing:** NEW - **DS-70: Module Composition Pattern**
- **Effectiveness:** Enables module reuse and composition. VPC module doesn't know about RDS, RDS module doesn't create VPCs. Loosely coupled, highly cohesive. Changes to VPC implementation don't affect RDS module.

### Technique 4: Tag Merging Pattern
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Use merge() function to combine default tags with custom tags
- **Example from resource:**
```hcl
tags = merge(
  {
    Name = var.name
    Tier = "private"
  },
  var.tags
)
```
- **Maps to existing:** NEW - **DS-71: Tag Merging Pattern**
- **Effectiveness:** Ensures consistent tagging while allowing customization. Default tags (Name, Tier) always present, custom tags (var.tags) overlay. User can override defaults by specifying same key in var.tags. Common pattern for organizational tag policies.

### Technique 5: Conditional Resource Creation
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Use count with ternary operator for optional resources
- **Example from resource:**
```hcl
resource "aws_internet_gateway" "main" {
  count  = var.create_internet_gateway ? 1 : 0
  vpc_id = aws_vpc.main.id
}
```
- **Maps to existing:** NEW - **DS-72: Conditional Resource Creation**
- **Effectiveness:** Enables flexible module behavior. Internet Gateway optional based on use case (private VPC doesn't need IGW). count = 0 → resource not created, count = 1 → resource created. Prevents unnecessary resources in production.

### Technique 6: Terratest Integration Pattern
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Infrastructure testing as code using Terratest (Go library)
- **Example from resource:**
```go
func TestVPCModule(t *testing.T) {
    terraformOptions := &terraform.Options{
        TerraformDir: "../examples/complete",
    }

    defer terraform.Destroy(t, terraformOptions)
    terraform.InitAndApply(t, terraformOptions)

    vpcID := terraform.Output(t, terraformOptions, "vpc_id")
    assert.NotEmpty(t, vpcID)
}
```
- **Maps to existing:** NEW - **DS-73: Terratest Integration Pattern**
- **Effectiveness:** Infrastructure testing workflow: Init → Apply → Validate outputs → Destroy. defer ensures cleanup even if test fails. Validates module actually works, not just syntax. Enables CI/CD for infrastructure modules.

### Technique 7: Best Practices Enumeration
- **Category:** DS (Domain-Specific) - EXISTING
- **Pattern:** Numbered lists of IaC best practices
- **Example from resource:**
```markdown
## Best Practices

1. **Use semantic versioning** for modules
2. **Document all variables** with descriptions
3. **Provide examples** in examples/ directory
...
10. **Tag all resources** consistently

## AWS Best Practices

1. Use AWS provider version ~> 5.0
2. Enable encryption by default
...
10. Follow AWS Well-Architected Framework
```
- **Maps to existing:** DS-58 (from previous analyses)
- **Effectiveness:** 10 general best practices + 10 AWS-specific = 20 total. Consolidates Terraform tribal knowledge. Security-focused (encryption, least-privilege, logging).

### Technique 8: Repository Structure Templates
- **Category:** DS (Domain-Specific) - EXISTING
- **Pattern:** Directory tree showing multi-cloud organization
- **Example from resource:**
```
terraform-modules/
├── aws/
│   ├── vpc/
│   ├── eks/
│   └── rds/
├── azure/
│   ├── vnet/
│   └── aks/
└── gcp/
    ├── vpc/
    └── gke/
```
- **Maps to existing:** DS-55 (from gitops-workflow analysis)
- **Effectiveness:** Organized by cloud provider (aws/, azure/, gcp/). Each provider has similar patterns (networking, compute, database). Enables multi-cloud strategy with consistent organization.

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Standard Module Pattern (DS-68)

**Description:** Standardized file structure for reusable modules with defined responsibilities per file, enabling discoverability and consistency.

**Implementation:**
```
module-name/
├── main.tf          # Resource definitions
├── variables.tf     # Input declarations
├── outputs.tf       # Output declarations
├── versions.tf      # Provider version constraints
├── README.md        # Usage documentation
├── examples/        # Usage examples
│   └── complete/
│       ├── main.tf
│       └── variables.tf
└── tests/           # Automated tests
    └── module_test.go
```

**Use case:**
- Terraform modules (official pattern)
- Helm charts (Chart.yaml, values.yaml, templates/)
- CloudFormation modules (template.yaml, parameters.yaml)
- Pulumi components (index.ts, package.json, README.md)

**Why it's novel:** Industry-standard pattern that enables tool ecosystem. Terraform Registry expects this structure. Developers know where to find inputs, outputs, examples. Consistent structure → better discoverability → faster onboarding.

**Proposed category:** DS (Domain-Specific - Infrastructure-as-Code)
**Proposed code:** DS-68

---

### Pattern 2: Input Validation Patterns (DS-69)

**Description:** Validate inputs with regex conditions and actionable error messages at plan time (not runtime).

**Implementation:**
```hcl
variable "input_name" {
  description = "Description"
  type        = string
  validation {
    condition     = can(regex("^pattern$", var.input_name))
    error_message = "Actionable error message with example."
  }
}
```

**Use case:**
- CIDR block validation (IP format)
- Resource naming conventions (kebab-case, max length)
- Enum values (must be one of: dev, staging, prod)
- Version strings (semantic versioning format)

**Why it's novel:** Shift-left validation. Catch errors at plan time (free, fast) vs apply time (costs money, slow). Regex enables format validation. Custom error message guides user to fix. Prevents cascading failures.

**Proposed category:** DS (Domain-Specific - Infrastructure-as-Code)
**Proposed code:** DS-69

---

### Pattern 3: Module Composition Pattern (DS-70)

**Description:** Compose infrastructure by passing outputs from one module as inputs to another, enabling loosely coupled, reusable modules.

**Implementation:**
```hcl
module "foundation" {
  source = "./foundation"
}

module "application" {
  source = "./application"

  # Output from foundation → Input to application
  foundation_id     = module.foundation.id
  foundation_config = module.foundation.config
}
```

**Use case:**
- VPC → EKS (VPC outputs subnet IDs, EKS consumes them)
- Network → Database (Network outputs security groups, Database consumes)
- IAM → Lambda (IAM outputs role ARN, Lambda consumes)
- Foundation → Application (any layered architecture)

**Why it's novel:** Enables separation of concerns. VPC module doesn't know about EKS, EKS module doesn't create VPCs. Changes to VPC implementation don't break EKS module (as long as outputs remain). Loosely coupled → independently testable → reusable.

**Proposed category:** DS (Domain-Specific - Infrastructure-as-Code)
**Proposed code:** DS-70

---

### Pattern 4: Tag Merging Pattern (DS-71)

**Description:** Use merge() function to combine default tags (required for compliance) with custom tags (user-specified), ensuring consistent tagging.

**Implementation:**
```hcl
tags = merge(
  {
    # Default tags (always present)
    ManagedBy   = "terraform"
    Environment = var.environment
  },
  var.tags  # Custom tags (user can override)
)
```

**Use case:**
- Organizational tag policies (cost center, environment, owner)
- Compliance requirements (data classification, compliance framework)
- Billing tags (project, team, application)
- Security tags (sensitivity, retention)

**Why it's novel:** Ensures compliance while allowing flexibility. Default tags always present (organizational requirements), custom tags add context. User can override defaults by specifying same key. Single pattern handles both required and optional tags.

**Proposed category:** DS (Domain-Specific - Infrastructure-as-Code)
**Proposed code:** DS-71

---

### Pattern 5: Conditional Resource Creation (DS-72)

**Description:** Use count with ternary operator to create resources conditionally based on input variables, enabling flexible module behavior.

**Implementation:**
```hcl
resource "resource_type" "name" {
  count = var.create_resource ? 1 : 0

  # Resource configuration
}
```

**Use case:**
- Optional Internet Gateway (private VPC doesn't need IGW)
- Optional NAT Gateway (public-only VPC doesn't need NAT)
- Optional monitoring (dev: false, prod: true)
- Optional high-availability (single-AZ vs multi-AZ)

**Why it's novel:** Single module supports multiple use cases. Same VPC module creates private VPC (no IGW) or public VPC (with IGW). Prevents code duplication (separate modules for private/public). User controls behavior via variables.

**Proposed category:** DS (Domain-Specific - Infrastructure-as-Code)
**Proposed code:** DS-72

---

### Pattern 6: Terratest Integration Pattern (DS-73)

**Description:** Infrastructure testing as code using Terratest (Go library): Init → Apply → Validate → Destroy.

**Implementation:**
```go
func TestModule(t *testing.T) {
    options := &terraform.Options{TerraformDir: "../examples"}

    defer terraform.Destroy(t, options)       // Cleanup
    terraform.InitAndApply(t, options)        // Deploy

    output := terraform.Output(t, options, "output_name")
    assert.NotEmpty(t, output)                // Validate
}
```

**Use case:**
- Terraform module testing (validate outputs, resource creation)
- Packer image testing (validate AMI attributes)
- Kubernetes manifest testing (validate deployment success)
- Infrastructure validation (end-to-end tests)

**Why it's novel:** Infrastructure as code → Infrastructure testing as code. Automated validation ensures modules work, not just compile. defer ensures cleanup even if test fails. Enables CI/CD for infrastructure modules. Catches regressions before production.

**Proposed category:** DS (Domain-Specific - Infrastructure Testing)
**Proposed code:** DS-73

---

## Multi-Technique Combinations

### Combination 1: Standard Pattern + Validation + Composition (DS-68 + DS-69 + DS-70)

**Pattern:** Standard module structure → Input validation → Module composition

**Example:**
1. Standard module pattern (DS-68): variables.tf, outputs.tf, main.tf
2. Input validation (DS-69): Validate CIDR blocks, naming conventions
3. Module composition (DS-70): VPC module → RDS module

**Why effective:** Professional module development workflow. Standard structure → predictable layout. Input validation → catch errors early. Module composition → reusable components.

---

### Combination 2: Conditional + Tagging + Best Practices (DS-72 + DS-71 + DS-58)

**Pattern:** Conditional resources → Consistent tagging → Best practices compliance

**Example:**
1. Conditional creation (DS-72): Optional IGW based on VPC type
2. Tag merging (DS-71): Required tags + custom tags
3. Best practices (DS-58): "Tag all resources consistently"

**Why effective:** Flexible modules that follow standards. Conditional resources → cost optimization. Tag merging → compliance. Best practices → production readiness.

---

### Combination 3: Testing + Examples (DS-73 + DS-68)

**Pattern:** Terratest integration → Examples directory

**Example:**
1. Examples directory (DS-68): examples/complete/main.tf
2. Terratest (DS-73): tests/module_test.go uses examples/complete

**Why effective:** Examples serve dual purpose: documentation for users + test fixtures for CI. Single source of truth.

---

## Integration Notes

### For MASTER_TECHNIQUE_INDEX.md

**6 new techniques to add:**

1. **DS-68: Standard Module Pattern** - Standardized file structure for reusable modules
2. **DS-69: Input Validation Patterns** - Validate inputs with regex and error messages
3. **DS-70: Module Composition Pattern** - Compose modules by passing outputs as inputs
4. **DS-71: Tag Merging Pattern** - Combine default tags with custom tags
5. **DS-72: Conditional Resource Creation** - Use count/for_each for optional resources
6. **DS-73: Terratest Integration Pattern** - Infrastructure testing as code

### For USE_CASE_LOOKUP.md

**Add to existing sections:**

**"Infrastructure-as-Code":**
- DS-68: Standard Module Pattern (Terraform, Helm, CloudFormation module structure)
- DS-69: Input Validation (validate variables at plan time)
- DS-70: Module Composition (compose infrastructure from reusable modules)
- DS-71: Tag Merging (ensure consistent resource tagging)
- DS-72: Conditional Resource Creation (flexible module behavior)
- DS-73: Terratest Integration (automated infrastructure testing)

### Key Insight: Production-Ready IaC Pattern

**Observation:** This skill demonstrates **production-ready IaC** pattern:

1. **Standard structure** (DS-68) → Predictable organization
2. **Input validation** (DS-69) → Fail fast at plan time
3. **Module composition** (DS-70) → Reusable components
4. **Tag merging** (DS-71) → Compliance and flexibility
5. **Conditional creation** (DS-72) → Cost optimization
6. **Automated testing** (DS-73) → Quality assurance

**Design principle:** Modules should be reusable, testable, and production-ready out of the box.

**Comparison:**
- **Quick scripts:** No structure, no validation, no tests → works once, breaks in production
- **Production modules:** Standard structure, input validation, automated tests → works reliably across environments

---

## Summary

**terraform-module-library** demonstrates **production-ready Infrastructure-as-Code** using:
- Standard module pattern (consistent file structure)
- Input validation (fail fast with actionable errors)
- Module composition (loosely coupled, reusable components)
- Tag merging (compliance + flexibility)
- Conditional resources (cost optimization)
- Terratest integration (automated testing)
- Best practices enumeration (20 IaC practices)

**Novel contribution:** Shows how to create **enterprise-grade Terraform modules** with testing and validation.

**Key metrics:**
- **Module patterns:** 7 AWS modules (VPC, EKS, RDS, S3, ALB, Lambda, Security Group)
- **Best practices:** 20 (10 general + 10 AWS-specific)
- **Testing:** Terratest integration with Go
- **Validation:** Regex-based input validation
- **Total knowledge:** ~314 lines (concise IaC guide)

**Recommended applications:**
- Terraform module libraries
- CloudFormation template libraries
- Pulumi component libraries
- Helm chart repositories
- Any Infrastructure-as-Code standardization

---

## Analysis Metadata

- **Analyzer:** Claude (Task 2.2 Priority 2)
- **Review Status:** Complete
- **Priority:** High (Infrastructure-as-Code, enterprise patterns)
- **Recommended for MASTER_TECHNIQUE_INDEX:** Yes (6 novel techniques)
- **Integration Complexity:** Low (well-established IaC patterns)
