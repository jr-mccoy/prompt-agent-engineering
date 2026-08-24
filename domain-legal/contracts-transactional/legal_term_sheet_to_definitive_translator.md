---
title: "Term Sheet to Definitive Documents Translator"
category: legal/contracts-transactional
description: "Convert a signed or near-final term sheet into a structured first-draft set of definitive agreements with explicit open-issue tracking, identified silences requiring resolution, and a definitive-doc-by-doc roadmap."
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
  - contracts
  - term-sheet
  - definitive-documents
  - open-issues
  - drafting
updated: "2026-05-11"
related_prompts:
  - domain-legal/contracts-transactional/legal_msa_drafter.md
  - domain-legal/contracts-transactional/legal_licensing_agreement_drafter.md
  - domain-legal/contracts-transactional/legal_negotiation_position_paper.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Take a term sheet (LOI, MOU, summary of terms) and translate it into a structured first draft of definitive documents — identifying which definitive documents are needed, mapping each term-sheet provision to the right document and section, surfacing **silences** (issues the term sheet did not address but the definitive must), and producing an open-issue list with proposed resolutions for each. This is the bridge between deal handshake and signing.

**When to use:** Right after term-sheet signature, before definitive drafting begins; mid-stream when a definitive draft is bogging down and the team needs to re-map back to term-sheet commitments; quality control after definitives are drafted to confirm fidelity. Use the specific document drafters (MSA, License, SaaS) for the actual definitive drafting.

---

## Your Input

- **Term sheet:** [Paste full text]
- **Term-sheet status:** [Signed / unsigned / under negotiation / non-binding letter of intent]
- **Deal type:** [Acquisition (asset / stock / merger) / financing / licensing / joint venture / commercial supply / partnership / other]
- **Parties:** [Names and roles]
- **Governing law (if specified):** [State]
- **Posture:** [Buyer / Seller / Investor / Issuer / Licensor / Licensee / etc.]
- **Definitive documents anticipated:** [Purchase agreement / SPA / APA / merger agreement / disclosure schedules / employment agreements / lease assignments / IP assignments / SAFE / Note / SHA / etc. — list what you expect]
- **Closing timeline target:** [Sign date target; close date target]
- **Conditions to closing already identified:** [Regulatory approvals, financing, third-party consents, no-MAC, employee retention]
- **Open issues already flagged:** [If any]
- **Internal positions on silences:** [If the team has pre-decided fallbacks]

---

## Constraints

**Must:**
- Read the term sheet as the **binding (or non-binding) record of agreed terms** — definitives must give effect to it; deviations are open issues.
- Produce a **document-by-document map**: for each definitive document, list which term-sheet provisions belong in it.
- For each term-sheet provision, identify **what additional drafting is needed** to make it operative (e.g., "TS says 'subject to standard reps and warranties' — definitive needs full reps and warranties package with knowledge qualifiers, materiality, survival, and disclosure-schedule references").
- Surface **silences** — issues the term sheet did not address that the definitive must address:
  - Reps and warranties scope and survival
  - Indemnification baskets, caps, survival, escrow, sole-remedy framing
  - MAC / Material Adverse Change definition and exceptions
  - Disclosure schedules structure
  - Tax treatment and allocation
  - Restrictive covenants (non-compete, non-solicit) — duration and geography
  - Employment matters (which employees, terms)
  - IP assignment mechanics
  - Working capital adjustment
  - Earn-out mechanics (if applicable) — milestones, measurement, dispute resolution
  - Indemnification escrow mechanics
  - Closing conditions and termination rights
  - Governing law / venue / dispute resolution
  - Confidentiality / publicity
  - Expense allocation
- Produce an **open-issue list** with: issue, term-sheet text (if any), proposed resolution, owner, decision deadline, dependency.
- Identify **enforceability of binding vs non-binding provisions** of the term sheet (typical: exclusivity, confidentiality, fees, governing law are binding; rest is not).
- Identify **conditions precedent to closing** implied or stated.
- Identify **diligence items** required to validate or refine term-sheet assumptions.

**Must Not:**
- Treat the term sheet as the definitive — translation requires expansion, not transcription.
- Invent terms not in the term sheet and not flagged as silences. Use `[NEED: ...]` for items requiring client decision.
- Ignore the binding/non-binding distinction — drafting must respect what was actually agreed.
- Conflate one definitive document with another (e.g., putting employment terms in the SPA when they belong in employment agreements).
- Use generic disclaimers.
- Invent statutory or regulatory provisions. Use `[CITE: ...]`.

---

## Open-Issue Metadata Schema

Every open issue gets a structured entry:

| Field | Values / Format |
|---|---|
| Issue ID | OI-001, OI-002, ... |
| Document | SPA / DPA / Employment / Other |
| Term-sheet provision | Section reference + quoted text, or "Silence" |
| Issue type | Silence / Ambiguity / Inconsistency / Diligence-dependent / Drafting decision |
| Severity | Critical (closing-blocker) / High / Medium / Low |
| Proposed resolution | Specific drafting proposal |
| Fallback | Alternative if primary is rejected |
| Walkaway | Position we won't go below |
| Owner | Deal lead / GC / CFO / Tax / IP / etc. |
| Decision deadline | Date or milestone |
| Dependency | Other issue, diligence finding, third-party consent |

---

## Instructions

1. **Parse the term sheet.** Identify every operative provision. Tag each as binding or non-binding.
2. **Identify definitive document set.** Based on deal type, list which definitives will be drafted. Cross-check user input.
3. **Map provisions to documents.** For each term-sheet provision, identify the document(s) it belongs in and the section(s) within.
4. **Identify drafting expansions.** For each provision, what additional drafting is needed to make it operative? (Examples: "Reps and warranties — full list; survival; materiality and knowledge qualifiers; sandbagging treatment.")
5. **Surface silences.** Walk through the silence checklist above; flag every silence the deal requires resolving.
6. **Build the open-issue list.** Each entry uses the metadata schema.
7. **Identify conditions precedent.** What must happen between signing and closing.
8. **Identify diligence items.** What needs to be confirmed to refine term-sheet assumptions.
9. **Draft skeleton definitives.** For each definitive document, produce a section outline with term-sheet-derived content + `[NEED: ...]` placeholders for open issues.
10. **Surface inconsistencies.** Where two term-sheet provisions appear inconsistent, flag and propose resolution.
11. **Identify the critical path.** Which open issues must resolve first to unblock drafting.

---

## Output Format

```markdown
# Term Sheet to Definitive Documents — {Deal Name}
**Deal Type:** {type}  |  **Posture:** {posture}  |  **Governing Law:** {state}  |  **Date:** {YYYY-MM-DD}

## 1. Executive Summary
- Definitive documents required: {list}
- Open issues: Critical {count} / High {count} / Medium {count} / Low {count}
- Critical-path items: {top 3–5 issues blocking drafting}
- Estimated time to first definitive drafts: {weeks}

## 2. Term Sheet Parse
| TS § | Provision | Binding? | Document(s) | Status |
|---|---|---|---|---|
| 1 | Purchase price: $X | Non-binding | SPA § 2 | Mapped |
| 2 | Exclusivity 60 days | Binding | Standalone — in effect | N/A |
| 3 | Confidentiality | Binding | Existing NDA controls | N/A |
| 4 | Reps and warranties | Non-binding | SPA § 4 | Needs expansion (see OI-003) |
| ... | | | | |

## 3. Document-by-Document Map

### Document 1: Stock Purchase Agreement (SPA)
**Term-sheet provisions in this document:**
- TS § 1: Purchase price
- TS § 4: Reps and warranties
- TS § 5: Indemnification
- TS § 6: Closing conditions

**Required drafting expansions:**
- Purchase price mechanics: payment timing, escrow allocation, working capital adjustment formula
- Reps and warranties: full schedule of reps (corporate, financial, operational, regulatory, employment, IP, tax, environmental, litigation); materiality and knowledge qualifiers; survival periods; disclosure-schedule references
- Indemnification: baskets (deductible vs first-dollar), caps (general / fundamental / fraud), survival, escrow mechanics, sole remedy, exclusive forum, sandbagging
- Closing conditions: HSR / regulatory, no-MAC, no-injunction, accuracy of reps (bring-down), performance of covenants, third-party consents

**Silences requiring resolution:**
- {OI-001} Disclosure schedule format
- {OI-002} Tax allocation methodology (asset deal) / §338(h)(10) election (stock deal)
- {OI-003} Restrictive covenants on sellers (non-compete duration and geography)
- ...

### Document 2: Disclosure Schedules
{...}

### Document 3: Employment Agreements
{...}

## 4. Open-Issue List

### OI-001 — Disclosure Schedule Format and Cross-Referencing
- **Document:** SPA + Disclosure Schedules
- **TS Provision:** Silence
- **Issue Type:** Silence
- **Severity:** Medium
- **Proposed Resolution:** Schedules organized to track section numbers of representations and warranties; cross-reference table at front; "general" vs "specific" disclosures clarified per buyer-favorable convention; carve-back for items disclosed against multiple representations.
- **Fallback:** Specific disclosures only against the rep cited; no cross-application.
- **Owner:** Lead counsel
- **Decision Deadline:** Before reps draft circulated
- **Dependency:** None

### OI-002 — Materiality and Knowledge Qualifiers in Reps
- **Document:** SPA § 4
- **TS Provision:** "Standard reps and warranties" (TS § 4)
- **Issue Type:** Silence / Drafting decision
- **Severity:** High
- **Proposed Resolution:** {Posture-driven: buyer prefers limited qualifiers; seller prefers broad. Recommend approach with rationale.}
- **Fallback:** {...}
- **Walkaway:** {...}
- **Owner:** Deal counsel + buyer rep
- **Decision Deadline:** Before reps draft circulated
- **Dependency:** Diligence findings on financial controls (qualifies "to seller's knowledge" framing)

### OI-003 — Indemnification Basket and Cap
- **Document:** SPA § 5
- **TS Provision:** "Indemnification subject to standard basket and cap" (TS § 5)
- **Issue Type:** Ambiguity
- **Severity:** Critical
- **Proposed Resolution:** Basket: 0.5% of purchase price, deductible (not first-dollar); General cap: 10% of purchase price for general reps; Fundamental cap: 100% for fundamental reps (authority, capitalization, taxes); Survival: 18 months general, 6 years fundamental, statute of limitations for tax and fraud.
- **Fallback:** Basket 1% first-dollar; cap 15%.
- **Walkaway:** No basket / no cap.
- **Owner:** Deal lead + CFO
- **Decision Deadline:** Before SPA draft circulated
- **Dependency:** RWI quote (if applicable)

{... continue through all open issues ...}

## 5. Conditions to Closing
| CP | Type | Owner | Timeline | Open Items |
|---|---|---|---|---|
| HSR clearance | Regulatory | Outside counsel | 30 days post-signing | Filing prep |
| No-MAC | Operational | Buyer | At closing | MAC definition |
| Third-party consents | Operational | Seller | Per closing deliverables | List required |
| ... | | | | |

## 6. Diligence Items Required to Refine TS Assumptions
- {Item} — affects {provision/section}; due by {date}
- ...

## 7. Inconsistencies in the Term Sheet
- {TS § X} says ... but {TS § Y} says ...; proposed resolution: ...

## 8. Critical Path
1. Resolve OI-003 (indemnification basket/cap) — blocks SPA drafting
2. Resolve OI-002 (materiality qualifiers) — blocks reps
3. Confirm OI-007 (restrictive covenants on sellers) — blocks employment agreements
{...}

## 9. Skeleton Definitive Outlines

### 9.1 SPA Outline
1. Definitions [NEED: confirm based on TS § 1 + diligence]
2. Purchase and Sale [TS § 1]
3. Closing [TS § 6]
4. Representations and Warranties [TS § 4 + OI-002 resolution]
5. Covenants [Silence — see OI-008]
6. Conditions to Closing [TS § 6 + standard set]
7. Indemnification [TS § 5 + OI-003 resolution]
8. Termination [Silence — see OI-009]
9. Miscellaneous

### 9.2 Disclosure Schedule Outline
{...}
```

---

## Verification

- [ ] Every term-sheet provision is mapped to at least one definitive document.
- [ ] Binding vs non-binding status of each term-sheet provision is identified.
- [ ] Silence checklist walked through; every applicable silence is flagged as an open issue.
- [ ] Each open issue has the full metadata schema completed (or `[NEED: ...]` flag).
- [ ] Conditions to closing identified, with owner and timeline.
- [ ] Diligence items linked to term-sheet provisions they affect.
- [ ] Inconsistencies in the term sheet flagged with proposed resolution.
- [ ] Critical path identifies blocking issues for drafting.
- [ ] No invented terms; placeholders for missing inputs.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Treating "standard reps and warranties" in a TS as a complete instruction | TS shorthand requires full expansion; reps schedule must be drafted with materiality/knowledge/survival decisions |
| Ignoring the binding/non-binding split in the TS | Always identify which TS provisions survive as enforceable (typically exclusivity, confidentiality, fees, governing law) and which are non-binding deal points |
| Putting employment terms in the SPA | Employment terms belong in employment agreements; SPA may reference but not embed |
| Treating indemnification basket and cap as "to be determined" without proposing | OI entry must include proposed resolution, fallback, and walkaway — not just a placeholder |
| Missing the disclosure-schedule structural decision | "General" vs "specific" disclosure conventions are critical and often a silence; flag and resolve |
| Failing to address tax structure decisions (§ 338(h)(10), asset vs stock allocation) | Tax structure is often a silence requiring tax counsel input; surface it |
| Treating MAC as drafting boilerplate | MAC definition is heavily negotiated; surface exceptions, knowledge qualifiers, and look-forward language as open issues |
| Omitting earn-out mechanics flag | If TS mentions earn-out, definitives must include milestones, measurement, dispute resolution, accounting standards, acceleration triggers — all silences typically |
| Forgetting working-capital adjustment in cash deals | If TS mentions purchase price without working-capital mechanic, flag — most cash deals include WC true-up |
| Generic "consult counsel" disclaimers | This prompt is the bridge to definitives; specific drafting guidance is the output |
| Missing exclusivity expiration tracking | If TS binding exclusivity is in effect, surface its expiration date prominently |
| RWI / R&W insurance interplay not flagged | If applicable, RWI quote and conditions affect basket, cap, survival, and seller indemnity scope; surface as open issue |
