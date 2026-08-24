---
title: "Microbiology Bug × Drug × Syndrome Grid Builder"
category: medical-education/learner-foundational-sciences
description: "Produce a high-yield three-axis grid (organism × clinical syndrome × empiric/definitive antimicrobial) for a named infection scope. Cells carry the empiric coverage, definitive agent after susceptibilities, duration anchor, and one resistance pitfall."
techniques:
  - ST-03
  - OC-03
  - CM-01
  - DS-02
  - RT-05
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-clinical
  - intern
  - resident-junior
  - pa-student
  - pharmacy-student
  - nursing-student
tags:
  - microbiology
  - antimicrobials
  - bug-drug
  - infectious-disease
  - empiric-therapy
  - foundational-science
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-foundational-sciences/study_microbiology_virology_table_builder.md
  - domain-medical-education/learner-foundational-sciences/study_pharmacology_mechanism_flashcard_set.md
---

## Objective

Build a compact, board- and bedside-useful grid: each row is an organism (or organism class), each column is a clinical syndrome that organism typically causes, and each cell carries: (1) empiric agent of choice, (2) definitive agent after susceptibilities, (3) duration anchor, (4) one common resistance pitfall. Output is a single visual grid plus a footnote per drug class for stewardship.

## Your Role

ID-trained hospitalist preparing a teaching aid for housestaff on a single page. Tight, current, no soft phrasing. Reference frame: IDSA / Sanford Guide / institutional antibiogram defaults. If institutional antibiogram is not provided, default to US national patterns and *say so*.

## Inputs

- `scope`: which slice of bugs to grid — e.g., "common gram-positive cocci," "ESKAPE pathogens," "atypical pneumonia organisms," "bloodstream infection — community-acquired," "intra-abdominal infection," "bacterial meningitis by age band," "STIs"
- `syndromes`: optional list (otherwise pick the canonical 3–6 syndromes for the scope)
- `learner_level`: `MS3 | MS4 | intern | resident | pharmacy-student`
- `setting`: `outpatient | ward | ICU | ED | OR`
- `local_antibiogram_notes`: free text (if absent, mark grid as "default US patterns; reconcile with local antibiogram")
- `age_band`: `neonate | infant | child | adult | elderly` — affects empiric defaults

## Method

1. **Lock the scope and syndromes.** State the slice of micro this grid covers, list the syndromes you'll use as columns, and acknowledge what the grid *does not* cover (e.g., "this grid does not include fungal coverage").

2. **Build the row list (organisms).** Pick organisms by clinical frequency *within the chosen scope and setting*. Note if any row is a class rather than a single species (e.g., "non-pseudomonal gram-negative rods").

3. **Build the column list (syndromes).** Each column is a specific clinical syndrome — bacteremia, pneumonia, meningitis, UTI, cellulitis, endocarditis, etc. Not a body region.

4. **Populate each cell** with four lines:
   - **EMPIRIC:** drug(s) of choice for that bug × syndrome in the chosen setting, including loading dose if relevant.
   - **DEFINITIVE:** narrowest agent once susceptibilities return, with duration.
   - **DURATION ANCHOR:** typical course (e.g., "uncomplicated 5 days; bacteremic 14 days from first negative culture").
   - **RESISTANCE PITFALL:** one specific resistance mechanism or stewardship trap (e.g., "MSSA: cefazolin/nafcillin > vanc — vanc *underperforms* in MSSA bacteremia").

5. **Footnote per drug class.** Below the grid, one line per drug class used: spectrum reminder, signature toxicity, dose adjustment cue (renal/hepatic), and one drug interaction.

6. **Mark cells where the empiric and definitive agent diverge sharply** — these are the high-yield teaching points.

## Output Format

```
BUG × DRUG × SYNDROME GRID
Scope: [...]   Setting: [...]   Age band: [...]
Reference frame: [IDSA / Sanford / institutional]   Local antibiogram: [supplied / default US]

NOT COVERED HERE: [explicit gaps, e.g., fungal, mycobacterial]

| Organism \ Syndrome | [Syndrome A] | [Syndrome B] | [Syndrome C] | ... |
|---|---|---|---|---|
| [Bug 1] | EMP: ...<br>DEF: ...<br>DUR: ...<br>PIT: ... | ... | ... |
| [Bug 2] | ... | ... | ... |
| ... |

HIGH-YIELD DIVERGENCE CALLOUTS
- [Bug × Syndrome]: empiric [X], definitive [Y] — because [reason]
- ...

DRUG CLASS FOOTNOTES
- [Class]: spectrum [...]; signature toxicity [...]; dose adjust in [renal/hepatic]; interaction [...]
- ...

STEWARDSHIP NOTES
- Cells where coverage is broader than needed pending culture — narrow to definitive within [N] hours of speciation.
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `scope` | Selects which bugs make rows |
| `setting` | Outpatient default → oral agents; ICU → IV, broader empiric |
| `age_band` | Changes empiric defaults (neonatal meningitis ≠ adult meningitis) |
| `pregnancy_overlay` | If true, mark each cell with pregnancy-safe alternative |
| `penicillin_allergy_overlay` | If true, add allergy-adapted alternative per cell |
| `mrsa_prevalence` | `low | moderate | high` — shifts empiric vanc/linezolid inclusion |

## Verification Checklist

- [ ] No empty cells. If a bug doesn't cause that syndrome, write `—` not a guess.
- [ ] Empiric ≠ definitive in at least one cell per row — otherwise the row is teaching nothing.
- [ ] Every cell has all four lines (EMP / DEF / DUR / PIT). No abbreviated cells.
- [ ] Duration anchor is a number with a condition (e.g., "5 days uncomplicated"), not "as long as needed."
- [ ] Resistance pitfall is *specific* (named mechanism or specific stewardship trap), not generic warning.
- [ ] Drug-class footnotes match the agents named in the grid (no class footnoted that doesn't appear, no agent in the grid without a footnote).
- [ ] If institutional antibiogram absent, the grid is explicitly labeled as default-US.
- [ ] No invented drugs, no invented organisms, no off-label combinations without a clinical rationale.

## Worked Example (compact)

**Input:** `scope = adult community-acquired pneumonia organisms`, `syndromes = outpatient CAP, ward CAP, ICU CAP, post-influenza pneumonia`, `setting = mixed`, `age_band = adult`.

**Output (excerpt):**

```
BUG × DRUG × SYNDROME GRID
Scope: Adult CAP organisms   Setting: mixed (outpatient / ward / ICU / post-flu)
Reference frame: ATS/IDSA 2019 CAP guideline   Antibiogram: default US

NOT COVERED HERE: aspiration with anaerobes, HCAP/HAP, fungal, TB.

| Organism \ Syndrome | Outpatient CAP | Ward CAP | ICU CAP | Post-influenza |
|---|---|---|---|---|
| Streptococcus pneumoniae | EMP: amoxicillin 1 g TID or doxycycline if no comorbid<br>DEF: PCN-S — penicillin / amoxicillin<br>DUR: 5 days uncomplicated<br>PIT: PCN-R serotypes rising; if MIC > 2 use ceftriaxone | EMP: ceftriaxone + macrolide (or doxycycline)<br>DEF: ceftriaxone or amoxicillin if susceptible<br>DUR: 5–7 days<br>PIT: macrolide resistance now ~30% — don't monotherapy outpatient empirically | EMP: ceftriaxone + azithromycin (or levofloxacin)<br>DEF: per susceptibility<br>DUR: 7–10 days; bacteremic 14<br>PIT: meningitis seeding if bacteremic — LP if suspicion | EMP: as ward/ICU + cover S. aureus including MRSA<br>DEF: per susceptibility<br>DUR: 7–10 days<br>PIT: streptococcal post-flu less common than staph but still occurs |
| Staphylococcus aureus (MSSA) | EMP: not typical outpatient CAP<br>DEF: cefazolin / nafcillin / oxacillin<br>DUR: 14 days from clinical improvement; longer if bacteremic<br>PIT: vancomycin underperforms in MSSA bacteremia — switch to cefazolin once MSSA confirmed | EMP: ceftriaxone + macrolide doesn't cover S. aureus; add nafcillin or cefazolin if suspected<br>DEF: cefazolin<br>DUR: 14 days<br>PIT: rapid cavitary necrosis with PVL+ strains | EMP: add vancomycin or linezolid until MRSA excluded<br>DEF: cefazolin if MSSA<br>DUR: 14 days; longer with empyema<br>PIT: same — narrow as soon as MSSA confirmed | EMP: cover MRSA empirically (vanc or linezolid)<br>DEF: per susceptibility<br>DUR: 14+ days<br>PIT: post-flu S. aureus mortality high — empiric MRSA coverage warranted |
| Mycoplasma pneumoniae | EMP: doxycycline or azithromycin<br>DEF: same<br>DUR: 5 days<br>PIT: macrolide-R Mycoplasma reported in Asia and emerging US; doxy is safer empiric | EMP: macrolide / doxy alongside beta-lactam<br>DEF: macrolide / doxy<br>DUR: 5–7 days<br>PIT: cold agglutinin hemolysis (rare) | EMP: levofloxacin covers atypicals + typicals<br>DEF: same<br>DUR: 7–10 days<br>PIT: ICU CAP rarely Mycoplasma alone | — |
| Legionella pneumophila | EMP: macrolide (rare outpatient unless severe) or fluoroquinolone<br>DEF: levofloxacin > azithromycin<br>DUR: 7–10 days<br>PIT: urinary antigen detects serogroup 1 only | EMP: as outpatient<br>DEF: same<br>DUR: 10–14 days if immunocompromised<br>PIT: hyponatremia, transaminitis are clue findings | EMP: levofloxacin (preferred) or azithromycin<br>DEF: same<br>DUR: 14–21 days<br>PIT: hot tubs / cooling towers — outbreak history matters | — |

HIGH-YIELD DIVERGENCE CALLOUTS
- MSSA bacteremic pneumonia: empiric vancomycin, but definitive should be *cefazolin or nafcillin* (vancomycin worse outcomes).
- Pneumococcus with MIC > 2: amoxicillin still works for non-CNS infection; meningitis requires ceftriaxone + vanc empirically.
- Post-flu pneumonia: don't omit MRSA coverage empirically.

DRUG CLASS FOOTNOTES
- Beta-lactams (amoxicillin, ceftriaxone, cefazolin, nafcillin): spectrum mostly gram-positive plus depending on agent; signature toxicity rash, rare seizure with carbapenems; dose-adjust ceftriaxone in cirrhosis not renal; interaction with warfarin via gut flora.
- Macrolides (azithromycin): atypicals + S. pneumoniae (with rising resistance); signature QT prolongation, GI motility (motilin agonism); hepatic metabolism; CYP3A4 interactions (less with azithro than erythromycin).
- Tetracyclines (doxycycline): broad atypical + gram-positive + some gram-negative; signature photosensitivity, esophagitis, pediatric tooth staining (now relaxed for short courses); no major renal dose adjust; chelates with cations.
- Fluoroquinolones (levofloxacin, moxifloxacin): broad typical + atypical; signature tendinopathy, aortic dissection risk, QT, dysglycemia, C. diff; renal adjust levofloxacin; many interactions including chelation, warfarin, QT-prolonging drugs.
- Anti-MRSA (vancomycin, linezolid): vanc nephrotoxicity (AUC-based dosing), red-man syndrome (rate-related); linezolid serotonin syndrome with SSRIs, thrombocytopenia, lactic acidosis with prolonged use.

STEWARDSHIP NOTES
- Narrow within 48–72 h of culture speciation; de-escalate empiric MRSA / Pseudomonas coverage when not supported by data.
- Atypical coverage is required for ward and ICU empiric CAP regimens (combination or monotherapy with respiratory FQ).
```
