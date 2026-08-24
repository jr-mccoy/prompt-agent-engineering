---
title: "Solo Developer Financial Planning"
category: startup/business-operations
description: "Financial planning framework for a solo app developer — monthly burn rate calculation, runway estimation, revenue milestones, and the decision framework for when to go full-time"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
difficulty: intermediate
tags:
  - solo-developer
  - startup
  - financial-planning
  - revenue
  - android
  - runway
  - burn-rate
updated: "2026-02-11"
---

# Solo Developer Financial Planning

**Objective:** Build a complete financial model for a solo app developer — from calculating your true monthly burn rate and business runway, to setting revenue milestones, deciding when (and whether) to go full-time, and managing the reinvestment vs. income tension — producing a financial dashboard and decision framework you can review monthly.

**When to Use:** Use this prompt when you're earning your first app revenue and need to understand the financial picture, when you're considering quitting your day job to go full-time, when you need to decide how much to reinvest vs. take as income, or when you simply want to stop guessing and start tracking. Financial clarity reduces anxiety and prevents the two most common failure modes: running out of money and making premature leaps.

**Important context:** Most solo developers are excellent engineers and terrible financial planners. That's not an insult — it's a skill gap that's easy to fix. Financial planning for a one-person app business is dramatically simpler than corporate finance. You need to understand about five numbers and review them monthly. This guide teaches you which numbers matter, how to calculate them, and how to make decisions based on them.

---

## Context Gathering

Before building your financial plan, understand your starting position:

1. **Personal Financial Situation:**
   - "What are your total monthly personal expenses (rent, food, insurance, debt payments, everything)?"
   - "Do you have an emergency fund? How many months of expenses does it cover?"
   - "Do you have any debt (student loans, credit cards, car payment)?"
   - "Do you have dependents (spouse, children) relying on your income?"

2. **Current Income:**
   - "What is your current salary or primary income?"
   - "Do you have any other income sources?"
   - "What benefits does your current job provide (health insurance, retirement match, etc.)?"
   - "What is the value of those benefits in dollar terms?"

3. **App Business Financials:**
   - "What is your current monthly app revenue (if any)?"
   - "What is the revenue trend — growing, flat, declining?"
   - "What are your current monthly business expenses (hosting, tools, subscriptions)?"
   - "Have you invested any money into the business (equipment, contractors, marketing)?"

4. **Goals and Timeline:**
   - "Is going full-time on your app a goal, or is this a side project?"
   - "If you want to go full-time, what's your target timeline?"
   - "What does financial success look like for you (replace salary, build wealth, lifestyle freedom)?"
   - "What is your risk tolerance (conservative, moderate, aggressive)?"

---

## Instructions

### CRITICAL: Verification Requirements

1. **Burn rate must include ALL expenses, not just obvious ones** — Health insurance, taxes, and benefit replacement are the biggest surprises when going full-time. A developer earning $120K salary actually needs much more than $120K in app revenue to replace that income.
2. **Revenue projections must be based on actual data, not hope** — Use your real growth rate, not "I think it could grow 50% per month." If you have no data, use conservative estimates.
3. **Tax burden must be factored into all calculations** — Self-employment income is taxed differently (and usually higher) than W-2 salary. Factor in the 15.3% self-employment tax.
4. **Emergency fund recommendations must account for the volatility of app revenue** — App revenue is not a steady paycheck. It fluctuates with seasonality, algorithm changes, and market shifts.
5. **The "go full-time" analysis must include non-financial factors** — Career risk, mental health, relationship strain, and opportunity cost of leaving your current job.
6. **Acceptable null result:** If the numbers clearly show that going full-time would be financially reckless given current revenue and savings, say so clearly and provide the milestones needed before it becomes viable.

### False-Positive Prevention

- ❌ Do NOT encourage quitting a day job based on one good month of revenue — require 6+ months of data
- ❌ Do NOT calculate runway without including taxes — self-employment tax alone is 15.3% of net income
- ❌ Do NOT ignore the cost of health insurance — this is $300-$800/month for an individual in the US and must be budgeted
- ❌ Do NOT assume revenue will keep growing — model flat and declining scenarios too
- ❌ Do NOT conflate revenue with profit — cloud costs, subscriptions, and contractor payments reduce what you actually keep
- ❌ Do NOT use vanity metrics like gross revenue when net profit is what matters
- ✅ DO use conservative estimates for all projections
- ✅ DO include the full cost of replacing employer benefits
- ✅ DO model multiple scenarios (optimistic, realistic, pessimistic)
- ✅ DO factor in quarterly estimated tax payments as a cash flow event
- ✅ DO recommend maintaining an emergency fund appropriate for variable income

---

### Phase 1: Understanding Your Numbers

#### 1.1 Key Terms in Plain Language

| Term | What It Means | Example |
|------|-------------|---------|
| **Revenue** | Total money coming in before any expenses | You earned $3,000 from app subscriptions this month |
| **Expenses** | Money going out for the business | $50 Firebase, $20 domain, $200 contractor = $270 |
| **Net Profit** | Revenue minus expenses — what you actually keep | $3,000 - $270 = $2,730 |
| **Burn Rate** | How much money you spend per month (personal + business) | $4,500 personal + $270 business = $4,770/month |
| **Runway** | How many months you can survive at current burn rate with current savings | $50,000 savings / $4,770 burn = 10.5 months |
| **MRR** | Monthly Recurring Revenue — predictable revenue that repeats | 150 subscribers x $4.99/month = $748.50 MRR |
| **ARR** | Annual Recurring Revenue — MRR x 12 | $748.50 x 12 = $8,982 ARR |
| **Unit Economics** | Revenue and cost per individual user/subscriber | Each subscriber costs $0.50 to acquire and pays $4.99/month |
| **Churn Rate** | Percentage of subscribers who cancel per month | 10 of 150 subscribers cancel = 6.7% monthly churn |
| **LTV** | Lifetime Value — total revenue from one customer over their lifetime | If average subscriber stays 8 months: 8 x $4.99 = $39.92 LTV |
| **CAC** | Customer Acquisition Cost — what you pay to get one customer | $50 ad spend / 10 new subscribers = $5.00 CAC |

#### 1.2 The Only 5 Numbers That Matter Initially

When you're starting out, don't overcomplicate it. Track these five numbers monthly:

1. **Monthly Revenue** — What came in
2. **Monthly Expenses** — What went out (business only)
3. **Monthly Net Profit** — Revenue minus expenses
4. **Personal Burn Rate** — Your total monthly personal cost of living
5. **Savings Balance** — Your financial cushion

Everything else (LTV, CAC, churn) matters later when you have enough data to calculate them meaningfully.

---

### Phase 2: Burn Rate Worksheet

#### 2.1 Personal Monthly Expenses

Fill this out honestly. Include everything. The most common mistake is underestimating by 20-30%.

```markdown
## Personal Monthly Expenses

### Fixed Expenses (same every month)
- Rent/Mortgage:              $________
- Car payment:                $________
- Student loan payment:       $________
- Other debt payments:        $________
- Health insurance:           $________  ← If employed, what would this cost on marketplace?
- Car insurance:              $________
- Phone plan:                 $________
- Internet:                   $________
- Streaming/subscriptions:    $________
- Gym membership:             $________
- Other fixed:                $________

### Variable Expenses (estimate monthly average)
- Groceries:                  $________
- Dining out:                 $________
- Gas/transportation:         $________
- Utilities (electric, water)$________
- Clothing:                   $________
- Entertainment:              $________
- Personal care:              $________
- Gifts:                      $________
- Miscellaneous:              $________

### Often Forgotten
- Annual expenses / 12:       $________  ← (car registration, tax prep, etc.)
- Medical co-pays/dental:     $________
- Pet expenses:               $________
- Home maintenance:           $________
- Savings contributions:      $________  ← (retirement, emergency fund)

### TOTAL PERSONAL BURN RATE:  $________/month
```

#### 2.2 Business Monthly Expenses

```markdown
## Business Monthly Expenses

### Infrastructure
- Firebase/Cloud hosting:     $________
- Domain name (annual/12):    $________
- CDN (if applicable):       $________
- Other hosting/APIs:         $________

### Tools & Software
- IDE/editor license:         $________
- Design tools (Figma etc.): $________
- Analytics tools:            $________
- Email service:              $________
- Project management:         $________
- Other subscriptions:        $________

### Services
- Registered agent:           $________  ← (annual/12)
- Accounting software:        $________
- Contractor payments:        $________
- Marketing spend:            $________

### Fees
- Google Play (annual/12):    $________  ← ($25 one-time, then ~$2/month amortized)
- Payment processing fees:    $________  ← (Google takes 15-30% of in-app purchases)
- State annual report (/12):  $________

### TOTAL BUSINESS BURN RATE:  $________/month
```

#### 2.3 Total Burn Rate

```
Personal burn rate:    $________
+ Business burn rate:  $________
= TOTAL BURN RATE:     $________/month
```

**Important note on Google's commission:** Google takes 15% of the first $1M in annual revenue (reduced from the historical 30%). This means if your app earns $1,000 in gross revenue, you receive $850. Always use NET revenue (after Google's cut) in your financial planning.

---

### Phase 3: Runway Calculator

#### 3.1 Basic Runway (No Revenue)

```
Savings balance:           $________
÷ Total monthly burn rate: $________
= RUNWAY:                  ________ months
```

#### 3.2 Adjusted Runway (With Revenue)

```
Savings balance:                      $________
÷ (Burn rate - Monthly net profit):   $________
= ADJUSTED RUNWAY:                    ________ months
```

Example: $50,000 savings, $4,770 burn rate, $2,000 net profit:
- Without revenue: $50,000 / $4,770 = 10.5 months
- With revenue: $50,000 / ($4,770 - $2,000) = 18 months

#### 3.3 Runway Scenarios

Always model three scenarios:

| Scenario | Revenue Assumption | Adjusted Burn | Runway |
|----------|-------------------|---------------|--------|
| **Pessimistic** | Revenue drops 30% | $________ | ________ months |
| **Realistic** | Revenue stays flat | $________ | ________ months |
| **Optimistic** | Revenue grows 15%/month | $________ | ________ months |

**Rule of thumb:** Make decisions based on the pessimistic scenario. Plan for the realistic one. Hope for the optimistic one.

#### 3.4 Minimum Runway Thresholds

| Situation | Minimum Runway Before Going Full-Time |
|-----------|---------------------------------------|
| Single, no dependents, low expenses | 6 months |
| Single with moderate expenses | 9 months |
| Partner/spouse with income | 6 months (their income provides a safety net) |
| Sole income provider, dependents | 12 months minimum |
| Significant debt obligations | 12+ months, or pay down debt first |

These are minimums. More conservative is always safer.

---

### Phase 4: Revenue Milestones

#### 4.1 Milestone Framework

Set concrete revenue milestones instead of vague goals. Each milestone unlocks a decision:

| Milestone | Monthly Net Profit | What It Means | Decision Unlocked |
|-----------|-------------------|---------------|-------------------|
| **Ramen Profitable** | Covers business expenses | Business sustains itself | Stop funding the business from savings |
| **Side Hustle** | $500-$2,000 | Meaningful supplemental income | Reinvest in growth or pocket it |
| **Salary Supplement** | $2,000-$5,000 | Covers a significant chunk of expenses | Start building the full-time financial runway |
| **Salary Replacement** | Covers full personal burn rate | Could survive on app income alone | Evaluate going full-time (see Phase 5) |
| **Salary + Buffer** | 1.5x personal burn rate | Covers expenses plus savings/taxes | Seriously consider going full-time |
| **Comfortable** | 2x personal burn rate | Covers expenses, taxes, savings, and reinvestment | Strong position for full-time transition |

#### 4.2 Revenue Growth Reality Check

App revenue growth is NOT linear. Here's what typical growth patterns look like:

```
Launch spike → Drop → Slow growth → Plateau → (Feature release spike → New plateau)
```

Common growth rates for indie Android apps after the launch spike settles:
- **Organic growth (no marketing spend):** 0-5% month-over-month
- **With ASO optimization:** 5-15% month-over-month for 3-6 months, then plateauing
- **With paid acquisition:** Depends entirely on CAC vs. LTV ratio
- **With viral/word-of-mouth features:** Unpredictable spikes

**Do not plan your finances around optimistic growth.** Plan around flat revenue and be pleasantly surprised if it grows.

---

### Phase 5: The Full-Time Decision Framework

#### 5.1 Financial Readiness Checklist

All of these should be YES before quitting your day job:

- [ ] App revenue has been consistent for 6+ months (not just one good month)
- [ ] Monthly net profit covers at least 100% of personal burn rate (150% is better)
- [ ] Emergency fund covers 6-12 months of full burn rate (personal + business)
- [ ] Health insurance alternative identified and priced into burn rate
- [ ] Quarterly estimated tax payments calculated and budgeted
- [ ] No high-interest debt (credit cards fully paid off)
- [ ] Revenue trend is stable or growing (not declining)
- [ ] You have modeled the pessimistic scenario and can survive it

#### 5.2 The True Cost of Leaving Employment

Your salary is NOT the only thing you lose. Calculate the full cost:

| Item | Monthly Value | Notes |
|------|-------------|-------|
| Base salary | $________ | Gross, divided by 12 |
| Employer health insurance contribution | $________ | Often $500-$1,500/month for an individual |
| 401(k)/retirement match | $________ | Free money you're giving up |
| Employer's share of payroll taxes | $________ | ~7.65% of salary (you now pay both halves) |
| Paid time off value | $________ | (Vacation days x daily rate) / 12 |
| Other benefits (life insurance, disability, HSA) | $________ | Company contributions |
| **TOTAL COMPENSATION** | **$________** | This is what your app needs to replace |

**Example:** A developer earning $120K salary with benefits:
- Salary: $10,000/month
- Health insurance: $800/month (employer's portion)
- 401(k) match: $500/month
- Payroll tax (employer half): $765/month
- PTO value: $460/month
- **Total: $12,525/month** — not $10,000

And your app revenue is subject to self-employment tax (15.3%), so you need to earn even more:
- **Revenue needed to net $12,525:** approximately $14,800/month (after self-employment tax)

This is why so many developers who quit their jobs feel the financial squeeze even when their app revenue "matches" their salary.

#### 5.3 The Part-Time Bridge Strategy

Going full-time doesn't have to be a binary switch. Consider these transition approaches:

| Strategy | How It Works | Risk Level |
|----------|------------|------------|
| **Cold turkey** | Quit job, go all-in on app | Highest risk, highest focus |
| **Reduce hours** | Negotiate part-time at current job | Moderate risk, keeps some safety net |
| **Freelance bridge** | Leave job but freelance 2 days/week for income | Moderate risk, but freelancing competes for time |
| **Sabbatical test** | Take 3-6 month unpaid leave to try full-time | Low risk, can return to job |
| **Slow build** | Keep day job, grow app until revenue reaches 2x threshold | Lowest risk, slowest path |

---

### Phase 6: Reinvestment vs. Income

#### 6.1 The Reinvestment Decision Framework

When your app generates profit, you face a constant decision: reinvest in growth or take the money as personal income.

| Revenue Level | Recommended Split | Why |
|--------------|-------------------|-----|
| $0-$500/month profit | 80% reinvest, 20% personal | Business needs growth fuel |
| $500-$2,000/month | 60% reinvest, 40% personal | Balance growth with reward |
| $2,000-$5,000/month | 50% reinvest, 50% personal | Sustainable balance |
| $5,000+/month | 40% reinvest, 60% personal | Business can grow efficiently at scale |

**What to reinvest in (priority order):**

1. **Infrastructure reliability** — Don't let your app go down because you're saving $20/month on hosting
2. **User experience improvements** — Design contractor, UX audit, icon/screenshot refresh
3. **Marketing** — ASO, content marketing, targeted ads (only when you know your unit economics)
4. **Tools that save time** — If a $30/month tool saves you 4 hours/month, that's a bargain
5. **Learning** — Courses, conferences, books that directly improve your product or business skills

**What NOT to reinvest in:**
- Expensive office space (work from home)
- Premium tools you don't fully utilize
- Marketing without tracking ROI
- "Nice to have" features that don't impact revenue or retention

#### 6.2 The Tax Set-Aside Rule

Before deciding reinvest vs. income, set aside money for taxes:

```
Monthly net profit:               $________
× 30% tax reserve:                $________  ← Set this aside in a separate savings account
= Available for reinvest/income:  $________
```

The 30% is a rough estimate covering:
- Self-employment tax: ~15.3%
- Federal income tax: ~10-22% (varies by bracket)
- State income tax: 0-13% (varies by state)

Your effective rate depends on your total income and deductions. A CPA can give you a precise number, but 30% is a safe starting estimate. Underpaying estimated taxes results in penalties.

---

### Phase 7: Monthly Financial Review

#### 7.1 The 30-Minute Monthly Review

Do this on the first Monday of every month:

```markdown
## Monthly Financial Review: [Month Year]

### Revenue
- Gross revenue (before Google's cut):  $________
- Google's commission (15%):             $________
- Net revenue:                           $________
- Month-over-month change:               ____%

### Expenses
- Business expenses this month:          $________
- Unusual/one-time expenses:             $________

### Profit
- Net profit (revenue - expenses):       $________
- Tax set-aside (30%):                   $________
- Available profit:                      $________

### Key Metrics
- MRR (if subscription):                $________
- Subscriber count:                      ________
- Churn rate:                           ____%
- New customers:                         ________

### Cash Position
- Business bank balance:                 $________
- Tax reserve account:                   $________
- Personal emergency fund:               $________
- Runway at current burn rate:           ________ months

### Decisions
- Reinvest this month: $________ on [what]
- Personal income draw: $________
- Changes needed: [any adjustments]

### Health Check
- [ ] All expenses tracked and categorized
- [ ] Tax set-aside transferred
- [ ] Runway is above minimum threshold
- [ ] Revenue trend is [growing/stable/declining] — action needed? [Y/N]
```

---

## Expected Output

```markdown
# Financial Plan: [App Name]

## Current Position
- Monthly personal burn rate: $[amount]
- Monthly business burn rate: $[amount]
- Total burn rate: $[amount]
- Current monthly net profit: $[amount]
- Savings balance: $[amount]
- Current runway: [N] months

## Revenue Milestones

| Milestone | Target MRR | Status | Projected Date |
|-----------|-----------|--------|---------------|
| Ramen Profitable | $[business expenses] | [status] | [date] |
| Side Hustle | $[amount] | [status] | [date] |
| Salary Supplement | $[amount] | [status] | [date] |
| Salary Replacement | $[personal burn] | [status] | [date] |
| Salary + Buffer | $[1.5x burn] | [status] | [date] |

## Full-Time Readiness
- Revenue consistency (6+ months): [Yes/No]
- Net profit vs. burn rate: [N]% covered
- Emergency fund: [N] months
- Health insurance plan: [identified/not yet]
- True compensation replacement needed: $[amount]/month

## Monthly Actions
- Tax set-aside: $[amount] → tax reserve account
- Reinvestment budget: $[amount] → [allocation]
- Personal income draw: $[amount]
- Monthly review date: 1st Monday of each month

## Scenario Analysis

| Scenario | Monthly Revenue | Runway | Action |
|----------|----------------|--------|--------|
| Pessimistic (-30%) | $[amount] | [N] months | [plan] |
| Realistic (flat) | $[amount] | [N] months | [plan] |
| Optimistic (+15%/mo) | $[amount] | [N] months | [plan] |
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on financial planning decisions specific to solo developers
- **ST-02** (Structured Sequential Instructions) — Phased approach from understanding numbers to making decisions
- **RT-02** (Multi-Dimensional Analysis) — Analyzing financials across revenue, expenses, taxes, and risk dimensions
- **CM-01** (Explicit Context Framing) — Solo developer constraints: variable income, no employer benefits, one-person operations
- **DS-06** (Prioritization Guidance) — Revenue milestones ordered by decision impact

---

## Related Prompts

- `solo_dev_business_formation.md` — Entity decisions that affect tax treatment and costs
- `solo_dev_tax_strategy.md` — Detailed tax planning including quarterly estimated payments
- `monetization_model_selector.md` — Revenue model decisions that feed into financial planning
- `solo_dev_metrics_dashboard.md` — Business metrics that drive financial decisions
- `solo_dev_decision_framework.md` — Framework for reinvestment and growth decisions

---

## Customization Guide

- **For developers still employed full-time:** Focus on Phases 1-4 (understanding numbers and setting milestones). Phase 5 (full-time decision) becomes relevant when revenue approaches your burn rate.
- **For developers already full-time:** Skip Phase 5 and focus heavily on Phase 6 (reinvestment) and Phase 7 (monthly review). Your financial discipline is now your company's financial discipline.
- **For developers with a working spouse/partner:** Your burn rate calculation changes significantly. Shared expenses reduce your individual burden. Factor in the safety net of a second income when assessing runway.
- **For developers with significant savings ($100K+):** Your runway is longer, which changes the risk calculus. You can afford to invest more aggressively in growth and take the full-time leap earlier. But don't mistake a long runway for infinite runway.
- **For developers earning under $100/month from their app:** Focus on product-market fit and growth, not financial optimization. At this revenue level, your time is better spent improving the app than building financial models. Track the five basic numbers and revisit this guide when revenue is meaningful.
