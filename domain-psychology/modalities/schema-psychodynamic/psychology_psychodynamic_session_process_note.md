---
title: "Psychodynamic Process Note (Transference / Defenses / Enactments)"
category: psychology/modalities/schema-psychodynamic
description: "Generate a psychodynamic process-focused session note capturing transference, countertransference, defenses, enactments, and the therapist's interventions and reasoning — distinct from a problem-oriented progress note."
techniques:
  - ST-04
  - RT-02
  - DT-02
  - ED-04
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - psychodynamic
  - process-note
  - transference
  - countertransference
  - enactment
  - defenses
  - supervision
intended_use: model-testing
updated: "2026-05-19"
related_prompts:
  - domain-psychology/modalities/schema-psychodynamic/psychology_psychodynamic_transference_focused_formulation.md
  - domain-psychology/modalities/schema-psychodynamic/psychology_schema_mode_mapper.md
  - domain-psychology/documentation/psychology_soap_progress_note.md
---

# Psychodynamic Process Note (Transference / Defenses / Enactments)

## Objective

Generate a psychodynamic **process note**: a session document capturing the unfolding intersubjective material — transference, countertransference, defenses, enactments, parapraxes, silences, affect shifts — alongside the therapist's interventions and reasoning. Distinct from a problem-oriented progress note (SOAP), the process note serves supervision, the therapist's own reflective practice, and continuity of formulation.

The note is **not** a substitute for the billing / clinical progress note (which goes in the chart) — it is the therapist's parallel process document, typically held separately per practice policy and supervision agreements.

## When to Use

- Psychodynamic / psychoanalytically informed therapy of any modality (CCRT, TFP, mentalization-based therapy, relational analysis, brief psychodynamic).
- Supervision case presentation (raw material for the supervisor to work with).
- Therapist's own reflective practice between sessions.
- Training contexts (psychoanalytic candidates, fellows).
- Not a billing document.

## Inputs / Context

- Session number, date, length.
- Formulation in current use (object-relations dyads, mentalization profile, attachment, schema modes — whichever applies).
- Recent themes / between-session events.
- Risk and frame status.
- Practice policy on process-note retention (some jurisdictions / boards have specific rules on process notes / "psychotherapy notes" under HIPAA).

## Constraints

### Must

- Distinguish **process note** from **progress note**:
  - Process note: unstructured-to-semi-structured, captures affect, transference, countertransference, defenses, enactments, hypotheses.
  - Progress note: structured for the chart, captures presenting concerns, interventions, risk, plan, billing.
- Capture the **arc of the session**: opening affect, key turns, closing state.
- Note **transference**: the client's experience of the therapist (idealizing, devaluing, paranoid, eroticized, contemptuous, mirroring).
- Note **countertransference**: the therapist's affective / somatic / fantasy responses, with reflection on whether they are concordant (matching the client's experience) or complementary (matching an internal object).
- Note **defenses**: which defenses the client used and where they activated (e.g., intellectualization at a moment of grief; splitting after an empathic failure).
- Note **enactments**: moments the therapist acted into the dynamic (e.g., became unusually directive after a devaluing comment).
- Note **interventions**: clarification, confrontation, interpretation, validation, holding, limit-setting, mentalization-promoting questions — with the therapist's reasoning.
- Note **the client's response** to interventions, including non-verbal.
- Note **frame events**: late, missed, fee, between-session contact, third-party involvement.
- Note **hypotheses** for next session and reformulation updates.
- Mark **gaps / uncertainties**: what the therapist doesn't yet understand.
- Honor practice policy and applicable law (HIPAA "psychotherapy notes" require separation from the medical record).
- For high-acuity material: include risk-stratification status, even though the formal risk note is in the chart.

### Must Not

- Do not use the process note as the billing / chart document.
- Do not include third-party identifiers; the process note is a working document for the therapist.
- Do not invent therapeutic interventions that did not occur.
- Do not pathologize moments without the formulation backing.
- Do not skip countertransference; missing it produces a censored record.
- Do not let process-note writing become a defense against in-session presence.
- Do not retain process notes longer than necessary or against practice policy.

## Instructions

1. Within 24 hours, write the process note. Memory degrades.
2. Open with the arc: opening affect → turns → closing state.
3. Capture transference moments verbatim where possible.
4. Reflect on countertransference: somatic, affective, fantasy. Concordant vs complementary.
5. Note defenses with examples.
6. Note enactments and how they were (or were not) recognized in-session.
7. List interventions with reasoning.
8. Capture client responses to each.
9. Note frame events.
10. Write hypotheses and formulation updates.
11. Mark gaps for next session and supervision.
12. Store per practice policy.

## Output Format

```
=== PSYCHODYNAMIC PROCESS NOTE ===
Therapist: [Name]    Session #: [N]    Date: [YYYY-MM-DD]    Length: [N min]
Formulation in use: [TFP dyad / MBT mentalization profile / Schema modes / Other]
Current frame status: [Adherent / Frame event observed]
Risk stratification at time of session: [Low / Moderate / High; rationale]

SESSION ARC
- Opening: [Affect, presentation, what the client brought]
- Key turn(s): [Moment(s) where the field shifted]
- Closing: [Affect, leave-taking]

TRANSFERENCE
- Client's experience of the therapist this session: [Idealizing / Devaluing / Paranoid / Eroticized / Contemptuous / Mirroring / ...]
- Verbatim moments: "[...]"
- Hypotheses about origin: [...]

COUNTERTRANSFERENCE
- Somatic: [...]
- Affective: [...]
- Fantasy / image / memory evoked: [...]
- Concordant vs complementary: [Reflection]
- Useful information about the client's inner world: [...]

DEFENSES OBSERVED
- [Defense type] at [moment]: [example]
- [...]

ENACTMENTS
- Moments the therapist acted into the dynamic: [example]
- Recognized in-session: [Y/N — when]
- Repair / reflection: [...]

INTERVENTIONS
- [Clarification / Confrontation / Interpretation / Validation / Holding / Limit-setting / Mentalization-promoting]
- Reasoning: [...]
- Client response: [...]
- [repeat per intervention]

FRAME EVENTS
- Late / missed / fee / contact / third party: [...]
- Hypothesis: [...]
- Action taken: [...]

HYPOTHESES FOR NEXT SESSION
- [...]
- Formulation update: [Y/N — what shifted]

GAPS / UNCERTAINTIES
- What the therapist doesn't yet understand: [...]

SUPERVISION ITEMS
- [...]

STORAGE / POLICY
- Note location: [Separate from chart per practice policy / HIPAA psychotherapy notes]
- Retention: [Per policy]
```

## Verification

- [ ] Process note distinct from chart progress note.
- [ ] Session arc captured.
- [ ] Transference moments noted with verbatim where possible.
- [ ] Countertransference reflected with somatic / affective / fantasy detail.
- [ ] Defenses identified with moments.
- [ ] Enactments noted; repair reflection included.
- [ ] Interventions listed with reasoning and client responses.
- [ ] Frame events captured.
- [ ] Hypotheses and formulation updates present.
- [ ] Gaps and supervision items flagged.
- [ ] Storage / policy adherence noted.
- [ ] Risk status reported even if formal risk note is in chart.
- [ ] No fabricated interventions.
