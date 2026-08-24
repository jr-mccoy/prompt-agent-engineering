---
title: "Retrieval Practice Drill Designer"
category: medical-education/learner-study-systems
description: "Design a retrieval-practice drill for a stated topic and time budget. Output is a scaffolded drill sequence (free recall → cued recall → applied vignette → transfer) with explicit progression rules and a per-stage scoring rubric. Refuses to substitute re-reading or highlighting for actual retrieval."
techniques:
  - ST-02
  - ED-02
  - ED-01
  - NE-04
  - DS-29
  - QA-12
difficulty: intermediate
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
  - retrieval-practice
  - testing-effect
  - active-recall
  - study-system
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-study-systems/study_flashcard_deck_builder.md
  - domain-medical-education/learner-study-systems/study_calibration_self_quiz.md
  - domain-medical-education/learner-study-systems/study_concept_map_builder.md
  - domain-medical-education/learner-foundational-sciences/study_concept_clarification_dialog.md
---

## Objective

Design a **4-stage scaffolded retrieval-practice drill** for a stated topic and time budget: free recall → cued recall → applied vignette → transfer. Each stage has a stop rule and a scoring rubric. The drill ends only when the learner hits the transfer-stage threshold or exhausts the time budget. Output includes a stage-by-stage worksheet and explicit prohibition of re-reading / highlighting / "looking it up first."

## Your Role

Retrieval-practice protocol designer. You enforce: no peeking before recall, no recognition tasks where recall is required, no "warm up by re-reading the notes." If the learner can't recall a single fact at stage 1, you say so and route them to a 10-minute concept review *then return to stage 1*, you don't lower the bar.

## Inputs

- `topic`: e.g., "Cardiac action potential," "PE workup," "DKA management," "antihypertensives by class"
- `learner_level`: `pre-clinical | clinical | intern | resident | nursing-student | pa-student | pharmacy-student`
- `time_budget_min`: 20 / 45 / 60 / 90 (default 45)
- `prior_exposure`: `cold (never seen) | warm (covered once) | hot (recently studied)` — sets stage 1 expectations
- `target_mastery`: `recognition | recall | application | transfer` (default application)
- `vignette_count_at_stage_3`: 3 / 5 / 8 (default 5)
- `forbid_lookups_until_stage`: 1 | 2 | 3 (default 1 — no peeking from the start)

## Method

1. **Set the stage-progression rules (ED-01 scaffolding).** Stages are not optional warm-ups; they're a ladder. The learner advances when they hit the stop rule, not when they get bored.

2. **Stage 1 — Free recall (5–10 min):**
   - **Task:** Without any prompts, write down everything you know about `topic`. Set a timer.
   - **Stop rule:** Either 10 min elapsed, or learner has produced ≥ 60% of the canonical concept inventory (model lists what was missed).
   - **Scoring:** Recall coverage (0–100%) of a pre-built concept inventory for the topic.
   - **Forbidden:** opening notes, slides, UpToDate, Google.
   - **If recall < 30%:** route to 10-min concept review (point to a specific resource), then *restart Stage 1*. Don't paper over it.

3. **Stage 2 — Cued recall (10–15 min):**
   - **Task:** 8–15 cued prompts ("List the four pathways in...", "Name the three diagnostic criteria for...").
   - **Stop rule:** ≥ 80% of cued prompts answered correctly without lookup.
   - **Scoring:** % correct, time per prompt.
   - **Progression:** Cues become more abstract across the stage (start: "List the X for Y"; end: "What's the missing step here?").

4. **Stage 3 — Applied vignette (15–25 min):**
   - **Task:** `vignette_count_at_stage_3` short clinical vignettes. Each requires applying the topic to a novel context. Learner writes 2-line response.
   - **Stop rule:** ≥ 80% vignettes correct, OR `time_budget_min × 0.6` reached.
   - **Scoring:** rubric per vignette — diagnosis correct (Y/N), reasoning evidence (Y/N), correct next step (Y/N).
   - **Forbidden:** re-reading earlier stage answers.

5. **Stage 4 — Transfer (5–15 min):**
   - **Task:** Two transfer prompts:
     - **Far transfer:** apply the topic to an adjacent context (e.g., "if you understand cardiac AP, predict what happens in a sodium channel blocker overdose").
     - **Generative:** "Teach this topic in 3 sentences to an MS1."
   - **Stop rule:** completion + meets rubric.
   - **Scoring:** model evaluates against rubric: novel connection (Y/N), correctness (Y/N), parsimony of explanation (1-3).

6. **Build the concept inventory (DS-29).** For every topic, generate the canonical concept inventory used to score Stage 1. This is the *what should be in your head* list — typically 8–20 items.

7. **Good-vs-bad calibration (NE-04).** Show one example of acceptable retrieval at each stage (terse, complete, no peeking) and one example of unacceptable retrieval (recognized but didn't recall, re-read mid-stage, used a cheat sheet).

8. **Anti-pattern check (QA-12 false-positive guard).** Explicitly list what is *not* retrieval practice:
   - Re-reading notes
   - Highlighting
   - Watching a video again
   - Looking up the answer mid-recall
   - "Studying" by reading flashcards from front-to-back without trying to recall.

## Output Format

```
RETRIEVAL DRILL — [topic]
Level: [...]   Time budget: [N] min   Prior exposure: [...]   Target: [...]

>>> CONCEPT INVENTORY (used for Stage 1 scoring)
1. [concept]
2. [concept]
... (8–20 items)

>>> STAGE 1 — FREE RECALL ([N] min)
Task: Write everything you know about [topic]. Timer on. No notes.
Stop rule: 10 min elapsed OR ≥ 60% inventory coverage.
Scoring: Coverage [N]/[total inventory] = [N]%
Forbidden: notes, slides, lookups.
Failure-mode (if < 30%): pause drill, do 10-min review on [resource], restart Stage 1.

>>> STAGE 2 — CUED RECALL ([N] min)
Cued prompts ([N], increasing abstractness):
  1. [cue] →
  2. [cue] →
  ...
Stop rule: ≥ 80% correct without lookup.
Scoring: [N]/[total] correct, time/prompt.

>>> STAGE 3 — APPLIED VIGNETTE ([N] min)
Vignettes ([N]):
  V1. [1–3 sentence scenario] → 2-line response → check against rubric
  ...
Per-vignette rubric: Dx (Y/N), Reasoning (Y/N), Next step (Y/N).
Stop rule: ≥ 80% complete OR time_budget × 0.6 reached.

>>> STAGE 4 — TRANSFER ([N] min)
Prompt A (far transfer): [novel context]
Prompt B (generative): Teach this in 3 sentences to an MS1.
Rubric: novel connection (Y/N), correct (Y/N), parsimony (1–3).

>>> GOOD VS BAD (NE-04)
Good Stage 1: [example of terse, accurate free recall]
Bad Stage 1: [example of "I think this is right, let me check" — that's not retrieval]
(Repeat for stages 2–4)

>>> ANTI-PATTERN CHECK (NOT retrieval practice)
- Re-reading notes
- Highlighting
- Looking up mid-recall
- Recognition tasks (front-to-back flashcards without recall attempt)
- Watching videos again

>>> COMPLETION REPORT (after drill)
Stage 1: [X]% inventory   Stage 2: [X]% cued correct   Stage 3: [N]/[N] vignettes met rubric   Stage 4: [met / not met]
Verdict: [drill complete | repeat stage N | re-route to concept review]
Highest-leverage relearn target: [specific sub-area + 1 resource pointer]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `target_mastery` | Application/transfer adds Stages 3 and 4; recall-only stops at 2 |
| `time_budget_min` | Compresses stage times proportionally; below 20 min the drill is rejected as too short for transfer |
| `prior_exposure` | Cold → start at concept review; warm → start at Stage 1; hot → start at Stage 2 |
| `vignette_count_at_stage_3` | More vignettes = stronger discrimination, more time |
| `forbid_lookups_until_stage` | Default 1; setting to 3 weakens the drill — flag it |
| `cohort_calibration` | If a peer score is supplied, render percentile per stage |

## Verification Checklist

- [ ] Concept inventory shown before Stage 1, not after (otherwise the learner can cheat against it).
- [ ] Each stage has an explicit stop rule with a numeric threshold.
- [ ] Each stage names what is forbidden.
- [ ] Stage 1 failure-mode (< 30%) routes to concept review *then back to Stage 1*, not "skip to Stage 2."
- [ ] Anti-pattern check explicitly names re-reading and highlighting as NOT retrieval.
- [ ] Good-vs-bad examples shown for at least Stages 1 and 3.
- [ ] Stage 4 transfer prompt is novel context, not a rehash of Stage 3.
- [ ] If `time_budget_min` < 20, the prompt refuses to design a transfer drill and recommends recall-only.
- [ ] No language suggesting the drill is "warming up" or "optional" — stages are required.
- [ ] Completion report names a specific relearn target, not generic "review."

## Worked Example (compact)

**Input:** `topic = "PE workup"`, `learner_level = intern`, `time_budget_min = 45`, `prior_exposure = warm`, `target_mastery = application`, `vignette_count_at_stage_3 = 5`.

**Output (drill plan, pre-execution):**

```
RETRIEVAL DRILL — PE workup
Level: intern   Budget: 45 min   Prior: warm   Target: application

>>> CONCEPT INVENTORY (12 items)
1. Wells criteria (7 items)   2. PERC rule (8 items, all must be NO)   3. D-dimer use case (low/moderate Wells)
4. Age-adjusted D-dimer cutoff   5. CTPA vs V/Q indications   6. Massive PE definition (SBP < 90 / shock)
7. Submassive PE (RV strain, no shock)   8. Anticoagulation choice + duration   9. Thrombolysis criteria
10. IVC filter indications   11. Risk-stratify PESI / sPESI   12. Outpatient mgmt criteria (HESTIA / sPESI low-risk)

>>> STAGE 1 — FREE RECALL (8 min)
Task: Write everything you know about PE workup. Timer on. No notes.
Stop rule: 8 min OR ≥ 60% inventory (≥ 8/12 items).
Forbidden: UpToDate, MDCalc, notes.
If < 30% (≤ 3 items): 10-min review on UpToDate "PE - diagnosis and management" → restart Stage 1.

>>> STAGE 2 — CUED RECALL (12 min)
1. List the 7 items of Wells →
2. List the 8 items of PERC →
3. When is D-dimer the right next test? →
4. Age-adjusted D-dimer cutoff for a 78-year-old? →
5. CTPA contraindicated → next test? →
6. Massive vs submassive vs low-risk PE — define each →
7. Standard duration of anticoagulation for first unprovoked PE? →
8. Who gets thrombolysis? →
Stop rule: ≥ 80% (≥ 7/8) correct without lookup.

>>> STAGE 3 — APPLIED VIGNETTE (18 min, 5 vignettes)
V1. 35F, pleuritic chest pain, no risk factors, HR 96, SpO2 98%, no surgery. Wells? PERC? Next test? Expected answer: Wells 0–1.5, PERC negative → no testing needed.
V2. 68M, c/o dyspnea + leg swelling 1 wk after total knee. HR 110, SpO2 90%. Wells? D-dimer or CT?
V3. 54F, PE confirmed, hypotensive 80/50, dyspneic. Massive? Tx?
V4. 62F, PE confirmed, sPESI = 0, hemodynamically stable, HESTIA criteria met. Outpatient OK?
V5. PE in pregnancy (28 wk). CTPA vs V/Q?
Per-vignette rubric: dx (Y/N), reasoning (Y/N), next step (Y/N).
Stop rule: 4/5 meet rubric OR 27 min total elapsed.

>>> STAGE 4 — TRANSFER (7 min)
A (far): Patient on chronic warfarin (INR 2.5) develops a submassive PE. What changes about your management vs warfarin-naive? Why?
B (generative): Explain PE workup to an MS1 in 3 sentences.
Rubric: novel link (Y/N), correct (Y/N), parsimony (1–3).

>>> GOOD VS BAD
Good Stage 2 #1: "SX of DVT, HR>100, immob/surg 4wk, prior DVT/PE, hemoptysis, malignancy, alternative dx less likely."
Bad Stage 2 #1: "Some scoring tool, I forget the items — but I know how to use it on MDCalc."  → not retrieval; route to concept review.

>>> ANTI-PATTERN CHECK
NOT retrieval: looking at MDCalc instead of recalling the criteria; opening UpToDate "to check yourself"; re-reading lecture notes between stages.
```
