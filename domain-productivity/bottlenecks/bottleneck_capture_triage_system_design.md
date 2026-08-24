---
title: "Design a Personal Capture-and-Triage System That Survives a Month"
category: productivity/bottlenecks
description: "Given the user's current inputs (ideas, todos, links, requests) and channels, design a capture/triage system spec — inbox shape, triage cadence, decision rules — sized to actual volume and verified by a 30-day survival test."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - DS-29
  - QA-19
difficulty: intermediate
tags:
  - capture
  - triage
  - inbox
  - todo-system
  - personal-productivity
updated: "2026-05-08"
related_prompts:
  - domain-productivity/deep-work/deepwork_message_triage_system.md
  - domain-productivity/deep-work/deepwork_environment_friction_design.md
  - domain-productivity/bottlenecks/bottleneck_pkm_second_brain_architecture.md
  - domain-productivity/bottlenecks/bottleneck_locator.md
  - domain-productivity/reviews/reviews_weekly_systems_review.md
---

# Design a Personal Capture-and-Triage System That Survives a Month

**Objective:** Architect a personal capture-and-triage system that fits the user's actual input volume, channel mix, and processing tolerance — not an aspirational system. Output the system spec, the daily/weekly cadence, the decision rules, and a 30-day survival test that will tell the user whether the system is working.

**When to use:** The user has multiple inboxes, scattered todos, captured links/notes that never get processed, and a sense of low-grade leakage — things slipping, decisions deferred, ideas lost. Often surfaces from `bottleneck_locator.md` execution-side or from a `reviews_time_audit_evidence_based.md` showing async/triage absorbing more time than expected.

**Audience:** An individual designing their own system. Not a team workflow. Not a generic "Getting Things Done" implementation guide — the prompt explicitly refuses framework worship.

---

## Inputs Required

1. **Current capture surfaces.** Where ideas, todos, links, and requests currently land. Be exhaustive: email, Slack, text messages, sticky notes, voice memos, task apps, browser tabs, screenshots, journal, "memory."
2. **Daily input volume estimate.** Rough count per day across all surfaces — emails, messages, requests, captured links/notes. If unknown, ask the user to count for one day.
3. **Categories of input.** What types of things show up: actionable requests (from others), self-generated todos, ideas/research links, reference material to keep, messages requiring response, calendar invites, financial/admin items.
4. **Current processing rituals.** Does the user have a triage time today? When? How long? What gets touched during it?
5. **Recent leak examples.** 3–5 specific things that fell through the cracks in the last 30 days — what they were, where they should have been captured, where they actually were when they got lost.
6. **Tolerance for system overhead.** Honest answer: how many minutes/day will the user actually spend on capture-and-triage? Cap at 30 minutes/day for individuals; if the user says more, push back — most personal systems collapse above that threshold.
7. **Tools they will actually use vs. tools they have.** Some users own 7 task apps and use one. List both.

If input 5 is "nothing has fallen through" *and* the user is asking for a system anyway, ask why. The system may not be needed; the user may be optimizing prematurely.

---

## Instructions

### Step 1 — Establish the system's design constraints

Before designing, name the constraints from inputs 2 and 6:

- **Daily input volume:** [N items / day across all surfaces]
- **Daily triage budget:** [M minutes / day]
- **Per-item triage time:** ≈ M / N minutes per item — typically should be ≤ 60 seconds for triage to be sustainable.

If per-item triage time is < 20 seconds, the system needs *capture filtering* before triage (not everything that arrives needs to be captured). If it's > 90 seconds, the system needs to be *coarser* (fewer categories, simpler decision rules).

State the per-item triage budget explicitly. The system follows from this constraint.

### Step 2 — Choose an inbox topology

Output one of these three patterns based on input 1's surface count and input 3's category mix:

- **Single-funnel.** All capture surfaces feed into one inbox. Triage in that one place. Best when: the user has < 3 surfaces or when category-mixing is not a problem.
- **Two-funnel.** Separate "people inbox" (messages from others) and "self inbox" (todos, ideas, captures). Triage cadences differ. Best when: messages and self-captures are roughly equal volume.
- **Channel-native.** Multiple inboxes, but with a *manifest* file the user reviews once per day pointing to each. Best when: the volume in any single funnel would exceed the daily triage budget.

Do not invent a fourth topology. Pick one. State why.

### Step 3 — Define the triage decision rules

Each captured item must resolve to *exactly one* of these outcomes within triage. No "I'll think about it later" — that's the leak path.

| Outcome | Rule | Action |
|---|---|---|
| **Do** | < 2 minutes, must be done, no context switch cost | Do it now in triage. |
| **Schedule** | Specific work, > 2 minutes, has a clear next physical action | Calendar block or task with date + next action. |
| **Defer-with-trigger** | Action requires a future event/decision/dependency | Capture with the trigger condition; route to a "waiting" list, not the inbox. |
| **Reference** | Information to keep, no action | Move to reference store (see `bottleneck_pkm_second_brain_architecture.md`). |
| **Drop** | Doesn't survive triage | Delete. Most users underuse this outcome — flag explicitly. |
| **Question-back** | Cannot decide which outcome without more info | Ask one specific question of the source; track the question, not the item. |

The decision rule for each item is one sentence. If the user can't decide in a sentence, the item gets a question-back, not a longer triage attempt.

### Step 4 — Define the cadence

Three cadences, each with a specific time and budget:

- **Inline capture (continuous):** the action of getting things *into* the inbox(es). Goal: under 5 seconds per capture, no triage during capture. State the specific mechanism per surface (e.g., "voice memo button → end-of-day batch transcribe," "email star → batch process," "sticky note → photographed at end of day").
- **Daily triage block (one or two times):** the only place items leave inboxes. State exact time and duration. Default: one 15–25 min block, daily. Two blocks max.
- **Weekly system maintenance (one time):** review the deferred-with-trigger list, the reference store entries from this week, and the calendar/task list for the next week. 30–45 min. Routes to `reviews_weekly_systems_review.md`.

The cadence must fit the user's stated triage budget (input 6). If it doesn't, scope down — fewer surfaces, coarser categories, more aggressive Drop rule.

### Step 5 — Address the documented leaks (input 5)

For each leak in input 5, state which surface/cadence/rule it would have caught in the new system:

- "Lost-link example: would have been captured into self-inbox via [browser bookmark to inbox folder]; triaged in daily block to Reference."
- "Forgotten request: would have been captured into people-inbox; triaged to Schedule with date or Defer-with-trigger."

If a leak example *wouldn't* have been caught, the system has a known gap — name the gap and either fix it or explicitly accept it.

### Step 6 — Specify the 30-day survival test

The system has succeeded if, at day 30:

- Daily triage block was held on ≥ 22 of 30 days.
- Both inboxes hit zero (or near-zero) on ≥ 22 days.
- ≤ 1 documented leak per week (compared to input 5's baseline).
- The user did not adopt new tools mid-month to "fix" the system.

State these as numeric checks. State that re-running this prompt at day 30 with new leak data is the right move if the system fails the test.

### Step 7 — Refuse aspirational features

Explicitly close with a section listing what this system *does not* include unless the user has earned it:

- No tagging beyond the categories in input 3.
- No nested folders > 2 levels deep.
- No tool migrations during the 30-day test.
- No backlog beyond a single "deferred-with-trigger" list.
- No daily review beyond the one (or two) defined triage blocks.

Most personal-system collapses come from feature accumulation. The 30 days is for the minimum viable system to prove itself.

---

## Constraints

### Must
- Compute and state the per-item triage budget (M / N).
- Pick exactly one inbox topology from the three options.
- Use the six-outcome triage rule set; no others.
- Fit the cadence inside the user's stated budget (input 6).
- Address every leak example (input 5) with a specific catch path.
- Specify a numeric 30-day survival test.

### Must Not
- Recommend a specific app or tool. Tools are user-chosen from input 7.
- Add capture or triage features beyond the spec.
- Recommend GTD, PARA, BASB, or any branded framework by name. Steal patterns; don't import dogma.
- Add nested category trees (> 2 levels deep) to the system.
- Promise the system will eliminate stress or "free your mind." Goal is leak reduction within budget.

---

## False-Positive Prevention

1. **Don't design above the user's stated tolerance (input 6).** A "better" system the user won't run is worse than a "worse" one the user will run. The tolerance is a hard constraint.
2. **Don't underuse Drop.** If the user has 4 categories and Drop is not visibly listed as an expected outcome for ≥ 20% of items, the system will overflow.
3. **Don't accept "I'll just be more disciplined."** That's the failure mode this prompt exists to replace. The system has to work without daily discipline beyond the cadence.
4. **Don't ignore inline-capture friction.** A sustainable triage block depends on inline capture being < 5 seconds. If capture friction is high, items will go uncaptured and the leaks will continue.
5. **Don't add a "review" cadence beyond the weekly maintenance.** Daily review of completed items is not in scope; that lives in `agency_end_of_session_review.md` (per-session) or `reviews_weekly_systems_review.md` (weekly).
6. **Don't escalate during triage.** If an item requires real thinking, it gets Schedule or Question-back. Triage is not the place to think.

---

## Output Format

```
## Constraints
- Daily input volume: ~ N items
- Daily triage budget: ~ M minutes
- Per-item triage budget: ~ (M/N × 60) seconds

## Inbox topology
**Pattern:** Single-funnel / Two-funnel / Channel-native
**Why:** [one sentence]
**Surface map:**
| Surface | Routes to | Inline-capture mechanism |
| email | people-inbox | star + batch |
| ... | ... | ... |

## Triage decision rules
[The six-outcome table reproduced for clarity, with any user-specific notes.]

## Cadence
- **Inline capture:** [per-surface mechanism, ≤ 5 sec each]
- **Daily triage block:** [time, duration, what gets touched]
- **Weekly maintenance:** [time, duration, what gets reviewed]

## Leak coverage (from input 5)
| Leak example | Catch path in new system | Catch confirmed? |
| ... | ... | ... |
[Any uncovered leaks named explicitly.]

## 30-day survival test
- Daily triage held on ≥ 22 of 30 days: yes/no
- Inboxes near-zero on ≥ 22 days: yes/no
- ≤ 1 leak per week: yes/no
- No tool migrations during the month: yes/no

If all four hold, the system is the system. If any fail, re-run this prompt at day 30 with new leak data.

## Aspirational features deferred until day 31+
- No tagging beyond the input 3 categories
- No nested folders > 2 levels
- No tool migrations
- No backlog beyond deferred-with-trigger list
- No additional review cadences
```

---

## Verification

- [ ] Per-item triage budget computed and stated.
- [ ] Exactly one topology selected with justification.
- [ ] Six-outcome triage table is the only ruleset used.
- [ ] Cadence fits stated tolerance (input 6).
- [ ] Every leak example (input 5) has a catch path or is explicitly accepted as uncovered.
- [ ] 30-day survival test stated as numeric checks.
- [ ] No specific tool/app prescribed; no branded framework imported.
- [ ] Aspirational-features deferral block included.
