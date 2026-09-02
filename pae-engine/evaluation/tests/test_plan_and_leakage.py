"""The freeze protocol and the leakage gates.

Both are pre-registration made checkable. The plan hash makes "we decided this
in advance" verifiable; the leakage gates make "the benchmark is independent"
measurable instead of asserted.
"""

from __future__ import annotations

import json
import unittest

from _support import REPO_ROOT, TempDirCase, git_repo_available, load_mini_benchmark

from pae_eval.errors import FrozenPlanError, ValidationError
from pae_eval.leakage import (
    LeakageCorpus,
    audit_benchmark,
    audit_task,
    containment,
    id_tail_tokens,
    jaccard,
    normalize_tokens,
)
from pae_eval.plan import (
    EvaluationPlan,
    ModelConfig,
    assert_matches_world,
    example_plan,
    validate_plan,
)


# --------------------------------------------------------------------------
# plan
# --------------------------------------------------------------------------


class TestPlanHashing(TempDirCase):
    def test_the_hash_is_stable(self) -> None:
        self.assertEqual(example_plan().sha256, example_plan().sha256)

    def test_any_change_changes_the_hash(self) -> None:
        from dataclasses import replace

        base = example_plan()
        for field, value in (("randomization_seed", 1),
                             ("minimum_meaningful_effect_pp", 5.0),
                             ("repeat_strategy", "all_repeats_must_pass")):
            self.assertNotEqual(base.sha256, replace(base, **{field: value}).sha256,
                                field)

    def test_write_emits_a_sidecar_digest(self) -> None:
        path = self.tmp_path("plan.json")
        digest = example_plan().write(path)
        sidecar = path.with_suffix(".json.sha256")
        self.assertTrue(sidecar.exists())
        self.assertEqual(sidecar.read_text(encoding="utf-8").strip(), digest)

    def test_a_written_plan_round_trips(self) -> None:
        path = self.tmp_path("plan2.json")
        original = example_plan()
        original.write(path)
        self.assertEqual(EvaluationPlan.load(path).sha256, original.sha256)

    def test_editing_a_frozen_plan_is_detectable(self) -> None:
        path = self.tmp_path("plan3.json")
        digest = example_plan().write(path)
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["minimum_meaningful_effect_pp"] = 1.0
        path.write_text(json.dumps(payload), encoding="utf-8")
        self.assertNotEqual(EvaluationPlan.load(path).sha256, digest)


class TestPlanValidation(unittest.TestCase):
    def test_the_example_plan_is_valid(self) -> None:
        self.assertEqual(validate_plan(example_plan()), [])

    def test_the_primary_comparison_must_be_run(self) -> None:
        from dataclasses import replace

        plan = replace(example_plan(), conditions=("A", "C"))
        problems = validate_plan(plan)
        self.assertTrue(any("does not run" in p for p in problems))

    def test_a_primary_family_is_required(self) -> None:
        from dataclasses import replace

        plan = replace(example_plan(), models=(
            ModelConfig(provider="openai", model="m", role="robustness"),))
        self.assertTrue(any("primary" in p for p in validate_plan(plan)))

    def test_same_family_judging_is_flagged(self) -> None:
        from dataclasses import replace

        from pae_eval.plan import JudgeConfig

        plan = replace(example_plan(),
                       judge=JudgeConfig(provider="anthropic", model="j"))
        self.assertTrue(any("participant family" in p for p in validate_plan(plan)))

    def test_a_sealed_plan_must_pin_everything(self) -> None:
        plan = example_plan(mode="sealed")
        problems = validate_plan(plan)
        for pinned in ("benchmark_sha256", "pae_commit",
                       "participant_snapshot_sha256", "pricing_snapshot_sha256"):
            self.assertTrue(any(pinned in p for p in problems), pinned)

    def test_credentials_in_a_model_config_are_refused(self) -> None:
        with self.assertRaises(ValidationError):
            ModelConfig.from_json_obj(
                {"provider": "anthropic", "model": "m", "api_key": "sk-secret"})

    def test_a_positive_non_inferiority_margin_is_refused(self) -> None:
        from dataclasses import replace

        plan = replace(example_plan(), non_inferiority_margin_pp=5.0)
        self.assertTrue(any("negative or zero" in p for p in validate_plan(plan)))


class TestFrozenPlanEnforcement(unittest.TestCase):
    def test_a_sealed_mismatch_refuses_execution(self) -> None:
        from dataclasses import replace

        plan = replace(example_plan(mode="sealed"),
                       benchmark_sha256="sha256:frozen", pae_commit="abc")
        with self.assertRaises(FrozenPlanError) as caught:
            assert_matches_world(plan, benchmark_sha256="sha256:different",
                                 pae_commit="abc")
        self.assertIn("new evaluation version", str(caught.exception))

    def test_development_mode_warns_instead_of_refusing(self) -> None:
        from dataclasses import replace

        plan = replace(example_plan(mode="development"),
                       benchmark_sha256="sha256:frozen")
        mismatches = assert_matches_world(plan, benchmark_sha256="sha256:different")
        self.assertTrue(mismatches)

    def test_a_tool_catalog_change_is_caught(self) -> None:
        from dataclasses import replace

        plan = replace(example_plan(mode="sealed"),
                       benchmark_sha256="b", pae_commit="c",
                       participant_snapshot_sha256="s",
                       tool_catalog_sha256={"D": "sha256:frozen"})
        with self.assertRaises(FrozenPlanError):
            assert_matches_world(plan, tool_catalog_sha256={"D": "sha256:changed"})

    def test_a_matching_world_passes(self) -> None:
        from dataclasses import replace

        plan = replace(example_plan(mode="sealed"),
                       benchmark_sha256="b", pae_commit="c",
                       participant_snapshot_sha256="s")
        self.assertEqual(
            assert_matches_world(plan, benchmark_sha256="b", pae_commit="c",
                                 snapshot_sha256="s"), [])


# --------------------------------------------------------------------------
# leakage
# --------------------------------------------------------------------------


class TestTokenization(unittest.TestCase):
    def test_stopwords_and_short_tokens_are_dropped(self) -> None:
        tokens = normalize_tokens("How do I review the API for a security problem?")
        self.assertNotIn("the", tokens)
        self.assertNotIn("do", tokens)
        self.assertIn("review", tokens)
        self.assertIn("security", tokens)

    def test_case_and_unicode_are_normalized(self) -> None:
        self.assertEqual(normalize_tokens("Résumé REVIEW"),
                         normalize_tokens("résumé review"))

    def test_jaccard_bounds(self) -> None:
        self.assertEqual(jaccard(set(), {"a"}), 0.0)
        self.assertEqual(jaccard({"a"}, {"a"}), 1.0)

    def test_containment(self) -> None:
        self.assertEqual(containment({"a", "b"}, {"a", "b", "c"}), 1.0)
        self.assertEqual(containment({"a", "z"}, {"a"}), 0.5)

    def test_id_tail_tokens(self) -> None:
        tokens = id_tail_tokens("prompt:software-engineering/api/api-rest-design-review")
        self.assertIn("rest", tokens)
        self.assertIn("design", tokens)
        self.assertNotIn("software", tokens)


class TestLeakageAudit(unittest.TestCase):
    def corpus(self) -> LeakageCorpus:
        return LeakageCorpus(
            records={"pae_x": {"id": "prompt:a/b/api-rest-design-review",
                               "title": "API REST design review",
                               "description": "Review a REST API design."}},
            tuning_queries=("review a rest api design for security problems",),
            routing_phrases=("review my rest api design",),
        )

    def task(self, query: str, uids=("pae_x",), mode="natural_external"):
        from pae_eval.benchmark import AcceptableResource, Task

        return Task(
            task_id="t", benchmark_version="1", task_class="ordinary_task",
            query=query, deliverable="d", criteria=(),
            scored_dimensions=("resource",),
            acceptable_resource_uids=tuple(
                AcceptableResource(uid=u) for u in uids),
            label_provenance={"authoring_mode": mode},
        )

    def test_full_title_containment_is_detected(self) -> None:
        audit = audit_task(self.task("api rest design review please"), self.corpus())
        self.assertTrue(audit.title_token_containment)

    def test_id_tail_containment_is_detected(self) -> None:
        audit = audit_task(self.task("api rest design review"), self.corpus())
        self.assertTrue(audit.id_tail_containment)

    def test_an_independent_query_scores_low(self) -> None:
        audit = audit_task(
            self.task("my endpoints keep leaking customer records"), self.corpus())
        self.assertLess(audit.query_target_overlap, 0.5)
        self.assertFalse(audit.title_token_containment)

    def test_a_duplicate_of_a_tuning_query_is_flagged(self) -> None:
        audit = audit_task(
            self.task("review a rest api design for security problems"),
            self.corpus())
        self.assertIsNotNone(audit.exact_duplicate_of)

    def test_gates_fail_a_leaky_benchmark(self) -> None:
        tasks = [self.task("api rest design review")]
        report = audit_benchmark(tasks, self.corpus())
        self.assertFalse(report.passed)
        self.assertTrue(any("title" in v for v in report.violations))

    def test_gates_pass_a_clean_benchmark(self) -> None:
        tasks = [self.task("my endpoints keep leaking customer records")]
        self.assertTrue(audit_benchmark(tasks, self.corpus()).passed)

    def test_tunable_thresholds_come_from_the_plan_not_a_constant(self) -> None:
        # Trips title/id containment but is not a verbatim copy of any phrase.
        tasks = [self.task("api rest design review of my checkout service")]
        self.assertFalse(audit_benchmark(tasks, self.corpus()).passed)
        permissive = audit_benchmark(tasks, self.corpus(), thresholds={
            "title_token_containment_max": 5, "id_tail_containment_max": 5,
            "median_target_overlap_max": 1.0,
            "median_target_overlap_masked_derived_max": 1.0,
            "routing_reference_jaccard_share_max": 1.0,
        })
        self.assertTrue(permissive.passed, permissive.violations)

    def test_exact_duplication_is_unconditional(self) -> None:
        """No threshold may permit a task that is verbatim a tuning phrase.

        The tunable gates trade off strictness against corpus vocabulary. A
        task copied word for word out of the tuning set is not a matter of
        degree, so it is a violation whatever the plan says.
        """
        tasks = [self.task("review my rest api design")]
        wide_open = audit_benchmark(tasks, self.corpus(), thresholds={
            "title_token_containment_max": 99, "id_tail_containment_max": 99,
            "median_target_overlap_max": 1.0,
            "median_target_overlap_masked_derived_max": 1.0,
            "routing_reference_jaccard_share_max": 1.0,
        })
        self.assertFalse(wide_open.passed)
        self.assertTrue(any("duplicate" in v for v in wide_open.violations))

    def test_the_masked_derived_stratum_is_measured_separately(self) -> None:
        tasks = [
            self.task("something unrelated entirely", mode="natural_external"),
            self.task("api rest design review", mode="masked_resource_derived"),
        ]
        report = audit_benchmark(tasks, self.corpus())
        self.assertIn("median_target_overlap_masked_derived", report.metrics)


@unittest.skipUnless(git_repo_available(), "needs the real checkout")
class TestCorpusFromRepo(unittest.TestCase):
    def test_it_loads_the_real_corpus(self) -> None:
        corpus = LeakageCorpus.from_repo(REPO_ROOT)
        self.assertGreater(len(corpus.records), 1000)
        self.assertGreater(len(corpus.routing_phrases), 100)
        self.assertGreater(len(corpus.tuning_queries), 50)

    def test_the_fixture_benchmark_is_clean_against_the_real_corpus(self) -> None:
        corpus = LeakageCorpus.from_repo(REPO_ROOT)
        report = audit_benchmark(load_mini_benchmark().tasks, corpus)
        self.assertEqual(report.metrics["title_token_containment_count"], 0)
        self.assertEqual(report.metrics["id_tail_containment_count"], 0)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
