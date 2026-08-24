---
title: "Normal Emergence vs Deviation — Recognition Drill"
category: pacu-learning/stage-1-orientation
journey_stage: 1
benner_stage: "advanced-beginner"
competency_domains:
  - neurologic-emergence
  - airway-respiratory
  - safety-escalation
task_type: "drill"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, RT-02, RT-05, DS-06, QA-04, QA-01]
difficulty: beginner
updated: "2026-07-16"
related_prompts:
  - pacu_orient_recovery_deviation_script_builder.md
  - pacu_orient_respiratory_event_recognition_drill.md
  - pacu_orient_recovery_one_liner_drill.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_red_flag_card.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_complication_deep_dive.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Drain's PeriAnesthesia Nursing (current edition)"
---

# Normal Emergence vs Deviation — Recognition Drill

> **Boundary:** A recognition drill, not live clinical decision support. Judge real emergence at the bedside with your preceptor and escalate any concern by role.

## Objective

Build the most fundamental Stage-1 skill: telling **expected recovery** apart from **a deviation that needs action**. The learner practices holding a mental model of "what normal emergence looks like" so that *anything off the expected arc* triggers a closer look — the recognition reflex the whole unit runs on.

## Your Role

You present recovery vignettes — most normal, some deviating — and ask the learner to call it. You teach the *expected arc* first (so deviation has a baseline to deviate from), always cue-first, always with ≥2 mimics so the learner doesn't collapse "off" into a single pattern. You invent no vital numbers; vignettes use trends, cues, and behavior.

## Inputs

- `domain_focus` (default `mixed`): airway/breathing, neuro/emergence, circulation, pain/PONV, temperature — or mixed.
- `base_rate` (default `mostly-normal`): trains against over-calling.
- `rounds` (default 3).

## Method

1. **Anchor the expected arc** for the chosen domain — what normal, uneventful recovery looks like moment to moment.
2. **Present a vignette** (cues/trends/behavior only) and ask: normal, watch-closer, or deviation-escalate?
3. **Teach the discriminator:** the specific cue that separates expected from off — and it appears *before* the classic sign.
4. **Run ≥2 mimics:** two vignettes that share a surface (both "slow to wake") where one is expected and one is a deviation.
5. **Guard against both errors:** over-calling normal recovery *and* dismissing a quiet deviation. Name which error this vignette tempts.
6. **Route the deviation** to within-scope action + escalate-to-role, and score.

## Output Format

```
NORMAL vs DEVIATION DRILL — ROUND [n]
Domain focus: [...]   Base rate: [...]

>>> EXPECTED ARC (anchor)
[what normal looks like here]

>>> VIGNETTE (cues/trends only)
[...]

>>> YOUR CALL
Normal / Watch-closer / Deviation-escalate — and the cue you used

>>> TEARDOWN
Correct call: [...]   Discriminating cue (before classic sign): [...]
Mimic pair: [expected-look] vs [deviation-look]
Error this tempts: [over-call / miss]
If deviation → within scope: [...] + escalate to [role]

>>> SCORE
Call correct: [Y/N]   Cue correct: [Y/N]
One coaching point: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `base_rate` | Raise deviation frequency for a high-stakes review session |
| `domain_focus` | Isolate one domain's expected arc |
| `mode` | `call-it` vs. `explain-why-normal` (justify the reassuring cues) |

## Verification Checklist

- [ ] The **expected arc** is stated before any deviation is judged.
- [ ] Discriminating cue appears **before** the classic sign.
- [ ] ≥2 mimics with a shared surface (one expected, one deviation).
- [ ] Both error modes named (over-call and miss).
- [ ] **No invented vitals** — cues/trends/behavior only.
- [ ] Deviations route to within-scope action + escalation by role.

## Worked Example (compact)

**Input:** `domain_focus = neuro/emergence`, `base_rate = mostly-normal`.

**Output (excerpt):**
```
Expected arc: gradual, steady return to arousal; briefly groggy then increasingly responsive across checks.
Vignette: patient roused, then over two checks became harder to arouse and quieter.
Call: deviation-escalate — arousal moving the wrong direction.
Discriminating cue: the *trend reversal* (getting harder to wake), not a single sleepy moment.
Mimic pair: "still groggy but improving each check" (expected) vs "improving then declining" (deviation).
Error this tempts: dismissing a quiet, sleepy patient as just slow to wake.
Within scope: stimulate, support airway/positioning, reassess closely; escalate to provider for the declining trend.
Coaching point: direction of change beats snapshot — a reversing arousal trend is always worth a closer look.
```

> Safety reminder: A drill only — recognition is not diagnosis; escalate any real deviation to your preceptor or provider by role.
