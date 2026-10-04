---
title: "Analytics Request Intake Triage — The Real Question, the Decision It Serves, Effort, and a Priority You Can Defend"
category: data-analytics/framing-and-metrics
description: "Triage a queue of inbound data and analysis requests before any one gets a plan: recover the real question behind each ask, name the decision and its date, size effort in bands, score decision value on anchored scales, route self-serve and duplicate asks away, and publish a ranked queue with a provisional reply to every requester."
techniques:
  - MP-03
  - DP-03
  - DS-06
  - DP-16
difficulty: intermediate
tags:
  - request-triage
  - analytics-intake
  - prioritization
  - stakeholder-management
  - analytics-team
  - backlog
  - too-many-data-requests
  - everything-is-urgent
  - which-request-first
updated: "2026-10-02"
related_prompts:
  - domain-data-analytics/framing-and-metrics/analytics_question_to_analysis_plan.md
  - domain-agentic-resources/skills/non-coding/cross-domain/intake-triage-pattern/SKILL.md
  - domain-sales-customer/support/support_ticket_triage_and_routing.md
---

# Analytics Request Intake Triage

**Objective:** Turn a pile of data requests into a ranked, defensible queue — each
request restated as the question behind it, tied to a decision and a date, sized,
scored, and either scheduled, redirected, merged, or declined with a reason the
requester can see.

**When to Use:**
- An analyst or small analytics team has more requests than hours, and order is set
  by whoever asked last or loudest.
- Requests arrive as "can you pull…" with no stated purpose.
- The same question arrives from three teams in three wordings.
- You need to explain to a manager why their request is fourth, not first.

**When NOT to use:**
- You have already chosen the request and need to scope it —
  `domain-data-analytics/framing-and-metrics/analytics_question_to_analysis_plan.md`
  takes one request and produces its plan; this prompt sits upstream and ranks many.
- You need to **design** the intake system itself (front door, form fields, service
  levels) for any kind of team — `domain-agentic-resources/skills/non-coding/cross-domain/intake-triage-pattern/SKILL.md`.
  This prompt runs one triage pass over an analytics queue.
- The queue is customer support tickets —
  `domain-sales-customer/support/support_ticket_triage_and_routing.md`.
- The question is which product features to build — that is product prioritisation in
  `domain-product-management/`.

## Inputs / Context

1. **The requests, verbatim**: who asked, when, the text, any stated deadline.
2. **Team capacity** for the period in analyst-hours, after run-the-business work
   (recurring reports, data fixes).
3. **Current commitments** already in flight and their remaining effort.
4. **Organisational priorities** for the period (the 3–5 goals leadership has named).
5. **Existing assets**: dashboards, self-serve tools, prior analyses that may already
   answer some requests.

## Method

1. **Recover the real question (MP-03).** For each request, ask or infer: what decision
   will this inform, who makes it, by when, and what they believe now. Mark the
   decision `CONFIRMED` or `ASSUMED — confirm`. A request with no decision is
   `monitoring` or `curiosity`.
2. **Redirect before ranking.** Route out requests that:
   - are answered by an existing dashboard or analysis (send the link);
   - are self-serve lookups under 15 minutes (do them or teach once);
   - duplicate another request (merge, name both requesters);
   - belong to another team (data engineering, finance, research).
3. **Size effort in bands.** S (< 4 h), M (4–16 h), L (2–5 days), XL (> 1 week or new
   data needed). Note data-readiness blockers separately; a request blocked on data is
   not "XL", it is "blocked".
4. **Score decision value on anchored scales (DP-03).** Fix anchors before scoring:
   - *Stakes*: 1 = < $10k or a team-level choice … 5 = > $1M, a pricing, hiring, or
     launch decision.
   - *Time-criticality*: 1 = no date … 5 = decision date within 2 weeks and the answer
     can still change it.
   - *Alignment*: 1 = no link to named goals … 5 = directly serves a named goal.
   - *Confidence the analysis changes the decision*: 1 = decision already made … 5 =
     genuinely open, and the data can discriminate.
   `Value = Stakes × 0.35 + Time × 0.25 + Alignment × 0.2 + Changes-decision × 0.2`.
5. **Prioritise (DS-06).** Rank by value per effort band; schedule into capacity
   with ~20% held for urgent unplanned work. Anything with a decision already made
   (score 1 on "changes the decision") drops to the bottom regardless of seniority.
6. **Reply to every requester (DP-16).** A provisional message: what you understood
   the question to be, its status (scheduled for [date], redirected to [link], merged
   with [request], declined because [reason]), and the date by which they can object.
7. **Record the triage** so the next pass starts from it, and track how many requests
   were redirected or declined — that is the analytics team's leverage metric.

## Output Format

```
# Analytics triage — [team]   Period: [..]   Capacity: [..] h (after run work and 20% buffer)

## Redirected / merged / declined
| # | Requester | Ask | Action | Link or reason |

## Scored queue
| # | Requester | Real question | Decision (owner, date) | Status | Effort | Stakes | Time | Align | Changes | Value | Rank |

## Scheduled this period
| Rank | Request | Effort | Start | Due | Analyst |
Capacity used: [..] of [..] h

## Not scheduled (and why)
## Replies sent
| Requester | Message summary | Objection deadline |
```

## Verification

- [ ] Every request has a real question and a decision, or is labelled monitoring/curiosity.
- [ ] Anchors were fixed before scoring.
- [ ] Redirects and merges happened before ranking.
- [ ] Scheduled effort fits stated capacity with the buffer held back.
- [ ] Every requester has a reply with status and an objection deadline.
- [ ] Assumed decisions are marked for confirmation.

## False-Positive Prevention

1. **Seniority as priority.** A VP's curiosity request is still curiosity. Score the
   decision, then let leaders overrule openly if they choose.
2. **Precision in the value score.** 3.45 vs 3.40 is a tie; break ties on effort and
   date, and say so.
3. **Effort guessed optimistically.** Requests needing new data or a new metric
   definition are routinely 3× the first estimate. Band them, and flag data readiness.
4. **Doing redirectable work.** If a dashboard answers it, building a one-off
   analysis trains the organisation to bypass the dashboard.
5. **Silent declines.** A request dropped without a reply comes back as an escalation.
6. **Decisions already made.** Analysis requested to justify a decision taken is
   documentation, not analysis. Score it honestly.

## Example Output

```
# Analytics triage — Growth analytics (2 analysts)   Period: 6–17 Oct
Capacity: 2 × 60 h = 120 h − 30 h recurring reports − 18 h buffer = 72 h

## Redirected / merged / declined
| 1 | Ops lead      | "Weekly signups by channel"          | redirect | Acquisition dashboard, tab 2 |
| 2 | Marketing mgr | "Why did trial conversion drop?"     | merge with #6 | same question, both named |
| 3 | Sales dir     | "Prove the new territory plan works" | declined as analysis; offered a measurement plan | plan approved 30 Sep |

## Scored queue (anchors fixed 3 Oct)
| # | Requester | Real question | Decision | Status | Effort | St | Ti | Al | Ch | Value | Rank |
| 4 | CFO      | Does annual-plan discount cannibalise monthly revenue? | Q1 pricing, 24 Oct | CONFIRMED | L 32 h | 5 | 4 | 5 | 4 | 4.55 | 1 |
| 5 | PM Onboarding | Did the new checklist raise week-1 activation? | Roll out to all, 20 Oct | CONFIRMED | M 12 h | 3 | 5 | 4 | 5 | 4.10 | 3 |
| 6 | Head of Growth (+ #2) | Is the trial-conversion drop real or a tracking change? | Pause paid campaign? 13 Oct | CONFIRMED | M 10 h | 4 | 5 | 4 | 4 | 4.25 | 2 ⚑ |
| 7 | CS lead  | Churn rate by industry | none named | ASSUMED — curiosity | M 14 h | 2 | 1 | 3 | 2 | 1.95 | 4 |
⚑ #6 ranks second on value but its decision date (13 Oct) is first, and it is M effort
→ scheduled to start first, in parallel with #4.

## Scheduled this period
| 1 | #6 trial conversion | 10 h | 6 Oct  | 9 Oct  | Analyst A |
| 2 | #4 annual discount  | 32 h | 6 Oct  | 17 Oct | Analyst B |
| 3 | #5 checklist        | 12 h | 10 Oct | 15 Oct | Analyst A |
Capacity used: 54 of 72 h; 18 h left for #7 only if its decision is confirmed.

## Not scheduled
#7 — no decision named; offered 30-min call to find one.

## Replies sent
| CS lead | "Understood as churn by industry for curiosity; parked until a decision is named." | 8 Oct |
| Sales dir | "Analysis can't prove the plan works before it runs; here is how we'll measure it." | 8 Oct |
```

## Techniques Used

- **MP-03 Task Clarification** — the decision, owner, date, and prior belief recovered for each ask.
- **DP-03 Anchored Scoring Scales** — stakes, time, alignment, and decision-openness scored on fixed anchors.
- **DS-06 Prioritization and Severity Guidance** — ranking by value within effort bands against stated capacity.
- **DP-16 Provisional Decision Message Template** — every requester gets a status with an objection deadline.

## Related Prompts

- `domain-data-analytics/framing-and-metrics/analytics_question_to_analysis_plan.md` — scoping the request once it is chosen.
- `domain-agentic-resources/skills/non-coding/cross-domain/intake-triage-pattern/SKILL.md` — designing the intake system itself.
- `domain-sales-customer/support/support_ticket_triage_and_routing.md` — triage for customer support queues.
