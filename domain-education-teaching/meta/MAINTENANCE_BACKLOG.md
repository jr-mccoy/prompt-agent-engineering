# Education & Teaching Prompt Maintenance Backlog

Source: [`PROMPT_TEST_REVIEW.md`](PROMPT_TEST_REVIEW.md) recommendations (2026-03-07).

> **2026-10-08:** All 12 items below are closed. Each updated prompt now carries a revised example and an **Output Contract Checks** section, per the Definition of Done. The flashcard prompt was renamed after the review: `teaching_study_flashcard_generator.md` is now `learner/memory-and-recall/learn_flashcard_generator.md` (see `REORG_MAP.tsv`).

## Backlog Checklist

- [x] **`teaching_exit_ticket_generator.md` — Add explicit answer-key separation guidance**  
  - **Prompt file:** `teaching_exit_ticket_generator.md`  
  - **Issue summary:** Prompt does not explicitly require separation of teacher answer key from student-facing ticket.  
  - **Priority:** Low  
  - **Proposed change:** Add instruction requiring a distinct “Teacher Copy / Answer Key” section separate from student handout output.  
  - **Owner:** `TBD`  
  - **Status:** `Done (2026-10-08)`
  - **Resolution:** New "Step 4: Create the Teacher Copy / Answer Key" (Data Analysis Plan is now Step 5); Output Format, "Example (abridged)" and "Output Contract Checks" enforce the separation.

- [x] **`teaching_exit_ticket_generator.md` — Soften rigid ASCII template requirement**  
  - **Prompt file:** `teaching_exit_ticket_generator.md`  
  - **Issue summary:** Strict ASCII layout may reduce formatting reliability across models.  
  - **Priority:** Low  
  - **Proposed change:** Reframe the ASCII layout as recommended format, while allowing structurally equivalent alternatives.  
  - **Owner:** `TBD`  
  - **Status:** `Done (2026-10-08)`
  - **Resolution:** "Step 3: Create the Student-Facing Exit Ticket" labels the template as recommended, not mandatory, and names acceptable equivalents; "Output Contract Checks" checks structure, not layout.

- [x] **`teaching_study_flashcard_generator.md` — Add factual-accuracy verification guardrail**  
  - **Prompt file:** `teaching_study_flashcard_generator.md` (now `learner/memory-and-recall/learn_flashcard_generator.md`)  
  - **Issue summary:** No explicit quality check for factual correctness, creating risk in STEM content.  
  - **Priority:** Low  
  - **Proposed change:** Add explicit instruction to verify factual claims (e.g., names, formulas, mechanisms, reactions).  
  - **Owner:** `TBD`  
  - **Status:** `Done (2026-10-08)`
  - **Resolution:** Phase 4 step 14 (verify names, formulas, mechanisms, reactions, dates, numbers) with the rule to flag uncertain facts for teacher review rather than guessing; extended False-Positive Prevention, "Output Contract Checks", and the example's accuracy-check line.

- [x] **`teaching_study_flashcard_generator.md` — Emphasize count rules over example length**  
  - **Prompt file:** `teaching_study_flashcard_generator.md` (now `learner/memory-and-recall/learn_flashcard_generator.md`)  
  - **Issue summary:** Long example may anchor models to example length instead of required card-count ranges.  
  - **Priority:** Low  
  - **Proposed change:** Add explicit “IMPORTANT” note that phase card-count ranges override example length.  
  - **Owner:** `TBD`  
  - **Status:** `Done (2026-10-08)`
  - **Resolution:** IMPORTANT line at Phase 4 step 12; Developing-level ranges added to the tiers; "Example Output" expanded to 19 cards (6/8/5) so it falls within the Developing ranges; tier-count check in "Output Contract Checks".

- [x] **`teaching_assessment_rubric_builder.md` — Add assessment-type routing to avoid skip flows**  
  - **Prompt file:** `teaching_assessment_rubric_builder.md`  
  - **Issue summary:** Current structure forces users to skip inapplicable sections (e.g., MC/short answer for essay-only assessments).  
  - **Priority:** Medium  
  - **Proposed change:** Add up-front assessment-type selection and conditional step routing so only relevant sections render.  
  - **Owner:** `TBD`  
  - **Status:** `Done (2026-10-08)`
  - **Resolution:** New "Step 1: Select Assessment Type and Route" (types A–E, route table, rendering rules: no "N/A" or skip headings); "Your Input" Assessment Type options updated; Blueprint became Step 2; steps renumbered with route tags.

- [x] **`teaching_assessment_rubric_builder.md` — Merge overlapping extended-response/performance-task paths**  
  - **Prompt file:** `teaching_assessment_rubric_builder.md`  
  - **Issue summary:** Steps 4 and 5 are redundant for single-task essay assessments.  
  - **Priority:** Medium  
  - **Proposed change:** Merge or conditionally collapse these sections when assessment is a single extended writing task.  
  - **Owner:** `TBD`  
  - **Status:** `Done (2026-10-08)`
  - **Resolution:** "Step 5: Extended Writing or Performance Task" is the single merged step, with a "Collapsed path for Type C" (one prompt, one rubric, one exemplar; Steps 7 and 9 reference 5b). The reserved empty step was removed.

- [x] **`teaching_assessment_rubric_builder.md` — Add student-facing version as explicit step**  
  - **Prompt file:** `teaching_assessment_rubric_builder.md`  
  - **Issue summary:** Student-facing printable assessment appears in outputs but is not explicit in procedural steps.  
  - **Priority:** Medium  
  - **Proposed change:** Add a dedicated step that requires generation of a clean student-facing assessment artifact.  
  - **Owner:** `TBD`  
  - **Status:** `Done (2026-10-08)`
  - **Resolution:** "Step 9: Student-Facing Assessment (all routes)" requires the full "STUDENT COPY" artifact; shown in "Example (abridged)" and verified in "Output Contract Checks".

- [x] **`teaching_assessment_rubric_builder.md` — Add data-analysis template as explicit step**  
  - **Prompt file:** `teaching_assessment_rubric_builder.md`  
  - **Issue summary:** Data-analysis template appears in outputs but is not explicitly requested in step sequence.  
  - **Priority:** Medium  
  - **Proposed change:** Add a dedicated step for post-assessment data-analysis template creation.  
  - **Owner:** `TBD`  
  - **Status:** `Done (2026-10-08)`
  - **Resolution:** "Step 10: Data Analysis Template (all routes)", with item-level analysis for MC/SA and criterion-level analysis for rubric-scored work; excerpt in "Example (abridged)".

- [x] **`teaching_assessment_rubric_builder.md` — Add essay-prompt design criteria**  
  - **Prompt file:** `teaching_assessment_rubric_builder.md`  
  - **Issue summary:** Prompt requires essay prompt generation but lacks quality criteria for good prompt design.  
  - **Priority:** Medium  
  - **Proposed change:** Add criteria (arguable, accessible, grade-appropriate, bias-aware) for essay prompt construction.  
  - **Owner:** `TBD`  
  - **Status:** `Done (2026-10-08)`
  - **Resolution:** Step 5a "Essay Prompt Design Criteria" (arguable, aligned, accessible, grade-appropriate, bias-aware, explicit, resource-bounded, feasible) plus a required "Prompt Design Check" table.

- [x] **`teaching_socratic_discussion_facilitator.md` — Enrich novice scaffold suggestions**  
  - **Prompt file:** `teaching_socratic_discussion_facilitator.md`  
  - **Issue summary:** Current novice scaffold guidance is minimal compared with high-value techniques found during testing.  
  - **Priority:** Low  
  - **Proposed change:** Add suggested scaffolds (e.g., Phone a Friend, Golden Passage, visual tracking, outer-circle observation roles).  
  - **Owner:** `TBD`  
  - **Status:** `Done (2026-10-08)`
  - **Resolution:** "Step 7: Novice Discussion Scaffolds" menu adds Outer-Circle Observer Roles, Visual Talk Tracking and Open Seat, alongside Phone a Friend, Golden Passage, partner share and the observation sheet; novice plans must use at least three.

- [x] **`teaching_socratic_discussion_facilitator.md` — Add teacher cheat-sheet deliverable**  
  - **Prompt file:** `teaching_socratic_discussion_facilitator.md`  
  - **Issue summary:** Teacher cheat sheet was highly useful in tested output but is not explicit in output requirements.  
  - **Priority:** Low  
  - **Proposed change:** Add explicit teacher-facing facilitation cheat-sheet output component.  
  - **Owner:** `TBD`  
  - **Status:** `Done (2026-10-08)`
  - **Resolution:** New "Step 8: Teacher Cheat Sheet" (five required components, one page), listed in Output Format and shown in "Example (abridged)".

- [x] **`teaching_socratic_discussion_facilitator.md` — Make pre-seminar written response essential for novices**  
  - **Prompt file:** `teaching_socratic_discussion_facilitator.md`  
  - **Issue summary:** Pre-seminar writing is not emphasized strongly enough for novice discussion groups.  
  - **Priority:** Low  
  - **Proposed change:** Require pre-seminar written response for novice cohorts to ensure all students enter with prepared ideas.  
  - **Owner:** `TBD`  
  - **Status:** `Done (2026-10-08)`
  - **Resolution:** Step 7 "Pre-Seminar Written Response (REQUIRED for novice cohorts)" with handout spec and door check; flagged in the Step 1 preparation table, Output Format item 8 and Common Discussion Pitfalls; handout shown in "Example (abridged)".

## Definition of Done

A backlog item is complete only when the updated prompt:

1. Includes **revised examples** aligned to the new/updated instructions.
2. Includes explicit **output-contract checks** that verify required sections are present and correctly separated/formatted.
