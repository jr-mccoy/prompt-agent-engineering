"""Building the two exports and their manifests (spec §5, §6, §11, §12).

One function writes the author tree, another writes the reviewer tree, and they
never write to each other's root. The mapping is assembled once, in memory, and
only the reviewer writer is given it — so "the author export contains no
mapping" is a property of the call graph rather than of a cleanup step that
could be skipped.

## Packet IDs

``PKT-0001``… ordered by ``SHA256(uid + "\\npacket-order/1")``. Two properties
matter:

* the ID contains no fragment of the target's identity, and
* the ordering is **not** the draw ordering, so packet number does not reveal
  selection rank.

## Why the author manifest carries a seed *commitment* and not the seed

Spec §12 lists the selection seed among the author manifest's fields. Writing
the raw seed there would defeat spec §5: the seed plus this repository plus
this module reproduces the entire packet-to-target mapping, so a seed in the
author's hands is the answer key in the author's hands, one command away.

The author manifest therefore records ``selection_seed_commitment`` —
``SHA256`` of the seed — and the reviewer-private manifest records the seed
itself. Provenance is preserved exactly: anyone holding both can verify the
seed matches the commitment, and the selection remains reproducible from the
commit. What is removed is the author's ability to invert it. This is a
deliberate, reported deviation from §12's literal wording in service of §5's
requirement, and it is the only one.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from .. import canonical
from ..errors import UsageError
from . import AUTHORING_TOOL_VERSION, masking, templates
from .composition import (
    MASKED_TOTAL,
    NATURAL_TOTAL,
    SEALED_TOTAL,
    natural_class_table,
)
from .selection import SelectionResult, SelectedTarget

AUTHOR_PACKET_NAME = "PAE_SEALED_AUTHOR_PACKET_V1"
REVIEWER_PACKET_NAME = "PAE_REVIEWER_PRIVATE_PACKET_V1"

AUTHOR_MANIFEST_SCHEMA = "pae-author-packet-manifest/1"
REVIEWER_MANIFEST_SCHEMA = "pae-reviewer-private-manifest/1"

_PACKET_ORDER_SALT = "packet-order/1"


def packet_order_key(uid: str) -> str:
    return hashlib.sha256(f"{uid}\n{_PACKET_ORDER_SALT}".encode("utf-8")).hexdigest()


def assign_packet_ids(targets: Sequence[SelectedTarget]) -> dict[str, str]:
    """``uid -> PKT-####``, ordered independently of the draw."""
    ordered = sorted(targets, key=lambda t: (packet_order_key(t.candidate.uid),
                                             t.candidate.uid))
    return {t.candidate.uid: f"PKT-{index:04d}"
            for index, t in enumerate(ordered, start=1)}


# --------------------------------------------------------------------------
# the mapping (reviewer-private)
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class PacketMapping:
    packet_id: str
    target_uid: str
    public_id: str
    source_path: str
    title: str
    description: str
    kind: str
    scope: str
    serving_policy: str
    cluster: str
    task_class: str
    selection_rank: int
    sanitized: masking.SanitizedBody
    guard_preserved: bool
    missing_guards: tuple[str, ...]

    def to_json_obj(self) -> dict[str, Any]:
        obj = {
            "packet_id": self.packet_id,
            "target_uid": self.target_uid,
            "public_id": self.public_id,
            "source_path": self.source_path,
            "title": self.title,
            "description": self.description,
            "kind": self.kind,
            "scope": self.scope,
            "serving_policy": self.serving_policy,
            "canonical_cluster": self.cluster,
            "assigned_class": self.task_class,
            "selection_rank": self.selection_rank,
            "guard_text_preserved": self.guard_preserved,
        }
        obj.update(self.sanitized.to_json_obj())
        if self.missing_guards:
            obj["missing_guard_headings"] = list(self.missing_guards)
        return obj

    def author_view(self) -> dict[str, Any]:
        """Only what the author may see. Used by the audit as a positive check."""
        return {"packet_id": self.packet_id, "task_class": self.task_class}


def build_mappings(
    selection: SelectionResult,
    records_by_uid: Mapping[str, Mapping[str, Any]],
    repo: Path,
) -> tuple[list[PacketMapping], list[str]]:
    """Sanitize every selected target's body and pair it with its identity."""
    packet_ids = assign_packet_ids(selection.targets)
    mappings: list[PacketMapping] = []
    problems: list[str] = []

    # Names of every *other* resource in the collection, so a packet cannot
    # hand the author a sibling's identity through a "use X instead" reference.
    # Built from the whole registry, not the draw: a real resource name is a
    # single search away from the collection whether or not it is one of the 45.
    all_identifier_keys = masking.foreign_identifier_keys(records_by_uid.values())
    # The in-draw titles get a second pass in whatever separator form the audit
    # would recognise, which is what keeps masker and audit from disagreeing.
    drawn_titles = {
        t.candidate.uid: str((records_by_uid.get(t.candidate.uid) or {}).get("title") or "")
        for t in selection.targets
    }

    for target in selection.targets:
        uid = target.candidate.uid
        record = records_by_uid.get(uid)
        if record is None:
            problems.append(f"{uid}: selected target is absent from the Registry")
            continue
        path = Path(repo) / target.candidate.source_path
        try:
            original = path.read_text(encoding="utf-8")
        except OSError as exc:
            problems.append(f"{uid}: cannot read body: {exc}")
            continue

        own_keys = masking.foreign_identifier_keys([record])
        sanitized = masking.sanitize_body(
            original,
            identifying_phrases=masking.identifying_phrases(record),
            foreign_identifier_keys=all_identifier_keys,
            own_identifier_keys=own_keys,
            foreign_phrases=[
                title for other_uid, title in drawn_titles.items()
                if other_uid != uid and len(title.split()) >= 2
            ],
        )
        preserved, missing = masking.guard_text_preserved(original, sanitized.text)
        if not preserved:
            problems.append(
                f"{uid}: sanitization dropped protected heading(s) {missing}; "
                "guard text is load-bearing content and must survive masking"
            )
        if not sanitized.text.strip():
            problems.append(f"{uid}: sanitized body is empty; nothing to author from")

        mappings.append(PacketMapping(
            packet_id=packet_ids[uid],
            target_uid=uid,
            public_id=target.candidate.public_id,
            source_path=target.candidate.source_path,
            title=str(record.get("title") or ""),
            description=str(record.get("description") or ""),
            kind=target.candidate.kind,
            scope=target.candidate.scope,
            serving_policy=target.candidate.serving_policy,
            cluster=target.candidate.cluster,
            task_class=target.task_class,
            selection_rank=target.rank,
            sanitized=sanitized,
            guard_preserved=preserved,
            missing_guards=tuple(missing),
        ))

    mappings.sort(key=lambda m: m.packet_id)
    return mappings, problems


# --------------------------------------------------------------------------
# author export
# --------------------------------------------------------------------------


def _write(path: Path, text: str) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = text.encode("utf-8")
    path.write_bytes(data)
    return canonical.sha256_bytes(data)


def build_author_packet(root: Path, mappings: Sequence[PacketMapping]) -> dict[str, str]:
    """Write the author-visible tree. Receives no identity but the class.

    Returns ``relative path -> digest`` for the manifest. Note the argument
    list: this function is given the mapping objects but writes only
    ``packet_id``, ``task_class`` and sanitized text from them. The audit
    verifies the result independently rather than trusting that claim.
    """
    root = Path(root)
    if root.exists() and any(root.iterdir()):
        raise UsageError(
            f"author export root is not empty: {root}; refusing to merge into an "
            "existing export, because a stale file is exactly what an audit "
            "would then have to catch"
        )
    digests: dict[str, str] = {}

    digests["READ_ME_FIRST.md"] = _write(
        root / "READ_ME_FIRST.md",
        templates.READ_ME_FIRST.format(masked_count=len(mappings)),
    )
    digests["AUTHOR_INSTRUCTIONS.md"] = _write(
        root / "AUTHOR_INSTRUCTIONS.md",
        templates.AUTHOR_INSTRUCTIONS.format(
            total_tasks=SEALED_TOTAL,
            natural_count=NATURAL_TOTAL,
            masked_count=len(mappings),
            class_guide="\n".join(
                f"**`{name}`** — {text}\n" for name, text in
                sorted(templates.CLASS_GUIDE.items())
            ),
        ),
    )
    digests["NATURAL_TASK_BRIEF.md"] = _write(
        root / "NATURAL_TASK_BRIEF.md",
        templates.NATURAL_TASK_BRIEF.format(
            natural_count=NATURAL_TOTAL,
            natural_class_table=natural_class_table(),
        ),
    )

    digests["natural-task-templates/README.md"] = _write(
        root / "natural-task-templates" / "README.md",
        templates.NATURAL_TEMPLATES_README,
    )
    digests["natural-task-templates/worked-shapes.md"] = _write(
        root / "natural-task-templates" / "worked-shapes.md",
        templates.WORKED_SHAPES,
    )

    digests["masked-resource-packets/README.md"] = _write(
        root / "masked-resource-packets" / "README.md",
        templates.MASKED_PACKETS_README.format(masked_count=len(mappings)),
    )
    for mapping in mappings:
        header = templates.PACKET_HEADER.format(
            packet_id=mapping.packet_id,
            task_class=mapping.task_class,
            class_description=templates.CLASS_GUIDE.get(mapping.task_class, ""),
        )
        rel = f"masked-resource-packets/{mapping.packet_id}.md"
        digests[rel] = _write(root / rel, header + mapping.sanitized.text)

    digests["submission-template/README.md"] = _write(
        root / "submission-template" / "README.md", templates.SUBMISSION_README,
    )
    digests["submission-template/tasks.jsonl"] = _write(
        root / "submission-template" / "tasks.jsonl", "",
    )
    digests["submission-template/provenance.json"] = _write(
        root / "submission-template" / "provenance.json",
        json.dumps(templates.PROVENANCE_TEMPLATE, indent=2, ensure_ascii=False) + "\n",
    )
    return digests


# --------------------------------------------------------------------------
# reviewer-private export
# --------------------------------------------------------------------------


def build_reviewer_packet(
    root: Path,
    mappings: Sequence[PacketMapping],
    selection: SelectionResult,
) -> dict[str, str]:
    """Write the reviewer-private tree: the mapping, plus how to use it."""
    root = Path(root)
    if root.exists() and any(root.iterdir()):
        raise UsageError(f"reviewer export root is not empty: {root}")
    digests: dict[str, str] = {}

    digests["README.md"] = _write(root / "README.md", templates.REVIEWER_README)
    digests["REVIEW_INSTRUCTIONS.md"] = _write(
        root / "REVIEW_INSTRUCTIONS.md", templates.REVIEW_INSTRUCTIONS,
    )

    mapping_doc = {
        "schema": "pae-packet-target-map/1",
        "warning": (
            "ANSWER KEY. Never place this file, its contents or any derivative "
            "in an author-visible location."
        ),
        "target_pae_commit": selection.target_pae_commit,
        "packet_count": len(mappings),
        "packets": [m.to_json_obj() for m in mappings],
    }
    digests["target-map/packet-target-map.json"] = _write(
        root / "target-map" / "packet-target-map.json",
        json.dumps(mapping_doc, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
    )
    digests["target-map/selection.json"] = _write(
        root / "target-map" / "selection.json",
        json.dumps(selection.to_json_obj(), indent=2, ensure_ascii=False,
                   sort_keys=True) + "\n",
    )

    digests["label-templates/README.md"] = _write(
        root / "label-templates" / "README.md", templates.LABEL_TEMPLATES_README,
    )
    digests["label-templates/label-record.json"] = _write(
        root / "label-templates" / "label-record.json",
        json.dumps(templates.LABEL_RECORD_TEMPLATE, indent=2,
                   ensure_ascii=False) + "\n",
    )
    digests["label-templates/adjudication-record.json"] = _write(
        root / "label-templates" / "adjudication-record.json",
        json.dumps(templates.ADJUDICATION_RECORD_TEMPLATE, indent=2,
                   ensure_ascii=False) + "\n",
    )
    digests["label-templates/reviewer-provenance.json"] = _write(
        root / "label-templates" / "reviewer-provenance.json",
        json.dumps(templates.REVIEWER_PROVENANCE_TEMPLATE, indent=2,
                   ensure_ascii=False) + "\n",
    )
    digests["candidate-tools/README.md"] = _write(
        root / "candidate-tools" / "README.md", templates.CANDIDATE_TOOLS_README,
    )
    return digests


# --------------------------------------------------------------------------
# manifests (spec §12)
# --------------------------------------------------------------------------


def _registry_hash(repo: Path) -> str:
    path = Path(repo) / "meta" / "registry" / "registry.jsonl"
    return canonical.sha256_file(path) if path.is_file() else ""


def author_manifest(
    *,
    repo: Path,
    selection: SelectionResult,
    mappings: Sequence[PacketMapping],
    digests: Mapping[str, str],
    created_at: str,
) -> dict[str, Any]:
    """Provenance for the author export. Names no target — see module docstring."""
    return {
        "schema": AUTHOR_MANIFEST_SCHEMA,
        "packet_name": AUTHOR_PACKET_NAME,
        "created_at": created_at,
        "tool_version": AUTHORING_TOOL_VERSION,
        "pae_commit": selection.target_pae_commit,
        "registry_sha256": _registry_hash(repo),
        "selection_algorithm_version": selection.algorithm_version,
        "masking_algorithm_version": masking.MASKING_ALGORITHM_VERSION,
        "selection_seed_commitment": canonical.sha256_text(selection.seed),
        "selection_seed_disclosure": (
            "The raw seed is reviewer-private. Seed + repository + selection "
            "algorithm reproduces the packet-to-target mapping, so publishing it "
            "here would hand the author the answer key. Holders of the "
            "reviewer-private manifest can verify the seed against this "
            "commitment."
        ),
        "development_exclusion_sha256": selection.development_exclusion_sha256,
        "eligible_population": dict(selection.population),
        "composition": selection.public_summary()["composition"],
        "packet_ids": [m.packet_id for m in mappings],
        "packet_count": len(mappings),
        "sanitized_packet_sha256": {
            m.packet_id: m.sanitized.sanitized_sha256 for m in mappings
        },
        "author_instructions_sha256": digests.get("AUTHOR_INSTRUCTIONS.md", ""),
        "natural_brief_sha256": digests.get("NATURAL_TASK_BRIEF.md", ""),
        "read_me_first_sha256": digests.get("READ_ME_FIRST.md", ""),
        "file_digests": dict(sorted(digests.items())),
        "contains_target_mapping": False,
    }


def reviewer_manifest(
    *,
    repo: Path,
    selection: SelectionResult,
    mappings: Sequence[PacketMapping],
    digests: Mapping[str, str],
    created_at: str,
) -> dict[str, Any]:
    return {
        "schema": REVIEWER_MANIFEST_SCHEMA,
        "packet_name": REVIEWER_PACKET_NAME,
        "warning": "Contains the answer key. Never hand to the task author.",
        "created_at": created_at,
        "tool_version": AUTHORING_TOOL_VERSION,
        "pae_commit": selection.target_pae_commit,
        "registry_sha256": _registry_hash(repo),
        "selection_algorithm_version": selection.algorithm_version,
        "masking_algorithm_version": masking.MASKING_ALGORITHM_VERSION,
        "selection_seed": selection.seed,
        "selection_seed_commitment": canonical.sha256_text(selection.seed),
        "development_exclusion_sha256": selection.development_exclusion_sha256,
        "packet_integrity": [
            {
                "packet_id": m.packet_id,
                "target_uid": m.target_uid,
                "original_sha256": m.sanitized.original_sha256,
                "sanitized_sha256": m.sanitized.sanitized_sha256,
                "operations": list(m.sanitized.operations),
                "guard_text_preserved": m.guard_preserved,
            }
            for m in mappings
        ],
        "file_digests": dict(sorted(digests.items())),
        "contains_target_mapping": True,
    }


def write_manifest(path: Path, manifest: Mapping[str, Any]) -> str:
    """Write a manifest and its ``.sha256`` sidecar. Returns the digest."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    encoded = data.encode("utf-8")
    path.write_bytes(encoded)
    digest = canonical.sha256_bytes(encoded)
    sidecar = path.with_name(path.name + ".sha256")
    sidecar.write_text(f"{digest}  {path.name}\n", encoding="utf-8")
    return digest
