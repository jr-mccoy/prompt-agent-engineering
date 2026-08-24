---
title: "Parkinson's Disease Longitudinal Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Build a Parkinson's disease management plan: dopaminergic therapy selection and titration, motor-fluctuation management, non-motor symptoms, and advanced-therapy referral with named drugs and doses."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - neurology
  - parkinsons
  - movement-disorder
  - care-plan
updated: "2026-06-19"
---

## Objective

Produce a Parkinson's disease care plan: initiate and titrate dopaminergic therapy matched to age and symptom burden, manage motor fluctuations and dyskinesia as disease advances, address non-motor symptoms, and time advanced-therapy referral. Output is a longitudinal motor + non-motor plan.

## Inputs

- Disease: duration, predominant symptoms (tremor/rigidity/bradykinesia/gait), Hoehn-Yahr stage, motor fluctuations (wearing-off, on-off, dyskinesia)
- Patient: age, cognition (dementia risk affects agent choice), falls, occupation
- Current regimen: levodopa/agonist/MAO-B doses and timing, response, side effects (impulse control, hallucinations, orthostasis)
- Non-motor: constipation, orthostatic hypotension, REM sleep behavior disorder, depression/anxiety, cognition/hallucinations, urinary, pain
- Comorbidities, medications (avoid dopamine blockers)

## Role

Neurologist/movement-disorder specialist managing Parkinson's disease.

## Reasoning Steps

1. **Confirm clinical diagnosis** (bradykinesia + rest tremor or rigidity; levodopa responsiveness) and assess motor + non-motor burden and stage.

2. **Initiate symptomatic therapy when symptoms impair function:**
   - **Carbidopa/levodopa** — most effective; first-line especially in older patients or significant disability. Start 25/100 TID, titrate to effect.
   - **Dopamine agonists** (pramipexole, ropinirole, rotigotine patch) — younger patients to delay levodopa motor complications, but higher impulse-control disorder, somnolence, orthostasis, edema; avoid in cognitive impairment/elderly.
   - **MAO-B inhibitors** (rasagiline, selegiline) — mild disease, modest benefit, adjunct.
   - **Amantadine** — tremor and especially dyskinesia.

3. **Manage motor fluctuations (wearing-off) as disease advances:**
   - Increase levodopa frequency / shorten interval; add COMT inhibitor (entacapone, opicapone) to extend each dose; add MAO-B inhibitor; add dopamine agonist; consider extended-release levodopa or inhaled levodopa for off periods.
   - **Dyskinesia:** amantadine (ER amantadine reduces dyskinesia); reduce individual levodopa dose while maintaining frequency.

4. **Advanced-therapy referral** for refractory fluctuations/dyskinesia despite optimization: deep brain stimulation (STN/GPi), levodopa-carbidopa intestinal gel, continuous subcutaneous infusions. Patient selection (good levodopa response, no significant dementia) matters.

5. **Non-motor management (major quality-of-life burden):**
   - Constipation: fiber/fluids, PEG.
   - Orthostatic hypotension: hydration/salt, droxidopa/midodrine/fludrocortisone; deprescribe contributors.
   - REM sleep behavior disorder: melatonin, clonazepam; safety.
   - Depression/anxiety: SSRI/SNRI; dopamine agonists may help.
   - Psychosis/hallucinations: reduce/sequence-down PD meds, then pimavanserin or quetiapine/clozapine — **never typical antipsychotics or risperidone** (worsen motor; avoid metoclopramide/prochlorperazine too).
   - Dementia: rivastigmine.

6. **Avoid dopamine-blocking drugs** (typical antipsychotics, metoclopramide, prochlorperazine) — worsen parkinsonism.

7. **Multidisciplinary:** physical therapy/exercise (disease-modifying for function), occupational/speech therapy (LSVT), fall prevention, swallow evaluation, support.

8. **Monitor:** motor response and fluctuations, impulse-control disorders (ask explicitly with agonists), orthostatics, cognition, mood, weight/swallow, medication timing adherence.

## Output Format

```
DIAGNOSIS / STAGE / PREDOMINANT FEATURES / FLUCTUATIONS:

MOTOR THERAPY:
- Initiation/optimization: [levodopa vs agonist vs MAO-B by age/cognition, dose]
- Fluctuation management: [COMT/MAO-B/frequency/amantadine]
- Dyskinesia management

ADVANCED THERAPY:
- DBS / infusion referral criteria

NON-MOTOR PLAN:
- Constipation / OH / RBD / mood / psychosis / cognition

DRUGS TO AVOID:
- [dopamine blockers]

MULTIDISCIPLINARY:
- PT/exercise, OT/speech, falls, swallow

MONITORING:
- Motor, ICD screen, orthostatics, cognition, mood, adherence

PITFALLS:
- [agonist ICD/hallucinations in elderly, typical antipsychotics/metoclopramide, under-recognized non-motor burden]
```

## Worked Example

**Input:** 72 y/o M, Parkinson's 5 years, Hoehn-Yahr 3. On carbidopa/levodopa 25/100 TID with end-of-dose wearing-off ~1 h before next dose and mild peak dyskinesia. Constipation, orthostatic dizziness. Mild cognitive complaints. No hallucinations. On no dopamine agonist.

**Output:**

```
DIAGNOSIS / STAGE / FLUCTUATIONS: PD 5 years, H-Y 3, wearing-off + mild peak-dose dyskinesia.

MOTOR THERAPY:
- Wearing-off: add a COMT inhibitor (opicapone 50 mg qhs or entacapone 200 mg with each levodopa dose) to extend each dose; and/or shorten interval to QID. Add rasagiline 1 mg as adjunct option.
- Avoid adding a dopamine agonist — age 72 + cognitive complaints → high risk of hallucinations/impulse-control/orthostasis. Optimize levodopa-based therapy instead.
- Peak dyskinesia: extended-release amantadine (also helps), and/or slightly reduce each levodopa dose while keeping frequency.

ADVANCED THERAPY:
- Not yet — optimize oral regimen first. If fluctuations stay refractory despite optimization and he remains levodopa-responsive without significant dementia, consider DBS/infusion referral (cognition will factor into candidacy).

NON-MOTOR PLAN:
- Constipation: PEG + fiber/fluids.
- Orthostatic hypotension: hydration/salt, review/deprescribe contributors; midodrine or droxidopa if persistent; counsel slow positional changes (fall risk).
- Cognition: formal assessment; if PD dementia emerges, rivastigmine.
- Mood/RBD/urinary: screen and treat.

DRUGS TO AVOID: no metoclopramide/prochlorperazine for the constipation/nausea, no typical antipsychotics/risperidone — they worsen parkinsonism.

MULTIDISCIPLINARY: PT/structured exercise, fall-prevention program, OT, speech/swallow eval as indicated.

MONITORING: motor diary (on/off, dyskinesia), orthostatic vitals, cognition, mood, adherence to dosing times.

PITFALLS:
- Resist the dopamine agonist in this older, cognitively-vulnerable patient.
- Treat the OH and constipation — major QoL and safety issues.
- Keep dopamine-blocking antiemetics off the list.
```
