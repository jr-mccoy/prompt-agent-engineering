---
title: "Will Drafter — Specific Bequests, Residuary, Pour-Over, Fiduciary Appointments and Tax Provisions"
category: legal/trusts-estates
description: "Draft a last will and testament for an estate-planning attorney from a completed intake: identification and family recitals, revocation, specific and general bequests with lapse and ademption handling, tangible personal property with a memorandum where state law allows, residuary disposition (outright, to testamentary trusts, or pouring over to a revocable trust), guardian nominations for minors, executor/personal representative appointments and powers, tax-apportionment and debts clauses, and execution formalities — every state-specific rule marked for verification. Attorney work product; distinct from the client's own pre-meeting wishes workbook and from a financial beneficiary review."
techniques:
  - ST-03
  - CM-02
  - OC-04
  - QA-01
difficulty: advanced
tags:
  - legal
  - trusts-estates
  - estate-planning
  - will
  - pour-over-will
  - executor
  - guardianship
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
  output_format: [document, checklist]
  user_role: [attorney, paralegal]
  mode: [draft, audit]
related_prompts:
  - domain-personal-development/major-decisions/personal_estate_wishes_attorney_prep.md
  - domain-finance/personal-finance-planning/finance_estate_beneficiary_review.md
  - domain-legal/trusts-estates/legal_revocable_trust_drafter.md
  - domain-legal/client-intake-communications/legal_engagement_letter_drafter.md
---

## Objective

Produce a complete draft will that implements the client's recorded decisions,
selects the correct structure (stand-alone, testamentary trust, or pour-over), handles
every contingency the plan depends on (lapse, simultaneous death, minors, ademption),
and ships with a drafter's notes table, an open-decisions list for the client meeting,
and an execution checklist whose state formalities are all marked `[VERIFY]`.

## When to Use

- Intake is complete and the attorney needs a first draft for review.
- A revocable-trust plan needs its companion pour-over will.
- An existing will must be restated after a marriage, divorce, birth, death, move to
  another state, or change in fiduciaries.

**Distinct from:**
- `domain-personal-development/major-decisions/personal_estate_wishes_attorney_prep.md`
  — the *client's* workbook for deciding who and what *before* the meeting; it never
  drafts. Its output is ideal input here.
- `domain-finance/personal-finance-planning/finance_estate_beneficiary_review.md` —
  inventories beneficiary designations and titling; it routes drafting to an attorney.
  Use it to confirm which assets actually pass under the will.
- `domain-legal/trusts-estates/legal_revocable_trust_drafter.md` — the trust the
  pour-over will funds.

## Your Input

- **Jurisdiction (required):** client's state of domicile; any other state where
  real property is held (ancillary administration risk).
- **Client and family:** names, marital status, children (including from prior
  relationships, adopted, and any the client wishes to exclude), grandchildren.
- **Plan structure:** stand-alone will / will with testamentary trusts / pour-over to
  a revocable trust (name and date of trust).
- **Dispositions:** specific gifts, tangible personal property, charitable gifts,
  residuary beneficiaries and shares, contingent beneficiaries.
- **Fiduciaries:** executor/personal representative and successors; guardian(s) of
  minor children and successors; testamentary trustees.
- **Tax posture:** size of estate, whether a marital or charitable deduction plan is
  intended, tax-apportionment preference.
- **Non-probate assets** summary (beneficiary designations, joint accounts) so the
  will does not purport to dispose of them.

## Constraints

**Must:**
- Choose and state the structure, and draft only the provisions it requires.
- For every gift: name the beneficiary precisely, state what happens on lapse (to
  descendants per stirpes / to residue / other) and, for specific gifts, what happens
  if the asset is gone.
- Include a residuary clause that disposes of 100% under every contingency, ending in
  a named "ultimate contingent" taker.
- Include a survivorship period and a simultaneous-death rule; flag interaction with
  any marital-deduction plan.
- Hold minor or disabled beneficiaries' shares in trust or a custodial arrangement;
  never outright to a minor.
- Include tax-apportionment and debts/expenses clauses consistent with the tax posture.
- Produce an execution checklist and mark every formality `[VERIFY]`.

**Must Not:**
- Invent statutes, witness counts, self-proving-affidavit forms, spousal elective-share
  rules, pretermitted-heir rules, or case law. Use `[VERIFY: …]` / `[CITE: …]`.
- Assert a tangible-personal-property memorandum is binding; mark `[VERIFY: whether
  state recognises a separate writing]`.
- Dispose of assets that pass by beneficiary designation or survivorship as if they
  were probate assets.
- Disinherit a spouse or child by silence; if intended, say so expressly and flag the
  elective-share / pretermitted-heir question `[VERIFY]`.
- State estate-tax exemption amounts as fact.

## Method

1. **Structure decision.** From intake, choose stand-alone / testamentary trust /
   pour-over and record why.
2. **Family recital.** Identify spouse and all children by name; define "descendants"
   and treatment of adopted and after-born children.
3. **Specific and general gifts.** Draft each with lapse and ademption language.
4. **Tangible personal property.** Gift clause plus memorandum reference `[VERIFY]`.
5. **Residuary.** Primary takers, shares, contingent takers, ultimate contingent taker;
   or pour-over to the named trust with a fallback incorporating the trust terms if the
   pour-over fails `[VERIFY: validity of pour-over to a trust amended after execution]`.
6. **Trusts for minors / contingent trusts.** Age of distribution, trustee, standards.
7. **Fiduciaries.** Executor and successors, bond waiver `[VERIFY]`, independent or
   unsupervised administration election where available `[VERIFY]`, powers.
8. **Guardian nominations.** Guardian of the person and of the estate, successors.
9. **Tax and debts.** Apportionment (residue bears vs. statutory proration), payment of
   debts, secured-debt treatment of encumbered specific gifts.
10. **Boilerplate.** Survivorship, definitions, no-contest clause only if requested and
    `[VERIFY: enforceability]`, governing law.
11. **Drafter's notes, open decisions, execution checklist.**

## Output Format

```markdown
# Last Will and Testament of [Name] — Draft [n], [date]
**Domicile:** [state] · **Structure:** [stand-alone / testamentary trust / pour-over to [Trust name, date]]

ARTICLE 1 — Declarations; Family
ARTICLE 2 — Revocation of Prior Wills
ARTICLE 3 — Specific Gifts (lapse and ademption)
ARTICLE 4 — Tangible Personal Property
ARTICLE 5 — Residuary Estate
ARTICLE 6 — Trusts for Beneficiaries Under [age] (if applicable)
ARTICLE 7 — Fiduciaries
ARTICLE 8 — Guardians of Minor Children
ARTICLE 9 — Taxes, Debts and Expenses
ARTICLE 10 — General Provisions (survivorship, definitions, governing law)
Attestation and [self-proving affidavit — VERIFY form]

## Drafter's notes
| Art. | Choice | Alternative | Reason |

## Open decisions for client meeting
1. …

## Execution checklist
- [ ] [VERIFY: number and qualification of witnesses]
- [ ] [VERIFY: notary / self-proving affidavit requirements]
- [ ] [VERIFY: interested-witness rule]
- [ ] Beneficiary designations and titling align with plan (cross-check finance review)
- [ ] Original storage and client copy instructions
```

## Worked Example

**Input (abridged):** Married client, two children (one aged 14), revocable trust
dated same day; wants her engagement ring to her daughter, everything else to the
trust; husband is executor, sister is successor and guardian.

**Selected drafting:**

> **3.1 Ring.** I give my diamond engagement ring to my daughter, [Name], if she
> survives me. If she does not survive me, this gift shall pass to her descendants who
> survive me, per stirpes, or if none, shall lapse and pass under Article 5. If I do not
> own the ring at my death, this gift shall lapse; no other property is substituted.

> **5.1 Pour-over.** I give my residuary estate to the trustee then acting under the
> [Name] Revocable Trust dated [date], as amended before my death, to be administered
> as part of that trust. If for any reason that gift is ineffective, I give my residuary
> estate to [Name of trustee], as trustee, to hold under the terms of that trust as in
> effect at my death, which terms are incorporated by reference.
> `[VERIFY: state pour-over and incorporation-by-reference rules]`

| Art. | Choice | Alternative | Reason |
|---|---|---|---|
| 5 | Pour-over with incorporation fallback | Testamentary trust in the will | Plan uses a revocable trust; fallback protects against a failed pour-over |
| 6 | Omitted | Minor's trust in the will | Minor's shares are held under the revocable trust; avoid two inconsistent regimes |
| 8 | Sister as guardian of person and estate | Separate guardian of estate | Estate passes to trust, so guardian-of-estate role is minimal; confirm with client |

**Open decision:** Does the client want the sister as guardian if the husband
survives but is incapacitated? Current draft only covers the husband not surviving.

## Verification

- [ ] Structure chosen and stated; unused articles omitted.
- [ ] Every gift has lapse handling; every specific gift has ademption handling.
- [ ] Residuary disposes of 100% under all contingencies, ending in an ultimate taker.
- [ ] No minor receives property outright.
- [ ] Spouse and every child are named; any omission is express and flagged.
- [ ] Non-probate assets are not purported to be disposed of.
- [ ] Every execution formality and state rule is `[VERIFY]`; no statute, case or
      exemption amount is asserted.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Residuary that fails if a named beneficiary predeceases | Draft a contingent chain to an ultimate taker; test each "if X dies first" path |
| Specific gift silent on ademption or lapse | Every specific gift gets both sentences |
| Outright gift to a minor | Route to a trust or custodial arrangement |
| Will "leaves" a 401(k) or joint account | Those pass outside probate; cross-check the beneficiary review and fix designations instead |
| Disinheriting a child by omission | Name and expressly exclude, and flag pretermitted-heir and elective-share checks `[VERIFY]` |
| Stating witness count or self-proving form from memory | Mark `[VERIFY]`; execution defects void wills |
| Tax clause that conflicts with the marital-deduction plan | Check apportionment and survivorship against the tax memo before finalising |
| Pour-over to a trust that does not yet exist | Confirm the trust is signed first or at the same signing; mark sequencing in the checklist |

## Related

- `domain-legal/trusts-estates/legal_revocable_trust_drafter.md` — the receptacle trust for a pour-over will
- `domain-legal/trusts-estates/legal_estate_tax_planning_memo.md` — tax posture that drives Article 9 and survivorship
- `domain-personal-development/major-decisions/personal_estate_wishes_attorney_prep.md` — client's decisions workbook (input)
- `domain-finance/personal-finance-planning/finance_estate_beneficiary_review.md` — non-probate asset and designation check
- `domain-legal/client-intake-communications/legal_engagement_letter_drafter.md` — scoping a joint-spouse representation
