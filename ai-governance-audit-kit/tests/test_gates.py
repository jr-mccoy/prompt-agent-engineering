#!/usr/bin/env python3
"""test_gates.py — prove the four gates in code, against the sample fixtures.

This kit reports structure. It does not review content, assert a quality tier,
assert a copy relationship, or determine a licence — and several of these tests
exist to keep it that way rather than to check that a number is right.

Run from the toolkit root:

    python3 -m unittest discover -s tests -v

The tests load each skill script directly from its path, so they exercise the
same code the pipeline runs — there is no separate test-only implementation of
any gate.
"""

from __future__ import annotations

import importlib.util
import json
import os
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAMPLES = ROOT / "samples"
CONFIG = ROOT / "config" / "audit.json"


def _load_module(name, relative):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


inventory = _load_module("inventory", "skills/corpus-inventory/scripts/inventory.py")
cluster = _load_module("cluster", "skills/duplication-clusters/scripts/cluster.py")
observed = _load_module("observed", "skills/observed-scoring/scripts/observed_score.py")
claim_guard = _load_module("claim_guard", "skills/claim-safety/scripts/claim_guard.py")
handback = _load_module("handback", "skills/registry-handback/scripts/handback.py")


def config():
    return json.loads(CONFIG.read_text(encoding="utf-8"))


def good_corpus():
    return str(SAMPLES / "corpus-good")


class SelfChecks(unittest.TestCase):
    """Every script ships its own regression suite; CI runs all five."""

    def test_inventory_self_check(self):
        self.assertTrue(inventory.self_check())

    def test_cluster_self_check(self):
        self.assertTrue(cluster.self_check())

    def test_observed_score_self_check(self):
        self.assertTrue(observed.self_check())

    def test_claim_guard_self_check(self):
        self.assertTrue(claim_guard.self_check())

    def test_handback_self_check(self):
        self.assertTrue(handback.self_check())


class Gate0Inventoriable(unittest.TestCase):

    def test_a_populated_corpus_passes(self):
        result = inventory.discover(good_corpus(), config())
        passed, unmet = inventory.gate_0(result)
        self.assertTrue(passed, unmet)
        self.assertEqual(result["by_kind"], {"prompt": 4, "skill": 2})

    def test_a_corpus_of_only_meta_documents_blocks(self):
        result = inventory.discover(str(SAMPLES / "corpus-empty"), config())
        passed, unmet = inventory.gate_0(result)
        self.assertFalse(passed)
        self.assertTrue(any("excluded" in reason for reason in unmet), unmet)

    def test_a_missing_root_blocks_rather_than_reporting_zero(self):
        cfg = config()
        cfg["membership"]["roots"] = ["does-not-exist"]
        result = inventory.discover(good_corpus(), cfg)
        passed, unmet = inventory.gate_0(result)
        self.assertFalse(passed)
        self.assertTrue(any("do not exist" in reason for reason in unmet), unmet)

    def test_exclusions_are_recorded_not_dropped(self):
        result = inventory.discover(good_corpus(), config())
        self.assertEqual(
            result["excluded"],
            {"non_resource_prefix": 2, "meta_document": 1, "bundled_component": 2},
        )


class MembershipInvariants(unittest.TestCase):
    """The prefixes-not-segments rule is enforced, not merely documented."""

    def test_a_bare_segment_exclusion_is_rejected(self):
        cfg = config()
        cfg["membership"]["non_resource_prefixes"] = ["documentation"]
        errors = inventory.validate_config(cfg)
        self.assertTrue(any("bare directory name" in e for e in errors), errors)

    def test_a_prefix_without_a_trailing_slash_is_rejected(self):
        cfg = config()
        cfg["membership"]["non_resource_prefixes"] = ["skills/_vendor"]
        errors = inventory.validate_config(cfg)
        self.assertTrue(any("must end with '/'" in e for e in errors), errors)

    def test_an_anchored_prefix_excludes_only_its_own_subtree(self):
        cfg = config()
        # The invariant's worked example: one 'documentation' tree is resources,
        # the other is documentation about them. Only the anchored one goes.
        cfg["membership"]["roots"] = ["agents", "documentation"]
        cfg["membership"]["non_resource_prefixes"] = ["documentation/"]
        kind, reason = inventory.classify("agents/documentation/writer.md", cfg)
        self.assertEqual(kind, "agent")
        self.assertIsNone(reason)
        kind, reason = inventory.classify("documentation/registry.md", cfg)
        self.assertIsNone(kind)
        self.assertEqual(reason, "non_resource_prefix")

    def test_the_fallback_detector_must_be_last(self):
        cfg = config()
        cfg["kind_detectors"] = [
            {"kind": "prompt", "fallback": True},
            {"kind": "skill", "basename": "SKILL.md"},
        ]
        errors = inventory.validate_config(cfg)
        self.assertTrue(any("must be last" in e for e in errors), errors)

    def test_exactly_one_fallback_is_required(self):
        cfg = config()
        cfg["kind_detectors"] = [{"kind": "skill", "basename": "SKILL.md"}]
        errors = inventory.validate_config(cfg)
        self.assertTrue(any("exactly one fallback" in e for e in errors), errors)


class Clustering(unittest.TestCase):

    def setUp(self):
        self.cfg = config()
        self.result = cluster.analyse(
            inventory.discover(good_corpus(), self.cfg), self.cfg
        )

    def test_byte_identical_files_are_an_exact_cluster(self):
        paths = {tuple(c["member_paths"]) for c in self.result["exact_clusters"]}
        self.assertIn(
            ("prompts/analysis_dependency_review.md",
             "prompts/analysis_dependency_review_copy.md"),
            paths,
        )

    def test_a_reworded_near_duplicate_is_a_candidate(self):
        pairs = {frozenset(c["member_paths"]) for c in self.result["candidate_clusters"]}
        self.assertIn(
            frozenset({"prompts/analysis_dependency_audit.md",
                       "prompts/analysis_dependency_review.md"}),
            pairs,
        )

    def test_an_unrelated_artifact_is_not_clustered(self):
        for entry in self.result["candidate_clusters"]:
            self.assertNotIn("prompts/analysis_incident_timeline.md", entry["member_paths"])

    def test_no_cluster_names_a_canonical(self):
        for entry in self.result["exact_clusters"] + self.result["candidate_clusters"]:
            self.assertIsNone(entry["canonical_uid"])
            self.assertIn("undetermined", entry["canonical_basis"])

    def test_similarity_is_the_conservative_direction(self):
        for entry in self.result["candidate_clusters"]:
            directional = entry["evidence"]["directional"]
            self.assertAlmostEqual(
                entry["similarity"], min(directional.values()), places=4
            )

    def test_raising_the_threshold_removes_candidates_not_exact_clusters(self):
        cfg = config()
        cfg["clustering"]["candidate_threshold"] = 0.99
        strict = cluster.analyse(inventory.discover(good_corpus(), cfg), cfg)
        self.assertEqual(strict["candidate_clusters"], [])
        self.assertEqual(len(strict["exact_clusters"]), 1)


class GateAScoreable(unittest.TestCase):

    def setUp(self):
        self.cfg = config()
        self.bundles = SAMPLES / "corpus-good" / "skills"

    def test_a_score_without_a_rubric_version_is_not_a_finding(self):
        record = json.loads((SAMPLES / "scores" / "score_no_rubric_version.json")
                            .read_text(encoding="utf-8"))
        passed, unmet = observed.gate_a(record)
        self.assertFalse(passed)
        self.assertTrue(any("rubric.version" in u for u in unmet), unmet)

    def test_a_score_without_provenance_is_not_a_finding(self):
        record = json.loads((SAMPLES / "scores" / "score_no_provenance.json")
                            .read_text(encoding="utf-8"))
        passed, unmet = observed.gate_a(record)
        self.assertFalse(passed)
        self.assertTrue(any("provenance" in u for u in unmet), unmet)

    def test_an_asserted_tier_is_refused(self):
        record = json.loads((SAMPLES / "scores" / "score_tier_asserted.json")
                            .read_text(encoding="utf-8"))
        passed, unmet = observed.gate_a(record)
        self.assertFalse(passed)
        self.assertTrue(any("tier" in u for u in unmet), unmet)

    def test_a_category_above_its_observable_maximum_is_refused(self):
        record = json.loads((SAMPLES / "scores" / "score_over_cap.json")
                            .read_text(encoding="utf-8"))
        passed, unmet = observed.gate_a(record)
        self.assertFalse(passed)
        self.assertTrue(any("observable maximum" in u for u in unmet), unmet)

    def test_the_produced_record_satisfies_its_own_gate(self):
        record = observed.score(str(self.bundles / "deploy-helper"), self.cfg)
        passed, unmet = observed.gate_a(record)
        self.assertTrue(passed, unmet)


class ObservedScoring(unittest.TestCase):

    def setUp(self):
        self.cfg = config()
        self.bundles = SAMPLES / "corpus-good" / "skills"

    def test_the_denominator_is_the_observable_subset_not_the_rubric(self):
        record = observed.score(str(self.bundles / "deploy-helper"), self.cfg)
        coverage = record["structural_coverage"]
        self.assertEqual(coverage["observable_max"], 54)
        self.assertEqual(coverage["rubric_max"], 100)
        self.assertLess(coverage["observable_max"], coverage["rubric_max"])

    def test_no_tier_is_ever_asserted(self):
        for name in ("deploy-helper", "release-notes"):
            record = observed.score(str(self.bundles / name), self.cfg)
            self.assertIsNone(record["tier"])
            self.assertIn("fabricat", record["tier_basis"])

    def test_a_blocking_security_finding_caps_the_verdict(self):
        record = observed.score(str(self.bundles / "release-notes"), self.cfg)
        self.assertEqual(record["verdict"], "blocked")
        codes = {f["check"] for f in record["blocking_findings"]}
        self.assertEqual(codes, set(observed.BLOCKING_CHECKS))

    def test_every_finding_names_a_location(self):
        record = observed.score(str(self.bundles / "release-notes"), self.cfg)
        for finding in record["findings"]:
            self.assertTrue(finding["path"])
            self.assertTrue(finding["detail"])

    def test_a_security_finding_names_its_file_and_line(self):
        record = observed.score(str(self.bundles / "release-notes"), self.cfg)
        details = " ".join(f["detail"] for f in record["blocking_findings"])
        self.assertIn("SKILL.md:", details)

    def test_an_iso_date_is_not_reported_as_a_contact_detail(self):
        # The regression that produced this test: `updated: "2026-06-18"` was
        # matched by an earlier phone-number pattern.
        record = observed.score(str(self.bundles / "deploy-helper"), self.cfg)
        self.assertEqual(record["blocking_findings"], [])

    def test_a_self_reported_block_is_never_merged_into_observed_scores(self):
        with tempfile.TemporaryDirectory() as staging:
            bundle = Path(staging) / "deploy-helper"
            shutil.copytree(self.bundles / "deploy-helper", bundle)
            skill = bundle / "SKILL.md"
            skill.write_text(
                skill.read_text(encoding="utf-8")
                + "\n<!-- RUBRIC cat1_metadata: 20 cat5_safety: 20 -->\n",
                encoding="utf-8",
            )
            record = observed.score(str(bundle), self.cfg)
        self.assertEqual(record["provenance"], "observed")
        self.assertEqual(record["self_reported"]["provenance"], "self_reported")
        self.assertLessEqual(record["scores"]["cat1_metadata"], 11)


class GateBClaimSafe(unittest.TestCase):

    def setUp(self):
        self.cfg = config()
        self.reports = SAMPLES / "reports"

    def _gate(self, name):
        return claim_guard.gate_b(str(self.reports / name), self.cfg)

    def test_a_clean_report_passes(self):
        passed, findings = self._gate("report_clean.md")
        self.assertTrue(passed, findings)

    def test_a_directional_word_beside_a_number_without_an_interval_blocks(self):
        passed, findings = self._gate("report_unlicensed_claim.md")
        self.assertFalse(passed)
        self.assertIn("unlicensed_direction", {f["rule"] for f in findings})

    def test_a_directional_word_with_no_number_is_not_blocked(self):
        # ADR-0040's rule is about a directional word with a number requiring
        # it. Blocking ordinary prose would get the gate switched off.
        with tempfile.TemporaryDirectory() as staging:
            report = Path(staging) / "prose.md"
            report.write_text(
                "# Report\n\nThis gate reduces the chance that an unbacked claim "
                "reaches a client.\n",
                encoding="utf-8",
            )
            passed, findings = claim_guard.gate_b(str(report), self.cfg)
        self.assertTrue(passed, findings)

    def test_an_asserted_tier_blocks(self):
        passed, findings = self._gate("report_tier_asserted.md")
        self.assertFalse(passed)
        self.assertIn("undisclosed_tier", {f["rule"] for f in findings})

    def test_fixture_figures_without_the_stamp_block(self):
        passed, findings = self._gate("report_missing_stamp.md")
        self.assertFalse(passed)
        self.assertIn("fixture_figure_unstamped", {f["rule"] for f in findings})

    def test_quantities_without_a_limitations_section_block(self):
        passed, findings = self._gate("report_no_limitations.md")
        self.assertFalse(passed)
        self.assertIn("missing_limitations", {f["rule"] for f in findings})

    def test_an_roi_claim_blocks(self):
        passed, findings = self._gate("report_roi_claim.md")
        self.assertFalse(passed)
        self.assertIn("roi_or_money_claim", {f["rule"] for f in findings})

    def test_the_sentences_adr_0040_forbids_by_name_block(self):
        passed, findings = self._gate("report_forbidden_sentence.md")
        self.assertFalse(passed)
        self.assertIn("forbidden_sentence", {f["rule"] for f in findings})

    def test_fenced_counterexamples_do_not_trip_the_gate(self):
        # Without this, the kit's own reference page could not be written.
        passed, findings = self._gate("report_fenced_counterexamples.md")
        self.assertTrue(passed, findings)

    def test_a_too_short_limitations_section_blocks(self):
        with tempfile.TemporaryDirectory() as staging:
            report = Path(staging) / "thin.md"
            report.write_text(
                "# Report\n\nOf 100 rubric points, 54 are observable.\n\n"
                "## Limitations\n\n- One caveat only.\n",
                encoding="utf-8",
            )
            passed, findings = claim_guard.gate_b(str(report), self.cfg)
        self.assertFalse(passed)
        self.assertIn("missing_limitations", {f["rule"] for f in findings})

    def test_every_finding_names_a_rule_and_a_location(self):
        _, findings = self._gate("report_unlicensed_claim.md")
        for finding in findings:
            self.assertTrue(finding["rule"])
            self.assertTrue(finding["path"])
            self.assertIn("line", finding)


class GateCHandback(unittest.TestCase):

    def setUp(self):
        self.cfg = config()
        _, self.clusters, self.scores, built = handback.produce(good_corpus(), self.cfg)
        self.records, self.summary = built

    def _staged(self):
        staging = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, staging, True)
        root = os.path.join(staging, "corpus")
        shutil.copytree(good_corpus(), root)
        handback.write_registry(root, self.records, self.summary)
        return root

    def test_the_unmodified_engine_opens_what_the_kit_wrote(self):
        root = self._staged()
        repository = handback.Repository.at(root)
        self.assertTrue(repository.registry_path.is_file())
        self.assertTrue(repository.summary_path.is_file())

    def test_engine_validation_is_the_gate(self):
        root = self._staged()
        passed, unmet, checked = handback.gate_c(root)
        self.assertTrue(passed, unmet)
        self.assertEqual(checked["records"], len(self.records))
        self.assertEqual(checked["unique_uids"], len(self.records))

    def test_a_tampered_checksum_is_caught(self):
        root = self._staged()
        path = os.path.join(root, handback.REGISTRY_RELPATH)
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()
        first = json.loads(lines[0])
        first["source"]["content_sha256"] = "sha256:" + "0" * 64
        lines[0] = json.dumps(first, sort_keys=True) + "\n"
        with open(path, "w", encoding="utf-8") as fh:
            fh.writelines(lines)
        passed, unmet, _ = handback.gate_c(root)
        self.assertFalse(passed)
        self.assertTrue(any("checksum_mismatch" in u for u in unmet), unmet)

    def test_a_missing_marker_file_blocks(self):
        root = self._staged()
        os.remove(os.path.join(root, handback.SUMMARY_RELPATH))
        passed, unmet, _ = handback.gate_c(root)
        self.assertFalse(passed)
        self.assertTrue(any("marker file missing" in u for u in unmet), unmet)

    def test_a_dry_run_leaves_the_corpus_untouched(self):
        before = sorted(p.name for p in Path(good_corpus()).iterdir())
        handback.run_one(good_corpus(), self.cfg, write=False)
        after = sorted(p.name for p in Path(good_corpus()).iterdir())
        self.assertEqual(before, after)
        self.assertNotIn("meta", after)

    def test_an_un_inventoriable_corpus_never_reaches_a_registry(self):
        inventoried, clusters, scores, built = handback.produce(
            str(SAMPLES / "corpus-empty"), self.cfg
        )
        self.assertIsNone(built)
        self.assertFalse(inventoried["gate_0"]["passed"])


class NothingIsInvented(unittest.TestCase):
    """The refusals are the product. These tests are the product's warranty."""

    def setUp(self):
        _, self.clusters, self.scores, built = handback.produce(good_corpus(), config())
        self.records, self.summary = built

    def test_no_record_asserts_a_copy_edge(self):
        self.assertEqual(handback.assert_nothing_invented(self.records), [])
        for record in self.records:
            self.assertIsNone(record["relationships"]["copy_of"])
            self.assertEqual(record["relationships"]["copies"], [])

    def test_duplicate_findings_ride_as_diagnostics_with_evidence(self):
        codes = {
            diagnostic["code"]
            for record in self.records
            for diagnostic in record["diagnostics"]
        }
        self.assertIn("exact_duplicate_detected", codes)
        self.assertIn("near_duplicate_candidate", codes)

    def test_no_record_asserts_a_review_status_or_a_tier(self):
        for record in self.records:
            self.assertEqual(record["governance"]["review_status"], "unknown")
            self.assertEqual(record["governance"]["eval_status"], "unknown")
            for assertion in record["quality"]:
                self.assertNotEqual(assertion["scheme"], "prompt-quality-tier")

    def test_no_record_asserts_a_licence(self):
        for record in self.records:
            self.assertEqual(record["license"]["status"], "unresolved")

    def test_an_observed_score_declares_how_it_was_obtained(self):
        assertions = [a for r in self.records for a in r["quality"]]
        self.assertTrue(assertions)
        for assertion in assertions:
            self.assertEqual(assertion["scheme"], "structural-coverage-observed")
            self.assertIn("observed by detector", assertion["evidence"])
            self.assertIn("mechanically observable", assertion["evidence"])

    def test_the_summary_discloses_that_governance_is_unknown_by_construction(self):
        self.assertIn("unknown by construction", self.summary["audit"]["disclosure"])
        self.assertEqual(self.summary["by_review_status"], {"unknown": len(self.records)})


if __name__ == "__main__":
    unittest.main()
