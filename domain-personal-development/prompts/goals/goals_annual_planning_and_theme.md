---
title: "Plan a Year or Quarter From Evidence, Not Resolutions"
category: personal-development/goals
description: "Turn a year or quarter into a small set of themes plus 2–3 keystone goals derived from evidence of what the last period actually produced, tolerated, and dropped — instead of from aspiration. Outputs the themes, the keystone goals, and the one anti-resolution guardrail."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - goals
  - annual-planning
  - themes
  - keystone-goals
  - anti-resolution
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/goals/goals_values_to_goals_derivation.md
  - domain-personal-development/prompts/goals/goals_anti_goals_avoidance_list.md
  - domain-personal-development/prompts/goals/goals_goal_system_designer.md
  - domain-personal-development/prompts/identity/identity_values_clarification.md
  - domain-personal-development/major-decisions/personal_career_offer_evaluation.md
---

# Plan a Year or Quarter From Evidence, Not Resolutions

**Objective:** Produce a small set of themes and 2–3 keystone goals for the coming period, each derived from documented evidence of the last period — not from a wish list — plus one anti-resolution guardrail.

**When to use:** Year-end or quarter-start planning; you feel the pull to write an ambitious resolution list you know from history you won't keep; you want a plan grounded in what you actually did last period rather than who you wish you were. Not for planning a single project's sprint (see `goals_goal_system_designer.md`) or for high-stakes one-off decisions (see `domain-personal-development/major-decisions/`).

**Audience:** An individual planning their own period. Not for setting objectives for a team or assessing someone else, and not clinical. If reviewing the last period surfaces persistent hopelessness or distress, that is not what this prompt treats — see `domain-psychology/` and a licensed professional.

---

## Inputs Required

1. **Period being planned.** Year or quarter, with start and end dates.
2. **Evidence from the last equal period.** Required, not optional. Supply:
   - 3–6 things that actually shipped/completed (with rough dates).
   - 3–6 things that were started and abandoned, or planned and never begun.
   - 2–4 recurring frustrations or costs the user paid repeatedly.
   - Where the largest blocks of time and money actually went (rough buckets).
3. **Last period's stated goals or resolutions, if any exist**, and which of them held.
4. **Fixed constraints for the coming period.** Known commitments, capacity ceilings, money limits, life events already on the calendar.
5. **The one outcome the user would be most disappointed to reach the period's end without.**

If input 2 has fewer than 3 completed items AND fewer than 3 abandoned items, refuse and ask for the evidence. A plan without a record of the last period is a resolution, which is exactly what this prompt exists to prevent.

---

## Instructions

### Step 1 — Read the evidence before touching aspiration
From input 2, extract the pattern of the last period: what this person, under their real constraints, actually completes vs. abandons. Name the completion pattern in one or two sentences (e.g., "finishes work with an external deadline and a named collaborator; abandons solo open-ended learning projects"). Cite specific items.

### Step 2 — Derive candidate themes from the pattern
A **theme** is a direction for the period, not a metric — e.g., "consolidate, don't expand," "get one thing to shipped-and-maintained," "reduce the recurring cost of X." Generate 2–4 candidate themes, each traceable to evidence from Step 1. A theme that is not supported by last-period evidence is an aspiration; drop it.

### Step 3 — Cut to at most 2 themes
Apply this fixed test to each candidate theme and keep at most two:

| Test | Keep only if |
|---|---|
| Evidence-backed | It answers a pattern from Step 1, not a wish |
| Capacity-fit | It survives input 4's constraints |
| Disappointment-linked | It moves input 5, or protects the capacity to |

Two themes maximum. Three or more themes is how a plan becomes a resolution list.

### Step 4 — Derive 2–3 keystone goals
A **keystone goal** is one whose completion drags several smaller things along with it. Under each surviving theme, name 1–2 keystone goals — 2–3 total across the whole period. Each keystone goal must be:
- **Observable** — a state you can watch yourself reach, not "get better at."
- **Sized to the completion pattern** from Step 1, not to the aspiration.
- **Traceable** to a theme and to input 5.

If a candidate goal matches the abandonment pattern (e.g., solo, open-ended, no external deadline for someone whose evidence shows they abandon exactly those), flag it and either restructure it to match the completion pattern or cut it.

### Step 5 — Write the one anti-resolution guardrail
Identify the single most likely way this plan becomes last period's failed resolutions again — drawn from input 3 and the abandonment list. Write one guardrail: a concrete rule or tripwire that catches that specific failure mode early (e.g., "if by end of month 1 goal X has no external deadline attached, it gets cut, not carried"). One guardrail, not a list of good intentions.

### Step 6 — State the first observable checkpoint
Name what should be observably true at the end of the first month (or first two weeks for a quarter) if this plan is real rather than aspirational. This is the decisive output that lets the user tell early whether the plan is holding.

---

## Constraints

### Must
- Ground every theme and keystone goal in specific evidence from input 2.
- Keep to ≤ 2 themes and 2–3 keystone goals total.
- Size goals to the demonstrated completion pattern, not to aspiration.
- Produce exactly one anti-resolution guardrail tied to a real past failure.
- End with one first-month observable checkpoint.

### Must Not
- Generate a list of 5+ goals or "areas of focus."
- Include a goal whose only support is that the user wants it (that is a resolution).
- Use motivational framing, "new year new you" language, or affirmations.
- Congratulate or shame the user for last period's abandoned items.
- Recommend a vision board, word-of-the-year, or generic reflection exercise.

---

## False-Positive Prevention

1. **Don't accept an aspiration as evidence-backed.** "I want to run a marathon" is not supported by a last period whose evidence shows zero running. Restructure to the completion pattern or cut it.
2. **Don't let theme count creep.** Three themes reads as balanced but functions as a resolution list. Two is the ceiling; enforce it.
3. **Don't confuse a keystone goal with a busy goal.** A keystone drags other things along; a busy goal just fills the plan. If completing it changes nothing downstream, it is not keystone.
4. **Don't mistake last period's held resolutions for the whole pattern.** One kept goal doesn't overturn an abandonment record. Weight by frequency of evidence, not by the flattering exception.
5. **Don't smooth over a time/money contradiction.** If the theme claims one priority but time and money went elsewhere, name it rather than planning as if the theme were already true.
6. **Don't size to a fantasy calendar.** Fit goals to input 4's real constraints, not to an imagined uninterrupted period.

---

## Output Format

```
## Last period's pattern (from your evidence)
Completes: [pattern, with cited items]
Abandons: [pattern, with cited items]
Recurring cost paid: [pattern, with cited items]

## Themes for [period] (max 2)
1. [Theme] — evidence: [specific items from last period]
2. [Theme] — evidence: ...

## Keystone goals (2–3 total)
- [Goal] — theme: [x] · observable state: [what you'll watch yourself reach] · sized to: [completion pattern] · serves: [input 5]
- ...

## Anti-resolution guardrail (one)
Most likely failure mode: [drawn from input 3 + abandonment list].
Guardrail: [one concrete rule / tripwire that catches it early].

## First checkpoint
By [end of month 1 / first two weeks], the following is observably true if this plan is real: [specific observable].
```

---

## Verification

- [ ] Input 2 evidence met the minimum bar; otherwise the prompt refused.
- [ ] Every theme and keystone goal cites specific last-period evidence.
- [ ] No more than 2 themes and no more than 3 keystone goals.
- [ ] At least one candidate goal matching the abandonment pattern was flagged and restructured or cut.
- [ ] Exactly one anti-resolution guardrail, tied to a documented past failure.
- [ ] One first-month observable checkpoint stated.
- [ ] No resolution language, no affirmations, no moralizing about abandoned items.
