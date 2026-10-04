#!/usr/bin/env python3
"""Validate the technique catalog and authoring docs against computed reality.

Recomputes ground truth from techniques/MASTER_TECHNIQUE_INDEX.md and the
filesystem, then checks that every hand-written claim and reference in the
authoring documentation set still matches it:

  1. Index header totals (active / catalogued / deprecated / categories)
  2. Technique-count claims in satellite docs (README, CLAUDE.md, quick-starts, ...)
  3. Every technique ID referenced in the authoring doc set resolves to a
     definition (no phantom IDs)
  4. No dead relative .md links in the authoring doc set (including
     techniques/new-techniques/ detail files)
  5. Resource counts (skills / agents / commands / personas) claimed in
     CLAUDE.md match the filesystem
  6. Every `techniques:` entry in PROMPT_INDEX.json names a catalogued ID
     (hard). Citing a deprecated (merged) ID, or attaching a parenthesised
     name that differs from the catalog's, is reported as a warning.

Usage:
    python3 scripts/validate_technique_catalog.py            # run all checks
    python3 scripts/validate_technique_catalog.py --counts   # print computed
                                                             # numbers only
    python3 scripts/validate_technique_catalog.py --uncited  # list active IDs
                                                             # no prompt cites

Exit code 0 if all checks pass, 1 otherwise. Run after any edit to the
master technique index or the authoring docs; counts in satellite docs are
hand-maintained, so this script is what keeps them honest.
"""

import argparse
import json
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = "techniques/MASTER_TECHNIQUE_INDEX.md"
PROMPT_INDEX_PATH = "PROMPT_INDEX.json"

# Docs whose technique-ID references and relative links must all resolve.
# (The audit report is excluded on purpose: it cites historical phantom IDs.)
REFERENCE_DOCS = [
    "techniques/MASTER_TECHNIQUE_INDEX.md",
    "techniques/USE_CASE_LOOKUP.md",
    "AI_AGENT_QUICK_START.md",
    "NON_CODING_QUICK_START.md",
    "PROMPT_QUALITY_STANDARDS.md",
    "authoring/TECHNIQUE_PICKER_FAST.md",
    "authoring/NEW_PROMPT_TEMPLATE.md",
    "authoring/PROMPT_STRUCTURE_GUIDE.md",
    "authoring/NEW_RESOURCE_CHECKLIST.md",
]

# Docs that state technique totals ("N active techniques", "across M categories").
CLAIM_DOCS = [
    "README.md",
    "CLAUDE.md",
    "START_HERE_FOR_AI.md",
    "REPO_MAP.md",
    "AI_AGENT_QUICK_START.md",
    "techniques/README.md",
    "techniques/USE_CASE_LOOKUP.md",
    "techniques/MASTER_TECHNIQUE_INDEX.md",
]

# Technique ID prefixes are DERIVED from the parsed catalog, never hand-listed.
# A hardcoded literal here previously omitted GT and IPC, which silently exempted
# 25 catalogued technique IDs from phantom-reference checking. Deriving the
# prefixes means a new category is covered the moment it is defined in the master
# index, with no second list to remember to edit.
ID_TOKEN_ANY = re.compile(r"\b([A-Z]{2,4})-\d{1,3}\b")


def id_token_pattern(prefixes):
    """Build the reference-scanning pattern from the catalog's own prefixes."""
    if not prefixes:
        raise ValueError("no technique ID prefixes were parsed from the master index")
    alternation = "|".join(sorted(prefixes, key=lambda p: (-len(p), p)))
    return re.compile(rf"\b(?:{alternation})-\d{{1,3}}\b")
HEADING_DEF = re.compile(r"^#{3,4} ([A-Z]{2,4}-\d+[a-z]?)(.*)$", re.M)
BOLD_DEF = re.compile(
    r"^\*\*((?:[A-Z]{2,4}-\d+)(?:/[A-Z]{2,4}-\d+)*)(?::| \()(.*)$", re.M
)
ALIAS = re.compile(r"\(also ([A-Z]{2,4}-\d+)\)")
# A frontmatter technique entry: a bare ID, optionally followed by "(Name)".
CITED_TECHNIQUE = re.compile(r"^([A-Z]{2,4}-\d{1,3})(?:\s*\((.*)\))?$")
MERGED_INTO = re.compile(r"Merged into \*{0,2}([A-Z]{2,4}-\d+)")


def read(path):
    with open(os.path.join(REPO_ROOT, path), encoding="utf-8") as f:
        return f.read()


def strip_code_fences(text):
    """Drop fenced code blocks so illustrative examples don't count as definitions."""
    return re.sub(r"```.*?```", "", text, flags=re.S)


def parse_index():
    raw = read(INDEX_PATH)
    text = strip_code_fences(raw)

    heading_ids = {}
    for m in HEADING_DEF.finditer(text):
        heading_ids.setdefault(m.group(1), []).append(m.group(2))

    bold_ids = {}
    for m in BOLD_DEF.finditer(text):
        for tid in m.group(1).split("/"):
            bold_ids.setdefault(tid, []).append(m.group(2))

    all_ids = set(heading_ids) | set(bold_ids)
    aliases = set(ALIAS.findall(text)) - all_ids

    def is_tombstone(entries):
        return any("Merged into" in e or "DEPRECATED" in e for e in entries)

    # An ID is deprecated when its only definitions are merge/deprecation stubs.
    # (An active heading definition outranks a tombstone elsewhere — IDs get reused.)
    deprecated = set()
    for tid in all_ids:
        heads = heading_ids.get(tid, [])
        bolds = bold_ids.get(tid, [])
        if heads:
            if is_tombstone(heads):
                deprecated.add(tid)
        elif is_tombstone(bolds):
            deprecated.add(tid)

    return {
        "raw": raw,
        "all_ids": all_ids,
        "aliases": aliases,
        "deprecated": deprecated,
        "active": len(all_ids) - len(deprecated),
        "total": len(all_ids),
        "categories": len({tid.split("-")[0] for tid in all_ids}),
        # Every prefix the catalog actually defines, for reference scanning.
        "prefixes": {tid.split("-")[0] for tid in all_ids},
        "heading_ids": heading_ids,
        "bold_ids": bold_ids,
    }


def check_index_header(idx, errors):
    m = re.search(
        r"\*\*Total Techniques:\*\* (\d+) active techniques across (\d+) categories "
        r"\((\d+) IDs catalogued, including (\d+) deprecated/merged stubs\)",
        idx["raw"],
    )
    if not m:
        errors.append(f"{INDEX_PATH}: header 'Total Techniques' line not found "
                      "or format changed — update this script's pattern with it")
        return
    claimed = tuple(int(g) for g in m.groups())
    actual = (idx["active"], idx["categories"], idx["total"], len(idx["deprecated"]))
    if claimed != actual:
        errors.append(
            f"{INDEX_PATH}: header claims active/categories/total/deprecated "
            f"{claimed}, computed {actual}"
        )


def check_satellite_claims(idx, errors):
    claim_patterns = [
        re.compile(r"(\d+) active(?: prompt engineering)? techniques across (\d+) categories"),
        re.compile(r"\((\d+) active techniques\)"),
        re.compile(r"\((\d+) active\) - Formally defined"),
        re.compile(r"(\d+) active techniques \(canonical\)"),
    ]
    for path in CLAIM_DOCS:
        text = read(path)
        for pat in claim_patterns:
            for m in pat.finditer(text):
                count = int(m.group(1))
                if count != idx["active"]:
                    line = text[: m.start()].count("\n") + 1
                    errors.append(
                        f"{path}:{line}: claims {count} active techniques, "
                        f"computed {idx['active']}"
                    )
                if pat.groups == 2 and m.lastindex == 2:
                    cats = int(m.group(2))
                    if cats != idx["categories"]:
                        line = text[: m.start()].count("\n") + 1
                        errors.append(
                            f"{path}:{line}: claims {cats} categories, "
                            f"computed {idx['categories']}"
                        )


def check_id_references(idx, errors):
    known = idx["all_ids"] | idx["aliases"]
    token = id_token_pattern(idx["prefixes"])
    for path in REFERENCE_DOCS:
        refs = set(token.findall(read(path)))
        missing = sorted(refs - known)
        if missing:
            errors.append(f"{path}: references undefined technique IDs: {', '.join(missing)}")


def _norm(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())


def canonical_names(idx):
    """ID -> catalog name, taken from its first ### heading definition."""
    names = {}
    for tid, entries in idx["heading_ids"].items():
        name = re.split(r"\*\(|→|\*\*", entries[0])[0].strip(" :*—-")
        if name:
            names[tid] = name
    return names


def load_prompt_records(path=PROMPT_INDEX_PATH):
    with open(os.path.join(REPO_ROOT, path), encoding="utf-8") as f:
        return json.load(f)["prompts"]


def check_prompt_technique_references(idx, records, errors, warnings):
    """Frontmatter `techniques:` lists must cite catalogued IDs.

    Unknown or malformed entries are hard errors. Deprecated IDs resolve
    through their merge target, so they only warn. A parenthesised name that
    is neither contained in nor contains the canonical name also warns: it
    usually means the author meant a different technique.
    """
    known = idx["all_ids"] | idx["aliases"]
    names = canonical_names(idx)
    merged_into = {}
    for tid in idx["deprecated"]:
        for entry in idx["heading_ids"].get(tid, []) + idx["bold_ids"].get(tid, []):
            m = MERGED_INTO.search(entry)
            if m:
                merged_into[tid] = m.group(1)
                break

    unknown, deprecated, mislabeled = {}, {}, []
    for record in records:
        path = record.get("path", "?")
        for raw in record.get("techniques") or []:
            m = CITED_TECHNIQUE.match(str(raw).strip())
            if not m or m.group(1) not in known:
                key = m.group(1) if m else str(raw).strip()
                unknown.setdefault(key, []).append(path)
                continue
            tid, cited_name = m.group(1), m.group(2)
            if tid in idx["deprecated"]:
                deprecated[tid] = deprecated.get(tid, 0) + 1
            canon = names.get(tid)
            if cited_name and canon:
                a, b = _norm(cited_name), _norm(canon)
                if a and a not in b and b not in a:
                    mislabeled.append((path, tid, cited_name, canon))

    for key in sorted(unknown):
        paths = unknown[key]
        sample = ", ".join(paths[:3]) + (" …" if len(paths) > 3 else "")
        errors.append(
            f"{PROMPT_INDEX_PATH}: technique '{key}' is not in the catalog "
            f"({len(paths)} citation(s): {sample})"
        )
    for tid in sorted(deprecated):
        target = merged_into.get(tid, "?")
        warnings.append(
            f"{tid} is deprecated (merged into {target}) but cited "
            f"{deprecated[tid]} time(s) in {PROMPT_INDEX_PATH}"
        )
    for path, tid, cited_name, canon in sorted(mislabeled):
        warnings.append(f"{path}: {tid} cited as '{cited_name}', catalog name '{canon}'")


def uncited_by_family(idx, records):
    """Active catalog IDs that no prompt's `techniques:` list cites."""
    cited = set()
    for record in records:
        for raw in record.get("techniques") or []:
            m = CITED_TECHNIQUE.match(str(raw).strip())
            if m:
                cited.add(m.group(1))
    families = {}
    for tid in sorted(idx["all_ids"] - idx["deprecated"] - cited,
                      key=lambda t: (t.split("-")[0], int(re.sub(r"\D", "", t.split("-")[1])))):
        families.setdefault(tid.split("-")[0], []).append(tid)
    return families


def check_relative_links(errors):
    link = re.compile(r"\]\(([^)#\s]+\.md)\)")
    for path in REFERENCE_DOCS:
        base = os.path.dirname(os.path.join(REPO_ROOT, path))
        for target in sorted(set(link.findall(read(path)))):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if not os.path.isfile(os.path.normpath(os.path.join(base, target))):
                errors.append(f"{path}: dead link -> {target}")


def count_resources():
    def count(subdir, pattern):
        root = os.path.join(REPO_ROOT, "domain-agentic-resources", subdir)
        n = 0
        for dirpath, _dirnames, filenames in os.walk(root):
            for fn in filenames:
                if pattern == "SKILL.md":
                    n += fn == "SKILL.md"
                else:
                    n += fn.endswith(".md") and fn.lower() != "readme.md"
        return n

    return {
        "skills": count("skills", "SKILL.md"),
        "agents": count("agents", "*.md"),
        "commands": count("commands", "*.md"),
        "personas": count("personas", "*.md"),
    }


def check_resource_claims(resources, errors):
    text = read("CLAUDE.md")
    pat = re.compile(r"(\d+) skills, (\d+) agents, (\d+) commands, (\d+) personas")
    for m in pat.finditer(text):
        claimed = dict(zip(("skills", "agents", "commands", "personas"),
                           (int(g) for g in m.groups())))
        for key, value in claimed.items():
            if value != resources[key]:
                line = text[: m.start()].count("\n") + 1
                errors.append(
                    f"CLAUDE.md:{line}: claims {value} {key}, "
                    f"filesystem has {resources[key]}"
                )


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--counts", action="store_true",
                        help="print computed counts and exit")
    parser.add_argument("--uncited", action="store_true",
                        help="list active technique IDs no prompt cites, by family, and exit")
    args = parser.parse_args()

    idx = parse_index()
    resources = count_resources()

    if args.counts:
        print(f"active techniques:     {idx['active']}")
        print(f"catalogued IDs:        {idx['total']}")
        print(f"deprecated stubs:      {len(idx['deprecated'])} "
              f"({', '.join(sorted(idx['deprecated']))})")
        print(f"categories (prefixes): {idx['categories']}")
        print(f"aliases:               {', '.join(sorted(idx['aliases'])) or '(none)'}")
        for key, value in resources.items():
            print(f"{key + ':':<23}{value}")
        return 0

    records = load_prompt_records()
    families = uncited_by_family(idx, records)
    if args.uncited:
        total = sum(len(ids) for ids in families.values())
        print(f"{total} active technique IDs are cited by no prompt:")
        for family, ids in sorted(families.items()):
            print(f"  {family:<4} {len(ids):>3}  {', '.join(ids)}")
        return 0

    errors, warnings = [], []
    check_index_header(idx, errors)
    check_satellite_claims(idx, errors)
    check_id_references(idx, errors)
    check_relative_links(errors)
    check_resource_claims(resources, errors)
    check_prompt_technique_references(idx, records, errors, warnings)

    if warnings:
        print(f"{len(warnings)} warning(s):")
        for w in warnings:
            print(f"  - {w}")
        print()

    if errors:
        print(f"FAIL — {len(errors)} problem(s):\n")
        for e in errors:
            print(f"  - {e}")
        print("\nIf the catalog legitimately changed, update the claims in the "
              "listed files (run with --counts for the correct numbers).")
        return 1

    print(f"OK — {idx['active']} active techniques across {idx['categories']} "
          f"categories ({idx['total']} IDs, {len(idx['deprecated'])} deprecated); "
          f"all references, links, and claims consistent.")
    uncited = sum(len(ids) for ids in families.values())
    print(f"Note: {uncited} active technique IDs are cited by no prompt "
          f"(informational; run with --uncited).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
