---
title: "Job Search Pipeline Tracker and Weekly Cadence — Find the Stage That Is Leaking"
category: personal-development/job-search
description: "Set up and run an active job search as a pipeline: a tracker with defined stages and conversion rates, a weekly cadence sized to real hours, a diagnosis of which stage is leaking and why, and one change per week — ending at the offer, which is handed off to the offer-evaluation prompt."
techniques:
  - DS-02
  - OC-03
  - RT-09
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - job-search
  - pipeline
  - application-tracking
  - weekly-review
  - funnel-metrics
  - candidate
  - no-callbacks
  - job-hunt-stalled
  - organize-applications
updated: "2026-09-24"
related_prompts:
  - domain-personal-development/prompts/life-transitions/lifetransition_job_loss_recovery_plan.md
  - domain-personal-development/major-decisions/personal_career_offer_evaluation.md
  - domain-personal-development/job-search/jobsearch_target_role_and_market_map.md
---

# Job Search Pipeline Tracker and Weekly Cadence

**Objective:** Produce a pipeline tracker with fixed stage definitions, the
current conversion rate between each stage, a diagnosis of the one stage
most limiting results, a weekly cadence that fits the hours the candidate
actually has, and the single change to make this week.

**When to Use:**
- You are actively searching and cannot say how many applications became
  screens, or screens became onsites.
- You feel busy and are getting nowhere, and do not know whether the problem
  is volume, targeting, the résumé, or interviews.
- You want a weekly routine that survives a bad week.
- **Not this prompt if** you have just lost a job and are not ready to search —
  `domain-personal-development/prompts/life-transitions/lifetransition_job_loss_recovery_plan.md`
  locates the recovery phase first and refuses to push a frantic search. Use
  this prompt once that plan reaches its re-entry phase.
- **Not this prompt if** you have an offer to weigh — hand off to
  `domain-personal-development/major-decisions/personal_career_offer_evaluation.md`
  for the decision, and `domain-negotiation/contexts/negotiation_salary_raise_promotion.md`
  for negotiating terms. This prompt stops at the offer.

## Inputs / Context

**Required:**
1. **Every opportunity so far**: company, role, source (board, referral,
   recruiter, outreach), date applied, furthest stage reached, outcome.
   A spreadsheet export or a rough list is fine.
2. **Target role family** and, if run, the kill signal from
   `jobsearch_target_role_and_market_map.md`.
3. **Hours per week available** for the search, measured, and any hard date
   (end of severance, visa, lease).

**Optional:**
- Which résumé version and which stories were used for each opportunity.
- Rejection feedback, verbatim.

## Method

1. **Fix the stage definitions.** Use these, and do not blur them:
   **Target** (identified, not yet applied) → **Applied** → **Screen**
   (first human conversation) → **Interview** (hiring-manager or loop) →
   **Final** → **Offer**. Plus two side channels: **Outreach** (message sent)
   and **Conversation** (held). Every opportunity sits in exactly one stage
   with a date entered.

2. **Build the tracker (OC-03).** One row per opportunity with the columns in
   the output format. Mark anything with no movement in 21 days as
   **Stale**; stale rows are closed or followed up, not counted as live.

3. **Compute conversion by stage and source (DS-02).** Applied→Screen,
   Screen→Interview, Interview→Final, Final→Offer; separately for referral,
   outreach-sourced, recruiter-inbound, and cold applications. Show counts
   alongside every rate — "1 of 2" is not "50%" in any useful sense.

4. **Diagnose the leak (RT-09).** Find the earliest stage with the lowest
   conversion relative to the others and trace it to a cause:

   | Leaking stage | Likely root cause | Where to fix it |
   |---|---|---|
   | Applied→Screen | targeting or résumé, or cold-only sourcing | `jobsearch_target_role_and_market_map.md`, `jobsearch_resume_evidence_rewriter.md`, `jobsearch_networking_outreach_plan.md` |
   | Screen→Interview | pitch, fit narrative, or level mismatch | `jobsearch_job_posting_fit_decoder.md`, `career_positioning_statement.md` |
   | Interview→Final | behavioral answers or technical depth | `jobsearch_behavioral_interview_story_bank.md` |
   | Final→Offer | often outside the candidate's control; check feedback before changing anything | — |

   State the evidence for the cause, not just the symptom.

5. **Size the weekly cadence to real hours.** Allocate the stated hours
   across: targeting and decoding, tailored applications, outreach,
   conversations, interview prep, and a 30-minute weekly review. Weight
   toward the leaking stage. State the **bad-week version**: the minimum that
   keeps the pipeline alive (e.g. two outreach messages and the review).

6. **Pick one change (DS-06).** One adjustment for the coming week, aimed at
   the leak, with the metric that will show whether it worked and when it
   will be read. Changing résumé, targets and outreach in the same week makes
   the next review uninterpretable.

7. **Check the kill signal and the offer boundary.** If the target map's kill
   signal has fired, say so and send the candidate back to that prompt. If an
   offer exists, stop pipeline work on that row and hand off.

## Output Format

```
# Search pipeline — [name], week of [date]

## Tracker
| Company | Role | Source | Stage | Date entered stage | Next action | Due | Stale? |

## Conversion
| Transition | All | Referral | Outreach | Recruiter | Cold |
(each cell: n of m, rate)

## Diagnosis
Leaking stage: [...]
Evidence: [...]
Root cause: [...]
Fix lives in: [prompt]

## Weekly cadence ([n] hrs)
| Block | Hours | Why this weight |
Bad-week version: [...]

## This week's one change
[change] — measured by [metric], read on [date]

## Checks
Kill signal: [fired / not fired]
Offers to hand off: [none / company → offer evaluation, then negotiation]
```

## Verification

- [ ] Every opportunity is in exactly one defined stage with a date.
- [ ] Rows with 21+ days of no movement are marked stale.
- [ ] Every conversion rate shows its counts.
- [ ] The diagnosis names evidence and a cause, not only the low number.
- [ ] Cadence hours sum to no more than hours available, and a bad-week version exists.
- [ ] Exactly one change is set, with a metric and a read date.
- [ ] Any offer is handed off; no offer terms are negotiated here.

## False-Positive Prevention

1. **Application count is not progress.** Forty cold applications and zero
   screens is a targeting or résumé problem that more volume will not fix.
2. **Small numbers lie.** A 0-of-3 Screen→Interview rate is a prompt to look
   at those three screens, not proof of a pitch problem. Say when the sample
   is too small to diagnose.
3. **Stale rows inflate the pipeline.** A search with 25 "live" applications,
   18 of them silent for a month, has 7 live applications.
4. **Rejection at Final is not always about the candidate.** Internal
   candidates, budget freezes and headcount moves close roles; do not rewrite
   everything after one final-round loss.
5. **Market timing is not a diagnosis.** "It's a slow market" may be true, but
   if referral-sourced applications convert and cold ones do not, the fix is
   still sourcing.
6. **Busy is not the same as weighted.** A cadence that spends most hours on
   applications while interviews are the leak looks diligent and changes
   nothing.
7. **Changing three things at once hides which one worked.** One change per
   week keeps the tracker useful as evidence.

## Example Output

```
# Search pipeline — Chen W. (QA engineer → SDET), week of 2026-09-28

## Tracker (excerpt; 31 rows total)
| Company | Role | Source | Stage | Entered | Next action | Due | Stale? |
|---|---|---|---|---|---|---|---|
| Logistics SaaS | SDET II | Referral | Interview | Sep 22 | Loop Oct 2 — prep S2, S5 | Oct 1 | No |
| Fintech | QA Automation Eng | Cold | Applied | Aug 25 | Close | — | Yes |
| Health-tech | SDET | Outreach | Screen | Sep 24 | Send thank-you + sample repo | Sep 29 | No |

## Conversion (6 weeks)
| Transition | All | Referral | Outreach | Recruiter | Cold |
|---|---|---|---|---|---|
| Applied→Screen | 6 of 27 (22%) | 3 of 3 | 2 of 4 | 1 of 2 | 0 of 18 |
| Screen→Interview | 3 of 6 | 2 of 3 | 1 of 2 | 0 of 1 | — |
| Interview→Final | 0 of 1 concluded (2 pending) | 0 of 1 | — | — | — |

## Diagnosis
Leaking stage: Applied→Screen, cold channel only.
Evidence: 0 of 18 cold vs 5 of 7 via referral or outreach; the same résumé was used for all.
Root cause: sourcing mix, not the résumé — the résumé gets screens when a person forwards it.
Fix lives in: jobsearch_networking_outreach_plan.md
Interview→Final (0 of 1) — too small to diagnose.

## Weekly cadence (10 hrs)
| Block | Hours | Why this weight |
|---|---|---|
| Outreach + conversations | 4 | The channel that converts |
| Interview prep (Oct 2 loop) | 3 | Only live loop |
| Tailored applications (referral or warm only) | 2 | Cut cold volume |
| Weekly review | 0.5 | Update tracker, read metric |
| Buffer | 0.5 | — |
Bad-week version: 2 outreach messages + the review.

## This week's one change
Stop cold applications; send 6 outreach messages to people at target companies — measured by conversations booked, read on Oct 5.

## Checks
Kill signal: not fired (target was ≥2 screens from 25 by Oct 15; currently 6).
Offers to hand off: none.
```

## Techniques Used

- **DS-02 Metric Specification** — fixed stages and counted conversion rates by source.
- **OC-03 Markdown Table Specification** — the tracker and conversion tables have set columns.
- **RT-09 Root Cause Explanation** — the leaking stage is traced from symptom to cause to the prompt that fixes it.
- **DS-06 Prioritization Guidance** — one change per week, weighted to the leak.
- **QA-12 False Positives Identification** — names the metrics that look like progress but are not.

## Related Prompts

- `domain-personal-development/prompts/life-transitions/lifetransition_job_loss_recovery_plan.md` — the phase before an active search, after a job loss.
- `domain-personal-development/major-decisions/personal_career_offer_evaluation.md` — where an offer goes next (then `domain-negotiation/contexts/negotiation_salary_raise_promotion.md` for terms).
- `domain-personal-development/job-search/jobsearch_target_role_and_market_map.md` — the target and kill signal this tracker checks.
