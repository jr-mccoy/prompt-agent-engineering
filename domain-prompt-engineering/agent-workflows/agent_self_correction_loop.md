---
title: "Self-Correction Loop for Agents"
category: prompt-engineering/agent-workflows
description: "Wrap an agent step with detect-error → diagnose → repair logic so transient or schema errors are recovered without escalating."
techniques:
  - QA-01
  - PR-03
difficulty: advanced
tags:
  - self-correction
  - agents
  - error-recovery
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/agent-workflows/agent_loop_termination_designer.md
---

## Objective

Add a tight detect-diagnose-repair wrapper around an agent step so common errors (schema mismatch, malformed tool output, contradiction) are corrected in-place before they propagate.

## When to Use

- Tool calls return malformed JSON the next step cannot parse
- Output occasionally violates a known constraint
- An agent benefits from one self-correction round, not full restart

## Inputs

1. The step prompt being wrapped
2. The known error classes (schema, contradiction, refusal-misroute, etc.)
3. Maximum correction attempts (default 1)

## Constraints

**Must:**
- Define error detection as a check on output, not a vibe
- Diagnose with a code from a fixed taxonomy
- Repair with the smallest change
- Log every correction for telemetry

**Must Not:**
- Loop correction beyond the cap
- Hide repaired errors from the agent's trace
- Repair errors that should escalate (safety, refusal cases)

## Instructions

1. Enumerate detectable error classes for this step.
2. Define a check per class.
3. Define a repair pass per class (different repair, not generic "try again").
4. Cap attempts.
5. Define escalation when cap reached.

## Output Format (the wrapper structure)

```
WRAPPER FLOW

attempt = 0
while attempt <= <cap>:
  output = run_step(input)
  detection = detect_errors(output)
  if detection.empty: return output
  if any detection.class in [<must-escalate set>]: escalate
  output = repair(output, detection)
  attempt += 1
escalate(reason="cap_exceeded", last_detection=detection)

DETECTION
  classes:
    - schema_violation: <regex / json-schema check>
    - contradiction: <self-consistency check>
    - refusal_misroute: <pattern>
    - empty_output: ...

REPAIR
  schema_violation → "Reformat to schema, preserve content"
  contradiction → "Resolve specified contradiction; keep one side"
  refusal_misroute → escalate
  empty_output → "Re-run with explicit instruction to produce output"

ESCALATION
  produce:
    {
      "status": "escalated",
      "reason": ...,
      "attempts": <n>,
      "last_output_snapshot": <abbrev>
    }

TELEMETRY
  every correction logged with: class, original, repaired, attempt
```

## Verification

- Each error class has a detection check and a repair (or escalation)
- Cap prevents infinite loops
- Escalation outputs are structured
- Safety/refusal errors do not get auto-repaired
