---
title: "Daily Accountability Check-in — Scheduled Focus Prompt"
category: productivity/automation
description: "Specify a deterministic scheduled automation that sends a daily focus/accountability prompt to a chosen channel at a chosen local time, with weekend handling, timezone correctness, and a delivery-failure fallback."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - automation
  - accountability
  - scheduling
  - habits
  - focus
updated: "2026-06-07"
related_prompts:
  - domain-productivity/automation/automation_weekly_digest.md
  - domain-productivity/automation/automation_form_notification.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
---

# Daily Accountability Check-in

**Objective:** Specify a simple, deterministic scheduled automation that delivers a daily focus prompt to a chosen channel at a chosen local time — handling timezone, weekends, and delivery failure — so the user starts each day by naming their top priority.

**When to use:**
- Building a morning focus or daily-planning habit.
- Lightweight personal accountability without a separate app.
- Establishing a fixed daily ritual (prompt → reply with priorities).
- A first, low-risk automation to learn a no-code platform.

**When NOT to use:**
- When the message content must change daily based on data — that needs a digest/data step, not a static reminder.
- When you need two-way tracking or analytics of responses (use a dedicated habit/check-in tool).

**Audience:** Individuals setting up a personal scheduled reminder in Zapier, Make, n8n, or a calendar/automation tool.

---

## Inputs / Context

Supply before generating the spec:

1. **Send time** — the local clock time (e.g., 9:00 AM).
2. **Timezone** — your timezone, stated explicitly (avoid relying on platform default = UTC).
3. **Weekends** — include or exclude Saturday/Sunday.
4. **Delivery method** — Slack DM to self, email to self, etc., and the address/channel.
5. **Message content** — the prompt questions you want (or use the default set).
6. **Available integration** — confirm the chosen delivery channel is connected on your platform.

---

## Constraints

### Must
- Schedule in the user's stated **local timezone**, not UTC.
- Honor the weekend include/exclude choice explicitly in the trigger.
- Keep the automation **deterministic** — fixed trigger, fixed message, no AI reasoning at runtime.
- Use only a delivery channel that is actually connected (or flag the gap).
- Define a fallback if delivery fails (retry or alert).

### Must Not
- Assume the platform default timezone matches the user's.
- Add data lookups or branching that the use case doesn't need (keep it one trigger, one action).
- Silently fail — if the message can't send, the user should know.

---

## Instructions

1. **Confirm the delivery channel** is available; flag if it needs connecting.
2. **Define the schedule trigger:** exact local time + explicit timezone + weekend rule.
3. **Define the single action:** send the message to the chosen channel.
4. **Write the message:** a short greeting plus 2–3 priority-naming questions, ending with an instruction to reply.
5. **Define delivery-failure handling:** on send error, retry once, then alert the user via an alternate channel (or log).
6. **Self-check before output.** Confirm: timezone is explicit and local; weekend rule matches the input; exactly one trigger and one action; failure path exists; channel is confirmed. Then emit the spec.

---

## False-Positive Prevention

❌ **DON'T:**
- Leave the timezone as the platform default and assume it's local.
- Add unnecessary AI/data steps that make a simple reminder fragile.
- Assume the Slack/email integration is authorized.
- Ignore what happens when delivery fails.
- Schedule for weekends when the user wanted weekdays only (or vice versa).

✅ **DO:**
- State the timezone explicitly and test that the fire time is local.
- Keep it to one trigger + one action (deterministic).
- Confirm the delivery channel is connected, or flag it.
- Add a retry-then-alert fallback on send failure.
- Run the platform's "test trigger" before going live.

---

## Output Format

```
AUTOMATION: Daily Focus Check-in
INTEGRATION REQUIRED: [Slack | Email] — [confirmed / NEEDS SETUP]

TRIGGER — Schedule
- Time: [HH:MM] local
- Timezone: [explicit timezone]
- Weekends: [include | exclude]

ACTION — Send message
- Channel: [Slack DM to self | email to <address>]
- Subject/Title: [...]
- Body:
  [greeting + 2–3 priority questions + "reply with your answers"]

FAILURE HANDLING
- On send error: retry once after [interval]; if still failing, alert via [alternate channel] / log

TESTING CHECKLIST
- [ ] ...

NOTES
- Deterministic: fixed trigger + fixed message, no runtime reasoning.
```

---

## Example Output

```
AUTOMATION: Daily Focus Check-in
INTEGRATION REQUIRED: Slack — CONFIRMED (Slack app connected, can DM self)

TRIGGER — Schedule
- Time: 09:00 local
- Timezone: America/Chicago
- Weekends: exclude (Mon–Fri only)

ACTION — Send Slack DM to self
- Subject/Title: "🎯 Daily Focus Check"
- Body:
  "Good morning.

   What's the one thing you must complete today?

   Take 2 minutes:
   1. My #1 priority today is: _____
   2. If I accomplish nothing else, I need to: _____
   3. The biggest obstacle in my way is: _____

   Reply to this message with your answers. Let's make today count."

FAILURE HANDLING
- On Slack send error: retry once after 5 min.
- If still failing: send fallback email to self ("Daily check-in failed to post to Slack") so the ritual isn't silently skipped.

TESTING CHECKLIST
- [ ] Trigger fires at 09:00 America/Chicago, not 09:00 UTC
- [ ] DM arrives in the correct Slack conversation
- [ ] No message sent on Saturday/Sunday
- [ ] "Test trigger" run succeeds before enabling
- [ ] Simulated send failure triggers the email fallback

NOTES
- Deterministic: one schedule trigger, one send action, static message body.
- If this holds for ~5 days, consider adding an end-of-day review message.
```

---

## Verification

- [ ] Schedule uses an explicit local timezone, not UTC.
- [ ] Weekend include/exclude matches the input.
- [ ] Exactly one trigger and one action (deterministic).
- [ ] Delivery channel is confirmed available or flagged.
- [ ] A retry-then-alert failure path is defined.
- [ ] Message contains a greeting + priority questions + reply instruction.
- [ ] Testing checklist verifies local fire time and weekend behavior.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** States the single purpose — a daily local-time focus prompt — so the build stays minimal and deterministic.
- **ST-03 (Output Format Specification):** Fixes the trigger/action/failure/test layout into a copy-ready spec.
- **CM-02 (Constraint Specification):** Encodes the determinism, timezone, weekend, and single-action constraints as explicit Must/Must-Not rules.
- **QA-01 (Self-Verification):** A pre-output check confirms timezone correctness, weekend rule, and failure handling before emitting.

---

## Related Prompts

- `domain-productivity/automation/automation_weekly_digest.md` — Scheduled summary instead of a static daily prompt.
- `domain-productivity/automation/automation_form_notification.md` — Event-triggered notification pattern.
- `domain-personal-development/prompts/agency/agency_next_action_spec.md` — Turn the check-in answers into a concrete next action.
