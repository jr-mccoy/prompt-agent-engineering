---
title: "Business Model Canvas Analysis for Codebase"
category: software-engineering/analysis/business
description: "Analyze a codebase using the Business Model Canvas framework to understand its business implications, monetization potential, and strategic alignment"
techniques:
  - ST-01
  - ST-02
  - DS-01
  - RT-02
  - QA-02
difficulty: intermediate
tags:
  - analysis
  - business-analysis
  - strategic-planning
  - business-model
  - monetization
updated: "2026-01-25"
related_prompts:
  - domain-software-engineering/analysis/business/lean_canvas_analysis.md
  - domain-software-engineering/analysis/business/value_proposition_canvas_analysis.md
  - domain-software-engineering/analysis/business/customer_journey_map_analysis.md
---

# Business Model Canvas Analysis for Codebase

**Objective:** Analyze the codebase using the Business Model Canvas framework to understand its business implications and potential.

## When to Use

- Use when: Evaluating whether a codebase can support a viable business model
- Use when: Planning monetization strategy for a new product or feature
- Use when: Assessing acquired code for business potential during M&A
- Use when: Identifying gaps between technical capabilities and business requirements
- Use when: Presenting technical assets to investors or business stakeholders
- Don't use when: You need immediate technical improvements (use architecture analysis instead)
- Don't use when: Evaluating code quality (use quality analysis prompts)

**Instructions:**

1. Review the codebase and identify key features and functionalities.
2. For each element of the Business Model Canvas, analyze how the codebase contributes:

   a. Value Propositions:
      - What user problems does the code solve?
      - What value does it deliver to users?

   b. Customer Segments:
      - Who are the target users/customers for this code?
      - Are there different user groups with distinct needs?

   c. Channels:
      - How does the code facilitate reaching users?
      - Are there features for distribution or communication?

   d. Customer Relationships:
      - How does the code support user engagement and retention?
      - Are there features for customer support or community building?

   e. Revenue Streams:
      - How could this code generate revenue?
      - Are there monetization features implemented?

   f. Key Resources:
      - What are the critical technical assets in the codebase?
      - Are there unique algorithms or data structures?

   g. Key Activities:
      - What are the core functionalities that keep the application running?
      - What ongoing processes does the code support?

   h. Key Partnerships:
      - Does the code integrate with external services or APIs?
      - Are there dependencies on third-party libraries?

   i. Cost Structure:
      - What are the main cost drivers in running this code?
      - Are there features aimed at optimizing costs?

3. Identify potential gaps or opportunities in the business model based on the codebase analysis.

4. Suggest improvements or new features that could enhance the business model.

5. **CRITICAL: Verify Each Finding**
   - Support every claim with specific code evidence (file paths, dependencies, configurations)
   - Distinguish between facts (code shows X) and inferences (X implies business opportunity Y)
   - **Assign confidence level:** High/Medium/Low for each business model element assessment
   - Cross-reference technical capabilities with market viability before stating opportunities

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Assume revenue potential without evidence of payment integration or monetization hooks in the code
- Claim "key partnerships" based solely on npm dependencies (most are utility libraries, not strategic partners)
- List every API integration as a "channel" when most are internal infrastructure
- Present technical features as "value propositions" without evidence of user-facing benefits
- Overstate customer segments based on generic user roles in the code
- Assume cost structure from code complexity (infrastructure costs depend on usage patterns)

✅ **DO:**
- Cite specific code paths that enable each business model element (payment flows, subscription logic, etc.)
- Distinguish between "currently implemented" vs "could be implemented" capabilities
- Validate customer segment claims with actual user data if available, or label as hypothesis
- Include confidence levels: High (code directly supports), Medium (code could support with modification), Low (speculation)
- Separate "technical dependencies" from "strategic partnerships" in Key Partners analysis
- Quantify where possible (e.g., "supports 3 pricing tiers" vs "has subscription capability")

**Expected Output:** A comprehensive analysis of the codebase using the Business Model Canvas framework, including:
- Assessment of each canvas element with specific code evidence
- **Confidence levels** for each finding (High/Medium/Low)
- Clear distinction between implemented vs potential capabilities
- Gap analysis with prioritized recommendations
- Strategic recommendations with implementation effort estimates

**Example Output:**

```markdown
## Business Model Canvas Analysis: Learning Management System (LMS)

### Canvas Overview

```
┌─────────────────┬─────────────────┬─────────────────┬─────────────────┬─────────────────┐
│  Key Partners   │ Key Activities  │  Value Props    │ Customer Rels   │ Customer Segs   │
│                 │                 │                 │                 │                 │
│ • AWS           │ • Course mgmt   │ • Self-paced    │ • Automated     │ • Enterprises   │
│ • Stripe        │ • User auth     │   learning      │   onboarding    │ • SMBs          │
│ • SendGrid      │ • Analytics     │ • Progress      │ • Email support │ • Educators     │
│ • Vimeo API     │ • Content CDN   │   tracking      │ • Community     │                 │
│                 │                 │ • Certifications│   forum         │                 │
├─────────────────┴─────────────────┼─────────────────┴─────────────────┴─────────────────┤
│        Key Resources              │                     Channels                         │
│                                   │                                                      │
│ • Course content engine           │ • Web app (responsive)                              │
│ • Video transcoding pipeline      │ • Mobile apps (iOS/Android)                         │
│ • User progress database          │ • Email marketing automation                        │
│ • ML recommendation engine        │ • API for integrations                              │
├───────────────────────────────────┼──────────────────────────────────────────────────────┤
│        Cost Structure             │                  Revenue Streams                     │
│                                   │                                                      │
│ • Cloud hosting (~40%)            │ • Subscription tiers ($29/$79/$199/mo)              │
│ • Video storage/CDN (~25%)        │ • Enterprise licensing                              │
│ • Payment processing (~3%)        │ • Course marketplace (20% commission)               │
│ • Support team (~20%)             │ • White-label licensing                             │
└───────────────────────────────────┴──────────────────────────────────────────────────────┘
```

---

### Detailed Analysis

#### Value Propositions

**Code Evidence:**
```typescript
// Self-paced learning with progress tracking
class CourseProgress {
  async updateProgress(userId: string, lessonId: string) {
    await this.progressRepo.save({
      userId,
      lessonId,
      completedAt: new Date(),
      timeSpent: this.calculateTimeSpent()
    });

    // Check for certificate eligibility
    if (await this.isCourseComplete(userId)) {
      await this.certificateService.generate(userId);
    }
  }
}
```

| Value Prop | Code Support | Strength |
|------------|--------------|----------|
| Self-paced learning | ✓ Full | Strong |
| Progress tracking | ✓ Full | Strong |
| Certifications | ✓ Full | Strong |
| Mobile access | ✓ Responsive | Moderate |
| Offline learning | ✗ Missing | Gap |

---

#### Customer Segments

**Identified from Codebase:**
```typescript
// User roles and organizations
enum UserRole {
  STUDENT = 'student',
  INSTRUCTOR = 'instructor',
  ADMIN = 'admin',
  ENTERPRISE_ADMIN = 'enterprise_admin'
}

// Organization types suggest target segments
interface Organization {
  type: 'enterprise' | 'smb' | 'education' | 'individual';
  seats: number;
  customBranding: boolean;  // Enterprise feature
}
```

**Segment Analysis:**
| Segment | Revenue % | Code Support | Notes |
|---------|-----------|--------------|-------|
| Enterprise | 45% | Strong | SSO, custom branding, analytics |
| SMB | 35% | Moderate | Team management, basic analytics |
| Individual Educators | 15% | Moderate | Course creation tools |
| Individual Learners | 5% | Basic | Consumer features limited |

---

#### Revenue Streams

**Code Evidence:**
```typescript
// Subscription management
const subscriptionPlans = {
  starter: { price: 29, courses: 10, students: 100 },
  professional: { price: 79, courses: 50, students: 500 },
  enterprise: { price: 199, courses: 'unlimited', students: 'unlimited' }
};

// Marketplace commission
async processCourseSale(sale: CourseSale) {
  const platformFee = sale.price * 0.20;  // 20% commission
  const instructorPayout = sale.price - platformFee;
  await this.paymentService.split(sale, [
    { recipient: 'platform', amount: platformFee },
    { recipient: sale.instructorId, amount: instructorPayout }
  ]);
}
```

---

#### Key Partnerships

**Third-Party Integrations Found:**
```typescript
// External service dependencies
const integrations = {
  payments: ['Stripe'],           // Payment processing
  video: ['Vimeo', 'YouTube'],    // Video hosting
  email: ['SendGrid'],            // Transactional email
  storage: ['AWS S3'],            // File storage
  auth: ['Auth0'],                // SSO for enterprise
  analytics: ['Mixpanel']         // User analytics
};
```

**Partnership Risk Assessment:**
| Partner | Criticality | Alternatives | Risk |
|---------|-------------|--------------|------|
| Stripe | High | PayPal, Adyen | Low |
| AWS S3 | High | GCP, Azure | Medium |
| Vimeo API | Medium | Mux, Cloudflare | Low |
| Auth0 | Medium | Cognito, Firebase | Low |

---

### Gap Analysis

| Canvas Element | Current State | Gap | Opportunity |
|----------------|---------------|-----|-------------|
| Offline Learning | Not supported | High | Progressive Web App |
| Mobile Apps | Web only | Medium | Native iOS/Android |
| B2C Marketing | Minimal | High | Referral system |
| Community | Basic forum | Medium | Social learning features |
| Gamification | None | Medium | Badges, leaderboards |

---

### Recommendations

**Quick Wins:**
1. Add course completion certificates (code ready, UI needed)
2. Implement referral system for viral growth
3. Add basic gamification (completion badges)

**Strategic Investments:**
1. Build native mobile apps (estimated 3 months)
2. Add offline support via PWA (estimated 1 month)
3. Develop AI-powered course recommendations (estimated 2 months)
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Defines purpose of business model evaluation from codebase
- ST-02 (Structured Sequential Instructions) - Guides systematic analysis of all 9 canvas elements
- DS-01 (Framework Application) - Applies proven Business Model Canvas framework
- RT-02 (Multi-Dimensional Analysis) - Evaluates technical code from multiple business perspectives
- QA-02 (Adversarial Thinking) - False-positive prevention ensures evidence-based findings
- CM-01 (Explicit Context Framing) - Frames technical analysis within business strategy context

## Related Prompts

- [lean_canvas_analysis.md](lean_canvas_analysis.md) - Simplified canvas for startups focusing on problem-solution fit
- [value_proposition_canvas_analysis.md](value_proposition_canvas_analysis.md) - Deep dive on value propositions and customer jobs
- [customer_journey_map_analysis.md](customer_journey_map_analysis.md) - Understand customer touchpoints from codebase
- [swot_analysis.md](swot_analysis.md) - Strategic assessment complementing business model analysis
- [competitive_positioning_map.md](competitive_positioning_map.md) - Position your product against competitors