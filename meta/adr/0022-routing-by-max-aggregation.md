# ADR-0022 — Routing aggregates by maximum, and ambiguity is a result

## Status

Accepted. Implemented in Phase 4.

## Context

Routing is not search. Search ranks resources; routing decides which scope and
which resource kind should handle a task, and only then offers starting points.
Two questions had to be settled with evidence rather than taste: how to
aggregate hits into a route, and what to do when the evidence is thin.

**Aggregation.** The registry is heavily imbalanced — 4,196 live prompts
against 53 personas — and 59 resources are registered copies of another
resource. Any scheme that adds scores hands the answer to whichever kind or
scope has the most members, and lets a copy vote twice for its toolkit.
Measured over 120 labelled cases:

| Aggregation | scope@1 | kind@1 |
|---|---|---|
| sum of hits | 68.2% | **58.5%** |
| mean of top 3 | 78.8% | 87.8% |
| discounted sum of top 3 | 81.2% | 82.9% |
| **maximum** | **83.5%** | **97.6%** |

**A hand-written rule table was also tried**, as the obvious way to preserve
the routing knowledge already in `CLAUDE.md`. Keyed on scope-name tokens plus
hand aliases it scored **16.5% scope@1** and returned no route for 81 of 120
cases. Natural language does not contain directory names.

**Ambiguity.** A top-hit-passthrough router scored the same 83.5% scope@1 —
maximum aggregation's winner *is* the top hit's scope, by construction — but
had no way to express doubt, and produced three confidently wrong routes on
cases where two scopes were genuinely close.

An absolute BM25F score floor was tested as a confidence signal and measured
**inert**: thresholds of 2.0, 3.0 and 4.5 produced near-identical status
distributions. It would have looked meaningful while deciding nothing.

## Decision

`Router` is a separate public class taking a `SearchEngine`. It aggregates the
top **40 logical** results (cluster-deduplicated, so copies cannot double-vote).

**Scope score and kind score are each the maximum hit score in that bucket.**
Never a sum, never scaled by hit count, never adjusted by a population prior.
`hit_count` is reported for inspection and never scored. No kind priors, no
verb heuristics, no prompt penalty, no skill boost.

Certainty is expressed with two named, defined quantities, neither called
confidence:

- **coverage** — the fraction of normalized query terms the top hit matched in
  its title, description, public ID or tags;
- **margin** — the relative gap between the best and second-best scope score.

Status, evaluated in order: no hits → `no_route`; coverage < 0.34 → `weak`;
two or more scopes and margin < 0.25 → `ambiguous`; otherwise `matched`.

`selected_scope` and `selected_kind` are populated **only** when the status is
`matched`. A consumer that ignores `status` and reads the selection anyway gets
nothing rather than a guess. Every status exits 0; callers branch on `status`,
not on an exit code.

## Consequences

- `matched` is deliberately rare. On the regression set the Router returns
  `ambiguous` for 64 of 120 cases and `matched` for 40. That is the intended
  posture — returning ranked alternatives beats manufacturing a single
  confident answer — but it means most routes present options.
- Zero false-confident routes on the 15 deliberately ambiguous cases; one
  forced route on the 10 off-corpus cases.
- The thresholds 0.34 and 0.25 are **provisional heuristics fitted on the same
  120 cases used to select the algorithm**. They are not calibrated, and they
  should be expected to move once an independently authored evaluation exists.
  They are documented as provisional everywhere they appear.
- Maximum aggregation is structurally immune to copy-vote inflation, which
  matters because `idea-to-product` alone holds 52 copies of other scopes'
  resources.
- Because maximum aggregation's winner is the top hit's scope, the Router's
  first answer matches a top-hit router. Its value is the ranked alternatives
  and the computable margin, not a different first answer.

## Related

- [ADR-0021](0021-deterministic-lexical-search.md) — the search it aggregates
- [ADR-0023](0023-executable-routing-migration.md) — how it replaces prose
- [ADR-0012](0012-one-record-per-copy.md) — the copy edges it deduplicates on
