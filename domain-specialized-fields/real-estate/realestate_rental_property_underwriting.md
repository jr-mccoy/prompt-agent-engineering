---
title: "Rental Property Underwriting — NOI, Cap Rate, DSCR, Cash-on-Cash, Reserves, and a Stress Test That Can Say No"
category: specialized-fields/real-estate
description: "Underwrite one small residential rental (1–4 units or a single-family rental) from a sourced rent roll and a line-item expense budget: effective gross income, NOI, cap rate, debt service, DSCR, cash-on-cash, break-even occupancy and a reserve requirement, then stress rents, vacancy and a known capital item and return a GREEN / AMBER / RED / INSUFFICIENT DATA verdict against the investor's own thresholds — distinct from the owner-occupier buy-vs-rent analysis (domain-finance) and from lender-side debt sizing."
techniques:
  - NE-11
  - RT-23
  - QA-02
  - DP-28
difficulty: advanced
tags:
  - real-estate
  - rental-property
  - underwriting
  - cap-rate
  - dscr
  - cash-on-cash
  - investing
  - first-rental
  - will-it-profit
  - becoming-a-landlord
updated: "2026-09-24"
reasoning:
  styles: [quantitative, analytic, adversarial]
  stakes: high
  horizon: years
  uncertainty: risk
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: solo
  output_format: [structured, matrix]
  user_role: [investor, real_estate_agent, analyst]
  mode: [diagnose, decide]
related_prompts:
  - domain-finance/personal-finance-planning/finance_buy_vs_rent_analysis.md
  - domain-finance/credit-lending/finance_debt_capacity_sizing.md
  - domain-specialized-fields/real-estate/realestate_inspection_report_triage.md
---

# Rental Property Underwriting

**Objective:** Decide whether one small rental property meets the investor's
thresholds at the asking price — from sourced rents and a full expense budget —
and, if not, state the price or condition at which it would.

**When to Use:**
- You are evaluating a duplex, triplex, fourplex or single-family rental before an
  offer, and the listing's "pro forma" is the only analysis so far.
- A deal "cash-flows" on a napkin and you want every expense line in before you believe it.
- You need to know how much reserve to hold and what happens if rents soften.
- **Not this prompt if** you will live in the home and are comparing buying with
  renting — `domain-finance/personal-finance-planning/finance_buy_vs_rent_analysis.md`.
  If you are the lender sizing a loan, use
  `domain-finance/credit-lending/finance_debt_capacity_sizing.md`. Commercial
  multifamily (5+ units) needs a full operating-statement review beyond this prompt.
  Tax effects (depreciation, passive-loss rules) are a CPA question; this prompt is pre-tax.

## Inputs / Context

1. **Price, units, and condition** — including capital items from the inspection.
2. **Rent roll:** current rent per unit, lease end dates, and the source — actual
   leases, the seller's statement, or market rents **you** gathered (listings,
   property manager). Tag each.
3. **Expenses, line by line:** property tax (current bill and any reassessment on
   sale), insurance quote, utilities the owner pays, HOA, management (even if
   self-managing), repairs, capital reserve, turnover and leasing, landscaping/snow.
4. **Financing:** down payment %, rate, term, closing costs, initial repairs.
5. **Thresholds:** minimum DSCR (base and stressed), minimum cash-on-cash, reserve
   months. If none, defaults below are used and labelled.

## Method

1. **Tag every figure (RT-23).** `[lease]` signed lease · `[seller]` seller or
   listing claim · `[user-market]` rents the user gathered · `[quote]` insurer or
   contractor quote · `[estimate]` a figure this prompt proposed. Seller rents that
   no lease supports are underwritten at `[user-market]` rents if lower.

2. **Build income (NE-11).**
   `GPI = Σ monthly rents × 12` · `Vacancy & credit loss = GPI × v` (default 6%;
   never 0) · `EGI = GPI − vacancy + other income`.

3. **Build expenses line by line.** Management is charged even when self-managed
   (your time is a cost; a buyer after you will pay it). Capital reserve is separate
   from repairs. The "50% rule" is a cross-check only: if expenses/EGI is far below
   ~40%, something is missing.

4. **Compute the core ratios.**
   - `NOI = EGI − operating expenses` (debt service is not an expense)
   - `Cap rate = NOI ÷ price`
   - `Annual debt service = 12 × P·r / (1 − (1 + r)^−n)`
   - `DSCR = NOI ÷ annual debt service`
   - `Cash flow = NOI − debt service`
   - `Cash-on-cash = cash flow ÷ (down + closing costs + initial repairs)`
   - `Break-even occupancy = (opex + debt service) ÷ GPI`
   - `Reserve = 6 × monthly PITI + known capital items` (default)

5. **Stress it (QA-02).** At minimum: rents −8%, vacancy to 10%, and the largest
   known capital item landing in year 1. Recompute NOI, DSCR and cash flow.

6. **Solve for the price that clears.** For a failing deal, compute the price at
   which the binding threshold is met (hold LTV and rate constant), and say which
   thresholds price alone cannot fix.

7. **Apply the verdict (DP-28).** Default thresholds: DSCR ≥ 1.20 base and ≥ 1.00
   stressed; cash-on-cash ≥ 5%.
   - **GREEN** — all thresholds met base and stressed.
   - **AMBER** — base met, stressed DSCR < 1.00 or one threshold within 10% of its bar.
   - **RED** — any base threshold missed.
   - **INSUFFICIENT DATA** — no insurance quote, no tax figure, or rents only
     `[seller]` with no market check; name the datum that unblocks it.

## Output Format

```
# Underwriting — [property] — ask $[..] — as of [date]
Thresholds: [investor's | default]

## Income
| Unit | Rent | Source | Lease end |
GPI / vacancy (v%) / EGI

## Expenses
| Line | Annual | Source |
Total opex, expense ratio

## Returns at ask
NOI · cap rate · debt service · DSCR · cash flow · cash invested · CoC · break-even occupancy

## Stress
| Scenario | NOI | DSCR | Cash flow |

## Reserve
## Price that clears
## Verdict
[GREEN | AMBER | RED | INSUFFICIENT DATA] — threshold that decided it
## Not tax, legal or lending advice
```

## Verification

- [ ] Every income and expense line has a source tag; no seller rent is used above market without a lease.
- [ ] Vacancy is > 0 and management is charged.
- [ ] NOI excludes debt service; DSCR and CoC are recomputed from the lines shown.
- [ ] The stress scenario changes at least rents, vacancy and one capital item.
- [ ] The verdict names the threshold that decided it.

## False-Positive Prevention

1. **The listing's pro forma is marketing.** Seller "market rents" and "potential"
   income are `[seller]` until a lease or your own market check supports them.
2. **Zero vacancy is a sales tool.** Every unit turns; every tenant pays late eventually.
3. **Self-management is not free.** Leaving it out overstates NOI and understates
   what the next buyer will pay.
4. **Repairs are not capital reserve.** A roof, a furnace and a parking surface
   arrive on their own schedule; a monthly reserve is how you pay for them.
5. **Taxes reset on sale in many places.** Underwriting at the seller's old bill
   can overstate NOI; ask the assessor's rule, don't assume.
6. **Cap rate says nothing about your financing.** A 6.7% cap can still have a DSCR
   under 1.2 at today's rates; report both.
7. **Appreciation is not in this verdict.** A deal that only works if the price
   rises is a speculation — say so, rather than hiding it in the returns.
8. **Do not give tax advice.** Depreciation and loss treatment go to a CPA.

## Example Output

```
# Underwriting — triplex, Orchard St — ask $465,000 — as of 2026-09-24
Thresholds: investor's — DSCR ≥1.20 base / ≥1.00 stressed; CoC ≥5%

## Income
| Unit 1 | $1,650 | [lease] | 2027-03 |
| Unit 2 | $1,650 | [lease] | 2026-12 |
| Unit 3 | $1,650 | [user-market] (vacant; seller claims $1,800) | — |
GPI $59,400 · vacancy 6% $3,564 · EGI $55,836

## Expenses
| Property tax | $6,045 | [user] assessor: 1.3% of price on sale |
| Insurance | $2,700 | [quote] |
| Management 9% of EGI | $5,025 | [estimate] |
| Repairs & maintenance | $3,000 | [estimate] $1,000/unit |
| Capital reserve | $3,600 | [estimate] $100/unit/mo |
| Water/sewer/trash (owner-paid) | $2,340 | [user] 12 months of bills |
| Landscaping/snow | $700 | [quote] |
| Turnover & leasing | $1,050 | [estimate] |
Total opex $24,460 · expense ratio 43.8%

## Returns at ask
NOI $31,376 · cap rate 6.75%
Loan $348,750 (75% LTV), 6.75%, 30 yr → $2,262/mo → debt service $27,144
DSCR 1.16 · cash flow $4,232
Cash invested: down $116,250 + closing $9,300 + initial repairs $7,500 = $133,050
CoC 3.2% · break-even occupancy (24,460 + 27,144) ÷ 59,400 = 86.9%

## Stress (rents −8%, vacancy 10%, roof section $9,000 in year 1)
| Rents/vacancy | NOI $25,322 | DSCR 0.93 | cash flow −$1,822 |
| + roof section | — | — | year-1 cash −$10,822 |

## Reserve
6 × PITI (2,262 + 504 tax + 225 ins = $2,991) = $17,946 + roof section $9,000
= $26,946 held after closing.

## Price that clears
DSCR 1.20 at 75% LTV: max debt service 31,376 ÷ 1.20 = $26,147 → loan $335,941
→ price ≈ $448,000. At $448,000, CoC ≈ 4.1% (cash flow $5,229 ÷ $128,460):
still below 5%. Price alone cannot meet the CoC bar; rents or rate must move.

## Verdict
RED — base DSCR 1.16 < 1.20 and CoC 3.2% < 5%. At ≈$448,000 the DSCR clears but
the return does not: at any price near ask this is an appreciation bet, not a
cash-flow deal. Unit 3 at the seller's $1,800 would add $1,800 GPI (≈$1,540 NOI
after vacancy and management): DSCR 1.21, CoC 4.3% — still RED on return, and only
after a signed lease proves the rent.

## Not tax, legal or lending advice
Pre-tax figures from the sources tagged; confirm taxes with the assessor and the
loan terms with the lender.
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — every ratio shown as a formula and recomputable.
- **RT-23 Input Provenance Tagging** — lease, seller, market, quote and estimate kept apart.
- **QA-02 Adversarial Stress-Test** — rents, vacancy and a capital item attacked together.
- **DP-28 Traffic-Light Verdict System** — thresholds decide the colour, not the mood.

## Related Prompts

- `domain-finance/personal-finance-planning/finance_buy_vs_rent_analysis.md` —
  the owner-occupier decision.
- `domain-finance/credit-lending/finance_debt_capacity_sizing.md` — the lender's
  side of coverage and leverage.
- `domain-specialized-fields/real-estate/realestate_inspection_report_triage.md` —
  where the capital items in the stress test come from.
