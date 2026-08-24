---
title: "Design an Email / Message Triage System"
category: productivity/deep-work
description: "Design a triage system for the user's specific inbox and message streams that routes each incoming item to one of five actions (now, today-batch, week-batch, delegate, drop) based on their actual sender mix and role — not a generic GTD template."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-02
  - OC-01
  - QA-01
difficulty: intermediate
tags:
  - deep-work
  - triage
  - email
  - messages
  - workflow
updated: "2026-04-20"
related_prompts:
  - domain-productivity/deep-work/deepwork_calendar_audit.md
  - domain-productivity/deep-work/deepwork_self_interruption_audit.md
  - domain-productivity/deep-work/deepwork_focus_parameters_estimator.md
---

# Design an Email / Message Triage System

**Objective:** Produce a triage rule set tailored to the user's real inbox and message streams. Every incoming item should map to exactly one of five actions: handle-now, today-batch, week-batch, delegate, drop. The rules must name actual senders, topics, and channels — not categories in the abstract.

**When to use:** When messages are interrupting deep-work blocks, when "inbox anxiety" is a stated blocker, or before designing focus blocks (triage must be bounded in time cost or the focus system will leak).

**Audience:** An individual designing their own triage, not a team-wide policy.

---

## Inputs Required

1. **A sample of 30–50 recent messages across all streams** (email, Slack/Teams, SMS, tickets). For each: sender, channel, subject or first line, and whether they replied within 24 hours.
2. **The user's role and the top three deliverables it owes.** One sentence each.
3. **Current triage behavior.** How often they check, for how long, whether they check during focus blocks.
4. **A list of "true emergencies" from the last 90 days** — times someone genuinely needed them in under 2 hours. Include who and why.
5. **Channels the user cannot turn off** (boss's DM, on-call pager, partner's text).

If item 4 is empty, the emergency tier is empty and the system should be stricter.

---

## Instructions

1. **Cluster the 30–50 sampled messages** by (sender × topic). Report the top 8 clusters with counts.

2. **For each cluster, assign one of five actions:**
   - **handle-now** — only if this cluster contains true emergencies from input 4, or blocks someone else in under 2 hours
   - **today-batch** — reply by end of day in a single session
   - **week-batch** — reply once a week on a named day
   - **delegate** — forward or redirect, not reply (requires a named delegate target)
   - **drop** — archive without reply; note whether to inform sender

   Every cluster must get exactly one action. If a cluster sometimes gets one action and sometimes another, split it by whatever field actually distinguishes them.

3. **Write the decision rule for each cluster in one line**, naming real things. Example: "Cluster: 'Recruiter cold outreach via LinkedIn DM' → drop, no reply."

4. **Compute the time cost of the system.** How many minutes per day will today-batch + week-batch + handle-now consume, given the volume in inputs? If this exceeds 60 min/day, cut — raise the bar for today-batch until it fits.

5. **Name the three rules most likely to break.** For each, note the failure mode ("boss's peer emails about their project, I'll feel guilty dropping") and the specific mitigation.

6. **Specify when triage happens.** Two or three named windows per day, none inside a protected focus block, with hard time caps.

---

## Output Format

```
## Triage Rule Set

| Cluster (sender × topic) | Volume/wk | Action | Rule |
|---|---|---|---|
| ... | ... | ... | ... |

## Emergency Definition
- Only these count as handle-now: [list from input 4]
- Everything else waits.

## Time Budget
- Today-batch window(s): [time(s), duration]
- Week-batch window: [day, duration]
- Expected daily cost: NN min
- Over budget? yes/no. If yes, what was cut.

## Rules Most Likely to Break
1. [rule] — fails when [condition] — mitigation: [specific action]
2. ...
3. ...

## One-Week Review Trigger
- Revisit this system after 7 days; if >N rules were broken, the rules are wrong, not the user.
```

---

## Constraints

**Must:**
- Name real senders and topics from the supplied sample.
- Keep emergency tier empty unless input 4 populates it.
- Fit the system inside a daily time budget ≤ 60 min.
- Place triage windows outside focus blocks.

**Must not:**
- Recommend any specific app, filter syntax, or automation tool.
- Suggest "inbox zero" as a goal; the goal is bounded time cost, not empty.
- Use categories like "urgent/important" without tying them to real message patterns.
- Create a rule the user does not have authority to enforce (e.g., "your boss must use email instead of DM").

---

## False-Positive Prevention

- **Fantasy emergency:** If the user claims many emergencies but input 4 is sparse, trust input 4. Most "urgent" messages are socially urgent, not operationally urgent.
- **Hidden status messaging:** Reply speed sometimes functions as status signaling to a boss or client. If the user's role depends on looking responsive, a pure week-batch rule for that sender will fail. Name this.
- **Delegate without a delegate:** Do not propose delegate unless a specific named person or system exists to delegate to.
- **Over-automation:** Filter rules become stale and hide real messages. Prefer human-window batching over clever filters.

---

## Self-Verification (before finalizing)

- [ ] Every cluster is drawn from the supplied 30–50 messages.
- [ ] Every cluster has exactly one action.
- [ ] Emergency tier matches input 4.
- [ ] Total time budget ≤ 60 min/day.
- [ ] Triage windows do not overlap any stated focus block.
- [ ] At least three failure modes are named with mitigations.
- [ ] No specific app or filter syntax appears in the output.
