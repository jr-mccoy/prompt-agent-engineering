---
title: "CBT-I Adapted for Comorbid Pain or PTSD — Provider Protocol with Safety Carve-Outs"
category: psychology/specialty-clinical
description: "Generate a CBT-I session plan adapted for comorbid chronic pain or PTSD, with safety carve-out screening before sleep restriction, sleep-compression alternative, Imagery Rehearsal Therapy for nightmares, and prescriber coordination (e.g., prazosin)."
techniques:
  - ST-04
  - RT-02
  - DT-02
  - DS-02
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - CBT-I
  - insomnia
  - PTSD
  - chronic-pain
  - imagery-rehearsal-therapy
  - sleep-compression
  - safety-carve-outs
intended_use: model-testing
updated: "2026-06-08"
related_prompts:
  - domain-psychology/specialty-clinical/psychology_cbt_i_provider_sleep_protocol.md
  - domain-psychology/client-self-use/coping-by-concern/clientself_sleep_cbt_i_sleep_restriction_calculator.md
  - domain-psychology/treatment-planning/psychology_relapse_prevention_plan_designer.md
---

# CBT-I Adapted for Comorbid Pain or PTSD — Provider Protocol with Safety Carve-Outs

## Objective

Generate a CBT-I session plan adapted for insomnia comorbid with chronic pain or PTSD, anchored to manualized Cognitive Behavioral Therapy for Insomnia (Edinger & Carney; Perlis et al. behavioral/cognitive components — sleep restriction, stimulus control, cognitive therapy, sleep hygiene, relaxation) and modified for these populations: a gentler sleep-compression approach (gradual reduction of time-in-bed) rather than aggressive sleep restriction; stimulus control adapted for nighttime hypervigilance and nightmares; pre-sleep arousal reduction for pain-related muscle tension and PTSD hyperarousal; and, for trauma-related nightmares, Imagery Rehearsal Therapy (IRT; Krakow) with consideration of prescriber-managed prazosin. The plan front-loads safety carve-out screening because sleep restriction is contraindicated or requires modification in several conditions, and because sleep loss can destabilize mood and elevate suicide risk.

## When to Use

- DSM-5-TR Insomnia Disorder comorbid with chronic pain conditions or PTSD.
- Trauma-related nightmares warranting IRT alongside insomnia treatment.
- Clients whose pain- or trauma-driven pre-sleep arousal blunts standard CBT-I.
- Coordinated care where a prescriber manages pain medication or prazosin.
- Not appropriate to apply standard aggressive sleep restriction when an active safety carve-out is present (untreated obstructive sleep apnea, bipolar disorder, seizure disorder, occupational driving/heavy-machinery duties with daytime sleepiness, or sleep-loss-driven suicidality) until that condition is addressed or the protocol is modified.

## Inputs / Context

- Sleep diary data: time in bed (TIB), total sleep time (TST), sleep efficiency (SE), sleep-onset latency, WASO, awakenings.
- Comorbid driver: pain condition and current pain level/medication, or PTSD with nightmare frequency/content (non-graphic).
- Insomnia measure: Insomnia Severity Index (ISI); for PTSD, PCL-5 trajectory.
- Safety carve-out screen: OSA risk/diagnosis, bipolar disorder, seizure disorder, occupational sleepiness risk, current SI. `[clinician input required: results of the safety carve-out screen this session]`
- Nightmare status and whether IRT is indicated. `[clinician input required: nightmare frequency/distress and IRT readiness]`
- Prescriber coordination: prazosin, pain regimen, sedating medications. `[clinician input required: current medication coordination status]`

## Constraints

### Must

- Complete the safety carve-out screen BEFORE prescribing or adjusting any time-in-bed restriction: untreated OSA, bipolar disorder, seizure disorder, occupational driving/heavy-machinery duties, and significant daytime sleepiness must be screened and documented.
- Use sleep compression (gradual TIB reduction toward average TST) rather than aggressive single-step restriction in pain and PTSD populations; set a TIB floor (commonly not below ~5–5.5 hours) and titrate by sleep efficiency.
- Adapt stimulus control for hypervigilance and nightmares (e.g., grounded, safety-oriented out-of-bed plan) rather than mechanical "leave the bedroom" instructions that may heighten threat.
- Integrate Imagery Rehearsal Therapy when trauma-related nightmares are present and the client is ready; rescript and rehearse the nightmare, keeping content non-graphic.
- Address pre-sleep arousal directly: pain pacing and relaxation for pain; arousal-reduction and hyperarousal management for PTSD.
- Coordinate with the prescriber on prazosin, pain medication, and any sedating agents; do not advise medication changes.
- Screen suicide risk; if sleep loss is elevating SI, modify (do not intensify) restriction and escalate.

### Must Not

- Do not apply standard aggressive sleep restriction in the presence of an active safety carve-out.
- Do not reduce time in bed below the protocol floor or push restriction when daytime sleepiness creates a driving/occupational hazard.
- Do not deliver prolonged trauma-narrative exposure within this insomnia plan; IRT is rescripting/rehearsal, distinct from trauma-focused exposure therapy.
- Do not give pharmacologic instructions (prazosin dosing, pain-med changes) — route to the prescriber.
- Do not present this as generic CBT-I; the pain/PTSD adaptations and carve-outs are the point.
- Do not fabricate sleep-diary values, ISI/PCL-5 scores, or medication details — all from diary, measures, and records.

## Instructions

1. Review the sleep diary and compute TIB, TST, and sleep efficiency; review ISI (and PCL-5 if PTSD).
2. Run the safety carve-out screen (OSA, bipolar, seizure, occupational sleepiness) and the SI screen; document results before any TIB decision.
3. If a carve-out or sleep-loss-driven SI is present, branch: address/refer the carve-out, modify the plan, and follow the risk pathway as needed.
4. Set the prescribed TIB window using sleep compression toward average TST, respecting the TIB floor; titrate by sleep efficiency.
5. Specify adapted stimulus-control instructions tuned for hypervigilance/nightmares.
6. Build the pre-sleep arousal-reduction plan matched to the comorbid driver (pain pacing/relaxation, or PTSD arousal management).
7. If trauma-related nightmares are present and the client is ready, add an IRT step (rescript and rehearse the dream image, non-graphic).
8. Coordinate medication issues with the prescriber and assign homework (diary, adapted stimulus control, arousal-reduction practice, IRT rehearsal); document outcomes, risk, coordination, and billing.

## Output Format

```
=== CBT-I (PAIN/PTSD-ADAPTED) SESSION PLAN ===
Client: [Initials/MRN]    Session #: [N]    Date: [YYYY-MM-DD]    Comorbid driver: [Chronic pain / PTSD]
Dx: [Insomnia Disorder + (pain condition / PTSD)]    Prescriber: [name/contact]

SLEEP DIARY / MEASURES
- TIB: [h]   TST: [h]   Sleep efficiency: [%]   SOL: [min]   WASO: [min]   Awakenings: [n]
- ISI: [__]   PCL-5 (if PTSD): [__]   Nightmare frequency: [/week]

SAFETY CARVE-OUT SCREEN (complete BEFORE TIB decision)
- Untreated OSA risk/dx: [Y/N]   Bipolar disorder: [Y/N]   Seizure disorder: [Y/N]
- Occupational driving/heavy machinery + daytime sleepiness: [Y/N]
- Suicidal ideation (sleep-loss-driven?): [result]
- Carve-out present → action: [refer / modify / hold restriction]

TIB PRESCRIPTION (sleep compression)
- Prescribed TIB window: [bedtime–risetime]   TIB floor respected: [Y/N, ≥ ~5–5.5h]
- Titration rule: [advance/maintain by sleep efficiency threshold]

STIMULUS CONTROL (adapted for hypervigilance/nightmares)
- Out-of-bed plan: [grounded, safety-oriented]   Nightmare contingency: [...]

PRE-SLEEP AROUSAL REDUCTION
- Pain: [pacing / relaxation / wind-down]   PTSD: [arousal-reduction / grounding]

IMAGERY REHEARSAL THERAPY (if nightmares)
- Target nightmare (non-graphic): [theme]   Rescripted image: [...]   Rehearsal plan: [daily]

MEDICATION COORDINATION
- Prazosin: [prescriber-managed — status]   Pain regimen / sedatives: [coordination noted]

HOMEWORK
- Sleep diary: [continue]
- Adapted stimulus control: [specific]
- Arousal-reduction practice: [specific]
- IRT rehearsal: [if applicable]

OUTCOME / RISK / BILLING
- Sleep-efficiency trend: [...]   ISI/PCL-5 trajectory: [...]
- Risk status: [...]   Prescriber contact: [Y/N — detail]
- CPT: [90837 (60 min) / 96158 (health-behavior intervention, individual) if applicable]   Next focus: [...]
Clinician: ____________________  Supervisor (high acuity): ____________________
```

## Verification

- [ ] Safety carve-out screen (OSA, bipolar, seizure, occupational sleepiness) completed and documented before any TIB restriction decision.
- [ ] Sleep compression used with a documented TIB floor; titration tied to sleep efficiency.
- [ ] Stimulus control adapted for hypervigilance/nightmares rather than mechanical instructions.
- [ ] Pre-sleep arousal reduction matched to the pain or PTSD driver.
- [ ] IRT included (rescript + rehearsal, non-graphic) when trauma-related nightmares are present and client is ready.
- [ ] Prescriber coordination noted (prazosin / pain meds); no pharmacologic instructions given.
- [ ] SI screened; restriction modified (not intensified) and escalated if sleep loss is elevating risk.
- [ ] Plan reads as pain/PTSD-adapted CBT-I, not generic CBT-I.
- [ ] CPT code and supervisor co-sign (if high acuity) recorded.
- [ ] No fabricated diary values, ISI/PCL-5 scores, or medication details — all from diary, measures, and records.
