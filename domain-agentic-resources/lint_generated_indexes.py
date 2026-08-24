#!/usr/bin/env python3
"""Lint generated README/index markdown files for quality and readability."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

HEADING_RE = re.compile(r"^#{1,6}\s+(.+)$")
SENTENCE_RE = re.compile(r"[^.!?]+[.!?]")
WORD_RE = re.compile(r"[A-Za-z][A-Za-z'-]*")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
ANCHOR_LINK_RE = re.compile(r"\[[^\]]+\]\(#[^)]+\)")
UNRESOLVED_RE = [
    re.compile(r"\{\{[^{}]+\}\}"),
    re.compile(r"\b(TODO|TBD|FIXME|PLACEHOLDER)\b", re.IGNORECASE),
    re.compile(r"<[^>]*\.\.\.[^>]*>"),
]
MISSING_SPACE_TEMPLATE_RE = [
    re.compile(r"\w\{\{[^{}]+\}\}"),
    re.compile(r"\}\}\w"),
    re.compile(r"\w\[[^\]]+\]\([^)]+\)"),
    re.compile(r"\[[^\]]+\]\([^)]+\)\w"),
]
FRAGMENT_END_RE = re.compile(r"\b(and|or|but|because|if|when|while|to|of|with|for)\.?$", re.IGNORECASE)


@dataclass
class Issue:
    severity: str
    file: Path
    line: int
    message: str


def slugify(heading: str) -> str:
    heading = heading.strip().lower()
    heading = re.sub(r"[`*_~]", "", heading)
    heading = re.sub(r"[^a-z0-9\s-]", "", heading)
    return re.sub(r"\s+", "-", heading).strip("-")


def collect_headings(text: str) -> set[str]:
    anchors: set[str] = set()
    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if not m:
            continue
        anchors.add(slugify(m.group(1)))
    return anchors


def lint_file(path: Path, min_avg_words: float, min_sentence_count: int) -> list[Issue]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    anchors = collect_headings(text)
    issues: list[Issue] = []

    for idx, line in enumerate(lines, start=1):
        for pat in MISSING_SPACE_TEMPLATE_RE:
            if pat.search(line):
                issues.append(Issue("warning", path, idx, "Missing spacing around template/link phrase"))
                break

        for pat in UNRESOLVED_RE:
            if pat.search(line):
                if "VIBE-TODO" in line.upper():
                    continue
                issues.append(Issue("error", path, idx, "Unresolved placeholder detected"))
                break

        if line.count("[") != line.count("]") or line.count("(") != line.count(")"):
            if "http" in line or "[" in line:
                issues.append(Issue("error", path, idx, "Potential malformed markdown link syntax"))

        if ANCHOR_LINK_RE.search(line):
            for _, target in LINK_RE.findall(line):
                if target.startswith("#"):
                    anchor = target[1:]
                    if anchor and anchor not in anchors:
                        issues.append(Issue("error", path, idx, f"Broken anchor link: #{anchor}"))

        stripped = line.strip()
        if stripped and len(stripped.split()) >= 4 and FRAGMENT_END_RE.search(stripped):
            issues.append(Issue("warning", path, idx, "Possible sentence fragment"))

    sentences = [s.strip() for s in SENTENCE_RE.findall(text) if s.strip()]
    sentence_count = len(sentences)
    word_count = sum(len(WORD_RE.findall(s)) for s in sentences)
    avg_words = (word_count / sentence_count) if sentence_count else 0.0

    if sentence_count < min_sentence_count:
        issues.append(Issue("error", path, 1, f"Readability threshold not met: only {sentence_count} sentences found"))
    if avg_words < min_avg_words:
        issues.append(Issue("error", path, 1, f"Readability threshold not met: average words per sentence {avg_words:.2f} < {min_avg_words}"))

    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--min-avg-words", type=float, default=7.0)
    parser.add_argument("--min-sentences", type=int, default=20)
    parser.add_argument("--warn-only-readability", action="store_true")
    args = parser.parse_args()

    all_issues: list[Issue] = []
    for file_path in args.files:
        all_issues.extend(lint_file(file_path, args.min_avg_words, args.min_sentences))

    for issue in all_issues:
        print(f"[{issue.severity.upper()}] {issue.file}:{issue.line} - {issue.message}")

    errors = [i for i in all_issues if i.severity == "error"]

    if args.warn_only_readability:
        non_readability = [
            i for i in errors if "Readability threshold not met" not in i.message
        ]
        return 1 if non_readability else 0

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
