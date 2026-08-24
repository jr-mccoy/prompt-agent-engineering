#!/usr/bin/env python3
"""Analyze Claude Code agent files and extract metadata for the agent index."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parent
AGENTS_DIR = ROOT_DIR / "domain-agentic-resources" / "agents"


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def _parse_inline_list(value: str) -> list[str]:
    value = value.strip()
    if not (value.startswith("[") and value.endswith("]")):
        return []
    inner = value[1:-1].strip()
    if not inner:
        return []
    parts = [p.strip().strip('"\'') for p in inner.split(",")]
    return [p for p in parts if p]


def extract_frontmatter_and_body(content: str) -> tuple[dict[str, Any], str]:
    """Extract simple YAML-like frontmatter and body without external deps."""
    match = FRONTMATTER_RE.match(content)
    if not match:
        return {}, content

    fm_text = match.group(1)
    body = content[match.end() :]

    frontmatter: dict[str, Any] = {}
    current_list_key: str | None = None

    for raw_line in fm_text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()

        if not stripped or stripped.startswith("#"):
            continue

        if current_list_key and stripped.startswith("- "):
            frontmatter.setdefault(current_list_key, []).append(stripped[2:].strip().strip('"\''))
            continue

        current_list_key = None

        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if not value:
            frontmatter[key] = []
            current_list_key = key
        elif value.startswith("[") and value.endswith("]"):
            frontmatter[key] = _parse_inline_list(value)
        else:
            frontmatter[key] = value.strip('"\'')

    return frontmatter, body


def _normalize_relation(value: str) -> str:
    clean = value.strip().strip("`'")
    if "/" in clean:
        clean = clean.split("/")[-1]
    if clean.endswith(".md"):
        clean = clean[:-3]
    return clean


def _extract_structured_list(body: str, section_names: set[str]) -> list[str]:
    lines = body.splitlines()
    in_section = False
    found: list[str] = []

    for line in lines:
        header = re.match(r"^##+\s+(.+?)\s*$", line)
        if header:
            normalized = header.group(1).strip().lower()
            in_section = normalized in section_names
            continue

        if not in_section:
            continue

        bullet = re.match(r"^\s*[-*]\s+(.+?)\s*$", line)
        if not bullet:
            if line.strip() == "":
                continue
            # stop on non-list content inside target section
            in_section = False
            continue

        item = bullet.group(1)
        link_match = re.search(r"\(([^)]+)\)", item)
        if link_match:
            item = link_match.group(1)
        item = _normalize_relation(item)
        if item:
            found.append(item)

    # de-dupe preserve order
    seen = set()
    unique = []
    for item in found:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique


def analyze_agent_file(file_path: Path) -> dict[str, Any] | None:
    content = file_path.read_text(encoding="utf-8")
    frontmatter, body = extract_frontmatter_and_body(content)
    if not frontmatter:
        return None

    related_agents = []
    for field in ("related_agents", "agents_used"):
        value = frontmatter.get(field, [])
        if isinstance(value, str):
            value = _parse_inline_list(value)
        if isinstance(value, list):
            related_agents.extend(_normalize_relation(v) for v in value if v)

    related_agents.extend(
        _extract_structured_list(body, {"related agents", "agents used", "related resources"})
    )

    related_skills = []
    for field in ("related_skills", "skills_used"):
        value = frontmatter.get(field, [])
        if isinstance(value, str):
            value = _parse_inline_list(value)
        if isinstance(value, list):
            related_skills.extend(_normalize_relation(v) for v in value if v)

    related_skills.extend(
        _extract_structured_list(body, {"related skills", "skills used"})
    )

    def unique(items: list[str]) -> list[str]:
        seen = set()
        out = []
        for item in items:
            if item and item not in seen:
                seen.add(item)
                out.append(item)
        return out

    rel_path = file_path.relative_to(AGENTS_DIR)

    return {
        "name": frontmatter.get("name", ""),
        "description": frontmatter.get("description", ""),
        "model": frontmatter.get("model", "inherit"),
        "file_path": f"agents/{rel_path.as_posix()}",
        "related_agents": unique(related_agents),
        "related_skills": unique(related_skills),
        "content_length": len(body),
    }


def main() -> None:
    agents_by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)
    model_counts: dict[str, int] = defaultdict(int)

    for md_file in AGENTS_DIR.rglob("*.md"):
        rel_path = md_file.relative_to(AGENTS_DIR)
        category = rel_path.parts[0] if len(rel_path.parts) > 1 else "uncategorized"

        agent_data = analyze_agent_file(md_file)
        if not agent_data:
            continue

        agent_data["category"] = category
        agent_data["relative_path"] = rel_path.as_posix()
        agents_by_category[category].append(agent_data)
        model_counts[agent_data["model"]] += 1

    total_agents = sum(len(agents) for agents in agents_by_category.values())

    output_data = {
        "categories": {cat: sorted(agents, key=lambda a: a["name"]) for cat, agents in sorted(agents_by_category.items())},
        "model_counts": dict(sorted(model_counts.items())),
        "total_agents": total_agents,
    }

    output_file = AGENTS_DIR / "agents_analysis.json"
    output_file.write_text(json.dumps(output_data, indent=2), encoding="utf-8")

    print(f"Analyzed {total_agents} agents across {len(agents_by_category)} categories")
    print(f"Detailed analysis saved to: {output_file}")


if __name__ == "__main__":
    main()
