---
title: "Developmental History Compiler"
category: psychology/intake-assessment
description: "Compile a structured developmental history from prenatal through late adolescence for an adult psychiatric intake, covering milestones, adversity, learning, and psychosocial transitions."
techniques:
  - ST-04
  - DT-02
  - RT-02
  - CM-02
  - QA-04
difficulty: intermediate
intended_use: model-testing
tags:
  - developmental-history
  - ACEs
  - childhood
  - milestones
  - neurodevelopment
  - ADHD
  - ASD
  - IEP
  - intake
  - cpt-90791
updated: "2026-06-08"
related_prompts:
  - domain-psychology/documentation/psychology_intake_assessment_note.md
  - domain-psychology/intake-assessment/psychology_trauma_history_intake_module.md
  - domain-psychology/intake-assessment/psychology_psychiatric_history_compiler.md
  - domain-psychology/diagnostic-formulation/psychology_case_conceptualization_framework.md
---

# Developmental History Compiler

## Objective

Compile a structured developmental history for an adult psychiatric intake, progressing from prenatal context through late adolescence. The output:

1. Organizes data across five developmental epochs: Prenatal/Perinatal, Early Childhood (0–5), Middle Childhood (6–12), Early Adolescence (13–15), and Late Adolescence (16–18/emerging adulthood).
2. Captures milestones (motor, language, social, cognitive) and flags delays.
3. Documents Adverse Childhood Experiences (ACEs) in each epoch as context for predisposing factors, without duplicating or replacing the trauma history module.
4. Records learning and neurodevelopmental history: educational evaluations, IEP/504 plans, ADHD/ASD evaluations, and academic trajectory.
5. Produces a Developmental History section and a brief Developmental Summary ready for the 90791 biopsychosocial intake note.

## When to Use

- At adult psychiatric intake when developmental history is clinically indicated (personality disorder presentations, suspected autism or ADHD, trauma-focused work, complex case formulation, neurodevelopmental differential).
- As a standalone section to complete when the full intake occurs over multiple sessions.
- When an existing case lacks a documented developmental history and a formulation review is underway.
- For predisposing-factors analysis in a five-P case formulation.

## Inputs / Context Required

Data for this section typically derive from client self-report, supplemented where available by records (school records, prior evaluations, prior clinical notes) or collateral from parents/guardians (with ROI). Note the source for each data element.

- **Prenatal / Perinatal:** Planned vs. unplanned pregnancy; maternal health during pregnancy (substance use, illness, mental health, nutrition, prenatal care); birth complications (premature, NICU, complications during delivery); birth weight and perinatal medical concerns; adoption or early separation from biological parents.
- **Early Childhood (0–5):** Motor milestones (walking, fine motor); language milestones (first words by 12 months, two-word phrases by 24 months, sentences by 36 months; regression); social development (reciprocal play, stranger anxiety, imaginary play); temperament as described by caregivers; early attachment quality; early medical conditions; early trauma or adversity; daycare or early care arrangements; quality of early caregiving environment.
- **Middle Childhood (6–12):** School entry age and experience; reading, writing, and math development; academic performance trajectory; teacher concerns; neuropsychological or educational evaluations (IQ testing, achievement testing); IEP or 504 plan (dates, services, primary disability category); ADHD or ASD evaluation (referral, diagnosis, outcome); peer relationships; extracurricular involvement; family stability (moves, separations, caregiver changes, economic instability); ACEs in this epoch.
- **Early Adolescence (13–15):** Onset of puberty and response; middle-school social dynamics; first significant peer conflicts or bullying; identity development beginnings; substance experimentation onset if any; legal involvement onset if any; family relational shifts; academic trajectory changes; first mental health symptoms or treatment; major losses or transitions.
- **Late Adolescence (16–18/emerging adulthood):** High school completion or disruption; driving, employment, independence milestones; romantic and sexual relationship beginnings; gender and sexual identity exploration; substance use patterns; legal involvement; departure from family home; post-secondary planning; first significant mental health episodes, hospitalizations, or treatment; cultural rites of passage or transitions.
- **ACE count (if administered):** Felitti et al. 10-item ACE score with categories endorsed. If not formally scored, note specific adversities mentioned by the client across categories (physical abuse, emotional abuse, sexual abuse, neglect physical/emotional, household substance use, household mental illness, domestic violence, incarceration of household member, parental separation/divorce).
- **Caregiver and family of origin:** Caregiver roster across developmental epochs; stability of care; attachment quality to primary caregiver; notable caregiver psychopathology, substance use, or incarceration.

## Constraints

### Must

- Organize output by developmental epoch in sequential order; do not merge epochs.
- Document milestone status as: achieved on schedule / delayed (specify domain) / not assessed / regressed (specify age and context).
- Flag developmental delays in each domain (motor, language, social, cognitive) explicitly.
- Document neurodevelopmental evaluation history: whether evaluated, when, findings, and services received.
- Record ACEs by epoch and compute or note total ACE count if available; use ACE categories as defined by Felitti et al. (1998) in the original study — abuse, neglect, and household dysfunction subscores.
- For any developmental epoch where the client was separated from primary caregivers, document the nature and duration of the separation and caregiving arrangement during that period.
- Note information source for each epoch (client self-report, records review, collateral with ROI status).
- Flag epochs for which no data were obtained with `[clinician input required: planned for session X / collateral to be sought]`.

### Must Not

- Do not interpret developmental data as definitive diagnosis (e.g., early language delay does not confirm ASD); flag as contributing data for differential.
- Do not reproduce trauma detail in this section beyond identifying that trauma occurred in a given epoch — detailed trauma narrative belongs in the Trauma History module.
- Do not assume caregiver quality; document what was reported, avoiding evaluative language about caregivers not in evidence.
- Do not import demographic assumptions about developmental norms across cultures without noting cultural context.
- Do not fabricate; gaps are flagged.

## Instructions

1. **Organize inputs by developmental epoch.** Assign each data point to its epoch before drafting.

2. **Draft Prenatal/Perinatal section.** Note maternal health context, complications, and early caregiver separation if applicable.

3. **Draft Early Childhood section.** Systematically address motor, language, social, and cognitive milestones. Note temperament and early attachment quality. Flag delays with domain and severity.

4. **Draft Middle Childhood section.** Cover school experience, academic trajectory, educational evaluations, IEP/504 history, neurodevelopmental evaluation history. List specific services provided. Document peer and family context.

5. **Draft Early Adolescence section.** Cover identity development, school and peer transitions, early symptom onset, and ACEs in this epoch.

6. **Draft Late Adolescence section.** Cover high school trajectory, independence milestones, post-secondary path, first significant mental health episodes, and major transitions.

7. **Compile ACE summary.** List categories endorsed, epoch of occurrence, and total ACE count if calculable. Note ACE count–dose relationship context (cite Felitti et al. 1998: ACE score ≥ 4 is associated with significantly elevated risk for multiple adult health and mental health outcomes).

8. **Write the Developmental Summary paragraph.** In two to four sentences, identify the most clinically salient developmental themes: primary attachment quality, key adversity epochs, neurodevelopmental factors, and developmental trajectory as context for the current presentation.

9. **Run verification.**

## Output Format

```
=== DEVELOPMENTAL HISTORY ===

Client: [Initials/MRN]    Date of Service: [YYYY-MM-DD]
Information Source(s): [Client self-report / Records reviewed / Collateral (ROI date)]
CPT Context: Section of 90791 biopsychosocial intake note.

─────────────────────────────────────────
PRENATAL / PERINATAL
─────────────────────────────────────────
Pregnancy planned/unplanned: [...]
Maternal health during pregnancy: [Substance use / Mental health / Medical illness /
Prenatal care adequacy / Nutritional status]
Birth: [Full-term / Premature at X weeks / Birth complications — describe]
Perinatal medical concerns: [NICU / Apgar / Weight / Other]
Early caregiver arrangement: [Raised by biological parents / Adoption at age X /
Foster care / Relative care — describe]
Source: [clinician input required / client report / records]

─────────────────────────────────────────
EARLY CHILDHOOD (Ages 0–5)
─────────────────────────────────────────
Motor milestones: [On schedule / Delayed — domain and age of concern]
Language milestones: [On schedule / Delayed — specify: first words, phrases,
sentences; any regression at age X]
Social development: [Reciprocal play, peer engagement, stranger anxiety, 
attachment behaviors — on track / concerning / delayed]
Temperament (caregiver-reported): [Easy / Difficult / Slow-to-warm / Mixed]
Early attachment quality: [Secure indicators / Anxious indicators /
Avoidant indicators / Disorganized indicators — base on reported behavior]
Early medical conditions: [...]
Early adversity: [ACE categories identified in this epoch — no detail; cross-reference Trauma History]
Early caregiving environment: [Stability, number of caregivers, quality indicators]
Source: [...]

─────────────────────────────────────────
MIDDLE CHILDHOOD (Ages 6–12)
─────────────────────────────────────────
School entry: [Age, public/private/homeschool, transition experience]
Academic trajectory: [Reading, writing, math — grade level / struggles / strengths]
Teacher concerns: [None reported / Attention, behavior, learning — describe]
Educational evaluations: [None / IEP or 504 evaluation at age X:
  Disability category: [...]
  Services received: [...]
  Duration: [...]
Neurodevelopmental evaluation:
  ADHD evaluation: [Not conducted / Conducted at age X — result: diagnosed / not diagnosed /
  equivocal — diagnostic label and services]
  ASD evaluation: [Not conducted / Conducted at age X — result: diagnosed / not diagnosed /
  equivocal]
  Other neuropsychological evaluation: [...]
Peer relationships: [Age-appropriate / Isolated / Bullied / Bully / Mixed]
Extracurricular engagement: [...]
Family stability in this epoch: [Moves, caregiver changes, separations, economic disruption]
ACEs in this epoch: [Categories, approximate ages — no traumatic detail]
Source: [...]

─────────────────────────────────────────
EARLY ADOLESCENCE (Ages 13–15)
─────────────────────────────────────────
Pubertal onset and response: [Age, client's and family's response]
Social peer context: [Friendships, bullying, cliques, social identity]
Identity development: [Gender identity, sexual orientation, cultural/religious identity]
Substance use onset: [None / First use of X at age Y]
Legal involvement onset: [None / Arrests, charges at age X]
Academic trajectory: [Maintained / Declining / Improved — grade history if known]
Mental health: [First recognized symptoms at age X / First treatment contact at age X]
Family context: [Stability, major changes, conflict]
Major losses or transitions in this epoch: [...]
ACEs in this epoch: [...]
Source: [...]

─────────────────────────────────────────
LATE ADOLESCENCE (Ages 16–18 / Emerging Adulthood)
─────────────────────────────────────────
High school outcome: [Graduated / GED / Dropped out at grade X — context]
Employment/independence milestones: [First job, driving, financial independence]
Romantic/sexual relationships: [Onset, patterns, quality]
Gender/sexual identity: [Stable / Emerging / Significant exploration in this period]
Substance use patterns: [Frequency, quantity, dependence signs in this epoch]
Legal involvement: [...]
Mental health in this epoch: [First episode, hospitalizations, diagnoses, medications]
Post-secondary path: [College / Vocational / Military / Employment / None — context]
Departure from family home: [Age, circumstances, voluntariness]
Cultural rites of passage / transitions: [...]
ACEs in this epoch: [...]
Source: [...]

─────────────────────────────────────────
ACE SUMMARY
─────────────────────────────────────────
ACEs identified across developmental history:

Abuse:
  Physical abuse:     [Epoch(s) / Not reported]
  Emotional abuse:    [Epoch(s) / Not reported]
  Sexual abuse:       [Epoch(s) / Not reported]

Neglect:
  Physical neglect:   [Epoch(s) / Not reported]
  Emotional neglect:  [Epoch(s) / Not reported]

Household Dysfunction:
  Substance use in household:             [Epoch(s) / Not reported]
  Mental illness in household:            [Epoch(s) / Not reported]
  Domestic violence (witnessed):          [Epoch(s) / Not reported]
  Incarceration of household member:      [Epoch(s) / Not reported]
  Parental separation / divorce:          [Epoch(s) / Not reported]

ACE count: [X / 10] (Felitti et al., 1998 categories)
Note: ACE scores ≥ 4 carry elevated risk for multiple adult health and mental health outcomes
(Felitti et al., 1998, Am J Prev Med). Detailed trauma narrative in Trauma History module.

─────────────────────────────────────────
DEVELOPMENTAL SUMMARY
─────────────────────────────────────────
[Two to four sentence narrative identifying the most clinically salient developmental themes:
primary attachment quality, key adversity epochs and ACE burden, neurodevelopmental factors
(if present), and developmental trajectory as predisposing context for the current presentation.
Frame as predisposing factors in the five-P formulation.]

─────────────────────────────────────────
DOMAINS REQUIRING FOLLOW-UP
─────────────────────────────────────────
[List any epoch or subdomain flagged [clinician input required] with plan for how data
will be obtained (collateral with ROI, records request, follow-up session) and timeline.]
```

## Verification

- [ ] All five developmental epochs present in sequence.
- [ ] Each epoch covers milestones (or flags them as not assessed).
- [ ] Developmental delays are flagged by domain (motor, language, social, cognitive) with specifics.
- [ ] Neurodevelopmental evaluation history (ADHD, ASD, IEP/504) documented — presence or explicit absence.
- [ ] ACE categories documented per epoch; ACE count compiled or noted as not calculable.
- [ ] Traumatic details are referenced (acknowledged in epoch) but not narrated here — Trauma History module cross-referenced.
- [ ] Source of data noted for each epoch (self-report, records, collateral with ROI status).
- [ ] Developmental Summary is integrative narrative, not a list restatement.
- [ ] Gaps flagged with `[clinician input required: ...]` and planned follow-up noted.
- [ ] No diagnostic conclusions drawn from developmental data alone without clinical interview corroboration.
