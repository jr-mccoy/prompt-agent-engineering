---
title: "Public Program Evaluation Design — Theory of Change, Evaluation Questions, Counterfactual Design Choice, Data, and Ethics"
category: policy/program-evaluation
description: "Design the evaluation of a public program before it launches or while it can still be changed: write the theory of change with its testable assumptions, set impact and process evaluation questions, choose the counterfactual design the rollout actually permits (RCT, phased-rollout, difference-in-differences, regression discontinuity, interrupted time series, or process-only), size it with a minimum detectable effect, specify data and indicators with their gaming risks, and clear the ethics and governance gates — distinct from education-program logic models and from general research causal-inference design."
techniques:
  - DS-01
  - DS-02
  - QA-21
  - QA-02
difficulty: advanced
tags:
  - program-evaluation
  - impact-evaluation
  - theory-of-change
  - quasi-experimental-design
  - process-evaluation
  - evidence-based-policy
  - did-the-program-work
  - how-to-evaluate-government-program
  - pilot-evaluation-plan
updated: "2026-10-02"
reasoning:
  styles: [causal, analytic, structural, adversarial]
  stakes: high
  horizon: years
  uncertainty: deep
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: team
  output_format: structured
  user_role: [policy, analyst, evaluator, program_manager, funder]
  mode: [plan, design, document]
related_prompts:
  - domain-science/statistics/science_causal_inference_design.md
  - domain-education-teaching/program/evaluation-analytics/program_program_evaluation_framework.md
  - domain-policy/policy_implementation_feasibility.md
---

# Public Program Evaluation Design

**Objective:** Produce an evaluation plan a funder, ministry or legislature can rely
on: what the program is supposed to change and through what chain, which questions
the evaluation will answer, the strongest counterfactual the rollout allows, whether
the sample can detect the effect that matters, and what data, ethics and governance
it needs — decided before the program makes the best designs impossible.

**Audience:** Government evaluation units, program managers, foundation and
development-agency staff, legislative auditors, and external evaluators bidding on
or scoping an evaluation.

**When to Use:**
- A public program, pilot or grant scheme is about to launch and someone asked
  "how will we know it worked?"
- Rollout is being planned and a phased or lottery-based allocation is still possible.
- A legislature or funder mandated an evaluation and you must write the terms of
  reference or evaluate the bids.
- An existing program has outcome data but no counterfactual, and you need to know
  what can still be learned.
- **Not this prompt if** the program is a school or training program and you need a
  Kirkpatrick / CIPP / logic-model framework for instructional quality —
  `domain-education-teaching/program/evaluation-analytics/program_program_evaluation_framework.md`
  does that for educators. If you are a researcher choosing an estimator for an
  observational dataset (DAG, backdoor criterion, IV), use
  `domain-science/statistics/science_causal_inference_design.md`; this prompt works
  from the policy side — rollout, budget, politics, governance — and hands the
  estimator detail to that one. Whether the program can be run at all is
  `domain-policy/policy_implementation_feasibility.md`.

## Inputs / Context

1. **The program**: target population, eligibility rule, what participants receive,
   dose and duration, delivery agents.
2. **Rollout plan**: all at once or phased, by region or cohort, oversubscribed or
   not, any eligibility score or cutoff.
3. **Decision the evaluation informs**: scale up, redesign, continue funding,
   statutory sunset review — and when it must be made.
4. **Existing data**: administrative records, linkage permissions, baseline surveys,
   pre-program time series length.
5. **Budget and timeline** for the evaluation.
6. **Constraints**: legal duty to serve all eligible people, political commitments
   to particular areas, data-protection regime, ethics review body.

## Method

1. **Theory of change (DS-01).** Inputs → activities → outputs → short-term
   outcomes → long-term outcomes, with the **assumption at each arrow** written as a
   testable statement ("caseworkers have time to meet clients fortnightly").
   Mark the two or three assumptions the program most depends on.
2. **Evaluation questions.** Separate **impact** (did outcomes change because of the
   program?), **process** (was it delivered as designed, to whom, at what fidelity?)
   and **economic** (cost per outcome) questions. Limit to 5–8; each names the
   decision it informs.
3. **Choose the counterfactual from the rollout, not the wish list.**
   - Oversubscribed or phased → **RCT** or randomised phase-in (wait-list).
   - Eligibility score with a cutoff → **regression discontinuity** (local effect
     near the cutoff only).
   - Staggered adoption across areas with comparable pre-trends → **difference-in-
     differences** (check parallel pre-trends on ≥3 pre-periods; use estimators
     robust to staggered timing).
   - Single population, long pre-series (≥8–12 points), sharp start → **interrupted
     time series** with a control series if any exists.
   - None of these → **process and contribution analysis only**, and say so; do not
     dress a before-after comparison as impact.
4. **Power (QA-02 for assumptions).** State the minimum detectable effect (MDE) at
   80% power and 5% significance, the policy-relevant effect, and whether the MDE is
   below it. For clustered rollout, include the intra-cluster correlation; small
   numbers of clusters are the usual reason an evaluation cannot answer its own
   question.
5. **Indicators and data (DS-02, QA-21).** For each question: indicator, source,
   frequency, baseline value. For every indicator delivery staff control, list how
   it could be moved without the outcome moving (creaming easy cases, reclassifying
   exits) and pair it with a harder-to-game measure.
6. **Process evaluation.** Fidelity, reach (who enrolled vs who was eligible),
   dose received, and implementation barriers — the data that explains a null result.
7. **Ethics and governance.** Equipoise or resource-scarcity justification for any
   withheld service; consent or a waiver basis; data-protection impact assessment
   for linkage; independence of the evaluator; a pre-registered analysis plan; and a
   commitment to publish whatever the result.
8. **Timeline against the decision.** When the first credible impact estimate
   arrives versus when the funding decision falls; if it arrives after, design an
   interim (process + early outcome) report.

## Output Format

```
# Evaluation design — [program]   Decision informed: [..] by [date]

## Theory of change
[chain] — critical assumptions: A1 .. A3
## Evaluation questions
| # | Type (impact / process / economic) | Question | Decision it informs |
## Design
Chosen: [..]  Why the rollout permits it: [..]  Rejected designs and why: [..]
Estimand: [ATE / effect at cutoff / ATT] — population it generalises to: [..]
## Power
MDE [..] vs policy-relevant effect [..] — adequate? [Y/N]
## Indicators and data
| Question | Indicator | Source | Baseline | Gaming risk | Paired measure |
## Process evaluation
## Ethics and governance gates
## Timeline vs decision
## Threats to validity and how each is checked
```

## Verification

- [ ] Each arrow in the theory of change has a written, testable assumption.
- [ ] Every evaluation question names the decision it informs.
- [ ] The design follows from the stated rollout; rejected designs are listed with reasons.
- [ ] The estimand and the population it generalises to are stated.
- [ ] MDE is computed and compared with a policy-relevant effect.
- [ ] Every staff-controlled indicator has a gaming risk and a paired measure.
- [ ] Ethics: justification for any withheld service, data-protection basis, pre-registration.
- [ ] The impact estimate's arrival date is compared with the decision date.

## False-Positive Prevention

1. **Before-after as impact.** Outcomes improved after launch while the economy
   recovered; without a counterfactual, that is a trend, not an effect.
2. **Pilot-site selection.** Pilots placed in the most capable areas overstate what
   scale-up will deliver; name how sites were chosen.
3. **Under-powered "no effect".** A null result from a design that could only detect
   a 15-point change says little about a 5-point one. Report the MDE beside any null.
4. **Outputs as outcomes.** "4,000 sessions delivered" is an output; the question is
   what changed for participants.
5. **RDD and DiD over-reach.** RDD estimates the effect at the cutoff; DiD rests on
   parallel trends. State the limit in the summary, not a footnote.
6. **Evaluator who cannot report failure.** An evaluation commissioned and managed by
   the program team, with no publication commitment, is a reputational risk; build
   independence in.

## Example Output

```
# Evaluation design — Intensive Employment Support (IES) for long-term unemployed
Decision informed: national roll-out funding in the 2029 budget (Sept 2028)

## Theory of change
Referral → caseworker (1:40) → fortnightly meetings + training voucher → job search
intensity and skills ↑ → job entry ↑ → sustained earnings ↑.
A1 caseworkers keep 1:40 (not 1:70) caseloads; A2 vouchers are spent on courses
employers value; A3 local vacancies exist for the target group.

## Evaluation questions
| 1 | impact | Does IES raise 12-month employment vs standard support? | fund / don't |
| 2 | impact | Does the effect persist at 24 months? | scale-up case |
| 3 | process | Were caseloads held at 1:40? Who dropped out? | redesign |
| 4 | economic | Cost per additional person employed at 12 months? | value for money |

## Design
Rollout: 24 job centres, capacity for 3,000 of ~6,000 eligible in year 1 →
oversubscribed. Chosen: individual-level randomised allocation of the 6,000,
50/50, controls get standard support and IES in year 2 (wait-list).
Rejected: DiD across centres (only 24 clusters, pilot centres self-selected);
RDD (no eligibility score).
Estimand: ITT effect of an IES offer among eligible long-term unemployed.

## Power
Baseline 12-month employment 30% [admin data]. n = 3,000 per arm → MDE ≈ 3.3 pts
(80% power, α = 0.05, two-sided). Policy-relevant effect 5 pts (break-even on cost)
→ adequate.

## Indicators and data
| Q1 | employed ≥1 day in month 12 | tax-record linkage | 30% | none — admin source | — |
| Q3 | caseload per worker | case system | — | reclassifying inactive cases | audited caseload sample |
| Q3 | "job outcomes" reported by provider | provider return | — | counting short spells | tax-record earnings ≥ threshold |

## Ethics and governance gates
Resource scarcity justifies the lottery (no one loses existing support); ethics
board approval; DPIA for tax-record linkage; independent evaluator; analysis plan
registered before month-12 data are released; publication committed in the grant.

## Timeline vs decision
12-month outcomes for the first cohort available June 2028 (tax lag 3 months) →
before the Sept 2028 decision. 24-month result arrives after; interim report says so.
```

## Techniques Used

- **DS-01 Framework Application** — theory of change and the design-selection ladder (RCT → RDD → DiD → ITS → process-only).
- **DS-02 Metric Specification** — each question has an indicator, source, baseline and frequency.
- **QA-21 Metric Gaming Vector Enumeration** — staff-controlled indicators listed with how they could be gamed and a paired measure.
- **QA-02 Adversarial Stress-Test** — power, parallel trends and pilot selection attacked before the design is accepted.

## Related Prompts

- `domain-science/statistics/science_causal_inference_design.md` — estimator-level detail (DAGs, IV, falsification tests) for the chosen design.
- `domain-education-teaching/program/evaluation-analytics/program_program_evaluation_framework.md` — Kirkpatrick / CIPP frameworks for education and training programs.
- `domain-policy/policy_implementation_feasibility.md` — the delivery capacity the process evaluation will test.
