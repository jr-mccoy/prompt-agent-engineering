# Tool Spec — read-domain-prompt

## Purpose
Load a named `domain-childrens-writing/` prompt so a stage can run it against the manuscript. This is the system's primary "capability injection" — each stage routes to one or more domain prompts.

## Signature
`read-domain-prompt(path) → prompt text`
- `path`: a path under `domain-childrens-writing/` (validated against the routing index in `referenced-prompts/README.md`).

## Behavior
Read-only. Returns the prompt's full text for the orchestrator/agent to apply. No side effects.

## Errors as guidance
- Path not under `domain-childrens-writing/` → return an error naming the routing index and the correct directory; do not fabricate prompt content.
- Path not found → list the available prompts for that stage from the routing index.

## Least privilege
Read-only; cannot write, cannot reach the network, cannot read outside the repo's children's-writing assets.
