---
title: PACU Orientation Shadowing Objectives Designer
category: pacu/orientation-curriculum
task_type: CREATE
audience: PACU preceptor or educator scheduling a shadow shift with a non-PACU role
updated: "2026-05-15"
tags:
  - pacu
  - orientation
  - shadowing
  - role-understanding
techniques:
  - ST-01
  - ST-02
  - RT-02
  - ED-02
  - DS-06
difficulty: beginner
related_prompts:
  - prompts/pacu_orientation_curriculum_designer.md
  - prompts/pacu_orientee_weekly_learning_plan.md
  - prompts/pacu_preceptor_debrief.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
---

# PACU Orientation Shadowing Objectives Designer

> Safety reminder: Shadowing is non-clinical for the orientee. Clinical scope remains with the shadowed role; orientee does not perform tasks outside PACU scope during a shadow.

## Objective

Produce a **shadow-shift objectives brief** for one specific role the PACU orientee will shadow during orientation: what to watch for, what questions to ask, what to bring back. Examples: anesthesia provider (CRNA / anesthesiologist), surgeon rounding, charge nurse, respiratory therapist, pharmacy consult, sterile processing, ambulatory discharge.

## Inputs

- **Role to shadow:** {{anesthesia provider | surgeon rounding | charge nurse | respiratory therapist | pharmacy | OR circulator | ambulatory recovery RN | other}}
- **Orientation week:** {{n — drives depth}}
- **Time budget:** {{e.g., one shift / 4 hours / 2 hours during one shift}}
- **Curriculum reason for this shadow:** {{e.g., "Wk 4 emergence content — see how the anesthesia provider thinks about emergence from the OR side"}}
- **Approval status:** {{primary preceptor approval + role-side approval both required — Y/N}}

## Audience / Scope

- **Primary:** PACU orientee.
- **Secondary:** Primary preceptor (briefs orientee before) and shadowed role (gets a 4-line brief).
- **Scope:** One shadow event. Not a sign-off event.

## Output requirements

```markdown
# Shadow Objectives — {Role}, Wk {n}

> Safety reminder: Orientee is observer only. Clinical responsibility belongs to the shadowed role.

**Role:** {role}
**Time budget:** {budget}
**Curriculum reason:** {one sentence}
**Approvals:** Primary preceptor ✓ Role side ✓

## Why this shadow now (one sentence)

Connect this shadow to the curriculum week's theme.

## What to watch for (3–5 items)

For each item:
- {Observable behavior or decision the orientee should track}
- {Why it matters to PACU practice}

Examples for anesthesia-provider shadow:
- How does the provider decide when a patient is ready for OR exit?
- What do they document about emergence that you'll see in PACU?
- What patient features make them flag for high PACU watch?

Examples for charge-nurse shadow:
- How do bay assignments get made when census changes?
- What's the trigger for stretching staffing?
- What's the trigger for diverting an admission?

## Questions to ask (3–5)

Open-ended, role-specific. Avoid yes/no.
- "What's the hardest decision you made today, and what made it hard?"
- "What information about this patient do you wish PACU always knew at handoff?"
- "If you could change one thing about how PACU receives patients, what would it be?"

## What NOT to do

- Do not perform clinical tasks outside PACU scope during shadow.
- Do not document in the shadowed role's section of the chart.
- Do not give clinical opinions in patient earshot.
- Do not photograph anything.

## What to bring back to PACU

After the shadow:
- One thing you saw that changes how you'll approach handoff next week.
- One question you couldn't answer that you'll bring to your primary preceptor.
- One thing that surprised you.

## Debrief with primary preceptor

15-min debrief at the next PACU shift start:
1. What did you see?
2. What changes how you approach our workflow?
3. What's the one thing you'll do differently?

Feed into rolling debrief log (`pacu_preceptor_debrief.md`).

## Brief for the shadowed role (4–6 lines)

"{Orientee} is shadowing you for {budget} on {date} as part of PACU orientation Wk {n}. They are observers only — no clinical tasks, no documentation in your scope. Their curriculum goal is {one sentence}. Open to questions when convenient. Debrief is with their primary preceptor afterward, not with you."

## Sources / reference

- ASPAN *Standards* — scope and role boundaries.
- Facility orientation program — for any specific shadow approvals required.
```

## Must / Must not

**Must:**
- Require both primary-preceptor and role-side approvals.
- Frame orientee as observer only — no clinical action outside PACU scope.
- Tie the shadow to a curriculum week's theme.
- Provide an open-ended question list (no yes/no).
- Schedule a debrief with the primary preceptor afterward.

**Must not:**
- Allow the shadowed role to evaluate the orientee.
- Frame the shadow as a sign-off event.
- Direct the orientee to perform tasks in the shadowed role's scope.
- Generate questions that probe personal information about the shadowed role or patients.
- Reference protected characteristics.

## Quality signals

- The shadowed role reads the brief and knows what's expected.
- The orientee leaves the shadow with three specific things to bring back.
- The primary preceptor can run the debrief in 15 min.

## Verification

- [ ] Both approvals required.
- [ ] Observer-only framing.
- [ ] Curriculum-week tie.
- [ ] Open-ended question list.
- [ ] Debrief scheduled.
- [ ] Brief for shadowed role ≤ 6 lines.
- [ ] Safety + FPP sections present.

## False-Positive Prevention

- **No invented facility shadow-approval policies.**
- **No invented role-scope claims** ("the CRNA will let you draw meds during shadow" — no).
- **No invented role conflicts or grievances** (e.g., generic claims about another department).
- **No invented patient interaction scripts** during shadow.
- **No protected-characteristic content** in observation prompts.
- **No license-pathway-based shadow eligibility.**

## Worked Example

<details>
<summary>Example: Anesthesia-provider shadow, Wk 4 (emergence theme), 4 hours (click to expand)</summary>

```markdown
# Shadow Objectives — Anesthesia Provider, Wk 4

**Role:** Anesthesia provider (CRNA or anesthesiologist).
**Time budget:** 4 hours, OR-side, 2 cases.
**Curriculum reason:** Wk 4 emergence content — see emergence from the OR side.
**Approvals:** Primary preceptor ✓ Anesthesia department ✓.

## Why this shadow now

Wk 4 is emergence theme in PACU. Seeing emergence from the OR side gives the orientee a fuller mental model of what the patient was through before arriving in PACU.

## What to watch for

- Decision points around emergence timing.
- What the provider documents at OR exit that you'll see in handoff.
- Patient features that make the provider flag for high PACU watch.
- The shape of the OR-to-PACU handoff from the provider's side.

## Questions to ask

- "How do you decide a patient is ready for OR exit?"
- "What about this patient would make you call ahead to PACU?"
- "What information do you wish PACU always knew at handoff?"

## What NOT to do

(as listed above — observer only)

## Bring back

- One thing that changes your handoff approach.
- One question for your primary preceptor.
- One surprise.

## Debrief with primary preceptor (15 min, next PACU shift start)

3 questions as listed.

## Brief for anesthesia provider

"Orientee is shadowing you for 4 hours on {date} for Wk 4 of PACU orientation. Observer only, no clinical tasks. Goal is to see emergence from the OR side. Open to questions when convenient. Debrief afterward is with their PACU preceptor."
```

Notes: observer-only explicit, curriculum-tie clear, brief is short, debrief scheduled.
</details>

## Self-check

- [ ] Both approvals stated.
- [ ] Observer-only framing.
- [ ] Curriculum tie present.
- [ ] Open-ended questions only.
- [ ] Debrief scheduled.
- [ ] Brief for role ≤ 6 lines.
- [ ] FPP section passed.
