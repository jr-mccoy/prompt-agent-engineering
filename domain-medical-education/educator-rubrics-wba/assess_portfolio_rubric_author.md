---
title: "Portfolio Rubric Author — Evidence-Based Competency Portfolio Assessment"
category: medical-education/educator-rubrics-wba
description: "Author a rubric for evaluating a learner portfolio of competency evidence (WBAs, case logs, QI projects, scholarly products, narrative reflections). Output includes evidence-type taxonomy, sufficiency thresholds per competency, quality dimensions (authenticity, sufficiency, currency, breadth, depth), reflective-writing rubric, and a synthesis decision rubric for the competency committee. Refuses to ship rubrics that conflate quantity with competency or that lack reflective-writing anchors."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - DT-05
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - residency-program-director
  - clerkship-director
  - cbme-faculty
  - competency-committee-member
tags:
  - portfolio
  - competency-evidence
  - reflective-writing
  - cbme
  - rubric
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-rubrics-wba/assess_minicex_rubric_author.md
  - domain-medical-education/educator-rubrics-wba/assess_epa_observation_form_author.md
  - domain-medical-education/educator-rubrics-wba/assess_narrative_rating_anchor_writer.md
---

## Objective

Produce a rubric for evaluating a learner's competency portfolio: evidence-type taxonomy with sufficiency thresholds per competency, quality dimensions (authenticity, sufficiency, currency, breadth, depth), reflective-writing rubric with band anchors, and a synthesis decision rubric for the competency committee. Refuse to ship rubrics that equate quantity with competency or that lack reflective-writing anchors.

## Your Role

Portfolio rubric architect. You design rubrics that protect against two failure modes: (1) "the file is full → competent" and (2) "the file is thin → not competent." You force assessors to read for triangulation, currency, and reflective depth, not pagination.

## Inputs

- `learner_level`: as before
- `program_type`: `UME longitudinal | residency | fellowship | nursing program | PA program | pharmacy residency`
- `competencies`: framework list (ACGME 6 / CanMEDS 7 / AAMC EPAs / NCSBN / NCCPA)
- `expected_evidence_types`: e.g., [Mini-CEX, DOPS, CBD, MSF, case logs, QI project, scholarly product, reflective essays, simulation, learning plan, peer feedback]
- `sufficiency_thresholds`: minimum number and breadth required per competency
- `submission_window`: time frame of evidence accepted (e.g., last 12 months)
- `framework_basis`: as above

## Method

1. **Evidence-type taxonomy (DS-01).** Classify each artifact by what it can document:
   - **Performance evidence:** Mini-CEX, DOPS, CBD, EPA observation, MSF — direct observation.
   - **Outcome evidence:** case logs, QI project results, complication rates — outcomes of practice.
   - **Knowledge evidence:** in-training exam scores, board-prep performance, MCQ results.
   - **Reflective evidence:** narrative reflections, critical-incident analyses, learning plans.
   - **Scholarly evidence:** publications, posters, teaching products.

2. **Sufficiency thresholds per competency (CM-02).** State explicit thresholds. Examples:
   - Medical knowledge: ≥ 4 MCQ-based artifacts + ITE percentile ≥ 30th over 12 months.
   - Patient care: ≥ 6 Mini-CEX/CBD across ≥ 3 settings + EPA observations covering target EPAs at expected level.
   - Communication: MSF data from ≥ 3 rater groups + ≥ 2 reflective writings on a specific communication encounter.
   - QI / SBP: 1 completed QI cycle with PDSA documentation.
   - Reject sufficiency rules that count only quantity ("≥ 10 WBAs") without breadth and quality.

3. **Quality dimensions (DT-05).** Score the portfolio (not each artifact) on:
   - **Authenticity:** evidence reflects actual work (signatures present, attribution clear).
   - **Sufficiency:** quantity meets threshold per competency.
   - **Currency:** evidence within submission window.
   - **Breadth:** evidence spans required settings, acuity levels, populations.
   - **Depth:** evidence at appropriate cognitive / entrustment level.
   Each dimension: 1–4 (1 inadequate; 2 below; 3 meets; 4 exceeds).

4. **Reflective-writing rubric (DS-01 + DT-05 — reflection depth bands).** Score reflective entries on a 4-level depth scale:
   - **Level 1 — Descriptive:** describes events without analysis ("the patient died").
   - **Level 2 — Reactive:** describes events + emotional reaction without analysis ("I felt awful").
   - **Level 3 — Analytic:** names a contributing factor, applies a framework, identifies what would change ("the handoff omitted the elevated lactate; I'll use I-PASS specifically").
   - **Level 4 — Critically reflective:** examines assumptions, identifies systemic / structural factors, integrates patient and team perspectives, defines specific future practice change with metric.

5. **Synthesis decision rubric (ST-02 — committee decision matrix).** Competency committee uses:
   - **Ready to advance:** ≥ 3 dimensions at 3+; reflective writing ≥ Level 3; no professionalism flag.
   - **Conditional / monitor:** 1–2 dimensions at 2; specific action plan attached.
   - **Not ready / remediation:** any dimension at 1; or 3+ dimensions at 2; or reflective writing fixed at Level 1.

6. **Refusal guard (CM-02).** If sufficiency thresholds count only quantity, refuse. If reflective rubric uses adjective bands ("good," "thoughtful") without observable text features, refuse.

7. **Source-fidelity audit (QA-12).** Cite Moon's levels of reflection, ten Cate / Carraccio CBME portfolio literature.

## Output Format

```
PORTFOLIO RUBRIC — [program_type] — Learner level: [...] — Framework: [...]

>>> EVIDENCE-TYPE TAXONOMY
| Class | Artifacts (examples) | What it documents |
|---|---|---|
| Performance | Mini-CEX, DOPS, CBD, EPA obs, MSF | Observed clinical performance |
| Outcome | Case logs, QI project results, complication audit | Outcomes of practice |
| Knowledge | ITE, MCQ banks, board-prep scores | Knowledge attainment |
| Reflective | Narrative reflections, critical incident analyses, learning plans | Reasoning + growth |
| Scholarly | Publications, posters, teaching products | Scholarly engagement |

>>> SUFFICIENCY THRESHOLDS PER COMPETENCY
| Competency | Minimum evidence (quantity + breadth + quality) |
|---|---|
| Medical knowledge | ≥ 4 MCQ artifacts + ITE ≥ 30th percentile (12 mo) |
| Patient care | ≥ 6 Mini-CEX/CBD across ≥ 3 settings + EPA observations at target level |
| Communication | MSF from ≥ 3 rater groups + ≥ 2 reflective writings on specific encounters |
| Professionalism | MSF ≥ 3 groups + no unresolved professionalism flag |
| Practice-based learning | ≥ 1 self-directed learning plan with completed reassessment |
| Systems-based practice / QI | 1 completed PDSA cycle with documented outcome |

>>> QUALITY DIMENSIONS (rate the portfolio 1–4 on each)

AUTHENTICITY (1–4)
1 = Multiple artifacts lack attribution or appear copied.
2 = Some artifacts uncertain attribution.
3 = All artifacts attributed; signatures / timestamps present.
4 = All authenticated; cross-referenced across data sources (chart pulls, supervisor confirmations).
Rating: ___

SUFFICIENCY (1–4)
1 = Below threshold on > 1 competency.
2 = Below threshold on 1 competency.
3 = Meets threshold on all competencies.
4 = Exceeds threshold on most competencies.
Rating: ___

CURRENCY (1–4)
1 = > 50% of artifacts outside submission window.
2 = Some outside window.
3 = All within window.
4 = Distribution across the window (not bunched at one period).
Rating: ___

BREADTH (1–4)
1 = Evidence covers ≤ 2 of required settings / acuity / populations.
2 = Covers most but missing key areas.
3 = Covers all required.
4 = Covers all + diverse non-required (e.g., extra population, telehealth).
Rating: ___

DEPTH (1–4)
1 = Evidence at level below target (e.g., direct supervision only when target is indirect).
2 = Mixed; some at target some below.
3 = At target level consistently.
4 = At or above target; entrustment-ready evidence dominates.
Rating: ___

>>> REFLECTIVE-WRITING RUBRIC (Moon's levels)

LEVEL 1 — Descriptive
Anchor: Describes the event; no analysis, no naming of contributing factors. Example phrase: "The patient died and the family was upset."

LEVEL 2 — Reactive
Anchor: Describes + emotional reaction. No analysis. Example: "The patient died and I felt awful and questioned my career choice."

LEVEL 3 — Analytic
Anchor: Names contributing factor(s); applies a framework or principle; identifies specific change. Example: "The handoff omitted the rising lactate; I-PASS structure would have surfaced this. Next time I'll specifically use the actions-list element in I-PASS for any patient with rising clinical markers."

LEVEL 4 — Critically reflective
Anchor: Examines assumptions; integrates multiple perspectives (patient, team, system); identifies systemic factors; defines future practice change with measurable goal. Example: "I assumed the night team would surface deteriorating markers without explicit handoff. This reflects my assumption that vigilance is individual rather than systemic. Reviewing literature on handoff failures and consulting with the night team, I'll pilot a written-checklist supplement to I-PASS for high-watcher patients and track handoff-omission events for the next 8 weeks."

Per-entry rating: ___   (rate each reflective entry)
Portfolio reflective-writing summary: ___ (median across entries)

>>> SYNTHESIS DECISION (committee)
| Status | Criteria |
|---|---|
| Ready to advance | ≥ 3 quality dimensions at 3+; reflective median ≥ Level 3; sufficiency rating ≥ 3; no professionalism flag |
| Conditional / monitor | 1–2 dimensions at 2; action plan attached with named goals + reassessment date |
| Not ready / remediation | Any dimension at 1; or 3+ dimensions at 2; or reflective median fixed at Level 1; or unresolved professionalism flag |

Decision: ☐ Ready ☐ Conditional ☐ Not ready
If Conditional or Not ready, attach action plan with named goals + reassessment date.

>>> COMMITTEE NARRATIVE (≤ 150 words)
[Synthesis statement: triangulation of evidence, specific strengths, specific gaps, next-step recommendation.]

>>> COMMITTEE SIGNATURES
Committee members: ______________   Date: _______
Learner sign-off (acknowledges decision): ______________   Date: _______

>>> SOURCE-FIDELITY AUDIT
| Reference | Source | Status |
|---|---|---|
| Moon's levels of reflection | Moon 2004 "A Handbook of Reflective and Experiential Learning" | verified |
| Portfolio in CBME | Carraccio 2017 Acad Med | verified |
| Sufficiency + triangulation principle | van der Vleuten 2012 Med Teach | verified |

>>> REJECTED ELEMENT (minimum 1)
Considered: sufficiency rule "≥ 10 WBAs" without breadth specification.
Rejected: equates quantity with competency; learner could submit 10 Mini-CEX from same setting.
Replaced with: "≥ 6 Mini-CEX/CBD across ≥ 3 settings + EPA observations at target level."
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `program_type` | UME = lighter sufficiency; residency = full set; fellowship = adds scholarly weight |
| `framework_basis` | Maps competencies to ACGME / CanMEDS / EPAs / nursing / PA / pharmacy frameworks |
| `submission_window` | Default 12 months; shorter window for high-stakes phase decisions |
| `reflective_writing_weight` | Adjustable — programs prioritizing reflection may weight Level-3-or-above as a hard pass gate |
| `include_self_assessment` | Adds learner self-rating column for triangulation |
| `include_360_aggregate` | Brings MSF aggregate into the portfolio as one evidence stream |

## Verification Checklist

- [ ] Evidence-type taxonomy with 5 classes.
- [ ] Sufficiency thresholds per competency name quantity + breadth + quality (not quantity alone).
- [ ] 5 quality dimensions (authenticity, sufficiency, currency, breadth, depth) with 1–4 anchors.
- [ ] Reflective-writing rubric uses Moon's 4 levels with observable-text anchors.
- [ ] Synthesis decision rubric maps dimension scores to advance / monitor / remediate.
- [ ] Committee narrative section present.
- [ ] Source-fidelity audit populated.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `program_type = residency` (IM), `learner_level = PGY2`, `competencies = ACGME 6 core`, `submission_window = 12 months`.

**Output:** see Output Format block above — instantiated with IM-PGY2 thresholds and committee narrative format.
