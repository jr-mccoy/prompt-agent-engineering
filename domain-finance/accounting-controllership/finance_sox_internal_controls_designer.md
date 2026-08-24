---
title: "SOX Internal Controls Designer — Control Matrix for a Process"
category: finance/accounting-controllership
description: "Design SOX-aligned internal controls for a business process: map risks to control objectives and assertions, build a control matrix (preventive/detective, manual/automated, key/non-key), embed segregation of duties and ITGC dependencies, and align to the COSO 2013 framework with §302/§404 context."
techniques:
  - RT-05
  - DT-02
  - QA-05
  - RT-03
  - QA-04
difficulty: advanced
tags:
  - sox
  - internal-controls
  - icfr
  - coso
  - control-matrix
  - segregation-of-duties
updated: "2026-06-08"
related_prompts:
  - domain-finance/accounting-controllership/finance_journal_entry_review_protocol.md
  - domain-finance/risk-management/finance_operational_risk_rcsa.md
  - domain-finance/accounting-controllership/finance_account_reconciliation_protocol.md
  - domain-finance/field_guide.md
---

**Informational only — not accounting, audit, or tax advice. Verify all standard references against current authoritative guidance (SEC rules, PCAOB standards, COSO framework).**

## Objective

Design a SOX-aligned internal-control structure for a defined business process (e.g., revenue, procure-to-pay, financial close, payroll): identify the risks of material misstatement, link them to financial-statement assertions and control objectives, build a control matrix specifying each control's type and attributes, embed segregation of duties (SoD) and IT general control (ITGC) dependencies, and map the design to the **COSO 2013** framework — providing a control file ready for management's §404 assessment and external-auditor walkthrough.

---

## When to Use

- Designing or redesigning controls for an in-scope process under SOX §404.
- Remediating a control gap or deficiency identified in testing.
- Preparing a risk-and-control matrix (RACM) for a new system, process, or acquisition being brought into scope.
- Documenting the control environment for a management ICFR assessment or auditor walkthrough.
- **Do not use** to opine on whether ICFR is "effective" (that requires testing and evidence, not design), or to assert a deficiency is/ isn't a material weakness without a severity evaluation.

---

## Inputs / Context Required

```
<sox_context>
Entity / filer status: accelerated | large accelerated | non-accelerated | newly public:
Process in scope: [revenue | P2P | O2C | close | payroll | treasury | inventory | tax]
Reporting framework: US GAAP | IFRS
Auditor attestation required? (§404(b)): Yes | No

PROCESS NARRATIVE (paste/describe):
- Key process steps end to end:
- Systems involved (ERP, sub-systems, spreadsheets):
- Roles/people performing each step:
- Existing controls (if any), with frequency:

RISK CONTEXT:
- Significant accounts / disclosures touched by this process:
- Relevant assertions of concern (existence, completeness, accuracy, valuation, rights/obligations, presentation):
- Materiality / significance for scoping:
- Known prior deficiencies:
</sox_context>
```

---

## Constraints

### Must
- Anchor the design in **COSO 2013**: address the five components (Control Environment, Risk Assessment, Control Activities, Information & Communication, Monitoring) and reference the 17 principles where they bear on the design.
- Distinguish **entity-level controls** from **process-level (transaction) controls**, and note **ITGCs** (access, change management, operations) that the automated process controls depend on.
- For each risk, identify the **financial-statement assertion(s)** at risk and a **control objective**, then specify a control with these attributes:
  - **Preventive vs detective**
  - **Manual vs automated** (and IT-dependent manual where a report feeds a manual control)
  - **Key vs non-key** (key = relied upon to address a material risk)
  - **Frequency** (per transaction, daily, weekly, monthly, quarterly, annual)
  - **Control owner** and **evidence of operation**
- Embed **segregation of duties**: no individual should both initiate and approve, or have custody + recording + authorization over the same transaction. Flag SoD conflicts.
- Map **§302** (CEO/CFO disclosure-controls certifications) and **§404** (management ICFR assessment; auditor attestation where applicable) context to the design.
- For **IT-dependent and automated controls**, state the ITGC the control relies on (e.g., an automated three-way match relies on access and change-management controls over the ERP).
- Include a **management review control (MRC)** design note where precision matters (level of precision, criteria, investigation threshold, evidence).
- Address how a **deficiency** would be evaluated for severity (deficiency → significant deficiency → material weakness) at a conceptual level — without concluding severity for a hypothetical.

### Must Not
- Assert ICFR is "effective" — design ≠ operating effectiveness; effectiveness requires testing.
- Invent SEC/PCAOB rule numbers, COSO principle numbers, or filer-deadline dates not independently known to be correct — reference by name and flag for confirmation.
- Conclude that a control gap is a "material weakness" without a severity analysis.
- Design a control with an unresolved SoD conflict and call it adequate.
- Treat an automated control as reliable without identifying its ITGC dependency.
- Omit the control owner or the evidence-of-operation for any key control.

---

## Instructions

1. **Scope and significant accounts.** Identify the significant accounts/disclosures and relevant assertions the process affects.

2. **Risk assessment.** For each process step, identify the risk(s) of material misstatement (what could go wrong — WCGW) and tie each to assertion(s).

3. **Map control objectives.** For each risk, state the control objective (what a control must achieve to address the risk).

4. **Design controls.** For each objective, specify a control and its full attribute set (preventive/detective, manual/automated, key/non-key, frequency, owner, evidence). Prefer preventive + automated where feasible; use detective controls (reconciliations, reviews) as backstops.

5. **SoD check.** Build the role-to-activity matrix; flag any single role spanning initiate/approve/record/custody for the same transaction; propose a remediation (split duties or add a compensating detective control).

6. **ITGC linkage.** For automated and IT-dependent manual controls, list the ITGC dependency (logical access, change management, computer operations, data integrity of feeder reports).

7. **Entity-level + monitoring.** Note relevant entity-level controls and monitoring controls (management reviews, internal audit) that provide indirect or direct assurance.

8. **COSO mapping.** Summarize how the design addresses the five COSO components / relevant principles.

9. **Deficiency-evaluation note.** State conceptually how a failure of each key control would be evaluated for severity (likelihood × magnitude of potential misstatement).

10. **Verification (QA-04/QA-05).** Confirm every risk maps to a control; every key control has owner + evidence + frequency; no unresolved SoD conflict; no fabricated rule/principle numbers.

---

## Output Format

```
## SOX Control Design — [Process]
Filer status: [__] | §404(b) attestation: [Yes/No] | Framework: [US GAAP/IFRS]
COSO 2013 basis | Status: DESIGN (not an effectiveness conclusion)

### Significant Accounts & Assertions
| Account / disclosure | Assertions at risk |
|----------------------|--------------------|
| Revenue | Existence, Completeness, Accuracy, Cutoff |

### Risk & Control Matrix (RACM)
| # | Process step | Risk (WCGW) | Assertion | Control objective | Control description | Prev/Det | Manual/Auto | Key? | Freq | Owner | Evidence | ITGC dependency |
|---|--------------|-------------|-----------|-------------------|---------------------|----------|-------------|------|------|-------|----------|-----------------|
| 1 | PO creation | Unauthorized purchase | Existence | Only approved POs proceed | System enforces approval limits | Prev | Auto | Yes | Per txn | Procurement | Approval config log | Access + change mgmt |
| 2 | Invoice match | Pay without receipt | Completeness/Accuracy | 3-way match before pay | Automated PO-receipt-invoice match | Prev | Auto | Yes | Per txn | AP | Match exception report | Access + data integrity |
| 3 | Period close | Material misstatement | Accuracy/Valuation | MRC over flux | Controller reviews flux > threshold w/ support | Det | IT-dep manual | Yes | Monthly | Controller | Signed flux w/ explanations | Report accuracy (ITGC) |

### Segregation of Duties
| Role | Initiate | Approve | Record | Custody | Conflict? | Remediation |
|------|----------|---------|--------|---------|-----------|-------------|
| AP Clerk | ✓ | | ✓ | | ⚠ initiate+record | Add independent approval |

### ITGC Dependencies Summary
[Access management, change management, operations the automated controls rely on.]

### COSO 2013 Mapping
| Component | How addressed |
|-----------|---------------|
| Control Environment | [tone, authority/responsibility] |
| Risk Assessment | RACM WCGW analysis |
| Control Activities | RACM controls |
| Information & Communication | [reporting, evidence] |
| Monitoring | [MRCs, internal audit] |

### Management Review Control (MRC) Design Notes
Precision: [level] | Criteria: [thresholds] | Investigation trigger: [variance] | Evidence: [retained]

### Deficiency Severity Framework (conceptual)
Deficiency → Significant deficiency → Material weakness, evaluated by likelihood × magnitude of potential misstatement. [No severity conclusion drawn for a hypothetical.]

Verify SEC/PCAOB references and COSO principle numbers against current authoritative sources as of [date].
```

---

## Verification

- [ ] Every identified risk (WCGW) maps to at least one control and the affected assertion(s).
- [ ] Each control specifies prev/det, manual/auto, key/non-key, frequency, owner, evidence.
- [ ] SoD matrix built; conflicts flagged with remediation.
- [ ] Automated / IT-dependent controls list their ITGC dependencies.
- [ ] Entity-level and monitoring controls noted.
- [ ] COSO 2013 five components addressed.
- [ ] §302 / §404 context reflected; design vs effectiveness distinction stated.
- [ ] No fabricated SEC/PCAOB rule numbers or COSO principle numbers.
- [ ] No severity (material-weakness) conclusion drawn for a hypothetical.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Claiming ICFR is "effective" from a design exercise | Label output DESIGN; effectiveness requires testing and evidence, not control design |
| Concluding a gap is a "material weakness" | Provide the severity framework only; do not conclude severity without a likelihood/magnitude analysis |
| Designing around an unresolved SoD conflict | Flag every initiate/approve/record/custody overlap and require a split or compensating detective control |
| Treating automated controls as reliable in isolation | Require the ITGC dependency for every automated / IT-dependent manual control |
| Fabricating SEC/PCAOB/COSO citation numbers | Reference frameworks by name; flag specific rule/principle numbers for confirmation |
| Applying US-SOX assumptions to an IFRS or non-SEC entity | Confirm filer status and applicable regime; the control objectives transfer but the regulatory overlay differs |
