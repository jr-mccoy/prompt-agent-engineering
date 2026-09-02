#!/usr/bin/env python3
"""Run the committed search/routing regression set against a live checkout.

    PYTHONPATH=src python3 tests/run_search_routing_diagnostics.py --repo ..
    PYTHONPATH=src python3 tests/run_search_routing_diagnostics.py --repo .. --compare
    PYTHONPATH=src python3 tests/run_search_routing_diagnostics.py --repo .. --json

A development tool, not part of the installed package and not a runtime
dependency of anything. ``--compare`` additionally scores the two rejected
ranking baselines against the same index and the same tokenizer, which is the
only way to compare them honestly: every earlier number that disagreed with
another did so because it was produced under a different configuration.

READ THIS BEFORE QUOTING A NUMBER FROM HERE
-------------------------------------------
This is an internal design and tuning regression set, not an independently
authored benchmark and not evidence of general model or search quality. Its
labels were written by the same process that selected the ranking algorithm,
and the router's coverage/margin thresholds were fitted on it. It exists to
catch regressions, not to make claims.
"""

from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Mapping, Sequence

from pae_engine import Registry, Repository, Router, SearchEngine
from pae_engine._lexical import B, FIELDS, K1, SCORE_PRECISION, normalize

from _support import peak_rss_mib

DATA = Path(__file__).parent / "data" / "search_routing_regression.v1.json"
CLASSES = ("task", "kind", "route", "ambig", "fuzzy", "norote", "dedup")

DISCLOSURE = (
    "internal tuning/regression set — NOT an independently authored benchmark, "
    "NOT evidence of general search quality"
)


# --------------------------------------------------------------------------
# rejected baselines, scored over the production index for a fair comparison
# --------------------------------------------------------------------------


def _rank(scored: Mapping[int, float], index) -> list[tuple[float, str, int]]:
    ranked = [
        (round(score, SCORE_PRECISION), index.documents[position].id, position)
        for position, score in scored.items()
        if score > 0
    ]
    ranked.sort(key=lambda entry: (-entry[0], entry[1]))
    return ranked


def score_overlap(index, terms: Sequence[str]) -> dict[int, float]:
    """Baseline A: uniform token overlap. No IDF, no length normalization."""
    scores: dict[int, float] = defaultdict(float)
    for term in sorted(set(terms)):
        for field in FIELDS:
            for position, _frequency in index.postings[field].get(term, ()):
                scores[position] += 1.0
    return scores


def score_flat_bm25(index, terms: Sequence[str]) -> dict[int, float]:
    """Baseline B: BM25 over one flattened document per record."""
    lengths = [sum(doc.lengths.values()) for doc in index.documents]
    average = (sum(lengths) / len(lengths)) if lengths else 0.0
    scores: dict[int, float] = defaultdict(float)
    for term in sorted(set(terms)):
        frequencies: dict[int, int] = defaultdict(int)
        for field in FIELDS:
            for position, frequency in index.postings[field].get(term, ()):
                frequencies[position] += frequency
        if not frequencies:
            continue
        weight = index.idf(term)
        for position, frequency in frequencies.items():
            norm = 1.0 - B + B * (lengths[position] / average if average else 1.0)
            scores[position] += weight * (frequency * (K1 + 1)) / (frequency + K1 * norm)
    return scores


def score_bm25f(index, terms: Sequence[str]) -> dict[int, float]:
    """The shipped ranker, reached through the same entry point as the others."""
    return index.score(terms)


BASELINES = {
    "weighted token overlap": score_overlap,
    "flat BM25": score_flat_bm25,
    "BM25F uniform (shipped)": score_bm25f,
}


# --------------------------------------------------------------------------
# metrics
# --------------------------------------------------------------------------


class Tally:
    def __init__(self) -> None:
        self.counts: Counter = Counter()
        self.rr: list[float] = []

    def rate(self, hits: str, total: str) -> float | None:
        denominator = self.counts[total]
        return (self.counts[hits] / denominator) if denominator else None


def _pct(value: float | None) -> str:
    return f"{100 * value:5.1f}%" if value is not None else "    --"


def score_cases(engine: SearchEngine, cases: Sequence[Mapping[str, Any]],
                scorer=None, limit: int = 10) -> dict[str, Any]:
    """Search metrics. ``scorer`` overrides the ranker for baseline comparison."""
    index = engine._ensure_index()
    position_of = {document.uid: n for n, document in enumerate(index.documents)}
    per: dict[str, Tally] = defaultdict(Tally)
    overall = Tally()
    latencies: list[float] = []
    leaks: Counter = Counter()
    duplicate_leaks = 0

    for case in cases:
        terms = normalize(case["query"])
        if not terms:
            # A query that normalizes away is rejected as a usage error by
            # design, so it cannot be a retrieval case. Unit tests pin that
            # rejection; the regression set is not the place for it.
            raise SystemExit(
                f"{case['id']}: query {case['query']!r} normalizes to no terms; "
                "regression cases must be searchable"
            )
        started = time.perf_counter()
        if scorer is None:
            hits = engine.search(case["query"], limit=limit).hits
            ids = [hit.id for hit in hits]
            scopes = [hit.scope for hit in hits]
            kinds = [hit.kind for hit in hits]
            documents = [index.documents[position_of[hit.uid]] for hit in hits]
        else:
            ranked = _rank(scorer(index, terms), index)
            seen: set[str] = set()
            collapsed = []
            for entry in ranked:
                key = index.documents[entry[2]].cluster_key
                if key in seen:
                    continue
                seen.add(key)
                collapsed.append(entry)
            documents = [index.documents[entry[2]] for entry in collapsed[:limit]]
            ids = [doc.id for doc in documents]
            scopes = [doc.scope for doc in documents]
            kinds = [doc.kind for doc in documents]
        latencies.append((time.perf_counter() - started) * 1000.0)

        for document in documents:
            if document.maturity == "deprecated":
                leaks["deprecated"] += 1
            if document.lifecycle == "tombstone":
                leaks["tombstone"] += 1
            if document.serving_policy == "excluded":
                leaks["excluded"] += 1

        # Duplicate leakage is a property of the un-collapsed ranking, so it is
        # measured with cluster suppression deliberately switched off.
        if scorer is None:
            physical = engine.search(case["query"], limit=limit, include_copies=True).hits
            clusters = [hit.canonical_uid for hit in physical]
            duplicate_leaks += len(clusters) - len(set(clusters))

        tallies = (per[case["class"]], overall)
        gold = set(case["acceptable_resource_ids"])
        if gold:
            for tally in tallies:
                tally.counts["n_resource"] += 1
            position = next((i + 1 for i, rid in enumerate(ids) if rid in gold), 0)
            for cutoff in (1, 3, 5):
                if position and position <= cutoff:
                    for tally in tallies:
                        tally.counts[f"r@{cutoff}"] += 1
            for tally in tallies:
                tally.rr.append(1.0 / position if position else 0.0)

        gold_scopes = set(case["acceptable_scopes"])
        if gold_scopes:
            for tally in tallies:
                tally.counts["n_scope"] += 1
            if scopes and scopes[0] in gold_scopes:
                for tally in tallies:
                    tally.counts["scope@1"] += 1
            if gold_scopes & set(scopes[:3]):
                for tally in tallies:
                    tally.counts["scope@3"] += 1

        gold_kinds = set(case["acceptable_kinds"])
        if gold_kinds:
            for tally in tallies:
                tally.counts["n_kind"] += 1
            if kinds and kinds[0] in gold_kinds:
                for tally in tallies:
                    tally.counts["kind@1"] += 1
            if gold_kinds & set(kinds[:2]):
                for tally in tallies:
                    tally.counts["kind@2"] += 1

        for tally in tallies:
            tally.counts["n"] += 1

    return {
        "per_class": per,
        "overall": overall,
        "latencies": latencies,
        "leaks": leaks,
        "duplicate_leaks": duplicate_leaks,
    }


def score_routing(router: Router, cases: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    counts: Counter = Counter()
    statuses: Counter = Counter()
    latencies: list[float] = []
    false_confident: list[str] = []
    forced: list[str] = []
    copy_distortion: list[str] = []
    toolkit_scopes = {"idea-to-product", "financial-records-toolkit"}

    for case in cases:
        started = time.perf_counter()
        decision = router.route(case["query"])
        latencies.append((time.perf_counter() - started) * 1000.0)
        statuses[decision.status] += 1

        names = [candidate.name for candidate in decision.candidate_scopes]
        gold_scopes = set(case["acceptable_scopes"])
        if gold_scopes:
            counts["n_scope"] += 1
            if decision.candidate_scopes and names[0] in gold_scopes:
                counts["scope@1"] += 1
            if gold_scopes & set(names[:3]):
                counts["scope@3"] += 1
            if (
                decision.candidate_scopes
                and names[0] in toolkit_scopes
                and names[0] not in gold_scopes
            ):
                copy_distortion.append(case["id"])

        gold_kinds = set(case["acceptable_kinds"])
        if gold_kinds:
            counts["n_kind"] += 1
            if decision.candidate_kinds and decision.candidate_kinds[0].name in gold_kinds:
                counts["kind@1"] += 1

        if case["expected_status"] == "ambiguous" and decision.status == "matched":
            if decision.selected_scope not in gold_scopes:
                false_confident.append(case["id"])
        if case["expected_status"] == "no_route" and decision.status == "matched":
            forced.append(case["id"])

    return {
        "counts": counts,
        "statuses": statuses,
        "latencies": latencies,
        "false_confident": false_confident,
        "forced": forced,
        "copy_distortion": copy_distortion,
    }


# --------------------------------------------------------------------------
# reporting
# --------------------------------------------------------------------------


def summarize(result: dict[str, Any]) -> dict[str, Any]:
    overall: Tally = result["overall"]
    latencies = sorted(result["latencies"])
    return {
        "n": overall.counts["n"],
        "r@1": overall.rate("r@1", "n_resource"),
        "r@3": overall.rate("r@3", "n_resource"),
        "r@5": overall.rate("r@5", "n_resource"),
        "mrr": statistics.mean(overall.rr) if overall.rr else None,
        "scope@1": overall.rate("scope@1", "n_scope"),
        "scope@3": overall.rate("scope@3", "n_scope"),
        "kind@1": overall.rate("kind@1", "n_kind"),
        "kind@2": overall.rate("kind@2", "n_kind"),
        "deprecated_leaks": result["leaks"]["deprecated"],
        "tombstone_leaks": result["leaks"]["tombstone"],
        "excluded_leaks": result["leaks"]["excluded"],
        "duplicate_cluster_leaks": result["duplicate_leaks"],
        "latency_median_ms": round(statistics.median(latencies), 3) if latencies else None,
        "latency_p95_ms": round(latencies[int(0.95 * (len(latencies) - 1))], 3)
        if latencies
        else None,
    }


def print_search(result: dict[str, Any]) -> None:
    summary = summarize(result)
    print(f"{'class':<8}{'n':>4}{'R@1':>8}{'R@3':>8}{'R@5':>8}{'MRR':>8}"
          f"{'scope@1':>9}{'scope@3':>9}{'kind@1':>8}")
    for name in CLASSES:
        tally: Tally = result["per_class"].get(name)
        if tally is None:
            continue
        mrr = statistics.mean(tally.rr) if tally.rr else None
        print(
            f"{name:<8}{tally.counts['n']:>4}"
            f"{_pct(tally.rate('r@1', 'n_resource')):>8}"
            f"{_pct(tally.rate('r@3', 'n_resource')):>8}"
            f"{_pct(tally.rate('r@5', 'n_resource')):>8}"
            f"{(f'{mrr:8.3f}' if mrr is not None else '      --')}"
            f"{_pct(tally.rate('scope@1', 'n_scope')):>9}"
            f"{_pct(tally.rate('scope@3', 'n_scope')):>9}"
            f"{_pct(tally.rate('kind@1', 'n_kind')):>8}"
        )
    print(
        f"{'ALL':<8}{summary['n']:>4}{_pct(summary['r@1']):>8}{_pct(summary['r@3']):>8}"
        f"{_pct(summary['r@5']):>8}{summary['mrr']:8.3f}{_pct(summary['scope@1']):>9}"
        f"{_pct(summary['scope@3']):>9}{_pct(summary['kind@1']):>8}"
    )
    print(
        f"\nleaks: deprecated={summary['deprecated_leaks']} "
        f"tombstone={summary['tombstone_leaks']} excluded={summary['excluded_leaks']} "
        f"duplicate-cluster={summary['duplicate_cluster_leaks']}"
    )
    print(
        f"latency: median {summary['latency_median_ms']} ms  "
        f"p95 {summary['latency_p95_ms']} ms"
    )


def print_routing(result: dict[str, Any]) -> None:
    counts = result["counts"]
    statuses = result["statuses"]
    rate = lambda a, b: _pct(counts[a] / counts[b]) if counts[b] else "    --"  # noqa: E731
    print(
        f"scope@1 {rate('scope@1','n_scope')}   scope@3 {rate('scope@3','n_scope')}   "
        f"kind@1 {rate('kind@1','n_kind')}"
    )
    print(
        "statuses: "
        + "  ".join(f"{name}={statuses[name]}" for name in
                    ("matched", "ambiguous", "weak", "no_route"))
    )
    print(f"false-confident on ambiguous cases: {len(result['false_confident'])} "
          f"{result['false_confident'] or ''}")
    print(f"forced matches on no-route cases:   {len(result['forced'])} "
          f"{result['forced'] or ''}")
    print(f"copy-cluster scope distortion:      {len(result['copy_distortion'])} "
          f"{result['copy_distortion'] or ''}")
    latencies = sorted(result["latencies"])
    print(f"latency: median {statistics.median(latencies):.2f} ms  "
          f"p95 {latencies[int(0.95 * (len(latencies) - 1))]:.2f} ms")


def validate_labels(registry: Registry, cases: Sequence[Mapping[str, Any]]) -> list[str]:
    known = {record.id for record in registry.load_all()}
    problems = []
    for case in cases:
        for resource_id in case["acceptable_resource_ids"]:
            if resource_id not in known:
                problems.append(f"{case['id']}: unknown resource id {resource_id}")
    return problems


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--repo", default=None, help="path to a PAE checkout")
    parser.add_argument("--compare", action="store_true",
                        help="also score the two rejected ranking baselines")
    parser.add_argument("--json", action="store_true", help="machine-readable summary")
    args = parser.parse_args(list(argv if argv is not None else sys.argv[1:]))

    document = json.loads(DATA.read_text(encoding="utf-8"))
    cases = document["cases"]
    registry = Registry.open(Repository.discover(args.repo))

    problems = validate_labels(registry, cases)
    if problems:
        for problem in problems:
            print(f"LABEL ERROR: {problem}", file=sys.stderr)
        return 1

    started = time.perf_counter()
    engine = SearchEngine(registry)
    engine._ensure_index()
    build_ms = (time.perf_counter() - started) * 1000.0
    router = Router(engine)

    search_result = score_cases(engine, cases)
    routing_result = score_routing(router, cases)
    peak_mb = peak_rss_mib()

    if args.json:
        payload = {
            "disclosure": DISCLOSURE,
            "cases": len(cases),
            "index": dict(engine.index_info),
            "search": summarize(search_result),
            "routing": {
                "scope@1": routing_result["counts"]["scope@1"] / routing_result["counts"]["n_scope"],
                "scope@3": routing_result["counts"]["scope@3"] / routing_result["counts"]["n_scope"],
                "kind@1": routing_result["counts"]["kind@1"] / routing_result["counts"]["n_kind"],
                "statuses": dict(routing_result["statuses"]),
                "false_confident": routing_result["false_confident"],
                "forced": routing_result["forced"],
                "copy_distortion": routing_result["copy_distortion"],
            },
            "build_ms": round(build_ms, 1),
            "peak_rss_mb": None if peak_mb is None else round(peak_mb, 1),
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0

    print("=" * 78)
    print(f"PAE search/routing diagnostics — {DISCLOSURE}")
    print("=" * 78)
    print(f"dataset:  {DATA.name}  ({len(cases)} cases)")
    print(f"registry: {engine.index_info['registry_root']}")
    print(f"index:    {engine.index_info['records_indexed']} documents, "
          f"{engine.index_info['distinct_terms']} terms, "
          f"{engine.index_info['scopes']} scopes, built in {build_ms:.0f} ms")
    print(f"config:   BM25F uniform weights, k1={K1}, b={B}, "
          f"NFKC+casefold+split+stopwords+depluralize, canonical-cluster dedup, limit=10")
    print("peak RSS: unavailable on this platform\n" if peak_mb is None
          else f"peak RSS: {peak_mb:.0f} MB\n")

    print("-- SEARCH --------------------------------------------------------------")
    print_search(search_result)

    if args.compare:
        print("\n-- RANKING COMPARISON (same index, same tokenizer, same dedup) ----------")
        print(f"{'algorithm':<26}{'R@1':>8}{'R@3':>8}{'R@5':>8}{'MRR':>8}"
              f"{'scope@1':>9}{'kind@1':>8}")
        for name, scorer in BASELINES.items():
            summary = summarize(score_cases(engine, cases, scorer=scorer))
            print(
                f"{name:<26}{_pct(summary['r@1']):>8}{_pct(summary['r@3']):>8}"
                f"{_pct(summary['r@5']):>8}{summary['mrr']:8.3f}"
                f"{_pct(summary['scope@1']):>9}{_pct(summary['kind@1']):>8}"
            )

    print("\n-- ROUTING -------------------------------------------------------------")
    print_routing(routing_result)
    print()
    print("Reminder: " + DISCLOSURE + ".")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
