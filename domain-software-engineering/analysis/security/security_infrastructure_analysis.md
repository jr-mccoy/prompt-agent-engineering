---
title: "Infrastructure Security Analysis"
category: code-analysis
description: "Infrastructure Security Analysis"
tags:
  - analysis
  - code-analysis
  - security
updated: "2026-03-19"
---

# Infrastructure Security Analysis

**Objective:** Analyze Infrastructure as Code (IaC), cloud configurations, and infrastructure security posture to identify misconfigurations, security weaknesses, and compliance violations that could lead to data breaches, unauthorized access, or service disruption.

**Instructions:**

1. **Analyze Infrastructure as Code (IaC) Security:**

   **A. Terraform Configuration Security**

   Review Terraform files (.tf) for security issues:

   - [ ] **Resource Configuration:**
     - Check for overly permissive security groups (0.0.0.0/0 inbound)
     - Review IAM policies for excessive permissions
     - Analyze S3 bucket public access configurations
     - Verify encryption at rest enabled
     - Check for public database instances
     - Review default VPC usage (should use custom VPCs)
     - Analyze network ACLs and security group rules

   - [ ] **State File Security:**
     - Verify remote state backend usage (S3, Terraform Cloud)
     - Check state file encryption
     - Review state locking configuration
     - Analyze access controls on state files
     - Verify no sensitive data in state file storage

   - [ ] **Secret Management:**
     - Check for hardcoded secrets in .tf files
     - Review use of variables for sensitive values
     - Verify integration with secret managers (AWS Secrets Manager, Vault)
     - Analyze variable file security (.tfvars)
     - Check for secrets in version control

   - [ ] **Module Security:**
     - Review module sources (official, verified, private)
     - Check module versions (pinning recommended)
     - Analyze third-party module security
     - Verify module input validation

   **B. CloudFormation Security**

   Review CloudFormation templates for security issues:

   - [ ] Template parameter security (no default secrets)
   - [ ] Resource configuration (S3, EC2, RDS, IAM)
   - [ ] Stack policy usage
   - [ ] Drift detection configuration
   - [ ] Output security (no sensitive data exposure)
   - [ ] Change set review process

   **C. Kubernetes Manifests (YAML)**

   Review Kubernetes infrastructure configuration:
   - [ ] Namespace isolation
   - [ ] Resource quotas and limits
   - [ ] NetworkPolicy enforcement
   - [ ] Ingress controller security
   - [ ] Service mesh configuration
   - [ ] Certificate management
   - [ ] Secrets management
   - [ ] RBAC configuration

2. **Analyze Cloud Security Configurations:**

   **A. AWS Security**

   - [ ] **IAM (Identity and Access Management):**
     - Review IAM user, group, role permissions
     - Check for root account usage
     - Verify MFA enabled on all accounts
     - Analyze policy least privilege compliance
     - Check for wildcard permissions (* in policies)
     - Review cross-account access
     - Verify password policy strength
     - Check for unused credentials and access keys

   - [ ] **Network Security:**
     - Review VPC configuration and segmentation
     - Analyze security group rules (inbound/outbound)
     - Check for overly permissive rules (0.0.0.0/0)
     - Verify network ACLs
     - Review NAT gateway configuration
     - Check VPN and Direct Connect security
     - Analyze VPC peering security
     - Review PrivateLink usage

   - [ ] **Storage Security (S3):**
     - Check bucket public access (Block Public Access enabled)
     - Review bucket policies and ACLs
     - Verify encryption at rest (SSE-S3, SSE-KMS)
     - Check versioning enabled
     - Review MFA Delete configuration
     - Analyze access logging
     - Check for secure transport (SSL/TLS) enforcement
     - Review CORS configuration

   - [ ] **Compute Security (EC2, Lambda):**
     - Review EC2 instance metadata service (IMDSv2)
     - Check for public EC2 instances
     - Verify encryption of EBS volumes
     - Review Lambda environment variable encryption
     - Check Lambda execution role permissions
     - Analyze VPC configuration for Lambda
     - Review EC2 security groups

   - [ ] **Database Security (RDS, DynamoDB):**
     - Check for publicly accessible databases
     - Verify encryption at rest
     - Review encryption in transit (SSL/TLS)
     - Check automated backups enabled
     - Review IAM database authentication
     - Analyze database security groups
     - Verify multi-AZ configuration
     - Check deletion protection

   - [ ] **Monitoring and Logging:**
     - Verify CloudTrail enabled in all regions
     - Check CloudTrail log file validation
     - Review CloudWatch logging configuration
     - Analyze VPC Flow Logs
     - Check S3 access logging
     - Verify GuardDuty enabled
     - Review Security Hub findings
     - Check Config rules for compliance

   **B. Azure Security**

   - [ ] **Azure AD and RBAC:**
     - Review role assignments
     - Check conditional access policies
     - Verify MFA enforcement
     - Analyze privileged identity management
     - Review guest user access

   - [ ] **Network Security:**
     - Review Network Security Groups (NSGs)
     - Analyze Application Security Groups
     - Check Azure Firewall configuration
     - Verify DDoS protection
     - Review Virtual Network service endpoints
     - Check Private Link usage

   - [ ] **Storage Security:**
     - Verify storage account encryption
     - Check for public blob access
     - Review shared access signatures (SAS)
     - Analyze firewall and virtual network rules
     - Check secure transfer required

   - [ ] **Key Vault:**
     - Review access policies
     - Check soft delete enabled
     - Verify purge protection
     - Analyze key rotation policies
     - Review networking restrictions

   - [ ] **Monitoring:**
     - Verify Azure Security Center enabled
     - Check Log Analytics configuration
     - Review Azure Monitor alerts
     - Analyze Azure Sentinel deployment

   **C. Google Cloud Platform (GCP) Security**

   - [ ] **IAM and Organization Policies:**
     - Review IAM roles and permissions
     - Check for primitive roles (Owner, Editor, Viewer)
     - Verify service account key management
     - Analyze organization policy constraints
     - Review Cloud Identity

   - [ ] **Network Security:**
     - Review VPC firewall rules
     - Check for 0.0.0.0/0 rules
     - Analyze VPC Service Controls
     - Review Cloud Armor configuration
     - Check Private Google Access

   - [ ] **Storage Security (GCS):**
     - Verify bucket IAM policies
     - Check for public access
     - Review encryption at rest
     - Analyze access logging
     - Check versioning and retention

   - [ ] **Compute Security:**
     - Review Compute Engine instance configurations
     - Check for external IP assignments
     - Verify OS Login enabled
     - Analyze shielded VMs
     - Review service account assignments

   - [ ] **Monitoring:**
     - Verify Cloud Logging enabled
     - Check Security Command Center
     - Review Cloud Monitoring alerts
     - Analyze audit logs

3. **Analyze Infrastructure Security Best Practices:**

   **A. Network Segmentation and Isolation**
   - [ ] Multi-tier architecture (web, app, data layers)
   - [ ] Public vs private subnet separation
   - [ ] DMZ configuration
   - [ ] Jump box/bastion host security
   - [ ] Micro-segmentation implementation

   **B. Encryption**
   - [ ] Encryption at rest for all data stores
   - [ ] Encryption in transit (TLS 1.2+)
   - [ ] Key management and rotation
   - [ ] Certificate management
   - [ ] End-to-end encryption

   **C. Access Control**
   - [ ] Principle of least privilege
   - [ ] Just-in-time access
   - [ ] Role-based access control
   - [ ] Multi-factor authentication
   - [ ] Service account management
   - [ ] API key rotation

   **D. Monitoring and Incident Response**
   - [ ] Centralized logging
   - [ ] SIEM integration
   - [ ] Real-time alerting
   - [ ] Anomaly detection
   - [ ] Incident response runbooks
   - [ ] Security information correlation

   **E. Backup and Disaster Recovery**
   - [ ] Automated backups configured
   - [ ] Backup encryption
   - [ ] Offsite/cross-region backups
   - [ ] Backup restoration testing
   - [ ] Disaster recovery plan
   - [ ] RTO/RPO defined and tested

   **F. Patch Management**
   - [ ] Automated patching for OS
   - [ ] Application update strategy
   - [ ] Vulnerability scanning
   - [ ] Patch testing process
   - [ ] Emergency patching procedures

4. **Analyze Compliance and Governance:**
   - [ ] Tagging strategy for resources
   - [ ] Cost allocation and optimization
   - [ ] Compliance frameworks (CIS benchmarks, NIST)
   - [ ] Policy as code implementation
   - [ ] Configuration drift detection
   - [ ] Automated compliance checking

5. **For each identified issue, provide:**
   - Infrastructure component affected
   - Security issue or misconfiguration
   - Location (file, resource, service)
   - Severity rating (Critical, High, Medium, Low)
   - Exploitation scenario
   - Potential impact (data breach, service disruption, cost)
   - Remediation steps with IaC examples
   - Best practice recommendations
   - Compliance implications

**Expected Output:** A comprehensive infrastructure security analysis including:

- **Executive Summary:**
  - Infrastructure security posture assessment
  - Critical misconfigurations
  - High-risk exposures
  - Compliance status
  - Immediate action items

- **Infrastructure as Code Security:**
  - Terraform/CloudFormation security issues
  - Hardcoded secrets
  - Overly permissive configurations
  - State file security
  - Module security
  - Remediation examples

- **Cloud Configuration Security:**

  **Per Cloud Provider (AWS/Azure/GCP):**
  - IAM and access control issues
  - Network security gaps
  - Storage security misconfigurations
  - Compute security weaknesses
  - Database exposure risks
  - Monitoring and logging gaps
  - Service-specific findings

- **Network Security Assessment:**
  - Network segmentation analysis
  - Firewall rule review
  - Public exposure inventory
  - VPN and connectivity security
  - DDoS protection
  - Recommendations

- **Data Security Assessment:**
  - Encryption at rest status
  - Encryption in transit status
  - Key management
  - Backup security
  - Data classification
  - Recommendations

- **Access Control Assessment:**
  - IAM policy review
  - Privilege escalation risks
  - Service account security
  - MFA coverage
  - Least privilege compliance
  - Recommendations

- **Monitoring and Logging Assessment:**
  - Logging coverage
  - Audit trail completeness
  - Security monitoring tools
  - Alerting configuration
  - SIEM integration
  - Recommendations

- **Remediation Roadmap:**

  **Immediate (Critical):**
  - Close publicly exposed databases/storage
  - Rotate exposed credentials
  - Fix overly permissive IAM policies
  - Enable encryption on unencrypted resources
  - Enable MFA on privileged accounts

  **Short-term (1-3 months):**
  - Implement network segmentation
  - Deploy security monitoring tools
  - Enable comprehensive logging
  - Implement automated compliance checking
  - Conduct vulnerability assessments

  **Medium-term (3-6 months):**
  - Implement policy as code
  - Deploy SIEM solution
  - Enhance backup and DR
  - Implement zero-trust architecture
  - Conduct penetration testing

  **Long-term (6-12 months):**
  - Achieve compliance certifications
  - Implement advanced threat detection
  - Deploy security automation
  - Establish security operations center
  - Continuous compliance monitoring

- **Compliance and Best Practices:**
  - CIS Benchmark compliance
  - Well-Architected Framework alignment
  - Industry-specific compliance (HIPAA, PCI-DSS)
  - Best practice recommendations

**Example Output Format:**

```
CRITICAL: Publicly Accessible RDS Database
Resource: aws_db_instance.production
Location: terraform/database.tf:45
Severity: CRITICAL

Vulnerable Configuration:
  resource "aws_db_instance" "production" {
    identifier           = "prod-db"
    engine              = "postgres"
    instance_class      = "db.t3.medium"
    publicly_accessible = true  # CRITICAL: Should be false
    vpc_security_group_ids = [aws_security_group.db.id]

    username = var.db_username
    password = var.db_password  # Should use AWS Secrets Manager
  }

  resource "aws_security_group" "db" {
    name = "database-sg"

    ingress {
      from_port   = 5432
      to_port     = 5432
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]  # CRITICAL: Open to internet
    }
  }

Issues:
  1. Database is publicly accessible (publicly_accessible = true)
  2. Security group allows access from anywhere (0.0.0.0/0)
  3. Database credentials in code (should use Secrets Manager)
  4. No encryption at rest configured
  5. No backup retention configured

Exploitation Scenario:
  1. Attacker scans for open PostgreSQL ports
  2. Database is accessible from internet
  3. Attacker attempts credential brute-force or exploitation
  4. If successful, full database access achieved
  5. Data exfiltration, modification, or destruction

Impact:
  - Complete database compromise
  - Data breach (PII, sensitive business data)
  - Regulatory violations (GDPR, CCPA)
  - Ransomware risk
  - Estimated incident cost: $500K - $5M

Remediation:
  resource "aws_db_instance" "production" {
    identifier           = "prod-db"
    engine              = "postgres"
    engine_version      = "14.7"
    instance_class      = "db.t3.medium"

    # Security: Not publicly accessible
    publicly_accessible = false

    # Security: Private subnet
    db_subnet_group_name = aws_db_subnet_group.private.name

    # Security: Restricted security group
    vpc_security_group_ids = [aws_security_group.db_private.id]

    # Security: Encryption at rest
    storage_encrypted = true
    kms_key_id       = aws_kms_key.rds.arn

    # Security: Secrets Manager
    username = "admin"
    manage_master_user_password = true

    # Reliability: Backups
    backup_retention_period = 30
    backup_window          = "03:00-04:00"

    # Reliability: Multi-AZ
    multi_az = true

    # Security: Deletion protection
    deletion_protection = true

    # Monitoring
    enabled_cloudwatch_logs_exports = ["postgresql", "upgrade"]
  }

  resource "aws_security_group" "db_private" {
    name   = "database-private-sg"
    vpc_id = aws_vpc.main.id

    # Only allow access from application tier
    ingress {
      from_port       = 5432
      to_port         = 5432
      protocol        = "tcp"
      security_groups = [aws_security_group.app.id]
    }

    egress {
      from_port   = 0
      to_port     = 0
      protocol    = "-1"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

Validation:
  # Check database is not publicly accessible
  aws rds describe-db-instances --db-instance-identifier prod-db \
    --query 'DBInstances[0].PubliclyAccessible'

  # Should return: false

Priority: IMMEDIATE
Timeline: 24 hours
Estimated Effort: 2-4 hours (plus testing)
Responsible: Infrastructure team + Security team approval
```

**Related Prompts:**
- security_container_review.md - Container infrastructure security
- security_compliance_analysis.md - Compliance requirements
- security_dependency_vulnerability_analysis.md - Third-party risk
- architecture_coupling_cohesion_analysis.md - Architecture review

**When to Use:**
Use this prompt when reviewing IaC code, before deploying to production, during security audits, after security incidents, for compliance assessments, during cloud migrations, or as part of regular infrastructure reviews. Essential for securing cloud environments and preventing misconfigurations.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with concise, unambiguous objective
- ST-02 (Structured Sequential Instructions) - Numbered steps with detailed checklists
- DT-02 (Specific Focus Areas with Examples) - Comprehensive checklists per cloud provider
- RT-02 (Multi-Dimensional Analysis Framework) - Component, Issue, Severity, Impact, Remediation structure
- DS-01 (Framework Application) - Applies CIS Benchmarks and Well-Architected Framework
- DS-06 (Prioritization and Severity Guidance) - Severity ratings and remediation timelines
- ST-03 (Output Format Templates) - Detailed example output with code snippets
- AG-05 (Concrete Deliverable Templates) - Full Terraform remediation examples
