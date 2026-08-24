---
title: "Personality Disorder Dimensional Formulation (DSM-5 Section III AMPD)"
category: psychology/diagnostic-formulation
description: "Generate a dimensional personality disorder formulation using the DSM-5 Alternative Model for Personality Disorders (Section III), rating self/interpersonal functioning and pathological trait domains"
techniques:
  - RT-02
  - DS-04
  - QA-04
  - ST-04
  - CM-01
difficulty: advanced
intended_use: model-testing
tags:
  - personality-disorder
  - dimensional-model
  - AMPD
  - DSM-5-Section-III
  - self-functioning
  - interpersonal-functioning
  - trait-domains
  - PID-5
  - diagnostic-formulation
updated: "2026-06-08"
related_prompts:
  - domain-psychology/diagnostic-formulation/psychology_dsm5_differential_generator.md
  - domain-psychology/diagnostic-formulation/psychology_case_conceptualization_framework.md
  - domain-psychology/diagnostic-formulation/psychology_comorbidity_mapping.md
  - domain-psychology/treatment-planning/psychology_modality_selection_decision_aid.md
---

# Personality Disorder Dimensional Formulation (DSM-5 Section III AMPD)

## Objective

Generate a structured personality disorder formulation using the DSM-5 Alternative Model for Personality Disorders (AMPD, Section III). The formulation profiles the client across: (A) Level of Personality Functioning (self and interpersonal domains), (B) pathological personality trait domains and facets, and (C) the clinical portrait that emerges from the intersection of functioning level and trait profile. The dimensional approach produces a formulation that captures severity, trait specificity, and functional impact without forcing categorical assignment to a single PD type where presentations are mixed or subthreshold. All formulation conclusions require clinician confirmation.

## When to Use

- Any presentation where personality functioning impairment is a central clinical feature — pervasive pattern across contexts, onset by early adulthood, not fully explained by Axis I pathology
- When categorical DSM-5-TR Section II PD diagnoses (Cluster A, B, C) are insufficient to describe a complex or mixed presentation
- Treatment planning that requires trait-specific intervention targets (not just a categorical label)
- Long-term psychotherapy (DBT, TFP, schema therapy, MBT) where the formulation drives the treatment frame
- Supervision or case consultation preparation for personality pathology cases
- Research or model-testing contexts requiring AMPD-structured reasoning

Not appropriate as a tool for personality assessment without an established clinical relationship and multi-session observation. Personality disorder formulation requires longitudinal, cross-contextual evidence.

## Inputs / Context Required

- **Longitudinal pattern evidence:** duration and pervasiveness of the pattern — onset, cross-contextual consistency `[clinician input required]`
- **Self-domain observations:** identity, self-direction, sense of self across stressors, level of self-criticism, emptiness, self-harm or self-destructive behavior history
- **Interpersonal domain observations:** capacity for empathy, intimacy pattern, relationships across contexts (work, family, romantic, therapeutic), recurrent relational conflicts or endings
- **Trait observations across the five AMPD domains:** behavioral, emotional, cognitive, and interpersonal observations that map to Negative Affectivity, Detachment, Antagonism, Disinhibition, and Psychoticism domains
- **PID-5 or other trait measure data:** if formal personality trait assessment has been administered `[clinician input required]`
- **Differential diagnostic context:** known Axis I diagnoses and their relationship to personality features (e.g., is identity instability more consistent with BPD vs. MDD with poor self-esteem?)
- **Cultural context:** cultural norms around self-expression, emotional display, relational closeness, and authority that may affect trait interpretation `[clinician input required]`
- **Functional impairment:** across work, relationships, self-care, and subjective well-being

## Constraints

### Must
- Structure the formulation across both AMPD Criterion A (Level of Personality Functioning Scale — LPFS) and Criterion B (pathological trait domains and facets)
- Rate the LPFS across all four elements: **Identity** (self domain), **Self-Direction** (self domain), **Empathy** (interpersonal domain), **Intimacy** (interpersonal domain) — at one of five levels: 0 (little or no impairment), 1 (some impairment), 2 (moderate impairment), 3 (severe impairment), 4 (extreme impairment)
- Profile trait domains and facets from the five AMPD domains: Negative Affectivity, Detachment, Antagonism, Disinhibition, Psychoticism — with relevant facets for each elevated domain
- Map elevated trait domains to the six AMPD-recognized PD types where the profile aligns: **Antisocial**, **Avoidant**, **Borderline**, **Narcissistic**, **Obsessive-Compulsive**, **Schizotypal** — and note when the profile crosses types or is best described dimensionally without a specific type assignment
- Include a **Section II / Section III comparison note**: note how the presentation maps (or fails to map) to the categorical Section II PD system, for clinical and documentation purposes
- Apply cultural calibration: behaviors that represent pathological antagonism, detachment, or negative affectivity within one cultural frame may be normative in another; flag where cultural context is relevant to trait interpretation
- Frame all LPFS ratings as clinician-derived estimates based on available evidence; LPFS ratings are clinical inferences, not psychometric scores unless the LPFS self-report (LPFS-SR) was formally administered

### Must Not
- Assign an AMPD formulation based on a single session or acute-state observation — personality formulation requires cross-contextual, longitudinal evidence
- Conflate Axis I state disorders with personality trait domains (e.g., acute MDD may produce apparent LPFS identity impairment and negative affectivity elevation that normalizes with treatment)
- Reduce the dimensional formulation to a single categorical label — the value of the AMPD is in the profile, not in replacing one category with another
- Apply pejorative language (e.g., "manipulative," "attention-seeking," "difficult") in the formulation — trait language (e.g., "antagonism," "attention-seeking as a facet of histrionism") is preferable
- Omit the distinction between state-related personality amplification and trait-level personality pathology
- Generate an AMPD formulation without acknowledging that Section III remains a proposed alternative model in DSM-5/DSM-5-TR and that Section II categorical diagnoses are the officially recognized coding system for ICD-10-CM billing

## Instructions

1. **Establish the longitudinal basis**. Before rating LPFS or trait domains, confirm:
   - Pattern duration: is there evidence of a pervasive, enduring pattern across early adulthood?
   - Cross-contextual consistency: is the pattern present across multiple relationship contexts (work, family, romantic, therapeutic), not only in one domain?
   - Not better explained by Axis I pathology: could the features be entirely explained by an active Axis I episode (e.g., MDD, PTSD, psychosis) rather than a stable trait pattern?
   Flag if longitudinal evidence is insufficient — AMPD formulation should be provisional when the observational base is limited.

2. **Rate the Level of Personality Functioning Scale (LPFS)** across four elements:

   **Self-Functioning Domain:**

   *Identity* — coherence and stability of self-experience, self-esteem regulation, capacity to tolerate distress
   - Level 0: Stable, coherent identity; self-esteem regulated within normal range; tolerates distress
   - Level 1: Minor inconsistencies in self-view; some vulnerability in self-esteem under stress; generally maintains identity
   - Level 2: Fragile self-esteem; identity markedly vulnerable to threat; struggles to maintain consistent self-view under stress; emptiness may be present
   - Level 3: Significant fragility; identity diffuse or defined primarily through relationship to others; chronic emptiness; little capacity for self-reflection without destabilization
   - Level 4: Poor differentiation of self from others; unstable self-concept; identity collapse under even mild stress; identity confusion and fragmentation
   Rating: `[clinician input required]`

   *Self-Direction* — goal pursuit, internal standards, prosocial reflection
   - Level 0: Coherent goals; reasonable internal standards; functions autonomously
   - Level 1: Some instability in goals; minor rigidity or lack of reflection on impact of behavior
   - Level 2: Goals unrealistic or incoherent; standards excessively rigid or absent; limited reflection on consequences
   - Level 3: Goals unstable and shifting; behavior driven by immediate gratification or external cues; limited future orientation
   - Level 4: Inability to sustain goal-directed behavior; internal standards absent; no ability to reflect on one's own role in difficulties
   Rating: `[clinician input required]`

   **Interpersonal-Functioning Domain:**

   *Empathy* — ability to consider and understand others' experiences, motivations, and perspectives
   - Level 0: Accurate perception of others' experiences; flexibility in perspective-taking
   - Level 1: Slightly limited awareness of others' perspectives; occasionally misses subtle emotional cues
   - Level 2: Limited awareness of, or interest in, others' experience; may misread emotional cues; hypervigilant to others' reactions as threats
   - Level 3: Hypervigilant to others as threatening; superficial understanding of others; relationships experienced primarily in terms of impact on self
   - Level 4: Limited capacity to consider others' perspectives; interactions experienced through projection; interpersonal reasoning dominated by own internal state
   Rating: `[clinician input required]`

   *Intimacy* — depth and duration of close relationships, desire for intimacy, capacity for mutuality
   - Level 0: Sustained, meaningful close relationships; capacity for mutual intimacy
   - Level 1: Some capacity for intimacy; may be somewhat constrained in depth or duration
   - Level 2: Relationships superficial or unstable; limited capacity for mutuality; patterns of idealization/devaluation or excessive dependency
   - Level 3: Relationships primarily experienced as vehicles for meeting own needs; limited genuine intimacy; exploitation or avoidance of closeness
   - Level 4: Relationships highly impoverished or absent; closeness avoided or deeply destabilizing; profound impairment in relational capacity
   Rating: `[clinician input required]`

3. **Profile the Criterion B pathological trait domains**. For each of the five domains, rate whether it is **elevated** (clinically significant level of the trait) or **not elevated**, and if elevated, identify the specific facets that are most prominent:

   **Negative Affectivity** (vs. Emotional Stability)
   - Facets: Emotional lability, Anxiousness, Separation insecurity, Perseveration, Submissiveness, Hostility, Depressivity, Suspiciousness, Restricted affectivity (inverse)
   - Elevated when: frequent and intense negative emotional experiences; emotional reactivity out of proportion to context; sustained negative affect between stressors
   - Most associated AMPD PD types: Borderline, Avoidant

   **Detachment** (vs. Extraversion/Positive Emotionality)
   - Facets: Withdrawal, Intimacy avoidance, Anhedonia, Depressivity (shared with Negative Affectivity), Restricted affectivity, Suspiciousness (shared)
   - Elevated when: pervasive distance from others and from positive experience; restricted emotional range; preference for solitude beyond individual variation
   - Most associated AMPD PD types: Avoidant (with Negative Affectivity), Schizotypal

   **Antagonism** (vs. Agreeableness)
   - Facets: Manipulativeness, Deceitfulness, Grandiosity, Attention seeking, Callousness, Hostility (shared with Negative Affectivity)
   - Elevated when: pervasive self-interested behavior at expense of others; exploitative or hostile interpersonal style; inflated self-regard or covert sense of specialness
   - Most associated AMPD PD types: Antisocial, Narcissistic, Borderline (Hostility)

   **Disinhibition** (vs. Conscientiousness)
   - Facets: Irresponsibility, Impulsivity, Distractibility, Risk taking, Rigid perfectionism (inverse)
   - Elevated when: actions without regard for consequences; poor planning; inability to tolerate delay; pattern of commitments abandoned
   - Most associated AMPD PD types: Antisocial, Borderline

   **Psychoticism** (vs. Lucidity)
   - Facets: Unusual beliefs and experiences, Eccentricity, Cognitive and perceptual dysregulation
   - Elevated when: odd or magical thinking; perceptual aberrations; pronounced eccentricity in behavior and speech that is stable and cross-contextual
   - Most associated AMPD PD types: Schizotypal

4. **Map the trait-domain profile to AMPD PD types** where applicable:

   | AMPD PD Type | Criterion A (LPFS) Threshold | Criterion B Trait Profile |
   |--------------|------------------------------|--------------------------|
   | Antisocial | Moderate (≥2) in self-direction and empathy | Antagonism (manipulativeness, deceit, callousness, hostility) + Disinhibition (irresponsibility, impulsivity, risk-taking) |
   | Avoidant | Moderate (≥2) in intimacy and self-direction | Negative Affectivity (anxiousness) + Detachment (withdrawal, anhedonia, intimacy avoidance) |
   | Borderline | Moderate (≥2) across all four LPFS elements | Negative Affectivity (emotional lability, anxiousness, separation insecurity, depressivity, impulsivity) + Antagonism (hostility) + Disinhibition (impulsivity, risk-taking) |
   | Narcissistic | Moderate (≥2) in identity (grandiosity) and empathy | Antagonism (grandiosity, attention seeking, callousness) |
   | OCD (AMPD) | Moderate (≥2) in self-direction | Negative Affectivity (perseveration, restricted affect) + Disinhibition (inverse: rigid perfectionism, risk aversion) |
   | Schizotypal | Moderate (≥2) across all four LPFS elements | Psychoticism (unusual beliefs, eccentricity, perceptual dysregulation) + Detachment |

   If the profile does not fit a single type, describe the **dimensional personality profile** without forcing a type assignment. Note which trait domains are elevated and which LPFS elements are most impaired.

5. **Generate the Section II comparison note**. For documentation and billing:
   - Note the corresponding Section II PD(s) that the Section III profile most closely maps to
   - Flag where the Section III profile is mixed across types and which Section II category is most defensible for ICD-10-CM coding
   - Use ICD-10-CM F60.x codes anchored to the Section II system for billing; Section III formulation is documented as the clinical formulation in the narrative

6. **Build treatment implications** from the dimensional profile:
   - LPFS severity drives level-of-care and stabilization needs (higher severity → more structured support, greater emphasis on alliance before exposure to difficult material)
   - Negative Affectivity elevation → emotion regulation skills priority (DBT, ACT)
   - Antagonism elevation → alliance rupture and repair work; motivational enhancement; forensic/coercive referrals require additional consideration
   - Detachment elevation → approach motivation activation, schema work, mentalizing
   - Disinhibition elevation → behavioral contingency work, impulsive-action chains, safety planning priority
   - Psychoticism elevation → reality testing support, structured relational work, Mentalization-Based Treatment (MBT)

## Output Format

### Formulation Context

```
LONGITUDINAL BASIS: [duration of pattern, contexts observed, cross-contextual consistency noted]
AXIS I DIFFERENTIAL APPLIED: [how Axis I state pathology was distinguished from trait pattern]
CULTURAL CONTEXT APPLIED: [relevant factors]
DATA SOURCES: [interview, records, collateral, PID-5 data if available]
OUTPUT STATUS: Dimensional formulation scaffold — all LPFS ratings and trait profile require clinician confirmation
```

---

### LPFS Profile

| LPFS Element | Domain | Rating (0–4) | Clinical Evidence |
|--------------|--------|-------------|-------------------|
| Identity | Self | [0–4] | [clinician input] |
| Self-Direction | Self | [0–4] | [clinician input] |
| Empathy | Interpersonal | [0–4] | [clinician input] |
| Intimacy | Interpersonal | [0–4] | [clinician input] |

**Overall LPFS Severity:** Little/Some/Moderate/Severe/Extreme impairment `[Clinician confirmation required]`

---

### Criterion B Trait Domain Profile

| Trait Domain | Elevated? | Most Prominent Facets | Clinical Evidence |
|-------------|-----------|----------------------|-------------------|
| Negative Affectivity | [ ] Yes / [ ] No | [list facets if elevated] | [clinician input] |
| Detachment | [ ] Yes / [ ] No | | |
| Antagonism | [ ] Yes / [ ] No | | |
| Disinhibition | [ ] Yes / [ ] No | | |
| Psychoticism | [ ] Yes / [ ] No | | |

---

### Dimensional Personality Profile Summary

```
LPFS Severity Level: [Overall rating]
Elevated Trait Domains: [list]
Most Prominent Facets: [list top 4–6 facets across domains]
AMPD PD Type Correspondence: [specific type(s) / mixed profile / dimensional without type assignment]
Section II Mapping for Billing: [ICD-10-CM F60.x with rationale]
Formulation Narrative: [2–4 sentence clinician-authored summary integrating LPFS + trait + functional context]
```

---

### Treatment Implications

| Elevated Domain or LPFS Element | Primary Treatment Target | Evidence-Informed Modality |
|--------------------------------|-------------------------|---------------------------|
| [domain/element] | [e.g., emotion dysregulation, impulsive action chains, identity instability] | [e.g., DBT, TFP, MBT, schema therapy, ISTDP] |

---

### Verification Checklist

- [ ] Longitudinal, cross-contextual basis established before LPFS ratings are applied
- [ ] Axis I state pathology distinguished from trait pattern — Axis I episodes not conflated with trait elevation
- [ ] All four LPFS elements rated with supporting clinical evidence
- [ ] All five Criterion B domains evaluated (not just domains that align with suspected PD type)
- [ ] Section II ICD-10-CM billing code identified for documentation purposes
- [ ] Cultural context applied to trait interpretation
- [ ] Pejorative or stigmatizing language absent — trait language used throughout
- [ ] Treatment implications derived from dimensional profile, not from categorical label
- [ ] AMPD Section III vs. Section II distinction noted for documentation clarity
- [ ] All LPFS ratings and trait elevations tagged `[Clinician confirmation required]`
