---
title: "Revocable Trust Drafter — Funding Mechanics, Successor Trustee, Distribution Standards and Tax Provisions"
category: legal/trusts-estates
description: "Draft a revocable living trust agreement and its funding plan for an estate-planning attorney: settlor and trustee designation, revocation and amendment powers, administration during the settlor's lifetime and incapacity (with a defined incapacity trigger), successor trustee chain, administration at death (debts, taxes, pour-over coordination), dispositive provisions and distribution standards (HEMS, age-based, discretionary, spendthrift), marital and credit-shelter or disclaimer structure where the tax memo calls for it, trustee powers, and an asset-by-asset funding schedule. Attorney work product; distinct from the client's pre-meeting workbook and from a financial beneficiary review."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - trusts-estates
  - revocable-trust
  - living-trust
  - trust-funding
  - successor-trustee
  - distribution-standards
  - drafting
updated: "2026-09-24"
reasoning:
  styles: [constructive, systematic, conditional]
  stakes: high
  horizon: weeks
  uncertainty: risk
  evidence_quality: rich
  domain_complexity: regulated
  collaboration: small_team
  output_format: [document, table]
  user_role: [attorney, paralegal]
  mode: [draft, plan]
related_prompts:
  - domain-legal/trusts-estates/legal_will_drafter.md
  - domain-legal/trusts-estates/legal_estate_tax_planning_memo.md
  - domain-finance/personal-finance-planning/finance_estate_beneficiary_review.md
  - domain-personal-development/major-decisions/personal_estate_wishes_attorney_prep.md
---

## Objective

Produce a draft revocable trust agreement whose lifetime, incapacity and post-death
phases each work without gaps, whose distribution standards are specific enough for a
successor trustee to apply, and which ships with an asset-by-asset **funding schedule**
— because an unfunded trust controls nothing.

## When to Use

- The plan uses a revocable trust as the main dispositive instrument (probate
  avoidance, privacy, multi-state real estate, incapacity management).
- Restating an older trust after a life event or a change in the tax picture.
- Reviewing a trust drafted elsewhere before the client moves states.

**Distinct from:**
- `domain-personal-development/major-decisions/personal_estate_wishes_attorney_prep.md`
  — the client's own decisions workbook before meeting the attorney.
- `domain-finance/personal-finance-planning/finance_estate_beneficiary_review.md` —
  checks existing designations and titling; this prompt's funding schedule *changes*
  them and should be reconciled against that review.
- `domain-legal/trusts-estates/legal_will_drafter.md` — the pour-over will that
  catches assets left out of the funding schedule.
- `domain-legal/trusts-estates/legal_trust_modification_or_decanting_analysis.md` —
  changing an *irrevocable* trust; a revocable trust is amended by its own terms.

## Your Input

- **Jurisdiction (required):** settlor's domicile and trust situs; states where real
  property is held.
- **Settlor(s):** single or joint; if joint, community-property or separate-property
  state `[VERIFY]`, and how contributions are tracked.
- **Initial and successor trustees**, co-trustee preferences, corporate-trustee option.
- **Incapacity definition preference:** physician certification(s), disability panel,
  court determination.
- **Beneficiaries and dispositive plan:** shares, ages, conditions, special-needs
  beneficiaries, charitable gifts.
- **Distribution standards:** HEMS, broad discretion, incentive provisions.
- **Tax posture:** from the estate tax memo (credit-shelter/marital split, disclaimer
  plan, portability reliance, GST allocation).
- **Asset list** with current titling and beneficiary designations.

## Constraints

**Must:**
- Draft three phases distinctly: lifetime (settlor controls), incapacity (successor
  acts for settlor's benefit), and after death (administration and distribution).
- Define incapacity with an objective trigger and a restoration mechanism, and
  include a HIPAA-style authorisation for the determination `[VERIFY: form]`.
- Name a successor trustee chain ending in a mechanism (e.g. majority of adult
  beneficiaries or a named protector appoints) so the trust never lacks a trustee.
- State distribution standards precisely; if an interested trustee holds discretion
  beyond an ascertainable standard, flag the tax consequence `[VERIFY]`.
- Include a spendthrift clause and flag exceptions `[VERIFY: state spendthrift
  exceptions]`.
- Coordinate with the pour-over will and designate who pays debts and taxes.
- Produce a funding schedule: for each asset, the action (retitle, assign, change
  beneficiary to trust, leave outside by design), who does it, and the document needed.

**Must Not:**
- Invent statutes, trust-code sections, tax thresholds, or case law. Use `[CITE: …]`
  and `[VERIFY: …]`.
- Name the trust as beneficiary of a retirement account without flagging the
  income-tax and see-through-trust analysis `[VERIFY]`.
- Retitle assets whose transfer could trigger a due-on-sale clause, loss of homestead
  or insurance issues without flagging them `[VERIFY]`.
- Treat a joint trust in a community-property state and a separate-property state
  the same way.

## Method

1. **Structure.** Single or joint; separate shares or common pot; tax sub-trusts
   needed? Record reasons.
2. **Lifetime article.** Revocation and amendment (method, by whom, during
   incapacity), settlor's rights to income and principal.
3. **Incapacity article.** Trigger, who certifies, successor's authority, standards for
   the settlor's and dependants' support, restoration.
4. **Successor trustee article.** Chain, resignation, removal, appointment mechanism,
   bond waiver, compensation, accounting obligations `[VERIFY: state reporting duties]`.
5. **Administration at death.** Payment of debts, expenses and taxes; coordination with
   the probate estate; tax elections authority.
6. **Tax sub-trusts** as directed by the tax memo (marital / credit-shelter formula or
   disclaimer trust).
7. **Dispositive provisions.** Shares, distribution standards, ages or milestones,
   special-needs supplemental trust language where needed, contingent and ultimate
   takers.
8. **Trustee powers and protective provisions.** Powers, spendthrift, perpetuities
   savings clause `[VERIFY: state rule]`, governing law and situs change.
9. **Funding schedule** and certification of trust `[VERIFY: statutory form if any]`.
10. **Drafter's notes and open decisions.**

## Output Format

```markdown
# [Name] Revocable Trust — Draft [n], [date]
**Settlor(s):** [ ] · **Situs / governing law:** [state] · **Structure:** [single / joint; sub-trusts]

ARTICLE 1 — Establishment; Name; Revocability
ARTICLE 2 — Lifetime Administration
ARTICLE 3 — Incapacity
ARTICLE 4 — Trustees; Succession; Removal
ARTICLE 5 — Administration at Death; Debts and Taxes
ARTICLE 6 — [Marital / Credit-Shelter / Disclaimer] Trusts (if applicable)
ARTICLE 7 — Dispositive Provisions and Distribution Standards
ARTICLE 8 — Trustee Powers
ARTICLE 9 — Protective Provisions (spendthrift, perpetuities savings)
ARTICLE 10 — General Provisions
Signature and acknowledgment [VERIFY]

## Funding schedule
| Asset | Current title / designation | Action | Responsible | Document | Caution |

## Drafter's notes
| Art. | Choice | Alternative | Reason |

## Open decisions
```

## Worked Example

**Input (abridged):** Single settlor, age 71, widower; two adult children, one with a
disability receiving means-tested benefits; home, brokerage account, IRA, rental
condo in a second state.

**Selected drafting:**

> **3.1 Incapacity.** The Settlor is incapacitated when two licensed physicians, at
> least one of whom has treated the Settlor within the preceding twelve months, certify
> in writing that the Settlor is unable to manage his financial affairs prudently.
> Capacity is restored on a like certification by one such physician.

> **7.3 Share for [Child B].** [Child B]'s share shall be held in a separate
> supplemental-needs trust, in the Trustee's sole discretion, to supplement and not
> supplant any public benefits; no distribution shall be made that would reduce or
> eliminate eligibility. `[VERIFY: state and program requirements for third-party
> supplemental-needs trusts]`

**Funding schedule (excerpt):**

| Asset | Current | Action | Caution |
|---|---|---|---|
| Home | Settlor individually | Deed to trustee | `[VERIFY: homestead tax treatment, title insurance continuation, transfer-tax exemption]` |
| Rental condo (second state) | Settlor individually | Deed to trustee (avoids ancillary probate) | `[VERIFY: second state's recording and transfer rules; HOA approval]` |
| Brokerage | Settlor individually | Retitle to trustee | — |
| IRA | Beneficiaries: children 50/50 | **Do not retitle.** Consider designating Child B's share to the supplemental-needs trust | `[VERIFY: see-through-trust and payout rules]` — outright designation would disqualify Child B from benefits |

## Verification

- [ ] Lifetime, incapacity and post-death phases each drafted and internally complete.
- [ ] Incapacity trigger is objective and has a restoration mechanism.
- [ ] Successor trustee chain never runs out.
- [ ] Distribution standards are applyable; interested-trustee tax flag raised if needed.
- [ ] Special-needs and minor beneficiaries protected.
- [ ] Funding schedule covers every listed asset, including those left outside by design.
- [ ] Retirement-account, homestead and due-on-sale issues flagged `[VERIFY]`.
- [ ] No statute, case or tax threshold asserted as fact.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Drafting a perfect trust with no funding plan | Deliver the funding schedule; unfunded assets go through probate via the pour-over will |
| "Incapacity as determined by the trustee" | Use an objective trigger with named certifiers; circular definitions invite litigation |
| Successor chain of two named people only | Add an appointment mechanism so the trust never lacks a trustee |
| Retitling an IRA to the trust | Retirement accounts change beneficiary designation, never title |
| Outright share for a beneficiary on means-tested benefits | Use a supplemental-needs trust and fix the designations that bypass it |
| Vague "best interests" standard for an interested trustee | Use an ascertainable standard or an independent trustee, and flag tax consequences `[VERIFY]` |
| Asserting state trust-code rules from memory | Mark `[VERIFY]`/`[CITE]`; trust codes vary even where modelled on a uniform act |

## Related

- `domain-legal/trusts-estates/legal_will_drafter.md` — the pour-over will
- `domain-legal/trusts-estates/legal_estate_tax_planning_memo.md` — sub-trust and formula decisions
- `domain-legal/trusts-estates/legal_trust_modification_or_decanting_analysis.md` — once the trust becomes irrevocable
- `domain-finance/personal-finance-planning/finance_estate_beneficiary_review.md` — reconciling designations and titling
- `domain-personal-development/major-decisions/personal_estate_wishes_attorney_prep.md` — client's decisions workbook (input)
