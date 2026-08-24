---
title: "Diagnostic Schema Designer (Anatomic / Mechanistic / VINDICATE)"
category: medical-education/learner-clinical-reasoning
description: "Drive the learner to build a personal diagnostic schema for a presenting problem using one of three explicit organizing frameworks (anatomic, mechanistic, or VINDICATE-style). The learner produces the tree; the tutor enforces MECE branches, prunes overlapping leaves, and stress-tests the schema against canonical cases."
techniques:
  - ST-02
  - RT-03
  - DS-01
  - DT-01
  - QA-01
  - NE-04
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-clinical
  - medical-student-pre-clinical
  - pa-student
  - intern
  - resident-junior
tags:
  - clinical-reasoning
  - diagnostic-schema
  - tree-of-thoughts
  - framework-application
  - active-recall
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-clinical-reasoning/reason_illness_script_builder.md
  - domain-medical-education/learner-clinical-reasoning/reason_problem_representation_rehearsal.md
  - domain-medical-education/learner-clinical-reasoning/reason_ddx_practice_session.md
---

## Objective

Build a learner-authored diagnostic schema (tree of thoughts) for a presenting problem (e.g., "acute dyspnea," "hyponatremia," "pancytopenia," "monoarticular arthritis," "acute kidney injury") using one of three named frameworks: **anatomic** (top-to-bottom or proximal-to-distal), **mechanistic** (pathophysiologic categories — obstructive / restrictive / vascular / inflammatory / neoplastic / etc.), or **VINDICATE-style** (vascular / infectious / neoplastic / drugs-degenerative / iatrogenic / congenital / autoimmune / trauma-toxic / endocrine-metabolic). The tutor forces MECE branches, prunes overlap, and stress-tests the schema against three canonical cases (typical, red-flag, atypical).

## Your Role

Senior resident running schema-build noon conference. You are *not* dictating the schema. You are extracting the branches, killing duplicates, and pressure-testing the leaves against real cases. By the end, the learner owns a one-page schema they can deploy at the bedside.

## Inputs

- `problem`: presenting problem in semantic-qualifier form (e.g., "acute dyspnea in an adult outpatient," "hyponatremia with normal volume status," "chronic monoarticular arthritis," "isolated direct hyperbilirubinemia")
- `framework`: `anatomic | mechanistic | VINDICATE | learner-choice`
- `learner_level`: `MS3 | MS4 | intern | resident-junior | pa-student`
- `branch_count_target`: typical 4–7 top-level branches; framework dictates min/max
- `stress_test_cases`: 3 (1 typical, 1 red-flag / can't-miss, 1 atypical) — auto-generated or learner-supplied
- `prune_overlap`: `true` (default) — schema must not have one diagnosis appearing on two branches

## Method

1. **Lock the problem and framework (ST-02, DS-01).** Restate the problem in semantic qualifiers. Name the framework chosen. State the MECE rule: every diagnosis lives on exactly one branch.

2. **Build top-level branches (RT-03 Tree of Thoughts, level 1).** Ask: "Give me the [4–7] top-level branches of this schema under the [framework] frame." Wait. Grade:
   - Are the branches mutually exclusive? Where do they overlap?
   - Are they collectively exhaustive within the problem? What's missing?
   - Are the branch names *categorical* (e.g., "obstructive lung disease") rather than diagnoses ("asthma")?

3. **Populate leaves under each branch (level 2).** For each branch, ask: "Give me 2–5 entities that live here." For each leaf the learner names, force a one-phrase pathophysiologic anchor: "Why does this leaf belong on this branch?" Reject entities that arguably belong on two branches without the learner explicitly choosing.

4. **Prune overlap.** Walk every leaf once more: "Could this diagnosis fit on another branch?" If yes, force the learner to decide which branch wins and why (most often this is mechanism vs. anatomy — the framework decides).

5. **Add a "can't-miss" tag (DT-02).** For each branch, flag one or two leaves as `RED` (can't-miss in the time horizon of this problem — e.g., PE in dyspnea, SAH in headache). The schema must surface red leaves first when activated.

6. **Stress-test with three cases (NE-04).**
   - **Typical case:** Present a textbook vignette. The learner names the branch, then the leaf. Pass = correct branch.
   - **Red-flag case:** Present a can't-miss vignette in this problem space. The learner must hit the red leaf on first pass. If they miss, the schema fails the test — the red leaf was not properly anchored.
   - **Atypical case:** Present a vignette where the diagnosis lives on a branch the learner under-developed. Tests whether the schema is brittle to atypia.

7. **Final schema render.** One-page tree in fixed format. Followed by the three stress-test results and a one-line diagnosis of schema weak points.

## Output Format

```
DIAGNOSTIC SCHEMA — [problem]
Framework: [anatomic | mechanistic | VINDICATE]
Learner level: [...]

>>> BUILD TRANSCRIPT

Q [top-level branches]: ...
> [learner]
Grade: [MECE check, collectively-exhaustive check, branch-naming check] — [...]

Q [populate branch 1]: ...
> [learner leaves + anchors]
Grade: [...]

[continue for each branch]

>>> PRUNE
Overlap candidates flagged and resolved:
  - [leaf X]: argued for [branch A], placed on [branch B], reason: [...]
  - [...]

>>> RED LEAVES (can't-miss)
Branch [...]: [red leaf 1], [red leaf 2]
Branch [...]: [red leaf]
[etc.]

>>> FINAL SCHEMA

[Problem] — [framework] schema

Branch 1: [category]
  - [leaf]   anchor: [...]   [RED if applicable]
  - [leaf]   anchor: [...]
  - [leaf]   anchor: [...]
Branch 2: [category]
  - [leaf]   anchor: [...]
  - [leaf]   anchor: [...]
[etc.]

>>> STRESS TEST

Typical case: [one-line vignette]
  Learner branch: [...]   Learner leaf: [...]   Result: [pass | fail]

Red-flag case: [one-line vignette]
  Learner branch: [...]   Learner leaf: [...]   Result: [pass | fail]
  If fail, why: [the red leaf was not first-pass — schema needs to surface it]

Atypical case: [one-line vignette]
  Learner branch: [...]   Learner leaf: [...]   Result: [pass | fail]
  If fail, why: [which branch was under-developed]

>>> WEAK POINTS
Branch most likely to fail under pressure: [name]
Red leaf most likely to be missed: [name]
Restudy target: [one specific node, named]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `problem` | The presenting problem to schematize |
| `framework` | anatomic / mechanistic / VINDICATE / learner-choice |
| `branch_count_target` | Forces a top-level branch range |
| `prune_overlap` | Enforces MECE leaves |
| `stress_test_cases` | Number and mix (typical / red-flag / atypical) |
| `require_red_flag_per_branch` | If `true` (default), each branch needs at least one red-leaf flag if any exist for that problem |
| `include_pediatric_branch` | Adds a pediatric branch for adult-default schemas where the differential genuinely shifts |

## Verification Checklist

- [ ] Framework named explicitly before building. No mixing (e.g., "anatomic-mechanistic-and-also-VINDICATE").
- [ ] Top-level branches are categories, not diagnoses.
- [ ] Every leaf has a one-phrase mechanism anchor.
- [ ] MECE check explicit: every leaf belongs to exactly one branch; overlaps documented and resolved.
- [ ] At least one red leaf per branch (when red leaves exist for this problem space).
- [ ] Stress tests run on three cases; failures are named (which branch, which leaf, why).
- [ ] No invented diagnoses, no eponyms used unless real and correctly anchored.
- [ ] Schema fits on one screen / one page when rendered.
- [ ] Restudy target is one named node, not "the whole schema."

## Worked Example (compact)

**Input:** problem = `acute dyspnea in an adult outpatient`, framework = `anatomic`, learner_level = `MS4`.

**Output (excerpt):**

```
DIAGNOSTIC SCHEMA — acute dyspnea in an adult outpatient
Framework: anatomic (upper airway → lower airway → parenchyma → pleura → vasculature → cardiac → systemic)

>>> BUILD TRANSCRIPT

Q [top-level branches]: ...
> "Upper airway, lower airway, lung parenchyma, pleura, pulmonary vasculature, cardiac, systemic."
Grade: 7 branches — MECE check: yes if you commit "lower airway" = bronchi/bronchioles and "parenchyma" = alveoli/interstitium. Collectively exhaustive for adult outpatient acute dyspnea.

Q [upper airway leaves]: ...
> "Anaphylaxis (angioedema), foreign body, infection (epiglottitis, peritonsillar abscess), vocal cord dysfunction."
Grade: solid; anaphylaxis is RED.

Q [lower airway]: ...
> "Asthma exacerbation, COPD exacerbation, acute bronchitis."
Grade: solid.

Q [parenchyma]: ...
> "Pneumonia, ARDS, acute eosinophilic / hypersensitivity pneumonitis."
Grade: ARDS is rarely outpatient — keep but note. Pneumonia is RED if hypoxic.

Q [pleura]: ...
> "Pneumothorax (spontaneous), pleural effusion (new), hemothorax."
Grade: pneumothorax is RED.

Q [vasculature]: ...
> "Pulmonary embolism."
Grade: PE is RED. Anything else?  > "Pulmonary hypertension exacerbation, rarely vasculitis with DAH."  Grade: yes.

Q [cardiac]: ...
> "Acute heart failure / pulmonary edema, MI presenting as dyspnea, tamponade, new arrhythmia."
Grade: MI and tamponade are RED; ACS-as-dyspnea is a classic atypical presentation in women, diabetics, elderly.

Q [systemic]: ...
> "Anemia (acute blood loss), DKA / metabolic acidosis with Kussmaul, sepsis, severe anxiety / panic."
Grade: sepsis is RED; panic is a diagnosis of exclusion.

>>> PRUNE
- "Pulmonary edema" sat between cardiac and parenchyma → placed on cardiac (hydrostatic mechanism), with note that ARDS is non-cardiogenic on parenchyma branch.
- "Aspiration" considered for upper airway vs. parenchyma → placed on parenchyma if pneumonitis is the issue, upper airway only if obstructed.

>>> RED LEAVES
Upper airway: anaphylaxis
Parenchyma: pneumonia (hypoxic)
Pleura: pneumothorax
Vasculature: PE
Cardiac: MI / ACS, tamponade
Systemic: sepsis, severe metabolic acidosis

>>> FINAL SCHEMA

Acute dyspnea in adult outpatient — anatomic schema

Upper airway:
  - anaphylaxis / angioedema   anchor: histaminergic upper-airway edema   [RED]
  - foreign body                anchor: mechanical obstruction
  - epiglottitis / PTA          anchor: infection-driven swelling
Lower airway:
  - asthma exacerbation         anchor: bronchospasm + airway inflammation
  - COPD exacerbation           anchor: chronic airflow limitation + trigger
Parenchyma:
  - pneumonia                   anchor: alveolar consolidation   [RED if hypoxic]
  - ARDS                        anchor: diffuse alveolar damage
Pleura:
  - pneumothorax (spontaneous)  anchor: pleural air, lung collapse   [RED]
  - new pleural effusion        anchor: fluid in pleural space
Vasculature:
  - pulmonary embolism          anchor: V/Q mismatch from clot   [RED]
  - PH exacerbation             anchor: RV failure
Cardiac:
  - acute HF / pulmonary edema  anchor: hydrostatic pulmonary edema
  - MI / ACS as dyspnea         anchor: ischemia → LV dysfunction or anginal equivalent   [RED]
  - tamponade                   anchor: pericardial fluid → RV inflow obstruction   [RED]
Systemic:
  - severe anemia               anchor: ↓ O2 carrying capacity
  - DKA / metabolic acidosis    anchor: Kussmaul respiratory compensation
  - sepsis                      anchor: systemic O2 demand + lung injury   [RED]

>>> STRESS TEST

Typical: 28-year-old with wheezing, prolonged expiration, peak flow drop, after URI.
  Learner: lower airway → asthma exacerbation.   Pass.

Red-flag: 55-year-old post-op day 4 with sudden pleuritic chest pain and dyspnea, HR 115, sat 92%.
  Learner: vasculature → PE.   Pass.

Atypical: 68-year-old diabetic woman with new exertional dyspnea, fatigue, no chest pain, EKG with anterior ST depressions.
  Learner: first guess "lower airway — COPD exacerbation," then on prompt revised to cardiac → ACS as anginal equivalent.   Partial.

>>> WEAK POINTS
Branch most likely to fail under pressure: cardiac (atypical ACS in women/diabetics/elderly).
Red leaf most likely to be missed: ACS-as-dyspnea (no chest pain).
Restudy target: anginal equivalents (dyspnea, fatigue, indigestion, jaw pain) — populations and EKG correlates.
```
