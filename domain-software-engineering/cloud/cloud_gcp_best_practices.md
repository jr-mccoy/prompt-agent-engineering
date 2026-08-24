---
title: "GCP Architecture Review and Best Practices Analysis"
category: cloud
description: "Analyze GCP infrastructure configurations for adherence to best practices across operational excellence, security, reliability, performance, and cost"
tags:
  - cloud
updated: "2026-03-19"
---

# GCP Architecture Review and Best Practices Analysis

**Objective:** Analyze Google Cloud Platform infrastructure configurations for adherence to GCP best practices, evaluating operational excellence, security, reliability, performance, and cost optimization across all deployed services.

**When to Use:** Use this prompt when designing new GCP architectures, reviewing existing deployments, preparing for cloud audits, optimizing GCP costs, or migrating workloads to Google Cloud.

**Instructions:**

1. **Analyze Architecture Overview**
   - Review the overall GCP architecture and service composition
   - Identify project and folder hierarchy structure
   - Map out service dependencies and data flows
   - Document multi-region or multi-zone configurations
   - Assess alignment with GCP reference architectures

2. **Organization and Resource Management Review**
   - Evaluate organization, folder, and project hierarchy
   - Review resource labeling and tagging strategy
   - Check for proper resource naming conventions
   - Assess billing account and budget configurations
   - Review quota management and limit monitoring

3. **Identity and Access Management (IAM) Review**
   - Analyze IAM policies for least privilege principle
   - Review service account usage and key management
   - Check for organization policy constraints
   - Evaluate Workload Identity configurations
   - Assess Cloud Identity and SSO integration
   - Review VPC Service Controls and access context

4. **Network Security Review**
   - Evaluate VPC architecture (Shared VPC, VPC peering)
   - Review firewall rules and hierarchical policies
   - Check Private Google Access configurations
   - Assess Cloud NAT and external connectivity
   - Review Cloud Armor and DDoS protection
   - Evaluate network segmentation and microsegmentation

5. **Compute and Container Review**
   - Analyze Compute Engine configurations
     - Machine types and custom machine sizes
     - Preemptible/Spot VM usage
     - Managed instance groups and autoscaling
   - Review GKE clusters
     - Node pool configurations
     - Autopilot vs. Standard mode
     - Workload Identity and pod security
     - Network policies and service mesh
   - Assess Cloud Run and Cloud Functions usage

6. **Data Services Review**
   - Evaluate Cloud SQL configurations
     - High availability and regional setup
     - Automated backups and PITR
     - Connection security (Private IP, Cloud SQL Auth Proxy)
   - Review Cloud Spanner and Bigtable configurations
   - Assess BigQuery
     - Dataset organization and access controls
     - Partitioning and clustering strategies
     - Slot reservations and flat-rate pricing
   - Check Cloud Storage
     - Bucket configurations and lifecycle policies
     - Uniform bucket-level access
     - Customer-managed encryption keys (CMEK)

7. **Reliability and Operations Review**
   - Evaluate high availability configurations
   - Review Cloud Monitoring and alerting setup
   - Assess Cloud Logging configurations and sinks
   - Check Error Reporting and Cloud Trace integration
   - Review backup and disaster recovery strategies
   - Evaluate SRE practices and SLO definitions

8. **Cost Optimization Review**
   - Analyze committed use discounts (CUDs)
   - Review Sustained Use Discounts (SUDs) benefits
   - Identify idle and underutilized resources
   - Evaluate BigQuery cost controls
   - Check for active cost recommendations
   - Review export and egress costs

**Expected Output:** A comprehensive GCP architecture review report including:
- Executive summary with architecture health assessment
- Category-by-category analysis with specific findings
- Risk assessment with severity ratings
- Prioritized recommendations with implementation steps
- Cost optimization opportunities with savings estimates
- GCP-specific best practice checklist

**Example Output:**

```markdown
## GCP Architecture Review Report

### Executive Summary
- **Overall Health Score**: 68/100 (Good with significant improvement opportunities)
- **Critical Issues**: 1
- **High Priority**: 4
- **Medium Priority**: 7
- **Estimated Monthly Savings**: $2,800-$3,500

### Architecture Overview
**Organization**: acme-corp.com
**Primary Region**: us-central1
**Multi-Zone**: Partial coverage
**Key Services**: GKE, Cloud SQL, BigQuery, Cloud Run, Cloud Storage

```
┌─────────────────────────────────────────────────────────┐
│                   Cloud Load Balancer                    │
│                 (Global, HTTPS, Cloud CDN)               │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────┐
│                      GKE Cluster                         │
│              (us-central1, Regional)                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │  Node Pool   │  │  Node Pool   │  │  Node Pool   │   │
│  │  (default)   │  │  (workload)  │  │  (spot)      │   │
│  │  e2-standard │  │  n2-standard │  │  n2-standard │   │
│  └──────────────┘  └──────────────┘  └──────────────┘   │
└──────────┬────────────────────────────────┬─────────────┘
           │                                │
    ┌──────▼──────┐                  ┌──────▼──────┐
    │  Cloud SQL  │                  │  BigQuery   │
    │  PostgreSQL │                  │  (Dataset)  │
    │  ⚠️ Single   │                  │             │
    │    Zone     │                  │             │
    └─────────────┘                  └─────────────┘
```

### Critical Issues

#### Issue 1: Cloud SQL Single-Zone Deployment (CRITICAL)
**Location**: Cloud SQL instance `prod-db-postgres`
**Project**: `acme-production`
**Risk**: Database outage if us-central1-a zone fails

**Current Configuration**:
```yaml
# terraform output
resource "google_sql_database_instance" "production" {
  name             = "prod-db-postgres"
  database_version = "POSTGRES_14"
  region           = "us-central1"

  settings {
    tier              = "db-custom-4-16384"
    availability_type = "ZONAL"  # ⚠️ CRITICAL - Single zone

    backup_configuration {
      enabled = true
      point_in_time_recovery_enabled = false  # ⚠️ No PITR
    }
  }
}
```

**Recommended Configuration**:
```yaml
resource "google_sql_database_instance" "production" {
  name             = "prod-db-postgres"
  database_version = "POSTGRES_14"
  region           = "us-central1"

  settings {
    tier              = "db-custom-4-16384"
    availability_type = "REGIONAL"  # ✅ High availability

    backup_configuration {
      enabled                        = true
      point_in_time_recovery_enabled = true  # ✅ Enable PITR
      transaction_log_retention_days = 7
      backup_retention_settings {
        retained_backups = 14
      }
    }

    maintenance_window {
      day          = 7  # Sunday
      hour         = 3  # 3 AM
      update_track = "stable"
    }
  }
}
```
**Cost Impact**: ~$280/month increase
**Priority**: CRITICAL - Implement within 48 hours

### High Priority Issues

#### Issue 2: Missing Workload Identity (HIGH)
**Location**: GKE cluster `prod-cluster`
**Risk**: Service account key exposure, credential management overhead

**Current State**: Pods using exported service account keys
**Recommended**: Enable Workload Identity for secure, keyless authentication

```yaml
# Enable Workload Identity on cluster
resource "google_container_cluster" "primary" {
  name = "prod-cluster"

  workload_identity_config {
    workload_pool = "acme-production.svc.id.goog"
  }
}

# Configure Kubernetes service account binding
resource "google_service_account_iam_binding" "workload_identity" {
  service_account_id = google_service_account.app_sa.name
  role               = "roles/iam.workloadIdentityUser"
  members = [
    "serviceAccount:acme-production.svc.id.goog[default/app-service-account]"
  ]
}
```

#### Issue 3: BigQuery Without Cost Controls (HIGH)
**Location**: BigQuery dataset `analytics`
**Risk**: Unexpected query costs from ad-hoc analysis

**Current State**: No slot reservations, on-demand pricing, no query limits
**Recommended**:
```sql
-- Create custom cost control
ALTER PROJECT `acme-production`
SET OPTIONS (
  `region-us`.default_query_quota_per_user_per_day = 10 TB
);

-- Consider flat-rate pricing for predictable workloads
-- 500 slots = ~$10,000/month vs variable on-demand
```

### IAM Analysis

| Check | Status | Finding |
|-------|--------|---------|
| Service Account Keys | ❌ FAIL | 12 active keys, 5 > 90 days old |
| Primitive Roles | ⚠️ WARN | 3 users with roles/owner |
| Workload Identity | ❌ FAIL | Not enabled on GKE |
| Organization Policies | ⚠️ WARN | Partial enforcement |
| VPC Service Controls | ❌ FAIL | Not configured |

### Cost Optimization Opportunities

| Opportunity | Current Cost | Optimized Cost | Monthly Savings |
|-------------|--------------|----------------|-----------------|
| Committed Use Discounts (3-year) | $4,200 | $2,520 | $1,680 |
| Preemptible/Spot VMs for batch | $800 | $240 | $560 |
| BigQuery slot reservations | $1,500 | $1,000 | $500 |
| Cloud Storage lifecycle policies | $450 | $280 | $170 |
| Idle VM shutdown automation | $320 | $0 | $320 |
| **Total** | | | **$3,230/month** |

### GCP Best Practices Checklist

| Category | Practice | Status |
|----------|----------|--------|
| **IAM** | No service account keys in code | ⚠️ Partial |
| **IAM** | Workload Identity enabled | ❌ No |
| **IAM** | Custom roles over primitive | ⚠️ Partial |
| **Network** | Private Google Access | ✅ Yes |
| **Network** | VPC Service Controls | ❌ No |
| **Network** | Hierarchical firewall policies | ✅ Yes |
| **Compute** | Committed use discounts | ❌ No |
| **Compute** | Managed instance groups | ✅ Yes |
| **Data** | Cloud SQL HA enabled | ❌ No |
| **Data** | CMEK for sensitive data | ⚠️ Partial |
| **Data** | BigQuery partitioning | ✅ Yes |
| **Ops** | Cloud Monitoring dashboards | ✅ Yes |
| **Ops** | Alerting policies | ⚠️ Basic |
| **Ops** | Error Reporting integration | ✅ Yes |

### Prioritized Recommendations

| Priority | Recommendation | Effort | Impact | Timeline |
|----------|----------------|--------|--------|----------|
| P0 | Enable Cloud SQL HA | Low | Critical | 48 hours |
| P1 | Enable Workload Identity | Medium | High | 1 week |
| P1 | Rotate service account keys | Medium | High | 1 week |
| P1 | Configure VPC Service Controls | High | High | 2 weeks |
| P2 | Purchase CUDs | Low | Medium | 1 month |
| P2 | Implement BigQuery cost controls | Low | Medium | 1 week |
| P3 | Convert batch to Spot VMs | Medium | Medium | 2 weeks |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- DS-01 (Framework Application - GCP Best Practices)
- DS-06 (Prioritization and Severity Guidance)
- RT-05 (Evidence-Based Reasoning)

**Related Prompts:**
- cloud_aws_architecture_review.md - For multi-cloud comparison
- cloud_cost_optimization.md - For deeper cost analysis
- cloud_security_review.md - For comprehensive security audit
- cloud_serverless_function_analysis.md - For Cloud Functions/Cloud Run
- devops_kubernetes_manifest_review.md - For GKE workload review

**Customization Guide:**
- **For Data Analytics Focus**: Emphasize BigQuery, Dataflow, Pub/Sub, and data pipeline configurations
- **For ML/AI Workloads**: Focus on Vertex AI, TPU configurations, model serving patterns
- **For Hybrid/Multi-Cloud**: Add Anthos, Cloud Interconnect, and federation patterns
- **For Regulated Industries**: Emphasize Assured Workloads, CMEK, and compliance controls
- **For Startups**: Focus on cost optimization, Firebase integration, and rapid scaling patterns
