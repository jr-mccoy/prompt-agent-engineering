#!/usr/bin/env python3
"""
Re-sync vendored android/skills forks from upstream.

Copies each upstream skill directory over our fork verbatim, then rewrites the
`name:` field to our prefixed directory name and injects provenance metadata
(upstream repo, path, pinned commit, sync date) into the frontmatter.

Usage:
    resync.py <upstream-root> <ours-root> <upstream-sha> <sync-date>
"""

import re
import shutil
import sys
from pathlib import Path

# our-dir-name -> upstream-relative-path
MAPPING = {
    "android-agp-9-upgrade": "build-system/agp/agp-9-upgrade",
    "android-r8-analyzer": "performance/r8-analyzer",
    "android-edge-to-edge": "system/edge-to-edge",
    "android-navigation-3": "navigation/navigation-3",
    "android-play-billing-upgrade": "play/play-billing-library-version-upgrade",
    "android-play-policy-insights": "play/play-policy-insights",
    "android-migrate-xml-to-compose": "jetpack-compose/migration/migrate-xml-views-to-jetpack-compose",
    "android-xr-jetpack-compose-glimmer": "xr/display-glasses-with-jetpack-compose-glimmer",
}


def rewrite_frontmatter(skill_md: Path, our_name: str, up_path: str,
                        sha: str, synced: str) -> None:
    """Set name to our_name and inject provenance under metadata:."""
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{skill_md}: missing YAML frontmatter")

    end = text.index("\n---\n", 4)
    fm, body = text[4:end], text[end + 5:]

    fm, n = re.subn(r"(?m)^name:.*$", f"name: {our_name}", fm, count=1)
    if n != 1:
        raise ValueError(f"{skill_md}: no name: field")

    provenance = (
        f"  upstream: https://github.com/android/skills\n"
        f"  upstream-path: {up_path}\n"
        f"  upstream-commit: {sha}\n"
        f"  upstream-synced: '{synced}'\n"
    )

    # Anchor after last-updated: if present, else after the metadata: line.
    if re.search(r"(?m)^  last-updated:.*$", fm):
        fm = re.sub(r"(?m)^(  last-updated:.*)$", r"\1\n" + provenance.rstrip("\n"),
                    fm, count=1)
    elif re.search(r"(?m)^metadata:$", fm):
        fm = re.sub(r"(?m)^(metadata:)$", r"\1\n" + provenance.rstrip("\n"),
                    fm, count=1)
    else:
        fm = fm.rstrip("\n") + "\nmetadata:\n" + provenance.rstrip("\n") + "\n"

    if not body.endswith("\n"):
        body += "\n"
    skill_md.write_text(f"---\n{fm}\n---\n{body}", encoding="utf-8")


def collect_overlays(src: Path, dst: Path) -> dict[str, bytes]:
    """Return {relpath: content} for files in our fork absent from upstream.

    These are deliberate local additions (e.g. offline mirrors of doc pages that
    upstream only links to over HTTPS). They must survive a re-sync, so we snapshot
    them before the overwrite and restore them after.
    """
    overlays = {}
    if not dst.exists():
        return overlays
    for f in dst.rglob("*"):
        if not f.is_file():
            continue
        rel = f.relative_to(dst)
        if rel.name == "SKILL.md":
            continue  # never treat the skill body as an overlay
        if not (src / rel).exists():
            overlays[str(rel)] = f.read_bytes()
    return overlays


WRAPPER_FILE = "local-wrapper.md"
WRAPPER_MARKER = "<!-- BEGIN LOCAL WRAPPER -->"


def apply_wrapper(dst: Path) -> bool:
    """Append the skill's local wrapper block to the upstream SKILL.md body.

    Upstream skill bodies omit the sections our rubric requires (When NOT to Use,
    Verification, Related Skills). Rather than hand-edit a vendored body -- which a
    re-sync would silently discard -- each skill keeps its additions in
    `local-wrapper.md`. That file is an overlay (absent upstream, so preserved
    automatically), and this appends it below the upstream body on every sync.

    Idempotent: skips if the marker is already present.
    """
    wrapper, skill_md = dst / WRAPPER_FILE, dst / "SKILL.md"
    if not wrapper.exists():
        return False

    body = skill_md.read_text(encoding="utf-8")
    if WRAPPER_MARKER in body:
        return False

    block = wrapper.read_text(encoding="utf-8").strip()
    if not body.endswith("\n"):
        body += "\n"
    skill_md.write_text(
        f"{body}\n---\n\n{WRAPPER_MARKER}\n"
        f"<!-- Not from upstream. Source: {WRAPPER_FILE}. Re-applied on every sync;\n"
        f"     edit that file, never this block. -->\n\n"
        f"{block}\n",
        encoding="utf-8",
    )
    return True


def main() -> int:
    upstream_root, ours_root, sha, synced = (
        Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3], sys.argv[4]
    )

    for our_name, up_path in sorted(MAPPING.items()):
        src, dst = upstream_root / up_path, ours_root / our_name
        if not (src / "SKILL.md").exists():
            print(f"SKIP {our_name}: upstream {up_path} has no SKILL.md")
            continue

        overlays = collect_overlays(src, dst)
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        rewrite_frontmatter(dst / "SKILL.md", our_name, up_path, sha, synced)

        for rel, content in sorted(overlays.items()):
            target = dst / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)

        wrapped = apply_wrapper(dst)

        n = sum(1 for _ in dst.rglob("*") if _.is_file())
        note = f"  [+{len(overlays)} local overlay(s) preserved]" if overlays else ""
        note += "  [+wrapper appended]" if wrapped else ""
        print(f"SYNCED {our_name:<38} <- {up_path}  ({n} files){note}")
        for rel in sorted(overlays):
            print(f"         overlay: {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
