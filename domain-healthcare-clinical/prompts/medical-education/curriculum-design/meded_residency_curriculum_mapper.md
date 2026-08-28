---
title: "Residency Curriculum Mapper (ACGME Milestones + EPAs)"
category: healthcare-clinical/medical-education/curriculum-design
description: "Build a residency program curriculum map: rotations × milestones × EPAs × assessment evidence — showing where each milestone is taught, practiced, and assessed; identifying gaps and redundancies; and producing the documentation needed for ACGME review."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - DS-01
  - QA-01
  - QA-02
difficulty: advanced
tags:
  - medical-education
  - residency
  - acgme
  - milestones
  - epa
  - curriculum-mapping
  - rotation-mapping
updated: "2026-05-15"
related_prompts:
  - meded_cbme_implementation_program.md
  - meded_epa_implementation_designer.md
  - meded_program_competency_framework_acgme.md
  - ../../../../domain-education-teaching/program/curriculum-design/program_curriculum_map_builder.md
---

# Residency Curriculum Mapper

**Objective:** Build a complete residency program curriculum map: rotations × ACGME Milestones × specialty EPAs × assessment evidence types — showing where each milestone is introduced, developed, and demonstrated; identifying gaps and redundancies; and producing the documentation expected by ACGME Annual Program Evaluation, Self-Study, and Site Visits.

## When to Use
- ✅ Building or revising a residency curriculum map for ACGME documentation
- ✅ Preparing for ACGME Self-Study with Site Visit
- ✅ Annual program evaluation (APE) curriculum-mapping section
- ✅ Identifying milestone or EPA coverage gaps in current rotation structure
- ❌ Designing a single rotation curriculum (use rotation-design prompts)
- ❌ Building the CBME implementation roadmap (use `meded_cbme_implementation_program.md`)

## Inputs Required
- **Specialty and program identity** (PGY years, learner count, training sites)
- **ACGME Milestones version for the specialty** (with verbatim language)
- **Specialty EPAs** (from specialty board or program-defined)
- **Rotation list** with duration, setting, supervision structure, scholarly/longitudinal experiences
- **Assessment inventory:** workplace-based assessments, ITEs, simulation, OSCEs, milestone evaluations
- **Existing rotation-milestone claims** (optional)

## Constraints

**Must:**
- Build three matrices: Rotation × Milestone (with I/D/M depth), Rotation × EPA (with entrustment-trajectory contribution), Rotation × Assessment Evidence
- Honor ACGME milestone language verbatim (cite for verification)
- Distinguish supplied evidence from inferred linkages
- Cover all six ACGME core competencies (Patient Care, Medical Knowledge, Practice-Based Learning and Improvement, Interpersonal and Communication Skills, Professionalism, Systems-Based Practice)
- Identify gaps (milestones with no rotation coverage, EPAs with no entrustment opportunity)
- Identify redundancies (milestones covered in many rotations with no Master-depth touch)

**Must Not:**
- Invent ACGME milestone or EPA text
- Treat rotation title as milestone evidence
- Inflate coverage by tagging every milestone at every rotation
- Confuse the six core competencies with the specialty sub-competencies (milestones operate at sub-competency level)
- Generate a map without the user's rotation list and assessment inventory

## Instructions

1. **Confirm inputs.** Echo specialty, Milestones version, rotation list, assessment inventory.

2. **Build the working milestone list.**
   - Extract specialty Milestones (verbatim, with version cite for verification)
   - Group by ACGME core competency

3. **Build the working EPA list.**
   - Specialty board EPAs OR locally defined EPAs aligned to specialty framework
   - For each EPA, the entrustment-supervision scale and target trajectory

4. **Build the rotation inventory.**
   - For each rotation: title, duration, setting, year(s) of training, supervision structure, scholarly activities, learning opportunities

5. **Build Matrix A: Rotation × Milestone (I/D/M).**
   - For each cell: based on rotation activities and assessments, what depth of milestone contribution?
   - Flag INFERRED for cells based on rotation description without explicit assessment evidence

6. **Build Matrix B: Rotation × EPA (entrustment trajectory contribution).**
   - For each cell: does this rotation contribute to entrustment for this EPA? At what trajectory phase (early observation / supervised practice / independent practice approaching entrustment)?

7. **Build Matrix C: Rotation × Assessment Evidence.**
   - For each rotation: what assessment evidence is generated (workplace-based assessments, simulation, OSCE, EITE, supervisor evaluations, MSF, patient outcomes)?
   - Map each evidence type to the milestones/EPAs it informs.

8. **Coverage audit.**
   - Every Milestone has ≥1 rotation at D depth
   - Every Milestone has ≥1 rotation at M depth by program completion
   - Every EPA has entrustment opportunities aligned to its trajectory
   - Every core competency has multiple-rotation, multi-modality coverage

9. **Gap and redundancy diagnostics.**
   - Uncovered: any milestone with no rotation
   - Mastery gaps: milestones with I/D but no M
   - Redundancy: milestones over-introduced without master-depth
   - EPA coverage gaps

10. **Recommendations.**
    - Specific rotations to add coverage to
    - Assessment types to add or retarget
    - Mastery touchpoints to designate

## Output Format

### Section 1: Map Identity
- Program, specialty, ACGME Milestones version, rotations in scope, assessment inventory

### Section 2: Milestone Inventory by Core Competency

| Core Competency | Sub-Competency / Milestone | Verbatim Language (verify) |
|---|---|---|

### Section 3: EPA Inventory

| EPA | Source | Entrustment Trajectory |
|---|---|---|

### Section 4: Rotation Inventory

| Rotation | Year(s) | Duration | Setting | Supervision | Key Activities |
|---|---|---|---|---|---|

### Section 5: Matrix A — Rotation × Milestone

|  | Mile-1 | Mile-2 | Mile-3 | … |
|---|---|---|---|---|
| Rotation 1 | I | D | | |
| Rotation 2 | | D | M | |

(With INFERRED flags as needed)

### Section 6: Matrix B — Rotation × EPA

| Rotation | EPA-1 | EPA-2 | … |
|---|---|---|---|

### Section 7: Matrix C — Rotation × Assessment Evidence

| Rotation | Assessment | Milestones / EPAs Informed |
|---|---|---|

### Section 8: Coverage Diagnostics by Core Competency

| Core Competency | Sub-Competencies | Coverage (I/D/M counts) | Status |
|---|---|---|---|

### Section 9: Gaps & Redundancies

| Type | Items | Recommendation |
|---|---|---|

### Section 10: Verification Notes
- Milestone language requiring source verification
- INFERRED linkages requiring program confirmation
- Rotation activities to confirm

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Inferring milestone coverage from rotation title | Title doesn't reflect actual activities or assessments | Use rotation descriptions + assessment evidence |
| All milestones at M for every rotation | Inflates coverage; hides gaps | Use I/D/M progression honestly |
| Inventing milestone text | Misalignment with ACGME version | Cite verbatim with verification flag |
| Treating six core competencies as milestones | They're broader categories | Milestones live at sub-competency level |
| Skipping EPA mapping | Misses CBME implementation | Map both Milestones and EPAs |
| No assessment evidence linkage | Coverage theoretical | Tie every coverage claim to assessment evidence |
| Confusing PGY year with milestone level | They're not synonymous | Milestone levels span PGY years variably |
| Hiding INFERRED linkages | Site visit reveals them | Maintain INFERRED tags |

## Verification Checklist

- [ ] Specialty Milestones version cited
- [ ] All six core competencies represented
- [ ] All Milestones in scope mapped to rotations
- [ ] EPA framework mapped to rotations
- [ ] Assessment evidence linked to rotations and milestones
- [ ] Every Milestone has ≥1 D-depth touch and ≥1 M-depth touch
- [ ] Gaps and redundancies surfaced
- [ ] INFERRED linkages flagged
- [ ] No invented milestone or EPA text
