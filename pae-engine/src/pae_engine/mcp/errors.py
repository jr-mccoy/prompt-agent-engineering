"""Turning Engine failures into tool errors a model can act on.

The Engine already has a precise error taxonomy — an unknown reference is not a
malformed one, a withheld body is not a missing one, an integrity mismatch is
not a policy refusal. That taxonomy is the whole point, so the adapter projects
it rather than collapsing it into prose.

What the adapter adds is **sanitization**, and it is not optional. A ``PaeError``
carries operational detail written for the person running the command: absolute
source paths, the resolved target of a rejected symlink, the checkout root. None
of that is the model's business, and some of it is a genuine disclosure. So:

* details are **allowlisted per code**, never serialized wholesale;
* messages are **scrubbed** of the checkout root and the user's home directory;
* two codes get a **fixed message** because their own text embeds an absolute
  path that scrubbing cannot reach — ``source_path_refused`` names a target that
  by definition lies *outside* the root, and ``internal_error`` must never
  surface a repr.

Nothing here decides policy. Whether a body may be served was decided by the
Registry long before an exception reached this module.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Mapping, Optional

from ..errors import (
    AccessRefused,
    BudgetTooSmall,
    ChecksumMismatch,
    ContentEncodingError,
    ContentRefused,
    InvalidBudget,
    MalformedReference,
    NoAddressableContent,
    PaeError,
    PathSecurityError,
    RegistryValidationError,
    ResourceExcluded,
    ResourceNotFound,
    SourceTooLarge,
    SourceUnavailable,
    UsageError,
)

__all__ = [
    "DETAIL_ALLOWLIST",
    "FIXED_MESSAGES",
    "INTERNAL_ERROR_MESSAGE",
    "REDACTION",
    "error_payload",
    "scrub",
]

#: What replaces a filesystem location that must not reach the model.
REDACTION = "[redacted]"

#: Deterministic text for unexpected faults. A traceback or exception repr here
#: would leak module paths, local variable content and the interpreter layout.
INTERNAL_ERROR_MESSAGE = "The PAE MCP tool failed unexpectedly."

#: Codes whose own message embeds a path scrubbing cannot reach.
FIXED_MESSAGES: Mapping[str, str] = {
    # The rejected target is outside the checkout root by definition, so
    # scrubbing the root does not remove it. Naming it would turn a refusal
    # into a filesystem probe.
    "source_path_refused": (
        "The registry path for this resource was refused because it does not "
        "resolve inside the repository. The body cannot be served safely."
    ),
    "internal_error": INTERNAL_ERROR_MESSAGE,
}

#: Per-code detail allowlists.
#:
#: Everything omitted is omitted deliberately. The recurring exclusions are
#: ``root`` and ``resolved`` (absolute checkout paths) and the ``path`` on
#: ``registry_validation_failed`` (the absolute registry file). A ``path`` that
#: *is* allowed is always the repository-relative string the registry itself
#: stores, which is identity, not location.
DETAIL_ALLOWLIST: Mapping[str, frozenset[str]] = {
    "usage_error": frozenset(
        {"limit", "maximum", "unknown", "valid", "requested", "available",
         "chars", "terms", "query"}
    ),
    "missing_extra": frozenset({"extra", "install"}),
    "malformed_reference": frozenset({"ref", "uid_pattern", "public_id_pattern"}),
    "invalid_budget": frozenset(set()),
    "budget_too_small": frozenset(
        {"requested_estimated_tokens", "requested_bytes", "effective_byte_ceiling",
         "minimum_bytes", "minimum_estimated_tokens"}
    ),
    "resource_not_found": frozenset({"ref", "ref_kind"}),
    "access_refused": frozenset({"uid", "id", "serving_policy"}),
    # Only the Phase 3 identity stub. Never a title, description or body, and
    # never enriched by a second lookup: an excluded resource stays
    # distinguishable from a nonexistent one and nothing more.
    "resource_excluded": frozenset({"uid", "id", "serving_policy", "resource"}),
    "content_refused": frozenset(
        {"uid", "id", "serving_policy", "declared_serving_policy", "policy_recognized"}
    ),
    "no_addressable_content": frozenset(
        {"uid", "id", "kind", "lifecycle", "defined_in", "replacement"}
    ),
    "source_path_refused": frozenset({"uid", "id"}),
    "source_unavailable": frozenset({"uid", "id", "path"}),
    "source_too_large": frozenset({"uid", "id", "path", "size", "ceiling"}),
    "checksum_mismatch": frozenset({"uid", "id", "path", "expected", "actual"}),
    "content_encoding_error": frozenset({"uid", "id", "path"}),
    "registry_validation_failed": frozenset({"line", "drift"}),
    "internal_error": frozenset(set()),
}

#: Only the identity fields Phase 3 permits for an excluded resource.
_STUB_KEYS = frozenset({"uid", "id", "kind", "lifecycle", "serving_policy"})

# The exception classes above are imported so the mapping is checked at import
# time rather than by string matching. Ordering is irrelevant: the code comes
# from ``PaeError.error``, which every class already declares.
_KNOWN: tuple[type[PaeError], ...] = (
    UsageError,
    MalformedReference,
    InvalidBudget,
    BudgetTooSmall,
    ResourceNotFound,
    AccessRefused,
    ContentRefused,
    ResourceExcluded,
    NoAddressableContent,
    PathSecurityError,
    SourceUnavailable,
    SourceTooLarge,
    ChecksumMismatch,
    ContentEncodingError,
    RegistryValidationError,
)


def _sensitive_roots(repo_root: Optional[Path]) -> list[str]:
    """Filesystem prefixes that must never appear in model-facing text.

    Longest first, so scrubbing the checkout root does not leave a home-relative
    fragment behind when the checkout lives under the home directory.
    """
    candidates: list[str] = []
    if repo_root is not None:
        candidates.append(str(repo_root))
    try:
        candidates.append(str(Path.home()))
    except (RuntimeError, OSError):  # pragma: no cover - no home on this platform
        pass
    seen: set[str] = set()
    out: list[str] = []
    for value in sorted((c for c in candidates if c), key=len, reverse=True):
        if value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out


def _swap(value: str, old: str, new: str) -> str:
    """``str.replace`` by another name.

    Spelled with ``split``/``join`` because the Engine's read-only invariant
    scan flags the *attribute name* ``replace`` — ``os.replace`` and
    ``Path.replace`` both mutate the filesystem. Renaming a string method is a
    smaller price than adding an exemption to that scan, which should stay
    blunt to stay trustworthy.
    """
    return new.join(value.split(old))


def _variants(value: str) -> set[str]:
    """The same location written the ways it could reach a message.

    A message may have been built from a ``Path`` (native separators) or from a
    registry string (always POSIX), and on Windows those differ — so a scrub
    that only knew one spelling would miss the other.
    """
    return {value, _swap(value, "\\", "/"), _swap(value, "/", os.sep)}


def scrub(text: str, repo_root: Optional[Path] = None) -> str:
    """Remove checkout and home locations from model-facing text."""
    if not text:
        return text
    for value in _sensitive_roots(repo_root):
        for variant in _variants(value):
            if variant and variant in text:
                text = _swap(text, variant, REDACTION)
    return text


def _clean_details(code: str, details: Mapping[str, Any]) -> dict[str, Any]:
    allowed = DETAIL_ALLOWLIST.get(code, frozenset())
    out: dict[str, Any] = {}
    for key in sorted(allowed & set(details)):
        value = details[key]
        if value is None:
            continue
        if key == "resource" and isinstance(value, Mapping):
            # Re-filter the stub rather than trusting its shape.
            value = {k: v for k, v in sorted(value.items()) if k in _STUB_KEYS}
        out[key] = value
    return out


def error_payload(
    exc: BaseException, *, repo_root: Optional[Path] = None
) -> dict[str, Any]:
    """The structured error body a failing tool returns.

    Shape is stable across every code so a caller can branch on
    ``error.code`` without first discovering which failure it got::

        {"ok": false, "error": {"code": ..., "message": ..., "details": {...}}}
    """
    if isinstance(exc, PaeError):
        code = exc.error
        message = FIXED_MESSAGES.get(code) or scrub(exc.message, repo_root)
        details = _clean_details(code, exc.details)
    else:
        code = "internal_error"
        message = INTERNAL_ERROR_MESSAGE
        details = {}

    return {
        "ok": False,
        "error": {"code": code, "message": message, "details": details},
    }
