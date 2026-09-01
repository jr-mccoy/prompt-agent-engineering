#!/usr/bin/env python3
"""Exercise an *installed* PAE Engine from outside the repository.

The unit suite imports ``pae_engine`` directly, which proves the code works but
not that the package works: a missing console entry point, a package left out
of the wheel, or a runtime dependency that only exists in the development
environment would all pass unit tests and fail a user.

So this drives the real ``pae`` binary as a subprocess, with the working
directory deliberately outside the checkout, and picks its own reference values
out of the registry rather than hard-coding identifiers that could rot.

    python3 smoke_install.py --repo /path/to/checkout [--pae /path/to/pae]

Exits 0 when every check passes, 1 otherwise.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

FAILURES: list[str] = []
CHECKS = 0


def run(pae: str, args: list[str], cwd: str, *, binary: bool = False):
    return subprocess.run(
        [pae, *args], cwd=cwd, capture_output=True, text=not binary, check=False
    )


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    if condition:
        print(f"  ok   {label}")
    else:
        print(f"  FAIL {label}{': ' + detail if detail else ''}")
        FAILURES.append(label)


def pick_references(repo: Path) -> dict[str, str]:
    """Choose live reference values from the registry under test."""
    chosen: dict[str, str] = {}
    with open(repo / "meta/registry/registry.jsonl", encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            policy = (record.get("serving_policy") or {}).get("value")
            source = record.get("source") or {}
            if (
                "servable" not in chosen
                and record["lifecycle"] == "live"
                and policy in ("standard", "safety_gated")
                and source.get("path")
                and source.get("content_sha256")
            ):
                chosen["servable"] = record["id"]
                chosen["servable_uid"] = record["uid"]
                chosen["servable_sha"] = source["content_sha256"]
            if "technique" not in chosen and record["kind"] == "technique":
                chosen["technique"] = record["id"]
            if "tombstone" not in chosen and record["lifecycle"] == "tombstone":
                chosen["tombstone"] = record["id"]
            if len(chosen) >= 5:
                break
    return chosen


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="a PAE checkout to query")
    parser.add_argument("--pae", default=shutil.which("pae") or "pae")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    pae = args.pae
    outside = tempfile.mkdtemp(prefix="pae-smoke-")

    print(f"pae binary : {pae}")
    print(f"checkout   : {repo}")
    print(f"cwd        : {outside}  (deliberately outside the checkout)\n")

    refs = pick_references(repo)

    print("no repository required")
    # Derived, not hard-coded: the invariant is that the console script reports
    # the same version the installed distribution declares. Pinning a literal
    # here just means editing it on every bump, and forgetting once.
    import importlib.metadata as _md

    expected_version = _md.version("prompt-agent-engineering")
    version = run(pae, ["--version"], outside)
    check("pae --version",
          version.returncode == 0 and f"pae {expected_version}" in version.stdout,
          f"expected {expected_version!r}; {version.stdout!r} {version.stderr}")
    version_json = run(pae, ["--version", "--json"], outside)
    payload = json.loads(version_json.stdout) if version_json.returncode == 0 else {}
    check("pae --version --json", payload.get("engine_version") == expected_version,
          f"expected {expected_version!r}, got {payload.get('engine_version')!r}")
    check("pae --help", run(pae, ["--help"], outside).returncode == 0)
    check(
        "module entry point",
        subprocess.run(
            [sys.executable, "-m", "pae_engine", "--version"],
            cwd=outside, capture_output=True, check=False,
        ).returncode == 0,
    )

    print("\nno checkout in reach")
    stranded = run(pae, ["stats"], outside)
    check("bare `pae stats` outside a checkout exits 3", stranded.returncode == 3,
          f"exit {stranded.returncode}")
    check("...and writes nothing to stdout", stranded.stdout == "")

    print("\ndiscovery and summary")
    where = run(pae, ["where", "--repo", str(repo), "--json"], outside)
    check("pae where --repo", where.returncode == 0
          and json.loads(where.stdout)["root"] == str(repo))
    check("pae stats", run(pae, ["stats", "--repo", str(repo)], outside).returncode == 0)
    stats_json = run(pae, ["stats", "--repo", str(repo), "--json"], outside)
    check("pae stats --json", stats_json.returncode == 0
          and json.loads(stats_json.stdout)["summary"]["total_records"] > 0)
    verified = run(pae, ["stats", "--repo", str(repo), "--verify", "--json"], outside)
    check("pae stats --verify", verified.returncode == 0
          and json.loads(verified.stdout)["verified"] is True, verified.stderr)

    print("\nlookup")
    by_id = run(pae, ["get", refs["servable"], "--repo", str(repo), "--json"], outside)
    by_uid = run(pae, ["get", refs["servable_uid"], "--repo", str(repo), "--json"], outside)
    check("pae get <public id> --json", by_id.returncode == 0, by_id.stderr)
    check("pae get <uid> --json", by_uid.returncode == 0, by_uid.stderr)
    if by_id.returncode == 0 and by_uid.returncode == 0:
        left = json.loads(by_id.stdout)["record"]
        right = json.loads(by_uid.stdout)["record"]
        check("uid and public id return the same resource",
              left["uid"] == right["uid"] and left["id"] == right["id"])

    print("\ncontent and integrity")
    content = run(pae, ["get", refs["servable"], "--repo", str(repo), "--content"],
                  outside, binary=True)
    digest = "sha256:" + hashlib.sha256(content.stdout).hexdigest()
    check("pae get --content succeeds", content.returncode == 0)
    check("raw content digest equals the registry checksum",
          digest == refs["servable_sha"], f"{digest} != {refs['servable_sha']}")

    if "technique" in refs:
        technique = run(pae, ["get", refs["technique"], "--repo", str(repo), "--content"],
                        outside)
        check("technique body is not addressable (exit 6)", technique.returncode == 6,
              f"exit {technique.returncode}")
    if "tombstone" in refs:
        tomb_meta = run(pae, ["get", refs["tombstone"], "--repo", str(repo)], outside)
        tomb_body = run(pae, ["get", refs["tombstone"], "--repo", str(repo), "--content"],
                        outside)
        check("tombstone metadata resolves (exit 0)", tomb_meta.returncode == 0)
        check("tombstone body is gone (exit 6)", tomb_body.returncode == 6,
              f"exit {tomb_body.returncode}")

    print("\nerror discipline")
    malformed = run(pae, ["get", "not a reference", "--repo", str(repo), "--json"], outside)
    missing = run(pae, ["get", "prompt:definitely/absent", "--repo", str(repo), "--json"],
                  outside)
    check("malformed reference exits 2", malformed.returncode == 2)
    check("unknown reference exits 4", missing.returncode == 4)
    check("failures leave stdout empty",
          malformed.stdout == "" and missing.stdout == "")
    check("failures emit one JSON object on stderr",
          json.loads(malformed.stderr)["error"] == "malformed_reference")
    check("no checksum bypass flag exists",
          run(pae, ["get", refs["servable"], "--repo", str(repo), "--content",
                    "--no-verify"], outside).returncode == 2)

    print("\nsearch")
    searched = run(pae, ["search", "android security audit", "--repo", str(repo)], outside)
    check("pae search", searched.returncode == 0, searched.stderr)
    search_json = run(
        pae, ["--json", "search", "android security audit", "--repo", str(repo)], outside
    )
    check("pae search --json", search_json.returncode == 0, search_json.stderr)
    if search_json.returncode == 0:
        payload = json.loads(search_json.stdout)
        check("search returns ranked hits", len(payload["hits"]) > 0)
        check("hits carry durable UIDs", payload["hits"][0]["uid"].startswith("pae_"))
        check("hits explain themselves", bool(payload["hits"][0]["matched_fields"]))
        check("no source path leaks into a hit", "source_path" not in search_json.stdout)
        check("no confidence value is emitted", "confidence" not in search_json.stdout.lower())
    empty = run(pae, ["search", "zzzzqqq wobblegonk", "--repo", str(repo)], outside)
    check("a query matching nothing still exits 0", empty.returncode == 0, empty.stderr)
    check("an empty query is a usage error",
          run(pae, ["search", "   ", "--repo", str(repo)], outside).returncode == 2)
    check("an unknown kind is a usage error",
          run(pae, ["search", "widget", "--kind", "nonsense", "--repo", str(repo)],
              outside).returncode == 2)
    exact = run(pae, ["--json", "search", "technique:ST-01", "--repo", str(repo)], outside)
    if exact.returncode == 0:
        check("an exact reference resolves at rank 1",
              json.loads(exact.stdout)["hits"][0]["id"] == "technique:ST-01")

    print("\nrouting")
    routed = run(pae, ["route", "my model drifted in production", "--repo", str(repo)], outside)
    check("pae route", routed.returncode == 0, routed.stderr)
    route_json = run(
        pae, ["--json", "route", "my model drifted in production", "--repo", str(repo)], outside
    )
    check("pae route --json", route_json.returncode == 0, route_json.stderr)
    if route_json.returncode == 0:
        decision = json.loads(route_json.stdout)
        check("route reports a declared status",
              decision["status"] in ("matched", "ambiguous", "weak", "no_route"))
        check("route explains itself", bool(decision["reasons"]))
        check("no confidence value in a route",
              "confidence" not in route_json.stdout.lower())
    unroutable = run(pae, ["route", "zzzzqqq wobblegonk", "--repo", str(repo)], outside)
    check("an unroutable task still exits 0", unroutable.returncode == 0, unroutable.stderr)

    print("\nvalidation")
    validated = run(pae, ["validate-registry", "--repo", str(repo)], outside)
    check("pae validate-registry", validated.returncode == 0, validated.stderr)
    deep = run(pae, ["validate-registry", "--repo", str(repo), "--verify-checksums",
                     "--json"], outside)
    check("pae validate-registry --verify-checksums", deep.returncode == 0, deep.stderr)
    if deep.returncode == 0:
        check("every live source hashed clean",
              json.loads(deep.stdout)["checksums_verified"] is True)

    shutil.rmtree(outside, ignore_errors=True)

    print(f"\n{CHECKS - len(FAILURES)}/{CHECKS} checks passed")
    if FAILURES:
        print("failed: " + ", ".join(FAILURES))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
