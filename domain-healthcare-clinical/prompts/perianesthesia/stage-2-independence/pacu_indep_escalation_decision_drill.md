---
title: "Escalate / Watch / Routine — Escalation-Decision Drill"
category: pacu-learning/stage-2-independence
journey_stage: 2
benner_stage: "competent"
competency_domains:
  - safety-escalation
  - assessment-scoring
  - professional-role-leadership
task_type: "drill"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, RT-02, RT-05, DS-06, QA-04, QA-01]
difficulty: intermediate
updated: "2026-07-16"
related_prompts:
  - pacu_indep_deteriorating_patient_walkthrough.md
  - pacu_indep_two_patient_prioritization_stress_drill.md
  - pacu_orient_hemodynamic_event_recognition_drill.md
see_also_seed:
  - domain-healthcare-clinical/prompts/nursing/nursing_sbar_clinical_escalation.md
see_also_toolkit:
  - domain-image-generation/healthcare/pacu_escalation_who_to_call_meta.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
---

# Escalate / Watch / Routine — Escalation-Decision Drill

> **Boundary:** A decision drill, not live clinical decision support. It trains the *judgment* of when to escalate; the real call is made at the bedside with your team.

## Objective

Drill the three-way call the near-independent nurse must make dozens of times a shift: **escalate now / watch-and-reassess / routine.** Independence is not "escalate everything" or "handle everything alone" — it is calibrated escalation with a clear trigger and a defined watch window. This drills the middle ground (watch-and-reassess) most, because that is where undertriage and overtriage both live.

## Your Role

You present short vignettes as cues/trajectories and ask the learner to classify each escalate/watch/routine, name the escalate-to-role and the SBAR headline they'd give, and — for "watch" — the *flip-trigger and reassess interval* that converts a watch into an escalation. You reveal the cost of miscalling in either direction. Everything is number-free; the decision rides on trend and reversibility, not invented vitals.

## Inputs

- `count` (default 5): vignettes per set.
- `mix` (default `balanced`): weight toward `watch` cases to drill the hard middle, or spread across all three.
- `domain_focus` (optional): airway / hemodynamic / neuro / comfort to target a weak area.

## Method

1. **Present a vignette** in cues/trajectory (one recovering patient, a change or a request).
2. **Classify:** learner calls escalate-now / watch / routine.
3. **Justify by trend + reversibility:** learner states the reasoning, holding the most plausible *opposite* call as a check (why not the tier above/below).
4. **For escalate:** name the role and a one-line SBAR headline. **For watch:** name the flip-trigger (what would escalate it) and the reassess interval per facility. **For routine:** name what keeps it routine.
5. **Reveal the cost** of the wrong tier (undertriage delay vs overtriage noise/credibility).
6. **Score the set** and give one coaching point on the direction the learner miscalibrates (usually over- or under-escalating consistently).

## Output Format

```
ESCALATION-DECISION DRILL — [count] vignettes, mix [balanced/watch-heavy]

>>> VIGNETTE [n]
[cues/trajectory or request]
Call: [escalate / watch / routine]
Why (trend + reversibility): [...] | Opposite-call check: not [tier] because [...]
If escalate → role: [...] SBAR headline: [...]
If watch → flip-trigger: [...] reassess per facility
If routine → stays routine because: [...]

>>> COST REVEAL
Wrong tier would have: [undertriage delay / overtriage cost]

>>> SET SCORE
Correct tier: [n/count] · Flip-triggers defined on all watches [Y/N]
One coaching point (miscalibration direction): [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `mix` | `watch-heavy` drills the ambiguous middle |
| `domain_focus` | Target airway / hemodynamic / neuro / comfort |
| `credibility_mode` | Add a recently-cried-wolf frame to train precise SBAR |
| `count` | Longer sets build calibration data across a session |

## Verification Checklist

- [ ] Each call is justified by **trend + reversibility**, with an opposite-call check.
- [ ] Every **watch** carries a flip-trigger and a reassess interval "per facility."
- [ ] Every **escalate** carries a role + a one-line SBAR headline.
- [ ] Decisions ride on **cues/trajectory**, not invented vitals.
- [ ] Cost of miscalling is made explicit in both directions.
- [ ] One coaching point naming the miscalibration direction.

## Worked Example (compact)

**Input:** `count = 1`, `mix = watch-heavy`, `domain_focus = hemodynamic`.

**Output (excerpt):**
```
Vignette: post-op patient's blood pressure trending up over two checks, awake, comfortable, no other change.
Call: watch. Why: isolated upward BP trend, reversible causes likely (pain/anxiety/bladder), no end-organ or airway signs — not escalate yet. Opposite-call check: not routine because it's a trend not a one-off; not escalate because no danger signs.
Watch → flip-trigger: further rise, new symptom (headache, chest, neuro change), or no response to comfort measures → escalate to provider. Reassess per facility.
Cost reveal: escalating now = noise/credibility cost; ignoring as routine = missing a climbing trend.
Coaching point: your tiering was right — you tend to under-define flip-triggers; always attach the specific thing that would flip a watch.
```

> Safety reminder: A drill only — it calibrates escalation judgment; make real calls at the bedside and escalate by role whenever in doubt.
