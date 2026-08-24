---
title: "Reg BI / Fiduciary-Standard Check — Recommendation Process Review"
category: finance/regulatory-compliance
description: "Review a recommendation or advice process against the four generic obligations of the broker-dealer best-interest standard (disclosure, care, conflict-of-interest, compliance) and the investment-adviser fiduciary duty (duty of care + duty of loyalty) — flagging gaps with no-fabrication and verify-against-current-source guardrails."
techniques:
  - DT-02
  - RT-02
  - CM-02
  - QA-02
  - NE-06
difficulty: intermediate
tags:
  - reg-bi
  - fiduciary
  - suitability
  - best-interest
  - conflicts-of-interest
  - broker-dealer
  - investment-adviser
updated: "2026-06-08"
related_prompts:
  - domain-finance/regulatory-compliance/finance_compliance_gap_analysis.md
  - domain-finance/regulatory-compliance/finance_regulatory_requirement_mapper.md
  - domain-finance/risk-management/finance_operational_risk_rcsa.md
  - domain-finance/field_guide.md
---

**Informational analysis only — not legal or compliance advice. The broker-dealer best-interest standard, the investment-adviser fiduciary standard, related disclosure (e.g., relationship-summary) requirements, and any state-level fiduciary rules change and vary by regulator and account type; confirm all obligations against current official sources (SEC, FINRA, applicable state regulators) and qualified counsel before relying on any output.**

## Objective

Assess whether a firm's recommendation/advice process is structured to meet the applicable conduct standard — the broker-dealer **best-interest** obligations or the investment-adviser **fiduciary** duty (or both, for dually registered firms/accounts) — by walking the process against the recognized obligation pillars and flagging design and evidence gaps. The output is a reviewer's findings register; final adequacy is for compliance/legal counsel.

## When to Use

- Reviewing a new product, recommendation type, or rollover/account-type recommendation process
- Designing or testing supervision/WSP coverage for recommendation conduct
- Pre-exam readiness for conduct-standard obligations
- Remediation after a finding related to disclosure, conflicts, or care obligations
- Mapping how a dually registered model applies the right standard per account/capacity

## Inputs / Context Required

```
<reg_bi_fiduciary_context>
FIRM / CAPACITY:
- Registration(s): broker-dealer, investment adviser, dually registered
- Account types in scope (brokerage, advisory, retirement/rollover)
- Applicable regulator(s) and jurisdiction(s)

RECOMMENDATION PROCESS:
- What is recommended (securities, strategies, account types, rollovers)
- Who is the retail customer/client and how is the profile gathered
- How reasonably-available alternatives are considered and documented
- Cost/comparison analysis performed (if any)
- Disclosures delivered (relationship summary, fees, conflicts) and timing

CONFLICTS:
- Compensation arrangements (commissions, revenue sharing, proprietary products, incentives)
- How conflicts are identified, disclosed, mitigated, or eliminated

SUPERVISION:
- Policies/procedures (WSPs), surveillance, training, documentation/evidence
- Date of review: __________
</reg_bi_fiduciary_context>
```

## Constraints

### Must
- Identify the **applicable standard** for each account/capacity (best-interest vs. fiduciary vs. both) and the **regulator/jurisdiction**.
- Mark any specific rule citation, form name, disclosure-timing requirement, or threshold as **"[verify against current {regulator} text]"** — never assert it as authoritative from memory.
- Assess the broker-dealer best-interest standard against its **four generic obligations**: **Disclosure, Care, Conflict-of-Interest, and Compliance** — framed generically (do not invent sub-paragraph citations).
- Assess the investment-adviser standard against the **fiduciary duty**: **duty of care** and **duty of loyalty** (including full and fair disclosure of material conflicts and informed consent).
- Require **evidence** for any "satisfied" rating — documented profiles, alternatives considered, cost comparisons, disclosures delivered (RT-05); process-on-paper is insufficient.
- Address **rollover/account-type recommendations** specifically (a common high-scrutiny area) where in scope.
- Run an **adversarial self-audit (QA-02 / NE-06)**: which conflicts are disclosed but not mitigated? Where does "best interest"/fiduciary rest on disclosure alone? Which alternatives were not genuinely considered?

### Must Not
- Assert specific rule numbers, form names, or disclosure deadlines as authoritative.
- Conflate suitability with the best-interest/fiduciary standard (the latter is higher and conflict-sensitive).
- Treat disclosure of a conflict as automatically satisfying the conflict obligation.
- Conclude the process "complies" — route final determinations to counsel.

## Instructions

**Step 1 — Determine the applicable standard per capacity (RT-02).**
For each account type/capacity, state which standard governs and why. For dually registered models, confirm the firm applies the correct standard for the capacity in which it acts. Mark citations "[verify against current text]".

**Step 2 — Best-interest four-obligation walk (broker-dealer scope) (DT-02).**

| Obligation (generic) | What to evidence | Status | Gap / finding |
|---|---|---|---|
| Disclosure | Material facts re: relationship, scope, fees, conflicts delivered before/at recommendation [verify timing] | | |
| Care | Reasonable basis (understand product); customer-specific basis (fits profile); series/quantitative basis where applicable; reasonably-available alternatives & costs considered | | |
| Conflict-of-interest | Conflicts identified and **mitigated/eliminated**, not merely disclosed; incentive/sales-contest controls | | |
| Compliance | WSPs, supervision, surveillance, training, recordkeeping reasonably designed to achieve compliance | | |

**Step 3 — Fiduciary duty walk (investment-adviser scope) (RT-02).**

| Duty | What to evidence | Status | Gap / finding |
|---|---|---|---|
| Duty of care | Advice in client's best interest given objectives; reasonable inquiry into profile; best-execution/monitoring as applicable | | |
| Duty of loyalty | Full & fair disclosure of all material conflicts; informed consent; not subordinating client interest | | |

**Step 4 — Conflicts deep-dive.**
Inventory each compensation/incentive conflict. For each: Is it identified? Disclosed (and is disclosure specific enough to be meaningful)? Mitigated or eliminated? Flag any conflict that is disclosed-only where mitigation is expected.

**Step 5 — Rollover / account-type recommendations.**
Where in scope, confirm the process documents the comparison and basis for recommending one account type/rollover over reasonably-available alternatives, including cost.

**Step 6 — Evidence and supervision test (RT-05).**
For a sample recommendation flow, confirm the file evidences: customer profile, alternatives considered, cost comparison, disclosures delivered with timing, and supervisory review. Flag evidence-thin steps.

**Step 7 — Adversarial self-audit (QA-02 / NE-06).**
Answer: Which conflicts are disclosed but not mitigated? Where does the process rely on disclosure to carry the care/loyalty obligation? Which "reasonably available alternatives" were not actually considered? Name the **checkbox-compliance illusion** and require a disconfirming check.

## Output Format

### Standard Determination
| Account/capacity | Standard applied | Regulator/jurisdiction | Correct standard? (verify) |
|---|---|---|---|

### Obligation Findings (Best-Interest and/or Fiduciary)
[Step 2 and/or Step 3 tables]

### Conflicts Register
| Conflict | Identified? | Disclosed (specific?) | Mitigated/Eliminated? | Finding |
|---|---|---|---|---|

### Rollover / Account-Type Findings
| Recommendation | Alternatives documented? | Cost comparison? | Basis documented? | Finding |
|---|---|---|---|---|

### Evidence & Supervision Findings
| Process step | Evidence present? | Finding | Severity |
|---|---|---|---|

### Adversarial Self-Audit
- Disclosed-but-not-mitigated conflicts: …
- Obligations resting on disclosure alone: …
- Alternatives not genuinely considered: …

### Verify-Against-Current Instruction
> Confirm the applicable conduct standard, disclosure content/timing, relationship-summary requirements, and any state fiduciary overlays against current official sources (SEC/FINRA/state) **as of [date]**. Final adequacy determinations route to qualified compliance/legal counsel.

## Verification

- [ ] Applicable standard identified per account/capacity with regulator/jurisdiction.
- [ ] Citations and form/timing requirements marked "[verify against current text]".
- [ ] Best-interest four obligations and/or fiduciary care+loyalty walked with status and findings.
- [ ] Conflicts assessed for identification, disclosure specificity, and mitigation (not disclosure alone).
- [ ] Rollover/account-type recommendations addressed where in scope.
- [ ] "Satisfied" ratings backed by documented evidence, not process-on-paper.
- [ ] Adversarial self-audit completed with disconfirming check.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Asserting a specific rule/form/timing requirement | Marked "[verify against current text]"; no authoritative citations generated |
| Treating disclosure of a conflict as satisfying the conflict obligation | Conflicts register requires a mitigation/elimination assessment separate from disclosure |
| Conflating suitability with best-interest/fiduciary | Standard determination step forces the correct, higher standard per capacity |
| Checkbox illusion (process exists = obligation met) | Evidence test and adversarial self-audit downgrade evidence-thin steps |
| Concluding the process "complies" | Findings only; final determination routed to counsel |
| Ignoring reasonably-available alternatives | Care obligation and rollover step require documented alternatives + cost comparison |
