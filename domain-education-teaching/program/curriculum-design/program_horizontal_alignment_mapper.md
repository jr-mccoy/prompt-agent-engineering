---
title: "Horizontal Alignment Mapper (Cross-Disciplinary, Same Level)"
category: education-teaching/program/curriculum-design
description: "Map opportunities for cross-disciplinary alignment within a single grade or program level — coordinating timing of related content across subjects, identifying shared cognitive demands, and surfacing redundancies and contradictions across the curriculum experienced by the same learner."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - QA-01
difficulty: intermediate
tags:
  - education
  - curriculum-design
  - horizontal-alignment
  - cross-disciplinary
  - integration
  - k12
  - higher-ed
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/program/curriculum-design/program_vertical_alignment_auditor.md
  - domain-education-teaching/program/curriculum-design/program_scope_sequence_k12.md
  - domain-education-teaching/program/curriculum-design/program_curriculum_map_builder.md
---

# Horizontal Alignment Mapper

**Objective:** Map cross-disciplinary alignment opportunities within a single grade or program level: identify content windows where related material is being taught across subjects, where shared cognitive demands occur, and where contradictions or redundancies exist in the curriculum a single learner experiences in a given term/year.

## When to Use
- ✅ K-12 grade-level alignment (e.g., 5th-grade team coordinating ELA + science + social studies pacing)
- ✅ HE term-level coordination across courses (e.g., a learning community or paired courses)
- ✅ Integrated curriculum design (STEM, humanities-block, project-based programs)
- ✅ Identifying skill-transfer opportunities (writing across the curriculum, math across the curriculum)
- ❌ Cross-grade audit (use `teaching_vertical_alignment_auditor.md`)

## Inputs Required
- **Grade or program level**
- **Subjects / courses in scope**
- **Pacing per subject** (when each unit/module occurs)
- **Standards / outcomes per subject**
- **Coordination goal:** light coordination (timing only) / shared assignments / integrated unit design

## Constraints

**Must:**
- Build a time × subject grid showing what each subject is teaching when
- Identify natural pairings (related content within same time window)
- Identify cognitive demand overlap (writing tasks, mathematical reasoning, scientific inquiry across subjects)
- Flag contradictions (e.g., terminology conflicts, conflicting framework assumptions)
- Surface redundancies (same skill taught the same way in two subjects)

**Must Not:**
- Force coordination where content is genuinely unrelated
- Recommend integration that disrupts each subject's own progression
- Treat surface keyword overlap as deep coordination opportunity

## Instructions

1. **Build the time × subject grid.** Rows: subjects. Columns: time windows (weeks, units, modules). Cells: unit/module titles + key standards.

2. **Identify content pairings.** For each time window, scan across subjects for related content. Examples:
   - 5th-grade Westward Expansion (SS) + American historical fiction (ELA) + Geology of mountains and rivers (Science)
   - HE Statistics course + Research Methods course + capstone

3. **Identify cognitive-demand overlap.** Independent of content topic, where do subjects make the same cognitive demand (writing argumentative essays, building data tables, modeling causality)?

4. **Flag contradictions.** Cases where subjects use different definitions, conflicting frameworks, or contradict each other in ways that confuse learners.

5. **Flag redundancies.** Cases where the same skill is taught the same way in multiple subjects when it could be deepened by differentiation.

6. **Recommend coordination at three levels:**
   - **Timing alignment:** sequence units so related content occurs in same window
   - **Shared assignments:** one assessment spanning multiple subjects (e.g., research paper for ELA on a science topic)
   - **Integrated unit:** co-designed unit with shared outcomes

7. **Audit:** for each recommendation, verify it doesn't disrupt each subject's progression.

## Output Format

### Section 1: Map Identity
- Level, subjects, time horizon, coordination goal

### Section 2: Time × Subject Grid

| Week / Module | Subject A | Subject B | Subject C | Subject D |
|---|---|---|---|---|

### Section 3: Content Pairings

| Time Window | Subjects | Topic | Pairing Type (timing / shared assignment / integrated unit) |
|---|---|---|---|

### Section 4: Cognitive-Demand Overlap

| Demand | Subjects Sharing It | Coordination Opportunity |
|---|---|---|

### Section 5: Contradictions

| Concept / Term | Subject A Use | Subject B Use | Resolution |
|---|---|---|---|

### Section 6: Redundancies

| Skill | Subjects Teaching It | Consolidation or Differentiation Recommendation |
|---|---|---|

### Section 7: Coordination Recommendations

| Level | Recommendation | Affected Subjects | Disruption Risk |
|---|---|---|---|

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Forcing integration on unrelated content | Damages depth in each subject | Only recommend coordination where content/skill is genuinely related |
| Surface keyword pairing | "Energy" in ELA poetry ≠ "energy" in physics | Verify conceptual overlap, not lexical |
| Ignoring subject-specific progressions | Coordination that disrupts a subject's sequencing harms the discipline | Audit recommendations against each subject's vertical progression |
| Recommending only integrated units | Overkill for most pairings; lighter coordination is often more effective | Offer three tiers; pick least disruptive option that achieves goal |

## Verification Checklist

- [ ] Time × subject grid complete
- [ ] Pairings identified with type
- [ ] Cognitive-demand overlaps surfaced
- [ ] Contradictions and redundancies flagged
- [ ] Recommendations tiered by disruption level
- [ ] Each recommendation audited against vertical progressions
