---
title: "Section 1031 Like-Kind Exchange Analysis"
category: legal/tax
description: "Counsel-facing qualification analysis for a real-property like-kind exchange under IRC §1031 — held-for-use/investment intent, like-kind real property, qualified intermediary and constructive-receipt safeguards, identification and exchange-period compliance, boot and debt relief, related-party and reverse/improvement exchange traps — producing a pass / fail / at-risk scorecard with every deadline and rule reference marked for verification."
techniques:
  - DS-01
  - ST-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - tax
  - section-1031
  - like-kind-exchange
  - real-estate-tax
  - qualified-intermediary
  - boot
updated: "2026-09-24"
reasoning:
  styles: [analytic, procedural, systematic]
  stakes: high
  horizon: months
  uncertainty: risk
  evidence_quality: moderate
  domain_complexity: regulated
  collaboration: solo_or_team
  output_format: [structured, matrix]
  user_role: [lawyer, analyst]
  mode: [audit, assess]
related_prompts:
  - domain-legal/tax/legal_tax_research_memo.md
  - domain-finance/tax-planning/finance_capital_gains_harvesting_analysis.md
  - domain-finance/tax-planning/finance_multi_year_tax_projection.md
  - domain-legal/contracts-transactional/legal_contract_review_full_redline.md
---

# Section 1031 Like-Kind Exchange Analysis

**Objective:** Determine whether a proposed or in-progress real-property exchange qualifies for nonrecognition under §1031, element by element, and quantify what gain is recognized anyway (boot, net debt relief). The analysis tests the documents — exchange agreement, qualified-intermediary agreement, identification notice, closing statements — rather than the parties' description of them, and flags every timing and related-party trap before the deal closes or while it can still be fixed.

**When to use:**
- Pre-closing review of a relinquished-property sale intended to begin an exchange.
- Mid-exchange compliance check before the identification or exchange period ends.
- Reverse or improvement (build-to-suit) exchange structuring.
- Post-closing review for return reporting or an examination.

**Distinct from:**
- `domain-finance/tax-planning/finance_capital_gains_harvesting_analysis.md` and `finance_multi_year_tax_projection.md` — whether to realize gain and the multi-year tax effect; this prompt tests legal qualification of the exchange.
- `domain-legal/divorce/legal_divorce_tax_consequences_analysis.md` — transfers between spouses incident to divorce, which follow different rules.
- A future `domain-legal/real-estate/` purchase-agreement prompt — the underlying conveyance terms; here only the exchange-relevant clauses are reviewed.

**Audience:** Tax and real-estate counsel advising investors, funds, and operating businesses.

---

## Your Input

- **Taxpayer:** [Individual / partnership / LLC (disregarded or not) / corporation / trust — same taxpayer must sell and buy]
- **Relinquished property:** [Description, use history, holding period, adjusted basis, debt, sale price, closing date]
- **Replacement property(ies):** [Description, intended use, price, debt, closing date or target]
- **Exchange structure:** [Forward / reverse / improvement; QI identity and agreement; exchange accommodation titleholder if reverse]
- **Identification:** [Notice text, date delivered, to whom, properties identified with descriptions and values]
- **Closing statements:** [Settlement statements for both legs — cash, credits, prorations, fees, debt]
- **Parties:** [Seller of replacement property; relationship to taxpayer; any related-party dealings]
- **Recent events:** [Partnership drop-and-swap, entity conversions, personal use, intent to sell soon after]
- **Rules you have verified:** [Current identification and exchange-period rules, return due date interaction — or leave blank for `[VERIFY]`]

---

## Constraints

### Must
- Test each element separately: (1) property held for productive use in a trade or business or for investment, both legs; (2) like-kind real property (and exclude property that is not real property under current rules `[VERIFY]`); (3) same taxpayer; (4) no actual or constructive receipt of proceeds (QI and exchange-agreement restrictions); (5) timely, written, unambiguous identification within the identification rules; (6) receipt of replacement property within the exchange period.
- Compute **realized gain, boot, and recognized gain**, netting liabilities per the regulations and treating cash paid or received correctly `[VERIFY: netting rules]`.
- Mark the **identification and exchange periods** with dates computed from the closing date *and* the verification tag — commonly cited as 45 and 180 days, with the exchange period cut short by the return due date unless extended `[VERIFY: §1031(a)(3)]`.
- Test identification against the **three-property, 200%, and 95%** alternatives `[VERIFY: Treas. Reg. §1.1031(k)-1(c)(4)]`.
- Screen **related-party** rules (disposition within the statutory holding period after exchange; acquiring replacement property from a related party) `[VERIFY: §1031(f) and related guidance]`.
- For reverse or improvement exchanges, test against the safe-harbor procedure and its time limits `[VERIFY: current revenue procedure]`.
- Report each element as **Pass / Fail / At risk** with the document that proves it.

### Must Not
- Compute deadlines without the `[VERIFY]` tag, or ignore that no extension exists for weekends or holidays except as specifically provided `[VERIFY]`.
- Accept "held for investment" on intent statements alone when facts show dealer activity, personal use, or an immediate resale plan.
- Treat a disregarded-entity change or drop-and-swap as neutral; flag the same-taxpayer and holding-intent risk.
- Invent revenue procedure numbers, safe-harbor time limits, or state withholding rules.
- Offer planning to rescue a failed exchange that depends on backdating or altering identification — flag any such suggestion as improper.

---

## Instructions

1. **Map the transaction timeline** from both closing statements and the identification notice.
2. **Element-by-element test** with evidence citations to documents.
3. **Identification audit:** number of properties, aggregate value vs. relinquished value, description adequacy, delivery method and recipient.
4. **Constructive-receipt audit:** QI agreement restrictions on the taxpayer's rights to money; earnest-money and closing-cost handling; any funds released to the taxpayer.
5. **Boot computation:** cash boot, mortgage boot netting, non-qualifying property, closing costs treatment.
6. **Related-party and entity screens.**
7. **State issues:** state conformity, withholding, and clawback-style tracking of deferred gain `[VERIFY: state rule]`.
8. **Scorecard and remediation** — what can still be fixed and by when; what cannot.

---

## Output Format

```markdown
# §1031 Exchange Analysis — {Taxpayer}
**Structure:** {forward / reverse / improvement}  |  **Relinquished closing:** {date}  |  **Privileged & Confidential**

## 1. Timeline
| Event | Date | Deadline computed | [VERIFY] |
## 2. Qualification Scorecard
| Element | Status (Pass / Fail / At risk) | Evidence (document, page) | Note |
## 3. Identification Audit
## 4. Constructive-Receipt Audit
## 5. Gain and Boot
| Item | Relinquished | Replacement | Net |
| Realized gain | | | |
| Recognized gain (boot) | | | |
| Deferred gain / replacement basis | | | |
## 6. Related-Party and Entity Screens
## 7. State Considerations
## 8. Remediation and Open Items
```

---

## Worked Example

**Input (abridged):** LLC taxed as a partnership sells a warehouse on 2026-03-02 for $3.0M (adjusted basis $1.1M; mortgage $900K paid off at closing). QI holds $2.07M net proceeds. Identification notice dated 2026-04-14, emailed to QI, identifies four properties with aggregate value $7.2M. Replacement: one property purchased 2026-07-20 for $2.6M with a new $600K loan. The LLC's two members plan to take the replacement property out as tenants-in-common next year.

**Output (excerpt):**

> **Timeline:** Identification period ends 2026-04-16 and exchange period ends 2026-08-29 if computed as 45/180 days from 2026-03-02 — and the exchange period could end earlier at the return due date unless extended `[VERIFY: §1031(a)(3); confirm partnership return due date and extension]`. Notice dated 2026-04-14 — **Pass** on timing if delivery on that date is documented.
>
> **Identification audit:** Four properties exceed the three-property rule; aggregate $7.2M exceeds 200% of $3.0M ($6.0M). The 95% alternative is not met — only one property ($2.6M of $7.2M) was acquired. **Fail** under the identification rules `[VERIFY: Treas. Reg. §1.1031(k)-1(c)(4)]`, unless a timely, written revocation of one property before the period ended exists — request it.
>
> **Boot (if identification is cured):** Debt relieved $900K vs. new debt $600K → $300K net debt relief; no additional cash from the LLC offsets it. Proceeds held $2.07M vs. $2.0M equity needed ($2.6M − $600K) → $70K unused proceeds released after the exchange period as cash boot. Recognized gain ≈ $300K + $70K = **$370K** (limited to the $1.9M realized gain before closing costs) `[VERIFY: netting per regulation; treatment of closing costs]`.
>
> **Entity screen:** The planned distribution to members as tenants-in-common soon after acquisition puts the LLC's "held for investment" intent at risk; flag before any restructuring.

---

## Verification

- [ ] Jurisdiction lock: federal §1031 analysis stated; state conformity addressed separately.
- [ ] Every element scored with a document cited.
- [ ] Identification and exchange periods computed and tagged `[VERIFY]`, including return-due-date interaction.
- [ ] Identification tested against all three alternatives.
- [ ] Boot computed with liability netting shown.
- [ ] Related-party and entity-change screens run.
- [ ] No revenue procedure numbers, safe-harbor limits, or state rules invented.
- [ ] No remediation that depends on altering dates or documents.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Accepting "we identified three properties" without reading the notice | Audit the notice itself: count, descriptions, values, delivery |
| Missing the return-due-date cutoff on the exchange period | Compute both and use the earlier; tag `[VERIFY]` |
| Treating replacement debt as automatically offsetting relinquished debt | Apply the netting rules; cash paid offsets debt relief, not the reverse |
| Assuming the QI arrangement blocks constructive receipt | Read the QI agreement's restrictions and any early releases |
| Ignoring entity changes around the exchange | Same-taxpayer and holding-intent risk from drop-and-swaps and conversions |
| Treating all "real estate" as like-kind without checking the current definition | Confirm the property is real property under current rules; personal property is excluded |
| Suggesting after-the-fact identification fixes | Flag as improper; only timely revocations or amendments count |
