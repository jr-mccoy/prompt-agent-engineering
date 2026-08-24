---
title: "Compliance Gap Analysis — Current State vs. Regulatory Requirements with Remediation Plan"
category: finance/regulatory-compliance
description: "Perform a structured gap analysis comparing current control and process state against applicable regulatory requirements, classify each gap by severity and exposure, and produce a prioritized, owned remediation plan — with verify-against-current-source and no-fabrication guardrails."
techniques:
  - DT-02
  - DS-06
  - NE-06
  - CM-02
  - QA-02
difficulty: advanced
tags:
  - gap-analysis
  - compliance
  - remediation
  - controls
  - regulatory
updated: "2026-06-08"
related_prompts:
  - domain-finance/regulatory-compliance/finance_regulatory_requirement_mapper.md
  - domain-finance/accounting-controllership/finance_sox_internal_controls_designer.md
  - domain-finance/risk-management/finance_operational_risk_rcsa.md
  - domain-finance/field_guide.md
---

**Informational analysis only — not legal or compliance advice. Regulations change and vary by jurisdiction; confirm all requirements against current official sources (SEC, FINRA, Basel/BIS, FinCEN, OFAC, EU/ESMA, and applicable local regulators) and qualified counsel before relying on any output.**

## Objective

Compare the organization's current state (policies, controls, processes, evidence) against the applicable regulatory requirements for a defined scope, identify and classify each gap, quantify residual exposure, and produce a prioritized, owned, time-bound remediation roadmap. The requirement baseline must be verified against current official sources; this prompt organizes and analyzes — it does not determine legal compliance.

## When to Use

- After producing a regulatory-requirement map (companion prompt) and before an exam or audit
- Pre-acquisition or post-acquisition compliance integration
- Responding to a new or amended regulation, enforcement trend, or consent order
- Periodic compliance self-assessment / attestation cycles
- Building the remediation plan that supports a board or regulator-facing readiness narrative

## Inputs / Context Required

```
<gap_analysis_context>
SCOPE:
- Activity / product / entity under review
- Jurisdiction(s) and applicable regulator(s)
- The requirement baseline (from requirement map or user-supplied): each requirement,
  its source, and the obligation in plain terms

CURRENT STATE EVIDENCE (per requirement):
- Relevant policy / procedure (name, version, date)
- Control(s) in place (preventive/detective, manual/automated, frequency)
- Evidence of operation (logs, testing results, attestations)
- Known issues, prior findings, open remediation items

ORGANIZATIONAL CONTEXT:
- Risk appetite / materiality threshold
- Resourcing constraints
- Target dates / regulatory deadlines (verify against current source)
- Date of this assessment: __________
</gap_analysis_context>
```

## Constraints

### Must
- Begin from a **verified requirement baseline**: for each requirement, mark its citation/threshold/deadline as "[verify against current [regulation] text]" and require confirmation against the official source as of the assessment date.
- State **jurisdiction and regulator** for each requirement assessed.
- Classify each requirement as **Compliant / Partial gap / Material gap / Not assessed (insufficient evidence)** — and require *evidence* for any "Compliant" rating (RT-05); a control's existence on paper is not sufficient.
- Rate each gap's **severity** (regulatory exposure × likelihood × detectability) using DS-06 tiers.
- For each gap, specify a **remediation action, owner, target date, and interim mitigant**.
- Run an **adversarial self-audit (QA-02 / NE-06)**: which "Compliant" ratings rest only on policy existence, not operating evidence? Which requirements were excluded from scope and why?
- Distinguish **design gaps** (control not designed to meet the requirement) from **operating gaps** (control designed but not operating effectively).
- State all **assumptions** (e.g., interpretation of an ambiguous requirement) explicitly and route interpretation to counsel.

### Must Not
- Fabricate or assert specific citations, thresholds, or deadlines as authoritative.
- Rate a requirement "Compliant" based solely on the existence of a policy without operating evidence (checkbox-compliance illusion).
- Carry forward prior-year ratings without re-testing current state (over-reliance on prior mapping).
- Silently drop requirements from scope — every excluded requirement must be named with a reason.
- Present the gap analysis as a legal conclusion of compliance.

## Instructions

**Step 1 — Lock the requirement baseline.**
For each in-scope requirement: restate the obligation in plain language, name the regulator and jurisdiction, and mark the citation/threshold/deadline as "[verify against current text]." Confirm the baseline is current as of the assessment date.

**Step 2 — Gather and rate current-state evidence (DT-02, RT-05).**
For each requirement, document the policy, control(s), and *evidence of operation*. Assign a current-state rating:
- **Compliant** — control is designed to meet the requirement AND operating evidence supports it.
- **Partial gap** — control partially addresses the requirement, or design adequate but operating evidence weak/incomplete.
- **Material gap** — no control, or control fundamentally inadequate to the requirement.
- **Not assessed** — insufficient evidence to conclude; treat as open risk.

**Step 3 — Classify gap type.**
For each gap, label **Design gap** vs. **Operating gap** (and **Documentation/evidence gap** where the control may work but cannot be evidenced).

**Step 4 — Score severity and exposure (DS-06).**
Composite severity from: regulatory exposure (enforcement/penalty/license risk), likelihood of occurrence, and detectability if it occurs.
- **Critical:** Core obligation; high enforcement exposure; license/registration or AML/sanctions/capital implications.
- **High:** Significant conduct/disclosure/recordkeeping obligation; meaningful penalty exposure.
- **Medium:** Process/documentation weakness with limited direct exposure.
- **Low:** Minor or hygiene issue.

**Step 5 — Build the remediation plan (ST-02).**
For each gap: define the remediation action, accountable owner, target completion date, dependencies, an **interim mitigant** for the period before remediation completes, and how completion will be evidenced/validated.

**Step 6 — Quantify residual exposure.**
Summarize residual exposure by severity tier before and after planned remediation. Note where remediation timelines run past a regulatory deadline (verify deadline against current source) and flag the resulting heightened exposure window.

**Step 7 — Adversarial self-audit (QA-02 / NE-06).**
Answer explicitly:
- Which "Compliant" ratings rely on policy existence rather than operating evidence?
- Which requirements were excluded from scope, and is the exclusion defensible?
- Were any ratings carried over from a prior assessment without re-testing?
- What disconfirming evidence (e.g., recent incidents, near-misses, exceptions) contradicts a favorable rating?

## Output Format

### Gap Analysis Register
| # | Requirement (plain language) | Jurisdiction / Regulator | Citation/threshold (verify) | Current-state rating | Gap type | Severity | Evidence reviewed |
|---|---|---|---|---|---|---|---|
| | | | [verify against current text] | Compliant/Partial/Material/Not assessed | Design/Operating/Documentation | Critical/High/Med/Low | |

### Remediation Plan
| # | Gap | Remediation action | Owner | Target date | Interim mitigant | Validation method | Past-deadline flag |
|---|---|---|---|---|---|---|---|

### Residual Exposure Summary
| Severity tier | # gaps (current) | # gaps after planned remediation | Notes |
|---|---|---|---|
| Critical | | | |
| High | | | |
| Medium | | | |
| Low | | | |

### Adversarial Self-Audit
- "Compliant" ratings resting only on policy existence: …
- Requirements excluded from scope (with reason): …
- Ratings carried over without re-testing: …
- Disconfirming evidence considered: …

### Verify-Against-Current Instruction
> Every requirement, citation, threshold, and deadline must be confirmed against the current official regulator source **as of [assessment date]**. Remediation timelines must be re-checked against current effective dates. Legal interpretation and final compliance conclusions route to qualified compliance/legal counsel.

## Verification
- [ ] Requirement baseline marked "[verify against current text]" and confirmed current.
- [ ] Each requirement has jurisdiction and regulator.
- [ ] Every "Compliant" rating is supported by operating evidence, not policy existence alone.
- [ ] Gaps classified by type (design / operating / documentation) and severity tier.
- [ ] Each gap has remediation action, owner, target date, and interim mitigant.
- [ ] Residual exposure summarized before and after remediation.
- [ ] Excluded requirements named with rationale.
- [ ] Adversarial self-audit completed, including disconfirming evidence.

## False-Positive Prevention
| Overclaim risk | Guardrail |
|---|---|
| Rating a requirement "Compliant" because a policy exists | Operating evidence required for any Compliant rating; policy-only items downgraded to Partial gap |
| Asserting a citation/threshold/deadline as authoritative | All marked "[verify against current text]"; confirmation against official source required |
| Checkbox-compliance illusion (full register = compliant program) | Adversarial self-audit forces disconfirming evidence and identifies evidence-thin ratings |
| Over-reliance on prior-year assessment | Carried-over ratings must be flagged and re-tested against current state |
| Scope omission (silent dropping of requirements) | Every excluded requirement named with rationale |
| Remediation plan that quietly slips past a regulatory deadline | Past-deadline flag mandatory; heightened-exposure window called out |
