---
title: "Recovery One-Liner + Problem List — Compression Drill"
category: pacu-learning/stage-1-orientation
journey_stage: 1
benner_stage: "advanced-beginner"
competency_domains:
  - assessment-scoring
  - handoff-communication
  - professional-role-leadership
task_type: "drill"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, DS-06, RT-02, ED-02, QA-01]
difficulty: beginner
updated: "2026-07-16"
related_prompts:
  - pacu_orient_shift_structure_card.md
  - pacu_orient_outbound_sbar_report_rehearsal.md
  - pacu_orient_normal_vs_deviation_drill.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_handoff_script.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Drain's PeriAnesthesia Nursing (current edition)"
---

# Recovery One-Liner + Problem List — Compression Drill

> **Boundary:** A study drill, not live clinical decision support. Build real patient summaries with your preceptor.

## Objective

Train the learner to compress a whole recovering patient into a **one-sentence recovery status** plus a **short active-problem list** — the mental artifact that powers handoff, prioritization, and escalation. When a learner can say the one-liner, they understand the patient; when they can't, they've found their knowledge gap.

## Your Role

You supply (or accept) a patient picture, ask the learner to build the one-liner and problem list, then teach the compression: what belongs in the one sentence, what drops to the problem list, and what's noise. No invented numbers — the one-liner is built from categories, trends, and cues.

## Inputs

- `case` (optional): the drill generates a recovering patient if none given.
- `element_focus` (optional): stress a specific slot (e.g., the "watch-item").
- `rounds` (default 1).

## Method

1. **Define the one-liner shape:** [age/relevant descriptor] + [surgery/anesthesia category] + [current recovery trajectory] + [the one thing being watched]. It is a *status*, not a history dump.
2. **Build the active-problem list:** the 2–4 things actually in play this recovery (pain, PONV, airway watch, slow emergence, hemodynamic trend), each with its current state and reassess rhythm per facility.
3. **Cut the noise:** the learner marks what they *left out* and why (chronic-but-inactive, already-resolved).
4. **Pressure-test:** could a receiving nurse act on this one-liner? If not, which slot is thin?
5. **Name the discriminator** that makes this patient's problem list *this* patient's and not a template.
6. **Score and give one coaching point.**

## Output Format

```
ONE-LINER DRILL — ROUND [n]

>>> THE ONE-LINER
[one sentence: descriptor + surgery/anesthesia category + trajectory + watch-item]

>>> ACTIVE PROBLEM LIST (2–4)
1. [problem] — current state — reassess per facility
2. ...

>>> LEFT OUT (and why)
[chronic-inactive / resolved / noise]

>>> PRESSURE TEST
Could a receiver act on this? [Y/N]   Thin slot: [ / none]

>>> SCORE + COACHING
Compression: [tight / bloated / thin]
One coaching point: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `element_focus` | Deep-drill one slot (e.g., watch-item precision) |
| `rounds` | Multiple patients to build speed |
| `mode` | `build` (learner writes) vs. `critique` (learner fixes a bloated one-liner) |

## Verification Checklist

- [ ] One-liner is a **status**, not a history dump, and names a watch-item.
- [ ] Problem list is 2–4 active items, each with a reassess rhythm per facility.
- [ ] **No invented vitals/scores** — trends/categories/cues only.
- [ ] "Left out" reasoning is explicit (why it isn't active).
- [ ] Pressure test asks whether a receiver could act on it.
- [ ] Exactly one coaching point.

## Worked Example (compact)

**Input:** `case = total knee, spinal + sedation`.

**Output (excerpt):**
```
One-liner: Older adult s/p total knee under spinal, recovering as expected, watching for block regression and first return of motor function.
Problem list: 1) Regional block — assessing sensory/motor return, reassess per facility. 2) Pain — controlled per order as block recedes. 3) PONV — none, monitoring.
Left out: well-controlled chronic HTN (inactive this recovery).
Pressure test: yes — a receiver knows the story and the watch-item.
Coaching point: for a spinal, the watch-item is almost always block trajectory — make it the star of the one-liner.
```

> Safety reminder: A drill only — summarize real patients with your preceptor and escalate any active problem by role.
