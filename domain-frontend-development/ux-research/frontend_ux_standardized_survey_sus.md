---
title: "Standardized Usability Questionnaires — Administer and Score SUS, UMUX-Lite, and SEQ Without Breaking Them"
category: frontend-development/ux-research
description: "Administer and score the three standard usability questionnaires — SUS (10 items, per-session), UMUX-Lite (2 items, per-session), and SEQ (1 item, per-task) — with exact item wording kept intact, the scoring formulas applied step by step, confidence intervals reported, and interpretation limited to what the instrument supports; distinct from the survey-instrument designer, which builds new questionnaires from constructs rather than administering validated ones."
techniques:
  - NE-11
  - DS-02
  - CM-02
  - QA-04
  - QA-01
difficulty: beginner
tags:
  - ux-research
  - sus
  - umux-lite
  - seq
  - questionnaire-scoring
  - usability-metrics
  - score-looks-wrong
  - compare-versions
  - ease-of-use
updated: "2026-09-24"
related_prompts:
  - domain-research-academic/research_survey_instrument_designer.md
  - domain-frontend-development/ux-research/frontend_ux_usability_test_plan.md
  - domain-frontend-development/ux-research/frontend_ux_usability_findings_severity_log.md
---

# Standardized Usability Questionnaires (SUS, UMUX-Lite, SEQ)

**Objective:** Choose the right standard questionnaire for the moment, administer
it exactly as validated, score it with the published formula, and report the
result with its uncertainty — so the number means what the literature says it means.

**When to Use:**
- A usability test plan calls for a perceived-usability score.
- A team wants to compare two versions, or track a product over releases.
- Someone has SUS responses and a spreadsheet, and the score "looks wrong".

**Not this prompt if:**
- You need to write *new* questions to measure a construct (satisfaction with
  onboarding, trust, etc.) → `domain-research-academic/research_survey_instrument_designer.md`.
  Rewording SUS items turns SUS into a new, unvalidated instrument.
- You need to decide what the study measures overall → `frontend_ux_usability_test_plan.md`.
- You want to rank observed problems → `frontend_ux_usability_findings_severity_log.md`.

## Inputs

1. Where the questionnaire sits: after each task, or once per session.
2. Response data (raw item responses per participant), if scoring.
3. Sample size and segments.
4. Any comparison: previous release, competitor, or variant.

## Method

1. **Pick the instrument by moment.**
   | Moment | Instrument | Items |
   |---|---|---|
   | After each task | SEQ | 1 item, 7-point: "Overall, how difficult or easy was the task to complete?" (1 = very difficult, 7 = very easy) |
   | End of session, full measure | SUS | 10 items, 5-point agreement, alternating positive/negative wording |
   | End of session, minimal burden | UMUX-Lite | 2 items, 7-point agreement: "[This system's] capabilities meet my requirements." / "[This system] is easy to use." |
2. **Administer without modification (CM-02).** Keep item wording, order,
   polarity, and scale points. Replacing "system" with the product name is the
   accepted substitution; anything more is a new instrument. Collect SUS after
   the last task and before any debrief discussion.
3. **Score SUS (NE-11).**
   - Odd items (1, 3, 5, 7, 9): contribution = response − 1
   - Even items (2, 4, 6, 8, 10): contribution = 5 − response
   - SUS = (sum of 10 contributions) × 2.5 → range 0–100
   - A missing item: treat the response as the scale midpoint (3) only if one
     item is missing; otherwise exclude the participant and say so.
4. **Score UMUX-Lite.** Raw = ((item1 − 1) + (item2 − 1)) ÷ 12 × 100.
   If a SUS-comparable number is needed, report the published regression
   adjustment (0.65 × raw + 22.9) and label it as adjusted.
5. **Score SEQ.** Report the mean per task with n; do not sum across tasks.
6. **Report with uncertainty (DS-02, QA-04).** Mean, SD, n, and a 95%
   confidence interval using the t-distribution (CI = mean ± t × SD/√n).
7. **Interpret within bounds.** SUS is not a percentage. Published benchmarks
   put the average SUS near 68 across many studies; treat benchmark
   comparisons as approximate and cite the source used `[verify]`. A CI that
   straddles the benchmark is "not distinguishable", not "average".
8. **Self-check (QA-01)** against the Verification list.

## Output Format

```
# Perceived usability — [study]
Instruments: [...] — administered [when]; wording unmodified: yes/no

## Scoring worksheet (first 2 participants shown in full)
## Results
| Measure | n | Mean | SD | 95% CI | Benchmark (source) | Reading |
## Per-task SEQ
| Task | n | Mean | 95% CI |
## Interpretation (bounded)
## Data-quality notes (exclusions, missing items)
```

## Verification

- [ ] Item wording and order are unchanged from the published instrument.
- [ ] Even SUS items were reverse-scored (5 − response).
- [ ] SUS scores fall within 0–100 and are multiples of 2.5.
- [ ] Every mean is reported with n and a confidence interval.
- [ ] SEQ is reported per task, not summed.
- [ ] Any adjusted UMUX-Lite number is labelled as adjusted.

## False-Positive Prevention

1. **SUS 70 does not mean "70% usable".** It is a scale score; say
   "SUS 70 (95% CI 63–77)".
2. **Forgetting to reverse even items is the most common scoring error.**
   Scores clustering near 50 regardless of experience are the symptom.
3. **Reworded items void the benchmarks.** An all-positive "SUS" is a
   different instrument; report it as such.
4. **n=5 SUS means are very wide.** Report the CI and do not declare a
   difference between versions whose intervals overlap substantially.
5. **SUS says how usable, not why.** Pair it with the findings log for causes.
6. **Do not average SUS and UMUX-Lite raw scores together.** They are
   different scales unless one is regression-adjusted and labelled.
7. **SEQ after a failed task still counts.** Excluding failures inflates ease.

## Example Output

```
# Perceived usability — Team-plan checkout v4 (unmoderated follow-up, n=12)
Instruments: SEQ after each task; SUS at session end. Wording unmodified;
"system" → "checkout".

## Scoring worksheet
P1 responses 4,2,4,1,5,2,4,2,4,2
  Odd (−1): 3+3+4+3+3 = 16   Even (5−x): 3+4+3+3+3 = 16   SUS = 32 × 2.5 = 80.0
P2 responses 3,3,3,2,4,3,3,3,3,2
  Odd: 2+2+3+2+2 = 11        Even: 2+3+2+2+3 = 12         SUS = 23 × 2.5 = 57.5
(P3–P12 scored identically; worksheet attached.)

## Results
| Measure | n | Mean | SD | 95% CI | Benchmark | Reading |
|---|---|---|---|---|---|---|
| SUS | 12 | 71.3 | 12.4 | 63.4–79.2 | ≈68 (published average) [verify source] | Not distinguishable from average |

CI: t(11) = 2.201; 12.4/√12 = 3.58; 2.201 × 3.58 = 7.9.

## Per-task SEQ
| Task | n | Mean | 95% CI |
|---|---|---|---|
| T1 add seats | 12 | 5.4 | 4.8–6.0 |
| T2 explain charge | 12 | 3.9 | 3.1–4.7 |
| T3 invoice billing | 12 | 4.6 | 3.8–5.4 |

## Interpretation
Overall perceived usability sits around the published average; T2 is the
clear low point and matches finding F2 (proration misread) in the findings log.
The data cannot say whether v4 beats v3 — v3 was not measured.

## Data-quality notes
One participant skipped SUS item 7; midpoint (3) imputed, noted. No exclusions.
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — SUS, UMUX-Lite, and CI formulas stated inline.
- **DS-02 Metric Specification** — which instrument, at which moment, reported how.
- **CM-02 Constraint Specification** — item wording and order may not change.
- **QA-04 Uncertainty Acknowledgment** — confidence intervals and bounded benchmark claims.
- **QA-01 Self-Verification** — scoring checks before reporting.

## Related Prompts

- `domain-research-academic/research_survey_instrument_designer.md` — building new instruments.
- `frontend_ux_usability_test_plan.md` — where the questionnaire is scheduled.
- `frontend_ux_usability_findings_severity_log.md` — the causes behind the scores.
