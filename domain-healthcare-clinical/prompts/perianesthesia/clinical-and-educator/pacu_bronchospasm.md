---
title: PACU Bronchospasm — Recognition & Response
category: pacu/complications
task_type: LEARN
audience: PACU orientee (mid/late) or preceptor for huddle
updated: "2026-07-06"
tags:
  - pacu
  - bronchospasm
  - airway
  - respiratory
  - wheeze
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
  - pacu_aspiration.md
  - pacu_negative_pressure_pulmonary_edema.md
  - pacu_emergency_drill_designer.md
  - pacu_red_flag_card.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — respiratory and airway chapters
  - ASPAN Standards of Perianesthesia Nursing Practice
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice — respiratory module
---

# Bronchospasm — PACU Deep Dive

> Safety reminder: Bronchospasm can be a stand-alone event or the first sign of anaphylaxis — always check for the other anaphylaxis signs. Bronchodilators and all pharmacology are per provider order; this prompt states no doses. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a structured deep dive on post-op bronchospasm that teaches recognition (expiratory wheeze, prolonged expiration, work of breathing), the must-not-miss link to anaphylaxis, and the difference from laryngospasm, aspiration, and NPPE.

## Inputs

- **Higher-risk patients in your unit:** {{asthma/COPD, reactive airways, recent URI, smokers, airway manipulation, known allergies}}
- **Source chapters:** {{Drain's respiratory/airway chapters, ASPAN Core Curriculum}}

## Audience

- Orientee weeks 4–10 recovering airway/reactive-airway patients.
- Preceptor building a respiratory-emergency huddle.

## Output requirements

```markdown
# Bronchospasm — PACU Deep Dive

> Safety reminder: Oxygenate, remove trigger, bronchodilator per order, escalate. Rule anaphylaxis in or out.

## Why it matters
[One paragraph — lower-airway narrowing impairs ventilation and oxygenation; may be transient and reversible or the herald of anaphylaxis; recognition drives fast escalation.]

## Pathophysiology
[2–4 sentences: bronchial smooth-muscle constriction (± mucosal edema/secretions) narrows lower airways, increasing expiratory resistance → wheeze, prolonged expiration, air trapping, and (if ventilated) rising peak airway pressures.]

## Triggers / setup
- Airway manipulation/secretions, reactive airways (asthma/COPD), recent URI, aspiration, histamine-releasing drugs, allergic reaction/anaphylaxis, cold/dry gases.

## Early cues
- New expiratory wheeze, prolonged expiratory phase, chest tightness/cough.
- Rising work of breathing; on a ventilated patient, rising peak inspiratory pressures.
- Desaturation is a later sign.

## Classic signs
- Diffuse expiratory wheeze, prolonged expiration, accessory-muscle use, hypoxemia; may progress to a "silent chest" (ominous — air movement too poor to wheeze).

## Differential — what else looks like this?
| Mimic | How to tell them apart |
|---|---|
| Laryngospasm | Upper-airway stridor (inspiratory), not expiratory wheeze; peri-extubation |
| Anaphylaxis | Wheeze + urticaria/flushing/angioedema/hypotension → treat as anaphylaxis |
| Aspiration | Aspiration event/risk; may have crackles + wheeze |
| NPPE | Follows obstruction; frothy transudate |

## Immediate management
1. Apply/increase O₂ per order; sit upright per position order → reassess in 1 min.
2. Remove/treat trigger where possible (secretions, suspected allergen) → reassess continuously.
3. Notify {anesthesia provider by role}; prepare bronchodilator per order → reassess after administration.
4. **Screen for anaphylaxis** (skin, airway swelling, hypotension); if present, escalate as anaphylaxis per facility.

## Escalation
- Call {anesthesia provider by role} for new significant wheeze/work of breathing.
- Rapid response / code per facility for severe distress, silent chest, or anaphylaxis features.

## Pharm / equipment likely used
- Supplemental O₂, bronchodilator (per order — no dose here), suction.
- Anaphylaxis medications per order/protocol if that pathway is triggered.

## After it resolves
- Continued respiratory monitoring; watch for recurrence → interval per facility/provider.
- Charting: onset, trigger, interventions, response, anaphylaxis screen, escalation.
- Handoff: event + monitoring window + any suspected allergen.

## Teaching pearls
- Expiratory wheeze = lower airway (bronchospasm); inspiratory stridor = upper airway (laryngospasm).
- A "silent chest" in a distressed patient is worse, not better — escalate urgently.
- Always ask "is this anaphylaxis?" when a patient wheezes.

## Common orientee mistakes
- Missing anaphylaxis by treating the wheeze in isolation.
- Reassurance when a wheezing patient goes quiet (silent chest).

## Sources
- ...
```

## Must / Must not

**Must:**
- Distinguish expiratory wheeze (bronchospasm) from inspiratory stridor (laryngospasm).
- Force an anaphylaxis screen on any bronchospasm.
- Flag "silent chest" as ominous.
- Bronchodilators per order.

**Must not:**
- No bronchodilator/anaphylaxis drug doses — "per order/protocol."
- No invented incidence statistics or numeric thresholds.
- No scope creep; no facility-specific protocol/pager invented.

## Quality signals

- Orientee screens for anaphylaxis on every wheeze.
- Orientee escalates a silent chest urgently rather than relaxing.

## Verification

- [ ] Expiratory-wheeze vs inspiratory-stridor distinction present.
- [ ] Anaphylaxis screen built into management.
- [ ] Silent chest flagged as ominous.
- [ ] Differential ≥ 2 mimics; management steps have reassess intervals.
- [ ] Bronchodilator per order; no doses.

## False-Positive Prevention

Do **not** fabricate or invent:

- **No bronchodilator or anaphylaxis drug doses.** Per order/protocol only.
- **No invented incidence statistics or numeric SpO₂/pressure thresholds.** Describe qualitatively.
- **No invented facility protocols or pager paths.**
- **No fabricated chapter citations.** Mark `{{confirm}}`.
- **No scope creep** — provider-scope airway interventions deferred.

## Worked Example

<details>
<summary>Example: is this bronchospasm or anaphylaxis? (click to expand)</summary>

```markdown
## Immediate management (with anaphylaxis screen)

A patient with an asthma history develops a new diffuse expiratory wheeze and rising work of breathing 15 minutes into recovery.

- Apply O₂ per order, sit them up, and call the anesthesia provider by role; prepare a bronchodilator per order.
- Screen for anaphylaxis before settling on "just bronchospasm": any new flushing, hives, lip/tongue swelling, or a drop in blood pressure? If yes → escalate as anaphylaxis per facility, not as isolated wheeze.
- If the chest goes quiet while distress worsens (silent chest), escalate urgently — that's less air movement, not improvement.
```

Notes: upper-vs-lower airway framing; anaphylaxis screen forced; silent chest flagged; bronchodilator per order; escalation by role; no doses invented.
</details>

## Self-check

- [ ] Expiratory wheeze vs inspiratory stridor taught.
- [ ] Anaphylaxis screen in management.
- [ ] Silent chest flagged.
- [ ] Differential ≥ 2 mimics; reassess intervals + escalation by role.
- [ ] Bronchodilator per order; no doses invented.
- [ ] Safety reminder at top.
- [ ] Verification + False-Positive Prevention passed.
