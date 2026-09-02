"""Layer A — independent retrieval and routing scoring.

No model calls, so it costs nothing and returns the same numbers forever. That
makes it the one layer that can be re-run on every Engine change indefinitely,
and the one that can say *why* an end-to-end result came out the way it did: if
retrieval is strong and end-to-end is null, the bundle or the agent loop is
wasting good retrieval.

Two semantics deserve naming. Cluster collapse means a canonical resource and
its registered copy are one answer, scored once. And a task that accepts only
``ambiguous`` marks a confident ``matched`` as *wrong* — the false-confidence
stratum exists precisely to catch a router that sounds certain when it should
not (spec §55, §19).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping, Sequence

from .benchmark import Benchmark, Task, collapse_clusters, expects_no_route
from .constants import FIXTURE_MARKER


@dataclass
class Tally:
    n: int = 0
    hits: dict[str, int] = field(default_factory=dict)
    reciprocal_ranks: list[float] = field(default_factory=list)

    def add(self, key: str, hit: bool) -> None:
        self.hits[key] = self.hits.get(key, 0) + (1 if hit else 0)

    def rate(self, key: str) -> float | None:
        return (self.hits.get(key, 0) / self.n) if self.n else None


@dataclass
class RetrievalReport:
    metrics: Mapping[str, Any]
    per_class: Mapping[str, Mapping[str, Any]]
    per_task: tuple[Mapping[str, Any], ...]
    disclosure: str | None = None

    def to_json_obj(self) -> dict[str, Any]:
        obj: dict[str, Any] = {
            "layer": "A",
            "metrics": dict(self.metrics),
            "per_class": {k: dict(v) for k, v in self.per_class.items()},
            "per_task": [dict(t) for t in self.per_task],
        }
        if self.disclosure:
            obj["disclosure"] = self.disclosure
        return obj


class LayerAScorer:
    """Scores a benchmark's labels against Search and Router on a snapshot."""

    def __init__(self, snapshot_root: Path, *, limit: int = 10) -> None:
        from pae_engine import Registry, Repository, Router, SearchEngine

        self.snapshot_root = Path(snapshot_root).resolve()
        self._registry = Registry.open(Repository.at(self.snapshot_root))
        self._engine = SearchEngine(self._registry)
        self._router = Router(self._engine)
        self.limit = limit
        self._cluster_of = self._build_clusters()

    def _build_clusters(self) -> dict[str, str]:
        """uid -> canonical cluster key, so copies collapse onto their original."""
        clusters: dict[str, str] = {}
        index = self._engine._ensure_index()
        for document in index.documents:
            key = getattr(document, "cluster_key", None) or document.uid
            clusters[document.uid] = key
        return clusters

    # -- scoring -----------------------------------------------------------

    def score_task(self, task: Task) -> dict[str, Any]:
        row: dict[str, Any] = {"task_id": task.task_id, "class": task.task_class}

        results = self._engine.search(task.query, limit=self.limit)
        hit_uids = [hit.uid for hit in results.hits]
        collapsed = collapse_clusters(hit_uids, self._cluster_of)
        by_uid = {hit.uid: hit for hit in results.hits}

        if task.scores("resource"):
            gold_clusters = {
                self._cluster_of.get(r.uid, r.uid)
                for r in task.acceptable_resource_uids
            }
            ranked_clusters = [self._cluster_of.get(u, u) for u in collapsed]
            rank = next(
                (i + 1 for i, c in enumerate(ranked_clusters) if c in gold_clusters),
                None,
            )
            row["recall_at_1"] = bool(rank == 1)
            row["recall_at_5"] = bool(rank is not None and rank <= 5)
            row["reciprocal_rank"] = (1.0 / rank) if rank else 0.0
            row["rank"] = rank

        if task.scores("scope"):
            top = by_uid.get(collapsed[0]) if collapsed else None
            row["scope_at_1"] = bool(top is not None and top.scope in task.acceptable_scopes)
        if task.scores("kind"):
            top = by_uid.get(collapsed[0]) if collapsed else None
            row["kind_at_1"] = bool(top is not None and top.kind in task.acceptable_kinds)

        if task.scores("route_status"):
            decision = self._router.route(task.query)
            row["route_status"] = decision.status
            row["route_status_correct"] = decision.status in task.acceptable_route_statuses
            # False confidence: the task says the corpus does not support a
            # single confident answer, and the router gave one anyway.
            row["false_confident"] = bool(
                decision.status == "matched"
                and "matched" not in task.acceptable_route_statuses
            )
            if expects_no_route(task):
                row["no_route_correct"] = decision.status in ("weak", "no_route")
        return row

    def score(self, benchmark: Benchmark, *, disclosure: str | None = None
              ) -> RetrievalReport:
        rows = [self.score_task(task) for task in benchmark.tasks]

        overall = _summarize(rows)
        per_class: dict[str, dict[str, Any]] = {}
        for row in rows:
            per_class.setdefault(row["class"], {"_rows": []})["_rows"].append(row)
        summarized = {
            name: _summarize(bucket["_rows"]) for name, bucket in per_class.items()
        }
        return RetrievalReport(
            metrics=overall, per_class=summarized, per_task=tuple(rows),
            disclosure=disclosure,
        )


def _summarize(rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    def mean_of(key: str) -> float | None:
        values = [bool(r[key]) for r in rows if key in r]
        return (sum(values) / len(values)) if values else None

    scored_resource = [r for r in rows if "recall_at_1" in r]
    rr = [float(r.get("reciprocal_rank", 0.0)) for r in scored_resource]
    route_rows = [r for r in rows if "route_status" in r]

    return {
        "n": len(rows),
        "n_resource_scored": len(scored_resource),
        "recall_at_1": mean_of("recall_at_1"),
        "recall_at_5": mean_of("recall_at_5"),
        "mrr": (sum(rr) / len(rr)) if rr else None,
        "scope_at_1": mean_of("scope_at_1"),
        "kind_at_1": mean_of("kind_at_1"),
        "route_status_accuracy": mean_of("route_status_correct"),
        "false_confident_rate": mean_of("false_confident"),
        "no_route_correct_rate": mean_of("no_route_correct"),
        "route_status_counts": _counts(r.get("route_status") for r in route_rows),
    }


def _counts(values) -> dict[str, int]:
    from collections import Counter

    return dict(sorted(Counter(v for v in values if v).items()))


# --------------------------------------------------------------------------
# running Layer A against tuning data (spec §56)
# --------------------------------------------------------------------------

TUNING_DISCLOSURE = (
    "regression fixture — not independent evaluation. These labels come from "
    "the Phase 4 tuning set that the router's thresholds were fitted on. The "
    "numbers exercise the scorer; they are not evidence of search quality and "
    "must never appear in a report headline."
)


def load_phase4_fixture(repo: Path) -> list[dict[str, Any]]:
    """The Phase 4 regression cases, for testing the scorer only."""
    import json

    path = (Path(repo) / "pae-engine" / "tests" / "data"
            / "search_routing_regression.v1.json")
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload.get("cases", [])


def fixture_disclosure() -> str:
    return f"{FIXTURE_MARKER}\n{TUNING_DISCLOSURE}"
