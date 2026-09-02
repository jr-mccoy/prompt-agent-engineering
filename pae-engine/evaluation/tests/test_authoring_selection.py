"""Deterministic masked-target selection (spec §4).

Two properties carry the weight. **Determinism**: the same commit draws the
same 45 targets, so nobody can claim the mix was resampled until it looked
right. **Constraint satisfaction as a property of the algorithm**, not of a
manual fix afterwards — the scope floor and the per-scope cap are enforced
during the draw, so a selection that violates them cannot be produced.
"""

from __future__ import annotations

import unittest

from _support import REPO_ROOT, engine_available

from pae_eval.authoring import selection as sel


def _record(uid: str, *, kind: str = "prompt", policy: str = "standard",
            public_id: str | None = None, path: str = "",
            copy_of: str | None = None, lifecycle: str = "live") -> dict:
    return {
        "uid": uid,
        "id": public_id or f"{kind}:scope-a/{uid}",
        "kind": kind,
        "lifecycle": lifecycle,
        "serving_policy": {"value": policy},
        "relationships": {"copy_of": copy_of},
        "source": {"path": path},
        "title": uid,
        "description": "",
    }


class TestSeed(unittest.TestCase):

    def test_seed_is_a_pure_function_of_the_commit(self) -> None:
        a = sel.selection_seed("abc123")
        self.assertEqual(a, sel.selection_seed("abc123"))
        self.assertNotEqual(a, sel.selection_seed("abc124"))

    def test_seed_uses_the_specified_domain_prefix(self) -> None:
        import hashlib

        expected = hashlib.sha256(
            f"{sel.SEED_PREFIX}\nabc123".encode("utf-8")).hexdigest()
        self.assertEqual(sel.selection_seed("abc123"), f"sha256:{expected}")

    def test_empty_commit_is_refused(self) -> None:
        from pae_eval.errors import UsageError

        with self.assertRaises(UsageError):
            sel.selection_seed("   ")

    def test_draw_position_depends_on_both_seed_and_uid(self) -> None:
        self.assertNotEqual(sel.draw_position("s1", "u"), sel.draw_position("s2", "u"))
        self.assertNotEqual(sel.draw_position("s", "u1"), sel.draw_position("s", "u2"))


class TestScopeDerivation(unittest.TestCase):

    def test_agentic_resources_splits_one_level_deeper(self) -> None:
        record = _record("u", public_id="skill:agentic-resources/security/x")
        self.assertEqual(sel.derive_scope(record), "agentic-resources/security")

    def test_ordinary_scope_is_the_first_segment(self) -> None:
        record = _record("u", public_id="prompt:legal/contracts/x")
        self.assertEqual(sel.derive_scope(record), "legal")

    def test_technique_uses_its_category(self) -> None:
        record = _record("u", kind="technique", public_id="technique:ST-01")
        record["native"] = {"category": "ST"}
        self.assertEqual(sel.derive_scope(record), "st")

    @unittest.skipUnless(engine_available(), "Engine not installed")
    def test_agrees_with_the_engine_on_every_registry_record(self) -> None:
        """The local reimplementation must not drift from the Engine's.

        ``candidates`` and ``selection`` both derive scopes without importing
        the search layer. That duplication is deliberate, and this is what
        stops it becoming a second, quietly different definition of a scope.
        """
        from pae_engine._lexical import derive_scope as engine_derive_scope

        class Shim:
            def __init__(self, raw: dict) -> None:
                self.raw = raw
                self.kind = raw.get("kind", "")
                self.id = raw.get("id", "")

        records = sel.load_registry_records(REPO_ROOT)
        self.assertGreater(len(records), 100)
        mismatches = [
            r["uid"] for r in records
            if sel.derive_scope(r) != engine_derive_scope(Shim(r))
        ]
        self.assertEqual(mismatches, [], f"scope derivation drifted: {mismatches[:5]}")


class TestClusterKey(unittest.TestCase):

    def test_canonical_is_its_own_cluster(self) -> None:
        self.assertEqual(sel.cluster_key(_record("u1")), "u1")

    def test_copy_joins_its_canonical(self) -> None:
        self.assertEqual(sel.cluster_key(_record("u2", copy_of="u1")), "u1")


class TestEligibility(unittest.TestCase):

    def setUp(self) -> None:
        self.seed = sel.selection_seed("commit")

    def _run(self, records, **kwargs):
        return sel.eligible_candidates(records, REPO_ROOT, seed=self.seed, **kwargs)

    def test_tombstones_are_excluded(self) -> None:
        _, exclusions, _ = self._run([_record("u", lifecycle="tombstone")])
        self.assertEqual([e.reason for e in exclusions], ["not_live"])

    def test_techniques_are_excluded_for_having_no_addressable_body(self) -> None:
        _, exclusions, _ = self._run([_record("u", kind="technique")])
        self.assertEqual(exclusions[0].reason, "ineligible_kind")

    def test_metadata_only_is_excluded(self) -> None:
        _, exclusions, _ = self._run([_record("u", policy="metadata_only")])
        self.assertEqual(exclusions[0].reason, "serving_policy")

    def test_development_cluster_is_reserved(self) -> None:
        records = [_record("u2", copy_of="u1", path="README.md")]
        _, exclusions, _ = self._run(records, excluded_clusters=["u1"])
        self.assertEqual(exclusions[0].reason, "development_reserved_cluster")

    def test_missing_body_is_a_recorded_mechanical_exclusion(self) -> None:
        records = [_record("u", path="does/not/exist.md")]
        candidates, exclusions, _ = self._run(records)
        self.assertEqual(candidates, [])
        self.assertEqual(exclusions[0].reason, "unverified_body")
        self.assertIn("does not exist", exclusions[0].detail)

    def test_order_is_the_draw_order_not_the_input_order(self) -> None:
        records = [_record(f"u{i}", path="README.md") for i in range(20)]
        forward, _, _ = self._run(records)
        backward, _, _ = self._run(list(reversed(records)))
        self.assertEqual([c.uid for c in forward], [c.uid for c in backward])


@unittest.skipUnless((REPO_ROOT / "meta" / "registry" / "registry.jsonl").is_file(),
                     "Registry not present")
class TestSelectionAgainstTheRealRegistry(unittest.TestCase):
    """The selection that will actually be used, against the real corpus."""

    COMMIT = "e471d80e1a5ba557527db644f27ed17653f3fcab"

    @classmethod
    def setUpClass(cls) -> None:
        cls.records = sel.load_registry_records(REPO_ROOT)
        cls.result = sel.select_targets(cls.records, REPO_ROOT,
                                        target_pae_commit=cls.COMMIT)

    def test_selection_satisfies_every_requirement(self) -> None:
        self.assertEqual(list(self.result.problems), [])

    def test_is_reproducible(self) -> None:
        again = sel.select_targets(self.records, REPO_ROOT,
                                   target_pae_commit=self.COMMIT)
        self.assertEqual([t.candidate.uid for t in self.result.targets],
                         [t.candidate.uid for t in again.targets])

    def test_a_different_commit_draws_a_different_set(self) -> None:
        other = sel.select_targets(self.records, REPO_ROOT,
                                   target_pae_commit=self.COMMIT[::-1])
        self.assertNotEqual({t.candidate.uid for t in self.result.targets},
                            {t.candidate.uid for t in other.targets})

    def test_class_quotas_are_exact(self) -> None:
        composition = self.result.composition()
        self.assertEqual(composition["class_distribution"],
                         dict(sorted(sel.DEFAULT_CLASS_QUOTAS.items())))

    def test_every_safety_gated_packet_targets_a_safety_gated_resource(self) -> None:
        for target in self.result.targets:
            if target.task_class == "safety_gated":
                self.assertEqual(target.candidate.serving_policy, "safety_gated")

    def test_no_non_prompt_kind_packet_targets_a_prompt(self) -> None:
        for target in self.result.targets:
            if target.task_class == "non_prompt_kind":
                self.assertNotEqual(target.candidate.kind, "prompt")

    def test_scope_floor_and_cap(self) -> None:
        composition = self.result.composition()
        self.assertGreaterEqual(composition["distinct_scopes"],
                                sel.DEFAULT_MIN_DISTINCT_SCOPES)
        self.assertLessEqual(composition["max_scope_count"],
                             sel.DEFAULT_MAX_PER_SCOPE)

    def test_no_two_targets_share_a_cluster(self) -> None:
        clusters = [t.candidate.cluster for t in self.result.targets]
        self.assertEqual(len(set(clusters)), len(clusters))

    def test_excluded_clusters_are_never_drawn(self) -> None:
        reserved = {self.result.targets[0].candidate.cluster,
                    self.result.targets[1].candidate.cluster}
        constrained = sel.select_targets(
            self.records, REPO_ROOT, target_pae_commit=self.COMMIT,
            excluded_clusters=sorted(reserved),
        )
        drawn = {t.candidate.cluster for t in constrained.targets}
        self.assertEqual(drawn & reserved, set())
        self.assertEqual(list(constrained.problems), [])

    def test_public_summary_names_no_target(self) -> None:
        """A public report may describe the draw; it may not publish the key."""
        import json

        text = json.dumps(self.result.public_summary())
        for target in self.result.targets:
            self.assertNotIn(target.candidate.uid, text)
            self.assertNotIn(target.candidate.public_id, text)
            self.assertNotIn(target.candidate.source_path, text)

    def test_prompt_quota_must_match_the_safety_gated_class_quota(self) -> None:
        """The corpus fact that forces the kind allocation, asserted directly."""
        broken = sel.select_targets(
            self.records, REPO_ROOT, target_pae_commit=self.COMMIT,
            kind_quotas={**sel.DEFAULT_KIND_QUOTAS, "prompt": 12},
        )
        self.assertTrue(any("must equal the safety_gated class quota" in p
                            for p in broken.problems))


if __name__ == "__main__":
    unittest.main()
