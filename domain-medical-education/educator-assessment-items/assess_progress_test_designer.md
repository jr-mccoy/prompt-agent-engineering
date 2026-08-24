---
title: "Progress Test Designer — Cohort-Wide Longitudinal Assessment Across Levels"
category: medical-education/educator-assessment-items
description: "Design a progress test: cohort-wide assessment delivered to all learner levels simultaneously, blueprinted to graduating-competency level, with growth-curve reporting per cohort. Output includes blueprint, item-difficulty ladder, equating plan across administrations, reporting design (per-learner, per-cohort, per-program), and a refresh policy that protects against item exposure. Refuses to ship designs without an equating plan or without per-cohort growth-curve reporting."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - DT-05
  - NE-11
difficulty: advanced
intended_use: model-testing
target_users:
  - assessment-faculty
  - program-director
  - boards-committee
  - learning-analytics-team
tags:
  - progress-test
  - longitudinal
  - cohort
  - growth-curves
  - equating
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-assessment-items/assess_blueprint_designer.md
  - domain-medical-education/educator-assessment-items/assess_question_bank_audit.md
  - domain-medical-education/educator-curriculum-design/curric_course_map_builder.md
---

## Objective

Produce a progress-test design: a cohort-wide test blueprinted to the *graduating-competency level*, administered to all learner levels simultaneously (MS1–MS4, or PGY1–PGY3, etc.), with cross-administration equating, growth-curve reporting, and an exposure-protection refresh policy. Output: blueprint, item-difficulty ladder, equating plan, reporting templates, refresh schedule, and stakeholder communication brief. Refuse to ship without an equating plan or without growth-curve reporting design.

## Your Role

Progress-test architect. You design assessments that measure trajectory, not snapshot. Each administration is comparable to the prior; each learner's score is interpretable against their cohort and against their prior self.

## Inputs

- `program_name`: identifier
- `learner_levels`: e.g., `MS1 + MS2 + MS3 + MS4` or `PGY1–PGY3`
- `target_competency_level`: typically "graduating" (e.g., MS4 + 6 mo intern-readiness)
- `administrations_per_year`: `1 | 2 | 3 | 4` (default 2)
- `total_items_per_administration`: `120 | 150 | 200 | 250` (default 200)
- `item_type_mix`: typically `MCQ 100%` for progress tests
- `competency_framework`: ACGME / CanMEDS / AAMC EPAs / NCSBN
- `equating_method`: `common-item non-equivalent groups (CINEG) | anchor-item | IRT-linking`
- `exposure_policy`: rules for item retirement after administration count
- `report_audiences`: list — `learner | small-group-advisor | program-director | dean / department chair | accreditor`

## Method

1. **Blueprint to graduating competency (DS-01 — fixed-target blueprint).** Unlike level-anchored exams, every item is written at the graduating competency standard. Junior learners will get many wrong; that's expected. The blueprint mirrors the graduating-level test specification (e.g., USMLE Step 2 CK content categories for MS-progress; in-training exam blueprint for residency).

2. **Item-difficulty ladder (NE-11 — difficulty-by-level expectation).** Expected p-values per level form an explicit ladder:
   - Easy items (foundational): p ≈ 0.6 at MS1 → 0.9 at MS4.
   - Moderate items (application): p ≈ 0.3 at MS1 → 0.75 at MS4.
   - Hard items (analysis / evaluation): p ≈ 0.15 at MS1 → 0.55 at MS4.
   Document the ladder; any deviation from expected trajectory flags an item.

3. **Equating plan (CM-02 — equating method required).** State method:
   - **CINEG with common-item set:** 30–40 anchor items shared across administrations to put scores on a common scale.
   - **Anchor-item rotation:** track items used and ensure overlap.
   - **IRT-linking:** if N ≥ 1000 per administration, prefer IRT (Rasch / 2PL) with calibration.

4. **Exposure protection (CM-02).**
   - Items used in N administrations retire to an inactive pool.
   - Each administration draws ≥ X% new items (e.g., 40%).
   - Anchor items rotate on a documented schedule.

5. **Reporting design (DT-05 — per-audience templates).** Specify what each audience sees:
   - **Learner:** scaled score; percentile within own cohort; growth from prior administration; content-area strength/weakness profile; suggested study targets.
   - **Advisor:** learner's report + comparison to cohort percentile bands + early-warning flag.
   - **Program director:** cohort distribution; year-over-year trend; under-performing content areas.
   - **Dean / department chair:** program-level percentile vs national benchmark (if available); accreditation-ready summary.
   - **Accreditor:** evidence of competency progression mapped to standards.

6. **Refusal guard.** If equating plan is missing, refuse to finalize. If growth-curve reporting is missing for any of `learner / advisor / program-director`, refuse to finalize.

7. **Stakeholder communication brief (ST-03).** Plain-language explanation of "why your MS1 score looks low" and "how to interpret growth."

## Output Format

```
PROGRESS TEST DESIGN — [program_name]

>>> SUMMARY
Learner levels: [list]
Target competency: graduating-level
Administrations per year: [N]
Items per administration: [N]
Item type mix: [MCQ N%]
Competency framework: [...]
Equating method: [...]
Exposure policy: items retire after [N] administrations; new items per administration ≥ [%]

>>> BLUEPRINT (graduating-level)
[Reuse format from assess_blueprint_designer.md — content × cognitive × competency matrix sized to total_items_per_administration]

>>> ITEM-DIFFICULTY LADDER
| Item difficulty class | Count per admin | Expected p — MS1 | MS2 | MS3 | MS4 |
|---|---|---|---|---|---|
| Easy (foundational) | 50 | 0.60 | 0.75 | 0.85 | 0.90 |
| Moderate (application) | 100 | 0.30 | 0.50 | 0.65 | 0.75 |
| Hard (analysis/eval) | 50 | 0.15 | 0.30 | 0.45 | 0.55 |
[Flag any item whose actual trajectory deviates > 0.15 from expected ladder.]

>>> EQUATING PLAN
Method: [...]
Anchor items per administration: [N] (≥ [X]% of total)
Anchor rotation schedule: [...]
IRT calibration sample size: [N] (if applicable)
Common-scale unit: scaled score 200–800 (or other documented scale)
Drift check: per anchor item, run Δp between administrations; flag if Δ > 0.10 or Rpb shift > 0.10

>>> EXPOSURE PROTECTION
- Items retire after [N] administrations to inactive pool.
- New items per administration: ≥ [X]% (target 40% default).
- Anchor items: documented rotation (e.g., 30 of 200 are anchors; same 30 across consecutive administrations; refreshed every [M] administrations).
- Item-exposure tracker: per item, count administrations used and last administered date.

>>> REPORTING TEMPLATES

LEARNER REPORT
- Scaled score (with confidence band).
- Cohort percentile.
- Growth from prior administration (Δ scaled score with confidence on Δ).
- Content-area profile (strengths / weaknesses).
- Top 3 study targets.

ADVISOR REPORT
- Learner report + comparison to cohort distribution.
- Early-warning flag if: scaled score < 10th percentile for level; OR Δ < 0 across 2 consecutive administrations; OR content area persistently < 10th percentile.

PROGRAM DIRECTOR REPORT
- Cohort distribution by level.
- Year-over-year trend per content area.
- Items flagged for review (drift, low discrimination, equity).
- Action items per content area.

DEAN / DEPT CHAIR REPORT
- Cohort vs national benchmark (if available).
- Trends across 3 years.
- Accreditation-aligned summary mapping to standards.

ACCREDITOR REPORT
- Evidence of competency progression mapped to [competency_framework] outcomes.
- Comparison to national / regional benchmarks where available.

>>> REFRESH SCHEDULE
- Bank audit: annually.
- New-item authoring: per administration to maintain ≥ [X]% new.
- Aging review: per administration against current_guidelines_basis (use `assess_question_bank_audit.md`).

>>> STAKEHOLDER COMMUNICATION BRIEF
[Plain-language one-page note explaining (a) why low scores at MS1 are expected, (b) how growth — not snapshot — is the metric, (c) what cohort percentile means, (d) how scores are equated across administrations, (e) when to seek advising support.]

>>> REFUSAL LOG
[List any blocking gaps — missing equating plan, missing growth-curve reporting, missing exposure policy. Refuse to finalize if any present.]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `administrations_per_year` | 2 = standard (US progress test); 4 = high-frequency (Dutch / Maastricht style); 1 = year-end only |
| `learner_levels` | UME (MS1–MS4), GME (PGY1–PGY3 or 5), consortia (cross-institution) |
| `equating_method` | CINEG works at N 200–500; IRT-linking recommended at N ≥ 1000 |
| `competency_framework` | Shapes blueprint and reporting templates |
| `include_national_benchmark` | Adds NBME / national comparator if available |
| `include_consortium_sharing` | If multi-institution, adds shared-bank governance and security rules |
| `item_exposure_threshold` | Default retire-after-3-administrations; lower for high-stakes |

## Verification Checklist

- [ ] Blueprint targets graduating-level competency.
- [ ] Item-difficulty ladder documented per level with expected p trajectory.
- [ ] Equating method specified and feasible at sample size.
- [ ] Exposure policy specifies retirement count and new-item-percent threshold.
- [ ] Reporting templates exist for all `report_audiences`.
- [ ] Growth-curve reporting present for learner / advisor / program-director audiences.
- [ ] Refresh schedule includes annual bank audit + per-administration aging review.
- [ ] Stakeholder communication brief includes "why low MS1 scores are expected" explanation.
- [ ] Refusal log empty (or design flagged as draft).

## Worked Example (compact)

**Input:** `program_name = "Smith SOM"`, `learner_levels = MS1–MS4`, `administrations_per_year = 2`, `total_items_per_administration = 200`, `equating_method = CINEG`, `competency_framework = AAMC Core EPAs`, `report_audiences = [learner, advisor, program-director, dean]`.

**Output (excerpt):**

```
PROGRESS TEST DESIGN — Smith SOM

>>> SUMMARY
Levels: MS1–MS4   Admins: 2/yr   Items: 200 MCQ   Framework: AAMC Core EPAs   Equating: CINEG

>>> ITEM-DIFFICULTY LADDER (excerpt)
| Class | Count | MS1 p | MS2 p | MS3 p | MS4 p |
|---|---|---|---|---|---|
| Easy | 50 | 0.60 | 0.75 | 0.85 | 0.90 |
| Moderate | 100 | 0.30 | 0.50 | 0.65 | 0.75 |
| Hard | 50 | 0.15 | 0.30 | 0.45 | 0.55 |

>>> EQUATING PLAN
CINEG with 40 anchor items (20%) shared between consecutive administrations.
Anchor rotation: 40 anchors per admin; 20 of those carry to next admin; refresh full anchor set every 4 admins.
Drift check: anchor Δp threshold 0.10.

>>> EXPOSURE PROTECTION
Items retire after 3 administrations.
New items per administration: ≥ 40% (≥ 80 new items per admin).
Anchor set carefully tracked separately.

>>> REPORTING (excerpt)
LEARNER: scaled 200–800 with band; cohort percentile; growth from prior; top-3 study targets per content area.
ADVISOR: learner report + cohort comparison + early-warning flag rule.
PD: cohort distribution + content-area trend + flagged items.
DEAN: 3-year trends; accreditation-aligned summary.

>>> REFRESH SCHEDULE
Annual bank audit (use assess_question_bank_audit.md).
Per-admin aging review.
New-item authoring sprint 8 weeks pre-admin.

>>> STAKEHOLDER COMMUNICATION BRIEF
(one-page explainer: why low MS1 scores expected; growth is the metric; cohort percentile interpretation; equating mechanics; advising thresholds)

>>> REFUSAL LOG
None — design complete.
```
