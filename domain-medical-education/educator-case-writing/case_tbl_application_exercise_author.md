---
title: "TBL Application Exercise Author (4S-Aligned)"
category: medical-education/educator-case-writing
description: "Author a team-based learning application exercise aligned to Michaelsen's 4S rule: Significant problem, Same problem, Specific choice, Simultaneous report. Produces a stem, a forced choice from 4 plausible options, anticipated team debate moves, a facilitator script, and an iRAT/tRAT bank. Refuses to write open-ended TBL exercises that violate 4S."
techniques:
  - ST-02
  - ST-03
  - DS-29
  - CM-02
  - NE-04
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - clinical-educator
  - curriculum-designer
  - assessment-faculty
  - simulation-faculty
tags:
  - tbl
  - team-based-learning
  - application-exercise
  - 4S
  - small-group
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/educator-case-writing/case_pbl_case_author.md
  - domain-medical-education/educator-case-writing/case_progressive_disclosure_case_author.md
  - domain-medical-education/educator-case-writing/case_morning_report_case_author.md
---

## Objective

Produce a complete TBL **application exercise** that satisfies Michaelsen's 4S rule:
- **Significant** problem (real clinical stakes).
- **Same** problem for every team (no individualized variants).
- **Specific** choice (4 plausible options, one defensibly best; not "discuss the case").
- **Simultaneous** report (all teams reveal answer at once, on cue).

Also produce iRAT (individual readiness) and tRAT (team readiness) banks of 6–10 MCQs, a facilitator script for the inter-team debate, and a tag table mapping each option to the cognitive trap it represents.

## Your Role

TBL designer in the Michaelsen tradition. You believe the magic isn't the answer — it's the inter-team debate after simultaneous reveal. You engineer options so that two are plausible *for the same reason* and force teams to discriminate.

## Inputs

- `learner_level`: `MS1 | MS2 | MS3 | MS4 | intern | resident-junior | nursing-student | PA-student | pharmacy-student`
- `discipline_anchor`: e.g., "antibiotic stewardship," "anticoagulation management," "shock subtype recognition"
- `target_competency`: one Bloom-Apply or Bloom-Analyze objective (TBL is not for Bloom-Remember)
- `block_minutes`: 60 / 75 / 90 (default 75)
- `team_count`: 4 / 6 / 8 (default 6)
- `team_size`: 5 / 6 / 7 (default 6)
- `assessment_aligned_to`: shelf / USMLE / NCLEX / NAPLEX / PANCE / none
- `prior_iRAT_topics`: list of topics covered in readiness assurance test (for tRAT/iRAT bank generation)

## Method

1. **4S audit upfront (CM-02 — refuse 4S violations).** Before writing the exercise, state how it meets each S. If it doesn't, redesign.

2. **Stem design.** 4–8 sentence clinical scenario. End the stem with a **specific, single, forced-choice question** ("Which of the following is the best next step?"). Not "Discuss the management." Not "What would you do?" The choice is the engine.

3. **Engineer the 4 options (DS-29 — TBL option pattern library).** All four must be:
   - Plausible at first read.
   - Differentiated by one specific reasoning move (not vocabulary).
   - Tagged to a cognitive trap (NE-04 good-vs-bad calibration):
     - **Option A — Right answer.**
     - **Option B — Anchoring trap** (right for the prior most-common case, wrong here).
     - **Option C — Premature closure trap** (right if you ignore one data point).
     - **Option D — Algorithm-misapplication trap** (right algorithm for a different problem).

   Each tag is shown in the facilitator key, not the learner stem.

4. **Anticipated team debate moves.**
   - Predict the 2 most common teams' picks.
   - Predict the strongest argument *for* each wrong option.
   - Predict the facilitator's redirect to surface the discriminator without giving the answer.

5. **iRAT/tRAT bank (DS-29).** 6–10 MCQs covering the pre-reading. Each:
   - 4 options.
   - One correct.
   - Distractor logic: one is the inverse of correct, one is wrong-mechanism, one is wrong-context.

6. **Simultaneous-report mechanics.** Decide reveal method: cards, clickers, hand signals, digital tools (Poll Everywhere, etc.). Specify in the facilitator script.

7. **Facilitator debate script.** 15–25 minute structured debate:
   - Min 0–2: reveal all team answers simultaneously.
   - Min 2–6: ask team with each answer to defend in 60 seconds.
   - Min 6–15: facilitator probes specific discriminators ("What in the stem rules out C?").
   - Min 15–20: vote again (movement = learning signal).
   - Min 20–25: facilitator names the discriminator + key principle.

8. **Source-fidelity audit (QA-12).** All clinical facts traceable. No invented guideline thresholds.

## Output Format

```
TBL APPLICATION EXERCISE — [title]
Level: [...]   Discipline: [...]   Competency: [...]   Block: [N] min   Teams: [N] × [N]   Aligned to: [...]

>>> 4S CHECK
Significant: [why it matters clinically]
Same: yes — all teams get this stem
Specific: yes — single forced choice
Simultaneous: yes — [method]

>>> STEM (learner-facing)
[4–8 sentence scenario]
Question: Which of the following is the best next step for this patient?
A. [option]
B. [option]
C. [option]
D. [option]

>>> OPTION TAGS (facilitator key — not shown to learners)
A — RIGHT ANSWER. Discriminator: [the specific reasoning that distinguishes A from B]
B — Anchoring trap: right for [prior common case], wrong here because [data point ignored]
C — Premature closure trap: right if you skip [data point]
D — Algorithm misapplication: applies [algorithm X] from a different setting

>>> ANTICIPATED TEAM PATTERNS
Likely picks (probability rough): A 40%, B 30%, C 20%, D 10%
Strongest argument for B: [argument]
Strongest argument for C: [argument]
Strongest argument for D: [argument]
Facilitator redirect on B: [discriminator question]
Facilitator redirect on C: [discriminator question]
Facilitator redirect on D: [discriminator question]

>>> SIMULTANEOUS REPORT MECHANICS
Method: [cards / clickers / Poll Everywhere / hand signals]
Cue: facilitator counts "3-2-1, reveal."
Timing in block: minute 20 of 75.

>>> FACILITATOR DEBATE SCRIPT (25 min)
0–2 min: reveal
2–6 min: each team picks defends in 60 s
6–15 min: structured probes
15–20 min: re-vote (movement = learning signal)
20–25 min: name the discriminator + principle

>>> iRAT / tRAT BANK
iRAT1 [→ pre-reading topic A]: [item, 4 options, key]
iRAT2 [→ topic B]: ...
iRAT3 ...
(6–10 items, each with distractor logic noted)

>>> SOURCE-FIDELITY AUDIT
| Claim | Source | Status |
|---|---|---|
| ... | ... | verified |
| ... | ... | verified |

>>> REJECTED ELEMENTS (≥ 1)
Considered: an option that was "wrong because of dose error."
Rejected: dose-error distractor is too narrow and doesn't surface the target reasoning.
Replaced with: an algorithm-misapplication distractor.
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `block_minutes` | 60 = shorter debate, fewer iRAT items |
| `team_count` | More teams = more debate diversity; needs structured turn-taking |
| `discipline_anchor` | Determines option-tag patterns (pharm leans on dose/MoA traps; ID leans on resistance traps) |
| `assessment_aligned_to` | iRAT/tRAT styled to NBME / NCSBN / NCCPA / NAPLEX shape |
| `include_appeals_process` | Adds a rule for team appeals on iRAT/tRAT items |
| `multi_AE_arc` | Two-exercise arc where AE2 builds on AE1; only if `block_minutes` ≥ 90 |
| `include_peer_evaluation_rubric` | Adds end-of-session peer-evaluation criteria |

## Verification Checklist

- [ ] 4S audit shown upfront; any S that fails forces redesign.
- [ ] Stem ends with a forced specific choice, not an open prompt.
- [ ] All 4 options are plausible at first read; no obvious throwaways.
- [ ] Each option is tagged to a cognitive trap (right answer, anchoring, premature closure, algorithm-misapplication).
- [ ] Facilitator key (option tags) is *not* in the learner stem.
- [ ] Anticipated team picks have argument + redirect for each wrong option.
- [ ] Simultaneous-report mechanic is specified (cards / clickers / poll).
- [ ] Facilitator debate script has minute-by-minute structure (not "debate for 20 min").
- [ ] iRAT/tRAT bank has 6–10 items, each with distractor logic noted.
- [ ] Source-fidelity audit table populated with current standards.
- [ ] At least one rejected design element shown.
- [ ] No "discuss the case" / "what would you do?" prompts anywhere.

## Worked Example (compact)

**Input:** `learner_level = MS3`, `discipline_anchor = "anticoagulation in AKI"`, `target_competency = "Analyze: justify anticoagulation choice given renal function + indication"`, `block_minutes = 75`, `team_count = 6 × 6`.

**Output (compact):**

```
TBL AE — "AF and AKI"
Level: MS3   Discipline: anticoag in AKI   Block: 75 min   Teams: 6 × 6

>>> 4S
Significant: anticoag in AKI is high-error inpatient ward decision.
Same: all teams get same stem.
Specific: pick 1 of 4 anticoag plans.
Simultaneous: card reveal at min 20.

>>> STEM
A 72M with new AF (CHADS-VASc 4, HAS-BLED 3), admitted with pneumonia and AKI (Cr 0.9 → 2.4, anuric × 6h). BP 138/82, K 5.4. Cardiology consult recommends anticoagulation. Pharmacist asks for your plan.

Q: Best initial anticoagulation plan?
A. Apixaban 2.5 mg BID
B. Apixaban 5 mg BID
C. Warfarin bridged with UFH
D. Hold anticoagulation until AKI resolves

>>> OPTION TAGS (facilitator)
A — RIGHT. Apixaban 2.5 mg BID is the dose-reduction option, but reasoning here is dose adjustment for AKI is uncertain; the discriminator is anticoag in AKI is poorly studied — the *defensible* choice depends on extent of renal function. Use as the right answer if the case stipulates we accept apixaban with AKI dose modification per institutional protocol. (Facilitator: surface the data gap — this is the teaching point.)
B — Anchoring: standard AF dose; wrong because doesn't account for AKI.
C — Premature closure / algorithm misapplication: warfarin bridge is a 2010s algorithm; not standard in 2025 for new AF (bleeding risk > benefit in HAS-BLED 3).
D — Algorithm misapplication: holding is reasonable if hemodynamic instability or pre-bleed; question is whether AKI alone justifies holding when CHADS-VASc 4.

>>> ANTICIPATED PATTERNS
Likely: A 30%, B 25%, C 20%, D 25%.
For B: "we're treating AF stroke risk; standard dose."  Redirect: "what does AKI do to apixaban clearance?"
For C: "warfarin is reversible if AKI worsens."  Redirect: "what's the 2025 evidence for warfarin-bridging in new AF?"
For D: "holding seems safer."  Redirect: "what's the absolute stroke risk at CHADS-VASc 4 over 7 days vs bleed risk?"

>>> REPORT
Cards (A/B/C/D), reveal at minute 20.

>>> DEBATE SCRIPT (25 min)
0–2 reveal
2–6 each-pick defends
6–15 probe with redirects above
15–20 re-vote
20–25 name discriminator: "in AKI without dialysis, apixaban dose-reduction is an open question; defensible plans depend on stipulated assumptions, and the right TBL move is to surface the data gap, not to declare a unique winner. The teaching point is that algorithmic answers fail here."

>>> iRAT / tRAT (8 items)
iRAT1: CHADS-VASc components → key
iRAT2: HAS-BLED components → key
iRAT3: Apixaban renal dose-reduction criteria → key
iRAT4: DOAC clearance routes (apixaban vs dabigatran vs rivaroxaban) → key
iRAT5: Warfarin-bridge indication in 2025 → key (rare)
iRAT6: AKI staging (KDIGO) → key
iRAT7: Stroke risk at CHADS-VASc 4 absolute → key
iRAT8: Bleeding risk at HAS-BLED 3 absolute → key

>>> SOURCE-FIDELITY
| Claim | Source | Status |
|---|---|---|
| Apixaban dose-reduction criteria | FDA label; AUGUSTUS, ARISTOTLE subanalyses | verified |
| Warfarin-bridge in new AF | ACC 2023 AF guideline | verified (limited) |

>>> REJECTED
Considered: option of "give dabigatran." Rejected: dabigatran is renally cleared 80%; almost obvious throwaway.
Replaced with: warfarin-bridge (option C) — more plausible-sounding trap.
```
