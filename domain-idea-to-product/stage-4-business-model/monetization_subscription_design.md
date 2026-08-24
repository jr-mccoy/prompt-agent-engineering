---
title: "Subscription Offering Design"
category: startup/monetization
description: "Design a subscription offering for an Android app — tier structure, feature gating, pricing psychology, trial optimization, and Google Play billing lifecycle management for solo developers"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
difficulty: intermediate
tags:
  - monetization
  - android
  - subscription
  - pricing
  - tier-design
  - feature-gating
  - solo-developer
updated: "2026-02-11"
---

# Subscription Offering Design

**Objective:** Design a complete subscription offering for an Android app — including tier structure (free/basic/premium), feature gating strategy, pricing psychology, trial length optimization, and billing lifecycle management — that maximizes conversion while remaining implementable and maintainable by a solo developer.

**When to Use:** Use this after you've decided that a subscription model is the right fit for your app (see `monetization_model_selector.md`). This prompt takes you from "I know I want subscriptions" to "here is my exact tier structure, pricing, feature gates, and trial strategy." Use it before writing any billing code — getting the subscription design wrong is expensive to fix because users develop expectations about what's free and what's paid.

---

## Context Gathering

Before designing your subscription offering, gather essential context:

1. **App Value Proposition:**
   - "What ongoing value does your app provide that justifies recurring payment?"
   - "What features or content are updated regularly?"
   - "What would users lose if they stopped paying (data, access, capabilities)?"
   - "How does your app's value compound over time (history, personalization, data)?"

2. **Current User Behavior:**
   - "Which features do users engage with most? Which are rarely used?"
   - "What's your current DAU/MAU ratio (stickiness)?"
   - "Do users have distinct segments (casual vs. power users)?"
   - "What do users request most in reviews or feedback?"

3. **Competitive Landscape:**
   - "What subscription tiers do your top 3 competitors offer?"
   - "What are their price points (monthly and annual)?"
   - "What do competitor users complain about in reviews regarding pricing?"
   - "Are there free alternatives that cover the basics?"

4. **Your Constraints:**
   - "How many subscription tiers can you realistically maintain?"
   - "Do you have server-side costs that scale with usage (API calls, storage)?"
   - "Can you commit to regular content/feature updates to justify ongoing payment?"
   - "What's your timeline for implementing subscriptions?"

5. **Revenue Goals:**
   - "What's your monthly revenue target?"
   - "What subscriber count would be sustainable for you?"
   - "Are you optimizing for user count or revenue per user?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before designing ANY subscription offering, you MUST:**

1. **Verify ongoing value** — A subscription must deliver continuous value. If your app is a one-time utility (flashlight, QR scanner, unit converter), a subscription will generate negative reviews and high churn. The app must provide something that renews: content, data, cloud sync, ongoing analysis, or evolving features.
2. **Verify the free tier is genuinely useful** — The free tier must solve a real problem on its own. If the free tier is too limited, users leave bad reviews ("pay to use the app"). If it's too generous, nobody upgrades. The free tier is your acquisition channel.
3. **Verify feature boundaries are natural** — Feature gates should feel logical, not arbitrary. "Export to PDF requires Premium" makes sense. "View more than 5 items requires Premium" feels punitive. Gates should align with the user's mental model of "basic" vs. "advanced."
4. **Verify pricing is competitive** — Check at least 3 competitors' subscription prices. Being 2x more expensive than the market leader requires a strong justification. Being 50% cheaper may signal low quality.
5. **Verify implementation feasibility** — A solo developer maintaining 4+ subscription tiers with complex feature gating and proration logic is a maintenance nightmare. Start with 2 tiers (Free + Premium) and add a middle tier only when data shows demand.
6. **Acceptable null result** — It is valid to conclude that a subscription model is premature for the current app state. If the app lacks sufficient ongoing value or the user base is too small to validate pricing, recommend building more value first and revisiting subscription design later.

### False-Positive Prevention

- ❌ Do NOT create more than 3 tiers initially — complexity kills solo developers. Netflix has thousands of engineers managing their tiers; you don't.
- ❌ Do NOT gate basic functionality behind a subscription — this is the fastest way to get 1-star reviews on Google Play
- ❌ Do NOT copy a competitor's tier structure without understanding why it works for them — their context is different
- ❌ Do NOT set pricing based on what you think it's "worth" — price based on what users will pay relative to alternatives
- ❌ Do NOT offer only monthly pricing — you'll leave 20-40% of potential revenue on the table
- ❌ Do NOT skip the free trial — conversion rates drop 40-60% without a trial in most app categories
- ✅ DO start with 2 tiers (Free + Premium) and validate before adding a middle tier
- ✅ DO make the upgrade path feel like a natural progression, not a punishment
- ✅ DO use annual pricing as the primary option with monthly as the fallback
- ✅ DO plan for the full billing lifecycle (trials, grace periods, account hold, cancellation)
- ✅ DO test your subscription with real users before assuming your tier design is correct

---

### Phase 1: Tier Architecture Design

#### 1.1 The Two-Tier Starting Point

Most solo developers should start here. Add a third tier only when you have data.

```
┌─────────────────────────────────────────────────┐
│                  PREMIUM TIER                    │
│         "Everything, no limits"                  │
│                                                  │
│   All Free features PLUS:                        │
│   ✦ Advanced Feature A                           │
│   ✦ Advanced Feature B                           │
│   ✦ Unlimited [resource]                         │
│   ✦ Priority support / early access              │
│   ✦ No ads (if applicable)                       │
├─────────────────────────────────────────────────┤
│                   FREE TIER                      │
│         "Genuinely useful on its own"            │
│                                                  │
│   ✦ Core feature set                             │
│   ✦ Limited [resource] (enough to be useful)     │
│   ✦ Basic analytics/insights                     │
│   ✦ Standard export options                      │
│   ✦ Ads (if using hybrid model)                  │
└─────────────────────────────────────────────────┘
```

#### 1.2 Three-Tier Design (When You Have Data)

Add a middle tier when you observe: (a) users who want more than Free but find Premium too expensive, or (b) a clear feature cluster that deserves its own price point.

| Aspect | Free | Basic | Premium |
|--------|------|-------|---------|
| **Purpose** | Acquisition & retention | Convert price-sensitive users | Maximize revenue per user |
| **Price** | $0 | $2.99-4.99/month | $7.99-14.99/month |
| **Core features** | Full | Full | Full |
| **Advanced features** | None | Subset (2-3 key features) | All |
| **Usage limits** | Conservative | Moderate (3-5x free) | Unlimited or very high |
| **Support** | Community/none | Email | Priority email |
| **Ads** | Yes (if applicable) | No | No |
| **Export/sharing** | Basic | Standard | Advanced |
| **Cloud sync** | None or limited | Yes | Yes + backup |

#### 1.3 Feature Gating Framework

Not all features should be gated equally. Use this framework to decide:

**Gate Tier: ALWAYS FREE (Never Gate These)**
- Core value proposition (the reason users downloaded the app)
- Basic data viewing and entry
- Essential settings and preferences
- Onboarding and tutorials
- Basic sharing functionality

**Gate Tier: PREMIUM CANDIDATES (Consider Gating These)**
- Advanced analytics and insights
- Export to professional formats (PDF, CSV)
- Cloud sync and backup
- Unlimited usage (storage, entries, projects)
- Customization (themes, layouts, widgets)
- Ad removal
- Priority processing (faster sync, higher quality)
- Advanced integrations (calendar, other apps)
- Historical data and trends

**Gate Tier: NEVER GATE (Bad User Experience)**
- Features the user has already been using for free (don't take away)
- Security features (encryption, backup)
- Accessibility features (screen reader support, font size)
- Bug fixes and stability improvements
- Data the user created (never hold data hostage)

#### 1.4 The Feature Gate Decision Matrix

For each potential premium feature, score it:

| Feature | User Demand (1-5) | Implementation Cost (1-5) | Revenue Potential (1-5) | Free Alternative Exists? | Gate Decision |
|---------|-------------------|--------------------------|------------------------|-------------------------|---------------|
| [Feature A] | [Score] | [Score] | [Score] | Yes/No | Free / Basic / Premium |
| [Feature B] | [Score] | [Score] | [Score] | Yes/No | Free / Basic / Premium |

**Decision rules:**
- High demand + High revenue + Low cost = Premium (this funds your development)
- High demand + Low revenue = Free (this drives acquisition)
- Low demand + High cost = Skip (don't build it yet)
- Any feature with a free alternative from competitors = Free (or users leave)

---

### Phase 2: Pricing Psychology and Strategy

#### 2.1 Price Point Selection

**The Android app subscription pricing landscape (2024-2026):**

| Category | Low End | Sweet Spot | High End | Notes |
|----------|---------|------------|----------|-------|
| Productivity | $1.99/mo | $4.99-6.99/mo | $12.99/mo | Higher for B2B crossover |
| Fitness/Health | $4.99/mo | $9.99-12.99/mo | $19.99/mo | Users conditioned by Peloton, etc. |
| Education | $2.99/mo | $6.99-9.99/mo | $14.99/mo | Sensitive to student budgets |
| Photo/Video editing | $2.99/mo | $5.99-8.99/mo | $14.99/mo | Competes with VSCO, Lightroom |
| Music/Audio | $1.99/mo | $4.99-7.99/mo | $12.99/mo | Spotify sets expectations |
| Finance/Budgeting | $2.99/mo | $4.99-7.99/mo | $12.99/mo | YNAB at $14.99 is the ceiling |
| Utility/Tools | $0.99/mo | $2.99-4.99/mo | $7.99/mo | Hard to justify high prices |
| Games | $1.99/mo | $4.99-9.99/mo | $14.99/mo | Battle pass model dominates |

#### 2.2 Pricing Psychology Principles

**Charm Pricing (.99):**
- $4.99 is perceived as significantly cheaper than $5.00
- Always use .99 endings for consumer apps
- Exception: B2B/professional tools can use round numbers ($10/month) to signal seriousness

**Price Anchoring:**
- Show the most expensive tier first (on the left or top) so the middle tier feels like a deal
- Display the per-month cost of annual plans prominently: "$3.33/month" feels cheaper than "$39.99/year"
- Show the savings percentage: "Save 44%" next to the annual plan

**The Decoy Effect (When Using 3 Tiers):**
```
┌──────────┬──────────┬──────────┐
│  Basic   │   Pro    │ Premium  │
│ $2.99/mo │ $6.99/mo │ $7.99/mo │ ← Pro exists to make Premium look like a deal
│ 5 items  │ 50 items │ Unlimited│
│ No sync  │ Sync     │ Sync+    │
│          │ No export│ Export   │
└──────────┴──────────┴──────────┘
```
The "Pro" tier at $6.99 makes "Premium" at $7.99 look like an obvious choice. Pro is the decoy.

**Loss Aversion (Trial Strategy):**
- Give users the full premium experience during trial
- When trial ends, they feel the loss of features they've been using
- "Keep your [specific feature they used]" is more compelling than "Upgrade to get [feature]"

#### 2.3 Monthly vs. Annual Pricing

**Optimal annual discount: 30-45% off monthly**

| Monthly Price | Annual Price | Per-Month Equivalent | Savings | Annual Discount % |
|--------------|-------------|---------------------|---------|-------------------|
| $2.99/mo | $19.99/yr | $1.67/mo | $15.89 | 44% |
| $4.99/mo | $29.99/yr | $2.50/mo | $29.89 | 50% |
| $6.99/mo | $47.99/yr | $4.00/mo | $35.89 | 43% |
| $9.99/mo | $59.99/yr | $5.00/mo | $59.89 | 50% |
| $12.99/mo | $79.99/yr | $6.67/mo | $75.89 | 49% |

**Why annual matters:**
- Annual subscribers have 80-90% lower churn than monthly (they forget they're paying, and the upfront commitment creates inertia)
- Google Play reduces commission to 15% for subscriptions after the first year — annual subscribers reach this faster
- Annual provides upfront cash to fund development
- Aim for 40-60% of subscribers choosing annual

**How to push annual:**
- Default the annual plan as pre-selected on the paywall
- Show the monthly price struck through: ~~$6.99/mo~~ → $4.00/mo (billed annually)
- Add a "Most Popular" or "Best Value" badge to the annual plan
- Show total annual savings in dollars: "Save $35.89 per year"

#### 2.4 Family and Team Plans (Defer Until Later)

**When to consider family/team plans:**
- After reaching 500+ individual subscribers
- When users explicitly request sharing
- When your app has multi-user value (shared lists, family budgets)

**If you do add them:**
- Family plan: 1.5-2x the individual price for up to 5-6 members
- Team plan: Per-seat pricing with a minimum (3-5 seats)
- Google Play's family sharing has specific requirements — research before implementing

---

### Phase 3: Trial Strategy Optimization

#### 3.1 Trial Length Decision

| Trial Length | Conversion Rate (Typical) | Best For | Watch Out For |
|-------------|--------------------------|----------|--------------|
| 3 days | 8-15% | Simple apps with immediate value | Too short for complex apps |
| 7 days | 10-18% | Most app categories, sweet spot | Standard, won't differentiate you |
| 14 days | 8-14% | Apps that need habit formation | Users forget about the trial |
| 30 days | 5-10% | Enterprise/professional tools | High risk of payment shock |
| No trial | 3-6% | Established brands only | Significant conversion penalty |

**Recommended: 7 days for most apps.** Long enough to experience value, short enough to create urgency.

#### 3.2 Trial Design Best Practices

**During the trial:**
- Give full premium access (don't hold back features — you want users to feel the loss)
- Send push notifications highlighting premium features they've used: "You analyzed 12 workouts this week with Premium insights"
- Show a subtle, non-intrusive countdown: "4 days left in your free trial"
- Track which premium features the trial user engages with

**Trial expiration messaging sequence:**
```
Day 5 (2 days before): "Your Premium trial ends in 2 days.
    You've used [feature X] 8 times this week."

Day 7 (expiration day): "Your trial ends today. Keep [specific
    feature they used most]? Subscribe now."

Day 8 (1 day after): "We've moved you to the Free plan.
    Missing [feature]? Get it back anytime."

Day 14 (1 week after): "Still thinking about Premium?
    Here's what you're missing: [personalized list]"
```

**Never do:**
- Don't require payment info upfront for a trial (Google Play handles this, but don't add extra friction)
- Don't nag users daily during the trial — it feels desperate
- Don't end the trial in the middle of active use (time it to natural break points if possible)

#### 3.3 Introductory Pricing

Google Play supports introductory pricing for new subscribers:

| Intro Type | How It Works | Conversion Impact | Revenue Impact |
|-----------|-------------|-------------------|----------------|
| Free trial | Full access for N days, then full price | Highest conversion | Delayed revenue |
| Intro price | Reduced price for first N periods | High conversion | Reduced early revenue |
| Free trial + intro | Trial, then discounted first period | Highest conversion + retention | Most delayed revenue |

**Recommended approach for solo developers:**
1. Start with a 7-day free trial + full price after
2. If conversion is below 8%, add an introductory price (50% off first month)
3. If conversion is still low, the problem is likely your value proposition, not your pricing

---

### Phase 4: Google Play Billing Lifecycle

#### 4.1 Subscription States

Understanding the full subscription lifecycle is critical. Users will encounter every one of these states:

```
┌─────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ No Sub  │───→│  Trial   │───→│  Active  │───→│ Renewed  │──→ ...
└─────────┘    └──────────┘    └──────────┘    └──────────┘
                    │               │               │
                    │               ▼               ▼
                    │         ┌──────────┐    ┌──────────┐
                    │         │  Paused  │    │  Grace   │
                    │         │ (user)   │    │  Period  │
                    │         └──────────┘    └──────────┘
                    │               │               │
                    ▼               ▼               ▼
              ┌──────────┐   ┌──────────┐    ┌──────────┐
              │ Expired  │   │ Resumed  │    │ Account  │
              │ (no pay) │   │          │    │  Hold    │
              └──────────┘   └──────────┘    └──────────┘
                                                   │
                                                   ▼
                                             ┌──────────┐
                                             │ Expired  │
                                             │(payment  │
                                             │ failed)  │
                                             └──────────┘
```

#### 4.2 Key Lifecycle Events to Handle

| Event | What Happens | Your App Should |
|-------|-------------|-----------------|
| **New subscription** | User subscribes | Grant premium access immediately |
| **Renewal** | Automatic charge succeeds | Continue premium access (log for analytics) |
| **Grace period** (3-7 days) | Payment failed, Google retrying | Keep premium access, show subtle "update payment" prompt |
| **Account hold** (up to 30 days) | Payment failed repeatedly | Revoke premium access, show "resubscribe" prompt |
| **Pause** (user-initiated, 1-12 weeks) | User pauses subscription | Revoke premium access, don't lose their data |
| **Resume** | User resumes from pause | Restore premium access |
| **Cancellation** | User cancels | Keep premium until period ends, then revoke |
| **Expiration** | Subscription period ends after cancellation | Revoke premium, show "resubscribe" option |
| **Upgrade/downgrade** | User changes tier | Apply proration, update access level |
| **Refund** | Google issues refund | Revoke premium access |

#### 4.3 Grace Period and Account Hold Configuration

**Recommended settings in Google Play Console:**

| Setting | Recommended Value | Why |
|---------|------------------|-----|
| Grace period | 7 days | Gives users time to fix payment issues |
| Account hold | 30 days | Maximizes recovery of failed payments |
| Resubscribe | Enabled | Let expired subscribers come back easily |
| Pause | Enabled (1-12 weeks) | Better than cancellation — they come back |

**Revenue recovery from grace period + account hold: 15-25% of otherwise-churned subscribers.** This is free money — always enable it.

---

### Phase 5: Tier Comparison Matrix Template

#### 5.1 User-Facing Comparison

Design this for your paywall and Play Store listing:

```markdown
## Subscription Plans

|                           | Free          | Premium                |
|---------------------------|---------------|------------------------|
| **Price**                 | $0            | $X.99/mo or $XX.99/yr  |
| **[Core Feature 1]**     | ✅            | ✅                     |
| **[Core Feature 2]**     | ✅            | ✅                     |
| **[Core Feature 3]**     | ✅ (limited)  | ✅ (unlimited)         |
| **[Premium Feature 1]**  | ❌            | ✅                     |
| **[Premium Feature 2]**  | ❌            | ✅                     |
| **[Premium Feature 3]**  | ❌            | ✅                     |
| **Ads**                   | Yes           | No                     |
| **Cloud sync**            | ❌            | ✅                     |
| **Export**                | Basic         | All formats            |
| **Support**               | Community     | Email                  |
|                           | [Current]     | [Start Free Trial]     |
```

#### 5.2 Internal Decision Matrix

Keep this for your own reference when deciding what goes in each tier:

| Feature | Usage % (Free Users) | Requested in Reviews? | Cost to Serve | Revenue Gate? | Tier Placement |
|---------|---------------------|----------------------|---------------|---------------|----------------|
| [Feature] | [X]% | Yes/No | Low/Med/High | Yes/No | Free/Premium |

---

## Expected Output

```markdown
# Subscription Design: [App Name]

## Tier Structure

### Tier Overview
| | Free | Premium |
|---|---|---|
| Price | $0 | $[X]/mo or $[X]/yr |
| [Features...] | ... | ... |

### Feature Gating Rationale
- [Feature A] is Premium because: [reason]
- [Feature B] is Free because: [reason]
- [Feature C] is gated at [limit] because: [reason]

## Pricing

### Price Points
- Monthly: $[X].99/month
- Annual: $[X].99/year ($[X]/month equivalent, [X]% savings)
- Rationale: [Why these prices based on competitive analysis]

### Competitive Comparison
| App | Monthly | Annual | What's Included |
|-----|---------|--------|-----------------|
| [Competitor 1] | $X | $X | [Features] |
| [Competitor 2] | $X | $X | [Features] |
| Your App | $X | $X | [Features] |

## Trial Strategy
- Trial length: [X] days
- Trial includes: Full premium access
- Pre-expiry messaging: [plan]
- Post-expiry messaging: [plan]

## Billing Lifecycle
- Grace period: [X] days
- Account hold: [X] days
- Pause: Enabled / Disabled
- Proration: [strategy for upgrades/downgrades]

## Revenue Projection
| Scenario | Month 3 | Month 6 | Month 12 |
|----------|---------|---------|----------|
| Pessimistic (2% conv, 12% churn) | $[X] | $[X] | $[X] |
| Expected (4% conv, 8% churn) | $[X] | $[X] | $[X] |
| Optimistic (7% conv, 5% churn) | $[X] | $[X] | $[X] |

## Implementation Priority
1. [First: MVP subscription with 1 tier]
2. [Second: Trial flow and messaging]
3. [Third: Analytics and optimization]
4. [Later: Additional tiers if data supports it]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on designing a complete subscription offering, not just picking a price
- **ST-02** (Structured Sequential Instructions) — Five-phase process from tier design through billing lifecycle
- **RT-02** (Multi-Dimensional Analysis) — Feature gating evaluated across demand, cost, revenue, and competitive dimensions
- **CM-01** (Explicit Context Framing) — Extensive context gathering about app, audience, competition, and constraints
- **DS-06** (Prioritization Guidance) — Feature gate decision matrix and tier placement rules with clear prioritization criteria

---

## Related Prompts

- `monetization_model_selector.md` — Choose the right monetization model before designing subscriptions
- `monetization_paywall_optimization.md` — Design the paywall screen that sells subscriptions
- `monetization_pricing_strategy.md` — Deep dive into pricing research and regional pricing
- `monetization_play_billing_implementation.md` — Implement the subscription billing code in Kotlin
- `monetization_revenue_analytics.md` — Track and analyze subscription metrics (MRR, churn, LTV)

---

## Customization Guide

- **For content apps (news, recipes, learning):** Emphasize metered access (5 free articles/month) over feature gating. Content freshness justifies ongoing subscription. Consider a "credits" system where free users get N credits per month.
- **For productivity apps:** Focus on usage limits (projects, storage, exports) rather than feature locking. Power users self-select into premium by hitting natural limits. Include team/collaboration features as a future premium expansion.
- **For fitness/health apps:** Trial length should be 14 days (habit formation takes time). Gate advanced analytics, workout plans, and historical trends. Keep basic tracking free — it's the hook.
- **For apps targeting emerging markets:** Consider a separate, cheaper tier for price-sensitive regions. Google Play supports country-specific pricing — use it. $1.99/month in India can be the equivalent of $9.99/month in the US relative to purchasing power.
- **For apps with existing free users:** Never take away features users currently have for free. Instead, add new premium features and gate those. Grandfather existing users with a generous transition period. Communicate changes 30+ days in advance.
