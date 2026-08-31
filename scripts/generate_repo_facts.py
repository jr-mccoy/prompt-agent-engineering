#!/usr/bin/env python3
"""Canonical repository facts for Prompt & Agent Engineering.

This is the single source of truth for every headline number the project
publishes. It composes the repository's existing authoritative counters rather
than reimplementing them:

  * ``domain-agentic-resources/inventory_counts.py`` — skills / agents / commands
  * ``scripts/validate_technique_catalog.py``        — technique catalog + personas
  * ``PROMPT_INDEX.json``                            — indexed artifacts

Outputs
-------
1. ``meta/REPOSITORY_FACTS.json`` — deterministic, committed, machine-readable.
   Every fact carries a stated membership rule. There is no timestamp: the file
   changes only when the repository's content changes, so diffs stay clean.

2. Generated blocks inside primary documentation, delimited by::

       <!-- REPO_FACTS:BEGIN name=<block> -->
       <!-- REPO_FACTS_DECLARATION: {...} -->
       ...generated markdown...
       <!-- REPO_FACTS:END name=<block> -->

   The declaration comment reuses the proven design of the repository's existing
   ``INVENTORY_COUNTS`` marker: a machine-readable payload that CI compares
   against freshly computed truth.

Validation contract (``--check``) — a missing match is ALWAYS an error:
  * a required block is absent                       -> fail
  * a required declaration is absent                 -> fail
  * a declared value differs from canonical facts    -> fail
  * a block's body differs from its regenerated form -> fail (manual edit)
  * the committed facts artifact is stale            -> fail

Usage::

    python3 scripts/generate_repo_facts.py --write   # regenerate artifact + docs
    python3 scripts/generate_repo_facts.py --check   # verify everything is current
    python3 scripts/generate_repo_facts.py --print   # print facts, change nothing
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

FACTS_PATH = REPO_ROOT / "meta" / "REPOSITORY_FACTS.json"
FACTS_SCHEMA = "repository-facts-v1"

# Directory names that hold a parent resource's bundled components rather than
# resources in their own right. Phase 2 will model these as attachments.
COMPONENT_DIRS = frozenset(
    {"references", "assets", "resources", "cards", "fixtures", "evals", "scripts"}
)

AGENTIC_ROOT = "domain-agentic-resources/"

BEGIN_MARKER = "<!-- REPO_FACTS:BEGIN name={name} -->"
END_MARKER = "<!-- REPO_FACTS:END name={name} -->"
# ``\n?`` on both sides so an empty placeholder block (the two markers on
# consecutive lines) is recognised and can be filled by --write.
BLOCK_RE_TMPL = (
    r"<!-- REPO_FACTS:BEGIN name={name} -->\n?(?P<body>.*?)\n?"
    r"<!-- REPO_FACTS:END name={name} -->"
)
DECL_RE = re.compile(r"<!-- REPO_FACTS_DECLARATION: (?P<json>\{.*\}) -->")


# --------------------------------------------------------------------------
# Composition of the existing authoritative counters
# --------------------------------------------------------------------------
def _load_module(name: str, path: Path):
    """Import a repository script by path (their directories are not packages)."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:  # pragma: no cover - defensive
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _inventory():
    mod = _load_module(
        "pae_inventory_counts",
        REPO_ROOT / "domain-agentic-resources" / "inventory_counts.py",
    )
    return mod.compute_inventory()


def _technique_catalog():
    mod = _load_module(
        "pae_validate_technique_catalog", REPO_ROOT / "scripts" / "validate_technique_catalog.py"
    )
    return mod.parse_index(), mod.count_resources()


def _middle_segments(path: str) -> set[str]:
    """Directory names between the top-level root and the filename."""
    return set(path.split("/")[1:-1])


def _index_partition() -> dict[str, int]:
    """Partition every PROMPT_INDEX.json entry into exactly one category."""
    with (REPO_ROOT / "PROMPT_INDEX.json").open(encoding="utf-8") as fh:
        entries = json.load(fh)["prompts"]

    bundled = agentic = domain_commands = domain_prompts = 0
    for entry in entries:
        path = entry["path"]
        middle = _middle_segments(path)
        if COMPONENT_DIRS & middle:
            bundled += 1
        elif path.startswith(AGENTIC_ROOT):
            agentic += 1
        elif "commands" in middle:
            domain_commands += 1
        else:
            domain_prompts += 1

    total = len(entries)
    assert bundled + agentic + domain_commands + domain_prompts == total, "partition is not total"
    return {
        "indexed_artifacts": total,
        "bundled_component_files": bundled,
        "agentic_resource_artifacts": agentic,
        "domain_command_artifacts": domain_commands,
        "domain_prompt_artifacts": domain_prompts,
    }


def _domain_directories() -> dict[str, int]:
    on_disk = sorted(
        p.name for p in REPO_ROOT.iterdir() if p.is_dir() and p.name.startswith("domain-")
    )
    source = (REPO_ROOT / "scripts" / "generate_prompt_index.py").read_text(encoding="utf-8")
    allowlist = source.split("DOMAIN_DIRS = [", 1)[1].split("]", 1)[0]
    listed = re.findall(r'"(domain-[A-Za-z0-9-]+)"', allowlist)
    unindexed = sorted(set(on_disk) - set(listed))
    return {
        "domain_directories": len(on_disk),
        "indexed_domain_directories": len(sorted(set(on_disk) & set(listed))),
        "unindexed_domain_directories": len(unindexed),
    }


DEFINITIONS = {
    "indexed_artifacts": (
        "Every entry in PROMPT_INDEX.json. A mixed population: domain prompts, "
        "agentic resources, and bundled component files. Not a prompt count."
    ),
    "domain_prompt_artifacts": (
        "Indexed entries outside domain-agentic-resources/ that are neither inside a "
        "bundled-component directory nor inside a commands/ directory."
    ),
    "domain_command_artifacts": (
        "Indexed entries outside domain-agentic-resources/ that sit in a commands/ "
        "directory. These are slash commands filed alongside a domain's prompts."
    ),
    "agentic_resource_artifacts": (
        "Indexed entries under domain-agentic-resources/ that are not inside a "
        "bundled-component directory: skills, agents, commands, personas and the "
        "directory's own documentation."
    ),
    "bundled_component_files": (
        "Indexed entries with a "
        + "/, ".join(sorted(COMPONENT_DIRS))
        + "/ directory between the top-level root and the filename. These are "
        "attachments of a parent resource, not resources in their own right."
    ),
    "skills": "Files matching domain-agentic-resources/skills/**/SKILL.md.",
    "agents": (
        "Markdown files under domain-agentic-resources/agents/**, excluding README.md."
    ),
    "commands": (
        "Markdown files under domain-agentic-resources/commands/**, excluding README.md."
    ),
    "personas": (
        "Markdown files under domain-agentic-resources/personas/**, excluding README.md."
    ),
    "active_techniques": (
        "Non-deprecated technique IDs structurally defined in "
        "techniques/MASTER_TECHNIQUE_INDEX.md, as parsed by "
        "scripts/validate_technique_catalog.py."
    ),
    "catalogued_technique_ids": "All technique IDs defined in the master index, active or deprecated.",
    "deprecated_technique_stubs": "Catalogued technique IDs marked deprecated or merged.",
    "technique_categories": "Distinct technique ID prefixes in the master index.",
    "domain_directories": "Top-level directories named domain-*.",
    "indexed_domain_directories": (
        "domain-* directories present in the DOMAIN_DIRS allowlist of "
        "scripts/generate_prompt_index.py, and therefore covered by PROMPT_INDEX.json."
    ),
    "unindexed_domain_directories": (
        "domain-* directories absent from that allowlist. Their content does not "
        "appear in PROMPT_INDEX.json and is excluded from every indexed count above."
    ),
}


def compute_facts() -> dict[str, int]:
    inventory = _inventory()
    catalog, resources = _technique_catalog()

    # Cross-check the two independent resource counters against each other.
    for key, mine in (
        ("skills", inventory.skills_total),
        ("agents", inventory.agents_total),
        ("commands", inventory.commands_total),
    ):
        if resources[key] != mine:
            raise SystemExit(
                f"counter disagreement for {key}: inventory_counts={mine} "
                f"validate_technique_catalog={resources[key]}"
            )

    facts: dict[str, int] = {}
    facts.update(_index_partition())
    facts.update(
        {
            "skills": inventory.skills_total,
            "agents": inventory.agents_total,
            "commands": inventory.commands_total,
            "personas": resources["personas"],
            "active_techniques": catalog["active"],
            "catalogued_technique_ids": catalog["total"],
            "deprecated_technique_stubs": len(catalog["deprecated"]),
            "technique_categories": catalog["categories"],
        }
    )
    facts.update(_domain_directories())

    missing = sorted(set(facts) - set(DEFINITIONS))
    if missing:
        raise SystemExit(f"facts without a membership definition: {missing}")
    return facts


def render_artifact(facts: dict[str, int]) -> str:
    payload = {
        "schema": FACTS_SCHEMA,
        "definitions": {k: DEFINITIONS[k] for k in facts},
        "facts": facts,
    }
    return json.dumps(payload, indent=2, sort_keys=False) + "\n"


# --------------------------------------------------------------------------
# Generated documentation blocks
# --------------------------------------------------------------------------
def _declaration(keys: list[str], facts: dict[str, int]) -> str:
    payload = {k: facts[k] for k in keys}
    return f"<!-- REPO_FACTS_DECLARATION: {json.dumps(payload, sort_keys=True)} -->"


def _badge(label: str, value: str, color: str, link: str) -> str:
    safe_label = label.replace("-", "--").replace(" ", "_")
    safe_value = value.replace("-", "--").replace(" ", "_")
    return f"[![{label}](https://img.shields.io/badge/{safe_label}-{safe_value}-{color}.svg)]({link})"


def _render_headline(facts: dict[str, int]) -> tuple[list[str], str]:
    keys = [
        "domain_prompt_artifacts",
        "active_techniques",
        "skills",
        "agents",
        "commands",
        "personas",
        "indexed_artifacts",
    ]
    lines = [
        _badge(
            "domain prompts",
            str(facts["domain_prompt_artifacts"]),
            "orange",
            "PROMPT_INDEX.md",
        ),
        _badge(
            "techniques",
            str(facts["active_techniques"]),
            "purple",
            "techniques/MASTER_TECHNIQUE_INDEX.md",
        ),
        _badge(
            "skills",
            str(facts["skills"]),
            "blue",
            "domain-agentic-resources/skills/README.md",
        ),
        _badge(
            "agents",
            str(facts["agents"]),
            "blue",
            "domain-agentic-resources/agents/README.md",
        ),
        "",
        "| Registry facts | Count |",
        "|---|---|",
        f"| Domain prompts | {facts['domain_prompt_artifacts']} |",
        f"| Active techniques (across {facts['technique_categories']} categories) "
        f"| {facts['active_techniques']} |",
        f"| Skills | {facts['skills']} |",
        f"| Agents | {facts['agents']} |",
        f"| Commands | {facts['commands']} |",
        f"| Personas | {facts['personas']} |",
        f"| Bundled component files (attachments, not resources) "
        f"| {facts['bundled_component_files']} |",
        f"| Total indexed artifacts (all of the above kinds mixed) "
        f"| {facts['indexed_artifacts']} |",
        "",
        "Every number above is generated by `scripts/generate_repo_facts.py` and"
        " verified in CI. Each category's membership rule is stated in"
        " [`meta/REPOSITORY_FACTS.json`](meta/REPOSITORY_FACTS.json).",
    ]
    return keys, "\n".join(lines)


def _render_counts(facts: dict[str, int]) -> tuple[list[str], str]:
    keys = [
        "domain_prompt_artifacts",
        "domain_command_artifacts",
        "agentic_resource_artifacts",
        "bundled_component_files",
        "indexed_artifacts",
        "skills",
        "agents",
        "commands",
        "personas",
        "active_techniques",
        "technique_categories",
        "domain_directories",
        "unindexed_domain_directories",
    ]
    lines = [
        f"- **{facts['domain_prompt_artifacts']} domain prompts** across "
        f"{facts['domain_directories']} `domain-*` directories.",
        f"- **{facts['skills']} skills, {facts['agents']} agents, "
        f"{facts['commands']} commands, {facts['personas']} personas** under "
        "`domain-agentic-resources/`.",
        f"- **{facts['active_techniques']} active techniques** across "
        f"{facts['technique_categories']} categories in "
        "`techniques/MASTER_TECHNIQUE_INDEX.md`.",
        f"- `PROMPT_INDEX.json` holds **{facts['indexed_artifacts']} indexed "
        "artifacts**. That total is not a prompt count: it mixes the "
        f"{facts['domain_prompt_artifacts']} domain prompts with "
        f"{facts['domain_command_artifacts']} domain slash commands, "
        f"{facts['agentic_resource_artifacts']} agentic resources, and "
        f"{facts['bundled_component_files']} bundled component files "
        "(a parent resource's `references/`, `assets/`, `cards/` and similar).",
    ]
    unindexed = facts["unindexed_domain_directories"]
    if unindexed:
        lines.append(
            f"- **{unindexed} `domain-*` directories are outside the index "
            "allowlist** (`DOMAIN_DIRS` in `scripts/generate_prompt_index.py`) and "
            "are excluded from every count above."
        )
    else:
        lines.append(
            f"- All {facts['domain_directories']} `domain-*` directories are covered "
            "by the index allowlist (`DOMAIN_DIRS` in "
            "`scripts/generate_prompt_index.py`)."
        )
    return keys, "\n".join(lines)


BLOCKS: dict[str, dict] = {
    "headline": {"render": _render_headline, "docs": ["README.md"]},
    "counts": {
        "render": _render_counts,
        "docs": ["CLAUDE.md", "AGENTS.md", "START_HERE_FOR_AI.md"],
    },
}


def render_block(name: str, facts: dict[str, int]) -> str:
    keys, body = BLOCKS[name]["render"](facts)
    return "\n".join(
        [
            BEGIN_MARKER.format(name=name),
            _declaration(keys, facts),
            body,
            END_MARKER.format(name=name),
        ]
    )


def _block_pattern(name: str) -> re.Pattern[str]:
    return re.compile(BLOCK_RE_TMPL.format(name=re.escape(name)), re.S)


def required_documents() -> list[tuple[str, str]]:
    pairs = []
    for name, spec in BLOCKS.items():
        for doc in spec["docs"]:
            pairs.append((doc, name))
    return sorted(pairs)


def write_docs(facts: dict[str, int]) -> list[str]:
    changed = []
    for doc, name in required_documents():
        path = REPO_ROOT / doc
        text = path.read_text(encoding="utf-8")
        pattern = _block_pattern(name)
        if not pattern.search(text):
            raise SystemExit(
                f"{doc}: no REPO_FACTS block named '{name}'. Add the begin/end markers "
                f"before running --write."
            )
        new_text = pattern.sub(lambda _m: render_block(name, facts), text, count=1)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            changed.append(doc)
    return changed


def check_docs(facts: dict[str, int], errors: list[str]) -> None:
    for doc, name in required_documents():
        path = REPO_ROOT / doc
        if not path.exists():
            errors.append(f"{doc}: required document is missing")
            continue
        text = path.read_text(encoding="utf-8")

        match = _block_pattern(name).search(text)
        if not match:
            errors.append(
                f"{doc}: required generated block '{name}' is missing or its markers "
                f"were altered"
            )
            continue

        decl = DECL_RE.search(match.group("body"))
        if not decl:
            errors.append(f"{doc}: block '{name}' has no REPO_FACTS_DECLARATION")
            continue

        declared = json.loads(decl.group("json"))
        for key, value in sorted(declared.items()):
            if key not in facts:
                errors.append(f"{doc}: block '{name}' declares unknown fact '{key}'")
            elif facts[key] != value:
                errors.append(
                    f"{doc}: block '{name}' publishes {key}={value}, computed {facts[key]}"
                )

        expected = render_block(name, facts)
        if match.group(0) != expected:
            errors.append(
                f"{doc}: block '{name}' does not match its generated form "
                f"(hand-edited or stale) — run scripts/generate_repo_facts.py --write"
            )


def check_artifact(facts: dict[str, int], errors: list[str]) -> None:
    if not FACTS_PATH.exists():
        errors.append(f"{FACTS_PATH.relative_to(REPO_ROOT)}: canonical facts artifact is missing")
        return
    if FACTS_PATH.read_text(encoding="utf-8") != render_artifact(facts):
        errors.append(
            f"{FACTS_PATH.relative_to(REPO_ROOT)}: stale — "
            f"run scripts/generate_repo_facts.py --write"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--write", action="store_true", help="regenerate artifact and doc blocks")
    parser.add_argument("--check", action="store_true", help="verify artifact and doc blocks")
    parser.add_argument("--print", dest="show", action="store_true", help="print facts only")
    args = parser.parse_args()
    if not (args.write or args.check or args.show):
        parser.error("pass at least one of --write/--check/--print")

    facts = compute_facts()

    if args.show:
        for key, value in facts.items():
            print(f"{value:>8}  {key}")

    if args.write:
        FACTS_PATH.parent.mkdir(parents=True, exist_ok=True)
        FACTS_PATH.write_text(render_artifact(facts), encoding="utf-8")
        changed = write_docs(facts)
        print(f"Wrote {FACTS_PATH.relative_to(REPO_ROOT)}")
        print("Updated: " + (", ".join(changed) if changed else "no documents needed changes"))

    if args.check:
        errors: list[str] = []
        check_artifact(facts, errors)
        check_docs(facts, errors)
        if errors:
            raise SystemExit("\n".join(f"::error::{e}" for e in errors))
        print(
            f"Repository facts check passed "
            f"({len(facts)} facts, {len(required_documents())} generated blocks)."
        )


if __name__ == "__main__":
    main()
