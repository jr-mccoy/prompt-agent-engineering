"""Typed errors and the process exit codes they map to.

Every failure an agent can hit is a distinct type carrying machine-readable
detail, because the distinctions matter operationally:

* an unknown reference is not a malformed reference;
* a withheld resource is not a nonexistent one;
* a resource with no body is not a withheld one;
* an incompatible registry is not a missing repository;
* an integrity mismatch is not a policy refusal.

Collapsing any of those into a generic error would force a caller to parse
prose to decide what to do next.
"""

from __future__ import annotations

from typing import Any

__all__ = [
    "PaeError",
    "UsageError",
    "MalformedReference",
    "RepositoryNotFound",
    "ResourceNotFound",
    "AccessRefused",
    "ContentRefused",
    "ResourceExcluded",
    "NoAddressableContent",
    "SourceIntegrityError",
    "PathSecurityError",
    "SourceUnavailable",
    "SourceTooLarge",
    "ChecksumMismatch",
    "ContentEncodingError",
    "IncompatibleRegistry",
    "RegistryValidationError",
    "EXIT_OK",
]

#: Success. Defined here so the CLI never spells a bare 0.
EXIT_OK = 0


class PaeError(Exception):
    """Base class. Unhandled engine faults surface as exit 1."""

    exit_code: int = 1
    error: str = "internal_error"

    def __init__(self, message: str, **details: Any) -> None:
        super().__init__(message)
        self.message = message
        #: Extra machine-readable fields merged into the JSON error object.
        self.details: dict[str, Any] = {k: v for k, v in details.items() if v is not None}

    def to_json_obj(self) -> dict[str, Any]:
        obj: dict[str, Any] = {
            "error": self.error,
            "exit_code": self.exit_code,
            "message": self.message,
        }
        obj.update(self.details)
        return obj


class UsageError(PaeError):
    """The command or its arguments do not form a valid request."""

    exit_code = 2
    error = "usage_error"


class MalformedReference(UsageError):
    """The reference does not satisfy the UID or public-ID grammar.

    Deliberately not ``ResourceNotFound``: "you typed something that cannot
    name a resource" and "nothing carries that name" are different problems
    with different fixes.
    """

    exit_code = 2
    error = "malformed_reference"


class RepositoryNotFound(PaeError):
    """No PAE checkout was found, or an explicit path holds no registry."""

    exit_code = 3
    error = "repository_not_found"


class ResourceNotFound(PaeError):
    """A well-formed reference that no record claims."""

    exit_code = 4
    error = "resource_not_found"


class AccessRefused(PaeError):
    """Serving policy withholds what was asked for."""

    exit_code = 5
    error = "access_refused"


class ContentRefused(AccessRefused):
    """Metadata is available; the body is not."""

    exit_code = 5
    error = "content_refused"


class ResourceExcluded(AccessRefused):
    """The resource is excluded from serving entirely.

    The exception still carries an identity stub, so an excluded resource stays
    distinguishable from one that does not exist — without leaking its title,
    description, native metadata or body.
    """

    exit_code = 5
    error = "resource_excluded"


class NoAddressableContent(PaeError):
    """The resource is real but has no independently addressable body.

    Techniques are defined inside the master technique index rather than by a
    file of their own; a tombstone's body no longer exists at all.
    """

    exit_code = 6
    error = "no_addressable_content"


class SourceIntegrityError(PaeError):
    """The stored source could not be read and trusted."""

    exit_code = 7
    error = "source_integrity_error"


class PathSecurityError(SourceIntegrityError):
    """A stored path escaped, or tried to escape, the repository root."""

    exit_code = 7
    error = "source_path_refused"


class SourceUnavailable(SourceIntegrityError):
    """The source file is missing, unreadable or not a regular file."""

    exit_code = 7
    error = "source_unavailable"


class SourceTooLarge(SourceIntegrityError):
    """The source exceeds the content ceiling."""

    exit_code = 7
    error = "source_too_large"


class ChecksumMismatch(SourceIntegrityError):
    """The file on disk is not the file the registry recorded."""

    exit_code = 7
    error = "checksum_mismatch"


class ContentEncodingError(SourceIntegrityError):
    """Verified bytes that are not valid UTF-8, requested as text."""

    exit_code = 7
    error = "content_encoding_error"


class IncompatibleRegistry(PaeError):
    """The registry declares a schema this Engine does not implement.

    Never reported as "repository not found": the checkout is right, the
    contract is wrong, and best-effort parsing of an unknown schema would be a
    silent correctness hazard.
    """

    exit_code = 8
    error = "incompatible_registry"


class RegistryValidationError(PaeError):
    """The registry violates a consumer trust assumption at runtime."""

    exit_code = 9
    error = "registry_validation_failed"
