"""Which files in this repository are first-class registry resources.

Membership requires two independent agreements: the file must sit under an
**approved root**, and it must match a **shape detector** for exactly one kind.

The load-bearing invariant is that exclusions are anchored path *prefixes*,
never bare directory names. A bare-segment blocklist is provably wrong here:
``domain-agentic-resources/agents/documentation/`` is a category of
documentation-*writing* agents, and a segment rule on ``documentation`` silently
deletes six genuine first-class resources while intending to exclude
``domain-agentic-resources/documentation/``, which is documentation *about*
resources. Prefixes can tell those apart; segment names cannot.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable, Optional

KINDS = ("prompt", "technique", "skill", "agent", "command", "persona")

#: Root directories that ship first-class resources but are not ``domain-*``.
#: An explicit allowlist, never unconstrained recursion (Phase 2A decision).
TOOLKIT_ROOTS = (
    "agentic-system-factory",
    "ai-investment-research-toolkit",
    "childrens-book-studio",
    "financial-records-toolkit",
    "sourced-nonfiction-studio",
)

#: Roots that hold authoring guidance, standalone exports, fixtures or tooling.
#: Recorded so the allowlist is auditable as a partition of the repository.
NON_REGISTRY_ROOTS = (
    "authoring",
    "continuity-kit",
    "meta",
    "portable-prompt-system",
    "scripts",
    "techniques",
    "tests",
)

#: Directories whose contents are a parent resource's bundled components.
COMPONENT_DIRS = frozenset(
    {"references", "assets", "resources", "cards", "fixtures", "evals", "scripts"}
)

#: Anchored non-resource prefixes. Demonstrations, proof bundles, vendored
#: pointer trees, adapted template exports and tool configuration.
NON_RESOURCE_PREFIXES = (
    "domain-agentic-resources/documentation/",
    "agentic-system-factory/samples/",
    "agentic-system-factory/templates/",
    "agentic-system-factory/worked-runs/",
    "ai-investment-research-toolkit/config/",
    "ai-investment-research-toolkit/referenced-prompts/",
    "ai-investment-research-toolkit/samples/",
    "childrens-book-studio/design-bundle/",
    "childrens-book-studio/referenced-prompts/",
    "financial-records-toolkit/config/",
    "sourced-nonfiction-studio/config/",
    "sourced-nonfiction-studio/referenced-prompts/",
    "sourced-nonfiction-studio/samples/",
)

#: Filenames that are documentation wherever they appear.
META_DOC_FILENAMES = frozenset(
    {
        "AGENTS.md",
        "ARCHITECTURE.md",
        "CLAUDE.md",
        "DRY_RUN.md",
        "EXPANSION_ROADMAP.md",
        "GOLD_STANDARD_RUN.md",
        "GUIDE.md",
        "GUIDE_SECTION_AUDIT.md",
        "INDEX.md",
        "LICENSE.md",
        "MAINTENANCE_BACKLOG.md",
        "MASTER_TECHNIQUE_INDEX.md",
        "PIPELINE_OVERVIEW.md",
        "PROMPT_INDEX.md",
        "PROMPT_INDEX_GUIDE.md",
        "PROMPT_PACK_PLAN.md",
        "PROMPT_TEST_REVIEW.md",
        "README.md",
        "ROADMAP.md",
        "RUNBOOK.md",
        "SKILL_PATTERN_INDEX.md",
        "SKILL_QUALITY_RUBRIC.md",
        "SKILL_USE_CASE_LOOKUP.md",
        "USE_CASE_LOOKUP.md",
        "field_guide.md",
    }
)

#: An ALL-CAPS Markdown file at a toolkit root is that toolkit's documentation.
CAPS_DOC_RE = re.compile(r"^[A-Z0-9_]+\.md$")

#: Structural container segments that only encode the kind, and are therefore
#: dropped from the public ID (``skills/x/y`` -> ``x/y``).
STRUCTURAL_SEGMENTS = {
    "skill": "skills",
    "agent": "agents",
    "command": "commands",
    "persona": "personas",
}


class MembershipError(RuntimeError):
    """Discovery cannot proceed: identity would be untrustworthy."""


@dataclass(frozen=True)
class Candidate:
    """A file-backed first-class resource."""

    path: str  # repo-relative, POSIX
    kind: str
    detector: str


@dataclass(frozen=True)
class Exclusion:
    path: str
    reason: str
    detail: str = ""


def domain_roots(repo_root: Path) -> tuple[str, ...]:
    """The ``domain-*`` allowlist, read from the index generator.

    Reusing ``DOMAIN_DIRS`` rather than globbing keeps the registry and the
    legacy index from drifting apart about which domains exist.
    """
    source = (repo_root / "scripts" / "generate_prompt_index.py").read_text(encoding="utf-8")
    try:
        block = source.split("DOMAIN_DIRS = [", 1)[1].split("]", 1)[0]
    except IndexError as exc:  # pragma: no cover - defensive
        raise MembershipError("cannot locate DOMAIN_DIRS in generate_prompt_index.py") from exc
    dirs = tuple(re.findall(r'"([^"]+)"', block))
    if not dirs:
        raise MembershipError("DOMAIN_DIRS parsed as empty")
    return dirs


def approved_roots(repo_root: Path) -> tuple[str, ...]:
    return tuple(sorted(set(domain_roots(repo_root)) | set(TOOLKIT_ROOTS)))


def validate_roots(repo_root: Path, roots: Iterable[str]) -> None:
    """An approved root that does not exist means a stale configuration."""
    missing = [r for r in roots if not (repo_root / r).is_dir()]
    if missing:
        raise MembershipError(f"approved roots do not exist: {', '.join(sorted(missing))}")
    overlap = set(roots) & set(NON_REGISTRY_ROOTS)
    if overlap:
        raise MembershipError(f"roots are both approved and non-registry: {sorted(overlap)}")


def scope_of(rel: PurePosixPath) -> str:
    """Public-ID scope: the root, with any ``domain-`` prefix removed."""
    root = rel.parts[0]
    return root[len("domain-"):] if root.startswith("domain-") else root


def classify(rel: PurePosixPath, roots: frozenset[str]) -> tuple[Optional[str], str, str]:
    """Return ``(kind, detector, exclusion_reason)`` for one repo-relative path.

    Precedence is fixed and total: every path either yields exactly one kind or
    one exclusion reason. Ties are impossible by construction because each rule
    returns immediately.
    """
    parts = rel.parts
    if len(parts) < 2:
        return None, "", "root_level_document"
    root, name = parts[0], parts[-1]
    text = rel.as_posix()

    if root not in roots:
        return None, "", "root_not_approved"
    if name.startswith("_"):
        return None, "", "planning_document"

    # 1. anchored non-resource prefix
    if text.startswith(NON_RESOURCE_PREFIXES):
        return None, "", "non_resource_prefix"

    middle = set(parts[1:-1])

    # 2. SKILL.md
    if name == "SKILL.md":
        if "skills" in parts[:-1] and not (COMPONENT_DIRS & middle):
            return "skill", "skill_manifest", ""
        return None, "", "skill_manifest_outside_skills_tree"

    # 3. bundled component directory
    if COMPONENT_DIRS & middle:
        return None, "", "bundled_component"

    # 4. meta-doc filename
    if name in META_DOC_FILENAMES:
        return None, "", "meta_document"

    # 5. toolkit ALL-CAPS documentation
    if root in TOOLKIT_ROOTS and CAPS_DOC_RE.match(name):
        return None, "", "toolkit_documentation"

    # 6-8. agentic container segments
    if "personas" in middle:
        return "persona", "personas_container", ""
    if "agents" in middle:
        return "agent", "agents_container", ""
    if "commands" in middle:
        return "command", "commands_container", ""

    # 9. anything else inside a skill bundle is an attachment of that skill
    if "skills" in middle:
        return None, "", "skill_bundle_attachment"

    # 10. prompt fallback
    if name.endswith(".md"):
        return "prompt", "markdown_under_approved_root", ""
    return None, "", "not_markdown"


def discover(repo_root: Path) -> tuple[list[Candidate], list[Exclusion]]:
    """Walk the repository and partition every Markdown file.

    Raises ``MembershipError`` on duplicate candidate paths or an invalid root
    configuration — identity must never be built on an ambiguous corpus.
    """
    roots = approved_roots(repo_root)
    validate_roots(repo_root, roots)
    root_set = frozenset(roots)

    candidates: list[Candidate] = []
    exclusions: list[Exclusion] = []
    seen: set[str] = set()

    # Only approved roots are walked. Everything outside them is out of scope by
    # construction rather than by exclusion, which keeps the generated summary
    # stable when unrelated documentation is added elsewhere in the repository.
    for root in roots:
        for path in sorted((repo_root / root).rglob("*.md")):
            rel = PurePosixPath(path.relative_to(repo_root).as_posix())
            kind, detector, reason = classify(rel, root_set)
            text = rel.as_posix()
            if kind is None:
                exclusions.append(Exclusion(path=text, reason=reason))
                continue
            if text in seen:
                raise MembershipError(f"duplicate candidate path: {text}")
            seen.add(text)
            candidates.append(Candidate(path=text, kind=kind, detector=detector))

    candidates.sort(key=lambda c: c.path)
    exclusions.sort(key=lambda e: e.path)
    return candidates, exclusions


def would_be_first_class(path: str, roots: frozenset[str]) -> Optional[str]:
    """Kind a *historical* path would have had, judged from the path alone.

    Used for reorg tombstones, where the file no longer exists on disk.
    """
    kind, _, _ = classify(PurePosixPath(path), roots)
    return kind
