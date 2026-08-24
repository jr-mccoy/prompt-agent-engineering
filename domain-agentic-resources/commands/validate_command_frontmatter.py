#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_FIELDS = ["name", "description", "version", "category", "tags", "agents_used"]


def parse_frontmatter(text: str) -> tuple[dict[str, str], str] | tuple[None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    fm_text = text[4:end]
    body = text[end + 5 :]

    data: dict[str, str] = {}
    for raw_line in fm_text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data, body


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    parsed, body = parse_frontmatter(text)
    if parsed is None:
        return [f"{path}: missing YAML frontmatter"]

    for field in REQUIRED_FIELDS:
        if field not in parsed or parsed[field] == "":
            errors.append(f"{path}: missing required field '{field}'")

    expected_name = path.stem
    actual_name = parsed.get("name", "")
    if actual_name != expected_name:
        errors.append(f"{path}: name '{actual_name}' must match filename stem '{expected_name}'")


    return errors


def main() -> int:
    root = Path(__file__).resolve().parent
    md_files = sorted(root.glob("**/*.md"))
    md_files = [p for p in md_files if p.name != "README.md"]

    all_errors: list[str] = []
    for path in md_files:
        all_errors.extend(validate_file(path))

    if all_errors:
        print("Frontmatter validation failed:\n")
        for err in all_errors:
            print(f"- {err}")
        return 1

    print(f"Frontmatter validation passed for {len(md_files)} command files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
