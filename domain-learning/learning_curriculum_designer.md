---
title: "Curriculum Designer — N-Week Path to a Defined Level in a Domain"
category: learning/curriculum
description: "Design a week-by-week curriculum (default 12 weeks) that moves a learner from a stated current level to a defined target level in a domain. Defines the target observably (a project, test, or shippable work), builds the prerequisite tree, sequences theory + practice each week, identifies the load-bearing skills that compound, schedules spaced revisits of foundations, and assigns a visible weekly deliverable. Counters the two failure modes: a reading list with no doing, and a pile of practice with no foundation."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-02
  - RT-11
  - QA-01
difficulty: intermediate
tags:
  - learning
  - curriculum
  - skill-acquisition
  - spaced-repetition
  - deliverables
updated: "2026-06-18"
reasoning:
  styles: [analytic, systems, strategic]
  stakes: moderate
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo
  output_format: [structured, ranked_list]
  user_role: [individual, learner, professional]
  mode: [plan, synthesize]
related_prompts:
  - domain-learning/learning_skill_gap_to_curriculum.md
  - domain-learning/learning_deliberate_practice_designer.md
  - domain-learning/learning_reading_list_curator.md
---

# Curriculum Designer — N-Week Path to a Defined Level in a Domain

**Objective:** Produce a sequenced, week-by-week curriculum that takes a learner from a current level to a defined target level in a domain, within a stated time budget. The discipline this enforces is the difference between a curriculum and a wish list: a curriculum has an observable target, a prerequisite order (you can't sequence what you haven't tree'd), theory paired with practice every week, a small set of load-bearing skills that everything else compounds on, deliberate re-encounters with the foundations so they don't decay, and a visible deliverable each week so progress is felt and verifiable. The default span is 12 weeks; the user can override.

**When to use:**
- A learner has a clear domain and a real reason to reach a defined level (a job, a project, a creative goal, a test).
- They have a sustainable weekly time budget and want it spent well.
- The domain is learnable through study + practice (not primarily through years of apprenticeship or credentialing).

**When NOT to use:**
- The goal is a single narrow skill, not a domain — use `learning_deliberate_practice_designer.md`.
- The learner can't yet name their target level observably — run `learning_skill_gap_to_curriculum.md` first to define the gap.
- The domain requires supervised/regulated training where a self-directed curriculum would be inappropriate (use the formal program; this can supplement, not replace).

**Audience:** Self-directed learners, professionals reskilling, and anyone building a structured path toward a defined competency.

---

## Inputs / Context

1. **Target domain.** What field/skill area.
2. **Current level.** Honest: never touched it / dabbled / working knowledge / intermediate. With evidence (what you can already do).
3. **Target level.** What you want to be able to do at the end.
4. **Time available per week.** Realistic hours, sustainable for N weeks.
5. **Span.** Number of weeks (default 12).
6. **Learning-style preferences.** Reading / video / projects / problem sets / live practice — and any known constraints.

---

## Constraints

### Must
- Define the target **observably**: a project, a test passed, a creative work produced, or a job-relevant task the learner can perform — not "understand X" or "get good at Y."
- Build the **prerequisite tree** before sequencing: what concept/skill must come before what. Sequencing follows the tree, not the table of contents of a textbook.
- Pair **theory and practice every week**. A week of pure reading or pure drilling is a flag.
- Identify the **load-bearing skills** — the few that compound, that later weeks depend on disproportionately — and front-load and over-invest in them.
- Schedule **spaced revisits** of foundations (not just forward motion); foundations decay and later material exposes the gaps.
- Assign a **visible weekly deliverable** — something shippable, gradeable, or showable each week, so progress is observable and not just felt.
- Constrain the plan to the learner's **actual weekly hours**; do not silently assume more.
- Include a **checkpoint** mid-way and at the end to test whether the target is on track.

### Must Not
- Produce a reading/watching list with no production. Consumption without output is the single most common failure of self-study.
- Sequence by a textbook's chapter order when the prerequisite tree implies a different order.
- Spread effort evenly across all topics when a few are load-bearing and the rest are leaves.
- Pack the plan to the edge of the time budget with no margin; learning needs slack for the weeks that run long.
- Define success as "completed the curriculum." Completion is not competence; the observable target is.

---

## Instructions

### Step 1 — Define the observable target
Translate the target level into something you can see: "ship a working CRUD web app with auth and tests," "pass the AWS SAA practice exams at 80%," "produce a 5-painting portfolio with consistent likeness," "give a 20-minute talk on the topic without notes." If the learner can't make it observable, that's the first thing to fix.

### Step 2 — Build the prerequisite tree
Map the concepts/skills and their dependencies. What must be solid before the next thing makes sense? Identify the roots (no prerequisites) and the leaves (depend on everything). This tree, not a syllabus, drives the order.

### Step 3 — Identify the load-bearing skills
From the tree, mark the few nodes that the most later nodes depend on. These compound. Plan to over-invest in them early and to revisit them deliberately. Name them explicitly.

### Step 4 — Set the weekly cadence
Given the hours/week and span, decide the rhythm: how much theory vs. practice per week, when deliverables ship, when checkpoints fall. Reserve margin (don't allocate 100% of available hours).

### Step 5 — Sequence the weeks
Lay out N weeks. Each week: the topic(s) (in tree order), the theory input (specific resources or types), the practice activity, and the deliverable. Front-load load-bearing skills. Build later weeks on earlier deliverables where possible.

### Step 6 — Insert spaced revisits
Schedule explicit re-encounters with the load-bearing foundations at increasing intervals (e.g., revisit week-2 fundamentals in weeks 5 and 9), woven into new material rather than as standalone review weeks.

### Step 7 — Place checkpoints
A mid-point checkpoint (is the target reachable on this trajectory?) and an end checkpoint (was the observable target met?). Each is a yes/no test, not a vibe. Include a redirect if the mid-checkpoint fails (cut scope, extend span, or change approach).

### Step 8 — Stress-test against the time budget
Sum the realistic hours per week against the stated budget. If it exceeds, cut leaf topics, not load-bearing ones, until it fits with margin. State what was cut.

### Step 9 — Verify and output
Run the verification checklist; deliver the week-by-week plan.

---

## False-Positive Prevention

1. **Consumption-only plan.** Weeks full of reading and videos with nothing produced. Every week needs a deliverable; flag any week that's input-only.
2. **Syllabus sequencing.** Ordering by a book's chapters instead of the prerequisite tree, so the learner hits material they're not ready for. Sequence the tree.
3. **Even-spread effort.** Giving load-bearing skills the same time as trivial ones. Front-load and over-invest in what compounds.
4. **No spaced revisit.** Pure forward motion, so foundations decay and week-8 material fails on week-2 gaps. Schedule deliberate re-encounters.
5. **Unobservable target.** "Understand machine learning." Reject and force a visible target.
6. **Budget overrun.** A plan that needs 15 hours/week when the learner has 6. Cut to fit with margin; don't hand over a plan that fails in week one.
7. **Completion = competence.** Treating finishing the plan as the goal. The checkpoint tests the observable target, not attendance.
8. **No redirect on the mid-checkpoint.** A checkpoint with no consequence is decoration. Specify what changes if it fails.

---

## Output Format

```
# Curriculum — [domain]: [current level] → [target level], [N] weeks @ [hrs/wk]

## Observable target
[What the learner can demonstrably do/produce at the end.]

## Prerequisite tree (summary)
- Roots: [...]
- Load-bearing skills (compound): [...]
- Leaves: [...]

## Cadence
- Theory/practice split: [...]
- Deliverable rhythm: [weekly]
- Margin reserved: [hrs/wk]

## Week-by-week
| Week | Topic (tree order) | Theory input | Practice | Deliverable | Revisit? |
|------|--------------------|--------------|----------|-------------|----------|
| 1 | | | | | |
| 2 | | | | | |
| ... | | | | | |
| N | Synthesis + target attempt | — | — | [target deliverable] | — |

## Checkpoints
- Mid (week [k]): [yes/no test]. If fail → [redirect: cut scope / extend / change approach].
- End (week N): [target met? yes/no test].

## What was cut to fit the budget
- [leaf topic dropped] — reason: [...]
```

---

## Verification

- [ ] The target is observable (a project, test, work, or task), not "understand X."
- [ ] A prerequisite tree exists and the week order follows it.
- [ ] Load-bearing skills are named and front-loaded.
- [ ] Every week pairs theory and practice and has a deliverable.
- [ ] Spaced revisits of foundations are scheduled at increasing intervals.
- [ ] Total hours fit the stated budget with margin; cuts are stated.
- [ ] Mid and end checkpoints are yes/no tests, and the mid-checkpoint has a redirect.
- [ ] Success is defined as the observable target, not curriculum completion.
- [ ] No input-only weeks survive.
