"""Per-kind normalization of native source formats.

Adapters read; they never write. Source frontmatter stays exactly as authored
(ADR-0004) and the registry carries the normalized projection.

Two rules the adapters exist to enforce:

* **Nothing is invented.** A missing description is omitted, not synthesized
  from the first paragraph the way the legacy index does. A derived value is
  always listed in ``derived_fields`` so a consumer can tell it apart from an
  authored one.
* **Malformed metadata degrades; it does not fall back to a regex scavenger.**
  The legacy index's ``_fallback_extract`` is right for best-effort search and
  wrong here: it produces partial metadata indistinguishable from parsed
  metadata.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

import yaml

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)

COMPLETENESS_FULL = "full"
COMPLETENESS_MINIMAL = "minimal"
COMPLETENESS_DEGRADED = "degraded"


@dataclass
class Normalized:
    title: str
    description: Optional[str]
    native: dict[str, Any]
    derived_fields: list[str] = field(default_factory=list)
    metadata_completeness: str = COMPLETENESS_FULL
    diagnostics: list[dict[str, str]] = field(default_factory=list)
    raw_frontmatter: dict[str, Any] = field(default_factory=dict)


def sha256_file(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def bundle_digest(files: list[Path], base: Path) -> tuple[str, int]:
    """Deterministic hash over a sorted ``relpath\\tsha256`` manifest."""
    entries = sorted(
        f"{p.relative_to(base).as_posix()}\t{hashlib.sha256(p.read_bytes()).hexdigest()}"
        for p in files
    )
    manifest = "\n".join(entries) + ("\n" if entries else "")
    return "sha256:" + hashlib.sha256(manifest.encode("utf-8")).hexdigest(), len(entries)


def _title_from_body(text: str) -> Optional[str]:
    match = H1_RE.search(text)
    return match.group(1).strip() if match else None


def _title_from_slug(slug: str) -> str:
    return re.sub(r"[-_]+", " ", slug).strip().title()


def parse_source(path: Path, slug: str) -> tuple[Optional[dict], str, Normalized]:
    """Read a source file and establish title / completeness / diagnostics.

    Returns ``(frontmatter_or_None, body_text, partially_filled_Normalized)``.
    ``frontmatter`` is ``None`` when the file has no frontmatter *or* when its
    YAML failed to parse; the two cases are distinguished by
    ``metadata_completeness``.
    """
    text = path.read_text(encoding="utf-8", errors="replace")
    match = FRONTMATTER_RE.match(text)

    derived: list[str] = []
    diagnostics: list[dict[str, str]] = []
    frontmatter: Optional[dict] = None
    completeness = COMPLETENESS_FULL

    if match is None:
        completeness = COMPLETENESS_MINIMAL
    else:
        try:
            loaded = yaml.safe_load(match.group(1))
            if isinstance(loaded, dict):
                frontmatter = loaded
            else:
                completeness = COMPLETENESS_DEGRADED
                diagnostics.append(
                    {
                        "severity": "error",
                        "code": "frontmatter_parse_failed",
                        "detail": "frontmatter is not a YAML mapping",
                    }
                )
        except yaml.YAMLError as exc:
            completeness = COMPLETENESS_DEGRADED
            detail = " ".join(str(exc).split())
            diagnostics.append(
                {
                    "severity": "error",
                    "code": "frontmatter_parse_failed",
                    "detail": detail[:300],
                }
            )

    title = None
    if frontmatter:
        raw_title = frontmatter.get("title") or frontmatter.get("name")
        if isinstance(raw_title, str) and raw_title.strip():
            title = raw_title.strip()
    if title is None:
        title = _title_from_body(text)
        if title is not None:
            derived.append("title")
    if title is None:
        title = _title_from_slug(slug)
        if "title" not in derived:
            derived.append("title")

    normalized = Normalized(
        title=title,
        description=None,
        native={},
        derived_fields=derived,
        metadata_completeness=completeness,
        diagnostics=diagnostics,
        raw_frontmatter=frontmatter or {},
    )
    return frontmatter, text, normalized


def _clean_str(value: Any) -> Optional[str]:
    if isinstance(value, str) and value.strip():
        return " ".join(value.split())
    return None


def _clean_list(value: Any) -> Optional[list[str]]:
    if isinstance(value, list):
        items = [str(v).strip() for v in value if str(v).strip()]
        return items or None
    return None


def _put(native: dict[str, Any], key: str, value: Any) -> None:
    """Absence means *not applicable*, so never store an empty value."""
    if value is not None:
        native[key] = value


def adapt_prompt(fm: dict, norm: Normalized, path: str) -> Normalized:
    norm.description = _clean_str(fm.get("description"))
    n = norm.native
    _put(n, "category", _clean_str(fm.get("category")))
    _put(n, "techniques", _clean_list(fm.get("techniques")))
    _put(n, "tags", _clean_list(fm.get("tags")))
    _put(n, "difficulty", _clean_str(fm.get("difficulty")))
    _put(n, "updated", _clean_str(fm.get("updated")))
    _put(n, "related", _clean_list(fm.get("related_prompts")))
    if isinstance(fm.get("reasoning"), dict):
        n["reasoning"] = fm["reasoning"]
    return norm


def adapt_skill(fm: dict, norm: Normalized, path: str) -> Normalized:
    norm.description = _clean_str(fm.get("description"))
    meta = fm.get("metadata") if isinstance(fm.get("metadata"), dict) else {}
    n = norm.native
    _put(n, "name", _clean_str(fm.get("name")))
    _put(n, "tags", _clean_list(meta.get("tags")) or _clean_list(meta.get("keywords")))
    _put(n, "updated", _clean_str(meta.get("updated")) or _clean_str(meta.get("last-updated")))
    return norm


def adapt_agent(fm: dict, norm: Normalized, path: str) -> Normalized:
    norm.description = _clean_str(fm.get("description"))
    n = norm.native
    _put(n, "name", _clean_str(fm.get("name")))
    _put(n, "model", _clean_str(fm.get("model")))
    return norm


def adapt_command(fm: dict, norm: Normalized, path: str) -> Normalized:
    norm.description = _clean_str(fm.get("description"))
    n = norm.native
    _put(n, "name", _clean_str(fm.get("name")))
    _put(n, "category", _clean_str(fm.get("category")))
    _put(n, "version", _clean_str(fm.get("version")))
    _put(n, "tags", _clean_list(fm.get("tags")))
    if isinstance(fm.get("agents_used"), list):
        n["agents_used"] = [str(v) for v in fm["agents_used"]]
    return norm


def adapt_persona(fm: dict, norm: Normalized, path: str) -> Normalized:
    norm.description = _clean_str(fm.get("description"))
    n = norm.native
    _put(n, "name", _clean_str(fm.get("name")))
    _put(n, "color", _clean_str(fm.get("color")))
    return norm


ADAPTERS = {
    "prompt": adapt_prompt,
    "skill": adapt_skill,
    "agent": adapt_agent,
    "command": adapt_command,
    "persona": adapt_persona,
}


def adapt(kind: str, path: Path, rel_path: str, slug: str) -> Normalized:
    frontmatter, _text, norm = parse_source(path, slug)
    if frontmatter:
        ADAPTERS[kind](frontmatter, norm, rel_path)
    return norm
