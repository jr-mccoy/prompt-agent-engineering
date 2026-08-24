---
title: "Product/Market Fit Analysis for Codebase"
category: business/analysis
description: "Evaluate product-market fit using quantitative and qualitative indicators including the Sean Ellis test, retention curves, organic growth signals, and customer feedback patterns to determine PMF status and identify improvement priorities"
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - DS-01  # Framework Application
  - RT-02  # Multi-Dimensional Analysis
  - QA-02  # Adversarial Thinking
  - DS-06  # Prioritization Guidance
difficulty: intermediate
tags:
  - product-market-fit
  - startup-metrics
  - growth-strategy
  - customer-validation
  - retention
updated: "2026-01-25"
related_prompts:
  - domain-business-strategy/analysis/lean_canvas_analysis.md
  - domain-business-strategy/analysis/jobs_to_be_done_analysis.md
  - domain-business-strategy/analysis/value_proposition_canvas_analysis.md
  - domain-business-strategy/analysis/kano_model_analysis.md
---

# Product/Market Fit Analysis for Codebase

**Objective:** Evaluate the product's product-market fit (PMF) using a multi-dimensional assessment framework that combines quantitative metrics (retention, NPS, organic growth) with qualitative signals (customer enthusiasm, usage patterns, competitive switching) to determine current PMF status and identify the highest-leverage improvements to strengthen fit.

## When to Use

- **Use when:** Deciding whether to scale go-to-market or iterate on product
- **Use when:** Investors or stakeholders ask about PMF status
- **Use when:** Growth is stalling and you need to diagnose why
- **Use when:** Preparing for fundraising and need to demonstrate traction
- **Use when:** Evaluating whether to pivot or persevere
- **Don't use when:** Product hasn't launched (use Lean Canvas for pre-launch)
- **Don't use when:** You have fewer than 20-30 active users (insufficient data)
- **Don't use when:** You need competitive analysis (use positioning map)

## Instructions

1. **Establish Context and Baseline**
   - Define the product and primary use case being evaluated
   - Identify the target market/customer segment
   - Note the product stage (MVP, beta, GA, growth)
   - Document current user/customer counts and trends
   - **Evidence to collect:** User database, signup trends, customer list

2. **Assess Quantitative PMF Indicators**

   **a. The Sean Ellis Test (40% Rule)**
   - Survey users: "How would you feel if you could no longer use [product]?"
   - Options: Very disappointed / Somewhat disappointed / Not disappointed
   - Calculate percentage answering "Very disappointed"
   - **PMF threshold:** 40%+ = strong PMF; 25-40% = emerging; <25% = weak
   - **Evidence to collect:** Survey responses (minimum 40 responses recommended)

   **b. Retention Analysis**
   - Calculate Day 1, Day 7, Day 30 retention rates
   - Plot retention curve over time
   - Identify if retention flattens (PMF signal) or approaches zero (no PMF)
   - Compare to industry benchmarks
   - **Evidence to collect:** Cohort analysis, retention curves, engagement logs

   **c. Net Promoter Score (NPS)**
   - Calculate NPS from customer surveys
   - Segment NPS by customer type, use case, tenure
   - Analyze promoter vs. detractor themes
   - **PMF threshold:** 50+ = strong; 20-50 = moderate; <20 = weak
   - **Evidence to collect:** NPS surveys, open-ended feedback

   **d. Organic Growth Indicators**
   - Calculate percent of new users from organic/referral channels
   - Track viral coefficient (K-factor) if applicable
   - Monitor word-of-mouth mentions and organic search growth
   - **Evidence to collect:** Channel attribution, referral data, social mentions

3. **Assess Qualitative PMF Indicators**

   **a. Customer Enthusiasm Signals**
   - Do customers complain when features break? (sign of dependency)
   - Do customers proactively suggest features? (sign of investment)
   - Do customers defend the product to skeptics?
   - Would customers pay more if asked?
   - **Evidence to collect:** Support tickets, feature requests, testimonials

   **b. Usage Depth and Frequency**
   - What percentage of users become power users?
   - Do users return without prompting?
   - How does usage change over time (growing vs. declining)?
   - Are users finding uses you didn't expect?
   - **Evidence to collect:** Usage analytics, session data, feature adoption

   **c. Competitive Switching Behavior**
   - Are customers switching FROM competitors to you? Why?
   - Are customers switching FROM you to competitors? Why?
   - What triggers switching decisions?
   - What alternatives do users mention?
   - **Evidence to collect:** Win/loss analysis, churn interviews, competitor mentions

   **d. Market Pull Signals**
   - Are customers asking for things you haven't built yet?
   - Are customers trying to use the product for unexpected jobs?
   - Is demand exceeding your ability to onboard?
   - Do customers want to co-develop or partner?
   - **Evidence to collect:** Feature requests, sales pipeline, partnership inquiries

4. **Synthesize PMF Status**
   - Map each indicator to PMF level (Strong / Emerging / Weak / None)
   - Weight indicators by reliability and relevance
   - Identify conflicting signals and investigate
   - Determine overall PMF assessment
   - Rate confidence in assessment

5. **CRITICAL: Validate PMF Claims Before Reporting**
   - For positive signals:
     - Are we measuring the right things?
     - Could positive metrics mask underlying problems?
     - Are we cherry-picking favorable cohorts or timeframes?
     - Is sample size sufficient for conclusions?
   - For negative signals:
     - Could product issues be causing problems (bugs, UX) rather than fit?
     - Is the target market correctly defined?
     - Are we comparing to appropriate benchmarks?
   - Common false PMF signals:
     - High engagement from free users who won't pay
     - Growth from unsustainable paid acquisition
     - Strong NPS from early adopters who aren't representative
     - Retention from sticky contracts, not product value

6. **Identify PMF Improvement Priorities**
   - What is the biggest gap between current and target state?
   - Which improvements would most move the PMF needle?
   - What experiments would validate hypotheses?
   - What's the fastest path to stronger PMF?

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Claim PMF based on vanity metrics (signups, downloads) without retention
- Assume paid acquisition growth equals PMF (it can mask weak organic demand)
- Cherry-pick best cohorts or favorable time periods
- Confuse product stickiness with product love (switching costs ≠ PMF)
- Rely on a single metric; PMF is multi-dimensional
- Assume early adopter enthusiasm represents mainstream market
- Ignore churn—high growth can hide high churn temporarily

✅ **DO:**
- Use multiple indicators; PMF shows up across dimensions
- Weight retention and organic growth most heavily
- Segment analysis by customer type (different segments may have different PMF)
- Compare to relevant benchmarks, not best-in-class outliers
- Distinguish between "users who need this" and "users who will pay for this"
- Update analysis regularly; PMF can strengthen or weaken
- Be honest about what the data shows, not what you hope it shows

## Confidence Levels

Rate each indicator with a confidence level:

- **High Confidence:** Large sample, reliable measurement, clear trend
- **Medium Confidence:** Moderate sample, some measurement uncertainty
- **Low Confidence:** Small sample, proxy metrics, early-stage data

## Expected Output

A comprehensive PMF analysis including:
- Quantitative metric assessment with benchmarks
- Qualitative signal assessment
- Overall PMF status determination
- Prioritized improvement recommendations

### Output Format

```markdown
## Product-Market Fit Analysis: [Product Name]

### Executive Summary
[3-5 sentences summarizing PMF status, key evidence, and primary recommendation]

### Context

**Product:** [Name and brief description]
**Target Market:** [Specific segment]
**Stage:** [MVP/Beta/GA/Growth]
**Current Users:** [Number, trend]
**Analysis Date:** [Date]

### Quantitative PMF Assessment

#### Sean Ellis Test
**Question:** "How would you feel if you could no longer use [product]?"

| Response | Count | Percentage |
|----------|-------|------------|
| Very Disappointed | X | Y% |
| Somewhat Disappointed | X | Y% |
| Not Disappointed | X | Y% |

**PMF Score:** Y% very disappointed
**Benchmark:** 40%+ = strong PMF
**Assessment:** [Strong/Emerging/Weak/Insufficient Data]
**Confidence:** High/Medium/Low

#### Retention Analysis

| Period | Rate | Benchmark | Status |
|--------|------|-----------|--------|
| Day 1 | X% | Y% | Above/Below |
| Day 7 | X% | Y% | Above/Below |
| Day 30 | X% | Y% | Above/Below |
| Day 90 | X% | Y% | Above/Below |

**Retention Curve Shape:** [Flattening (good) / Approaching zero (bad)]

```
100%│●
    │ ●
    │  ●
    │   ●●●●●●●●●  ← Flattening = PMF signal
 50%│
    │
    │
    │      ●●●●●●●●  ← Still declining
    │             ●●
  0%└─────────────────
    D1 D7 D14 D30  D60  D90
```

**Assessment:** [Strong/Emerging/Weak/Insufficient Data]
**Confidence:** High/Medium/Low

#### Net Promoter Score

**NPS Score:** [Number]
**Benchmark:** 50+ = strong, 20-50 = moderate, <20 = weak

| Category | Percentage | Key Themes |
|----------|------------|------------|
| Promoters (9-10) | X% | [What they love] |
| Passives (7-8) | X% | [What's missing] |
| Detractors (0-6) | X% | [Pain points] |

**Assessment:** [Strong/Emerging/Weak/Insufficient Data]
**Confidence:** High/Medium/Low

#### Organic Growth

| Metric | Value | Trend | Benchmark |
|--------|-------|-------|-----------|
| % Organic Acquisition | X% | ↑/↓/→ | 50%+ = healthy |
| Referral Rate | X% | ↑/↓/→ | Varies by category |
| Viral Coefficient (K) | X | ↑/↓/→ | >1 = viral; >0.5 = healthy |
| Organic Search Traffic | X% of total | ↑/↓/→ | Growing = demand |

**Assessment:** [Strong/Emerging/Weak/Insufficient Data]
**Confidence:** High/Medium/Low

### Qualitative PMF Assessment

#### Customer Enthusiasm Signals

| Signal | Evidence | PMF Indication |
|--------|----------|----------------|
| Complain when features break | [Evidence] | Strong/Weak |
| Proactively suggest features | [Evidence] | Strong/Weak |
| Defend product to skeptics | [Evidence] | Strong/Weak |
| Would pay more if asked | [Evidence] | Strong/Weak |

**Assessment:** [Strong/Emerging/Weak]

#### Usage Depth and Frequency

| Signal | Evidence | PMF Indication |
|--------|----------|----------------|
| Power user percentage | X% | [Benchmark comparison] |
| Return without prompting | [Evidence] | Strong/Weak |
| Usage trend over time | Growing/Stable/Declining | [Assessment] |
| Unexpected use cases | [Examples] | [Assessment] |

**Assessment:** [Strong/Emerging/Weak]

#### Competitive Dynamics

| Signal | Evidence | PMF Indication |
|--------|----------|----------------|
| Switching TO us | [From whom, why] | [Assessment] |
| Switching FROM us | [To whom, why] | [Assessment] |
| Win rate vs. specific competitors | X% | [Assessment] |

**Assessment:** [Strong/Emerging/Weak]

#### Market Pull

| Signal | Evidence | PMF Indication |
|--------|----------|----------------|
| Demand exceeds capacity | [Evidence] | Strong/Weak |
| Feature requests beyond roadmap | [Evidence] | Strong/Weak |
| Partnership/integration requests | [Evidence] | Strong/Weak |
| Organic inbound inquiries | [Volume, trend] | Strong/Weak |

**Assessment:** [Strong/Emerging/Weak]

### Overall PMF Synthesis

#### Indicator Summary

| Category | Assessment | Confidence | Weight |
|----------|------------|------------|--------|
| Sean Ellis Test | [Level] | [Confidence] | 25% |
| Retention | [Level] | [Confidence] | 30% |
| NPS | [Level] | [Confidence] | 15% |
| Organic Growth | [Level] | [Confidence] | 15% |
| Qualitative Signals | [Level] | [Confidence] | 15% |

#### PMF Status Determination

**Overall PMF Assessment:** [Strong PMF / Emerging PMF / Weak PMF / No PMF]

**Confidence Level:** High / Medium / Low

**Key Evidence Supporting Assessment:**
1. [Most compelling positive evidence]
2. [Second most compelling]
3. [Third most compelling]

**Key Concerns/Risks:**
1. [Most significant concern]
2. [Second concern]

### Recommendations

#### If Strong PMF: Scale
| Priority | Action | Expected Impact |
|----------|--------|-----------------|
| P0 | [Action] | [Impact] |

#### If Emerging PMF: Strengthen
| Priority | Action | Expected Impact |
|----------|--------|-----------------|
| P0 | [Action] | [Impact] |

#### If Weak/No PMF: Iterate or Pivot
| Priority | Action | Expected Impact |
|----------|--------|-----------------|
| P0 | [Action] | [Impact] |

### Validation Experiments

| Hypothesis | Experiment | Success Criteria | Timeline |
|------------|------------|------------------|----------|
| [What we believe] | [How to test] | [What would confirm] | [Duration] |
```

## Example Output

```markdown
## Product-Market Fit Analysis: ScheduleBot (AI Meeting Scheduler for Sales Teams)

### Executive Summary

ScheduleBot shows **emerging PMF** with a specific segment (SDRs at mid-market SaaS companies) but **weak PMF** with the broader market. The Sean Ellis test scores 38% "very disappointed"—just below the 40% threshold. Retention is strong (68% Day-30) but NPS is moderate (32) with detractors citing "too many edge cases." The clearest PMF signal is that **42% of new users come from referrals within the same company**, suggesting strong word-of-mouth within organizations once adopted. Primary recommendation: **narrow focus to the highest-fit segment (SDRs) and nail their workflow before expanding.**

### Context

**Product:** ScheduleBot - AI-powered meeting scheduling assistant
**Target Market:** Sales teams at B2B companies (100-1000 employees)
**Stage:** GA (launched 8 months ago)
**Current Users:** 2,847 active users across 312 companies
**MRR:** $48,000
**Analysis Date:** January 2026

---

### Quantitative PMF Assessment

#### Sean Ellis Test

**Question:** "How would you feel if you could no longer use ScheduleBot?"

| Response | Count | Percentage |
|----------|-------|------------|
| Very Disappointed | 84 | **38%** |
| Somewhat Disappointed | 102 | 46% |
| Not Disappointed | 35 | 16% |

**Sample Size:** 221 responses (7.7% of active users)

**PMF Score:** 38% very disappointed
**Benchmark:** 40%+ = strong PMF
**Assessment:** **Emerging** (just below threshold)
**Confidence:** **High** (large sample, representative distribution)

**Segmented Results:**
| Segment | Very Disappointed | Sample |
|---------|-------------------|--------|
| SDRs at SaaS companies | **52%** | n=67 |
| Account Executives | 34% | n=89 |
| Customer Success | 28% | n=41 |
| Other roles | 22% | n=24 |

**Insight:** PMF is **strong for SDRs** (52%) but weak for other roles. This suggests we may be spreading too thin.

---

#### Retention Analysis

| Period | Rate | B2B SaaS Benchmark | Status |
|--------|------|-----------|--------|
| Day 1 | 78% | 70% | ✅ Above |
| Day 7 | 71% | 55% | ✅ Above |
| Day 30 | 68% | 40% | ✅ Above |
| Day 90 | 54% | 30% | ✅ Above |

**Retention Curve:**

```
100%│●
    │ ●
 80%│  ●
    │   ●●
 60%│     ●●●●●●●●●●  ← Flattening at ~55%
    │
 40%│
    │
    │
  0%└──────────────────
    D1 D7 D14 D30  D60  D90
```

**Assessment:** **Strong** — Retention significantly above benchmark and curve flattens, indicating core users find lasting value.
**Confidence:** **High** (8 months of cohort data)

**Concern:** Early cohorts (month 1-2) retain at 62% D90; recent cohorts (month 6-7) retain at 48%. **Trend is declining.** May indicate market saturation among early adopters.

---

#### Net Promoter Score

**NPS Score:** **32**
**Benchmark:** 50+ = strong, 20-50 = moderate, <20 = weak

| Category | Percentage | Key Themes |
|----------|------------|------------|
| Promoters (9-10) | 41% | "Saves me 2+ hours/week"; "Prospects always find a time" |
| Passives (7-8) | 33% | "Works well but not magical"; "Wish it handled reschedules better" |
| Detractors (0-6) | 26% | "Too many edge cases"; "Confused my prospects"; "Expensive for what it does" |

**Assessment:** **Emerging** — Moderate NPS with clear improvement themes.
**Confidence:** **Medium** (182 responses)

**Detractor Deep Dive:**
- 45% of detractors cite "edge case handling" (complex timezone, recurring meetings)
- 30% cite "confused my prospect" (AI made wrong assumptions)
- 25% cite "not worth the price" (value perception issue)

---

#### Organic Growth

| Metric | Value | Trend | Benchmark |
|--------|-------|-------|-----------|
| % Organic Acquisition | 34% | → Stable | 50%+ = healthy |
| Referral Rate | 12% | ↑ Growing | 10%+ = good |
| Within-company referral | **42%** | ↑ Strong | Novel metric |
| Viral Coefficient (K) | 0.4 | → Stable | >0.5 = healthy |
| Organic Search Traffic | 18% of total | ↑ Growing | Good sign |

**Assessment:** **Emerging** — Paid acquisition still dominant (48%), but organic channels growing.
**Confidence:** **Medium** (attribution has some gaps)

**Key Insight:** Within-company referrals (42%) are exceptionally high. When one user adopts, teammates follow. This is a **strong PMF signal** for team adoption even if individual PMF is emerging.

---

### Qualitative PMF Assessment

#### Customer Enthusiasm Signals

| Signal | Evidence | PMF Indication |
|--------|----------|----------------|
| Complain when features break | Yes—3 support tickets within 1 hour when booking flow had a bug | **Strong** |
| Proactively suggest features | Yes—47 feature requests this month, mostly around reschedule handling | **Strong** |
| Defend product to skeptics | Mixed—some LinkedIn praise, but no viral advocacy | **Moderate** |
| Would pay more if asked | 67% said yes (to 20% increase) in survey | **Strong** |

**Assessment:** **Emerging to Strong** — Users care enough to complain and request, willing to pay more.

#### Usage Depth and Frequency

| Signal | Evidence | PMF Indication |
|--------|----------|----------------|
| Power user percentage | 23% use daily (5+ bookings/week) | **Moderate** |
| Return without prompting | 71% weekly return rate | **Strong** |
| Usage trend over time | Per-user bookings growing 8% month-over-month | **Strong** |
| Unexpected use cases | Users scheduling internal meetings, not just external | **Emerging opportunity** |

**Assessment:** **Strong** — Usage is sticky and growing per user.

#### Competitive Dynamics

| Signal | Evidence | PMF Indication |
|--------|----------|----------------|
| Switching TO us from Calendly | 31% of users came from Calendly | **Strong** |
| Switching TO us from Chili Piper | 12% of users came from Chili Piper | **Moderate** |
| Switching FROM us to competitors | 8% of churned users cited "switching to X" | **Moderate concern** |
| Win rate vs. Calendly | 42% when head-to-head | **Moderate** |

**Assessment:** **Emerging** — Winning some competitive deals but not dominant.

**Switching reasons TO us:** "AI saves time" (48%), "Better Salesforce integration" (31%), "Sales-specific features" (21%)
**Switching reasons FROM us:** "Too expensive" (45%), "Too many errors" (35%), "Switched to bundled solution" (20%)

#### Market Pull

| Signal | Evidence | PMF Indication |
|--------|----------|----------------|
| Demand exceeds capacity | No—sales capacity available | **Weak** |
| Feature requests beyond roadmap | Yes—requesting AI prep, recording integration | **Moderate** |
| Partnership/integration requests | 4 requests from CRMs this quarter | **Moderate** |
| Organic inbound inquiries | Growing 15% month-over-month | **Strong** |

**Assessment:** **Emerging** — Interest growing but not overwhelming demand.

---

### Overall PMF Synthesis

#### Indicator Summary

| Category | Assessment | Confidence | Weight |
|----------|------------|------------|--------|
| Sean Ellis Test | Emerging (38%) | High | 25% |
| Retention | Strong (68% D30) | High | 30% |
| NPS | Emerging (32) | Medium | 15% |
| Organic Growth | Emerging (34%) | Medium | 15% |
| Qualitative Signals | Emerging-Strong | Medium | 15% |

#### PMF Status Determination

**Overall PMF Assessment:** **Emerging PMF**

**Confidence Level:** **High** — Multiple data sources, adequate sample sizes, 8 months of data.

**Key Evidence Supporting Emerging PMF:**
1. **Strong retention** (68% D30, significantly above benchmark) indicates core users find lasting value
2. **Within-company viral spread** (42% of new users from same company) shows word-of-mouth working
3. **Segment-specific strong PMF** (52% very disappointed among SDRs) indicates we've found a beachhead
4. **Willingness to pay more** (67%) suggests value perception is solid

**Key Concerns:**
1. **Declining retention trend** in recent cohorts (62% → 48% D90) is a warning sign
2. **Detractor feedback** around edge cases suggests product quality gaps
3. **Weak PMF in non-SDR segments** (22-34% very disappointed) indicates we're spreading too thin
4. **Paid acquisition dominance** (48%) masks whether organic demand can sustain growth

---

### Recommendations

#### Primary Recommendation: NARROW AND NAIL

ScheduleBot has **strong PMF with SDRs** but only **emerging PMF with the broader sales market**. Rather than trying to fix PMF across all segments, we recommend:

**Strategy: Narrow focus to SDRs, achieve unambiguous PMF, then expand.**

| Priority | Action | Expected Impact | Timeline |
|----------|--------|-----------------|----------|
| **P0** | Rebuild positioning and marketing around SDRs specifically | Improve Sean Ellis to 45%+ in target segment | 4 weeks |
| **P0** | Fix top 5 edge cases causing detractor feedback | Reduce "confused my prospect" complaints by 50% | 6 weeks |
| **P1** | Launch SDR-specific workflow features (cadence integration) | Increase daily usage from 23% to 35% | 8 weeks |
| **P1** | Implement within-company referral program (leverage 42% organic) | Increase K-factor from 0.4 to 0.6 | 4 weeks |
| **P2** | Investigate declining retention in recent cohorts | Identify and fix root cause | 4 weeks |
| **P2** | Pause expansion into AE/CS segments until SDR PMF is 50%+ | Focus resources | Ongoing |

---

### Validation Experiments

| Hypothesis | Experiment | Success Criteria | Timeline |
|------------|------------|------------------|----------|
| SDRs are our best segment | Run Sean Ellis survey to SDRs-only cohort after positioning shift | 50%+ very disappointed | 6 weeks |
| Edge case fixes will reduce detractors | Deploy fixes; re-survey NPS in affected cohort | NPS increases from 32 to 45+ | 8 weeks |
| Within-company viral can scale | Launch referral program; measure K-factor change | K-factor increases to 0.6+ | 8 weeks |
| Declining retention is fixable | Interview recent churned users from month 6-7 cohorts | Identify 2-3 fixable causes | 3 weeks |

---

### PMF Scorecard (Track Over Time)

| Metric | Current | Target | Gap |
|--------|---------|--------|-----|
| Sean Ellis (all) | 38% | 45% | -7% |
| Sean Ellis (SDRs) | 52% | 60% | -8% |
| D30 Retention | 68% | 75% | -7% |
| NPS | 32 | 50 | -18 |
| Organic Acquisition | 34% | 50% | -16% |
| K-Factor | 0.4 | 0.6 | -0.2 |

**Next Review:** [Date + 8 weeks]
```

## Customization Guide

- **For B2B Products:** Weight retention and NPS heavily; Sean Ellis sample should be decision-makers
- **For B2C Products:** Weight DAU/MAU ratio and viral metrics; Sean Ellis requires larger samples
- **For Marketplace Products:** Run separate PMF analysis for supply and demand sides
- **For Enterprise Products:** Adjust benchmarks; enterprise retention should be higher; longer sales cycles affect organic metrics

## Techniques Used

- **ST-01 (Clear Objective Statement):** Explicit goal of determining PMF status with evidence
- **ST-02 (Structured Sequential Instructions):** Systematic progression through quantitative and qualitative indicators
- **DS-01 (Framework Application):** Direct application of PMF assessment methodology (Sean Ellis, retention curves, NPS)
- **RT-02 (Multi-Dimensional Analysis):** Evaluation across multiple PMF dimensions
- **QA-02 (Adversarial Thinking):** False-positive prevention challenges vanity metrics and cherry-picking
- **DS-06 (Prioritization Guidance):** Recommendations prioritized by impact on PMF indicators

## Related Prompts

- [Lean Canvas Analysis](../stage-4-business-model/lean_canvas_analysis.md) - Pre-launch business model validation
- [Jobs to be Done Analysis](jobs_to_be_done_analysis.md) - Understanding customer needs driving PMF
- [Value Proposition Canvas Analysis](value_proposition_canvas_analysis.md) - Value alignment assessment
- [Kano Model Analysis](../../domain-business-strategy/analysis/kano_model_analysis.md) - Feature prioritization for PMF improvement
