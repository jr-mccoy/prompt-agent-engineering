"""UID and public-ID derivation, and the ledger invariants that freeze them."""

import unittest
from pathlib import Path

from pae_registry import identity as I

REPO_ROOT = Path(__file__).resolve().parents[3]


class UidTests(unittest.TestCase):
    def test_fixed_fixture(self):
        """A pinned expectation: the UID algorithm must not silently change."""
        self.assertEqual(
            I.uid_for("prompt", "domain-reasoning-craft/reasoning-moves/reasoning_inversion.md"),
            "pae_621ynjevba85",
        )

    def test_shape(self):
        uid = I.uid_for("skill", "domain-agentic-resources/skills/marketing/revops/SKILL.md")
        self.assertRegex(uid, I.UID_RE)
        self.assertEqual(len(uid), len("pae_") + 12)

    def test_deterministic_across_calls(self):
        args = ("agent", "childrens-book-studio/agents/childrens-book-orchestrator.md")
        self.assertEqual(I.uid_for(*args), I.uid_for(*args))

    def test_kind_participates_in_the_seed(self):
        path = "domain-x/y.md"
        self.assertNotEqual(I.uid_for("prompt", path), I.uid_for("agent", path))

    def test_crockford_alphabet_excludes_ambiguous_letters(self):
        for letter in "ilou":
            self.assertNotIn(letter, I.CROCKFORD.lower())

    def test_encoding_is_big_endian_and_padded(self):
        self.assertEqual(I.crockford_encode(0), "0" * 12)
        self.assertEqual(I.crockford_encode(1), "0" * 11 + "1")


class PublicIdTests(unittest.TestCase):
    def test_full_path_semantics(self):
        self.assertEqual(
            I.public_id_for("prompt", "domain-reasoning-craft/reasoning-moves/reasoning_inversion.md"),
            "prompt:reasoning-craft/reasoning-moves/reasoning-inversion",
        )

    def test_structural_segment_is_removed(self):
        self.assertEqual(
            I.public_id_for("agent", "domain-agentic-resources/agents/backend/event_sourcing_architect.md"),
            "agent:agentic-resources/backend/event-sourcing-architect",
        )

    def test_skill_slug_is_the_bundle_directory(self):
        self.assertEqual(
            I.public_id_for("skill", "financial-records-toolkit/skills/divorce-financial-flagger/SKILL.md"),
            "skill:financial-records-toolkit/divorce-financial-flagger",
        )

    def test_toolkit_scope_is_the_toolkit(self):
        self.assertEqual(
            I.public_id_for("agent", "childrens-book-studio/agents/childrens-book-orchestrator.md"),
            "agent:childrens-book-studio/childrens-book-orchestrator",
        )

    def test_normalization(self):
        self.assertEqual(I.normalize_component("Foo_Bar Baz"), "foo-bar-baz")
        self.assertEqual(I.normalize_component("a--b"), "a-b")
        self.assertEqual(I.normalize_component("--trim--"), "trim")
        self.assertEqual(I.normalize_component("weird!@#chars"), "weird-chars")

    def test_technique_ids_are_namespaced_not_reslugged(self):
        self.assertEqual(I.technique_public_id("ST-01"), "technique:ST-01")
        self.assertEqual(I.technique_public_id("IPC-14"), "technique:IPC-14")
        with self.assertRaises(I.IdentityError):
            I.technique_public_id("not-a-technique")

    def test_bad_path_segments_are_rejected(self):
        for path in ("domain-x/../y.md", "domain-x/!!!/z.md"):
            with self.subTest(path=path):
                with self.assertRaises(I.IdentityError):
                    I.public_id_for("prompt", path)

    def test_naive_scheme_would_collide_but_full_path_does_not(self):
        """The two commands that motivated full-path IDs."""
        a = I.public_id_for("command", "domain-agentic-resources/commands/documentation/doc_generate.md")
        b = I.public_id_for("command", "domain-agentic-resources/commands/other/doc_generate.md")
        self.assertNotEqual(a, b)
        self.assertTrue(a.endswith("/doc-generate") and b.endswith("/doc-generate"))


class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.rows = [
            I.IdentityRow("pae_aaaaaaaaaaaa", "prompt", "prompt:a/b", "domain-a/b.md"),
            I.IdentityRow("pae_bbbbbbbbbbbb", "prompt", "prompt:a/c", "domain-a/c.md"),
        ]

    def test_clean_ledger(self):
        self.assertEqual(I.check_uniqueness(self.rows, []), [])

    def test_duplicate_uid(self):
        errors = I.check_uniqueness(self.rows + [self.rows[0]], [])
        self.assertTrue(any("duplicate uid" in e for e in errors))

    def test_duplicate_public_id(self):
        clash = I.IdentityRow("pae_cccccccccccc", "prompt", "prompt:a/b", "domain-a/d.md")
        errors = I.check_uniqueness(self.rows + [clash], [])
        self.assertTrue(any("duplicate public id" in e for e in errors))

    def test_alias_cannot_collide_with_a_current_id(self):
        errors = I.check_uniqueness(self.rows, [I.AliasRow("prompt:a/b", "pae_aaaaaaaaaaaa", "x")])
        self.assertTrue(any("alias collides" in e for e in errors))

    def test_alias_must_point_at_a_known_uid(self):
        errors = I.check_uniqueness(self.rows, [I.AliasRow("prompt:z/z", "pae_zzzzzzzzzzzz", "x")])
        self.assertTrue(any("unknown uid" in e for e in errors))

    def test_public_id_must_match_kind(self):
        bad = [I.IdentityRow("pae_dddddddddddd", "skill", "prompt:a/d", "domain-a/d.md")]
        self.assertTrue(any("does not match kind" in e for e in I.check_uniqueness(bad, [])))

    # -- post-freeze stability ---------------------------------------------
    def test_birth_path_may_not_change(self):
        moved = [I.IdentityRow("pae_aaaaaaaaaaaa", "prompt", "prompt:a/b", "domain-z/b.md"), self.rows[1]]
        self.assertTrue(any("birth path changed" in e for e in I.ledger_stability_errors(self.rows, moved, [])))

    def test_kind_may_not_change(self):
        changed = [I.IdentityRow("pae_aaaaaaaaaaaa", "skill", "prompt:a/b", "domain-a/b.md"), self.rows[1]]
        self.assertTrue(any("kind changed" in e for e in I.ledger_stability_errors(self.rows, changed, [])))

    def test_row_may_not_disappear(self):
        self.assertTrue(any("disappeared" in e for e in I.ledger_stability_errors(self.rows, self.rows[1:], [])))

    def test_public_id_change_requires_an_alias(self):
        renamed = [I.IdentityRow("pae_aaaaaaaaaaaa", "prompt", "prompt:new/home", "domain-a/b.md"), self.rows[1]]
        self.assertTrue(any("without an alias row" in e for e in I.ledger_stability_errors(self.rows, renamed, [])))
        alias = [I.AliasRow("prompt:a/b", "pae_aaaaaaaaaaaa", "moved domain")]
        self.assertEqual(I.ledger_stability_errors(self.rows, renamed, alias), [])


class CommittedLedgerTests(unittest.TestCase):
    def test_committed_ledger_is_internally_consistent(self):
        rows = I.read_identity(REPO_ROOT / "meta" / "registry" / "identity.tsv")
        aliases = I.read_aliases(REPO_ROOT / "meta" / "registry" / "aliases.tsv")
        self.assertTrue(rows, "identity ledger is empty; identity has not been frozen")
        self.assertEqual(I.check_uniqueness(rows, aliases), [])

    def test_every_committed_uid_matches_its_seed(self):
        """The ledger must be reproducible from birth paths, not hand-written."""
        for row in I.read_identity(REPO_ROOT / "meta" / "registry" / "identity.tsv"):
            with self.subTest(uid=row.uid):
                self.assertEqual(row.uid, I.uid_for(row.kind, row.birth_path))


if __name__ == "__main__":
    unittest.main()
