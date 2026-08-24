#!/usr/bin/env python3
"""Regenerate primary index files and run post-generation lint checks."""

from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(cmd: list[str]) -> None:
    print(f"\n$ {' '.join(cmd)}")
    subprocess.run(cmd, check=True, cwd=ROOT)


def main() -> int:
    run(["python3", "analyze_agents.py"])
    run(["python3", "generate_agent_readme.py"])
    run(["python3", "analyze_skills.py"])
    run(["python3", "generate_skills_readme.py"])
    run(["python3", "domain-agentic-resources/inventory_counts.py", "--write"])

    files = [
        "domain-agentic-resources/agents/README.md",
        "domain-agentic-resources/skills/README.md",
        "domain-agentic-resources/master_index.md",
    ]
    run([
        "python3",
        "domain-agentic-resources/lint_generated_indexes.py",
        *files,
    ])

    print("\n✅ Regeneration + lint completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
