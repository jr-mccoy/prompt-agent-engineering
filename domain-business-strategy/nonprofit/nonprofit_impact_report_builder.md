---
title: "Impact Report Builder — Results Against an Existing Logic Model, Every Number Tagged"
category: business-strategy/nonprofit
description: "Turn a program's existing logic model, measured results and actual spend into a funder or donor impact report — results against targets with honest denominators, provenance tags on every figure, what fell short and why, and consented stories only — without re-deriving the logic model or inventing numbers; distinct from program_logic_model_designer, which builds the model this prompt reports against."
techniques:
  - RT-23
  - QA-26
  - DS-02
  - NE-15
  - RT-05
difficulty: intermediate
tags:
  - nonprofit
  - impact-report
  - program-evaluation
  - donor-communications
  - funder-reporting
  - outcomes
  - grant-report-due
  - show-donors-results
  - annual-report
updated: "2026-09-24"
related_prompts:
  - domain-education-teaching/program/evaluation-analytics/program_logic_model_designer.md
  - domain-education-teaching/program/evaluation-analytics/program_program_evaluation_framework.md
  - domain-business-strategy/nonprofit/nonprofit_case_for_support.md
---

# Impact Report Builder

**Objective:** Produce an impact report that shows what a program actually achieved
against the targets in its logic model — with every figure tagged by where it came
from, shortfalls reported alongside successes, and nothing invented to fill a gap.

**When to Use:**
- A grant's interim or final report is due.
- Year-end donor impact report or annual report section.
- The board wants results against the targets set last year.

**Not this prompt if:**
- You have no logic model, or need to redesign one —
  `domain-education-teaching/program/evaluation-analytics/program_logic_model_designer.md`
  owns that. This prompt takes the model as **input** and does not re-derive it; if
  the model is missing, stop and build it first.
- You need an evaluation design (methods, comparison groups, data collection) —
  `domain-education-teaching/program/evaluation-analytics/program_program_evaluation_framework.md`.
- You need the forward-looking fundraising argument — `nonprofit_case_for_support.md`.

## Inputs

1. **The logic model:** activities, outputs, outcomes, indicators and the targets set
   for the period.
2. **Measured results** per indicator, each with source, date and denominator.
3. **Actual spend** for the period from the finance records, against budget.
4. **Funder report template** or required questions, if any.
5. **Consented stories and quotes**, with the consent terms.
6. Known problems during the period: staffing gaps, closures, changes to the plan.

## Method

1. **Tag every input by provenance (RT-23).** Before writing, classify each figure:

   | Tag | Meaning |
   |---|---|
   | `[measured]` | Counted or assessed by the program, record exists |
   | `[self-reported]` | Participant survey or testimony |
   | `[estimated]` | Calculated or extrapolated — method stated |
   | `[external]` | Third-party data, with source and year |
   | `[not measured]` | The logic model has the indicator, the program did not collect it |

   `[not measured]` is reported as such. It is never filled in.

2. **Report results against targets with the right denominator (DS-02).** For each
   indicator: target, actual, denominator, variance. Where more than one denominator
   is defensible (enrolled vs completed), show both and say which the target used.

3. **Separate outputs from outcomes.** Sessions delivered are outputs; changes in
   participants are outcomes. Report them in different sections.

4. **Report shortfalls and their reasons.** Every missed target gets one plain
   sentence on why and what changes. Funders trust reports that contain a miss.

5. **Claim contribution, not attribution (RT-05).** Unless the evaluation design
   supports causal claims, write "participants gained" rather than "the program
   caused".

6. **Shape the narrative for the reader (NE-15).** Lead with the one result that
   matters most to this reader, then the table, then the story. For a funder, follow
   their template order exactly.

7. **Run the first-invented-fact test (QA-26).** Read the draft sentence by sentence
   and stop at the first figure or detail that does not trace to a tagged input.
   Fix it, then continue. Repeat until the draft is clean.

## Output Format

```
# Impact report — [program], [period], for [reader]

## Headline
[the one result that matters most, with its tag]

## Results against targets
| Indicator | Target | Actual | Denominator | Variance | Tag |

## Outputs (what we did)
## Outcomes (what changed)
## What fell short, and what changes
| Target missed | Why | Change for next period |

## How the money was used
| Line | Budget | Actual | Variance |

## A story (consented)
## Provenance and limits
[what was not measured; which denominators were used; contribution statement]
```

## Verification

- [ ] Every figure carries a provenance tag.
- [ ] Targets are copied from the logic model, not reset after the fact.
- [ ] Rates state their denominator.
- [ ] At least one shortfall is reported if any target was missed.
- [ ] Spend figures match the finance records.
- [ ] The first-invented-fact test found nothing on the final pass.

## False-Positive Prevention

1. **Do not re-derive the logic model.** If the draft starts proposing new outcomes,
   stop: that is `program_logic_model_designer.md`'s job and changes the targets
   being reported against.
2. **Do not move the goalposts.** Reporting against a target set after results were
   known is a misrepresentation, even when the new target is more sensible.
3. **Choose the denominator before seeing the rate.** Switching from "enrolled" to
   "completed" because it looks better is the most common inflation in impact
   reporting.
4. **Never fill a `[not measured]` gap.** Write that it was not measured and what
   will be measured next period.
5. **No invented beneficiaries.** No composites, no unconsented details, no quotes
   polished beyond what was said.
6. **Contribution, not causation.** Pre/post change in participants is not proof the
   program caused it without a comparison.
7. **Dual failure:** a report so hedged the reader cannot find the result fails too.
   State the headline plainly; put the limits in their own section.

## Example Output

```
# Impact report — Riverbend Adult Literacy Tutoring, Jan–Dec 2025, for Hartwell Family Foundation

## Headline
42 of 72 enrolled adults (58%) gained at least one reading level [measured],
against a target of 55% of enrolled.

## Results against targets
| Indicator | Target | Actual | Denominator | Variance | Tag |
| Learners enrolled | 75 | 72 | — | −3 | [measured] |
| Gained ≥1 reading level | 55% of enrolled | 58% (42) | 72 enrolled | +3 pts | [measured] |
| Same, of those assessed at exit | — | 70% (42) | 60 assessed | — | [measured] |
| Report using skills at work | 50% | — | — | — | [not measured] |

## Outputs
2,880 tutoring sessions logged by 41 volunteer tutors [measured]; 4 tutor trainings.

## Outcomes
Reading-level gains above. Twelve enrolled learners left before exit assessment;
their outcomes are unknown and counted as not gaining in the headline rate.

## What fell short
| Target missed | Why | Change |
| Enrolment 72 vs 75 | Coordinator vacancy Mar–Apr paused intake | Cross-trained a second intake volunteer |
| Work-use indicator not collected | Survey not built | Exit survey added Jan 2026 |

## How the money was used
| Line | Budget | Actual | Variance |
| Program total | $81,000 | $79,200 | −$1,800 (coordinator vacancy) |
Cost per enrolled learner: $79,200 / 72 = $1,100.

## A story
None supplied with consent for this report. [request from program staff]

## Provenance and limits
Headline uses enrolled learners as the denominator, as the target did. Gains are
pre/post on the program's own assessment; no comparison group — we report
contribution, not causation.
```

## Techniques Used

- **RT-23 Input Provenance Tagging:** every figure carries its source class.
- **QA-26 First-Invented-Fact Test:** the draft is scanned for the first untraceable detail.
- **DS-02 Metric Specification:** target, actual and denominator per indicator.
- **NE-15 Data Storytelling Framework:** headline, table, then story.
- **RT-05 Evidence-Based Reasoning:** contribution claims stay within the evidence.

## Related Prompts

- `domain-education-teaching/program/evaluation-analytics/program_logic_model_designer.md` — the model this report consumes
- `domain-education-teaching/program/evaluation-analytics/program_program_evaluation_framework.md` — evaluation design
- `domain-business-strategy/nonprofit/nonprofit_case_for_support.md` — where these results feed the next ask
