---
title: PACU Complication Deep Dive
category: pacu/complications
task_type: LEARN
audience: PACU orientee (late-orientation) or preceptor for huddle
updated: "2026-04-16"
tags:
  - pacu
  - complication
  - deep-dive
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - ../../domain-healthcare-clinical/prompts/medicine_adverse_event_analyzer.md
  - ../../domain-healthcare-clinical/prompts/nursing_sbar_clinical_escalation.md
  - prompts/pacu_topic_primer.md
  - prompts/pacu_red_flag_card.md
  - prompts/pacu_simulation_scenario_builder.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
  - ASPAN Standards of Perianesthesia Nursing Practice
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
---

# PACU Complication Deep Dive

> Safety reminder: Educational reference — clinical judgment, facility protocol, and provider orders govern real-time decisions.

## Objective

Produce a structured deep dive on a single post-op complication, suitable for huddle teaching or late-orientation review. Covers pathophysiology → early cues → differential → management → escalation → post-event documentation.

## Inputs

- **Complication:** {{e.g., residual neuromuscular blockade, post-spinal hypotension, emergence delirium, laryngospasm, PONV escalation}}
- **Patient populations most at risk in your unit:** {{…}}
- **Source chapters:** {{…}}

## Audience

- Orientee in weeks 4–8 who has seen the complication once or twice.
- Or a preceptor preparing a 20-minute huddle topic.

## Output requirements

```markdown
# {Complication} — PACU Deep Dive

> Safety reminder: Educational aid only — verify every intervention against facility protocol.

## Why it matters
[One paragraph — incidence context from source; typical severity on the PACU continuum.]

## Pathophysiology
[2–4 sentences; mechanism level, not full textbook recap.]

## Early cues (what you see *before* the classic signs)
- ...
- ...
- ...

## Classic signs
- ...

## Differential — what else looks like this?
| Mimic | How to tell them apart |
|---|---|
| ... | ... |

## Immediate management
1. ...
2. ...
3. ... (include reassess-in-X interval)

## Escalation
- Call {role} when: ...
- Call {role} when: ...
- Rapid response / code criteria: per facility

## Pharm / equipment likely used
- Agent(s): ...
- Reversal: ...
- Equipment: ... (bag-mask, succs, etc. — generic)

## After it resolves
- Reassessment schedule: ...
- Charting: event, action, response, escalation.
- Handoff note to next caregiver: ...

## Teaching pearls
- ...
- ...

## Common orientee mistakes
- ...

## Sources
- ...
```

## Must / Must not

**Must:**
- "Early cues" section **before** "Classic signs" — teaches pattern recognition.
- Differential table with ≥ 2 mimics.
- Each management step names a reassessment interval.
- Every escalation row has a role.

**Must not:**
- No invented doses; reversal agents named by generic class, specific doses *per order*.
- No facility-specific equipment or paging paths.
- No chronology that implies the nurse is acting outside scope ("intubate the patient" — reframe as "prepare equipment and assist provider").

## Quality signals

- Orientee can name 3 early cues they would not have looked for before.
- Differential prevents anchoring on the first thing seen.
- Escalation is concrete.

## Verification

Before returning, verify:

- [ ] Pathophysiology section is 2–4 sentences and accurate at the mechanism level (not textbook-expanded).
- [ ] Every early cue is observable at the bedside without waiting for alarms.
- [ ] Differential table has ≥ 2 mimics with distinguishing features that can be checked without a new consult.
- [ ] Every management step names a reassess-in-X interval.
- [ ] No step instructs the nurse outside scope (no "intubate the patient"; reframe as "prepare equipment and assist provider").
- [ ] Every escalation row names a role, not a name or pager.

## False-Positive Prevention

Do **not** fabricate or invent:

- **No invented doses.** Reversal agents and adjuncts named by generic class only; specific doses stated as "per order" or with a source citation.
- **No invented vital-sign thresholds or SpO₂ cutoffs** unless the source chapter supplies them. If not in source, describe qualitatively ("desaturation trend," "persistent hypotension").
- **No invented equipment specifics** (syringe size, tubing brand, circuit model). Use generic terms.
- **No invented facility-specific escalation pathways, pager numbers, or rapid response criteria** — state "per facility protocol."
- **No invented incidence statistics** ("occurs in 7% of cases"). If the source does not give a number, describe qualitatively ("uncommon but high-consequence").
- **No fabricated chapter citations.** If unknown, mark `{{confirm chapter in Drain's / Core Curriculum}}`.
- **No implied scope creep.** Nurses assist providers; they do not perform provider-scope interventions in this prompt's output.

## Worked Example

<details>
<summary>Example: Complication = "Residual Neuromuscular Blockade" (click to expand, abbreviated)</summary>

```markdown
# Residual Neuromuscular Blockade — PACU Deep Dive

> Safety reminder: Educational aid only — verify every intervention against facility protocol.

## Why it matters
One of the most common post-op respiratory events on PACU arrival. Even partial residual paralysis degrades airway protection, tidal volume, and cough — all before SpO₂ numbers fall.

## Pathophysiology
Non-depolarizing agents (rocuronium, vecuronium) bind post-synaptic nicotinic receptors at the neuromuscular junction. Reversal (neostigmine + glycopyrrolate, or sugammadex for steroidal agents) competes or chelates the agent. Incomplete reversal leaves a fraction of receptors blocked — the patient looks awake but cannot sustain head-lift or full tidal volume.

## Early cues (before the classic signs)
- Shallow, rapid breathing that looks "fine" on the pulse-ox but the tidal-volume numbers are low.
- Uncoordinated swallow; drool on chin.
- Can open eyes on command but cannot sustain.

## Classic signs
- Sustained head-lift < 5 seconds.
- Diaphoresis, air hunger.
- SpO₂ drift (late sign).

## Differential — what else looks like this?
| Mimic | How to tell them apart |
|---|---|
| Over-sedation from opioid | Pupils pinpoint; responds less to cue; sustained head-lift if you can rouse them |
| Hypoventilation from residual volatile | Slowly lightens; not responsive to reversal agent |
| Post-op delirium / emergence agitation | Movement is large, not weak; coordination present |

## Immediate management
1. Elevate head of bed (per position order) → reassess in 1 min.
2. Coach deep breaths / cough; support airway → reassess in 2 min.
3. Notify CRNA or anesthesiologist by role; prepare reversal agent per provider order → reassess in 5 min after administration.

## Escalation
- Call CRNA when: head-lift < 5 sec persists after reposition and coaching.
- Call anesthesiologist on call when: desaturation with labored breathing or new bradycardia.
- Rapid response / code criteria: per facility.

## Pharm / equipment likely used
- Agent(s) commonly implicated: rocuronium, vecuronium (generic names only; specific doses per order).
- Reversal: neostigmine + glycopyrrolate, or sugammadex (per order).
- Equipment: bag-valve-mask, suction, reversal agents drawn per pharmacy.

## After it resolves
- Reassessment schedule: VS + head-lift + ability to take deep breath every 15 min × 4, then per facility.
- Charting: event, intervention, response, escalation path.
- Handoff note: flag residual-blockade history + reversal timing for receiving unit.

## Teaching pearls
- SpO₂ is a late indicator — watch tidal volume and work of breathing first.
- Reversal timing is surgery + patient specific; do not assume "fully reversed" at OR exit.

## Common orientee mistakes
- Waiting for the SpO₂ alarm before escalating.
- Attributing shallow breathing to "just tired after surgery" without testing head-lift.

## Sources
- *Drain's PeriAnesthesia Nursing*, Ch. on Neuromuscular Blockade & Reversal
- ASPAN *Core Curriculum* — airway & respiratory module
```

Notes: early cues precede classic signs, every management step has a reassess interval, escalation is by role, no specific mg doses invented, reversal named by class with "per order" qualifier.
</details>

## Self-check

- [ ] Early cues come before classic signs.
- [ ] Differential has ≥ 2 mimics with distinguishing features.
- [ ] Management steps have reassess intervals.
- [ ] Escalation names role + trigger.
- [ ] "Common orientee mistakes" has ≥ 2 items.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed — no invented doses, thresholds, equipment, citations, or scope-creep instructions.
