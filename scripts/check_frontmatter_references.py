#!/usr/bin/env python3
"""Frontmatter cross-reference validator with a ratchet baseline.

`scripts/check_relative_links.py` validates Markdown *body* links. It never
looks inside YAML frontmatter, so the repository's largest set of machine-read
cross-references — `related_prompts` and its siblings — has been unvalidated.
This script closes that gap without demanding a flag-day rewrite of existing
debt.

Reference fields inspected
--------------------------
``related_prompts``, ``see_also_toolkit``, ``see_also_seed``.

(``references`` is deliberately excluded: it holds prose citations to external
literature, not repository paths.)

Canonical format
----------------
A reference must be a **repository-relative POSIX path** that resolves from the
repository root, e.g. ``domain-AI-ML/data-for-ml/mldata_data_quality_audit.md``.

Statuses
--------
``ok``                     resolves from the repository root — canonical.
``noncanonical_relative``  resolves only relative to the referring file.
``noncanonical_basename``  a bare filename that resolves uniquely somewhere.
``unresolved``             does not resolve at all.

Ratchet
-------
Everything that is not ``ok`` is recorded in ``meta/xref_baseline.json``.

* ``--check`` fails on any non-ok reference that is **not** in the baseline, and
  on a baseline that no longer matches the file it claims to describe. Existing
  baselined debt passes.
* ``--update`` rewrites the baseline. It refuses to add entries unless
  ``--allow-growth`` is passed, so debt cannot grow silently, but it always
  accepts a shrinking baseline.

Usage::

    python3 scripts/check_frontmatter_references.py --check
    python3 scripts/check_frontmatter_references.py --update
    python3 scripts/check_frontmatter_references.py --report
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - PyYAML is a declared CI dependency
    raise SystemExit("PyYAML is required: pip install -r requirements-ci.txt")

REPO_ROOT = Path(__file__).resolve().parent.parent
BASELINE_PATH = REPO_ROOT / "meta" / "xref_baseline.json"
BASELINE_SCHEMA = "xref-baseline-v1"

REFERENCE_FIELDS = ("related_prompts", "see_also_toolkit", "see_also_seed")
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)

OK = "ok"
NONCANONICAL_RELATIVE = "noncanonical_relative"
NONCANONICAL_BASENAME = "noncanonical_basename"
UNRESOLVED = "unresolved"
DEBT_STATUSES = (NONCANONICAL_RELATIVE, NONCANONICAL_BASENAME, UNRESOLVED)


def markdown_files() -> list[Path]:
    found = []
    for path in REPO_ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.relative_to(REPO_ROOT).parts):
            continue
        found.append(path)
    return sorted(found)


def _basename_map(files: list[Path]) -> dict[str, list[str]]:
    index: dict[str, list[str]] = defaultdict(list)
    for path in files:
        index[path.name].append(path.relative_to(REPO_ROOT).as_posix())
    return index


def _frontmatter(path: Path) -> dict | None:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        # A malformed-YAML file is already reported by the prompt-index
        # generator; this validator does not duplicate that error.
        return None
    return data if isinstance(data, dict) else None


def classify(reference: str, source: Path, basenames: dict[str, list[str]]) -> str:
    ref = reference.strip()
    if not ref:
        return UNRESOLVED

    if (REPO_ROOT / ref).is_file():
        return OK

    relative = (source.parent / ref).resolve()
    try:
        relative.relative_to(REPO_ROOT)
    except ValueError:
        pass
    else:
        if relative.is_file():
            return NONCANONICAL_RELATIVE

    if "/" not in ref and len(basenames.get(ref, ())) == 1:
        return NONCANONICAL_BASENAME

    return UNRESOLVED


def collect() -> tuple[list[dict], Counter]:
    files = markdown_files()
    basenames = _basename_map(files)
    findings: list[dict] = []
    tally: Counter = Counter()

    for path in files:
        frontmatter = _frontmatter(path)
        if not frontmatter:
            continue
        rel_source = path.relative_to(REPO_ROOT).as_posix()
        for field in REFERENCE_FIELDS:
            value = frontmatter.get(field)
            if value is None:
                continue
            items = value if isinstance(value, list) else [value]
            for item in items:
                if not isinstance(item, str):
                    continue
                status = classify(item, path, basenames)
                tally[status] += 1
                tally["references"] += 1
                if status != OK:
                    findings.append(
                        {"file": rel_source, "field": field, "reference": item.strip(), "status": status}
                    )

    findings.sort(key=lambda f: (f["file"], f["field"], f["reference"]))
    return findings, tally


def _key(finding: dict) -> tuple[str, str, str]:
    return finding["file"], finding["field"], finding["reference"]


def render_baseline(findings: list[dict], tally: Counter) -> str:
    payload = {
        "schema": BASELINE_SCHEMA,
        "purpose": (
            "Known-unresolved or noncanonical frontmatter cross-references. This is "
            "a ratchet: CI fails on any entry not listed here. Entries may be "
            "removed as references are fixed; adding one requires --allow-growth "
            "and a deliberate decision."
        ),
        "canonical_format": "repository-relative POSIX path that resolves from the repository root",
        "fields_checked": list(REFERENCE_FIELDS),
        "totals": {
            "references_checked": tally["references"],
            "canonical": tally[OK],
            "noncanonical_relative": tally[NONCANONICAL_RELATIVE],
            "noncanonical_basename": tally[NONCANONICAL_BASENAME],
            "unresolved": tally[UNRESOLVED],
            "baselined": len(findings),
        },
        "entries": findings,
    }
    return json.dumps(payload, indent=2) + "\n"


def load_baseline() -> tuple[set[tuple[str, str, str]], dict]:
    if not BASELINE_PATH.exists():
        raise SystemExit(
            f"::error::{BASELINE_PATH.relative_to(REPO_ROOT)} is missing. "
            f"Run: python3 scripts/check_frontmatter_references.py --update"
        )
    payload = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    if payload.get("schema") != BASELINE_SCHEMA:
        raise SystemExit(
            f"::error::{BASELINE_PATH.relative_to(REPO_ROOT)}: unexpected schema "
            f"{payload.get('schema')!r}, expected {BASELINE_SCHEMA!r}"
        )
    return {_key(entry) for entry in payload["entries"]}, payload


def cmd_report(findings: list[dict], tally: Counter) -> None:
    print(f"references checked      : {tally['references']}")
    print(f"  canonical             : {tally[OK]}")
    for status in DEBT_STATUSES:
        print(f"  {status:<21} : {tally[status]}")
    by_field = Counter(f["field"] for f in findings)
    if by_field:
        print("debt by field:")
        for field, count in by_field.most_common():
            print(f"  {count:>5}  {field}")


def cmd_check(findings: list[dict], tally: Counter) -> None:
    baselined, payload = load_baseline()
    current = {_key(f) for f in findings}

    new = sorted(current - baselined)
    errors = [
        f"::error::{path}: {field} reference does not resolve from the repository "
        f"root: {reference!r}"
        for path, field, reference in new
    ]

    if errors:
        errors.append(
            f"::error::{len(new)} new unresolved/noncanonical frontmatter reference(s). "
            f"Use a repository-relative POSIX path that resolves. Existing debt is "
            f"tracked in {BASELINE_PATH.relative_to(REPO_ROOT)}; do not add to it to "
            f"silence this check."
        )
        raise SystemExit("\n".join(errors))

    fixed = len(baselined - current)
    declared = payload.get("totals", {}).get("baselined")
    if declared is not None and fixed == 0 and declared != len(baselined):
        raise SystemExit(
            f"::error::{BASELINE_PATH.relative_to(REPO_ROOT)}: totals.baselined="
            f"{declared} but the file lists {len(baselined)} entries"
        )

    print(
        f"Frontmatter cross-reference check passed: {tally['references']} references, "
        f"{tally[OK]} canonical, {len(current)} known debt entries."
    )
    if fixed:
        print(
            f"{fixed} baselined reference(s) now resolve. Shrink the baseline with: "
            f"python3 scripts/check_frontmatter_references.py --update"
        )


def cmd_update(findings: list[dict], tally: Counter, allow_growth: bool) -> None:
    if BASELINE_PATH.exists():
        baselined, _ = load_baseline()
        new = sorted({_key(f) for f in findings} - baselined)
        if new and not allow_growth:
            listing = "\n".join(f"  {p}: {f} -> {r}" for p, f, r in new[:20])
            raise SystemExit(
                f"refusing to grow the baseline by {len(new)} entry/entries.\n"
                f"{listing}\n"
                f"Fix the references, or pass --allow-growth if the growth is intended."
            )
    BASELINE_PATH.parent.mkdir(parents=True, exist_ok=True)
    BASELINE_PATH.write_text(render_baseline(findings, tally), encoding="utf-8")
    print(
        f"Wrote {BASELINE_PATH.relative_to(REPO_ROOT)} "
        f"({len(findings)} entries, {tally['references']} references checked)."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="fail on new debt (CI mode)")
    parser.add_argument("--update", action="store_true", help="rewrite the baseline")
    parser.add_argument("--report", action="store_true", help="print current tallies")
    parser.add_argument(
        "--allow-growth",
        action="store_true",
        help="with --update, permit the baseline to gain entries",
    )
    args = parser.parse_args()
    if not (args.check or args.update or args.report):
        args.check = True

    findings, tally = collect()

    if args.report:
        cmd_report(findings, tally)
    if args.update:
        cmd_update(findings, tally, args.allow_growth)
    if args.check:
        cmd_check(findings, tally)


if __name__ == "__main__":
    main()
