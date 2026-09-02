"""Statistics, checked against analytically known answers.

Deliberately not "compare the function to itself". Every expected value here is
either computed from the binomial definition with exact integer arithmetic, or
is a case whose answer is forced by the definition (perfect agreement, no
discordance, symmetric split). A statistics module validated only against its
own output is a module that reproduces its own bugs.
"""

from __future__ import annotations

import unittest
from fractions import Fraction
from math import comb

from _support import TempDirCase

from pae_eval.errors import UsageError
from pae_eval.judging.reliability import (
    cohen_kappa,
    evaluate_reliability,
    pearson_r,
    position_flip_rate,
    self_consistency,
    spearman_rho,
    verbosity_correlation,
    weighted_kappa,
)
from pae_eval.statistics import (
    aggregate_repeats,
    exact_binomial_two_sided,
    holm_bonferroni,
    mcnemar_exact,
    non_inferiority,
    paired_bootstrap_ci,
    paired_continuous,
    primary_endpoint,
)


def paired(b: int, c: int, both: int = 0, neither: int = 0):
    """Construct paired outcomes with an exact discordance structure."""
    first = [True] * b + [False] * c + [True] * both + [False] * neither
    second = [False] * b + [True] * c + [True] * both + [False] * neither
    return first, second


class TestExactBinomial(unittest.TestCase):
    def test_symmetric_case_matches_the_doubled_tail(self) -> None:
        # For a symmetric split the two-sided exact value equals 2*P(X<=k).
        expected = Fraction(2 * sum(comb(24, k) for k in range(7)), 2 ** 24)
        got = exact_binomial_two_sided(18, 24, 0.5)
        self.assertAlmostEqual(got, float(expected), places=12)

    def test_all_successes(self) -> None:
        # p = 2 * (1/2)^5
        self.assertAlmostEqual(exact_binomial_two_sided(5, 5, 0.5), 2 * 0.5 ** 5, 12)

    def test_perfectly_balanced_is_one(self) -> None:
        self.assertAlmostEqual(exact_binomial_two_sided(5, 10, 0.5), 1.0, 12)

    def test_zero_trials(self) -> None:
        self.assertEqual(exact_binomial_two_sided(0, 0), 1.0)

    def test_never_exceeds_one(self) -> None:
        for n in range(1, 30):
            for k in range(n + 1):
                self.assertLessEqual(exact_binomial_two_sided(k, n, 0.5), 1.0 + 1e-12)


class TestMcNemar(unittest.TestCase):
    def test_known_discordance(self) -> None:
        first, second = paired(b=18, c=6, both=10)
        result = mcnemar_exact(first, second)
        self.assertEqual((result.b, result.c, result.discordant), (18, 6, 24))
        expected = Fraction(2 * sum(comb(24, k) for k in range(7)), 2 ** 24)
        self.assertAlmostEqual(result.p_value, float(expected), places=12)

    def test_no_discordance_is_p_one(self) -> None:
        result = mcnemar_exact([True] * 5, [True] * 5)
        self.assertEqual(result.discordant, 0)
        self.assertEqual(result.p_value, 1.0)

    def test_symmetric_discordance_is_p_one(self) -> None:
        first, second = paired(b=5, c=5)
        self.assertAlmostEqual(mcnemar_exact(first, second).p_value, 1.0, 12)

    def test_concordant_pairs_do_not_change_the_p_value(self) -> None:
        """The whole point of a paired test: agreements carry no information."""
        a1, b1 = paired(b=8, c=2)
        a2, b2 = paired(b=8, c=2, both=50, neither=50)
        self.assertAlmostEqual(mcnemar_exact(a1, b1).p_value,
                               mcnemar_exact(a2, b2).p_value, 12)

    def test_mismatched_lengths_are_refused(self) -> None:
        with self.assertRaises(UsageError):
            mcnemar_exact([True], [True, False])


class TestBootstrap(unittest.TestCase):
    def test_point_estimate_is_the_paired_mean_difference(self) -> None:
        ci = paired_bootstrap_ci([1.0, 1.0, 0.0], [0.0, 0.0, 0.0],
                                 resamples=500, seed=1)
        self.assertAlmostEqual(ci.point, 2 / 3, places=12)

    def test_identical_inputs_give_a_zero_width_interval(self) -> None:
        ci = paired_bootstrap_ci([1.0] * 8, [1.0] * 8, resamples=500, seed=3)
        self.assertEqual((ci.point, ci.lower, ci.upper), (0.0, 0.0, 0.0))

    def test_seed_is_reproducible(self) -> None:
        args = ([1.0, 0.0, 1.0, 1.0], [0.0, 0.0, 1.0, 0.0])
        a = paired_bootstrap_ci(*args, resamples=800, seed=11)
        b = paired_bootstrap_ci(*args, resamples=800, seed=11)
        self.assertEqual((a.lower, a.upper), (b.lower, b.upper))

    def test_different_seeds_may_differ(self) -> None:
        args = ([1.0, 0.0, 1.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 1.0, 0.0, 1.0])
        a = paired_bootstrap_ci(*args, resamples=800, seed=1)
        b = paired_bootstrap_ci(*args, resamples=800, seed=2)
        self.assertEqual(a.point, b.point)  # the estimate is not random
        self.assertTrue(a.lower <= a.point <= a.upper)
        self.assertTrue(b.lower <= b.point <= b.upper)

    def test_interval_brackets_the_point(self) -> None:
        ci = paired_bootstrap_ci([1, 1, 0, 1, 0, 0, 1, 1], [0, 1, 0, 0, 0, 1, 1, 0],
                                 resamples=1000, seed=5)
        self.assertLessEqual(ci.lower, ci.point)
        self.assertLessEqual(ci.point, ci.upper)


class TestRepeatAggregation(unittest.TestCase):
    def test_first_repeat_confirmatory(self) -> None:
        self.assertTrue(aggregate_repeats([True, False], "first_repeat_confirmatory"))
        self.assertFalse(aggregate_repeats([False, True], "first_repeat_confirmatory"))

    def test_all_must_pass(self) -> None:
        self.assertFalse(aggregate_repeats([True, False], "all_repeats_must_pass"))
        self.assertTrue(aggregate_repeats([True, True], "all_repeats_must_pass"))

    def test_any_passes(self) -> None:
        self.assertTrue(aggregate_repeats([False, True], "any_repeat_passes"))

    def test_mean_proportion_is_refused_for_the_binary_endpoint(self) -> None:
        """Two repeats can tie; the strategy must not silently pick a side."""
        with self.assertRaises(UsageError):
            aggregate_repeats([True, False], "mean_pass_proportion")

    def test_unknown_strategy_is_refused(self) -> None:
        with self.assertRaises(UsageError):
            aggregate_repeats([True], "majority_vote_probably")

    def test_empty_is_undecidable(self) -> None:
        self.assertIsNone(aggregate_repeats([], "first_repeat_confirmatory"))


class TestPrimaryEndpoint(unittest.TestCase):
    def test_rates_and_difference(self) -> None:
        pairs = {f"t{i}": (True, False) for i in range(7)}
        pairs.update({f"u{i}": (False, False) for i in range(3)})
        result = primary_endpoint(pairs, first_condition="D", second_condition="B",
                                  resamples=500, seed=0,
                                  minimum_meaningful_effect=0.10)
        self.assertAlmostEqual(result.first_pass_rate, 0.7)
        self.assertAlmostEqual(result.second_pass_rate, 0.0)
        self.assertAlmostEqual(result.absolute_difference, 0.7)
        self.assertEqual(result.n_tasks, 10)

    def test_mme_requires_the_interval_not_just_the_point(self) -> None:
        # Point estimate is +0.2 but the interval will straddle the MME.
        pairs = {"a": (True, False), "b": (False, False), "c": (False, False),
                 "d": (False, False), "e": (False, False)}
        result = primary_endpoint(pairs, first_condition="D", second_condition="B",
                                  resamples=2000, seed=0,
                                  minimum_meaningful_effect=0.10)
        self.assertAlmostEqual(result.absolute_difference, 0.2)
        self.assertIn(result.meets_mme, (True, False))
        self.assertEqual(result.meets_mme, result.ci.lower >= 0.10)


class TestNonInferiority(unittest.TestCase):
    def test_passes_when_the_lower_bound_clears_the_margin(self) -> None:
        ci = paired_bootstrap_ci([1.0] * 10, [1.0] * 10, resamples=200, seed=0)
        self.assertTrue(non_inferiority(ci, -0.05).passed)

    def test_fails_when_the_lower_bound_is_below(self) -> None:
        ci = paired_bootstrap_ci([0.0] * 10, [1.0] * 10, resamples=200, seed=0)
        self.assertFalse(non_inferiority(ci, -0.05).passed)


class TestHolmBonferroni(unittest.TestCase):
    def test_known_adjustment(self) -> None:
        adjusted = {t.name: t.adjusted_p for t in
                    holm_bonferroni({"a": 0.01, "b": 0.04, "c": 0.03})}
        self.assertAlmostEqual(adjusted["a"], 0.03, places=12)   # 0.01 * 3
        self.assertAlmostEqual(adjusted["c"], 0.06, places=12)   # 0.03 * 2
        self.assertAlmostEqual(adjusted["b"], 0.06, places=12)   # max(0.04*1, 0.06)

    def test_monotone_non_decreasing(self) -> None:
        values = holm_bonferroni({"a": 0.001, "b": 0.2, "c": 0.05, "d": 0.9})
        adjusted = [t.adjusted_p for t in values]
        self.assertEqual(adjusted, sorted(adjusted))

    def test_never_exceeds_one(self) -> None:
        for t in holm_bonferroni({"a": 0.6, "b": 0.7, "c": 0.8}):
            self.assertLessEqual(t.adjusted_p, 1.0)

    def test_empty_family(self) -> None:
        self.assertEqual(holm_bonferroni({}), [])


class TestAgreementMetrics(unittest.TestCase):
    def test_perfect_agreement_is_one(self) -> None:
        values = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertAlmostEqual(weighted_kappa(values, values), 1.0, places=12)

    def test_cohen_kappa_perfect(self) -> None:
        self.assertAlmostEqual(cohen_kappa(["a", "b", "a"], ["a", "b", "a"]), 1.0, 12)

    def test_cohen_kappa_known_value(self) -> None:
        # 2x2 with observed 0.8, expected 0.5 -> kappa = 0.6
        first = ["p"] * 4 + ["n"] * 4 + ["p"] + ["n"]
        second = ["p"] * 4 + ["n"] * 4 + ["n"] + ["p"]
        self.assertAlmostEqual(cohen_kappa(first, second), 0.6, places=10)

    def test_spearman_perfect_monotone(self) -> None:
        self.assertAlmostEqual(spearman_rho([1, 2, 3, 4], [10, 20, 30, 40]), 1.0, 12)

    def test_spearman_perfect_inverse(self) -> None:
        self.assertAlmostEqual(spearman_rho([1, 2, 3, 4], [40, 30, 20, 10]), -1.0, 12)

    def test_spearman_handles_ties(self) -> None:
        self.assertAlmostEqual(spearman_rho([1, 1, 2, 2], [1, 1, 2, 2]), 1.0, 12)

    def test_pearson_perfect(self) -> None:
        self.assertAlmostEqual(pearson_r([1, 2, 3], [2, 4, 6]), 1.0, places=12)

    def test_position_flip_rate(self) -> None:
        self.assertAlmostEqual(
            position_flip_rate(["D", "D", "B", "D"], ["D", "B", "B", "B"]), 0.5, 12)

    def test_no_flips(self) -> None:
        self.assertEqual(position_flip_rate(["D", "B"], ["D", "B"]), 0.0)

    def test_verbosity_correlation_detects_length_bias(self) -> None:
        answers = ["a " * 10, "a " * 20, "a " * 30, "a " * 40]
        self.assertAlmostEqual(
            verbosity_correlation([0.1, 0.2, 0.3, 0.4], answers), 1.0, places=6)

    def test_self_consistency_identical_passes(self) -> None:
        values = [0.0, 0.5, 1.0, 0.5]
        self.assertAlmostEqual(self_consistency([values, values, values]), 1.0, 12)


class TestReliabilityGates(unittest.TestCase):
    def test_good_metrics_pass(self) -> None:
        report = evaluate_reliability({
            "self_consistency_weighted_kappa": 0.9,
            "inter_judge_weighted_kappa": 0.7,
            "manual_review_spearman_rho": 0.8,
            "position_flip_rate": 0.05,
            "verbosity_correlation": 0.1,
        })
        self.assertTrue(report.passed)

    def test_low_agreement_blocks(self) -> None:
        report = evaluate_reliability({"inter_judge_weighted_kappa": 0.2})
        self.assertFalse(report.passed)
        self.assertTrue(any("inter-judge" in v for v in report.violations))

    def test_position_bias_blocks(self) -> None:
        report = evaluate_reliability({"position_flip_rate": 0.5})
        self.assertFalse(report.passed)

    def test_verbosity_bias_blocks_in_both_directions(self) -> None:
        self.assertFalse(evaluate_reliability({"verbosity_correlation": 0.9}).passed)
        self.assertFalse(evaluate_reliability({"verbosity_correlation": -0.9}).passed)


class TestContinuous(unittest.TestCase):
    def test_mean_and_median_difference(self) -> None:
        result = paired_continuous([1.0, 0.5, 0.0], [0.0, 0.5, 0.0],
                                   resamples=200, seed=0)
        self.assertAlmostEqual(result.mean_difference, 0.5 / 1.5, places=6)
        self.assertAlmostEqual(result.median_difference, 0.0, places=12)

    def test_wilcoxon_is_absent_without_scipy_rather_than_wrong(self) -> None:
        result = paired_continuous([1.0, 0.0], [0.0, 1.0], resamples=100, seed=0)
        if not result.wilcoxon_available:
            self.assertIsNone(result.wilcoxon_p_value)
        else:
            self.assertIsNotNone(result.wilcoxon_p_value)

    def test_require_wilcoxon_fails_loudly_when_unavailable(self) -> None:
        from pae_eval.statistics import scipy_available

        if scipy_available():
            self.skipTest("scipy is installed")
        with self.assertRaises(UsageError):
            paired_continuous([1.0, 0.0], [0.0, 1.0], require_wilcoxon=True)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
