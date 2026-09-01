"""Synthetic PAE checkouts for tests.

Production data is never mutated to create a negative case, and production has
no aliases and no excluded records at all, so every interesting path — alias
resolution, exclusion, traversal, symlink escape, checksum mismatch, summary
drift — exists only here. These builders make one throwaway checkout per test
in a temporary directory.
"""

from __future__ import annotations

import hashlib
import json
import os
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Mapping, Optional, Sequence

RECORD_SCHEMA = "pae-registry-record/1"
SUMMARY_SCHEMA = "pae-registry-summary/1"

REGISTRY_RELPATH = "meta/registry/registry.jsonl"
SUMMARY_RELPATH = "meta/registry/registry-summary.json"


def sha256_of(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def record(
    uid: str,
    id: str,
    *,
    kind: str = "prompt",
    lifecycle: str = "live",
    policy: Optional[str] = "standard",
    title: str = "Fixture Resource",
    description: Optional[str] = None,
    aliases: Sequence[str] = (),
    path: Optional[str] = None,
    content_sha256: Optional[str] = None,
    checksum_payload: Optional[str] = "raw_source_bytes",
    defined_in: Optional[str] = None,
    guard_preservation: Optional[Mapping[str, Any]] = None,
    relationships: Optional[Mapping[str, Any]] = None,
    schema_version: str = RECORD_SCHEMA,
    maturity: str = "experimental",
    drop: Sequence[str] = (),
    **overrides: Any,
) -> dict[str, Any]:
    """One registry record shaped like the real thing."""
    serving: dict[str, Any] = {"basis": ["fixture"]}
    if policy is not None:
        serving["value"] = policy
    if guard_preservation is not None:
        serving["guard_preservation"] = dict(guard_preservation)

    obj: dict[str, Any] = {
        "schema_version": schema_version,
        "uid": uid,
        "kind": kind,
        "id": id,
        "aliases": list(aliases),
        "lifecycle": lifecycle,
        "title": title,
        "derived_fields": [],
        "metadata_completeness": "full",
        "native": {},
        "governance": {
            "maturity": maturity,
            "review_status": "unknown",
            "eval_status": "unknown",
            "eval_artifacts": [],
        },
        "quality": [],
        "provenance": {"origin": "project_native"},
        "license": {"status": "resolved", "spdx": "MIT", "basis": "fixture"},
        "serving_policy": serving,
        "relationships": {
            "copy_of": None,
            "copies": [],
            "superseded_by": None,
            "supersedes": [],
            "merged_into": None,
            "merges": [],
            "split_into": [],
            "attachments": [],
            **(dict(relationships) if relationships else {}),
        },
        "diagnostics": [],
    }
    if description is not None:
        obj["description"] = description
    if path is not None or lifecycle == "tombstone":
        source: dict[str, Any] = {
            "birth_path": path or f"fixtures/{uid}.md",
            "previous_paths": [],
        }
        if path is not None:
            source["path"] = path
        if content_sha256 is not None:
            source["content_sha256"] = content_sha256
        if checksum_payload is not None:
            source["checksum_payload"] = checksum_payload
        obj["source"] = source
    if defined_in is not None:
        obj["defined_in"] = defined_in
    obj.update(overrides)
    for key in drop:
        obj.pop(key, None)
    return obj


def summary_for(records: Iterable[Mapping[str, Any]], **overrides: Any) -> dict[str, Any]:
    """A summary that agrees with the records, unless a test overrides it."""
    records = list(records)
    lifecycle: Counter[str] = Counter()
    kinds: Counter[str] = Counter()
    live: Counter[str] = Counter()
    tomb: Counter[str] = Counter()
    policies: Counter[str] = Counter()
    maturity: Counter[str] = Counter()
    completeness: Counter[str] = Counter()
    for rec in records:
        lifecycle[rec["lifecycle"]] += 1
        kinds[rec["kind"]] += 1
        (live if rec["lifecycle"] == "live" else tomb)[rec["kind"]] += 1
        policies[str((rec.get("serving_policy") or {}).get("value"))] += 1
        maturity[(rec.get("governance") or {}).get("maturity", "experimental")] += 1
        completeness[rec.get("metadata_completeness", "full")] += 1
    obj = {
        "schema": SUMMARY_SCHEMA,
        "total_records": len(records),
        "by_lifecycle": dict(lifecycle),
        "by_kind": dict(kinds),
        "by_kind_live": dict(live),
        "by_kind_tombstone": dict(tomb),
        "by_serving_policy": dict(policies),
        "by_maturity": dict(maturity),
        "by_metadata_completeness": dict(completeness),
    }
    obj.update(overrides)
    return obj


def build_repo(
    root: os.PathLike[str] | str,
    records: Sequence[Mapping[str, Any]] = (),
    *,
    sources: Optional[Mapping[str, bytes]] = None,
    summary: Optional[Mapping[str, Any]] = None,
    extra_lines: Sequence[str] = (),
) -> Path:
    """Write a synthetic checkout and return its root."""
    root = Path(root)
    (root / "meta" / "registry").mkdir(parents=True, exist_ok=True)

    for rel, data in (sources or {}).items():
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)

    lines = [json.dumps(rec, sort_keys=True) for rec in records]
    lines.extend(extra_lines)
    (root / REGISTRY_RELPATH).write_text("\n".join(lines) + "\n", encoding="utf-8")

    resolved_summary = summary_for(records) if summary is None else summary
    (root / SUMMARY_RELPATH).write_text(
        json.dumps(resolved_summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return root


def with_source(
    root: os.PathLike[str] | str, rel: str, body: bytes
) -> tuple[str, str]:
    """Write a source file and return ``(relative path, checksum)``."""
    target = Path(root) / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(body)
    return rel, sha256_of(body)


# -- ready-made resources --------------------------------------------------

STANDARD_UID = "pae_0000000000st"
STANDARD_ID = "prompt:fixtures/standard-resource"
SAFETY_UID = "pae_0000000000sg"
SAFETY_ID = "prompt:fixtures/safety-gated-resource"
METADATA_ONLY_UID = "pae_0000000000md"
METADATA_ONLY_ID = "prompt:fixtures/metadata-only-resource"
EXCLUDED_UID = "pae_0000000000ex"
EXCLUDED_ID = "prompt:fixtures/excluded-resource"
TOMBSTONE_UID = "pae_0000000000tb"
TOMBSTONE_ID = "prompt:fixtures/retired-resource"
TECHNIQUE_UID = "pae_0000000000tq"
TECHNIQUE_ID = "technique:XX-01"
RENAMED_UID = "pae_0000000000rn"
RENAMED_ID = "prompt:fixtures/renamed-resource"
RETIRED_ALIAS = "prompt:fixtures/old-name-of-renamed-resource"

STANDARD_BODY = b"# Standard fixture\n\nA body the engine may serve whole.\n"
SAFETY_BODY = b"# Safety-gated fixture\n\nGuards are load-bearing; serve whole or not at all.\n"
RENAMED_BODY = b"# Renamed fixture\n\nReachable by its current id and by its retired alias.\n"
METADATA_ONLY_BODY = b"# Withheld fixture\n\nThis body must never be served.\n"


def standard_repo(root: os.PathLike[str] | str) -> Path:
    """A checkout exercising every serving policy and lifecycle at once."""
    root = Path(root)
    (root / "meta" / "registry").mkdir(parents=True, exist_ok=True)

    std_path, std_sha = with_source(root, "fixtures/standard.md", STANDARD_BODY)
    sg_path, sg_sha = with_source(root, "fixtures/safety_gated.md", SAFETY_BODY)
    mo_path, mo_sha = with_source(root, "fixtures/metadata_only.md", METADATA_ONLY_BODY)
    ex_path, ex_sha = with_source(root, "fixtures/excluded.md", b"# Excluded fixture\n")
    rn_path, rn_sha = with_source(root, "fixtures/renamed.md", RENAMED_BODY)

    records = [
        record(STANDARD_UID, STANDARD_ID, path=std_path, content_sha256=std_sha,
               description="A standard fixture resource."),
        record(
            SAFETY_UID,
            SAFETY_ID,
            policy="safety_gated",
            path=sg_path,
            content_sha256=sg_sha,
            guard_preservation={
                "must_not_truncate": True,
                "note": "Serve the resource whole or not at all.",
            },
        ),
        record(METADATA_ONLY_UID, METADATA_ONLY_ID, policy="metadata_only",
               path=mo_path, content_sha256=mo_sha),
        record(EXCLUDED_UID, EXCLUDED_ID, policy="excluded", path=ex_path,
               content_sha256=ex_sha, title="Excluded Fixture",
               description="Must never be returned by get()."),
        record(
            TOMBSTONE_UID,
            TOMBSTONE_ID,
            lifecycle="tombstone",
            policy="metadata_only",
            maturity="deprecated",
            relationships={
                "superseded_by": {"ref": STANDARD_UID, "object_kind": "resource"}
            },
        ),
        record(TECHNIQUE_UID, TECHNIQUE_ID, kind="technique",
               defined_in="techniques/MASTER_TECHNIQUE_INDEX.md",
               content_sha256=None, checksum_payload=None),
        record(RENAMED_UID, RENAMED_ID, aliases=[RETIRED_ALIAS], path=rn_path,
               content_sha256=rn_sha),
    ]
    return build_repo(root, records)
