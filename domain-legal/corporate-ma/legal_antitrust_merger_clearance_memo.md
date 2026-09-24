---
title: "Antitrust Merger Clearance Memo — Reportability, Theories of Harm, and Remedies Posture"
category: legal/corporate-ma
description: "Attorney-facing merger-control memo for a proposed acquisition: pre-merger notification reportability across jurisdictions, substantive theories of harm the agencies are likely to test, document and gun-jumping risk, a remedies posture, and the risk-allocation terms the deal documents need — distinct from general due-diligence findings and from an antitrust conduct-compliance program review."
techniques:
  - DS-32
  - RT-02
  - NE-10
  - QA-02
  - CM-02
difficulty: advanced
tags:
  - legal
  - antitrust
  - merger-control
  - hsr
  - corporate-ma
  - buying-a-competitor
  - deal-regulatory-risk
updated: "2026-09-24"
related_prompts:
  - domain-legal/corporate-ma/legal_due_diligence_findings_memo.md
  - domain-legal/contracts-transactional/legal_term_sheet_to_definitive_translator.md
  - domain-legal/regulatory-compliance/legal_compliance_program_gap_analysis.md
---

# Antitrust Merger Clearance Memo — Reportability, Theories of Harm, and Remedies Posture

> **Scope guard — attorney-facing only.** This prompt is for antitrust and M&A counsel advising a buyer, seller, or target on merger clearance. It does not decide whether a deal should proceed on business grounds, and it is not a substitute for economist market analysis where the agencies will demand one. A founder or executive without counsel should route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md`.

> **No-fabrication rule.** Do not state notification thresholds, filing fees, waiting-period lengths, concentration cut-offs, or foreign-regime triggers as settled numbers — they are adjusted periodically and differ by regime. Write them as `[VERIFY: …]`. Do not invent agency guidance, consent decrees, or case names; use `[CITE: …]` / `[NEED HOLDING: …]`.

## When to Use

- Early deal stage: counsel needs a clearance-risk read before signing to set efforts covenants, outside date, and any reverse termination fee.
- Pre-filing: the team needs the reportability analysis, a document-risk review plan, and a narrative on the likely theories of harm.
- A second-request or in-depth-review risk is emerging and the team needs a remedies posture.

**Not this prompt if:**
- You need the full diligence findings across all legal workstreams — use `domain-legal/corporate-ma/legal_due_diligence_findings_memo.md` and feed its antitrust items here.
- The question is ongoing antitrust conduct compliance (pricing contacts, trade-association exposure) — use `domain-legal/regulatory-compliance/legal_compliance_program_gap_analysis.md`.
- You are translating an agreed term sheet into definitive terms without a clearance question — use `domain-legal/contracts-transactional/legal_term_sheet_to_definitive_translator.md`.

## Inputs

- **Jurisdictions (required):** Where the parties have sales, assets, or subsidiaries; which merger-control regimes may apply (US federal, US state AG interest, EU/UK/other) — or `unknown` for screening.
- **Deal structure:** Asset or equity purchase, merger, minority stake, joint venture; consideration; whether voting securities or assets are acquired; closing conditions drafted so far.
- **Parties' financials:** Revenues and assets by jurisdiction as needed for threshold tests (supplied, not estimated).
- **Overlaps:** Products and services where the parties compete (horizontal), supply one another (vertical), or are adjacent/nascent competitors; customer and competitor lists; share estimates with their source.
- **Deal documents and internal materials:** Board decks, strategy documents, and deal-team emails that discuss competition, markets, or synergies.
- **Sector regulators:** Any industry-specific approval (communications, banking, energy, defense, healthcare) and foreign-investment screening exposure.
- **Timetable:** Target signing and outside dates.

## Method

1. **Reportability screen, per regime.** For each jurisdiction, run its test on the supplied figures: size-of-transaction and size-of-person tests for US pre-merger notification `[VERIFY: current annually adjusted thresholds and filing-fee tiers]`; foreign turnover/share-of-supply or other triggers `[VERIFY each regime]`. Check applicable exemptions `[VERIFY]`. Output: file / do not file / analysis needed, with the deciding figure. Never estimate a party's revenue to force an answer.
2. **Filing content and timing.** Identify what the filing requires, including transaction-related documents and any expanded disclosures under the current form `[VERIFY: current notification form and instructions]`. Waiting period and extension mechanics `[VERIFY]`; second-request or in-depth-review timelines are estimates only.
3. **Market framing.** For each overlap, propose candidate product and geographic markets and the evidence that would test them (customer switching, ordinary-course documents, bidding data). Flag where the agencies are likely to argue for a narrower market than the parties.
4. **Theories of harm — one row each.** Unilateral effects (closeness of competition, diversion); coordinated effects (market structure, transparency, history of coordination); vertical foreclosure (input or customer); elimination of potential or nascent competition; entrenchment or ecosystem effects; labor-market effects; serial-acquisition patterns. For each: evidence for, evidence against, and a probability tier (low / moderate / high) with reasoning. Refer to the currently operative merger guidelines and any concentration presumptions only as `[VERIFY: current guidelines and thresholds]`.
5. **Document risk.** Review supplied internal materials for statements about "eliminating a competitor," pricing power, or market dominance. List each, its author and date, and how it will read to an agency. Recommend document-creation guidance going forward — never destruction or editing of existing documents.
6. **Gun-jumping and information exchange.** Check interim operating covenants and pre-closing integration plans for premature transfer of control; set clean-team rules for competitively sensitive information.
7. **Remedies posture.** Whether a divestiture could resolve each theory of harm; whether an upfront buyer or fix-it-first approach is realistic; the agencies' current stance on behavioral remedies `[VERIFY]`.
8. **Deal-document risk allocation.** Recommend efforts standard (and whether any divestiture limit applies), outside date and extensions, reverse termination fee, ticking fee, cooperation and control-of-strategy covenants, and closing conditions tied to each regime.

## Output Format

```markdown
# Merger Clearance Memo — {Buyer} / {Target}
**Deal:** {structure, consideration}  |  **Target signing:** {…}  |  **Outside date (proposed):** {…}  |  **Privileged & Confidential**

## 1. Executive Summary (clearance risk: low / moderate / high, and why in three sentences)
## 2. Reportability by Regime
| Regime | Test applied | Figures used (source) | Threshold [VERIFY] | Result | Waiting period [VERIFY] |
## 3. Overlaps and Candidate Markets
## 4. Theories of Harm
| Theory | Overlap | Evidence for | Evidence against | Tier | What would change the tier |
## 5. Document Risk Log
## 6. Gun-Jumping / Clean-Team Controls
## 7. Remedies Posture
## 8. Recommended Deal Terms
## 9. Timeline Scenarios (clean clearance / extended review / challenge)
## 10. Verification Items
```

## Verification

- [ ] Jurisdiction lock: every regime considered is named, and each threshold, fee, and waiting period is `[VERIFY]` unless supplied with a source.
- [ ] Citation discipline: no guideline section, case, or consent decree cited without `[CITE]`.
- [ ] Scope discipline: memo addresses clearance risk and deal terms, not deal valuation or business merit.
- [ ] Reportability used only supplied financial figures; gaps listed as `[NEED: …]`.
- [ ] Each theory of harm has evidence on both sides and a stated tier, not a bare conclusion.
- [ ] Document risk section recommends forward-looking guidance only; nothing suggests altering existing records.
- [ ] Recommended deal terms map to the identified risk tier.
- [ ] Sector-regulator approvals and foreign-investment screening checked separately from merger control, each with its own timeline `[VERIFY]`.
- [ ] Clean-team and interim-covenant review completed before any integration planning is shared.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Stating HSR or foreign thresholds from memory | They are adjusted periodically; mark every figure `[VERIFY]` and cite the source used |
| "No overlap, no issue" | Check vertical, potential-competition, and labor-market theories even without a horizontal overlap |
| Accepting the parties' preferred broad market | Present the narrower market the agencies may test and the evidence that decides it |
| Treating combined share alone as the answer | Add closeness of competition, entry conditions, and ordinary-course documents |
| Recommending "clean up" of hot documents | Existing documents are preserved and produced as required; advise only on future drafting |
| Promising a timeline | Give scenarios with drivers; review length depends on agency decisions |
| Treating a below-threshold deal as immune | Non-reportable deals can still be investigated and challenged; assess substance regardless of filing status `[VERIFY]` |
| Pre-closing integration that transfers control | Check interim covenants and integration plans for gun-jumping before signing |

## Example

**Input (abridged):** Fictional Brightline Analytics (buyer) acquiring all voting securities of Kestrel Metrics (target), both US-based; each sells workflow analytics software to regional hospitals. Parties estimate a combined 30% share from an industry report. A buyer board deck says the deal "takes our most aggressive price competitor off the table." Target has EU customers.

**Output (excerpt):**

> **Reportability (US).** Apply size-of-transaction and size-of-person tests to the supplied purchase price and financials `[VERIFY: current thresholds]`. Result pending the target's latest balance sheet `[NEED: target financials]`. **EU:** turnover test cannot be run without EU revenue by party `[NEED]`; screen national regimes too `[VERIFY]`.
>
> **Unilateral effects — Tier: high.** The board-deck statement is direct evidence of closeness of competition and will be produced with the filing if it is a transaction-related document `[VERIFY: filing document requirements]`. Evidence against: two larger national vendors reportedly win most large-system bids `[NEED: win/loss data]`.
>
> **Deal terms.** Given a high-tier theory, recommend an outside date with extension for an extended review, a reverse termination fee sized to the risk, and a clear divestiture limit in the efforts covenant.
