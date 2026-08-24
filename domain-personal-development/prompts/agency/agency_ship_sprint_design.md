---
title: "Design a Ship-Within-a-Short-Window Exercise"
category: personal-development/agency
description: "Design a 2–10 day sprint where the user ships something substantial and real to an external audience, with bounded scope, forced deadline, and a definition of done that survives contact with reality."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - agency
  - ship
  - sprint
  - constrained-execution
  - forcing-function
updated: "2026-04-20"
related_prompts:
  - domain-personal-development/prompts/agency/agency_project_ownership_converter.md
  - domain-personal-development/prompts/agency/agency_foundation_session.md
  - domain-personal-development/prompts/agency/agency_end_of_session_review.md
---

# Design a Ship-Within-a-Short-Window Exercise

**Objective:** Design a time-boxed exercise — somewhere between a long weekend and two weeks — in which the user ships a real deliverable to a real external audience. Not a draft for themselves. Not a "soft launch to friends." Something a stranger could find and react to.

**When to use:** The user has been working on a project for months and has not shipped anything external. Or: they want to break a stall by forcing a real deadline. Or: they want to build the muscle of finishing by practicing finishing at small scale.

**Audience:** An individual with a bounded calendar block they can protect (a weekend, a vacation week, a designated evening-block of a work week). Not a team working together. Not an employee whose manager sets their scope.

---

## Inputs Required

1. **The project context.** What domain (writing, code, video, design, research, a pitch, a workshop, a product), and what the user has been working on generally.
2. **The calendar window.** Start date, end date, and realistic hours-per-day inside that window.
3. **Constraints.** Family, job, travel, anything that eats hours from the nominal window.
4. **What the user has available to work with today.** Existing drafts, code, notes, audience, skills. No assumption of net-new learning during the window.
5. **What "shipped" has to mean in their domain.** Published where? Visible to whom? This is the user's definition; if they don't have one, help them pick one.

If the calendar window is shorter than 2 focused days or longer than 10 focused days, flag and resize before designing.

---

## Instructions

### Step 1 — Size the deliverable to the window

The deliverable must be one that:

- Can be finished inside the window using only what the user already knows and has. No planning for skill acquisition during the sprint.
- Is a full, recognizable artifact in its domain. A short essay, not "research." A small working app, not "a prototype of a framework." A 10-minute talk, not "an outline."
- Is one deliverable. Not three. If the user is tempted to ship three small things, they'll ship zero. Pick one.

Rewrite the user's first instinct if it doesn't pass these tests. Draft an alternative that does.

### Step 2 — Define "shipped" in domain-specific terms

"Shipped" means the deliverable is in a place where a person the user does not personally know could encounter it. Concretely:

- **Writing:** published on a public URL. Not a Google Doc shared with a friend.
- **Code:** deployed somewhere accessible, or published to a public repo with a README that explains the thing, and submitted to at least one place it could get seen.
- **Video/audio:** uploaded to a public platform.
- **Pitch/talk:** delivered to a real audience, not a dry-run.
- **Design/product:** posted to a public portfolio or marketplace, or put in front of real potential users.

If the user's domain makes this hard, name the closest equivalent and why.

### Step 3 — Budget the window backwards

Break the window into three phases, with the end-state for each:

- **Phase 1 — Lock-in (first 10–20% of the window).** End-state: full scope decision made, cannot be renegotiated. What's in, what's out.
- **Phase 2 — Build (middle 60–70%).** End-state: a complete, rough, end-to-end draft or build. Ugly is fine. Incomplete is not.
- **Phase 3 — Finish-and-ship (last 15–20%).** End-state: the thing is in the public place. Finishing and shipping are the activity of this phase; no new scope enters.

State the specific calendar hours for each phase. Include a hard cutoff before the end of the window for "no new scope" — typically at the 70% mark.

### Step 4 — Define the minimum viable success

The exercise's purpose is shipping, not perfection. Define two levels:

- **Ship floor:** The minimum the artifact must contain or do to count as shipped. If a real phase-3 bug forces cutting scope, cut to the floor, not below.
- **Ship target:** What the user is actually aiming for. Between floor and target, the user chooses based on remaining hours.

If the floor and target collapse to the same thing, the floor is too high — redefine.

### Step 5 — Anti-avoidance pre-commitments

Name, up front, the three moves most likely to derail the sprint for this user and a pre-decided response to each:

- **Scope creep** ("it would be better if it also…") → response: write it in a "next version" doc, do not add to this sprint.
- **Polish-as-escape** (rewriting the intro for the fifth time on day 6) → response: at the 70% cutoff, no more new scope; only finishing-existing-scope is allowed.
- **Emergency research** ("I need to learn X to do this") → response: if X wasn't required at lock-in, it isn't required now; fake-it or cut-scope.

If the user has a known derailment pattern not on this list, include a specific pre-commitment for it.

### Step 6 — Define post-ship

Name what the user does in the 24 hours after shipping: (a) confirm the thing is in fact in the public place (b) announce it to one real recipient (c) write one page of what they learned about finishing (see `agency_end_of_session_review.md`). Nothing else.

---

## Constraints

### Must
- Produce exactly one deliverable for the sprint.
- Size the deliverable so it fits the available hours, not the nominal days.
- Define "shipped" in domain-specific, publicly-observable terms.
- Set a no-new-scope cutoff inside the window.
- Define ship floor and ship target separately.

### Must Not
- Recommend sprints shorter than 2 focused days or longer than 10.
- Require learning new skills during the sprint.
- Allow "ship to a private circle of friends" as the ship definition.
- Allow three small deliverables in place of one real one.
- Suggest the sprint is about productivity or self-optimization. It's about finishing.

---

## False-Positive Prevention

1. **Don't design a sprint the user cannot actually protect.** If the "window" contains two family obligations and a travel day, factor those in at input time.
2. **Don't set a fake deadline.** External commitment (a posted date, a registered event, a published schedule) matters more than a private deadline. Recommend creating one where the user can.
3. **Don't let ship-floor collapse to target.** They must be different; floor is what allows finishing under pressure.
4. **Don't schedule perfectionism as "final polish."** Polish is bounded by the remaining hours, not by quality wishes.
5. **Don't celebrate in advance.** The prompt ends before the sprint begins.

---

## Output Format

```
# Ship Sprint: [Project / deliverable name]

## Deliverable
[One sentence naming the single artifact.]

## "Shipped" means
[Domain-specific definition: where it lives, who can encounter it.]

## Window
Start: [date/time]
End: [date/time]
Realistic work hours inside the window: [N]

## Phases
- Lock-in — [calendar dates, hours]
  End-state: [full scope locked]
- Build — [calendar dates, hours]
  End-state: [complete rough end-to-end version]
- Finish-and-ship — [calendar dates, hours]
  End-state: [in the public place]

## No-new-scope cutoff
[Specific date/time at ~70% of the window]

## Ship floor (minimum to count as shipped)
- [Specific element]
- [Specific element]

## Ship target (aiming for)
- [Specific element]
- [Specific element]

## Pre-committed responses to derailers
- Scope creep → [response]
- Polish-as-escape → [response]
- Emergency research → [response]
- [User-specific derailer] → [response]

## Post-ship (first 24 hours)
1. Confirm public visibility.
2. Announce to [named recipient].
3. Write one page: [link to end-of-session review prompt].

## Flags
[Any constraint that suggests the window is too short, too crowded, or the deliverable is too large.]
```

---

## Verification

- [ ] Deliverable is one artifact, not multiple.
- [ ] "Shipped" is defined in a way a stranger could verify.
- [ ] Hours are sized to the window after family/job subtraction.
- [ ] Ship floor and ship target are clearly different.
- [ ] The no-new-scope cutoff is named with a specific date/time.
- [ ] Pre-committed responses cover the user's known derailment patterns.
- [ ] No language suggesting the sprint is "about productivity."
