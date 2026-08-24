---
title: "Build vs Buy vs Partner Decision for AI Capabilities"
category: AI-ML/ai-product-leadership
description: "Decide whether to build, buy, or partner for an AI capability by weighing cost, control, time-to-value, strategic differentiation, and risk from a leadership vantage."
techniques:
  - ST-02
  - RT-02
  - DS-06
  - NE-13
  - RP-02
difficulty: intermediate
tags:
  - build-vs-buy
  - vendor-strategy
  - differentiation
  - total-cost
  - ai-strategy
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/ai-product-leadership/aipm_vendor_model_selection.md
  - domain-AI-ML/ai-product-leadership/aipm_roi_business_case.md
  - domain-AI-ML/ai-product-leadership/aipm_use_case_prioritization.md
---

# Build vs Buy vs Partner Decision for AI Capabilities

**Objective:** For a specific AI capability, produce a structured build-vs-buy-vs-partner recommendation that weighs total cost, control/differentiation, time-to-value, switching cost, and risk — with the reasoning made explicit so leadership can defend it and revisit it as conditions change.

**When to Use:**
- A needed AI capability could plausibly be built in-house, bought off-the-shelf, or delivered via a partner/vendor.
- A vendor proposal is on the table and someone asks "why not just build it?"
- Reassessing an existing build that's straining the team, or an existing vendor that's straining the budget.

**When NOT to Use:**
- The buy path is already chosen and you need to pick among vendors/models (use `aipm_vendor_model_selection.md`).
- You need the dollar case for an in-house build specifically (use `aipm_roi_business_case.md`).

## Inputs / Context

- **Capability definition** — what it does, where it sits in the product, who depends on it.
- **Strategic stance** — is this core differentiation or commodity plumbing?
- **Constraints** — budget band, deadline, team skills/headcount, data sensitivity, compliance.
- **Options on the table** — known vendors/partners, internal estimates if any.
- **Time horizon** — how long this decision must hold and how reversible it must be.

## Constraints

**Must:**
- Evaluate all three paths (build, buy, partner) against the same criteria, even if one looks obviously favored — name why the others lose.
- Distinguish core-differentiating capabilities (lean build) from commodity capabilities (lean buy) explicitly.
- Account for total cost of ownership over the time horizon, not just upfront price — include maintenance, ops, switching, and opportunity cost.

**Must Not:**
- Fabricate vendor pricing or build-cost figures; use ranges/scenarios and label assumptions, requesting real quotes/estimates where decisive.
- Treat "we have engineers" as a free build; engineer-time has a high opportunity cost that must be priced.
- Ignore lock-in and switching cost when the buy/partner path is recommended.

**Instructions:**

1. **Classify the capability.** Place it on a core-vs-commodity and differentiating-vs-table-stakes axis. This single classification reshapes the whole decision and should be stated first.

2. **Define the evaluation criteria.** Lock the dimensions: total cost of ownership, time-to-value, control/customization, strategic differentiation, switching cost/lock-in, operational burden, and risk (compliance, vendor viability, model drift).

3. **Score the build path.** Estimate effort in ranges, the talent required, the maintenance tail, and what it gives you that buying can't. Be honest about the long-term ops cost.

4. **Score the buy path.** Assess fit, integration effort, recurring cost, customization ceiling, data/privacy terms, and lock-in. Flag where a vendor's roadmap controls your future.

5. **Score the partner path.** Assess shared-build/co-development or managed-service arrangements, IP ownership, dependency risk, and exit terms.

6. **Run a switching-cost and reversibility check.** For the leading option, state what it would cost and take to reverse the decision in 18–24 months — cross-reference strategic AI-vendor switch-cost thinking where relevant.

7. **Recommend with conditions.** Give a primary recommendation, the conditions under which you'd flip, and a short trigger list (tripwires) that should prompt a revisit.

**Output Format:**

A markdown decision brief:
- **Capability Classification** — core/commodity, differentiating/table-stakes, and what that implies.
- **Decision Matrix** — table: Criterion | Weight | Build | Buy | Partner (scores + one-line reasoning).
- **Recommendation** — the call, in one paragraph of plain language.
- **Cost Picture** — TCO ranges per path over the horizon, assumptions labeled.
- **Lock-in & Reversibility** — switching cost and exit story for the recommended path.
- **Revisit Triggers** — conditions that should reopen the decision.

## Verification

- [ ] All three paths scored on the same weighted criteria.
- [ ] Capability is classified core/commodity and that classification drives the logic.
- [ ] TCO is over the full horizon and uses labeled ranges, not invented precise figures.
- [ ] Switching cost / lock-in addressed for the recommended path.
- [ ] Recommendation includes conditions-to-flip and revisit triggers.

## False-Positive Prevention

❌ **DON'T:**
- Recommend "build" for a commodity capability just because the team enjoys building.
- Quote a vendor's list price as the total cost while ignoring integration, ops, and lock-in.
- Treat internal engineering time as free or already-paid-for.
- Recommend "buy" for the capability that is your actual competitive moat.

✅ **DO:**
- Let the core-vs-commodity classification dominate: build moats, buy plumbing.
- Price engineer-time at its opportunity cost and include the multi-year maintenance tail.
- Surface lock-in and exit cost as a first-class factor in any buy/partner call.
- Frame the recommendation with tripwires so it can be revisited without re-litigating from scratch.

## Example Output

```markdown
## Build vs Buy vs Partner — Document OCR + Extraction Pipeline

### Capability Classification
Commodity / table-stakes. OCR is not our differentiation; the workflow built ON
extracted data is. → Bias strongly toward buy unless fit is poor.

### Decision Matrix (1–5)
| Criterion | Wt | Build | Buy | Partner |
|---|---|---|---|---|
| TCO (3-yr) | 25 | 2 (high maint tail) | 4 | 3 |
| Time-to-value | 25 | 1 (6–9 mo) | 5 (weeks) | 3 |
| Control/customization | 15 | 5 | 3 | 4 |
| Differentiation gained | 10 | 1 | 1 | 1 |
| Lock-in (higher=worse) | 15 | 5 | 2 | 2 |
| Ops burden | 10 | 1 | 4 | 3 |
| **Weighted** | | 2.4 | **4.0** | 3.0 |

### Recommendation
Buy. OCR/extraction is commodity; a mature vendor gets us to value in weeks at a
TCO range well below a build whose only payoff is control we don't strategically need.

### Cost Picture (3-yr, ranges; assumptions labeled)
- Buy: low-five-figure to low-six-figure/yr depending on volume tier (assumes ~X pages/mo).
- Build: high-six-figure all-in once 1.5 FTE maintenance is priced — confirm with eng estimate.

### Lock-in & Reversibility
Moderate. Standardize on a vendor-neutral output schema so a future swap is a
connector change, not a re-architecture. Exit ≈ 1 sprint if schema discipline holds.

### Revisit Triggers
- Volume grows 5×+ (build economics may flip). - Vendor raises price >30%.
- Extraction accuracy on our docs becomes a differentiator (then build the hard 10%).
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** classify → score three paths → reversibility → recommend.
- **RT-02 (Multi-Dimensional Analysis Framework):** weighted decision matrix across paths.
- **DS-06 (Prioritization & Severity Guidance):** recommendation with revisit triggers.
- **NE-13 (Technical-to-Business Translation):** technical fit rendered as a cost/control/risk call.
- **RP-02 (Audience-Specific Framing):** framed for a leadership decision.

**Related Prompts:**
- `aipm_vendor_model_selection.md` — once "buy" wins, choose the vendor/model.
- `aipm_roi_business_case.md` — build the financial case for the chosen path.
- `aipm_use_case_prioritization.md` — confirm the capability is worth funding at all.
