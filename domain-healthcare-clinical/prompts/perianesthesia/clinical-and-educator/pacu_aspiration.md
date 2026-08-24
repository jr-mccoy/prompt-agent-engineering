---
title: PACU Pulmonary Aspiration — Recognition & Response
category: pacu/complications
task_type: LEARN
audience: PACU orientee (mid/late) or preceptor for huddle
updated: "2026-07-06"
tags:
  - pacu
  - aspiration
  - airway
  - respiratory
  - emergency
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - pacu_complication_deep_dive.md
  - pacu_bronchospasm.md
  - pacu_negative_pressure_pulmonary_edema.md
  - pacu_emergence_agitation_deescalation.md
  - pacu_red_flag_card.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — respiratory and airway chapters
  - ASPAN Standards of Perianesthesia Nursing Practice
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice — respiratory module
---

# Pulmonary Aspiration — PACU Deep Dive

> Safety reminder: Aspiration risk peaks around emergence when airway reflexes are not yet fully restored. Positioning and suction to protect the airway are immediate nursing actions; advanced airway management is per provider. This prompt states no doses. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a structured deep dive on peri-operative pulmonary aspiration that teaches risk recognition, the difference between witnessed and silent aspiration, and the immediate airway-protective response — while distinguishing it from bronchospasm and NPPE.

## Inputs

- **Higher-risk populations/cases in your unit:** {{emergency surgery, obesity, pregnancy, GERD, bowel obstruction, difficult airway, impaired consciousness}}
- **Source chapters:** {{Drain's respiratory/airway chapters, ASPAN Core Curriculum}}

## Audience

- Orientee weeks 4–10 recovering higher-risk airway patients.
- Preceptor building an airway-emergency huddle.

## Output requirements

```markdown
# Pulmonary Aspiration — PACU Deep Dive

> Safety reminder: Protect the airway (position + suction), oxygenate, escalate. Advanced management per provider.

## Why it matters
[One paragraph — aspiration can cause acute hypoxemia, chemical pneumonitis, and later infection; the emergence window is high-risk because protective reflexes lag consciousness.]

## Pathophysiology
[2–4 sentences: gastric/oropharyngeal contents enter the airway when protective reflexes are blunted; acidic/particulate material injures the airway and alveoli, causing bronchospasm, atelectasis, and inflammatory injury.]

## Risk / setup (who and when)
- Full stomach, emergency/urgent surgery, obesity, pregnancy, GERD, bowel obstruction, difficult airway, depressed consciousness, active PONV with impaired airway control.

## Early cues (witnessed AND silent)
- Witnessed: regurgitation/vomitus in the airway or mouth around emergence.
- Silent: new cough, wheeze, tachypnea, desaturation, or laryngospasm/bronchospasm without an obvious vomiting event.
- New respiratory distress in a high-risk patient = consider aspiration.

## Classic signs
- Coughing, wheeze/crackles, desaturation, tachypnea, increased work of breathing; possible fever later.

## Differential — what else looks like this?
| Mimic | How to tell them apart |
|---|---|
| Bronchospasm (non-aspiration) | Wheeze without aspiration event; trigger/history differs |
| NPPE | Follows airway obstruction; frothy transudate rather than gastric content |
| Pulmonary edema / overload | Fluid context; no aspiration event |
| Pre-existing pulmonary disease flare | Baseline history |

## Immediate management
1. Position to protect the airway (head down / lateral per position and surgical constraints); suction the airway → reassess continuously.
2. Apply O₂ per order; support ventilation as needed → reassess in 1–2 min.
3. Notify {anesthesia provider by role} immediately; prepare for possible bronchodilator/advanced airway per order → reassess after intervention.
4. Do not force oral intake; keep NPO pending provider.

## Escalation
- Call {anesthesia provider by role} for any suspected aspiration event or new post-op respiratory distress in a high-risk patient.
- Rapid response / code per facility for refractory hypoxemia or airway compromise.

## Pharm / equipment likely used
- Suction, supplemental O₂, airway/BVM equipment.
- Bronchodilator or other agents if ordered (per order — no dose here).

## After it resolves
- Continued respiratory monitoring (delayed pneumonitis possible) → interval per facility/provider.
- Charting: event/risk, findings, airway-protective actions, response, escalation.
- Handoff: aspiration concern + monitoring window + NPO status.

## Teaching pearls
- Silent aspiration is real — new distress in a high-risk patient counts even without visible vomitus.
- Position and suction first to protect the airway; then oxygenate and escalate.

## Common orientee mistakes
- Waiting for visible vomitus before considering aspiration.
- Sitting a vomiting, obtunded patient upright without protecting the airway/suctioning.

## Sources
- ...
```

## Must / Must not

**Must:**
- Distinguish witnessed vs silent aspiration.
- Lead management with airway protection (position + suction).
- Differentiate from bronchospasm and NPPE.
- Emphasize emergence as the high-risk window.

**Must not:**
- No bronchodilator/other doses — "per order."
- No invented incidence statistics or SpO₂ thresholds.
- No scope creep — advanced airway is provider-scope ("prepare and assist").
- No facility-specific protocol/pager invented.

## Quality signals

- Orientee considers silent aspiration in a high-risk patient.
- Orientee protects the airway before other steps.

## Verification

- [ ] Witnessed vs silent aspiration distinguished.
- [ ] Airway protection (position + suction) leads management.
- [ ] Differential ≥ 2 mimics (incl. bronchospasm, NPPE).
- [ ] Management steps have reassess intervals; escalation by role.
- [ ] No doses/thresholds invented.

## False-Positive Prevention

Do **not** fabricate or invent:

- **No drug doses.** Per order only.
- **No invented incidence statistics or numeric SpO₂/RR thresholds.** Describe qualitatively.
- **No invented facility protocols or pager paths.**
- **No fabricated chapter citations.** Mark `{{confirm}}`.
- **No scope creep** — advanced airway remains provider-scope.

## Worked Example

<details>
<summary>Example: silent aspiration in a high-risk patient (click to expand)</summary>

```markdown
## Early cues (silent aspiration)

An obese patient after urgent surgery, emerging, has no visible vomiting — but over two minutes develops a new cough, audible wheeze, and SpO₂ drifting into the low 90s.

- No visible vomitus does not rule out aspiration in a high-risk patient. Treat the new distress as possible aspiration.
- Position to protect the airway and suction, apply O₂ per order, and call the anesthesia provider by role. Keep NPO. Reassess continuously and prepare to assist if advanced airway management is needed.
```

Notes: silent aspiration recognized; airway protected first; escalation by role; NPO maintained; no doses/thresholds invented.
</details>

## Self-check

- [ ] Witnessed vs silent taught.
- [ ] Airway protection leads.
- [ ] Differential ≥ 2 mimics.
- [ ] Reassess intervals + escalation by role.
- [ ] No invented doses/thresholds/facility specifics.
- [ ] Safety reminder at top.
- [ ] Verification + False-Positive Prevention passed.
