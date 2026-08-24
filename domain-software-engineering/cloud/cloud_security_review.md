---
title: "Cloud Security Review and Compliance Analysis"
category: cloud
description: "Comprehensive security assessment of cloud infrastructure identifying vulnerabilities and compliance gaps"
tags:
  - cloud
  - review
  - security
updated: "2026-03-19"
---

# Cloud Security Review and Compliance Analysis

**Objective:** Conduct a comprehensive security assessment of cloud infrastructure across AWS, Azure, or GCP, identifying vulnerabilities, misconfigurations, and compliance gaps while providing remediation guidance aligned with industry frameworks.

**When to Use:** Use this prompt when performing cloud security audits, preparing for compliance assessments (SOC2, HIPAA, PCI-DSS, GDPR), responding to security incidents, or implementing cloud security posture management (CSPM).

**Instructions:**

1. **Identity and Access Management (IAM) Review**
   - Audit user accounts and service principals
   - Review role assignments and permission boundaries
   - Check for overly permissive policies (*, admin access)
   - Evaluate MFA enforcement and conditional access
   - Assess service account key rotation and management
   - Review federation and SSO configurations
   - Check for unused/stale credentials

2. **Network Security Analysis**
   - Review VPC/VNet architecture and segmentation
   - Audit security groups and firewall rules
   - Check for public-facing resources
   - Evaluate private endpoint configurations
   - Assess DDoS protection and WAF rules
   - Review VPN and Direct Connect security
   - Analyze network flow logs

3. **Data Protection Assessment**
   - Verify encryption at rest configurations
   - Check encryption in transit (TLS versions)
   - Review key management (KMS/Key Vault)
   - Assess backup encryption and access controls
   - Evaluate data classification and tagging
   - Check for sensitive data exposure
   - Review data residency compliance

4. **Compute Security Review**
   - Audit VM/instance configurations
   - Check for security agent deployment
   - Review container and Kubernetes security
   - Assess serverless function permissions
   - Evaluate patch management and updates
   - Check for hardening baselines
   - Review secrets in environment variables

5. **Logging and Monitoring Assessment**
   - Verify audit logging enablement
   - Check log retention and integrity
   - Review SIEM integration
   - Assess alerting configurations
   - Evaluate threat detection services
   - Check for security monitoring gaps
   - Review incident response procedures

6. **Compliance Posture Evaluation**
   - Map controls to compliance frameworks
   - Identify compliance gaps and violations
   - Review security benchmark scores
   - Assess regulatory requirements
   - Check for policy exceptions
   - Evaluate governance controls
   - Review audit readiness

7. **Storage Security Analysis**
   - Check bucket/blob public access settings
   - Review access policies and ACLs
   - Verify versioning and MFA delete
   - Assess lifecycle and retention policies
   - Check for sensitive data in storage
   - Review cross-account access
   - Evaluate backup security

8. **Database Security Review**
   - Check network isolation and access controls
   - Review authentication mechanisms
   - Assess encryption configurations
   - Evaluate audit logging
   - Check for public endpoints
   - Review backup security
   - Assess query auditing

**Expected Output:** A comprehensive cloud security assessment including:
- Executive summary with risk rating
- Detailed findings organized by severity
- Compliance gap analysis
- Prioritized remediation roadmap
- Security architecture recommendations
- Compliance checklist and evidence requirements

**Example Output:**

```markdown
## Cloud Security Assessment Report

### Executive Summary

| Metric | Value | Status |
|--------|-------|--------|
| **Overall Risk Rating** | HIGH | 🔴 |
| **Critical Findings** | 4 | Immediate action required |
| **High Findings** | 8 | Address within 1 week |
| **Medium Findings** | 15 | Address within 1 month |
| **Low Findings** | 23 | Address in next quarter |
| **Compliance Score** | 67% | Below target (85%) |

### Risk Distribution by Category

```
Identity & Access    ████████████░░░░ 75% (HIGH risk)
Network Security     ██████████░░░░░░ 62% (CRITICAL risk)
Data Protection      ████████████████ 89% (LOW risk)
Compute Security     ██████████████░░ 78% (MEDIUM risk)
Logging & Monitoring █████████░░░░░░░ 56% (HIGH risk)
Storage Security     ██████████████░░ 71% (MEDIUM risk)
```

### Critical Findings

#### CRITICAL-001: Public S3 Bucket with Sensitive Data
**Resource**: `s3://company-customer-data`
**Region**: us-east-1
**Risk**: Complete data exposure, potential data breach
**Compliance Impact**: GDPR Article 32, SOC2 CC6.1, HIPAA §164.312

**Finding Details**:
```json
{
  "BucketName": "company-customer-data",
  "PublicAccessBlock": {
    "BlockPublicAcls": false,
    "IgnorePublicAcls": false,
    "BlockPublicPolicy": false,
    "RestrictPublicBuckets": false
  },
  "BucketPolicy": {
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::company-customer-data/*"
  },
  "SensitiveDataFound": ["PII", "Financial Records", "Health Information"]
}
```

**Immediate Remediation**:
```bash
# 1. Block all public access immediately
aws s3api put-public-access-block \
  --bucket company-customer-data \
  --public-access-block-configuration \
  "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"

# 2. Remove public bucket policy
aws s3api delete-bucket-policy --bucket company-customer-data

# 3. Enable server-side encryption
aws s3api put-bucket-encryption \
  --bucket company-customer-data \
  --server-side-encryption-configuration '{
    "Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "aws:kms"}}]
  }'
```

**Long-term Remediation**:
```hcl
# Terraform - Enforce secure bucket configuration
resource "aws_s3_bucket_public_access_block" "customer_data" {
  bucket = aws_s3_bucket.customer_data.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "customer_data" {
  bucket = aws_s3_bucket.customer_data.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.customer_data.arn
    }
    bucket_key_enabled = true
  }
}
```

#### CRITICAL-002: Security Group Allows SSH from Internet
**Resource**: `sg-0abc123def456`
**Attached To**: 12 EC2 instances (including prod-db-primary)
**Risk**: Direct attack vector for credential stuffing, brute force

**Current Configuration**:
```json
{
  "IpPermissions": [
    {
      "IpProtocol": "tcp",
      "FromPort": 22,
      "ToPort": 22,
      "IpRanges": [
        {"CidrIp": "0.0.0.0/0"}  // ⚠️ CRITICAL: Open to world
      ]
    }
  ]
}
```

**Remediation**:
```hcl
# Replace with bastion host pattern
resource "aws_security_group" "bastion" {
  name = "bastion-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/8"]  # VPN CIDR only
  }
}

resource "aws_security_group" "private_instances" {
  name = "private-instances-sg"

  ingress {
    from_port       = 22
    to_port         = 22
    protocol        = "tcp"
    security_groups = [aws_security_group.bastion.id]  # Bastion only
  }
}
```

**Better Alternative - Use SSM Session Manager**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ssm:StartSession",
        "ssm:TerminateSession"
      ],
      "Resource": [
        "arn:aws:ec2:*:*:instance/*",
        "arn:aws:ssm:*:*:document/AWS-StartSSHSession"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Environment": "production"
        }
      }
    }
  ]
}
```

#### CRITICAL-003: Root Account Used for Daily Operations
**Account**: 123456789012
**Risk**: Unrestricted access, no MFA enforcement, audit trail issues

**Evidence**:
```
Root Account Activity (Last 30 Days):
- Console logins: 47
- API calls: 1,234
- MFA Status: NOT ENABLED ⚠️
- Access keys: 2 ACTIVE (1 unused for 180 days) ⚠️
```

**Remediation**:
1. Enable MFA on root account immediately
2. Delete root access keys
3. Create IAM users with appropriate permissions
4. Enable AWS Organizations SCPs to restrict root usage

```json
// SCP to restrict root account
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "RestrictRootAccount",
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "aws:PrincipalArn": "arn:aws:iam::*:root"
        }
      }
    }
  ]
}
```

#### CRITICAL-004: Database Publicly Accessible
**Resource**: RDS instance `prod-mysql-primary`
**Risk**: Direct database access from internet

**Current State**:
- PubliclyAccessible: true
- Security Group: Allows 3306 from 0.0.0.0/0
- No SSL enforcement

**Remediation**:
```sql
-- 1. Enforce SSL connections
ALTER USER 'app_user'@'%' REQUIRE SSL;

-- 2. Check current connections
SELECT user, host, ssl_type FROM mysql.user;
```

```hcl
# Terraform remediation
resource "aws_db_instance" "production" {
  identifier             = "prod-mysql-primary"
  publicly_accessible    = false  # Disable public access

  vpc_security_group_ids = [aws_security_group.rds_private.id]
  db_subnet_group_name   = aws_db_subnet_group.private.name

  # Enforce encryption in transit
  parameter_group_name   = aws_db_parameter_group.ssl_required.name
}

resource "aws_db_parameter_group" "ssl_required" {
  family = "mysql8.0"

  parameter {
    name  = "require_secure_transport"
    value = "1"
  }
}
```

### IAM Security Findings

| Finding | Severity | Count | Remediation |
|---------|----------|-------|-------------|
| Users without MFA | HIGH | 8 | Enforce MFA policy |
| Overly permissive policies (*:*) | HIGH | 5 | Implement least privilege |
| Unused access keys (>90 days) | MEDIUM | 12 | Rotate or delete |
| Service accounts with console access | MEDIUM | 3 | Remove console access |
| Cross-account trust without conditions | MEDIUM | 2 | Add external ID |
| Missing permission boundaries | LOW | 15 | Implement boundaries |

### Compliance Gap Analysis

#### SOC2 Type II Mapping
| Control | Requirement | Status | Gap |
|---------|-------------|--------|-----|
| CC6.1 | Logical access security | ⚠️ Partial | MFA not enforced |
| CC6.2 | System authentication | ⚠️ Partial | Weak password policy |
| CC6.3 | Access removal | ✅ Pass | Automated deprovisioning |
| CC6.6 | Encryption | ✅ Pass | At-rest and in-transit |
| CC6.7 | Transmission security | ⚠️ Partial | TLS 1.0/1.1 allowed |
| CC7.1 | Configuration standards | ❌ Fail | No CIS benchmarks |
| CC7.2 | Change management | ✅ Pass | IaC with approvals |

#### HIPAA Compliance (if applicable)
| Requirement | Status | Evidence Gap |
|-------------|--------|--------------|
| §164.312(a)(1) - Access Control | ⚠️ Partial | MFA documentation |
| §164.312(b) - Audit Controls | ⚠️ Partial | 90-day log retention only |
| §164.312(c)(1) - Integrity | ✅ Pass | Checksums enabled |
| §164.312(d) - Authentication | ❌ Fail | Root account usage |
| §164.312(e)(1) - Transmission Security | ⚠️ Partial | TLS version enforcement |

### Security Benchmark Scores

```
CIS AWS Foundations Benchmark v1.5:
├── Identity and Access Management: 62% ⚠️
│   ├── 1.1 Root account MFA: FAIL
│   ├── 1.4 Access key rotation: FAIL
│   ├── 1.10 MFA for IAM users: FAIL
│   └── 1.16 IAM policies attached to groups: PASS
├── Logging: 78% ⚠️
│   ├── 2.1 CloudTrail enabled: PASS
│   ├── 2.2 Log file validation: PASS
│   ├── 2.6 S3 bucket logging: FAIL
│   └── 2.9 VPC Flow Logs: PARTIAL
├── Monitoring: 45% ❌
│   ├── 3.1-3.14 CloudWatch alarms: FAIL (only 6/14 configured)
│   └── Security Hub enabled: FAIL
├── Networking: 71% ⚠️
│   ├── 4.1 SSH restricted: FAIL
│   ├── 4.2 RDP restricted: PASS
│   └── 4.3 Default SG restrictions: FAIL
└── Storage: 85% ✅
    ├── 5.1 S3 public access: PARTIAL
    ├── 5.2 S3 encryption: PASS
    └── 5.3 S3 versioning: PASS
```

### Prioritized Remediation Roadmap

#### Immediate (24-48 hours)
| Action | Finding | Owner | Effort |
|--------|---------|-------|--------|
| Block public S3 bucket | CRITICAL-001 | Security Team | 1 hour |
| Remove 0.0.0.0/0 SSH rule | CRITICAL-002 | DevOps | 2 hours |
| Enable root MFA | CRITICAL-003 | Security Team | 30 min |
| Disable RDS public access | CRITICAL-004 | DBA Team | 4 hours |

#### Short-term (1-2 weeks)
| Action | Finding | Owner | Effort |
|--------|---------|-------|--------|
| Enforce MFA for all users | HIGH-001 | IT Admin | 2 days |
| Implement least privilege IAM | HIGH-002 | Security Team | 1 week |
| Enable Security Hub | HIGH-003 | Security Team | 1 day |
| Configure VPC Flow Logs | HIGH-004 | Network Team | 2 days |

#### Medium-term (1 month)
| Action | Finding | Owner | Effort |
|--------|---------|-------|--------|
| Implement CIS benchmarks | MEDIUM-001 | DevOps | 2 weeks |
| Deploy AWS Config rules | MEDIUM-002 | Security Team | 1 week |
| Implement secrets rotation | MEDIUM-003 | DevOps | 1 week |
| Complete compliance documentation | MEDIUM-004 | Compliance | 2 weeks |

### Security Architecture Recommendations

```
CURRENT STATE:
┌─────────────────────────────────────────┐
│             Internet                     │
└─────────────────┬───────────────────────┘
                  │ (Direct access)
┌─────────────────▼───────────────────────┐
│         Public Subnet                    │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  │
│  │ Web App │  │   RDS   │  │   S3    │  │
│  │ (SSH)   │  │ (3306)  │  │(Public) │  │
│  └─────────┘  └─────────┘  └─────────┘  │
└─────────────────────────────────────────┘

RECOMMENDED STATE:
┌─────────────────────────────────────────┐
│             Internet                     │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│    WAF + CloudFront + Shield Advanced   │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│         Public Subnet (DMZ)              │
│           ┌─────────────┐               │
│           │     ALB     │               │
│           └──────┬──────┘               │
└──────────────────┼──────────────────────┘
                   │ (Private only)
┌──────────────────▼──────────────────────┐
│         Private Subnet                   │
│  ┌─────────┐              ┌─────────┐   │
│  │ Web App │◄────────────▶│ ElastiC │   │
│  │ (No SSH)│              │  ache   │   │
│  └────┬────┘              └─────────┘   │
│       │                                  │
│  ┌────▼────┐                            │
│  │   RDS   │ (Private endpoints)        │
│  └─────────┘                            │
└─────────────────────────────────────────┘
```
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- DS-01 (Framework Application - CIS Benchmarks, NIST, SOC2)
- DS-06 (Prioritization and Severity Guidance)
- RT-05 (Evidence-Based Reasoning)
- DS-05 (Visualization and Communication Guidance)

**Related Prompts:**
- cloud_aws_architecture_review.md - For AWS Well-Architected security
- cloud_azure_best_practices.md - For Azure security best practices
- cloud_gcp_best_practices.md - For GCP security best practices
- code-analysis/security/security_owasp_top_10_analysis.md - For application security
- devops_container_security.md - For container-specific security
- code-analysis/security/security_compliance_analysis.md - For compliance mapping

**Customization Guide:**
- **For Healthcare (HIPAA)**: Focus on PHI protection, BAA requirements, audit controls
- **For Financial (PCI-DSS)**: Emphasize cardholder data environment, network segmentation
- **For Government (FedRAMP)**: Add FedRAMP control mappings, boundary documentation
- **For GDPR**: Focus on data residency, consent management, right to deletion
- **For Multi-Cloud**: Include consistent security controls across cloud providers
