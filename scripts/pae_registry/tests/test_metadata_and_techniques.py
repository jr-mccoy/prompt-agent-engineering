"""Adapters, degraded/minimal records, governance defaults, and the technique catalog."""

import re
import unittest
from pathlib import Path

from pae_registry import adapters, governance, techniques

REPO_ROOT = Path(__file__).resolve().parents[3]
TMP = REPO_ROOT / "meta" / "registry"


class AdapterTests(unittest.TestCase):
    def _write(self, name, text):
        path = TMP / name
        path.write_text(text, encoding="utf-8")
        self.addCleanup(path.unlink)
        return path

    def test_full_metadata(self):
        path = self._write(
            "_t_full.md",
            '---\ntitle: "A Prompt"\ndescription: "Does a thing."\ndifficulty: intermediate\n'
            "techniques:\n  - ST-01\n---\n\n# Heading\n",
        )
        norm = adapters.adapt("prompt", path, "x/_t_full.md", "_t_full")
        self.assertEqual(norm.metadata_completeness, "full")
        self.assertEqual(norm.title, "A Prompt")
        self.assertEqual(norm.description, "Does a thing.")
        self.assertEqual(norm.native["techniques"], ["ST-01"])
        self.assertEqual(norm.derived_fields, [])

    def test_minimal_record_derives_title_and_omits_description(self):
        path = self._write("_t_min.md", "# Real Title\n\nA first paragraph that must NOT become a description.\n")
        norm = adapters.adapt("prompt", path, "x/_t_min.md", "_t_min")
        self.assertEqual(norm.metadata_completeness, "minimal")
        self.assertEqual(norm.title, "Real Title")
        self.assertIn("title", norm.derived_fields)
        self.assertIsNone(norm.description, "a description must never be synthesized")

    def test_minimal_record_falls_back_to_the_slug(self):
        path = self._write("_t_noh1.md", "Just prose, no heading.\n")
        norm = adapters.adapt("prompt", path, "x/_t_noh1.md", "some_slug_here")
        self.assertEqual(norm.title, "Some Slug Here")
        self.assertIn("title", norm.derived_fields)

    def test_degraded_record_on_parse_failure_and_no_scavenging(self):
        path = self._write(
            "_t_bad.md",
            '---\nname: x\ndescription: Output is layered: setup, complications\n---\n\n# Body Title\n',
        )
        norm = adapters.adapt("skill", path, "x/_t_bad.md", "_t_bad")
        self.assertEqual(norm.metadata_completeness, "degraded")
        self.assertEqual(norm.diagnostics[0]["code"], "frontmatter_parse_failed")
        self.assertEqual(norm.native, {}, "no fields may be scavenged from unparseable YAML")
        self.assertIsNone(norm.description)
        self.assertEqual(norm.title, "Body Title")

    def test_absent_fields_are_omitted_not_nulled(self):
        path = self._write("_t_sparse.md", "---\ntitle: T\n---\n\nbody\n")
        norm = adapters.adapt("prompt", path, "x/_t_sparse.md", "_t_sparse")
        for key in ("techniques", "tags", "difficulty", "updated", "related"):
            self.assertNotIn(key, norm.native)

    def test_bundle_digest_is_order_independent(self):
        base = TMP
        files = sorted((REPO_ROOT / "meta" / "registry" / "schemas").glob("*.json"))
        first, _ = adapters.bundle_digest(files, base)
        second, _ = adapters.bundle_digest(list(reversed(files)), base)
        self.assertEqual(first, second)


class GovernanceTests(unittest.TestCase):
    def test_migration_defaults(self):
        gov = governance.default_governance()
        self.assertEqual(gov["maturity"], "experimental")
        self.assertEqual(gov["review_status"], "unknown")
        self.assertEqual(gov["eval_status"], "unknown")

    def test_no_quality_tier_is_ever_asserted(self):
        body = "This prompt follows the Tier 1 standard and is a Gold Standard example."
        assertions = governance.quality_assertions({}, body)
        self.assertEqual([a["scheme"] for a in assertions], [])

    def test_evidence_backed_assertions_only(self):
        assertions = governance.quality_assertions({"intended_use": "model-testing"}, "STRONG-GUARD here")
        self.assertEqual(
            sorted(a["scheme"] for a in assertions), ["guard-level", "intended-use"]
        )
        for assertion in assertions:
            self.assertTrue(assertion["evidence"])

    def test_model_testing_is_safety_gated(self):
        policy = governance.serving_policy(
            path="domain-x/y.md",
            frontmatter={"intended_use": "model-testing"},
            body="",
            metadata_completeness="full",
            maturity="experimental",
            license_status="resolved",
            provenance_origin="project_native",
        )
        self.assertEqual(policy["value"], "safety_gated")
        self.assertTrue(policy["guard_preservation"]["must_not_truncate"])

    def test_most_restrictive_policy_wins(self):
        policy = governance.serving_policy(
            path="domain-psychology/y.md",
            frontmatter={"intended_use": "model-testing"},
            body="STRONG-GUARD",
            metadata_completeness="degraded",
            maturity="experimental",
            license_status="resolved",
            provenance_origin="project_native",
        )
        self.assertEqual(policy["value"], "metadata_only")
        self.assertGreater(len(policy["basis"]), 1)

    def test_default_is_standard_and_fallback_is_fail_closed(self):
        policy = governance.serving_policy(
            path="domain-x/y.md",
            frontmatter={},
            body="",
            metadata_completeness="full",
            maturity="experimental",
            license_status="resolved",
            provenance_origin="project_native",
        )
        self.assertEqual(policy["value"], "standard")
        self.assertEqual(governance.DEFAULT_SERVING_POLICY, "metadata_only")

    def test_provenance_is_never_invented(self):
        prov, lic = governance.provenance_and_license("domain-x/y.md", {})
        self.assertEqual(prov["origin"], "project_native")
        self.assertEqual(lic["spdx"], "MIT")

        prov, lic = governance.provenance_and_license(
            "domain-agentic-resources/agents/backend/x.md", {}
        )
        self.assertEqual(prov["origin"], "adapted")
        self.assertEqual(lic["status"], "inherited")
        self.assertIn("no per-file map", lic["basis"])

    def test_vendored_upstream_is_read_from_metadata(self):
        prov, lic = governance.provenance_and_license(
            "domain-agentic-resources/skills/mobile-development/android-r8-analyzer/SKILL.md",
            {
                "metadata": {
                    "upstream": "https://github.com/android/skills",
                    "upstream-commit": "23d9eae21a4bfe0209e5b678f0ebe931e3c7dff4",
                    "author": "Google LLC",
                }
            },
        )
        self.assertEqual(prov["origin"], "vendored")
        self.assertEqual(prov["upstream"]["revision"], "23d9eae21a4bfe0209e5b678f0ebe931e3c7dff4")
        self.assertEqual(lic["spdx"], "Apache-2.0")
        self.assertEqual(lic["status"], "resolved")


class TechniqueTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records, cls.summary = techniques.technique_records(REPO_ROOT)

    def test_catalog_counts(self):
        self.assertEqual(self.summary["total"], 336)
        self.assertEqual(self.summary["active"], 327)
        self.assertEqual(self.summary["deprecated"], 9)
        self.assertEqual(self.summary["categories"], 18)

    def test_active_record(self):
        record = next(r for r in self.records if r["technique_id"] == "ST-01")
        self.assertEqual(record["state"], "active")
        self.assertEqual(record["category"], "ST")
        self.assertTrue(record["title"] and record["title"] != "ST-01")

    def test_deprecated_record_carries_its_merge_target(self):
        record = next(r for r in self.records if r["technique_id"] == "DD-01")
        self.assertEqual(record["state"], "deprecated")
        self.assertEqual(record["merged_into_technique"], "QA-08")

    def test_every_merge_target_resolves(self):
        known = {r["technique_id"] for r in self.records}
        for record in self.records:
            if record["merged_into_technique"]:
                self.assertIn(record["merged_into_technique"], known)

    def test_alias_is_reported_not_invented(self):
        self.assertEqual(self.summary["unresolved_aliases"], ["ST-26"])

    def test_detail_files_become_attachments(self):
        with_attachments = [r for r in self.records if r["attachments"]]
        self.assertEqual(len(with_attachments), 12)
        for record in with_attachments:
            self.assertTrue((REPO_ROOT / record["attachments"][0]).exists())

    # -- the GT / IPC validation gap ---------------------------------------
    def test_gt_and_ipc_are_catalogued(self):
        ids = {r["technique_id"] for r in self.records}
        self.assertIn("GT-01", ids)
        self.assertIn("IPC-14", ids)

    def test_reference_scanning_covers_every_catalogued_prefix(self):
        """The prefix list is derived, so a new category needs no second edit."""
        catalog = techniques.load_catalog(REPO_ROOT)
        pattern = _catalog_module(REPO_ROOT).id_token_pattern(catalog["prefixes"])
        for technique_id in ("GT-01", "IPC-14", "ST-01"):
            with self.subTest(technique_id=technique_id):
                self.assertEqual(pattern.findall(f"see {technique_id} here"), [technique_id])

    def test_a_hypothetical_new_prefix_needs_no_literal_edit(self):
        module = _catalog_module(REPO_ROOT)
        pattern = module.id_token_pattern({"ZZ"})
        self.assertEqual(pattern.findall("uses ZZ-07"), ["ZZ-07"])

    def test_phantom_references_are_still_caught(self):
        catalog = techniques.load_catalog(REPO_ROOT)
        pattern = _catalog_module(REPO_ROOT).id_token_pattern(catalog["prefixes"])
        found = set(pattern.findall("references GT-99 and IPC-99"))
        self.assertEqual(found - catalog["all_ids"], {"GT-99", "IPC-99"})


def _catalog_module(repo_root):
    import importlib.util
    import sys

    path = repo_root / "scripts" / "validate_technique_catalog.py"
    spec = importlib.util.spec_from_file_location("pae_vtc_test", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    unittest.main()
