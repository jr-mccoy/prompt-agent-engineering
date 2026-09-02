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

Context compilation assembles whole verified bodies into a budgeted bundle::

    from pae_engine import Budget, ContextCompiler

    compiler = ContextCompiler(registry)
    bundle = compiler.compile_route(decision, budget=Budget(estimated_tokens=8000))
    print(bundle.render_markdown())

An optional MCP server adapter ships in the ``mcp`` extra and is exposed
only through ``pae mcp``. It is never imported from here: importing this
package must stay dependency-free.
"""

from __future__ import annotations

from ._version import __version__
from .context import (
    DEFAULT_MAX_RESOURCES,
    LOW_TOKEN_BUDGET_THRESHOLD,
    MAX_BUNDLE_BYTES,
    ApproximateTokenCounterV1,
    Budget,
    ContextCompiler,
    TokenCounter,
)
from .errors import (
    AccessRefused,
    BudgetTooSmall,
    ChecksumMismatch,
    ContentEncodingError,
    ContentRefused,
    IncompatibleRegistry,
    InvalidBudget,
    MalformedReference,
    MissingExtra,
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
    BUNDLE_SCHEMA,
    MARKDOWN_RENDERER,
    OMISSION_REASONS,
    ORDERINGS,
    RECORD_SCHEMA,
    ROUTE_STATUSES,
    SERVING_POLICIES,
    SOURCE_MODES,
    SUMMARY_SCHEMA,
    BudgetReport,
    BundleItem,
    Content,
    ContextBundle,
    OmittedItem,
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
    # context compilation
    "ContextCompiler",
    "Budget",
    "TokenCounter",
    "ApproximateTokenCounterV1",
    "MAX_BUNDLE_BYTES",
    "DEFAULT_MAX_RESOURCES",
    "LOW_TOKEN_BUDGET_THRESHOLD",
    "ContextBundle",
    "BundleItem",
    "OmittedItem",
    "BudgetReport",
    "BUNDLE_SCHEMA",
    "MARKDOWN_RENDERER",
    "OMISSION_REASONS",
    "ORDERINGS",
    "SOURCE_MODES",
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
    "MissingExtra",
    "InvalidBudget",
    "BudgetTooSmall",
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
