# Education & Teaching Prompt Maintenance Backlog

Source: [`PROMPT_TEST_REVIEW.md`](PROMPT_TEST_REVIEW.md) recommendations (2026-03-07).

## Backlog Checklist

- [ ] **`teaching_exit_ticket_generator.md` — Add explicit answer-key separation guidance**  
  - **Prompt file:** `teaching_exit_ticket_generator.md`  
  - **Issue summary:** Prompt does not explicitly require separation of teacher answer key from student-facing ticket.  
  - **Priority:** Low  
  - **Proposed change:** Add instruction requiring a distinct “Teacher Copy / Answer Key” section separate from student handout output.  
  - **Owner:** `TBD`  
  - **Status:** `Not started`

- [ ] **`teaching_exit_ticket_generator.md` — Soften rigid ASCII template requirement**  
  - **Prompt file:** `teaching_exit_ticket_generator.md`  
  - **Issue summary:** Strict ASCII layout may reduce formatting reliability across models.  
  - **Priority:** Low  
  - **Proposed change:** Reframe the ASCII layout as recommended format, while allowing structurally equivalent alternatives.  
  - **Owner:** `TBD`  
  - **Status:** `Not started`

- [ ] **`teaching_study_flashcard_generator.md` — Add factual-accuracy verification guardrail**  
  - **Prompt file:** `teaching_study_flashcard_generator.md`  
  - **Issue summary:** No explicit quality check for factual correctness, creating risk in STEM content.  
  - **Priority:** Low  
  - **Proposed change:** Add explicit instruction to verify factual claims (e.g., names, formulas, mechanisms, reactions).  
  - **Owner:** `TBD`  
  - **Status:** `Not started`

- [ ] **`teaching_study_flashcard_generator.md` — Emphasize count rules over example length**  
  - **Prompt file:** `teaching_study_flashcard_generator.md`  
  - **Issue summary:** Long example may anchor models to example length instead of required card-count ranges.  
  - **Priority:** Low  
  - **Proposed change:** Add explicit “IMPORTANT” note that phase card-count ranges override example length.  
  - **Owner:** `TBD`  
  - **Status:** `Not started`

- [ ] **`teaching_assessment_rubric_builder.md` — Add assessment-type routing to avoid skip flows**  
  - **Prompt file:** `teaching_assessment_rubric_builder.md`  
  - **Issue summary:** Current structure forces users to skip inapplicable sections (e.g., MC/short answer for essay-only assessments).  
  - **Priority:** Medium  
  - **Proposed change:** Add up-front assessment-type selection and conditional step routing so only relevant sections render.  
  - **Owner:** `TBD`  
  - **Status:** `Not started`

- [ ] **`teaching_assessment_rubric_builder.md` — Merge overlapping extended-response/performance-task paths**  
  - **Prompt file:** `teaching_assessment_rubric_builder.md`  
  - **Issue summary:** Steps 4 and 5 are redundant for single-task essay assessments.  
  - **Priority:** Medium  
  - **Proposed change:** Merge or conditionally collapse these sections when assessment is a single extended writing task.  
  - **Owner:** `TBD`  
  - **Status:** `Not started`

- [ ] **`teaching_assessment_rubric_builder.md` — Add student-facing version as explicit step**  
  - **Prompt file:** `teaching_assessment_rubric_builder.md`  
  - **Issue summary:** Student-facing printable assessment appears in outputs but is not explicit in procedural steps.  
  - **Priority:** Medium  
  - **Proposed change:** Add a dedicated step that requires generation of a clean student-facing assessment artifact.  
  - **Owner:** `TBD`  
  - **Status:** `Not started`

- [ ] **`teaching_assessment_rubric_builder.md` — Add data-analysis template as explicit step**  
  - **Prompt file:** `teaching_assessment_rubric_builder.md`  
  - **Issue summary:** Data-analysis template appears in outputs but is not explicitly requested in step sequence.  
  - **Priority:** Medium  
  - **Proposed change:** Add a dedicated step for post-assessment data-analysis template creation.  
  - **Owner:** `TBD`  
  - **Status:** `Not started`

- [ ] **`teaching_assessment_rubric_builder.md` — Add essay-prompt design criteria**  
  - **Prompt file:** `teaching_assessment_rubric_builder.md`  
  - **Issue summary:** Prompt requires essay prompt generation but lacks quality criteria for good prompt design.  
  - **Priority:** Medium  
  - **Proposed change:** Add criteria (arguable, accessible, grade-appropriate, bias-aware) for essay prompt construction.  
  - **Owner:** `TBD`  
  - **Status:** `Not started`

- [ ] **`teaching_socratic_discussion_facilitator.md` — Enrich novice scaffold suggestions**  
  - **Prompt file:** `teaching_socratic_discussion_facilitator.md`  
  - **Issue summary:** Current novice scaffold guidance is minimal compared with high-value techniques found during testing.  
  - **Priority:** Low  
  - **Proposed change:** Add suggested scaffolds (e.g., Phone a Friend, Golden Passage, visual tracking, outer-circle observation roles).  
  - **Owner:** `TBD`  
  - **Status:** `Not started`

- [ ] **`teaching_socratic_discussion_facilitator.md` — Add teacher cheat-sheet deliverable**  
  - **Prompt file:** `teaching_socratic_discussion_facilitator.md`  
  - **Issue summary:** Teacher cheat sheet was highly useful in tested output but is not explicit in output requirements.  
  - **Priority:** Low  
  - **Proposed change:** Add explicit teacher-facing facilitation cheat-sheet output component.  
  - **Owner:** `TBD`  
  - **Status:** `Not started`

- [ ] **`teaching_socratic_discussion_facilitator.md` — Make pre-seminar written response essential for novices**  
  - **Prompt file:** `teaching_socratic_discussion_facilitator.md`  
  - **Issue summary:** Pre-seminar writing is not emphasized strongly enough for novice discussion groups.  
  - **Priority:** Low  
  - **Proposed change:** Require pre-seminar written response for novice cohorts to ensure all students enter with prepared ideas.  
  - **Owner:** `TBD`  
  - **Status:** `Not started`

## Definition of Done

A backlog item is complete only when the updated prompt:

1. Includes **revised examples** aligned to the new/updated instructions.
2. Includes explicit **output-contract checks** that verify required sections are present and correctly separated/formatted.
