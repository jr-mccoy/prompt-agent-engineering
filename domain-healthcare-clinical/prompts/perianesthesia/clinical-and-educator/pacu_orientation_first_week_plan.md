---
title: PACU Orientation — First Week Day-by-Day Plan
category: pacu/orientation-curriculum
task_type: CREATE
audience: PACU primary preceptor or unit educator scheduling Week 1
updated: "2026-05-15"
tags:
  - pacu
  - orientation
  - week-1
  - preceptor
  - pairing
techniques:
  - ST-01
  - ST-02
  - RT-02
  - ED-02
  - DS-06
difficulty: beginner
related_prompts:
  - prompts/pacu_orientation_curriculum_designer.md
  - prompts/pacu_orientation_first_day_packet.md
  - prompts/pacu_orientee_weekly_learning_plan.md
  - prompts/pacu_preceptor_debrief.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
---

# PACU Orientation — First Week Day-by-Day Plan

> Safety reminder: Draft Week-1 schedule. Verify against facility orientation program and the orientee's competency framework before adopting. Hands-on scope on Day 1–3 is intentionally restricted.

## Objective

Produce a **Day-by-Day Week-1 plan** that sequences pairing, observation targets, hands-on scope, end-of-shift debrief topics, and source readings across the orientee's first 3–5 shifts. Designed to scaffold an orientee from "shadow only" on Day 1 to "leading admission under primary preceptor cover" by end of Week 1.

## Inputs

- **Orientee background:** {{new-grad RN | experienced RN | etc.}}
- **Shifts in Week 1:** {{e.g., 3 × 12s, 4 × 10s, 5 × 8s}}
- **Primary preceptor available:** {{Mon/Tue/Wed | full week | partial week — name secondary preceptor coverage}}
- **Facility surgical mix on Week-1 days:** {{e.g., Mon = ortho/GYN, Tue = mixed general, Wed = ENT/ortho — best-known}}
- **Facility-mandated Week-1 items:** {{e.g., EHR competency, fire-and-safety training, blood-product administration training — paste in if known}}

## Audience / Scope

- **Primary:** Primary preceptor designing Week 1 with the orientee.
- **Secondary:** Unit educator reviewing for fit with the broader curriculum (`pacu_orientation_curriculum_designer.md`).
- **Scope:** Week 1 of a Phase 1 PACU orientation. Subsequent weeks live in `pacu_orientee_weekly_learning_plan.md`.

## Output requirements

```markdown
# PACU Orientation — Week 1 Day-by-Day Plan

> Safety reminder: Week-1 scope is intentionally narrow. Hands-on independent action is not the Week-1 goal.

**Orientee background:** {background}
**Week-1 shift count:** {count}
**Primary preceptor coverage:** {coverage}
**Surgical mix this week (declared):** {mix}

## Week-1 arc (one sentence)

By end of Week 1, the orientee can articulate the PACU admission workflow, has observed at least 3 inbound and 3 outbound handoffs, and has led one admission under direct primary-preceptor shadow.

## Day-by-day

Repeat the block below for each Week-1 shift.

### Day {N} — {Date placeholder} — {Shift hours}

**Theme:** {1-line theme — e.g., "Watch the workflow end-to-end" / "Co-admit with preceptor" / "Lead admission under preceptor shadow"}

**Pairing:** Primary preceptor / Secondary preceptor / Charge for orientation moments.

**Observation targets (what to watch for):**
- {target 1 — concrete, observable}
- {target 2}
- (3–4 items)

**Hands-on scope today:**
- {what orientee is permitted to do today, in scope-appropriate language}
- {explicit list of what is not in scope today, e.g., "no independent medication administration; preceptor draws and verifies"}

**Source reading (≤30 min, optional but recommended):**
- {chapter / module — rationale in one line}

**Mid-shift micro-check (5 min):**
- One concrete question the preceptor asks: {question}
- One concrete thing the orientee shares: {prompt}

**End-of-shift debrief topics (10–15 min):**
- {topic 1}
- {topic 2}
- (2–3 items — feeds `pacu_preceptor_debrief.md`)

**Question-log addition target:** {how many questions to log today — typically 3–5}

## End-of-Week-1 debrief

Run at end of last Week-1 shift. Themes:
- Did the orientee see the full admit-to-discharge arc at least once?
- Did Day 5 hands-on scope match Day 1 expectations (gradual expansion)?
- What surprised the orientee this week? What surprised the preceptor?
- Three things to start Week 2 with (continuity to `pacu_orientee_weekly_learning_plan.md` for Week 2).

## Background-specific adjustments applied

3–4 sentences naming exactly which Week-1 pacing choices were shaped by the orientee's background. For an experienced ICU RN: Day 1 shadow time is unchanged (workflow is unfamiliar), but Day 3 hands-on scope expands earlier on titration-and-monitoring tasks that transfer from ICU. For a new-grad: Day 5 still ends at "co-admit," not "lead admission."

## Sources / reference

- ASPAN *Standards* — orientation expectations for first week (foundation phase).
- *Drain's* — PACU admission workflow chapter.
- *ASPAN Core Curriculum* — orientation module.
```

## Must / Must not

**Must:**
- Match the user-declared shift count exactly.
- Sequence hands-on scope from shadow → co-admit → lead-under-shadow over the week.
- Include a mid-shift micro-check and an end-of-shift debrief on every day.
- Name pairing per shift (primary / secondary / charge).
- Adapt pacing to the orientee's background (visible in the adjustments paragraph).
- Reference `pacu_preceptor_debrief.md` for the debrief structure.

**Must not:**
- Schedule independent medication administration in Week 1 (defer to facility orientation program; default is "preceptor draws and verifies").
- Schedule charge nurse coverage as the orientee's primary preceptor.
- Specify named individuals.
- Invent facility-mandated Week-1 items (defer to facility orientation program checklist).
- Reference protected characteristics or license pathway.

## Quality signals

- A primary preceptor can post this on the bulletin board and run Week 1 from it.
- An orientee reading it on Sunday night knows what each shift will look like.
- The hands-on scope expansion across the week is visible and gradual.

## Verification

- [ ] Shift count matches input.
- [ ] Hands-on scope sequences shadow → co-admit → lead-under-shadow.
- [ ] Pairing named per shift.
- [ ] Mid-shift micro-check + end-of-shift debrief present every day.
- [ ] Background adjustments paragraph names concrete pacing decisions.
- [ ] No invented facility items.
- [ ] Safety reminder + FPP sections present.

## False-Positive Prevention

- **No invented facility-mandated Week-1 items** (EHR competency timing, fire safety training, mandatory videos). Use only what the user pasted.
- **No invented facility orientation program scope-expansion rules** ("at our facility, orientees can pull meds on Day 3"). Defer to facility.
- **No invented surgical-mix scheduling** beyond what the user declared.
- **No invented staff names.**
- **No invented competency thresholds** ("must complete 5 admissions to advance to Week 2").
- **No protected-characteristic references.**
- **No license-pathway scope decisions.**

## Worked Example

<details>
<summary>Example: new-grad RN, 3 × 12s, Mon–Wed, primary preceptor full week, ortho-heavy Mon (click to expand)</summary>

```markdown
### Day 1 — Mon — 0700–1930

**Theme:** Watch the workflow end-to-end.

**Pairing:** Primary preceptor, full shift.

**Observation targets:**
- The complete arc of one OR-to-PACU handoff, from CRNA arrival to admission documentation closed.
- The shape of an Aldrete/discharge-criteria assessment over time.
- One PACU-to-floor outbound handoff in full.

**Hands-on scope today:**
- May: attach monitors, position patient, take vitals with preceptor coaching.
- May not: administer meds, perform independent assessments, document independently.

**Source reading:**
- *Drain's*, PACU admission workflow chapter — ≤ 30 min, optional, end-of-day.

**Mid-shift micro-check:**
- Preceptor asks: "What did you notice about the handoff that you didn't expect?"
- Orientee shares: one question logged from morning.

**End-of-shift debrief:**
- What was the admission workflow's hardest step to follow?
- What did the CRNA mention in handoff that you'd want to learn more about?

**Question-log addition target:** 5+ questions.

### Day 2 — Tue — 0700–1930

**Theme:** Co-admit with preceptor.

**Pairing:** Primary preceptor, full shift.

**Hands-on scope:**
- May: take vitals, document baseline assessment, attach monitors, perform initial pain/PONV assessment under direct preceptor observation.
- May not: titrate meds, escalate independently.

(rest of day continues)

### Day 3 — Wed — 0700–1930

**Theme:** Lead admission under preceptor shadow.

**Pairing:** Primary preceptor, full shift, "preceptor of record but offstage" for one admission.

**Hands-on scope:**
- May: lead one admission end-to-end with preceptor present but not narrating.
- May not: still no independent med pull (per facility orientation program).

(rest)
```

Notes: Day 1 = shadow, Day 2 = co-admit, Day 3 = lead-under-shadow. Hands-on scope grows visibly without exceeding Week 1 cap. Medication-administration scope deferred to facility.
</details>

## Self-check

- [ ] Hands-on scope expands gradually across the week.
- [ ] Every day has a debrief.
- [ ] Pairing explicit on every day.
- [ ] Background adjustments visible.
- [ ] No invented facility items.
- [ ] Safety reminder + FPP sections passed.
