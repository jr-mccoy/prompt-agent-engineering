---
title: "Azure Architecture Review and Best Practices Analysis"
category: cloud
description: "Azure Architecture Review and Best Practices Analysis"
tags:
  - cloud
updated: "2026-03-19"
---

# Azure Architecture Review and Best Practices Analysis

**Objective:** Analyze Microsoft Azure infrastructure configurations for adherence to the Azure Well-Architected Framework, evaluating cost optimization, operational excellence, performance efficiency, reliability, and security across all deployed resources.

**When to Use:** Use this prompt when designing new Azure architectures, reviewing existing deployments, preparing for Azure Well-Architected Reviews, optimizing cloud costs, or conducting Azure migration assessments.

**Instructions:**

1. **Analyze Architecture Overview**
   - Review the overall Azure architecture and service composition
   - Identify management group, subscription, and resource group hierarchy
   - Map out service dependencies and data flows
   - Document multi-region and availability zone configurations
   - Assess alignment with Azure reference architectures and landing zones

2. **Cost Optimization Pillar Review**
   - Analyze Azure Advisor cost recommendations
   - Review Reserved Instance and Savings Plan coverage
   - Check Azure Hybrid Benefit utilization
   - Identify orphaned and unused resources
   - Evaluate resource SKU selection and right-sizing
   - Review cost allocation tags and budgets

3. **Operational Excellence Pillar Review**
   - Evaluate Infrastructure as Code (ARM, Bicep, Terraform)
   - Review Azure DevOps or GitHub Actions pipelines
   - Assess Azure Monitor configuration and alerting
   - Check Application Insights integration
   - Review Azure Automation and runbooks
   - Evaluate deployment strategies (Blue-Green, Canary)

4. **Performance Efficiency Pillar Review**
   - Analyze compute SKU selection and scaling
   - Review Azure CDN and Front Door configurations
   - Evaluate storage account performance tiers
   - Check Azure Cache for Redis implementation
   - Assess database performance (DTU vs vCore, read replicas)
   - Review network latency optimization (ExpressRoute, proximity placement)

5. **Reliability Pillar Review**
   - Evaluate availability zone and regional redundancy
   - Review Azure Site Recovery configurations
   - Check backup policies and retention
   - Assess health probes and traffic manager routing
   - Review auto-scaling rules and capacity planning
   - Evaluate resilience patterns (retry, circuit breaker)

6. **Security Pillar Review**
   - Analyze Azure AD and RBAC configurations
   - Review Network Security Groups and Azure Firewall
   - Check Azure Key Vault usage and access policies
   - Evaluate Microsoft Defender for Cloud findings
   - Assess Private Endpoints and Service Endpoints
   - Review Azure Policy compliance and initiatives
   - Check encryption configurations (TDE, SSE, TLS)

7. **Azure Service-Specific Analysis**
   - Virtual Machines: Size selection, availability sets, scale sets
   - Azure SQL: Service tier, geo-replication, elastic pools
   - App Service: Service plans, deployment slots, health checks
   - AKS: Node pools, CNI configuration, pod identity
   - Storage Accounts: Redundancy, access tiers, lifecycle management
   - Azure Functions: Consumption vs Premium, cold start mitigation

8. **Governance and Compliance Review**
   - Evaluate Azure Policy assignments and exemptions
   - Review management group hierarchy
   - Check Azure Blueprints implementation
   - Assess regulatory compliance posture
   - Review Azure Lighthouse for multi-tenant scenarios

**Expected Output:** A comprehensive Azure architecture review report including:
- Executive summary with Well-Architected Framework scores
- Pillar-by-pillar analysis with specific findings
- Risk assessment with severity ratings
- Azure Advisor alignment and recommendations
- Cost optimization opportunities with ROI estimates
- Architecture diagrams showing current and target states

**Example Output:**

```markdown
## Azure Architecture Review Report

### Executive Summary
- **Overall Health Score**: 71/100 (Good with improvement areas)
- **Critical Issues**: 2
- **High Priority**: 4
- **Medium Priority**: 9
- **Azure Advisor Score**: 67%
- **Estimated Monthly Savings**: $4,200-$5,600

### Architecture Overview
**Tenant**: Contoso Corp (contoso.onmicrosoft.com)
**Primary Region**: East US
**Secondary Region**: West US 2 (DR only)
**Subscription Model**: Production, Non-Production, Shared Services

```
┌─────────────────────────────────────────────────────────┐
│                    Azure Front Door                      │
│              (Global Load Balancer + WAF)                │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────┐
│                   Application Gateway                    │
│                      (East US)                           │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────┐
│                         AKS                              │
│              (East US, 3 Node Pools)                     │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐        │
│  │  System    │  │  User      │  │  Spot      │        │
│  │  Pool      │  │  Pool      │  │  Pool      │        │
│  └────────────┘  └────────────┘  └────────────┘        │
└──────────┬────────────────────────────┬─────────────────┘
           │                            │
    ┌──────▼──────┐              ┌──────▼──────┐
    │ Azure SQL   │              │  Cosmos DB  │
    │ ⚠️ No Geo-   │              │  (Multi-    │
    │   Replication│              │   Region)   │
    └─────────────┘              └─────────────┘
```

### Critical Issues

#### Issue 1: Azure SQL Without Geo-Replication (CRITICAL)
**Resource**: Azure SQL Server `contoso-sql-prod`
**Resource Group**: `rg-prod-data`
**Risk**: Complete data tier outage if East US region fails

**Current Configuration**:
```bicep
resource sqlServer 'Microsoft.Sql/servers@2022-05-01-preview' = {
  name: 'contoso-sql-prod'
  location: 'eastus'

  resource database 'databases' = {
    name: 'app-database'
    sku: {
      name: 'GP_Gen5_4'
      tier: 'GeneralPurpose'
    }
    // ⚠️ No geo-replication configured
  }
}
```

**Recommended Configuration**:
```bicep
resource sqlServer 'Microsoft.Sql/servers@2022-05-01-preview' = {
  name: 'contoso-sql-prod'
  location: 'eastus'
}

resource sqlServerSecondary 'Microsoft.Sql/servers@2022-05-01-preview' = {
  name: 'contoso-sql-prod-secondary'
  location: 'westus2'
}

resource database 'Microsoft.Sql/servers/databases@2022-05-01-preview' = {
  parent: sqlServer
  name: 'app-database'
  sku: {
    name: 'GP_Gen5_4'
    tier: 'GeneralPurpose'
  }
}

// ✅ Active geo-replication
resource geoReplication 'Microsoft.Sql/servers/databases/geoReplication@2022-05-01-preview' = {
  name: 'westus2'
  parent: database
  properties: {
    partnerServer: sqlServerSecondary.id
    partnerDatabase: 'app-database'
  }
}

// ✅ Auto-failover group
resource failoverGroup 'Microsoft.Sql/servers/failoverGroups@2022-05-01-preview' = {
  parent: sqlServer
  name: 'contoso-failover'
  properties: {
    partnerServers: [{ id: sqlServerSecondary.id }]
    readWriteEndpoint: {
      failoverPolicy: 'Automatic'
      failoverWithDataLossGracePeriodMinutes: 60
    }
  }
}
```
**Cost Impact**: ~$450/month (secondary database)
**Priority**: CRITICAL - Implement within 1 week

#### Issue 2: Overly Permissive NSG Rules (CRITICAL)
**Resource**: NSG `nsg-web-tier`
**Risk**: Unrestricted inbound access to web tier from any source

**Current Rule**:
```json
{
  "name": "Allow-All-Inbound",
  "priority": 100,
  "direction": "Inbound",
  "access": "Allow",
  "protocol": "*",
  "sourceAddressPrefix": "*",
  "destinationAddressPrefix": "*",
  "destinationPortRange": "*"
}
```

**Recommended**:
```bicep
resource nsg 'Microsoft.Network/networkSecurityGroups@2023-04-01' = {
  name: 'nsg-web-tier'
  properties: {
    securityRules: [
      {
        name: 'Allow-HTTPS-From-AppGW'
        properties: {
          priority: 100
          direction: 'Inbound'
          access: 'Allow'
          protocol: 'Tcp'
          sourceAddressPrefix: '10.0.1.0/24'  // App Gateway subnet
          destinationPortRange: '443'
        }
      }
      {
        name: 'Deny-All-Inbound'
        properties: {
          priority: 4096
          direction: 'Inbound'
          access: 'Deny'
          protocol: '*'
          sourceAddressPrefix: '*'
          destinationPortRange: '*'
        }
      }
    ]
  }
}
```
**Priority**: CRITICAL - Implement immediately

### Well-Architected Framework Scores

| Pillar | Score | Key Issues |
|--------|-------|------------|
| Cost Optimization | 65/100 | No Reserved Instances, orphaned resources |
| Operational Excellence | 72/100 | Limited alerting, no runbooks |
| Performance Efficiency | 78/100 | Good CDN usage, needs caching review |
| Reliability | 58/100 | No geo-replication, limited DR testing |
| Security | 62/100 | Permissive NSGs, Key Vault partially used |

### Azure Advisor Recommendations

| Category | Recommendation | Impact | Status |
|----------|----------------|--------|--------|
| Cost | Right-size underutilized VMs | $820/month | Not Implemented |
| Cost | Delete orphaned disks | $180/month | Not Implemented |
| Cost | Purchase Reserved Instances | $2,400/month | Not Implemented |
| Security | Enable Azure Defender | High | Partially Enabled |
| Reliability | Enable backup for VMs | High | 70% Coverage |
| Performance | Enable accelerated networking | Medium | Not Implemented |

### Cost Optimization Opportunities

| Opportunity | Current Cost | Optimized Cost | Monthly Savings |
|-------------|--------------|----------------|-----------------|
| 3-Year Reserved Instances | $8,400 | $4,800 | $3,600 |
| Azure Hybrid Benefit (existing licenses) | $2,100 | $840 | $1,260 |
| Delete orphaned resources | $380 | $0 | $380 |
| Right-size VMs (Advisor) | $2,200 | $1,380 | $820 |
| Storage tier optimization | $450 | $280 | $170 |
| **Total** | | | **$6,230/month** |

### Security Posture Assessment

| Control | Status | Microsoft Defender Score |
|---------|--------|-------------------------|
| Network Security | ⚠️ Needs Work | 45% |
| Identity & Access | ✅ Good | 78% |
| Data Protection | ⚠️ Needs Work | 62% |
| Compute Security | ✅ Good | 71% |
| IoT Security | N/A | - |
| **Overall** | | **64%** |

### Prioritized Recommendations

| Priority | Recommendation | Effort | Impact | Timeline |
|----------|----------------|--------|--------|----------|
| P0 | Fix overly permissive NSG rules | Low | Critical | Immediate |
| P0 | Enable Azure SQL geo-replication | Medium | Critical | 1 week |
| P1 | Purchase Reserved Instances | Low | High | 1 month |
| P1 | Enable Microsoft Defender for all | Low | High | 1 week |
| P1 | Implement Azure Key Vault for all secrets | Medium | High | 2 weeks |
| P2 | Enable Azure Hybrid Benefit | Low | Medium | 1 week |
| P2 | Implement comprehensive backup policy | Medium | Medium | 2 weeks |
| P3 | Right-size VMs per Advisor | Medium | Medium | Ongoing |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- DS-01 (Framework Application - Azure Well-Architected)
- DS-06 (Prioritization and Severity Guidance)
- RT-05 (Evidence-Based Reasoning)

**Related Prompts:**
- cloud_aws_architecture_review.md - For multi-cloud comparison
- cloud_gcp_best_practices.md - For GCP comparison
- cloud_cost_optimization.md - For deeper cost analysis
- cloud_security_review.md - For comprehensive security audit
- devops_infrastructure_as_code_review.md - For ARM/Bicep review

**Customization Guide:**
- **For .NET Workloads**: Emphasize App Service, Azure SQL, Application Insights integration
- **For Enterprise**: Focus on Azure Landing Zones, Express Route, Azure AD integration
- **For Hybrid Cloud**: Add Azure Arc, Azure Stack, and hybrid networking patterns
- **For SAP Workloads**: Include SAP-certified configurations, HANA Large Instances
- **For Government/Regulated**: Emphasize Azure Government, compliance controls, Azure Policy
