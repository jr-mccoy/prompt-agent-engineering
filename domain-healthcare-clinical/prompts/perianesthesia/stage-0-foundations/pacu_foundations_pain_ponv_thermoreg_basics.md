---
title: "Comfort Basics — Pain, PONV, and Thermoregulation at a Beginner Level"
category: pacu-learning/stage-0-foundations
journey_stage: 0
benner_stage: "novice"
competency_domains:
  - pain-comfort
  - nausea-ponv
  - thermoregulation
task_type: "primer"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, ED-02, RT-02, DS-06, QA-01]
difficulty: beginner
updated: "2026-07-16"
related_prompts:
  - pacu_foundations_hemodynamics_of_emergence.md
  - pacu_foundations_monitoring_and_scores_primer.md
  - pacu_foundations_anesthesia_types_primer.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_hypothermia_shivering.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_drug_antiemetics_reference.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_drug_analgesics_reference.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition) — comfort/PONV/normothermia"
  - "Drain's PeriAnesthesia Nursing (current edition)"
---

# Comfort Basics — Pain, PONV, and Thermoregulation

> **Boundary:** A study primer, not live clinical decision support. Real comfort management follows your preceptor, provider order, and facility protocol.

## Objective

Introduce the three "comfort" domains a PACU nurse manages constantly — **pain**, **PONV** (post-operative nausea and vomiting), and **thermoregulation** (mostly hypothermia/shivering on emergence) — at a level a beginner can act on: what each is, why it happens post-op, how the nurse assesses and responds within scope, and how the three interact.

## Your Role

You are a primer author making three linked domains concrete and connected. For each you give the "why post-op," the *assessment approach* (including non-verbal cues, since patients emerge unable to report clearly), within-scope responses, and escalation. You keep it qualitative — **no pain-score cutoffs, temperatures, or antiemetic doses** — and you highlight how the three feed each other.

## Inputs

- `domains`: default all three; or one to focus.
- `patient_note` (optional): populations where these differ (e.g., peds can't self-report; elderly lose heat faster).
- `show_interactions` (default true): teach how pain↔PONV↔temperature interact.

## Method

1. **Pain:** why post-op pain varies (surgical site, anesthesia type, residual analgesia); how to assess when the patient can't clearly self-report (behavioral/physiologic cues before a stated score); within-scope response (comfort measures, positioning, analgesia *per order*, reassess); escalate when the plan isn't working.
2. **PONV:** why it's common post-anesthesia; cues (pallor, swallowing, retching precede vomiting — cues before the classic sign); within-scope response (positioning for airway protection, antiemetic *per order*, reassess); escalate for persistent PONV or airway concern.
3. **Thermoregulation:** why patients arrive cool and shiver; consequences (shivering raises oxygen demand, worsens pain and BP); within-scope response (warming *per facility*, reassess); escalate per protocol.
4. **Cues-before-classic-signs** for each; **≥2 mimics** where relevant (e.g., shivering vs. rigors vs. emergence tremor; nausea vs. anxiety vs. hypotension).
5. **Show the interactions:** pain drives BP and nausea; hypothermia worsens pain and shivering; treating one often eases another.
6. **Close with the single habit:** assess comfort *actively and repeatedly* — the emerging patient can't always tell you.

## Output Format

```
COMFORT BASICS — PAIN / PONV / THERMOREGULATION
Domains: [...]   Patient note: [...]

For each domain:
### [Domain] (acronym defined)
- Why it happens post-op: [...]
- How I assess (cues before classic signs, incl. non-verbal): [...]
- Within-scope response (per order / per facility): [...]
- Escalate to [role] when: [...]
- Mimics: [A] vs [B]

>>> HOW THE THREE INTERACT
[short diagram/paragraph: pain ↔ PONV ↔ temperature]

>>> THE ONE HABIT
[one sentence]

Domain I feel least ready to assess: [ ]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `domains` | Focus one comfort domain |
| `patient_note` | Population overlays (peds/geri) |
| `show_interactions` | Toggle the cross-domain interaction map |

## Verification Checklist

- [ ] PONV and any acronym defined on first use.
- [ ] **No pain-score thresholds, temperatures, or antiemetic/analgesic doses invented** — all "per order / per facility."
- [ ] Assessment includes non-verbal cues (patient may not self-report).
- [ ] Cues-before-classic-signs stated per domain; ≥2 mimics where relevant.
- [ ] Within-scope responses only (comfort measures / meds per order / warming per facility / reassess); no provider verbs.
- [ ] The interaction section genuinely links the three, not three siloed blurbs.
- [ ] "Reassess" interval framed per facility.

## Worked Example (compact)

**Input:** `domains = thermoregulation`, `show_interactions = true`.

**Output (excerpt):**
```
### Thermoregulation (hypothermia / shivering)
- Why post-op: the OR is cool, anesthesia blunts the body's heat conservation, and patients often arrive cool.
- How I assess: cues before classic signs — visible shivering, "cold" complaints, and the downstream signs (rising BP/HR, worsening pain) before I even confirm a temperature.
- Within-scope response: active warming per facility, comfort measures, reassess.
- Escalate when: shivering/instability persists despite warming per protocol.
- Mimics: shivering vs. rigors (possible infection) vs. emergence tremor.

>>> INTERACTIONS
Being cold makes them shiver → shivering raises oxygen demand and BP and worsens pain → warming them often calms pain and BP together. One fix, three wins.
```

> Safety reminder: Study aid only — assess comfort here, but treat real patients by your preceptor, provider order, and facility protocol.
