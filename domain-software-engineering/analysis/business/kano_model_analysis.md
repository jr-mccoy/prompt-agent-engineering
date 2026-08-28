---
title: "Kano Model Analysis for Codebase"
category: software-engineering/analysis/business
description: "Apply the Kano Model to categorize product features by their impact on customer satisfaction (Must-be, Performance, Attractive, Indifferent, Reverse), enabling evidence-based feature prioritization"
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - ST-04  # Delimited Sections
  - DS-01  # Framework Application
  - DS-06  # Prioritization Guidance
  - QA-02  # Adversarial Thinking
difficulty: intermediate
tags:
  - product-strategy
  - feature-prioritization
  - customer-satisfaction
  - business-analysis
  - framework
updated: "2026-01-25"
related_prompts:
  - domain-software-engineering/analysis/business/jobs_to_be_done_analysis.md
  - domain-software-engineering/analysis/business/product_market_fit_analysis.md
  - domain-software-engineering/analysis/business/value_proposition_canvas_analysis.md
---

# Kano Model Analysis for Codebase

**Objective:** Analyze the codebase's product features using the Kano Model to classify them by their impact on customer satisfaction (Must-be, Performance, Attractive, Indifferent, Reverse), enabling strategic prioritization of development efforts to maximize customer delight while ensuring baseline expectations are met.

## When to Use

- **Use when:** Deciding which features to build next from a backlog of options
- **Use when:** Evaluating whether to cut, keep, or enhance existing features
- **Use when:** Resources are limited and trade-offs between features must be made
- **Use when:** Understanding why customers are unsatisfied despite having many features
- **Don't use when:** You lack customer feedback data (Kano requires user input to validate)
- **Don't use when:** Building for a single customer with explicit requirements
- **Don't use when:** Technical debt reduction (not about customer satisfaction)

## Instructions

1. **Inventory Current Features (Required First)**
   - List all user-facing features in the codebase
   - Note implementation completeness (full, partial, stub)
   - Identify features in development or planned
   - Group features by functional area

2. **Gather Customer Input**
   - For proper Kano analysis, survey customers with functional/dysfunctional questions:
     - Functional: "How would you feel if feature X was present?"
     - Dysfunctional: "How would you feel if feature X was absent?"
   - If survey data unavailable, use proxies:
     - Support tickets (complaints = Must-be gaps)
     - Feature requests (often Attractive or Performance)
     - Usage analytics (low usage may indicate Indifferent)
     - Churn reasons (often reveal Must-be failures)

3. **Classify Each Feature Using Kano Categories**

   **a. Must-be (Basic) Features:**
   - Customers expect these; absence causes extreme dissatisfaction
   - Presence doesn't increase satisfaction (taken for granted)
   - Often undifferentiated across competitors
   - **Examples:** Login works, data doesn't disappear, basic security
   - **Code signals:** Error handling, data persistence, authentication

   **b. Performance (One-dimensional) Features:**
   - Satisfaction is proportional to fulfillment level
   - More is better; less is worse
   - Often the main competitive battleground
   - **Examples:** Speed, storage limits, number of integrations
   - **Code signals:** Optimization code, scaling logic, configurable limits

   **c. Attractive (Excitement) Features:**
   - Not expected; presence creates delight
   - Absence doesn't cause dissatisfaction
   - Differentiators that create word-of-mouth
   - **Examples:** Unexpected shortcuts, AI-powered suggestions, delightful animations
   - **Code signals:** Innovative algorithms, surprise UX, going beyond requirements

   **d. Indifferent Features:**
   - Customers don't care whether present or absent
   - Often over-engineered or built for edge cases
   - Candidates for removal or simplification
   - **Examples:** Rarely-used settings, obscure export formats
   - **Code signals:** Features with <5% usage, never-executed code paths

   **e. Reverse Features:**
   - Presence causes dissatisfaction; absence is preferred
   - Often well-intentioned features that annoy users
   - **Examples:** Aggressive upsells, mandatory tutorials, auto-playing content
   - **Code signals:** Interruption patterns, forced flows, modal overuse

4. **Validate Classifications**
   - Cross-reference with usage data (if available)
   - Check support tickets for patterns
   - Interview power users about feature value
   - Consider segment differences (features may classify differently by persona)

5. **CRITICAL: Verify Before Recommending**
   - Don't assume based on code alone—customer input is essential
   - Acknowledge when classification is inferred vs. validated
   - Note that Kano categories shift over time (Attractive becomes Must-be)
   - Consider competitive context (your Must-be may be competitor's gap)

6. **Develop Prioritization Recommendations**
   - **Priority 1:** Fix Must-be gaps (causes dissatisfaction)
   - **Priority 2:** Optimize key Performance features (competitive advantage)
   - **Priority 3:** Add selected Attractive features (differentiation)
   - **Deprioritize:** Remove or simplify Indifferent features
   - **Urgent:** Remove or redesign Reverse features

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Classify features without customer input (even proxies)
- Assume all feature requests are Attractive (many are Must-be gaps)
- Ignore that categories shift over time (today's delight is tomorrow's expectation)
- Apply uniform classification across all customer segments
- Treat founder preferences as customer preferences
- Build Attractive features while Must-be features are broken

✅ **DO:**
- Use customer data (surveys, analytics, support) to validate classifications
- Acknowledge confidence level for each classification
- Consider segment-specific Kano curves
- Recognize competitive context affects classifications
- Regularly reassess as market evolves
- Prioritize Must-be completion before Attractive investment

## Confidence Levels

Rate each feature classification with a confidence level:

- **High Confidence:** Validated by customer survey or multiple data signals (usage + support + interviews)
- **Medium Confidence:** Supported by one data source or industry pattern
- **Low Confidence:** Inferred from code/logic only; needs validation

## Expected Output

A comprehensive Kano Model analysis including:
- Feature inventory with classifications
- Evidence supporting each classification
- Confidence ratings
- Prioritized development roadmap
- Recommendations for feature changes

### Output Format

```markdown
## Kano Model Analysis: [Product Name]

### Executive Summary
[3-5 sentences summarizing the feature landscape and key priorities]

### Kano Model Visualization

```
SATISFACTION
     ▲
     │                          ╱ Attractive
     │                        ╱   (delight zone)
     │                      ╱
     │    ─────────────────────── Performance
     │                    ╱       (competitive zone)
     │                  ╱
     │                ╱
─────┼───────────────────────────────────────▶ FULFILLMENT
     │              ╲
     │                ╲
     │                  ╲
     │                    ╲ Must-be
     │                      (expectation zone)
     ▼
```

### Feature Classification

#### Must-be (Basic) Features
| Feature | Status | Evidence | Confidence | Gap? |
|---------|--------|----------|------------|------|
| [Feature] | Complete | [Data] | High | No |

#### Performance Features
| Feature | Current Level | Competitor | Evidence | Confidence |
|---------|---------------|------------|----------|------------|
| [Feature] | [Level] | [Benchmark] | [Data] | High |

#### Attractive Features
| Feature | Status | Evidence | Confidence | Impact |
|---------|--------|----------|------------|--------|
| [Feature] | [Status] | [Data] | Medium | High |

#### Indifferent Features
| Feature | Usage | Evidence | Confidence | Recommendation |
|---------|-------|----------|------------|----------------|
| [Feature] | <1% | Analytics | High | Remove |

#### Reverse Features
| Feature | Issue | Evidence | Confidence | Recommendation |
|---------|-------|----------|------------|----------------|
| [Feature] | [Problem] | [Data] | High | Redesign |

### Priority Matrix

| Priority | Category | Features | Rationale |
|----------|----------|----------|-----------|
| P0 | Must-be gaps | [List] | Causing churn |
| P1 | Performance | [List] | Competitive advantage |
| P2 | Attractive | [List] | Differentiation |
| Deprioritize | Indifferent | [List] | Low value |
| Urgent | Reverse | [List] | Causing harm |

### Recommendations
[Prioritized action items]
```

## Example Output

```markdown
## Kano Model Analysis: CloudDocs (Document Management SaaS)

### Executive Summary

CloudDocs has solid Must-be features (documents save, sync works) but critical gaps in Performance features (search is slow, storage limits are restrictive). The product has one standout Attractive feature (AI document summaries) that drives word-of-mouth, but several Indifferent features are adding complexity without value. Most concerning: the forced onboarding tutorial is a Reverse feature causing user frustration. **Priority: Fix search performance, remove forced tutorial, then invest in AI features.**

### Kano Model Visualization

```
SATISFACTION
     ▲
     │                           AI Summaries ★
     │                          ╱ (delighting users)
     │         Smart Folders ◇ ╱
     │                      ╱
     │    ─────────────────────────────────────
     │         Search ⚠️     ╱ Storage ⚠️       Performance
     │    (slow)        ╱    (too limited)
     │                ╱
─────┼───────────────────────────────────────────────▶ FULFILLMENT
     │              ╲
     │    Sync ✓      ╲ Save ✓
     │    Security ✓    ╲
     │                    ╲ Must-be
     │      Onboarding Tutorial ✗ (annoying users)
     ▼

Legend: ✓ Complete | ⚠️ Needs improvement | ◇ Opportunity | ★ Differentiator | ✗ Problem
```

---

### Feature Classification

#### Must-be (Basic) Features
*These features are expected. Absence = extreme dissatisfaction. Presence = neutral.*

| Feature | Status | Evidence | Confidence | Gap? |
|---------|--------|----------|------------|------|
| Document saves correctly | ✓ Complete | 0 support tickets on data loss | High | No |
| Sync across devices | ✓ Complete | 99.9% sync success rate | High | No |
| Basic security (encryption) | ✓ Complete | SOC2 compliance achieved | High | No |
| File organization (folders) | ✓ Complete | Standard feature, no complaints | High | No |
| Share documents externally | ✓ Complete | 45% of users use sharing | High | No |
| Mobile access | ⚠️ Partial | Mobile app rated 2.8 stars; "buggy" complaints | High | **Yes** |
| Offline access | ⚠️ Partial | #3 support request: "Can't access docs on plane" | High | **Yes** |

**Analysis:**
Core document management is solid. Two Must-be gaps are causing dissatisfaction:
1. **Mobile app quality** - Users expect mobile to work; current bugs are causing churn
2. **Offline access** - Increasingly expected for document tools; competitors have it

**Code Evidence:**
```typescript
// Mobile app: Known issues in src/mobile/
// TODO: Fix sync race condition causing data conflicts
// TODO: Address memory leak on large documents

// Offline: Stub implementation only
src/offline/
├── cache_manager.ts    // Basic caching, no conflict resolution
└── sync_queue.ts       // Not implemented: "// Phase 2"
```

---

#### Performance Features
*Satisfaction is proportional to performance. Better = happier. Competitive battleground.*

| Feature | Current Level | Competitor Benchmark | Evidence | Confidence | Gap? |
|---------|---------------|---------------------|----------|------------|------|
| Search speed | 3.2s average | Notion: <1s | Analytics, complaints | High | **Yes** |
| Storage per user | 5GB free, 50GB paid | Dropbox: 2TB | Churn reason #2 | High | **Yes** |
| Upload speed | 2MB/s | Box: 10MB/s | Support tickets | Medium | Moderate |
| Number of integrations | 12 | Zapier: 3000+ | Feature requests | Medium | Yes |
| Collaboration (simultaneous editing) | 5 users | Google Docs: 100+ | Enterprise feedback | Medium | Segment-specific |

**Analysis:**
Two critical Performance gaps are hurting competitiveness:
1. **Search speed** - 3.2s is painfully slow; users notice and complain
2. **Storage limits** - 5GB free is below market; causes upgrade friction

**Code Evidence:**
```typescript
// Search: Full-text search on every query (no indexing)
// src/search/document_search.ts
async function search(query: string) {
  // WARNING: This scans all documents - O(n) complexity
  const allDocs = await this.getAllUserDocuments();
  return allDocs.filter(doc =>
    doc.content.toLowerCase().includes(query.toLowerCase())
  );
}

// Storage: Hardcoded limits, no optimization
const STORAGE_LIMITS = {
  free: 5 * GB,      // Industry is moving to 15GB+
  paid: 50 * GB,     // Competitors offer 2TB
};
```

---

#### Attractive (Excitement) Features
*Not expected. Presence = delight. Absence = neutral. Differentiators.*

| Feature | Status | Evidence | Confidence | Impact |
|---------|--------|----------|------------|--------|
| **AI Document Summaries** | ✓ Launched | NPS mentions "love the summaries", 34% of users use daily | High | **High** |
| Smart Folders (auto-organize) | ◇ Beta | Beta users: "This is magic", 89% retention vs 72% control | Medium | High |
| Document version comparison | ✓ Launched | 12% usage, positive feedback from power users | Medium | Medium |
| Template suggestions | ◇ Planned | Competitor launched; market expects eventually | Low | Medium |

**Analysis:**
AI Summaries is a genuine Attractive feature driving differentiation and word-of-mouth. Smart Folders shows promise in beta. These are strategic advantages worth investing in.

**Code Evidence:**
```typescript
// AI Summaries - Well-implemented, users love it
// src/ai/summarizer.ts
export class DocumentSummarizer {
  async summarize(doc: Document): Promise<Summary> {
    // Claude API integration - high quality results
    // Caching implemented for cost efficiency
    // Usage tracking shows 34% DAU
  }
}

// Smart Folders - Beta, showing strong results
// src/ai/auto_organize.ts
// Beta metrics: 89% retention vs 72% control group
```

**Warning:** Attractive features decay to Performance (expected) over time. AI summaries will become table-stakes within 1-2 years as competitors copy.

---

#### Indifferent Features
*Users don't care whether present or absent. Candidates for removal.*

| Feature | Usage | Evidence | Confidence | Recommendation |
|---------|-------|----------|------------|----------------|
| Custom themes (12 options) | 2% | Analytics | High | Simplify to 3 |
| Export to .rtf format | 0.3% | Analytics | High | Remove |
| Detailed activity log | 1% | Analytics, no requests | High | Hide in settings |
| Custom keyboard shortcuts | 4% | Analytics | Medium | Keep but don't invest |
| Document password protection | 3% | Analytics, some enterprise use | Medium | Keep for enterprise |
| Print formatting options | 1.5% | Analytics, print is dying | High | Minimal maintenance |

**Analysis:**
These features consume development and maintenance resources without customer value. 6 features used by <5% of users = significant complexity for minimal benefit.

**Code Evidence:**
```typescript
// Themes: 12 themes, 847 lines of CSS, 2% usage
// src/themes/
├── ocean.css
├── forest.css
├── sunset.css
├── ... (9 more themes nobody uses)

// RTF Export: Complex converter, 0.3% usage
// src/export/rtf_converter.ts - 1,200 lines for 0.3% of users
```

**Recommendation:** Remove 3 lowest-usage features, simplify themes to Light/Dark/System, reduce maintenance burden.

---

#### Reverse Features
*Presence causes dissatisfaction. Should be removed or redesigned.*

| Feature | Issue | Evidence | Confidence | Recommendation |
|---------|-------|----------|------------|----------------|
| **Forced onboarding tutorial** | Can't skip, 5 minutes, condescending | 23% bounce rate, angry reviews | High | **Make skippable** |
| Upgrade prompts (modal) | Interrupts workflow | "Annoying" in 15% of churn surveys | High | Reduce frequency |
| Auto-save notification | Toast every 30 seconds | Support complaints | Medium | Silent save |
| "Tips" sidebar | Can't permanently dismiss | Feature request: "let me hide this" | Medium | Add dismiss option |

**Analysis:**
The forced onboarding tutorial is the most damaging. New users who could self-serve are forced through a 5-minute tutorial, causing 23% to abandon signup. This is actively harming acquisition.

**Code Evidence:**
```typescript
// Forced tutorial - blocking user progress
// src/onboarding/tutorial.tsx
const Tutorial = () => {
  // NOTE: No skip option by design (PM decision from 2023)
  // TODO: This is causing bounces - see analytics
  const [step, setStep] = useState(0);
  const steps = [...]; // 8 mandatory steps

  // User MUST complete all steps to access app
  if (step < steps.length) {
    return <TutorialStep step={steps[step]} />;
  }
  return <App />;
};
```

**Recommendation:** Make tutorial skippable immediately. Offer guided tour as option, not requirement.

---

### Priority Matrix

| Priority | Category | Features | Rationale | Effort |
|----------|----------|----------|-----------|--------|
| **P0 (Urgent)** | Reverse | Forced onboarding tutorial | 23% bounce rate = revenue loss | Small |
| **P0** | Must-be gap | Mobile app stability | 2.8 star rating hurts acquisition | Medium |
| **P1** | Performance | Search speed (indexing) | 3.2s is embarrassingly slow | Large |
| **P1** | Performance | Storage limits increase | Churn reason #2 | Small (cost decision) |
| **P2** | Must-be gap | Offline access | Growing expectation | Large |
| **P2** | Attractive | Smart Folders GA | Beta shows strong impact | Medium |
| **P3** | Reverse | Reduce upgrade modal frequency | Annoying but less urgent | Small |
| **Deprioritize** | Indifferent | Custom themes | Keep 3, remove 9 | Small (removal) |
| **Deprioritize** | Indifferent | RTF export | Remove entirely | Small (removal) |
| **Protect** | Attractive | AI Summaries | Key differentiator | Ongoing |

---

### Recommendations

#### Immediate Actions (This Sprint)

1. **Make onboarding tutorial skippable**
   - Remove forced flow; offer optional guided tour
   - Expected impact: Reduce bounce rate from 23% to ~10%
   - Effort: 2-3 days

2. **Reduce upgrade modal frequency**
   - Change from every session to max 1x/week
   - Effort: 1 day

#### Short-Term (Next Quarter)

3. **Fix mobile app stability**
   - Address sync race condition and memory leak
   - Target: 4.0+ app store rating
   - Effort: 4-6 weeks

4. **Implement search indexing**
   - Replace full-scan with Elasticsearch/Algolia
   - Target: <500ms search response
   - Effort: 6-8 weeks

5. **Increase storage limits**
   - Free: 5GB → 15GB (match market)
   - Paid: 50GB → 200GB
   - Effort: Business decision (cost increase)

#### Medium-Term (Next 2 Quarters)

6. **Ship Smart Folders to GA**
   - Beta results are strong; expand
   - Effort: 4 weeks

7. **Implement offline access**
   - Full offline with conflict resolution
   - Effort: 8-12 weeks

#### Simplification Actions

8. **Remove/simplify Indifferent features**
   - Remove RTF export (0.3% usage)
   - Reduce themes from 12 to 3
   - Hide activity log in advanced settings
   - Effort: 2 weeks total, reduces ongoing maintenance

---

### Kano Decay Warning

**Features at risk of category shift:**

| Feature | Current | Shifting To | Timeline | Action |
|---------|---------|-------------|----------|--------|
| AI Summaries | Attractive | Performance | 12-18 months | Invest to stay ahead |
| Real-time collaboration | Attractive | Must-be | Already happening | Must improve |
| Mobile app | Must-be | Competitive liability | Now | Fix urgently |

AI features are being rapidly copied. What delights today will be expected tomorrow. Continuous investment in Attractive features is necessary to maintain differentiation.

---

### Validation Needs

**High-confidence classifications** (validated by data):
- Search speed, storage limits, mobile quality (support + analytics + churn data)
- AI Summaries (usage data + NPS mentions)
- Forced tutorial (bounce rate + reviews)

**Medium-confidence** (partial data):
- Smart Folders (beta only, small sample)
- Upgrade modal annoyance (churn survey, may be biased)

**Recommended validation:**
- Run Kano survey for 10 key features (functional/dysfunctional questions)
- Segment analysis: Are classifications different for Enterprise vs SMB?
- Competitive benchmark: Which Performance features matter most?
```

## Customization Guide

- **For B2B Enterprise:** Must-be features often include compliance, SSO, audit logs—validate with procurement
- **For B2C Consumer:** Attractive features drive virality; prioritize delight over optimization
- **For Mature Products:** Focus on Performance optimization; Attractive features harder to find
- **For New Products:** Ensure Must-be features are solid before investing in Attractive

## Techniques Used

- **ST-01 (Clear Objective Statement):** Explicit goal of classifying features by customer satisfaction impact
- **ST-02 (Structured Sequential Instructions):** Systematic feature inventory and classification process
- **DS-01 (Framework Application):** Direct application of Kano Model categories
- **DS-06 (Prioritization Guidance):** Clear priority matrix based on Kano principles
- **QA-02 (Adversarial Thinking):** False-positive prevention ensures classifications are evidence-based

## Related Prompts

- [Jobs to Be Done Analysis](jobs_to_be_done_analysis.md) - Understand underlying customer needs
- [Product-Market Fit Analysis](product_market_fit_analysis.md) - Evaluate overall product-market fit
- [Value Proposition Canvas Analysis](value_proposition_canvas_analysis.md) - Map features to customer value
- [Competitive Positioning Map](competitive_positioning_map.md) - Compare features to competitors
