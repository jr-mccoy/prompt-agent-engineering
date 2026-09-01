"""Relationship migration from the repository's two existing evidence files.

``meta/REORG_MAP.tsv`` records four *different* semantics that must not collapse
into one alias relation:

    move            identity preserved, the resource lives somewhere else
    superseded-by   a DIFFERENT resource replaced this one
    merged-into     this content was folded into another identity
    split-into      this identity dispersed across a collection

``meta/VENDORED.tsv`` records explicit canonical/copy pairs. Copy relations come
from that file and from nowhere else — never from content similarity, because
the repository deliberately contains adapted near-duplicates that are genuinely
different resources.

Neither file is modified.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

DELETED_PREFIX = "DELETED "
REORG_PREDICATES = ("superseded-by", "merged-into", "split-into")

#: Predicate names as they appear on a registry record.
PREDICATE_FIELD = {
    "superseded-by": "superseded_by",
    "merged-into": "merged_into",
    "split-into": "split_into",
}


class RelationshipError(RuntimeError):
    """A relationship cannot be resolved and identity would be misrepresented."""


@dataclass(frozen=True)
class ReorgMove:
    old_path: str
    new_path: str


@dataclass(frozen=True)
class ReorgRelation:
    old_path: str
    predicate: str  # superseded-by | merged-into | split-into
    raw_target: str


@dataclass(frozen=True)
class CopyPair:
    canonical: str
    copy: str


@dataclass
class ReorgModel:
    moves: dict[str, str] = field(default_factory=dict)
    relations: list[ReorgRelation] = field(default_factory=list)

    def resolve(self, path: str) -> str:
        """Follow the move chain transitively. A cycle is a hard error."""
        seen = [path]
        current = path
        while current in self.moves:
            current = self.moves[current]
            if current in seen:
                raise RelationshipError(
                    "cycle in REORG_MAP move chain: " + " -> ".join(seen + [current])
                )
            seen.append(current)
        return current


def _read_rows(path: Path) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) != 2:
            continue
        rows.append((parts[0].strip(), parts[1].strip()))
    return rows


def load_reorg(path: Path) -> ReorgModel:
    model = ReorgModel()
    for old, dest in _read_rows(path):
        if dest.startswith(DELETED_PREFIX):
            predicate, _, target = dest[len(DELETED_PREFIX):].partition(":")
            predicate = predicate.strip()
            if predicate not in REORG_PREDICATES:
                raise RelationshipError(f"unknown deletion predicate {predicate!r} for {old}")
            if not target.strip():
                raise RelationshipError(f"deletion row without a target: {old}")
            model.relations.append(ReorgRelation(old, predicate, target.strip()))
        else:
            if old in model.moves:
                raise RelationshipError(f"duplicate move source: {old}")
            model.moves[old] = dest
    return model


def load_vendored(path: Path) -> list[CopyPair]:
    return [CopyPair(canonical=c, copy=p) for c, p in _read_rows(path)]


def classify_target(repo_root: Path, target: str, is_resource) -> tuple[str, str]:
    """Return ``(object_kind, resolved_path)`` for a relationship target.

    ``resource``   a live first-class registry resource
    ``collection`` a directory absorbing the old identity (``split-into``)
    ``document``   a file that exists but is not a registry resource

    An unresolvable target is a hard error: a dangling edge would let a
    tombstone point at nothing while claiming a replacement exists.
    """
    normalized = target.rstrip("/")
    on_disk = repo_root / normalized
    if target.endswith("/") or on_disk.is_dir():
        if not on_disk.is_dir():
            raise RelationshipError(f"relationship target directory does not exist: {target}")
        return "collection", normalized + "/"
    if is_resource(normalized):
        return "resource", normalized
    if on_disk.exists():
        return "document", normalized
    raise RelationshipError(f"relationship target does not exist: {target}")
