---
title: "Technology Adoption Lifecycle Analysis for Codebase"
category: software-engineering/analysis/business
description: "Use the Technology Adoption Lifecycle model to place a product's current market stage based on observable signals in its codebase and supplied context, then recommend prioritized strategies and a roadmap for crossing to the next stage."
techniques:
  - ST-01
  - DS-01
  - DS-02
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - business-analysis
  - adoption-lifecycle
  - market-position
  - codebase-analysis
  - go-to-market
updated: "2026-06-07"
related_prompts:
  - domain-software-engineering/analysis/business/business_impact_analysis.md
  - domain-software-engineering/analysis/business/customer_journey_map_analysis.md
  - domain-software-engineering/analysis/business/stakeholder_persona_generation.md
---

# Technology Adoption Lifecycle Analysis for Codebase

**Objective:** Apply the Technology Adoption Lifecycle model (Innovators → Early Adopters → Early Majority → Late Majority → Laggards) to a product, using observable code signals and supplied context to place its current stage and recommend a prioritized roadmap for reaching the next stage.

**When to use:**
- Founders/PMs want a structured read on where the product sits in its market evolution.
- Planning go-to-market or product investment and need to know which adopter segment to target next.
- Diagnosing why growth has stalled at a stage boundary (e.g., the "chasm" to the early majority).
- Aligning engineering investment (reliability, ease-of-use) with the next adopter segment's needs.

**When NOT to use:**
- You have no market, sales, or usage context — stage placement will be guesswork dressed as analysis.
- You need rigorous market sizing or forecasting — use a dedicated market/finance prompt.
- The product is internal-only with no external adoption to model.

**Audience:** Founders, product managers, growth/marketing leaders, and CTOs.

---

## Inputs / Context

The user should supply (or the analysis should flag what is missing):

1. **The codebase** (or feature inventory) and what the product does.
2. **Market context:** target customers, how it's sold, current traction signals (customers, growth, churn) if known.
3. **Code-readable maturity signals:** error handling/reliability features, onboarding polish, documentation, configurability, accessibility, integrations.
4. **The decision the analysis feeds:** GTM strategy, roadmap, fundraising narrative.
5. **Scope/depth:** quick read vs. deep stage-crossing plan.

---

## Constraints

### Must
- Use the **five lifecycle stages explicitly** and define the characteristics of the relevant ones.
- Place the current stage using a **mix of code signals and supplied context**, and state which evidence drives the placement. Cite files/modules for code signals.
- Distinguish **fact** (the product has no onboarding flow / extensive config exposed) from **inference** (this *suggests* it targets early adopters).
- Analyze the **current and adjacent stages'** user characteristics and needs.
- Produce a **prioritized** set of strategies and a roadmap for crossing to the next stage.
- Where placement rests on unsupplied data, **label it as hypothesis** and name the data that would confirm it.

### Must Not
- Invent customer counts, growth rates, or market share not supplied.
- Present a stage placement as certain when it rests on inference.
- Treat code sophistication alone as proof of market maturity.
- Recommend a generic "cross the chasm" plan with no tie to this product's specific gaps.

---

## Instructions

1. **Summarize the product and capabilities.** From the codebase, list the major features and any maturity signals (reliability, onboarding, docs, configurability, integrations). Cite files.
2. **Define the lifecycle frame.** State the five stages briefly, emphasizing the stages adjacent to your placement.
3. **Place the current stage.** Combine code signals and supplied context. List the evidence for the placement and label each as fact or inference. Note the confidence.
4. **Profile current and adjacent adopters.** Characteristics, needs, and what they require to adopt.
5. **Identify stage-crossing gaps.** What the next segment needs that the product lacks (e.g., reliability, simplicity, social proof, integrations) — tie each to a code or product observation.
6. **Recommend prioritized strategies.** Product, positioning, and support moves to reach the next segment, ranked by impact.
7. **Build a roadmap.** Sequence the moves with rough milestones.
8. **Self-check (verification step).** Re-read: any invented traction figure? Is the stage placement honest about its evidence? Are gaps tied to specifics and the needed data named?

---

## False-Positive Prevention

❌ **DON'T:**
- State "the product is in the early majority" with no traction data and no caveat.
- Assume rich, complex code means a mature-market product.
- Present inference (target segment, stage) as established fact.
- Hand over a textbook "crossing the chasm" plan with no link to this product's gaps.
- Recommend strategies for one segment while ignoring what the current base needs.

✅ **DO:**
- Label the stage placement **evidence-based** vs. **hypothesis** and state confidence.
- Cite specific code/product signals behind the placement and gaps.
- Acknowledge that code alone can't confirm market stage and name the data (sales, cohort, churn) that would.
- Prioritize stage-crossing strategies by impact.
- Suggest validation steps (pull win/loss, segment current customers) before committing GTM spend.

---

## Output Format

```
# Technology Adoption Lifecycle Analysis: [Product / Codebase]

## Context & Evidence Basis
- Product: [...]
- Traction context: [supplied signals, or "none — placement is inference-heavy"]
- Code maturity signals (file/module): [...]

## Lifecycle Frame
[Brief definition of the five stages; emphasis on adjacent stages]

## Current Stage Placement
- Stage: [...]  (Confidence: High/Medium/Low)
- Evidence for placement:
  - [signal] — fact / inference
- Why not the adjacent stages: [...]

## Adopter Profiles (current + next)
- Current segment: needs, characteristics
- Next segment: needs, characteristics, adoption barriers

## Stage-Crossing Gaps
- [Gap] → next-segment need it blocks, tied to [code/product observation]

## Prioritized Strategies
1. [Strategy] — segment targeted, gap addressed, impact
2. ...

## Roadmap
- Near-term: [...]
- Mid-term: [...]

## Gaps & Data Needed
- [What code can't tell us, and the data that would]

## Self-Check
- Invented traction figures: [none / list]
- Placement evidence labeled: [yes/no]
```

---

## Example Output

```
# Technology Adoption Lifecycle Analysis: ExampleCo Dev Tool (placeholder)

## Context & Evidence Basis
- Product: CLI-first developer tool (placeholder)
- Traction context: none supplied — placement below is inference-heavy and labeled as such
- Code maturity signals: heavy CLI surface (src/cli/*), sparse onboarding (no GUI installer), extensive config flags (src/config/schema.ts), minimal error-recovery messaging

## Lifecycle Frame
Innovators (risk-tolerant tinkerers) → Early Adopters (visionaries seeking edge) → Early Majority (pragmatists needing proven, easy, reliable) → Late Majority → Laggards. Focus: the Early Adopter → Early Majority crossing.

## Current Stage Placement
- Stage: Early Adopters  (Confidence: Low — no usage/sales data)
- Evidence for placement:
  - CLI-only, no GUI/installer (fact) → suits technical, tolerant users (inference)
  - Many exposed config flags, few sane defaults (fact) → expects users who enjoy configuration (inference)
  - Thin onboarding and error messaging (fact) → not yet built for pragmatists (inference)
- Why not Early Majority: pragmatists need reliability, defaults, and hand-holding the code does not yet provide.

## Adopter Profiles (current + next)
- Current (Early Adopters): tolerate rough edges for capability; configure heavily.
- Next (Early Majority): need proven reliability, sensible defaults, easy onboarding, social proof, and integrations into existing stacks.

## Stage-Crossing Gaps
- No guided onboarding → blocks pragmatist activation (tied to absence of installer/wizard).
- Config-heavy with few defaults → raises adoption cost (tied to src/config/schema.ts).
- Sparse error recovery → erodes reliability perception (tied to thin error handling).

## Prioritized Strategies
1. Add sane defaults + a guided first-run experience — directly lowers the early-majority adoption barrier. High impact.
2. Improve error messages and recovery paths — builds the reliability perception pragmatists require. High impact.
3. Add integrations with common stacks + publish case studies for social proof. Medium impact.

## Roadmap
- Near-term: defaults + first-run wizard; error-handling pass.
- Mid-term: top-3 integrations; reference customers / case studies.

## Gaps & Data Needed
- No adoption/cohort data → stage placement is a hypothesis; pull active-user trends and win/loss to confirm.
- No segment breakdown of current users → confirm whether base is truly early-adopter-heavy.

## Self-Check
- Invented traction figures: none.
- Placement evidence labeled: yes — each signal marked fact vs. inference; confidence stated as Low.
```

---

## Verification

- [ ] All five lifecycle stages referenced; adjacent stages defined.
- [ ] Stage placement combines code signals and supplied context, each labeled fact or inference.
- [ ] Confidence in the placement stated honestly.
- [ ] No invented traction, growth, or market-share figures.
- [ ] Current and next adopter segments profiled.
- [ ] Stage-crossing gaps tied to specific code/product observations.
- [ ] Strategies prioritized and sequenced into a roadmap.
- [ ] Data needed to confirm the placement is named.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the task as placing the product's adoption stage and planning the next-stage crossing.
- **DS-01 (Framework Application):** Applies the Technology Adoption Lifecycle model as the analytical structure.
- **DS-02 (Evidence-Based Decision Making):** Requires stage placement and gaps to trace to code signals or supplied context, labeling inference.
- **DS-06 (Prioritization and Severity Guidance):** Produces prioritized stage-crossing strategies and a sequenced roadmap.
- **QA-01 (Self-Critique Triggers):** Final self-check audits for invented traction and overconfident placement.

---

## Related Prompts

- `domain-software-engineering/analysis/business/business_impact_analysis.md` — Translate features into prioritized business value.
- `domain-software-engineering/analysis/business/customer_journey_map_analysis.md` — Map how users move through the product.
- `domain-software-engineering/analysis/business/stakeholder_persona_generation.md` — Infer the adopter personas the product serves.
