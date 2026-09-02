"""Multiple-comparison control.

One pre-declared primary comparison, which is *not* corrected — correcting a
single pre-registered endpoint is a category error. The secondary inferential
family gets Holm–Bonferroni. Everything else is exploratory and is labelled as
such so it cannot be quoted as a finding (spec §68).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence


@dataclass(frozen=True)
class AdjustedTest:
    name: str
    raw_p: float
    adjusted_p: float
    significant: bool

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "raw_p": self.raw_p,
            "adjusted_p": self.adjusted_p,
            "significant": self.significant,
        }


def holm_bonferroni(p_values: Mapping[str, float], alpha: float = 0.05
                    ) -> list[AdjustedTest]:
    """Holm–Bonferroni step-down adjustment.

    Adjusted values are made monotone non-decreasing in rank order, which is
    what keeps a later test from appearing more significant than an earlier one
    it should dominate.
    """
    if not p_values:
        return []
    ordered = sorted(p_values.items(), key=lambda kv: (kv[1], kv[0]))
    m = len(ordered)
    adjusted: list[AdjustedTest] = []
    running = 0.0
    for index, (name, raw) in enumerate(ordered):
        value = min(1.0, (m - index) * raw)
        running = max(running, value)
        adjusted.append(AdjustedTest(
            name=name, raw_p=raw, adjusted_p=running, significant=running <= alpha,
        ))
    return adjusted


@dataclass(frozen=True)
class ComparisonFamily:
    """A declared family of comparisons and how it may be read."""

    name: str
    role: str  # "primary" | "secondary" | "exploratory"
    corrected: bool

    def to_json_obj(self) -> dict[str, Any]:
        return {"name": self.name, "role": self.role, "corrected": self.corrected}


def classify_families(secondary_names: Sequence[str],
                      exploratory_names: Sequence[str]) -> list[ComparisonFamily]:
    families = [ComparisonFamily("primary", "primary", corrected=False)]
    families += [ComparisonFamily(n, "secondary", corrected=True) for n in secondary_names]
    families += [ComparisonFamily(n, "exploratory", corrected=False)
                 for n in exploratory_names]
    return families
