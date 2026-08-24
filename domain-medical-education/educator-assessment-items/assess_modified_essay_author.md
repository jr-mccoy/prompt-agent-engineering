---
title: "Modified Essay Question (MEQ) Author — Sequential Disclosure with Locked Marking Scheme"
category: medical-education/educator-assessment-items
description: "Author a modified essay question with serial disclosure: stem → 4–8 sequential sub-questions revealed one at a time, each with its own bounded prompt, expected response, mark allocation, and exemplar anchors. Includes a no-backtrack rule (later answers cannot revise earlier ones) and a source-fidelity audit. Refuses prompts that depend on the examinee having read ahead."
techniques:
  - ST-02
  - ST-03
  - DS-29
  - CM-02
  - DT-05
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - assessment-faculty
  - item-writer
  - course-director
  - residency-program-director
tags:
  - meq
  - modified-essay
  - sequential-disclosure
  - assessment
  - marking-scheme
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-assessment-items/assess_short_answer_constructed_response_author.md
  - domain-medical-education/educator-assessment-items/assess_oral_exam_question_author.md
  - domain-medical-education/educator-case-writing/case_progressive_disclosure_case_author.md
---

## Objective

Produce a modified essay question (MEQ) with sequential disclosure: opening stem → 4–8 sub-questions released in order, each with its own bounded prompt + expected response + mark allocation + anchors at full / partial / no credit. The MEQ enforces a no-backtrack rule (the examinee cannot revise prior answers after seeing later disclosures). Output a complete marking pack: question booklet (per-page disclosures), marking scheme, and source audit. Refuse prompts that require the examinee to have read ahead.

## Your Role

MEQ author trained in the UK / Commonwealth medical-school tradition where the MEQ tests sequential clinical reasoning under information release. You enforce the no-backtrack rule and engineer each disclosure to surface one decision.

## Inputs

- `exam_style`: `course-final | clinical-clerkship-final | residency-mock | OSCE-knowledge-station-extended`
- `learner_level`: as before
- `content_domain`: e.g., "Pediatric DKA progression," "Postpartum hemorrhage cascade"
- `sub_question_count`: `4 | 5 | 6 | 7 | 8` (default 6)
- `mark_total`: `20 | 30 | 40 | 50` (default 30)
- `cognitive_level_progression`: ladder, e.g., `recall → application → analysis → evaluation`
- `time_minutes`: `20 | 30 | 45 | 60` (default 30)
- `target_misconception_per_step`: 1 misconception per sub-question (optional but recommended)

## Method

1. **Architect the disclosure sequence (DS-29 — sequential trigger pattern).** Each sub-question reveals new information AND asks a focused question. The information release must be irreversible: once disclosed, the examinee writes the answer and cannot return to revise earlier responses.

2. **Lock each sub-question prompt (CM-02 — bounded verbs).** Each prompt uses a specific verb: list, calculate, justify, predict, prioritize. Specify the number of items and word/element budget.

3. **Allocate marks (ST-02).** Distribute `mark_total` across sub-questions with a typical pattern of escalating weight as cognitive level rises. Sum must equal `mark_total`.

4. **Author expected responses + anchors (DT-05).** Per sub-question, provide:
   - Expected response elements with mark weights.
   - Full-credit exemplar.
   - Partial-credit exemplar with named missing element.
   - No-credit exemplar showing the named misconception or off-target answer.

5. **No-backtrack rule (CM-02 — irreversibility lock).** Each disclosure includes the line: "Do not revise earlier answers. Continue forward." Marking scheme says: earlier-answer revisions seen on later pages are ignored or zero'd.

6. **Cluing-flaw + leak audit (QA-12).** Sweep for:
   - Sub-question 2 inadvertently reveals the answer to sub-question 1.
   - Sub-question N references data not yet disclosed.
   - Off-target prompts that have no anchor in the released information.

7. **Source-fidelity audit (ST-03).** Every clinical claim cited traces to current standard.

## Output Format

```
MEQ — [content_domain] — [exam_style] — Time: [N min] — Marks: [N]

>>> COVER PAGE (visible to examinee)
[Brief instructions: "This question discloses information in sequence. Answer each part before turning to the next. DO NOT revise earlier answers. Time: [N] min. Marks: [N]."]

>>> PAGE 1 — OPENING STEM + Q1
STEM: [2–5 sentences. Initial scenario.]
Q1: [bounded prompt; e.g., "List THREE most likely diagnoses in order of probability and JUSTIFY each in ONE sentence. (6 marks)"]
[Response space.]
"Turn the page. Do not revise above."

>>> PAGE 2 — DISCLOSURE 1 + Q2
DISCLOSURE: [new data; e.g., labs, exam finding, time advance.]
Q2: [bounded prompt. (X marks)]
[Response space.]
"Turn the page. Do not revise above."

>>> PAGE 3 — DISCLOSURE 2 + Q3
[as above]

(repeat for sub_question_count)

>>> MARKING SCHEME (for examiner; not shown to examinee)

Q1 (6 marks)
| Element | Marks | Acceptable variants |
|---|---|---|
| [...] | [...] | [...] |
Full-credit exemplar: [...]
Partial-credit exemplar (4/6): [...]. Missing: [element].
No-credit exemplar: [...]. Misconception: [...].

Q2 (X marks)
[as above]

...

>>> CLUING + LEAK AUDIT
| Risk | Status |
|---|---|
| Q[n+1] reveals answer to Q[n] | pass / fail |
| Q[n] depends on data not yet disclosed | pass / fail |
| Examinee can guess later answers without engaging earlier | pass / fail |
| Prompt verb is bounded | pass / fail |

>>> BLUEPRINT TAGS
| Field | Value |
|---|---|
| Exam style | [...] |
| Content area | [...] |
| Cognitive progression | [...] |
| Mark total | [...] |
| Time | [...] |
| Inter-rater target | κ ≥ 0.8 |
| Target misconceptions | [list per sub-question] |

>>> SOURCE-FIDELITY AUDIT
| Clinical claim | Source | Status |
|---|---|---|
| [each #/threshold] | [...] | verified / [verify before use] |

>>> REJECTED ELEMENT (minimum 1)
Considered: [a disclosure that leaks the next answer]
Why rejected: [leak / cluing]
Replaced with: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `sub_question_count` | 4 = tight; 8 = wide. More sub-questions improve discrimination but extend time |
| `cognitive_level_progression` | Sets the ladder; final sub-question should be at the apex (evaluation / justify trade-off) |
| `time_minutes` | Adjusts disclosure pacing; rule of thumb 5 min per sub-question |
| `include_calculation_step` | Requires explicit math at one sub-question (e.g., maintenance fluid, anion gap) |
| `include_communication_step` | Requires writing a short script for a clinical conversation (capped at ≤ 25% of total marks) |
| `cross_link_to_OSCE` | Marks as compatible with OSCE knowledge-station deployment |

## Verification Checklist

- [ ] Disclosure sequence is irreversible; no-backtrack rule stated on every page.
- [ ] Each sub-question has a bounded verb prompt.
- [ ] Mark allocation per sub-question sums to `mark_total`.
- [ ] Cognitive level rises across sub-questions (or ladder is explicit and intentional).
- [ ] Each sub-question has full / partial / no-credit exemplars.
- [ ] Cluing + leak audit table populated; no fails.
- [ ] Source-fidelity audit populated.
- [ ] Inter-rater target ≥ 0.8 stated.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `exam_style = course-final`, `learner_level = MS3`, `content_domain = "Pediatric DKA progression"`, `sub_question_count = 5`, `mark_total = 30`, `time_minutes = 30`, `cognitive_level_progression = "recall → application → analysis → evaluation → evaluation"`.

**Output (abbreviated):**

```
MEQ — Pediatric DKA progression — course-final — Time: 30 min — Marks: 30

>>> PAGE 1 — STEM + Q1
STEM: A 7-year-old (22 kg) is brought to the ED with 2 days of polyuria, vomiting, and lethargy. HR 138, BP 92/58, RR 32, glucose 512 mg/dL. POC VBG: pH 7.12, HCO3 8, anion gap 22.
Q1 (4 marks): State the diagnosis and severity classification (ISPAD). JUSTIFY using TWO findings.
"Turn the page. Do not revise above."

>>> PAGE 2 — DISCLOSURE 1 + Q2
DISCLOSURE: K 3.4 (3.5–5.0); Na 132; corrected Na 138; Cl 100; β-OHB 6.2.
Q2 (8 marks): Calculate the maintenance + replacement fluid rate for the first hour and JUSTIFY each component (rate, type of fluid, K supplementation). Show your math.
"Turn the page. Do not revise above."

>>> PAGE 3 — DISCLOSURE 2 + Q3
DISCLOSURE: 1 h later, you have started 0.9% NaCl with 40 mEq/L KCl at 80 mL/h. Insulin infusion at 0.1 U/kg/h has begun. The child is now drowsy (was alert), HR 130, BP 96/60. Repeat Na 130 (was 132).
Q3 (6 marks): State your TWO top concerns and ONE diagnostic + ONE therapeutic step for each. JUSTIFY in ONE sentence per item.
"Turn the page. Do not revise above."

>>> PAGE 4 — DISCLOSURE 3 + Q4
DISCLOSURE: Bedside neuro: pupils unequal (R > L), responds to voice but slow. POC glucose 280.
Q4 (6 marks): What is the diagnosis? What is your immediate management plan? List THREE specific interventions in order.
"Turn the page. Do not revise above."

>>> PAGE 5 — DISCLOSURE 4 + Q5
DISCLOSURE: After your interventions, child is now alert and oriented. Family asks why this happened.
Q5 (6 marks): Write a 4–6 sentence explanation to the family, in plain language, addressing what happened, why it can happen during DKA treatment, and what monitoring will continue.

>>> MARKING SCHEME (excerpt)

Q4 (6 marks)
| Element | Marks | Acceptable variants |
|---|---|---|
| Diagnose cerebral edema | 2 | "DKA cerebral edema," "cerebral oedema" |
| Hypertonic therapy: 3% NaCl 2.5–5 mL/kg OR mannitol 0.5–1 g/kg | 2 | named with weight-based dose |
| Reduce fluid rate by 1/3 to 1/2 | 1 | "slow IVF" alone = 0.5 marks |
| Elevate head, maintain ETCO2 35–40 if intubated | 1 | one of these |

Full-credit exemplar: "Cerebral edema. (1) 3% NaCl 5 mL/kg = 110 mL IV bolus over 15 min. (2) Reduce IVF rate by half. (3) Head of bed 30°, neurosurg consult, plan for CT once stable."
Partial (3/6): identifies edema and gives hypertonic but no rate reduction or HOB; misses dosing math.
No-credit: gives bicarbonate or accelerates insulin — addresses wrong physiology.

>>> CLUING + LEAK AUDIT
All rows: pass.

>>> BLUEPRINT TAGS
| Field | Value |
|---|---|
| Exam style | course-final |
| Content area | Pediatrics — DKA |
| Cognitive progression | recall → application → analysis → evaluation → evaluation (communication) |
| Mark total | 30 |
| Time | 30 min |
| Inter-rater target | κ ≥ 0.8 |
| Target misconceptions | "rapid fluid resuscitation safe in pediatric DKA"; "bicarb fixes acidosis"; "edema is rare, can be missed" |

>>> SOURCE-FIDELITY AUDIT
| Claim | Source | Status |
|---|---|---|
| ISPAD 2022 DKA severity | ISPAD 2022 | verified |
| 3% NaCl 2.5–5 mL/kg for DKA cerebral edema | PALS 2023 + ISPAD 2022 | verified |
| Corrected Na formula | standard 1.6 mEq Na rise per 100 mg/dL glucose above 100 | verified |

>>> REJECTED
Considered: a Q5 asking examinee to "discuss the pathophysiology of cerebral edema" — too broad, unbounded, redundant with Q4.
Rejected: unscorable and off-pattern.
Replaced with: communication task with bounded length and named audience.
```
