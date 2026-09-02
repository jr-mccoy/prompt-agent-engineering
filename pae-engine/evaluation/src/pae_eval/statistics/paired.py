"""Paired analysis for the primary and secondary endpoints.

The primary endpoint is a paired binary: for each task, did condition D pass and
did condition B pass. Exact McNemar tests it; a paired bootstrap gives the
interval that actually gets reported. The p-value is secondary — the confidence
interval is the number a reader should take away.

Two rules are enforced structurally rather than by convention:

**The unit of analysis is the task.** Repeats are aggregated to one value per
task before anything is tested. Treating repeats as independent observations
would inflate n by the repeat count and shrink every interval accordingly, which
is the single easiest way to manufacture a significant result.

**Aggregation is chosen in advance.** With two repeats a majority vote can tie,
and inventing a tie rule after seeing the data is exactly the degree of freedom
pre-registration exists to remove. The strategies are named, and the example
plan uses the first pre-scheduled repeat as confirmatory (spec §66, §109).

The exact McNemar test and the bootstrap are implemented on the standard
library so the primary endpoint runs everywhere. Wilcoxon is delegated to SciPy
under the ``analysis`` extra rather than hand-rolled, because ties and zeros are
where hand-rolled implementations quietly go wrong.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from ..errors import UsageError

# --------------------------------------------------------------------------
# repeat aggregation
# --------------------------------------------------------------------------


def aggregate_repeats(outcomes: Sequence[bool], strategy: str) -> bool | None:
    """Collapse one task-condition's repeats into the confirmatory value.

    Returns ``None`` when the strategy cannot decide, which the caller must
    treat as a missing pair rather than a failure.
    """
    values = [bool(o) for o in outcomes]
    if not values:
        return None
    if strategy == "first_repeat_confirmatory":
        return values[0]
    if strategy == "all_repeats_must_pass":
        return all(values)
    if strategy == "any_repeat_passes":
        return any(values)
    if strategy == "mean_pass_proportion":
        # Not a binary endpoint; callers wanting this should use the continuous
        # path. Refusing here beats silently thresholding at 0.5.
        raise UsageError(
            "'mean_pass_proportion' is a continuous endpoint; use "
            "paired_continuous() rather than the binary primary"
        )
    raise UsageError(f"unknown repeat strategy: {strategy!r}")


def mean_pass_proportion(outcomes: Sequence[bool]) -> float | None:
    values = [1.0 if o else 0.0 for o in outcomes]
    return sum(values) / len(values) if values else None


# --------------------------------------------------------------------------
# exact McNemar
# --------------------------------------------------------------------------


def _binom_coeff(n: int, k: int) -> int:
    return math.comb(n, k)


def exact_binomial_two_sided(successes: int, trials: int, p: float = 0.5) -> float:
    """Two-sided exact binomial p-value.

    Uses the "sum of outcomes no more likely than the observed" definition,
    which is the standard exact two-sided construction and, unlike doubling the
    one-sided tail, cannot exceed 1 or misbehave on asymmetric cases.
    """
    if trials <= 0:
        return 1.0
    if not 0 < p < 1:
        raise UsageError("p must be strictly between 0 and 1")

    def pmf(k: int) -> float:
        return _binom_coeff(trials, k) * (p ** k) * ((1 - p) ** (trials - k))

    observed = pmf(successes)
    # Floating tolerance: without it, the symmetric partner of the observed
    # count is excluded and every symmetric case reports half the correct value.
    tolerance = observed * (1 + 1e-9)
    total = sum(pmf(k) for k in range(trials + 1) if pmf(k) <= tolerance)
    return min(1.0, total)


@dataclass(frozen=True)
class McNemarResult:
    b: int  # first condition passed, second failed
    c: int  # first failed, second passed
    n_pairs: int
    p_value: float
    discordant: int

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "test": "exact_mcnemar",
            "n_pairs": self.n_pairs,
            "discordant": self.discordant,
            "b_first_only": self.b,
            "c_second_only": self.c,
            "p_value": self.p_value,
        }


def mcnemar_exact(first: Sequence[bool], second: Sequence[bool]) -> McNemarResult:
    """Exact McNemar on paired binary outcomes.

    ``first`` and ``second`` are aligned per task. Concordant pairs carry no
    information about the difference and are excluded from the test by
    construction — that is what makes it a *paired* test.
    """
    if len(first) != len(second):
        raise UsageError("paired sequences must be the same length")
    b = sum(1 for x, y in zip(first, second) if x and not y)
    c = sum(1 for x, y in zip(first, second) if y and not x)
    discordant = b + c
    p = 1.0 if discordant == 0 else exact_binomial_two_sided(b, discordant, 0.5)
    return McNemarResult(b=b, c=c, n_pairs=len(first), p_value=p, discordant=discordant)


# --------------------------------------------------------------------------
# paired bootstrap
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class BootstrapCI:
    point: float
    lower: float
    upper: float
    level: float
    resamples: int
    seed: int

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "point_estimate": self.point,
            "ci_lower": self.lower,
            "ci_upper": self.upper,
            "ci_level": self.level,
            "resamples": self.resamples,
            "seed": self.seed,
        }


def paired_bootstrap_ci(
    first: Sequence[float],
    second: Sequence[float],
    *,
    resamples: int = 10000,
    level: float = 0.95,
    seed: int = 0,
) -> BootstrapCI:
    """Percentile bootstrap CI for the paired mean difference (first - second).

    Resampling is over *tasks*, not observations: a task is drawn with both its
    values together, which is what preserves the pairing.
    """
    if len(first) != len(second):
        raise UsageError("paired sequences must be the same length")
    n = len(first)
    if n == 0:
        return BootstrapCI(0.0, 0.0, 0.0, level, resamples, seed)

    diffs = [float(a) - float(b) for a, b in zip(first, second)]
    point = sum(diffs) / n
    if n == 1:
        return BootstrapCI(point, point, point, level, resamples, seed)

    rng = random.Random(seed)
    means: list[float] = []
    for _ in range(resamples):
        total = 0.0
        for _ in range(n):
            total += diffs[rng.randrange(n)]
        means.append(total / n)
    means.sort()

    alpha = (1.0 - level) / 2.0
    lower = means[max(0, int(math.floor(alpha * resamples)))]
    upper = means[min(resamples - 1, int(math.ceil((1 - alpha) * resamples)) - 1)]
    return BootstrapCI(point, lower, upper, level, resamples, seed)


# --------------------------------------------------------------------------
# primary endpoint
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class PrimaryResult:
    first_condition: str
    second_condition: str
    first_pass_rate: float
    second_pass_rate: float
    absolute_difference: float
    ci: BootstrapCI
    mcnemar: McNemarResult
    n_tasks: int
    repeat_strategy: str
    minimum_meaningful_effect: float | None = None

    @property
    def meets_mme(self) -> bool | None:
        """Whether the CI lower bound clears the pre-registered effect.

        Deliberately strict: a point estimate above the MME with an interval
        straddling it has not demonstrated the effect.
        """
        if self.minimum_meaningful_effect is None:
            return None
        return self.ci.lower >= self.minimum_meaningful_effect

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "primary_contrast": [self.first_condition, self.second_condition],
            "n_tasks": self.n_tasks,
            "repeat_strategy": self.repeat_strategy,
            f"{self.first_condition}_pass_rate": round(self.first_pass_rate, 6),
            f"{self.second_condition}_pass_rate": round(self.second_pass_rate, 6),
            "absolute_difference": round(self.absolute_difference, 6),
            "ci": self.ci.to_json_obj(),
            "mcnemar": self.mcnemar.to_json_obj(),
            "minimum_meaningful_effect": self.minimum_meaningful_effect,
            "meets_minimum_meaningful_effect": self.meets_mme,
        }


def primary_endpoint(
    paired: Mapping[str, tuple[bool, bool]],
    *,
    first_condition: str,
    second_condition: str,
    repeat_strategy: str = "first_repeat_confirmatory",
    resamples: int = 10000,
    seed: int = 0,
    level: float = 0.95,
    minimum_meaningful_effect: float | None = None,
) -> PrimaryResult:
    """The confirmatory analysis, from ``task_id -> (first_pass, second_pass)``."""
    task_ids = sorted(paired)
    firsts = [bool(paired[t][0]) for t in task_ids]
    seconds = [bool(paired[t][1]) for t in task_ids]
    n = len(task_ids)

    first_rate = sum(firsts) / n if n else 0.0
    second_rate = sum(seconds) / n if n else 0.0
    ci = paired_bootstrap_ci(
        [1.0 if v else 0.0 for v in firsts],
        [1.0 if v else 0.0 for v in seconds],
        resamples=resamples, level=level, seed=seed,
    )
    return PrimaryResult(
        first_condition=first_condition,
        second_condition=second_condition,
        first_pass_rate=first_rate,
        second_pass_rate=second_rate,
        absolute_difference=first_rate - second_rate,
        ci=ci,
        mcnemar=mcnemar_exact(firsts, seconds),
        n_tasks=n,
        repeat_strategy=repeat_strategy,
        minimum_meaningful_effect=minimum_meaningful_effect,
    )


# --------------------------------------------------------------------------
# secondary continuous endpoint
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class ContinuousResult:
    mean_difference: float
    median_difference: float
    ci: BootstrapCI
    wilcoxon_statistic: float | None
    wilcoxon_p_value: float | None
    wilcoxon_available: bool
    n_tasks: int

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "mean_difference": round(self.mean_difference, 6),
            "median_difference": round(self.median_difference, 6),
            "ci": self.ci.to_json_obj(),
            "wilcoxon": {
                "available": self.wilcoxon_available,
                "statistic": self.wilcoxon_statistic,
                "p_value": self.wilcoxon_p_value,
                "note": (
                    None if self.wilcoxon_available
                    else "install the 'analysis' extra (scipy) for Wilcoxon"
                ),
            },
            "n_tasks": self.n_tasks,
        }


def scipy_available() -> bool:
    try:
        import scipy.stats  # noqa: F401
    except ImportError:
        return False
    return True


def paired_continuous(
    first: Sequence[float],
    second: Sequence[float],
    *,
    resamples: int = 10000,
    seed: int = 0,
    level: float = 0.95,
    require_wilcoxon: bool = False,
) -> ContinuousResult:
    """Paired continuous comparison with a bootstrap CI and Wilcoxon.

    Wilcoxon comes from SciPy or not at all. A hand-rolled version that mishandles
    zero differences and tied ranks produces a plausible number that is wrong,
    which is worse than an honest "not available".
    """
    if len(first) != len(second):
        raise UsageError("paired sequences must be the same length")
    diffs = [float(a) - float(b) for a, b in zip(first, second)]
    n = len(diffs)
    mean = sum(diffs) / n if n else 0.0
    ordered = sorted(diffs)
    if n == 0:
        med = 0.0
    elif n % 2:
        med = ordered[n // 2]
    else:
        med = (ordered[n // 2 - 1] + ordered[n // 2]) / 2.0

    ci = paired_bootstrap_ci(first, second, resamples=resamples, level=level, seed=seed)

    statistic: float | None = None
    p_value: float | None = None
    available = scipy_available()
    if available and n and any(d != 0 for d in diffs):
        from scipy.stats import wilcoxon  # noqa: PLC0415

        result = wilcoxon(list(first), list(second), zero_method="wilcox",
                          alternative="two-sided")
        statistic = float(result.statistic)
        p_value = float(result.pvalue)
    elif require_wilcoxon and not available:
        raise UsageError(
            "this analysis requires the Wilcoxon signed-rank test; install the "
            "evaluation project's 'analysis' extra (scipy) and re-run"
        )

    return ContinuousResult(
        mean_difference=mean, median_difference=med, ci=ci,
        wilcoxon_statistic=statistic, wilcoxon_p_value=p_value,
        wilcoxon_available=available, n_tasks=n,
    )


# --------------------------------------------------------------------------
# non-inferiority gate (spec §69)
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class NonInferiorityResult:
    margin: float
    ci_lower: float
    passed: bool

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "margin": self.margin,
            "ci_lower": round(self.ci_lower, 6),
            "quality_non_inferior": self.passed,
        }


def non_inferiority(ci: BootstrapCI, margin: float) -> NonInferiorityResult:
    """Quality non-inferiority: the CI lower bound must clear the margin.

    An efficiency win reported without this gate is not a result — it is the
    observation that a worse answer is cheaper.
    """
    return NonInferiorityResult(margin=margin, ci_lower=ci.lower, passed=ci.lower > margin)


# --------------------------------------------------------------------------
# power / sample-size planning (spec §71)
# --------------------------------------------------------------------------


def detectable_effect(n_tasks: int, *, discordance: float = 0.22,
                      alpha: float = 0.05, power: float = 0.80) -> float:
    """Approximate detectable absolute difference for a paired binary design.

    A normal approximation to McNemar, adequate for *planning*. It is never
    used for inference — the reported test is exact.
    """
    if n_tasks <= 0 or discordance <= 0:
        return 1.0
    z_alpha = 1.959963984540054  # two-sided 0.05
    z_beta = {0.80: 0.8416212335729143, 0.90: 1.2815515655446004}.get(power, 0.8416212335729143)
    n_discordant = n_tasks * discordance
    if n_discordant <= 0:
        return 1.0
    # Solve (b-c)/n for the smallest detectable imbalance among discordant pairs.
    return min(1.0, (z_alpha + z_beta) * math.sqrt(discordance / n_tasks))


def ci_half_width(n_tasks: int, *, pass_rate: float = 0.5, level: float = 0.95) -> float:
    """Approximate half-width of a proportion CI, for planning tables."""
    if n_tasks <= 0:
        return 1.0
    z = 1.959963984540054 if abs(level - 0.95) < 1e-9 else 1.6448536269514722
    return min(1.0, z * math.sqrt(max(pass_rate * (1 - pass_rate), 1e-9) / n_tasks))
