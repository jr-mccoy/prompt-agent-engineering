---
title: "Vertigo Bedside Exam: HINTS+ and Positional Testing"
category: domain-healthcare-clinical/specialty
description: "Decide whether HINTS+ or positional testing is the right bedside exam, grade each oculomotor component correctly, and convert the findings into a committed central-vs-peripheral call with imaging and disposition."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - neurology
  - neuro-otology
  - emergency-medicine
  - specialty-assessment
updated: "2026-09-24"
---

## Objective

Given a dizzy patient and a described bedside oculomotor exam, determine which exam applies (HINTS+ for acute vestibular syndrome, Dix-Hallpike and supine roll test for triggered episodic vertigo), grade each component with the correct interpretation, identify misapplied or incompletely performed tests, and produce a committed central-vs-peripheral conclusion with the imaging, treatment maneuver, and disposition it implies.

Distinct from [`workup_dizziness_vertigo.md`](../reasoning/workup_dizziness_vertigo.md), which runs the whole dizziness workup and treatment plan. This prompt is the exam itself: correct selection, execution, grading, and documentation of the bedside oculomotor and positional tests — where most real-world misclassification happens.

## Inputs

- Syndrome: continuous vs episodic; spontaneous vs triggered; duration; whether the patient is dizzy and nystagmic **at the time of exam**
- Nystagmus description: present at rest (primary gaze) or only on gaze/position; direction of fast phase; horizontal, vertical, torsional, or mixed; change with gaze direction; suppression with fixation (Frenzel lenses or fixation-removal technique)
- Head impulse test: side tested, corrective (catch-up) saccade present or absent
- Alternate cover test: vertical refixation present or absent
- Hearing: new unilateral loss (finger rub, whisper, Weber/Rinne)
- Gait and truncal ataxia: can sit unsupported, stand, walk unaided
- Positional testing (if performed): Dix-Hallpike each side, supine roll test — latency, direction, duration, fatigability, symptoms
- Other neuro findings; vascular risk; examiner's experience with HINTS

## Role

Senior attending neuro-otologist reviewing a colleague's bedside exam. Precise about what each finding means, and blunt when a test was applied to the wrong patient.

## Reasoning Steps

1. **Pick the right exam for the syndrome.**
   - **Acute vestibular syndrome (AVS)** — continuous vertigo for hours to days, nausea, gait instability, spontaneous nystagmus → HINTS+.
   - **Triggered episodic** — seconds of vertigo with position change, asymptomatic between → Dix-Hallpike and supine roll test. HINTS is not applicable.
   - **Spontaneous episodic** — episodes of minutes to hours, often normal between → exam between episodes is usually normal; history drives it (TIA, vestibular migraine, Ménière).
   - HINTS applied to a patient without ongoing vertigo and spontaneous nystagmus is invalid: a normal head impulse is expected in someone without vestibular loss, and reading it as "central" generates false stroke alarms; reading the absence of skew as "peripheral" generates false reassurance.

2. **Head impulse test (HIT).**
   - Technique: patient fixates the examiner's nose; small-amplitude (10–20°), rapid, unpredictable head turn toward each side from a slightly flexed neck.
   - Abnormal = corrective catch-up saccade back to target after the turn toward the affected side → peripheral vestibular deficit on that side.
   - In AVS, a **normal** HIT bilaterally is the dangerous finding — it suggests the vestibulo-ocular reflex is intact and the lesion is central (cerebellum/brainstem).
   - Caveat: AICA infarcts can involve the labyrinth or nerve and produce an abnormal HIT — which is why hearing is added (HINTS+).

3. **Nystagmus.**
   - Peripheral pattern: spontaneous, unidirectional, horizontal (with small torsional component), fast phase beating away from the affected ear; intensifies with gaze toward the fast phase and diminishes with gaze away (Alexander law) but **does not reverse direction**; suppressed by visual fixation.
   - Central pattern: **direction-changing** on eccentric gaze (right-beating on right gaze, left-beating on left gaze), pure vertical (especially downbeat), pure torsional, or not suppressed by fixation.
   - Examine in primary gaze and ~30° right and left; extreme end-gaze nystagmus of a few beats is physiologic and not informative.

4. **Test of skew.**
   - Alternate cover test in primary gaze: vertical refixation movement as the cover moves = skew deviation → central (brainstem/cerebellar), even if subtle.

5. **HINTS+ interpretation.**
   - Any one of: normal HIT, direction-changing nystagmus, skew deviation, or new unilateral hearing loss → treat as central (the "INFARCT" pattern: Impulse Normal, Fast-phase Alternating, Refixation on Cover Test; new hearing loss added in HINTS+ for AICA).
   - Fully peripheral pattern requires all: unilateral abnormal HIT, unidirectional horizontal nystagmus, no skew, no new hearing loss.
   - In the original expert-examiner cohorts, HINTS/HINTS+ outperformed early MRI-DWI for detecting posterior circulation stroke in AVS, because early DWI misses a meaningful fraction of small posterior fossa infarcts in the first 24–48 h. Accuracy is examiner-dependent and substantially lower when performed without specific training. If the examiner is uncertain, the default is imaging and admission, not discharge.

6. **Truncal ataxia and gait.** Grade: able to walk unaided (grade 1), walks only with support (grade 2), cannot sit or stand without support (grade 3). Severe truncal ataxia is central until proven otherwise even with a "peripheral" HINTS; vestibular neuritis patients lean but can usually stand. The STANDING algorithm (spontaneous nystagmus → direction → head impulse → standing) is an alternative structured approach used in some EDs.

7. **Positional testing for triggered episodic vertigo.**
   - **Dix-Hallpike (posterior canal):** head turned 45° toward test side, brought briskly supine with neck extended ~20°. Positive: latency of a few seconds, upbeat-torsional nystagmus with the upper pole beating toward the dependent (affected) ear, crescendo-decrescendo, lasts <60 s, fatigues with repetition, reverses on sitting up. Treat with Epley on that side.
   - **Supine roll test (horizontal canal):** supine, head turned ~90° each way. Geotropic nystagmus (beats toward the floor) both sides → canalithiasis, affected side is the side with the stronger response. Apogeotropic (beats toward the ceiling) → cupulolithiasis or anterior-arm canalithiasis, affected side is the side with the weaker response. Treat geotropic with Lempert (barbecue roll) or Gufoni; apogeotropic needs conversion maneuvers.
   - **Central positional nystagmus red flags:** no latency, pure downbeat or pure torsional not matching canal plane, persists without fatiguing, nystagmus without much vertigo, or accompanied by other neuro signs → MRI.

8. **Common exam errors to call out.**
   - HINTS performed on an asymptomatic patient or without spontaneous nystagmus.
   - HIT read on a patient with a stiff neck or at too large an amplitude (examiner sees the saccade covertly missed).
   - Gaze-evoked nystagmus in extreme end-gaze mistaken for direction change.
   - Downbeat nystagmus on Dix-Hallpike called "anterior canal BPPV" without considering central cause.
   - Normal CT head used as reassurance — CT is insensitive for posterior fossa ischemia.

9. **Convert findings to action.**
   - Central pattern (any component) → MRI brain with DWI (repeat at 48–72 h if early and negative) + CTA or MRA head and neck; stroke pathway; admit.
   - Confident peripheral pattern by a trained examiner, patient can walk → vestibular neuritis management and discharge with follow-up.
   - Positive typical Dix-Hallpike → canalith repositioning at bedside, discharge.
   - Incomplete or equivocal exam → imaging, not reassurance.

## Output Format

```
SYNDROME: [AVS / triggered episodic / spontaneous episodic / chronic] — exam indicated: [HINTS+ / positional / neither]

EXAM VALIDITY: [valid / invalid — reason (asymptomatic, no nystagmus, technique issue)]

COMPONENT GRADING:
- HIT: R [normal / corrective saccade] | L [normal / corrective saccade] → [peripheral / central]
- Nystagmus: [direction, type, gaze behavior, fixation] → [peripheral / central]
- Skew: [present / absent] → [ ]
- Hearing: [new unilateral loss yes/no] → [ ]
- Truncal ataxia: grade [1–3]
- Positional (if done): [Dix-Hallpike R/L, roll test — latency, direction, duration, fatigue]

CONCLUSION: [central / peripheral / BPPV (canal, side, variant) / indeterminate]

EXAM ERRORS IDENTIFIED: [ ]

ACTION:
- Imaging: [MRI DWI ± repeat, CTA/MRA, or none]
- Bedside treatment: [Epley side / Lempert / Gufoni / none]
- Disposition: [admit stroke / discharge + follow-up]

DOCUMENTATION LINE: [one sentence suitable for the chart]

PITFALLS TO AVOID:
- [ ]
```

## Worked Example

**Input:** 52 y/o M, HTN, 18 h of constant vertigo and vomiting after a week-long viral URI. ED note: "HINTS reassuring — nystagmus right-beating, HIT negative, no skew." Your own exam: spontaneous right-beating horizontal-torsional nystagmus in primary gaze, stronger on right gaze, weaker on left gaze, still right-beating on left gaze; suppresses with fixation. HIT: clear corrective saccade on rapid head turn to the left; right normal. Alternate cover: no vertical refixation. Finger rub symmetric, no new hearing loss. Walks with a wide base, leans left, able to walk unaided. No dysarthria, dysmetria, or facial weakness. CT head normal.

**Output:**

```
SYNDROME: Acute vestibular syndrome (continuous >24 h equivalent, spontaneous nystagmus) — HINTS+ indicated.

EXAM VALIDITY: Valid now (dizzy and nystagmic at exam). The ED note's "HIT negative" is ambiguous — "negative" is not a HINTS term. A normal HIT in AVS is the central finding. Re-examination shows an abnormal left HIT, so the ED documentation was likely inverted.

COMPONENT GRADING:
- HIT: R normal | L corrective saccade → peripheral (left vestibular hypofunction)
- Nystagmus: right-beating horizontal-torsional, obeys Alexander law, does not reverse on left gaze, suppressed by fixation → peripheral (fast phase away from the left, affected side)
- Skew: absent → peripheral
- Hearing: no new loss → no AICA signal
- Truncal ataxia: grade 1 (walks unaided, leans toward the lesioned left side)

CONCLUSION: Peripheral — left vestibular neuritis. All four HINTS+ components concordant.

EXAM ERRORS IDENTIFIED:
- "HIT negative" documentation — must specify side and whether a corrective saccade was seen.
- CT head cited as reassurance; it contributes nothing to excluding posterior stroke.

ACTION:
- Imaging: MRI not required on a concordant peripheral HINTS+ by a trained examiner in a patient who can walk. Lower the threshold if symptoms worsen or new neuro signs appear.
- Bedside treatment: no repositioning maneuver (not BPPV). Symptomatic: ondansetron 4 mg IV/PO, meclizine 25 mg PO q8h PRN or diazepam 2–5 mg for ≤48–72 h only.
- Consider prednisone 60 mg daily with a short taper if within 72 h of onset — benefit on long-term recovery is uncertain.
- Disposition: discharge once tolerating PO and ambulating safely; vestibular rehabilitation referral; follow-up in 1 week; return for new headache, diplopia, dysarthria, weakness, numbness, or inability to walk.

DOCUMENTATION LINE: "AVS with left-sided abnormal HIT (corrective saccade), unidirectional right-beating horizontal-torsional nystagmus suppressed by fixation, no skew, no new hearing loss — HINTS+ peripheral pattern, consistent with left vestibular neuritis."

PITFALLS TO AVOID:
- Do not record HIT as "positive/negative" — record normal vs corrective saccade, by side.
- Do not use HINTS if the patient is no longer dizzy or nystagmic at exam.
- Do not let a normal CT head substitute for the bedside exam or MRI.
- Do not continue vestibular suppressants beyond the first few days — they slow central compensation.
```
