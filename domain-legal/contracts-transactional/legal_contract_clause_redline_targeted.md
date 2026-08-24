---
title: "Targeted Clause Redline — Indemnity, LoL, IP, Warranties, Termination"
category: legal/contracts-transactional
description: "Focused redline pass on the five highest-risk clause families: indemnification, limitation of liability, IP ownership, warranties, and termination. Produces clause-by-clause markup with primary, fallback, and walkaway positions calibrated to posture."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - contracts
  - indemnity
  - limitation-of-liability
  - ip-ownership
  - termination
updated: "2026-05-11"
related_prompts:
  - domain-legal/contracts-transactional/legal_contract_review_full_redline.md
  - domain-legal/contracts-transactional/legal_contract_risk_heatmap.md
  - domain-legal/contracts-transactional/legal_negotiation_position_paper.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Run a deep, surgical redline on the five clause families that dominate risk allocation: indemnification, limitation of liability (LoL), IP ownership and licenses, warranties (including disclaimers), and term/termination. Output is clause-specific markup plus a position ladder (primary / fallback / walkaway) for each.

**When to use:** Counterparty paper has been accepted at the framework level; the negotiation now concentrates on these five clusters. Also use as a sanity check before signing when full review is not feasible.

---

## Your Input

- **Operative clauses:** [Paste § indemnification, § LoL, § IP/license, § warranties + disclaimers, § term/termination — verbatim]
- **Defined terms used in those clauses:** [Paste relevant definitions]
- **Contract type:** [Services / SaaS / License / Reseller / Other]
- **Governing law:** [State and country]
- **Posture:** [Customer/Licensee OR Supplier/Licensor]
- **Deal economics:** [Annual fees, total contract value, payment terms — needed for LoL cap calibration]
- **Data and IP profile:** [Counterparty access to PII/PHI; counterparty contribution to deliverables; pre-existing IP at risk]
- **Insurance carried:** [Type and limits — affects LoL cap reasonableness]
- **Regulatory overlay:** [HIPAA, GDPR, sector-specific]
- **Internal playbook positions (if any):** [Paste; otherwise use reasonable posture-aligned defaults]

---

## Constraints

**Must:**
- Treat each clause family as an interlocking system; LoL caps interact with indemnity carve-outs; termination triggers interact with warranty cures.
- For each clause, output a **position ladder**: Primary (opener), Fallback (round 2), Walkaway (do-not-sign).
- For indemnity, separately address: (i) trigger (third-party claim only, or also direct losses), (ii) scope (IP, confidentiality breach, data breach, bodily injury / property damage, breach of law, breach of representations), (iii) procedure (notice, control of defense, cooperation, settlement consent), (iv) exclusions.
- For LoL, separately address: (i) cap amount and reference period, (ii) cap type (aggregate / per-claim), (iii) carve-outs from the cap, (iv) exclusion of indirect/consequential damages, (v) carve-outs from the consequential exclusion (data breach, IP, confidentiality, gross negligence/willful misconduct, indemnity obligations, payment obligations).
- For IP, separately address: (i) ownership of background IP, (ii) ownership of foreground/deliverables, (iii) license grants (scope, exclusivity, sublicensability, irrevocability, transferability), (iv) feedback license, (v) residuals clause, (vi) open-source treatment.
- For warranties, separately address: (i) express warranties and remedies, (ii) implied warranty disclaimers and their enforceability under governing law, (iii) anti-sandbagging vs pro-sandbagging, (iv) knowledge qualifiers, (v) survival.
- For termination, separately address: (i) term and renewal mechanic, (ii) termination for convenience, (iii) termination for cause (material breach + cure), (iv) termination for insolvency / change of control, (v) effects of termination (transition services, data return, license survival, fee true-up), (vi) survival schedule.
- Cite section numbers in every comment.
- Use the redline notation in the convention section below.

**Must Not:**
- Invent statutes, case citations, or regulatory provisions. Use `[CITE: ...]`.
- Insert facts not provided. Use `[NEED: ...]` placeholders.
- Apply identical markup to indemnitor and indemnitee. Posture changes everything.
- Suggest "mutual" markup as a default without considering whether mutual creates real reciprocity or only the appearance.
- Use generic disclaimers about needing counsel.
- Treat unlimited liability and uncapped indemnity as drafting style — they are the deal.

---

## Redline Notation Convention

- **Insertions:** `{+inserted text+}`
- **Deletions:** `{-deleted text-}`
- **Position-ladder anchors:** `[P]` primary, `[F]` fallback, `[W]` walkaway, attached to the rationale entry.
- **Cross-clause dependencies:** `[X-REF § __]` when one clause's markup depends on another.

---

## Instructions

1. **Read all five clauses together** before drafting any markup. Note interdependencies (e.g., LoL carve-out for IP indemnity is meaningless if the IP indemnity itself is gutted).
2. **Indemnification.** Build a matrix: covered events × indemnitor × indemnitee × procedure × carve-outs from LoL. Markup to reach posture-aligned position.
3. **Limitation of Liability.** Compute the cap as a multiple/fraction of fees. Identify and markup carve-outs. Confirm the consequential-damages exclusion has the right carve-backs.
4. **IP Ownership and License.** Identify each IP bucket (background, foreground, deliverables, feedback, residuals). Set ownership; set license scope, exclusivity, perpetuity, sublicensability, transferability.
5. **Warranties.** List express warranties; review disclaimer of implied warranties for governing-law enforceability (e.g., UCC §§ 2-314, 2-315, magnuson-moss for consumer goods). Add or remove knowledge qualifiers per posture. Set survival period.
6. **Term and Termination.** Build the lifecycle: effective date → initial term → renewal → termination triggers → cure → effects → survival. Confirm each termination right has matched effects (e.g., termination for cause by customer = fee refund; termination for convenience = wind-down fees).
7. **Cross-check.** Re-read the five clauses together with the markup applied. Confirm no contradictions; confirm carve-outs are reciprocal where required.
8. **Generate the position ladder** for each clause: primary opener, defensible fallback, walkaway threshold.
9. **Output** the redlined clauses, the position ladder, and a top-of-document summary.

---

## Output Format

```markdown
# Targeted Clause Redline — {Contract Title}
**Posture:** {Buyer/Supplier}  |  **Governing Law:** {state}  |  **Date:** {YYYY-MM-DD}

## Summary
- Worst clause as drafted: {clause name}
- Strongest dependency: {e.g., "LoL carve-out for IP indemnity is the linchpin"}
- Recommended sequencing in negotiation: {order to push}

## 1. Indemnification (§ __)
### Markup
{+/- redlined text+}
### Position Ladder
- **[P] Primary:** {description + key terms}
- **[F] Fallback:** {what we will concede}
- **[W] Walkaway:** {what we will not accept}
### Rationale
{2–4 sentences tied to posture and risk profile}

## 2. Limitation of Liability (§ __)
### Markup
{+/- redlined text+}
### Cap Computation
- Proposed cap: {amount or multiple of fees} | Period: {12 months prior / total fees / TCV}
- Carve-outs from cap: {list}
- Carve-backs from consequential exclusion: {list}
### Position Ladder
[P] / [F] / [W]
### Rationale
{...}

## 3. IP Ownership and License (§ __)
### Markup
{+/- redlined text+}
### Ownership Matrix
| Bucket | Owner | License granted | Scope | Survival |
|---|---|---|---|---|
| Background IP | | | | |
| Foreground IP / Deliverables | | | | |
| Feedback | | | | |
| Residuals | | | | |
### Position Ladder
[P] / [F] / [W]
### Rationale
{...}

## 4. Warranties and Disclaimers (§ __)
### Markup
{+/- redlined text+}
### Warranty Schedule
| Warranty | Knowledge qualifier | Survival | Remedy |
|---|---|---|---|
| | | | |
### Position Ladder
[P] / [F] / [W]
### Rationale
{...}

## 5. Term and Termination (§ __)
### Markup
{+/- redlined text+}
### Lifecycle
- Initial term: __ | Renewal: __ | Non-renewal notice: __
- Termination for cause: __ cure period
- Termination for convenience: {yes/no/which party}
- Effects: {transition services, data return, license survival, fee true-up}
- Survival list: {sections that survive}
### Position Ladder
[P] / [F] / [W]
### Rationale
{...}

## Cross-Clause Dependencies
- {LoL § __ ↔ Indemnity § __: ...}
- {Warranty § __ ↔ Termination § __: ...}
```

---

## Verification

- [ ] All five clause families covered with markup and position ladder.
- [ ] LoL cap and carve-outs computed against actual deal economics.
- [ ] Indemnity carve-outs from LoL match indemnity scope (no orphan carve-outs).
- [ ] Each warranty has a knowledge qualifier decision and a survival period.
- [ ] Termination effects match each termination trigger (cause vs convenience vs insolvency).
- [ ] IP ownership matrix covers background, foreground, feedback, residuals.
- [ ] No invented citations or facts; placeholders used.
- [ ] Cross-clause dependencies surfaced.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Reciprocal "mutual" indemnity that protects neither party because the risk is one-sided | Make the indemnity asymmetric where the risk profile is asymmetric (e.g., customer rarely indemnifies vendor for IP infringement unless customer-supplied materials) |
| LoL cap at "fees paid" without clarifying period | Specify "fees paid or payable in the 12 months preceding the claim" and confirm it is aggregate, not per-claim |
| Carving data breach out of LoL but not out of the consequential-damages exclusion | Both carve-outs are needed; consequential exclusion swallows the cap-carveout otherwise |
| Knowledge qualifier on every warranty | Knowledge qualifiers belong on third-party-conduct or unknowable representations; not on the basic ones (authority, organization, no conflicts) |
| Pro-sandbagging clause in a state where common-law sandbagging is unsettled | Add an express pro- or anti-sandbagging clause; do not rely on background law |
| Termination for convenience with no wind-down fees in a long-term services contract | Supplier should require wind-down fees; customer should preserve TFC right but accept reasonable wind-down |
| Survival clause that survives "all obligations indefinitely" | Survival should be a list of sections with defined survival periods; indefinite survival of payment obligations is fine, indefinite survival of warranties is not |
| Confusing IP assignment with IP license | Deliverables can be assigned OR licensed; pick one and be explicit. Background IP almost always licensed, never assigned |
| Treating "as-is" disclaimer as effective in a jurisdiction that won't enforce it for negligence or consumer claims | Verify enforceability under governing law; UCC and consumer-protection statutes constrain |
| Residuals clause accepted blindly on customer side | Residuals clauses gut confidentiality protection for trade secrets in memory; customer should reject or narrowly scope |
