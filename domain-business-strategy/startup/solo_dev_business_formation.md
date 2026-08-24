---
title: "Solo Developer Business Formation Guide"
category: startup/business-operations
description: "Guide a solo app developer through business entity decisions — LLC vs sole proprietorship vs S-Corp, state selection, registered agent, EIN, bank accounts — with a step-by-step formation checklist and cost breakdown"
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
  - business-formation
  - llc
  - legal
  - android
  - entity-selection
updated: "2026-02-11"
---

# Solo Developer Business Formation Guide

**Objective:** Walk a solo app developer through the complete process of forming a legal business entity — from choosing between sole proprietorship, LLC, and S-Corp, to selecting a state of formation, obtaining an EIN, opening a business bank account, and setting up the ongoing compliance calendar — producing a concrete action plan with cost estimates and a timeline.

**When to Use:** Use this prompt when you are earning (or about to earn) revenue from your Android app and need to formalize your business structure. Also use it when you want liability protection, need a business bank account for payment processing, or when your accountant says "you should probably form an LLC." This is a foundational decision that affects your taxes, liability, and operational overhead for years.

**Important context:** Most solo developers delay this decision because it feels intimidating and expensive. The truth is that forming a business entity is straightforward, costs between $50-$500 in most states, and can be done in a single afternoon. The hard part is choosing the RIGHT entity — and that depends on your revenue, risk profile, and growth plans. This guide explains the options in plain language so you can make an informed decision, then gives you the exact steps to execute it.

**Disclaimer:** This guide provides general educational information about business formation. It is NOT legal or tax advice. Laws vary by state and change frequently. Consult a licensed attorney and CPA in your state before making entity decisions, especially if you have significant revenue, partners, or complex tax situations.

---

## Context Gathering

Before choosing a business entity, understand your situation:

1. **Revenue and Financial Status:**
   - "How much app revenue are you currently earning per month?"
   - "Do you have other income sources (day job, freelancing)?"
   - "What is your total annual income from all sources?"
   - "Do you have savings to cover formation and maintenance costs?"

2. **Risk Profile:**
   - "Does your app collect personal user data (names, emails, location, health data)?"
   - "Does your app process payments or handle financial information?"
   - "Could your app cause harm if it malfunctions (health apps, navigation, financial tools)?"
   - "Are you using third-party APIs that could expose you to liability?"

3. **Location and Plans:**
   - "What state do you live in?"
   - "Do you plan to stay in this state long-term?"
   - "Do you plan to bring on a co-founder or investors in the next 1-2 years?"
   - "Are you planning to keep this as a side project or go full-time?"

4. **Current Business Status:**
   - "Have you already been earning revenue without a formal entity?"
   - "Do you have a business bank account?"
   - "Have you been tracking income and expenses?"
   - "Have you filed any business tax returns?"

---

## Instructions

### CRITICAL: Verification Requirements

1. **Entity recommendation must match the developer's actual revenue level** — Don't recommend S-Corp election for someone earning $2K/year. The accounting costs alone would exceed the tax savings.
2. **State-specific information must be flagged as requiring verification** — Filing fees, annual report requirements, and tax rates change. Always recommend verifying with the Secretary of State website.
3. **Cost estimates must include ALL ongoing costs, not just formation fees** — Annual reports, registered agent fees, state franchise taxes, and accounting costs add up. Show the full picture.
4. **Tax implications must include the "consult a CPA" disclaimer** — General guidance is fine; specific tax advice requires a licensed professional.
5. **Timeline must be realistic** — Some states process in 24 hours; others take 4-6 weeks. Don't promise instant formation everywhere.
6. **Acceptable null result:** If the developer's situation is complex (multiple states, co-founders, investors, significant revenue), the right answer may be "you need a lawyer for this specific situation" rather than a DIY guide.

### False-Positive Prevention

- ❌ Do NOT recommend an S-Corp for someone earning under $50K/year from the app — the accounting overhead typically exceeds the tax savings
- ❌ Do NOT suggest incorporating in Delaware or Wyoming "because everyone does" without explaining the cost of foreign qualification in the developer's home state
- ❌ Do NOT imply that an LLC makes you completely immune from lawsuits — it limits liability but doesn't eliminate it
- ❌ Do NOT skip ongoing compliance requirements — formation is step one; maintenance is ongoing
- ❌ Do NOT recommend the cheapest option without explaining what you give up
- ✅ DO explain WHY each entity type matters in plain language
- ✅ DO include the full annual cost of each option, not just the filing fee
- ✅ DO recommend forming in the developer's home state unless there's a specific reason not to
- ✅ DO explain the concept of "piercing the corporate veil" — an LLC only protects you if you treat it like a real business
- ✅ DO acknowledge that many successful solo developers operate as sole proprietors for years without issues

---

### Phase 1: Understanding Your Options

#### 1.1 Entity Comparison Matrix

| Factor | Sole Proprietorship | Single-Member LLC | S-Corp (LLC + S Election) |
|--------|-------------------|-------------------|--------------------------|
| **What it is** | You and the business are the same legal entity | A separate legal entity that you own | An LLC that elects special tax treatment |
| **Formation cost** | $0 (it's the default) | $50-$500 (varies by state) | $50-$500 + $500-$2,000/yr accounting |
| **Annual maintenance** | $0-$50 (business license) | $0-$800/yr (varies by state) | $1,500-$5,000/yr (payroll + accounting) |
| **Liability protection** | None — your personal assets are exposed | Yes — personal assets generally protected | Yes — same as LLC |
| **Tax filing** | Schedule C on personal return | Schedule C on personal return (single-member) | S-Corp return (Form 1120-S) + W-2 to yourself |
| **Self-employment tax** | 15.3% on all profit | 15.3% on all profit | 15.3% only on your "reasonable salary" |
| **Complexity** | Minimal | Low | Moderate to high |
| **Best for revenue range** | $0-$10K/year | $1K-$80K/year | $80K+/year (when tax savings > accounting costs) |
| **Credibility/perception** | Informal | Professional | Professional |

#### 1.2 What "Liability Protection" Actually Means

This is the #1 reason developers form an LLC, so let's be precise about what it does and doesn't do:

**What an LLC protects against:**
- A user sues because your app lost their data → they can go after the LLC's assets (business bank account, equipment) but generally NOT your personal savings, home, or car
- A contractor claims you owe them money → same protection applies
- Business debts → if the LLC owes money, creditors generally can't come after your personal assets

**What an LLC does NOT protect against:**
- Your own negligence or fraud → if YOU personally did something wrong, the LLC won't shield you
- Personal guarantees → if you personally guaranteed a loan or lease, the LLC doesn't help
- "Piercing the corporate veil" → if you mix personal and business finances, courts can treat the LLC as if it doesn't exist

**The "piercing" risk is real for solo developers.** Courts can disregard your LLC if you:
- Use the business bank account for personal expenses
- Don't maintain separate business records
- Don't have an operating agreement
- Treat the LLC as a formality rather than a real business

**Bottom line:** An LLC is worth it if you maintain the separation. If you're going to dump everything into one checking account, the LLC provides less protection than you think.

#### 1.3 When to Form Each Entity Type

**Stay as sole proprietor when:**
- Revenue is under $5K/year
- Your app doesn't handle sensitive data
- You're still validating the idea
- You want zero overhead
- You're comfortable with personal liability

**Form an LLC when:**
- Revenue exceeds $5K/year (or is growing toward it)
- Your app handles user data of any kind
- You want to separate business and personal finances
- You're signing contracts with other businesses
- You want to look professional (business bank account, business name on invoices)
- You plan to go full-time eventually

**Elect S-Corp treatment when:**
- Net profit (after expenses) consistently exceeds $50K-$80K/year
- You've done the math: S-Corp tax savings > accounting costs
- You're comfortable with payroll complexity (or willing to pay for it)
- You have a CPA who can handle the additional filings

---

### Phase 2: State Selection

#### 2.1 The Default Answer: Your Home State

For 95%+ of solo developers, you should form your LLC in the state where you live and work. Here's why:

**Why NOT Delaware/Wyoming/Nevada (despite what you've heard):**

| Scenario | What Actually Happens | Cost |
|----------|---------------------|------|
| Form in Delaware, live in Texas | Must register as "foreign LLC" in Texas too | Delaware fee + Texas fee + registered agent in both states |
| Form in Wyoming, live in California | California still taxes you on all income | Wyoming fee + California fee + California's $800/yr minimum franchise tax |
| Form in Nevada, live in New York | Must still file in New York | Nevada fee + New York fee + registered agent in Nevada |

**When another state IS worth considering:**
- You're planning to raise venture capital (Delaware C-Corp is standard for that — but that's a different entity type entirely)
- Your home state has unusually high formation/maintenance costs AND you don't need to register there as a foreign entity
- You're moving to a different state soon

#### 2.2 State Cost Comparison (Common States)

| State | Filing Fee | Annual Report | Franchise/Annual Tax | Notes |
|-------|-----------|---------------|---------------------|-------|
| California | $70 | $20 (biennial) | $800/year minimum | Expensive. The $800 tax hits even if you earn $0. |
| Texas | $300 | $0 | No state income tax | Higher upfront, lower ongoing |
| Florida | $125 | $138.75/year | No state income tax | Moderate costs |
| New York | $200 | $9 (biennial) | Filing fee, no franchise tax for LLCs | Publication requirement can cost $1,000+ |
| Delaware | $90 | $300/year | $300/year franchise tax | Plus you still pay in your home state |
| Wyoming | $100 | $60/year | No state income tax | Low cost but you likely still register in home state |
| Washington | $200 | $71/year | No state income tax | B&O tax applies instead |
| Colorado | $50 | $10/year | No franchise tax | One of the cheapest |
| Georgia | $100 | $50/year | State income tax applies | Moderate |
| Illinois | $150 | $75/year | Replacement tax on some entities | Moderate |

**Important:** These fees change. Always verify with your state's Secretary of State website before filing.

---

### Phase 3: Step-by-Step Formation

#### 3.1 Pre-Formation Checklist

Before you file anything:

- [ ] **Choose your business name.** Must be unique in your state. Search your state's business name database. The name must include "LLC" or "Limited Liability Company."
- [ ] **Decide on registered agent.** This is the person/company designated to receive legal documents. Options: yourself (free, but your address becomes public record), or a registered agent service ($50-$300/year for privacy).
- [ ] **Draft an operating agreement.** Even for a single-member LLC, you need one. It proves the LLC is a real entity. Templates are available online or from legal services ($0-$100).

#### 3.2 Formation Steps

**Step 1: File Articles of Organization (Day 1)**
- Go to your state's Secretary of State website
- File "Articles of Organization" (some states call it "Certificate of Formation")
- Provide: LLC name, registered agent, organizer name, business address, purpose (usually "any lawful business")
- Pay the filing fee
- Timeline: Some states approve online filings in minutes; others take 1-4 weeks

**Step 2: Get Your EIN (Same Day or Day 2)**
- Go to IRS.gov → "Apply for an EIN"
- Free. Takes 10 minutes online.
- You need this for: bank accounts, tax filings, contractor payments, Google Play developer registration (if using a business account)
- You can apply immediately after filing your Articles of Organization — you don't need to wait for state approval in most cases

**Step 3: Draft Operating Agreement (Day 2-3)**
- Single-member LLC operating agreement covers:
  - Member name and ownership percentage (100%)
  - How profits and losses are allocated (100% to you)
  - Management structure (member-managed)
  - Dissolution process
  - Initial capital contribution
- Keep this in your records. Some states require it; all states benefit from having one.

**Step 4: Open Business Bank Account (Day 3-7)**
- Bring: EIN letter, Articles of Organization, operating agreement, personal ID
- Options: Traditional bank (Chase, Bank of America), online bank (Mercury, Relay, Novo), or credit union
- Minimum features needed: checking account, debit card, ability to accept ACH transfers
- Google and Apple pay app revenue via ACH, so make sure your bank supports incoming ACH

**Step 5: Set Up Business Finances (Day 7-14)**
- Connect bank account to Google Play Console for revenue deposits
- Set up accounting software (Wave — free, or QuickBooks — $30/month)
- Create expense categories: cloud hosting, software subscriptions, contractor payments, equipment, marketing, app store fees
- Set up a system to transfer money FROM business account TO personal account (this is called an "owner's draw" for an LLC)

**Step 6: Obtain Business Licenses (Day 7-30)**
- Check your city and county for business license requirements
- Some cities require a general business license even for online businesses
- Cost: typically $25-$100/year
- Some states require additional registrations for businesses collecting sales tax

**Step 7: Ongoing Compliance Calendar (Set Up Immediately)**

| Task | Frequency | Typical Due Date | Penalty for Missing |
|------|-----------|-----------------|-------------------|
| Annual report | Annual or biennial | Varies by state (check yours) | Late fees, potential administrative dissolution |
| Franchise/annual tax | Annual | Varies (CA: Apr 15, DE: Jun 1) | Late fees + interest |
| Estimated tax payments | Quarterly | Apr 15, Jun 15, Sep 15, Jan 15 | Underpayment penalties |
| Business license renewal | Annual | Varies by city | Fines, inability to operate |
| Registered agent renewal | Annual | Varies by provider | Loss of registered agent, missed legal notices |
| Update business address | As needed | Within 30-60 days of change | Missed legal notices |

---

### Phase 4: Google Play Console Business Account

#### 4.1 Individual vs. Organization Account

If you form an LLC, you should consider switching your Google Play developer account to an "Organization" type:

| Factor | Individual Account | Organization Account |
|--------|-------------------|---------------------|
| Verification | Personal ID | DUNS number + business documents |
| Display name | Your personal name | Your business name |
| Setup time | Minutes | Days to weeks (DUNS verification) |
| Professionalism | Informal | Professional |
| Required for | Personal projects | Apps that handle sensitive data |

**Steps to get a DUNS number (free):**
1. Go to dnb.com and search for your business
2. If not found, request a free DUNS number
3. Takes 5-10 business days (expedited: $229 for 1 day)
4. You need: legal business name, EIN, business address, phone number

**Note:** You cannot convert an Individual account to Organization. You would need to create a new Organization account ($25 fee) and transfer your apps. Consider this before publishing.

#### 4.2 Payment Setup

- Google Play deposits revenue via ACH to your bank account
- Set up your business bank account as the payment recipient in the Play Console
- Payments are made monthly, with a $1 minimum threshold (standard)
- Make sure the name on the bank account matches the name on your Play Console merchant account

---

### Phase 5: Total Cost Breakdown

#### 5.1 First-Year Costs (Typical)

| Item | Sole Proprietorship | LLC (DIY) | LLC (with Legal Service) |
|------|-------------------|-----------|--------------------------|
| State filing fee | $0 | $50-$500 | $50-$500 |
| Legal service fee | $0 | $0 | $100-$300 |
| Registered agent | $0 | $0 (self) or $50-$150 | Often included in service |
| Operating agreement | $0 | $0 (template) | Often included in service |
| EIN | $0 | $0 | $0 |
| Business bank account | $0 | $0 (many are free) | $0 |
| Business license | $25-$100 | $25-$100 | $25-$100 |
| Accounting software | $0 (spreadsheet) | $0-$360 | $0-$360 |
| **Total Year 1** | **$25-$100** | **$75-$1,110** | **$175-$1,260** |

#### 5.2 Annual Ongoing Costs

| Item | Sole Proprietorship | LLC | LLC + S-Corp Election |
|------|-------------------|-----|----------------------|
| Annual report | $0 | $0-$300 | $0-$300 |
| Franchise/annual tax | $0 | $0-$800 | $0-$800 |
| Registered agent | $0 | $0-$150 | $0-$150 |
| Accounting/bookkeeping | $0 | $0-$360 | $1,500-$5,000 |
| Payroll service | $0 | $0 | $500-$1,200 |
| Tax preparation | $0-$200 | $0-$500 | $1,000-$3,000 |
| Business license renewal | $25-$100 | $25-$100 | $25-$100 |
| **Total Annual** | **$25-$300** | **$25-$2,210** | **$3,025-$10,550** |

This is why S-Corp only makes sense at higher revenue levels. You need the tax savings to exceed the $3K-$10K annual overhead.

---

### Phase 6: Common Mistakes

| Mistake | Why It Happens | How to Avoid |
|---------|---------------|--------------|
| **Mixing personal and business finances** | Convenience; "it's just me" | Open a business bank account on Day 1 and use it for ALL business transactions |
| **Forgetting annual report** | Set it and forget it | Add to your calendar immediately with 2-week advance reminder |
| **No operating agreement** | "I'm the only member, why bother?" | Courts look for this. Spend 30 minutes creating one. |
| **Incorporating in Delaware for no reason** | "I read online that Delaware is best" | That advice is for funded startups, not solo developers. Form in your home state. |
| **Rushing to S-Corp** | "I'll save on taxes!" | Do the math first. Under $50K net profit, you'll likely pay MORE in accounting than you save in taxes. |
| **Not tracking expenses from Day 1** | "I'll catch up later" | You won't. Set up tracking now, even if it's a spreadsheet. |
| **Using personal credit card for business** | Card was already saved in AWS/Firebase | Get a business card or use the business debit card. Keep the paper trail clean. |
| **Ignoring state nexus** | "I'm just an app developer" | If you sell to customers in states with sales tax, you may have nexus obligations. Talk to a CPA. |

---

## Expected Output

```markdown
# Business Formation Plan: [App Name / Business Name]

## Entity Decision
- **Chosen entity:** [Sole Proprietorship / LLC / LLC + S-Corp]
- **Reasoning:** [Why this entity fits your situation]
- **State of formation:** [Your state]
- **Estimated first-year cost:** $[amount]
- **Estimated annual ongoing cost:** $[amount]

## Formation Checklist

### Week 1
- [ ] Search for business name availability in [state]
- [ ] Choose registered agent: [self / service name]
- [ ] File Articles of Organization with [state] Secretary of State
- [ ] Apply for EIN on IRS.gov
- [ ] Draft single-member operating agreement

### Week 2
- [ ] Open business bank account at [bank name]
- [ ] Set up accounting: [Wave / QuickBooks / spreadsheet]
- [ ] Update Google Play Console payment information
- [ ] Check city/county business license requirements

### Week 3-4
- [ ] File for business license if required
- [ ] Set up expense tracking categories
- [ ] Create compliance calendar (see below)
- [ ] Consider Google Play Organization account (DUNS number)

## Compliance Calendar

| Date | Task | Notes |
|------|------|-------|
| [Month] | Annual report due | File with [state] SOS |
| Apr 15 | Q1 estimated taxes | Federal + state if applicable |
| Jun 15 | Q2 estimated taxes | Federal + state if applicable |
| Sep 15 | Q3 estimated taxes | Federal + state if applicable |
| Jan 15 | Q4 estimated taxes | Federal + state if applicable |
| [Month] | Business license renewal | [City/county] |
| [Month] | Registered agent renewal | If using a service |

## Financial Separation Rules
1. ALL app revenue deposits to business bank account
2. ALL business expenses paid from business account or business card
3. Transfer personal income via owner's draw (document each transfer)
4. Keep receipts for all business expenses
5. Never pay personal expenses from business account

## Next Steps
- [ ] Review with CPA for tax implications specific to your situation
- [ ] Consider umbrella insurance for additional liability protection
- [ ] Revisit entity choice when revenue exceeds $50K/year (S-Corp evaluation)
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on the specific entity decision and formation process
- **ST-02** (Structured Sequential Instructions) — Step-by-step formation process with timeline
- **RT-02** (Multi-Dimensional Analysis) — Entity comparison across cost, liability, tax, and complexity dimensions
- **CM-01** (Explicit Context Framing) — Solo developer constraints, revenue ranges, and risk profiles
- **DS-06** (Prioritization Guidance) — Clear thresholds for when each entity type makes sense

---

## Related Prompts

- `solo_dev_financial_planning.md` — Financial planning after entity formation
- `solo_dev_tax_strategy.md` — Tax planning for app revenue including quarterly estimated payments
- `solo_dev_contractor_management.md` — Hiring contractors under your new business entity
- `solo_dev_weekly_operating_rhythm.md` — Include compliance tasks in your weekly rhythm
- `monetization_model_selector.md` — Revenue model decisions that affect entity choice

---

## Customization Guide

- **For developers with a co-founder:** Multi-member LLC changes the operating agreement significantly. You need ownership percentages, voting rights, profit distribution, and exit clauses. Strongly recommend a lawyer for this.
- **For developers in California:** Be aware of the $800 minimum franchise tax. If your app earns less than $800/year, this tax exceeds your revenue. Some CA developers delay LLC formation until revenue justifies it.
- **For developers planning to raise investment:** VCs strongly prefer Delaware C-Corps. If fundraising is on your 12-month roadmap, consider forming a Delaware C-Corp instead of an LLC. This is a fundamentally different path — consult a startup attorney.
- **For international developers:** This guide is US-focused. Other countries have different entity types (Ltd in the UK, GmbH in Germany, etc.). The principles (separate entity, liability protection, tax optimization) apply universally, but the specifics differ entirely.
- **For developers already earning revenue without an entity:** You've been operating as a sole proprietor by default. Forming an LLC doesn't retroactively change past tax obligations, but it does protect you going forward. File any back taxes if you haven't been reporting the income.
