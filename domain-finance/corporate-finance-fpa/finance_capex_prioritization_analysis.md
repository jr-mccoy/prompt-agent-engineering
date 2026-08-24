---
title: "Capex Prioritization Analysis — NPV / IRR / Payback Ranking with Strategic and Risk Overlays"
category: finance/corporate-finance-fpa
description: "Prioritize competing capital projects using NPV, IRR, and payback against the WACC hurdle, then overlay strategic fit, risk, and capital rationing to produce a fundable ranked queue."
techniques:
  - NE-11
  - DS-06
  - NE-10
  - RT-02
  - QA-04
difficulty: intermediate
tags:
  - capex
  - capital-budgeting
  - npv
  - irr
  - payback
  - project-prioritization
updated: "2026-06-08"
related_prompts:
  - domain-finance/corporate-finance-fpa/finance_capital_allocation_framework.md
  - domain-finance/valuation/finance_dcf_model_builder.md
  - domain-finance/valuation/finance_wacc_builder.md
  - domain-finance/field_guide.md
---

**Informational only — not financial or investment advice.**

## Objective

Prioritize a slate of competing capital projects by computing NPV, IRR, and discounted payback against the cost-of-capital hurdle, then overlaying strategic fit, execution risk, and capital-rationing constraints — producing a defensible, fundable ranked queue rather than a first-come-first-served capex list.

---

## When to Use

- Annual capital-budgeting cycle with more project requests than budget.
- Choosing among mutually exclusive projects (e.g., two ways to add capacity).
- Maintenance vs growth capex tradeoffs under a constrained budget.
- Re-justifying in-flight projects whose economics may have shifted.
- **Do not use** to value an acquisition or a whole business (use a DCF/LBO model), or to make accounting capitalization decisions; this ranks discrete projects.

---

## Inputs / Context Required

```
<capex_inputs>
Company / business unit:
Currency:
Hurdle rate (WACC or project-specific hurdle from finance_wacc_builder.md):
Total capital budget available (the rationing constraint):

PER PROJECT (one block each):
- Project name, type (maintenance | growth | compliance | cost-saving | strategic)
- Initial investment (and phasing if multi-year)
- Projected incremental cash flows by year (state assumptions)
- Project life / horizon; terminal/salvage value if any
- Risk class (low/med/high) and basis
- Strategic rationale / dependency on other projects
- Whether mandatory (safety/compliance) or discretionary
- Mutually exclusive alternatives, if any

CONTEXT:
- Tax rate (for after-tax cash flows / depreciation tax shield)
- Reinvestment-rate assumption for IRR caveats
</capex_inputs>
```

---

## Constraints

### Must
- Compute, for each project, **NPV, IRR, and discounted payback** with formulas shown (NE-11):
  ```
  NPV = Σ [ CF_t / (1 + r)^t ] − Initial Investment        (r = hurdle/WACC)
  IRR = rate where NPV = 0  (solve)
  Discounted Payback = years until cumulative discounted CF ≥ initial investment
  Profitability Index (PI) = PV of future cash flows / Initial Investment
  ```
- Use **after-tax incremental cash flows** including the depreciation tax shield; exclude sunk costs and allocated overhead that won't change.
- Rank primarily by **NPV** (absolute value creation), but report IRR and PI; under **capital rationing**, rank by **PI** (NPV per dollar) to maximize value within the budget.
- Flag the **NPV vs IRR conflict** for mutually exclusive projects (different scale/timing) and resolve in favor of NPV.
- Overlay **strategic fit and risk** (RT-02): mandatory/compliance projects rank ahead of discretionary regardless of NPV; high-risk projects carry a higher hurdle or a haircut.
- Use **scenario ranges** (NE-10) for projects with uncertain cash flows; show NPV under base/bull/bear.
- Acknowledge IRR's reinvestment-rate and multiple-IRR caveats (QA-04); prefer NPV/MIRR where cash flows change sign.
- Produce a **ranked, fundable queue** (DS-06) that respects the budget.

### Must Not
- Rank purely by IRR (it ignores scale and can mislead on mutually exclusive projects).
- Include sunk costs or non-incremental allocated overhead in project cash flows.
- Fund discretionary high-NPV projects ahead of mandatory compliance/safety projects.
- Present a single-point NPV for an uncertain project without a range.
- Invent cash-flow projections; require them as inputs or label assumptions.

---

## Instructions

1. **Normalize cash flows.** For each project, build after-tax incremental free cash flows; remove sunk costs; include the depreciation tax shield and any salvage. State the horizon.

2. **Compute the metrics (NE-11).** NPV at the hurdle, IRR, discounted payback, and PI for each project. Show the discounting.

3. **Handle mutually exclusive sets.** Where projects are alternatives, compare NPV directly; if IRR and NPV disagree (scale/timing), choose by NPV and explain the conflict. Use incremental analysis (Δ cash flows of the larger over the smaller).

4. **Classify and overlay (RT-02).**
   ```
   Tier 0 — Mandatory (safety/compliance/keep-the-lights-on): fund first regardless of NPV.
   Tier 1 — Value-creating discretionary (NPV > 0 at hurdle): rank by PI under rationing.
   Tier 2 — Strategic options (low/negative near-term NPV, real-option value): judgment.
   Tier 3 — NPV < 0: reject unless mandatory.
   ```

5. **Risk-adjust.** For high-risk projects, either raise the project hurdle or apply a probability haircut to cash flows; state which. Scenario the most uncertain projects (NE-10).

6. **Apply capital rationing (DS-06).** With a fixed budget, select the combination of projects that maximizes total NPV within the budget (PI ranking is the practical heuristic; note it can be imperfect with lumpy projects — check a couple of feasible combinations).

7. **Build the fundable queue.** Order: all Tier 0, then Tier 1 by PI until budget exhausted, with Tier 2 options flagged for judgment. Show what falls below the funding line and why.

8. **Verification (QA-01).** Confirm NPV uses the correct hurdle and after-tax cash flows; confirm IRR caveats noted; confirm the funded set fits the budget; state the swing assumption.

---

## Output Format

```
## Capex Prioritization — [Company/BU]
Hurdle: [x]% | Budget: $[z]M | Tax rate: [t]%
NOTE: figures below are ILLUSTRATIVE.

### Project Economics
| Project | Type | Invest | NPV | IRR | Disc. Payback | PI | Risk |
|---------|------|--------|-----|-----|---------------|----|----- |
| Line upgrade | Cost-saving | 10 | 6.2 | 24% | 3.1 yr | 1.62 | Low |
| New plant    | Growth     | 40 | 11.5| 16% | 5.4 yr | 1.29 | Med |
| Compliance   | Mandatory  | 5  | (0.4)| n/a | n/a    | 0.92 | Low |
| R&D platform | Strategic  | 8  | (1.0)| 6%  | >horizon| 0.88| High|

### Tiering & Overlay
| Tier | Project | Decision |
|------|---------|----------|
| 0 Mandatory | Compliance | Fund (regulatory; NPV not the gate) |
| 1 Value     | Line upgrade (PI 1.62) | Fund — highest NPV/$ |
| 1 Value     | New plant (PI 1.29)    | Fund if budget allows |
| 2 Option    | R&D platform | Real-option value; small allocation by judgment |
| 3 Reject    | — | — |

### Capital Rationing (budget $[z]M, illustrative)
Fund: Compliance ($5) + Line upgrade ($10) + New plant ($40) = $55 vs budget $50.
→ With $50: Compliance + Line upgrade + (partial/defer plant or pick highest-PI combo).
Selected set maximizes NPV within budget: total NPV = $[x]M.

### Scenario (uncertain project — New plant)
| Scenario | NPV |
|----------|-----|
| Bear (demand −20%) | (3.0) |
| Base | 11.5 |
| Bull (demand +15%) | 22.0 |
NPV turns negative in the bear case → fund only if demand floor is credible.

### Below-the-Line
R&D platform deferred this cycle pending milestone; revisit when option clarifies.

### IRR Caveats
IRR assumes reinvestment at IRR; for the plant vs upgrade choice, NPV governs (scale differs).
```

---

## Verification

- [ ] NPV computed at the correct hurdle using after-tax incremental cash flows.
- [ ] Sunk costs and non-incremental overhead excluded.
- [ ] IRR, discounted payback, and PI reported alongside NPV.
- [ ] Mutually exclusive conflicts resolved by NPV with the reason stated.
- [ ] Mandatory projects funded ahead of discretionary regardless of NPV.
- [ ] Capital rationing uses PI and checks feasible combinations within budget.
- [ ] Uncertain projects scenario-ranged; bear case shown.
- [ ] IRR reinvestment/multiple-IRR caveats noted; swing assumption stated.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Ranking by IRR alone | Rank by NPV (and PI under rationing); IRR ignores scale and misleads on mutually exclusive projects |
| Including sunk costs in project economics | Use only incremental after-tax cash flows; exclude sunk and non-changing allocated overhead |
| Funding high-NPV discretionary over mandatory | Mandatory/compliance is Tier 0 — funded first; NPV is not the gate for safety/regulatory |
| Single-point NPV on uncertain projects | Scenario-range the cash flows; show the bear case before funding |
| Treating IRR as a reinvestment-safe metric | Note the reinvestment-rate assumption; use MIRR/NPV where cash flows change sign |
| Assuming PI ranking is always optimal under rationing | With lumpy budgets, check a few feasible combinations to confirm the NPV-maximizing set |
