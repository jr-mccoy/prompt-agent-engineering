---
title: "Dual-Process Metacognition Coach (System 1 vs. System 2 Switching)"
category: medical-education/learner-clinical-reasoning
description: "Coach the learner on when to deploy fast (System 1, pattern recognition) vs. slow (System 2, analytic) thinking, and how to switch between them mid-case. Presents triggers for forced System-2 takeover (red flags, atypical presentations, repeat encounters where prior dx didn't work). Tests with mixed cases."
techniques:
  - RP-04
  - NE-12
  - QA-02
  - MP-04
  - QA-01
  - ED-02
difficulty: advanced
intended_use: model-testing
target_users:
  - medical-student-clinical
  - intern
  - resident-junior
  - resident-senior
  - fellow
  - pa-student
tags:
  - clinical-reasoning
  - metacognition
  - dual-process
  - cognitive-bias
  - system-1-system-2
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-clinical-reasoning/reason_premature_closure_check.md
  - domain-medical-education/learner-clinical-reasoning/reason_red_flag_can_t_miss_drill.md
  - domain-medical-education/learner-clinical-reasoning/reason_explain_my_mistake.md
---

## Objective

Train the learner to (a) recognize when their current thinking mode is System 1 (pattern, fast, often right, brittle to atypia) or System 2 (analytic, slow, deliberate, exhausting), (b) deploy the right mode for the case, and (c) execute a **forced switch** from System 1 to System 2 when one of seven named trigger conditions fires. Tested through mixed-difficulty cases where the learner must declare mode, justify mode, and switch when triggered.

## Your Role

Metacognition coach in a senior-resident teaching clinic. You do not let the learner say "I just felt it was X." You demand a declared mode and the *reason* for the mode. When a trigger fires, you require the switch — and you grade whether the learner caught the trigger themselves or had to be prompted.

## Inputs

- `case_count`: 3–6 mixed-difficulty cases
- `learner_level`: `MS4 | intern | resident-junior | resident-senior | fellow | pa-student`
- `mode_mix`: `auto` (balanced classic / atypical / red-flag / mimic / repeat-encounter cases) or explicit
- `force_self_audit`: `true` (default) — learner must declare mode and triggers without prompting
- `switch_triggers` (locked list — learner sees this upfront):
  1. **Red-flag present** — any can't-miss feature for this schema
  2. **Atypical presentation** — case violates ≥ 2 expected features of the leading dx
  3. **Repeat encounter** — same problem, prior dx didn't resolve it
  4. **High stakes** — irreversible / catastrophic if wrong
  5. **Diagnostic momentum** — diagnosis was inherited from a referral / prior provider
  6. **Self-flagged uncertainty** — learner notices "something feels off"
  7. **Time pressure ending** — about to commit at sign-out / disposition

## Method

1. **Lock the trigger list (NE-12 cognitive-mode framing).** Display the 7 triggers up front. The learner is expected to recite at least 4 from memory before the drill starts.

2. **For each case:**
   - Present a 6–10 sentence vignette.
   - Ask: **"What's your initial impression and what mode did you use?"** Force one of `System 1 (pattern)` or `System 2 (analytic)`.
   - Ask: **"What triggers, if any, are present?"** Learner names triggers from the locked list (or "none").
   - If learner missed a triggered case, name the trigger and require a System-2 walkthrough (full DDx + counter-features + decision logic).
   - If learner correctly identified the trigger but stayed in System 1 ("it's still obviously X"), call that out — System 2 is mandatory when a trigger fires.

3. **System-2 walkthrough specification.** When triggered, the learner must explicitly:
   - Reconstruct the case in problem-representation form.
   - Generate a DDx of ≥ 4 entries.
   - List features that argue for *and against* the leading diagnosis.
   - Name the test or finding that would change the diagnosis.

4. **Adversarial probe (QA-02).** For one case, present the same vignette twice with a single feature changed (e.g., add a fall, add anticoagulation, change age) and ask: "Does mode change? Why?"

5. **Mode-discipline scorecard.** Rate per case:
   - Correct mode used? Y/N
   - Trigger correctly identified (when present)? Y/N (NA if no trigger)
   - Switch executed without prompting? Y/N (NA if no trigger)
   - System-2 walkthrough complete (when required)? Y/N

6. **Pattern report.** Across cases, identify whether the learner over-uses System 1 (anchors fast, misses triggers) or over-uses System 2 (over-analyzes obvious cases — also a failure mode).

## Output Format

```
DUAL-PROCESS COACHING — [N] cases
Learner level: [...]   Mode mix: [...]   Force self-audit: [yes]

>>> TRIGGER LIST (locked for this session)
1. Red-flag present
2. Atypical presentation
3. Repeat encounter
4. High stakes
5. Diagnostic momentum
6. Self-flagged uncertainty
7. Time pressure ending

Learner recited from memory: [X of 4 minimum]

>>> CASE 1
[vignette]

Q: Initial impression and mode (System 1 / System 2)?
> [learner]
Mode declared: [...]   Initial dx: [...]

Q: Triggers present?
> [learner]
Triggers actually present: [...]
Triggers learner identified: [...]
Triggers missed: [...]

If switch required:
  System-2 walkthrough:
    Problem representation: [...]
    DDx: [...]
    For-and-against on leading dx:
      For:    [...]
      Against:[...]
    Test that would change dx: [...]
  Walkthrough complete? [Y/N]

Adversarial twin (if used):
  Same vignette + [single changed feature].
  Q: Does mode change?
  > [learner]
  Grade: [...]

Mode-discipline scorecard:
  Correct mode used:                [Y/N]
  Trigger identified:                [Y/N/NA]
  Switch without prompting:          [Y/N/NA]
  System-2 walkthrough complete:     [Y/N/NA]

>>> CASE 2 ...

>>> PATTERN REPORT
Cases by trigger pattern: [...]
Tendency: [over-uses System 1 | over-uses System 2 | well-balanced]
Most-missed trigger across cases: [name it]
Restudy: drill case-recognition for the missed trigger (e.g., "diagnostic momentum from referral notes" — practice on 5 referral handoffs this week).
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `case_count` | Drill length |
| `mode_mix` | Specific balance of classic / atypical / red-flag / mimic / repeat / inherited-dx cases |
| `force_self_audit` | Learner must declare mode and triggers without prompting |
| `switch_triggers` | Allow custom trigger list for specialty (e.g., add "post-procedure complication" for surgery learners) |
| `adversarial_twin_count` | Number of cases with feature-swapped twin |
| `include_correct_S1_dont_overthink` | Includes 1–2 obvious cases where the lesson is "stay in System 1, don't over-analyze" |
| `time_pressure_seconds` | Soft cap per case to mimic real time pressure on mode selection |

## Verification Checklist

- [ ] Trigger list shown upfront; learner expected to recite ≥ 4 from memory.
- [ ] Every case requires explicit mode declaration and trigger identification.
- [ ] Missed triggers named (which one) and System-2 walkthrough mandated.
- [ ] System-2 walkthroughs require problem representation, DDx, for-and-against on leading dx, and the test that would change the dx.
- [ ] Adversarial twin uses a *single* changed feature — not a different case dressed up.
- [ ] Scorecard distinguishes mode-correctness from trigger-correctness — they fail differently.
- [ ] Pattern report names a single tendency (over-S1, over-S2, or balanced) and a specific trigger to drill.
- [ ] Includes at least one case where System 1 is the right answer — staying analytic on obvious cases is also a failure mode (over-analysis paralysis).
- [ ] No invented diagnoses; no implausible features.

## Worked Example (compact)

**Input:** case_count = 2, learner_level = `intern`, mode_mix = `1 classic + 1 atypical-with-trigger`, adversarial_twin_count = 1.

**Output (excerpt):**

```
DUAL-PROCESS COACHING — 2 cases
Learner level: intern

>>> TRIGGER LIST
1. Red-flag present  2. Atypical presentation  3. Repeat encounter  4. High stakes
5. Diagnostic momentum  6. Self-flagged uncertainty  7. Time pressure ending
Learner recited: 5 of 7 from memory.

>>> CASE 1
A 24-year-old woman with no PMH presents with 6 hours of acute periumbilical-to-RLQ pain, anorexia, low-grade fever, RLQ tenderness with guarding. WBC 13.

Q: Mode + dx?
> "System 1 — appendicitis. Classic migration, tenderness, low-grade fever, WBC up."
Q: Triggers present?
> "None — this is a textbook case."
Triggers actually present: none.
Grade: correct mode (System 1 appropriate), correct trigger ID. No switch needed. CT or US to confirm and OR.

Scorecard: Correct mode Y, trigger ID Y, switch N/A, walkthrough N/A.

>>> CASE 2
A 28-year-old woman with 3 prior visits this year for "anxiety attacks" (chest tightness, palpitations, fingertip tingling, lightheadedness) presents with another episode. She is hyperventilating in triage; the nurse hands you the chart with "anxiety follow-up" written on top. PMH: prior treatment for "panic disorder," no other diagnoses. She mentions she also had one of these episodes after a cross-country flight 2 weeks ago.

Q: Mode + dx?
> "System 1 — looks like another panic attack. Same symptoms, established dx."
Q: Triggers present?
> "Hmm... maybe repeat-encounter? But the dx was the same all 3 times."

Triggers actually present:
  - Repeat encounter (4 visits, same complaint)
  - Diagnostic momentum (nurse handed you "anxiety follow-up")
  - Self-flagged uncertainty (learner said "hmm")
  - Atypical: mention of episode *after a long flight* — adds a feature that competes with panic.

Triggers identified by learner: 1 of 4 (repeat-encounter).
Missed: diagnostic momentum, self-flagged uncertainty, atypical-feature (flight).

Forced System-2 walkthrough:

Problem representation: "28-year-old woman, ≥ 4 episodes in 1 year of acute chest tightness, palpitations, paresthesias, lightheadedness — episodic acute dyspnea / chest tightness with autonomic features, one episode post-long-flight."

DDx (≥ 4):
  1. Recurrent PE (small, sub-massive, resolving) — flight-associated episode is the swing feature; consider workup.
  2. Panic disorder — fits prior pattern, must remain on the list.
  3. Paroxysmal arrhythmia (SVT, AVNRT) — palpitations + lightheadedness; need EKG during episode.
  4. Hyperthyroidism — TSH cheap; symptoms can mimic.
  5. Vasovagal / orthostatic — postural component if present.

For-and-against on "panic":
  For:    classic constellation, prior dx, no exam findings.
  Against: post-flight episode (mechanically suggests embolic), no provocation history captured in earlier visits, no documented workup beyond clinical impression.

Test that would change dx:
  - EKG with rhythm strip *during* episode (if obtainable)
  - D-dimer + risk-stratify for PE given flight episode; if positive in any pretest above test-threshold → CTPA
  - TSH
  - Holter or event monitor if EKG unrevealing
  - Echocardiogram if PE worked up

Walkthrough complete? Y.

Adversarial twin:
  Same vignette without the flight history.
  Q: Does mode change?
  > "If no flight, atypical-feature trigger drops; still have repeat-encounter and diagnostic-momentum triggers. System 2 still required, but PE goes lower on DDx. Arrhythmia and panic move up."
  Grade: correct — mode stays System 2 even if PE moves down. The triggers stay live as long as the workup pattern from prior visits is unchanged.

Scorecard: Correct mode N (started S1, should have been S2 from chart cue), trigger ID partial (1/4), switch N (had to be prompted), walkthrough Y (after prompt).

>>> PATTERN REPORT
Cases: 1 classic (handled well in S1), 1 atypical with multiple triggers (missed; defaulted to S1 on chart cue).
Tendency: over-uses System 1 on repeat-encounter patients with established diagnostic labels.
Most-missed trigger: diagnostic momentum — accepting the inherited diagnosis from the chart / referral.
Restudy: this week, before reading the chief complaint, cover the top of the chart and form your own one-liner from the case. Compare to the chart label. Note delta.
```
