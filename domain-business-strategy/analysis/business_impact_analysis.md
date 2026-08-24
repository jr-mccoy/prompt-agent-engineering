---
title: "Codebase Business Impact Analysis"
category: business-strategy/analysis
description: "Analyze a codebase to map its major features to concrete business value (revenue, cost, satisfaction, competitive advantage), prioritize them, and propose value-adding enhancements grounded in evidence rather than guesswork."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - business-analysis
  - business-impact
  - feature-prioritization
  - codebase-analysis
  - value-mapping
updated: "2026-06-07"
related_prompts:
  - domain-business-strategy/analysis/customer_journey_map_analysis.md
  - domain-business-strategy/analysis/stakeholder_persona_generation.md
  - domain-business-strategy/analysis/tech_adoption_lifecycle_analysis.md
---

# Codebase Business Impact Analysis

**Objective:** Translate the technical capabilities present in a codebase into a prioritized view of business value, so engineering and product leaders can see which features carry the most revenue, cost, satisfaction, and competitive weight — and where investment would most increase value.

**When to use:**
- Engineering/product leadership needs to defend or reprioritize a roadmap against business value.
- You inherited a codebase and need to understand what is actually load-bearing for the business.
- Planning a refactor/sunset and need to know which features are worth keeping or hardening.
- Preparing a build-vs-cut argument for a feature whose business case is unclear.

**When NOT to use:**
- You have no domain context about who uses the product or how it monetizes (the analysis will be speculation).
- You need rigorous financial modeling (unit economics, LTV/CAC) — use a dedicated market/finance prompt.
- The codebase is a library/internal tool with no direct business-facing value to map.

**Audience:** Engineering managers, technical product managers, founders/CTOs, and architects making prioritization or investment decisions.

---

## Inputs / Context

The user should supply (or the analysis should explicitly flag what is missing):

1. **The codebase** (or a feature inventory / module list) to analyze.
2. **Product context:** what the product does, who pays for it, and how it makes money.
3. **Business goals** the analysis feeds (growth, retention, cost reduction, fundraising, M&A).
4. **Known metrics** if any (usage, conversion, churn, support load) — these ground impact claims.
5. **Scope:** whole product vs. a specific area; depth (quick scan vs. deep dive).

---

## Constraints

### Must
- Map every business-impact claim to **observable evidence** in the code or supplied metrics (a feature's existence, complexity, integration points, instrumentation) — not to assumed market behavior.
- Distinguish clearly between **fact** (this feature exists / handles payments / is heavily instrumented) and **inference** (this *probably* drives revenue).
- Rate impact across **four dimensions**: revenue generation, cost savings, customer satisfaction, competitive advantage.
- **Prioritize** features using a transparent scheme (e.g., impact × confidence, or impact vs. effort).
- Flag features where business value **cannot be assessed from the code** and state what data would resolve it.

### Must Not
- Invent revenue figures, usage numbers, or market sizing not supplied by the user.
- Present inferred impact as established fact.
- Recommend building/cutting based on a single dimension without acknowledging tradeoffs.
- Treat code volume or complexity as a proxy for business value.

---

## Instructions

1. **Inventory features.** Identify major features/functionalities from the codebase (modules, routes, services, key flows). Group into a clean feature list.
2. **Establish evidence per feature.** For each, note observable signals: payment/billing integration, third-party APIs, instrumentation/analytics, auth gating, prominence in the UI flow. Cite the file/module.
3. **Assess four-dimension impact.** For each feature, rate (High/Medium/Low) on:
   - Revenue generation potential
   - Cost-saving opportunity
   - Customer satisfaction contribution
   - Competitive advantage
   Attach a one-line rationale and label each as evidence-based or inferred.
4. **Assign confidence.** Note how much of the rating rests on code evidence vs. domain inference.
5. **Prioritize.** Rank features by business value, combining impact and confidence (and effort, if enhancement-focused). Produce a clear ordered list or matrix.
6. **Identify enhancement opportunities.** Suggest enhancements/new features that would raise value, tied to a specific dimension and a gap you observed.
7. **Self-check (verification step).** Re-read the output: is any number invented? Is any inference dressed as fact? Are gaps acknowledged? List what additional data (analytics, revenue by feature) would sharpen the analysis.

---

## False-Positive Prevention

❌ **DON'T:**
- State "this feature drives 40% of revenue" with no supplied data.
- Assume a complex/large module is high-value just because it is large.
- Present inference ("users probably love this") as a measured fact.
- Deliver a feature dump with ratings but no prioritization or synthesis.
- Recommend cutting a feature on one dimension while ignoring that it gates retention.

✅ **DO:**
- Label each impact claim as **evidence-based** (from code/metrics) or **hypothesis** (domain inference).
- Cite the specific module/file behind each evidence claim.
- Acknowledge where the code cannot reveal business value and name the data that would.
- Synthesize into a ranked priority list with rationale.
- Suggest validation steps (instrument feature X, pull conversion for flow Y) before high-stakes calls.

---

## Output Format

```
# Business Impact Analysis: [Product / Codebase]

## Context & Evidence Basis
- Product: [...]
- Monetization: [...]
- Metrics available: [list, or "none — impact ratings are inference-heavy"]

## Feature Impact Matrix
| Feature | Evidence (file/module) | Revenue | Cost Save | Satisfaction | Competitive | Confidence | Basis |
|---------|------------------------|---------|-----------|--------------|-------------|------------|-------|
| ...     | ...                    | H/M/L   | H/M/L     | H/M/L        | H/M/L       | H/M/L      | evidence / inference |

## Prioritized Features (highest business value first)
1. [Feature] — [why ranked here]
2. ...

## Enhancement Opportunities
- [Enhancement] → dimension targeted, gap it addresses, rough effort

## Gaps & Data Needed
- [What the code can't tell us, and the data that would]

## Self-Check
- Invented figures: [none / list]
- Inference labeled: [yes/no]
```

---

## Example Output

```
# Business Impact Analysis: ExampleCo SaaS Platform

## Context & Evidence Basis
- Product: team workflow SaaS (placeholder)
- Monetization: per-seat subscription, annual + monthly
- Metrics available: none supplied — ratings below are inference unless tied to code evidence

## Feature Impact Matrix
| Feature | Evidence (file/module) | Revenue | Cost Save | Satisfaction | Competitive | Confidence | Basis |
|---------|------------------------|---------|-----------|--------------|-------------|------------|-------|
| Checkout / billing | src/billing/Checkout.ts (Stripe integration) | High | Low | Medium | Low | High | evidence: directly handles payment |
| Onboarding wizard | src/onboarding/* (4-step flow, no analytics) | Medium | Low | High | Medium | Medium | inference: activation usually drives retention; not instrumented |
| Keyboard shortcuts | src/ui/shortcuts.ts | Low | Low | Medium | Medium | Low | inference: power-user delight, audience size unknown |
| Audit log export | src/compliance/AuditExport.ts | Medium | Low | Low | High | Medium | evidence: gated to Enterprise tier — likely deal-enabler |

## Prioritized Features (highest business value first)
1. Checkout / billing — directly converts revenue; any defect is a direct loss (high confidence).
2. Audit log export — gates Enterprise deals; competitive differentiator in regulated buyers.
3. Onboarding wizard — strong satisfaction/retention lever but UNVERIFIED; instrument before investing.
4. Keyboard shortcuts — nice-to-have; defer unless power-user segment is confirmed large.

## Enhancement Opportunities
- Instrument the onboarding wizard (step-level drop-off) — converts a hypothesis into a measurable retention lever. Low effort.
- Add usage-based billing option in src/billing — opens expansion revenue beyond per-seat. Medium effort.

## Gaps & Data Needed
- No per-feature usage analytics in the codebase → cannot confirm which features are actually used.
- No revenue attribution → revenue ratings are directional, not measured.

## Self-Check
- Invented figures: none (no revenue/usage numbers asserted).
- Inference labeled: yes — each row marks evidence vs. inference.
- Next data to pull: feature-level usage events, revenue by plan tier.
```

---

## Verification

- [ ] Every feature ties to an observable code/metric signal (file/module cited).
- [ ] Each impact rating labeled evidence-based or inferred.
- [ ] No invented revenue/usage/market figures.
- [ ] All four dimensions rated per feature.
- [ ] Features prioritized with transparent rationale.
- [ ] Enhancement suggestions tied to a specific gap and dimension.
- [ ] Gaps and the data needed to resolve them are listed.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the task as translating code capability into prioritized business value.
- **RT-02 (Multi-Dimensional Analysis Framework):** Rates each feature across revenue, cost, satisfaction, and competitive advantage.
- **DS-02 (Evidence-Based Decision Making):** Requires every impact claim to trace to code evidence or supplied metrics, labeling inference.
- **DS-06 (Prioritization and Severity Guidance):** Produces a ranked priority list combining impact and confidence.
- **QA-01 (Self-Critique Triggers):** Final self-check audits for invented figures and unlabeled inference.

---

## Related Prompts

- `domain-business-strategy/analysis/customer_journey_map_analysis.md` — Map code components to journey stages and user experience.
- `domain-business-strategy/analysis/stakeholder_persona_generation.md` — Infer the stakeholders whose value these features serve.
- `domain-business-strategy/analysis/tech_adoption_lifecycle_analysis.md` — Position the product in its adoption lifecycle.
