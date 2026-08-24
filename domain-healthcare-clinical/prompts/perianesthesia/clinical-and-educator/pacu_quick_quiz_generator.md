---
title: PACU Quick Quiz Generator (10-Question MCQ, Bloom-Structured)
category: pacu/education
task_type: LEARN
audience: PACU preceptor or educator building a 10-minute knowledge check from a topic primer or deep dive
updated: "2026-04-16"
tags:
  - pacu
  - quiz
  - mcq
  - knowledge-check
  - blooms
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - prompts/pacu_topic_primer.md
  - prompts/pacu_complication_deep_dive.md
  - prompts/pacu_medication_profile.md
  - prompts/pacu_unfolding_case_study.md
  - prompts/pacu_simulation_scenario_builder.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Bloom's Revised Taxonomy (Anderson & Krathwohl)
  - NCSBN Clinical Judgment Measurement Model (CJMM)
---

# PACU Quick Quiz Generator

> Safety reminder: Educational knowledge check only. Does not replace bedside preceptor observation, clinical judgment, or facility competency sign-off. All clinical specifics in rationales defer to provider order and facility protocol.

## Objective

Produce a **10-question multiple-choice quiz** from a provided PACU topic primer, deep dive, or medication profile — with Bloom's-taxonomy distribution (5 recall, 3 application, 2 analysis), plausible distractors, and rationales that cite the source chapter. Output is ready to hand to an orientee for self-testing, with an answer key block separable for preceptor-proctored mode.

## When to use

- Post-reading check on a `pacu_topic_primer.md`, `pacu_complication_deep_dive.md`, or `pacu_medication_profile.md`.
- Pre-test before a sim (`pacu_simulation_scenario_builder.md`) or emergency drill (`pacu_emergency_drill_designer.md`).
- Weekly knowledge check during orientation; reassessment knowledge check during remediation.
- Low-census-shift self-study.

## When not to use

- For judgment / reasoning assessment — use `pacu_unfolding_case_study.md` or a sim.
- For bedside skill assessment — use `pacu_skill_drill_designer.md` or direct observation.
- As the sole competency measure — knowledge checks correlate weakly with bedside performance.

## Inputs

- **Source material:** {{paste the topic primer / deep dive / med profile, OR reference the file name and chapter}}
- **Topic:** {{e.g., "post-spinal hypotension," "ondansetron PACU profile," "residual NMB recognition"}}
- **Target learner level:** {{Week 0–2, Week 2–6, Week 6–10, final sign-off}}
- **Mode:** {{self-test (answer key inline after each question) | preceptor-proctored (answer key in appendix)}}
- **Any specific learning objectives to hit:** {{optional — ensures coverage}}

## Audience / Scope

- **Primary user:** Preceptor or educator generating the quiz.
- **Learner:** Phase 1 PACU orientee.
- **Scope:** PACU Phase 1 orientation knowledge checks.

## Output requirements

```markdown
# {Topic} — PACU Quick Quiz ({N} questions, ~10 minutes)

> Safety reminder: Knowledge check only — bedside performance and facility protocol govern real patients. Rationales reference source chapters; verify against current facility policy and provider orders at the bedside.

## Instructions
- Read each question and choose the single best answer.
- {If self-test:} Answer key and rationale follow each question.
- {If preceptor-proctored:} Answer key is in the appendix at the end.
- Time budget: ~1 minute per question.

## Question Distribution (Bloom's)
| Bloom level | Question count | Typical verb |
|---|---|---|
| Recall / Remember | 5 | define, identify, list, name |
| Application / Apply | 3 | apply, calculate (qualitative), choose, demonstrate |
| Analysis / Analyze | 2 | differentiate, compare, interpret, infer |

---

## Question 1 — [Recall]
{Stem: one clear question, no trick wording, no double-negative}

A. {distractor — plausible to a novice, clearly wrong to a topic-aware learner}
B. {distractor — same}
C. {correct answer}
D. {distractor — same}

**Answer: C**
**Rationale:** {1–2 sentences, cites source chapter by title — e.g., "Drain's PeriAnesthesia Nursing, Ch. on Neuromuscular Blockade"}

---

[Questions 2–10 follow same pattern; recall Q2–Q5, application Q6–Q8, analysis Q9–Q10]

---

## Answer Key Summary
| Q | Correct | Bloom | Source |
|---|---|---|---|
| 1 | C | Recall | Drain's Ch. X |
| 2 | ... | ... | ... |
| ... | ... | ... | ... |
| 10 | ... | ... | ... |

## Learner Self-Assessment (after completion)
- **Recall score (Q1–Q5):** _____ / 5
- **Application score (Q6–Q8):** _____ / 3
- **Analysis score (Q9–Q10):** _____ / 2
- **Which Bloom level needs re-reading?** ...
- **Which source chapter / module to re-read first?** ...

## Sources / reference
- {Primary source chapter cited per question}
- ASPAN *Core Curriculum for PeriAnesthesia Nursing Practice*, {module}
- *Drain's PeriAnesthesia Nursing*, {chapters}
```

## Distractor design rules

- **Plausible to a novice, wrong to a topic-aware learner.** The distractor should be something a Week 2 orientee could reasonably choose; a Week 8 orientee should reject it quickly.
- **No "all of the above" / "none of the above" options** — they test test-taking skill, not knowledge.
- **No distractors that are true statements but don't answer the question** — that's a trick, not a teaching moment.
- **One clear correct answer per question.** If two options are defensible, rewrite.
- **Distractors are mutually exclusive** — no two options that could both be correct depending on interpretation.
- **Distractors tied to common misconceptions** (from "Common orientee mistakes" section of the deep dive, if available).

## Must / Must not

**Must:**
- Exactly 10 questions (default) or match user-specified count.
- Bloom distribution: 5 recall / 3 application / 2 analysis (default); match user-specified override.
- Each question has exactly 4 options (A / B / C / D), one correct, three distractors.
- Every rationale cites the source chapter by title (not invented number).
- Distractors follow distractor-design rules above.
- Application and analysis questions use realistic PACU scenarios, not abstract pharmacology.

**Must not:**
- Include "all of the above" or "none of the above" options.
- Include trick questions, double-negatives, or grammatically-inconsistent options.
- Invent doses, concentrations, thresholds, or lab values. If a question needs a number, use qualitative cues ("trending down," "persistently below baseline") OR pull a sourced number and cite it.
- Invent facility-specific policies, pager numbers, or equipment.
- Invent ASPAN or Drain's citations. Mark `{{confirm chapter}}` if unknown.
- Reference age, race, sex, disability, religion, national origin, pregnancy, license pathway, or prior unit as variables unless clinically essential (e.g., pregnancy-relevant pharmacology) — and then handled clinically, not as a performance signal.
- Include patient-identifying information (MRN, full name, full DOB, room number) in question stems.
- Write analysis-level questions that are actually recall in disguise — an analysis question requires comparing / differentiating / inferring.

## Quality signals

- Every question's rationale cites a specific source chapter.
- Distractors are plausible; a Week 2 orientee would be tempted, a Week 8 orientee would not.
- Application questions require the learner to apply a concept to a realistic PACU scenario.
- Analysis questions require the learner to differentiate between closely-related concepts.
- Self-assessment block helps learner identify which Bloom level needs re-study.

## Verification

Before returning the quiz, verify:

- [ ] Exactly 10 questions (or user-specified count).
- [ ] Bloom distribution matches default (5 / 3 / 2) or user override — verify per-question level in the answer-key table.
- [ ] Each question has 4 options, one correct.
- [ ] No "all / none of the above."
- [ ] No double-negatives or trick wording.
- [ ] Every rationale cites a source chapter.
- [ ] Distractors are plausible and tied to common misconceptions.
- [ ] Self-assessment block lets learner identify Bloom-level weakness.

## False-Positive Prevention

Do **not** fabricate:

- **No invented doses, drip rates, concentrations, or specific values in stems or distractors.** If a question uses a number, it must be sourced or qualitative.
- **No invented vital-sign thresholds** used as correct answers.
- **No invented ASPAN section / Drain's chapter citations.** Mark `{{confirm}}` if unknown.
- **No invented facility policies, protocols, or equipment specifics.**
- **No invented clinical trial results, incidence rates, or statistics** without citation.
- **No protected-characteristic references** used to steer answers.
- **No patient-identifying information** in stems.
- **No contradictions with the source primer / deep dive** — the quiz should reinforce the primer, not contradict it.

## Worked Example

<details>
<summary>Example: Two questions from a post-spinal hypotension quiz (click to expand)</summary>

```markdown
## Question 1 — [Recall]
Which of the following is the primary mechanism of post-spinal hypotension?

A. Direct myocardial depression from the local anesthetic reaching systemic circulation
B. Sympathetic blockade below the block level → vasodilation → reduced venous return
C. Acute blood loss from epidural vein puncture during needle placement
D. Opioid-induced histamine release from adjunctive intrathecal opioids

**Answer: B**
**Rationale:** The dominant mechanism is sympathetic blockade below the block level, causing vasodilation and reduced preload. Source: *Drain's PeriAnesthesia Nursing*, Ch. on Regional Anesthesia / Neuraxial Block Management.

---

## Question 7 — [Application]
A Week 4 PACU orientee admits a post-spinal patient. First-cycle BP is 128/78, second-cycle 118/72, third-cycle 108/68. The patient reports feeling "a little dizzy." The orientee's single best next action is:

A. Document the trend and continue the admission checklist
B. Reposition (legs elevated per order) and recheck BP before completing the checklist
C. Immediately push 500 mL fluid bolus without an order
D. Administer ephedrine from the crash cart

**Answer: B**
**Rationale:** At this point, the trend is recognizable and symptomatic but does not yet warrant unordered interventions. The orientee should reposition (within scope), recheck, and escalate by role. Fluid boluses and vasopressors require provider orders. Source: *Drain's PeriAnesthesia Nursing*, Ch. on Cardiovascular Assessment in PACU + ASPAN Core Curriculum hemodynamics module.
```

Notes: Q1 distractors are all mechanism statements — plausible to novice, clearly wrong to topic-aware learner; Q7 application uses a realistic PACU admission sequence without invented specific doses; correct answer is within nursing scope; distractor C and D represent real common misconceptions (acting without order); rationale cites chapter by title.
</details>

## Self-check

- [ ] 10 questions with correct Bloom distribution.
- [ ] 4 options per question, one correct.
- [ ] No all-of/none-of options, no trick wording.
- [ ] Every rationale cites source chapter.
- [ ] No invented doses, thresholds, or facility specifics.
- [ ] No patient-identifying information.
- [ ] No protected-characteristic references.
- [ ] Self-assessment block included.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed.
