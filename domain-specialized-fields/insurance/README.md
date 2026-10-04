# Insurance — Broking, Underwriting, and Claims Work

Four prompts for **insurance industry professionals** — brokers, underwriters and
claims adjusters — covering the core commercial work of the trade: building a
submission, assessing it, reviewing a claim file against the policy, and planning a
renewal. Each one turns the documents the user supplies (applications, loss runs,
COPE schedules, the issued policy wording, market indications) into a structured
work product with the arithmetic and the quoted wording shown.

These are written for the **industry side**. A policyholder disputing a denial,
negotiating a claim, or checking their own cover is routed out (see boundaries).

## Contents

| File | Use |
|---|---|
| [`insurance_commercial_submission_builder.md`](insurance_commercial_submission_builder.md) | Broker: source-tagged exposures, developed loss runs with large losses explained, COPE and TIV with valuation basis, missing-items list, underwriter-ready narrative |
| [`insurance_underwriting_risk_assessment.md`](insurance_underwriting_risk_assessment.md) | Underwriter: appetite and authority gate, anchored risk-quality scores, burning cost and indicated loss ratio, stress tests, terms tied to findings, referral triggers |
| [`insurance_claim_file_coverage_review.md`](insurance_claim_file_coverage_review.md) | Adjuster: insuring agreement, definitions, exclusions with exceptions, conditions and endorsements quoted; facts established vs needed; reservation-of-rights considerations for the authority holder |
| [`insurance_renewal_remarketing_plan.md`](insurance_renewal_remarketing_plan.md) | Broker: probability-weighted renewal outlook, renew / selective / full-market decision with its cost, market approach, backward timeline with client decisions |

Order of use: renewal plan (−150 days) → submission → underwriting assessment →
(after a loss) claim file review. The examples share one account — Harbor
Fabrication — so exposures, losses and premiums carry through the broker and
underwriter prompts.

## Guards (every prompt)

- **No fabricated market or policy data.** Rates, appetites, loss figures and
  values come from the user and are source-tagged; policy wording is quoted from
  the issued policy with form and page. A gap is `[NOT PROVIDED]` or `[NOT IN FILE]`.
- **Coverage determinations rest with licensed professionals.** The claim review
  organises the file and frames questions; the licensed adjuster, the claims
  authority holder and coverage counsel decide coverage and any reservation of rights.
- **Authority stays with the authority holder.** Underwriting referrals and binding
  decisions follow the carrier's guidelines and authority letter, which the user supplies.
- **Jurisdiction matters.** Claim-handling deadlines, unfair-claims-practices
  standards, notice periods and licensing rules vary by state and country and are
  confirmed locally, never assumed.

## Boundaries — not here

| If you need… | Go to |
|---|---|
| A business owner's review of its own cover against its exposures | [`finance_business_insurance_coverage_review.md`](../../domain-finance/risk-management/finance_business_insurance_coverage_review.md) |
| Personal insurance needs (life, income, household) | [`finance_insurance_needs_analysis.md`](../../domain-finance/personal-finance-planning/finance_insurance_needs_analysis.md) |
| A policyholder's appeal of a denied claim | [`advocacy_insurance_claim_denial_appeal.md`](../../domain-written-advocacy/insurance-and-medical/advocacy_insurance_claim_denial_appeal.md) |
| A claimant negotiating the settlement amount with an adjuster | [`negotiation_insurance_claim_settlement.md`](../../domain-negotiation/contexts/negotiation_insurance_claim_settlement.md) |
| A client-facing comparison of quoted policies | [`domain_writing_insurance_comparison.md`](../../domain-professional-writing/domain-specific/domain_writing_insurance_comparison.md) |
| Enterprise risk registers and risk appetite | [`domain-risk/`](../../domain-risk/README.md) |
| Litigated coverage disputes, policy drafting, bad-faith questions | An attorney; legal research via [`domain-legal/`](../../domain-legal/) |
