---
title: "Engineer Defaults and Friction in the Workspace"
category: productivity/deep-work
description: "Audit the user's physical and digital workspace for default-actions and friction-points; propose specific add/remove changes that change the easy-path so behavior follows defaults rather than discipline."
techniques:
  - ST-01
  - ST-02
  - DS-26
  - RT-02
  - NE-22
difficulty: beginner
tags:
  - environment
  - defaults
  - friction
  - deep-work
  - behavior-design
updated: "2026-05-08"
related_prompts:
  - domain-productivity/deep-work/deepwork_calendar_audit.md
  - domain-productivity/bottlenecks/bottleneck_capture_triage_system_design.md
  - domain-productivity/bottlenecks/bottleneck_procrastination_systems_diagnostic.md
  - domain-productivity/deep-work/deepwork_self_interruption_audit.md
  - domain-productivity/deep-work/deepwork_message_triage_system.md
---

# Engineer Defaults and Friction in the Workspace

**Objective:** Audit the user's physical and digital workspace for what is currently the *easy-path* (the default behavior) and the *friction-path* (what requires deliberate effort), then prescribe a small set of specific add-friction / remove-friction changes that flip the defaults toward the work the user wants to do.

**When to use:** The user notices a gap between what they intend to do and what they end up doing — picking up the phone "for one second," opening Slack on autopilot, getting derailed by notifications, or finding it consistently easier to do the wrong thing than the right one. Run this when the diagnosis is environment-shaped, not motivation-shaped.

**Audience:** An individual designing their own workspace. Single-user. Not a corporate office redesign.

---

## Inputs Required

1. **Where the user works.** Physical: home office, kitchen table, coworking, varies. Digital: which devices, OS, browsers, primary apps.
2. **The intended work.** What the user wants the environment to support — focused work blocks, async writing, code, learning, calls. One to three categories.
3. **What actually keeps happening instead.** The off-default behaviors: 5–10 specific instances of getting pulled into something else. Be granular: "opened phone, scrolled Twitter for 15 min, was supposed to be writing." Not "I get distracted."
4. **Notification and inbox state.** Honest snapshot: which apps notify, on which devices, at what hours. Lock screen visible? Phone face-up on desk? Do-not-disturb default?
5. **Browser and tab state.** Default browser homepage, pinned tabs, currently-open tab count, which sites auto-login.
6. **Phone state.** Home-screen apps, what's on first screen, which apps have one-tap access from lock.
7. **Physical surface state.** What's within arm's reach of the work seat. Visible decision-points (snacks, the TV remote, a guitar, mail).
8. **One change the user has already tried that didn't stick.** Useful diagnostic — failed changes usually fail because they added discipline-cost rather than removing or adding friction.

If input 3 is < 3 specific instances, ask for more — the prompt designs against specific behaviors, not vague "distraction."

---

## Instructions

### Step 1 — Map current defaults vs. friction paths

For each of the off-default behaviors in input 3, name **what made it the easy path**. Use this audit table:

| Off-default behavior | Easy-path mechanism | Friction on the intended path |
|---|---|---|
| Opened phone, scrolled | Phone face-up on desk, lock screen has notifications, primary app on first screen | Writing app required: open laptop, open file, scroll up to where I left off |

The friction column is often the more useful column. The intended path frequently has hidden friction the user has stopped noticing.

### Step 2 — Apply the four-move framework

Every change is one of four moves. State which move applies for each behavior. (NE-22 constraint inversion in practice.)

| Move | Description | Example |
|---|---|---|
| **Add friction to the wrong path** | Make the off-default behavior take more steps. | Phone in another room. Twitter blocked at the network level on the work device. Slack signed out at end of day. |
| **Remove friction from the right path** | Make the intended behavior take fewer steps. | Writing app pinned, file open, cursor on last line. Terminal pre-staged with the right working directory. |
| **Change the default state** | The action that requires *no* deliberate choice is the right one. | Browser home page is your work doc, not a feed. New-tab page is blank or the doc you're writing. DND on by default; you toggle it off to be reachable, not on to focus. |
| **Reduce decision points** | Remove visible alternatives near the workspace. | Music pre-chosen for the day, queued. Snacks not within arm's reach. Phone charged in another room. |

For each input-3 behavior, propose one move from the four. Specify: which move, what physical / digital change, where it applies.

### Step 3 — Pick the highest-leverage three

Looking at the table from Step 2, pick **at most three** changes to implement first. Prioritize by:

1. Frequency of the off-default behavior (how often does it cost the user time?).
2. Magnitude of the cost (a 30-second hit vs. a 30-minute hit).
3. Reversibility (changes that are easy to back out of are safer to try).

Three changes maximum. The 80/20 of environment design is a small set of well-chosen friction shifts, not a total environment overhaul.

### Step 4 — Address the failed prior change (input 8)

Take input 8 and re-classify it: was it a "Add friction to wrong path" move, "Remove friction from right path," "Change default state," or "Reduce decision points"? Almost all failed environment changes share one of these patterns:

- It added a daily decision rather than changing the default. (User has to choose every morning to enable Focus mode → fails.)
- It increased friction symbolically but kept the easy path one workaround away. (Phone in a drawer next to the desk → no real friction.)
- It removed friction on the wrong work. (Pinned the writing app, but the hard work was actually research, not writing.)

Diagnose the prior failure. Propose the change pattern that would have stuck.

### Step 5 — Define a 14-day check

State what the user should observe over 14 days:

- Off-default behaviors from input 3: count occurrences. Should drop by ≥ 50% if the changes are working.
- Time-to-first-keystroke when starting a planned block: should drop measurably.
- New off-default behaviors: if a Slack-replacement appears (the user was on Twitter, now they're on news), the friction was added but the underlying pull wasn't addressed. Re-run.

If the prompt's predicted drops don't materialize, the diagnosis was probably motivation-shaped, not environment-shaped. Route to `bottleneck_procrastination_systems_diagnostic.md` or personal-development.

### Step 6 — Refuse the maximalist redesign

Close with explicit refusal: this prompt does not produce a digital-minimalism manifesto, a deep-clean of the home, or a 30-step ergonomic redesign. Three changes, 14 days, observe, re-run. The system improves through small reversible moves, not a one-time overhaul.

---

## Constraints

### Must
- Map current defaults / friction for each off-default behavior in input 3.
- Use the four-move framework explicitly.
- Limit prescription to three changes.
- Diagnose the prior failed change (input 8) by classifying its move pattern.
- State a 14-day observable check.

### Must Not
- Prescribe more than three changes.
- Recommend buying new tools, apps, or hardware as the primary intervention. (A USB switcher to swap displays is fine if it removes friction; "buy a standing desk" is not.)
- Frame the work as "build discipline." That's the framing the prompt replaces.
- Recommend rituals or visualizations as the change. The change is structural.
- Recommend a productivity-app subscription that requires daily use to work. (Apps that depend on the user's daily discipline are themselves friction.)

---

## False-Positive Prevention

1. **Don't add friction symbolically.** Phone-in-a-drawer-on-the-desk doesn't work. Phone-in-another-room does. The friction has to be high enough to be the binding constraint.
2. **Don't remove friction from the wrong work.** If the user thinks they're avoiding writing but is actually avoiding research, removing writing-friction won't change behavior. Trace input 3 back to the *actual* avoided work.
3. **Don't recommend "turn off all notifications."** Coarse and unsustainable. Turn off specific notifications on specific channels; keep urgent ones (medical, family) on. Selectivity is the point.
4. **Don't propose a behavior change without a defaults change.** Every behavior change requires a defaults change to stick; otherwise the user is in motivation territory.
5. **Don't add a fourth or fifth change "just in case."** Three. Re-run after 14 days if needed.
6. **Don't blame the environment for everything.** If after two re-runs the off-default behaviors persist with strong friction in place, the diagnosis is upstream — energy, burnout, motivation, or values mismatch. Refer.

---

## Output Format

```
## Defaults / friction map
| Off-default behavior (input 3) | Easy-path mechanism | Friction on intended path |
|---|---|---|
| ... | ... | ... |

## Proposed changes (max 3)
| # | Move | Change | Where it applies | Cost to set up |
|---|---|---|---|---|
| 1 | Add friction / Remove friction / Change default / Reduce decisions | [specific] | [physical/digital location] | [one-time, low/medium] |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |

## Why these three (and not others)
[Brief — frequency, magnitude, reversibility.]

## Prior failed change (input 8) — diagnosis
**Move pattern attempted:** [one of the four]
**Why it didn't stick:** [pattern from Step 4]
**Pattern that would have stuck:** [one alternative]

## 14-day observable check
- Off-default behaviors (count): baseline N → target ≤ N/2
- Time-to-first-keystroke on planned blocks: measurable drop
- Watch for replacement behaviors (off-default shifts to a new app/site)

If observable check fails: the diagnosis was likely motivation-shaped, not environment-shaped. Route to `bottleneck_procrastination_systems_diagnostic.md`.

## What this prompt is not producing
- Not a digital-minimalism overhaul
- Not a recommendation to buy new gear
- Not a "build discipline" plan
- Not more than three changes in one pass
```

---

## Verification

- [ ] Defaults / friction map built from input 3's specific behaviors.
- [ ] Each proposed change uses one of the four moves explicitly.
- [ ] Exactly ≤ 3 changes prescribed.
- [ ] Prior failed change diagnosed by move pattern.
- [ ] 14-day observable check stated with concrete numbers.
- [ ] No "build discipline" framing.
- [ ] No tool / hardware purchase as the primary intervention.
- [ ] Refusal block included.
