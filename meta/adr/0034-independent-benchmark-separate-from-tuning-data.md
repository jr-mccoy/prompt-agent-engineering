# ADR-0034 — The independent benchmark is separate from tuning data

## Status

Accepted. Implemented in Phase 7.

## Context

Phases 4 and 5 produced material that looks like evaluation:

- a 120-case search/routing regression set,
- regression floors asserted in CI,
- roughly 1,100 hand-written "user phrase" to resource mappings in
  `meta/ROUTING_REFERENCE.md`,
- context-packing diagnostics.

The router's coverage and margin thresholds were **fitted on the first of
these**. The floors are deliberately set below the measured values so an
ordinary corpus edit cannot fail the build. The routing phrases are
documentation labels that frequently share vocabulary with their target's title,
which flatters any lexical ranker — and the shipped ranker is lexical.

Phase 7A measured the size of that last effect on this corpus. Cases authored
*against* a resource record showed a median query-to-target vocabulary overlap
of **0.71**, against **0.44** for phrases that predated the search
implementation. 89% of resource-derived cases cleared 0.50, versus 48%.

## Decision

None of that material may support a public quality claim. It may be used to test
harness mechanics, and any output derived from it is labelled:

```text
regression fixture — not independent evaluation
```

The sealed benchmark is authored separately, in a separate repository, by an
author shown operational content only — no UID, public ID, title, description,
tags, path or H1 — with labels assigned afterwards by a different actor.

Independence is then **measured, not asserted**. `leakage.py` computes
query-to-target overlap, full title-token containment, public-ID-tail
containment, maximum Jaccard against the routing reference, and exact or near
duplication. The acceptance gates live in the frozen plan rather than in code,
so they cannot be relaxed without leaving a trace in a hashed artifact.

Ordinary domain vocabulary is deliberately *not* stripped. A clinical task
contains clinical words; that is the domain, not leakage. The gates target echo
of a specific target's identifiers, plus statistical over-similarity.

Exact duplication of a tuning query or routing phrase is a violation regardless
of any threshold. The tunable gates trade strictness against corpus vocabulary;
a verbatim copy is not a matter of degree.

## Consequences

- The repository cannot accidentally publish a tuning number as a result.
- Authoring the sealed benchmark is real work that this phase does not do.
- A benchmark that fails the gates is rejected before any money is spent.
- The measured 0.71-versus-0.44 gap is why the recommended authoring mix is
  mostly natural or external, with a bounded masked-derived stratum reserved for
  rare kinds and domains that natural authoring will not reach.
