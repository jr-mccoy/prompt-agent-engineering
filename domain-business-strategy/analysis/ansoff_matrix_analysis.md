---
title: "Ansoff Matrix Analysis for Codebase"
category: business/analysis
description: "Apply the Ansoff Growth Matrix to evaluate strategic growth options for a product/codebase across market penetration, product development, market development, and diversification dimensions"
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - ST-04  # Delimited Sections
  - DS-01  # Framework Application
  - RT-02  # Multi-Dimensional Analysis
  - QA-02  # Adversarial Thinking
difficulty: intermediate
tags:
  - strategic-analysis
  - growth-strategy
  - business-analysis
  - framework
  - market-analysis
updated: "2026-01-25"
related_prompts:
  - domain-business-strategy/analysis/bcg_matrix_analysis.md
  - domain-business-strategy/analysis/blue_ocean_strategy_analysis.md
  - domain-business-strategy/analysis/product_market_fit_analysis.md
---

# Ansoff Matrix Analysis for Codebase

**Objective:** Analyze the codebase using the Ansoff Growth Matrix framework to systematically evaluate potential growth strategies across four quadrants (Market Penetration, Product Development, Market Development, Diversification) and identify the most promising strategic paths based on current capabilities and market position.

## When to Use

- **Use when:** Planning the next phase of product growth and need to evaluate strategic options systematically
- **Use when:** Investors or stakeholders are asking "what's the growth strategy?"
- **Use when:** The product has achieved initial traction and needs to decide where to invest next
- **Use when:** Evaluating build vs. buy decisions for expansion
- **Don't use when:** The product hasn't achieved product-market fit (focus on that first)
- **Don't use when:** You need competitive analysis (use Porter's Five Forces instead)
- **Don't use when:** The business model itself is in question (use Business Model Canvas instead)

## Instructions

1. **Establish Current Position (Required First)**
   - Document the product's current market(s) and customer segments
   - Identify the product's core features and value proposition
   - Assess current market share and competitive position
   - Note the codebase's technical capabilities and constraints

2. **Analyze Each Quadrant**

   **a. Market Penetration (Existing Products, Existing Markets):**
   - What is the current market share? What's the achievable ceiling?
   - How can the codebase enable increased adoption among existing customer segments?
   - What features or improvements would reduce churn and increase usage?
   - Are there pricing, packaging, or go-to-market optimizations possible?
   - **Evidence to collect:** Usage metrics, churn data, feature adoption rates, competitive pricing

   **b. Product Development (New Products, Existing Markets):**
   - What new features or functionalities would serve existing customers better?
   - Are there adjacent problems the current customer base has that the codebase could solve?
   - What does the technical architecture support vs. require significant rework?
   - Are there product line extensions that leverage existing code and infrastructure?
   - **Evidence to collect:** Feature requests, customer interviews, architecture flexibility, competitor features

   **c. Market Development (Existing Products, New Markets):**
   - Are there new customer segments that could use the existing product?
   - Are there geographic markets where the product could expand?
   - Are there vertical industries where the product applies with minimal adaptation?
   - What localization, compliance, or integration work would be required?
   - **Evidence to collect:** Market size data, regulatory requirements, localization effort, channel opportunities

   **d. Diversification (New Products, New Markets):**
   - Are there strategic opportunities that leverage core competencies in new areas?
   - What synergies exist between current capabilities and potential new directions?
   - What are the risks of spreading focus vs. the opportunity cost of not pursuing?
   - Does the codebase architecture support or hinder diversification?
   - **Evidence to collect:** Market research, capability assessment, M&A opportunities, partnership potential

3. **Assess Risk and Resource Requirements**
   - For each quadrant, evaluate:
     - Technical effort required (codebase changes, new development)
     - Market risk (uncertainty, competition, timing)
     - Resource requirements (team, budget, time)
     - Strategic fit (alignment with mission, capabilities)

4. **CRITICAL: Validate Assumptions Before Recommending**
   - For each growth opportunity, identify key assumptions
   - Distinguish between evidence-backed conclusions and hypotheses
   - Note what market validation would be needed before committing
   - Consider scenarios where assumptions prove wrong

5. **Prioritize and Recommend**
   - Rank opportunities by risk-adjusted potential
   - Identify quick wins vs. long-term bets
   - Recommend a balanced portfolio of growth initiatives
   - Define success metrics for each recommended path

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Assume market size = addressable opportunity (market share capture is hard)
- Recommend diversification without acknowledging its high failure rate (~70%)
- Conflate "technically possible" with "strategically wise"
- Ignore the cost of complexity when recommending multiple growth paths
- Present market research as certainty (all market data has uncertainty)
- Recommend growth strategies that exceed organizational execution capacity

✅ **DO:**
- Ground every opportunity in specific evidence (usage data, customer feedback, market research)
- Explicitly state confidence levels and key assumptions for each recommendation
- Acknowledge trade-offs between focus and diversification
- Consider the "do nothing" option as a valid baseline
- Factor in execution risk based on team capabilities and track record
- Recommend validation steps before major investment

## Confidence Levels

Rate each growth opportunity with a confidence level:

- **High Confidence:** Strong evidence from customer data, validated market demand, proven technical feasibility, within team's execution capability
- **Medium Confidence:** Moderate evidence, some market validation needed, technically feasible with effort, stretch for team but achievable
- **Low Confidence:** Limited evidence, significant market uncertainty, technical feasibility uncertain, would require new capabilities

## Expected Output

A comprehensive Ansoff Matrix analysis including:
- Visual matrix positioning current and potential offerings
- Detailed assessment of opportunities within each quadrant
- Risk/reward analysis with confidence ratings
- Prioritized recommendations with resource requirements
- Key assumptions and validation needs

### Output Format

```markdown
## Ansoff Matrix Analysis: [Product Name]

### Executive Summary
[3-5 sentences summarizing the growth opportunity landscape and recommended strategy]

### Current Position
- **Markets Served:** [Description]
- **Products/Features:** [Core offerings]
- **Market Share:** [If known]
- **Key Strengths:** [Competitive advantages]

### Ansoff Matrix Visualization

```
                    EXISTING PRODUCTS          NEW PRODUCTS
                 ┌─────────────────────────┬─────────────────────────┐
                 │                         │                         │
    EXISTING     │   MARKET PENETRATION    │   PRODUCT DEVELOPMENT   │
    MARKETS      │                         │                         │
                 │   Risk: LOW             │   Risk: MEDIUM          │
                 │   [Opportunities]       │   [Opportunities]       │
                 │                         │                         │
                 ├─────────────────────────┼─────────────────────────┤
                 │                         │                         │
    NEW          │   MARKET DEVELOPMENT    │    DIVERSIFICATION      │
    MARKETS      │                         │                         │
                 │   Risk: MEDIUM          │   Risk: HIGH            │
                 │   [Opportunities]       │   [Opportunities]       │
                 │                         │                         │
                 └─────────────────────────┴─────────────────────────┘
```

### Quadrant Analysis

#### Q1: Market Penetration
**Opportunity:** [Description]
**Evidence:** [Supporting data]
**Technical Requirements:** [Codebase changes needed]
**Confidence:** High | Medium | Low
**Key Assumptions:** [What must be true]

[Repeat for Q2, Q3, Q4]

### Risk-Reward Summary

| Quadrant | Opportunity | Potential | Risk | Confidence | Effort |
|----------|-------------|-----------|------|------------|--------|
| Q1 | [Name] | $XM ARR | Low | High | S/M/L |

### Prioritized Recommendations

| # | Strategy | Quadrant | Rationale | Success Metric |
|---|----------|----------|-----------|----------------|
| 1 | [Action] | Q1 | [Why] | [Metric] |

### Key Assumptions & Validation Needs
[What must be validated before committing resources]
```

## Example Output

```markdown
## Ansoff Matrix Analysis: TaskFlow (Project Management SaaS)

### Executive Summary

TaskFlow has strong product-market fit in the SMB segment with a 4.2% market share and healthy 92% retention. The highest-confidence growth opportunity is **Market Penetration** through improved onboarding and team collaboration features, which could increase market share to 6-7% with moderate technical investment. **Product Development** via AI-powered project insights represents a medium-confidence bet that could differentiate from competitors. **Market Development** into enterprise is technically feasible but requires significant sales/compliance investment. **Diversification** into time tracking should be deprioritized despite customer requests—the market is saturated with better-positioned competitors.

### Current Position

- **Markets Served:** SMB companies (10-200 employees) in North America, primarily tech, marketing, and professional services
- **Products/Features:** Task management, team workspaces, Kanban boards, basic reporting, integrations (Slack, Google, Microsoft)
- **Market Share:** ~4.2% of SMB project management market ($2.8B TAM)
- **Key Strengths:** Intuitive UX (NPS 62), fast onboarding (5-min time-to-value), strong integrations, affordable pricing

### Ansoff Matrix Visualization

```
                    EXISTING PRODUCTS          NEW PRODUCTS
                 ┌─────────────────────────┬─────────────────────────┐
                 │                         │                         │
    EXISTING     │   MARKET PENETRATION    │   PRODUCT DEVELOPMENT   │
    MARKETS      │                         │                         │
                 │   Risk: LOW             │   Risk: MEDIUM          │
                 │   ★ Onboarding 2.0      │   ◆ AI Project Insights │
                 │   ★ Team Collaboration  │   ◇ Resource Planning   │
                 │   ★ Mobile Experience   │   ◇ Client Portal       │
                 │                         │                         │
                 ├─────────────────────────┼─────────────────────────┤
                 │                         │                         │
    NEW          │   MARKET DEVELOPMENT    │    DIVERSIFICATION      │
    MARKETS      │                         │                         │
                 │   Risk: MEDIUM          │   Risk: HIGH            │
                 │   ◆ Enterprise Segment  │   ✗ Time Tracking       │
                 │   ◇ LATAM Expansion     │   ✗ CRM Features        │
                 │   ◇ Vertical: Legal     │   ? White-label API     │
                 │                         │                         │
                 └─────────────────────────┴─────────────────────────┘

Legend: ★ Recommended | ◆ Consider | ◇ Monitor | ✗ Deprioritize | ? Needs validation
```

---

### Quadrant Analysis

#### Q1: Market Penetration (Existing Products, Existing Markets)

**Strategic Question:** How do we capture more of our current market with our current product?

---

**Opportunity 1.1: Onboarding 2.0**
- **Description:** Redesign onboarding to reduce time-to-first-completed-project from 3 days to 1 day
- **Evidence:**
  - Churn analysis: 45% of churned users never completed a project
  - Competitor analysis: Monday.com has 1-day time-to-value vs. our 3 days
  - User feedback: "Took too long to see the value" (23% of churn surveys)
- **Technical Requirements:**
  - New onboarding wizard (2 weeks frontend)
  - Sample project templates (1 week content + backend)
  - Progress tracking analytics (1 week)
- **Potential Impact:** Reduce Day-30 churn by 15% = ~$420K ARR saved
- **Confidence:** High
- **Key Assumptions:**
  - Faster time-to-value correlates with retention (validated by churn data)
  - Users will engage with guided onboarding (A/B test needed)

---

**Opportunity 1.2: Team Collaboration Enhancement**
- **Description:** Add real-time presence, @mentions, and inline comments to increase stickiness
- **Evidence:**
  - Feature requests: "Real-time collaboration" is #2 requested feature (847 upvotes)
  - Usage data: Teams with 3+ daily active users have 98% retention vs. 85% for single-user teams
  - Competitor gap: Asana and ClickUp have this; we don't
- **Technical Requirements:**
  - WebSocket infrastructure (exists, needs expansion)
  - Presence indicators (2 weeks)
  - @mentions and notifications (2 weeks)
  - Inline comments (3 weeks)
- **Potential Impact:** Increase team-level adoption = $1.2M ARR opportunity (based on upgrade path modeling)
- **Confidence:** High
- **Key Assumptions:**
  - More collaboration features drive multi-user adoption
  - Technical infrastructure can handle real-time at scale (needs load testing)

---

**Opportunity 1.3: Mobile Experience Upgrade**
- **Description:** Native mobile apps with offline support to increase daily engagement
- **Evidence:**
  - Current mobile: 12% of sessions, mostly view-only
  - User requests: "Better mobile app" is #4 requested feature
  - Industry benchmark: 35% mobile sessions for leading competitors
- **Technical Requirements:**
  - React Native rewrite (current hybrid app is limiting)
  - Offline sync with conflict resolution
  - Estimated: 3-4 months with 2 mobile engineers
- **Potential Impact:** Increase DAU by 20% through mobile engagement
- **Confidence:** Medium (significant technical investment, less certain ROI)
- **Key Assumptions:**
  - Users want to do real work on mobile, not just check status
  - React Native will deliver acceptable performance

---

#### Q2: Product Development (New Products, Existing Markets)

**Strategic Question:** What new products can we build for our existing SMB customers?

---

**Opportunity 2.1: AI-Powered Project Insights**
- **Description:** AI assistant that predicts project risks, suggests task prioritization, and identifies bottlenecks
- **Evidence:**
  - Market trend: AI features are table-stakes by 2026; Monday.com, Asana all shipping AI
  - Customer interviews: "I spend 2 hours/week analyzing project status" (common pain point)
  - Data advantage: We have 5M+ historical projects for training
- **Technical Requirements:**
  - ML pipeline infrastructure (new capability)
  - Model training on project data
  - UX for AI suggestions
  - Estimated: 4-6 months with 2 ML engineers (need to hire)
- **Potential Impact:**
  - Differentiation enabling 20% price increase premium tier
  - Churn reduction through proactive risk alerts
- **Confidence:** Medium
- **Key Assumptions:**
  - AI predictions will be accurate enough to be useful (needs validation)
  - Users will trust AI recommendations
  - We can hire ML talent competitively

---

**Opportunity 2.2: Resource Planning Module**
- **Description:** Capacity planning and workload management across projects
- **Evidence:**
  - Feature requests: #3 most requested feature
  - Upgrade path: Could be premium-only feature driving upgrades
  - Competitor analysis: Monday.com and Wrike have this; Asana basic
- **Technical Requirements:**
  - New data model for capacity/availability
  - Visualization components (Gantt-style)
  - Estimated: 2-3 months
- **Potential Impact:** Premium tier upgrade driver = $800K ARR opportunity
- **Confidence:** Medium
- **Key Assumptions:**
  - SMB customers have resource planning needs (may be more enterprise)
  - Complexity won't hurt our "simple" positioning

---

**Opportunity 2.3: Client Portal**
- **Description:** External-facing portal for agencies to share project status with clients
- **Evidence:**
  - User segment: 28% of customers are agencies/consultancies
  - Feature requests: Consistent ask from agency segment
  - Competitor: No strong incumbent for agency-focused PM
- **Technical Requirements:**
  - Permission model changes (significant)
  - Branded external views
  - Estimated: 3-4 months
- **Potential Impact:** Capture agency vertical = $600K ARR opportunity
- **Confidence:** Medium (strong signal but niche segment)
- **Key Assumptions:**
  - Agency segment is large enough to justify investment
  - Won't confuse our product positioning

---

#### Q3: Market Development (Existing Products, New Markets)

**Strategic Question:** Can we take our existing product to new customer segments or geographies?

---

**Opportunity 3.1: Enterprise Segment (500+ employees)**
- **Description:** Move upmarket to capture enterprise customers
- **Evidence:**
  - Inbound interest: 15+ enterprise inquiries/month currently turned away
  - Pricing opportunity: Enterprise contracts 5-10x SMB ARPU
  - Market size: Enterprise PM market is $4.5B (larger than SMB)
- **Technical Requirements:**
  - SSO/SAML (3 weeks—partially built)
  - Advanced permissions (6 weeks)
  - Audit logging (4 weeks)
  - SOC2 compliance (6 months process, $50K+)
  - Admin console (4 weeks)
- **Potential Impact:** 10 enterprise deals = $1M+ ARR
- **Confidence:** Medium
- **Key Assumptions:**
  - Enterprise buyers will choose us over established vendors (Asana, Monday, Jira)
  - We can build enterprise sales motion (currently product-led only)
  - Technical requirements are complete list (enterprise often has surprises)
- **Risks:**
  - Significant distraction from SMB focus
  - Sales cycle: 6-12 months vs. same-day for SMB
  - Support burden: Enterprise expects dedicated support

---

**Opportunity 3.2: LATAM Geographic Expansion**
- **Description:** Localize product for Spanish/Portuguese markets in Latin America
- **Evidence:**
  - Current traffic: 8% of website visitors from LATAM, 0.5% conversion (vs. 2.5% US)
  - Market research: Brazilian and Mexican SaaS markets growing 30% YoY
  - Competitor presence: Major competitors have weak LATAM presence
- **Technical Requirements:**
  - i18n refactor (4 weeks—codebase is mostly ready)
  - Spanish/Portuguese translations (2 weeks with contractor)
  - Localized payment (Stripe supports LATAM)
  - Local pricing (currency, market-appropriate pricing)
- **Potential Impact:** $500K ARR in year 1 (conservative)
- **Confidence:** Medium
- **Key Assumptions:**
  - Language is the primary barrier (may also be payment, trust, support)
  - We can support Portuguese/Spanish without local team
  - Market pricing expectations are viable ($X vs. US $Y)

---

**Opportunity 3.3: Vertical Focus: Legal Industry**
- **Description:** Vertical-specific features and positioning for law firms
- **Evidence:**
  - Current usage: 7% of customers are legal/professional services
  - Legal PM market: $800M, underserved by horizontal tools
  - Legal-specific needs: Matter management, conflict checking, time tracking
- **Technical Requirements:**
  - Significant—would need legal-specific features
  - Compliance (client confidentiality requirements)
  - Estimated: 4-6 months to be competitive
- **Potential Impact:** $400K ARR (small but defensible niche)
- **Confidence:** Low
- **Key Assumptions:**
  - Legal firms will choose horizontal tool over legal-specific vendors
  - We can build legal expertise (or partner)
  - The vertical justifies the investment vs. horizontal growth

---

#### Q4: Diversification (New Products, New Markets)

**Strategic Question:** Should we build entirely new products for new markets?

---

**Opportunity 4.1: Time Tracking Product** ❌ NOT RECOMMENDED
- **Description:** Standalone or integrated time tracking
- **Evidence:**
  - Customer requests: #1 requested feature (but see below)
  - Market analysis: Time tracking market is $1.5B BUT:
    - Saturated with strong incumbents (Toggl, Harvest, Clockify)
    - Race to bottom on pricing (freemium dominant)
    - Low switching costs = commoditized
- **Technical Requirements:** 2-3 months to build basic
- **Potential Impact:** Unclear—would compete with established free tools
- **Confidence:** Low
- **Recommendation:** **Deprioritize.** Integrate with existing time tracking tools instead of building. Customer requests may reflect desire for integration, not new product.
- **Key Assumptions Being Challenged:**
  - "Customers want us to build time tracking" — May actually want integration
  - "Bundling adds value" — May create unfocused product

---

**Opportunity 4.2: CRM Features** ❌ NOT RECOMMENDED
- **Description:** Customer relationship management functionality
- **Evidence:**
  - Some customer overlap (agencies managing both projects and clients)
  - Market: CRM is $60B but dominated by Salesforce, HubSpot, Pipedrive
- **Analysis:** This is not our competency. CRM is a different product category with different buyers, different competitive dynamics, and would distract from PM focus.
- **Confidence:** Low
- **Recommendation:** **Deprioritize.** Build integrations with CRMs instead.

---

**Opportunity 4.3: White-Label API Platform** ❓ NEEDS VALIDATION
- **Description:** Offer TaskFlow as white-label solution for other SaaS companies
- **Evidence:**
  - Inbound interest: 3 companies have inquired about white-labeling
  - Technical readiness: API is reasonably complete (85% coverage)
  - Potential: High margins on platform deals
- **Technical Requirements:**
  - Multi-tenancy enhancements
  - White-label branding system
  - Enterprise SLAs and support
- **Potential Impact:** Unknown—could be $2M+ or could be distraction
- **Confidence:** Low (insufficient data)
- **Recommendation:** **Validate before investing.** Talk to the 3 inbound leads, understand their needs and willingness to pay. If validated, could be high-ROI opportunity.

---

### Risk-Reward Summary

| Quadrant | Opportunity | Potential | Risk | Confidence | Effort | Recommendation |
|----------|-------------|-----------|------|------------|--------|----------------|
| Q1 | Onboarding 2.0 | $420K ARR saved | Low | High | 1 month | ★ DO |
| Q1 | Team Collaboration | $1.2M ARR | Low | High | 2 months | ★ DO |
| Q1 | Mobile Upgrade | +20% DAU | Medium | Medium | 4 months | ◆ CONSIDER |
| Q2 | AI Insights | Premium tier | Medium | Medium | 6 months | ◆ CONSIDER |
| Q2 | Resource Planning | $800K ARR | Low | Medium | 3 months | ◆ CONSIDER |
| Q2 | Client Portal | $600K ARR | Low | Medium | 4 months | ◇ MONITOR |
| Q3 | Enterprise | $1M+ ARR | High | Medium | 9 months | ◆ CONSIDER |
| Q3 | LATAM | $500K ARR | Medium | Medium | 2 months | ◆ CONSIDER |
| Q3 | Legal Vertical | $400K ARR | High | Low | 6 months | ◇ MONITOR |
| Q4 | Time Tracking | Low | High | Low | 3 months | ✗ SKIP |
| Q4 | CRM | Low | High | Low | 6+ months | ✗ SKIP |
| Q4 | White-Label | Unknown | Medium | Low | 3 months | ❓ VALIDATE |

---

### Prioritized Recommendations

| Priority | Strategy | Quadrant | Rationale | Investment | Success Metric |
|----------|----------|----------|-----------|------------|----------------|
| **P0** | Onboarding 2.0 | Q1 | High confidence, low effort, immediate churn impact | 1 month, 2 engineers | Day-30 churn -15% |
| **P0** | Team Collaboration | Q1 | High confidence, strong feature request signal, competitive necessity | 2 months, 3 engineers | Team adoption +30% |
| **P1** | AI Project Insights | Q2 | Strategic differentiation, market trend, data advantage | 6 months, 2 ML engineers (hire) | Premium tier conversion +10% |
| **P1** | LATAM Expansion | Q3 | Low effort, clear demand signal (traffic), underserved market | 2 months, 1 engineer + contractor | LATAM revenue $500K Y1 |
| **P2** | Enterprise (limited) | Q3 | Validate with 3-5 design partners before full commitment | 3 months initial (SSO, audit log) | 5 enterprise pilots |
| **Deprioritize** | Time Tracking | Q4 | Saturated market, commoditized, not our strength | — | — |
| **Deprioritize** | CRM | Q4 | Out of scope, integrate don't build | — | — |
| **Validate** | White-Label | Q4 | Interesting but unvalidated; talk to leads first | 2 weeks discovery | Decision: invest or not |

---

### Key Assumptions & Validation Needs

**Before P0 Investments (proceed with high confidence):**
- A/B test new onboarding flow before full rollout
- Load test WebSocket infrastructure for team collaboration scale

**Before P1 Investments (validate first):**
- AI Insights: Build prototype, test with 10 beta customers, measure prediction accuracy
- LATAM: Validate payment and support assumptions with local market research
- Enterprise: Sign 3 design partner agreements before building enterprise features

**Strategic Assumption to Monitor:**
- SMB market growth rate (if slowing, enterprise becomes more attractive)
- Competitor AI feature launches (may accelerate our timeline)
- Economic conditions affecting SMB software budgets

---

### Portfolio Balance Assessment

**Current Recommended Portfolio:**
- **70% Market Penetration** (low risk, known market, proven product)
- **20% Product Development** (medium risk, strategic bets)
- **10% Market Development** (medium risk, geographic/segment expansion)
- **0% Diversification** (highest risk, no compelling opportunities identified)

This is an appropriately conservative portfolio for a growth-stage company that has achieved product-market fit and should maximize its core opportunity before diversifying.
```

## Customization Guide

- **For Pre-PMF Companies:** Focus analysis on Market Penetration only—find PMF before expanding
- **For High-Growth Startups:** Emphasize Q1 and Q2; Q3/Q4 are distractions
- **For Mature Products:** Q3 and Q4 become more relevant as core market saturates
- **For Platform Companies:** White-label/API (Q4) may be higher priority than for point solutions

## Techniques Used

- **ST-01 (Clear Objective Statement):** Explicit goal of evaluating growth strategies using the Ansoff framework
- **ST-02 (Structured Sequential Instructions):** Systematic quadrant-by-quadrant analysis process
- **DS-01 (Framework Application):** Direct application of the Ansoff Growth Matrix
- **RT-02 (Multi-Dimensional Analysis):** Evaluation across risk, reward, confidence, and effort dimensions
- **QA-02 (Adversarial Thinking):** False-positive prevention challenges growth assumptions and highlights risks

## Related Prompts

- [BCG Matrix Analysis](bcg_matrix_analysis.md) - Portfolio analysis for multi-product companies
- [Blue Ocean Strategy Analysis](blue_ocean_strategy_analysis.md) - Creating uncontested market space
- [Product-Market Fit Analysis](product_market_fit_analysis.md) - Validating fit before growth strategies
- [SWOT Analysis](swot_analysis.md) - Internal/external analysis to inform strategy
