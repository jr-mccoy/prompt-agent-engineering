---
title: PACU Delayed Emergence / Failure to Wake — Recognition & Response
category: pacu/complications
task_type: LEARN
audience: PACU orientee (mid/late) or preceptor for huddle
updated: "2026-07-06"
tags:
  - pacu
  - delayed-emergence
  - failure-to-wake
  - neurologic
  - differential
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
  - pacu_emergence_agitation_deescalation.md
  - pacu_opioid_induced_respiratory_depression.md
  - pacu_hypothermia_shivering.md
  - pacu_red_flag_card.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — emergence and neurologic chapters
  - ASPAN Standards of Perianesthesia Nursing Practice
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice — neurologic module
---

# Delayed Emergence / Failure to Wake — PACU Deep Dive

> Safety reminder: Delayed emergence is a symptom, not a diagnosis — the job is a structured hunt for reversible causes while protecting the airway. All medications and reversal agents are per provider order; this prompt states no doses. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a structured deep dive on delayed emergence that gives the orientee a **systematic differential** (residual drug effect, metabolic, thermal, respiratory, neurologic) rather than defaulting to "still sleepy." Teaching goal: work the reversible-cause list before assuming a benign course.

## Inputs

- **Typical case mix / anesthesia types in your unit:** {{general/volatile, TIVA, neuraxial + sedation, high-opioid}}
- **Higher-risk populations:** {{older adults, renal/hepatic impairment, hypothyroid, diabetic}}
- **Source chapters:** {{Drain's emergence/neurologic chapters, ASPAN Core Curriculum}}

## Audience

- Orientee weeks 4–10 building a wake-up differential.
- Preceptor building a neurologic-emergency huddle.

## Output requirements

```markdown
# Delayed Emergence / Failure to Wake — PACU Deep Dive

> Safety reminder: Protect the airway; hunt reversible causes; escalate. Reversal agents per order.

## Why it matters
[One paragraph — most delayed emergence is residual drug effect and resolves, but a minority is a metabolic or neurologic emergency (hypoglycemia, stroke). The differential protects against anchoring on "just slow to wake."]

## Pathophysiology
[2–4 sentences: emergence depends on redistribution/elimination of anesthetics and opioids and on intact metabolic and neurologic function. Any of drug persistence, metabolic derangement, hypothermia, hypercarbia, or a CNS event can delay it.]

## First: protect and stabilize
- Airway patency, oxygenation, ventilation, hemodynamics — before working the differential.

## Structured differential (work the list)
| Category | What to check / consider |
|---|---|
| Residual anesthetic (volatile/propofol) | Time since agents off; trending lighter slowly |
| Residual opioid | Sedation + hypoventilation + pinpoint pupils; consider reversal per order |
| Residual neuromuscular blockade | Weak/uncoordinated; poor head-lift; breathing ineffective |
| Hypoglycemia | POC glucose per facility |
| Hypothermia | Measured temp; warm actively |
| Hypercarbia / hypoxia | RR/pattern, SpO₂, consider gas if ordered |
| Electrolyte (e.g., hyponatremia) | Labs if ordered; irrigation-fluid absorption context |
| Neurologic event (stroke) | Focal deficit, pupil asymmetry, new lateralizing signs → urgent |

## Early cues within the differential
- Focal or lateralizing signs, pupil asymmetry → escalate for possible neurologic event, don't wait.
- Sedation + shallow breathing + pinpoint pupils → opioid pattern.
- Cool patient, low temp → thermal contribution.

## Immediate management
1. Stabilize airway/oxygenation; stimulate; position → reassess in 1–2 min.
2. POC glucose and temperature per facility → act on reversible findings.
3. Notify {anesthesia provider by role}; prepare reversal agents per order if opioid/benzodiazepine/NMB pattern suspected → reassess after intervention.
4. Escalate urgently for any focal neurologic sign.

## Escalation
- Call {anesthesia provider by role} for failure to wake beyond expected window or any reversible cause you can't correct.
- Escalate urgently (rapid response / stroke pathway per facility) for focal deficit or pupil asymmetry.

## Pharm / equipment likely used
- Reversal agents per order (naloxone / flumazenil / sugammadex or neostigmine) — no dose here.
- POC glucose, warming, airway support equipment.

## After it resolves
- Continued neuro + respiratory monitoring; document cause found.
- Charting: differential worked, findings, interventions, response, escalation.
- Handoff: cause, current neuro baseline, monitoring window.

## Teaching pearls
- "Still sleepy" is a hypothesis, not a conclusion — check glucose, temp, and pupils every time.
- A focal deficit changes everything: that's a neurologic emergency, not slow emergence.

## Common orientee mistakes
- Waiting it out without checking glucose/temp/pupils.
- Missing a lateralizing sign because "post-op patients are groggy."

## Sources
- ...
```

## Must / Must not

**Must:**
- Stabilize airway/oxygenation before the differential.
- Provide a structured differential across drug/metabolic/thermal/respiratory/neurologic.
- Flag focal neurologic signs as an urgent, different pathway.
- Reversal agents per order.

**Must not:**
- No reversal/other doses — "per order."
- No invented lab thresholds or "expected wake-up" minute values.
- No scope creep; no facility pathway/pager invented.

## Quality signals

- Orientee checks glucose, temp, and pupils rather than waiting.
- Orientee recognizes a focal deficit as an emergency.

## Verification

- [ ] Airway/oxygenation stabilization precedes the differential.
- [ ] Differential spans drug, metabolic, thermal, respiratory, neurologic.
- [ ] Focal-deficit flagged as urgent separate pathway.
- [ ] Management steps have reassess intervals; escalation by role.
- [ ] Reversal agents per order; no doses.

## False-Positive Prevention

Do **not** fabricate or invent:

- **No reversal or other drug doses.** Per order only.
- **No invented lab thresholds or specific "normal wake-up time" values.** Describe qualitatively / "beyond expected window per provider."
- **No invented facility stroke-pathway criteria or pager paths.**
- **No fabricated chapter citations.** Mark `{{confirm}}`.
- **No scope creep** — provider-scope interventions deferred.

## Worked Example

<details>
<summary>Example: working the differential on a slow-to-wake patient (click to expand)</summary>

```markdown
## Structured differential (worked)

45 minutes after a general anesthetic, the patient still won't rouse to voice or light touch. Instead of waiting:

- Airway/oxygenation stable, SpO₂ good on O₂ — first priority confirmed.
- POC glucose per facility — low → treat per order; this may be the cause.
- Temp low → active warming per facility.
- Pupils equal, no focal weakness noted — reassuring against an acute neurologic event, but re-check.
- Notify the anesthesia provider by role with the findings; if an opioid pattern emerges, prepare reversal per order.
```

Notes: airway first; glucose/temp/pupils checked rather than waiting; reversible causes surfaced; escalation by role; no doses or thresholds invented.
</details>

## Self-check

- [ ] Stabilize-first, then structured differential.
- [ ] Drug/metabolic/thermal/respiratory/neurologic all covered.
- [ ] Focal deficit = urgent separate pathway.
- [ ] Reassess intervals + escalation by role.
- [ ] Reversal per order; no doses/thresholds invented.
- [ ] Safety reminder at top.
- [ ] Verification + False-Positive Prevention passed.
