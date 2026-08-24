#!/usr/bin/env python3
"""Relative-link checker for the repository's Markdown files.

Walks every tracked Markdown file, extracts inline Markdown links and reference
definitions, ignores external/mailto/anchor-only targets, URL-decodes the path,
and verifies the referenced file or directory exists. Exits non-zero if any
relative link is broken.

Usage:
    python3 scripts/check_relative_links.py [--root DIR] [--quiet]
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from urllib.parse import unquote

# [text](target)  — target may be <bracketed>; stop at whitespace-title
INLINE = re.compile(r'\[(?:[^\]]*)\]\(\s*<?([^)<>\s]+)>?(?:\s+"[^"]*")?\s*\)')
# [label]: target
REFDEF = re.compile(r'^\s{0,3}\[[^\]]+\]:\s*<?([^\s<>]+)>?', re.M)

SKIP_PREFIX = ("http://", "https://", "mailto:", "tel:", "ftp://", "data:", "#", "//")
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}

# Literal placeholders used in documentation that demonstrates link syntax.
PLACEHOLDER_TARGETS = {
    "link", "url", "URL", "path", "target", "filename", "file", "example.md",
    "your-file.md", "TBD", "tbd",
}


def is_external(target: str) -> bool:
    """True for targets a relative-path checker must not try to resolve."""
    if target.startswith(SKIP_PREFIX):
        return True
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
        return True
    # Template variables substituted at runtime, e.g. {baseDir}/..., {{var}}, $ROOT/...
    if any(ch in target for ch in "{}$"):
        return True
    # A relative filesystem path never contains a quote character. Quoted tokens
    # here come from source code inside a nested fence that the fence-stripper
    # could not pair (e.g. a ```typescript block inside a ```markdown example).
    if any(ch in target for ch in "'\"`"):
        return True
    if target in PLACEHOLDER_TARGETS:
        return True
    return False


def check(root: str, quiet: bool) -> int:
    broken: list[tuple[str, str]] = []
    checked = 0
    files = 0

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if not fn.lower().endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            files += 1
            try:
                text = open(path, encoding="utf-8").read()
            except (OSError, UnicodeDecodeError):
                continue
            # strip fenced code blocks so examples are not treated as links
            text = re.sub(r"^```.*?^```", "", text, flags=re.S | re.M)

            targets = [m.group(1) for m in INLINE.finditer(text)]
            targets += [m.group(1) for m in REFDEF.finditer(text)]

            for raw in targets:
                target = raw.split("#", 1)[0].strip()
                if not target or is_external(target):
                    continue
                checked += 1
                resolved = os.path.normpath(
                    os.path.join(dirpath, unquote(target))
                )
                if not os.path.exists(resolved):
                    broken.append((os.path.relpath(path, root), raw))

    if not quiet:
        print(f"Scanned {files} markdown files; checked {checked} relative links.")
    if broken:
        print(f"\nBROKEN RELATIVE LINKS: {len(broken)}\n")
        for src, tgt in sorted(broken):
            print(f"  {src} -> {tgt}")
        return 1
    print("OK — all relative Markdown links resolve.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".", help="repository root to scan (default: .)")
    ap.add_argument("--quiet", action="store_true", help="suppress the scan summary line")
    args = ap.parse_args()
    return check(args.root, args.quiet)


if __name__ == "__main__":
    sys.exit(main())
