---
title: "Operational-Risk Control Self-Assessment (RCSA) with KRIs"
category: finance/risk-management
description: "Run an operational-risk RCSA that maps processes to risks and controls, scores inherent vs. residual risk on calibrated likelihood × impact scales, assesses control design and operating effectiveness, and attaches key risk indicators with action thresholds."
techniques:
  - RT-02
  - DS-06
  - DT-02
  - OC-01
  - QA-01
difficulty: intermediate
tags:
  - operational-risk
  - rcsa
  - controls
  - kri
  - likelihood-impact
  - governance
updated: "2026-06-08"
related_prompts:
  - domain-finance/risk-management/finance_enterprise_risk_register.md
  - domain-finance/risk-management/finance_model_risk_validation.md
  - domain-finance/risk-management/finance_tail_risk_premortem.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, audit, or risk-management advice. RCSA outputs must be validated by qualified risk and control professionals.*

## Objective

Conduct a Risk and Control Self-Assessment (RCSA) for a defined process or unit: decompose the process into steps, identify operational risks (people, process, systems, external events) per step, score inherent likelihood × impact, catalog and rate controls (design adequacy and operating effectiveness), derive residual risk, and attach key risk indicators (KRIs) with thresholds that trigger action. Every score carries a stated basis; no loss data is invented.

## When to Use

- First-line RCSA for a business process, function, or product
- Pre-launch operational-risk review of a new process or system
- Refreshing controls after an incident, audit finding, or near-miss
- Standardizing operational risk inputs into the enterprise risk register
- Designing a KRI dashboard for ongoing monitoring

## Inputs / Context Required

- **Process scope:** The process/unit, its objective, and key steps (or source material to decompose).
- **Risk taxonomy:** Basel-style operational categories (internal/external fraud, employment practices, clients/products/business practices, damage to physical assets, business disruption/systems, execution/delivery/process management) or a custom taxonomy.
- **Existing controls:** Preventive/detective/corrective controls, manual vs. automated, owners.
- **Loss / incident history:** Past events, near-misses, frequencies — if available. State if none.
- **Scoring scales:** Likelihood and impact definitions, or accept the proposed 5×5 scales.
- **KRI data sources:** Available metrics that could serve as leading/lagging indicators.

## Constraints

### Must
- Decompose the process before scoring; risks attach to specific steps.
- Score inherent (pre-control) and residual (post-control) risk separately as `Likelihood × Impact`.
- Rate each control on two axes: design adequacy and operating effectiveness.
- State the basis for each score (loss data / incident history / expert judgment) and mark judgment-based scores.
- Attach at least one KRI to each high/critical residual risk, with a defined threshold and escalation path.
- Distinguish preventive, detective, and corrective controls.

### Must Not
- Invent loss frequencies or amounts; mark gaps `[ASSUMED]` and keep them out of quantitative conclusions.
- Lower residual below inherent without naming the specific effective control.
- Treat a documented control as effective without an operating-effectiveness assessment.
- Score risk for the process as a whole instead of at the step/risk level.
- Present a KRI without a threshold and an owner.

## Instructions

1. **Decompose the process (NE-10 / DT-02).** Break the process into discrete steps; note handoffs, system dependencies, and manual touchpoints (common failure points).
2. **Identify risks per step.** For each step, list operational risks by taxonomy category in cause → event → consequence form.
3. **Score inherent risk.** Rate likelihood and impact pre-control on the confirmed scales:
   ```
   Inherent score = Likelihood (1–5) × Impact (1–5)   → 1–25
   ```
   Record basis (data / history / judgment).
4. **Catalog controls.** For each risk, list controls; classify preventive / detective / corrective and manual / automated; name the control owner.
5. **Assess control effectiveness (RT-02 / QA-01).**
   - **Design adequacy:** Would the control, if operating, address the risk? (Adequate / Partially / Inadequate)
   - **Operating effectiveness:** Is it actually operating as designed? (Effective / Partially / Ineffective — basis: testing, evidence, judgment)
   A control reduces residual risk only to the extent it is both well-designed and operating.
6. **Score residual risk.** Re-rate likelihood/impact reflecting effective controls; compute residual score. Flag risks where residual ≈ inherent (controls add no value).
7. **Define KRIs.** For high/critical residuals, specify a leading or lagging indicator, a green/amber/red threshold, frequency, and escalation owner.
   ```
   KRI threshold example: failed-trade rate > 2% (amber) / > 5% (red) → escalate to [owner]
   ```
8. **Disconfirming check.** Challenge "effective" ratings: is effectiveness asserted or evidenced? Re-rate controls supported only by assertion. Name optimism bias in self-assessment.
9. **Prioritize.** Rank residual risks; produce an action list for inadequate/ineffective controls.

## Output Format

### Process Decomposition
| Step | Description | System(s) | Manual touchpoint? | Handoff? |
|---|---|---|---|---|

### RCSA Matrix
| ID | Step | Risk (cause → event → consequence) | Category | Inh. L | Inh. I | Inherent | Controls (type) | Design | Op. Effectiveness | Res. L | Res. I | Residual | Owner | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OR-01 | … | … | Execution | 4 | 4 | 16 | Recon (detective, manual) | Adequate | Partially | 3 | 4 | 12 | [role] | history |

### Control Effectiveness Summary
| Control | Type | Design | Operating | Evidence basis | Gap / action |
|---|---|---|---|---|---|

### KRI Dashboard
| Risk ID | KRI | Green | Amber | Red | Frequency | Escalation owner |
|---|---|---|---|---|---|---|

### Prioritized Actions
| Rank | Risk ID | Residual | Issue | Remediation | Owner | Due |
|---|---|---|---|---|---|---|

## Verification

- [ ] The process is decomposed into steps before risks are scored.
- [ ] Each risk is stated as cause → event → consequence at the step level.
- [ ] Inherent and residual scores both shown as `L × I`; residual reductions name an effective control.
- [ ] Each control is rated on design adequacy AND operating effectiveness.
- [ ] Score bases are tagged; judgment-based scores are marked.
- [ ] No loss frequencies/amounts are invented; gaps `[ASSUMED]` and excluded from conclusions.
- [ ] High/critical residuals each have a KRI with thresholds and an escalation owner.
- [ ] The disconfirming pass challenges asserted-but-unevidenced "effective" ratings.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Documented control assumed effective | Operating-effectiveness rating with an evidence basis required; assertion-only ratings re-challenged |
| Self-assessment optimism inflating control quality | Disconfirming pass; name optimism bias; require evidence over assertion |
| Residual = inherent passed as controlled | Flag risks where controls produce no reduction as effectively uncontrolled |
| Inventing incident frequencies | Loss data must be user-supplied; `[ASSUMED]` placeholders barred from quantitative conclusions |
| KRI without an action trigger | Every KRI carries thresholds, frequency, and an escalation owner |
| Scoring the whole process at once | Risks must attach to specific steps; aggregate-only scoring rejected |
| Detective control credited as if preventive | Control type classified; detective controls reduce impact/duration, not occurrence |
