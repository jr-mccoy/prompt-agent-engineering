---
title: "Team-Level Focus Audit and Norms"
category: productivity/deep-work
description: "Audit a team's working norms — meeting load, message patterns, response-time expectations, shared calendar habits — to find where team structure is destroying individual focus, and propose 3–5 team norms tied to observed patterns rather than a generic 'no meeting Wednesdays' playbook."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - deep-work
  - team
  - norms
  - focus
  - audit
updated: "2026-04-20"
related_prompts:
  - domain-productivity/deep-work/deepwork_calendar_audit.md
  - domain-productivity/deep-work/deepwork_meeting_cost_estimator.md
  - domain-productivity/deep-work/deepwork_meeting_to_async_converter.md
---

# Team-Level Focus Audit and Norms

**Objective:** Given data about a team's current working rhythms, diagnose the specific structural patterns destroying individual focus at the team level and propose 3–5 norms tied to those patterns. Not generic focus advice; norms that target observed problems.

**When to use:** A team lead or engineering manager sees recurring signals (missed deadlines, burnout, overrun meetings, nobody shipping during the day) and suspects the team's shared rhythm is the cause. Before proposing a process change to the team.

**Audience:** A team lead, manager, or tech lead with authority to propose norms. Not the individual worker — for individual-level focus, use other prompts in this folder.

---

## Inputs Required

1. **Team size and composition.** Roles and count.
2. **Shared meeting load** — recurring meetings everyone on the team attends, with duration and frequency.
3. **Sample of last 2 weeks of team channel activity** — what kinds of messages dominate (requests, decisions, FYIs, social), with rough volume.
4. **Current expectations around response time** — explicit or implicit, e.g., "within an hour during work hours" or "nobody said, but everyone replies fast."
5. **Shared or visible calendars.** Whether anyone blocks focus time on a public calendar and whether those blocks get respected.
6. **Two or three anecdotes of recent focus failures** — concrete examples of someone losing a day to interruptions, a project slipping because nobody had time, a meeting that should have been async.
7. **What the team lead has the authority to change.** Meeting calendar, norms, tools, staffing — list.

---

## Instructions

1. **Compute collective meeting load.** Hours per week per person from input 2. Flag if > 15 hours/week.

2. **Classify channel activity** into categories (request / decision / FYI / social / noise) with a rough percentage each. If requests or FYIs dominate, the team is using chat as broadcast — a structural issue.

3. **Identify the dominant team-level focus-destruction pattern** from a fixed set:
   - **Meeting monoculture** — everyone's week is shaped by the same recurring meetings
   - **Ambient availability expectation** — the implicit response-time norm prevents any protected block
   - **Chat as status meeting** — decisions and coordination happen by broadcast, not by record
   - **Calendar as suggestion** — nobody respects blocked focus time
   - **Single-point-of-contact bottleneck** — one or two people are interrupted constantly because they hold knowledge

   A team may have two patterns. List both, with evidence from inputs.

4. **For each dominant pattern, propose exactly one norm.** Norm format:
   - **Norm name**
   - **Observable behavior change**
   - **How it will be verified** (weekly signal the team lead will watch)
   - **What happens when violated** — not punishment, but repair

5. **Check each proposed norm against input 7.** If the team lead lacks authority to enforce it, rewrite as "escalate to [role]" or cut.

6. **Anticipate resistance.** For each norm, name the person or sub-group most likely to resist and the specific concern. If the resistance is legitimate, adjust the norm.

7. **Produce a trial period.** No norm is permanent. Propose 4 weeks with a specific review date.

---

## Output Format

```
## Current State
- Team size: N
- Meeting load: NN hr/wk/person
- Dominant channel type: [category, N%]
- Stated response-time expectation: [...]
- Focus-time blocks respected? yes/sometimes/no

## Dominant Patterns
1. [pattern from fixed set] — evidence: [inputs cited]
2. [pattern] — evidence: [...]

## Proposed Norms (≤ 5)
### Norm 1: [name]
- Behavior change: [...]
- Verified by: [weekly signal]
- Repair when violated: [...]
- Likely resistance: [who, what concern]
- Authority check: [confirmed / escalate / cut]

...

## Trial Period
- Start: [date]
- Review: [date]
- Kept / adjusted / dropped criteria: [specific signals]

## What This Audit Does Not Address
- [individual-level focus issues, for example]
```

---

## Constraints

**Must:**
- Tie every norm to one or more observed patterns from inputs.
- Verify authority before proposing enforceable norms.
- Name a specific review date.
- Limit to 5 norms maximum — more than 5 will not stick.

**Must not:**
- Propose generic norms ("no-meeting Wednesday") without evidence the team's pattern warrants that specific day.
- Assume cultural changes via Slack post alone — norms need both an announcement and a review mechanism.
- Ignore resistance. If a legitimate concern surfaces, name it and adjust.
- Roll up individual-level focus prescriptions into team norms. Keep scope to team structure.

---

## False-Positive Prevention

- **Vanity norm:** "Protect deep work" is not a norm; it's a slogan. Force observable behavior change.
- **Meeting-count fallacy:** Reducing meeting count doesn't help if the remaining meetings are badly placed. Structure matters more than count.
- **Imported playbook:** Just because another team succeeded with no-meeting-Friday doesn't mean this team has a Friday problem. Evidence first.
- **Authority overreach:** A team lead proposing a CEO-level policy change produces nothing. Keep norms within input 7.
- **Social-to-policy leap:** Sometimes team dysfunction is social (trust, psychological safety) and norms won't fix it. If audit evidence points there, say so.

---

## Self-Verification (before finalizing)

- [ ] Every dominant pattern cites evidence from inputs.
- [ ] Every norm has behavior change + verification + repair.
- [ ] Every norm is within the team lead's authority per input 7.
- [ ] Likely resistance named for each norm.
- [ ] Trial period with specific review date included.
- [ ] No more than 5 norms.
- [ ] Scope is team-level; individual-level issues are flagged as out of scope.
