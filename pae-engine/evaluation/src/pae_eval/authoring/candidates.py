"""Reviewer candidate discovery, with no PAE retrieval anywhere in it (spec §10).

A reviewer decides which resource *should* have answered a task. If they reach
that decision by asking PAE, the label records what PAE returned and the
benchmark grades PAE against its own opinion. The resulting number would be
unfalsifiable, and it would look exactly like a good result.

So discovery here is deliberately crude and entirely generic:

* ripgrep over the participant snapshot, one fixed-string pass per query token;
* hit counts aggregated per file, ranked by how many distinct tokens matched;
* the Registry consulted **only** to turn a discovered file path into a stable
  identity — UID, kind, scope, title, description — never to rank anything.

``pae_engine.search``, ``pae_engine.routing``, ``pae_engine.context`` and
``pae_engine.mcp`` are not imported, and neither ``SearchEngine``, ``Router``
nor ``ContextCompiler`` is referenced. ``test_authoring_candidates`` proves
that at source level and again over the transitive import closure, because a
comment promising restraint is not a control.

## The ranking is not a relevance judgement

``rank`` is the position in a token-hit ordering and nothing more. Every
emitted record carries ``ranking_basis`` saying so, and the reviewer's form
always offers **none of these** and **search further** — a fixed-length
candidate list with no escape hatch is a forced-choice instrument that
manufactures agreement with whatever the list happened to contain.
"""

from __future__ import annotations

import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..errors import UsageError
from ..raw_repo import find_ripgrep, ripgrep_version

#: Bumped when a change would reorder candidates for a fixed query.
DISCOVERY_ALGORITHM_VERSION = "reviewer-candidate-discovery/1"

#: Stated on every candidate list so its ordering is never quoted as PAE
#: relevance, in a report or anywhere else.
RANKING_BASIS = (
    "raw ripgrep token-hit aggregation over the participant snapshot; "
    "not a PAE relevance score, not a PAE ranking, and not derived from any "
    "PAE Search, Router or ContextCompiler output"
)

#: Options the reviewer always has, whatever the list contains.
REVIEWER_ESCAPE_OPTIONS = ("none of these", "search further")

DEFAULT_MAX_CANDIDATES = 12
DEFAULT_EXCERPT_CHARS = 600

#: Query words carrying no discriminating power. Kept short on purpose: an
#: aggressive stoplist is a retrieval decision, and retrieval decisions are
#: what this module is forbidden to make.
STOPWORDS = frozenset("""
a an and are as at be but by can do does for from get give has have how i in is
it its me my need of on or our should so that the their them then there these
this to use used using want was we what when where which who why will with you
your
""".split())

_TOKEN = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{2,}")
_SEARCHABLE_SUFFIXES = (".md", ".json", ".yaml", ".yml", ".txt")


def query_tokens(query: str, *, stopwords: frozenset[str] = STOPWORDS) -> list[str]:
    """Distinct, lowercased, order-preserving query tokens."""
    out: list[str] = []
    for match in _TOKEN.finditer(query):
        token = match.group(0).casefold()
        if token in stopwords or len(token) < 3:
            continue
        if token not in out:
            out.append(token)
    return out


# --------------------------------------------------------------------------
# identity mapping (Registry read as data, never as a ranker)
# --------------------------------------------------------------------------


def _derive_scope(record: Mapping[str, Any]) -> str:
    kind = str(record.get("kind") or "")
    public_id = str(record.get("id") or "")
    rest = public_id.split(":", 1)[1] if ":" in public_id else public_id
    segments = [s for s in rest.split("/") if s]
    if kind == "technique":
        category = (record.get("native") or {}).get("category") or ""
        if isinstance(category, (list, tuple)):
            category = " ".join(str(c) for c in category)
        category = str(category).strip()
        return category.casefold() or (segments[0].casefold() if segments else "")
    if not segments:
        return ""
    if segments[0] == "agentic-resources" and len(segments) > 1:
        return f"agentic-resources/{segments[1]}".casefold()
    return segments[0].casefold()


@dataclass(frozen=True)
class Identity:
    uid: str
    public_id: str
    kind: str
    scope: str
    title: str
    description: str
    serving_policy: str
    lifecycle: str

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "uid": self.uid,
            "public_id": self.public_id,
            "kind": self.kind,
            "scope": self.scope,
            "title": self.title,
            "description": self.description,
            "serving_policy": self.serving_policy,
            "lifecycle": self.lifecycle,
        }


def load_identity_index(repo: Path) -> dict[str, Identity]:
    """``source path -> Identity``, read straight from the Registry artifact."""
    path = Path(repo) / "meta" / "registry" / "registry.jsonl"
    if not path.is_file():
        raise UsageError(f"registry not found: {path}")
    index: dict[str, Identity] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            source = record.get("source") or {}
            rel = str(source.get("path") or "")
            if not rel:
                continue
            index[rel] = Identity(
                uid=str(record.get("uid") or ""),
                public_id=str(record.get("id") or ""),
                kind=str(record.get("kind") or ""),
                scope=_derive_scope(record),
                title=str(record.get("title") or ""),
                description=str(record.get("description") or ""),
                serving_policy=str(
                    (record.get("serving_policy") or {}).get("value") or ""
                ),
                lifecycle=str(record.get("lifecycle") or ""),
            )
    return index


# --------------------------------------------------------------------------
# discovery
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Candidate:
    rank: int
    path: str
    matched_tokens: tuple[str, ...]
    total_hits: int
    identity: Identity | None
    excerpt: str = ""
    excerpt_withheld_reason: str = ""

    def to_json_obj(self) -> dict[str, Any]:
        obj: dict[str, Any] = {
            "rank": self.rank,
            "path": self.path,
            "matched_tokens": list(self.matched_tokens),
            "distinct_tokens_matched": len(self.matched_tokens),
            "total_hits": self.total_hits,
            "ranking_basis": RANKING_BASIS,
        }
        obj["identity"] = self.identity.to_json_obj() if self.identity else None
        if self.excerpt:
            obj["excerpt"] = self.excerpt
        if self.excerpt_withheld_reason:
            obj["excerpt_withheld_reason"] = self.excerpt_withheld_reason
        return obj


def _rg_count(executable: str, root: Path, token: str,
              timeout: float = 60.0) -> dict[str, int]:
    """``path -> match count`` for one fixed-string, case-insensitive token."""
    command = [
        executable,
        "--count-matches",
        "--fixed-strings",
        "--ignore-case",
        "--no-messages",
        "--hidden",
        "--glob", "!.git/**",
    ]
    for suffix in _SEARCHABLE_SUFFIXES:
        command += ["--glob", f"*{suffix}"]
    command += ["--", token, "."]

    try:
        completed = subprocess.run(
            command, cwd=str(root), capture_output=True, text=True,
            timeout=timeout, check=False,
        )
    except subprocess.TimeoutExpired:
        return {}
    if completed.returncode not in (0, 1):  # 1 == no matches, which is a result
        return {}

    counts: dict[str, int] = {}
    for line in completed.stdout.splitlines():
        path, _, number = line.rpartition(":")
        if not path or not number.isdigit():
            continue
        normalized = path.replace("\\", "/").lstrip("./")
        counts[normalized] = counts.get(normalized, 0) + int(number)
    return counts


def _excerpt(root: Path, rel: str, identity: Identity | None,
             max_chars: int) -> tuple[str, str]:
    """A short opening excerpt, or the reason there is none.

    A safety-gated resource is served whole or not at all — its guards are
    load-bearing and an excerpt would show the reviewer a version of the
    resource with the guards cut off. So those are withheld by policy rather
    than truncated.
    """
    if identity is not None and identity.serving_policy == "safety_gated":
        return "", ("safety_gated: guard text must not be truncated, so no "
                    "excerpt is shown")
    path = Path(root) / rel
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return "", f"unreadable: {exc}"
    body = text.strip()
    if len(body) <= max_chars:
        return body, ""
    return body[:max_chars].rstrip() + " […]", ""


@dataclass(frozen=True)
class DiscoveryResult:
    query: str
    tokens: tuple[str, ...]
    candidates: tuple[Candidate, ...]
    files_considered: int
    ripgrep_version: str
    algorithm_version: str = DISCOVERY_ALGORITHM_VERSION
    unregistered_files_outranked: int = 0
    registered_only: bool = True

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "algorithm_version": self.algorithm_version,
            "query": self.query,
            "query_tokens": list(self.tokens),
            "files_considered": self.files_considered,
            "ripgrep_version": self.ripgrep_version,
            "ranking_basis": RANKING_BASIS,
            "registered_only": self.registered_only,
            "unregistered_files_outranked": self.unregistered_files_outranked,
            "scope_filter_disclosure": (
                "Files with no Registry identity are excluded because the "
                "reviewer's question is which *resource* answers the task, and "
                "an index, README or roadmap is not a resource. This is a scope "
                "filter, not a relevance judgement: the order among the files "
                "shown is unchanged, and the count of excluded higher-ranked "
                "files is reported above rather than hidden."
            ) if self.registered_only else "no scope filter applied",
            "reviewer_options": list(REVIEWER_ESCAPE_OPTIONS),
            "candidates": [c.to_json_obj() for c in self.candidates],
            "pae_retrieval_used": False,
        }


def discover(
    snapshot_root: Path,
    query: str,
    *,
    repo: Path | None = None,
    max_candidates: int = DEFAULT_MAX_CANDIDATES,
    excerpt_chars: int = DEFAULT_EXCERPT_CHARS,
    ripgrep: str | None = None,
    registered_only: bool = True,
) -> DiscoveryResult:
    """Rank snapshot files by raw token hits. No PAE retrieval is involved.

    ``registered_only`` drops files that carry no Registry identity. Raw token
    aggregation puts ``PROMPT_INDEX.md`` and the domain READMEs at the top of
    almost every query — they contain every word in the corpus — and a
    candidate list whose first six entries are indexes is one the reviewer
    cannot use. The filter is on *whether a file is a resource at all*, never
    on how well it matches, the surviving order is untouched, and the number of
    higher-ranked files it removed is reported.
    """
    root = Path(snapshot_root)
    if not root.is_dir():
        raise UsageError(f"snapshot root is not a directory: {root}")

    executable = ripgrep or find_ripgrep()
    if executable is None:
        raise UsageError(
            "ripgrep is not installed; reviewer discovery is defined as ripgrep "
            "over the snapshot and has no fallback ranker by design"
        )

    tokens = query_tokens(query)
    per_file_tokens: dict[str, list[str]] = {}
    per_file_hits: dict[str, int] = {}
    for token in tokens:
        for path, count in _rg_count(executable, root, token).items():
            per_file_tokens.setdefault(path, []).append(token)
            per_file_hits[path] = per_file_hits.get(path, 0) + count

    identities = load_identity_index(Path(repo)) if repo else {}

    ordered = sorted(
        per_file_tokens,
        key=lambda p: (-len(per_file_tokens[p]), -per_file_hits[p], p),
    )

    kept, dropped = [], 0
    for rel in ordered:
        if registered_only and identities and rel not in identities:
            if len(kept) < max_candidates:
                dropped += 1
            continue
        kept.append(rel)
        if len(kept) >= max_candidates:
            break

    candidates: list[Candidate] = []
    for position, rel in enumerate(kept, start=1):
        identity = identities.get(rel)
        excerpt, withheld = _excerpt(root, rel, identity, excerpt_chars)
        candidates.append(Candidate(
            rank=position,
            path=rel,
            matched_tokens=tuple(per_file_tokens[rel]),
            total_hits=per_file_hits[rel],
            identity=identity,
            excerpt=excerpt,
            excerpt_withheld_reason=withheld,
        ))

    return DiscoveryResult(
        query=query,
        tokens=tuple(tokens),
        candidates=tuple(candidates),
        files_considered=len(per_file_tokens),
        ripgrep_version=ripgrep_version(executable) or "unknown",
        unregistered_files_outranked=dropped,
        registered_only=bool(registered_only and identities),
    )
