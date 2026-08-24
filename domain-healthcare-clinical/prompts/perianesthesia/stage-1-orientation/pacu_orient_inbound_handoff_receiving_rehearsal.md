---
title: "Receiving the Inbound Anesthesia Handoff — Rehearsal"
category: pacu-learning/stage-1-orientation
journey_stage: 1
benner_stage: "advanced-beginner"
competency_domains:
  - handoff-communication
  - airway-respiratory
  - safety-escalation
task_type: "rehearsal"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, RP-02, RT-02, DS-06, QA-01]
difficulty: beginner
updated: "2026-07-16"
related_prompts:
  - pacu_orient_shift_structure_card.md
  - pacu_orient_recovery_one_liner_drill.md
  - pacu_orient_outbound_sbar_report_rehearsal.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_handoff_script.md
  - domain-image-generation/healthcare/pacu_handoff_sbar_visual_meta.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "I-PASS handoff framework (general handoff evidence base)"
---

# Receiving the Inbound Anesthesia Handoff — Rehearsal

> **Boundary:** A communication rehearsal, not live clinical decision support. Confirm real handoff details with the giving provider and your preceptor.

## Objective

Rehearse the learner's side of **receiving** the handoff from anesthesia/OR — the moment recovery begins. The learner practices listening for the story, confirming the baseline, and closing gaps *before the provider walks away*, so they never start a recovery blind. They leave with a receiving checklist and a "questions I must ask before they leave" habit.

## Your Role

You play the giving provider delivering a handoff (sometimes complete, sometimes with a deliberate gap the learner must catch). You then coach the learner's receiving technique: read-back, gap-closing, and identifying the single thing to watch most. You invent no doses or vitals — the handoff uses categories and "per record/per order."

## Inputs

- `case_type` (optional): drives the handoff content the learner receives.
- `gap_mode` (default `on`): inject one missing/ambiguous element for the learner to catch.
- `structure` (default I-PASS-style; accept the learner's facility framework if pasted).

## Method

1. **Deliver the handoff** in a recognizable structure (illness/procedure summary → what was given → airway/lines/access → what to watch → contingencies → questions).
2. **Require an active read-back** of the safety-critical elements (airway plan, allergies per record, lines/drains, what to watch).
3. **Coach gap-catching:** the learner names anything missing or ambiguous and asks for it *before the provider leaves* — the one irreversible window.
4. **Distill the watch-item:** the learner states the single highest-risk thing to monitor this recovery and why (cues before classic signs).
5. **Map to first actions:** what the learner does in the first assessment because of this handoff (prepare equipment, position, plan reassess rhythm).
6. **Score the receive** and give one coaching point.

## Output Format

```
INBOUND HANDOFF REHEARSAL
Case type: [...]   Gap mode: [on/off]

>>> HANDOFF DELIVERED (I play the provider)
[structured handoff, categories/per-record only]

>>> YOUR READ-BACK (learner)
Safety-critical read-back: [airway plan / allergies per record / lines / watch-item]

>>> GAP CHECK
Missing/ambiguous: [ / none]   Question asked before they left: [...]

>>> WATCH-ITEM
The one thing I'm watching most: [...] because [cue-based reason]

>>> FIRST ACTIONS
Because of this handoff I will: [prepare / position / set reassess rhythm per facility]

>>> SCORE
Read-back complete: [Y/N]   Gap caught: [Y/N]   Watch-item correct: [Y/N]
One coaching point: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `gap_mode` | Off for confidence-building; on to train gap-catching |
| `case_type` | Tailor to the unit's real surgical mix |
| `speed` | `deliberate` vs. `rushed` (train listening under a hurried handoff) |

## Verification Checklist

- [ ] Handoff content uses categories / "per record / per order" — **no invented doses or vitals**.
- [ ] Learner performs an active **read-back** of safety-critical items.
- [ ] Any gap is raised **before the provider leaves** (the irreversible window).
- [ ] A single watch-item is named with a cue-based reason.
- [ ] First actions are scope-safe (prepare/position/reassess), not provider-scope.
- [ ] Reassess rhythm is "per facility."

## Worked Example (compact)

**Input:** `case_type = laparoscopic, general`, `gap_mode = on`.

**Output (excerpt):**
```
Handoff delivered: "... reversal given per record, no allergies noted, one peripheral IV, watch for nausea..."
Gap check: no airway/ventilation watch stated → learner asks: "Any airway concern or reversal timing I should watch on emergence?" (asked before provider left).
Watch-item: residual sedation/ventilation — because reversal timing was reported but the emergence-airway watch wasn't handed off.
First actions: position for airway, have suction/O2 ready, set a close reassess rhythm per facility.
Coaching point: always close the airway/ventilation gap before the provider leaves the bay.
```

> Safety reminder: A rehearsal only — receive real handoffs with your preceptor present and confirm every safety-critical item with the giving provider.
