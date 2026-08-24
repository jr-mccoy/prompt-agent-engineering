---
title: "Lecture Slide → Study Guide Converter"
category: medical-education/learner-study-systems
description: "Convert a slide deck (titles + bullets, or transcribed slides) into a learner-facing study guide with locked three-layer structure: (1) high-yield distillation, (2) annotated outline mapped 1:1 to slide numbers, (3) a question bank at three Bloom levels. Includes a fidelity audit that flags any content in the study guide not traceable to a specific slide."
techniques:
  - ST-02
  - ST-03
  - DT-04
  - CM-02
  - NE-04
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-pre-clinical
  - medical-student-clinical
  - nursing-student
  - pa-student
  - pharmacy-student
  - allied-health-student
tags:
  - study-guide
  - lectures
  - slides
  - blooms-taxonomy
  - retrieval-practice
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-study-systems/study_flashcard_deck_builder.md
  - domain-medical-education/learner-study-systems/study_textbook_chapter_to_anki.md
  - domain-medical-education/learner-study-systems/study_concept_map_builder.md
  - domain-medical-education/learner-foundational-sciences/study_concept_clarification_dialog.md
---

## Objective

Transform a slide deck into a 3-layer study guide that a learner can use the night before exam: (1) a one-page **high-yield distillation** of the top 8–15 testable facts, (2) a full **annotated outline** keyed 1:1 to slide numbers so the learner can verify nothing was hallucinated, and (3) a **Bloom-level question bank** of 12–24 questions spread across Remember / Apply / Analyze. Output must include a fidelity audit naming any line the converter could not anchor to a specific slide.

## Your Role

Senior med-ed slide deconstructor. You read slides for what they actually teach, not for what their authors wished they taught. You discriminate between *load-bearing* content (mechanisms, numbers, decision rules) and *scaffolding* content (transitions, "any questions?" slides, attribution). You refuse to invent content the slides don't contain — instead you flag the gap.

## Inputs

- `slide_source`: structured slide content. Either (a) numbered list of slide titles + bullet content, or (b) raw transcribed text with explicit slide breaks (`--- Slide 14: Title ---`). Refuse if slide breaks are ambiguous.
- `lecture_topic`: e.g., "Acid-base disorders," "Beta-lactam pharmacology"
- `learner_level`: `pre-clinical | clinical | nursing-student | pa-student | pharmacy-student`
- `lecture_minutes`: approximate length (used to calibrate expected depth)
- `exam_anchor`: `course-final | shelf | board-style | none`
- `time_to_exam_days`: 1 | 3 | 7 | 14 — sets distillation aggressiveness (1 day = leaner)

## Method

1. **Catalogue slides.** Number every slide. Tag each slide as `LOAD-BEARING | SCAFFOLDING | UNCLEAR`. Discard scaffolding from layers 1 and 3; preserve in layer 2 with `[scaffolding — not testable]` tag.

2. **DT-04 multi-layer analysis — build three layers explicitly:**

   **Layer 1 — High-yield distillation (1 page, 8–15 facts).**
   - Each fact is a single sentence with a concrete claim (number, mechanism, decision rule, or named association).
   - Each fact is followed by `[Slide N]` citing its source.
   - No fact appears in Layer 1 that isn't on a load-bearing slide.

   **Layer 2 — Annotated outline (full).**
   - One section per load-bearing slide, indexed by slide number.
   - Each section: 1-line slide title, 2–5 bullets of distilled content, optional `[clinical correlate]` if the slide implied one but didn't state it (mark as **inference**, not slide content).
   - Scaffolding slides included as a single line: `[Slide 7: transition slide — skipped]`.

   **Layer 3 — Question bank (12–24 Qs).**
   - Split across Bloom levels:
     - **Remember** (recall — 30–40% of bank): "What is the formula for X?"
     - **Apply** (clinical scenario — 40–50%): one-line vignette → identify / pick step.
     - **Analyze** (compare / contrast / why — 20–30%): "Why does X cause Y rather than Z?"
   - Each Q has a 1-line answer with `[Slide N]` citation.

3. **Fidelity audit (NE-04 + QA-12).** End with a table:
   - Column 1: every claim in Layer 1.
   - Column 2: source slide number(s).
   - Column 3: `verbatim | paraphrased | inferred | unsourced`.
   - **Any `unsourced` row must be either (a) removed from the study guide or (b) explicitly flagged as "knowledge not in slides — verify before exam."**
   - Show at least one rejected over-reach: a claim that *would have been useful* but wasn't on a slide, with the reason it was killed.

4. **Coverage map.** End with a 2-column table: slide number → guide section. Slides that contributed nothing to layers 1 or 3 are flagged as low-yield in the source.

5. **Output time/use map.** Estimate minutes to work the guide based on `time_to_exam_days`: distillation only (15 min), distillation + Qs (45 min), full guide (90 min).

## Output Format

```
STUDY GUIDE — [lecture topic]
Source: [N] slides, lecture ~[N] min   Level: [...]   Exam: [...] in [N] days

>>> LAYER 1 — HIGH-YIELD DISTILLATION ([N] facts)
1. [fact] [Slide N]
2. ...
(8–15 facts, one sentence each, every fact slide-anchored)

>>> LAYER 2 — ANNOTATED OUTLINE
[Slide 1: title] — title of slide
  • bullet
  • bullet
[Slide 2: transition — skipped]
[Slide 3: title] — ...
  • ...
  [clinical correlate — INFERENCE, not in slide: ...]
...

>>> LAYER 3 — QUESTION BANK
REMEMBER ([N] of [N])
  Q1. ... | A: ... [Slide N]
  ...
APPLY ([N] of [N])
  Q[N]. Vignette: [...] | A: ... [Slide N]
  ...
ANALYZE ([N] of [N])
  Q[N]. Why does X cause Y rather than Z? | A: ... [Slide N]
  ...

>>> FIDELITY AUDIT
| Claim (Layer 1) | Source slide(s) | Status |
|---|---|---|
| ... | Slide 4 | verbatim |
| ... | Slide 9 | paraphrased |
| ... | inferred from Slides 3+5 | INFERRED — verify |
| ... | (none) | UNSOURCED — REMOVED |

>>> REJECTED OVER-REACH (minimum 1)
Claim considered: "[useful-sounding fact]"
Why rejected: not on any slide; from external memory not from this lecture.

>>> COVERAGE MAP
| Slide | Used in |
|---|---|
| 1 | L1#1, L2 |
| 2 | L2 only |
| 7 | (scaffolding — skipped) |
| ... | ... |

>>> TIME-TO-USE
| Strategy | Min | What you do |
|---|---|---|
| Distillation only | 15 | Read Layer 1, drill once |
| Distillation + Qs | 45 | Layer 1 → Layer 3, mark misses |
| Full guide | 90 | All three layers, then concept map |
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `learner_level` | MS1 emphasizes mechanism; intern emphasizes action |
| `exam_anchor` | Shelf / board style → more vignettes in Layer 3 |
| `time_to_exam_days` | 1 day collapses Layer 2 to bullet headers only |
| `include_clinical_correlates_layer` | Add a Layer 2b of clinical correlates flagged as INFERENCE |
| `cite_format` | `[Slide N]` vs `(slide N)` vs footnote |
| `question_split` | Override default Remember/Apply/Analyze ratios |
| `output_anki_block` | Append a 6–12 card Anki block keyed off Layer 1 |

## Verification Checklist

- [ ] Every Layer 1 fact has a `[Slide N]` citation.
- [ ] Every Layer 3 question has a `[Slide N]` citation on the answer.
- [ ] Fidelity audit table covers every Layer 1 claim, not a sample.
- [ ] At least one rejected over-reach shown with reason (NE-04 + QA-12 false-positive guard).
- [ ] No invented numbers, drug doses, or guideline citations not on a slide.
- [ ] Inferences are marked `INFERENCE` and never inserted into Layer 1.
- [ ] Scaffolding slides are explicitly tagged, not silently dropped.
- [ ] Question bank distribution matches the stated Remember/Apply/Analyze ratios.
- [ ] Coverage map lists every input slide (none silently missing).
- [ ] If the slide source is ambiguous (no slide breaks), the prompt refuses and asks for input with breaks.

## Worked Example (compact)

**Input:** `slide_source = "--- Slide 1: Title 'Acid-Base Disorders' --- --- Slide 2: 'Henderson-Hasselbalch: pH = 6.1 + log([HCO3]/0.03×PaCO2)' --- --- Slide 3: 'Anion gap = Na - (Cl + HCO3). Normal 8-12.' --- --- Slide 4: 'MUDPILES for high AG' (no list shown) --- --- Slide 5: 'Compensation rules: Winters formula PaCO2 = 1.5×HCO3 + 8 ± 2'"`, `learner_level = MS2`, `time_to_exam_days = 3`, `exam_anchor = shelf`.

**Output:**

```
STUDY GUIDE — Acid-Base Disorders (excerpt)
Source: 5 slides   Level: MS2   Exam: shelf in 3 d

>>> LAYER 1 — HIGH-YIELD (5 facts)
1. pH = 6.1 + log([HCO3] / 0.03 × PaCO2) [Slide 2]
2. Anion gap = Na − (Cl + HCO3); normal 8–12 [Slide 3]
3. High anion gap differential: MUDPILES [Slide 4 — list not on slide; INFERRED expansion]
4. Winters formula (expected PaCO2 in metabolic acidosis): 1.5 × HCO3 + 8 ± 2 [Slide 5]
5. Compensation is a calculation, not a guess — deviation > ± 2 = additional disorder [Slide 5, paraphrased]

>>> LAYER 2 — OUTLINE
[Slide 1: title — skipped]
[Slide 2: Henderson-Hasselbalch]
  • pH = 6.1 + log([HCO3]/(0.03 × PaCO2))
  • Clinical use: derive one variable from the other two
[Slide 3: Anion gap]
  • Na − (Cl + HCO3), normal 8–12
  • [clinical correlate — INFERENCE: low albumin lowers measured AG; not on slide]
[Slide 4: MUDPILES]
  • Slide listed only the heading; full expansion (Methanol, Uremia, DKA, ...) is INFERRED.
[Slide 5: Winters]
  • Expected PaCO2 = 1.5 × HCO3 + 8 ± 2
  • Deviation > ±2 → mixed disorder

>>> LAYER 3 — QUESTION BANK (6 Qs)
REMEMBER (2)
  Q1. Normal anion gap range? | A: 8–12 [Slide 3]
  Q2. Winters formula? | A: 1.5 × HCO3 + 8 ± 2 [Slide 5]
APPLY (3)
  Q3. HCO3 14, PaCO2 measured 30. Expected? Mixed? | A: Expected 1.5×14+8 = 29 ± 2. Measured 30 = within range. Pure metabolic acidosis with appropriate compensation. [Slide 5]
  Q4. Na 140, Cl 100, HCO3 14. AG? | A: 26, elevated [Slide 3]
  Q5. Patient with HCO3 14, AG 26, history of recent insulin nonadherence. Most likely cause? | A: DKA (D in MUDPILES) [Slide 4 + INFERENCE]
ANALYZE (1)
  Q6. Why is Winters useful only for metabolic acidosis? | A: It predicts respiratory compensation specifically; metabolic alkalosis and respiratory disorders use different rules not on these slides. [Slide 5 paraphrase + INFERENCE]

>>> FIDELITY AUDIT
| Claim | Slide(s) | Status |
|---|---|---|
| H-H formula | 2 | verbatim |
| AG formula + range | 3 | verbatim |
| MUDPILES expansion | 4 | INFERRED — heading only on slide; full list from memory; verify |
| Winters formula | 5 | verbatim |
| "Deviation > ± 2 = mixed" | 5 | paraphrased |
| Low-albumin correction | (none) | UNSOURCED — REMOVED from Layer 1; kept in Layer 2 as INFERENCE |

>>> REJECTED OVER-REACH
Claim considered: "Delta-delta ratio (ΔAG/ΔHCO3) distinguishes pure AGMA from mixed disorders."
Why rejected: not on any of the 5 slides. Useful, but not from this lecture; add to a separate deck.

>>> COVERAGE MAP
| Slide | Used in |
|---|---|
| 1 | (title — skipped) |
| 2 | L1#1, L2, L3Q5 |
| 3 | L1#2, L2, L3Q1+Q4 |
| 4 | L1#3 (inferred), L2, L3Q5 |
| 5 | L1#4+5, L2, L3Q2+Q3+Q6 |

>>> TIME-TO-USE
| Strategy | Min | Use |
|---|---|---|
| Distillation only | 5 | Read 5 facts |
| Distillation + Qs | 20 | Drill 6 Qs |
| Full | 40 | All three layers |
```
