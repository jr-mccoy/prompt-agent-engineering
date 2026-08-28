---
title: "Value Proposition Canvas Analysis for Codebase"
category: software-engineering/analysis/business
description: "Apply the Value Proposition Canvas framework to evaluate fit between customer needs (jobs, pains, gains) and product offerings (products, pain relievers, gain creators), identifying alignment gaps and improvement opportunities"
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - DS-01  # Framework Application
  - RT-02  # Multi-Dimensional Analysis
  - QA-02  # Adversarial Thinking
  - DS-06  # Prioritization Guidance
difficulty: intermediate
tags:
  - value-proposition
  - customer-needs
  - product-strategy
  - product-market-fit
  - customer-research
updated: "2026-01-25"
related_prompts:
  - domain-software-engineering/analysis/business/jobs_to_be_done_analysis.md
  - domain-software-engineering/analysis/business/business_model_canvas_analysis.md
  - domain-software-engineering/analysis/business/product_market_fit_analysis.md
  - domain-software-engineering/analysis/business/lean_canvas_analysis.md
---

# Value Proposition Canvas Analysis for Codebase

**Objective:** Analyze the codebase using the Value Proposition Canvas framework to evaluate the fit between what customers need (Customer Profile: jobs, pains, gains) and what the product offers (Value Map: products/services, pain relievers, gain creators), identifying alignment gaps and opportunities to strengthen the value proposition.

## When to Use

- **Use when:** Validating whether a product truly addresses customer needs
- **Use when:** Prioritizing features based on pain/gain importance
- **Use when:** Preparing messaging or positioning for a product launch
- **Use when:** Diagnosing why a product isn't getting traction despite good features
- **Use when:** Evaluating product-market fit for a specific customer segment
- **Don't use when:** You haven't identified a clear customer segment (do segmentation first)
- **Don't use when:** You need business model analysis beyond value proposition (use Business Model Canvas)
- **Don't use when:** The product is internal infrastructure with no end-user

## Instructions

1. **Define the Customer Segment**
   - Clearly identify the specific customer segment being analyzed
   - Avoid "everyone" – focus on a single, well-defined segment
   - Note if different segments have different profiles
   - **Evidence to collect:** Persona documentation, customer interviews, user research

2. **Build the Customer Profile**

   **a. Customer Jobs (Tasks they're trying to complete):**
   - **Functional jobs:** What practical tasks are they trying to accomplish?
   - **Social jobs:** How do they want to be perceived by others?
   - **Emotional jobs:** How do they want to feel?
   - **Supporting jobs:** Jobs in the context of purchasing, using, or disposing
   - Rank jobs by importance (critical → nice-to-have)
   - **Evidence to collect:** Interviews, support tickets, search queries, review analysis

   **b. Customer Pains (Problems, frustrations, risks):**
   - What frustrates them about current solutions?
   - What are they afraid of or trying to avoid?
   - What obstacles prevent them from doing their jobs?
   - What risks concern them (functional, social, emotional, financial)?
   - Rate pains by severity (extreme → moderate → mild)
   - **Evidence to collect:** Churn reasons, complaints, competitive switching triggers

   **c. Customer Gains (Benefits and desires):**
   - What outcomes do they expect or desire?
   - What would exceed their expectations?
   - What would make their job or life easier?
   - What social consequences are they seeking?
   - Rate gains by relevance (essential → nice-to-have)
   - **Evidence to collect:** Feature requests, NPS feedback, positive reviews

3. **Build the Value Map**

   **a. Products & Services (What you offer):**
   - List all features, services, and offerings
   - Note which are core vs. supplementary
   - Identify which jobs each product/service helps with
   - **Evidence to collect:** Feature inventory, product documentation, usage data

   **b. Pain Relievers (How you address pains):**
   - For each pain identified, how does the product alleviate it?
   - Be specific: which feature addresses which pain?
   - Note pains that are NOT addressed (gaps)
   - Rate effectiveness: eliminates vs. reduces vs. doesn't address
   - **Evidence to collect:** Support ticket reduction, user feedback on problem resolution

   **c. Gain Creators (How you create gains):**
   - For each gain desired, how does the product create it?
   - Which features create which gains?
   - Note gains that are NOT created (gaps)
   - Rate effectiveness: exceeds expectations vs. matches vs. doesn't deliver
   - **Evidence to collect:** Positive reviews, feature usage, NPS drivers

4. **Assess Fit Quality**
   - Map each Value Map element to Customer Profile elements
   - Identify fit patterns:
     - **Strong fit:** Important job/pain/gain addressed effectively
     - **Weak fit:** Important job/pain/gain addressed inadequately
     - **No fit:** Important job/pain/gain not addressed at all
     - **Overserved:** Low-importance job/pain/gain addressed extensively
   - Calculate a rough fit score

5. **CRITICAL: Validate Fit Claims Before Reporting**
   - For each claimed fit:
     - Is there evidence that customers recognize this value?
     - Do customers use the features that create this fit?
     - Would customers describe the fit the same way we do?
   - For each identified gap:
     - Is this a real gap or a perception issue?
     - Have customers explicitly asked for this to be addressed?
     - Is the gap important enough to prioritize?
   - Watch for:
     - Inside-out bias: Describing features, not customer benefits
     - Importance inflation: Assuming all jobs/pains/gains are equal
     - Fit overconfidence: Claiming fit without customer validation

6. **Develop Recommendations**
   - Prioritize gaps by importance × severity
   - Identify quick wins (easy fixes for significant gaps)
   - Identify strategic opportunities (major improvements for core jobs)
   - Identify simplification opportunities (reduce investment in overserved areas)
   - Consider messaging improvements (fit exists but isn't communicated)

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- List jobs/pains/gains without ranking by importance (not all are equal)
- Claim pain relievers without evidence customers experience relief
- Confuse features with benefits ("has notifications" vs. "never misses important updates")
- Assume customers value what we think they should value
- Ignore negative evidence (complaints, churn, low usage)
- Over-claim fit based on feature availability vs. actual customer experience

✅ **DO:**
- Rank everything by importance to the customer
- Validate fit claims with behavioral evidence (usage, retention, NPS)
- Express benefits in customer language, not product language
- Acknowledge gaps honestly – they're opportunities
- Distinguish between "we offer this" and "customers value this"
- Test fit claims with customer interviews or surveys

## Confidence Levels

Rate each fit assessment with a confidence level:

- **Validated:** Customer evidence confirms the fit (interviews, usage data, testimonials)
- **Claimed:** We believe this fit exists but lack direct validation
- **Gap:** We know this doesn't fit well (acknowledged gap)

## Expected Output

A comprehensive Value Proposition Canvas analysis including:
- Customer Profile (jobs, pains, gains with rankings)
- Value Map (products, pain relievers, gain creators)
- Fit assessment matrix
- Prioritized recommendations

### Output Format

```markdown
## Value Proposition Canvas Analysis: [Product Name] for [Customer Segment]

### Executive Summary
[3-5 sentences summarizing the value proposition fit and key opportunities]

### Customer Profile: [Segment Name]

#### Customer Jobs (Ranked by Importance)

| Rank | Job | Type | Importance | Evidence |
|------|-----|------|------------|----------|
| 1 | [Job description] | Functional/Social/Emotional | Critical/Important/Nice-to-Have | [How we know] |

#### Customer Pains (Ranked by Severity)

| Rank | Pain | Severity | Evidence |
|------|------|----------|----------|
| 1 | [Pain description] | Extreme/Moderate/Mild | [How we know] |

#### Customer Gains (Ranked by Relevance)

| Rank | Gain | Relevance | Evidence |
|------|------|-----------|----------|
| 1 | [Gain description] | Essential/Nice-to-Have/Unexpected | [How we know] |

### Value Map: [Product Name]

#### Products & Services

| Product/Feature | Jobs Addressed | Core/Supplementary |
|-----------------|----------------|-------------------|
| [Feature] | [Which jobs] | Core/Supplementary |

#### Pain Relievers

| Pain | Pain Reliever | Effectiveness | Evidence |
|------|---------------|---------------|----------|
| [Pain from profile] | [How addressed] | Eliminates/Reduces/Doesn't Address | [Usage data, feedback] |

#### Gain Creators

| Gain | Gain Creator | Effectiveness | Evidence |
|------|--------------|---------------|----------|
| [Gain from profile] | [How created] | Exceeds/Matches/Doesn't Deliver | [Usage data, feedback] |

### Fit Assessment

#### Visual Canvas
```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        VALUE PROPOSITION CANVAS                              │
├───────────────────────────────┬─────────────────────────────────────────────┤
│       VALUE MAP               │           CUSTOMER PROFILE                   │
│                               │                                              │
│   ┌─────────────────────┐     │     ┌─────────────────────────────────┐     │
│   │   GAIN CREATORS     │     │     │           GAINS                 │     │
│   │   [List]            │←────┼────→│           [List]                │     │
│   └─────────────────────┘     │     └─────────────────────────────────┘     │
│                               │                                              │
│   ┌─────────────────────┐     │     ┌─────────────────────────────────┐     │
│   │ PRODUCTS & SERVICES │←────┼────→│           JOBS                  │     │
│   │   [List]            │     │     │           [List]                │     │
│   └─────────────────────┘     │     └─────────────────────────────────┘     │
│                               │                                              │
│   ┌─────────────────────┐     │     ┌─────────────────────────────────┐     │
│   │   PAIN RELIEVERS    │←────┼────→│           PAINS                 │     │
│   │   [List]            │     │     │           [List]                │     │
│   └─────────────────────┘     │     └─────────────────────────────────┘     │
│                               │                                              │
└───────────────────────────────┴─────────────────────────────────────────────┘
```

#### Fit Matrix

| Customer Need | Type | Importance | Product Response | Fit Quality | Confidence |
|---------------|------|------------|------------------|-------------|------------|
| [Job/Pain/Gain] | Job/Pain/Gain | Critical/Important | [Feature/capability] | Strong/Weak/No Fit | Validated/Claimed/Gap |

#### Fit Score Summary

| Category | Strong Fit | Weak Fit | No Fit | Overserved |
|----------|------------|----------|--------|------------|
| Jobs | X | Y | Z | W |
| Pains | X | Y | Z | W |
| Gains | X | Y | Z | W |

**Overall Fit Assessment:** [Strong / Moderate / Weak]

### Prioritized Recommendations

| # | Opportunity | Need Addressed | Type | Impact | Effort | Priority |
|---|-------------|----------------|------|--------|--------|----------|
| 1 | [Recommendation] | [Job/Pain/Gain] | Close Gap/Strengthen/Simplify | High/Med/Low | High/Med/Low | P0/P1/P2 |

### Messaging Implications
[How should the value proposition be communicated based on this analysis?]
```

## Example Output

```markdown
## Value Proposition Canvas Analysis: InvoiceFlow for Freelance Designers

### Executive Summary

InvoiceFlow has **moderate fit** with the freelance designer segment. The product strongly addresses the functional job of creating professional invoices and the pain of manual calculations, but **significantly underserves** the critical emotional pain of "chasing payments feels awkward" and the essential gain of "getting paid faster." The biggest opportunity is enhancing automated payment reminders with a human, non-aggressive tone that preserves client relationships. Additionally, the product overserves enterprise features (approval workflows) that this segment doesn't need.

### Customer Profile: Freelance Graphic Designers (Solo, $50-150K annual revenue)

#### Customer Jobs (Ranked by Importance)

| Rank | Job | Type | Importance | Evidence |
|------|-----|------|------------|----------|
| 1 | Get paid on time for completed work | Functional | **Critical** | 12/15 interviewees said this is their #1 concern |
| 2 | Look professional to clients | Social | **Critical** | "Clients judge you by your invoice" - 8 mentions |
| 3 | Spend minimal time on admin | Functional | **Important** | Avg. user spends 4hr/week on invoicing |
| 4 | Track business finances easily | Functional | **Important** | Tax season panic mentioned by 9/15 |
| 5 | Feel confident about pricing | Emotional | **Important** | "Am I charging enough?" anxiety common |
| 6 | Avoid awkward money conversations | Emotional | **Important** | "Asking for money feels gross" - 7 mentions |
| 7 | Accept multiple payment methods | Functional | Nice-to-Have | Some clients prefer specific methods |
| 8 | Create recurring invoices | Functional | Nice-to-Have | Only 30% have retainer clients |

#### Customer Pains (Ranked by Severity)

| Rank | Pain | Severity | Evidence |
|------|------|----------|----------|
| 1 | Clients pay late (60+ days) | **Extreme** | Avg. receivables are 45 days; 23% are 60+ |
| 2 | Chasing payments damages relationships | **Extreme** | "I feel like a debt collector" - 9 mentions |
| 3 | Not knowing if client received/viewed invoice | **Moderate** | "Did it go to spam?" uncertainty |
| 4 | Manual calculations for taxes/totals | **Moderate** | Error rate of 8% in manual invoices |
| 5 | Invoices look unprofessional (Word/Excel) | **Moderate** | "I lost a client because of a sloppy invoice" |
| 6 | Forgetting to invoice for completed work | **Moderate** | Avg. user forgets 2 invoices/quarter |
| 7 | Multiple payment platforms to reconcile | **Mild** | Minor friction, not urgent |
| 8 | Tax prep is chaotic at year end | **Mild** | Seasonal pain, not daily |

#### Customer Gains (Ranked by Relevance)

| Rank | Gain | Relevance | Evidence |
|------|------|-----------|----------|
| 1 | Predictable cash flow | **Essential** | "I just want to know when money is coming" |
| 2 | Spend time on design, not paperwork | **Essential** | "Every minute on invoicing is a minute not designing" |
| 3 | Clients perceive me as professional | **Essential** | Social proof of professionalism matters |
| 4 | Clear picture of business health | **Important** | "I have no idea if I'm profitable" |
| 5 | Automated reminders so I don't have to ask | **Important** | "I want the tool to be the bad guy" |
| 6 | Easy year-end tax reporting | Nice-to-Have | Seasonal value |
| 7 | Impress clients with branded experience | Nice-to-Have | Some want white-label |
| 8 | Get paid instantly (same-day) | **Unexpected** | Would delight if possible |

---

### Value Map: InvoiceFlow

#### Products & Services

| Product/Feature | Jobs Addressed | Core/Supplementary |
|-----------------|----------------|-------------------|
| Invoice templates | Look professional, Create invoices quickly | **Core** |
| Automatic calculations | Spend minimal time on admin | **Core** |
| Payment processing (Stripe/PayPal) | Accept multiple payment methods | **Core** |
| Invoice tracking (sent/viewed/paid) | Know if client received invoice | **Core** |
| Payment reminders | Get paid on time | **Core** |
| Dashboard & reporting | Track business finances | Supplementary |
| Recurring invoices | Create recurring invoices | Supplementary |
| Client portal | Look professional | Supplementary |
| Approval workflows | (Enterprise feature) | Supplementary |
| Multi-currency support | (Enterprise feature) | Supplementary |

#### Pain Relievers

| Pain | Pain Reliever | Effectiveness | Evidence |
|------|---------------|---------------|----------|
| Manual calculations | Auto-calc totals, taxes, discounts | **Eliminates** | 0% error rate; 15 min saved/invoice |
| Invoices look unprofessional | Professional templates | **Eliminates** | 4.8/5 satisfaction rating |
| Not knowing if invoice was viewed | Read receipts & tracking | **Reduces** | 70% of users check status regularly |
| **Clients pay late** | Payment reminders | **Reduces partially** | Only 12% improvement in collection time |
| **Chasing payments damages relationships** | Automated reminders | **Doesn't Address Well** | Reminder tone is "aggressive"; complaints |
| Forgetting to invoice | No feature | **Gap** | No project-to-invoice automation |
| Multiple platforms to reconcile | Some integrations | **Reduces** | Only 3 integrations; users want more |
| Tax prep chaos | Basic reports | **Reduces** | Reports exist but aren't tax-ready |

#### Gain Creators

| Gain | Gain Creator | Effectiveness | Evidence |
|------|--------------|---------------|----------|
| Spend time on design, not paperwork | Quick invoice creation (< 5 min) | **Matches** | Users report 70% time savings |
| Clients perceive me as professional | Branded templates, client portal | **Exceeds** | Multiple testimonials cite this |
| Clear picture of business health | Dashboard | **Matches** | Used by 45% of users monthly |
| **Predictable cash flow** | Basic forecasting | **Doesn't Deliver** | Feature exists but inaccurate |
| **Automated reminders so I don't have to ask** | Reminder feature | **Partially matches** | Feature works but tone is wrong |
| Easy year-end tax reporting | Report export | **Doesn't Deliver** | Reports not accountant-friendly |
| Get paid instantly | No feature | **Gap** | Instant payout not available |
| Impress with branded experience | White-label | **Doesn't Deliver** | Only on expensive plan |

---

### Fit Assessment

#### Fit Matrix

| Customer Need | Type | Importance | Product Response | Fit Quality | Confidence |
|---------------|------|------------|------------------|-------------|------------|
| Get paid on time | Job | Critical | Payment reminders | **Weak Fit** | Validated (data shows minimal improvement) |
| Look professional | Job | Critical | Templates, portal | **Strong Fit** | Validated (testimonials) |
| Minimal admin time | Job | Important | Auto-calc, templates | **Strong Fit** | Validated (time savings data) |
| Chasing payments awkwardness | Pain | Extreme | Automated reminders | **No Fit** | Validated (complaints about tone) |
| Late payments | Pain | Extreme | Reminders, tracking | **Weak Fit** | Validated (only 12% improvement) |
| Invoice viewed uncertainty | Pain | Moderate | Read receipts | **Strong Fit** | Validated (usage data) |
| Predictable cash flow | Gain | Essential | Forecasting | **No Fit** | Gap (feature is inaccurate) |
| Professional perception | Gain | Essential | Branding features | **Strong Fit** | Validated (testimonials) |
| Auto reminders (right tone) | Gain | Important | Current reminders | **Weak Fit** | Validated (tone complaints) |

#### Fit Score Summary

| Category | Strong Fit | Weak Fit | No Fit | Overserved |
|----------|------------|----------|--------|------------|
| Jobs (8) | 3 | 2 | 1 | 2 |
| Pains (8) | 3 | 2 | 2 | 1 |
| Gains (8) | 2 | 2 | 3 | 1 |
| **Total** | **8** | **6** | **6** | **4** |

**Overall Fit Assessment:** **Moderate** — Strong on professionalism and admin efficiency; Weak on the core job of getting paid faster and the emotional pain of payment conversations.

---

### Prioritized Recommendations

| # | Opportunity | Need Addressed | Type | Impact | Effort | Priority |
|---|-------------|----------------|------|--------|--------|----------|
| 1 | **Redesign payment reminders** with friendly, relationship-preserving tone | "Chasing payments feels awkward" pain | Close Gap | **High** | Low | **P0** |
| 2 | **Add instant payout option** (Stripe Instant Payouts) | "Get paid faster" job + "Predictable cash flow" gain | Close Gap | **High** | Medium | **P0** |
| 3 | **Improve cash flow forecasting** with ML-based predictions | "Predictable cash flow" gain | Close Gap | **High** | Medium | **P1** |
| 4 | **Add project-to-invoice automation** (integrate with Figma, Notion) | "Forgetting to invoice" pain | Close Gap | Medium | Medium | **P1** |
| 5 | **Create tax-ready reports** (Schedule C format) | "Easy tax prep" gain | Close Gap | Medium | Low | **P2** |
| 6 | **Reduce enterprise features** in freelancer tier (approval workflows) | N/A - simplification | Simplify | Low | Low | **P2** |
| 7 | **Add white-label to lower tier** | "Impress clients with branding" gain | Strengthen | Low | Low | **P3** |

---

### Messaging Implications

**Current messaging focuses on:** "Professional invoicing made easy"

**Should shift to:** "Get paid faster without the awkward follow-ups"

**Key messages to emphasize:**
1. **Speed to payment** (not just speed to invoice) — focus on the outcome, not the activity
2. **Relationship-preserving collections** — "Your tool is the bad guy, so you don't have to be"
3. **Predictable cash flow** — if/when we fix forecasting

**Messages to de-emphasize:**
- Enterprise features (approval workflows, multi-currency) — confuses solo freelancers
- Feature lists — focus on outcomes

**Positioning statement suggestion:**
> "InvoiceFlow helps freelance designers get paid on time while keeping client relationships strong. Create professional invoices in minutes, then let us handle the awkward follow-ups—so you can focus on the work you love."
```

## Customization Guide

- **For B2B Products:** Create separate canvases for economic buyer vs. end user—their jobs/pains/gains differ
- **For Multi-sided Platforms:** Create a canvas for each side (e.g., marketplace buyers vs. sellers)
- **For Multiple Segments:** Run the analysis separately for each segment; don't blend profiles
- **For New Products:** Focus on the Customer Profile first; validate before building the Value Map

## Techniques Used

- **ST-01 (Clear Objective Statement):** Explicit goal of evaluating value proposition fit
- **ST-02 (Structured Sequential Instructions):** Systematic progression from profile to map to fit assessment
- **DS-01 (Framework Application):** Direct application of Value Proposition Canvas methodology
- **RT-02 (Multi-Dimensional Analysis):** Evaluation across jobs, pains, and gains dimensions
- **QA-02 (Adversarial Thinking):** False-positive prevention challenges fit claims
- **DS-06 (Prioritization Guidance):** Recommendations prioritized by importance and impact

## Related Prompts

- [Jobs to be Done Analysis](jobs_to_be_done_analysis.md) - Deeper dive on customer jobs
- [Business Model Canvas Analysis](business_model_canvas_analysis.md) - Broader business model context
- [Product-Market Fit Analysis](product_market_fit_analysis.md) - Evaluating overall market fit
- [Lean Canvas Analysis](lean_canvas_analysis.md) - Startup-focused business model analysis
