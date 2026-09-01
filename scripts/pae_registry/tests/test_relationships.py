"""Reorg semantics stay distinct; copy edges come only from explicit evidence."""

import unittest
from pathlib import Path

from pae_registry import membership as M
from pae_registry import relationships as R

REPO_ROOT = Path(__file__).resolve().parents[3]


class ReorgParsingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = R.load_reorg(REPO_ROOT / "meta" / "REORG_MAP.tsv")
        cls.candidates = {c.path for c in M.discover(REPO_ROOT)[0]}

    def test_four_semantics_are_parsed_separately(self):
        predicates = {}
        for relation in self.model.relations:
            predicates[relation.predicate] = predicates.get(relation.predicate, 0) + 1
        self.assertEqual(len(self.model.moves), 236)
        self.assertEqual(predicates.get("superseded-by"), 43)
        self.assertEqual(predicates.get("merged-into"), 7)
        self.assertEqual(predicates.get("split-into"), 1)

    def test_moves_are_not_relations(self):
        """A move preserves identity and must never become a replacement edge."""
        for relation in self.model.relations:
            self.assertNotIn(relation.old_path, self.model.moves)

    def test_chain_resolution_through_a_moved_target(self):
        """8 supersession targets were themselves moved afterwards."""
        chained = [
            r for r in self.model.relations if r.raw_target.rstrip("/") in self.model.moves
        ]
        self.assertEqual(len(chained), 8)
        for relation in chained:
            resolved = self.model.resolve(relation.raw_target)
            self.assertNotEqual(resolved, relation.raw_target)
            self.assertTrue((REPO_ROOT / resolved.rstrip("/")).exists())

    def test_no_cycles_and_every_target_resolves(self):
        for old in self.model.moves:
            self.model.resolve(old)  # raises on a cycle
        for relation in self.model.relations:
            kind, _ = R.classify_target(
                REPO_ROOT, self.model.resolve(relation.raw_target), lambda p: p in self.candidates
            )
            self.assertIn(kind, {"resource", "document", "collection"})

    def test_cycle_is_a_hard_error(self):
        model = R.ReorgModel(moves={"a.md": "b.md", "b.md": "a.md"})
        with self.assertRaises(R.RelationshipError):
            model.resolve("a.md")

    def test_unknown_predicate_is_rejected(self):
        path = REPO_ROOT / "meta" / "registry" / "_tmp_reorg.tsv"
        path.write_text("old.md\tDELETED renamed-to:new.md\n", encoding="utf-8")
        try:
            with self.assertRaises(R.RelationshipError):
                R.load_reorg(path)
        finally:
            path.unlink()

    def test_missing_target_is_a_hard_error(self):
        with self.assertRaises(R.RelationshipError):
            R.classify_target(REPO_ROOT, "domain-nowhere/nothing.md", lambda p: False)

    def test_target_typing(self):
        self.assertEqual(
            R.classify_target(REPO_ROOT, "domain-engineering-workflows/workflows/", lambda p: False)[0],
            "collection",
        )
        self.assertEqual(
            R.classify_target(REPO_ROOT, "domain-productivity/README.md", lambda p: False)[0],
            "document",
        )
        self.assertEqual(
            R.classify_target(REPO_ROOT, "x.md", lambda p: p == "x.md")[0], "resource"
        )


class VendoredTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pairs = R.load_vendored(REPO_ROOT / "meta" / "VENDORED.tsv")
        cls.candidates = {c.path for c in M.discover(REPO_ROOT)[0]}

    def test_registry_visible_edges(self):
        visible = [p for p in self.pairs if p.canonical in self.candidates and p.copy in self.candidates]
        self.assertEqual(len(self.pairs), 154)
        self.assertEqual(len(visible), 59)

    def test_adapted_copies_are_kept_distinct_from_their_canonical(self):
        """22 of the 59 registry-visible copies genuinely differ; that is expected."""
        import hashlib

        def digest(path):
            return hashlib.sha256((REPO_ROOT / path).read_bytes()).hexdigest()

        visible = [p for p in self.pairs if p.canonical in self.candidates and p.copy in self.candidates]
        adapted = [p for p in visible if digest(p.canonical) != digest(p.copy)]
        self.assertEqual(len(adapted), 22)

    def test_unregistered_near_duplicates_are_not_collapsed(self):
        """These adapted trees are documented as NOT mirrors and must stay separate."""
        registered = {(p.canonical, p.copy) for p in self.pairs} | {
            (p.copy, p.canonical) for p in self.pairs
        }
        pairs_that_must_not_be_linked = [
            (
                "childrens-book-studio/agents/nonfiction-accuracy-checker.md",
                "childrens-book-studio/design-bundle/agents/nonfiction-accuracy-checker.md",
            ),
        ]
        for a, b in pairs_that_must_not_be_linked:
            with self.subTest(pair=(a, b)):
                self.assertNotIn((a, b), registered)
                self.assertNotIn(b, self.candidates, "the design-bundle draft must not be a resource")

    def test_no_byte_identical_group_lacks_an_explicit_edge(self):
        """Every content duplicate among candidates is explained by VENDORED.tsv.

        This is why copy detection never needs a similarity heuristic.
        """
        import collections
        import hashlib

        buckets = collections.defaultdict(list)
        for path in self.candidates:
            buckets[hashlib.sha256((REPO_ROOT / path).read_bytes()).hexdigest()].append(path)
        registered = {frozenset((p.canonical, p.copy)) for p in self.pairs}
        for paths in buckets.values():
            if len(paths) < 2:
                continue
            explained = any(
                frozenset((a, b)) in registered for a in paths for b in paths if a != b
            )
            self.assertTrue(explained, f"unexplained byte-identical group: {paths}")


if __name__ == "__main__":
    unittest.main()
