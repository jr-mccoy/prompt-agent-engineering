---
name: evidence-synthesis
description: Conduct systematic evidence synthesis from literature search through GRADE assessment to defensible conclusions.
tags:
  - research
  - evidence-synthesis
  - systematic-review
  - meta-analysis
  - grade-framework
updated: "2026-04-11"
---

# Evidence Synthesis

Synthesize findings from multiple research sources using systematic review methodology, evidence grading frameworks, and structured bias assessment to produce defensible, transparent conclusions.

## When to Use This Skill

- Conducting a systematic review or scoping review of published literature
- Combining quantitative findings across multiple studies for a meta-analysis
- Grading the certainty of evidence to support clinical or policy recommendations
- Reconciling conflicting findings across studies with different designs
- Preparing evidence summaries for guideline panels, decision-makers, or grant applications

## Core Concepts

### Evidence Hierarchy

Evidence is ranked by study design and susceptibility to bias. Higher levels provide stronger causal inference but are not always available or appropriate.

```
Level 1  ── Systematic reviews and meta-analyses of RCTs
Level 2  ── Individual randomized controlled trials (RCTs)
Level 3  ── Controlled cohort studies (prospective)
Level 4  ── Case-control studies, retrospective cohorts
Level 5  ── Case series, case reports
Level 6  ── Expert opinion, mechanism-based reasoning
```

**Key principle:** Higher-level evidence can be downgraded (e.g., high risk of bias in an RCT), and lower-level evidence can be upgraded (e.g., large effect size in an observational study). The hierarchy is a starting point, not a verdict.

### GRADE Framework (Grading of Recommendations, Assessment, Development and Evaluation)

GRADE provides a systematic approach for rating certainty of evidence across outcomes.

| Certainty Level | Meaning | Implication |
|-----------------|---------|-------------|
| **High** | Very confident the true effect lies close to the estimate | Strong basis for recommendation |
| **Moderate** | Moderately confident; true effect likely close but could differ | Recommendation with caveats |
| **Low** | Limited confidence; true effect may be substantially different | Weak recommendation; more research needed |
| **Very Low** | Very little confidence; true effect likely substantially different | Uncertainty dominates; research priority |

**Factors that lower certainty:** Risk of bias, inconsistency, indirectness, imprecision, publication bias.
**Factors that raise certainty:** Large magnitude of effect, dose-response gradient, all plausible confounders would reduce effect.

### Heterogeneity Assessment

The I-squared (I²) statistic quantifies the percentage of variability in effect estimates due to true differences rather than sampling error.

| I² Value | Interpretation | Action |
|----------|---------------|--------|
| 0-25% | Low heterogeneity | Pooling generally appropriate |
| 25-50% | Moderate heterogeneity | Investigate sources; pooling may be acceptable |
| 50-75% | Substantial heterogeneity | Subgroup analysis required; consider narrative synthesis |
| 75-100% | Considerable heterogeneity | Do not pool without explanation; use random-effects model minimum |

Supplement I² with Cochran's Q test (p-value), tau-squared (between-study variance), and prediction intervals for a complete picture.

## Workflow

### Phase 1: Define the Review Question

Frame the question using the PICO/PECO framework:

- **P** (Population): Who is studied?
- **I/E** (Intervention/Exposure): What is being evaluated?
- **C** (Comparator): What is it compared against?
- **O** (Outcome): What outcomes are measured?

Specify eligibility criteria upfront: study designs included, date range, language restrictions, publication status. Register the protocol (PROSPERO for health; OSF for social science) before searching.

### Phase 2: Systematic Search and PRISMA Flow

Execute a reproducible search strategy across multiple databases. Document every step using the PRISMA 2020 flow:

```
Records identified through database searching (n = ?)
  + Records from other sources (n = ?)
  ──────────────────────────────────
  Records after duplicates removed (n = ?)
        │
        ▼
  Records screened by title/abstract (n = ?)
        │ Excluded (n = ?, with reasons)
        ▼
  Full-text articles assessed for eligibility (n = ?)
        │ Excluded (n = ?, with reasons by category)
        ▼
  Studies included in qualitative synthesis (n = ?)
        │
        ▼
  Studies included in quantitative synthesis / meta-analysis (n = ?)
```

**Search documentation requirements:** Full search strings per database, date of search, any filters applied, grey literature sources checked.

### Phase 3: Data Extraction

Build a standardized extraction form before beginning. Minimum fields:

- Study ID (author, year, country)
- Study design and setting
- Population characteristics and sample size
- Intervention/exposure details (dose, duration, delivery)
- Comparator details
- Outcome definitions and measurement tools
- Results (effect estimates, confidence intervals, p-values)
- Funding source and conflict of interest declarations

Use dual independent extraction with a third reviewer for discrepancies. Pilot the form on 3-5 studies before full extraction.

### Phase 4: Risk of Bias Assessment

Select the appropriate tool based on study design:

| Study Design | Assessment Tool | Domains |
|-------------|----------------|---------|
| Randomized trials | **Cochrane RoB 2** | Randomization, deviations, missing data, measurement, selection |
| Non-randomized interventions | **ROBINS-I** | Confounding, selection, classification, deviations, missing data, measurement, reporting |
| Diagnostic accuracy | **QUADAS-2** | Patient selection, index test, reference standard, flow/timing |
| Prognostic studies | **QUIPS** | Participation, attrition, measurement, confounding, analysis |

Present bias assessments in summary tables and traffic-light plots. Never exclude studies solely based on bias risk; instead, use sensitivity analysis to test the impact of high-risk studies.

### Phase 5: Synthesis — Narrative or Quantitative

**Decision: narrative synthesis vs. meta-analysis**

Choose meta-analysis when:
- Studies address the same question with comparable PICO elements
- Outcomes are measured in similar ways (or can be converted)
- Clinical and methodological heterogeneity is manageable
- At least 3-5 studies are available for meaningful pooling

Choose narrative synthesis when:
- Studies are too diverse in design, population, or outcomes to pool
- High unexplained heterogeneity persists after subgroup analysis
- Fewer than 3 comparable studies exist
- Qualitative and quantitative evidence must be integrated

**For meta-analysis:**
1. Select effect measure (risk ratio, odds ratio, mean difference, standardized mean difference)
2. Choose model (fixed-effect if homogeneous; random-effects if heterogeneity expected)
3. Generate forest plot: point estimates, confidence intervals, weights, pooled diamond
4. Assess heterogeneity (I², Q, tau², prediction interval)
5. Conduct subgroup and sensitivity analyses
6. Evaluate publication bias (funnel plot, Egger's test, trim-and-fill if >=10 studies)

**For narrative synthesis:**
1. Tabulate study characteristics and findings
2. Group by theme, population, intervention variant, or outcome
3. Describe patterns: direction of effect, consistency, dose-response
4. Identify outliers and explore explanations
5. Use vote counting only as a descriptive supplement, never as a decision method

### Phase 6: Grade the Evidence and Report

Apply GRADE to each critical outcome:

1. Start at high certainty for RCTs, low for observational
2. Assess five downgrading factors per outcome
3. Assess three upgrading factors for observational evidence
4. Produce a Summary of Findings table

Write the synthesis report following PRISMA 2020 checklist (27 items). Include: structured abstract, registered protocol link, complete PRISMA flow, evidence tables, forest plots, GRADE summary, and explicit statements of limitations.

## Templates

### PICO Question Template

```
In [population], does [intervention/exposure] compared to [comparator]
improve/reduce [primary outcome] and [secondary outcome]?

Eligibility:
- Designs: [RCT, cohort, case-control, etc.]
- Date range: [start] to [end]
- Languages: [specify or "no restriction"]
- Exclusions: [list]
```

### Evidence Table Template

| Study | Design | N | Population | Intervention | Comparator | Outcome | Effect (95% CI) | RoB |
|-------|--------|---|-----------|-------------|------------|---------|-----------------|-----|
| Author 2024 | RCT | 200 | Adults 18-65 | Drug A 10mg | Placebo | Pain at 12w | -2.1 (-3.0, -1.2) | Low |

### GRADE Summary of Findings Template

| Outcome | Studies (N) | Effect (95% CI) | Certainty | Downgrade Reasons | Plain Language |
|---------|-------------|-----------------|-----------|-------------------|----------------|
| Primary | 5 RCTs (1200) | RR 0.72 (0.61-0.85) | Moderate | Imprecision (-1) | Probably reduces risk |

## Best Practices

- **Register the protocol before searching.** Pre-registration prevents selective reporting and demonstrates methodological commitment. Use PROSPERO, OSF, or a journal protocol publication.
- **Use at least two independent reviewers** for screening, extraction, and bias assessment. Agreement statistics (kappa) should be reported.
- **Document every search decision.** Reproducibility is the hallmark of systematic review. Save search strings, database versions, and screening decisions.
- **Never use vote counting as the primary synthesis method.** Tallying "significant vs. not significant" studies ignores effect size, sample size, and precision. Describe direction and magnitude instead.
- **Present heterogeneity transparently.** Do not hide high I² values. Explore sources through pre-specified subgroup analyses and meta-regression.
- **Separate strength of evidence from strength of recommendation.** GRADE certainty addresses confidence in the evidence; the recommendation also weighs values, preferences, resources, and feasibility.
- **Report what you did not find.** Gaps in evidence are findings. Explicitly state which outcomes, populations, or comparisons lacked evidence.
- **Update searches before final reporting.** If months pass between initial search and publication, run an updated search to capture new studies.

## Common Pitfalls

| Pitfall | Why It Happens | How to Avoid |
|---------|---------------|--------------|
| Pooling apples and oranges | Eagerness to produce a single effect estimate despite clinical diversity | Define strict eligibility criteria; test homogeneity before pooling |
| Ignoring publication bias | Assumption that all relevant studies are published | Use funnel plots, Egger's test; search grey literature, trial registries, and conference abstracts |
| Conflating statistical significance with clinical importance | Over-reliance on p-values in individual studies | Focus on effect sizes and confidence intervals; define minimally important differences upfront |
| Cherry-picking outcomes | Selecting outcomes post-hoc to match a narrative | Pre-specify primary and secondary outcomes in the protocol |
| Treating GRADE as mechanical | Applying downgrade factors without judgment | GRADE requires reasoning: explain each rating decision in footnotes |
| Overlooking indirectness | Included studies address a slightly different question | Explicitly map each study's PICO to the review PICO; flag mismatches |

## Quality Checklist

- [ ] Review question framed with explicit PICO/PECO elements
- [ ] Protocol registered before search execution
- [ ] Search strategy documented for every database with full strings
- [ ] PRISMA flow diagram completed with numbers at each stage
- [ ] Dual independent screening, extraction, and bias assessment performed
- [ ] Risk of bias assessed using validated, design-appropriate tool
- [ ] Decision to pool or narratively synthesize is justified
- [ ] Heterogeneity quantified (I², Q, tau²) and explored via subgroups
- [ ] Publication bias evaluated (funnel plot, statistical tests if >=10 studies)
- [ ] GRADE applied to each critical outcome with footnoted reasoning
- [ ] Summary of Findings table produced
- [ ] Limitations and evidence gaps explicitly stated
- [ ] Report follows PRISMA 2020 checklist

## Examples

### Example: Synthesizing Evidence on Remote Work and Productivity

**Question:** In knowledge workers (P), does fully remote work (I) compared to fully in-office work (C) affect individual productivity (O)?

**Search:** PubMed, PsycINFO, Business Source Complete, SSRN, Google Scholar. 2015-2026. English.

**PRISMA result:** 1,847 records identified; 412 screened full-text; 38 included in qualitative synthesis; 14 in meta-analysis.

**Bias assessment:** ROBINS-I applied (all observational). 6 studies rated serious risk (confounding by self-selection); 8 moderate.

**Meta-analysis:** Random-effects model. Pooled SMD = 0.12 (95% CI: -0.05 to 0.29). I² = 68%. Subgroup by industry: tech sector SMD = 0.31 (CI: 0.10-0.52, I² = 34%); non-tech SMD = -0.04 (CI: -0.22 to 0.14, I² = 41%).

**GRADE assessment:** Very low certainty. Downgraded for risk of bias (-1, confounding), inconsistency (-1, I² = 68%), and indirectness (-1, productivity measures varied widely).

**Conclusion:** Current evidence does not permit confident conclusions about remote work's effect on productivity overall. Sector-specific analyses suggest a possible modest benefit in technology roles, but certainty remains low. Self-selection bias is the dominant methodological threat across studies. Future research should prioritize natural experiments or quasi-experimental designs with standardized productivity measures.
