"""Packet export, manifests, composition plan and the dev/sealed firewall.

The export tests are written against the files on disk rather than the objects
that produced them. Auditing the intention proves nothing about the artefact
that actually gets handed over.
"""

from __future__ import annotations

import json
import unittest

from _support import TempDirCase

from pae_eval.authoring import audit, composition, masking, packets
from pae_eval.authoring.selection import Candidate, SelectedTarget, SelectionResult

BODY = """---
title: "Contract Risk Heatmap"
---

# Contract Risk Heatmap

## Objective

Score each clause on severity and likelihood.

## Limitations

Not a substitute for counsel.
"""


def _target(uid: str, kind: str, policy: str, task_class: str,
            rank: int) -> SelectedTarget:
    return SelectedTarget(
        candidate=Candidate(
            uid=uid, public_id=f"{kind}:legal/{uid}", kind=kind, scope="legal",
            cluster=uid, serving_policy=policy, source_path=f"{uid}.md",
            position=f"{rank:064d}",
        ),
        task_class=task_class, stratum=kind, rank=rank,
    )


class PacketCase(TempDirCase):

    def setUp(self) -> None:
        super().setUp()
        self.repo = self.tmp_path("repo")
        (self.repo / "meta" / "registry").mkdir(parents=True)
        (self.repo / "meta" / "registry" / "registry.jsonl").write_text(
            "", encoding="utf-8")

        self.targets = [
            _target("pae_aaa", "prompt", "safety_gated", "safety_gated", 0),
            _target("pae_bbb", "skill", "standard", "non_prompt_kind", 1),
        ]
        self.records = {}
        for target in self.targets:
            uid = target.candidate.uid
            (self.repo / f"{uid}.md").write_text(BODY, encoding="utf-8")
            self.records[uid] = {
                "uid": uid, "id": target.candidate.public_id,
                "kind": target.candidate.kind, "title": "Contract Risk Heatmap",
                "description": "Score clauses.",
                "source": {"path": f"{uid}.md"}, "aliases": [],
            }

        self.selection = SelectionResult(
            seed="sha256:deadbeef", target_pae_commit="c0ffee",
            algorithm_version="masked-target-selection/1",
            targets=tuple(self.targets), exclusions=(),
            population={"records_total": 2, "eligible": 2},
            kind_quotas={"prompt": 1, "skill": 1},
            class_quotas={"safety_gated": 1, "non_prompt_kind": 1},
            max_per_scope=4,
        )
        self.mappings, problems = packets.build_mappings(
            self.selection, self.records, self.repo)
        self.assertEqual(problems, [])

        self.author_root = self.tmp_path("author")
        self.reviewer_root = self.tmp_path("reviewer")
        self.author_digests = packets.build_author_packet(
            self.author_root, self.mappings)
        self.reviewer_digests = packets.build_reviewer_packet(
            self.reviewer_root, self.mappings, self.selection)


class TestPacketIds(unittest.TestCase):

    def test_ids_are_opaque_and_stable(self) -> None:
        targets = [_target(f"pae_{i:03d}", "prompt", "standard", "ordinary_task", i)
                   for i in range(5)]
        first = packets.assign_packet_ids(targets)
        second = packets.assign_packet_ids(list(reversed(targets)))
        self.assertEqual(first, second)
        self.assertEqual(sorted(first.values()),
                         [f"PKT-{i:04d}" for i in range(1, 6)])

    def test_ids_encode_no_part_of_the_uid(self) -> None:
        targets = [_target("pae_secretuid", "prompt", "standard", "ordinary_task", 0)]
        packet_id = packets.assign_packet_ids(targets)["pae_secretuid"]
        self.assertNotIn("secret", packet_id.casefold())

    def test_packet_order_is_not_the_draw_order(self) -> None:
        """Otherwise packet number would leak selection rank."""
        targets = [_target(f"pae_{i:03d}", "prompt", "standard", "ordinary_task", i)
                   for i in range(30)]
        assigned = packets.assign_packet_ids(targets)
        by_draw = [assigned[t.candidate.uid] for t in targets]
        self.assertNotEqual(by_draw, sorted(by_draw))


class TestAuthorExport(PacketCase):

    def test_required_structure_exists(self) -> None:
        for relative in ("READ_ME_FIRST.md", "AUTHOR_INSTRUCTIONS.md",
                         "NATURAL_TASK_BRIEF.md",
                         "natural-task-templates/README.md",
                         "masked-resource-packets/README.md",
                         "submission-template/README.md",
                         "submission-template/provenance.json"):
            with self.subTest(relative=relative):
                self.assertTrue((self.author_root / relative).is_file())

    def test_one_packet_file_per_target(self) -> None:
        files = sorted((self.author_root / "masked-resource-packets").glob("PKT-*.md"))
        self.assertEqual(len(files), len(self.targets))

    def test_packet_states_its_class_and_id(self) -> None:
        mapping = self.mappings[0]
        text = (self.author_root / "masked-resource-packets"
                / f"{mapping.packet_id}.md").read_text(encoding="utf-8")
        self.assertIn(mapping.packet_id, text)
        self.assertIn(mapping.task_class, text)

    def test_export_carries_no_target_identity(self) -> None:
        report = audit.audit_export(
            self.author_root,
            audit.target_identities(m.to_json_obj() for m in self.mappings),
        )
        self.assertTrue(report.passed, report.to_json_obj()["findings"])

    def test_refuses_to_write_into_a_non_empty_root(self) -> None:
        from pae_eval.errors import UsageError

        with self.assertRaises(UsageError):
            packets.build_author_packet(self.author_root, self.mappings)

    def test_guard_headings_survive_into_the_packet(self) -> None:
        text = (self.author_root / "masked-resource-packets"
                / f"{self.mappings[0].packet_id}.md").read_text(encoding="utf-8")
        self.assertIn("## Limitations", text)
        self.assertIn("Not a substitute for counsel.", text)


class TestReviewerExport(PacketCase):

    def test_mapping_is_present_and_complete(self) -> None:
        payload = json.loads(
            (self.reviewer_root / "target-map" / "packet-target-map.json")
            .read_text(encoding="utf-8"))
        self.assertEqual(payload["packet_count"], len(self.targets))
        uids = {p["target_uid"] for p in payload["packets"]}
        self.assertEqual(uids, {t.candidate.uid for t in self.targets})

    def test_integrity_hashes_recorded_for_every_packet(self) -> None:
        payload = json.loads(
            (self.reviewer_root / "target-map" / "packet-target-map.json")
            .read_text(encoding="utf-8"))
        for entry in payload["packets"]:
            self.assertTrue(entry["original_sha256"].startswith("sha256:"))
            self.assertTrue(entry["sanitized_sha256"].startswith("sha256:"))

    def test_exports_are_disjoint(self) -> None:
        self.assertEqual(
            audit.assert_disjoint(self.author_root, self.reviewer_root), [])


class TestManifests(PacketCase):

    def setUp(self) -> None:
        super().setUp()
        self.author_manifest = packets.author_manifest(
            repo=self.repo, selection=self.selection, mappings=self.mappings,
            digests=self.author_digests, created_at="2026-09-02T00:00:00+00:00")
        self.reviewer_manifest = packets.reviewer_manifest(
            repo=self.repo, selection=self.selection, mappings=self.mappings,
            digests=self.reviewer_digests, created_at="2026-09-02T00:00:00+00:00")

    def test_author_manifest_names_no_target(self) -> None:
        text = json.dumps(self.author_manifest)
        for target in self.targets:
            self.assertNotIn(target.candidate.uid, text)
            self.assertNotIn(target.candidate.public_id, text)
            self.assertNotIn(target.candidate.source_path, text)

    def test_author_manifest_carries_a_commitment_not_the_seed(self) -> None:
        """The seed plus the repo reproduces the mapping — see packets.py."""
        from pae_eval import canonical

        self.assertNotIn(self.selection.seed, json.dumps(self.author_manifest))
        self.assertEqual(self.author_manifest["selection_seed_commitment"],
                         canonical.sha256_text(self.selection.seed))

    def test_reviewer_manifest_carries_the_seed_and_it_verifies(self) -> None:
        from pae_eval import canonical

        seed = self.reviewer_manifest["selection_seed"]
        self.assertEqual(canonical.sha256_text(seed),
                         self.author_manifest["selection_seed_commitment"])

    def test_author_manifest_has_the_required_provenance_fields(self) -> None:
        for field in ("pae_commit", "registry_sha256", "selection_algorithm_version",
                      "eligible_population", "development_exclusion_sha256",
                      "packet_ids", "sanitized_packet_sha256",
                      "author_instructions_sha256", "natural_brief_sha256",
                      "created_at", "tool_version"):
            self.assertIn(field, self.author_manifest)

    def test_sidecar_digest_matches_the_bytes_written(self) -> None:
        from pae_eval import canonical

        path = self.tmp_path("author-packet-manifest.json")
        digest = packets.write_manifest(path, self.author_manifest)
        self.assertEqual(digest, canonical.sha256_file(path))
        sidecar = path.with_name(path.name + ".sha256")
        self.assertTrue(sidecar.read_text(encoding="utf-8").startswith(digest))


class TestCompositionPlan(unittest.TestCase):

    def test_masked_plus_natural_reconciles_to_the_sealed_target(self) -> None:
        reconciliation = composition.plan_reconciliation()
        self.assertTrue(reconciliation["reconciled"], reconciliation["problems"])
        self.assertEqual(reconciliation["sealed_total"], 150)
        self.assertEqual(reconciliation["masked_total"], 45)
        self.assertEqual(reconciliation["natural_total"], 105)

    def test_acceptance_checks_fail_a_thin_benchmark(self) -> None:
        class Task:
            acceptable_scopes = ("legal",)
            acceptable_resource_uids = ()
            leakage_audit: dict = {}

        checks = composition.acceptance_checks([Task()], {})
        failed = {c.name for c in checks if not c.passed}
        self.assertIn("distinct_scopes", failed)
        self.assertIn("multi_acceptable_tasks", failed)


class TestFirewall(unittest.TestCase):

    class Task:
        def __init__(self, task_id, query, deliverable, uids=()):
            self.task_id = task_id
            self.query = query
            self.deliverable = deliverable
            self.acceptable_resource_uids = tuple(
                type("R", (), {"uid": u})() for u in uids)

    def test_duplicate_task_text_is_caught(self) -> None:
        dev = [self.Task("d1", "Write   a plan", "A plan")]
        sealed = [self.Task("s1", "Write a plan", "A plan")]
        checks = composition.firewall_checks(dev, sealed)
        self.assertFalse(checks[0].passed)

    def test_reused_development_cluster_is_caught(self) -> None:
        sealed = [self.Task("s1", "q", "d", uids=["pae_copy"])]
        checks = composition.firewall_checks(
            [], sealed,
            development_clusters=["pae_canon"],
            sealed_clusters={"pae_copy": "pae_canon"},
        )
        self.assertFalse(checks[1].passed)

    def test_clean_sets_pass(self) -> None:
        dev = [self.Task("d1", "alpha", "one")]
        sealed = [self.Task("s1", "beta", "two", uids=["pae_x"])]
        checks = composition.firewall_checks(
            dev, sealed, development_clusters=["pae_y"],
            sealed_clusters={"pae_x": "pae_x"}, author_export_findings=0)
        self.assertTrue(all(c.passed for c in checks))


if __name__ == "__main__":
    unittest.main()
