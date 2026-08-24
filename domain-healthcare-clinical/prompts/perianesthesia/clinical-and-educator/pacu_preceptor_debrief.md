---
title: End-of-Shift Preceptor Debrief
category: pacu/preceptor
task_type: COMMUNICATE
audience: PACU preceptor conducting end-of-shift debrief with orientee
updated: "2026-04-16"
tags:
  - pacu
  - preceptor
  - debrief
techniques:
  - ST-01
  - ST-02
  - RT-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - ../../domain-healthcare-clinical/prompts/nursing_preceptor_daily_debrief.md
  - ../../domain-healthcare-clinical/prompts/nursing_preceptor_fumble_postmortem.md
  - prompts/pacu_preceptor_approach_guide.md
  - prompts/pacu_preceptor_writing_orientee_evaluation.md
  - prompts/pacu_competency_self_assessment.md
  - prompts/pacu_preceptor_difficult_conversation_guide.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Benner, P. — From Novice to Expert (behavioral anchors for cueing levels)
---

# End-of-Shift Preceptor Debrief

> Safety reminder: Debrief guide only — it does not replace the facility's formal competency sign-off documentation.

## Objective

Produce a **preceptor-led end-of-shift debrief script** with time-boxed sections, questions, and a short written capture the preceptor hands (or emails) to the orientee afterward.

## Inputs

- **Orientee name (or initials):** {{…}}
- **Week of orientation:** {{…}}
- **Notable events from the shift:** {{…}}
- **Priority teaching focus going into the shift (if any):** {{…}}

## Audience

- Preceptor (experienced PACU nurse).
- Secondary: orientee, who receives the written summary.

## Output requirements

```markdown
# End-of-Shift Debrief — {Orientee} (Week {N}), {Date}

> Safety reminder: Debrief aid — formal competency sign-off happens in the documented tool.

## Time budget: 15 minutes

## Part 1 — What went well (3 min)
Preceptor asks:
- "Walk me through one case today where you felt things went the way you wanted."
- "What did you specifically do that made that go well?"

## Part 2 — What was hard (4 min)
Preceptor asks:
- "What was the moment today that felt hardest?"
- "What was your thinking right before that?"
- "What cue would have told you sooner?"

## Part 3 — Pattern across the shift (3 min)
Preceptor observation (share 1–2 specific examples, one strength and one growth edge):
- Strength: ...
- Growth edge: ...

## Part 4 — Commit to one thing (3 min)
Orientee chooses:
- One specific behavior or skill to focus on next shift.
- Preceptor confirms it's measurable and observable.

## Part 5 — Preceptor next-shift plan (2 min)
- I will: observe you doing ... at least twice.
- I will: give you room to try ... before I intervene.
- Call me immediately if: ... (no exceptions).

## Written summary (preceptor completes and gives to orientee)
| Category | Note |
|---|---|
| Strength demonstrated | ... |
| Growth edge | ... |
| Orientee's commitment next shift | ... |
| Preceptor's observation plan | ... |
| Non-negotiable escalation triggers | ... |

## Rolling Evidence Log (preceptor's own copy)

The written summary table above, accumulated across shifts, **is** the preceptor's shift-by-shift evidence log. Keep a running copy (preceptor-owned; not the orientee's chart) so it is ready to feed into:
- `pacu_preceptor_approach_guide.md` — evidence inventory for mid-orientation or final sign-off prep.
- `pacu_preceptor_writing_orientee_evaluation.md` — shift-dated citations for each strength and growth edge.
- `pacu_preceptor_calibration_facilitator.md` — evidence base when norming with other preceptors.
- `pacu_preceptor_difficult_conversation_guide.md` — confirms the no-surprises principle (concerns already delivered).

No new artifact is needed — the debrief summary table accumulated over time **is** the rolling log.

## Sources / reference
- ASPAN *Standards of Perianesthesia Nursing Practice*, {relevant section} (if cited during debrief).
```

## Must / Must not

**Must:**
- Time-boxed sections summing to ~15 minutes.
- Specific preceptor prompts (not general "how did it go?").
- One strength + one growth edge based on observation.
- Orientee commits to exactly one focus for next shift.
- Preceptor names their own next-shift plan.
- Written summary table the preceptor completes.

**Must not:**
- No vague affect-based prompts ("how did you feel?" without a behavior anchor).
- No patient-identifying content in the written summary.
- No doses, supplies, or facility-specific escalations baked in — those belong in the unit's formal tools.

## Quality signals

- Debrief ends with a concrete next-shift commitment.
- Both strength and growth edge are observable.
- Preceptor commits to a specific observation plan.

## Verification

Before finalizing the written summary, verify:

- [ ] Strength and growth edge are both phrased as observable behaviors, not traits or affect ("cued on BP trend at second cycle" not "good judgment").
- [ ] Orientee's next-shift commitment is one item, specific, and observable — a second preceptor could assess it.
- [ ] Preceptor's observation plan names at least one specific behavior to watch and one boundary ("I will give you room to try X before I intervene").
- [ ] No patient-identifying content in the written summary (no MRN, full name, DOB, room).
- [ ] Nothing in the summary is first-time critical feedback that hasn't been raised live during the shift.

## False-Positive Prevention

Do **not** fabricate:

- **No invented observations.** If the preceptor did not see a specific behavior, do not generate one to fill the table.
- **No personality labels** ("quiet," "confident," "defensive"). Translate to what the orientee did or said.
- **No invented incident details** (exact times, exact vitals, specific drug doses) unless the preceptor supplied them.
- **No patient-identifying information** (MRN, full name, full DOB, room number).
- **No speculation about medical, mental-health, or family circumstances.** If concern arises, refer to EAP by role.
- **No references to age, race, sex, disability, religion, national origin, pregnancy, or license pathway** (BSN/ASN/LPN-bridge).
- **No invented facility policies or specific escalation phone numbers.**

## Worked Example

<details>
<summary>Example: Week 4 orientee, shift included a PONV escalation (click to expand)</summary>

```markdown
# End-of-Shift Debrief — J.M. (Week 4), 2026-04-15

> Safety reminder: Debrief aid — formal competency sign-off happens in the documented tool.

## Time budget: 15 minutes

## Part 1 — What went well (3 min)
- "Walk me through the PONV case in bay 2 — what went the way you wanted?"
- "What did you specifically do that made it go well?"

## Part 2 — What was hard (4 min)
- "What was the moment today that felt hardest?"
- "What was your thinking right before that?"
- "What cue would have told you sooner?"

## Part 3 — Pattern across the shift (3 min)
- Strength: On bay 2 PONV case, recognized the second wave of nausea and proactively prepared the next anti-emetic before patient complained — preempted escalation.
- Growth edge: On bay 4 post-spinal case, defaulted to completing PACU checklist before noting BP trend; verbalized differential after I cued on the trend.

## Part 4 — Commit to one thing (3 min)
- Orientee commits: "When any vital drifts outside expected range during admission assessment, I will verbalize a two-item differential before completing the rest of the checklist."

## Part 5 — Preceptor next-shift plan (2 min)
- I will: observe at least two admission assessments where vitals trend early.
- I will: wait for you to verbalize before I cue.
- Call me immediately if: any red-flag trigger, especially post-spinal BP trends.

## Written summary (preceptor completes and gives to orientee)
| Category | Note |
|---|---|
| Strength demonstrated | Preempted PONV second wave (bay 2, ~13:30) — prepared next anti-emetic before patient complained. |
| Growth edge | Completed PACU checklist before verbalizing differential on bay 4 post-spinal BP trend (~14:45). |
| Orientee's commitment next shift | Verbalize two-item differential before completing checklist when any vital drifts outside expected range. |
| Preceptor's observation plan | Two admission assessments with early trends; will wait before cueing. |
| Non-negotiable escalation triggers | Any red-flag trigger (reviewed on red-flag pocket card); post-spinal BP trends especially. |
```

Notes: strength and growth edge both observable + anchored to specific bay/time; commitment is one measurable behavior; no patient identifiers beyond initials; no personality labels.
</details>

## Self-check

- [ ] Five time-boxed parts totaling ~15 min.
- [ ] Prompts are behavior-anchored, not affect-only.
- [ ] Written summary table included.
- [ ] Commits to one focus + observation plan.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed — no invented observations, personality labels, or patient identifiers.
