---
title: "At-Risk Student Outreach and Intervention Plan — Triage by Reason, Outreach Sequence, Matched Support, and Closing the Loop"
category: education-teaching/program/student-success
description: "For a student-success team holding a list of flagged students this term — early alerts, midterm grades, non-registration, holds, attendance drops — triage each case by reason (academic, financial, engagement, wellbeing, administrative), run a multi-channel outreach sequence with non-deficit messages and named owners, match each reason to a specific service, route any safety concern immediately, track every case from attempted to resolved, and judge the effort against a fair comparison rather than a pre-post count."
techniques:
  - AG-11
  - DS-06
  - RP-02
  - DS-40
  - QA-12
difficulty: intermediate
tags:
  - education
  - student-success
  - at-risk-students
  - intervention-plan
  - case-management
  - early-alert-response
  - higher-ed
  - student-stopped-coming-to-class
  - how-to-reach-struggling-students
  - student-might-drop-out
updated: "2026-10-03"
related_prompts:
  - domain-education-teaching/program/evaluation-analytics/program_early_warning_system_designer.md
  - domain-education-teaching/program/curriculum-design/program_remediation_pathway_designer.md
  - domain-education-teaching/program/student-success/program_first_year_advising_touchpoint_model.md
---

# At-Risk Student Outreach and Intervention Plan

**Objective:** Turn a list of flagged students into a working caseload: each student
triaged by the likely reason they are struggling, contacted through a sequence that
actually reaches them, connected to a matched service, tracked to resolution, and
counted honestly at the end of term.

## When to Use
- ✅ An early-alert or early-warning system has produced a list this term and the team
  must decide who contacts whom, how, and with what offer.
- ✅ Midterm grades, attendance drops, or non-registration have identified students
  and outreach so far has been a single email.
- ✅ Alerts are raised but faculty never hear what happened, and the loop needs closing.
- ✅ A K-12 attendance or credit-recovery team needs the same structure for its
  flagged list (adjust services and owners).
- ❌ **Not this prompt if** you are designing **which indicators and thresholds flag
  students** — use `program/evaluation-analytics/program_early_warning_system_designer.md`.
  If the need is a structured academic remediation sequence (diagnostics, dose, exit
  criteria), use `program/curriculum-design/program_remediation_pathway_designer.md`.
  For the universal advising calendar every first-year receives, use
  `program/student-success/program_first_year_advising_touchpoint_model.md`. For one
  high-school student's graduation gaps, use
  `instructor/student-support/teaching_graduation_tracker.md`.

## Inputs Required
- **The flagged list in aggregate**: how many students, flagged by which source
  (faculty alert, midterm grade, attendance, non-registration, hold, aid status), and
  any overlap.
- **Staff and hours** available for outreach this term (advisors, success coaches,
  peer mentors, faculty).
- **Services available**: tutoring, supplemental instruction, aid counselling,
  emergency grants, food pantry/basic needs, counselling centre, disability services,
  registrar for holds — with any wait times.
- **Channels** the institution can use (text, email, phone, CRM, LMS message).
- **Deadlines** that make outreach time-sensitive (withdrawal date, registration,
  aid deadlines).

> **Privacy:** Work with counts and anonymised examples. Do not paste student names,
> grades, or health information into an AI tool; follow FERPA or local equivalents.

## Constraints

**Must:**
- Triage every case into a primary reason category, with the evidence that suggests it.
- Give every case one named owner and a response time.
- Use at least three channels before a case is marked "unreached".
- Write outreach messages in a non-deficit voice: what was noticed, care, one easy
  next step — never "you have been flagged as at-risk".
- Route any indication of self-harm, threat, or crisis to the counselling or
  behavioural intervention team the same day, outside the normal sequence.
- Track each case through attempted → reached → connected to service → resolved.
- Close the loop with the person who raised the alert.

**Must Not:**
- Send every student the same generic message.
- Refer to a service without checking its capacity or wait time.
- Count "message sent" as an intervention.
- Claim the outreach caused retention from a pre-post comparison alone.

## Instructions

1. **Size the caseload.** Deduplicate students flagged by more than one source;
   count cases per owner against hours available.
2. **Triage by reason (AG-11).** Academic (grades, missing work), financial (holds,
   aid gaps, work hours), engagement (attendance, LMS inactivity, belonging),
   wellbeing (stress, health, family), administrative (registration, paperwork).
   Note the evidence; mark "unknown" when the flag gives no reason — the first contact
   finds out.
3. **Prioritise (DS-06).** Highest first: safety concerns (same day), cases facing a
   deadline within 10 days, multiple flags, and students with no contact yet this term.
4. **Write the outreach sequence (RP-02).** Day 0 text from the named owner; day 2
   email with a booking link; day 4 phone call; day 7 a faculty member or peer the
   student knows. Draft the messages for each reason category.
5. **Match each reason to a service** with a warm hand-off (introduction, booked
   slot, or walk-over), not only a link. Check capacity — a tutoring centre with a
   two-week wait is not a midterm intervention.
6. **Set case status and follow-up (DS-40).** Each contact produces a status and a
   dated next action. Unreached after the sequence → registrar or dean-of-students
   check (enrolment, address, safety).
7. **Close the loop.** Tell the alert-raiser, within a week, that contact happened
   and the general nature of the support (without private details).
8. **Plan the count.** Report reach rate, connection rate, and term outcomes for
   flagged students compared with similar flagged students from a prior term, or with
   a lagged comparison group — and say what the comparison cannot rule out.

## Output Format

```
# Outreach and intervention plan — [term], [unit]
Flagged: [n] (deduplicated)  Owners: [..]  Window: [dates]

## Triage
| Reason category | Cases | Evidence typical of this group | Priority |

## Outreach sequence
| Day | Channel | Sender | Message (per reason) |

## Service matching
| Reason | Service | Hand-off method | Capacity / wait |

## Case tracking
Statuses: attempted → reached → connected → resolved / unreached
Unreached protocol: [..]
Safety route: [team, same-day]

## Loop closure
[who is told what, by when]

## Measures and comparison
| Measure | Target | Comparison |
```

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| One email to everyone | Struggling students are the least likely to read it | Three channels, named sender, day-by-day sequence |
| "You are at risk" language | Labels students and lowers response | Non-deficit message: noticed, care, one easy step |
| Every flag treated as academic | Many first-term problems are financial or administrative | Triage by reason; the first contact confirms it |
| Referral as a link | Students rarely follow a bare link | Warm hand-off with a booked slot |
| Ignoring service capacity | A full service makes the referral empty | Check wait times before matching |
| Safety in the queue | A crisis cannot wait for day 4 | Same-day route outside the sequence |
| "Sent" counted as done | Contact attempted is not support delivered | Track to connected and resolved |
| Pre-post as proof | Flagged students often recover anyway | Compare with similar flagged students |

## Verification Checklist

- [ ] Every case has a reason category with evidence or "unknown"
- [ ] Owner and response time for every case; caseload fits hours
- [ ] Sequence uses ≥3 channels and names the sender
- [ ] Messages drafted per reason, non-deficit
- [ ] Each service checked for capacity; hand-off method stated
- [ ] Same-day safety route defined
- [ ] Case statuses run to resolved; unreached protocol defined
- [ ] Loop closed with alert-raisers; comparison group stated

## Example Output

```
# Outreach and intervention plan — Fall 2026, weeks 6–9, Riverbend Community College
Flagged: 214 (deduplicated from 263 flags)  Owners: 4 success coaches, 6 peer mentors
Window: Oct 5 – Oct 30 (withdrawal deadline Nov 6)

## Triage
| Academic | 92 | 2+ missing assignments or midterm below C | 2 |
| Financial | 41 | Registration hold, aid not disbursed, works 30+ h | 1 (hold blocks spring) |
| Engagement | 48 | No LMS login 10+ days, absent 3+ classes | 1 |
| Wellbeing | 9 | Faculty note mentions stress, illness, family | 1 — 2 cases same-day to CARE team |
| Unknown | 24 | Single alert, no detail | 2 |

## Outreach sequence
| Day 0 | Text | Coach by name | "Hi [first name], it's Jordan from Student Success. Your instructors want
  to make sure the semester's going OK. Can I call you for 10 minutes this week? Reply with a time." |
| Day 2 | Email | Coach | Same message + booking link + the one service matched to the reason |
| Day 4 | Phone | Coach | Script per reason |
| Day 7 | Message from instructor or peer mentor | Faculty/peer | "We miss you in BIO 101 — Jordan can help." |

## Service matching
| Academic | Tutoring centre / SI | Coach books slot during call | 3-day wait — added 2 SI sessions |
| Financial | Aid counsellor; emergency grant | Same-day referral; hold reviewed by registrar | Grant fund $18,000 left |
| Engagement | Peer mentor check-in | Mentor meets at class | 6 mentors × 8 cases |
| Wellbeing | Counselling centre | Coach walks over or books | 5-day wait; crisis same-day |

## Case tracking
Unreached after day 7 → registrar checks enrolment and contact details; dean of
students welfare check if no contact by day 10.

## Loop closure
Instructors get a one-line update in the alert tool within 5 working days:
"Contacted; connected with tutoring" (no private details).

## Measures and comparison
| Reach rate | ≥80% | Fall 2025 flagged list: 52% |
| Connected to a service | ≥50% of reached | Fall 2025: not tracked |
| Course completion, flagged students | +5 pp vs Fall 2025 flagged students | Same flag criteria |
Caveat: Fall 2026 midterm grading changed; differences may partly reflect that.
```

## Techniques Used

- **AG-11 Taxonomy-Based Classification Systems** — five reason categories drive the message and the service.
- **DS-06 Prioritization and Severity Guidance** — safety, deadlines, and multiple flags first.
- **RP-02 Audience-Specific Framing** — non-deficit messages written per reason category.
- **DS-40 Follow-Up Action Extraction** — each contact produces a status and a dated next action.
- **QA-12 False Positives Identification** — guards against "sent" as support and pre-post as proof.

## Related Prompts

- `domain-education-teaching/program/evaluation-analytics/program_early_warning_system_designer.md` — the system that produces the flagged list.
- `domain-education-teaching/program/curriculum-design/program_remediation_pathway_designer.md` — structured academic remediation once a student is reached.
- `domain-education-teaching/program/student-success/program_first_year_advising_touchpoint_model.md` — the universal calendar that hands cases to this plan.
