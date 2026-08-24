---
title: "RAI Model Risk Management (SR 11-7)"
category: AI-ML/responsible-ai-governance
description: "Assess a model's governance against banking Model Risk Management principles — robust development/implementation/use, effective validation with independent effective challenge, and sound governance/policies/controls, plus model inventory and ongoing monitoring — without inventing regulatory citations, capital figures, or deadlines."
techniques:
  - DS-01
  - ST-02
  - DS-06
  - QA-12
  - CM-02
difficulty: advanced
tags:
  - model-risk-management
  - sr-11-7
  - model-validation
  - effective-challenge
  - responsible-ai
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_model_risk_register.md
  - domain-AI-ML/responsible-ai-governance/rai_fair_lending_ecoa_assessment.md
  - domain-AI-ML/responsible-ai-governance/rai_governance_framework_design.md
---

# RAI Model Risk Management (SR 11-7)

**Objective:** Assess a model's governance against banking Model Risk Management (MRM) principles — the three pillars of robust model development/implementation/use, effective validation (including independent "effective challenge"), and sound governance/policies/controls, plus the model inventory and ongoing monitoring — while requiring the user (and compliance) to confirm the applicable regulator/version and without inventing specific regulatory citations, capital figures, or deadlines.

**When to Use:**
- To structure a model-governance self-assessment at a financial institution against MRM principles.
- To prepare materials for an independent model-validation function or internal audit.
- To map existing development, validation, and governance artifacts onto the three MRM pillars.

**When NOT to Use:**
- As legal or compliance advice — this is a structured pre-assessment; route conclusions to compliance/MRM.
- As a substitute for an independent model-validation function or qualified compliance staff.
- For fair-lending analysis specifically — that is a distinct discipline; use the fair-lending assessment.

## Inputs / Context

- **Model description** — purpose, materiality/risk rating, business use, and consumers of its output.
- **Development artifacts** — design rationale, data, assumptions, testing, implementation evidence.
- **Validation status** — whether independent validation occurred, by whom, and findings.
- **Governance** — policies, roles, model owner, inventory entry, change control, monitoring.
- **Ongoing monitoring** — performance tracking, override tracking, benchmarking, escalation.
- **User-confirmed regime** — applicable regulator and supervisory-guidance version (ask; do not assume).

## Constraints

**Must:**
- Organize the assessment around the three MRM pillars plus inventory and ongoing monitoring.
- Treat "effective challenge" as requiring genuine independence and competence — assess it, don't assume it.
- Separate evidenced controls from gaps and route conclusions to the MRM/compliance function.

**Must Not:**
- NO-FABRICATION: never invent specific regulatory citations, supervisory-guidance section numbers, regulatory text, numeric thresholds, capital figures, dollar amounts, or deadlines from memory; the user confirms the applicable regulator and version; map the model to the guidance's STRUCTURE and principles at a conceptual level and explicitly flag any specific citation, figure, or threshold as "verify against the current official source."
- Declare the model "validated," "compliant," or "approved" — produce a gap assessment and route to MRM/compliance.
- Assume which regulator applies; confirm with the user.

**Instructions:**

1. **Confirm regime and materiality.** Establish the applicable regulator/version and the model's materiality/risk rating. Mark unknowns as open questions.

2. **Assess Pillar 1 — development, implementation, use.** Evaluate design soundness, data and assumptions, conceptual rationale, testing, implementation controls, and appropriate use (including documented limitations). Note evidence and gaps.

3. **Assess Pillar 2 — validation & effective challenge.** Evaluate whether independent validation occurred, the competence and *independence* of the challenge, the scope (conceptual soundness, ongoing monitoring, outcomes analysis), and how findings were resolved.

4. **Assess Pillar 3 — governance, policies, controls.** Evaluate model ownership, roles and responsibilities, policies, change control, and escalation.

5. **Check the model inventory.** Confirm the model is in the inventory with required attributes (purpose, owner, validation status, risk rating) — described generically, not quoted.

6. **Assess ongoing monitoring.** Evaluate performance tracking, override/exception tracking, benchmarking, and tripwires for revalidation.

7. **Rank gaps and route to MRM.** Prioritize gaps by significance × model materiality and effort; mark items needing compliance/validation interpretation.

**Output Format:**

A markdown MRM assessment:
- **Regime & Materiality** — regulator/version, model risk rating, open questions.
- **Pillar 1 — Development/Implementation/Use** — evidence | gaps.
- **Pillar 2 — Validation & Effective Challenge** — independence, scope, findings resolution | gaps.
- **Pillar 3 — Governance/Policies/Controls** — evidence | gaps.
- **Model Inventory & Ongoing Monitoring** — present/missing attributes; monitoring gaps.
- **Ranked Gaps & MRM Handoff** — significance × materiality × effort.

## Verification

- [ ] Applicable regulator/version and model materiality are confirmed (or flagged open).
- [ ] All three pillars plus inventory and monitoring are assessed.
- [ ] "Effective challenge" is assessed for genuine independence and competence, not assumed.
- [ ] No regulatory citations, capital figures, numeric thresholds, or deadlines are invented.
- [ ] Each pillar separates evidence-present from gap.
- [ ] No "validated/compliant/approved" verdict is issued — routed to MRM/compliance.

## False-Positive Prevention

❌ **DON'T:**
- Cite a specific supervisory-guidance section, capital figure, or revalidation deadline from memory — these must be verified against the current official source.
- Treat developer self-review or a same-team check as "effective challenge" — it must be genuinely independent and competent.
- Conflate model performance monitoring (an MRM ongoing-monitoring activity) with fair-lending disparity analysis (a separate discipline).
- Declare a model "validated" or "compliant" because documentation exists — substance and independence matter.

✅ **DO:**
- Organize around the three pillars plus inventory and ongoing monitoring.
- Scrutinize the independence and competence of the effective-challenge function.
- Scale gap severity to the model's materiality/risk rating.
- Route all conclusions and any figures to MRM/compliance for verification against the current official source.

## Example Output

```markdown
## Model Risk Management Assessment: Deposit-Attrition Model

### Regime & Materiality
Regulator/version: user-confirmed. Model risk rating: high (drives retention spend). Open: whether a parallel consumer-protection review is needed — verify.

### Pillar 1 — Development/Implementation/Use
Evidence: design doc, data lineage, backtest. Gaps: assumptions not stress-tested; documented use limits absent.

### Pillar 2 — Validation & Effective Challenge
Validation: performed by the development team. Gap: not independent — does not meet effective-challenge expectations; scope omitted outcomes analysis.

### Pillar 3 — Governance/Policies/Controls
Evidence: model owner named; change control in ticketing. Gap: no MRM policy mapping; escalation path undefined.

### Model Inventory & Ongoing Monitoring
Inventory: present but missing validation-status and risk-rating attributes. Monitoring: accuracy tracked; no override tracking or revalidation tripwire.

### Ranked Gaps & MRM Handoff
1. Independent validation / effective challenge (critical × high) — MRM function.
2. Documented use limits + assumption stress-testing (high × moderate) — model owner.
3. Inventory attribute completion + revalidation tripwire (moderate × low) — governance.
Route all to MRM/compliance for verification against the current official source.
```

**Techniques Used:**
- **DS-01 (Framework Application):** structures the review against the three MRM pillars plus inventory and monitoring.
- **ST-02 (Structured Sequential Instructions):** regime → Pillar 1 → Pillar 2 → Pillar 3 → inventory/monitoring → handoff.
- **DS-06 (Prioritization & Severity Guidance):** scales gap severity to model materiality and effort.
- **QA-12 (False Positives Identification):** prevents fabricated citations and rubber-stamp "effective challenge."
- **CM-02 (Constraint Specification):** the no-invented-regulatory-text constraint governs the analysis.

**Related Prompts:**
- `rai_model_risk_register.md` — the inventory/register feeding the model-inventory assessment.
- `rai_fair_lending_ecoa_assessment.md` — the distinct fair-lending discipline, separate from MRM.
- `rai_governance_framework_design.md` — turn Pillar 3 gaps into an internal governance framework.
