"""Serving policy, enforced in the library rather than the CLI."""

from __future__ import annotations

import json
import unittest

from _support import EngineTestCase
import fixtures as fx

from pae_engine import (
    ContentRefused,
    NoAddressableContent,
    Repository,
    ResourceExcluded,
)


class TestServingPolicy(EngineTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.root = fx.standard_repo(self.tmp_path())
        self.registry = Repository.at(self.root).registry()

    # -- standard ----------------------------------------------------------

    def test_standard_serves_metadata_and_whole_body(self) -> None:
        self.assertEqual(self.registry.get(fx.STANDARD_ID).serving_policy, "standard")
        content = self.registry.content(fx.STANDARD_ID)
        self.assertEqual(content.data, fx.STANDARD_BODY)
        self.assertTrue(content.verified)

    # -- safety_gated ------------------------------------------------------

    def test_safety_gated_serves_the_whole_body_and_propagates_guards(self) -> None:
        """Whole or not at all. There is no partial variant to fall back to."""
        content = self.registry.content(fx.SAFETY_ID)
        self.assertEqual(content.data, fx.SAFETY_BODY)
        self.assertEqual(content.serving_policy, "safety_gated")
        self.assertTrue(content.guard_preservation["must_not_truncate"])
        self.assertIn("guard_preservation", content.to_json_obj())

    # -- metadata_only -----------------------------------------------------

    def test_metadata_only_returns_metadata_but_refuses_the_body(self) -> None:
        record = self.registry.get(fx.METADATA_ONLY_ID)
        self.assertEqual(record.serving_policy, "metadata_only")
        with self.assertRaises(ContentRefused) as ctx:
            self.registry.content(fx.METADATA_ONLY_ID)
        self.assertEqual(ctx.exception.exit_code, 5)

    def test_metadata_only_never_opens_the_source_file(self) -> None:
        """A withheld body must not be read from disk merely to be discarded.

        Deleting the file leaves the refusal identical: if the Engine were
        reading first and refusing second, this would surface as an integrity
        error instead.
        """
        (self.root / "fixtures/metadata_only.md").unlink()
        with self.assertRaises(ContentRefused):
            self.registry.content(fx.METADATA_ONLY_ID)

    # -- excluded ----------------------------------------------------------

    def test_excluded_resolves_but_refuses_its_record(self) -> None:
        resolution = self.registry.resolve(fx.EXCLUDED_ID)
        self.assertEqual(resolution.uid, fx.EXCLUDED_UID)

        with self.assertRaises(ResourceExcluded) as ctx:
            self.registry.get(fx.EXCLUDED_ID)
        self.assertEqual(ctx.exception.exit_code, 5)

    def test_excluded_error_carries_an_identity_stub_and_nothing_more(self) -> None:
        """Distinguishable from nonexistent, without leaking the resource."""
        with self.assertRaises(ResourceExcluded) as ctx:
            self.registry.get(fx.EXCLUDED_ID)
        stub = ctx.exception.details["resource"]
        self.assertEqual(
            set(stub), {"uid", "id", "kind", "lifecycle", "serving_policy"}
        )
        blob = json.dumps(ctx.exception.to_json_obj())
        self.assertNotIn("Excluded Fixture", blob)
        self.assertNotIn("Must never be returned", blob)

    def test_excluded_content_is_refused(self) -> None:
        with self.assertRaises(ResourceExcluded) as ctx:
            self.registry.content(fx.EXCLUDED_ID)
        self.assertEqual(ctx.exception.exit_code, 5)

    # -- no addressable body ----------------------------------------------

    def test_technique_metadata_is_served_but_has_no_body(self) -> None:
        record = self.registry.get(fx.TECHNIQUE_ID)
        self.assertEqual(record.kind, "technique")
        self.assertFalse(record.has_body)
        with self.assertRaises(NoAddressableContent) as ctx:
            self.registry.content(fx.TECHNIQUE_ID)
        self.assertEqual(ctx.exception.exit_code, 6)
        self.assertEqual(
            ctx.exception.details["defined_in"], "techniques/MASTER_TECHNIQUE_INDEX.md"
        )

    def test_tombstone_content_is_absent_not_withheld(self) -> None:
        """Exit 6, not 5, even though the tombstone's policy is metadata_only.

        "The body no longer exists" and "the body is withheld" call for
        different next steps, so addressability is decided before policy.
        """
        with self.assertRaises(NoAddressableContent) as ctx:
            self.registry.content(fx.TOMBSTONE_ID)
        self.assertEqual(ctx.exception.exit_code, 6)


class TestFailClosedPolicy(EngineTestCase):
    def _repo_with_policy(self, policy):
        root = self.tmp_path(f"policy-{policy or 'missing'}")
        path, sha = fx.with_source(root, "fixtures/body.md", b"body\n")
        fx.build_repo(
            root,
            [fx.record("pae_0000000000aa", "prompt:fixtures/odd", policy=policy,
                       path=path, content_sha256=sha)],
        )
        return Repository.at(root).registry()

    def test_unknown_policy_fails_closed_to_metadata_only(self) -> None:
        """Never ``standard``. A policy the Engine cannot interpret withholds."""
        registry = self._repo_with_policy("some_future_policy")
        record = registry.get("prompt:fixtures/odd")
        self.assertEqual(record.serving_policy, "metadata_only")
        self.assertFalse(record.serving_policy_recognized)
        self.assertEqual(record.serving_policy_declared, "some_future_policy")
        with self.assertRaises(ContentRefused) as ctx:
            registry.content("prompt:fixtures/odd")
        self.assertFalse(ctx.exception.details["policy_recognized"])

    def test_missing_policy_fails_closed_and_says_so(self) -> None:
        registry = self._repo_with_policy(None)
        record = registry.get("prompt:fixtures/odd")
        self.assertEqual(record.serving_policy, "metadata_only")
        self.assertIsNone(record.serving_policy_declared)
        self.assertFalse(record.serving_policy_recognized)


class TestServingPolicyCli(EngineTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.root = fx.standard_repo(self.tmp_path())

    def _get(self, *args):
        return self.run_cli(["get", *args, "--repo", str(self.root), "--json"])

    def test_exit_codes_by_policy(self) -> None:
        cases = [
            ((fx.STANDARD_ID, "--content"), 0),
            ((fx.SAFETY_ID, "--content"), 0),
            ((fx.METADATA_ONLY_ID,), 0),
            ((fx.METADATA_ONLY_ID, "--content"), 5),
            ((fx.EXCLUDED_ID,), 5),
            ((fx.EXCLUDED_ID, "--content"), 5),
            ((fx.TOMBSTONE_ID,), 0),
            ((fx.TOMBSTONE_ID, "--content"), 6),
            ((fx.TECHNIQUE_ID,), 0),
            ((fx.TECHNIQUE_ID, "--content"), 6),
        ]
        for args, expected in cases:
            with self.subTest(args=args):
                result = self._get(*args)
                self.assertEqual(result.code, expected, msg=result.stderr)
                if expected != 0:
                    self.assertTrue(result.stdout_empty)

    def test_excluded_cli_error_includes_the_identity_stub(self) -> None:
        result = self._get(fx.EXCLUDED_ID)
        self.assertFails(result, 5)
        payload = json.loads(result.stderr)
        self.assertEqual(payload["error"], "resource_excluded")
        self.assertEqual(payload["resource"]["uid"], fx.EXCLUDED_UID)

    def test_raw_content_is_byte_exact(self) -> None:
        result = self.run_cli(
            ["get", fx.SAFETY_ID, "--repo", str(self.root), "--content"]
        )
        self.assertEqual(result.code, 0)
        self.assertEqual(result.stdout_bytes, fx.SAFETY_BODY)


if __name__ == "__main__":
    unittest.main()
