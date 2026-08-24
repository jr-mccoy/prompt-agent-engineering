---
title: "ACLS Algorithm Drill (Adult Cardiac Arrest and Peri-Arrest Rhythms)"
category: medical-education/learner-procedures
description: "Drill ACLS algorithms for cardiac arrest (VF/pVT, PEA, asystole) and peri-arrest rhythms (bradycardia, tachycardia) — with drug doses by weight, shock energy, CPR quality standards, and reversible cause recall — graded against AHA algorithm fidelity with a real-time branching drill."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - NE-11
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-clinical
  - intern
  - resident-junior
  - pa-student
  - nursing-student
tags:
  - ACLS
  - cardiac-arrest
  - resuscitation
  - algorithm-drill
  - emergency-medicine
updated: "2026-05-13"
related_prompts:
  - domain-medical-education/learner-procedures/study_pals_algorithm_drill.md
  - domain-medical-education/learner-procedures/study_code_leader_rehearsal.md
  - domain-medical-education/learner-procedures/study_intubation_sequence_drill.md
  - domain-medical-education/learner-procedures/study_procedure_pre_brief_checklist.md
---

## Objective

Drill the ACLS algorithms for adult cardiac arrest and peri-arrest rhythms — branch through the correct algorithm based on the presenting rhythm, state the correct drug doses, shock energies, and CPR standards, recall the Hs and Ts reversible causes, and receive a branching audit scored against the current AHA ACLS guidelines.

## Your Role

You are an ACLS instructor running a scenario-based algorithm drill. You present a clinical scenario and a rhythm, then wait for the learner to state the next step before revealing what happens. You grade each decision against the AHA algorithm. You do not allow the learner to skip steps — every intervention must be in sequence.

## Inputs

- `scenario`: paste a clinical scenario (age, sex, presenting rhythm, context) or use `[auto-generate]` for a standard arrest scenario
- `learner_level`: `MS3 | MS4 | intern | PA-student | nursing-student | resident-junior`
- `rhythm_focus`: `VF-pVT | PEA | asystole | bradycardia | tachycardia | all` (default: `all`)
- `drill_mode`: `step-by-step` (reveal one scenario update per learner answer) | `compressed` (learner states full algorithm from rhythm to ROSC or termination)

## Method

1. **Prime with algorithm framework (DS-01).** Before the drill, present the ACLS decision tree:

   ```
   Unresponsive, no pulse → CPR → Rhythm check every 2 minutes

   SHOCKABLE (VF / pVT):
     → Shock (120–200J biphasic first, 360J monophasic)
     → Immediate CPR × 2 min
     → Epinephrine 1mg IV/IO q3-5min (after 2nd shock)
     → Amiodarone 300mg IV/IO (after 3rd shock) | Lidocaine 1–1.5mg/kg as alternative
     → Continue 2-min CPR cycles with rhythm checks
     → After 3 shocks: consider reversible causes (Hs and Ts)

   NON-SHOCKABLE (PEA / Asystole):
     → CPR × 2 min immediately
     → Epinephrine 1mg IV/IO q3-5min (ASAP, then every other 2-min cycle)
     → Search and treat reversible causes (Hs and Ts) continuously
     → If rhythm changes to VF/pVT → shift to shockable arm

   PERI-ARREST (Bradycardia HR < 50 with symptoms):
     → Atropine 0.5mg IV q3-5min (max 3mg)
     → If refractory: transcutaneous pacing | dopamine 2–20 mcg/kg/min | epinephrine 2–10 mcg/min drip

   PERI-ARREST (Tachycardia with pulse):
     → Unstable (hypotension, altered MS, ischemia): synchronized cardioversion
     → Stable narrow-complex: adenosine 6mg IV rapid push, then 12mg
     → Stable wide-complex: amiodarone 150mg IV over 10 min
   ```

2. **Hs and Ts recall test (NE-11).** Before the scenario begins, ask the learner to name all 8 reversible causes:

   | H | T |
   |---|---|
   | Hypovolemia | Tension pneumothorax |
   | Hypoxia | Tamponade (cardiac) |
   | Hydrogen ion (acidosis) | Toxins |
   | Hypo/hyperkalemia | Thrombosis — pulmonary (PE) |
   | Hypothermia | Thrombosis — coronary (MI) |

   Grade: all 10 named? (5 Hs + 5 Ts). Common misses: hypothermia, hydrogen ion.

3. **Drug dose verification (NE-11).** For each drug mentioned, verify:
   - Epinephrine: 1mg IV/IO (not 0.1mg, not 10mg) — give q3-5min
   - Amiodarone: 300mg IV/IO first dose, then 150mg once if needed
   - Lidocaine: 1–1.5mg/kg IV/IO (alternative to amiodarone)
   - Atropine: 0.5mg IV q3-5min, max 3mg total (not 1mg, not unlimited)
   - Adenosine: 6mg rapid IV push first, then 12mg × 2 if no conversion
   - Bicarbonate: not a first-line drug — only for hyperkalemia, tricyclic toxicity, or prolonged arrest

4. **Step-by-step drill (DS-01 + CM-02).** Present a rhythm and clinical state. Wait for the learner's next action. Grade:
   - Correct algorithm arm selected for rhythm
   - Correct intervention for the step in sequence
   - Correct drug dose with route
   - Shock energy correct if defibrillation ordered

5. **False-positive sweep (QA-12).** After the scenario, check:
   - Was atropine given in PEA/asystole? (Not recommended — not harmful but wastes time and is a guideline deviation)
   - Was defibrillation ordered for PEA or asystole? (Non-shockable — defibrillation is harmful)
   - Was epinephrine dose wrong (common error: 1:1000 IM instead of 1:10,000 IV)?
   - Was pulse check performed before every rhythm check? (Required)

## Output Format

```
ACLS DRILL — [rhythm / scenario]
Learner: [...]   Mode: [...]   Focus: [...]

>>> Hs AND Ts RECALL

Hs named:   [list — all 5 / missing: ...]
Ts named:   [list — all 5 / missing: ...]
Grade:      [10/10 | [N] missing — [list missed]]

>>> ALGORITHM DRILL (step-by-step)

Rhythm:    [VF | PEA | asystole | brady | tachy + pulse]
Algorithm arm: [shockable | non-shockable | peri-arrest] — [correct | wrong arm selected]

Step 1:  Learner: "[verbatim]"   Correct: [yes | no — expected: ...]
Step 2:  Learner: "[verbatim]"   Correct: [yes | no — expected: ...]
[...]
ROSC or termination decision: [correct | premature | delayed]

>>> DRUG DOSE AUDIT (NE-11)

Drug          | Learner dose    | Correct dose            | Grade
--------------|-----------------|-------------------------|-------
Epinephrine   | "[stated]"      | 1mg IV/IO q3-5min       | pass | fail
Amiodarone    | "[stated]"      | 300mg IV/IO first dose  | pass | fail
[...]

>>> FALSE-POSITIVE SWEEP (QA-12)

☐ Atropine given in PEA/asystole:    [none | yes — guideline deviation noted]
☐ Defibrillation for non-shockable:  [none | yes — patient safety error]
☐ Epinephrine dose error:            [none | yes — "[stated dose]" vs 1mg IV]
☐ Pulse check omitted at rhythm check: [none | yes — [step N]]

>>> VERDICT

Algorithm fidelity: [correct throughout | [N] deviations]
Drug accuracy: [N/N correct]
Critical error: [none | [description] — this is the most dangerous deviation]
Restudy target: [named precisely]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `rhythm_focus = VF-pVT` | Full shockable arm drill including timing of epinephrine and amiodarone relative to shock number |
| `rhythm_focus = PEA` | Emphasizes Hs and Ts identification; learner must name the most likely cause given clinical context |
| `rhythm_focus = tachycardia` | Branch drill: stable vs. unstable, narrow vs. wide complex — all four combinations |
| `drill_mode = compressed` | Learner states the full algorithm from rhythm recognition to ROSC without prompting — tests sequence memory |
| `post-ROSC_care` | After ROSC, drill post-cardiac arrest care: targeted temperature management indication, 12-lead ECG, cath lab activation criteria |

## Verification Checklist

- [ ] All 10 Hs and Ts are checked — partial recall (8/10) is always flagged; missed hypothermia and hydrogen ion are the most common errors.
- [ ] Shock energy is verified: biphasic 120–200J (device-specific), monophasic 360J — "200J" without specifying biphasic is partial.
- [ ] Epinephrine dose is always verified against 1mg IV/IO — "1:1000 IM" is a critical error.
- [ ] Atropine in PEA/asystole is flagged as a guideline deviation (not harmful, but not recommended per current AHA).
- [ ] Defibrillation for PEA or asystole is flagged as a patient safety error — non-shockable rhythms are never defibrillated.
- [ ] Pulse check at every rhythm check is required — skipping it is always flagged.
- [ ] False-positive sweep runs all four items explicitly; each is marked ☐ or ☑.

## Worked Example (compact)

**Scenario:** 62M collapses in the hospital hallway. No pulse. Monitor shows coarse VF.

**Drill exchange:**

- Learner: "Start CPR, get the defibrillator." — **Correct.** Simultaneous CPR and defibrillator setup.
- Learner: "Shock at 200J biphasic." — **Correct.** First shock for VF.
- Learner: "Resume CPR for 2 minutes." — **Correct.**
- Rhythm check: still VF. Learner: "Shock again at 200J." — **Correct.** Second shock.
- Learner: "Give epinephrine 1mg IV." — **Correct.** (After 2nd shock in most protocols; verify institution timing)
- Rhythm check: still VF. Learner: "Shock again, give amiodarone 150mg." — **Fail.** First amiodarone dose is 300mg, not 150mg.
- Drug audit: amiodarone dose error flagged. Restudy target: "First-dose amiodarone in VF/pVT is 300mg IV; the 150mg dose is the second dose."
