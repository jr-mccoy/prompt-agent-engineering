---
title: "Feasibility & Risk Assessment"
category: AI-ML/problem-framing-scoping
description: "Pressure-test technical feasibility and surface the risks of an ML initiative — data, modeling, deployment, and harm — before resources are committed."
techniques:
  - ST-02
  - RT-02
  - DS-06
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - feasibility
  - risk-assessment
  - pre-mortem
  - deployment-risk
  - problem-framing
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/problem-framing-scoping/mlframe_data_readiness_assessment.md
  - domain-AI-ML/problem-framing-scoping/mlframe_cost_of_being_wrong_analysis.md
  - domain-AI-ML/problem-framing-scoping/mlframe_build_buy_finetune_decision.md
---

# Feasibility & Risk Assessment

**Objective:** Before committing resources, evaluate whether an ML initiative is technically feasible and surface its risks across data, modeling, deployment/serving, and harm/governance — producing a ranked risk register with mitigations and an overall feasibility verdict.

**When to Use:**
- At a go/no-go gate before staffing an ML project.
- When optimism is high and a structured pre-mortem is needed.
- When stakeholders ask "what could go wrong?" and need more than a hand-wave.

**When NOT to Use:**
- You only need the data side (use `mlframe_data_readiness_assessment.md`).
- You need to quantify asymmetric error costs (use `mlframe_cost_of_being_wrong_analysis.md`).

## Inputs / Context

Provide what you can:
- **The use case** — task, target, decision it drives.
- **Data situation** — availability, labels, quality (or note `mlframe_data_readiness_assessment.md` output).
- **Performance bar** — the metric and threshold needed for value.
- **Deployment context** — latency/throughput, online vs batch, where it runs.
- **Team & timeline** — skills, headcount, deadline.
- **Stakes** — consequence of failure or harmful errors; regulatory exposure.

## Constraints

**Must:**
- Cover four risk categories: data, modeling/performance, deployment/operations, and harm/governance.
- Score each risk by likelihood × impact and attach a concrete mitigation or a test that resolves the uncertainty.
- Distinguish risks that can be retired by an experiment from ones that are structural blockers.

**Must Not:**
- Invent likelihood percentages, latency numbers, or accuracy ceilings — express uncertainty qualitatively or as "to test."
- Treat feasibility as a single yes/no without showing the dominant risks behind it.
- Omit harm/governance risk for high-stakes use cases.

**Instructions:**

1. **Restate the bar feasibility is judged against.** Name the metric/threshold, latency, and scale the system must hit to deliver value. Feasibility is relative to this bar.

2. **Surface data risks.** Sufficiency, representativeness, label noise, drift potential, and pipeline fragility — pulling from a data-readiness output if available.

3. **Surface modeling/performance risks.** Whether the achievable accuracy plausibly clears the bar, signal-to-noise ceiling, leakage temptation, and overfitting/validation risks.

4. **Surface deployment/operations risks.** Latency/throughput feasibility, train/serve skew, monitoring and retraining burden, dependency and integration risk.

5. **Surface harm/governance risks.** Fairness exposure across groups, regulatory requirements, explainability needs, privacy, and the consequence of confident wrong answers.

6. **Score and identify retirable uncertainties.** Rate each risk likelihood × impact; mark which can be retired cheaply by a spike/experiment versus which are structural blockers.

7. **Render the feasibility verdict and the de-risking plan.** Give FEASIBLE / FEASIBLE-WITH-MITIGATION / INFEASIBLE-NOW, the top risks driving it, and the experiments that would most cheaply reduce uncertainty.

**Output Format:**

A markdown feasibility brief:
- **Verdict** — FEASIBLE / FEASIBLE-WITH-MITIGATION / INFEASIBLE-NOW + rationale.
- **Performance Bar** — metric/threshold/latency/scale feasibility is judged against.
- **Risk Register** — table: Risk | Category | Likelihood | Impact | Mitigation / Test | Retirable?
- **Top Risks Driving the Verdict** — ranked.
- **De-Risking Plan** — cheapest experiments to retire the biggest uncertainties first.
- **INSUFFICIENT EVIDENCE** — a fourth verdict, for the case where the performance bar itself is unstated or unagreed. Feasibility is meaningless without the bar it is judged against, so an assessment run before one exists is measuring nothing. Name the unblocking datum: the metric, threshold, latency, and scale the system must meet, and who owns that number.

## Verification

- [ ] All four risk categories are covered (data, modeling, deployment, harm/governance).
- [ ] Each risk has likelihood × impact and a concrete mitigation or resolving test.
- [ ] Retirable-by-experiment risks are separated from structural blockers.
- [ ] The verdict is justified by the top-ranked risks.
- [ ] No likelihood/latency/accuracy figure is fabricated; uncertainties are marked "to test."
- [ ] Where the performance bar is unstated or unagreed, the verdict is INSUFFICIENT EVIDENCE naming the bar and its owner — feasibility is not judged against an assumed threshold.

## False-Positive Prevention

❌ **DON'T:**
- Declare a project feasible because the data exists, ignoring whether achievable accuracy clears the value bar.
- Assume offline performance will hold in production — train/serve skew and drift are deployment risks, not afterthoughts.
- Skip fairness/governance risk on a high-stakes decision because the model "is just a recommendation."
- Attach made-up probabilities to risks to seem rigorous.

✅ **DO:**
- Judge feasibility against the *value bar*, not against beating a trivial baseline.
- List the cheap spikes (a leakage check, a small labeled pilot, a latency benchmark) that retire the biggest unknowns first.
- Treat confident-wrong-answer consequences as a first-class risk for any decision affecting people.
- Express uncertainty honestly as qualitative or "to test" rather than inventing numbers.

## Example Output

```markdown
## Feasibility & Risk: Automated Resume Screening

### Verdict
FEASIBLE-WITH-MITIGATION — technically buildable, but governance/fairness risk dominates and
must be controlled before deployment.

### Performance Bar
Must surface qualified candidates with precision ≥ recruiter baseline, p95 < 1s, batch nightly OK.

### Risk Register
| Risk | Category | Likelihood | Impact | Mitigation / Test | Retirable? |
|---|---|---|---|---|---|
| Labels encode historical hiring bias | Harm/Gov | High | Severe | Audit slices; reweight; legal review | Partly (test) |
| Proxy label (was-hired ≠ good-hire) | Data | High | High | Define better target; outcome labels | Yes (relabel pilot) |
| Achievable lift over recruiter is thin | Modeling | Med | High | Small labeled pilot vs recruiter | Yes (spike) |
| Train/serve text-parsing skew | Deployment | Med | Med | Shared parsing code path | Yes (integration test) |

### Top Risks Driving the Verdict
1. Bias in historical labels (regulatory + ethical) — gating.
2. Proxy-label validity — caps real value.

### De-Risking Plan
Run a 300-resume labeled pilot with fairness slices and a recruiter-comparison before any build
commitment; engage legal on protected-attribute exposure first.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** walks the four risk categories in sequence.
- **RT-02 (Multi-Dimensional Analysis Framework):** likelihood × impact across categories.
- **DS-06 (Prioritization & Severity Guidance):** ranks risks and orders de-risking experiments.
- **CM-02 (Constraint Specification):** the value bar and latency are binding feasibility constraints.
- **QA-12 (False Positives Identification):** guards against "data exists ⇒ feasible" optimism.

**Related Prompts:**
- `mlframe_data_readiness_assessment.md` — supplies the data-risk inputs.
- `mlframe_cost_of_being_wrong_analysis.md` — quantifies the harm-risk dimension.
- `mlframe_build_buy_finetune_decision.md` — sourcing choice changes the deployment risk profile.
