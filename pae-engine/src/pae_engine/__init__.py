"""PAE Engine — a read-only runtime for the PAE Registry.

The Engine binds to a local PAE checkout, resolves resource identity, returns
normalized metadata, and serves whole verified bodies where policy allows. It
never writes, never executes, never reaches the network, and treats every
resource body as data rather than as instructions.

Quickstart::

    from pae_engine import Repository

    registry = Repository.discover().registry()
    record = registry.get("technique:ST-01")
    body = registry.content(record.id).text()

Deterministic lexical search and task routing are available too::

    from pae_engine import Router, SearchEngine

    search = SearchEngine(registry)
    results = search.search("android security audit")
    decision = Router(search).route("review my terraform setup")

Both read registry metadata only; neither ever calls ``Registry.content()``.

Context compilation and MCP are later phases and are deliberately absent.
"""

from __future__ import annotations

from ._version import __version__
from .errors import (
    AccessRefused,
    ChecksumMismatch,
    ContentEncodingError,
    ContentRefused,
    IncompatibleRegistry,
    MalformedReference,
    NoAddressableContent,
    PaeError,
    PathSecurityError,
    RegistryValidationError,
    RepositoryNotFound,
    ResourceExcluded,
    ResourceNotFound,
    SourceIntegrityError,
    SourceTooLarge,
    SourceUnavailable,
    UsageError,
)
from .models import (
    RECORD_SCHEMA,
    ROUTE_STATUSES,
    SERVING_POLICIES,
    SUMMARY_SCHEMA,
    Content,
    Record,
    Resolution,
    RouteCandidate,
    RouteDecision,
    SearchHit,
    SearchResults,
    Summary,
)
from .registry import MAX_CONTENT_BYTES, PUBLIC_ID_PATTERN, UID_PATTERN, Registry, classify_ref
from .repository import REPO_ENV_VAR, Repository
from .routing import COVERAGE_THRESHOLD, MARGIN_THRESHOLD, Router
from .search import KINDS, SearchEngine
from .validate import Issue, ValidationReport, validate_registry

__all__ = [
    "__version__",
    # runtime
    "Repository",
    "Registry",
    "REPO_ENV_VAR",
    # search and routing
    "SearchEngine",
    "Router",
    "KINDS",
    "COVERAGE_THRESHOLD",
    "MARGIN_THRESHOLD",
    # models
    "Record",
    "Resolution",
    "Content",
    "Summary",
    "SearchHit",
    "SearchResults",
    "RouteCandidate",
    "RouteDecision",
    "ROUTE_STATUSES",
    "RECORD_SCHEMA",
    "SUMMARY_SCHEMA",
    "SERVING_POLICIES",
    "MAX_CONTENT_BYTES",
    "UID_PATTERN",
    "PUBLIC_ID_PATTERN",
    "classify_ref",
    # validation
    "validate_registry",
    "ValidationReport",
    "Issue",
    # errors
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
]
