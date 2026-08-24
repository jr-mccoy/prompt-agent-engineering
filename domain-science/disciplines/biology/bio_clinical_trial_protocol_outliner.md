---
title: "Clinical Trial Protocol Outliner"
category: science/disciplines/biology
description: "Outline a clinical trial protocol with CONSORT/SPIRIT-aligned structure, pre-specified primary endpoint, randomization and blinding plan, and statistical analysis plan"
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-02
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - clinical-trial
  - rct
  - consort
  - spirit
  - endpoint
  - randomization
  - blinding
  - statistical-analysis-plan
updated: "2026-05-19"
related_prompts:
  - domain-science/methods-foundations/science_experimental_design_advisor.md
  - domain-healthcare-clinical/prompts/medicine_anticoagulation_decision_support.md
---

# Clinical Trial Protocol Outliner

**Objective:** Outline a SPIRIT-aligned clinical trial protocol with a single pre-specified primary endpoint, a randomization and blinding plan defensible to a regulator, a pre-specified statistical analysis plan, safety monitoring, and a CONSORT-ready reporting scaffold.

**When to use:** Early in protocol development — before IRB / ethics submission, before any pilot enrollment — when the user has a defined intervention, a target population, and a candidate primary endpoint and needs a structured protocol scaffold a methodologist and a statistician can review. This prompt produces a **methodological outline**, not regulatory submission text and not clinical advice.

**Required inputs:**
- **Intervention** (drug / device / behavioral / surgical / digital) including dose, schedule, and comparator.
- **Target population.** Inclusion / exclusion criteria sketch.
- **Indication / condition.**
- **Phase** (I, II, III, IV) or design family (pragmatic, platform, adaptive, n-of-1, cluster).
- **Candidate primary endpoint** with time horizon.
- **Setting** (single site / multi-site / multi-country).
- **Funder posture** (academic, industry, public).
- **Regulatory geography** (FDA, EMA, MHRA, PMDA, other — affects guideline alignment).

**Optional inputs:**
- Candidate secondary endpoints.
- Known prior effect-size estimates (user-supplied).
- Anticipated control-arm event rate.
- Adaptive features under consideration.
- Existing DSMB / DMC arrangement.

**Constraints — Must:**
- Pre-specify **exactly one** primary endpoint with a time horizon and a single primary estimand. Secondary endpoints are clearly labeled and not promotable.
- Align structure to SPIRIT 2025 (or the version current at the time of authoring) and prepare the reporting scaffold so the eventual paper can map directly to CONSORT 2025.
- Specify allocation method, allocation concealment mechanism, and blinding level (open, single-blind, double-blind, triple-blind) — including who is blinded and how unblinding is handled.
- Include a pre-specified statistical analysis plan (SAP) skeleton with primary analysis population (ITT vs. modified ITT vs. per-protocol), estimand (treatment-policy / hypothetical / composite / while-on-treatment / principal-stratum), missing-data strategy, and stopping rules if applicable.
- Include a safety monitoring plan with AE / SAE definitions, reporting cadence, DSMB role, and stopping criteria.
- Surface ethical considerations: equipoise, consent process for vulnerable populations, placebo justification, post-trial access.

**Constraints — Must Not:**
- Do not draft text for regulatory submission, ICF, or IRB application. Outline only.
- Do not invent reference numbers, guidance document section numbers, drug brand names, or trial registry IDs.
- Do not propose multiple co-primary endpoints without specifying the Type I error control plan (Bonferroni, Hochberg, hierarchical, gatekeeping) and the statistical cost.
- Do not give clinical or dosing advice. If the user requests a dose, mark `[clinical input required]` and stop.
- Do not propose a power calculation without a fully written assumption set (control event rate, effect size, alpha, power, allocation ratio, dropout).
- Do not bias the design toward sponsor expectation.

**Instructions:**

1. **Confirm the design family fits the question and phase.** If the intervention is first-in-human, do not propose Phase III. If the question is comparative effectiveness, lean pragmatic. Output a one-paragraph design-family rationale.

2. **Lock the PICO and primary estimand.** Population, Intervention, Comparator, Outcome — written out. Then add the estimand attributes per ICH E9(R1): treatment, target population, variable / endpoint, intercurrent-event handling, summary measure.

3. **Pre-specify the primary endpoint.** Single endpoint, time horizon, measurement method, who measures, when, and how missingness is handled. State the minimum clinically important difference (MCID) anchor — ask if user has not supplied.

4. **Secondary and exploratory endpoints.** Labeled, ranked, with their own time horizons. State that they are not promotable to primary post-hoc.

5. **Sample-size and power.** Build three scenarios (pessimistic / central / optimistic) with the assumption set written out: control event rate, expected effect size, allocation ratio, alpha, power, dropout, interim looks. State the method (continuous: t / ANCOVA; binary: chi-square / logistic; time-to-event: log-rank with hazard ratio; non-inferiority margin if NI). Cite the calculation method by name but do not invent numerical defaults.

6. **Randomization and blinding plan.** Specify simple / block / stratified / minimization randomization; stratification factors; block size (typically not disclosed in protocol); allocation concealment mechanism; who is blinded; emergency unblinding procedure. Address how the analysis is preserved when blinding fails partially.

7. **Statistical analysis plan skeleton.** Primary analysis population; estimator (ANCOVA, logistic regression, Cox PH, mixed-model for repeated measures); covariate set; missing-data approach (MAR / MNAR sensitivity); interim analyses and alpha spending; subgroup analyses (pre-specified, no post-hoc promotion); handling of multiplicity across endpoints.

8. **Safety, monitoring, and stopping rules.** AE / SAE definitions; reporting cadence; DSMB charter elements; safety, futility, and efficacy stopping rules with the statistical cost of looks.

9. **Operational risks and ethical considerations.** Equipoise statement; placebo justification (if used); consent process for vulnerable populations; post-trial access; data sharing posture; registry commitment (ICMJE-compliant registration before enrolling the first participant).

10. **CONSORT mapping.** Pre-build the eventual reporting table so the team knows each CONSORT item has a home in the protocol now.

**Output format (locked):**

```
## Design family rationale
[1 paragraph]

## PICO + estimand (ICH E9(R1))
- Population:
- Intervention:
- Comparator:
- Outcome (primary):
- Estimand attributes: treatment / population / variable / intercurrent handling / summary measure

## Pre-specified primary endpoint
- Endpoint:
- Time horizon:
- Measurement method:
- Adjudication / blinding of assessment:
- Missing-data rule:
- MCID anchor:

## Secondary / exploratory endpoints
| Endpoint | Type | Time horizon | Adjudication |

## Sample-size scenarios
| Scenario | Control rate | Effect | Allocation | Alpha | Power | Dropout | N total | Method |

## Randomization and blinding
- Allocation method:
- Stratification factors:
- Concealment mechanism:
- Blinding level + who is blinded:
- Unblinding procedure:

## Statistical analysis plan (skeleton)
- Primary analysis population:
- Primary estimator:
- Covariates:
- Missing-data approach + sensitivity:
- Interim analyses + alpha spending:
- Pre-specified subgroup analyses:
- Multiplicity control:

## Safety and monitoring
- AE / SAE definitions and grading:
- Reporting cadence:
- DSMB role + charter elements:
- Stopping rules (safety / futility / efficacy):

## Ethical and operational considerations
- Equipoise:
- Placebo justification (if applicable):
- Consent considerations:
- Post-trial access:
- Registry posture (ICMJE):
- Data-sharing posture:

## SPIRIT alignment
| SPIRIT 2025 item | Section above | Status |

## CONSORT pre-mapping
| CONSORT 2025 item | Where it will be produced | Data needed |

## Open questions for the user
[gaps marked [user-supplied] or [clinical input required]]
```

**Reporting-standard alignment:** SPIRIT 2025 (protocol); CONSORT 2025 (eventual report); ICH E8(R1) (general considerations); ICH E9(R1) (estimands and missing data); ICH E6(R3) (GCP); applicable phase-specific guidance (FDA / EMA / MHRA / PMDA / equivalent).

**Verification checklist:**
- [ ] Exactly one primary endpoint, with single estimand fully specified.
- [ ] Three sample-size scenarios with assumption sets.
- [ ] Allocation method, concealment, blinding all named.
- [ ] Missing-data strategy is named and includes a sensitivity analysis.
- [ ] Safety stopping rules and DSMB role specified.
- [ ] No clinical or dosing advice anywhere.
- [ ] No invented references, registry IDs, or guidance section numbers.
- [ ] SPIRIT items traceable; CONSORT mapping pre-built.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Endpoint switching post-hoc | Secondary endpoint promoted after seeing primary fails | Single locked primary; secondaries non-promotable |
| Underpowered "pilot" claimed as efficacy evidence | Phase II with N=20 read as Phase III | Phase named; power scenarios show what claim is supportable |
| Estimand drift | "Treatment effect" interpreted differently mid-trial | ICH E9(R1) estimand attributes locked here |
| Missing-data wishful thinking | "We'll just use complete-case" without testing | Primary missing-data strategy + sensitivity required |
| Blinding washout (futility looks) | Multiple interim looks consuming alpha | Alpha-spending function pre-specified |
| Subgroup mining | Post-hoc subgroup hit promoted to result | Pre-specified subgroups only; post-hoc labeled exploratory |
| Invented guidance citation | Plausible "per FDA Guidance §..." text | All citations user-supplied or marked missing |
| Drift into ICF / IRB drafting | Methodologist outline becomes regulatory document | Outline only; drafting deferred to qualified author |
