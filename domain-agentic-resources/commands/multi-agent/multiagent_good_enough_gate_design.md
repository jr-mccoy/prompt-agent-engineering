---
name: multiagent_good_enough_gate_design
description: "Translate fuzzy acceptance into a mix of pass/fail gates (must-pass) and graded criteria (scored). Prevents the two failure modes: ship-on-vibes and never-ship-because-perfect."
version: "1.0.0"
category: multi-agent
tags: [design, enough, gate, good, multi-agent, multiagent]
agents_used: []
title: "Define 'Good Enough' via Pass/Fail Gates and Graded Criteria"
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DD-04
  - DD-02
  - QA-08
difficulty: intermediate
updated: "2026-04-20"
related_prompts:
  - domain-agentic-resources/commands/multi-agent/multiagent_two_tier_architecture_template.md
  - domain-agentic-resources/commands/multi-agent/multiagent_coordination_via_tests_and_policy.md
  - domain-engineering-workflows/done-definition/done_definition_translator.md
---
# Define "Good Enough" via Pass/Fail Gates and Graded Criteria

**Purpose:** Multi-agent systems need two kinds of acceptance criteria: **pass/fail gates** that are non-negotiable (fail any → not done) and **graded criteria** that allow a "good enough" band (score within range → accept; below → iterate). Mixing these up produces either gate-bloat (everything is pass/fail, so nothing ships) or gate-rot (too much graded, so low-quality output passes). This prompt produces the right mix for a specific task and makes each criterion mechanically checkable.

**When to use:**
- A judge / reviewer agent is either too lenient (accepts low-quality) or too strict (rejects acceptable work)
- Your acceptance is currently "looks good" — not a criterion anyone can check
- You're designing a convergence loop and need the stop condition
- The same output needs to pass CI-style binary gates and also hit a quality score
- A grading rubric is in play and you need to separate hard floors from graded bands

**What you'll get:** A set of pass/fail gates (exhaustive list of not-negotiable failures), a set of graded criteria with scoring rules and a minimum acceptable score, a tie-breaker policy, and the structured verdict the judge will emit.

---

```
## ROLE
You design the acceptance contract for a multi-agent (or single-agent) task. You produce two lists: pass/fail gates (binary, exhaustive, cheap-to-check) and graded criteria (scored, weighted, produce a composite). You do NOT produce the task's work itself. The contract is the downstream judge's checklist.

## CONTEXT
Pass/fail gates and graded criteria are not interchangeable.

- **Pass/fail** is for facts the world refuses to negotiate: tests pass, schema is valid, no secrets committed, no deprecated API used, no unresolved TODOs in the diff.
- **Graded** is for quality where more-is-better up to a point: clarity of explanation, code readability, thoroughness of a research summary, coverage of a test suite beyond a floor.

Two common failures:
1. **Gate bloat:** treating every preference as a pass/fail. Every iteration fails on something minor. The loop never closes.
2. **Gate rot:** treating everything as graded. Real hard requirements get weighted-averaged away.

A good contract has 3–7 gates and 3–7 graded criteria, each checkable, with a clear aggregation rule.

## INPUTS
Ask the user:

1. **The task the output satisfies** — one paragraph.
2. **Current acceptance language** — copy/paste what the team is already using. Usually too fuzzy.
3. **Non-negotiables** — things that are absolutely required (security, compliance, contracts, regressions banned).
4. **Quality axes that matter** — what "better" looks like beyond the non-negotiables.
5. **Who checks** — agent / human / both. If agent, what tools does it have (tests, linters, scoring rubrics)?
6. **Iteration budget** — how many handback cycles are tolerable before escalation.

## INSTRUCTIONS

1. **Separate inputs into gates vs graded.** For each item in the current acceptance language or non-negotiables / quality axes:
   - If failure means "do not ship under any circumstance," it's a gate
   - If failure means "this could be better but could also ship," it's graded
   - If unclear, ask: "would a team with a reasonable bar ship this output if everything else passed but this was weak?" — yes ⇒ graded, no ⇒ gate

2. **Write each gate** as a binary check:
   - **Statement:** observable fact about the output (not the process)
   - **Check:** the exact command / test / tool / human action that produces pass or fail
   - **Evidence location:** where the check's output lives (test file, CI log, lint report, manual reviewer note)
   - **Reason:** why this must be a gate, not graded
   
   Cap gates at 7. If there are more, some are graded in disguise.

3. **Write each graded criterion** as a scored check:
   - **Statement:** the quality axis
   - **Scale:** 0–3 or 0–5, each level defined concretely (what does a 3 look like that a 2 doesn't?)
   - **Weight:** numeric, summing to 100 across all graded criteria
   - **Evidence location:** same as gates — specific
   - **Floor:** the minimum score on this criterion alone that would block accept (e.g., "no criterion below 1")
   
   Cap graded at 7. If there are more, consolidate or drop.

4. **Define the aggregation rule.**
   - Composite score = Σ (criterion_score × weight) / max_possible
   - Minimum acceptable composite = [user-defined threshold]
   - Floors enforced: any criterion below its floor ⇒ fail regardless of composite
   - Gates are AND (all must pass)

5. **Define the verdict schema** the judge emits. Example:
   ```
   verdict: ACCEPT | HANDBACK | ESCALATE
   gates:
     - id: gate1
       passed: true|false
       evidence: "..."
   graded:
     - id: g1
       score: 0-N
       evidence: "..."
   composite: 0.0-1.0
   min_required: 0.0-1.0
   reason: "concise rationale"
   ```

6. **Define the tie-breaker / handback rule.** When gates pass but composite is below threshold:
   - Which criterion's weakness is the primary reason?
   - What specific hint goes back to the worker? (not "improve clarity" — "split the 400-line function into two, one for validation, one for formatting")
   - After N failed handbacks, escalate.

7. **Check the contract's cost.** If every gate and criterion takes the judge more than a minute to evaluate, the loop will be expensive. Prioritize cheap gates first; graded criteria can be ordered by weight.

8. **Produce the "why this contract" summary** — one paragraph that the team can sign off on: what's in, what's out, and why.

## FALSE-POSITIVE PREVENTION (MUST follow)
- Do NOT write adjective gates. "Code is readable" is not a gate. "No function exceeds 60 lines" is a gate. Moves to graded if fuzzier.
- Do NOT write graded criteria without concrete anchor points. Level 3 must be distinguishable from Level 2 by something other than feel.
- Do NOT let weights sum to anything other than 100 (or 1.0, pick one and stick with it).
- Do NOT forget per-criterion floors. Without floors, one fatal flaw gets averaged away.
- Do NOT accept evidence locations like "the judge decides." Every criterion names where the evidence lives.
- Do NOT cap gates at zero. Every output has some non-negotiables. If the user says "none," ask what would make them NOT ship, and those are the gates.
- Do NOT include gates that can't be checked by the actors you have. If the judge is an agent, gates like "sign off from Legal" must be modeled as an external approval, not a gate the agent can mark passed.
- Do NOT let the task author also write graded scoring rules the task will be judged by (same failure mode as judge=planner). Graded scores are locked before the worker starts.
- DO include the minimum composite threshold explicitly. "Looks good" is not a threshold.
- DO flag when a criterion is actually two criteria. One criterion → one score.

## OUTPUT FORMAT

### Task
[One paragraph]

### Pass/Fail Gates
| # | Statement | Check | Evidence location | Reason it's a gate |
|---|-----------|-------|-------------------|--------------------|
| 1 | | | | |

### Graded Criteria
| # | Statement | Scale (0–N) | Weight | Floor | Evidence location |
|---|-----------|-------------|--------|-------|-------------------|
| 1 | | | | | |

**Anchor points** (Level 3 vs Level 2 vs Level 1 vs Level 0) for each criterion:
- Criterion 1: 
  - 3: 
  - 2: 
  - 1: 
  - 0: 
- ...

### Aggregation Rule
- Composite = Σ(score × weight) / max
- Minimum acceptable composite: 
- Gates: all AND
- Per-criterion floors: [list]

### Verdict Schema
```
[insert schema from instructions]
```

### Handback Rule
- On composite-below-threshold: hint = "[criterion → specific instruction]"
- On floor violation: hint = "[criterion → specific instruction]"
- Iteration cap: N
- Escalation target: 

### Why This Contract
[One paragraph]

### Sanity Checklist
- [ ] ≤7 gates, ≤7 graded
- [ ] Every gate is binary and has a named check + evidence location
- [ ] Every graded criterion has concrete anchor points, a weight, and a floor
- [ ] Weights sum to 100 (or 1.0)
- [ ] Min composite is explicit
- [ ] Graded rules locked before the worker starts (not mutable mid-task)
- [ ] Judge has the tools to evaluate every gate and criterion

## IMPORTANT
- Gates are negative: what blocks ship. Graded is positive: where more is better up to a point.
- Fewer gates are stronger gates. If you have 15, prune.
- If the judge can't check a criterion with the tools it has, the criterion is aspirational, not operational.
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — output is the acceptance contract, not a philosophy of quality
- ST-02 (Structured Sequential Instructions) — 8 steps separate gates from graded, define each, then aggregate
- CM-02 (Constraint Specification) — Must / Must Not rules block adjective gates and unweighted criteria
- DD-04 (MVP Gates) — gate-vs-graded distinction is the core MVP-gate discipline applied to agent acceptance
- DD-02 (Evidence Requirements) — every gate and every criterion names its evidence location
- QA-08 (Gate-Based Verification) — verdict schema becomes the judge's pass/fail contract downstream
