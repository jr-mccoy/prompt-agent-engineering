---
title: "Nonprofit Operating Budget — Restricted vs Unrestricted, Indirect Recovery, Functional Allocation"
category: business-strategy/nonprofit
description: "Build or diagnose a nonprofit's annual operating budget the way restrictions actually constrain it — revenue by restriction class and releases, restricted money matched only to eligible costs, indirect-cost recovery against the organisation's real indirect rate, shared costs allocated to program, management and fundraising on stated bases, and the unrestricted gap and reserve months that result; distinct from finance_budget_variance_investigator (explaining actuals against a budget) and science_grant_budget_justification_drafter (one research grant's budget narrative)."
techniques:
  - NE-11
  - OC-03
  - RT-05
  - DD-05
  - QA-01
difficulty: advanced
tags:
  - nonprofit
  - budgeting
  - restricted-funds
  - indirect-costs
  - functional-expenses
  - reserves
  - finance
updated: "2026-09-24"
related_prompts:
  - domain-finance/corporate-finance-fpa/finance_budget_variance_investigator.md
  - domain-science/grants-funding/science_grant_budget_justification_drafter.md
  - domain-business-strategy/nonprofit/nonprofit_foundation_grant_proposal.md
---

# Nonprofit Operating Budget with Restrictions

**Objective:** Show the executive director and board whether next year's budget
actually balances once restrictions are respected — which costs restricted money may
pay, how much unrestricted money the organisation must raise, how far indirect-cost
recovery falls short of the real cost of running the place, and how many months of
reserves stand behind the plan.

**When to Use:**
- Building next year's budget, or before the board approves it.
- The budget "balances" in total but cash is always tight in unrestricted funds.
- A new grant is on offer and nobody knows whether it helps or costs money.
- Preparing to negotiate an indirect-cost rate with a funder.

**Not this prompt if:**
- You are explaining last month's actuals against budget —
  `domain-finance/corporate-finance-fpa/finance_budget_variance_investigator.md`.
- You need one research grant's budget justification —
  `domain-science/grants-funding/science_grant_budget_justification_drafter.md`.
- You need a determination of how a specific gift must be classified or reported, or
  what the tax filing requires — that is the auditor's or accountant's call; this
  prompt flags it.

## Inputs

1. Expected revenue by source, with each source's restriction: none, purpose
   (which program), or time (which period).
2. Restricted balances from prior years expected to be released this year.
3. Each grant's terms: eligible costs, indirect-cost cap or negotiated rate.
4. Direct costs per program and fundraising; shared costs (leadership, finance,
   rent, insurance, IT, audit).
5. Allocation bases: staff time estimates, square footage, headcount.
6. Unrestricted liquid reserves at year start.

## Method

1. **Classify revenue (RT-05).** Two classes: without donor restrictions, and with
   donor restrictions (purpose or time). Add prior-year releases. Every classification
   cites the gift agreement or grant letter; anything ambiguous is flagged.

2. **Match restricted money to eligible costs only.** For each restricted source:
   eligible direct costs it may pay, the indirect it may recover, and any program
   cost it cannot cover. The uncovered remainder falls to unrestricted funds.

3. **Allocate shared costs on stated bases (NE-11).**
   `shared cost × allocation % = amount to each function`
   Program, management and general, fundraising. The bases (time, space) are written
   down so the auditor and next year's budget can reproduce them.

4. **Compute the real indirect rate.**
   `indirect rate = management & general ÷ direct program costs`
   Compare with what funders pay. The difference is the subsidy unrestricted money
   gives restricted programs — state it in dollars.

5. **Find the unrestricted gap.**
   `unrestricted need = uncovered program direct + shared + fundraising − indirect recovered`
   `gap = unrestricted revenue − unrestricted need`
   Then `reserve months = unrestricted liquid reserves ÷ (total expenses ÷ 12)`.

6. **Present options (OC-03).** Negotiate indirect, raise unrestricted, reduce shared
   cost, decline or restructure a grant. Each with its dollar effect.

7. **Flag for qualified review (DD-05).** Restriction interpretations, time-release
   timing, classification of any grant as a contribution or an exchange, and the
   functional expense presentation in public filings — auditor or accountant.

8. **Check (QA-01).** Functional totals equal total expenses; revenue plus gap equals
   expenses; allocation percentages sum to 100%.

## Output Format

```
# Operating budget with restrictions — [organisation], FY[yyyy]

## Revenue by restriction class
| Source | Amount | Class | Restriction | Document |

## Restricted money against eligible costs
| Source | Direct paid | Indirect recovered | Program cost left uncovered |

## Shared-cost allocation
| Shared cost | Basis | Program(s) | M&G | Fundraising |

## Functional expense summary
| Function | Direct | Allocated | Total | % |

## Indirect reality
Real rate [x%] vs funder rates [y%] → subsidy [$]

## Unrestricted position
Need / revenue / gap / reserve months

## Options
| Option | Effect on gap | Risk |

## Flags for qualified review
```

## Verification

- [ ] Every restricted source cites its document.
- [ ] No restricted dollar pays a cost outside its restriction.
- [ ] Allocation percentages sum to 100% per shared cost.
- [ ] Functional totals equal total expenses.
- [ ] Total revenue + gap = total expenses.
- [ ] Classification and filing questions are flagged, not decided.

## False-Positive Prevention

1. **A balanced total can hide an unrestricted deficit.** $100,000 restricted to one
   program does not pay the rent. Always compute the unrestricted line separately.
2. **A grant can cost money.** A grant at a 10% indirect cap for a program whose
   real indirect rate is 40% is a subsidy from unrestricted funds; say how much.
3. **Allocation is not optional decoration.** Reporting all leadership time as
   administration understates program cost; reporting it all as program overstates
   efficiency. Use a stated basis.
4. **Do not reclassify to make a ratio look good.** Low "overhead" achieved by moving
   costs is a reporting problem, not a strength.
5. **Do not decide restriction questions.** "The donor probably won't mind" is not a
   release; flag it and ask the donor or auditor.
6. **Released-from-restriction is not new money.** It is last year's gift being used;
   it cannot be counted twice.
7. **Dual failure:** a budget so conservative it assumes no unrestricted growth may
   close programs that the board would fund with a clear ask.

## Example Output

```
# Operating budget with restrictions — Riverbend Literacy, FY2027

## Revenue by restriction class
| Source | Amount | Class | Restriction | Document |
| Literacy foundation grant | $57,500 | With restrictions | Literacy program; 15% indirect cap | Award letter |
| City contract | $20,000 | With restrictions | Literacy direct costs only | Contract §4 |
| ESL foundation grant | $92,000 | With restrictions | ESL program; 15% indirect cap | Award letter |
| Released: ESL year-2 installment | $30,000 | Release (time) | Received FY26 for FY27 | Grant schedule |
| Individuals | $118,000 | Without restrictions | — | Giving forecast |
| Events (net) | $32,000 | Without restrictions | — | Event budget |
| Board giving | $18,000 | Without restrictions | — | Pledges |
| Workshop fees | $12,000 | Without restrictions | — | Fee schedule |
Total $379,500

## Restricted money against eligible costs
| Source | Direct paid | Indirect | Uncovered |
| Literacy grant + city | $50,000 + $20,000 | $7,500 | Literacy direct $76,000 − $70,000 = $6,000 |
| ESL grant + release | $80,000 + $30,000 | $12,000 | ESL direct $118,000 − $110,000 = $8,000 |
Indirect recovered: $19,500

## Shared-cost allocation
| Shared cost | Basis | Literacy | ESL | M&G | Fundraising |
| ED salary + benefits $96,000 | Time 15/15/45/25% | $14,400 | $14,400 | $43,200 | $24,000 |
| Rent $36,000 | Sq ft 40/40/12/8% | $14,400 | $14,400 | $4,320 | $2,880 |
| Audit, insurance, IT $32,000 | M&G | — | — | $32,000 | — |

## Functional expense summary
| Function | Direct | Allocated | Total | % |
| Literacy | $76,000 | $28,800 | $104,800 | 25.0% |
| ESL | $118,000 | $28,800 | $146,800 | 35.0% |
| Management & general | — | $79,520 | $79,520 | 18.9% |
| Fundraising | $62,000 | $26,880 | $88,880 | 21.2% |
| Total | | | $420,000 | 100% (rounded) |

## Indirect reality
Real rate: M&G $79,520 ÷ program direct $194,000 = 41.0%; funders pay 15% on
$150,000 of grant-funded direct = $19,500. Unrestricted funds subsidise the gap.

## Unrestricted position
Need: $6,000 + $8,000 + shared $164,000 + fundraising direct $62,000 − $19,500 = $220,500
Revenue: $180,000 → gap −$40,500 (= $420,000 − $379,500)
Reserves: $60,000 ÷ ($420,000 ÷ 12 = $35,000) = 1.7 months; the gap would use 68%.

## Options
| Option | Effect | Risk |
| Ask literacy funder for 25% indirect at renewal | +$5,000 | Funder policy may not allow |
| Raise unrestricted individual giving 15% | +$17,700 | Needs appeal + major-gift plan |
| Defer IT upgrade | +$8,000 | Security debt |
| Board-designated draw from reserves | covers remainder | Reserves fall below 1 month |

## Flags for qualified review
- Whether the ESL year-2 installment is released in FY27 as scheduled — auditor
- Functional allocation bases for the public filing — accountant
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas:** allocation, indirect rate, gap and reserves.
- **OC-03 Markdown Table Specification:** restriction and functional tables the board can audit.
- **RT-05 Evidence-Based Reasoning:** every restriction cites its document.
- **DD-05 Human Review Flags:** classification and filing questions routed to the auditor.
- **QA-01 Self-Verification:** totals reconcile across tables.

## Related Prompts

- `domain-finance/corporate-finance-fpa/finance_budget_variance_investigator.md` — actuals against this budget
- `domain-science/grants-funding/science_grant_budget_justification_drafter.md` — one research grant's budget
- `domain-business-strategy/nonprofit/nonprofit_foundation_grant_proposal.md` — the proposals that set these restrictions
