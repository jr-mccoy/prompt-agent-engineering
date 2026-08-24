---
title: "OKR (Objectives and Key Results) Analysis for Codebase"
category: business-analysis
description: "Analyze a codebase to align its features and capabilities with potential business Objectives and Key Results (OKRs)"
techniques:
  - ST-01
  - ST-02
  - DS-01
  - DS-06
  - RT-02
  - QA-02
difficulty: advanced
tags:
  - analysis
  - business-analysis
  - okr
  - strategic-alignment
  - roadmap
updated: "2026-01-25"
related_prompts:
  - domain-business-strategy/analysis/swot_analysis.md
  - domain-business-strategy/analysis/business_impact_analysis.md
  - domain-engineering-workflows/workflows/engineering_delivery_sprint_planner.md
---

# OKR (Objectives and Key Results) Analysis for Codebase

**Objective:** Analyze the codebase to align its features and capabilities with potential business Objectives and Key Results (OKRs).

## When to Use

- Use when: Planning quarterly or annual engineering roadmaps
- Use when: Aligning technical work with business goals for leadership communication
- Use when: Evaluating product-market fit through technical lens
- Use when: Justifying development investments with business impact
- Don't use when: Business OKRs are already well-defined (start from those instead)
- Don't use when: The codebase is too early-stage to infer business objectives

**Instructions:**

1. Review the codebase and identify key features, functionalities, and architectural decisions.

2. Based on the codebase analysis, infer potential high-level business objectives that the code might support. For each objective:
   a. Formulate a clear, ambitious yet achievable objective statement.
   b. Identify 3-5 key results that would indicate progress towards this objective.
   c. Explain how specific aspects of the code contribute to these key results.

3. Consider the following categories of objectives:
   - User Acquisition and Growth
   - User Engagement and Retention
   - Revenue Generation
   - Operational Efficiency
   - Product Innovation
   - Market Expansion

4. For each set of OKRs:
   a. Evaluate how well the current codebase supports achieving the key results.
   b. Identify any gaps or limitations in the code that might hinder achieving the OKRs.
   c. Suggest potential code improvements or new features that could better support the OKRs.

5. Analyze the overall alignment of the codebase with the inferred OKRs:
   - Are there features that don't clearly contribute to any of the key results?
   - Are there important OKRs that lack sufficient support in the current codebase?

6. Propose a prioritized list of development initiatives that would improve the codebase's alignment with the most critical OKRs.

7. **CRITICAL: Validate OKR Inferences**
   - Cross-reference inferred objectives with any available business documentation
   - Verify code evidence actually supports the claimed capability level
   - **Assign confidence level:** High/Medium/Low for each OKR alignment score
   - Distinguish between "feature exists" vs "feature works well"

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Claim high alignment based on feature presence without verifying completeness
- Infer business objectives that have no code evidence (pure speculation)
- Over-report alignment percentages without explaining methodology
- Assume all code features are intentionally supporting business goals
- Create OKRs that are too generic to be actionable
- Report "gaps" for features that may be intentionally out of scope

✅ **DO:**
- Cite specific code paths, configurations, or architectures for each alignment claim
- Label inferred OKRs with confidence: High (clear evidence), Medium (implied), Low (speculative)
- Explain the gap analysis methodology (what counts as "support" vs "gap")
- Acknowledge limitations (e.g., "Unable to assess KR without access to analytics data")
- Validate gaps are actually gaps, not intentional product decisions
- Include stakeholder validation recommendations for key inferences

**Expected Output:** A comprehensive analysis of how the codebase aligns with potential business OKRs, including:
- A set of inferred Objectives and Key Results based on the codebase capabilities
- An evaluation of how well the code supports each OKR with **confidence levels**
- Identified gaps and limitations in the current implementation
- Prioritized suggestions for code improvements or new features to better support critical OKRs
- **Alignment scores** with methodology explanation
- **Validation recommendations** for key inferences

This analysis should provide insights into how the technical implementation aligns with potential business goals and guide future development priorities.

**Example Output:**

```markdown
## OKR Alignment Analysis: Analytics Dashboard Platform

### Executive Summary
The codebase strongly supports User Engagement (85% alignment) and Operational Efficiency (78%) objectives, but has significant gaps in Revenue Generation (45%) and Market Expansion (35%) capabilities.

---

### Inferred OKRs Based on Codebase Analysis

---

## Objective 1: Increase User Engagement and Retention
*"Make our platform indispensable for daily decision-making"*

### Key Results

| KR# | Key Result | Target | Code Support | Gap Analysis |
|-----|------------|--------|--------------|--------------|
| 1.1 | Increase daily active users by 40% | 40% | 85% | Minor |
| 1.2 | Improve user session duration to 15 min avg | 15 min | 70% | Moderate |
| 1.3 | Achieve NPS score of 50+ | 50 | 60% | Moderate |
| 1.4 | Reduce churn rate to <5% monthly | 5% | 45% | Significant |

### Code Evidence

**Supporting KR 1.1 (DAU):**
```typescript
// Real-time dashboard updates
const DashboardWidget: React.FC = () => {
  const { data, isLoading } = useRealTimeData(widgetId, {
    refreshInterval: 30000,  // 30-second auto-refresh
    websocket: true          // WebSocket for instant updates
  });
  // Drives daily check-ins
};
```

**Supporting KR 1.2 (Session Duration):**
```typescript
// Interactive data exploration
const DataExplorer = () => {
  const [filters, setFilters] = useState(defaultFilters);
  const [visualization, setVisualization] = useState('chart');
  // Drill-down, filtering, and visualization options
  // Encourages deeper engagement
};
```

**Gap for KR 1.4 (Churn):**
- No onboarding flow detected in codebase
- Missing user health scoring system
- No automated re-engagement triggers

### Recommendations
1. **Add Onboarding Module** - Guided first-time user experience
2. **Implement Health Scoring** - Track user engagement signals
3. **Build Notification System** - Re-engagement for dormant users

---

## Objective 2: Drive Revenue Growth
*"Expand monetization while delivering clear ROI to customers"*

### Key Results

| KR# | Key Result | Target | Code Support | Gap Analysis |
|-----|------------|--------|--------------|--------------|
| 2.1 | Increase ARPU by 25% | 25% | 40% | Significant |
| 2.2 | Launch enterprise tier with 100 customers | 100 | 30% | Critical |
| 2.3 | Achieve 20% upsell rate | 20% | 55% | Moderate |
| 2.4 | Reduce CAC payback to <12 months | 12 mo | 50% | Moderate |

### Code Evidence

**Partially Supporting KR 2.1 (ARPU):**
```typescript
// Basic subscription management exists
const plans = {
  starter: { price: 29, dashboards: 3, users: 5 },
  professional: { price: 79, dashboards: 10, users: 20 },
  // Missing: enterprise tier, usage-based pricing
};
```

**Gap for KR 2.2 (Enterprise):**
Missing enterprise-critical features:
- ❌ SSO/SAML authentication
- ❌ Audit logging
- ❌ Role-based access control (RBAC)
- ❌ Data residency controls
- ✓ API access (partial)

### Recommendations
1. **Implement RBAC** - Required for enterprise sales (est. 3 weeks)
2. **Add SSO Integration** - Okta, Azure AD support (est. 2 weeks)
3. **Build Audit Log** - Compliance requirement (est. 1 week)
4. **Usage-Based Pricing** - Track API calls, data processed

---

## Objective 3: Achieve Operational Excellence
*"Scale efficiently while maintaining quality"*

### Key Results

| KR# | Key Result | Target | Code Support | Gap Analysis |
|-----|------------|--------|--------------|--------------|
| 3.1 | Reduce infrastructure costs by 30% | 30% | 65% | Moderate |
| 3.2 | Achieve 99.9% uptime | 99.9% | 80% | Minor |
| 3.3 | Deploy daily with zero downtime | Daily | 90% | Minor |
| 3.4 | Reduce P1 incidents to <2/month | <2 | 70% | Moderate |

### Code Evidence

**Supporting KR 3.3 (Deployment):**
```yaml
# .github/workflows/deploy.yml
name: Production Deploy
on:
  push:
    branches: [main]
jobs:
  deploy:
    steps:
      - run: npm test
      - run: npm run build
      - uses: aws-actions/ecs-deploy@v1
        with:
          cluster: production
          service: api
          # Blue-green deployment enabled
```

**Supporting KR 3.2 (Uptime):**
```typescript
// Health check and circuit breaker patterns
@HealthCheck()
async checkDatabase(): Promise<HealthIndicatorResult> {
  return this.db.pingCheck('database', { timeout: 300 });
}

@CircuitBreaker({ threshold: 5, timeout: 30000 })
async callExternalAPI(request: APIRequest): Promise<APIResponse> {
  // Prevents cascade failures
}
```

---

## Objective 4: Expand Market Reach
*"Become the analytics platform of choice globally"*

### Key Results

| KR# | Key Result | Target | Code Support | Gap Analysis |
|-----|------------|--------|--------------|--------------|
| 4.1 | Launch in 5 new countries | 5 | 25% | Critical |
| 4.2 | Support 10 languages | 10 | 20% | Critical |
| 4.3 | Achieve SOC2 Type II certification | Yes | 40% | Significant |
| 4.4 | Integrate with 20 new data sources | 20 | 75% | Minor |

### Code Evidence

**Gap for KR 4.1 & 4.2 (Internationalization):**
```typescript
// i18n not implemented
const WelcomeMessage = () => (
  <h1>Welcome to Dashboard</h1>  // Hardcoded English
);

// Currency handling missing
const formatPrice = (amount: number) =>
  `$${amount.toFixed(2)}`;  // USD only
```

**Partially Supporting KR 4.3 (SOC2):**
- ✓ Encryption at rest (AES-256)
- ✓ Encryption in transit (TLS 1.3)
- ❌ Audit logging
- ❌ Access reviews
- ❌ Incident response documentation

---

### OKR Alignment Summary

```
Alignment Score by Objective:

User Engagement   ████████░░ 80%
Revenue Growth    ████░░░░░░ 45%
Operational       ████████░░ 78%
Market Expansion  ███░░░░░░░ 35%

Overall Alignment: 60%
```

### Prioritized Development Roadmap

| Priority | Initiative | OKR Impact | Effort | ROI |
|----------|------------|------------|--------|-----|
| P0 | Implement RBAC | O2 (Revenue) | 3 weeks | High |
| P0 | Add SSO/SAML | O2 (Revenue) | 2 weeks | High |
| P1 | Build audit logging | O2, O4 | 1 week | High |
| P1 | User onboarding flow | O1 (Engagement) | 2 weeks | Medium |
| P2 | i18n framework | O4 (Expansion) | 4 weeks | Medium |
| P2 | Usage-based billing | O2 (Revenue) | 3 weeks | Medium |
| P3 | Health scoring | O1 (Engagement) | 2 weeks | Low |

### Gap Analysis Matrix

| Feature | O1 | O2 | O3 | O4 | Priority |
|---------|----|----|----|----|----------|
| RBAC | | ★★★ | ★ | ★★ | P0 |
| SSO | | ★★★ | | ★★ | P0 |
| Audit Log | | ★★ | ★★ | ★★★ | P1 |
| Onboarding | ★★★ | ★ | | | P1 |
| i18n | | | | ★★★ | P2 |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Defines purpose of OKR alignment analysis
- ST-02 (Structured Sequential Instructions) - Guides through systematic OKR mapping
- DS-01 (Framework Application) - Applies OKR framework to codebase evaluation
- DS-06 (Prioritization and Severity Guidance) - Prioritizes gaps and initiatives
- RT-02 (Multi-Dimensional Analysis) - Evaluates across engagement, revenue, operations, expansion
- QA-02 (Adversarial Thinking) - False-positive prevention ensures evidence-based alignment claims

## Related Prompts

- [swot_analysis.md](swot_analysis.md) - Complementary strategic analysis
- [business_impact_analysis.md](business_impact_analysis.md) - Quantify business impact of technical decisions
- engineering_delivery_sprint_planner.md - Plan sprints based on OKR priorities