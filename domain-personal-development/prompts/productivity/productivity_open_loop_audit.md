---
title: "Open Loop Mental Clarity Audit"
category: personal-development
description: "Capture all unfinished tasks, worries, and commitments from your head, sort them into actionable buckets, and identify the next action for each — based on Getting Things Done methodology"
techniques:
  - ST-01
  - ST-02
  - CM-01
  - DD-02
  - DS-06
difficulty: beginner
tags:
  - personal-development
  - mental-clarity
  - open-loops
  - GTD
  - stress-reduction
  - task-management
updated: "2026-06-21"
related_prompts:
  - domain-personal-development/prompts/productivity/productivity_personal_energy_audit.md
  - domain-personal-development/prompts/productivity/productivity_automation_gold_mine.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
  - domain-personal-development/prompts/agency/agency_planning_masquerade_detector.md
---

# Open Loop Mental Clarity Audit

**Objective:** Capture every unfinished task, worry, commitment, and "I should..." thought rattling around in your head, sort them into actionable buckets, and define a clear next action for each — freeing your mind from the anxiety of trying to remember everything.

## When to Use

- Use when: you feel overwhelmed but can't pinpoint why, or have a vague sense of "too many things."
- Use when: you can't focus because your mind keeps jumping to other tasks, or you haven't done a brain dump in 2+ weeks.
- Use this to **capture and triage an unstructured mental backlog** into buckets and next actions. To then turn a single top item into a keystroke-level next move, hand off to `agency_next_action_spec.md`. To check whether the "tasks" are actually planning-as-avoidance, run `agency_planning_masquerade_detector.md`.
- Don't use when: you already have a clean list and just need to schedule it against your energy — use `productivity_personal_energy_audit.md`.

**Important context:** Open loops are commitments, tasks, and thoughts that your brain keeps cycling on because they don't have a trusted external home. The stress comes not from having too much to do, but from not having a clear system for what to do next. This audit closes the loops.

---

## Inputs / Context

**Brain Dump:** [Paste your entire list of tasks, worries, notes, and "I should..." thoughts. Don't organize — just dump everything. Include work, personal, admin, health, relationships, finances, projects, someday/maybe ideas — everything.]

**Refusal / insufficiency logic:** This audit works only on the user's own material. If the brain dump is empty or just a topic ("help me get organized"), prompt the user to actually dump their open loops first — do **not** invent tasks, worries, or commitments on their behalf. If the dump is a single tidy line, ask whether that's truly everything; the value is in surfacing the messy full set. Sort only what the user wrote.

---

## Instructions

### Phase 1: Capture and Sort

Sort every item from the brain dump into buckets:

| Bucket | Items | Count |
|--------|-------|-------|
| **Work** | [Tasks related to your job/business] | |
| **Personal** | [Home, family, relationships, hobbies] | |
| **Admin** | [Bills, paperwork, appointments, errands] | |
| **Health** | [Exercise, diet, medical, wellness] | |
| **Projects** | [Multi-step initiatives that need planning] | |
| **Someday/Maybe** | [Ideas you want to remember but not act on now] | |

**Rule:** Every item from the brain dump must appear in exactly one bucket. Nothing gets lost.

### Phase 2: Next Action Definition

For each item in active buckets (not Someday/Maybe), define:

| Item | Next Physical Action | Time Needed | Priority |
|------|---------------------|-------------|----------|
| [Task] | [The very next thing to DO — not "think about" or "figure out"] | [Minutes] | High/Med/Low |

**Key principle:** If the next action takes less than 2 minutes, do it now. Don't put it on a list.

### Phase 3: Triage

- **Do today:** Items that are urgent + important (max 3)
- **Schedule this week:** Items that are important but not urgent
- **Delegate:** Items someone else could handle
- **Drop:** Items that have been on your list so long they clearly don't matter
- **Someday/Maybe:** Items to review next month, not act on now

### Phase 4: System Check

- Are there items that keep reappearing? (You need a recurring system, not a one-time action)
- Are there items older than 30 days? (Either do them, schedule them, or admit you won't)
- Are there items you're avoiding? (Name the avoidance — fear, boredom, uncertainty — and address it)

---

### False-Positive Prevention

- ❌ Do NOT create a beautiful organized list that the user will never look at again — focus on next actions
- ❌ Do NOT add items the user didn't mention — this is their brain dump, not yours
- ❌ Do NOT prioritize everything as "high" — real triage requires honest deprioritization
- ❌ Do NOT guilt-trip about old items — some things genuinely don't matter anymore and should be dropped
- ✅ DO ensure every item has exactly one next physical action (not "research" but "spend 15 minutes googling X")
- ✅ DO flag the 2-minute items for immediate action
- ✅ DO normalize dropping items — a shorter list is a more honest list
- ✅ DO recommend a weekly review cadence to prevent loop re-accumulation

---

## Expected Output

```markdown
# Open Loop Audit: [Date]

## Summary
- Total items captured: [N]
- Active items: [N]
- Someday/Maybe: [N]
- Dropped: [N]

## Sorted Buckets
### Work ([N] items)
| Item | Next Action | Time | Priority |
|------|------------|------|----------|

### Personal ([N] items)
...

## Today's Focus (max 3)
1. [Most important next action]
2. [Second]
3. [Third]

## 2-Minute Actions (do now)
- [Quick action 1]
- [Quick action 2]

## Items to Drop (be honest)
- [Item you've been avoiding that doesn't actually matter]

## Weekly Review Reminder
Schedule 15 minutes every [day] to re-run this audit.
```

---

## Verification

Before delivering the audit, confirm each of these. If any fails, fix it before responding:

- [ ] **Every item from the brain dump appears in exactly one bucket** — nothing was lost, nothing was added that the user didn't write.
- [ ] Each active item has a **physical next action** ("spend 15 min googling X"), never "research" / "think about" / "figure out."
- [ ] **2-minute items are flagged for immediate action**, not parked on a list.
- [ ] Today's focus is **capped at 3 items** — not everything is marked High priority.
- [ ] At least one honest **Drop** candidate is surfaced where warranted (a shorter list is a more honest list) — without guilt-tripping.
- [ ] Recurring or 30-day-old items are flagged for a **system fix or honest deletion**, not just re-listed.
- [ ] A **weekly re-run cadence** is recommended to prevent loop re-accumulation.

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Mental clarity through complete capture and sorting
- **ST-02** (Structured Sequential Instructions) — Capture, sort, define actions, triage
- **CM-01** (Explicit Context Framing) — Unfiltered brain dump as input
- **DD-02** (Vague-to-Concrete Translation) — Converts vague worries into specific next actions
- **DS-06** (Prioritization Guidance) — Triage into do/schedule/delegate/drop

---

## Related Prompts

- [productivity_personal_energy_audit.md](../productivity/productivity_personal_energy_audit.md) — Optimize *when* you tackle these tasks.
- [productivity_automation_gold_mine.md](../productivity/productivity_automation_gold_mine.md) — Automate recurring tasks from your list.
- [agency_next_action_spec.md](../agency/agency_next_action_spec.md) — Turn a top item into one keystroke-level next action.
- [agency_planning_masquerade_detector.md](../agency/agency_planning_masquerade_detector.md) — Check whether the "tasks" are planning-as-avoidance.
