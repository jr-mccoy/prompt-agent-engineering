---
title: Preceptor Writing an Orientee Evaluation
category: pacu/preceptor-evaluation
task_type: CREATE
audience: PACU preceptor drafting a mid-orientation or final sign-off evaluation narrative
updated: "2026-04-16"
tags:
  - pacu
  - preceptor-evaluation
  - evaluation
  - sign-off
  - writing
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: advanced
related_prompts:
  - prompts/pacu_orientee_evaluation_meta_prompt.md
  - prompts/pacu_preceptor_approach_guide.md
  - prompts/pacu_peer_preceptor_360_feedback.md
  - prompts/pacu_preceptor_calibration_facilitator.md
  - prompts/pacu_orientee_remediation_plan.md
  - prompts/pacu_competency_self_assessment.md
  - prompts/pacu_preceptor_difficult_conversation_guide.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
  - Benner, P. — From Novice to Expert
---

# Preceptor Writing an Orientee Evaluation

> Safety reminder: Draft only. Every output is a draft the preceptor edits before submitting to the facility orientation program; it does not replace official competency sign-off documentation or patient-safety event reports.

## Objective

Produce a draft **PACU orientee evaluation narrative** from the preceptor's consolidated evidence and the scaffold from `pacu_orientee_evaluation_meta_prompt.md`. Every claim is evidence-anchored, growth edges are actionable observable behaviors, and the output is explicitly a draft.

## When to use

- **After** running `pacu_preceptor_approach_guide.md` (evidence + bias audit) and consuming the scaffold from `pacu_orientee_evaluation_meta_prompt.md`.
- For mid-orientation checkpoint, end-of-phase sign-off, final orientation sign-off, or probationary extension reviews.
- Do **not** use this to invent observations the preceptor doesn't have, or to produce final-submission text without human editing.

## Inputs

Ask for all of these before drafting. Do not proceed if any is missing.

- **Orientee identifier:** {{initials or placeholder}}
- **Orientation phase & evaluation type:** {{e.g., Week 2–6 checkpoint, final sign-off}}
- **Sign-off scale:** Defaults to **Independent / With Cues / With Direction / Not Yet** unless facility uses different tokens.
- **Target overall disposition + one-sentence justification:** Advance / extend orientation / remediation.
- **Competency scaffold** from `pacu_orientee_evaluation_meta_prompt.md` (pasted or referenced).
- **Evidence grid** from `pacu_preceptor_approach_guide.md` (shift-by-shift with citations).
- **Self-assessment excerpts** from the orientee (`pacu_competency_self_assessment.md`) — where their view aligns or diverges.
- **Peer preceptor 360 themes** from `pacu_peer_preceptor_360_feedback.md` — summarized themes, not raw quotes.
- **Prior-phase commitments** — what did the orientee commit to at the last debrief? Progress?
- **Known delivery concerns** flagged during the approach guide (first-time feedback, hard conversations).

## Audience / Scope

- **Primary:** Preceptor drafting the narrative.
- **Secondary:** Educator, nurse manager, or HR partner who will review the draft before it becomes facility-submitted text.
- **Scope:** Phase 1 PACU orientation only.

## Output requirements

Draft in the order below (growth edges first, summary last). Output uses this template:

```markdown
# PACU Orientee Evaluation — {Initials} — {Phase / Type} — {Date}

> Safety reminder: DRAFT — preceptor edits before submission. Does not replace facility sign-off documentation or patient-safety event reports. Verify evidence, tone, and disposition with educator / charge / facility HR partner per facility process.

## Summary (3–5 sentences)
[Overall disposition in plain language. 1–2 defining strengths, 1 defining growth edge. No platitudes.]

## Demonstrated Strengths (2–4 items)
1. **{Named strength.}** Behavior → Evidence (shift/date) → Impact on patient care or team.
2. ...

## Growth Edges (2–3 items)
1. **{Named edge, phrased as a desired change.}** Observed behavior (multiple specific examples) → Impact → Desired change (observable, actionable next-phase focus).
2. ...

## Progress Against Prior Phase Commitments
- **{Prior commitment}:** Outcome + read. What does the gap or follow-through tell us?

## Sign-off Recommendation per Competency

| Competency | Sign-off level | Evidence |
|---|---|---|
| Airway & breathing management | Independent / With Cues / With Direction / Not Yet | {shift/date + observed behavior} |
| Hemodynamic assessment & intervention | ... | ... |
| Oxygenation & ventilation | ... | ... |
| Post-op pain management | ... | ... |
| PONV recognition & escalation | ... | ... |
| Emergence & delirium | ... | ... |
| Regional / neuraxial block assessment | ... | ... |
| Handoff communication | ... | ... |
| Family communication & discharge teaching | ... | ... |
| Clinical judgment in ambiguity | ... | ... |
| Documentation accuracy | ... | ... |
| Team collaboration & role recognition | ... | ... |

**Overall phase disposition:** Advance to next phase / Extend orientation / Remediation (triggers `pacu_orientee_remediation_plan.md`)
**One-paragraph justification:** [Walks the competency ratings; does not back-fit the overall disposition from a gut impression.]

## Next-Phase Focus (3 behaviors)
1. {Specific observable behavior the orientee and next preceptor will concentrate on.}
2. ...
3. ...

## Divergence from Self-Assessment (if applicable)
[Where the orientee's self-view differs from the preceptor's view. Name the divergence without framing it as right/wrong; plan a specific conversation to resolve it.]

---

## Delivery Notes (NOT SUBMITTED)
- Likely orientee reactions: [defensive / emotional / dismissive / blindsided / grateful] — plan for each.
- Hardest sentence (confirm it's in the body above, verbatim): "..."
- Not up for negotiation in the 1:1: sign-off disposition, patient-safety documentation, rubric criteria, facility escalation expectations.
- Flags for preceptor before submission: [any first-time feedback? any peer 360 theme not yet addressed? any evidence still UNSUPPORTED?]

## Sources / reference
- ASPAN *Standards of Perianesthesia Nursing Practice*, {relevant sections}
- *Drain's PeriAnesthesia Nursing*, {relevant chapters}
- Facility orientation program document.
```

## Drafting rules per section

**Growth edges first:** Hardest to write; don't leave them until you're tired.

**Strengths:** Structure as **Behavior → Evidence → Impact.** Example: "Recognized residual neuromuscular blockade after a long rocuronium case (04/02 shift). Held handoff, called CRNA by role, documented sustained head-lift <5 sec. Result: reversal re-administered before transfer; no respiratory event downstream."

**Growth edges:** Structure as **Observed behavior → Impact → Desired change.** Must be actionable and observable. Example: "In PACU bay assessment, defaults to completing the checklist before forming a differential when vitals trend abnormal (observed 03/18, 03/25, 04/02 shifts). Impact: cue-recognition lags 2–5 minutes behind what the pattern already showed. Desired change: verbalize a two-item differential before completing the full checklist when any vital drifts outside expected range."

**Sign-off recommendation:** Walk the competency grid. If the overall disposition does not fall out of the competency-level ratings, stop and reconsider — do not back-fit.

## Must / Must not

**Must:**
- Treat every output as a draft the preceptor edits before submission.
- Anchor every substantive claim to a specific, observable example the preceptor provided.
- Translate personality labels into observed behavior.
- Make growth edges actionable — name the specific behavior to shift.
- Flag any feedback that appears to be new to the orientee (not raised in a prior debrief).
- Flag competencies where evidence is thin with **"insufficient observation this phase"** rather than inventing a rating.
- Name escalation partners by role (charge, CRNA, anesthesiologist on call, rapid response, rapid-transfusion), never by name.
- Use the sign-off scale tokens **Independent / With Cues / With Direction / Not Yet** consistently.

**Must not:**
- Fabricate examples, metrics, chart references, shift dates, or dose figures. If the preceptor did not provide it, do not produce it.
- Reference age, race, sex, disability, religion, national origin, pregnancy, or other protected characteristics.
- Speculate about medical or family circumstances ("seems burned out," "may be distracted at home"). Refer orientee to facility EAP if a concern exists; do not document it here.
- Use personality labels ("shy," "arrogant," "abrasive," "too passive," "aggressive"). Describe behavior.
- Reference license pathway (BSN/ASN/LPN-bridge) or prior unit as a performance signal.
- Compare the orientee by name to other specific orientees or staff RNs.
- Use vague praise ("great nurse," "team player," "strong communicator") without evidence.
- Back-fit a disposition. The competency-level sign-off ratings produce the overall disposition, not the reverse.
- Soften critical feedback until it disappears.
- Document medication errors that have not been reported through the facility's incident-reporting system. Remediation is not a substitute for a patient-safety event report.
- Include patient-identifying information (MRN, full name, date of birth, room number).
- Invent facility specifics — defer to `{{per facility protocol}}`.

## Quality signals

- Every strength and growth edge has a specific shift/date/artifact anchor.
- The overall disposition is traceable through the competency grid.
- A reviewer (educator / charge / HR) can tell why each sign-off level was assigned.
- The orientee reading the draft would recognize every observation.
- The document is labeled as a draft.

## Verification

Before returning the draft, verify:

- [ ] Every strength follows **Behavior → Evidence (shift/date) → Impact.**
- [ ] Every growth edge follows **Observed behavior → Impact → Desired change** and names an observable, actionable next-phase behavior.
- [ ] Competency-level ratings walk to the overall disposition — you can trace Advance / Extend / Remediation back through specific rows.
- [ ] Every claim in Summary is also in the body (no orphan claims).
- [ ] Delivery Notes block is labeled "NOT SUBMITTED" and contains flags for unresolved first-time feedback, peer-360 themes, and UNSUPPORTED items.
- [ ] Top of document carries the DRAFT label + safety reminder.

## False-Positive Prevention

Do **not** fabricate:

- **No invented shift dates, case details, vitals, times, or observations.** If the preceptor did not supply it, do not write it.
- **No invented ASPAN section numbers, Drain's chapter numbers, or citation titles.** Mark `{{confirm}}` when unknown.
- **No invented competency rubric weights or scoring thresholds.**
- **No invented facility orientation program specifics** (extension length, forms, HR triggers).
- **No invented peer-360 quotes.** Summarize themes only; the peer prompt explicitly forbids raw quote passage.
- **No personality labels** ("shy," "arrogant," "too passive," "not a good fit"). Translate to behavior.
- **No references to age, race, sex, disability, religion, national origin, pregnancy, license pathway, or prior unit as performance signals.**
- **No speculation about medical, mental-health, or family circumstances.**
- **No patient-identifying information** (MRN, full name, full DOB, room number).
- **No back-fitting** the disposition — if the competency ratings don't walk to it, stop.

## Worked Example

<details>
<summary>Example: Strength + growth edge from a final sign-off draft (click to expand)</summary>

**Demonstrated Strengths — excerpt:**

> **Residual-blockade recognition under uncertainty.** On 04/02 PM shift (post-laparoscopic chole + long rocuronium case), orientee noted shallow breathing and drool on chin before SpO₂ drift; held transfer; called CRNA by role with SBAR that included sustained head-lift <5 sec as the cue. **Impact:** reversal re-administered before transfer; no respiratory event downstream. **Evidence:** debrief summary 04/02; preceptor direct observation.

**Growth Edges — excerpt:**

> **Verbalize a differential before completing the full PACU checklist when vitals trend.** **Observed behavior:** on 03/18, 03/25, 04/02 shifts, orientee completed the PACU admission checklist before noting a BP or SpO₂ trend; each time, cue-recognition lagged 2–5 minutes behind what the pattern already showed. **Impact:** escalation timing was behind the trend. **Desired change:** when any vital drifts outside expected range during admission assessment, verbalize a two-item differential before completing the rest of the checklist. Measurable by direct observation on 3 of 4 shifts over the next phase.

Notes on what makes this Tier 1: strength has behavior + specific date + impact; growth edge lists multiple date anchors (not just one incident), frames as desired change, and defines the measurement. No personality labels, no protected-characteristic references, no invented vitals.
</details>

## Self-check

- [ ] Every strength and growth edge has a specific observable example.
- [ ] Every growth edge names a desired change the orientee can act on next phase.
- [ ] No personality labels remain.
- [ ] No protected-characteristic references; no medical or family speculation.
- [ ] No patient-identifying information.
- [ ] No invented doses, pager numbers, facility specifics, or fabricated citations.
- [ ] Summary matches the body of the evaluation.
- [ ] Competency grid walks to the overall disposition — no back-fit.
- [ ] Any first-time feedback is flagged to the preceptor with a plan to deliver it live first.
- [ ] Draft is labeled "DRAFT" at the top.
- [ ] Safety reminder present.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed — no invented observations, personality labels, or disposition back-fit.

Return the draft with a short note at the top: **"This is a draft. Edit before submitting. Verify evidence, tone, and sign-off disposition with the educator / charge / facility HR partner per facility process."**
