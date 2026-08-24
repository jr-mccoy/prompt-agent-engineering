---
title: "Decompose a Complex Single Task"
category: productivity/deep-work
description: "Take one stuck or oversized task and decompose it into sub-tasks with clear entry points, pre-conditions, and verification — so the user stops treating 'design the dashboard' as a single 4-hour item and starts working at the level where progress is visible."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-02
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - deep-work
  - decomposition
  - task-planning
  - stuck
updated: "2026-04-20"
related_prompts:
  - domain-productivity/deep-work/deepwork_chunk_project_to_calendar.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_first_delegation_spec.md
---

# Decompose a Complex Single Task

**Objective:** Decompose one oversized or stuck task into a sequence of sub-tasks where each has a clear entry point, a pre-condition stating what must exist to start, and a verification that shows it's done. The decomposition should reveal, not hide, where the task's real difficulty sits.

**When to use:** The user keeps writing the same single task on a daily list and never finishes. A task feels blurry, too big, or "I don't know where to start." Before a focus block where the task's shape is unclear.

**Audience:** The individual doing the task, not a delegate or collaborator.

---

## Inputs Required

1. **The task, stated as the user currently thinks of it.** One sentence.
2. **Why it matters — what depends on it.** One sentence.
3. **What "done" looks like concretely.** A named artifact, decision, or state.
4. **What the user has already tried.** Even one sentence.
5. **Their guess at what the hard part is.** Optional. If empty, decomposition itself may surface it.
6. **Whether there's an external deadline.** Date or none.

---

## Instructions

1. **Restate the task in one sentence using verb-object form with a visible output.** "Design the dashboard" becomes "Produce a single screen that shows X/Y/Z for role W." If you cannot, the task is too vague — ask for input 3 again.

2. **Decompose into 3–7 sub-tasks.** Each must have:
   - **Entry point** — the first physical action to begin this sub-task
   - **Pre-condition** — what must exist before this sub-task is startable
   - **Verification** — how the user will know this sub-task is done, independent of the whole task
   - **Est. minutes** — rough

   A sub-task with unclear verification is not a sub-task, it's a wish. Rewrite or cut.

3. **Identify the hard sub-task.** The one that contains the real difficulty. Name it explicitly. Hard sub-tasks are often short but dependent on an unavailable decision or piece of information.

4. **Classify each sub-task:**
   - **Clear and doable now** — start here
   - **Blocked** — waiting on external input or decision
   - **Exploratory** — no certain path; needs investigation before it can be broken down further
   - **Optional** — contributes to done but not required

   Explicitly flag Exploratory sub-tasks — those resist decomposition until explored.

5. **Produce the sequence.** Start with a Clear-and-doable-now sub-task, even if it's small, before the hard one. Momentum from visible completion makes the hard sub-task easier to enter.

6. **Name what this decomposition does not solve.** If the real block is a missing decision from someone else, decomposition won't help and should say so.

---

## Output Format

```
## Task Restated
[Verb + object + visible output]

## Decomposition
| # | Sub-task | Entry point | Pre-condition | Verification | Est min | Class |
|---|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... | clear |
| ... |

## The Hard Sub-Task
[Name it; one-sentence reason it's hard.]

## Sequence
[Ordered list of sub-tasks, starting with a clear-and-doable-now item.]

## What This Does Not Solve
- [external dependency or missing decision, if any]
```

---

## Constraints

**Must:**
- Restate the task with a visible output before decomposing.
- Every sub-task has entry point + pre-condition + verification.
- Name exactly one "hard" sub-task.
- Start the sequence with a clear-and-doable-now item if any exist.

**Must not:**
- Produce sub-tasks named "research", "think about", or "plan" without a concrete output.
- Flatten hard sub-tasks out of the list. Hiding difficulty is the failure mode this prompt exists to prevent.
- Produce more than 7 sub-tasks. If you need more, the user is actually doing a project — switch to `deepwork_chunk_project_to_calendar.md`.
- Recommend a specific timer or technique for each sub-task.

---

## False-Positive Prevention

- **Theater decomposition:** "1. Gather requirements 2. Draft 3. Review 4. Refine 5. Ship" is not decomposition; it's a stock template. Reject if sub-tasks could apply to any task.
- **Hidden hard part:** If decomposition feels suspiciously easy, the hard sub-task was dropped. Reinspect input 4 — what has the user bounced off?
- **Verification-as-feeling:** "I'll know it's done when it feels right" is not verification. Force artifact-level specificity.
- **Fake unblocking:** A blocked sub-task waiting on someone else stays blocked. Decomposition cannot force someone else's decision.

---

## Self-Verification (before finalizing)

- [ ] Task restated with visible output.
- [ ] 3–7 sub-tasks, each with entry point + pre-condition + verification + estimate + class.
- [ ] One hard sub-task named with a reason.
- [ ] Sequence starts with a clear-and-doable-now item if any exist.
- [ ] At least one verification is artifact-based, not feeling-based.
- [ ] What the decomposition does not solve is named if applicable.
