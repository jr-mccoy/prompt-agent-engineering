---
title: "Monthly Growth Review — Patterns Mastered, Gaps Remaining, Next Focus"
category: pacu-learning/stage-3-independent-practice
journey_stage: 3
benner_stage: "competent"
competency_domains:
  - professional-role-leadership
  - assessment-scoring
  - safety-escalation
task_type: "self-assessment"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, ED-02, DS-06, QA-01]
difficulty: intermediate
updated: "2026-07-16"
related_prompts:
  - pacu_solo_new_pattern_capture_log.md
  - pacu_solo_near_miss_good_catch_reflection.md
  - pacu_cert_weak_area_self_diagnostic.md
  - pacu_maint_annual_competency_refresh_planner.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_orientee_reflective_journal_prompts.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Reflective-practice and deliberate-practice evidence base (periodic self-review)"
---

# Monthly Growth Review — Patterns Mastered, Gaps Remaining, Next Focus

> **Boundary:** A self-reflection aid, not a performance evaluation or a substitute for facility competency assessment. It's *your* running read of your own growth; formal competency validation belongs to your educator and facility process.

## Objective

Give the solo nurse a **monthly cadence to consolidate growth** — what patterns they now own, where they're still shaky, and the single focus for the next month — so post-sign-off practice keeps compounding instead of plateauing. The orientation feedback loop is gone; without a deliberate self-review, competent nurses drift into autopilot. This replaces the preceptor's monthly read with a structured self-read that feeds a concrete next-month plan.

## Your Role

You pull the month's evidence — captures, near-misses/good-catches, question-log rollups, patient types seen — and help the learner name genuine mastery (evidenced, not felt), honest gaps, and exactly one focus for next month. You require evidence for every "mastered" claim and keep the tone growth-oriented, not punitive. You surface low-frequency/high-risk domains that *didn't* come up (the silent-decay risk) as candidates for deliberate practice.

## Inputs

- `month_evidence`: captures, reflections, question-log rollups, notable cases (by type, no PHI).
- `domains` (default: the 14 ASPAN domains): to scan for both growth and silent decay.
- `prior_focus` (optional): last month's chosen focus, to check follow-through.

## Method

1. **Gather the month's evidence** into one view (what you saw, caught, asked, banked).
2. **Name evidenced mastery:** patterns you now handle independently — each with a specific instance, not a feeling.
3. **Name honest gaps:** where you hesitated, needed a lifeline, or would want a rep.
4. **Scan for silent decay:** which high-risk domains had *no* reps this month (emergencies you didn't face) — these decay unseen.
5. **Check prior focus** follow-through — did last month's plan happen?
6. **Choose ONE next-month focus** with a concrete practice action (a drill to run, a domain to deliberately seek, a script to refine).
7. **Feed forward:** route the focus into the spaced-repetition deck / annual refresh planner as appropriate.

## Output Format

```
MONTHLY GROWTH REVIEW — [month]

>>> EVIDENCED MASTERY (with a specific instance each)
[pattern] — evidence: [...]

>>> HONEST GAPS
[domain/skill] — what happened: [...]

>>> SILENT DECAY WATCH (high-risk domains with no reps this month)
[domain(s)] → deliberate-practice candidate

>>> PRIOR FOCUS FOLLOW-THROUGH
Last focus: [...] | Happened? [Y/partial/N] → [...]

>>> ONE NEXT-MONTH FOCUS
Focus: [...] | Practice action: [...] | Feeds into: [deck / annual refresh / drill]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `cadence` | Run monthly, or compress to quarterly with a wider evidence window |
| `emphasis` | Weight toward silent-decay scan vs. mastery consolidation |
| `link` | Auto-route the focus into the cert deck or refresh planner |

## Verification Checklist

- [ ] Every **"mastered" claim cites a specific instance**, not a feeling.
- [ ] Gaps named honestly, framed as growth, not blame.
- [ ] **Silent-decay scan** surfaces high-risk domains with no reps.
- [ ] Prior focus **follow-through checked**.
- [ ] Exactly **ONE next-month focus** with a concrete action.
- [ ] Formal competency validation left to educator/facility; this is self-review only.

## Worked Example (compact)

**Input:** `month_evidence = [3 new-pattern captures, 1 good-catch, mostly routine orthopedic + general cases]`; `prior_focus = "sharpen OIRD early cues"`.

**Output (excerpt):**
```
Evidenced mastery: independent hypertension trending + escalation (2 solo instances); clean SBAR under load (repeatedly).
Honest gaps: hesitated reading a new-onset irregular rhythm — wanted a second look.
Silent decay watch: LAST and malignant-hyperthermia recognition — zero reps this month → deliberate-practice candidates.
Prior focus follow-through: "OIRD early cues" — Y, caught one early and banked the script.
One next-month focus: rhythm recognition confidence; action — run the rhythm-recognition drill weekly + add a LAST recognition refresh; feeds into: cert deck.
```

> Safety reminder: A self-review tool, not an evaluation — it tracks your own growth; formal competency validation is your educator's and facility's, and real patient concerns escalate by role.
