---
title: "§409A and §1202 QSBS Issue Spotter (Deal Context)"
category: legal/corporate-ma
description: "Identify Section 409A deferred-compensation issues and Section 1202 qualified small business stock (QSBS) qualification questions in an M&A deal: who bears the risk, how it interacts with deal structure, what diligence and structuring moves preserve or impair tax positions."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - m-and-a
  - corporate
  - tax
  - section-409a
  - section-1202
  - qsbs
  - deferred-compensation
updated: "2026-05-11"
related_prompts:
  - domain-legal/corporate-ma/legal_due_diligence_findings_memo.md
  - domain-legal/corporate-ma/legal_disclosure_schedule_drafter.md
  - domain-legal/corporate-ma/legal_board_resolution_drafter.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Surface the §409A deferred-compensation exposures and §1202 QSBS qualification issues that appear in M&A diligence and structuring. Output is a categorized issues list with per-issue risk profile, deal-structure interaction, and recommended diligence / structuring move. This is not a tax opinion — it is the legal-team's issue spotter to drive a qualified tax adviser engagement and inform deal-team risk allocation.

**When to use:** Early diligence on a target with stock options, RSUs, SARs, profits interests, deferred-comp arrangements; structuring discussions where seller QSBS treatment is part of the economics; tax-rep / tax-indemnity drafting; §280G analysis; F-reorg or rollover planning.

---

## Your Input

- **Deal structure:** [Asset / stock / forward merger / reverse triangular merger / 338(h)(10) / 336(e) / F-reorganization / drop-down]
- **Consideration mix:** [Cash / acquirer stock / rollover into newco / earnout / seller note]
- **Governing law of definitive agreement:** [Default: Delaware]
- **Target state of formation/incorporation:** [State]
- **Target entity type and tax classification:** [C-corp / S-corp / LLC taxed as partnership / LLC taxed as C-corp / LLC taxed as S-corp]
- **Industry:** [Industry — drives "qualified trade or business" §1202(e)(3) analysis]
- **Posture:** [Buyer / Seller — drives which side bears each risk]
- **§409A items to evaluate:** [Stock options (ISO / NQSO), SARs, RSUs (vested / unvested at closing), phantom stock, deferred bonus programs, severance arrangements, transaction bonuses, gross-up clauses, change-of-control acceleration provisions]
- **§1202 items to evaluate:** [Stockholders potentially holding QSBS, original-issuance dates, target aggregate-gross-asset history, qualified-trade-or-business analysis, intended rollover structure]
- **Prior §409A valuations:** [Dates, methodology (independent appraisal vs. illiquid startup safe-harbor vs. formula); presumptive reasonableness status]
- **Prior §83(b) elections:** [For restricted stock and profits interests — drives basis and holding period]
- **§280G interaction:** [Is the target potentially a "small business corporation" under §280G(b)(5)(A) and eligible for cleansing vote? Are parachute payments triggered? Is the buyer the §280G safe-harbor target after going public via the deal?]

---

## Constraints

**Must:**
- Address **§409A** and **§1202 QSBS** as separate analytical tracks, each with its own issues list, risk allocation, and structuring moves.
- For each issue, identify: (a) the legal/regulatory test, (b) the factual question to resolve in diligence, (c) the party who bears the economic risk under each typical deal structure, (d) the structuring or contractual mitigation.
- Cite the specific Code section and (where confirmed) the Treasury regulation; use `[CITE: confirm]` markers where uncertain.
- Identify how the deal structure changes the analysis:
  - **§409A**: Asset deals can leave deferred-comp liabilities behind (depending on assumption); stock deals and mergers do not. Acceleration in connection with COC must satisfy §409A's change-in-control rules under Treas. Reg. §1.409A-3(i)(5) or qualify under the "short-term deferral" exception.
  - **§1202 QSBS**: Holding period tacks in a §368 reorganization (§1202(h)); a §1001 taxable exchange resets the period. Cash-out destroys QSBS treatment for any stock not yet at 5 years; rollover via stock-for-stock may preserve.
- Flag the **5-year holding period** under §1202(b)(2) and what tolls vs. tacks.
- Flag the **$50 million aggregate-gross-assets cap** under §1202(d) — measured at the time of issuance and immediately after; once exceeded, future issuances fail QSBS but past-issued QSBS is grandfathered.
- Flag the **original-issuance** requirement (§1202(c)(1)(B)) — secondary purchases are not QSBS.
- Flag **qualified-trade-or-business** disqualifiers under §1202(e)(3) (health, law, accounting, consulting, financial services, brokerage, farming, hospitality, etc.) — common deal-killer for QSBS in service businesses.
- Flag the **per-issuer gain cap** under §1202(b)(1) (greater of $10M or 10× basis) — drives whether multi-entity stacking is worth pursuing.
- Flag §409A failure consequences: 20% additional tax, premium-interest charge, immediate income inclusion of all vested deferred amounts.
- Distinguish documentary failures from operational failures under Treas. Reg. §1.409A-1(c) and the §409A correction programs (IRS Notice 2008-113 for operational; Notice 2010-6 for documentary).
- Address §280G-§409A intersection: parachute gross-ups themselves can be §409A deferred comp; gross-up cancellations can trigger §409A modification rules.

**Must Not:**
- Provide a tax opinion or a legal opinion. Output is the issue spotter; specialized tax counsel/CPA delivers the opinion.
- Invent statutory provisions, regulation citations, revenue rulings, PLRs, or case law. Use `[CITE: confirm]` placeholders.
- Conflate §409A and §83 (separate code sections with separate consequences).
- Conflate ISO and NQSO treatment under §409A (statutory ISOs are excluded from §409A under Treas. Reg. §1.409A-1(b)(5)(ii); NQSOs are excluded only if the option meets specific requirements including strike price ≥ FMV at grant).
- Treat all stockholders as having identical QSBS analysis — original-issuance date and holding period are per-holder facts.
- Insert "consult counsel" disclaimers — this is the practitioner work product flagging issues for qualified tax counsel engagement.

---

## Instructions

1. **Header.** Deal name, target, posture, deal structure, governing law, date, version. Privilege and "attorney work product" legend.
2. **Section A — §409A issue list.** For each potential issue:
   - Item title (e.g., "Stock options with strike price below FMV at grant")
   - Test: cite §409A and relevant regulation
   - Factual diligence questions
   - Risk bearer under the proposed deal structure
   - Mitigation (correction program eligibility, indemnity, special-indemnity recommendation, escrow tranche, R&W treatment)
3. **Section B — §1202 QSBS issue list.** For each potential issue (per-stockholder where appropriate):
   - Item title (e.g., "5-year holding period not yet met at closing")
   - Test: cite §1202 and relevant subsection
   - Factual diligence questions
   - Structuring move (e.g., §368(a)(1)(B) stock-for-stock to tack under §1202(h)(2); deferral via §1045 rollover)
   - Risk if structuring fails
4. **Section C — Deal-structure interaction matrix.** Tabular view: each issue row × each candidate deal structure column, showing whether the issue is heightened, neutralized, or unchanged.
5. **Section D — Risk allocation recommendations.** Specific reps, covenants, special indemnities, escrow tranches, R&W treatment, and pre-close covenants to address each material issue.
6. **Section E — Open items.** Diligence questions still outstanding, who is responsible, target completion date.

---

## Output Format

```markdown
# §409A and §1202 QSBS Issue Spotter
**Project:** [CODE NAME]
**Target:** [TARGET]
**Posture:** [Buyer / Seller]
**Deal Structure:** [Structure]   **Governing Law:** [State]
**Date:** [Date]   **Privileged & Confidential — Attorney Work Product**

**Scope statement:** This memo identifies §409A deferred-compensation and §1202 QSBS issues for risk-allocation and structuring purposes. It is not a tax opinion. Tax conclusions, valuation, and corrections require engagement of qualified tax counsel and the target's tax advisers.

---

## A. §409A Deferred Compensation Issues

### A.1 Stock Options — Strike Price < FMV at Grant
**Test:** Under Treas. Reg. §1.409A-1(b)(5)(i)(A), a stock option is excluded from §409A only if the strike price was at least FMV at the date of grant. A strike below FMV is §409A deferred comp [CITE: confirm].
**Diligence questions:**
- For each option grant, was a §409A valuation in place (independent appraisal under Treas. Reg. §1.409A-1(b)(5)(iv)(B) or illiquid startup safe harbor) and was the strike set at or above the per-share FMV?
- Have any grants been backdated, repriced, or extended without §409A modification analysis?
- For private companies, was the safe-harbor valuation completed within 12 months of each grant date and refreshed after material events?
**Risk bearer:** In a stock deal or merger, buyer inherits the §409A liability with the company (target). In an asset deal, depends on whether the deferred-comp arrangement is an assumed liability.
**Mitigation:**
- Pre-close: correct under IRS Notice 2008-113 (operational failures) or Notice 2010-6 (documentary failures) if eligible — corrections may not be available in the year of vesting/exercise [CITE: confirm].
- Indemnity: tax indemnity covering pre-closing §409A failures with survival = statute of limitations; recommend special-indemnity carve-out from cap and basket.
- R&W: typically excluded by underwriters; seller carve-out required.

### A.2 Acceleration of Vesting on Change of Control
**Test:** Acceleration of vesting tied to a change-in-control event must qualify under Treas. Reg. §1.409A-3(i)(5) (specific definitions of "change in control event") or, alternatively, fit a §409A exclusion (e.g., short-term deferral under Treas. Reg. §1.409A-1(b)(4)).
**Diligence questions:** [...]
**Risk bearer:** [...]
**Mitigation:** [...]

### A.3 Transaction Bonuses / Sale Bonuses
[Same structure]

### A.4 Severance Arrangements
**Test:** Severance can qualify for the §409A "involuntary separation pay" exclusion under Treas. Reg. §1.409A-1(b)(9) if (a) capped at 2× the lesser of base salary or §401(a)(17) limit, (b) paid by end of 2nd year following separation, and (c) tied to involuntary separation [CITE: confirm].

### A.5 §280G Parachute Gross-Up Clauses
**Test:** Gross-up payments are typically themselves §409A deferred comp; their cancellation or modification can trigger §409A modification rules under Treas. Reg. §1.409A-3(j).
**Note:** Pre-closing termination of gross-up clauses must be structured carefully.

### A.6 SARs / Phantom Stock / Profits Interests
[Same structure — SARs follow option-like analysis; phantom stock is typically §409A deferred comp; profits interests have their own partnership-tax considerations under Rev. Proc. 93-27 and 2001-43]

### A.7 RSU Settlement Timing
**Test:** RSUs that fail the short-term deferral exception (settlement within 2.5 months after end of year of vesting) are §409A deferred comp and require compliant settlement timing under Treas. Reg. §1.409A-3.

---

## B. §1202 QSBS Qualification Issues

### B.1 Original Issuance Requirement
**Test:** §1202(c)(1)(B) requires that the stock be acquired by the taxpayer at original issuance directly from the corporation (or through an underwriter), in exchange for money, other property (not stock), or services.
**Diligence questions:**
- For each potential QSBS holder, was the stock acquired by original issuance, or was it a secondary purchase?
- Was the issuance in exchange for stock of another corporation (which generally disqualifies)?
- Were there any redemptions within 1 year before or 1 year after issuance that disqualify under §1202(c)(3) [CITE: confirm]?
**Per-holder fact** — answer for each potential QSBS stockholder.

### B.2 Five-Year Holding Period
**Test:** §1202(b)(2) requires more than 5 years of holding to qualify for the §1202(a) exclusion.
**Tacking and tolling:**
- §1202(h)(2) permits holding-period tacking in a §368 reorganization (e.g., stock-for-stock exchange) where the buyer's stock is QSBS.
- A taxable exchange resets the holding period.
- §1045 rollover allows deferral and tacking if rolled into other QSBS within 60 days.
**Deal-structure interaction:**
- Cash-out merger: 5-year clock must be met as of closing; otherwise QSBS treatment lost.
- Stock-for-stock §368 reorganization: tacking under §1202(h)(2) if buyer's stock is itself QSBS (rare for large public buyers).
- §1045 rollover: time-limited (60 days) and requires reinvestment in original-issuance QSBS — not the buyer's stock.

### B.3 $50 Million Aggregate Gross Assets Cap
**Test:** §1202(d)(1) — the issuer's aggregate gross assets must not have exceeded $50M at any time before and immediately after the issuance.
**Diligence questions:**
- Has the target ever crossed the $50M gross-asset threshold?
- If so, when, and what stock was issued before vs. after?
- Stock issued before the threshold was crossed remains QSBS (grandfathered); stock issued after does not qualify.
- Note: §1202(d)(2)(B) excludes cash and certain investment assets contributed in exchange for the stock issued in the same transaction from the cap measurement [CITE: confirm].

### B.4 Qualified Trade or Business
**Test:** §1202(e)(3) excludes specific trades or businesses: health, law, accounting, actuarial science, performing arts, consulting, athletics, financial services, brokerage services, any trade where the principal asset is the reputation or skill of one or more employees, banking, insurance, financing, leasing, investing, farming, mineral extraction (other than de minimis), and hospitality (hotel, motel, restaurant).
**Diligence questions:**
- What is the target's principal trade or business?
- Is the principal asset the reputation or skill of one or more employees (a common challenge for professional services and consulting)?
- Does any single line of business push the company into a disqualified category?
**Per-line-of-business analysis** for multi-line targets.

### B.5 Active Business Requirement
**Test:** §1202(e)(1) — during substantially all of the taxpayer's holding period, the corporation must use at least 80% of its assets in the active conduct of a qualified trade or business.

### B.6 Per-Issuer Gain Exclusion Cap
**Test:** §1202(b)(1) — exclusion is capped per issuer at the greater of $10M or 10× the aggregate adjusted basis of the QSBS disposed of.
**Implication:** Stacking via gifts to non-grantor trusts or to family members can multiply the per-issuer cap.

### B.7 Redemptions and §1202(c)(3)
**Test:** §1202(c)(3)(A) — significant redemptions of stock from the taxpayer (or related person) within 2 years before/after the issuance date can disqualify; §1202(c)(3)(B) — redemptions of more than 5% of aggregate value within 1 year before/after also disqualify [CITE: confirm].
**Diligence questions:**
- Has the target conducted any redemptions, including tender offers, in the 2 years before each potential QSBS issuance?

### B.8 Rollover and F-Reorganization Considerations
**Test:** A pre-closing F-reorganization (e.g., to convert an S-corp to a holdco / opco structure) can affect QSBS treatment if executed in a manner that creates a new corporation. Careful structuring required to preserve original-issuance date.

---

## C. Deal-Structure Interaction Matrix

| Issue | Asset Deal | Stock Deal | Forward Merger | Reverse Triangular Merger | F-Reorg (Pre-Close) |
|---|---|---|---|---|---|
| §409A deferred comp liability | May be left behind | Inherited | Inherited | Inherited | Generally inherited |
| §1202 QSBS holding period | Cash sale → lost if <5 years | Cash sale → lost if <5 years | Cash sale → lost | Cash sale → lost; stock consideration may tack under §1202(h)(2) | May preserve original-issuance date |
| §280G parachute gross-up | Less likely triggered (assets) | Likely | Likely | Likely | N/A directly |
| §338(h)(10) availability | N/A | Available for stock of S-corp or 80% sub | N/A | N/A | N/A |

---

## D. Risk Allocation Recommendations

### Reps and Warranties
- Tax rep §[X.Y]: separate sub-section confirming §409A compliance (operational and documentary) for all "nonqualified deferred compensation plans" as defined in Treas. Reg. §1.409A-1(a).
- Tax rep §[X.Y]: stockholder-level QSBS confirmation — note this is unusual; QSBS is a per-holder analysis and target generally only reps issuer-level facts ($50M cap, qualified trade or business, active business).

### Covenants
- Pre-close covenant: target shall not modify any deferred-comp arrangement in a manner inconsistent with §409A; no new grants of stock options without §409A valuation; no acceleration outside the agreement.
- §280G cleansing-vote covenant if parachute exposure exists.

### Special Indemnities
- §409A special indemnity: uncapped or capped at purchase price; survival = statute of limitations; no basket; excluded from R&W coverage.
- Pre-closing tax indemnity with §409A failures and QSBS-issuer-level reps treated as fundamental.

### Escrow
- Separate tax escrow tranche sized to estimated §409A and other identified tax exposures; release tied to statute of limitations.

### R&W Insurance
- §409A and QSBS issues are commonly excluded or scoped down by underwriters; require seller-side carve-out indemnity for excluded items.

---

## E. Open Items

| # | Question | Owner | Target Date |
|---|---|---|---|
| 1 | §409A valuations for option grants from [date] to closing | Tax counsel | [date] |
| 2 | Stockholder-level QSBS chart (issuance date, holding period, original-issuance status) | Target counsel | [date] |
| 3 | Aggregate-gross-assets history at each issuance | Target CFO | [date] |
{...}
```

---

## Verification

- [ ] §409A and §1202 analyzed as separate tracks.
- [ ] Each issue includes test, diligence questions, risk bearer, and mitigation.
- [ ] Deal-structure interaction matrix present.
- [ ] §280G-§409A intersection addressed.
- [ ] QSBS five-year holding, $50M cap, original-issuance, qualified-trade-or-business, and per-issuer gain cap all addressed.
- [ ] Tacking under §1202(h)(2) and §1045 rollover addressed.
- [ ] §409A correction programs (Notice 2008-113 and Notice 2010-6) referenced.
- [ ] Statutory and regulatory citations are placeholders or marked `[CITE: confirm]`; no fabricated authority.
- [ ] Risk-allocation recommendations specific (special indemnity uncapped, separate tax escrow tranche, fundamental survival).
- [ ] Output frames itself as an issue spotter, not a tax opinion.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Treating QSBS as an issuer-only analysis | QSBS is per-holder: original-issuance date, holding period, and §1045 elections vary per stockholder; analyze each holder separately |
| Assuming a §368 stock-for-stock exchange preserves QSBS | Only if the buyer's stock is itself QSBS (§1202(h)(2)); a public-company buyer's stock generally is not — tacking does not produce QSBS, only allows the original QSBS shares (if continued to be held) to retain status until disposition |
| Confusing ISO and §409A | Statutory ISOs that meet §422 are excluded from §409A under Treas. Reg. §1.409A-1(b)(5)(ii); NQSOs are excluded only if strike ≥ FMV at grant and other requirements met |
| Treating safe-harbor §409A valuation as automatically valid | The safe harbor under Treas. Reg. §1.409A-1(b)(5)(iv)(B) is rebuttable; valuations refresh requirement after material events; older than 12 months may lose presumption |
| Assuming severance is §409A-exempt | Only if it fits the involuntary-separation pay exclusion under Treas. Reg. §1.409A-1(b)(9): capped (2× lesser of base or §401(a)(17) limit), payment by end of 2nd year, involuntary separation |
| Treating QSBS qualified-trade-or-business test as a global yes/no | §1202(e)(3) excludes specific service businesses; mixed-business targets need per-line analysis; "principal asset is reputation or skill of employees" is a common trap for consulting/professional services |
| Ignoring the redemption rules under §1202(c)(3) | Redemptions within the windows can disqualify entire issuances; diligence target redemption history before relying on QSBS treatment |
| Cancelling a §280G gross-up clause without §409A analysis | Cancellation may itself be a §409A "modification" or "acceleration"; structure carefully or risk additional §409A failure |
| Treating §1202 cap as fixed at $10M | Cap is greater of $10M or 10× aggregate adjusted basis; for high-basis QSBS (e.g., founders who contributed substantial property), 10× basis can be much higher |
| Promising §409A correction will fix any failure | Correction programs (Notice 2008-113 and 2010-6) have eligibility limits, year-of-vesting restrictions, and may not be available; do not promise; identify eligibility as a diligence question |
| Treating §1202(d) gross-asset cap as a continuing requirement | Cap is measured at issuance and immediately after; once stock is QSBS at issuance, later asset growth does not retroactively disqualify (though future issuances are not QSBS) |
| Drafting a stockholder-level QSBS rep into the target's tax reps | Issuer-level reps belong with target ($50M cap, qualified trade, active business, no disqualifying redemptions); holding-period and original-issuance are per-holder and either repped by individual sellers or excluded |
