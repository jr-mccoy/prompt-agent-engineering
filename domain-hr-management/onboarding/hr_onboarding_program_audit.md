---
title: "Onboarding Program Audit — Early Attrition, Time to Productivity, and the Leading Indicators That Explain Them"
category: hr-management/onboarding
description: "Audit whether an organisation's employee onboarding works across many hires: metric definitions fixed before the data is opened, early attrition computed only on cohorts old enough to count, time to productivity on a role-specific milestone with not-yet-reached hires kept in, leading indicators (day-one readiness, written 90-day bar, 1:1 adherence, 30-day survey) cross-tabbed by team, small-sample intervals instead of bare percentages, a gaming check, and two or three owned changes with a re-measure date. Refuses slices by protected characteristic without counsel."
techniques:
  - DS-02
  - RT-06
  - QA-04
  - QA-21
difficulty: advanced
tags:
  - onboarding-audit
  - early-attrition
  - time-to-productivity
  - new-hire-retention
  - people-analytics
  - onboarding-metrics
  - new-hires-keep-quitting
  - is-our-onboarding-working
  - slow-ramp-up
updated: "2026-10-03"
related_prompts:
  - domain-hr-management/onboarding/hr_onboarding_thirty_sixty_ninety.md
  - domain-hr-management/people-ops/hr_engagement_survey_design.md
  - domain-hr-management/people-ops/hr_exit_interview.md
---

# Onboarding Program Audit

**Objective:** Find out whether onboarding — not hiring, not one manager's style —
is costing the organisation new hires and ramp time, and where, using numbers that
survive small samples, then change two or three things and re-measure.

**When to Use:**
- New hires leave in their first months more than they should, and nobody can say where.
- Ramp time is long and variable and every team blames something different.
- You are about to redesign onboarding and want a baseline before you do.
- **Not this prompt if** you are planning one person's ramp — use
  `domain-hr-management/onboarding/hr_onboarding_thirty_sixty_ninety.md` or, for the
  first week, `hr_preboarding_first_week_plan.md`. For an organisation-wide engagement
  survey, use `domain-hr-management/people-ops/hr_engagement_survey_design.md`; for one
  leaver's conversation, `domain-hr-management/people-ops/hr_exit_interview.md`.
  Onboarding for a training cohort is
  `domain-education-teaching/instructor/higher-ed-corporate/teaching_corporate_onboarding_program.md`;
  customer onboarding is `domain-sales-customer/customer-success/`.

## Inputs / Context

1. **Starters** over 12+ months: start date, team, role family, manager, location or
   work pattern, and leave date and type (voluntary / involuntary) where applicable.
2. **A productivity milestone per role family**, defined by the function (first
   independent ticket resolution at standard quality, first merged production change,
   quota ramp attainment).
3. **Process records**: equipment and access on day one, buddy assigned, written 90-day
   bar given in week one, 1:1s held vs. scheduled.
4. **New-hire surveys** at ~30 and ~90 days, with response counts.
5. **Exit-interview themes** for early leavers.
6. **Anonymity threshold** used by your survey process.

## Method

1. **Fix definitions before opening the data (DS-02).** Write each metric, its
   numerator, denominator, window, and exclusions. Example: *90-day attrition* = leavers
   within 90 days of start ÷ starters whose start was ≥ 90 days ago. Decide voluntary
   vs. involuntary handling, and minimum cell sizes (e.g. no rate on fewer than 10
   starters; no survey cut on fewer than 5 respondents).
2. **Handle censoring.** Recent starters have not had time to leave or ramp; exclude
   them from rates that need the full window, and for time to productivity report "% who
   reached the milestone by week X", keeping those not yet there.
3. **Compute the outcomes.** 90-day and first-year attrition (voluntary and total) and
   time to productivity (median and spread) overall and by team or role family.
4. **Compute the leading indicators.** Day-one readiness, written 90-day bar, buddy
   assigned, 1:1 adherence in weeks 1–6, and survey items such as "I know what good
   looks like at 90 days".
5. **Cross-analyse (RT-06).** Set outcomes beside indicators by team, manager group,
   location, and source. Look for teams where both are bad. This is association across
   small groups; it points to where to look, not to proof.
6. **State uncertainty (QA-04).** For any rate on a small group, give the count and an
   interval (e.g. Wilson 95%), and call a difference real only when the intervals
   barely overlap or the pattern repeats across quarters.
7. **Separate onboarding from hiring and management.** Exit themes like "the job was not
   what was described" point to the hiring stage; one manager's team failing across all
   indicators points to that manager's support. Route accordingly.
8. **Gaming check (QA-21).** How could each metric improve without onboarding
   improving? (Milestone redefined as "finished training"; involuntary exits recorded
   as voluntary; surveys sent while the manager watches.) Add a guard for each.
9. **Two or three changes.** Each with an owner, the indicator it should move, and a
   re-measure date on cohorts that start after the change.
10. **Legal care.** Comparing outcomes by sex, race, age, disability or other protected
    characteristics is an adverse-impact analysis — do it only with counsel engaged, as
    the pay equity audit does. This audit slices by team, role, location, and process.

## Output Format

```
# Onboarding audit — [org]   Cohorts: [start range]   Prepared: [date]

## Definitions (fixed [date], before data)
| Metric | Numerator | Denominator | Window | Exclusions | Min cell |

## Outcomes
| Group | Starters (eligible) | 90-day leavers (vol/invol) | Rate [interval] | Time to productivity (median, IQR, % reached by wk X) |

## Leading indicators
| Group | Day-one ready | 90-day bar written wk 1 | Buddy | 1:1 adherence wk 1–6 | Survey: "know what good looks like" (n) |

## Where outcomes and indicators line up
[group] — [outcome] with [indicator]; confidence [H/M/L]

## Not onboarding
[hiring-stage or manager-specific signals, routed to ...]

## Gaming guards
| Metric | How it could be gamed | Guard |

## Changes
| Change | Owner | Indicator it should move | Target | Re-measure on cohorts starting after [date] |
```

## Verification

- [ ] Definitions were written and dated before the data was opened.
- [ ] Rates use only cohorts old enough for the window; not-yet-ramped hires are kept.
- [ ] Every rate on a small group shows its count and an interval.
- [ ] Cells below the minimum are suppressed, not reported.
- [ ] Hiring-stage and manager-specific signals are separated and routed.
- [ ] Each metric has a gaming guard.
- [ ] Changes have owners, target indicators, and a re-measure date.
- [ ] No slice by protected characteristic was made without counsel.

## False-Positive Prevention

1. **Counting recent starters as retained.** Someone who started three weeks ago has
   not survived 90 days. Censor, or the rate looks better every quarter you add hires.
2. **Percentages from tiny teams.** "Support attrition is 26%" on 19 people has an
   interval from roughly 12% to 49%. Report the counts and the interval.
3. **Invented benchmarks.** "Industry average 90-day attrition" figures are rarely
   comparable. Compare to your own baseline and across your own teams.
4. **Time to productivity as time to training complete.** Completing modules is
   attendance; the milestone must be work done at the standard.
5. **Blaming onboarding for a hiring miss.** If leavers say the role was not as
   described, fix the job description and interviews, not week one.
6. **Correlation as cause.** A team with low readiness and high attrition is where to
   look first, not proof that laptops cause resignations.
7. **Survey exposure.** Small-group survey cuts can identify individuals; respect the
   threshold even when the finding is interesting.

## Example Output

```
# Onboarding audit — Brightline (140 staff)   Cohorts: starts Oct 2025 – Sep 2026   Prepared: 3 Oct 2026

## Definitions (fixed 22 Sep, before data)
90-day attrition: leavers ≤ 90 d ÷ starters with start ≤ 5 Jul 2026 · voluntary and total
Time to productivity (Support): first week with ≥ 25 tickets closed unassisted at QA ≥ 90%
Time to productivity (Engineering): first production change merged
Min cell: 10 starters for rates; 5 respondents for survey cuts

## Outcomes
| All         | 58 (49) | 6 (5/1) | 12.2% [≈6–24%] | — |
| Support     | 22 (19) | 5 (5/0) | 26.3% [≈12–49%] | median 9 wk (IQR 7–12); 14 of 17 eligible reached by wk 16; plan says 6 wk |
| All others  | 36 (30) | 1 (0/1) | 3.3% [≈1–17%]   | Eng: median 8 days to first merged change |

## Leading indicators
| Support    | 9/22 (41%)  | 4/22  | 22/22 | 61% | 31% agree (n=16) |
| All others | 32/36 (89%) | 25/36 | 30/36 | 84% | 64% agree (n=28) |

## Where outcomes and indicators line up
Support — highest early attrition with lowest day-one readiness (headset and telephony
licences requested on start day; 10-day lead time) and no written 90-day bar for 18 of
22 hires. Pattern holds in 3 of 4 quarters. Confidence: Medium (small n, consistent).

## Not onboarding
4 of 5 Support leavers' exit notes cite "rota different from what was described" →
hiring stage: job description and interview to show the actual rota.

## Gaming guards
| Support milestone | redefined as "completed training" | milestone owned by Support QA lead; definition dated |
| 90-day attrition  | involuntary exits coded voluntary | People ops codes leave type from the separation record |
| 30-day survey     | sent during manager 1:1           | sent by People ops, anonymous, threshold 5 |

## Changes
| Request telephony + headset at offer acceptance | IT + People ops | day-one readiness | ≥ 90% | Q1 2027 cohorts |
| Support managers write the 90-day bar in week 1 (30/60/90 prompt) | Head of Support | bar written wk 1 | 100% | Q1 2027 cohorts |
| Show the real rota in Support job description and final interview | Talent lead | "role as described" exit theme | 0 of next 5 leavers | Q1–Q2 2027 |
Re-measure: 90-day attrition and ramp on Jan–Mar 2027 starters, reported July 2027.
```

## Techniques Used

- **DS-02 Metric Specification** — numerators, denominators, windows, and minimum cells fixed before the data.
- **RT-06 Correlation and Cross-Analysis** — outcomes set beside process indicators by team.
- **QA-04 Uncertainty Acknowledgment** — counts and intervals on every small-group rate.
- **QA-21 Metric Gaming Vector Enumeration** — how each metric could improve without onboarding improving.

## Related Prompts

- `domain-hr-management/onboarding/hr_onboarding_thirty_sixty_ninety.md` — the individual ramp plan whose adoption this measures.
- `domain-hr-management/people-ops/hr_engagement_survey_design.md` — survey item and anonymity discipline for the 30/90-day pulses.
- `domain-hr-management/people-ops/hr_exit_interview.md` — the conversations that supply early-leaver themes.
