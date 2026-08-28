---
title: "Customer Journey Map Analysis for Codebase"
category: software-engineering/analysis/business
description: "Map a codebase to the stages of the customer journey, evaluate the experience and likely emotional state at each stage, surface pain points and gaps, and recommend prioritized improvements grounded in observable code evidence."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - business-analysis
  - customer-journey
  - user-experience
  - codebase-analysis
  - journey-mapping
updated: "2026-06-07"
related_prompts:
  - domain-software-engineering/analysis/business/business_impact_analysis.md
  - domain-software-engineering/analysis/business/stakeholder_persona_generation.md
  - domain-software-engineering/analysis/business/tech_adoption_lifecycle_analysis.md
---

# Customer Journey Map Analysis for Codebase

**Objective:** Map the parts of a codebase to the stages of the customer journey, evaluate how each stage supports (or frustrates) the user, and produce a prioritized set of improvements grounded in what the code actually does.

**When to use:**
- Product/engineering leaders want to see how the build supports the end-to-end user experience.
- You inherited a codebase and need to understand which flows serve which journey stage.
- Planning UX or conversion improvements and need to locate the friction in code, not assumptions.
- Preparing a roadmap that ties technical work to experience outcomes.

**When NOT to use:**
- You have no instrumentation or domain context — emotional-state and drop-off claims will be speculation.
- You need quantitative funnel analysis — pull real analytics instead of inferring from code.
- The codebase has no user-facing surface (pure infra/library).

**Audience:** Product managers, engineering managers, UX practitioners, and founders connecting code to experience.

---

## Inputs / Context

The user should supply (or the analysis should flag what is missing):

1. **The codebase** (or a feature/route/component inventory) to analyze.
2. **Product context:** what the product does and who the primary users are.
3. **Journey scope:** full journey vs. a specific stage (e.g., onboarding only).
4. **Known metrics** if any (conversion, drop-off, support volume, NPS) — these ground experience and emotion claims.
5. **Decision the map feeds:** UX investment, conversion work, roadmap prioritization.

---

## Constraints

### Must
- Tie every journey-stage claim to **observable code evidence** (a component, route, flow, instrumentation point) — cite the file/module.
- Distinguish **fact** (this flow exists / collects 12 fields / has no analytics) from **inference** (users *probably* feel overwhelmed here).
- Evaluate each stage across the standard dimensions: **what the user can do, what feedback they get, friction/delight, and transition to the next stage.**
- **Prioritize** recommendations (e.g., P0/P1/P2 or impact × effort), not a flat list.
- Where emotional state or drop-off is asserted without metrics, **label it as hypothesis** and name the data that would confirm it.

### Must Not
- Invent drop-off rates, completion percentages, or emotion data not supplied by the user.
- Present inferred user feelings as measured fact.
- Recommend changes on one stage while ignoring downstream effects on adjacent stages.
- Treat the presence of a feature as proof it works well.

---

## Instructions

1. **Inventory user-facing components.** Identify pages, routes, flows, and components and group them by what part of the experience they serve. Cite files/modules.
2. **Define journey stages.** Select the stages the product actually supports (e.g., Awareness, Consideration, Decision, Onboarding, Usage, Support, Retention, Advocacy). Drop stages the code does not touch.
3. **Map code to stages.** For each stage, list the supporting components and what they let the user do, what feedback they return, and how they hand off to the next stage.
4. **Assess experience and emotion.** For each stage note likely friction or delight. Label emotion/drop-off as evidence-based (if metrics supplied) or hypothesis.
5. **Identify touchpoints and gaps.** UI elements, inputs/outputs, notifications, integrations; flag stages with thin or missing code support.
6. **Prioritize improvements.** Rank recommendations by user impact and effort; tie each to a specific gap and the stage it affects.
7. **Self-check (verification step).** Re-read the output: any invented metric? Any inferred emotion stated as fact? Are adjacent-stage effects considered? Name the analytics that would sharpen the map.

---

## False-Positive Prevention

❌ **DON'T:**
- State "45% drop off at onboarding" when no analytics were supplied.
- Assume a stage is healthy just because the code exists.
- Present inferred user emotion ("users feel anxious here") as measured fact.
- Deliver a stage-by-stage description with no prioritized recommendations.
- Optimize one stage in isolation while breaking the handoff to the next.

✅ **DO:**
- Label each experience/emotion claim **evidence-based** (from metrics) or **hypothesis** (inference).
- Cite the specific component/file behind each mapping.
- Acknowledge stages the code can't fully reveal and name the data needed.
- Synthesize into a ranked, actionable improvement list.
- Suggest validation steps (instrument the onboarding flow, pull checkout funnel) before high-stakes UX investment.

---

## Output Format

```
# Customer Journey Map Analysis: [Product / Codebase]

## Context & Evidence Basis
- Product: [...]
- Primary users: [...]
- Metrics available: [list, or "none — emotion/drop-off below are hypotheses"]

## Journey Overview
[Stage list with one-line summary per stage]

## Stage-by-Stage Map
### [Stage name]
- Code components (file/module): [...]
- What the user can do / feedback received: [...]
- Friction / delight: [...] (evidence / hypothesis)
- Transition to next stage: [...]

## Journey Summary Matrix
| Stage | Code Maturity | Experience Signal | Basis | Priority |
|-------|---------------|-------------------|-------|----------|
| ...   | %/H/M/L       | friction/delight  | evidence / hypothesis | P0/P1/P2 |

## Prioritized Improvements
- [P0] [Improvement] → stage, gap addressed, rough effort
- [P1] ...

## Gaps & Data Needed
- [What the code can't reveal, and the analytics that would]

## Self-Check
- Invented metrics: [none / list]
- Emotion/drop-off labeled: [yes/no]
```

---

## Example Output

```
# Customer Journey Map Analysis: ExampleCo SaaS Platform (placeholder)

## Context & Evidence Basis
- Product: team workflow SaaS (placeholder)
- Primary users: small-team admins and individual contributors
- Metrics available: none supplied — emotion/drop-off below are labeled hypotheses

## Journey Overview
Awareness → Consideration → Decision (Checkout) → Onboarding → Usage → Support → Retention

## Stage-by-Stage Map
### Awareness
- Code components: src/pages/LandingPage.tsx (hero, feature showcase, static testimonials)
- What the user can do: read value prop, click "Start Free Trial"; feedback is purely static
- Friction / delight: testimonials are hardcoded, not live (evidence: no API call in component); reduces trust signal (hypothesis)
- Transition: CTA routes to /signup

### Decision (Checkout)
- Code components: src/pages/CheckoutFlow.tsx (4-step wizard), src/forms/AccountForm.tsx
- What the user can do: select plan, create account, pay, confirm
- Friction: account form requires 12 fields, 7 marked required that are non-essential (evidence: AccountForm.tsx field list); likely raises abandonment (hypothesis — no funnel data)
- Transition: confirmation screen has no welcome/next-step (evidence: no post-submit content)

### Onboarding
- Code components: src/components/Onboarding/OnboardingFlow.tsx (4 steps, skip button)
- What the user can do: watch welcome video, set up profile, invite team, create first project
- Friction: profile step re-collects data already taken at checkout (evidence: duplicate fields); first-project wizard is complex (hypothesis: high day-1 drop-off)
- Transition: lands in main app workspace

## Journey Summary Matrix
| Stage | Code Maturity | Experience Signal | Basis | Priority |
|-------|---------------|-------------------|-------|----------|
| Awareness | Medium | static social proof | evidence | P2 |
| Decision | Medium | 12-field form friction | evidence + hypothesis | P0 |
| Onboarding | Low | duplicate data, complex first project | evidence + hypothesis | P0 |
| Usage | High | shortcuts + celebration moments | evidence | P3 |

## Prioritized Improvements
- [P0] Reduce account form to 4 essential fields (email, password, name, company) — collect the rest during onboarding. Low effort; addresses checkout friction.
- [P0] Remove duplicate profile collection in onboarding and simplify first-project to a templated example. Medium effort.
- [P2] Replace hardcoded testimonials with live, dated reviews. Low–medium effort.

## Gaps & Data Needed
- No funnel/drop-off instrumentation in checkout or onboarding → abandonment claims are directional, not measured.
- No event tracking on feature usage → "Usage" maturity is inferred from code richness, not real use.

## Self-Check
- Invented metrics: none (no percentages asserted).
- Emotion/drop-off labeled: yes — each row marks evidence vs. hypothesis.
- Next data to pull: step-level funnel events for checkout and onboarding.
```

---

## Verification

- [ ] Every stage ties to an observable code signal (file/module cited).
- [ ] Each experience/emotion claim labeled evidence-based or hypothesis.
- [ ] No invented drop-off, completion, or emotion figures.
- [ ] Each stage covers actions, feedback, friction/delight, and transition.
- [ ] Recommendations are prioritized with rationale and effort.
- [ ] Adjacent-stage effects considered before recommending changes.
- [ ] Gaps and the data needed to resolve them are listed.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the task as mapping code to journey stages and producing prioritized experience improvements.
- **RT-02 (Multi-Dimensional Analysis Framework):** Evaluates each stage across actions, feedback, friction/delight, and transition.
- **DS-02 (Evidence-Based Decision Making):** Requires every stage and experience claim to trace to code evidence or supplied metrics, labeling inference.
- **DS-06 (Prioritization and Severity Guidance):** Produces a ranked (P0/P1/P2) improvement list.
- **QA-01 (Self-Critique Triggers):** Final self-check audits for invented metrics and emotion stated as fact.

---

## Related Prompts

- `domain-software-engineering/analysis/business/business_impact_analysis.md` — Translate features into prioritized business value.
- `domain-software-engineering/analysis/business/stakeholder_persona_generation.md` — Infer the personas whose journeys these flows serve.
- `domain-software-engineering/analysis/business/tech_adoption_lifecycle_analysis.md` — Position the product in its adoption lifecycle.
