---
title: "Flipped Classroom Module Designer — Pre-Work, In-Class Application, Reinforcement"
category: medical-education/educator-curriculum-design
description: "Design a flipped-classroom module: pre-class self-paced resources (videos, readings, foundational MCQ check), in-class application session (case-based / TBL / problem-solving), and post-class reinforcement (spaced retrieval, application to clinical work). Output includes pre-work spec with time budget, accountability mechanism (entry quiz / iRAT), in-class facilitation script, and reinforcement schedule. Refuses to ship without pre-work accountability mechanism or with content duplication between pre-class and in-class."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - DT-05
  - DS-29
difficulty: advanced
intended_use: model-testing
target_users:
  - clinical-educator
  - course-director
  - curriculum-designer
  - faculty-developer
tags:
  - flipped-classroom
  - pre-class
  - active-learning
  - tbl
  - spaced-repetition
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-curriculum-design/curric_lecture_outline_designer.md
  - domain-medical-education/educator-curriculum-design/curric_microlecture_script_author.md
  - domain-medical-education/educator-curriculum-design/curric_small_group_facilitation_guide.md
  - domain-medical-education/educator-case-writing/case_tbl_application_exercise_author.md
---

## Objective

Design a complete flipped-classroom module covering pre-class, in-class, and post-class phases: pre-work content + time budget + accountability mechanism (entry quiz / iRAT); in-class application script (TBL / case-based / problem-solving) with facilitator moves; post-class spaced retrieval + application-to-practice plan. Refuse to ship modules without pre-work accountability or with content duplicated across phases (pre-class teaches what's repeated in-class).

## Your Role

Flipped-classroom module architect. You design modules where pre-class builds foundation, in-class applies, post-class consolidates. You'd rather kill a beloved slide than repeat content between phases.

## Inputs

- `learner_level`: as before
- `topic`: e.g., "Heart failure pharmacology — GDMT"
- `LOs`: 3–5 ABCD LOs
- `total_module_hours`: e.g., 3 h (typical: 1.5 h pre-class + 1.5 h in-class + 30 min/wk × 4 wk post-class)
- `class_size`: small group (6–10) / medium (20–40) / large (≥ 50) — affects in-class format
- `tbl_or_case_based`: TBL / case-based / problem-solving (default TBL for medium-large, case-based for small)
- `accountability_mechanism`: `iRAT + tRAT (TBL)` / `entry-quiz` / `pre-class write-up`
- `pre_class_resource_types`: subset of [microlecture, reading, podcast, animated explainer, simulator]
- `post_class_reinforcement_window`: e.g., 4 weeks of spaced retrieval

## Method

1. **Lock LOs (CM-02 — no content drift).** All three phases (pre-class, in-class, post-class) trace to the same LOs.

2. **Phase 1 — Pre-class self-paced (DS-01 — pre-class shell).**
   - Time budget for learner: 45–90 minutes total (state per LO).
   - Content: microlecture(s) + reading(s) + optional animated explainer.
   - Each resource tagged to specific LO.
   - Accountability mechanism specified:
     - **iRAT (TBL):** 10-item individual MCQ at start of in-class.
     - **Entry quiz:** online MCQ due 24 h pre-class; counts toward grade.
     - **Pre-class write-up:** 1-paragraph commit on assigned case.
   - State sufficiency: pre-class should not include content that will be repeated in-class.

3. **Phase 2 — In-class application (DS-29 — triggered application sequence).**
   - Open with brief accountability check (review iRAT / quiz results; address common gaps).
   - Application activities ordered:
     - **TBL format:** iRAT (10 min) → tRAT team RAT (10 min) → application exercise sequence (1–3 cases, 4S — same problem, specific choice, simultaneous report, significant problem) → inter-team discussion → wrap.
     - **Case-based:** 1 progressive-disclosure case with 3–5 triggers; facilitator probes; group commits before reveal.
     - **Problem-solving:** structured worked examples → fading scaffolds → independent practice.
   - Per activity: time budget, facilitator script, expected wrong turns + redirects, scoring (if competitive).

4. **Phase 3 — Post-class reinforcement (DS-01 — spaced-retrieval shell).**
   - Spaced retrieval schedule: day 1, day 3, day 7, day 14, day 30 (or similar).
   - Items: 4–8 spaced-retrieval MCQs at application-or-analysis Bloom level.
   - Application-to-practice prompt: "In the next 7 days, when you encounter a patient with [LO topic], apply [specific behavior] and log one example."
   - Reinforcement check: brief quiz at week 4 or rotation transition.

5. **Duplication audit (CM-02 — no-content-duplication rule).** Sweep pre-class against in-class slides / content. If any specific concept is taught in both, flag and refuse. The rule: pre-class teaches concepts; in-class applies them.

6. **Refusal guard.** No accountability mechanism → refuse. Duplication ≥ 25% of in-class repeating pre-class → refuse.

7. **Source-fidelity audit (QA-12).** Clinical content cited. TBL framework cited (Michaelsen). Spaced-repetition reference cited (Cepeda 2008 meta-analysis).

## Output Format

```
FLIPPED MODULE — [topic] — Learner: [...] — Total: [N h]

>>> LOs
LO1 [Bloom]: [ABCD] → Competency: [...]
LO2 [...]
LO3 [...]
[3–5]

>>> PHASE 1 — PRE-CLASS (target learner time: [M] min)

Resource 1: [type] — [title]
Time: [N] min
LO: [...]
Content brief: [2–3 sentences]

Resource 2: [type] — [title]
[...]

Resource 3: [...]

Accountability:
- Mechanism: [iRAT / entry-quiz / write-up]
- Sample item:
  Q: [...]
  Options / response format: [...]
  Key: [...]
- Submission deadline: [...]
- Weight in grade: [%]

>>> PHASE 2 — IN-CLASS APPLICATION (target time: [M] min)
Format: [TBL / case-based / problem-solving]

[00:00–10:00] Accountability check
- Review iRAT / quiz histograms.
- Address top-3 common errors (named).
- 1-slide synthesis.

[10:00–20:00] tRAT (if TBL) or initial-case open
- Same MCQs, teams discuss + commit.
- Facilitator captures distribution; surfaces dissent.

[20:00–60:00] Application sequence
Activity 1: [name] — [time]
  Same problem (4S): [...]
  Specific choice: [...]
  Simultaneous report: scratch-off or vote-cards
  Significant problem: [...]
  Facilitator script (verbatim): "[...]"
  Common wrong turn: [...]
  Redirect: [open question]

Activity 2: [...]

Activity 3 (optional): [...]

[60:00–75:00] Wrap
- Synthesis of application activities.
- Surface application-to-practice prompt.

>>> PHASE 3 — POST-CLASS REINFORCEMENT (over [N] weeks)

Spaced retrieval schedule:
| Day | Item count | Bloom level | Delivery |
|---|---|---|---|
| 1 | 3 | application | LMS quiz |
| 3 | 3 | application | LMS quiz |
| 7 | 4 | analysis | LMS quiz |
| 14 | 4 | analysis | LMS quiz |
| 30 | 6 | analysis + evaluation | LMS quiz |

Sample items (3 of N):
SR1 [→ LO1]: [stem + options + key + rationale]
SR2 [→ LO2]: [...]
SR3 [→ LO3]: [...]

Application-to-practice prompt: "[Specific clinical behavior tied to LO; log 1 instance in EHR comment field; review with attending or in continuity clinic in 7 days]."

Reinforcement check at week 4: 6-item brief quiz + 1 reflective prompt.

>>> DUPLICATION AUDIT
| Pre-class concept | In-class concept | Duplication % | Status |
|---|---|---|---|
| [GDMT drug classes named] | [GDMT drug classes named again] | 30% | fail → in-class drops re-listing; opens directly with case |
| ... |

>>> CROSS-MODULE AUDIT
| Risk | Status |
|---|---|
| Accountability mechanism specified | pass |
| Pre-class time budget within 45–90 min | pass |
| In-class blocks tied to LOs | pass |
| Post-class schedule includes spacing intervals | pass |
| No content duplicated > 25% across phases | pass |

>>> SOURCE-FIDELITY AUDIT
| Reference | Source | Status |
|---|---|---|
| Clinical content | [...] | verified |
| TBL framework (4S, RAT) | Michaelsen 2008 | verified |
| Spaced retrieval | Cepeda 2008 Psychol Sci | verified |
| Flipped-classroom evidence in med ed | Hew 2018 BMC Med Educ systematic review | verified |

>>> REJECTED ELEMENT (minimum 1)
Considered: 30-minute in-class lecture re-explaining GDMT classes.
Rejected: duplicates pre-class microlecture.
Replaced with: 8-minute accountability check + immediate move to application activities.
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `total_module_hours` | Adjusts phase distribution; minimum viable = 30 min pre + 60 min in-class + 4 wk reinforcement |
| `class_size` | Small → case-based / Socratic; medium → TBL; large → TBL + ARS |
| `accountability_mechanism` | TBL → iRAT; non-TBL → entry-quiz or pre-class write-up |
| `pre_class_resource_types` | Microlecture preferred for procedural; reading for conceptual; animated for mechanisms |
| `post_class_reinforcement_window` | Default 4 weeks; longer for high-yield / boards material |
| `include_continuous_assessment_link` | Ties post-class application prompt to portfolio entry |

## Verification Checklist

- [ ] All 3 phases present (pre, in, post).
- [ ] LOs traced across all phases.
- [ ] Pre-class time budget 45–90 min stated.
- [ ] Accountability mechanism named.
- [ ] In-class format matches `class_size`.
- [ ] In-class activities tagged to LOs and time-budgeted.
- [ ] Post-class spaced-retrieval schedule defined.
- [ ] Application-to-practice prompt present.
- [ ] Duplication audit shows ≤ 25% overlap.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `learner_level = PGY1 IM`, `topic = "HF GDMT titration"`, `total_module_hours = 3`, `class_size = medium (24)`, `tbl_or_case_based = TBL`, `pre_class_resource_types = [microlecture, reading]`, `post_class_reinforcement_window = 4 weeks`.

**Output:** see Output Format block above — instantiated with HF GDMT case + iRAT/tRAT structure + 5-point spaced retrieval over 4 wk.
