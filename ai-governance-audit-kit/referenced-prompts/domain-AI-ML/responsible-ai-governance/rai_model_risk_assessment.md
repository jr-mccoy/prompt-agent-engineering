---
title: "RAI Model Risk Assessment"
category: AI-ML/responsible-ai-governance
description: "Assess an AI model's risk by enumerating failure modes, scoring harm severity × likelihood, identifying affected populations, and mapping controls — grounded in evidence rather than speculative or aggregate reassurance."
techniques:
  - RT-02
  - DS-06
  - QA-12
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - risk-assessment
  - failure-modes
  - harm-severity
  - controls
  - responsible-ai
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_red_teaming_plan.md
  - domain-AI-ML/responsible-ai-governance/rai_governance_framework_design.md
  - domain-AI-ML/responsible-ai-governance/rai_bias_detection_audit.md
---

# RAI Model Risk Assessment

**Objective:** Assess an AI model's risk by enumerating concrete failure modes, scoring each by harm severity × likelihood, naming who is affected, and mapping existing and needed controls — producing a ranked risk register that distinguishes evidenced risks from hypothesized ones and ties residual risk to a decision.

**When to Use:**
- Before deployment or a major change, as the risk gate in a governance process.
- When prioritizing safety/fairness/robustness work under limited time.
- When a risk register exists but lacks evidence or controls mapping.

**When NOT to Use:**
- To assess regulatory classification — use `rai_eu_ai_act_compliance_assessment.md`.
- To design adversarial tests — use `rai_red_teaming_plan.md` (this assessment may call for one).

## Inputs / Context

- **System & decision** — what the model does, the stakes, the autonomy level, who is affected.
- **Known performance** — aggregate and per-group metrics, calibration, robustness results if any.
- **Operating environment** — data drift exposure, adversarial exposure, dependency on upstream systems.
- **Existing controls** — human oversight, monitoring, fallbacks, rollback, access controls.
- **Risk appetite / framework** — the org's tolerance and any reference framework (ask the user).

## Constraints

**Must:**
- Enumerate concrete, model-specific failure modes (not generic "model could be wrong").
- Score each by severity (worst-case harm) and likelihood, and name the affected population per failure mode.
- Map each material risk to existing controls and identify the residual risk and any control gaps.

**Must Not:**
- Treat good aggregate accuracy as evidence of low risk — high-severity tail and per-group failures matter more than the mean.
- Assert a likelihood number with false precision; use bands and state the basis (evidence vs estimate).
- Fabricate incident statistics or regulatory risk thresholds; mark unknowns as unknown and ask the user for any required threshold.

**Instructions:**

1. **Frame the harm surface.** State the decision, stakes, autonomy, and the populations who bear the consequences of each error direction.

2. **Enumerate failure modes.** List specific ways the model fails: systematic errors, per-group disparities, calibration failures, distribution-shift degradation, adversarial manipulation, automation/over-reliance, and upstream-dependency failures.

3. **Score severity and likelihood.** For each failure mode, rate worst-case harm severity and likelihood (banded), noting whether the rating is evidence-based or estimated, and name the affected population.

4. **Distinguish evidenced from hypothesized.** Separate failure modes you have observed/measured from those that are plausible but untested — and recommend tests (e.g., a red-team) for the latter.

5. **Map controls and residual risk.** For each material risk, list existing controls, judge their effectiveness, and state the residual risk after controls.

6. **Rank the register.** Order by severity × likelihood × population, surfacing the high-severity items even when likelihood is low.

7. **Recommend treatment and a decision.** For top risks, recommend mitigate/monitor/accept/avoid, and tie residual risk to a go/conditional-go/no-go recommendation under the stated appetite.

8. **Define monitoring tripwires.** Specify the metrics and thresholds whose breach reopens the assessment.

**Output Format:**

A markdown risk register:
- **Harm Surface** — decision, stakes, autonomy, affected populations.
- **Risk Register** — table: Failure mode | Severity | Likelihood (band) | Affected population | Evidence vs estimate | Existing controls | Residual risk.
- **Top Risks (ranked)** — detail + recommended treatment.
- **Open Tests Needed** — for hypothesized risks (e.g., red-team, bias audit).
- **Decision Recommendation** — go / conditional / no-go under appetite.
- **Monitoring Tripwires**.
- **INSUFFICIENT EVIDENCE** — an enumerated likelihood band, distinct from `Low`. A hypothesized failure mode nobody has tested for is unquantified, not improbable, and collapsing the two is how untested risks leave the register. Pair each with the specific test from Open Tests Needed that would move it to a real band.

## Verification

- [ ] Failure modes are specific to this model, not generic.
- [ ] Each risk has severity, likelihood band, and named affected population.
- [ ] Evidenced risks are separated from hypothesized ones with tests proposed.
- [ ] Each material risk maps to controls and a residual-risk statement.
- [ ] High-severity/low-likelihood risks are surfaced, not buried by the mean.
- [ ] No fabricated likelihood precision, incident stats, or thresholds.
- [ ] Untested failure modes carry an INSUFFICIENT EVIDENCE likelihood tied to a named test, rather than being banded Low by default.

## False-Positive Prevention

❌ **DON'T:**
- Conclude "low risk" because overall accuracy is 95% — the 5% may concentrate catastrophic, per-group, or adversarial failures.
- Assign a precise likelihood (e.g., "0.3%") with no basis.
- List only failure modes you've already tested, ignoring plausible untested ones.
- Claim controls reduce risk without judging their actual effectiveness.

✅ **DO:**
- Weight high-severity tail and per-group failures over the mean.
- Use likelihood bands and state evidence vs estimate.
- Flag untested-but-plausible risks and route them to testing.
- Judge control effectiveness and report residual risk explicitly.

## Example Output

```markdown
## Model Risk Assessment: Triage Chatbot v2 (assistive, human-in-loop)

### Harm Surface
Suggests urgency level to a nurse; nurse decides. Autonomy: advisory. Affected: patients (esp. atypical presentations) and clinicians (over-reliance).

### Risk Register
| Failure mode | Severity | Likelihood | Affected | Evidence/Est | Controls | Residual |
|---|---|---|---|---|---|---|
| Under-triages atypical chest pain | Critical | Low–Med | Atypical patients | Estimate (untested) | Nurse override | Med — needs test |
| Per-group recall gap (limited-English) | High | Med | LEP patients | Evidenced (audit) | None | High |
| Over-reliance erodes nurse scrutiny | High | Med | All patients | Estimate | Training only | Med-High |
| Degrades after seasonal shift | Med | Med | All | Evidenced (drift) | Monitoring | Low-Med |

### Top Risks (ranked)
1. **LEP recall gap (High/Med, evidenced).** Treatment: mitigate (bias mitigation + human review for LEP) before scale.
2. **Atypical under-triage (Critical/Low-Med, untested).** Treatment: red-team before deployment.

### Open Tests Needed
Red-team on atypical/edge presentations; LEP-specific evaluation.

### Decision Recommendation
Conditional-go: pilot with LEP human-review safeguard; full deploy gated on red-team + LEP audit closure.

### Monitoring Tripwires
Per-group recall gap CI upper bound > 0.05; override rate drop > 20% (over-reliance signal).
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** risks across severity, likelihood, population, evidence.
- **DS-06 (Prioritization & Severity Guidance):** ranks the register and surfaces high-severity tails.
- **QA-12 (False Positives Identification):** blocks "accuracy = safe" and false-precision likelihoods.
- **CM-02 (Constraint Specification):** risk appetite as the decision constraint.
- **DS-02 (Metric Specification):** defines monitoring tripwire thresholds.

**Related Prompts:**
- `rai_red_teaming_plan.md` — test the hypothesized high-severity risks.
- `rai_governance_framework_design.md` — the gate this assessment feeds.
- `rai_bias_detection_audit.md` — evidence for per-group failure modes.
