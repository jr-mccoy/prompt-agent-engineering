---
title: "First-Year Advising Touchpoint Model — Proactive Advising Calendar, Caseload Capacity, and the Risk Moments of the First Year"
category: education-teaching/program/student-success
description: "Design the universal, proactive advising layer for first-year students: map the touchpoints to the first year's known risk moments (first two weeks, first graded work, midterm, next-term registration, aid and holds, end-of-term standing), choose the format of each (individual, group, or automated nudge), test it against real advisor capacity with caseload arithmetic, assign owners, and define the few measures that show whether it is working — the every-student layer that an early-warning system and targeted outreach sit on top of."
techniques:
  - NE-11
  - DS-06
  - AG-12
  - QA-12
difficulty: advanced
tags:
  - education
  - student-success
  - proactive-advising
  - first-year-experience
  - advising-caseload
  - retention
  - higher-ed
  - first-year-students-dropping-out
  - too-many-students-per-advisor
  - plan-advising-for-freshmen
updated: "2026-10-03"
related_prompts:
  - domain-education-teaching/program/evaluation-analytics/program_early_warning_system_designer.md
  - domain-education-teaching/program/student-success/program_at_risk_student_outreach_plan.md
  - domain-education-teaching/instructor/student-support/teaching_course_selection_advising.md
---

# First-Year Advising Touchpoint Model

**Objective:** Produce a first-year advising calendar that puts a contact in front of
every student at the moments first-year students are most likely to drift away, sized
to what the advising staff can actually deliver, with owners and a small set of
measures — so retention work starts before anyone is flagged.

## When to Use
- ✅ A college or university is redesigning first-year advising, or moving from
  "students come when they need us" to proactive (sometimes called intrusive) advising.
- ✅ Advisors are overloaded and the first-year plan promises more meetings than the
  hours allow.
- ✅ Fall-to-spring or fall-to-fall retention of first-year students has slipped and
  leadership wants a universal intervention, not only a risk flag.
- ✅ A new first-year experience programme needs its advising component specified.
- ❌ **Not this prompt if** you are designing the **risk-flagging system** — indicators,
  thresholds, tiers — use
  `program/evaluation-analytics/program_early_warning_system_designer.md`. If students
  are already flagged and you need the outreach and case plan, use
  `program/student-success/program_at_risk_student_outreach_plan.md`. For one advisor's
  course-selection conversation with one student, use
  `instructor/student-support/teaching_course_selection_advising.md`.

## Inputs Required
- **Cohort size** and mix (full-/part-time, residential/commuter, first-generation,
  Pell-eligible, transfer-in, online).
- **Advising staff**: number of advisors (FTE), hours per week each can spend in direct
  student contact after other duties, and any faculty or peer advisors.
- **Academic calendar**: term start, add/drop, first graded work, midterm grades,
  withdrawal deadline, next-term registration opening, aid deadlines, term end.
- **Current touchpoints** and their show rates, if known.
- **Systems**: student information system holds, messaging/CRM tool, appointment
  scheduling, early-alert tool.
- **Institutional definitions** of retention and academic standing (the user supplies
  them; this prompt does not state policy from memory).

> **Privacy:** Plan with aggregate numbers. Do not paste identifiable student records
> into an AI tool; follow your institution's FERPA or equivalent data rules.

## Constraints

**Must:**
- Anchor every touchpoint to a dated risk moment in the institution's own calendar.
- Show the capacity arithmetic: students × touchpoints × minutes against available
  advisor hours, per term.
- Assign a format (individual, group, or automated nudge with a human reply path) and
  an owner to every touchpoint.
- Treat next-term registration as a tracked milestone with a date, not a reminder.
- Define 3–5 measures, with at least one leading indicator inside the term.

**Must Not:**
- Promise more individual meetings than capacity allows.
- Use automated messages as the only contact for students who have not responded twice.
- Present touchpoint attendance as proof the model caused retention.
- State accreditor or regulatory requirements from memory.

## Instructions

1. **Lay out the first-year calendar** with the institution's dates for each risk
   moment: pre-term (orientation, schedule check), weeks 1–2 (belonging, schedule
   fit, add/drop), first graded work (weeks 3–5), midterm, withdrawal deadline,
   next-term registration window, aid renewal and holds, end-of-term standing,
   between-term re-enrolment.
2. **Choose the touchpoints.** Usually 5–7 for the year. For each: purpose, what the
   advisor checks, and what triggers a hand-off to targeted outreach.
3. **Pick a format per touchpoint.** Individual where judgement is needed
   (registration plan, standing); group for information and connection (first two
   weeks); automated nudge for logistics, always with a named person to reply to.
4. **Run the capacity check (NE-11).**
   `Hours needed per term = Σ (students × share receiving touchpoint × minutes ÷ 60)`;
   `Hours available = advisors × direct-contact hours per week × weeks in window`.
   If needed exceeds available, convert touchpoints to group format, narrow them to
   the students who need them, or say plainly what staffing would close the gap.
5. **Prioritise when it does not fit (DS-06).** Protect the touchpoints closest to
   attrition decisions — registration and end-of-term standing — over orientation-style
   contacts.
6. **Assign owners and hand-offs.** Advisor, peer mentor, faculty, aid office; what
   each does when a student does not respond, and when the student moves to the
   targeted outreach plan.
7. **Define measures (AG-12).** Contact rate, show rate by format, registered-by-date
   rate for next term, holds cleared by registration, and term-to-term persistence —
   each disaggregated by the cohort groups in the inputs.
8. **Plan the evaluation honestly.** Compare like with like (prior cohorts, or students
   with similar risk who were and were not reached) rather than attenders against
   non-attenders.

## Output Format

```
# First-year advising touchpoint model — [institution/programme], [year]
Cohort: [n, mix]   Advisors: [FTE] × [direct-contact h/week]

## Risk-moment calendar
| Week/date | Risk moment | Touchpoint | Format | Owner | Hand-off trigger |

## Capacity check (per term)
| Touchpoint | Students | Minutes | Hours needed |
Total needed: [..] h   Available: [..] h   Gap: [..] h → [adjustment or staffing ask]

## Non-response rules
[attempts, channels, escalation]

## Measures
| Measure | Leading/lagging | Target | Disaggregated by | Source |

## Evaluation design
[comparison group, caveats]
```

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| A calendar with no capacity check | Advisors silently skip touchpoints by October | Show the arithmetic; cut or convert before launch |
| Touchpoints on generic weeks | Risk moments follow this institution's dates | Use the actual add/drop, midterm, and registration dates |
| Nudges as contact | Unanswered automated messages reach no one | Human follow-up after two non-responses |
| Attendance = impact | Students who attend differ from those who don't | Compare similar students or prior cohorts |
| Registration as a reminder | Unregistered students by a date are the clearest sign of leaving | Track registered-by-date as a milestone |
| Undisaggregated measures | An average hides the group the model misses | Report each measure by cohort group |
| Universal = identical | Part-time and online students need different times and channels | Vary format and timing by subgroup |
| Policy stated from memory | Requirements vary and change | Use the definitions the user supplies |

## Verification Checklist

- [ ] Every touchpoint tied to a dated risk moment from the inputs
- [ ] Capacity arithmetic shown; needed ≤ available, or the gap and remedy stated
- [ ] Each touchpoint has format, owner, and a hand-off trigger
- [ ] Non-response rule includes a human contact
- [ ] Registration-by-date tracked as a milestone
- [ ] 3–5 measures, at least one leading, all disaggregated
- [ ] Evaluation does not compare attenders with non-attenders
- [ ] No identifiable student data; no policy stated from memory

## Example Output

```
# First-year advising touchpoint model — Lakeside State University, 2026–27
Cohort: 1,800 first-time students (22% part-time, 41% first-generation, 38% Pell)
Advisors: 6 FTE × 20 h/week direct contact

## Risk-moment calendar
| Aug 18 (pre-term) | Schedule fit | Schedule check | Automated + reply-to advisor | Advisor | Fewer than 12 credits or a missing gateway course |
| Wk 2 (Sep 2) | Belonging | Cohort meeting, 15 students | Group, 45 min | Advisor + peer mentor | No-show → phone call |
| Wk 5 (Sep 22) | First graded work | Grade check | Faculty early alert → advisor | Faculty, advisor | Any alert → outreach plan |
| Wk 8 (Oct 13) | Midterm | Midterm meeting | Individual, 30 min — only students with any midterm grade below C (est. 35%) | Advisor | 2+ below C → outreach plan |
| Wk 10 (Oct 27) | Spring registration | Registration plan | Individual, 20 min for all | Advisor | Not registered by Nov 14 → outreach plan |
| Wk 12 (Nov 10) | Holds | Hold clearance | Automated + aid office call list | Aid office | Hold still on Nov 21 |
| Jan 6 | Standing | Standing review | Individual, 30 min — probation only | Advisor | All probation students |

## Capacity check (fall)
| Cohort meetings: 120 groups × 45 min | 90 h |
| Midterm: 630 students × 30 min | 315 h |
| Registration: 1,800 × 20 min | 600 h |
| No-show follow-up calls: est. 400 × 10 min | 67 h |
Total needed: 1,072 h   Available: 6 × 20 h × 15 wk = 1,800 h   Gap: none
(An earlier draft with three 30-minute individual meetings for everyone needed
2,700 h — 900 h over capacity; converting week 2 to groups and targeting the midterm
meeting closed the gap.)

## Non-response rules
Text, then email, then phone within 5 working days; a second missed touchpoint goes
to the targeted outreach plan.

## Measures
| Contact rate per touchpoint | leading | ≥90% | FT/PT, first-gen, Pell | CRM |
| Spring registered by Nov 14 | leading | ≥85% (last year 78%) | same | SIS |
| Holds cleared by Nov 21 | leading | ≥90% | same | SIS |
| Fall-to-spring persistence | lagging | ≥88% | same | IR |

## Evaluation design
Compare with the 2024 and 2025 cohorts on the same measures, adjusted for cohort mix;
do not compare students who attended cohort meetings with those who did not.
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — capacity arithmetic for hours needed against hours available.
- **DS-06 Prioritization and Severity Guidance** — protects touchpoints closest to attrition decisions when capacity is short.
- **AG-12 Quantitative Success Metrics** — a short set of leading and lagging measures, disaggregated.
- **QA-12 False Positives Identification** — guards against attendance-as-impact and nudge-as-contact errors.

## Related Prompts

- `domain-education-teaching/program/evaluation-analytics/program_early_warning_system_designer.md` — the risk-flagging layer that sits on top of this universal one.
- `domain-education-teaching/program/student-success/program_at_risk_student_outreach_plan.md` — where hand-offs from this calendar go.
- `domain-education-teaching/instructor/student-support/teaching_course_selection_advising.md` — the individual registration conversation inside the week-10 touchpoint.
