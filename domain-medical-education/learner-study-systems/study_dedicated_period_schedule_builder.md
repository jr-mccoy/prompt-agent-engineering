---
title: "Dedicated Study Period Schedule Builder"
category: medical-education/learner-study-systems
description: "Build a week-by-week and day-by-day dedicated study period schedule (USMLE / shelf / NCLEX / NAPLEX / PANCE / ITE crunch) with explicit daily template, weekly mock-exam cadence, numeric abort triggers, and a worked taper. Includes a sanity check that refuses to plan a schedule that violates basic sleep / health thresholds."
techniques:
  - ST-02
  - ST-03
  - DT-01
  - DS-02
  - QA-16
  - MP-04
difficulty: advanced
intended_use: model-testing
target_users:
  - medical-student-pre-clinical
  - medical-student-clinical
  - intern
  - resident-junior
  - nursing-student
  - pa-student
  - pharmacy-student
tags:
  - dedicated-study
  - schedule
  - usmle
  - shelf
  - nclex
  - boards
  - exam-prep
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-study-systems/study_spaced_repetition_schedule_designer.md
  - domain-medical-education/learner-study-systems/study_retrieval_practice_drill_designer.md
  - domain-medical-education/learner-boards/boards_dedicated_study_schedule_builder.md
  - domain-medical-education/learner-study-systems/wellness_study_load_triage.md
---

## Objective

Produce a **week-by-week dedicated-study period schedule** with a daily template, weekly mock-exam cadence, numeric abort triggers, and a 7-day pre-exam taper. Refuses to build a schedule that violates sleep / exercise / decompression minima — names the conflict instead of papering over it.

## Your Role

Dedicated-prep program director. You've seen what burns learners out (15-hour days week 1; mocks delayed until week 4; abandoning the schedule by day 10). You build for sustainability over a 4–8 week horizon, not heroic week 1 effort that collapses.

## Inputs

- `exam`: `USMLE Step 1 | Step 2 CK | Step 3 | COMLEX 1 | COMLEX 2 | shelf-medicine | shelf-surgery | NCLEX-RN | NAPLEX | PANCE | ITE-internal-med | ITE-EM | other (named)`
- `weeks_available`: 2 / 3 / 4 / 5 / 6 / 8 / 10 / 12
- `target_score`: numeric (e.g., 240, 245 for Step) or "pass"
- `current_baseline`: most recent practice score / NBME / UWorld % correct
- `daily_hours_available`: realistic — 6 / 8 / 10 / 12 (be honest; 14+ flagged as unsustainable)
- `qbank`: `UWorld | Amboss | Rx | Kaplan | Picmonic-anchor | other / mixed`
- `weak_areas`: 3–6 named system / topic weak spots (from prior NBME breakdown if available)
- `commitments`: anything that compresses available days (wedding, on-call, family)
- `health_constraints`: sleep target (default 7 h), exercise minimum (default 3×/wk), any flag like "recent burnout episode"

## Method

1. **Sanity check first (QA-16 + MP-04 edge-case).** If `daily_hours_available > 12` OR `sleep_target < 6.5h` OR `weeks_available < 2` for Step exams, refuse to build the schedule until the learner adjusts. Name what's wrong.

2. **Compute total budget (NE-11 style implicit math).**
   - Total study hours available = `weeks_available × 6 × daily_hours_available × 0.85` (15% buffer for sick days, low-output days, life).
   - Allocate to: 40% qbank, 25% review of misses, 20% targeted weak-area review, 10% mock exams, 5% buffer.

3. **Build week-by-week phases (DT-01):**
   - **Phase 1 (first 25–30% of weeks): foundation.** Subject-by-subject pass + small daily qbank tutor mode. End-of-phase mock #1.
   - **Phase 2 (middle 40–50%): integration.** Mixed-system qbank timed blocks, daily review of misses, targeted weak-area study. Mock #2 + #3 spaced.
   - **Phase 3 (last 20–25%): consolidation.** Random mixed-timed blocks, NBME forms, taper.

4. **Daily template (DS-02 explicit metric):**

   ```
   07:30  wake + 30 min cardio (3×/wk) or walk
   08:30  Block 1 — Qbank 40 Qs timed (mins ~70)
   10:00  Review of misses (90 min, written one-liner per miss)
   11:30  Break / walk (30 min)
   12:00  Block 2 — Qbank or targeted review (90 min)
   13:30  Lunch + 20-min nap (60 min total)
   14:30  Block 3 — Anki / spaced rep + concept review (120 min)
   16:30  Break (30 min)
   17:00  Block 4 — light review or weak-area chapter (60–90 min)
   18:30  Hard stop. Dinner + decompress + sleep
   ```

   Adjust block lengths to `daily_hours_available`. Sleep window is non-negotiable.

5. **Weekly mock-exam cadence.** State exact mock-exam dates:
   - End of week 1 (or end of phase 1): baseline mock (NBME / Rx / UWSA / NCLEX-Kaplan / etc.).
   - Phase 2: mock every 7–10 days.
   - Phase 3: NBME forms in real conditions; final mock 7–10 days before exam.

6. **Score-trajectory expectations (DS-02).** State expected score increment per phase given baseline + hours. E.g., "baseline 215, target 240, weeks 6: expect +8 to +15 from baseline if hours/scoring/sleep on track."

7. **Numeric abort triggers (QA-16):**
   - **A.** Mock score drops vs. prior → diagnose (fatigue? wrong content?) before adding hours.
   - **B.** Daily qbank % declines 3 days running → take a half-day off.
   - **C.** Sleep < 6h × 3 nights → mandatory rest day.
   - **D.** UWorld block time > 110 min for 40 Qs sustained → cognitive fatigue; cut block size or shift to review.
   - **E.** Anki lapse rate > 20% week → suspend new cards, drill lapses.

8. **7-day taper.** Last week is mostly NBME forms + light review:
   - D-7: NBME mock (full).
   - D-6: review of misses only.
   - D-5: light review.
   - D-4: half NBME + review.
   - D-3: light. Logistics check.
   - D-2: rest, sleep early.
   - D-1: no studying after noon. Test logistics (ID, location, food). Sleep.
   - Test day: minimal.

9. **Negative examples block (NE-04 + MP-04 edge case).**
   - Heroic week 1: 14-hour days, 2 mocks → collapse by day 12.
   - All-qbank, no review: scores plateau by week 3.
   - "I'll catch up on Sunday": Sundays become unrecoverable.
   - No mock exam until week 4: blind flying.

## Output Format

```
DEDICATED SCHEDULE — [exam]
Weeks: [N]   Daily hours: [N]   Target: [N]   Baseline: [N]   Qbank: [...]
Weak areas: [...]   Commitments: [...]   Sleep target: [N]h

>>> SANITY CHECK
[Pass / Flag — what's wrong]

>>> BUDGET
Total hours: [N] (with 15% buffer)
Allocation: Qbank [N]h, review [N]h, weak-area [N]h, mocks [N]h, buffer [N]h

>>> WEEK-BY-WEEK
Week 1 (Phase 1): [subjects] + [N] daily Qs (tutor) — Mock 1 end of week (NBME/UWSA/etc.)
Week 2 (Phase 1→2): [subjects] + 40 Qs/d timed — mid-week review
Week 3 (Phase 2): mixed blocks 40+40/d — Mock 2
Week 4 (Phase 2): mixed blocks + weak-area focus — Mock 3
Week 5 (Phase 3): NBME forms — Mock 4
Week 6 (Phase 3 + taper): see 7-day taper

>>> DAILY TEMPLATE
[hour-by-hour as above, adjusted to daily_hours_available]

>>> MOCK CADENCE
| Mock | Date | Form | Expected score range | Decision rule |
|---|---|---|---|---|
| 1 | end W1 | NBME 30 | baseline + 0–5 | if + 5 maintain plan; if 0 review block strategy |
| 2 | mid W3 | UWSA 1 | baseline + 5–10 | if flat reassess weak areas |
| 3 | mid W4 | NBME free 150 | target − 10 | adjust phase 3 emphasis |
| 4 | D-7 | NBME free 150 | target − 5 to + 5 | proceed to taper |

>>> SCORE TRAJECTORY
Baseline [N] → expected at end W2 [N] → W4 [N] → D-7 [N] → exam target [N]

>>> ABORT TRIGGERS
A. Mock drops → diagnose before adding hours
B. Daily Qbank % declines 3 d → half-day off
C. Sleep < 6 h × 3 nights → mandatory rest day
D. UWorld block time > 110 min sustained → cut block
E. Anki lapse rate > 20% / wk → suspend new

>>> 7-DAY TAPER
D-7: full mock
D-6: review misses
D-5: light review
D-4: half mock + review
D-3: logistics
D-2: rest, sleep early
D-1: no study after noon; logistics; sleep
Test day: minimal

>>> NEGATIVE EXAMPLES (what NOT to do)
- Heroic week 1
- All-qbank, no review
- "Catch up on Sunday"
- No mock until week 4
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `weeks_available` | Compresses or expands phases; < 2 wk for Step is refused |
| `daily_hours_available` | Drives block count; > 12 flagged unsustainable |
| `target_score` | Score trajectory + mock thresholds |
| `weak_areas` | Phase 2 weights toward weak areas |
| `qbank` | Adjusts block size and tutor/timed pattern |
| `commitments` | Reduces available days; output names the days lost |
| `include_call_compression` | If learner has a call week, output integrates a lighter call-week template |
| `force_minimum_sleep` | Default 7 h; cannot be overridden below 6.5 h |

## Verification Checklist

- [ ] Sanity check fires before any schedule is built; fails are named explicitly.
- [ ] Total study-hours budget shown with the math (weeks × days × hours × buffer).
- [ ] Week-by-week phases each have a stated goal (foundation / integration / consolidation).
- [ ] Daily template names a hard sleep window; not a suggestion.
- [ ] Mock-exam dates are specific (week and form), not "around week 3."
- [ ] Score trajectory has a baseline + intermediate + target, not just target.
- [ ] All 5 abort triggers stated with numeric thresholds.
- [ ] 7-day taper has day-by-day actions, not "wind down."
- [ ] Negative-examples block shows ≥ 4 concrete patterns to avoid.
- [ ] If `weeks_available × daily_hours_available` is mathematically insufficient for `target_score − baseline`, the prompt says so and recommends scope adjustment.
- [ ] Health constraints (sleep / exercise) are preserved even when learner asks for more hours.

## Worked Example (compact)

**Input:** `exam = USMLE Step 1`, `weeks_available = 6`, `target_score = 240`, `current_baseline = 218 (NBME 28)`, `daily_hours_available = 10`, `qbank = UWorld`, `weak_areas = [biochem, pharm-cardio, pathology-renal]`, `commitments = wedding day 22`, `sleep_target = 7h`.

**Output:**

```
DEDICATED SCHEDULE — USMLE Step 1
Weeks: 6   Daily: 10 h   Target: 240   Baseline: 218   Qbank: UWorld
Weak: biochem, pharm-cardio, path-renal   Commit: wedding D22   Sleep: 7 h

>>> SANITY CHECK
OK. 6 weeks × 6 days × 10 h × 0.85 = 306 h. Realistic delta target 218 → 240 (+22) in 6 weeks is on the upper end but feasible at this hour count.
Wedding D22 → that day = 0 study, surrounding 2 days at 50%. Adjusted: ~290 h effective.

>>> BUDGET (290 effective h)
Qbank: 116 h (≈ 2,640 UWorld Qs at 90 sec each + reviewing 2,640 ≈ 5 min/Q means review dominates)
Review of misses: 73 h
Weak-area targeted: 58 h
Mock exams: 29 h
Buffer: 14 h

>>> WEEK-BY-WEEK
W1 (Phase 1, foundation): biochem subject pass + 40 UW Qs/day tutor. End W1: NBME 28 baseline (already done).
W2 (Phase 1→2): pharm-cardio + path-renal pass. 40 Qs/day, switching to timed mid-week. Mock: NBME 29 end W2.
W3 (Phase 2): mixed UWorld 40 timed + 40 tutor daily. Targeted micro / immuno review afternoons. Mid-W3 mock: UWSA 1.
W4 (Phase 2): mixed 80 Qs/d (2 timed blocks). Weak-area sweeps Sun. WEDDING D22 — 0 study; D21/D23 at 50%. End-W4 mock: NBME free 150.
W5 (Phase 3): random mixed-timed blocks. 2 NBME forms across the week.
W6 (Phase 3 + taper): NBME free 150 D-7. Taper begins. Exam end W6.

>>> DAILY TEMPLATE (10 h study)
07:30 wake + 30 min cardio (3×/wk)
08:30 Block 1 — UW 40 Q timed (70 min)
10:00 Review of misses (90 min)
11:30 break (30)
12:00 Block 2 — UW or targeted (90 min)
13:30 lunch + 20-min nap (60)
14:30 Block 3 — Anki + weak-area concept (120 min)
16:30 break (30)
17:00 Block 4 — light review (60–90)
18:30 hard stop. Dinner, decompress, sleep by 23:30 for 7 h.

>>> MOCK CADENCE
| Mock | When | Form | Expect | Rule |
|---|---|---|---|---|
| 1 | (already done) | NBME 28 | 218 | baseline |
| 2 | end W2 | NBME 29 | 222–227 | if < 222 reassess Phase 1 coverage |
| 3 | mid W3 | UWSA 1 | 225–235 | if < 225 cut new-content; double review |
| 4 | end W4 | NBME free 150 | 230–238 | adjust phase 3 emphasis |
| 5 | D-7 | NBME free 150 | 235–243 | proceed to taper if ≥ 235 |

>>> SCORE TRAJECTORY
218 → 224 (end W2) → 230 (end W3) → 235 (end W4) → 240 (D-7) → 240 (exam).

>>> ABORTS
A–E as above; if Mock 3 < 225 → cut new-content week, shift to all-review + NBME-form drill.

>>> TAPER (D-7 to test day)
D-7 NBME / D-6 review misses / D-5 light / D-4 half NBME / D-3 logistics / D-2 rest / D-1 no study after noon / test day minimal.

>>> NEGATIVE EXAMPLES
- 14-h days week 1
- All Qbank, no review
- Wedding-week catch-up plan
- No mock until W4
```
