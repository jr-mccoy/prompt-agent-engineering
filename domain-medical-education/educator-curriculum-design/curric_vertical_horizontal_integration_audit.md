---
title: "Vertical + Horizontal Curriculum Integration Audit"
category: medical-education/educator-curriculum-design
description: "Audit a curriculum for vertical integration (foundational ↔ clinical years; classroom ↔ clinical workplace) and horizontal integration (across concurrent subjects within a phase). Detects siloed teaching, redundant content, gaps in spiral re-encounter, and missed integration opportunities. Outputs a heatmap of integration density per topic plus an action list. Refuses to mark a curriculum 'integrated' based only on stated intent — requires evidence in the LO × session × assessment map."
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
  - curriculum-designer
  - course-director
  - associate-dean
  - accreditation-self-study-team
tags:
  - integration
  - spiral-curriculum
  - vertical-integration
  - horizontal-integration
  - audit
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-curriculum-design/curric_course_map_builder.md
  - domain-medical-education/educator-curriculum-design/curric_clinical_clerkship_orientation_designer.md
  - domain-medical-education/educator-curriculum-design/curric_resident_didactic_curriculum_designer.md
---

## Objective

Audit a curriculum for vertical integration (foundational sciences ↔ clinical years; classroom ↔ workplace) and horizontal integration (across concurrent courses or subjects). Detect siloed teaching, redundant content, gaps in spiral re-encounter, and missed integration opportunities. Output an integration-density heatmap per topic, a gap-and-action list, and a recommended re-integration plan. Refuse to mark a curriculum "integrated" based only on stated intent — evidence in the LO × session × assessment map is required.

## Your Role

Integration auditor. You read curricula across years and courses simultaneously. Your standard is: a topic encountered in foundational year should re-appear at higher Bloom level in clinical year, in a related (not identical) context, and be assessed in a way that requires retrieval from prior encounters.

## Inputs

- `curriculum_scope`: e.g., `UME Years 1–4`, `residency PGY1–3`, `nursing pre-licensure 4 semesters`
- `topic_inventory`: list of major topics with the years/courses they appear in
- `lo_session_assessment_maps`: from `curric_course_map_builder.md` for each course
- `integration_target_density`: e.g., "every major topic should re-appear in ≥ 2 phases at rising Bloom levels"
- `horizontal_courses_concurrent`: which courses run concurrently within a phase
- `vertical_pairs`: which foundational topics should map to which clinical applications
- `accreditation_standards_relevant`: e.g., LCME 6.3, ACGME milestones, CCNE essentials

## Method

1. **Define integration types (DS-01).**
   - **Vertical integration:** topic re-appears across years / phases at rising Bloom levels (foundational → clinical → continuing).
   - **Horizontal integration:** topic taught simultaneously across concurrent courses with cross-references (e.g., pharm + path + clinical med all touching HF same week).
   - **Spiral re-encounter:** topic re-encountered ≥ 2× across curriculum at rising depth.

2. **Build the integration heatmap (DT-05 — topic × phase matrix).**
   - Rows: major topics.
   - Columns: phases / years / courses.
   - Cell: highest Bloom level achieved in that phase × topic intersection.
   - Empty cells flag gaps; same-Bloom-repeated cells flag redundancy.

3. **Vertical-integration audit (QA-12).**
   - For each foundational topic in Year 1, confirm clinical re-encounter at higher Bloom in Years 2–4.
   - Flag foundational topics with no clinical re-encounter.
   - Flag clinical topics with no foundational scaffold.

4. **Horizontal-integration audit (QA-12).**
   - For each major clinical topic in a phase, confirm concurrent course cross-references.
   - Flag siloed teaching (e.g., HF pathology Week 3, HF pharmacology Week 9, HF clinical Week 14 with no cross-tagging or shared cases).

5. **Spiral re-encounter audit (CM-02).**
   - Topic must be re-encountered ≥ 2× across curriculum.
   - Re-encounter must be at rising Bloom level OR in a different context (not identical lecture again).

6. **Refusal guard.** Mark "integrated" only if evidence exists in LO × session × assessment maps. Stated intent ("we integrate") without map evidence → refuse.

7. **Source-fidelity audit (QA-12).** Spiral curriculum reference (Bruner 1960; Harden 1999); integration ladder (Harden 2000).

## Output Format

```
INTEGRATION AUDIT — [curriculum_scope]

>>> INTEGRATION TYPES SCANNED
- Vertical integration: foundational → clinical → continuing.
- Horizontal integration: across concurrent courses in a phase.
- Spiral re-encounter: topic re-appears ≥ 2× with rising depth.

>>> INTEGRATION HEATMAP (topic × phase, Bloom level recorded)
| Topic | Year 1 | Year 2 | Year 3 | Year 4 | Status |
|---|---|---|---|---|---|
| Acid-base + AKI | App | Analysis | Analysis | (none) | siloed-late; Y4 re-encounter missing |
| Heart failure | App (path) | Analysis (pharm + clinical) | Analysis | Eval | well-integrated vertical |
| Antibiotic stewardship | App (path) | App (pharm) | App (clinical) | App | spiral re-encounter but Bloom-flat |
| Sepsis | (none) | App | Analysis | Eval | weak Y1 foundation |
| Ethics — capacity | App | (none) | App | (none) | gaps in 2 of 4 phases |

>>> VERTICAL-INTEGRATION AUDIT
| Foundational topic | Clinical re-encounter found? | Bloom rise? | Status |
|---|---|---|---|
| Renal physiology | yes (Y2, Y3) | App → Analysis | pass |
| Pulm gas exchange | yes (Y2) but only at App | no Bloom rise | flag |
| Immunology — autoimmunity | partial (Y2 path, no Y3 clinical re-encounter) | no | gap |
| ...

>>> HORIZONTAL-INTEGRATION AUDIT
| Phase | Concurrent courses | Topics taught with cross-reference | Topics siloed |
|---|---|---|---|
| Y2 Wk 5–7 | Path + Pharm + Clinical Med | HF, COPD, AKI (cross-tagged) | Diabetes (taught in pharm; not picked up in path / clinical med in same window) |
| Y3 Wk 1–4 | IM + Surgery clerkships | (none cross-tagged) | many |
| ...

>>> SPIRAL RE-ENCOUNTER AUDIT
| Topic | # encounters | Bloom progression | Status |
|---|---|---|---|
| Acid-base | 3 | App, Analysis, Analysis | partial (final encounter same Bloom) |
| Heart failure | 5 | App → App → Analysis → Analysis → Eval | strong |
| Sepsis | 3 | App → Analysis → Eval | strong |
| Antibiotic stewardship | 4 | App × 4 | Bloom-flat — recommend Analysis or Eval encounter in Y4 |
| ...

>>> GAP + REDUNDANCY SUMMARY
| Issue | Count | Example | Action |
|---|---|---|---|
| Siloed-late (no Y4 re-encounter) | 5 topics | Acid-base + AKI | Add Y4 elective module or AHC integration day |
| Bloom-flat re-encounters | 4 topics | Antibiotic stewardship | Add Analysis-level case in Y3 or Y4 |
| No foundational scaffold | 3 topics | Geriatrics pharmacology | Add Y1 foundations module |
| Horizontal silos (Y3) | many | IM ↔ Surgery clerkships not cross-referencing | Implement shared cases across clerkships |

>>> RE-INTEGRATION PLAN (priority order)
1. Add Y4 acid-base / AKI re-encounter case at Analysis level (1 session + portfolio entry).
2. Add Y4 Analysis-level antibiotic stewardship case (Bloom rise from App-flat).
3. Implement shared cases across IM and Surgery clerkships (≥ 4 shared cases over 12 wk).
4. Author Y1 geriatrics-pharmacology foundations module.
5. Add Y2 diabetes cross-reference in path + clinical med during pharm week.

>>> ACCREDITATION ALIGNMENT
| Standard | Status |
|---|---|
| LCME 6.3 (integration) | partial — see gaps above |
| ACGME milestones | n/a for UME audit |
| CCNE Essentials | n/a |

>>> SOURCE-FIDELITY AUDIT
| Reference | Source | Status |
|---|---|---|
| Spiral curriculum | Bruner 1960 "The Process of Education" | verified |
| Integration ladder (11 steps) | Harden 2000 Med Educ | verified |
| Constructive alignment | Biggs 1996 | verified |

>>> REFUSAL LOG
Considered marking curriculum "integrated" based on dean's statement.
Refused: no map evidence; only intent. Required map-based evidence for integration claim.
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `curriculum_scope` | UME 4-year / 3-year accelerated / residency 3-year / nursing 2-year |
| `integration_target_density` | Adjustable; default ≥ 2 phases per major topic at rising Bloom |
| `accreditation_standards_relevant` | LCME 6.3 / ACGME milestones / CCNE Essentials / WFME — adds standards-mapping table |
| `include_workplace_integration` | Maps classroom topics to specific workplace EPAs |
| `include_inter_professional` | Adds IPE integration check across nursing / pharmacy / PA curricula |
| `include_assessment_integration` | Verifies that integrated topics are assessed in integrated formats (e.g., progress test) |

## Verification Checklist

- [ ] Heatmap covers all major topics × phases.
- [ ] Vertical-integration audit done topic-by-topic.
- [ ] Horizontal-integration audit done phase-by-phase.
- [ ] Spiral re-encounter audit done with Bloom-progression check.
- [ ] Gap + redundancy summary with named topics + actions.
- [ ] Re-integration plan in priority order.
- [ ] Accreditation alignment table populated.
- [ ] Refusal log present (any "integrated" claim without map evidence rejected).
- [ ] Source-fidelity audit populated.

## Worked Example (compact)

**Input:** `curriculum_scope = UME Y1–Y4`, major topics = [acid-base + AKI, heart failure, antibiotic stewardship, sepsis, geriatrics pharmacology, ethics — capacity, diabetes, mental health].

**Output:** see Output Format block above — instantiated with the 8-topic heatmap, 4-priority re-integration plan, and LCME 6.3 alignment notes.
