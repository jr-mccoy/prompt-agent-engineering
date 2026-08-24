---
title: "Full Contract Review with Risk-Tiered Redline"
category: legal/contracts-transactional
description: "Conduct a full review of a third-party paper contract; produce a redlined version, a clean version with accepted changes, and an issues memo with severity-tiered comments calibrated to the reviewer's posture (buyer or supplier)."
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
  - redline
  - review
  - risk-allocation
  - playbook
updated: "2026-05-11"
related_prompts:
  - domain-legal/contracts-transactional/legal_contract_clause_redline_targeted.md
  - domain-legal/contracts-transactional/legal_contract_risk_heatmap.md
  - domain-legal/contracts-transactional/legal_negotiation_position_paper.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Convert a third-party contract draft into three deliverables — a tracked-changes redline, a clean accepted version, and an issues memo — with comments and changes calibrated to the user's posture (buyer/customer or supplier/vendor), governing law, and any internal playbook supplied.

**When to use:** First-pass or final-pass review of an inbound contract draft (MSA, SaaS, services, license, NDA) where the counterparty supplied the form. Use the targeted clause redline prompt when scope is narrower; use the heatmap when the goal is triage rather than markup.

---

## Your Input

- **Contract document:** [Paste full text or attach]
- **Contract type:** [MSA / SOW / SaaS / License / NDA / Reseller / Other]
- **Governing law specified in draft:** [State + country, or "silent"]
- **Posture:** [Buyer/Customer/Licensee OR Supplier/Vendor/Licensor]
- **Deal value and term:** [Annual contract value, total contract value, initial term, renewal mechanic]
- **Counterparty leverage:** [High / equal / low — affects fallback aggressiveness]
- **Internal playbook or standards:** [Paste relevant sections, or "none supplied — use reasonable market positions for posture"]
- **Industry / regulatory overlay:** [HIPAA, GLBA, GDPR, FedRAMP, PCI-DSS, ITAR, etc., or "none"]
- **Known dealbreakers:** [Issues already flagged by business as must-fix]
- **Data flows:** [Will counterparty process PII / PHI / regulated data? At what volume?]
- **Time/sign target:** [If urgency drives must-have vs nice-to-have triage]

---

## Constraints

**Must:**
- Read the full document before commenting; cross-references and definitions affect downstream interpretation.
- Tag every comment with a **severity tier**: Critical / High / Medium / Low (defined below).
- Tag every comment with a **posture rationale**: why this matters from the reviewer's side of the table.
- For each material change, provide both a **markup** (redline text) and a **comment** explaining the change and the fallback if rejected.
- Distinguish **legal risk** (enforceability, regulatory non-compliance, indemnity gaps) from **commercial risk** (price, term length, exit cost) — both go in the memo but legal risk gets primary attention.
- Identify **missing provisions** the draft omits that the reviewer's posture requires (e.g., audit rights for a customer; cap on indemnity for a supplier).
- Cite the operative section number when commenting (e.g., "§ 8.2(b)(ii)").
- Reconcile defined terms — flag every use of an undefined capitalized term or a defined term used inconsistently.

**Must Not:**
- Invent statutes, case citations, or regulatory provisions. Use `[CITE: ...]` if a citation slot is needed.
- Insert contract terms not supplied by the user as if they were in the draft. Use `[NEED: ...]` for assumptions.
- Apply a generic "balanced" markup when posture is specified — markup must serve the reviewer.
- Redline stylistic preferences unless they create ambiguity. Track only substantive changes.
- Re-paper sections that are already acceptable; over-redlining destroys credibility and lengthens negotiations.
- Treat every supplier-friendly clause as a problem — some are market and should be accepted with a noted concession.
- Use generic disclaimer language ("consult an attorney"). The output is the work product.

---

## Severity Tiers

| Tier | Definition | Examples |
|---|---|---|
| **Critical** | Dealbreaker. Sign-as-is creates material legal, regulatory, or financial exposure. Escalate before signing. | Uncapped indemnity, no LoL cap, IP assignment of pre-existing IP, no termination for convenience where required, missing DPA/SCCs for EU data |
| **High** | Strong push. Defensible fallback exists but primary position should be held in early rounds. | LoL cap below 1× fees, one-way indemnity, auto-renewal without notice window, broad MFN, unbounded audit rights |
| **Medium** | Negotiate if leverage allows. Accept with comment if traded for higher-tier wins. | 30-day vs 60-day cure, governing law in counterparty's home state, narrow force majeure, asymmetric notice provisions |
| **Low** | Note only. Do not block signature. | Defined-term inconsistencies, stylistic ambiguity, optional clarifying language |

---

## Redline Notation Convention

- **Insertions:** `{+inserted text+}`
- **Deletions:** `{-deleted text-}`
- **Comment anchors:** `[C1]`, `[C2]`, ... numbered sequentially; full comment in the issues memo.
- **Open issues for client decision:** `[OPEN: ...]` inline plus an entry in the open-issues list.

---

## Instructions

1. **Index pass.** Build a section map: numbered sections, defined terms, schedules, exhibits, and incorporated documents. Flag every incorporated-by-reference document not supplied.
2. **Risk allocation pass.** Identify the spine: indemnification, limitation of liability, warranties, IP ownership, confidentiality, term/termination, data protection. Score each against posture.
3. **Operational pass.** Payment terms, acceptance, SLAs/service credits, change-order mechanics, audit, reporting, sub-processor approval, insurance.
4. **Compliance pass.** Regulatory overlays from input (HIPAA BAA, GDPR DPA + SCCs, PCI, export controls, sanctions, anti-corruption). Note required addenda.
5. **Boilerplate pass.** Governing law, venue/forum, jury waiver, dispute resolution (negotiation/mediation/arbitration), assignment, no-waiver, severability, integration, counterparts, electronic signature, notice provisions, force majeure, third-party beneficiaries.
6. **Definitions reconciliation.** Every defined term used; every used capitalized term defined; no circular or conflicting definitions.
7. **Schedule and exhibit pass.** Verify every referenced schedule exists and is consistent with the main body.
8. **Generate the redline** with `{+...+}` / `{-...-}` markup and `[C#]` anchors.
9. **Generate the clean version** with all proposed changes accepted (for negotiation-internal use).
10. **Write the issues memo** with one entry per `[C#]` anchor: section, tier, current text, proposed text, rationale, fallback, walkaway threshold.
11. **Add the open-issues list** for business decisions (price, term, scope) not legal in nature.

---

## Output Format

```markdown
# Contract Review — {Contract Title}
**Reviewer Posture:** {Buyer/Supplier}  |  **Governing Law:** {state}  |  **Date:** {YYYY-MM-DD}

## 1. Executive Summary
- Recommended action: {Sign / Sign with negotiated changes / Do not sign as drafted}
- Critical issues: {count}; High: {count}; Medium: {count}; Low: {count}
- Key escalations for business: {bullet list}

## 2. Issues Memo

### [C1] § {section} — {Issue title}  |  Tier: Critical
- **Current text:** "{quote}"
- **Why it matters (posture-specific):** {1–3 sentences}
- **Proposed markup:** "{redlined text}"
- **Fallback position:** {first concession}
- **Walkaway:** {what we will not accept}

### [C2] § {section} — {Issue title}  |  Tier: High
{same structure}

{... continue through all comments, ordered by tier then section ...}

## 3. Missing Provisions
- {Provision name} — required because {posture/regulatory reason}; proposed insertion at § {location}: "{text}"

## 4. Open Issues for Business
- {Issue} — needs {decision-maker} input by {date}.

## 5. Redline (Excerpt)
{Inline {+...+} / {-...-} markup of the most material changed sections, with [C#] anchors}

## 6. Clean Accepted Version
{Full text with all proposed changes accepted, for internal preview}
```

---

## Verification

- [ ] Every comment has a severity tier and a posture-grounded rationale.
- [ ] Every material change appears in both the redline and the issues memo.
- [ ] Defined terms reconciled across the document.
- [ ] Regulatory overlays from input addressed (DPA, BAA, etc.) or affirmatively noted as not required.
- [ ] No invented citations or contract language. Placeholders used where data was missing.
- [ ] Indemnity, LoL, IP, warranties, termination, and confidentiality all addressed at minimum.
- [ ] Open-issues list separates legal from commercial decisions.
- [ ] Recommended action stated up front, not buried.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Redlining stylistic preferences and creating an 80-comment markup | Cut to substantive changes only; stylistic notes go in a separate "non-blocking" appendix |
| Applying a "neutral" markup when posture is buyer or supplier | Re-run the risk allocation pass from the reviewer's side; clauses are asymmetric by design |
| Treating an uncapped indemnity as routine | Always Critical for the indemnifying party unless reciprocal and capped, or carved to a specific narrow risk |
| Accepting LoL cap = fees paid in prior 12 months without checking termination interplay | Verify cap survives termination and applies to the relevant claim types; data-breach and IP indemnity often carve out |
| Missing the DPA / SCCs requirement on a contract touching EU personal data | Always check data flows in input; flag missing DPA as Critical when GDPR applies |
| Accepting auto-renewal without notice mechanics | Require a specific notice window (e.g., 60 days) and a non-renewal mechanism that does not require board action |
| Flagging governing law in counterparty state as Critical | This is rarely Critical for buyer with leverage; Medium absent regulatory or enforcement concerns |
| Inventing market terms ("industry standard is X") without basis | Anchor to specific clause language, not unattributed "market" claims |
| Conflating warranty with indemnity in the comments | Warranty = promise (basis for breach); indemnity = defense/payment obligation. Keep separate |
| Redlining schedules without reviewing the main body's incorporation language | Schedules often incorporate by reference and inherit defined terms — review together |
