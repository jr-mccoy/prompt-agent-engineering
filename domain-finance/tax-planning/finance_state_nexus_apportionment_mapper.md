---
title: "State Nexus & Apportionment Mapper — Multistate Income-Tax Exposure Analysis"
category: finance/tax-planning
description: "Map a business's multistate tax footprint by analyzing nexus triggers (physical, economic, factor-presence), apportionment factor formulas (single-sales vs three-factor, market-based vs cost-of-performance sourcing), and throwback/throwout exposure — as analysis only, routing filing positions to a tax professional."
techniques:
  - NE-11
  - DT-02
  - QA-02
  - DS-02
  - RT-02
difficulty: advanced
tags:
  - state-tax
  - nexus
  - apportionment
  - salt
  - multistate
  - economic-nexus
updated: "2026-06-08"
related_prompts:
  - domain-finance/tax-planning/finance_entity_structure_tax_comparison.md
  - domain-finance/tax-planning/finance_rd_and_credits_mapping.md
  - domain-finance/tax-planning/finance_multi_year_tax_projection.md
  - domain-finance/field_guide.md
---

**Informational analysis only — not tax, legal, or accounting advice. State nexus and apportionment rules vary by state, change frequently, and depend on specific facts; filing positions, voluntary-disclosure decisions, registration, and reliance must be made with a qualified state-and-local tax (SALT) professional (CPA/attorney). Verify every state's nexus thresholds, apportionment formula, sourcing rule, and throwback status against current law as of the analysis date and each applicable state.**

## Objective

Produce an auditable map of a business's potential state income/franchise-tax exposure that (1) identifies nexus-creating activities per state, (2) classifies each state's apportionment formula and sourcing rule, (3) estimates an illustrative apportionment percentage per state from user-supplied factor data, and (4) flags throwback/throwout, P.L. 86-272 protection, and registration gaps — so the user and their SALT professional can prioritize. This prompt analyzes exposure; it does not establish filing positions.

## When to Use

- A company has grown into remote sales, remote employees, or marketplace sales and needs to scope where it may owe income/franchise tax.
- Pre-acquisition or pre-financing diligence on state-tax exposure and reserves.
- Building a voluntary-disclosure-agreement (VDA) prioritization list before professional engagement.
- Sanity-checking an outside provider's apportionment workpapers.
- Modeling the state-tax cost of a new office, warehouse, or remote-hire expansion.

## Inputs / Context Required

```
<nexus_context>
Entity type: C-corp | S-corp | partnership/LLC (note pass-through composite/PTE elections vary by state)
Tax years in scope:
States with ANY of the following (list per state):
  - Physical presence: office, warehouse, inventory (incl. 3PL/FBA), owned/leased property
  - Payroll: employees, remote workers, traveling salespeople
  - Economic presence: sales into the state (amount $) and transaction count
  - Affiliate/agency relationships, contractors performing services
Activity detail per state:
  In-state sales $:                         [user-supplied]
  In-state property $ (avg or year-end):    [user-supplied]
  In-state payroll $:                        [user-supplied]
  Nature of activity (solicitation only? services? installation?):
TOTALS (everywhere):
  Total sales $:   Total property $:   Total payroll $:
Per-state thresholds (user must supply current figures):
  Economic nexus $ / transaction threshold for income tax: [input current-year figure per state; verify]
  Factor-presence thresholds (e.g., $ sales / $ property / $ payroll): [input; verify]
Product vs service mix; tangible goods vs intangibles/SaaS (affects sourcing).
P.L. 86-272 question: is in-state activity limited to mere SOLICITATION of orders for tangible personal property shipped from out of state? (yes/no/unsure)
</nexus_context>
```

## Constraints

### Must
- For each state, run a **nexus screen** across the dimensions (RT-02): physical presence, payroll/employees, economic/factor-presence, and affiliate/agency — marking each as Present / Absent / Uncertain.
- Apply **P.L. 86-272** analysis: federal protection bars a state from imposing a **net income tax** if in-state activity is limited to solicitation of orders for **tangible personal property** filled from out of state. Note it does NOT protect services, intangibles/SaaS, or franchise/gross-receipts taxes, and that some states assert internet-activity exceptions.
- Classify each state's **apportionment formula**: single-sales-factor vs three-factor (sales/property/payroll, possibly weighted) — `[input per-state; verify]`.
- Classify each state's **sales sourcing**: **market-based** (sourced to where the customer receives the benefit) vs **cost-of-performance** (where the income-producing activity occurs) — `[input per-state; verify]`.
- Compute illustrative apportionment with formula → inputs → result (NE-11):
  - Single-sales: `Apportionment % = In-state sales / Total sales`
  - Three-factor (equal weight): `(Sales% + Property% + Payroll%) / 3`
  - Weighted (e.g., double-weighted sales): apply the state's weights explicitly.
- Flag **throwback** (untaxed sales thrown back to the origin state) and **throwout** rules where the destination state has no nexus.
- Flag **nowhere income** and **double-counting** risks (sum of apportionment %s across states ≠ 100% is normal and expected — do not "true up" to 100%).
- State that filing positions, registration, and VDAs route to the SALT professional.

### Must Not
- Assert specific current-year per-state nexus thresholds, formulas, or sourcing rules from memory — require user input or mark `[input current-year figure per state; verify]`.
- Conclude "you must file in State X" — present exposure and uncertainty; the filing position routes to the professional.
- Assume apportionment percentages across states sum to 100% (they need not; overlap and gaps are inherent to differing rules).
- Treat P.L. 86-272 as protecting service revenue, SaaS, or gross-receipts/franchise taxes.
- Ignore that pass-through entities may face composite returns, PTE-tax elections, and partner-level nexus that differ from C-corp rules.

## Instructions

**Step 1 — Build the activity matrix (DT-02).**

| State | Physical | Payroll | Economic (sales) | Affiliate/agent | P.L. 86-272 protected? | Nexus conclusion |
|---|---|---|---|---|---|---|
| | office? | employees? | $ / # txns vs threshold | | TPP-solicitation only? | Present/Uncertain/Absent |

**Step 2 — Economic-nexus screen.**
```
For each state: nexus IF in-state sales ≥ [state $ threshold; verify]
                     OR transactions ≥ [state count threshold; verify]
                     OR factor-presence threshold met.
Mark UNCERTAIN where facts are borderline or the threshold is user-unknown.
```

**Step 3 — P.L. 86-272 filter.**
```
If in-state activity = solicitation of orders for TPP shipped from out of state ONLY → likely protected (income tax).
Disqualifiers: in-state services, installation, repairs, inventory, non-solicitation employees, SaaS, intangibles,
   and (in some states) interactive website / app activity.
Note: does NOT protect franchise, gross-receipts (e.g., margin/CAT-style), or sales/use taxes.
```

**Step 4 — Apportionment computation per nexus state (NE-11).**
```
Sales factor    = In-state sales / Total sales         (apply MARKET-BASED or COST-OF-PERFORMANCE sourcing per state)
Property factor = In-state property / Total property
Payroll factor  = In-state payroll / Total payroll
Apportionment % = per-state formula:
   single-sales:        Sales factor
   3-factor equal:      (Sales + Property + Payroll)/3
   double-weighted:     (2·Sales + Property + Payroll)/4   [or the state's exact weights]
```

**Step 5 — Throwback / throwout / nowhere-income flags.**
```
Throwback: sales shipped from State A to a state with NO nexus may be "thrown back" into State A's numerator.
Throwout: such sales removed from the denominator instead (raises everyone else's %).
Flag states that apply each, and quantify the illustrative effect on State A's apportionment %.
```

**Step 6 — Exposure prioritization (DS-02 / QA-02).**

| State | Nexus confidence | Apportionment % | Approx. taxable base × % | Est. rate [verify] | Illustrative exposure | Priority |
|---|---|---|---|---|---|---|

**Step 7 — Adversarial stress-test (QA-02).**
- Where is nexus asserted on borderline economic thresholds the user has not verified?
- Does P.L. 86-272 protection silently fail because of in-state services, SaaS, or a single installing employee?
- Do market-based-sourcing states pull in sales that cost-of-performance states would source elsewhere — creating double taxation?
- Are inventory in 3PL/FBA warehouses creating physical nexus the user forgot?
- For pass-throughs: are partner-level and PTE-election obligations being missed?
- Statute-of-limitations / look-back: unregistered states have open exposure for prior years — does a VDA reduce look-back?

## Output Format

```
## State Nexus & Apportionment Map
Entity: [type] | Years: [scope] | As of: [date] | Per-state figures: user-supplied/verify

### Nexus Activity Matrix
[Step 1 table]

### Economic-Nexus & P.L. 86-272 Conclusions
[Steps 2–3 per state]

### Apportionment by State
[Step 4 computations with factor detail and formula used]

### Throwback / Throwout Flags
[Step 5 — states + illustrative effect]

### Exposure Prioritization
[Step 6 table, ranked]

### Stress-Test Findings
[Step 7 bullets]

### Items to route to your SALT professional
[filing positions, registration, VDA candidates, unverified thresholds, sourcing calls]
```

## Verification

- [ ] Nexus screened across physical, payroll, economic, and affiliate dimensions for every state.
- [ ] P.L. 86-272 applied only to net-income tax on TPP-solicitation; services/SaaS/gross-receipts disqualifiers noted.
- [ ] Apportionment formula identified per state (single-sales vs weighted three-factor) and marked verify.
- [ ] Sales sourcing (market-based vs cost-of-performance) stated per state.
- [ ] Each apportionment % shown as formula → inputs → result.
- [ ] Throwback/throwout flagged; no forced "true-up" to 100% across states.
- [ ] Pass-through composite/PTE considerations noted where relevant.
- [ ] No current-year per-state threshold/formula/rate asserted from memory.
- [ ] Output frames exposure and priority, not filing positions.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Concluding "no nexus" on economic activity below a guessed threshold | Mark UNCERTAIN unless the user supplies the verified state threshold |
| Treating P.L. 86-272 as blanket protection | Restricted to income tax on TPP solicitation; flag service/SaaS/gross-receipts/franchise disqualifiers |
| Assuming apportionment %s sum to 100% | Differing state rules create overlap and gaps by design; do not normalize to 100% |
| Ignoring 3PL/FBA inventory as physical nexus | Activity matrix explicitly asks for inventory location including third-party warehouses |
| Applying one sourcing rule to all states | Market-based vs cost-of-performance is per-state; state each and flag double-tax risk |
| Asserting per-state thresholds/rates | All marked `[input current-year figure per state; verify]` |
| Stating "you must file in State X" | Output is exposure analysis; filing positions and VDAs route to the SALT professional |
