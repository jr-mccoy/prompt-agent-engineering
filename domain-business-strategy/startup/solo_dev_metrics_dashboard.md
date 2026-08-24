---
title: "Solo Developer Metrics Dashboard"
category: startup/business-operations
description: "Design a metrics dashboard for a solo app developer — the 5-7 metrics that actually matter, where to find each data source, weekly review cadence, avoiding vanity metrics, red/yellow/green thresholds, and action triggers — with metrics hierarchy, data source mapping, and weekly review template"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - CM-02
  - DS-06
difficulty: intermediate
tags:
  - solo-developer
  - startup
  - metrics
  - analytics
  - android
  - dashboard
  - retention
  - revenue
updated: "2026-02-11"
---

# Solo Developer Metrics Dashboard

**Objective:** Design a focused metrics dashboard for a solo app developer — identifying the 5-7 metrics that actually drive decisions, mapping each to its data source (Play Console, Firebase, RevenueCat, etc.), establishing a weekly review cadence that takes 15 minutes, defining red/yellow/green thresholds that trigger action, and building the discipline to look at data regularly without drowning in dashboards — producing a metrics system that fits a one-person operation.

**When to Use:** Use this prompt when you realize you have no idea how your app is actually performing beyond "downloads look okay," when you check your Play Console dashboard daily but never know what to do with the numbers, when you want to make data-driven decisions but don't know which data matters, or when you suspect you're celebrating vanity metrics (downloads) while ignoring the numbers that actually predict success (retention, revenue).

**Important context:** The analytics trap for solo developers comes in two forms. Form one: not tracking anything, making decisions based on vibes and gut feelings, then being surprised when things don't work. Form two: tracking everything, building complex dashboards with 30 metrics, then being overwhelmed and not actually using any of them. The sweet spot is 5-7 metrics reviewed weekly, with clear thresholds that tell you whether to celebrate, investigate, or panic. This guide builds that system.

---

## Context Gathering

Before designing your dashboard, understand your starting point:

1. **App Model:**
   - "Is your app free, freemium, subscription, or paid upfront?"
   - "What is your primary revenue source (subscriptions, in-app purchases, ads, one-time purchase)?"
   - "How many active users do you have approximately?"
   - "How long has your app been live on the Play Store?"

2. **Current Analytics:**
   - "What analytics tools do you currently have installed (Firebase Analytics, Mixpanel, etc.)?"
   - "Do you use RevenueCat, Adapty, or another subscription management tool?"
   - "Do you check your Play Console regularly?"
   - "What numbers do you currently look at, if any?"

3. **Business Goals:**
   - "What is your #1 business goal right now (grow users, improve retention, increase revenue)?"
   - "Are you trying to validate product-market fit or optimize an already-working product?"
   - "Do you have a target monthly revenue?"
   - "What would 'success' look like for you in 6 months?"

4. **Time Commitment:**
   - "How much time are you willing to spend on analytics per week?"
   - "Do you prefer dashboards (visual) or spreadsheets (manual but flexible)?"
   - "Do you want automated alerts or manual checks?"

---

## Instructions

### CRITICAL: Verification Requirements

1. **Metrics must be actionable** — Every metric on the dashboard must answer the question "what would I do differently if this number changed?" If the answer is "nothing," it doesn't belong on the dashboard.
2. **Data sources must be verified as accessible** — Don't recommend tracking D7 retention if the developer hasn't set up Firebase Analytics or an equivalent tool.
3. **Thresholds must be appropriate for the app's stage** — A 40% D1 retention rate is good for a new app and concerning for an established one. Context matters.
4. **Vanity metrics must be explicitly called out** — Downloads without retention context is the most common vanity metric trap. Address it directly.
5. **The review cadence must be sustainable** — A 15-minute weekly review is maintainable. A 2-hour daily analytics deep-dive is not.
6. **Acceptable null result:** If the developer has fewer than 100 daily active users, many metrics (churn rate, conversion rate) will be noisy and unreliable. The honest answer may be "focus on user acquisition first, then measure retention and conversion when you have statistical significance."

### False-Positive Prevention

- Do NOT recommend tracking 20+ metrics — a solo developer should track 5-7 core metrics and nothing more at first
- Do NOT treat downloads as a success metric — downloads without retention are noise. 10,000 downloads with 1% retention is worse than 1,000 downloads with 30% retention
- Do NOT recommend expensive analytics tools for early-stage apps — Firebase Analytics (free) covers 90% of what you need
- Do NOT set thresholds without acknowledging they vary by category — a social app and a productivity app have very different "good" retention benchmarks
- Do NOT recommend daily metric checking — it leads to over-reaction to normal fluctuations. Weekly is enough for solo developers.
- Do NOT ignore the denominator — "50 new subscribers" means nothing without knowing it's out of 500 trials (10% conversion, good) vs. 5,000 trials (1% conversion, terrible)
- DO explain what each metric means in plain language before asking developers to track it
- DO connect each metric to a specific business decision it influences
- DO recommend starting simple and adding metrics only when the simpler ones are well-understood
- DO emphasize that trends matter more than absolute numbers — a metric going in the right direction is more important than hitting a specific target

---

### Phase 1: The Metrics That Matter

#### 1.1 The Vanity Metrics Trap

First, let's name the problem. These metrics feel good but don't drive decisions:

| Vanity Metric | Why It's Misleading | What to Track Instead |
|--------------|--------------------|--------------------|
| **Total downloads** | Counts everyone who ever installed, including those who used it once and deleted it | Daily/Monthly Active Users (DAU/MAU) |
| **Total registered users** | Same problem — includes abandoned accounts | Active users in the last 7 or 30 days |
| **Page views** | More views could mean users are confused, not engaged | Feature adoption rate, task completion |
| **Social media followers** | Followers don't equal users or revenue | Conversion from social to install |
| **App store impressions** | Seeing your listing isn't success | Conversion rate (impressions → installs) |
| **Gross revenue** | Doesn't account for refunds, commissions, or costs | Net revenue (after Google's cut and refunds) |

**The rule:** If a metric makes you feel good but doesn't change what you do tomorrow, it's a vanity metric.

#### 1.2 The Core 7 Metrics

These are the 5-7 metrics that matter for a solo developer running a consumer Android app. Track these and nothing else until you've mastered them:

| # | Metric | What It Tells You | Why It Matters |
|---|--------|-------------------|---------------|
| 1 | **DAU / MAU** | How many people actively use your app daily and monthly | Core health indicator — are people coming back? |
| 2 | **D1 / D7 / D30 Retention** | What percentage of new users come back after 1, 7, and 30 days | The best predictor of long-term success |
| 3 | **MRR (Monthly Recurring Revenue)** | Predictable monthly revenue from subscriptions | Financial health and growth trajectory |
| 4 | **Crash-Free Rate** | Percentage of user sessions without a crash | Technical quality — crashes directly cause churn |
| 5 | **Store Rating** | Your average rating on Google Play | Affects discoverability AND user trust |
| 6 | **Trial-to-Paid Conversion** | Percentage of free trial users who convert to paid | Revenue engine efficiency |
| 7 | **Net Revenue** | Actual money deposited after Google's commission and refunds | The bottom line — what you actually earn |

**Why these 7?** Because they cover the three things that matter: **Are users staying?** (Retention, DAU/MAU), **Are users paying?** (MRR, Conversion, Net Revenue), **Is the product working?** (Crash-Free Rate, Store Rating).

#### 1.3 Metric Definitions in Detail

**1. DAU / MAU (Daily Active Users / Monthly Active Users)**

- **DAU:** Unique users who open your app on a given day
- **MAU:** Unique users who open your app at least once in a 30-day window
- **DAU/MAU ratio (Stickiness):** What percentage of monthly users come back daily. Higher is better.
  - A DAU/MAU of 20% means 1 in 5 monthly users uses the app every day
  - Social apps: 30-50% is strong
  - Utility/productivity apps: 15-30% is good
  - Casual games: 10-20% is typical

**2. D1 / D7 / D30 Retention**

- **D1 Retention:** Of users who installed today, what % opened the app again tomorrow?
- **D7 Retention:** Of users who installed today, what % opened the app within 7 days?
- **D30 Retention:** Of users who installed today, what % opened the app within 30 days?

| App Type | Good D1 | Good D7 | Good D30 |
|----------|---------|---------|----------|
| Social / Communication | 40-60% | 25-40% | 15-25% |
| Productivity / Utility | 30-50% | 20-35% | 10-20% |
| Health / Fitness | 25-40% | 15-25% | 8-15% |
| Casual Games | 25-40% | 10-20% | 5-10% |
| Education | 20-35% | 10-20% | 5-12% |

**These benchmarks are approximate.** Your specific category and audience will vary. Focus on the TREND (improving vs. declining) more than hitting a specific number.

**3. MRR (Monthly Recurring Revenue)**

```
MRR = (number of active subscribers) × (average subscription price per month)

Example:
- 200 monthly subscribers at $4.99 = $998/month
- 50 annual subscribers at $39.99 = 50 × ($39.99 / 12) = $166.63/month
- Total MRR: $1,164.63
```

For apps with in-app purchases instead of subscriptions, use **Monthly Revenue** (total revenue in a 30-day window) as the equivalent.

**4. Crash-Free Rate**

- Percentage of user sessions that complete without a crash
- Target: 99.5%+ (Google's recommendation for a healthy app)
- Below 99%: Users are experiencing crashes regularly — this is a fire to put out

**5. Store Rating**

- Your cumulative average star rating on Google Play
- Target: 4.0+ stars (below 4.0 significantly affects conversion from listing to install)
- Monitor the trend: improving ratings mean product improvements are landing

**6. Trial-to-Paid Conversion**

```
Conversion Rate = (Users who started paying) / (Users who started a free trial) × 100

Example:
- 500 users started a free trial this month
- 75 converted to paid
- Conversion rate: 75 / 500 = 15%
```

| Conversion Benchmark | Rating |
|---------------------|--------|
| 2-5% | Below average — paywall or value prop needs work |
| 5-10% | Average for most app categories |
| 10-20% | Good — your free trial effectively demonstrates value |
| 20-30% | Excellent — strong product-market fit |
| 30%+ | Outstanding — you may be under-pricing |

**7. Net Revenue**

```
Net Revenue = Gross Revenue - Google's Commission - Refunds

Google takes 15% of the first $1M in annual revenue.

Example:
- Gross revenue: $5,000
- Google's commission (15%): $750
- Refunds: $100
- Net revenue: $4,150
```

---

### Phase 2: Data Source Mapping

#### 2.1 Where to Find Each Metric

| Metric | Primary Data Source | How to Access | Cost |
|--------|-------------------|--------------|------|
| **DAU / MAU** | Firebase Analytics | Firebase Console → Analytics → Dashboard | Free |
| **D1/D7/D30 Retention** | Firebase Analytics | Firebase Console → Analytics → Retention | Free |
| **MRR** | RevenueCat Dashboard | RevenueCat → Overview | Free (up to $2.5K MRR) |
| **MRR (alternative)** | Google Play Console | Financial Reports → Revenue | Free |
| **Crash-Free Rate** | Firebase Crashlytics | Firebase Console → Crashlytics → Dashboard | Free |
| **Store Rating** | Google Play Console | Play Console → Ratings & Reviews | Free |
| **Trial-to-Paid Conversion** | RevenueCat Dashboard | RevenueCat → Charts → Conversion | Free |
| **Trial-to-Paid (alternative)** | Firebase Analytics | Custom events + funnel analysis | Free (requires setup) |
| **Net Revenue** | Google Play Console | Financial Reports → Estimated Revenue | Free |
| **Store Listing Conversion** | Google Play Console | Store Listing Performance → Conversion | Free |

#### 2.2 Tool Stack Recommendations

**Minimum viable analytics stack (free):**

| Tool | What It Provides | Setup Time |
|------|-----------------|-----------|
| **Google Play Console** | Downloads, revenue, ratings, store performance, device stats | Already have it |
| **Firebase Analytics** | DAU/MAU, retention, custom events, user properties | 30 minutes |
| **Firebase Crashlytics** | Crash-free rate, crash reports, stack traces | 30 minutes |

**Total cost: $0. Total setup time: 1 hour.**

This covers 5 of your 7 core metrics. For the remaining 2 (MRR breakdown and trial-to-paid conversion), you can either:

**Option A: Add RevenueCat (recommended if you have subscriptions):**

| Tool | What It Adds | Cost |
|------|-------------|------|
| **RevenueCat** | MRR, subscriber counts, conversion rates, churn, LTV | Free up to $2.5K MRR, then $0.01/API call |

**Option B: Calculate manually from Play Console data:**
- Download monthly financial reports
- Track subscriber counts in a spreadsheet
- Calculate conversion from trial starts vs. paid subscriptions

**Option A is worth it.** RevenueCat's free tier covers most solo developers, and the dashboard saves hours of manual calculation.

#### 2.3 Setting Up Firebase Analytics (Quick Guide)

If you haven't set up Firebase Analytics yet:

1. **Add Firebase to your project** (if not already): Firebase Console → Add Project → Follow Android setup
2. **Add the Analytics SDK** to your app's `build.gradle`:
   ```
   implementation 'com.google.firebase:firebase-analytics'
   ```
3. **Log key events** that map to your business:
   ```kotlin
   // User completes onboarding
   Firebase.analytics.logEvent("onboarding_complete") {}

   // User starts a trial
   Firebase.analytics.logEvent("trial_started") {}

   // User performs core action
   Firebase.analytics.logEvent("core_action_completed") {
       param("action_type", "export_pdf")
   }
   ```
4. **Wait 24 hours** for data to populate in the Firebase Console

**Essential custom events to log:**

| Event | When to Fire | Why Track It |
|-------|-------------|-------------|
| `onboarding_complete` | User finishes initial setup | Measures onboarding funnel completion |
| `trial_started` | User begins free trial | Denominator for conversion rate |
| `subscription_started` | User converts to paid | Numerator for conversion rate |
| `core_action` | User performs main value action | Measures engagement beyond just opening the app |
| `paywall_viewed` | User sees the paywall | Understanding conversion funnel |
| `paywall_dismissed` | User closes paywall without buying | Conversion friction point |

---

### Phase 3: Dashboard Setup

#### 3.1 The One-Page Dashboard

Your dashboard should fit on one screen and be readable in 60 seconds:

```markdown
## [App Name] Weekly Dashboard — Week of [Date]

### Health Indicators
| Metric | This Week | Last Week | Trend | Status |
|--------|----------|----------|-------|--------|
| DAU (avg) | ________ | ________ | [▲/▼/━] | [🟢/🟡/🔴] |
| MAU | ________ | ________ | [▲/▼/━] | [🟢/🟡/🔴] |
| D1 Retention | ________% | ________% | [▲/▼/━] | [🟢/🟡/🔴] |
| D7 Retention | ________% | ________% | [▲/▼/━] | [🟢/🟡/🔴] |
| Crash-Free Rate | ________% | ________% | [▲/▼/━] | [🟢/🟡/🔴] |
| Store Rating | ________ | ________ | [▲/▼/━] | [🟢/🟡/🔴] |

### Revenue
| Metric | This Month (MTD) | Last Month | Trend | Status |
|--------|-----------------|-----------|-------|--------|
| MRR | $________ | $________ | [▲/▼/━] | [🟢/🟡/🔴] |
| Net Revenue | $________ | $________ | [▲/▼/━] | [🟢/🟡/🔴] |
| Trial-to-Paid | ________% | ________% | [▲/▼/━] | [🟢/🟡/🔴] |
| Active Subscribers | ________ | ________ | [▲/▼/━] | [🟢/🟡/🔴] |

### Alerts
- [Any metric in red status — requires immediate attention]
- [Any significant change from last week]

### This Week's Action
- [One specific action based on the data above]
```

#### 3.2 Red / Yellow / Green Thresholds

Define thresholds BEFORE you need them. When a metric turns red, you don't want to debate whether it's "really that bad" — you want to act.

**Example thresholds (adjust for your app category and stage):**

| Metric | Green (Healthy) | Yellow (Watch) | Red (Act Now) |
|--------|----------------|---------------|--------------|
| **DAU** | Growing or stable | Declined 10-20% vs. last month | Declined 20%+ vs. last month |
| **MAU** | Growing or stable | Declined 5-15% vs. last month | Declined 15%+ vs. last month |
| **D1 Retention** | Above category benchmark | 5-10% below benchmark | 10%+ below benchmark or declining 3 weeks in a row |
| **D7 Retention** | Above 15% | 10-15% | Below 10% |
| **D30 Retention** | Above 8% | 5-8% | Below 5% |
| **Crash-Free Rate** | 99.5%+ | 99.0-99.5% | Below 99.0% |
| **Store Rating** | 4.0+ stars | 3.5-4.0 stars | Below 3.5 stars |
| **Trial-to-Paid** | Above 10% | 5-10% | Below 5% |
| **MRR Growth** | Month-over-month growth | Flat (0% growth) | Declining |
| **Net Revenue** | Covers business expenses | Below business expenses | Declining for 3+ months |

**Threshold calibration:** These thresholds should be adjusted after 3 months of data. If your D1 retention is consistently 35%, then 30% is yellow (a meaningful decline), not 25%.

#### 3.3 Dashboard Implementation Options

| Method | Complexity | Best For | Update Frequency |
|--------|-----------|----------|-----------------|
| **Google Sheets (manual)** | Low | Getting started, < 1K DAU | Weekly (manual entry from sources) |
| **Notion database** | Low | Visual thinkers, already using Notion | Weekly (manual entry) |
| **RevenueCat + Firebase dashboards** | Low-Medium | Subscription apps, no custom needs | Real-time (automatic) |
| **Google Data Studio (Looker Studio)** | Medium | Automated, visual dashboards | Daily (connect data sources) |
| **Custom dashboard (Retool, Metabase)** | High | Full customization, multiple sources | Real-time |

**Recommendation:** Start with a Google Sheet. Manually enter numbers every Monday morning. It takes 10 minutes and forces you to actually look at each number. Automate AFTER you've proven the habit (4+ consecutive weeks of reviews).

---

### Phase 4: Weekly Review Cadence

#### 4.1 The 15-Minute Monday Review

Do this every Monday morning before you start development:

```markdown
## Weekly Metrics Review — [Date]

### Step 1: Pull Numbers (5 minutes)
Open each data source and record this week's numbers:
- [ ] Firebase Analytics → DAU/MAU, Retention
- [ ] Firebase Crashlytics → Crash-free rate
- [ ] Google Play Console → Rating, downloads
- [ ] RevenueCat (or Play Console) → MRR, conversion, subscribers
- [ ] Enter all numbers into dashboard spreadsheet

### Step 2: Compare to Last Week (3 minutes)
For each metric:
- [ ] Is it up, down, or flat vs. last week?
- [ ] Update the trend arrows
- [ ] Flag any yellow or red status

### Step 3: Identify the One Thing (5 minutes)
- What is the most important signal in this week's data?
  Answer: ________________________________
- Does any metric require immediate action?
  Answer: ________________________________
- What is the ONE metric-driven action for this week?
  Answer: ________________________________

### Step 4: Log It (2 minutes)
- [ ] Save the dashboard
- [ ] Note any actions in your weekly plan
- [ ] Done. Start building.
```

**Critical rule:** The review must take 15 minutes or less. If you find yourself diving into analytics rabbit holes, stop. Note the question and schedule a separate time for deep analysis. The Monday review is for awareness, not investigation.

#### 4.2 Monthly Deep Dive (30 minutes, first Monday)

Once a month, go deeper:

```markdown
## Monthly Metrics Deep Dive — [Month Year]

### Trend Analysis (look at 4-week trend, not just this week)
| Metric | Week 1 | Week 2 | Week 3 | Week 4 | 30-Day Trend |
|--------|--------|--------|--------|--------|-------------|
| DAU | ______ | ______ | ______ | ______ | [Improving/Stable/Declining] |
| D1 Ret. | ______% | ______% | ______% | ______% | [Improving/Stable/Declining] |
| D7 Ret. | ______% | ______% | ______% | ______% | [Improving/Stable/Declining] |
| MRR | $______ | $______ | $______ | $______ | [Improving/Stable/Declining] |
| Crash-Free | ______% | ______% | ______% | ______% | [Improving/Stable/Declining] |
| Rating | ______ | ______ | ______ | ______ | [Improving/Stable/Declining] |
| Conversion | ______% | ______% | ______% | ______% | [Improving/Stable/Declining] |

### Release Impact
- Releases this month: [Version X.Y on Date, Version X.Z on Date]
- Impact on retention: [Improved / No change / Declined]
- Impact on crash rate: [Improved / No change / Worsened]
- Impact on rating: [Improved / No change / Declined]

### Revenue Analysis
- MRR at start of month: $________
- MRR at end of month: $________
- New subscriptions: ________
- Churned subscriptions: ________
- Net subscriber growth: ________
- Revenue trend: [Growing / Flat / Declining]

### Key Insight
What is the single most important thing the data is telling you this month?
Answer: ________________________________

### Action for Next Month
Based on the data, what ONE thing should change in your roadmap or focus?
Answer: ________________________________
```

#### 4.3 Quarterly Metrics Review (1 hour)

Every quarter, zoom out further:

```markdown
## Quarterly Metrics Summary — Q[N] [Year]

### Quarter-over-Quarter Comparison
| Metric | Last Quarter Avg | This Quarter Avg | Change |
|--------|-----------------|-----------------|--------|
| DAU | ________ | ________ | ________% |
| MAU | ________ | ________ | ________% |
| D1 Retention | ________% | ________% | [+/-]______pp |
| D30 Retention | ________% | ________% | [+/-]______pp |
| MRR | $________ | $________ | ________% |
| Crash-Free Rate | ________% | ________% | [+/-]______pp |
| Store Rating | ________ | ________ | [+/-]______ |
| Trial Conversion | ________% | ________% | [+/-]______pp |

### What Worked This Quarter
- [Feature or change that moved metrics positively]
- [Marketing action that drove growth]

### What Didn't Work
- [Feature that didn't impact metrics as expected]
- [Area where metrics declined]

### Goals for Next Quarter
Based on this data, next quarter's focus is:
1. [Metric to improve]: from ________% to ________%
2. [Metric to improve]: from $________ to $________
```

---

### Phase 5: Action Triggers

#### 5.1 When Metrics Go Red

The purpose of thresholds is to trigger action, not just to change a color on a spreadsheet. Here's what to do when each metric goes red:

| Red Metric | Immediate Action | Investigation |
|-----------|-----------------|--------------|
| **DAU dropping sharply** | Check for Play Store ranking changes, algorithm changes, or broken onboarding | Was there a recent update? Did a competitor launch? Is onboarding broken for new users? |
| **D1 Retention below benchmark** | Review onboarding flow. Is the first-time user experience working? | What's the last step users complete before leaving? Where is the drop-off? |
| **D7 Retention declining** | Check if the core value proposition is being delivered quickly enough | Are users reaching the "aha moment" within the first week? |
| **MRR declining** | Check churn rate immediately. Are more users canceling than subscribing? | Is there a specific plan or price point with higher churn? Did a competitor undercut? |
| **Crash-free rate below 99%** | This is a severity-1 bug fix situation. Drop everything and stabilize. | Open Crashlytics, sort by user impact, fix the top crashers |
| **Store rating below 3.5** | Respond to every negative review. Identify the common complaint. Fix it. | Is there a recent update that introduced a regression? Are users confused by a change? |
| **Trial conversion below 5%** | Evaluate your paywall. Is the value proposition clear? Is the price right? | Where in the trial do users drop off? Do they reach the premium features before the trial ends? |

#### 5.2 When Metrics Go Green (Celebrate and Learn)

Don't just track problems. When metrics improve, understand WHY so you can do more of it:

```markdown
## Win Analysis: [Metric] improved from [X] to [Y]

What changed recently?
- [ ] New feature shipped: [Which one?]
- [ ] Bug fixed: [Which one?]
- [ ] Marketing campaign: [Which one?]
- [ ] ASO change: [What was updated?]
- [ ] Nothing I can identify (organic improvement)

Can this be replicated or amplified?
- [How to do more of what worked]

Documented for future reference: [Y/N]
```

#### 5.3 Metrics-Driven Decision Matrix

Connect metrics directly to roadmap decisions:

| Metric Signal | Business Implication | Roadmap Action |
|--------------|---------------------|---------------|
| Low D1 retention | First-time experience isn't compelling | Prioritize onboarding improvements |
| Low D7 retention, OK D1 | Users try it but don't form a habit | Add engagement hooks, reminders, streaks |
| Low trial conversion | Users see value but won't pay | Test pricing, improve paywall, extend trial |
| High crash rate | Technical quality issue | Prioritize stability sprint |
| Declining MRR | Churn exceeding acquisition | Investigate churn reasons, improve retention features |
| Low store rating | User experience or expectation mismatch | Fix top complaints, respond to reviews |
| High DAU, low revenue | Users love it but aren't paying | Monetization optimization (paywall placement, pricing) |
| Low DAU, high conversion | Small but loyal paying base | Focus on user acquisition, marketing |

---

### Phase 6: Common Pitfalls

#### 6.1 Analytics Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| **Checking metrics daily** | Over-reacting to normal daily fluctuations | Check weekly. Daily noise is not signal. |
| **Tracking 30 metrics** | Information overload leads to analysis paralysis | Stick to 7 core metrics. Add others only when you've mastered these. |
| **Celebrating downloads** | Downloads without retention = vanity | Always pair download numbers with retention rates. |
| **Comparing to industry averages** | Your app is unique; averages don't account for your specific audience | Compare to YOUR last month, not to "what the average app does." |
| **Ignoring seasonality** | Panicking over a December dip that happens every year | Compare to the same period last year, not just last month. |
| **No baseline period** | Setting thresholds without data | Track for 4-8 weeks before setting red/yellow/green thresholds. |
| **Analysis without action** | Looking at dashboards but never changing behavior | Every review must end with ONE specific action. |
| **Building before measuring** | Shipping features without checking if they moved metrics | Check metrics 2-4 weeks after every release. |

#### 6.2 Statistical Significance Warning

With small numbers, metrics fluctuate wildly:

| Sample Size | Reliability | What to Do |
|-------------|------------|-----------|
| < 100 events/week | Very low — daily swings of 30%+ are normal | Track trend over 4+ weeks, don't react to weekly changes |
| 100-500 events/week | Low — significant weekly variation | Look at 2-week rolling averages |
| 500-2,000 events/week | Moderate — weekly numbers are somewhat reliable | Weekly review is meaningful |
| 2,000+ events/week | High — weekly numbers are statistically reliable | Weekly changes are worth investigating |

**Example:** If 20 users start a trial each week and 3 convert, your conversion rate is 15%. If next week 4 convert, it jumps to 20%. Did your paywall get better? Probably not — that's normal fluctuation with small numbers. Wait for 4+ weeks of data.

---

## Expected Output

```markdown
# Metrics Dashboard: [App Name]
## Setup Date: [Date]

### Core Metrics

| # | Metric | Data Source | Current Value | Green | Yellow | Red |
|---|--------|-----------|--------------|-------|--------|-----|
| 1 | DAU | Firebase Analytics | [N] | > [N] | [N]-[N] | < [N] |
| 2 | D1 Retention | Firebase Analytics | [N]% | > [N]% | [N]-[N]% | < [N]% |
| 3 | D7 Retention | Firebase Analytics | [N]% | > [N]% | [N]-[N]% | < [N]% |
| 4 | MRR | RevenueCat / Play Console | $[N] | Growing | Flat | Declining |
| 5 | Crash-Free Rate | Firebase Crashlytics | [N]% | > 99.5% | 99.0-99.5% | < 99.0% |
| 6 | Store Rating | Play Console | [N] stars | > 4.0 | 3.5-4.0 | < 3.5 |
| 7 | Trial-to-Paid | RevenueCat | [N]% | > [N]% | [N]-[N]% | < [N]% |

### Data Sources
| Source | URL | Login Required | Data Available |
|--------|-----|---------------|---------------|
| Firebase Console | console.firebase.google.com | Yes | DAU, MAU, retention, crashes |
| Play Console | play.google.com/console | Yes | Revenue, ratings, downloads |
| RevenueCat | app.revenuecat.com | Yes | MRR, conversion, churn |

### Review Schedule
| Cadence | When | Duration | Focus |
|---------|------|----------|-------|
| Weekly | Monday AM | 15 min | Pull numbers, check trends, set 1 action |
| Monthly | 1st Monday | 30 min | 4-week trends, release impact, revenue analysis |
| Quarterly | Last week of quarter | 1 hour | QoQ comparison, goal setting |

### Action Log
| Date | Metric Signal | Action Taken | Result (check in 30 days) |
|------|-------------|-------------|--------------------------|
| [Date] | [What you saw] | [What you did] | [Pending / Positive / Neutral / Negative] |
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on building a minimal, actionable metrics system for one person
- **ST-02** (Structured Sequential Instructions) — Phased approach from metric selection through review cadence
- **RT-02** (Multi-Dimensional Analysis) — Analyzing app health across retention, revenue, stability, and reputation dimensions
- **CM-01** (Explicit Context Framing) — Solo developer constraints: limited time for analytics, no data team, need for simplicity
- **CM-02** (Constraint Specification) — 15-minute weekly review cap, 7-metric maximum, free tool preference
- **DS-06** (Prioritization Guidance) — Metrics ranked by decision impact, thresholds that trigger specific actions

---

## Related Prompts

- `solo_dev_roadmap_planner.md` — Use metrics to prioritize features and validate roadmap decisions
- `solo_dev_financial_planning.md` — Revenue metrics feeding into financial planning and milestone tracking
- `solo_dev_weekly_operating_rhythm.md` — Embed the Monday metrics review into your weekly rhythm
- `solo_dev_decision_framework.md` — Data-driven feature decisions using dashboard insights
- `solo_dev_support_system.md` — Correlation between support volume and product metrics
- `monetization_paywall_optimization.md` — Deep dive when trial-to-paid conversion needs improvement

---

## Customization Guide

- **For pre-launch apps:** You don't have user data yet, so skip this guide until post-launch. During development, the only "metric" that matters is progress toward launch. After launch, start with just DAU and D1 retention for the first 2 weeks, then add the remaining metrics.
- **For apps with advertising revenue (not subscriptions):** Replace "MRR" with "Monthly Ad Revenue" and "Trial-to-Paid Conversion" with "eCPM" (effective cost per 1,000 impressions) or "ARPDAU" (average revenue per daily active user). The rest of the framework applies unchanged.
- **For apps with one-time purchases (not subscriptions):** Replace "MRR" with "Monthly Revenue" and "Trial-to-Paid Conversion" with "Install-to-Purchase Conversion." Track daily sales volume as a leading indicator.
- **For developers with fewer than 100 DAU:** Your numbers will be noisy. Focus on just 3 metrics: DAU trend (growing?), crash-free rate (stable?), and store rating (acceptable?). Add retention and revenue metrics when you have enough users for the numbers to be meaningful (typically 100+ DAU).
- **For developers who love data:** Resist the urge to add more metrics. Master these 7 first. Once you can articulate what each number means and what action each threshold triggers, THEN consider adding secondary metrics like LTV, CAC, or feature-specific adoption rates. Complexity is a luxury earned through discipline, not a starting point.
- **For developers who hate data:** Start with literally one metric: crash-free rate. Check it every Monday. Takes 60 seconds. Once that's a habit, add store rating. Then DAU. Build the habit before building the dashboard. A developer who checks one metric consistently beats a developer who built a beautiful 30-metric dashboard they never look at.
