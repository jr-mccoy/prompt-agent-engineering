#!/usr/bin/env python3
"""Analyze Claude Code commands and generate a metadata index."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def _parse_inline_list(value: str) -> list[str]:
    value = value.strip()
    if not (value.startswith("[") and value.endswith("]")):
        return []
    inner = value[1:-1].strip()
    if not inner:
        return []
    return [p.strip().strip('"\'') for p in inner.split(",") if p.strip()]


def extract_frontmatter_and_body(content: str) -> tuple[dict[str, Any], str]:
    match = FRONTMATTER_RE.match(content)
    if not match:
        return {}, content

    fm_text = match.group(1)
    body = content[match.end() :]

    fm: dict[str, Any] = {}
    current_list_key: str | None = None

    for raw_line in fm_text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if current_list_key and stripped.startswith("- "):
            fm.setdefault(current_list_key, []).append(stripped[2:].strip().strip('"\''))
            continue

        current_list_key = None

        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()

        if value == "":
            fm[key] = []
            current_list_key = key
        elif value.startswith("[") and value.endswith("]"):
            fm[key] = _parse_inline_list(value)
        else:
            fm[key] = value.strip('"\'')

    return fm, body


def _normalize_item(value: str) -> str:
    cleaned = value.strip().strip("`'")
    if cleaned.endswith(".md"):
        cleaned = cleaned[:-3]
    if "/" in cleaned:
        cleaned = cleaned.split("/")[-1]
    return cleaned


def _extract_structured_list(body: str, headings: set[str]) -> list[str]:
    items: list[str] = []
    in_section = False

    for line in body.splitlines():
        header = re.match(r"^##+\s+(.+?)\s*$", line)
        if header:
            in_section = header.group(1).strip().lower() in headings
            continue

        if not in_section:
            continue

        bullet = re.match(r"^\s*[-*]\s+(.+?)\s*$", line)
        if not bullet:
            if line.strip() == "":
                continue
            in_section = False
            continue

        value = bullet.group(1)
        link_match = re.search(r"\(([^)]+)\)", value)
        if link_match:
            value = link_match.group(1)

        normalized = _normalize_item(value)
        if normalized:
            items.append(normalized)

    seen = set()
    unique = []
    for item in items:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique


def extract_command_syntax(content: str, file_path: Path) -> str:
    syntax_patterns = [r"`(/[a-zA-Z0-9-_:]+[^`]*)`", r"^/[a-zA-Z0-9-_:]+"]
    for pattern in syntax_patterns:
        matches = re.findall(pattern, content, re.MULTILINE)
        if matches:
            return matches[0]
    return f"/{file_path.stem.replace('_', '-')}"


def extract_description(body: str, frontmatter: dict[str, Any]) -> str:
    if "description" in frontmatter and isinstance(frontmatter["description"], str):
        return frontmatter["description"]

    for line in body.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            return stripped[:200] + ("..." if len(stripped) > 200 else "")

    return "Command description not available"


def analyze_commands(commands_dir: Path) -> dict[str, list[dict[str, Any]]]:
    commands_by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for md_file in sorted(commands_dir.rglob("*.md")):
        # Per-category README.md files are navigation, not commands. Excluding
        # them keeps this generator's totals equal to inventory_counts.py, which
        # is the authoritative counter for the agentic resource inventory.
        if md_file.name.lower() == "readme.md":
            continue
        rel_path = md_file.relative_to(commands_dir)
        category = rel_path.parent.as_posix() if rel_path.parent.as_posix() != "." else "other"

        content = md_file.read_text(encoding="utf-8")
        frontmatter, body = extract_frontmatter_and_body(content)

        agents = []
        value = frontmatter.get("agents_used", [])
        if isinstance(value, str):
            value = _parse_inline_list(value)
        if isinstance(value, list):
            agents.extend(_normalize_item(v) for v in value if v)
        agents.extend(_extract_structured_list(body, {"related agents", "agents used"}))

        skills = []
        for key in ("skills_used", "related_skills"):
            value = frontmatter.get(key, [])
            if isinstance(value, str):
                value = _parse_inline_list(value)
            if isinstance(value, list):
                skills.extend(_normalize_item(v) for v in value if v)
        skills.extend(_extract_structured_list(body, {"related skills", "skills used"}))

        def _uniq(items: list[str]) -> list[str]:
            seen = set()
            out = []
            for item in items:
                if item and item not in seen:
                    seen.add(item)
                    out.append(item)
            return out

        command_data = {
            "name": md_file.stem.replace("_", "-"),
            "file_path": f"commands/{rel_path.as_posix()}",
            "category": category,
            "syntax": extract_command_syntax(body, md_file),
            "description": extract_description(body, frontmatter),
            "agents": _uniq(agents),
            "skills": _uniq(skills),
            "content_length": len(content),
        }

        commands_by_category[category].append(command_data)

    return commands_by_category


def main() -> dict[str, Any]:
    commands_dir = Path(__file__).resolve().parent
    commands_by_category = analyze_commands(commands_dir)

    sorted_categories = sorted(commands_by_category.keys())
    total_commands = sum(len(cmds) for cmds in commands_by_category.values())

    output = {
        "total_commands": total_commands,
        "total_categories": len(sorted_categories),
        "commands_by_category": {
            cat: sorted(cmds, key=lambda x: x["name"]) for cat, cmds in sorted(commands_by_category.items())
        },
        "categories": sorted_categories,
    }

    output_file = commands_dir / "commands_analysis.json"
    output_file.write_text(json.dumps(output, indent=2), encoding="utf-8")

    print(f"Found {total_commands} commands across {len(sorted_categories)} categories")
    print(f"Analysis saved to: {output_file}")
    return output


if __name__ == "__main__":
    main()
