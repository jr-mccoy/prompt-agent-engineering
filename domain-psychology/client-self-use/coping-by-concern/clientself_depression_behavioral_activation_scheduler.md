---
title: "Behavioral Activation Scheduler"
category: psychology/client-self-use/coping-by-concern
description: "Help a client schedule behavioral activation activities — small, specific, mood-aware activities that reverse the depression-withdrawal-flatness loop."
techniques:
  - ST-04
  - DT-02
  - ED-04
  - DS-02
difficulty: beginner
tags:
  - client-self-use
  - depression
  - behavioral-activation
  - activity-scheduling
  - cbt
intended_use: model-testing
updated: "2026-05-08"
---

# Behavioral Activation Scheduler

## Objective

Help a client schedule activities matched to depression's specific physics: action precedes motivation; small precedes large; doing precedes feeling. Output a 1-week schedule of small, specific activities tagged by mastery (M) and pleasure (P), with mood ratings before and after.

## When to Use

- Mild-to-moderate depression with significant withdrawal.
- After a stretch of "I should be doing more but I can't get started."
- Between sessions when therapist has assigned BA-style work.

## When Not to Use

- Severe depression with risk — needs clinician contact, not solo scheduling.
- Burnout from over-doing — opposite intervention (rest, subtraction).

## Inputs / Context

- Current activity floor (what is the client doing today, even minimally).
- Pre-depression activities the client used to enjoy or get a sense of mastery from.
- Time available daily.
- Energy patterns (when is energy least bad).
- Social access (anyone the client could text / see).
- What's gotten in the way of activation in the past.

## Constraints

### Must

- Output a 7-day schedule with 2–3 activities per day, each:
  - Specific (when, where, with whom, for how long)
  - ≤ 15 minutes for first 2 days; ≤ 30 minutes for the rest of the week
  - Tagged M (mastery — sense of achievement) and/or P (pleasure)
  - Predicted mood (0–10 before) and actual mood (0–10 after) tracked
- Front-load with smallest possible items — taking the trash out, walking to the mailbox, washing one dish.
- Mix M and P; depression often gives back mastery before pleasure.
- Schedule for client's lower-energy windows, not their wishful-thinking peak windows.
- Add 2 social contacts in the week (text / call / brief in-person).
- Include "if I don't do it, what's the smaller version" line per item.

### Must Not

- Don't list "go to the gym" or "meal prep for the week" as starter activities.
- Don't moralize about not having done these.
- Don't tell the client to "feel better" by doing the activities — the order is action → mood, not motivation → action.
- Don't substitute for risk assessment if SI present.

## Instructions

1. Find the activity floor (what's already happening).
2. Generate a small-first ramp.
3. Tag each item M / P.
4. Schedule for realistic energy windows.
5. Add 2 social contacts.
6. Add backup "smaller version" per item.

## Output Format

```
=== BEHAVIORAL ACTIVATION — 1 WEEK ===

Activity floor (what's happening today, baseline): [...]
Energy windows (when is least-bad): [...]

Day 1 (smallest):
- [Time] — [Activity, ≤ 15 min] — Tag: [M / P / both]
   Predicted mood (0–10): __    Actual after: __    Smaller version if I can't: [...]
- [...]

Day 2 (smallest):
- [...]

Day 3:
- [...]
- [Social contact: text [name] — 1 line]

Day 4:
- [...]

Day 5:
- [...]
- [Social contact: brief call or in-person, 10 min cap]

Day 6:
- [...]

Day 7:
- [Mini review: which activities had biggest mood-bump? Pattern?]
- [...]

Reminders to me:
- Action comes before motivation. If I wait to feel like it, depression keeps me waiting.
- Smaller is better than nothing. The trash-going-out version counts.
- Predicted mood bump is usually less than actual mood bump in depression — track this; it's data.
- This is a CBT technique called Behavioral Activation. It works in studies as well as antidepressants for mild-moderate depression — but it requires actually doing the small thing.

When to skip this and reach a clinician instead:
- SI is rising
- I literally cannot get out of bed for ≥ 2 days
- I'm using substances daily to cope
- My therapist hasn't seen me in 2+ weeks and I'm losing function
```

## Verification

- [ ] Activity floor identified.
- [ ] Day 1–2 activities ≤ 15 min, very small.
- [ ] Each activity tagged M / P.
- [ ] Mood predicted and actual tracked.
- [ ] 2 social contacts in the week.
- [ ] Smaller-version backup per item.
- [ ] Scheduled for realistic energy windows.
- [ ] No "go to the gym" starters.
- [ ] Risk-routing exit present.
