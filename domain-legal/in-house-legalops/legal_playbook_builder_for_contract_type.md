---
title: "Contract Playbook Builder (Primary / Fallback / Walkaway)"
category: legal/in-house-legalops
description: "Build a clause-by-clause negotiation playbook for one contract type (MSA, vendor agreement, NDA, DPA, etc.) with primary / fallback / walkaway positions, rationale, market-standard reference, counterparty-leverage adjustment, and escalation triggers — calibrated to the company's posture (buyer vs supplier) and risk appetite."
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
  - in-house
  - contracts
  - playbook
  - negotiation
updated: "2026-05-11"
related_prompts:
  - domain-legal/in-house-legalops/legal_legal_intake_triage_router.md
  - domain-legal/in-house-legalops/legal_legal_spend_anomaly_analyzer.md
  - domain-legal/contracts-transactional/legal_contract_risk_heatmap.md
---

**Purpose:** Produce a structured, clause-by-clause negotiation playbook for a single contract type. Each clause carries three positions — **primary** (preferred drafting we open with), **fallback** (acceptable concession with rationale and conditions), **walkaway** (red line that requires escalation to senior counsel or the business decision-maker). Output is the reference paralegals, commercial counsel, and procurement use without re-asking the GC every time.

**When to use:** Standing up a contract-review function, refreshing an existing playbook after a market shift or regulatory change, onboarding a new commercial-counsel hire, building a self-service review path for low-risk contracts, calibrating procurement's authority to sign without legal review.

---

## Your Input

- **Contract type:** [MSA / SOW / vendor agreement / reseller / channel / SaaS subscription / mutual NDA / one-way NDA / DPA / BAA / cloud services / professional services / consulting / licensing / employment / contractor / referral / partnership]
- **Company posture:** [Buyer / supplier / mutual; sometimes both — specify]
- **Risk appetite:** [Conservative / standard / aggressive — usually company-set, sometimes deal-size dependent]
- **Deal-size bands (if posture varies):** [e.g., <$50K self-serve; $50K–$500K commercial-counsel; >$500K senior counsel]
- **Industry / regulatory overlay:** [Healthcare/HIPAA, financial services, EU/GDPR data, public sector, defense/ITAR, life sciences — any that change clause defaults]
- **Governing-law preference and forum preference:** [Company's preferred state and dispute mechanism]
- **Known market-standard positions:** [If the user has a market reference — e.g., Tech-GC market data, industry trade-group form, prior internal precedent]
- **Counterparty-leverage scenarios to handle:** [e.g., "Fortune 100 customer with their paper" vs "small vendor on our paper"]
- **Existing form on file (if any):** [Reference for primary positions; otherwise the playbook authors from common market position]
- **Hard escalation triggers (company-set):** [Provisions that always escalate — e.g., uncapped indemnity, IP-assignment of background IP, perpetual term, source-code escrow, MFN clauses]

---

## Constraints

**Must:**
- Cover the **core clause set** for the contract type. For a commercial agreement that typically includes: parties/recitals, scope, term, fees & payment, IP ownership, license grants, confidentiality, data protection, warranties, indemnification, limitation of liability, insurance, termination, post-termination obligations, dispute resolution, governing law, assignment, change orders, force majeure, audit, publicity, anti-corruption, export, modern slavery, sanctions, AI/algorithmic-decision provisions where applicable.
- For each clause provide all three positions:
  - **Primary** — preferred drafting language or a position statement; the opener.
  - **Fallback** — what we will concede, why, and under what conditions.
  - **Walkaway** — the red line; what triggers escalation; who in the org owns the escalation.
- **Tier each clause's risk** using a consistent framework (e.g., COSO/CGMA-style impact × likelihood, or the company's existing risk-tier vocabulary) so reviewers know which clauses matter most.
- **Adjust by counterparty leverage.** Identify which positions shift when the counterparty has structural leverage (large customer on their paper, sole-source vendor, regulated counterparty).
- Identify **escalation triggers**: clauses or combinations that always go to senior counsel regardless of deal size.
- For each fallback, state the **trade or conditions** that make the concession acceptable (e.g., "Mutual indemnity acceptable if liability cap is enforced and IP carveout from cap is bilateral").

**Must Not:**
- Invent statutes, case law, market data, or industry-standard percentages. If the user has not supplied a market reference, frame positions as "common market position" and identify what would falsify that framing.
- Treat the playbook as a substitute for the company's actual outside-counsel review of unusual transactions.
- Provide single-jurisdiction drafting (e.g., Delaware-only language) when the contract is cross-border without flagging the conflict-of-laws gap.
- Embed boilerplate "consult counsel" disclaimers — the playbook IS the institutionalized counsel guidance.
- Authorize self-serve sign-off on clauses the user listed as hard escalation triggers.
- Conflate primary and fallback (the primary is what we open with; the fallback is what we accept under pressure — they must be distinct).

---

## Instructions

1. **Confirm the contract-type scope.** Build the canonical clause list for the type and posture. NDA scope is narrower than MSA scope; DPA has GDPR-mandated articles; BAA has HIPAA-mandated terms.
2. **Set the posture overlay.** Buyer-of-services positions on liability and IP run opposite to supplier-of-services positions; the playbook should make this explicit per clause.
3. **For each clause, build the three positions.**
   - Primary: opening drafting language or position. Annotate why it is the opener (risk reduction, market consistency, internal precedent).
   - Fallback: the line of concession. Identify the trade (what we get in exchange) or condition (what must be true) for the concession.
   - Walkaway: the unacceptable position; the escalation owner; the consequence of crossing the line (escalate / decline deal / require business sign-off with risk acknowledgment).
4. **Assign a clause risk tier.** High / medium / low impact × probability. Drives review priority and self-serve authority.
5. **Counterparty-leverage adjustment.** For each high-risk clause, identify how the positions shift when counterparty leverage is high (large customer, regulated entity, monopoly supplier).
6. **Escalation triggers.** Build a single list of any-deal-size escalation triggers and the escalation owner.
7. **Quick-reference matrix.** A single-screen table so a reviewer can locate primary/fallback/walkaway for a clause in one glance.
8. **Versioning & owner.** Playbook version, effective date, internal owner, review cadence (annual minimum, more often if regulatory shift).

---

## Output Format

```markdown
# {Contract Type} Playbook — {Company} as {Buyer / Supplier / Mutual}

**Version:** {x.y} | **Effective:** {date} | **Owner:** {role} | **Next review:** {date}
**Posture:** {buyer / supplier / mutual}
**Risk appetite:** {conservative / standard / aggressive}
**Self-serve authority:** Deals <${threshold} may close on primary positions only. Any fallback requires {role}. Any walkaway requires {senior role}.

## Hard Escalation Triggers (any deal size)
- {Trigger 1 — e.g., uncapped indemnity in any form}
- {Trigger 2 — e.g., assignment of background IP}
- {Trigger 3 — e.g., MFN / most-favored-customer clauses}
- {Trigger 4 — e.g., perpetual term with no termination for convenience}
- Escalation owner: {role}

## Clause-by-Clause Playbook

### {Clause Name} — Risk Tier: {High/Med/Low}

**Why this clause matters:** {one-sentence business rationale}

**Primary position (opener):**
> {drafting language or position statement}

Rationale: {why this is the opener}.

**Fallback position (acceptable concession):**
> {drafting language or position statement}

Conditions / trade: {what must be true; what we get}.

**Walkaway position (red line):**
- Trigger: {language / scope that we will not accept}
- Escalation owner: {role}
- Consequence: {escalate / decline deal / require business sign-off with risk acknowledgment}

**Counterparty-leverage adjustment:**
- High leverage (e.g., {scenario}): {how positions shift}
- Low leverage (e.g., {scenario}): {how positions shift}

---

{Repeat for each core clause}

## Quick-Reference Matrix

| Clause | Risk Tier | Primary | Fallback | Walkaway |
|---|---|---|---|---|
| {clause} | {H/M/L} | {one-line} | {one-line + trade} | {one-line + escalation owner} |

## Open Questions / Refresh Triggers
- {Provision flagged for refresh — e.g., evolving AI/algorithmic-decision rules}
- {Market shift to monitor}
- {Regulatory item with horizon for re-tier}
```

---

## Verification

- [ ] All core clauses for the contract type are covered.
- [ ] Each clause has distinct primary / fallback / walkaway positions (no collapse into two).
- [ ] Each fallback identifies the trade or condition.
- [ ] Each walkaway names an escalation owner.
- [ ] Risk tiers applied consistently across clauses.
- [ ] Counterparty-leverage adjustments stated for high-tier clauses.
- [ ] Hard escalation triggers listed once at the top.
- [ ] No invented statutes, case law, or market percentages.
- [ ] Quick-reference matrix matches the detailed entries.
- [ ] Version, effective date, owner, and review cadence present.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Primary and fallback are the same position with different wording | Fallback must be a real concession — different scope, different cap, different mutual/unilateral framing |
| Walkaway listed without an escalation owner | Every walkaway requires a named role to escalate to; otherwise reviewer is stuck |
| "Market standard is X%" without a citation | Frame as "common market position" or cite the source; do not invent a number |
| Single set of positions regardless of company being buyer or supplier | Posture flips many clauses (liability, indemnity, IP); restate per posture |
| Including a clause that does not exist in this contract type (e.g., HIPAA terms in a generic NDA) | Build the canonical clause list first; do not pad |
| Self-serve authority extended to escalation-trigger clauses | Hard triggers always escalate regardless of deal size |
| Treating the playbook as legal advice for unusual transactions | Playbook handles routine deals; unusual transactions still escalate |
| Omitting counterparty-leverage adjustment on high-tier clauses | High-tier clauses need leverage adjustment or reviewers will apply primary positions in low-leverage scenarios and lose deals |
| Forgetting jurisdictional / regulatory overlays (GDPR DPA articles, HIPAA BAA terms, public-sector flowdowns) | Overlay terms are mandatory, not negotiable in the same way commercial terms are |
| No versioning or review cadence | Playbooks rot; date them and schedule the refresh |
