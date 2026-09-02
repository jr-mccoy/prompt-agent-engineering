"""The whole pipeline on the fake provider, with no credential and no spend.

This is the test that would have caught every integration bug the unit tests
cannot see: plan, snapshot, isolation, four conditions, tool loops, append-only
trials, resume, scoring, analysis and report, wired together.

It runs twice with opposite ground truth — a known-positive fixture and a
known-negative one — because a pipeline that only ever sees PAE win is a
pipeline whose reporting has never been tested.
"""

from __future__ import annotations

import json
import unittest
from dataclasses import replace
from pathlib import Path

from _support import (
    MINI_BENCHMARK,
    REPO_ROOT,
    TempDirCase,
    engine_available,
    git_repo_available,
    load_mini_benchmark,
    mcp_sdk_available,
)

from pae_eval.analysis import AnalysisInputs, analyze
from pae_eval.judging import score_task
from pae_eval.plan import example_plan
from pae_eval.pricing import example_snapshot
from pae_eval.providers.fake import BehaviouralFake
from pae_eval.report import render_markdown
from pae_eval.runner import dry_run, execute, prepare
from pae_eval.trials import TrialStore


def development_plan():
    """A/B/C only: condition D needs a live MCP server, covered separately."""
    plan = example_plan()
    return replace(
        plan,
        conditions=("A", "B", "C"),
        primary_comparison=("C", "B"),
        models=(plan.models[0],),
        repeats={"A": 1, "B": 1, "C": 1},
        bootstrap_resamples=1000,
    )


@unittest.skipUnless(git_repo_available() and engine_available(),
                     "needs the real checkout and the Engine")
class TestFakePipeline(TempDirCase):
    def _run(self, quality: str) -> dict:
        plan = development_plan()
        benchmark = load_mini_benchmark()
        output = self.tmp_path(f"out-{quality}")
        context = prepare(
            plan=plan, benchmark=benchmark, repo=REPO_ROOT, output_dir=output,
            benchmark_root=MINI_BENCHMARK, pricing=example_snapshot(),
            mode="development",
        )
        adapter = BehaviouralFake(quality=quality)
        summary = execute(
            context, adapters={"anthropic": adapter}, max_cost_usd=100.0,
            max_trials=500, require_ripgrep=False,
        )
        trials = list(TrialStore(context.trials_path).read())
        scores = [
            score_task(benchmark.by_id(row["task_id"]), trial=row).to_json_obj()
            for row in trials if row["state"] == "completed"
        ]
        result = analyze(
            AnalysisInputs(trials=trials, scores=scores, plan=plan),
            planned_trials=summary.planned,
        )
        return {"summary": summary, "analysis": result, "plan": plan,
                "context": context, "trials": trials}

    def test_known_positive_fixture(self) -> None:
        outcome = self._run("by_condition")
        primary = outcome["analysis"]["primary"]
        self.assertEqual(primary["primary_contrast"], ["C", "B"])
        self.assertGreater(primary["absolute_difference"], 0)
        self.assertGreater(primary["C_pass_rate"], primary["B_pass_rate"])

        markdown = render_markdown(outcome["analysis"], plan=outcome["plan"],
                                   is_fixture=True)
        self.assertIn("SYNTHETIC TEST FIXTURE", markdown)
        self.assertIn("excludes zero", markdown)

    def test_known_negative_fixture_is_reported_without_spin(self) -> None:
        outcome = self._run("by_condition_inverted")
        primary = outcome["analysis"]["primary"]
        self.assertLess(primary["absolute_difference"], 0)

        markdown = render_markdown(outcome["analysis"], plan=outcome["plan"],
                                   is_fixture=True)
        self.assertIn("performed worse", markdown)
        summary = markdown.split("## Evaluation design")[0]
        for word in ("improved", "outperformed", "better"):
            self.assertNotIn(word, summary.lower())

    def test_every_planned_trial_is_accounted_for(self) -> None:
        outcome = self._run("pass")
        summary = outcome["summary"]
        self.assertEqual(summary.attempted, summary.planned)
        failures = outcome["analysis"]["failures"]
        self.assertEqual(failures["recorded_trials"], summary.planned)

    def test_evidence_artifacts_are_written_and_hashed(self) -> None:
        outcome = self._run("pass")
        output = outcome["context"].output_dir
        for name in ("run-manifest.json", "trial-schedule.json",
                     "participant-snapshot.json", "trials.jsonl"):
            self.assertTrue((output / name).exists(), name)
        for name in ("run-manifest.json", "trial-schedule.json"):
            self.assertTrue((output / f"{name}.sha256").exists(), name)

    def test_the_manifest_contains_no_absolute_output_path(self) -> None:
        outcome = self._run("pass")
        manifest = json.loads(
            (outcome["context"].output_dir / "run-manifest.json")
            .read_text(encoding="utf-8"))
        self.assertNotIn("output_dir", manifest)
        self.assertIn("output_dir_identity", manifest)
        self.assertNotIn(str(outcome["context"].output_dir),
                         json.dumps(manifest))

    def test_conditions_are_interleaved_not_blocked(self) -> None:
        outcome = self._run("pass")
        order = [t.condition for t in outcome["context"].schedule.trials]
        # A blocked schedule would have exactly one run of each condition.
        runs = sum(1 for a, b in zip(order, order[1:]) if a != b)
        self.assertGreater(runs, len(set(order)),
                           "conditions must interleave to avoid confounding "
                           "the contrast with provider drift over time")

    def test_resume_skips_completed_trials(self) -> None:
        plan = development_plan()
        benchmark = load_mini_benchmark()
        output = self.tmp_path("out-resume")
        context = prepare(
            plan=plan, benchmark=benchmark, repo=REPO_ROOT, output_dir=output,
            benchmark_root=MINI_BENCHMARK, pricing=example_snapshot(),
            mode="development",
        )
        first = execute(context, adapters={"anthropic": BehaviouralFake()},
                        max_cost_usd=100.0, max_trials=4, require_ripgrep=False)
        self.assertEqual(first.attempted, 4)

        second = execute(context, adapters={"anthropic": BehaviouralFake()},
                         max_cost_usd=100.0, max_trials=500,
                         require_ripgrep=False)
        self.assertEqual(second.skipped_resume, first.completed)
        # Append-only: the first run's records are still there.
        rows = list(TrialStore(context.trials_path).read())
        self.assertEqual(len(rows), first.attempted + second.attempted)

    def test_the_cost_guard_stops_before_overspending(self) -> None:
        plan = development_plan()
        context = prepare(
            plan=plan, benchmark=load_mini_benchmark(), repo=REPO_ROOT,
            output_dir=self.tmp_path("out-cost"), benchmark_root=MINI_BENCHMARK,
            pricing=example_snapshot(), mode="development",
        )
        summary = execute(context, adapters={"anthropic": BehaviouralFake()},
                          max_cost_usd=0.02, max_trials=500,
                          require_ripgrep=False)
        self.assertTrue(summary.ceiling_reached)
        self.assertLess(summary.attempted, summary.planned)


@unittest.skipUnless(git_repo_available() and engine_available(),
                     "needs the real checkout and the Engine")
class TestDryRun(TempDirCase):
    def test_dry_run_makes_no_provider_call(self) -> None:
        plan = development_plan()
        context = prepare(
            plan=plan, benchmark=load_mini_benchmark(), repo=REPO_ROOT,
            output_dir=self.tmp_path("out-dry"), benchmark_root=MINI_BENCHMARK,
            pricing=example_snapshot(), mode="development",
        )
        report = dry_run(context, max_cost_usd=100.0, require_ripgrep=False)
        self.assertGreater(report.trial_count, 0)
        self.assertGreaterEqual(report.estimated_cost_usd, 0.0)
        self.assertTrue(report.isolation.passed,
                        [c.detail for c in report.isolation.failures])

    def test_dry_run_flags_an_unaffordable_plan(self) -> None:
        plan = development_plan()
        context = prepare(
            plan=plan, benchmark=load_mini_benchmark(), repo=REPO_ROOT,
            output_dir=self.tmp_path("out-dry2"), benchmark_root=MINI_BENCHMARK,
            pricing=example_snapshot(), mode="development",
        )
        report = dry_run(context, max_cost_usd=0.0001, require_ripgrep=False)
        self.assertFalse(report.within_ceiling)
        self.assertTrue(any("exceeds the ceiling" in w for w in report.warnings))


@unittest.skipUnless(
    git_repo_available() and engine_available() and mcp_sdk_available(),
    "condition D needs the MCP SDK installed")
class TestConditionDLive(TempDirCase):
    """Condition D against a real ``pae mcp`` process."""

    def test_four_tools_and_a_working_call(self) -> None:
        from pae_eval.pae_conditions import MCP_TOOL_NAMES, McpSession
        from pae_eval.snapshot import build_snapshot

        snapshot = build_snapshot(REPO_ROOT, self.tmp_path("snap"))
        with McpSession(snapshot.root) as session:
            session.assert_expected_tools()
            self.assertEqual(
                sorted(t["name"] for t in session.tools), sorted(MCP_TOOL_NAMES))
            call = session.call("pae_route_task", {"task": "review an API design"})
            self.assertEqual(call.status, "ok")
            self.assertGreater(call.bytes_returned, 0)
            self.assertTrue(session.catalog_hash().startswith("sha256:"))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
