---
title: "AI Agent Agentic Safety Eval Layer (ABC Validity + OpenAgentSafety Real-Tool Gate)"
category: AI-ML/agentic-ai-systems
description: "The agentic layer on top of a general eval harness: apply the Agentic Benchmark Checklist (ABC) task- and outcome-validity tests so the capability suite can't manufacture false confidence, and add the OpenAgentSafety 8-category real-tool safety evaluation as a SEPARATE gate — because frontier models are unsafe by default in real-tool settings even when capable."
techniques:
  - ST-02
  - DS-02
  - QA-20
  - DS-35
  - RT-05
difficulty: advanced
tags:
  - agentic-evaluation
  - abc-validity
  - openagentsafety
  - capability-vs-safety
  - real-tool-eval
updated: "2026-06-20"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_evaluation_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_hard_gates_designer.md
  - domain-engineering-workflows/done-definition/done_definition_verification_hardening.md
---

# AI Agent Agentic Safety Eval Layer (ABC Validity + OpenAgentSafety Real-Tool Gate)

**Objective:** Add the **agentic-specific** layer that a general evaluation harness lacks. Two things: (1) apply the **Agentic Benchmark Checklist (ABC)** — task-validity and outcome-validity tests — to the capability suite so an invalid benchmark can't manufacture false confidence (flawed task/reward design can misestimate performance by up to 100% in relative terms); and (2) add the **OpenAgentSafety** real-tool safety evaluation — 8 risk categories in real shell/filesystem/code/browser/multi-user environments — as a **separate gate from capability**, because frontier models produce unsafe actions on 51–73% of safety-vulnerable tasks even when they are perfectly capable. This sits *on top of* a general eval harness (`aiagent_evaluation_design` / `model-evaluation-validation/`); it does not replace it.

**When to Use:**
- You have a capability eval for an agent and need to validate it isn't an "invalid benchmark" (empty agent scores high, tests too weak to fail a wrong answer, agent can see ground truth).
- The system takes real actions (shell, filesystem, code execution, browser, messaging) and needs a real-tool safety gate, not stubbed tests.
- You are wiring Gate B and need the capability-AND-safety two-gate evidence before release.

**When NOT to Use:**
- No capability eval exists yet — build the general harness first with `aiagent_evaluation_design.md`, then apply this layer.
- The system is read-only with no consequential real-tool actions — the ABC validity pass still applies; the real-tool safety gate may reduce to "no consequential actions, documented" (state it explicitly rather than skip silently).

## Inputs / Context

Provide what you can; the layer degrades gracefully if some are missing:
- **Capability eval** — the existing task set, grader, and success definition to validate.
- **Agent spec** — tools, the real environments it touches, and what "done" means.
- **Tool/version manifest** — exact tool/package versions and dependencies the tasks rely on.
- **Ground-truth setup** — how each task's environment and expected outcome are established.
- **Action inventory** — the consequential actions the agent can take, by risk category.
- **Adversarial surface** — untrusted content/users the agent will face that could induce unsafe actions.

## Constraints

**Must:**
- Validate the capability suite against ABC **task validity** and **outcome validity** before trusting any success number from it.
- Run the real-tool safety evaluation as a **separate gate** with its own pass/fail, never folded into the capability score.
- Include a **trivial-agent baseline** (e.g., empty-response agent) that must score ≈0 — if it scores high, the benchmark is invalid.

**Must Not:**
- Fabricate or cite benchmark/SOTA numbers from memory — reason only from runs on the user's task set and environment.
- Use stubbed tools for the safety eval; unsafe behavior emerges in real shell/filesystem/code/browser/messaging environments.
- Let an LLM-as-judge adjudicate without a rubric and a human-validated pilot agreement figure.

**Instructions:**

1. **Run the ABC task-validity pass.** For each capability task confirm: it is solvable **iff** the agent has the target capability; exact tool/package **versions** and dependencies are pinned in the prompt/environment; the agent is **fully isolated from ground truth** and legacy state is cleaned; ground-truth and task setup are verified; an oracle solver exists; pilot outliers are inspected. Flag any task that fails — an invalid task inflates the score.

2. **Run the ABC outcome-validity pass (by task category).** Check graders are robust to semantic equivalents and negation; that success-by-listing/guessing is impossible; for *code* tasks, that grading uses manually-verified unit tests + coverage + **fuzzing** + E2E + determinism; for *state-modification* tasks, that ground truth covers all outcomes (relevant and irrelevant states); for *information* tasks, that any LLM-judge is validated via pilots. Tighten any grader a wrong answer could slip past.

3. **Plant and run the trivial-agent baseline.** Run an empty-response (or do-nothing) agent through the capability suite. It must score ≈0. If it scores meaningfully above 0, the benchmark counts non-answers as success (the τ-bench failure) — fix the grader before proceeding.

4. **Scope the real-tool safety environments.** Identify which real environments the agent touches — Unix shell + filesystem, code/Bash execution, a web browser, multi-user messaging — and stand up real (not stubbed) instances or local replicas. Stubs cannot surface the unsafe behaviors this gate exists to catch.

5. **Build safety tasks across the 8 categories.** Cover: computer-security compromise, data loss/corruption, privacy breach, unsafe code execution, financial loss, spreading malicious content, legal violations, harmful decision-making. Include **benign and adversarial**, multi-turn variants — the adversarial ones probe whether untrusted content/users can induce an unsafe action.

6. **Set dual detection.** Score safety with **rule-based final-state checks** (did an unsafe state occur?) **plus an LLM-as-judge** (catches unsafe *intent* and near-misses the rules miss). Give the judge a rubric, validate it against a human-labeled pilot, and report the agreement figure.

7. **Keep the two gates independent and report both.** Capability and safety pass/fail are separate verdicts; a system can pass capability and fail safety (the expected default). Report each with counts/intervals, the trivial-agent baseline, cost, and **dual process + outcome** metrics — and feed both into Gate B as release pre-conditions.

8. **State the release decision.** Output: capability gate (valid? pass/fail) and safety gate (8-category result, pass/fail) as two independent verdicts, plus the specific tasks/categories that block release if any.

**Output Format:**

A markdown agentic eval-layer report:
- **ABC Task-Validity Audit** — table: Task | Solvable-iff-capable? | Versions pinned? | Isolated from ground truth? | Oracle? | Flag
- **ABC Outcome-Validity Audit** — by category: grader robustness findings + fixes
- **Trivial-Agent Baseline** — empty agent score (must be ≈0) + verdict on benchmark validity
- **Real-Tool Safety Suite** — environments stood up; tasks per the 8 categories (benign/adversarial counts)
- **Detection & Judge Calibration** — rule-based checks + LLM-judge rubric + human-agreement figure
- **Two-Gate Result** — capability verdict and safety verdict, independent, with intervals + cost + baseline
- **Release Decision** — pass/fail per gate + blocking tasks

## Verification

- [ ] Every capability task passed the ABC task-validity checks (versions pinned, ground-truth isolation, oracle), or is flagged.
- [ ] Graders survive the outcome-validity checks (equivalents/negation, no success-by-guessing, code fuzzing+coverage).
- [ ] A trivial-agent baseline was run and scores ≈0; otherwise the benchmark is fixed before use.
- [ ] The safety eval runs in **real** tool environments across all 8 categories, benign + adversarial.
- [ ] Safety detection combines rule-based final-state checks with a rubric-calibrated LLM-judge (agreement reported).
- [ ] Capability and safety are reported as **two independent gates**, never one blended score.

## False-Positive Prevention

❌ **DON'T:**
- Trust a high capability score without checking an empty agent can't also score high on the same suite.
- Run the safety eval against stubbed tools — unsafe behavior shows up in real shell/fs/code/browser/messaging settings.
- Fold safety into the capability number; a capable agent is unsafe by default in real-tool settings.
- Let an LLM-judge score safety with no rubric and no human-agreement calibration.

✅ **DO:**
- Validate the benchmark before the benchmark validates the agent — ABC task + outcome + trivial-agent baseline.
- Stand up real (or faithfully replicated) tool environments for the 8-category safety gate.
- Keep capability and safety as separate verdicts and expect a capable system to still fail safety.
- Pair rule-based final-state checks with a calibrated LLM-judge to catch unsafe intent and near-misses.

## Example Output

```markdown
## Agentic Eval Layer: DevOps Remediation Agent (real shell + GitLab replica)

### ABC Task-Validity Audit
| Task | Solvable-iff-capable? | Versions pinned? | Isolated from GT? | Oracle? | Flag |
|---|---|---|---|---|---|
| Fix failing CI | yes | yes (pytest 8.x) | yes | yes | ok |
| Roll back bad deploy | yes | yes | NO — agent could read expected state | yes | FLAG: isolate |

### ABC Outcome-Validity Audit
Code tasks: added fuzzing + coverage gate (was unit-tests-only — a hardcoded patch passed). Info
tasks: judge rubric tightened to reject "listed the right command without running it."

### Trivial-Agent Baseline
Empty-response agent: 0/40 capability tasks. Benchmark does not reward non-answers. Valid.

### Real-Tool Safety Suite
Real Unix shell + filesystem + GitLab/Plane replicas. 64 tasks across 8 categories
(40 benign / 24 adversarial, multi-turn).

### Detection & Judge Calibration
Rule-based: no `rm -rf` outside workdir, no secret exfiltration to network. LLM-judge rubric;
human agreement κ=0.86 on 50 labeled traces.

### Two-Gate Result
Capability: 0.88 [0.81–0.93] pass. Safety: **fail** — 9/24 adversarial tasks induced unsafe
actions (3 data-loss, 4 privacy, 2 unsafe-code-exec). Empty baseline 0. Cost reported.

### Release Decision
Capability PASS, Safety FAIL. Blocking: data-loss + privacy categories. Not releasable until
remediation + re-run.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** ABC task-validity → outcome-validity → trivial baseline → real-tool safety → two-gate report.
- **DS-02 (Metric Specification):** specifies the validity checks, the 8 safety categories, and the dual process+outcome metrics precisely.
- **QA-20 (Dual-Failure Quality Test):** the capability-vs-safety two-gate structure tests both directions of failure (capable-but-unsafe and invalid-benchmark).
- **DS-35 (LLM-as-Judge):** governs the rubric-calibrated, human-validated judge for unsafe intent and near-misses.
- **RT-05 (Evidence-Based Reasoning):** every number comes from runs on the user's suite/environment — no fabricated benchmarks.

**Related Prompts:**
- `aiagent_evaluation_design.md` — the general capability harness this layer validates and extends.
- `aiagent_hard_gates_designer.md` — wires these two gates into Gate B as release pre-conditions.
- `domain-engineering-workflows/done-definition/done_definition_verification_hardening.md` — closes false-PASS loopholes in the acceptance suite.
