"""Locating the PAE checkout the Engine reads.

The wheel ships no corpus and no registry, so every run must bind to a local
checkout. Discovery is deliberately small and entirely local: an agent that
silently bound to the wrong checkout — or, worse, downloaded one — would
produce confidently wrong answers.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Optional

from .errors import IncompatibleRegistry, RepositoryNotFound, UsageError
from .models import SUMMARY_SCHEMA

__all__ = [
    "Repository",
    "REGISTRY_RELPATH",
    "SUMMARY_RELPATH",
    "REPO_ENV_VAR",
    "DISCOVERY_EXPLICIT",
    "DISCOVERY_ENVIRONMENT",
    "DISCOVERY_ANCESTOR",
]

REGISTRY_RELPATH = "meta/registry/registry.jsonl"
SUMMARY_RELPATH = "meta/registry/registry-summary.json"
REPO_ENV_VAR = "PAE_REPO"

DISCOVERY_EXPLICIT = "explicit"
DISCOVERY_ENVIRONMENT = "environment"
DISCOVERY_ANCESTOR = "ancestor"


def _has_marker(root: Path) -> bool:
    """Both generated registry artifacts present. Either alone is not a root."""
    return (root / REGISTRY_RELPATH).is_file() and (root / SUMMARY_RELPATH).is_file()


def _read_summary(root: Path) -> Mapping[str, Any]:
    """Parse the summary of a directory already known to carry the markers.

    An unparsable or non-object summary here is an incompatible registry, not a
    missing repository: the checkout is a PAE checkout, its contract is one this
    Engine cannot honour.
    """
    path = root / SUMMARY_RELPATH
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise IncompatibleRegistry(
            f"registry summary could not be read: {path}",
            path=str(path),
            reason=str(exc),
        ) from None
    try:
        obj = json.loads(text)
    except json.JSONDecodeError as exc:
        raise IncompatibleRegistry(
            f"registry summary is not valid JSON: {path}",
            path=str(path),
            reason=str(exc),
        ) from None
    if not isinstance(obj, dict):
        raise IncompatibleRegistry(
            f"registry summary is not a JSON object: {path}", path=str(path)
        )
    return obj


def _require_supported(root: Path, summary: Mapping[str, Any]) -> None:
    declared = summary.get("schema")
    if declared != SUMMARY_SCHEMA:
        raise IncompatibleRegistry(
            f"{root} holds a PAE registry declaring schema {declared!r}, which this "
            f"engine does not implement (supported: {SUMMARY_SCHEMA!r})",
            root=str(root),
            declared_schema=declared,
            supported_schema=SUMMARY_SCHEMA,
        )


@dataclass(frozen=True)
class Repository:
    """A resolved PAE checkout."""

    root: Path
    discovery_source: str
    search_start: Optional[Path] = None

    # -- construction ------------------------------------------------------

    @classmethod
    def at(cls, path: os.PathLike[str] | str, *, discovery_source: str = DISCOVERY_EXPLICIT
           ) -> "Repository":
        """Bind to one named directory. Never falls through to another source."""
        if path is None or str(path) == "":
            raise UsageError("repository path is empty")
        root = Path(path).expanduser()
        try:
            root = root.resolve()
        except OSError as exc:  # pragma: no cover - platform dependent
            raise RepositoryNotFound(
                f"repository path could not be resolved: {path}", path=str(path), reason=str(exc)
            ) from None
        if not root.is_dir():
            raise RepositoryNotFound(
                f"repository path is not a directory: {root}",
                path=str(root),
                source=discovery_source,
            )
        if not _has_marker(root):
            raise RepositoryNotFound(
                f"{root} holds no PAE registry (expected {REGISTRY_RELPATH} and "
                f"{SUMMARY_RELPATH})",
                path=str(root),
                source=discovery_source,
                expected=[REGISTRY_RELPATH, SUMMARY_RELPATH],
            )
        _require_supported(root, _read_summary(root))
        return cls(root=root, discovery_source=discovery_source)

    @classmethod
    def discover(
        cls,
        explicit: os.PathLike[str] | str | None = None,
        *,
        env: Mapping[str, str] | None = None,
        cwd: os.PathLike[str] | str | None = None,
    ) -> "Repository":
        """Resolve a checkout by the one precedence the Engine supports.

        1. an explicit path;
        2. ``PAE_REPO``;
        3. the working directory and its ancestors;
        4. failure.

        An explicit source that does not hold a registry is an error, never a
        reason to try the next source. Falling through would let an agent
        believe it had queried the checkout it named.
        """
        if explicit is not None and str(explicit) != "":
            return cls.at(explicit, discovery_source=DISCOVERY_EXPLICIT)

        environ = os.environ if env is None else env
        from_env = environ.get(REPO_ENV_VAR)
        if from_env:
            return cls.at(from_env, discovery_source=DISCOVERY_ENVIRONMENT)

        start = Path(cwd) if cwd is not None else Path.cwd()
        try:
            start = start.resolve()
        except OSError as exc:  # pragma: no cover - platform dependent
            raise RepositoryNotFound(
                f"working directory could not be resolved: {start}", reason=str(exc)
            ) from None

        for candidate in (start, *start.parents):
            if not _has_marker(candidate):
                # Not a PAE root at all. Keep walking.
                continue
            # A PAE root whose contract is unsupported stops the walk. Stepping
            # over it to find a compatible checkout higher up would answer from
            # a repository the caller is not standing in.
            _require_supported(candidate, _read_summary(candidate))
            return cls(
                root=candidate, discovery_source=DISCOVERY_ANCESTOR, search_start=start
            )

        raise RepositoryNotFound(
            f"no PAE repository found in {start} or any ancestor; pass --repo or set "
            f"{REPO_ENV_VAR}",
            search_start=str(start),
            env_var=REPO_ENV_VAR,
        )

    # -- accessors ---------------------------------------------------------

    @property
    def registry_path(self) -> Path:
        return self.root / REGISTRY_RELPATH

    @property
    def summary_path(self) -> Path:
        return self.root / SUMMARY_RELPATH

    def registry(self) -> "Any":
        """Open the registry bound to this checkout. Reads no registry data yet."""
        from .registry import Registry

        return Registry.open(self)

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "root": str(self.root),
            "discovery_source": self.discovery_source,
            "search_start": str(self.search_start) if self.search_start else None,
            "registry": str(self.registry_path),
            "summary": str(self.summary_path),
        }
