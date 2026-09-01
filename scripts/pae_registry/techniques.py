"""Technique records, built from the repository's existing catalog parser.

There is deliberately no second parser. ``scripts/validate_technique_catalog.py``
already encodes the semantics a naive reader gets wrong — code-fence stripping,
``###``/``####`` heading definitions, ``**ID:**`` and ``**ID/ID:**`` bold
definitions, the tombstone test, the rule that an active heading outranks a
tombstone elsewhere because IDs get reused, and ``(also XX-NN)`` aliases — so
this module imports it and normalizes its output.
"""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path
from typing import Any

MASTER_INDEX = "techniques/MASTER_TECHNIQUE_INDEX.md"
DETAIL_DIR = "techniques/new-techniques"

MERGED_INTO_RE = re.compile(r"Merged into \*{0,2}([A-Z]{2,4}-\d+)")
NAME_RE = re.compile(r"^[:\s]*([^→*]+?)(?:\s*\*\*)?(?:\s*→.*)?$")


def load_catalog(repo_root: Path) -> dict[str, Any]:
    path = repo_root / "scripts" / "validate_technique_catalog.py"
    spec = importlib.util.spec_from_file_location("pae_validate_technique_catalog", path)
    if spec is None or spec.loader is None:  # pragma: no cover - defensive
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.parse_index()


def _canonical_name(entries: list[str]) -> str | None:
    for entry in entries:
        match = NAME_RE.match(entry.strip())
        if match:
            name = match.group(1).strip(" *:—-")
            if name:
                return name
    return None


def technique_records(repo_root: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Normalized technique inputs, plus the catalog's own summary numbers."""
    catalog = load_catalog(repo_root)
    detail_files = {
        p.stem.replace("_", "-"): p.relative_to(repo_root).as_posix()
        for p in sorted((repo_root / DETAIL_DIR).glob("*.md"))
    }

    records: list[dict[str, Any]] = []
    for technique_id in sorted(catalog["all_ids"]):
        headings = catalog["heading_ids"].get(technique_id, [])
        bolds = catalog["bold_ids"].get(technique_id, [])
        entries = headings + bolds
        deprecated = technique_id in catalog["deprecated"]

        merged_into = None
        if deprecated:
            merged_into = next(
                (m.group(1) for e in entries for m in [MERGED_INTO_RE.search(e)] if m), None
            )

        records.append(
            {
                "technique_id": technique_id,
                "title": _canonical_name(entries) or technique_id,
                "category": technique_id.split("-")[0],
                "state": "deprecated" if deprecated else "active",
                "merged_into_technique": merged_into,
                "attachments": [detail_files[technique_id]] if technique_id in detail_files else [],
                "aliases": sorted(
                    alias for alias in catalog["aliases"] if alias == technique_id
                ),
            }
        )

    summary = {
        "total": catalog["total"],
        "active": catalog["active"],
        "deprecated": len(catalog["deprecated"]),
        "categories": catalog["categories"],
        "unresolved_aliases": sorted(catalog["aliases"]),
    }
    return records, summary
