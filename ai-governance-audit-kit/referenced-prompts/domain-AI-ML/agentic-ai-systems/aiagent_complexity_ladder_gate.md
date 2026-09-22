---
title: "AI Agent Complexity-Ladder Gate (Does This Need an Agent At All?)"
category: AI-ML/agentic-ai-systems
description: "The Gate-0 decision before any agent design: force a use case down the complexity ladder — deterministic function → single model call → code-controlled workflow → agent → multi-agent — and stop at the lowest rung that reliably meets the requirement, with a written justification when an agent is genuinely earned."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - AG-14
  - QA-01
difficulty: advanced
tags:
  - complexity-ladder
  - workflow-vs-agent
  - agent-justification
  - least-agency
  - gate-zero
updated: "2026-06-20"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_multi_agent_orchestration.md
  - domain-AI-ML/agentic-ai-systems/aiagent_least_agency_scoping.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_code_distance_scorer.md
---

# AI Agent Complexity-Ladder Gate (Does This Need an Agent At All?)

**Objective:** Before any architecture, topology, or tool design, answer the prior question every credible source leads with — *does this use case need an agent at all, or can a lower rung of the complexity ladder do it more cheaply and reliably?* Walk the ladder in order (deterministic function → single model call → code-controlled workflow → single agent → multi-agent), stop at the lowest rung that reliably meets the requirement, and either (a) recommend that lower rung and STOP, or (b) produce a one-sentence written justification that an agent is genuinely required. Ending the exercise with "use a workflow" is a success, not a failure.

**When to Use:**
- Someone has asked for "an agent" or "a multi-agent system" and you want to test whether the complexity is earned before designing it.
- You are at Step 0 of the agentic-system authoring process and need the written justification the architecture doc requires.
- A design already exists and feels heavier than the problem (an agent where a workflow, or multi-agent where a single agent, would do).

**When NOT to Use:**
- The agent decision is already justified and recorded, and you now need the topology or architecture (use `aiagent_orchestration_topology_selection.md` / `aiagent_architecture_design.md`).
- The question is specifically single-agent *vs.* multi-agent — that is the next rung down; use `aiagent_multi_agent_orchestration.md` (this gate gets you to "an agent is justified" first).

## Inputs / Context

Provide what you can; the gate degrades gracefully if some are missing:
- **Use case** — one sentence on the job-to-be-done and who/what consumes the output.
- **Inputs & outputs** — types, formats, volume, and which inputs are untrusted external content.
- **Variability** — is the number/order of steps and the tool choice knowable in advance, or does it depend on intermediate results?
- **Success criterion** — the observable check that says the task is done.
- **Blast radius** — the worst action the system could take (sends money? deletes data? emails customers?).
- **Constraints** — cost/latency ceilings, reliability needs, and any deadline pressure favoring the simplest path.

## Constraints

**Must:**
- Evaluate the rungs **in order, lowest first**, and stop at the first rung that reliably meets the requirement — never start by assuming an agent.
- Name a concrete reason the *current* rung fails before climbing to the next; "might need flexibility later" is not a reason.
- Produce the required justification sentence verbatim if and only if an agent is reached, or recommend the lower rung explicitly and stop.

**Must Not:**
- Climb the ladder for fashion, future-proofing, or "to be safe" — escalating complexity expands cost and attack surface without adding value (the Least-Agency principle).
- Treat "the task has multiple steps" as evidence it needs an agent — code-controlled workflows run multiple steps deterministically.
- Recommend multi-agent to hedge against single-agent risk; multi-agent is ~15× the tokens and harder to make safe.

**Instructions:**

1. **Restate the task as an observable outcome.** One sentence: what verifiable artifact or state change counts as done. If you cannot, scoping is the real gap — return that, not an agent.

2. **Rung 1 — deterministic function / rule.** Ask: can a function or hardcoded rule produce this output? If yes, write the function. STOP — no LLM at all. (E.g., a lookup, a regex, a formula, a state machine.)

3. **Rung 2 — single model call (augmented).** Ask: can one LLM call, optionally plus retrieval and one tool, do this reliably? If yes, this is a *direct call* — author it as a **prompt**, not a system. STOP.

4. **Rung 3 — code-controlled workflow.** Ask: does the task decompose into a known, fixed set of steps whose order and branching **code** can decide (prompt chain, deterministic router, parallel fan-out/aggregate, generator→evaluator)? If yes, build the **workflow** — control flow stays in code. STOP unless runtime dynamism is genuinely required.

5. **Rung 4 — single agent (the model controls the loop).** Climb here only if the number/order of steps or the tool choice is **not knowable in advance** and must be decided by the model at runtime. If so, a single agent is justified. Continue to step 6 only if a single agent demonstrably cannot do it.

6. **Rung 5 — multi-agent.** Reach here only when a single agent provably fails (tool overload, context overflow, privilege conflicts, or independent parallelizable breadth). Hand off to `aiagent_multi_agent_orchestration.md` for the single-vs-multi decision — do not assume it here.

7. **Apply the cost reality as back-pressure.** State the cost multiple of the recommended rung (single agent ≈ 4× a chat turn; multi-agent ≈ 15×) and confirm the value justifies it. If a lower rung is within reach, prefer it.

8. **Record the decision and the justification.** Output the chosen rung, the reason each lower rung was rejected, and — if an agent is reached — the required sentence. If the answer is a workflow, say so plainly and point to where it should be built.

**Output Format:**

A markdown gate decision:
- **Task as Observable Outcome** — the one-sentence done-check
- **Ladder Walk** — table: Rung | Could it do this? | Reason rejected / accepted
- **Recommended Rung** — function / direct-call prompt / workflow / single agent / multi-agent
- **Cost Multiple & Value Check** — the multiplier and whether value justifies it
- **Agent Justification Sentence** — present only if an agent is reached (verbatim template below), else "N/A — lower rung recommended"
- **Next Step** — the specific prompt/build target for the recommended rung

The justification sentence (fill the blanks, record verbatim if an agent is reached):
> *"An agent is required because ____ (the number/order of steps is not knowable in advance / tool choice depends on intermediate results / the task needs runtime replanning), and a deterministic workflow cannot because ____."*

## Verification

- [ ] The rungs were evaluated lowest-first and the walk stops at the first sufficient rung.
- [ ] Each climb past a rung names a concrete failure of that rung, not future-proofing.
- [ ] If an agent is recommended, the justification sentence is completed honestly; if not, a lower rung is named and the exercise stops.
- [ ] The cost multiple of the recommended rung is stated and value-justified.
- [ ] "Multiple steps" is never used as the sole reason to climb to an agent.
- [ ] The next build target matches the recommended rung (prompt vs workflow vs agent).

## False-Positive Prevention

❌ **DON'T:**
- Start at "what kind of agent?" and rationalize backward — that skips the only question that matters here.
- Call a fixed draft→review→polish sequence "an agent" because it has steps; that is a code-controlled workflow.
- Climb to an agent because the requirements *might* change later — build for the requirement you have.
- Reach for multi-agent to reduce risk; it adds coordination failure modes and ~15× cost.

✅ **DO:**
- Force the task down to the cheapest rung that reliably works and stop there.
- Treat "use a workflow / write a prompt / write a function" as the most common and most successful outcome.
- Make each climb earn itself with a named failure of the rung below.
- Hand the single-vs-multi question to the dedicated prompt only after an agent is justified.

## Example Output

```markdown
## Complexity-Ladder Gate: "Triage inbound support tickets and draft replies"

### Task as Observable Outcome
For each ticket, produce a category label + a draft reply that a human approves before send.

### Ladder Walk
| Rung | Could it do this? | Reason rejected / accepted |
|---|---|---|
| 1 Function/rule | Partly | Keyword rules misclassify nuanced tickets — fails on accuracy |
| 2 Single model call | Yes for classify+draft per ticket | Each ticket is independent; one augmented call labels + drafts |
| 3 Workflow | Not needed | No fixed multi-step pipeline beyond the single call + a human gate |
| 4 Single agent | No | No runtime-unknown step count or dynamic tool choice — nothing to loop over |
| 5 Multi-agent | No | Single call suffices |

### Recommended Rung
**Rung 2 — single model call** per ticket (classify + draft), behind a human approval gate. Author as a prompt, not a system.

### Cost Multiple & Value Check
~1× a chat turn per ticket. An agent loop here would add ~4× cost for zero capability gain.

### Agent Justification Sentence
N/A — lower rung recommended.

### Next Step
Author a Tier-1 classification+drafting prompt; wire the human approval gate in code. No agent.
```

**Techniques Used:**
- **ST-01 (Clear Objective Statement):** restates the task as one observable done-check before any rung is considered.
- **ST-02 (Structured Sequential Instructions):** the ladder is walked in a fixed lowest-first order, gating each climb.
- **CM-02 (Constraint Specification):** the must/must-not rules forbid climbing for fashion or future-proofing.
- **AG-14 (Cost-Aware Agent Orchestration):** the 4×/15× cost multiples are applied as back-pressure against escalation.
- **QA-01 (Chain-of-Verification):** the verbatim justification sentence forces evidence that an agent is genuinely required.

**Related Prompts:**
- `aiagent_multi_agent_orchestration.md` — the next rung down: single-agent vs. multi-agent, once an agent is justified.
- `aiagent_least_agency_scoping.md` — apply least-agency *within* a system once the agent rung is chosen.
- `domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_code_distance_scorer.md` — Delegate / Decompose / DIY scoring for a task already destined for an agent.
