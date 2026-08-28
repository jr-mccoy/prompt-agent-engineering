---
title: "Medical Clinical Reasoning Drill"
category: education-teaching/learner-study-skills
description: "Case-based clinical reasoning practice for medical students: generates chief complaint vignettes at increasing complexity, guides through the diagnostic reasoning chain (chief complaint → history → exam findings → DDx → workup → diagnosis), and includes self-scoring against a reference reasoning chain."
techniques:
  - ST-01
  - ST-02
  - ED-02
  - ED-03
  - QA-01
difficulty: advanced
tags:
  - medical-education
  - clinical-reasoning
  - differential-diagnosis
  - USMLE
  - shelf-exams
  - case-based-learning
  - diagnostics
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner-study-skills/learnstudy_med_pharmacology_recall.md
  - domain-education-teaching/learner-study-skills/learnstudy_retrieval_drill_designer.md
  - domain-education-teaching/learner-study-skills/learnstudy_practice_test_generator.md
---

## Objective

Generate clinical reasoning practice cases for medical students and clinicians in training — not just knowledge recall, but the diagnostic reasoning process: generating a differential, ordering appropriate studies, interpreting results, and arriving at a diagnosis. Each case is self-contained and includes a reference reasoning chain for self-scoring.

## When to Use

- Preparing for USMLE Step 1, Step 2 CK, Step 3, or clerkship shelf exams
- During clinical rotations to practice applying knowledge to real-scenario reasoning
- When a learner can recall facts about diseases but cannot apply them to vignette-style questions
- When diagnostic reasoning (generating DDx, ordering the right workup) is weaker than factual recall

**Do not use** as a substitute for clinical supervision with real patients — this is a knowledge and reasoning practice tool for educational settings. For pharmacology recall specifically, use `learnstudy_med_pharmacology_recall.md`.

## Instructions

1. **Collect inputs.**
   - Ask: "Which organ system or clinical domain? (e.g., cardiology, neurology, nephrology, general internal medicine)"
   - Ask: "What exam are you preparing for? (USMLE Step 1/2/3, shelf, COMLEX, other)"
   - Ask: "What difficulty level? (1 = core presentation of common disease, 2 = atypical presentation or common disease with complication, 3 = rare disease or complex differential)"
   - Ask: "How many cases for this session?"
   - Ask: "Focus on any specific clinical reasoning weakness? (e.g., 'I miss the diagnosis when the presentation is atypical' or 'I generate a DDx but don't know how to narrow it')"

2. **Structure each case as a sequential reveal.**
   Each case unfolds in stages to simulate clinical reasoning:

   **Stage 1 — Chief complaint:**
   "[Age]-year-old [sex], presenting with [symptom] for [duration]."
   Learner task: Generate initial DDx (3–5 diagnoses) before any history.

   **Stage 2 — History and review of systems:**
   Provide key history details. Include pertinent positives AND pertinent negatives.
   Learner task: Narrow DDx. Which diagnoses moved up? Which were eliminated? Why?

   **Stage 3 — Physical exam:**
   Provide relevant exam findings (vital signs + focused exam for the system in question).
   Learner task: Update DDx. What does the exam add or eliminate?

   **Stage 4 — Workup decision:**
   "What is your next step in management? What diagnostic test(s) do you order first, and why?"
   Do not yet reveal results. The learner must justify the workup rationale.

   **Stage 5 — Lab/imaging results:**
   Reveal the key test result(s).
   Learner task: State the diagnosis. Explain why this result confirms (or changes) the working diagnosis.

   **Stage 6 — Management:**
   "What is your immediate management for this diagnosis?"
   Learner task: State the treatment, any monitoring, and any contraindications to watch for.

3. **Provide a reference reasoning chain.**
   After the learner has completed all stages, reveal:
   - The correct diagnosis
   - The expected initial DDx at Stage 1 (what a competent clinician would have listed)
   - The key pivot point: what clinical feature should have most changed the DDx between stages
   - Common diagnostic error for this presentation: the diagnosis most often missed or incorrectly made
   - The "classic teaching phrase" if one exists (e.g., "saddle nose + septal perforation → think Wegener's")

4. **Include a self-scoring rubric.**
   After the case is complete, ask the learner to score their reasoning:

   | Reasoning step | 2 pts: Complete | 1 pt: Partial | 0 pts: Missed |
   |---|---|---|---|
   | Initial DDx included correct diagnosis | Yes | Yes but too broad or missed key alternative | No |
   | Key pivot point identified | Yes | Moved in right direction | No change in DDx after new info |
   | Workup selection appropriate | Correct first test | Close but not optimal | Wrong test ordered |
   | Diagnosis stated correctly | Yes | Partially right | Incorrect |
   | Management correct | Yes | Partially correct | Incorrect |

   Score: ___/10 per case.

5. **For difficulty Level 2–3 cases, include a "teaching point" trap.**
   Embed a classic exam distractor: a piece of information that sounds important but is not (meant to test information weighting), or a result that initially looks like a different diagnosis (meant to test persistence of reasoning past an unexpected finding).

## Output Format

```
# Clinical Reasoning Drill: [System/Domain]
Exam: [target exam] | Difficulty: [1/2/3] | Cases: N

---

## Case [#]: [System — Difficulty]

**Stage 1 — Chief Complaint:**
[Age]-year-old [sex], presenting with [symptom] for [duration].

*Your DDx at this stage (list 3–5 before reading on):*
1. ___
2. ___
3. ___
4. ___
5. ___

---

**Stage 2 — History:**
[History details — pertinent positives and negatives]

*Update your DDx: Which moved up? Which were eliminated? Why?*

---

**Stage 3 — Physical Exam:**
[Vital signs + exam findings]

*Update your DDx again.*

---

**Stage 4 — Workup:**
*What is your next step? What tests do you order first, and why?*
Order: ___
Rationale: ___

---

**Stage 5 — Results:**
[Key lab/imaging results revealed]

*State your diagnosis and why this confirms it:*
Diagnosis: ___
Reasoning: ___

---

**Stage 6 — Management:**
*Immediate management for this diagnosis:*
Treatment: ___
Monitoring: ___

---

## Reference Reasoning Chain (reveal after all stages)

**Correct diagnosis:** [Diagnosis]
**Expected Stage 1 DDx:** [List what a competent clinician would generate]
**Key pivot point:** [The clinical feature that should shift the DDx most]
**Common diagnostic error:** [What learners typically miss or misdiagnose]
**Classic teaching phrase:** [If one exists]

---

## Self-Scoring Rubric

| Step | 2 pts | 1 pt | 0 pts | My score |
|---|---|---|---|---|
| Initial DDx | | | | |
| Key pivot identified | | | | |
| Workup appropriate | | | | |
| Diagnosis correct | | | | |
| Management correct | | | | |
**Total: ___/10**
```

## Example Output

---

**Input:** Internal Medicine — USMLE Step 2 CK — Difficulty 2 — 1 case — Weakness: missing diagnosis when presentation is atypical

---

# Clinical Reasoning Drill: Internal Medicine
Exam: USMLE Step 2 CK | Difficulty: 2 | Cases: 1

---

## Case 1: Cardiology — Difficulty 2 (Atypical Presentation)

---

**Stage 1 — Chief Complaint:**
67-year-old woman presenting to the ED with nausea, vomiting, and epigastric pain for 2 hours.

*Before reading further — write your initial DDx (3–5 diagnoses):*
1. ___
2. ___
3. ___
4. ___
5. ___

---

*(Pause here. Generate DDx before advancing.)*

---

**Stage 2 — History:**

- Pain began suddenly while climbing stairs; she initially thought it was indigestion
- No fevers, chills, or diarrhea
- No recent NSAID use, no alcohol use
- Past medical history: Type 2 diabetes (on metformin), hypertension, hyperlipidemia; smoker (1 PPD × 35 years)
- Family history: Father had "a heart attack" at age 60
- Medications: Metformin, amlodipine, atorvastatin
- **Pertinent negatives:** No chest pain, no dyspnea, no arm or jaw pain reported

*Update your DDx: Which diagnoses moved up? Which were eliminated?*

---

**Stage 3 — Physical Exam:**

- Vital signs: BP 158/96, HR 98, RR 18, O2 sat 96% on room air, T 37.1°C
- General: Diaphoretic, appears uncomfortable
- Cardiovascular: Regular rate and rhythm, no murmurs; **S4 gallop present**
- Abdomen: Mild epigastric tenderness to palpation; no guarding, no rigidity, no rebound
- Extremities: No edema

*Update your DDx: What does the S4 gallop tell you? What does the normal abdominal exam suggest?*

---

**Stage 4 — Workup:**

*What is your NEXT STEP? What do you order first, and why?*

Your order: ___
Your rationale: ___

---

*(Pause. Commit to a test before advancing.)*

---

**Stage 5 — Results:**

ECG: ST-segment elevation in leads II, III, and aVF; reciprocal ST depression in leads I and aVL.
Troponin I (initial): 0.18 ng/mL (normal < 0.04 ng/mL). ↑

*State your diagnosis and explain why this result confirms it:*
Diagnosis: ___
Reasoning: ___

---

**Stage 6 — Management:**

*Immediate management for this diagnosis (this is time-sensitive — list in order):*
Treatment: ___
Monitoring: ___
Contraindications to check: ___

---

## Reference Reasoning Chain

*(Reveal only after completing all stages)*

**Correct diagnosis:** Inferior STEMI (ST-elevation myocardial infarction) with atypical presentation — nausea/epigastric pain as anginal equivalent

**Expected Stage 1 DDx (competent clinician):**
1. Peptic ulcer disease / gastritis (most common first impression given epigastric symptoms)
2. Acute coronary syndrome / NSTEMI (should be on DDx given age, DM, HTN, smoking, family history)
3. Acute pancreatitis (epigastric pain, nausea/vomiting pattern)
4. Cholecystitis (epigastric/RUQ pain with nausea)
5. GERD exacerbation

*Note: ACS must be on this DDx in any patient >50 with multiple cardiovascular risk factors — even with purely GI symptoms.*

**Key pivot point:**
The diaphoresis + S4 gallop + cardiovascular risk factors (DM, HTN, hyperlipidemia, smoking, family history of MI) should dramatically elevate ACS on the DDx by Stage 3. Diaphoresis in a setting of nausea + cardiac risk is a cardiovascular alarm sign — not just a GI symptom. The S4 gallop indicates decreased left ventricular compliance consistent with acute ischemia.

**Stage 4 — Correct next step:**
12-lead ECG immediately (first test in any patient with possible ACS — before troponins, before GI workup). Any diagnostic delay for a STEMI increases mortality.

**Common diagnostic error:**
Missing ACS when epigastric pain is the chief complaint — especially in women and diabetic patients, who more commonly present with "atypical" symptoms (nausea, epigastric pain, fatigue) rather than classic chest pain. Diabetic neuropathy blunts visceral pain sensation.

**Classic teaching phrase:**
"Women and diabetics are more likely to have silent or atypical MI. When nausea + diaphoresis + cardiac risk factors are present, get an ECG before calling GI."

**Stage 6 — Immediate management:**
1. Activate cath lab (door-to-balloon time target: ≤90 min)
2. Aspirin 325 mg chewed
3. P2Y12 inhibitor (ticagrelor or clopidogrel)
4. Anticoagulation (heparin or bivalirudin)
5. Supplemental oxygen only if O2 sat < 90%
6. Nitroglycerin — **CAUTION:** Inferior STEMI (leads II, III, aVF) raises concern for right ventricular involvement. Give IV fluids first; nitroglycerin can cause severe hypotension in RV infarction (preload-dependent).
7. Do NOT give beta-blockers if HR is elevated or there is concern for heart failure.

---

## Self-Scoring Rubric

| Reasoning Step | 2 pts: Complete | 1 pt: Partial | 0 pts: Missed | My score |
|---|---|---|---|---|
| ACS on initial DDx (Stage 1) | ACS explicitly listed | Listed vague "cardiac" but not ACS | Not listed | /2 |
| Key pivot identified (diaphoresis + S4 + risk factors) | Named all three | Named 1–2 but not all | Did not pivot DDx | /2 |
| ECG as first test | ECG ordered first | Ordered ECG after troponin | Ordered GI workup first | /2 |
| Inferior STEMI diagnosed correctly | Yes | Identified MI but missed inferior/STEMI specifics | Incorrect | /2 |
| Nitroglycerin RV caution noted | Flagged RV concern | Ordered nitro without RV consideration | Not addressed | /2 |

**Total: ___/10**

- 9–10: Excellent clinical reasoning — ready for exam-level vignettes
- 7–8: Sound overall, one weak step — review that step's mechanism
- 5–6: Key pivot or management step missed — targeted re-study needed
- < 5: Foundational gap — review the clinical presentation and management of inferior STEMI before more case drills

---

## False-Positive Prevention

**❌ DON'T** reveal Stage 2 history before the learner has generated a Stage 1 DDx. A DDx generated after seeing the history is not a DDx — it's reverse-engineered pattern matching.

**✅ DO** enforce sequential staging: generate DDx → read next stage → update → continue. Each stage must be completed before the next is read.

**❌ DON'T** include all findings as equally important. Clinical cases include noise — normal findings that aren't relevant and should be deprioritized. Cases that list only relevant findings don't represent real clinical reasoning.

**✅ DO** include at least one pertinent negative and one potentially distracting finding per case. The reasoning skill includes data weighting, not just data accumulation.

**❌ DON'T** make every case a "classic presentation." Atypical presentations are what learners fail on — and are more common in USMLE Step 2 cases specifically.

**✅ DO** include at least 50% non-classic presentations in sessions targeting Step 2 or clinical reasoning (not Step 1 knowledge recall).

**❌ DON'T** score only on the final diagnosis. The process matters — a learner who gets the diagnosis right by guessing (without correct workup reasoning) needs to practice the process, not just the answer.

**✅ DO** score each reasoning step separately, so the feedback identifies exactly where the process broke down.

## Quality Criteria

- [ ] Case unfolds in stages — DDx is generated before history is revealed
- [ ] Stage 2 includes both pertinent positives and pertinent negatives
- [ ] Stage 4 asks for workup rationale (not just the test name)
- [ ] Reference reasoning chain identifies the key pivot point and common diagnostic error
- [ ] Self-scoring rubric scores each reasoning step separately
- [ ] At least one management contraindication or nuance is included (not just the primary treatment)
- [ ] Difficulty 2–3 cases include a teaching point trap or atypical presentation

## Techniques Used

- **ST-01 (Clear Objective Statement):** Objective specifies diagnostic reasoning process (not knowledge recall) as the target — the distinction between knowing facts and applying them clinically
- **ST-02 (Structured Sequential Instructions):** Six-stage case structure (chief complaint → history → exam → workup → results → management) enforces the clinical reasoning sequence
- **ED-02 (Progressive Exercise Generation):** Difficulty levels scale from core presentations (Level 1) to atypical presentations with complications (Level 2–3)
- **ED-03 (Guided Discovery):** Sequential reveal forces the learner to update the DDx at each stage rather than reading the full case and working backward
- **QA-01 (Self-Verification):** Reference reasoning chain + rubric enables self-scoring at the process level, not just the answer level
