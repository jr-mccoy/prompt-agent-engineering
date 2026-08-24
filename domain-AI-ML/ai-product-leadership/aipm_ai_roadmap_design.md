---
title: "Phased AI Roadmap Design"
category: AI-ML/ai-product-leadership
description: "Design a phased AI roadmap aligned to business strategy and honest capability maturity, sequencing bets so each phase builds the foundations the next one needs."
techniques:
  - ST-02
  - RT-02
  - DS-06
  - DS-01
  - NE-13
difficulty: advanced
tags:
  - roadmap
  - ai-strategy
  - capability-maturity
  - sequencing
  - foundations
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/ai-product-leadership/aipm_use_case_prioritization.md
  - domain-AI-ML/ai-product-leadership/aipm_mlops_maturity_for_leaders.md
  - domain-AI-ML/ai-product-leadership/aipm_ml_team_structure_hiring.md
---

# Phased AI Roadmap Design

**Objective:** Produce a phased AI roadmap that ties each phase to a business outcome and to the capability maturity required to deliver it — sequencing so foundational investments (data, platform, governance) precede the ambitious bets that depend on them, and so value lands continuously rather than only at the end.

**When to Use:**
- Leadership wants a multi-quarter or multi-year AI plan, not a list of projects.
- Multiple AI bets exist and the question is order and dependency, not just selection.
- An "AI strategy" deck needs a credible delivery spine underneath the vision.

**When NOT to Use:**
- You only need to rank candidates (use `aipm_use_case_prioritization.md`).
- You need to assess current operational maturity in isolation (use `aipm_mlops_maturity_for_leaders.md`).

## Inputs / Context

- **Business strategy** — the company's goals and how AI is meant to serve them.
- **Candidate bets** — prioritized use cases or initiatives (ideally already ranked).
- **Current capability maturity** — data, platform/MLOps, talent, governance state.
- **Constraints** — budget/headcount trajectory, time horizon, regulatory deadlines.
- **Dependencies** — shared infrastructure (feature store, eval harness, data contracts) that multiple bets need.

## Constraints

**Must:**
- Anchor every phase to a business outcome and a measurable signal of progress, not just "build X."
- Sequence by dependency: foundational capabilities that unlock multiple bets come before the bets.
- Make each phase deliver standalone value so the roadmap survives a budget cut after any phase.

**Must Not:**
- Promise a transformative end-state bet in phase 1 when the data/platform foundations don't exist.
- Invent timelines or capability levels; ground phasing in the stated maturity and resourcing.
- Present a roadmap with no kill/revisit points — strategy and conditions change.

**Instructions:**

1. **Restate the strategic intent.** In a sentence or two, what business outcomes AI must drive. Every phase will be checked against this. Cross-reference the org's broader AI strategy where one exists.

2. **Baseline capability maturity.** Score the foundations (data readiness, platform/MLOps, talent, governance) honestly. The roadmap's early phases exist to close the gating gaps.

3. **Map dependencies.** Identify shared enablers (feature store, eval harness, labeling pipeline, data contracts, governance process) that multiple bets require, and treat them as funded infrastructure, not per-project tax.

4. **Define phases by capability unlock.** Structure phases as Foundation → Early Value → Scale → Differentiate (or similar), where each phase raises the capability floor the next depends on.

5. **Place bets into phases.** Assign each prioritized bet to the earliest phase whose foundations support it. A high-value bet with unmet dependencies waits — and the roadmap shows why.

6. **Attach outcomes and signals.** Per phase: the business outcome, the leading indicators, and the decision to make at the gate (continue/adjust/stop).

7. **Stress-test the roadmap.** Name the assumptions that, if wrong, break the sequence; add revisit triggers and a "what survives a 30% budget cut" fallback.

**Output Format:**

A markdown roadmap:
- **Strategic Intent** — what AI must achieve for the business.
- **Capability Baseline** — current maturity scores and gating gaps.
- **Phase Plan** — per phase: theme | capabilities built | bets shipped | business outcome | gate decision.
- **Dependency Map** — shared enablers and which bets they unlock.
- **Risks & Revisit Triggers** — assumptions, budget-cut fallback, conditions to replan.

## Verification

- [ ] Each phase tied to a business outcome and a progress signal.
- [ ] Foundations sequenced before the bets that depend on them.
- [ ] Each phase delivers standalone value (survives a post-phase budget cut).
- [ ] Shared enablers funded as infrastructure, not duplicated per bet.
- [ ] Revisit triggers and a budget-cut fallback are present.

## False-Positive Prevention

❌ **DON'T:**
- Put the flagship "AI transformation" bet in phase 1 before any data foundation exists.
- Sequence bets by excitement rather than by dependency readiness.
- Build a roadmap whose value only materializes in the final phase.
- Re-fund the same enabler (e.g., a feature store) inside three different projects.

✅ **DO:**
- Lead with the foundation that unlocks the most downstream bets.
- Let unmet dependencies, not enthusiasm, decide what waits.
- Make every phase ship something usable so funding can stop without total loss.
- Fund shared enablers once, as infrastructure, and show which bets they unblock.

## Example Output

```markdown
## Phased AI Roadmap — Marketplace Co. (18 months)

### Strategic Intent
Use AI to lift conversion and retention while reducing ops cost — without taking
on consumer-protection risk that outpaces our governance.

### Capability Baseline
Data readiness: 2/5 (siloed, no contracts). Platform/MLOps: 1/5 (notebooks → prod by hand).
Talent: 2/5 (2 ML eng, no platform). Governance: 1/5. → Phase 1 must close foundations.

### Phase Plan
| Phase | Theme | Capabilities built | Bets shipped | Outcome | Gate |
|---|---|---|---|---|---|
| 1 (0–6mo) | Foundation | Feature store, data contracts, basic MLOps, governance v1 | Ticket auto-triage (low-risk) | Ops cost ↓; pipeline proven | Pipeline reliable? |
| 2 (6–12mo) | Early value | Eval harness, monitoring | Search ranking, email personalization | Conversion ↑ | Lift measurable? |
| 3 (12–18mo) | Differentiate | Online features, A/B infra | Churn early-warning + retention play | Retention ↑ | Wired to action? |

### Dependency Map
Feature store (P1) unlocks ranking, personalization, churn. Eval harness (P2)
unlocks trustworthy iteration on all customer-facing models. Governance v1 (P1)
gates the higher-risk bets to phase 3.

### Risks & Revisit Triggers
Assumes the P1 platform hire lands on schedule. If not, P2 slips — replan, don't
compress quality. Budget-cut fallback: P1 alone (triage + foundations) pays for itself.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** intent → baseline → dependencies → phases → stress-test.
- **RT-02 (Multi-Dimensional Analysis Framework):** phasing balances value, dependency, and maturity.
- **DS-06 (Prioritization & Severity Guidance):** dependency-driven sequencing with gates.
- **DS-01 (Framework Application):** maturity model + capability-unlock phasing.
- **NE-13 (Technical-to-Business Translation):** each phase expressed as a business outcome.

**Related Prompts:**
- `aipm_use_case_prioritization.md` — the ranked bets that feed the phases.
- `aipm_mlops_maturity_for_leaders.md` — the maturity baseline the foundation phase closes.
- `aipm_ml_team_structure_hiring.md` — staff the team to deliver the roadmap.
