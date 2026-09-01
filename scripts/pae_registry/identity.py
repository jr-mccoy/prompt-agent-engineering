"""Stable identity: immutable UIDs, human-readable public IDs, and the ledger.

Identity is public API. A UID never changes and is never recycled; a public ID
may change when a resource moves to a new semantic home, and the retired value
becomes a permanent alias. See ADR-0010.
"""

from __future__ import annotations

import csv
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable, Optional

from .membership import STRUCTURAL_SEGMENTS, scope_of

#: Crockford base32 — no I, L, O or U, so a UID cannot be misread or mistyped
#: into a different UID. Emitted lowercase to match the repository's ID style.
CROCKFORD = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"

UID_BITS = 60
UID_CHARS = UID_BITS // 5  # 12
UID_RE = re.compile(r"^pae_[0-9abcdefghjkmnpqrstvwxyz]{12}$")
PUBLIC_ID_RE = re.compile(r"^[a-z]+:[a-z0-9]+(?:[.-][a-z0-9]+)*(?:/[a-z0-9]+(?:[.-][a-z0-9]+)*)*$")

IDENTITY_HEADER = ("uid", "kind", "public_id", "birth_path")
ALIAS_HEADER = ("retired_public_id", "uid", "reason")


class IdentityError(RuntimeError):
    """Identity cannot be established or would be ambiguous."""


def crockford_encode(value: int, chars: int = UID_CHARS) -> str:
    out = []
    for _ in range(chars):
        out.append(CROCKFORD[value & 0x1F])
        value >>= 5
    return "".join(reversed(out))


def uid_for(kind: str, birth_path: str) -> str:
    """Deterministic UID proposal.

    ``sha256(kind + "\\0" + birth_path)``, first 60 bits, Crockford base32.
    Depends only on kind and birth path — never on title, frontmatter or
    content — so a content edit can never move a resource's identity.
    """
    digest = hashlib.sha256(f"{kind}\0{birth_path}".encode("utf-8")).digest()
    token = int.from_bytes(digest[:8], "big") >> (64 - UID_BITS)
    return "pae_" + crockford_encode(token).lower()


def normalize_component(token: str) -> str:
    """Lowercase, separator-fold, collapse and trim a single ID component."""
    token = token.lower()
    token = re.sub(r"[_\s]+", "-", token)
    token = re.sub(r"[^a-z0-9.-]", "-", token)
    token = re.sub(r"-{2,}", "-", token)
    return token.strip("-.")


def _reject_bad_components(kind: str, components: list[str], source: str) -> None:
    for comp in components:
        if not comp or comp in {".", ".."}:
            raise IdentityError(f"invalid public-ID component {comp!r} derived from {source}")


def public_id_for(kind: str, path: str) -> str:
    """``<kind>:<scope>/<mid-path...>/<slug>`` with structural segments removed."""
    rel = PurePosixPath(path)
    parts = list(rel.parts)
    if kind == "skill":
        middle, slug_source = parts[1:-2], parts[-2]
    else:
        middle, slug_source = parts[1:-1], rel.stem

    structural = STRUCTURAL_SEGMENTS.get(kind)
    if structural:
        middle = [seg for seg in middle if seg != structural]

    components = [normalize_component(scope_of(rel))]
    components += [normalize_component(seg) for seg in middle]
    components.append(normalize_component(slug_source))
    _reject_bad_components(kind, components, path)

    public_id = f"{kind}:" + "/".join(components)
    if "//" in public_id or not PUBLIC_ID_RE.match(public_id):
        raise IdentityError(f"malformed public ID {public_id!r} derived from {path}")
    return public_id


def technique_public_id(technique_id: str) -> str:
    """Techniques namespace their existing catalog identifier directly."""
    if not re.match(r"^[A-Z]{2,4}-\d+$", technique_id):
        raise IdentityError(f"unexpected technique identifier {technique_id!r}")
    return f"technique:{technique_id}"


def technique_uid(technique_id: str) -> str:
    return uid_for("technique", f"technique:{technique_id}")


@dataclass(frozen=True)
class IdentityRow:
    uid: str
    kind: str
    public_id: str
    birth_path: str


def read_identity(path: Path) -> list[IdentityRow]:
    if not path.exists():
        return []
    rows: list[IdentityRow] = []
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.reader(fh, delimiter="\t")
        header = next(reader, None)
        if header is None:
            return []
        if tuple(header) != IDENTITY_HEADER:
            raise IdentityError(f"{path}: unexpected header {header!r}")
        for line in reader:
            if not line or line[0].startswith("#"):
                continue
            if len(line) != len(IDENTITY_HEADER):
                raise IdentityError(f"{path}: malformed row {line!r}")
            rows.append(IdentityRow(*line))
    return rows


def write_identity(path: Path, rows: Iterable[IdentityRow]) -> None:
    ordered = sorted(rows, key=lambda r: r.uid)
    lines = ["\t".join(IDENTITY_HEADER)]
    lines += ["\t".join((r.uid, r.kind, r.public_id, r.birth_path)) for r in ordered]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


@dataclass(frozen=True)
class AliasRow:
    retired_public_id: str
    uid: str
    reason: str


def read_aliases(path: Path) -> list[AliasRow]:
    if not path.exists():
        return []
    rows: list[AliasRow] = []
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.reader(fh, delimiter="\t")
        header = next(reader, None)
        if header is None:
            return []
        if tuple(header) != ALIAS_HEADER:
            raise IdentityError(f"{path}: unexpected header {header!r}")
        for line in reader:
            if not line or line[0].startswith("#"):
                continue
            if len(line) != len(ALIAS_HEADER):
                raise IdentityError(f"{path}: malformed row {line!r}")
            rows.append(AliasRow(*line))
    return rows


def write_aliases(path: Path, rows: Iterable[AliasRow]) -> None:
    ordered = sorted(rows, key=lambda r: (r.retired_public_id, r.uid))
    lines = ["\t".join(ALIAS_HEADER)]
    lines += ["\t".join((r.retired_public_id, r.uid, r.reason)) for r in ordered]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def check_uniqueness(rows: list[IdentityRow], aliases: list[AliasRow]) -> list[str]:
    """Every identity invariant that can be checked from the ledgers alone."""
    errors: list[str] = []

    def duplicates(values: Iterable[str]) -> list[str]:
        seen, dupes = set(), set()
        for value in values:
            if value in seen:
                dupes.add(value)
            seen.add(value)
        return sorted(dupes)

    for uid in duplicates(r.uid for r in rows):
        errors.append(f"duplicate uid: {uid}")
    for public_id in duplicates(r.public_id for r in rows):
        errors.append(f"duplicate public id: {public_id}")
    for retired in duplicates(a.retired_public_id for a in aliases):
        errors.append(f"duplicate alias: {retired}")

    current = {r.public_id for r in rows}
    known_uids = {r.uid for r in rows}
    for alias in aliases:
        if alias.retired_public_id in current:
            errors.append(f"alias collides with a current public id: {alias.retired_public_id}")
        if alias.uid not in known_uids:
            errors.append(f"alias points at unknown uid: {alias.retired_public_id} -> {alias.uid}")

    for row in rows:
        if not UID_RE.match(row.uid):
            errors.append(f"malformed uid: {row.uid}")
        if not row.public_id.startswith(f"{row.kind}:"):
            errors.append(f"public id does not match kind: {row.public_id} (kind={row.kind})")
    return errors


def ledger_stability_errors(
    frozen: list[IdentityRow], proposed: list[IdentityRow], aliases: list[AliasRow]
) -> list[str]:
    """Post-freeze invariants: UIDs and birth paths are permanent.

    A public-ID change is allowed only when the retired value is registered as
    an alias for the same UID.
    """
    errors: list[str] = []
    by_uid = {row.uid: row for row in frozen}
    proposed_by_uid = {row.uid: row for row in proposed}
    retired = {a.retired_public_id: a.uid for a in aliases}

    for uid, old in by_uid.items():
        new = proposed_by_uid.get(uid)
        if new is None:
            errors.append(f"identity row disappeared: {uid} ({old.public_id})")
            continue
        if new.birth_path != old.birth_path:
            errors.append(f"birth path changed for {uid}: {old.birth_path} -> {new.birth_path}")
        if new.kind != old.kind:
            errors.append(f"kind changed for {uid}: {old.kind} -> {new.kind}")
        if new.public_id != old.public_id and retired.get(old.public_id) != uid:
            errors.append(
                f"public id changed for {uid} without an alias row: "
                f"{old.public_id} -> {new.public_id}"
            )
    return errors


def resolve_or_propose(
    frozen: dict[str, IdentityRow], kind: str, birth_path: str, current_public_id: str
) -> IdentityRow:
    """Ledger wins after freeze; otherwise propose deterministically."""
    proposed_uid = uid_for(kind, birth_path)
    existing = frozen.get(proposed_uid)
    if existing is not None:
        return existing
    return IdentityRow(uid=proposed_uid, kind=kind, public_id=current_public_id, birth_path=birth_path)
