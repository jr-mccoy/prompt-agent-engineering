---
title: "Cloud Cost Optimization Analysis"
category: cloud
description: "Cloud Cost Optimization Analysis"
tags:
  - cloud
  - optimization
updated: "2026-03-19"
---

# Cloud Cost Optimization Analysis

**Objective:** Analyze cloud infrastructure across AWS, Azure, or GCP to identify cost reduction opportunities, optimize resource utilization, and implement FinOps best practices for sustainable cloud spending.

**When to Use:** Use this prompt when reviewing monthly cloud bills, preparing for budget planning, implementing FinOps practices, rightsizing resources, or conducting cloud cost audits.

**Instructions:**

1. **Analyze Current Spending Overview**
   - Review total cloud spend by service/category
   - Identify top 10 cost drivers
   - Analyze spending trends (month-over-month, year-over-year)
   - Map costs to business units/applications/teams
   - Calculate unit economics (cost per transaction, user, API call)

2. **Evaluate Commitment-Based Discounts**
   - **AWS**: Reserved Instances, Savings Plans, Compute Savings Plans
   - **Azure**: Reserved Instances, Azure Savings Plans, Azure Hybrid Benefit
   - **GCP**: Committed Use Discounts (CUDs), Sustained Use Discounts (SUDs)
   - Analyze current coverage percentage
   - Identify optimal commitment term (1-year vs 3-year)
   - Calculate break-even points and ROI

3. **Identify Idle and Unused Resources**
   - Unattached storage volumes and snapshots
   - Idle load balancers and NAT gateways
   - Unused Elastic IPs/Static IPs
   - Stopped instances still incurring costs
   - Orphaned resources after deployments
   - Unused reserved capacity

4. **Rightsizing Analysis**
   - Analyze CPU, memory, network, and storage utilization
   - Identify oversized compute instances
   - Evaluate database tier appropriateness
   - Review storage class/tier selection
   - Assess container resource requests vs actual usage
   - Identify candidates for instance family changes

5. **Optimize Compute Costs**
   - Evaluate Spot/Preemptible/Low-Priority instance opportunities
   - Review auto-scaling configurations
   - Analyze scheduled scaling for predictable workloads
   - Assess containerization opportunities
   - Evaluate serverless migration candidates
   - Check for unnecessary high-availability in non-prod

6. **Optimize Storage Costs**
   - Review storage tier distribution (hot/warm/cold/archive)
   - Analyze object lifecycle policies
   - Identify large, infrequently accessed data
   - Evaluate compression and deduplication
   - Check snapshot retention policies
   - Review database storage provisioning

7. **Optimize Network and Data Transfer Costs**
   - Analyze inter-region data transfer
   - Review NAT Gateway/Cloud NAT usage
   - Evaluate CDN effectiveness
   - Check VPC/Private Endpoint optimization
   - Identify unnecessary public IP usage
   - Review cross-AZ traffic patterns

8. **Implement FinOps Practices**
   - Review cost allocation tags and coverage
   - Assess budget and alert configurations
   - Evaluate showback/chargeback implementation
   - Check anomaly detection setup
   - Review governance policies
   - Assess team cost awareness and accountability

**Expected Output:** A comprehensive cost optimization report including:
- Executive summary with total savings opportunity
- Detailed analysis by cost optimization category
- Specific resource-level recommendations
- Implementation priority and effort estimates
- ROI calculations and payback periods
- Monthly and annual savings projections

**Example Output:**

```markdown
## Cloud Cost Optimization Report

### Executive Summary

| Metric | Current | Optimized | Savings |
|--------|---------|-----------|---------|
| **Monthly Spend** | $127,450 | $89,200 | $38,250 (30%) |
| **Annual Projection** | $1,529,400 | $1,070,400 | $459,000 |
| **Quick Wins (< 1 week)** | - | - | $12,400/month |
| **Medium Term (1-4 weeks)** | - | - | $18,600/month |
| **Long Term (1-3 months)** | - | - | $7,250/month |

### Spending Distribution

```
Top 10 Services by Cost:
┌────────────────────────────────────────────────────────┐
│ Compute (EC2/VMs)           ████████████████  $52,300  │
│ Database (RDS/SQL)          ████████████      $31,200  │
│ Storage (S3/Blob)           ████████          $18,400  │
│ Data Transfer               █████             $9,800   │
│ Kubernetes (EKS/AKS)        ████              $6,200   │
│ Load Balancing              ███               $4,100   │
│ Serverless                  ██                $2,800   │
│ Monitoring                  ██                $1,400   │
│ Other                       █                 $1,250   │
└────────────────────────────────────────────────────────┘
```

### Commitment-Based Discounts Analysis

#### Current Coverage
| Resource Type | On-Demand | Reserved/Committed | Spot/Preemptible |
|--------------|-----------|-------------------|------------------|
| Compute | 68% | 22% | 10% |
| Database | 85% | 15% | N/A |
| **Target** | 30% | 55% | 15% |

#### Recommended Commitments

**Option A: Conservative (1-Year Commitments)**
```
EC2 Reserved Instances (1-year, partial upfront):
- 20x m5.xlarge: $8,760/year savings (vs on-demand)
- 10x r5.2xlarge: $12,400/year savings
- Break-even: 7.2 months

RDS Reserved Instances (1-year, partial upfront):
- 4x db.r5.large Multi-AZ: $6,200/year savings
- Break-even: 7.8 months

Total 1-Year Savings: $27,360/year
```

**Option B: Aggressive (3-Year Commitments)**
```
Compute Savings Plan (3-year, partial upfront):
- $15/hour commitment
- Covers 75% of compute spend
- 52% discount vs on-demand
- Annual savings: $48,200

Total 3-Year Savings: $144,600 over term
ROI: 186%
```

### Idle Resources to Terminate

| Resource | Type | Region | Monthly Cost | Last Activity |
|----------|------|--------|--------------|---------------|
| vol-0abc123 | EBS gp3 | us-east-1 | $240 | Unattached 45 days |
| vol-0def456 | EBS gp3 | us-east-1 | $180 | Unattached 30 days |
| snap-0123abc | Snapshot | us-east-1 | $85 | Orphaned |
| eip-192-168-1-1 | Elastic IP | us-west-2 | $7.30 | Unassociated |
| lb-old-prod | ALB | us-east-1 | $22 | 0 requests/day |
| dev-cluster-old | EKS | eu-west-1 | $146 | No pods running |
| **Total Waste** | | | **$680/month** | |

### Rightsizing Recommendations

#### Compute Instances
| Instance | Current | Recommended | Monthly Savings | Utilization |
|----------|---------|-------------|-----------------|-------------|
| prod-api-1 | m5.2xlarge | m5.xlarge | $146 | CPU: 12% |
| prod-api-2 | m5.2xlarge | m5.xlarge | $146 | CPU: 15% |
| prod-worker-1 | c5.4xlarge | c5.2xlarge | $244 | CPU: 22% |
| batch-proc-1 | r5.4xlarge | r5.2xlarge | $365 | Mem: 28% |
| **Subtotal** | | | **$901/month** | |

#### Database Instances
| Database | Current | Recommended | Monthly Savings | Utilization |
|----------|---------|-------------|-----------------|-------------|
| prod-mysql | db.r5.2xlarge | db.r5.xlarge | $420 | CPU: 18%, Mem: 35% |
| analytics-pg | db.r5.4xlarge | db.r5.2xlarge | $840 | CPU: 22%, Mem: 42% |
| **Subtotal** | | | **$1,260/month** | |

### Spot/Preemptible Instance Opportunities

| Workload | Current Cost | Spot Cost | Savings | Interruption Risk |
|----------|--------------|-----------|---------|-------------------|
| Batch Processing | $2,400 | $720 | $1,680 (70%) | Acceptable |
| Dev/Test Clusters | $1,800 | $540 | $1,260 (70%) | Acceptable |
| CI/CD Runners | $960 | $288 | $672 (70%) | Acceptable |
| ML Training | $3,200 | $960 | $2,240 (70%) | With checkpoints |
| **Total** | **$8,360** | **$2,508** | **$5,852/month** | |

### Storage Optimization

#### Lifecycle Policy Recommendations
```json
{
  "Rules": [
    {
      "ID": "MoveToInfrequentAccess",
      "Status": "Enabled",
      "Transitions": [
        {
          "Days": 30,
          "StorageClass": "STANDARD_IA"
        }
      ],
      "Filter": {
        "Prefix": "logs/"
      }
    },
    {
      "ID": "MoveToGlacier",
      "Status": "Enabled",
      "Transitions": [
        {
          "Days": 90,
          "StorageClass": "GLACIER"
        }
      ],
      "Filter": {
        "Prefix": "backups/"
      }
    },
    {
      "ID": "DeleteOldLogs",
      "Status": "Enabled",
      "Expiration": {
        "Days": 365
      },
      "Filter": {
        "Prefix": "logs/"
      }
    }
  ]
}
```

**Storage Savings Projection:**
| Tier Change | Data Volume | Current Cost | New Cost | Savings |
|-------------|-------------|--------------|----------|---------|
| Standard → IA | 15 TB | $345 | $189 | $156 |
| Standard → Glacier | 45 TB | $1,035 | $180 | $855 |
| Delete old logs | 8 TB | $184 | $0 | $184 |
| **Total** | | | | **$1,195/month** |

### Network Cost Optimization

| Issue | Current Cost | Optimization | Savings |
|-------|--------------|--------------|---------|
| Cross-AZ traffic via public IPs | $420 | Use private IPs | $380 |
| No VPC Endpoints for S3 | $280 | Add Gateway Endpoint | $250 |
| NAT Gateway overuse | $540 | Consolidate + review | $180 |
| Unused static IPs | $35 | Release | $35 |
| **Total** | | | **$845/month** |

### Implementation Roadmap

#### Week 1: Quick Wins ($12,400/month savings)
- [ ] Delete orphaned EBS volumes and snapshots
- [ ] Terminate idle resources (old clusters, LBs)
- [ ] Release unused Elastic IPs
- [ ] Implement S3 lifecycle policies

#### Weeks 2-4: Medium-Term ($18,600/month savings)
- [ ] Rightsize oversized compute instances
- [ ] Rightsize database instances
- [ ] Convert batch workloads to Spot instances
- [ ] Implement VPC endpoints

#### Months 2-3: Strategic ($7,250/month savings)
- [ ] Purchase Reserved Instances/Savings Plans
- [ ] Implement comprehensive tagging
- [ ] Set up FinOps dashboards and alerts
- [ ] Train teams on cost-aware development

### FinOps Maturity Assessment

| Practice | Current State | Target State | Gap |
|----------|---------------|--------------|-----|
| Cost Allocation Tags | 45% coverage | 95% coverage | High |
| Budget Alerts | Basic | Per-team | Medium |
| Anomaly Detection | Not configured | Active | High |
| Showback Reports | Manual monthly | Automated daily | Medium |
| Team Accountability | Centralized | Distributed | High |

### Summary by Savings Category

| Category | Monthly Savings | Annual Savings | Effort |
|----------|-----------------|----------------|--------|
| Commitment Discounts | $4,050 | $48,600 | Low |
| Idle Resource Cleanup | $680 | $8,160 | Low |
| Compute Rightsizing | $901 | $10,812 | Medium |
| Database Rightsizing | $1,260 | $15,120 | Medium |
| Spot Instance Migration | $5,852 | $70,224 | Medium |
| Storage Optimization | $1,195 | $14,340 | Low |
| Network Optimization | $845 | $10,140 | Low |
| **Grand Total** | **$14,783** | **$177,396** | |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- OC-03 (Markdown Table Specification)
- DS-02 (Metric Specification)
- DS-06 (Prioritization and Severity Guidance)
- NE-11 (Embedded Calculation Formulas)

**Related Prompts:**
- cloud_aws_architecture_review.md - For AWS-specific optimization
- cloud_azure_best_practices.md - For Azure-specific optimization
- cloud_gcp_best_practices.md - For GCP-specific optimization
- devops_monitoring_observability.md - For cost monitoring dashboards
- business-analysis/business_value_chain_analysis.md - For cost-to-value mapping

**Customization Guide:**
- **For Startups**: Focus on quick wins and avoiding commitment until usage patterns stabilize
- **For Enterprises**: Emphasize FinOps governance, chargeback models, and enterprise agreements
- **For Multi-Cloud**: Add comparison analysis and workload placement optimization
- **For Seasonal Workloads**: Focus on auto-scaling and scheduled scaling over commitments
- **For Data-Intensive**: Prioritize storage tiering, data transfer, and compute-storage colocation


---

## Must / Must Not

**Must:**
- Quote actual costs (or ranges) from the user's bill / Cost Explorer output — never fabricate dollar amounts.
- Label each recommendation with: **Quick Win** (< 1 day, no arch change), **Medium** (1-4 weeks, some arch change), **Major** (> 1 quarter, significant refactor).
- Include expected savings range (e.g., "20-40% of EC2 spend"), NOT a single number unless grounded in the user's data.
- Verify whether workloads are production vs. non-production — cost rules differ (non-prod: spot, schedules, auto-shutdown).
- Distinguish between **commitment-based savings** (RIs/SPs — need usage stability) and **architectural savings** (rightsizing, tiered storage — work immediately).

**Must Not:**
- Recommend Reserved Instances or Savings Plans without confirming usage stability for at least 90 days.
- Suggest deleting resources without a reversibility / recovery plan.
- Recommend spot instances for stateful production workloads without explaining interruption handling.
- Propose cost cuts that violate **compliance** (data residency, retention, isolation) or **SLAs**.
- Promise a specific percentage savings without the data to back it.

## Verification (Self-Check)

Before delivering recommendations:

1. **Workload criticality confirmed** — Each recommendation tagged by environment (prod / staging / dev).
2. **Compliance impact stated** — Any cost-cut that touches retention, encryption, region, or logging is flagged with the compliance dimension affected.
3. **Savings range, not point estimate** — Every dollar figure is a range with stated assumptions.
4. **Rollback path stated** — For any destructive action (delete, resize, migrate), include the restore / revert command or plan.
5. **Confidence level** on each savings estimate (High = from user's billing data; Medium = industry benchmark; Low = guess).

## False-Positive Prevention

Rule out:

- **"Rightsize this oversized instance"** — Verify actual CPU/memory utilization over 14+ days; spikes matter, averages mislead.
- **"Buy Reserved Instances"** — Only if baseline stable for 90+ days and the team can commit; otherwise dangerous.
- **"Move to spot"** — Only for fault-tolerant, stateless workloads that handle 2-minute interruption.
- **"Delete unused NAT Gateway"** — Verify no VPC endpoints / private subnets depend on it before recommending removal.
- **"Storage class tiering"** — Infrequent-access tiers have retrieval costs; bursty access can cost MORE than standard.
- **"Multi-region is wasteful"** — Only if DR requirements don't demand it; check RPO/RTO first.

Every "Quick Win" label must be genuinely < 1 day of engineering; if in doubt, demote to **Medium**.
