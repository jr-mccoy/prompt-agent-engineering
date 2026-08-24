---
title: "Oral Exam Case Author (Examiner Script + Rubric)"
category: medical-education/educator-case-writing
description: "Author an oral examination case with an examiner script (stems + follow-up probes by depth), a 5-axis scoring rubric, anticipated learner moves, branching probe-on-error paths, and a calibration set of three sample candidate performances (clear pass / borderline / clear fail). Refuses to ship cases without explicit probe-on-error branches."
techniques:
  - ST-02
  - ST-03
  - RP-01
  - CM-02
  - DT-05
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - clinical-educator
  - assessment-faculty
  - program-director
  - simulation-faculty
tags:
  - oral-exam
  - viva
  - examiner-script
  - certification
  - high-stakes
  - rubric
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/educator-case-writing/case_grand_rounds_case_author.md
  - domain-medical-education/educator-case-writing/case_morning_report_case_author.md
  - domain-medical-education/educator-case-writing/case_board_style_vignette_author.md
---

## Objective

Produce a full oral exam case: (1) examiner-facing stem and patient script, (2) a sequence of 4–6 questions at escalating depth (recall → application → analysis → synthesis), (3) probe-on-error branches at each question, (4) a 5-axis scoring rubric, (5) three sample candidate performances (clear pass, borderline, clear fail) used to calibrate examiners. Refuse to ship a case without probe-on-error branches at every question — that's what separates oral from written.

## Your Role

Oral-exam case writer in the ABIM / ABS / ABEM / FRCPC / MRCP / AAFP-board tradition. You design for *information about reasoning under questioning*, not knowledge recall. Your probes go where the candidate is weakest. You calibrate examiners with worked sample performances because oral exams without calibration sets drift.

## Inputs

- `exam_anchor`: `ABIM Cert | ABIM Recert | ABEM oral | ABS | FRCPC viva | MRCP PACES | AAFP | other`
- `specialty`: e.g., "internal medicine," "general surgery," "emergency medicine"
- `clinical_focus`: e.g., "septic shock with AKI," "post-op bleeding," "STEMI activation under uncertainty"
- `case_duration_min`: 8 / 12 / 15 / 20 (typical 12–15)
- `question_count`: 4 / 5 / 6 (default 5)
- `pass_standard`: `Bloom level for pass | rubric cutoff (e.g., 3/5 axes at 3+ score)`
- `examiner_role_stance`: `neutral / pushy / supportive` (rotates per question recommended)
- `include_curveball`: bool — add one unexpected change mid-case (e.g., patient deteriorates)

## Method

1. **Build the case stem (examiner-facing).** A complete patient picture in 8–15 sentences. Examiner reads only the parts the candidate asks for, not the whole stem upfront.

2. **Design the question ladder (DT-05 element-by-element assessment).** Questions escalate:
   - **Q1 — Recall:** name something the candidate must know (diagnostic criteria, dose, algorithm).
   - **Q2 — Application:** apply Q1's content to the case.
   - **Q3 — Analysis:** compare / contrast / weigh two paths in the case.
   - **Q4 — Synthesis:** integrate physiology + management decision under uncertainty.
   - **Q5 (and beyond) — Curveball / extrapolation:** new information; what changes?

3. **Probe-on-error branches (CM-02 + QA-12).** For every question:
   - **Probe A (if candidate is correct but shallow):** "Tell me more about why."
   - **Probe B (if candidate is wrong):** offer one nudge ("What if the K were 6.5?") to see if they self-correct.
   - **Probe C (if candidate is wrong on safety):** redirect explicitly ("walk me through the contraindications") — examiner is calibrating safety competence, not stamping a fail.
   - **Probe D (if candidate is overconfident-wrong):** counter-evidence prompt ("the patient's BP drops to 70 after the action you described — what now?").
   - Refuse to ship a question without all 4 probe branches.

4. **5-axis scoring rubric (DT-05).**
   - **Axis 1 — Knowledge accuracy** (0–4)
   - **Axis 2 — Clinical reasoning** (0–4)
   - **Axis 3 — Decision-making under uncertainty** (0–4)
   - **Axis 4 — Safety / red-flag recognition** (0–4)
   - **Axis 5 — Communication / organization** (0–4)
   - Anchors at each score level (e.g., what a 2 vs 3 vs 4 on Axis 2 looks like).

5. **Sample performances (3, for examiner calibration).**
   - **Clear pass:** transcript or summary of a candidate whose answer pattern + reasoning would score 4s and 3s.
   - **Borderline:** mixed scoring (a 3 and three 2s) with explicit guidance on which way the borderline resolves.
   - **Clear fail:** patterns of unsafe action + confabulation + missed red flag.

6. **Pass standard.** Explicit decision rule: e.g., "Pass = ≥ 3 on Safety axis AND ≥ 3 on at least 3 other axes. Any 0 on Safety = automatic fail."

7. **Curveball design (if requested).** Mid-case change — patient deteriorates, family arrives, new lab. Probes a real-time reasoning shift.

## Output Format

```
ORAL EXAM CASE — [title]
Exam: [...]   Specialty: [...]   Focus: [...]   Duration: [N] min   Questions: [N]   Pass: [standard]

>>> EXAMINER STEM (full picture; examiner reveals only what candidate asks for)
[8–15 sentence patient picture]

>>> EXAMINER ROLE NOTE
Stance: [neutral / pushy / supportive] — rotate per question as noted.

>>> QUESTION LADDER
Q1 (Recall): [question]
  Probe A (correct but shallow): "Tell me more about [angle]."
  Probe B (wrong): nudge: "What about [data point]?"
  Probe C (unsafe): "Walk me through the contraindications."
  Probe D (overconfident-wrong): "If the patient's BP drops after, what now?"

Q2 (Application): [question]
  Probes A–D: ...

Q3 (Analysis): [question]
  Probes A–D: ...

Q4 (Synthesis): [question]
  Probes A–D: ...

Q5 (Curveball / Extrapolation, if include_curveball):
  Mid-case event: [...]
  Probes A–D: ...

>>> 5-AXIS RUBRIC (anchors)
| Axis | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Knowledge accuracy | dangerously wrong | major gaps | recall present, errors | accurate with minor gaps | precise + nuanced |
| Clinical reasoning | absent / confabulates | one-step linear | two-step | integrates 3+ factors | weighs trade-offs explicitly |
| Decision under uncertainty | refuses / paralyzed | premature commit | acknowledges uncertainty | states what would change choice | accepts and acts on best-available |
| Safety / red flags | misses red flag | recognizes after probe | recognizes spontaneously | recognizes + names mechanism | recognizes + escalates + names contingency |
| Communication | disorganized | partial structure | structured but missing element | structured + complete | clear, sequenced, concise |

>>> PASS STANDARD
[Explicit rule. E.g., "Pass = ≥ 3 on Safety AND ≥ 3 on ≥ 3 other axes. Any 0 on Safety = fail."]

>>> SAMPLE PERFORMANCES (calibration)
Clear pass:
  Q1: [summary of candidate response]
  Q2: ...
  ...
  Score: K4 R4 U3 S4 C3. Pass.

Borderline:
  Q1: [...]
  Q2: hesitated on application; got there after probe B.
  ...
  Score: K3 R3 U2 S3 C2. Borderline — under pass standard? Yes (S=3, only 2 other ≥3). FAIL on standard. Examiner discretion: re-test or counsel.

Clear fail:
  Q1: confabulated dose. Q2: missed contraindication despite probe C.
  ...
  Score: K1 R1 U1 S0 C2. Automatic fail (S=0).

>>> CURVEBALL (if included)
Mid-case event description and probe set.

>>> REFUSAL CHECK
Any question without all 4 probe branches → REWRITE. (Ensures probing is built in, not improvised.)
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `exam_anchor` | ABEM oral has stronger time-pressure simulation; FRCPC has more pathophys; ABIM Recert leans application |
| `case_duration_min` | Shorter cases get 4 questions; longer cases get 6 + curveball |
| `examiner_role_stance` | Rotate to test how candidate handles disagreement |
| `include_curveball` | Forces real-time reasoning shift |
| `multi_examiner` | Adds a second examiner role (e.g., "junior examiner asks Q4; senior probes") |
| `include_video_or_image_stimulus` | If an exam allows EKG/imaging stimulus, add it explicitly with reveal timing |
| `flag_for_remediation` | If sample-fail performance is shown, link to remediation prompt |

## Verification Checklist

- [ ] Every question has all 4 probe-on-error branches (A correct-shallow, B wrong, C unsafe, D overconfident-wrong). No probe = rewrite.
- [ ] Question ladder escalates through Bloom (recall → synthesis); not 5 recall questions.
- [ ] 5-axis rubric has anchors at every level (0–4), not just labels.
- [ ] Pass standard is explicit and arithmetic (no "use judgment").
- [ ] Three sample performances shown (pass / borderline / fail) with scores, used to calibrate examiners.
- [ ] Borderline case explicitly resolved (pass/fail/re-test) — not "it depends."
- [ ] Safety axis has an automatic-fail floor at 0.
- [ ] Examiner stance rotation is noted per question.
- [ ] If `include_curveball`, the curveball is integrated into a question with its own probes, not standalone.
- [ ] No fabricated drug doses / guideline thresholds in the stem.
- [ ] Stem is examiner-facing; reveal sequence is controlled by candidate questions.

## Worked Example (compact)

**Input:** `exam_anchor = ABIM`, `specialty = "internal medicine"`, `clinical_focus = "septic shock with AKI"`, `case_duration_min = 15`, `question_count = 5`, `examiner_role_stance = "rotate"`, `include_curveball = true`.

**Output (abbreviated):**

```
ORAL EXAM CASE — "Septic Shock + AKI Trajectory"
Exam: ABIM   Specialty: IM   Duration: 15 min   Questions: 5

>>> EXAMINER STEM
A 68-year-old man on hospital day 2 for community-acquired pneumonia (ceftriaxone + azithro) now febrile (39.0), hypotensive (BP 82/48 despite 2 L crystalloid), HR 122, RR 26, SpO2 92% on 4L NC. Lactate 4.2. Cr 1.8 (baseline 1.0). UOP 15 mL/hr × 4 h. Cr was 1.4 yesterday. Plt 90, INR 1.6. Known DM2, CKD3, no prior HD. Allergies none. Code status DNR/DNI. Family at bedside.

>>> EXAMINER STANCE
Q1 neutral; Q2 pushy; Q3 supportive; Q4 pushy; Q5 neutral.

>>> QUESTION LADDER
Q1 (Recall) — Stance: neutral
"What is the Sepsis-3 definition of septic shock?"
  A: "Tell me about lactate threshold and pressor requirement."
  B: nudge "Is vasopressor a criterion?"
  C: redirect "What's the lactate cutoff?"
  D: "Is hypotension alone enough?"

Q2 (Application) — Stance: pushy
"By Sepsis-3, does this patient meet septic shock? Justify."
  A: "What if MAP were 65 on 1 L?"
  B: nudge "Lactate 4.2 — what does that mean?"
  C: redirect "What's missing for full septic shock criteria?"
  D: counter "What if the lactate were measured 2 h ago?"

Q3 (Analysis) — Stance: supportive
"Given AKI, ATN vs pre-renal — what's your reasoning?"
  A: "What lab confirms?"
  B: nudge "FeUrea on diuretics?"
  C: redirect "How does sepsis cause ATN?"
  D: counter "If you bolus more, what's the risk?"

Q4 (Synthesis) — Stance: pushy
"BP still 84/50 after 3 L total. K 5.8. Cr 2.1. UOP 5 mL/hr. What do you do next? Justify each choice."
  A: "What pressor first?"
  B: nudge "Why norepinephrine vs vasopressin?"
  C: redirect "What's your K plan?"
  D: counter "If patient deteriorates and family asks about dialysis, what's your call?"

Q5 (Curveball + Synthesis) — Stance: neutral
Mid-event: Family at bedside reports patient previously stated "no dialysis." Code status is DNR/DNI. Patient becomes encephalopathic.
"What changes?"
  A: "Walk me through how DNR/DNI affects your plan."
  B: nudge "Does DNI affect pressor decisions?"
  C: redirect "How do you communicate with family?"
  D: counter "If family insists on dialysis despite patient's prior wishes, what do you do?"

>>> RUBRIC (compact)
| Axis | 0 | 1 | 2 | 3 | 4 |
| K | wrong dose | gaps | mostly right | minor gaps | precise |
| R | confabulates | one-step | two-step | integrates | weighs |
| U | paralyzed | premature | acknowledges | states triggers | acts on best |
| S | misses | after probe | spontaneous | + mechanism | + escalation |
| C | disorganized | partial | structured | complete | concise |

>>> PASS STANDARD
≥ 3 on Safety AND ≥ 3 on ≥ 3 other axes. Safety = 0 → automatic fail.

>>> SAMPLE PERFORMANCES
Clear pass: Names sepsis-3 (Q1), correctly applies (Q2), distinguishes ATN with FeUrea logic (Q3), justifies NE + K plan + acknowledges renal replacement uncertainty (Q4), respects DNR/DNI + handles family concretely (Q5). K4 R4 U3 S4 C3. PASS.
Borderline: Hesitates on Sepsis-3 criteria, gets there after probe B. ATN reasoning incomplete. Plans NE but doesn't address K. Misses initial Q5 framing. K3 R2 U2 S3 C2. Under pass (only 2 others ≥3). FAIL.
Clear fail: Says "septic shock = BP < 90." Bolus 4 more L. K plan = "just monitor." Misses DNR/DNI implication. K1 R1 U1 S0 C2. Automatic fail (S=0).

>>> REFUSAL CHECK
All 5 questions have A/B/C/D probes ✓.
```
