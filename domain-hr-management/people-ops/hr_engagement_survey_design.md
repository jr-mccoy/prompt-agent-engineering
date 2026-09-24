---
title: "Engagement Survey — Design Against Decisions, Read Within the Noise, Close the Loop"
category: hr-management/people-ops
description: "Run an employee engagement survey end to end from the people-ops seat: each item tied to a decision someone will make, an anonymity threshold set before launch, results read against a stated noise band rather than ranked, open text coded before it is quoted, and one to three committed actions with owners and a report-back date — distinct from research_survey_instrument_designer (generic item-writing craft this routes wording to) and psychology_organizational_culture_diagnostic (framework-based culture assessment)."
techniques:
  - ST-02
  - DS-02
  - QA-04
  - NE-24
  - CM-02
difficulty: intermediate
tags:
  - engagement-survey
  - employee-listening
  - survey-analysis
  - anonymity
  - action-planning
  - people-ops
updated: "2026-09-24"
related_prompts:
  - domain-research-academic/research_survey_instrument_designer.md
  - domain-psychology/research-organizational/psychology_organizational_culture_diagnostic.md
  - domain-hr-management/people-ops/hr_exit_interview.md
---

# Engagement Survey

**Objective:** Design, read and act on an employee engagement survey so that it changes
something: items chosen because a named person will decide something with the answer,
anonymity protected by a threshold set before launch, results interpreted against a
stated noise band, and a small number of committed actions reported back to the people
who answered. A survey with no pre-committed owner for the results is refused, because
asking and then doing nothing damages trust more than not asking.

**When to Use:**
- You are about to run an annual or pulse survey and want to know what to ask.
- Results are in and leadership is about to rank teams by score.
- Last year's survey produced a slide deck and nothing else.

**Distinct from:**
- `../../domain-research-academic/research_survey_instrument_designer.md` — the general
  craft of item wording, scales and bias control. Use it for the wording of any new item;
  this prompt decides *which* items, for *whom*, and what happens *after*.
- `../../domain-psychology/research-organizational/psychology_organizational_culture_diagnostic.md`
  — a framework-based assessment of culture. This is a recurring operational instrument.
- `hr_exit_interview.md` — listens to people who are leaving; this listens to those who stayed.

---

## Inputs

1. **Headcount by team**, and the smallest team size.
2. **The decisions leadership expects to make this year** that employee sentiment should inform.
3. **Previous survey items and results**, if any, with response rates.
4. **Who owns acting on results** — named, with time budgeted.
5. **Platform and its anonymity controls** — can it suppress small groups? Who can see raw data?

---

## Method

1. **Gate: name the owner before writing an item.** If nobody will commit time to act on
   the results within one quarter, stop. Recommend not surveying and say why.

2. **Choose items against decisions (CM-02).** For each candidate item, name the decision
   it informs and who makes it. An item with no decision attached is dropped. Keep
   15–25 items for an annual survey, 5–8 for a pulse. Keep the items you tracked last
   year unchanged in wording, or the trend is broken. Route new wording through the
   survey instrument designer.

3. **Set the anonymity threshold before launch.** Minimum respondents for any cut to be
   shown, commonly 5, higher for sensitive demographic cuts. Groups below it are rolled
   up. Publish the threshold in the invitation. Changing it after seeing results is not
   permitted.

4. **Define the metrics and the noise band (DS-02, QA-04).** Report percent favourable
   (top two boxes) per item, with the response rate beside every figure. As a working
   rule, treat differences smaller than about 1/√n (in proportion points, for the smaller
   group) as noise. That gives ±8 points at n = 144 and ±29 points at n = 12. The rule is
   a screening heuristic, not a significance test. Route any consequential comparison to
   an analyst.

5. **Read, do not rank.** Report the three strongest and three weakest items overall,
   changes from last year that exceed the noise band, and team cuts only where n clears
   the threshold. A league table of teams inside the noise band invites managers to be
   judged on sampling error.

6. **Code open text before quoting it.** Build a small set of themes, count comments per
   theme, and only then select representative quotes. Remove anything that identifies the
   writer. A single vivid comment is an anecdote until the count says otherwise.

7. **Commit one to three actions and close the loop (NE-24).** For each action: the finding
   it answers, the owner, the date, and how progress will be visible. Map the path from
   finding to action. Name every handoff, and find where last year's actions stalled.
   Report back to all staff within 30 days of closing the survey, including what you
   chose not to act on and why.

---

## Output Format

```markdown
## Engagement survey — [org], [cycle]

### Design
| Item | Decision it informs | Decision owner | Tracked from last year? |
|---|---|---|---|
Anonymity threshold: [n], published in invitation · Items: [count] · Owner of results: [name]

### Results
Response rate: [x of y = z%]
| Item | % favourable | Last year | Change | Beyond noise band (±[b])? |
|---|---|---|---|---|
Team cuts shown: [teams ≥ threshold] · rolled up: [teams below]

### Open text
| Theme | Comments | Representative quote (de-identified) |
|---|---|---|

### Actions
| Finding | Action | Owner | Date | How progress is visible |
|---|---|---|---|---|

### Not acting on
[finding — reason]

### Report-back
Date: [≤30 days after close] · Channel: [...]
```

---

## Verification

- [ ] A named owner committed to acting before the survey launched
- [ ] Every item maps to a decision and a decision owner
- [ ] Tracked items kept last year's wording exactly
- [ ] The anonymity threshold was set and published before launch, and applied to every cut
- [ ] Every percentage is shown with its response rate or n
- [ ] Only changes beyond the stated noise band are described as changes
- [ ] Open text was coded into counted themes before quotes were chosen
- [ ] One to three actions, each with owner, date and visible progress
- [ ] The report-back names what will not be acted on

## False-Positive Prevention

1. **Do not rank teams inside the noise band.** A team at 58% and one at 66%, each with
   n = 12, are statistically indistinguishable. Presenting them as ranked punishes a
   manager for sampling error.
2. **A falling score after a hard year is not necessarily a management failure.** Check
   what else changed first: layoffs, reorganisation, a pay freeze.
3. **Low response rates bias toward the extremes.** Below about 50%, say the results
   describe respondents, not the organisation.
4. **One comment is not a theme.** Count before quoting, and do not let the most
   articulate complaint set the agenda.
5. **Never de-anonymise to "help".** Using writing style, team size or tenure to guess
   who wrote a comment breaks the promise the response rate depends on. Refuse requests
   to do it.
6. **An eNPS-style single number hides the reason.** Report it only alongside the items
   that explain it.
7. **Do not promise action on everything.** Ten actions with no owners is the pattern
   that made the last survey's results feel ignored.

**Legally careful, per this domain's standing principles.** Demographic cuts touch
protected characteristics. Collect them only where there is a stated purpose and a
lawful basis. Apply a higher threshold, and do not publish any cut small enough to
identify someone.

---

## Example

**Context:** 180 employees, 9 teams. Owner: the COO, with 4 hours a week budgeted in Q1.
20 items, 14 tracked from last year. Threshold 5, published. Survey closed 17 Nov.

- **Response:** 144 of 180 = 80%. Seven teams clear the threshold; two teams of 4 and 3
  are rolled into their department.
- **Noise band overall:** 1/√144 ≈ 0.083 → ±8 points.

| Item | Favourable | Last year | Change | Beyond ±8? |
|---|---|---|---|---|
| I understand how my work connects to company priorities | 62% | 71% | −9 | Yes, narrowly: Medium confidence |
| My manager gives me useful feedback | 74% | 72% | +2 | No |
| I can see myself here in two years | 55% | 58% | −3 | No |

- **Open text:** 61 comments. Top themes: "priorities changed without explanation" (19),
  "promotion criteria unclear" (14), tooling (9).
- **Actions (2):** (1) The COO publishes quarterly priorities with the reasons for any
  change, by 15 Jan. This answers the −9 item and the 19-comment theme. (2) Engineering
  publishes its career ladder by 1 Mar (`hr_career_ladder_framework.md`). This answers
  the 14-comment theme.
- **Not acting on:** tooling (9 comments). Already funded in the Q2 budget, so the
  report-back will say so.
- **Report-back:** all-hands on 12 Dec, 25 days after the survey closed.

---

## Techniques Used

- **ST-02 Structured Sequential Instructions** — gate, design, threshold, metrics, read, code, act.
- **DS-02 Metric Specification** — percent favourable with n and a stated noise band.
- **QA-04 Uncertainty Acknowledgment** — changes inside the band are reported as no change.
- **NE-24 Insight-to-Action Chain Mapping** — each finding traced to an owned action and a report-back.
- **CM-02 Constraint Specification** — anonymity threshold fixed before launch; no de-anonymising.

## Related Prompts

- `../../domain-research-academic/research_survey_instrument_designer.md` — wording for any new item
- `../../domain-psychology/research-organizational/psychology_organizational_culture_diagnostic.md` — deeper culture assessment
- `hr_exit_interview.md` — the leavers' view, to triangulate against
- `hr_career_ladder_framework.md` — a common action when promotion clarity scores low
