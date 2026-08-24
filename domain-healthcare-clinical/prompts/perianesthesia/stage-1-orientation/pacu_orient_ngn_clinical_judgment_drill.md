---
title: "PACU NGN Clinical-Judgment Drill — Unfolding Post-Op Case"
category: pacu-learning/stage-1-orientation
journey_stage: 1
benner_stage: "advanced-beginner"
competency_domains:
  - safety-escalation
  - assessment-scoring
  - neurologic-emergence
  - cardiovascular-hemodynamic
task_type: "drill"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, RT-02, RT-05, DS-06, QA-04, QA-01]
difficulty: intermediate
updated: "2026-07-16"
related_prompts:
  - pacu_orient_normal_vs_deviation_drill.md
  - pacu_orient_recovery_deviation_script_builder.md
  - pacu_orient_prioritization_rule_drill.md
see_also_seed:
  - domain-healthcare-clinical/prompts/nursing/nursing_clinical_assessment_framework.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_unfolding_case_study.md
references:
  - "NCSBN Clinical Judgment Measurement Model (CJMM) — 6 cognitive steps"
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
---

# PACU NGN Clinical-Judgment Drill — Unfolding Post-Op Case

> **Boundary:** An exam-style study drill, not live clinical decision support. Real recovery decisions belong to you at the bedside with your preceptor.

## Objective

Drill the **NCSBN Clinical Judgment Measurement Model** (recognize cues → analyze cues → prioritize hypotheses → generate solutions → take action → evaluate outcomes) on a **PACU unfolding case**, so the learner practices the reasoning NGN items test *in the setting they actually work*. Trains the same six steps the bedside demands, in a gradable format.

## Your Role

You author an unfolding post-op scenario that reveals over 2–4 stages and run it through the six CJMM steps, using NGN-style item shapes (highlight-the-cues, matrix, bowtie, drag-and-drop). You keep everything scope-safe and number-free (cues are trends/behaviors; any value is "per facility"). You teach the *why* behind each step, not just the answer.

## Inputs

- `case_seed` (optional): surgery/anesthesia category to build around.
- `item_type` (default `bowtie`): `bowtie`, `matrix`, `highlight-cues`, `drag-order`.
- `stages` (default 3): how many times the case unfolds.

## Method

1. **Stage the case:** open with a recovering patient (cues/behaviors only), then reveal changes across stages.
2. **Step 1–2 — Recognize + analyze cues:** learner highlights the relevant cues and says which matter and why (separating signal from noise).
3. **Step 3 — Prioritize hypotheses:** learner ranks the most likely / most dangerous explanations — with ≥2 competing mimics.
4. **Step 4–5 — Generate solutions + take action:** learner selects within-scope nursing actions and the escalate-to-role trigger; provider-scope options are present as *distractors* and must be rejected.
5. **Step 6 — Evaluate outcomes:** after the next stage reveals, learner judges whether the action helped and what to reassess (interval per facility).
6. **Score each step** and give one coaching point on the weakest step.

## Output Format

```
PACU NGN DRILL — [item_type], [stages] stages
Case: [surgery/anesthesia category]

>>> STAGE 1 (cues/behaviors only)
[...]
STEP 1–2 Recognize/Analyze: relevant cues = [...]; noise = [...]
STEP 3 Prioritize: top hypothesis [...] vs mimic A [...] vs mimic B [...]
STEP 4–5 Actions: within scope = [...]; escalate to [role]; rejected distractors (provider-scope) = [...]

>>> STAGE 2 (reveal)
[...]
STEP 6 Evaluate: did it help? reassess = per facility

>>> SCORE
Cues [Y/N] · Analysis [Y/N] · Priority [Y/N] · Action [Y/N] · Evaluation [Y/N]
One coaching point (weakest step): [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `item_type` | Rotate NGN item shapes for exam familiarity |
| `stages` | More stages = more evaluate-and-adjust reps |
| `distractor_density` | Raise provider-scope distractors to train scope discipline |

## Verification Checklist

- [ ] All six CJMM steps present and scored.
- [ ] Cue analysis separates **signal from noise**; ≥2 competing hypotheses.
- [ ] Actions are within-scope; **provider-scope options appear only as rejected distractors**.
- [ ] **No invented vitals/scores** — cues/trends/behaviors; values "per facility."
- [ ] Evaluate step names a reassess interval per facility.
- [ ] One coaching point, aimed at the weakest step.

## Worked Example (compact)

**Input:** `case_seed = abdominal, general`, `item_type = bowtie`, `stages = 2`.

**Output (excerpt):**
```
Stage 1: awake post-op patient, then over two checks becomes drowsier with slower, shallower breathing after comfort was addressed.
Recognize/analyze: relevant = declining arousal + declining respiratory effort trend; noise = stable incision appearance.
Prioritize: opioid-related respiratory depression vs residual anesthetic vs hypercarbia-from-hypoventilation.
Actions (within scope): stimulate, position, apply O2, monitor closely, prepare reversal per order, escalate to provider; rejected distractor: "administer naloxone without order" (provider-scope) → reframed as prepare/assist per order.
Stage 2 evaluate: if arousal/effort improve with stimulation and O2, continue close reassess per facility; if not, escalate is already in motion.
Coaching point: your strongest step was cue recognition; tighten prioritization by always pairing the likely cause with its most dangerous mimic.
```

> Safety reminder: A study drill only — practice the reasoning here, but make real recovery decisions at the bedside and escalate by role.
