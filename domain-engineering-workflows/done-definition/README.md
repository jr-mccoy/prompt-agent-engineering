# Done Definition & Convergence

**Scope:** Prompts that turn fuzzy tasks into bounded, convergent agentic work. Each prompt operates on a specific stage of the done-definition pipeline: translate the task into gates, bound the loop with a stop policy, run the loop with self-audits, harden against false-done, pick a domain-appropriate gate baseline, or troubleshoot a loop that failed.

**When to use this subfolder:**
- You're about to delegate a task to an agent and want it to stop at the right moment
- You have a recurring artifact type (refactor, postmortem, summary) and want a consistent gate set
- A prior loop shipped wrong work, ran too long, or couldn't tell it had converged

**When NOT to use this subfolder:**
- The task is a single-shot request with no iteration (use a regular prompt)
- The task is pure judgment with no checkable component (use `domain-prompt-engineering/delegation/` or a human review workflow)

---

## Prompts

| # | File | Role in the pipeline |
|---|------|----------------------|
| 1 | [`done_definition_translator.md`](done_definition_translator.md) | Convert a fuzzy task into a concrete gate table with evidence + location |
| 2 | [`done_definition_stop_policy.md`](done_definition_stop_policy.md) | Design the iteration budget, escalation triggers, and diagnostic rules |
| 3 | [`done_definition_loop_operator.md`](done_definition_loop_operator.md) | Run the work → check → retry → ship loop per iteration |
| 4 | [`done_definition_verification_hardening.md`](done_definition_verification_hardening.md) | Tighten gates so an agent can't claim PASS without real evidence |
| 5 | [`done_definition_gate_sets_by_domain.md`](done_definition_gate_sets_by_domain.md) | Pre-built baseline gate sets for six common artifact types |
| 6 | [`done_definition_loop_troubleshooter.md`](done_definition_loop_troubleshooter.md) | Diagnose why a loop failed and prescribe the upstream repair |

---

## Typical end-to-end flow

1. Use the **translator** on the fuzzy task to produce a first-pass gate table.
   - OR, if the artifact is one of the six domains, start with **gate_sets_by_domain** and tune from there.
2. Run **verification hardening** against the gate set (especially for high-stakes work).
3. Design the **stop policy** (budget + escalation triggers) before launching the loop.
4. Run the **loop operator** with the gate set + stop policy.
5. If the loop fails (ships wrong work, stalls, thrashes, or grinds without progress), use the **troubleshooter** to classify the failure and prescribe an upstream repair — almost always in one of the first three prompts, not in the loop operator itself.

---

## Core techniques used across this subfolder

| Technique | What it contributes |
|-----------|---------------------|
| [DD-02](../../techniques/MASTER_TECHNIQUE_INDEX.md) Vague-to-Concrete Translation | Adjective → noun/verb gate |
| [DD-04](../../techniques/MASTER_TECHNIQUE_INDEX.md) MVP Gates | Top-3 highest-leverage gates |
| [DD-05](../../techniques/MASTER_TECHNIQUE_INDEX.md) Human Review Flags | Separates checkable gates from judgment |
| [DD-06](../../techniques/MASTER_TECHNIQUE_INDEX.md) Iteration Control | Budget + stop + escalation + diagnostics |
| [DD-07](../../techniques/MASTER_TECHNIQUE_INDEX.md) Self-Audit Table | Evidence + location per gate each iteration |
| [DD-10](../../techniques/MASTER_TECHNIQUE_INDEX.md) Change Log Iteration | Per-iteration log with diagnostic signal |
| [DD-11](../../techniques/MASTER_TECHNIQUE_INDEX.md) BLOCKED Protocol | Missing-input as a first-class escalation |
| [QA-08](../../techniques/MASTER_TECHNIQUE_INDEX.md) Gate-Based Verification | Binary pass/fail gates anchor the loop |
| [AG-27](../../techniques/MASTER_TECHNIQUE_INDEX.md) End-State Task Specification | Outcomes + verification, not steps |
| [AG-28](../../techniques/MASTER_TECHNIQUE_INDEX.md) Oversight-Risk Calibration | Stakes × feedback sizes the budget |
| [AG-29](../../techniques/MASTER_TECHNIQUE_INDEX.md) Agent Loop Architecture | Full cycle + exit + checkpoint + stuck detection |

---

## Related subfolders

- [`../ai-patterns/`](../ai-patterns/) — adjacent workflow prompts for AI-assisted development
- [`../../domain-prompt-engineering/delegation/`](../../domain-prompt-engineering/delegation/) — deciding whether to delegate and how to specify intent before the loop runs
