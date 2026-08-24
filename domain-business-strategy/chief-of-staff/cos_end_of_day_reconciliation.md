---
title: "End-of-Day Reconciliation: What Got Done vs Planned"
category: business-strategy/chief-of-staff
description: "A 5–10 minute end-of-day close: reconcile what actually got done against what was planned, capture loose context for tomorrow's reload, and pick one signal from the day worth carrying into the weekly review."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - RT-02
  - QA-01
difficulty: beginner
tags:
  - chief-of-staff
  - end-of-day
  - reconciliation
  - daily-close
  - reflection
updated: "2026-04-20"
related_prompts:
  - domain-business-strategy/chief-of-staff/cos_morning_briefing.md
  - domain-business-strategy/chief-of-staff/cos_weekly_review.md
  - domain-productivity/deep-work/deepwork_block_end_context_capture.md
  - domain-personal-development/prompts/agency/agency_end_of_session_review.md
---

# End-of-Day Reconciliation

**Objective:** A 5–10 minute end-of-day ritual that (1) reconciles what got done against what was planned for today, (2) captures just enough context for a fast reload tomorrow, (3) names one signal from today worth tracking into the weekly review. Stops short of grading the day.

**When to use:** Last 10 minutes before stopping work. Daily, same shape. Especially useful on days that felt busy without a clear deliverable, or days the morning briefing set a ship item.

**Audience:** Individual knowledge worker or executive. Same user that ran the morning briefing. Consistency across days is the point.

---

## Inputs Required

1. **Today's morning briefing** (if the user ran one). If not, today's planned list.
2. **What the user actually did.** From calendar, git/doc activity, slack/email sent, or best recall.
3. **Anything in progress at end of day** that will need to pick up tomorrow.
4. **Any waiting-fors that landed or shifted today.**

If the user has no plan to compare against (no briefing, no list), refuse to run a full reconciliation. Offer only Step 2 (reload capture) and a note that tomorrow's morning briefing is the fix.

---

## Instructions

### Step 1 — Reconcile ship item and plan

Compare the morning briefing / plan to what actually happened:

- **Ship item:** shipped / partial / displaced / not started. If displaced, by what.
- **Meetings:** happened as planned / added / cancelled / ran long.
- **Commitments due today:** delivered / late / renegotiated.

One line each. No narrative.

### Step 2 — Capture reload context

One short paragraph, for the user's future self tomorrow morning:
- Where is the work currently sitting?
- What was the last concrete step taken?
- What is the first move tomorrow?
- Any open questions blocking the first move.

Write this so the user can walk in tomorrow, read these 4 lines, and resume in under 2 minutes. This is the single most valuable output of the reconciliation.

### Step 3 — Record slippage

For anything that didn't ship or got displaced, one line per item:
- What.
- What displaced it (specific thing, not "got busy").
- Whether to reschedule, renegotiate, or drop.

If the same item has slipped 2+ days in a row, flag it. Not a judgment — a signal.

### Step 4 — Waiting-for shifts

- Any waiting-for that landed today: what did the user receive, is it actionable now.
- Any waiting-for that shifted: new expected-back date.
- Any waiting-for the user nudged today: what they said, when to re-nudge.

### Step 5 — One signal for the weekly review

One sentence naming something about today worth tracking into the weekly review. Categories:
- A pattern ("third time this week a 30-minute meeting became 60").
- A surprise ("X took way longer than expected").
- A friction point ("still can't find the right doc quickly").
- A small win worth repeating.

One signal. Not five. The weekly review is where signals get weighed — the daily close just catches them while they're fresh.

---

## Constraints

### Must
- Compare against the actual morning plan, not a reconstructed-after-the-fact plan.
- Produce a reload-context paragraph every day.
- Keep slippage entries specific (what displaced, not "got busy").
- Produce exactly one signal for the weekly review.
- Keep the whole output to one screen.

### Must Not
- Grade the day ("great day," "bad day," "mediocre day").
- Turn into a task list for tomorrow. Tomorrow's list is a separate exercise.
- Re-plan the week at end of day.
- Pad slippage reasons with generalizations.
- Invent wins or losses that weren't in the day's actual activity.

---

## False-Positive Prevention

1. **Don't smooth over a missed ship item.** "Didn't quite get to the proposal" is less useful than "proposal slipped; displaced by the 3pm that ran 45 min long."
2. **Don't let reload-context become a status report to nobody.** Write it for the user's morning self — specific, not formal.
3. **Don't convert every slippage into an action.** Some slippages just happened and need no action. Say so.
4. **Don't skip signals to look productive.** The most valuable days often produce the most interesting signals (a meeting that went unexpectedly well, a tool that saved an hour).
5. **If the day genuinely had no plan,** say so and run the reduced version. Inventing a retrospective plan makes tomorrow's briefing worse.

---

## Output Format

```
# End-of-day — [date]

## Reconciliation
- Ship item: [shipped / partial / displaced by X / not started]
- Meetings: [as planned / +N added / -N cancelled / N ran long]
- Commitments due today: [delivered / late / renegotiated]

## Reload context (for tomorrow morning, 2-min read)
[4-line paragraph: where the work is, last step taken, first move tomorrow, open questions.]

## Slippage
- [Item] — displaced by [specific]. Disposition: [reschedule / renegotiate / drop].
  [Flag if slipped 2+ days.]

## Waiting-for shifts
- Landed: [what, actionable now?]
- Shifted: [new expected-back]
- Nudged: [whom, what said, re-nudge on]

## One signal for weekly review
[One sentence — pattern / surprise / friction / small win.]
```

---

## Verification

- [ ] Reconciliation compares to the actual morning plan, not reconstructed.
- [ ] Reload context is 4 lines and concrete.
- [ ] Slippage reasons are specific, not generic.
- [ ] Exactly one signal is named.
- [ ] No grading language.
- [ ] Output fits on one screen.
