---
title: "Navigate the First 90 Days in a New Role Without Running the Old Playbook"
category: personal-development/life-transitions
description: "Map what actually changed in a new job or promotion, locate where old habits now misfire, and commit to the one relationship and one competence to invest in first — instead of coasting on prior-role instincts."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - life-transitions
  - new-role
  - onboarding
  - promotion
  - habits
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/life-transitions/lifetransition_transition_map_and_timeline.md
  - domain-personal-development/prompts/life-transitions/lifetransition_returning_from_leave.md
  - domain-personal-development/prompts/identity/identity_purpose_reignition.md
  - domain-personal-development/major-decisions/personal_career_offer_evaluation.md
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
---

# Navigate the First 90 Days in a New Role Without Running the Old Playbook

**Objective:** Produce a first-90-days orientation that names what changed, flags which old habits now misfire, and commits to exactly one relationship and one competence to invest in first.

**When to use:** You started a new job, were promoted into a different scope, or changed teams and are already in the role. Useful in weeks 1–8 when instincts from the last role are firing automatically. Not for deciding whether to accept the role — that is `major-decisions/personal_career_offer_evaluation.md`.

**Audience:** An individual settling into their own new role. Not for onboarding someone you manage, not clinical. If the transition produces persistent dread, insomnia, or a sense of collapse rather than ordinary adjustment strain, this is not a substitute for professional support — see `domain-psychology/` and a licensed professional.

---

## Inputs Required

1. **Old role vs. new role — scope delta.** In two columns: what you owned before, what you own now. Include who you now report to, who reports to you, budget/decision authority, and what success is measured by.
2. **What earned you the last role.** 3–5 behaviors, strengths, or habits that made you good at the previous job (e.g., "I fixed things fast myself," "I knew every detail").
3. **Two weeks of real activity.** How your first 10–14 working days actually went, in rough time buckets and 5–8 concrete moments (a meeting you led, a decision you made or dodged, a task you grabbed).
4. **The people map.** 5–10 people in the new orbit and, for each, one line: what they need from you and what you need from them.
5. **One moment that already felt wrong.** A specific recent instance where you acted and it landed badly or awkwardly.

If the scope delta (input 1) is missing or the activity log has fewer than 5 concrete moments, refuse and ask for them. You cannot locate misfiring habits without the before/after and real behavior.

---

## Instructions

### Step 1 — Classify the type of change

Assign the move to the **dominant** change type (pick one primary, note a secondary if real):

| Change type | What actually shifts | Habit that now misfires |
|---|---|---|
| Scope-up (IC → lead / bigger area) | You win through others, not output | Doing the work yourself |
| Lateral-context (new team/company, same level) | Relationships and norms reset to zero | Assuming shared context |
| Domain-shift (new function/skill) | Your expertise no longer transfers cleanly | Leaning on old expertise for credibility |
| Authority-jump (new decision rights) | Your words now carry weight you didn't have | Thinking out loud / casual opinions |

### Step 2 — Locate where the old playbook misfires

For each behavior in input 2, ask: in the new role, does this still work, work partially, or now backfire? Use the input 3 activity log and input 5 as evidence. A behavior only gets flagged as "backfires" if a specific moment shows it landing badly — no speculation.

### Step 3 — Read the wrong-moment (input 5)

Trace input 5 to one misfiring habit from Step 2. State in one sentence: *the old-role instinct that fired, and what the new role needed instead.* This is the concrete anchor for everything below.

### Step 4 — Pick the one relationship to invest in first

From the people map, select the single relationship where (a) early trust compounds most over the next 90 days and (b) it is currently thin or unbuilt. Not the friendliest, not the most senior by default — the highest-leverage-and-underbuilt one. Name the specific first move (a scheduled 1:1, a specific ask, a specific offer).

### Step 5 — Pick the one competence to build first

From the scope delta, select the single new-role skill that most gates your success and that you do not yet have. Name how you'll practice it on real work in the next two weeks — a specific task or decision you'll deliberately do the new way.

### Step 6 — Commit the one substitution

Produce one **stop-doing / start-doing** substitution: the top misfiring old habit to consciously suspend, and the specific new behavior that replaces it this week, with an observable check.

---

## Constraints

### Must
- Assign exactly one primary change type and justify it from the scope delta.
- Flag "backfires" only where input 3 or 5 shows a concrete instance.
- Select exactly one relationship and exactly one competence — not a list.
- End with one stop/start substitution that is physical and time-bounded.

### Must Not
- Recommend a generic "30-60-90 plan" template or "listen and learn for 90 days" platitude.
- Congratulate the user on the promotion or reassure them it'll be fine.
- Flag an old habit as misfiring without a supporting moment.
- Output a ranked list of five relationships or five skills — pick one of each.

---

## False-Positive Prevention

1. **Don't assume every old habit is now wrong.** Many still work. Only the ones with evidence of backfiring get flagged; the rest are explicitly kept.
2. **Don't diagnose impostor feeling as the problem.** Ordinary competence lag in a new role is expected, not a defect. Route persistent, function-impairing self-doubt to `domain-psychology/`; don't pathologize week-two uncertainty.
3. **Don't pick the most comfortable relationship.** The prompt selects for leverage-and-underbuilt, which is usually not the person you already click with.
4. **Don't confuse being busy with onboarding.** High activity in the first weeks can be old-playbook reflex (grabbing tasks). Check whether the activity serves the new scope.
5. **Don't over-scope the competence.** One skill, practiced on real work, not an enrolled course or a reading list.
6. **Don't treat a bad first meeting as a verdict.** One awkward moment is data about a habit, not proof the role was a mistake.

---

## Output Format

```
## Change type
Primary: [type] — because [scope-delta evidence]. Secondary (if any): [type].

## Old playbook audit
| Old behavior (input 2) | Status in new role | Evidence |
|---|---|---|
| ... | Still works / Partial / Backfires | [moment] |

## The wrong moment (input 5)
Old instinct that fired: [...]. What the role needed: [...].

## First relationship to build
[Person] — highest leverage + currently thin because [...].
First move: [scheduled, specific action] by [date].

## First competence to build
[Skill] — gates success because [...].
Practice on: [specific real task/decision] in the next 2 weeks.

## The one substitution (this week)
Stop: [misfiring habit]. Start: [replacement behavior].
Predicted check: within [n] days, [observable difference in a meeting / decision / handoff].
```

---

## Verification

- [ ] Exactly one primary change type, justified from the scope delta.
- [ ] Every "backfires" flag cites a concrete moment from input 3 or 5.
- [ ] Behaviors that still work are explicitly kept, not all flagged.
- [ ] Exactly one relationship and one competence selected, each with a reason.
- [ ] One stop/start substitution, physical and time-bounded, with a check.
- [ ] No 30-60-90 template, no reassurance, no congratulation.
- [ ] Persistent dread/collapse routed to professional support, not coached here.
