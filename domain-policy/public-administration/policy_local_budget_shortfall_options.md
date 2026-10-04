---
title: "Local Government Budget Shortfall Options — Structural vs One-Time Gap, Legal Screen, Service and Equity Impact, and Balanced Packages"
category: policy/public-administration
description: "Close a municipal, county or special-district budget gap honestly: split the gap into structural and one-time parts over a multi-year forecast, screen every revenue, expenditure and balance-sheet option for legal availability, score each on dollars by year, service impact in service units, equity, reversibility and implementation time, refuse one-time money for a structural hole unless it is a dated bridge, and assemble two or three packages that each balance with the reserve policy tested — distinct from a nonprofit's restricted-fund budget (nonprofit_operating_budget_restrictions) and from a company's budget-variance investigation."
techniques:
  - NE-11
  - RT-02
  - QA-09
  - RT-23
difficulty: advanced
tags:
  - municipal-budget
  - local-government-finance
  - structural-deficit
  - fund-balance-policy
  - service-level-trade-offs
  - budget-equity-analysis
  - city-budget-gap
  - where-to-cut-spending
  - balance-the-budget
updated: "2026-10-03"
reasoning:
  styles: [quantitative, comparative, normative, analytic]
  stakes: high
  horizon: years
  uncertainty: risk
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: team
  output_format: [structured, matrix]
  user_role: [budget_analyst, finance_director, city_manager, council_staff]
  mode: [synthesize, decide, document]
related_prompts:
  - domain-policy/policy_options_memo.md
  - domain-business-strategy/nonprofit/nonprofit_operating_budget_restrictions.md
  - domain-finance/corporate-finance-fpa/finance_budget_variance_investigator.md
---

# Local Government Budget Shortfall Options

**Objective:** Turn a projected budget gap into a set of legally available, costed
and equity-tested options, and into two or three balanced packages an elected body
can choose between — with the one-time versus structural distinction kept honest
and the service consequences stated in units residents would notice.

**Audience:** Budget and finance staff in cities, counties, school and special
districts; city or county managers; council and board staff; and civic analysts
reviewing a proposed budget.

**When to Use:**
- The forecast shows expenditures exceeding revenues for next fiscal year and the
  body must adopt a balanced budget.
- Leadership is proposing "use reserves" or "freeze vacancies" and you need to show
  what each buys and what it leaves for next year.
- A mid-year revenue shortfall forces in-year reductions.
- **Not this prompt if** you run a **nonprofit** budget with donor restrictions —
  `domain-business-strategy/nonprofit/nonprofit_operating_budget_restrictions.md`
  handles restricted versus unrestricted funds for a charity. A company's
  actual-versus-budget explanation is
  `domain-finance/corporate-finance-fpa/finance_budget_variance_investigator.md`. For
  a single policy choice with values trade-offs across many criteria, use
  `domain-policy/policy_options_memo.md`; this prompt is the fiscal engine underneath it.

## Inputs / Context

1. **The forecast**: current-year and next-year general fund revenues and
   expenditures, and a 3–5 year projection with its growth assumptions.
2. **The gap's composition**: which items are recurring (wage settlements, pension
   rate increases, lost recurring revenue) and which are one-time (an election,
   a legal settlement, a storm).
3. **Fund structure and reserves**: unassigned general fund balance, the adopted
   reserve policy, restricted and enterprise funds, and interfund transfers.
4. **Legal constraints**: balanced-budget rules, tax and levy limits, voter-approval
   thresholds, collective bargaining agreements, state or federal mandates,
   maintenance-of-effort and debt covenants.
5. **Service data**: positions, vacancies, and service measures by department
   (response times, cycle times, hours open, caseloads).
6. **Equity data**: who uses each service by neighbourhood, income or age, and the
   incidence of fees and taxes.

Tag each figure `[data]` (adopted budget, audited CAFR/ACFR, payroll),
`[estimate]` (derived) or `[assumption]`. Legal availability of any option is marked
`[verify — finance director / city attorney]`, never asserted.

## Method

1. **Size and split the gap (NE-11).**
   `Gap_t = Expenditures_t − Revenues_t`;
   `Structural gap = recurring expenditures − recurring revenues`;
   `One-time gap = Gap_t − structural gap`. Project the structural gap for years 2–3.
   A gap that grows each year is structural, whatever this year's label says.
2. **Screen for legal availability.** Before scoring, drop or flag what cannot be
   used: restricted or enterprise funds for general purposes, revenue requiring a
   vote that cannot be held in time, bargained terms that need negotiation. A
   blocked option stays on the list with its blocker and earliest date.
3. **Build the long list across four families.** Revenue (fee cost-recovery, levy
   within limits, new taxes needing approval), expenditure (vacancies, service
   reductions, efficiencies, shared services), capital and maintenance deferral,
   and balance-sheet (reserves, refinancing, interfund loans).
4. **Score each option (RT-02).** Dollars in year 1 and year 2 (separately),
   recurring or one-time, service impact in service units, who bears it, legal
   status, time to implement, and reversibility.
5. **Reversibility and deferral cost (QA-09).** Note what is hard to undo (closing a
   facility, losing trained staff, selling an asset) and what deferral costs later
   (deferred maintenance compounding, fleet repair costs).
6. **Apply the matching rule.** One-time resources close one-time gaps. Using them
   for a structural gap is allowed only as a **dated bridge** to recurring options
   that are already adopted and phase in by a stated year.
7. **Assemble 2–3 packages.** Each must balance year 1, show the year-2 structural
   position, and keep the reserve at or above policy after any draw. A package that
   does not balance is shown with its shortfall — it tells the body the price of
   protecting something.
8. **Equity check.** For each package, which groups and neighbourhoods carry the
   service loss or fee increase, and any mitigation (fee waivers, protecting the
   highest-use site).
9. **Decisions for the body.** The values choices left to elected officials, in plain
   words, without a recommendation dressed as arithmetic.

## Output Format

```
# Budget shortfall options — [jurisdiction]   FY [..]   General fund $[..]
Inputs: [n data / n estimate / n assumption]

## 1. Gap
| Year | Revenue | Expenditure | Gap | Structural | One-time |
## 2. Reserves
Unassigned balance $[..] = [..]% · policy minimum [..]% = $[..] · headroom $[..]
## 3. Options
| ID | Option | Yr1 $ | Yr2 $ | Recurring? | Service impact | Who bears | Legal status | Reversible? |
## 4. Blocked or deferred options (blocker · earliest date)
## 5. Packages
| Package | Yr1 closes? | Yr2 structural position | Reserve after | One-time used for structural? |
## 6. Equity and mitigation
## 7. Decisions for the body
```

## Verification

- [ ] Gap is split into structural and one-time, with years 2–3 projected.
- [ ] Every option's legal availability is marked; none is asserted as lawful.
- [ ] Year-1 and year-2 dollars are separate; recurring and one-time never summed blindly.
- [ ] Each package's arithmetic recomputes and balances, or its shortfall is shown.
- [ ] Reserve after each package is tested against the adopted policy.
- [ ] Any one-time money used for a structural gap is labelled a dated bridge.
- [ ] Service impacts are in service units (days, hours, response time), not "reduced".

## False-Positive Prevention

1. **Balanced this year, broken next.** Reserves, deferrals and asset sales close
   year 1 and leave the structural gap intact. Year 2 is shown every time.
2. **"Vacancy savings" as free.** Unfilled positions usually carry real service
   loss; name the service.
3. **Phase-in ignored.** A change needing bargaining or a new contract rarely yields
   a full year's saving in year 1.
4. **Counting a vote before it happens.** Revenue needing voter or state approval is
   not in a package until approved.
5. **Deferral as saving.** Deferred maintenance and fleet replacement usually cost
   more later; show the later cost.
6. **Across-the-board cuts as neutral.** Equal percentage cuts fall unequally on
   services used by lower-income residents. Show who bears them.
7. **Reserve floor as target.** Drawing to exactly the policy minimum leaves no
   cushion for the next shock; state the remaining cushion.

## Example Output

```
# Budget shortfall options — City of Riverbend (illustrative, pop. ~85,000)
FY 2027   General fund expenditures $142.0 M   Inputs: 9 data / 6 estimate / 2 assumption

## 1. Gap
| FY27 | Rev 133.6 | Exp 142.0 | Gap 8.4 | Structural 6.1 | One-time 2.3 |
One-time: election 0.6 + retro pay settlement 1.7 [data]. FY28 structural 6.4 [estimate] (wage step growth net of revenue growth).

## 2. Reserves
Unassigned $26.0 M = 18.3% of expenditures. Policy minimum 16.7% (two months) = $23.7 M.
Headroom $2.3 M.

## 3. Options (FY27 / FY28, $M)
| R1 | Fees to 85% cost recovery (rec, permits), net of $0.2 M scholarships | 1.20 | 1.20 | Rec | Youth program cost +$40/season | Fee payers | Council authority [verify] | Yes |
| R2 | Levy +0.8% within 2% no-vote cap | 0.43 | 0.43 | Rec | — | Property owners | Within cap [verify] | Yes |
| E1 | Eliminate 22 vacancies (8 in parks) | 2.60 | 2.60 | Rec | Mowing cycle 14 → 21 days | Park users | OK | Slow to rehire |
| E2 | Close 3 branch libraries one day/week | 0.45 | 0.45 | Rec | 1,450 visits/week displaced | Eastside branch users | OK | Yes |
| E4 | Fire overtime: staffing-policy change | 0.45 | 0.90 | Rec | None if minimum staffing kept | — | Meet-and-confer | Yes |
| E5 | Shared dispatch with county | −0.20 | 0.70 | Rec | Transition risk | — | IGA needed | Hard |
| E3 | Defer fleet replacement 1 yr | 1.10 | −0.15 | One-time | Repair cost +$0.15 M/yr | — | OK | Yes |
| B1 | Reserve draw (up to headroom) | ≤2.30 | 0 | One-time | — | Future budgets | Policy OK | — |
| B2 | Refinance 2016 bonds | 0.35 | 0.35 | Rec | — | — | Bond counsel [verify] | — |

## 4. Blocked
R3 Utility users tax ($3.5 M/yr) — needs voter approval; earliest Nov 2027 ballot.

## 5. Packages
A — Structural first: R1 + R2 + E1 + E2 + E4 + E5 + B2 = 5.28 recurring-type FY27;
    + E3 1.10 + B1 2.02 → 8.40 ✓. FY28 recurring 6.63 − E3 repair 0.15 = 6.48 vs 6.4 structural ✓ (margin 0.08).
    One-time covers 0.82 of FY27 structural gap — dated bridge to E4/E5 full year in FY28.
    Reserve after: 26.0 − 2.02 = 23.98 = 16.9% ✓ (cushion $0.3 M — thin).
B — Protect parks and libraries (drop E2, E1 limited to 14 non-parks vacancies 1.70):
    FY27 3.93 + 3.40 one-time = 7.33 → short 1.07 ✗. FY28 5.13 vs 6.4 → short 1.27 ✗.
    Price of protecting both: $1.35 M/yr recurring — affordable only if R3 passes.

## 6. Equity
E2 falls mostly on the Eastside branch (lowest-income tract, highest use). Mitigation:
close the two lower-use branches two days instead — same saving [estimate], Eastside kept.
R1 scholarships hold youth fees flat for households under 200% of poverty line.

## 7. Decisions for the body
1. Accept a slower mowing cycle, or fund parks by placing R3 on the 2027 ballot?
2. Draw reserves to within $0.3 M of policy, or adopt E3 deferral plus a smaller draw?
3. Begin shared-dispatch negotiations now (FY28 saving depends on it)?
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — gap split, reserve percentages, and package totals that recompute.
- **RT-02 Multi-Dimensional Analysis Framework** — dollars, service, equity, legality, reversibility scored separately.
- **QA-09 Reversibility Assessment** — hard-to-undo cuts and the later cost of deferral named.
- **RT-23 Input Provenance Tagging** — every figure tagged data / estimate / assumption; legal status marked for verification.

## Related Prompts

- `domain-policy/policy_options_memo.md` — the decision memo when the choice is wider than the fiscal arithmetic.
- `domain-business-strategy/nonprofit/nonprofit_operating_budget_restrictions.md` — the nonprofit equivalent, with donor restrictions.
- `domain-finance/corporate-finance-fpa/finance_budget_variance_investigator.md` — explaining actuals versus budget in a company.
