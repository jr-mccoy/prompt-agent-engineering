---
title: "Tool Naming Convention for Disambiguation Without Docs"
category: prompt-engineering/tool-use
description: "Define a naming pattern that lets the model and humans pick the right tool from the name alone."
techniques:
  - ST-03
  - CM-02
  - DC-01
difficulty: beginner
tags:
  - tool_use
  - naming
  - convention
  - disambiguation
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/tool-use/tooluse_tool_description_writer.md
  - domain-prompt-engineering/tool-use/tooluse_tool_set_minimization.md
---

## Objective

Standardize tool names with a `<verb>_<object>[_<qualifier>]` pattern so a model selecting from a registry can route correctly using the name alone, without re-reading every description.

## When to Use

- Adding tools to an existing registry of ≥ 5 tools.
- The registry contains both reads and writes, both internal and external services.
- Names like `process_data`, `handle_request`, `do_thing` exist.

## Inputs

```
TOOL_LIST: <existing names + one-line purpose>
SERVICE_BOUNDARIES: <optional list of services: stripe, github, internal_db>
SCOPE_QUALIFIERS: <optional: by_user, by_org, in_session>
```

## Constraints

### Must
- Pattern: `<verb>_<object>[_<qualifier>]`. Lowercase snake_case. ≤ 32 chars.
- `verb` from the closed set: `get`, `list`, `search`, `create`, `update`, `delete`, `send`, `cancel`, `confirm`, `validate`, `compute`, `summarize`. Add to the set only with explicit registry-level approval.
- Read tools start with `get`, `list`, or `search`. Writes start with the rest.
- Destructive tools (delete, cancel) MUST include the object scope: `delete_message_by_id`, not `delete_message`.
- If a service boundary applies, prefix or suffix it consistently across the registry: pick one of `<service>_<verb>_<object>` OR `<verb>_<object>_in_<service>`. Do not mix.
- Singular vs plural object follows return cardinality: `get_invoice` returns one; `list_invoices` returns many.

### Must Not
- Use generic verbs: `process`, `handle`, `do`, `manage`, `work_on`.
- Use abbreviations: `usr`, `msg`, `cfg`. Spell them out.
- Encode the user's job in the name: `help_user_pay` (use `create_payment`).
- Repeat the service boundary inside the verb (`stripe_get_stripe_customer`).

## Instructions

1. Audit TOOL_LIST. For each, classify as `compliant` or `rename_needed` with the violated rule.
2. Propose new names; preserve `verb` semantics.
3. Detect service-boundary inconsistency; pick one convention and rewrite to it.
4. Detect singular/plural mismatches; rewrite to match return cardinality.
5. Emit a migration table mapping old → new.

## Output Format

```
convention:
- pattern: <verb>_<object>[_<qualifier>]
- allowed_verbs: [<list>]
- service_position: prefix | suffix
- destructive_scope_required: yes

audit:
- compliant: [<names>]
- rename_needed:
  - <old_name>: violates <rule>; proposed=<new_name>

migration:
| old | new | reason |
|-----|-----|--------|
| <old> | <new> | <rule> |

deprecation_window: <e.g., "old name aliased for 2 releases">
```

## Verification

- Every name in `migration.new` matches the pattern regex `^[a-z]+_[a-z][a-z0-9_]*$` and uses an allowed verb.
- No two names in the post-migration registry are equal.
- Every destructive tool's name contains a scope qualifier.
- Service-boundary placement is consistent across the entire post-migration registry.
