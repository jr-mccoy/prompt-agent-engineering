---
title: "AML/KYC Program Designer — Risk Rating, CDD/EDD Tiers, and Transaction Monitoring"
category: finance/regulatory-compliance
description: "Design a risk-based Anti-Money-Laundering / Know-Your-Customer program covering the five pillars: governance, customer risk rating, CDD/EDD onboarding tiers, ongoing monitoring and SAR escalation, and independent testing — with no-fabrication and verify-against-current-source guardrails."
techniques:
  - DT-02
  - ST-02
  - CM-02
  - NE-06
  - DS-06
difficulty: advanced
tags:
  - aml
  - kyc
  - cdd
  - edd
  - transaction-monitoring
  - bsa
  - sanctions
updated: "2026-06-08"
related_prompts:
  - domain-finance/regulatory-compliance/finance_sanctions_screening_program.md
  - domain-finance/regulatory-compliance/finance_regulatory_requirement_mapper.md
  - domain-finance/risk-management/finance_operational_risk_rcsa.md
  - domain-finance/field_guide.md
---

**Informational analysis only — not legal or compliance advice. AML/KYC rules (e.g., BSA/FinCEN program requirements, CDD/beneficial-ownership rules, OFAC sanctions, EU AML directives, FATF guidance) change and vary by jurisdiction; confirm all requirements, thresholds, and reporting obligations against current official sources (FinCEN, OFAC, FATF, EU/ESMA, applicable national FIU) and qualified counsel before implementation.**

## Objective

Design a risk-based AML/KYC program framework structured around the recognized program pillars: (1) designated compliance officer and governance, (2) internal policies/procedures and risk assessment, (3) customer due diligence (CDD), enhanced due diligence (EDD), and customer risk rating, (4) ongoing transaction monitoring with suspicious-activity escalation, and (5) independent testing and training. The output is a design framework with placeholders for jurisdiction-specific thresholds, all marked for verification against current rule text.

## When to Use

- Standing up an AML/KYC program for a new bank, broker-dealer, MSB/payments firm, fintech, or fund
- Remediating a program after an exam finding, consent order, or independent-test deficiency
- Extending an existing program to a new product, customer segment, or jurisdiction
- Refreshing the enterprise AML risk assessment and recalibrating CDD/EDD tiers

## Inputs / Context Required

```
<aml_program_context>
INSTITUTION:
- Entity type (bank, BD, RIA, MSB, payments, fintech, fund, crypto-asset service provider)
- Primary AML regulator(s) and jurisdiction(s) — home and host
- Products/services and delivery channels (in-person, online, agent, correspondent)

CUSTOMER BASE:
- Customer types (retail, business/legal-entity, institutional, correspondent, non-resident)
- Higher-risk segments present (PEPs, cash-intensive businesses, MSBs, non-resident, high-risk geographies)
- Beneficial-ownership complexity (layered entities, trusts, nominees)

CURRENT STATE (if remediating):
- Existing risk assessment, CDD/EDD procedures, monitoring system/rules
- Known deficiencies / prior findings

CONSTRAINTS:
- Risk appetite and resourcing
- Date of this design exercise: __________
</aml_program_context>
```

## Constraints

### Must
- State the **applicable AML regulator(s) and jurisdiction(s)**; note that requirements differ across regimes.
- Mark every specific threshold, reporting deadline, form name, or rule citation (e.g., CTR/SAR-type filing thresholds and timelines, beneficial-ownership ownership-percentage thresholds) as **"[verify against current {regulator} rule text]"** — never assert them as authoritative from memory.
- Build the program on a **documented risk assessment** that drives customer risk rating and the CDD/EDD tiering (risk-based approach, not one-size-fits-all).
- Define **risk-rating factors** and a transparent, auditable scoring methodology (customer type, geography, product, channel, behavior).
- Specify **CDD baseline** vs. **EDD triggers and additional measures**, including beneficial-ownership identification and PEP handling.
- Define **ongoing monitoring** logic (rule-based and/or behavioral), alert triage, investigation, and **suspicious-activity escalation/reporting** workflow with decision documentation.
- Include **independent testing**, training, and recordkeeping/retention requirements (mark retention periods for verification).
- Run a **coverage self-audit (NE-06)**: which higher-risk typologies, customer types, products, or channels are not covered by a rule or procedure?

### Must Not
- Assert specific filing thresholds, deadlines, ownership-percentage triggers, or form numbers as authoritative.
- Design a flat program that applies identical diligence regardless of risk (defeats the risk-based standard).
- Treat customer onboarding as a one-time checkbox without ongoing monitoring and periodic refresh.
- Provide a definitive determination that any specific activity is or is not reportable — route SAR/STR decisions through the program's governance and counsel.

## Instructions

**Step 1 — Governance and pillars setup (ST-02).**
Designate the AML/BSA compliance officer and governance reporting line. Confirm the program addresses each pillar; flag any pillar that is undefined.

**Step 2 — Enterprise AML risk assessment (DT-02).**
Score inherent risk across the standard dimensions, then net against controls for residual risk:

| Risk dimension | Factors to assess | Inherent risk (L/M/H) | Key controls | Residual (L/M/H) |
|---|---|---|---|---|
| Customer | PEPs, legal-entity complexity, non-resident, cash-intensive | | | |
| Product/service | Anonymity, cross-border, speed, value transfer | | | |
| Geography | Higher-risk jurisdictions (verify against current lists) | | | |
| Channel | Non-face-to-face, agent, correspondent | | | |

Mark any reference to high-risk-jurisdiction lists as "[verify against current FATF/OFAC/regulator lists]".

**Step 3 — Customer risk-rating methodology (DS-02).**
Define factors, weights, and the score-to-tier mapping. Example structure (weights illustrative — calibrate to the institution):

```
Customer Risk Score = Σ (factor weight × factor score)
  Factors: customer type, beneficial-ownership complexity, geography,
           product/channel, expected vs. actual activity, adverse media/PEP status
Tier mapping:
  Low     → standard CDD, periodic refresh on a longer cycle
  Medium  → standard CDD + targeted EDD elements
  High    → full EDD + senior approval + shorter refresh cycle + enhanced monitoring
```
Refresh cycles and approval levels are policy choices — state them; do not assert a regulator-mandated cycle without verification.

**Step 4 — CDD and EDD design (DT-02).**

| Element | CDD baseline (all customers) | EDD (high-risk / triggered) |
|---|---|---|
| Identity verification (CIP) | Verify identity of customer | + documentary/non-documentary corroboration |
| Beneficial ownership | Identify/verify beneficial owners [verify ownership-% trigger] | + ownership-chain mapping, source-of-funds/wealth |
| Purpose & expected activity | Capture expected activity profile | + deeper rationale, site visits where applicable |
| PEP / adverse media | Screen at onboarding | + senior sign-off, ongoing enhanced review |
| Approval | Standard | Senior/committee approval documented |

State EDD **triggers** explicitly (e.g., PEP, high-risk geography, high-risk product, unusual structure).

**Step 5 — Ongoing monitoring and escalation (ST-02).**
Define: monitoring approach (rule thresholds and/or behavioral analytics), alert generation, triage/scoring, investigation steps, and the **suspicious-activity escalation path** ending in a documented file/no-file decision. Mark filing thresholds/deadlines as "[verify against current {regulator} rule text]". Specify decision documentation and quality assurance over the SAR/STR process.

**Step 6 — Testing, training, recordkeeping.**
Define independent testing scope and cadence, role-based training, and recordkeeping/retention (mark retention periods for verification).

**Step 7 — Coverage self-audit (NE-06 / QA-02).**
List higher-risk typologies, customer types, products, geographies, or channels not covered by an explicit rule/procedure. Name the **checkbox-compliance illusion** (onboarding completed ≠ risk understood) and require a disconfirming check: "Which customers passed onboarding but exhibit behavior the monitoring rules would not catch?"

## Output Format

### Program Overview
- Pillars status, compliance officer, governance line, jurisdiction/regulator(s).

### Enterprise AML Risk Assessment
[Step 2 table + residual-risk narrative]

### Customer Risk-Rating Methodology
[Factors, weights, scoring formula, tier mapping]

### CDD / EDD Design
[Step 4 table + EDD trigger list]

### Monitoring & Escalation Workflow
| Stage | Logic / criteria (verify thresholds) | Owner | Documentation |
|---|---|---|---|
| Alert generation | [verify thresholds] | | |
| Triage | | | |
| Investigation | | | |
| File/no-file decision | [verify SAR/STR threshold & deadline] | | |

### Testing, Training, Recordkeeping
| Component | Scope | Cadence | Retention (verify) | Owner |
|---|---|---|---|---|

### Coverage Self-Audit
- Uncovered typologies/segments/channels: …
- Disconfirming check result: …

### Verify-Against-Current Instruction
> Confirm all CDD/EDD requirements, beneficial-ownership triggers, monitoring/reporting thresholds, filing deadlines, high-risk-jurisdiction lists, and retention periods against current official sources (FinCEN/OFAC/FATF/EU/national FIU) **as of [date]**. Route SAR/STR determinations and legal interpretation to qualified compliance/legal counsel.

## Verification

- [ ] Applicable AML regulator(s) and jurisdiction(s) stated.
- [ ] All thresholds, deadlines, ownership-% triggers, and form names marked "[verify against current rule text]".
- [ ] Program is risk-based: risk assessment drives risk rating, which drives CDD/EDD tiering.
- [ ] Risk-rating methodology is transparent and auditable (factors, weights, score-to-tier).
- [ ] EDD triggers and additional measures specified; beneficial ownership and PEP handling addressed.
- [ ] Monitoring → escalation → documented file/no-file workflow defined.
- [ ] Independent testing, training, and recordkeeping/retention included.
- [ ] Coverage self-audit identifies uncovered typologies and includes a disconfirming check.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Asserting a CTR/SAR threshold or BO ownership-% from memory | All such specifics marked "[verify against current rule text]" |
| Checkbox-compliance illusion (onboarding done = customer understood) | Disconfirming check required: which onboarded customers behave outside the monitoring rule set |
| Flat program applied to all customers | Risk-based tiering is mandatory; EDD triggers explicit; flat designs flagged as deficient |
| Treating KYC as one-time | Periodic refresh and ongoing monitoring required; refresh cycles tied to risk tier |
| Over-reliance on prior-year risk assessment | Self-audit asks what changed in customers/products/geographies since last assessment |
| Presenting a file/no-file conclusion as definitive | SAR/STR decisions routed through governance and counsel; documentation and QA required |
