---
title: "Meta-Analysis Scoping — Feasibility Assessment and Analytic Plan"
category: research-academic/meta-analysis
description: "Decide whether a meta-analysis is feasible given the available studies, and if so, scope the analytic plan: model choice, heterogeneity assessment, subgroup / sensitivity analyses, and publication-bias checks. Prevents the most common meta-analysis failure: pooling studies that aren't comparable."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - meta-analysis
  - feasibility
  - heterogeneity
  - effect-size
  - statistics
updated: "2026-05-10"
reasoning:
  styles: [systematic, statistical, feasibility]
  stakes: high
  horizon: weeks_to_months
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: pair_or_team
  output_format: feasibility_verdict_plus_plan
  user_role: [researcher, methodologist, clinician, policy]
  mode: [audit, plan]
related_prompts:
  - domain-research-academic/research_systematic_review_protocol.md
  - domain-research-academic/research_evidence_map.md
  - domain-research-academic/research_literature_review_plan.md
---

# Meta-Analysis Scoping

**Objective:** Decide whether a meta-analysis is feasible given the candidate study pool, and if yes, build the analytic plan: model choice, heterogeneity assessment, subgroup and sensitivity analyses, publication-bias diagnostics. Outputs a clear verdict (feasible / feasible-with-narrowing / not feasible) and, when feasible, a plan ready to execute.

**When to use:**
- Inside a systematic review where pooling is being considered.
- Standalone meta-analysis on a focused question.
- Updating a prior meta-analysis with new studies.
- Deciding whether to pool a heterogeneous set or report narratively.

**When NOT to use:**
- < 5 studies on the same effect (descriptive synthesis is more honest).
- Studies with non-comparable populations / interventions / outcomes.
- Single-study evidence base (no pooling possible).

**Audience:** Methodologists, clinical researchers, evidence synthesis specialists, policy analysts.

---

## Inputs / Context

1. **The pooled question.** What outcome is being estimated, in what population, with what intervention/exposure and comparator.
2. **Study pool.** List of candidate studies with brief summary.
3. **Effect-size data availability** per study (means and SDs, event counts, ORs, hazard ratios, raw data).
4. **Prior meta-analyses** on this question (if any).
5. **Resources** (statistical software, methodology expertise, time).

---

## Constraints

### Must
- Assess **comparability** across PICO dimensions: populations comparable, interventions comparable, comparators comparable, outcomes comparable, study designs comparable.
- Assess **effect-size extractability**: do the studies report data that can be converted to a common metric?
- Estimate **heterogeneity** likely magnitude before pooling: clinical heterogeneity (population / intervention / outcome differences), methodological heterogeneity (design / risk-of-bias differences), statistical heterogeneity (effect-size variance).
- Verdict explicit: **feasible** / **feasible-with-narrowing** (specify what to drop) / **not feasible** (specify why; recommend narrative synthesis).
- If feasible, plan: **model** (fixed vs random effects, default random for clinical data), **effect metric** (OR, RR, MD, SMD, HR), **heterogeneity assessment** (I², τ², 95% prediction interval), **subgroup analyses** for hypothesized effect modifiers, **sensitivity analyses** (excluding high-risk-of-bias studies, leave-one-out), **publication bias** diagnostics (funnel plot, Egger's test if ≥10 studies, trim-and-fill).

### Must Not
- Pool clinically heterogeneous studies (different populations, interventions, outcomes) just because the math works.
- Use fixed-effects when between-study heterogeneity is plausible.
- Compute Egger's test on < 10 studies (low power, misleading).
- Treat I² as the only heterogeneity metric (it depends on study size; complement with τ² and PI).
- Forget the GRADE step for certainty rating across the pooled body of evidence.

---

## Instructions

### Step 1 — Restate the pooled question
PICOS terms.

### Step 2 — Comparability matrix
For the candidate studies, score:
| Dimension | Comparability across studies | Notes |
|-----------|------------------------------|-------|
| Population | high / mod / low |       |
| Intervention | high / mod / low |    |
| Comparator | high / mod / low |      |
| Outcome | high / mod / low |         |
| Design | high / mod / low |          |

If any dimension is "low", pooling produces a clinically meaningless average; flag for narrowing or narrative synthesis.

### Step 3 — Effect-size extractability
Per study: can effect size be computed? In a common metric? With variance?

### Step 4 — Heterogeneity expectation
Pre-pool estimate: clinical heterogeneity (high if populations / interventions vary), methodological (high if design / RoB varies), expected I².

### Step 5 — Feasibility verdict
- **Feasible:** comparable across PICO, ≥ 5 (ideally ≥ 10) studies, effect sizes extractable, heterogeneity manageable.
- **Feasible-with-narrowing:** feasible if a subset is restricted (specify which studies to exclude and why).
- **Not feasible:** flag the reason, recommend narrative synthesis or design-specific subset.

### Step 6 — If feasible, analytic plan

#### Model
- Fixed effects: assumes single true effect; appropriate only for very homogeneous studies (same population, intervention, outcome — rare).
- **Random effects (default for clinical / behavioral pooling):** assumes distribution of true effects across studies.

#### Effect metric
Match to outcome type: binary → OR, RR; continuous → MD, SMD; time-to-event → HR.

#### Heterogeneity
- I² (proportion of variance attributable to heterogeneity)
- τ² (between-study variance)
- 95% prediction interval (where the true effect of a new study would likely fall)

#### Subgroup analyses
Pre-specify hypothesized effect modifiers (population subgroups, intervention variants, dose). Test interaction.

#### Sensitivity analyses
- Excluding high-risk-of-bias studies
- Leave-one-out
- Different effect-size metric where applicable

#### Publication bias
- Funnel plot (visual)
- Egger's regression (if ≥ 10 studies)
- Trim-and-fill (interpret cautiously)

#### Certainty assessment
GRADE for the pooled estimate per outcome.

### Step 7 — Reporting plan
Forest plot, summary table, GRADE rating, narrative interpretation, limitations.

---

## False-Positive Prevention

1. **Apple-orange pooling.** Different populations or interventions averaged into meaninglessness.
2. **Fixed-effects default.** Inappropriate for clinical pooling where heterogeneity is the rule.
3. **I² alone.** Add τ² and PI; I² is sample-size dependent.
4. **Underpowered Egger's.** < 10 studies → misleading.
5. **Subgroup sprawl.** Many subgroup comparisons → false positives. Pre-specify.
6. **Narrative dismissal.** Refusing meta-analysis when studies are comparable just because heterogeneity is non-zero (some heterogeneity always exists; the question is whether it's manageable).
7. **GRADE skip.** Pooled estimate without certainty rating misleads downstream users.

---

## Output Format

```
# Meta-analysis scoping — [pooled question]

## Pooled question (PICOS)
- P: [...]
- I: [...]
- C: [...]
- O: [...]
- S: [...]

## Candidate studies
| Study | Year | Population | Intervention | Outcome | Effect-size data |
|-------|------|------------|--------------|---------|-------------------|
| [...] |      |            |              |         |                   |

## Comparability
| Dimension    | Comparability | Notes |
|--------------|---------------|-------|
| Population   |               |       |
| Intervention |               |       |
| Comparator   |               |       |
| Outcome      |               |       |
| Design       |               |       |

## Effect-size extractability
- Studies with computable effect size: [N / total]
- Common metric possible: [yes / no, why]

## Heterogeneity expectation
- Clinical: [...]
- Methodological: [...]
- Expected I²: [rough range]

## Verdict
- [Feasible / Feasible-with-narrowing / Not feasible]
- Reasoning: [...]
- If narrowing: include only [...]
- If not feasible: recommend [narrative synthesis / design-restricted subset]

## Analytic plan (if feasible)
- Model: [random effects / fixed]
- Effect metric: [OR / RR / MD / SMD / HR]
- Heterogeneity: I², τ², PI
- Pre-specified subgroups: [list]
- Sensitivity analyses: [list]
- Publication bias: [funnel + Egger if ≥10]
- Software: [...]

## GRADE plan
- Per-outcome certainty rating

## Reporting
- Forest plot
- Summary table
- Narrative interpretation
- Limitations
```

---

## Verification

- [ ] Pooled question framed as PICOS.
- [ ] Comparability scored across all PICO dimensions.
- [ ] Effect-size extractability assessed.
- [ ] Heterogeneity expectation stated pre-pool.
- [ ] Verdict explicit (feasible / narrow / not feasible).
- [ ] If feasible: model, metric, heterogeneity, subgroups, sensitivity, pub bias all planned.
- [ ] GRADE plan included.
- [ ] No fixed-effects default for clinical pool.
- [ ] No Egger's planned on < 10 studies.
