---
title: "Convert a Vague Goal into a Project You Fully Own"
category: personal-development/agency
description: "Turn a diffuse aspiration into a concrete project with named scope, a first deliverable, an owner of record, and a definition of done — so the work stops drifting and starts moving."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - QA-01
difficulty: beginner
tags:
  - agency
  - ownership
  - goal-setting
  - project-definition
  - self-directed-work
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/delegation/delegation_intent_specification.md
  - domain-personal-development/prompts/goals/goals_goal_system_designer.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
---

# Convert a Vague Goal into a Project You Fully Own

**Objective:** Take a fuzzy, drifting aspiration ("get healthier," "learn AI," "build an audience," "ship a side project") and convert it into a defined project the user personally owns — with a named scope, a first deliverable, a single owner of record, a short-horizon definition of done, and a first-week action plan.

**When to use:** The user keeps stating the same goal week after week with no movement. They can say what they want in the abstract but cannot describe what they are working on today. Energy is being spent on research, planning, reading, and optionality-preservation instead of execution.

**Audience:** A single individual doing self-directed work, often alongside a day job or other commitments. Not a manager defining work for someone else. Not a coach facilitating a session with a client.

---

## Inputs Required

Before producing output, collect:

1. **The goal as currently stated** (one sentence, in their words).
2. **How long they've been stating this goal.** (days, months, years)
3. **What they've actually done in the last 30 days toward it.** Concrete actions, not intentions.
4. **What's on their plate already.** Job, family, other commitments that set time and energy constraints.
5. **Why it matters to them personally** — not a generic reason, a specific one. If they can't articulate one, flag that and ask.
6. **What "done" would look like in 90 days.** If unclear, part of the job is to make it clear.

If fewer than four of these are answered, ask for the missing ones before drafting the project definition.

---

## Instructions

### Step 1 — Diagnose the goal's current state

Classify the stated goal on these axes:

- **Scope:** infinite (lifestyle-level) / bounded (could plausibly finish) / unclear
- **Ownership:** self-owned / shared / waiting on someone else
- **Verifiability:** observable from outside / only felt internally / unclear
- **Evidence of movement:** none / sporadic / consistent

Report the classification plainly. Goals that are infinite, externally-dependent, or unobservable will not convert into projects without reshaping first.

### Step 2 — Reshape into a project candidate

A project, for this prompt's purposes, has:

- **A name.** Short, specific, not a category. ("Ship a newsletter for sales engineers" — not "Build an audience.")
- **A first deliverable.** Something that can exist in the world within 2–6 weeks, that the user could show another human.
- **An owner of record.** For a personal project, this is the user. Name them. Write the sentence "I, [name], own this end-to-end." No sharing responsibility with a future collaborator.
- **A definition of done for the first deliverable.** Concrete, checkable, binary.
- **An explicit out-of-scope list.** Three to five things this project is not, to prevent scope drift.

If the goal cannot be reshaped this way, say so and explain which part resists. Do not invent a project the user didn't agree to.

### Step 3 — Identify the smallest credible first deliverable

The first deliverable is not the whole project. It is the piece that:

- Can be built in one focused session or one weekend.
- Proves at least one real question about the project.
- Exists as an artifact (a document, a commit, a published post, a recorded call, a working script). Not "decide on a topic." Not "research the market."

Draft the first deliverable as a one-sentence description plus a two-line acceptance test.

### Step 4 — Lock the first week

Produce a 5–7 line plan for the coming week. Each line is an action the user will personally do, with a specific day and a specific output. No "think about," "explore," or "look into." If an item cannot be stated as "[verb] [object] by [day]," rewrite it.

### Step 5 — Ownership confirmation

End with a short ownership statement the user is expected to commit to, verbatim or in their own words:

- What they are building.
- What the first deliverable is.
- By when.
- That they own it.
- What they will stop doing to make room for it.

If the user cannot commit to the stop-doing item, the project is not real yet — say that.

---

## Constraints

### Must
- Produce a single named project, not a menu.
- Give a first deliverable bounded at 2–6 weeks, with a binary definition of done.
- Name the owner (the user) explicitly.
- Include a first-week plan with day-level specificity.
- Include an out-of-scope list.
- Flag when the stated goal is not yet project-shaped and explain why.

### Must Not
- Produce motivational language ("you've got this," "believe in yourself").
- Reshape the goal into someone else's project (a team, a cofounder, a future hire).
- Suggest research, reading, or planning as the first deliverable.
- Propose a 6-month or 12-month roadmap — this prompt is about the first 2–6 weeks.
- Assume constraints (budget, time, family) that were not stated.
- Invent success criteria the user did not agree to.

---

## False-Positive Prevention

This prompt produces prose that can easily masquerade as a project. Guard against:

1. **Category-as-project.** "Build an audience" is a category. "Publish 6 essays on sales-engineering career moves by June 1" is a project. If the name could describe 50 different people's work, it's a category.
2. **Planning-as-deliverable.** "Create a content calendar" is not a first deliverable. The first deliverable must be an artifact someone outside the user could encounter.
3. **Optionality preservation.** If every option is kept open "just in case," no project has been defined. Force the user to pick one.
4. **Ownership laundering.** "I'll work on this with my friend" is shared ownership. Ask who owns it end-to-end. If neither person does, it won't ship.
5. **Fake urgency.** If the user sets a 2-week deadline for something that realistically takes 8, they'll miss, lose trust in the process, and drift. Push back on deadlines that don't match the work.

If any of these show up in the draft, rewrite the relevant section before returning it.

---

## Output Format

```
# Project: [Name]

## Owner
[User name]. I own this end-to-end.

## What this is
[2–3 sentence plain-English description.]

## What this is NOT
- [Out-of-scope item 1]
- [Out-of-scope item 2]
- [Out-of-scope item 3]

## First deliverable
[One-sentence description.]

**Definition of done (binary):**
- [ ] [Checkable criterion 1]
- [ ] [Checkable criterion 2]

**Target date:** [Specific date, 2–6 weeks out]

## First-week plan
- [Day]: [Verb] [object] — output: [artifact]
- [Day]: [Verb] [object] — output: [artifact]
- ...

## Stop-doing (to make room)
- [Specific thing being cut or deferred]

## Goal-state classification
- Scope: [infinite / bounded / unclear]
- Ownership: [self / shared / external]
- Verifiability: [observable / internal-only / unclear]
- Evidence of movement last 30 days: [none / sporadic / consistent]

## Flags
[Anything that suggests the goal is not yet project-shaped, or a constraint the user should confront before committing.]
```

---

## Verification

Before returning the output, check:

- [ ] Project name is specific enough that another person could not mistake it for a different project.
- [ ] First deliverable is an external artifact, not an internal state.
- [ ] Definition of done has at least two binary criteria.
- [ ] First-week plan has day-level specificity and verbs that produce output.
- [ ] Out-of-scope list has at least three items.
- [ ] Nothing in the draft assumes constraints the user didn't state.
- [ ] Nothing in the draft invents scope the user didn't agree to.

If any fail, revise before returning.
