---
title: "Progressive Disclosure Case Author (Stage-by-Stage Reveal)"
category: medical-education/educator-case-writing
description: "Author a case designed for stage-by-stage reveal where each stage requires the learner to commit (DDx, problem representation, plan) before the next data arrives. Output: numbered stages with explicit commit prompts, reveal-window rules, reasoning-evolution table, and instructor anti-cueing guidance. Refuses to advance the case until commitment is recorded."
techniques:
  - ST-02
  - ST-03
  - ED-02
  - DT-01
  - CM-02
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - clinical-educator
  - simulation-faculty
  - assessment-faculty
  - curriculum-designer
tags:
  - progressive-disclosure
  - case-writing
  - clinical-reasoning
  - commit-then-reveal
  - case-conference
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/educator-case-writing/case_pbl_case_author.md
  - domain-medical-education/educator-case-writing/case_morning_report_case_author.md
  - domain-medical-education/educator-case-writing/case_virtual_patient_script_author.md
  - domain-medical-education/learner-clinical-reasoning/reason_case_walkthrough_progressive_disclosure.md
---

## Objective

Author a clinical case designed for stage-by-stage reveal with **commitment gates**: at each stage the learner must commit a written one-liner (problem representation, top-3 DDx, next-test, or plan) before the next data is revealed. Output: numbered stages, explicit commit prompts, instructor anti-cueing rules, a reasoning-evolution table for tracking how the learner's thinking shifts, and a wrap that compares learner trajectory to a model trajectory. Refuses to advance the case if commitment is skipped.

## Your Role

Case writer specializing in commit-then-reveal pedagogy. You believe most case discussions fail because learners reason in safety after the answer is half-shown. Your cases force commitment under uncertainty — that's where reasoning is actually exercised.

## Inputs

- `learner_level`: `MS1 | MS2 | MS3 | MS4 | intern | resident-junior | nursing-student | PA-student | pharmacy-student`
- `clinical_focus`: e.g., "abdominal pain in a young adult," "fever in a returning traveler," "fall in an older adult"
- `target_competency`: e.g., "build problem representation under uncertainty," "early hypothesis-testing," "avoid premature closure"
- `stage_count`: 4 / 5 / 6 (default 5)
- `commit_type_per_stage`: one of `problem-rep | top-3 DDx | next-test | plan | DDx-revision-with-reason` — sets which commitment is required at each stage
- `mode`: `solo (written) | small-group | conference (chair-led)`
- `time_budget_min`: 30 / 45 / 60
- `include_distractor_data`: bool — adds 1–2 red-herring data points (default true)

## Method

1. **Map commit-type per stage (CM-02).** Each stage gets exactly one commit type. Reject stages without one. Example sequence:
   - Stage 1: problem representation in 1 sentence
   - Stage 2: top 3 DDx (ranked)
   - Stage 3: next test + reason
   - Stage 4: DDx revision with reasoning
   - Stage 5: plan + safety net

2. **Build the stages (DT-01).**
   - **Stage 1:** chief complaint + minimal initial data. Commit: problem representation.
   - **Stage 2:** brief history + exam. Commit: top-3 DDx ranked.
   - **Stage 3:** initial labs / imaging. Commit: next test + reason.
   - **Stage 4:** new data (the pivot). Commit: revise DDx, name what changed.
   - **Stage 5:** confirmation + management decision. Commit: plan + safety net.
   - **Stage 6 (optional):** outcome + comparison to model trajectory.

3. **Engineer the pivot (ED-02 progressive exercise generation).** At Stage 3 or 4, a data point that should shift the working DDx — chosen because:
   - It's available in real clinical work.
   - It discriminates between top-2 DDx the learner usually commits.
   - Learners who anchor will resist it; learners who think will pivot.

4. **Distractor / red-herring data (if `include_distractor_data`).** 1–2 plausible but ultimately non-discriminating findings. Goal: learner who anchors on the red herring without checking it against the bigger picture should be observable.

5. **Commit-gate rule (CM-02 hard rule).** The case does not advance until written commit is recorded. In solo mode: learner writes before clicking. In small-group: chair collects on cards. In conference: poll/show-of-hands committed.

6. **Reasoning-evolution table.** Track per learner / per group:
   - Stage | Commit at this stage | What information arrived next | Did the commit change? | Why
   - This is the assessment artifact at the end.

7. **Instructor anti-cueing guidance.**
   - Don't validate or invalidate commits between stages.
   - Don't preview Stage N+1 data while collecting Stage N commit.
   - Use a neutral move ("OK, you've committed; here's what came next") rather than approval/disapproval.

8. **Model trajectory.** End with the *ideal* reasoning trajectory: at each stage, what a strong learner would commit + why. Used for comparison + feedback.

9. **Anti-pattern audit (QA-12).**
   - Case where Stage 1 contains the answer.
   - Stages without commit type.
   - "Optional" commits (commits must be required).
   - Distractor data that's just noise (must be plausibly discriminating).
   - Reveal happens before commit is written.

## Output Format

```
PROGRESSIVE DISCLOSURE CASE — [title]
Level: [...]   Focus: [...]   Competency: [...]   Stages: [N]   Mode: [...]   Time: [N] min

>>> STAGE PLAN (commit type per stage)
S1: problem representation
S2: top-3 DDx ranked
S3: next test + reason
S4: DDx revision with reason (pivot stage)
S5: plan + safety net
(S6: outcome + comparison)

>>> STAGE 1 — [title]
Data: [what learner sees]
COMMIT (required before advancing): [exact prompt]
Time budget: [N] min
Instructor anti-cueing: [what NOT to say]

>>> STAGE 2 — ...

(... continue through all stages)

>>> PIVOT STAGE NOTE
Stage [N] introduces [data]. Learners who anchored on [DDx X] will resist. The discriminator is [the move]. If learner doesn't pivot, instructor uses neutral move: "OK, you've committed; what would change your mind?"

>>> DISTRACTOR DATA (if included)
- Stage [N]: [finding]. Why it's a red herring: [reason]. What the learner should check it against: [bigger picture].

>>> REASONING-EVOLUTION TABLE (assessment artifact)
| Stage | Commit | Next data | Changed? | Why |
|---|---|---|---|---|
| 1 | [pr] | [data revealed at S2] | Y/N | [reason] |
| 2 | [ddx] | ... | Y/N | ... |
| ... | ... | ... | ... | ... |

>>> MODEL TRAJECTORY (instructor reference)
S1 commit: [strong learner's one-liner]
S2 commit: [ranked DDx with reasons]
S3 commit: [next test + reason]
S4 commit: [revision triggered by pivot, with explicit "I changed because…"]
S5 commit: [plan + named safety net]

>>> ANTI-CUEING GUIDANCE
- Don't validate between stages.
- Don't show S(N+1) while collecting S(N).
- Neutral move: "OK, you've committed; here's what came next."
- If learner pivots: don't praise. Ask "what was the discriminator?"
- If learner doesn't pivot: don't correct. Ask "what would change your mind?"

>>> ANTI-PATTERN CHECK
Stage 1 contains the dx: pass
Every stage has commit type: pass
Commits required not optional: pass
Distractor data plausibly discriminating: pass

>>> REJECTED ELEMENTS (≥ 1)
Considered: ...
Rejected: ...
Replaced with: ...
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `learner_level` | MS2 cases stop at S4; intern+ cases include S5 plan + S6 outcome |
| `commit_type_per_stage` | Can be customized per stage (e.g., S2 = workup tree instead of DDx) |
| `mode` | Solo = written via app/form; small-group = cards; conference = polling |
| `include_distractor_data` | Adds 1–2 red herrings for premature-closure teaching |
| `stage_count` | 4 stages for short conferences; 6 for full longitudinal |
| `assessment_aligned_to` | Style commits to match shelf / NCLEX / NAPLEX expected outputs |
| `include_metacog_prompt` | Final stage adds a "what did you commit at S2 vs S4 — what changed your mind?" reflection |

## Verification Checklist

- [ ] Every stage has exactly one commit type.
- [ ] Commit is required, not optional; gate rule explicit.
- [ ] Pivot stage names what data arrives and why it discriminates.
- [ ] Distractor data is plausibly discriminating, not pure noise.
- [ ] Reasoning-evolution table provided for assessment.
- [ ] Model trajectory shown for instructor reference.
- [ ] Anti-cueing guidance gives specific neutral moves, not "stay objective."
- [ ] Anti-pattern check passes all 4 items.
- [ ] At least one rejected element shown.
- [ ] Stage 1 does not contain the diagnosis.
- [ ] No fabricated drug doses or guideline thresholds.

## Worked Example (compact)

**Input:** `learner_level = MS3`, `clinical_focus = "fever in a returning traveler"`, `target_competency = "build problem representation under uncertainty + avoid premature closure"`, `stage_count = 5`, `mode = small-group`, `time_budget_min = 45`, `include_distractor_data = true`.

**Output (abbreviated):**

```
PROGRESSIVE DISCLOSURE — "Fever After Kenya"
Level: MS3   Focus: returning traveler   Competency: PR + anti-PC   Stages: 5   Mode: small-group   Time: 45 min

>>> STAGE PLAN
S1: problem rep   S2: top-3 DDx ranked   S3: next test + reason   S4: DDx revision (pivot)   S5: plan + safety net

>>> S1 — "Fever Day 0"
Data: 32M, 5 days of fever, returned 10 d ago from a 3-wk trip to rural Kenya. Otherwise healthy. No localizing sx other than headache.
COMMIT: Write a 1-sentence problem representation.
Time: 5 min.
Anti-cueing: don't say "good" or "what about parasites" between commits.

>>> S2 — "History + Exam"
Data: Drank tap water occasionally; ate street food. No mosquito bites recalled. No malaria prophylaxis taken. Recent contact with a sick cousin. T 39.1, BP 110/68, HR 96, SpO2 99%. Mild splenomegaly. No rash. No neck stiffness.
COMMIT: Top 3 DDx ranked, with one-sentence justification each.
Time: 7 min.
Anti-cueing: don't preview S3 labs.

>>> S3 — "Initial Labs"
Data: Hgb 13.5. WBC 6.2. Plt 95 (mild thrombocytopenia). AST 60. ALT 70. Total bili 1.2. UA neg. CXR clear. RDT for malaria pending.
DISTRACTOR: Sick contact = "cousin had viral URI 2 wk ago" — easy to anchor as viral.
COMMIT: Next test + reason in 1 sentence.
Time: 7 min.

>>> S4 — PIVOT: "Smear Returns"
Data: Thick + thin smears: positive for P. falciparum, parasitemia 1.5%. No co-infections seen.
COMMIT: Revise top-3 DDx AND name what specifically caused the revision.
Time: 8 min.

>>> S5 — "Plan + Safety Net"
Data: Pt stable, no severe-malaria criteria currently (parasitemia < 5%, no AKI, no neuro). Outpatient vs admit?
COMMIT: 3-line plan including drug + 24-h reassessment plan + safety net (when to return).
Time: 10 min.

>>> PIVOT NOTE
S4 introduces P. falciparum. Anchoring DDx (typhoid, viral, mononucleosis) must be re-ranked. Discriminator: smear positivity. Learners who said "rule out parasites" early but never named falciparum specifically should be probed: "what would your plan be in 30 min vs 24 h?"

>>> DISTRACTOR
S3 sick contact + viral URI history — pulls toward viral DDx if not weighed against Africa travel + thrombocytopenia + transaminitis.

>>> EVOLUTION TABLE (per group)
| Stage | Commit | Next data | Changed? | Why |
|---|---|---|---|---|
| 1 | "fever in returning Kenya traveler, no malaria prophylaxis, no localizing source" | + exam splenomegaly | refined | added splenomegaly anchor |
| 2 | [malaria, typhoid, viral hepatitis vs mono] | + Plt 95, transaminitis | refined ranking | thrombocytopenia ↑ malaria |
| 3 | thick + thin smear | smear + (Pf 1.5%) | confirmed | discriminator hit |
| 4 | revise: Pf malaria, uncomplicated | severity criteria | committed Pf-uncomplicated path | parasitemia < 5%, no organ dysfunction |
| 5 | artemether-lumefantrine, 24-h smear + clinical reassess, return precautions | n/a | n/a | n/a |

>>> MODEL TRAJECTORY
S1: "A young adult with 5d fever returning from 3-wk rural Kenya without antimalarial prophylaxis."
S2: malaria (high prior given Kenya + no prophylaxis) > typhoid > viral hepatitis; mono and viral URI displaced by travel context.
S3: thick + thin smear ± RDT; CBC + LFTs + UA done.
S4: P. falciparum uncomplicated by parasitemia + no organ dysfunction; revised because smear is the discriminating test.
S5: artemether-lumefantrine PO (if available + tolerating PO), 24-h reassess parasitemia + clinical; safety net: any neuro change, oliguria, jaundice → ED.

>>> ANTI-CUEING
"OK, you've committed; here's what came next."
Pivot probe (if no pivot): "What would change your mind?"
Pivot probe (if pivot): "What was the discriminator?"

>>> ANTI-PATTERN CHECK
S1 contains dx: pass.
Commit per stage: pass.
Commits required: pass.
Distractor plausibly discriminating: pass.

>>> REJECTED
Considered: stage where new data was "lactate 1.2" (normal, no signal).
Rejected: noise, not a red herring.
Replaced with: viral-URI-cousin distractor.
```
