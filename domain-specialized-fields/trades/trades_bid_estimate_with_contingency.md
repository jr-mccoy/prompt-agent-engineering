---
title: "Bid Estimate with Contingency — Quantity Takeoff, Allowances, and a Contingency Sized to Named Unknowns Instead of a Flat Ten Percent"
category: specialized-fields/trades
description: "Build the number behind a trade or construction bid: a quantity takeoff with waste factors and sources, labor hours at the contractor's burdened rate, sub quotes, allowances for owner selections, an unknowns register where each unknown is resolved before bid, unit-priced, excluded, or carried in a contingency sized by probability times impact, then overhead, profit and the bid — distinct from writing the customer-facing estimate document (domain_writing_hvac_estimate and siblings) and from scoping a services engagement (client-services-studio stage 3)."
techniques:
  - DT-01
  - NE-11
  - QA-04
  - CM-03
difficulty: intermediate
tags:
  - trades
  - construction
  - estimating
  - bidding
  - contingency
  - allowances
  - contractor
  - pricing-a-job
  - underpriced-jobs
  - hidden-surprises
updated: "2026-09-24"
reasoning:
  styles: [quantitative, systematic, analytic]
  stakes: high
  horizon: weeks
  uncertainty: risk
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, matrix]
  user_role: [contractor, estimator, tradesperson]
  mode: [plan, synthesize]
related_prompts:
  - domain-professional-writing/domain-specific/domain_writing_hvac_estimate.md
  - client-services-studio/prompts/stage-3-scope-and-estimate.md
  - domain-specialized-fields/trades/trades_change_order_pricing_notice.md
---

# Bid Estimate with Contingency

**Objective:** Produce a bid price a contractor can defend line by line — where
every quantity has a source, every owner choice is an allowance, and the
contingency is the sum of named risks rather than a percentage nobody can explain.

**When to Use:**
- You have walked the job (or have plans) and need a number, not a document yet.
- Your last few jobs ran over and the overrun always came from "something we found."
- A client asks why your price is higher than another bid, and you want to show
  what yours includes that theirs may not.
- **Not this prompt if** the number is done and you need the customer-facing
  estimate — `domain-professional-writing/domain-specific/domain_writing_hvac_estimate.md`
  (and its trade siblings) write that from this output. Selling expertise by the
  engagement (deliverables, acceptance criteria) is
  `client-services-studio/prompts/stage-3-scope-and-estimate.md`. Contract and
  scope-of-work drafting belong to the contract you use and, where needed, an
  attorney (`domain-legal/contracts-transactional/legal_sow_drafter.md`). Pricing a
  change once work is under way is `trades_change_order_pricing_notice.md`.

## Inputs / Context

1. **Scope as understood:** what the client asked for, site-visit notes, photos or
   plan sheets, measurements.
2. **Your rates:** burdened labor rate per hour (wages + taxes + insurance + benefits),
   equipment rates, overhead % and profit % — yours, not an industry average.
3. **Supplier and sub quotes** with dates and expiry.
4. **Owner selections** made and not made (fixtures, finishes).
5. **What you could not see:** inside walls, under floors, above ceilings, the age
   and materials of the building.
6. **Permit and inspection requirements** as you understand them — verified with
   the local authority, not assumed.

## Method

1. **Break the work down (DT-01).** Trade sequence: demo → rough-ins → structure →
   substrate → finishes → fixtures → cleanup. Each line: quantity, unit, waste
   factor, source (`[measured]`, `[plans sheet]`, `[sub quote]`, `[supplier quote]`,
   `[estimate]`).

2. **Price each line (NE-11).**
   - `Material = quantity × (1 + waste) × unit cost`
   - `Labor = hours × burdened rate`
   - `Line = material + labor + equipment + sub`
   Round quantities to purchasable units (sheets, boxes, sticks).

3. **Separate allowances from everything else (CM-03).** An owner choice not yet
   made is an **allowance**: a stated amount, reconciled at cost plus the agreed
   markup when the choice is made. An allowance is not contingency and not
   profit; say which lines are allowances.

4. **Build the unknowns register (QA-04).** For each thing you could not see or
   confirm: probability, cost impact, and one treatment:
   - **Resolve before bid** — test, open up, or ask (cheapest when possible).
   - **Unit price** — a stated price per unit if found (e.g. per sheet of subfloor).
   - **Time-and-materials alternate** with a not-to-exceed, owner approval first.
   - **Exclude** — stated in writing, priced separately if it arises.
   - **Carry in contingency** — only small unknowns: default rule, impact ≤ 5% of
     direct cost.
   `Contingency = Σ (probability × impact)` over carried items; report the
   worst case of carried items beside it.

5. **Apply overhead and profit** as your contract states (on direct + contingency,
   compounding or combined — say which).

6. **Write exclusions and assumptions.** Everything the price does not include,
   including licensed-trade work outside your license and any code or permit
   requirement you have not confirmed.

7. **Compare to a flat percentage.** Show what a flat 10% would have carried, so
   the difference is visible — and the named version is explainable.

## Output Format

```
# Bid estimate — [job] — [date] — valid until [date]

## Takeoff and pricing
| # | Line | Qty (unit, waste) | Source | Material | Labor (hr × rate) | Sub | Line total |
Direct cost subtotal

## Allowances
| Item | Amount | Basis | Reconciled how |

## Unknowns register
| U# | Unknown | P | Impact | Treatment | Contingency (P × I) |
Contingency carried: $[..]  Worst case of carried items: $[..]  Flat 10% would be: $[..]

## Price build
Direct + contingency → overhead [..]% → profit [..]% → bid

## Unit prices and alternates offered
## Exclusions and assumptions
## Licensed / permit items to verify
```

## Verification

- [ ] Every takeoff line has a source tag; `[estimate]` lines are few and named.
- [ ] Line totals, direct subtotal and bid are recomputed and match.
- [ ] Allowances are listed separately and are not inside contingency.
- [ ] Every unknown has exactly one treatment; carried items meet the ≤5% rule or say why not.
- [ ] Sub and supplier quotes are dated and valid through the planned start.
- [ ] Permit fees and code items are marked `[verify with authority]`.

## False-Positive Prevention

1. **A flat percentage is not a contingency.** It cannot be explained to a client
   or checked after the job; named unknowns can be both.
2. **Contingency is not a place to hide profit.** If it is never spent, the
   estimate was wrong, not lucky — review it.
3. **Big unknowns do not belong in contingency.** A 30% chance of $1,800 carried as
   $540 means you lose $1,260 when it happens; unit-price or exclude it.
4. **An allowance is not a promise of that product.** State the amount, not a
   brand, unless the owner chose it.
5. **Expired quotes are not prices.** A sub quote valid 30 days on a job starting
   in six weeks is an unknown.
6. **"Code requires" is not yours to say** unless you hold the license for that
   trade in that jurisdiction; mark it for the authority or the licensed sub.
7. **Burdened rate, not wage.** Pricing labor at what you pay per hour omits taxes,
   insurance and non-billable time.

## Example Output

```
# Bid estimate — hall bath gut remodel, 5'×8', 1962 house — 2026-09-24 —
# valid until 2026-10-24

## Takeoff and pricing (burdened labor $68/hr [user])
| 1 | Demo & disposal | 1 lot | [measured] | dumpster $475 | 14 × 68 = $952 | — | $1,427 |
| 2 | Asbestos test, floor tile & mastic | 2 samples | [lab quote] | — | — | $350 | $350 |
| 3 | Plumbing rough (valve, drain relocate) | 1 lot | [sub quote 09-20, valid 45 d] | — | — | $2,850 | $2,850 |
| 4 | Electrical (GFCI, fan, 2 lights) | 1 lot | [sub quote 09-21, valid 60 d] | — | — | $1,650 | $1,650 |
| 5 | Framing / blocking | — | [measured] | $180 | 6 × 68 = $408 | — | $588 |
| 6 | Cement board + waterproofing | 100 sf +10% = 110 sf | [measured] | $319 | 10 × 68 = $680 | — | $999 |
| 7 | Drywall | 180 sf +10% → 7 sheets | [measured] | $140 | 12 × 68 = $816 | — | $956 |
| 8 | Tile install (floor 44 + surround 66 sf) | 110 sf | [measured] | $260 setting | 22 × 68 = $1,496 | — | $1,756 |
| 9 | Tile material | 110 sf × $6 | ALLOWANCE | $660 | — | — | $660 |
| 10 | Fixtures (vanity, toilet, tub, trim) | 4 | ALLOWANCE | $2,300 | — | — | $2,300 |
| 11 | Fixture install | — | [estimate] | — | 10 × 68 = $680 | — | $680 |
| 12 | Paint | — | [measured] | $95 | 6 × 68 = $408 | — | $503 |
| 13 | Permit | 1 | [verify with authority] | — | — | $325 | $325 |
Direct cost subtotal: $15,044 (labor 80 hr = $5,440)

## Allowances
| Tile | $660 | 110 sf × $6/sf | At cost + 20% markup per contract |
| Fixtures | $2,300 | vanity $900, toilet $350, tub $650, trim $400 | Same |

## Unknowns register
| U1 | Subfloor rot at toilet flange / tub | 50% | $1,080 (3 sheets) | Unit price $360/sheet installed | — |
| U2 | Galvanized supply beyond bath wall | 30% | $1,800 | T&M alternate, NTE $1,800, owner approval first | — |
| U3 | Walls out of plumb > 1/4" | 40% | $400 | Carry | $160 |
| U4 | Asbestos in floor tile/mastic | ? | — | Resolve: test (line 2); abatement excluded | — |
| U5 | Out-of-square room, tile layout | 50% | $272 | Carry | $136 |
| U6 | Hallway wall patch after plumbing access | 60% | $350 | Carry | $210 |
| U7 | Labor productivity ±10% on 80 hr | 50% | $544 | Carry | $272 |
Contingency carried: $778 (5.2% of direct)  Worst case of carried items: $1,566
Flat 10% would be: $1,504 — and would still lose money if U1 or U2 hit.

## Price build
Direct $15,044 + contingency $778 = $15,822
Overhead 10% → $17,404.20 · profit 10% → $19,144.62 · Bid: $19,145

## Unit prices and alternates offered
Subfloor replacement $360 per 4×8 sheet installed ($300 direct + 20%).
Supply-line replacement beyond bath wall: T&M at $68/hr + materials + 20%, NTE $1,800.

## Exclusions and assumptions
Asbestos abatement (if test positive, licensed abatement contractor, priced
separately); mold remediation; work outside the bathroom except U6 patch; owner
selections by 10-15 to hold the start date.

## Licensed / permit items to verify
Permit fee and inspections with the building department; GFCI and fan
requirements confirmed by the licensed electrician on line 4.
```

## Techniques Used

- **DT-01 Hierarchical Task Breakdown** — the takeoff in trade sequence, one priced line each.
- **NE-11 Embedded Calculation Formulas** — material, labor, contingency and markup math shown.
- **QA-04 Uncertainty Acknowledgment** — each unknown carries probability, impact and a treatment.
- **CM-03 Scope Definition** — allowances, exclusions and alternates bound what the price covers.

## Related Prompts

- `domain-professional-writing/domain-specific/domain_writing_hvac_estimate.md` —
  the customer-facing estimate written from this number (trade siblings alongside it).
- `client-services-studio/prompts/stage-3-scope-and-estimate.md` — scope-before-price
  for engagement-based services work.
- `domain-specialized-fields/trades/trades_change_order_pricing_notice.md` — what
  happens when U1, an owner request, or an unlisted condition shows up mid-job.
