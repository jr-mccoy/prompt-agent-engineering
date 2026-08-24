---
title: "Ship a Real Change Into a Codebase Without Writing Code Yourself"
category: engineering-workflows/ai-native-rollouts
description: "A step-by-step runbook for shipping a real, reviewable change into a real codebase entirely through AI delegation — no manual code writing. Forces specification, verification, and merge discipline, so the outcome is production-quality and the engineer learns how to manage AI-authored code end-to-end."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - RT-11
  - QA-01
difficulty: intermediate
tags:
  - ai-native-rollouts
  - ai-delegation
  - code-authoring
  - verification
  - runbook
updated: "2026-04-21"
related_prompts:
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_first_delegation_spec.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_engineering_manager_stance.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_intent_and_verification_first.md
  - domain-engineering-workflows/ai-patterns/ai_review_outcome_level_code_review.md
  - domain-engineering-workflows/ai-native-rollouts/airollout_delegate_like_parallel_coworker.md
  - domain-software-engineering/vibe-coding-rescue/viberescue_rules_file_design.md
---

# Ship a Real Change Into a Codebase Without Writing Code Yourself

**Purpose:** A concrete runbook for an engineer to ship one real PR, merged, into a real codebase — entirely through AI delegation — without manually writing code. The goal is not productivity; the goal is to learn, end-to-end, what the "manage AI-authored code" workflow actually feels like, including the specification work, verification work, and review work that no-code-writing reveals. Ship-by-delegation is a skill; this prompt teaches it with guardrails so the PR is still production-quality.

**When to use:**
- An engineer new to AI-native work wants to learn the end-to-end loop on a real task, not a toy.
- A team is standing up AI-assisted development and wants a shared exercise that produces concrete artifacts and lessons.
- A senior engineer is evaluating whether their current AI tools and rules file actually hold up under a real change.
- An AI-native onboarding exercise for a new hire.

**Don't use when:** The task is genuinely trivial (typo fix), where delegation overhead exceeds benefit. Pick a task with at least some logic.

**Audience:** A working engineer with commit access, an AI tool, and a real task in their queue.

---

## Inputs Required

1. **The candidate task.** 1–2 sentences describing what needs to change and why. Rule of thumb: the task should have 1–3 files of expected change and at least one testable behavior.
2. **The repo.** Language, framework, test runner, rough size, and whether the test suite runs cleanly today.
3. **AI tool(s) being used.** Claude Code / Cursor / Copilot / custom — whichever the engineer is using.
4. **Existing rules file or conventions doc, if any.** If none, note that; step 2 addresses it.
5. **The engineer's no-code-writing commitment horizon.** For this task only, or for the next N tasks? Scope this prompt to a single task.

---

## Instructions

### Step 1 — Confirm task fit

Check the task against this filter:

- [ ] Has a clearly testable behavior (at least one unit or integration test could fail or pass to prove the change).
- [ ] Touches code you understand well enough to review, not just files you've never seen.
- [ ] Is not time-critical (learning exercise ships, but shouldn't carry a deadline).
- [ ] Is not security-sensitive at the load-bearing layer. (Changing auth, crypto, or permission logic is a bad first task.)

If two or more checks fail, pick a different task. Don't force fit.

### Step 2 — Write the specification before opening the tool

Produce a written spec that an unfamiliar engineer could implement from. Include:

- **What changes, from what, to what.** State the current behavior and the target behavior.
- **Why the change matters.** One sentence.
- **Files likely touched.** Best guess; the AI may expand it.
- **Observable success criteria.** A test that currently fails (or doesn't exist) and, after the change, passes.
- **Out-of-scope.** What you are NOT changing, even if tempted.
- **Conventions to follow.** If a rules file exists, name it. If not, write a one-paragraph mini-rules-file now — naming, error handling, logging, test style.

If the spec takes < 10 minutes, it's probably too vague. Expand until a competent colleague could work from it.

### Step 3 — Plan verification before opening the tool

Write down, in this order, how you will verify the change:

- **Test-level:** Which tests must pass. Which tests you will add. If you can't state this, stop and redo the spec.
- **Code-level review:** What you will check specifically (no hand-waving "I'll read it"). E.g., "Check that X is called from Y only in the branch where Z." List 3–5 concrete checks.
- **Behavioral-level:** Run the code. What command, what input, what output you'll observe.

Verification plan exists before the AI writes a line.

### Step 4 — Delegate in scoped turns, not one megaprompt

Give the AI the spec. Then ask for:

1. Its understanding of the task, stated back in its own words. If the understanding is off, correct it before it writes code.
2. Its plan for which files to change and in what order. If the plan looks wrong, redirect.
3. The first file's change only. Review. Approve or reshape.
4. Subsequent files, one or a few at a time.

Do NOT paste the whole spec and say "do it all." That is the failure mode.

### Step 5 — Review like it came from a junior engineer

Check the AI's output against:

- The spec (step 2). Does it match the "from what, to what" description?
- The conventions (step 2). Naming, error handling, logging, test style.
- The three concrete code-level checks (step 3).
- Style drift against neighboring code.
- Obvious overreach: changes outside the listed files, changes that look correct but aren't what you asked for.

If anything fails, send the specific feedback back to the AI. Do not fix it yourself.

### Step 6 — Run the verification plan yourself

- Run the tests. All must pass.
- Run the code-level checks. Eyes on the actual code.
- Run the behavioral test. Input / output as pre-planned.

Write, in one or two sentences, what you observed. Don't skip this.

### Step 7 — Handle the edge cases the AI didn't anticipate

Before opening a PR, ask yourself (not the AI): what real situation, user, or input does this change not handle well? List 2–3 edge cases. Send them to the AI to address, one at a time. Each edge case goes through steps 4–6.

### Step 8 — Open the PR

Write the PR description yourself. The description states:

- The change in one sentence.
- The tests added/updated and why.
- What's out-of-scope of this PR.
- A note that the change was authored via AI delegation (transparency helps reviewers calibrate).

Link the spec and verification plan in the PR body or a linked doc.

### Step 9 — Process review comments through the AI

When a human reviewer comments, paste the comment and the surrounding code to the AI. Ask the AI to propose a change. Review it yourself before applying. If the reviewer is asking for something you should just decide (a design choice), decide it yourself, then tell the AI what you decided and have it execute.

### Step 10 — After merge, capture lessons

In 5–10 bullets, note:

- Specification moments where the spec was too vague and the AI guessed.
- Verification moments where the AI's change would have passed a loose review but failed your checklist.
- Tool friction (token limits, context mgmt, tool calling quirks).
- What you would add to the rules file / conventions doc for next time.
- Whether this felt faster or slower than hand-writing. Be honest — the goal wasn't speed.

### Step 11 — Verify and output

Run the verification checklist. Output the full runbook artifact the engineer produced.

---

## Constraints

### Must
- Write the specification and verification plan before the AI writes any code.
- Delegate in scoped turns, not one megaprompt.
- Review every AI-produced change against a specific checklist.
- Run the verification plan yourself, observably.
- Write the PR description yourself.
- Capture lessons after merge.

### Must Not
- Write code yourself during the task. (Configuration and rules-file edits are allowed; production code is the AI's.)
- Ship without running the verification plan.
- Let the AI scope-creep beyond the spec without explicitly expanding the spec first.
- Commit AI-generated commit messages without reading them.
- Merge without a human reviewer's approval.
- Choose a first task that's security-critical, production-critical, or on a tight deadline.

---

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Accept "looks right" as a review pass. Tie each approval to a specific code-level check.
- Let the AI explain what it did in lieu of reading the diff. The AI's explanation is a claim; the diff is evidence.
- Skip the edge-case pass because the tests pass. Tests the AI wrote check the AI's own understanding — they can be self-confirming.
- Merge after only automated tests pass. You must also run the behavioral check.
- Call the exercise a success because the PR merged. The success is the lessons in step 10 and the shape of the resulting rules file.

✅ **DO:**
- Treat the AI like a junior engineer who is fast and confident and sometimes wrong.
- Require the AI to state its understanding before it writes code.
- Run the tests with your own hands, not just trust a CI green check.
- Track how often the AI drifted from the spec — that's the number you'll reduce as you get better.
- Keep the rules file as the artifact of this exercise. Next task starts from a better rules file.

---

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Engineer approves AI output without real review; AI generates plausible-looking code with a subtle correctness bug; bug ships.

❌ **UNHELPFUL failure:** Engineer spends 10x the hand-writing time on ceremony, learns nothing beyond "AI is slow," and concludes delegation doesn't work.

✅ **Quality check:** At merge + lessons-captured, the engineer can point to at least 2 specific moments where the workflow caught something (correctly), and 2 specific moments where the workflow was friction they'd reduce next time.

---

## Output Format

```markdown
# Ship-By-Delegation Runbook — [Task Name]

## Spec
- What changes (from → to):
- Why:
- Files likely touched:
- Observable success criteria (test):
- Out of scope:
- Conventions (inline or linked rules file):

## Verification Plan
- Test-level: [which tests, which tests to add]
- Code-level checks (3–5 concrete): [list]
- Behavioral check: [command, input, expected output]

## Delegation Log (per turn)
| Turn | Ask | AI output summary | Review result (accept / reshape / reject) |
|------|-----|-------------------|------------------------------------------|
| 1 | | | |

## PR
- Title:
- Body: [link]
- Reviewer(s):
- Merged: [date]

## Post-Merge Lessons (5–10 bullets)
- …

## Rules File Additions (for next time)
- …
```

---

## Verification

- [ ] Spec and verification plan exist before any AI code.
- [ ] Every AI turn is scoped; no single megaprompt.
- [ ] Every AI change was reviewed against a concrete checklist.
- [ ] Verification plan was run by the engineer, not inferred.
- [ ] Edge-case pass happened.
- [ ] PR description written by the engineer.
- [ ] Post-merge lessons captured (5–10 bullets).
- [ ] Rules file updated with at least one addition.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Ship a reviewable, merged PR through delegation — explicit, bounded.
- **ST-02 (Structured Sequential Instructions):** 11 steps from task fit → spec → verification plan → scoped turns → review → verify → edge cases → PR → review cycle → lessons → verify.
- **CM-02 (Constraint Specification):** Must Not block forbids megaprompts, unsigned-off AI commit messages, and merging without human review.
- **DS-01 (Framework Application):** Task-fit filter is a 4-check framework that keeps the exercise from starting on a bad task.
- **RT-11 (Error Recovery):** Explicit handling for AI drift — restate spec, scope down, redirect — rather than assuming the AI won't drift.
- **QA-01 (Self-Verification):** Concrete code-level checks, behavioral verification, and a lessons-capture step gate the runbook.
