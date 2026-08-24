import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AGENTS_DIR = ROOT / "domain-agentic-resources" / "agents"
COMMANDS_DIR = ROOT / "domain-agentic-resources" / "commands"


class TestAnalysisSchema(unittest.TestCase):
    def test_agents_analysis_schema_and_parity(self):
        data = json.loads((AGENTS_DIR / "agents_analysis.json").read_text(encoding="utf-8"))

        self.assertIn("categories", data)
        self.assertIn("model_counts", data)
        self.assertIn("total_agents", data)
        self.assertIsInstance(data["categories"], dict)
        self.assertIsInstance(data["model_counts"], dict)
        self.assertIsInstance(data["total_agents"], int)

        required_keys = {
            "name": str,
            "description": str,
            "model": str,
            "file_path": str,
            "related_agents": list,
            "related_skills": list,
            "content_length": int,
            "category": str,
            "relative_path": str,
        }

        counted = 0
        for category, agents in data["categories"].items():
            self.assertIsInstance(category, str)
            self.assertIsInstance(agents, list)
            for agent in agents:
                counted += 1
                for key, expected_type in required_keys.items():
                    self.assertIn(key, agent)
                    self.assertIsInstance(agent[key], expected_type)

                self.assertRegex(agent["file_path"], r"^agents/.+\.md$")
                self.assertNotRegex(agent["file_path"], r"^/")
                self.assertEqual(agent["category"], category)
                self.assertEqual(agent["file_path"], f"agents/{agent['relative_path']}")

        self.assertEqual(counted, data["total_agents"])

        # Parity with filesystem scan: only markdown files with frontmatter are counted.
        frontmatter_agents = 0
        for md in AGENTS_DIR.rglob("*.md"):
            text = md.read_text(encoding="utf-8", errors="ignore")
            if text.startswith("---\n"):
                frontmatter_agents += 1
        self.assertEqual(counted, frontmatter_agents)

    def test_commands_analysis_schema_and_parity(self):
        data = json.loads((COMMANDS_DIR / "commands_analysis.json").read_text(encoding="utf-8"))

        self.assertIn("total_commands", data)
        self.assertIn("total_categories", data)
        self.assertIn("commands_by_category", data)
        self.assertIn("categories", data)
        self.assertIsInstance(data["commands_by_category"], dict)
        self.assertIsInstance(data["categories"], list)

        required_keys = {
            "name": str,
            "file_path": str,
            "category": str,
            "syntax": str,
            "description": str,
            "agents": list,
            "skills": list,
            "content_length": int,
        }

        counted = 0
        for category, commands in data["commands_by_category"].items():
            self.assertIsInstance(commands, list)
            for command in commands:
                counted += 1
                for key, expected_type in required_keys.items():
                    self.assertIn(key, command)
                    self.assertIsInstance(command[key], expected_type)

                self.assertRegex(command["file_path"], r"^commands/.+\.md$")
                self.assertNotRegex(command["file_path"], r"^/")
                self.assertTrue(command["syntax"].startswith("/"))
                self.assertEqual(command["category"], category)

        self.assertEqual(counted, data["total_commands"])
        self.assertEqual(len(data["commands_by_category"]), data["total_categories"])

        # Per-category README.md files are navigation, not commands. Count them
        # out so this parity check agrees with inventory_counts.py, which is the
        # authoritative counter for the agentic resource inventory.
        fs_count = sum(
            1 for p in COMMANDS_DIR.rglob("*.md") if p.name.lower() != "readme.md"
        )
        self.assertEqual(counted, fs_count)


if __name__ == "__main__":
    unittest.main()
