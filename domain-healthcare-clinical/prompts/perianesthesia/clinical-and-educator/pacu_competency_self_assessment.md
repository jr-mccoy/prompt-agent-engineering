---
title: PACU Orientee Competency Self-Assessment
category: pacu/orientation
task_type: IMPROVE
audience: Phase 1 PACU orientee, mid-orientation or end-of-phase
updated: "2026-04-16"
tags:
  - pacu
  - orientation
  - self-assessment
  - reflection
techniques:
  - ST-01
  - ST-02
  - RT-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - prompts/pacu_preceptor_approach_guide.md
  - prompts/pacu_peer_preceptor_360_feedback.md
  - prompts/pacu_orientee_evaluation_meta_prompt.md
  - prompts/pacu_preceptor_debrief.md
  - prompts/pacu_preceptor_writing_orientee_evaluation.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Benner, P. — From Novice to Expert (self-appraisal cueing levels)
---

# PACU Orientee Competency Self-Assessment

> Safety reminder: Self-assessment supports learning — it does not substitute for preceptor observation or facility competency sign-off.

## Objective

Produce a **structured self-reflection prompt** the orientee completes mid-orientation or at the end of a rotation. Output is the filled form *template*; the user then hands it to the orientee to complete.

## Inputs

- **Mode:** {{`competency` (default — 7-part skill reflection) or `holistic` (adds end-of-phase impact / misses / questions sections)}}
- **Skill domain or role:** {{e.g., "airway management", "regional block assessment", "week-4 global check", or — for holistic mode — "end-of-Week-6 overall self-review"}}
- **Weeks into orientation:** {{…}}
- **Specific experiences the orientee has had:** {{user provides or orientee fills in}}

## Audience

- Phase 1 PACU orientee.
- Completes the form alone, then reviews with preceptor.

## Output requirements

```markdown
# Self-Assessment — {Domain / role} (Week {N})

> Safety reminder: Self-reflection only — your preceptor validates actual performance.

## Orientee
Name: ____________    Week of orientation: ____________    Date: ____________

## Part 1 — What I can do independently
List 3–5 things you can now do without cueing.
1. ...
2. ...
3. ...

## Part 2 — What I can do with cueing
List 3–5 things you do well when a preceptor prompts you.
1. ...
2. ...
3. ...

## Part 3 — What still surprises me
Things that still catch me off guard or that I freeze on.
1. ...
2. ...
3. ...

## Part 4 — One recent case I'm proud of
Briefly describe — what happened, what you did, what worked.

## Part 5 — One recent case I'd redo
Describe — what you'd do differently next time.

## Part 6 — Specific asks for my preceptor next week
- I want to practice: ...
- I want to be observed doing: ...
- I have a question about: ...

## Part 7 — Reading / study plan this week
- Topic: ...
- Source chapter: ...
- How I'll check myself: ... (quiz, flashcard drill, explain-it-aloud)

## Signed
Orientee: ____________    Preceptor review date: ____________
```

## Holistic mode addendum (append when mode = `holistic`)

When the orientee is at mid-orientation (e.g., end of Week 6) or approaching final sign-off, append these additional parts to the seven-part form above. Holistic mode **complements** the competency reflection; it does not replace it.

```markdown
## Part 8 — Impact (what changed because of what I did)
Convert two or three of the items in Part 1 or 4 from activity to impact using the template:

| What I did | → | What changed for the patient, team, or handoff |
|---|---|---|
| e.g., "Assisted with 12 PACU admissions" | → | "Developed independent SpO₂-trend recognition in 8 admissions; preceptor signed off on independent first assessment." |
| ... | → | ... |

If an item doesn't have a "what changed" answer, demote it. Activity without impact is a status report, not a self-review.

## Part 9 — Misses and what I learned
For 1–2 cases where the outcome fell short of what I or my preceptor hoped:
- **Intended outcome:** ...
- **What actually happened:** ...
- **What I now know that I didn't know going in:** ...
- **What I'll do differently next time:** ...

Real misses with real lessons. Humblebrags ("I care too much," "I'm too detail-oriented") are not growth edges — rewrite.

## Part 10 — Questions for my preceptor
2–4 specific questions I want the next 1:1 to address:
- Where did my self-assessment diverge most from your view, and why?
- What's the single biggest skill to master before independent practice?
- What's a strength I'm under-using?
- What specifically would move me from "With Cues" to "Independent" in {named competency}?

Skip generic ones ("any feedback?").

## Part 11 — Credit honestly
For every major item above, name the preceptor, peer, resource nurse, or CRNA who contributed — by role, not name. ("Charge helped triangulate the PONV escalation." "Resource nurse pointed me to the residual block assessment.") PACU is a team — self-reviews that claim sole credit are easy to spot.
```

## When to use each mode
- **`competency` mode (default):** shift-level or skill-level reflection throughout orientation. Use weekly or after any focused skill rotation.
- **`holistic` mode:** mid-orientation check-in (Week 6) or final sign-off preparation. Pairs directly with `pacu_preceptor_approach_guide.md` (preceptor preps evidence) and `pacu_peer_preceptor_360_feedback.md` (if multi-preceptor input is part of the cycle). Output is shared with the primary preceptor before the 1:1 evaluation conversation.

## Must / Must not

**Must:**
- Seven parts in order — independence, with-cueing, surprises, proud case, redo case, preceptor asks, study plan.
- Behavior-anchored language (verbs + what was done), not affective ("I feel good").
- Closes with explicit preceptor asks.
- **Holistic mode (when invoked):** also convert at least two activities to impact statements (Part 8), include at least one real miss with lesson (Part 9), and list at least two specific preceptor questions (Part 10).
- Credit collaborators by role (charge, CRNA, resource nurse, peer), not by name.

**Must not:**
- Do not ask about personality, attitude, or "fit" — the form is about demonstrated skill.
- Do not require specific case details that could violate patient privacy — use de-identified summary only; no patient-identifying information (MRN, full name, date of birth, room number).
- Do not use humblebrags as growth edges ("I work too hard," "I care too much") in holistic mode.
- Do not take sole credit for team wins — PACU work is collaborative.
- Do not reference age, race, sex, disability, religion, national origin, pregnancy, or other protected characteristics.
- Do not document medication errors that haven't been reported through the facility's incident-reporting system — file those in parallel; they do not belong in a reflective self-assessment.

## Quality signals

- Form can be completed in 10–15 minutes.
- Preceptor reviewing it immediately sees a growth edge and a practice ask.
- Self-identified gaps align with what preceptor is already seeing.

## Verification

Before returning the filled form (or handing the template to the orientee), verify:

- [ ] Parts 1–7 labels and order are preserved exactly.
- [ ] Each of Parts 1/2/3 requests 3–5 specific items.
- [ ] Parts 4/5 use de-identified case description (initials + context only, no MRN / full name / DOB / room).
- [ ] Part 6 preceptor-asks are specific, not generic ("any feedback?").
- [ ] Holistic mode (if invoked): Parts 8–11 all present; Part 8 converts activity → impact for ≥ 2 items; Part 9 has ≥ 1 real miss with a specific lesson (no humblebrags); Part 11 credits collaborators by role, not by name.
- [ ] Nothing in the form invites personality, attitude, or "fit" commentary.

## False-Positive Prevention

Do **not** fabricate:

- **No invented case details, vitals, dates, or doses** — the orientee fills in the form; the output is the template, not fabricated answers.
- **No prescribed emotional labels** ("I felt confident," "I was anxious"). The form is about demonstrated skill, not affect.
- **No patient-identifying information** (MRN, full name, full DOB, room number).
- **No humblebrags-as-growth-edges** ("I work too hard," "I care too much"). In holistic mode, explicitly reject these.
- **No sole-credit claims** — PACU is collaborative; role-based credit required.
- **No invented ASPAN section numbers, Drain's chapter numbers, or facility orientation program specifics.**
- **No protected-characteristic references** (age, race, sex, disability, religion, national origin, pregnancy, license pathway).

## Worked Example

<details>
<summary>Example: holistic-mode Part 8 (activity → impact) for a Week 6 new-grad (click to expand)</summary>

```markdown
## Part 8 — Impact (what changed because of what I did)

| What I did | → | What changed for the patient, team, or handoff |
|---|---|---|
| Assisted with 14 PACU admissions across Weeks 4–6, including 4 regional/neuraxial cases. | → | In the last 6 admissions, I completed the initial SpO₂/BP trend read without prompting — preceptor signed off on independent first-cycle assessment for non-high-risk admissions. |
| Took the lead on three PONV escalations after first dose failed. | → | In two of three, I recognized the second-wave pattern and prepared a different-class anti-emetic before patient complained, reducing escalation time (debrief 03/25 and 04/02). |
| Started using the handoff script template inbound from OR. | → | Receiving preceptor feedback (two shifts) that the inbound summary was more complete than early-orientation baseline; I can now reliably name lines, devices, last dose, anticipated trend. |

If an item doesn't have a "what changed" answer, I demote it. Activity without impact is a status report, not a self-review.
```

Notes: every "What I did" row has a specific "What changed" anchor tied to a debrief date or observable outcome; collaborators credited by role (preceptor, receiving preceptor); no vague "I got better at things."
</details>

## Self-check

- [ ] Seven labeled parts present.
- [ ] Each skill-based part asks for 3–5 specific items.
- [ ] Case sections ask for de-identified description.
- [ ] Preceptor asks block is explicit.
- [ ] Safety reminder at top.
- [ ] **Holistic mode only:** Parts 8–11 appended; at least two activity→impact conversions, one real miss with lesson, two specific preceptor questions, and role-based collaborator credit.
- [ ] No patient-identifying information.
- [ ] No protected-characteristic references.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed — no invented case details, humblebrags, or sole-credit claims.
