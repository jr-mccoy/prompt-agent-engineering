---
title: "Emergency Rehearsal — Opioid-Induced Respiratory Depression & Naloxone-Assist, Nurse Role"
category: pacu-learning/stage-2-independence
journey_stage: 2
benner_stage: "competent"
competency_domains:
  - airway-respiratory
  - pharmacology-reversal
  - safety-escalation
task_type: "rehearsal"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, RP-02, RT-02, RT-05, DS-06, QA-01]
difficulty: advanced
updated: "2026-07-16"
related_prompts:
  - pacu_indep_emergency_response_rehearsal_airway.md
  - pacu_indep_escalation_decision_drill.md
  - pacu_orient_respiratory_event_recognition_drill.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_opioid_induced_respiratory_depression.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_drug_naloxone.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Drain's PeriAnesthesia Nursing (current edition)"
---

# Emergency Rehearsal — Opioid-Induced Respiratory Depression & Naloxone-Assist, Nurse Role

> **Boundary:** An emergency rehearsal, not live clinical decision support. Naloxone dosing, titration, and re-dose timing are **per order / per facility protocol** — paste your unit's material; this rehearses *your role*, not the orders.

## Objective

Rehearse **recognizing opioid-induced respiratory depression (OIRD) early and executing the nurse's escalation-and-naloxone-assist role** — the most common serious PACU respiratory event. The learner practices catching the sedation-plus-hypoventilation trend before frank apnea, stimulating and supporting ventilation, escalating, and preparing/administering reversal *per order*, then watching for re-sedation. Because naloxone is short-acting relative to some opioids, the *reassess-and-re-dose-per-order* discipline is the point of the drill.

## Your Role

You present an over-sedated, hypoventilating patient and drive the response. You coach recognize → stimulate/support → escalate → prepare/administer reversal per order → watch for renarcotization, holding scope (the nurse recognizes, supports ventilation in scope, escalates, and administers naloxone *per order/protocol* — not by inventing a dose). You supply no numbers; reversal is "per order," reassess intervals "per facility."

## Inputs

- `context` (optional): the opioid exposure context (multimodal, neuraxial opioid, etc.) — categories only.
- `trajectory` (default `progressive`): `early` (rising sedation) or `progressive` (toward apnea).
- `facility_protocol` (paste): the unit's naloxone/reversal and monitoring protocol location.

## Method

1. **Present the trend:** increasing sedation with declining respiratory rate/effort and rising end-tidal or falling saturation trend — cues before apnea.
2. **Discriminate:** OIRD vs residual anesthetic vs hypercarbia-from-splinting vs other causes (≥2 mimics) — enough to act while escalating.
3. **Stimulate + support ventilation in scope:** rouse, position, coach breathing, apply O2/positive-pressure support per protocol.
4. **Escalate** by role and prepare reversal *per order* — parallel, not sequential.
5. **Administer naloxone per order/protocol** (learner pastes the order; no dose stated here), titrating to respiratory effort per order.
6. **Watch for renarcotization:** name the reassess interval per facility and the re-dose-per-order plan, since reversal may outlast less than the opioid; score and give one coaching point (usually the re-sedation watch or the early catch).

## Output Format

```
OIRD REHEARSAL — context [...], trajectory [early/progressive]
Facility protocol pasted: [location / yes-no]

>>> TREND (I present)
[rising sedation + declining RR/effort + sat/EtCO2 trend — cues before apnea]

>>> DISCRIMINATION
OIRD leads because [...] vs mimic [A] vs mimic [B]

>>> SUPPORT + ESCALATE (parallel)
Stimulate/position/coach · O2/positive-pressure per protocol | Escalate to [role] | Prepare reversal per order

>>> REVERSAL (per order)
Administer naloxone per order/protocol · titrate to respiratory effort per order

>>> RE-SEDATION WATCH
Reassess per facility · re-dose per order if effort declines again

>>> SCORE
Caught trend early [Y/N] · Support + escalate parallel [Y/N] · Reversal per order not invented [Y/N] · Named renarcotization watch [Y/N]
One coaching point: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `trajectory` | `early` trains the pre-apnea catch; `progressive` trains the full response |
| `context` | Neuraxial-opioid context trains a longer re-sedation watch |
| `mimic_pressure` | Add residual-anesthetic cues to sharpen discrimination |
| `renarcotization` | Force a second dip to drill the re-dose-per-order habit |

## Verification Checklist

- [ ] Recognition uses the **sedation + hypoventilation trend**, before apnea.
- [ ] ≥2 mimics discriminated.
- [ ] Ventilation support + escalation run **in parallel**.
- [ ] Naloxone/reversal is **per order / per facility protocol** — no invented dose or timing.
- [ ] **Renarcotization watch** named with a reassess interval "per facility" and re-dose-per-order plan.
- [ ] Scope-safe throughout; one coaching point.

## Worked Example (compact)

**Input:** `context = multimodal with opioid`, `trajectory = progressive`.

**Output (excerpt):**
```
Trend: patient increasingly hard to rouse, breaths slower and shallower, saturation trend easing down after comfort was treated.
Discrimination: OIRD leads (sedation + hypoventilation after opioid) vs residual anesthetic (would expect global slow emergence, less isolated respiratory) vs splinting/hypercarbia.
Support + escalate: stimulate, position, coach breathing, O2/positive-pressure per protocol — while escalating to provider by role and preparing reversal per order.
Reversal: administer naloxone per order/protocol, titrate to effort per order.
Re-sedation watch: reassess per facility; re-dose per order if effort declines again since reversal may not outlast the opioid.
Coaching point: strong early catch — make the renarcotization watch explicit out loud so the next nurse keeps it after handoff.
```

> Safety reminder: A rehearsal only — recognize and support in scope, escalate by role, and give reversal strictly per order/protocol. Naloxone can wear off before the opioid; keep watching.
