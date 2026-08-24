---
title: "Tool Description Writer"
category: prompt-engineering/tool-use
description: "Write tool descriptions, parameter docs, and disambiguators so the model picks the right tool on first try."
techniques:
  - ST-03
  - CM-02
  - DC-01
  - PR-02
difficulty: intermediate
tags:
  - tool_use
  - description
  - tool_selection
  - disambiguation
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/tool-use/tooluse_tool_naming_convention.md
  - domain-prompt-engineering/tool-use/tooluse_tool_set_minimization.md
  - domain-prompt-engineering/tool-use/tooluse_when_to_call_decision_prompt.md
---

## Objective

Produce a tool description object — `name`, `description`, `parameters` (JSON Schema), and `do_not_use_when` — calibrated so the model selects this tool only when it is the right tool and not when a sibling tool fits better.

## When to Use

- Adding a tool to a tool set ≥ 3 tools.
- Misrouting has been observed (model picked tool A when B was correct).
- Two tools share verbs ("get", "fetch", "find").

## Inputs

```
TOOL_PURPOSE: <one sentence: what state changes or info is returned>
SIBLING_TOOLS: <names + 1-line summaries of tools the model could confuse this with>
INPUTS_NEEDED: <param name, type, required?, source>
DESTRUCTIVE: <yes|no>
IDEMPOTENT: <yes|no>
LATENCY_CLASS: <ms | s | minutes>
```

## Constraints

### Must
- `description` is 1–4 sentences. First sentence states the action and object: "Creates a Stripe customer record." No marketing words.
- Include explicit "Use when" and "Do not use when" lines, each referencing at least one SIBLING_TOOLS by name.
- Every required parameter has: type, one-sentence purpose, and an example value or source ("from the user's message", "from prior tool output").
- If `DESTRUCTIVE=yes`, the description starts with "DESTRUCTIVE: " and names the side effect.
- If `IDEMPOTENT=no`, mention what re-running causes.

### Must Not
- Use "various", "etc.", "appropriate", "as needed" anywhere.
- Describe the implementation; describe the contract.
- Name parameters with abbreviations (`uid`, `tgt`); use full words.
- Repeat the tool name inside the description text.

## Instructions

1. Write the action sentence: `<verb>` + `<object>` + `<scope/qualifier>`.
2. Add a "Returns:" sentence stating the shape (e.g., "Returns the created customer's `id` and `email`.").
3. List the two routing lines:
   - "Use when: <decision rule that excludes siblings>."
   - "Do not use when: <case that routes to <sibling_name>>."
4. Build the parameter schema. For each: type, required, purpose, example, source.
5. If destructive, append a one-line confirmation expectation: "Caller is expected to confirm with the user before invoking."

## Output Format

```json
{
  "name": "<tool_name>",
  "description": "<action sentence> <returns sentence> Use when: <rule>. Do not use when: <case routes to sibling>.",
  "parameters": {
    "type": "object",
    "required": ["..."],
    "properties": {
      "<param>": {"type": "string", "description": "<purpose>", "example": "<value>"}
    }
  },
  "do_not_use_when": ["<case 1>", "<case 2>"],
  "destructive": true | false,
  "idempotent": true | false
}
```

## Verification

- Read description aloud. If a sibling tool's description would also fit the same user message, sharpen the routing line.
- Every SIBLING_TOOLS name appears in the routing block.
- No banned words present.
- `DESTRUCTIVE=yes` ⇒ "DESTRUCTIVE:" prefix present.
