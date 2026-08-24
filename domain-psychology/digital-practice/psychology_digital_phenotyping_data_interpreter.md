---
title: "Digital Phenotyping Data Interpreter"
category: psychology/digital-practice
description: "Interpret passive and app-collected behavioral data (sleep, mobility/GPS, phone-use, typing dynamics, actigraphy, EMA self-report) into hypothesis-generating clinical signal requiring clinical correlation — never diagnosis — with baseline/deviation logic, false-positive sources, consent/privacy, and clinician-outreach triggers."
techniques:
  - DS-02
  - AG-02
  - DT-01
  - CM-02
  - QA-04
difficulty: advanced
intended_use: model-testing
tags:
  - digital-phenotyping
  - passive-sensing
  - EMA
  - actigraphy
  - hypothesis-generating
  - clinical-correlation
  - privacy
  - digital-practice
updated: "2026-06-08"
related_prompts:
  - domain-psychology/digital-practice/psychology_ai_augmented_practice_ops_design.md
  - domain-psychology/treatment-planning/psychology_measurement_based_care_plan.md
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
  - domain-psychology/digital-practice/psychology_telemental_health_program_design.md
---

# Digital Phenotyping Data Interpreter

## Objective

Translate passive and app-collected behavioral data streams — sleep, mobility/GPS, phone/communication use, typing dynamics, actigraphy, and ecological momentary assessment (EMA) self-report — into **hypothesis-generating clinical signal** that a clinician correlates with the clinical picture. The interpreter maps each stream to candidate constructs, distinguishes baseline from clinically meaningful deviation, names the false-positive sources that could explain a signal, specifies consent/privacy handling, and defines what triggers clinician outreach. The output is explicitly **not a diagnosis and not an automated clinical action**: passive data is decision-support that requires clinical correlation, and the licensed clinician retains decision authority. This implements the digital-phenotyping framework (e.g., Torous and colleagues) and EMA methodology.

## When to Use

- When a practice or research program collects passive-sensing or EMA data and needs a principled way to interpret it without overreaching into diagnosis.
- When designing the rule set that decides which data patterns warrant clinician review versus normal variation.
- When a measurement-based-care program adds passive/EMA streams alongside validated instruments and needs interpretation guardrails.
- When reviewing a digital-phenotyping vendor's "risk scores" critically — to separate genuine signal from artifact and to ensure a human clinician, not the algorithm, makes clinical decisions.
- When establishing consent, privacy, and outreach protocols before passive data collection begins.

## Inputs / Context Required

- **Data streams available**: which of sleep, mobility/GPS, phone/communication use, typing dynamics, actigraphy, EMA are collected, and at what sampling rate.
- **Baseline window**: how much per-client baseline data exists (passive data is only interpretable relative to the individual's own baseline).
- **Clinical context**: working diagnosis/formulation, current treatment targets, known risk history.
- **Client's life context**: work schedule, travel, caregiving, physical illness, life events that confound passive signals.
- **Consent status**: what the client consented to collect, how it is used, and who sees it.
- **Outreach capacity**: who reviews flagged signals and how quickly (the human-in-the-loop responder).
- `[clinician input required: the formulation and any specific behaviors this client's relapse signature is known to involve]`
- `[clinician input required: confounders specific to this client (e.g., shift work, recent move, medical condition affecting sleep/mobility)]`

## Constraints

### Must

- Frame all output as **hypothesis-generating signal requiring clinical correlation** — never as a diagnosis, a risk score acted on autonomously, or a standalone clinical conclusion.
- Interpret every stream **relative to the individual's own baseline**, not population norms alone; require an adequate baseline window before flagging deviations.
- For each candidate signal, enumerate **false-positive / confound sources** (life events, travel, illness, device/sensor artifact, missing data) that could explain the pattern non-clinically.
- Keep the **clinician as decision authority**: passive data triggers human review, not automated outreach, clinical messaging, or risk classification.
- Define **clinician-outreach triggers** with a detection-to-response expectation, and route any deterioration/suicidality signal to the human escalation ladder (clinician this week / today / 988 / 911-ED); state that passive channels are NOT crisis-monitoring or emergency channels and must not be relied upon to detect imminent risk in real time.
- Address **consent and privacy**: what is collected, the sensitivity of location/communication data, data minimization, retention, and the client's ability to pause/withdraw.
- Distinguish **signal from missingness**: treat large gaps in data as an interpretive limitation (and possibly itself a behavioral signal) rather than as reassurance.

### Must Not

- Do not output a diagnosis, a probability of a disorder, or a risk category presented as a clinical determination.
- Do not infer mental states from a single stream or a single day; require convergent, sustained deviation across streams and time.
- Do not treat passive monitoring as a substitute for direct risk assessment or as a reliable real-time crisis-detection system.
- Do not ignore confounds; every flagged signal must list plausible non-clinical explanations.
- Do not over-interpret location/communication data in ways that exceed consent or stigmatize ordinary behavior.
- Do not fabricate effect sizes or cite specific predictive accuracies as established; mark such claims as `[verify in literature for this population]`.

## Instructions

1. **Map streams to candidate constructs.** For each collected stream, state the construct(s) it may index and the directional pattern of interest. Use the reference table as the anchor — these are *candidate associations*, not deterministic rules.

   | Data stream | Candidate construct | Pattern of interest (relative to baseline) | Primary confounds |
   |-------------|--------------------|--------------------------------------------|-------------------|
   | Mobility / GPS (radius, locations, entropy) | Behavioral activation; withdrawal | ↓ radius/entropy, fewer unique locations → possible withdrawal/depressive episode | Travel, weather, illness, schedule change, holidays |
   | Sleep / actigraphy | Sleep disruption; circadian regulation | Fragmentation, ↑/↓ duration, phase shift → possible mood/anxiety change | Shift work, new baby, medical issues, device non-wear |
   | Circadian regularity | Mood stability | Disrupted/irregular rhythm → possible mood instability | Travel/jet lag, work schedule, life events |
   | Phone / communication use | Social engagement | ↓ outgoing calls/messages, ↓ social-app contact → possible social withdrawal | Phone change, vacation, relationship context |
   | Screen / app use | Activation; rumination/avoidance | Marked ↑ passive use late-night → possible rumination/avoidance | Normal habit variation, work use |
   | Typing dynamics | Psychomotor change; cognitive load | Slowed/erratic typing, error rate → possible psychomotor slowing | Device, fatigue, multitasking |
   | EMA self-report | Momentary affect, symptoms, context | Rising negative-affect ratings, context-linked spikes | Response fatigue, reactivity, missing entries |

2. **Establish baseline and deviation logic.** State the minimum baseline window required before interpretation; define what constitutes a clinically meaningful deviation (sustained, cross-stream, beyond the client's normal variability), and require **convergence** — a single stream's wobble is noise; a coherent pattern across streams and time is signal worth reviewing.

3. **Run the false-positive screen.** For any flagged pattern, list the plausible non-clinical explanations (the confound column) and require they be considered before treating the pattern as clinical signal. Explicitly handle **device/sensor artifact** and **missing data** as alternative explanations.

4. **Integrate, don't isolate.** Combine passive streams with EMA and with the clinician's formulation. Map patterns to this client's known relapse signature (from inputs). Note that convergent signals (e.g., mobility ↓ + sleep fragmentation + EMA negative-affect rise) are more informative than any single stream.

5. **Define clinician-outreach triggers and SLAs.** Specify which signal patterns prompt the clinician to reach out, who reviews, and the detection-to-review timeframe. State the boundary clearly: passive monitoring **flags for human review**; it is not a real-time crisis-detection system. If a deterioration or suicidality-related signal appears, route to the human escalation ladder.

   | Signal pattern | Interpretation (hypothesis) | Action |
   |----------------|-----------------------------|--------|
   | Sustained cross-stream withdrawal + sleep disruption | Possible emerging depressive episode | Clinician review within review window; outreach to assess |
   | EMA negative-affect rise + reduced social contact | Possible deterioration | Clinician outreach this week; assess directly |
   | EMA item endorsing hopelessness / passive ideation | Risk signal — needs direct assessment | Clinician same-day review; conduct direct risk assessment (e.g., C-SSRS); ladder: today / 988 / 911-ED |
   | Large data gap during known high-risk period | Interpretive limitation + possible disengagement | Clinician outreach; do not interpret silence as safety |

6. **Specify consent, privacy, and data governance.** State what is collected and why; emphasize the sensitivity of GPS and communication metadata; apply data minimization and retention limits; describe how the client can pause/withdraw; and confirm collection operates under appropriate privacy/HIPAA safeguards (and a BAA where a third-party platform is used).

7. **Write the interpretation summary.** Produce a clinician-facing summary that states hypotheses (not conclusions), the supporting streams, the competing confounds, and the recommended human action — always preserving clinical correlation as the final step.

8. **Run verification.**

## Output Format

```
=== DIGITAL PHENOTYPING SIGNAL INTERPRETATION ===
(Hypothesis-generating only — requires clinical correlation. NOT a diagnosis.
 NOT a real-time crisis-detection system. Clinician retains decision authority.)

CLIENT / DATA CONTEXT
Streams collected: [sleep / mobility / phone-use / typing / actigraphy / EMA]
Baseline window available: [___]  Working formulation: [___]
Known relapse signature: [clinician input required: ...]
Client confounds: [clinician input required: shift work / travel / medical ...]

────────────────────────────────────────────────────────
1. STREAM → CONSTRUCT MAP (candidate associations)
| Stream | Candidate construct | Observed pattern vs baseline | Confounds to rule out |
| [stream] | [construct] | [deviation] | [confounds] |

────────────────────────────────────────────────────────
2. BASELINE & DEVIATION LOGIC
Minimum baseline: [___]
Meaningful deviation = sustained + cross-stream + beyond client's normal variability.
Convergence required: single-stream change = noise; coherent multi-stream pattern = reviewable signal.

────────────────────────────────────────────────────────
3. FALSE-POSITIVE / CONFOUND SCREEN
Flagged pattern: [___]
Plausible non-clinical explanations: [life event / travel / illness / device artifact / missing data]
Resolved? [Y/N — basis]

────────────────────────────────────────────────────────
4. INTEGRATED HYPOTHESES (passive + EMA + formulation)
Hypothesis 1: [___] — supporting streams: [___] — competing explanation: [___]
Hypothesis 2: [___] ...

────────────────────────────────────────────────────────
5. CLINICIAN-OUTREACH TRIGGERS  (flags for human review; not auto-action)
| Signal pattern | Hypothesis | Action + review SLA |
| [pattern] | [hypothesis] | [clinician review within ___] |
Risk signal handling: direct human assessment; ladder = clinician this week / today / 988 / 911-ED.
Passive channels are NOT crisis-monitoring or emergency channels.
Data gap rule: silence is NOT reassurance.

────────────────────────────────────────────────────────
6. CONSENT / PRIVACY / GOVERNANCE
Collected: [streams] for [purpose] | Sensitivity flagged: [GPS / communications]
Data minimization + retention: [___] | Client pause/withdraw: [how]
Platform BAA (if third-party): [Y/N]

────────────────────────────────────────────────────────
7. CLINICIAN-FACING SUMMARY
Hypotheses (not conclusions): [___]
Supporting signal: [___] | Competing confounds: [___]
Recommended human action: [___] — final step is clinical correlation by the clinician.
```

## Verification

- [ ] Every interpretation is framed as hypothesis-generating signal requiring clinical correlation; no diagnosis or autonomous risk classification.
- [ ] Each stream is interpreted relative to the client's own baseline, with an adequate baseline window required.
- [ ] Convergence across streams/time required before a pattern is treated as signal; single-stream/single-day wobble treated as noise.
- [ ] Every flagged pattern lists false-positive/confound sources, including device artifact and missing data.
- [ ] Clinician retains decision authority; passive data flags for human review, never triggers automated clinical action or outreach.
- [ ] Outreach triggers include a review SLA; risk signals route to direct human assessment with the this-week/today/988/911-ED ladder.
- [ ] Stated explicitly that passive monitoring is not a real-time crisis-detection or emergency channel.
- [ ] Data gaps treated as an interpretive limitation, not as reassurance.
- [ ] Consent, privacy (esp. GPS/communications), data minimization, retention, and withdrawal addressed; BAA noted for third-party platforms.
- [ ] Predictive-accuracy/effect-size claims flagged `[verify in literature for this population]` rather than asserted.
- [ ] Missing inputs flagged with `[clinician input required]`.
```
