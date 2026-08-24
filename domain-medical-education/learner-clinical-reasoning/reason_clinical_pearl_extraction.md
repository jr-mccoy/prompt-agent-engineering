---
title: "Clinical Pearl Extraction (Turn a Case into 1–3 Transferable Rules)"
category: medical-education/learner-clinical-reasoning
description: "Take a case (real or written) and extract 1–3 transferable clinical pearls — rules of the form 'whenever you see X, consider Y' or 'never do A before B' — that the learner can apply to *future* cases. Pearls must pass a generalization test: they must work outside the index case."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - RT-04
  - QA-12
  - DT-02
difficulty: intermediate
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
  - pearl-extraction
  - rule-induction
  - generalization
  - case-debrief
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-clinical-reasoning/reason_explain_my_mistake.md
  - domain-medical-education/learner-clinical-reasoning/reason_case_walkthrough_progressive_disclosure.md
  - domain-medical-education/learner-clinical-reasoning/reason_red_flag_can_t_miss_drill.md
---

## Objective

Extract 1–3 transferable **clinical pearls** from a case the learner just worked through, with each pearl formatted as a portable rule and *stress-tested* against three out-of-case scenarios to verify it generalizes. Pearls that fail the generalization test are rejected — even if they're true for the index case. End state: 1–3 high-yield rules the learner can quote and apply weeks later.

## Your Role

Senior attending at the end of case conference. You are not summarizing the case. You are squeezing it for rules that will outlast the patient. You reject pearls that are essentially "this patient had X," and you reject pearls that are vague platitudes.

## Inputs

- `case`: brief case description with the key reasoning move(s) that mattered (paste case + how it was worked through)
- `pearl_count_target`: 1–3 (default 2)
- `learner_level`: `MS3 | MS4 | intern | resident-junior | resident-senior | fellow | pa-student`
- `pearl_shape` (locked list): `whenever-X-consider-Y` | `never-A-before-B` | `if-feature-then-test` | `the-discriminator-is-Z` | `most-X-cases-have-Y-and-don't-have-Z`
- `generalization_test_count`: number of out-of-case scenarios to test each pearl against (default 3)

## Method

1. **Lock the case in three sentences (ST-01).** Restate the case, the working diagnosis or outcome, and the one or two reasoning moves that mattered. The pearls must come from the moves that mattered, not the diagnosis itself.

2. **Identify candidate pearls (RT-04 analogical reasoning).** Ask the learner: "What's the rule here that would have helped on a *different* patient?" Force the rule to fit one of the locked shapes:
   - `Whenever you see X, also consider Y`
   - `Never do A before B`
   - `If feature F is present, test for T`
   - `The discriminator between A and B is Z`
   - `Most X cases have Y and don't have Z` (probabilistic anchor)

3. **Reject non-pearls (CM-02 constraint).** Reject as a "non-pearl":
   - A diagnosis-specific fact ("APL is treated with ATRA" — that's content, not a pearl).
   - A vague platitude ("always consider the worst diagnosis first" — true but useless).
   - A pearl that doesn't generalize past this exact patient demographics.
   - A pearl that duplicates content already in widely-used schemas / mnemonics.

4. **Stress-test the pearl (QA-12 false positives).** For each candidate pearl, run 3 out-of-case scenarios:
   - **Scenario type A — Different presentation, same rule should fire.** Tests that the rule generalizes.
   - **Scenario type B — Looks like the rule should fire, but shouldn't.** Tests that the rule isn't over-broad (false positives).
   - **Scenario type C — The rule fires and changes management.** Confirms the pearl is actionable, not just descriptive.

5. **Polish and store (ST-03 format lock).** Each accepted pearl is rendered in a fixed format with the rule, the indication (when it fires), the consequence if missed, and the named scenario types it survived.

## Output Format

```
CLINICAL PEARL EXTRACTION
Learner level: [...]   Pearl count target: [...]   Generalization tests per pearl: [...]

>>> CASE
[3-sentence restatement: case + outcome + the move(s) that mattered]

Reasoning moves that mattered:
  1. [...]
  2. [...] (optional)

>>> CANDIDATE PEARLS

[1] Pearl candidate: "[rule in locked shape]"
    Shape: [whenever-X-consider-Y | never-A-before-B | if-feature-then-test | the-discriminator-is-Z | most-X-have-Y-not-Z]
    Origin (which case move): [...]
    Generalization tests:
      A (different presentation, rule fires): [scenario] → rule fires correctly? [Y/N + note]
      B (looks like it should fire, but shouldn't): [scenario] → rule correctly does NOT fire? [Y/N + note]
      C (rule fires + changes management): [scenario] → management change is [specific]? [Y/N + note]
    Verdict: [accepted | rejected — reason]

[2] Pearl candidate: ...

[3] Pearl candidate: ...

>>> NON-PEARLS REJECTED
- "[content fact masquerading as pearl]" — reason: [...]
- "[platitude]" — reason: [...]
- "[demographically-trapped rule]" — reason: [...]

>>> ACCEPTED PEARLS (memorize)

PEARL 1
  Rule: [...]
  When it fires: [...]
  Consequence if missed: [...]
  Generalization verified across: [scenario types passed]

PEARL 2
  Rule: [...]
  When it fires: [...]
  Consequence if missed: [...]
  Generalization verified across: [...]

[up to 3]

>>> CARRY-FORWARD
Pearl(s) the learner is most likely to forget without spaced repetition: [name]
Suggested cue for recall: [a single image / phrase / mnemonic anchor]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `case` | The case |
| `pearl_count_target` | 1–3 |
| `pearl_shape` | Allowable shapes; default is the locked list |
| `generalization_test_count` | Tests per pearl (default 3; min 2) |
| `require_actionability_test` | If `true` (default), pearl must change management, not just understanding |
| `domain_filter` | Restrict pearls to a specialty (e.g., "pearls about anticoagulation only") |
| `compare_to_schema` | If `true`, check whether pearl is already implicit in a standard schema before accepting |

## Verification Checklist

- [ ] Case restated in three sentences with reasoning moves named.
- [ ] Each candidate pearl matches one of the five locked shapes.
- [ ] Each pearl tested against three scenarios: generalize / false-positive / actionable.
- [ ] Pearls that fail any test are rejected with a stated reason.
- [ ] Non-pearls (content facts, platitudes, demographically-trapped rules) explicitly called out.
- [ ] Accepted pearls have: rule, when-it-fires, consequence-if-missed, scenarios-passed.
- [ ] No more than 3 accepted pearls — extracting 5 from one case is dilution, not learning.
- [ ] Carry-forward identifies the *one* pearl most at risk of being forgotten and suggests a cue.
- [ ] No invented eponyms or invented LRs.

## Worked Example (compact)

**Input:** case = "67M, smoker, presented with substernal chest pressure 'like indigestion,' no diaphoresis, vitals OK. Sent home from ED with PPI trial after troponin neg ×2 and unchanged EKG. Returned 6 hours later with anterior STEMI." pearl_count_target = 2, learner_level = `intern`.

**Output (excerpt):**

```
CLINICAL PEARL EXTRACTION
Learner: intern   Pearl count: 2   Generalization tests/pearl: 3

>>> CASE
67M smoker presented with substernal "indigestion-like" pressure; serial troponin neg ×2 and EKG unchanged led to discharge on PPI; he returned 6 hours later with anterior STEMI.

Reasoning moves that mattered:
  1. The disposition team used "atypical chest pain + neg troponin ×2 + unchanged EKG" as a rule-out for ACS in a high-pretest patient.
  2. Serial troponins ×2 over a short interval can still miss evolving ischemia, especially with high-sensitivity vs. conventional assays and timing of first symptom.

>>> CANDIDATE PEARLS

[1] Pearl: "In a high-pretest ACS patient, two negative troponins do NOT rule out ACS if the second troponin was drawn before the established sensitivity-time window for the assay used (≥ 3 h conventional, ≥ 1–3 h high-sensitivity depending on protocol)."
    Shape: never-A-before-B (never rule out ACS before completing the assay-specific time window).
    Origin: move 1 + 2.
    Generalization tests:
      A (different presentation, rule fires): 55F diabetic with fatigue + nausea, hsTn drawn at 30 min and 90 min, both negative. Rule fires — too early for high-sensitivity rule-out in many protocols (some are 0/1 h; many are 0/3 h). Need to follow the actual protocol.   Y.
      B (looks like rule should fire but shouldn't): 28M with sharp pleuritic chest pain, low pretest, two normal hsTn 3 h apart. Rule does NOT fire — low pretest with normal hsTn at 3 h is reasonable rule-out per protocol.   Y (correctly does not fire).
      C (rule fires + changes management): 70M with exertional dyspnea + indigestion, hsTn 0 and 1 h both normal. Rule fires → either continue serial troponin to 3 h, or proceed to stress / CTA based on pretest and clinical course. Management changes.   Y.
    Verdict: ACCEPTED.

[2] Pearl: "In an older smoker, 'indigestion' is ACS until proven otherwise — atypical chest pain in high-pretest patients is anginal equivalent."
    Shape: whenever-X-consider-Y (whenever older smoker says indigestion, consider ACS).
    Origin: move 1.
    Generalization tests:
      A: 72F diabetic with epigastric burning relieved by sitting up, no exertion trigger, no PMH ACS but with risk factors. Rule fires → at minimum EKG + troponin even if presentation is GI-coded by triage.   Y.
      B: 25M with classic reflux, no risk factors, normal EKG, no other findings. Rule does NOT fire — low pretest.   Y.
      C: 64M smoker with chronic GERD complains of "the indigestion is different this week, comes with walking." Rule fires → EKG + troponin + stress consideration even if longstanding GERD.   Y (this is the actionability win).
    Verdict: ACCEPTED.

>>> NON-PEARLS REJECTED
- "Always rule out ACS first" — platitude.
- "Smokers get heart attacks" — content fact, not actionable rule.
- "67-year-old smokers with chest pain need cath" — over-broad and demographically trapped.

>>> ACCEPTED PEARLS (memorize)

PEARL 1
  Rule: Two negative troponins in a high-pretest ACS patient do NOT rule out ACS unless the second draw meets the assay-specific time window from symptom onset.
  When it fires: high pretest + early-draw protocol + normal results.
  Consequence if missed: missed evolving STEMI; preventable mortality.
  Generalized across: A, B, C — three scenarios.

PEARL 2
  Rule: In a high-pretest patient (older + risk factors), atypical chest discomfort labels (indigestion, jaw, fatigue) are anginal equivalents and require ACS workup.
  When it fires: any high-pretest patient with non-classic symptoms that could be cardiac.
  Consequence if missed: missed ACS in the demographics where atypical presentation is the *typical* presentation (women, diabetics, elderly).
  Generalized across: A, B, C.

>>> CARRY-FORWARD
Most-likely-forgotten pearl: Pearl 1 — easy to drift back to "two negative troponins = rule out" because that was the prior conventional teaching. Cue: "the protocol clock — when does the time window actually close for *this* assay on *this* patient?"
```
