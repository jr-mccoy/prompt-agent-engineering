---
title: "Insurance Agent Policy Comparison Letter — Form-Level Coverage, Claim Scenarios, Client Priorities"
category: professional-writing/domain-specific
description: "Draft an insurance agent's or broker's client-facing comparison of quoted policies: coverage read from the policy forms and endorsements rather than the declarations page or carrier summary, quotes normalised to the same limits, deductible structure, sublimits and valuation basis (ACV vs replacement cost) shown through what the client pays in realistic claims, gaps no quote covers, and a recommendation tied to the client's stated priorities. Presents quotes already received — distinct from building the submission (insurance_commercial_submission_builder) or deciding whether to remarket (insurance_renewal_remarketing_plan)."
techniques:
  - RT-05
  - RT-02
  - NE-11
  - NE-16
  - QA-20
difficulty: intermediate
tags:
  - insurance-agent
  - policy-comparison
  - compare-insurance-quotes
  - homeowners-insurance
  - deductible-vs-premium
  - acv-vs-replacement-cost
  - client-quote-presentation
updated: "2026-10-06"
related_prompts:
  - domain-specialized-fields/insurance/insurance_renewal_remarketing_plan.md
  - domain-specialized-fields/insurance/insurance_commercial_submission_builder.md
  - domain-finance/risk-management/finance_business_insurance_coverage_review.md
  - domain-finance/personal-finance-planning/finance_insurance_needs_analysis.md
---

# Insurance Agent Policy Comparison Letter

**Objective:** Present two or more quoted policies to a client so they can see, in dollars and plain words, what each would pay in the claims they are most likely to have — and choose with the agent's recommendation tied to what they said matters.

**When to Use:**
- Quotes are back (new business, renewal remarket, or a client-requested shop) and the client must choose.
- The cheapest quote differs from the others in deductible structure, roof or contents valuation, or sublimits the client will not spot.
- Personal or small commercial lines where the client reads the comparison themselves rather than through a risk manager.
- **Not this prompt if** you are assembling the underwriting submission — `domain-specialized-fields/insurance/insurance_commercial_submission_builder.md` — or deciding whether to renew or go to market — `domain-specialized-fields/insurance/insurance_renewal_remarketing_plan.md`, which hands off to this prompt once quotes arrive. A business owner mapping their own exposures to coverage is `domain-finance/risk-management/finance_business_insurance_coverage_review.md`; sizing life or disability cover is `domain-finance/personal-finance-planning/finance_insurance_needs_analysis.md`.

**Audience:** A policyholder (household or small business owner) choosing between quotes, who will look at the premium first and needs to see what it buys. The licensed agent signs the comparison; the issued policy wording governs, not the comparison.

## Inputs / Context

Paste source material inside the named tags and refer to it by tag name.

1. **Client situation** — property or operation, values, construction and age (roof age for property), exposures, prior claims — in `<client_situation>`.
2. **Client priorities**, in their words and ranked — budget ceiling, out-of-pocket tolerance after a claim, specific worries — in `<client_priorities>`.
3. **Quotes** — for each: carrier, premium, limits, every deductible (all-peril, wind/hail, named-storm, percentage or flat), valuation basis by coverage, sublimits, endorsements included and available — in `<quotes>`.
4. **Policy forms and endorsements** for each quote, or the relevant excerpts — in `<policy_forms>`. Declarations pages and carrier marketing summaries are not substitutes.
5. **Market and service notes** — markets approached and declined, the agent's own claims-service experience, carrier financial-strength ratings as checked — in `<agency_notes>`.

## Method

1. **Read coverage from the form (RT-05).** For each quote, confirm from `<policy_forms>`: valuation basis (replacement cost, ACV, payment schedule) for dwelling, roof, and contents; exclusions relevant to the client's exposures; sublimits; how each deductible applies. Where only a declarations page or summary is available, mark the line `[VERIFY: policy form]`.
2. **Normalise before comparing.** If quotes differ in a primary limit (e.g. dwelling amount), say so, request a requote, and note the premium is not yet comparable.
3. **Choose 3–4 claim scenarios from the client's exposures (RT-02)** — the likely claim (e.g. hail on an older roof), a severe one, and one tied to a stated worry.
4. **Compute out-of-pocket per scenario (NE-11).**
   - `Paid = min(loss at the policy's valuation basis − applicable deductible, sublimit)`; `Client pays = loss − Paid`.
   - Percentage deductibles: `deductible = % × the limit it is based on`, shown as dollars.
   - Premium difference vs. out-of-pocket difference shown side by side.
5. **Name gaps common to all quotes.** Exposures none of the quotes covers adequately, with the separate cover to quote.
6. **Recommend against the ranked priorities (NE-16).** One pick, with the condition that would change it; the other options described fairly, not dismissed.
7. **Verify before drafting.** Every coverage statement traces to `<policy_forms>` or is `[VERIFY]`; every dollar figure recomputes; no carrier rating or claims reputation is supplied from memory; markets approached and declined are disclosed.

## Output Format

```
[Agency letterhead]   Policy comparison — [client]   [date]   Quotes valid until [date]

## Our recommendation
[Pick · why against your priorities · what would change it]

## Side by side
| | Quote A | Quote B | Quote C |
Annual premium | Main limit | All-peril deductible | Wind/hail deductible ($) |
Roof valuation | Contents valuation | Key sublimits | Key exclusions/endorsements

## What you'd pay in a claim
| Scenario | Loss | A pays / you pay | B | C |

## What none of these quotes covers
[Gap — what to quote separately]

## Each option in plain words
[A / B / C — strengths, trade-offs]

## Before you decide
[Requotes pending · items to confirm · decision deadline]

[Agent signature, licence]  The issued policy's wording governs.
[Markets approached and declined; compensation disclosure per agency practice]
```

## Verification

- [ ] Every valuation basis, exclusion, and sublimit is sourced to `<policy_forms>` or marked `[VERIFY]`.
- [ ] Percentage deductibles are converted to dollars at the quoted limit.
- [ ] Each scenario's "you pay" recomputes from loss, deductible, valuation basis, and sublimit.
- [ ] Quotes with different primary limits are flagged and a requote requested.
- [ ] The recommendation names the client priority it serves and the condition that would change it.
- [ ] Carrier ratings and service claims come from `<agency_notes>`, not the model.
- [ ] Markets approached and declined are listed.

## False-Positive Prevention

1. **Coverage copied from the declarations page.** The dec page lists limits; the form and endorsements decide whether a roof is paid at replacement cost or on a depreciation schedule. A comparison built from dec pages can call two very different policies "the same coverage".
2. **Premium as the comparison.** The cheapest quote often carries the percentage wind/hail deductible or the ACV roof endorsement that costs the client far more in the first storm than it saved in premium.
3. **A percentage deductible left as a percentage.** "2% wind/hail" reads small; at a $485,000 dwelling limit it is $9,700. Always show the dollars.
4. **Unequal limits compared as equal.** A quote with a lower dwelling limit looks cheaper and has a smaller percentage deductible for the same reason. Requote before ranking.
5. **Sublimits invisible in the headline.** Business property at home, water backup, jewellery, and similar items carry small sublimits that matter only to the client who has them — which is why the client's exposures choose the scenarios.
6. **Carrier reputation from memory.** Financial-strength ratings and claims service are current facts; take them from the agent's own checks and experience or mark `[VERIFY: current rating, source]`.
7. **"Unbiased" with undisclosed market limits.** If two appointed carriers declined or only some markets were approached, the comparison is of what was available, and the client should know it.

## Dual-Failure Prevention (QA-20)

- **Harmful:** steering the client to the lowest premium — or to the agent's preferred carrier — without showing what it pays in the claim they are most likely to have.
- **Unhelpful:** a grid of every coverage line and form number with no recommendation, leaving the client to decode it and pick on price anyway.
- **Bar:** the client can say which quote pays most in their most likely claim, what each costs per year, what none of them covers, and why the agent picked the one they did.

## Example Output

```
Greenway Insurance Agency   Policy comparison — Priya & Tom Nakamura   6 Oct 2026
Quotes valid until 31 Oct 2026

## Our recommendation
Cedar Point (Quote B). Your first priority was keeping a storm claim under
$5,000 out of pocket within a $2,700 budget; B does that at $2,640. One
condition: Summit (C) is requoting at the same $485,000 dwelling limit. If that
comes back at or under $2,640, we would switch our pick to C for its stronger
basement water cover — your third priority.

## Side by side
|                        | A Northfield | B Cedar Point | C Summit (as quoted) |
| Annual premium         | $2,180       | $2,640        | $2,390 |
| Dwelling limit         | $485,000     | $485,000      | $460,000 — requote requested |
| All-peril deductible   | $1,000       | $1,000        | $2,500 |
| Wind/hail deductible   | 2% = $9,700  | $2,500 flat   | 1% = $4,600 |
| Roof valuation         | Payment schedule: 45% of cost at 12 yrs | Replacement cost | Replacement cost |
| Water/sewer backup     | Excluded (add $10,000 for $95/yr) | $5,000 | $10,000 |
| Business property home | $2,500       | $2,500        | $5,000 |

## What you'd pay in a claim
| Scenario                         | Loss    | A you pay | B you pay | C you pay |
| Hail replaces 12-yr-old roof     | $28,000 | $25,100   | $2,500    | $4,600 |
| Sewer backup, finished basement  | $12,000 | $12,000   | $7,000    | $2,500 |
| Kitchen fire                     | $40,000 | $1,000    | $1,000    | $2,500 |
Roof under A: 45% × $28,000 = $12,600, less $9,700 deductible = $2,900 paid;
you pay $25,100. A saves $460/yr against B; one roof claim costs $22,600 more.
Backup under B: $12,000 − $1,000 = $11,000, capped at $5,000 → you pay $7,000.
Under C at $485,000 the hail deductible would be $4,850 — still under $5,000.

## What none of these quotes covers
Tom's workshop tools (~$40,000, used for his cabinetry business): at most
$2,500–$5,000 under any quote. We'll quote a separate business/tools policy.

## Each option in plain words
A: lowest premium; you carry most of a storm loss on an older roof.
B: meets your storm limit and budget; basement water cover is modest.
C: best basement cover, higher deductible for everyday claims; not yet
comparable on price until the requote arrives.

## Before you decide
- Summit requote at $485,000 — expected by 14 Oct.
- Tools policy quote — by 17 Oct.
- Decide by 24 Oct; current policy renews 1 Nov.

Sam Greenway, licensed agent   The issued policy's wording governs.
Markets approached: five; Ridge Mutual and Harbor Home declined (roof age).
Financial-strength ratings checked 3 Oct [VERIFY on renewal date].
```

## Techniques Used

- **RT-05 Evidence-Based Reasoning** — every coverage statement sourced to the policy form, not the dec page or summary.
- **RT-02 Multi-Dimensional Analysis Framework** — premium, deductible structure, valuation basis, and sublimits compared as separate dimensions.
- **NE-11 Embedded Calculation Formulas** — out-of-pocket per claim scenario, with percentage deductibles in dollars.
- **NE-16 Non-Judgmental Comparison** — each option described fairly before and after the pick.
- **QA-20 Dual-Failure Quality Test** — neither premium-steering nor an undecoded grid.

## Related Prompts

- `domain-specialized-fields/insurance/insurance_renewal_remarketing_plan.md` — the remarket decision that produces the quotes compared here.
- `domain-specialized-fields/insurance/insurance_commercial_submission_builder.md` — the submission behind commercial quotes.
- `domain-finance/risk-management/finance_business_insurance_coverage_review.md` — the business owner's exposure-first view of the same cover.
- `domain-finance/personal-finance-planning/finance_insurance_needs_analysis.md` — life, disability, and long-term-care needs, not property quotes.
