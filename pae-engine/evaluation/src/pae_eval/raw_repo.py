"""Condition B — generic read-only repository access.

This is the baseline the headline claim rests on, so it is deliberately *not*
weak. A strawman baseline manufactures a win: if Condition B can only do exact
string matching, "PAE beats generic access" measures our choice of baseline
rather than the Engine. Ripgrep is what a real coding agent actually has, so
that is what the baseline gets.

Three tools, no more: search, list, read. Explicitly absent are a shell, Python
execution, the PAE CLI, any PAE import, MCP, a semantic index and a generic
BM25 ranker. The last is a real temptation and is refused on principle — the
moment we build a retrieval system for the baseline, we are tuning the thing we
are measuring against.

Containment is enforced by resolving every path and requiring the result to sit
inside the participant snapshot. It is never enforced by a denylist of things
the model must not read: a denylist is a list of the attacks someone thought
of, and the benchmark's gold labels are exactly what an unlucky glob would
reach.
"""

from __future__ import annotations

import shutil
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Sequence

from .constants import RAW_REPO_LIMITS
from .errors import UsageError
from .providers.base import ToolSpec

RG_MISSING_MESSAGE = (
    "ripgrep (rg) was not found on PATH. Condition B is defined as "
    "ripgrep-backed search; substituting a different search implementation "
    "would change what the baseline is and invalidate the comparison. "
    "Install ripgrep or exclude condition B from the plan."
)


# --------------------------------------------------------------------------
# path containment
# --------------------------------------------------------------------------


def _reject_reason(raw: str) -> str | None:
    """Why ``raw`` is not an acceptable relative path, or ``None`` if it is.

    Checked before touching the filesystem, and checked textually because the
    dangerous forms are platform-dependent: ``C:/x`` is absolute on Windows and
    merely a funny relative path on POSIX, so ``Path.is_absolute()`` alone
    would let a drive-qualified path through on Linux and give a false sense of
    coverage in tests.
    """
    if raw is None or not isinstance(raw, str) or not raw.strip():
        return "path must be a non-empty string"
    if "\x00" in raw:
        return "path contains a NUL byte"
    normalized = raw.replace("\\", "/")
    # UNC is checked before the absolute-path rule: a UNC path also starts with
    # a separator, so the general rule would shadow it and the specific branch
    # would be unreachable — correct behaviour with a misleading message.
    if normalized.startswith("//"):
        return "UNC paths are not permitted"
    if normalized.startswith("/"):
        return "absolute paths are not permitted"
    if raw.startswith("~"):
        return "home-relative paths are not permitted"
    head = normalized.split("/", 1)[0]
    if len(head) >= 2 and head[1] == ":":
        return "drive-qualified paths are not permitted"
    if any(part == ".." for part in normalized.split("/")):
        return "parent-directory traversal is not permitted"
    return None


def resolve_within(root: Path, raw: str) -> Path:
    """Resolve ``raw`` under ``root``, refusing anything that escapes.

    Resolution follows symlinks deliberately: the question is not what the path
    looks like but what it ends up pointing at.
    """
    reason = _reject_reason(raw)
    if reason:
        raise UsageError(f"{reason}: {raw!r}")

    root = Path(root).resolve()
    relative = PurePosixPath(raw.replace("\\", "/"))
    candidate = root.joinpath(*relative.parts)
    resolved = candidate.resolve()
    if resolved != root and root not in resolved.parents:
        raise UsageError(f"path escapes the participant root: {raw!r}")
    return resolved


# --------------------------------------------------------------------------
# tool results
# --------------------------------------------------------------------------


@dataclass
class ToolOutcome:
    """What a tool returned, plus what it touched."""

    status: str  # "ok" | "error"
    content: str
    bytes_returned: int
    latency_ms: float
    paths: tuple[str, ...] = ()
    matches: int = 0
    truncated: bool = False

    @property
    def is_error(self) -> bool:
        return self.status != "ok"


@dataclass
class RawRepoLog:
    """Per-task observability (spec §36). Counts calls; never rewards them."""

    calls: list[dict[str, Any]] = field(default_factory=list)

    def record(self, tool: str, arguments: Mapping[str, Any], outcome: ToolOutcome) -> None:
        self.calls.append({
            "tool": tool,
            "arguments": dict(arguments),
            "status": outcome.status,
            "paths": list(outcome.paths),
            "matches": outcome.matches,
            "bytes": outcome.bytes_returned,
            "latency_ms": round(outcome.latency_ms, 2),
            "truncated": outcome.truncated,
        })

    def summary(self) -> dict[str, Any]:
        searched: set[str] = set()
        read: set[str] = set()
        for call in self.calls:
            target = read if call["tool"] == "repo_read" else searched
            target.update(call["paths"])
        return {
            "search_calls": sum(1 for c in self.calls if c["tool"] == "repo_search"),
            "list_calls": sum(1 for c in self.calls if c["tool"] == "repo_list"),
            "read_calls": sum(1 for c in self.calls if c["tool"] == "repo_read"),
            "error_calls": sum(1 for c in self.calls if c["status"] != "ok"),
            "files_searched": len(searched),
            "files_read": len(read),
            "unique_paths": len(searched | read),
            "total_tool_bytes": sum(c["bytes"] for c in self.calls),
            "search_queries": [
                c["arguments"].get("pattern")
                for c in self.calls
                if c["tool"] == "repo_search"
            ],
        }


# --------------------------------------------------------------------------
# ripgrep
# --------------------------------------------------------------------------


def find_ripgrep() -> str | None:
    return shutil.which("rg")


def ripgrep_version(executable: str | None = None) -> str | None:
    exe = executable or find_ripgrep()
    if not exe:
        return None
    try:
        out = subprocess.run([exe, "--version"], capture_output=True, text=True,
                             check=False, timeout=30)
    except (OSError, subprocess.SubprocessError):  # pragma: no cover
        return None
    first = (out.stdout or "").splitlines()
    return first[0].strip() if first else None


# --------------------------------------------------------------------------
# the tools
# --------------------------------------------------------------------------

TOOL_SPECS: tuple[ToolSpec, ...] = (
    ToolSpec(
        name="repo_search",
        description=(
            "Search the repository's file contents for a regular expression and "
            "return matching lines with their file paths and line numbers. Use "
            "this to locate material when you do not already know which file "
            "holds it."
        ),
        input_schema={
            "type": "object",
            "properties": {
                "pattern": {"type": "string", "minLength": 1, "maxLength": 500,
                            "description": "Regular expression to search for."},
                "glob": {"type": "string", "maxLength": 200,
                         "description": "Optional path glob, e.g. '*.md', to restrict the search."},
                "case_sensitive": {"type": "boolean", "default": False},
                "max_results": {"type": "integer", "minimum": 1,
                                "maximum": RAW_REPO_LIMITS["search_max_matches"],
                                "default": 50},
            },
            "required": ["pattern"],
            "additionalProperties": False,
        },
    ),
    ToolSpec(
        name="repo_list",
        description=(
            "List repository file paths matching a glob, e.g. 'domain-*/**/*.md'. "
            "Use this to discover what exists before reading."
        ),
        input_schema={
            "type": "object",
            "properties": {
                "glob": {"type": "string", "minLength": 1, "maxLength": 200},
                "max_results": {"type": "integer", "minimum": 1,
                                "maximum": RAW_REPO_LIMITS["list_max_paths"],
                                "default": 200},
            },
            "required": ["glob"],
            "additionalProperties": False,
        },
    ),
    ToolSpec(
        name="repo_read",
        description=(
            "Read a UTF-8 text file from the repository by its relative path. "
            "Optionally start at a line offset and limit the number of lines."
        ),
        input_schema={
            "type": "object",
            "properties": {
                "path": {"type": "string", "minLength": 1, "maxLength": 4096},
                "offset": {"type": "integer", "minimum": 0, "default": 0,
                           "description": "Zero-based first line to return."},
                "limit": {"type": "integer", "minimum": 1,
                          "maximum": RAW_REPO_LIMITS["read_default_max_lines"],
                          "default": RAW_REPO_LIMITS["read_default_max_lines"]},
            },
            "required": ["path"],
            "additionalProperties": False,
        },
    ),
)

TOOL_NAMES = tuple(spec.name for spec in TOOL_SPECS)


class RawRepoTools:
    """The three generic tools, rooted at one participant snapshot."""

    def __init__(
        self,
        root: Path,
        *,
        files: Sequence[str] | None = None,
        limits: Mapping[str, int] | None = None,
        ripgrep: str | None = None,
        require_ripgrep: bool = True,
    ) -> None:
        self.root = Path(root).resolve()
        if not self.root.is_dir():
            raise UsageError(f"participant root is not a directory: {self.root}")
        self.limits = {**RAW_REPO_LIMITS, **(limits or {})}
        self._files = tuple(sorted(files)) if files is not None else None
        self._rg = ripgrep or find_ripgrep()
        if require_ripgrep and not self._rg:
            raise UsageError(RG_MISSING_MESSAGE)
        self.log = RawRepoLog()

    # -- metadata ----------------------------------------------------------

    @property
    def ripgrep_version(self) -> str | None:
        return ripgrep_version(self._rg)

    def describe(self) -> Mapping[str, Any]:
        return {
            "tools": list(TOOL_NAMES),
            "ripgrep_version": self.ripgrep_version,
            "limits": dict(self.limits),
            "root_is_snapshot": True,
        }

    # -- dispatch ----------------------------------------------------------

    def call(self, name: str, arguments: Mapping[str, Any]) -> ToolOutcome:
        started = time.perf_counter()
        try:
            if name == "repo_search":
                outcome = self._search(**dict(arguments))
            elif name == "repo_list":
                outcome = self._list(**dict(arguments))
            elif name == "repo_read":
                outcome = self._read(**dict(arguments))
            else:
                outcome = ToolOutcome("error", f"unknown tool: {name}", 0, 0.0)
        except UsageError as exc:
            outcome = ToolOutcome("error", f"error: {exc}", 0, 0.0)
        except TypeError as exc:  # wrong/extra arguments from the model
            outcome = ToolOutcome("error", f"error: invalid arguments — {exc}", 0, 0.0)
        outcome.latency_ms = (time.perf_counter() - started) * 1000.0
        outcome.bytes_returned = len(outcome.content.encode("utf-8"))
        self.log.record(name, arguments, outcome)
        return outcome

    # -- implementations ---------------------------------------------------

    def _known_files(self) -> tuple[str, ...]:
        if self._files is not None:
            return self._files
        found: list[str] = []
        for path in self.root.rglob("*"):
            if path.is_file():
                found.append(path.relative_to(self.root).as_posix())
        self._files = tuple(sorted(found))
        return self._files

    def _search(self, pattern: str, glob: str | None = None,
                case_sensitive: bool = False,
                max_results: int | None = None) -> ToolOutcome:
        if not isinstance(pattern, str) or not pattern:
            raise UsageError("pattern must be a non-empty string")
        cap = min(int(max_results or 50), self.limits["search_max_matches"])

        argv = [
            self._rg, "--line-number", "--with-filename", "--no-heading",
            "--color", "never",
            # No --follow: a symlink out of the snapshot is exactly the escape
            # this condition must not have.
            "--max-count", str(cap),
            "--max-columns", str(self.limits["search_max_line_chars"]),
            "--max-columns-preview",
            "--case-sensitive" if case_sensitive else "--ignore-case",
        ]
        if glob:
            if "\x00" in glob:
                raise UsageError("glob contains a NUL byte")
            argv += ["--glob", glob]
        argv += ["--regexp", pattern, "."]

        try:
            proc = subprocess.run(
                argv, cwd=self.root, capture_output=True, text=True,
                encoding="utf-8", errors="replace", check=False, timeout=60,
            )
        except subprocess.TimeoutExpired:
            return ToolOutcome("error", "error: search timed out", 0, 0.0)
        except OSError as exc:  # pragma: no cover
            return ToolOutcome("error", f"error: search failed — {exc}", 0, 0.0)

        # rg exits 1 for "no matches", which is a result, not a failure.
        if proc.returncode not in (0, 1):
            detail = (proc.stderr or "").strip().splitlines()
            return ToolOutcome(
                "error", f"error: search failed — {detail[0] if detail else 'unknown'}",
                0, 0.0,
            )

        lines = [ln for ln in (proc.stdout or "").splitlines() if ln.strip()]
        truncated = len(lines) > cap
        lines = lines[:cap]
        paths = {ln.split(":", 1)[0].lstrip("./") for ln in lines if ":" in ln}

        body = "\n".join(lines) if lines else "(no matches)"
        body, clipped = _clip(body, self.limits["search_max_result_bytes"])
        return ToolOutcome(
            "ok", body, 0, 0.0,
            paths=tuple(sorted(paths)), matches=len(lines),
            truncated=truncated or clipped,
        )

    def _list(self, glob: str, max_results: int | None = None) -> ToolOutcome:
        if not isinstance(glob, str) or not glob:
            raise UsageError("glob must be a non-empty string")
        if "\x00" in glob:
            raise UsageError("glob contains a NUL byte")
        cap = min(int(max_results or 200), self.limits["list_max_paths"])

        pattern = PurePosixPath(glob.replace("\\", "/"))
        matched = [p for p in self._known_files() if PurePosixPath(p).match(str(pattern))]
        if not matched and "/" not in glob and "**" not in glob:
            # A bare '*.md' is almost always meant recursively; matching only
            # the repository root would be a confusing empty answer.
            matched = [p for p in self._known_files()
                       if PurePosixPath(p).match(f"**/{pattern}")]

        truncated = len(matched) > cap
        body = "\n".join(matched[:cap]) if matched else "(no matching paths)"
        body, clipped = _clip(body, self.limits["list_max_result_bytes"])
        return ToolOutcome(
            "ok", body, 0, 0.0,
            paths=tuple(matched[:cap]), matches=len(matched),
            truncated=truncated or clipped,
        )

    def _read(self, path: str, offset: int = 0, limit: int | None = None) -> ToolOutcome:
        resolved = resolve_within(self.root, path)
        if not resolved.exists():
            raise UsageError(f"no such file: {path}")
        if not resolved.is_file():
            raise UsageError(f"not a regular file: {path}")

        max_lines = min(
            int(limit or self.limits["read_default_max_lines"]),
            self.limits["read_default_max_lines"],
        )
        start = max(0, int(offset or 0))

        try:
            text = resolved.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:  # pragma: no cover
            raise UsageError(f"could not read {path}: {exc}") from exc

        lines = text.splitlines()
        window = lines[start:start + max_lines]
        truncated = (start + max_lines) < len(lines)
        body = "\n".join(window)
        body, clipped = _clip(body, self.limits["read_max_result_bytes"])
        if truncated or clipped:
            body += (
                f"\n\n[truncated: showed lines {start}-{start + len(window)} "
                f"of {len(lines)}]"
            )
        return ToolOutcome(
            "ok", body, 0, 0.0,
            paths=(resolved.relative_to(self.root).as_posix(),),
            matches=len(window), truncated=truncated or clipped,
        )


def _clip(text: str, max_bytes: int) -> tuple[str, bool]:
    """Trim to a byte budget without splitting a character."""
    encoded = text.encode("utf-8")
    if len(encoded) <= max_bytes:
        return text, False
    return encoded[:max_bytes].decode("utf-8", "ignore"), True
