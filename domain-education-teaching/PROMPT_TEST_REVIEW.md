# Education Prompt Test Review

**Date:** 2026-03-07
**Tested by:** Claude Code automated subagent evaluation
**Method:** Each prompt was executed by an independent subagent with realistic inputs. Outputs were reviewed for completeness, accuracy, classroom-readiness, and adherence to prompt structure.

---

## Summary

| # | Prompt | Test Scenario | Grade | Verdict |
|---|--------|---------------|-------|---------|
| 1 | Lesson Plan Generator | 7th grade Science — Photosynthesis, 50 min, ELL/IEP/gifted | A | No revision needed |
| 2 | Exit Ticket Generator | 4th grade Math — Adding fractions, 3 min | A | Minor improvements suggested |
| 3 | Analogy Engine | DNS explained to non-technical marketing team | A | No revision needed |
| 4 | Flashcard Generator | College Organic Chemistry — Functional groups | A | Minor improvements suggested |
| 5 | Assessment Rubric Builder | 10th grade ELA — Persuasive essay rubric | A- | Structural improvements suggested |
| 6 | Socratic Discussion Facilitator | 11th grade — "Letter from Birmingham Jail" | A | Minor improvements suggested |

**Overall finding: All 6 prompts produced high-quality, classroom-ready outputs. No prompt requires a major rewrite.** Three prompts have minor improvement opportunities, and one (Assessment Rubric Builder) has a structural issue worth addressing.

---

## Detailed Reviews

### 1. Lesson Plan Generator (`teaching_lesson_plan_generator.md`)

**Test scenario:** 7th grade Science, Photosynthesis, 50 minutes, 28 students including 3 ELL (Spanish-speaking), 2 IEP, 4 gifted learners. Full materials list provided.

**Output quality:**
- All 7 steps completed thoroughly
- 3 measurable SWBAT objectives at varied Bloom's levels (Understand, Analyze, Create)
- Realistic 50-minute timing with minute-by-minute breakdown
- Specific teacher language (actual questions to ask, not placeholders)
- Differentiation included Spanish cognates, bilingual lab sheets, scaffolded handouts
- Exit ticket with 3 questions targeting different objectives including a misconception-check
- Post-lesson reflection framework with specific questions

**Strengths:**
- The 5E model procedure is genuinely classroom-ready with practical teacher actions
- ELL support goes beyond "provide a bilingual dictionary" to include cognate highlighting and strategic pairing
- The misconception about plant mass coming from soil was explicitly addressed

**Issues found:** None significant.

**Revision needed:** No.

---

### 2. Exit Ticket Generator (`teaching_exit_ticket_generator.md`)

**Test scenario:** 4th grade Math, adding fractions with unlike denominators (1/3 + 1/4), Apply level, 3 minutes, mixed format, targeting specific misconceptions.

**Output quality:**
- All 4 steps completed
- 2 MC items with excellent diagnostic distractors (each wrong answer reveals a specific misconception)
- 1 short answer with exemplar, look-fors table, and common errors
- Clean ASCII student-facing ticket with self-assessment
- Data analysis plan with quick-sort, recording template, and decision tree

**Strengths:**
- Distractor design is genuinely diagnostic — each wrong answer reveals WHY the student is struggling, not just THAT they're struggling
- The decision tree (80%+ / 60-80% / 40-60% / <40%) with specific instructional responses is highly practical
- The misconception tally on the data recording template is a smart addition

**Issues found:**
1. The prompt doesn't explicitly instruct the model to separate the answer key from the student-facing ticket. The output handled this well ("Teacher Copy Only"), but the prompt should mention it.
2. The prompt's Step 3 ASCII template is quite rigid. Some models may struggle to reproduce it exactly, leading to formatting inconsistencies. Consider making the template format a suggestion rather than a strict requirement.

**Revision needed:** Minor — add a note about answer key separation; soften the ASCII template requirement.

---

### 3. Analogy Engine (`teaching_analogy_engine.md`)

**Test scenario:** Explain DNS to a non-technical marketing team. Replace the "phone book" analogy. Must capture hierarchical lookup, caching, multiple server types, and failure modes.

**Output quality:**
- Output Contract followed exactly — no internal process exposed
- Clean 5-part narrative (Setup, Mapping, Mechanism, Where It Breaks, The Upgrade)
- Structural Map with 8 element-to-element correspondences (exceeds the 4 minimum)
- "Where It Breaks" section is thorough and honest
- The "library reference desk" analogy is genuinely effective — structurally mapped, not just surface-level

**Strengths:**
- The "Internal Method / Output Contract" architecture works beautifully — the model does the analytical work but delivers only the polished artifact
- The analogy correctly captures the hierarchical narrowing (root → TLD → authoritative) which was the key requirement
- The Upgrade section (DNS propagation via "librarians working from yesterday's notes") adds real value
- The detailed "Where It Breaks" table prevents learners from over-extending the analogy

**Issues found:** None. This prompt was recently updated (2026-03-06) and is in excellent shape.

**Revision needed:** No.

---

### 4. Flashcard Generator (`teaching_study_flashcard_generator.md`)

**Test scenario:** College Organic Chemistry 1, functional group identification and reactivity basics. Student at "Developing" level (forgets carboxyl, confuses aldehydes/ketones, struggles with solubility prediction). Full multi-turn simulation.

**Output quality:**
- Natural conversational flow across all 4 phases
- 10-topic list appropriate for Orgo 1
- 4 calibration questions at escalating Bloom's levels
- 23 cards total (8 Tier 1, 10 Tier 2, 5 Tier 3) — appropriate distribution for Developing level
- Cards are factually accurate (chemistry content verified)
- Quizlet export block properly tab-separated
- Study order recommendation and follow-up question included

**Strengths:**
- The calibration phase feels genuinely adaptive — the model accurately diagnosed gaps and tailored cards accordingly
- Card quality is high: "Why it matters" lines connect each fact to exam relevance or bigger-picture understanding
- The Quizlet export block is actually copy-paste ready (tab-separated, newline-separated)
- Cards 19-23 (Tier 3) test synthesis and application, not just harder recall

**Issues found:**
1. The prompt doesn't include an explicit instruction to verify factual accuracy of generated cards. For STEM subjects especially, incorrect cards could be harmful to learning. Consider adding a quality check note: "Verify all factual claims. For scientific content, ensure chemical names, formulas, mechanisms, and reactions are accurate."
2. The prompt's example output (Biology) is excellent but quite long. Some models might produce shorter card sets to match the example's length rather than the explicit count guidance. The explicit count ranges in Phase 4 should take priority — consider bolding them or adding "IMPORTANT: follow the card count ranges, not the example length."

**Revision needed:** Minor — add factual accuracy note; emphasize card count guidance over example length.

---

### 5. Assessment Rubric Builder (`teaching_assessment_rubric_builder.md`)

**Test scenario:** 10th grade ELA, persuasive essay, end-of-unit summative. 3 learning objectives (argument construction, counterargument, academic language/structure). 90 minutes across 2 class periods.

**Output quality:**
- All 8 steps completed
- Assessment blueprint with Bloom's levels and point values
- Full analytical rubric with 4 criteria × 4 levels, specific observable descriptors
- Exemplary response sample (~520 words) that genuinely demonstrates Exemplary-level work
- Scoring guide with calibration protocol and grade conversion
- Accommodations guide covering 10 accommodation types
- Student-facing version formatted for printing
- Data analysis template with performance distribution and item analysis

**Strengths:**
- The rubric descriptors are specific and differentiable (not vague "good understanding" language)
- The exemplary response is genuinely strong writing — it could serve as a real anchor paper
- The scoring guide includes a calibration protocol (score anchor papers first, then compare) which is best practice
- The "Item Analysis — Common Patterns to Look For" table is exceptionally practical

**Issues found:**
1. **Structural redundancy:** Steps 2-3 (MC and Short Answer) were skipped as "not applicable." The prompt should handle assessment type routing more gracefully. Currently, for essay assessments, the user must specify "skip" for 2 steps. Consider restructuring the prompt to ask for assessment type upfront and then conditionally include only relevant steps.
2. **Steps 4 and 5 overlap:** For a pure essay assessment, the "Extended Response" (Step 4) and "Performance Task" (Step 5) sections cover substantially the same thing. The rubric appears twice in slightly different forms. Consider merging these steps when the assessment is a single extended writing task.
3. **Missing from prompt template:** The output included a student-facing assessment version and a data analysis template, but these are not explicitly listed in the prompt's Output Format section. The output format section lists them implicitly ("Student Assessment (clean version for printing)" and "Data Analysis Template") but the step-by-step instructions don't include steps for creating them. Add explicit steps.
4. **No prompt for the student:** The prompt template says to generate an essay prompt but provides no guidance on what makes a good essay prompt (arguable, accessible, grade-appropriate, avoidable bias). Consider adding brief essay prompt design criteria.

**Revision needed:** Moderate — restructure steps to avoid "skip" instructions; merge redundant steps for single-task assessments; add student-facing version and data analysis as explicit steps; add essay prompt design criteria.

---

### 6. Socratic Discussion Facilitator (`teaching_socratic_discussion_facilitator.md`)

**Test scenario:** 11th grade US History/ELA, "Letter from Birmingham Jail" (just/unjust laws section), novice discussers (first Socratic seminar), 45 minutes.

**Output quality:**
- All 7 steps completed thoroughly
- Text criteria checklist with specific passage recommendation (paragraphs 15-22)
- 9-question bank (2 opening, 5 core, 2 closing) plus 7 follow-up prompts
- Fishbowl format recommended for novices with detailed 45-minute timeline
- Comprehensive norms with "Teacher DOES / DOES NOT" table
- Facilitation moves for both stalls AND successes
- Participation tracking with contribution codes
- Detailed novice scaffolds including sentence starters, "Phone a Friend" rule, "Golden Passage" bookmark, and outer circle observation sheet

**Strengths:**
- The novice scaffolding is outstanding — "Phone a Friend," "Golden Passage," and the pre-discussion partner share are all creative and practical
- The teacher cheat sheet ("Before you speak, ask yourself...") is a brilliant touch for new facilitators
- The core questions genuinely promote analytical thinking, not just recall
- The facilitation moves tables are genuinely useful — not generic advice but specific language to use
- The progression plan at the end (retire sentence starters by Seminar 3, move to full circle by Seminar 4) helps teachers see the trajectory

**Issues found:**
1. The prompt template's Step 7 (Novice Discussion Scaffolds) provides only a brief progression timeline (Week 1-2, 3-4, 5+) and basic sentence starters. The output added several excellent scaffolds (Phone a Friend, Golden Passage, visual tracking, outer circle observation sheet) that the prompt doesn't mention. Consider enriching the prompt's novice scaffold section with these specific techniques as suggestions.
2. The prompt doesn't mention creating a "Teacher Cheat Sheet" as a deliverable, but the output included one and it was the single most useful artifact for a teacher running their first seminar. Consider adding it as an explicit output component.
3. The prompt could benefit from a note about the pre-seminar written response being essential (not optional) for novice groups — it guarantees every student has at least one prepared thought, which dramatically reduces the "no one talks" problem.

**Revision needed:** Minor — enrich novice scaffold suggestions; add teacher cheat sheet to output format; emphasize pre-seminar written response as essential for novice groups.

---

## Cross-Cutting Observations

### What works well across all prompts:
1. **Structured step-by-step instructions** produce consistently complete outputs
2. **Tables and structured formats** (rubrics, checklists, tracking sheets) are reliably generated
3. **Quality Indicators and Common Pitfalls** sections effectively constrain output quality
4. **False-Positive Prevention** sections (where present) noticeably improve output precision

### Patterns to address:
1. **Factual accuracy guardrails:** STEM-focused prompts (flashcards, lesson plans) should include a note about verifying factual correctness. Currently, only the Analogy Engine has explicit "stress-testing" for accuracy.
2. **Conditional step routing:** The Assessment Rubric Builder suffers from "skip these steps" instructions. Other prompts with conditional paths should handle routing more gracefully.
3. **Best practices discovered in outputs:** Several outputs included artifacts (teacher cheat sheets, outer circle observation sheets) that aren't in the prompt templates but are extremely useful. These should be added as suggested deliverables.

---

## Recommendations Summary

| Prompt | Priority | Action |
|--------|----------|--------|
| Lesson Plan Generator | None | No changes needed |
| Exit Ticket Generator | Low | Add answer key separation note; soften ASCII template |
| Analogy Engine | None | No changes needed |
| Flashcard Generator | Low | Add factual accuracy note; emphasize card count guidance |
| Assessment Rubric Builder | Medium | Restructure conditional steps; merge redundant sections; add explicit deliverables |
| Socratic Discussion Facilitator | Low | Enrich novice scaffolds; add teacher cheat sheet; emphasize pre-write |
