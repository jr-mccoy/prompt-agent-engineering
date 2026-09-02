"""Statistical analysis.

The primary endpoint (exact McNemar plus a paired bootstrap CI) runs on the
standard library so it works in any environment. Only the secondary Wilcoxon
test needs SciPy, and it is delegated rather than reimplemented.
"""

from .multiple import AdjustedTest, ComparisonFamily, classify_families, holm_bonferroni
from .paired import (
    BootstrapCI,
    ContinuousResult,
    McNemarResult,
    NonInferiorityResult,
    PrimaryResult,
    aggregate_repeats,
    ci_half_width,
    detectable_effect,
    exact_binomial_two_sided,
    mcnemar_exact,
    mean_pass_proportion,
    non_inferiority,
    paired_bootstrap_ci,
    paired_continuous,
    primary_endpoint,
    scipy_available,
)

__all__ = [
    "AdjustedTest", "ComparisonFamily", "classify_families", "holm_bonferroni",
    "BootstrapCI", "ContinuousResult", "McNemarResult", "NonInferiorityResult",
    "PrimaryResult", "aggregate_repeats", "ci_half_width", "detectable_effect",
    "exact_binomial_two_sided", "mcnemar_exact", "mean_pass_proportion",
    "non_inferiority", "paired_bootstrap_ci", "paired_continuous",
    "primary_endpoint", "scipy_available",
]
