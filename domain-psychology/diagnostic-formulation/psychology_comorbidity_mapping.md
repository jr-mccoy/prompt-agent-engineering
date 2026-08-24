---
title: "Comorbidity Mapping and Treatment Implication Planner"
category: psychology/diagnostic-formulation
description: "Map common comorbidity patterns across DSM-5-TR diagnostic pairs and triads, and derive sequencing and treatment-modification implications for each pattern"
techniques:
  - RT-02
  - DS-04
  - QA-04
  - ST-04
  - RT-05
difficulty: advanced
intended_use: model-testing
tags:
  - comorbidity
  - co-occurring-disorders
  - MDD
  - PTSD
  - SUD
  - BPD
  - anxiety
  - treatment-planning
  - sequencing
updated: "2026-06-08"
related_prompts:
  - domain-psychology/diagnostic-formulation/psychology_dsm5_differential_generator.md
  - domain-psychology/diagnostic-formulation/psychology_case_conceptualization_framework.md
  - domain-psychology/diagnostic-formulation/psychology_normal_reaction_vs_disorder_reasoner.md
  - domain-psychology/treatment-planning/psychology_modality_selection_decision_aid.md
---

# Comorbidity Mapping and Treatment Implication Planner

## Objective

Generate a structured comorbidity map for a given diagnostic profile — identifying the pattern type (hierarchical, shared-diathesis, sequential, bidirectional), the clinical and neuroscientific basis for co-occurrence, how each diagnosis modifies the other's presentation, and the evidence-based sequencing and treatment-modification implications that follow. Output functions as a treatment planning scaffold; all diagnostic and sequencing decisions require clinician confirmation.

## When to Use

- Treatment planning for any client carrying two or more confirmed or provisional diagnoses
- When symptom presentation seems cross-diagnostic and treatment targets are not obvious
- Before selecting a therapeutic modality for a comorbid profile — to determine whether an integrated or sequential approach is indicated
- Stepped-care decisions: when to address diagnosis A before, alongside, or after diagnosis B
- Supervision preparation to articulate the comorbidity rationale for a treatment plan
- Model-testing scenarios requiring accurate comorbidity epidemiology and treatment-implication reasoning

Do not use to generate a differential — this tool assumes the diagnostic picture is established (Confirmed or Provisional). Run `psychology_dsm5_differential_generator.md` first if diagnoses are not yet assigned.

## Inputs / Context Required

- **Confirmed or provisional diagnoses:** DSM-5-TR terms with ICD-10-CM codes if available `[clinician input required]`
- **Temporal relationship:** which disorder appeared first, and by how long; or if simultaneous onset
- **Severity of each diagnosis:** mild / moderate / severe; primary presenting concern vs. background
- **Treatment history for each diagnosis:** what has been tried, with what outcome
- **Current functional impairment:** which diagnosis is causing the greatest burden right now
- **Client-identified priorities:** which problem the client most wants addressed first `[clinician input required]`
- **Safety status:** active suicidal ideation, self-harm, substance use acuity — these override sequencing logic `[clinician input required]`
- **Setting and level of care:** outpatient, IOP/PHP, inpatient — affects feasibility of simultaneous treatment

## Constraints

### Must
- Identify the **pattern type** for each diagnostic pair or triad: hierarchical (one causes or maintains the other), shared-diathesis (common vulnerability), sequential (one predated the other), bidirectional (each maintains the other), or coincidental (independent conditions co-occurring)
- For each pattern type, derive the **treatment-sequencing implication**: address simultaneously, address A before B, address B before A, or treat the shared mechanism
- Reference empirically-supported treatment guidance from the evidence base (without overstating — use uncertainty language where evidence is limited)
- Flag when a comorbid pattern **contra-indicates** or **modifies** a standard first-line treatment (e.g., standard imaginal exposure for PTSD may require modification when SUD is actively destabilizing, or BPD-level emotion dysregulation may require DBT stabilization before trauma processing)
- Address **symptom overlap and diagnostic boundary issues** for each pair — which symptoms are shared and how overlap affects treatment target selection
- Include a **monitoring consideration** for each comorbid pair: how does treatment of one diagnosis change the presentation or severity trajectory of the other
- Frame all outputs as clinician scaffolds, not final treatment recommendations

### Must Not
- Assign comorbidity pattern type without acknowledging the evidence base for the classification (some patterns are epidemiologically established; others are theoretical models)
- Present sequential treatment (A before B) as universally superior to integrated treatment without context — evidence supports both approaches for specific pairings
- Omit safety-status override: when active suicidality, acute substance use, or life-threatening symptoms are present, standard sequencing logic is suspended in favor of stabilization priority
- Overstate causal relationships — many comorbidity patterns involve correlation, not established causality
- Apply adult comorbidity epidemiology directly to pediatric or geriatric populations without noting population-specific caveats

## Instructions

1. **Receive and organize the diagnostic profile**. List each confirmed or provisional diagnosis, its severity, temporal onset relative to other diagnoses, and current functional burden.

2. **Identify all diagnosis pairs and triads** in the profile. For three or more diagnoses, prioritize pairings by clinical relevance (highest burden, most treatable, most treatment-modifying).

3. **For each pair, classify the comorbidity pattern type**:

   **Hierarchical (primary/secondary):**
   - One disorder appears to drive or directly cause the other
   - Classic example: Alcohol Use Disorder → MDD (substance-induced depressive disorder must be ruled out; if MDD persists >4 weeks after abstinence, primary MDD is more likely)
   - Treatment implication: generally address the primary disorder first, though exceptions exist

   **Shared-Diathesis (common vulnerability):**
   - Both disorders share a common genetic, neurobiological, or psychological risk factor
   - Classic example: MDD + GAD — both associated with neuroticism, negative affectivity, HPA axis dysregulation; share the "internalizing spectrum"
   - Treatment implication: transdiagnostic approaches (Unified Protocol, ACT) may address shared mechanisms more efficiently than separate disorder-specific protocols

   **Sequential (predated → sensitization):**
   - Earlier disorder sensitizes the system, increasing vulnerability to the second
   - Classic example: Childhood trauma / PTSD → adult MDD; PTSD → SUD (self-medication onset)
   - Treatment implication: trauma-focused work is often indicated even when MDD appears "primary" to current presentation; PTSD treatment may resolve downstream SUD

   **Bidirectional (mutual maintenance):**
   - Each disorder actively maintains or exacerbates the other through behavioral or neurobiological mechanisms
   - Classic examples: MDD ↔ insomnia; PTSD ↔ SUD; BPD ↔ MDD; panic disorder ↔ agoraphobia
   - Treatment implication: integrated treatment targeting the maintaining cycle is generally superior to sequential treatment of either disorder alone; neither disorder remits durably without addressing the other

   **Coincidental:**
   - Epidemiological co-occurrence without a demonstrated mechanistic relationship
   - Less common in clinical populations, where shared pathways are the rule
   - Treatment implication: address independently but monitor for cross-diagnostic interactions

4. **Apply the sequencing decision algorithm** for each pair:

   | Pattern Type | Default Sequencing Guidance | Override Conditions |
   |--------------|---------------------------|---------------------|
   | Hierarchical (A → B) | Address A first; reassess B after A improves | B is life-threatening or causing severe impairment independent of A |
   | Shared-Diathesis | Transdiagnostic or integrated approach; or address more impairing diagnosis first | Strong modality-specific preference; prior treatment history favors single-diagnosis protocol |
   | Sequential (A predated B) | Address A (the sensitizing condition) unless B is currently more impairing; monitor for B resolution | B is in current acute episode requiring stabilization before A can be addressed |
   | Bidirectional | Integrated or parallel treatment preferred; if sequential is necessary, address the maintaining cycle entry point | Safety concerns, level of care, or client readiness may force sequencing |
   | Coincidental | Address by severity and client priority | Cross-diagnostic medication interactions |

5. **For the highest-priority pairings**, produce detailed treatment modification notes:

   **Common high-burden pairings and their treatment modification evidence:**

   **MDD + Anxiety Disorders (GAD, Panic, Social Anxiety, OCD)**
   - Pattern: Shared-diathesis (internalizing spectrum); bidirectional at symptom level
   - Treatment modification: CBT protocols with integrated cognitive and exposure components; anxious distress specifier modifies MDD presentation; anxiety often warrants higher therapy frequency in early treatment
   - Sequencing: typically simultaneous — transdiagnostic or anxiety-augmented CBT-D
   - Monitoring: as depression lifts, anxiety may become more functionally prominent; reassess after 4–6 sessions

   **PTSD + MDD**
   - Pattern: Sequential (trauma → depression) and bidirectional (each maintains the other)
   - Treatment modification: trauma-focused treatment (PE, CPT, EMDR) addresses both when MDD is secondary to PTSD; standalone depression treatment has poor durability without trauma processing
   - Sequencing: CPT and PE show efficacy for comorbid MDD+PTSD simultaneously; DBT-PE or CPT preferred when emotion dysregulation is prominent
   - Monitoring: depressive symptoms often remit partially with PTSD treatment; track separately

   **PTSD + Substance Use Disorder (SUD)**
   - Pattern: Sequential (PTSD → SUD via self-medication) and bidirectional (SUD re-traumatization risk, intoxication prevents trauma processing)
   - Treatment modification: Seeking Safety for stabilization; COPE (concurrent treatment of PTSD and substance use) or DBT-PTSD for simultaneous treatment; standard imaginal exposure requires modification during active SUD
   - Sequencing: integrated treatment outperforms sequential in most RCTs; abstinence is not required before trauma work begins but active intoxication during sessions is a contraindication
   - Safety override: active suicidality or AUD/withdrawal risk (Wernicke's, seizure threshold) takes sequencing precedence

   **BPD + MDD**
   - Pattern: Bidirectional and shared-diathesis (emotion dysregulation, early adversity, attachment disruption)
   - Treatment modification: BPD-level emotion dysregulation destabilizes standard CBT-D; DBT (the evidence base for BPD) addresses MDD as a secondary target; antidepressants have limited efficacy in BPD-predominant presentations without stabilization
   - Sequencing: DBT as the primary modality addresses BPD features while MDD responds as emotion regulation improves; standalone MDD treatment without BPD-specific skills work has high dropout and low durability
   - Monitoring: BPD-driven MDD episodes may be brief-episodic rather than sustained; track episode frequency and intensity separately from BPD behavioral targets

   **BPD + PTSD**
   - Pattern: Sequential (early relational trauma → BPD features) and bidirectional; high diagnostic overlap in trauma-spectrum presentations
   - Treatment modification: Phase-based approach (stabilization → trauma processing) is standard; DBT-PE is the most validated protocol; trauma work before DBT skills acquisition increases risk of decompensation
   - Sequencing: DBT Phase 1 stabilization before EMDR or PE; exception if trauma is the acutely driving problem and emotion regulation skills are sufficient
   - Monitoring: PTSD symptoms may partially overlap with BPD dissociative criteria; track separately using structured measures

   **MDD + SUD (any substance)**
   - Pattern: Bidirectional and hierarchical (SUD may be primary, or MDD may drive self-medication)
   - Treatment modification: Integrated Cognitive Behavioral Therapy (ICBT), COPE; antidepressant efficacy is reduced during active SUD; MDD may be substance-induced and should be re-evaluated after 4 weeks of abstinence
   - Sequencing: determine temporal order to assess primary vs. substance-induced MDD; both require concurrent treatment in most presentations; naltrexone + antidepressant in AUD+MDD has RCT support
   - Safety override: AUD withdrawal, opioid use disorder with overdose risk — medical stabilization before psychotherapy sequencing decisions

   **Anxiety Disorders + SUD**
   - Pattern: Sequential (anxiety → substance use as anxiolytic) and bidirectional (substance withdrawal exacerbates anxiety)
   - Treatment modification: standard exposure-based anxiety treatment requires adjustment if benzodiazepine use is present (benzos blunt fear response, reducing habituation); ICBT or Integrated CBT for comorbid anxiety+SUD
   - Monitoring: anxiety often worsens in early sobriety before improving; normalize and monitor separately

6. **Generate the comorbidity map** in the Output Format below. Include all diagnosed pairs, their pattern types, sequencing guidance, and treatment modification notes.

7. **Apply the safety-status override check**: Before finalizing sequencing, confirm no active safety concern overrides the derived sequence. Document the override if present.

## Output Format

### Diagnostic Profile Summary

```
CONFIRMED/PROVISIONAL DIAGNOSES:
  1. [Diagnosis, ICD-10-CM code, Severity, Onset]
  2. [Diagnosis, ICD-10-CM code, Severity, Onset]
  3. [...]
PRIMARY PRESENTING CONCERN: [clinician input required]
SAFETY STATUS: [clinician input required — active SI/SH/substance acuity]
OUTPUT STATUS: Comorbidity scaffold — all sequencing decisions require clinician confirmation
```

---

### Comorbidity Pair Analysis Table

| Pair | Pattern Type | Clinical Basis for Co-occurrence | Symptom Overlap | Sequencing Guidance | Treatment Modification | Monitoring Flag |
|------|-------------|----------------------------------|-----------------|---------------------|----------------------|-----------------|
| [Dx A + Dx B] | [Bidirectional / Sequential / Shared-Diathesis / Hierarchical / Coincidental] | [Mechanism or epidemiological basis] | [Shared symptom domains — e.g., "sleep, concentration, anhedonia overlap across MDD and PTSD"] | [Simultaneous / A before B / B before A / Treat shared mechanism] | [Named protocol modifications, contraindications, evidence base] | [What to monitor as one diagnosis is treated] |

---

### Treatment Sequencing Priority Ranking

```
Priority 1 (Address First / Simultaneously):
  Rationale: [safety-status, acuity, or pattern type]

Priority 2 (Address After Priority 1 Stabilizes or Alongside):
  Rationale:

Priority 3 (Address After Priority 2 or as Adjunct):
  Rationale:

Safety Override Active? [Yes / No]
  If Yes: [Specify override condition and resulting modified sequence]

[Clinician confirmation required — final sequencing is a clinical judgment]
```

---

### Modality Fit by Comorbidity Profile

| Comorbidity Pattern | Best-Fit Modality or Protocol | Evidence Level | Limitations |
|--------------------|-------------------------------|---------------|-------------|
| [Pattern] | [e.g., DBT-PE, COPE, ICBT, Unified Protocol, CPT] | [RCT / Pilot / Expert Consensus] | [Population limits, severity thresholds, access barriers] |

---

### Verification Checklist

- [ ] Every diagnosed pair has a pattern type classification with stated rationale
- [ ] Sequencing guidance is derived from pattern type, not applied generically
- [ ] Treatment modification notes reference named protocols or evidence-based guidance
- [ ] Safety-status override check is complete and documented
- [ ] Symptom overlap between diagnoses is noted so treatment targets are not double-counted
- [ ] Monitoring flags are present for each pair — what changes as one diagnosis is treated
- [ ] Output is framed as a scaffold; final sequencing and modality decisions are `[Clinician confirmation required]`
- [ ] Uncertainty language is used where evidence for a specific comorbidity management approach is limited
