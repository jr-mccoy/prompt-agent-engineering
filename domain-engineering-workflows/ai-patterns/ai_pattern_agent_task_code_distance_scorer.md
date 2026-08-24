---
title: "Code Distance Scorer for Agent Task Suitability"
category: ai-patterns
description: "Score a candidate task on its 'code distance' — how far the agent has to reason, read, and change from any well-marked entry point. Short code-distance tasks suit agents; long ones suit humans or need decomposition."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - ai-patterns
  - agent-task-design
  - delegation
  - task-suitability
  - scoring
updated: "2026-04-20"
related_prompts:
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_first_delegation_spec.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_work_loop_design.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_delegation_rule_test.md
---

# Code Distance Scorer for Agent Task Suitability

**Purpose:** Not every task is a good candidate for agent delegation — but "use your judgment" is vague. This prompt produces a structured score along five dimensions of **code distance**: how far the task's reasoning, reading, and editing need to reach from a clean starting point. Tasks with short code distance are strong agent candidates; medium-distance tasks need decomposition; long-distance tasks should stay with humans or be reshaped before delegation.

**When to use:**
- You're deciding whether to delegate a task to an agent or do it yourself
- You're triaging a backlog of candidate tasks to find the agent-friendly ones
- You're about to delegate a task that "feels" hard to delegate but you can't articulate why
- You're teaching a team to pick good agent tasks and need a shared language
- You keep delegating tasks that fail in the same way — use this to catch the pattern upstream

**What you'll get:** A five-axis score (Entry Points / Read Radius / Edit Radius / Semantic Depth / Implicit Knowledge), a composite verdict (Delegate / Decompose / Do It Yourself), named reasons per axis, and — if Decompose — a suggested split.

---

```
## ROLE
You score a candidate task's code distance and produce a delegate/decompose/do-it-yourself verdict. You do NOT solve the task. You evaluate how far from known anchors the agent would have to travel to complete it.

## CONTEXT
Code distance is a rough proxy for "how hard this task is to delegate well." Five dimensions:

1. **Entry Points** — how clearly does the task start somewhere known?
   - 0: the fix/feature/change has an explicit line/file/function named or obvious
   - 3: the agent has to search from a vague description ("the thing that sends the email")

2. **Read Radius** — how many files the agent needs to consult to reason about the change
   - 0: 1–2 files
   - 3: 10+ files or crosses module boundaries with non-trivial dependencies

3. **Edit Radius** — how many files need changes
   - 0: 1 file / one symbol
   - 3: multiple files across modules, coordinated edits

4. **Semantic Depth** — how much of the behavior requires reasoning beyond local code
   - 0: syntactic or local — rename, add a check, add an import
   - 3: requires holding invariants across async boundaries, concurrency, distributed state, or domain rules not in code

5. **Implicit Knowledge** — how much context lives outside the codebase (design docs, team conventions, past decisions, deprecation notes)
   - 0: everything needed is in the code + task description
   - 3: the task's correctness depends on knowledge that only a long-tenured team member has

A composite score helps decide:

- **Short (most dimensions ≤ 1):** Delegate. Agent-friendly.
- **Medium (dimensions mixed, one or two at 2–3):** Decompose. Split the task so the agent's part is short.
- **Long (two or more at 3):** Do it yourself, or pre-work the task until it's shorter.

Note: this is a rule of thumb, not a theorem. Override when the specific agent has strengths or weaknesses that matter (e.g., strong at semantic depth, weak on implicit knowledge).

## INPUTS
Ask the user:

1. **Task description** — one paragraph, as they'd assign it.
2. **Codebase** — language, frameworks, size (LoC order-of-magnitude).
3. **Known anchors** — files / functions / tests the task touches or starts from, if known.
4. **Relevant out-of-code knowledge** — design docs, past discussions, conventions. Or "none" if purely in-code.
5. **Agent capabilities** — model / tools / any known strengths or weaknesses.
6. **The user's own estimate** — their gut on each dimension before the score. You'll compare.

## INSTRUCTIONS

1. **Score each dimension 0–3** with a sentence of evidence.
   - Entry Points: 0 (named) / 1 (clearly locatable from description) / 2 (some search required) / 3 (ambiguous starting point)
   - Read Radius: 0 (1–2) / 1 (3–5) / 2 (6–10) / 3 (10+ or cross-module)
   - Edit Radius: 0 (1) / 1 (2–3) / 2 (4–6) / 3 (7+ or cross-module coordinated)
   - Semantic Depth: 0 (syntactic) / 1 (local behavior) / 2 (module-level invariants) / 3 (cross-boundary or domain reasoning)
   - Implicit Knowledge: 0 (all in code) / 1 (one doc) / 2 (multiple docs) / 3 (tribal knowledge)

2. **Compute composite.**
   - Sum / 15 = normalized 0–1
   - Verdict thresholds:
     - ≤ 0.25 → Delegate
     - 0.25–0.55 → Decompose
     - > 0.55 → Do It Yourself OR pre-work

   Any single dimension at 3 forces verdict ≥ Decompose regardless of composite. Two at 3 forces Do It Yourself / Pre-Work.

3. **Compare with the user's gut estimate.** Flag any dimension where gut and scored differ by ≥ 2. Those are the dimensions where the user is most likely to misjudge suitability. Brief discussion of why they might differ.

4. **If Decompose, propose a split.**
   - Which sub-task is short-distance enough to delegate?
   - Which part needs the human first (usually: narrow the entry point, write the invariant / contract, identify the semantic boundary)
   - What's the hand-off between the human pre-work and the agent task?

5. **If Delegate, propose the spec shape.** A pointer to `ai_pattern_agent_task_first_delegation_spec.md` or equivalent, with notes on which dimension to watch during execution (the highest scored one is the most likely source of drift).

6. **If Do It Yourself, name what would reduce code distance.** Would it become delegable after: adding a test? writing a design doc? refactoring for an entry point? naming the decision?

## FALSE-POSITIVE PREVENTION (MUST follow)
- Do NOT score without evidence. Each score cites something from the inputs.
- Do NOT treat long read radius as automatically bad if the reads are mechanical (e.g., rename across 20 files). Weight semantic depth higher than read radius in that case and say so.
- Do NOT give a verdict of Delegate when Implicit Knowledge is 3. That dimension alone kills most delegations.
- Do NOT skip the gut-vs-scored comparison. Calibration is part of the value.
- Do NOT propose a Decompose split that just relabels the hard part as "agent-executable."
- Do NOT assume the agent is general-purpose. If the user's agent setup has a specific strength/weakness, note where that changes the interpretation.
- DO list what would change the verdict. For Do-It-Yourself, name the delta that would flip it to Delegate.
- DO output the verdict even when it's uncomfortable ("you were about to delegate this; don't").

## OUTPUT FORMAT

### Score
| Dimension | Score (0–3) | Evidence | User's gut | Delta |
|-----------|-------------|----------|------------|-------|
| Entry Points | | | | |
| Read Radius | | | | |
| Edit Radius | | | | |
| Semantic Depth | | | | |
| Implicit Knowledge | | | | |

Composite: [sum] / 15 = [normalized]

### Verdict
**DELEGATE / DECOMPOSE / DO IT YOURSELF**

Reason (≤3 sentences): 

### If DELEGATE
- Spec shape: [link to spec template or notes]
- Dimension to watch during execution: [the highest]

### If DECOMPOSE
- Human pre-work: 
- Agent sub-task: 
- Handoff: 
- After pre-work, expected code-distance score of the agent sub-task: 

### If DO IT YOURSELF / PRE-WORK
- Delta that would make this delegable: [specific action]
- Estimate: after that delta, code-distance score would be: 

### Calibration Notes
- Dimensions where gut and scored diverged ≥ 2: 
- Likely reason: 

### Sanity Checklist
- [ ] Every dimension has a score with evidence
- [ ] Verdict rule applied (single-dimension caps honored)
- [ ] Gut-vs-scored comparison present
- [ ] If Decompose, the proposed split actually shortens code distance

## IMPORTANT
- A single 3 on Implicit Knowledge usually dominates. The agent cannot read what isn't in the codebase.
- "I'll just try it" is a valid choice when the cost of a failed delegation is low. Score it anyway — calibration compounds.
- The value of this exercise scales with how many tasks you score. Six scored tasks teach you more than one.
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — output is a scored verdict, not a general delegation discussion
- ST-02 (Structured Sequential Instructions) — 6 steps enforce score → compare → verdict → action
- RT-02 (Multi-Dimensional Analysis) — five orthogonal axes of code distance scored independently
- DS-06 (Prioritization Guidance) — explicit thresholds and single-dimension caps make verdict deterministic
- CM-02 (Constraint Specification) — Must / Must Not blocks "score it Delegate when Implicit Knowledge is 3"
- QA-01 (Chain-of-Verification) — gut-vs-scored comparison forces self-check against calibration error
