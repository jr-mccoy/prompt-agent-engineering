---
title: "BCG Growth-Share Matrix Analysis for Codebase"
category: business-analysis
description: "Analyze a codebase and its product portfolio using the BCG Growth-Share Matrix to assess resource allocation, identify growth opportunities, and optimize investment decisions"
techniques:
  - ST-01
  - ST-02
  - DS-01
  - RT-02
  - QA-02
difficulty: intermediate
tags:
  - analysis
  - business-analysis
  - portfolio-strategy
  - resource-allocation
  - product-management
updated: "2026-01-25"
related_prompts:
  - domain-business-strategy/analysis/ansoff_matrix_analysis.md
  - domain-business-strategy/analysis/product_market_fit_analysis.md
---

# BCG Growth-Share Matrix Analysis for Codebase

**Objective:** Analyze the codebase and its associated product portfolio using the BCG Growth-Share Matrix to assess resource allocation and identify growth opportunities.

## When to Use

- Use when: Evaluating where to allocate engineering resources across multiple products/features
- Use when: Planning product lifecycle decisions (invest, maintain, sunset)
- Use when: Presenting portfolio strategy to leadership or investors
- Use when: Deciding which features to prioritize in a multi-product codebase
- Use when: Assessing acquired codebases with multiple revenue streams
- Don't use when: Analyzing a single-product codebase (BCG requires portfolio comparison)
- Don't use when: Evaluating code quality (use quality analysis prompts)

**Instructions:**

1. Review the codebase and identify the key products or features it supports.

2. For each product or feature, analyze its position within the BCG Growth-Share Matrix:

   a. Relative Market Share:
      - How does the product's market share compare to that of its largest competitor?
      - Is the product a market leader or a follower?

   b. Market Growth Rate:
      - How fast is the market for this product growing?
      - Is the market in a high-growth or low-growth phase?

3. Based on the analysis, classify each product or feature into one of the four categories:

   a. Stars (High Market Share, High Market Growth):
      - These products are market leaders in high-growth markets.
      - They require significant investment to maintain their position.

   b. Cash Cows (High Market Share, Low Market Growth):
      - These products are market leaders in mature, slow-growth markets.
      - They generate significant cash flow that can be used to fund other products.

   c. Question Marks (Low Market Share, High Market Growth):
      - These products have low market share in high-growth markets.
      - They require investment to increase market share, with the potential to become stars.

   d. Dogs (Low Market Share, Low Market Growth):
      - These products have low market share in slow-growth markets.
      - They may generate little profit and consume resources that could be better used elsewhere.

4. Evaluate the overall balance and sustainability of the product portfolio.

5. Identify potential strategies for each product category (e.g., invest, maintain, harvest, divest).

6. **CRITICAL: Verify Each Classification**
   - Support market share claims with actual data or clearly label as estimates
   - Distinguish between code metrics (e.g., feature usage) and actual market position
   - **Assign confidence levels:** High/Medium/Low for each quadrant placement
   - Cross-reference multiple data sources before classifying products

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Classify products based solely on code complexity or development effort
- Assume "high usage features" equals "high market share" (they measure different things)
- Label mature products as "Dogs" just because they're stable and not changing
- Put every new feature in "Question Marks" without market growth data
- Use company revenue instead of relative market share (BCG specifically requires relative share)
- Confuse feature adoption within your product with market share in the broader market

✅ **DO:**
- Use relative market share (your share ÷ largest competitor's share), not absolute share
- Cite specific data sources for market growth rates (industry reports, analyst data)
- Distinguish between "internal product metrics" and "external market position"
- Rate confidence for each quadrant placement: High (data-backed), Medium (inferred), Low (hypothesis)
- Consider the portfolio as a whole—a healthy portfolio needs cash cows to fund stars
- Include code-based evidence for investment recommendations (what needs to change)

**Expected Output:** A comprehensive BCG Growth-Share Matrix analysis of the codebase and its associated product portfolio, including:
- Classification of each product/feature with **confidence ratings**
- Visual matrix with relative positioning
- Assessment of portfolio balance and health
- Investment recommendations with code-level action items
- Resource allocation strategy tied to engineering capacity

**Example Output:**

```markdown
## BCG Matrix Analysis: SaaS Analytics Platform

### Executive Summary
The product portfolio shows concerning imbalance: strong Cash Cow (Core Analytics) funding two Question Marks with limited Star presence. Strategic decision required on Question Mark investments within Q2 to prevent resource drain. Recommendation: Accelerate Predictive Analytics to Star status, sunset Real-Time Dashboard.

### Portfolio Overview

```
                    RELATIVE MARKET SHARE
                 High (>1.0)           Low (<1.0)
           ┌─────────────────────┬─────────────────────┐
    High   │     ★ STARS         │   ? QUESTION MARKS  │
    (>10%) │                     │                     │
           │  ┌───────────────┐  │  ┌───────────────┐  │
  MARKET   │  │ Predictive    │  │  │ Real-Time     │  │
  GROWTH   │  │ Analytics     │  │  │ Dashboard     │  │
  RATE     │  │ (★ 0.8 → 1.2) │  │  │ (? 0.3)       │  │
           │  └───────────────┘  │  └───────────────┘  │
           │                     │  ┌───────────────┐  │
           │                     │  │ AI Insights   │  │
           │                     │  │ (? 0.4)       │  │
           │                     │  └───────────────┘  │
           ├─────────────────────┼─────────────────────┤
    Low    │    $ CASH COWS      │     🐕 DOGS         │
    (<10%) │                     │                     │
           │  ┌───────────────┐  │  ┌───────────────┐  │
           │  │ Core          │  │  │ Legacy        │  │
           │  │ Analytics     │  │  │ Reports       │  │
           │  │ ($ 2.1)       │  │  │ (🐕 0.2)      │  │
           │  └───────────────┘  │  └───────────────┘  │
           │  ┌───────────────┐  │                     │
           │  │ Data          │  │                     │
           │  │ Warehouse     │  │                     │
           │  │ ($ 1.8)       │  │                     │
           │  └───────────────┘  │                     │
           └─────────────────────┴─────────────────────┘

Legend: (category relative_market_share)
```

---

### Product Classifications

#### ★ STARS: High Share, High Growth

##### Predictive Analytics Module
**Classification Confidence:** Medium → moving to High

| Metric | Value | Source |
|--------|-------|--------|
| Relative Market Share | 0.8x (vs. DataRobot) | Internal estimates + Gartner |
| Market Growth Rate | 23% CAGR | Gartner Analytics Report 2026 |
| Revenue Contribution | 18% ($4.2M ARR) | Finance dashboard |
| Engineering Investment | 35% of team | Jira capacity planning |

**Code Evidence:**
```typescript
// src/predictive/ - Active development area
src/predictive/
├── models/           // 12 ML models, 8 added in last 6 months
├── pipelines/        // AutoML pipeline (competitive advantage)
├── explainability/   // SHAP integration (differentiation)
└── api/
    ├── v1/           // Legacy API
    └── v2/           // New API with streaming predictions

// Feature velocity: 3.2 features/month (highest in portfolio)
// Technical debt ratio: 12% (healthy)
```

**Strategic Implication:**
- Close to Star threshold (1.0x share) - accelerate to cross
- High market growth justifies continued heavy investment
- Code shows active development and competitive features

**Recommendation:** INVEST HEAVILY
- Increase engineering allocation from 35% → 45%
- Prioritize AutoML completion (Q2 target)
- Focus on enterprise features to win larger deals

---

#### $ CASH COWS: High Share, Low Growth

##### Core Analytics Dashboard
**Classification Confidence:** High

| Metric | Value | Source |
|--------|-------|--------|
| Relative Market Share | 2.1x (vs. Looker) | IDC Report 2025 |
| Market Growth Rate | 5% CAGR | Mature BI market |
| Revenue Contribution | 52% ($12.1M ARR) | Finance dashboard |
| Engineering Investment | 15% of team | Maintenance mode |

**Code Evidence:**
```typescript
// src/core-analytics/ - Stable, mature codebase
// Last major feature: 14 months ago
// Code churn: 2.3% monthly (very stable)

// Technical indicators of Cash Cow:
src/core-analytics/
├── dashboard/        // 847 components, 94% test coverage
├── visualizations/   // 45 chart types (comprehensive)
├── exports/          // PDF, Excel, CSV (feature complete)
└── sharing/          // Slack, email, embed (feature complete)

// Dependency graph shows minimal changes needed
// Performance: 99.97% uptime, P50 < 100ms
```

**Strategic Implication:**
- Primary cash generator—protect this revenue
- Low investment needs; harvest for funding Stars
- Code maturity allows minimal maintenance team

**Recommendation:** MAINTAIN & HARVEST
- Reduce engineering allocation to 12%
- Focus on security patches and stability only
- Allocate freed resources to Predictive Analytics

##### Data Warehouse Connector Hub
**Classification Confidence:** High

| Metric | Value | Source |
|--------|-------|--------|
| Relative Market Share | 1.8x (vs. Fivetran) | Company analysis |
| Market Growth Rate | 8% CAGR | Mature ETL market |
| Revenue Contribution | 22% ($5.1M ARR) | Finance dashboard |
| Engineering Investment | 18% of team | Mostly integrations |

**Code Evidence:**
```typescript
// src/connectors/ - Extensive but stable
const CONNECTOR_COUNT = 127;  // Industry-leading
const CONNECTOR_CATEGORIES = ['database', 'saas', 'files', 'streaming'];

// New connector development: 2/month (maintenance pace)
// Most effort: Keeping pace with API changes from sources
```

**Recommendation:** MAINTAIN
- Current investment level appropriate
- Prioritize connector reliability over new additions
- Consider partnership model for long-tail connectors

---

#### ? QUESTION MARKS: Low Share, High Growth

##### AI-Powered Insights
**Classification Confidence:** Medium

| Metric | Value | Source |
|--------|-------|--------|
| Relative Market Share | 0.4x (vs. ThoughtSpot) | Estimates |
| Market Growth Rate | 31% CAGR | AI Analytics market |
| Revenue Contribution | 4% ($0.9M ARR) | Finance dashboard |
| Engineering Investment | 22% of team | Heavy R&D |

**Code Evidence:**
```typescript
// src/ai-insights/ - Heavy investment, unclear ROI
src/ai-insights/
├── nlp/              // Natural language queries
│   ├── parser/       // Custom NLP (expensive to maintain)
│   └── generator/    // Narrative generation
├── anomaly/          // Anomaly detection
└── recommendations/  // Action recommendations

// Technical concerns:
// - Custom NLP vs. using GPT-4 API (build vs buy decision)
// - 34% technical debt ratio (highest in portfolio)
// - Feature adoption: 12% of users (low engagement)
```

**Strategic Decision Required:**
- High growth market is attractive
- But: Low share AND low adoption signals product-market fit issues
- Investment consuming 22% of resources with 4% revenue return

**Recommendation:** INVEST SELECTIVELY or DIVEST
- Set Q2 milestone: 25% user adoption or pivot
- Replace custom NLP with GPT-4 integration (reduce cost 40%)
- If Q2 milestone missed, reallocate resources to Predictive Analytics

##### Real-Time Dashboard
**Classification Confidence:** High

| Metric | Value | Source |
|--------|-------|--------|
| Relative Market Share | 0.3x (vs. Grafana) | Clear market data |
| Market Growth Rate | 15% CAGR | Observability market |
| Revenue Contribution | 3% ($0.7M ARR) | Finance dashboard |
| Engineering Investment | 8% of team | Limited |

**Code Evidence:**
```typescript
// src/realtime/ - Struggling product
src/realtime/
├── streaming/        // WebSocket implementation
│   └── issues/       // Known scaling issues at >1000 connections
├── widgets/          // 12 widget types (competitors have 40+)
└── alerts/           // Basic alerting (no PagerDuty integration)

// Technical debt: 41% (critical)
// Customer churn: 23% annually (highest in portfolio)
// Competitive gap: Missing key features (multi-source, mobile)
```

**Strategic Decision:**
- Low share in moderately growing market
- Significant feature gap vs. competitors (Grafana, Datadog)
- High technical debt makes catch-up expensive

**Recommendation:** DIVEST
- Stop new feature development immediately
- Migrate remaining customers to partner solution
- Reallocate 8% engineering capacity to Stars

---

#### 🐕 DOGS: Low Share, Low Growth

##### Legacy Reports Module
**Classification Confidence:** High

| Metric | Value | Source |
|--------|-------|--------|
| Relative Market Share | 0.2x (vs. Crystal Reports) | Declining market |
| Market Growth Rate | -3% CAGR | Declining segment |
| Revenue Contribution | 1% ($0.2M ARR) | Finance dashboard |
| Engineering Investment | 2% of team | Bug fixes only |

**Code Evidence:**
```typescript
// src/legacy-reports/ - Technical liability
// Technology: jQuery + PHP (2012 architecture)
// No TypeScript, no tests
// Security scan: 12 medium vulnerabilities

// Customer profile:
// - 23 customers remaining (down from 180 in 2020)
// - Average customer age: 8+ years
// - Most valuable: $45K ARR (will migrate eventually)
```

**Strategic Decision:**
- Declining market + declining share = classic Dog
- Minimal revenue doesn't justify ongoing maintenance risk
- Security vulnerabilities create liability

**Recommendation:** DIVEST IMMEDIATELY
- Set sunset date: Q3 2026
- Proactive migration program for remaining 23 customers
- Offer Core Analytics migration incentive (20% discount year 1)
- Eliminate security liability and engineering distraction

---

### Portfolio Balance Assessment

**Current State:**

| Quadrant | Products | Revenue % | Engineering % | Balance |
|----------|----------|-----------|---------------|---------|
| Stars | 1 (almost) | 18% | 35% | ⚠️ Needs more Stars |
| Cash Cows | 2 | 74% | 33% | ✓ Strong foundation |
| Question Marks | 2 | 7% | 30% | ⚠️ Overinvested |
| Dogs | 1 | 1% | 2% | ✓ Minimal drag |

**Portfolio Health Score: 62/100**

| Factor | Score | Notes |
|--------|-------|-------|
| Cash Cow strength | 18/20 | Strong, but concentration risk |
| Star pipeline | 10/20 | Only 1 near-Star; need more |
| Question Mark conversion | 8/20 | AI Insights struggling |
| Dog management | 16/20 | Legacy overstayed; act now |
| Balance | 10/20 | Too dependent on Cash Cows |

**Key Concern:** Portfolio heavily reliant on mature Cash Cows with weak Star pipeline. If Core Analytics disrupted, limited growth fallback.

---

### Resource Reallocation Plan

**Current Allocation:**
```
Core Analytics:        15% ████████░░░░░░░░░░░░
Data Warehouse:        18% █████████░░░░░░░░░░░
Predictive Analytics:  35% █████████████████░░░
AI Insights:           22% ███████████░░░░░░░░░
Real-Time Dashboard:    8% ████░░░░░░░░░░░░░░░░
Legacy Reports:         2% █░░░░░░░░░░░░░░░░░░░
```

**Recommended Allocation (Q2):**
```
Core Analytics:        12% ██████░░░░░░░░░░░░░░  (-3%)
Data Warehouse:        15% ████████░░░░░░░░░░░░  (-3%)
Predictive Analytics:  45% ██████████████████████ (+10%)
AI Insights:           15% ████████░░░░░░░░░░░░  (-7%) [milestone-gated]
Real-Time Dashboard:    0% ░░░░░░░░░░░░░░░░░░░░  (-8%) [sunset]
Legacy Reports:         0% ░░░░░░░░░░░░░░░░░░░░  (-2%) [sunset]
New Star Initiative:   13% ███████░░░░░░░░░░░░░  (reserved)
```

---

### Action Items

**Immediate (This Quarter):**

| Action | Product | Impact | Engineering Cost |
|--------|---------|--------|------------------|
| Stop Real-Time development | Dog→Sunset | Free 8% capacity | 0 (savings) |
| Sunset Legacy Reports | Dog→Divest | Eliminate liability | 2 weeks migration |
| Accelerate Predictive ML | Question→Star | Path to leadership | +3 engineers |

**Next Quarter:**

| Action | Product | Decision Gate | Investment |
|--------|---------|---------------|------------|
| AI Insights go/no-go | Question Mark | 25% adoption | Conditional |
| New Star exploration | Portfolio gap | Market analysis | 13% reserved |
| Cash Cow optimization | Cash Cows | Margin improvement | -6% total |

**Annual Strategy:**
- Graduate Predictive Analytics to clear Star (>1.0x share)
- Launch 1 new Star candidate from reserved capacity
- Maintain Cash Cow margins while reducing investment
- Achieve portfolio balance: 25% Stars, 50% Cash Cows, 25% Question Marks
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Defines purpose of portfolio analysis from codebase
- ST-02 (Structured Sequential Instructions) - Guides systematic quadrant classification
- DS-01 (Framework Application) - Applies proven BCG Growth-Share Matrix framework
- RT-02 (Multi-Dimensional Analysis) - Evaluates products across market share and growth dimensions
- QA-02 (Adversarial Thinking) - False-positive prevention ensures evidence-based classifications
- CM-01 (Explicit Context Framing) - Frames technical analysis within portfolio strategy context

## Related Prompts

- [ansoff_matrix_analysis.md](ansoff_matrix_analysis.md) - Growth strategy options for Stars and Question Marks
- [product_market_fit_analysis.md](product_market_fit_analysis.md) - Validate Question Mark potential before investing
- [business_impact_analysis.md](business_impact_analysis.md) - Quantify portfolio rebalancing impact
