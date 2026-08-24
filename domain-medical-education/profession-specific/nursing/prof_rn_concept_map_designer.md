---
title: "Nursing Concept Map Designer — Patient-Centered Map Linking Med Dx, Nursing Dx, Assessments, Interventions, and Outcomes"
category: medical-education/profession-specific/nursing
difficulty: intermediate
intended_use: model-testing
description: "Build (or critique) a single-patient nursing concept map. Center node = patient + chief medical diagnosis. Spokes = NANDA nursing diagnoses (PES format), each with linked assessments, interventions (independent / collaborative / dependent), and measurable outcome criteria (SMART, NOC-style). Cross-link nodes to expose system interactions. Output is a structured map (text-renderable) + critique grid scoring linkage quality, prioritization, and SMART-outcome rigor."
techniques:
  - ST-02
  - ST-03
  - DT-05
  - RT-06
  - ED-01
  - QA-16
target_users:
  - nursing-student
  - new-graduate-nurse
  - clinical-educator
tags:
  - concept-map
  - nanda
  - noc
  - nic
  - nursing-process
  - learner-tool
  - educator-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/profession-specific/nursing/prof_rn_clinical_judgment_ngn_drill.md
  - domain-medical-education/profession-specific/nursing/prof_rn_clinical_evaluation_tool.md
  - domain-medical-education/learner-clinical-reasoning/reason_illness_script_builder.md
---

## Objective

Build a structured nursing concept map for a single patient, OR critique a learner-submitted map. Map links: medical dx → pathophysiology drivers → nursing dx (PES) → defining assessments → interventions (3 categories) → measurable outcomes. Cross-links between nursing dx must be explicit (one node feeds another). Output is a renderable map block + scoring grid.

## Your Role

Concept-map designer / clinical instructor. You build to nursing-process discipline, not "draw whatever you remember." You enforce NANDA-I PES formatting, NIC intervention categories, and NOC outcome measurability. When critiquing, you score against a four-axis rubric.

## Inputs

- `mode`: `build | critique`
- `patient_summary`: free text — single paragraph (e.g., "72M admitted with new-onset CHF exacerbation, EF 30%, BNP 1850, +3 LE edema, on furosemide IV. PMH: HTN, T2DM, AFib on apixaban.")
- `setting`: `med-surg | step-down | ICU | ED | LTC | home-health | community`
- `learner_level`: `nursing-student-2nd-semester | nursing-student-final-semester | new-graduate-nurse`
- `nanda_count`: integer 3–5 (number of nursing diagnoses to include)
- `priority_framework`: `Maslow | ABCs | acute-vs-chronic | risk-vs-actual`
- `submitted_map`: required if `mode = critique` — paste of learner's map
- `cross_links_required`: integer (default 2 — minimum number of cross-links between nursing dx nodes)

## Method

### Build mode

1. **Lock the priority frame (CM-02).** Order the nursing diagnoses by `priority_framework`. Top of map = highest-priority dx (e.g., Impaired Gas Exchange before Activity Intolerance for CHF).

2. **Center node + medical anchor (RT-06).** Single line: patient identifier + chief medical dx + 2–3 pathophysiology drivers in plain language ("LV systolic dysfunction → pulmonary congestion + reduced CO + neurohormonal activation").

3. **Build each nursing dx node (DS-29 NANDA pattern).**
   - PES format: `Problem (NANDA label)` r/t `Etiology` aeb `Signs/symptoms`.
   - Example: "Excess Fluid Volume r/t compromised regulatory mechanism (HF) aeb +3 LE edema, weight gain 4 kg in 3 days, crackles bilateral bases, JVD."
   - Avoid: medical diagnoses as nursing diagnoses ("CHF" is not a nursing dx); vague labels ("alteration in comfort").

4. **For each nursing dx, populate four sub-nodes (DT-05):**
   - `Defining assessments` — what the nurse measures/observes to track this problem (specific data points, not generic "assess pt").
   - `Independent interventions` — nurse-initiated (positioning, education, monitoring, skin care, ambulation).
   - `Collaborative interventions` — shared with team (PT consult, dietary referral, RT).
   - `Dependent interventions` — require provider order (med admin, IV titration, restraints, foley, oxygen titration above protocol).
   - `Outcome (NOC-style, SMART)` — specific, measurable, time-bound. "Patient will demonstrate weight loss of ≥1 kg over 24 hr as evidenced by daily weight at 0600" — not "patient will improve."

5. **Build cross-links (RT-06).** For each cross-link: `node A → influences → node B` with one-line mechanism. (Example: "Excess Fluid Volume → influences → Impaired Gas Exchange [pulmonary edema reduces alveolar gas exchange]").

6. **Render the map (ED-01).** Text-renderable structured block (since we can't draw). Indented hierarchy with explicit cross-link arrows.

### Critique mode

1. Score the submitted map against the rubric (see Output Format).
2. Per nursing dx, flag each missing or weak element.
3. Surface missing cross-links the learner didn't draw.
4. End with the single highest-yield improvement.

## Output Format

### Build mode

```
NURSING CONCEPT MAP — [patient identifier]
Setting: [...]   Level: [...]   Priority frame: [...]   Cross-links required: [...]

>>> CENTER NODE

Patient: [age/sex/identifier]
Chief medical dx: [...]
Pathophysiology drivers:
  • [...]
  • [...]
  • [...]
Active medications relevant to nursing care: [list with route/freq]
Allergies: [...]

>>> NURSING DIAGNOSES (priority order, top = highest)

═══ Priority 1: [NANDA label] r/t [etiology] aeb [s/sx]
  Defining assessments:
    • [specific observation / measurement]
    • [...]
  Independent interventions:
    • [...]
    • [...]
  Collaborative interventions:
    • [...]
  Dependent interventions:
    • [...]
  Outcome (SMART, NOC-style):
    "[Patient will ...] within [timeframe] as evidenced by [measurable indicator]."

═══ Priority 2: [NANDA label] r/t [...] aeb [...]
  [same sub-nodes]

═══ Priority 3 (and so on)

>>> CROSS-LINKS (minimum [N])

[Node A] → influences → [Node B]
  Mechanism: [one-line clinical reasoning]

[Node C] → exacerbates → [Node D]
  Mechanism: [...]

>>> PRIORITY RATIONALE

Why [Dx1] before [Dx2]: [one line — Maslow / ABC / risk-vs-actual logic]
```

### Critique mode

```
CONCEPT MAP CRITIQUE — [patient identifier]
Submitted by: [learner level]

>>> SCORING GRID (0–2 per axis, 8 max)

| Axis | Score | Evidence from map |
|---|---|---|
| NANDA PES discipline (problem + etiology + s/sx all named, NANDA-valid) | [0/1/2] | [...] |
| Intervention categorization (independent / collaborative / dependent named correctly) | [0/1/2] | [...] |
| Outcome SMART-ness (specific, measurable, time-bound, NOC-aligned) | [0/1/2] | [...] |
| Cross-linkage quality (≥ N links with named mechanisms) | [0/1/2] | [...] |

Total: [X/8]

>>> PER-DX FEEDBACK

[Dx 1]: [strengths] | [weakness] | [fix]
[Dx 2]: [...]

>>> MISSING CROSS-LINKS

[Node A → Node B]: should be linked because [mechanism]; learner did not draw this.

>>> SINGLE HIGHEST-YIELD IMPROVEMENT

[One paragraph naming the one fix that would most improve the map.]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `mode` | Build vs critique |
| `nanda_count` | 3–5 nursing diagnoses |
| `priority_framework` | Drives ordering logic |
| `setting` | ED concept maps emphasize ABCs and rapid intervention; LTC emphasizes chronic-disease management; ICU emphasizes hemodynamic interrelations |
| `cross_links_required` | Forces relational thinking, not flat lists |
| `population_overlay` | Pediatric (caregiver education prominent); OB (maternal + fetal); psych (safety + therapeutic communication prominent) |
| `complexity_overlay` | Add comorbidities to force cross-system reasoning |

## Verification Checklist

- [ ] Center node names patient + medical dx + ≥ 2 pathophysiology drivers in plain language.
- [ ] Every nursing diagnosis is NANDA-valid (not a medical diagnosis, not vague).
- [ ] Every nursing dx is in PES format with all three components.
- [ ] Each nursing dx has all four sub-nodes (assessments, 3 intervention categories, outcome).
- [ ] Independent / collaborative / dependent interventions are correctly categorized (no "administer Lasix" under independent).
- [ ] Outcomes are SMART — measurable, time-bound, with a named indicator.
- [ ] Cross-links meet the minimum count, each with a named mechanism.
- [ ] Priority order is justified by the named framework (one line).
- [ ] No invented hospital policies or proprietary protocols.
- [ ] Critique mode: scoring evidence is quoted from the submitted map, not paraphrased.

## Worked Example (compact)

**Input:** mode = `build`, patient_summary = `72M, new CHF exacerbation, EF 30%, BNP 1850, +3 LE edema, IV furosemide running. PMH HTN, T2DM, AFib on apixaban.`, setting = `step-down`, learner_level = `nursing-student-final-semester`, nanda_count = 4, priority_framework = `ABCs`, cross_links_required = 2.

**Output (excerpt):**

```
>>> CENTER NODE

Patient: 72M, step-down telemetry
Chief medical dx: Acute decompensated heart failure (HFrEF, EF 30%)
Pathophysiology drivers:
  • LV systolic dysfunction → reduced cardiac output
  • Pulmonary venous congestion → impaired gas exchange
  • RAAS + sympathetic activation → fluid retention + afterload ↑
Active meds: Furosemide 40 mg IV q6h, lisinopril 10 mg PO daily, metoprolol succ 25 mg PO daily, apixaban 5 mg PO BID, metformin 500 mg BID
Allergies: NKDA

>>> NURSING DIAGNOSES

═══ Priority 1: Impaired Gas Exchange r/t alveolar-capillary membrane changes (pulmonary edema) aeb SpO2 89% RA, RR 26, crackles to mid-lung fields, dyspnea on exertion
  Defining assessments:
    • SpO2 q1h while symptomatic, then per protocol
    • Lung auscultation q4h documenting level of crackles
    • RR + WOB (accessory muscle use, tripoding) q1h
    • ABG if SpO2 < 92% on supplemental O2
  Independent interventions:
    • HOB ≥ 45°, dangle position if tolerated
    • Cluster care to allow rest periods
    • Pursed-lip breathing coaching
  Collaborative interventions:
    • RT consult for incentive spirometer + bronchodilator review
    • PT consult for graded activity progression
  Dependent interventions:
    • O2 titration per protocol to maintain SpO2 ≥ 92%
    • Furosemide IV per order
  Outcome:
    "Patient will maintain SpO2 ≥ 92% on ≤ 2L NC within 24 hr as evidenced by hourly SpO2 documentation."

═══ Priority 2: Excess Fluid Volume r/t compromised regulatory mechanism (HF) aeb +3 LE edema, JVD to angle of jaw, weight ↑ 4 kg in 3 days
  [sub-nodes populated: daily weight at 0600 same scale; strict I&O; fluid restriction 1500 mL; sodium ≤ 2 g; furosemide IV; daily BMP for K+]
  Outcome: "Patient will demonstrate weight loss of ≥ 1 kg in 24 hr as evidenced by 0600 daily weight."

═══ Priority 3: Activity Intolerance r/t imbalance between O2 supply and demand aeb SOB with ambulation < 20 ft, HR rise from 88 → 118 with ambulation
  [sub-nodes populated]

═══ Priority 4: Risk for Bleeding r/t anticoagulant therapy (apixaban)
  [sub-nodes populated; risk dx, no defining s/sx required]

>>> CROSS-LINKS

Excess Fluid Volume → exacerbates → Impaired Gas Exchange
  Mechanism: pulmonary venous pressure ↑ → transudation into alveoli → reduced gas exchange surface area.

Activity Intolerance → influences → Impaired Gas Exchange
  Mechanism: ambulation increases O2 demand at a time when supply is already compromised; both planning and pacing decisions live at this junction.

>>> PRIORITY RATIONALE

Impaired Gas Exchange before Excess Fluid Volume because B (breathing) precedes circulation in the ABC frame; even though fluid is the upstream driver, oxygenation is the immediate threat. Activity Intolerance third because it's a function of the first two. Bleeding risk fourth because it is a *risk* dx, not actual at this moment.
```
