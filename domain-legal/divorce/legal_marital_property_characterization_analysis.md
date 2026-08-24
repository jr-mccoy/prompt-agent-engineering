---
title: "Marital Property Characterization Analysis"
category: legal/divorce
description: "Characterize each asset and debt as marital/community, separate, or mixed under the controlling state's regime, analyzing premarital ownership, gift/inheritance, commingling, transmutation, active vs. passive appreciation, source-of-funds tracing, and reimbursement/equitable claims — producing an asset-by-asset characterization memo with tracing requirements and confidence levels."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-01
  - RT-02
  - RT-05
  - RP-01
  - CM-02
  - QA-01
  - QA-12
difficulty: advanced
tags:
  - legal
  - divorce
  - family-law
  - property-characterization
  - tracing
  - community-property
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_financial_affidavit_and_disclosure_builder.md
  - domain-legal/divorce/legal_property_division_and_equalization_proposal.md
  - domain-legal/divorce/legal_business_valuation_and_division_framework.md
  - domain-legal/divorce/legal_hidden_asset_and_dissipation_investigation.md
  - domain-legal/divorce/legal_marital_settlement_agreement_drafter.md
---

**Purpose:** Determine, asset by asset, what is marital/community, separate, or mixed under the controlling state's regime, and identify the tracing and proof required to establish each characterization. Output is an internal characterization memo that drives the division proposal — not a final division and not advice to the client.

**When to use:** After disclosure, before drafting a division proposal or MSA; when separate-property, commingling, or transmutation claims are disputed; preparing a property issue for trial.

---

## Your Input

- **Jurisdiction & regime:** [State; community-property or equitable-distribution; the state's marital-property statute and key doctrines]
- **Marriage/separation dates:** [Date of marriage; date of separation/valuation if the state uses one]
- **Asset/debt inventory:** [Each item with value, title, acquisition date, and funding history]
- **Premarital ownership:** [Items owned before marriage; documentation]
- **Gifts/inheritances:** [Items received by gift or inheritance during marriage; to whom]
- **Commingling facts:** [Accounts mixing separate and marital funds; deposits/withdrawals history]
- **Transmutation facts:** [Title changes, written agreements, conduct suggesting a change in character]
- **Appreciation:** [Whether growth was passive (market) or active (spousal effort/contribution)]
- **Contributions:** [Marital funds/effort improving separate property, or separate funds into marital property]
- **Documentation:** [Account statements, deeds, gift letters, prenup/postnup, business records]

---

## Constraints

**Must:**
- State the **regime** and the controlling characterization doctrines for the state `[CITE: …]` before analyzing.
- Characterize **each asset and debt** as marital/community, separate, or mixed, with the reasoning and the tracing/proof required.
- Apply the state's rules on **commingling** (whether it converts separate to marital, and the tracing standard to rebut), **transmutation** (what suffices — title, writing, conduct), and **appreciation** (active vs. passive, community-effort/Pereira-Van Camp-type or state equivalents) `[CITE: …]`.
- Identify **reimbursement / equitable claims** (separate funds into marital property, marital funds into separate property, improvements) available in the state.
- Address the **separation/valuation date** and its effect on characterization of post-separation acquisitions.
- Assign a **confidence level** (High/Medium/Low) to each characterization based on documentation.
- Use placeholders `[CITE: ...]`, `[NEED DOCTRINE: ...]`, `[NEED: ...]` for unsupplied authority or facts.

**Must Not:**
- Apply community-property rules in an equitable-distribution state or vice versa.
- Invent the state's tracing standard, transmutation requirements, appreciation doctrine, or case names.
- Declare an item separate where commingling defeats tracing without addressing the burden and standard.
- Treat appreciation as automatically separate or marital without the active/passive analysis.
- Conflate characterization (what is it) with division/valuation (how is it split / what is it worth).
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **State the regime and doctrines.** Regime; characterization statute; tracing standard; transmutation requirements; appreciation rule; reimbursement claims `[CITE: …]`.
2. **Set the timeline.** Marriage date; separation/valuation date; effect on post-separation acquisitions.
3. **Per-asset characterization.** For each item: acquisition facts → applicable doctrine → characterization → tracing/proof required → confidence.
4. **Commingling analysis.** For mixed accounts/assets, apply the state's tracing method and burden; identify what records are needed.
5. **Transmutation analysis.** Identify any title change, writing, or conduct and whether it meets the state's transmutation standard.
6. **Appreciation analysis.** For separate assets that grew, classify appreciation active vs. passive and allocate accordingly.
7. **Reimbursement/equitable claims.** Identify and quantify available claims (or mark as needing computation).
8. **Summary table & disputed items.** Produce a characterization table; flag the genuinely disputed items and the proof that would resolve them.

---

## Output Format

```markdown
# PROPERTY CHARACTERIZATION ANALYSIS — PRIVILEGED WORK PRODUCT
**State / regime:** {…} [CITE: …]   **Marriage:** {date}   **Separation/valuation:** {date}

## 1. Controlling Doctrines
- Characterization: {…} [CITE] ; Tracing standard: {…} ; Transmutation: {…} ; Appreciation: {active/passive rule} ; Reimbursement: {…}

## 2. Asset-by-Asset Characterization
| Asset/Debt | Acquisition facts | Doctrine applied | Characterization | Tracing/proof needed | Confidence |
|---|---|---|---|---|---|
| {Residence} | {…} | {commingling/transmutation} | Marital/Separate/Mixed | {records} | High/Med/Low |

## 3. Commingling
- {Account}: separate-fund tracing under {standard}; records needed: {…}; risk: {…}

## 4. Transmutation
- {Item}: {title change / writing / conduct} → meets/does not meet {state standard}

## 5. Appreciation
- {Separate asset}: appreciation {active/passive}; allocation: {…}

## 6. Reimbursement / Equitable Claims
- {Claim}: {basis}; amount: {$ / [NEED: computation]}

## 7. Summary & Disputed Items
- Clearly marital: {…} ; Clearly separate: {…} ; Mixed/disputed: {…}
- Proof that would resolve each dispute: {…}
```

---

## Verification

- [ ] Regime and controlling doctrines stated before analysis [CITE].
- [ ] Separation/valuation date addressed and applied to post-separation acquisitions.
- [ ] Each asset and debt characterized with reasoning and required proof.
- [ ] Commingling analyzed with the state's tracing standard and burden.
- [ ] Transmutation assessed against the state's specific requirements.
- [ ] Appreciation classified active vs. passive and allocated.
- [ ] Reimbursement/equitable claims identified and quantified or flagged.
- [ ] Confidence levels assigned per item.
- [ ] No cross-regime errors; no invented doctrines or case names.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Applying community-property tracing in an equitable-distribution state | Confirm the regime; use the state's characterization framework [CITE] |
| Declaring a commingled account "separate" without tracing | Apply the state's tracing standard and burden; identify needed records |
| Treating all appreciation of a separate asset as separate | Run the active vs. passive analysis; allocate community-effort growth |
| Assuming a title change transmutes property | Apply the state's transmutation requirements (often a writing) |
| Ignoring reimbursement claims for funds crossing the marital/separate line | Identify and quantify available reimbursement/equitable claims |
| Conflating characterization with valuation/division | Keep "what is it" separate from "what is it worth / how split" |
| Stating high confidence without documentation | Tie confidence to the records that exist; mark Low where unproven |
| Inventing the state's tracing or transmutation case law | Use [CITE]/[NEED DOCTRINE] placeholders |
| Ignoring the separation date for post-separation earnings/acquisitions | Apply the state's rule on the cutoff date |
| Treating debts as automatically marital | Characterize debts by purpose and timing under the state's rule |
