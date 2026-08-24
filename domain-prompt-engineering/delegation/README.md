# Delegation Decisions (Tool vs Colleague)

**Scope:** Prompts that decide how to delegate a task to AI (or to a human) and how to set the delegation up so it has a realistic chance of succeeding. The subfolder sits upstream of execution: it produces the mode choice, the intent spec, the verification plan, and the role-based plan — all before the work itself starts.

**When to use this subfolder:**
- You're about to hand off a task and want to pick the right mode and brief the delegate well
- A past delegation failed and you suspect the problem was upstream of the delegate
- You're designing a recurring workflow that mixes human and AI roles

**When NOT to use this subfolder:**
- You already know the task is a one-line tool-mode request (just do it)
- The task is still fuzzy at the goal level — use `domain-prompt-engineering/prompt-improvement/` or the done-definition translator first

---

## Prompts

| # | File | Role in the pipeline |
|---|------|----------------------|
| 1 | [`delegation_tool_vs_colleague_decision.md`](delegation_tool_vs_colleague_decision.md) | Decide whether to treat AI as tool or colleague (or split) for a specific task |
| 2 | [`delegation_intent_specification.md`](delegation_intent_specification.md) | Convert a one-line request into a full, self-contained intent brief with a gap list |
| 3 | [`delegation_verification_plan.md`](delegation_verification_plan.md) | Design a tiered verification plan that catches the task's actual failure modes |
| 4 | [`delegation_role_based_plan.md`](delegation_role_based_plan.md) | Map the task to named roles with explicit handoff artifacts between phases |

---

## Typical end-to-end flow

1. Start with the **mode decision** — tool, colleague, or split — so you know what kind of brief you're writing.
2. Produce the **intent specification** — the self-contained brief that the delegate can act on without you.
3. Design the **verification plan** up front, before work is delivered, so acceptance criteria aren't rationalized after the fact.
4. For larger tasks with multiple contributors, produce the **role-based plan** so nothing falls between roles.
5. Hand off to execution. If the work is iterative/gated, the done-definition subfolder provides the loop runtime.

---

## Core techniques used across this subfolder

| Technique | What it contributes |
|-----------|---------------------|
| [ST-01](../../techniques/MASTER_TECHNIQUE_INDEX.md) Clear Objective Statement | Every prompt has one job |
| [RT-02](../../techniques/MASTER_TECHNIQUE_INDEX.md) Multi-Dimensional Analysis | Factor-based mode and failure-mode breakdowns |
| [RT-03](../../techniques/MASTER_TECHNIQUE_INDEX.md) Tree of Thoughts | Forced two-option comparison in the mode decision |
| [CM-01](../../techniques/MASTER_TECHNIQUE_INDEX.md) Explicit Context Framing | Seven-question frame for intent specs |
| [CM-02](../../techniques/MASTER_TECHNIQUE_INDEX.md) Constraint Specification | Must / Must Not guardrails in every prompt |
| [DT-01](../../techniques/MASTER_TECHNIQUE_INDEX.md) Hierarchical Task Breakdown | Phased plans with inputs and outputs |
| [DD-02](../../techniques/MASTER_TECHNIQUE_INDEX.md) Vague-to-Concrete Translation | Strip adjectives from the brief |
| [QA-01](../../techniques/MASTER_TECHNIQUE_INDEX.md) Self-Verification | Pre-handoff re-read + reviewer self-check |
| [QA-08](../../techniques/MASTER_TECHNIQUE_INDEX.md) Gate-Based Verification | Pass/bounce rules in the verification plan |
| [AG-27](../../techniques/MASTER_TECHNIQUE_INDEX.md) End-State Task Specification | Outcome-framed briefs |
| [AG-28](../../techniques/MASTER_TECHNIQUE_INDEX.md) Oversight-Risk Calibration | Stakes + feedback signal drive mode, review depth, role design |

---

## Related subfolders

- [`../../domain-engineering-workflows/done-definition/`](../../domain-engineering-workflows/done-definition/) — runtime prompts for executing the delegated work once these upstream decisions are made
- [`../prompt-improvement/`](../prompt-improvement/) — improve an existing prompt (different scope; this subfolder is for delegation structure, not prompt wording)
- [`../evaluation/`](../evaluation/) — evaluation design for AI systems in general
