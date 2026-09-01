"""Reference grammar, identity resolution and alias behaviour."""

from __future__ import annotations

import json
import unittest

from _support import EngineTestCase
import fixtures as fx

from pae_engine import (
    IncompatibleRegistry,
    MalformedReference,
    RegistryValidationError,
    Repository,
    ResourceNotFound,
    classify_ref,
)


class TestReferenceGrammar(unittest.TestCase):
    def test_uid_shape(self) -> None:
        self.assertEqual(classify_ref("pae_008wn0yc495j"), "uid")

    def test_public_id_shape(self) -> None:
        self.assertEqual(classify_ref("technique:ST-01"), "public_id")
        self.assertEqual(classify_ref("prompt:psychology/documentation/soap-note"), "public_id")

    def test_malformed_references_are_usage_errors_not_misses(self) -> None:
        """The fix for a malformed reference is to retype it, not to go looking."""
        for bad in ("", "no-colon", "pae_TOOSHORT", "pae_00000000000i", " ", "Prompt:Upper/Scope",
                    "prompt:", ":path", "prompt:has space"):
            with self.subTest(ref=bad):
                with self.assertRaises(MalformedReference) as ctx:
                    classify_ref(bad)
                self.assertEqual(ctx.exception.exit_code, 2)


class TestLookup(EngineTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.root = fx.standard_repo(self.tmp_path())
        self.registry = Repository.at(self.root).registry()

    def test_uid_and_public_id_return_the_same_resource(self) -> None:
        by_uid = self.registry.get(fx.STANDARD_UID)
        by_id = self.registry.get(fx.STANDARD_ID)
        self.assertEqual(by_uid.uid, by_id.uid)
        self.assertEqual(by_uid.id, by_id.id)

    def test_alias_resolves_and_says_so(self) -> None:
        """A retired public ID answers, but never silently."""
        resolution = self.registry.resolve(fx.RETIRED_ALIAS)
        self.assertEqual(resolution.ref_kind, "alias")
        self.assertEqual(resolution.matched_alias, fx.RETIRED_ALIAS)
        self.assertEqual(resolution.current_id, fx.RENAMED_ID)
        self.assertEqual(resolution.uid, fx.RENAMED_UID)

    def test_current_id_outranks_an_alias_held_by_another_record(self) -> None:
        """An alias must never shadow a live public ID, wherever it appears.

        The alias here is listed on a record that precedes the record whose
        current id it collides with, so a naive first-match scan would return
        the wrong resource.
        """
        root = self.tmp_path("shadow")
        path, sha = fx.with_source(root, "fixtures/live.md", b"live body\n")
        records = [
            fx.record("pae_0000000000aa", "prompt:fixtures/holder",
                      aliases=["prompt:fixtures/contested"]),
            fx.record("pae_0000000000bb", "prompt:fixtures/contested",
                      path=path, content_sha256=sha),
        ]
        fx.build_repo(root, records)
        registry = Repository.at(root).registry()
        resolution = registry.resolve("prompt:fixtures/contested")
        self.assertEqual(resolution.ref_kind, "public_id")
        self.assertEqual(resolution.uid, "pae_0000000000bb")

    def test_unknown_reference_is_a_miss_not_a_usage_error(self) -> None:
        with self.assertRaises(ResourceNotFound) as ctx:
            self.registry.get("prompt:fixtures/nothing-here")
        self.assertEqual(ctx.exception.exit_code, 4)

    def test_tombstone_identity_stays_addressable(self) -> None:
        record = self.registry.get(fx.TOMBSTONE_ID)
        self.assertEqual(record.lifecycle, "tombstone")
        self.assertFalse(record.has_body)

    def test_tombstone_reports_its_replacement_without_following_it(self) -> None:
        resolution = self.registry.resolve(fx.TOMBSTONE_ID)
        self.assertEqual(resolution.replacement["relation"], "superseded_by")
        self.assertEqual(resolution.replacement["edges"][0]["ref"], fx.STANDARD_UID)
        # The tombstone's own identity is returned, not the replacement's.
        self.assertEqual(resolution.uid, fx.TOMBSTONE_UID)

    def test_records_and_load_all_agree(self) -> None:
        streamed = [r.uid for r in self.registry.records()]
        loaded = [r.uid for r in self.registry.load_all()]
        self.assertEqual(streamed, loaded)
        self.assertEqual(len(streamed), 7)

    def test_load_all_is_memoized(self) -> None:
        first = self.registry.load_all()
        self.assertIs(first, self.registry.load_all())


class TestRegistryDefects(EngineTestCase):
    def test_unsupported_record_schema_is_exit_8(self) -> None:
        root = self.tmp_path()
        fx.build_repo(
            root,
            [fx.record("pae_0000000000aa", "prompt:fixtures/future",
                       schema_version="pae-registry-record/2")],
        )
        registry = Repository.at(root).registry()
        with self.assertRaises(IncompatibleRegistry) as ctx:
            registry.get("prompt:fixtures/future")
        self.assertEqual(ctx.exception.exit_code, 8)

    def test_malformed_line_on_the_matched_record_is_a_validation_failure(self) -> None:
        root = self.tmp_path()
        fx.build_repo(
            root,
            [fx.record("pae_0000000000aa", "prompt:fixtures/ok")],
            extra_lines=['{"id": "prompt:fixtures/broken", "uid": '],
        )
        registry = Repository.at(root).registry()
        with self.assertRaises(RegistryValidationError) as ctx:
            registry.get("prompt:fixtures/broken")
        self.assertEqual(ctx.exception.exit_code, 9)

    def test_a_broken_line_elsewhere_does_not_break_an_unrelated_lookup(self) -> None:
        """One corrupt line must not make every lookup fail.

        The prefilter skips lines that cannot match, so a defect in an
        unrelated record stays where it belongs — reported by
        ``validate-registry``, not raised at an innocent caller.
        """
        root = self.tmp_path()
        path, sha = fx.with_source(root, "fixtures/ok.md", b"ok\n")
        fx.build_repo(
            root,
            [fx.record("pae_0000000000aa", "prompt:fixtures/ok", path=path, content_sha256=sha)],
            extra_lines=['{"id": "prompt:fixtures/broken", "uid": '],
        )
        registry = Repository.at(root).registry()
        self.assertEqual(registry.get("prompt:fixtures/ok").uid, "pae_0000000000aa")


class TestLookupCli(EngineTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.root = fx.standard_repo(self.tmp_path())

    def test_get_json_carries_record_resolution_and_serving(self) -> None:
        result = self.run_cli(["get", fx.STANDARD_ID, "--repo", str(self.root), "--json"])
        self.assertEqual(result.code, 0)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["record"]["uid"], fx.STANDARD_UID)
        self.assertEqual(payload["resolution"]["ref_kind"], "public_id")
        self.assertTrue(payload["serving"]["content_available"])

    def test_get_json_is_one_line_with_a_trailing_newline(self) -> None:
        result = self.run_cli(["get", fx.STANDARD_ID, "--repo", str(self.root), "--json"])
        self.assertTrue(result.stdout.endswith("\n"))
        self.assertEqual(result.stdout.count("\n"), 1)

    def test_alias_lookup_via_cli_reports_the_rename(self) -> None:
        result = self.run_cli(["get", fx.RETIRED_ALIAS, "--repo", str(self.root), "--json"])
        self.assertEqual(result.code, 0)
        resolution = json.loads(result.stdout)["resolution"]
        self.assertEqual(resolution["ref_kind"], "alias")
        self.assertEqual(resolution["current_id"], fx.RENAMED_ID)

    def test_malformed_ref_exits_2_and_unknown_ref_exits_4(self) -> None:
        bad = self.run_cli(["get", "nonsense", "--repo", str(self.root), "--json"])
        self.assertFails(bad, 2)
        missing = self.run_cli(["get", "prompt:fixtures/absent", "--repo", str(self.root), "--json"])
        self.assertFails(missing, 4)
        self.assertNotEqual(
            json.loads(bad.stderr)["error"], json.loads(missing.stderr)["error"]
        )


if __name__ == "__main__":
    unittest.main()
