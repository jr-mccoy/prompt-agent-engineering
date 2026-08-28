#!/usr/bin/env python3
"""
Rewrite repository cross-references after a reorganization.

Reads ``meta/REORG_MAP.tsv`` -- the record of every file moved or removed by a
reorg -- and repoints references to those files at their new homes.

The map has two columns separated by a tab::

    old/path.md<TAB>new/path.md
    old/path.md<TAB>DELETED superseded-by:surviving/path.md
    old/path.md<TAB>DELETED merged-into:surviving/path.md

A deleted file still has a *destination*: the prompt that absorbed it. Readers
following an old reference want that prompt, so deletions are rewritten just
like moves.

Two reference forms are rewritten:

1. **Repo-root paths** (``domain-x/sub/file.md``) -- appear in ``related_prompts``
   frontmatter and in prose. Replaced with the destination's repo-root path.
2. **Bare basenames** (``file.md``, usually inside backticks or a Markdown link)
   -- replaced with the bare destination basename when the destination lands in
   the *same* directory as the referring file, and with the destination's full
   repo-root path otherwise, since a bare name no longer resolves across
   directories.

A bare basename is only rewritten when it is unambiguous: if the same basename
belongs to more than one map entry, or a surviving file elsewhere in the
repository still carries it, the basename rule is skipped for that name and only
the full-path rule applies. This is what keeps a deleted
``business-documents/business_writing_sop.md`` from clobbering references to the
surviving ``business-writing/business_writing_sop.md``.

Usage::

    python3 scripts/apply_reorg_map.py [--map PATH] [--check] [--verbose]

``--check`` reports what would change and exits non-zero if anything would,
without writing. Run it in CI to prove no stale references remain.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MAP = REPO_ROOT / "meta" / "REORG_MAP.tsv"

# Generated artifacts: rebuilt by their own generators, never hand-patched.
SKIP_FILES = {"PROMPT_INDEX.md", "PROMPT_INDEX.json", "PROMPT_INDEX_LEARNER_AUDIENCE.json"}
SKIP_DIRS = {".git", "node_modules", "__pycache__"}

# "DELETED superseded-by:path" / "DELETED merged-into:path"
DELETED_RE = re.compile(r"^DELETED\s+\S+?:(?P<dest>\S+)")


def parse_map(map_path: Path) -> dict[str, str]:
    """Return {old_repo_path: destination_repo_path} from the reorg map."""
    mapping: dict[str, str] = {}
    for lineno, raw in enumerate(map_path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) != 2:
            sys.exit(f"{map_path}:{lineno}: expected two tab-separated columns, got {len(parts)}")
        old, target = parts[0].strip(), parts[1].strip()
        match = DELETED_RE.match(target)
        if match:
            dest = match.group("dest")
        elif target.startswith("DELETED"):
            # A deletion with no destination: nothing to repoint references at.
            continue
        else:
            dest = target
        mapping[old] = dest
    return _resolve_chains(mapping, map_path)


def _resolve_chains(mapping: dict[str, str], map_path: Path) -> dict[str, str]:
    """
    Collapse A->B->C into A->C.

    A reorg run in phases records intermediate hops: a file absorbed into a
    second file in one phase, which is itself moved in a later phase. Following
    only one hop would repoint readers at a path that no longer exists, so each
    entry is followed to its final destination.
    """
    resolved: dict[str, str] = {}
    for old in mapping:
        seen = [old]
        dest = mapping[old]
        while dest in mapping and dest not in seen:
            seen.append(dest)
            dest = mapping[dest]
        if dest in seen:
            sys.exit(f"{map_path}: reference cycle in reorg map: {' -> '.join(seen + [dest])}")
        resolved[old] = dest
    return resolved


def build_basename_rules(mapping: dict[str, str], all_md: list[Path]) -> dict[str, str]:
    """
    Return {old_basename: destination_repo_path} for basenames safe to rewrite.

    A basename is unsafe when two map entries share it, or when a file that
    still exists in the repository carries the same basename -- a bare
    reference to it is more likely to mean the survivor than the moved file.
    """
    counts: dict[str, int] = {}
    for old in mapping:
        counts[os.path.basename(old)] = counts.get(os.path.basename(old), 0) + 1

    surviving: set[str] = set()
    moved_sources = set(mapping)
    for path in all_md:
        rel = path.relative_to(REPO_ROOT).as_posix()
        if rel not in moved_sources:
            surviving.add(path.name)

    rules: dict[str, str] = {}
    for old, dest in mapping.items():
        base = os.path.basename(old)
        if counts[base] > 1 or base in surviving:
            continue
        rules[base] = dest
    return rules


def iter_markdown() -> list[Path]:
    files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name.endswith(".md") and name not in SKIP_FILES:
                files.append(Path(dirpath) / name)
    return sorted(files)


def rewrite(text: str, rel_path: str, mapping: dict[str, str], basename_rules: dict[str, str]) -> str:
    """Apply full-path rules then basename rules to one file's text."""
    referring_dir = os.path.dirname(rel_path)

    # Longest paths first, so a/b/c.md is not partially rewritten by a rule for c.md.
    for old in sorted(mapping, key=len, reverse=True):
        if old in text:
            text = text.replace(old, mapping[old])

    for base in sorted(basename_rules, key=len, reverse=True):
        if base not in text:
            continue
        dest = basename_rules[base]
        # A bare name still resolves if the destination sits in this directory.
        replacement = os.path.basename(dest) if os.path.dirname(dest) == referring_dir else dest
        text = re.sub(rf"(?<![\w/-]){re.escape(base)}", replacement, text)

    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--map", type=Path, default=DEFAULT_MAP, help="path to REORG_MAP.tsv")
    parser.add_argument("--check", action="store_true", help="report changes without writing; exit 1 if any")
    parser.add_argument("--verbose", action="store_true", help="list every rewritten reference")
    args = parser.parse_args()

    if not args.map.exists():
        sys.exit(f"reorg map not found: {args.map}")

    mapping = parse_map(args.map)
    if not mapping:
        print("reorg map has no rewritable entries; nothing to do.")
        return 0

    all_md = iter_markdown()
    basename_rules = build_basename_rules(mapping, all_md)

    changed: list[tuple[str, int]] = []
    for path in all_md:
        rel = path.relative_to(REPO_ROOT).as_posix()
        original = path.read_text(encoding="utf-8")
        updated = rewrite(original, rel, mapping, basename_rules)
        if updated == original:
            continue
        hits = sum(
            1
            for a, b in zip(original.splitlines(), updated.splitlines())
            if a != b
        )
        changed.append((rel, hits))
        if not args.check:
            path.write_text(updated, encoding="utf-8")

    verb = "would update" if args.check else "updated"
    print(f"{len(mapping)} map entries, {len(basename_rules)} safe basename rules.")
    print(f"{verb} {len(changed)} file(s).")
    if args.verbose or args.check:
        for rel, hits in changed:
            print(f"  {rel} ({hits} line(s))")

    if args.check and changed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
