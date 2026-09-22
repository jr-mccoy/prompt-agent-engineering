---
title: "RAI NIST AI RMF Assessment"
category: AI-ML/responsible-ai-governance
description: "Assess an AI system against the NIST AI Risk Management Framework's four functions — GOVERN, MAP, MEASURE, MANAGE — producing a function-by-function maturity gap assessment with evidence, gaps, and prioritized actions, without inventing category identifiers or normative thresholds."
techniques:
  - DS-01
  - ST-02
  - DS-06
  - QA-12
  - RP-02
difficulty: advanced
tags:
  - nist-ai-rmf
  - risk-management
  - governance-maturity
  - responsible-ai
  - gap-assessment
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_governance_framework_design.md
  - domain-AI-ML/responsible-ai-governance/rai_eu_ai_act_compliance_assessment.md
  - domain-AI-ML/responsible-ai-governance/rai_model_risk_assessment.md
---

# RAI NIST AI RMF Assessment

**Objective:** Assess an AI system's risk-management maturity against the NIST AI Risk Management Framework's four functions (GOVERN, MAP, MEASURE, MANAGE) and their categories — producing a function-by-function gap assessment with evidence, gaps, and prioritized actions — while treating the framework as voluntary guidance, not a pass/fail legal compliance check, and without inventing category/subcategory identifiers or normative thresholds.

**When to Use:**
- To establish a baseline of AI risk-management maturity across an organization or system.
- To structure a self-assessment ahead of an internal governance review or audit.
- To map existing controls and documentation onto a recognized risk-management structure.

**When NOT to Use:**
- As a legal compliance determination — the AI RMF is voluntary and non-binding; this is a maturity assessment, not a verdict.
- As a substitute for qualified legal counsel or a regulatory specialist when binding regulation also applies.
- For frameworks the user has not confirmed — ask which framework and version applies first.

## Inputs / Context

- **System description** — purpose, lifecycle stage, who and what it affects.
- **Organizational context** — roles, accountability structures, risk appetite, existing policies.
- **Existing artifacts** — governance policies, risk register, model cards, evaluation reports, monitoring dashboards.
- **Scope** — single system, product line, or organization-wide.
- **User-confirmed framework version** — which edition/profile of the AI RMF applies (ask; do not assume).

## Constraints

**Must:**
- Frame the result as a risk-management *maturity* assessment, not a compliance pass/fail.
- Organize findings under the four functions (GOVERN, MAP, MEASURE, MANAGE) and describe their category *areas* generically.
- Separate evidenced controls from gaps, and rank gaps by significance and effort.

**Must Not:**
- NO-FABRICATION: never invent specific category/subcategory identifiers, section numbers, normative text, numeric thresholds, dollar amounts, or deadlines from memory; the user confirms which framework and version applies; map the system to the framework's STRUCTURE and obligations at a conceptual level and explicitly flag any specific identifier or threshold as "verify against the current official source."
- Declare the system "compliant" or "certified" — the framework is voluntary; produce maturity findings, not verdicts.
- Assume a particular profile or version applies; confirm with the user first.

**Instructions:**

1. **Confirm scope and framework version.** Establish what is being assessed and which edition/profile the user is using. Mark unknowns as open questions.

2. **Assess GOVERN.** Evaluate the governance area: accountability structures, policies, risk culture, roles, and oversight. Note evidence and gaps generically.

3. **Assess MAP.** Evaluate context-setting: intended use, stakeholders, the categorization of risks and impacts, and identification of where harms could arise.

4. **Assess MEASURE.** Evaluate how risks are analyzed, tracked, and measured: metrics, evaluation methods, validity/reliability, and trustworthiness characteristics.

5. **Assess MANAGE.** Evaluate how identified risks are prioritized, treated, monitored, and responded to over the lifecycle.

6. **Rate maturity per function.** Use a simple, transparent maturity scale (e.g., absent / partial / defined / managed) with stated rationale — not a normative score from the framework.

7. **Rank gaps and propose actions.** Prioritize gaps by significance × effort and propose concrete next actions, flagging any that need legal or specialist interpretation.

**Output Format:**

A markdown maturity assessment:
- **Scope & Framework Version** — what is assessed; version; open questions.
- **Function Summary Table** — Function | Maturity (absent/partial/defined/managed) | Rationale.
- **Per-Function Detail** — for GOVERN/MAP/MEASURE/MANAGE: category areas | evidence present | gaps.
- **Ranked Gaps & Actions** — significance × effort × owner.
- **Verification Notes** — items to verify against the current official source.
- **INSUFFICIENT EVIDENCE** — an enumerated maturity value alongside absent / partial / defined / managed, and distinct from `absent`. A function nobody has looked for evidence of is unassessed, not missing — and recording it as absent generates remediation work for a control that may already exist. Name the unblocking datum: the artifact or owner interview that would place the function on the scale.

## Verification

- [ ] Scope and the user-confirmed framework version are stated (or flagged open).
- [ ] Findings are organized under GOVERN, MAP, MEASURE, MANAGE.
- [ ] No specific category/subcategory identifiers, section numbers, or numeric thresholds are invented.
- [ ] Maturity is rated with a transparent scale, not a fabricated normative score.
- [ ] No "compliant/certified" verdict is issued — it is framed as voluntary maturity.
- [ ] Gaps are ranked by significance and effort with proposed actions.
- [ ] Functions with no evidence gathered are marked INSUFFICIENT EVIDENCE, not `absent`, with the artifact or interview that would resolve them named.

## False-Positive Prevention

❌ **DON'T:**
- Cite a specific subcategory identifier (e.g., "GOVERN 1.1 requires…") from memory — identifiers and their text must be verified against the official source.
- Treat the AI RMF as a binding legal standard or issue a "compliant" verdict — it is voluntary guidance.
- Conflate MEASURE (analyzing/tracking risk) with MANAGE (treating/responding to risk).
- Invent a maturity score from the framework when it does not prescribe one.

✅ **DO:**
- Describe category areas generically and flag any specific identifier as "verify against the current official source."
- Frame the deliverable as a maturity assessment, not a compliance pass/fail.
- Keep the four functions distinct and map evidence to the right one.
- Use a transparent, self-defined maturity scale with explicit rationale.

## Example Output

```markdown
## NIST AI RMF Maturity Assessment: Fraud-Scoring Service

### Scope & Framework Version
Scope: single production model + its governance. Version: user-confirmed (current edition). Open: whether a sector profile also applies — verify.

### Function Summary Table
| Function | Maturity | Rationale |
|---|---|---|
| GOVERN | Partial | Policy exists; accountability roles undocumented |
| MAP | Defined | Intended use, stakeholders, and risk context documented |
| MEASURE | Partial | Performance metrics tracked; fairness/robustness measures incomplete |
| MANAGE | Absent | No formal treatment/monitoring workflow for identified risks |

### Per-Function Detail
**GOVERN** — Areas: policy, roles, oversight. Evidence: AI policy v2. Gap: no named risk owner; escalation path undefined.
**MAP** — Areas: context, stakeholders, impact categorization. Evidence: impact assessment doc. Gap: third-party data risks not mapped.
**MEASURE** — Areas: metrics, validity, trustworthiness traits. Evidence: accuracy/latency dashboards. Gap: no per-group performance or drift measurement.
**MANAGE** — Areas: prioritization, treatment, monitoring, response. Evidence: none. Gap: no tripwires or response plan.

### Ranked Gaps & Actions
1. Establish risk treatment + monitoring workflow (high × moderate) — owner: ML platform.
2. Add per-group performance + drift measurement (high × moderate) — owner: DS.
3. Document accountability roles and escalation (moderate × low) — owner: governance.

### Verification Notes
Any reference to specific category identifiers must be verified against the current official source before publication.
```

**Techniques Used:**
- **DS-01 (Framework Application):** structures the assessment against the four AI RMF functions and their category areas.
- **ST-02 (Structured Sequential Instructions):** scope → GOVERN → MAP → MEASURE → MANAGE → rate → rank.
- **DS-06 (Prioritization & Severity Guidance):** ranks gaps by significance and effort.
- **QA-12 (False Positives Identification):** prevents fabricated identifiers and premature compliance verdicts.
- **RP-02 (Output Format Specification):** locks the function summary table and per-function structure.

**Related Prompts:**
- `rai_governance_framework_design.md` — turn GOVERN-function gaps into an internal framework.
- `rai_eu_ai_act_compliance_assessment.md` — pair voluntary maturity with binding-regulation assessment.
- `rai_model_risk_assessment.md` — the risk assessment feeding MAP/MEASURE evidence.
