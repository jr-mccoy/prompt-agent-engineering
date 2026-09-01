"""Behaviour against the repository's own registry, when one is present.

Synthetic fixtures cover the paths production does not have (aliases, excluded
resources, corruption). These tests cover the opposite risk: that the Engine
works on hand-made 7-record checkouts and not on the real 5,000-record one.

Skipped when run from an installed wheel with no checkout in reach, which is
exactly the situation the packaging smoke tests exercise separately.
"""

from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from pae_engine import Repository, RepositoryNotFound, validate_registry

ENGINE_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_ROOT.parent


def _repository():
    try:
        return Repository.at(REPO_ROOT)
    except (RepositoryNotFound, OSError):
        return None


class TestAgainstRealRegistry(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repository = _repository()
        if cls.repository is None:
            raise unittest.SkipTest("no PAE checkout alongside the engine")
        cls.registry = cls.repository.registry()

    def test_summary_is_readable_and_non_trivial(self) -> None:
        summary = self.registry.stats()
        self.assertGreater(summary.total_records, 1000)
        self.assertGreater(summary.by_lifecycle.get("live", 0), 0)
        self.assertIn("prompt", summary.by_kind)
        self.assertIn("technique", summary.by_kind)

    def test_summary_agrees_with_the_records(self) -> None:
        self.assertTrue(self.registry.stats(verify=True).verified)

    def test_uid_and_public_id_reach_the_same_record(self) -> None:
        sample = next(iter(self.registry.records()))
        by_id = self.registry.get(sample.id)
        by_uid = self.registry.get(sample.uid)
        self.assertEqual(by_id.uid, by_uid.uid)
        self.assertEqual(by_id.id, by_uid.id)

    def test_a_real_body_verifies_byte_for_byte(self) -> None:
        target = None
        for record in self.registry.records():
            if record.content_available:
                target = record
                break
        self.assertIsNotNone(target, "expected at least one servable resource")
        content = self.registry.content(target.id)
        digest = "sha256:" + hashlib.sha256(content.data).hexdigest()
        self.assertEqual(digest, target.content_sha256)
        self.assertEqual(content.byte_length, len(content.data))

    def test_techniques_have_no_addressable_body(self) -> None:
        from pae_engine import NoAddressableContent

        technique = next(r for r in self.registry.records() if r.kind == "technique")
        self.assertFalse(technique.has_body)
        with self.assertRaises(NoAddressableContent):
            self.registry.content(technique.id)

    def test_tombstones_keep_their_identity(self) -> None:
        tombstones = [r for r in self.registry.records() if r.lifecycle == "tombstone"]
        if not tombstones:
            self.skipTest("this checkout has no tombstones")
        record = self.registry.get(tombstones[0].uid)
        self.assertEqual(record.lifecycle, "tombstone")
        self.assertFalse(record.has_body)

    def test_the_committed_registry_passes_consumer_validation(self) -> None:
        report = validate_registry(self.repository)
        self.assertTrue(
            report.ok, msg="\n".join(i.message for i in report.issues[:20])
        )


if __name__ == "__main__":
    unittest.main()
