---
title: "Reconcile Planned Week Against What Actually Happened"
category: productivity/reviews
description: "Given a stated weekly plan and the evidence (calendar, commits, messages, notes), produce a delta report — where time actually went, where the plan was wrong, and what to update for next week."
techniques:
  - ST-01
  - ST-02
  - RT-05
  - RT-06
  - DS-02
  - QA-12
difficulty: intermediate
tags:
  - time-audit
  - reconciliation
  - plan-vs-actuals
  - review
  - evidence-based
updated: "2026-05-08"
related_prompts:
  - domain-productivity/deep-work/deepwork_calendar_audit.md
  - domain-productivity/reviews/reviews_weekly_systems_review.md
  - domain-productivity/reviews/reviews_monthly_quarterly_cadence.md
  - domain-personal-development/prompts/agency/agency_weekly_review.md
  - domain-productivity/bottlenecks/bottleneck_locator.md
---

# Reconcile Planned Week Against What Actually Happened

**Objective:** Take last week's stated plan and last week's actual evidence (calendar, commits, sent messages, notes, output artifacts) and produce a delta. Output: where time actually went, where the plan was systematically wrong, and a small set of updates for the next plan. Not motivational. Not retrospective in the agency sense. A telemetry pass.

**When to use:** End of week, before the next week's plan is set. Run before any cadence-level review (`reviews_weekly_systems_review.md`, `agency_weekly_review.md`, monthly review) — those depend on accurate telemetry, and most users overestimate how accurately they remember the week.

**Audience:** An individual reviewing their own week. Single-week scope. Multi-week patterns belong to `reviews_monthly_quarterly_cadence.md` or `deepwork_calendar_audit.md`.

---

## Inputs Required

1. **Stated plan from start of last week.** What the user committed to do, in their own words. If no plan was written, refuse — there is nothing to reconcile against. Minimum: 3 named items with rough hour estimates.
2. **Calendar evidence.** Last week's actual calendar — meetings held, blocks kept or skipped, blocks added mid-week. Hours per category if tagged; otherwise, raw events.
3. **Output evidence.** Concrete artifacts produced: commits, drafts, messages sent, decisions made, files touched. List or rough log.
4. **Communication evidence.** Counts or rough volumes for: messages sent in primary channels, meetings actually attended, async writeups posted.
5. **Mid-week interruptions and changes.** Things that pulled the user off plan: an outage, a request, an emergency, a sudden meeting block. Be honest about which were genuinely external vs. which were self-introduced.
6. **Subjective sense at end-of-week.** One sentence: did the week feel productive, scattered, blocked, or something else?

If input 1 is missing or vague ("I was going to work on stuff"), output: *"No reconcilable plan exists for last week. Run this prompt prospectively — write a plan now, run reconciliation next week."*

---

## Instructions

### Step 1 — Bucket the actual time

Build a simple table of where time actually went, drawn only from inputs 2–4 (not from memory):

| Bucket | Hours (rough) | Source evidence |
|---|---|---|
| Planned work item A | | calendar / commits / messages |
| Planned work item B | | ... |
| Unplanned but internal-decision work | | |
| Unplanned external (input 5) | | |
| Meetings (planned) | | |
| Meetings (added mid-week) | | |
| Async communication / triage | | |
| Slack / interruption / context switch | | inferred from interleaving |
| Unaccounted | | |

Total to ~ 40–50 hours of waking work-window. If "Unaccounted" exceeds 20% of the total, flag it: the evidence base is thin and confidence in this audit is low.

### Step 2 — Compute the plan-vs-actuals delta

For each item in input 1, compare estimated to actual hours. Format:

| Plan item | Estimated | Actual | Delta | Hit? |
|---|---|---|---|---|
| ... | 8h | 3h | -5h | No |
| ... | 4h | 6h | +2h | Yes (over) |

"Hit" = within ±25% of estimate AND the work it was meant to produce was produced. A plan item with the correct hours but no output is *not* a hit.

### Step 3 — Identify the systematic patterns

Looking at the deltas and the bucketed hours, name 2–4 specific patterns observable from this single week. Examples:

- "Unplanned external work consumed 9h, of which 5h was a single incident."
- "Two of three planned work items hit estimate; the third was halved by mid-week meeting additions."
- "Async/triage absorbed 11h — higher than the user's estimated baseline of 5h."
- "Unaccounted is 8h on Wednesday; evidence is thin for that day."

These are observations from this week's data only. Do not generalize to "the user always …" from a single week.

### Step 4 — Compare patterns to the user's subjective sense (input 6)

Take input 6 and check it against the data:

- If the user said "scattered" and the data shows interruption / unplanned-external dominance, **confirmed**.
- If the user said "productive" but the planned-item hit-rate was low, **subjective sense disagrees with telemetry** — name this. Often a "felt productive but produced nothing" week is a deep-work depletion week, not a productive one.
- If the user said "blocked" but the data shows full hours on the planned items, **subjective sense disagrees** — name what was actually blocked (decision, dependency, motivation), not "the work."

### Step 5 — Diagnose plan vs. reality mismatches

For each missed plan item (Hit? = No), name one of the following causes from this week's evidence:

| Cause | Signal | Update for next plan |
|---|---|---|
| Underestimated hours | Actual = estimated × 1.5+ | Multiply this work-class estimate by your typical overrun ratio. |
| External shock | Specific interruption in input 5 absorbed the time | Plan with a 4–8h external-shock buffer. |
| Self-introduced interruption | New work added mid-week that wasn't in input 5 | Triage discipline: the new work was scheduled into next week, not this one. |
| Decision deferred | The work waited on a decision the user kept postponing | Decision needs to come *before* the work is on the plan. |
| Energy collapse | The hours existed but the user didn't / couldn't use them | Likely route to `agency_burnout_recovery.md` or `deepwork_focus_parameters_estimator.md`, not a plan tweak. |
| Wrong-level item | The plan item was vague ("work on X") and time scattered around the periphery | Decompose to a `agency_next_action_spec.md`-grade item. |

Name causes with evidence; do not guess.

### Step 6 — Output a small update list for the next plan

Maximum 3 updates. Each update is a *change* to next week's plan, not a generic resolution:

- ✓ "Add a 4h external-shock buffer Wednesday."
- ✓ "Decompose 'finish migration' into the next 3 ship-able pieces with hour estimates."
- ✓ "Move async triage into two 25-min blocks rather than ambient throughout the day."
- ✗ "Be more focused." (Generic; not a plan change.)
- ✗ "Don't get interrupted." (Outside the user's control.)

If more than 3 updates are warranted, the diagnosis is structural and should escalate to `reviews_weekly_systems_review.md` or `bottleneck_locator.md`. Say so.

### Step 7 — Set the next-week reconciliation hook

State: "The next plan is reconcilable if it includes: [N] named items with hour estimates, written *before* the week starts." This makes the loop self-sustaining.

---

## Constraints

### Must
- Use evidence (inputs 2–5), not memory, for the time-bucket table.
- Show estimated vs. actual side by side.
- Name 2–4 patterns from this week's data only.
- Compare subjective sense (input 6) against telemetry; name disagreements.
- Diagnose missed-plan causes with evidence.
- Output ≤ 3 updates, each a specific plan change.

### Must Not
- Diagnose character traits ("you have a focus problem") from one week.
- Recommend new productivity systems or apps.
- Recommend "be more disciplined" or motivation-class advice (refer to `domain-personal-development/`).
- Use "Hit" for plan items that consumed the right hours but produced no output.
- Output more than 3 updates.

---

## False-Positive Prevention

1. **Don't accept "I had a productive week" with thin evidence.** If output evidence (input 3) is thin, the productive feeling may have been busyness. State the disagreement.
2. **Don't blame "interruption" without distinguishing external vs. self-introduced.** Self-introduced mid-week additions look like interruptions but indicate planning failure or scope creep, not external shock.
3. **Don't generalize from one week.** Multi-week patterns require the monthly review prompt.
4. **Don't roll missed plan items into "do them next week" without diagnosing why they missed.** Rolling forward without diagnosis just produces the same miss.
5. **Don't conflate this with `agency_weekly_review.md`.** This prompt is plan-vs-actuals telemetry. Agency weekly review is portfolio / proof-of-work / direction. Run this *first*, then that.
6. **Don't recommend a calendar overhaul off of one week.** That's `deepwork_calendar_audit.md` territory and needs ≥ 4 weeks of data.

---

## Output Format

```
## Time bucket (from evidence)
| Bucket | Hours | Source |
|---|---|---|
| ... | ... | ... |
**Unaccounted:** Nh ([flag if > 20%])

## Plan-vs-actuals delta
| Plan item | Est. | Actual | Delta | Hit? | Output produced? |
|---|---|---|---|---|---|

## Patterns observed (this week only)
1. ...
2. ...
3. ...

## Subjective vs. telemetry
User said: "[input 6]"
Telemetry says: [confirmed / contradicted, in one sentence].

## Cause diagnosis (per missed item)
| Plan item | Cause | Evidence |
|---|---|---|

## Updates for next plan (max 3)
1. ...
2. ...
3. ...

(If more than 3 are warranted: structural — escalate to `reviews_weekly_systems_review.md` or `bottleneck_locator.md`.)

## Next-week reconciliation hook
For next week to be reconcilable: write a plan with [N] named items with hour estimates before the week starts.
```

---

## Verification

- [ ] Time-bucket table built from evidence inputs (2–5), not from memory.
- [ ] Unaccounted column reported and flagged if > 20%.
- [ ] Plan-vs-actuals delta shows estimate, actual, delta, hit (with output check).
- [ ] 2–4 patterns named from this week's data.
- [ ] Subjective sense compared against telemetry; disagreement named if present.
- [ ] Each missed item has a diagnosed cause from the table.
- [ ] No more than 3 plan updates output.
- [ ] No multi-week generalizations.
- [ ] No motivation-class advice.
