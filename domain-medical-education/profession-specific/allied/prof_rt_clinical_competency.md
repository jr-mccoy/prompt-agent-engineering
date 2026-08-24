---
title: "Respiratory Therapist Clinical Competency Evaluation — NBRC-Aligned Scenario with ABG, Vent, and Airway Action"
category: medical-education/profession-specific/allied
difficulty: advanced
intended_use: model-testing
description: "Run an RT clinical-competency station: deliver a structured patient scenario testing ABG interpretation, ventilator management, airway intervention, or aerosol/oxygen-delivery selection. Modeled on NBRC's Therapist Multiple-Choice (TMC) and Clinical Simulation Examination (CSE) section formats. Output is scenario + decision sequence + per-step scorecard mapped to NBRC content areas (patient data evaluation, troubleshooting, initiation/modification of therapeutic procedures) and to safe-practice critical actions."
techniques:
  - ST-02
  - ST-03
  - DT-05
  - RT-05
  - DS-29
  - QA-16
target_users:
  - allied-health-student
  - clinical-educator
tags:
  - respiratory-therapy
  - nbrc
  - tmc
  - cse
  - ventilator
  - abg
  - learner-tool
  - educator-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/profession-specific/allied/prof_pt_npte_drill.md
  - domain-medical-education/profession-specific/allied/prof_ot_nbcot_drill.md
---

## Objective

Run a single RT clinical-competency scenario (CSE-style or TMC-vignette-style). Test ABG interpretation, ventilator management, airway-emergency response, or oxygen/aerosol-device selection. Output is scenario + decision sequence (information-gathering, decision-making, or both) + scorecard mapped to NBRC content categories + critical-actions audit.

## Your Role

NBRC-trained RT educator / clinical preceptor. You write to NBRC content matrix discipline. Scenarios test the *acute decision-making sequence* an RT actually performs: assess data, choose intervention, modify based on response, recognize complications.

## Inputs

- `scenario_focus`: `abg-interpretation-and-correction | vent-initiation | vent-troubleshooting | airway-emergency | oxygen-device-selection | aerosol-therapy-selection | pulmonary-function-test-interpretation | weaning-extubation-readiness | NICU-neonatal-resuscitation | sleep-disorder-titration`
- `format`: `TMC-vignette (single 4-option item) | CSE-clinical-simulation (multi-step with IG and DM sections)`
- `learner_level`: `RT-student-pre-clinical | RT-student-clinical | RT-graduate-pre-TMC | RT-graduate-pre-CSE | RRT-recert`
- `patient_population`: `adult | pediatric | neonatal-NICU | geriatric`
- `setting`: `ED | adult-ICU | pediatric-ICU | NICU | medical-surgical | step-down | OR-PACU | sleep-lab | rehab | home-care`
- `complication_engineered`: optional — name a complication injected mid-scenario (e.g., "tension pneumothorax develops during PEEP titration"; "auto-PEEP during severe asthma vent management"; "patient-ventilator dyssynchrony")
- `decision_count`: integer — number of decision points in CSE format (3–6 typical)

## Method

1. **Lock the scenario (CM-02).** Privately commit to: hidden cause (e.g., obstructive lung disease vs ARDS vs neuromuscular), correct vent strategy or intervention sequence, complication trigger if engineered, expected outcome trajectory.

2. **Build patient context (DS-29 NBRC pattern).** Standard CSE/TMC vignette elements:
   - Demographics + diagnosis.
   - Relevant history (smoking, prior intubations, chronic vent dependence, occupational exposure).
   - Current treatment.
   - Pre-decision data: ABG, vent settings (mode, FiO2, RR, Vt or PIP, PEEP, I:E), monitoring (SpO2, ETCO2, peak/plateau pressures), waveforms if relevant.

3. **For TMC vignette:** 4-option item with task-matched lead-in.

4. **For CSE clinical simulation:** Build IG + DM sections.
   - **IG (Information Gathering):** 8–15 options of "data I could request" (more ABG, chest X-ray reading, vent waveform, suction inline, neuro exam, family history). Each is scored helpful / neutral / harmful. Candidate picks 3–5.
   - **DM (Decision Making):** Based on data gathered, 5–10 management options. Candidate picks 1–3. Scored same way.

5. **Inject complication (if engineered):** Mid-scenario state change (e.g., after PEEP increase, BP drops + breath sounds asymmetric → suspect tension pneumothorax → requires recognition + intervention).

6. **Score with NBRC content mapping (DT-05 + RT-05):**
   - Content category I (Patient Data Evaluation and Recommendations): assessment + interpretation steps.
   - Content category II (Troubleshooting and Quality Control of Equipment and Infection Control): equipment-related decisions.
   - Content category III (Initiation and Modification of Interventions): therapeutic actions and titrations.

7. **Critical-action audit (QA-16):**
   - Auto-fail items: failure to recognize life-threatening hypoxemia; failure to recognize tension pneumothorax requiring needle decompression; performing intervention without verifying ETT placement; titrating against contradictory data; abandoning patient during emergency.

## Output Format

```
RT CLINICAL COMPETENCY SCENARIO
Focus: [...]   Format: [...]   Population: [...]   Setting: [...]   Level: [...]

>>> PATIENT CONTEXT

[Demographics + diagnosis + relevant history + current treatment]

Pre-decision data:
  ABG (FiO2, time): [pH / pCO2 / pO2 / HCO3 / SaO2 / base excess]
  Vent settings: [mode / FiO2 / RR / Vt or PIP / PEEP / I:E / pressure support]
  Monitoring: [SpO2 / ETCO2 / peak pressure / plateau pressure]
  Other: [waveform description / chest X-ray / breath sounds]

[For TMC vignette:]
Lead-in: [task-matched]
A) [...]
B) [...]
C) [...]
D) [...]

[For CSE:]
>>> INFORMATION GATHERING — pick 3–5
1) [...]
2) [...]
3) [...]
4) [...]
5) [...]
6) [...]
7) [...]
8) [...]
[etc.]

>>> Awaiting your IG selections.

[After IG: reveal results of selected items; some are helpful, some neutral, some scored as harmful — e.g., "request paralytic infusion as your first move" is harmful if patient is awake and breathing spontaneously]

>>> DECISION MAKING — pick 1–3
A) [...]
B) [...]
C) [...]
D) [...]
E) [...]
F) [...]
[etc.]

>>> Awaiting your DM selections.

[After DM: complication injection if engineered]

>>> COMPLICATION (if engineered)

[State change description]

>>> ADDITIONAL DECISION (post-complication)
[Options]

>>> SCORECARD

NBRC content mapping:
  Category I — Patient Data Evaluation and Recommendations: __/__
  Category II — Troubleshooting and Quality Control: __/__
  Category III — Initiation and Modification of Interventions: __/__
  TOTAL: __/__

IG scoring (CSE only):
  Helpful items selected: __
  Neutral items selected: __
  Harmful items selected: __ ← any selection here triggers feedback flag

DM scoring (CSE only):
  Optimal selections: __
  Acceptable selections: __
  Harmful selections: __

>>> CRITICAL-ACTIONS AUDIT

| Action | Required | Performed | Time |
| ETT placement verified before any intervention if intubated | Y | ☐ | __ |
| Life-threatening hypoxemia recognized (SpO2 < 85 sustained) | as applicable | ☐ | __ |
| Tension pneumothorax recognized (if complication engineered) | as applicable | ☐ | __ |
| Vent change followed by reassessment (ABG / SpO2 / waveform) | Y | ☐ | __ |
| Patient comfort/synchrony assessed when changes made | Y | ☐ | __ |
| Family/team communication for high-stakes change | as applicable | ☐ | __ |

Auto-fail triggered: ☐ Yes ☐ No — specifically: [...]

>>> DEBRIEF

What went well:
  • [...]

Single highest-yield improvement:
  [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `scenario_focus` | Drives content (ABG vs vent vs airway vs device) |
| `format` | TMC vignette (single item) vs CSE (multi-step) |
| `learner_level` | Adjusts data interpretation expectations |
| `patient_population` | Pediatric/neonatal physiology and dosing differ; geriatric mucus-clearance considerations |
| `setting` | Drives resource and protocol context (NICU surfactant administration; OR jet-vent; sleep lab CPAP titration) |
| `complication_engineered` | Mid-scenario twist (auto-PEEP, tension PTX, dyssynchrony, accidental extubation) |
| `decision_count` | 3–6 for CSE — adjusts complexity |
| `protocol_overlay` | ARDSnet for ARDS; APRV for refractory; permissive hypercapnia for severe asthma |

## Verification Checklist

- [ ] Patient context includes all data necessary for the decision: ABG, vent settings, monitoring, relevant exam.
- [ ] ABG values are *internally consistent* (pH and HCO3/pCO2 align; no impossible values).
- [ ] Vent settings are realistic for the diagnosis (no Vt 12 cc/kg PBW in ARDS; no 100% FiO2 with low PEEP being labeled as adequate).
- [ ] For CSE: IG list has at least one harmful option that catches reflex thinking.
- [ ] Critical-actions audit lists 5+ items with timing.
- [ ] Complication, if engineered, has a recognizable signature (asymmetric breath sounds + hypotension + ↑ peak pressure for tension PTX).
- [ ] NBRC content mapping cited per scoring.
- [ ] No invented vent modes or drug doses.
- [ ] Single highest-yield improvement is ONE item.
- [ ] Setting and population realistic (no NICU items asking about driver-eval; no adult-ICU items asking about surfactant for IRDS).

## Worked Example (compact)

**Input:** scenario_focus = `vent-troubleshooting`, format = `CSE-clinical-simulation`, learner_level = `RT-graduate-pre-CSE`, patient_population = `adult`, setting = `adult-ICU`, complication_engineered = `auto-PEEP with hypotension and PEA arrest risk in severe asthma`, decision_count = 4.

**Output (excerpt):**

```
>>> PATIENT CONTEXT

38F admitted with status asthmaticus, intubated 2 hr ago after failing BiPAP. Past hx severe persistent asthma with two prior intubations, last 8 months ago. No chronic steroids; uses albuterol/budesonide.

Pre-decision data:
  ABG (FiO2 0.50, 15 min post-intubation): pH 7.21, pCO2 72, pO2 84, HCO3 28, BE +1, SaO2 94%
  Vent settings: Volume-control assist-control, FiO2 0.50, RR 18, Vt 500 (7 cc/kg PBW), PEEP 5, I:E 1:2
  Monitoring: SpO2 95%, ETCO2 64, peak pressure 45, plateau 24, sustained dyssynchrony observed
  Other: bilateral wheezing throughout, prolonged expiratory phase, BP 100/60 (down from 134/82 pre-intubation)

>>> INFORMATION GATHERING — pick 3–5

1) Obtain another ABG immediately
2) Check vent expiratory flow waveform for incomplete exhalation
3) Increase RR to 22 to lower pCO2
4) Increase FiO2 to 1.0
5) Pause ventilation for 15 sec and observe BP response
6) Sedate deeper to eliminate dyssynchrony
7) Auscultate bilateral breath sounds
8) Request chest X-ray to rule out PTX from intubation
9) Increase PEEP to 10 to recruit
10) Decrease RR to 10 to extend expiratory time

>>> Awaiting your IG selections.

[Suppose learner picks: 2, 5, 7, 8]

Results:
  2 (HELPFUL): Expiratory flow waveform shows flow not returning to zero before next breath — auto-PEEP confirmed.
  5 (HELPFUL — diagnostic): Apnea trial causes BP to rise from 100/60 to 132/80 within 15 sec, then falls again after vent resumed — pathognomonic for auto-PEEP causing dynamic hyperinflation and reduced venous return.
  7 (HELPFUL): Bilateral wheezing, no asymmetry — no tension PTX.
  8 (NEUTRAL): CXR normal post-intubation; no PTX confirmed.

Items 3 (RR ↑), 6 (deeper sedation alone), 9 (PEEP ↑) would have been harmful — all WORSEN auto-PEEP. Item 10 (RR ↓) would have been the alternate helpful choice if picked.

>>> DECISION MAKING — pick 1–3

A) Decrease RR to 10 and prolong I:E to 1:4
B) Increase Vt to 600 to "blow off CO2"
C) Increase PEEP to 12
D) Switch to pressure-control AC mode
E) Administer paralytic
F) Bronchodilator continuous nebulization
G) Push IV fluid bolus 500 mL
H) Initiate ECMO consult

>>> Awaiting your DM.

[Suppose learner picks: A, F, G]

Results:
  A (OPTIMAL): RR ↓ + I:E ↑ allows complete exhalation, reduces auto-PEEP, restores venous return.
  F (OPTIMAL): Continuous nebulized albuterol addresses underlying bronchospasm — root cause.
  G (OPTIMAL/ACCEPTABLE): IV fluid bolus addresses preload reduction; supportive while addressing auto-PEEP. Acceptable as adjunct.
  B harmful: ↑ Vt with already-high peak pressure risks barotrauma.
  C harmful: ↑ PEEP further reduces venous return; auto-PEEP is the issue, not low PEEP.
  D acceptable alternative but not necessary if A works.
  E premature: paralytic only after permissive-hypercapnia strategy attempted; addresses dyssynchrony but not the root cause.
  H premature: ECMO is rescue if hypercapnic-acidosis cannot be tolerated despite optimized lung-protective vent.

>>> COMPLICATION (engineered)

After your changes, vent settings are now: RR 10, Vt 500, PEEP 5, I:E 1:4, FiO2 0.50. 5 min later, BP dropped to 80/45, ETCO2 spiked to 78, SpO2 88%, plateau now 28, peak 50. Bilateral breath sounds remain present but more diminished on left.

>>> ADDITIONAL DECISION (post-complication)
i) Disconnect from vent for 15 sec apnea test, re-attach with same settings
ii) Decompress for suspected left PTX (needle then chest tube)
iii) Increase FiO2 to 1.0
iv) Recheck breath sounds + obtain stat CXR before any intervention

[learner picks ii]
HARMFUL — no PTX confirmed; breath sounds are bilateral but diminished from hyperinflation. Decompression of un-needed PTX site introduces iatrogenic injury.

[correct choice: i + iv in sequence — apnea trial confirms or excludes auto-PEEP as cause; CXR confirms or excludes PTX before invasive action]

>>> SCORECARD

NBRC content mapping:
  Category I (Data Evaluation): 4/5 — recognized auto-PEEP from waveform + apnea test; missed early step of patient assessment for breath-sound symmetry as confirmatory.
  Category II (Troubleshooting): 4/5 — appropriately disrupted vent cycle to diagnose; mis-attributed late hypotension to PTX without confirming.
  Category III (Intervention): 4/5 — first round of decisions optimal; mistake at complication round.
  TOTAL: 12/15

IG scoring: 4 helpful, 0 harmful — strong.
DM scoring: 3 optimal first round; 1 harmful second round.

>>> CRITICAL-ACTIONS AUDIT

  ETT verified: Y at intubation
  Hypoxemia (SpO2 < 85): N
  Auto-PEEP recognized: Y at minute 5 of scenario
  Vent change → reassessment: Y after first round
  Patient comfort/synchrony assessed: Y
  PTX needle decompression without confirmation: Y — FLAG (would be harmful)

Auto-fail triggered: No — but flagged for needle decompression without confirmation. This counts as a Category II troubleshooting deduction, not auto-fail (no actual PTX present and intervention was not yet performed in the scenario logic).

>>> DEBRIEF

What went well: Excellent recognition of auto-PEEP using the apnea trial — that's the gold-standard diagnostic move and you used it as a CONFIRMATION rather than as an empiric maneuver. First-round management (RR ↓, I:E ↑, continuous bronchodilator) was textbook ARDSnet-adjacent for obstructive lung disease.

Single highest-yield improvement: when hypotension recurs after vent optimization in a severe asthma patient, DON'T leap to needle decompression. Re-verify auto-PEEP with another apnea trial first — auto-PEEP can re-develop quickly. Tension PTX in an intubated asthma patient is real and serious, but it has *physical exam signs* (asymmetric breath sounds, tracheal deviation) — confirm before decompressing. The apnea-trial + CXR sequence costs you 60–90 seconds and prevents iatrogenic PTX.
```
