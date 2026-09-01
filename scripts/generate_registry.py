#!/usr/bin/env python3
"""Generate and validate the PAE Registry.

The registry is the durable, normalized catalog of this repository's first-class
AI resources: prompts, techniques, skills, agents, commands and personas. It is
**not** ``PROMPT_INDEX.json`` (see ADR-0007) — the index is a mixed artifact
population that both includes non-resources and omits resources.

Files under ``meta/registry/``:

  hand-maintained   identity.tsv, aliases.tsv, relationships.tsv, overrides/
  generated         registry.jsonl, registry-summary.json, diagnostics.jsonl

Usage::

    python3 scripts/generate_registry.py --dry-run   # propose, validate, report
    python3 scripts/generate_registry.py --write     # regenerate artifacts
    python3 scripts/generate_registry.py --check     # CI: everything current + valid
    python3 scripts/generate_registry.py --summary   # print the summary

Exit code 0 on success, 1 on any failure.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pae_registry import build as build_mod  # noqa: E402
from pae_registry import identity, membership, relationships  # noqa: E402
from pae_registry import schema as schema_mod  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_DIR = REPO_ROOT / "meta" / "registry"
SCHEMA_DIR = REGISTRY_DIR / "schemas"

GENERATED = ("registry.jsonl", "registry-summary.json", "diagnostics.jsonl")


def _fail(errors: list[str], limit: int = 25) -> int:
    for error in errors[:limit]:
        print(f"  ✗ {error}")
    if len(errors) > limit:
        print(f"  … and {len(errors) - limit} more")
    return 1


def validate_schemas(result: build_mod.BuildResult, outputs: dict[str, str]) -> list[str]:
    errors: list[str] = []
    record_schema = schema_mod.load(SCHEMA_DIR / "registry-record.v1.schema.json")
    ledger_schema = schema_mod.load(SCHEMA_DIR / "identity-ledger.v1.schema.json")
    rel_schema = schema_mod.load(SCHEMA_DIR / "relationships.v1.schema.json")
    schema_mod.load(SCHEMA_DIR / "overrides.v1.schema.json")

    for record in result.records:
        for error in schema_mod.validate(record, record_schema):
            errors.append(f"{record['id']}: {error}")

    for row in result.identity_rows:
        instance = {
            "uid": row.uid,
            "kind": row.kind,
            "public_id": row.public_id,
            "birth_path": row.birth_path,
        }
        for error in schema_mod.validate(instance, ledger_schema):
            errors.append(f"identity.tsv {row.uid}: {error}")

    for row in result.relationship_rows:
        instance = dict(zip(build_mod.RELATIONSHIP_HEADER, row))
        for error in schema_mod.validate(instance, rel_schema):
            errors.append(f"relationships.tsv {row[0]}: {error}")
    return errors


def integrity_checks(result: build_mod.BuildResult) -> list[str]:
    """Invariants that must hold regardless of freeze state."""
    errors: list[str] = []
    aliases = identity.read_aliases(REGISTRY_DIR / "aliases.tsv")
    errors.extend(identity.check_uniqueness(result.identity_rows, aliases))

    ledger_uids = {row.uid for row in result.identity_rows}
    record_uids = {record["uid"] for record in result.records}
    for uid in sorted(ledger_uids - record_uids):
        errors.append(f"identity row without a registry record: {uid}")
    for uid in sorted(record_uids - ledger_uids):
        errors.append(f"registry record without an identity row: {uid}")

    # Every resource-typed relationship reference must resolve.
    for record in result.records:
        rels = record["relationships"]
        refs: list[str] = []
        if rels["copy_of"]:
            refs.append(rels["copy_of"])
        refs.extend(rels["copies"])
        refs.extend(rels["supersedes"])
        refs.extend(rels["merges"])
        for edge in [rels["superseded_by"], rels["merged_into"], *rels["split_into"]]:
            if isinstance(edge, dict) and edge.get("object_kind") == "resource":
                refs.append(edge["ref"])
        for ref in refs:
            if ref not in record_uids:
                errors.append(f"{record['id']}: relationship points at unknown uid {ref}")

    for record in result.records:
        if record["serving_policy"]["value"] not in {
            "standard",
            "safety_gated",
            "metadata_only",
            "excluded",
        }:
            errors.append(f"{record['id']}: invalid serving policy")
    return errors


def freeze_checks(result: build_mod.BuildResult) -> list[str]:
    """Post-freeze ledger stability. A no-op before the ledger exists."""
    frozen = identity.read_identity(REGISTRY_DIR / "identity.tsv")
    if not frozen:
        return []
    aliases = identity.read_aliases(REGISTRY_DIR / "aliases.tsv")
    return identity.ledger_stability_errors(frozen, result.identity_rows, aliases)


def dry_run_report(result: build_mod.BuildResult) -> None:
    summary = result.summary
    stats = result.stats
    print("=" * 68)
    print("PAE REGISTRY — DRY RUN")
    print("=" * 68)
    print(f"\nIdentity ledger present: {'yes' if stats['frozen_ledger_present'] else 'no (pre-freeze)'}")
    print(f"\nTotal records: {summary['total_records']}")
    print("  live:      ", dict(summary["by_kind_live"]))
    print("  tombstones:", dict(summary["by_kind_tombstone"]))
    print(f"\nFile-backed candidates: {stats['candidates']}")
    print(f"Excluded Markdown files: {stats['exclusions']}")
    for reason, count in summary["membership"]["exclusion_reasons"].items():
        print(f"    {reason:34} {count}")
    print("\nUID / public-ID collisions: 0 (generation aborts on any collision)")
    print(f"\nMetadata completeness: {dict(summary['by_metadata_completeness'])}")
    print(f"Serving policy:        {dict(summary['by_serving_policy'])}")
    print(f"Provenance origin:     {dict(summary['by_provenance_origin'])}")
    print(f"License status:        {dict(summary['by_license_status'])}")
    print(f"Quality assertions:    {dict(summary['quality_assertions_by_scheme'])}")
    print(f"\nRelationships: {dict(summary['relationships'])}")
    print(f"  reorg moves parsed:     {stats['reorg_moves']}")
    print(f"  reorg relations parsed: {stats['reorg_relations']}")
    print(f"  copy edges:             {stats['copy_edges']}")
    print(f"\nTechnique catalog: {summary['technique_catalog']}")
    print(f"\nDiagnostics: {dict(summary['diagnostics_by_code'])}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true", help="propose and report; write nothing")
    group.add_argument("--write", action="store_true", help="regenerate committed artifacts")
    group.add_argument("--check", action="store_true", help="verify artifacts are current and valid")
    group.add_argument("--summary", action="store_true", help="print the generated summary")
    group.add_argument("--freeze", action="store_true", help="write the identity ledger (one time)")
    args = parser.parse_args()

    try:
        result = build_mod.build(REPO_ROOT, REGISTRY_DIR)
    except (
        membership.MembershipError,
        identity.IdentityError,
        relationships.RelationshipError,
        build_mod.BuildError,
    ) as exc:
        print(f"registry generation failed: {exc}")
        return 1

    errors = integrity_checks(result) + freeze_checks(result)
    if SCHEMA_DIR.is_dir():
        errors += validate_schemas(result, {})
    if errors:
        print("registry invariants violated:")
        return _fail(errors)

    outputs = build_mod.write_artifacts(REGISTRY_DIR, result)

    if args.dry_run:
        dry_run_report(result)
        print("\nNo files written (--dry-run).")
        return 0

    if args.summary:
        print(json.dumps(result.summary, indent=2, sort_keys=True))
        return 0

    if args.freeze:
        identity.write_identity(REGISTRY_DIR / "identity.tsv", result.identity_rows)
        (REGISTRY_DIR / "relationships.tsv").write_text(
            build_mod.relationships_tsv(result), encoding="utf-8"
        )
        for name, content in outputs.items():
            (REGISTRY_DIR / name).write_text(content, encoding="utf-8")
        print(f"✓ froze {len(result.identity_rows)} identity rows and wrote all artifacts")
        return 0

    if args.write:
        identity.write_identity(REGISTRY_DIR / "identity.tsv", result.identity_rows)
        (REGISTRY_DIR / "relationships.tsv").write_text(
            build_mod.relationships_tsv(result), encoding="utf-8"
        )
        for name, content in outputs.items():
            (REGISTRY_DIR / name).write_text(content, encoding="utf-8")
        print(f"✓ wrote {len(result.records)} records to {REGISTRY_DIR.relative_to(REPO_ROOT)}")
        return 0

    # --check
    stale: list[str] = []
    for name, content in outputs.items():
        path = REGISTRY_DIR / name
        if not path.exists():
            stale.append(f"{name}: missing")
        elif path.read_text(encoding="utf-8") != content:
            stale.append(f"{name}: stale — regenerate with --write")
    rel_path = REGISTRY_DIR / "relationships.tsv"
    expected_rels = build_mod.relationships_tsv(result)
    if not rel_path.exists():
        stale.append("relationships.tsv: missing")
    elif rel_path.read_text(encoding="utf-8") != expected_rels:
        stale.append("relationships.tsv: stale — regenerate with --write")
    if not (REGISTRY_DIR / "identity.tsv").exists():
        stale.append("identity.tsv: missing — identity has not been frozen")
    if stale:
        print("registry artifacts are not current:")
        return _fail(stale)

    print(
        f"OK — {result.summary['total_records']} registry records "
        f"({sum(result.summary['by_kind_live'].values())} live, "
        f"{sum(result.summary['by_kind_tombstone'].values())} tombstones); "
        "identity stable, schemas valid, artifacts current."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
