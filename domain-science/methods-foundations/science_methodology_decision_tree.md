---
title: "Methodology Decision Tree"
category: science/methods-foundations
description: "Route a research question to RCT, quasi-experiment, observational, simulation, or qualitative design via an explicit decision tree that surfaces each route's load-bearing assumption and validity cost."
techniques:
  - ST-01
  - ST-03
  - RT-03
  - CM-02
  - NE-10
  - QA-01
difficulty: advanced
tags:
  - study-design
  - rct
  - quasi-experiment
  - observational
  - causal-inference
  - simulation
  - decision-tree
  - internal-validity
updated: "2026-06-26"
related_prompts:
  - domain-science/methods-foundations/science_experimental_design_advisor.md
  - domain-science/methods-foundations/science_qualitative_vs_quantitative_decision.md
  - domain-science/methods-foundations/science_power_and_sample_size_calculator.md
  - domain-science/methods-foundations/science_pilot_study_designer.md
---

# Methodology Decision Tree

**Objective:** Route a research question to the most defensible design — randomized controlled trial, quasi-experiment (ITS, RDD, DiD, non-equivalent control group), observational study (cohort, case-control, cross-sectional), computational simulation / in-silico, or qualitative — using an explicit decision tree keyed on the causal vs descriptive goal, manipulability of the independent variable, ethics/feasibility of randomization, time structure, and available comparison groups. For each candidate route, surface the load-bearing assumption it buys and what it costs in validity.

**When to use:** Early in design, after the research question is articulated but before a method is committed. Precondition: you can state whether the goal is causal, predictive, or descriptive, and whether the key exposure/treatment is manipulable.

**Required inputs:**
- **Discipline.** <field, e.g. epidemiology, economics, education, ecology>
- **Study type.** <observational / experimental / computational / etc.> — or "undecided" if that is the question.
- **Research question.** Stated precisely, including the exposure/treatment and outcome.
- **Goal.** Causal effect / prediction / description / mechanism / theory-building.
- **Manipulability & ethics.** Can the independent variable be assigned, and is randomization ethical and feasible?

**Optional inputs:**
- Available data structure (cross-sectional, panel/longitudinal, time series, registry).
- Existence of a control/comparison group or a natural experiment / threshold / policy shock.
- Constraints (budget, time, sample, regulatory).
- Prior knowledge / mechanistic model (relevant to simulation).
- Stakeholder or evidence-grading requirement (e.g. GRADE, what counts as sufficient).

**Constraints — Must:**
- Produce an **explicit decision tree (or decision table)** with the branching criteria visible.
- Compare **multiple candidate routes** (Tree-of-Thoughts), not a single recommendation, and rank them.
- For each route, name its **load-bearing identifying assumption** and the **validity it trades** (internal vs external, threats it admits).
- Tie the recommendation to the goal: causal questions demand a credible identification strategy; descriptive questions do not.
- Distinguish **pre-specified confirmatory** designs from **exploratory** ones, and note where the design forces analysis pre-specification.
- Use calibrated language in drafted text.
- Default to an **Open Science** branch (pre-register the chosen design and analysis); closed-data only as a named non-default exception.

**Constraints — Must Not:**
- Do not invent citations, DOIs, effect sizes, prior-study parameters, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not default to "RCT is best" regardless of feasibility, ethics, or question type.
- Do not assert causation from an observational route without naming the unverifiable assumptions it rests on.
- Do not use "novel", "groundbreaking", "first-ever", or "gold standard" in drafted text.
- Do not present a single route as assumption-free; every route buys an assumption.

**Instructions:**

1. **Classify the goal.** Determine whether the question seeks a causal effect, prediction, description/frequency, or mechanism/theory. If it is about meaning/process-as-experienced, route to the qualitative-vs-quantitative prompt and say so.
2. **Test manipulability and ethics.** Decide whether the independent variable can be assigned by the researcher, and whether random assignment is ethical and feasible. This is the first major fork.
3. **Map the comparison and time structure.** Identify whether a control/comparison group exists, whether there is a natural experiment (threshold, policy shock, staggered rollout), and whether data are cross-sectional, panel, or time series. These determine which quasi-experimental designs are available.
4. **Enumerate candidate routes (Tree-of-Thoughts).** Generate the plausible designs given the above: RCT (incl. cluster/stepped-wedge); quasi-experiments — interrupted time series (ITS), regression discontinuity (RDD), difference-in-differences (DiD), non-equivalent control group (NECGD); observational — cohort, case-control, cross-sectional; simulation/in-silico; qualitative. Keep only feasible ones.
5. **Surface each route's load-bearing assumption.** For every retained route, state the identifying assumption it depends on (e.g. RCT: successful randomization + adherence; DiD: parallel trends; RDD: continuity at the cutoff + no manipulation; cohort: no unmeasured confounding / correct adjustment set; simulation: validated generative model and parameters) and the validity it trades.
6. **Score routes against criteria.** Build a comparison table rating each route on internal validity, external validity, feasibility/ethics, cost/time, and assumption credibility for *this* question.
7. **Recommend and justify with the tree path.** Select the top route, show the path through the tree that leads there, and name the runner-up and the condition under which you'd switch to it.
8. **Specify confirmatory vs exploratory and next steps.** State whether the design is confirmatory (pre-register) or exploratory, and route forward (power/sample-size, pilot, or qualitative design prompt) as appropriate.

**Output format (locked):**

```
## Question & Goal Classification
[research question | goal: causal/predictive/descriptive/mechanism | exposure & outcome]

## Decision Tree (branching criteria)
[manipulable IV? → ethical/feasible to randomize? → comparison group / natural experiment? → time structure? → leaf design(s)]
(render as an indented tree or a decision table)

## Candidate Routes Considered (Tree-of-Thoughts)
| Route | Feasible here? | Load-bearing assumption | Validity it trades |
|---|---|---|---|
[RCT | ITS | RDD | DiD | NECGD | cohort | case-control | cross-sectional | simulation | qualitative]

## Route Comparison
| Route | Internal validity | External validity | Feasibility/ethics | Cost/time | Assumption credibility (this Q) |
|---|---|---|---|---|---|

## Recommendation
[chosen route | tree path that reaches it | runner-up + switch condition]

## Confirmatory vs Exploratory & Next Steps
[pre-register? | route to power/pilot/qual-vs-quant prompt]

## Open-Data / Reproducibility Note
[Open Science default; closed-data exception only with justification]
```

**Reporting-standard alignment:** Match the chosen design to its reporting standard — **CONSORT** (RCTs), **TREND** (non-randomized interventions), **STROBE** (observational), **TRIPOD** (prediction models), **ARRIVE 2.0** (animal studies), and simulation reporting conventions (e.g. **TRACE / ODD** for agent-based and ecological models). For causal observational work, reference **GRADE** for evidence grading. Name the standard explicitly.

**Verification checklist (before delivering):**
- [ ] An explicit decision tree/table with visible branching criteria is present.
- [ ] Multiple candidate routes are compared and ranked (not a single foregone choice).
- [ ] Each route names its load-bearing identifying assumption and the validity it trades.
- [ ] The recommendation matches the goal (causal questions get a credible identification strategy).
- [ ] RCT is not asserted as universally best; ethics/feasibility forks are honored.
- [ ] No observational causal claim is made without naming its unverifiable assumptions.
- [ ] Confirmatory vs exploratory status is stated; next-step routing is given.
- [ ] A design-appropriate reporting standard is named; Open Science default present.
- [ ] No fabricated parameters/citations; gaps marked `[user-supplied]`; no banned hype terms.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| RCT reflex | Recommending an RCT for an unmanipulable or unethical-to-randomize exposure | Manipulability + ethics fork in Step 2; route to quasi/observational when randomization is impossible. |
| Hidden assumption | An observational route presented as if it cleanly identifies a causal effect | Require the load-bearing assumption (e.g. no unmeasured confounding) named per route. |
| Parallel-trends hand-wave | DiD chosen without checking pre-trends | List parallel trends as DiD's assumption and require a pre-trend check as a condition. |
| Simulation as fact | An in-silico model treated as evidence without validation | Name "validated generative model + parameters" as the simulation assumption; flag `[user-supplied]` validation. |
| Single-route tunnel | One method proposed with no alternatives weighed | Enforce the Tree-of-Thoughts candidate table and ranking. |
| Goal/method mismatch | A descriptive question over-engineered into a causal design (or vice versa) | Classify the goal first; let it gate which routes are even eligible. |
