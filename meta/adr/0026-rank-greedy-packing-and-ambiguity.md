# ADR-0026 — Rank-preserving greedy packing, with one promotion for an ambiguous route

## Status

Accepted. Implemented in Phase 5 (`pae_engine.context`).

## Context

Given more candidates than budget, something has to choose. Four strategies
were measured over the 120-case Phase 4 regression set at five budgets, using
whole-body packing and the production renderer.

| Budget | Strategy | top-1 kept | top-3 kept | mean included | median utilization | mean deepest rank |
|---:|---|---:|---:|---:|---:|---:|
| 8,000 | **rank-greedy** | **99.1%** | **76.3%** | 3.19 | 95.5% | 6.6 |
| 8,000 | score-per-token | 60.3% | 44.9% | 4.61 | 92.3% | 16.2 |
| 8,000 | 0/1 knapsack | 71.6% | 54.0% | 4.51 | 96.8% | 15.0 |
| 4,000 | **rank-greedy** | **77.6%** | **37.3%** | 1.66 | 91.9% | 6.4 |
| 4,000 | score-per-token | 32.8% | 20.9% | 2.39 | 83.3% | 13.6 |

The mechanism is visible in the last column. Score-per-token and knapsack reach
to rank 15–16 to fill the budget; rank-greedy stops around 6.6. They buy about
1.4 extra resources and a point of utilization by evicting the best-scoring hit
for several small mediocre ones — the predictable result of treating a BM25F
score as calibrated utility when [ADR-0021](0021-deterministic-lexical-search.md)
is explicit that it is an unbounded ranking number. Knapsack has a second
defect: "the dynamic program preferred a different subset" cannot be rendered
as a per-resource omission reason.

Ambiguity is not an edge case. Across the same 120 cases the Router returns
`ambiguous` for 64 — **54% of routed traffic** — and rank-greedy alone
collapsed those bundles into a single scope 9.4% of the time at 8k and 6.2% at
16k, silently discarding the second reading the Router had explicitly flagged
as close.

## Decision

**Default order is the order the caller supplied** — search or route rank,
or literal input order for explicit references. No reordering by score-per-
token, size, kind, serving policy or lexical score.

**Greedy, whole-item, skip-and-continue.** For each candidate in priority
order: intrinsic omissions are recorded and skipped; beyond `max_resources` the
reason is `max_resources`; a body that does not fit alongside what is already
included is `budget`, unless it would not fit in a minimal bundle either, in
which case it is `oversized`. Packing never stops at the first non-fitting
item, which is why an oversized rank-1 does not empty the bundle.

**For an ambiguous route only, exactly one promotion.** The Router named two
close scopes; the compiler keeps rank 1, promotes the earliest candidate from
the *other* of those two scopes to second position, and appends the rest in
rank order. It is deliberately not a round robin over every scope the query
touched, and it is disabled when the caller supplied a scope filter. If that
other scope has no resource among the candidates, the compiler falls back to
rank order and warns `ambiguity_diversity_unavailable`.

Measured, this removes the collapse at no cost to the top hit: at 8k, top-1
retention stays 99.1% while single-scope ambiguous bundles fall from 9.4% to
6.2% raw — and of that residue only **1.6%** held two or more bodies, meaning
the rest simply had no room for a second scope. At 16k and 32k the collapse is
0.0%.

**Route status survives compilation.** `matched` compiles plainly; `weak`
compiles with a `weak_route` warning and its status intact; `ambiguous` keeps
`selected_scope` and `selected_kind` null and warns `ambiguous_route`;
`no_route` returns a valid empty bundle with provenance and exits 0. A scope
filter is a packing filter, never a re-route: filtered candidates become
`filtered` omissions, the status is unchanged, and an unknown scope is a usage
error.

**A final validation loop re-measures the real artifact.** Omission lines and
warnings are themselves part of the rendering, so after selection the compiler
renders the complete bundle, measures it, and sheds the lowest-priority body
until the emitted Markdown honours what the report claims. If the top-ranked
candidate is lost to budget, `top_hit_omitted` is raised as a warning, because
a bundle whose best hit silently vanished looks exactly like one where it fit.

## Consequences

Bundles are explainable: every absence has one of nine closed reason codes and
a deterministic detail string derived from it. Utilization is slightly lower
than knapsack would achieve, which is the intended trade — the packer optimizes
for keeping what the ranking ranked highest, not for filling space.

`tests/run_context_compiler_diagnostics.py` reports these figures at 2k–32k and
exits non-zero if a guarded body is ever shortened or a rendered bundle exceeds
the budget it reported. Those two columns are assertions, not measurements. It
is run locally rather than per PR: unlike the metadata-only search diagnostics,
it reads bodies, and `Registry` scans the whole registry file per reference, so
the sweep is I/O-bound on a cold disk. The same invariants are asserted against
the live registry by `tests/test_context_regression.py` inside the unit-test
job.
