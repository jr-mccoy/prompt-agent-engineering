---
title: "Lean Canvas Analysis for Codebase"
category: business/analysis
description: "Apply the Lean Canvas framework to evaluate a product/codebase's business model, identifying problem-solution fit, unique value propositions, and areas requiring validation or pivot"
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
  - business-model
  - startup
  - lean-methodology
  - product-strategy
updated: "2026-01-25"
related_prompts:
  - domain-business-strategy/analysis/business_model_canvas_analysis.md
  - domain-business-strategy/analysis/product_market_fit_analysis.md
  - domain-business-strategy/analysis/value_proposition_canvas_analysis.md
---

# Lean Canvas Analysis for Codebase

**Objective:** Analyze the codebase using the Lean Canvas framework to evaluate its business model through nine key elements (Problem, Solution, Unique Value Proposition, Unfair Advantage, Customer Segments, Key Metrics, Channels, Cost Structure, Revenue Streams), identifying areas for validation, improvement, or strategic pivot.

## When to Use

- **Use when:** Evaluating a startup or early-stage product's business viability
- **Use when:** Deciding whether to pivot or persevere based on current product-market fit
- **Use when:** Communicating business model to investors, team, or stakeholders
- **Use when:** Identifying the riskiest assumptions that need validation
- **Don't use when:** Analyzing established enterprise businesses (use Business Model Canvas instead)
- **Don't use when:** You only need technical analysis (use architecture or code quality analysis)
- **Don't use when:** The product has no commercial intent (internal tools, open source)

## Instructions

1. **Establish Product Context (Required First)**
   - Document the product's stated purpose and target user
   - Identify the development stage (idea, MVP, growth, scale)
   - Note any existing customer/user feedback
   - Understand the team's assumptions about the market

2. **Analyze Each Lean Canvas Element**

   **a. Problem (Top 3 Problems):**
   - What user problems does the code address?
   - How severe and frequent are these problems?
   - What existing alternatives or workarounds exist?
   - **Evidence to collect:** User research, support tickets, competitor analysis

   **b. Customer Segments (Early Adopters):**
   - Who are the target users for this product?
   - Who would be the early adopters (most desperate for solution)?
   - Are there distinct user personas with different needs?
   - **Evidence to collect:** User demographics, usage patterns, customer interviews

   **c. Unique Value Proposition:**
   - What makes this solution uniquely compelling?
   - What is the single, clear message that states why the user should choose this?
   - How does it differ from existing solutions?
   - **Evidence to collect:** Positioning statements, competitor comparison, customer testimonials

   **d. Solution (Top 3 Features):**
   - How does the code solve the identified problems?
   - What are the top 3 features that address user needs?
   - Is the solution minimal (MVP) or over-engineered?
   - **Evidence to collect:** Feature inventory, user value mapping, complexity assessment

   **e. Channels:**
   - How will/does the product reach its target users?
   - What acquisition, activation, and retention channels exist?
   - Are there built-in viral or distribution features?
   - **Evidence to collect:** Marketing code, referral systems, integration points

   **f. Revenue Streams:**
   - How will/does this product generate revenue?
   - What monetization features are implemented?
   - What's the pricing model (subscription, usage, one-time)?
   - **Evidence to collect:** Payment integration, pricing logic, billing systems

   **g. Cost Structure:**
   - What are the main cost drivers in building and operating this?
   - What are fixed vs. variable costs?
   - What's the burn rate trajectory?
   - **Evidence to collect:** Infrastructure costs, third-party services, team size

   **h. Key Metrics:**
   - What metrics indicate success for this product?
   - What analytics/tracking is implemented?
   - Are the metrics actionable or vanity?
   - **Evidence to collect:** Analytics implementation, dashboards, event tracking

   **i. Unfair Advantage:**
   - What makes this hard to copy or buy?
   - Are there network effects, data moats, or unique expertise?
   - What defensibility does the codebase create?
   - **Evidence to collect:** Proprietary algorithms, data assets, unique integrations

3. **Identify Riskiest Assumptions**
   - For each element, identify the key assumptions being made
   - Rate assumptions by risk (if wrong, does the business fail?)
   - Prioritize assumptions that need validation first
   - Design experiments to test critical assumptions

4. **CRITICAL: Validate Claims Before Reporting**
   - For each canvas element, distinguish between:
     - Implemented and validated (evidence from customers)
     - Implemented but unvalidated (assumption)
     - Not implemented (gap)
   - Challenge founder/team assumptions with evidence
   - Note where optimism may be clouding judgment

5. **Develop Recommendations**
   - Identify gaps in the Lean Canvas
   - Suggest experiments to validate assumptions
   - Recommend pivot opportunities if current approach is risky
   - Prioritize next actions by risk reduction

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Accept stated problems without evidence of customer pain
- Claim "unfair advantage" for things competitors can easily replicate
- Assume revenue model will work without validation
- Confuse features with customer value
- Accept "everyone" as a customer segment
- Treat founder enthusiasm as market validation
- Ignore evidence that contradicts the business model

✅ **DO:**
- Distinguish between validated learnings and assumptions
- Challenge claims of uniqueness with competitor evidence
- Rate each element by confidence level (validated/assumed/gap)
- Identify the single riskiest assumption for the business
- Consider scenarios where key assumptions prove false
- Recommend validation experiments before building

## Confidence Levels

Rate each canvas element with a confidence level:

- **Validated:** Customer evidence supports this element (interviews, usage data, payments)
- **Assumed:** Team believes this but lacks validation; needs testing
- **Gap:** This element is not adequately addressed; critical work needed

## Expected Output

A comprehensive Lean Canvas analysis including:
- Visual canvas with all nine elements
- Confidence rating for each element
- Identification of riskiest assumptions
- Prioritized validation experiments
- Pivot or persevere recommendation

### Output Format

```markdown
## Lean Canvas Analysis: [Product Name]

### Executive Summary
[3-5 sentences summarizing business model viability and key risks]

### Lean Canvas

┌─────────────────┬─────────────────┬─────────────────┬─────────────────┬─────────────────┐
│    PROBLEM      │    SOLUTION     │  UNIQUE VALUE   │ UNFAIR ADVANTAGE│    CUSTOMER     │
│                 │                 │   PROPOSITION   │                 │    SEGMENTS     │
│  [Problems]     │  [Features]     │                 │  [Advantage]    │                 │
│                 │                 │  [UVP]          │                 │  [Segments]     │
│  Confidence:    │  Confidence:    │                 │  Confidence:    │                 │
│  [Level]        │  [Level]        │  Confidence:    │  [Level]        │  Confidence:    │
│                 │                 │  [Level]        │                 │  [Level]        │
├─────────────────┴─────────────────┤                 ├─────────────────┴─────────────────┤
│            KEY METRICS            │                 │            CHANNELS               │
│                                   │                 │                                   │
│  [Metrics]                        │                 │  [Channels]                       │
│                                   │                 │                                   │
│  Confidence: [Level]              │                 │  Confidence: [Level]              │
├───────────────────────────────────┴─────────────────┴───────────────────────────────────┤
│                     COST STRUCTURE                  │           REVENUE STREAMS         │
│                                                     │                                   │
│  [Costs]                                            │  [Revenue]                        │
│                                                     │                                   │
│  Confidence: [Level]                                │  Confidence: [Level]              │
└─────────────────────────────────────────────────────┴───────────────────────────────────┘

### Element Analysis

#### Problem
**Top 3 Problems:**
1. [Problem 1]
2. [Problem 2]
3. [Problem 3]

**Evidence:** [What validates these are real problems]
**Confidence:** Validated | Assumed | Gap
**Risk Assessment:** [What if these aren't the real problems?]

[Repeat for each element]

### Risk Assessment

| Element | Confidence | Assumption | If Wrong... | Priority |
|---------|------------|------------|-------------|----------|
| Problem | Assumed | Users have X pain | No market | P0 |

### Riskiest Assumptions

1. **[Assumption]** - [Why it's risky] - [How to validate]

### Recommendations

| # | Action | Element | Type | Priority |
|---|--------|---------|------|----------|
| 1 | [Action] | Problem | Validate | P0 |

### Pivot or Persevere?
[Assessment and recommendation]
```

## Example Output

```markdown
## Lean Canvas Analysis: FocusFlow (Productivity App for Remote Teams)

### Executive Summary

FocusFlow has a clear problem hypothesis (remote worker distraction) and a working MVP, but lacks customer validation. The biggest risk is the **Unfair Advantage** element—there's nothing preventing competitors from copying the core features. The **Revenue Stream** is assumed but untested (no paying customers yet). Recommend: run a 2-week validation sprint focused on (1) validating problem severity through interviews and (2) testing willingness to pay before further development.

### Lean Canvas

```
┌─────────────────┬─────────────────┬─────────────────┬─────────────────┬─────────────────┐
│    PROBLEM      │    SOLUTION     │  UNIQUE VALUE   │ UNFAIR ADVANTAGE│    CUSTOMER     │
│                 │                 │   PROPOSITION   │                 │    SEGMENTS     │
│ 1. Remote       │ 1. Focus timer  │                 │ ⚠️ WEAK         │                 │
│    workers get  │    with team    │ "Stay focused   │                 │ Remote workers  │
│    distracted   │    visibility   │  together,      │ - Team network  │ at tech         │
│                 │                 │  apart"         │   effects (not  │ companies       │
│ 2. Hard to know │ 2. Async status │                 │   validated)    │ (10-200 people) │
│    when team is │    broadcasts   │ Focus sessions  │                 │                 │
│    available    │                 │ with team       │ - Usage data    │ Early adopter:  │
│                 │ 3. Focus        │ accountability  │   for ML (not   │ Engineering     │
│ 3. Zoom fatigue │    analytics    │                 │   yet built)    │ managers        │
│    from syncs   │    dashboard    │                 │                 │                 │
│                 │                 │                 │                 │                 │
│ ⚠️ ASSUMED      │ ✓ BUILT         │ ⚠️ ASSUMED      │ ❌ GAP          │ ⚠️ ASSUMED      │
├─────────────────┴─────────────────┤                 ├─────────────────┴─────────────────┤
│            KEY METRICS            │                 │            CHANNELS               │
│                                   │                 │                                   │
│ - Daily active teams              │                 │ - Product Hunt launch             │
│ - Focus sessions/user/day         │                 │ - Twitter/LinkedIn content        │
│ - Team retention (30-day)         │                 │ - Slack community integration     │
│ - NPS                             │                 │ - Word of mouth (teams)           │
│                                   │                 │                                   │
│ ⚠️ ASSUMED (not tracking yet)     │                 │ ⚠️ ASSUMED (not tested)           │
├───────────────────────────────────┴─────────────────┴───────────────────────────────────┤
│                     COST STRUCTURE                  │           REVENUE STREAMS         │
│                                                     │                                   │
│ Fixed:                                              │ Freemium model:                   │
│ - 2 founders (no salary yet)                        │ - Free: 3 users, basic features   │
│ - $200/mo infrastructure                            │ - Team: $8/user/mo, analytics     │
│ - $50/mo tools                                      │ - Enterprise: Custom pricing      │
│                                                     │                                   │
│ Variable:                                           │ Target: $50 ARPU for teams        │
│ - Support (not yet)                                 │                                   │
│ - Marketing (not yet)                               │                                   │
│                                                     │                                   │
│ ✓ KNOWN (low burn)                                  │ ❌ GAP (no paying customers)      │
└─────────────────────────────────────────────────────┴───────────────────────────────────┘
```

---

### Element Analysis

#### Problem
**Top 3 Problems:**
1. **Remote workers struggle to maintain focus** - Constant Slack notifications, context switching
2. **Hard to know when teammates are available** - No visibility into deep work vs. available time
3. **Zoom fatigue from synchronous coordination** - Too many status meetings

**Evidence:**
- Founder experience (anecdotal, not validated at scale)
- 3 customer discovery interviews (small sample)
- General industry reports on remote work challenges

**Confidence:** ⚠️ **Assumed**

**Risk Assessment:** If these aren't severe enough problems, users won't pay. Remote workers have many coping mechanisms already (Do Not Disturb, Slack status, calendar blocking).

**Validation Needed:** Interview 20+ potential customers. Ask about current solutions, pain severity (1-10), and willingness to pay.

---

#### Customer Segments
**Target:** Remote workers at tech companies (10-200 employees)

**Early Adopter Profile:** Engineering managers who want visibility into team focus without micromanaging

**Evidence:**
- Founder network is tech-heavy (convenient, not validated)
- No usage data yet on who actually adopts

**Confidence:** ⚠️ **Assumed**

**Risk Assessment:** Tech workers may not be the most acute segment. Consider: agencies, consultants, freelancers, students—all have focus challenges.

**Validation Needed:** Run ads targeting different segments; measure click-through and signup conversion.

---

#### Unique Value Proposition
**Stated UVP:** "Stay focused together, apart"

**Value Proposition:** Focus sessions with team accountability—see when teammates are in focus mode, create social pressure/support for deep work.

**Evidence:**
- No A/B testing of messaging
- No customer validation of whether "team" aspect matters

**Confidence:** ⚠️ **Assumed**

**Risk Assessment:** Individual focus apps (Forest, Freedom) are established. If the "team" angle isn't compelling, this is a commodity.

**Validation Needed:** Test messaging variants; interview users about individual vs. team value.

---

#### Solution
**Top 3 Features:**
1. **Focus timer with team visibility** - Start a focus session; teammates see you're in deep work
2. **Async status broadcasts** - "I'm focusing on X until 3pm" without Slack noise
3. **Focus analytics dashboard** - Track personal and team focus patterns

**Evidence:**
- MVP built and functional
- 47 beta users signed up
- Average session: 1.2 focus periods/user/day (low)

**Confidence:** ✓ **Built** (but usage is low)

**Risk Assessment:** Features exist but engagement is weak. Either solution doesn't solve problem well, or problem isn't acute enough.

**Validation Needed:** User interviews with active vs. churned beta users. Why did they stop?

---

#### Channels
**Planned Channels:**
- Product Hunt launch (one-time spike)
- Twitter/LinkedIn content marketing
- Slack community integration
- Word of mouth within teams

**Evidence:**
- None tested yet
- No CAC data
- No conversion funnel data

**Confidence:** ⚠️ **Assumed**

**Risk Assessment:** B2B SaaS for small teams is notoriously hard to reach. Product Hunt gives spike but not sustained growth. Content marketing takes 6-12 months.

**Validation Needed:** Test one channel with small budget before committing.

---

#### Revenue Streams
**Model:** Freemium with team upgrade

| Tier | Price | Features |
|------|-------|----------|
| Free | $0 | 3 users, basic timer |
| Team | $8/user/mo | Analytics, integrations |
| Enterprise | Custom | SSO, admin, support |

**Evidence:**
- No paying customers yet
- Pricing based on competitor benchmarking, not willingness-to-pay research
- No payment flow implemented

**Confidence:** ❌ **Gap**

**Risk Assessment:** Critical gap. Without revenue validation, no evidence of viable business. $8/user may be too high or too low.

**Validation Needed:** Implement payment; run willingness-to-pay survey; offer early-adopter pricing.

---

#### Cost Structure
**Current Burn:** ~$250/month (infrastructure + tools)

**Projected at Scale:**
- $2,000/mo infrastructure at 10K users
- $10,000/mo if founders take salary
- Marketing TBD

**Evidence:**
- Actual costs tracked
- Low burn is an advantage for runway

**Confidence:** ✓ **Known**

**Note:** Low burn gives time to validate, but also means founders aren't committed full-time yet.

---

#### Key Metrics
**Planned Metrics:**
- Daily active teams (DAT)
- Focus sessions per user per day
- 30-day team retention
- NPS

**Evidence:**
- Basic analytics implemented (Mixpanel)
- Not tracking team-level metrics yet
- No NPS survey implemented

**Confidence:** ⚠️ **Assumed**

**Risk Assessment:** Without proper tracking, can't learn. Need to implement cohort analysis and team retention tracking.

**Validation Needed:** Implement team-level analytics; set up NPS survey.

---

#### Unfair Advantage
**Claimed Advantages:**
1. Team network effects (more teammates = more value)
2. Usage data for ML-based focus recommendations (future)

**Evidence:**
- Network effects not validated—do teams actually grow usage?
- ML is vaporware; no data scientist on team
- Nothing prevents Slack, Microsoft, or existing apps from adding this feature

**Confidence:** ❌ **Gap**

**Risk Assessment:** This is the weakest element. If a competitor with distribution (Slack, Notion) adds focus features, FocusFlow has no defense.

**Validation Needed:** Measure network effect coefficient (do teams with more users retain better?). Consider what creates real lock-in.

---

### Risk Assessment

| Element | Confidence | Key Assumption | If Wrong... | Priority |
|---------|------------|----------------|-------------|----------|
| **Problem** | Assumed | Remote focus is acute pain | No willingness to pay | P0 |
| **Revenue** | Gap | Users will pay $8/user/mo | No viable business | P0 |
| **Unfair Advantage** | Gap | Team network creates lock-in | Easily copied; commoditized | P1 |
| **Customer Segment** | Assumed | Tech workers are best segment | Missing better market | P1 |
| **UVP** | Assumed | "Team" angle differentiates | Just another focus app | P2 |
| **Channels** | Assumed | Content + PH will drive growth | Can't acquire customers | P2 |
| **Key Metrics** | Assumed | Current metrics are right ones | Learning wrong things | P2 |
| **Solution** | Built | Features solve problem | Over/under-built | P3 |
| **Costs** | Known | Can stay lean | N/A - known | - |

---

### Riskiest Assumptions

**#1: Problem Severity**
- **Assumption:** Remote workers are desperate enough for focus help to pay for a tool
- **Why Risky:** Many free alternatives exist (calendar blocking, DND, browser extensions). If pain isn't acute, no market.
- **How to Validate:** Customer interviews with severity scoring. Ask: "How much would you pay to solve this?" "What have you already tried?"

**#2: Willingness to Pay**
- **Assumption:** Teams will pay $8/user/month for focus productivity
- **Why Risky:** No paying customers. Competitor Clockwise is free. Hard to justify budget for "soft" productivity tool.
- **How to Validate:** Implement payment. Offer 50% early-adopter discount. Track conversion from free to paid.

**#3: Team Network Effects**
- **Assumption:** More teammates using FocusFlow = more valuable for each user
- **Why Risky:** Individual focus apps work fine. "Team" angle may not create stickiness.
- **How to Validate:** Cohort analysis: do teams with 5+ users retain better than teams with 2-3? Is there invitation behavior?

---

### Recommendations

| # | Action | Element | Type | Timeline | Priority |
|---|--------|---------|------|----------|----------|
| 1 | Run 20 customer discovery interviews | Problem, Segment | Validate | 2 weeks | P0 |
| 2 | Implement payment and track conversion | Revenue | Validate | 1 week | P0 |
| 3 | Analyze beta user retention by team size | Unfair Advantage | Validate | 1 week | P1 |
| 4 | Interview churned users | Solution | Learn | 1 week | P1 |
| 5 | Test 1 acquisition channel with $500 | Channels | Validate | 2 weeks | P2 |
| 6 | Implement team-level analytics | Key Metrics | Build | 1 week | P2 |

---

### Pivot or Persevere?

**Current Recommendation:** ⚠️ **Validate Before Persevering**

**Rationale:**
- MVP is built and functional—good execution
- But no evidence of problem-solution fit or willingness to pay
- Low engagement (1.2 sessions/user/day) is warning sign
- Unfair advantage is critically weak

**Decision Framework:**
1. **Persevere if:** Customer interviews confirm acute pain + 10% of beta users convert to paid
2. **Pivot if:** Interviews reveal different problem/segment with better fit
3. **Quit if:** No willingness to pay after direct asks; competitors enter with distribution advantage

**Recommended Pivot Options (if validation fails):**
- **Segment pivot:** Target agencies/consultants instead of tech teams (more acute billing pressure)
- **Problem pivot:** Focus on async communication, not focus time (bigger pain?)
- **Channel pivot:** B2B2C through team productivity consultants
```

## Customization Guide

- **For Pre-MVP Products:** Focus on Problem and Customer Segment validation first; Solution can wait
- **For Post-PMF Products:** Emphasize Revenue, Channels, and Cost Structure; growth mechanics matter more
- **For B2B Products:** Customer Segment and Channels often hardest; validate sales motion early
- **For B2C Products:** Channels and Key Metrics critical; viral mechanics determine success

## Techniques Used

- **ST-01 (Clear Objective Statement):** Explicit goal of evaluating business model viability through Lean Canvas
- **ST-02 (Structured Sequential Instructions):** Systematic element-by-element analysis process
- **DS-01 (Framework Application):** Direct application of Lean Canvas framework
- **RT-02 (Multi-Dimensional Analysis):** Evaluation across nine business model elements
- **QA-02 (Adversarial Thinking):** False-positive prevention challenges assumptions and identifies risks

## Related Prompts

- [Business Model Canvas Analysis](business_model_canvas_analysis.md) - More comprehensive business model framework
- [Product-Market Fit Analysis](product_market_fit_analysis.md) - Evaluating product-market fit specifically
- [Value Proposition Canvas Analysis](value_proposition_canvas_analysis.md) - Deep dive on value proposition
- [Jobs to Be Done Analysis](jobs_to_be_done_analysis.md) - Customer needs framework
