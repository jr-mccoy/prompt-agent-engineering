"""Immutable public value objects returned by the Engine.

Each model owns its own JSON serialization. The CLI calls ``to_json_obj()``
rather than selecting fields itself, so there is exactly one description of the
machine-readable contract and a future MCP server gets the same shapes for
free.

Every model keeps the normalized registry object it came from in ``raw``.
Registry record schema v1 may gain additive keys; a later phase can consume
them without waiting for a typed attribute to be promoted here.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Any, Mapping, Optional

from .errors import ContentEncodingError, IncompatibleRegistry

__all__ = [
    "RECORD_SCHEMA",
    "SUMMARY_SCHEMA",
    "SERVING_POLICIES",
    "FAIL_CLOSED_POLICY",
    "Record",
    "Resolution",
    "Content",
    "Summary",
]

#: The only registry contracts this Engine implements.
RECORD_SCHEMA = "pae-registry-record/1"
SUMMARY_SCHEMA = "pae-registry-summary/1"

#: Recognized serving policies, in no particular order — they are not a scale.
SERVING_POLICIES = frozenset({"standard", "safety_gated", "metadata_only", "excluded"})

#: What an unknown or missing policy is treated as. Never ``standard``:
#: a policy the Engine cannot interpret must withhold the body, not serve it.
FAIL_CLOSED_POLICY = "metadata_only"


def _plain(value: Any) -> Any:
    """Recursively convert mappings/sequences into plain JSON-ready containers.

    Callers own the result, so mutating it cannot reach back into a model.
    """
    if isinstance(value, (dict, MappingProxyType)):
        return {k: _plain(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(v) for v in value]
    return value


def _freeze(value: Any) -> Any:
    if isinstance(value, dict):
        return MappingProxyType({k: _freeze(v) for k, v in value.items()})
    if isinstance(value, list):
        return tuple(_freeze(v) for v in value)
    return value


@dataclass(frozen=True)
class Record:
    """One normalized registry record."""

    uid: str
    id: str
    kind: str
    lifecycle: str
    title: str
    description: Optional[str]
    aliases: tuple[str, ...]
    maturity: Optional[str]
    review_status: Optional[str]
    eval_status: Optional[str]
    metadata_completeness: Optional[str]
    #: The policy the Engine enforces. Equals ``serving_policy_declared`` when
    #: that value is recognized, and ``metadata_only`` when it is not.
    serving_policy: str
    serving_policy_declared: Optional[str]
    serving_policy_recognized: bool
    guard_preservation: Optional[Mapping[str, Any]]
    source_path: Optional[str]
    birth_path: Optional[str]
    previous_paths: tuple[str, ...]
    content_sha256: Optional[str]
    checksum_payload: Optional[str]
    defined_in: Optional[str]
    raw: Mapping[str, Any] = field(repr=False)

    # -- derived, cheap ----------------------------------------------------

    @property
    def has_body(self) -> bool:
        """Whether an independently addressable file backs this resource.

        False for techniques (defined inside the master technique index) and
        for tombstones (the file no longer exists).
        """
        return self.lifecycle == "live" and bool(self.source_path)

    @property
    def content_available(self) -> bool:
        """Whether ``Registry.content()`` can succeed, policy included."""
        return self.has_body and self.serving_policy in ("standard", "safety_gated")

    def identity_stub(self) -> dict[str, Any]:
        """The minimum that keeps an excluded resource distinguishable from
        one that does not exist. No title, description, native fields or body.
        """
        return {
            "uid": self.uid,
            "id": self.id,
            "kind": self.kind,
            "lifecycle": self.lifecycle,
            "serving_policy": self.serving_policy,
        }

    def to_json_obj(self) -> dict[str, Any]:
        """The normalized registry record, exactly as the registry states it."""
        return _plain(self.raw)

    def serving_json_obj(self) -> dict[str, Any]:
        """How the Engine read this record's serving policy.

        Separate from ``to_json_obj()`` so the registry's own record shape is
        never mixed with the Engine's interpretation of it.
        """
        return {
            "effective_policy": self.serving_policy,
            "declared_policy": self.serving_policy_declared,
            "policy_recognized": self.serving_policy_recognized,
            "has_body": self.has_body,
            "content_available": self.content_available,
        }

    @classmethod
    def from_raw(cls, obj: Mapping[str, Any], *, origin: str = "registry") -> "Record":
        declared_schema = obj.get("schema_version")
        if declared_schema != RECORD_SCHEMA:
            raise IncompatibleRegistry(
                "registry record declares an unsupported schema: "
                f"{declared_schema!r} (this engine implements {RECORD_SCHEMA!r})",
                declared_schema=declared_schema,
                supported_schema=RECORD_SCHEMA,
                origin=origin,
                uid=obj.get("uid"),
            )

        policy_block = obj.get("serving_policy") or {}
        declared_policy = policy_block.get("value") if isinstance(policy_block, dict) else None
        recognized = declared_policy in SERVING_POLICIES
        effective = declared_policy if recognized else FAIL_CLOSED_POLICY

        source = obj.get("source") or {}
        governance = obj.get("governance") or {}

        return cls(
            uid=obj.get("uid", ""),
            id=obj.get("id", ""),
            kind=obj.get("kind", ""),
            lifecycle=obj.get("lifecycle", ""),
            title=obj.get("title", ""),
            description=obj.get("description"),
            aliases=tuple(obj.get("aliases") or ()),
            maturity=governance.get("maturity"),
            review_status=governance.get("review_status"),
            eval_status=governance.get("eval_status"),
            metadata_completeness=obj.get("metadata_completeness"),
            serving_policy=effective,
            serving_policy_declared=declared_policy,
            serving_policy_recognized=recognized,
            guard_preservation=_freeze(policy_block.get("guard_preservation"))
            if isinstance(policy_block, dict)
            else None,
            source_path=source.get("path"),
            birth_path=source.get("birth_path"),
            previous_paths=tuple(source.get("previous_paths") or ()),
            content_sha256=source.get("content_sha256"),
            checksum_payload=source.get("checksum_payload"),
            defined_in=obj.get("defined_in"),
            raw=_freeze(dict(obj)),
        )


@dataclass(frozen=True)
class Resolution:
    """How a caller's reference mapped onto a registry identity.

    Alias use is always reported. Silently answering a retired public ID as
    though it were current would hide a rename from the caller.
    """

    ref_given: str
    ref_kind: str  # "uid" | "public_id" | "alias"
    uid: str
    current_id: str
    lifecycle: str
    matched_alias: Optional[str]
    replacement: Optional[Mapping[str, Any]]

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "ref_given": self.ref_given,
            "ref_kind": self.ref_kind,
            "uid": self.uid,
            "current_id": self.current_id,
            "lifecycle": self.lifecycle,
            "matched_alias": self.matched_alias,
            "replacement": _plain(self.replacement) if self.replacement is not None else None,
        }

    @classmethod
    def from_record(
        cls, record: Record, *, ref_given: str, ref_kind: str, matched_alias: Optional[str]
    ) -> "Resolution":
        return cls(
            ref_given=ref_given,
            ref_kind=ref_kind,
            uid=record.uid,
            current_id=record.id,
            lifecycle=record.lifecycle,
            matched_alias=matched_alias,
            replacement=replacement_of(record),
        )


def replacement_of(record: Record) -> Optional[dict[str, Any]]:
    """Where a superseded, merged or split resource went, if anywhere.

    Reported, never followed: redirecting a caller to a replacement's content
    would answer a question they did not ask.
    """
    relationships = record.raw.get("relationships") or {}
    superseded_by = relationships.get("superseded_by")
    if superseded_by:
        return {"relation": "superseded_by", "edges": [_plain(superseded_by)]}
    merged_into = relationships.get("merged_into")
    if merged_into:
        return {"relation": "merged_into", "edges": [_plain(merged_into)]}
    split_into = relationships.get("split_into")
    if split_into:
        return {"relation": "split_into", "edges": _plain(split_into)}
    return None


@dataclass(frozen=True)
class Content:
    """A verified, whole resource body.

    There is no partial variant. For guard-preserving resources truncation is
    not merely discouraged, it is structurally unavailable.
    """

    uid: str
    id: str
    data: bytes = field(repr=False)
    byte_length: int
    content_sha256: str
    verified: bool
    serving_policy: str
    guard_preservation: Optional[Mapping[str, Any]]
    source_path: str

    def text(self) -> str:
        """Strictly decoded UTF-8.

        A text resource that is not valid UTF-8 is an integrity failure, not an
        invitation to substitute replacement characters. Raw byte output stays
        available for callers that need the file exactly as stored.
        """
        try:
            return self.data.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise ContentEncodingError(
                "source bytes are not valid UTF-8; use raw content output to read "
                "them exactly as stored",
                uid=self.uid,
                id=self.id,
                path=self.source_path,
                reason=str(exc),
            ) from None

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "uid": self.uid,
            "id": self.id,
            "content": self.text(),
            "encoding": "utf-8",
            "byte_length": self.byte_length,
            "content_sha256": self.content_sha256,
            "verified": self.verified,
            "serving_policy": self.serving_policy,
            "guard_preservation": _plain(self.guard_preservation)
            if self.guard_preservation is not None
            else {},
        }


@dataclass(frozen=True)
class Summary:
    """The generated registry summary, plus whether it was recounted."""

    schema: str
    total_records: int
    by_lifecycle: Mapping[str, int]
    by_kind: Mapping[str, int]
    by_kind_live: Mapping[str, int]
    by_kind_tombstone: Mapping[str, int]
    by_serving_policy: Mapping[str, int]
    by_maturity: Mapping[str, int]
    by_metadata_completeness: Mapping[str, int]
    verified: bool
    raw: Mapping[str, Any] = field(repr=False)

    def to_json_obj(self) -> dict[str, Any]:
        return _plain(self.raw)

    @classmethod
    def from_raw(cls, obj: Mapping[str, Any], *, verified: bool = False) -> "Summary":
        declared_schema = obj.get("schema")
        if declared_schema != SUMMARY_SCHEMA:
            raise IncompatibleRegistry(
                "registry summary declares an unsupported schema: "
                f"{declared_schema!r} (this engine implements {SUMMARY_SCHEMA!r})",
                declared_schema=declared_schema,
                supported_schema=SUMMARY_SCHEMA,
            )
        return cls(
            schema=declared_schema,
            total_records=int(obj.get("total_records", 0)),
            by_lifecycle=_freeze(obj.get("by_lifecycle") or {}),
            by_kind=_freeze(obj.get("by_kind") or {}),
            by_kind_live=_freeze(obj.get("by_kind_live") or {}),
            by_kind_tombstone=_freeze(obj.get("by_kind_tombstone") or {}),
            by_serving_policy=_freeze(obj.get("by_serving_policy") or {}),
            by_maturity=_freeze(obj.get("by_maturity") or {}),
            by_metadata_completeness=_freeze(obj.get("by_metadata_completeness") or {}),
            verified=verified,
            raw=_freeze(dict(obj)),
        )

    def with_verified(self, verified: bool) -> "Summary":
        return Summary.from_raw(self.raw, verified=verified)
