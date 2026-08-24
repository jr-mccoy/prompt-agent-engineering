---
title: "Ending Therapy Conversation Planner (Client-Side)"
category: psychology/client-self-use/session-prep-integration
description: "Help a client plan the conversation about ending therapy — whether because the work is complete, because of fit, finances, life change, or because they want a break."
techniques:
  - ST-04
  - DT-02
  - NE-07
  - RP-04
difficulty: intermediate
tags:
  - client-self-use
  - termination-from-clients-side
  - ending-therapy
  - planned-ending
intended_use: model-testing
updated: "2026-05-08"
---

# Ending Therapy Conversation Planner (Client-Side)

## Objective

Help a client plan how to bring up ending therapy — whether the ending is "we're done" or "I need a break" or "this isn't fit." Output should:

1. Clarify the type of ending the client is contemplating (complete / pause / switch).
2. Surface what's driving the decision and check it's not avoidance of a hard topic.
3. Generate the script for raising it.
4. Plan for what the client wants the ending itself to do (closure, summary, future-self letter, no formal ending).

## When to Use

- Considering ending after meeting initial goals.
- Wanting to take a break (cost, life change, capacity).
- Considering switching to a different therapist.
- Wanting to move from weekly to monthly or as-needed.
- Stuck and unsure if to push through or step away.

## Inputs / Context

- Type of ending considering: complete / pause / switch / step-down to lower frequency.
- What's driving it: gains achieved / cost / time / mismatch / avoidance / life change.
- How long in therapy with this clinician.
- Whether the client has talked about endings with this therapist before.
- What the client wants the last session(s) to do.

## Constraints

### Must

- Output sections in order: **Type of Ending I'm Considering**, **What's Driving This (honest check)**, **Avoidance Check**, **The Conversation Script**, **What I Want the Last Session(s) to Do**, **Door I Want Left Open**.
- The Avoidance Check explicitly asks: is this an ending or am I bouncing off something hard? Both can be true; the client should know which.
- Plan for therapist response: agreement, request for an arc to ending, exploration of avoidance.
- Distinguish endings that need 1 session from those that benefit from 2–4 closing sessions.
- Address how to handle the door being open (return, periodic check-ins, none).

### Must Not

- Don't talk the client into staying or leaving.
- Don't pathologize wanting to end.
- Don't promise the therapist won't push back (some will, sometimes appropriately).
- Don't override the client's decision; reflect it back accurately.

## Instructions

1. Clarify type of ending.
2. Check the driving reason — is it gains, fit, finances, life, or avoidance?
3. Run avoidance check explicitly.
4. Generate the script.
5. Plan the arc — how many sessions, what each is for.
6. Address the door-open question.

## Output Format

```
=== ENDING THERAPY — PLANNING THE CONVERSATION ===

Type of Ending I'm Considering:
- [Complete (work feels done) / Pause / Switch to a different therapist / Step-down to lower frequency]

What's Driving This (honest):
- Primary: [Gains / cost / time / fit / life change / avoidance]
- Secondary: [...]

Avoidance Check:
- Is there a topic I've been bouncing off that this ending would let me avoid?
   - [Yes — the topic is: ... / No — the work feels at a natural pause / Mixed]
- If Yes: am I willing to bring that topic to one more session before deciding?
   - [Yes / No / Not sure]
- If I bring it and the ending still feels right after, that's okay; I'm checking, not interrogating myself.

The Conversation Script:
"I want to talk about ending [or pausing / stepping down / switching]. What's bringing it up for me is [reason]. I'm thinking [proposed shape: 'this would be our last session,' or 'a few more sessions to wrap up,' or 'a 3-month pause and then check in']. Before we land on that, I want to hear your read."

What I Want the Last Session(s) to Do:
- [Summary of what we worked on]
- [A future-self letter or written summary]
- [Naming what's unfinished and what I'll do with it]
- [Just a clean ending; I don't need formal closure]
- [Nothing — this is the last one]

Number of sessions to wrap up: [1 / 2–4 / Open]

Door I Want Left Open:
- Return anytime: [Yes / No]
- Check-in in [N months]: [Yes / No]
- Refer me out if I want a different fit later: [Yes / No]
- I want a clean break: [Yes / No]

If Therapist Pushes Back:
- I'll listen to what they're seeing.
- I'll separate "they're picking up something I'm avoiding" from "they want to keep me as a client."
- I can hold both: I appreciate the input AND I am the one who decides.
- If they suggest a few more sessions before final ending: that's often reasonable and I can agree without it meaning I changed my mind about ending.
```

## Verification

- [ ] Ending type explicitly chosen.
- [ ] Driving reason named honestly.
- [ ] Avoidance check run, with willingness-to-explore answered.
- [ ] Script names the proposal and invites the therapist's read.
- [ ] Arc to ending planned (single session vs multi).
- [ ] Door-open question answered explicitly.
- [ ] Pushback plan separates legitimate exploration from over-holding.
- [ ] No talking-into or talking-out-of.
