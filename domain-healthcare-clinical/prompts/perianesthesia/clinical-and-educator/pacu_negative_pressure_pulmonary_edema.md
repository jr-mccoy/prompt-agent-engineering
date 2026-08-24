---
title: PACU Negative-Pressure Pulmonary Edema (NPPE) — Recognition & Response
category: pacu/complications
task_type: LEARN
audience: PACU orientee (mid/late) or preceptor for huddle
updated: "2026-07-06"
tags:
  - pacu
  - NPPE
  - pulmonary-edema
  - airway-obstruction
  - respiratory
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: advanced
related_prompts:
  - pacu_complication_deep_dive.md
  - pacu_bronchospasm.md
  - pacu_aspiration.md
  - pacu_opioid_induced_respiratory_depression.md
  - pacu_red_flag_card.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — respiratory chapters
  - ASPAN Standards of Perianesthesia Nursing Practice
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice — respiratory module
---

# Negative-Pressure Pulmonary Edema (NPPE) — PACU Deep Dive

> Safety reminder: NPPE typically follows an airway-obstruction event (often laryngospasm or biting the tube). Recognition, oxygen support, and escalation are the nursing priorities; diuretics and advanced support are per provider order. This prompt states no doses. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a structured deep dive on NPPE — pulmonary edema caused by forced inspiration against an obstructed airway. The teaching goal is recognizing that a patient who *just* had a relieved airway obstruction and is now desaturating with pink frothy sputum has NPPE, not simple fluid overload.

## Inputs

- **Triggering context in your unit:** {{post-extubation laryngospasm | biting the ETT on emergence | upper-airway obstruction | OSA }}
- **Source chapters:** {{Drain's respiratory chapters, ASPAN Core Curriculum respiratory module}}

## Audience

- Orientee weeks 4–10 who recovers airway/emergence patients.
- Preceptor building a respiratory-emergency huddle.

## Output requirements

```markdown
# Negative-Pressure Pulmonary Edema (NPPE) — PACU Deep Dive

> Safety reminder: Support oxygenation and escalate; pharmacologic and advanced airway management per order.

## Why it matters
[One paragraph — often dramatic and frightening but frequently self-limited with support; the danger is mistaking it for something else or under-supporting oxygenation. Frequently follows laryngospasm.]

## Pathophysiology
[2–4 sentences: forced inspiration against a closed/obstructed glottis generates large negative intrathoracic pressure → increased venous return and pulmonary capillary transmural pressure → fluid transudates into the alveoli. Type 1 follows acute obstruction; Type 2 follows relief of chronic obstruction.]

## Setup (who and when)
- Minutes after a relieved airway obstruction (laryngospasm, biting the tube, upper-airway obstruction).
- Young, muscular patients can generate especially large negative pressures.

## Early cues (before florid edema)
- Falling SpO₂ shortly after an obstruction event was "resolved."
- Tachypnea, increasing work of breathing, restlessness.
- Cough, then frothy/pink-tinged sputum.

## Classic signs
- Pink frothy secretions, diffuse crackles, hypoxemia, dyspnea, often bilateral.

## Differential — what else looks like this?
| Mimic | How to tell them apart |
|---|---|
| Volume overload / TACO | No preceding obstruction event; slower onset; fluid-balance context |
| Aspiration | Aspiration event/risk; may be more focal; different history |
| Cardiogenic pulmonary edema | Cardiac history/signs; NPPE follows an airway event in a often-healthy patient |
| Bronchospasm | Wheeze/prolonged expiration dominate; not frothy transudate |

## Immediate management
1. Sit the patient up (per position order); apply high-flow O₂ per order → reassess in 1–2 min.
2. Support ventilation; anticipate CPAP/PEEP or positive-pressure support per order → reassess continuously.
3. Notify {anesthesia provider by role} immediately; prepare for possible diuretic or advanced support per order → reassess after intervention.
4. Keep the airway patent; be ready to assist provider if re-intubation is considered.

## Escalation
- Call {anesthesia provider by role} for any new post-obstruction desaturation with frothy sputum.
- Rapid response / code per facility for refractory hypoxemia.

## Pharm / equipment likely used
- Supplemental O₂, CPAP/PEEP equipment, suction.
- Diuretic if ordered (per order — no dose here).

## After it resolves
- Continued respiratory monitoring; NPPE often improves over hours with support → interval per facility.
- Charting: obstruction event, onset, interventions, response, escalation.
- Handoff: flag NPPE + monitoring window.

## Teaching pearls
- Obstruction event + new frothy desaturation = think NPPE before "fluid overload."
- Often self-limited *with* support — but oxygenation support and escalation are not optional.

## Common orientee mistakes
- Calling it fluid overload and reaching for a diuretic mindset before escalating.
- Under-supporting oxygenation while waiting.

## Sources
- ...
```

## Must / Must not

**Must:**
- Tie onset to a preceding airway-obstruction event.
- Put falling SpO₂ / frothy sputum cues before "florid edema."
- Differentiate from TACO/fluid overload, aspiration, cardiogenic edema, bronchospasm.
- Nurse role: position, oxygenate, escalate, assist.

**Must not:**
- No diuretic or other doses — "per order."
- No invented incidence statistics or SpO₂ cutoffs.
- No scope-creep (no nurse-initiated re-intubation; "assist provider").
- No facility-specific equipment/pager invented.

## Quality signals

- Orientee links a just-resolved obstruction to new desaturation and names NPPE.
- Orientee escalates and supports oxygenation rather than defaulting to "overload."

## Verification

- [ ] Onset tied to preceding obstruction event.
- [ ] Early cues (desaturation, frothy sputum) before florid signs.
- [ ] Differential ≥ 2 mimics (incl. TACO/overload).
- [ ] Management steps have reassess intervals.
- [ ] Escalation by role; pharmacology per order.

## False-Positive Prevention

Do **not** fabricate or invent:

- **No diuretic/drug doses.** Per order only.
- **No invented incidence statistics or numeric SpO₂ thresholds.** Describe qualitatively.
- **No invented facility equipment specifics or pager paths.**
- **No fabricated chapter citations.** Mark `{{confirm}}`.
- **No scope creep** — re-intubation is provider-scope ("prepare and assist").

## Worked Example

<details>
<summary>Example: "Early cues" after a post-extubation laryngospasm (click to expand)</summary>

```markdown
## Early cues (before florid edema)

A healthy 24-year-old had brief laryngospasm on emergence that was broken by the anesthesia team. Five minutes later in PACU his SpO₂ drifts to the low 90s, he's breathing fast and looks anxious, and you hear a wet cough with pink-tinged froth.

- Recent obstruction (laryngospasm) + new desaturation + frothy sputum = think NPPE, not "he's just wet from fluids."
- Sit him up per order, apply high-flow O₂ per order, call the anesthesia provider by role, and prepare for CPAP/positive-pressure support. Reassess continuously.
```

Notes: obstruction-then-edema pattern recognized; oxygenation supported; escalation by role; no doses invented; provider-scope actions deferred.
</details>

## Self-check

- [ ] Obstruction-then-edema pattern taught.
- [ ] Cues before florid signs.
- [ ] Differential ≥ 2 mimics.
- [ ] Reassess intervals present.
- [ ] Escalation by role; pharmacology per order.
- [ ] No invented doses/thresholds/facility specifics.
- [ ] Safety reminder at top.
- [ ] Verification + False-Positive Prevention passed.
