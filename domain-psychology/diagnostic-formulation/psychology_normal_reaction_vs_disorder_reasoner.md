---
title: "Normal Reaction vs. Disorder Reasoner"
category: psychology/diagnostic-formulation
description: "Apply structured clinical reasoning to determine when grief, acute stress, life-stage transition, or other expected human experiences cross the threshold into a diagnosable disorder"
techniques:
  - RT-02
  - QA-04
  - DS-04
  - CM-01
  - RT-05
difficulty: advanced
intended_use: model-testing
tags:
  - differential-diagnosis
  - grief
  - adjustment-disorder
  - acute-stress-response
  - normal-vs-pathological
  - bereavement
  - life-stage-transition
  - DSM-5-TR
  - diagnostic-reasoning
updated: "2026-06-08"
related_prompts:
  - domain-psychology/diagnostic-formulation/psychology_dsm5_differential_generator.md
  - domain-psychology/diagnostic-formulation/psychology_provisional_vs_rule_out_decision_aid.md
  - domain-psychology/diagnostic-formulation/psychology_comorbidity_mapping.md
  - domain-psychology/diagnostic-formulation/psychology_case_conceptualization_framework.md
---

# Normal Reaction vs. Disorder Reasoner

## Objective

Apply multi-dimensional clinical reasoning to determine whether a presenting distress response — grief, bereavement, acute stress reaction, life-stage transition, anticipated loss, cultural mourning practice, or situational emotional intensity — constitutes an expected human reaction or meets criteria for a DSM-5-TR diagnosable disorder. The output provides a structured evidence-weight analysis across the key threshold dimensions (severity, duration, impairment, cultural context, trajectory), not a binary verdict. All diagnostic conclusions require clinician confirmation.

## When to Use

- Intake or re-evaluation where the clinician is uncertain whether distress is grief/adjustment vs. MDD, PTSD, Prolonged Grief Disorder (PGD), acute stress disorder, or other diagnoses
- When prior providers or clients themselves have labeled an experience as "just grief" or "just stress" in a way that may have delayed appropriate treatment
- When a client or family is questioning whether what they are experiencing is "normal" or "needs treatment"
- Cross-cultural presentations where expected mourning practices, community responses to loss, or socially sanctioned distress duration differ significantly from Western clinical norms
- Supervision or consultation preparation for ethically complex presentations involving the cultural context of grief, religious mourning frameworks, or community-specific loss practices
- Model-testing contexts requiring nuanced grief/disorder boundary reasoning

Do not use to override a client's own framework for their experience. The goal is accurate clinical reasoning for appropriate care — not pathologizing normal human experiences, and not under-responding to genuine disorder.

## Inputs / Context Required

- **Precipitating event(s):** type of loss or stressor, timing relative to symptom onset, whether loss was anticipated or sudden, whether loss was traumatic in nature
- **Symptom description:** full symptom inventory across affective, cognitive, somatic, behavioral, relational, and functional domains
- **Duration:** how long since the precipitating event; trajectory of symptoms over time (improving, stable, worsening, fluctuating)
- **Functional impact:** work/school, relationships, self-care, safety behaviors; which domains are impaired and by how much
- **Cultural and religious context:** cultural community, religious traditions related to mourning, community expectations for grief expression and duration `[clinician input required]`
- **Prior loss history:** previous bereavements, prior grief episodes, prior treatment for grief or depression
- **Client's own framework:** how the client understands their experience; whether they believe they need help `[clinician input required]`
- **Pre-loss baseline:** whether mood, functioning, or interpersonal difficulties predated the precipitating event
- **Safety:** suicidal ideation, self-harm, substance use since loss `[clinician input required]`

## Constraints

### Must
- Evaluate distress against multiple threshold dimensions — not duration alone or severity alone
- Explicitly apply DSM-5-TR grief and bereavement guidance: DSM-5-TR removed bereavement exclusion for MDD in 2013; clinicians must actively evaluate MDD criteria even in the context of bereavement, while recognizing that normative grief can mimic MDD
- Apply Prolonged Grief Disorder (PGD, F43.8) criteria from DSM-5-TR (added in DSM-5-TR 2022): duration >12 months post-loss in adults (6 months in children), grief intensity beyond expected social/cultural norms, significant functional impairment; distinguish from normal grief and from MDD
- Distinguish among: normal grief / bereavement, acute stress response (subclinical), Acute Stress Disorder (ASD, F43.0), PTSD (F43.1x), Adjustment Disorder (F43.2x), Prolonged Grief Disorder (PGD, F43.8), Major Depressive Disorder (F32–F33), and Persistent Depressive Disorder (F34.1)
- Apply cultural context as a primary moderating dimension — what is normative varies substantially by community, and applying Western duration norms to non-Western mourning practices is a documented diagnostic error
- Frame output as a dimensional, evidence-weight analysis rather than a binary "normal vs. pathological" verdict
- Include a trajectory dimension: a symptom pattern that is improving even if currently intense may warrant watchful waiting rather than immediate diagnosis; a plateau or worsening trajectory is a diagnostic signal regardless of duration
- Flag bereavement-specific vs. non-grief-related symptoms: in MDD during bereavement, symptoms like worthlessness, pervasive anhedonia, psychomotor change, suicidal ideation, and severe impairment are less typical of normative grief

### Must Not
- Default to "normal grief" as a reason to withhold assessment or treatment — failure to diagnose treatable MDD or PTSD during bereavement is a clinical error
- Apply DSM-5-TR duration criteria as hard thresholds without acknowledging that trajectory and impairment are as clinically significant as duration
- Dismiss culturally sanctioned mourning practices as pathological simply because they differ from Western norms; consult cultural formulation approach (DSM-5-TR CFI) where cultural fit is uncertain
- Pathologize normal human suffering — the goal of this tool is accurate classification, not diagnostic inflation
- Omit the safety screen: suicidal ideation, passive death wishes, and self-harm are elevated after significant loss and must be assessed regardless of whether a diagnosable disorder is present

## Instructions

1. **Characterize the precipitating event** on the following axes:
   - Type: bereavement (human death), non-death loss (divorce, job, health, relationship, role), cumulative losses, developmental transition (empty nest, retirement, new parenthood), traumatic event (sudden/violent loss, disaster, assault)
   - Temporal position: acute (within days/weeks), subacute (weeks to months), chronic/prolonged (>6 months from event)
   - Expectedness: anticipated (e.g., terminal illness death) vs. sudden (e.g., accident, suicide); whether anticipatory grief was present
   - Traumatic features: was the death or stressor traumatic in nature (sudden, violent, witnessed, physically threatening)? Traumatic loss activates both grief and potential PTSD symptom pathways simultaneously

2. **Map symptoms to the candidate disorder domains** using the following boundary framework:

   **Normal grief / bereavement reaction (non-pathological):**
   - Intermittent waves of sadness, yearning, longing for the deceased
   - Preoccupation with the deceased and circumstances of death
   - Preserved capacity for positive affect at least intermittently ("dual process")
   - Symptoms diminish in frequency and intensity over time (improving trajectory)
   - Social functioning impaired but not collapsed; support-seeking is present
   - Meaning-making progresses, albeit non-linearly
   - Duration varies substantially by culture; premature resolution is not the goal

   **Prolonged Grief Disorder (PGD — F43.8):**
   - Intense yearning/longing for deceased OR intense preoccupation with deceased persisting beyond 12 months (adults) / 6 months (children) post-loss
   - At least 3 of: identity disruption, disbelief about death, avoidance of reminders, intense emotional pain, difficulty engaging with life, emotional numbness, feeling life is meaningless, intense loneliness
   - Clinically significant distress or impairment
   - Out of proportion to cultural/religious norms
   - Not better explained by MDD, PTSD, or another disorder
   - Key distinction from MDD: PGD is loss-specific; emotions center on the relationship and absence of the person; hedonic capacity for non-loss-related activities is relatively preserved

   **Major Depressive Disorder (MDD — F32/F33) during bereavement:**
   - Pervasive anhedonia (not just inability to enjoy without the deceased, but global loss of pleasure)
   - Persistent worthlessness or excessive guilt unrelated to the loss itself
   - Psychomotor retardation or agitation
   - Suicidal ideation beyond passive death wishes to be reunited with the deceased
   - Severe cognitive impairment (concentration, memory)
   - Full criteria met for at least 2 weeks; impairment across multiple domains, not only loss-related
   - Symptoms do not fluctuate with context — present throughout the day, not only in grief waves
   - Key distinction from normal grief: MDD is pervasive across contexts; grief is more contextually triggered

   **Adjustment Disorder (F43.2x):**
   - Emotional or behavioral symptoms in response to an identifiable stressor
   - Disproportionate distress relative to the severity or nature of the stressor
   - OR significant impairment in functioning
   - Onset within 3 months of stressor
   - Duration does not exceed 6 months after the stressor (or its consequences) has ended
   - Does not meet criteria for another disorder (most important rule-out)
   - Subtypes: with depressed mood, with anxiety, with mixed emotional features, with disturbance of conduct, with mixed disturbance of emotions and conduct, unspecified

   **Acute Stress Disorder (ASD — F43.0) vs. PTSD (F43.1x):**
   - ASD: intrusion, negative mood, dissociation, avoidance, arousal symptoms within 3 days to 1 month of traumatic event; requires at least 9 of 14 specified symptoms
   - PTSD: same symptom clusters, onset any time, duration >1 month after trauma, full 4-cluster structure (intrusion, avoidance, negative cognitions/mood, arousal)
   - Both require exposure to traumatic event meeting Criterion A — death, threatened death, serious injury, or sexual violence
   - Distinction from grief: grief after a traumatic death may trigger both PGD and PTSD simultaneously; evaluate criteria sets independently

3. **Evaluate the threshold dimensions independently**:

   | Dimension | Normal Reaction Signal | Disorder Threshold Signal |
   |-----------|----------------------|--------------------------|
   | **Severity** | Intense but bearable; fluctuates; positive affect interspersed | Unrelenting; no positive-affect windows; overwhelming across the day |
   | **Duration** | Decreasing over time; cultural norms respected | Plateau or worsening; chronologically beyond cultural normative range |
   | **Impairment** | Temporary functional reduction; person maintains essential self-care and relationships | Functional collapse across multiple domains; unable to work, maintain safety, maintain essential care |
   | **Trajectory** | Gradual, non-linear improvement; "dual process" oscillation present | Stuck; worsening; no oscillation; no functional adaptation |
   | **Cultural fit** | Consistent with community mourning norms | Flagged by the person's own community as concerning; or markedly exceeding community norms |
   | **Identity continuity** | Sense of self is intact even while grieving | Identity disruption, loss of purpose, feeling life has no meaning going forward |
   | **Hedonic access** | Grief is contextually triggered; person can experience pleasure in non-loss-related contexts at least intermittently | Global hedonic loss; anhedonia even for previously valued activities unrelated to loss |
   | **Cognitive pattern** | Thinking is loss-focused; concentration temporarily reduced | Pervasive worthlessness, hopelessness, cognitive impairment across contexts |
   | **Safety** | Passive death wish to "be with" deceased; no active plan or intent | Active suicidal ideation with plan or intent; self-harm; substance use as acute risk |

4. **Apply the cultural context modifier**. Before assigning any threshold determination:
   - Identify the cultural and religious community the client belongs to
   - Assess community-specific mourning duration norms (e.g., Jewish shiva and shloshim; South Asian mourning practices; West African community grief expression; Indigenous community practices)
   - Determine whether the client identifies the community norms as personally relevant
   - Flag when cultural practice appears to overlap with PGD symptoms structurally but is normative within the cultural context
   - Use the DSM-5-TR Cultural Formulation Interview (CFI) supplementary module on grief as a reference framework `[clinician input required for full CFI]`

5. **Generate a threshold evidence matrix** weighing each dimension and arriving at a provisional classification:

   Provisional classification options:
   - **Normal grief/expected reaction — watchful waiting appropriate**
   - **Subthreshold distress — monitor, psychoeducation, and support; no diagnostic coding**
   - **Adjustment Disorder — criteria met; evaluate subtype**
   - **Prolonged Grief Disorder — duration and intensity criteria met; PGD protocol indicated**
   - **Major Depressive Disorder — pervasive criteria met independent of grief context; treatment indicated**
   - **Acute Stress Disorder — traumatic loss with sufficient ASD criteria within 1 month**
   - **PTSD — traumatic loss + 4-cluster criteria >1 month**
   - **Comorbid presentation — e.g., PGD + MDD or PTSD + PGD** (use comorbidity mapping prompt for treatment implications)
   - **Insufficient information to classify — defer; list information needed**

6. **Produce a watchful waiting vs. active treatment recommendation frame**:
   - Watchful waiting: when trajectory is improving, impairment is manageable, cultural context supports, client does not identify as needing treatment
   - Active treatment: when trajectory has plateaued or worsened, impairment is significant and not improving, safety concerns are present, client is requesting help
   - Include a re-evaluation timeline for watchful waiting recommendations

## Output Format

### Presentation Summary

```
PRECIPITATING EVENT: [clinician input required]
TIME SINCE EVENT: [clinician input required]
SYMPTOM DURATION: [clinician input required]
SYMPTOM TRAJECTORY: [Improving / Plateau / Worsening / Fluctuating]
CULTURAL/RELIGIOUS CONTEXT: [clinician input required]
SAFETY STATUS: [clinician input required]
OUTPUT STATUS: Clinical reasoning scaffold — diagnostic conclusions require clinician confirmation
```

---

### Threshold Evidence Matrix

| Dimension | Evidence Present | Signal Direction | Weight |
|-----------|-----------------|-----------------|--------|
| Severity | [describe] | Normal / Subthreshold / Disorder | Low / Moderate / High |
| Duration | [describe] | Normal / Subthreshold / Disorder | |
| Trajectory | [describe] | Normal / Subthreshold / Disorder | |
| Functional impairment | [describe] | Normal / Subthreshold / Disorder | |
| Cultural fit | [describe] | Within norms / Exceeds norms / Uncertain | |
| Identity continuity | [describe] | Preserved / Disrupted | |
| Hedonic access | [describe] | Present / Globally lost | |
| Cognitive pattern | [describe] | Loss-focused / Pervasive | |
| Safety | [describe] | No active concerns / Passive ideation / Active risk | |

---

### Diagnostic Boundary Analysis

| Candidate Diagnosis | ICD-10-CM | Evidence Supporting | Evidence Against | Current Status |
|--------------------|-----------|--------------------|-----------------|-|
| Normal grief / expected reaction | N/A | [list] | [list] | In / Out / Uncertain |
| Adjustment Disorder (specify subtype) | F43.2x | | | |
| Prolonged Grief Disorder | F43.8 | | | |
| Major Depressive Disorder | F32.x / F33.x | | | |
| Acute Stress Disorder | F43.0 | | | |
| PTSD | F43.1x | | | |

---

### Provisional Classification and Recommendation

```
Provisional Classification: [clinician input required — based on matrix above]

Recommendation:
  [ ] Watchful waiting — re-evaluate at: [date/session target]
  [ ] Psychoeducation and support without formal diagnosis
  [ ] Adjustment Disorder treatment (specify subtype)
  [ ] PGD-specific treatment (e.g., Complicated Grief Treatment / PGT)
  [ ] MDD treatment (CBT-D, BA, pharmacotherapy consult)
  [ ] ASD/PTSD treatment (PE, CPT, EMDR)
  [ ] Comorbid protocol — see comorbidity mapping prompt
  [ ] Defer — information needed: [list]

Safety Plan Needed: [ ] Yes — refer to risk-crisis prompts  [ ] Not currently indicated

Cultural Consultation Recommended: [ ] Yes  [ ] Not currently indicated

[Clinician confirmation required for all classification and treatment decisions]
```

---

### Verification Checklist

- [ ] Each threshold dimension evaluated independently, not just duration
- [ ] DSM-5-TR bereavement exclusion removal applied — MDD criteria evaluated even in grief context
- [ ] PGD criteria (DSM-5-TR 2022) applied separately from MDD criteria
- [ ] Traumatic loss evaluated for ASD/PTSD criteria independent of grief criteria
- [ ] Cultural context applied as a primary moderating dimension, not an afterthought
- [ ] Trajectory dimension included — improving vs. plateau vs. worsening affects classification
- [ ] Safety screen completed and documented
- [ ] Output framed as evidence-weight analysis, not binary normal/pathological verdict
- [ ] Watchful waiting recommendation includes specific re-evaluation trigger and date
- [ ] All classification conclusions tagged `[Clinician confirmation required]`
