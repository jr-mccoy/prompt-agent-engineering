---
title: "Diagnose Stuckness Across a Fixed Taxonomy of Blockers"
category: personal-development/agency
description: "When the user is 'stuck' on a project, classify the stuckness into one of a small fixed set of blocker types — each with a different unblock move — so the user stops searching and starts doing the right unblock action."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - agency
  - stuck
  - diagnosis
  - blockers
  - unblock
updated: "2026-04-20"
related_prompts:
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_code_footgun_detector.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_first_delegation_spec.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_unstructured_start_exploration.md
  - domain-personal-development/prompts/agency/agency_planning_masquerade_detector.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
---

# Diagnose Stuckness Across a Fixed Taxonomy of Blockers

**Objective:** When the user says "I'm stuck," produce a specific diagnosis from a fixed taxonomy and the corresponding unblock move. Refuse to output general advice. Each blocker type has its own answer.

**When to use:** The user has been on a project or a specific task for more than a few sessions with no advance. They describe being stuck, blocked, confused, or unable to start.

**Audience:** An individual working solo. The diagnosis is for the user to act on; it is not meant for a manager, coach, or third party to apply from outside.

---

## Inputs Required

1. **The project or task they're stuck on.** One to two sentences.
2. **Concretely, what they tried most recently.** What was open, what they typed, what they stopped doing and why.
3. **How long they've been stuck.** Rough hours or days.
4. **What "unstuck" would look like physically.** The next artifact or state.
5. **How they'd describe being stuck in their own words.** Verbatim. The exact phrasing matters: "I don't know where to start" is a different blocker than "I keep starting over."

If any of (2)–(5) is missing, ask. Don't diagnose without them.

---

## Instructions

### Step 1 — Classify into exactly one category

Use only this taxonomy. Pick the one that fits best. If two seem to fit, pick the one earliest in the causal chain.

| # | Category | Signs | Core unblock |
|---|---|---|---|
| 1 | **Undefined outcome** | User cannot state what "done" looks like for this task. | Spec the outcome before the work. |
| 2 | **Scope too large** | User can describe done but every start runs out of energy before hitting it. | Halve the scope; pick the smallest shippable slice. |
| 3 | **Missing input** | Real external info is required and hasn't been obtained. | Identify the one person/source to ask, ask today. |
| 4 | **Skill gap (real, narrow)** | A specific known technique or piece of knowledge is required, not a field. | Single focused learning session (≤2h) aimed at that exact input; see `agency_skill_gap_reframe.md`. |
| 5 | **Skill gap (imagined, wide)** | "I need to learn X first" where X is a whole field. | Skill gap is being used as avoidance; see `agency_planning_masquerade_detector.md`. Proceed without X. |
| 6 | **Decision deferral** | Multiple viable paths; user refuses to pick one. | Pick one now, for this session only, revocable after. |
| 7 | **First-step ambiguity** | Project is clear; the very next physical motion is not. | Run `agency_next_action_spec.md`. |
| 8 | **Fear-of-shipping** | Work is near-finished; user keeps polishing. | Set a 24-hour ship deadline; see `agency_ship_sprint_design.md`. |
| 9 | **Wrong project** | User keeps drifting into adjacent work; the project they named isn't the one they want. | Name the real project; see `agency_project_ownership_converter.md`. |
| 10 | **Legitimate depletion** | User is tired, sick, life is hard. | Rest. No unblock move. |
| 11 | **Environment blocker** | A tool, setup, or access is actually broken. | Fix the specific technical thing; ignore the rest of this framework. |
| 12 | **Loss of why** | User no longer remembers why the project matters to them. | Pause project; reopen the question of whether to continue. |

Do not invent new categories. If none fit, return that and ask for clarification.

### Step 2 — Justify the classification

In one or two sentences, quote or paraphrase the user's own words and show why they map to the chosen category. If the user's description spans two categories, name the second and say why it was ranked second.

### Step 3 — Deliver the unblock move

The move must be:

- **Specific.** Named artifact, file, person, or action.
- **Small.** Under 60 minutes or clearly bounded.
- **Directly against the diagnosed blocker.** Undefined-outcome gets a spec move, not a scope move.

If the category is 10 (depletion), the move is to stop. Say that plainly.

### Step 4 — Verify by prediction

State what should be true at the end of the unblock move if the diagnosis is correct:

- For Category 1: a one-sentence "done" statement exists.
- For Category 2: a smaller scope is named, and the first 25 minutes on the smaller scope are defined.
- For Category 3: a specific ask has been sent.
- For Category 4: a specific concept has been practiced once.
- For Category 6: a decision is written down (revocable).
- For Category 7: a next-action spec exists.
- For Category 8: a public date is posted somewhere.
- For Category 11: the broken thing is fixed; the project itself is untouched.

This gives the user a check. If the move runs and the prediction doesn't hold, the diagnosis was probably wrong — re-run the prompt.

### Step 5 — Flag secondary blocker (if present)

If a secondary blocker is likely to surface once the primary is cleared, name it briefly. Do not solve it preemptively — the diagnosis may update once the primary is gone.

---

## Constraints

### Must
- Pick exactly one category from the taxonomy.
- Justify the pick using the user's actual words.
- Deliver exactly one unblock move.
- State a verifiable prediction for what changes after the move.
- Treat category 10 (depletion) as a real diagnosis — not an excuse to skip to a project move.

### Must Not
- Invent new categories.
- Give generic advice ("take a walk," "try meditation," "believe in yourself").
- Diagnose character flaws or mental health conditions.
- Present all 12 categories as a menu for the user to pick — the prompt picks one.
- Offer multiple unblock moves. One move, the right one.

---

## False-Positive Prevention

1. **Don't default to "skill gap (imagined)."** Check if the user has stated a specific missing piece (category 4) before labeling the whole field as avoidance.
2. **Don't over-diagnose "fear of shipping."** It requires near-finished work. If the work is 40% done, it's usually scope or first-step, not fear.
3. **Don't misread depletion as avoidance.** If the user has been ill, grieving, or overloaded at a day job, that's depletion, and the answer is rest — not a reframing exercise.
4. **Don't treat environment blockers as psychological.** If the build is broken, the diagnosis is "fix the build," not "examine your relationship to work."
5. **Don't chain the prompt.** Run it, try the move, see what happens, run again if needed. Each run picks one category.

---

## Output Format

```
## Diagnosis
**Category:** [Number + name from taxonomy]

**Justification:** [One to two sentences grounded in the user's words.]

**Secondary candidate (if any):** [Category + brief reason it was ranked second, or "none"]

## Unblock move
[One specific, small, bounded action.]

## Prediction
After doing the move, the following will be true: [specific checkable state].

If this prediction doesn't hold, re-run this prompt.

## Likely next blocker after primary clears
[One sentence, or "unknown — reassess after the primary clears."]
```

---

## Verification

- [ ] Exactly one category chosen.
- [ ] Justification quotes or paraphrases the user.
- [ ] Unblock move is small, specific, and directly fights the diagnosed blocker.
- [ ] Prediction is observable after the move runs.
- [ ] Category 10 (depletion) was considered — not skipped.
- [ ] No generic advice, no character commentary.
