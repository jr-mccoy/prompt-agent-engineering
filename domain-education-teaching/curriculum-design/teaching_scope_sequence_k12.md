---
title: "K-12 Scope & Sequence Architect (Multi-Year, Multi-Grade)"
category: education-teaching/curriculum-design
description: "Design a K-12 multi-year scope-and-sequence for a subject area — grade-by-grade and unit-by-unit, with standards anchoring, prerequisite logic, spiraling/revisiting patterns, and pacing windows accounting for testing calendars."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - DS-01
  - ED-01
  - QA-01
difficulty: advanced
tags:
  - education
  - curriculum-design
  - scope-and-sequence
  - k12
  - standards-alignment
  - vertical-alignment
  - district-curriculum
  - pacing
updated: "2026-05-15"
related_prompts:
  - teaching_curriculum_map_builder.md
  - teaching_vertical_alignment_auditor.md
  - teaching_horizontal_alignment_mapper.md
  - teaching_standards_alignment_audit.md
  - teaching_progression_map_designer.md
---

# K-12 Scope & Sequence Architect

**Objective:** Design a complete K-12 (or grade-band) scope-and-sequence for a subject area: which units are taught in which grades, in what order within each grade, anchored to specific standards, with prerequisite logic, spiraling/revisiting patterns, and pacing windows that respect testing calendars and instructional days.

## When to Use
- ✅ Building a district-level multi-year curriculum for a subject (math K-8, science 6-12, ELA K-5)
- ✅ Revising an existing scope-and-sequence after standards adoption (state CCR, NGSS, AP framework changes)
- ✅ Coordinating across feeder schools or grade-level teams
- ✅ Designing the pacing backbone before unit planning
- ❌ Designing a single unit (use `teaching_unit_curriculum_planner.md` or `teaching_unit_design_advanced.md`)
- ❌ Auditing vertical alignment of an existing sequence (use `teaching_vertical_alignment_auditor.md`)

## Inputs Required
- **Subject:** Math / ELA / Science / Social Studies / World Language / Arts / CTE / Other
- **Grade band:** K-2, 3-5, K-5, 6-8, K-8, 9-12, K-12
- **Standards framework:** state CCR, CCSS, NGSS, C3, state-specific (provide codes + text)
- **Instructional calendar:** instructional days per year, marking periods/quarters/trimesters, testing windows
- **Daily/weekly instructional minutes** per grade
- **Existing scope-and-sequence** (optional): to revise vs. build from scratch
- **District priorities:** equity commitments, ELL population, IEP/504 prevalence, advanced-learner programming
- **Vertical articulation needs:** alignment to feeder/receiver schools or post-secondary (e.g., AP, college readiness)
- **Adoption status:** materials adopted (curriculum, textbooks, resources)

## Constraints

**Must:**
- Honor the standards framework — every grade has standards-anchored units; no orphan units; no orphan standards
- Build a grade-by-grade × unit-by-unit grid with pacing in weeks (or days)
- Show prerequisite logic: each unit's prerequisites (within-grade and prior-grade)
- Designate spiral/revisit patterns for standards that recur across grades (with depth advancing: I → D → M)
- Reserve buffer days each quarter for reteaching, assessment, and unplanned events
- Honor testing windows (don't schedule a new high-stakes unit immediately before a state test)
- Sequence concepts before applications, foundational before integrative

**Must Not:**
- Generate a scope-and-sequence that exceeds instructional days available
- Drop standards required by the framework
- Treat all standards as equal pacing weight — power standards warrant more time
- Invent standards codes
- Front-load complex content where prerequisite knowledge has not been built
- Ignore developmental appropriateness (K-2 attention spans, abstract-reasoning emergence in middle grades)

## Instructions

1. **Confirm inputs.**
   - Echo back: subject, grade band, framework, instructional days/year, marking periods, testing windows, vertical articulation requirements, instructional minutes.

2. **Identify power standards per grade.**
   - From the framework, designate Power / Supporting / Enrichment for each standard.
   - **Power:** assessed on state/national tests; foundational for next grade; high-leverage across the subject
   - **Supporting:** built around power standards; deepens understanding
   - **Enrichment:** extends; addressed when time allows

3. **Compute instructional time available per grade.**
   - Subtract testing windows, district benchmark windows, mandated assemblies/events.
   - Reserve 10-15% as buffer.
   - Convert to instructional weeks.

4. **Generate unit list per grade.**
   - Each unit: title, primary standards (codes + brief text), supporting standards, estimated weeks.
   - Each unit ties to ≥1 power standard.

5. **Sequence within each grade.**
   - Anchor with developmental progression: simple → complex, concrete → abstract, single-skill → integrated.
   - Place unit prerequisites before their dependents.
   - Position high-cognitive-load units after foundational ones in the year.
   - Avoid placing new content in the week before a high-stakes assessment.

6. **Build vertical spiral.**
   - For standards that span multiple grades (typical for math operations, reading comprehension strategies, scientific practices), specify depth at each grade: I / D / M.
   - Verify M occurs at the grade the framework specifies (or earlier).

7. **Build horizontal coordination notes.**
   - Within each grade, identify standards that benefit from cross-subject coordination (e.g., 5th-grade ELA informational text reading aligned to 5th-grade science units).
   - Suggest pairing windows.

8. **Insert pacing windows.**
   - For each unit: start week, end week, summative assessment week, formative checkpoint dates.

9. **Audit the design.**
   - Total weeks per grade ≤ instructional weeks available (with buffer)
   - All power standards have M-depth coverage at the appropriate grade
   - All standards have ≥1 grade where they appear
   - Prerequisite logic is satisfied (no dependents before prerequisites)
   - Testing windows protected

10. **Produce the output.**

## Output Format

### Section 1: Design Identity
- Subject, grade band, framework + version, calendar inputs, district priorities, vertical articulation goals

### Section 2: Standards Inventory (per grade)

| Grade | Standard Code | Standard Text | Priority (Power/Supporting/Enrichment) |
|---|---|---|---|

### Section 3: Master Scope-and-Sequence Grid

For each grade:

**Grade [N] — [Subject]**

| Unit # | Title | Weeks | Start Wk | End Wk | Primary Standards | Supporting Standards | Depth (I/D/M) | Summative Assessment |
|---|---|---|---|---|---|---|---|---|

### Section 4: Vertical Spiral Map

For each standard that spans multiple grades:

| Standard | Grade K | Grade 1 | Grade 2 | Grade 3 | … |
|---|---|---|---|---|---|
| [code] | | I | D | M | (re-engage with new content) |

### Section 5: Horizontal Coordination Suggestions

| Grade | Window | Subject A Unit | Subject B Unit | Coordination Type |
|---|---|---|---|---|

### Section 6: Pacing Calendar (per grade)

Weeks 1-36 (or actual instructional weeks), with units, assessment dates, buffer days, testing windows marked.

### Section 7: Design Audit

| Audit Question | Result | Notes |
|---|---|---|
| Total weeks within available days | Pass / Fail | |
| All power standards Mastered by required grade | Pass / Fail | |
| All standards covered at least once | Pass / Fail | |
| Prerequisite logic satisfied | Pass / Fail | |
| Testing windows protected | Pass / Fail | |
| Buffer days reserved (10-15%) | Pass / Fail | |
| Developmentally appropriate sequencing | Pass / Fail | |

### Section 8: Implementation Notes
- Adoption-status considerations (existing materials fit / don't fit)
- District-priority alignment
- Vertical articulation flags
- Differentiation expectations (ELL, IEP, advanced learners)

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Equal time for every standard | Power standards warrant disproportionate time; one-size-fits-all pacing fails students | Tier standards (Power/Supporting/Enrichment) and pace accordingly |
| Generating a sequence that exceeds available days | The plan becomes aspirational and fails on contact with reality | Compute actual instructional days and pace within (with buffer) |
| Putting new content in the week before state tests | Students need review time, not new cognitive load | Reserve test-prep windows; sequence new units away from tests |
| Treating spiral as repetition | Re-encountering at same depth wastes time | Spiraling deepens: I → D → M across grades, not I → I → I |
| Front-loading abstract concepts | Developmental readiness matters; abstract reasoning emerges over middle grades | Foundational concrete before abstract; concrete-pictorial-abstract progression in math |
| Ignoring horizontal opportunities | Cross-subject pairing is high-leverage and easy to plan | Identify natural pairings (ELA informational text + content-area units) |
| Inventing standards codes | A scope-and-sequence with invented codes is unusable | Use framework's verbatim codes; flag if unverified |
| No buffer days | The plan is rigid and fails on snow days, assemblies, fire drills | Reserve 10-15% per quarter |

## Verification Checklist

- [ ] All grades in band addressed
- [ ] Every standard has ≥1 grade assignment
- [ ] Every unit ties to ≥1 power standard
- [ ] Vertical spiral shows depth progression (I → D → M)
- [ ] Total weeks per grade ≤ available
- [ ] Testing windows protected
- [ ] Buffer days included
- [ ] Prerequisite logic satisfied (within and across grades)
- [ ] Developmental progression honored
- [ ] No invented standards codes
- [ ] Horizontal coordination suggestions for high-leverage pairings
