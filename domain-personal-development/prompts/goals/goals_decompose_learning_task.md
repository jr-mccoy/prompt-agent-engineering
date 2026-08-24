---
title: "Learning Task Decomposition"
category: personal-development
description: "Break a vague learning goal into 7-9 atomic sub-skills with deliberate practice drills, dependency mapping, and a progressive practice schedule"
techniques:
  - ST-01
  - ST-02
  - CM-01
  - DD-02
  - DS-06
difficulty: beginner
tags:
  - personal-development
  - learning
  - skill-acquisition
  - practice
  - decomposition
  - deliberate-practice
updated: "2026-06-21"
related_prompts:
  - domain-personal-development/prompts/goals/goals_skill_breakdown_blueprint.md
  - domain-personal-development/prompts/goals/goals_goal_system_designer.md
  - domain-personal-development/prompts/thinking/thinking_memory_palace_generator.md
  - domain-personal-development/prompts/agency/agency_ship_sprint_design.md
---

# Learning Task Decomposition

**Objective:** Take a vague learning goal and decompose it into 7-9 atomic sub-skills, each with a specific deliberate practice drill, so you can build competence systematically instead of feeling overwhelmed by the whole.

## When to Use

- Use when: you are starting to learn something new and feel overwhelmed by its complexity, or you've been "studying" without measurable progress.
- Use when: you want a drill-focused practice path (scales-not-songs) for one specific skill.
- **Use this over its sibling `goals_skill_breakdown_blueprint.md` when** the input is a fuzzy *learning goal* that first needs to be sharpened into an observable capability — this prompt front-loads goal clarification (Phase 1) and produces a lighter 8-week arc. If you already have a clearly named skill and want a fully day-by-day scheduled 8-week blueprint with a learning-path diagram and explicit pitfall section, use `goals_skill_breakdown_blueprint.md` instead.
- Don't use when: you want to wrap a learning goal inside a broader multi-goal tracking/accountability system — use `goals_goal_system_designer.md`.

**Important context:** Effective learning requires practicing at the edge of your ability on specific sub-skills — not just "doing the thing" over and over. A pianist doesn't improve by playing full pieces; they improve by drilling scales, chord progressions, and difficult passages. This prompt creates that drill-focused learning path for any skill.

---

## Inputs / Context

**Skill to Master:** [The specific skill you want to develop]
**Current Level:** [Beginner/Intermediate/Advanced — with brief description of what you can do now]
**Time Available:** [Hours per week for practice]
**Specific Goal:** [What you want to be able to DO — not just "understand" or "know about"]
**Why Now:** [What prompted this learning goal]

**Refusal / insufficiency logic:** Do not produce a decomposition from a one-word skill ("coding," "design," "Spanish"). If **Specific Goal** is missing or is phrased as knowledge ("understand React") rather than a DO-able capability ("ship a deployed React app with auth"), stop and ask for the observable target first. If **Current Level** and **Time Available** are both absent, ask for them before scheduling — a schedule built on guessed hours is noise. Refuse to invent a goal the user did not state.

---

## Instructions

### Phase 1: Goal Clarification

Restate the learning goal as a specific, observable capability:
- **Bad:** "Get better at public speaking"
- **Good:** "Deliver a 10-minute technical presentation to 50+ people without notes, with clear structure and audience engagement"

### Phase 2: Sub-Skill Identification

Identify exactly 7-9 atomic sub-skills, ordered from foundational to advanced:

**Sub-skill #N: [Name]**
- **What it is:** [Specific capability — not a topic, but something you DO]
- **Why it matters:** [How it contributes to the whole skill]
- **Prerequisites:** [Which sub-skills must come first, or "none"]
- **Deliberate Practice Drill:** [One specific 15-30 minute exercise]
- **"Good Enough" Checkpoint:** [How you know you can move on — observable indicator]
- **Common Mistake:** [What learners typically get wrong at this stage]

### Phase 3: Dependency Map

Show which sub-skills build on which:

```
[Foundational A] ──→ [Intermediate C] ──→ [Advanced F]
[Foundational B] ──→ [Intermediate D] ──→ [Advanced G]
                     [Intermediate E] ──↗
```

Identify:
- **Parallel opportunities** — sub-skills that can be practiced simultaneously
- **Critical path** — the sequence that leads most directly to your goal
- **Optional enrichment** — sub-skills that are nice but not essential

### Phase 4: Practice Schedule

Design a progressive weekly schedule based on available time:

**Weeks 1-2: Foundation**
- Focus sub-skills: [Which ones]
- Practice sessions: [How many per week, how long]
- Checkpoint: [What you should be able to do by end of week 2]

**Weeks 3-4: Building**
- Focus sub-skills: [Which ones]
- Integration: [How to start combining sub-skills]
- Checkpoint: [Observable milestone]

**Weeks 5-8: Integration**
- Focus: [Combining sub-skills into the full skill]
- Practice: [Progressively harder applications]
- Checkpoint: [Can you do the target goal at a basic level?]

### Phase 5: Progress Tracking

- **Weekly self-test:** [One exercise that measures overall progress]
- **Plateau detector:** If no progress for 2 weeks, [specific diagnostic questions]
- **Mastery indicator:** [How you know you've achieved your goal]

---

### False-Positive Prevention

- ❌ Do NOT create sub-skills that are still too vague ("get better at X" is not a sub-skill)
- ❌ Do NOT assume linear progression — some skills have natural plateaus
- ❌ Do NOT skip foundational sub-skills even if they seem "boring" — they compound
- ❌ Do NOT create more than 9 sub-skills — decompose further if needed, but present the top level
- ✅ DO identify parallel learning opportunities to maximize practice time
- ✅ DO include "good enough" checkpoints — perfectionism on sub-skills delays overall progress
- ✅ DO make practice drills specific enough to do in 15-30 minutes
- ✅ DO address the most common mistakes at each stage

---

## Expected Output

```markdown
# Learning Path: [Skill]

## Goal
[Observable capability statement]

## Sub-Skills (7-9)
| # | Sub-Skill | Prerequisite | Drill | Checkpoint |
|---|-----------|-------------|-------|------------|
| 1 | [Name] | None | [15-30 min exercise] | [Observable indicator] |
| 2 | [Name] | #1 | [Exercise] | [Indicator] |
...

## Dependency Map
[Visual showing parallel and sequential paths]

## 8-Week Schedule
- Weeks 1-2: [Foundation sub-skills]
- Weeks 3-4: [Building sub-skills]
- Weeks 5-8: [Integration]

## Progress Tracking
- Weekly test: [Exercise]
- Plateau fix: [Diagnostic questions]
- Done when: [Mastery indicator]
```

---

## Verification

Before delivering the learning path, confirm each of these. If any fails, fix it before responding:

- [ ] The goal is restated as an **observable capability** (something you can watch the user DO), not a topic or "understand X."
- [ ] There are **7–9 sub-skills**, each atomic (a thing you do, not a subject area) — no item is itself a fuzzy "get better at…".
- [ ] Every sub-skill has a **drill completable in 15–30 minutes** and an **observable "good enough" checkpoint** (not "feel confident").
- [ ] The dependency map names at least one **parallel opportunity** and one **critical path** — it is not a single linear chain by default.
- [ ] The schedule's total weekly load **fits the user's stated Time Available** — no week silently exceeds it.
- [ ] **Verification-by-prediction:** for the Week-2 checkpoint, state what the user will be able to *do* that they cannot do today. If, after two weeks of the schedule, that prediction does not hold, the decomposition over- or under-shot — re-run with the corrected level.
- [ ] No sub-skill, drill, or constraint was invented that contradicts the user's stated context.

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Observable capability as the learning target
- **ST-02** (Structured Sequential Instructions) — Clarify, decompose, map, schedule, track
- **CM-01** (Explicit Context Framing) — Current level, time, and goals captured
- **DD-02** (Vague-to-Concrete Translation) — Converts vague goals into atomic sub-skills
- **DS-06** (Prioritization Guidance) — Critical path identification and schedule design

---

## Related Prompts

- [goals_skill_breakdown_blueprint.md](../goals/goals_skill_breakdown_blueprint.md) — Sibling: fully scheduled day-by-day 8-week blueprint once the skill is already named.
- [goals_goal_system_designer.md](../goals/goals_goal_system_designer.md) — Wrap learning goals in a broader multi-goal tracking system.
- [thinking_memory_palace_generator.md](../thinking/thinking_memory_palace_generator.md) — Memorize factual knowledge within the learning path.
- [agency_ship_sprint_design.md](../agency/agency_ship_sprint_design.md) — Ship something using the skills you're building.
