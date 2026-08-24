---
title: "Disambiguation Before Destructive Tool Calls"
category: prompt-engineering/tool-use
description: "Force a clarification turn before invoking a destructive or high-blast-radius tool when args are ambiguous."
techniques:
  - ST-02
  - CM-02
  - DP-04
  - QA-01
difficulty: intermediate
tags:
  - tool_use
  - disambiguation
  - destructive
  - confirmation
  - safety
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/tool-use/tooluse_when_to_call_decision_prompt.md
  - domain-prompt-engineering/tool-use/tooluse_dry_run_pattern.md
  - domain-prompt-engineering/tool-use/tooluse_argument_extraction_prompt.md
---

## Objective

Before calling a destructive tool, detect ambiguity (multiple matching targets, vague verbs, plural-vs-singular references) and emit a single specific question rather than guessing.

## When to Use

- The tool deletes, sends, charges, transfers, force-pushes, or otherwise affects shared state.
- The user said "the customer", "that file", "those messages" without unique identifiers.
- A search step returned ≥ 2 candidates.

## Inputs

```
TOOL_NAME: <name>
DESTRUCTIVE: <must be yes; otherwise this prompt does not apply>
USER_MESSAGE: <verbatim>
RESOLVED_TARGETS: <list of candidate targets returned by a prior lookup; each with id + label + last_modified>
PROPOSED_ARGS: <args the model would send if no disambiguation>
```

## Constraints

### Must
- Detect ambiguity if any of:
  - `RESOLVED_TARGETS.length != 1`.
  - USER_MESSAGE contains a definite article without enough qualifiers ("the file" with multiple files in scope).
  - PROPOSED_ARGS contains a plural noun against a singular-target tool.
  - The tool affects "all" of something and USER_MESSAGE did not say "all".
- If ambiguous, emit `action: "ask_user"` with one question that lists candidates (≤ 5; if more, say "and N more — narrow by <attribute>").
- The question references at least one disambiguating attribute (id, last_modified, owner, size).
- If unambiguous, emit `action: "proceed"` with the args echoed and a one-line `confirmation_summary` for the dry-run pattern to consume.

### Must Not
- Pick a candidate by recency, alphabetical order, or any heuristic without the user's explicit nod.
- Hide the question inside a longer message.
- Re-ask if the user already disambiguated in the same turn.

## Instructions

1. Run the four ambiguity checks. If any fires, set `action: "ask_user"`.
2. Build the question:
   - Lead: "Which one?" or "Did you mean..."
   - List candidates with id + 1 disambiguator.
   - End with a "or none of these — describe further" option.
3. If no ambiguity, build `confirmation_summary` of the form: "<tool_name> on <target_label> (id: <id>) with <key arg>=<value>."
4. Echo back what was assumed (timezone, user identity) so the user can correct it.

## Output Format

```json
{
  "action": "ask_user | proceed",
  "ambiguity_signals": ["multiple_targets", "definite_article_unqualified", "..."],
  "question": "<one sentence; null if proceed>",
  "candidates": [{"id": "...", "label": "...", "disambiguator": "..."}],
  "confirmation_summary": "<one sentence; null if ask_user>",
  "assumptions": ["timezone=UTC", "user=session.caller"]
}
```

## Verification

- `RESOLVED_TARGETS.length != 1` ⇒ `action == "ask_user"`.
- Question includes at least one candidate's id or disambiguating attribute.
- `proceed` ⇒ `candidates.length == 1` AND `confirmation_summary != null`.
- No assumed value contradicts USER_MESSAGE.
