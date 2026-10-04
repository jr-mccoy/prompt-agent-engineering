---
title: "Retention and Persistence Data Review — Cohort Definitions, Disaggregated Gaps, Where Students Leave, and What the Numbers Can and Cannot Say"
category: education-teaching/program/student-success
description: "Review an institution's or programme's retention and persistence data: fix the cohort and the definitions (retention at this institution vs. persistence anywhere), compute rates and equity gaps by student group with small-cell suppression, locate where in the pathway students leave and in what academic standing, convert percentage gaps into numbers of students, separate signal from year-to-year noise, and end with ranked hypotheses and the evidence needed to test each — the institution-side annual or term review, not course-level learning analytics."
techniques:
  - RT-06
  - NE-11
  - QA-04
  - RT-09
  - QA-12
difficulty: advanced
tags:
  - education
  - student-success
  - retention-rate
  - persistence
  - cohort-analysis
  - equity-gaps
  - institutional-research
  - why-are-students-leaving
  - retention-numbers-dropped
  - who-is-not-coming-back
updated: "2026-10-03"
related_prompts:
  - domain-education-teaching/program/evaluation-analytics/program_learning_analytics_interpreter.md
  - domain-education-teaching/program/student-success/program_at_risk_student_outreach_plan.md
  - domain-data-analytics/analysis-and-sql/analytics_cohort_retention_analysis.md
---

# Retention and Persistence Data Review

**Objective:** Turn a retention report into a defensible reading: the right cohort and
definitions, rates and gaps by group with honest uncertainty, the point in the pathway
where students are lost and in what standing, the gaps expressed as numbers of
students, and a short list of testable explanations — so the next decision rests on
what the data can support.

## When to Use
- ✅ The annual retention figure has arrived and a dean, provost, or student-success
  committee wants to know what it means.
- ✅ Retention dropped (or rose) and people already have competing explanations.
- ✅ A strategic plan or equity goal requires disaggregated retention and persistence.
- ✅ Before choosing interventions, to see where in the first two years students leave.
- ❌ **Not this prompt if** you are interpreting **course-level** learning data — LMS
  engagement, formative results, grade dashboards — use
  `program/evaluation-analytics/program_learning_analytics_interpreter.md`. If you are
  building a prospective risk-flagging model, use
  `program/evaluation-analytics/program_early_warning_system_designer.md`. For customer
  or product retention cohorts, use
  `domain-data-analytics/analysis-and-sql/analytics_cohort_retention_analysis.md`.
  Once you know who to reach this term, use
  `program/student-success/program_at_risk_student_outreach_plan.md`.

## Inputs Required
- **Cohort definition** the institution uses (e.g., first-time, full-time, fall entry;
  or all new entrants including part-time and transfer) and the official retention
  definition — supplied by the user or institutional research, not assumed.
- **Counts**, not only rates: cohort size and number retained, overall and by group
  (Pell, first-generation, race/ethnicity, age, full-/part-time, residency, programme,
  entry pathway).
- **Where available**: term-by-term enrolment (term 1→2, 2→3, 3→4), academic standing
  or GPA band of leavers, holds at departure, and enrolment elsewhere (e.g., from
  National Student Clearinghouse records) for a persistence rate.
- **Three to five prior cohorts** on the same definition.
- **Suppression rule** for small cells (the institution's own; commonly n < 10).
- **Context**: policy, pricing, programme, or enrolment-mix changes over the period.

> **Privacy:** Use aggregate tables only. Do not paste student-level records into an AI
> tool; follow FERPA or local equivalents and your IR office's suppression rules.

## Constraints

**Must:**
- State the cohort and both definitions — retention (same institution) and persistence
  (enrolled anywhere) — before any number.
- Show counts alongside every rate and suppress cells below the stated threshold.
- Express every equity gap in percentage points **and** in number of students.
- Compare against a multi-year range, not only last year, and give a rough margin of
  error for rates on small groups.
- Separate leavers by academic standing where data allows.
- End with hypotheses, each paired with the evidence that would test it.

**Must Not:**
- Change cohort definitions between years without flagging it.
- Treat a one-year change within normal variation as a trend.
- Present a demographic gap as caused by the demographic characteristic.
- State federal reporting rules or accreditor thresholds from memory.

## Instructions

1. **Fix definitions.** Write down the cohort, the census date, the retention and
   persistence definitions, and any change across years.
2. **Compute headline rates (NE-11).** `Retention = retained ÷ cohort`;
   `Persistence = (retained + enrolled elsewhere) ÷ cohort`. For each rate on a group of
   n students, an approximate 95% margin is `±1.96 × √(p(1−p)/n)` — use it to decide
   whether differences are distinguishable.
3. **Check the trend.** Place this year against the prior three to five. A change
   inside the range of past year-to-year swings is reported as "within normal variation".
4. **Disaggregate (RT-06).** Rates by each group, with counts and suppression. Compute
   gaps against the overall rate or a stated reference group; name which.
5. **Convert gaps to students.** `Students behind the gap = group n × (reference rate −
   group rate)`. A 9-point gap in a group of 60 is five students; in a group of 600 it is
   fifty-four.
6. **Locate the loss.** Where term-by-term data exists, find the step with the biggest
   drop. Split leavers by standing: those in good standing are usually leaving for
   non-academic reasons (cost, work, family, belonging, transfer) and need a different
   response from those on probation.
7. **Check for mix effects.** If the cohort's composition changed (more part-time,
   more of a lower-retaining programme), estimate how much of the overall change is mix
   rather than a change within groups.
8. **Rank hypotheses (RT-09).** For each pattern, list plausible explanations and the
   evidence that would confirm or rule each out: hold and balance data, exit or
   non-returner surveys, course-level DFW rates, aid packaging, transfer destinations.
9. **State uncertainty (QA-04).** Say what the data cannot show and which decisions
   should wait for the evidence in step 8.

## Output Format

```
# Retention and persistence review — [cohort], [year]

## Definitions
Cohort: [..]   Retention: [..]   Persistence: [..]   Changes across years: [..]

## Headline
Retention: [x/n = %] (±[..])   Persistence: [x/n = %]   5-year range: [..]
Read: [change / within normal variation]

## By group
| Group | n | Retained | Rate | Gap (pp) vs [ref] | Students behind gap | Distinguishable? |

## Where students leave
| Step | Enrolled | Lost | Share of all leavers |
Leavers by standing: good standing [n] / probation-suspension [n]

## Mix effect
[estimate]

## Hypotheses and tests
| Pattern | Explanation | Evidence that would test it | Owner |

## What this cannot tell us
[..]
```

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Rates without counts | 50% of 4 students is not a finding | Counts beside every rate; suppress small cells |
| Retention read as persistence | Transfers out look like dropouts | Report both when enrolment-elsewhere data exists |
| One-year blip as trend | Year-to-year noise is often ±2–3 pp | Compare with a multi-year range and margins |
| Gap blamed on the group | Demographics proxy for cost, work, preparation, and institutional barriers | Treat gaps as pointers to conditions to investigate |
| All leavers as academic failures | Many leave in good standing | Split by standing; different reasons, different responses |
| Ignoring mix change | A shift in who enrolled can move the average with no change within groups | Estimate the mix effect |
| Percentages only | Leadership cannot size a response | Convert gaps to students |
| Definitions from memory | Reporting definitions vary and change | Use the definitions IR supplies |

## Verification Checklist

- [ ] Cohort, retention, and persistence definitions stated first
- [ ] Counts beside every rate; cells below threshold suppressed
- [ ] Margins shown for group rates; differences labelled distinguishable or not
- [ ] Current year placed in a multi-year range
- [ ] Every gap in pp and in students, with the reference group named
- [ ] Leavers split by step and by academic standing where data exists
- [ ] Mix effect checked
- [ ] Each hypothesis paired with testing evidence; limits stated

## Example Output

```
# Retention and persistence review — Fall 2024 first-time, full-time cohort, Northgate University

## Definitions
Cohort: first-time, full-time degree-seeking, fall census.  Retention: enrolled at
Northgate on fall 2025 census.  Persistence: enrolled anywhere (Clearinghouse match).
Changes: none since 2021.

## Headline
Retention: 868/1,240 = 70.0% (±2.6)   Persistence: 964/1,240 = 77.7%
5-year range: 70.0–74.1%   Read: within normal variation — 2.3 pp below the 2023
cohort, inside the ±2.6 margin — but the lowest in five years; watch, do not declare a trend.

## By group
| Pell | 520 | 338 | 65.0% | −8.6 vs non-Pell | 45 | Yes (±4.1 vs ±3.2) |
| Non-Pell | 720 | 530 | 73.6% | ref | — | — |
| First-gen | 455 | 300 | 65.9% | −6.5 vs continuing-gen | 30 | Yes |
| Continuing-gen | 785 | 568 | 72.4% | ref | — | — |
| American Indian/Alaska Native | 7 | — | suppressed (n<10) | — | — | — |

## Where students leave
| Fall → spring | 1,240 | 161 | 43% |
| Spring → fall | 1,079 | 211 | 57% |
Leavers by standing: good standing (GPA ≥ 2.0) 158 / probation or suspension 214.
96 of 372 leavers enrolled elsewhere (mostly two local community colleges).

## Mix effect
Pell share rose from 36% to 42%. Holding 2023 group rates fixed, the mix change alone
lowers overall retention by about 0.5 pp — most of the 2.3 pp decline is within groups.

## Hypotheses and tests
| More spring→fall loss | Balance holds blocked fall registration | Holds at spring census vs. non-return | Bursar + IR |
| 158 left in good standing | Cost or work hours, not academics | Non-returner survey; aid gap by leaver | Aid office |
| Pell gap widened | 2025 aid packaging change | Unmet need, 2023 vs 2024 cohorts | Aid office |

## What this cannot tell us
Why individual students left; whether the 96 transfers were planned. Decide on spring
hold policy after the holds analysis (due Dec 1), not before.
```

## Techniques Used

- **RT-06 Correlation and Cross-Analysis** — rates cross-cut by group, step, and standing.
- **NE-11 Embedded Calculation Formulas** — rates, margins, gap-to-students, and mix effect.
- **QA-04 Uncertainty Acknowledgment** — margins, "within normal variation", and explicit limits.
- **RT-09 Root Cause Explanation Pattern** — patterns turned into testable explanations.
- **QA-12 False Positives Identification** — guards against noise-as-trend and gap-as-cause.

## Related Prompts

- `domain-education-teaching/program/evaluation-analytics/program_learning_analytics_interpreter.md` — course-level learning data, the layer below this review.
- `domain-education-teaching/program/student-success/program_at_risk_student_outreach_plan.md` — acting this term on the students the review points to.
- `domain-data-analytics/analysis-and-sql/analytics_cohort_retention_analysis.md` — cohort retention method for products and customers.
