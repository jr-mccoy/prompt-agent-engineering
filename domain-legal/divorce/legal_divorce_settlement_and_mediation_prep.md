---
title: "Divorce Settlement and Mediation Prep"
category: legal/divorce
description: "Prepare client and counsel for divorce mediation or settlement on the financial issues: gate on disclosure completeness, map interests behind positions for property, support, and tax, set a BATNA against the likely litigated property division and support range, build a proposal ladder (opening/target/walk-away) per issue, identify trade space (asset trades vs. support duration, tax character, timing, QDRO mechanics), screen DV/coercion mediation-appropriateness, and produce a mediation agenda and a draft financial term-sheet skeleton."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - CM-02
  - DS-02
  - QA-01
  - QA-12
difficulty: advanced
tags:
  - legal
  - divorce
  - family-law
  - mediation
  - settlement
  - negotiation
  - property-division
  - spousal-support
updated: "2026-06-10"
related_prompts:
  - domain-legal/custody/legal_custody_settlement_and_mediation_prep.md
  - domain-legal/divorce/legal_divorce_mediation_brief_drafter.md
  - domain-legal/divorce/legal_post_mediation_term_sheet_and_mou_drafter.md
  - domain-legal/divorce/legal_property_division_and_equalization_proposal.md
  - domain-legal/divorce/legal_spousal_support_alimony_analysis.md
  - domain-legal/divorce/legal_marital_settlement_agreement_drafter.md
---

**Purpose:** Prepare a divorce client and counsel for mediation or settlement on the financial issues — property division, equalization, spousal support, child support, and fees — by gating on disclosure completeness, anchoring to a realistic litigated BATNA, building a proposal ladder and trade space that exploits differences in what each spouse values (cash flow vs. assets, tax character, timing), and producing a mediation agenda plus a financial term-sheet skeleton. Output is a preparation memo and term-sheet skeleton, not advice to the client and not a binding agreement. For custody and parenting-time issues, use `legal_custody_settlement_and_mediation_prep.md` alongside this prompt.

**When to use:** Before divorce mediation (voluntary or court-ordered), a settlement conference, or a four-way settlement meeting; structuring an opening financial proposal; deciding whether the case is ready to mediate at all.

---

## Your Input

- **Jurisdiction:** [State whose dissolution law governs; community-property vs. equitable-distribution regime; whether mediation is mandatory; mediation-confidentiality rule `[CITE: …]`]
- **Disclosure status:** [Financial affidavits exchanged? Mandatory disclosures complete? Outstanding discovery, valuations, or suspected nondisclosure/dissipation]
- **Marital estate:** [Asset/debt inventory with values, characterization (marital/separate/mixed), and items still needing appraisal or tracing]
- **Support posture:** [Incomes, earning capacities, marriage length, guideline child-support model, spousal-support exposure/entitlement range `[NEED GUIDELINE: …]`]
- **Tax facts:** [Filing posture, basis in major assets, retirement account types (pre-tax vs. Roth), support tax treatment under current law]
- **Positions:** [What each spouse says they want on each financial issue]
- **Interests:** [The needs behind the positions — liquidity, housing stability, retirement security, business continuity, speed, privacy, cost control]
- **Likely litigated outcome:** [Realistic division and support range under the governing regime — the BATNA anchor; cross-reference the property-division and spousal-support analyses]
- **Conflict & safety:** [Conflict level; any DV, coercive control, or severe power imbalance affecting whether and how to mediate]
- **Constraints:** [Client's cash-flow needs, deadlines (trial date, lock expiration, business event), fee budget remaining]

---

## Constraints

**Must:**
- **Gate on disclosure:** assess whether disclosure is complete enough to value the trade space; if material assets are unvalued or nondisclosure/dissipation is suspected, flag that mediating now means negotiating blind and state what must be obtained first. Do not paper over an incomplete record.
- Confirm the **property regime** (community vs. equitable distribution); if not supplied, mark `[NEED REGIME]` — the entire BATNA turns on it.
- Separate **positions from interests** for each financial issue and build the strategy around interests.
- Anchor the negotiation to a realistic **BATNA** — the likely litigated division and support range plus the cost, delay, and risk of trial — so every concession is measured against the real alternative.
- Build a **proposal ladder** (opening, target, walk-away) for each issue in play: property division/equalization, spousal support amount and duration, child support, and fees.
- Identify **trade space** across issues: assets vs. support duration, pre-tax vs. after-tax dollars, lump sum vs. stream, house vs. retirement, buyout timing, QDRO mechanics, who carries debt, fee allocation — and value trades on an **after-tax, risk-adjusted** basis.
- Treat **child support as guideline-governed**, not freely tradeable: deviations require the state's findings and child support is never bargained non-modifiable `[NEED GUIDELINE: …]`.
- **Screen for DV/coercive control and power imbalance:** assess whether mediation is appropriate, and if so what safeguards (separate sessions/caucus, shuttle, counsel present, no direct contact) are needed; some cases should not be mediated jointly.
- Respect **mediation confidentiality** and what can/cannot be used later `[CITE: …]`.
- Produce a **mediation agenda** (sequenced easy-to-hard or package-based) and a **financial term-sheet skeleton** capturing the target proposal.
- State **confidence levels** (High/Medium/Low) on the BATNA range and key valuations.
- Use placeholders `[CITE: …]`, `[NEED: …]`, `[NEED GUIDELINE: …]`, `[NEED VALUATION: …]` for any authority, figure, or fact not supplied.

**Must Not:**
- Invent the state's division standard, support guideline figures, alimony factors, or mediation-confidentiality rules.
- Recommend mediating where suspected nondisclosure or missing valuations make the trade space unknowable, without flagging the risk and the cure.
- Set a BATNA untethered to the realistic litigated outcome (an over-optimistic anchor wastes leverage; an under-confident one gives the case away).
- Trade nominal dollars as if equal — compare after-tax, time-adjusted values (pre-tax retirement ≠ cash; support stream ≠ lump sum).
- Counsel concealment, dissipation, or bad-faith negotiation; disclosure obligations continue through mediation.
- Treat a DV or coercion disclosure as a routine prep item — escalate it to the safety screen.
- Predict a specific judicial outcome as certain — ranges with confidence levels only.
- Insert generic "consult counsel" disclaimers — this is the attorney's own preparation memo.

---

## Instructions

1. **Readiness gate.** Assess disclosure completeness: affidavits, mandatory disclosures, valuations, tracing. List what is missing and whether each gap is material to the trade space. State whether the case is ready to mediate, ready with caveats, or not ready (and what would make it ready).
2. **Regime & legal frame.** Confirm community property vs. equitable distribution `[CITE: …]`; note the division standard and any statutory factors `[NEED FACTOR LIST: …]`; note whether mediation is mandatory and the confidentiality rule.
3. **Interests mapping.** Translate each spouse's positions on each financial issue into underlying interests (liquidity, housing, retirement security, business continuity, speed, privacy, cost).
4. **BATNA.** State the realistic litigated division and support range, plus trial cost, delay, and risk; assign confidence levels; cross-reference the property-division and spousal-support analyses where they exist.
5. **Proposal ladder.** Define opening, target, and walk-away for each issue: property/equalization, spousal support (amount and duration), child support (guideline-anchored), fees.
6. **Trade space & tax lens.** Map cross-issue trades and value each on an after-tax, risk-adjusted basis: house vs. retirement (QDRO mechanics, basis), lump sum vs. support stream, debt allocation, buyout timing. Flag trades that look even in nominal dollars but are not.
7. **Safety & power-imbalance screen.** Assess mediation-appropriateness given any DV, coercive control, or severe imbalance; specify safeguards or recommend against joint mediation.
8. **Agenda & sequencing.** Build the mediation agenda: issue order (momentum-building vs. package negotiation), what to caucus on, what the client should and should not say, and decision points requiring a recess.
9. **Term-sheet skeleton.** Produce the financial term-sheet skeleton for the target proposal: property allocation, equalization amount and payment terms, support amount/duration/modifiability, child support, fees, conditions (QDRO review, refinance deadlines, appraisal true-ups).
10. **Close-out plan.** Note how agreement will be captured at the session (hand off to `legal_post_mediation_term_sheet_and_mou_drafter.md`) and what happens on impasse (next session, discovery, trial track).

---

## Output Format

```markdown
# DIVORCE SETTLEMENT / MEDIATION PREP — PRIVILEGED & CONFIDENTIAL ATTORNEY WORK PRODUCT
**Client:** {name}   **Matter:** {short title}   **Date:** {date}
**State:** {…}   **Regime:** {community / equitable / [NEED REGIME]}   **Mediation:** {voluntary/mandatory; confidentiality [CITE: …]}

## 1. Readiness Gate
- Disclosure status: {complete / gaps}   Material gaps: {item — why it matters}
- Verdict: {Ready / Ready with caveats: … / NOT ready — obtain: …}

## 2. Interests Behind Positions
| Issue | Client position | Client interest | Other spouse position | Likely interest |
|---|---|---|---|---|

## 3. BATNA (litigated anchor)
- Likely division range: {…} — Confidence: {H/M/L}
- Likely support range: {amount/duration} [NEED GUIDELINE: …] — Confidence: {…}
- Trial cost/delay/risk: {…}

## 4. Proposal Ladder
| Issue | Opening | Target | Walk-away |
|---|---|---|---|
| Property / equalization | {…} | {…} | {…} |
| Spousal support (amt/duration) | {…} | {…} | {…} |
| Child support | {guideline-anchored} | {…} | {…} |
| Fees | {…} | {…} | {…} |

## 5. Trade Space (after-tax view)
| Give | Get | Nominal value | After-tax / risk-adjusted value | Note |
|---|---|---|---|---|

## 6. Safety & Power-Imbalance Screen
- Mediation appropriate? {yes / with safeguards / no}   Safeguards: {caucus / shuttle / counsel present / no contact}

## 7. Agenda & Sequencing
- Order: {…}   Caucus items: {…}   Client coaching: {say / don't say}   Recess triggers: {…}

## 8. Financial Term-Sheet Skeleton (target)
- Property: {allocation} ; Equalization: {amount, payment terms}
- Spousal support: {amount / duration / modifiability}
- Child support: {guideline figure / deviation + findings} [NEED GUIDELINE: …]
- Fees: {…} ; Conditions: {QDRO review / refinance by … / appraisal true-up}

## 9. Close-Out / Impasse Plan
- If agreement: {capture method — term sheet / MOU}   If impasse: {next step}
```

---

## Verification

- [ ] Disclosure-completeness gate applied; material gaps listed with a ready/not-ready verdict.
- [ ] Property regime confirmed or flagged `[NEED REGIME]`.
- [ ] Positions translated into interests for both spouses on each financial issue.
- [ ] BATNA anchored to the realistic litigated division and support range with confidence levels and trial cost/risk.
- [ ] Proposal ladder set (opening/target/walk-away) for every issue in play.
- [ ] Trades valued after-tax and risk-adjusted, not in nominal dollars.
- [ ] Child support kept guideline-anchored; no non-modifiable child-support bargaining.
- [ ] DV/coercion/power-imbalance screen performed; safeguards or no-mediation recommendation stated.
- [ ] Mediation confidentiality respected `[CITE: …]`.
- [ ] Term-sheet skeleton and agenda produced; no invented guideline figures, factors, or rules.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Mediating on an incomplete or suspect financial record | Gate first: list material gaps; negotiating blind is the error, not a detail |
| Assuming community property in an equitable-distribution state (or vice versa) | Confirm the regime — the BATNA and every trade turn on it |
| Treating pre-tax retirement dollars as equal to cash or home equity | Compare after-tax values; note QDRO mechanics and basis |
| Trading child support like any other chip | Guideline-governed; deviations need findings; never non-modifiable [NEED GUIDELINE] |
| Over-optimistic BATNA inflating the walk-away | Tie the anchor to the realistic litigated range plus trial cost/delay/risk |
| Under-confident BATNA giving the estate away | Same anchor discipline — ranges with stated confidence, not fear |
| Ignoring DV/coercive control because "it's just financial mediation" | Screen; power imbalance corrupts financial bargains too; safeguards or no joint mediation |
| Valuing a support stream and a lump sum as interchangeable | Time-adjust and risk-adjust (payor default, modifiability, remarriage termination) |
| Opening position with no defined walk-away | Define opening, target, and walk-away per issue before the session |
| Letting the agenda default to hardest-issue-first | Sequence deliberately — momentum-building or package — and plan caucus use |
| Inventing alimony factors or guideline numbers to fill the memo | Use [CITE] / [NEED GUIDELINE] placeholders |
| Counseling silence about a known material asset | Disclosure duties continue through mediation; concealment voids agreements |
