"""CLI surface, output discipline and the exit-code contract."""

from __future__ import annotations

import json
import unittest

from _support import EngineTestCase
import fixtures as fx

from pae_engine import RECORD_SCHEMA, SUMMARY_SCHEMA, __version__
from pae_engine.repository import REPO_ENV_VAR


class TestVersion(EngineTestCase):
    def test_version_needs_no_repository(self) -> None:
        result = self.run_cli(["--version"], env={})
        self.assertEqual(result.code, 0)
        self.assertIn(__version__, result.stdout)
        self.assertIn(RECORD_SCHEMA, result.stdout)

    def test_version_json_carries_both_contracts(self) -> None:
        result = self.run_cli(["--version", "--json"], env={})
        payload = json.loads(result.stdout)
        self.assertEqual(payload["console"], "pae")
        self.assertEqual(payload["engine_version"], __version__)
        self.assertEqual(payload["record_schema"], RECORD_SCHEMA)
        self.assertEqual(payload["summary_schema"], SUMMARY_SCHEMA)


class TestCommandSurface(EngineTestCase):
    def test_only_the_phase_three_commands_exist(self) -> None:
        """Search, routing, bundling and MCP are later phases."""
        from pae_engine import cli

        parser = cli._build_parser()
        actions = [
            a for a in parser._subparsers._group_actions  # noqa: SLF001 - introspection
            if hasattr(a, "choices")
        ]
        commands = set(actions[0].choices)
        self.assertEqual(commands, {"where", "stats", "get", "validate-registry"})

    def test_no_command_prints_help_and_exits_2(self) -> None:
        result = self.run_cli([], env={})
        self.assertFails(result, 2)
        self.assertIn("usage", result.stderr.lower())

    def test_unknown_command_exits_2(self) -> None:
        result = self.run_cli(["search", "anything"], env={})
        self.assertEqual(result.code, 2)


class TestOutputDiscipline(EngineTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.root = fx.standard_repo(self.tmp_path())

    def test_success_writes_only_to_stdout(self) -> None:
        result = self.run_cli(["stats", "--repo", str(self.root), "--json"])
        self.assertEqual(result.code, 0)
        self.assertEqual(result.stderr, "")

    def test_failure_leaves_stdout_empty(self) -> None:
        for argv in (
            ["get", "prompt:fixtures/absent", "--repo", str(self.root)],
            ["get", "nonsense", "--repo", str(self.root)],
            ["get", fx.EXCLUDED_ID, "--repo", str(self.root)],
            ["get", fx.TECHNIQUE_ID, "--content", "--repo", str(self.root)],
        ):
            for extra in ([], ["--json"]):
                with self.subTest(argv=argv + extra):
                    result = self.run_cli(argv + extra)
                    self.assertNotEqual(result.code, 0)
                    self.assertTrue(result.stdout_empty)
                    self.assertNotEqual(result.stderr, "")

    def test_json_errors_are_one_object_on_stderr(self) -> None:
        result = self.run_cli(
            ["get", "prompt:fixtures/absent", "--repo", str(self.root), "--json"]
        )
        payload = json.loads(result.stderr)
        self.assertEqual(payload["exit_code"], result.code)
        self.assertIn("error", payload)
        self.assertIn("message", payload)
        self.assertEqual(result.stderr.count("\n"), 1)

    def test_json_success_is_compact_sorted_and_single_line(self) -> None:
        result = self.run_cli(["where", "--repo", str(self.root), "--json"])
        line = result.stdout.rstrip("\n")
        self.assertNotIn("\n", line)
        parsed = json.loads(line)
        self.assertEqual(
            line, json.dumps(parsed, ensure_ascii=False, sort_keys=True,
                             separators=(",", ":"))
        )

    def test_argparse_failures_also_honour_json(self) -> None:
        """The one failure mode that could otherwise break the contract."""
        import sys

        saved = sys.argv
        sys.argv = ["pae", "get", "--json"]
        try:
            result = self.run_cli(["get", "--json"])
        finally:
            sys.argv = saved
        self.assertEqual(result.code, 2)
        payload = json.loads(result.stderr)
        self.assertEqual(payload["error"], "usage_error")

    def test_json_flag_is_accepted_before_or_after_the_command(self) -> None:
        after = self.run_cli(["where", "--repo", str(self.root), "--json"])
        before = self.run_cli(["--json", "where", "--repo", str(self.root)])
        self.assertEqual(after.stdout, before.stdout)

    def test_human_output_has_no_ansi_escapes(self) -> None:
        result = self.run_cli(["get", fx.STANDARD_ID, "--repo", str(self.root)])
        self.assertNotIn("\x1b[", result.stdout)


class TestStats(EngineTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.root = fx.standard_repo(self.tmp_path())

    def test_stats_without_verify_does_not_read_the_records(self) -> None:
        """The summary is the fast path; a broken JSONL must not slow it down."""
        (self.root / "meta/registry/registry.jsonl").write_text("{ broken\n", encoding="utf-8")
        result = self.run_cli(["stats", "--repo", str(self.root), "--json"])
        self.assertEqual(result.code, 0)
        self.assertFalse(json.loads(result.stdout)["verified"])

    def test_stats_verify_recounts_and_catches_drift(self) -> None:
        root = self.tmp_path("drift")
        records = [fx.record("pae_0000000000aa", "prompt:fixtures/one")]
        fx.build_repo(root, records, summary=fx.summary_for(records, total_records=42))
        ok = self.run_cli(["stats", "--repo", str(root)])
        self.assertEqual(ok.code, 0)
        strict = self.run_cli(["stats", "--repo", str(root), "--verify", "--json"])
        self.assertFails(strict, 9)

    def test_human_stats_never_prints_one_ambiguous_count(self) -> None:
        """Six kinds share the registry; a bare total would misinform."""
        result = self.run_cli(["stats", "--repo", str(self.root)])
        for expected in ("by kind", "by maturity", "by serving policy",
                         "by metadata completeness", "tombstone"):
            self.assertIn(expected, result.stdout)


class TestEnvironmentAndRepoFlags(EngineTestCase):
    def test_env_var_is_honoured_by_the_cli(self) -> None:
        root = fx.standard_repo(self.tmp_path())
        result = self.run_cli(["where", "--json"], env={REPO_ENV_VAR: str(root)})
        self.assertEqual(json.loads(result.stdout)["discovery_source"], "environment")

    def test_repo_flag_wins_over_the_environment(self) -> None:
        chosen = fx.standard_repo(self.tmp_path("chosen"))
        other = fx.standard_repo(self.tmp_path("other"))
        result = self.run_cli(
            ["where", "--repo", str(chosen), "--json"], env={REPO_ENV_VAR: str(other)}
        )
        self.assertEqual(json.loads(result.stdout)["root"], str(chosen.resolve()))


if __name__ == "__main__":
    unittest.main()
