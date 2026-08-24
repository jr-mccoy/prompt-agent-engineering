---
title: "Deteriorating Patient — Progressive-Disclosure Integrative Walkthrough"
category: pacu-learning/stage-2-independence
journey_stage: 2
benner_stage: "competent"
competency_domains:
  - safety-escalation
  - cardiovascular-hemodynamic
  - airway-respiratory
  - assessment-scoring
task_type: "drill"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, RT-02, RT-05, DS-06, QA-04, QA-01]
difficulty: advanced
updated: "2026-07-16"
related_prompts:
  - pacu_indep_escalation_decision_drill.md
  - pacu_indep_run_bay_solo_simulation.md
  - pacu_orient_recovery_deviation_script_builder.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_complication_deep_dive.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_last_recognition_response.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Drain's PeriAnesthesia Nursing (current edition)"
---

# Deteriorating Patient — Progressive-Disclosure Integrative Walkthrough

> **Boundary:** A reasoning walkthrough, not live clinical decision support. It rehearses *how you think* as a patient declines; real deterioration is managed at the bedside with your team.

## Objective

Run a **multi-system deterioration case** that reveals one clue at a time, so the learner practices integrating cues across domains (respiratory + hemodynamic + neuro) instead of pattern-matching a single complication. Approaching independence means recognizing that a patient going the wrong way often crosses systems — and acting *early on the trend* rather than waiting for a classic picture. This drills that integration and the "escalate before it's obvious" instinct.

## Your Role

You reveal the case in stages, giving only cues/behaviors at each step. You force the learner to reason *before* the next clue drops — hypothesis, action, reassess — then reveal whether the trend continued. You keep ≥2 competing explanations alive across systems so the learner cannot anchor early. Everything is scope-safe and number-free; values are "per facility." You reward early trend-recognition, not late certainty.

## Inputs

- `case_seed` (optional): surgery/anesthesia/comorbidity category to build the decline around.
- `stages` (default 4): how many reveals.
- `crossing` (default `on`): make the deterioration cross ≥2 systems.

## Method

1. **Open with a plausibly-stable patient** (cues only), then reveal a first subtle drift.
2. **Reason before the next reveal:** learner names the leading hypothesis *and* ≥2 mimics across systems, an in-scope action, and what they'll reassess (interval per facility).
3. **Reveal the trend:** driver shows whether the drift continued or resolved, adding one new cross-system cue.
4. **Force the escalation decision:** at each stage the learner states escalate-now / watch-and-reassess / routine, with the trigger that would flip it.
5. **Converge:** once the trend is unmistakable, learner states the within-scope bundle (position, O2, monitor, prepare/assist per order) and the escalate-to-role call — noting they should have escalated on the *trend*, not the certainty.
6. **Debrief the reasoning arc** and give one coaching point on the earliest missed escalation window.

## Output Format

```
DETERIORATION WALKTHROUGH — [stages] stages, crossing [on/off]
Case: [category]

>>> STAGE 1 (cues only)
[...]
Hypothesis: [top] vs mimic A [system] vs mimic B [system] | Action (in scope): [...] | Escalate? [now/watch/routine] + flip-trigger: [...] | Reassess per facility

>>> STAGE 2..n (reveal + new cross-system cue)
[trend continued?] [new cue]
[updated hypothesis / action / escalation]

>>> CONVERGENCE
Within-scope bundle: [...] | Escalate to [role] | Earliest window I should have escalated: [stage]

>>> SCORE
Integrated across systems [Y/N] · ≥2 mimics held [Y/N] · Escalated on trend not certainty [Y/N]
One coaching point: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `crossing` | On trains cross-system integration; off is a single-system drill |
| `stages` | More stages = more reassess-and-adjust reps |
| `resolve_early` | Occasionally let it resolve to punish over-escalation-by-reflex |
| `case_seed` | Target a comorbidity mix the learner finds hard |

## Verification Checklist

- [ ] Case revealed **one clue at a time**; learner reasons before each reveal.
- [ ] ≥2 mimics held **across systems** at each stage.
- [ ] Escalation decision (now/watch/routine) named each stage with a **flip-trigger**.
- [ ] **No invented vitals** — cues/trends/behaviors; values "per facility."
- [ ] Debrief identifies the **earliest** appropriate escalation window.
- [ ] One coaching point on the reasoning arc.

## Worked Example (compact)

**Input:** `case_seed = major abdominal, general, older adult`, `stages = 3`, `crossing = on`.

**Output (excerpt):**
```
Stage 1: quiet, slightly cool, comfort okay; then subtly less responsive to voice.
Reason: hypothesis = residual sedation vs early hypoperfusion (hemodynamic) vs hypoventilation-hypercarbia (respiratory). Action: stimulate, O2, monitor closely. Escalate? watch + flip-trigger = any further arousal drop or effort change. Reassess per facility.
Stage 2 reveal: arousal keeps drifting down AND skin is cooler/mottled — cross-system. Now hypoperfusion leads. Escalate? now → escalate to provider; continue support in scope.
Convergence: position, O2, monitor, prepare/assist per order, escalate to [role]. Earliest window: end of Stage 1, on the combined arousal + perfusion drift.
Coaching point: you integrated well by Stage 2 — next time let the *combination* of two small drifts trigger escalation a stage earlier.
```

> Safety reminder: A reasoning drill only — practice the integration here; manage real deterioration at the bedside and escalate by role, early.
