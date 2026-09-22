#!/usr/bin/env python3
"""cluster.py — find exact and candidate near-duplicate clusters in a corpus.

Part of ai-governance-audit-kit. Stdlib-only; no network, no LLM, no embeddings.

**Why this exists.** Duplicate handling in the parent repository is deliberately
edge-based: ``copy_of`` / ``copies`` are asserted from explicit ledger entries,
"never hashes or filenames" (ADR-0012). That is the right rule for a repository
that knows its own provenance, and it is useless on a client corpus that has no
ledger. So an audit needs detection, and detection must never masquerade as
provenance.

**Two tiers, and they are not the same claim.**

* ``exact`` — byte-identical content, evidenced by ``source.content_sha256``.
  This is free: every inventory record already carries the hash.
* ``candidate`` — lexically similar, evidenced by BM25F query-by-document over
  the Engine's own index. A finding for a human to adjudicate, never a copy.

**Neither tier names a canonical.** An audit cannot tell which of two
byte-identical files is the original; a file's mtime is a checkout artifact and
its path is not evidence. ``canonical_uid`` is therefore ``null`` with a stated
basis, mirroring ``pae_registry/governance.py``'s refusal to infer a quality
tier from document structure. The client names the canonical; the kit hands
them the cluster.

**The ranking is the Engine's, not a second implementation.** This script
imports ``pae_engine._lexical`` and scores through the same ``LexicalIndex``
that ``pae search`` uses, so a cluster the audit reports is a cluster the
handed-back registry will reproduce. A private BM25F here would eventually
disagree with the tool the client ends up running.

**Normalization.** Raw BM25F sums are not comparable across documents — a long
document generates more query terms and therefore a larger score. Each pair is
scored in both directions and divided by the querying document's self-score,
which is the maximum that query can reach, giving a ratio in [0, 1]. The
reported similarity is the **minimum** of the two directions: a short document
whose every term appears inside a long one scores high one way and low the
other, and calling that a near-duplicate is the false positive this choice
exists to prevent.

Usage:
  python3 cluster.py --inventory PATH [--out PATH] [--json]
  python3 cluster.py <corpus_dir> [--config PATH] [--out PATH] [--json]
  python3 cluster.py --self-check

Exit code: 0 always for a successful analysis (clusters are findings, not
failures); 1 if the inventory could not be read or Gate 0 blocked it;
2 = usage error.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
KIT_ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PAE_ROOT = os.path.dirname(KIT_ROOT)

sys.path.insert(0, os.path.join(PAE_ROOT, "pae-engine", "src"))
try:
    from pae_engine._lexical import (  # noqa: E402  (intentional: after path shim)
        FIELDS,
        MAX_QUERY_TOKENS,
        Document,
        LexicalIndex,
    )
    from pae_engine.models import Record  # noqa: E402
except ImportError as exc:  # pragma: no cover - environment defect, not input
    raise SystemExit(
        "ai-governance-audit-kit scores clusters through the Engine's own BM25F "
        f"index; expected {os.path.join(PAE_ROOT, 'pae-engine', 'src')} ({exc})."
    ) from exc


def _load_inventory_module():
    """Load the sibling skill's inventory module by path.

    By path rather than by import because skill bundles are independent
    directories with no shared package, and because a second copy of the
    membership rules is exactly the drift this kit exists to find.
    """
    path = os.path.join(KIT_ROOT, "skills", "corpus-inventory", "scripts", "inventory.py")
    spec = importlib.util.spec_from_file_location("kit_inventory", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------- records


def as_record(resource):
    """Project one inventory resource into a registry-shaped record.

    Only the fields the lexical index reads are populated. This is not the
    handback record — that is ``registry-handback``'s job and carries the
    governance and serving-policy blocks this one has no business inventing.
    """
    return Record.from_raw({
        "schema_version": "pae-registry-record/1",
        "uid": resource["uid"],
        "id": resource["id"],
        "kind": resource["kind"],
        "aliases": [],
        "lifecycle": "live",
        "title": resource.get("title") or "",
        "description": resource.get("description"),
        "serving_policy": {"value": "standard"},
        "source": {
            "path": resource["path"],
            "birth_path": resource["path"],
            "content_sha256": resource["content_sha256"],
            "checksum_payload": "raw_source_bytes",
        },
        "native": {
            "category": resource.get("scope"),
            "tags": resource.get("tags") or [],
            "techniques": resource.get("techniques") or [],
            "name": resource.get("title") or "",
        },
        "relationships": {},
    })


# ---------------------------------------------------------------- exact


def exact_clusters(resources):
    """Group byte-identical artifacts. The hash is the whole evidence."""
    by_hash = {}
    for resource in resources:
        by_hash.setdefault(resource["content_sha256"], []).append(resource)
    clusters = []
    for digest, members in sorted(by_hash.items()):
        if len(members) < 2:
            continue
        members = sorted(members, key=lambda r: r["path"])
        clusters.append({
            "status": "exact",
            "canonical_uid": None,
            "canonical_basis": (
                "undetermined — byte-identical files carry no evidence of which "
                "came first; mtime is a checkout artifact and a path is not "
                "provenance. The corpus owner names the canonical."
            ),
            "member_uids": [m["uid"] for m in members],
            "member_paths": [m["path"] for m in members],
            "similarity": 1.0,
            "evidence": {
                "basis": "source.content_sha256 equality",
                "content_sha256": digest,
            },
        })
    return clusters


# ---------------------------------------------------------------- candidate


def _query_terms(document):
    """Every normalized term the document carries, deduplicated and capped.

    Capped at the Engine's own ``MAX_QUERY_TOKENS`` so a very long artifact
    cannot be scored under a query the Engine would itself refuse.
    """
    terms = Counter()
    for field in FIELDS:
        terms.update(document.fields[field])
    ordered = [term for term, _ in terms.most_common()]
    return ordered[:MAX_QUERY_TOKENS]


def candidate_clusters(resources, threshold=0.35, max_neighbours=5, exclude_pairs=()):
    """All-pairs query-by-document over the Engine's BM25F index."""
    documents = [Document(as_record(r)) for r in resources]
    if len(documents) < 2:
        return []
    index = LexicalIndex(documents)
    by_position = {position: document for position, document in enumerate(documents)}

    directed = {}
    term_sets = {}
    for position, document in by_position.items():
        terms = _query_terms(document)
        term_sets[position] = set(terms)
        scores = index.score(terms)
        anchor = scores.get(position)
        if not anchor:
            continue
        for other, score in scores.items():
            if other == position:
                continue
            directed[(position, other)] = score / anchor

    excluded = {frozenset(pair) for pair in exclude_pairs}
    pairs = []
    seen = set()
    for (a, b) in directed:
        key = frozenset((a, b))
        if key in seen:
            continue
        seen.add(key)
        forward = directed.get((a, b), 0.0)
        backward = directed.get((b, a), 0.0)
        similarity = min(forward, backward)
        if similarity < threshold:
            continue
        left, right = sorted((a, b), key=lambda p: by_position[p].id)
        uid_key = frozenset((by_position[left].uid, by_position[right].uid))
        if uid_key in excluded:
            continue
        shared = sorted(term_sets[left] & term_sets[right])
        pairs.append({
            "status": "candidate",
            "canonical_uid": None,
            "canonical_basis": (
                "undetermined — lexical similarity is not provenance. This is a "
                "finding for the corpus owner to adjudicate, not an asserted copy "
                "(ADR-0012: copies come from explicit edges, never from hashes or "
                "filenames)."
            ),
            "member_uids": [by_position[left].uid, by_position[right].uid],
            "member_paths": [resources[left]["path"], resources[right]["path"]],
            "similarity": round(similarity, 4),
            "evidence": {
                "basis": "BM25F query-by-document over pae_engine._lexical.LexicalIndex",
                "directional": {
                    resources[left]["path"]: round(directed.get((left, right), 0.0), 4),
                    resources[right]["path"]: round(directed.get((right, left), 0.0), 4),
                },
                "reported": "minimum of the two directions",
                "shared_terms": shared[:20],
                "shared_term_count": len(shared),
            },
        })

    pairs.sort(key=lambda c: (-c["similarity"], c["member_paths"]))
    # Per-artifact neighbour cap, applied after ordering so the strongest
    # candidates survive the cap rather than whichever happened to be walked
    # first.
    kept = []
    seen_counts = Counter()
    for cluster in pairs:
        if any(seen_counts[uid] >= max_neighbours for uid in cluster["member_uids"]):
            continue
        for uid in cluster["member_uids"]:
            seen_counts[uid] += 1
        kept.append(cluster)
    return kept


# ---------------------------------------------------------------- analyse


def analyse(inventory, cfg):
    resources = inventory["resources"]
    clustering = cfg.get("clustering") or {}
    exact = exact_clusters(resources)
    exact_pairs = set()
    for cluster in exact:
        uids = cluster["member_uids"]
        for i, left in enumerate(uids):
            for right in uids[i + 1:]:
                exact_pairs.add(frozenset((left, right)))
    candidates = candidate_clusters(
        resources,
        threshold=float(clustering.get("candidate_threshold", 0.35)),
        max_neighbours=int(clustering.get("max_neighbours", 5)),
        exclude_pairs=exact_pairs,
    )
    return {
        "corpus_label": inventory.get("corpus_label"),
        "resources_analysed": len(resources),
        "exact_clusters": exact,
        "candidate_clusters": candidates,
        "disclosure": (
            "Exact clusters are byte-identical, evidenced by content hash. "
            "Candidate clusters are lexical near-neighbours and are findings for "
            "adjudication, not asserted copies. No cluster names a canonical: "
            "this kit cannot infer provenance and does not pretend to."
        ),
        "method": {
            "exact": "source.content_sha256 equality",
            "candidate": "BM25F query-by-document via pae_engine._lexical",
            "normalization": "score / querying document's self-score, min of both directions",
            "threshold": float(clustering.get("candidate_threshold", 0.35)),
            "max_neighbours_per_artifact": int(clustering.get("max_neighbours", 5)),
        },
    }


# ---------------------------------------------------------------- cli


def _inventory_for(args, inventory_module):
    if args.inventory:
        with open(args.inventory, encoding="utf-8") as fh:
            return json.load(fh), inventory_module.load_config(args.config)
    cfg = inventory_module.load_config(args.config)
    inventory = inventory_module.discover(args.corpus, cfg)
    passed, unmet = inventory_module.gate_0(inventory)
    inventory["gate_0"] = {"passed": passed, "unmet": unmet}
    return inventory, cfg


def report(result, as_json=False):
    if as_json:
        print(json.dumps(result, indent=2, sort_keys=True))
        return
    print(f"clusters — {result['corpus_label']} "
          f"({result['resources_analysed']} artifacts analysed)")
    print(f"  exact:     {len(result['exact_clusters'])}")
    for cluster in result["exact_clusters"]:
        print(f"    [exact]     {' == '.join(cluster['member_paths'])}")
    print(f"  candidate: {len(result['candidate_clusters'])}")
    for cluster in result["candidate_clusters"]:
        print(f"    [candidate] {cluster['similarity']:.2f}  "
              f"{' ~ '.join(cluster['member_paths'])}")
    print("  canonical: never inferred — see the disclosure in the JSON output")


def self_check():
    inventory_module = _load_inventory_module()
    cfg = inventory_module.load_config()
    corpus = os.path.join(KIT_ROOT, "samples", "corpus-good")
    inventory = inventory_module.discover(corpus, cfg)
    result = analyse(inventory, cfg)
    print("cluster --self-check:")
    report(result)

    checks = []

    exact_paths = {tuple(c["member_paths"]) for c in result["exact_clusters"]}
    checks.append((
        "the byte-identical pair is reported as exact",
        ("prompts/analysis_dependency_review.md",
         "prompts/analysis_dependency_review_copy.md") in exact_paths,
    ))
    checks.append((
        "no exact cluster names a canonical",
        all(c["canonical_uid"] is None for c in result["exact_clusters"]),
    ))

    candidate_pairs = {
        frozenset(c["member_paths"]) for c in result["candidate_clusters"]
    }
    checks.append((
        "the reworded near-duplicate is reported as a candidate",
        frozenset({"prompts/analysis_dependency_audit.md",
                   "prompts/analysis_dependency_review.md"}) in candidate_pairs,
    ))
    checks.append((
        "the exact pair is not double-reported as a candidate",
        frozenset({"prompts/analysis_dependency_review.md",
                   "prompts/analysis_dependency_review_copy.md"})
        not in candidate_pairs,
    ))
    checks.append((
        "an unrelated artifact is not clustered with the dependency set",
        not any("prompts/analysis_incident_timeline.md" in c["member_paths"]
                for c in result["candidate_clusters"]),
    ))
    checks.append((
        "no cluster asserts a copy_of edge",
        "copy_of" not in json.dumps(result),
    ))

    ok = True
    for label, passed in checks:
        if not passed:
            ok = False
        print(f"   -> {label}: {'ok' if passed else 'UNEXPECTED'}")
    print("SELF-CHECK", "PASS" if ok else "FAIL")
    return ok


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="cluster.py",
        description="Find exact and candidate near-duplicate clusters in a corpus.",
        epilog="Exit codes: 0 = analysed, 1 = inventory unusable, 2 = usage error.")
    parser.add_argument("corpus", nargs="?", help="corpus root (inventoried on the fly)")
    parser.add_argument("--inventory", help="an inventory JSON written by inventory.py")
    parser.add_argument("--config", help="audit config (default: config/audit.json)")
    parser.add_argument("--json", action="store_true", help="emit the full result as JSON")
    parser.add_argument("--out", help="also write the result JSON to this path")
    parser.add_argument("--self-check", action="store_true",
                        help="run the regression suite against the tracked samples/ fixtures")
    args = parser.parse_args(argv)

    if args.self_check:
        return 0 if self_check() else 1
    if not args.corpus and not args.inventory:
        parser.error("a corpus directory or --inventory is required (or use --self-check)")

    inventory_module = _load_inventory_module()
    try:
        inventory, cfg = _inventory_for(args, inventory_module)
    except (OSError, json.JSONDecodeError, inventory_module.ConfigError) as exc:
        print(f"ERROR  inventory unusable: {exc}")
        return 1
    gate = inventory.get("gate_0") or {}
    if gate and not gate.get("passed"):
        print("ERROR  Gate 0 blocked this corpus; clustering an un-inventoriable "
              "corpus would report zero duplicates it cannot support")
        for reason in gate.get("unmet", []):
            print(f"        - {reason}")
        return 1

    result = analyse(inventory, cfg)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=2, sort_keys=True)
            fh.write("\n")
    report(result, as_json=args.json)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
