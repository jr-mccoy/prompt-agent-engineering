---
title: "Systematic Review Protocol — PRISMA-Grade Scaffold for Defensible Synthesis"
category: research-academic/systematic-review
description: "Build a registration-ready systematic review protocol following PRISMA / Cochrane conventions: PICOS framing, inclusion/exclusion in binary form, comprehensive search strategy, dual independent screening, risk-of-bias assessment, data extraction template, synthesis plan, and PROSPERO-style registration. For when audit-grade defensibility is non-negotiable."
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
  - systematic-review
  - prisma
  - cochrane
  - protocol
  - meta-analysis
updated: "2026-05-10"
reasoning:
  styles: [systematic, structured, audit-grade]
  stakes: high
  horizon: months
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: team
  output_format: registration_ready_protocol
  user_role: [researcher, clinician, policy, methodologist]
  mode: [synthesize, document, plan]
related_prompts:
  - domain-research-academic/research_literature_review_plan.md
  - domain-research-academic/research_meta_analysis_scoping.md
  - domain-research-academic/research_search_strategy_designer.md
---

# Systematic Review Protocol

**Objective:** Build a registration-ready systematic review protocol that meets PRISMA / Cochrane / PROSPERO standards. Distinct from `research_literature_review_plan.md` (which covers any review type); this prompt is specifically for systematic reviews where defensibility is non-negotiable — clinical evidence synthesis, regulatory submissions, evidence-based policy, decision-grade syntheses where critics will audit the method.

**When to use:**
- Clinical or epidemiological evidence synthesis intended for guideline development.
- Regulatory submission requiring evidence base review.
- High-stakes policy / programmatic decisions where the synthesis will be challenged.
- Academic systematic review for publication in a methods-rigorous outlet.
- Evidence base for litigation, expert testimony, or major investment.

**When NOT to use:**
- Lighter synthesis tasks (use `research_literature_review_plan.md`).
- Single-question fact verification (use `research_source_triangulation.md`).
- Internal team scoping that doesn't need formal registration.

**Audience:** Methodologists, evidence synthesis specialists, clinicians, policy researchers, anyone producing audit-grade evidence reviews.

---

## Inputs / Context

1. **Review question** with PICOS / PECO framing capacity.
2. **Field / domain.** Clinical, epidemiological, social science, environmental, education.
3. **Registration target.** PROSPERO, Cochrane, Open Science Framework, internal.
4. **Resources.** Reviewer count (minimum 2 for dual screening), software (Covidence, Rayyan, RevMan, EPPI), time horizon.
5. **Statistical analysis intent.** Narrative synthesis only, or meta-analysis if data permit.

---

## Constraints

### Must
- Frame the question with **PICOS** (Population, Intervention, Comparator, Outcomes, Study design) or **PECO** (Population, Exposure, Comparator, Outcomes) — pick one and apply rigorously.
- Specify **inclusion / exclusion criteria** as binary tests across PICOS dimensions plus date, language, geography, document type.
- Build a **comprehensive search** across ≥3 databases plus grey literature, with full Boolean strings per database.
- Plan **dual independent screening** at title/abstract and full-text stages, with documented disagreement resolution (third reviewer or consensus).
- Specify a **risk-of-bias tool** appropriate to study design (Cochrane RoB 2 for RCTs, ROBINS-I for non-randomized intervention, QUADAS-2 for diagnostic accuracy, JBI for prevalence, AMSTAR-2 for reviews of reviews, GRADE for certainty across body of evidence).
- Build an **extraction template** with all fields needed for synthesis and quality assessment.
- Plan **synthesis method** explicitly: narrative, thematic, statistical pooling (with model choice), GRADE-CERQual for qualitative.
- Plan **PRISMA flow diagram** for reporting.
- Plan for **registration** before search starts.

### Must Not
- Skip dual screening — single-reviewer screening is not systematic-review-grade.
- Use a generic risk-of-bias tool when a design-appropriate one exists.
- Begin search before registration.
- Modify inclusion criteria post-hoc without documenting and justifying.
- Pool quantitatively without checking heterogeneity assumptions.

---

## Instructions

### Step 1 — PICOS framing
- **Population:** who / what is studied; inclusion bounds.
- **Intervention / Exposure:** what is delivered or measured.
- **Comparator:** what is the alternative or control.
- **Outcomes:** primary and secondary, with measurement approach.
- **Study design:** which designs included (RCTs only, all interventional, observational included).

### Step 2 — Eligibility criteria
Convert each PICOS dimension into binary tests. Add: publication date range, language, geographic scope, publication type (peer-reviewed, preprint, grey).

### Step 3 — Search strategy
Per database:
- Database name and platform (PubMed, Embase via Ovid, CINAHL via EBSCO, etc.)
- Full Boolean string with controlled vocabulary
- Date / language / type filters
- Estimated yield

Plus: grey literature sources, hand-search journals, citation tracking from named seed papers, contact with experts for unpublished work.

### Step 4 — Screening process
- Title/abstract screen: 2 reviewers independent, blinded to each other's votes, conflict resolution by third reviewer or consensus.
- Full-text screen: same, with documented exclusion reasons per study.
- PRISMA flow numbers tracked from identification through inclusion.
- Software: [Covidence / Rayyan / EPPI / DistillerSR].

### Step 5 — Risk-of-bias assessment
- Tool: [select appropriate to designs included]
- Process: dual independent assessment, conflict resolution.
- Use of RoB ratings in synthesis: [excluded if high-risk / sensitivity analysis / qualitative flag].

### Step 6 — Data extraction
Template fields:
- Bibliographic + study identifier
- Country, setting, funding, conflicts
- Population: N, demographics, inclusion
- Intervention/exposure: details, dose, duration
- Comparator
- Outcomes: measure, time points, effect estimate with 95% CI, raw data for pooling
- Risk-of-bias rating per domain
- Notes / extraction issues

Pilot extraction on 2–3 studies before full extraction.

### Step 7 — Synthesis plan
Decide before extraction:
- Narrative-only if heterogeneity expected high or designs differ.
- Meta-analysis if outcomes comparable: random vs fixed effects (default random for clinical heterogeneity), heterogeneity assessment (I², τ²), subgroup / meta-regression for hypothesized effect modifiers, sensitivity analyses.
- Publication bias: funnel plot, Egger's test if ≥10 studies.
- GRADE assessment for certainty across body of evidence per outcome.

### Step 8 — Reporting
- PRISMA 2020 checklist commitment.
- PRISMA flow diagram.
- Search strategy in appendix (full Boolean, date executed).
- Excluded studies list with reasons (full-text exclusions).
- Funding and conflicts disclosure.

### Step 9 — Registration
- Where: PROSPERO / OSF / Cochrane.
- When: before search execution.
- Protocol publication: [yes / no, where].
- Amendments policy: how protocol changes will be tracked and reported.

### Step 10 — Timeline
Phase by phase: registration, search, screen, extract, RoB, synthesize, write, peer review, submit. Realistic durations per phase given reviewer count.

---

## False-Positive Prevention

1. **Single-reviewer screening.** Not systematic-grade.
2. **Generic RoB tool.** Cochrane RoB 2 for RCTs, ROBINS-I for non-randomized — use design-appropriate.
3. **Post-hoc criterion change.** Acceptable only if documented and justified as protocol amendment.
4. **Search-before-register.** Defeats the purpose of pre-registration.
5. **Pooling without heterogeneity check.** Pooling clinically heterogeneous studies produces meaningless averages.
6. **GRADE skip.** Without GRADE (or equivalent), the synthesis can't communicate certainty.
7. **Excluded-list omission.** PRISMA requires reasons for full-text exclusions.

---

## Output Format

```
# Systematic review protocol — [topic]

## Registration
- Where: [PROSPERO / OSF / Cochrane]
- ID (when assigned): [...]

## Question
- PICOS:
  - P: [...]
  - I: [...]
  - C: [...]
  - O (primary): [...]
  - O (secondary): [...]
  - S: [designs]

## Eligibility criteria
| Dimension       | Inclusion              | Exclusion              |
|-----------------|------------------------|------------------------|
| Population      | [...]                  | [...]                  |
| Intervention    | [...]                  | [...]                  |
| Comparator      | [...]                  | [...]                  |
| Outcomes        | [...]                  | [...]                  |
| Design          | [...]                  | [...]                  |
| Date            | [yyyy–yyyy]            | [pre-yyyy]             |
| Language        | [...]                  | [...]                  |

## Search strategy
| Database (platform) | Boolean string | Filters | Date executed |
|---------------------|----------------|---------|---------------|
| [PubMed]            | [...]          | [...]   | [planned]     |
| [Embase via Ovid]   | [...]          | [...]   | [planned]     |
| [...]               | [...]          |         |               |

- Grey literature: [list]
- Hand-search: [journals]
- Citation tracking: [seed papers, generations]
- Expert contact: [yes/no]

## Screening
- Title/abstract: dual independent, [software]
- Full-text: dual independent, [software]
- Conflict resolution: [third reviewer / consensus]
- PRISMA flow: tracked

## Risk-of-bias
- Tool: [...]
- Process: dual independent
- Use in synthesis: [...]

## Extraction
- Template fields: [list]
- Piloting: [N studies]

## Synthesis
- Method: [narrative / thematic / meta-analysis / GRADE-CERQual]
- If meta-analysis: model [fixed/random], heterogeneity [I²/τ²], subgroups [planned], sensitivity [planned], publication bias [funnel/Egger]
- GRADE: per-outcome certainty assessment

## Reporting
- PRISMA 2020 checklist: [yes]
- Flow diagram: [yes]
- Excluded list with reasons: [yes]
- Conflicts and funding: [disclosed]

## Timeline
[Phase-by-phase with durations]

## Amendments policy
[How changes from this protocol will be documented]
```

---

## Verification

- [ ] PICOS / PECO fully specified.
- [ ] Eligibility criteria binary-testable per dimension.
- [ ] Search across ≥3 databases plus grey lit.
- [ ] Boolean strings full per database.
- [ ] Dual independent screening planned.
- [ ] Design-appropriate RoB tool selected.
- [ ] Extraction template complete with pilot plan.
- [ ] Synthesis method matched to expected heterogeneity.
- [ ] GRADE planned for certainty rating.
- [ ] Registration before search.
- [ ] PRISMA reporting committed.
