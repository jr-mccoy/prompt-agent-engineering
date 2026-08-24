---
title: "Weekly Automation Audit of Repetitive Browser Tasks"
category: business-strategy/browser-automation
description: "A weekly 15–30 minute audit of the previous week's browser activity to identify tasks worth automating — scored by frequency, friction, and automation fit — and to flag tasks that look automatable but shouldn't be."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - browser-automation
  - automation-audit
  - ops
  - workflow
  - weekly-review
updated: "2026-04-20"
related_prompts:
  - domain-business-strategy/browser-automation/browserauto_recording_blueprint.md
  - domain-business-strategy/browser-automation/browserauto_safety_check.md
  - domain-productivity/automation/automation_data_sync.md
---

# Weekly Automation Audit of Repetitive Browser Tasks

**Objective:** A repeatable 15–30 minute weekly audit that scans the previous week's browser activity and surfaces (1) tasks worth automating, scored on frequency × friction × automation fit, (2) tasks that *look* automatable but shouldn't be — because the variability or judgment involved makes automation a net negative, and (3) one concrete automation to prototype or record this week.

**When to use:** End of the week, or start of the following week, for an individual or small team running browser-based operational work. When "we keep doing this manually" has come up more than once. Before committing to a larger automation project — this audit is what tells you whether the idea is the right one.

**Audience:** Ops lead, individual contributor, automation engineer evaluating where to spend their next unit of automation effort. Not an infrastructure-level exercise — this is per-user or per-small-team.

---

## Inputs Required

1. **Activity signal from the past week.** Browser history, screen-time summaries, tab-usage data, or the user's own recall of what they spent time on. Even rough is usable.
2. **An inventory of previously attempted or active automations** — what works, what broke, what was retired.
3. **Tool constraints.** Which automation tools the user has access to (recorder-style tools, headless browsers, RPA, their org's approved list). This shapes "automation fit."
4. **Risk tolerance.** Specifically: what kinds of errors are unacceptable if an automation runs wrong. Billing / compliance / customer-facing actions are higher-stakes than internal lookups.
5. **Available time-to-build.** Realistic budget this week or next (hours, not weeks).

If the user can't supply activity signal (input 1), the audit produces generic recommendations. Push for at least a rough self-inventory of the week.

---

## Instructions

### Step 1 — Enumerate candidate tasks

From activity signal, list every browser task that happened 2+ times in the week or felt tedious even once. For each:
- **What** happens (verb-first).
- **Where** — which site(s) or tabs.
- **How often** this week.
- **Roughly how long** per run.
- **What triggers** the user to do it (time of day, a signal, a request).

Aim for 8–20 candidates. Short-list candidates that happened at least twice or are expected weekly going forward.

### Step 2 — Score each candidate on three axes

For each task:

- **Frequency:** daily / weekly / monthly / one-off. Anything less than monthly is usually not worth automating.
- **Friction per run:** low (<2 min, no context-switch) / medium (2–10 min, some focus) / high (>10 min, major context-switch or error-prone).
- **Automation fit:** good (deterministic inputs, stable site, low judgment) / partial (some variability or judgment) / poor (high variability, judgment-heavy, frequent UI changes) / risky (wrong action has material consequence).

The score is not a number; it's a label per axis. Good-fit high-friction weekly tasks are the sweet spot.

### Step 3 — Apply the "don't automate yet" filters

Flag candidates that should NOT be automated this week, even if they scored well, if any of the following apply:

- **The task is infrequent** (less than monthly) and small. Manual is cheaper than maintenance.
- **The site UI changes frequently** (recorded automation will break within 30 days; budget for maintenance exceeds savings).
- **The task involves judgment you haven't stabilized** (you still make different decisions case-by-case). Automating is premature; write the decision rule first.
- **The risk of the automation running wrong is high** (billing, compliance, customer comms) and no rollback or dry-run path exists.
- **The task is a symptom of a different underlying problem** (e.g., you keep copy-pasting between two systems that should have an integration). Automating the copy-paste entrenches the underlying problem.

For each filtered task, note which filter caught it — the filter is the useful output, not the exclusion.

### Step 4 — Pick the one to prototype this week

From the remaining candidates, pick one. Criteria, in order:

1. Fits in the available time-to-build.
2. Highest (frequency × friction) among good-fit candidates.
3. Low enough risk that a failed prototype does not produce a production incident.

Name the pick, why it won, and what you expect the payback to be in time-saved per week.

### Step 5 — One "stop automating" candidate

From the active-automations inventory (input 2), name one automation that should probably be retired or paused. Criteria:

- Runs frequently but fails more than 1 in 5 times.
- Saves less time than it takes to maintain.
- Covers a task that is no longer frequent or important.
- Produces output nobody reads or acts on.

If no automation meets this, say so. The point is to keep the fleet from bloating.

### Step 6 — Carry-forward list

Short list of candidates that weren't picked this week but are worth tracking:
- "Good fit, not enough time this week" — carry.
- "Good fit, but risk review needed first" — route to `browserauto_safety_check.md`.
- "Partial fit, would benefit from a judgment-rule first" — note the rule that needs writing.

### Step 7 — One observation about the week

One sentence: what did the audit reveal about the user's (or team's) week that is not itself a candidate for automation? Examples:
- "Most of this week's repetition happened inside one tool — the leverage is probably in using that tool's native features better, not automating the browser."
- "Every candidate touches the same two systems — there may be a single integration that eliminates three candidates at once."

Observations compound. The automation you build this week is often less valuable than what the audit teaches you about the week's shape.

---

## Constraints

### Must
- Score every candidate on all three axes.
- Apply the "don't automate yet" filters and name which filter caught each excluded task.
- Pick exactly one candidate to prototype this week.
- Name exactly one "stop automating" candidate (or explicitly say none qualifies).
- End with one observation about the week that isn't a candidate.

### Must Not
- Produce a long list of "would be nice to automate" without scoring.
- Recommend automating a task that is judgment-heavy without flagging it.
- Score frequency or fit by intuition alone; ground in the week's actual activity.
- Skip the retirement candidate. Automation fleets rot without pruning.
- Assume the user has tools they don't (validate against the tool-constraints input).

---

## False-Positive Prevention

1. **Don't automate rare tasks.** The maintenance tail dominates the time savings. Monthly is the practical floor; less than that, automate only if the task is also high-risk or high-error-prone manually.
2. **Don't automate judgment.** If you're still deciding case-by-case, the automation will do the wrong thing confidently. Write the decision rule first.
3. **Don't automate symptoms.** Copy-paste between two systems is usually a missing integration, not a missing automation. Flag these explicitly.
4. **Don't count high-friction as an automation case on its own.** High friction + low frequency is better solved by eliminating the task or batching it, not automating.
5. **Don't skip the retirement candidate.** Old automations that fail quietly are a worse risk than manual tasks — they run on autopilot and get trusted.
6. **If the week's activity signal is mostly communication / meetings,** say so. Browser automation is not the lever this week.

---

## Output Format

```
# Browser automation audit — [week of date]

## Candidate tasks ([count])
| Task (verb-first) | Where | Count/wk | Time/run | Trigger |
|-------------------|-------|----------|----------|---------|

## Scoring
| Task | Frequency | Friction | Automation fit |
|------|-----------|----------|----------------|

## Filtered out (and why)
- [Task] — filter: [infrequent / UI-volatile / judgment-unstable / high-risk-no-rollback / symptom-of-other-problem].

## This week's pick
- **Task:** [name]
- Why it won: [one line on frequency × friction × fit]
- Expected payback: [min saved per week]
- Time to build: [hours]

## Retirement candidate
- [Automation to pause/retire] — reason: [fails often / low payoff / stale purpose]
(or: "None this week; fleet is healthy.")

## Carry-forward
| Task | Reason deferred | Next step |
|------|-----------------|-----------|

## One observation about the week
[One sentence about the week's shape, not a candidate.]
```

---

## Verification

- [ ] Every candidate has all three axis scores.
- [ ] Filter applied to excluded candidates with reason named.
- [ ] Exactly one pick for this week with payback estimate.
- [ ] Retirement candidate named (or honest "none").
- [ ] One observation that isn't itself a candidate.
- [ ] Output fits on one to two screens.
