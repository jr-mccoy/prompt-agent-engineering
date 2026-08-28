---
title: "Monetization Model Selector"
category: startup/monetization
description: "Evaluate monetization models for an Android app — freemium, subscription, one-time purchase, ads, hybrid — analyzing app type, audience, competition, and user behavior to recommend the optimal model"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-03
  - CM-01
  - QA-02
  - DS-06
difficulty: beginner
tags:
  - monetization
  - startup
  - revenue
  - pricing
  - android
  - solo-developer
  - business-model
updated: "2026-02-11"
---

# Monetization Model Selector

**Objective:** Evaluate monetization models for an Android app — freemium, subscription, one-time purchase, ads, and hybrid approaches — by analyzing app type, target audience, competitive landscape, and user behavior patterns to recommend the optimal model with projected revenue ranges and implementation complexity.

**When to Use:** Use this prompt before launching a new app when deciding how to generate revenue, when your current monetization isn't working and you want to pivot, or when planning a major app redesign that could change the business model. Critical because choosing the wrong monetization model is the #1 reason apps with good products fail financially — you can always change later, but switching costs are high (user expectations, code changes, store listing updates).

**Important context:** This prompt teaches monetization fundamentals while making a recommendation. If you have "no experience" with monetization, that's exactly who this is for. The goal is not to find the theoretically best model — it's to find the model that works for YOUR app, YOUR audience, and YOUR capacity as a solo developer to implement and maintain it.

---

## Context Gathering

Before evaluating monetization models, gather essential context:

1. **App Details:**
   - "What does your app do? What problem does it solve?"
   - "What category is it in (productivity, fitness, gaming, social, utility, etc.)?"
   - "How often do users open the app (daily, weekly, occasionally)?"
   - "How long has the app been live? How many active users?"

2. **Target Audience:**
   - "Who are your users (consumers, professionals, students, etc.)?"
   - "What is their willingness to pay? (Are they used to paying for similar tools?)"
   - "How price-sensitive is your audience?"
   - "What age range and geography are your primary users?"

3. **Competitive Landscape:**
   - "What are the top 3-5 competing apps?"
   - "How do they monetize (free, paid, subscription, ads)?"
   - "What do competitors charge? What do users say about their pricing?"
   - "Is there a dominant monetization model in your category?"

4. **Your Constraints:**
   - "How much development time can you invest in monetization features?"
   - "Are you comfortable with ads in your app?"
   - "Do you have ongoing costs that need to be covered (servers, APIs)?"
   - "What is your minimum viable revenue target per month?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending ANY monetization model, you MUST:**

1. **Research the app category norms** — Users in different categories have different expectations. Productivity app users expect subscriptions. Game users expect free-to-play with IAPs. Utility users expect one-time purchase or free with ads. Going against category norms requires strong justification.
2. **Assess the value proposition strength** — Subscription models only work if the app delivers ongoing value. If your app is a one-time-use tool, don't force a subscription.
3. **Consider implementation complexity** — Some models require significant backend work (subscription management, receipt validation, paywall logic). A solo developer should factor this in.
4. **Account for Google Play's 15-30% cut** — Google takes 15% on the first $1M annual revenue (30% above that). Factor this into all revenue projections.
5. **Check for regulatory requirements** — Some monetization models have specific legal requirements (subscription auto-renewal disclosures, children's app restrictions, gambling regulations).

### False-Positive Prevention

- ❌ Do NOT recommend subscriptions for apps that don't provide ongoing value — users will churn immediately
- ❌ Do NOT recommend ads for apps where the user experience is the product's core value (premium tools, meditation apps)
- ❌ Do NOT project revenue without accounting for Google's commission, refund rates, and churn
- ❌ Do NOT recommend the most profitable model if it requires engineering effort the solo developer can't sustain
- ❌ Do NOT assume "freemium" means "free with a paywall" — it's a spectrum of approaches
- ✅ DO recommend the simplest model that meets revenue needs
- ✅ DO consider the implementation and maintenance cost of each model
- ✅ DO research what competitors charge and what users say about their pricing
- ✅ DO factor in the solo developer's capacity to maintain the monetization system
- ✅ DO provide realistic revenue projections with ranges, not point estimates

---

### Phase 1: Monetization Model Overview

#### 1.1 Model Comparison

| Model | Best For | Revenue Pattern | Implementation Effort | User Friction |
|-------|---------|----------------|----------------------|---------------|
| **Free + Ads** | High-volume, casual use apps | Steady, scales with users | Low (SDK integration) | Low entry, medium ongoing |
| **Freemium** | Apps with clear free/premium divide | Grows with conversion rate | Medium (paywall + feature gating) | Low entry, medium upgrade |
| **Subscription** | Apps providing ongoing value | Predictable recurring revenue | High (billing lifecycle) | High (commitment required) |
| **One-Time Purchase** | Complete tools, utility apps | Spike on launch, declines | Low (simple purchase) | Medium (upfront commitment) |
| **Paid App** | Niche professional tools | Spike on launch, declines | Lowest (just set price) | Highest (pay before try) |
| **Hybrid (Freemium + Ads)** | Mass market apps | Mixed streams | Medium-High | Variable |

#### 1.2 Model Deep Dives

**Free + Ads:**
```markdown
How it works: App is free, revenue comes from ad impressions/clicks
Revenue formula: DAU × sessions/day × ads/session × eCPM / 1000

Pros:
- No barrier to download (maximum user acquisition)
- Revenue scales linearly with users
- Simple to implement (AdMob SDK)
- No billing code to maintain

Cons:
- Needs very high DAU to be meaningful (10K+ DAU for $100+/month)
- Ads degrade user experience
- Revenue dependent on ad market conditions
- Users increasingly use ad blockers
- eCPM varies wildly by country and category ($0.50 - $15)

Best when:
- App is used daily by a large audience
- User experience can absorb ads without degradation
- Category norm is free (weather, news, casual games)

Typical revenue:
- 1K DAU: $15-50/month
- 10K DAU: $150-500/month
- 100K DAU: $1,500-5,000/month
(Assumes mixed ad formats, US-heavy audience)
```

**Freemium:**
```markdown
How it works: Core app is free, premium features behind a paywall
Revenue formula: Users × conversion rate × price − Google's cut

Pros:
- Low barrier to entry (free download)
- Users experience value before paying
- Can optimize conversion over time
- Higher revenue per user than ads

Cons:
- Must clearly divide free and premium features
- Risk of giving away too much (low conversion) or too little (bad reviews)
- Requires paywall UX design and A/B testing
- Typical conversion rate: 2-5% (most users never pay)

Best when:
- Clear premium features that power users need
- App has both casual and power user segments
- Competitive landscape includes both free and paid options

Typical revenue:
- 1K MAU, 3% conversion, $5/month: $127/month (after Google's cut)
- 10K MAU, 3% conversion, $5/month: $1,275/month
- 10K MAU, 5% conversion, $10/month: $4,250/month
```

**Subscription:**
```markdown
How it works: Users pay recurring fee for ongoing access/features
Revenue formula: Subscribers × price × (1 − churn rate) − Google's cut

Pros:
- Predictable, recurring revenue (MRR)
- Highest lifetime value per user
- Google takes only 15% after first year (reduced commission)
- Aligns incentives: you keep improving, users keep paying

Cons:
- Highest user commitment = highest friction
- Must deliver ongoing value (not just unlock features)
- Complex billing lifecycle (trials, grace period, account hold, downgrades)
- Monthly churn of 5-15% is typical — constant acquisition needed
- Google Play Billing Library integration is complex

Best when:
- App provides continuous, evolving value
- Content or data is regularly updated
- Users have ongoing needs (fitness tracking, project management)
- Category norm is subscription (Spotify, Netflix model)

Typical revenue:
- 500 subscribers at $5/month: $2,125/month (after 15% cut)
- 1K subscribers at $10/month: $8,500/month
- Annual subscriptions improve LTV by 20-40% vs monthly
```

**One-Time Purchase (In-App or Paid App):**
```markdown
How it works: User pays once for full access
Revenue formula: Downloads × price × conversion rate − Google's cut

Pros:
- Simple for users to understand
- No billing lifecycle complexity
- Users feel they "own" the product
- No churn management needed

Cons:
- Revenue declines after launch spike (no recurring income)
- Must constantly acquire new users for revenue
- Users expect free updates forever after purchase
- Difficult to fund ongoing development long-term

Best when:
- App is a complete tool (calculator, file converter, reference)
- Users don't need ongoing updates or content
- Low ongoing server/infrastructure costs
- Niche professional tool with clear value

Typical revenue:
- 100 purchases/month at $5: $425/month (after cut)
- Decreases over time unless marketing sustains acquisition
```

---

### Phase 2: Evaluation Framework

#### 2.1 Scoring Matrix

Rate your app on each dimension (1-5 scale):

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| **Usage frequency** (daily=5, monthly=1) | [1-5] | 3x | [Score] |
| **Ongoing value delivery** (continuous=5, one-time=1) | [1-5] | 3x | [Score] |
| **Audience willingness to pay** (high=5, low=1) | [1-5] | 2x | [Score] |
| **Competitive pricing norm** (subscription=5, free=1) | [1-5] | 2x | [Score] |
| **Content/feature depth** (deep=5, shallow=1) | [1-5] | 1x | [Score] |
| **User volume potential** (mass market=5, niche=1) | [1-5] | 1x | [Score] |
| **Your dev capacity for billing code** (high=5, low=1) | [1-5] | 2x | [Score] |

**Scoring interpretation:**

| Total Weighted Score | Recommended Model |
|---------------------|-------------------|
| 50+ | Subscription |
| 35-49 | Freemium |
| 25-34 | One-time purchase or freemium |
| 15-24 | Free + ads or one-time purchase |
| < 15 | Free + ads (focus on growth first) |

#### 2.2 Category-Specific Guidance

| App Category | Dominant Model | Why |
|-------------|---------------|-----|
| Productivity/Tools | Freemium or Subscription | Users pay for professional-grade features |
| Fitness/Health | Subscription | Ongoing coaching, tracking, content |
| Social/Communication | Free + Ads | Network effects need maximum users |
| Games (Casual) | Free + Ads + IAPs | Volume-based, impulse purchases |
| Games (Premium) | One-time or Subscription | Dedicated gamers willing to pay |
| Photo/Video | Freemium | Free basic editing, premium filters/features |
| Music/Audio | Subscription | Ongoing content delivery |
| Education | Freemium or Subscription | Course access, progress tracking |
| Finance/Budgeting | Freemium | Free tracking, premium analysis |
| Utility | One-time or Free + Ads | Simple, complete tools |
| News/Content | Subscription or Ads | Ongoing content delivery |
| Weather | Free + Ads | High volume, frequent use |

---

### Phase 3: Revenue Projection

#### 3.1 Build Your Revenue Model

```markdown
## Revenue Projection: [Model Name]

### Assumptions
- Monthly active users (MAU): [N]
- Monthly growth rate: [X]%
- Conversion rate (free to paid): [X]%
- Price point: $[X]/month or $[X] one-time
- Monthly churn (subscribers): [X]%
- Google's commission: 15% (first $1M/year) or 30%
- Refund rate: ~2-5%

### Month-by-Month Projection

| Month | MAU | New Subscribers | Churned | Active Subscribers | Gross Revenue | Net Revenue |
|-------|-----|----------------|---------|-------------------|---------------|-------------|
| 1 | [N] | [N] | 0 | [N] | $[X] | $[X] |
| 3 | [N] | [N] | [N] | [N] | $[X] | $[X] |
| 6 | [N] | [N] | [N] | [N] | $[X] | $[X] |
| 12 | [N] | [N] | [N] | [N] | $[X] | $[X] |

### Break-Even Analysis
- Monthly costs: $[X] (Firebase, tools, services)
- Break-even subscribers/purchases: [N]
- Time to break-even: [estimate]
```

#### 3.2 Sensitivity Analysis

Test your model with optimistic and pessimistic assumptions:

| Scenario | Conversion Rate | Churn | Monthly Revenue (Month 12) |
|----------|----------------|-------|----------------------------|
| Pessimistic | 1% | 15% | $[X] |
| Expected | 3% | 10% | $[X] |
| Optimistic | 5% | 5% | $[X] |

---

### Phase 4: Implementation Roadmap

#### 4.1 Minimum Viable Monetization

Don't build the perfect monetization system on day one. Start with the simplest version:

**For Freemium/Subscription:**
1. **Week 1:** Define free vs. premium features (just 1-2 premium features to start)
2. **Week 2:** Implement Google Play Billing Library (one subscription tier)
3. **Week 3:** Build a simple paywall screen (clear value proposition, one price)
4. **Week 4:** Test purchase flow end-to-end, handle edge cases

**For Ads:**
1. **Day 1:** Integrate AdMob SDK
2. **Day 2:** Add banner ad on one screen (non-intrusive placement)
3. **Week 2:** Add interstitial at natural break points (between tasks, not mid-action)
4. **Week 3:** Add rewarded ads if applicable (optional premium content)

**For One-Time Purchase:**
1. **Week 1:** Define what the purchase unlocks
2. **Week 2:** Implement Google Play Billing Library (one-time product)
3. **Week 3:** Build unlock flow and purchase restoration

#### 4.2 What to Defer

Don't build these until you have data showing you need them:

| Feature | When to Add |
|---------|------------|
| Multiple subscription tiers | After 100+ subscribers and feedback requesting it |
| Annual pricing | After monthly pricing is validated |
| Family/team plans | After individual pricing is working |
| Promotional pricing | After you understand your baseline conversion |
| A/B testing paywalls | After you have enough traffic for statistical significance |
| Cross-platform billing | After one platform is profitable |

---

## Expected Output

### Monetization Recommendation Report

```markdown
# Monetization Analysis: [App Name]

## Recommendation: [Model Name]

### Why This Model
- [Reason 1 based on analysis]
- [Reason 2 based on analysis]
- [Reason 3 based on analysis]

### Models Considered

| Model | Fit Score | Pros for Your App | Cons for Your App |
|-------|-----------|-------------------|-------------------|
| [Model 1] | [Score] | [Specific pros] | [Specific cons] |
| [Model 2] | [Score] | [Specific pros] | [Specific cons] |
| [Model 3] | [Score] | [Specific pros] | [Specific cons] |

### Recommended Pricing
- Price point: $[X]
- Rationale: [Why this price]
- Competitor comparison: [How it compares]

### Revenue Projection (12 months)
| Month | Revenue (pessimistic) | Revenue (expected) | Revenue (optimistic) |
|-------|----------------------|--------------------|--------------------|
| 3 | $[X] | $[X] | $[X] |
| 6 | $[X] | $[X] | $[X] |
| 12 | $[X] | $[X] | $[X] |

### Implementation Plan
1. [Step 1 with timeline]
2. [Step 2 with timeline]
3. [Step 3 with timeline]

### Key Metrics to Track
- [Metric 1]: [Target]
- [Metric 2]: [Target]
- [Metric 3]: [Target]

### When to Reconsider
Revisit this decision if:
- [Condition 1]
- [Condition 2]
- [Condition 3]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Monetization selection focus
- **ST-02** (Structured Sequential Instructions) - Evaluation process
- **RT-02** (Multi-Dimensional Analysis) - Multiple monetization dimensions
- **RT-03** (Tree of Thoughts) - Multiple model options evaluated
- **CM-01** (Explicit Context Framing) - App and audience context
- **QA-02** (Adversarial Stress-Test) - Sensitivity analysis and pessimistic scenarios
- **DS-06** (Prioritization Guidance) - Model scoring and ranking

---

## Related Prompts

- `firebase_analytics_strategy.md` - Track monetization events and funnels
- `marketing_zero_budget_launch_plan.md` - User acquisition to feed the monetization funnel
- `domain-productivity/reviews/reviews_solo_dev_weekly_operating_rhythm.md` - Time allocation for monetization work
- `play_store_policy_compliance_check.md` - Billing policy compliance
- `solo_dev_financial_planning.md` - Financial planning with revenue projections (planned)

---

## Customization Guide

- **For games:** Expand the IAP section with virtual currency design, gacha/loot box considerations (legal in your markets?), and battle pass models
- **For B2B/professional apps:** Consider per-seat pricing, enterprise tiers, and annual-only billing to reduce churn
- **For apps with existing free users:** Add a section on migration strategy — how to introduce monetization without alienating your current user base
- **For children's apps:** Note COPPA restrictions on monetization, certified ad SDK requirements, and in-app purchase parental gate requirements
- **For apps in emerging markets:** Adjust pricing expectations significantly — $1/month can be premium pricing. Consider regional pricing on Google Play.
