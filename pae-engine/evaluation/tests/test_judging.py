"""Scoring: deterministic rules, the pass endpoint, and judge blinding.

The endpoint rule that matters: a judge's opinion can never rescue a
deterministic required failure. If the required elements are absent, the task
failed, however impressed the judge was.
"""

from __future__ import annotations

import unittest

from _support import load_mini_benchmark

from pae_eval.errors import IsolationError
from pae_eval.judging import (
    Judge,
    OpaqueAnswer,
    assert_judge_family_separation,
    available_rules,
    build_absolute_payload,
    build_pairwise_payload,
    deterministic_weight_share,
    parse_json_object,
    resolve_pairwise_winner,
    run_rule,
    score_task,
)
from pae_eval.errors import UsageError
from pae_eval.providers.fake import FakeAdapter, text_step


class TestDeterministicRules(unittest.TestCase):
    def rule(self, kind, args, answer, context=None):
        return run_rule({"kind": kind, "args": args}, answer, context or {})

    def test_contains_all(self) -> None:
        self.assertTrue(self.rule("contains_all", {"strings": ["Summary"]},
                                  "Summary\n\nbody").passed)
        self.assertFalse(self.rule("contains_all", {"strings": ["Summary"]},
                                   "no heading").passed)

    def test_contains_none(self) -> None:
        self.assertFalse(self.rule("contains_none", {"strings": ["TODO"]},
                                   "TODO finish").passed)

    def test_min_length(self) -> None:
        self.assertFalse(self.rule("min_length", {"words": 20}, "too short").passed)
        self.assertTrue(self.rule("min_length", {"words": 2}, "long enough").passed)

    def test_valid_json_with_required_fields(self) -> None:
        good = '```json\n{"a": 1, "b": 2}\n```'
        self.assertTrue(self.rule("valid_json", {"required_fields": ["a"]}, good).passed)
        self.assertFalse(self.rule("valid_json", {"required_fields": ["z"]},
                                   good).passed)

    def test_invalid_json_fails(self) -> None:
        self.assertFalse(self.rule("valid_json", {}, "not json at all").passed)

    def test_has_sections(self) -> None:
        answer = "# Summary\ntext\n## Risks\nmore"
        self.assertTrue(self.rule("has_sections", {"sections": ["Summary", "Risks"]},
                                  answer).passed)
        self.assertFalse(self.rule("has_sections", {"sections": ["Appendix"]},
                                   answer).passed)

    def test_absolute_paths_are_caught(self) -> None:
        for leak in ("/home/jane/secrets.md", r"C:\Users\jane\gold.json",
                     r"\\server\share\x"):
            self.assertFalse(self.rule("no_absolute_paths", {}, f"see {leak}").passed,
                             leak)

    def test_ordinary_relative_paths_are_not_flagged(self) -> None:
        self.assertTrue(
            self.rule("no_absolute_paths", {}, "see domain-x/readme.md").passed)

    def test_gold_leakage_is_caught(self) -> None:
        context = {"acceptable_resource_uids": ["pae_secret_uid"]}
        self.assertFalse(
            self.rule("no_gold_leakage", {}, "the answer is pae_secret_uid",
                      context).passed)

    def test_tool_use_constraints(self) -> None:
        context = {"observable_tool_calls": [{"tool": "repo_read"}] * 5}
        self.assertFalse(self.rule("tool_use_within", {"max_calls": 3}, "", context).passed)
        self.assertTrue(self.rule("tool_use_within", {"max_calls": 10}, "", context).passed)
        self.assertFalse(
            self.rule("tool_use_within", {"forbidden_tools": ["repo_read"]},
                      "", context).passed)

    def test_an_unknown_rule_kind_is_an_error(self) -> None:
        from pae_eval.errors import ValidationError

        with self.assertRaises(ValidationError):
            run_rule({"kind": "invent_a_rule", "args": {}}, "x", {})

    def test_the_rule_catalog_is_stable(self) -> None:
        self.assertIn("contains_all", available_rules())
        self.assertIn("no_absolute_paths", available_rules())


class TestPassEndpoint(unittest.TestCase):
    def setUp(self) -> None:
        self.benchmark = load_mini_benchmark()
        self.task = self.benchmark.tasks[0]

    def trial(self, answer: str, **kw) -> dict:
        base = {"trial_id": "t1", "task_id": self.task.task_id, "condition": "D",
                "final_answer": answer, "observable_tool_calls": []}
        base.update(kw)
        return base

    def test_a_good_answer_passes(self) -> None:
        answer = ("Summary\n\n" + "word " * 40)
        score = score_task(self.task, trial=self.trial(answer))
        self.assertTrue(score.passed)

    def test_a_missing_required_element_fails(self) -> None:
        score = score_task(self.task, trial=self.trial("word " * 40))
        self.assertFalse(score.passed)
        self.assertIn("required_elements", score.required_failures)

    def test_a_judge_cannot_rescue_a_required_failure(self) -> None:
        """The whole point of deterministic-first scoring."""
        payload = {"criteria": {
            "correctness": {"score": 1.0, "passed": True, "evidence": "great"},
            "completeness": {"score": 1.0, "passed": True, "evidence": "great"},
        }}
        score = score_task(self.task, trial=self.trial("word " * 40),
                           judge_payload=payload)
        self.assertFalse(score.passed)

    def test_a_failure_gate_blocks_the_pass(self) -> None:
        answer = "Summary\n\n" + "word " * 40 + " see /home/jane/secret.md"
        score = score_task(self.task, trial=self.trial(answer))
        self.assertFalse(score.passed)
        self.assertIn("format_gate", score.gate_failures)

    def test_a_fabrication_flag_blocks_the_pass(self) -> None:
        answer = "Summary\n\n" + "word " * 40
        score = score_task(self.task, trial=self.trial(answer),
                           judge_payload={"fabrication_flagged": True})
        self.assertFalse(score.passed)

    def test_a_missing_judge_verdict_scores_zero_rather_than_vanishing(self) -> None:
        answer = "Summary\n\n" + "word " * 40
        score = score_task(self.task, trial=self.trial(answer), judge_payload={})
        judged = [c for c in score.criteria if c.type == "judge"]
        self.assertTrue(judged)
        self.assertTrue(all(c.source == "missing" and c.score == 0.0 for c in judged))

    def test_continuous_score_is_bounded(self) -> None:
        answer = "Summary\n\n" + "word " * 40
        score = score_task(self.task, trial=self.trial(answer))
        self.assertGreaterEqual(score.continuous_score, 0.0)
        self.assertLessEqual(score.continuous_score, 1.0)

    def test_deterministic_weight_share_is_reported(self) -> None:
        share = deterministic_weight_share(self.benchmark.tasks)
        self.assertGreater(share, 0.5)
        self.assertLessEqual(share, 1.0)


class TestJudgeBlinding(unittest.TestCase):
    def setUp(self) -> None:
        self.task = load_mini_benchmark().tasks[0]

    def test_the_payload_contains_no_condition_label(self) -> None:
        answer = OpaqueAnswer.create("trial-1", "Summary text")
        payload = build_absolute_payload(self.task, answer)
        for label in ("condition A", "condition B", "condition C", "condition D"):
            self.assertNotIn(label, payload)

    def test_answer_ids_are_opaque(self) -> None:
        answer = OpaqueAnswer.create("trial-abc", "text")
        self.assertTrue(answer.answer_id.startswith("ans_"))
        self.assertNotIn("trial-abc", answer.answer_id)

    def test_a_leaked_condition_label_is_refused(self) -> None:
        answer = OpaqueAnswer.create("t", "I used condition D tools to answer.")
        with self.assertRaises(IsolationError):
            build_absolute_payload(self.task, answer)

    def test_a_leaked_pae_tool_name_is_refused(self) -> None:
        answer = OpaqueAnswer.create("t", "I called pae_route_task first.")
        with self.assertRaises(IsolationError):
            build_absolute_payload(self.task, answer)

    def test_pairwise_payload_labels_only_left_and_right(self) -> None:
        left = OpaqueAnswer.create("t1", "answer one")
        right = OpaqueAnswer.create("t2", "answer two")
        payload = build_pairwise_payload(self.task, left, right)
        self.assertIn("LEFT", payload)
        self.assertIn("RIGHT", payload)
        self.assertNotIn("condition", payload.lower().replace("conditions", ""))


class TestJudgeAdapter(unittest.TestCase):
    def setUp(self) -> None:
        self.task = load_mini_benchmark().tasks[0]

    def test_absolute_scoring_parses_a_json_verdict(self) -> None:
        verdict_json = ('{"criteria": {"correctness": {"score": 0.8, '
                        '"passed": true, "evidence": "ok"}}, '
                        '"fabrication_flagged": false}')
        judge = Judge(FakeAdapter([text_step(verdict_json)]), "fake-model-1")
        verdict = judge.score_absolute(self.task, OpaqueAnswer.create("t", "answer"))
        self.assertTrue(verdict.ok)
        self.assertEqual(verdict.payload["criteria"]["correctness"]["score"], 0.8)

    def test_a_fenced_json_block_is_accepted(self) -> None:
        fenced = '```json\n{"criteria": {}, "fabrication_flagged": false}\n```'
        judge = Judge(FakeAdapter([text_step(fenced)]), "fake-model-1")
        self.assertTrue(judge.score_absolute(
            self.task, OpaqueAnswer.create("t", "a")).ok)

    def test_unparseable_output_is_recorded_not_guessed(self) -> None:
        judge = Judge(FakeAdapter([text_step("I think it was pretty good!")]),
                      "fake-model-1")
        verdict = judge.score_absolute(self.task, OpaqueAnswer.create("t", "a"))
        self.assertFalse(verdict.ok)
        self.assertIn("parseable", verdict.error or "")

    def test_the_judge_is_never_given_tools(self) -> None:
        adapter = FakeAdapter([text_step('{"criteria": {}}')])
        Judge(adapter, "fake-model-1").score_absolute(
            self.task, OpaqueAnswer.create("t", "a"))
        self.assertEqual(adapter.requests[0].tools, ())

    def test_pairwise_verdict_maps_back_only_after_storage(self) -> None:
        judge = Judge(FakeAdapter([text_step('{"winner": "left", "reason": "r"}')]),
                      "fake-model-1")
        verdict = judge.compare_pairwise(
            self.task, OpaqueAnswer.create("t1", "one"),
            OpaqueAnswer.create("t2", "two"))
        self.assertEqual(verdict.payload["winner"], "left")
        self.assertEqual(
            resolve_pairwise_winner(verdict, left_condition="D", right_condition="B"),
            "D")

    def test_an_invalid_winner_is_unjudgeable(self) -> None:
        judge = Judge(FakeAdapter([text_step('{"winner": "the first one"}')]),
                      "fake-model-1")
        verdict = judge.compare_pairwise(
            self.task, OpaqueAnswer.create("a", "x"), OpaqueAnswer.create("b", "y"))
        self.assertFalse(verdict.ok)
        self.assertIsNone(resolve_pairwise_winner(
            verdict, left_condition="D", right_condition="B"))


class TestFamilySeparation(unittest.TestCase):
    def test_same_family_is_refused_by_default(self) -> None:
        with self.assertRaises(UsageError):
            assert_judge_family_separation("anthropic", "anthropic")

    def test_cross_family_is_fine(self) -> None:
        assert_judge_family_separation("anthropic", "openai")

    def test_same_family_can_be_opted_into_explicitly(self) -> None:
        assert_judge_family_separation("anthropic", "anthropic", allow_same=True)


class TestJsonExtraction(unittest.TestCase):
    def test_bare_object(self) -> None:
        self.assertEqual(parse_json_object('{"a": 1}'), {"a": 1})

    def test_object_with_prose_around_it(self) -> None:
        self.assertEqual(parse_json_object('Here you go:\n{"a": 1}\nHope that helps'),
                         {"a": 1})

    def test_non_object_is_none(self) -> None:
        self.assertIsNone(parse_json_object("[1, 2, 3]"))
        self.assertIsNone(parse_json_object("no json here"))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
