---
title: "Resident Didactic Curriculum Designer — Year-Long Conference Schedule, Topic Spiral, ITE-Aligned"
category: medical-education/educator-curriculum-design
description: "Design a year-long resident didactic curriculum: noon conferences / academic half-day / journal club / M&M / board-review schedule, spiral topic coverage across PGY1–3, ITE / board content alignment, attendance + accountability rules, and a learning-outcomes mapping back to ACGME milestones. Refuses curricula with Bloom-flat coverage, with topic redundancy across years at the same level, or without ITE blueprint alignment."
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
  - associate-program-director
  - chief-resident
  - faculty-developer
tags:
  - residency-curriculum
  - didactic
  - conference-schedule
  - ite-aligned
  - acgme-milestones
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-curriculum-design/curric_course_map_builder.md
  - domain-medical-education/educator-curriculum-design/curric_vertical_horizontal_integration_audit.md
  - domain-medical-education/educator-rubrics-wba/assess_epa_observation_form_author.md
  - domain-medical-education/educator-assessment-items/assess_blueprint_designer.md
---

## Objective

Produce a year-long resident didactic curriculum: weekly schedule (noon conference / academic half-day / journal club / M&M / board review) with topics, formats, presenters, target LOs, and ACGME-milestone mapping; spiral topic coverage across PGY1–3; ITE / board-content alignment; attendance and accountability rules. Refuse curricula with Bloom-flat year-over-year repetition, topic redundancy at the same Bloom level across years, or without alignment to the ITE / board blueprint.

## Your Role

Residency didactic curriculum architect. You design a year that ties weekly conferences to milestones, builds spiral coverage across PGY years, and aligns to the ITE blueprint without becoming a fact-cram. You'd rather drop a vanity lecture than break the spiral.

## Inputs

- `program_name`: identifier
- `specialty`: e.g., "Internal Medicine," "Family Medicine," "Pediatrics," "EM," "Surgery"
- `pgy_levels`: which years are included (PGY1 / PGY2 / PGY3, fellow if relevant)
- `weeks_per_year`: typically 48 (4 weeks vacation; varies)
- `conference_types`: subset of [noon conference, academic half-day, journal club, M&M, board review, simulation, IPE]
- `cadence`: weekly hours per type (e.g., noon × 4/wk, half-day × monthly, M&M × monthly)
- `ite_blueprint`: content blueprint of in-training exam or boards
- `milestone_framework`: ACGME specialty milestones
- `attendance_policy`: requirement (e.g., 70% noon-conference attendance per ACGME RC)

## Method

1. **Topic inventory + spiral structure (DS-01).**
   - Map specialty content into 30–60 major topics.
   - Distribute across PGY1–3 with rising Bloom level per topic.
   - PGY1 = foundations / application of management.
   - PGY2 = analysis / complex cases / outpatient continuity.
   - PGY3 = evaluation / teaching / supervisory.

2. **Year schedule build (ST-02).** Per week, slot conference types and topics:
   - Noon × 4: 3 didactic + 1 board-review or jeopardy.
   - Academic half-day: monthly deep-dive (3 h block).
   - Journal club: monthly.
   - M&M: monthly.
   - Simulation: quarterly.
   - IPE: 1–2 per year.

3. **Conference brief per session (DT-05 — content × LO × milestone).** Each session:
   - Topic + format + presenter.
   - 2–3 LOs.
   - Milestone tags.
   - Pre-reading (≤ 30 min).
   - Recap items for next week's retrieval drill.

4. **Spiral audit (QA-12).** Across the 3-year cycle, every major topic must:
   - Appear ≥ 2× across PGY1–3.
   - Rise in Bloom level on re-encounter OR appear in a different context.
   - Flag Bloom-flat repetitions (same topic at same Bloom level across years).

5. **ITE / board alignment (CM-02 — blueprint match).**
   - Match curriculum coverage % to ITE blueprint %.
   - Flag overweighted / underweighted areas.
   - Tighten coverage on board-relevant low-coverage areas.

6. **Attendance + accountability (CM-02).**
   - Attendance tracked per RC policy.
   - Failure-to-attend remediation: makeup via recorded conference + brief quiz.
   - Pre-conference retrieval drill (5-min open-question on prior week) to incentivize attendance.

7. **Milestone mapping (ST-03).**
   - Each conference tagged to ≥ 1 milestone subcompetency.
   - Year-end report: milestone coverage per resident from conferences (in addition to WBAs).

8. **Refusal guard.**
   - Bloom-flat repetition across years → refuse.
   - Missing ITE blueprint alignment → refuse.

9. **Source-fidelity audit (QA-12).** Cite ACGME RC requirements, ABIM / specialty board content outlines.

## Output Format

```
RESIDENCY DIDACTIC CURRICULUM — [specialty] — [program_name] — Weeks: [N]

>>> TOPIC INVENTORY × PGY SPIRAL
| Topic | PGY1 Bloom | PGY2 Bloom | PGY3 Bloom | Cross-year context shift |
|---|---|---|---|---|
| Heart failure | App | Analysis | Eval (teaching junior) | ward → cardiology rotation → supervisory |
| Sepsis | App | Analysis | Eval | ward → ICU → critical-care policy |
| GIM polypharmacy | App | Analysis | Analysis (geri) | adult → geriatric clinic → consultative |
| ...

>>> YEAR SCHEDULE (week × conference type)

WEEK 1
- Mon noon: HF foundations — PGY1 target — presenter [...] — LOs [...] — Milestones PC1, MK2
- Tue noon: Sepsis recognition — PGY1 target — [...]
- Wed noon: Board review — Endocrine drugs — Jeopardy — [...]
- Thu noon: Inpatient anticoagulation — PGY2 target — [...]
- Half-day (1st Wk of month): Acute kidney injury — analysis-level cases — all PGYs — [...]
- M&M: none this week.
- Journal club: none this week.

WEEK 2
[...]

[... 48 weeks ...]

>>> CONFERENCE BRIEF (per session)

Wk 1 Mon — HF foundations
Format: didactic + ARS
Time: 45 min noon
Presenter: [...]
LOs (3): [...]
Milestones: PC1, MK2
Pre-reading: [≤ 30 min]
Retrieval drill (next week): 4 ARS items at recall + application
Slides: 10 max; sparse text rule
Recording: yes

[... per conference ...]

>>> SPIRAL AUDIT
| Topic | PGY1 | PGY2 | PGY3 | Status |
|---|---|---|---|---|
| HF | App | Analysis | Eval | strong |
| AKI | App | Analysis | Analysis | Bloom-flat between PGY2-3 → flag |
| Antibiotic stewardship | App × 3 | | | Bloom-flat → flag |
| ECG arrhythmias | App | Analysis | Eval | strong |
| ...

>>> ITE BLUEPRINT ALIGNMENT
| ITE content area | ITE % | Curriculum coverage % | Status |
|---|---|---|---|
| Cardiovascular | 14 | 16 | over (acceptable) |
| Pulmonary | 10 | 8 | under |
| Endocrine | 9 | 6 | under — add 3 sessions |
| Renal | 6 | 7 | OK |
| GI | 8 | 9 | OK |
| ID | 10 | 8 | under — add 2 sessions |
| Rheum | 5 | 6 | OK |
| Heme/onc | 7 | 8 | OK |
| ...

>>> MILESTONE COVERAGE PER PGY YEAR
| Milestone (subcompetency) | PGY1 sessions covering | PGY2 | PGY3 |
|---|---|---|---|
| PC1 | 12 | 14 | 16 |
| PC2 | 8 | 12 | 14 |
| MK1 | 20 | 24 | 22 |
| MK2 | 18 | 22 | 20 |
| ...

>>> ATTENDANCE + ACCOUNTABILITY
- Target: 70% noon-conference attendance per ACGME RC.
- Makeup policy: recorded conference + 5-item retrieval quiz within 7 days.
- Pre-conference retrieval drill: 5-min open-question on prior week.
- Quarterly attendance report to PD + remediation if below threshold.

>>> GAP RESOLUTION
| Gap | Action |
|---|---|
| Endocrine ITE under-coverage (6% vs 9%) | Add 3 endocrine sessions: thyroid management; diabetes complications; pituitary disorders |
| ID under-coverage | Add 2 sessions: stewardship for inpatient; outpatient HIV PrEP |
| Bloom-flat AKI between PGY2-3 | Reframe PGY3 AKI as evaluation + consultative — supervise a junior workup |
| Bloom-flat antibiotic stewardship | Add PGY3 analysis-level session on antibiogram-driven empiric choice |

>>> SOURCE-FIDELITY AUDIT
| Reference | Source | Status |
|---|---|---|
| ACGME RC requirements | ACGME specialty-specific requirements | verified |
| ABIM IM content outline | ABIM 2024 IM content | verified |
| Spiral curriculum | Bruner 1960; Harden 1999 | verified |
| Active learning in didactics | Schwartzstein 2016 NEJM | verified |

>>> REJECTED ELEMENT (minimum 1)
Considered: repeating "HF foundations" lecture at PGY1, PGY2, PGY3 — same content.
Rejected: Bloom-flat repetition; violates spiral rule.
Replaced with: PGY1 foundations (application) → PGY2 cardiology-rotation analysis → PGY3 supervisory / teaching block.
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `specialty` | Drives ITE blueprint and content inventory entirely |
| `pgy_levels` | 2-year vs 3-year vs 4–7-year residency adjusts spiral depth |
| `weeks_per_year` | Typical 48; allows for vacation + flex weeks |
| `cadence` | Conference cadence per RC; some specialties academic-half-day-only |
| `milestone_framework` | ACGME specialty milestones drive tagging |
| `include_well_being_track` | Adds wellness + burnout-prevention sessions |
| `include_qi_track` | Adds QI / PDSA project block tied to SBP milestone |
| `include_research_block` | Adds scholarly half-day if program research-track |

## Verification Checklist

- [ ] Topic inventory × PGY spiral matrix populated.
- [ ] Every conference has topic / format / presenter / LOs / milestones / pre-reading / retrieval drill.
- [ ] Spiral audit shows rising Bloom or context shift per topic across years.
- [ ] ITE blueprint alignment table with overweight / underweight flags.
- [ ] Milestone coverage per PGY year tabulated.
- [ ] Attendance + accountability policy + makeup mechanism explicit.
- [ ] Gap resolution action list named.
- [ ] Source-fidelity audit populated.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `program_name = "Smith IM Residency"`, `specialty = Internal Medicine`, `pgy_levels = PGY1–3`, `weeks_per_year = 48`, `conference_types = [noon conference, academic half-day, journal club, M&M, board review, simulation, IPE]`, `cadence = "noon × 4/wk; half-day × monthly; M&M × monthly; JC × monthly; sim × quarterly; IPE × 2/yr"`, `ite_blueprint = ABIM 2024 IM content outline`, `milestone_framework = ACGME IM milestones`.

**Output:** see Output Format block above — instantiated with the 48-week IM-residency schedule, ABIM blueprint alignment table, and the gap-resolution actions (endocrine, ID coverage; Bloom-flat AKI / stewardship fixes).
