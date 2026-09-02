"""Author-packet leakage audit (spec §6).

The export is the firewall. Everything upstream — deterministic selection,
sanitization, opaque packet IDs — is a design intention; this module is the
only place that checks the intention survived contact with the files actually
being handed over. It reads the export as bytes, knows the answer key, and
fails closed.

## What is gated at zero, and what is only measured

Gated at exactly zero, because each one hands over identity outright:

``uid`` ``public_id`` ``source_path``
    Literal identifiers. There is no benign reason for one to appear.
``full_title``
    The target's title as a **consecutive token sequence**. That is the spec's
    phrase and it is the right test: a title reproduced in order is the answer
    written out.
``reviewer_map`` ``gold_label`` ``search_router_output``
    Reviewer-side material that must live only in the other export.

Measured and reported, deliberately **not** gated at zero:

``title token overlap`` ``description token overlap``
    A packet about medication review will contain the words "medication" and
    "review", and its title contains them too. Scattered token overlap is a
    consequence of preserving operational content, which spec §5 requires. So
    the audit reports the distribution and flags outliers rather than demanding
    disjointness — a zero-overlap gate here would be satisfiable only by
    destroying the body the author is supposed to write about.

That distinction is the one judgement call in this module and it is made in the
open: a hard gate on the ordered title, a measurement on the bag of words.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from .. import canonical

#: Categories that must be exactly zero for an export to ship.
GATED_CATEGORIES = (
    "uid",
    "public_id",
    "source_path",
    "full_title",
    "reviewer_map",
    "gold_label",
    "search_router_output",
)

#: Substrings that mean reviewer-side mapping material reached the author tree.
REVIEWER_MAP_MARKERS = (
    "reviewer-private",
    "reviewer_private",
    "PAE_REVIEWER_PRIVATE",
    "target_map",
    "target-map",
    "packet_to_target",
    "target_uid",
)

#: Substrings that mean a gold label reached the author tree.
GOLD_LABEL_MARKERS = (
    "acceptable_resource_uids",
    "acceptable_route_statuses",
    "acceptable_scopes",
    "acceptable_kinds",
    "label_rationale",
    "label_provenance",
    "expected_uid",
    "gold_label",
    "gold label",
)

#: Substrings that mean PAE Search, Router or ContextCompiler output reached the
#: author tree. Names of the machinery, not of a task class: ``safety_gated``
#: is an author-visible class name and must not match anything here.
SEARCH_ROUTER_MARKERS = (
    "pae route",
    "pae search",
    "pae_engine",
    "SearchEngine",
    "ContextCompiler",
    "ContextBundle",
    "ROUTING_REFERENCE",
    "route_status",
    "matched_terms",
    "scope_scores",
    "routing_reference",
    "PROMPT_INDEX",
    "registry.jsonl",
)

#: Files the audit reads as text. Anything else is hashed and listed but not
#: searched, and an unexpected binary in an author export is itself a finding.
TEXT_SUFFIXES = (".md", ".txt", ".json", ".jsonl", ".yaml", ".yml", ".csv", ".tsv")

_TOKEN = re.compile(r"[a-z0-9]+")


def tokens(text: str) -> list[str]:
    return _TOKEN.findall(text.casefold())


def token_set(text: str) -> set[str]:
    return set(tokens(text))


def contains_sequence(haystack: Sequence[str], needle: Sequence[str]) -> bool:
    """Whether ``needle`` appears as a consecutive run inside ``haystack``."""
    if not needle or len(needle) > len(haystack):
        return False
    first = needle[0]
    width = len(needle)
    for index, value in enumerate(haystack):
        if value == first and list(haystack[index:index + width]) == list(needle):
            return True
    return False


def containment(subset: set[str], superset: set[str]) -> float:
    if not subset:
        return 0.0
    return len(subset & superset) / len(subset)


# --------------------------------------------------------------------------
# the answer key, in the shape the audit needs
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class TargetIdentity:
    packet_id: str
    uid: str
    public_id: str
    source_path: str
    title: str
    description: str

    @property
    def title_tokens(self) -> list[str]:
        return tokens(self.title)

    @property
    def is_distinctive_title(self) -> bool:
        """Whether the ordered-title gate can mean anything for this target.

        Some agentic resources are titled with a single ordinary word —
        ``issue``, ``debugger``. For those, "the title appears as a consecutive
        token sequence" degenerates into "the English word appears", which
        fires on unrelated packets and cannot be cleared without deleting a
        common word from operational text that spec §5 requires kept.

        A single-word title carries no more identity than the packet's subject
        matter, which the author is *supposed* to see. So the gate applies to
        multi-token titles, and single-token titles are counted and reported
        rather than silently skipped.
        """
        return len(self.title_tokens) >= 2

    @property
    def path_fragments(self) -> tuple[str, ...]:
        """Strings whose presence would give the path away.

        The full path and the bare filename always. The stem only when it is
        actually path-shaped — it contains a separator, or it is long enough to
        be distinctive. A bare stem like ``debugger`` is an ordinary word, and
        gating on it flags every packet that mentions debugging.
        """
        if not self.source_path:
            return ()
        name = self.source_path.rsplit("/", 1)[-1]
        stem = re.sub(r"\.[A-Za-z0-9]+$", "", name)
        out = [self.source_path, name]
        if ("-" in stem or "_" in stem) or len(stem) >= 12:
            out.append(stem)
        return tuple(dict.fromkeys(out))


# --------------------------------------------------------------------------
# findings
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Finding:
    category: str
    file: str
    detail: str
    packet_id: str = ""

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "category": self.category,
            "file": self.file,
            "detail": self.detail,
            "packet_id": self.packet_id,
        }


@dataclass(frozen=True)
class AuditReport:
    root: str
    files_scanned: int
    counts: Mapping[str, int]
    findings: tuple[Finding, ...]
    overlap: Mapping[str, Any]
    file_digests: Mapping[str, str] = field(default_factory=dict)
    problems: tuple[str, ...] = ()

    @property
    def passed(self) -> bool:
        return not self.problems and all(
            self.counts.get(category, 0) == 0 for category in GATED_CATEGORIES
        )

    @property
    def readiness(self) -> str:
        return ("READY FOR INDEPENDENT TASK AUTHORING" if self.passed
                else "NOT READY FOR INDEPENDENT TASK AUTHORING")

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "root": self.root,
            "files_scanned": self.files_scanned,
            "counts": dict(self.counts),
            "gated_categories": list(GATED_CATEGORIES),
            "passed": self.passed,
            "readiness": self.readiness,
            "findings": [f.to_json_obj() for f in self.findings],
            "overlap": dict(self.overlap),
            "problems": list(self.problems),
        }

    def summary_lines(self) -> list[str]:
        label = {
            "uid": "UID leaks",
            "public_id": "public-ID leaks",
            "source_path": "source-path leaks",
            "full_title": "full-title leaks",
            "reviewer_map": "reviewer-map files",
            "gold_label": "gold labels",
            "search_router_output": "Search/Router outputs",
        }
        width = max(len(v) for v in label.values()) + 2
        return [
            f"{label[c] + ':':<{width}}{self.counts.get(c, 0)}"
            for c in GATED_CATEGORIES
        ]


# --------------------------------------------------------------------------
# the audit
# --------------------------------------------------------------------------


def _iter_files(root: Path) -> list[Path]:
    return sorted(p for p in Path(root).rglob("*") if p.is_file())


def audit_export(
    root: Path,
    targets: Sequence[TargetIdentity],
    *,
    forbidden_digests: Mapping[str, str] | None = None,
) -> AuditReport:
    """Scan every file under ``root`` for any trace of ``targets``.

    ``forbidden_digests`` maps a digest to the name of a reviewer-private file;
    a byte-identical copy inside the author tree is caught even if it was
    renamed, which a filename check alone would miss.
    """
    root = Path(root)
    files = _iter_files(root)
    findings: list[Finding] = []
    counts: dict[str, int] = {category: 0 for category in GATED_CATEGORIES}
    problems: list[str] = []
    digests: dict[str, str] = {}

    by_digest = dict(forbidden_digests or {})

    title_overlaps: list[float] = []
    description_overlaps: list[float] = []

    for path in files:
        rel = path.relative_to(root).as_posix()
        digest = canonical.sha256_file(path)
        digests[rel] = digest

        if digest in by_digest:
            findings.append(Finding(
                "reviewer_map", rel,
                f"byte-identical to reviewer-private file {by_digest[digest]!r}",
            ))
            counts["reviewer_map"] += 1

        if path.suffix.lower() not in TEXT_SUFFIXES:
            problems.append(
                f"{rel}: unexpected non-text file in an author export; the audit "
                "cannot read it, so it cannot be cleared"
            )
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            problems.append(f"{rel}: unreadable as UTF-8 text: {exc}")
            continue

        lowered = text.casefold()
        text_tokens = tokens(text)
        text_token_set = set(text_tokens)

        for marker in REVIEWER_MAP_MARKERS:
            if marker.casefold() in lowered:
                findings.append(Finding("reviewer_map", rel,
                                        f"reviewer-mapping marker {marker!r}"))
                counts["reviewer_map"] += 1
        for marker in GOLD_LABEL_MARKERS:
            if marker.casefold() in lowered:
                findings.append(Finding("gold_label", rel,
                                        f"gold-label marker {marker!r}"))
                counts["gold_label"] += 1
        for marker in SEARCH_ROUTER_MARKERS:
            if marker.casefold() in lowered:
                findings.append(Finding("search_router_output", rel,
                                        f"PAE output marker {marker!r}"))
                counts["search_router_output"] += 1

        for target in targets:
            if target.uid and target.uid.casefold() in lowered:
                findings.append(Finding("uid", rel, "target UID present",
                                        target.packet_id))
                counts["uid"] += 1
            if target.public_id and target.public_id.casefold() in lowered:
                findings.append(Finding("public_id", rel, "target public ID present",
                                        target.packet_id))
                counts["public_id"] += 1
            for fragment in target.path_fragments:
                if fragment and fragment.casefold() in lowered:
                    findings.append(Finding("source_path", rel,
                                            f"path fragment {fragment!r}",
                                            target.packet_id))
                    counts["source_path"] += 1
                    break
            title_tokens = target.title_tokens
            if target.is_distinctive_title \
                    and contains_sequence(text_tokens, title_tokens):
                findings.append(Finding("full_title", rel,
                                        "title present as a consecutive sequence",
                                        target.packet_id))
                counts["full_title"] += 1

            title_overlaps.append(containment(set(title_tokens), text_token_set))
            if target.description:
                description_overlaps.append(
                    containment(token_set(target.description), text_token_set)
                )

    single_token_titles = sorted(
        t.packet_id for t in targets if not t.is_distinctive_title
    )
    overlap = {
        "title_token_overlap": _distribution(title_overlaps),
        "description_token_overlap": _distribution(description_overlaps),
        "single_token_title_packets": single_token_titles,
        "single_token_title_count": len(single_token_titles),
        "note": (
            "Scattered token overlap is expected: spec §5 requires operational "
            "content to be preserved verbatim, and a body about its own subject "
            "shares vocabulary with its title. Only the ordered title sequence "
            "is gated, and only for multi-token titles — a one-word title is an "
            "ordinary English word whose presence identifies nothing."
        ),
    }

    return AuditReport(
        root=str(root),
        files_scanned=len(files),
        counts=counts,
        findings=tuple(findings),
        overlap=overlap,
        file_digests=digests,
        problems=tuple(problems),
    )


def _distribution(values: Sequence[float]) -> dict[str, Any]:
    if not values:
        return {"count": 0}
    ordered = sorted(values)
    mid = len(ordered) // 2
    median = (ordered[mid] if len(ordered) % 2
              else (ordered[mid - 1] + ordered[mid]) / 2)
    return {
        "count": len(ordered),
        "min": round(ordered[0], 4),
        "median": round(median, 4),
        "max": round(ordered[-1], 4),
        "mean": round(sum(ordered) / len(ordered), 4),
    }


def assert_disjoint(author_root: Path, reviewer_root: Path) -> list[str]:
    """Prove the two exports share no file path and no file bytes (spec §11)."""
    author = {p.relative_to(author_root).as_posix(): canonical.sha256_file(p)
              for p in _iter_files(author_root)}
    reviewer = {p.relative_to(reviewer_root).as_posix(): canonical.sha256_file(p)
                for p in _iter_files(reviewer_root)}

    problems: list[str] = []
    shared_paths = sorted(set(author) & set(reviewer))
    for path in shared_paths:
        problems.append(f"path present in both exports: {path}")

    reviewer_by_digest: dict[str, list[str]] = {}
    for path, digest in reviewer.items():
        reviewer_by_digest.setdefault(digest, []).append(path)
    for path, digest in sorted(author.items()):
        if digest in reviewer_by_digest:
            problems.append(
                f"author file {path!r} is byte-identical to reviewer-private "
                f"{reviewer_by_digest[digest][0]!r}"
            )
    return problems


def target_identities(
    packets: Iterable[Mapping[str, Any]],
) -> list[TargetIdentity]:
    """Build the answer key from private mapping entries."""
    out: list[TargetIdentity] = []
    for entry in packets:
        out.append(TargetIdentity(
            packet_id=str(entry.get("packet_id") or ""),
            uid=str(entry.get("target_uid") or ""),
            public_id=str(entry.get("public_id") or ""),
            source_path=str(entry.get("source_path") or ""),
            title=str(entry.get("title") or ""),
            description=str(entry.get("description") or ""),
        ))
    return out
