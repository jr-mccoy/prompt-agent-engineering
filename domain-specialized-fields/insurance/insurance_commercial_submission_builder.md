---
title: "Broker Commercial Lines Submission Builder — Exposures, Loss Runs, COPE, and an Underwriter-Ready Narrative"
category: specialized-fields/insurance
description: "For a commercial insurance broker or account executive preparing a new-business or remarketed submission: assemble exposure data with every figure source-tagged, summarise and develop loss runs (frequency, severity, open reserves, large losses explained, corrective action), build property COPE schedules with TIV and valuation basis, list what is missing before it goes to market, and write the account narrative that answers an underwriter's first questions — distinct from a business owner's own coverage-gap review (finance_business_insurance_coverage_review) and from comparing quoted policies for a client (domain_writing_insurance_comparison)."
techniques:
  - RT-23
  - NE-11
  - NE-23
  - IPC-11
difficulty: advanced
tags:
  - commercial-insurance
  - insurance-broker
  - underwriting-submission
  - loss-runs
  - cope
  - account-narrative
  - get-quotes-from-insurers
  - prepare-account-for-market
  - market-the-account
updated: "2026-10-02"
reasoning:
  styles: [synthetic, quantitative, communicative, systematic]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, prose]
  user_role: [insurance_broker, account_executive, account_manager]
  mode: [synthesize, communicate]
related_prompts:
  - domain-specialized-fields/insurance/insurance_underwriting_risk_assessment.md
  - domain-specialized-fields/insurance/insurance_renewal_remarketing_plan.md
  - domain-finance/risk-management/finance_business_insurance_coverage_review.md
---

# Broker Commercial Lines Submission Builder

**Objective:** Send underwriters a submission they can quote from on first read —
complete exposures, developed losses with the large ones explained, a property
schedule with credible values, and a narrative that answers the questions they would
otherwise send back — so the account is quoted on its merits rather than declined
for missing information or priced for the unknown.

**When to Use:**
- A new commercial account (property, general liability, auto, workers' compensation,
  umbrella, or a package) is going to market.
- An existing account is being remarketed and last year's submission was thin.
- An underwriter has declined or asked for "more information" and you need to know
  what was missing.
- **Not this prompt if** you are the **business owner** checking whether your own
  cover fits your exposures — `domain-finance/risk-management/finance_business_insurance_coverage_review.md`
  does that from the buyer's side. Turning received quotes into a client-facing
  comparison is `domain-professional-writing/domain-specific/domain_writing_insurance_comparison.md`.
  Deciding whether to remarket at all, and the timeline, is
  `domain-specialized-fields/insurance/insurance_renewal_remarketing_plan.md`.
  The underwriter's side of the same file is
  `domain-specialized-fields/insurance/insurance_underwriting_risk_assessment.md`.

## Inputs / Context

1. **Applications and supplements** completed by the insured (ACORD or carrier forms).
2. **Exposure data**: revenue by operation, payroll by class code, vehicle schedule
   and driver list, subcontractor costs, products, locations, employee counts.
3. **Property schedule**: per location — construction, occupancy, protection,
   exposure (COPE), year built and updates, square footage, sprinklers and alarms,
   building / contents / business-income values and how they were set.
4. **Loss runs**: carrier-issued, valued within the last 90 days, covering at least
   5 years per line, plus large-loss descriptions and corrective actions.
5. **Current program**: carriers, limits, retentions, premiums, expiring terms.
6. **Account story**: ownership, years in business, safety and risk-management
   programs, contracts requiring specific cover, why the account is moving.

Every figure is tagged `[insured]`, `[loss run, valued <date>]`, `[inspection]`,
`[broker estimate]` or `[NOT PROVIDED]`. Nothing is filled from memory; insured
statements are labelled as such, not as verified.

## Method

1. **Completeness check (IPC-11).** Build the missing-items list first: loss runs
   older than 90 days, years without loss runs, locations without COPE, vehicles
   without VINs or garaging, payroll without class codes, values without a basis.
   Each gap carries forward into the narrative as a stated open item.
2. **Exposure summary (RT-23).** Line by line: rating basis (sales, payroll,
   units, TIV), current and prior-year values, change and why.
3. **Loss analysis (NE-11).** Per line and year: claim count, paid, outstanding
   reserves, incurred; frequency per $M revenue or per 100 vehicles; loss ratio to
   expiring premium where premium is known. For the latest 1–3 years, note that
   incurred will develop; show a simple development factor only if the user
   supplies one or a carrier triangle.
4. **Large losses.** Each claim above a threshold (e.g. $25k or 10% of premium):
   what happened, status, reserve, root cause, and the corrective action with date.
   An unexplained large loss is the single most common reason for a high quote.
5. **Property schedule.** COPE per location, TIV, valuation basis (replacement cost,
   recent appraisal, or insured estimate), and a flag where values look stale
   (e.g. no update in 3+ years of construction-cost inflation).
6. **Narrative (NE-23).** One to two pages: operations, management, safety culture,
   loss story, changes since last year, and the expiring program — written to
   pre-empt the questions an underwriter in this class would ask.
7. **Market notes.** Which line goes to which market and why (appetite, class),
   the target terms, and anything the insured will not accept.

## Output Format

```
# Submission — [insured]   Lines: [..]   Effective: [..]   Broker: [..]

## Missing before market (blockers first)
| Item | Line | Why it matters | Owner | Due |

## Account narrative (1–2 pages)

## Exposure summary
| Line | Rating basis | Prior | Current | Change | Source |

## Loss summary (5+ years)
| Line | Year | # claims | Paid | Reserves | Incurred | Freq./unit | Source / valued |
Large losses: [date, description, incurred, status, root cause, corrective action]

## Property / COPE schedule
| Loc | Construction | Occupancy | Protection | Exposure | Bldg | Contents | BI | Basis |

## Expiring program and target terms
## Market plan notes
```

## Verification

- [ ] Every figure carries a source tag; insured statements are not presented as verified.
- [ ] Loss runs cover 5+ years per line and are valued within 90 days, or the gap is listed.
- [ ] Frequency and incurred totals recompute from the rows.
- [ ] Every large loss has a cause and a dated corrective action, or says none.
- [ ] Each location has COPE and a valuation basis.
- [ ] The narrative mentions every open item rather than hiding it.

## False-Positive Prevention

1. **Clean loss runs that are incomplete.** "No losses" on a run that covers two of
   five years, or one carrier of two, is missing data, not a good record.
2. **Reserves as final.** Recent-year incurred is immature; a quiet current year can
   still develop.
3. **Stale values.** Building values carried unchanged for years understate TIV and
   invite coinsurance problems on a loss; flag them rather than market them.
4. **Narrative over data.** Underwriters discount adjectives ("excellent safety
   culture"); cite programs, dates and results.
5. **Hiding the bad loss.** It is in the loss run anyway; explaining it with
   corrective action is the only way to change how it is priced.
6. **Misclassification.** Payroll or sales placed in a cheaper class code may be
   corrected at audit with an additional premium; describe operations accurately.

## Example Output

```
# Submission — Harbor Fabrication LLC (metal fabrication, 2 plants)
Lines: property, GL, auto, WC, umbrella $5M   Effective: 1 Jan 2027

## Missing before market
| WC loss run 2022 (prior carrier) | WC | 5-yr history incomplete | client to request | 25 Oct |
| Plant 2 roof update year | Property | roof age drives wind terms | client | 25 Oct |

## Exposure summary
| GL | sales | $18.2 M | $21.5 M | +18% new trailer-frame contract | [insured] |
| WC | payroll 3632 (machine shop NOC) | $4.1 M | $4.6 M | +6 welders | [insured] |
| Auto | power units | 9 | 11 | 2 box trucks added | [insured] |

## Loss summary (WC)
| 2022 | [NOT PROVIDED] |
| 2023 | 6 | $48k | $0 | $48k | 1.5 / $1M payroll | [loss run, valued 30 Sep 2026] |
| 2024 | 4 | $212k | $35k | $247k | 0.9 | same |
| 2025 | 5 | $31k | $12k | $43k | 1.1 | same |
| 2026 YTD | 2 | $6k | $14k | $20k | — | immature |
WC incurred 2023–26: $358k vs WC premium ~$118k/yr × 4 = $472k [insured] → loss
ratio ≈ 76% (2026 is a part year; treat as a floor).
Large loss: Mar 2024 — welder crush injury (press brake), incurred $247k, closed
except $35k medical reserve. Root cause: light-curtain bypassed. Corrective:
interlocks on all 4 press brakes (May 2024), lockout audit monthly; no
press-brake injury since.

## Property / COPE
| 1 | non-combustible steel | fabrication | sprinklered, PC 3 | 40 ft to warehouse | $6.8 M | $3.2 M | $2.4 M | appraisal 2025 |
| 2 | joisted masonry | fabrication + paint booth | no sprinkler, PC 5 | open | $2.1 M | $1.5 M | $0.8 M | insured est. 2019 — stale |

## Narrative (extract)
Second-generation owners, 31 years in business. WC frequency fell from 1.5 to
0.9–1.1 per $1 M payroll after the 2024 interlock programme; the one large loss is
explained above. Plant 2's paint booth has a dedicated suppression system
(inspected June 2026); the plant's values date from 2019 and a new appraisal is
booked for November.
```

## Techniques Used

- **RT-23 Input Provenance Tagging** — every exposure, loss and value tagged by source and valuation date.
- **NE-11 Embedded Calculation Formulas** — frequency per unit, incurred totals and loss ratio shown so they recompute.
- **NE-23 Objection Pre-emption** — the narrative answers the underwriter's predictable questions (large loss, stale values, growth).
- **IPC-11 Propagating Ignorance Channels** — missing items listed first and carried into the narrative rather than dropped.

## Related Prompts

- `domain-specialized-fields/insurance/insurance_underwriting_risk_assessment.md` — how the underwriter will read this submission.
- `domain-specialized-fields/insurance/insurance_renewal_remarketing_plan.md` — whether to remarket and on what timeline.
- `domain-finance/risk-management/finance_business_insurance_coverage_review.md` — the insured's own exposure-first coverage review.
