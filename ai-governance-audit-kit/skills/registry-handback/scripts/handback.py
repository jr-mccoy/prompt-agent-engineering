#!/usr/bin/env python3
"""handback.py — write a conformant PAE registry into the audited tree.

Part of ai-governance-audit-kit. Stdlib-only; no network, no LLM.

**This is the move that turns a report into an asset.** ``Repository.at()``
requires exactly two marker files at fixed relative paths —
``meta/registry/registry.jsonl`` and ``meta/registry/registry-summary.json`` —
plus supported schema versions. Nothing ties the Engine to *this* repository's
content, only to that contract (ADR-0018). So a conformant ``meta/registry/``
written into the client's own tree makes the whole Engine — search, routing,
context bundling, validation, MCP — work on their corpus unchanged, and
``PAE_REPO`` makes pointing it there a one-liner.

The registry is written **inside the audited corpus**, not beside it, because
``pae validate-registry`` resolves every record's ``source.path`` against the repository
root. A registry whose sources do not resolve is a report, not a handback.

**What this refuses to invent.**

* ``governance.maturity`` is ``experimental`` and both review and eval statuses
  are ``unknown`` for every record. ``pae_registry/governance.py`` already
  refuses to assert a quality tier, in terms that bind here: *"inferring one
  from document structure would be fabricating a rubric score."*
* ``relationships.copy_of`` is ``null`` and ``copies`` is empty **even where a
  cluster was found**. Copies come from explicit edges, never from hashes or
  filenames (ADR-0012). Cluster findings are written as ``diagnostics`` —
  observations with evidence — so the client can adjudicate them and then
  assert the edges themselves.
* ``license.status`` is ``unresolved``. An audit that guesses a client's
  licensing has invented the one fact most expensive to get wrong.
* ``quality`` carries the observed structural coverage under its own scheme,
  never ``prompt-quality-tier``.

Gate C — HANDBACK COMPLETE. The gate is the Engine's own verdict, obtained by
calling ``validate_registry`` in process rather than by trusting that the files
look right. A handback is complete when the Engine can open the tree and
validation returns no issues.

Usage:
  python3 handback.py <corpus_dir> [--config PATH] [--write] [--json]
  python3 handback.py --self-check

Without ``--write`` the registry is built and validated in a temporary copy of
the marker files, and the corpus is left untouched.

Exit code: 0 = Gate C PASS, 1 = Gate C BLOCKED, 2 = usage error.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
KIT_ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PAE_ROOT = os.path.dirname(KIT_ROOT)

sys.path.insert(0, os.path.join(PAE_ROOT, "pae-engine", "src"))
try:
    from pae_engine.repository import Repository  # noqa: E402 (after path shim)
    from pae_engine.validate import validate_registry  # noqa: E402
    from pae_engine.errors import PaeError  # noqa: E402
except ImportError as exc:  # pragma: no cover - environment defect, not input
    raise SystemExit(
        "Gate C is the Engine's own verdict, so the Engine must be importable; "
        f"expected {os.path.join(PAE_ROOT, 'pae-engine', 'src')} ({exc})."
    ) from exc

RECORD_SCHEMA = "pae-registry-record/1"
SUMMARY_SCHEMA = "pae-registry-summary/1"
REGISTRY_RELPATH = os.path.join("meta", "registry", "registry.jsonl")
SUMMARY_RELPATH = os.path.join("meta", "registry", "registry-summary.json")


def _load(name, relative):
    path = os.path.join(KIT_ROOT, relative)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


inventory_module = _load("kit_inventory", "skills/corpus-inventory/scripts/inventory.py")
cluster_module = _load("kit_cluster", "skills/duplication-clusters/scripts/cluster.py")
score_module = _load("kit_score", "skills/observed-scoring/scripts/observed_score.py")


# ---------------------------------------------------------------- records


def build_records(inventory, clusters, scores):
    """One record per inventoried artifact. Nothing is inferred into it."""
    diagnostics_by_uid = {}

    for cluster in clusters["exact_clusters"]:
        for uid in cluster["member_uids"]:
            others = [p for p, u in zip(cluster["member_paths"], cluster["member_uids"])
                      if u != uid]
            diagnostics_by_uid.setdefault(uid, []).append({
                "code": "exact_duplicate_detected",
                "severity": "warning",
                "detail": (
                    "byte-identical to " + ", ".join(others) +
                    " (evidence: " + cluster["evidence"]["content_sha256"] + "). "
                    "No copy_of edge is asserted: which file is the canonical is "
                    "the corpus owner's to declare."
                ),
            })

    for cluster in clusters["candidate_clusters"]:
        for uid in cluster["member_uids"]:
            others = [p for p, u in zip(cluster["member_paths"], cluster["member_uids"])
                      if u != uid]
            diagnostics_by_uid.setdefault(uid, []).append({
                "code": "near_duplicate_candidate",
                "severity": "info",
                "detail": (
                    f"lexical near-neighbour of {', '.join(others)} at similarity "
                    f"{cluster['similarity']} ({cluster['evidence']['basis']}, "
                    f"{cluster['evidence']['shared_term_count']} shared terms). "
                    "A candidate for adjudication, not an asserted copy."
                ),
            })

    for uid, record in scores.items():
        for finding in record["findings"]:
            diagnostics_by_uid.setdefault(uid, []).append({
                "code": "structural_finding",
                "severity": "error" if finding.get("severity") == "blocking" else "info",
                "detail": f"{finding['check']}: {finding['detail']}",
            })

    records = []
    for resource in inventory["resources"]:
        uid = resource["uid"]
        score_record = scores.get(uid)
        quality = []
        if score_record:
            coverage = score_record["structural_coverage"]
            quality.append({
                # Deliberately not "prompt-quality-tier". The scheme name says
                # what the number is and how it was obtained, so a later reader
                # cannot mistake it for a tier.
                "scheme": "structural-coverage-observed",
                "value": f"{coverage['observed']}/{coverage['observable_max']}",
                "evidence": (
                    f"observed by detector against {score_record['rubric']['name']} "
                    f"{score_record['rubric']['version']}; "
                    f"{coverage['observable_max']} of {coverage['rubric_max']} rubric "
                    "points are mechanically observable"
                ),
            })
        records.append({
            "schema_version": RECORD_SCHEMA,
            "uid": uid,
            "id": resource["id"],
            "kind": resource["kind"],
            "aliases": [],
            "lifecycle": "live",
            "title": resource["title"],
            "description": resource.get("description"),
            "metadata_completeness": "full" if resource["has_frontmatter"] else "minimal",
            "governance": {
                "maturity": "experimental",
                "review_status": "unknown",
                "eval_status": "unknown",
                "eval_artifacts": [],
            },
            "license": {
                "status": "unresolved",
                "basis": "not determined by this audit",
                "spdx": None,
            },
            "provenance": {"origin": "unknown"},
            "quality": quality,
            "relationships": {
                "copy_of": None,
                "copies": [],
                "supersedes": [],
                "superseded_by": None,
                "merges": [],
                "merged_into": None,
                "split_into": [],
                "attachments": [],
            },
            "serving_policy": {
                "value": "standard",
                "basis": ["audit default; no client serving policy was supplied"],
            },
            "source": {
                "path": resource["path"],
                "birth_path": resource["path"],
                "previous_paths": [],
                "content_sha256": resource["content_sha256"],
                "checksum_payload": "raw_source_bytes",
            },
            "native": {
                "category": resource.get("scope"),
                "tags": resource.get("tags") or [],
                "techniques": resource.get("techniques") or [],
            },
            "diagnostics": sorted(
                diagnostics_by_uid.get(uid, []),
                key=lambda d: (d["code"], d["detail"]),
            ),
            "derived_fields": [],
        })
    records.sort(key=lambda r: r["id"])
    return records


def build_summary(records, inventory):
    def tally(key):
        counts = {}
        for record in records:
            value = key(record)
            counts[value] = counts.get(value, 0) + 1
        return dict(sorted(counts.items()))

    live = [r for r in records if r["lifecycle"] == "live"]
    tombstones = [r for r in records if r["lifecycle"] == "tombstone"]
    diagnostics = {}
    for record in records:
        for diagnostic in record["diagnostics"]:
            diagnostics[diagnostic["code"]] = diagnostics.get(diagnostic["code"], 0) + 1

    return {
        "schema": SUMMARY_SCHEMA,
        "total_records": len(records),
        "by_kind": tally(lambda r: r["kind"]),
        "by_kind_live": dict(sorted(
            {k: sum(1 for r in live if r["kind"] == k)
             for k in {r["kind"] for r in live}}.items())),
        "by_kind_tombstone": dict(sorted(
            {k: sum(1 for r in tombstones if r["kind"] == k)
             for k in {r["kind"] for r in tombstones}}.items())),
        "by_lifecycle": tally(lambda r: r["lifecycle"]),
        "by_serving_policy": tally(lambda r: r["serving_policy"]["value"]),
        "by_maturity": tally(lambda r: r["governance"]["maturity"]),
        "by_metadata_completeness": tally(lambda r: r["metadata_completeness"]),
        "by_review_status": tally(lambda r: r["governance"]["review_status"]),
        "by_license_status": tally(lambda r: r["license"]["status"]),
        "diagnostics_by_code": dict(sorted(diagnostics.items())),
        "membership": {
            "file_backed_candidates": len(records),
            "exclusion_reasons": inventory["excluded"],
        },
        "audit": {
            "produced_by": "ai-governance-audit-kit",
            "corpus_label": inventory.get("corpus_label"),
            "disclosure": (
                "Governance fields are unknown by construction. This audit "
                "observes structure; it does not review content, and it asserts "
                "no quality tier, no copy edge and no licence."
            ),
        },
    }


# ---------------------------------------------------------------- write


def write_registry(root, records, summary):
    registry_dir = os.path.join(root, "meta", "registry")
    os.makedirs(registry_dir, exist_ok=True)
    with open(os.path.join(root, REGISTRY_RELPATH), "w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, sort_keys=True) + "\n")
    with open(os.path.join(root, SUMMARY_RELPATH), "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2, sort_keys=True)
        fh.write("\n")
    return registry_dir


# ---------------------------------------------------------------- gate C


def gate_c(root):
    """Return ``(passed, unmet, checked)``. The verdict is the Engine's own."""
    unmet = []
    for relpath in (REGISTRY_RELPATH, SUMMARY_RELPATH):
        if not os.path.isfile(os.path.join(root, relpath)):
            unmet.append(f"marker file missing: {relpath}")
    if unmet:
        return False, unmet, {}

    try:
        repository = Repository.at(root)
    except PaeError as exc:
        return False, [f"the Engine cannot open the handback: {exc}"], {}

    try:
        report = validate_registry(repository, verify_checksums=True)
    except PaeError as exc:
        return False, [f"validation could not complete: {exc}"], {}

    for issue in report.issues:
        unmet.append(f"[{issue.code}] {issue.message}")
    return report.ok, unmet, dict(report.checked)


def assert_nothing_invented(records):
    """Belt-and-braces: the refusals above are structural, so prove them."""
    problems = []
    for record in records:
        rels = record["relationships"]
        if rels["copy_of"] or rels["copies"]:
            problems.append(f"{record['id']} asserts a copy edge the audit cannot know")
        if record["governance"]["review_status"] != "unknown":
            problems.append(f"{record['id']} asserts a review status")
        for assertion in record["quality"]:
            if assertion["scheme"] == "prompt-quality-tier":
                problems.append(f"{record['id']} asserts a quality tier")
    return problems


# ---------------------------------------------------------------- pipeline


def produce(corpus, cfg):
    """Run the whole chain and return everything the gate and report need."""
    inventory = inventory_module.discover(corpus, cfg)
    passed, unmet = inventory_module.gate_0(inventory)
    inventory["gate_0"] = {"passed": passed, "unmet": unmet}
    if not passed:
        return inventory, None, None, None

    clusters = cluster_module.analyse(inventory, cfg)
    scores = {}
    for resource in inventory["resources"]:
        if resource["kind"] != "skill":
            continue
        bundle = os.path.join(corpus, os.path.dirname(resource["path"]))
        record = score_module.score(bundle, cfg)
        gate_passed, gate_unmet = score_module.gate_a(record)
        record["gate_a"] = {"passed": gate_passed, "unmet": gate_unmet}
        scores[resource["uid"]] = record

    records = build_records(inventory, clusters, scores)
    summary = build_summary(records, inventory)
    return inventory, clusters, scores, (records, summary)


def run_one(corpus, cfg, write=False, as_json=False):
    inventory, clusters, scores, built = produce(corpus, cfg)
    if built is None:
        print("BLOCK  Gate C (handback complete) — Gate 0 blocked this corpus")
        for reason in inventory["gate_0"]["unmet"]:
            print(f"        - {reason}")
        return False

    records, summary = built
    invented = assert_nothing_invented(records)

    blocked_scores = [
        uid for uid, record in scores.items() if not record["gate_a"]["passed"]
    ]

    if write:
        write_registry(corpus, records, summary)
        passed, unmet, checked = gate_c(corpus)
        root = corpus
    else:
        # Validate against a staged copy so a dry run cannot leave a partial
        # registry in a client tree. The corpus is copied, not moved, and the
        # copy is discarded.
        with tempfile.TemporaryDirectory() as staging:
            root = os.path.join(staging, "corpus")
            shutil.copytree(corpus, root)
            write_registry(root, records, summary)
            passed, unmet, checked = gate_c(root)

    if invented:
        passed = False
        unmet = [f"[invented_fact] {problem}" for problem in invented] + unmet
    if blocked_scores:
        passed = False
        unmet = [
            f"[gate_a] {uid} carries a score Gate A rejects, so it cannot be handed back"
            for uid in blocked_scores
        ] + unmet

    result = {
        "corpus": os.path.abspath(corpus),
        "written": bool(write),
        "records": len(records),
        "gate_c": {"passed": passed, "unmet": unmet, "engine_checked": checked},
    }
    if as_json:
        print(json.dumps(result, indent=2, sort_keys=True))
        return passed

    print(f"{'PASS' if passed else 'BLOCK'}  Gate C (handback complete) — "
          f"{len(records)} record(s), "
          f"{'written into' if write else 'staged from'} {os.path.abspath(corpus)}")
    if checked:
        print(f"        engine: {checked.get('records')} records, "
              f"{checked.get('unique_uids')} unique UIDs, "
              f"summary schema {checked.get('summary_schema')}")
    for reason in unmet:
        print(f"        - {reason}")
    return passed


def self_check():
    print("handback --self-check:")
    cfg = inventory_module.load_config()
    ok = True

    good = os.path.join(KIT_ROOT, "samples", "corpus-good")
    passed = run_one(good, cfg)
    ok = ok and passed
    print(f"   -> corpus-good stages and validates: {'ok' if passed else 'UNEXPECTED'}")

    empty = os.path.join(KIT_ROOT, "samples", "corpus-empty")
    blocked = not run_one(empty, cfg)
    ok = ok and blocked
    print(f"   -> corpus-empty is refused before a registry is built: "
          f"{'ok' if blocked else 'UNEXPECTED'}")

    # The Engine must actually be able to open and search what was written.
    inventory, clusters, scores, built = produce(good, cfg)
    records, summary = built
    with tempfile.TemporaryDirectory() as staging:
        root = os.path.join(staging, "corpus")
        shutil.copytree(good, root)
        write_registry(root, records, summary)
        try:
            repository = Repository.at(root)
            opened = True
        except PaeError:
            opened = False
        ok = ok and opened
        print(f"   -> the unmodified Engine opens the handback: "
              f"{'ok' if opened else 'UNEXPECTED'}")

        # A tampered record must be caught, or Gate C proves nothing.
        with open(os.path.join(root, REGISTRY_RELPATH), encoding="utf-8") as fh:
            lines = fh.readlines()
        tampered = json.loads(lines[0])
        tampered["source"]["content_sha256"] = "sha256:" + "0" * 64
        lines[0] = json.dumps(tampered, sort_keys=True) + "\n"
        with open(os.path.join(root, REGISTRY_RELPATH), "w", encoding="utf-8") as fh:
            fh.writelines(lines)
        caught, unmet, _ = gate_c(root)
        detected = (not caught) and any("checksum_mismatch" in u for u in unmet)
        ok = ok and detected
        print(f"   -> a tampered checksum is caught by Gate C: "
              f"{'ok' if detected else 'UNEXPECTED'}")

    invented = assert_nothing_invented(records)
    ok = ok and not invented
    print(f"   -> no record asserts a copy edge, review status or tier: "
          f"{'ok' if not invented else 'UNEXPECTED'}")

    clustered = sum(
        1 for record in records
        for diagnostic in record["diagnostics"]
        if diagnostic["code"] in ("exact_duplicate_detected", "near_duplicate_candidate")
    )
    carried = clustered > 0
    ok = ok and carried
    print(f"   -> cluster findings ride as diagnostics, not edges: "
          f"{'ok' if carried else 'UNEXPECTED'} ({clustered} diagnostic(s))")

    print("SELF-CHECK", "PASS" if ok else "FAIL")
    return ok


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="handback.py",
        description="Write a conformant PAE registry into the audited tree.",
        epilog="Exit codes: 0 = Gate C PASS, 1 = Gate C BLOCKED, 2 = usage error.")
    parser.add_argument("corpus", nargs="?", help="the corpus root to hand back")
    parser.add_argument("--config", help="audit config (default: config/audit.json)")
    parser.add_argument("--write", action="store_true",
                        help="write meta/registry/ into the corpus (default: stage and discard)")
    parser.add_argument("--json", action="store_true", help="emit the result as JSON")
    parser.add_argument("--self-check", action="store_true",
                        help="run the regression suite against the tracked samples/ fixtures")
    args = parser.parse_args(argv)

    if args.self_check:
        return 0 if self_check() else 1
    if not args.corpus:
        parser.error("a corpus directory is required (or use --self-check)")
    if not os.path.isdir(args.corpus):
        parser.error(f"{args.corpus} is not a directory")
    try:
        cfg = inventory_module.load_config(args.config)
    except inventory_module.ConfigError as exc:
        print(f"BLOCK  Gate C (handback complete) — config rejected\n        - {exc}")
        return 1
    return 0 if run_one(args.corpus, cfg, write=args.write, as_json=args.json) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
