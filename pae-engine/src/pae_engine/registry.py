"""Reading, resolving and serving from the normalized PAE Registry.

The registry is the Engine's whole resource contract. Nothing here re-derives
corpus membership, identity, kinds or relationships — that work belongs to the
repository-maintenance generator, and duplicating it would create a second
source of truth that could disagree with the frozen one.

Two invariants shape the code below:

* **Read-only.** The Engine opens files for reading and does nothing else to
  the filesystem.
* **Retrieved text is data.** A resource body is bytes to hand back, never
  something to interpret, template, expand or execute.
"""

from __future__ import annotations

import hashlib
import json
import re
import stat as stat_module
from pathlib import Path, PurePosixPath
from typing import Any, Iterator, Mapping, Optional

from .errors import (
    ChecksumMismatch,
    IncompatibleRegistry,
    MalformedReference,
    NoAddressableContent,
    PathSecurityError,
    RegistryValidationError,
    ResourceExcluded,
    ResourceNotFound,
    SourceTooLarge,
    SourceUnavailable,
)
from .models import Content, Record, Resolution, Summary
from .repository import Repository

__all__ = [
    "Registry",
    "UID_PATTERN",
    "PUBLIC_ID_PATTERN",
    "MAX_CONTENT_BYTES",
    "classify_ref",
]

#: Immutable internal key.
UID_PATTERN = re.compile(r"^pae_[0-9abcdefghjkmnpqrstvwxyz]{12}$")

#: Human-readable handle. Always scoped, so it always contains a colon.
PUBLIC_ID_PATTERN = re.compile(
    r"^[a-z]+:[A-Za-z0-9]+([.-][A-Za-z0-9]+)*(/[A-Za-z0-9]+([.-][A-Za-z0-9]+)*)*$"
)

#: Hard ceiling on a served source, in bytes.
#:
#: Every source in the corpus today is orders of magnitude smaller than this
#: (the largest are tens of kilobytes), so the ceiling never touches a valid
#: resource. What it does is bound the damage if a registry path is ever made
#: to point at something pathological: the call fails instead of streaming an
#: arbitrarily large file into an agent's context.
MAX_CONTENT_BYTES = 4 * 1024 * 1024

#: Characters that appear verbatim inside a JSON string, so a substring
#: prefilter over raw registry lines cannot produce a false negative for them.
_PREFILTER_SAFE = re.compile(r"^[A-Za-z0-9:/._-]+$")


def classify_ref(ref: str) -> str:
    """``"uid"`` or ``"public_id"``, or raise.

    A reference that satisfies neither grammar is a usage error. Reporting it
    as "not found" would tell a caller to go looking for a resource when the
    real fix is to correct what they typed.
    """
    if not isinstance(ref, str) or not ref:
        raise MalformedReference("reference is empty", ref=ref if isinstance(ref, str) else None)
    if UID_PATTERN.match(ref):
        return "uid"
    if PUBLIC_ID_PATTERN.match(ref):
        return "public_id"
    raise MalformedReference(
        f"{ref!r} is neither a PAE UID (pae_ + 12 Crockford base32 characters) nor a "
        "public ID (scope:path)",
        ref=ref,
        uid_pattern=UID_PATTERN.pattern,
        public_id_pattern=PUBLIC_ID_PATTERN.pattern,
    )


def _validate_relative_path(raw_path: Optional[str]) -> Optional[str]:
    """Reject a stored path before it is joined to anything.

    Registry paths are untrusted input: the registry is a generated file that a
    consumer may be reading from any checkout. Every rejection reason is
    returned rather than raised so the caller can attach resource identity.
    """
    if raw_path is None or raw_path == "":
        return "stored source path is empty"
    if "\x00" in raw_path:
        return "stored source path contains a NUL byte"
    if raw_path.startswith("/"):
        return "stored source path is absolute (POSIX)"
    if re.match(r"^[A-Za-z]:", raw_path):
        return "stored source path is absolute (Windows drive)"
    if raw_path.startswith("\\\\") or raw_path.startswith("//"):
        return "stored source path is a UNC path"
    if "\\" in raw_path:
        return "stored source path contains a backslash separator"
    parts = PurePosixPath(raw_path).parts
    if ".." in parts:
        return "stored source path contains a '..' component"
    return None


class Registry:
    """Lazy, streaming access to one checkout's registry.

    Opening reads nothing. A lookup streams the JSONL at most once. There is no
    persistent cache, no index file and no database: the access patterns that
    would justify one belong to search, which does not exist yet, and inventing
    a cache now would freeze the wrong shape.
    """

    def __init__(self, repository: Repository) -> None:
        self.repository = repository
        self._all: Optional[tuple[Record, ...]] = None

    @classmethod
    def open(cls, repository: Repository) -> "Registry":
        return cls(repository)

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return f"Registry(root={self.repository.root!s})"

    # -- summary -----------------------------------------------------------

    def stats(self, *, verify: bool = False) -> Summary:
        """The generated summary, optionally recounted against the records.

        Without ``verify`` this reads one small JSON file and never touches the
        10 MB JSONL, which is what makes ``pae stats`` fast.
        """
        path = self.repository.summary_path
        try:
            obj = json.loads(path.read_text(encoding="utf-8"))
        except OSError as exc:
            raise RegistryValidationError(
                f"registry summary could not be read: {path}", path=str(path), reason=str(exc)
            ) from None
        except json.JSONDecodeError as exc:
            raise IncompatibleRegistry(
                f"registry summary is not valid JSON: {path}", path=str(path), reason=str(exc)
            ) from None
        summary = Summary.from_raw(obj, verified=False)
        if not verify:
            return summary
        self._verify_summary(summary)
        return summary.with_verified(True)

    def _verify_summary(self, summary: Summary) -> None:
        from .validate import recount, summary_drift

        counts = recount(self.records())
        drift = summary_drift(summary, counts)
        if drift:
            raise RegistryValidationError(
                "registry summary disagrees with the records it summarizes",
                drift=drift,
                path=str(self.repository.summary_path),
            )

    # -- iteration ---------------------------------------------------------

    def records(self) -> Iterator[Record]:
        """Stream every record. Bounded memory; nothing is retained."""
        if self._all is not None:
            yield from self._all
            return
        for _lineno, obj in self._raw_records():
            yield Record.from_raw(obj)

    def load_all(self) -> tuple[Record, ...]:
        """Every record, memoized for the life of the process.

        Deliberately opt-in: parsing the whole registry costs roughly a second
        and tens of megabytes, which a single ``pae get`` should never pay.
        """
        if self._all is None:
            self._all = tuple(Record.from_raw(obj) for _lineno, obj in self._raw_records())
        return self._all

    def _raw_records(self) -> Iterator[tuple[int, Mapping[str, Any]]]:
        path = self.repository.registry_path
        try:
            handle = open(path, "r", encoding="utf-8")
        except OSError as exc:
            raise RegistryValidationError(
                f"registry could not be read: {path}", path=str(path), reason=str(exc)
            ) from None
        with handle as fh:
            for lineno, line in enumerate(fh, 1):
                if not line.strip():
                    continue
                yield lineno, _decode_line(line, path, lineno)

    # -- lookup ------------------------------------------------------------

    def _lookup(self, ref: str) -> tuple[Record, str, Optional[str]]:
        """Find one record by UID, current public ID or retired alias.

        Precedence is current public ID, then retired alias. An alias match is
        therefore held rather than returned, so a current ID appearing later in
        the file still wins; a current-ID match can return immediately because
        public IDs are unique and nothing outranks them.
        """
        ref_kind = classify_ref(ref)
        path = self.repository.registry_path

        # A raw-substring prefilter avoids decoding ~5,000 JSON objects for a
        # miss. It is only applied when the reference contains no character
        # JSON could escape, so it can skip a line only when that line provably
        # cannot match. Correctness never depends on it: when the guard fails,
        # every line is decoded instead.
        needle = f'"{ref}"' if _PREFILTER_SAFE.match(ref) else None

        alias_hit: Optional[Mapping[str, Any]] = None
        try:
            handle = open(path, "r", encoding="utf-8")
        except OSError as exc:
            raise RegistryValidationError(
                f"registry could not be read: {path}", path=str(path), reason=str(exc)
            ) from None
        with handle as fh:
            for lineno, line in enumerate(fh, 1):
                if needle is not None and needle not in line:
                    continue
                if not line.strip():
                    continue
                obj = _decode_line(line, path, lineno)
                if ref_kind == "uid":
                    if obj.get("uid") == ref:
                        return Record.from_raw(obj), "uid", None
                    continue
                if obj.get("id") == ref:
                    return Record.from_raw(obj), "public_id", None
                if alias_hit is None and ref in (obj.get("aliases") or ()):
                    alias_hit = obj

        if alias_hit is not None:
            return Record.from_raw(alias_hit), "alias", ref

        raise ResourceNotFound(
            f"no registry record claims {ref!r}", ref=ref, ref_kind=ref_kind
        )

    def resolve(self, ref: str) -> Resolution:
        """Identity only. Resolves excluded resources too.

        Identity is public API; serving is not. Refusing to resolve an excluded
        resource would make it indistinguishable from one that never existed,
        and the registry deliberately keeps those apart.
        """
        record, ref_kind, matched_alias = self._lookup(ref)
        return Resolution.from_record(
            record, ref_given=ref, ref_kind=ref_kind, matched_alias=matched_alias
        )

    def lookup(self, ref: str) -> tuple[Resolution, Record]:
        """Resolution and record together, from a single pass.

        Same access gate as :meth:`get`.
        """
        record, ref_kind, matched_alias = self._lookup(ref)
        self._require_metadata_allowed(record, ref)
        resolution = Resolution.from_record(
            record, ref_given=ref, ref_kind=ref_kind, matched_alias=matched_alias
        )
        return resolution, record

    def get(self, ref: str) -> Record:
        """The full record, unless serving policy withholds it."""
        return self.lookup(ref)[1]

    @staticmethod
    def _require_metadata_allowed(record: Record, ref: str) -> None:
        if record.serving_policy == "excluded":
            raise ResourceExcluded(
                f"{record.id} is excluded from serving; identity is available, its record "
                "is not",
                ref=ref,
                uid=record.uid,
                serving_policy=record.serving_policy,
                resource=record.identity_stub(),
            )

    # -- content -----------------------------------------------------------

    def content(self, ref: str) -> Content:
        """A whole, verified resource body.

        The order of the checks below is load-bearing. Exclusion is an identity
        level refusal and comes first. Addressability comes next, so a
        tombstone or a technique reports "no body" rather than a policy
        refusal — a caller can act on that difference. Only then is policy
        consulted, and only after that is any file opened: a withheld resource
        is never read from disk merely to be discarded.
        """
        record, _ref_kind, _alias = self._lookup(ref)
        self._require_metadata_allowed(record, ref)

        if record.lifecycle == "tombstone":
            raise NoAddressableContent(
                f"{record.id} is a tombstone; the historical body no longer exists",
                ref=ref,
                uid=record.uid,
                id=record.id,
                lifecycle=record.lifecycle,
                replacement=_json_replacement(record),
            )

        if not record.source_path:
            raise NoAddressableContent(
                f"{record.id} has no independently addressable body"
                + (f"; it is defined in {record.defined_in}" if record.defined_in else ""),
                ref=ref,
                uid=record.uid,
                id=record.id,
                kind=record.kind,
                defined_in=record.defined_in,
            )

        if record.serving_policy == "metadata_only":
            raise self._content_refused(record, ref)

        return self._read_verified(record, ref)

    @staticmethod
    def _content_refused(record: Record, ref: str):
        from .errors import ContentRefused

        detail = (
            f"{record.id} is served as metadata only; its body is withheld"
            if record.serving_policy_recognized
            else (
                f"{record.id} declares an unrecognized serving policy "
                f"({record.serving_policy_declared!r}); the engine fails closed to "
                "metadata_only and withholds the body"
            )
        )
        return ContentRefused(
            detail,
            ref=ref,
            uid=record.uid,
            id=record.id,
            serving_policy=record.serving_policy,
            declared_serving_policy=record.serving_policy_declared,
            policy_recognized=record.serving_policy_recognized,
        )

    def _read_verified(self, record: Record, ref: str) -> Content:
        root = self.repository.root
        rel = record.source_path or ""

        reason = _validate_relative_path(rel)
        if reason is not None:
            raise PathSecurityError(
                f"{reason}: {rel!r}", ref=ref, uid=record.uid, id=record.id, path=rel
            )

        candidate = (root / rel).resolve()
        if not candidate.is_relative_to(root):
            # Reached only via a symlink that leaves the checkout, since the
            # lexical checks above already rejected traversal and absolutes.
            raise PathSecurityError(
                f"source path resolves outside the repository root: {rel!r} -> {candidate}",
                ref=ref,
                uid=record.uid,
                id=record.id,
                path=rel,
                resolved=str(candidate),
                root=str(root),
            )

        try:
            st = candidate.stat()
        except FileNotFoundError:
            raise SourceUnavailable(
                f"source file does not exist: {rel}",
                ref=ref,
                uid=record.uid,
                id=record.id,
                path=rel,
            ) from None
        except OSError as exc:
            raise SourceUnavailable(
                f"source file could not be inspected: {rel}",
                ref=ref,
                uid=record.uid,
                id=record.id,
                path=rel,
                reason=str(exc),
            ) from None

        if not stat_module.S_ISREG(st.st_mode):
            raise SourceUnavailable(
                f"source path is not a regular file: {rel}",
                ref=ref,
                uid=record.uid,
                id=record.id,
                path=rel,
            )

        if st.st_size > MAX_CONTENT_BYTES:
            raise SourceTooLarge(
                f"source is {st.st_size} bytes, above the {MAX_CONTENT_BYTES}-byte ceiling: {rel}",
                ref=ref,
                uid=record.uid,
                id=record.id,
                path=rel,
                size=st.st_size,
                ceiling=MAX_CONTENT_BYTES,
            )

        if record.checksum_payload != "raw_source_bytes":
            raise ChecksumMismatch(
                f"{record.id} declares checksum payload {record.checksum_payload!r}, which "
                "this engine cannot verify (expected 'raw_source_bytes')",
                ref=ref,
                uid=record.uid,
                id=record.id,
                path=rel,
                checksum_payload=record.checksum_payload,
            )
        if not record.content_sha256:
            raise ChecksumMismatch(
                f"{record.id} records no content checksum, so its body cannot be verified",
                ref=ref,
                uid=record.uid,
                id=record.id,
                path=rel,
            )

        try:
            data = candidate.read_bytes()
        except OSError as exc:
            raise SourceUnavailable(
                f"source file could not be read: {rel}",
                ref=ref,
                uid=record.uid,
                id=record.id,
                path=rel,
                reason=str(exc),
            ) from None

        # A second size check, because the file could have changed between the
        # stat and the read.
        if len(data) > MAX_CONTENT_BYTES:
            raise SourceTooLarge(
                f"source is {len(data)} bytes, above the {MAX_CONTENT_BYTES}-byte ceiling: {rel}",
                ref=ref,
                uid=record.uid,
                id=record.id,
                path=rel,
                size=len(data),
                ceiling=MAX_CONTENT_BYTES,
            )

        actual = "sha256:" + hashlib.sha256(data).hexdigest()
        if actual != record.content_sha256:
            raise ChecksumMismatch(
                f"{rel} does not match the checksum recorded for {record.id}. The file on "
                "disk differs from the one the generated registry describes — usually an "
                "uncommitted local edit, or a registry that has not been regenerated.",
                ref=ref,
                uid=record.uid,
                id=record.id,
                path=rel,
                expected=record.content_sha256,
                actual=actual,
            )

        return Content(
            uid=record.uid,
            id=record.id,
            data=data,
            byte_length=len(data),
            content_sha256=record.content_sha256,
            verified=True,
            serving_policy=record.serving_policy,
            guard_preservation=record.guard_preservation,
            source_path=rel,
        )


def _decode_line(line: str, path: Path, lineno: int) -> Mapping[str, Any]:
    try:
        obj = json.loads(line)
    except json.JSONDecodeError as exc:
        raise RegistryValidationError(
            f"{path}:{lineno} is not valid JSON",
            path=str(path),
            line=lineno,
            reason=str(exc),
        ) from None
    if not isinstance(obj, dict):
        raise RegistryValidationError(
            f"{path}:{lineno} is not a JSON object", path=str(path), line=lineno
        )
    return obj


def _json_replacement(record: Record) -> Optional[dict[str, Any]]:
    from .models import replacement_of

    return replacement_of(record)
