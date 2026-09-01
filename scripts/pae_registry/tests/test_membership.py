"""Discovery must include real resources and exclude everything else."""

import unittest
from pathlib import Path, PurePosixPath

from pae_registry import membership as M

REPO_ROOT = Path(__file__).resolve().parents[3]


class DetectorTests(unittest.TestCase):
    def setUp(self):
        self.roots = frozenset(M.approved_roots(REPO_ROOT))

    def kind(self, path):
        return M.classify(PurePosixPath(path), self.roots)[0]

    def reason(self, path):
        return M.classify(PurePosixPath(path), self.roots)[2]

    # -- the regression this detector exists for ---------------------------
    def test_agents_documentation_category_is_retained(self):
        """`agents/documentation/` is a CATEGORY of documentation-writing agents.

        A bare-segment blocklist on "documentation" deletes it, along with five
        siblings. Exclusions must be anchored prefixes.
        """
        self.assertEqual(
            self.kind("domain-agentic-resources/agents/documentation/docs_architect.md"),
            "agent",
        )

    def test_commands_documentation_category_is_retained(self):
        self.assertEqual(
            self.kind("domain-agentic-resources/commands/documentation/doc_generate.md"),
            "command",
        )

    def test_documentation_root_is_excluded(self):
        """...while documentation ABOUT resources is excluded by prefix."""
        self.assertEqual(
            self.reason(
                "domain-agentic-resources/documentation/technique-analyses/skills/github_ops_analysis.md"
            ),
            "non_resource_prefix",
        )

    def test_all_six_recovered_resources_are_present(self):
        recovered = [
            "domain-agentic-resources/agents/documentation/api_documenter.md",
            "domain-agentic-resources/agents/documentation/docs_architect.md",
            "domain-agentic-resources/agents/documentation/mermaid_expert.md",
            "domain-agentic-resources/agents/documentation/reference_builder.md",
            "domain-agentic-resources/agents/documentation/tutorial_engineer.md",
            "domain-agentic-resources/commands/documentation/doc_generate.md",
        ]
        for path in recovered:
            with self.subTest(path=path):
                self.assertIsNotNone(self.kind(path))

    # -- kinds --------------------------------------------------------------
    def test_skill_manifest(self):
        self.assertEqual(
            self.kind("domain-agentic-resources/skills/marketing/revops/SKILL.md"), "skill"
        )

    def test_persona(self):
        self.assertEqual(
            self.kind("domain-agentic-resources/personas/design/design_visual_storyteller.md"),
            "persona",
        )

    def test_domain_command_outside_agentic_root(self):
        self.assertEqual(self.kind("domain-deep-analysis/commands/deepthink-problem.md"), "command")

    def test_prompt_fallback(self):
        self.assertEqual(
            self.kind("domain-reasoning-craft/reasoning-moves/reasoning_inversion.md"), "prompt"
        )

    # -- root toolkits ------------------------------------------------------
    def test_root_toolkit_resources_are_first_class(self):
        cases = {
            "childrens-book-studio/agents/childrens-book-orchestrator.md": "agent",
            "financial-records-toolkit/skills/divorce-financial-flagger/SKILL.md": "skill",
            "sourced-nonfiction-studio/commands/find-sources.md": "command",
            "ai-investment-research-toolkit/prompts/stage-4-screening.md": "prompt",
        }
        for path, expected in cases.items():
            with self.subTest(path=path):
                self.assertEqual(self.kind(path), expected)

    # -- exclusions ---------------------------------------------------------
    def test_bundled_components_excluded(self):
        self.assertEqual(
            self.reason("domain-agentic-resources/skills/x/y/references/guide.md"),
            "bundled_component",
        )

    def test_skill_bundle_extras_excluded(self):
        self.assertEqual(
            self.reason("domain-agentic-resources/skills/blockchain-web3/x/CHANGELOG.md"),
            "skill_bundle_attachment",
        )

    def test_sample_and_design_bundles_excluded(self):
        for path in (
            "agentic-system-factory/samples/bundle-pass/agents/worker.md",
            "childrens-book-studio/design-bundle/agents/craft-reviewer.md",
        ):
            with self.subTest(path=path):
                self.assertEqual(self.reason(path), "non_resource_prefix")

    def test_non_registry_roots_excluded(self):
        for path in (
            "authoring/NEW_PROMPT_TEMPLATE.md",
            "portable-prompt-system/techniques/tool_comparison.md",
            "continuity-kit/continuity_kit/templates/session.md",
            "techniques/security_checklist.md",
        ):
            with self.subTest(path=path):
                self.assertEqual(self.reason(path), "root_not_approved")

    def test_readmes_and_planning_docs_excluded(self):
        self.assertEqual(self.reason("domain-legal/README.md"), "meta_document")
        self.assertEqual(
            self.reason("domain-prompt-engineering/evaluation/_PLANNED_x.md"), "planning_document"
        )

    def test_skill_manifest_inside_component_dir_is_not_a_skill(self):
        self.assertIsNone(self.kind("domain-agentic-resources/skills/x/references/SKILL.md"))

    # -- totality and determinism ------------------------------------------
    def test_every_path_yields_exactly_one_outcome(self):
        candidates, exclusions = M.discover(REPO_ROOT)
        paths = [c.path for c in candidates] + [e.path for e in exclusions]
        self.assertEqual(len(paths), len(set(paths)), "a path was classified twice")
        for candidate in candidates:
            self.assertIn(candidate.kind, M.KINDS)

    def test_discovery_reconciles_with_repository_facts(self):
        """Independently computed counts must agree with meta/REPOSITORY_FACTS.json."""
        import json

        facts = json.loads((REPO_ROOT / "meta" / "REPOSITORY_FACTS.json").read_text())["facts"]
        candidates, _ = M.discover(REPO_ROOT)
        agentic = [c for c in candidates if c.path.startswith("domain-agentic-resources/")]
        for kind, key in (("skill", "skills"), ("agent", "agents"), ("command", "commands"), ("persona", "personas")):
            with self.subTest(kind=kind):
                self.assertEqual(
                    sum(1 for c in agentic if c.kind == kind), facts[key],
                    f"{kind} count diverged from REPOSITORY_FACTS.json",
                )

    def test_invalid_root_configuration_fails(self):
        with self.assertRaises(M.MembershipError):
            M.validate_roots(REPO_ROOT, ["domain-does-not-exist"])

    def test_approved_root_cannot_also_be_non_registry(self):
        with self.assertRaises(M.MembershipError):
            M.validate_roots(REPO_ROOT, ["authoring"])


if __name__ == "__main__":
    unittest.main()
