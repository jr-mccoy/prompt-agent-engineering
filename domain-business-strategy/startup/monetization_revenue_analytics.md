---
title: "Revenue Analytics"
category: startup/monetization
description: "Analyze revenue metrics for an Android app — ARPU/ARPPU formulas, LTV calculation, subscription churn analysis, trial-to-paid conversion benchmarks, cohort revenue analysis, MRR/ARR tracking, and revenue forecasting for solo developers"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
  - QA-02
difficulty: intermediate
tags:
  - monetization
  - android
  - analytics
  - revenue-metrics
  - ltv
  - churn
  - mrr
  - cohort-analysis
  - solo-developer
updated: "2026-02-11"
---

# Revenue Analytics

**Objective:** Analyze revenue metrics for an Android app — including ARPU/ARPPU formulas with calculation examples, LTV modeling, subscription churn analysis (voluntary vs. involuntary), trial-to-paid conversion benchmarks, cohort-based revenue analysis, MRR/ARR tracking, and revenue forecasting with confidence intervals — so that you make pricing, feature, and growth decisions based on real data rather than gut feeling.

**When to Use:** Use this once you have paying users (even a handful) and need to understand your revenue health. Revenue analytics is not a "later" activity — start tracking from Day 1 of monetization. This prompt covers the metrics that matter, how to calculate them, what benchmarks to compare against, and how to forecast future revenue. Use it alongside `monetization_pricing_strategy.md` and `monetization_subscription_design.md` to close the feedback loop between pricing decisions and revenue outcomes.

---

## Context Gathering

Before analyzing revenue, gather essential context:

1. **Current Revenue State:**
   - "What is your current monthly revenue (gross and net of Google's commission)?"
   - "How many paying users do you have? How many total active users?"
   - "What monetization models are you using (subscription, IAP, ads, hybrid)?"
   - "How long have you been monetized? Do you have at least 3 months of data?"

2. **Subscription Details (if applicable):**
   - "What subscription plans do you offer (monthly, annual, tiers)?"
   - "What is your current trial length and trial-to-paid conversion rate?"
   - "What is your monthly churn rate? Do you track voluntary vs. involuntary churn?"
   - "What are your grace period and account hold settings?"

3. **User Metrics:**
   - "What is your MAU (Monthly Active Users)?"
   - "What is your DAU/MAU ratio?"
   - "What is your Day 1, Day 7, Day 30 retention?"
   - "What is your average session length and sessions per user per day?"

4. **Data Infrastructure:**
   - "What analytics tools are you using (Firebase Analytics, Mixpanel, custom)?"
   - "Do you have server-side revenue validation or only client-side?"
   - "Can you segment users by acquisition source, country, and plan type?"
   - "Do you have a spreadsheet or dashboard for revenue tracking?"

5. **Goals:**
   - "What is your revenue target for the next 3, 6, 12 months?"
   - "Are you optimizing for revenue growth, profitability, or user growth?"
   - "What specific decision are you trying to make with this analysis?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before analyzing ANY revenue metrics, you MUST:**

1. **Verify data accuracy** — Revenue data must reconcile with Google Play Console reports. If your internal numbers differ from Google's payout reports by more than 5%, you have a tracking issue. Fix it before making any decisions.
2. **Verify sufficient sample size** — Metrics calculated from fewer than 30 data points are unreliable. If you have 12 subscribers and 2 churned, your churn rate is technically 16.7%, but the confidence interval is so wide that the number is meaningless. Wait for more data or use wider time windows.
3. **Verify time period consistency** — Always compare like-with-like. Monthly churn in January (31 days) should not be compared directly with February (28 days) without normalization. Use 30-day rolling windows instead of calendar months.
4. **Verify you are tracking net revenue** — Google takes 15% (first $1M/year) or 30%. All revenue metrics should use net revenue (what you actually receive) for business decisions. Use gross revenue only when comparing with industry benchmarks that use gross.
5. **Verify refund exclusion** — Google Play refund rates are typically 2-5%. Exclude refunded transactions from revenue calculations or your metrics will be inflated.
6. **Acceptable null result** — It is valid to conclude that you do not have enough data to perform meaningful analysis. If you have fewer than 50 paying users or less than 3 months of data, focus on the basics (total revenue, subscriber count, conversion rate) and defer advanced analytics.

### False-Positive Prevention

- Do NOT celebrate a conversion rate spike without checking if it was caused by a one-time event (feature launch, seasonal effect, press coverage)
- Do NOT calculate LTV from fewer than 6 months of cohort data — early cohorts are biased toward enthusiasts
- Do NOT compare your metrics to benchmarks from different app categories — a 5% conversion rate in games means something different than in productivity
- Do NOT ignore involuntary churn (payment failures) — it is typically 20-40% of total churn and is recoverable
- Do NOT use averages when medians are more appropriate — one whale paying $99/month skews your ARPU
- Do NOT forecast more than 12 months out — the error bars become wider than the forecast itself
- DO track revenue metrics weekly, review monthly, and do deep analysis quarterly
- DO segment every metric by plan type, geography, and acquisition source
- DO compare month-over-month AND year-over-year to account for seasonality
- DO track leading indicators (trial starts, engagement) alongside lagging indicators (revenue, churn)
- DO document your metric definitions so they remain consistent as your team grows

---

### Phase 1: Metric Definitions

#### 1.1 Core Revenue Metrics

**ARPU (Average Revenue Per User)**
```
Formula:
  ARPU = Total Revenue / Total Active Users (in period)

Example:
  Monthly revenue: $3,000
  MAU: 10,000
  ARPU = $3,000 / 10,000 = $0.30/user/month

What it tells you:
  How effectively you are monetizing your entire user base,
  including non-paying users. Low ARPU with high MAU means
  you have a conversion problem, not a pricing problem.

Benchmarks (monthly, gross revenue):
  - Casual games: $0.05-$0.20
  - Productivity apps: $0.10-$0.50
  - Fitness/health apps: $0.20-$0.80
  - Professional tools: $0.50-$2.00
  - Social apps: $0.05-$0.15
```

**ARPPU (Average Revenue Per Paying User)**
```
Formula:
  ARPPU = Total Revenue / Total Paying Users (in period)

Example:
  Monthly revenue: $3,000
  Paying users: 300
  ARPPU = $3,000 / 300 = $10.00/paying user/month

What it tells you:
  How much each paying user spends on average.
  If ARPPU equals your subscription price, all revenue is
  subscriptions. If ARPPU > subscription price, you have
  additional IAP revenue or multiple tiers.

Benchmarks (monthly, gross revenue):
  - Single-tier subscription: ≈ subscription price
  - Multi-tier: $8-$15/paying user
  - IAP-heavy games: $5-$50+ (whale distribution)
  - Hybrid (sub + IAP): $10-$25
```

**Conversion Rate**
```
Formula:
  Conversion Rate = Paying Users / Total Active Users × 100

Example:
  Paying users: 300
  MAU: 10,000
  Conversion = 300 / 10,000 × 100 = 3.0%

Benchmarks:
  - Freemium apps (overall): 2-5%
  - Subscription apps: 1-4%
  - Games with IAP: 2-7%
  - Productivity/professional: 5-10%
  - Apps with ads + premium: 3-8%
```

#### 1.2 Subscription-Specific Metrics

**MRR (Monthly Recurring Revenue)**
```
Formula:
  MRR = Sum of all active subscription revenue for the month
      = (Monthly subscribers × monthly price) + (Annual subscribers × annual price / 12)

Components:
  New MRR:        Revenue from new subscribers this month
  Expansion MRR:  Revenue from upgrades (Basic → Premium)
  Contraction MRR: Revenue lost from downgrades (Premium → Basic)
  Churned MRR:    Revenue lost from cancellations
  Reactivation MRR: Revenue from returning subscribers

Net New MRR = New + Expansion + Reactivation - Contraction - Churned

Example:
  150 monthly subscribers × $4.99 = $748.50
  100 annual subscribers × $47.99/12 = $399.92
  MRR = $1,148.42

ARR (Annual Recurring Revenue):
  ARR = MRR × 12 = $13,781.04
  (This is a projection, not a guarantee. Use for planning, not celebration.)
```

**Churn Rate**
```
Formula (subscriber churn):
  Monthly Churn = Subscribers Lost / Subscribers at Start of Month × 100

Formula (revenue churn):
  Revenue Churn = MRR Lost / MRR at Start of Month × 100

Types of churn:
  Voluntary: User actively cancels (billing issue, dissatisfied, competitor)
  Involuntary: Payment fails (expired card, insufficient funds, bank decline)

Example:
  Start of month: 500 subscribers
  Voluntary cancellations: 25
  Involuntary failures (not recovered): 15
  Total churned: 40
  Churn rate: 40/500 = 8.0%
    Voluntary: 25/500 = 5.0%
    Involuntary: 15/500 = 3.0%

Benchmarks (monthly):
  - Excellent: <4%
  - Good: 4-6%
  - Average: 6-10%
  - Concerning: 10-15%
  - Critical: >15%

  Involuntary churn should be 20-40% of total churn.
  If involuntary churn is >50% of total, your grace period
  and account hold settings need optimization.
```

**Trial-to-Paid Conversion**
```
Formula:
  Trial Conversion = Users Who Paid After Trial / Users Who Started Trial × 100

Benchmarks:
  - Excellent: 60%+ (requires payment method upfront)
  - Good: 40-60%
  - Average: 25-40%
  - Below average: 15-25%
  - Poor: <15%

  Note: Google Play free trials automatically convert if user
  does not cancel. Conversion rates are therefore higher than
  "opt-in to pay" models. The benchmarks above assume auto-convert.

  Without payment method upfront (free trial no payment info):
  - Good: 10-18%
  - Average: 5-10%
  - Poor: <5%
```

#### 1.3 LTV (Lifetime Value)

**Simple LTV Formula**
```
Formula:
  LTV = ARPPU / Monthly Churn Rate

Example:
  ARPPU: $8.00/month (net of Google's commission)
  Monthly churn: 7%
  LTV = $8.00 / 0.07 = $114.29

This tells you: The average paying user will generate $114.29
in total revenue over their lifetime.

Limitation: Assumes constant churn rate, which is rarely true.
Early-month churn is typically higher than later-month churn.
```

**Improved LTV with Cohort Survival**
```
Formula:
  LTV = ARPPU × (Sum of survival rates for each month)
  LTV = ARPPU × (S₁ + S₂ + S₃ + ... + Sₙ)

Where Sₙ = percentage of cohort still active in month N

Example:
  ARPPU: $8.00/month
  Survival rates: Month 1: 100%, Month 2: 85%, Month 3: 75%,
  Month 4: 68%, Month 5: 63%, Month 6: 59%, Month 7: 56%,
  Month 8: 54%, Month 9: 52%, Month 10: 51%, Month 11: 50%,
  Month 12: 49%

  LTV (12-month) = $8.00 × (1.00 + 0.85 + 0.75 + 0.68 + 0.63
    + 0.59 + 0.56 + 0.54 + 0.52 + 0.51 + 0.50 + 0.49)
  LTV (12-month) = $8.00 × 7.62 = $60.96

  This is more conservative and more accurate than the simple formula.
```

**LTV:CAC Ratio**
```
Formula:
  LTV:CAC = LTV / Customer Acquisition Cost

Benchmarks:
  - Healthy: 3:1 or higher (every $1 spent on acquisition generates $3+)
  - Break-even: 1:1 (you are paying $1 to get $1 back — unsustainable)
  - Danger zone: <1:1 (you are losing money on every acquired user)

For organic-only solo developers, CAC is often near $0 (organic discovery),
making LTV:CAC theoretically infinite. This changes dramatically if you
start running paid acquisition (Google Ads, social media ads).
```

---

### Phase 2: Benchmark Comparison

#### 2.1 Revenue Health Scorecard

Rate your app on each metric. Green = healthy, yellow = needs attention, red = critical.

| Metric | Your Value | Green | Yellow | Red |
|--------|-----------|-------|--------|-----|
| **Conversion rate** | [X]% | >5% | 2-5% | <2% |
| **Monthly churn** | [X]% | <5% | 5-10% | >10% |
| **Trial-to-paid** | [X]% | >50% | 30-50% | <30% |
| **ARPU** | $[X] | >$0.50 | $0.10-$0.50 | <$0.10 |
| **ARPPU** | $[X] | >$8 | $4-$8 | <$4 |
| **LTV** | $[X] | >$50 | $20-$50 | <$20 |
| **MRR growth** | [X]% | >10% | 0-10% | Negative |
| **Net revenue churn** | [X]% | <3% | 3-8% | >8% |
| **Annual plan %** | [X]% | >40% | 20-40% | <20% |
| **Involuntary churn %** | [X]% of total | <25% | 25-40% | >40% |

**Interpreting the scorecard:**
- 8+ green: Revenue engine is healthy. Focus on growth.
- 5-7 green: Good foundation with specific areas to improve.
- 3-4 green: Significant issues. Prioritize the red metrics.
- <3 green: Revenue model may need fundamental rethinking.

#### 2.2 Category Benchmarks

| Category | Median Conversion | Median Monthly Churn | Median ARPU | Median LTV |
|----------|------------------|---------------------|-------------|-----------|
| Productivity | 4-6% | 5-8% | $0.30-$0.60 | $40-$80 |
| Fitness/Health | 3-5% | 8-12% | $0.40-$1.00 | $30-$60 |
| Education | 2-4% | 6-10% | $0.20-$0.50 | $25-$50 |
| Finance/Budgeting | 3-5% | 4-7% | $0.30-$0.70 | $50-$100 |
| Photo/Video | 2-4% | 8-12% | $0.15-$0.40 | $20-$40 |
| Games (subscription) | 1-3% | 10-18% | $0.10-$0.30 | $10-$25 |
| Utility/Tools | 5-10% | 3-6% | $0.20-$0.40 | $40-$80 |
| Music/Audio | 2-4% | 8-14% | $0.20-$0.50 | $20-$40 |

**How to use these benchmarks:** Find your category row. If your metric is below the range, that is a priority area for improvement. If you are above the range, you are performing well on that metric. Benchmarks are approximate and vary by geography, app maturity, and competitive landscape.

---

### Phase 3: Cohort Analysis

#### 3.1 Subscription Cohort Table

Track each monthly cohort of new subscribers through their lifecycle:

```
Cohort: January 2026 New Subscribers

| Month | Subscribers Remaining | Survival Rate | Revenue (cumulative) |
|-------|----------------------|---------------|---------------------|
| Jan (Month 0) | 100 | 100% | $499 |
| Feb (Month 1) | 82 | 82% | $908 |
| Mar (Month 2) | 71 | 71% | $1,262 |
| Apr (Month 3) | 64 | 64% | $1,581 |
| May (Month 4) | 59 | 59% | $1,875 |
| Jun (Month 5) | 55 | 55% | $2,149 |

Key observations:
- Biggest drop: Month 0→1 (18% churn — typical "trial tourists")
- Stabilizing at: ~5% monthly churn after Month 3
- Payback period: Revenue exceeds CAC at Month [X]
- Projected 12-month LTV: $[calculated from survival curve]
```

#### 3.2 Cohort Comparison Matrix

Compare cohorts to identify trends:

```
                    Survival Rate at Month N
Cohort    | M1    | M2    | M3    | M6    | M12
----------+-------+-------+-------+-------+------
Oct 2025  | 80%   | 68%   | 60%   | 48%   | 38%
Nov 2025  | 82%   | 70%   | 63%   | 50%   | —
Dec 2025  | 78%   | 65%   | 58%   | —     | —
Jan 2026  | 85%   | 73%   | 66%   | —     | —
Feb 2026  | 84%   | 72%   | —     | —     | —
Mar 2026  | 87%   | —     | —     | —     | —

Observations:
- M1 survival improving over time (80% → 87%) — onboarding or product improvements working
- Dec 2025 cohort underperformed — holiday subscribers may be less committed
- Jan 2026 cohort significantly better — investigate what changed (new feature? better paywall?)
```

#### 3.3 Revenue Cohort Spreadsheet Template

```
=== Revenue Cohort Tracker (Google Sheets / Excel) ===

Sheet 1: "Raw Data"
Columns:
  A: User ID
  B: Subscription start date
  C: Plan type (monthly/annual)
  D: Price
  E: Cohort month (=TEXT(B,"YYYY-MM"))
  F: Current status (active/churned/paused)
  G: Churn date (if applicable)
  H: Churn reason (voluntary/involuntary)
  I: Months active (=IF(F="active", DATEDIF(B,TODAY(),"M"), DATEDIF(B,G,"M")))
  J: Total revenue (=D * I * 0.85)   [net of Google's 15%]

Sheet 2: "Cohort Pivot"
  Rows: Cohort months
  Columns: Month 0, Month 1, Month 2, ..., Month 12
  Values: Count of active subscribers (survival)

Sheet 3: "Metrics Dashboard"
  - MRR trend (line chart)
  - Churn rate trend (line chart)
  - Conversion funnel (funnel chart)
  - LTV by cohort (bar chart)
  - Revenue by plan type (pie chart)

Sheet 4: "Forecast"
  - 3-month, 6-month, 12-month projections
  - Pessimistic, expected, optimistic scenarios
```

#### 3.4 Churn Deep Dive

**Voluntary vs. Involuntary Churn Breakdown:**

| Churn Type | Typical Share | Causes | Solutions |
|-----------|-------------|--------|----------|
| **Voluntary - Feature gap** | 15-25% of total | Missing features users need | Feature prioritization from churn surveys |
| **Voluntary - Value mismatch** | 10-20% of total | Users don't use premium enough | Better onboarding for premium features |
| **Voluntary - Competitor** | 5-15% of total | Competitor offers better deal | Competitive monitoring, loyalty perks |
| **Voluntary - Price** | 5-15% of total | Perceived too expensive | Pricing review, annual plan promotion |
| **Involuntary - Card expired** | 15-25% of total | Credit card expired | Grace period (7 days), account hold (30 days) |
| **Involuntary - Insufficient funds** | 5-10% of total | Temporary payment issue | Google's billing retry (automatic) |
| **Involuntary - Bank decline** | 5-10% of total | Bank-side decline | Retry logic, user notification |

**Involuntary churn recovery checklist:**
1. Enable grace period: 7 days (maintain premium access while Google retries payment)
2. Enable account hold: 30 days (suspend access but preserve subscription)
3. Send push notification on Day 1 of grace period: "Your payment didn't go through. Update your payment method to keep Premium."
4. Send push notification on Day 5: "Your Premium access ends in 2 days unless payment is updated."
5. Enable resubscription: Let expired subscribers easily resubscribe without a new trial.

**Expected recovery rate:** 15-25% of involuntary churn with grace period + account hold enabled.

---

### Phase 4: Revenue Forecasting

#### 4.1 Bottom-Up Forecast Model

```
Month N Forecast:

Starting subscribers:     [Current subscribers]
+ New subscribers:        [MAU × conversion rate]
- Voluntary churn:        [Subscribers × voluntary churn rate]
- Involuntary churn:      [Subscribers × involuntary churn rate × (1 - recovery rate)]
+ Reactivations:          [Previously churned × reactivation rate]
= Ending subscribers:     [Calculated]

MRR = (Monthly subscribers × monthly price × 0.85)
    + (Annual subscribers × annual price / 12 × 0.85)

Repeat for each future month.
```

#### 4.2 Three-Scenario Forecast

| Assumption | Pessimistic | Expected | Optimistic |
|-----------|------------|---------|-----------|
| MAU growth/month | 2% | 5% | 10% |
| Free-to-trial conversion | 2% | 4% | 7% |
| Trial-to-paid conversion | 30% | 50% | 65% |
| Monthly churn | 12% | 7% | 4% |
| Annual plan adoption | 20% | 40% | 55% |
| Involuntary churn recovery | 10% | 20% | 30% |

**Example forecast (starting with 5,000 MAU, $4.99/mo or $47.99/yr):**

| Month | Pessimistic MRR | Expected MRR | Optimistic MRR |
|-------|----------------|-------------|---------------|
| 1 | $127 | $424 | $1,061 |
| 3 | $298 | $1,142 | $3,450 |
| 6 | $561 | $2,584 | $9,218 |
| 9 | $785 | $4,020 | $16,400 |
| 12 | $968 | $5,350 | $24,800 |

**Important:** These are illustrative. Your actual numbers depend on your specific conversion rates, churn rates, and growth rates. Use your real data to populate the model.

#### 4.3 Forecasting Confidence Intervals

```
Rule of thumb for forecast confidence:

Month 1-3:   ±20% of expected (high confidence)
Month 4-6:   ±35% of expected (moderate confidence)
Month 7-9:   ±50% of expected (low confidence)
Month 10-12: ±70% of expected (directional only)

Translation: A "Month 12 MRR = $5,000" forecast really means
"somewhere between $1,500 and $8,500 depending on how things go."

Use forecasts for:
  ✅ Setting directional goals
  ✅ Planning expenses (don't commit to costs you can only afford in the optimistic scenario)
  ✅ Identifying the scenarios that matter most (e.g., "if churn drops 2%, revenue doubles")
  ✅ Communicating potential to stakeholders

Do NOT use forecasts for:
  ❌ Precise financial planning beyond 3 months
  ❌ Justifying expenses that require the optimistic scenario
  ❌ Comparing yourself to well-funded competitors' growth rates
```

#### 4.4 Sensitivity Analysis: What Moves Revenue Most?

```
Rank of impact on 12-month revenue (from highest to lowest):

1. Churn rate reduction (-2% churn → +25-40% 12-month revenue)
   Why: Compound effect — retained users generate revenue every month

2. Conversion rate increase (+2% conversion → +20-30% 12-month revenue)
   Why: More subscribers entering the funnel each month

3. Price increase (+$2/month → +15-25% 12-month revenue)
   Why: Direct multiplier on existing subscribers (if churn doesn't spike)

4. MAU growth (+50% MAU → +10-20% 12-month revenue)
   Why: Amplifies conversion, but new users take time to convert

5. Annual plan adoption (+20% annual adoption → +5-15% 12-month revenue)
   Why: Reduces effective churn (annual users have ~80% renewal rate)

Key insight for solo developers:
  Reducing churn is almost always more impactful than acquiring new users.
  If you have a churn problem, no amount of growth will save you.
```

---

### Phase 5: Action Planning

#### 5.1 Revenue Improvement Decision Matrix

| If Your Problem Is... | Primary Metric to Track | Top 3 Actions | Expected Impact |
|----------------------|------------------------|--------------|----------------|
| **Low conversion** (<2%) | Trial start rate, paywall engagement | 1. Improve paywall copy/design 2. Add free trial 3. Better premium feature visibility | +50-200% conversion |
| **High voluntary churn** (>8%) | Cancellation reasons, feature usage | 1. Churn survey 2. Premium onboarding 3. Feature improvement | -20-40% churn |
| **High involuntary churn** (>4%) | Grace period recovery, card failure rate | 1. Enable grace period (7 days) 2. Enable account hold (30 days) 3. Payment failure notifications | -30-60% involuntary churn |
| **Low ARPPU** (<$5) | Plan distribution, upsell conversion | 1. Price increase analysis 2. Higher-tier offering 3. IAP alongside subscription | +20-50% ARPPU |
| **Poor trial conversion** (<30%) | Trial engagement, feature usage during trial | 1. Trial onboarding emails 2. Feature discovery prompts 3. Shorten trial (if >7 days) | +15-40% trial conversion |
| **Low annual adoption** (<25%) | Paywall plan selection, annual vs. monthly CTA | 1. Default to annual on paywall 2. Show savings prominently 3. "Best Value" badge | +20-50% annual adoption |

#### 5.2 Monthly Revenue Review Template

```
## Monthly Revenue Review — [Month Year]

### Headline Metrics
| Metric | This Month | Last Month | MoM Change | 3-Month Avg |
|--------|-----------|------------|------------|-------------|
| MRR | $[X] | $[X] | [+/-X%] | $[X] |
| Total subscribers | [N] | [N] | [+/-N] | [N] |
| New subscribers | [N] | [N] | [+/-N] | [N] |
| Churned subscribers | [N] | [N] | [+/-N] | [N] |
| Conversion rate | [X]% | [X]% | [+/-X pp] | [X]% |
| Monthly churn | [X]% | [X]% | [+/-X pp] | [X]% |
| Trial-to-paid | [X]% | [X]% | [+/-X pp] | [X]% |
| ARPU | $[X] | $[X] | [+/-X%] | $[X] |

### MRR Breakdown
| Component | Amount | % of MRR |
|-----------|--------|----------|
| New MRR | $[X] | [X]% |
| Expansion MRR | $[X] | [X]% |
| Reactivation MRR | $[X] | [X]% |
| Contraction MRR | -$[X] | [X]% |
| Churned MRR | -$[X] | [X]% |
| Net New MRR | $[X] | — |

### Churn Analysis
| Churn Type | Count | Rate | Notes |
|-----------|-------|------|-------|
| Voluntary | [N] | [X]% | Top reason: [reason] |
| Involuntary | [N] | [X]% | Recovery rate: [X]% |
| Total | [N] | [X]% | |

### Plan Distribution
| Plan | Subscribers | % of Total | MRR Contribution |
|------|-----------|-----------|-----------------|
| Monthly | [N] | [X]% | $[X] |
| Annual | [N] | [X]% | $[X] |

### Top Insights
1. [What improved and why]
2. [What declined and why]
3. [What action to take next month]

### Next Month Focus
- [ ] [Specific action 1]
- [ ] [Specific action 2]
- [ ] [Specific action 3]
```

#### 5.3 Quarterly Deep Dive Topics

| Quarter | Focus Area | Key Analysis |
|---------|-----------|-------------|
| Q1 | Cohort performance | Compare all cohorts from prior year. Which acquisition channels produce highest LTV? |
| Q2 | Pricing review | Run competitive benchmark update. Should prices change? |
| Q3 | Churn deep dive | Full voluntary/involuntary breakdown. Interview churned users if possible. |
| Q4 | Annual planning | Build 12-month forecast. Set revenue targets. Plan feature investments. |

---

## Expected Output

```markdown
# Revenue Analytics: [App Name] — [Period]

## Revenue Health Summary
| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| MRR | $[X] | — | [Growing/Flat/Declining] |
| Conversion rate | [X]% | [X]% (category avg) | [Above/At/Below] |
| Monthly churn | [X]% | [X]% (category avg) | [Above/At/Below] |
| Trial-to-paid | [X]% | [X]% (category avg) | [Above/At/Below] |
| LTV | $[X] | $[X] (category avg) | [Above/At/Below] |
| LTV:CAC | [X]:1 | 3:1 (healthy) | [Healthy/Marginal/Unhealthy] |

## Cohort Analysis
[Cohort survival table for last 6 months]
[Key observations about trends]

## Revenue Forecast (12-month)
| Scenario | Month 3 | Month 6 | Month 12 |
|----------|---------|---------|----------|
| Pessimistic | $[X] | $[X] | $[X] |
| Expected | $[X] | $[X] | $[X] |
| Optimistic | $[X] | $[X] | $[X] |

## Priority Actions
1. [Highest-impact action with expected result]
2. [Second-highest action with expected result]
3. [Third action with expected result]

## Metrics to Watch Next Month
- [Leading indicator 1]: Target [X]
- [Leading indicator 2]: Target [X]
- [Lagging indicator 1]: Target [X]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on building a complete revenue analytics practice, not just calculating metrics
- **ST-02** (Structured Sequential Instructions) — Five-phase process from metric definitions through action planning
- **RT-02** (Multi-Dimensional Analysis) — Revenue analyzed across multiple metrics, cohorts, segments, and time periods
- **CM-01** (Explicit Context Framing) — Context gathering about current revenue state, subscription details, and goals
- **DS-06** (Prioritization Guidance) — Sensitivity analysis ranking which levers move revenue most, action matrix by problem type
- **QA-02** (Adversarial Stress-Test) — Three-scenario forecasting with confidence intervals and explicit limitations

---

## Related Prompts

- `monetization_pricing_strategy.md` — Set the prices that revenue analytics will track and validate
- `monetization_subscription_design.md` — Design the subscription tiers that generate MRR
- `monetization_paywall_optimization.md` — Optimize the paywall conversion funnel
- `monetization_play_billing_implementation.md` — Implement the billing code that generates the revenue data
- `monetization_ad_placement_strategy.md` — Track ad revenue alongside subscription revenue
- `solo_dev_financial_planning.md` — Connect revenue analytics to personal financial planning

---

## Customization Guide

- **For ad-supported apps:** Replace subscription metrics with ad metrics: ARPDAU (Average Revenue Per Daily Active User), eCPM by format, fill rate by network, ad engagement rate. The cohort analysis framework still applies — track ARPDAU by acquisition cohort to understand which user segments generate the most ad revenue.
- **For hybrid models (subscription + ads):** Track both revenue streams separately AND combined. Key hybrid metric: "What percentage of revenue comes from subscribers vs. ads?" If ads contribute less than 15% of total revenue, consider removing them for subscribers as a premium perk rather than optimizing ad placement.
- **For apps with fewer than 100 subscribers:** Keep it simple. Track only: total subscribers, new this month, churned this month, MRR, and conversion rate. Cohort analysis and LTV calculations require more data to be meaningful. Focus on growing to 100 subscribers first.
- **For apps with IAP (in-app purchases) alongside subscriptions:** Segment revenue by type. IAP revenue is lumpy (whale-driven), while subscription revenue is predictable. Calculate ARPPU separately for IAP-only users, subscription-only users, and both. The "both" segment is your most valuable — understand what drives them.
- **For apps expanding internationally:** Build separate revenue dashboards per region. A blended global ARPU is misleading when your US ARPU is $1.20 and your India ARPU is $0.05. Regional cohort analysis reveals which markets are worth investing in localization and regional marketing.
