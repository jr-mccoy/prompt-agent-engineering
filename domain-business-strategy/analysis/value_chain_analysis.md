---
title: "Value Chain Analysis for Codebase"
category: business/analysis
description: "Apply Porter's Value Chain framework to analyze how a codebase/product supports primary and support activities, identifying opportunities to enhance value creation and competitive advantage"
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - ST-04  # Delimited Sections
  - DS-01  # Framework Application
  - RT-02  # Multi-Dimensional Analysis
  - QA-02  # Adversarial Thinking
difficulty: advanced
tags:
  - strategic-analysis
  - value-creation
  - business-analysis
  - framework
  - competitive-advantage
updated: "2026-01-25"
related_prompts:
  - domain-business-strategy/analysis/porters_five_forces_analysis.md
  - domain-business-strategy/analysis/business_model_canvas_analysis.md
  - domain-business-strategy/analysis/mckinsey_7s_analysis.md
---

# Value Chain Analysis for Codebase

**Objective:** Analyze the codebase to understand how it fits into and supports the organization's value chain—the sequence of activities (primary and support) that create and deliver value to customers. Identify where the codebase creates competitive advantage and where it may be limiting value creation.

## When to Use

- **Use when:** Evaluating a codebase's strategic importance to the overall business
- **Use when:** Deciding where to invest engineering resources for maximum business impact
- **Use when:** Analyzing build vs. buy decisions for different system components
- **Use when:** Assessing technical debt impact on business value creation
- **Don't use when:** Analyzing pure technical quality (use code quality analysis instead)
- **Don't use when:** The codebase is a standalone product with no organizational context
- **Don't use when:** You need competitive analysis (use Porter's Five Forces instead)

## Instructions

1. **Understand the Business Context (Required First)**
   - Document the organization's value proposition and target customers
   - Identify the key business outcomes the codebase supports
   - Map the high-level flow from inputs to customer value delivery
   - Note any stated strategic priorities or competitive positioning

2. **Map Codebase to Primary Activities**

   **a. Inbound Logistics:**
   - How does the code handle data or resource inputs?
   - Are there features for data acquisition, validation, or initial processing?
   - How efficient and reliable is the input processing?
   - **Evaluate:** Does the codebase create advantage in sourcing/receiving inputs?

   **b. Operations:**
   - What are the core processing or transformation functions?
   - How does the code support the main business operations?
   - What is the throughput, reliability, and quality of core processing?
   - **Evaluate:** Does the codebase create operational excellence or competitive advantage?

   **c. Outbound Logistics:**
   - How does the code manage output or delivery of results?
   - Are there features for data export, reporting, or product delivery?
   - How does the system ensure timely and accurate delivery?
   - **Evaluate:** Does the codebase enable superior delivery to customers?

   **d. Marketing and Sales:**
   - Does the code include features that support marketing efforts?
   - Are there components that facilitate sales processes or customer acquisition?
   - Does the product itself serve as a marketing vehicle (PLG)?
   - **Evaluate:** Does the codebase enhance customer acquisition and conversion?

   **e. Service (Post-Sale):**
   - How does the code support customer service or after-sales support?
   - Are there features for user feedback, issue tracking, or support management?
   - Does the system enable proactive customer success?
   - **Evaluate:** Does the codebase create differentiation through superior service?

3. **Map Codebase to Support Activities**

   **f. Procurement:**
   - Does the code interface with systems for acquiring resources or services?
   - Are there features for managing suppliers, vendors, or third-party integrations?
   - **Evaluate:** Does the codebase optimize procurement costs or efficiency?

   **g. Technology Development:**
   - What innovative or unique technological aspects does the code implement?
   - How does the codebase leverage or advance technology in its domain?
   - Is the architecture enabling or limiting future innovation?
   - **Evaluate:** Does the codebase create technology-based competitive advantage?

   **h. Human Resource Management:**
   - Does the code support HR functions or employee productivity?
   - Are there features for performance tracking, training, or collaboration?
   - **Evaluate:** Does the codebase enhance workforce effectiveness?

   **i. Firm Infrastructure:**
   - How does the code support overall business management and strategy?
   - Are there features for analytics, reporting, or decision support?
   - Does the system provide visibility into business performance?
   - **Evaluate:** Does the codebase enable better management decisions?

4. **Analyze Linkages and Integration**
   - How well does the code facilitate flow between value chain activities?
   - Are there bottlenecks or inefficiencies in the linkages?
   - Does the system enable coordination across activities?
   - Are there opportunities for better integration?

5. **CRITICAL: Verify Strategic Claims Before Reporting**
   - For each "competitive advantage" claim, provide specific evidence
   - Distinguish between "adequate" and "advantage-creating"
   - Consider what competitors likely have—is this truly differentiating?
   - Validate that technical capabilities translate to business value

6. **Identify Strategic Opportunities**
   - Which value chain activities are supported strongly vs. weakly?
   - Where could codebase improvements create the most business value?
   - Are there activities that should be built in-house vs. outsourced?
   - What technical debt is most impacting value creation?

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Claim "competitive advantage" for table-stakes capabilities
- Assume technical excellence = business value (they don't always correlate)
- Map every feature to a value chain activity (some features may not be strategic)
- Ignore the cost side of the value equation (value = benefits - costs)
- Assume the codebase is the only contributor to value chain activities
- Conflate "the code can do X" with "X creates value"

✅ **DO:**
- Distinguish between "supports" and "creates advantage in" for each activity
- Ground value claims in customer outcomes, not just feature existence
- Consider the full system (code + process + people) when assessing value creation
- Acknowledge when an activity is table-stakes vs. differentiating
- Validate that technical capabilities are actually used and valued by customers
- Consider total cost of ownership, not just feature capability

## Confidence Levels

Rate each value chain assessment with a confidence level:

- **High Confidence:** Direct evidence links codebase capabilities to customer value outcomes; competitive comparison validates differentiation; business metrics support the assessment
- **Medium Confidence:** Logical connection between capability and value; limited competitive comparison; assumed but not validated customer value
- **Low Confidence:** Theoretical value connection; no competitive benchmark; capability exists but usage/value uncertain

## Expected Output

A comprehensive Value Chain analysis including:
- Visual mapping of codebase to value chain activities
- Assessment of value contribution for each activity
- Identification of competitive advantages and gaps
- Strategic recommendations for value enhancement
- Confidence ratings for all assessments

### Output Format

```markdown
## Value Chain Analysis: [Product/Codebase Name]

### Executive Summary
[3-5 sentences summarizing the codebase's role in value creation and key opportunities]

### Value Chain Visualization

```
SUPPORT ACTIVITIES
┌─────────────────────────────────────────────────────────────────────────────┐
│ Firm Infrastructure: [Assessment]                               │ MARGIN  │
├─────────────────────────────────────────────────────────────────┤         │
│ Human Resource Management: [Assessment]                         │         │
├─────────────────────────────────────────────────────────────────┤         │
│ Technology Development: [Assessment]                            │         │
├─────────────────────────────────────────────────────────────────┤         │
│ Procurement: [Assessment]                                       │         │
└─────────────────────────────────────────────────────────────────┤         │
PRIMARY ACTIVITIES                                                 │         │
┌──────────┬───────────┬───────────┬──────────┬──────────┐        │         │
│ Inbound  │           │ Outbound  │Marketing │          │        │         │
│ Logistics│ Operations│ Logistics │ & Sales  │ Service  │────────│         │
│          │           │           │          │          │        │         │
│ [Rating] │ [Rating]  │ [Rating]  │ [Rating] │ [Rating] │        │         │
└──────────┴───────────┴───────────┴──────────┴──────────┴────────┴─────────┘
```

### Primary Activities Analysis

#### Inbound Logistics
**Codebase Support:** [How the code supports this activity]
**Value Contribution:** Table-Stakes | Supports | Enables Advantage
**Evidence:** [Specific capabilities and their impact]
**Confidence:** High | Medium | Low
**Opportunities:** [Improvements that would enhance value]

[Repeat for each primary activity]

### Support Activities Analysis

[Same format for support activities]

### Linkages Analysis

| From Activity | To Activity | Integration Quality | Value Impact |
|---------------|-------------|---------------------|--------------|
| Inbound | Operations | Strong | Smooth data flow |

### Competitive Advantage Assessment

| Activity | Our Capability | Competitor Benchmark | Advantage? |
|----------|---------------|---------------------|------------|
| Operations | [Description] | [What competitors have] | Yes/No/Parity |

### Strategic Recommendations

| # | Recommendation | Activity | Impact | Effort |
|---|----------------|----------|--------|--------|
| 1 | [Action] | Operations | High | Medium |
```

## Example Output

```markdown
## Value Chain Analysis: DataPipeline Pro (ETL/Data Integration Platform)

### Executive Summary

DataPipeline Pro creates clear competitive advantage in **Operations** (data transformation) and **Technology Development** (proprietary optimization engine) but is at parity or behind in **Marketing & Sales** (limited self-serve, no PLG motion) and **Service** (reactive support model). The codebase strongly supports core value creation but underinvests in activities that would improve customer acquisition and retention. Key recommendation: invest in product-led growth features and proactive monitoring to convert operational excellence into market advantage.

### Value Chain Visualization

```
SUPPORT ACTIVITIES
┌─────────────────────────────────────────────────────────────────────────────┐
│ Firm Infrastructure: ⚠️ Adequate - basic analytics, limited visibility     │ MARGIN  │
├─────────────────────────────────────────────────────────────────────────────┤         │
│ Human Resource Management: ➖ Minimal - no HR features                      │         │
├─────────────────────────────────────────────────────────────────────────────┤         │
│ Technology Development: ⭐ Strong - proprietary optimization, patents      │         │
├─────────────────────────────────────────────────────────────────────────────┤         │
│ Procurement: ⚠️ Adequate - cloud provider integrations                     │         │
└─────────────────────────────────────────────────────────────────────────────┤         │
PRIMARY ACTIVITIES                                                            │         │
┌──────────┬───────────┬───────────┬──────────┬──────────┐                   │         │
│ Inbound  │           │ Outbound  │Marketing │          │                   │         │
│ Logistics│ Operations│ Logistics │ & Sales  │ Service  │───────────────────┤         │
│          │           │           │          │          │                   │         │
│ ⭐ Strong │ ⭐⭐ Best  │ ⭐ Strong  │ ⚠️ Gap   │ ⚠️ Gap   │                   │         │
└──────────┴───────────┴───────────┴──────────┴──────────┴───────────────────┴─────────┘

Legend: ⭐⭐ Competitive Advantage | ⭐ Strong | ⚠️ Adequate/Gap | ➖ Minimal/N/A
```

---

### Primary Activities Analysis

#### Inbound Logistics
**What This Means:** Receiving, storing, and distributing inputs (for a data platform: connecting to data sources, ingesting data, staging for processing)

**Codebase Support:**
```typescript
// Connector Framework - supports 150+ data sources
src/connectors/
├── databases/       # PostgreSQL, MySQL, Oracle, MongoDB, etc.
├── cloud/          # S3, GCS, Azure Blob, Snowflake, BigQuery
├── streaming/      # Kafka, Kinesis, Pub/Sub
├── apis/           # REST, GraphQL, SOAP adapters
└── files/          # CSV, JSON, Parquet, Avro, XML

// Key capabilities:
- Parallel ingestion with adaptive rate limiting
- Schema inference and drift detection
- Incremental extraction with change data capture (CDC)
- Connection pooling and credential management
```

**Value Contribution:** ⭐ **Strong** (Supports Value)

**Evidence:**
- 150+ connectors vs. industry average of 80-100
- CDC capability is competitive table-stakes (Fivetran, Airbyte have similar)
- Customer feedback: "Connection setup is straightforward" (common, not differentiating)
- Schema drift detection reduces data quality issues (valuable but competitors have similar)

**Confidence:** High (verified against competitor capabilities)

**Why Not Advantage:** While comprehensive, connector coverage is now table-stakes. Competitors like Fivetran have similar or better coverage. This is necessary but not differentiating.

**Opportunities:**
- Real-time streaming connectors are limited—Kafka/Kinesis only; adding Flink would differentiate
- No-code connector builder would reduce time-to-value for custom sources

---

#### Operations
**What This Means:** Transforming inputs into outputs (for a data platform: data transformation, cleaning, enrichment, orchestration)

**Codebase Support:**
```python
# Proprietary Optimization Engine
src/engine/
├── optimizer/
│   ├── query_planner.py      # Cost-based optimization
│   ├── partition_pruner.py   # Intelligent partitioning
│   └── parallel_executor.py  # Distributed execution
├── transforms/
│   ├── sql_transforms.py     # SQL-based transformations
│   ├── python_transforms.py  # Python UDFs
│   └── ml_transforms.py      # ML feature engineering
└── quality/
    ├── validators.py         # Data quality rules
    └── profiler.py          # Automatic data profiling

# Performance benchmarks (internal testing):
- 3x faster than Apache Spark for common transforms
- 40% cost reduction through intelligent caching
- 99.7% SLA on scheduled pipelines
```

**Value Contribution:** ⭐⭐ **Competitive Advantage**

**Evidence:**
- Independent benchmark (TPC-DS): 2.8x faster than nearest competitor
- Customer case study: FinanceCorp reduced processing time from 4 hours to 45 minutes
- Patent #US11,234,567: "Adaptive query optimization for heterogeneous data sources"
- Customer retention: 95% in segment where Operations is primary buying criteria
- Pricing power: 20% premium over competitors, justified by performance

**Confidence:** High (third-party benchmark, customer outcomes, patent protection)

**Why This Is Advantage:**
1. Performance is measurably superior and validated by third parties
2. Patent protection creates barrier to competition
3. Customers cite operations/performance as #1 reason for choosing us
4. Enables pricing premium that proves value

**Opportunities:**
- Extend ML feature engineering to real-time (currently batch only)
- Add natural language to SQL for non-technical users

---

#### Outbound Logistics
**What This Means:** Delivering outputs to destinations (for a data platform: data delivery, API access, reverse ETL)

**Codebase Support:**
```typescript
// Delivery Framework
src/delivery/
├── destinations/
│   ├── warehouses/     # Snowflake, BigQuery, Redshift, Databricks
│   ├── databases/      # Operational DB writeback
│   └── apis/           # REST API endpoints, webhooks
├── formats/
│   ├── schema_management.ts  # Automatic schema evolution
│   └── type_coercion.ts      # Cross-platform type mapping
└── orchestration/
    ├── scheduler.ts          # Cron-based scheduling
    ├── dependencies.ts       # DAG-based orchestration
    └── notifications.ts      # Alerting on completion/failure
```

**Value Contribution:** ⭐ **Strong** (Supports Value)

**Evidence:**
- Comprehensive destination coverage (40+ destinations)
- Reverse ETL capability (increasingly important, we were early)
- Schema evolution handling reduces operational burden
- Customer feedback: "Delivery reliability is excellent"

**Confidence:** High (feature parity verified, customer feedback consistent)

**Why Not Advantage:** Good execution but not differentiated. Competitors have similar destination coverage. Reverse ETL was differentiating 2 years ago but is now table-stakes.

**Opportunities:**
- Real-time streaming delivery (currently batch windows minimum 5 min)
- Embedded analytics / semantic layer would extend value beyond "delivery"

---

#### Marketing and Sales
**What This Means:** Activities that enable customers to purchase (for a SaaS platform: self-serve signup, product trials, in-product growth)

**Codebase Support:**
```typescript
// Limited PLG features
src/growth/
├── trial/
│   ├── signup_flow.ts       # Basic email signup
│   └── limits.ts            # Trial limitations
└── billing/
    ├── stripe_integration.ts
    └── usage_metering.ts

// GAPS identified:
// - No in-product onboarding wizard
// - No usage-based upsell prompts
// - No viral/sharing features
// - No freemium tier
// - Trial requires sales contact for extension
```

**Value Contribution:** ⚠️ **Gap** (Limits Acquisition)

**Evidence:**
- Conversion metrics: 2% trial-to-paid (industry benchmark: 5-8% for similar tools)
- Time-to-value: 14 days average (competitors achieve 2-3 days)
- Sales-assisted: 100% of deals require human sales involvement
- Customer feedback: "Took a while to figure out how to get started"

**Confidence:** High (internal metrics compared to industry benchmarks)

**Business Impact:**
- CAC is 2.5x industry average due to sales-heavy motion
- Missing self-serve segment entirely (SMB, developers)
- Growth rate limited by sales headcount, not product

**Opportunities (High Value):**
1. Interactive onboarding wizard (reduce time-to-value to 2 days)
2. Template library for common use cases (accelerate initial success)
3. Usage-based upgrade prompts (product-qualified leads)
4. Freemium tier for individual developers (bottom-up adoption)

---

#### Service
**What This Means:** Activities that maintain and enhance product value after sale (for a SaaS platform: customer support, success, documentation, community)

**Codebase Support:**
```typescript
// Support Features
src/support/
├── help/
│   ├── documentation.ts      # In-product help links
│   └── search.ts             # Doc search
├── diagnostics/
│   ├── error_reporting.ts    # Error logging to support
│   └── debug_mode.ts         # Debug information capture
└── feedback/
    └── nps_survey.ts         # Periodic NPS collection

// GAPS identified:
// - No in-app chat support
// - No proactive health monitoring
// - No customer success automation
// - Error messages are technical, not actionable
// - No self-service troubleshooting wizard
```

**Value Contribution:** ⚠️ **Gap** (Limits Retention)

**Evidence:**
- Support ticket volume: 45 tickets/customer/year (benchmark: 20-30)
- Time to resolution: 8 hours average (benchmark: 2-4 hours)
- NPS by segment: Customers with support issues NPS 32 vs. overall NPS 48
- Churn correlation: 70% of churned customers had 3+ support tickets

**Confidence:** High (internal metrics, churn analysis)

**Business Impact:**
- High support cost per customer ($1,200/year vs. $400 benchmark)
- Churn risk from support experience
- Support team scaling linearly with customer growth (not sustainable)

**Opportunities (High Value):**
1. Proactive pipeline health monitoring with automated alerts
2. Self-service troubleshooting wizard for common issues
3. Improved error messages with resolution steps
4. In-app chat with AI-assisted first response

---

### Support Activities Analysis

#### Firm Infrastructure
**What This Means:** General management, planning, finance, accounting, legal (for a SaaS platform: admin dashboards, billing management, compliance features)

**Codebase Support:**
```typescript
// Admin/Management Features
src/admin/
├── dashboard/
│   ├── usage_metrics.ts      # Basic usage visibility
│   └── billing_admin.ts      # Invoice management
├── compliance/
│   ├── audit_log.ts          # Activity logging
│   └── export.ts             # Data export for compliance
└── settings/
    └── workspace_config.ts   # Basic workspace settings
```

**Value Contribution:** ⚠️ **Adequate** (Table-Stakes)

**Evidence:**
- Audit logging meets SOC2 requirements
- Usage visibility is basic (aggregate only, not per-user/per-pipeline)
- No cost attribution or chargeback features
- Limited multi-tenant administration

**Confidence:** Medium (adequate but not validated against enterprise requirements)

**Opportunities:**
- Granular cost attribution by team/project (enterprise requirement)
- Chargeback reporting for cost allocation
- Advanced RBAC for enterprise governance

---

#### Technology Development
**What This Means:** Activities that improve products and processes (for a tech company: R&D, innovation, patents, technical differentiation)

**Codebase Support:**
```python
# Innovation/R&D Capabilities
src/experimental/
├── ml_optimization/     # ML-based query optimization (research)
├── semantic_layer/      # Next-gen semantic modeling (beta)
└── natural_language/    # NL query interface (prototype)

# Patents & IP:
# - US11,234,567: Adaptive query optimization
# - US11,345,678: Distributed cache coherence for data pipelines
# - 3 pending patents on ML-based optimization

# Architecture for Innovation:
# - Plugin architecture enables experimentation
# - Feature flag system for controlled rollouts
# - Modular design allows component replacement
```

**Value Contribution:** ⭐ **Strong** (Creates Advantage)

**Evidence:**
- Patent portfolio provides legal protection for core innovations
- R&D velocity: shipping 2-3 major features per quarter
- Architecture enables rapid experimentation
- Customer perception: "Most innovative in the space" (analyst reports)

**Confidence:** High (patents verified, shipping velocity measurable)

**Why This Matters:**
Technology Development directly feeds Operations advantage. The optimization engine (Operations) exists because of sustained R&D investment.

**Opportunities:**
- Continue ML optimization research—next breakthrough could extend advantage
- Semantic layer could be next differentiator (market emerging)

---

#### Human Resource Management
**Codebase Support:** Minimal (no HR-specific features; enterprise customers may need SSO/SCIM provisioning)

**Value Contribution:** ➖ **Minimal/N/A**

**Opportunities:** SCIM provisioning for enterprise user management

---

#### Procurement
**What This Means:** Acquiring inputs for value chain (for a SaaS platform: cloud infrastructure, third-party services, data sources)

**Codebase Support:**
```typescript
// Cloud/Vendor Management
src/infrastructure/
├── cloud/
│   ├── aws_integration.ts    # Multi-account AWS support
│   ├── gcp_integration.ts    # GCP integration
│   └── azure_integration.ts  # Azure integration
├── cost/
│   ├── spot_management.ts    # Spot instance optimization
│   └── reserved_instances.ts # RI utilization
└── vendors/
    └── api_keys.ts           # Third-party credential management
```

**Value Contribution:** ⚠️ **Adequate** (Cost Savings)

**Evidence:**
- Spot instance management reduces compute costs 40-60%
- Multi-cloud support avoids vendor lock-in
- No advanced FinOps features (competitors have better cost dashboards)

**Confidence:** Medium

**Opportunities:**
- FinOps dashboard with cost optimization recommendations
- Committed use discount automation

---

### Linkages Analysis

| From Activity | To Activity | Integration Quality | Value Impact | Codebase Support |
|---------------|-------------|---------------------|--------------|------------------|
| Inbound Logistics | Operations | ⭐ Excellent | Seamless data flow | Unified pipeline model |
| Operations | Outbound Logistics | ⭐ Excellent | Efficient delivery | Same pipeline model |
| Operations | Service | ⚠️ Poor | Errors hard to diagnose | Error messages non-actionable |
| Technology Dev | Operations | ⭐ Excellent | Innovations ship to core | Plugin architecture |
| Marketing & Sales | Service | ⚠️ Poor | No feedback loop | No usage→success pipeline |

**Key Linkage Issues:**
1. **Operations → Service gap:** When pipelines fail, customers can't self-diagnose. Error messages are technical, requiring support tickets. This creates support burden and customer frustration.
2. **Marketing & Sales → Service gap:** No product-led customer success. Trial users get no guidance; paid users get no proactive outreach.

---

### Competitive Advantage Assessment

| Activity | Our Capability | Competitor Benchmark | Advantage? |
|----------|---------------|---------------------|------------|
| Inbound Logistics | 150+ connectors, CDC | Fivetran: 200+, CDC | Parity |
| **Operations** | 2.8x perf, patented | Spark-based competitors | **Yes** |
| Outbound Logistics | 40+ destinations, reverse ETL | Similar coverage | Parity |
| Marketing & Sales | Sales-led, 14-day TTV | PLG, 2-day TTV | **Behind** |
| Service | Reactive support | Proactive health | **Behind** |
| Technology Dev | 3 patents, research pipeline | Variable | **Yes** |

**Net Assessment:**
- Core value creation (Operations) is differentiated and protected
- Customer acquisition and retention activities are weaknesses
- Technology pipeline sustains operational advantage

---

### Strategic Recommendations

| # | Recommendation | Activity | Impact | Effort | Priority |
|---|----------------|----------|--------|--------|----------|
| 1 | Build interactive onboarding wizard | Marketing & Sales | High | Medium | P0 |
| 2 | Implement proactive pipeline health monitoring | Service | High | Medium | P0 |
| 3 | Improve error messages with resolution steps | Service (linkage) | Medium | Low | P1 |
| 4 | Add template library for common use cases | Marketing & Sales | Medium | Medium | P1 |
| 5 | Build FinOps cost dashboard | Procurement | Medium | Medium | P2 |
| 6 | Continue ML optimization R&D | Technology Dev | High | High | Ongoing |

**Strategic Priorities:**
1. **Protect the moat:** Continue Operations/Technology advantage through R&D
2. **Fix the gaps:** Marketing & Sales and Service improvements have highest ROI
3. **Improve linkages:** Operations → Service linkage directly impacts retention

---

### Value Creation Summary

**Where We Create Value:**
- Core data transformation (Operations) — this is why customers pay premium
- Technology innovation pipeline — this sustains the moat

**Where We Capture Value:**
- Currently: Enterprise sales motion only
- Missing: Self-serve/PLG segment, customer success expansion

**Value Chain Efficiency:**
- Strong: Inbound → Operations → Outbound (core pipeline)
- Weak: Acquisition → Retention loop (no product-led motion)

**Margin Implication:**
Current architecture supports high margins on operations but high customer acquisition costs due to sales-heavy model. Fixing Marketing & Sales gaps could improve net margins by reducing CAC while growing faster.
```

## Customization Guide

- **For B2B SaaS:** Focus on Operations (core value), Marketing & Sales (acquisition), Service (retention)
- **For Internal Systems:** Firm Infrastructure and HR Management become more relevant
- **For Marketplaces:** Marketing & Sales and Inbound Logistics (supplier acquisition) are critical
- **For Hardware + Software:** Inbound and Outbound Logistics have physical components

## Techniques Used

- **ST-01 (Clear Objective Statement):** Explicit goal of mapping codebase to value chain activities
- **ST-02 (Structured Sequential Instructions):** Systematic activity-by-activity analysis process
- **DS-01 (Framework Application):** Direct application of Porter's Value Chain framework
- **RT-02 (Multi-Dimensional Analysis):** Evaluation across primary and support activities, linkages, and competitive positioning
- **QA-02 (Adversarial Thinking):** False-positive prevention distinguishes "supports" from "creates advantage"

## Related Prompts

- [Porter's Five Forces Analysis](porters_five_forces_analysis.md) - Industry competitive dynamics
- [Business Model Canvas Analysis](business_model_canvas_analysis.md) - Business model evaluation
- [McKinsey 7S Analysis](mckinsey_7s_analysis.md) - Organizational alignment assessment
- [Competitive Positioning Map](competitive_positioning_map.md) - Market positioning analysis
