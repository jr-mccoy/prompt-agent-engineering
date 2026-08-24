---
title: "GCP Google for Startups Cloud Program Application Guide"
category: cloud-infrastructure
description: "Navigate the Google for Startups Cloud Program application process, covering eligibility assessment for all three tiers ($2K Start, $100K Scale, $350K AI First), application strategy, credit maximization during the award period, and post-credit planning to avoid cost cliffs."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
  - DS-02
  - RT-05
difficulty: beginner
tags:
  - gcp
  - startup
  - credits
  - google-for-startups
  - cost-management
  - cloud-credits
  - solo-developer
  - android
  - business
updated: "2026-02-11"
---

# GCP Google for Startups Cloud Program Application Guide

**Objective:** Successfully apply to the Google for Startups Cloud Program and maximize the value of GCP credits you receive. This guide covers the eligibility requirements for all three program tiers ($2K Start, $100K Scale, $350K AI First), how to position your application for the best chance of acceptance, what to do during the credit period to extract maximum value, and how to plan for the transition when credits expire so your infrastructure costs do not blindside you.

**When to Use:** Use this prompt when you are building a product on GCP/Firebase and want to reduce your cloud infrastructure costs with startup credits. Also use it before you start spending significant money on GCP -- the earlier you apply, the more runway you get from the credits. Solo developers and early-stage founders often do not realize they qualify, or they apply without understanding the tier differences and leave money on the table. If you are spending more than $0 on GCP and have not applied, you are leaving free money unused.

---

## Context Gathering

Before starting your application, gather the following:

1. **Company/Project Status**
   - Do you have a registered business entity? (LLC, C-Corp, etc.)
   - When was it incorporated/registered?
   - What is your product or service?
   - What stage are you? (Idea, MVP, launched, revenue-generating)
   - Have you raised funding? If so, how much and what round?

2. **Current GCP Usage**
   - Do you have an existing GCP project?
   - What is your current monthly GCP spend?
   - What GCP services are you using or planning to use?
   - Are you using any AI/ML services? (Vertex AI, Cloud AI APIs, Gemini API)

3. **Growth Indicators**
   - What is your current user count or traction?
   - What does your 12-month growth projection look like?
   - Do you have a website with your product described?
   - Do you have a pitch deck or one-pager?

4. **Affiliation**
   - Are you affiliated with any startup accelerator, incubator, or VC firm?
   - Are you part of any Google-partnered programs?
   - Do you have a Google account manager or partner contact?

---

## Instructions

### CRITICAL: Verification Requirements

Before applying, verify these prerequisites:

1. **Your company is a startup** (generally under 5 years old and under Series B funding) -- not a consultancy, agency, or enterprise division
2. **You have not previously received Google for Startups Cloud credits** at the tier you are applying for (you can upgrade tiers)
3. **Your GCP billing account is in good standing** with no unpaid balances
4. **You have a working website or app** that demonstrates your product (applications with "coming soon" landing pages have lower acceptance rates)
5. **You are using or plan to use GCP** as your primary cloud provider (not just Firebase, though Firebase counts since it runs on GCP)
6. **Acceptable null result:** Getting rejected does not mean you can never apply again. Many startups are accepted on a second application after demonstrating more traction or a clearer GCP usage plan.

### False-Positive Prevention

- **DO NOT** apply to the highest tier if you do not meet its requirements. Applying for $350K AI First when you have no AI/ML component will get rejected and may delay your ability to apply for the correct tier.
- **DO NOT** assume credits cover everything. Some GCP services, premium support, and marketplace purchases may not be covered by startup credits.
- **DO NOT** burn through credits on experimentation without a plan. Credits expire (typically 12-24 months), and wasting them on services you do not end up using means you need to pay full price later for the services you do need.
- **DO NOT** scale up infrastructure during the credit period beyond what you would be willing to pay for post-credits. This creates a cost cliff.
- **DO NOT** apply with a personal Gmail account if you have a business domain. Applications from business domains are taken more seriously.
- **DO** apply as early as possible. Credits start from the approval date, not from when you start using them.
- **DO** be specific about which GCP services you plan to use and why. Generic "we use the cloud" descriptions hurt your application.
- **DO** mention AI/ML plans even for the lower tiers -- Google is investing heavily in AI and favors startups in that space.

---

### Phase 1: Eligibility Check

#### Program Overview

The Google for Startups Cloud Program offers three tiers of GCP credits. Each tier has different requirements and benefits.

```
Google for Startups Cloud Program Tiers:
│
├── Tier 1: START ($2,000 in credits)
│   ├── Eligibility: Most early-stage startups
│   ├── Requirements:
│   │   ├── New to Google Cloud (no prior significant usage)
│   │   ├── Company is less than 10 years old
│   │   ├── Funded up to Series A (or bootstrapped)
│   │   ├── Has a website or app
│   │   └── Self-serve application
│   ├── Credit duration: 12 months
│   ├── Additional benefits:
│   │   ├── Google Cloud Skills Boost training credits
│   │   ├── Technical onboarding guidance
│   │   └── Google Workspace discounts
│   └── Best for: Solo developers, pre-revenue, MVP stage
│
├── Tier 2: SCALE ($100,000 in credits)
│   ├── Eligibility: Startups with traction and funding
│   ├── Requirements:
│   │   ├── Funded: Seed to Series A (typical)
│   │   ├── Affiliated with approved accelerator, incubator, or VC
│   │   ├── Company less than 10 years old
│   │   ├── Has not previously received $100K+ in GCP credits
│   │   └── Referred through partner or applied directly
│   ├── Credit duration: 12-24 months
│   ├── Additional benefits:
│   │   ├── Technical architecture review
│   │   ├── 12 months Google Workspace Business Plus
│   │   ├── Google Cloud Skills Boost
│   │   ├── Access to startup community events
│   │   └── Potential Google engineer office hours
│   └── Best for: Funded startups, post-MVP, growing user base
│
└── Tier 3: AI FIRST ($350,000 in credits)
    ├── Eligibility: AI/ML-focused startups
    ├── Requirements:
    │   ├── AI/ML is core to the product (not just a feature)
    │   ├── Funded: Seed to Series B
    │   ├── Plans to use Vertex AI, Cloud AI APIs, or TPUs
    │   ├── Company less than 10 years old
    │   ├── Has not previously received $350K+ in GCP credits
    │   └── Typically requires referral or partner affiliation
    ├── Credit duration: 24 months
    ├── Additional benefits:
    │   ├── Everything in Scale tier
    │   ├── Dedicated Google Cloud AI engineer support
    │   ├── Early access to AI/ML features
    │   ├── Google AI ecosystem introductions
    │   └── Potential co-marketing opportunities
    └── Best for: AI-native startups, heavy ML workloads, LLM-based products
```

#### Self-Assessment Checklist

```markdown
## Eligibility Self-Assessment

### Basic Requirements (All Tiers)
- [ ] Company is less than 10 years old
- [ ] Company is a technology startup (not a consulting firm, agency, or subsidiary)
- [ ] Has a website or app that describes the product
- [ ] Has a GCP billing account (or will create one)
- [ ] Has not already received credits at the target tier

### START Tier ($2K) -- Additional Requirements
- [ ] New to Google Cloud (or very low usage)
- [ ] Funded up to Series A OR bootstrapped
- [ ] Willing to self-serve (no partner required)
→ If all checked: Apply directly at cloud.google.com/startup

### SCALE Tier ($100K) -- Additional Requirements
- [ ] Has received funding (Seed to Series A typical)
- [ ] Affiliated with an approved partner (accelerator, VC, incubator)
   OR
- [ ] Has significant traction (users, revenue, growth metrics)
- [ ] Can articulate specific GCP service usage plans
→ If all checked: Apply through partner or directly

### AI FIRST Tier ($350K) -- Additional Requirements
- [ ] AI/ML is central to the product (not supplementary)
- [ ] Plans to use Vertex AI, Gemini API, Cloud AI APIs, or TPUs
- [ ] Has a clear AI/ML technical architecture
- [ ] Funded Seed to Series B
→ If all checked: Apply through partner, with AI focus emphasized
```

#### Approved Partner Organizations

Getting a referral from an approved partner significantly increases your acceptance rate, especially for the Scale and AI First tiers.

```
Types of Approved Partners:
│
├── Accelerators/Incubators
│   ├── Y Combinator
│   ├── Techstars
│   ├── 500 Global
│   ├── Plug and Play
│   ├── Google for Startups Accelerator
│   ├── Antler
│   ├── Seedcamp
│   └── Many regional accelerators (check Google's partner list)
│
├── Venture Capital Firms
│   ├── Most institutional VC firms are partners
│   ├── Check with your lead investor's portfolio team
│   └── Some angel groups also qualify
│
├── Startup Support Organizations
│   ├── Google for Startups Campus members
│   ├── Startup Grind (Google-affiliated)
│   ├── Local startup hubs partnered with Google
│   └── University entrepreneurship programs
│
└── Google Cloud Partners
    ├── Google Cloud Premier Partners
    ├── Google Cloud Partner advantage members
    └── Google Developer Expert network
```

---

### Phase 2: Program Selection

#### Decision Framework: Which Tier to Apply For

```
Start here:
│
├─→ Do you have AI/ML as your core product?
│   ├── Yes, AI is central → Apply for AI FIRST ($350K)
│   │   └── Examples: LLM-powered product, ML model serving,
│   │       computer vision app, NLP service, AI coding tool
│   └── No, or AI is a feature → Continue below
│
├─→ Have you raised Seed or Series A funding?
│   ├── Yes → Apply for SCALE ($100K)
│   │   └── Even better with partner referral
│   └── No → Continue below
│
├─→ Are you affiliated with an approved accelerator/incubator?
│   ├── Yes → Apply for SCALE ($100K) through the partner
│   └── No → Continue below
│
├─→ Do you have meaningful traction? (1K+ users, revenue, press)
│   ├── Yes → Try for SCALE ($100K) with direct application
│   │   └── Emphasize traction metrics in application
│   └── No → Continue below
│
└─→ Default → Apply for START ($2K)
    └── You can upgrade later when you qualify for a higher tier
```

#### Strategic Considerations

| Scenario | Recommended Approach |
|----------|---------------------|
| Solo dev, no funding, building MVP | START ($2K). Apply now, upgrade later. |
| Solo dev, accepted to accelerator | SCALE ($100K) through accelerator. Apply immediately. |
| Bootstrapped with 5K+ users | SCALE ($100K) direct. Emphasize organic growth. |
| Pre-seed funded, building AI product | AI FIRST ($350K). Lead with AI architecture. |
| Seed funded, not AI-focused | SCALE ($100K). Mention any AI plans for bonus points. |
| Side project, not a registered company | START ($2K) if you can show it is a real product. Consider incorporating first. |

---

### Phase 3: Application Preparation

#### What the Application Asks For

The application form varies by tier but generally includes:

```markdown
## Application Fields (Typical)

### Company Information
- Company name
- Company website URL
- Year founded
- Country/region
- Industry vertical
- Number of employees
- Company description (2-3 sentences)

### Funding Information
- Funding stage (Pre-seed, Seed, Series A, etc.)
- Total funding raised
- Lead investors (if applicable)
- Accelerator/incubator affiliation

### Technical Information
- Current GCP project ID (if existing)
- Current monthly GCP spend
- GCP services currently using
- GCP services planning to use
- Technical architecture description
- How GCP fits into your product

### Growth & Traction
- Current users/customers
- Monthly growth rate
- Key metrics (MRR, DAU, transactions, etc.)
- 12-month growth plan

### AI/ML (for AI First tier)
- AI/ML technologies used
- Training infrastructure needs
- Inference/serving requirements
- Vertex AI or Gemini API usage plans
```

#### Application Tips: What Reviewers Look For

```
Application Scoring Factors (Unofficial, Based on Pattern Matching):
│
├── STRONG SIGNALS (significantly help your application)
│   ├── Specific GCP service names and use cases
│   │   → "We use Cloud Functions for payment webhooks, Firestore for
│   │      user data, and plan to use Vertex AI for recommendation engine"
│   ├── Growth metrics with context
│   │   → "3,200 MAU growing 15% month-over-month since launch in October"
│   ├── Clear technical architecture
│   │   → Brief description of how GCP services connect in your stack
│   ├── Revenue or strong engagement metrics
│   │   → Shows you are building something people want
│   └── Partner referral
│       → Warm introduction from accelerator/VC carries weight
│
├── WEAK SIGNALS (do not hurt but do not help much)
│   ├── "We plan to use Google Cloud"
│   │   → Too vague, every applicant says this
│   ├── "We are disrupting the X industry"
│   │   → Buzzwords without substance
│   ├── Large team size without traction
│   │   → Raises questions about efficiency
│   └── Requesting credits without a clear usage plan
│       → Suggests you might waste the credits
│
└── RED FLAGS (may cause rejection)
    ├── Consulting/agency business model
    │   → Program is for product startups
    ├── No website or "coming soon" page only
    │   → Suggests the product does not exist yet
    ├── Applying for AI First with no AI component
    │   → Mismatch with tier requirements
    ├── Previously received credits at this tier
    │   → Disqualifying (but can upgrade tiers)
    └── Company is clearly over 10 years old
        → Outside eligibility window
```

#### Sample Application Descriptions

**For a solo developer building a mobile app (START tier):**

> [Company name] is a mobile-first platform that helps [target users] do [specific thing]. We are built entirely on Firebase and GCP, using Cloud Functions for our API layer, Firestore for real-time data, Cloud Storage for user media, and Firebase Analytics exported to BigQuery for product analytics. We have [X] active users on Android with an iOS launch planned. GCP credits will directly fund our infrastructure as we scale from beta to general availability, specifically covering increased Firestore read/write operations and Cloud Functions invocations as we grow past Firebase free tier limits.

**For a funded startup (SCALE tier):**

> [Company name] is a [brief product description] serving [target market]. We raised a [$X] Seed round led by [Investor] in [date] and are part of [Accelerator name]. Our architecture runs on GCP: Cloud Run for our API backend, Firestore for document storage, BigQuery for analytics, Cloud Pub/Sub for event processing, and Cloud Storage for media. We currently spend $[X]/month on GCP and project this growing to $[X]/month as we scale to [target users] over the next 12 months. Specific infrastructure needs include increased Cloud Run instances for API serving, BigQuery for expanded analytics, and potential Vertex AI integration for [specific ML use case].

**For an AI startup (AI FIRST tier):**

> [Company name] builds [AI product description] using [specific AI/ML technologies]. Our core ML pipeline runs on GCP: training on Vertex AI with [model type], serving predictions via Cloud Run with [framework], and storing training data in Cloud Storage. We use the Gemini API for [specific use case] and plan to fine-tune models on Vertex AI as our training dataset grows. Current monthly GCP spend is $[X] with $[X] going to AI/ML compute. Credits will primarily fund training infrastructure on Vertex AI and inference serving on Cloud Run with GPU support, enabling us to iterate on model quality without compute cost constraints.

---

### Phase 4: Credit Maximization

Once approved, you have a fixed window (typically 12-24 months) to use your credits. Here is how to get the most value.

#### Credit Usage Strategy

```
Credit Allocation Priority:
│
├── Priority 1: Production Infrastructure (50-60% of credits)
│   ├── The services your users directly depend on
│   ├── Cloud Functions / Cloud Run compute
│   ├── Firestore / Cloud SQL database
│   ├── Cloud Storage for user content
│   └── Networking and load balancing
│
├── Priority 2: Analytics and Data (15-20% of credits)
│   ├── BigQuery for product analytics
│   ├── Firebase Analytics export
│   ├── Cloud Logging for debugging
│   └── Cloud Monitoring for observability
│
├── Priority 3: Development Acceleration (10-15% of credits)
│   ├── Cloud Build for CI/CD
│   ├── Artifact Registry for container images
│   ├── Preview/staging environments
│   └── Testing infrastructure
│
├── Priority 4: AI/ML Experimentation (10-20% of credits)
│   ├── Vertex AI training experiments
│   ├── Gemini API exploration
│   ├── Cloud AI API experimentation (Vision, NLP, Speech)
│   └── GPU instances for ML prototyping
│
└── Priority 5: Future-Proofing (5-10% of credits)
    ├── Load testing at scale
    ├── Disaster recovery testing
    ├── Multi-region deployment testing
    └── Security scanning and hardening
```

#### Monthly Credit Burn Tracking

```bash
# Check your credit balance
# Navigation: GCP Console → Billing → Credits

# Query credit usage from billing export (if you have it set up)
# Replace the table name with your billing export table
bq query --use_legacy_sql=false "
SELECT
  invoice.month AS billing_month,
  ROUND(SUM(cost), 2) AS gross_cost,
  ROUND(SUM(IFNULL(
    (SELECT SUM(c.amount)
     FROM UNNEST(credits) c
     WHERE c.type = 'PROMOTION'), 0
  )), 2) AS credits_applied,
  ROUND(SUM(cost) + SUM(IFNULL(
    (SELECT SUM(c.amount)
     FROM UNNEST(credits) c
     WHERE c.type = 'PROMOTION'), 0
  )), 2) AS net_cost
FROM
  \`$PROJECT_ID.gcp_billing_export.gcp_billing_export_v1_*\`
WHERE
  invoice.month >= '202601'
GROUP BY billing_month
ORDER BY billing_month DESC
"
```

#### Credit Pacing Calculator

```markdown
## Credit Pacing Worksheet

### Your Numbers
- Total credits: $________
- Credit start date: ________
- Credit expiration date: ________
- Months remaining: ________
- Monthly budget (credits / months): $________

### Monthly Tracking
| Month | Budgeted | Actual Spend | Credits Remaining | Pace |
|-------|----------|-------------|-------------------|------|
| Month 1 | $______ | $______ | $______ | On track / Over / Under |
| Month 2 | $______ | $______ | $______ | On track / Over / Under |
| Month 3 | $______ | $______ | $______ | On track / Over / Under |
| ... | | | | |

### Example: $100K credits over 24 months
- Monthly budget: $4,167/month
- Quarter 1-2 (ramp up): $2,000-3,000/month
- Quarter 3-6 (growth): $4,000-5,000/month
- Quarter 7-8 (optimize): $3,000-4,000/month
- Target at expiry: $0-5,000 remaining (wasted credits are lost)
```

#### Things to Use Credits For That You Normally Would Skip

| Service | What to Try | Why Now |
|---------|------------|---------|
| BigQuery ML | Train ML models directly in BigQuery | Normally expensive for experiments |
| Cloud Armor | DDoS protection and WAF | Usually skipped by solo devs for cost |
| Cloud CDN | Content delivery for static assets | Performance boost, usually a luxury |
| Vertex AI | Fine-tune an LLM on your data | Prohibitively expensive without credits |
| Cloud SQL (HA) | High-availability PostgreSQL | Normally solo devs use single-instance |
| Load testing | Run large-scale load tests | Normally costs too much to simulate 10K users |
| Multi-region | Test multi-region deployment | Normally too expensive to maintain |
| Cloud Monitoring premium | Custom metrics and dashboards | Normally limited to free tier |
| Secret Manager | Store all secrets properly | Free tier is limited; credits remove hesitation |

---

### Phase 5: Post-Credit Planning

The most dangerous moment is when credits expire. If you have scaled up during the credit period without tracking what you would actually pay, you face a cost cliff.

#### Timeline: 6 Months Before Expiration

```
6 Months Before Credit Expiration:
│
├── Month -6: AUDIT
│   ├── Calculate current monthly spend (gross, before credits)
│   ├── Identify which services you actually need vs nice-to-have
│   ├── Start the cost optimization process (see gcp_solo_dev_cost_management.md)
│   └── Determine your sustainable monthly budget without credits
│
├── Month -4: OPTIMIZE
│   ├── Downsize over-provisioned resources
│   ├── Delete unused resources (old Cloud Run revisions, test data, etc.)
│   ├── Enable committed use discounts if usage is predictable
│   ├── Move development/staging to smaller instances or scale-to-zero
│   └── Set up budget alerts for your post-credit budget
│
├── Month -3: TEST
│   ├── Simulate post-credit costs by tracking gross spend
│   ├── Verify your budget alerts work
│   ├── Ensure auto-scaling settings have reasonable max-instance limits
│   └── Review BigQuery query patterns for cost efficiency
│
├── Month -2: TRANSITION PLAN
│   ├── Apply for a higher credit tier if eligible (upgrade from Start to Scale)
│   ├── Explore other credit programs (GCP free trial, startup competitions)
│   ├── Consider committed use discounts (1-year or 3-year)
│   └── Set up billing export if not already done
│
├── Month -1: FINAL CHECK
│   ├── Confirm post-credit budget is survivable
│   ├── All cost optimizations are in place
│   ├── Budget alerts are set for new (lower) thresholds
│   └── Kill switch function is deployed (see gcp_solo_dev_cost_management.md)
│
└── Month 0: CREDITS EXPIRE
    ├── Monitor billing daily for the first week
    ├── Verify no unexpected charges
    └── Adjust resources if actual spend exceeds projections
```

#### Post-Credit Cost Reduction Strategies

```bash
# 1. Committed Use Discounts (CUDs) -- save 20-57% on predictable workloads
# Navigate: GCP Console → Billing → Commitments
# Only commit to resources you are certain you will use for 1-3 years

# 2. Review and right-size Cloud Run instances
gcloud run services describe my-backend \
  --region=us-central1 \
  --format="table(spec.template.spec.containers[0].resources.limits)" \
  --project=$PROJECT_ID

# Downsize if over-provisioned
gcloud run services update my-backend \
  --memory=256Mi \
  --cpu=1 \
  --max-instances=2 \
  --region=us-central1 \
  --project=$PROJECT_ID

# 3. Check for orphaned resources
# List all Cloud Run services
gcloud run services list --project=$PROJECT_ID

# List all Cloud Functions
gcloud functions list --project=$PROJECT_ID

# List all Cloud Storage buckets and their sizes
gsutil du -s gs://*

# List all Compute Engine instances (should be zero for serverless stacks)
gcloud compute instances list --project=$PROJECT_ID

# 4. Set aggressive budget alerts for post-credit period
gcloud billing budgets create \
  --billing-account=$BILLING_ACCOUNT_ID \
  --display-name="Post-Credit Monthly Budget" \
  --budget-amount=50.00USD \
  --threshold-rule=percent=0.50 \
  --threshold-rule=percent=0.80 \
  --threshold-rule=percent=1.00 \
  --filter-projects="projects/$PROJECT_ID"
```

#### Re-Application and Tier Upgrade

```markdown
## Can You Apply Again?

| Current Status | Can Apply For | Notes |
|---------------|--------------|-------|
| Received $2K START | $100K SCALE | Yes, this is an upgrade |
| Received $2K START | $350K AI FIRST | Yes, if AI-focused |
| Received $100K SCALE | $350K AI FIRST | Yes, if AI-focused |
| Received $100K SCALE | $100K SCALE again | No, same tier not allowed |
| Rejected | Same tier | Yes, after improving application |
| Rejected | Different tier | Yes, immediately |
| Credits expired | Higher tier | Yes, standard eligibility rules |

## Other GCP Credit Sources
- GCP Free Trial: $300 for 90 days (new accounts only)
- Google Cloud Research Credits: For academic research
- Google.org Impact Challenge: For nonprofits and social enterprises
- Google Developer Expert program: GCP credits as a benefit
- Startup competition prizes: Many Google-sponsored events include credits
- Google Cloud Partner programs: If you become a partner
```

---

## Expected Output

After following this guide, your startup credit strategy should produce:

```markdown
## Google for Startups Cloud Program Application Summary

### Application Details
| Field | Value |
|-------|-------|
| Company | My Android App, Inc. |
| Applied Tier | SCALE ($100K) |
| Application Date | 2026-02-15 |
| Partner Referral | Techstars Atlanta 2026 |
| Status | APPROVED |
| Credit Amount | $100,000 |
| Credit Start | 2026-03-01 |
| Credit Expiration | 2028-02-28 (24 months) |

### Credit Allocation Plan
| Category | Monthly Budget | 24-Month Total | % of Credits |
|----------|---------------|----------------|-------------|
| Production infra | $2,500 | $60,000 | 60% |
| Analytics & data | $625 | $15,000 | 15% |
| Dev acceleration | $500 | $12,000 | 12% |
| AI/ML experiments | $415 | $10,000 | 10% |
| Buffer/contingency | $125 | $3,000 | 3% |
| **Total** | **$4,167** | **$100,000** | **100%** |

### Monthly Burn Tracking
| Month | Budget | Actual | Credits Left | Pace |
|-------|--------|--------|-------------|------|
| Mar 2026 | $4,167 | $1,850 | $98,150 | Under (ramping up) |
| Apr 2026 | $4,167 | $2,340 | $95,810 | Under (still growing) |
| May 2026 | $4,167 | $3,100 | $92,710 | Under (approaching target) |

### Post-Credit Planning
| Action | Target Date | Status |
|--------|------------|--------|
| Set up billing export | Mar 2026 | Complete |
| Deploy budget alerts | Mar 2026 | Complete |
| First cost audit | Sep 2027 (6 mo before) | Pending |
| Apply for AI First upgrade | Dec 2027 | Pending |
| Right-size resources | Jan 2028 | Pending |
| Set post-credit budget | Feb 2028 | Pending |
```

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Defined the goal of applying for and maximizing startup credits
- **ST-02 (Sequential Step-by-Step Instructions):** Phased approach from eligibility assessment through application, credit use, and post-credit planning
- **RT-02 (Multi-Dimensional Analysis):** Analyzed the program across three tiers, multiple eligibility criteria, and various credit usage strategies
- **CM-01 (Contextual Framing):** All advice targeted at solo developers and early-stage startups on GCP/Firebase
- **DS-06 (Prioritization and Severity Guidance):** Credit allocation priorities and post-credit timeline with escalating urgency
- **DS-02 (Metric Specification):** Concrete credit amounts, budget pacing numbers, and monthly tracking targets
- **RT-05 (Evidence-Based Reasoning):** Application tips based on common acceptance/rejection patterns

---

## Related Prompts

- `gcp_solo_dev_cost_management.md` -- Cost management that complements credit strategy
- `gcp_cloud_run_backend.md` -- Infrastructure to build during credit period
- `gcp_bigquery_analytics_pipeline.md` -- Analytics pipeline to set up with credit-funded BigQuery
- `gcp_monitoring_alerting_setup.md` -- Monitoring to deploy while credits cover the cost
- `cloud_cost_optimization.md` -- General cost optimization for when credits expire

---

## Customization Guide

- **For solo developers with no funding:** Focus on the START tier ($2K). Even $2K covers many months of GCP usage for a solo project. Emphasize your product vision and specific GCP usage plans. If you are part of any startup community (even a meetup group), mention it.
- **For bootstrapped startups with revenue:** You may qualify for SCALE ($100K) without VC funding if you can demonstrate strong traction and growth. Revenue is a powerful signal in the application. Emphasize your growth rate and GCP architecture.
- **For accelerator-affiliated startups:** This is your strongest path to SCALE or AI FIRST credits. Ask your accelerator's Google partnership contact to submit a referral. Some accelerators automatically include GCP credits as part of their program -- check before applying separately.
- **For AI/ML-focused startups:** Always apply for AI FIRST ($350K), even if you think you might not qualify. The worst outcome is a redirect to SCALE. Be specific about your model architecture, training compute needs, and Vertex AI usage plans.
- **For startups already spending $500+/month on GCP:** Apply urgently. Every month without credits is money lost. If approved, the credits apply to future billing, not past invoices. Include your current spending in the application as evidence of GCP commitment.
- **For startups outside the US:** The program is global. Application requirements are the same, but partner networks vary by region. Check for Google for Startups programs specific to your country (e.g., Google for Startups Accelerator Africa, India, etc.).
