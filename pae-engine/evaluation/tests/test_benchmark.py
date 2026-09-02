"""Benchmark schema and label semantics.

The rule worth defending: an empty acceptable-list is never ambiguous.
``acceptable_scopes: []`` could mean "no scope is correct" or "scope is not
graded here", and a scorer that guesses marks a whole stratum wrong without
anyone noticing. ``scored_dimensions`` decides, and a mismatch is a validation
error rather than a silent default.
"""

from __future__ import annotations

import json
import unittest
from copy import deepcopy

from _support import MINI_BENCHMARK, TempDirCase, load_mini_benchmark

from pae_eval.benchmark import (
    Benchmark,
    Task,
    collapse_clusters,
    composition_report,
    expects_no_route,
    load_benchmark,
    resource_is_correct,
    route_status_is_correct,
    validate_benchmark,
)
from pae_eval.errors import ValidationError


def base_task(**overrides) -> dict:
    task = {
        "task_id": "t-1", "benchmark_version": "1.0.0", "class": "ordinary_task",
        "query": "do the thing", "deliverable": "a note",
        "rubric": {"criteria": [
            {"criterion_id": "req", "description": "d", "type": "deterministic",
             "weight": 1.0, "required": True,
             "deterministic_rule": {"kind": "min_length", "args": {"words": 1}}},
        ]},
        "scored_dimensions": [], "acceptable_resource_uids": [],
        "acceptable_scopes": [], "acceptable_kinds": [],
        "acceptable_route_statuses": [],
        "canonical_policy": "canonical_or_registered_copy_both_credited",
        "label_rationale": "because", "label_provenance": {
            "authoring_mode": "natural_external",
            "author": {"kind": "human"}, "reviewer": {"kind": "human"},
        },
        "leakage_audit": {}, "tags": [],
    }
    task.update(overrides)
    return Task.from_json_obj(task)


def bench(*tasks) -> Benchmark:
    return Benchmark(version="1.0.0", tasks=tuple(tasks))


class TestScoredDimensions(unittest.TestCase):
    def test_scored_dimension_with_no_values_is_an_error(self) -> None:
        task = base_task(scored_dimensions=["scope"], acceptable_scopes=[])
        problems = validate_benchmark(bench(task))
        self.assertTrue(any("scored_dimensions" in p and "empty" in p
                            for p in problems))

    def test_values_for_an_unscored_dimension_are_an_error(self) -> None:
        task = base_task(scored_dimensions=[], acceptable_scopes=["finance"])
        problems = validate_benchmark(bench(task))
        self.assertTrue(any("unscored dimension" in p for p in problems))

    def test_a_consistent_task_validates(self) -> None:
        task = base_task(scored_dimensions=["scope"], acceptable_scopes=["finance"])
        self.assertEqual(validate_benchmark(bench(task)), [])

    def test_scores_helper(self) -> None:
        task = base_task(scored_dimensions=["scope"], acceptable_scopes=["finance"])
        self.assertTrue(task.scores("scope"))
        self.assertFalse(task.scores("resource"))


class TestLabelSemantics(unittest.TestCase):
    def test_a_registered_copy_earns_credit(self) -> None:
        task = base_task(
            scored_dimensions=["resource"],
            acceptable_resource_uids=[{"uid": "pae_canonical", "grade": "primary"}],
        )
        clusters = {"pae_canonical": "c1", "pae_copy": "c1", "pae_other": "c2"}
        self.assertTrue(resource_is_correct(task, "pae_copy", clusters))
        self.assertFalse(resource_is_correct(task, "pae_other", clusters))

    def test_canonical_only_policy_refuses_the_copy(self) -> None:
        task = base_task(
            scored_dimensions=["resource"], canonical_policy="canonical_only",
            acceptable_resource_uids=[{"uid": "pae_canonical", "grade": "primary"}],
        )
        clusters = {"pae_canonical": "c1", "pae_copy": "c1"}
        self.assertFalse(resource_is_correct(task, "pae_copy", clusters))

    def test_clusters_collapse_without_double_credit(self) -> None:
        clusters = {"a": "c1", "b": "c1", "c": "c2"}
        self.assertEqual(collapse_clusters(["a", "b", "c"], clusters), ["a", "c"])

    def test_ambiguous_only_makes_confident_matching_wrong(self) -> None:
        task = base_task(scored_dimensions=["route_status"],
                         acceptable_route_statuses=["ambiguous"])
        self.assertTrue(route_status_is_correct(task, "ambiguous"))
        self.assertFalse(route_status_is_correct(task, "matched"))

    def test_ambiguous_or_matched_accepts_both(self) -> None:
        task = base_task(scored_dimensions=["route_status"],
                         acceptable_route_statuses=["ambiguous", "matched"])
        self.assertTrue(route_status_is_correct(task, "matched"))
        self.assertTrue(route_status_is_correct(task, "ambiguous"))

    def test_no_route_tasks_are_recognized(self) -> None:
        task = base_task(scored_dimensions=["route_status"],
                         acceptable_route_statuses=["weak", "no_route"])
        self.assertTrue(expects_no_route(task))
        self.assertTrue(route_status_is_correct(task, "no_route"))
        self.assertFalse(route_status_is_correct(task, "matched"))

    def test_a_no_route_task_may_not_also_demand_a_resource(self) -> None:
        task = base_task(
            scored_dimensions=["route_status", "resource"],
            acceptable_route_statuses=["no_route"],
            acceptable_resource_uids=[{"uid": "pae_x", "grade": "primary"}],
        )
        problems = validate_benchmark(bench(task))
        self.assertTrue(any("declining to route" in p for p in problems))

    def test_unscored_route_status_is_always_correct(self) -> None:
        task = base_task()
        self.assertTrue(route_status_is_correct(task, "anything"))


class TestRubricValidation(unittest.TestCase):
    def test_weights_must_sum_to_one(self) -> None:
        task = base_task(rubric={"criteria": [
            {"criterion_id": "a", "description": "d", "type": "deterministic",
             "weight": 0.5, "required": True,
             "deterministic_rule": {"kind": "min_length", "args": {"words": 1}}},
        ]})
        self.assertTrue(any("sum to" in p for p in validate_benchmark(bench(task))))

    def test_a_task_needs_at_least_one_required_criterion(self) -> None:
        task = base_task(rubric={"criteria": [
            {"criterion_id": "a", "description": "d", "type": "deterministic",
             "weight": 1.0, "required": False,
             "deterministic_rule": {"kind": "min_length", "args": {"words": 1}}},
        ]})
        self.assertTrue(any("required" in p for p in validate_benchmark(bench(task))))

    def test_a_deterministic_criterion_needs_a_rule(self) -> None:
        task = base_task(rubric={"criteria": [
            {"criterion_id": "a", "description": "d", "type": "deterministic",
             "weight": 1.0, "required": True},
        ]})
        self.assertTrue(any("deterministic_rule" in p
                            for p in validate_benchmark(bench(task))))

    def test_a_judge_criterion_needs_an_instruction(self) -> None:
        task = base_task(rubric={"criteria": [
            {"criterion_id": "a", "description": "d", "type": "judge",
             "weight": 1.0, "required": True},
        ]})
        self.assertTrue(any("judge_instruction" in p
                            for p in validate_benchmark(bench(task))))


class TestProvenance(unittest.TestCase):
    def test_ai_authorship_must_be_fully_recorded(self) -> None:
        task = base_task(label_provenance={
            "authoring_mode": "natural_external",
            "author": {"kind": "ai"},
            "reviewer": {"kind": "human"},
        })
        problems = validate_benchmark(bench(task))
        for field in ("provider", "model", "date", "prompt_sha256",
                      "saw_pae_metadata"):
            self.assertTrue(any(field in p for p in problems), field)

    def test_missing_authoring_mode_is_an_error(self) -> None:
        task = base_task(label_provenance={"author": {"kind": "human"},
                                           "reviewer": {"kind": "human"}})
        self.assertTrue(any("authoring_mode" in p
                            for p in validate_benchmark(bench(task))))

    def test_provenance_can_be_waived_for_fixtures(self) -> None:
        task = base_task(label_provenance={})
        self.assertEqual(
            validate_benchmark(bench(task), require_provenance=False), [])


class TestDuplicateIds(unittest.TestCase):
    def test_duplicate_task_ids_are_caught(self) -> None:
        problems = validate_benchmark(bench(base_task(), base_task()))
        self.assertTrue(any("duplicate task_id" in p for p in problems))


class TestMiniBenchmarkFixture(unittest.TestCase):
    def test_it_loads_and_validates(self) -> None:
        benchmark = load_mini_benchmark()
        self.assertEqual(len(benchmark), 6)
        self.assertEqual(validate_benchmark(benchmark), [])

    def test_it_is_labelled_as_a_fixture(self) -> None:
        manifest = json.loads(
            (MINI_BENCHMARK / "manifest.json").read_text(encoding="utf-8"))
        self.assertTrue(manifest.get("fixture"))
        self.assertIn("SYNTHETIC TEST FIXTURE", manifest.get("disclosure", ""))

    def test_the_hash_is_stable_across_loads(self) -> None:
        self.assertEqual(load_mini_benchmark().sha256, load_mini_benchmark().sha256)

    def test_composition_report(self) -> None:
        report = composition_report(load_mini_benchmark())
        self.assertEqual(report["task_count"], 6)
        self.assertIn("weak_no_route", report["class_distribution"])
        self.assertEqual(report["tagged_adversarial_governance"], 1)


class TestLoading(TempDirCase):
    def test_an_empty_benchmark_directory_is_refused(self) -> None:
        root = self.tmp_path("bench")
        (root / "tasks").mkdir(parents=True, exist_ok=True)
        with self.assertRaises(ValidationError):
            load_benchmark(root)

    def test_malformed_json_is_reported_with_the_file_name(self) -> None:
        root = self.tmp_path("bench2")
        (root / "tasks").mkdir(parents=True, exist_ok=True)
        (root / "tasks" / "broken.json").write_text("{ not json", encoding="utf-8")
        with self.assertRaises(ValidationError) as caught:
            load_benchmark(root)
        self.assertIn("broken.json", str(caught.exception))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
