---
title: "Vertical Alignment Auditor (Cross-Grade / Cross-Level)"
category: education-teaching/program/curriculum-design
description: "Audit a subject's curriculum across grades or program levels for vertical alignment — confirming that learning progressions, prerequisite logic, and depth advancement (Introduced → Developed → Mastered) actually compound across levels rather than repeat or skip."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - QA-01
  - QA-02
  - DS-01
difficulty: intermediate
tags:
  - education
  - curriculum-design
  - vertical-alignment
  - learning-progression
  - k12
  - higher-ed
  - audit
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/program/curriculum-design/program_horizontal_alignment_mapper.md
  - domain-education-teaching/program/curriculum-design/program_scope_sequence_k12.md
  - domain-education-teaching/program/curriculum-design/program_progression_map_designer.md
  - domain-education-teaching/program/curriculum-design/program_curriculum_map_builder.md
---

# Vertical Alignment Auditor

**Objective:** Audit a subject's curriculum across grades (K-12) or program levels (HE / workforce) for vertical alignment. Confirm that recurring standards or competencies advance in depth across levels (not just repeat); that prerequisite knowledge taught at one level supports content at the next; and that gaps (a standard that disappears without being mastered) and redundancies (a standard mastered then re-introduced at the same depth) are surfaced.

## When to Use
- ✅ Cross-grade audit (e.g., K-5 ELA, 6-12 math, K-12 science)
- ✅ Course-sequence audit within a higher-ed major
- ✅ Pre-K to K transition audit; middle-to-high transition; high-to-college articulation
- ✅ Apprenticeship pre-apprenticeship → apprenticeship → journey-level audit
- ❌ Same-grade cross-subject audit (use `teaching_horizontal_alignment_mapper.md`)
- ❌ Initial scope-and-sequence design (use `teaching_scope_sequence_k12.md` or `_he.md`)

## Inputs Required
- **Sector:** K-12 / HE / Workforce / Med-Ed
- **Subject / discipline**
- **Grade or level span:** which grades or program years are in scope
- **Standards or competencies framework:** with codes
- **Curriculum artifacts per grade/level:** scope-and-sequence, course/unit descriptions, assessments
- **Existing alignment claims** (optional): what the program claims about vertical progression

## Constraints

**Must:**
- Build a standard × grade matrix with depth (I/D/M) per cell
- For each standard that spans multiple grades, check that depth advances
- Flag four patterns: **Strong progression** (I → D → M with no regression), **Plateau** (D → D → D with no M), **Premature M** (M at lower grade than framework expects), **Disappearance** (taught then dropped without M), **Redundancy** (M then re-introduced at same depth)
- Distinguish supplied evidence from inferred

**Must Not:**
- Treat re-encountering content as advancement (depth must increase)
- Conflate horizontal coordination with vertical progression
- Recommend changes without evidence (cite the actual gap)
- Invent standards or curriculum content

## Instructions

1. **Confirm inputs and build the working standard list.** For each standard, note the framework's expected grade(s) for I, D, M.

2. **Build the depth matrix.** Rows: standards. Columns: grades/levels. Cells: I/D/M (or blank).

3. **Diagnose each row.**
   - Strong progression: I → D → M with each appearing at the right grade
   - Plateau: stuck at D, never reaches M
   - Premature M: M assigned before framework's grade
   - Disappearance: drops out before M
   - Redundancy: M then I/D again

4. **Diagnose prerequisite logic.**
   - For each grade, identify what content at higher grades depends on it.
   - Flag prerequisites taught after their dependents.

5. **Compute summary statistics.**
   - % of standards with strong progression
   - % plateauing / disappearing
   - % redundant

6. **Recommend specific changes.**
   - For plateaus: add Master-depth touch at appropriate grade
   - For disappearances: investigate (is it covered elsewhere? out of scope?)
   - For premature M: re-examine depth coding
   - For redundancies: consolidate or advance depth

## Output Format

### Section 1: Audit Identity
- Subject, span, framework, artifacts audited

### Section 2: Depth Matrix

|  | Grade K | Grade 1 | Grade 2 | … |
|---|---|---|---|---|
| [Standard] | I | D | M | |

### Section 3: Pattern Diagnostics

| Standard | Pattern | Notes |
|---|---|---|
| | Strong / Plateau / Premature M / Disappearance / Redundancy | |

### Section 4: Prerequisite Audit

| Prerequisite Standard (Grade) | Dependent Standard (Grade) | Issue (if any) |
|---|---|---|

### Section 5: Summary Statistics

| Pattern | Count | % | Standards |
|---|---|---|---|

### Section 6: Recommendations

| Standard | Issue | Specific Recommendation |
|---|---|---|

### Section 7: Verification Notes
- Inferred linkages flagged
- Out-of-scope candidates

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Re-teaching = advancement | Repeated teaching at same depth does not develop | Verify each subsequent encounter advances depth |
| Inferring depth from grade number | Frameworks specify expected grades; not all standards follow linear progression | Use framework-specified expectations |
| Suppressing the "Disappearance" finding | "It's covered somewhere" without evidence | Require curriculum-artifact evidence; flag honest gaps |
| Treating horizontal pairing as vertical alignment | These are different audits | Stay on the vertical axis (across grades, same subject) |
| Generic recommendations | Authors can't act on "improve alignment" | Specific: standard, grade, depth target, suggested unit |

## Verification Checklist

- [ ] Depth matrix complete across all in-scope standards × grades
- [ ] Each standard tagged with pattern
- [ ] Prerequisite logic checked
- [ ] Summary statistics reported
- [ ] Specific recommendations for each issue
- [ ] Inferred linkages flagged
