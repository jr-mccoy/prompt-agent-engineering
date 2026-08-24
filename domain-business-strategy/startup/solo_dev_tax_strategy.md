---
title: "Solo Developer Tax Strategy"
category: startup/business-operations
description: "Tax planning framework for a solo app developer — self-employment tax, quarterly estimated payments, deductible expenses, Section 199A QBI deduction, state nexus from multi-state app sales, and international revenue considerations — with a tax calendar, deduction checklist, and estimated payment calculator"
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
  - taxes
  - tax-planning
  - self-employment
  - android
  - deductions
  - quarterly-payments
updated: "2026-02-11"
---

# Solo Developer Tax Strategy

**Objective:** Build a complete tax planning strategy for a solo app developer — from understanding self-employment tax mechanics and identifying every legitimate deduction, to calculating quarterly estimated payments, navigating state nexus from app store sales, and handling international revenue — producing a tax calendar, deduction inventory, and quarterly payment schedule you can execute throughout the year.

**When to Use:** Use this prompt when you start earning app revenue and realize the IRS expects you to pay taxes four times a year (not once), when you want to make sure you're not leaving deductions on the table, when you get a surprisingly large tax bill and want to prevent that next year, or when your app starts earning money from multiple states or countries and you don't know what that means for your taxes. Tax planning is not something you do in April — it's a year-round discipline that directly affects how much of your revenue you keep.

**Important context:** Most solo developers dramatically overpay taxes — not because the rates are high, but because they don't claim legitimate deductions and they don't plan ahead. At the same time, some developers under-pay estimated taxes and get hit with penalties in April. The sweet spot is knowing what you owe, paying it on time, and keeping every dollar the law allows you to keep. This guide teaches the fundamentals so you can have an informed conversation with your CPA rather than going in blind.

**Disclaimer:** This guide provides general educational information about tax planning for U.S.-based solo developers. It is NOT tax advice. Tax law is complex, changes frequently, and varies by state. Consult a licensed CPA or tax professional for advice specific to your situation. The information here is based on tax law as of early 2026 and may not reflect recent changes.

---

## Context Gathering

Before building your tax strategy, understand your situation:

1. **Business Structure:**
   - "What is your business entity type (sole proprietorship, single-member LLC, S-Corp)?"
   - "In what state is your business registered?"
   - "In what state do you physically live and work?"
   - "Do you have an EIN, or are you using your SSN for business?"

2. **Income Sources:**
   - "What is your estimated annual app revenue (gross, before Google's cut)?"
   - "Do you have a W-2 job in addition to app income?"
   - "Do you have any other 1099 income (freelancing, consulting)?"
   - "Does your app earn revenue from in-app purchases, subscriptions, ads, or a combination?"

3. **Current Tax Situation:**
   - "Have you been making quarterly estimated tax payments?"
   - "Do you have a CPA or tax preparer?"
   - "Did you owe a large amount or get a refund last April?"
   - "Are you tracking business expenses separately from personal expenses?"

4. **Expense Profile:**
   - "Do you work from a home office?"
   - "What hardware have you purchased for development (computer, phone, tablet)?"
   - "What software subscriptions do you pay for (IDE, design tools, cloud services)?"
   - "Have you paid any contractors this year?"
   - "Have you attended any conferences or purchased courses?"

---

## Instructions

### CRITICAL: Verification Requirements

1. **Tax rates and thresholds must be flagged as subject to change** — Federal rates, bracket thresholds, and state rules change. Always recommend verifying with IRS.gov or a CPA for the current tax year.
2. **Deductions must be legitimately business-related** — Don't recommend claiming personal expenses as business deductions. The IRS requires that expenses be "ordinary and necessary" for the business.
3. **Quarterly payment calculations must account for ALL income sources** — If the developer has a W-2 job, the withholding from that job offsets the estimated tax obligation. Don't calculate payments in isolation.
4. **State tax guidance must acknowledge complexity** — Multi-state nexus from app store sales is a genuinely complex area. For anything beyond basics, recommend a CPA.
5. **International revenue guidance must be general** — Tax treaties, foreign tax credits, and international reporting requirements are highly specific. This guide covers awareness, not execution.
6. **Acceptable null result:** If the developer's situation involves complex international income, multi-member entities, significant revenue ($500K+), or S-Corp considerations, the right answer is "you need a CPA for this specific situation" rather than a DIY calculation.

### False-Positive Prevention

- Do NOT recommend aggressive deductions that would not survive an audit — the "I use my phone 100% for business" claim is almost never true
- Do NOT suggest that an LLC changes your tax obligations — a single-member LLC is taxed identically to a sole proprietorship unless you elect otherwise
- Do NOT imply that quarterly payments are optional — they are required if you expect to owe $1,000 or more in taxes
- Do NOT calculate state obligations for all 50 states — focus on the developer's home state and flag multi-state nexus as a CPA conversation
- Do NOT treat gross revenue as taxable income — taxable income is net profit (revenue minus deductions)
- Do NOT recommend tax strategies that require an S-Corp without explaining the overhead costs
- DO explain why self-employment tax exists (you pay both the employee AND employer share of Social Security/Medicare)
- DO emphasize that good record-keeping is the foundation of every tax strategy
- DO recommend a CPA for situations that exceed the scope of this guide
- DO distinguish between tax avoidance (legal, encouraged) and tax evasion (illegal)

---

### Phase 1: Income Classification

#### 1.1 How App Revenue Is Taxed

When you earn money from your Android app, the IRS sees it as self-employment income. This is true whether you're a sole proprietor or a single-member LLC (unless you've elected S-Corp treatment). Here's what that means in practical terms:

| Tax Type | Rate | What It Covers | Who Pays It |
|----------|------|---------------|-------------|
| **Self-Employment Tax** | 15.3% | Social Security (12.4%) + Medicare (2.9%) | You — both halves |
| **Federal Income Tax** | 10-37% | Federal income tax on your bracket | You |
| **State Income Tax** | 0-13.3% | Varies by state (some states have 0%) | You |

**Why self-employment tax feels harsh:** When you're employed by a company, your employer pays half of Social Security and Medicare (7.65%) and you pay the other half (7.65%). When you're self-employed, you pay BOTH halves — the full 15.3%. This is the single biggest tax surprise for new solo developers.

**The silver lining:** You can deduct the employer-equivalent portion (half of self-employment tax, roughly 7.65%) from your adjusted gross income. This is an "above the line" deduction, meaning you get it even if you take the standard deduction.

#### 1.2 Revenue Flow Understanding

Your app revenue goes through several stages before it becomes taxable income:

```
Gross App Revenue (what users pay)
  - Google Play Commission (15% of first $1M annually)
  = Net Revenue (what Google deposits in your bank)
  - Business Expenses (deductible costs)
  = Net Profit (Schedule C, Line 31)
  - Self-Employment Tax Deduction (50% of SE tax)
  - Other Above-the-Line Deductions
  = Adjusted Gross Income (for income tax calculation)
  - Standard or Itemized Deductions
  - QBI Deduction (if eligible)
  = Taxable Income
```

**Key insight:** You are taxed on NET PROFIT, not gross revenue. Every legitimate deduction reduces both your income tax AND your self-employment tax. A $100 deduction saves you roughly $30-45 in taxes depending on your bracket.

#### 1.3 If You Also Have a W-2 Job

Many solo developers have a day job. Your app income is ADDED to your employment income for income tax purposes. This means your app income is taxed at your marginal rate (the top of your bracket), not starting from zero.

**Example:**
- W-2 salary: $80,000/year
- App net profit: $20,000/year
- Total income: $100,000/year
- The $20,000 from the app is taxed at the 22% bracket (not starting at 10%)
- Plus 15.3% self-employment tax on the $20,000

**Effective tax rate on the app income:** Roughly 37.3% (22% income + 15.3% SE tax) before state taxes. This is why quarterly estimated payments matter — your W-2 withholding doesn't cover this additional tax.

---

### Phase 2: Deduction Inventory

#### 2.1 Direct Business Expenses (100% Deductible)

These expenses exist solely because of your app business. They are fully deductible.

**Software and Subscriptions:**

| Expense | Typical Annual Cost | Notes |
|---------|-------------------|-------|
| Android Studio / IDE | $0 (free) | Not deductible since it's free |
| JetBrains IDE license | $149-$249/year | If you use it for app development |
| Figma / design tools | $0-$144/year | Pro plans for app design |
| Firebase (Blaze plan) | $0-$600+/year | Cloud hosting for your app |
| Google Cloud Platform | $0-$1,200+/year | Backend services |
| AWS / Azure services | $0-$1,200+/year | Alternative cloud providers |
| GitHub Pro | $48/year | Code repository |
| Domain name | $12-$50/year | Your app's website |
| Analytics tools | $0-$300/year | Mixpanel, Amplitude, etc. |
| Email service | $0-$240/year | For transactional or marketing emails |
| App Store fee | $25 (one-time) | Google Play developer registration |
| Privacy policy generator | $0-$100/year | Legal compliance tools |
| Crash reporting | $0-$300/year | If beyond Firebase's free tier |
| CI/CD service | $0-$600/year | Bitrise, GitHub Actions, etc. |
| Stock photos / icons | $0-$200/year | Assets for your app |
| VPN (for testing) | $60-$120/year | Testing app behavior in different regions |

**Hardware (see Section 2.3 for depreciation rules):**

| Item | Typical Cost | Deduction Method |
|------|-------------|-----------------|
| Development computer | $1,000-$3,500 | Section 179 or depreciation |
| Android test devices | $200-$1,000 | Section 179 (phones, tablets) |
| Monitor(s) | $200-$800 | Section 179 or depreciation |
| Keyboard, mouse, accessories | $50-$300 | Expense in year purchased |
| Desk, chair (home office) | $200-$1,500 | Section 179 or depreciation |

**Services:**

| Expense | Typical Annual Cost | Notes |
|---------|-------------------|-------|
| CPA / tax preparation | $300-$2,000/year | Yes, tax prep fees are deductible |
| Legal services | $0-$1,000/year | Contracts, terms of service |
| Contractor payments | Varies | Fully deductible (see contractor management guide) |
| Business insurance | $300-$1,000/year | If applicable |
| Registered agent service | $50-$300/year | If you have an LLC |

**Professional Development:**

| Expense | Typical Cost | Notes |
|---------|-------------|-------|
| Technical courses (Udemy, Coursera) | $0-$500/year | Must relate to your business |
| Books and publications | $50-$300/year | Technical and business books |
| Conference attendance | $200-$2,000/event | Ticket + travel (see 2.2) |
| Professional memberships | $0-$500/year | Developer communities, associations |

#### 2.2 Travel and Conference Expenses

If you attend conferences, meetups, or travel for business, these costs are deductible:

- **Transportation:** Flights, train tickets, rideshares to/from business events
- **Lodging:** Hotel for business travel (reasonable, not luxury)
- **Meals during business travel:** 50% deductible (this is a common audit trigger — keep receipts and document the business purpose)
- **Conference registration fees:** Fully deductible
- **Internet and phone during business travel:** Deductible for the business-use portion

**Important:** Purely personal travel is never deductible. If you extend a business trip for vacation days, only the business days and business-related expenses qualify.

#### 2.3 Home Office Deduction

If you work from home (and most solo developers do), you have two options:

**Option A: Simplified Method**
- $5 per square foot of dedicated office space
- Maximum 300 square feet = $1,500 maximum deduction
- No tracking of actual home expenses required
- Best for: Developers who want simplicity

**Option B: Regular Method**
- Calculate the percentage of your home used exclusively for business
- Apply that percentage to: rent/mortgage interest, utilities, insurance, repairs, depreciation
- Requires detailed record-keeping
- Best for: Developers with expensive housing or large dedicated office space

| Factor | Simplified Method | Regular Method |
|--------|------------------|----------------|
| Max deduction | $1,500 | No cap (limited to business income) |
| Record-keeping | Minimal | Detailed |
| Calculation | Square footage x $5 | Percentage of actual expenses |
| Risk of audit | Lower | Higher (but legitimate) |
| Home depreciation | Not calculated | Required (affects home sale later) |

**The "exclusive use" requirement:** Your home office space must be used REGULARLY and EXCLUSIVELY for business. A desk in the corner of your bedroom technically qualifies if that area is dedicated to work. Your couch where you sometimes code does not qualify.

#### 2.4 Mixed-Use Assets

Some expenses serve both personal and business purposes. You can deduct the business-use percentage:

| Asset | Typical Business-Use % | How to Determine |
|-------|----------------------|-----------------|
| Internet service | 30-60% | Estimate business vs. personal hours |
| Cell phone | 30-70% | Track business vs. personal usage |
| Computer (if also personal) | 50-80% | Reasonable estimate based on usage |
| Vehicle (if used for business) | Varies | Mileage log required |

**Critical rule:** Be honest about these percentages. Claiming 100% business use of your cell phone when you also use it for personal calls, texts, and social media is a red flag. A reasonable estimate (say 50-60%) is defensible; 100% almost never is.

#### 2.5 Master Deduction Checklist

Use this checklist at year-end to ensure you haven't missed anything:

```markdown
## Annual Deduction Inventory

### Direct Business Expenses
- [ ] Cloud hosting (Firebase, AWS, GCP): $________
- [ ] Software subscriptions (IDE, design, analytics): $________
- [ ] App store fees: $________
- [ ] Domain names and web hosting: $________
- [ ] Contractor payments: $________
- [ ] Legal and accounting fees: $________
- [ ] Business insurance: $________
- [ ] Business bank account fees: $________
- [ ] Payment processing fees (beyond Google's cut): $________

### Hardware and Equipment
- [ ] Computer / laptop: $________
- [ ] Test devices (phones, tablets): $________
- [ ] Monitors and peripherals: $________
- [ ] Office furniture (if new this year): $________

### Home Office
- [ ] Method chosen: [Simplified / Regular]
- [ ] Square footage (simplified): ________ sq ft x $5 = $________
- [ ] OR percentage of home (regular): ________% of home expenses = $________

### Mixed-Use (Business Portion Only)
- [ ] Internet service: $________ x ________% = $________
- [ ] Cell phone: $________ x ________% = $________
- [ ] Computer (if mixed use): $________ x ________% = $________

### Professional Development
- [ ] Courses and training: $________
- [ ] Books and publications: $________
- [ ] Conference registration: $________
- [ ] Conference travel: $________

### Other
- [ ] Business travel (non-conference): $________
- [ ] Business meals (50%): $________
- [ ] Marketing and advertising: $________
- [ ] Registered agent fee: $________
- [ ] State filing fees and annual reports: $________

### TOTAL DEDUCTIONS: $________

### Tax Impact Estimate
- [ ] SE tax savings (TOTAL x 15.3%): $________
- [ ] Income tax savings (TOTAL x marginal rate): $________
- [ ] Total estimated tax savings: $________
```

---

### Phase 3: Quarterly Estimated Payments

#### 3.1 Why Quarterly Payments Exist

The U.S. tax system is "pay as you go." Employees have taxes withheld from every paycheck. Self-employed people don't have anyone withholding for them, so the IRS requires quarterly estimated payments. If you don't make these payments, you'll owe a penalty — even if you pay the full amount on April 15.

**You must make quarterly payments if:**
- You expect to owe $1,000 or more in taxes for the year, AND
- Your W-2 withholding (if any) won't cover at least 90% of this year's tax OR 100% of last year's tax

#### 3.2 The Tax Calendar

| Date | What's Due | Form | Notes |
|------|-----------|------|-------|
| **January 15** | Q4 estimated payment (prior year) | 1040-ES | For income earned Oct-Dec |
| **January 31** | Send 1099-NEC to contractors | 1099-NEC | If you paid any contractor $600+ |
| **March 15** | S-Corp return due (if applicable) | 1120-S | Only if you elected S-Corp |
| **April 15** | Annual tax return + Q1 estimated payment | 1040 + 1040-ES | File return OR extension + pay Q1 |
| **April 15** | Annual report (some states) | Varies | Check your state's schedule |
| **June 15** | Q2 estimated payment | 1040-ES | For income earned Apr-May |
| **September 15** | Q3 estimated payment | 1040-ES | For income earned Jun-Aug |
| **October 15** | Extended return due (if you filed extension) | 1040 | Only if you filed for extension in April |

**Set calendar reminders** for each of these dates, at least 2 weeks in advance. Missing a quarterly payment by even one day triggers a penalty.

#### 3.3 Estimated Payment Calculator

There are two safe harbor methods to avoid underpayment penalties:

**Method 1: Current-Year Method (90% of current year's tax)**
```
Estimated annual net profit:                       $________
× Self-employment tax rate (15.3%):                $________  (A)
× 50% (deductible half of SE tax):                 $________
Adjusted net profit (for income tax):              $________
× Marginal income tax rate:                        $________  (B)
× State income tax rate:                           $________  (C)
Total estimated tax (A + B + C):                   $________
× 90%:                                             $________
- W-2 withholding (if applicable):                 $________
= Total estimated payments needed:                 $________
÷ 4 quarters:                                      $________  per quarter
```

**Method 2: Prior-Year Method (100% of last year's tax)**
```
Total tax from last year's return (Form 1040, Line 24):  $________
+ Self-employment tax (Schedule SE):                      $________
= Total prior year tax:                                   $________
× 100% (or 110% if AGI > $150,000):                      $________
- W-2 withholding (if applicable):                        $________
= Total estimated payments needed:                        $________
÷ 4 quarters:                                             $________  per quarter
```

**Which method to use:**
- If your income is **growing**: Use Method 2 (prior-year). You'll pay based on last year's (lower) income and settle up in April.
- If your income is **stable**: Either method works. Method 1 is more precise.
- If your income is **declining**: Use Method 1 (current-year) to avoid overpaying.

**Pro tip:** If your income varies significantly quarter to quarter, you can use the "annualized income installment method" (Form 2210, Schedule AI) to adjust each quarter's payment. This is complex — your CPA can help.

#### 3.4 Payment Logistics

**How to pay:**
- **IRS Direct Pay** (irs.gov/payments) — free, pay from bank account
- **EFTPS** (Electronic Federal Tax Payment System) — free, requires enrollment
- **Credit/debit card** — convenience fee applies (1.87-1.99% for credit cards)

**State payments:** Each state has its own payment system. Check your state's department of revenue website.

**Record-keeping:** Save confirmation numbers for every payment. If the IRS claims you didn't pay, you need proof.

---

### Phase 4: State Tax Considerations

#### 4.1 Your Home State

You owe state income tax (if your state has one) on ALL of your income, including app revenue. This is straightforward — you file in the state where you live.

**States with no income tax (as of 2025):** Alaska, Florida, Nevada, New Hampshire (dividends/interest only), South Dakota, Tennessee, Texas, Washington, Wyoming.

**If you live in one of these states,** you still owe federal self-employment tax and federal income tax. You just skip the state income tax part of the calculation.

#### 4.2 Multi-State Nexus from App Sales

This is where things get complex. When your app is sold in the Google Play Store, users in all 50 states can buy it. Does that create a tax obligation in every state?

**The short answer:** It depends on the state and the type of tax.

**Sales Tax Nexus:**
- Most states exempt digital goods (apps, in-app purchases) from sales tax
- Some states DO tax digital goods (currently ~25 states)
- Google may collect and remit sales tax on your behalf through the Play Store ("marketplace facilitator" laws)
- In most cases, Google handles this for you, but verify for your specific situation

**Income Tax Nexus:**
- Selling an app into a state generally does NOT create income tax nexus by itself
- Physical presence (office, employees, inventory) typically does create nexus
- The Supreme Court's Wayfair decision (2018) expanded economic nexus for sales tax, but income tax nexus rules vary
- If you're a solo developer working from one state, you almost certainly owe income tax only to that state

**Practical guidance for solo developers:**
1. File income tax in your home state only (unless you have physical presence elsewhere)
2. Verify whether Google is collecting sales tax on your behalf
3. If you earn more than $100K in app revenue, consult a CPA about multi-state obligations
4. Keep records of where revenue comes from (Google Play Console provides this data)

#### 4.3 State-Specific Gotchas

| State | Issue | Impact |
|-------|-------|--------|
| **California** | $800 minimum franchise tax for LLCs | Owed even if you earn $0 |
| **New York** | City tax on top of state tax | Can add 3-4% |
| **Washington** | B&O tax instead of income tax | Tax on gross revenue, not profit |
| **Texas** | No income tax but franchise tax for larger businesses | Usually doesn't apply to solo developers under $1.23M |
| **Ohio** | Commercial Activity Tax (CAT) | Tax on gross receipts over $150K |
| **Illinois** | Replacement tax on some entities | May apply to S-Corps |

---

### Phase 5: Advanced Tax Topics

#### 5.1 Section 199A — Qualified Business Income (QBI) Deduction

The QBI deduction allows eligible self-employed individuals to deduct up to 20% of their qualified business income from a pass-through entity (sole proprietorship, LLC, S-Corp).

**In plain language:** If your app earns $50,000 in net profit, you may be able to deduct $10,000 from your taxable income. That's a real tax cut.

**Eligibility basics:**
- You must have qualified business income from a pass-through entity
- Your total taxable income must be below certain thresholds for the full deduction
  - Single: ~$191,950 (2025, adjusted annually for inflation)
  - Married filing jointly: ~$383,900
- Above these thresholds, the deduction phases out for "specified service trades or businesses" (SSTBs)

**Is software development an SSTB?** This is a gray area. The IRS defines SSTBs to include consulting, but pure product development (building and selling an app) is generally NOT considered consulting. If your app revenue is from selling a product (subscriptions, in-app purchases), you're likely eligible. If your income is from custom consulting, it may be an SSTB.

**Impact example:**
```
Net app profit:           $60,000
QBI deduction (20%):      $12,000
Tax savings (22% bracket): $2,640
```

**This is free money.** Make sure your CPA applies it.

#### 5.2 International Revenue Considerations

If your app is available globally, you're earning revenue from international sources:

**What Google handles for you:**
- Google collects payment from international users in their local currency
- Google converts to USD and deposits to your U.S. bank account
- Google may withhold taxes required by other countries (tax treaties affect this)
- Google provides tax forms (1042-S) for any foreign tax withheld

**What you need to handle:**
- **Report all income:** International revenue deposited to your account is part of your total income. No special reporting needed since Google already converted it to USD.
- **Foreign tax credit:** If Google withheld taxes for other countries, you may be able to claim a foreign tax credit (Form 1116) to avoid being taxed twice on the same income.
- **FBAR/FATCA:** Only relevant if you have foreign bank accounts. If all your money goes through Google to your U.S. bank, this doesn't apply.

**Practical for most solo developers:** International revenue just shows up as part of your total Google Play deposits. You report it as regular income. If you see foreign tax withholding on your Google statements, tell your CPA so they can claim the credit.

#### 5.3 Year-End Tax Planning Moves

Before December 31 each year, consider these strategies:

**Accelerate deductions (if you want to reduce THIS year's taxes):**
- Buy equipment you need in December instead of January
- Pre-pay January subscriptions in December
- Pay contractor invoices before year-end
- Make any planned business purchases now

**Defer income (if you expect lower income next year):**
- This is difficult with app revenue since Google pays on a fixed schedule
- If you do consulting on the side, you could delay invoicing until January

**Retirement contributions:**
- **SEP-IRA:** Contribute up to 25% of net self-employment income (max ~$69,000 for 2025)
- **Solo 401(k):** Even more generous limits with employee + employer contributions
- Contributions reduce your taxable income dollar for dollar
- Deadline: April 15 (or October 15 with extension) for SEP-IRA; December 31 for Solo 401(k) employee contributions

**Health insurance deduction:**
- If you're self-employed and pay for your own health insurance, the premiums are deductible (above the line)
- This includes medical, dental, and vision for you, your spouse, and dependents
- Cannot exceed your net self-employment income

#### 5.4 Retirement Account Comparison for Solo Developers

| Feature | SEP-IRA | Solo 401(k) | Roth IRA |
|---------|---------|-------------|----------|
| **Max contribution** | 25% of net SE income (up to ~$69K) | $23,500 employee + 25% employer (up to ~$69K total) | $7,000/year |
| **Tax benefit** | Deduct now, taxed on withdrawal | Traditional: same as SEP. Roth option available. | No deduction now, tax-free withdrawal |
| **Setup complexity** | Low | Moderate | Low |
| **Deadline** | Tax filing deadline | Dec 31 (employee portion) | Tax filing deadline |
| **Best for** | Simple, high income | Maximizing contributions | Lower income, long time horizon |

---

### Phase 6: Record-Keeping System

#### 6.1 What to Keep and For How Long

| Document | Retention Period | Format |
|----------|-----------------|--------|
| Tax returns | 7 years minimum | PDF + paper |
| Receipts for deductions | 7 years | Digital scans OK |
| Bank and credit card statements | 7 years | PDF downloads |
| Contractor invoices and 1099s | 7 years | PDF |
| Google Play earnings reports | 7 years | Download monthly |
| Quarterly payment confirmations | 7 years | Screenshot / PDF |
| Home office measurements | While claiming deduction | Notes + photos |

#### 6.2 Monthly Tax Maintenance (15 Minutes)

```markdown
## Monthly Tax Maintenance Checklist

1. [ ] Download Google Play earnings report for the month
2. [ ] Categorize all business expenses in accounting software
3. [ ] Scan and save any paper receipts
4. [ ] Check year-to-date profit vs. estimated payment calculations
5. [ ] Set aside tax reserve (30% of net profit) into tax savings account
6. [ ] Note any large upcoming expenses (for year-end planning)
```

#### 6.3 Accounting Software Recommendations

| Tool | Cost | Best For | Notes |
|------|------|----------|-------|
| **Wave** | Free | Budget-conscious developers | Free invoicing and accounting |
| **QuickBooks Self-Employed** | $15/month | Most solo developers | Automatic expense categorization |
| **QuickBooks Simple Start** | $30/month | Developers with contractors | Full accounting features |
| **FreshBooks** | $17/month | Developers who invoice clients | Strong invoicing focus |
| **Spreadsheet** | Free | Minimalists | Works if you're disciplined |

---

## Expected Output

```markdown
# Tax Strategy: [App Name / Business Name]

## Tax Profile
- Entity type: [Sole Prop / LLC / S-Corp]
- Home state: [State]
- Filing status: [Single / MFJ / etc.]
- W-2 income (if any): $[amount]
- Estimated app net profit: $[amount]
- Marginal federal tax bracket: [%]
- State income tax rate: [%]

## Estimated Annual Tax Obligation

| Tax Type | Amount |
|----------|--------|
| Self-employment tax (15.3% of net profit) | $[amount] |
| Federal income tax (marginal rate) | $[amount] |
| State income tax | $[amount] |
| **Total estimated tax** | **$[amount]** |
| Less: W-2 withholding | ($[amount]) |
| **Net estimated payments needed** | **$[amount]** |

## Quarterly Payment Schedule

| Due Date | Amount | Payment Method |
|----------|--------|---------------|
| April 15 | $[amount] | IRS Direct Pay |
| June 15 | $[amount] | IRS Direct Pay |
| September 15 | $[amount] | IRS Direct Pay |
| January 15 | $[amount] | IRS Direct Pay |

## Deduction Summary

| Category | Estimated Annual Amount |
|----------|----------------------|
| Software/subscriptions | $[amount] |
| Hardware (Section 179) | $[amount] |
| Home office | $[amount] |
| Mixed-use (business %) | $[amount] |
| Professional development | $[amount] |
| Professional services (CPA, legal) | $[amount] |
| Contractor payments | $[amount] |
| Other business expenses | $[amount] |
| **Total deductions** | **$[amount]** |
| **Estimated tax savings from deductions** | **$[amount]** |

## Tax Calendar

| Date | Action | Notes |
|------|--------|-------|
| Monthly | Categorize expenses, save receipts | 15-minute task |
| [Q dates] | Pay quarterly estimates | $[amount] each |
| Dec 31 | Year-end planning, accelerate deductions | Review with CPA |
| Jan 31 | Send 1099s to contractors (if any) | Required if $600+ |
| Apr 15 | File return or extension | Annual return |

## Action Items
- [ ] Set up accounting software: [tool]
- [ ] Open tax reserve savings account
- [ ] Schedule CPA consultation
- [ ] Set calendar reminders for quarterly payments
- [ ] Complete deduction inventory for current year
- [ ] Evaluate retirement account options (SEP-IRA / Solo 401(k))

## ⚠️ Consult a CPA For:
- [List specific items in your situation that require professional guidance]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on tax planning decisions specific to solo app developers
- **ST-02** (Structured Sequential Instructions) — Phased approach from income classification through year-end planning
- **RT-02** (Multi-Dimensional Analysis) — Analyzing tax obligations across federal, state, self-employment, and deduction dimensions
- **CM-01** (Explicit Context Framing) — Solo developer constraints: self-employment, variable income, home office, mixed-use assets
- **DS-06** (Prioritization Guidance) — Deductions ordered by impact and accessibility

---

## Related Prompts

- `solo_dev_business_formation.md` — Entity decisions that determine how you're taxed (sole prop vs. LLC vs. S-Corp)
- `solo_dev_financial_planning.md` — Financial planning including tax set-aside and burn rate calculations
- `solo_dev_contractor_management.md` — 1099 requirements when you pay contractors
- `solo_dev_weekly_operating_rhythm.md` — Include monthly tax maintenance in your operating rhythm
- `monetization_model_selector.md` — Revenue model decisions that affect tax treatment

---

## Customization Guide

- **For developers with a W-2 job:** Your W-2 withholding offsets some of your estimated payment obligation. Ask your employer to increase withholding (via W-4) as an alternative to making separate quarterly payments. Some developers find this simpler than writing quarterly checks.
- **For developers in no-income-tax states (TX, FL, WA, etc.):** Skip Phase 4 state considerations, but remember that Washington has a B&O tax on gross revenue. Your tax calculation is simpler, but federal obligations remain the same.
- **For developers earning under $5K/year from their app:** Your tax obligation may be small enough to handle on your annual return without quarterly payments, especially if your W-2 withholding covers the difference. Still track deductions — they reduce your tax to potentially zero on the app income.
- **For developers considering S-Corp election:** S-Corp can save significant self-employment tax when net profit exceeds $50K-$80K/year, because you only pay SE tax on your "reasonable salary" rather than all profit. But it adds $2K-$5K/year in accounting and payroll costs. Do the math with your CPA before electing.
- **For developers with international users but no international bank accounts:** Your situation is simpler than you think. Google handles currency conversion and foreign tax withholding. Just make sure your CPA knows about any foreign tax withholding so they can claim the credit.
- **For developers who haven't been paying quarterly estimates:** Don't panic. File your annual return, pay what you owe, and start making quarterly payments going forward. The underpayment penalty is an interest charge, not a crime. Your CPA can calculate the penalty and often minimize it.
