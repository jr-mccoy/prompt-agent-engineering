"""Assemble registry records and emit the generated artifacts.

Determinism is a contract: every artifact is sorted by a stable key, carries no
timestamp, and is byte-identical on repeat generation from the same tree.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any, Optional

import yaml

from . import REGISTRY_RECORD_SCHEMA_VERSION
from . import adapters, governance, identity, membership, relationships, techniques

REGISTRY_DIR = Path("meta/registry")
OVERRIDE_KINDS = ("prompt", "skill", "agent", "command", "persona", "technique")

RELATIONSHIP_HEADER = ("subject_uid", "predicate", "object_ref", "object_kind", "evidence")


class BuildError(RuntimeError):
    """Generation cannot produce a trustworthy registry."""


@dataclass
class BuildResult:
    records: list[dict[str, Any]] = field(default_factory=list)
    identity_rows: list[identity.IdentityRow] = field(default_factory=list)
    relationship_rows: list[tuple[str, str, str, str, str]] = field(default_factory=list)
    diagnostics: list[dict[str, Any]] = field(default_factory=list)
    summary: dict[str, Any] = field(default_factory=dict)
    stats: dict[str, Any] = field(default_factory=dict)


def load_overrides(registry_dir: Path) -> dict[str, dict[str, Any]]:
    """Hand-maintained governance overrides, keyed by public ID."""
    overrides: dict[str, dict[str, Any]] = {}
    directory = registry_dir / "overrides"
    if not directory.is_dir():
        return overrides
    for kind in OVERRIDE_KINDS:
        path = directory / f"{kind}.yaml"
        if not path.exists():
            continue
        loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
        if loaded is None:
            continue
        if not isinstance(loaded, dict) or not isinstance(loaded.get("overrides"), dict):
            raise BuildError(f"{path}: expected a mapping with an 'overrides' key")
        for public_id, payload in loaded["overrides"].items():
            if not public_id.startswith(f"{kind}:"):
                raise BuildError(f"{path}: override {public_id!r} is not of kind {kind!r}")
            if not isinstance(payload, dict):
                raise BuildError(f"{path}: override {public_id!r} must be a mapping")
            overrides[public_id] = payload
    return overrides


def _apply_override(record: dict[str, Any], override: dict[str, Any]) -> None:
    """Shallow-merge reviewed overrides over generated values."""
    for key, value in override.items():
        if key in {"governance", "provenance", "license", "serving_policy"} and isinstance(value, dict):
            record.setdefault(key, {})
            record[key].update(value)
        elif key == "quality" and isinstance(value, list):
            record["quality"] = value
        else:
            record[key] = value


def _skill_bundle_files(repo_root: Path, skill_manifest: PurePosixPath) -> list[Path]:
    bundle = repo_root / skill_manifest.parent
    return sorted(p for p in bundle.rglob("*") if p.is_file())


def build(repo_root: Path, registry_dir: Optional[Path] = None) -> BuildResult:
    registry_dir = registry_dir or (repo_root / REGISTRY_DIR)
    result = BuildResult()

    candidates, exclusions = membership.discover(repo_root)
    candidate_paths = {c.path for c in candidates}
    roots = frozenset(membership.approved_roots(repo_root))

    reorg = relationships.load_reorg(repo_root / "meta" / "REORG_MAP.tsv")
    # A resource removed from a domain that has since been retired was still
    # first-class when it existed. Judging historical paths against today's
    # allowlist alone would silently drop those tombstones, so the reorg map's
    # own source roots are treated as evidence that the root once existed.
    historical_roots = roots | {
        old_path.split("/", 1)[0] for old_path in reorg.moves
    } | {relation.old_path.split("/", 1)[0] for relation in reorg.relations}
    vendored = relationships.load_vendored(repo_root / "meta" / "VENDORED.tsv")
    overrides = load_overrides(registry_dir)

    frozen_rows = identity.read_identity(registry_dir / "identity.tsv")
    frozen_by_uid = {row.uid: row for row in frozen_rows}
    frozen_is_present = bool(frozen_rows)

    # --- birth paths -------------------------------------------------------
    # A move preserves identity, so a moved resource's UID is seeded from where
    # it was first recorded, not from where it lives now.
    birth_of_current: dict[str, str] = {}
    for old, _dest in reorg.moves.items():
        final = reorg.resolve(old)
        if final in candidate_paths:
            birth_of_current.setdefault(final, old)

    previous_paths: dict[str, list[str]] = {}
    for old in reorg.moves:
        final = reorg.resolve(old)
        if final in candidate_paths:
            previous_paths.setdefault(final, []).append(old)

    # --- copy edges --------------------------------------------------------
    copy_of: dict[str, str] = {}
    copies: dict[str, list[str]] = {}
    for pair in vendored:
        if pair.canonical in candidate_paths and pair.copy in candidate_paths:
            if pair.copy in copy_of:
                raise BuildError(f"copy registered against two canonicals: {pair.copy}")
            copy_of[pair.copy] = pair.canonical
            copies.setdefault(pair.canonical, []).append(pair.copy)

    # --- live records ------------------------------------------------------
    by_path_uid: dict[str, str] = {}
    seen_public_ids: dict[str, str] = {}
    seen_uids: dict[str, str] = {}

    for candidate in sorted(candidates, key=lambda c: c.path):
        rel = PurePosixPath(candidate.path)
        birth_path = birth_of_current.get(candidate.path, candidate.path)
        public_id = identity.public_id_for(candidate.kind, candidate.path)
        row = identity.resolve_or_propose(frozen_by_uid, candidate.kind, birth_path, public_id)

        if row.uid in seen_uids:
            raise BuildError(
                f"UID collision: {row.uid} claimed by {seen_uids[row.uid]} and {candidate.path}"
            )
        if public_id in seen_public_ids:
            raise BuildError(
                f"public ID collision: {public_id} claimed by "
                f"{seen_public_ids[public_id]} and {candidate.path}"
            )
        seen_uids[row.uid] = candidate.path
        seen_public_ids[public_id] = candidate.path
        by_path_uid[candidate.path] = row.uid

        source_file = repo_root / candidate.path
        slug = rel.parent.name if candidate.kind == "skill" else rel.stem
        norm = adapters.adapt(candidate.kind, source_file, candidate.path, slug)
        body = source_file.read_text(encoding="utf-8", errors="replace")

        provenance, license_block = governance.provenance_and_license(
            candidate.path, norm.raw_frontmatter
        )
        gov = governance.default_governance()
        policy = governance.serving_policy(
            path=candidate.path,
            frontmatter=norm.raw_frontmatter,
            body=body,
            metadata_completeness=norm.metadata_completeness,
            maturity=gov["maturity"],
            license_status=license_block.get("status", "unresolved"),
            provenance_origin=provenance["origin"],
        )

        source: dict[str, Any] = {
            "path": candidate.path,
            "birth_path": birth_path,
            "previous_paths": sorted(previous_paths.get(candidate.path, [])),
            "content_sha256": adapters.sha256_file(source_file),
            "checksum_payload": "raw_source_bytes",
        }
        if candidate.kind == "skill":
            digest, count = adapters.bundle_digest(
                _skill_bundle_files(repo_root, rel), repo_root / rel.parent
            )
            source["bundle_sha256"] = digest
            source["bundle_file_count"] = count

        record: dict[str, Any] = {
            "schema_version": REGISTRY_RECORD_SCHEMA_VERSION,
            "uid": row.uid,
            "kind": candidate.kind,
            "id": public_id,
            "aliases": [],
            "lifecycle": "live",
            "source": source,
            "title": norm.title,
            "derived_fields": sorted(norm.derived_fields),
            "metadata_completeness": norm.metadata_completeness,
            "native": norm.native,
            "governance": gov,
            "quality": governance.quality_assertions(norm.raw_frontmatter, body),
            "provenance": provenance,
            "license": license_block,
            "serving_policy": policy,
            "relationships": {
                "copy_of": None,
                "copies": [],
                "superseded_by": None,
                "supersedes": [],
                "merged_into": None,
                "merges": [],
                "split_into": [],
                "attachments": [],
            },
            "diagnostics": list(norm.diagnostics),
        }
        if norm.description:
            record["description"] = norm.description
        result.records.append(record)
        result.identity_rows.append(
            identity.IdentityRow(row.uid, candidate.kind, public_id, birth_path)
        )

    records_by_uid = {r["uid"]: r for r in result.records}
    records_by_path = {r["source"]["path"]: r for r in result.records}

    # --- attachments -------------------------------------------------------
    # Every file in a skill bundle other than its SKILL.md manifest. Derived
    # from the same walk that produces bundle_sha256, so the attachment list and
    # the bundle digest can never describe different sets of files.
    for record in result.records:
        if record["kind"] != "skill":
            continue
        manifest = PurePosixPath(record["source"]["path"])
        bundle = repo_root / manifest.parent
        record["relationships"]["attachments"] = sorted(
            p.relative_to(repo_root).as_posix()
            for p in bundle.rglob("*")
            if p.is_file() and p.relative_to(repo_root).as_posix() != record["source"]["path"]
        )

    # --- copy edges onto records ------------------------------------------
    for copy_path, canonical_path in sorted(copy_of.items()):
        copy_record = records_by_path[copy_path]
        canonical_record = records_by_path[canonical_path]
        copy_record["relationships"]["copy_of"] = canonical_record["uid"]
        canonical_record["relationships"]["copies"].append(copy_record["uid"])
        result.relationship_rows.append(
            (copy_record["uid"], "copy_of", canonical_record["uid"], "resource", "meta/VENDORED.tsv")
        )
    for record in result.records:
        record["relationships"]["copies"].sort()

    # --- previous paths as relationship rows -------------------------------
    for path, olds in sorted(previous_paths.items()):
        uid = by_path_uid[path]
        for old in sorted(olds):
            result.relationship_rows.append(
                (uid, "previous_path", old, "path", "meta/REORG_MAP.tsv")
            )

    # --- tombstones --------------------------------------------------------
    tombstone_count = 0
    for relation in sorted(reorg.relations, key=lambda r: (r.old_path, r.predicate)):
        kind = membership.would_be_first_class(relation.old_path, historical_roots)
        if kind is None:
            result.diagnostics.append(
                {
                    "severity": "info",
                    "code": "reorg_relation_on_non_resource",
                    "path": relation.old_path,
                    "detail": (
                        f"{relation.predicate} recorded for a path that was never a "
                        "first-class resource; no tombstone created"
                    ),
                }
            )
            continue

        resolved = reorg.resolve(relation.raw_target)
        object_kind, object_path = relationships.classify_target(
            repo_root, resolved, lambda p: p in candidate_paths
        )
        public_id = identity.public_id_for(kind, relation.old_path)
        uid = identity.uid_for(kind, relation.old_path)
        if uid in seen_uids:
            raise BuildError(f"tombstone UID collides with a live resource: {uid}")
        if public_id in seen_public_ids:
            raise BuildError(f"tombstone public ID collides: {public_id}")
        seen_uids[uid] = relation.old_path
        seen_public_ids[public_id] = relation.old_path

        target_ref = records_by_path[object_path]["uid"] if object_kind == "resource" else object_path
        predicate_field = relationships.PREDICATE_FIELD[relation.predicate]

        rels: dict[str, Any] = {
            "copy_of": None,
            "copies": [],
            "superseded_by": None,
            "supersedes": [],
            "merged_into": None,
            "merges": [],
            "split_into": [],
            "attachments": [],
        }
        edge = {"ref": target_ref, "object_kind": object_kind}
        if predicate_field == "split_into":
            rels["split_into"] = [edge]
        else:
            rels[predicate_field] = edge

        record = {
            "schema_version": REGISTRY_RECORD_SCHEMA_VERSION,
            "uid": uid,
            "kind": kind,
            "id": public_id,
            "aliases": [],
            "lifecycle": "tombstone",
            "source": {
                "birth_path": relation.old_path,
                "previous_paths": [relation.old_path],
            },
            "title": adapters._title_from_slug(PurePosixPath(relation.old_path).stem),
            "derived_fields": ["title"],
            "metadata_completeness": "minimal",
            "native": {},
            "governance": {
                "maturity": "deprecated",
                "review_status": "unknown",
                "eval_status": "unknown",
                "eval_artifacts": [],
            },
            "quality": [],
            "provenance": {"origin": "unknown"},
            "license": {
                "status": "unresolved",
                "basis": "source file no longer exists; licensing not established",
            },
            "serving_policy": {"value": "metadata_only", "basis": ["maturity:deprecated"]},
            "relationships": rels,
            "diagnostics": [
                {
                    "severity": "info",
                    "code": "tombstone",
                    "detail": (
                        f"Historical resource removed by reorganization "
                        f"({relation.predicate}); the file no longer exists."
                    ),
                }
            ],
        }
        result.records.append(record)
        result.identity_rows.append(identity.IdentityRow(uid, kind, public_id, relation.old_path))
        result.relationship_rows.append(
            (uid, predicate_field, target_ref, object_kind, "meta/REORG_MAP.tsv")
        )
        tombstone_count += 1

        if object_kind == "resource":
            survivor = records_by_path[object_path]
            reverse = {"superseded_by": "supersedes", "merged_into": "merges"}.get(predicate_field)
            if reverse:
                survivor["relationships"][reverse].append(uid)

    for record in result.records:
        for key in ("supersedes", "merges"):
            record["relationships"][key].sort()

    # --- technique records --------------------------------------------------
    technique_inputs, technique_summary = techniques.technique_records(repo_root)
    master = repo_root / techniques.MASTER_INDEX
    master_digest = adapters.sha256_file(master)
    technique_uids = {t["technique_id"]: identity.technique_uid(t["technique_id"]) for t in technique_inputs}

    for item in technique_inputs:
        public_id = identity.technique_public_id(item["technique_id"])
        uid = technique_uids[item["technique_id"]]
        if uid in seen_uids:
            raise BuildError(f"technique UID collision: {uid}")
        if public_id in seen_public_ids:
            raise BuildError(f"technique public ID collision: {public_id}")
        seen_uids[uid] = public_id
        seen_public_ids[public_id] = public_id

        deprecated = item["state"] == "deprecated"
        merged_target = item["merged_into_technique"]
        rels: dict[str, Any] = {
            "copy_of": None,
            "copies": [],
            "superseded_by": None,
            "supersedes": [],
            "merged_into": None,
            "merges": [],
            "split_into": [],
            "attachments": list(item["attachments"]),
        }
        if merged_target:
            if merged_target not in technique_uids:
                raise BuildError(
                    f"technique {item['technique_id']} merges into undefined {merged_target}"
                )
            rels["merged_into"] = {"ref": technique_uids[merged_target], "object_kind": "resource"}
            result.relationship_rows.append(
                (uid, "merged_into", technique_uids[merged_target], "resource", techniques.MASTER_INDEX)
            )

        record = {
            "schema_version": REGISTRY_RECORD_SCHEMA_VERSION,
            "uid": uid,
            "kind": "technique",
            "id": public_id,
            "aliases": [],
            # A deprecated technique is still a catalogued stub with a
            # resolvable ID, so it stays "live"; its removal is expressed by
            # maturity and by native.state, not by lifecycle.
            "lifecycle": "live",
            "defined_in": techniques.MASTER_INDEX,
            "content_sha256": master_digest,
            "title": item["title"],
            "derived_fields": [],
            "metadata_completeness": "full",
            "native": {"category": item["category"], "state": item["state"]},
            "governance": {
                "maturity": "deprecated" if deprecated else "experimental",
                "review_status": "unknown",
                "eval_status": "unknown",
                "eval_artifacts": [],
            },
            "quality": [],
            "provenance": {"origin": "project_native"},
            "license": {"spdx": "MIT", "status": "resolved", "basis": "repository LICENSE"},
            "serving_policy": (
                {"value": "metadata_only", "basis": ["maturity:deprecated"]}
                if deprecated
                else {"value": "standard", "basis": ["default"]}
            ),
            "relationships": rels,
            "diagnostics": [],
        }
        result.records.append(record)
        result.identity_rows.append(
            identity.IdentityRow(uid, "technique", public_id, f"technique:{item['technique_id']}")
        )

    # reverse merge edges between techniques
    tech_by_uid = {r["uid"]: r for r in result.records if r["kind"] == "technique"}
    for record in list(tech_by_uid.values()):
        merged = record["relationships"]["merged_into"]
        if merged:
            tech_by_uid[merged["ref"]]["relationships"]["merges"].append(record["uid"])
    for record in tech_by_uid.values():
        record["relationships"]["merges"].sort()

    # --- overrides ----------------------------------------------------------
    applied = 0
    known_ids = {r["id"] for r in result.records}
    for public_id, payload in sorted(overrides.items()):
        if public_id not in known_ids:
            raise BuildError(f"override targets an unknown public ID: {public_id}")
        for record in result.records:
            if record["id"] == public_id:
                _apply_override(record, payload)
                applied += 1

    # --- aliases ------------------------------------------------------------
    alias_rows = identity.read_aliases(registry_dir / "aliases.tsv")
    aliases_by_uid: dict[str, list[str]] = {}
    for alias in alias_rows:
        aliases_by_uid.setdefault(alias.uid, []).append(alias.retired_public_id)
    for record in result.records:
        record["aliases"] = sorted(aliases_by_uid.get(record["uid"], []))

    # --- diagnostics --------------------------------------------------------
    for record in result.records:
        for diagnostic in record["diagnostics"]:
            entry = dict(diagnostic)
            entry.setdefault("path", record.get("source", {}).get("path", record["id"]))
            entry["uid"] = record["uid"]
            entry["id"] = record["id"]
            result.diagnostics.append(entry)
    for record in result.records:
        if record["metadata_completeness"] == "minimal" and record["lifecycle"] == "live":
            result.diagnostics.append(
                {
                    "severity": "warning",
                    "code": "no_frontmatter",
                    "uid": record["uid"],
                    "id": record["id"],
                    "path": record.get("source", {}).get("path", ""),
                    "detail": "first-class resource has no frontmatter; minimal record built",
                }
            )

    result.records.sort(key=lambda r: r["uid"])
    result.diagnostics.sort(key=lambda d: (d.get("code", ""), d.get("uid", "")))
    result.relationship_rows = sorted(set(result.relationship_rows))
    result.identity_rows.sort(key=lambda r: r.uid)

    result.stats = {
        "candidates": len(candidates),
        "exclusions": len(exclusions),
        "tombstones": tombstone_count,
        "overrides_applied": applied,
        "copy_edges": len(copy_of),
        "reorg_moves": len(reorg.moves),
        "reorg_relations": len(reorg.relations),
        "frozen_ledger_present": frozen_is_present,
        "exclusion_reasons": _counter(e.reason for e in exclusions),
        "technique_catalog": technique_summary,
    }
    result.summary = summarize(result)
    return result


def _counter(values) -> dict[str, int]:
    out: dict[str, int] = {}
    for value in values:
        out[value] = out.get(value, 0) + 1
    return dict(sorted(out.items()))


def summarize(result: BuildResult) -> dict[str, Any]:
    records = result.records

    def tally(fn) -> dict[str, int]:
        return _counter(fn(r) for r in records)

    return {
        "schema": "pae-registry-summary/1",
        "total_records": len(records),
        "by_kind": tally(lambda r: r["kind"]),
        "by_lifecycle": tally(lambda r: r["lifecycle"]),
        "by_kind_live": _counter(r["kind"] for r in records if r["lifecycle"] == "live"),
        "by_kind_tombstone": _counter(r["kind"] for r in records if r["lifecycle"] == "tombstone"),
        "by_metadata_completeness": tally(lambda r: r["metadata_completeness"]),
        "by_maturity": tally(lambda r: r["governance"]["maturity"]),
        "by_review_status": tally(lambda r: r["governance"]["review_status"]),
        "by_eval_status": tally(lambda r: r["governance"]["eval_status"]),
        "by_serving_policy": tally(lambda r: r["serving_policy"]["value"]),
        "by_provenance_origin": tally(lambda r: r["provenance"]["origin"]),
        "by_license_status": tally(lambda r: r["license"].get("status", "unresolved")),
        "quality_assertions_by_scheme": _counter(
            assertion["scheme"] for r in records for assertion in r["quality"]
        ),
        "relationships": {
            "copy_of": sum(1 for r in records if r["relationships"]["copy_of"]),
            "previous_paths": sum(len(r.get("source", {}).get("previous_paths", [])) for r in records),
            "superseded_by": sum(1 for r in records if r["relationships"]["superseded_by"]),
            "merged_into": sum(1 for r in records if r["relationships"]["merged_into"]),
            "split_into": sum(len(r["relationships"]["split_into"]) for r in records),
            "attachments": sum(len(r["relationships"]["attachments"]) for r in records),
        },
        "diagnostics_by_code": _counter(d["code"] for d in result.diagnostics),
        "membership": {
            "file_backed_candidates": result.stats["candidates"],
            "excluded_markdown_files": result.stats["exclusions"],
            "exclusion_reasons": result.stats["exclusion_reasons"],
        },
        "technique_catalog": result.stats["technique_catalog"],
    }


def write_artifacts(registry_dir: Path, result: BuildResult) -> dict[str, str]:
    """Serialize the three generated artifacts. Deterministic, no timestamps."""
    registry_dir.mkdir(parents=True, exist_ok=True)
    outputs: dict[str, str] = {}

    outputs["registry.jsonl"] = "".join(
        json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in result.records
    )
    outputs["registry-summary.json"] = (
        json.dumps(result.summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    )
    outputs["diagnostics.jsonl"] = "".join(
        json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n" for entry in result.diagnostics
    )
    return outputs


def relationships_tsv(result: BuildResult) -> str:
    lines = ["\t".join(RELATIONSHIP_HEADER)]
    lines += ["\t".join(row) for row in result.relationship_rows]
    return "\n".join(lines) + "\n"
