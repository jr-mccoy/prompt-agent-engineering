"""Task routing: which scope and kind should handle this, and what to start from.

The Router answers a different question from search. Search ranks resources;
routing decides *where a task belongs* and then offers the strongest starting
points. It never executes a resource and never serves a body.

Two design commitments carry most of the weight:

* **Maximum, not sum.** A scope or kind scores as its single best hit. Summing
  hands every route to whichever kind has the most members — measured at 68%
  scope and 59% kind accuracy in the Phase 4A trials, against 84% and 98% for
  maximum — and it lets a registered copy vote twice for its toolkit.
* **Ambiguity is an answer.** When two scopes are close, or the query barely
  overlaps the best hit, the Router says so and returns alternatives instead of
  manufacturing a confident single route.
"""

from __future__ import annotations

from typing import Optional, Sequence

from ._lexical import SCORE_PRECISION
from .errors import UsageError
from .models import RouteCandidate, RouteDecision, SearchHit
from .search import SearchEngine

__all__ = ["Router", "CANDIDATE_DEPTH", "COVERAGE_THRESHOLD", "MARGIN_THRESHOLD"]

#: How many logical results the Router aggregates over. Independent of the
#: caller's ``limit``, which only controls how many resources come back.
CANDIDATE_DEPTH = 40

#: Provisional heuristics fitted on the Phase 4A diagnostic set. They are
#: **not** calibrated confidence thresholds, and the numbers should be expected
#: to move once an independently authored evaluation exists.
#:
#: Coverage was chosen over an absolute score floor because an absolute BM25F
#: threshold measured inert — 2.0, 3.0 and 4.5 produced near-identical status
#: distributions, so it would have looked meaningful while deciding nothing.
COVERAGE_THRESHOLD = 0.34
MARGIN_THRESHOLD = 0.25

DEFAULT_ROUTE_LIMIT = 5
MAX_ROUTE_LIMIT = 25

#: Only these fields count toward coverage. Path, kind and technique terms
#: match too easily to say anything about whether the query was understood.
_COVERAGE_FIELDS = ("title", "desc", "pid", "tags")


class Router:
    """Routes a task description to a scope, a kind and candidate resources."""

    def __init__(self, search: SearchEngine) -> None:
        self.search = search

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return f"Router({self.search!r})"

    def route(
        self,
        task: str,
        *,
        kinds: Optional[Sequence[str]] = None,
        limit: int = DEFAULT_ROUTE_LIMIT,
    ) -> RouteDecision:
        limit = SearchEngine._check_limit(
            limit, maximum=MAX_ROUTE_LIMIT, label="route limit"
        )
        results = self.search.search(
            task, kinds=kinds, limit=CANDIDATE_DEPTH, include_copies=False
        )
        hits = results.hits

        if not hits:
            return RouteDecision(
                query=task,
                normalized_terms=results.normalized_terms,
                status="no_route",
                selected_scope=None,
                selected_kind=None,
                candidate_scopes=(),
                candidate_kinds=(),
                resources=(),
                coverage=0.0,
                margin=0.0,
                reasons=("no eligible resource matched any query term",),
            )

        scopes = _aggregate(hits, lambda hit: hit.scope)
        kind_candidates = _aggregate(hits, lambda hit: hit.kind)
        coverage = _coverage(hits[0], results.normalized_terms)
        margin = _margin(scopes)

        reasons: list[str] = []
        top = hits[0]
        evidence = ", ".join(
            f"{field}[{' '.join(top.match_terms[field])}]" for field in top.matched_fields
        )
        reasons.append(f"top hit {top.id} matched {evidence}")
        reasons.append(f"coverage {coverage:.2f} (threshold {COVERAGE_THRESHOLD})")
        reasons.append(f"scope margin {margin:.2f} (threshold {MARGIN_THRESHOLD})")

        if coverage < COVERAGE_THRESHOLD:
            status = "weak"
            reasons.append("query terms barely overlap the best hit; no route selected")
        elif len(scopes) >= 2 and margin < MARGIN_THRESHOLD:
            status = "ambiguous"
            reasons.append(
                f"{scopes[0].name} and {scopes[1].name} score within "
                f"{MARGIN_THRESHOLD:.0%}; no route selected"
            )
        else:
            status = "matched"

        selected_scope = scopes[0].name if status == "matched" else None
        selected_kind = kind_candidates[0].name if status == "matched" else None

        return RouteDecision(
            query=task,
            normalized_terms=results.normalized_terms,
            status=status,
            selected_scope=selected_scope,
            selected_kind=selected_kind,
            candidate_scopes=scopes,
            candidate_kinds=kind_candidates,
            resources=hits[:limit],
            coverage=coverage,
            margin=margin,
            reasons=tuple(reasons),
        )


def _aggregate(hits: Sequence[SearchHit], key) -> tuple[RouteCandidate, ...]:
    """Rank buckets by their single best hit.

    ``hit_count`` is recorded but never scored. That is the whole point: a
    scope with forty mediocre matches must not outrank one with a single
    excellent match, or the largest directory wins every route.
    """
    best: dict[str, tuple[float, str]] = {}
    counts: dict[str, int] = {}
    for hit in hits:
        name = key(hit)
        if not name:
            continue
        counts[name] = counts.get(name, 0) + 1
        current = best.get(name)
        if current is None or hit.score > current[0]:
            best[name] = (hit.score, hit.uid)

    candidates = [
        RouteCandidate(
            name=name,
            score=round(score, SCORE_PRECISION),
            hit_count=counts[name],
            top_resource_uid=uid,
        )
        for name, (score, uid) in best.items()
    ]
    candidates.sort(key=lambda candidate: (-candidate.score, candidate.name))
    return tuple(candidates)


def _coverage(top: SearchHit, terms: Sequence[str]) -> float:
    """Fraction of query terms the best hit matched in its descriptive fields."""
    unique = set(terms)
    if not unique:
        return 0.0
    if top.matched_fields == ("exact_reference",):
        # The caller named the resource outright. There is nothing uncertain
        # about that, and scoring it as unmatched vocabulary would report the
        # most precise query the Engine accepts as the least confident.
        return 1.0
    matched: set[str] = set()
    for field in _COVERAGE_FIELDS:
        matched |= set(top.match_terms.get(field, ()))
    return len(matched & unique) / len(unique)


def _margin(scopes: Sequence[RouteCandidate]) -> float:
    if not scopes or scopes[0].score <= 0.0:
        return 0.0
    if len(scopes) == 1:
        return 1.0
    return (scopes[0].score - scopes[1].score) / scopes[0].score
