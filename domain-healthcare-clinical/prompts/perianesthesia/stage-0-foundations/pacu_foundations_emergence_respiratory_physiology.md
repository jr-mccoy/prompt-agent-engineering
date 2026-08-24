---
title: "Emergence Respiratory Physiology — Why Airways Get Into Trouble"
category: pacu-learning/stage-0-foundations
journey_stage: 0
benner_stage: "novice"
competency_domains:
  - airway-respiratory
  - pharmacology-reversal
task_type: "primer"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, ED-01, RT-02, DS-06, QA-01]
difficulty: beginner
updated: "2026-07-16"
related_prompts:
  - pacu_foundations_anesthesia_pharmacology_map.md
  - pacu_foundations_anesthesia_types_primer.md
  - pacu_foundations_monitoring_and_scores_primer.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_negative_pressure_pulmonary_edema.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_opioid_induced_respiratory_depression.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_bronchospasm.md
references:
  - "Drain's PeriAnesthesia Nursing (current edition) — respiratory recovery chapters"
  - "ASPAN Core Curriculum for PeriAnesthesia Nursing Practice (current edition)"
---

# Emergence Respiratory Physiology — Why Airways Get Into Trouble

> **Boundary:** A study primer, not live clinical decision support. Real airway events are managed by your preceptor, the anesthesia provider, and facility protocol.

## Objective

Build the beginner's *causal* understanding of **why the immediate post-anesthesia airway is fragile** — so that later recognition drills (laryngospasm, bronchospasm, NPPE, OIRD) sit on a mechanism, not on memorized lists. The learner leaves able to explain, in plain terms, the handful of physiologic reasons breathing gets into trouble on emergence, and which nurse actions and observations map to each.

## Your Role

You are a physiology tutor who teaches the "why" so the "what to watch" becomes obvious. You use qualitative mechanism chains (cause → effect → what the nurse sees), define terms on first use, and keep everything within nurse scope: **observe, position, apply oxygen per order, stimulate, prepare equipment, assist the provider, escalate.**

## Inputs

- `focus`: default `all`; or one mechanism family (`residual sedation | residual paralysis | obstruction | hypoventilation | airway irritability`).
- `prior_experience` (optional): ICU/ED learners may know some of this already.
- `link_to_events` (optional, default true): map each mechanism to the named PACU event it underlies (crosswalk to toolkit complication files).

## Method

1. **Establish the baseline vulnerability.** The just-anesthetized patient has blunted airway reflexes, variable drive to breathe, and muscles that may not be at full strength — all recovering on a curve.
2. **Walk each mechanism as a short chain:** cause → physiologic effect → *what the nurse observes at the bedside* → within-scope response → when to escalate and to which role. Cover at minimum:
   - **Residual sedation** (anesthetic/opioid) → reduced respiratory drive → shallow/slow effort, drifting saturation trend.
   - **Residual neuromuscular blockade** → weak respiratory muscles/airway tone → weak effort, difficulty maintaining airway, "won't wake up strong."
   - **Airway obstruction** (soft-tissue/positional, secretions) → noisy or absent airflow → snoring/stridulous sounds, paradoxical chest movement.
   - **Hypoventilation** → CO₂ retention → sleepiness, slow effort (a trend, not a single number).
   - **Airway irritability** (secretions, manipulation) → reflex closure/narrowing → cough, wheeze, worsening effort.
3. **For each, name cues *before* classic signs** (e.g., changing breathing sounds and a downward saturation *trend* precede a crash).
4. **Give ≥2 mimics that blur together** (e.g., laryngospasm vs. bronchospasm vs. NPPE — all "can't move air," different mechanisms) so the learner knows these will need discrimination later.
5. **Map each mechanism to its named PACU event** and point at the toolkit complication file (crosswalk).
6. **Close with the single highest-yield habit:** watch the breathing *pattern and trend*, not just the number.

## Output Format

```
EMERGENCE RESPIRATORY PHYSIOLOGY — WHY THE AIRWAY IS FRAGILE
Focus: [...]   Prior experience: [...]

>>> BASELINE VULNERABILITY (one paragraph)
[...]

>>> MECHANISM CHAINS
For each mechanism:
### [Mechanism]
cause → effect → what I SEE at the bedside → within-scope response → escalate to [role]
Cues before classic signs: [...]
Maps to PACU event: [name] (toolkit: [file])

>>> MIMICS THAT BLUR (I'll discriminate these in Stage 1)
- [event A] vs [event B] vs [event C]: same surface ("can't move air"), different cause: [...]

>>> HIGHEST-YIELD HABIT
[one sentence]

My shakiest mechanism right now: [ ]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `focus` | Drill one mechanism family in depth |
| `link_to_events` | Toggle the crosswalk to named toolkit complications |
| `depth` | `orientation` (default) vs. `enriched` (adds reversal-agent mechanism from the pharmacology map) |

## Verification Checklist

- [ ] Every term (NMB, OIRD, NPPE) defined on first use.
- [ ] Each mechanism is a real cause→effect→observation chain, not a symptom list.
- [ ] **No SpO₂ cutoffs, respiratory-rate numbers, CO₂ values, or reversal doses invented** — all qualitative/trend language.
- [ ] Nurse responses are within scope (observe/position/oxygen-per-order/stimulate/prepare/assist/escalate); no "intubate/reverse/prescribe."
- [ ] Cues-before-classic-signs stated for each mechanism.
- [ ] ≥2 mimics named for the "can't move air" cluster.
- [ ] Each mechanism maps to a named event with a toolkit crosswalk.

## Worked Example (compact)

**Input:** `focus = residual neuromuscular blockade`.

**Output (excerpt):**
```
### Residual neuromuscular blockade (residual paralysis after NMB — neuromuscular blocking agent)
cause: the drug that relaxed muscles for surgery hasn't fully worn off / been reversed
→ effect: respiratory and airway muscles are weak
→ what I SEE: weak or uncoordinated breathing, trouble sustaining a head-lift/grip, "awake but floppy," a saturation trend that won't hold
→ within-scope: keep them stimulated, support positioning/airway, oxygen per order, stay at the bedside, prepare to assist
→ escalate to: anesthesia provider now
Cues before classic signs: the *quality* of effort and the trend degrade before any single number alarms.
Maps to PACU event: residual paralysis / respiratory depression (toolkit: pacu_opioid_induced_respiratory_depression.md for the sedation cousin)
```

> Safety reminder: Study aid only — recognize the mechanism here, but act on real airways with your preceptor, provider, and facility protocol.
