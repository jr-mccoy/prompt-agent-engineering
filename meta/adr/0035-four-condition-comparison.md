# ADR-0035 — Four conditions, with D vs B as the primary comparison

## Status

Accepted. Implemented in Phase 7.

## Context

"Does PAE help?" is four different questions depending on what it is compared
against, and the cheapest comparison is the least informative one.

## Decision

Four conditions, all in the final benchmark:

| | Context | Tools | PAE |
|---|---|---|---|
| **A** | none | none | no |
| **B** | none | ripgrep-backed search, list, read | no |
| **C** | canonical `ContextBundle` Markdown, injected | none | route and compile, outside the model |
| **D** | none | the four Phase 6 MCP tools | the whole product |

**The primary comparison is D vs B**, paired, with the task as the unit of
analysis.

A vs D is nearly a tautology on a corpus-specific benchmark — it mostly
establishes that the tasks are about this corpus — so it is never the headline.

Condition C is kept even though it answers a secondary question, because the
cost intuition inverts: C is a single call with no tool loop, making it the
*second cheapest* arm at roughly a quarter of B's cost. Cutting it would save
about 9% of run cost and forfeit the only clean separation between "the bundle
is good" and "the agent drove the tools well".

Every condition shares one base system prompt, one turn budget, one output limit
and one timeout. Conditions with tools receive one additional generic paragraph
about tool use, rendered identically for B and D. This is asserted rather than
intended: a baseline quietly given a worse deal produces a win that means
nothing.

## Consequences

- The headline rests on the hardest available comparison rather than the
  flattering one.
- Four arms mean more comparisons; a single pre-declared primary plus
  Holm–Bonferroni across the secondary family keeps that honest.
- If D beats A but not B, the finding is "the corpus helps", not "the Engine
  helps" — and this design can tell the difference.
