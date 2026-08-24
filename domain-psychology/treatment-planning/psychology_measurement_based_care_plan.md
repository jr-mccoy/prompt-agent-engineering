---
title: "Measurement-Based Care Plan"
category: psychology/treatment-planning
description: "Build a measurement-based care (MBC) plan specifying instrument selection, administration cadence, scoring interpretation, and a feedback-to-treatment-decision protocol."
techniques:
  - DS-02
  - DT-01
  - ST-04
  - CM-01
  - QA-04
difficulty: intermediate
intended_use: model-testing
tags:
  - measurement-based-care
  - outcome-monitoring
  - PHQ-9
  - GAD-7
  - PCL-5
  - ROM
  - treatment-planning
  - feedback-informed-treatment
updated: "2026-06-08"
related_prompts:
  - domain-psychology/treatment-planning/psychology_smart_treatment_goal_generator.md
  - domain-psychology/treatment-planning/psychology_golden_thread_writer.md
  - domain-psychology/treatment-planning/psychology_treatment_resistance_reformulation.md
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
---

# Measurement-Based Care Plan

## Objective

Produce a structured measurement-based care (MBC) plan that specifies: (1) which validated outcome instruments to use and why, (2) the administration cadence, (3) how scores are reviewed and interpreted in session, (4) the decision rules that link score trajectories to treatment adjustments, and (5) documentation standards for the treatment record. The plan implements feedback-informed treatment (FIT) principles and satisfies requirements for value-based care reporting, accreditation, and utilization review.

## When to Use

- At treatment initiation, to establish the outcome-monitoring infrastructure before the first formal progress review.
- When a practice, clinic, or training site is building an MBC protocol from scratch.
- When a clinician inherits a client mid-treatment without prior ROM (routine outcome monitoring) data.
- When the current treatment plan includes goals but no specified measurement method — retrofitting the measurement layer.
- When moving from one level of care to another and a new baseline is needed.

## Inputs / Context Required

- **Diagnoses** (DSM-5-TR / ICD-10-CM): all active, including SUD and medical comorbidities.
- **Primary treatment target(s)**: the 1–3 problems that the current episode will prioritize.
- **Episode type and length**: outpatient weekly / IOP / PHP / ongoing (no fixed end); approximate planned duration.
- **Available instruments at the practice**: which validated instruments the setting is already using (to avoid introducing an entirely new battery if duplication exists).
- **Client literacy and language**: reading level; whether translated instruments are needed.
- **Session frequency**: weekly / biweekly / 2×/week — affects administration burden.
- **Setting type**: private practice, community mental health, hospital outpatient, integrated primary care, training clinic — affects what infrastructure exists for scoring and tracking.
- `[clinician input required: any cultural considerations that affect instrument validity for this client]`
- `[clinician input required: whether the client has previously expressed negative reactions to rating scales — use this to shape the consent framing]`

## Constraints

### Must

- Select instruments that are (a) validated for the diagnosis or symptom domain, (b) freely available or in widespread licensed use in clinical settings, (c) brief enough for routine session administration (≤ 5 minutes per instrument).
- Specify a primary instrument (the one that drives the clinical decision rule) and secondary instruments (those that add detail or track comorbid domains).
- Set a minimum administration cadence: at least every 2–4 sessions for the primary instrument. More frequent cadence (every session) is preferred for PHQ-9, GAD-7, and PCL-5 in active treatment.
- Define score interpretation bands using the instrument's published norms; include the minimally clinically important difference (MCID) and remission threshold.
- Write a decision-rule protocol: specific score patterns that trigger a defined clinical response (continue, discuss, modify, refer, step up LOC).
- Include a not-improving rule: if no meaningful improvement (as defined by MCID) is detected by session 8 (or equivalent for IOP/PHP), the clinician must discuss the trajectory with the client and document a plan review.
- Specify how scores are reviewed in session (not just collected in a waiting room): include a brief dialogue script for introducing and reviewing scores.
- Include a documentation standard: where in the progress note the score is recorded and how it links to the goal/objective in the treatment plan.

### Must Not

- Do not assign instruments that have no validation for the target population or diagnosis.
- Do not use a cadence so infrequent (e.g., quarterly in active weekly treatment) that trajectory data is clinically useless.
- Do not allow the score to be collected but never reviewed in session — this violates the feedback loop that makes MBC effective.
- Do not select a primary instrument solely because it is the only one the setting uses, without confirming it matches the primary diagnosis; if it does not, flag the gap.
- Do not fabricate norms; use published score-interpretation bands from instrument manuals or validation studies.

## Instructions

1. **Build the diagnostic-instrument map**: For each active diagnosis or primary symptom domain, identify the best-fit validated instrument. Use the reference table below as the anchor. Select a minimum of one primary instrument; secondary instruments are optional but recommended for comorbid presentations.

   | Symptom Domain | First-line Instrument | Alternative | Notes |
   |----------------|-----------------------|-------------|-------|
   | Depression | PHQ-9 (Kroenke et al., 2001) | BDI-II, QIDS-SR | PHQ-9 ≤ 4 = remission; MCID ≥ 5 |
   | Anxiety (generalized) | GAD-7 (Spitzer et al., 2006) | BAI, PSWQ | GAD-7 ≤ 4 = remission; MCID ≥ 4 |
   | PTSD | PCL-5 (Blevins et al., 2015) | IES-R, SPRINT | PCL-5 MCID ≥ 10; probable PTSD ≥ 31–33 |
   | Panic disorder | PDSS-SR | ACQ | PDSS-SR ≥ 8 = clinical range |
   | OCD | OCI-R (Foa et al., 2002) | Y-BOCS-SR | OCI-R ≥ 21 = clinical range; MCID ≈ 6 |
   | Alcohol use | AUDIT (Babor et al.) | AUDIT-C | ≥ 8 hazardous; ≥ 16 harmful; ≥ 20 dependence |
   | Substance use | DAST-10 | | Low ≥ 1; Moderate ≥ 3; Substantial ≥ 6 |
   | Social anxiety | LSAS-SR | SPS/SIAS | LSAS-SR ≥ 30 = clinical range |
   | Global distress | ORS (Miller & Duncan) | CORE-OM | ORS < 25 = clinical population; MCID ≥ 5 |
   | Alliance / session quality | SRS (Miller & Duncan) | WAI-SR | SRS < 36 = alliance concern |
   | Functional impairment | WHODAS 2.0 | SDS | SDS ≥ 5/10 per domain = impairment |
   | Mood / bipolar monitoring | MDQ (screening) | PHQ-9 modified | Screening only; not longitudinal monitoring tool |
   | Eating disorder | EDE-Q | EAT-26 | |
   | Child/adolescent depression | PHQ-A | CDI-2 | PHQ-A validated 11–17 yrs |
   | Child/adolescent anxiety | SCARED | MASC-2 | SCARED ≥ 25 = clinical range |

2. **Set the administration cadence**: Specify:
   - **Primary instrument**: frequency (every session recommended; minimum every 2–4 sessions).
   - **Secondary instruments**: frequency (can be less frequent; every 4–6 sessions for comorbid monitoring).
   - **Baseline**: administered at intake / session 1 before intervention begins.
   - **Progress check**: first formal trajectory review at session 4–6 (IOP: week 2; PHP: week 1).
   - **Episode-end**: final administration at last session to document outcome.
   - **Booster / follow-up**: if applicable (e.g., 3-month post-discharge check for IOP alumni).

3. **Define interpretation guidance**: For the primary instrument, write:
   - Severity bands (using published norms).
   - MCID (what constitutes meaningful change, not just noise).
   - Remission threshold (the score or range that indicates remission from a clinical standpoint).
   - Reliable change index (RCI) if available — the change needed to exceed measurement error.
   - Flag thresholds: scores that, if reached, trigger a safety review or step-up evaluation.

4. **Write the in-session review protocol**: A 3–5 minute structured exchange for reviewing the score with the client. Include:
   - Consent framing (session 1 only): brief rationale for why the measurement matters.
   - Score review script: how to present the score, situate it relative to baseline, and invite the client's reaction.
   - Discordance protocol: what to do when the score does not match the client's verbal report or the clinician's observation (explore, not dismiss).

5. **Build the decision-rule table**: Map score trajectories to clinical actions.

   | Trajectory Pattern | Definition | Clinical Action |
   |--------------------|------------|-----------------|
   | Early responder | ≥ MCID improvement by session 4–6 | Continue current plan; reinforce |
   | Adequate progress | Improvement trend; MCID not yet reached | Continue; note timeline |
   | Plateau — no deterioration | < MCID change over ≥ 4 sessions | Discuss trajectory; consider modality review |
   | Non-response | < MCID change by session 8 (or equivalent) | Formal plan review; consider reformulation |
   | Deterioration | ≥ 5-point increase (PHQ-9 / GAD-7) or ≥ 10-point PCL-5 increase | Same-session safety check; document; consider LOC step-up |
   | Reliable deterioration | Score crosses clinical range from below | Immediate clinical review; document; may require LOC or safety re-evaluation |
   | Remission | Score at or below remission threshold ≥ 3 consecutive administrations | Begin discharge planning; introduce relapse prevention |

6. **Define documentation standards**: Specify the format for recording MBC data in the progress note (SOAP, BIRP, DAP, or other). Minimum: instrument name + score + session number + clinical response.

7. **Run verification.**

## Output Format

```
=== MEASUREMENT-BASED CARE PLAN ===

CLIENT / EPISODE CONTEXT
Episode type: [Outpatient / IOP / PHP / Other]
Session frequency: [Weekly / 2×/week / Other]
Planned episode length: [e.g., 16 sessions / 8-week IOP]
Primary treatment target(s): [Problems being measured]

────────────────────────────────────────────────────────
INSTRUMENT SELECTION

Primary Instrument: [Name + brief citation]
  Symptom domain: [Depression / Anxiety / PTSD / etc.]
  Why selected for this presentation: [Diagnostic match, prior baseline if available, validated norms]
  Score range: [0–X]
  Severity bands: [Minimal / Mild / Moderate / Severe — with score cutoffs]
  Remission threshold: [Score ≤ X]
  MCID: [≥ X-point change = clinically meaningful]
  Safety flag threshold: [Score ≥ X → triggers safety review]

Secondary Instrument(s):
  1. [Name] — Domain: [___] — Rationale: [Why this comorbid domain needs separate monitoring]
     Severity bands / MCID: [...]
  2. [Name] — Domain: [___] — Rationale: [...]
  
Alliance / session quality (optional but recommended for alliance-rupture-prone presentations):
  SRS or equivalent — administered end of every session.

────────────────────────────────────────────────────────
ADMINISTRATION CADENCE

| Instrument | Baseline | Sessions 1–4 | Sessions 5–8 | Sessions 9+ | Episode End | Follow-up |
|------------|----------|--------------|--------------|-------------|-------------|-----------|
| [Primary]  | ✓ | Every session | Every session | Every session | ✓ | [Optional] |
| [Secondary]| ✓ | Every 4 sessions | Every 4 sessions | Every 4 sessions | ✓ | [Optional] |

First trajectory review: Session [4–6] — clinician and client review progress together.

────────────────────────────────────────────────────────
IN-SESSION REVIEW PROTOCOL

Consent framing (Session 1):
  "[Clinician script — 2–3 sentences explaining the rationale for routine measurement, framed as collaborative monitoring, not surveillance or report card.]"

Score review (every administration):
  "[Script: 'Your score today is [X]. Last session it was [Y], and your starting score was [Z].
  What stands out to you about that? Does that match how you have been feeling?']"

Discordance protocol (score and clinical picture disagree):
  "[Script and action — explore openly; consider session content, response bias, or instrument
  limitation before drawing a clinical conclusion.]"

────────────────────────────────────────────────────────
DECISION-RULE TABLE

| Trajectory | Definition (for this episode) | Clinical Action |
|------------|-------------------------------|-----------------|
| Early responder | ≥ [MCID] improvement by session [4–6] | Continue plan; reinforce mechanisms of change |
| Adequate progress | Improving trend; MCID not yet reached | Continue; document trend; note target date |
| Plateau | < [MCID] change over ≥ 4 sessions | Discuss with client; consider modality review |
| Non-response | < [MCID] by session 8 [or equivalent] | Formal plan review; consider reformulation prompt |
| Deterioration | ≥ [X]-point increase over 2 sessions | Safety check this session; document; consider LOC |
| Safety flag | Score ≥ [threshold] | Immediate safety assessment; do not defer |
| Remission | ≤ [threshold] × 3 consecutive assessments | Begin discharge / relapse-prevention planning |

────────────────────────────────────────────────────────
DOCUMENTATION STANDARD

Progress note format: [SOAP / BIRP / DAP / Other]
Required MBC line: "[Instrument]: score = [X] (baseline [X], session [N]); trajectory: [improving / plateauing / deteriorating]; clinical response: [action taken or no change indicated]."
Treatment plan link: Objective [#] — score serves as the measurement method for this objective.
Non-improving rule: If no MCID improvement by session 8, document: "[Date]: Non-response protocol activated. Plan review conducted. [Action recorded.]"
```

## Verification

- [ ] Primary instrument is validated for the primary diagnosis or symptom domain.
- [ ] Severity bands, MCID, and remission threshold documented for the primary instrument using published norms.
- [ ] Safety flag threshold specified for instruments with suicidality items (PHQ-9 item 9, PCL-5 item 9).
- [ ] Administration cadence specifies baseline, session-level frequency, episode-end, and optional follow-up.
- [ ] First trajectory review scheduled at session 4–6 (or equivalent).
- [ ] In-session review protocol includes consent framing, score review script, and discordance protocol.
- [ ] Decision-rule table covers: early responder, adequate progress, plateau, non-response, deterioration, safety flag, remission.
- [ ] Non-improving rule: defined as failure to reach MCID by session 8 (or equivalent); triggers plan review.
- [ ] Documentation standard specifies where in the note the score appears and links to the treatment plan objective.
- [ ] No instrument assigned without validation match to target domain.
- [ ] Missing inputs flagged with `[clinician input required]`.
