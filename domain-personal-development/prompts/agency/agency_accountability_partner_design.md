---
title: "Design an Accountability Structure Matched to What the User Responds To"
category: personal-development/agency
description: "Pick the one accountability mechanism — partner, cadence, stakes, and commitment format — that fits the user's actual track record of what makes them follow through, then produce the exact first message to set it up today."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - agency
  - accountability
  - follow-through
  - commitment
  - forcing-function
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/agency/agency_ship_sprint_design.md
  - domain-personal-development/prompts/agency/agency_habit_loop_repair.md
  - domain-personal-development/prompts/agency/agency_weekly_review.md
  - domain-personal-development/prompts/goals/goals_goal_setting_and_reflection_loop.md
  - domain-productivity/bottlenecks/bottleneck_procrastination_systems_diagnostic.md
---

# Design an Accountability Structure Matched to What the User Responds To

**Objective:** Given a commitment the user keeps failing to keep alone, pick exactly one accountability mechanism — matched to the user's own history of what actually made them follow through — and produce the fully specified structure plus the exact first message to send today.

**When to use:** The user has a real commitment (ship a thing, keep a habit, hit a milestone) that they repeatedly plan and repeatedly drop when only they are watching. Also useful when a past accountability setup fizzled and they want to know why. Not for team accountability, and not for holding someone else accountable — this is the user arranging a structure over their own behavior.

**Audience:** An individual arranging accountability over their own work. Not for a manager tracking reports, not for a coach managing a client. If the failure to follow through is tied to persistent low mood, hopelessness, or shutdown rather than structure, that is not an accountability problem — see `domain-psychology/` and a licensed professional.

---

## Inputs Required

1. **The commitment.** What the user wants to be held to, stated as an observable end-state ("the second chapter is drafted," not "make progress on the book").
2. **Track record of past commitments — kept and broken.** 4–8 real cases where the user committed to something and either did or didn't follow through. For each: *what the commitment was, who else knew, what (if anything) was at stake, kept or broken.* Trivial cases (showed up to a paid appointment) don't count.
3. **Past accountability attempts.** Any prior partner, app, group, or stake the user has used, and whether it worked or fizzled — and their honest guess at why.
4. **Available people.** Who in the user's life could plausibly play a role, and how reliable each is at their own commitments.
5. **What the user can actually put at stake.** Money they'd genuinely miss, a reputation that matters to them, a relationship whose regard they don't want to lose.

If input 2 has fewer than 4 real cases, refuse and ask for more. A structure matched to nothing is a guess.

---

## Instructions

### Step 1 — Identify the response driver from the track record

Read input 2 for the pattern: across the *kept* commitments, what was present that was absent in the broken ones? Classify into exactly one primary **response driver** from this fixed taxonomy:

| # | Response driver | Signature in the track record |
|---|---|---|
| 1 | **Social visibility** | Kept commitments were ones another specific person knew about and would notice. |
| 2 | **Loss aversion** | Kept commitments had a concrete cost attached; broken ones were "free" to drop. |
| 3 | **Peer belonging** | Followed through inside a group of people doing the same thing; drifted when solo. |
| 4 | **External structure** | Kept commitments had a fixed time/place/appointment; broke the open-ended ones. |
| 5 | **Reputation stake** | Delivered when a named audience's regard was on the line; skipped private ones. |
| 6 | **No driver found yet** | Kept and broken cases look the same — nothing external distinguished them. |

Cite the specific cases that support the pick. If two drivers tie, name both and rank by which appeared in more kept cases.

### Step 2 — Map the driver to one mechanism

Use this fixed mapping. Pick the mechanism for the primary driver.

| Response driver | Mechanism |
|---|---|
| Social visibility | **Deadline witness** — one named person who holds the deadline and will ask on the date. |
| Loss aversion | **Financial stake** — money the user forfeits (to a person, a bet, or a cause they dislike) on a miss. |
| Peer belonging | **Cohort / co-working** — a small group or recurring body-double session doing parallel work. |
| External structure | **Fixed cadence check-in** — a standing call/message at a set time the user does not reschedule. |
| Reputation stake | **Public commitment** — the commitment posted where the audience the user cares about will see the outcome. |
| No driver found yet | **Instrumented default** — start with a fixed cadence check-in *plus* a small financial stake, and run it for two cycles to generate the missing evidence. |

Do not blend mechanisms beyond what the mapping specifies. One primary mechanism.

### Step 3 — Choose the concrete partner or instrument

From input 4/5, name the actual person, group, or instrument. Apply the **stake-has-bite test**: the partner must themselves be reliable (they won't forget to check), and the stake must be one the user would genuinely feel. Reject a partner who is flaky or a stake that is painless, and pick the next candidate. If no candidate passes, say so and name what the user must arrange first.

### Step 4 — Specify cadence, stake size, and commitment format

- **Cadence:** matched to the work's real rhythm, not tighter. Daily check-ins on weekly-cadence work will be ignored within a week.
- **Stake (if the mechanism uses one):** large enough to feel, small enough to actually pay. Name the exact amount or consequence and who enforces it.
- **Commitment format:** a single sentence in the checkable form *"By [date/time], [named artifact] exists / [observable state] is true."* No "make progress," no "work on."

### Step 5 — Define the miss protocol

State up front what happens on a missed check: the stake is paid (no renegotiation), the partner is told the real reason (not a cover story), and the next commitment is re-cut smaller if the miss was a scope problem. A structure with no consequence on a miss is encouragement, not accountability.

### Step 6 — Produce the exact first message

Write the verbatim message the user sends to the partner (or the exact action to set up the instrument) today. It must name the commitment, the cadence, the stake, and what the user is asking the partner to actually do. This is the one decisive move.

---

## Constraints

### Must
- Pick exactly one response driver, cited to specific track-record cases.
- Map to exactly one primary mechanism using the fixed table.
- Name a concrete partner/instrument that passes the stake-has-bite test.
- State the commitment in checkable *"by [date], [artifact] exists"* form.
- Produce a verbatim first message the user can send today.

### Must Not
- Recommend a partner who is themselves unreliable at their own commitments.
- Treat encouragement or cheerleading as accountability — consequence is the point.
- Propose financial stakes for a user with clear money-comfort (no bite).
- Blend three mechanisms into a complex system the user won't maintain.
- Moralize about the user's past broken commitments or use motivational language.

---

## False-Positive Prevention

1. **Don't confuse a cheerleader with a witness.** A friend who says "you've got this" applies no consequence. Accountability requires someone who will note a miss, not soothe it.
2. **Don't default to financial stakes.** They only work under a loss-aversion driver with money the user would actually miss. For a comfortable user, a reputation or relationship stake bites harder.
3. **Don't pick a flaky partner because they're available.** If the named person forgets their own deadlines, they will forget to check yours. Reliability of the partner is a hard filter.
4. **Don't over-tighten cadence.** Daily accountability on work that genuinely moves weekly produces noise and then abandonment. Match the check to the work's real rhythm.
5. **Don't recommend a group if the user hides in groups.** If the track record shows the user goes quiet inside cohorts, a group adds cover, not pressure — use a one-to-one witness instead.
6. **Don't mistake a motivation problem for a structure problem.** If the user doesn't want the outcome (loss of why), no accountability structure will hold — route to `agency_stuck_diagnosis.md` category 12 first.

---

## Output Format

```
## Response driver
**Primary:** [# + name from taxonomy]
**Evidence:** [specific kept vs. broken cases from the track record]
**Secondary (if any):** [driver + why ranked second, or "none"]

## Mechanism
[Mechanism name from the mapping table.]

## Concrete setup
- Partner / instrument: [named, with one line on why it passes the stake-has-bite test]
- Cadence: [when the check happens, matched to work rhythm]
- Stake: [exact amount / consequence + who enforces, or "none — mechanism is visibility-based"]
- Commitment format: "By [date/time], [named artifact] exists."

## Miss protocol
On a missed check: [stake paid / real reason told / re-cut rule]. No renegotiation.

## First message to send today
> [Verbatim message to the partner, or exact instrument-setup action.]

## Predicted check
If this fits the user's driver, the first scheduled check will find [named artifact] exists. If the first two checks are missed with the stake paid and still no artifact, the driver was misread — re-run this prompt.
```

---

## Verification

- [ ] Exactly one response driver chosen, cited to specific track-record cases.
- [ ] Mechanism follows the fixed mapping, not a freehand blend.
- [ ] The named partner/instrument passes the stake-has-bite test.
- [ ] Commitment is in checkable *"by [date], [artifact] exists"* form.
- [ ] A miss protocol with a real consequence is stated.
- [ ] A verbatim, send-today first message is produced.
- [ ] No cheerleading, no moralizing about past misses.
