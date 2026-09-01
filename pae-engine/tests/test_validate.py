"""Consumer-side registry validation."""

from __future__ import annotations

import json
import unittest

from _support import EngineTestCase
import fixtures as fx

from pae_engine import IncompatibleRegistry, Repository, validate_registry


def codes(report) -> set[str]:
    return {issue.code for issue in report.issues}


class TestHealthyRegistry(EngineTestCase):
    def test_a_well_formed_checkout_passes(self) -> None:
        root = fx.standard_repo(self.tmp_path())
        report = validate_registry(Repository.at(root))
        self.assertTrue(report.ok, msg=[i.message for i in report.issues])
        self.assertEqual(report.checked["records"], 7)

    def test_checksum_verification_passes_on_intact_sources(self) -> None:
        root = fx.standard_repo(self.tmp_path())
        report = validate_registry(Repository.at(root), verify_checksums=True)
        self.assertTrue(report.ok, msg=[i.message for i in report.issues])
        self.assertTrue(report.checksums_verified)


class TestDefects(EngineTestCase):
    def _report(self, records, *, name="repo", summary=None, extra_lines=(),
                sources=None, verify_checksums=False):
        root = self.tmp_path(name)
        fx.build_repo(root, records, summary=summary, extra_lines=extra_lines,
                      sources=sources)
        return root, validate_registry(
            Repository.at(root), verify_checksums=verify_checksums
        )

    def test_malformed_json_line(self) -> None:
        _root, report = self._report(
            [fx.record("pae_0000000000aa", "prompt:fixtures/ok")],
            extra_lines=['{"uid": "pae_0000000000bb"'],
            summary=fx.summary_for([fx.record("pae_0000000000aa", "prompt:fixtures/ok")]),
        )
        self.assertIn("malformed_json_line", codes(report))
        self.assertFalse(report.ok)

    def test_duplicate_uid(self) -> None:
        records = [
            fx.record("pae_0000000000aa", "prompt:fixtures/one"),
            fx.record("pae_0000000000aa", "prompt:fixtures/two"),
        ]
        _root, report = self._report(records)
        self.assertIn("duplicate_uid", codes(report))

    def test_duplicate_public_id(self) -> None:
        records = [
            fx.record("pae_0000000000aa", "prompt:fixtures/same"),
            fx.record("pae_0000000000bb", "prompt:fixtures/same"),
        ]
        _root, report = self._report(records)
        self.assertIn("duplicate_public_id", codes(report))

    def test_duplicate_alias(self) -> None:
        records = [
            fx.record("pae_0000000000aa", "prompt:fixtures/one",
                      aliases=["prompt:fixtures/old"]),
            fx.record("pae_0000000000bb", "prompt:fixtures/two",
                      aliases=["prompt:fixtures/old"]),
        ]
        _root, report = self._report(records)
        self.assertIn("duplicate_alias", codes(report))

    def test_alias_shadowing_a_live_public_id(self) -> None:
        """An alias that is also somebody's current id makes lookup ambiguous."""
        records = [
            fx.record("pae_0000000000aa", "prompt:fixtures/one",
                      aliases=["prompt:fixtures/two"]),
            fx.record("pae_0000000000bb", "prompt:fixtures/two"),
        ]
        _root, report = self._report(records)
        self.assertIn("alias_shadows_public_id", codes(report))

    def test_malformed_identity_shapes(self) -> None:
        records = [
            fx.record("not-a-uid", "prompt:fixtures/one"),
            fx.record("pae_0000000000bb", "NOT A PUBLIC ID"),
            fx.record("pae_0000000000cc", "prompt:fixtures/three", aliases=["bad alias"]),
        ]
        _root, report = self._report(records)
        self.assertLessEqual(
            {"invalid_uid", "invalid_public_id", "invalid_alias"}, codes(report)
        )

    def test_missing_required_field(self) -> None:
        _root, report = self._report(
            [fx.record("pae_0000000000aa", "prompt:fixtures/one", drop=["title"])]
        )
        self.assertIn("missing_required_field", codes(report))

    def test_dangling_relationship_uid(self) -> None:
        records = [
            fx.record(
                "pae_0000000000aa",
                "prompt:fixtures/one",
                relationships={
                    "superseded_by": {"ref": "pae_0000000000zz", "object_kind": "resource"}
                },
            )
        ]
        _root, report = self._report(records)
        self.assertIn("dangling_relationship_uid", codes(report))

    def test_document_edges_are_not_reported_as_dangling(self) -> None:
        """Only resource edges name registry records; documents are not records."""
        records = [
            fx.record(
                "pae_0000000000aa",
                "prompt:fixtures/one",
                relationships={
                    "superseded_by": {"ref": "docs/somewhere.md", "object_kind": "document"}
                },
            )
        ]
        _root, report = self._report(records)
        self.assertNotIn("dangling_relationship_uid", codes(report))

    def test_unsafe_source_paths(self) -> None:
        records = [
            fx.record("pae_0000000000aa", "prompt:fixtures/one", path="../escape.md",
                      content_sha256=fx.sha256_of(b"")),
            fx.record("pae_0000000000bb", "prompt:fixtures/two", path="/etc/passwd",
                      content_sha256=fx.sha256_of(b"")),
        ]
        _root, report = self._report(records)
        self.assertIn("unsafe_source_path", codes(report))
        self.assertEqual(
            sum(1 for i in report.issues if i.code == "unsafe_source_path"), 2
        )

    def test_missing_source_file(self) -> None:
        records = [
            fx.record("pae_0000000000aa", "prompt:fixtures/one", path="fixtures/gone.md",
                      content_sha256=fx.sha256_of(b""))
        ]
        _root, report = self._report(records)
        self.assertIn("missing_source_file", codes(report))

    def test_missing_checksum_on_a_live_body(self) -> None:
        root = self.tmp_path()
        path, _sha = fx.with_source(root, "fixtures/body.md", b"body\n")
        fx.build_repo(
            root,
            [fx.record("pae_0000000000aa", "prompt:fixtures/one", path=path,
                       content_sha256=None)],
        )
        report = validate_registry(Repository.at(root))
        self.assertIn("missing_checksum", codes(report))

    def test_checksum_mismatch_is_only_found_when_asked(self) -> None:
        root = self.tmp_path()
        path, _sha = fx.with_source(root, "fixtures/body.md", b"changed\n")
        fx.build_repo(
            root,
            [fx.record("pae_0000000000aa", "prompt:fixtures/one", path=path,
                       content_sha256=fx.sha256_of(b"original\n"))],
        )
        repo = Repository.at(root)
        self.assertTrue(validate_registry(repo).ok)
        deep = validate_registry(repo, verify_checksums=True)
        self.assertIn("checksum_mismatch", codes(deep))

    def test_summary_drift(self) -> None:
        records = [fx.record("pae_0000000000aa", "prompt:fixtures/one")]
        drifted = fx.summary_for(records, total_records=99)
        _root, report = self._report(records, summary=drifted)
        self.assertIn("summary_drift", codes(report))

    def test_every_defect_is_collected_not_just_the_first(self) -> None:
        """An agent told about one problem at a time will re-run four times."""
        records = [
            fx.record("pae_0000000000aa", "prompt:fixtures/one",
                      aliases=["prompt:fixtures/two"]),
            fx.record("pae_0000000000aa", "prompt:fixtures/two", path="../escape.md",
                      content_sha256=fx.sha256_of(b"")),
        ]
        _root, report = self._report(records)
        self.assertGreaterEqual(len(report.issues), 3)
        self.assertLessEqual(
            {"duplicate_uid", "alias_shadows_public_id", "unsafe_source_path"},
            codes(report),
        )

    def test_unsupported_record_schema_stops_the_run(self) -> None:
        """Beyond the schema boundary the Engine cannot name what it is checking."""
        root = self.tmp_path()
        fx.build_repo(
            root,
            [fx.record("pae_0000000000aa", "prompt:fixtures/one",
                       schema_version="pae-registry-record/2")],
        )
        with self.assertRaises(IncompatibleRegistry) as ctx:
            validate_registry(Repository.at(root))
        self.assertEqual(ctx.exception.exit_code, 8)


class TestValidateBoundary(unittest.TestCase):
    def test_the_validator_does_not_reimplement_the_generator(self) -> None:
        """Consumer validation, not a second copy of the producer's checks.

        Membership discovery, kind classification, UID derivation, override
        application and ledger migration all stay in the repository-maintenance
        package; duplicating them here would create a second source of truth
        that could disagree with the frozen one.

        Only executable code is inspected. The module's own prose says what it
        deliberately does not do, and a naive text search would flag that
        sentence as the very thing it promises to avoid.
        """
        from pae_engine import validate as module
        from _codescan import code_only

        source = code_only(module)
        for forbidden in (
            "rglob",           # corpus discovery
            "walk",            # corpus discovery
            "frontmatter",     # source-schema parsing
            "DOMAIN_DIRS",     # membership allowlist
            "yaml",            # override/ledger formats
            "REORG_MAP",       # migration bookkeeping
            "VENDORED",
            "birth_path",      # UID derivation input
        ):
            self.assertNotIn(
                forbidden, source, f"validate.py must not do {forbidden!r} work"
            )

    def test_the_validator_imports_only_stdlib_and_the_engine(self) -> None:
        import ast
        import sys
        from pathlib import Path

        from pae_engine import validate as module

        tree = ast.parse(Path(module.__file__).read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.level:  # relative: inside pae_engine
                    continue
                root = (node.module or "").split(".")[0]
                self.assertIn(root, sys.stdlib_module_names, f"non-stdlib import: {root}")
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    root = alias.name.split(".")[0]
                    self.assertIn(
                        root, sys.stdlib_module_names, f"non-stdlib import: {root}"
                    )


class TestValidateCli(EngineTestCase):
    def test_healthy_registry_exits_0(self) -> None:
        root = fx.standard_repo(self.tmp_path())
        result = self.run_cli(["validate-registry", "--repo", str(root), "--json"])
        self.assertEqual(result.code, 0)
        self.assertTrue(json.loads(result.stdout)["ok"])

    def test_corrupt_registry_exits_9_with_issues_on_stderr(self) -> None:
        root = self.tmp_path()
        fx.build_repo(
            root,
            [
                fx.record("pae_0000000000aa", "prompt:fixtures/one"),
                fx.record("pae_0000000000aa", "prompt:fixtures/two"),
            ],
        )
        result = self.run_cli(["validate-registry", "--repo", str(root), "--json"])
        self.assertFails(result, 9)
        payload = json.loads(result.stderr)
        self.assertEqual(payload["error"], "registry_validation_failed")
        self.assertGreaterEqual(payload["issue_count"], 1)

    def test_verify_checksums_flag_is_reported(self) -> None:
        root = fx.standard_repo(self.tmp_path())
        result = self.run_cli(
            ["validate-registry", "--repo", str(root), "--verify-checksums", "--json"]
        )
        self.assertEqual(result.code, 0)
        self.assertTrue(json.loads(result.stdout)["checksums_verified"])


if __name__ == "__main__":
    unittest.main()
