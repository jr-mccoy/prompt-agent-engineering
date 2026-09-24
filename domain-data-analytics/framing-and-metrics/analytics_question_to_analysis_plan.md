---
title: "Question to Analysis Plan — From a Vague Stakeholder Ask to a Decision-Linked Plan"
category: data-analytics/framing-and-metrics
description: "Turn a vague business ask (\"can you look into churn?\") into a one-page analysis plan: the decision it serves, the question restated so it can be answered, the metric and population, the comparison that would change the decision, the data and its known gaps, the cut list, and a stop rule — before any query is written."
techniques:
  - DD-02
  - MP-03
  - CM-03
  - DP-13
  - QA-02
difficulty: intermediate
tags:
  - analysis-plan
  - stakeholder-request
  - problem-framing
  - business-analytics
  - scoping
  - decision-support
updated: "2026-09-24"
related_prompts:
  - domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md
  - domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md
  - domain-science/statistics/science_pre_specified_analysis_plan.md
---

# Question to Analysis Plan

**Objective:** Convert a stakeholder's loosely worded request into a written analysis
plan that names the decision it informs and the result that would change that
decision, so the analyst builds the one analysis that matters instead of the ten
that are easy.

**When to Use:**
- Someone asked you to "look into", "dig into", or "pull the numbers on" something
  and did not say what they will do with the answer.
- You have been burned before by delivering a thorough analysis that nobody used.
- Several stakeholders want different things from the same request and you need one
  written scope to point at.
- The request would take more than half a day and you want agreement before starting.

**When NOT to use:**
- You need a pre-registered statistical analysis plan for research, with estimands and
  a data-lock date — `domain-science/statistics/science_pre_specified_analysis_plan.md`
  is the research version; this prompt is the business analyst's lighter, decision-first one.
- A known metric has already moved and you need to explain why —
  `domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md`.
- You are designing an experiment before launch — `domain-agentic-resources/skills/marketing/ab-test-setup/`.
- The ask is a two-minute lookup. Answer it; a plan costs more than the question.

## Inputs / Context

1. **The request, verbatim** — the Slack message, email, or meeting note. Do not
   paraphrase it before the plan does.
2. **Who asked, and who else will read the answer.**
3. **Any deadline, and what happens on that date** (a board meeting, a pricing
   change, a quarterly plan).
4. **Data you already know exists** — tables, dashboards, prior analyses.
5. **Prior answers to similar questions**, and whether anyone acted on them.

If the requester is reachable, ask the three questions in Step 1 before drafting
(MP-03). If not, draft with the decision marked `[ASSUMED — confirm]`.

## Method

1. **Find the decision (MP-03).** Ask, in this order:
   - "What will you do differently depending on the answer?"
   - "What do you currently believe the answer is?"
   - "By when do you need it to be useful?"
   If nobody can name a decision, the output is a *monitoring* request or a
   *curiosity* request. Say so in the plan and size it down accordingly.

2. **Restate the question so it can be answered (DD-02).** Replace every adjective
   with a measurable noun. "Are enterprise customers less engaged?" becomes "Among
   accounts on the Enterprise plan for ≥90 days, is median weekly active seats per
   licensed seat lower in Q3 than Q2?" Each restatement must name a **metric**, a
   **population**, a **time window**, and a **comparison**.

3. **Write the decision rule before looking at data (DP-13).** State the result that
   would move the decision each way, and the band where it would not:
   - "If seat utilisation fell by more than 5 points, we open the renewal-risk play."
   - "If it moved less than 2 points, we do nothing."
   - "Between 2 and 5, we look at the top 20 accounts by ARR by hand."
   A plan with no threshold ends up as whatever the data happens to show.

4. **Bound the scope (CM-03).** List what is **in**, what is **out**, and the cut list
   of segmentations you will run, capped at the number the deadline allows. Name the
   cuts you are deliberately *not* running and why. Every extra cut is another chance
   of a false positive.

5. **Name the data and its known gaps.** For each metric: the source table, the
   grain, the known definition issues, and whether a spec exists. If no spec exists,
   write one first — `analytics_metric_definition_spec.md`.

6. **Attack the plan (QA-02).** Before sending, answer:
   - Could this analysis come back with a result that changes nothing? If yes, why run it?
   - Is there a cheaper proxy that would give the same decision?
   - Which confounder (seasonality, a pricing change, a tracking change) would make
     the comparison unfair?

7. **Send the plan for sign-off**, with a stated default: "If I don't hear back by
   Thursday, I'll proceed with this scope."

## Output Format

```
# Analysis plan — [short name]      Requested by: [name]   Date: [date]

## Decision
[The decision this informs, and who makes it] — [CONFIRMED | ASSUMED — confirm]
Request type: [decision | monitoring | curiosity]

## Question (answerable form)
Metric: [..]  Population: [..]  Window: [..]  Comparison: [..]

## Decision rule (written before data)
| Result | Action |
|---|---|

## Scope
In: [...]   Out: [...]
Cuts run (max [n]): [...]   Cuts deliberately not run: [...] — because [...]

## Data
| Metric | Source | Grain | Spec exists? | Known issue |
|---|---|---|---|---|

## Risks to a fair comparison
- [confounder] — mitigation: [...]

## Effort and delivery
Estimate: [hours]   Delivery: [format, date]   Default if no reply: [...]
```

## Verification

- [ ] A named decision exists, or the plan says plainly that it does not.
- [ ] The question names metric, population, window, and comparison.
- [ ] The decision rule has thresholds in both directions plus a no-action band.
- [ ] The cut list is capped, and names the cuts that will not be run.
- [ ] Every metric either has a spec or has an action to write one.
- [ ] At least one confounder is named with a mitigation.

## False-Positive Prevention

1. **A request is not a question.** "Look into churn" has no answer. If the plan
   still holds an adjective ("engaged", "healthy", "struggling"), the restatement
   is not finished.
2. **Writing the threshold after seeing the number.** A decision rule written after
   the query has run is a rationalisation. Date-stamp the plan.
3. **Cut sprawl.** Twelve segment cuts at a 5% false-positive rate each give you
   roughly a coin-flip chance of at least one spurious "finding". Cap the cuts.
4. **Treating curiosity as a decision.** A curiosity request sized like a decision
   request wastes a week. Label it and time-box it.
5. **Inheriting the stakeholder's hypothesis as the frame.** Record what they
   believe (Step 1) so you can test it, not so you can confirm it.
6. **Assuming the metric is defined.** "Active user" has at least three definitions
   in most companies. Name which one before comparing periods.
7. **No default on silence.** Plans without a stated default stall in review.

## Example Output

```
# Analysis plan — Enterprise engagement    Requested by: VP Customer Success   Date: 2026-09-24

## Decision
Whether to launch the Q4 renewal-risk outreach to Enterprise accounts, owned by
VP CS — CONFIRMED on call 09-23.
Request type: decision

## Question (answerable form)
Metric: weekly active seats ÷ licensed seats (seat utilisation), account-week grain
Population: Enterprise-plan accounts with tenure ≥ 90 days on 2026-07-01
Window: Q3 2026 (Jul 1 – Sep 21) vs Q2 2026
Comparison: change in median account utilisation, and in share of accounts < 40%

## Decision rule (written before data, 2026-09-24)
| Result | Action |
|---|---|
| Median drop > 5 pts OR share < 40% up > 8 pts | Launch outreach to all < 40% accounts |
| Median change within ±2 pts | No outreach; revisit in Q1 |
| Anything between | Hand-review top 20 accounts by ARR |

## Scope
In: Enterprise plan, paid accounts only. Out: trials, Team plan, churned-before-Jul-1.
Cuts run (max 3): region, account size band, product line.
Cuts not run: industry, CSM owner — industry is self-reported and 30% null;
CSM owner is a performance question, not this decision.

## Data
| Metric | Source | Grain | Spec exists? | Known issue |
|---|---|---|---|---|
| Weekly active seats | fct_seat_activity | seat-day | Yes | SSO logins not counted before 08-04 [verify] |
| Licensed seats | dim_contract | contract | No — write spec | Mid-term upgrades overwrite prior value |

## Risks to a fair comparison
- SSO tracking change on 08-04 may inflate Q3 actives — compare Aug 4 onward
  against the same weeks of Q2, and report both.
- Summer seasonality — add a Q3-2025 vs Q2-2025 baseline.

## Effort and delivery
Estimate: 6 hours. Delivery: one-page memo, 2026-09-29.
Default if no reply by 2026-09-25 EOD: proceed with this scope.
```

## Techniques Used

- **DD-02 Vague-to-Concrete Translation** — every adjective in the ask becomes a metric, population, window, and comparison.
- **MP-03 Task Clarification** — the three questions that find the decision come before any drafting.
- **CM-03 Scope Definition** — explicit in/out lists and a capped cut list.
- **DP-13 Kill Signal Definition** — the decision rule states in advance what result changes the action.
- **QA-02 Adversarial Stress-Test** — the plan is attacked for no-decision outcomes and unfair comparisons.

## Related Prompts

- `domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md` — write the spec the plan depends on.
- `domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md` — when the question is "why did it move".
- `domain-science/statistics/science_pre_specified_analysis_plan.md` — the research-grade, pre-registered version.
