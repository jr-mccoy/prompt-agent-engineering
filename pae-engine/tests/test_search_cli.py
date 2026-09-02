"""``pae search`` and ``pae route``: flags, output shape and exit codes.

The contract that matters most here is that finding nothing exits 0. A caller
must be able to tell "your query matched no resource" apart from "the engine
could not run", and an exit code is the only channel a shell script reads.
"""

from __future__ import annotations

import json
import unittest

import fixtures
from _support import EngineTestCase

_CROCKFORD = str.maketrans({"i": "1", "l": "1", "o": "0", "u": "v"})


def _uid(mnemonic: str) -> str:
    return "pae_" + (mnemonic.translate(_CROCKFORD) + "0" * 12)[:12]


class CliCase(EngineTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.root = self.tmp_path()
        fixtures.build_repo(
            self.root,
            [
                fixtures.record(
                    uid=_uid("kube"),
                    id="prompt:alpha/kubernetes-cluster-upgrade",
                    title="Kubernetes Cluster Upgrade Runbook",
                    description="Upgrade a kubernetes cluster safely.",
                    path="alpha/kube.md",
                    native={"category": "alpha", "tags": ["kubernetes", "cluster"]},
                ),
                fixtures.record(
                    uid=_uid("helm"),
                    id="skill:agentic-resources/cloud-infrastructure/helm-chart-scaffolding",
                    kind="skill",
                    title="Helm Chart Scaffolding",
                    description="Generate a production ready helm chart.",
                    path="skills/helm.md",
                    native={"name": "helm-chart-scaffolding", "tags": ["helm"]},
                ),
                fixtures.record(
                    uid=_uid("secret"),
                    id="prompt:alpha/excluded-thing",
                    title="Excluded Kubernetes Secret",
                    policy="excluded",
                    path="alpha/secret.md",
                ),
                fixtures.record(
                    uid=_uid("dead"),
                    id="prompt:alpha/retired-kubernetes-guide",
                    title="Retired Kubernetes Guide",
                    lifecycle="tombstone",
                    maturity="deprecated",
                ),
            ],
        )

    def cli(self, *argv: str):
        return self.run_cli(["--repo", str(self.root), *argv])


class TestSearchCli(CliCase):
    def test_human_output_lists_ranked_hits_with_evidence(self) -> None:
        result = self.cli("search", "kubernetes cluster upgrade")
        self.assertEqual(result.code, 0)
        self.assertIn("prompt:alpha/kubernetes-cluster-upgrade", result.stdout)
        self.assertIn("Kubernetes Cluster Upgrade Runbook", result.stdout)
        self.assertIn("title:", result.stdout)
        self.assertIn("score", result.stdout)

    def test_json_output_is_one_line_on_stdout(self) -> None:
        result = self.cli("--json", "search", "kubernetes cluster upgrade")
        self.assertEqual(result.code, 0)
        self.assertEqual(len(result.stdout.strip().splitlines()), 1)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["hits"][0]["id"], "prompt:alpha/kubernetes-cluster-upgrade")
        self.assertIn("normalized_terms", payload)
        self.assertIn("total_matched", payload)

    def test_zero_results_exits_zero(self) -> None:
        result = self.cli("search", "zzzzqqq wobblegonk")
        self.assertEqual(result.code, 0)
        self.assertIn("no results", result.stdout)
        payload = json.loads(self.cli("--json", "search", "zzzzqqq wobblegonk").stdout)
        self.assertEqual(payload["hits"], [])
        self.assertEqual(payload["total_matched"], 0)

    def test_malformed_queries_exit_two(self) -> None:
        for query in ("", "   ", "the and of"):
            self.assertFails(self.cli("search", query), 2)

    def test_invalid_filters_exit_two(self) -> None:
        self.assertFails(self.cli("search", "kubernetes", "--kind", "nonsense"), 2)
        self.assertFails(self.cli("search", "kubernetes", "--scope", "no-such-scope"), 2)
        self.assertFails(self.cli("search", "kubernetes", "--limit", "0"), 2)
        self.assertFails(self.cli("search", "kubernetes", "--limit", "101"), 2)

    def test_json_errors_go_to_stderr(self) -> None:
        result = self.cli("--json", "search", "the and of")
        self.assertEqual(result.code, 2)
        self.assertTrue(result.stdout_empty)
        self.assertEqual(json.loads(result.stderr)["exit_code"], 2)

    def test_kind_filter_is_repeatable(self) -> None:
        payload = json.loads(
            self.cli("--json", "search", "helm chart", "--kind", "skill").stdout
        )
        self.assertTrue(payload["hits"])
        self.assertTrue(all(hit["kind"] == "skill" for hit in payload["hits"]))

    def test_excluded_never_appears_under_any_flag(self) -> None:
        result = self.cli(
            "--json",
            "search",
            "kubernetes",
            "--include-deprecated",
            "--include-tombstones",
            "--limit",
            "100",
        )
        self.assertNotIn("excluded-thing", result.stdout)
        self.assertNotIn(_uid("secret"), result.stdout)

    def test_tombstones_appear_only_with_their_flag(self) -> None:
        plain = self.cli("--json", "search", "retired kubernetes guide").stdout
        self.assertNotIn("retired-kubernetes-guide", plain)
        included = self.cli(
            "--json", "search", "retired kubernetes guide", "--include-tombstones"
        ).stdout
        self.assertIn("retired-kubernetes-guide", included)

    def test_no_source_body_is_ever_printed(self) -> None:
        body = (self.root / "alpha" / "kube.md")
        body.parent.mkdir(parents=True, exist_ok=True)
        body.write_text("SECRET BODY MARKER\n", encoding="utf-8")
        for argv in (
            ("search", "kubernetes cluster upgrade"),
            ("--json", "search", "kubernetes cluster upgrade"),
            ("route", "kubernetes cluster upgrade"),
            ("--json", "route", "kubernetes cluster upgrade"),
        ):
            self.assertNotIn("SECRET BODY MARKER", self.cli(*argv).stdout, argv)

    def test_exact_reference_from_the_cli(self) -> None:
        payload = json.loads(
            self.cli("--json", "search", "prompt:alpha/kubernetes-cluster-upgrade").stdout
        )
        self.assertEqual(payload["hits"][0]["matched_fields"], ["exact_reference"])


class TestRouteCli(CliCase):
    def test_human_output_reports_status_and_evidence(self) -> None:
        result = self.cli("route", "kubernetes cluster upgrade")
        self.assertEqual(result.code, 0)
        self.assertIn("status:", result.stdout)
        self.assertIn("candidate scopes", result.stdout)
        self.assertIn("why", result.stdout)

    def test_json_route_is_one_line_and_has_no_confidence(self) -> None:
        result = self.cli("--json", "route", "kubernetes cluster upgrade")
        self.assertEqual(result.code, 0)
        self.assertEqual(len(result.stdout.strip().splitlines()), 1)
        payload = json.loads(result.stdout)
        self.assertIn(payload["status"], ("matched", "ambiguous", "weak", "no_route"))
        for banned in ("confidence", "probability"):
            self.assertNotIn(banned, result.stdout.lower())

    def test_every_status_exits_zero(self) -> None:
        for query in (
            "kubernetes cluster upgrade",
            "zzzzqqq wobblegonk",
            "kubernetes sourdough starter hydration bakery schedule",
        ):
            self.assertEqual(self.cli("route", query).code, 0, query)

    def test_ambiguity_is_not_an_error_exit(self) -> None:
        payload = json.loads(self.cli("--json", "route", "zzzzqqq wobblegonk").stdout)
        self.assertEqual(payload["status"], "no_route")
        self.assertIsNone(payload["selected_scope"])

    def test_route_limit_and_kind_bounds(self) -> None:
        self.assertFails(self.cli("route", "kubernetes", "--limit", "0"), 2)
        self.assertFails(self.cli("route", "kubernetes", "--limit", "26"), 2)
        self.assertFails(self.cli("route", "kubernetes", "--kind", "nonsense"), 2)

    def test_route_accepts_kind_and_limit(self) -> None:
        payload = json.loads(
            self.cli("--json", "route", "helm chart", "--kind", "skill", "--limit", "1").stdout
        )
        self.assertLessEqual(len(payload["resources"]), 1)
        self.assertTrue(all(r["kind"] == "skill" for r in payload["resources"]))


class TestHelpSurface(CliCase):
    def test_search_and_route_are_advertised(self) -> None:
        result = self.run_cli(["--help"])
        self.assertIn("search", result.stdout)
        self.assertIn("route", result.stdout)

    def test_version_reports_the_engine_version(self) -> None:
        payload = json.loads(self.run_cli(["--json", "--version"]).stdout)
        self.assertEqual(payload["engine_version"], "0.5.0.dev0")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
