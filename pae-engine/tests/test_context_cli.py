"""``pae bundle``: input contract, output contract, exit codes, stdout only."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import fixtures as fx  # noqa: E402
from _support import EngineTestCase  # noqa: E402


class BundleCliTestCase(EngineTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.root = fx.standard_repo(self.tmp_path())

    def bundle(self, *args: str):
        return self.run_cli(["bundle", "--repo", str(self.root), *args])


class TestInputContract(BundleCliTestCase):
    def test_a_source_is_required(self) -> None:
        result = self.bundle("--budget-tokens", "8000")
        self.assertEqual(result.code, 2)
        self.assertTrue(result.stdout_empty)

    def test_task_and_ref_are_mutually_exclusive(self) -> None:
        result = self.bundle("--task", "x", "--ref", fx.STANDARD_ID, "--budget-tokens", "8000")
        self.assertEqual(result.code, 2)
        self.assertTrue(result.stdout_empty)

    def test_a_budget_is_required(self) -> None:
        result = self.bundle("--ref", fx.STANDARD_ID)
        self.assertEqual(result.code, 2)
        self.assertTrue(result.stdout_empty)

    def test_kind_and_scope_are_task_only(self) -> None:
        for flag in ("--kind", "--scope"):
            with self.subTest(flag=flag):
                result = self.bundle(
                    "--ref", fx.STANDARD_ID, "--budget-tokens", "8000", flag, "prompt"
                )
                self.assertEqual(result.code, 2)
                self.assertTrue(result.stdout_empty)

    def test_there_is_no_output_flag(self) -> None:
        """The Engine writes nothing; redirection stays the caller's decision."""
        for flag in ("--output", "--save", "--cache", "--truncate"):
            with self.subTest(flag=flag):
                result = self.bundle(
                    "--ref", fx.STANDARD_ID, "--budget-tokens", "8000", flag, "x"
                )
                self.assertEqual(result.code, 2)

    def test_a_repeated_ref_is_accepted_and_deduplicated(self) -> None:
        result = self.bundle(
            "--ref", fx.STANDARD_ID, "--ref", fx.SAFETY_ID, "--budget-tokens", "8000", "--json"
        )
        self.assertEqual(result.code, 0)
        payload = json.loads(result.stdout)
        self.assertEqual(len(payload["included"]), 2)


class TestOutputContract(BundleCliTestCase):
    def test_markdown_is_the_default_and_the_body_appears_verbatim(self) -> None:
        result = self.bundle("--ref", fx.STANDARD_ID, "--budget-tokens", "8000")
        self.assertEqual(result.code, 0)
        self.assertIn("# PAE context bundle", result.stdout)
        self.assertIn(fx.STANDARD_BODY.decode("utf-8"), result.stdout)

    def test_json_is_one_object_with_stable_keys_and_no_markdown(self) -> None:
        result = self.bundle("--ref", fx.STANDARD_ID, "--budget-tokens", "8000", "--json")
        self.assertEqual(result.code, 0)
        self.assertEqual(len(result.stdout.strip().splitlines()), 1)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["schema_version"], "pae-context-bundle/1")
        self.assertEqual(payload["renderer"], "pae-context-markdown/1")
        self.assertNotIn("markdown", payload)
        self.assertNotIn("# PAE context bundle", result.stdout)
        self.assertEqual(payload["included"][0]["content"], fx.STANDARD_BODY.decode("utf-8"))

    def test_the_reported_budget_matches_the_emitted_markdown(self) -> None:
        markdown = self.bundle("--ref", fx.STANDARD_ID, "--budget-tokens", "8000").stdout
        payload = json.loads(
            self.bundle("--ref", fx.STANDARD_ID, "--budget-tokens", "8000", "--json").stdout
        )
        self.assertEqual(payload["budget"]["used_bytes"], len(markdown.encode("utf-8")))
        self.assertLessEqual(
            payload["budget"]["used_bytes"], payload["budget"]["effective_byte_ceiling"]
        )

    def test_the_default_estimator_is_reported_as_inexact(self) -> None:
        payload = json.loads(
            self.bundle("--ref", fx.STANDARD_ID, "--budget-tokens", "8000", "--json").stdout
        )
        self.assertFalse(payload["budget"]["estimator_exact"])
        self.assertEqual(payload["budget"]["estimator_name"], "utf8-bytes-div4")


class TestErrorPaths(BundleCliTestCase):
    def _json_error(self, *args: str):
        result = self.bundle(*args, "--json")
        self.assertTrue(result.stdout_empty)
        return result.code, json.loads(result.stderr)

    def test_a_withheld_body_named_explicitly_is_an_error_not_an_empty_bundle(self) -> None:
        code, payload = self._json_error(
            "--ref", fx.METADATA_ONLY_ID, "--budget-tokens", "8000"
        )
        self.assertEqual(code, 5)
        self.assertEqual(payload["error"], "content_refused")

    def test_a_technique_reference_reports_no_addressable_body(self) -> None:
        code, payload = self._json_error("--ref", fx.TECHNIQUE_ID, "--budget-tokens", "8000")
        self.assertEqual(code, 6)
        self.assertEqual(payload["error"], "no_addressable_content")

    def test_an_excluded_reference_refuses_without_leaking_the_record(self) -> None:
        code, payload = self._json_error("--ref", fx.EXCLUDED_ID, "--budget-tokens", "8000")
        self.assertEqual(code, 5)
        self.assertNotIn("Excluded Fixture", json.dumps(payload))

    def test_an_unknown_reference_is_not_found(self) -> None:
        code, payload = self._json_error(
            "--ref", "prompt:fixtures/nope", "--budget-tokens", "8000"
        )
        self.assertEqual(code, 4)

    def test_a_malformed_reference_is_a_usage_error(self) -> None:
        code, _ = self._json_error("--ref", "not a ref", "--budget-tokens", "8000")
        self.assertEqual(code, 2)

    def test_a_budget_too_small_for_the_framing_exits_two(self) -> None:
        code, payload = self._json_error("--ref", fx.STANDARD_ID, "--budget-bytes", "200")
        self.assertEqual(code, 2)
        self.assertEqual(payload["error"], "budget_too_small")

    def test_no_new_exit_code_was_allocated_for_phase_five(self) -> None:
        from pae_engine import errors

        self.assertEqual(errors.InvalidBudget.exit_code, 2)
        self.assertEqual(errors.BudgetTooSmall.exit_code, 2)


class TestTaskMode(EngineTestCase):
    """Task mode against the real checkout: the Router must run exactly once."""

    def setUp(self) -> None:
        super().setUp()
        self.repo = Path(__file__).resolve().parents[2]

    def bundle(self, *args: str):
        return self.run_cli(["bundle", "--repo", str(self.repo), *args])

    def test_a_task_compiles_a_bundle_and_exits_zero(self) -> None:
        result = self.bundle("--task", "review my terraform setup", "--budget-tokens", "8000")
        self.assertEqual(result.code, 0)
        self.assertIn("# PAE context bundle", result.stdout)
        self.assertIn("Source mode: route", result.stdout)

    def test_route_provenance_survives_into_the_bundle(self) -> None:
        result = self.bundle(
            "--task", "review my terraform setup", "--budget-tokens", "8000", "--json"
        )
        payload = json.loads(result.stdout)
        self.assertEqual(payload["source_mode"], "route")
        self.assertIn(payload["route_status"], {"matched", "ambiguous", "weak", "no_route"})
        self.assertTrue(payload["candidate_scopes"])

    def test_the_router_is_invoked_exactly_once(self) -> None:
        from pae_engine import routing

        calls = []
        original = routing.Router.route

        def counting(self, task, **kwargs):  # noqa: ANN001
            calls.append(task)
            return original(self, task, **kwargs)

        routing.Router.route = counting
        try:
            result = self.bundle("--task", "android accessibility", "--budget-tokens", "8000")
        finally:
            routing.Router.route = original
        self.assertEqual(result.code, 0)
        self.assertEqual(len(calls), 1)

    def test_an_uncertain_route_is_a_result_rather_than_a_failure(self) -> None:
        for task in ("qzzx nonsense token", "improve the thing"):
            with self.subTest(task=task):
                result = self.bundle("--task", task, "--budget-tokens", "8000", "--json")
                self.assertEqual(result.code, 0)
                payload = json.loads(result.stdout)
                self.assertIn(
                    payload["route_status"], {"matched", "ambiguous", "weak", "no_route"}
                )

    def test_a_kind_filter_is_passed_to_the_router(self) -> None:
        result = self.bundle(
            "--task", "security review", "--kind", "skill", "--budget-tokens", "8000", "--json"
        )
        payload = json.loads(result.stdout)
        self.assertEqual(result.code, 0)
        for item in payload["included"]:
            self.assertEqual(item["kind"], "skill")

    def test_a_scope_filter_records_filtered_omissions_without_rerouting(self) -> None:
        probe = json.loads(
            self.bundle("--task", "terraform review", "--budget-tokens", "8000", "--json").stdout
        )
        if not probe["candidate_scopes"]:
            self.skipTest("no candidate scopes to filter")
        scope = probe["candidate_scopes"][0]
        result = self.bundle(
            "--task", "terraform review", "--scope", scope, "--budget-tokens", "8000", "--json"
        )
        payload = json.loads(result.stdout)
        self.assertEqual(result.code, 0)
        self.assertEqual(payload["route_status"], probe["route_status"])
        self.assertEqual(payload["ordering"], "rank+scope-filter")

    def test_an_unknown_scope_for_this_decision_is_a_usage_error(self) -> None:
        result = self.bundle(
            "--task", "terraform review", "--scope", "no-such-scope",
            "--budget-tokens", "8000", "--json",
        )
        self.assertEqual(result.code, 2)
        self.assertTrue(result.stdout_empty)


if __name__ == "__main__":
    unittest.main()
