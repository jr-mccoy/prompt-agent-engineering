---
title: "Agent Failure Recovery & Safe Re-Scope"
category: AI-ML/agentic-ai-systems
description: "Decide what to do after a long-running agent run fails or stalls — triage the failure (transient vs systemic vs spec), then choose and execute the right recovery: resume from checkpoint, compensate-and-rerun, or adjust the task spec and continue — without losing completed work or repeating irreversible actions."
techniques:
  - ST-02
  - CM-02
  - AG-29
  - QA-12
  - QA-01
difficulty: advanced
tags:
  - failure-recovery
  - re-scoping
  - compensation
  - resume
  - reliability
updated: "2026-06-21"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_durable_execution_state_persistence.md
  - domain-AI-ML/agentic-ai-systems/aiagent_failure_mode_analysis.md
  - domain-AI-ML/agentic-ai-systems/aiagent_long_running_task_setup.md
  - domain-engineering-workflows/done-definition/done_definition_loop_troubleshooter.md
  - domain-engineering-workflows/done-definition/done_definition_stop_policy.md
  - domain-AI-ML/agentic-ai-systems/aiagent_human_in_the_loop_design.md
---

# Agent Failure Recovery & Safe Re-Scope

**Objective:** Given a long-running agent run that has failed, stalled, or hit its stop policy, decide the correct next move — **resume** from the last good checkpoint, **compensate-and-rerun** the affected steps, or **re-scope** the task and continue — and execute it without losing completed work or repeating irreversible actions. This is the *decision-and-action* layer that sits after diagnosis: a troubleshooter tells you *why* a loop failed; this prompt decides *what to do about it* and how to do it safely.

**When to Use:**
- A long-running run crashed, timed out, exceeded its budget, hit its iteration cap, or is thrashing.
- The run produced wrong or partial output and you must decide whether to resume, undo, or change the task.
- A run is "stuck" and naive restart-from-scratch would lose hours of work or repeat irreversible actions.

**When NOT to Use:**
- You only need to *diagnose* why the loop failed — use `done_definition_loop_troubleshooter.md` first, then return here.
- The task is cheap to re-run from scratch — just re-run.
- You are designing durability/checkpoints up front (before any failure) — use `aiagent_durable_execution_state_persistence.md`.

## Inputs / Context

Provide what you can:
- **Failure signal** — what happened (crash, timeout, budget/iteration cap, wrong output, stall) and any error/trace.
- **Run state** — last checkpoint, completed steps, outstanding/ambiguous actions, current cursor/plan position.
- **Side-effect ledger** — which irreversible actions already fired and whether they're confirmed.
- **Original spec / done-definition** — what the task was supposed to achieve and its acceptance gates.
- **Constraints** — remaining budget, deadline, and what changes to the spec are permissible.

## Constraints

**Must:**
- Triage the failure into a class before acting: **transient** (rate-limit/network/crash), **systemic** (tool/data/environment defect), or **spec** (the task or done-definition was wrong/ambiguous/infeasible).
- Reconcile the side-effect ledger first — determine which irreversible actions actually completed before choosing a recovery.
- Choose exactly one primary recovery path — resume, compensate-and-rerun, or re-scope — with a stated reason tied to the failure class.
- Preserve completed, still-valid work; never restart from scratch when resume/compensation can save it.
- If re-scoping, state precisely what in the spec/done-definition changes and confirm prior completed work is still valid under the new spec (or is explicitly invalidated/compensated).

**Must Not:**
- Blindly retry from scratch after a mid-action crash whose outcome is unknown (may double-fire irreversible actions).
- Re-scope to make a failing run "pass" by weakening the acceptance gate without justification (moving the goalposts).
- Resume on top of a corrupted or poisoned state without validating it.
- Treat a systemic failure as transient (endless retries that can't succeed) or a spec failure as systemic (fixing tools when the task was wrong).

**Instructions:**

1. **Reconcile state and the side-effect ledger.** From the last checkpoint, determine completed steps and which irreversible actions confirmed. Resolve ambiguous actions by their operation key (query for completion) — never assume.
2. **Classify the failure.** Transient (retry-able), systemic (a defect in tool/data/environment that retrying won't fix), or spec (the task/done-definition was ambiguous, wrong, or infeasible). State the evidence for the class.
3. **Choose the recovery path:**
   - **Resume** — for transient failures with intact state: continue from the last good checkpoint (idempotency guards prevent double-effects).
   - **Compensate-and-rerun** — for systemic failures or corrupted partial progress: run compensating actions (reverse order) to undo committed effects past the pivot, then rerun the affected segment with the defect fixed.
   - **Re-scope** — for spec failures: adjust the task/done-definition (narrow scope, fix ambiguity, split into sub-tasks, relax an infeasible constraint with justification), then continue.
4. **If resuming:** confirm the loaded state is valid (not corrupted/poisoned), confirm idempotency guards are in place, and set/adjust the stop policy so the same failure can't loop indefinitely.
5. **If compensating:** list the committed irreversible actions to undo, their compensating actions, the reverse order, and a check that each compensation succeeded (compensations can themselves fail — monitor and alert).
6. **If re-scoping:** write the precise spec delta (before → after), confirm which completed work remains valid under the new spec, mark what must be invalidated/compensated, and re-run the relevant acceptance gates.
7. **Set the re-run guardrails.** Adjust budget/iteration caps and stop policy so the retry is bounded; define what escalates to a human if recovery itself fails.
8. **Record the recovery.** Capture the failure class, chosen path, spec delta (if any), and outcome so the pattern feeds failure-mode analysis and future setup.

**Output Format:**

A markdown recovery decision + action plan:
- **State Reconciliation** — completed steps; confirmed vs ambiguous irreversible actions
- **Failure Classification** — transient / systemic / spec + evidence
- **Recovery Decision** — resume / compensate-and-rerun / re-scope + reason
- **Action Plan** — concrete steps for the chosen path (resume point | compensations in order | spec delta)
- **Validity Check** — which completed work survives; what is invalidated
- **Re-run Guardrails** — adjusted caps, stop policy, escalation
- **Recovery Record** — for failure-mode feedback

## Verification

- [ ] The side-effect ledger is reconciled; no irreversible action will be repeated on recovery.
- [ ] The failure is classified (transient/systemic/spec) with evidence, and the path matches the class.
- [ ] Exactly one primary recovery path is chosen, with a stated reason.
- [ ] Completed, still-valid work is preserved (no needless restart-from-scratch).
- [ ] If re-scoping, the spec delta is explicit and the acceptance gate was not weakened just to force a pass.
- [ ] Re-run guardrails (caps, stop policy, escalation) prevent the same failure from looping.

## False-Positive Prevention

❌ **DON'T:**
- Retry from scratch after a mid-action crash without checking whether the action already succeeded.
- Re-scope by quietly lowering the done-definition so a broken run "passes."
- Resume onto state you haven't validated (it may be corrupted or poisoned).
- Keep retrying a systemic failure that no amount of retries can fix.
- Discard hours of valid completed work because one late step failed.

✅ **DO:**
- Reconcile by operation key before any resume; treat ambiguous actions as "verify, don't repeat."
- Match the recovery path to the failure class; justify any spec change explicitly.
- Validate loaded state before resuming; run compensations in reverse order and confirm each.
- Preserve still-valid completed work; only re-run the affected segment.
- Bound the retry and define a human-escalation path if recovery itself fails.

## Example Output

```markdown
## Recovery Decision: Data-Migration Agent stalled at 18,402/25,000 records (sent 2 notify emails)

### State Reconciliation
Checkpoint at record 18,402. Completed: 18,402 migrated. Irreversible: 2 "migration-complete" emails — both confirmed in sent_actions by op-key. 1 in-flight write to record 18,403 ambiguous → query shows NOT committed.

### Failure Classification
Systemic: source schema changed at record ~18,400 (new nullable column) → mapper throws. Retrying as-is can't succeed.

### Recovery Decision
Compensate-and-rerun the affected segment. Reason: defect is in the mapper (systemic); records 1–18,402 are valid; no need to re-scope the task.

### Action Plan
1. No compensation needed for migrated records (idempotent upsert). 2. Roll back ambiguous record 18,403 (not committed → no-op). 3. Patch mapper for nullable column. 4. Resume from cursor 18,403.

### Validity Check
Records 1–18,402 valid and retained. 2 emails already correctly sent. Nothing invalidated.

### Re-run Guardrails
Cap: stop + escalate if >5 consecutive mapper errors. Budget unchanged. Escalate to data-eng if schema drifts again.

### Recovery Record
Class=systemic(schema drift); path=compensate-and-rerun; spec unchanged; outcome=resumed.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** reconcile → classify → choose → execute → guardrail → record.
- **CM-02 (Constraint Specification):** the failure class and "preserve valid work / don't weaken the gate" rules govern the decision.
- **AG-29 (Agent Loop Architecture):** recovery is expressed in terms of checkpoints, pivots, and the control loop's stop policy.
- **QA-12 (False Positives Identification):** ledger reconciliation prevents double-firing; the no-goalpost-moving rule prevents false "passes."
- **QA-01 (Self-Verification):** the checklist enforces class-matched recovery and preserved work.

**Related Prompts:**
- `done_definition_loop_troubleshooter.md` — diagnose *why* the loop failed (run first).
- `aiagent_durable_execution_state_persistence.md` — the checkpoints/idempotency this recovery relies on.
- `aiagent_failure_mode_analysis.md` — feed the recovery record back into failure-mode design.
- `aiagent_long_running_task_setup.md` — the setup whose runs this prompt recovers.
