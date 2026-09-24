---
title: "Third-Party Risk Assessment — The Whole Vendor, Not Just Its Security Answers"
category: risk/third-party
description: "Assess an existing or prospective vendor, outsourcer or critical supplier across every way it can hurt you — financial viability, operational resilience, concentration, compliance and conduct, fourth-party dependencies, and exit — rate each dimension on evidence, let the worst dimension rather than the average set the overall rating, and end with conditions, a monitoring cadence and a named owner; distinct from `domain-risk/risk_vendor_security_questionnaire_review.md` (security answers only) and `domain-operations/supply-chain-procurement/ops_supplier_selection_scorecard.md` (choosing between suppliers)."
techniques:
  - ST-43
  - RT-02
  - RT-07
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - third-party-risk
  - vendor-risk
  - concentration-risk
  - fourth-party
  - outsourcing
  - due-diligence
  - depend-on-supplier
  - supplier-goes-under
  - exit-plan
updated: "2026-09-24"
reasoning:
  styles: [systems, evidential, structural, adversarial]
  stakes: variable
  horizon: weeks_to_months
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: cross_domain
  collaboration: small_team
  output_format: [matrix, structured]
  user_role: [operator, procurement, finance, founder, risk-lead]
  mode: [audit, assess, decide]
related_prompts:
  - domain-risk/risk_vendor_security_questionnaire_review.md
  - domain-risk/risk_dependency_chain_audit.md
  - domain-operations/supply-chain-procurement/ops_supplier_selection_scorecard.md
---

# Third-Party Risk Assessment

**Objective:** Decide how much of your operation you can safely rest on one outside
party. Rate the vendor on each dimension through which it can fail you, on evidence
rather than reputation; trace the failure through to your own customers; name what
would have to be true to keep it; and hand the result to one owner with a date to look again.

**When to Use:**
- A vendor, outsourcer, logistics provider, contract manufacturer or managed service now
  carries a function you could not run for a week without it.
- An auditor, lender, insurer or large customer asks for your third-party risk process.
- A vendor has changed ownership, missed payments to its own suppliers, lost a big client,
  or started routing your work to someone you have never met.
- A renewal is due and the last assessment was the sales call.

**Not this prompt if:**
- You only need the vendor's **security** answers graded — `risk_vendor_security_questionnaire_review.md`
  (this prompt consumes its result as one dimension).
- You are **choosing between** candidate suppliers on cost and fit — `domain-operations/supply-chain-procurement/ops_supplier_selection_scorecard.md`
  or `domain-business-strategy/research/research_vendor_evaluation.md`.
- The question is financial counterparty exposure (netting, collateral, expected loss) —
  `domain-finance/risk-management/finance_counterparty_risk_assessment.md`.
- The vendor's privacy paper (DPA, transfers) needs review — `domain-legal/privacy-data/legal_vendor_privacy_assessment.md`.

## Inputs / Context

1. **What the vendor does for you**, which of your functions stops without it, and for how long you could cope.
2. **Money:** annual spend, contract term, notice period, termination rights, any prepayment or deposit.
3. **Evidence on the vendor:** filed accounts or credit report, insurance certificates, audit or
   attestation reports, regulatory register entries, adverse media, references, incident history with you.
4. **Their dependencies you know of:** key subcontractors, platforms, sites, the people who actually do your work.
5. **Alternatives:** who else could do it, and how long a switch would take.
6. **Your appetite:** from `risk_appetite_statement.md` if one exists.

## Method

1. **Tier the relationship before gathering evidence (ST-43).** Criticality = what stops
   if the vendor stops × how long a switch takes. Tier 1: a customer-facing or regulated function
   stops within days and a switch takes more than a month. Tier 2: an internal function degrades.
   Tier 3: an inconvenience. Depth of evidence follows the tier.

2. **Rate six dimensions separately (RT-02).** Each gets Low / Medium / High with the evidence
   that set it and an evidence grade (independent document / vendor's own statement / none).

   | Dimension | Ask |
   |---|---|
   | Financial viability | Can they still exist and pay their own suppliers in 12 months? Accounts, credit report, customer concentration on their side |
   | Operational resilience | One site? One key person? Tested continuity plan? Record of outages or missed service levels with you |
   | Concentration (yours) | Share of the function they carry; whether you have a second source; share of their revenue you are |
   | Compliance and conduct | Licences, regulatory actions, sanctions and adverse media, labour and environmental practice that would land on your name |
   | Security and data | Take the grade from `risk_vendor_security_questionnaire_review.md`; do not redo it |
   | Fourth parties and exit | Who they depend on; what you can take back at exit, in what format, how fast |

3. **Trace the cascade (RT-07).** For each High dimension, write the chain in three hops:
   vendor event → your function → your customer or regulator. A High that stops at "we
   would be annoyed" is a Medium.

4. **Find the fourth parties that matter.** Ask the vendor who they cannot operate without.
   Flag any fourth party shared by two or more of your vendors — that is concentration
   you cannot see from any single assessment.

5. **Set the overall rating by the worst dimension, then rank the gaps (DS-06).** One High
   on a Tier-1 vendor makes the relationship High regardless of five Lows. Rank gaps by
   cascade severity × how quickly the dimension can deteriorate.

6. **Decide, with conditions.** Keep / keep-with-conditions (contract clause, second
   source, escrow, deposit reduction, monitoring feed) / reduce reliance (plan and date) /
   exit. Name the residual-risk owner and the re-assessment date. Tier 1 is re-assessed at
   least annually and on any trigger event listed in the output.

## Output Format

```
# Third-party risk assessment — [vendor], [service], [date]
Assessor: [role] · Tier: [1/2/3] because [function stopped] × [switch time]

## Dimension ratings
| Dimension | Rating L/M/H | Evidence | Evidence grade | Trend |

## Cascades (High dimensions only)
[vendor event] → [our function] → [customer / regulator impact, quantified]

## Fourth parties that matter
| Fourth party | What it provides | Shared with our other vendors? |

## Overall: [L/M/H] — set by [dimension]
## Ranked gaps and conditions
| Gap | Cascade severity | Speed of change | Condition / action | Owner | Due |

## Decision: keep / keep-with-conditions / reduce reliance / exit
Residual risk accepted by: [role], [date] · Re-assess: [date]
Trigger events that force early re-assessment: [...]
Confidence: High / Medium / Low — [what evidence is missing]
```

## Verification

- [ ] Tier set from function-stopped × switch-time before evidence was gathered.
- [ ] All six dimensions rated, each with evidence and an evidence grade.
- [ ] Security dimension taken from the questionnaire review, not re-derived.
- [ ] Every High has a three-hop cascade ending at a customer, regulator or cash impact.
- [ ] Overall rating equals the worst dimension on a Tier-1 vendor, not an average.
- [ ] Fourth parties named, with any shared across vendors flagged.
- [ ] Exit route stated with time and data format.
- [ ] Named owner, re-assessment date and trigger events recorded.

## False-Positive Prevention

1. **Averaging the dimensions.** A vendor strong on five dimensions and about to run out of
   cash is a High. Score by the worst dimension.
2. **Size as solvency.** A well-known name is not a financial rating. Read the accounts or
   the credit report; mark "no evidence" when you have neither.
3. **Certificate as resilience.** A security attestation says nothing about whether their
   only warehouse floods. Security is one dimension of six.
4. **Invisible concentration.** Three vendors on the same cloud region or the same payroll
   processor are one dependency. Check fourth parties across the portfolio, not per vendor.
5. **Uniform depth.** Full due diligence on a Tier-3 stationery supplier is how Tier 1 goes
   unreviewed. Depth follows the tier.
6. **Exit assumed.** "We can always switch" is a claim; state the weeks, the cost and whether
   your data comes back usable.
7. **Their risk as your finding.** Adverse media is a lead to verify, not a conclusion.
   Record the source and whether it was corroborated.

## Example Output

```
# Third-party risk assessment — FreightLink, outbound 3PL, 2026-09-18
Assessor: Head of Operations · Tier 1: carries 62% of outbound orders; switch estimated at 14 weeks

## Dimension ratings
| Financial viability | High | Filed accounts: current ratio 0.9; largest client = 31% of their revenue | Independent | Worsening |
| Operational resilience | Medium | Single warehouse; continuity plan exists, never tested | Vendor statement | Flat |
| Concentration (ours) | High | 62% of our volume; no second source; we are 6.7% of their revenue ($1.2M of $18M) | Independent | Flat |
| Compliance and conduct | Low | Operator licence current; no adverse media found | Independent | Flat |
| Security and data | Medium | Questionnaire review 2026-08: approve-with-conditions | Independent | Improving |
| Fourth parties and exit | Medium | One warehouse-management system; order data exportable as CSV | Vendor statement | Flat |

## Cascade (Financial viability)
FreightLink loses its 31% client and fails → 62% of our orders unshipped → at $400k weekly shipped
revenue, 2 weeks of disruption = $496k delayed (0.62 × $400k × 2)

## Fourth parties that matter
| Warehouse-management SaaS | Order routing | Yes — also used by our returns vendor |

## Overall: High — set by financial viability and concentration
## Ranked gaps and conditions
1. No second source — onboard backup 3PL for 20% of volume — Head of Ops — 2026-12-31
2. Financial deterioration — quarterly credit report + covenant to notify change of control — Finance Lead — 2026-10-15
3. Untested continuity plan — join their next test as observer — Ops Manager — 2027-01-31

## Decision: keep-with-conditions
Residual risk accepted by: COO, 2026-09-24 · Re-assess: 2027-03 (6 months, Tier 1 at High)
Trigger events: loss of their largest client, late payment to us of credits, change of ownership
Confidence: Medium — accounts are 9 months old
```

## Techniques Used

- **ST-43 Risk-Stratified Documentation** — tier sets depth of evidence.
- **RT-02 Multi-Dimensional Analysis Framework** — six dimensions rated separately.
- **RT-07 Cascade Effect Analysis** — every High traced to a customer or cash impact.
- **DS-06 Prioritization and Severity Guidance** — worst-dimension rating and gap ranking.
- **QA-12 False Positives Identification** — reputation, certificates and averages are not assurance.

## Related Prompts

- `domain-risk/risk_vendor_security_questionnaire_review.md` — the security dimension.
- `domain-risk/risk_dependency_chain_audit.md` — replaceability and single points of failure across all dependencies.
- `domain-risk/risk_acceptance_exception_memo.md` — when a High is kept, record it formally.
- `domain-risk/risk_key_risk_indicators.md` — turn the trigger events into monitored indicators.
- `domain-operations/supply-chain-procurement/ops_supplier_selection_scorecard.md` — choosing the second source.
