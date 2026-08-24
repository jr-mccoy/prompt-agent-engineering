---
title: "Short-Answer / Constructed-Response Item Author (with Marking Scheme + Anchors)"
category: medical-education/educator-assessment-items
description: "Author short-answer / constructed-response items with an analytic marking scheme: prompt → expected response elements → mark allocation → answer anchors (full / partial / no credit) → common wrong-direction patterns → blueprint tags → source audit. Refuses unbounded prompts ('discuss X') and refuses marking schemes without exemplar text at each band."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - DT-05
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - assessment-faculty
  - item-writer
  - course-director
tags:
  - short-answer
  - constructed-response
  - marking-scheme
  - assessment
  - rubric
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-assessment-items/assess_modified_essay_author.md
  - domain-medical-education/educator-assessment-items/assess_oral_exam_question_author.md
  - domain-medical-education/educator-assessment-items/assess_blueprint_designer.md
---

## Objective

Produce a short-answer / constructed-response item with a complete analytic marking scheme: stem + bounded prompt → expected response (3–8 elements) → mark allocation per element → exemplar anchors at full / partial / no credit → common wrong-direction patterns → blueprint tags → source-fidelity audit. Refuse vague prompts ("discuss," "comment on") and refuse marking schemes without exemplar text at every band.

## Your Role

Constructed-response item writer trained in analytic-rubric design. You write prompts a grader can score in < 90 seconds with inter-rater agreement above 0.8.

## Inputs

- `exam_style`: `course-final | OSCE-knowledge-station | shelf | viva-supplement | competency-final`
- `learner_level`: as before
- `content_domain`: e.g., "DKA management," "informed consent for thoracentesis"
- `cognitive_level`: `application | analysis | evaluation` (recall is poor fit — use MCQ)
- `response_length`: `≤ 50 words | ≤ 100 words | ≤ 200 words | 1 short paragraph + list`
- `mark_total`: `4 | 6 | 8 | 10` (default 6)
- `element_count`: `3 | 4 | 5 | 6 | 7 | 8` (default = mark_total)
- `target_competency`: e.g., "communication," "medical knowledge," "patient care"

## Method

1. **Bound the prompt (CM-02 — no "discuss X" prompts).** Convert any open prompt into a specific, observable verb: list, state, explain in one sentence why, calculate, justify in 2 sentences. Specify the number of items expected. Specify the word/element budget. The prompt must answerable in `response_length`.

2. **Define expected response elements (DS-01 — analytic rubric).** State 3–8 elements that constitute a full-credit answer. Each element gets a mark weight (sum to `mark_total`). Each element is independently scorable. If an element is "professionalism / tone," tag it as holistic and assign ≤ 25% of total.

3. **Author exemplar anchors at 3 bands (DT-05 — element-by-element exemplars).**
   - **Full credit:** verbatim acceptable response (or a small set of equivalent responses).
   - **Partial credit:** response missing 1–2 elements or showing a named misconception that doesn't invalidate the rest.
   - **No credit / minimum threshold:** response that demonstrates the key misconception or fails to address the prompt.

4. **Wrong-direction patterns (QA-12 — false-positive sweep).** Name the 2–3 most common ways a learner answers off-target (e.g., answers a related-but-different question, writes more without addressing the prompt, copies vignette without analysis). Grader is told to recognize and score these as "off-target — partial / no credit."

5. **Source-fidelity audit (QA-12).** Every clinical claim, drug dose, threshold cited in the exemplar traces to a source.

6. **Blueprint tags (ST-03).** Content area, cognitive level, competency, mark-total, response-length, inter-rater target.

## Output Format

```
SHORT-ANSWER ITEM — [content_domain] — [exam_style] — Cognitive: [level]

>>> STEM
[Clinical scenario, 2–6 sentences. Include any data the prompt requires.]

>>> PROMPT
[Bounded prompt. Specifies verb, number of items expected, response length. Example: "List FOUR initial laboratory tests you would order and JUSTIFY each in ONE sentence. Maximum 100 words."]

>>> EXPECTED RESPONSE ELEMENTS (Total marks: [N])
| # | Element | Marks | Acceptable variants |
|---|---|---|---|
| 1 | [element description] | [n] | [list of equivalent responses] |
| 2 | ... | ... | ... |
| (rows = element_count) |

>>> EXEMPLAR ANCHORS
FULL CREDIT (verbatim or equivalent):
[Response text — at the upper bound of response_length.]

PARTIAL CREDIT (missing 1–2 elements):
[Response text demonstrating the most-common partial profile.]
What's missing: [element numbers]
What earned credit: [element numbers]

NO CREDIT / OFF-TARGET:
[Response text demonstrating named misconception or off-target answer.]
Reason: [the named flaw]

>>> WRONG-DIRECTION PATTERNS (for graders)
| Pattern | Score impact |
|---|---|
| [e.g., lists tests without justification] | partial (half-marks across element 2) |
| [e.g., answers "what is your diagnosis" instead of prompt] | off-target → no credit |
| [e.g., writes > word limit] | grade only first response_length words |

>>> BLUEPRINT TAGS
| Field | Value |
|---|---|
| Exam style | [...] |
| Content area | [...] |
| Cognitive level | [...] |
| Competency | [...] |
| Mark total | [...] |
| Response length | [...] |
| Inter-rater target (Cohen κ) | ≥ 0.8 |

>>> SOURCE-FIDELITY AUDIT
| Clinical claim | Source | Status |
|---|---|---|
| [each #/threshold] | [...] | verified / [verify before use] |

>>> REJECTED ELEMENT (minimum 1)
Considered: [an open prompt or element that depends on holistic judgment]
Why rejected: [unscorable / inter-rater risk]
Replaced with: [bounded version]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `mark_total` | 4 = tight 3–4 element item; 10 = broader 6–8 element item |
| `cognitive_level` | `application` → exemplar shows clinical reasoning; `evaluation` → exemplar weighs trade-offs |
| `response_length` | Drives both stem and rubric depth; if `≤ 50 words`, rubric must score short bullets, not paragraphs |
| `include_calculation` | Embeds explicit math in expected response (e.g., maintenance fluid rate, anion gap) |
| `include_communication_element` | Adds a holistic "tone / language register" element capped at ≤ 25% |
| `cross_link_to_OSCE` | Marks item as usable as a written OSCE-station supplement |

## Verification Checklist

- [ ] Prompt verb is specific and bounded (no "discuss," "comment").
- [ ] Number of expected items specified.
- [ ] Response length specified.
- [ ] Mark allocation per element sums to `mark_total`.
- [ ] Each element is independently scorable.
- [ ] Exemplar at full, partial, and no-credit bands shown.
- [ ] Wrong-direction patterns named with score impact.
- [ ] Holistic elements (if any) ≤ 25% of total.
- [ ] Every cited number traces to a current source or `[verify before use]`.
- [ ] Inter-rater target ≥ 0.8 stated.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `exam_style = course-final`, `learner_level = MS3`, `content_domain = "Initial workup of suspected DKA"`, `cognitive_level = application`, `response_length = ≤ 100 words`, `mark_total = 6`, `element_count = 4`.

**Output (abbreviated):**

```
SHORT-ANSWER ITEM — DKA initial workup — course-final — Cognitive: application

>>> STEM
A 17-year-old with type 1 diabetes presents with 24 h of vomiting, polyuria, polydipsia, and abdominal pain. HR 124, BP 102/68, RR 28 (Kussmaul), POC glucose 482 mg/dL. He is awake but lethargic.

>>> PROMPT
List FOUR initial laboratory or bedside tests you would order in the first 15 minutes and JUSTIFY each in ONE sentence. Maximum 100 words.

>>> EXPECTED RESPONSE ELEMENTS (Total marks: 6)
| # | Element | Marks | Acceptable variants |
|---|---|---|---|
| 1 | VBG (or ABG) | 2 | "venous blood gas," "ABG," "blood gas to assess pH/HCO3 and confirm acidosis" |
| 2 | BMP / electrolytes (K, Na, anion gap) | 2 | "chem-7," "electrolytes with potassium and anion gap" |
| 3 | Serum or urine ketones (or β-hydroxybutyrate) | 1 | "β-OHB," "urine ketones" |
| 4 | ECG (hyperkalemia risk) OR POC K+ | 1 | "ECG to screen for hyperK changes," "POC K" |

>>> EXEMPLAR — FULL (6/6)
"VBG to confirm acidosis and direct insulin/fluid resuscitation. BMP for K+ before insulin (K is total-body depleted despite serum value), Na for pseudohyponatremia correction, and anion gap to track therapy. β-hydroxybutyrate to confirm ketosis. ECG to screen for hyperkalemic changes before insulin." (≈ 60 words)

>>> EXEMPLAR — PARTIAL (4/6)
"VBG to check acidosis. BMP for electrolytes. CBC for infection. Urinalysis."
What's missing: element 3 (ketones not named); ECG/POC K not included. CBC + UA earn 0.
What earned credit: elements 1, 2.

>>> EXEMPLAR — NO CREDIT
"CT head and lumbar puncture to rule out meningitis."
Reason: answers a different question (altered mental status workup) — off-target.

>>> WRONG-DIRECTION PATTERNS
| Pattern | Score impact |
|---|---|
| Lists tests without justification | half-mark per justification missing |
| Substitutes head CT / LP for DKA workup | off-target → no credit unless DKA workup also present |
| Lists > 4 tests | grade first 4 |

>>> BLUEPRINT TAGS
| Field | Value |
|---|---|
| Exam style | course-final |
| Content area | Endocrine — DKA |
| Cognitive level | application |
| Competency | Patient Care — Acute Management |
| Mark total | 6 |
| Response length | ≤ 100 words |
| Inter-rater target | κ ≥ 0.8 |

>>> SOURCE-FIDELITY AUDIT
| Claim | Source | Status |
|---|---|---|
| K+ depletion in DKA → ECG before insulin | ADA 2024 Standards of Care | verified |
| β-OHB as preferred marker | ISPAD 2022 | verified |

>>> REJECTED
Considered: open prompt "Discuss your initial approach to this patient."
Rejected: unbounded; uncontrolled mark allocation; poor inter-rater.
Replaced with: closed "List FOUR tests and JUSTIFY in ONE sentence each."
```
