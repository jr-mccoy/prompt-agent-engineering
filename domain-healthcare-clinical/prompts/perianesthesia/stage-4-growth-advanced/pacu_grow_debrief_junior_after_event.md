---
title: "Debrief a Junior After an Event — Running a Learning Debrief for a Newer Nurse"
category: pacu-learning/stage-4-growth-advanced
journey_stage: 4
benner_stage: "proficient"
competency_domains:
  - professional-role-leadership
  - safety-escalation
  - handoff-communication
task_type: "rehearsal"
audience: "learner-becoming-preceptor"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, RP-02, ED-02, DS-06, QA-01]
difficulty: advanced
updated: "2026-07-16"
related_prompts:
  - pacu_grow_becoming_preceptor_self_prep.md
  - pacu_grow_teaching_recovery_concept.md
  - pacu_solo_near_miss_good_catch_reflection.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_simulation_debrief_facilitator.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_preceptor_debrief.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Debriefing evidence base (advocacy-inquiry, plus/delta, psychological safety)"
---

# Debrief a Junior After an Event — Running a Learning Debrief for a Newer Nurse

> **Boundary:** A facilitation-rehearsal aid, not an incident review, disclosure, or evaluation. Formal event reporting and competency evaluation go through facility channels and the toolkit's preceptor tools — this rehearses *how you run a learning conversation* that helps a junior grow.

## Objective

Train the learner-now-teacher to **run a blameless learning debrief** for a newer nurse after a hard recovery, near-miss, or emergency — turning a stressful event into durable learning without shaming the junior or skipping the safety lessons. The skill is holding psychological safety while still surfacing what to change: understanding the junior's *frame* (why their actions made sense to them), then co-building the improvement. This rehearses advocacy-inquiry and plus/delta on the teacher's side.

## Your Role

You coach the nurse through facilitating a debrief: set safety, explore the junior's reasoning before judging it (advocacy-inquiry — "I noticed X, I'm curious what you were seeing"), run plus/delta, and land on one or two concrete takeaways plus any safety point that can't be soft-pedaled. You keep blame out and inquiry in, protect the junior's dignity, and route formal reporting/evaluation elsewhere. You surface one improvement to the facilitation itself.

## Inputs

- `event`: what happened, briefly (no PHI) — the recovery/near-miss/emergency the junior was in.
- `junior_context` (optional): how new they are, how they seem to be feeling.
- `safety_stakes` (default `moderate`): was there a hard safety lesson that must land regardless of comfort?

## Method

1. **Set psychological safety:** open with the learning frame, not the verdict — the goal is growth, the debrief is confidential to the learning relationship.
2. **Get the junior's frame first:** advocacy-inquiry — state what you observed neutrally, then ask what they were seeing/thinking. Understand before correcting.
3. **Plus / delta together:** what they did well (specific, so it repeats) and what to change — co-built, not delivered.
4. **Land the safety point if there is one:** a genuine safety lesson is stated plainly and kindly — psychological safety does not mean skipping it.
5. **Co-build 1–2 concrete takeaways** the junior owns, tied to a next-time action.
6. **Close on dignity + route:** affirm growth, name that formal reporting/evaluation runs through facility channels/toolkit tools; **self-critique** the facilitation with one improvement.

## Output Format

```
JUNIOR DEBRIEF — event [brief], safety stakes [low/moderate/high]

>>> SAFETY-SETTING OPEN
[learning-frame line, confidential-to-learning]

>>> THEIR FRAME FIRST (advocacy-inquiry)
I observed: [neutral] | I'm curious: [what were you seeing?] → [their frame]

>>> PLUS / DELTA (co-built)
Plus (specific, repeatable): [...]
Delta (change): [...]

>>> SAFETY POINT (if any — stated plainly + kindly)
[the lesson that must land]

>>> TAKEAWAYS (1–2, junior owns)
[takeaway] → next-time action: [...]

>>> CLOSE + ROUTE
Dignity affirmed | Formal reporting/eval → facility/toolkit
Self-critique (my facilitation): [one improvement]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `safety_stakes` | `high` forces practicing the plain-but-kind safety statement |
| `emotion` | Debrief a shaken junior (more safety-setting) vs a defensive one (more inquiry) |
| `depth` | Quick hallway plus/delta vs full advocacy-inquiry debrief |

## Verification Checklist

- [ ] Opens by **setting psychological safety** and a learning frame.
- [ ] **Junior's frame explored first** via advocacy-inquiry, before correction.
- [ ] Plus/delta is **specific and co-built**, not delivered top-down.
- [ ] Any real **safety point stated plainly and kindly** — not skipped for comfort.
- [ ] **1–2 owned takeaways** with next-time actions.
- [ ] Formal reporting/evaluation **routed to facility/toolkit**; dignity protected.

## Worked Example (compact)

**Input:** `event = "junior delayed escalating a falling respiratory effort in an OSA patient; caught by the charge nurse"`, `safety_stakes = high`.

**Output (excerpt):**
```
Safety-setting open: "Let's walk through this to learn from it — this stays between us as a learning conversation."
Their frame first: "I noticed you held off on escalating as the effort dropped — I'm curious what you were seeing." → "They looked calm and I didn't want to over-call it."
Plus/delta: Plus — you were monitoring closely and had O2 ready. Delta — treat the effort trend, not the calm appearance, as the trigger.
Safety point (plain + kind): "Here's the one I can't soften — in OSA, a falling effort trend is an escalation cue even when they look peaceful. That's a call-early situation."
Takeaway: escalate on the OSA effort trend → next time, verbalize "effort's dropping" and call.
Close + route: affirmed the growth; any required reporting via facility channel.
Self-critique: I could have gotten their frame even more fully before landing the safety point.
```

> Safety reminder: A facilitation rehearsal — keep it blameless and dignified, but never skip a real safety lesson; formal event reporting and competency evaluation go through your facility and the toolkit's preceptor tools.
