"""End-to-end generation: determinism, schema validity, and committed-artifact integrity."""

import json
import unittest
from pathlib import Path

from pae_registry import build as build_mod
from pae_registry import identity, schema as schema_mod

REPO_ROOT = Path(__file__).resolve().parents[3]
REGISTRY = REPO_ROOT / "meta" / "registry"


class GenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = build_mod.build(REPO_ROOT, REGISTRY)
        cls.outputs = build_mod.write_artifacts(REGISTRY, cls.result)
        cls.record_schema = schema_mod.load(REGISTRY / "schemas" / "registry-record.v1.schema.json")

    # -- determinism --------------------------------------------------------
    def test_regeneration_is_byte_identical(self):
        again = build_mod.build(REPO_ROOT, REGISTRY)
        self.assertEqual(build_mod.write_artifacts(REGISTRY, again), self.outputs)

    def test_committed_artifacts_are_current(self):
        for name, content in self.outputs.items():
            with self.subTest(artifact=name):
                self.assertEqual(
                    (REGISTRY / name).read_text(encoding="utf-8"),
                    content,
                    f"{name} is stale — run scripts/generate_registry.py --write",
                )

    def test_records_are_sorted_by_uid(self):
        uids = [r["uid"] for r in self.result.records]
        self.assertEqual(uids, sorted(uids))

    def test_diagnostics_are_sorted(self):
        keys = [(d.get("code", ""), d.get("uid", "")) for d in self.result.diagnostics]
        self.assertEqual(keys, sorted(keys))

    def test_no_timestamp_churn(self):
        """Generated artifacts carry no generation time, so diffs stay content-only."""
        blob = self.outputs["registry-summary.json"]
        for token in ("timestamp", "generated_at", '"generated"'):
            self.assertNotIn(token, blob.lower())

    def test_summary_is_stable_against_documentation_added_outside_approved_roots(self):
        """Adding an ADR or a README must not churn the registry summary."""
        scratch = REPO_ROOT / "meta" / "adr" / "_tmp_registry_stability_probe.md"
        scratch.write_text("# probe\n", encoding="utf-8")
        try:
            again = build_mod.build(REPO_ROOT, REGISTRY)
            self.assertEqual(again.summary, self.result.summary)
        finally:
            scratch.unlink()

    # -- schema -------------------------------------------------------------
    def test_every_record_is_schema_valid(self):
        for record in self.result.records:
            errors = schema_mod.validate(record, self.record_schema)
            self.assertEqual(errors, [], f"{record['id']}: {errors[:3]}")

    def test_ledger_and_records_are_bijective(self):
        ledger = {row.uid for row in self.result.identity_rows}
        records = {record["uid"] for record in self.result.records}
        self.assertEqual(ledger, records)

    def test_uid_and_public_id_uniqueness(self):
        uids = [r["uid"] for r in self.result.records]
        ids = [r["id"] for r in self.result.records]
        self.assertEqual(len(uids), len(set(uids)))
        self.assertEqual(len(ids), len(set(ids)))

    # -- content invariants -------------------------------------------------
    def test_every_record_has_a_serving_policy(self):
        for record in self.result.records:
            self.assertIn(record["serving_policy"]["value"], schema_mod.load(
                REGISTRY / "schemas" / "registry-record.v1.schema.json"
            )["properties"]["serving_policy"]["properties"]["value"]["enum"])

    def test_migration_defaults_hold_for_live_resources(self):
        live = [r for r in self.result.records if r["lifecycle"] == "live" and r["kind"] != "technique"]
        for record in live:
            self.assertEqual(record["governance"]["maturity"], "experimental")
            self.assertEqual(record["governance"]["review_status"], "unknown")
            self.assertEqual(record["governance"]["eval_status"], "unknown")

    def test_nothing_was_promoted(self):
        matured = [r for r in self.result.records if r["governance"]["maturity"] in {"candidate", "stable"}]
        self.assertEqual(matured, [])

    def test_no_tier_assertions(self):
        schemes = {a["scheme"] for r in self.result.records for a in r["quality"]}
        self.assertNotIn("prompt-quality-tier", schemes)

    def test_degraded_records_are_metadata_only(self):
        degraded = [r for r in self.result.records if r["metadata_completeness"] == "degraded"]
        self.assertEqual(len(degraded), 2)
        for record in degraded:
            self.assertEqual(record["serving_policy"]["value"], "metadata_only")
            self.assertTrue(any(d["code"] == "frontmatter_parse_failed" for d in record["diagnostics"]))

    def test_tombstones_are_deprecated_and_metadata_only(self):
        tombstones = [r for r in self.result.records if r["lifecycle"] == "tombstone"]
        self.assertEqual(len(tombstones), 45)
        for record in tombstones:
            self.assertEqual(record["governance"]["maturity"], "deprecated")
            self.assertEqual(record["serving_policy"]["value"], "metadata_only")
            self.assertNotIn("path", record["source"], "a tombstone must not claim a live file")
            rels = record["relationships"]
            self.assertTrue(
                rels["superseded_by"] or rels["merged_into"] or rels["split_into"],
                "a tombstone must record what replaced it",
            )

    def test_tombstone_is_a_different_identity_from_its_replacement(self):
        by_uid = {r["uid"]: r for r in self.result.records}
        for record in self.result.records:
            edge = record["relationships"]["superseded_by"] or record["relationships"]["merged_into"]
            if edge and edge["object_kind"] == "resource":
                self.assertNotEqual(edge["ref"], record["uid"])
                self.assertIn(edge["ref"], by_uid)

    def test_copy_edges_are_bidirectional_and_evidence_backed(self):
        by_uid = {r["uid"]: r for r in self.result.records}
        copies = [r for r in self.result.records if r["relationships"]["copy_of"]]
        self.assertEqual(len(copies), 59)
        for record in copies:
            canonical = by_uid[record["relationships"]["copy_of"]]
            self.assertIn(record["uid"], canonical["relationships"]["copies"])
        evidence = {row[4] for row in self.result.relationship_rows if row[1] == "copy_of"}
        self.assertEqual(evidence, {"meta/VENDORED.tsv"})

    def test_relationship_references_resolve(self):
        uids = {r["uid"] for r in self.result.records}
        for record in self.result.records:
            rels = record["relationships"]
            for ref in [rels["copy_of"], *rels["copies"], *rels["supersedes"], *rels["merges"]]:
                if ref:
                    self.assertIn(ref, uids)

    def test_expected_inventory(self):
        summary = self.result.summary
        self.assertEqual(summary["by_kind_live"], {
            "agent": 158, "command": 144, "persona": 53,
            "prompt": 4196, "skill": 339, "technique": 336,
        })
        self.assertEqual(summary["by_kind_tombstone"], {"prompt": 45})
        self.assertEqual(summary["total_records"], 5271)

    def test_summary_matches_the_records(self):
        summary = self.result.summary
        self.assertEqual(summary["total_records"], len(self.result.records))
        recomputed = {}
        for record in self.result.records:
            recomputed[record["kind"]] = recomputed.get(record["kind"], 0) + 1
        self.assertEqual(summary["by_kind"], dict(sorted(recomputed.items())))

    def test_skill_bundle_digest_matches_its_attachment_list(self):
        for record in self.result.records:
            if record["kind"] != "skill":
                continue
            self.assertEqual(
                record["source"]["bundle_file_count"],
                len(record["relationships"]["attachments"]) + 1,
                f"{record['id']}: bundle digest and attachment list disagree",
            )

    def test_techniques_have_no_source_block(self):
        for record in self.result.records:
            if record["kind"] == "technique":
                self.assertNotIn("source", record)
                self.assertEqual(record["defined_in"], "techniques/MASTER_TECHNIQUE_INDEX.md")


class FailureModeTests(unittest.TestCase):
    """Generation must abort rather than emit an untrustworthy registry."""

    def test_override_for_an_unknown_id_is_rejected(self):
        path = REGISTRY / "overrides" / "prompt.yaml"
        original = path.read_text(encoding="utf-8")
        path.write_text(
            "schema: pae-registry-overrides/1\noverrides:\n"
            "  prompt:does/not/exist:\n    governance:\n      maturity: stable\n",
            encoding="utf-8",
        )
        try:
            with self.assertRaises(build_mod.BuildError):
                build_mod.build(REPO_ROOT, REGISTRY)
        finally:
            path.write_text(original, encoding="utf-8")

    def test_override_of_the_wrong_kind_is_rejected(self):
        path = REGISTRY / "overrides" / "prompt.yaml"
        original = path.read_text(encoding="utf-8")
        path.write_text(
            "schema: pae-registry-overrides/1\noverrides:\n"
            "  skill:a/b:\n    governance:\n      maturity: stable\n",
            encoding="utf-8",
        )
        try:
            with self.assertRaises(build_mod.BuildError):
                build_mod.build(REPO_ROOT, REGISTRY)
        finally:
            path.write_text(original, encoding="utf-8")

    def test_schema_validator_rejects_malformed_records(self):
        record_schema = schema_mod.load(REGISTRY / "schemas" / "registry-record.v1.schema.json")
        result = build_mod.build(REPO_ROOT, REGISTRY)
        valid = json.loads(json.dumps(result.records[0]))
        self.assertEqual(schema_mod.validate(valid, record_schema), [])
        for mutate in (
            lambda r: r.update({"uid": "pae_BADUID"}),
            lambda r: r.update({"kind": "widget"}),
            lambda r: r["governance"].update({"maturity": "gold"}),
            lambda r: r.pop("serving_policy"),
            lambda r: r.update({"unexpected": 1}),
        ):
            broken = json.loads(json.dumps(valid))
            mutate(broken)
            with self.subTest(mutation=str(mutate)):
                self.assertTrue(schema_mod.validate(broken, record_schema))


if __name__ == "__main__":
    unittest.main()
