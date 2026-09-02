"""The participant snapshot.

Conditions B, C and D must all see *the same product bytes*, and none of them
may see the evaluation infrastructure. Once `pae-engine/evaluation/` is
committed, pointing a raw-repository agent at the developer checkout would let
it read the condition definitions, the participant prompt, the judge logic and
the fixtures — contaminating Condition B even though the gold benchmark lives
outside the repository entirely (spec §15).

So a sealed run never binds to the working tree. It binds to a snapshot
extracted from Git objects at an explicit commit, with the evaluation tree
excluded and uncommitted files structurally unable to enter.

Reading from Git objects rather than copying the working tree buys three
things: a dirty file cannot leak in, the bytes are exactly what the commit
says, and the result is reproducible from `(commit, exclusions)` alone. The
manifest records a digest per file plus one aggregate digest, and contains no
absolute paths — a snapshot built in two different directories must hash the
same or the hash is measuring the wrong thing.
"""

from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping, Sequence

from . import canonical
from .constants import SNAPSHOT_EXCLUDED_PREFIXES, SNAPSHOT_SCHEMA
from .errors import IsolationError, UsageError

#: Git modes we accept in a snapshot. Symlinks (120000) and submodules
#: (160000) are refused rather than guessed at: a symlink is an aliasing
#: primitive and this is a containment boundary.
MODE_BLOB = "100644"
MODE_EXEC = "100755"
ACCEPTED_MODES = frozenset({MODE_BLOB, MODE_EXEC})
MODE_SYMLINK = "120000"
MODE_GITLINK = "160000"


@dataclass(frozen=True)
class SnapshotFile:
    path: str  # POSIX, relative to the snapshot root
    sha256: str
    size: int
    executable: bool


@dataclass(frozen=True)
class Snapshot:
    root: Path
    commit: str
    files: tuple[SnapshotFile, ...]
    excluded_prefixes: tuple[str, ...]
    excluded_count: int
    aggregate_sha256: str
    refused: tuple[str, ...] = ()

    @property
    def file_count(self) -> int:
        return len(self.files)

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "schema_version": SNAPSHOT_SCHEMA,
            "source_commit": self.commit,
            "included_file_count": self.file_count,
            "excluded_infrastructure_prefixes": list(self.excluded_prefixes),
            "excluded_file_count": self.excluded_count,
            "refused_entries": list(self.refused),
            "aggregate_sha256": self.aggregate_sha256,
            "files": [
                {
                    "path": f.path,
                    "sha256": f.sha256,
                    "size": f.size,
                    "executable": f.executable,
                }
                for f in self.files
            ],
        }


def _git(repo: Path, *args: str, binary: bool = False) -> Any:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise UsageError(
            f"git {' '.join(args)} failed in {repo}: "
            f"{result.stderr.decode('utf-8', 'replace').strip()}"
        )
    return result.stdout if binary else result.stdout.decode("utf-8")


def resolve_commit(repo: Path, rev: str = "HEAD") -> str:
    return _git(repo, "rev-parse", rev).strip()


def is_dirty(repo: Path) -> bool:
    return bool(_git(repo, "status", "--porcelain").strip())


def is_excluded(path: str, prefixes: Sequence[str]) -> bool:
    return any(path == p.rstrip("/") or path.startswith(p) for p in prefixes)


def _list_tree(repo: Path, commit: str) -> list[tuple[str, str, str]]:
    """(mode, object_sha, path) for every entry in the commit's tree."""
    raw = _git(repo, "ls-tree", "-r", "-z", "--full-tree", commit)
    entries: list[tuple[str, str, str]] = []
    for record in raw.split("\0"):
        if not record:
            continue
        meta, _, path = record.partition("\t")
        parts = meta.split()
        if len(parts) < 3:
            continue
        entries.append((parts[0], parts[2], path))
    return entries


def _read_blobs(repo: Path, shas: Sequence[str]) -> dict[str, bytes]:
    """Bulk-read blobs through a single ``git cat-file --batch``.

    7,000+ individual ``git show`` calls would dominate snapshot time; one
    batched process reads the whole tree in a fraction of a second.
    """
    if not shas:
        return {}
    unique = sorted(set(shas))
    proc = subprocess.run(
        ["git", "-C", str(repo), "cat-file", "--batch"],
        input=("\n".join(unique) + "\n").encode("ascii"),
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise UsageError(
            "git cat-file --batch failed: "
            f"{proc.stderr.decode('utf-8', 'replace').strip()}"
        )

    out = proc.stdout
    blobs: dict[str, bytes] = {}
    offset = 0
    for _ in unique:
        newline = out.find(b"\n", offset)
        if newline < 0:
            break
        header = out[offset:newline].decode("ascii", "replace").split()
        if len(header) != 3:
            raise UsageError(f"unexpected cat-file header: {header!r}")
        sha, _kind, size_text = header
        size = int(size_text)
        start = newline + 1
        blobs[sha] = out[start:start + size]
        offset = start + size + 1  # trailing newline after the payload
    return blobs


def build_snapshot(
    repo: Path,
    dest: Path,
    *,
    commit: str = "HEAD",
    excluded_prefixes: Iterable[str] = SNAPSHOT_EXCLUDED_PREFIXES,
    require_clean: bool = False,
) -> Snapshot:
    """Materialize the product tree at ``commit`` into ``dest``.

    ``dest`` must be empty or absent. ``require_clean`` is for sealed runs: the
    extraction itself cannot pick up dirty files, but a dirty checkout means
    the operator's intent and the commit have diverged, and a sealed run should
    say so rather than quietly evaluate something the developer is not looking
    at (spec §74).
    """
    repo = Path(repo).resolve()
    dest = Path(dest).resolve()
    prefixes = tuple(excluded_prefixes)

    if require_clean and is_dirty(repo):
        raise IsolationError(
            f"refusing to build a sealed snapshot from a dirty checkout at {repo}; "
            "commit or stash first, or run in development mode"
        )
    if dest.exists() and any(dest.iterdir()):
        raise UsageError(f"snapshot destination is not empty: {dest}")

    resolved = resolve_commit(repo, commit)
    entries = _list_tree(repo, resolved)

    refused: list[str] = []
    keep: list[tuple[str, str, str]] = []
    excluded_count = 0
    for mode, sha, path in entries:
        if is_excluded(path, prefixes):
            excluded_count += 1
            continue
        if mode in (MODE_SYMLINK, MODE_GITLINK):
            # Neither can be reproduced safely inside a containment boundary.
            refused.append(f"{path} (mode {mode})")
            continue
        if mode not in ACCEPTED_MODES:
            refused.append(f"{path} (unsupported mode {mode})")
            continue
        keep.append((mode, sha, path))

    blobs = _read_blobs(repo, [sha for _m, sha, _p in keep])

    files: list[SnapshotFile] = []
    dest.mkdir(parents=True, exist_ok=True)
    for mode, sha, path in keep:
        data = blobs.get(sha)
        if data is None:
            raise UsageError(f"git object missing for {path} ({sha})")
        # PurePosixPath guarantees the tree path is interpreted the same way on
        # every platform; joining a raw string would let a backslash in a path
        # mean something different on Windows.
        relative = PurePosixPath(path)
        if relative.is_absolute() or ".." in relative.parts:
            raise IsolationError(f"refusing suspicious tree path: {path}")
        target = dest.joinpath(*relative.parts)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        if mode == MODE_EXEC:
            try:
                target.chmod(target.stat().st_mode | 0o111)
            except OSError:  # pragma: no cover - Windows has no exec bit
                pass
        files.append(SnapshotFile(
            path=path,
            sha256=canonical.sha256_bytes(data),
            size=len(data),
            executable=mode == MODE_EXEC,
        ))

    files.sort(key=lambda f: f.path)
    # The aggregate covers path + content only. No absolute path, no mtime, no
    # build host: a snapshot of the same commit must hash identically wherever
    # it is built (spec §16).
    aggregate = canonical.sha256_obj(
        {"commit": resolved, "files": [[f.path, f.sha256] for f in files]}
    )

    return Snapshot(
        root=dest,
        commit=resolved,
        files=tuple(files),
        excluded_prefixes=prefixes,
        excluded_count=excluded_count,
        aggregate_sha256=aggregate,
        refused=tuple(refused),
    )


def write_manifest(snapshot: Snapshot, path: Path) -> str:
    """Write ``participant-snapshot.json`` and return its digest."""
    return canonical.write_canonical(path, snapshot.to_json_obj())


# --------------------------------------------------------------------------
# equivalence and isolation checks (spec §17)
# --------------------------------------------------------------------------


def assert_no_evaluation_infrastructure(snapshot: Snapshot) -> None:
    """The snapshot must not contain the harness that is grading it."""
    leaked = [
        f.path for f in snapshot.files
        if is_excluded(f.path, SNAPSHOT_EXCLUDED_PREFIXES)
        or f.path.startswith("pae-engine/evaluation")
        or "/pae_eval/" in f.path
        or f.path.endswith("/pae_eval")
    ]
    if leaked:
        raise IsolationError(
            "participant snapshot contains evaluation infrastructure: "
            + ", ".join(sorted(leaked)[:10])
        )


def assert_product_present(snapshot: Snapshot) -> None:
    """The snapshot must still be a usable PAE checkout.

    Excluding too much is as wrong as excluding too little: a snapshot without
    the registry is not the product, and every condition would be measuring an
    empty repository.
    """
    paths = {f.path for f in snapshot.files}
    required = [
        "meta/registry/registry.jsonl",
        "meta/registry/identity.tsv",
        "pae-engine/src/pae_engine/__init__.py",
        "CLAUDE.md",
    ]
    missing = [p for p in required if p not in paths]
    if missing:
        raise IsolationError(
            "participant snapshot is missing product files it must contain: "
            + ", ".join(missing)
        )
    if not any(p.startswith("domain-") for p in paths):
        raise IsolationError("participant snapshot contains no corpus domains")


def assert_benchmark_outside(benchmark_root: Path, *forbidden: Path) -> None:
    """The benchmark must not live inside anything the participant can read.

    Containment is checked by resolving both paths — which follows symlinks —
    rather than by comparing strings, so a symlinked benchmark directory cannot
    alias its way inside (spec §13).
    """
    benchmark = Path(benchmark_root).resolve()
    for other in forbidden:
        if other is None:
            continue
        root = Path(other).resolve()
        if benchmark == root or root in benchmark.parents:
            raise IsolationError(
                f"benchmark root {benchmark} resolves inside {root}; "
                "a participant with read access there could see gold labels"
            )


def verify_against_commit(
    snapshot: Snapshot, repo: Path, sample: int = 25
) -> list[str]:
    """Re-hash a sample of snapshot files against the source commit.

    Cheap insurance that the extraction is what it claims. Returns the paths
    that disagreed; an empty list is the pass condition.
    """
    if not snapshot.files:
        return []
    step = max(1, len(snapshot.files) // max(1, sample))
    chosen = snapshot.files[::step][:sample]
    blobs = _read_blobs(
        Path(repo),
        [
            sha
            for _m, sha, path in _list_tree(Path(repo), snapshot.commit)
            if path in {f.path for f in chosen}
        ],
    )
    by_digest = {canonical.sha256_bytes(data) for data in blobs.values()}
    return [f.path for f in chosen if f.sha256 not in by_digest]


def snapshot_env(snapshot: Snapshot) -> Mapping[str, str]:
    """Environment for a subprocess bound to the snapshot.

    ``PAE_REPO`` points the Engine at the snapshot. Notably it does *not*
    inherit the developer's environment wholesale: a stray ``PAE_REPO`` from a
    shell would silently redirect a condition at the real checkout.
    """
    env = {k: v for k, v in os.environ.items() if not k.startswith("PAE_")}
    env["PAE_REPO"] = str(snapshot.root)
    return env
