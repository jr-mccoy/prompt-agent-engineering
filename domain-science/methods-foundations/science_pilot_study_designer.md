---
title: "Pilot Study Designer"
category: science/methods-foundations
description: "Design a feasibility-focused pilot that de-risks a full study by setting pre-specified progression criteria, and that is explicit about what a pilot can and cannot establish."
techniques:
  - ST-01
  - ST-03
  - DS-02
  - CM-02
  - QA-01
  - QA-02
difficulty: advanced
tags:
  - pilot-study
  - feasibility
  - progression-criteria
  - study-design
  - go-no-go
  - recruitment
  - protocol-fidelity
  - pre-registration
updated: "2026-06-26"
related_prompts:
  - domain-science/methods-foundations/science_experimental_design_advisor.md
  - domain-science/methods-foundations/science_power_and_sample_size_calculator.md
  - domain-science/methods-foundations/science_methodology_decision_tree.md
---

# Pilot Study Designer

**Objective:** Produce a pilot/feasibility study design whose objectives are feasibility objectives — recruitment and retention rates, protocol fidelity, instrument performance, and parameter estimates to seed a later power calculation — each tied to a pre-specified green/amber/red progression criterion. The output is explicit that a pilot is *not* powered for efficacy and protects against treating pilot p-values or effect sizes as confirmatory.

**When to use:** Before committing resources to a definitive study, when feasibility (recruitment, adherence, procedures, measures, or estimates) is genuinely uncertain. Precondition: the definitive study's question and broad design exist, and the open uncertainty is feasibility, not the scientific hypothesis.

**Required inputs:**
- **Discipline.** <field, e.g. clinical trials, education, ecology, HCI>
- **Study type.** <observational / experimental / computational / etc.>
- **Definitive study it feeds.** The full study the pilot de-risks, and its primary outcome.
- **Feasibility uncertainties.** What is actually unknown (recruitment rate, retention, adherence, procedure fidelity, instrument behavior, parameter estimates).
- **Resource envelope.** Time, budget, and the maximum pilot sample feasible.

**Optional inputs:**
- Candidate progression thresholds the team already has in mind.
- Known constraints (single site vs multi-site, eligibility funnel estimates).
- Instruments/measures under evaluation and their `[user-supplied]` prior performance.
- Whether the pilot is internal (rolls into the main study) or external (standalone).
- Stakeholder or funder decision deadline.

**Constraints — Must:**
- Frame every aim as a **feasibility objective**, not an efficacy aim.
- Set **pre-specified progression criteria** with green (go) / amber (adjust) / red (stop) thresholds defined *before* data collection.
- Separate **what the pilot CAN establish** from **what it CANNOT** in a dedicated section.
- Treat any effect/variance estimate as a **planning input** for a later power calc, reported with its imprecision — never as a confirmatory result.
- Mark the distinction between **pre-specified feasibility analysis** and any **exploratory** look at clinical/scientific signals.
- Use calibrated language throughout drafted text.
- Default to an **Open Science** branch (pre-register the pilot protocol and progression criteria; share materials); closed-data handling only as a named non-default exception.

**Constraints — Must Not:**
- Do not invent citations, DOIs, effect sizes, prior-study parameters, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not interpret pilot p-values or effect sizes as evidence of efficacy.
- Do not run or recommend a hypothesis test of the primary clinical/scientific outcome as the pilot's success criterion.
- Do not let the pilot become an underpowered version of the main study (garden-of-forking-paths / HARKing risk).
- Do not use "novel", "groundbreaking", "first-ever", or "gold standard" in drafted text.
- Do not promise that a green pilot guarantees a successful definitive study.

**Instructions:**

1. **Name the feasibility uncertainties.** List the specific unknowns that block the definitive study and rank them by how much they threaten it. Discard "uncertainties" that are really about the scientific hypothesis — those belong in the main study, not a pilot.
2. **Write feasibility objectives.** Convert each retained uncertainty into a measurable feasibility objective (e.g. "estimate monthly recruitment rate", "estimate 8-week retention", "assess fidelity of the intervention checklist", "assess completion/missingness of instrument X").
3. **Set progression criteria up front.** For each objective, pre-specify green/amber/red thresholds and the action each triggers (proceed as planned / proceed with modification / stop or redesign). Make thresholds defensible against the definitive study's needs.
4. **Size the pilot for precision, not power.** Choose a sample size justified by the precision needed on feasibility estimates (e.g. confidence-interval width on a retention proportion) or an accepted rule-of-thumb, explicitly *not* by efficacy power. State the justification.
5. **Specify CAN vs CANNOT.** Lay out plainly what the pilot will establish (feasibility rates, fidelity, instrument performance, parameter estimates for power planning) and what it cannot (efficacy, confirmatory effect size, significance of the primary outcome).
6. **Plan the feasibility analysis.** Pre-specify how each rate/estimate is computed and reported with uncertainty (proportions with CIs, descriptive summaries, qualitative fidelity notes). Keep any scientific-signal look strictly exploratory, labeled, and excluded from go/no-go.
7. **Define the decision and handoff.** Specify the go/no-go decision rule that aggregates the progression criteria, and how surviving parameter estimates feed the definitive study's power analysis (link to the power/sample-size prompt).
8. **Pre-register and stress-test.** Draft a pre-registration-ready protocol (objectives, thresholds, analysis) and adversarially check: could an amber/red result be rationalized away? Could a "successful" pilot mask a fatal feasibility problem? Tighten thresholds accordingly.

**Output format (locked):**

```
## Definitive Study & Feasibility Uncertainties
[main study + primary outcome | ranked list of feasibility unknowns | discarded "uncertainties" that aren't feasibility]

## Feasibility Objectives
| # | Objective | Measure | Why it de-risks the main study |
|---|---|---|---|

## Progression Criteria (pre-specified)
| Objective | Green (go) | Amber (adjust) | Red (stop) | Action on trigger |
|---|---|---|---|---|

## Pilot Size & Justification
[sample size | precision-based or rule-of-thumb rationale | explicit "not powered for efficacy"]

## What This Pilot CAN vs CANNOT Establish
**CAN:** [feasibility rates, fidelity, instrument performance, planning estimates]
**CANNOT:** [efficacy, confirmatory effect size, primary-outcome significance]

## Feasibility Analysis Plan
[per-objective computation + uncertainty reporting | exploratory-signal section, clearly labeled, excluded from go/no-go]

## Go/No-Go Decision & Handoff
[aggregate decision rule | how parameter estimates feed the definitive power calc]

## Pre-Registration & Open-Data Note
[Open Science default: pre-register protocol + thresholds, share materials; closed-data exception only with justification]
```

**Reporting-standard alignment:** For clinical/health pilots, align with the **CONSORT 2010 extension for randomised pilot and feasibility trials** and the **Pilot and Feasibility Studies** reporting conventions; register on the relevant trial registry. For other fields, align with the discipline's pre-registration template (OSF/AsPredicted) and STROBE/SPIRIT-style protocol conventions where applicable. Name the standard explicitly.

**Verification checklist (before delivering):**
- [ ] Every aim is a feasibility objective, not an efficacy aim.
- [ ] Green/amber/red progression criteria are pre-specified with triggered actions.
- [ ] A dedicated CAN vs CANNOT section is present and accurate.
- [ ] Sample size is justified by precision/feasibility, with explicit "not powered for efficacy".
- [ ] Any effect/variance estimate is framed as a planning input with stated imprecision.
- [ ] Exploratory scientific-signal looks are labeled and excluded from the go/no-go.
- [ ] No fabricated parameters, citations, or instrument specs; gaps marked `[user-supplied]`.
- [ ] A pilot/feasibility reporting standard is named; Open Science default branch present.
- [ ] No banned hype terms; no claim that a green pilot guarantees the main study.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Mini-efficacy trial | A "pilot" that tests the primary outcome and reports a p-value as success | Force feasibility objectives + CAN/CANNOT section; ban primary-outcome hypothesis tests as success criteria. |
| Effect-size mining | Reading the pilot's observed effect as the expected effect for the main study | Report estimates with CIs as planning inputs only; route to SESOI-anchored power planning. |
| Post-hoc thresholds | Progression criteria chosen after seeing the data | Require thresholds pre-specified and pre-registered before data collection. |
| Underpowered → "promising" | A non-significant signal spun as encouraging | Calibrated language; exploratory signals labeled and walled off from the decision. |
| Feasibility theater | Green on trivial metrics while the real blocker (e.g. eligibility funnel) is untested | Rank uncertainties by threat in Step 1; ensure the top threat has its own objective. |
| Green-guarantees-success | Implying a feasible pilot means the main study will work | State explicitly that feasibility ≠ efficacy; the pilot de-risks, it does not predict the result. |
