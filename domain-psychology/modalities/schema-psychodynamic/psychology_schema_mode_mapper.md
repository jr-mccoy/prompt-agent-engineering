---
title: "Schema Mode Mapper (Young)"
category: psychology/modalities/schema-psychodynamic
description: "Map active schema modes — Vulnerable Child, Angry/Impulsive Child, Punitive/Demanding Parent, Detached Protector / Self-Soother / Compliant Surrenderer / Bully-Attack, and Healthy Adult — using Young's Schema Mode Inventory framework with a session-specific mode formulation."
techniques:
  - ST-04
  - RT-02
  - DT-02
  - ED-04
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - schema-therapy
  - Young
  - schema-modes
  - vulnerable-child
  - punitive-parent
  - healthy-adult
  - SMI
intended_use: model-testing
updated: "2026-05-19"
related_prompts:
  - domain-psychology/modalities/schema-psychodynamic/psychology_psychodynamic_transference_focused_formulation.md
  - domain-psychology/modalities/schema-psychodynamic/psychology_psychodynamic_session_process_note.md
  - domain-psychology/modalities/ifs-parts/psychology_ifs_parts_mapping.md
---

# Schema Mode Mapper (Young)

## Objective

Map a client's active schema modes per Young's Schema Therapy framework, distinguishing **child modes** (Vulnerable, Angry, Impulsive, Undisciplined, Happy), **maladaptive coping modes** (Compliant Surrenderer, Detached Protector, Detached Self-Soother, Avoidant Protector, Overcompensator, Bully-Attack, Self-Aggrandizer), **maladaptive parent modes** (Punitive Parent, Demanding Parent), and the **Healthy Adult** mode. Output is a formulation with triggers, body markers, behaviors, and a treatment plan that strengthens Healthy Adult and limits maladaptive modes.

## When to Use

- Schema therapy intake / early sessions (1–6) after EMS assessment.
- Mid-treatment when modes are shifting and the formulation needs updating.
- Personality-disorder treatment (especially BPD, NPD, AvPD, OCPD) within schema therapy or schema-informed therapy.
- Group schema therapy.
- Telehealth or in-office.
- Not as a substitute for risk assessment; not as a substitute for trauma-focused therapy where indicated.

## Inputs / Context

- Young Schema Mode Inventory (SMI; full or short) scores or comparable inventory.
- Early Maladaptive Schemas (EMS) endorsed (Young Schema Questionnaire / SMI).
- Recent episodes of mode flips (date / context / behavior).
- Trauma / attachment history.
- Treatment-stage targets and prior formulation.
- Cultural / family context.
- Risk plan (suicidality, self-harm, substance use).
- Modality, time (mode mapping 30–60 min).

## Constraints

### Must

- Identify modes present **per the SMI categories** and the client's own labels.
- For each active mode, capture: **triggers, body markers, behaviors, schemas underneath, function (what it protects against), and Healthy-Adult counter-response**.
- Distinguish **modes from traits**: a mode is a temporary state, not a fixed identity.
- Identify **mode flips**: which mode follows which (e.g., Punitive Parent → Vulnerable Child → Detached Self-Soother via substance).
- Capture **schema couplings**: which EMSs feed which modes (e.g., Defectiveness/Shame → Punitive Parent; Abandonment → Vulnerable Child).
- Strengthen the **Healthy Adult** mode: capture its strengths, gaps, and skills the client already has when in this mode.
- Plan **limited reparenting** moves the therapist will use (validation, soothing, limit-setting, encouragement).
- Identify **schema-mode-specific interventions** to deploy: imagery rescripting (Vulnerable Child); empty-chair (Punitive Parent); behavioral pattern-breaking (coping modes).
- Document risk modifiers (e.g., Bully-Attack and Self-Aggrandizer modes can include aggression risk).
- For NPD presentations, mode-mapping is particularly sensitive to alliance — pace carefully.

### Must Not

- Do not label modes the client doesn't endorse without exploration.
- Do not pathologize coping modes; they were adaptive once.
- Do not import IFS-parts terminology onto schema modes (different frameworks, different mechanisms).
- Do not use Punitive Parent–style language toward the client.
- Do not promise mode elimination; the goal is reduced frequency / intensity and strengthened Healthy Adult.
- Do not finalize the map without the client's recognition.
- Do not deliver schema-mode interventions without adequate training.

## Instructions

1. Review SMI scores and recent mode-flip episodes.
2. For each elevated mode, walk through triggers, body, behaviors, schemas, function.
3. Identify mode-flip sequences with examples.
4. Identify Healthy Adult capacities and gaps.
5. Plan reparenting moves and mode-specific interventions.
6. Document risk modifiers.
7. Set homework: mode log (daily, brief) and Healthy Adult strengthening prompts.
8. Review with client; adjust language to their lived experience.
9. Schedule next session.

## Output Format

```
=== SCHEMA MODE MAP ===
Client: [Initials/MRN]    Date: [YYYY-MM-DD]    Session #: [N]    Modality: [...]
SMI / SMI-SF scores: [Date, top elevations]
Active EMSs (top 3–5): [...]

CHILD MODES PRESENT
- Vulnerable Child: triggers / body / behavior / underlying schemas / function: [...]
- Angry / Impulsive / Undisciplined Child: [...]
- Happy Child (capacities): [...]

COPING MODES PRESENT
- Compliant Surrenderer: [...]
- Detached Protector: [...]
- Detached Self-Soother: [...]
- Avoidant Protector: [...]
- Overcompensator (variants — Self-Aggrandizer, Bully-Attack, Perfectionistic): [...]

MALADAPTIVE PARENT MODES
- Punitive Parent: [Verbatim self-talk: "[...]"]
- Demanding Parent: [Verbatim self-talk]

HEALTHY ADULT MODE
- Strengths client demonstrates: [...]
- Gaps to strengthen: [...]
- Skills already in repertoire: [...]

MODE-FLIP SEQUENCES
- Example 1: [Trigger] → [Mode A] → [Mode B] → behavior
- Example 2: [...]

SCHEMA COUPLINGS
- EMS → mode: [...]
- EMS → mode: [...]

REPARENTING MOVES (therapist)
- Validation: [...]
- Soothing: [...]
- Limit-setting: [...]
- Encouragement: [...]

MODE-SPECIFIC INTERVENTIONS PLANNED
- Imagery rescripting (Vulnerable Child target): [...]
- Empty-chair / mode dialogues (Punitive Parent confrontation): [...]
- Behavioral pattern-breaking (coping mode disruption): [...]

RISK MODIFIERS
- Aggression risk (Bully-Attack / Self-Aggrandizer): [...]
- Suicidality / self-harm (Punitive Parent + Vulnerable Child + Detached Self-Soother): [...]
- Substance / self-soothing escalation: [...]

HOMEWORK
- Daily mode log: brief — trigger / mode / Healthy Adult response attempted
- Healthy Adult strengthening prompts: [...]

CLINICIAN NOTES
- Alliance considerations (especially NPD): [...]
- Cultural / family schema considerations: [...]
- Consultation / supervision item: [...]
- Next session: [Date / target]
```

## Verification

- [ ] Modes labeled per Young's framework; client-endorsed.
- [ ] Each active mode has triggers, body, behaviors, schemas, function captured.
- [ ] Healthy Adult capacities and gaps mapped.
- [ ] Mode-flip sequences with examples.
- [ ] Reparenting moves planned.
- [ ] Mode-specific interventions specified.
- [ ] Risk modifiers identified.
- [ ] Daily mode-log homework assigned.
- [ ] No pathologizing of coping modes.
- [ ] No mixing of frameworks (IFS vs schema) without intent.
- [ ] No fabricated mode endorsements.
