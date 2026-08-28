#!/usr/bin/env python3
"""
Repair relative Markdown links left dangling by a reorganization.

``scripts/apply_reorg_map.py`` rewrites references written as repo-root paths.
It cannot fix a *relative* link such as ``../productivity/foo.md``, because the
correct replacement depends on where the referring file itself now sits -- and
during a reorg both ends may have moved.

This script closes that gap. For every broken relative link reported by
``scripts/check_relative_links.py`` it takes the link target's basename, looks
that basename up among the destinations recorded in ``meta/REORG_MAP.tsv``, and
rewrites the link to a correct relative path from the referring file to the
file's new home.

A link is only repaired when the basename resolves to exactly one destination.
Ambiguous basenames, and links whose target simply never existed, are reported
and left alone for a human to resolve.

Usage::

    python3 scripts/repair_relative_links.py [--check]
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REORG_MAP = REPO_ROOT / "meta" / "REORG_MAP.tsv"
CHECKER = REPO_ROOT / "scripts" / "check_relative_links.py"

DELETED_RE = re.compile(r"^DELETED\s+\S+?:(?P<dest>\S+)")
BROKEN_RE = re.compile(r"^\s*(?P<src>\S+\.md)\s*->\s*(?P<target>\S+)\s*$")


def destinations() -> dict[str, list[str]]:
    """
    Return {basename: [destination repo paths]} for resolving a broken link.

    Indexed under both basenames, because a dangling link can carry either:

    - the *old* name, when the link text was never updated
      (``../productivity/productivity_personal_energy_audit.md``); and
    - the *new* name, when the text was updated but the relative path was not.

    A third source covers the case where the link target never moved at all and
    only the referring file did: every file still present in the repository,
    added under its basename. Map destinations are indexed first so a moved
    file always wins over a same-named survivor.
    """
    direct: dict[str, str] = {}
    for raw in REORG_MAP.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) != 2:
            continue
        old, target = parts[0].strip(), parts[1].strip()
        match = DELETED_RE.match(target)
        dest = match.group("dest") if match else (None if target.startswith("DELETED") else target)
        if dest:
            direct[old] = dest

    # A phased reorg records intermediate hops (A->B, then B->C); follow each
    # entry to the path that actually exists now.
    by_base: dict[str, list[str]] = {}
    for old, dest in direct.items():
        seen = {old}
        while dest in direct and dest not in seen:
            seen.add(dest)
            dest = direct[dest]
        for base in {os.path.basename(dest), os.path.basename(old)}:
            by_base.setdefault(base, []).append(dest)

    mapped = {b: sorted(set(d)) for b, d in by_base.items()}

    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in dirnames if d not in {".git", "node_modules", "__pycache__"}]
        for name in filenames:
            if not name.endswith(".md") or name in mapped:
                continue
            rel = (Path(dirpath) / name).relative_to(REPO_ROOT).as_posix()
            by_base.setdefault(name, []).append(rel)

    return {b: sorted(set(d)) for b, d in by_base.items()}


def broken_links() -> list[tuple[str, str]]:
    """Run the link checker and return its (source_file, link_target) pairs."""
    proc = subprocess.run(
        [sys.executable, str(CHECKER)], capture_output=True, text=True, cwd=REPO_ROOT
    )
    pairs: list[tuple[str, str]] = []
    for line in proc.stdout.splitlines():
        match = BROKEN_RE.match(line)
        if match:
            pairs.append((match.group("src"), match.group("target")))
    return pairs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="report repairs without writing")
    args = parser.parse_args()

    by_base = destinations()
    repaired: list[str] = []
    unresolved: list[tuple[str, str, str]] = []
    edits: dict[str, list[tuple[str, str]]] = {}

    for src, target in broken_links():
        if src.startswith("PROMPT_INDEX"):
            continue  # regenerated wholesale by its own generator
        base = os.path.basename(target.rstrip("/"))
        if not base.endswith(".md"):
            unresolved.append((src, target, "directory reference"))
            continue
        if base == "README.md":
            # Which README a broken link meant is a judgement call, not a lookup.
            unresolved.append((src, target, "README target — resolve by hand"))
            continue
        candidates = by_base.get(base)
        if not candidates:
            unresolved.append((src, target, "no destination in reorg map"))
            continue
        if len(candidates) > 1:
            unresolved.append((src, target, f"ambiguous: {candidates}"))
            continue
        new_rel = os.path.relpath(REPO_ROOT / candidates[0], (REPO_ROOT / src).parent)
        edits.setdefault(src, []).append((target, new_rel))

    for src, pairs in sorted(edits.items()):
        path = REPO_ROOT / src
        text = original = path.read_text(encoding="utf-8")
        for old, new in pairs:
            # Bound the match so ../a/x.md does not also rewrite ../../a/x.md.
            text = re.sub(rf"(?<![\w./-]){re.escape(old)}(?![\w.-])", new, text)
        if text != original:
            repaired.append(src)
            if not args.check:
                path.write_text(text, encoding="utf-8")

    verb = "would repair" if args.check else "repaired"
    print(f"{verb} links in {len(repaired)} file(s).")
    for src in repaired:
        print(f"  {src}")
    if unresolved:
        print(f"\n{len(unresolved)} link(s) need a human decision:")
        for src, target, why in unresolved:
            print(f"  {src} -> {target}   ({why})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
