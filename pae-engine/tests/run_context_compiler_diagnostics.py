#!/usr/bin/env python3
"""Pack the committed regression tasks into real bundles at several budgets.

    PYTHONPATH=src python3 tests/run_context_compiler_diagnostics.py --repo ..
    PYTHONPATH=src python3 tests/run_context_compiler_diagnostics.py --repo .. --json

A development tool. It is not part of the installed package, adds no
dependency, and uses the production renderer and the production default
counter — never an external tokenizer — so the numbers describe the artifact
the Engine actually emits.

READ THIS BEFORE QUOTING A NUMBER FROM HERE
-------------------------------------------
This is **packing regression, not task-quality evaluation.** Every figure
below answers one narrow question: does the packer keep what the ranking put
at the top, honour the budget it reports, and refuse to shorten a guarded
body? None of it says whether the selected resources are the right answer to
the task. The cases are the same internal Phase 4 tuning set, with the same
disclosure: their labels were written by the process that chose the ranking.

The two figures that are correctness assertions rather than measurements —
safety-gated truncations and final-render budget violations — must both be
zero, and the suite fails loudly if they are not.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import resource
import sys
import time
from collections import Counter
from pathlib import Path
from typing import Any, Sequence

from pae_engine import (
    ApproximateTokenCounterV1,
    Budget,
    ContextCompiler,
    Registry,
    Repository,
    Router,
    SearchEngine,
)

DATA = Path(__file__).parent / "data" / "search_routing_regression.v1.json"
BUDGETS = (2000, 4000, 8000, 16000, 32000)

DISCLOSURE = (
    "internal packing regression — NOT task-quality evaluation, NOT a benchmark "
    "of whether the selected resources answer the task"
)


def percentile(values: Sequence[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    k = (len(ordered) - 1) * q
    low, high = math.floor(k), math.ceil(k)
    if low == high:
        return ordered[low]
    return ordered[low] + (ordered[high] - ordered[low]) * (k - low)


def measure(repo: str | None) -> dict[str, Any]:
    started = time.perf_counter()
    repository = Repository.discover(repo)
    registry = Registry.open(repository)
    search = SearchEngine(registry)
    router = Router(search)
    compiler = ContextCompiler(registry)
    counter = ApproximateTokenCounterV1()

    cases = json.loads(DATA.read_text(encoding="utf-8"))["cases"]
    decisions = []
    for case in cases:
        decision = router.route(case["query"], limit=25)
        decisions.append((case, decision))
    routed_at = time.perf_counter()

    rows: list[dict[str, Any]] = []
    for budget_tokens in BUDGETS:
        stat = Counter()
        utilization: list[float] = []
        cases_with_candidates = 0
        top1_possible = top1_kept = 0
        top3_possible = top3_kept = 0
        included_total = 0
        ambiguous_cases = 0
        ambiguous_collapsed = 0
        ambiguous_collapsed_with_room = 0

        for case, decision in decisions:
            if not decision.resources:
                continue
            cases_with_candidates += 1
            budget = Budget(estimated_tokens=budget_tokens)
            try:
                bundle = compiler.compile_route(decision, budget=budget)
            except Exception as exc:  # noqa: BLE001 - a failure is a datum here
                stat[f"compile_error:{type(exc).__name__}"] += 1
                continue

            markdown = bundle.render_markdown()
            if len(markdown.encode("utf-8")) > bundle.budget.effective_byte_ceiling:
                stat["final_render_byte_violations"] += 1
            if counter.count(markdown) > budget_tokens:
                stat["final_render_token_violations"] += 1

            included_uids = {item.uid for item in bundle.included}
            included_total += len(bundle.included)
            if bundle.included:
                stat["non_empty"] += 1
                utilization.append(100.0 * bundle.budget.used_bytes /
                                   bundle.budget.effective_byte_ceiling)

            servable = {
                o.uid for o in bundle.omitted if o.reason in ("budget", "oversized")
            } | included_uids
            ranked = [hit.uid for hit in decision.resources]
            if ranked and ranked[0] in servable:
                top1_possible += 1
                if ranked[0] in included_uids:
                    top1_kept += 1
            for uid in ranked[:3]:
                if uid in servable:
                    top3_possible += 1
                    if uid in included_uids:
                        top3_kept += 1

            for omission in bundle.omitted:
                stat[f"omit_{omission.reason}"] += 1

            for item in bundle.included:
                if item.serving_policy == "safety_gated":
                    stat["safety_gated_included"] += 1
                    # Wholeness proved against the checksum the Registry
                    # verified, rather than by reading the source again.
                    encoded = item.content.encode("utf-8")
                    digest = "sha256:" + hashlib.sha256(encoded).hexdigest()
                    if digest != item.content_sha256 or len(encoded) != item.byte_length:
                        stat["safety_gated_truncations"] += 1

            if bundle.route_status == "ambiguous":
                ambiguous_cases += 1
                candidate_scopes = {
                    hit.scope for hit in decision.resources if hit.scope
                }
                included_scopes = {item.scope for item in bundle.included if item.scope}
                if len(candidate_scopes) > 1 and len(included_scopes) == 1:
                    ambiguous_collapsed += 1
                    # A single-scope bundle holding one body had no room for a
                    # second scope. Holding two or more is a genuine collapse.
                    if len(bundle.included) > 1:
                        ambiguous_collapsed_with_room += 1

        rows.append(
            {
                "budget_estimated_tokens": budget_tokens,
                "cases": cases_with_candidates,
                "non_empty_rate": _pct(stat["non_empty"], cases_with_candidates),
                "top1_retention": _pct(top1_kept, top1_possible),
                "top3_retention": _pct(top3_kept, top3_possible),
                "mean_included": round(included_total / max(cases_with_candidates, 1), 2),
                "utilization_median": round(percentile(utilization, 0.5), 1),
                "utilization_p95": round(percentile(utilization, 0.95), 1),
                "oversized_skips": stat["omit_oversized"],
                "budget_skips": stat["omit_budget"],
                "metadata_only_omissions": stat["omit_metadata_only"],
                "no_body_omissions": stat["omit_no_addressable_body"] + stat["omit_tombstone"],
                "ambiguous_cases": ambiguous_cases,
                "ambiguous_single_scope_collapse": _pct(
                    ambiguous_collapsed, ambiguous_cases
                ),
                "ambiguous_collapse_with_room": _pct(
                    ambiguous_collapsed_with_room, ambiguous_cases
                ),
                "safety_gated_included": stat["safety_gated_included"],
                "safety_gated_truncations": stat["safety_gated_truncations"],
                "final_render_violations": (
                    stat["final_render_byte_violations"] + stat["final_render_token_violations"]
                ),
                "compile_errors": sum(
                    v for k, v in stat.items() if k.startswith("compile_error:")
                ),
            }
        )

    done = time.perf_counter()
    return {
        "disclosure": DISCLOSURE,
        "renderer": "pae-context-markdown/1",
        "counter": f"{counter.name}/{counter.version} (exact={counter.exact})",
        "cases": len(cases),
        "rows": rows,
        "timing": {
            "route_all_seconds": round(routed_at - started, 2),
            "pack_all_seconds": round(done - routed_at, 2),
            "peak_rss_mib": round(
                resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 1
            ),
        },
    }


def _pct(part: int, whole: int) -> float:
    return round(100.0 * part / whole, 1) if whole else 0.0


def render(report: dict[str, Any]) -> str:
    lines = [
        "PAE context compiler — packing diagnostics",
        f"  {report['disclosure']}",
        f"  renderer {report['renderer']}   counter {report['counter']}"
        f"   cases {report['cases']}",
        "",
        f"  {'budget':>7} {'cases':>6} {'nonempty':>9} {'top1':>6} {'top3':>6} "
        f"{'inc':>5} {'util50':>7} {'util95':>7} {'over':>5} {'budg':>5} "
        f"{'nobody':>7} {'amb':>4} {'collapse':>9} {'room':>6} {'sg':>4} {'sgTrunc':>8} {'viol':>5}",
    ]
    for row in report["rows"]:
        lines.append(
            f"  {row['budget_estimated_tokens']:>7} {row['cases']:>6} "
            f"{row['non_empty_rate']:>8.1f}% {row['top1_retention']:>5.1f}% "
            f"{row['top3_retention']:>5.1f}% {row['mean_included']:>5.2f} "
            f"{row['utilization_median']:>6.1f}% {row['utilization_p95']:>6.1f}% "
            f"{row['oversized_skips']:>5} {row['budget_skips']:>5} "
            f"{row['no_body_omissions']:>7} {row['ambiguous_cases']:>4} "
            f"{row['ambiguous_single_scope_collapse']:>8.1f}% "
            f"{row['ambiguous_collapse_with_room']:>5.1f}% "
            f"{row['safety_gated_included']:>4} {row['safety_gated_truncations']:>8} "
            f"{row['final_render_violations']:>5}"
        )
    timing = report["timing"]
    lines += [
        "",
        f"  routed {report['cases']} cases in {timing['route_all_seconds']}s; "
        f"packed {len(report['rows'])} budgets in {timing['pack_all_seconds']}s; "
        f"peak RSS {timing['peak_rss_mib']} MiB",
        "",
        "  collapse = ambiguous bundles holding one scope; room = those that held two",
        "  or more bodies and still one scope, i.e. a collapse with space to avoid it.",
        "  sgTrunc and viol are assertions, not measurements: both must be 0.",
    ]
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--repo", default=None, help="path to a PAE checkout")
    parser.add_argument("--json", action="store_true", help="machine-readable summary")
    args = parser.parse_args(list(sys.argv[1:] if argv is None else argv))

    report = measure(args.repo)
    if args.json:
        print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    else:
        print(render(report))

    failures = [
        row
        for row in report["rows"]
        if row["safety_gated_truncations"]
        or row["final_render_violations"]
        or row["compile_errors"]
    ]
    if failures:
        print(
            "\nFAIL: a guarded body was shortened, a bundle exceeded the budget it "
            "reported, or a compile raised.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
