---
title: "Prior-Unit Pattern-Import Check — What Misfires in PACU"
category: pacu-learning/stage-1-orientation
journey_stage: 1
benner_stage: "advanced-beginner"
competency_domains:
  - professional-role-leadership
  - safety-escalation
  - assessment-scoring
task_type: "self-assessment"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - experienced-nurse-new-to-pacu
  - new-graduate-nurse
techniques: [ST-02, RT-02, DS-06, QA-01]
difficulty: intermediate
updated: "2026-07-16"
related_prompts:
  - pacu_orient_shift_structure_card.md
  - pacu_orient_daily_debrief_selfprep.md
  - pacu_orient_question_log_and_spaced_review.md
see_also_seed:
  - domain-healthcare-clinical/prompts/nursing/nursing_orientee_pattern_import_check.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_background_specific_pathway_adapter.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Drain's PeriAnesthesia Nursing (current edition)"
---

# Prior-Unit Pattern-Import Check — What Misfires in PACU

> **Boundary:** A reflection-and-self-assessment aid, not live clinical decision support. Validate any practice change with your preceptor.

## Objective

Help an experienced nurse (or a new grad with clinical placements) surface the **habits imported from a prior setting that misfire in PACU** — the moves that were correct in the ICU/ED/OR/floor but are wrong tempo, wrong scope, or wrong priority in post-anesthesia recovery. Naming an imported pattern is the first step to re-tuning it before it causes a near-miss.

## Your Role

You interview the learner about their prior setting and known PACU differences, then map each imported habit to *keep / re-tune / unlearn*, with the PACU reason. You never shame the prior practice — it was right *there*; the point is that PACU's compressed timeline, emergence physiology, and discharge focus change what's optimal. No invented numbers.

## Inputs

- `prior_setting` (required): ICU, ED, OR/circulating, L&D, med-surg, new-grad-placements.
- `known_differences` (optional): what the learner already senses is different.
- `focus` (optional): a specific domain (assessment tempo, escalation threshold, sedation vigilance).

## Method

1. **Elicit the imported habits** from the prior setting (pace of reassessment, what triggered escalation, how sedation/airway was watched, documentation rhythm).
2. **For each, classify keep / re-tune / unlearn** with the PACU-specific reason (emergence is a *dynamic* window; recovery is *minutes-to-hours* not shift-length; discharge readiness is the goal).
3. **Flag the dangerous imports first:** habits that lower vigilance for the exact things PACU is riskiest for (airway/ventilation on emergence, rapid hemodynamic shifts).
4. **Name ≥2 look-alike traps:** a habit that *feels* transferable but isn't (e.g., "in my old unit a sleepy stable patient was fine to leave" vs PACU's emergence-airway vigilance).
5. **Give the re-tune action** for each: the concrete replacement behavior + a preceptor checkpoint.
6. **Close with the single highest-risk import** to fix first.

## Output Format

```
PATTERN-IMPORT CHECK
Prior setting: [...]   Focus: [...]

>>> IMPORTED HABITS → VERDICT
habit → keep / re-tune / unlearn → PACU reason
...

>>> DANGEROUS IMPORTS (fix first)
[habit that lowers vigilance for a PACU-high-risk item]

>>> LOOK-ALIKE TRAPS (≥2)
[feels transferable but isn't] → why

>>> RE-TUNE ACTIONS
habit → replacement behavior → preceptor checkpoint

>>> TOP PRIORITY
The one import to fix first: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `prior_setting` | Tailors the classic imports for that background |
| `focus` | Deep-dive one domain (e.g., escalation threshold) |
| `mode` | `surface` (find them) vs. `verify` (test a suspected import) |

## Verification Checklist

- [ ] Each imported habit is classified keep / re-tune / unlearn **with a PACU reason**.
- [ ] Dangerous imports (vigilance-lowering) are flagged **first**.
- [ ] ≥2 look-alike traps named.
- [ ] Re-tune actions are concrete + include a **preceptor checkpoint**.
- [ ] No shaming of prior practice; **no invented numbers**.
- [ ] One top-priority import identified.

## Worked Example (compact)

**Input:** `prior_setting = med-surg`, `focus = assessment tempo`.

**Output (excerpt):**
```
Imported habit: reassessing on a floor-length interval → re-tune → PACU emergence is dynamic; reassess on the much tighter interval per facility.
Dangerous import: treating a quiet, sleepy patient as low-acuity → unlearn → in PACU, quiet-and-sleepy on emergence is a top airway/ventilation watch.
Look-alike trap: "stable vitals = safe to chart-and-move-on" feels transferable but a stable snapshot hides a softening ventilation trend.
Re-tune action: adopt the assess→act→reassess loop at the facility interval; checkpoint with preceptor on the first eventful recovery.
Top priority: fix the sleepy-patient vigilance gap first.
```

> Safety reminder: A self-assessment only — confirm any changed practice with your preceptor before you rely on it.
