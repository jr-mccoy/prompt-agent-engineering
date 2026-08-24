#!/usr/bin/env python3
"""Single source of truth inventory for agents, skills, and commands.

Scans:
- domain-agentic-resources/agents/**/*.md (excluding README.md)
- domain-agentic-resources/skills/**/SKILL.md
- domain-agentic-resources/commands/**/*.md (excluding README.md)

Can update declared counts in index files and verify they match.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AGENTS_DIR = ROOT / "agents"
SKILLS_DIR = ROOT / "skills"
COMMANDS_DIR = ROOT / "commands"

MASTER_INDEX = ROOT / "master_index.md"
AGENTS_README = ROOT / "agents" / "README.md"
SKILLS_README = ROOT / "skills" / "README.md"
COMMANDS_README = ROOT / "commands" / "README.md"

DECL_RE = re.compile(r"<!-- INVENTORY_COUNTS: (?P<json>\{.*\}) -->")


@dataclass
class Inventory:
    agents_total: int
    skills_total: int
    commands_total: int
    agents_categories: dict[str, int]
    skills_categories: dict[str, int]
    commands_categories: dict[str, int]



def _count_agents() -> tuple[int, dict[str, int]]:
    files = [p for p in AGENTS_DIR.glob("**/*.md") if p.name.lower() != "readme.md"]
    by_category = Counter(p.parent.name for p in files)
    return len(files), dict(sorted(by_category.items()))


def _count_skills() -> tuple[int, dict[str, int]]:
    files = list(SKILLS_DIR.glob("**/SKILL.md"))
    by_category = Counter(p.parent.parent.name for p in files)
    return len(files), dict(sorted(by_category.items()))


def _count_commands() -> tuple[int, dict[str, int]]:
    files = [p for p in COMMANDS_DIR.glob("**/*.md") if p.name.lower() != "readme.md"]
    by_category = Counter(p.parent.name for p in files)
    return len(files), dict(sorted(by_category.items()))


def compute_inventory() -> Inventory:
    at, ac = _count_agents()
    st, sc = _count_skills()
    ct, cc = _count_commands()
    return Inventory(at, st, ct, ac, sc, cc)


def _inventory_comment(payload: dict) -> str:
    return f"<!-- INVENTORY_COUNTS: {json.dumps(payload, sort_keys=True)} -->"


def _upsert_inventory_comment(text: str, payload: dict) -> str:
    line = _inventory_comment(payload)
    if DECL_RE.search(text):
        return DECL_RE.sub(line, text, count=1)
    return line + "\n\n" + text


def _replace(pattern: str, repl: str, text: str) -> str:
    return re.sub(pattern, repl, text, count=1, flags=re.MULTILINE)


def _replace_category_toc(text: str, categories: dict[str, int], unit: str) -> str:
    lines = ["**By Category:**"]
    for cat, count in sorted(categories.items()):
        disp = cat.replace("-", " ").title()
        anchor = cat.lower()
        lines.append(f"- [{disp}](#{anchor}) ({count} {unit})")
    block = "\n".join(lines)
    return re.sub(r"\*\*By Category:\*\*[\s\S]*?(?=\n## )", block + "\n\n", text, count=1)


def update_files(inv: Inventory) -> None:
    today = date.today().isoformat()

    # master_index.md
    m = MASTER_INDEX.read_text(encoding="utf-8")
    m = _upsert_inventory_comment(
        m,
        {
            "type": "master",
            "date": today,
            "total_resources": inv.agents_total + inv.skills_total + inv.commands_total,
            "agents_total": inv.agents_total,
            "skills_total": inv.skills_total,
            "commands_total": inv.commands_total,
            "agents_categories": inv.agents_categories,
            "skills_categories": inv.skills_categories,
            "commands_categories": inv.commands_categories,
        },
    )
    m = _replace(r"\*\*Quick searchable reference for all .* resources in this directory\.\*\*", f"**Quick searchable reference for all {inv.agents_total + inv.skills_total + inv.commands_total} resources in this directory.**", m)
    m = _replace(r"\*\*Last Updated:\*\* .*", f"**Last Updated:** {today}", m)
    m = _replace(r"\*\*Total Resources:\*\* .*", f"**Total Resources:** {inv.agents_total + inv.skills_total + inv.commands_total} ({inv.agents_total} agents + {inv.skills_total} skills + {inv.commands_total} commands)", m)
    m = _replace(r"\| \[\*\*Agents\*\*\]\(#agent-index\) \| .*", f"| [**Agents**](#agent-index) | {inv.agents_total} | Parallel workers with model assignments |", m)
    m = _replace(r"\| \[\*\*Skills\*\*\]\(#skill-index\) \| .*", f"| [**Skills**](#skill-index) | {inv.skills_total} | Domain containers with workflows |", m)
    m = _replace(r"\| \[\*\*Commands\*\*\]\(#command-index\) \| .*", f"| [**Commands**](#command-index) | {inv.commands_total} | Slash commands in `commands/` (workflow commands are a subset, not additional) |", m)
    m = _replace(r"\*\*Total:\*\* .* agents across .* categories", f"**Total:** {inv.agents_total} agents across {len(inv.agents_categories)} categories", m)
    m = _replace(r"\*\*Total:\*\* .* skills across .* categories", f"**Total:** {inv.skills_total} skills across {len(inv.skills_categories)} categories", m)
    m = _replace(r"\*\*Total:\*\* .*commands.*", f"**Total:** {inv.commands_total} commands across {len(inv.commands_categories)} categories", m)

    cmd_def = (
        "## Command Counting Definition\n\n"
        "- **Command:** any Markdown file under `domain-agentic-resources/commands/**/*.md`, excluding category `README.md` files.\n"
        "- **Workflow command:** a command subtype (typically in orchestration/multi-agent categories). It is **included within** the command total and is never counted separately.\n"
    )
    if "## Command Counting Definition" in m:
        m = re.sub(r"## Command Counting Definition[\s\S]*?(?=\n## )", cmd_def + "\n", m, count=1)
    else:
        m = m.replace("## Command Index", cmd_def + "\n## Command Index", 1)

    MASTER_INDEX.write_text(m, encoding="utf-8")

    # agents readme
    a = AGENTS_README.read_text(encoding="utf-8")
    a = _upsert_inventory_comment(
        a,
        {"type": "agents", "date": today, "total": inv.agents_total, "categories": inv.agents_categories},
    )
    a = _replace(r"\*\*Comprehensive index of .* specialized Claude Code agents organized by domain\.\*\*", f"**Comprehensive index of {inv.agents_total} specialized Claude Code agents organized by domain.**", a)
    a = _replace(r"This directory contains \*\*.* specialized AI agents\*\*", f"This directory contains **{inv.agents_total} specialized AI agents**", a)
    a = _replace(r"- \*\*Total Agents:\*\* .*", f"- **Total Agents:** {inv.agents_total}", a)
    a = _replace(r"- \*\*Categories:\*\* .*", f"- **Categories:** {len(inv.agents_categories)}", a)
    a = _replace_category_toc(a, inv.agents_categories, "agents")
    AGENTS_README.write_text(a, encoding="utf-8")

    # skills readme
    s = SKILLS_README.read_text(encoding="utf-8")
    s = _upsert_inventory_comment(
        s,
        {"type": "skills", "date": today, "total": inv.skills_total, "categories": inv.skills_categories},
    )
    s = _replace(r"\*\*Comprehensive index of .* Claude Code skills organized by domain\.\*\*", f"**Comprehensive index of {inv.skills_total} Claude Code skills organized by domain.**", s)
    s = _replace(r"This directory contains \*\*.* specialized skills\*\*", f"This directory contains **{inv.skills_total} specialized skills**", s)
    s = _replace(r"- \*\*Total Skills:\*\* .*", f"- **Total Skills:** {inv.skills_total}", s)
    s = _replace(r"- \*\*Categories:\*\* .*", f"- **Categories:** {len(inv.skills_categories)}", s)
    s = _replace_category_toc(s, inv.skills_categories, "skills")
    SKILLS_README.write_text(s, encoding="utf-8")

    # commands readme
    c = COMMANDS_README.read_text(encoding="utf-8")
    c = _upsert_inventory_comment(
        c,
        {"type": "commands", "date": today, "total": inv.commands_total, "categories": inv.commands_categories},
    )
    c = _replace(r"\*\*Total Commands:\*\* .*", f"**Total Commands:** {inv.commands_total} across {len(inv.commands_categories)} categories", c)
    c = _replace(r"\*\*Last Updated:\*\* .*", f"**Last Updated:** {today}", c)

    canon = (
        "## Command Counting Definition\n\n"
        "- **Command:** any Markdown file under `domain-agentic-resources/commands/**/*.md`, excluding category `README.md` files.\n"
        "- **Workflow command:** a command subtype used for multi-step orchestration. Workflow commands are **not** added on top of command totals.\n\n"
    )
    if "## Command Counting Definition" in c:
        c = re.sub(r"## Command Counting Definition[\s\S]*?(?=\n## )", canon, c, count=1)
    else:
        c = c.replace("## What Are Commands?", canon + "## What Are Commands?", 1)

    c = _replace_commands_category_table(c, inv.commands_categories)
    COMMANDS_README.write_text(c, encoding="utf-8")




def _replace_commands_category_table(text: str, categories: dict[str, int]) -> str:
    rows = ["| Category | Count | Description |", "|----------|-------|-------------|"]
    for cat, count in sorted(categories.items(), key=lambda kv: (-kv[1], kv[0])):
        disp = cat.replace("-", " ").title()
        rows.append(f"| {disp} | {count} | Various development commands |")
    block = "\n".join(rows)
    return re.sub(r"\| Category \| Count \| Description \|\n\|----------\|-------\|-------------\|[\s\S]*?(?=\n## Quick Reference by Category)", block + "\n", text, count=1)

def extract_decl(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = DECL_RE.search(text)
    if not m:
        raise ValueError(f"Missing INVENTORY_COUNTS declaration: {path}")
    return json.loads(m.group("json"))


def check_files(inv: Inventory) -> None:
    checks = {
        MASTER_INDEX: {
            "total_resources": inv.agents_total + inv.skills_total + inv.commands_total,
            "agents_total": inv.agents_total,
            "skills_total": inv.skills_total,
            "commands_total": inv.commands_total,
            "agents_categories": inv.agents_categories,
            "skills_categories": inv.skills_categories,
            "commands_categories": inv.commands_categories,
        },
        AGENTS_README: {"total": inv.agents_total, "categories": inv.agents_categories},
        SKILLS_README: {"total": inv.skills_total, "categories": inv.skills_categories},
        COMMANDS_README: {"total": inv.commands_total, "categories": inv.commands_categories},
    }

    errors = []
    for path, expected in checks.items():
        declared = extract_decl(path)
        for key, value in expected.items():
            if declared.get(key) != value:
                errors.append(f"{path}: key '{key}' mismatch. declared={declared.get(key)!r} expected={value!r}")

    if errors:
        raise SystemExit("\n".join(errors))


def main() -> None:
    parser = argparse.ArgumentParser(description="Inventory counter and validator")
    parser.add_argument("--write", action="store_true", help="Update declared counts and top-level totals")
    parser.add_argument("--check", action="store_true", help="Check declared counts against computed inventory")
    args = parser.parse_args()

    if not args.write and not args.check:
        parser.error("Pass at least one of --write/--check")

    inv = compute_inventory()
    if args.write:
        update_files(inv)
    if args.check:
        check_files(inv)
        print("Inventory check passed.")


if __name__ == "__main__":
    main()
