---
title: "Countertransference Reflection Prompt"
category: psychology/supervision-professional
description: "Structured countertransference reflection for a supervisee — triggers, somatic/affective signals, origin hypotheses, impact on the work, and a management plan that keeps the supervision/therapy boundary intact."
techniques:
  - RT-03
  - DT-01
  - QA-04
  - RP-03
  - CM-02
difficulty: intermediate
intended_use: model-testing
tags:
  - countertransference
  - clinical-supervision
  - reflective-practice
  - self-of-the-therapist
  - discrimination-model
  - boundary-maintenance
updated: "2026-06-08"
related_prompts:
  - domain-psychology/supervision-professional/psychology_parallel_process_detector.md
  - domain-psychology/supervision-professional/psychology_supervision_agenda_builder.md
  - domain-psychology/supervision-professional/psychology_dual_relationship_analyzer.md
  - domain-psychology/supervision-professional/psychology_therapeutic_technique_explainer.md
---

# Countertransference Reflection Prompt

## Objective

Guide a supervisee through a structured reflection on countertransference toward a specific client, so the reaction is named, understood, and managed in service of the client's treatment rather than enacted. The reflection must:

1. Identify the precise client material or moment that triggered the reaction.
2. Capture the supervisee's somatic, affective, and cognitive/behavioral signals before they are interpreted.
3. Generate hypotheses about origin — distinguishing *objective* countertransference (a reaction most clinicians would have to this client) from *subjective* countertransference (rooted in the supervisee's own history) — without converting supervision into therapy.
4. Assess the impact on the clinical work and produce a concrete management plan.

## When to Use

- A supervisee notices a strong, recurrent reaction to a client (dread, rescue urges, attraction, boredom, irritation, protectiveness, over-identification).
- A case where the supervisee is acting out of pattern (running over time, forgetting content, avoiding a topic, over-disclosing).
- After a session that "stuck" with the supervisee afterward.
- Training contexts building self-of-the-therapist awareness and reflective practice.

## Inputs / Context Required

- **Client snapshot (de-identified)**: presenting concern, interpersonal pattern, relevant demographics that bear on the reaction (initials/MRN only).
- **Trigger moment**: the specific exchange, content, or behavior that preceded the reaction.
- **The reaction as experienced**: `[supervisee input required: what you felt in your body, your emotions, and the impulses/urges that arose]`.
- **Behavioral signs**: any change in the supervisee's behavior toward the client (frame deviations, avoidance, special treatment).
- **Relevant supervisee context the supervisee chooses to share**: `[supervisee input required: only what you consent to bring into supervision; this is not therapy]`.
- **Supervisee stage**: IDM level (Level 1 reactivity differs from Level 3 use of self).
- `[clinician input required (supervisor): observations of the supervisee's process when presenting this case]`

## Constraints

### Must

- Capture the reaction (somatic / affective / cognitive-behavioral signals) *before* interpreting it.
- Distinguish **objective countertransference** (reaction this client would evoke in most clinicians — diagnostic data about the client) from **subjective countertransference** (reaction rooted in the supervisee's own history).
- Frame origin hypotheses as hypotheses, tied only to material the supervisee has consented to explore in supervision.
- Hold the **supervision/therapy boundary** explicitly: name the supervisee's history only to the extent it affects the work, and route deeper personal exploration to the supervisee's own therapy.
- Produce a management plan with concrete in-session and between-session steps, and a discrimination-model focus (typically *personalization*) and supervisory role.
- Specify how the management plan benefits the client's treatment.
- Include a supervision-record line and supervisor co-sign field.

### Must Not

- Do not pathologize the supervisee or treat the reflection as a clinical evaluation of the supervisee.
- Do not pursue the supervisee's personal trauma history beyond consented, work-relevant material; refer onward to personal therapy when indicated.
- Do not treat all countertransference as the supervisee's problem — name objective countertransference as data about the client.
- Do not include client-identifying detail.
- Do not fabricate; flag missing inputs with `[supervisee input required: ...]`.

## Instructions

1. **Anchor the trigger**: pin down the exact moment/content that preceded the reaction.
2. **Record the raw signals** at three levels (somatic, affective, cognitive/behavioral) in descriptive language, before interpretation.
3. **Sort the reaction**: estimate how much is objective (client-evoked, shared across clinicians) vs. subjective (supervisee-specific), with reasoning.
4. **Generate origin hypotheses** for the subjective portion, restricted to consented, work-relevant material; flag anything that belongs in the supervisee's own therapy.
5. **Assess impact**: how the reaction has shown up in the work (frame, alliance, technique, avoidance) and the risk if unmanaged.
6. **Build the management plan**: in-session regulation/strategy, between-session reflective steps, what to monitor, and whether to use or bracket the reaction.
7. **Translate to client benefit**: what changes for the client as a result.
8. Run verification.

## Output Format

```
=== COUNTERTRANSFERENCE REFLECTION ===

CONTEXT (de-identified)
Client (de-id): [Initials/MRN]   Supervisee: [Initials, IDM stage]
Presenting concern / interpersonal pattern: [...]

────────────────────────────────────────────────────────
TRIGGER
Moment / content that preceded the reaction: [Specific exchange or theme]

RAW SIGNALS (describe before interpreting)
Somatic: [Body sensations]
Affective: [Emotions]
Cognitive / behavioral / urges: [Thoughts, impulses, behaviors]

────────────────────────────────────────────────────────
OBJECTIVE vs. SUBJECTIVE SORT
Objective component (client-evoked, shared by most clinicians): [%/description]
  → Diagnostic data about the client: [What this reveals about the client's relational world]
Subjective component (supervisee-specific): [%/description]

────────────────────────────────────────────────────────
ORIGIN HYPOTHESES (subjective portion; consented, work-relevant only)
- [Hypothesis tied to a relevant theme]
- [Hypothesis]
Boundary flag — route to personal therapy: [Material that belongs outside supervision, if any]

────────────────────────────────────────────────────────
IMPACT ON THE WORK
Frame / alliance / technique effects observed: [...]
Risk if unmanaged: [...]

────────────────────────────────────────────────────────
MANAGEMENT PLAN
Use vs. bracket decision: [Use as data / Bracket and regulate] — Rationale: [...]
In-session strategy: [Regulation, reframing, pacing]
Between-session reflective steps: [Journaling, consultation, personal therapy if indicated]
Discrimination-model focus: [Personalization / other]   Supervisory role: [Counselor / Consultant / Teacher]
Monitoring: [What to watch next session]

CLIENT-LEVEL BENEFIT
[How managing this reaction improves the client's treatment]

────────────────────────────────────────────────────────
SUPERVISION RECORD
Reflection completed: [Date]   Follow-up: [...]
Supervisee: ____________________  Date: ________
Supervisor co-sign: ____________  Date: ________
```

## Verification

- [ ] Trigger moment specified concretely.
- [ ] Raw signals captured at somatic, affective, and cognitive/behavioral levels before interpretation.
- [ ] Objective vs. subjective countertransference distinguished, with the objective portion named as data about the client.
- [ ] Origin hypotheses restricted to consented, work-relevant material; deeper material routed to personal therapy.
- [ ] Supervision/therapy boundary explicitly preserved; supervisee not pathologized or evaluated.
- [ ] Management plan includes in-session and between-session steps and a use-vs-bracket decision.
- [ ] Discrimination-model focus and supervisory role labeled.
- [ ] Client-level benefit stated.
- [ ] All client material de-identified.
- [ ] Supervisor co-sign field present; gaps flagged with `[supervisee input required]`; nothing fabricated.
