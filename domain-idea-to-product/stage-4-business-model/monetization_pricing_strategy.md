---
title: "Pricing Strategy"
category: startup/monetization
description: "Set optimal pricing for Android app subscriptions and in-app purchases — competitive analysis, willingness-to-pay research, Van Westendorp model, Play Store regional pricing, price anchoring, introductory offers, price change strategy, and sensitivity analysis for solo developers"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-03
  - CM-01
  - DS-06
difficulty: intermediate
tags:
  - monetization
  - android
  - pricing
  - subscriptions
  - iap
  - willingness-to-pay
  - regional-pricing
  - solo-developer
updated: "2026-02-11"
---

# Pricing Strategy

**Objective:** Set optimal pricing for an Android app's subscriptions and in-app purchases — using competitive analysis, willingness-to-pay research (including the Van Westendorp Price Sensitivity Meter), Google Play Store regional pricing strategies, price anchoring psychology, introductory offer design, and a safe price change playbook — so that you capture maximum revenue without over-pricing your way out of conversions or under-pricing your way into unsustainability.

**When to Use:** Use this after you have designed your subscription tiers (see `monetization_subscription_design.md`) and need to determine the exact dollar amounts. Pricing is the single highest-leverage decision in monetization — a 20% price increase with no conversion drop doubles your margin more than a 20% user increase would. This prompt covers the research, psychology, and mechanics of getting the number right. Use it before your initial launch and again every 6-12 months when re-evaluating.

---

## Context Gathering

Before setting pricing, gather essential context:

1. **Your App and Market:**
   - "What specific value does your app deliver? What problem does it solve?"
   - "What category does your app compete in (productivity, fitness, education, etc.)?"
   - "How established is your app (pre-launch, early, growing, mature)?"
   - "What is your current user base size and growth rate?"

2. **Competitive Landscape:**
   - "Who are your top 5 competitors (direct and indirect)?"
   - "What do they charge for monthly subscriptions? Annual?"
   - "What do competitor users say about pricing in reviews (too expensive? worth it? bargain?)?"
   - "Are there strong free alternatives?"

3. **Your Users:**
   - "What is the geographic distribution of your users (top 5 countries)?"
   - "Are your users consumers, professionals, or students?"
   - "What other paid apps or subscriptions do your users likely have?"
   - "Have you received any feedback about pricing (too high, too low, requests for features at any price)?"

4. **Your Economics:**
   - "What are your monthly operating costs (servers, APIs, tools)?"
   - "What monthly revenue do you need to sustain full-time development?"
   - "What is your current conversion rate (if you already have a paid tier)?"
   - "Are there variable costs that scale with users (API calls, storage, bandwidth)?"

5. **Pricing History:**
   - "Have you priced this app before? What happened?"
   - "Have you run any pricing experiments?"
   - "What is the most a user has ever paid for your product or service?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before setting ANY price point, you MUST:**

1. **Research at least 3 competitors' pricing** — Pricing in a vacuum is guessing. Users compare your price to alternatives. If you are 3x the competition with no clear differentiation, conversions will suffer. If you are 50% cheaper, users may question quality.
2. **Calculate your break-even point** — Know exactly how many subscribers or purchases you need to cover costs. If break-even requires 10,000 subscribers and you have 1,000 users with a 3% conversion rate, your price point won't save you — you need more users.
3. **Check Google Play's minimum prices** — Google Play has per-country minimum prices (e.g., $0.99 USD, approximately equivalent in other currencies). Your price must meet or exceed these minimums.
4. **Factor in Google's commission** — Google takes 15% on the first $1M/year (30% above that). A $4.99/month subscription nets you $4.24 after commission. All projections must use net revenue.
5. **Validate against purchasing power** — A $9.99/month subscription that works in the US may be untenable in India, Brazil, or Indonesia. Either set regional prices or accept lower conversion in those markets.
6. **Acceptable null result** — It is valid to conclude that you do not have enough data to set a confident price. If you have fewer than 100 survey responses or no competitive benchmarks, recommend launching at a conservative price and iterating based on data.

### False-Positive Prevention

- Do NOT set pricing based on what you think your app is "worth" — price based on what the market will pay
- Do NOT copy a competitor's exact pricing without understanding their positioning, feature set, and audience
- Do NOT ignore regional pricing — 70% of Android users are in markets where US pricing is not viable
- Do NOT set one price and forget it — pricing should be reviewed every 6-12 months
- Do NOT raise prices without a communication plan and grandfathering strategy
- Do NOT use penetration pricing (cheap to win users, raise later) unless you have funding to sustain losses
- DO research willingness to pay before picking a number
- DO use price anchoring (show annual savings relative to monthly)
- DO set regional prices manually rather than relying solely on Google's auto-conversion
- DO offer introductory pricing for new subscribers to reduce commitment friction
- DO test price points with real users when possible (A/B or sequential testing)
- DO document your pricing rationale so future-you understands why you chose these numbers

---

### Phase 1: Competitive Benchmarking

#### 1.1 Competitive Price Map

Build this table for your top 5 competitors:

| Competitor | Monthly Price | Annual Price | Annual Discount % | Free Tier? | Key Premium Features | Play Store Rating | Pricing Sentiment in Reviews |
|-----------|--------------|-------------|-------------------|-----------|---------------------|-------------------|------------------------------|
| [Competitor A] | $[X]/mo | $[X]/yr | [X]% | Yes/No | [Features] | [X] stars | [Summary of pricing feedback] |
| [Competitor B] | $[X]/mo | $[X]/yr | [X]% | Yes/No | [Features] | [X] stars | [Summary] |
| [Competitor C] | $[X]/mo | $[X]/yr | [X]% | Yes/No | [Features] | [X] stars | [Summary] |
| [Competitor D] | $[X]/mo | $[X]/yr | [X]% | Yes/No | [Features] | [X] stars | [Summary] |
| [Competitor E] | $[X]/mo | $[X]/yr | [X]% | Yes/No | [Features] | [X] stars | [Summary] |

**How to gather this data:**
1. Download competitor apps and navigate to their paywall/pricing screen
2. Check their Play Store listing for subscription details (often listed under "In-app purchases")
3. Read the most recent 50 reviews filtered for "price," "expensive," "subscription," and "worth"
4. Note their Play Store "Top Developer" or "Editors' Choice" status (affects pricing power)

#### 1.2 Positioning Matrix

Plot yourself against competitors on a 2x2 matrix:

```
            Premium Pricing ($10+/mo)
                    │
        ┌───────────┼───────────┐
        │    Niche  │  Premium  │
        │   Expert  │  Leader   │
        │           │           │
Low ────┼───────────┼───────────┼──── High
Feature │           │           │ Feature
Count   │   Budget  │   Value   │ Count
        │   Option  │   Leader  │
        │           │           │
        └───────────┼───────────┘
                    │
            Budget Pricing ($1-4/mo)
```

**Your positioning determines your pricing lane:**
- **Premium Leader:** You have the most features AND charge the most. Requires proven value.
- **Value Leader:** You have the most features at a moderate price. Hard to sustain long-term.
- **Niche Expert:** You have fewer features but deep expertise, justifying a premium. Best for solo devs.
- **Budget Option:** You are the cheapest. Race to the bottom — avoid this unless volume is your strategy.

#### 1.3 Competitive Pricing Boundaries

```
Pricing floor (minimum viable):
  = MAX(Google Play minimum, break-even revenue / expected subscriber count)

Competitive median:
  = Median of competitor monthly prices

Pricing ceiling (maximum viable):
  = Highest competitor price that maintains positive review sentiment about pricing

Your target range:
  = Competitive median × 0.8 to Competitive median × 1.2

  If you have MORE features → price at 1.0-1.2x median
  If you have FEWER but deeper features → price at 0.9-1.1x median
  If you are new/unknown → price at 0.7-0.9x median initially
```

---

### Phase 2: Willingness-to-Pay Research

#### 2.1 The Van Westendorp Price Sensitivity Meter

The Van Westendorp model uses 4 questions to identify the optimal price range:

**Survey Questions (ask existing users or target audience):**
1. "At what price would you consider [App Premium] to be so expensive that you would NOT consider buying it?" (Too Expensive)
2. "At what price would you consider [App Premium] to be priced so low that you would question its quality?" (Too Cheap)
3. "At what price would you consider [App Premium] to be starting to get expensive, but you'd still consider buying it?" (Expensive/High Side)
4. "At what price would you consider [App Premium] to be a bargain — a great buy for the money?" (Cheap/Good Value)

**How to run this survey:**
- Use Google Forms, Typeform, or an in-app survey
- Target: Minimum 50 responses (100+ preferred for reliability)
- Include only active users who have experienced both free and premium features
- Provide a clear feature list of what "Premium" includes before the questions

#### 2.2 Interpreting Van Westendorp Results

Plot the cumulative distribution of responses:

```
100% ──────────────┐
     Too Cheap ──→ │╲         ╱── Too Expensive
                   │  ╲     ╱
                   │    ╲ ╱      ← Point of Marginal
 50% ──────────────│─────╳────     Expensiveness (PME)
                   │   ╱ ╲
                   │ ╱     ╲
                   │╱    ↑   ╲── Expensive
  0% ──────────────┴─────┴────
                  $2  $5  $8  $12

Key intersections:
  • OPP (Optimal Price Point): Where "Too Cheap" and "Too Expensive" cross
    = The price with the least resistance from both directions

  • IPP (Indifference Price Point): Where "Cheap" and "Expensive" cross
    = The price users consider "normal" — neither a deal nor expensive

  • PME (Point of Marginal Expensiveness): Where "Expensive" and "Too Expensive" cross
    = Upper boundary — do not price above this

  • PMC (Point of Marginal Cheapness): Where "Cheap" and "Too Cheap" cross
    = Lower boundary — do not price below this

  Your acceptable range: PMC to PME
  Your recommended price: Between OPP and IPP
```

#### 2.3 Quick Willingness-to-Pay Methods (When You Cannot Run a Full Survey)

**Method 1: Review Mining (No survey needed)**
1. Read 100+ competitor reviews mentioning price
2. Categorize as: "Too expensive," "Fair/worth it," "Great deal"
3. Note the price they reference
4. Your price should land in the "Fair/worth it" zone

**Method 2: The "Would You Pay $X?" In-App Prompt**
```
Show a non-binding prompt to free users after they've been active for 7+ days:

"Quick question: Would you pay $X.99/month for [Premium Feature A],
[Premium Feature B], and [Premium Feature C]?"

[ Yes, probably ]  [ Maybe ]  [ No ]

Rotate $X across users: $2.99, $4.99, $6.99, $9.99
Track response rates at each price.
```

**Method 3: Sequential Price Testing**
- Launch at price A for 4 weeks, measure conversion
- Change to price B for 4 weeks, measure conversion
- Change to price C for 4 weeks, measure conversion
- Compare revenue (not just conversion rate) across periods
- Warning: Seasonality and feature changes can confound results

#### 2.4 Price Elasticity Estimation

```
Price elasticity = % change in conversion / % change in price

Elastic demand (|elasticity| > 1):
  A 10% price increase causes >10% conversion decrease
  → Your users are price-sensitive; keep prices low
  → Common in: utility apps, general-purpose tools, student audiences

Inelastic demand (|elasticity| < 1):
  A 10% price increase causes <10% conversion decrease
  → Your users value the product enough to absorb increases
  → Common in: professional tools, health apps, niche expertise

Unit elastic (|elasticity| ≈ 1):
  Revenue stays roughly the same regardless of price direction
  → Optimize for subscriber volume (lower price) or margin (higher price)
```

**How to estimate elasticity without an economist:**
- If 80%+ of your users are in the US/EU and use your app for work: likely inelastic
- If your users are students, casual users, or primarily in emerging markets: likely elastic
- If you have no free alternative: less elastic. If strong free alternatives exist: more elastic.

---

### Phase 3: Regional Pricing

#### 3.1 Google Play Regional Pricing Options

**Option A: Auto-Converted Pricing (Default)**
- You set a USD price, Google converts to local currency using current exchange rates
- Pros: Zero effort
- Cons: Exchange rates fluctuate; prices in some markets become unreasonable
- Result: $9.99 USD becomes ~800 INR in India (which is 2-3x what users will pay)

**Option B: Manual Regional Pricing (Recommended)**
- You set specific prices for each country or region
- Pros: Prices optimized for local purchasing power
- Cons: Requires research and periodic updates
- Result: $9.99 USD in US, 299 INR in India (~$3.60), R$14.90 in Brazil (~$2.80)

#### 3.2 Purchasing Power Parity (PPP) Pricing Table

Use this table to set prices relative to US pricing:

| Region | PPP Multiplier | US $4.99/mo Equivalent | US $9.99/mo Equivalent | Notes |
|--------|---------------|----------------------|----------------------|-------|
| **United States** | 1.0x | $4.99 | $9.99 | Baseline |
| **Canada** | 0.9x | CAD $5.99 | CAD $12.99 | Similar to US |
| **UK** | 0.9x | GBP 3.99 | GBP 7.99 | Slightly lower |
| **EU (Western)** | 0.85x | EUR 4.49 | EUR 8.99 | VAT included |
| **EU (Eastern)** | 0.5-0.6x | EUR 2.99 | EUR 5.99 | Poland, Romania, etc. |
| **Australia** | 0.85x | AUD 7.99 | AUD 14.99 | Higher nominal, similar PPP |
| **Japan** | 0.8x | JPY 480 | JPY 980 | Price-sensitive mobile market |
| **South Korea** | 0.7x | KRW 4,900 | KRW 8,900 | Competitive app market |
| **Brazil** | 0.3-0.4x | BRL 9.90 | BRL 19.90 | Highly price-sensitive |
| **India** | 0.15-0.25x | INR 149 | INR 299 | Most price-sensitive major market |
| **Indonesia** | 0.2-0.3x | IDR 29,000 | IDR 59,000 | Large market, very price-sensitive |
| **Mexico** | 0.35-0.45x | MXN 49 | MXN 89 | Growing market |
| **Russia** | 0.3-0.4x | RUB 199 | RUB 399 | Sanctions may affect payments |
| **Turkey** | 0.2-0.3x | TRY 59.99 | TRY 109.99 | High inflation, adjust frequently |
| **Nigeria** | 0.1-0.2x | NGN 999 | NGN 1,999 | Emerging market |

#### 3.3 Setting Regional Prices in Google Play Console

```
Steps:
1. Open Google Play Console → Subscriptions (or In-app products)
2. Select your subscription
3. Click "Set prices"
4. Default: "Use converted price from default country"
5. Override: Click individual countries and set custom prices
6. Save and publish

Key considerations:
- Google Play enforces minimum prices per country
- Prices must end in approved increments (varies by currency)
- You can update prices without creating a new subscription product
- Existing subscribers keep their current price until you explicitly migrate them
```

#### 3.4 Regional Pricing Revenue Impact

**Case study: Before vs. after regional pricing optimization**

| Metric | Auto-Converted (Before) | PPP-Adjusted (After) | Change |
|--------|------------------------|---------------------|--------|
| US conversion rate | 4.2% | 4.2% | No change |
| India conversion rate | 0.3% | 2.8% | +833% |
| Brazil conversion rate | 0.8% | 3.1% | +288% |
| Global blended conversion | 1.8% | 3.4% | +89% |
| ARPU (US) | $4.99 | $4.99 | No change |
| ARPU (India) | $0.01 | $0.45 | +4400% |
| Total monthly revenue | $1,200 | $2,850 | +138% |

**The insight:** Lower prices in price-sensitive markets increase total revenue because the volume increase more than compensates for the per-user revenue decrease.

---

### Phase 4: Price Psychology

#### 4.1 Price Anchoring Techniques

**Technique 1: Annual vs. Monthly Anchor**
```
Show monthly price first (the "anchor"), then reveal the savings:

  Monthly:  $6.99/month
  Annual:   $3.58/month (billed as $42.99/year)
            ─── Save 49% ───

The $6.99 anchor makes $3.58 feel like a steal.
Result: 40-60% of subscribers choose annual (vs. 20-30% without anchoring).
```

**Technique 2: Per-Day Framing**
```
Instead of:  "$47.99/year"
Show:        "Just $0.13/day — less than a cup of coffee per week"

Per-day framing reduces perceived cost by 60-70% in user perception studies.
Best for: Annual subscriptions over $20/year.
```

**Technique 3: Three-Tier Decoy**
```
┌──────────────┬──────────────┬──────────────┐
│    Basic     │     Pro      │   Premium    │
│  $2.99/mo    │  $7.99/mo    │  $8.99/mo    │
│              │              │  ★ BEST      │
│  5 projects  │ 50 projects  │  Unlimited   │
│  No export   │ PDF export   │  All exports │
│  No sync     │ Cloud sync   │  Sync + API  │
└──────────────┴──────────────┴──────────────┘

Pro at $7.99 exists to make Premium at $8.99 an obvious choice.
Only $1 more for "unlimited" vs "50" and "all exports" vs "PDF only."
Expected result: 60-70% choose Premium, 20-25% choose Basic, 10-15% choose Pro.
```

**Technique 4: Strikethrough Pricing**
```
Original: $9.99/month
Show:     ~~$9.99/mo~~ $6.99/mo (first 3 months)

Strikethrough creates a reference price that makes the current price feel discounted,
even if no user ever paid $9.99.
Google Play supports introductory pricing natively.
```

#### 4.2 Charm Pricing Rules

| Price Type | Correct Format | Incorrect Format | Why |
|-----------|---------------|-----------------|-----|
| Consumer monthly | $4.99 | $5.00 | .99 perceived as significantly cheaper |
| Consumer annual | $47.99 | $48.00 | Same .99 effect |
| Professional monthly | $10/month | $9.99/month | Round numbers signal "professional tool" |
| Introductory | $0.99 | $1.00 | Sub-dollar feels like "almost free" |
| Premium tier | $14.99 | $15.00 | Still consumer-facing, use .99 |

**When to break the rule:** B2B or professional tools aimed at businesses can use round numbers ($10, $25, $50) to signal seriousness and simplify expense reporting.

#### 4.3 Loss Aversion and Trial Design

```
Frame the trial end as a LOSS, not a purchase decision:

WEAK (purchase frame):
  "Your trial ended. Subscribe for $4.99/month to access Premium."

STRONG (loss frame):
  "You've used Advanced Analytics 23 times this week.
   Keep it? Subscribe for $4.99/month.
   Or switch to Free and lose access to Analytics, Cloud Sync, and Export."

The strong frame converts 20-35% better because users evaluate
what they'll LOSE, not what they'll BUY.
```

#### 4.4 The "Most Popular" Badge Effect

```
Adding a "Most Popular" or "Best Value" badge to your preferred plan
increases selection of that plan by 15-25%.

Implementation:
  ┌─────────────────────────┐
  │  ★ MOST POPULAR         │  ← Badge on the plan you want users to pick
  │  Annual: $3.58/month    │
  │  Billed as $42.99/year  │
  │  Save 49%               │
  ├─────────────────────────┤
  │  Monthly: $6.99/month   │  ← No badge, appears "standard"
  └─────────────────────────┘

Users trust social proof signals. "Most Popular" implies other users
chose this plan, reducing the decision burden.
```

---

### Phase 5: Price Change Strategy

#### 5.1 When to Raise Prices

**Raise prices when:**
- Your conversion rate is above 7% (indicates under-pricing)
- You have added significant new premium features since last pricing
- Competitor prices have increased
- Your operating costs have grown
- You have not changed prices in 12+ months and inflation has eroded real value
- Users regularly say "this is a great deal" in reviews

**Do NOT raise prices when:**
- Churn is already above 10% monthly
- You have not added new value since the last price change
- Your app is in a growth phase where user acquisition is the priority
- Competitor prices have decreased
- You have fewer than 200 active subscribers (insufficient data)

#### 5.2 How to Raise Prices Safely

```
Step 1: Grandfather existing subscribers (30-60 days minimum)
  - Existing subscribers keep current price for N months
  - Google Play supports this: existing subscriptions are NOT auto-updated

Step 2: Communicate the change (30 days before new subscriber pricing)
  - In-app notification: "Starting [date], Premium will be $X.99/month
    for new subscribers. Your price stays at $X.99/month for now."
  - Optional: "Lock in your current rate for 12 months by switching to annual."

Step 3: Increase price for new subscribers first
  - Create a new subscription product or update the price in Play Console
  - Existing subscribers remain on old pricing

Step 4: Migrate existing subscribers (optional, 60+ days later)
  - Google Play requires explicit user consent for price increases
  - Users must accept or their subscription will cancel at period end
  - Expect 5-15% churn from price migration — this is normal
  - Offer a "loyalty discount" to migrated users: "Thanks for being an
    early subscriber — here's 20% off the new price for the next year."

Step 5: Monitor and adjust
  - Track new subscriber conversion rate at new price
  - Track existing subscriber churn from migration
  - If total revenue increases despite churn, the increase was correct
  - If total revenue decreases, consider a partial rollback
```

#### 5.3 How to Lower Prices (or Offer Discounts)

```
When to lower prices:
  - Conversion rate below 1% (indicates over-pricing)
  - Entering a new market with different purchasing power
  - Competing against a new, cheaper entrant

Lowering price safely:
  - Temporary promotional pricing: "50% off for the next 30 days"
  - Seasonal sales: Align with Black Friday, New Year, back-to-school
  - Introductory pricing: Lower price for first 3 months only
  - Avoid permanent price cuts if possible — they are hard to reverse
  - Never lower prices AND reduce features simultaneously

Google Play introductory pricing:
  - Available for subscriptions
  - Set in Google Play Console under subscription settings
  - Can be free trial, discounted first period, or both
  - Example: "First month $0.99, then $4.99/month"
```

#### 5.4 Price Change Impact Calculator

```
Before the price change:
  Subscribers: [N]
  Price: $[X]/month
  Monthly revenue: $[N × X × 0.85] (after Google's 15% cut)

After the price change:
  Expected churn from price change: [5-15]%
  Remaining subscribers: [N × (1 - churn%)]
  New price: $[Y]/month
  New monthly revenue: [Remaining × Y × 0.85]

Revenue change: (New revenue - Old revenue) / Old revenue × 100

Example:
  Before: 500 subscribers × $4.99 × 0.85 = $2,120/month
  After: 500 × 0.90 (10% churn) = 450 subscribers × $6.99 × 0.85 = $2,674/month
  Revenue change: +26.1%

  Break-even churn: Old price / New price = $4.99 / $6.99 = 71.4%
  Translation: You can lose up to 28.6% of subscribers before revenue drops.
```

---

## Expected Output

```markdown
# Pricing Strategy: [App Name]

## Competitive Analysis
| Competitor | Monthly | Annual | Annual Discount | Positioning |
|-----------|---------|--------|-----------------|-------------|
| [A] | $[X] | $[X] | [X]% | [Position] |
| [B] | $[X] | $[X] | [X]% | [Position] |
| [C] | $[X] | $[X] | [X]% | [Position] |
| Market median | $[X] | $[X] | [X]% | — |

## Recommended Pricing
- Monthly: $[X].99/month
- Annual: $[X].99/year ($[X]/month equivalent, [X]% savings)
- Introductory: $[X].99 for first [N] months
- Rationale: [Competitive position + WTP data + cost analysis]

## Regional Pricing
| Country/Region | Monthly | Annual | PPP Multiplier |
|---------------|---------|--------|---------------|
| United States | $[X] | $[X] | 1.0x |
| [Country 2] | [Local currency] | [Local currency] | [X]x |
| [Country 3] | [Local currency] | [Local currency] | [X]x |

## Price Psychology
- Anchoring: [Strategy — e.g., "Monthly as anchor for annual savings"]
- Default plan: [Annual / Monthly]
- Badge: ["Best Value" on annual plan]
- Per-day framing: ["$[X]/day — less than..."]

## Revenue Projection at This Pricing
| Scenario | Subscribers (Mo 6) | Monthly Revenue | Annual Revenue |
|----------|-------------------|----------------|---------------|
| Pessimistic (2% conv, 12% churn) | [N] | $[X] | $[X] |
| Expected (4% conv, 8% churn) | [N] | $[X] | $[X] |
| Optimistic (7% conv, 5% churn) | [N] | $[X] | $[X] |

## Price Review Schedule
- Next review date: [6-12 months from now]
- Trigger conditions for early review: [Conversion <1%, competitor price change >20%]
- Price change process: [Grandfather existing, communicate 30 days, migrate 60+ days later]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on setting optimal pricing using research and psychology, not guessing
- **ST-02** (Structured Sequential Instructions) — Five-phase process from competitive analysis through price changes
- **RT-02** (Multi-Dimensional Analysis) — Pricing evaluated across competition, willingness-to-pay, regional economics, psychology, and change management
- **RT-03** (Tree of Thoughts) — Multiple pricing methods explored (Van Westendorp, competitive benchmarking, review mining, sequential testing) with strengths and weaknesses
- **CM-01** (Explicit Context Framing) — Extensive context gathering about market, users, economics, and pricing history
- **DS-06** (Prioritization Guidance) — Clear guidance on when to raise vs. lower prices, which markets to prioritize, and which anchoring techniques to use

---

## Related Prompts

- `monetization_subscription_design.md` — Design the subscription tiers that pricing applies to
- `monetization_paywall_optimization.md` — Design the paywall that presents these prices
- `monetization_revenue_analytics.md` — Track revenue metrics to validate pricing decisions
- `monetization_play_billing_implementation.md` — Implement the pricing in Google Play Billing code
- `monetization_model_selector.md` — Choose the right monetization model before pricing it

---

## Customization Guide

- **For apps with existing subscribers:** Never skip the grandfathering analysis. Existing subscribers are your most loyal users — alienating them with a surprise price increase costs more in churn and negative reviews than the revenue gain. Always grandfather for at least 3 months and communicate proactively.
- **For apps targeting a single market (US or EU only):** You can skip regional pricing complexity entirely. Focus your energy on competitive benchmarking and A/B testing price points in your single market. Regional pricing becomes important only when 20%+ of your users are in emerging markets.
- **For professional/B2B-leaning apps:** Use value-based pricing (what is the ROI of your app to the user) rather than competitive pricing. If your app saves a contractor 5 hours per month and they bill at $100/hour, $29.99/month is 6% of the value created — easy to justify.
- **For apps in highly competitive categories:** Price matching or slight undercutting the market leader is a valid strategy, but only if you can sustain the lower margin. Differentiate on features and experience rather than racing to the bottom on price. A clear "why we're different" justifies equal or higher pricing.
- **For apps with high variable costs per user:** Calculate your per-user cost carefully and ensure your price covers it with margin. If each premium user costs you $1/month in API calls and you charge $2.99, your margin after Google's cut is only $1.54 — thin enough that a cost increase wipes you out. Price with a 3x minimum margin over variable costs.
