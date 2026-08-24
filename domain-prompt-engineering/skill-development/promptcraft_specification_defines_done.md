---
title: "Write a Specification That Fully Defines 'Done'"
category: prompt-engineering/skill-development
description: "Given a task the user is handing to AI, produce a specification where 'done' is unambiguous — every criterion is observable, the set is closed (nothing important is unstated), and a stranger could pass/fail any output against it without asking the user a question. Refuses to produce specs for tasks the user can't yet describe as an outcome."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - skill-development
  - specification
  - done-definition
  - observable-criteria
  - pass-fail
updated: "2026-04-20"
related_prompts:
  - domain-engineering-workflows/done-definition/done_definition_translator.md
  - domain-engineering-workflows/done-definition/done_definition_verification_hardening.md
  - domain-engineering-workflows/done-definition/done_definition_gate_sets_by_domain.md
  - domain-prompt-engineering/skill-development/promptcraft_eval_harness.md
  - domain-prompt-engineering/evaluation/correctness_tradeoff_forcer.md
---

# Write a Specification That Fully Defines "Done"

**Objective:** Produce a specification that turns a task into a set of observable pass/fail criteria. A stranger reading the spec and looking at a candidate output must be able to say "done" or "not done" without asking the user a clarifying question. This is the skill-development-focused complement to `done_definition_translator.md` (which is the engineering-workflow production tool) — this version teaches the user how to build specs for their own recurring tasks.

**When to use:** The user has a recurring task type (memo drafts, code reviews, research summaries, decision memos, etc.) and keeps ending up in "this isn't quite right" loops. Or: the user is about to delegate a task to AI and can feel the spec is loose.

**Audience:** Individuals working on their specification muscle. Repeat users of this prompt build a personal library of specs for their top task types over time.

**Distinction from done_definition_translator.md:** The engineering tool is optimized for on-the-fly production use — translate a fuzzy task into done gates *now*. This prompt is optimized for learning — the user walks through each step, produces a spec they save for reuse, and builds intuition for what "observable" actually means.

---

## Inputs Required

1. **The task as an outcome sentence.** If the user can't state this, stop and route to `promptcraft_pre_ai_thinking_exercise.md`.
2. **Who the output is for.** A downstream person, a downstream system, or the user themselves.
3. **An example of a past output that was "done."** Real, not hypothetical.
4. **An example of a past output that was "not done" even though it looked like it might be.** Real, not hypothetical. This is the more important of the two.
5. **Stakes and reversibility.** If the output ships and is wrong, what's the cost? And can it be undone?

Refuse to produce a spec on an invented task. Synthetic tasks produce synthetic criteria; the user learns nothing transferable. If the user has no past outputs, they haven't run the task type enough to need a spec yet.

---

## Instructions

### Step 1 — Contrast the two past examples

Put the "done" and "not done" examples side by side. Ask: *what specifically made one done and the other not?* The user will initially answer "it just felt wrong"; push until the answer is specific. "The not-done one didn't name the March exception" is a criterion. "It felt unfocused" is not.

Extract 2–5 differences. These are the raw material for the spec.

### Step 2 — Rewrite each difference as a pass/fail criterion

Every criterion must:
- Be observable by looking at the output (not the process).
- Be answerable by a stranger who has not seen the user's prior chats.
- Produce pass or fail, not a score.

Good: "Output contains the phrase 'March exception' at least once and names the specific exception number."
Good: "Output recommends exactly one path, not two or more."
Bad: "Output is focused." (Not observable by a stranger.)
Bad: "Output feels right." (Not anything.)

### Step 3 — Close the set

Now ask: *could a submission pass every criterion above and still be "not done"?* Usually yes. Keep adding criteria until a stranger who reads only the spec and grades only against it would agree with the user's acceptance decision.

Stop when:
- The user looks at a candidate pass and says "yes, that's actually done."
- And a candidate that fails would, in the user's judgment, correctly be rejected.

Most specs stop at 4–8 criteria. Beyond 10, the spec starts to become a style guide and the criteria interact — fail one and you've failed them all.

### Step 4 — Rank by load-bearing

Not every criterion is equal. Rank:
- **Must-pass (1–3):** If any of these fail, the output is rejected regardless of the rest.
- **Should-pass (2–5):** Expected to pass; failures are fixable.
- **Nice-to-have (0–3):** Increase quality but not gates.

This ranking is what makes the spec usable. An agent loop that treats every criterion as must-pass will thrash; one that treats them all as nice-to-have will accept garbage.

### Step 5 — Add the stop rule

A spec without a stop rule is an infinite loop. State:
- Maximum iterations before the user looks at the output manually (e.g., 3).
- What happens if must-pass criteria fail on the final iteration — does the output ship with flags, or is the task escalated to human?
- What to do if the output passes all criteria but still feels wrong (usually: add the missing criterion to the spec, then ship).

### Step 6 — Add the escalation triggers

Some outputs should escalate out of AI regardless of spec pass. Usually:
- Task touches regulated output (legal, medical, financial — domain-dependent).
- Must-pass fails with the same root cause twice.
- Output mentions anything the user didn't ask about that would change the scope. (A legal memo AI writes that flags "also, you might be out of compliance with X" — the X part gets routed to human.)

### Step 7 — Name the counterfactual

Every spec has boundaries. What is the spec *not* trying to enforce? Common examples:
- Style is not specified — any clean style passes.
- Length is not specified above the floor.
- Ordering of sections is not specified.

Naming what the spec doesn't cover prevents hidden criteria from sneaking in during review. Hidden criteria are the source of the "not done, but I can't tell you why" loop.

### Step 8 — File the spec for reuse

The output is a reusable artifact, not a disposable prompt. File it by task type so the next time the user runs this task, they start from the saved spec, not from scratch. Suggest a folder layout:
- `personal-specs/[task-type]/v[N].md` — the current spec.
- `personal-specs/[task-type]/past-examples/` — the training examples.
- `personal-specs/[task-type]/revision-log.md` — what changed and why.

---

## Constraints

### Must
- Be built from contrasting a real done and real not-done example.
- Produce 4–10 criteria, ranked must-pass / should-pass / nice-to-have.
- Include a stop rule and escalation triggers.
- Name what the spec doesn't cover.
- Be saved as a reusable artifact, not produced as a one-shot chat reply.

### Must Not
- Be produced for a hypothetical task.
- Include a criterion that can't be graded by a stranger.
- Contain more than 10 criteria without forcing the user to cut.
- Omit the stop rule — a spec without a stop rule is incomplete.
- Collapse must-pass and nice-to-have into a single flat list.

---

## False-Positive Prevention

1. **Process criteria masquerading as output criteria.** "The user consulted the stakeholder before drafting" is process, not output. A spec grades output. If the user can't see it in the artifact, it doesn't belong in the spec.
2. **"Observable" that isn't observable by a stranger.** "Sounds like me" requires knowing the user. "Uses second-person voice throughout" is observable. Rewrite every criterion until it could be graded by someone who's never met the user.
3. **The closed set that isn't closed.** After Step 3, push once more: can you construct a submission that passes everything and is still wrong? If yes, add the missing criterion. This is the highest-leverage step; users skip it and ship loose specs.
4. **Rank inflation.** Users often mark everything must-pass. A must-pass list with 8 items isn't a must-pass list. Force the cut to 1–3.
5. **Specs that are actually style guides.** A spec enforces correctness; a style guide enforces taste. If Step 2 keeps producing style criteria, the task is actually a style-guide task and needs a different tool.
6. **Running spec on an AI task the user can't do themselves.** If the user can't produce a "done" example by hand, they don't know what done is. Don't produce a spec until a done example exists.
7. **Stop rule that's actually "keep going."** "Retry until it passes" is not a stop rule. Set a hard iteration cap and name what happens at the cap.
8. **Missing counterfactual.** Specs without a "what this doesn't cover" section grow hidden criteria during review. Require Step 7.

---

## Output Format

```markdown
## Training examples
- Done example: [reference/link]
- Not-done example: [reference/link]
- Differences extracted: [...]

## Specification

### Must-pass (1–3)
1. [Observable criterion]
2. [Observable criterion]

### Should-pass (2–5)
1. [...]
2. [...]

### Nice-to-have (0–3)
1. [...]

### Stop rule
- Max iterations: [N]
- On final-iteration must-pass failure: [ship with flag / escalate / reject]
- On pass-but-feels-wrong: [add missing criterion, then ship]

### Escalation triggers
- [Condition that forces human review]
- [...]

### What this spec doesn't cover
- [Style | length above floor | section order | ...]

---

## Closed-set test
Does a candidate that passes every criterion above match the user's
"done" intuition? [Yes / No — if No, add missing criterion and repeat.]

## Filing
- Save as: `personal-specs/[task-type]/v[N].md`
- Retire when: [specific revision trigger]
```

---

## Verification

- [ ] Spec was built from a real done + real not-done contrast.
- [ ] Every criterion is observable by a stranger.
- [ ] Criteria are ranked must-pass / should-pass / nice-to-have, and must-pass is 1–3.
- [ ] Stop rule is present and names a hard iteration cap.
- [ ] Escalation triggers are specific, not "if it seems bad."
- [ ] A "what this spec doesn't cover" section is present.
- [ ] The closed-set test was run and passed, or a missing criterion was added.
- [ ] The spec is saved to a reusable location.
