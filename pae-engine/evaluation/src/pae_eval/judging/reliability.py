"""Judge reliability metrics and calibration gates.

A judge is an instrument, and an uncalibrated instrument produces numbers with
no error bar. These metrics are measured on the development set *before* the
sealed run, and the plan's thresholds are gates: failing calibration blocks the
run rather than being noted in the limitations afterwards (spec §64).

All implemented on the standard library. Weighted kappa and Spearman are short
enough to write correctly and to check against hand-computed fixtures, which is
what the known-answer tests do.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from ..constants import EXAMPLE_JUDGE_THRESHOLDS
from ..errors import UsageError


# --------------------------------------------------------------------------
# agreement
# --------------------------------------------------------------------------


def _bucket(value: float, buckets: int) -> int:
    """Map a continuous score in [0, 1] onto an ordinal category."""
    clamped = max(0.0, min(1.0, float(value)))
    index = int(clamped * buckets)
    return min(buckets - 1, index)


def weighted_kappa(first: Sequence[float], second: Sequence[float], *,
                   buckets: int = 5, weighting: str = "quadratic") -> float:
    """Cohen's kappa with linear or quadratic disagreement weights.

    Returns 1.0 for perfect agreement, 0.0 for chance-level, negative for worse
    than chance. Continuous scores are bucketed first, because kappa is defined
    on categories.
    """
    if len(first) != len(second):
        raise UsageError("rating sequences must be the same length")
    n = len(first)
    if n == 0:
        return 0.0

    a = [_bucket(v, buckets) for v in first]
    b = [_bucket(v, buckets) for v in second]

    observed = [[0.0] * buckets for _ in range(buckets)]
    for x, y in zip(a, b):
        observed[x][y] += 1.0 / n

    row = [sum(observed[i]) for i in range(buckets)]
    col = [sum(observed[i][j] for i in range(buckets)) for j in range(buckets)]
    expected = [[row[i] * col[j] for j in range(buckets)] for i in range(buckets)]

    denominator = (buckets - 1) ** (2 if weighting == "quadratic" else 1)
    if denominator == 0:
        return 1.0

    def weight(i: int, j: int) -> float:
        diff = abs(i - j)
        return (diff ** 2 if weighting == "quadratic" else diff) / denominator

    numerator_o = sum(weight(i, j) * observed[i][j]
                      for i in range(buckets) for j in range(buckets))
    numerator_e = sum(weight(i, j) * expected[i][j]
                      for i in range(buckets) for j in range(buckets))
    if numerator_e == 0:
        return 1.0 if numerator_o == 0 else 0.0
    return 1.0 - numerator_o / numerator_e


def cohen_kappa(first: Sequence[Any], second: Sequence[Any]) -> float:
    """Unweighted kappa for nominal labels (e.g. pass/fail)."""
    if len(first) != len(second):
        raise UsageError("rating sequences must be the same length")
    n = len(first)
    if n == 0:
        return 0.0
    labels = sorted({*map(str, first), *map(str, second)})
    index = {label: i for i, label in enumerate(labels)}
    size = len(labels)
    matrix = [[0.0] * size for _ in range(size)]
    for x, y in zip(first, second):
        matrix[index[str(x)]][index[str(y)]] += 1.0 / n
    observed = sum(matrix[i][i] for i in range(size))
    row = [sum(matrix[i]) for i in range(size)]
    col = [sum(matrix[i][j] for i in range(size)) for j in range(size)]
    expected = sum(row[i] * col[i] for i in range(size))
    if expected >= 1.0:
        return 1.0 if observed >= 1.0 else 0.0
    return (observed - expected) / (1.0 - expected)


def _ranks(values: Sequence[float]) -> list[float]:
    """Average ranks, so ties do not distort the correlation."""
    order = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    position = 0
    while position < len(order):
        end = position
        while end + 1 < len(order) and values[order[end + 1]] == values[order[position]]:
            end += 1
        average = (position + end) / 2.0 + 1.0
        for k in range(position, end + 1):
            ranks[order[k]] = average
        position = end + 1
    return ranks


def spearman_rho(first: Sequence[float], second: Sequence[float]) -> float:
    """Spearman rank correlation, tie-aware."""
    if len(first) != len(second):
        raise UsageError("sequences must be the same length")
    n = len(first)
    if n < 2:
        return 0.0
    a, b = _ranks(list(first)), _ranks(list(second))
    mean_a, mean_b = sum(a) / n, sum(b) / n
    numerator = sum((x - mean_a) * (y - mean_b) for x, y in zip(a, b))
    denom_a = sum((x - mean_a) ** 2 for x in a) ** 0.5
    denom_b = sum((y - mean_b) ** 2 for y in b) ** 0.5
    if denom_a == 0 or denom_b == 0:
        return 0.0
    return numerator / (denom_a * denom_b)


def pearson_r(first: Sequence[float], second: Sequence[float]) -> float:
    n = len(first)
    if n < 2 or len(second) != n:
        return 0.0
    mean_a, mean_b = sum(first) / n, sum(second) / n
    numerator = sum((x - mean_a) * (y - mean_b) for x, y in zip(first, second))
    denom_a = sum((x - mean_a) ** 2 for x in first) ** 0.5
    denom_b = sum((y - mean_b) ** 2 for y in second) ** 0.5
    if denom_a == 0 or denom_b == 0:
        return 0.0
    return numerator / (denom_a * denom_b)


# --------------------------------------------------------------------------
# bias measures
# --------------------------------------------------------------------------


def position_flip_rate(forward: Sequence[str], reversed_order: Sequence[str]) -> float:
    """Share of pairs whose winner changes when the sides are swapped.

    ``forward`` and ``reversed_order`` are winners already mapped back to
    conditions. A judge with no position bias returns the same winner both ways,
    so a high flip rate means the instrument is reading the layout, not the
    answers.
    """
    if len(forward) != len(reversed_order):
        raise UsageError("sequences must be the same length")
    comparable = [
        (a, b) for a, b in zip(forward, reversed_order)
        if a is not None and b is not None
    ]
    if not comparable:
        return 0.0
    flips = sum(1 for a, b in comparable if a != b)
    return flips / len(comparable)


def verbosity_correlation(scores: Sequence[float], answers: Sequence[str]) -> float:
    """Correlation between answer length and score.

    Not zero-by-right — a longer answer is sometimes genuinely better — but a
    large value means length is doing the judging.
    """
    lengths = [float(len(a.split())) for a in answers]
    return pearson_r(list(scores), lengths)


def self_consistency(repeated: Sequence[Sequence[float]], *, buckets: int = 5) -> float:
    """Mean pairwise weighted kappa across repeated gradings of the same items."""
    passes = [list(p) for p in repeated if p]
    if len(passes) < 2:
        return 1.0
    values: list[float] = []
    for i in range(len(passes)):
        for j in range(i + 1, len(passes)):
            values.append(weighted_kappa(passes[i], passes[j], buckets=buckets))
    return sum(values) / len(values) if values else 1.0


# --------------------------------------------------------------------------
# calibration report and gate
# --------------------------------------------------------------------------


@dataclass
class ReliabilityReport:
    metrics: Mapping[str, float]
    thresholds: Mapping[str, float]
    violations: tuple[str, ...]
    measured_on: str = "development"

    @property
    def passed(self) -> bool:
        return not self.violations

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "measured_on": self.measured_on,
            "metrics": {k: round(v, 6) for k, v in self.metrics.items()},
            "thresholds": dict(self.thresholds),
            "violations": list(self.violations),
            "passed": self.passed,
        }


def evaluate_reliability(metrics: Mapping[str, float],
                         thresholds: Mapping[str, float] | None = None,
                         *, measured_on: str = "development") -> ReliabilityReport:
    """Apply the frozen calibration gates to measured reliability."""
    gates = {**EXAMPLE_JUDGE_THRESHOLDS, **(thresholds or {})}
    violations: list[str] = []

    def at_least(key: str, label: str) -> None:
        if key in metrics and metrics[key] < float(gates[key]):
            violations.append(
                f"{label} {metrics[key]:.3f} is below the required {gates[key]}"
            )

    at_least("self_consistency_weighted_kappa", "judge self-consistency")
    at_least("inter_judge_weighted_kappa", "inter-judge agreement")
    at_least("manual_review_spearman_rho", "agreement with manual review")

    if "position_flip_rate" in metrics and metrics["position_flip_rate"] > float(
        gates["position_flip_rate_max"]
    ):
        violations.append(
            f"position flip rate {metrics['position_flip_rate']:.3f} exceeds "
            f"{gates['position_flip_rate_max']}"
        )
    if "verbosity_correlation" in metrics and abs(
        metrics["verbosity_correlation"]
    ) > float(gates["verbosity_correlation_abs_max"]):
        violations.append(
            f"verbosity correlation {metrics['verbosity_correlation']:.3f} exceeds "
            f"±{gates['verbosity_correlation_abs_max']}"
        )

    return ReliabilityReport(
        metrics=dict(metrics), thresholds=gates,
        violations=tuple(violations), measured_on=measured_on,
    )
