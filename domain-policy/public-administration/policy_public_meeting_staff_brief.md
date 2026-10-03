---
title: "Public Meeting Staff Brief — Agenda-Item Report and Official's Briefing for a Council, Board or Commission Meeting"
category: policy/public-administration
description: "Prepare the staff report and the one-page briefing an elected or appointed official reads before a council, board or commission meeting: the decision in one sentence and the motion language, background, legal authority and required findings, fiscal impact by year, options with alternative motions, public input summarised by position and theme, the questions officials and the public are likely to raise with sourced answers, and the procedural traps (notice, vote threshold, quasi-judicial contact rules, conflicts, serial-meeting risk) — distinct from an internal options memo (policy_options_memo), legislative testimony preparation, and a company board pack."
techniques:
  - NE-14
  - NE-23
  - RT-23
  - NE-17
difficulty: intermediate
tags:
  - staff-report
  - agenda-item
  - council-briefing
  - board-of-supervisors
  - open-meetings
  - public-hearing
  - prepare-council-for-meeting
  - staff-report-for-board
  - explain-agenda-item
updated: "2026-10-03"
reasoning:
  styles: [communicative, analytic, procedural]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: mixed
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, prose]
  user_role: [department_staff, city_manager_office, council_aide, board_clerk]
  mode: [synthesize, communicate]
related_prompts:
  - domain-policy/policy_options_memo.md
  - domain-science/public-engagement/science_congressional_or_parliamentary_testimony_prep.md
  - domain-finance/corporate-finance-fpa/finance_board_finance_package_builder.md
---

# Public Meeting Staff Brief

**Objective:** Make sure every official walks into the meeting knowing exactly what
they are being asked to decide, what it costs, what the public said, what they will
be asked, and what procedure the vote must follow — in a report the public can read
too, with the staff recommendation clearly separated from the facts.

**Audience:** Department staff writing agenda items; city, county or district
manager's office; council and board aides; clerks; and officials preparing their
own questions.

**When to Use:**
- An item is going on a council, board or commission agenda and needs a staff
  report and a briefing for each official.
- A contested item will draw public comment and officials need the questions in
  advance.
- The item has a procedural trap (public hearing, two readings, supermajority,
  quasi-judicial rules) that has caught the body before.
- **Not this prompt if** the decision is an internal choice among policy options
  with values trade-offs and no public meeting — use
  `domain-policy/policy_options_memo.md`. If a staff member or expert is
  **testifying** before a legislative committee, use
  `domain-science/public-engagement/science_congressional_or_parliamentary_testimony_prep.md`.
  A company's board pack is
  `domain-finance/corporate-finance-fpa/finance_board_finance_package_builder.md`.

## Inputs / Context

1. **The item**: what action is requested, by whom, and the draft motion,
   resolution or ordinance text.
2. **Body and procedure**: council, board or commission; legislative,
   administrative or quasi-judicial item; readings required; vote threshold; notice
   requirements already met.
3. **Facts and data**: background, history of prior actions, and the evidence base.
4. **Fiscal information**: one-time and recurring costs and revenues, funding
   source, budget amendment needed.
5. **Public input received**: comments, petitions, prior hearing testimony.
6. **Known positions and concerns** of officials, without lobbying them.

Every factual claim is tagged `[data]` with its source, `[estimate]`, or
`[staff view]`. Legal findings and procedure are `[verify — city attorney / clerk]`
unless supplied.

## Method

1. **Write the decision in one sentence and the motion.** If staff cannot state the
   action in one sentence, the item is not ready.
2. **Separate facts from recommendation.** Background, data and fiscal impact are
   neutral; the staff recommendation sits in its own labelled section.
3. **State authority and required findings.** The legal basis and any findings the
   body must make on the record (e.g. for a land-use or licensing decision).
4. **Fiscal impact by year (RT-23).** One-time and recurring, years 1–3, funding
   source, with each figure tagged. Revenue that falls as behaviour changes is shown
   falling.
5. **Options with alternative motions.** Approve as proposed, approve with named
   amendments, defer with a specific information request and return date, or
   decline — each with consequence.
6. **Summarise public input.** Counts by position and channel, the themes with
   representative quotes, and anything factual that staff have checked.
7. **Pre-empt the questions (NE-23).** The 6–10 questions officials and speakers
   are most likely to ask, each with a sourced short answer, and "unknown — staff
   will report back by [date]" where true.
8. **Flag procedural traps.** Notice and posting, readings, vote threshold,
   quasi-judicial ex parte disclosure, conflicts of interest and recusal, and the
   open-meetings risk of officials deliberating by reply-all email.
9. **Produce two versions (NE-14).** The full staff report for the public record,
   and a one-page official's brief: decision, motion, cost, three key facts, top
   questions, procedure.
10. **Close with the action (NE-17).** The exact motion text and what happens after
    each vote outcome.

## Output Format

```
# Staff report — [item title]   Meeting: [body, date]   Item type: [..]
Requested action (one sentence): [..]
Motion: "[..]"

## 1. Background
## 2. Authority and required findings
## 3. Fiscal impact
| | Yr1 | Yr2 | Yr3 | Source tag |
## 4. Options and alternative motions
## 5. Public input (counts, themes, fact-checks)
## 6. Staff recommendation (labelled as such)
## 7. Procedure: notice · readings · vote threshold · ex parte · conflicts · open-meetings
## 8. After the vote

--- Official's one-page brief ---
Decision · motion · cost · 3 facts · likely questions with answers · procedure
```

## Verification

- [ ] Requested action fits one sentence and matches the motion text.
- [ ] Recommendation is in its own section; background is neutral.
- [ ] Fiscal table covers three years with recurring and one-time separated.
- [ ] Every option has motion language and a consequence.
- [ ] Public input is counted and themed, not cherry-picked.
- [ ] Likely questions have sourced answers or a dated report-back.
- [ ] Procedure section is checked by the clerk or attorney.

## False-Positive Prevention

1. **Advocacy as background.** Facts selected to support the recommendation erode
   trust in every future report. Include the facts that cut the other way.
2. **Year-1 revenue as permanent.** Fines, fees and one-time grants often fall or
   end; show the trajectory.
3. **Comment counts as a vote.** Report counts, but weight themes by substance; a
   campaign of identical messages is one theme.
4. **Missing the alternative motion.** Officials who want a different outcome
   improvise motions from the dais; drafting them prevents defective motions.
5. **Ex parte contacts on quasi-judicial items.** Officials who discussed the matter
   privately may need to disclose; flag the rule, do not decide it.
6. **"No fiscal impact" because it is in the budget.** Already-budgeted spending is
   still a fiscal impact; say where it is budgeted.

## Example Output

```
# Staff report — School-zone speed safety cameras ordinance (first reading)
Meeting: City Council, 20 Oct 2026   Item type: legislative ordinance
Requested action: introduce an ordinance authorising speed cameras in 8 school zones.
Motion: "I move to introduce Ordinance 2026-41 establishing a school-zone speed safety
camera program, and set second reading for 3 November 2026."

## 1. Background
State law (enacted 2025) permits cities to operate school-zone cameras [verify]. In the
8 zones, 85th-percentile speed during school hours is 31 mph in a 20 mph zone [data:
Sept 2026 tube counts]; 14 injury crashes in 5 years, 3 involving children [data: police].

## 3. Fiscal impact ($000)
|                          | Yr1  | Yr2  | Yr3  |
| Fine revenue ($50, state cap [verify]) | 900 [estimate: 18,000 citations] | 450 [estimate: 9,000] | 400 |
| Vendor fixed fee (8 × $38k) | −304 | −304 | −304 [data: quote] |
| Admin 1.5 FTE + hearing officer | −240 | −240 | −240 [estimate] |
| Net                      | +356 | −94  | −144 |
Program costs more than it collects from Yr2 as speeding falls — do not budget fines as revenue.

## 4. Options
A. Introduce as proposed. B. Introduce with amendment: first violation a warning,
and income-based fine reduction (−$70k/yr [estimate]). C. Defer to 1 Dec with an
equity analysis of camera locations. D. Decline.

## 5. Public input (to 14 Oct)
212 comments: 128 support, 71 oppose, 13 other. Themes: child safety (102), privacy and
data retention (44), "revenue grab" (31), burden of fines on low-income drivers (22).
Fact-check: the ordinance limits image retention to 60 days unless contested.

## Likely questions
Q: Will this make money? A: Year 1 only; see fiscal table.
Q: Who sees the photos? A: Vendor and city hearing staff; 60-day deletion (§ 6).
Q: Do cameras work? A: [staff view] evaluations elsewhere show speed reductions; local
effect will be measured by before/after speed counts — report back in 12 months.

## 7. Procedure
Two readings; simple majority. Legislative item — no ex parte disclosure needed [verify].
No conflicts reported; each member to confirm. Please do not reply-all on this item.

--- Official's brief ---
Decide: introduce speed-camera ordinance (8 school zones). Cost: net −$94k from Yr2.
Facts: 31 mph in 20 zones; 14 injury crashes; 212 comments, 60% support.
Top questions: revenue, privacy, equity of fines. Procedure: first reading, majority.
```

## Techniques Used

- **NE-14 Multi-Audience Documentation Targeting** — the full public report and the one-page official's brief from one source.
- **NE-23 Objection Pre-emption** — likely questions answered with sources before the meeting.
- **RT-23 Input Provenance Tagging** — facts, estimates and staff views tagged so the recommendation is not mistaken for data.
- **NE-17 Call-to-Action Mandatory Close** — exact motion text and what follows each outcome.

## Related Prompts

- `domain-policy/policy_options_memo.md` — the internal options analysis behind a contested item.
- `domain-science/public-engagement/science_congressional_or_parliamentary_testimony_prep.md` — preparing a witness to testify before a legislature.
- `domain-finance/corporate-finance-fpa/finance_board_finance_package_builder.md` — the corporate board-pack counterpart.
