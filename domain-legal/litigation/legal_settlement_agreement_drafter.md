---
title: "Civil Litigation Settlement Agreement Drafter"
category: legal/litigation
description: "Draft a comprehensive settlement agreement for a pending or threatened civil dispute — payment mechanics, release scope and carve-outs, dismissal and continuing jurisdiction, confidentiality and non-disparagement within statutory limits, allocation and tax reporting, liens, and enforcement — distinct from a marital settlement agreement and from an employment separation agreement."
techniques:
  - DT-05
  - RT-07
  - QA-02
  - CM-02
difficulty: advanced
tags:
  - legal
  - litigation
  - settlement-agreement
  - release
  - confidentiality
  - we-settled-now-what
  - write-up-the-settlement
updated: "2026-09-24"
related_prompts:
  - domain-legal/litigation/legal_settlement_value_range_analysis.md
  - domain-legal/divorce/legal_marital_settlement_agreement_drafter.md
  - domain-legal/employment-labor/legal_employment_offer_and_separation_package.md
---

# Civil Litigation Settlement Agreement Drafter

**Objective:** Turn an agreed deal (term sheet, email exchange, or mediator's proposal) into a complete settlement agreement that does exactly what the parties agreed — no more, no less — and survives later enforcement: the release covers what it must and carves out what it must, payment and dismissal steps are sequenced, confidentiality and non-disparagement terms are enforceable in the forum, tax allocation is stated with its limits, and liens and approvals are handled before money moves.

> **Scope guard — attorney-facing.** For counsel memorializing a civil settlement for a represented client. It does not advise on whether to accept the deal or give tax advice to either party. A self-represented party should route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md`.

## When to Use

- A commercial, tort, consumer, or employment-related lawsuit (or threatened claim) has settled in principle and needs a long-form agreement.
- The other side circulated a draft and you need a markup with reasons.
- A mediation produced a signed term sheet that must be converted into definitive terms.

**Not this prompt if:**
- The dispute is a divorce — use `domain-legal/divorce/legal_marital_settlement_agreement_drafter.md`.
- The agreement is a routine employee separation without pending claims — use `domain-legal/employment-labor/legal_employment_offer_and_separation_package.md`.
- You are still deciding what number to accept — use `domain-legal/litigation/legal_settlement_value_range_analysis.md`.

## Inputs

- **Jurisdiction (required):** Court and case number (if filed), governing law for the agreement, and the forum's rules on dismissal and retained jurisdiction `[VERIFY]`.
- **Deal terms:** The agreed term sheet or correspondence — amount, timing, non-monetary terms. Paste verbatim.
- **Parties:** Full legal names, affiliates and insurers to be bound or released, whether any party is a minor, estate, class, or government entity (court or agency approval may be required `[VERIFY]`).
- **Claims:** Claims pleaded and threatened; related matters (other suits, agency charges, arbitrations).
- **Payment facts:** Payor(s), insurer contribution, payees, trust-account routing, W-9/tax-form collection.
- **Tax and lien facts:** Nature of the claimed damages (physical injury, emotional distress, wages, punitive, interest, fees); known liens (medical, government-payer, ERISA plan, attorney's liens) `[VERIFY: applicable lien regimes]`.
- **Sensitive terms:** Whether confidentiality, non-disparagement, no-rehire, or cooperation clauses are on the table, and any statute limiting them in this forum or claim type `[VERIFY]`.

## Method

**Ground rules:** Do not invent statute numbers, required release language, or case law; use `[CITE: …]` / `[VERIFY: …]`. Draft only the terms the parties agreed; any term you add for protection goes in a separate "proposed additions" list, not silently into the draft. Draft to the stated governing law.

1. **Term extraction.** List every agreed term from the source with a pinpoint to where it appears. Mark gaps (terms a complete agreement needs but the deal is silent on) as open items.
2. **Parties and released persons.** Define releasors and releasees precisely — affiliates, officers, insurers, successors — and check each against the deal; broad definitions are a common source of later fights.
3. **Release architecture.** Choose general vs. specific, mutual vs. one-way. Address unknown claims and any statutory waiver of unknown claims required by the governing law `[VERIFY: e.g., whether a Cal. Civ. Code § 1542-type waiver is needed]`. List carve-outs: obligations under the agreement; claims that cannot be released by law `[VERIFY]`; vested benefits; claims the deal excludes.
4. **Age and other special-release rules.** If an individual releases age-discrimination or similar claims, flag statutory release requirements (consideration and revocation periods, advisement to consult counsel) `[VERIFY: OWBPA or analog]`.
5. **Payment and sequencing.** Amount, payee(s), method, deadline, conditions (signed agreement, tax forms, lien resolution), and the order of payment vs. dismissal. Address late payment.
6. **Allocation and tax.** Allocate among wage and non-wage components, physical-injury damages, interest, and fees *only as the parties agreed*; state reporting forms each party expects `[VERIFY: IRS reporting rules]`; include a no-tax-advice representation and a tax indemnity if agreed. Note that labels do not bind the taxing authority `[VERIFY]`.
7. **Liens and approvals.** Lien identification, satisfaction, and indemnity; government-payer reporting where applicable `[VERIFY]`; court approval for minors, class, or other protected parties `[VERIFY]`.
8. **Confidentiality and non-disparagement.** Draft only if agreed; include statutory carve-outs (communications with government agencies, testimony under subpoena, disclosures to tax advisors and spouses, any whistleblower or harassment-disclosure protections) `[VERIFY: federal and state limits]`; define "disparage"; state remedies (not automatic forfeiture unless agreed).
9. **Dismissal and enforcement.** Dismissal with or without prejudice, each side bearing its own fees and costs unless agreed; retained jurisdiction to enforce (which may need to be in the dismissal order itself `[VERIFY: forum practice]`); governing law; venue; fee-shifting for enforcement if agreed.
10. **Boilerplate that matters here.** No admission of liability; entire agreement; authority to sign; counterparts and e-signature; construction (jointly drafted); severability tied to release validity.
11. **Adversarial read.** Read the draft as the other side's lawyer three years from now looking for a way out, and as your client's successor looking for a claim that was not released. Record each exposure.

## Output Format

```markdown
# Settlement Agreement Package — {Matter}

## 1. Term Extraction
| # | Agreed term | Source pinpoint | In draft § | Gap / open item |

## 2. SETTLEMENT AGREEMENT AND RELEASE (draft)
Recitals (no admission)
1. Definitions
2. Settlement Payment (amount, payees, timing, conditions)
3. Allocation and Tax Treatment [VERIFY]
4. Liens and Indemnity
5. Release by {Party A}  |  6. Release by {Party B} (if mutual)
7. Unknown Claims / Statutory Waiver [VERIFY]
8. Excluded Claims (carve-outs)
9. {Special-release provisions — if applicable}
10. {Confidentiality — if agreed, with statutory carve-outs}
11. {Non-Disparagement — if agreed}
12. Dismissal and Retained Jurisdiction
13. No Admission
14. Representations and Warranties
15. Enforcement; Governing Law; Venue
16. General Provisions
Signature blocks; Exhibit A — Stipulation/Order of Dismissal

## 3. Proposed Additions (not in the deal — attorney decision)
## 4. Adversarial Read — Exposure Register
| Provision | Exposure | Who it hurts | Fix |
## 5. Verification Items
```

## Verification

- [ ] Jurisdiction lock: governing law, dismissal mechanics, and statutory release/confidentiality limits tied to the stated forum.
- [ ] Citation discipline: no invented statutes, required language, or case law; placeholders used.
- [ ] Scope discipline: the draft contains only agreed terms; protective extras are listed separately.
- [ ] Every agreed term appears in the draft, and every draft term traces to the deal or the additions list.
- [ ] Releasors, releasees, and carve-outs are defined and consistent throughout.
- [ ] Payment is sequenced against signature, tax forms, lien resolution, and dismissal.
- [ ] Allocation matches the deal and carries the "labels do not bind the taxing authority" caution.
- [ ] Confidentiality/non-disparagement carve-outs cover agency communications and compelled testimony.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Adding unagreed terms "for protection" inside the draft | Put them in Proposed Additions for attorney decision |
| Releasing "all claims" while the deal excluded a related matter | Carve-outs drawn from the term extraction |
| Confidentiality clause that bars reporting to a government agency | Statutory carve-outs `[VERIFY]` are mandatory |
| Tax allocation stated as if it binds the IRS | Allocation reflects intent; include no-tax-advice rep and caution |
| Dismissal filed before payment with no enforcement hook | Sequence payment → dismissal; address retained jurisdiction |
| Ignoring liens or required court approval | Lien and approval step before payment |

## Example

**Input sketch:** State-court negligence suit; plaintiff Marisol Venn (fictional) injured in a fall at defendant Greyline Storage's facility. Term sheet: $185,000 paid by Greyline's insurer within 30 days of signature; mutual confidentiality of amount; plaintiff to resolve a hospital lien; dismissal with prejudice; each side bears its own fees.

**Output (abridged):**

> **Term extraction.** Row 4: "confidentiality of amount" — term sheet ¶5 — § 10 — Gap: deal is silent on what may be disclosed to tax advisors and in lien negotiations → open item.
>
> **§ 3 Allocation (excerpt).** The Parties intend that the Settlement Payment is paid on account of personal physical injuries `[VERIFY: IRC § 104(a)(2) applicability to these facts]`. No Party makes any representation regarding tax treatment, and each Party relies on its own advisors.
>
> **§ 4 Liens (excerpt).** Plaintiff represents that the only known lien is asserted by Lakeside Regional Hospital and will satisfy it from the Settlement Payment… Plaintiff represents that she {is / is not} and {has / has not} been a beneficiary of a government health program `[VERIFY: reporting obligation]`.
>
> **Exposure register.** § 5 releases "Greyline and its affiliates" — the term sheet named only Greyline; the property manager (a separate entity) may also be a tortfeasor. Fix: confirm with client whether the manager is included, or define releasees to match the deal.
