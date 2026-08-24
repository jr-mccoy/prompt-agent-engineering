---
title: "Enterprise Risk Register Builder — Likelihood × Impact, Owners, Treatment"
category: finance/risk-management
description: "Build an auditable enterprise risk register that scores each risk on calibrated likelihood and impact scales, computes inherent vs. residual exposure, assigns owners and treatment strategies, and surfaces the top risks on a heat map — without inventing probabilities."
techniques:
  - RT-02
  - DS-06
  - DT-02
  - OC-01
  - QA-01
difficulty: intermediate
tags:
  - enterprise-risk
  - risk-register
  - heat-map
  - risk-appetite
  - controls
  - governance
updated: "2026-06-08"
related_prompts:
  - domain-finance/risk-management/finance_operational_risk_rcsa.md
  - domain-finance/risk-management/finance_tail_risk_premortem.md
  - domain-finance/risk-management/finance_stress_test_scenario_design.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, investment, or risk-management advice. All outputs must be reviewed by qualified risk professionals before use in any decision.*

## Objective

Construct a defensible enterprise risk register that, for each identified risk, captures: a clear risk statement (cause → event → consequence), inherent likelihood and impact on calibrated scales, the controls in place, residual likelihood and impact after controls, a named owner, a treatment strategy (avoid / reduce / transfer / accept), and a status. The register rolls up into a likelihood × impact heat map and a top-risk list ranked by residual exposure, with every score traceable to a stated rationale rather than an invented probability.

## When to Use

- Standing up or refreshing an enterprise risk management (ERM) program
- Quarterly or annual board / audit-committee risk reporting
- Pre-deal, pre-financing, or pre-product-launch risk inventory
- Consolidating siloed departmental risk logs into one enterprise view
- Establishing a baseline before designing controls or stress tests

## Inputs / Context Required

- **Entity & scope:** Organization, business unit(s), and time horizon (e.g., 12-month rolling).
- **Risk universe / categories:** Strategic, financial, operational, compliance/legal, technology/cyber, reputational, ESG — or a custom taxonomy. List candidate risks if known.
- **Scoring scales:** Existing likelihood and impact definitions if the entity has them; otherwise the model proposes calibrated 5×5 scales for confirmation.
- **Risk appetite / tolerance:** Stated appetite per category, or thresholds (e.g., "no single risk above $X impact uncapped").
- **Existing controls:** Known mitigations, insurance, and their assessed effectiveness.
- **Owners:** Functions or roles accountable for each category.
- **Impact units:** Financial ($ ranges), and any non-financial dimensions (safety, regulatory, customer, brand).

## Constraints

### Must
- Define likelihood and impact scales explicitly (anchored levels) before scoring any risk.
- Write each risk as cause → event → consequence, not a one-word label.
- Score inherent (before controls) and residual (after controls) separately; show both.
- Compute exposure as Likelihood × Impact score and rank by residual exposure.
- Assign one accountable owner per risk (a role, not "the team").
- State the basis for each likelihood and impact rating (data, history, expert judgment) and mark judgment-based scores.
- Map residual exposure against stated risk appetite; flag breaches.

### Must Not
- Invent probabilities, loss frequencies, or impact figures the user has not supplied or that cannot be reasoned from stated facts; mark gaps `[ASSUMED]`.
- Present a residual score lower than inherent without naming the specific control that reduces it.
- Collapse likelihood and impact into a single number without showing both components.
- Treat the register as static — every risk must carry a review date and status.
- Declare a risk "mitigated" when only a treatment plan (not an implemented control) exists.

## Instructions

1. **Confirm scales.** Present calibrated 5×5 scales and have the user confirm or amend. Default anchors:
   ```
   Likelihood: 1 Rare (<10%/yr) · 2 Unlikely (10–30%) · 3 Possible (30–50%)
               4 Likely (50–75%) · 5 Almost Certain (>75%)
   Impact:     1 Insignificant · 2 Minor · 3 Moderate · 4 Major · 5 Severe
               (each tied to $ bands + non-financial anchors supplied by user)
   Exposure score = Likelihood × Impact   (range 1–25)
   ```
2. **Enumerate the risk universe.** For each category, list candidate risks. For each, draft the cause → event → consequence statement.
3. **Score inherent risk.** Rate likelihood and impact pre-control. Record the rationale and basis (`data` / `history` / `judgment`). Compute inherent exposure.
4. **Inventory controls.** For each risk, list existing controls and assess effectiveness (strong / moderate / weak). Insurance and transfer count as controls.
5. **Score residual risk.** Re-rate likelihood and/or impact reflecting control effectiveness. A control that lowers frequency moves likelihood; one that caps severity moves impact. Compute residual exposure.
6. **Assign owner and treatment.** Choose treatment: Avoid, Reduce (add/strengthen controls), Transfer (insure/contract), Accept (within appetite). Name the accountable owner and any treatment actions with target dates.
7. **Test against appetite.** Compare each residual exposure to category appetite. Flag any risk above tolerance as a breach requiring escalation.
8. **Disconfirming check (RT-02 / QA-01).** Re-examine the lowest-scored risks: would a reasonable skeptic argue any is under-rated due to optimism, recency, or anchoring on the last incident? Re-score if warranted and note the change.
9. **Build heat map and top-risk list.** Plot residual scores on the 5×5 grid; list the top risks by residual exposure with owner, treatment, and status.

## Output Format

### Scoring Scales (confirmed)
| Scale | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Likelihood | Rare | Unlikely | Possible | Likely | Almost Certain |
| Impact ($ band) | [<$a] | [$a–b] | [$b–c] | [$c–d] | [>$d] |

### Risk Register
| ID | Risk (cause → event → consequence) | Category | Inh. L | Inh. I | Inh. Exp | Key Controls (effectiveness) | Res. L | Res. I | Res. Exp | Owner | Treatment | Basis | Appetite Breach? | Status / Review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R-01 | … | … | 4 | 5 | 20 | … (moderate) | 3 | 4 | 12 | [role] | Reduce | judgment | No | Open / [date] |

### Residual Heat Map (count of risks per cell)
| Impact ↓ / Likelihood → | 1 Rare | 2 Unlikely | 3 Possible | 4 Likely | 5 Almost Certain |
|---|---|---|---|---|---|
| 5 Severe | | | | | |
| 4 Major | | | | | |
| 3 Moderate | | | | | |
| 2 Minor | | | | | |
| 1 Insignificant | | | | | |

### Top Risks by Residual Exposure
| Rank | ID | Risk | Residual Exp | Owner | Treatment | Appetite Status |
|---|---|---|---|---|---|---|

### Appetite Breaches & Escalations
| ID | Residual Exp | Appetite Threshold | Gap | Required Action |
|---|---|---|---|---|

## Verification

- [ ] Likelihood and impact scales are defined with explicit anchors and confirmed before any scoring.
- [ ] Every risk is written as cause → event → consequence, not a label.
- [ ] Inherent and residual scores are both shown; residual reductions name a specific control.
- [ ] Every likelihood/impact score carries a stated basis; judgment-based scores are marked.
- [ ] No probabilities or impact figures appear that were not supplied or defensibly reasoned; gaps are `[ASSUMED]`.
- [ ] Each risk has exactly one accountable owner (a role).
- [ ] Residual exposures are compared to stated appetite; breaches are flagged.
- [ ] The disconfirming pass on low-scored risks was performed and any re-scores noted.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Presenting invented likelihoods as data | Require a basis tag (data/history/judgment); judgment scores cannot be cited as empirical probabilities |
| Residual scores lower than inherent with no real control | Residual reduction must name an implemented control and its effectiveness; planned-only controls keep inherent score |
| Treating a planned treatment as a completed mitigation | Status distinguishes "control in place" from "treatment planned"; only the former lowers residual |
| Optimism / recency bias deflating scores | Mandatory disconfirming pass on lowest-rated risks; re-score and document |
| One number hiding a low-likelihood / catastrophic-impact risk | Show L and I separately; severe-impact risks surface even at low likelihood on the heat map |
| Owner = "the company" / diffuse accountability | One named role per risk required; reject collective ownership |
| Static register presented as current | Every row carries a review date and status; stale rows are flagged |
