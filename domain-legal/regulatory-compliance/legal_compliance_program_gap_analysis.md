---
title: "Compliance Program Gap Analysis — FCPA, AML, Sanctions, Antitrust"
category: legal/regulatory-compliance
description: "Evaluate a corporate compliance program for a named misconduct-risk area (anti-bribery / FCPA, AML, economic sanctions and export controls, antitrust) against a user-supplied evaluation framework — design, resourcing and autonomy, and operation in practice — and produce a prioritized, owned remediation plan. Counsel-facing and privilege-aware; tests whether the program works, not whether documents exist."
techniques:
  - DS-01
  - RT-02
  - CM-02
  - QA-05
  - QA-01
difficulty: advanced
tags:
  - legal
  - regulatory-compliance
  - compliance-program
  - fcpa
  - anti-corruption
  - aml
  - sanctions
  - antitrust
  - gap-analysis
updated: "2026-09-24"
reasoning:
  styles: [analytic, systematic, evaluative]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: mixed
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, matrix]
  user_role: [attorney, in_house_counsel, chief_compliance_officer]
related_prompts:
  - domain-legal/regulatory-compliance/legal_regulatory_change_impact_assessment.md
  - domain-legal/regulatory-compliance/legal_internal_investigation_plan.md
  - domain-legal/regulatory-compliance/legal_voluntary_disclosure_decision_memo.md
  - domain-finance/regulatory-compliance/finance_aml_kyc_program_designer.md
  - domain-finance/regulatory-compliance/finance_sanctions_screening_program.md
---

# Compliance Program Gap Analysis

**Objective:** Assess whether a company's compliance program for one misconduct-risk area is well designed, adequately resourced and empowered, and working in practice, measured against an evaluation framework the user supplies (for example, an enforcement agency's published program-evaluation guidance, a sentencing-guidelines effective-program standard, or a statutory program requirement). Produce a gap table with evidence, a severity rating tied to enforcement consequence, and an owned remediation plan that counsel can use for board reporting, pre-transaction diligence, or a remediation narrative to a regulator.

**When to use:**
- Periodic program review commissioned by the GC, CCO, or audit committee.
- Pre-acquisition diligence or post-closing integration of a target's program.
- After an incident or investigation, to build the remediation record that supports cooperation or charging-decision credit.
- Before a monitorship, certification, or program-attestation deadline.

**Distinct from:**
- `domain-finance/regulatory-compliance/finance_compliance_gap_analysis.md` — maps financial-services controls to regulatory requirements for a compliance function. This prompt evaluates *program effectiveness* in enforcement-risk areas for counsel, in any industry.
- `domain-finance/regulatory-compliance/finance_aml_kyc_program_designer.md` and `finance_sanctions_screening_program.md` — they *design* operational programs; this prompt *evaluates* an existing one and is typically run under privilege.
- `domain-legal/regulatory-compliance/legal_regulatory_change_impact_assessment.md` — one rule's delta, not whole-program effectiveness.

---

## Your Input

- **Risk area:** [Anti-bribery / FCPA and local anti-corruption; AML; sanctions and export controls; antitrust / competition; other — one per run]
- **Jurisdiction(s) and enforcers:** [e.g., US DOJ / SEC; OFAC; FinCEN; UK SFO / OFSI; EU Commission / national competition authority]
- **Evaluation framework (text):** [Paste the framework's questions or hallmarks, with its title and version date. If none is supplied, the prompt uses a generic three-question structure — design, resourcing/empowerment, operation — and marks it GENERIC.]
- **Company risk profile:** [Countries of operation, third-party intermediaries, government touchpoints, customer types, products, M&A activity, market position / competitor contact points]
- **Program documents:** [Code, policies, procedures, risk assessment, training records, third-party due diligence files, hotline data, investigation logs, discipline records, testing / audit reports]
- **Organization:** [Compliance reporting line, headcount, budget, board oversight, access to data]
- **Known incidents or findings:** [Prior investigations, audit findings, regulator correspondence]
- **Purpose of review:** [Board report / diligence / remediation narrative / certification]
- **Privilege posture:** [Counsel-directed review? Outside counsel engaged?]

---

## Constraints

**Must:**
- Map every finding to a specific element of the supplied framework, quoting the element.
- Test operation, not existence: for each element, identify the evidence that the control ran (data, samples, metrics), not just the policy that describes it.
- Tie the risk assessment to the program: controls must be proportionate to the specific risks in the company's profile (e.g., high-risk intermediaries, state-owned customers, competitor trade-association contact).
- Rate severity by enforcement consequence: **Critical** (likely to be viewed as a program failure contributing to misconduct), **High**, **Medium**, **Low** — each with a one-line reason.
- Give every remediation item an accountable role, a target date, and the evidence that will demonstrate completion.
- Mark privilege: note which work product should stay under counsel direction and which outputs (e.g., a board summary) will be non-privileged.

**Must Not:**
- Invent agency guidance, framework versions, sentencing provisions, case names, or enforcement outcomes. Use `[CITE: ...]`, `[NEED PIN: ...]`, `[VERIFY: current version of framework]`.
- Score the program as effective because documents exist, training completion is high, or the hotline has low volume.
- Import a different risk area's framework (e.g., AML customer-due-diligence standards into an antitrust review) without saying so.
- Predict charging decisions or penalty amounts.
- Use generic "consult counsel" boilerplate.

---

## Instructions

1. **Lock scope.** State the risk area, jurisdictions, framework (title + version as supplied), review period, and purpose. If the framework is not supplied, state GENERIC and use design / resourcing-empowerment / operation.
2. **Build the risk profile.** From the company facts, list the top risk scenarios for this area (e.g., third-party agent payments in high-risk jurisdictions; shipments through transshipment hubs; information exchange at trade associations).
3. **Element-by-element review.** For each framework element: quote it, summarize the company's control, cite the evidence of operation, and mark Met / Partial / Gap / No Evidence.
4. **Risk-to-control fit.** Cross-check each top risk scenario against the controls that address it. A top risk with no specific control is at least High.
5. **Root cause.** For each Gap or Partial, identify whether the cause is design, resourcing / authority, or operation. Remediation differs by cause.
6. **Severity rating.** Rate each finding with a one-line enforcement-consequence reason.
7. **Remediation plan.** Action, owner, dependencies, date, completion evidence. Sequence Critical items first; flag any that require board action.
8. **Privilege and output plan.** Specify what stays privileged and what is released, and in what form.
9. **Executive summary.** Overall posture, top five findings, resourcing asks, board decisions needed.

---

## Output Format

```markdown
# Compliance Program Gap Analysis — {Risk area} — {Company}
**Framework:** {title, version as supplied / GENERIC} | **Review period:** {dates} | **Privileged & Confidential — Prepared at the Direction of Counsel** {if applicable}

## 1. Executive Summary
- Overall posture: {one paragraph}
- Top findings: {1–5, with severity}
- Board / leadership decisions needed: {...}

## 2. Scope and Method
{risk area, jurisdictions, framework, evidence reviewed, limitations}

## 3. Risk Profile — Top Scenarios
| # | Scenario | Why it is elevated for this company |
|---|---|---|

## 4. Element-by-Element Findings
| Framework element (quoted) | Company control | Evidence of operation | Status | Root cause | Severity (reason) |
|---|---|---|---|---|---|

## 5. Risk-to-Control Fit
| Scenario | Specific controls | Gap? |
|---|---|---|

## 6. Remediation Plan
| Finding | Action | Owner (role) | Target date | Completion evidence | Board action? |
|---|---|---|---|---|---|

## 7. Privilege and Distribution
{privileged work product vs releasable summaries}

## 8. Open Items and Placeholders
{missing documents; [CITE] / [VERIFY] list}
```

---

## Worked Example

**Input (abridged):** Anti-bribery review for a medical-device manufacturer selling through distributors in eight countries, several with government-hospital customers. Framework supplied: an enforcement agency's program-evaluation questions (user pasted the text and version date). Evidence: third-party due diligence files, distributor contracts, T&E data, training records.

**Output (excerpt):**

| Framework element (quoted) | Company control | Evidence of operation | Status | Root cause | Severity |
|---|---|---|---|---|---|
| "Does the company have a process for managing risks presented by third parties…?" (as supplied) | Distributor onboarding questionnaire | 31 of 44 distributors have completed questionnaires; 0 renewed since onboarding; no red-flag escalation log | Partial | Operation — no refresh cycle, no owner | **High** — government-hospital sales run through the un-refreshed distributors |
| "Is the compliance function adequately resourced…?" (as supplied) | One compliance manager covering eight countries, reporting to CFO | Budget data; no direct access to audit committee | Gap | Resourcing / authority | **High** — reporting line to the function it monitors |

Risk-to-control fit: "Distributor discounts used to fund payments to hospital officials" — no margin-analysis control exists → **Critical**. Remediation: implement distributor margin monitoring against peer baseline; owner Director of Finance Operations; target 60 days; completion evidence: first quarterly exception report reviewed by compliance.

---

## Verification

- [ ] Jurisdiction and enforcer lock: findings measured against the supplied framework for the named jurisdiction only.
- [ ] Citation discipline: framework elements quoted from supplied text; no invented guidance, versions, or enforcement outcomes.
- [ ] Every Met rating has evidence of operation, not just a policy reference.
- [ ] Every top risk scenario is cross-checked against a specific control.
- [ ] Every finding has a root cause (design / resourcing-authority / operation) and a severity reason.
- [ ] Every remediation item has an owner, date, and completion evidence.
- [ ] Privilege and distribution plan stated.
- [ ] No charging or penalty predictions.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| "Paper program" scored effective because policies and training exist | Require operating evidence (samples, data, escalations, discipline) for every Met |
| High training-completion or low hotline volume read as a healthy culture | Treat both as ambiguous; low hotline volume can mean distrust; look for substantiation and retaliation data |
| Generic risk assessment accepted without company-specific scenarios | Build scenarios from the company's actual geography, customers, and intermediaries |
| Quoting a framework version or agency guidance from memory | Quote only supplied text; `[VERIFY: current version]` if the user has not confirmed it |
| Remediation that fixes the document but not the cause (e.g., rewriting a policy when the problem is no headcount) | Root-cause each gap; remediation must address the cause |
| Mixing risk areas (AML customer due diligence standards applied to antitrust) | One risk area per run; say so explicitly when borrowing a concept |
| Predicting whether an enforcer would decline or reduce charges | Describe program strengths and weaknesses; leave outcome prediction out |
