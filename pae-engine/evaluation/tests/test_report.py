"""Report neutrality.

The generator must describe a positive, null and negative result with the same
template and the same prominence. These tests render all three from fixed
analyses and assert the wording follows the numbers — in particular that a
null result never acquires directional language, and a negative result says so
plainly rather than reaching for a silver lining.
"""

from __future__ import annotations

import re
import unittest

from _support import TempDirCase

from pae_eval.plan import example_plan
from pae_eval.report import claim_sentence, render_markdown

#: Matched on word boundaries, not as substrings: "gain" occurs inside
#: "against", and a test that cannot tell those apart fails on its own prose.
POSITIVE_WORDS = ("improve", "improved", "improves", "win", "wins", "better",
                  "outperform", "outperforms", "success", "gain", "gains",
                  "beat", "beats", "superior")


def positive_words_in(text: str) -> list[str]:
    return [
        word for word in POSITIVE_WORDS
        if re.search(rf"\b{re.escape(word)}\b", text, re.IGNORECASE)
    ]


def analysis(*, d_rate: float, b_rate: float, lower: float, upper: float,
             p_value: float = 0.05, token_reduction: float | None = None,
             non_inferior: bool = True, claim_supported: bool = False) -> dict:
    return {
        "schema_version": "pae-eval-analysis/1",
        "evaluation_version": "1.0.0-test",
        "plan_sha256": "sha256:" + "0" * 64,
        "mode": "development",
        "primary": {
            "primary_contrast": ["D", "B"],
            "n_tasks": 150,
            "repeat_strategy": "first_repeat_confirmatory",
            "D_pass_rate": d_rate,
            "B_pass_rate": b_rate,
            "absolute_difference": d_rate - b_rate,
            "ci": {"point_estimate": d_rate - b_rate, "ci_lower": lower,
                   "ci_upper": upper, "ci_level": 0.95, "resamples": 10000,
                   "seed": 1},
            "mcnemar": {"test": "exact_mcnemar", "n_pairs": 150, "discordant": 30,
                        "b_first_only": 20, "c_second_only": 10,
                        "p_value": p_value},
            "minimum_meaningful_effect": 0.10,
            "meets_minimum_meaningful_effect": lower >= 0.10,
        },
        "primary_accounting": {"paired_tasks": 150, "incomplete_pairs": []},
        "primary_model": {"provider": "fake", "model": "fake-model-1"},
        "robustness_model": None,
        "secondary": {"continuous_rubric_score": None, "holm_bonferroni": [],
                      "policy": "holm_bonferroni_on_secondary"},
        "efficiency": {
            "B": {"n": 150, "total_tokens": 10000.0, "input_tokens": 9000.0,
                  "output_tokens": 1000.0, "tool_calls": 6.0, "latency_ms": 5000.0,
                  "cost_usd": 0.3},
            "D": {"n": 150, "total_tokens": 7000.0, "input_tokens": 6000.0,
                  "output_tokens": 1000.0, "tool_calls": 3.0, "latency_ms": 3000.0,
                  "cost_usd": 0.2},
        },
        "efficiency_claim": {
            "quality_non_inferiority": {"margin": -0.05, "ci_lower": lower,
                                        "quality_non_inferior": non_inferior},
            "token_reduction": token_reduction,
            "target_token_reduction": 0.20,
            "claim_supported": claim_supported,
            "note": "gate note",
        },
        "retrieval": None,
        "judge_reliability": None,
        "failures": {"planned_trials": 600, "recorded_trials": 600,
                     "total_attempts": 610, "states": {"completed": 600},
                     "error_classes": {}, "provider_refusals": 0,
                     "infrastructure_failures": 0, "timeouts": 0,
                     "turn_budget_exhausted": 0, "invalid_tool_calls": 0},
        "condition_a_sensitivity": {"tasks_with_condition_a": 150,
                                    "tasks_condition_a_passed": 12,
                                    "low_discrimination_task_ids": [],
                                    "note": "Retained in the primary analysis."},
        "exploratory": {"note": "Exploratory.", "per_task_class": {}},
    }


class TestPositiveResult(unittest.TestCase):
    def setUp(self) -> None:
        self.plan = example_plan()
        self.markdown = render_markdown(
            analysis(d_rate=0.71, b_rate=0.58, lower=0.04, upper=0.22),
            plan=self.plan)

    def test_it_reports_the_direction(self) -> None:
        self.assertIn("excludes zero", self.markdown)

    def test_it_reports_the_interval(self) -> None:
        self.assertIn("+4.0 pp", self.markdown)
        self.assertIn("+22.0 pp", self.markdown)

    def test_it_does_not_claim_the_mme_when_the_bound_is_below_it(self) -> None:
        self.assertIn("does not clear the", self.markdown)


class TestNullResult(unittest.TestCase):
    def setUp(self) -> None:
        self.plan = example_plan()
        self.markdown = render_markdown(
            analysis(d_rate=0.60, b_rate=0.58, lower=-0.06, upper=0.10),
            plan=self.plan)

    def test_it_says_the_run_does_not_distinguish(self) -> None:
        self.assertIn("does not distinguish", self.markdown)

    def test_it_uses_no_directional_language(self) -> None:
        summary = self.markdown.split("## Evaluation design")[0]
        self.assertEqual(
            positive_words_in(summary), [],
            "a null summary must not acquire directional language",
        )


class TestNegativeResult(unittest.TestCase):
    def setUp(self) -> None:
        self.plan = example_plan()
        self.markdown = render_markdown(
            analysis(d_rate=0.45, b_rate=0.62, lower=-0.28, upper=-0.06),
            plan=self.plan)

    def test_it_states_the_loss_plainly(self) -> None:
        self.assertIn("performed worse", self.markdown)

    def test_it_has_no_positive_spin(self) -> None:
        summary = self.markdown.split("## Evaluation design")[0]
        self.assertEqual(
            positive_words_in(summary), [],
            "a negative summary must not reach for a silver lining",
        )

    def test_the_negative_report_has_every_section(self) -> None:
        for section in ("Executive summary", "Primary endpoint", "Efficiency",
                        "Failure accounting", "Limitations", "Reproduction"):
            self.assertIn(f"## {section}", self.markdown)


class TestCheaperButWorse(unittest.TestCase):
    def test_no_efficiency_claim_without_the_quality_gate(self) -> None:
        markdown = render_markdown(
            analysis(d_rate=0.40, b_rate=0.62, lower=-0.30, upper=-0.10,
                     token_reduction=0.45, non_inferior=False,
                     claim_supported=False),
            plan=example_plan())
        self.assertIn("No efficiency claim is made", markdown)
        self.assertIn("quality non-inferiority gate did not pass", markdown)

    def test_a_supported_efficiency_claim_is_stated(self) -> None:
        markdown = render_markdown(
            analysis(d_rate=0.62, b_rate=0.60, lower=-0.01, upper=0.06,
                     token_reduction=0.30, non_inferior=True,
                     claim_supported=True),
            plan=example_plan())
        self.assertIn("met the pre-registered efficiency target", markdown)


class TestDisclosures(unittest.TestCase):
    def test_a_development_run_is_labelled(self) -> None:
        markdown = render_markdown(
            analysis(d_rate=0.7, b_rate=0.5, lower=0.1, upper=0.3),
            plan=example_plan(mode="development"))
        self.assertIn("Development run", markdown)

    def test_a_fixture_report_carries_the_marker(self) -> None:
        markdown = render_markdown(
            analysis(d_rate=0.7, b_rate=0.5, lower=0.1, upper=0.3),
            plan=example_plan(), is_fixture=True)
        self.assertIn("SYNTHETIC TEST FIXTURE", markdown)

    def test_single_family_limitation_is_stated(self) -> None:
        markdown = render_markdown(
            analysis(d_rate=0.7, b_rate=0.5, lower=0.1, upper=0.3),
            plan=example_plan())
        self.assertIn("cannot separate", markdown)

    def test_nondeterminism_is_always_disclosed(self) -> None:
        markdown = render_markdown(
            analysis(d_rate=0.7, b_rate=0.5, lower=0.1, upper=0.3),
            plan=example_plan())
        self.assertIn("nondeterministic", markdown)


class TestClaimSentence(unittest.TestCase):
    def test_no_claim_for_a_development_run(self) -> None:
        self.assertIsNone(claim_sentence(
            analysis(d_rate=0.71, b_rate=0.58, lower=0.05, upper=0.22),
            plan=example_plan(mode="development"), manifest={}))

    def test_no_claim_when_the_interval_straddles_zero(self) -> None:
        self.assertIsNone(claim_sentence(
            analysis(d_rate=0.60, b_rate=0.58, lower=-0.06, upper=0.10),
            plan=example_plan(mode="sealed"), manifest={}))

    def test_no_claim_for_a_negative_result(self) -> None:
        self.assertIsNone(claim_sentence(
            analysis(d_rate=0.45, b_rate=0.62, lower=-0.28, upper=-0.06),
            plan=example_plan(mode="sealed"), manifest={}))

    def test_a_supported_claim_names_everything_required(self) -> None:
        sentence = claim_sentence(
            analysis(d_rate=0.71, b_rate=0.58, lower=0.05, upper=0.22),
            plan=example_plan(mode="sealed"),
            manifest={"pae_commit": "abcdef1234567890"})
        self.assertIsNotNone(sentence)
        for required in ("tasks", "commit" if "commit" in sentence else "abcdef",
                         "95% CI", "repeat"):
            self.assertIn(required, sentence)

    def test_no_bare_accuracy_field_is_ever_produced(self) -> None:
        sentence = claim_sentence(
            analysis(d_rate=0.71, b_rate=0.58, lower=0.05, upper=0.22),
            plan=example_plan(mode="sealed"),
            manifest={"pae_commit": "abcdef1234567890"}) or ""
        self.assertNotIn("PAE accuracy", sentence)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
