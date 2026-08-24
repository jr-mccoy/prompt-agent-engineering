---
title: "Solo Developer Skill Gap Assessment"
category: personal-development
description: "Assess skill gaps as a solo developer — map required skills across development, backend, design, marketing, business, and legal against current abilities, identify the most impactful skill to develop next, and find efficient learning paths"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
difficulty: intermediate
tags:
  - solo-developer
  - skills
  - career
  - learning
  - personal-development
updated: "2026-06-21"
related_prompts:
  - domain-personal-development/prompts/solo-dev/solo_dev_automation_audit.md
  - domain-personal-development/prompts/solo-dev/solo_dev_network_building.md
  - domain-personal-development/prompts/goals/goals_skill_breakdown_blueprint.md
  - domain-personal-development/prompts/agency/agency_skill_gap_reframe.md
---

# Solo Developer Skill Gap Assessment

**Objective:** Assess your skill gaps as a solo developer running an app business — mapping all required skills across Android development, backend/infrastructure, design, marketing, business operations, legal/compliance, and user support against your current ability levels, identifying the highest-impact skill to develop next based on your business stage, and producing an efficient learning plan that doesn't eat into development time.

**When to Use:** Use this prompt when feeling overwhelmed by the breadth of solo developer responsibilities, when deciding what to learn next, when evaluating whether to learn a skill or outsource/automate it, during quarterly planning, or when your business stage changes (pre-launch → post-launch → growth).

**Important context:** A solo developer must be "good enough" at many things, not excellent at everything. The goal is not to become an expert marketer AND expert designer AND expert backend engineer — it is to identify which skill gap is currently the biggest bottleneck to your business success and invest in closing that specific gap. The right skill to learn depends on your business stage: pre-launch requires different skills than growth-stage.

---

## Inputs / Context

Provide what you can so the recommendation targets your real bottleneck:

- **Your product / platform:** [e.g., Android app + Firebase, web SaaS]
- **Current business stage:** [ideation / building / pre-launch / post-launch / growth / sustain — or "unsure"]
- **Self-ratings:** [your 1-5 ratings from Step 1, or "help me self-rate"]
- **What feels like it's holding the business back right now:** [the symptom, in your words]
- **Time available for learning per week:** [realistically]

### Refusal logic (insufficient input)

- The "highest-impact skill" answer depends entirely on **business stage** — if the user cannot identify their stage, walk them through the Step 2 stage table before recommending anything to learn.
- If the user has not self-rated any skills, do not assume their levels; run Step 1 as a worksheet first. Do not invent ratings on their behalf.
- If the user names a desire to "learn everything," redirect: the prompt's job is to pick *one* bottleneck skill, not to validate broad upskilling. (For when a claimed skill gap is actually avoidance, point to `agency_skill_gap_reframe.md`.)

---

## Instructions

### Step 1: Skill Inventory

Rate yourself 1-5 on each skill area:

**1 = No knowledge** | **2 = Basic awareness** | **3 = Can do it slowly** | **4 = Competent** | **5 = Expert**

**Android Development:**
- [ ] Kotlin language proficiency: ___/5
- [ ] Jetpack Compose UI development: ___/5
- [ ] Architecture patterns (MVVM/MVI, Clean Architecture): ___/5
- [ ] Room database and data persistence: ___/5
- [ ] Testing (unit, UI, integration): ___/5
- [ ] Performance optimization (startup, rendering, memory): ___/5
- [ ] Accessibility (TalkBack, content descriptions): ___/5
- [ ] Build system (Gradle, version catalogs, CI/CD): ___/5

**Backend & Infrastructure:**
- [ ] Firebase (Firestore, Auth, Functions): ___/5
- [ ] Firebase security rules: ___/5
- [ ] GCP basics (monitoring, cost management): ___/5
- [ ] API design (REST or similar): ___/5
- [ ] Server-side logic (Cloud Functions, Cloud Run): ___/5

**Design:**
- [ ] UI/UX design principles: ___/5
- [ ] Material Design implementation: ___/5
- [ ] Design tool proficiency (Figma or similar): ___/5
- [ ] App icon and store screenshot creation: ___/5
- [ ] User research and usability testing: ___/5

**Marketing:**
- [ ] App Store Optimization (ASO): ___/5
- [ ] Content marketing (blog, social media): ___/5
- [ ] Analytics interpretation (Firebase, Play Console): ___/5
- [ ] User acquisition strategies: ___/5
- [ ] Email marketing: ___/5

**Business Operations:**
- [ ] Financial planning and budgeting: ___/5
- [ ] Pricing and monetization strategy: ___/5
- [ ] Legal basics (privacy policy, ToS, business entity): ___/5
- [ ] User support and communication: ___/5
- [ ] Product management (roadmap, prioritization): ___/5

### Step 2: Business Stage Assessment

Identify your current stage:

| Stage | Characteristics | Highest-Impact Skills |
|-------|----------------|---------------------|
| **Ideation** | No code yet, validating idea | Market research, MVP design, user research |
| **Building** | Active development, pre-launch | Android development, architecture, Firebase |
| **Pre-Launch** | App functional, preparing to ship | ASO, Play Store listing, legal compliance, testing |
| **Post-Launch (Early)** | First users, seeking product-market fit | Analytics, user support, feedback loops, iteration |
| **Growth** | Product-market fit, growing users | Marketing, monetization, scaling, performance |
| **Sustain** | Mature app, maintaining and growing | Maintenance, operations, cost optimization, retention |

### Step 3: Gap-Impact Analysis

For each skill rated 1-3, assess:

| Skill Gap | Current Level | Stage Relevance (H/M/L) | Business Impact if Improved | Learn vs Outsource |
|-----------|--------------|-------------------------|---------------------------|-------------------|
| ASO | 2 | H (Growth) | Direct download impact | Learn (recurring need) |
| UI Design | 2 | M (Building) | User experience, conversion | Outsource (occasional need) |
| Security Rules | 1 | H (All stages) | Data protection, compliance | Learn (ongoing responsibility) |

**Decision framework:**
- **Learn** if: Recurring need, core to your product, affordable learning time
- **Outsource** if: Occasional need, high skill ceiling, specialized (legal, design)
- **Automate** if: Repetitive, tools exist, doesn't require judgment
- **Skip** if: Not relevant to your business stage, low impact

### Step 4: Learning Plan

For the top 1-2 skills to develop:

```
Skill: [e.g., App Store Optimization]
Current Level: 2/5
Target Level: 4/5
Time Investment: 2 hours/week for 4 weeks

Week 1: Foundations
- Resource: [Specific resource — blog, course, documentation]
- Practice: Analyze 5 competitor app listings

Week 2: Apply Basics
- Resource: [Next learning step]
- Practice: Rewrite your app's title and description using ASO principles

Week 3: Advanced Techniques
- Resource: [Advanced resource]
- Practice: Set up A/B test for app listing

Week 4: Review and Iterate
- Measure: Compare download metrics before/after changes
- Decide: Continue investing or sufficient for now?
```

---

## Expected Output

1. **Skill Inventory** — rated across all domains
2. **Business Stage Assessment** — current stage and critical skills
3. **Top 3 Skill Gaps** — highest impact gaps with learn/outsource/automate recommendation
4. **Learning Plan** — 4-week plan for the #1 priority skill
5. **Outsource Plan** — for skills better handled by contractors
6. **Quarterly Review Schedule** — when to reassess skill gaps

---

## False-Positive Prevention

- ❌ Do NOT label a gap "critical" without tying it to the user's actual business stage and near-term needs.
- ❌ Do NOT recommend learning a skill that is cheaper and safer to outsource or buy at this stage.
- ❌ Do NOT confuse mere unfamiliarity with a true, business-blocking gap.
- ❌ Do NOT produce a learning plan longer than the user's stated weekly capacity — it will not be executed.
- ❌ Do NOT treat every gap as equally urgent — force a must-learn-now vs. defer split.
- ✅ DO distinguish skills the founder must hold personally from skills the business merely needs access to.
- ✅ DO surface the opportunity cost of each learning investment against shipping the actual product.

## Verification

Before delivering the assessment, confirm each of the following:

- [ ] The skill inventory spans all domains (dev, backend, design, marketing, business, legal/support) — not just technical.
- [ ] A specific business stage is identified, and the recommended skill is relevant to *that* stage.
- [ ] The #1 recommended skill maps to the user's stated current bottleneck, not just a low self-rating in isolation.
- [ ] Each top gap carries an explicit learn / outsource / automate / skip decision, with a reason.
- [ ] The learn-vs-outsource call weighs recurring need vs. one-time need (recurring → learn; specialized one-off → outsource).
- [ ] The learning plan is time-bounded (e.g., 4 weeks, N hrs/week) with concrete resources and practice steps — not open-ended.
- [ ] Only 1-2 skills are prioritized for active learning (a solo dev cannot close five gaps at once).
- [ ] No skill ratings or business-stage assumptions were invented on the user's behalf.

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Targets a single highest-impact skill gap rather than broad upskilling.
- **ST-02** (Structured Sequential Instructions) — Inventory → stage → gap-impact → learning plan.
- **RT-02** (Multi-Dimensional Analysis) — Rates skills across six domains and weighs stage relevance vs. business impact.
- **CM-01** (Explicit Context Framing) — Anchors the assessment to the user's product and business stage.
- **DS-06** (Prioritization and Severity Guidance) — Ranks gaps by impact and produces a top-3 with learn/outsource/automate calls.

---

## Related Prompts

- [solo_dev_automation_audit.md](../solo-dev/solo_dev_automation_audit.md) — When the answer to a gap is "automate" rather than "learn."
- [solo_dev_network_building.md](../solo-dev/solo_dev_network_building.md) — Use mentors/communities to accelerate closing a prioritized gap.
- [goals_skill_breakdown_blueprint.md](../goals/goals_skill_breakdown_blueprint.md) — Decompose the chosen skill into a concrete learning sequence.
- [agency_skill_gap_reframe.md](../agency/agency_skill_gap_reframe.md) — Check whether a claimed skill gap is real or is avoidance blocking shipping.
