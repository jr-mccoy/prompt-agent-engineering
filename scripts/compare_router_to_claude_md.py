#!/usr/bin/env python3
"""Compare the executable router against the hand-written routing table.

    PYTHONPATH=pae-engine/src python3 scripts/compare_router_to_claude_md.py

Migration diagnostics, and nothing else. `meta/ROUTING_REFERENCE.md` (split out
of `CLAUDE.md`, which now carries only the always-loaded essentials) carries
roughly 1,500 hand-written ``"user phrase" -> resource`` mappings that predate the search
implementation. They are the closest thing the repository has to an
independent opinion about where a task should go, so agreement with them is
useful evidence about whether an executable router could eventually replace
the mechanical part of that table.

Three things this is NOT:

* not a benchmark — the phrases are documentation labels, not user queries,
  and many share vocabulary with their target's title, which flatters any
  lexical ranker;
* not a correctness oracle — where the router and the table disagree, either
  may be right, and some table rows are stale;
* not a licence to edit the table so the numbers improve. The table is
  evidence. Rewriting evidence to match a measurement is how a repository
  starts lying to itself.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

#: Rows shaped ``| "user phrase" | `path/to/resource.md` |``.
_TABLE_ROW = re.compile(r'^\|\s*"([^"]{6,160})"\s*\|\s*(.+?)\s*\|\s*$', re.M)
#: Bullets shaped ``- Example: "user phrase" -> `path/to/resource.md```.
_EXAMPLE = re.compile(r'Example:\s*"([^"]{6,180})"\s*→\s*`([^`]+)`')
_BACKTICKED_MD = re.compile(r"`([^`]+\.md)`")


def extract_pairs(text: str) -> list[tuple[str, list[str]]]:
    pairs: list[tuple[str, list[str]]] = []
    for phrase, cell in _TABLE_ROW.findall(text):
        targets = _BACKTICKED_MD.findall(cell)
        if targets:
            pairs.append((phrase, targets))
    for phrase, target in _EXAMPLE.findall(text):
        pairs.append((phrase, [target]))
    return pairs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", default=str(REPO_ROOT))
    parser.add_argument("--router", default="meta/ROUTING_REFERENCE.md")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])

    from pae_engine import Registry, Repository, Router, SearchEngine

    repository = Repository.at(args.repo)
    registry = Registry.open(repository)
    engine = SearchEngine(registry)
    router = Router(engine)

    by_path = {r.source_path: r for r in registry.load_all() if r.source_path}

    raw_pairs = extract_pairs((Path(args.repo) / args.router).read_text(encoding="utf-8"))
    resolved: dict[str, set[str]] = {}
    unresolved = 0
    for phrase, targets in raw_pairs:
        ids = {by_path[t].id for t in targets if t in by_path}
        if not ids:
            unresolved += 1
            continue
        resolved.setdefault(phrase.strip().casefold(), set()).update(ids)

    # A phrase's expected scopes are the scopes of its expected resources.
    engine.search("warm up the index")
    documents = engine._ensure_index().documents
    document_scope = {d.id: d.scope for d in documents}
    # A table row that names a canonical is not contradicted by a router that
    # returns that canonical's registered copy: it is the same logical
    # resource, and cluster dedup returns whichever member scores higher.
    document_cluster = {d.id: d.cluster_key for d in documents}

    totals = Counter()
    disagreements: Counter = Counter()
    examples: list[tuple[str, str, str]] = []
    for phrase, expected_ids in sorted(resolved.items()):
        expected_scopes = {document_scope[i] for i in expected_ids if i in document_scope}
        hits = engine.search(phrase, limit=3).hits
        ids = [hit.id for hit in hits]
        scopes = [hit.scope for hit in hits]
        totals["n"] += 1
        if ids[:1] and ids[0] in expected_ids:
            totals["resource@1"] += 1
        if expected_ids & set(ids):
            totals["resource@3"] += 1
        if expected_scopes:
            totals["n_scope"] += 1
            if scopes[:1] and scopes[0] in expected_scopes:
                totals["scope@1"] += 1
            if expected_scopes & set(scopes):
                totals["scope@3"] += 1
        same_cluster = bool(
            ids[:1]
            and document_cluster.get(ids[0])
            and document_cluster.get(ids[0])
            in {document_cluster.get(i) for i in expected_ids}
        )
        if same_cluster:
            totals["resource@1_same_cluster"] += 1
        if not (ids[:1] and ids[0] in expected_ids):
            if same_cluster:
                disagreements["same logical resource (registered copy)"] += 1
                continue
            decision = router.route(phrase)
            reason = _classify(ids, expected_ids, expected_scopes, document_scope, decision)
            disagreements[reason] += 1
            if len(examples) < 12:
                examples.append((phrase, ids[0] if ids else "-", sorted(expected_ids)[0]))

    rate = lambda a, b: (totals[a] / totals[b]) if totals[b] else 0.0  # noqa: E731
    report = {
        "parsed_pairs": len(raw_pairs),
        "unresolved_pairs": unresolved,
        "resolved_unique_phrases": totals["n"],
        "resource@1": rate("resource@1", "n"),
        "resource@1_including_registered_copies": rate("resource@1_same_cluster", "n"),
        "resource@3": rate("resource@3", "n"),
        "scope@1": rate("scope@1", "n_scope"),
        "scope@3": rate("scope@3", "n_scope"),
        "disagreement_categories": dict(disagreements.most_common()),
    }
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0

    print("Router vs hand-written routing table — migration diagnostics only")
    print("=" * 64)
    print(f"parsed pairs                {report['parsed_pairs']}")
    print(f"unresolved (globbed paths)  {report['unresolved_pairs']}")
    print(f"resolved unique phrases     {report['resolved_unique_phrases']}")
    print(f"resource@1                  {report['resource@1']:.1%}")
    print(f"  + registered copies       "
          f"{report['resource@1_including_registered_copies']:.1%}")
    print(f"resource@3                  {report['resource@3']:.1%}")
    print(f"scope@1                     {report['scope@1']:.1%}")
    print(f"scope@3                     {report['scope@3']:.1%}")
    print("\ntop disagreement categories")
    for reason, count in disagreements.most_common():
        print(f"  {count:>4}  {reason}")
    print("\nexamples (phrase -> router top hit vs table target)")
    for phrase, got, want in examples:
        print(f"  {phrase[:44]:<44}\n      got  {got}\n      want {want}")
    return 0


def _classify(ids, expected_ids, expected_scopes, document_scope, decision) -> str:
    """Why the router and the table differ, in observable terms."""
    if not ids:
        return "router returned nothing"
    if expected_ids & set(ids):
        return "table target present but not first"
    if expected_scopes and document_scope.get(ids[0]) in expected_scopes:
        return "same scope, different resource"
    if decision.status in ("ambiguous", "weak", "no_route"):
        return f"router declined to commit (status={decision.status})"
    return "different scope"


if __name__ == "__main__":
    raise SystemExit(main())
