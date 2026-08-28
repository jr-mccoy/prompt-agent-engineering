---
title: "Goal System Designer"
category: decision-making
description: "Design a coherent goal system for a team or org: top-level objective, key results that gate it, cascading sub-goals owned by named layers, review cadence, and the rule for what to drop. Output is a single-page system that can run for a quarter or longer without re-litigation, with explicit failure modes and a cascade-integrity check."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - DS-06
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - decision-making
  - goal-system
  - okrs
  - alignment
  - cadence
  - team-design
updated: "2026-04-26"
related_prompts:
  - domain-decision-making/decisioning_chained_alignment_evaluator.md
  - domain-decision-making/decisioning_multi_constraint_optimizer.md
  - domain-productivity/operating-cadence/cos_clarify_fuzzy_goals.md
  - domain-software-engineering/analysis/business/okr_analysis.md
---

# Goal System Designer

**Objective:** Design a goal system for a team, function, or organization that consists of: one top-level objective, 3–5 key results that gate the objective, a cascade of sub-goals owned by named layers (function, team, individual), an explicit review cadence with kill / change / continue rules, and a documented "what to drop when overloaded" policy. The output is a single-page system that can run for a planning cycle (quarter, half, year) without weekly re-litigation.

**When to Use:**
- A new planning cycle is starting and the goals are still vague.
- The current goal system is generating activity but not progress.
- A team has grown and the cascade between top-level intent and individual work has frayed.
- A reorg or strategy shift means the existing goals no longer match the world.

**When NOT to use:**
- The user only needs a single goal stated more clearly. Use `cos_clarify_fuzzy_goals.md`.
- The user already has goals and wants to evaluate progress mid-cycle. Use `decisioning_chained_alignment_evaluator.md`.
- The user wants OKR theory or templates only. Use `okr_analysis.md`.
- The user is designing engineering-team OKRs in a single-team scope. The legacy `domain-personal-development/prompts/goals/goals_goal_system_designer.md` covers that narrower case.

**Audience:** Founders, CEOs, function heads, team leads, chiefs of staff, anyone responsible for getting an org to row in one direction.

---

## Inputs / Context

1. **Scope of the system.** Whose goals are we designing? Single team, function, business unit, whole org. Include headcount and number of layers.
2. **Time horizon.** Quarter, half, year, multi-year.
3. **Strategic input.** The 1–2 most important strategic moves the org is trying to make this cycle. If unclear, the system cannot be designed — stop and request.
4. **Top-level objective candidate.** A draft, even rough. The prompt will sharpen it.
5. **Constraints.** Headcount cap, budget cap, hiring freeze, contractual commitments, regulatory deadlines.
6. **Existing goal system.** What is currently in place. Even broken systems contain useful information about what was tried.
7. **Failure history.** What has gone wrong with goals here in the past? Goal inflation, abandonment mid-cycle, sandbagging, decoupling from compensation, dashboard rot.

If strategic input is empty, **stop**. A goal system designed without a strategy serves no objective.

---

## Constraints

### Must
- Produce **one** top-level objective. Not three. Not five.
- Top-level objective must be a measurable outcome, not an activity. ("Reach 30% pilot-to-paid conversion by Q3" — not "Run pilot program.")
- Produce 3–5 key results that, taken together, mean the top-level objective is achieved. Each KR is a number or a binary milestone with a date.
- Cascade sub-goals to each named layer (function, team, individual where appropriate). Each sub-goal must be traceable upward to a specific KR.
- Each goal at every layer has a single owner with a name (or "TBD — name by [date]" if unfilled). No co-ownership without a named lead.
- Define a review cadence: when, who attends, what each review *decides* (not just reports). Reviews that decide nothing are banned.
- Include kill / change / continue rules: under what evidence does a sub-goal get killed, changed, or continued at the next review.
- Include an explicit drop-policy: when overloaded, which goals get dropped first and which are protected. This is the single most-skipped step and the most common failure mode.
- Run a cascade-integrity check: every sub-goal traces to a KR; every KR traces to the objective; no orphan goals.

### Must Not
- Allow more than one top-level objective. Multi-objective systems silently re-rank in the field and cause drift.
- Confuse activity with outcome. "Ship feature X" is an activity; the outcome is what feature X enables.
- Permit unowned goals.
- Silently inflate ambition past capacity. If KRs sum to more capacity than the team has, the system breaks under contact.
- Output a system without a drop-policy. Without it, the team will drop randomly under stress.
- Cascade more than 3–4 layers without justifying each layer. Most cascades break past 3 layers.
- Include vanity metrics (impressions, mentions) as KRs unless explicitly tied to a downstream outcome.

---

## Instructions

### Step 1 — Sharpen the top-level objective
Take the draft objective. Apply three filters:
- **Outcome filter:** Is it a measurable outcome, not an activity?
- **Single-goal filter:** Is it one objective, or three smashed together?
- **Time-bound filter:** Does it have a horizon-end date?

Output the sharpened objective in one sentence.

### Step 2 — Define key results
Generate 3–5 candidate KRs. For each:
- The metric or milestone.
- The threshold (number, percentage, or binary).
- The date.
- The relationship to the objective (additive, gating, or evidentiary).

Test the set: if all 3–5 KRs were achieved, would the objective necessarily be true? If no, revise the KR set. If yes, lock.

### Step 3 — Cascade sub-goals
For each named layer below the top:
- Translate each KR into 1–3 sub-goals owned by that layer.
- Sub-goals are owned by a single name; co-ownership is converted to "lead + supporting."
- Cap total sub-goals per layer at the smaller of (a) layer headcount * 1.5 or (b) what can fit on one page. Goal counts that don't fit on a page get dropped, not nested.

Mark each sub-goal with the KR it traces to.

### Step 4 — Capacity check
Sum committed time per sub-goal across the cascade. Compare to available capacity (headcount * cycle length, with realistic discount for ops, support, and meetings — usually 50–70%).

If committed > available, flag overload. Recommend cuts in priority order before locking the system.

### Step 5 — Review cadence
Design the review rhythm:
- **Weekly stand-up:** owners report blockers and update KR progress in numbers.
- **Bi-weekly check-in:** function leads compare progress to forecast; identify slipping KRs.
- **Mid-cycle review:** kill / change / continue decision per sub-goal.
- **End-of-cycle review:** final scoring, lessons captured, inputs to next cycle.

For each cadence, name what gets *decided*, not just what gets reported. Reviews without decisions are dropped.

### Step 6 — Kill / change / continue rules
For each sub-goal, write the rules:
- **Kill if:** [specific evidence — owner gone, blocker unresolvable, market shifted].
- **Change if:** [specific evidence — wrong target, right intent].
- **Continue if:** [evidence of forward progress, even slow].

These rules are pre-committed at design time so mid-cycle reviews are not negotiation theater.

### Step 7 — Drop-policy
Write the explicit rule for what gets dropped under overload. Two acceptable patterns:
- **KR-priority order:** "If we cannot deliver all KRs, we drop in this order: KR-3, KR-4, KR-5. KR-1 and KR-2 are protected."
- **Outcome-class order:** "We drop internal-facing goals before customer-facing; we drop optimization goals before foundational goals."

State the rule and have the owners pre-commit before the cycle starts.

### Step 8 — Cascade-integrity check
Walk the system bottom-up:
- Every individual sub-goal traces to a team sub-goal.
- Every team sub-goal traces to a function sub-goal.
- Every function sub-goal traces to a KR.
- Every KR traces to the objective.

Flag orphans (goals with no upward trace) and orphans-by-implication (KRs that no sub-goal serves). Both are system bugs.

---

## False-Positive Prevention

1. **Activity disguised as outcome.** "Run a customer-research program" looks like a goal but is an activity. The outcome is whatever the research changes — pricing, segment, retention. Outcome must be the goal.
2. **Goal inflation.** A system that "stretches" past plausible capacity does not motivate; it teaches the team that goals are aspirational fiction. Cap at capacity * 1.0–1.2, not 2x.
3. **Vanity-metric KRs.** "Generate 1M impressions" or "100 LinkedIn posts" are activities masquerading as outcomes. Replace with the conversion downstream of the impression or post.
4. **Co-ownership theater.** Two owners means no owner. Always name a single lead.
5. **Decoupling from comp / promo.** A goal system that does not affect compensation, promotion, or budget is a writing exercise. Flag if the user has not addressed downstream incentives.
6. **Cadence without decisions.** Reviews that read out a dashboard without making a kill / change / continue call drift into status theater. Force a decision at every review.
7. **Drop-policy avoidance.** Most teams refuse to write the drop-policy because it forces a public ranking. The drop-policy is exactly the artifact that makes the system survive contact with reality.
8. **Cascade depth past 3–4 layers.** Cascades that go 5–6 layers deep almost always lose fidelity. If the org has more layers, group some.
9. **One-and-done design.** A system designed once and never revised will degrade. Build the next-cycle review into the cadence.

---

## Output Format

```
# Goal system — [scope] — [horizon]

## Top-level objective
> [one sentence — measurable outcome with date]

## Key results
| # | KR | Threshold | Date | Relationship to objective |
|---|----|-----------|------|---------------------------|
| 1 | [...] | [...] | [...] | additive / gating / evidentiary |

## Cascade

### Function: [name]
| Sub-goal | Owner | Traces to KR | Capacity (% of FTE) |
|----------|-------|---------------|----------------------|
| [...]    | [...] | KR-[#]        | [%]                  |

### Team: [name]
| Sub-goal | Owner | Traces to | Capacity |
|----------|-------|-----------|----------|

### Individual: [name]
| Sub-goal | Owner | Traces to | Capacity |
|----------|-------|-----------|----------|

## Capacity check
- Committed: [%] of available capacity.
- Verdict: [under / at / over capacity]
- Cuts proposed if over: [list]

## Review cadence
| Cadence | Frequency | Attendees | Decision made |
|---------|-----------|-----------|----------------|
| Stand-up | Weekly | Owners | Unblock |
| Check-in | Bi-weekly | Function leads | Forecast vs plan |
| Mid-cycle | Mid-horizon | All owners | Kill / change / continue per goal |
| End-of-cycle | Last week | All | Score + carry-forward |

## Kill / change / continue rules
[Per sub-goal or per category — explicit triggers.]

## Drop-policy
> [Single rule the team has pre-committed to.]

## Cascade-integrity check
- Orphans (sub-goals not tracing upward): [list or "none"]
- Unsupported KRs (KRs no sub-goal serves): [list or "none"]
- Verdict: [pass / fix needed]

## Next-cycle inputs
- Open questions to revisit at end-of-cycle: [list]
```

---

## Verification

- [ ] Exactly one top-level objective, stated as a measurable outcome with a date.
- [ ] 3–5 KRs that, taken together, would constitute objective achievement.
- [ ] Every sub-goal has a single named owner.
- [ ] Every sub-goal traces to a KR; every KR traces to the objective.
- [ ] Capacity check is performed and over-capacity systems are cut, not deferred.
- [ ] Review cadence specifies *decisions made*, not just reports.
- [ ] Kill / change / continue rules are pre-committed for each goal or category.
- [ ] Drop-policy is explicit and pre-committed.
- [ ] Cascade-integrity check finds no orphans.
- [ ] No vanity metrics or activity-disguised-as-outcome goals remain.
