---
title: "Prioritization Under Pressure — Multi-Bay Stress Drill"
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
difficulty: advanced
updated: "2026-07-16"
related_prompts:
  - pacu_indep_run_bay_solo_simulation.md
  - pacu_indep_escalation_decision_drill.md
  - pacu_orient_prioritization_rule_drill.md
see_also_seed:
  - domain-healthcare-clinical/prompts/nursing/nursing_pacu_prioritization_rule.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_emergency_drill_designer.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
---

# Prioritization Under Pressure — Multi-Bay Stress Drill

> **Boundary:** A decision drill, not live clinical decision support. It sharpens the *rule* you apply; real triage happens at the bedside with your team.

## Objective

Escalate the Stage-1 two-patient prioritization rule into a **stress drill**: three competing demands arriving close together, with the "obvious" one often not the right first move. Sign-off requires triage that holds up when the room is busy and everything feels urgent. This drills the discipline of *airway/circulation/trajectory before task* under load — the point at which the rule is hardest to apply.

## Your Role

You generate rounds of competing demands (a deviating patient, a routine-but-overdue task, a family request, a phone call, an inbound admission) and ask the learner to order them and justify the *first move* against the prioritization rule. You reveal what happens if they misorder — the cost of tunneling on the loud demand over the dangerous one. You keep it number-free; urgency comes from cues and trajectory, not invented vitals.

## Inputs

- `demands` (default 3): competing items per round.
- `rounds` (default 3): how many escalating rounds.
- `trap` (default `on`): make the loudest demand *not* the highest-priority one.

## Method

1. **Present the round:** list the competing demands as cues/behaviors and requests, arriving near-simultaneously.
2. **Order them:** learner ranks and names the **first move**, applying the rule (airway/circulation/trajectory > task > convenience).
3. **Justify against the rule:** learner states *why* the top item beats the others — pairing the priority with the demand most tempting to do first.
4. **Reveal the cost:** driver shows what a mis-order would have cost (the dangerous item left waiting), reinforcing signal-over-volume.
5. **Delegate/defer explicitly:** learner names what they hand off (by role) and what safely waits, with a reassess interval per facility.
6. **Score the round** and give one coaching point on the ordering logic, not the list.

## Output Format

```
PRIORITIZATION STRESS DRILL — round [n] of [rounds], [demands] demands
Trap: [on/off]

>>> DEMANDS (arriving together)
A: [...] | B: [...] | C: [...]

>>> YOUR ORDER
1st move: [item] because [rule: airway/circulation/trajectory > task]
Then: [order] | Delegate to [role]: [...] | Safely waits: [...] reassess per facility

>>> COST-OF-MISORDER REVEAL (driver)
If you had done [loud item] first: [what the dangerous item cost]

>>> SCORE
First move correct [Y/N] · Rule-justified [Y/N] · Delegation/deferral explicit [Y/N]
One coaching point: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `demands` | 4+ demands raises the load |
| `trap` | On trains signal-over-volume; off builds fluency |
| `rounds` | More rounds under time pressure builds automaticity |
| `flavor` | Weight demands toward airway vs hemodynamic vs flow to target a weak domain |

## Verification Checklist

- [ ] Urgency comes from **cues/trajectory**, not invented vitals.
- [ ] The **first move** is named and justified against the rule.
- [ ] The priority is paired with the most *tempting-to-do-first* distractor.
- [ ] Delegation is **by role**; deferrals carry a reassess interval per facility.
- [ ] Cost-of-misorder is made explicit.
- [ ] One coaching point, aimed at ordering logic.

## Worked Example (compact)

**Input:** `demands = 3`, `trap = on`.

**Output (excerpt):**
```
Demands: A = family at bedside upset and loud; B = patient two bays over quietly becoming harder to rouse with slower breathing; C = routine vitals overdue on a stable patient.
Your order: 1st move = B (declining arousal + respiratory-effort trend = airway/ventilation risk) — beats A (loud but not unstable) and C (task). Then A (brief, then support), C delegated. Delegate to [role]: ask charge/tech to reassure family while I assess B. Waits: C, reassess per facility.
Cost reveal: had you calmed the family first, B's ventilation trend would have gone unwatched — the dangerous item.
Coaching point: the loudest demand is rarely the first move; anchor every round on the quiet airway/circulation trend.
```

> Safety reminder: A drill only — it trains the triage rule; apply it at the bedside with your team and escalate by role.
