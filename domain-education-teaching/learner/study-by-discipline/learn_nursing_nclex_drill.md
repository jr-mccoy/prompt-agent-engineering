---
title: "Nursing NCLEX Drill"
category: education-teaching/learner-study-skills
description: "Generates NCLEX-style alternate-format questions: SATA (Select All That Apply), ordered response, priority/delegation questions, and hot-spot descriptions. Includes rationale for correct and incorrect options and test-taking strategy notes for each question type."
techniques:
  - ST-01
  - ST-02
  - ED-02
  - NE-04
  - QA-01
difficulty: intermediate
tags:
  - nursing
  - NCLEX
  - alternate-format
  - priority-nursing
  - delegation
  - SATA
  - test-taking-strategy
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner-study-skills/learnstudy_med_clinical_reasoning_drill.md
  - domain-education-teaching/learner-study-skills/learnstudy_practice_test_generator.md
  - domain-education-teaching/learner-study-skills/learnstudy_error_correction_cycle.md
---

## Objective

Generate NCLEX-style alternate-format question drills that go beyond standard MCQ: SATA (select all that apply), ordered response, priority and delegation, and hot-spot descriptions. Each question includes rationale for every option (correct and incorrect), test-taking strategy guidance, and NCLEX Next Generation (NGN) question awareness.

## When to Use

- Preparing for the NCLEX-RN or NCLEX-PN exam
- When SATA or delegation questions are the most missed question types in practice
- When a learner is scoring well on standard MCQ but struggling with alternate formats
- During the final review phase (4–8 weeks before exam) when realistic question exposure matters

**Do not use** as a substitute for content review — content knowledge must be solid before question practice is effective. If foundational knowledge gaps are the primary problem, use `learnstudy_retrieval_drill_designer.md` for content mastery first.

## Instructions

1. **Collect inputs.**
   - Ask: "Which clinical area(s) for this session? (Medical-surgical, pediatrics, OB/maternity, psychiatric/mental health, community, leadership/management)"
   - Ask: "Which question formats to include? (SATA, ordered response, priority, delegation, or all)"
   - Ask: "How many questions for this session? (10–20 recommended per session)"
   - Ask: "Any specific topics where you are losing points?"

2. **Generate questions by format type.**

   **Format 1 — SATA (Select All That Apply):**
   - Provide a clinical stem + 5–7 options
   - Correct answers: typically 2–4 options (avoid all or none correct)
   - Test-taking strategy note: "Each option stands alone — evaluate each independently as True/False"
   - Rationale: provide a brief explanation for WHY each option is correct or incorrect (most learners only read why the correct answers are right, not why wrong answers are wrong)

   **Format 2 — Ordered Response / Priority (Drag-and-drop):**
   - Provide 4–6 actions or assessments that the nurse must place in the correct sequence
   - Include the ordering rationale (which step must precede which and why)
   - Common error: placing intervention before assessment

   **Format 3 — Priority Question:**
   - Provide 4 patients or 4 nursing actions and ask which the nurse should address FIRST
   - Prioritization framework: use ABCs (Airway, Breathing, Circulation), then Maslow's Hierarchy, then safety
   - Distinguish: Which option is the most physiologically urgent? (Not: which is most interesting or most recently mentioned)

   **Format 4 — Delegation Question:**
   - Provide a clinical scenario and ask what can be delegated to UAP (unlicensed assistive personnel) vs. LPN vs. RN
   - Delegation rules built in:
     - UAP can: assist with ADLs, vital signs on stable patients, repositioning, oral hygiene
     - UAP cannot: assess, teach, interpret data, perform skills requiring nursing judgment
     - LPN can: perform stable, predictable tasks; cannot perform initial assessments, IV push meds in most states
     - RN retains: initial assessment, care planning, evaluation, patient teaching, unstable patients

   **Format 5 — NGN (Next Generation NCLEX) Matrix/Bowtie:**
   - Describe the scenario: condition + context
   - Ask learner to identify: (1) client condition, (2) priority nursing actions, (3) parameters to monitor
   - Evaluate using the NGN "Bowtie" framework: Patient conditions → Priority actions → Expected outcomes

3. **Provide full rationale for every option.**
   Not just "correct" or "incorrect" — explain the clinical reasoning:
   - Why is this option correct? What assessment finding or pathophysiology supports it?
   - Why is this wrong answer plausible? What misconception does it target?

4. **Include a test-taking strategy note per question.**
   Each question includes a 1–2 sentence test-taking tip specific to that question format or topic area.

5. **Generate a session performance summary.**
   After all questions:
   - Score by format type (SATA, priority, delegation) to identify where errors cluster
   - Flag any content area where 2+ questions were missed

## Output Format

```
# NCLEX Drill: [Clinical Area]
Format types: [SATA/Priority/Delegation/Ordered] | Questions: N

---

## Question [#] — [Format Type] — [Clinical Area/Topic]

[Clinical stem]

**Options:**
A. [Option]
B. [Option]
[etc.]

*(Cover answers below until attempted)*

---

**Correct answer(s):** [A, C, E] or [Sequence: B, D, A, C]

**Rationale:**
✓ A: [Why correct]
✗ B: [Why incorrect — what misconception this targets]
✓ C: [Why correct]
[etc.]

**Test-taking strategy:** [1–2 sentences]

---

## Session Summary
| Format | Questions | Correct | % |
|---|---|---|---|
| SATA | | | |
| Priority | | | |
| Delegation | | | |
| Ordered | | | |

Content areas to review: [topics with ≥2 errors]
```

## Example Output

---

**Input:** Medical-surgical + Leadership/Management — All formats — 8 questions — Weakness: delegation and SATA

---

# NCLEX Drill: Medical-Surgical / Leadership
Format types: SATA, Priority, Delegation, Ordered Response | Questions: 8

---

## Question 1 — SATA — Respiratory (COPD)

A nurse is caring for a client with COPD who is dyspneic. Which nursing interventions are appropriate? Select all that apply.

**Options:**
A. Administer oxygen at 2 L/min via nasal cannula
B. Administer oxygen at 10 L/min via non-rebreather mask
C. Position the client in high Fowler's position
D. Teach pursed-lip breathing
E. Administer a bronchodilator as prescribed
F. Restrict oral fluids to prevent fluid overload
G. Monitor O₂ saturation and respiratory rate

*(Cover until attempted)*

---

**Correct answers: A, C, D, E, G**

**Rationale:**
✓ A: COPD patients should receive low-flow oxygen (1–2 L/min) — they have a hypoxic drive and high-flow O₂ can suppress the respiratory stimulus (hypercarbic drive is impaired; hypoxia is the remaining stimulus)
✗ B: High-flow oxygen (10 L/min) is dangerous in COPD — can suppress hypoxic respiratory drive → respiratory arrest
✓ C: High Fowler's (90°) optimizes diaphragmatic excursion and reduces the work of breathing
✓ D: Pursed-lip breathing slows exhalation, keeps airways open longer, reduces air trapping
✓ E: Bronchodilators relax bronchospasm → improve airflow → reduce dyspnea
✗ F: Fluid restriction is NOT indicated for COPD unless the patient has concurrent heart failure or fluid overload. Adequate hydration helps thin secretions.
✓ G: Continuous monitoring of O₂ sat and RR is essential to detect worsening or O₂ toxicity

**Test-taking strategy:** For COPD questions, remember the key reversal: what helps most patients (high-flow O₂) can harm COPD patients. Also: each SATA option stands alone — do not let finding one correct answer make you assume related options are also correct.

---

## Question 2 — Priority — Multi-patient Assignment

A nurse is assigned four clients. Which client should the nurse assess FIRST?

A. A 68-year-old post-op day 2 abdominal surgery patient with a pain level of 6/10
B. A 45-year-old with a new diagnosis of type 2 diabetes who wants to learn about diet
C. A 72-year-old with COPD who suddenly becomes confused and restless
D. A 55-year-old with stable CHF who is requesting to call family

*(Cover until attempted)*

---

**Correct answer: C**

**Rationale:**
✓ C: Sudden confusion and restlessness in a COPD patient is a PRIORITY — this is a sign of hypoxia (acute change in mental status = neurological symptom of inadequate oxygenation). This is an airway/breathing emergency until proven otherwise. Assess immediately.
✗ A: Pain 6/10 in a post-op day 2 patient is expected and uncomfortable but not immediately life-threatening. Address after the emergency.
✗ B: Patient education is important but is an elective activity that can wait — not an acute physiological need.
✗ D: Stable CHF with a social request is the lowest priority — stable condition + non-clinical need.

**Prioritization framework applied:** ABC first → neurological change (sign of hypoxia) > pain > education > social/communication need

**Test-taking strategy:** Whenever a question includes "sudden change" or "new onset" of a neurological or respiratory symptom, that patient is almost always priority #1. Stable pain with an expected number (6/10 post-op) does not compete with acute neurological change.

---

## Question 3 — Delegation — UAP vs. RN

A nurse is managing a busy medical-surgical floor. Which task is appropriate to delegate to the unlicensed assistive personnel (UAP)?

A. Performing an initial admission assessment on a newly admitted client
B. Administering a scheduled oral pain medication to a stable patient
C. Repositioning a client who is on contact precautions every 2 hours
D. Teaching a post-op patient how to perform incentive spirometry
E. Interpreting a declining urine output trend in a post-surgical patient

*(Cover until attempted)*

---

**Correct answer: C**

**Rationale:**
✓ C: Repositioning is a standard, predictable activity of daily living that does not require nursing judgment. Contact precautions require PPE training (which UAPs receive), but the act of repositioning itself is within UAP scope.
✗ A: Initial admission assessment requires nursing judgment and RN clinical decision-making — never delegable to UAP.
✗ B: Oral medications require verification of "5 Rights," assessment of swallowing/aspiration risk, and understanding of medication effects — within LPN scope in many states, but generally not UAP scope.
✗ D: Patient teaching requires assessment of learning readiness and clinical judgment — never delegable to UAP.
✗ E: Interpreting clinical trends and recognizing deviations (declining UO) is assessment + clinical judgment — RN only.

**Test-taking strategy for delegation:** Ask "Does this require nursing judgment, assessment, teaching, or evaluation?" → If yes → RN. If it's a simple, stable, predictable physical task → UAP may perform. When in doubt: if the patient can change or deteriorate → RN.

---

## Question 4 — Ordered Response — Post-Op Care

A nurse receives a post-operative patient from the recovery room following abdominal surgery. Place the following nursing actions in the correct sequence.

A. Check vital signs and oxygen saturation
B. Review the post-op orders and surgeon's notes
C. Perform a head-to-toe assessment
D. Administer ordered pain medication if the patient rates pain ≥ 7/10
E. Document assessment findings and interventions

*(Cover until attempted)*

---

**Correct sequence: B → A → C → D → E**

**Rationale for sequence:**
1. **B first:** Review orders first — you need to know what parameters exist and what is ordered before you assess or intervene. Attempting assessment without knowing the surgeon's orders means you won't know what to watch for.
2. **A second:** Vital signs and O₂ sat are the first clinical data points — these are rapid and may reveal an immediate emergency (hypotension, hypoxia) requiring intervention before a full assessment.
3. **C third:** Systematic head-to-toe assessment provides a complete baseline picture; this follows vital signs because you've already identified any urgent abnormalities.
4. **D fourth:** Intervention (medication) follows assessment — you don't medicate before you assess (critical principle: assess before intervene).
5. **E last:** Documentation comes after all clinical actions are completed.

**Common error:** Placing D (pain medication) before the assessment (C) — driven by empathy/urgency to relieve pain. Remember: assess before you intervene, always.

**Test-taking strategy:** For ordered response questions, apply this hierarchy: Review orders → Assess → Intervene → Document. When two assessment steps are present, vital signs usually precede a full physical exam.

---

## Question 5 — SATA — Medications (Digoxin Toxicity)

A nurse is assessing a client taking digoxin. Which findings should the nurse report to the healthcare provider? Select all that apply.

**Options:**
A. Apical pulse of 48 beats per minute
B. Serum digoxin level of 0.8 ng/mL
C. Client reports yellow-green halos around lights
D. Potassium level of 3.1 mEq/L
E. Nausea and vomiting for the past 24 hours
F. Client reports feeling "really good" today
G. Urine output of 60 mL/hr

*(Cover until attempted)*

---

**Correct answers: A, C, D, E**

**Rationale:**
✓ A: Bradycardia (apical pulse < 60) is a sign of digoxin toxicity. Digoxin slows conduction → HR < 60 is a critical sign to hold the dose and report.
✗ B: A digoxin level of 0.8 ng/mL is within therapeutic range (0.5–2.0 ng/mL) — not a reportable finding.
✓ C: Visual disturbances — yellow-green halos, blurred vision — are classic signs of digoxin toxicity (direct CNS/retinal effect).
✓ D: Hypokalemia (K⁺ < 3.5) potentiates digoxin toxicity — low K⁺ increases digoxin binding to Na-K-ATPase → toxic effects at lower drug levels. This is a priority electrolyte concern.
✓ E: Nausea and vomiting are early GI signs of digoxin toxicity — often the first symptom reported by patients.
✗ F: "Feeling really good" is a reassuring symptom — not a toxicity indicator. Learners sometimes choose this due to "too good to be true" thinking, but there is no clinical reason to report it.
✗ G: Urine output of 60 mL/hr (>30 mL/hr) is adequate and expected — not concerning.

**Test-taking strategy:** For digoxin toxicity, remember the triad: HR (bradycardia), vision (yellow-green halos), GI (nausea/vomiting). Hypokalemia is always a dangerous companion to digoxin. The therapeutic level does NOT rule out toxicity in the presence of symptoms.

---

## Question 6 — Priority — Delegation (Multi-part)

The RN is working with one LPN and one UAP. Which assignment is MOST appropriate?

A. The LPN performs the initial assessment on a newly admitted patient with pneumonia
B. The UAP takes vital signs on a post-op day 1 patient who is stable
C. The LPN administers IV morphine via push for a patient with sickle cell crisis pain
D. The UAP provides perineal care to a patient with a urinary catheter

*(Cover until attempted)*

---

**Correct answer: B and D (both are appropriate; B is most clearly correct)**

In single-answer format, **B** is the best answer:

**Rationale:**
✓ B: UAP taking vital signs on a stable patient is the most clearly appropriate delegation — stable patient, non-invasive task, routine, predictable. UAP scope includes vital signs on stable patients.
✗ A: Initial assessment is RN-only — LPN cannot perform initial admission assessments.
✗ C: IV push morphine — in most U.S. states and most facility policies, LPNs cannot administer IV push medications. This would require RN administration. Also: opioid IV push requires assessment skills for side effects (respiratory depression).
✓ D: Perineal care is a standard ADL within UAP scope — but "D" is correct as a standalone question. In this format, B is the "most appropriate" because it avoids any scope ambiguity.

**Test-taking strategy for delegation:** Know the hierarchy of who can do what:
UAP ← LPN ← RN (most restrictive to least restrictive)
IV push = RN only (in most contexts)
Initial assessment = RN only
Stable, routine ADL tasks = UAP appropriate

---

## Question 7 — SATA — Psychiatric (Lithium Toxicity)

A nurse is caring for a patient with bipolar disorder on lithium therapy. Which findings indicate possible lithium toxicity? Select all that apply.

**Options:**
A. Serum lithium level of 1.0 mEq/L
B. Coarse hand tremors
C. Slurred speech
D. Polyuria and polydipsia
E. Ataxia (difficulty with coordination)
F. Serum sodium of 138 mEq/L
G. Report of nausea and vomiting

*(Cover until attempted)*

---

**Correct answers: B, C, E, G**

**Rationale:**
✗ A: A lithium level of 1.0 mEq/L is within the therapeutic range (0.6–1.2 mEq/L for maintenance). Not a toxicity sign.
✓ B: Coarse tremors (as opposed to fine tremors, which are a normal side effect) indicate increasing toxicity.
✓ C: Slurred speech is a CNS sign of lithium toxicity.
✗ D: Polyuria and polydipsia are common side effects of lithium at therapeutic levels (nephrogenic diabetes insipidus) — not necessarily toxicity indicators.
✓ E: Ataxia is a CNS toxicity sign — loss of coordination indicates neurological impairment.
✗ F: Normal sodium is not a toxicity indicator. (Low sodium actually increases toxicity by causing lithium reabsorption in the kidney — hyponatremia is a risk factor, not a sign of toxicity.)
✓ G: GI symptoms (nausea, vomiting, diarrhea) are early signs of lithium toxicity.

**Test-taking strategy:** Distinguish normal lithium side effects (fine tremor, polyuria, weight gain) from toxicity signs (coarse tremors, ataxia, slurred speech, seizures, altered consciousness). The progression: early toxicity = GI; mid = neuromuscular; late = seizures, coma.

---

## Question 8 — Ordered Response — Seizure Management

A nurse witnesses a patient having a generalized tonic-clonic seizure. Place the following actions in the correct order.

A. Time the seizure duration
B. Clear the area of hard or sharp objects
C. Document the seizure: duration, type, post-ictal state
D. Turn the patient to the side (recovery position)
E. Call for help / activate emergency response
F. Administer prescribed benzodiazepine if seizure continues > 5 minutes

*(Cover until attempted)*

---

**Correct sequence: B → A → E → D → F → C**

**Rationale:**
1. **B:** Safety first — clear the environment to prevent injury during the seizure. Do not restrain.
2. **A:** Time the seizure immediately — duration determines intervention threshold (benzodiazepines if > 5 min = status epilepticus).
3. **E:** Call for help — do not leave the patient alone; activate emergency response in case rapid medication or airway management is needed.
4. **D:** Turn to the side — recovery position prevents aspiration; airway protection is ongoing priority.
5. **F:** Benzodiazepine administration if seizure > 5 minutes (status epilepticus) — intervention after safety, timing, and positioning.
6. **C:** Documentation follows all clinical interventions — accurate documentation is important but happens last.

**Common error:** Choosing restraint as an early action — never restrain a seizing patient (increases injury risk). Also: do not place anything in the patient's mouth (common myth — can cause injury).

---

## Session Summary

| Format | Questions | Correct | % |
|---|---|---|---|
| SATA | 3 (Q1, Q5, Q7) | ___ | ___ |
| Priority | 2 (Q2, Q6) | ___ | ___ |
| Delegation | 2 (Q3, Q6) | ___ | ___ |
| Ordered Response | 2 (Q4, Q8) | ___ | ___ |

**Content areas to review if ≥2 errors:**
- Digoxin toxicity signs (Q5)
- Delegation hierarchy (Q3, Q6)
- COPD oxygen management (Q1)
- Post-ictal seizure management sequence (Q8)

---

## False-Positive Prevention

**❌ DON'T** treat SATA as "pick the best 2-3 answers." Each option is independently correct or incorrect.

**✅ DO** evaluate each SATA option separately as if it were a true/false statement. Selecting too few or too many is equally wrong.

**❌ DON'T** prioritize patient-expressed wishes (e.g., "patient wants medication") over physiological urgency in priority questions.

**✅ DO** apply ABCs, then Maslow, then safety before considering patient preferences in priority sequencing.

**❌ DON'T** assume any task can be delegated to an LPN just because the LPN is "more skilled than UAP." LPN scope is state-dependent — know the federal NCLEX standard (initial assessment and IV push = RN only).

**✅ DO** use the three-tier delegation hierarchy: UAP (stable, routine, predictable physical tasks) → LPN (stable, predictable nursing skills) → RN (assessment, teaching, evaluation, unstable patients, IV push).

**❌ DON'T** read distractor options as equally plausible in ordered response questions. Apply the universal sequence: assess/review orders → assess → intervene → document.

**✅ DO** use "assess before intervene" as a default tie-breaker for ordered response questions where two steps are competing.

## Quality Criteria

- [ ] All four format types are represented across the session
- [ ] SATA questions have 2–4 correct options (not all correct, not only one)
- [ ] Every rationale explains WHY each option is correct or incorrect (not just "correct" or "incorrect")
- [ ] Delegation questions specify the staff member by role (UAP/LPN/RN) with a scope justification
- [ ] Test-taking strategy note is present for every question
- [ ] Session summary tracks performance by format type, not just total score

## Techniques Used

- **ST-01 (Clear Objective Statement):** Objective specifies alternate-format questions specifically (not standard MCQ) as the target — this is what distinguishes NCLEX drill from generic Q&A
- **ST-02 (Structured Sequential Instructions):** Five-step process ensures format selection and content specification before questions are generated
- **ED-02 (Progressive Exercise Generation):** Format types escalate from SATA (structured selection) to ordered response (sequencing) to NGN-style (pattern recognition)
- **NE-04 (Good vs Bad Example Calibration):** Rationale section pairs correct and incorrect options explicitly — not just "why C is right" but "why B is wrong and what misconception it exploits"
- **QA-01 (Self-Verification):** Session summary tracks performance by format type, revealing which question format is weakest rather than obscuring it in an overall score
