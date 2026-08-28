#!/usr/bin/env python3
"""
Keep deliberately duplicated files in sync with the originals they were copied from.

Several directories in this repository are *self-contained by design*: copy the
folder into another project and it works on its own. `domain-idea-to-product/`
and the `*-toolkit` bundles therefore carry copies of prompts that also live in
a canonical domain.

That is a deliberate trade, but nothing detected when an original was edited and
its copies were not. This script closes that gap. `meta/VENDORED.tsv` records
each pair as ``canonical<TAB>copy``, and every copy is compared against its
canonical.

Three differences are expected and ignored:

- **Relative links.** A copy sits at a different depth, so ``](../x/y.md)`` has
  to be rewritten to still resolve. Links are compared by the repo-root path
  they resolve to, not by their literal text.
- **Links re-pointed at a sibling copy.** A bundle points its internal
  cross-references at its own copies rather than back out at the canonicals --
  that is what makes it self-contained -- so a link to a registered copy counts
  as a link to that copy's canonical.
- **The ``category:`` frontmatter field**, which names where the file lives.

Everything else -- prose, instructions, model names, technique lists -- must
match. `--fix` rewrites each copy from its canonical, re-resolving the links and
preserving the copy's own ``category:``.

Only *mirrors* are registered. `portable-prompt-system/` and
`agentic-system-factory/templates/` are deliberately **adapted** exports rather
than mirrors -- the first flattens the directory structure for standalone use,
the second adds machine-readable markers its own scripts parse -- so syncing
them would break them. `meta/VENDORED.tsv` records why they are excluded.

Usage::

    python3 scripts/check_vendored_copies.py            # report drift, exit 1 if any
    python3 scripts/check_vendored_copies.py --fix      # rewrite copies from canonicals
    python3 scripts/check_vendored_copies.py --verbose  # show a diff for each drifted pair
"""

from __future__ import annotations

import argparse
import difflib
import posixpath
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY = REPO_ROOT / "meta" / "VENDORED.tsv"

LINK_RE = re.compile(r"(?P<open>\]\()(?P<target>[^)\s]+)(?P<close>\))")
CATEGORY_RE = re.compile(r"^category:.*$", re.M)
# A link that points outside the repository, or at an anchor, is left alone.
EXTERNAL_RE = re.compile(r"^(https?:|mailto:|#|/)")


def pairs() -> list[tuple[str, str]]:
    if not REGISTRY.exists():
        sys.exit(f"vendored registry not found: {REGISTRY}")
    out: list[tuple[str, str]] = []
    for lineno, raw in enumerate(REGISTRY.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) != 2:
            sys.exit(f"{REGISTRY}:{lineno}: expected two tab-separated columns")
        out.append((parts[0].strip(), parts[1].strip()))
    return out


def resolve_links(text: str, from_file: str) -> str:
    """Replace each relative link target with the repo-root path it resolves to."""
    base = posixpath.dirname(from_file)

    def repl(match: re.Match[str]) -> str:
        target = match.group("target")
        if EXTERNAL_RE.match(target):
            return match.group(0)
        resolved = posixpath.normpath(posixpath.join(base, target))
        return f"{match.group('open')}{resolved}{match.group('close')}"

    return LINK_RE.sub(repl, text)


def rewrite_links(text: str, from_file: str, to_file: str) -> str:
    """Re-point every relative link in `from_file`'s text to work from `to_file`."""
    src_dir = posixpath.dirname(from_file)
    dst_dir = posixpath.dirname(to_file)

    def repl(match: re.Match[str]) -> str:
        target = match.group("target")
        if EXTERNAL_RE.match(target):
            return match.group(0)
        resolved = posixpath.normpath(posixpath.join(src_dir, target))
        rel = posixpath.relpath(resolved, dst_dir or ".")
        return f"{match.group('open')}{rel}{match.group('close')}"

    return LINK_RE.sub(repl, text)


def comparable(text: str, path: str, copy_to_canonical: dict[str, str] | None = None) -> str:
    """
    Normalize a file to the form in which a copy must equal its canonical.

    Beyond resolving links and blanking `category:`, a link pointing at another
    *registered copy* is folded back to that copy's canonical. A self-contained
    bundle deliberately re-points its internal cross-references at its own
    copies -- that is the property that makes it self-contained, so a link to
    the in-bundle sibling and a link to the canonical sibling mean the same
    thing here.
    """
    text = resolve_links(text, path)
    if copy_to_canonical:
        for copy, canonical in copy_to_canonical.items():
            text = text.replace(f"]({copy})", f"]({canonical})")
    text = CATEGORY_RE.sub("category: <normalized>", text)
    return text.strip() + "\n"


def is_subtree_mirror(canonical: str, copy: str) -> bool:
    """
    True when the copy reproduces the canonical's directory shape.

    `authoring/templates/X.md` -> `portable-prompt-system/resource-patterns/templates/X.md`
    keeps its parent directory name, so relative links still resolve unchanged.
    `domain-deep-analysis/X.md` -> `domain-idea-to-product/stage-6-.../X.md` does
    not, so its links have to be rewritten.
    """
    return posixpath.basename(posixpath.dirname(canonical)) == posixpath.basename(
        posixpath.dirname(copy)
    )


def literal(text: str) -> str:
    """Normalize for the subtree-mirror case: only `category:` may differ."""
    return CATEGORY_RE.sub("category: <normalized>", text).strip() + "\n"


def in_sync(
    ctext: str, canonical: str, ptext: str, copy: str, copy_to_canonical: dict[str, str]
) -> bool:
    """
    True when a copy still matches its canonical, under either vendoring style.

    A copy is vendored one of two ways, and each keeps its links valid
    differently:

    - **Subtree mirror** (``portable-prompt-system/resource-patterns/`` mirrors
      ``authoring/``): the whole directory shape is reproduced, so relative links
      are correct *unchanged* and the file is byte-identical.
    - **Flat re-file** (``domain-idea-to-product/stage-N/`` gathers prompts from
      many domains): the file lands at a different depth, so its links must be
      rewritten to still resolve.

    Comparing only resolved links would flag every subtree mirror; comparing only
    raw text would flag every flat re-file. A pair is in sync if it matches under
    either reading.
    """
    if literal(ctext) == literal(ptext):
        return True
    return comparable(ctext, canonical, copy_to_canonical) == comparable(
        ptext, copy, copy_to_canonical
    )


def category_of(text: str) -> str | None:
    match = CATEGORY_RE.search(text)
    return match.group(0) if match else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--fix", action="store_true", help="rewrite drifted copies from their canonicals")
    parser.add_argument("--verbose", action="store_true", help="show a diff for each drifted pair")
    args = parser.parse_args()

    drifted: list[tuple[str, str]] = []
    missing: list[tuple[str, str]] = []
    copy_to_canonical = {copy: canonical for canonical, copy in pairs()}

    for canonical, copy in pairs():
        cpath, ppath = REPO_ROOT / canonical, REPO_ROOT / copy
        if not cpath.exists() or not ppath.exists():
            missing.append((canonical, copy))
            continue

        ctext = cpath.read_text(encoding="utf-8")
        ptext = ppath.read_text(encoding="utf-8")
        if in_sync(ctext, canonical, ptext, copy, copy_to_canonical):
            continue

        drifted.append((canonical, copy))
        if args.verbose and not args.fix:
            diff = difflib.unified_diff(
                comparable(ctext, canonical, copy_to_canonical).splitlines(),
                comparable(ptext, copy, copy_to_canonical).splitlines(),
                fromfile=canonical, tofile=copy, lineterm="", n=1,
            )
            for line in list(diff)[:40]:
                print(f"    {line}")

        if args.fix:
            # Restore the copy in its own vendoring style: a subtree mirror keeps
            # the canonical's links verbatim (its directory shape matches), a flat
            # re-file needs them re-pointed for its new depth. Rewriting a
            # mirror's links would break exactly what makes it a mirror.
            rebuilt = ctext if is_subtree_mirror(canonical, copy) else rewrite_links(ctext, canonical, copy)
            copy_category = category_of(ptext)
            if copy_category:
                rebuilt = CATEGORY_RE.sub(lambda _: copy_category, rebuilt, count=1)
            ppath.write_text(rebuilt, encoding="utf-8")

    total = len(pairs())
    if missing:
        print(f"{len(missing)} registry entry/entries point at a file that does not exist:")
        for canonical, copy in missing:
            print(f"  {canonical}  ->  {copy}")

    if args.fix:
        print(f"{total} vendored pair(s); rewrote {len(drifted)} copy/copies from canonical.")
        return 1 if missing else 0

    if drifted:
        print(f"{total} vendored pair(s); {len(drifted)} have drifted from canonical:")
        for canonical, copy in drifted:
            print(f"  {canonical}\n    -> {copy}")
        print("\nRun 'python3 scripts/check_vendored_copies.py --fix' to re-sync,")
        print("or edit meta/VENDORED.tsv if the copy is meant to diverge.")
        return 1

    print(f"{total} vendored pair(s) in sync with their canonicals.")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
