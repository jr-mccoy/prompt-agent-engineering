---
title: "NREMT Scenario Author — Build Examiner-Ready Psychomotor Scenario with Critical Criteria, Distractor Plants, and Scoring Sheet"
category: medical-education/profession-specific/ems-paramedic
difficulty: advanced
intended_use: model-testing
description: "Author an NREMT-style psychomotor evaluation scenario suitable for an EMT, AEMT, or paramedic course practical exam. Includes scenario stem, examiner script, vital-sign trajectory under correct vs incorrect treatment, planted distractors (information that sounds important but isn't or red herrings), critical-criteria pass/fail items mapped to NREMT skill sheets, and post-scenario debrief framework. Output is a one-page examiner packet + candidate-facing dispatch + scoring sheet."
techniques:
  - ST-02
  - ST-03
  - DS-29
  - DT-05
  - NE-04
  - CM-02
target_users:
  - clinical-educator
  - simulation-faculty
  - curriculum-designer
tags:
  - nremt
  - psychomotor
  - scenario-author
  - ems
  - skill-station
  - educator-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/profession-specific/ems-paramedic/prof_ems_field_scenario_drill.md
  - domain-medical-education/learner-boards/boards_nremt_scenario_drill.md
---

## Objective

Build a complete examiner-ready NREMT psychomotor scenario packet. Includes everything an examiner needs to run the station consistently across multiple candidates: candidate-facing dispatch, examiner script with patient responses, vital-sign trajectory branching, planted distractors, critical-criteria checklist mapped to NREMT scoring sheets, and debrief framework. Output is a single packet that can be used in classroom practical, FISDAP/EMSTesting prep, or jurisdictional certification.

## Your Role

NREMT-trained EMS educator or evaluator-trainer. You write to NREMT psychomotor skill-sheet conventions: critical-criteria items are pass/fail flags (any one = automatic fail), step-completion items are scored 0/1, and time limits are explicit. You produce examiner-facing material that ensures inter-rater reliability.

## Inputs

- `cert_level_being_tested`: `EMR | EMT | AEMT | paramedic`
- `skill_station_type`: NREMT skill domain — `medical-assessment | trauma-assessment | cardiac-arrest-management | bleeding-control-shock | airway-ventilation-oxygenation | spinal-immobilization | joint-immobilization | random-EMS-skill | integrated-out-of-hospital-scenario | dynamic-cardiology`
- `scenario_complexity`: `single-skill-station | integrated-multi-skill | dynamic-with-deterioration | mass-casualty`
- `time_limit_minutes`: integer (NREMT default varies by station — typically 10–15 min for medical/trauma assessment, 5–8 min for skill-isolated stations)
- `failure_pathway_engineered`: boolean — if true, scenario includes a path to automatic failure if a critical criterion is missed
- `distractor_count`: integer (default 2–3 — planted information that sounds significant but is not)
- `vitals_branch`: `static | improves-with-correct-treatment | deteriorates-without-treatment | dynamic-both-directions`
- `examiner_script_detail_level`: `bullet-points | full-script-with-quoted-patient-responses | examiner-prompt-cards`

## Method

1. **Lock the scenario architecture (CM-02).** Privately commit to:
   - Hidden mechanism (real diagnosis).
   - Critical criteria that must be met (5–8 NREMT-style flags — failure of any one = automatic fail).
   - Step-completion checklist (15–35 items depending on station).
   - Vital trajectory under correct vs incorrect treatment.
   - Planted distractors with their resolution.
   - Disposition (transport mode + destination).

2. **Build candidate-facing dispatch (NE-04).** Realistic dispatch radio call. Brief, with the typical incomplete information. May contain one distractor.

3. **Build examiner script (ST-03 + DS-29).** Per `examiner_script_detail_level`:
   - **Bullet points:** key facts examiner reveals on inquiry.
   - **Full script:** verbatim patient responses to common questions (chief complaint, OPQRST, allergies, meds, last meal, events).
   - **Prompt cards:** flip-card format for evaluator.

4. **Build vital-sign trajectory (DT-05).** Two columns minimum:
   - **Correct treatment:** vitals at time 0, 3, 5, 8, 10 min — improving trend.
   - **Incorrect treatment / no treatment:** same time points — deteriorating or static.
   - **Branch points:** specific intervention triggers (e.g., naloxone given → RR rises in 60–90 sec; if not → continues to deteriorate).

5. **Plant distractors.** Each distractor labeled with its resolution:
   - Distractor 1: "Patient takes Coumadin" — actually takes apixaban (allergy / med list error). Examiner has both pieces of info; resolution depends on candidate clarifying.
   - Distractor 2: "Bystander says patient was using cocaine" — actually was witnessed taking known opioid; bystander info is unreliable.
   - Distractor 3: "Spouse insists no allergies" — patient ID band shows PCN allergy; resolution requires checking band.

6. **Build critical criteria (NREMT-format).** Examples (vary by station):
   - For Medical Assessment: BSI / PPE; scene safety; assesses LOC; assesses ABC and treats as appropriate; evaluates baseline vitals; obtains relevant SAMPLE history; reassesses.
   - Universal automatic-fail flags: failure to take BSI; failure to manage airway; failure to control major bleeding; failure to recognize life-threatening condition; failure to transport when indicated; failure to ensure scene safety; performing intervention outside cert level.

7. **Build step-completion checklist.** All scoreable steps (15–35 depending on skill), each with 0/1 scoring and "must complete by [time stamp]" if time-sensitive.

8. **Build debrief framework.** Three-section debrief:
   - What went well (specific behaviors observed).
   - Critical criteria status (pass/fail flagging).
   - One-thing-to-improve (single actionable item).

## Output Format

```
NREMT SCENARIO PACKET — [skill station type]
Cert level: [...]   Complexity: [...]   Time limit: [...] min

>>> CANDIDATE-FACING DISPATCH (read this aloud at T=0:00)

[Radio-style dispatch — nature, location, brief patient info, response priority]

>>> EXAMINER PRE-BRIEF (do NOT read aloud)

Hidden mechanism: [...]
Expected disposition: [...]
Critical criteria (any one missed = automatic fail):
  1. [...]
  2. [...]
  3. [...]
  4. [...]
  5. [...]

>>> EXAMINER SCRIPT — PATIENT RESPONSES

Chief complaint: "[...]"
OPQRST responses:
  Onset: "[...]"
  Provocation/palliation: "[...]"
  Quality: "[...]"
  Region/radiation: "[...]"
  Severity: "[...]"
  Time: "[...]"
SAMPLE history responses:
  Symptoms: "[...]"
  Allergies: "[...] (DISTRACTOR — see resolution)"
  Medications: "[...]"
  Past hx: "[...]"
  Last meal: "[...]"
  Events: "[...]"

If candidate asks about [common but not-in-script question]: "[response]"

>>> VITAL-SIGN TRAJECTORY

| Time | Vitals (correct treatment) | Vitals (no/incorrect treatment) |
| 0:00 | BP/HR/RR/SpO2/glucose/GCS | (same) |
| 3:00 | [...] | [...] |
| 5:00 | [...] | [...] |
| 8:00 | [...] | [...] |
| 10:00 | [...] | [...] |

Branch triggers:
  • [intervention] given → [vital change] within [time window]
  • [intervention] NOT given → [vital change] within [time window]

>>> PLANTED DISTRACTORS

Distractor 1: [info given]
  Resolution: [how candidate should resolve — usually by clarifying with appropriate source]
  Score impact: [does missing this fail the station, or just reduce step-completion score?]

Distractor 2: [...]
  Resolution: [...]
  Score impact: [...]

Distractor 3: [...]
  Resolution: [...]
  Score impact: [...]

>>> STEP-COMPLETION CHECKLIST

| # | Step | Time required by | Done | Notes |
| 1 | BSI / PPE | T+0:30 | ☐ | |
| 2 | Scene safety stated | T+0:30 | ☐ | |
| 3 | Approach + initial general impression | T+1:00 | ☐ | |
| 4 | LOC assessment (AVPU) | T+1:00 | ☐ | |
| 5 | Airway assessment + opens if compromised | T+1:30 | ☐ | |
| 6 | Breathing assessment + supports if compromised | T+2:00 | ☐ | |
| 7 | Circulation assessment + treats major bleeding if any | T+2:00 | ☐ | |
| 8 | Decision: transport priority | T+2:30 | ☐ | |
| 9 | Baseline vitals obtained | T+5:00 | ☐ | |
| 10 | SAMPLE history obtained | T+6:00 | ☐ | |
| 11 | Focused exam to chief complaint | T+7:00 | ☐ | |
| 12 | Treatment per protocol initiated | as appropriate | ☐ | |
| 13 | Reassessment of vitals + interventions | T+9:00 | ☐ | |
| 14 | Disposition decision (transport mode + destination) | T+10:00 | ☐ | |
| ... | (additional skill-specific steps) | | ☐ | |

Total possible: __/35    Step-score: __/35

>>> CRITICAL CRITERIA AUDIT

| Critical criterion | Met | Evidence (timestamp + observed action) |
| 1 | ☐ | [...] |
| 2 | ☐ | [...] |
| 3 | ☐ | [...] |
| 4 | ☐ | [...] |
| 5 | ☐ | [...] |

ANY ONE missed = AUTOMATIC FAIL regardless of step-score.

>>> DEBRIEF FRAMEWORK

What went well (specific behaviors with timestamps):
  • [...]

Critical criteria status:
  ☐ All met → eligible for pass
  ☐ One or more missed → automatic fail; specifically: [...]

One thing to improve (single actionable item):
  [...]

Re-test eligibility (per program policy):
  [...]

>>> POST-SCENARIO RATIONALE BLOCK (for examiner reference)

The hidden mechanism was [...]. Critical criterion #[X] is the highest-leverage flag because [reasoning]. Common candidate failure mode at this station is [...].
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `cert_level_being_tested` | Scope of allowable interventions changes |
| `skill_station_type` | Drives skill-sheet items and critical criteria |
| `scenario_complexity` | Single-skill vs integrated multi-skill |
| `time_limit_minutes` | NREMT-station-specific (10–15 medical/trauma; 5–8 isolated) |
| `failure_pathway_engineered` | Toggles whether scenario has critical-criterion fail trap |
| `distractor_count` | 2–3 typical; more raises difficulty |
| `vitals_branch` | Static vs dynamic vital trajectory |
| `examiner_script_detail_level` | Adjusts how much examiner discretion is needed |
| `population_overlay` | Pediatric scenarios add weight-based dosing fail traps |
| `mass_casualty_overlay` | Adds START triage critical criteria |

## Verification Checklist

- [ ] Candidate-facing dispatch is realistic and contains at most ONE distractor.
- [ ] Examiner script includes verbatim patient responses to OPQRST and SAMPLE in full.
- [ ] Vital trajectory has at least 2 columns (correct vs incorrect) and 5 time points.
- [ ] Branch triggers are explicit (intervention → response within time window).
- [ ] Planted distractors are *labeled* and have *resolutions* documented.
- [ ] Critical criteria are 5–8 items (NREMT-typical), pass/fail, with automatic-fail consequence stated.
- [ ] Step-completion checklist has 15–35 items with time stamps for time-sensitive steps.
- [ ] Critical-criteria audit table has evidence column with timestamp.
- [ ] Debrief has only ONE thing-to-improve.
- [ ] Post-scenario rationale block exists for examiner training / inter-rater calibration.
- [ ] Scope: no actions in checklist exceed `cert_level_being_tested`.
- [ ] No invented NREMT criteria; standard skill-sheet conventions used.

## Worked Example (compact)

**Input:** cert_level_being_tested = `paramedic`, skill_station_type = `dynamic-cardiology`, scenario_complexity = `dynamic-with-deterioration`, time_limit_minutes = 15, failure_pathway_engineered = true, distractor_count = 2, vitals_branch = `dynamic-both-directions`, examiner_script_detail_level = `full-script-with-quoted-patient-responses`.

**Output (excerpt):**

```
>>> CANDIDATE-FACING DISPATCH (T=0:00)

"Med-3, respond Code 3 to 1240 Oak Lane — 58yo male, chest pain, conscious and breathing, family on scene. PD not requested."

>>> EXAMINER PRE-BRIEF

Hidden mechanism: Inferior STEMI (RCA occlusion) — will progress to bradycardia + heart block + RV infarct hypotension if not preload-managed.
Expected disposition: PCI-capable cath lab within 90 min FMC-to-balloon; pre-notify; ground transport adequate (15 min away).
Critical criteria:
  1. BSI / scene safety stated.
  2. 12-lead EKG obtained within 10 min of patient contact.
  3. ASA administered (no contraindication present in this scenario) — chewed.
  4. Recognizes inferior STEMI (II, III, aVF + reciprocal in I, aVL).
  5. Does NOT give nitroglycerin without first checking for RV involvement (right-sided EKG / V4R) AND blood pressure ≥ 100 systolic. Inferior MI with RV involvement is preload-dependent — nitro can cause profound hypotension.
  6. Notifies receiving cath lab en route.
  7. Transports to PCI-capable facility (NOT nearest ED).

>>> EXAMINER SCRIPT — PATIENT RESPONSES

Chief complaint: "I've got this crushing pressure in my chest. Started about 45 minutes ago. I was just sitting in my chair watching TV."
OPQRST:
  Onset: "Sudden, while I was sitting still."
  Provocation: "Nothing makes it better. It got worse when I tried to walk to the bathroom."
  Quality: "Pressure. Like an elephant on my chest."
  Region/radiation: "Right here in the middle. Goes up into my jaw and into my left arm a little."
  Severity: "Like an 8 out of 10."
  Time: "45 minutes."
SAMPLE:
  Symptoms: "Sweaty. Nauseated. Felt like I was going to throw up."
  Allergies: "I'm allergic to sulfa drugs." [DISTRACTOR — examine relevance: ASA is salicylate, not sulfa; nitro and morphine are not sulfa. No actual contraindication.]
  Medications: "Lisinopril 20 mg, atorvastatin 40 mg, aspirin 81 mg daily, sildenafil 50 mg as needed for ED — took one this morning at 9 AM." [CRITICAL DISTRACTOR — sildenafil within 24h is an ABSOLUTE contraindication to nitroglycerin.]
  Past hx: "High blood pressure, high cholesterol. No prior heart attack."
  Last meal: "Coffee around 11 AM, light lunch around 1."
  Events: "I was just sitting watching TV when it started."

Patient appearance: 58M, diaphoretic, appears in distress, sitting upright. Denies SOB at rest.

>>> VITAL TRAJECTORY

| Time | Correct treatment (no nitro given, ASA given, transport to PCI) | Wrong treatment (nitro given despite sildenafil OR despite RV involvement) |
| 0:00 | BP 134/82, HR 58, RR 18, SpO2 96% RA | same |
| 3:00 | (after ASA, IV access, O2 if SpO2 < 94) BP 128/80, HR 56 | (after nitro) BP 78/40, HR 48, diaphoretic, dizzy |
| 5:00 | BP 124/76, HR 54 (mild bradycardia from RCA), pt comfortable | BP 70/30, HR 42, near-syncope, pt vomiting |
| 8:00 | BP 122/74, HR 54, transport en route | (if unrecognized) BP 60/palp, HR 38 — junctional rhythm, candidate must give fluids and atropine |
| 12:00 | At hospital, transferring care | Critically unstable, may require pacing |

Branch triggers:
  • Nitro given → hypotension within 2 min if sildenafil OR RV involvement
  • Right-sided EKG performed and V4R shows ST elevation → RV infarct confirmed; nitro contraindicated regardless of BP
  • Atropine given for HR < 50 with hypotension → some HR response; fluid bolus more effective for RV preload

>>> PLANTED DISTRACTORS

Distractor 1: "Allergic to sulfa"
  Resolution: ASA is salicylate, not sulfa. Candidate should administer ASA without hesitation. If candidate withholds ASA, that is a step-completion deduction (not a critical-criteria fail unless ASA is later withheld throughout).
  Score impact: -1 step if ASA delayed > 5 min on incorrect concern.

Distractor 2: "Sildenafil 50 mg this morning at 9 AM"
  Resolution: Sildenafil within 24 hr is an absolute contraindication to nitroglycerin. Candidate must elicit this on med history AND not administer nitro.
  Score impact: AUTOMATIC FAIL if nitro administered (critical criterion #5).

>>> STEP-COMPLETION CHECKLIST (paramedic, dynamic cardiology)

| # | Step | Time required by | Done |
| 1 | BSI / PPE | T+0:30 | ☐ |
| 2 | Scene safety stated | T+0:30 | ☐ |
| 3 | Initial impression / general appearance | T+1:00 | ☐ |
| 4 | LOC assessment AVPU | T+1:00 | ☐ |
| 5 | Airway / Breathing / Circulation primary survey | T+2:00 | ☐ |
| 6 | Position of comfort (typically Fowler's for chest pain) | T+2:00 | ☐ |
| 7 | O2 if SpO2 < 94% (NOT routine for SpO2 ≥ 94 per current AHA guidance) | as indicated | ☐ |
| 8 | Cardiac monitor + 4-lead | T+3:00 | ☐ |
| 9 | 12-lead EKG | T+8:00 | ☐ ← critical criterion #2 |
| 10 | EKG interpretation: identifies inferior STEMI | T+9:00 | ☐ ← critical criterion #4 |
| 11 | Right-sided EKG (V4R minimum) for inferior STEMI | T+10:00 | ☐ |
| 12 | IV access (large bore preferred) | T+5:00 | ☐ |
| 13 | OPQRST + SAMPLE complete (including sildenafil discovery) | T+6:00 | ☐ |
| 14 | ASA 324 mg chewed (or confirms taken in last 24 hr) | T+6:00 | ☐ ← critical criterion #3 |
| 15 | Nitroglycerin: WITHHELD given sildenafil (or absent RV-involvement check) | always | ☐ ← critical criterion #5 |
| 16 | Fentanyl/morphine for pain if BP allows and per protocol | as appropriate | ☐ |
| 17 | Pre-notify cath lab / receiving | T+10:00 | ☐ ← critical criterion #6 |
| 18 | Transport mode/destination = PCI-capable | T+10:00 | ☐ ← critical criterion #7 |
| 19 | Reassessment vitals q5 min | T+10:00 + ongoing | ☐ |
| 20 | Reassessment after each intervention | as appropriate | ☐ |
| 21 | Hand-off radio report to receiving | T+13:00 | ☐ |

>>> CRITICAL CRITERIA AUDIT

| # | Met | Evidence |
| 1 BSI/scene safety | ☐ | [...] |
| 2 12-lead within 10 min | ☐ | [...] |
| 3 ASA given | ☐ | [...] |
| 4 STEMI recognized | ☐ | [...] |
| 5 Nitro WITHHELD | ☐ | [...] |
| 6 Cath lab notified | ☐ | [...] |
| 7 PCI destination | ☐ | [...] |

ANY ONE missed = AUTOMATIC FAIL.

>>> POST-SCENARIO RATIONALE

The sildenafil distractor is the highest-leverage critical criterion at this station. Most candidates correctly identify the STEMI; the differentiator is whether they obtained a thorough medication history and recognized the absolute contraindication to nitro. Common failure mode: candidate gives nitro reflexively for chest pain because that's the muscle-memory pattern from training; consequence is iatrogenic hypotension. The right-sided EKG for inferior MI is a step-completion item rather than a critical fail because contemporary protocols vary on whether it is required vs recommended.
```
